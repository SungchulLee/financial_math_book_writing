# Forward Consistency

**Forward consistency** aims to ensure that a model calibrated today remains internally consistent when viewed from tomorrow's perspective. It provides a theoretical framework for mitigating the recalibration problem by requiring that model dynamics and calibration be mutually compatible.

---

## Definition of forward consistency

### Informal statement

A model is forward consistent if:

1. Parameters calibrated at time $t$ to market data,
2. when evolved according to the model's own dynamics to time $t + \Delta t$,
3. generate prices consistent with what recalibration at $t + \Delta t$ would produce.

In other words, **recalibration should not contradict the model's implied evolution**.

### Formal definition

Let $\theta_t$ denote calibrated parameters at time $t$, and let $\Phi_{t \to t+\Delta t}(\theta_t, \omega)$ denote the model-implied parameter evolution (possibly stochastic, depending on path $\omega$).

A model is **forward consistent** if, for typical market realizations:

$$
\hat{\theta}_{t+\Delta t}^{\text{calib}} \approx \Phi_{t \to t+\Delta t}(\hat{\theta}_t, \omega)
$$

where $\hat{\theta}_{t+\Delta t}^{\text{calib}}$ is the result of fresh calibration at $t + \Delta t$.

### Why this matters

If forward consistency fails:

- The model provides no guidance on how to evolve positions.
- Hedging becomes path-dependent in unmodeled ways.
- P&L attribution breaks down.
- Exotics with future calibration dates (e.g., cliquets) are inconsistently priced.

---

## Forward consistency in interest-rate models

Recall (see [§ HJM forward rates](../../ch19/hjm/forward_rate_dynamics.md)) the dynamics $df(t,T) = \alpha(t,T)\,dt + \sigma(t,T)\,dW_t$ and the no-arbitrage drift $\alpha(t,T) = \sigma(t,T)\int_t^T \sigma(t,u)\,du$. HJM is the canonical forward-consistent framework: the entire forward curve $f(t,\cdot)$ is the state variable, so "calibration" reduces to observing today's curve and the model itself specifies how it evolves. Only the volatility structure $\sigma(t,T)$ remains to be recalibrated, and even that is typically restricted (Hull--White, Gaussian HJM).

---

## Challenges in equity and volatility models

Equity volatility models typically have different structure:

### Low-dimensional parameterization

Models like Heston use a small number of parameters ($\kappa$, $\bar{v}$, $\sigma_v$, $\rho$, $v_0$) to generate an entire implied volatility surface. This is convenient but creates a mismatch:

- The parameter space is $\mathbb{R}^5$.
- The implied vol surface is (effectively) infinite-dimensional.
- A 5-parameter model cannot capture arbitrary surface dynamics.

### The calibration-dynamics gap

In Heston, the variance process follows:

$$
dv_t = \kappa(\bar{v} - v_t) \, dt + \sigma_v \sqrt{v_t} \, dW_t^v
$$

The model specifies how $v_t$ evolves, but not how $(\kappa, \bar{v}, \sigma_v, \rho)$ evolve. When we recalibrate:

- $\hat{v}_0^{\text{new}}$ from calibration may differ from $v_{\Delta t}$ evolved under the model.
- $\hat{\kappa}^{\text{new}}$, $\hat{\bar{v}}^{\text{new}}$ are treated as constants but are re-estimated.

This violates forward consistency.

### Result: recalibration is necessary

Unlike HJM, equity vol models cannot fit arbitrary surfaces. The model is misspecified, so recalibration compensates. Forward consistency is structurally violated.

---

## Approaches to restore consistency

Several frameworks attempt to reconcile calibration with dynamics.

### 1. State-extended models

Enlarge the state space to include variables that can track surface dynamics.

**Example: Bergomi's variance curve model**

Model the entire forward variance curve $\xi_t(T) = \mathbb{E}_t[v_T]$ as the state:

