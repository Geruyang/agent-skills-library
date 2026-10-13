"""Validate self-contained references and optionally pinned local source evidence."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote
from query_catalog import SKILL, resolve_under

def check(root: Path | None = None):
    errors=[]; links=0; paths=0; hashes=0
    required=['SKILL.md','references/source-index.json','references/skill-index.json','references/mcp-index.json','references/runtime-dependencies.json','references/mcp-followup.json']
    absent=[rel for rel in required if not (SKILL/rel).is_file()]
    if absent:
        return {'passed':False,'errors':['Missing skill resource: '+rel for rel in absent],
                'hint':'Restore the complete skill folder; rebuild indexes only with the downloaded resource bundle.'}
    body=(SKILL/'SKILL.md').read_text(encoding='utf-8')
    if not body.startswith('---\nname: agent-designer\ndescription: '): errors.append('Invalid entrypoint frontmatter')
    for p in SKILL.rglob('*.md'):
        text=p.read_text(encoding='utf-8')
        if re.search(r'(?i)[a-z]:[\\/](?:Users|AIProject)[\\/]',text): errors.append('Machine path: '+p.name)
        for target in re.findall(r'\]\(([^)]+)\)',text):
            if target.startswith(('http:','https:','#','mailto:')): continue
            rel=unquote(target.split('#',1)[0].strip('<>'))
            resolved=(p.parent/rel).resolve(); links+=1
            if not resolved.is_relative_to(SKILL): errors.append('Nonportable link '+target)
            elif not resolved.exists(): errors.append('Broken link '+target)
    repos=json.loads((SKILL/'references/source-index.json').read_text(encoding='utf-8'))
    skills=json.loads((SKILL/'references/skill-index.json').read_text(encoding='utf-8'))
    mcp=json.loads((SKILL/'references/mcp-index.json').read_text(encoding='utf-8'))
    locks=json.loads((SKILL/'references/runtime-dependencies.json').read_text(encoding='utf-8'))
    followup=json.loads((SKILL/'references/mcp-followup.json').read_text(encoding='utf-8'))
    if len(repos)!=35 or len(skills)!=667: errors.append('Coverage counts differ')
    if len({r['id'] for r in repos})!=len(repos) or len({r['id'] for r in skills})!=len(skills): errors.append('Duplicate identity')
    if sum(r['kind']=='catalog-definition' for r in mcp)!=45: errors.append('Missing catalog definitions')
    if sum(r['kind']=='local-implementation' for r in mcp)!=16: errors.append('Missing local implementations')
    if len(followup['entries'])!=41: errors.append('Missing MCP followup entry')
    known={r['id'] for r in repos}
    if any(r['repository'] not in known for r in skills): errors.append('Out-of-scope skill')
    if any(not r['design_use'] or not r['evidence'] or not re.fullmatch('[0-9a-f]{40}',r['commit']) for r in repos): errors.append('Incomplete source synthesis')
    if root:
        root=root.resolve()
        items=[]
        for row in repos: items.extend(row['evidence']+row['license_files'])
        items+=skills+locks
        for row in mcp:
            items.append({'path':row['source'],'sha256':row.get('source_sha256')})
            if row.get('path'): items.append({'path':row['path']})
        for row in items:
            rel=row.get('path')
            try: p=resolve_under(root,rel)
            except ValueError: errors.append('Escaping path '+rel); continue
            paths+=1
            if not p.exists(): errors.append('Missing '+rel); continue
            if row.get('sha256'):
                hashes+=1
                if hashlib.sha256(p.read_bytes()).hexdigest()!=row['sha256']: errors.append('Hash drift '+rel)
    return {'passed':not errors,'portable_links_checked':links,'repositories':len(repos),'skills':len(skills),
            'mcp_definitions':45,'local_implementations':16,'resource_paths_checked':paths,'hashes_checked':hashes,
            'mode':'source-integrity' if root else 'standalone','errors':errors,
            'limits':'Static integrity validation; does not prove model behavior, framework runtime or client loading'}

def main():
    if hasattr(sys.stdout,'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--root',type=Path); ap.add_argument('--report',type=Path); args=ap.parse_args()
    result=check(args.root); content=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if args.report: args.report.parent.mkdir(parents=True,exist_ok=True); args.report.write_text(content,encoding='utf-8')
    print(content); raise SystemExit(0 if result['passed'] else 1)

if __name__=='__main__': main()
