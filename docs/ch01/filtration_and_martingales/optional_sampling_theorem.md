# Optional Sampling Theorem

## Statement (basic bounded stopping times)

Let \(\{M_t\}_{t\ge 0}\) be a martingale with respect to \((\mathcal{F}_t)\). Let \(\sigma\) and \(\tau\) be stopping times such that
\[
0\le \sigma \le \tau \le T
\quad \text{almost surely}
\]
for some constant \(T<\infty\). Then
\[
\boxed{
\mathbb{E}[M_{\tau}\mid \mathcal{F}_{\sigma}] = M_{\sigma}
}
\]
and in particular
\[
\boxed{
\mathbb{E}[M_{\tau}] = \mathbb{E}[M_{\sigma}].
}
\]

This is the **optional sampling theorem** in its cleanest bounded form.

---

## Proof idea (stopping and approximation)

Define the stopped martingale
\[
M_t^{\tau} := M_{t\wedge \tau}.
\]
For bounded \(\tau\le T\), one shows \(M_t^{\tau}\) is a martingale. Then for \(s\le t\),
\[
\mathbb{E}[M_{t\wedge \tau}\mid \mathcal{F}_s] = M_{s\wedge \tau}.
\]
Choosing \(s=\sigma\) and \(t=T\) yields the result since \(T\wedge \tau=\tau\) and \(\sigma\wedge \tau=\sigma\).

---

## Why boundedness matters

Without boundedness (or other integrability conditions), optional sampling may fail. Typical sufficient conditions include:

- \(\tau\) bounded (the simplest).
- \(\tau\) integrable and \(M\) uniformly integrable.
- \(\tau\) bounded in expectation with suitable \(L^p\) bounds.

A standard counterexample uses the martingale \(W_t\) and an unbounded hitting time \(\tau_a\): although \(\mathbb{E}[W_{\tau_a}]=a\), one cannot always justify passing limits without integrability control.

---

## Application template

Optional sampling is often used in this pattern:

1. Construct a martingale \(M_t\) from Brownian motion or a diffusion (often via Itô’s formula).
2. Choose a stopping time \(\tau\) (e.g., an exit time from a domain).
3. Apply
\[
\mathbb{E}[M_{\tau\wedge T}] = \mathbb{E}[M_0]
\]
and then let \(T\to\infty\) with justification.
4. Extract probabilities or expectations of interest (hitting probabilities, expected exit times, harmonic measure, etc.).
