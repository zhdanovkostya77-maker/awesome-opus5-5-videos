# Tiny Paws Animation Studio

Two free prototypes for original children's short-form animation.

## 1. Browser preview
Open `index.html` to see the animated bunny. The **Record WebM** button needs a browser with MediaRecorder support; Safari compatibility varies. Browser recording does not include narration.

## 2. Narrated MP4 (new)
`render_short.py` produces a 15-second vertical 360×640 MP4 with original 2D bunny animation, English text, and synthesized US-English narration. It requires Python 3, Pillow, FFmpeg, and eSpeak. On Ubuntu/Debian:

```bash
sudo apt-get install -y ffmpeg espeak python3-pip
python3 -m pip install Pillow
python3 render_short.py
```

The generated `tiny-paws-episode-1.mp4` is saved in the same folder. The voice is robotic; replace it with licensed narration if desired. This is a **2D prototype**, not a photorealistic 3D cartoon. The script has not yet been run in GitHub CI; verify output before publication.

## Content and publishing
Characters, scenery and dialogue are original code-drawn assets, with no reused TikTok clips. For YouTube, mark content as **made for kids** when applicable. No paid API is required.
