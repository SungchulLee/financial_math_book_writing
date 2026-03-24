# Managing the Forward Smile

A model's value for exotic products depends not only on whether it fits today's smile but on whether it generates the **correct smile dynamics** --- how the smile evolves as the underlying moves. The SABR model, with its explicit backbone and stochastic volatility, produces smile dynamics that are qualitatively superior to local volatility models: when the forward decreases, ATM implied volatility increases (for $\beta < 1$), matching the behavior observed in interest rate markets. However, the absence of mean reversion in the SABR volatility process creates a **dynamic inconsistency** between the model's predicted future smiles and the smiles actually observed in the market at later dates. This section analyzes the SABR smile dynamics, explains the dynamic inconsistency, and presents approaches for managing the forward smile in practice.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Explain how the SABR smile moves when the forward changes
    2. Contrast SABR smile dynamics with local volatility smile dynamics
    3. Identify the source of dynamic inconsistency in the SABR model
    4. Describe approaches for managing the forward smile (time-dependent parameters, recalibration)
    5. Analyze the impact on forward-starting and compound options

---

## Smile Dynamics Under SABR

### The Backbone Revisited

The ATM Black implied volatility in the SABR model depends on the forward through the backbone:

$$
\sigma_B^{\text{ATM}}(F) \approx \frac{\alpha}{F^{1-\beta}}
$$

When the forward moves from $F_0$ to a new level $F_1$, the model predicts:

$$
\frac{\sigma_B^{\text{ATM}}(F_1)}{\sigma_B^{\text{ATM}}(F_0)} \approx \left(\frac{F_0}{F_1}\right)^{1-\beta}
$$

For $\beta = 0.5$ and a 10% decrease in the forward ($F_1 = 0.9 F_0$):

$$
\frac{\sigma_B^{\text{ATM}}(F_1)}{\sigma_B^{\text{ATM}}(F_0)} \approx \left(\frac{1}{0.9}\right)^{0.5} \approx 1.054
$$

ATM vol increases by about 5.4%. This is the **sticky-backbone** behavior: the smile is anchored to the forward level through the $F^{1-\beta}$ term.

### Sticky-Strike vs. Sticky-Delta vs. Sticky-Backbone

Different models produce different smile dynamics, which are classified by their "stickiness":

**Sticky-strike** (local volatility): The implied volatility at a fixed strike $K$ does not change when the forward moves. The smile appears to be nailed to the strike axis. This means that when $F$ decreases, the ATM vol decreases (because we are now looking at a higher-strike option relative to ATM), which contradicts market behavior.

**Sticky-delta** (Black--Scholes): The implied volatility at a fixed moneyness (e.g., 25-delta put) does not change when the forward moves. The smile translates rigidly with the forward. This is the trivial case with a flat smile.

**Sticky-backbone** (SABR): The implied volatility at a fixed moneyness moves along the backbone as the forward changes. When $F$ decreases, the entire smile shifts upward. This matches the observed market behavior for interest rate options.

!!! info "Why Backbone Dynamics Matter"
    The difference between sticky-strike and sticky-backbone dynamics has a direct impact on **delta hedging**:

    - Under local volatility (sticky-strike): $\Delta_{\text{LV}} \approx \Delta_{\text{BS}}$
    - Under SABR (sticky-backbone): $\Delta_{\text{SABR}} < \Delta_{\text{BS}}$ for calls when $\beta < 1$

    The SABR delta is lower because it accounts for the increase in implied vol when $F$ decreases. Using the wrong dynamics leads to systematic hedging errors.

### Smile Shape Dynamics

When the forward moves, the SABR model predicts that:

1. **ATM level shifts**: via the backbone $\alpha / F^{1-\beta}$
2. **Skew changes**: the skew $\partial\sigma_B/\partial K|_{K=F}$ also depends on $F$ through the Hagan formula
3. **Curvature adjusts**: the smile curvature changes mildly with $F$

The dominant effect is the ATM level shift. The skew and curvature changes are second-order effects that become important for exotic products with forward-starting features.

---

## Dynamic Inconsistency

### The Problem

The SABR model is calibrated independently at each expiry $T$, producing a set of parameters $(\alpha(T), \rho(T), \nu(T))$. However, the SABR model itself has **no mechanism for connecting parameters across expiries**, because:

