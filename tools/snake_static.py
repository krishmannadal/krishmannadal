"""Make genuine still contribution grids from the pinned snk SVG output.

The still retains the original cells and activity colors. It has no snake,
consumed-cell bar, CSS animation, JavaScript or external resources.
"""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)
ROOT = Path(__file__).resolve().parents[1]


def make_static(source: str) -> str:
    original = ET.fromstring(source)
    css = ''.join(e.text or '' for e in original.findall(f'{{{NS}}}style'))
    variables = dict(re.findall(r'(--[\w-]+):([^;}]+)', css))
    cell_styles = dict(re.findall(r'\.c\.(\w+)\{fill:var\((--c\d+)\)', css))
    base_style = re.search(r'\.c\{([^}]+)\}', css)
    if base_style is None or '--ce' not in variables:
        raise ValueError('Unrecognized snk SVG format; keep the previous artwork.')
    dimensions = dict(re.findall(r'(width|height):(\d+)px', base_style.group(1)))
    if set(dimensions) != {'width', 'height'}:
        raise ValueError('Contribution-cell dimensions are missing.')
    root = ET.Element(f'{{{NS}}}svg', {
        key: original.attrib[key] for key in ('viewBox', 'width', 'height')
    })
    root.set('role', 'img')
    ET.SubElement(root, f'{{{NS}}}title').text = 'Krishnakumar Mandal — contribution grid'
    ET.SubElement(root, f'{{{NS}}}desc').text = (
        'Static snapshot of the public contribution grid used for the snake animation. '
        'Generated from GitHub data by Platane/snk.'
    )
    count = 0
    for cell in original.findall(f'.//{{{NS}}}rect'):
        classes = cell.get('class', '').split()
        if 'c' not in classes:
            continue
        fill = variables['--ce']
        for cls in classes:
            if cls in cell_styles:
                fill = variables[cell_styles[cls]]
        attrs = {key: value for key, value in cell.attrib.items()
                 if key in ('x', 'y', 'rx', 'ry')}
        attrs.update(dimensions, fill=fill, stroke=variables.get('--cb', '#d0d7de'))
        attrs['stroke-width'] = '1'
        ET.SubElement(root, f'{{{NS}}}rect', attrs)
        count += 1
    if count < 350:
        raise ValueError('Unexpectedly short contribution calendar; keep previous artwork.')
    return ET.tostring(root, encoding='unicode') + '\n'


if __name__ == '__main__':
    for theme in ('', '-dark'):
        path = ROOT / f'assets/contributions/snake{theme}.svg'
        output = path.with_name(f'snake{theme}-static.svg')
        output.write_text(make_static(path.read_text()))
        print(f'Generated {output.relative_to(ROOT)}')
