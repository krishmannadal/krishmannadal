"""Rebuild documentation artwork with Pillow; no remote widgets or model calls.

Run from this profile repository. Project cards are copied to sibling checkouts
when they exist. The cards are editorial graphics, never screenshots/results.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import html

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
ASSETS.mkdir(exist_ok=True)
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
MONO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'

def font(size, bold=False, mono=False):
    return ImageFont.truetype(MONO if mono else BOLD if bold else FONT, size)

for theme,bg,fg,muted,accent,line in [
    ('dark','#0d1b2a','#f1f5f9','#b5c6d6','#5eead4','#20384b'),
    ('light','#f3f7f8','#102a3b','#466174','#087f76','#d3e2e7'),
]:
    grid=''.join(f'<path d="M{x} 0V230"/>' for x in range(820,1200,32))
    grid+=''.join(f'<path d="M800 {y}H1200"/>' for y in range(0,240,32))
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 230" role="img" aria-labelledby="title desc">
<title id="title">Build with evidence</title><desc id="desc">NLP, evaluation and practical AI. Krishnakumar Mandal.</desc>
<rect width="1200" height="230" rx="16" fill="{bg}"/>
<g stroke="{line}" fill="none" stroke-width="1">{grid}</g>
<rect x="34" y="34" width="5" height="162" fill="{accent}"/>
<g font-family="Arial, Helvetica, sans-serif">
<text x="62" y="57" font-size="15" letter-spacing="3" fill="{muted}">KRISHNAKUMAR MANDAL / SELECTED WORK</text>
<text x="58" y="119" font-size="54" font-weight="700" fill="{fg}">Build with evidence.</text>
<text x="62" y="160" font-size="22" fill="{muted}">NLP, evaluation &amp; practical AI</text>
<text x="62" y="199" font-size="14" letter-spacing="2" fill="{accent}">SFIT MUMBAI · CLASS OF 2028</text>
</g>
<g fill="none" stroke="{accent}" stroke-width="3">
<path d="M858 165V110L900 135 942 83 984 110 1038 58 1110 96"/>
<circle cx="858" cy="165" r="6" fill="{bg}"/><circle cx="942" cy="83" r="6" fill="{bg}"/>
<circle cx="1038" cy="58" r="6" fill="{bg}"/><circle cx="1110" cy="96" r="6" fill="{bg}"/>
</g>
<text x="859" y="201" fill="{muted}" font-family="monospace" font-size="12">QUESTION / BUILD / CHECK</text>
</svg>'''
    (ASSETS/f'banner-{theme}.svg').write_text(svg)

def intro(active=None, progress=1):
    im=Image.new('RGB',(1200,68),'#0d1b2a');d=ImageDraw.Draw(im)
    labels=['01  BUILD APPLICATIONS','02  INSPECT EVIDENCE','03  TEST ASSUMPTIONS']
    for i,t in enumerate(labels):
        x=30+i*390
        d.text((x,20),t,font=font(18,mono=True),fill='#5eead4' if i==active else '#e2e8f0')
    d.rectangle((30,58,1170,60),fill='#20384b')
    d.rectangle((30,58,30+int(1140*progress),60),fill='#5eead4')
    return im

intro().save(ASSETS/'intro-static.png')
frames=[intro(min(2,int(i/8)),(i+1)/24) for i in range(24)]
frames.append(intro())
# No loop extension: one two-second opening, ending on a readable still frame.
frames[0].save(ASSETS/'intro.gif',save_all=True,append_images=frames[1:],duration=[80]*24+[120],optimize=True)

cards=[
 ('mini-r1','Mini-R1','SMALL LANGUAGE MODELS', ['A PyTorch Transformer and an auditable','arithmetic-retention experiment trail.'],'PyTorch / SentencePiece / Evaluation'),
 ('StemLab','StemLab','AI APPLICATION', ['Pretrained music separation, rehearsal','mixing and local audio processing.'],'JavaScript / ONNX / Web Audio'),
 ('Nullius','Nullius','RESEARCH INSTRUMENT', ['Inspect claims, retrieved evidence','and aggregation decisions.'],'Python / FastAPI / Hybrid retrieval'),
 ('traffic-rl-twin','Traffic RL Twin','SIMULATION PROTOTYPE', ['Explore traffic control and emergency','preemption in a local SUMO workbench.'],'SUMO / Gymnasium / FastAPI / React'),
 ('UNSUPERVISED_ASTRONOMY','Disk morphology','EXPLORATORY ML', ['FITS images, autoencoder embeddings','and exploratory morphological clusters.'],'PyTorch / Astropy / UMAP / HDBSCAN'),
 ('portfolio','Research portfolio','PRESENTATION INTERFACE', ['Project dossiers, experiment notes','and interactive concept illustrations.'],'Next.js / React / TypeScript'),
 ('krishmannadal','Krishnakumar Mandal','NLP / EVALUATION / APPLICATIONS', ['AIML student at SFIT, Mumbai.','Seeking paid, remote internships.'],'AI/ML / Python applications / Research assistance'),
]
for repo,title,kind,lines,stack in cards:
    im=Image.new('RGB',(1280,640),'#0d1b2a');d=ImageDraw.Draw(im)
    for x in range(920,1280,36):d.line((x,0,x,640),fill='#173145')
    for y in range(0,640,36):d.line((920,y,1280,y),fill='#173145')
    d.rectangle((56,58,62,535),fill='#5eead4')
    d.text((92,66),kind,font=font(19,mono=True),fill='#5eead4')
    size=64
    while d.textbbox((0,0),title,font=font(size,True))[2]>1100:size-=1
    d.text((87,143),title,font=font(size,True),fill='#f1f5f9')
    for i,t in enumerate(lines):d.text((92,260+i*49),t,font=font(30),fill='#c5d5e3')
    d.text((92,418),stack,font=font(21),fill='#5eead4')
    d.line((92,486,1188,486),fill='#375166',width=1)
    d.text((92,522),f'github.com/krishmannadal/{repo}',font=font(20,mono=True),fill='#c5d5e3')
    dest=(ROOT.parent/repo/'docs/assets/social-preview.png') if repo!='krishmannadal' else ASSETS/'social-preview.png'
    dest.parent.mkdir(parents=True,exist_ok=True);im.save(dest,optimize=True)

print('Generated theme-aware banners, finite GIF, static fallback and seven social cards.')
