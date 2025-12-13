# Strong Markov Property

This section states the **strong Markov property** for Brownian motion and (under standard assumptions) for diffusions. It is conceptually different from the **Optional Sampling Theorem**, which concerns expectations of martingales rather than conditional laws of future paths.

---

## Markov vs Strong Markov

A process \((X_t)\) is (time-inhomogeneous) Markov if for bounded measurable \(\varphi\) and \(0\le s\le t\),
\[
\boxed{
\mathbb{E}[\varphi(X_t)\mid \mathcal{F}_s] = \mathbb{E}[\varphi(X_t)\mid X_s].
}
\]

It is **strong Markov** if the same property holds when \(s\) is replaced by a stopping time \(\tau\).

---

## Strong Markov Property (Stopping-Time Form)

Let \(\tau\) be a stopping time. For bounded measurable \(\varphi\) and \(t\ge 0\),
\[
\boxed{
\mathbb{E}[\varphi(X_{\tau+t})\mid \mathcal{F}_\tau]
=
\mathbb{E}^{X_\tau}[\varphi(X_t)].
}
\]

Equivalently, conditionally on \(X_\tau\), the post-\(\tau\) evolution is independent of the past and distributed like a fresh copy started from \(X_\tau\).

---

## Brownian Motion Case

If \(W_t\) is Brownian motion and \(\tau\) is a stopping time, define
\[
B_t := W_{\tau+t} - W_\tau.
\]
Then
\[
\boxed{
(B_t)_{t\ge 0} \text{ is Brownian motion and is independent of }\mathcal{F}_\tau.
}
\]

---

## Diffusion Case (Under Standard Conditions)

If \(X_t\) solves an SDE
\[
\mathrm{d}X_t^{i} = b^{i}(t,X_t)\,\mathrm{d}t + \sigma^{i\alpha}(t,X_t)\,\mathrm{d}W_t^\alpha
\]
with assumptions ensuring existence and uniqueness of strong solutions (e.g. local Lipschitz and linear growth), then \(X\) is strong Markov.

---

## Application: Exit Times

For an open set \(D\subset \mathbb{R}^d\), the exit time
\[
\tau_D := \inf\{t\ge 0: X_t\notin D\}
\]
is a stopping time. Strong Markov allows “restart at \(\tau_D\)” arguments, essential in hitting/exit problems and boundary value PDEs.

---

## What to Remember

- Markov: memoryless at deterministic times.
- Strong Markov: memoryless at stopping times.
- For Brownian motion, increments after \(\tau\) are independent Brownian motion.
