import subprocess
import os

def run_lip_sync(video_path, audio_path, output_path, model_path="Wav2Lip/checkpoints/wav2lip.pth"):
    """
    Runs Wav2Lip lip sync on the video with new hindi audio.

    Args:
        video_path  : path to the input video clip
        audio_path  : path to the hindi audio file
        output_path : path to save the lip synced output video
        model_path  : path to the wav2lip pretrained model
    """

    # extract raw audio from video for wav2lip processing
    print("Extracting audio from clip...")
    subprocess.run(
        f"ffmpeg -i {video_path} -vn -acodec pcm_s16le -ar 16000 -ac 1 temp/clip_audio.wav -y",
        shell=True, capture_output=True
    )

    # run wav2lip inference with hindi audio
    print("Running Wav2Lip lip sync...")
    result = subprocess.run(
        f"python Wav2Lip/inference.py "
        f"--checkpoint_path {model_path} "
        f"--face {video_path} "
        f"--audio {audio_path} "
        f"--outfile {output_path} "
        f"--resize_factor 1",
        shell=True, capture_output=True, text=True
    )

    if result.returncode == 0:
        print(f"Lip sync done! Output saved at: {output_path}")
        return True
    else:
        print("Error:", result.stderr)
        return False


if __name__ == "__main__":
    run_lip_sync(
        video_path="temp/clip_15_30.mp4",
        audio_path="temp/hindi_audio.mp3",
        output_path="output/dubbed_output.mp4"
    )
