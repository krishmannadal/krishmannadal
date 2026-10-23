"""Frame snk artwork with labels from the same real GitHub calendar.

The workflow token is used only for GitHub's GraphQL request, never saved.
Reject a mismatch rather than publishing fabricated or misaligned cells.
"""
from datetime import date
import json
import os
from pathlib import Path
import re
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets/contributions'
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)
LEVELS = {'NONE': 0, 'FIRST_QUARTILE': 1, 'SECOND_QUARTILE': 2,
          'THIRD_QUARTILE': 3, 'FOURTH_QUARTILE': 4}
QUERY = '''query ($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays { date weekday contributionCount contributionLevel }
        }
      }
    }
  }
}'''


def fetch_calendar():
    payload = json.dumps({'query': QUERY, 'variables': {'login': 'krishmannadal'}}).encode()
    request = urllib.request.Request('https://api.github.com/graphql', data=payload,
        headers={'Authorization': 'Bearer ' + os.environ['GITHUB_TOKEN'],
                 'Content-Type': 'application/json', 'User-Agent': 'profile-contribution-calendar'})
    with urllib.request.urlopen(request, timeout=45) as response:
        result = json.load(response)
    if result.get('errors'):
        raise RuntimeError('GitHub could not return the contribution calendar.')
    calendar = result['data']['user']['contributionsCollection']['contributionCalendar']
    days = [d for w in calendar['weeks'] for d in w['contributionDays']]
    if sum(d['contributionCount'] for d in days) != calendar['totalContributions']:
        raise ValueError('Calendar total does not match the returned day counts.')
    return calendar


def verify_cells(svg, calendar):
    root = ET.fromstring(svg)
    css = ''.join(n.text or '' for n in root.findall(f'{{{NS}}}style'))
    classes = dict(re.findall(r'\.c\.(\w+)\{fill:var\(--c(\d)\)', css))
    actual = {}
    for rect in root.findall(f'.//{{{NS}}}rect'):
        tags = rect.get('class', '').split()
        if 'c' not in tags:
            continue
        level = next((int(classes[t]) for t in tags if t in classes), 0)
        actual[(int(rect.get('x')), int(rect.get('y')))] = level
    expected = {(2 + x * 16, 2 + d['weekday'] * 16): LEVELS[d['contributionLevel']]
                for x, week in enumerate(calendar['weeks']) for d in week['contributionDays']}
    if actual != expected:
        raise ValueError('Calendar changed during generation or SVG layout changed; rerun safely.')


def decorate(svg, calendar, dark=False):
    root = ET.fromstring(svg)
    bg, border, fg, muted = (('#0d1117', '#30363d', '#e6edf3', '#8b949e') if dark else
                             ('#ffffff', '#d1d9e0', '#1f2328', '#59636e'))
    colors = (['#161b22', '#0e4429', '#006d32', '#26a641', '#39d353'] if dark else
              ['#ebedf0', '#9be9a8', '#40c463', '#30a14e', '#216e39'])
    root.set('viewBox', '-56 -68 960 290')
    root.set('width', '960')
    root.set('height', '290')
    root.set('role', 'img')
    frame = ET.Element(f'{{{NS}}}rect', {'x': '-54', 'y': '-66', 'width': '956',
        'height': '286', 'rx': '8', 'fill': bg, 'stroke': border})
    root.insert(0, frame)
    group = ET.SubElement(root, f'{{{NS}}}g', {'font-family': 'Arial, Helvetica, sans-serif',
                                             'font-size': '11', 'fill': muted})
    def text(x, y, content, **attrs):
        ET.SubElement(group, f'{{{NS}}}text', {'x': str(x), 'y': str(y), **attrs}).text = content
    text(-30, -42, f"{calendar['totalContributions']:,} contributions in the last 12 months",
         fill=fg, **{'font-size': '15'})
    # Place each month at its first week in the actual returned calendar.
    last_month, last_label_x = None, -100
    for x, week in enumerate(calendar['weeks']):
        month = week['contributionDays'][0]['date'][:7]
        if month != last_month:
            label_x = x * 16 + 2
            if label_x - last_label_x >= 32:
                text(label_x, -12, date.fromisoformat(week['contributionDays'][0]['date']).strftime('%b'))
                last_label_x = label_x
            last_month = month
    for weekday, label in [(1, 'Mon'), (3, 'Wed'), (5, 'Fri')]:
        text(-12, weekday * 16 + 12, label, **{'text-anchor': 'end'})
    text(650, 177, 'Less')
    for i, color in enumerate(colors):
        ET.SubElement(group, f'{{{NS}}}rect', {'x': str(682 + i * 16), 'y': '166',
            'width': '12', 'height': '12', 'rx': '2', 'fill': color})
    text(768, 177, 'More')
    days = [d for w in calendar['weeks'] for d in w['contributionDays']]
    text(2, 202, f"{days[0]['date']} – {days[-1]['date']} · GitHub contribution calendar")
    return ET.tostring(root, encoding='unicode') + '\n'


def publish(calendar):
    raw = {theme: (ASSETS / f'snake{theme}.svg').read_text() for theme in ('', '-dark')}
    for svg in raw.values():
        verify_cells(svg, calendar)
    # Verify all original animated grids before touching any files.
    for theme in ('', '-dark'):
        for suffix in ('', '-static'):
            path = ASSETS / f'snake{theme}{suffix}.svg'
            source = raw[theme] if not suffix else path.read_text()
            path.write_text(decorate(source, calendar, dark=bool(theme)))
    (ASSETS / 'calendar.json').write_text(json.dumps(calendar, indent=2) + '\n')
    print('Verified real GitHub dates, levels and total; generated labeled contribution artwork.')


if __name__ == '__main__':
    publish(fetch_calendar())
