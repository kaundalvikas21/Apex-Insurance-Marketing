// Derivatives for the three client-supplied coverage hero banners.
//
// The rest of the photography comes from the Unsplash CDN, which resizes for us
// (tools/images.py). These three are local files, so they need a real encoder.
// sharp is NOT a dependency of this repo; run this once per new source image:
//
//   mkdir -p /tmp/sharp && cd /tmp/sharp && npm init -y && npm i sharp
//   NODE_PATH=/tmp/sharp/node_modules node tools/hero_images.cjs
//
// Sources: public/**/*.png (2752x1536). Output: assets/img/, committed.
//   <name>-{1280,1920}.{avif,webp}   the whole 16:9 frame, the desktop background
//   <name>-m-{480,800}.{avif,webp}   a 4:3 crop of the people, for below 1024px
const sharp = require("sharp");
const path = require("path");

const ROOT = path.join(__dirname, "..");
// name -> [source under public/, top edge of the 4:3 phone crop]. The subjects
// sit in the right 55% of every frame; how low they sit varies per photograph.
const JOBS = {
  "term-hero": ["coverage_hero/Term_Life_hero.png", 320],
  "whole-hero": ["coverage_hero/Whole_Life_hero.png", 320],
  "fe-hero": ["coverage_hero/Final_Expense_hero.png", 320],
  "home-banner": ["Apex_homepage_hero.png", 400],
  "contact-banner": ["Apex_contact_page_hero.png", 250],
  "review-banner": ["Apex_Free_Policy_Review_hero_American_cast.png", 330],
};

(async () => {
  for (const [name, [file, top]] of Object.entries(JOBS)) {
    const src = path.join(ROOT, "public", file);
    const CROP = { left: 1238, top, width: 1514, height: 1136 };
    const out = (suffix) => path.join(ROOT, "assets/img", name + suffix);
    for (const w of [1280, 1920]) {
      await sharp(src).resize(w).avif({ quality: 50 }).toFile(out(`-${w}.avif`));
      await sharp(src).resize(w).webp({ quality: 76 }).toFile(out(`-${w}.webp`));
    }
    for (const w of [480, 800]) {
      await sharp(src).extract(CROP).resize(w).avif({ quality: 50 }).toFile(out(`-m-${w}.avif`));
      await sharp(src).extract(CROP).resize(w).webp({ quality: 76 }).toFile(out(`-m-${w}.webp`));
    }
    console.log("ok", name);
  }
})();
