import json, html
from decor import CLOUD, INKLINE, SEAL, PAPER
IT = json.load(open('items.json', encoding='utf-8'))
for i, x in enumerate(IT, 1): x['n'] = i
LIVE = 'https://xn--hq1b348b.kr/'
FONTS = f'<link rel="stylesheet" href="{LIVE}fonts/fonts.css"><link rel="stylesheet" href="{LIVE}fonts/fonts-zh.css">'
NAV = ['소장품', '감정', '인증 조회', '위탁·판매', '디지털 자산', '소식·행사', '센터 소개', '문의']
E = html.escape
def cut(x): return f'img/g/{x["ph"][0]}.webp'
def orig(k): return f'{LIVE}img/{k}.webp'
HERO = next(x for x in IT if x['id'] == 'cs07')

JS = '''<script>
const RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.18});
document.querySelectorAll('[data-ink]').forEach(el=>RM?el.classList.add('in'):io.observe(el));
if(!RM){const ps=[...document.querySelectorAll('[data-par]')];let t=0;addEventListener('scroll',()=>{if(t)return;t=requestAnimationFrame(()=>{t=0;ps.forEach(p=>{const r=p.getBoundingClientRect();const k=(r.top+r.height/2-innerHeight/2)/innerHeight;p.style.transform=`translate3d(0,${(k*-18).toFixed(1)}px,0) scale(${(1.02-Math.abs(k)*.02).toFixed(3)})`})})},{passive:true})}
const vt=f=>document.startViewTransition&&!RM?document.startViewTransition(f):f();
document.querySelectorAll('[data-open]').forEach(b=>b.addEventListener('click',e=>{e.preventDefault();const id=b.dataset.open;vt(()=>showItem(id))}));
function showItem(id){const x=ITEMS.find(i=>i.id===id);const d=document.getElementById('detail');if(!x||!d)return;
 d.querySelector('[data-f=t]').textContent=x.t;d.querySelector('[data-f=era]').textContent=x.era;d.querySelector('[data-f=size]').textContent=x.size;d.querySelector('[data-f=no]').textContent=x.no;d.querySelector('[data-f=n]').textContent=String(x.n).padStart(2,'0');d.querySelector('[data-f=docs]').textContent=x.docs;
 const m=d.querySelector('.d-main img');m.src='img/g/'+x.ph[0]+'.webp';m.alt=x.t;
 d.querySelector('.d-th').innerHTML=x.ph.map((k,i)=>`<button type="button" aria-label="사진 ${i+1} 크게 보기" data-z="${LIVE}img/${k}.webp"><img loading="lazy" src="${LIVE}img/${k}.webp" alt=""></button>`).join('');
 document.querySelectorAll('.room [data-open]').forEach(c=>c.setAttribute('aria-current',c.dataset.open===id?'true':'false'));
 d.hidden=false;d.scrollIntoView({behavior:RM?'auto':'smooth',block:'start'})}
const LIVE="'''+LIVE+'''";
document.addEventListener('click',e=>{const z=e.target.closest('[data-z],.d-main');if(!z)return;const src=z.dataset.z||z.querySelector('img').src;const o=document.createElement('div');o.className='zoom';o.setAttribute('role','dialog');o.setAttribute('aria-label','확대 보기');o.innerHTML=`<img src="${src}" alt=""><button type="button" class="z-x" aria-label="닫기">닫기</button>`;document.body.append(o);const im=o.querySelector('img');let on=false;
 im.addEventListener('click',ev=>{on=!on;const r=im.getBoundingClientRect();im.style.transformOrigin=`${(ev.clientX-r.left)/r.width*100}% ${(ev.clientY-r.top)/r.height*100}%`;im.style.transform=on?'scale(2.2)':'none'});
 const close=()=>{o.remove();z.focus&&z.focus()};o.querySelector('.z-x').onclick=close;o.addEventListener('keydown',ev=>{if(ev.key==='Escape')close()});o.tabIndex=-1;o.querySelector('.z-x').focus()});
</script>'''

