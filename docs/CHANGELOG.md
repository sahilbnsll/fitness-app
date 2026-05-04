# Change Log

## 2026-05-04 Feature Expansion

- Added Quick Start one-screen workout mode with current exercise, visible timer status, complete-set action, previous/next exercise navigation, and workout finish feedback.
- Added RPE logging, drop-set flags, copy-set action, exercise notes, swipe-right complete, and swipe-left delete for workout sets.
- Added previous workout comparison and progressive overload weight suggestions.
- Added workout heatmap, best/current streak stats, missed workout detection, and today’s training suggestion.
- Added simple progress stats for today volume, sets done, weekly training load, muscles hit, and top exercise PRs.
- Added diet calories/protein tracker on the Diet tab.
- Added editable exercises, supplements, mobility routines, diet meals for the current session, and body stat goals.
- Added expanded body stat rings for weight, waist, chest, arms, hips, and body fat.
- Added visible JSON export/import controls and expanded backup contents to include workout logs, diet logs, mobility, and body goals.
- Added manifest/service-worker registration in the HTML and integrated PWA support files.
- Improved exercise library metadata with muscle, equipment, and movement-type tags.
- Replaced workout day badge text/emoji with clearer SVG-style muscle icons for push, pull, quad, hamstring, rest, and custom days.

Verification:

- Extracted inline JavaScript from `fitness_hub_v3.html` and ran `node --check`.
- Parsed `manifest.webmanifest` as JSON and ran `node --check sw.js`.
- Ran a static `getElementById` check to confirm literal DOM references exist.
- Ran `node test_diet.js`.

## 2026-05-04 Gap Analysis And Streak Fix

- Fixed streak date calculations to use local calendar dates instead of UTC date slices.
- Kept Sunday as a true rest day that never counts toward streaks and never breaks streaks.
- Added [GAP_ANALYSIS.md](GAP_ANALYSIS.md) covering present features, features needing improvement, missing features, and recommended build order.
- Added `.gitignore` for local/editor/cache/build artifacts.
- Updated README with a roadmap link.

Verification:

- Extracted inline JavaScript from `fitness_hub_v3.html` and ran `node --check`.
- Ran a static `getElementById` check to confirm literal DOM references exist.
- Ran `node test_diet.js`.

## 2026-05-04 Layout Repair

- Repaired the broken app shell by keeping More, Mobility, modals, and bottom navigation inside the same `#app` wrapper.
- Removed the stray wrapper close that caused later views to render outside the main application layout.
- Moved desktop width/centering from `body` to `#app` and aligned the fixed bottom navigation to the same max width.
- Preserved the bottom safe-area spacing so lower workout content can scroll above the fixed nav.
- Raised modal and rest timer layers so add/edit overlays no longer sit behind the fixed bottom navigation.

Verification:

- Extracted inline JavaScript from `fitness_hub_v3.html` and ran `node --check`.
- Ran a static `getElementById` check to confirm literal DOM references exist.
- Ran `node test_diet.js`.

## 2026-05-04 Initial Fixes

- Fixed empty Diet section by wiring the diet day tabs and meal content rendering into initialization.
- Rebuilt Supplements so daily checkboxes work and default stack includes protein, creatine, pre-workout, fish oil, and vitamin D3.
- Fixed Tracking layout by adding missing shared UI primitives, functional weight logging, measurement logging, progress rings, and measurement rendering.
- Expanded Mobility with default pre-workout, post-workout, stretch, breathing, and kegel routines with daily checkboxes.
- Hid the Training Hub hero outside the home/workout page so it no longer appears on every page.
- Added project documentation and this change log.

Verification:

- Extracted inline JavaScript from `fitness_hub_v3.html` and ran `node --check`.
- Ran a static `getElementById` check to confirm literal DOM references exist.
- Ran `node test_diet.js`.
