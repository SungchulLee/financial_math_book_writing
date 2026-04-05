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

??? success "Solution to Exercise 1"
    **Computing ATM vols using the backbone.** The SABR backbone gives $\sigma_{\text{ATM}} \approx \alpha / F^{1-\beta}$. With $\beta = 0.5$ and $\alpha = 0.025$:

    At $F = 0.03$:

    $$
    \sigma_{\text{ATM}}(0.03) = \frac{0.025}{(0.03)^{0.5}} = \frac{0.025}{0.17321} = 0.14434 = 14.43\%
    $$

    At $F = 0.025$:

    $$
    \sigma_{\text{ATM}}(0.025) = \frac{0.025}{(0.025)^{0.5}} = \frac{0.025}{0.15811} = 0.15811 = 15.81\%
    $$

    The ATM vol **increases** by approximately 138 bps when the forward drops from 3.0% to 2.5%. This is the sticky-backbone effect: a lower forward implies higher Black implied volatility through the $F^{-(1-\beta)}$ relationship.

    **Local volatility (sticky-strike) prediction.** Under a local volatility model, the implied volatility at each fixed strike $K$ is unchanged when the forward moves. The smile is "nailed" to the strike axis. When $F$ drops from 3.0% to 2.5%, the option that was ATM at $F = 3.0\%$ (strike $K = 3.0\%$) is now an OTM call. The new ATM option has strike $K = 2.5\%$.

    Under sticky-strike, the vol at $K = 2.5\%$ was read from the original smile at $F = 3.0\%$. If the original smile had positive skew (higher vol at lower strikes, typical for rates), the local volatility model assigns the vol at $K = 2.5\%$ from the original smile, which is higher than ATM vol at $F = 3.0\%$ but through a different mechanism. Critically, the sticky-strike model predicts that the **entire smile remains fixed** --- the vol at each strike does not change. The new ATM vol (at $K = 2.5\%$) is simply whatever the old smile assigned to that strike.

    In practice, when rates decrease, ATM implied volatility tends to increase (the so-called "rates-vol negative correlation"). The SABR backbone captures this directly through the $\alpha/F^{1-\beta}$ dependence. The local volatility model, by keeping vols fixed at each strike, fails to generate this dynamic response. SABR's sticky-backbone dynamics are therefore **more consistent with observed market behavior** in interest rate markets.

---

**Exercise 2.** The dynamic inconsistency of SABR arises because independently calibrated parameters at different expiries are not consistent with the model's own dynamics. Illustrate this: if the 1-year SABR gives $\alpha_1 = 0.025$ and the 2-year gives $\alpha_2 = 0.028$, but the SABR volatility process $\sigma_t = \alpha e^{-\nu^2 t/2 + \nu W_t}$ has $\mathbb{E}[\sigma_t] = \alpha$ (constant), explain the contradiction.

