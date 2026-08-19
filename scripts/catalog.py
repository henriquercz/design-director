#!/usr/bin/env python3
from pathlib import Path
import re, json

root = Path(__file__).resolve().parents[1]
skill = root / 'skills' / 'design-director'
refs = sorted(p.name for p in (skill/'references').glob('*.md'))
templates = sorted(p.name for p in (skill/'templates').glob('*.md'))
evals = (skill/'evals'/'EVALS.md').read_text(encoding='utf-8')
eval_count = len(re.findall(r'^##\s+\d+\.', evals, flags=re.M))
skill_text = (skill/'SKILL.md').read_text(encoding='utf-8')
mode_rows=[]
for line in skill_text.splitlines():
    m=re.match(r'^\| (.+?) \| ([^|]+) \| ([^|]+) \|$', line)
    if m and '`' in m.group(1):
        aliases=re.findall(r'`([^`]+)`', m.group(1))
        mode_rows.append({'mode': ' / '.join(aliases), 'aliases': aliases, 'job':m.group(2).strip(),'edits':m.group(3).strip()})
result={
    'skill':'design-director',
    'references':refs,
    'reference_count':len(refs),
    'templates':templates,
    'template_count':len(templates),
    'eval_count':eval_count,
    'modes':mode_rows,
    'mode_count':len(mode_rows),
}
print(json.dumps(result, indent=2, ensure_ascii=False))
