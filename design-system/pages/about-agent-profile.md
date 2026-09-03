# Page override: Agent profile template (`/about/agents/first-last/`)
Inherits `design-system/MASTER.md`. Only deviations are listed.

- **Purpose:** the reference target for every article byline. `chrome.person_schema()` points its Person `@id` here, so the node the hubs emit resolves to a page that describes a person. This is why the page leads with verifiable licence numbers rather than a biography.
- **One module per agent.** Copy `tools/pages/about_agent_profile.py`, change the `AGENT` dict, add the module to `build.py`'s `PAGES`. The slug in `PATH` must match the slug in `about_agents.AGENTS` or the index links to a 404.
- **Split hero:** name and focus in seven columns, a `.panel` in four holding the photo slot, a three-row `<dl>`, and both CTAs. `.avatar-slot-lg` (132px) is the profile-scale variant of the byline's 84px slot; it keeps the dashed border so it can never read as a filled portrait.
- **Licences are the signature table.** `.table-scroll.table-signature` with `.rate-table`, four columns, tabular numbers on the licence number column. Dated `.pill` beneath, and the copy states that the state lookup is authoritative over this page rather than the reverse.
- **`ACTIVE` is `/about/agents/`,** so the index stays the nav ancestor even though this page is a level deeper.
- **No byline.** The page is about the agent; a byline crediting the agent to themselves is circular.
- Layout families in order: split hero + panel, table, split + bento pair, navy band. Eyebrow budget 2, used 2.
