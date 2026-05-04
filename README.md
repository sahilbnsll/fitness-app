# FitPal — Offline Fitness Tracker

> **Live →** [myfitpal.netlify.app](https://myfitpal.netlify.app/)

A professional-grade, zero-dependency PWA fitness dashboard built for serious athletes. One HTML file. No accounts. No cloud. Instant load.

---

## Features

| Category | Highlights |
|---|---|
| 🏋️ **Workout Logging** | 6-day PPL × 2 split · per-set weight/reps/RPE · drop sets · progressive overload suggestions · Quick Start mode |
| 📊 **Analytics** | 45-day workout heatmap · supplement adherence heatmap · body-weight trend chart · exercise PR history |
| 🥩 **Nutrition** | Shuffleable weekly meal plans · macro tracking (kcal, protein) · diet phase tagging |
| 💊 **Supplements** | Custom stack · daily check-in · per-supplement heatmap |
| 🧘 **Mobility** | Custom mobility/stretching routines with notes |
| 🏃 **Cardio** | Protocol guide with zone targets |
| 🔄 **Deload** | Structured deload protocol with auto-scheduling cues |
| ⚖️ **Weight Log** | Weekly fasted weigh-in modal with historical chart |
| 📤 **Backup** | Full data export/import via JSON |

---

## Tech Stack

- **Frontend**: HTML5 · Vanilla JavaScript (ES2022) · CSS3 (Custom Properties, Grid, Flexbox)
- **Persistence**: `localStorage` — 100% private, local-only, no accounts
- **PWA**: Service Worker (network-first for navigation, cache-first for assets) · `manifest.webmanifest` · installable on iOS & Android
- **Deployment**: Netlify (auto-deploy from `main`) with strict security headers

---

## Architecture

```
fitness-app/
├── fitness_hub.html      # Entire app — single self-contained file
├── manifest.webmanifest  # PWA manifest with inline SVG icons (192 + 512 + maskable)
├── sw.js                 # Service worker — offline-first caching
├── netlify.toml          # Deploy config + security headers (HSTS, CSP, X-Frame)
└── docs/
    └── CHANGELOG.md
```

---

## Accessibility & Quality

- ✅ **Full Keyboard Navigation**: All complex components (Day Headers, Exercise Rows) use `role="button"` + `tabindex="0"` + `onEnter` helper for seamless keyboard activation.
- ✅ **Focus Management**: Modals now strictly manage focus, trapped using the `inert` attribute and `aria-hidden` toggles.
- ✅ **Navigation Accessibility**: The bottom navigation bar now dynamically updates `aria-current="page"` to accurately inform assistive technology of the user's location.
- ✅ **Live Feedback**: The toast notification system utilizes `role="status"` and `aria-live="polite"` for non-disruptive, accessible system messages.
- ✅ **Weight Tracking Fix**: Standardized modal opening/closing logic ensures the weight update interface is always interactive and visible.
- ✅ **Headings & Hierarchy**: Logical document structure with `<h1>` and `<h2>` for clear document outlining.
- ✅ **Mobile Optimized**: Font sizes ≥ 16px to prevent iOS auto-zoom, with safe-area inset support for "notch" devices.
- ✅ **Reduced Motion**: All animations respect the `prefers-reduced-motion` system setting.
- ✅ **Offline Reliability**: Service worker logic handles cross-origin requests and provides a robust offline fallback to the main app shell.

---

## PWA Install

| Platform | How |
|---|---|
| **iOS Safari** | Share → Add to Home Screen |
| **Android Chrome** | Menu → Add to Home Screen / Install App |
| **Desktop Chrome/Edge** | Address bar install icon |

---

## Security Headers (via `netlify.toml`)

```
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Content-Security-Policy: default-src 'self'; ...
X-Frame-Options: DENY
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

---

## Local Development

No build step required — it's a single HTML file.

```bash
# Clone
git clone https://github.com/sahilbnsll/fitness-app.git
cd fitness-app

# Open directly
open fitness_hub.html

# Or serve with any static server (needed for SW registration)
npx serve .
```

---

## Privacy

All data is stored in your browser's `localStorage`. Nothing is transmitted to any server. Clearing browser data will erase your logs — use the **Export JSON** button in the More tab to back up regularly.

---

## License

MIT
