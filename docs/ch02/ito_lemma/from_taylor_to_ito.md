# From Taylor Expansion to Itô’s Formula


The fastest way to understand Itô’s formula is to view it as a **Taylor expansion where the second-order term does not vanish**. The “magic” is not magic at all—it is quadratic variation.

---

## Deterministic Reminder: Taylor Expansion


For a smooth function \(f\) and a small increment \(\Delta x\),

\[
f(x+\Delta x) - f(x)
= f'(x)\Delta x
+ \frac12 f''(x)(\Delta x)^2
+ o((\Delta x)^2).
\]

If \(x(t)\) is a smooth path, then \((\Delta x)^2\) is typically much smaller than \(\Delta x\), and in the limit only the first-order term survives. This is why the classical chain rule is first-order in nature.

---

## What Changes for Brownian Motion


Let \(W_t\) be Brownian motion. Over a small time step \(\Delta t\),

- \(\Delta W_t := W_{t+\Delta t}-W_t\) is typically of size \(\sqrt{\Delta t}\)
- hence \((\Delta W_t)^2\) is typically of size \(\Delta t\)

So unlike smooth paths, **the second-order term is not negligible**.

Heuristically,

\[
(\Delta W_t)^2 \approx \Delta t.
\]

This heuristic is made precise by quadratic variation:

\[
\sum_i (W_{t_{i+1}}-W_{t_i})^2 \longrightarrow t
\quad \text{(in probability)}.
\]

---

## The “Magic Box” Rules


In Itô calculus, we summarize the quadratic-variation behavior by the symbolic rules:

\[
(dW_t)^2 = dt,
\qquad
dW_t\,dt = 0,
\qquad
(dt)^2 = 0.
\]

These rules encode exactly which second-order terms survive in the limit.

---

## Heuristic Derivation of Itô’s Formula


Apply the second-order Taylor expansion to \(f(W_t)\):

\[
f(W_{t+\Delta t}) - f(W_t)
\approx f'(W_t)\Delta W_t
+ \frac12 f''(W_t)(\Delta W_t)^2.
\]

Summing over a partition and passing to the limit:

- the sum of \(f'(W_{t_i})\Delta W_i\) becomes the Itô integral \(\int_0^t f'(W_s)\,dW_s\)
- the sum of \(\frac12 f''(W_{t_i})(\Delta W_i)^2\) becomes \(\frac12\int_0^t f''(W_s)\,ds\)

This yields Itô’s formula in one dimension:

\[
\boxed{
df(W_t) = f'(W_t)\,dW_t + \frac12 f''(W_t)\,dt
}
\]

More generally, for \(f(t,x)\) with \(x=W_t\),

\[
\boxed{
df(t,W_t)
= f_t(t,W_t)\,dt
+ f_x(t,W_t)\,dW_t
+ \frac12 f_{xx}(t,W_t)\,dt.
}
\]

---

## Why This Is the Correct Intuition


- **Taylor expansion** explains why \(f_x\,dW_t\) appears.
- **Quadratic variation** explains why the extra drift \(\frac12 f_{xx}\,dt\) appears.
- The “Itô correction” is the honest second-order term that survives because Brownian motion is too rough.