??? success "Solution to Exercise 2"
    The SABR volatility process is $\sigma_t = \alpha e^{-\nu^2 t/2 + \nu W_t}$, which is a geometric Brownian motion with drift $-\nu^2/2$ in the log. Therefore:

    $$
    \mathbb{E}[\sigma_t] = \alpha\,\mathbb{E}\!\left[e^{-\nu^2 t/2 + \nu W_t}\right] = \alpha\,e^{-\nu^2 t/2}\,e^{\nu^2 t/2} = \alpha
    $$

    So $\mathbb{E}[\sigma_t] = \alpha$ for all $t$. The expected volatility is constant over time.

    **The contradiction.** If the 1-year calibration gives $\alpha_1 = 0.025$ and the 2-year gives $\alpha_2 = 0.028$, these parameters are interpreted as the **initial volatility** $\sigma_0$ for their respective expiries. Within the SABR model, the volatility process started at $\alpha_1 = 0.025$ at time 0 has $\mathbb{E}[\sigma_t] = 0.025$ for all $t$. In particular, at $t = 1$, the expected volatility is still 0.025.

    For the 2-year option to be dynamically consistent, the SABR model used for the period $[1, 2]$ should use whatever volatility $\sigma_1$ was realized at $t = 1$ as its initial condition. The expected value of this initial condition is $\mathbb{E}[\sigma_1] = \alpha_1 = 0.025$. But the independently calibrated 2-year model starts with $\alpha_2 = 0.028 \neq 0.025$.

    This means the market-implied term structure of volatility ($\alpha$ increasing from 0.025 to 0.028) is inconsistent with the SABR model's prediction that the expected volatility remains constant. The model has no mechanism (such as mean reversion toward a higher long-run level, or a positive drift in $\sigma_t$) to explain why the initial volatility parameter should increase with maturity. This is the **dynamic inconsistency**: the independently calibrated parameters at different expiries cannot be reconciled with a single SABR process running from $t = 0$ to $t = 2$.

    Adding mean reversion $d\sigma_t = \kappa(\bar{\sigma} - \sigma_t)\,dt + \nu\sigma_t\,dW_t$ would allow $\mathbb{E}[\sigma_t]$ to evolve toward a long-run level $\bar{\sigma}$, potentially resolving the inconsistency at the cost of losing the Hagan closed-form approximation.

---

**Exercise 3.** A forward-starting swaption has a payoff that depends on the smile at a future date. Explain why the SABR dynamic inconsistency is particularly problematic for this product. If the trader uses today's SABR parameters to price a 1Y-forward-starting 5Y swaption, what error might result?

??? success "Solution to Exercise 3"
    A **forward-starting swaption** has its strike set at a future date $t_1$ (e.g., ATM forward at $t_1$), with the swaption then exercisable at $t_1 + T_{\text{opt}}$. Its value depends critically on the **conditional implied volatility smile** at time $t_1$.

    **Why dynamic inconsistency is problematic.** The forward-starting swaption payoff at $t_1$ is:

    $$
    V_{t_1} = \text{Swaption}(S_{t_1}, K = S_{t_1}, T_{\text{opt}}, \text{smile at } t_1)
    $$

    This requires knowing the smile for an option of maturity $T_{\text{opt}}$ at the future date $t_1$. Under SABR, the conditional smile at $t_1$ is determined by:

    1. The realized forward $F_{t_1}$
    2. The realized volatility $\sigma_{t_1}$ (both stochastic)

    The SABR model predicts a specific joint distribution of $(F_{t_1}, \sigma_{t_1})$ and thus a specific distribution of conditional smiles. However, the market also implies a smile for the $T_{\text{opt}}$-maturity option at future date $t_1$ (embedded in the prices of forward-starting options). Because the SABR parameters at the two expiries ($t_1$ and $t_1 + T_{\text{opt}}$) are calibrated independently, the model's predicted conditional smile generally **does not match** the market-implied forward smile.

    **Specific error from using today's parameters.** If the trader prices a 1Y-forward-starting 5Y swaption using today's SABR parameters for the 5Y expiry, the errors include:

    - The initial volatility $\alpha$ used at $t_1$ will be today's 5Y $\alpha$, not the $\alpha$ consistent with the 1Y SABR dynamics having evolved from today's state. Since $\mathbb{E}[\sigma_1] = \alpha_{\text{1Y}}$ but the 5Y calibration may use a different $\alpha_{\text{5Y}}$, the level of the forward smile is wrong.
    - The vol-of-vol $\nu$ and correlation $\rho$ at $t_1$ should reflect the conditional distribution after 1 year of stochastic evolution, but using today's 5Y parameters ignores this conditioning.
    - The net effect is typically a **mispricing of the smile convexity** at the forward date, leading to errors in the valuation of the ATM forward-starting option that can be 1--5 vega, depending on the degree of inconsistency between the 1Y and 5Y calibrations.

---

**Exercise 4.** One approach to managing the forward smile is time-dependent SABR parameters: $\alpha(T)$, $\rho(T)$, $\nu(T)$. If $\alpha(T)$ is piecewise constant between calibration expiries, the model matches each expiry's smile exactly. Explain the trade-off: what is gained (consistency) and what is lost (simplicity, uniqueness of hedge ratios) compared to independent per-expiry calibration?