def items_js(): return '<script>const ITEMS=' + json.dumps(IT, ensure_ascii=False) + ';</script>'

BASE_CSS = '''
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}html,body{overflow-x:clip}body{margin:0}
img{max-width:100%;display:block}a{color:inherit}
:focus-visible{outline:2px solid var(--focus);outline-offset:3px}
.skip{position:absolute;left:-999px}.skip:focus{left:12px;top:12px;z-index:50;background:var(--paper);padding:8px 12px}
.wrap{max-width:1320px;margin:0 auto;padding:0 clamp(16px,4vw,48px)}
.vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
@view-transition{navigation:auto}
::view-transition-old(root),::view-transition-new(root){animation-duration:.45s}
[data-ink]{--r:0%;-webkit-mask:radial-gradient(circle at 30% 40%,#000 var(--r),transparent calc(var(--r) + 18%));mask:radial-gradient(circle at 30% 40%,#000 var(--r),transparent calc(var(--r) + 18%));transition:--r 1.4s cubic-bezier(.2,.7,.2,1)}
[data-ink].in{--r:160%}
@property --r{syntax:'<percentage>';inherits:false;initial-value:0%}
.zoom{position:fixed;inset:0;z-index:100;background:rgba(20,18,15,.92);display:grid;place-items:center;overflow:hidden}
.zoom img{max-width:92vw;max-height:88vh;cursor:zoom-in;transition:transform .35s}
.z-x{position:absolute;top:16px;right:16px;background:#fff;border:0;padding:10px 16px;font:inherit;cursor:pointer}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important}[data-ink]{-webkit-mask:none;mask:none}::view-transition-group(*){animation:none!important}}
'''