$$
d\xi_t(T) = \text{(drift)} \, dt + \eta(T - t) \xi_t(T) \, dW_t
$$

The forward variance curve is now a state variable, analogous to forward rates in HJM. Calibration becomes observing $\xi_t(\cdot)$ from option prices.

**Advantages:** Forward consistent by construction.

**Disadvantages:** Infinite-dimensional; requires choosing $\eta(\cdot)$; computational complexity.

### 2. Stochastic parameter models

Allow parameters to follow their own stochastic processes:

$$
d\theta_t = \mu_\theta(\theta_t) \, dt + \Sigma_\theta(\theta_t) \, dZ_t
$$

The parameter process $\theta_t$ is now part of the model. Calibration estimates the current state $\theta_t$, and the model specifies future evolution.

**Challenges:**

- What dynamics for $\theta$? Often ad-hoc.
- Identification: separating parameter uncertainty from parameter dynamics.
- Nested calibration: must calibrate both the base model and the parameter process.

### 3. Term-structure extensions

Extend scalar parameters to term structures:

- Instead of a single $\bar{v}$, use a forward long-run variance curve $\bar{v}(T)$.
- Instead of scalar $\rho$, use maturity-dependent correlation $\rho(T)$.

This increases flexibility to fit the surface and allows smoother recalibration.

### 4. Consistent recalibration (CRC) framework

The CRC framework (Björk, Landén, Svensson; Carmona, Nadtochiy) formalizes the requirement:

> **The calibration map and model dynamics must be consistent.**

Let $\mathcal{C}: \text{(market data)} \to \theta$ be the calibration map. Let $\Phi: \theta_t \to \theta_{t+\Delta t}$ be model-implied evolution. CRC requires:

$$
\mathcal{C}(\text{prices at } t + \Delta t) = \Phi(\mathcal{C}(\text{prices at } t), \omega)
$$

This is a strong constraint that typically cannot be satisfied by standard models. The CRC framework characterizes *which* models and calibration procedures are mutually consistent.

### 5. Market models for volatility

By analogy with LIBOR market models for rates, one can model tradeable volatility instruments (e.g., variance swaps, VIX futures) directly:

$$
d\text{VS}_t(T) = \text{VS}_t(T) \sigma_{\text{VS}}(t, T) \, dW_t
$$

This ensures that calibration to variance swap prices is consistent with modeled dynamics.

---

## Practical implications

### When forward consistency matters most

- **Cliquets and forward-starting options:** Pricing depends on future calibration.
- **Long-dated exotics:** Inconsistent recalibration accumulates over time.
- **Dynamic hedging of path-dependent options:** Hedge ratios depend on how parameters evolve.
- **Risk management:** Scenario analysis requires consistent future model states.

### When it matters less

- **Short-dated vanillas:** Calibrated daily; recalibration effects are small.
- **Static hedging:** No parameter evolution needed.
- **Relative value trades:** Inconsistencies may cancel across legs.

### Practical compromise

Full forward consistency is often unattainable. A pragmatic approach:

1. Use HJM-style models where possible (rates, variance curves).
2. For low-dimensional models, recalibrate slowly-changing parameters infrequently.
3. Use regularization to penalize parameter jumps.
4. Document model limitations; report parameter uncertainty.
5. Stress test pricing under alternative parameter paths.

---

## Forward consistency and model risk

Forward inconsistency is a form of model risk:

- The model does not fully describe the system.
- Unmodeled parameter dynamics introduce uncertainty.
- P&L explanations are incomplete.

Quantifying this risk requires:

- Estimating typical recalibration magnitude.
- Propagating parameter uncertainty to prices and Greeks.
- Scenario analysis with alternative parameter paths.

---

## Key takeaways

