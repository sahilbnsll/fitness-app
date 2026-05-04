# Fitness App

A single-file mobile-first fitness tracker in `fitness_hub_v3.html`.

## What It Does

- Tracks a 6-day PPL workout split with weekly completion status.
- Logs workout sets, reps, weight, RPE, drop-set flags, exercise notes, and rest timer data in `localStorage`.
- Includes Quick Start one-screen workout mode with previous-set comparison and progressive overload suggestions.
- Shows a 15-day diet plan with training/rest day macros, micronutrients, and meals.
- Adds a simple daily calories/protein diet tracker.
- Tracks default daily supplements with checkboxes: protein, creatine, pre-workout, fish oil, and vitamin D3.
- Supports adding, editing, and deleting exercises, supplements, and mobility routines.
- Tracks body weight history, measurements, progress rings, body stat rings, and simple workout progress stats.
- Includes cardio, deload, and mobility sections with daily mobility checkboxes.
- Shows streak stats, missed workout messaging, and a 28-day workout heatmap.
- Uses a centered app shell with a fixed bottom navigation that stays aligned on desktop and mobile.

## Roadmap

See [docs/GAP_ANALYSIS.md](docs/GAP_ANALYSIS.md) for what exists today, what needs improvement, and what is missing from the target gym-companion feature set.

## How To Run

Open `fitness_hub_v3.html` in a browser. No build step is required.

## PWA Support

The repository includes `manifest.webmanifest` and `sw.js` for offline support. `fitness_hub_v3.html` links the manifest and registers the service worker. Serve the app over `http://localhost` or HTTPS for service worker registration to work.

The service worker pre-caches `fitness_hub_v3.html` and serves that file for offline navigation after registration.

## Data Storage

The app stores user data in browser `localStorage`, including:

- `ft_tracker_v1`
- `ft_exercises_v1`
- `ft_weight_v1`
- `ft_weight_history`
- `ft_workout_logs_v1`
- `ft_supplements_v1`
- `ft_supp_log_v1`
- `ft_measurements`
- `ft_mobility_v1`
- `ft_diet_log_v1`
- `ft_body_goals_v1`
- `ft_custom_days_v1`

Clearing browser site data will reset the app.

## Maintenance Rule

Update `README.md` when the application behavior, setup, or storage model changes.
Update `docs/CHANGELOG.md` after every request/change with a short note of what changed and how it was checked.
