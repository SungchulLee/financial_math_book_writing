# Study Paths and Topic Dependencies

This page provides recommended study paths through the course material, depending on your focus area and background.

## Course Structure Overview

The course spans **24 chapters** organized into five parts:

| Part | Chapters | Focus |
|------|----------|-------|
| **I: Math Foundations** | Ch 1–5 | Discrete models, stochastic processes, SDEs, measure change, PDEs |
| **II: Black–Scholes and Extensions** | Ch 6–11 | BS model, exotic options, numerical methods, Fourier pricing, Greeks, hedging |
| **III: Volatility and Calibration** | Ch 12–17 | Implied/local/stochastic volatility, affine processes, Heston, calibration |
| **IV: Interest Rates and Credit** | Ch 18–21 | Short-rate models, HJM, Hull–White, credit risk |
| **V: Risk and AI** | Ch 22–24 | Risk management, robust pricing, AI in finance |

## Topic Dependencies

```
Part I: Math Foundations (Ch 1–5) → All other parts

Part II (Ch 6–11) depends on:
  Ch 1 (Discrete Models, FTAP)
  Ch 2 (Stochastic Processes)
  Ch 3 (SDEs, Itô Calculus)
  Ch 4 (Measure Change, Girsanov)
  Ch 5 (PDE, Feynman–Kac)

Part III (Ch 12–17) depends on:
  Part II (especially Ch 6, 7, 10)
  Ch 5 (PDEs)

Part IV (Ch 18–21) depends on:
  Ch 3 (SDEs)
  Ch 4 (Measure Change)
  Ch 5 (PDEs, Kolmogorov)
  Ch 15 (Affine Processes)

Part V (Ch 22–24) depends on:
  Selectively from Parts I–IV
```

## Recommended Study Paths

### Path 1: Derivatives Pricing Track

For students interested in option pricing theory and implementation:

Ch 1 (Discrete Models, Binomial Trees) → Ch 2 (Brownian Motion) → Ch 3 (Itô Calculus, SDEs) → Ch 4 (Girsanov) → Ch 6 (Black–Scholes) → Ch 7 (Exotic Options) → Ch 8 (Numerical Methods for BS PDE) → Ch 9 (Fourier/COS Pricing) → Ch 10 (Greeks)

### Path 2: Volatility Modeling Track

For students focused on volatility modeling and calibration:

Ch 2 (Stochastic Processes) → Ch 3 (SDEs) → Ch 6 (Black–Scholes) → Ch 12 (Implied Volatility) → Ch 13 (Local Volatility) → Ch 14 (Stochastic Volatility, SABR) → Ch 15 (Affine Processes) → Ch 16 (Heston Model) → Ch 17 (Calibration)

### Path 3: Computational Methods Track

For students interested in numerical and simulation techniques:

Ch 2 (BM Simulation) → Ch 3 (SDE Simulation) → Ch 5 (Heat Equation, FFT) → Ch 7 (Monte Carlo for Exotics) → Ch 8 (Finite Difference Methods) → Ch 9 (COS/FFT Pricing) → Ch 16 (Heston MC/FDM)

### Path 4: Interest Rates Track

For students focused on fixed income:

Ch 2 (Stochastic Processes) → Ch 3 (SDEs) → Ch 4 (Measure Change) → Ch 15 (Affine Processes) → Ch 18 (Term Structure, Vasicek, CIR) → Ch 19 (HJM, LMM, Derivatives) → Ch 20 (Hull–White Model)

### Path 5: Risk Management and AI Track

For students interested in risk management and machine learning in finance:

Ch 6 (Black–Scholes) → Ch 10 (Greeks) → Ch 11 (Hedging) → Ch 21 (Credit Risk) → Ch 22 (Risk Management, VaR, XVA) → Ch 23 (Robust Pricing) → Ch 24 (AI in Finance, Deep Hedging, RL)

## Prerequisites

### Mathematical Background

- Real analysis (measure theory helpful)
- Probability theory (measure-theoretic preferred)
- Linear algebra and matrix theory
- Partial differential equations (basic)
- Numerical analysis (basic)

### Python Proficiency

- Core Python (functions, classes, modules)
- NumPy and SciPy
- Data structures and algorithms
- Object-oriented programming

### Recommended Preparation

- Stochastic calculus (can be learned concurrently with the course)
- Financial markets basics
- Optimization theory

## Key Textbooks

1. **Shreve, S.E.** (2004). *Stochastic Calculus for Finance I & II*. Springer.
2. **Oosterlee, C.W. & Grzelak, L.A.** (2019). *Mathematical Modeling and Computation in Finance*. World Scientific.
3. **Glasserman, P.** (2003). *Monte Carlo Methods in Financial Engineering*. Springer.
4. **Hull, J.C.** (2021). *Options, Futures, and Other Derivatives*. Pearson.