- Forward consistency links calibration across time.
- HJM-style models achieve consistency by modeling the full term structure.
- Low-dimensional equity/vol models are typically not forward consistent.
- Achieving consistency requires richer state dynamics (variance curves, stochastic parameters).
- The CRC framework provides a theoretical criterion for consistency.
- Forward inconsistency is a source of model risk that should be acknowledged and managed.

---

## Further reading

- Heath, Jarrow & Morton, "Bond Pricing and the Term Structure of Interest Rates" (1992).
- Björk & Christensen, "Interest Rate Dynamics and Consistent Forward Rate Curves" (1999).
- Carmona & Nadtochiy, "Local Volatility Dynamic Models" (2009).
- Bergomi, *Stochastic Volatility Modeling* (forward variance models).
- Filipović, *Term-Structure Models: A Graduate Course*.

---

## Exercises

**Exercise 1.** State the definition of forward consistency for a parameterized model. Then consider a simple model where option prices depend on a single parameter $\sigma$ (implied volatility). The model dynamics predict that $\sigma_{t+\Delta t} = \sigma_t + \mu\Delta t + \eta\sqrt{\Delta t}\,Z$ where $Z \sim N(0,1)$. If recalibration at $t + \Delta t$ yields $\hat{\sigma}_{t+\Delta t}$ that differs systematically from the model-predicted $\sigma_{t+\Delta t}$, explain what this implies about forward consistency.

??? success "Solution to Exercise 1"
    **Definition.** A parameterized model is forward consistent if the parameters obtained by fresh calibration at a future time $t + \Delta t$ agree (in distribution or approximately) with the parameters obtained by evolving the time-$t$ calibrated parameters according to the model's own dynamics. Formally, if $\hat{\theta}_t$ is the calibrated parameter at time $t$ and $\Phi_{t \to t+\Delta t}(\hat{\theta}_t, \omega)$ is the model-implied parameter at $t + \Delta t$ (given the realized market path $\omega$), then forward consistency requires

    $$
    \hat{\theta}_{t+\Delta t}^{\text{calib}} \approx \Phi_{t \to t+\Delta t}(\hat{\theta}_t, \omega)
    $$

    for typical market realizations.

    **Analysis of the given model.** The model specifies that implied volatility evolves as

    $$
    \sigma_{t+\Delta t} = \sigma_t + \mu\,\Delta t + \eta\sqrt{\Delta t}\,Z, \qquad Z \sim N(0,1)
    $$

    Starting from the calibrated value $\hat{\sigma}_t$, the model predicts that $\sigma_{t+\Delta t}$ has mean $\hat{\sigma}_t + \mu\,\Delta t$ and variance $\eta^2\,\Delta t$.

    If recalibration at $t + \Delta t$ yields $\hat{\sigma}_{t+\Delta t}$ that differs **systematically** from the model prediction (not just due to random noise), this constitutes a violation of forward consistency. Specifically:

    - If $\mathbb{E}[\hat{\sigma}_{t+\Delta t}^{\text{calib}} - \sigma_{t+\Delta t}^{\text{model}}] \ne 0$, there is a systematic bias. The drift $\mu$ in the model does not match the empirical drift of recalibrated parameters. This means the model's dynamics are misspecified.
    - If the variance of $\hat{\sigma}_{t+\Delta t}^{\text{calib}} - \sigma_{t+\Delta t}^{\text{model}}$ is much larger than can be explained by observation noise, the model fails to capture the true parameter dynamics.

    In either case, the model cannot be trusted to extrapolate forward: hedging strategies based on the model's predicted parameter evolution will systematically err, and products with forward-starting features (cliquets, forward-starting options) will be inconsistently priced across calibration dates.

---

**Exercise 2.** In the HJM framework, the no-arbitrage drift condition is $\alpha(t,T) = \sigma(t,T)\int_t^T \sigma(t,u)\,du$. Derive this condition starting from the requirement that discounted bond prices are martingales under the risk-neutral measure. Show each step of the derivation.

