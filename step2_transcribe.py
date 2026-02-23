import whisper
import json

def transcribe_audio(video_path, output_path="temp/transcription.json"):
    """
    Transcribes speech from video using OpenAI Whisper large model.

    Args:
        video_path  : path to the video file
        output_path : path to save transcription as json

    Note: Using large model for better accuracy on Indian regional languages.
    Base model was tested but failed on Kannada - large model works correctly.
    """

    # large model gives much better results for Indian languages like Kannada
    print("Loading Whisper large model...")
    model = whisper.load_model("large")

    # transcribe with language explicitly set to kannada
    print("Transcribing audio...")
    result = model.transcribe(
        video_path,
        language="kn",
        verbose=False
    )

    # save full transcription with timestamps to json for next pipeline step
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Language detected: {result[chr(39)]language[chr(39)]}")
    print(f"Transcribed text: {result[chr(39)]text[chr(39)]}")

    return result


if __name__ == "__main__":
    transcribe_audio(
        video_path="temp/clip_15_30.mp4",
        output_path="temp/transcription.json"
    )
