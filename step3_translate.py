from googletrans import Translator
import json

def translate_to_hindi(transcription_path="temp/transcription.json",
                        output_path="temp/translation.json"):
    """
    Translates Kannada transcription to Hindi using googletrans.

    Args:
        transcription_path : path to whisper transcription json
        output_path        : path to save hindi translation
    """

    # load transcription saved from previous whisper step
    with open(transcription_path, "r", encoding="utf-8") as f:
        transcription = json.load(f)

    kannada_text = transcription["text"]
    print(f"Original: {kannada_text}")

    # translate kannada to hindi
    translator = Translator()
    translated = translator.translate(kannada_text, src="kn", dest="hi")
    hindi_text = translated.text

    print(f"Hindi: {hindi_text}")

    # save both original and translated text for reference
    result = {
        "original_language": "kn",
        "original_text": kannada_text,
        "hindi_text": hindi_text
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print("Translation saved!")
    return result


if __name__ == "__main__":
    translate_to_hindi()
