# The Cox-Ingersoll-Ross (CIR) Model

The Cox-Ingersoll-Ross model (1985) is a mean-reverting short-rate model with **square-root volatility**. Unlike Vasicek, the CIR model can ensure non-negative interest rates under appropriate parameter conditions, while retaining analytical tractability.

---

## Model Specification

### Risk-Neutral Dynamics

Under the risk-neutral measure $\mathbb{Q}$, the short rate follows:

$$
dr_t = \kappa(\theta - r_t) \, dt + \sigma \sqrt{r_t} \, dW_t^{\mathbb{Q}}
$$

where:
- $\kappa > 0$: mean-reversion speed
- $\theta > 0$: long-run mean level
- $\sigma > 0$: volatility parameter
- $W_t^{\mathbb{Q}}$: standard Brownian motion under $\mathbb{Q}$

### Key Difference from Vasicek

| Feature | Vasicek | CIR |
|---------|---------|-----|
| Volatility | $\sigma$ (constant) | $\sigma\sqrt{r_t}$ (state-dependent) |
| Rate distribution | Gaussian | Non-central chi-squared |
| Negative rates | Possible | Prevented (under Feller condition) |

---

## The Feller Condition

### Statement

The **Feller condition** is:

$$
\boxed{2\kappa\theta \geq \sigma^2}
$$

### Boundary Behavior

The behavior at $r = 0$ depends on the Feller condition:

| Condition | Behavior at $r = 0$ |
|-----------|---------------------|
| $2\kappa\theta \geq \sigma^2$ | $r = 0$ is **inaccessible**; rates stay strictly positive |
| $2\kappa\theta < \sigma^2$ | $r = 0$ is **attainable** but instantaneously reflecting |

In both cases, $r_t \geq 0$ for all $t$.

### Intuition

- The drift $\kappa(\theta - r_t)$ pushes $r_t$ toward $\theta > 0$
- Near $r = 0$, volatility $\sigma\sqrt{r_t}$ becomes small
- The Feller condition ensures the drift dominates near zero

---

## Distribution of $r_t$

### Transition Density

Given $r_s$ at time $s < t$, the distribution of $r_t$ is:

$$
r_t \mid r_s \sim \frac{c}{2} \chi^2\left(\nu, \lambda\right)
$$

where:
- $c = \frac{4\kappa}{\sigma^2(1 - e^{-\kappa(t-s)})}$
- $\nu = \frac{4\kappa\theta}{\sigma^2}$ (degrees of freedom)
- $\lambda = c \cdot r_s e^{-\kappa(t-s)}$ (non-centrality parameter)
- $\chi^2(\nu, \lambda)$ is the **non-central chi-squared** distribution

### Moments

**Mean:**

$$
\mathbb{E}[r_t \mid r_s] = r_s e^{-\kappa(t-s)} + \theta(1 - e^{-\kappa(t-s)})
$$

This is identical to Vasicek!

**Variance:**

$$
\text{Var}(r_t \mid r_s) = r_s \frac{\sigma^2}{\kappa}(e^{-\kappa(t-s)} - e^{-2\kappa(t-s)}) + \frac{\theta\sigma^2}{2\kappa}(1 - e^{-\kappa(t-s)})^2
$$

Unlike Vasicek, variance depends on the current rate $r_s$.

### Stationary Distribution

As $t \to \infty$:

$$
r_\infty \sim \text{Gamma}\left(\frac{2\kappa\theta}{\sigma^2}, \frac{2\kappa}{\sigma^2}\right)
$$

with mean $\theta$ and variance $\frac{\theta\sigma^2}{2\kappa}$.

---

## Zero-Coupon Bond Pricing

### Affine Structure

Like Vasicek, CIR yields **exponential-affine** bond prices:

$$
\boxed{P(t, T) = A(\tau) \exp(-B(\tau) \cdot r_t)}
$$

where $\tau = T - t$.

### Key Parameter

Define:

$$
\gamma = \sqrt{\kappa^2 + 2\sigma^2}
$$

### Solution for $B(\tau)$

$$
\boxed{B(\tau) = \frac{2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}}
$$

### Solution for $A(\tau)$

$$
\boxed{A(\tau) = \left[\frac{2\gamma \exp\left(\frac{(\kappa + \gamma)\tau}{2}\right)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}\right]^{2\kappa\theta/\sigma^2}}
$$

### Derivation Outline

The bond pricing PDE is:

$$
\frac{\partial P}{\partial t} + \kappa(\theta - r)\frac{\partial P}{\partial r} + \frac{1}{2}\sigma^2 r \frac{\partial^2 P}{\partial r^2} = rP
$$

Using ansatz $P = A(\tau) e^{-B(\tau)r}$ leads to:
- Riccati ODE for $B(\tau)$: $B' = 1 - \kappa B - \frac{1}{2}\sigma^2 B^2$
- Linear ODE for $\log A$: $(\log A)' = \kappa\theta B$

---

## Yield Curve Analysis

### Zero Rate

$$
z(t, T) = -\frac{\log P(t, T)}{\tau} = \frac{B(\tau)}{\tau} r_t - \frac{\log A(\tau)}{\tau}
$$

### Long-Term Yield

As $\tau \to \infty$:

$$
z_\infty = \frac{2\kappa\theta}{\gamma + \kappa}
$$

---

## Option Pricing

### Bond Options

A European call on a $T_2$-bond with strike $K$, expiring at $T_1$, has price involving the non-central chi-squared distribution:

$$
C = P(0, T_2) \cdot \chi^2_{2r^*(\phi + \psi + B)}(\nu, \lambda_1) - K P(0, T_1) \cdot \chi^2_{2r^*(\phi + \psi)}(\nu, \lambda_2)
$$

where the parameters are functions of model inputs and $r^*$ solves $P(T_1, T_2, r^*) = K$.

---

## Comparison: CIR vs. Vasicek

| Aspect | Vasicek | CIR |
|--------|---------|-----|
| SDE | $dr = \kappa(\theta-r)dt + \sigma dW$ | $dr = \kappa(\theta-r)dt + \sigma\sqrt{r}dW$ |
| Distribution | Gaussian | Non-central $\chi^2$ |
| Negative rates | Possible | No (if Feller holds) |
| $B(\tau)$ | $\frac{1-e^{-\kappa\tau}}{\kappa}$ | $\frac{2(e^{\gamma\tau}-1)}{(\gamma+\kappa)(e^{\gamma\tau}-1)+2\gamma}$ |
| Option pricing | Gaussian formulas | Non-central $\chi^2$ |
| Tractability | Very high | High |

---

## Strengths and Limitations

### Strengths

- **Non-negativity:** Rates remain non-negative (under Feller)
- **Analytical tractability:** Closed-form bond prices
- **Realistic volatility:** State-dependent volatility
- **Affine structure:** Efficient computation

### Limitations

- **Single factor:** Limited yield curve dynamics
- **Cannot fit arbitrary curves:** Pure CIR needs extension
- **Feller condition:** May be binding in low-rate environments

---

## Key Takeaways

- CIR: $dr_t = \kappa(\theta - r_t)dt + \sigma\sqrt{r_t}dW_t$
- Feller condition $2\kappa\theta \geq \sigma^2$ ensures $r_t > 0$
- Distribution is non-central chi-squared
- Bond prices: $P = A(\tau)e^{-B(\tau)r}$ with $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$

---

## Further Reading

- Cox, Ingersoll & Ross (1985), "A Theory of the Term Structure of Interest Rates"
- Brigo & Mercurio, *Interest Rate Models*, Chapter 3
