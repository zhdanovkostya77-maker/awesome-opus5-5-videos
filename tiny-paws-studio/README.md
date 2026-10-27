# Tiny Paws Animation Studio — Episode 1

Original 20-second vertical 9:16 animated bunny scene, implemented with HTML Canvas. No third-party images, audio, characters, or paid API required.

## Preview
Open `index.html` in a modern browser. Tap **Play / Restart**.

## Export
Use **Record WebM** on desktop Chrome or another browser supporting Canvas capture and MediaRecorder. Recording is silent; English title cards are included. For YouTube Shorts, convert WebM to MP4 using FFmpeg:

```bash
ffmpeg -i tiny-paws-episode-1.webm -c:v libx264 -pix_fmt yuv420p -movflags +faststart tiny-paws-episode-1.mp4
```

This is a simple 2D animated prototype, not a photorealistic 3D render. iPhone Safari may not support WebM recording. No voiceover has been generated yet. Review YouTube's made-for-kids requirements before publishing.
