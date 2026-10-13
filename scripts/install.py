"""Install selected skills and their companion resources without replacing files."""
from pathlib import Path
import argparse, hashlib, json, shutil

ROOT=Path(__file__).resolve().parents[1]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--client',choices=['codex','claude','trae'],default='codex')
    p.add_argument('--project',type=Path,help='Project directory for TRAE or Claude')
    p.add_argument('--dest',type=Path,help='Explicit client data directory, e.g. ~/.codex')
    p.add_argument('--skill',action='append',default=[],help='Skill directory ID; repeat to select several')
    p.add_argument('--all',action='store_true',help='Select all 669 entries')
    p.add_argument('--list',action='store_true')
    p.add_argument('--apply',action='store_true',help='Write files; otherwise only preview')
    a=p.parse_args()
    available={x.name:x for x in (ROOT/'skills').iterdir() if (x/'SKILL.md').is_file()}
    if a.list:
        print('\n'.join(sorted(available)));return
    selected=sorted(available) if a.all else sorted(set(a.skill))
    if not selected:p.error('Choose --skill ID, --all, or --list')
    if any(x not in available for x in selected):p.error('Unknown skill ID; use --list')
    if a.project and a.client=='codex':p.error('Use --dest for a custom Codex skill root')
    if a.dest:dest=a.dest.expanduser().resolve()
    elif a.project:dest=a.project.resolve()/('.trae' if a.client=='trae' else '.claude')
    else:dest=Path.home()/{'codex':'.codex','claude':'.claude','trae':'.trae-cn'}[a.client]
    pairs=[]
    for name in selected:
        for f in available[name].rglob('*'):
            if f.is_file():pairs.append((f,dest/'skills'/name/f.relative_to(available[name])))
    for folder in ['resources','licenses']:
        for f in (ROOT/folder).rglob('*'):
            if f.is_file():pairs.append((f,dest/folder/f.relative_to(ROOT/folder)))
    for f in ['skill-aliases.json','SKILLS_INDEX.md']:
        pairs.append((ROOT/f,dest/f))
    for source,target in pairs:
        if source.is_symlink():raise SystemExit('Refusing source symlink: '+str(source))
        if not target.resolve().is_relative_to(dest.resolve()):raise SystemExit('Destination link escapes root')
        if target.exists() and (not target.is_file() or digest(source)!=digest(target)):
            raise SystemExit('Conflict; nothing written: '+str(target))
    new=[(s,t) for s,t in pairs if not t.exists()]
    if a.apply:
        for s,t in new:
            t.parent.mkdir(parents=True,exist_ok=True)
            with t.open('xb') as h:h.write(s.read_bytes())
        if not all(digest(s)==digest(t) for s,t in pairs):raise SystemExit('Verification failed')
    print(json.dumps({'client':a.client,'destination':str(dest),'selected_skills':len(selected),
                      'new_files':len(new),'already_identical':len(pairs)-len(new),
                      'applied':a.apply,'verified':bool(a.apply),'configs_modified':False},ensure_ascii=True))

if __name__=='__main__':main()
