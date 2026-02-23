from gtts import gTTS
import json
import os

def generate_hindi_audio(translation_path="temp/translation.json",
                          output_path="temp/hindi_audio.mp3"):
    """
    Generates Hindi audio from translated text using gTTS.

    Args:
        translation_path : path to translation json from previous step
        output_path      : path to save generated hindi audio

    Note: Coqui XTTS was attempted for voice cloning but is incompatible
    with Python 3.12. gTTS is used as a reliable fallback for Hindi TTS.
    """

    # load hindi text from translation step
    with open(translation_path, "r", encoding="utf-8") as f:
        translation = json.load(f)

    hindi_text = translation["hindi_text"]
    print(f"Generating audio for: {hindi_text}")

    # generate hindi speech - slow=False for natural speaking speed
    tts = gTTS(text=hindi_text, lang="hi", slow=False)
    tts.save(output_path)

    print(f"Hindi audio saved at: {output_path}")
    return output_path


if __name__ == "__main__":
    generate_hindi_audio()
