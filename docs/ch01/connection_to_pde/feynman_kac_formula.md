Excellent! You've captured the essence of the generalization perfectly. Let me write this out with full mathematical detail.

---

## Kolmogorov Backward Equation as a Special Case

### Kolmogorov Backward (Expectation Version)

$$v(x, t) = \mathbb{E}[f(X_T) \mid X_t = x]$$

satisfies:

$$\frac{\partial v}{\partial t} + \mu(x,t)\frac{\partial v}{\partial x} + a(x,t)\frac{\partial^2 v}{\partial x^2} = 0$$

with terminal condition $v(x, T) = f(x)$.

**Integrand structure:** Only $f(X_T)$ at the fixed terminal time $T$.

---

## Feynman-Kac Formula: The Generalization

### General Form

$$v(x, t) = \mathbb{E}\left[\int_t^T e^{-\int_t^s r(X_u, u) \, du} g(X_s, s) \, ds + e^{-\int_t^T r(X_u, u) \, du} f(X_T) \,\bigg|\, X_t = x\right]$$

where the process $X_t$ follows:

$$dX_t = \mu(X_t, t) \, dt + \sigma(X_t, t) \, dW_t$$

This satisfies the **Feynman-Kac PDE:**

$$\boxed{\frac{\partial v}{\partial t} + \mu(x,t)\frac{\partial v}{\partial x} + a(x,t)\frac{\partial^2 v}{\partial x^2} - r(x,t)v + g(x,t) = 0}$$

with terminal condition $v(x, T) = f(x)$.

### Three Generalizations

As you correctly identified:

1. **Terminal payoff:** $f(X_T)$ 
   - Same as Kolmogorov backward equation
   - Value at fixed future time $T$

2. **Running payoff (dividend):** $\int_t^T e^{-\int_t^s r(X_u, u) du} g(X_s, s) \, ds$
   - **NEW:** Path-dependent accumulation of rewards/costs
   - Example: dividend payments, running costs, consumption

3. **Discounting (interest rate):** $e^{-\int_t^T r(X_u, u) du}$
   - **NEW:** Time value of money
   - Can be state-dependent: $r(X_t, t)$
   - Also interpreted as "killing rate" in probabilistic context

---

## Mathematical Breakdown

### The Expectation Integrand

$$\underbrace{e^{-\int_t^T r(X_u, u) du}}_{\text{discount factor}} \underbrace{f(X_T)}_{\text{terminal payoff}} + \int_t^T \underbrace{e^{-\int_t^s r(X_u, u) du}}_{\text{discount to time } s} \underbrace{g(X_s, s)}_{\text{flow payoff}} ds$$

**Kolmogorov backward is the case:** $r \equiv 0$ and $g \equiv 0$.

---

## Derivation Sketch of Feynman-Kac PDE

**Step 1:** Define the value function with time-to-maturity $\tau = T - t$:

$$v(x, \tau) = \mathbb{E}\left[\int_0^\tau e^{-\int_0^s r(X_u, T-\tau+u) du} g(X_s, T-\tau+s) ds + e^{-\int_0^\tau r(X_u, T-\tau+u) du} f(X_\tau) \,\bigg|\, X_0 = x\right]$$

**Step 2:** For small $h > 0$, by the law of iterated expectations:

$$v(x, \tau) = \mathbb{E}\left[e^{-\int_0^h r(X_u, T-\tau+u) du} g(X_h, T-\tau+h) h + e^{-\int_0^h r(X_u, T-\tau+u) du} v(X_h, \tau - h) \,\bigg|\, X_0 = x\right] + o(h)$$

**Step 3:** Expand to first order:

$$v(x, \tau) \approx \mathbb{E}[g(X_h, t) h + (1 - r(x,t)h)v(X_h, \tau - h) \mid X_0 = x] + o(h)$$

**Step 4:** Apply Itô's lemma to $v(X_h, \tau - h)$ and take expectations:

$$v(x, \tau) \approx g(x,t)h + (1-r(x,t)h)\left[v(x,\tau) - h\frac{\partial v}{\partial \tau} + h\mu(x,t)\frac{\partial v}{\partial x} + ha(x,t)\frac{\partial^2 v}{\partial x^2}\right] + o(h)$$

**Step 5:** Rearranging and dividing by $h$:

$$0 = g(x,t) - \frac{\partial v}{\partial \tau} + \mu(x,t)\frac{\partial v}{\partial x} + a(x,t)\frac{\partial^2 v}{\partial x^2} - r(x,t)v + \frac{o(h)}{h}$$

**Step 6:** Since $\frac{\partial v}{\partial t} = -\frac{\partial v}{\partial \tau}$, as $h \to 0$:

$$\boxed{\frac{\partial v}{\partial t} + \mu(x,t)\frac{\partial v}{\partial x} + a(x,t)\frac{\partial^2 v}{\partial x^2} - r(x,t)v + g(x,t) = 0}$$

---

## Comparison Table

| Component | Kolmogorov Backward | Feynman-Kac |
|-----------|-------------------|-------------|
| **Terminal payoff** | $f(X_T)$ | $e^{-\int_t^T r(X_u,u) du} f(X_T)$ |
| **Running payoff** | None | $\int_t^T e^{-\int_t^s r(X_u,u) du} g(X_s,s) ds$ |
| **Discount rate** | None ($r=0$) | $r(X_t, t)$ |
| **PDE** | $\frac{\partial v}{\partial t} + \mathcal{L}v = 0$ | $\frac{\partial v}{\partial t} + \mathcal{L}v - rv + g = 0$ |

where $\mathcal{L} = \mu(x,t)\frac{\partial}{\partial x} + a(x,t)\frac{\partial^2}{\partial x^2}$ is the infinitesimal generator.

---

## Financial Interpretation

In option pricing context:

- **$f(X_T)$:** Payoff at expiration (e.g., $(S_T - K)^+$ for a call option)
- **$g(X_s, s)$:** Dividend payments along the path
- **$r(X_s, s)$:** Risk-free interest rate (discounting cash flows)
- **$v(x, t)$:** Present value of the derivative at time $t$ when spot is $x$

The **Black-Scholes equation** is a special case of Feynman-Kac with constant $r$ and $g=0$:

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0$$

With dividends at rate $q$, we have $g(S,t) = -qS\frac{\partial V}{\partial S}$ (modifying the drift).

---

## Summary

You've stated it perfectly:

$$\boxed{\begin{align}
&\text{Kolmogorov Backward:} \\
&\qquad \mathbb{E}[f(X_T) \mid X_t = x] \\[10pt]
&\text{Feynman-Kac:} \\
&\qquad \mathbb{E}\left[\text{(discounted terminal payoff)} + \text{(discounted path integral)} \mid X_t = x\right]
\end{align}}$$

The Feynman-Kac formula is indeed the natural generalization that incorporates:
1. Terminal value at fixed future time $T$
2. Running rewards/costs accumulated along the path before $T$
3. Time value of money through discounting between $t$ and $T$