# ======================= A안: 도록(圖錄) =======================
A_CSS = BASE_CSS + '''
:root{--paper:#f4eee2;--paper2:#ebe2d1;--ink:#1d1a16;--ink2:#4b443a;--gold:#7a5b22;--goldl:#b8924a;--seal:#a3301f;--line:#d6c8ae;--focus:#a3301f;
 --serif:"Noto Serif KR Variable","Noto Serif KR","Nanum Myeongjo",serif;--sans:"Pretendard Variable",Pretendard,-apple-system,"Apple SD Gothic Neo",sans-serif;--han:"Noto Serif TC Variable","Noto Serif KR Variable",serif}
body{background:var(--paper) url("''' + PAPER + '''");color:var(--ink);font:400 16px/1.75 var(--sans);letter-spacing:-.005em;word-break:keep-all;overflow-wrap:anywhere}
h1,h2,h3{font-family:var(--serif);font-weight:400;letter-spacing:-.02em;margin:0}
header.top{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--paper) 92%,transparent);backdrop-filter:blur(6px);border-bottom:1px solid var(--line)}
.top .wrap{display:flex;align-items:center;gap:28px;height:72px}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none}.brand img{height:42px;width:auto;mix-blend-mode:multiply}.brand b{font:600 17px/1.2 var(--serif);letter-spacing:-.03em}.brand small{display:block;font:400 11px var(--han);color:var(--ink2);letter-spacing:.12em}
nav.m{display:flex;gap:22px;margin-left:auto;font-size:14.5px}nav.m a{text-decoration:none;padding:6px 0;border-bottom:1px solid transparent}nav.m a:hover,nav.m a[aria-current]{border-color:var(--seal)}
.lg{display:flex;gap:2px;font-size:12.5px}.lg button{border:1px solid var(--line);background:none;padding:5px 8px;font:inherit;color:var(--ink2)}.lg button[aria-pressed=true]{background:var(--ink);color:var(--paper);border-color:var(--ink)}
/* hero: 도록 펼침면 */
.hero{display:grid;grid-template-columns:96px minmax(0,1.15fr) minmax(0,1fr);gap:0 clamp(20px,4vw,64px);padding:clamp(32px,6vw,88px) 0 40px;align-items:end;min-height:min(86vh,860px)}
.vcol{align-self:stretch;display:flex;flex-direction:column;align-items:center;justify-content:space-between;border-right:1px solid var(--line);padding-right:28px}
.vcol .v{writing-mode:vertical-rl;font:300 clamp(64px,7vw,104px)/1 var(--han);letter-spacing:.18em;color:var(--ink)}
.vcol .vs{writing-mode:vertical-rl;font:400 13px/1 var(--han);letter-spacing:.4em;color:var(--ink2)}
.seal{width:62px;color:var(--seal);transform:rotate(-3deg)}
.plate{position:relative;align-self:stretch;display:grid;place-items:end center;padding-bottom:30px}
.plate::before{content:"";position:absolute;inset:6% 4% 0;background:radial-gradient(60% 46% at 50% 54%,#fffaf0 0,rgba(255,250,240,.0) 70%)}
.plate .shadow{position:absolute;bottom:22px;left:22%;right:22%;height:34px;background:radial-gradient(closest-side,rgba(45,35,20,.38),transparent);filter:blur(4px)}
.plate img{position:relative;max-height:min(70vh,700px);width:auto;view-transition-name:hero-obj;will-change:transform}
.cap{font-size:13.5px;color:var(--ink2);line-height:1.6;border-top:1px solid var(--ink);padding-top:10px;max-width:340px}
.cap b{display:block;font:500 15px/1.5 var(--serif);color:var(--ink)}
.txt h1{font-size:clamp(32px,3.7vw,56px);line-height:1.22;font-weight:350}
.txt h1 span{display:block}
.txt p{font-size:17px;max-width:30em;color:var(--ink2);margin:26px 0 30px}
.btns{display:flex;gap:10px;flex-wrap:wrap}
.btn{display:inline-flex;align-items:center;min-height:46px;padding:0 22px;border:1px solid var(--ink);text-decoration:none;font-size:15px;background:var(--ink);color:var(--paper)}
.btn.o{background:transparent;color:var(--ink)}
.btn:hover{background:var(--seal);border-color:var(--seal);color:#fff}
.cloud{display:block;color:var(--goldl);width:150px;margin:0 0 22px}.cloud svg{width:100%;height:auto}
.inkline{color:var(--ink);height:14px;width:100%;opacity:.85}
/* 서문 */
.pre{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:clamp(24px,5vw,80px);padding:64px 0 90px}
.pre h2{font-size:clamp(26px,2.6vw,38px);line-height:1.35}
.pre p{font:400 18px/1.95 var(--serif);color:var(--ink2);margin:0 0 1em;max-width:36em}
.pre p:first-child::first-letter{float:left;font:400 64px/0.9 var(--serif);margin:6px 10px 0 0;color:var(--seal)}
/* 전시 도판 13 */
.plates-h{display:flex;align-items:end;justify-content:space-between;gap:20px;border-bottom:1px solid var(--ink);padding-bottom:14px}
.plates-h h2{font-size:clamp(28px,3vw,44px)}.plates-h p{margin:0;color:var(--ink2);max-width:30em;font-size:15px}
.cat{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));gap:56px 28px;padding:48px 0 100px}
.cat a{text-decoration:none;display:flex;flex-direction:column;gap:12px}
.cat .ph{background:linear-gradient(#efe7d8,#e6dcc8);aspect-ratio:4/5;display:grid;place-items:center;padding:12%;position:relative;overflow:hidden}
.cat .ph img{max-height:100%;width:auto;transition:transform .6s cubic-bezier(.2,.7,.2,1);filter:drop-shadow(0 18px 18px rgba(40,30,15,.22))}
.cat a:hover .ph img{transform:scale(1.04)}
.cat .lab{display:grid;grid-template-columns:auto 1fr;gap:2px 12px;font-size:13.5px;color:var(--ink2)}
.cat .lab i{font:italic 400 22px/1 var(--serif);color:var(--gold);grid-row:span 2}
.cat .lab b{font:500 15.5px/1.45 var(--serif);color:var(--ink)}
.cat a:nth-child(1){grid-column:1/6}.cat a:nth-child(2){grid-column:7/10;margin-top:120px}.cat a:nth-child(3){grid-column:10/13}
.cat a:nth-child(4){grid-column:2/5}.cat a:nth-child(5){grid-column:6/9;margin-top:60px}.cat a:nth-child(6){grid-column:9/13}
.cat a:nth-child(n+7){grid-column:span 3}
/* 감정 절차: 타임라인 */
.flow{background:var(--paper2);padding:90px 0}
.flow h2{font-size:clamp(26px,2.6vw,38px);margin-bottom:8px}.flow .sub{color:var(--ink2);margin:0 0 44px}
.tl{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));position:relative}
.tl::before{content:"";position:absolute;left:0;right:0;top:27px;height:2px;background:var(--ink);opacity:.8}
.tl li{position:relative;padding:0 24px 0 0}
.tl .k{display:grid;place-items:center;width:56px;height:56px;border-radius:50%;background:var(--paper);border:2px solid var(--ink);font:500 20px var(--serif);position:relative}
.tl li:last-child .k{background:var(--seal);border-color:var(--seal);color:#fff}
.tl h3{font-size:21px;margin:18px 0 6px}.tl p{margin:0;color:var(--ink2);font-size:15px}
.tl small{display:block;margin-top:8px;color:var(--gold);font-size:13px}
footer.f{border-top:1px solid var(--ink);padding:40px 0 60px;font-size:14px;color:var(--ink2)}
footer.f .wrap{display:flex;flex-wrap:wrap;gap:16px 48px;justify-content:space-between}
footer.f b{font:500 16px var(--serif);color:var(--ink)}
/* 전시실 */
.room-h{padding:56px 0 30px;display:grid;grid-template-columns:minmax(0,1fr) auto;align-items:end;gap:24px;border-bottom:1px solid var(--ink)}
.room-h h1{font-size:clamp(38px,5vw,72px);font-weight:300}
.room-h p{margin:0;color:var(--ink2);max-width:32em}
.room{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:40px 28px;padding:44px 0 60px}
.room a{text-decoration:none}.room a[aria-current=true] .ph{outline:2px solid var(--seal);outline-offset:4px}
.room .ph{background:linear-gradient(#efe7d8,#e5dac6);aspect-ratio:4/5;display:grid;place-items:center;padding:13%}
.room .ph img{max-height:100%;width:auto;filter:drop-shadow(0 14px 14px rgba(40,30,15,.2))}
.room .lab{margin-top:12px;font-size:13.5px;color:var(--ink2)}.room .lab b{display:block;font:500 15px/1.45 var(--serif);color:var(--ink)}
#detail{border-top:1px solid var(--ink);padding:56px 0 90px}
.d-g{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:clamp(24px,5vw,72px)}
.d-main{background:radial-gradient(70% 60% at 50% 45%,#fffaf0,#e9dfcc);aspect-ratio:1/1;display:grid;place-items:center;padding:8%;cursor:zoom-in;border:0;width:100%}
.d-main img{max-height:100%;width:auto;view-transition-name:hero-obj;filter:drop-shadow(0 24px 22px rgba(40,30,15,.25))}
.d-th{display:grid;grid-template-columns:repeat(auto-fill,minmax(84px,1fr));gap:8px;margin-top:12px}
.d-th button{border:0;padding:0;background:#222;aspect-ratio:3/4;cursor:zoom-in}.d-th img{width:100%;height:100%;object-fit:cover}
.d-l .pn{font:italic 400 44px/1 var(--serif);color:var(--gold)}
.d-l h2{font-size:clamp(26px,2.4vw,36px);line-height:1.35;margin:10px 0 22px}
.d-l dl{display:grid;grid-template-columns:7em 1fr;gap:10px 16px;margin:0 0 26px;border-top:1px solid var(--line);padding-top:16px}.d-l dt{color:var(--ink2)}.d-l dd{margin:0}
.d-l .note{font-size:13.5px;color:var(--ink2);border-left:3px solid var(--seal);padding-left:12px}
@media(max-width:1100px){nav.m{display:none}}
@media(max-width:860px){.hero{grid-template-columns:56px minmax(0,1fr);min-height:0}.vcol{padding-right:14px}.vcol .v{font-size:52px}.seal{width:44px}.plate{grid-column:2;min-height:420px}.txt{grid-column:1/-1;margin-top:28px}
 .pre,.d-g{grid-template-columns:1fr}.cat{grid-template-columns:repeat(2,minmax(0,1fr));gap:36px 16px}.cat a:nth-child(n){grid-column:auto;margin-top:0}
 .tl{grid-template-columns:1fr;gap:28px}.tl::before{left:27px;right:auto;top:0;bottom:0;width:2px;height:auto}.tl li{padding:0 0 0 76px}.tl .k{position:absolute;left:0;top:0}.tl h3{margin-top:10px}
 .room-h{grid-template-columns:1fr}.room{grid-template-columns:repeat(2,minmax(0,1fr));gap:28px 14px}}
@media(max-width:520px){.top .wrap{gap:10px;height:62px}.brand{min-width:0}.brand img{height:34px}.brand b{font-size:13px;white-space:nowrap}.brand small{display:none}.lg{margin-left:auto}.lg button{padding:4px 5px;font-size:11px;white-space:nowrap}.plate img{max-height:52vh}}
@media(max-width:860px){.plates-h{flex-direction:column;align-items:flex-start}}
@media(max-width:380px){.brand b{display:none}}
'''