1. The volatility process has no mean reversion: $\sigma_t$ follows a martingale (geometric Brownian motion)
2. The model does not specify how $\alpha$ at one expiry relates to $\alpha$ at another

This creates a **dynamic inconsistency**: if we simulate the SABR process forward from $t = 0$ to some future time $t_1 < T$, the conditional distribution of $(F_{t_1}, \sigma_{t_1})$ does not, in general, match the SABR calibration at expiry $T - t_1$ for the forward starting at $F_{t_1}$.

### Consequences

The dynamic inconsistency affects:

**Forward-starting options**: An option whose strike is set at a future date $t_1$ (e.g., at the money forward at $t_1$) depends on the conditional smile at $t_1$. The SABR model predicts a specific conditional smile that may differ from what the market implies for expiry $T - t_1$ at that future date.

**Compound options**: Options on options (e.g., Bermudans) require the conditional smile at each exercise date. The SABR model's conditional smile differs from the separately calibrated smile at each date.

**CMS products**: CMS pricing involves expectations of swap rates under the wrong measure (the annuity measure), requiring the entire smile at each fixing date.

### Quantifying the Inconsistency

Consider the SABR model calibrated at expiries $T_1$ and $T_2$ with $T_1 < T_2$. The volatility process predicts:

$$
\text{Var}[\ln\sigma_{T_1}] = \nu^2 T_1
$$

If the model were dynamically consistent, the parameters at $T_2$ conditional on the state at $T_1$ would satisfy:

$$
\nu^2(T_2) \cdot T_2 = \nu^2(T_1) \cdot T_1 + \nu^2_{\text{forward}} \cdot (T_2 - T_1)
$$

In practice, the independently calibrated $\nu(T_1)$ and $\nu(T_2)$ do not satisfy this relationship, reflecting the model's inability to describe the term structure of smile dynamics.

---

## Approaches for Managing the Forward Smile

### Approach 1: Time-Dependent Parameters

Allow the SABR parameters to be piecewise-constant functions of time:

$$
\alpha(t) = \alpha_i, \quad \rho(t) = \rho_i, \quad \nu(t) = \nu_i \quad \text{for } t \in [T_{i-1}, T_i)
$$

The parameters are chosen so that the model reproduces the calibrated smiles at each expiry $T_i$. This approach is used in the **SABR/LIBOR Market Model** (Rebonato, McKay, and White, 2009), where each forward rate has its own time-dependent SABR parameters.

**Advantages**: Exact fit to each expiry's smile. Dynamic consistency within the model.

**Disadvantages**: The Hagan formula does not apply directly with time-dependent parameters (it assumes constant parameters). Numerical methods (MC, PDE) are required for pricing.

### Approach 2: Recalibration

The simplest approach: calibrate SABR independently at each expiry and do not attempt dynamic consistency. When pricing forward-starting options, use the SABR model at the relevant expiry with the calibrated parameters.

**Advantages**: Simple, fast, and standard industry practice for vanilla products.

**Disadvantages**: Ignores the dynamic inconsistency, which can lead to mispricing of forward-starting and compound options.

### Approach 3: Mean-Reverting Extensions

Add mean reversion to the volatility dynamics:

$$
d\sigma_t = \kappa(\bar{\sigma} - \sigma_t)\,dt + \nu\sigma_t\,dW_t^{(2)}
$$

This connects the short-term and long-term smile behavior, reducing the dynamic inconsistency. However, the Hagan formula no longer applies, and the main advantage of SABR (analytic tractability) is lost.

### Approach 4: Interpolation in SABR Parameters

Interpolate the calibrated parameters $(\alpha(T), \rho(T), \nu(T))$ smoothly across expiries using splines or other interpolation methods. This provides a consistent parameter surface without enforcing dynamic consistency.

**Common interpolation choices:**

- $\alpha(T)$: Interpolate $\alpha^2 T$ linearly in $T$ (ensures consistent total variance)
- $\rho(T)$: Interpolate directly (typically varies slowly)
- $\nu(T)$: Interpolate $\nu^2 T$ linearly (consistent vol-of-vol scaling)

---

## Impact on Exotic Products

### Forward-Starting Swaptions

A forward-starting swaption with fixing date $t_1$ and expiry $T$ has payoff determined by the swap rate $S_{t_1}$ at $t_1$ and the swaption value at $t_1$. The pricing requires the conditional smile at $t_1$.

Under SABR, the forward smile at $t_1$ is computed by:

