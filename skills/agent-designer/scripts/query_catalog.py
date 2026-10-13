"""Search bundled metadata. Optional resource root resolves files; nothing executes."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import re
import sys

SKILL=Path(__file__).resolve().parents[1]
FILES={'repo':'source-index.json','skill':'skill-index.json','mcp':'mcp-index.json'}

def resource_root(explicit: Path | None = None) -> Path | None:
    candidate=explicit or (Path(os.environ['AGENT_DESIGNER_RESOURCE_ROOT']) if os.environ.get('AGENT_DESIGNER_RESOURCE_ROOT') else None)
    if candidate is not None:
        candidate=candidate.expanduser().resolve()
        if not candidate.is_dir(): raise ValueError('Resource root does not exist: '+str(candidate))
        return candidate
    for start in (Path.cwd().resolve(),SKILL):
        for parent in (start,*start.parents):
            if (parent/'code').is_dir() and (parent/'export/skills').is_dir(): return parent
    return None

def resolve_under(root: Path, rel: str) -> Path:
    path=(root/rel).resolve()
    if not path.is_relative_to(root.resolve()): raise ValueError('Catalog path escapes selected resource root')
    return path

def search(kind: str, query: str, limit: int) -> list[dict]:
    rows=json.loads((SKILL/'references'/FILES[kind]).read_text(encoding='utf-8'))
    terms=re.findall(r'[\w-]+',query.lower())
    scored=[]
    for row in rows:
        identity=' '.join(str(row.get(k,'')) for k in ('id','name','category','topics')).lower()
        text=json.dumps(row,ensure_ascii=False).lower()
        score=sum((4 if term in identity else 1) for term in terms if term in text)
        if not terms or score: scored.append((score,row))
    scored.sort(key=lambda item:(-item[0],item[1]['id']))
    return [dict(row,search_score=score) for score,row in scored[:limit]]

def main():
    if hasattr(sys.stdout,'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--kind',choices=FILES,default='repo'); ap.add_argument('--query',default=''); ap.add_argument('--limit',type=int,default=8); ap.add_argument('--root',type=Path); ap.add_argument('--metadata-only',action='store_true',help='Use bundled metadata without locating source resources')
    args=ap.parse_args()
    if not 1<=args.limit<=100: ap.error('--limit must be 1..100')
    if args.metadata_only and args.root: ap.error('--metadata-only and --root are mutually exclusive')
    try: root=None if args.metadata_only else resource_root(args.root)
    except ValueError as exc: ap.error(str(exc))
    rows=search(args.kind,args.query,args.limit)
    for row in rows:
        rel=row.get('path') or row.get('root') or row.get('source')
        row['local_available']=bool(root and rel and resolve_under(root,rel).exists())
        if root and rel: row['resolved_path']=str(resolve_under(root,rel))
    print(json.dumps({'resource_root':str(root) if root else None,'mode':'metadata-only' if root is None else 'resource-aware','results':rows},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
