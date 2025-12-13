# Quadratic Variation

## Motivation

Brownian motion is continuous but extremely rough. The key quantitative measure of this roughness is **quadratic variation**, which is the mechanism behind Itô’s correction terms.

---

## Definition (quadratic variation)

Let \(X=\{X_t\}_{t\in[0,T]}\) be a real-valued process with continuous paths. For a partition
\[
\Pi = \{0=t_0<t_1<\cdots<t_n=T\},
\]
define
\[
Q(X,\Pi) := \sum_{k=1}^n \left(X_{t_k}-X_{t_{k-1}}\right)^2.
\]
If as the mesh \(\|\Pi\|:=\max_k(t_k-t_{k-1})\to 0\) we have convergence in probability
\[
Q(X,\Pi)\xrightarrow{\mathbb{P}} [X]_T,
\]
then \([X]_T\) is called the **quadratic variation** of \(X\) over \([0,T]\). The process \([X]_t\) is defined similarly on \([0,t]\).

---

## Quadratic variation of Brownian motion

For standard Brownian motion \(\{W_t\}\),
\[
\boxed{
[W]_t = t \quad \text{for all } t\ge 0
}
\]
(with convergence in probability, and in fact in \(L^2\)).

Intuition: since increments satisfy \(\Delta W_k \sim \mathcal{N}(0,\Delta t_k)\), we expect \((\Delta W_k)^2\) to behave like \(\Delta t_k\), and summing yields \(t\).

---

## Finite variation vs quadratic variation

If \(A_t\) has finite variation on \([0,T]\), then
\[
\boxed{
[A]_T = 0.
}
\]
In particular, for smooth deterministic functions \(f(t)\),
\[
[f]_T=0.
\]
This sharply distinguishes Brownian motion from smooth paths: Brownian motion has nonzero quadratic variation.

---

## Covariation

For two real-valued continuous processes \(X,Y\), define the **quadratic covariation**
\[
[X,Y]_T := \lim_{\|\Pi\|\to 0}\sum_{k=1}^n (X_{t_k}-X_{t_{k-1}})(Y_{t_k}-Y_{t_{k-1}})
\]
when the limit exists in probability.

For a multidimensional Brownian motion \(W_t=(W_t^{1},\dots,W_t^{m})\),
\[
\boxed{
[W^{\alpha},W^{\beta}]_t = \delta^{\alpha\beta}t.
}
\]

---

## Key algebra (Itô table)

Quadratic variation is the rigorous content behind the heuristic rules:
\[
(\mathrm{d}t)^2=0,
\qquad
\mathrm{d}t\,\mathrm{d}W_t^{\alpha}=0,
\qquad
\mathrm{d}W_t^{\alpha}\,\mathrm{d}W_t^{\beta}=\delta^{\alpha\beta}\,\mathrm{d}t.
\]
These are shorthand for statements about covariation.

---

## Quadratic variation of Itô integrals

Let
\[
M_t := \int_0^t H_s\,\mathrm{d}W_s
\]
with \(H\) square-integrable and adapted. Then \(M\) is a continuous martingale and
\[
\boxed{
[M]_t = \int_0^t H_s^2\,\mathrm{d}s.
}
\]
More generally, for two integrals
\[
M_t := \int_0^t H_s^{\alpha}\,\mathrm{d}W_s^{\alpha},
\qquad
N_t := \int_0^t K_s^{\alpha}\,\mathrm{d}W_s^{\alpha},
\]
their covariation is
\[
\boxed{
[M,N]_t = \int_0^t H_s^{\alpha}K_s^{\alpha}\,\mathrm{d}s.
}
\]

---

## Why this matters for Itô’s formula

When expanding \(f(t,W_t)\) via a second-order Taylor approximation, a term involving \((\Delta W_k)^2\) survives in the limit because
\[
\sum_k (\Delta W_k)^2 \to t,
\]
whereas terms involving \((\Delta t_k)^2\) vanish. This is exactly why Itô’s formula has a second-derivative correction term.
