"""Generate the profile's self-contained typewriter GIFs and static PNGs.

Run: python -m pip install Pillow; python tools/generate_typewriter.py
Requires DejaVu Sans fonts (override FONT_DIR to use a local installation).
No network requests. Outputs are written only under assets/.
"""
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets'
OUT.mkdir(exist_ok=True)
FONT_DIR = Path(os.environ.get('FONT_DIR', '/usr/share/fonts/truetype/dejavu'))
NAME = "Hi, I'm Krishnakumar Mandal."
LINES = [
    'Building AI. Testing its limits.',
    'Small models. Careful experiments.',
    'Useful apps, from model to interface.',
    'AI reliability & human-AI interaction.',
]
THEMES = {
    'dark': ('#0d1b2a', '#f1f5f9', '#b5c6d6', '#5eead4', '#20384b'),
    'light': ('#f3f7f8', '#102a3b', '#466174', '#087f76', '#d3e2e7'),
}
bold = ImageFont.truetype(str(FONT_DIR / 'DejaVuSans-Bold.ttf'), 52)
mono = ImageFont.truetype(str(FONT_DIR / 'DejaVuSansMono.ttf'), 32)
small = ImageFont.truetype(str(FONT_DIR / 'DejaVuSans.ttf'), 24)
label = ImageFont.truetype(str(FONT_DIR / 'DejaVuSansMono.ttf'), 18)


def draw(theme, name=NAME, line=LINES[0], cursor=False, phase='line'):
    bg, fg, muted, accent, border = THEMES[theme]
    im = Image.new('RGB', (1200, 290), bg)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((1, 1, 1198, 288), 18, outline=border, width=2)
    d.rectangle((38, 36, 43, 253), fill=accent)
    d.text((70, 32), 'NLP / EVALUATION / APPLICATIONS', font=label, fill=accent)
    d.text((68, 77), name, font=bold, fill=fg)
    d.text((70, 154), line, font=mono, fill=accent)
    if cursor:
        is_name = phase == 'name'
        text, font, y, x = (name, bold, 88, 68) if is_name else (line, mono, 160, 70)
        x += d.textlength(text, font=font) + 5
        d.rectangle((x, y, x + 3, y + (43 if is_name else 30)), fill=accent)
    d.line((70, 218, 1130, 218), fill=border, width=1)
    d.text((70, 236), 'AIML student at SFIT, Mumbai', font=small, fill=muted)
    d.text((805, 240), 'QUESTION / BUILD / CHECK', font=label, fill=muted)
    return im


for theme in THEMES:
    frames, durations = [], []

    def add(name=NAME, line='', cursor=True, duration=60, phase='line'):
        frames.append(draw(theme, name, line, cursor, phase))
        durations.append(duration)

    add(name='', cursor=True, duration=200, phase='name')
    for n in range(1, len(NAME) + 1):
        add(name=NAME[:n], phase='name', duration=45)
    add(duration=250)
    for index, line in enumerate(LINES):
        for n in range(1, len(line) + 1):
            add(line=line[:n], duration=40)
        add(line=line, cursor=False, duration=1300)
        for n in range(len(line) - 1, -1, -2):
            add(line=line[:n], duration=20)
        add(duration=100)
    for n in range(1, len(LINES[0]) + 1):
        add(line=LINES[0][:n], duration=35)
    add(line=LINES[0], cursor=False, duration=1000)
    # No loop extension: one restrained introduction, then a readable still.
    frames[0].save(OUT / f'typewriter-{theme}.gif', save_all=True,
                   append_images=frames[1:], duration=durations,
                   optimize=True, disposal=1)
    draw(theme).save(OUT / f'typewriter-{theme}-static.png', optimize=True)
    with Image.open(OUT / f'typewriter-{theme}.gif') as gif:
        assert 'loop' not in gif.info
        gif.seek(gif.n_frames - 1)
        assert gif.size == (1200, 290)
        print(theme, gif.n_frames, 'frames;', sum(durations), 'ms;',
              (OUT / f'typewriter-{theme}.gif').stat().st_size, 'bytes')