def header(cur=None, logo='img/g/logo.webp'):
    nav = ''.join(f'<a href="{"room.html" if n=="소장품" else "#"}"{" aria-current=\"page\"" if n==cur else ""}>{n}</a>' for n in NAV)
    return (f'<a class="skip" href="#main">본문 바로가기</a><header class="top"><div class="wrap"><a class="brand" href="home.html"><img src="{logo}" alt="천도예술품국제교류센터 로고" width="84" height="42"><span><b>천도예술품국제교류센터</b><small>天道藝術品國際交流中心</small></span></a>'
            f'<nav class="m" aria-label="주 메뉴">{nav}</nav><div class="lg" role="group" aria-label="언어"><button aria-pressed="true">한국어</button><button aria-pressed="false">EN</button><button aria-pressed="false">中文</button><button aria-pressed="false">日本語</button></div></div></header>')

FOOT = '''<footer class="f"><div class="wrap"><div><b>(주)천도예술품국제교류센터</b><br>서울특별시 서대문구 남가좌동 382-6, DMC 빌딩 1~2층</div><div>대표전화 02-303-7877<br>회장 장유성 010-8606-1141<br>jus1141@naver.com</div></div></footer>'''

def doc(title, css, body):
    return f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>{FONTS}<style>{css}</style></head><body>{body}{items_js()}{JS}</body></html>'

