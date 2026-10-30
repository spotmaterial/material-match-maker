const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  const p = await b.newPage({ viewport: { width: 700, height: 700 } });
  p.on('pageerror', e => console.log('ERR', e.message)); p.on('console', m => { if (m.type() !== 'log') console.log(m.type(), m.text()); });
  await p.goto('http://127.0.0.1:8765/render.html'); await p.waitForFunction(() => window.ready, null, { timeout: 60000 });
  const only = process.argv.slice(2); const looks = only.length ? only : await p.evaluate(() => window.looks);
  for (const l of looks) { const t = Date.now(); const url = await p.evaluate(s => window.renderLook(s), l); fs.writeFileSync(`out/${l}.png`, Buffer.from(url.split(',')[1], 'base64')); console.log(l, Date.now() - t, 'ms'); }
  await b.close();
})();
