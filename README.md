# Thai Local – "Get your free website draft" landing page

Static, bilingual (Thai first, English beneath) landing page for Thai Local, a website service for local businesses in Northeast Thailand (Isan).

- Live: https://thailocal.online/ (www and the old https://axess34.github.io/thailocal/ redirect here)
- All asset paths are relative; only og:url, og:image and canonical are absolute.

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

## Domain
- DNS on Cloudflare (DNS only / grey cloud): apex A 185.199.108-111.153, AAAA 2606:50c0:8000-8003::153, CNAME www -> axess34.github.io.
- `CNAME` file in this repo = thailocal.online.
- Client sites: CNAME <name>.thailocal.online -> axess34.github.io (DNS only) + a CNAME file with <name>.thailocal.online in that client's repo.