def a_home():
    x = HERO
    cat = ''.join(f'<a href="room.html#{i["id"]}"><div class="ph"><img loading="lazy" src="{cut(i)}" alt="{E(i["t"])}" data-par></div><div class="lab"><i>{i["n"]:02d}</i><b>{E(i["t"])}</b><span>{E(i["era"])}</span></div></a>' for i in IT[:9])
    body = header() + f'''<main id="main">
<section class="wrap hero" aria-label="대표 소장품">
 <div class="vcol" aria-hidden="true"><span class="v">天道</span><span class="vs">藝術品國際交流中心</span><span class="seal">{SEAL}</span></div>
 <figure class="plate" style="margin:0"><span class="shadow"></span><img src="{cut(x)}" alt="{E(x["t"])}" data-par width="900" height="960"></figure>
 <div class="txt"><span class="cloud" aria-hidden="true">{CLOUD}</span><h1><span>옛 그릇이 걸어온 길을</span><span>오늘의 기록으로 잇습니다</span></h1>
 <p>천도예술품국제교류센터는 중국 고미술품을 과학 검사와 감정위원의 눈으로 감정하고, 그 기록을 바탕으로 박물관과 수장가에게 연결합니다.</p>
 <div class="btns"><a class="btn" href="#">감정 신청</a><a class="btn o" href="room.html">전시실 둘러보기</a></div>
 <p class="cap" style="margin-top:44px"><b>도판 {x["n"]:02d}. {E(x["t"])}</b>{E(x["era"])}<br>{E(x["size"])}<br>위탁 소장품 {x["no"]}</p></div>
</section>
<div class="wrap"><span class="inkline" aria-hidden="true" style="display:block">{INKLINE}</span></div>
<section class="wrap pre" data-ink><h2>감정은 물건의 내력을<br>다시 읽는 일입니다</h2><div><p>센터는 2026년 서울 서대문구에 문을 열었습니다. 중국 감정 전문가 팀이 도자기, 서화, 옥기, 청동기를 맡아 실물을 보고, 광학현미경과 XRF 성분 분석, 연대 측정으로 근거를 남깁니다.</p><p>남긴 기록은 인증번호와 QR로 누구나 조회할 수 있습니다. 감정을 마친 소장품은 중국 국·공립 박물관과 국제 수장가에게 소개합니다.</p></div></section>
<section class="wrap" aria-labelledby="ph"><div class="plates-h"><h2 id="ph">전시 도판</h2><p>센터에 위탁된 소장품 13점입니다. 도판을 누르면 전시실에서 상세 사진과 감정 자료를 볼 수 있습니다.</p></div><div class="cat">{cat}</div></section>
<section class="flow" aria-labelledby="fl"><div class="wrap"><h2 id="fl">감정은 이렇게 진행됩니다</h2><p class="sub">신청부터 감정서 발급까지 네 단계입니다.</p>
<ol class="tl"><li data-ink><span class="k">1</span><h3>온라인 신청</h3><p>작품 사진과 소장 경위를 보냅니다.</p></li><li data-ink><span class="k">2</span><h3>사전 검토</h3><p>감정 가능 여부를 알려 드립니다.</p><small>3영업일 안</small></li><li data-ink><span class="k">3</span><h3>실물 감정</h3><p>서울 센터 방문 또는 출장 감정.</p></li><li data-ink><span class="k">4</span><h3>감정서 발급</h3><p>인증번호와 QR로 진위를 조회합니다.</p></li></ol></div></section>
</main>''' + FOOT
    return doc('천도예술품국제교류센터 · 시안 A 도록', A_CSS, body)

