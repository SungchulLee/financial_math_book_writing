# Time Reversal of Diffusions


Time reversal studies the law of a diffusion when observed backward in time.

Let \((X_t)_{0\le t\le T}\) solve

\[
\mathrm{d}X_t^{i} = b^{i}(t,X_t)\,\mathrm{d}t + \sigma^{i\alpha}(t,X_t)\,\mathrm{d}W_t^\alpha,
\qquad
a^{ij}(t,x)=\sigma^{i\alpha}(t,x)\sigma^{j\alpha}(t,x).
\]


Assume \(X_t\) admits a sufficiently smooth density \(p(t,x)\).

Define the reversed process

\[
\widetilde{X}_t := X_{T-t},\qquad 0\le t\le T.
\]



---

## Key Message: Score Correction


A central (formal) phenomenon is that the reversed drift involves the **score**

\[
\nabla \log p(t,x).
\]


In the simplest constant-diffusion case (constant \(a\)), a commonly used formula is

\[
\boxed{
\widetilde{b}(t,x)
=
-\,b(T-t,x)
+
a\,\nabla \log p(T-t,x),
}
\]


leading (in distribution) to

\[
\mathrm{d}\widetilde{X}_t = \widetilde{b}(t,\widetilde{X}_t)\,\mathrm{d}t + \sigma\,\mathrm{d}\widetilde{W}_t.
\]



Precise statements require careful regularity assumptions and filtration choices; the essential structural feature is the appearance of the score term.

---

## Reversible Stationary Case


If \(X_t\) is stationary with invariant measure \(\pi\) and **reversible** w.r.t. \(\pi\), then

\[
\boxed{
(X_t)_{0\le t\le T}\ \stackrel{d}{=}\ (X_{T-t})_{0\le t\le T}.
}
\]


In this case time reversal produces no new dynamics.

---

## What to Remember


- Time reversal typically introduces a correction term involving \(\nabla\log p\).
- Under detailed balance (reversibility), the process is symmetric in time.
