#!/usr/bin/env python3
from pathlib import Path
import shutil, subprocess, tempfile

HERE = Path(__file__).resolve().parent

CURRENT_REFS = [
'accessibility.md','activation-retention.md','anti-slop.md','audit-scorecard.md','borders-depth.md','calibration.md','color.md','companion-routing.md','composition-layout.md','controls-interaction.md','conversion-monetization.md','creation-redesign.md','ethical-persuasion.md','experimentation-evidence.md','feature-discipline.md','implementation.md','mode-bars.md','motion.md','product-outcomes.md','project-memory.md','prompt-invariants.md','prompt-recipes.md','refine.md','registers.md','responsive.md','routing.md','surface-taxonomy.md','surface.md','tokenize.md','typography.md','verification.md','voice.md','writing.md']
TEMPLATES=['checkup-report.md','design-brief.md','design-decision-log.md','principle-entry.md','review-report.md','smell-report.md']

def main():
    with tempfile.TemporaryDirectory() as td:
        root=Path(td)
        (root/'scripts').mkdir(parents=True)
        shutil.copy2(HERE/'validate.py', root/'scripts'/'validate.py')
        skill=root/'skills'/'design-director'
        (skill/'references').mkdir(parents=True)
        (skill/'templates').mkdir()
        (skill/'evals').mkdir()
        for r in CURRENT_REFS:
            (skill/'references'/r).write_text('# placeholder\n', encoding='utf-8')
        for t in TEMPLATES:
            (skill/'templates'/t).write_text('# placeholder\n', encoding='utf-8')
        (skill/'SKILL.md').write_text('''---\nname: design-director\ndescription: Test fixture\nlicense: MIT\ncompatibility: Test\nmetadata:\n  version: "3.0.0"\n---\n# Test\n''', encoding='utf-8')
        (skill/'evals'/'EVALS.md').write_text('## 1. Fixture\n', encoding='utf-8')
        r=subprocess.run(['python', str(root/'scripts'/'validate.py')], text=True, capture_output=True)
        if r.returncode == 0:
            raise AssertionError('validator incorrectly accepted a tree missing required v4 references')
        out=r.stdout+r.stderr
        for required in ['design-evidence.md','component-contracts.md','micro-craft.md']:
            if required not in out:
                raise AssertionError(f'validator failure did not name missing v4 reference: {required}\n{out}')
        print('PASS: validator rejects missing v4 references')

if __name__ == '__main__':
    main()
