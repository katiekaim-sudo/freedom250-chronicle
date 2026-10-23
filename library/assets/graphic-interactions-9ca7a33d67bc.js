/* Subject records: one interaction contract for existing HTML/SVG graphics. */
(()=>{'use strict';
 const dataEl=document.querySelector('#f-data,#g-data,#eo-data,#x-data');let D={};try{if(dataEl)D=window.D?.schema===/"schema"\s*:\s*"([^"]+)"/.exec(dataEl.textContent)?.[1]?window.D:JSON.parse(dataEl.textContent)}catch{return}
 const panels=D.interaction_panels||{},get=(path)=>path.reduce((v,k)=>v==null?undefined:v[k],D);
 let lastTrigger=null,activePanel=null;
 const plain=(s)=>{const t=document.createElement('div');t.innerHTML=String(s||'');return t.textContent||''};
 function node(tag,text,cls){const e=document.createElement(tag);if(text!=null)e.textContent=String(text);if(cls)e.className=cls;return e}
 function libraryURL(url){const u=new URL(url,location.href);return u.hostname===location.hostname||(u.hostname==='freedom-250-observatory.katiekaim.chatgpt.site'&&(/^\/library\//).test(u.pathname))||(u.hostname==='katiekaim-sudo.github.io'&&u.pathname.startsWith('/freedom250-chronicle/library/'))}
 function link(url,label){const a=node('a',label||url);a.href=url;if(/^https?:/.test(url)&&!libraryURL(url)){a.target='_blank';a.rel='noopener'}return a}
 const skip=new Set(['anchor','key','keys','face','col','parent','go','tone','cls','x','y','w','h','ls','source_data','source_section','source_pointer','source_home','source_sha256','schema','artifact_role','doc_id','entity_ids','_as','_bs','_ay','_by','_same']);
 function value(v){const box=node('div',null,'ix-value');if(v==null)return box;
  if(typeof v!=='object'){box.textContent=String(v);return box}
  if(Array.isArray(v)){const ul=node('ul');v.forEach(x=>{const li=node('li');li.append(value(x));ul.append(li)});box.append(ul);return box}
  const u=v.href||v.url;if(typeof u==='string'&&/^(https?:\/\/|\/|#|\.\.\/)/.test(u)){box.append(link(u,v.label||v.text||v.title||u));if(v.date)box.append(node('span',' · '+v.date));const rest=Object.fromEntries(Object.entries(v).filter(([k])=>!['href','url','label','text','title','date'].includes(k)));if(Object.keys(rest).length)box.append(value(rest));return box}
  if(v.badge?.text){box.append(node('p',v.badge.text,'ix-record-badge'));v=Object.fromEntries(Object.entries(v).filter(([k])=>k!=='badge'))}
  if(typeof v.text==='string'){box.append(node('p',v.text));v=Object.fromEntries(Object.entries(v).filter(([k])=>k!=='text'))}
  const dl=node('dl');for(const [k,x] of Object.entries(v)){if(skip.has(k)||x==null||x===''||Array.isArray(x)&&!x.length)continue;dl.append(node('dt',k.replaceAll('_',' ').replace(/^./,s=>s.toUpperCase())));const dd=node('dd');dd.append(value(x));dl.append(dd)}box.append(dl);return box;
 }
 function record(entry){const raw=get(entry.source_path),a=node('article',null,'ix-source-record');if(raw==null){a.append(node('p','This saved entry is unavailable in this page’s data.'));return a}
  const path=entry.source_path,section=D.sections?.[path[1]],cols=section?.columns;
  if(Array.isArray(raw)&&Array.isArray(cols)){const dl=node('dl');raw.forEach((cell,i)=>{dl.append(node('dt',cols[i]||'Field '+(i+1)));const dd=node('dd');dd.append(value(cell));dl.append(dd)});a.append(dl)}else a.append(value(raw));return a;
 }
 let anonymousCard=0;
 function syncCard(card){if(!card.id)card.id='ix-record-card-'+(++anonymousCard);const b=card.querySelector(':scope > .more-btn'),t=card.querySelector(':scope > .t'),more=b?.nextElementSibling;if(!b||!t||!more)return;
  if(!card.dataset.ixReady){card.dataset.ixReady='1';more.id=more.id||card.id+'-details';b.setAttribute('aria-controls',more.id);const title=node('button',null,'ix-record-button');title.type='button';while(t.firstChild)title.append(t.firstChild);title.setAttribute('aria-controls',more.id);t.append(title)}
  const expanded=b.getAttribute('aria-expanded')==='true';card.dataset.ixCard=expanded?'open':'closed';card.querySelector('.ix-record-button')?.setAttribute('aria-expanded',String(expanded));
 }
 function openTarget(id,trigger){if(!id)return;trigger=trigger||[...document.querySelectorAll('[data-go]')].find(el=>el.getAttribute('data-go')===id);lastTrigger=trigger||lastTrigger;
  if(panels[id]){lastTrigger=lastTrigger||document.querySelector('[data-go="'+id+'"]');if(activePanel)activePanel.remove();const p=panels[id],section=node('section',null,'ix-panel');section.id=id;section.setAttribute('role','region');const h=node('h2',p.title||'Matching saved records');h.id=id+'-title';h.tabIndex=-1;section.setAttribute('aria-labelledby',h.id);const close=node('button','Back to graphic','ix-close');close.type='button';close.dataset.ixClose='1';const linked=p.records.filter(x=>x.anchor).length,plainCount=p.records.length-linked,scope=p.records.length===1?'This is the existing saved entry behind the selected item.':linked&&plainCount?linked+' linked records and '+plainCount+' supporting saved '+(plainCount===1?'entry are':'entries are')+' included. Each keeps its own dates and limits.':'All '+p.records.length+' matching saved entries are included. Each keeps its own dates and limits.';section.append(close,h,node('p',scope,'ix-scope'));
   const anchors=p.records.map(x=>x.anchor).filter(Boolean),duplicates=new Set(anchors.filter((x,i)=>anchors.indexOf(x)!==i));
   for(const entry of p.records){const raw=get(entry.source_path);if(entry.anchor&&!duplicates.has(entry.anchor)){const label=raw?.title||raw?.label||raw?.name||entry.anchor;const article=node('article',null,'ix-record-link');article.append(link('#'+entry.anchor,label));if(raw?.sub)article.append(node('p',raw.sub));if(raw?.badge?.text)article.append(node('p',raw.badge.text));section.append(article)}else section.append(record(entry))}
   const research=document.querySelector('.reader-research-primary');if(research){const p=node('p');p.append(link(research.getAttribute('href'),'Continue into the saved research and sources →'));section.append(p)}
   const narrative=document.querySelector('[data-reader-narrative]');if(narrative){const p=node('p');p.append(link(narrative.getAttribute('href'),narrative.textContent));section.append(p)}
   const where=trigger?.closest('.pic')||document.querySelector('#sections')||document.querySelector('main');where?.after(section);activePanel=section;h.focus({preventScroll:true});section.scrollIntoView({block:'start'});return;
  }
  const el=document.getElementById(id);if(!el)return;const b=el.querySelector('.more-btn');if(b&&b.getAttribute('aria-expanded')!=='true')b.click();syncCard(el);document.querySelectorAll('.cd.hit').forEach(c=>c.classList.remove('hit'));el.classList.add('hit');const focus=el.querySelector('.ix-record-button,summary,h2,h3')||el;if(!focus.hasAttribute('tabindex')&&!focus.matches('button,a,summary'))focus.tabIndex=-1;focus.focus({preventScroll:true});el.scrollIntoView({block:'start'});
 }
 function hash(id,trigger){const u=new URL(location.href);u.hash=id;history.pushState(null,'',u.pathname+u.search+u.hash);openTarget(id,trigger)}
 function activate(mark){const url=mark.getAttribute('data-url'),go=mark.getAttribute('data-go');if(url){if(/^https?:/.test(url)&&!libraryURL(url))window.open(url,'_blank','noopener');else location.assign(url)}else if(go){if(/\.html|\//.test(go))location.assign(go);else hash(go,mark)}}
 function caption(mark){const p=mark.closest('.pic'),c=p?.querySelector('.pic-cap');if(c)c.textContent='Summary only: '+plain(mark.getAttribute('data-cap'))}
 function init(){document.querySelectorAll('.cd').forEach(syncCard);
  document.querySelectorAll('.pic').forEach(pic=>{let hasStatic=false;pic.querySelectorAll('[data-go],[data-url]').forEach(mark=>{
   const label=plain(mark.getAttribute('data-cap'))||mark.textContent?.trim()||'Open saved record';
   if(mark.matches('td,th')){const button=node('button',null,'ix-mark-button');button.type='button';for(const k of ['data-go','data-url','data-cap'])if(mark.hasAttribute(k)){button.setAttribute(k,mark.getAttribute(k));if(k!=='data-cap')mark.removeAttribute(k)}while(mark.firstChild)button.append(mark.firstChild);button.setAttribute('aria-label',label);mark.append(button)}else if(!mark.matches('a,button')){mark.setAttribute('role','button');mark.tabIndex=0;mark.setAttribute('aria-label',label)}
  });pic.querySelectorAll('[data-cap]:not([data-go]):not([data-url])').forEach(mark=>{if(mark.querySelector('[data-go],[data-url]'))return;hasStatic=true;mark.dataset.ixSummary='1';mark.setAttribute('role','note');mark.tabIndex=0;mark.setAttribute('aria-label','Summary only: '+plain(mark.getAttribute('data-cap')));const title=mark.querySelector('title');if(title)title.textContent='Summary only: '+plain(mark.getAttribute('data-cap'))});
  pic.querySelectorAll('svg').forEach(svg=>{if(svg.querySelector('[data-go],[data-url]')){svg.removeAttribute('aria-hidden');svg.setAttribute('role','group')}});
  const hint=pic.querySelector('.pic-cap');if(hint)hint.textContent=hasStatic?'Select an item to open its matching records. Marks labelled “Summary only” have no further record on this page.':'Click or tap an item to open its matching saved record. Keyboard: focus an item, then Enter or Space.';
  if(hasStatic){const note=node('p','Includes summary-only marks','ix-summary-note');pic.append(note)}
  });
  document.querySelectorAll('.stat').forEach(card=>{const label=node('span','Summary','ix-static-label');card.prepend(label)});
  if(location.hash)openTarget(decodeURIComponent(location.hash.slice(1)));
 }
 document.addEventListener('click',e=>{
  const close=e.target.closest('[data-ix-close]');if(close){e.preventDefault();activePanel?.remove();activePanel=null;history.replaceState(null,'',location.pathname+location.search);lastTrigger?.focus();return}
  const mark=e.target.closest('[data-go],[data-url]');if(mark?.closest('.pic')){e.preventDefault();e.stopImmediatePropagation();activate(mark);return}
  const summary=e.target.closest('[data-ix-summary]');if(summary?.closest('.pic')){caption(summary);return}
  const card=e.target.closest('.cd'),b=card?.querySelector(':scope > .more-btn');if(!b)return;
  if(e.target.closest('.ix-record-button')){e.preventDefault();b.click();syncCard(card);return}
  if(e.target.closest('.more-btn')){requestAnimationFrame(()=>syncCard(card));return}
  if(e.target.closest('a,button,input,select,textarea,summary,details,label')||window.getSelection()?.toString())return;
  if(b.getAttribute('aria-expanded')!=='true'){b.click();syncCard(card)}
 },true);
 document.addEventListener('keydown',e=>{const mark=e.target.closest('.pic [data-go],.pic [data-url]');if(!mark||mark.matches('button,a'))return;if(e.key==='Enter'||e.key===' '){e.preventDefault();e.stopImmediatePropagation();activate(mark)}} ,true);
 document.addEventListener('focusin',e=>{const m=e.target.closest('[data-ix-summary]');if(m)caption(m)});
 const restore=()=>{if(location.hash)openTarget(decodeURIComponent(location.hash.slice(1)))};window.addEventListener('hashchange',restore);window.addEventListener('popstate',restore);
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init,{once:true});else init();
})();
