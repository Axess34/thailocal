# Thai Local – "Get your free website draft" landing page

Static, bilingual (Thai first, English beneath) landing page for Thai Local, a website service for local businesses in Northeast Thailand (Isan).

- Live (for now): https://axess34.github.io/thailocal/
- Planned domain: thailocal.online (all paths are relative, so the site works on either)

## Files
- `index.html`, `style.css`, `app.js`: the page and form logic
- `img/`: OG image (1200x630), hero visual, favicons, draft thumbnails (built by `make_assets.py`)
- `favicon.svg`, `site.webmanifest`

## Form submissions
`app.js` POSTs to Supabase (project "Thai Voice Helper", ref `ivleheagpnenoaevpcjv`), table `public.thailocal_draft_requests`.
The public (publishable) key can only INSERT into that table (RLS + column grants); it cannot read, update or delete.

Read new requests (Supabase SQL editor or MCP execute_sql):

```sql
select created_at at time zone 'Asia/Bangkok' as received_th, shop_name, fb_url, contact, email, city, status
from public.thailocal_draft_requests
where status = 'new'
order by created_at desc;
```

Mark one done: `update public.thailocal_draft_requests set status = 'done' where id = '...';`

If the request fails (network, Supabase paused), the form shows a WhatsApp link pre-filled with the visitor's details.

## Moving to thailocal.online
1. Buy the domain, add `CNAME` file containing `thailocal.online` (or set it in repo Settings → Pages), point DNS to GitHub Pages.
2. Optionally update the absolute `og:image` URL in `index.html` to `https://thailocal.online/img/og-image.jpg` (the old URL keeps working via GitHub's redirect).
