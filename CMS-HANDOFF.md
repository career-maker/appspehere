# CMS handoff: what the backend must output

Titles (no span/class needed)
- Wrap accent words in asterisks in the plain-text title: `Ready to Join *India's Retail* Revolution?`. `js/main.js` turns them into the accent colour on every page load.

Lists (retailer / manufacturer / role panels)
- Output plain `<ul><li>text</li></ul>`. CSS adds the tick icon; no svg or classes needed.

Banner mobile image (every inner-page banner)
- Output `<picture><source media="(max-width: 760px)" srcset="MOBILE-IMAGE-URL"><img class="page-hero__art" src="DESKTOP-IMAGE-URL" alt="..."></picture>`.
- The same pattern is used for the home hero scene (`media="(max-width: 767px)"`). Each banner needs its own "mobile image" upload field in the CMS; the front end is ready for it.

Home slider (hero) fields
- Per slide: Title, Subtitle, Description, Desktop image, Mobile image. One slide is supported (no scroll story, no extra spacing).

Distributors page
- `distributorData` in `js/distributors.js` holds the real data. The `SAMPLE` Ernakulam entries are demo only; remove before go-live.