def room(css, variant):
    cards = ''.join(f'<a href="#{i["id"]}" data-open="{i["id"]}" aria-current="false"><div class="ph"><img loading="lazy" src="{cut(i)}" alt="{E(i["t"])}"></div><div class="lab"><b>{E(i["t"])}</b>{E(i["era"])}</div></a>' for i in IT)
    x = HERO
    th = ''.join(f'<button type="button" aria-label="사진 {k+1} 크게 보기" data-z="{orig(p)}"><img loading="lazy" src="{orig(p)}" alt=""></button>' for k, p in enumerate(x['ph']))
    body = header('소장품') + f'''<main id="main"><div class="wrap">
<div class="room-h"><h1>전시실</h1><p>위탁 소장품 13점. 유물을 고르면 아래에 상세 사진과 감정 자료가 열립니다. 사진을 누르면 확대해 볼 수 있습니다.</p></div>
<div class="room">{cards}</div>
<section id="detail" aria-live="polite"><div class="d-g"><div><button type="button" class="d-main" aria-label="대표 사진 확대"><img src="{cut(x)}" alt="{E(x["t"])}"></button><div class="d-th">{th}</div></div>
<div class="d-l"><span class="pn" data-f="n">{x["n"]:02d}</span><h2 data-f="t">{E(x["t"])}</h2><dl><dt>시대</dt><dd data-f="era">{E(x["era"])}</dd><dt>크기</dt><dd data-f="size">{E(x["size"])}</dd><dt>아카이브</dt><dd data-f="no">{x["no"]}</dd><dt>감정 자료</dt><dd><span data-f="docs">{x["docs"]}</span>건 (감정서 원본·검사 기록)</dd></dl>
<p class="note">대표 사진은 배경만 정리했고, 아래 상세 사진은 촬영 원본입니다. 감정 자료는 진위와 가치를 보장하지 않는 참고 자료입니다.</p>
<div class="btns" style="margin-top:22px"><a class="btn" href="#">이 유물 위탁 상담</a><a class="btn o" href="#">인증 조회</a></div></div></div></section>
</div></main>''' + FOOT + '<script>addEventListener("load",()=>{const h=location.hash.slice(1);if(h&&ITEMS.find(i=>i.id===h))showItem(h)})</script>'
    return doc('천도예술품국제교류센터 · 전시실 · 시안 ' + variant, css, body)

