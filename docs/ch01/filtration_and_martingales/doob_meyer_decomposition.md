# Doob Meyer


This section explains the **Doob–Meyer decomposition**, a structural theorem stating that (under mild hypotheses) every submartingale can be written as the sum of a **martingale** and a **predictable increasing** process.

Fix a filtered probability space


$$
(\Omega,\mathcal{F},(\mathcal{F}_t)_{t\ge 0},\mathbb{P})
$$




satisfying the usual conditions.

---

## Motivation Drift


For an Itô process


$$
X_t = X_0 + \int_0^t b_s\,\mathrm{d}s + \int_0^t \sigma_s\,\mathrm{d}W_s,
$$




we can see explicitly a finite-variation “drift” and a martingale “noise”. Doob–Meyer asserts an analogous decomposition **without** assuming an SDE representation.

---

## Submartingales Class


A càdlàg adapted process \((X_t)_{t\ge 0}\) is a **submartingale** if for all \(0\le s\le t\),


$$
\mathbb{E}[X_t\mid \mathcal{F}_s] \ge X_s \quad \text{a.s.}
$$





It is of **class \((D)\)** if the family


$$
\{X_\tau:\ \tau \text{ is a bounded stopping time}\}
$$




is uniformly integrable.

---

## Predictable


A process \((A_t)_{t\ge 0}\) is
- **increasing** if \(A_s \le A_t\) a.s. for \(s\le t\),
- **predictable** if it is measurable with respect to the predictable \(\sigma\)-algebra on \(\Omega\times[0,\infty)\),
- of **finite variation** if its sample paths have finite total variation on compact intervals.

---

## Theorem Doob Meyer


**Theorem.** If \((X_t)_{t\ge 0}\) is a càdlàg submartingale of class \((D)\), then there exist:
- a càdlàg martingale \((M_t)_{t\ge 0}\),
- a predictable càdlàg increasing process \((A_t)_{t\ge 0}\) with \(A_0=0\),

such that


$$
\boxed{
X_t = X_0 + M_t + A_t,\qquad t\ge 0.
}
$$





Equivalently,


$$
\boxed{
M_t := X_t - X_0 - A_t \quad \text{is a martingale.}
}
$$





---

## Uniqueness


If


$$
X_t = X_0 + M_t + A_t = X_0 + \widetilde{M}_t + \widetilde{A}_t
$$




with both \(A,\widetilde{A}\) predictable increasing and \(M,\widetilde{M}\) martingales, then


$$
\boxed{
A_t=\widetilde{A}_t\ \text{for all }t\quad\text{a.s.}
}
$$




Hence \(M=\widetilde{M}\) as well.

Reason: \(A-\widetilde{A}=\widetilde{M}-M\) is both finite variation and a martingale, hence (up to indistinguishability) constant; with zero initial value it must be \(0\).

---

## Example W t 2


For Brownian motion \(W_t\), Itô’s formula gives


$$
W_t^2 = W_0^2 + 2\int_0^t W_s\,\mathrm{d}W_s + t.
$$




Thus


$$
M_t = 2\int_0^t W_s\,\mathrm{d}W_s,\qquad A_t=t
$$




yields the Doob–Meyer decomposition of the submartingale \(W_t^2\).

---

## Connection Optional


Doob–Meyer is a **structural** theorem (what a submartingale is made of). Optional Sampling is a **behavioral** theorem (how martingales behave when stopped). A common pattern is:
1. Decompose \(X=M+A\) via Doob–Meyer,
2. Apply Optional Sampling to \(M\) to obtain identities for stopped processes.

---

## What Remember


- **Submartingale** \(=\) **martingale** \(+\) **predictable increasing**.
- The predictable increasing part is unique and captures the “drift” relative to the filtration.
