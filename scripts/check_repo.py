"""Stdlib kit checks. Adapted from boombignose/chinese-short-film-flow (MIT); see THIRD_PARTY_NOTICES.md."""

import re
from xml.etree import ElementTree
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        self.targets.extend(value for key, value in attrs if key in ('href', 'src') and value)


def check(root):
    root = root.resolve()
    errors = []
    required = (
        "README.md", "WORKFLOW.md", "AGENTS.md", "LICENSE", "THIRD_PARTY_NOTICES.md",
        "prompts/MASTER-PROMPT.md", "prompts/REPAIR.md", "templates/PRODUCTION.md",
        "examples/one-floor-below-48s.md", "docs/GOOGLE-FLOW.md", "docs/EDITING.md",
        "docs/TEST-REPORT.md", "assets/hero.svg", ".github/workflows/check.yml",
        "scripts/check_repo.py", "scripts/test_check_repo.py",
    )
    errors.extend(f"missing required file: {name}" for name in required if not (root / name).is_file())
    documents = sorted(p for p in root.rglob('*.md') if not {'.git', '.superpowers', 'runs', 'media', 'exports'} & set(p.relative_to(root).parts))
    links = 0
    for path in documents:
        text = path.read_text(encoding='utf-8')
        if len(re.findall(r'^```', text, re.M)) % 2:
            errors.append(f'{path.relative_to(root)}: unclosed fenced block')
        prose = re.sub(r'^```.*?^```[^\n]*', '', text, flags=re.M | re.S)
        html = References()
        html.feed(prose)
        targets = re.findall(r'\]\(([^\s)]+)\)', prose) + html.targets
        for target in targets:
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            links += 1
            if not resolved.is_relative_to(root) or not resolved.exists():
                errors.append(f'{path.relative_to(root)}: missing/escaping reference {target}')
    example = root / 'examples/one-floor-below-48s.md'
    if not example.is_file():
        errors.append('missing six-shot example')
    else:
        text = example.read_text(encoding='utf-8')
        rows = re.findall(r'^\| (S\d{2}) \| (\d{2}):(\d{2})–(\d{2}):(\d{2}) \| (E01): “([^”]+)”', text, re.M)
        if [row[0] for row in rows] != [f'S{i:02}' for i in range(1, 7)]:
            errors.append('expected six ordered storyboard rows S01–S06')
        headings = re.findall(r'^### (S\d{2}) · (\d{2}):(\d{2})–(\d{2}):(\d{2})$', text, re.M)
        if headings != [row[:5] for row in rows]:
            errors.append('prompt heading times/order do not match storyboard')
        prompt_ids = re.findall(r'^```text\nShot (S\d{2})\.', text, re.M)
        if prompt_ids != [row[0] for row in rows]:
            errors.append('prompt order does not match storyboard')
        end = 0
        for shot, sm, ss, em, es, speaker, dialogue in rows:
            start, finish = int(sm) * 60 + int(ss), int(em) * 60 + int(es)
            if start != end or finish - start != 8:
                errors.append(f'{shot}: timeline gap or duration is not 8 seconds')
            end = finish
            blocks = re.findall(r'```text\n(Shot ' + shot + r'\..*?)\n```', text, re.S)
            if len(blocks) != 1 or f'"{dialogue}"' not in blocks[0]:
                errors.append(f'{shot}: missing self-contained prompt or changed dialogue')
            elif 'Only Ella speaks' not in blocks[0]:
                errors.append(f'{shot}: speaker does not match the script')
            if blocks and (not blocks[0].startswith(f'Shot {shot}. Vertical 9:16, 8-second ') or any(token not in blocks[0] for token in (
                'Ella Ward', 'dark brown bob',
                'navy wool coat', 'cream sweater', 'No subtitles',
            ))):
                errors.append(f'{shot}: prompt is not self-contained or has wrong format/duration')
        if end != 48:
            errors.append('storyboard must end at 48 seconds')
    hero = root / 'assets/hero.svg'
    if hero.is_file():
        try:
            svg = ElementTree.parse(hero).getroot()
            if svg.tag != '{http://www.w3.org/2000/svg}svg':
                errors.append('hero is not an SVG')
        except ElementTree.ParseError:
            errors.append('hero is not valid SVG XML')
    return errors, len(documents), links


if __name__ == '__main__':
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    errors, documents, links = check(root)
    for error in errors:
        print('FAIL:', error)
    if not errors:
        print(f'PASS: {documents} Markdown files; {links} local references; 6 shot prompts; 48s timeline; SVG banner')
    sys.exit(bool(errors))