# ======================= B안: 백자 전시실(展示室) =======================
B_CSS = A_CSS.replace(':root{--paper:#f4eee2;--paper2:#ebe2d1;--ink:#1d1a16;--ink2:#4b443a;--gold:#7a5b22;--goldl:#b8924a;--seal:#a3301f;--line:#d6c8ae;--focus:#a3301f;',
                      ':root{--paper:#f7f6f2;--paper2:#1f2c4a;--ink:#1a1d24;--ink2:#4a4f5a;--gold:#7d6024;--goldl:#b39350;--seal:#b0362a;--line:#dcdad3;--focus:#1f2c4a;--navy:#1f2c4a;') + '''
body{background:var(--paper)}
.hero{grid-template-columns:minmax(0,1fr);min-height:0;padding:clamp(28px,4vw,56px) 0 0;text-align:left}
.hb{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:clamp(20px,4vw,60px);align-items:end}
.hb h1{font-size:clamp(44px,6.4vw,104px);line-height:1.04;font-weight:600;letter-spacing:-.045em}
.hb p{font-size:17px;color:var(--ink2);margin:0 0 26px;max-width:28em}
.vit{margin-top:clamp(28px,4vw,56px);background:linear-gradient(180deg,#eef0f3 0,#e3e6ea 70%,#d7dbe0 100%);position:relative;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,auto) minmax(0,1fr);align-items:end;padding:56px clamp(16px,4vw,56px) 0;border-top:3px solid var(--navy)}
.vit .obj{grid-column:2;display:grid;justify-items:center}
.vit .obj img{max-height:min(66vh,640px);width:auto;view-transition-name:hero-obj;filter:drop-shadow(0 30px 26px rgba(20,28,45,.28))}
.vit .plinth{width:min(70vw,520px);height:64px;background:linear-gradient(#fbfbfa,#e9e8e3);box-shadow:0 18px 30px rgba(20,28,45,.12);margin-top:-6px}
.vit .side{grid-column:3;align-self:center;font-size:13.5px;color:var(--ink2);padding-left:28px;border-left:1px solid #b9bec7;max-width:260px}
.vit .side b{display:block;font:500 16px/1.45 var(--serif);color:var(--ink);margin-bottom:6px}
.vit .han{grid-column:1;align-self:center;writing-mode:vertical-rl;font:300 clamp(48px,6vw,92px)/1 var(--han);letter-spacing:.2em;color:#9aa3b2;justify-self:start}
.vit .seal{position:absolute;right:clamp(16px,4vw,56px);top:24px;width:54px}
.walk{padding:90px 0}
.walk .plates-h{border-color:var(--navy)}
.strip{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(240px,22%);gap:24px;overflow-x:auto;scroll-snap-type:x mandatory;padding:36px 0 20px;scrollbar-color:var(--navy) transparent}
.strip a{scroll-snap-align:start;text-decoration:none}
.strip .ph{background:linear-gradient(180deg,#eef0f3,#dfe3e8);aspect-ratio:3/4;display:grid;place-items:center;padding:14%;border-bottom:3px solid var(--navy)}
.strip .ph img{max-height:100%;width:auto;filter:drop-shadow(0 16px 14px rgba(20,28,45,.22));transition:transform .6s}
.strip a:hover img{transform:translateY(-6px)}
.strip .lab{margin-top:12px;font-size:13.5px;color:var(--ink2)}.strip .lab b{display:block;font:500 15px/1.45 var(--serif);color:var(--ink)}
.flow{color:#eef0f4}.flow h2,.flow h3{color:#fff}.flow .sub,.flow .tl p{color:#c9d0dc}.flow .tl::before{background:#c9a65e}.flow .tl .k{background:var(--navy);border-color:#c9a65e;color:#fff}.flow .tl small{color:#d9bd7e}
.room .ph,.d-main{background:linear-gradient(180deg,#eef0f3,#dfe3e8)}
.room .ph{border-bottom:3px solid var(--navy)}
.btn:hover{background:var(--navy);border-color:var(--navy)}
@media(max-width:860px){.hb{grid-template-columns:1fr}.vit{grid-template-columns:1fr;padding-top:40px}.vit .obj{grid-column:1}.vit .han{display:none}.vit .side{grid-column:1;border-left:0;border-top:1px solid #b9bec7;padding:16px 0 24px;max-width:none}.strip{grid-auto-columns:72%}}
'''