??? success "Solution to Exercise 2"
    **Setup.** In the HJM framework, the forward rate evolves as

    $$
    df(t, T) = \alpha(t, T)\,dt + \sigma(t, T)\,dW_t
    $$

    The price of a zero-coupon bond maturing at $T$ is

    $$
    P(t, T) = \exp\!\left(-\int_t^T f(t, u)\,du\right)
    $$

    **Step 1: Dynamics of the integrated forward rate.** Define $F(t, T) = \int_t^T f(t, u)\,du$. By Leibniz's rule and the dynamics of $f$:

    $$
    dF(t, T) = -f(t, t)\,dt + \int_t^T df(t, u)\,du = -r_t\,dt + \int_t^T \alpha(t, u)\,du\,dt + \int_t^T \sigma(t, u)\,du\,dW_t
    $$

    where $r_t = f(t, t)$ is the short rate.

    **Step 2: Dynamics of the bond price.** Since $P(t, T) = e^{-F(t, T)}$, applying Ito's formula:

    $$
    dP(t, T) = P(t, T)\!\left[-dF(t, T) + \tfrac{1}{2}(dF)^2\right]
    $$

    The quadratic variation is $(dF)^2 = \left(\int_t^T \sigma(t, u)\,du\right)^2 dt$. Define $\Sigma(t, T) = \int_t^T \sigma(t, u)\,du$. Then

    $$
    dP(t, T) = P(t, T)\!\left[\left(r_t - \int_t^T \alpha(t, u)\,du + \tfrac{1}{2}\Sigma(t, T)^2\right)dt - \Sigma(t, T)\,dW_t\right]
    $$

    **Step 3: Martingale condition.** Under the risk-neutral measure, the discounted bond price $\tilde{P}(t, T) = e^{-\int_0^t r_s\,ds}P(t, T)$ must be a martingale. This requires

    $$
    d\tilde{P}(t, T) = \tilde{P}(t, T)\!\left[\left(-\int_t^T \alpha(t, u)\,du + \tfrac{1}{2}\Sigma(t, T)^2\right)dt - \Sigma(t, T)\,dW_t\right]
    $$

    to have zero drift, so

    $$
    -\int_t^T \alpha(t, u)\,du + \tfrac{1}{2}\Sigma(t, T)^2 = 0
    $$

    **Step 4: Deriving the drift condition.** The above must hold for all $T$. Differentiating with respect to $T$:

    $$
    -\alpha(t, T) + \Sigma(t, T)\,\sigma(t, T) = 0
    $$

    since $\frac{\partial}{\partial T}\Sigma(t, T) = \sigma(t, T)$. Substituting $\Sigma(t, T) = \int_t^T \sigma(t, u)\,du$:

    $$
    \alpha(t, T) = \sigma(t, T)\int_t^T \sigma(t, u)\,du
    $$

    This is the HJM no-arbitrage drift condition. It uniquely determines the drift of forward rates in terms of the volatility structure, ensuring that no recalibration of the drift is needed once the volatility is specified.

---

**Exercise 3.** Consider the Heston model with parameters $(\kappa, \bar{v}, \sigma_v, \rho, v_0)$. Explain why the model is not forward consistent by constructing a concrete example: calibrate on day $t$ to obtain $\hat{v}_0 = 0.04$; evolve $v_t$ one day according to the CIR dynamics with $\kappa = 2$, $\bar{v} = 0.04$, $\sigma_v = 0.3$; then show that recalibration on day $t+1$ could yield $\hat{v}_0^{\text{new}} \ne v_{\Delta t}^{\text{model}}$.

