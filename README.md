# Supernan Hindi Dubber

AI pipeline that dubs Kannada videos into Hindi using free, open-source tools.
Built for Supernan AI Automation Intern Assignment.

## Pipeline Flow
```
Input Video
    ↓
FFmpeg  →  Extract 15 sec clip (0:15 - 0:30)
    ↓
Whisper Medium  →  Kannada speech to text
    ↓
googletrans  →  Kannada to Hindi translation
    ↓
gTTS  →  Hindi audio generation
    ↓
Wav2Lip  →  Lip sync with Hindi audio
    ↓
Output: Hindi Dubbed Video
```

## Tools Used

| Task | Tool | Cost |
|------|------|------|
| Clip extraction | FFmpeg | Free |
| Transcription | OpenAI Whisper (medium) | Free |
| Translation | googletrans | Free |
| Hindi audio | gTTS | Free |
| Lip sync | Wav2Lip | Free |
| Runtime | Google Colab T4 GPU | Free |

## Why These Tools?

- **Whisper medium** — large model crashed Colab RAM, medium gave accurate Kannada results
- **googletrans** — lightweight, no API key needed, works well for Kannada to Hindi
- **gTTS** — Coqui XTTS v2 is incompatible with Python 3.12, gTTS is reliable fallback
- **Wav2Lip** — best open source lip sync, runs on free Colab T4 GPU

## Setup & Run
```bash
git clone https://github.com/Mishra-coder/supernan-hindi-dubber.git
cd supernan-hindi-dubber
pip install -r requirements.txt
python dub_video.py --input video.mp4 --start 15 --duration 15
```

## Project Structure
```
supernan-hindi-dubber/
├── dub_video.py            # main pipeline - runs all steps
├── step1_extract_clip.py   # ffmpeg clip extraction
├── step2_transcribe.py     # whisper transcription
├── step3_translate.py      # kannada to hindi translation
├── step4_voice_generate.py # hindi audio generation
├── step5_lip_sync.py       # wav2lip lip sync
├── requirements.txt        # all dependencies
├── input/                  # source video goes here
├── temp/                   # intermediate files
├── output/                 # final dubbed video
└── models/                 # pretrained models
```

## Estimated Cost at Scale

| Scale | Tool | Cost |
|-------|------|------|
| Current (Colab Free T4) | All free tools | Rs. 0 |
| 1 min video on AWS T4 | Spot instance | ~Rs. 2.5 |
| 500 hrs overnight on A100 | Batch processing | ~Rs. 8,000 |

## Scaling to 500 Hours Overnight

1. Split videos into 15-sec chunks using FFmpeg
2. Run parallel jobs on multiple A100 GPUs
3. Use AWS Batch or Google Cloud Run for orchestration
4. Whisper + Wav2Lip both support batch processing
5. Estimated: 10 A100s x 8 hrs = 500 hrs processed overnight

## Known Limitations

- Wav2Lip slightly blurs face around mouth area
- gTTS does not clone original speaker voice
- Whisper medium may miss some Kannada words
- googletrans may timeout on long texts

## What I Would Improve With More Time

- Use GFPGAN for face restoration after Wav2Lip
- Use Coqui XTTS v2 on Python 3.9 for actual voice cloning
- Use IndicTrans2 for better Kannada to Hindi translation
- Add background music preservation using audio separation
- Build FastAPI wrapper for production deployment

<!-- updated -->