def b_home():
    x = HERO
    strip = ''.join(f'<a href="room.html#{i["id"]}"><div class="ph"><img loading="lazy" src="{cut(i)}" alt="{E(i["t"])}"></div><div class="lab"><b>{E(i["t"])}</b>{E(i["era"])}</div></a>' for i in IT)
    body = header() + f'''<main id="main">
<section class="wrap hero" aria-label="대표 소장품"><div class="hb"><h1>천도,<br>옛 그릇의 길을 잇다</h1><div><p>중국 고미술품을 과학 검사와 감정위원의 눈으로 감정하고, 그 기록을 바탕으로 박물관과 수장가에게 연결합니다.</p><div class="btns"><a class="btn" href="#">감정 신청</a><a class="btn o" href="room.html">전시실 둘러보기</a></div></div></div>
<div class="vit"><span class="han" aria-hidden="true">天道</span><figure class="obj" style="margin:0"><img src="{cut(x)}" alt="{E(x["t"])}" data-par width="900" height="960"><span class="plinth" aria-hidden="true"></span></figure>
<p class="side"><b>{E(x["t"])}</b>{E(x["era"])}<br>{E(x["size"])}<br>위탁 소장품 {x["no"]}</p><span class="seal" style="color:var(--seal)">{SEAL}</span></div></section>
<section class="wrap walk" aria-labelledby="wk"><div class="plates-h"><h2 id="wk">전시실 한 바퀴</h2><p>위탁 소장품 13점을 옆으로 넘기며 보세요. 고르면 상세 사진과 감정 자료로 이어집니다.</p></div><div class="strip" tabindex="0" aria-label="위탁 소장품 목록">{strip}</div></section>
<section class="flow" aria-labelledby="fl"><div class="wrap"><h2 id="fl">감정은 이렇게 진행됩니다</h2><p class="sub">신청부터 감정서 발급까지 네 단계입니다.</p>
<ol class="tl"><li data-ink><span class="k">1</span><h3>온라인 신청</h3><p>작품 사진과 소장 경위를 보냅니다.</p></li><li data-ink><span class="k">2</span><h3>사전 검토</h3><p>감정 가능 여부를 알려 드립니다.</p><small>3영업일 안</small></li><li data-ink><span class="k">3</span><h3>실물 감정</h3><p>서울 센터 방문 또는 출장 감정.</p></li><li data-ink><span class="k">4</span><h3>감정서 발급</h3><p>인증번호와 QR로 진위를 조회합니다.</p></li></ol></div></section>
</main>''' + FOOT
    return doc('천도예술품국제교류센터 · 시안 B 전시실', B_CSS, body)

import os
for d in ('a', 'b'): os.makedirs(f'mock/{d}', exist_ok=True)
open('mock/a/home.html', 'w').write(a_home()); open('mock/a/room.html', 'w').write(room(A_CSS, 'A'))
open('mock/b/home.html', 'w').write(b_home()); open('mock/b/room.html', 'w').write(room(B_CSS, 'B'))
for d in ('a', 'b'):
    if not os.path.exists(f'mock/{d}/img'): os.symlink('../img', f'mock/{d}/img')
print('ok')