??? success "Solution to Exercise 3"
    **Setup.** On day $t$, we calibrate the Heston model and obtain $\hat{v}_0 = 0.04$, $\kappa = 2$, $\bar{v} = 0.04$, $\sigma_v = 0.3$. The CIR dynamics for variance are

    $$
    dv_t = \kappa(\bar{v} - v_t)\,dt + \sigma_v\sqrt{v_t}\,dW_t^v
    $$

    **Model-predicted variance on day $t+1$.** The conditional expectation under CIR dynamics is

    $$
    \mathbb{E}[v_{t+\Delta t}] = \bar{v} + (v_0 - \bar{v})e^{-\kappa\,\Delta t}
    $$

    With $v_0 = \bar{v} = 0.04$, we get $\mathbb{E}[v_{t+\Delta t}] = 0.04$ regardless of $\kappa$ and $\Delta t$. The conditional standard deviation is

    $$
    \text{Std}(v_{t+\Delta t}) \approx \sigma_v\sqrt{v_0\,\Delta t} = 0.3\sqrt{0.04/252} \approx 0.3 \times 0.0126 \approx 0.00378
    $$

    So under the model, $v_{t+\Delta t}$ is approximately $0.04 \pm 0.0038$ (one standard deviation).

    **Recalibration on day $t+1$.** The market may have moved in a way not fully captured by the Heston model. Suppose the implied volatility surface steepened or the ATM level shifted. Fresh calibration to day-$(t+1)$ market data could yield $\hat{v}_0^{\text{new}} = 0.048$, which is roughly 2.1 standard deviations above the model-predicted mean. While not impossible, if such discrepancies occur systematically, it violates forward consistency.

    **Concrete inconsistency.** Even more telling: recalibration might also yield $\hat{\kappa}^{\text{new}} = 1.7$ and $\hat{\bar{v}}^{\text{new}} = 0.045$. The Heston model treats $(\kappa, \bar{v}, \sigma_v, \rho)$ as constants, so it provides no dynamics for them whatsoever. Yet recalibration produces different values, meaning

    $$
    \hat{\theta}_{t+1}^{\text{calib}} = (0.048,\; 1.7,\; 0.045,\; 0.3,\; -0.75) \ne \Phi_{t \to t+1}(\hat{\theta}_t) = (0.04,\; 2.0,\; 0.04,\; 0.3,\; -0.70)
    $$

    The model evolution $\Phi$ keeps $(\kappa, \bar{v}, \sigma_v, \rho)$ constant and evolves only $v_t$ via CIR, while recalibration changes all five parameters. This structural mismatch is the essence of forward inconsistency: the model dynamics and the calibration procedure produce contradictory parameter paths. The model does not "know" that $\kappa$ will change, yet in practice it does, because the Heston model is an imperfect representation of the true volatility dynamics.

---

**Exercise 4.** Bergomi's forward variance model specifies the dynamics of $\xi_t(T) = \mathbb{E}_t[v_T]$. Explain why this model is forward consistent by analogy with HJM. What plays the role of the forward rate curve? What is the analog of the HJM drift condition? What are the practical challenges of implementing this model?

