# Invariant Measures and Stationarity


Let \((X_t)_{t\ge 0}\) be a Markov process on \(\mathbb{R}^d\) with semigroup \((P_t)_{t\ge 0}\),

\[
P_t f(x) := \mathbb{E}^x[f(X_t)].
\]



---

## Invariant Measure


A probability measure \(\pi\) is **invariant** if for all bounded measurable \(f\) and all \(t\ge 0\),

\[
\boxed{
\int_{\mathbb{R}^d} P_t f(x)\,\pi(\mathrm{d}x)
=
\int_{\mathbb{R}^d} f(x)\,\pi(\mathrm{d}x).
}
\]


Equivalently, if \(X_0\sim \pi\) then \(X_t\sim \pi\) for all \(t\ge 0\).

---

## Stationarity


A process is **stationary** if its finite-dimensional distributions are invariant under time shifts; in particular,

\[
X_t \stackrel{d}{=} X_0\quad \text{for all }t\ge 0.
\]


Starting a Markov process from an invariant measure yields a stationary process.

---

## Generator Characterization


Let \(\mathcal{L}\) be the generator. Formally, invariance implies

\[
\boxed{
\int_{\mathbb{R}^d} (\mathcal{L}f)(x)\,\pi(\mathrm{d}x) = 0
}
\]


for a suitable class of test functions \(f\).

---

## Fokker–Planck (Adjoint) View


For a diffusion with drift \(b\) and diffusion matrix \(a=\sigma\sigma^\top\), a stationary density \(\pi(x)\) satisfies

\[
\boxed{
0
=
-\frac{\partial}{\partial x_i}\!\bigl(b^{i}(x)\pi(x)\bigr)
+
\frac{1}{2}\frac{\partial^2}{\partial x_i\partial x_j}\!\bigl(a^{ij}(x)\pi(x)\bigr),
}
\]


i.e. \(\mathcal{L}^\ast \pi = 0\).

---

## Reversibility (Detailed Balance)


A stationary process is **reversible** w.r.t. \(\pi\) if for all bounded measurable \(f,g\),

\[
\boxed{
\int f\,P_t g\,\mathrm{d}\pi
=
\int g\,P_t f\,\mathrm{d}\pi.
}
\]


Reversibility is stronger than invariance and connects directly to time reversal.

---

## Example: Gradient Diffusion


For

\[
\mathrm{d}X_t = -\nabla V(X_t)\,\mathrm{d}t + \sqrt{2}\,\mathrm{d}W_t,
\]


a natural invariant density is

\[
\boxed{
\pi(x) = Z^{-1}e^{-V(x)},\qquad Z=\int_{\mathbb{R}^d} e^{-V(x)}\,\mathrm{d}x.
}
\]



---

## What to Remember


- Invariance: \(\pi P_t = \pi\).
- Stationarity is obtained by starting from \(\pi\).
- Invariant densities solve \(\mathcal{L}^\ast \pi=0\).
