from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import json
root=Path(__file__).resolve().parents[1]/'dist'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=[];self.h1=0;self.titles=0;self.descriptions=0;self.alts=[]
 def handle_starttag(self,t,attrs):
  d=dict(attrs)
  if 'id' in d:self.ids.append(d['id'])
  if t=='h1':self.h1+=1
  if t=='title':self.titles+=1
  if t=='meta' and d.get('name')=='description':self.descriptions+=1
  if t in ['a','link','img','script']:
   u=d.get('href') if t in ['a','link'] else d.get('src')
   if u:self.links.append(u)
  if t=='img':self.alts.append(d.get('alt'))
errors=[];pages={}
for path in root.rglob('*.html'):
 p=Page();p.feed(path.read_text());pages[path]=p
 if p.h1!=1:errors.append(f'{path}: H1 count {p.h1}')
 if len(p.ids)!=len(set(p.ids)):errors.append(f'{path}: duplicate IDs')
 if any(a is None for a in p.alts):errors.append(f'{path}: missing alt')
 if path.name!='404.html' and (p.titles!=1 or p.descriptions!=1):errors.append(f'{path}: metadata')
for path,p in pages.items():
 for href in p.links:
  u=urlparse(href)
  if u.scheme or u.netloc:continue
  dest=root/unquote(u.path.lstrip('/')) if u.path.startswith('/') else path.parent/u.path
  if not u.path:dest=path
  if dest.is_dir():dest=dest/'index.html'
  if not dest.exists():errors.append(f'{path}: missing {href}')
  elif u.fragment and dest.suffix=='.html' and u.fragment not in pages[dest].ids:errors.append(f'{path}: missing anchor {href}')
print(json.dumps({'html_pages':len(pages),'local_references':sum(len(p.links) for p in pages.values()),'errors':errors},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
