# Fitness App

A single-file mobile-first fitness tracker in `fitness_hub_v3.html`.

## What It Does

- Tracks a 6-day PPL workout split with weekly completion status.
- Logs workout sets, reps, weight, and rest timer data in `localStorage`.
- Shows a 15-day diet plan with training/rest day macros, micronutrients, and meals.
- Tracks default daily supplements with checkboxes: protein, creatine, pre-workout, fish oil, and vitamin D3.
- Tracks body weight history, measurements, progress rings, and a small trend chart.
- Includes cardio, deload, and mobility sections with daily mobility checkboxes.
- Uses a centered app shell with a fixed bottom navigation that stays aligned on desktop and mobile.

## Roadmap

See [docs/GAP_ANALYSIS.md](docs/GAP_ANALYSIS.md) for what exists today, what needs improvement, and what is missing from the target gym-companion feature set.

## How To Run

Open `fitness_hub_v3.html` in a browser. No build step is required.

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

Clearing browser site data will reset the app.

## Maintenance Rule

Update `README.md` when the application behavior, setup, or storage model changes.
Update `docs/CHANGELOG.md` after every request/change with a short note of what changed and how it was checked.