??? success "Solution to Exercise 4"
    **Analogy with HJM.** In the HJM framework for interest rates, the entire forward rate curve $f(t, T)$ is the state variable. The model specifies how this infinite-dimensional object evolves, and "calibration" consists of observing the current forward curve from bond prices. There is no need to recalibrate the curve shape because it is a model output.

    **Bergomi's forward variance model.** In Bergomi's framework, the state variable is the forward variance curve $\xi_t(T) = \mathbb{E}_t[v_T]$ for $T \ge t$. The model specifies dynamics

    $$
    d\xi_t(T) = \lambda(t, T, \xi_t)\,dt + \eta(T - t)\,\xi_t(T)\,dW_t
    $$

    where $\eta(\cdot)$ is a volatility-of-variance function depending on time to maturity.

    **What plays the role of the forward rate curve?** The forward variance curve $\xi_t(\cdot)$ plays the role of the forward rate curve $f(t, \cdot)$. Just as forward rates determine bond prices, forward variances determine variance swap prices:

    $$
    \text{VS}_t(T) = \int_t^T \xi_t(u)\,du
    $$

    **The analog of the HJM drift condition.** In HJM, the no-arbitrage drift of forward rates is determined by the volatility: $\alpha(t, T) = \sigma(t, T)\int_t^T \sigma(t, u)\,du$. Similarly, in the forward variance model, requiring that variance swap prices (or their discounted values) satisfy no-arbitrage conditions determines the drift $\lambda(t, T, \xi_t)$ in terms of the volatility function $\eta$. The precise form depends on whether the variance swap is treated as a tradeable asset and on the specification of the risk premium.

    **Why the model is forward consistent.** At time $t$, the forward variance curve $\xi_t(\cdot)$ is observed (extracted from variance swap quotes or option prices). The model then specifies exactly how this curve evolves. At time $t + \Delta t$, the new curve $\xi_{t+\Delta t}(\cdot)$ is a model output, not the result of an ad-hoc recalibration. There is no gap between calibration and dynamics because the calibrated object (the full curve) is the state variable.

    **Practical challenges:**

    - **Infinite dimensionality.** The state is a function $\xi_t(\cdot)$, requiring discretization (finitely many maturity points). The number of state variables can be large.
    - **Choice of $\eta(\cdot)$.** The volatility-of-variance function must be specified and potentially recalibrated. This introduces a secondary calibration problem.
    - **Computational cost.** Pricing exotics under the forward variance model typically requires Monte Carlo simulation of the entire curve, which is expensive.
    - **Limited market data.** Variance swap quotes may be available only for a few maturities, requiring interpolation.
    - **Non-negativity.** Ensuring $\xi_t(T) > 0$ for all $T$ requires careful modeling (e.g., lognormal specification as above).

---

**Exercise 5.** In the Consistent Recalibration (CRC) framework, the requirement is $\mathcal{C}(\text{prices at }t+\Delta t) = \Phi(\mathcal{C}(\text{prices at }t), \omega)$. Consider a model with two parameters $(\sigma, \rho)$ and a calibration map $\mathcal{C}$ that extracts these from ATM implied volatility and 25-delta skew. Write down the CRC condition explicitly. Explain why most standard models fail to satisfy it, and what additional structure (e.g., stochastic parameters) is needed.

??? success "Solution to Exercise 5"
    **Explicit CRC condition.** Let $\theta = (\sigma, \rho)$ be the model parameters, and let the calibration map $\mathcal{C}$ extract them from two market observables:

    - $\sigma = \mathcal{C}_1(\sigma_{\text{ATM}})$: the ATM implied volatility determines $\sigma$.
    - $\rho = \mathcal{C}_2(\text{skew}_{25\delta})$: the 25-delta skew determines $\rho$.

    Let $\Phi_{t \to t+\Delta t}$ denote the model-implied evolution of $(\sigma, \rho)$ over one time step. The CRC condition states

    $$
    \begin{pmatrix} \mathcal{C}_1(\sigma_{\text{ATM}}(t+\Delta t)) \\ \mathcal{C}_2(\text{skew}_{25\delta}(t+\Delta t)) \end{pmatrix} = \Phi_{t \to t+\Delta t}\!\left(\begin{pmatrix} \mathcal{C}_1(\sigma_{\text{ATM}}(t)) \\ \mathcal{C}_2(\text{skew}_{25\delta}(t)) \end{pmatrix}, \omega\right)
    $$

    In other words, extracting parameters from tomorrow's market data must yield the same result as evolving today's parameters using the model dynamics.

    **Why standard models fail.** In a standard stochastic volatility model (e.g., Heston), $(\sigma, \rho)$ are constants. The model provides no dynamics for them, so $\Phi$ is the identity:

    $$
    \Phi_{t \to t+\Delta t}(\sigma, \rho) = (\sigma, \rho)
    $$

    But the market observables $\sigma_{\text{ATM}}$ and $\text{skew}_{25\delta}$ change daily, so $\mathcal{C}$ applied to new data yields different $(\sigma, \rho)$. The CRC condition fails because the left-hand side varies while the right-hand side is constant.

    Even if we allow $(\sigma, \rho)$ to vary by treating them as state variables, the CRC condition requires that the model-implied joint dynamics of $(S_t, v_t, \sigma_t, \rho_t)$ produce implied volatility surfaces whose ATM level and 25-delta skew evolve in a manner consistent with $\mathcal{C}$. This is a stringent condition linking the calibration map (which involves option pricing, a nonlinear operation) with the state dynamics.

    **Additional structure needed.** To satisfy CRC, one needs:

    - **Stochastic parameter dynamics** $d\sigma_t = \mu_\sigma\,dt + \Sigma_\sigma\,dZ_t^\sigma$ and $d\rho_t = \mu_\rho\,dt + \Sigma_\rho\,dZ_t^\rho$ with drift and diffusion coefficients chosen so that the model-implied observables match the empirical dynamics of $\sigma_{\text{ATM}}$ and $\text{skew}_{25\delta}$.
    - **Consistency between pricing and dynamics:** The pricing function must be computed under the joint dynamics of all state variables including the stochastic parameters, and the resulting implied vol surface must be consistent with the calibration map $\mathcal{C}$.
    - In practice, this often requires an iterative or fixed-point approach: specify candidate dynamics, compute implied observables, check CRC, and adjust dynamics accordingly.

