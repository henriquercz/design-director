#!/usr/bin/env python3
from pathlib import Path
import re, sys, subprocess
try:
    import yaml
except Exception:
    yaml = None

root = Path(__file__).resolve().parents[1]
skill = root / 'skills' / 'design-director'
p = skill / 'SKILL.md'
text = p.read_text(encoding='utf-8')
errors=[]
if not text.startswith('---\n'):
    errors.append('SKILL.md must start with YAML frontmatter')
else:
    parts=text.split('---',2)
    front=parts[1]
    if yaml:
        data=yaml.safe_load(front)
    else:
        data={}
        for line in front.splitlines():
            if ':' in line and not line.startswith(' '):
                k,v=line.split(':',1); data[k.strip()]=v.strip().strip('"')
    name=data.get('name'); desc=data.get('description')
    if name != skill.name: errors.append(f'name must equal parent directory: {skill.name!r}')
    if not isinstance(name,str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name or ''):
        errors.append('name is not valid kebab-case')
    if not isinstance(desc,str) or not (1 <= len(desc) <= 1024):
        errors.append('description must be 1..1024 characters')
    comp=data.get('compatibility')
    if comp is not None and (not isinstance(comp,str) or len(comp)>500):
        errors.append('compatibility must be a string <=500 chars')
    meta=data.get('metadata')
    if meta is not None and (not isinstance(meta,dict) or any(not isinstance(k,str) or not isinstance(v,str) for k,v in meta.items())):
        errors.append('metadata must map string keys to string values')

lines=text.count('\n')+1
if lines>500: errors.append(f'SKILL.md is {lines} lines; recommended maximum is 500')

for rel in re.findall(r'`((?:references|templates|scripts|assets)/[^`]+)`', text):
    rel=rel.rstrip('.,;:')
    if not (skill/rel).exists(): errors.append(f'missing referenced file: {rel}')

for md in skill.rglob('*.md'):
    body=md.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^\]]+\]\(([^)]+\.md)(?:#[^)]+)?\)', body):
        if target.startswith(('http://','https://')): continue
        q=(md.parent/target).resolve()
        if not q.exists(): errors.append(f'{md.relative_to(skill)} links missing file: {target}')

for sh in (root/'scripts').glob('*.sh'):
    if not sh.stat().st_mode & 0o111:
        errors.append(f'not executable: {sh.relative_to(root)}')
    else:
        r=subprocess.run(['bash','-n',str(sh)],capture_output=True,text=True)
        if r.returncode: errors.append(f'shell syntax error in {sh.name}: {r.stderr.strip()}')

eval_text=(skill/'evals'/'EVALS.md').read_text(encoding='utf-8')
eval_cases=len(re.findall(r'^##\s+\d+\.', eval_text, flags=re.M))

required_v4 = {
    'product-outcomes.md','ethical-persuasion.md','activation-retention.md',
    'conversion-monetization.md','experimentation-evidence.md','feature-discipline.md',
    'design-evidence.md','component-contracts.md','micro-craft.md'
}
missing_v4 = required_v4 - {x.name for x in (skill/'references').glob('*.md')}
if missing_v4:
    errors.append('missing v4 required references: ' + ', '.join(sorted(missing_v4)))
if eval_cases < 46:
    errors.append(f'v4 requires at least 46 eval cases; found {eval_cases}')

if errors:
    print('Validation FAILED')
    for e in errors: print(' -',e)
    sys.exit(1)
print('Validation OK')
print(f' - skill: {skill.name}')
print(f' - SKILL.md lines: {lines}')
print(f' - reference files: {len(list((skill/"references").glob("*.md")))}')
print(f' - templates: {len(list((skill/"templates").glob("*.md")))}')
print(f' - eval cases: {eval_cases}')
