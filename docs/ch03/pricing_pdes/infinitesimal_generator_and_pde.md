# Infinitesimal


## Motivation

In continuous-time finance, derivative prices are functions of time and the current state of the underlying assets.
The evolution of these prices is governed by partial differential equations (PDEs).
The central mathematical object linking stochastic dynamics to PDEs is the **infinitesimal generator**.

This section explains why *every arbitrage-free pricing PDE is determined by the generator of the underlying process*.

---

## Diffusion Models

Let \((X_t)_{t \ge 0}\) be a one-dimensional Itô diffusion:
\[
dX_t = b(X_t)\,dt + \sigma(X_t)\,dW_t.
\]

For any twice continuously differentiable function \(f \in C^2\), Itô's formula gives
\[
df(X_t) = \mathcal{L}f(X_t)\,dt + \sigma(X_t) f_x(X_t)\,dW_t,
\]
where the **infinitesimal generator** is defined by
\[
\boxed{
\mathcal{L}f(x) = b(x) f_x(x) + \tfrac12 \sigma^2(x) f_{xx}(x).
}
\]

The generator captures the *local drift and volatility structure* of the process.

---

## Backward Kolmogorov

Let
\[
u(t,x) = \mathbb{E}[\Phi(X_T) \mid X_t = x].
\]

Then \(u\) satisfies the backward Kolmogorov equation:
\[
\partial_t u + \mathcal{L}u = 0,
\quad u(T,x) = \Phi(x).
\]

This PDE describes the evolution of conditional expectations backward in time.

---

## Pricing PDE

In finance, future payoffs must be discounted.
If the short rate is constant \(r\), the price is
\[
V(t,x) = \mathbb{E}\left[e^{-r(T-t)}\Phi(X_T) \mid X_t = x\right].
\]

Applying Feynman–Kac yields the **pricing PDE**:
\[
\boxed{
\partial_t V + \mathcal{L}V - rV = 0,
}
\quad V(T,x) = \Phi(x).
\]

---

## Financial

- The generator encodes the **economic dynamics** of the underlying asset.
- The discount term \(-rV\) reflects time value of money.
- Pricing reduces to solving a backward PDE.

---

## Connection Forward

Understanding the generator explains why pricing PDEs take a universal form.
Next, we investigate how **martingale conditions** eliminate arbitrage.