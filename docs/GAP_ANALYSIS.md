# Fitness App Gap Analysis

Last updated: 2026-05-04

## Implementation Update

The 2026-05-04 feature expansion moved several items out of “missing” into “present but still needs polish”: Quick Start workout mode, RPE logging, drop-set flags, exercise notes, swipe set actions, progressive overload suggestions, workout heatmap, missed workout detection, training load, diet calorie/protein tracking, visible backup/restore UI, body stat rings, and PWA support.

These features are intentionally lightweight first versions. The remaining gap is polish: reducing tap count further, improving charts, hardening data migration, and making plan editing more complete.

## Current State

The app is a single-file offline-first HTML/CSS/JavaScript fitness tracker. It already has useful foundations: a 6-day PPL plan, workout set logging, exercise library modal, diet tab, supplements, mobility, bodyweight tracking, and `localStorage` persistence.

The next big product direction is to make it feel like a real gym companion: fewer taps, better workout mode, smarter suggestions, richer charts, and safer data portability.

## Present And Usable

1. **LocalStorage Persistence**

   Present. Current data is stored across several keys such as `ft_tracker_v1`, `ft_exercises_v1`, `ft_workout_logs_v1`, `ft_weight_history`, `ft_supplements_v1`, `ft_supp_log_v1`, `ft_measurements`, and `ft_mobility_v1`.

2. **Structured Workout Plans**

   Present. The app ships with a fixed Push/Pull/Legs split across Monday-Saturday, with Sunday as rest.

3. **Basic Workout Logger**

   Present. Exercise rows open a logger for sets, reps, weight, completion, add set, and rest timer.

4. **Exercise Library**

   Present. There is a predefined exercise database, custom exercise creation, search, and muscle-group filters.

5. **Basic Supplements**

   Present. Default supplements and daily checkbox tracking exist. Custom supplement add/delete exists.

6. **Basic Mobility**

   Present. Default mobility routines and daily checkbox tracking exist. Custom mobility add/delete exists.

7. **Bodyweight Tracker**

   Present. Daily weight input and a simple SVG line chart exist.

8. **Diet Tab**

   Present. A generated 15-day diet plan exists with macros, micronutrients, and meals.

9. **Haptic Feedback**

   Partially present. Timer completion uses `navigator.vibrate`.

10. **Offline First**

   Mostly present. The app runs locally without backend/API calls, though it loads Google Fonts from the network unless cached.

11. **PWA Support**

   Present. Apple mobile web app meta tags, `manifest.webmanifest`, service worker registration, and offline app-shell caching exist. App icon assets still need polish.

12. **Export / Import Helpers**

   Present. Export/import helpers are wired from the More tab and include workout logs, diet logs, mobility, supplements, body goals, and measurements.

## Present But Needs Improvement

1. **Workout Logger Tap Count**

   Improved with Quick Complete, copy set, previous values, and swipe gestures. It still needs an even more polished one-tap path for every common gym scenario.

2. **Superset Support**

   Partial. Superset tags exist and drop-set flags exist, but true paired/grouped superset completion still needs a dedicated flow.

3. **Custom Plans / Custom Days**

   Partial. Custom day creation and exercise editing exist, but full persistent plan templates, plan metadata, and reordering are not built.

4. **Progress Tracking**

   Improved with PRs, today volume, sets done, muscles hit, weekly load, weight chart, and heatmap. It still needs richer charts per exercise and longer-term trend views.

5. **Previous Workout Comparison**

   Improved. Logger and workout mode show last set and next-weight suggestions. It still needs a clearer visual comparison table.

6. **Diet Tracker**

   Improved. Daily calories/protein tracking exists. Meal-level consumed tracking and persistent edited meal plans still need work.

7. **Body Stats Rings**

   Improved. Weight, waist, chest, arms, hips, and body-fat rings with editable goals exist. Per-metric history charts still need work.

8. **Icons**

   Improved for workout day badges with inline SVG-style muscle icons. Remaining emoji icons elsewhere can be replaced later.

9. **Edit Features**

   Improved. Exercises, supplements, mobility routines, body goals, and current-session diet meals can be edited. Full plan metadata and persistent diet-plan editing still need work.

10. **PWA Install**

   Manifest and service worker exist. Real app icon assets and install-flow testing still need work.

## Not Present Yet

1. **Structured Unified Storage**

   Current storage is still split across multiple legacy keys. Target shape should move toward:

   ```json
   {
     "workouts": [],
     "exercises": [],
     "plans": [],
     "bodyStats": [],
     "nutrition": [],
     "stats": {}
   }
   ```

2. **Full Adaptive Training Engine**

   The app has simple “what to train today” messaging, but it does not yet track muscle freshness deeply or adapt the plan from recovery history.

3. **Dedicated Workout Summary Screen**

   Finish feedback and progress cards exist, but there is not yet a dedicated summary screen with PR celebration, session RPE, and shareable closure.

## Recommended Build Order

1. **Stabilize Data Model**

   Add a migration layer from current `ft_*` keys into one structured app state while preserving existing data.

2. **Workout Logger v2**

   Add RPE, notes, last-set comparison, one-tap complete, better autofill, superset/drop-set modeling, and volume calculation.

3. **Workout Mode**

   Build a one-screen active workout flow with current exercise, add set, timer, haptics, wake lock, and summary.

4. **Progress Analytics**

   Add exercise max weight chart, volume chart, PR detection, body stats rings, and training load.

5. **Plan Builder**

   Support custom days, editable exercises, tags, target rep ranges, and notes.

6. **Diet Tracker v2**

   Keep the 15-day plan but add daily calories/protein tracking and quick-add meals.

7. **PWA + Backup**

   Add manifest, service worker, visible export/import UI, and installation polish.

## Product Standard

The main success metric should be workout logging friction. Common set completion should be one tap after opening workout mode. Any flow that needs more than two taps during training needs simplification.