??? success "Solution to Exercise 4"
    **What is gained with time-dependent parameters:**

    - **Exact calibration at each expiry:** With piecewise-constant $\alpha(t)$, $\rho(t)$, $\nu(t)$ between calibration dates $T_0 < T_1 < \cdots < T_n$, the model fits each expiry's smile exactly. This eliminates the static calibration error that would arise from using a single set of parameters.
    - **Internal dynamic consistency:** The model now describes a single stochastic process $(F_t, \sigma_t)$ with time-varying coefficients, so the conditional distributions at intermediate times are well-defined and consistent with the calibrated marginal distributions at each $T_i$. Forward-starting options and compound options are priced consistently with the calibrated vanilla smiles.
    - **Meaningful forward smiles:** The conditional smile at a future date $t_1$ is determined by the dynamics between $t_1$ and $T$, using the parameters for that time period. This is internally consistent, unlike independent per-expiry calibration.

    **What is lost:**

    - **Analytical tractability:** The Hagan formula assumes constant parameters over $[0, T]$. With time-dependent parameters, the formula no longer applies directly. One must use either numerical integration (averaging over the piecewise-constant parameter values), PDE methods, or Monte Carlo simulation, all of which are slower.
    - **Simplicity of implementation:** A single SABR calibration per expiry is straightforward. Time-dependent parameters require a global calibration across all expiries simultaneously, with constraints ensuring smooth or monotone parameter profiles.
    - **Non-uniqueness of hedge ratios:** With independent per-expiry calibration, delta and vega at each expiry depend only on that expiry's parameters. With time-dependent parameters, a change in the smile at one expiry can affect the calibrated parameters for other time periods, creating **cross-expiry sensitivities** that complicate hedging. The hedge ratios depend on which parameters are bumped and how the recalibration propagates, leading to non-unique delta and vega definitions.
    - **Over-parameterization risk:** With three parameters per time interval, the model may have more degrees of freedom than the market data can constrain, leading to instability in calibration.

    The trade-off is therefore: **dynamic consistency and forward smile accuracy** at the cost of **analytical tractability, implementation simplicity, and hedge ratio uniqueness**.

---

**Exercise 5.** Compare sticky-strike, sticky-delta, and sticky-backbone (SABR) smile dynamics. If $F$ drops by 50 bps from 3%: (a) under sticky-strike, what happens to the vol at $K = 2.5\%$? (b) under sticky-delta, how does the ATM vol change? (c) under SABR backbone, compute the new ATM vol for $\beta = 0.5$, $\alpha = 0.025$. Which model best matches the empirical behavior of interest rate smiles?

??? success "Solution to Exercise 5"
    Starting from $F_0 = 3\% = 0.03$, after a 50 bps drop: $F_1 = 2.5\% = 0.025$.

    **(a) Sticky-strike (local volatility):** The implied volatility at each fixed strike is unchanged. The vol at $K = 2.5\%$ remains whatever it was before the move. In particular, the vol at the new ATM strike $K = 2.5\%$ was previously an OTM put strike. If the original smile had typical negative skew (higher vol at lower strikes), the new ATM vol is equal to the **old OTM put vol at $K = 2.5\%$**, which is higher than the old ATM vol. However, this is purely a mechanical consequence of reading a different point on the same (static) smile, not a genuine dynamic response. The smile itself has not moved.

    **(b) Sticky-delta (Black--Scholes with flat smile):** The ATM vol does not change because the flat smile translates rigidly with the forward. The implied volatility at any fixed moneyness (e.g., ATM, 25-delta) is the same before and after the move. Hence the ATM vol is unchanged.

    **(c) SABR backbone ($\beta = 0.5$, $\alpha = 0.025$):**

    Before the move:

    $$
    \sigma_{\text{ATM}}(F_0) = \frac{\alpha}{F_0^{1-\beta}} = \frac{0.025}{(0.03)^{0.5}} = \frac{0.025}{0.17321} = 14.43\%
    $$

    After the move:

    $$
    \sigma_{\text{ATM}}(F_1) = \frac{\alpha}{F_1^{1-\beta}} = \frac{0.025}{(0.025)^{0.5}} = \frac{0.025}{0.15811} = 15.81\%
    $$

    The ATM vol increases by approximately **138 bps** (from 14.43% to 15.81%).

    **Which model matches empirical behavior?** In interest rate markets, the empirical observation is that when rates decrease, ATM implied volatility increases --- there is a negative correlation between rates and their implied volatility. The SABR backbone model captures this behavior directly through the $\alpha/F^{1-\beta}$ mechanism. The sticky-delta model misses it entirely (no vol change). The sticky-strike model may partially capture it (if the original smile has the right shape) but through a static mechanism rather than a genuine dynamic response.

    The **SABR sticky-backbone** model best matches the empirical behavior of interest rate smiles, which is one of the primary reasons for its widespread adoption in rates markets.

