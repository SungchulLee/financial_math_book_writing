# Grzelak Textbook Cross-Reference

This page maps the chapters of this course to the corresponding chapters in *Mathematical Modeling and Computation in Finance* by C.W. Oosterlee and L.A. Grzelak (World Scientific, 2019). Many Python code examples in this course are adapted from or based on the textbook's implementations.

---

## Quick Reference Table

| Course Chapter | Grzelak Chapter(s) | Main Theme | Alignment |
|---|---|---|---|
| Ch 1 (Discrete Models, FTAP) | Ch 2 (partial) | Binomial model, risk-neutral pricing | Related |
| Ch 2 (Stochastic Processes) | Ch 2 | Brownian motion, random walks | Direct |
| Ch 3 (SDEs, Itô Calculus) | Ch 2, 3 | SDEs, GBM, Itô's lemma | Direct |
| Ch 4 (Measure Change) | Ch 2 | Girsanov theorem, Radon-Nikodym | Direct |
| Ch 5 (PDE, Feynman-Kac) | Ch 5 (partial) | Heat equation, BS PDE | Related |
| Ch 6 (Black-Scholes Model) | Ch 6 | BS formula, European options | Direct |
| Ch 7 (Exotic Options, Jump-Diffusion) | Ch 6, 7, 9 | Monte Carlo, Merton, Poisson | Direct |
| Ch 8 (Numerical Methods for BS PDE) | Ch 5 | FDM: explicit, implicit, Crank-Nicolson | Direct |
| Ch 9 (Fourier / COS Pricing) | Ch 8 | COS method, FFT, density recovery | Direct |
| Ch 10 (Greeks) | Ch 3 (partial) | Sensitivities, pathwise estimation | Related |
| Ch 11 (Hedging) | Ch 3 (partial) | Delta hedging, hedge with jumps | Related |
| Ch 12 (Implied Volatility) | Ch 14 (partial) | Implied vol, vol surface | Partial |
| Ch 13 (Local Volatility) | Ch 14 | Dupire, local vol | Related |
| Ch 14 (Stoch. Vol, SABR, Rough Vol) | Ch 13, 14 | SABR, rough Heston | Related |
| Ch 15 (Affine Processes) | Ch 10 (partial) | Characteristic functions, affine models | Related |
| Ch 16 (Heston Model) | Ch 10 | Heston, CIR vol, discretization | Direct |
| Ch 17 (Calibration) | Ch 10, 14 | Model calibration | Related |
| Ch 18 (Fixed Income) | Ch 11 | Vasicek, CIR, Ho-Lee, yield curves | Direct |
| Ch 19 (Complex Bond Products) | Ch 11 | Multi-curve, mortgages, LMM | Direct |
| Ch 20 (Hull-White Model) | Ch 11, 12 | HW model, hybrid models | Direct |
| Ch 21 (Credit Risk) | — | Merton credit, CDS | Course only |
| Ch 22 (Risk Management) | — | VaR, ES, CVA, xVA | Course only |
| Ch 23 (Robust Pricing) | — | Model uncertainty | Course only |
| Ch 24 (AI in Finance) | — | Neural nets, deep hedging, RL | Course only |

---

## Cross-Reference by Concept

**Brownian Motion and Stochastic Calculus**
Course: Ch 2–4 | Grzelak: Ch 2
Both cover Wiener process construction, Itô integral, Itô's lemma, and Girsanov theorem. The course emphasizes simulation and visualization; the textbook emphasizes mathematical rigor.

**Monte Carlo Methods**
Course: Ch 7 | Grzelak: Ch 3–4
Both cover variance reduction, path-dependent options, and American options via LSM. The textbook provides more detail on SDE discretization schemes (Euler, Milstein) and convergence analysis.

**Black-Scholes and European Options**
Course: Ch 6 | Grzelak: Ch 6
Nearly identical coverage: BS formula, put-call parity, digital options, closed-form pricing.

**Finite Difference Methods**
Course: Ch 8 | Grzelak: Ch 5
Both cover explicit/implicit/Crank-Nicolson schemes, stability analysis, and American option pricing via FDM.

**Fourier / COS Methods**
Course: Ch 9 | Grzelak: Ch 8
Both cover the COS method for option pricing, FFT-based approaches, and density recovery. The textbook provides more implementation detail.

**Heston and Stochastic Volatility**
Course: Ch 16 | Grzelak: Ch 10
Both cover the Heston model extensively: characteristic function, CIR variance process, discretization schemes (QE, exact), and COS pricing.

**Jump-Diffusion Models**
Course: Ch 7 | Grzelak: Ch 9
Both cover Merton jump-diffusion, compound Poisson processes, and Bates model. The textbook includes Kou double-exponential and affine jump-diffusion.

**Interest Rate Models**
Course: Ch 18–20 | Grzelak: Ch 11–12
Both cover Vasicek, CIR, Hull-White, HJM, and multi-curve construction. The textbook includes more on hybrid equity-IR models and FX extensions (Ch 12).

**SABR and Local/Stochastic Vol**
Course: Ch 12–14 | Grzelak: Ch 13–14
Both cover SABR model and implied volatility. The textbook adds local-stochastic volatility models and advanced calibration.

---

## Topics Unique to This Course

Chapters 21–24 cover material not in the Grzelak textbook: credit risk (Merton structural model, CDS pricing), risk management (VaR, Expected Shortfall, CVA/xVA), robust pricing under model uncertainty, and AI/ML applications (neural network pricing, deep hedging, reinforcement learning for portfolios).

## Topics Unique to the Grzelak Textbook

Grzelak Ch 12 (Hybrid Models in full generality), Ch 14 (Stochastic Local Volatility — SLV models and advanced calibration), and Ch 15 (advanced research-level topics) go beyond the scope of this course.

---

## Grzelak Code Files in This Course

All Grzelak-authored Python files in this course are marked with "(Grzelak)" in the navigation. They are distributed across chapters 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 16, 18, 19, 20, and 22.
