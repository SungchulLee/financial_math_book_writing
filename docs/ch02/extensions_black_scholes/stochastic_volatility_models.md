# Stochastic Volatility Models

Stochastic volatility introduces a second factor \(v_t\) (variance), capturing smile/skew dynamics and volatility clustering.

---

## 1. Generic Two-Factor Model

\[
\boxed{
\begin{aligned}
\mathrm{d}S_t &= rS_t\,\mathrm{d}t+\sqrt{v_t}S_t\,\mathrm{d}W_t^{(1)},\\
\mathrm{d}v_t &= \alpha(t,v_t)\,\mathrm{d}t+\beta(t,v_t)\,\mathrm{d}W_t^{(2)},\\
\mathrm{d}\langle W^{(1)},W^{(2)}\rangle_t &= \rho\,\mathrm{d}t.
\end{aligned}
}
\]

---

## 2. Heston Example

\[
\boxed{
\mathrm{d}v_t=\kappa(\theta-v_t)\,\mathrm{d}t+\xi\sqrt{v_t}\,\mathrm{d}W_t^{(2)}.
}
\]

---

## 3. Pricing PDE (2D)

For \(V(t,S,v)\), one obtains a two-dimensional parabolic PDE (with a mixed derivative term proportional to \(\rho\)).

---

## 4. Incompleteness

Two risk factors with one underlying typically implies market incompleteness; pricing depends on additional assumptions (volatility risk premium).

---

## 5. What to Remember

- Stochastic volatility improves smile dynamics.
- Pricing is higher-dimensional and often numerical/transform-based.
- Incompleteness is structural.
