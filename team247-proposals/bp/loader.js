(()=>{'use strict';const url=new URL(location.href),zh=url.searchParams.get('lang')==='zh';document.documentElement.lang=zh?'zh-CN':'en';
const labels=zh?['总目录','业务概览','财务口径','参考来源']:['Index','Overview','Financials','Sources'];
document.querySelectorAll('[data-main]').forEach((a,i)=>a.textContent=labels[i]);
document.querySelector('.wordmark').setAttribute('aria-label',zh?'Team247 商业计划书总目录':'Team247 business-plan index');
document.querySelector('.masthead nav').setAttribute('aria-label',zh?'主导航':'Main navigation');document.querySelector('.skip').textContent=zh?'跳到正文':'Skip to content';
document.querySelectorAll('[data-lang]').forEach(a=>{const target=new URL(location.href);target.searchParams.set('lang',a.dataset.lang);a.href=target.href;if((a.dataset.lang==='zh')===zh)a.setAttribute('aria-current','true');});
function languageLinks(){document.querySelectorAll('[data-lang]').forEach(a=>{const target=new URL(location.href);target.searchParams.set('lang',a.dataset.lang);a.href=target.href;});}addEventListener('hashchange',languageLinks);
function load(src){return new Promise((ok,fail)=>{const s=document.createElement('script');s.src=src;s.onload=ok;s.onerror=fail;document.head.append(s);});}
load(zh?'bp/content.js?v=8':'bp/content-en.js?v=8').then(()=>load(zh?'bp/app.js?v=8':'bp/app-en.js?v=8')).catch(()=>{document.getElementById('app').innerHTML=zh?'<main class="cover"><h1>资料暂未载入</h1><p>请刷新重试，或<a href="bp/business-plans.md">下载完整正文</a>。</p></main>':'<main class="cover"><h1>Content could not be loaded</h1><p>Please refresh or <a href="bp/business-plans-en.md">download the complete plans</a>.</p></main>';});})();
