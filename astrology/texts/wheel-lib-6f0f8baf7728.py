#!/usr/bin/env python3
"""Shared SVG chart-wheel engine for the Freedom 250 Observatory.

WHEEL_JS holds the canonical `wheelSVG(rec, gname, withOverlay)` JavaScript —
a pure string-builder (no DOM): testable in node, renderable to PNG for visual
verification. Used by build_almanac.py, build_ingress_wheels.py, and
build_lunation_wheels.py. Edit the wheel HERE, then re-run those builders.

rec = {pos:[[name,sign,dms,retro,lon],...], asp:[{t,o,x,ap},...], asc: deg,
       rise?: str, __date: str, cap1?: str, cap2?: str}
A global `CHARTS` (ingress positions) must exist where the overlay is used.
Katie-approved conventions: hand-drawn glyph paths (never font glyphs),
midnight-UT ephemeris, Whole Sign houses, Huber aspect colors, element-tinted
sign band with italic serif sign abbreviations.
"""

WHEEL_JS = r'''// ===== The Wheel — pure-string SVG biwheel (testable outside the DOM) =====
function wheelSVG(rec, gname, withOverlay){
  const SGN=["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"];
  const SAB={Aries:"Ari",Taurus:"Tau",Gemini:"Gem",Cancer:"Can",Leo:"Leo",Virgo:"Vir",Libra:"Lib",Scorpio:"Sco",Sagittarius:"Sag",Capricorn:"Cap",Aquarius:"Aqu",Pisces:"Pis"};
  const PAB={Sun:"Su",Moon:"Mo",Mercury:"Me",Venus:"Ve",Mars:"Ma",Jupiter:"Ju",Saturn:"Sa",Uranus:"Ur",Neptune:"Ne",Pluto:"Pl",Chiron:"Ch",Node:"NN",SNode:"SN",America:"Am",ASC:"AS"};
  const ELEM={Aries:"#b3402e",Leo:"#b3402e",Sagittarius:"#b3402e",Taurus:"#4a7d5f",Virgo:"#4a7d5f",Capricorn:"#4a7d5f",Gemini:"#a8821f",Libra:"#a8821f",Aquarius:"#a8821f",Cancer:"#3a6ea5",Scorpio:"#3a6ea5",Pisces:"#3a6ea5"};
  const ASPC={conjunct:"#c9a227",semisextile:"#5a8a4a",sextile:"#3a6ea5",trine:"#3a6ea5",square:"#b3402e",opposite:"#b3402e",quincunx:"#5a8a4a"};
  const PCOL={Sun:"#b07d2b",Moon:"#8d7960",Mercury:"#7b5ea7",Venus:"#2e8b74",Mars:"#c0504d",Jupiter:"#5b554a",Saturn:"#7a2e1d",Uranus:"#3a6ea5",Neptune:"#4a5fa5",Pluto:"#6e3d5e",Chiron:"#a3622e",Node:"#6b6257",SNode:"#9a917f",America:"#1d3f8c"};
  // hand-drawn glyph paths in a 20x20 box — immune to emoji font substitution
  const GLY={
   Sun:'<circle cx="10" cy="10" r="5.6"/><circle cx="10" cy="10" r="1.5" fill="currentColor" stroke="none"/>',
   Moon:'<path d="M 11.5 3.9 A 6.3 6.3 0 1 0 11.5 16.1 A 7.1 7.1 0 0 1 11.5 3.9 Z" fill="currentColor" stroke="none"/>',
   Mercury:'<circle cx="10" cy="8.6" r="3.4"/><path d="M 6.6 2.4 A 3.5 3.5 0 0 0 13.4 2.4"/><line x1="10" y1="12" x2="10" y2="17.4"/><line x1="7.2" y1="14.7" x2="12.8" y2="14.7"/>',
   Venus:'<circle cx="10" cy="7.2" r="4.1"/><line x1="10" y1="11.3" x2="10" y2="17.6"/><line x1="6.9" y1="14.4" x2="13.1" y2="14.4"/>',
   Mars:'<circle cx="8.4" cy="11.6" r="4.3"/><line x1="11.5" y1="8.5" x2="15.9" y2="4.1"/><polyline points="12.3,4.1 15.9,4.1 15.9,7.7" fill="none"/>',
   Jupiter:'<path d="M 4.4 6.4 A 3.5 3.5 0 0 1 11.2 5.6 Q 11.2 9.4 5.2 13.1 L 16 13.1" fill="none"/><line x1="12.9" y1="9.4" x2="12.9" y2="17.4"/>',
   Saturn:'<line x1="7.4" y1="3.2" x2="7.4" y2="11"/><line x1="4.8" y1="5.8" x2="10" y2="5.8"/><path d="M 7.4 11 Q 7.4 8.9 9.9 8.9 Q 12.9 8.9 12.9 12 Q 12.9 14.6 10.5 16 Q 9.9 16.5 10.4 17.5" fill="none"/>',
   Uranus:'<line x1="5.7" y1="3.4" x2="5.7" y2="11"/><line x1="14.3" y1="3.4" x2="14.3" y2="11"/><line x1="5.7" y1="7.2" x2="14.3" y2="7.2"/><line x1="10" y1="7.2" x2="10" y2="12.3"/><circle cx="10" cy="14.7" r="2.5"/><circle cx="10" cy="14.7" r="0.9" fill="currentColor" stroke="none"/>',
   Neptune:'<path d="M 4.6 3.8 Q 4.6 10.4 10 10.4 Q 15.4 10.4 15.4 3.8" fill="none"/><line x1="10" y1="3.4" x2="10" y2="17.2"/><line x1="6.9" y1="14.2" x2="13.1" y2="14.2"/>',
   Pluto:'<circle cx="10" cy="5.4" r="2.1"/><path d="M 5.8 6 A 4.2 4.2 0 0 0 14.2 6" fill="none"/><line x1="10" y1="10.2" x2="10" y2="17.4"/><line x1="7" y1="14.2" x2="13" y2="14.2"/>',
   Chiron:'<circle cx="10" cy="14.6" r="3.1"/><line x1="10" y1="2.2" x2="10" y2="11.5"/><line x1="10" y1="7.6" x2="14.4" y2="3.4"/><line x1="10" y1="7.6" x2="14.4" y2="11.4"/>',
   Node:'<circle cx="5.6" cy="15.2" r="1.9"/><circle cx="14.4" cy="15.2" r="1.9"/><path d="M 6.9 13.8 A 6.4 6.4 0 1 1 13.1 13.8" fill="none"/>',
   SNode:'<circle cx="5.6" cy="4.8" r="1.9"/><circle cx="14.4" cy="4.8" r="1.9"/><path d="M 6.9 6.2 A 6.4 6.4 0 1 0 13.1 6.2" fill="none"/>',
   America:'<path d="M 10 2.8 L 8.35 7.73 L 3.34 7.84 L 7.34 10.87 L 5.89 15.66 L 10 12.8 L 14.11 15.66 L 12.66 10.87 L 16.66 7.84 L 11.65 7.73 Z" fill="none" stroke-linejoin="round"/>'
  };
  const KKSIGNS=["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"];
  const KKPLANETS={Sun:1,Moon:1,Mercury:1,Venus:1,Mars:1,Jupiter:1,Saturn:1,Uranus:1,Neptune:1,Pluto:1};
  function kkspec(name,L){ if(!KKPLANETS[name])return "";
    const sg=KKSIGNS[Math.floor((((L%360)+360)%360)/30)];
    return "planet:"+name+";sign:"+sg; }
  function glyph(name,x,y,scale,color,sw,kk){
    return `<g transform="translate(${f2(x-10*scale)} ${f2(y-10*scale)}) scale(${scale})" color="${color}" stroke="currentColor" stroke-width="${sw||1.5}" stroke-linecap="round" fill="none"${kk?` data-kk="${kk}" style="cursor:pointer"`:""}>${kk?`<circle cx="10" cy="10" r="13" fill="transparent" stroke="none"/>`:""}${GLY[name]||""}</g>`;
  }
  const cx=330, cy=330;
  // gname may be a single chart name (classic) or an array of names (multi-ring overlay)
  const gnames = Array.isArray(gname) ? gname : (gname ? [gname] : []);
  const ovCharts = withOverlay ? gnames.map(function(n){
      return {name:n, c:(n && typeof CHARTS!=="undefined" && CHARTS && CHARTS[n])||null};
    }).filter(function(o){return o.c;}) : [];
  const chart = ovCharts.length ? ovCharts[0].c
    : ((gnames[0] && typeof CHARTS!=="undefined" && CHARTS && CHARTS[gnames[0]])||null);
  const ov = ovCharts.length>0;
  const asc = (rec.asc!==null && rec.asc!==undefined) ? rec.asc : (chart ? chart.ASC : 0);
  const cusp = Math.floor(asc/30)*30;
  // optional Placidus cusps (12 longitudes; [0]=Asc,[9]=MC) — enables the WS/Placidus toggle
  const placCusps = (rec.cusps && rec.cusps.length===12) ? rec.cusps.map(Number) : null;
  const placMc = (rec.mc!==undefined && rec.mc!==null) ? Number(rec.mc) : (placCusps?placCusps[9]:null);
  function pt(r, L){ const a=(180+(L-cusp))*Math.PI/180; return [cx+r*Math.cos(a), cy-r*Math.sin(a)]; }
  function f2(x){ return Math.round(x*100)/100; }
  const s=[];
  const EXT = Math.max(0, ovCharts.length-1)*38;  // extra rings expand the canvas
  s.push('<svg class="f250-wheel" viewBox="'+(-EXT)+' '+(-EXT)+' '+(660+2*EXT)+' '+(660+2*EXT)+'" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block" font-family="Iowan Old Style,Palatino,Georgia,serif">');
  // zodiac band
  for(let i=0;i<12;i++){
    const a1=i*30, a2=a1+30;
    const [x1,y1]=pt(276,a1),[x2,y2]=pt(276,a2),[x3,y3]=pt(240,a2),[x4,y4]=pt(240,a1);
    s.push(`<path d="M${f2(x1)} ${f2(y1)} A276 276 0 0 0 ${f2(x2)} ${f2(y2)} L${f2(x3)} ${f2(y3)} A240 240 0 0 1 ${f2(x4)} ${f2(y4)} Z" fill="${ELEM[SGN[i]]}" fill-opacity="0.10" stroke="#d9cfb8" stroke-width="1"/>`);
    const [lx,ly]=pt(258,a1+15);
    s.push(`<text x="${f2(lx)}" y="${f2(ly)}" text-anchor="middle" dominant-baseline="central" font-size="13.5" font-style="italic" fill="${ELEM[SGN[i]]}">${SAB[SGN[i]]}</text>`);
  }
  // degree ticks every 10
  for(let L=0;L<360;L+=10){
    const big=(L%30===0);
    const [x1,y1]=pt(240,L),[x2,y2]=pt(big?232:236,L);
    s.push(`<line x1="${f2(x1)}" y1="${f2(y1)}" x2="${f2(x2)}" y2="${f2(y2)}" stroke="#c9bda0" stroke-width="${big?1.4:0.7}"/>`);
  }
  s.push(`<circle cx="${cx}" cy="${cy}" r="240" fill="none" stroke="#d9cfb8" stroke-width="1"/>`);
  s.push(`<circle cx="${cx}" cy="${cy}" r="148" fill="none" stroke="#e7dcc2" stroke-width="1"/>`);
  // ===== house systems: Whole Sign (default) + optional Placidus, toggleable =====
  // -- Whole Sign layer (the analytical default) --
  s.push('<g class="f250-hs f250-hs-ws">');
  {
    const ascIdx=Math.floor(asc/30);
    for(let i=0;i<12;i++){
      const L=((ascIdx+i)%12)*30;
      const [x1,y1]=pt(148,L),[x2,y2]=pt(240,L);
      s.push(`<line x1="${f2(x1)}" y1="${f2(y1)}" x2="${f2(x2)}" y2="${f2(y2)}" stroke="#e7dcc2" stroke-width="0.8"/>`);
      const [hx,hy]=pt(160,L+15);
      s.push(`<text x="${f2(hx)}" y="${f2(hy)}" text-anchor="middle" dominant-baseline="central" font-size="9.5" fill="#b5a98c">${i+1}</text>`);
    }
  }
  s.push('</g>');
  // -- Placidus layer (hidden by default; drawn only when cusps are supplied) --
  if(placCusps){
    s.push('<g class="f250-hs f250-hs-pla" style="display:none">');
    // intercepted signs: a sign that contains NO cusp is swallowed inside one house
    const cuspSign=placCusps.map(c=>Math.floor((((c%360)+360)%360)/30));
    for(let sg=0;sg<12;sg++){
      if(cuspSign.indexOf(sg)===-1){
        const a1=sg*30,a2=a1+30;
        const [x1,y1]=pt(276,a1),[x2,y2]=pt(276,a2),[x3,y3]=pt(240,a2),[x4,y4]=pt(240,a1);
        s.push(`<path d="M${f2(x1)} ${f2(y1)} A276 276 0 0 0 ${f2(x2)} ${f2(y2)} L${f2(x3)} ${f2(y3)} A240 240 0 0 1 ${f2(x4)} ${f2(y4)} Z" fill="#7a2e1d" fill-opacity="0.13" stroke="none"/>`);
        const [ilx,ily]=pt(286,a1+15);
        s.push(`<text x="${f2(ilx)}" y="${f2(ily)}" text-anchor="middle" dominant-baseline="central" font-size="7" fill="#7a2e1d" font-style="italic">intercept</text>`);
      }
    }
    // unequal cusp spokes + house numbers (angular cusps emphasized)
    for(let i=0;i<12;i++){
      const c=placCusps[i], cn=placCusps[(i+1)%12];
      const ang=(i===0||i===3||i===6||i===9);
      const [x1,y1]=pt(148,c),[x2,y2]=pt(240,c);
      s.push(`<line x1="${f2(x1)}" y1="${f2(y1)}" x2="${f2(x2)}" y2="${f2(y2)}" stroke="${ang?'#b89a5a':'#e0d4b8'}" stroke-width="${ang?1.3:0.8}"/>`);
      let span=(((cn-c)%360)+360)%360; const midL=(c+span/2)%360;
      const [hx,hy]=pt(162,midL);
      s.push(`<text x="${f2(hx)}" y="${f2(hy)}" text-anchor="middle" dominant-baseline="central" font-size="9.5" fill="#a8821f" font-weight="bold">${i+1}</text>`);
    }
    if(placMc!==null){
      const [m1x,m1y]=pt(240,placMc),[m2x,m2y]=pt(292,placMc);
      s.push(`<line x1="${f2(m1x)}" y1="${f2(m1y)}" x2="${f2(m2x)}" y2="${f2(m2y)}" stroke="#7a2e1d" stroke-width="1.3" stroke-dasharray="2 2"/>`);
      const [mtx,mty]=pt(304,placMc);
      s.push(`<text x="${f2(mtx)}" y="${f2(mty)}" text-anchor="middle" dominant-baseline="central" font-size="10" font-weight="bold" fill="#7a2e1d">MC</text>`);
    }
    s.push('</g>');
  }
  // ASC arrow at the exact Ascendant degree (shared by both house systems).
  // rec.noAsLabel (sunrise charts — estimated AS) keeps the line but drops the "AS" letters
  {
    const [ax1,ay1]=pt(240,asc),[ax2,ay2]=pt(rec.noAsLabel?286:290,asc);
    s.push(`<line x1="${f2(ax1)}" y1="${f2(ay1)}" x2="${f2(ax2)}" y2="${f2(ay2)}" stroke="#7a2e1d" stroke-width="1.6"${rec.noAsLabel?' stroke-dasharray="5 3"':''}/>`);
    if(!rec.noAsLabel){
      const [atx,aty]=pt(302,asc);
      s.push(`<text x="${f2(atx)}" y="${f2(aty)}" text-anchor="middle" dominant-baseline="central" font-size="11" font-weight="bold" fill="#7a2e1d">AS</text>`);
    }
  }
  // WS/Placidus toggle (only when Placidus cusps are present)
  if(placCusps){
    const bx=-EXT+12, by=-EXT+12;
    s.push(`<g class="f250-htoggle" font-size="11">`);
    s.push(`<g data-hbtn="ws" style="cursor:pointer"><rect x="${bx}" y="${by}" width="94" height="21" rx="10.5" fill="#7a2e1d" stroke="#7a2e1d"/><text x="${bx+47}" y="${by+11}" text-anchor="middle" dominant-baseline="central" fill="#fff">Whole Sign</text></g>`);
    s.push(`<g data-hbtn="pla" style="cursor:pointer"><rect x="${bx+100}" y="${by}" width="80" height="21" rx="10.5" fill="#f5efe2" stroke="#c9bda0"/><text x="${bx+100+40}" y="${by+11}" text-anchor="middle" dominant-baseline="central" fill="#7a2e1d">Placidus</text></g>`);
    s.push(`</g>`);
  }
  // fan-out helper
  function fan(items){ // items: [{key,L}] -> Map key->display angle (v5 centered clusters)
    // v5 (2026-06-10): forward-push fan replaced — it let late-sign clusters
    // collide across 0° Aries and dragged glyphs far downwind. Now planets
    // merge into clusters; each cluster spreads symmetrically around the
    // circular mean of its TRUE degrees, so drift is minimal and wrap-safe.
    const GAP=8, norm=L=>((L%360)+360)%360;
    let clusters=items.map(o=>({mem:[o]}));
    const cen=cl=>{let x=0,y=0;cl.mem.forEach(m=>{const r=norm(m.L)*Math.PI/180;x+=Math.cos(r);y+=Math.sin(r);});return norm(Math.atan2(y,x)*180/Math.PI);};
    const half=cl=>(cl.mem.length-1)*GAP/2;
    for(let guard=0;guard<60;guard++){
      clusters.forEach(cl=>cl.c=cen(cl));
      clusters.sort((a,b)=>a.c-b.c);
      let merged=false;
      for(let i=0;i<clusters.length&&clusters.length>1;i++){
        const a=clusters[i], b=clusters[(i+1)%clusters.length];
        if(norm(b.c-a.c)-half(a)-half(b)<GAP){
          a.mem=a.mem.concat(b.mem); clusters.splice(clusters.indexOf(b),1); merged=true; break;
        }
      }
      if(!merged) break;
    }
    const map=new Map();
    clusters.forEach(cl=>{
      const c=cen(cl), n=cl.mem.length;
      const ord=cl.mem.slice().sort((x,y)=>(((norm(x.L)-c+540)%360)-180)-(((norm(y.L)-c+540)%360)-180));
      ord.forEach((m,i)=>map.set(m.key, norm(c-(n-1)*GAP/2+i*GAP)));
    });
    return map;
  }
  // aspect lines (inner)
  const lonOf={}; rec.pos.forEach(p=>lonOf[p[0]]=p[4]);
  rec.asp.forEach(a=>{
    const w=a.t.split(" "); const l1=lonOf[w[0]], l2=lonOf[w[2]];
    if(l1===undefined||l2===undefined) return;
    const [x1,y1]=pt(146,l1),[x2,y2]=pt(146,l2);
    const c=ASPC[w[1]]||"#8a8377";
    s.push(`<line x1="${f2(x1)}" y1="${f2(y1)}" x2="${f2(x2)}" y2="${f2(y2)}" stroke="${c}" stroke-width="${a.x?2.4:(a.o<=1?1.7:1)}" stroke-opacity="${a.o<=1?0.9:0.45}"/>`);
  });
  // transit planets — Astro Gold-style layout v4 (2026-06-10, Katie-approved):
  // ONE radius, glyphs side by side with degrees below, planets SPREAD to fill
  // their sign's wedge when crowded (never crossing a sign boundary). The rim
  // tick + a thin connector still mark each planet's true degree.
  function layoutPlanets(items){
    const out=new Map();
    const bySign={};
    items.forEach(m=>{
      const k=Math.floor((((m.L%360)+360)%360)/30);
      (bySign[k]=bySign[k]||[]).push(m);
    });
    Object.keys(bySign).forEach(k=>{
      const g=bySign[k].slice().sort((a,b)=>a.L-b.L);
      const s0=Number(k)*30, n=g.length;
      const lo=s0+4.5, hi=s0+25.5;                       // stay inside the wedge
      const GAP=n>1?Math.min(9,(hi-lo)/(n-1)):0;         // side-by-side spacing
      const D=g.map(m=>Math.max(lo,Math.min(hi,m.L)));
      for(let i=1;i<n;i++) if(D[i]<D[i-1]+GAP) D[i]=D[i-1]+GAP;
      for(let i=n-1;i>=0;i--){const cap=hi-(n-1-i)*GAP; if(D[i]>cap)D[i]=cap;}
      for(let i=1;i<n;i++) if(D[i]<D[i-1]+GAP) D[i]=D[i-1]+GAP;
      g.forEach((m,i)=>out.set(m.key,D[i]));
    });
    return out;
  }
  const tLay=layoutPlanets(rec.pos.map(p=>({key:p[0],L:p[4]})));
  rec.pos.forEach(p=>{
    const L=p[4], D=tLay.has(p[0])?tLay.get(p[0]):L;
    const [tx1,ty1]=pt(240,L),[tx2,ty2]=pt(228,L);
    s.push(`<line x1="${f2(tx1)}" y1="${f2(ty1)}" x2="${f2(tx2)}" y2="${f2(ty2)}" stroke="#5b554a" stroke-width="1.3"/>`);
    const [dx,dy]=pt(146,L);
    s.push(`<circle cx="${f2(dx)}" cy="${f2(dy)}" r="2.2" fill="#5b554a"/>`);
    const [px,py]=pt(206,D);
    s.push(glyph(p[0],px,py,1.05,PCOL[p[0]]||"#23201a",1.6,kkspec(p[0],L)));
    const [qx,qy]=pt(184,D);
    s.push(`<text x="${f2(qx)}" y="${f2(qy)}" text-anchor="middle" dominant-baseline="central" font-size="8.5" fill="#8a8377">${p[2]}${p[3]?" ℞":""}</text>`);
    // thin connector from the glyph out to its true-degree tick when shifted
    const shift=Math.abs((D-L+180)%360-180);
    if(shift>1.5){ const [c1x,c1y]=pt(218,D),[c2x,c2y]=pt(226,L);
      s.push(`<line x1="${f2(c1x)}" y1="${f2(c1y)}" x2="${f2(c2x)}" y2="${f2(c2y)}" stroke="#c9bda0" stroke-width="0.6"/>`); }
  });
  // overlay ring(s) — classic single governing chart, or several stacked rings
  if(ov){
    const RINGC=["#9b6a3f","#3a6ea5","#6e3d5e"];
    ovCharts.forEach(function(oc,ri){
      const off=38*ri, col=RINGC[ri%3];
      if(ri>0) s.push(`<circle cx="${cx}" cy="${cy}" r="${276+off}" fill="none" stroke="${col}" stroke-opacity="0.25" stroke-width="1"/>`);
      const pts=Object.entries(oc.c).filter(([k])=>k!=="ASC").map(([k,v])=>({key:k,L:v}));
      // reserve the AS arrow/label's angle so no overlay glyph hides beneath it
      // (not needed when the label is dropped — sunrise charts)
      const oFan=fan(rec.noAsLabel?pts:pts.concat([{key:"__asc",L:asc}]));
      pts.forEach(o=>{
        const [x1,y1]=pt(276+off,o.L),[x2,y2]=pt(286+off,o.L);
        s.push(`<line x1="${f2(x1)}" y1="${f2(y1)}" x2="${f2(x2)}" y2="${f2(y2)}" stroke="${col}" stroke-width="1.4"/>`);
        const D=oFan.get(o.key);
        const [lx,ly]=pt(299+off,D);
        if(GLY[o.key]) s.push(glyph(o.key,lx,ly,0.66,col,1.9,kkspec(o.key,o.L)));
        else s.push(`<text x="${f2(lx)}" y="${f2(ly)}" text-anchor="middle" dominant-baseline="central" font-size="10" font-weight="bold" fill="${col}">${PAB[o.key]||o.key}</text>`);
        const [mx,my]=pt(313+off,D);
        s.push(`<text x="${f2(mx)}" y="${f2(my)}" text-anchor="middle" dominant-baseline="central" font-size="7.5" fill="${col}" fill-opacity="0.75">${Math.floor(o.L%30)}°</text>`);
        // thin connector back to the true-degree tick when fanned away
        const oShift=Math.abs((D-o.L+540)%360-180);
        if(oShift>4){ const [k1x,k1y]=pt(292+off,D),[k2x,k2y]=pt(287+off,o.L);
          s.push(`<line x1="${f2(k1x)}" y1="${f2(k1y)}" x2="${f2(k2x)}" y2="${f2(k2y)}" stroke="${col}" stroke-opacity="0.45" stroke-width="0.6"/>`); }
      });
    });
  }
  // center
  s.push(`<text x="${cx}" y="${cy-14}" text-anchor="middle" font-size="12" font-weight="bold" fill="#5b554a">${rec.__date||""}</text>`);
  const cap1 = rec.cap1 || (rec.rise ? ("sunrise "+rec.rise+" ET · houses from the day's ASC") : "houses from the chart Ascendant");
  const cap2 = rec.cap2 || (ov ? (ovCharts.length>1 ? "rings: "+ovCharts.map(function(o){return o.name;}).join(" · ") : ovCharts[0].name+" ingress on the outer ring") : "planets: midnight UT");
  s.push(`<text x="${cx}" y="${cy+3}" text-anchor="middle" font-size="9" font-style="italic" fill="#8a8377">${cap1}</text>`);
  s.push(`<text x="${cx}" y="${cy+18}" text-anchor="middle" font-size="9" font-style="italic" fill="#8a8377">${cap2}</text>`);
  s.push('</svg>');
  return s.join("");
}
// one delegated, idempotent listener handles the WS/Placidus toggle on every wheel
;(function(){
  if(typeof document==="undefined"||window.__f250HouseToggle)return;
  window.__f250HouseToggle=1;
  document.addEventListener("click",function(ev){
    var b=(ev.target&&ev.target.closest)?ev.target.closest("[data-hbtn]"):null;
    if(!b)return;
    var svg=b.closest("svg.f250-wheel"); if(!svg)return;
    var pla=svg.querySelector(".f250-hs-pla"), ws=svg.querySelector(".f250-hs-ws");
    if(!pla)return;
    var on=(b.getAttribute("data-hbtn")==="pla");
    if(ws)ws.style.display=on?"none":"";
    pla.style.display=on?"":"none";
    var bw=svg.querySelector('[data-hbtn="ws"] rect'), bp=svg.querySelector('[data-hbtn="pla"] rect');
    var tw=svg.querySelector('[data-hbtn="ws"] text'), tp=svg.querySelector('[data-hbtn="pla"] text');
    if(bw){bw.setAttribute("fill",on?"#f5efe2":"#7a2e1d");bw.setAttribute("stroke",on?"#c9bda0":"#7a2e1d");}
    if(tw)tw.setAttribute("fill",on?"#7a2e1d":"#fff");
    if(bp){bp.setAttribute("fill",on?"#7a2e1d":"#f5efe2");bp.setAttribute("stroke",on?"#7a2e1d":"#c9bda0");}
    if(tp)tp.setAttribute("fill",on?"#fff":"#7a2e1d");
  });
})();'''