1. Simulating $(F_{t_1}, \sigma_{t_1})$ from the SABR dynamics
2. At each simulated state, computing the SABR smile for the residual maturity $T - t_1$ with the simulated $\sigma_{t_1}$ as the initial volatility

This produces a model-implied forward smile that may differ from the market-implied forward smile.

### Bermudan Swaptions

Bermudan swaptions (with multiple exercise dates) require the conditional smile at each exercise date. The standard approach is:

1. Calibrate SABR independently at each exercise date
2. Price the Bermudan using a backward induction algorithm (e.g., Longstaff--Schwartz regression)
3. At each step, use the calibrated SABR smile to compute continuation values

This approach ignores dynamic consistency but is the market standard for Bermudan swaption pricing.

---

## Summary

The SABR model produces sticky-backbone smile dynamics, where ATM implied volatility moves inversely with the forward level through the $\alpha/F^{1-\beta}$ relationship. This qualitatively matches market behavior and is the primary advantage of SABR over local volatility models for hedging. However, the absence of mean reversion creates a dynamic inconsistency: independently calibrated parameters at different expiries are not consistent with the model's own dynamics. Practitioners manage this through time-dependent parameters, recalibration, parameter interpolation, or mean-reverting extensions. For vanilla products, independent per-expiry calibration is sufficient. For exotic products depending on the forward smile (forward-starting options, Bermudans, CMS), the dynamic inconsistency must be addressed explicitly.

---

## Further Reading

- Hagan, P. et al. (2002). *Managing smile risk*. Wilmott Magazine, 1, 84--108.
- Rebonato, R., McKay, K., & White, R. (2009). *The SABR/LIBOR Market Model*. Wiley.
- Piterbarg, V. (2005). *Stochastic volatility model with time-dependent skew*. Applied Mathematical Finance.
- Andersen, L. & Piterbarg, V. (2010). *Interest Rate Modeling*, Volume II. Atlantic Financial Press, Chapters 15--16.

---

## Exercises

**Exercise 1.** The SABR backbone predicts that ATM vol changes as $\sigma_{\text{ATM}} \approx \alpha/F^{1-\beta}$. For $\beta = 0.5$ and $\alpha = 0.025$, compute $\sigma_{\text{ATM}}$ at $F = 0.03$ and $F = 0.025$. If a local volatility model predicts the ATM vol at $F = 0.025$ using the current smile (sticky strike), explain why its prediction differs from SABR's and which is more consistent with market behavior.

---

**Exercise 2.** The dynamic inconsistency of SABR arises because independently calibrated parameters at different expiries are not consistent with the model's own dynamics. Illustrate this: if the 1-year SABR gives $\alpha_1 = 0.025$ and the 2-year gives $\alpha_2 = 0.028$, but the SABR volatility process $\sigma_t = \alpha e^{-\nu^2 t/2 + \nu W_t}$ has $\mathbb{E}[\sigma_t] = \alpha$ (constant), explain the contradiction.

---

**Exercise 3.** A forward-starting swaption has a payoff that depends on the smile at a future date. Explain why the SABR dynamic inconsistency is particularly problematic for this product. If the trader uses today's SABR parameters to price a 1Y-forward-starting 5Y swaption, what error might result?

---

**Exercise 4.** One approach to managing the forward smile is time-dependent SABR parameters: $\alpha(T)$, $\rho(T)$, $\nu(T)$. If $\alpha(T)$ is piecewise constant between calibration expiries, the model matches each expiry's smile exactly. Explain the trade-off: what is gained (consistency) and what is lost (simplicity, uniqueness of hedge ratios) compared to independent per-expiry calibration?

---

**Exercise 5.** Compare sticky-strike, sticky-delta, and sticky-backbone (SABR) smile dynamics. If $F$ drops by 50 bps from 3%: (a) under sticky-strike, what happens to the vol at $K = 2.5\%$? (b) under sticky-delta, how does the ATM vol change? (c) under SABR backbone, compute the new ATM vol for $\beta = 0.5$, $\alpha = 0.025$. Which model best matches the empirical behavior of interest rate smiles?

---

**Exercise 6.** A Bermudan swaption allows exercise at multiple dates. Its price depends on the smile at each exercise date. Explain why independent per-expiry SABR calibration may be insufficient for Bermudan pricing, and what additional modeling features are needed to produce consistent smile evolution across exercise dates.