---

**Exercise 6.** A Bermudan swaption allows exercise at multiple dates. Its price depends on the smile at each exercise date. Explain why independent per-expiry SABR calibration may be insufficient for Bermudan pricing, and what additional modeling features are needed to produce consistent smile evolution across exercise dates.

??? success "Solution to Exercise 6"
    A **Bermudan swaption** with exercise dates $T_1 < T_2 < \cdots < T_n$ requires, at each exercise date $T_i$, a comparison between the immediate exercise value and the continuation value. The continuation value depends on the **conditional distribution of the swap rate and its smile** at each subsequent exercise date $T_{i+1}, \ldots, T_n$.

    **Why independent per-expiry calibration is insufficient:**

    1. **No consistent state space evolution.** Independent calibration gives SABR parameters $(\alpha_i, \rho_i, \nu_i)$ for each co-terminal swaption expiry $T_i$. But these are parameters for separate, unconnected models. There is no single stochastic process $(F_t, \sigma_t)$ that generates all these smiles simultaneously. When computing the continuation value at $T_i$, one needs the conditional smile at $T_{i+1}$ given the state at $T_i$ --- and independent calibration provides no such conditional information.

    2. **Arbitrage between exercise dates.** If the smiles at adjacent exercise dates are not dynamically linked, the continuation values may be inconsistent with each other. For example, the model might simultaneously predict that early exercise is optimal (because the continuation value is low given one set of parameters) and that the option has high value at a later date (given a different set of parameters). This inconsistency can produce Bermudan prices that are not monotone in the number of exercise dates.

    3. **Incorrect early exercise boundary.** The early exercise decision is particularly sensitive to the smile dynamics because it depends on the expected future smile shape. If the model predicts a smile at $T_{i+1}$ that is inconsistent with the dynamics from $T_i$ to $T_{i+1}$, the early exercise boundary will be incorrectly located.

    **Additional modeling features needed:**

    - **Time-dependent SABR parameters** $\alpha(t)$, $\rho(t)$, $\nu(t)$ that are piecewise constant between exercise dates, calibrated globally to all co-terminal swaption smiles simultaneously. This ensures a single consistent process drives the evolution.
    - **Mean reversion in volatility** ($d\sigma_t = \kappa(\bar{\sigma} - \sigma_t)\,dt + \nu\sigma_t\,dW_t$) to connect the short-term and long-term smile behavior, ensuring that the conditional smile at $T_{i+1}$ given the state at $T_i$ is realistic.
    - **The SABR/LIBOR Market Model (LMM)** framework, where each forward rate has its own SABR dynamics with time-dependent parameters, and the correlations between forward rates are modeled explicitly. This is the industry standard for Bermudan swaption pricing in rates markets.
    - **Markov-functional models** as an alternative that directly specifies the mapping from a low-dimensional Markov state to the conditional smile at each exercise date, ensuring consistency by construction.
