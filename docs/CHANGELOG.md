# Change Log

## 2026-05-04 Branding: FitPal Launch

- **Branding**: Renamed the application from "Training Hub" to **FitPal** across all UI elements, page titles, and documentation.
- **PWA Integrity**: Updated `manifest.webmanifest` and `sw.js` with the new app name and corrected all file references to point to the renamed `fitness_hub.html`.
- **Documentation**: Simplified `README.md` to a concise 5-point value proposition as per user request.

Verification:
- Verified `<h1>` and `<title>` show "FitPal".
- Confirmed `manifest.webmanifest` name/short_name is "FitPal".
- Verified `sw.js` cache version and APP_SHELL paths are correct.

## 2026-05-04 High-Density Dashboard & Efficiency Pass

- **Visual Density**: Refactored the Workout and Adherence modules to a nested-card layout. Performance stats are now integrated directly inside the tracker cards for better visual balance and zero wasted space.
... [remaining entries preserved]
