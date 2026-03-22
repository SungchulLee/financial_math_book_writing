| | v1 | v2 |
|---|---|---|
| Math score | 1.0 / 10 | 9.0 / 10 |
| Writing score | 1.0 / 10 | 9.0 / 10 |

v1 → v2  2026-03-23
Math fixes: 4 (🔴 4, 🟡 0, 🟢 0)
- 🔴 1: Cap calibration objective function with weighted squared errors
- 🔴 2: Swaption calibration objective and joint calibration weighting
- 🔴 3: Theta calibration via numerical differentiation of market curve
- 🔴 4: Validation via Hessian-based parameter uncertainty and repricing
Writing fixes: 6 (🔴 4, 🟡 1, 🟢 1)
- 🔴 1: Pipeline overview with three-stage structure
- 🔴 2: Code-to-math mapping for each calibration stage
- 🔴 3: Replaced generic objectives with calibration-workflow-specific ones
- 🔴 4: Added prerequisite links and cross-references
- 🟡 1: Warning about one-factor limitations for swaption fit
- 🟢 1: Removed generic placeholder text
Skipped: none
