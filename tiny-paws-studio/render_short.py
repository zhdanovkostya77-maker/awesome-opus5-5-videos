#!/usr/bin/env python3
"""Generate an original vertical animated short with English narration.
Requires Pillow, ffmpeg, and espeak (all free/open-source).
Usage: python render_short.py
"""
import math, subprocess, shutil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
W,H,FPS,DURATION=360,640,15,15
OUT=Path(__file__).resolve().parent
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def font(size):
    try: return ImageFont.truetype(FONT,size)
    except OSError: return ImageFont.load_default()
def oval(d,xy,fill): d.ellipse(tuple(map(int,xy)),fill=fill)
def draw_frame(t):
    im=Image.new('RGB',(W,H));d=ImageDraw.Draw(im)
    for y in range(H):
        p=y/H
        d.line((0,y,W,y),fill=(int(111+30*p),int(209-27*p),int(248-96*p)))
    oval(d,(248,40,332,124),'#fff1ad')
    for i in range(9):
        x=i*55-35
        oval(d,(x,400+10*math.sin(i),x+115,640),'#6bbf70' if i%2 else '#82cd78')
    for i in range(38):
        x=(i*97)%W;y=490+(i*41)%145;s=4+i%4
        d.line((x,y,x,y+24),fill='#398e51',width=2)
        for a in range(5):
            ang=a*2*math.pi/5
            oval(d,(x+math.cos(ang)*s-5,y+math.sin(ang)*s-5,x+math.cos(ang)*s+5,y+math.sin(ang)*s+5),['#ff7caa','#fff3a2','#a8a4ff'][i%3])
        oval(d,(x-3,y-3,x+3,y+3),'#ffe365')
    hop=abs(math.sin(t*4))*35 if 6<t<10 else 0
    bob=3*math.sin(t*4);cy=360+bob-hop
    oval(d,(123,cy+85,237,cy+235),'#e9e7f1')
    oval(d,(110,cy+190,180,cy+230),'#f7f3fa')
    oval(d,(185,cy+190,255,cy+230),'#f7f3fa')
    oval(d,(118,cy-160,162,cy+30),'#eeeaf5')
    oval(d,(198,cy-160,242,cy+30),'#eeeaf5')
    oval(d,(130,cy-144,150,cy+7),'#f6a3bd')
    oval(d,(210,cy-144,230,cy+7),'#f6a3bd')
    oval(d,(105,cy-10,255,cy+130),'#f3f0f8')
    for x in (145,215):
        oval(d,(x-20,cy+35,x+20,cy+77),'white')
        oval(d,(x-11,cy+39,x+11,cy+70),'#242d3d')
        oval(d,(x-5,cy+42,x+2,cy+51),'white')
    oval(d,(169,cy+82,191,cy+98),'#f08eaa')
    d.arc((162,cy+85,198,cy+111),0,180,fill='#76536a',width=3)
    oval(d,(97,cy+115,139,cy+183),'#f1edf6')
    oval(d,(221,cy+115,263,cy+183),'#f1edf6')
    caption='HELLO, FRIEND!' if t<5 else ('LET’S EXPLORE!' if t<10 else 'KINDNESS GROWS!')
    d.text((W/2,55),caption,anchor='mm',font=font(25),fill='white',stroke_width=2,stroke_fill='#397d64')
    sub='A little bunny, a big adventure' if t<10 else 'Share a smile today!'
    d.text((W/2,92),sub,anchor='mm',font=font(13),fill='#284a49')
    return im
def main():
    for cmd in ('ffmpeg','espeak'):
        if not shutil.which(cmd): raise SystemExit(f'Missing {cmd}')
    voice=OUT/'narration.wav'
    subprocess.run(['espeak','-v','en-us','-s','130','-w',str(voice),
        'Hello, friend! I am Poppy the bunny. Come explore the flower garden with me! A little kindness makes friendship grow.'],check=True)
    video=OUT/'tiny-paws-episode-1.mp4'
    p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pixel_format','rgb24',
        '-video_size',f'{W}x{H}','-framerate',str(FPS),'-i','pipe:0','-i',str(voice),
        '-f','lavfi','-i','anullsrc=channel_layout=mono:sample_rate=22050',
        '-filter_complex','[1:a][2:a]amix=inputs=2:duration=longest:weights=1 0.01[a]',
        '-map','0:v','-map','[a]','-c:v','libx264','-preset','ultrafast','-pix_fmt','yuv420p',
        '-c:a','aac','-t',str(DURATION),'-movflags','+faststart',str(video)],stdin=subprocess.PIPE)
    for i in range(FPS*DURATION):
        p.stdin.write(draw_frame(i/FPS).tobytes())
    p.stdin.close()
    if p.wait(): raise RuntimeError('ffmpeg failed')
    print(video)
if __name__=='__main__':main()
