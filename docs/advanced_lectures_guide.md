# Advanced Lectures: Interest Rates, Hybrid Models, and Risk

This page provides a guide to the advanced lecture series by L.A. Grzelak, covering interest rate modeling, cross-asset derivatives, valuation adjustments, and risk management. The Python implementations from these lectures are integrated into Chapters 18–22 of this course.

**Level:** Advanced (Graduate/Professional)

**Prerequisites:** Chapters 1–5 (Stochastic Calculus Foundations), Chapters 18–20 (Interest Rate Models)

**Reference:** Based on the "Financial Engineering" course by L.A. Grzelak and the textbook *Mathematical Modeling and Computation in Finance* by C.W. Oosterlee and L.A. Grzelak (World Scientific, 2019).

---

## Lecture Series Overview

### Part I: Interest Rate Foundations (Lectures 1–7)

**Lecture 1 — Introduction and Overview**
Course structure and overview of interest rate markets. No Python code.

**Lecture 2 — Filtrations and Measures**
Advanced probability theory applied to interest rate markets: filtration-adapted processes, risk-neutral measures, martingale representation, and jump processes in rates.
Python code in this course: `ch04/codes/grzelak_martingale_verification.py`, `ch07/codes/grzelak_bs_jump_volatility.py`

**Lecture 3 — The HJM Framework**
Heath-Jarrow-Morton forward rate dynamics, no-arbitrage drift conditions, and the connection from HJM to short rate models.
Python code: `ch18/codes/grzelak_cir_ir_paths.py`, `ch18/codes/grzelak_ho_lee_zcbs.py`, `ch20/codes/grzelak_hull_white_paths.py`, `ch20/codes/grzelak_hull_white_zcbs.py`

**Lecture 4 — Yield Curve Dynamics under Short Rate**
Short rate models (Vasicek, CIR, Hull-White), yield curve evolution, term structure dynamics, and model comparison.
Python code: `ch20/codes/grzelak_hull_white_zcbs_v2.py`, `ch20/codes/grzelak_hw_1f_2f_comparison.py`, `ch20/codes/grzelak_hw_compound_rate_sim.py`

**Lecture 5 — Interest Rate Products**
Caps, floors, swaptions, and options on zero-coupon bonds under the Hull-White model.
Python code: `ch20/codes/grzelak_hw_caplets.py`, `ch20/codes/grzelak_hw_options_on_zcbs.py`, `ch20/codes/grzelak_swaps_hw.py`

**Lecture 6 — Construction of Yield Curve and Multi-Curve**
Post-crisis multi-curve framework: OIS discounting, basis spreads, bootstrapping, and Treasury curve construction.
Python code: `ch19/codes/grzelak_multi_curve_build.py`, `ch19/codes/grzelak_yield_curve_greeks.py`, `ch19/codes/grzelak_yield_curve_treasury.py`

**Lecture 7 — Pricing of Swaptions and Negative Interest Rates**
Swaption pricing, Jamshidian's trick, shifted lognormal and normal (Bachelier) models for negative rate environments.
Python code: `ch20/codes/grzelak_hw_caplets_and_floorlets.py`, `ch20/codes/grzelak_jamshidian_trick.py`, `ch20/codes/grzelak_shifted_lognormal.py`

---

### Part II: Advanced Topics (Lectures 8–14)

**Lecture 8 — Mortgages and Prepayments**
Mortgage mathematics, prepayment modeling, MBS valuation, and stochastic amortization schedules.
Python code: `ch19/codes/grzelak_annuity_mortgage.py`, `ch19/codes/grzelak_bullet_mortgage.py`, `ch19/codes/grzelak_mortgage_incentives.py`, `ch19/codes/grzelak_stochastic_amortizing_swap.py`

**Lecture 9 — Hybrid Models and Stochastic Interest Rates**
Equity-IR hybrid models combining Black-Scholes or Heston with Hull-White. Covers the BSHW and Schöbel-Zhu Hull-White (SZHW) models for pricing cross-asset derivatives.
Python code: `ch20/codes/grzelak_bshw_comparison.py`, `ch20/codes/grzelak_bshw_implied_volatility.py`, `ch20/codes/grzelak_heston_hw_cos_vs_mc.py`, `ch20/codes/grzelak_szhw_implied_volatilities.py`, `ch20/codes/grzelak_szhw_mc_diversification.py`

**Lecture 10 — Foreign Exchange (FX) and Inflation**
FX derivatives pricing with the Heston-Hull-White hybrid model using COS method and Monte Carlo.
Python code: `ch20/codes/grzelak_heston_hw_fx_cos_vs_mc.py`

**Lecture 11 — Market Models and Convexity Adjustments**
LIBOR Market Model (LMM), convexity corrections, and displaced diffusion for implied volatility modeling.
Python code: `ch19/codes/grzelak_convexity_correction.py`, `ch19/codes/grzelak_dd_implied_volatility.py`

**Lecture 12 — Valuation Adjustments (xVA)**
Credit Valuation Adjustment (CVA), Bilateral CVA (BCVA), and Funding Valuation Adjustment (FVA). Exposure modeling with netting.
Python code: `ch22/codes/grzelak_exposures_hw_netting.py`

**Lecture 13 — Value-at-Risk and Expected Shortfall**
Historical VaR, Monte Carlo VaR, and Expected Shortfall computation.
Python code: `ch22/codes/grzelak_historical_var.py`, `ch22/codes/grzelak_monte_carlo_var.py`

**Lecture 14 — Course Summary**
Integration of all topics and review of applications. No additional Python code.

---

## Recommended Study Order

For students working through this course, the advanced lectures are best studied after completing the foundation chapters:

1. Complete Ch 1–5 (Stochastic Calculus, SDEs, PDEs)
2. Complete Ch 6–9 (Black-Scholes, Exotic Options, Numerical Methods, Fourier)
3. Complete Ch 15–16 (Affine Processes, Heston Model)
4. Study Ch 18 (Fixed Income Fundamentals) → then Lectures 1–4
5. Study Ch 19 (Complex Bond Products) → then Lectures 5–8
6. Study Ch 20 (Hull-White Model) → then Lectures 9–10
7. Study Ch 22 (Risk Management) → then Lectures 11–13
