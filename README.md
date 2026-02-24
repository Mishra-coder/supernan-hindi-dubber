# Supernan Hindi Dubber

AI pipeline that dubs English videos into Hindi using free, open-source tools.

## Pipeline Flow
```
Input Video
    ↓
FFmpeg  →  Extract 15 sec clip
    ↓
Whisper  →  English speech to text
    ↓
IndicTrans2  →  English to Hindi translation
    ↓
Coqui XTTS v2  →  Hindi voice cloning
    ↓
Wav2Lip + GFPGAN  →  Lip sync + face restore
    ↓
Output: Hindi Dubbed Video
```

## Tools Used

| Task | Tool | Cost |
|------|------|------|
| Clip extraction | FFmpeg | Free |
| Transcription | OpenAI Whisper | Free |
| Translation | IndicTrans2 | Free |
| Voice cloning | Coqui XTTS v2 | Free |
| Lip sync | Wav2Lip | Free |
| Face restore | GFPGAN | Free |

## Setup
```bash
git clone https://github.com/Mishra-coder/supernan-hindi-dubber.git
cd supernan-hindi-dubber
pip install -r requirements.txt
python dub_video.py --input video.mp4 --start 15 --end 30
```

## Estimated Cost at Scale

| Scale | Cost |
|-------|------|
| Colab Free Tier | Rs. 0 |
| 1 min video on AWS T4 | ~Rs. 2.5 |
| 500 hrs overnight on A100 | ~Rs. 8,000 |

## Known Limitations

- XTTS needs minimum 6 sec reference audio for voice cloning
- Wav2Lip slightly blurs face, fixed using GFPGAN
- IndicTrans2 takes ~2 min to load on Colab

## Future Improvements

- Preserve background music separately
- Detect multiple speakers
- Build FastAPI wrapper for production
