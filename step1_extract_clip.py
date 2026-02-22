import subprocess
import os

def extract_clip(input_path, output_path, start_time=15, duration=15):
    """
    Extracts a 15-second clip from the source video.

    Args:
        input_path  : path to the original video
        output_path : path to save the trimmed clip
        start_time  : where to start cutting (in seconds)
        duration    : how long the clip should be (in seconds)
    """

    # make sure input video exists before processing
    if not os.path.exists(input_path):
        print(f"Error: video not found at {input_path}")
        return False

    # -ss = start time, -t = duration, -c copy = no re-encoding (fast)
    command = [
        "ffmpeg",
        "-ss", str(start_time),
        "-t", str(duration),
        "-i", input_path,
        "-c", "copy",
        output_path,
        "-y"
    ]

    print(f"Extracting clip from {start_time}s to {start_time + duration}s ...")
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"Clip saved at: {output_path}")
        return True
    else:
        print("FFmpeg error:", result.stderr)
        return False


if __name__ == "__main__":
    extract_clip(
        input_path="input/Hygiene - Kannada.mp4",
        output_path="temp/clip_15_30.mp4",
        start_time=15,
        duration=15
    )
