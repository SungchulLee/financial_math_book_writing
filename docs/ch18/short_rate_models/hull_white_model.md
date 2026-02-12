# The Hull-White Model

The **Hull-White model** (1990) extends Vasicek by introducing a time-dependent drift that enables **exact calibration to the initial yield curve**. This makes it the workhorse model for interest rate derivatives in practice.

!!! note "Detailed Treatment"
    This page provides an overview of the Hull-White model within the short-rate framework. For complete derivations, proofs, named function references, and Python implementations, see [§17.9 Hull-White Detailed](../hull_white_detailed/named_functions.md).

---

## Model Specification

Under the risk-neutral measure $\mathbb{Q}$:

$$
dr_t = [\theta(t) - \kappa r_t] \, dt + \sigma \, dW_t^{\mathbb{Q}}
$$

or equivalently $dr_t = \kappa[\bar{\theta}(t) - r_t] \, dt + \sigma \, dW_t^{\mathbb{Q}}$ where $\bar{\theta}(t) = \theta(t)/\kappa$.

**Key difference from Vasicek:** The function $\theta(t)$ is time-dependent, chosen to match market data.

**Parameters:**

- $\kappa > 0$: mean-reversion speed (constant)
- $\theta(t)$: time-dependent drift function (calibrated)
- $\sigma > 0$: volatility (constant or time-dependent $\sigma(t)$)

---

## Exact Fit to the Initial Yield Curve

The model reprices all observed discount bonds exactly: $P^{\text{model}}(0, T) = P^{\text{market}}(0, T)$ for all $T$. This determines $\theta(t)$ uniquely:

$$
\boxed{\theta(t) = \frac{\partial f(0, t)}{\partial t} + \kappa f(0, t) + \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})}
$$

where $f(0, t) = -\frac{\partial}{\partial t} \log P(0, t)$ is the market instantaneous forward rate. See [§17.9 Short Rate](../hull_white_detailed/short_rate.md) for the full HJM-based derivation.

---

## Key Results

### Gaussian Distribution

The short rate $r_t$ conditional on $r_s$ is Gaussian with variance $v(s,t) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa(t-s)})$, identical to Vasicek.

### Affine Bond Prices

$$
P(t, T) = A(t, T) \exp(-B(t, T) \cdot r_t), \qquad B(t, T) = \frac{1 - e^{-\kappa(T-t)}}{\kappa}
$$

where $B(t,T)$ is identical to Vasicek. The function $A(t,T)$ incorporates market bond prices to ensure exact calibration. See [§17.9 Zero Bond Pricing](../hull_white_detailed/zero_bond_pricing.md) for explicit formulas and proofs.

### Closed-Form Derivative Prices

The Hull-White model provides analytical formulas for European bond options, caplets/floorlets, and swaptions (via Jamshidian's trick). See:

- [§17.9 Zero Bond Options](../hull_white_detailed/zero_bond_options.md) — bond option pricing under the $T$-forward measure
- [§17.9 Caplet and Floor Formula](../hull_white_detailed/caplet_formula.md) — caplet pricing as ZCB put options
- [§17.9 Swaption Formula](../hull_white_detailed/swaption_formula.md) — Jamshidian decomposition and proof

---

## Calibration

**Step 1 — Fit the initial curve:** Given market discount factors, compute $f(0,t)$ and $\theta(t)$. This is automatic once $\kappa$ and $\sigma$ are fixed.

**Step 2 — Calibrate to volatility instruments:** Fit $\kappa$ and $\sigma$ to cap and swaption implied volatilities:

$$
\min_{\kappa, \sigma} \sum_{i} w_i \left(\sigma^{\text{model}}_i(\kappa, \sigma) - \sigma^{\text{market}}_i\right)^2
$$

---

## Extensions

**Time-dependent volatility:** Allow $\sigma(t)$ to vary for additional flexibility in fitting the volatility term structure.

**Two-factor Hull-White (G2++):** $r_t = x_t + y_t + \phi(t)$ where $x_t, y_t$ are correlated OU processes, enabling richer yield curve dynamics including twists and butterfly shifts. See [§17.9 Two-Factor Model](../hull_white_detailed/two_factor_model.md).

---

## Strengths and Limitations

**Strengths:** Exact curve fit by construction. Analytical tractability with closed-form bond and option prices. Industry standard with efficient calibration.

**Limitations:** Gaussian rates allow negative values. No volatility smile/skew. Single-factor model has limited curve dynamics. Time-inhomogeneous $\theta(t)$ must be stored.

---

## Further Reading

- Hull & White (1990), "Pricing Interest-Rate-Derivative Securities"
- Brigo & Mercurio, *Interest Rate Models*, Chapter 3
- Andersen & Piterbarg, *Interest Rate Modeling*, Volume 2
