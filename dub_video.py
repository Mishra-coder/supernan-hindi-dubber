import subprocess
import os
import json
import argparse
from gtts import gTTS
from googletrans import Translator
import whisper

# ─────────────────────────────────────────
# SUPERNAN HINDI DUBBER - Full Pipeline
# Runs all 5 steps in sequence
# ─────────────────────────────────────────

def extract_clip(input_path, output_path, start_time, duration):
    """Step 1: Extract target clip from source video using ffmpeg."""

    print("[Step 1] Extracting clip...")
    cmd = f"ffmpeg -ss {start_time} -t {duration} -i \"{input_path}\" -c copy {output_path} -y"
    result = subprocess.run(cmd, shell=True, capture_output=True)

    if result.returncode == 0:
        print(f"  Clip saved: {output_path}")
    else:
        raise RuntimeError("FFmpeg clip extraction failed")


def transcribe_audio(video_path, output_path):
    """Step 2: Transcribe speech from video using Whisper medium model."""

    print("[Step 2] Transcribing audio with Whisper...")
    model = whisper.load_model("medium")
    result = model.transcribe(video_path, language="kn", verbose=False)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"  Transcribed: {result['text'][:80]}...")
    return result["text"]


def translate_text(text, output_path):
    """Step 3: Translate Kannada text to Hindi using googletrans."""

    print("[Step 3] Translating to Hindi...")
    translator = Translator()
    translated = translator.translate(text, src="kn", dest="hi")
    hindi_text = translated.text

    result = {"original_text": text, "hindi_text": hindi_text}
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"  Hindi: {hindi_text[:80]}...")
    return hindi_text


def generate_audio(hindi_text, output_path):
    """Step 4: Generate Hindi audio using gTTS.
    
    Note: Coqui XTTS v2 was attempted but is incompatible with Python 3.12.
    gTTS is used as a reliable, free fallback for Hindi speech synthesis.
    """

    print("[Step 4] Generating Hindi audio...")
    tts = gTTS(text=hindi_text, lang="hi", slow=False)
    tts.save(output_path)
    print(f"  Audio saved: {output_path}")


def run_lip_sync(video_path, audio_path, output_path):
    """Step 5: Run Wav2Lip to sync lips with new Hindi audio."""

    print("[Step 5] Running Wav2Lip lip sync...")
    cmd = (
        f"python Wav2Lip/inference.py "
        f"--checkpoint_path Wav2Lip/checkpoints/wav2lip.pth "
        f"--face {video_path} "
        f"--audio {audio_path} "
        f"--outfile {output_path} "
        f"--resize_factor 1"
    )
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"  Lip sync done: {output_path}")
    else:
        raise RuntimeError(f"Wav2Lip failed: {result.stderr}")


def main():
    parser = argparse.ArgumentParser(description="Supernan Hindi Dubber Pipeline")
    parser.add_argument("--input", required=True, help="Path to source video")
    parser.add_argument("--start", type=int, default=15, help="Start time in seconds")
    parser.add_argument("--duration", type=int, default=15, help="Duration in seconds")
    parser.add_argument("--output", default="output/dubbed_output.mp4", help="Output path")
    args = parser.parse_args()

    # create required folders
    os.makedirs("temp", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    # run all pipeline steps in sequence
    extract_clip(args.input, "temp/clip_15_30.mp4", args.start, args.duration)
    kannada_text = transcribe_audio("temp/clip_15_30.mp4", "temp/transcription.json")
    hindi_text = translate_text(kannada_text, "temp/translation.json")
    generate_audio(hindi_text, "temp/hindi_audio.mp3")
    run_lip_sync("temp/clip_15_30.mp4", "temp/hindi_audio.mp3", args.output)

    print("\n Pipeline complete!")
    print(f" Output saved at: {args.output}")


if __name__ == "__main__":
    main()