---

**Exercise 6.** A cliquet option pays the sum of capped monthly returns over one year. Explain why forward consistency is particularly important for pricing this product. If the model is not forward consistent, describe how the cliquet price might change between two consecutive calibration dates even when the underlying spot price is unchanged, and quantify the economic impact for a notional of \$10 million with a monthly cap of 3%.

??? success "Solution to Exercise 6"
    **Why forward consistency matters for cliquets.** A cliquet option pays the sum of capped monthly returns over one year:

    $$
    \text{Payoff} = \sum_{i=1}^{12} \min\!\left(\frac{S_{t_i} - S_{t_{i-1}}}{S_{t_{i-1}}},\; c\right)
    $$

    where $c = 0.03$ (3% monthly cap) and $t_i$ are monthly dates. Pricing this product requires the model to generate the joint distribution of all twelve monthly returns, which depends on the volatility surface at each future reset date.

    If the model is not forward consistent, the implied volatility surface at future dates $t_1, \ldots, t_{11}$ is not determined by the model's dynamics from today's calibration. Each forward-starting option embedded in the cliquet effectively depends on a future recalibration that the model cannot predict. This means:

    - The cliquet price depends on assumptions about future parameter evolution that are outside the model.
    - Two consecutive calibrations may produce materially different cliquet prices even without spot moves, because the recalibrated parameters imply different forward volatility surfaces.

    **Price change without spot moves.** Suppose on day $t$ the model is calibrated with parameters $\theta_t$, yielding a cliquet price $V_t$. On day $t+1$, the spot is unchanged but recalibration gives $\theta_{t+1} \ne \theta_t$ (e.g., the forward skew changes). The new cliquet price $V_{t+1}$ differs because:

    - The model-implied distribution of future monthly returns changes with $\theta$.
    - The cap $c = 3\%$ makes the payoff sensitive to the tails: higher forward vol increases the probability of hitting the cap, reducing the expected capped return; changes in skew affect the asymmetry.

    **Quantifying the economic impact.** For a notional of \$10 million and monthly cap of 3%, the maximum annual payoff is $12 \times 3\% = 36\%$ of notional, or \$3.6 million. A typical cliquet value might be 5--10% of notional (\$500,000--\$1,000,000).

    If recalibration shifts the forward volatility by, say, 1 vol point across maturities, the cliquet price can change by approximately 0.5--2% of notional (this is highly model-dependent). For \$10 million notional, this is \$50,000--\$200,000. Over multiple recalibration dates, these changes accumulate and create unexplained P&L.

    More precisely, if the forward ATM vol for month $i$ shifts by $\Delta\sigma_i$ and the cliquet vega per month is approximately $\nu_i$, the total price change is

    $$
    \Delta V \approx \sum_{i=1}^{12} \nu_i \,\Delta\sigma_i
    $$

    For a \$10 million cliquet with $\nu_i \approx$ \$15,000--\$30,000 per vol point per month, a 1 vol point shift across all months gives $\Delta V \approx$ \$180,000--\$360,000. This is economically significant and represents pure model risk from forward inconsistency.

