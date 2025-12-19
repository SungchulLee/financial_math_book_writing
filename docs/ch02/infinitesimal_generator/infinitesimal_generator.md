# Infinitesimal Generator

Let \(X_t\) be a Markov process and \(f:\mathbb R\to\mathbb R\) a smooth test function.

## Definition

The infinitesimal generator \(L\) is defined by

\[
Lf(x) := \lim_{t\downarrow 0}\frac{\mathbb E_x[f(X_t)] - f(x)}{t}.
\]



It measures the **instantaneous rate of change of expected observables**.

## Generator of a Diffusion

If \(X_t\) solves

\[
dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t,
\]


then

\[
Lf(x) = \mu(x)f'(x) + \frac12\sigma^2(x)f''(x).
\]



## Interpretation

- \(L\) is a **local object**
- It depends only on infinitesimal drift and variance
- It completely characterizes the diffusion

## Where the Generator Appears

- Kolmogorov backward equation
- Dynkin’s formula
- Martingale problems
- Adjoint operator → Fokker–Planck equation
