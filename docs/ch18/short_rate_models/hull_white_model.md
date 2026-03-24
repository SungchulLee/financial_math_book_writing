# The Hull-White Model

The **Hull-White model** (1990) extends Vasicek by introducing a time-dependent drift that enables **exact calibration to the initial yield curve**. This makes it the workhorse model for interest rate derivatives in practice.

!!! note "Detailed Treatment"
    This page provides an overview of the Hull-White model within the short-rate framework. For complete derivations, proofs, named function references, and Python implementations, see [§20 Hull-White Detailed](../../ch20/named_functions/named_functions_definition.md).

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

where $f(0, t) = -\frac{\partial}{\partial t} \log P(0, t)$ is the market instantaneous forward rate. See [§20 Short Rate](../../ch20/short_rate/short_rate_solution.md) for the full HJM-based derivation.

---

## Key Results

### Gaussian Distribution

The short rate $r_t$ conditional on $r_s$ is Gaussian with variance $v(s,t) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa(t-s)})$, identical to Vasicek.

### Affine Bond Prices

$$
P(t, T) = A(t, T) \exp(-B(t, T) \cdot r_t), \qquad B(t, T) = \frac{1 - e^{-\kappa(T-t)}}{\kappa}
$$

where $B(t,T)$ is identical to Vasicek. The function $A(t,T)$ incorporates market bond prices to ensure exact calibration. See [§20 Zero Bond Pricing](../../ch20/bond_pricing/bond_price_formula.md) for explicit formulas and proofs.

### Closed-Form Derivative Prices

The Hull-White model provides analytical formulas for European bond options, caplets/floorlets, and swaptions (via Jamshidian's trick). See:

- [§20 Zero Bond Options](../../ch20/bond_options/zero_coupon_bond_options.md) — bond option pricing under the $T$-forward measure
- [§20 Caplet and Floor Formula](../../ch20/derivatives_pricing/caplet_floorlet_formula.md) — caplet pricing as ZCB put options
- [§20 Swaption Formula](../../ch20/derivatives_pricing/swaption_formula.md) — Jamshidian decomposition and proof

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

**Two-factor Hull-White (G2++):** $r_t = x_t + y_t + \phi(t)$ where $x_t, y_t$ are correlated OU processes, enabling richer yield curve dynamics including twists and butterfly shifts. See [§20 Two-Factor Model](../../ch20/two_factor/two_factor_model_definition.md).

---

## Strengths and Limitations

**Strengths:** Exact curve fit by construction. Analytical tractability with closed-form bond and option prices. Industry standard with efficient calibration.

**Limitations:** Gaussian rates allow negative values. No volatility smile/skew. Single-factor model has limited curve dynamics. Time-inhomogeneous $\theta(t)$ must be stored.

---

## Further Reading

- Hull & White (1990), "Pricing Interest-Rate-Derivative Securities"
- Brigo & Mercurio, *Interest Rate Models*, Chapter 3
- Andersen & Piterbarg, *Interest Rate Modeling*, Volume 2

---

## Exercises

**Exercise 1.** Write the Hull-White SDE and identify each component. How does it differ from the Vasicek SDE? What specific role does the time-dependent function $\theta(t)$ play, and why can it not be replaced by a constant if exact yield curve fitting is required?

---

**Exercise 2.** The Hull-White drift function is given by $\theta(t) = f_t(0,t) + \kappa f(0,t) + \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})$, where $f(0,t)$ is the market instantaneous forward rate. For a flat forward rate curve $f(0,t) = 4\%$, compute $\theta(t)$ at $t = 0, 1, 5, 10$ with $\kappa = 0.05$ and $\sigma = 0.01$.

---

**Exercise 3.** Explain why the Hull-White model produces the same $B(\tau) = (1 - e^{-\kappa\tau})/\kappa$ as the Vasicek model, while the $A(t,T)$ function differs. What part of the bond pricing formula absorbs the time-dependent drift?

---

**Exercise 4.** A trader observes that the Hull-White model can generate negative rates. For $\kappa = 0.03$, $\sigma = 0.01$, and $r_0 = 0.5\%$, compute the conditional distribution of $r_5$ (the rate in 5 years) and find $\mathbb{P}(r_5 < 0)$. Is this probability negligible or material?

---

**Exercise 5.** Hull-White preserves the affine structure of Vasicek. Explain why this means that Jamshidian's decomposition applies for swaption pricing. How many zero-coupon bond options would appear in the Jamshidian decomposition of a 2Y-into-5Y annual payer swaption?

---

**Exercise 6.** Compare the calibration procedures for Hull-White and Black-Karasinski. Both use time-dependent drifts to fit the yield curve. Why can Hull-White extract $\theta(t)$ analytically while Black-Karasinski requires iterative tree-based calibration?

---

**Exercise 7.** The two-factor Hull-White (G2++) model uses $r_t = x_t + y_t + \phi(t)$ with two correlated OU processes. Explain what additional yield curve dynamics this enables compared to the one-factor model. Why might a single-factor Hull-White fail for pricing a 10Y Bermudan swaption even if it calibrates well to the swaption volatility matrix diagonal?
