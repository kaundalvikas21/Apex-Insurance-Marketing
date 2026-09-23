// Derivatives for the three client-supplied coverage hero banners.
//
// The rest of the photography comes from the Unsplash CDN, which resizes for us
// (tools/images.py). These three are local files, so they need a real encoder.
// sharp is NOT a dependency of this repo; run this once per new source image:
//
//   mkdir -p /tmp/sharp && cd /tmp/sharp && npm init -y && npm i sharp
//   NODE_PATH=/tmp/sharp/node_modules node tools/hero_images.cjs [name ...]
//
// Pass job names to rebuild only those; with none, every job runs.
// Sources: public/**/*.png, normally 2752x1536. A smaller source is fine: the
// phone crop below is written in 2752-wide coordinates and scaled to the file. Output: assets/img/, committed.
//   <name>-{1280,1920}.{avif,webp}   the whole 16:9 frame, the desktop background
//   <name>-m-{480,800}.{avif,webp}   a 4:3 crop of the people, for below 1024px
const sharp = require("sharp");
const path = require("path");

const ROOT = path.join(__dirname, "..");
// name -> [source under public/, top edge of the 4:3 phone crop, desktop aspect].
// The subjects sit in the right 55% of every frame; how low they sit varies per
// photograph. A desktop aspect wider than the source's 16:9 extends the frame
// leftward by repeating its edge pixels (the empty wall), so the ~2.6:1 hero box
// shows the whole photograph instead of cover-cropping a third of its height.
const JOBS = {
  "term-hero": ["coverage_hero/Term_Life_hero.png", 320],
  // Replaced 2026-09-23 (1360x768). The heads sit high, so the crop starts high.
  "whole-hero": ["coverage_hero/Whole_Life_hero.png", 80, 2.6],
  "fe-hero": ["coverage_hero/Final_Expense_hero.png", 320],
  "home-banner": ["Apex_homepage_hero.png", 400],
  "contact-banner": ["Apex_contact_page_hero.png", 250],
  "review-banner": ["Apex_Free_Policy_Review_hero_American_cast.png", 330],
};

(async () => {
  const only = process.argv.slice(2);
  for (const [name, [file, top, aspect]] of Object.entries(JOBS)) {
    if (only.length && !only.includes(name)) continue;
    const src = path.join(ROOT, "public", file);
    const k = (await sharp(src).metadata()).width / 2752;
    const r = (n) => Math.round(n * k);
    const CROP = { left: r(1238), top: r(top), width: r(1514), height: r(1136) };
    const out = (suffix) => path.join(ROOT, "assets/img", name + suffix);
    const meta = await sharp(src).metadata();
    const pad = aspect ? Math.max(0, Math.round(meta.height * aspect) - meta.width) : 0;
    let wide = await sharp(src).extend({ left: pad, extendWith: "copy" }).png().toBuffer();
    if (pad) {
      // Repeated edge pixels streak; a heavy blur over the added strip (plus a
      // little of the original edge, to hide the seam) reads as out-of-focus wall.
      const strip = { left: 0, top: 0, width: pad + 40, height: meta.height };
      const soft = await sharp(wide).extract(strip).blur(40).toBuffer();
      wide = await sharp(wide).composite([{ input: soft, left: 0, top: 0 }]).png().toBuffer();
    }
    for (const w of [1280, 1920]) {
      await sharp(wide).resize(w).avif({ quality: 50 }).toFile(out(`-${w}.avif`));
      await sharp(wide).resize(w).webp({ quality: 76 }).toFile(out(`-${w}.webp`));
    }
    for (const w of [480, 800]) {
      await sharp(src).extract(CROP).resize(w).avif({ quality: 50 }).toFile(out(`-m-${w}.avif`));
      await sharp(src).extract(CROP).resize(w).webp({ quality: 76 }).toFile(out(`-m-${w}.webp`));
    }
    console.log("ok", name);
  }
})();