---

**Exercise 7.** Compare three approaches to achieving forward consistency: (a) HJM-style infinite-dimensional state models, (b) stochastic parameter extensions, and (c) term-structure extensions of scalar parameters. For each approach, discuss: dimensionality of the state space, calibration complexity, computational cost for pricing, and suitability for equity volatility versus interest rate modeling.

??? success "Solution to Exercise 7"
    **(a) HJM-style infinite-dimensional state models.**

    - **Dimensionality:** Infinite (the full forward curve or forward variance curve). In practice, discretized to $N_T$ maturity points, giving a state dimension of $N_T$ (typically 10--50).
    - **Calibration complexity:** Calibration reduces to observing the current forward curve from market data (bond prices, variance swaps). This is an interpolation/smoothing problem rather than an optimization problem, making it relatively straightforward.
    - **Computational cost for pricing:** High. Monte Carlo simulation must evolve the entire curve, and pricing path-dependent exotics requires simulating $N_T$-dimensional dynamics at each time step. Pricing a single exotic may take seconds to minutes.
    - **Suitability:** Naturally suited for **interest rate modeling**, where the forward rate curve is directly observable from liquid bond and swap markets. For **equity volatility**, the analog (Bergomi's forward variance model) is less natural because forward variances are less directly observable and require extraction from option prices.

    **(b) Stochastic parameter extensions.**

    - **Dimensionality:** Low to moderate. The state includes the original model states plus the stochastic parameters. For example, Heston with stochastic $(\kappa, \bar{v}, \rho)$ has dimension $1 + 3 = 4$ (or more with the spot process).
    - **Calibration complexity:** High. Must jointly calibrate the base model parameters and the dynamics of the stochastic parameters (drift, diffusion, correlation with other factors). Identification is difficult: separating parameter uncertainty from parameter dynamics requires long time series.
    - **Computational cost for pricing:** Moderate to high. The augmented state increases the dimensionality of the pricing PDE or the number of factors in Monte Carlo. For a 2-factor model becoming 5-factor, pricing cost may increase by an order of magnitude.
    - **Suitability:** Applicable to both equity and rates, but more commonly used in **equity volatility** where the number of base parameters is small. For rates, the HJM approach is more natural.

    **(c) Term-structure extensions of scalar parameters.**

    - **Dimensionality:** Moderate. Each scalar parameter is replaced by a term-structure function, discretized at $N_T$ points. For example, replacing $\bar{v}$ with $\bar{v}(T)$ at 10 maturities adds 9 dimensions.
    - **Calibration complexity:** Moderate. The additional degrees of freedom improve the fit to the observed surface, but the calibration problem has more parameters. Regularization (smoothness penalties) is typically needed.
    - **Computational cost for pricing:** Moderate. The pricing engine must handle maturity-dependent parameters, which slightly increases complexity but does not add stochastic factors. The dimensionality of the SDE system is unchanged.
    - **Suitability:** Most useful for **equity volatility models** where the implied vol surface has rich term-structure features that a single scalar parameter cannot capture. For interest rates, this approach is less common because HJM already provides a full term-structure framework. The main advantage is that it improves calibration quality while remaining in a familiar low-dimensional framework, but it does not fully resolve forward consistency because the term-structure parameters themselves may need recalibration.