def placidus_cusps(jd_ut, lat, lon):
    """Placidus house cusps for a chart, for the wheel's WS/Placidus toggle.
    Returns (cusps12, mc): cusps12 = 12 ecliptic longitudes for houses 1..12
    (cusps12[0] = Ascendant, cusps12[9] = MC). Attach to a rec as
    rec['cusps'] = cusps12 ; rec['mc'] = mc. Whole Sign stays the default view."""
    import swisseph as swe
    cusps, ascmc = swe.houses(jd_ut, lat, lon, b'P')
    c = list(cusps)
    if len(c) >= 13:            # some builds return a 1-indexed length-13 tuple
        c = c[1:13]
    return [round(x % 360, 4) for x in c[:12]], round(ascmc[1] % 360, 4)


ASPECT_DEFS = [(0, "conjunct"), (30, "semisextile"), (60, "sextile"), (90, "square"),
               (120, "trine"), (150, "quincunx"), (180, "opposite")]

def point_aspects(point_lons, lons, cap=2.0):
    """Katie's tight policy for the minor points (Chiron / Node / America):
    conjunction, square, opposition only, ≤2° orb, point-to-planet only
    (no point-to-point pairs — noise). Returns wheel-format aspect dicts."""
    out = []
    for pn, pl in point_lons.items():
        for qn, ql in lons.items():
            sep = abs((pl - ql + 180) % 360 - 180)
            for ang, nm in [(0, "conjunct"), (90, "square"), (180, "opposite")]:
                orb = abs(sep - ang)
                if orb <= cap:
                    out.append({"t": f"{pn} {nm} {qn}", "o": round(orb, 2),
                                "x": 1 if orb <= 0.3 else 0, "ap": 0, "pt": 1})
    out.sort(key=lambda a: a["o"])
    return out

def aspects_between(lons, moon_name="Moon", cap_major=3.0, cap_tight=2.0):
    """lons: {planet: longitude}. Returns aspect dicts in the wheel's format."""
    keys = list(lons)
    out = []
    for i, p1 in enumerate(keys):
        for p2 in keys[i+1:]:
            sep = abs((lons[p1] - lons[p2] + 180) % 360 - 180)
            for ang, nm in ASPECT_DEFS:
                cap = cap_tight if (moon_name in (p1, p2) or ang == 30) else cap_major
                orb = abs(sep - ang)
                if orb <= cap:
                    out.append({"t": f"{p1} {nm} {p2}", "o": round(orb, 2),
                                "x": 1 if orb <= 0.3 else 0, "ap": 0})
    out.sort(key=lambda a: a["o"])
    return out
