// Password gate for the preview deploy. Netlify's own site password is a paid
// feature; this is the free-tier equivalent. Credentials come from the Netlify
// UI (PREVIEW_USER / PREVIEW_PASSWORD) and are never committed.
//
// It fails closed: no env vars set means nobody gets in, rather than the site
// opening to the world. Remove this function and its netlify.toml block when the
// site is cleared to launch.

const DENY = (msg: string) =>
  new Response(msg, {
    status: 401,
    headers: {
      "WWW-Authenticate": 'Basic realm="Apex preview", charset="UTF-8"',
      "Cache-Control": "no-store",
      "X-Robots-Tag": "noindex, nofollow, noarchive",
    },
  });

export default async (request: Request) => {
  const user = Netlify.env.get("PREVIEW_USER");
  const password = Netlify.env.get("PREVIEW_PASSWORD");
  if (!user || !password) return DENY("Preview credentials are not configured.");

  const header = request.headers.get("authorization") || "";
  const [scheme, encoded] = header.split(" ");
  if (scheme !== "Basic" || !encoded) return DENY("Authentication required.");

  let decoded = "";
  try {
    decoded = atob(encoded);
  } catch {
    return DENY("Authentication required.");
  }
  const sep = decoded.indexOf(":");
  if (decoded.slice(0, sep) !== user || decoded.slice(sep + 1) !== password) {
    return DENY("Authentication required.");
  }
  return; // hand back to the static file
};

export const config = { path: "/*" };
