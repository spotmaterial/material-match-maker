const { chromium } = require('playwright'); const fs = require('fs');
// usage: node run2.js '<json: [{slug, params}]>'
(async () => {
  const jobs = JSON.parse(process.argv[2]);
  const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  const p = await b.newPage({ viewport: { width: 960, height: 960 } });
  p.on('pageerror', e => console.log('ERR', e.message));
  await p.goto('http://127.0.0.1:8765/render2.html'); await p.waitForFunction(() => window.ready, null, { timeout: 60000 });
  fs.mkdirSync('out2', { recursive: true });
  for (const j of jobs) { const url = await p.evaluate(([s, pr]) => window.renderSphere(s, pr), [j.slug, j.params || {}]);
    fs.writeFileSync(`out2/${j.slug}.png`, Buffer.from(url.split(',')[1], 'base64')); console.log('rendered', j.slug); }
  await b.close();
})();
