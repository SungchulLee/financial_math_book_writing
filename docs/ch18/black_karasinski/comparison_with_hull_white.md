# Comparison with Hull-White

The Hull-White and Black-Karasinski models are the two most widely used one-factor short-rate models with time-dependent drift, both capable of fitting the initial term structure exactly. Yet they differ fundamentally in their mathematical structure and practical implications. Hull-White is affine, producing closed-form bond and option prices with normal rate distributions that allow negative rates. Black-Karasinski is non-affine, requiring numerical methods for all pricing, but guaranteeing positive rates through its log-normal structure. This section provides a systematic comparison along every dimension that matters in practice: dynamics, distributions, tractability, calibration, and suitability for different products.

---

## Side-by-side SDE comparison

### Hull-White model

$$
dr_t = [\theta^{HW}(t) - a\,r_t]\,dt + \sigma\,dW_t
$$

The short rate $r_t$ is the state variable directly. The drift is linear in $r_t$ and the volatility is constant.

### Black-Karasinski model

$$
d(\ln r_t) = [\theta^{BK}(t) - a\,\ln r_t]\,dt + \sigma\,dW_t
$$

The log rate $x_t = \ln r_t$ is the state variable. The drift is linear in $x_t$ and the volatility is constant in the log domain.

### Unified view

Both models specify a mean-reverting OU process for a transformed state variable:

| | Hull-White | Black-Karasinski |
|---|---|---|
| **State variable** | $r_t$ | $x_t = \ln r_t$ |
| **SDE** | $dr = [\theta(t) - ar]\,dt + \sigma\,dW$ | $dx = [\theta(t) - ax]\,dt + \sigma\,dW$ |
| **Transformation to rate** | $r_t = r_t$ (identity) | $r_t = e^{x_t}$ |
| **Rate volatility** | $\sigma$ (constant) | $\sigma r_t$ (proportional to level) |

---

## Rate distribution

### Hull-White: normal rates

Given $r_s$, the rate at a future time $t > s$ is

$$
r_t \mid r_s \sim \mathcal{N}\!\left(\mu_{HW}(s,t),\;\frac{\sigma^2}{2a}(1 - e^{-2a(t-s)})\right)
$$

**Key properties**:

- Symmetric distribution around the conditional mean
- Non-zero probability of negative rates: $\mathbb{P}(r_t < 0) > 0$
- Light tails (Gaussian decay)

### Black-Karasinski: log-normal rates

Given $r_s$, the rate at time $t$ satisfies $\ln r_t \sim \mathcal{N}(\mu_{BK}(s,t), \nu^2(s,t))$, so

$$
r_t \mid r_s \sim \text{LogNormal}\!\left(\mu_{BK}(s,t),\;\nu^2(s,t)\right)
$$

**Key properties**:

- Right-skewed distribution
- Strictly positive: $\mathbb{P}(r_t < 0) = 0$
- Heavier right tail than normal

!!! note "Negative rates in practice"
    European and Japanese government bond yields were negative for extended periods (2014--2022). Hull-White naturally accommodates this. Black-Karasinski cannot produce negative rates, requiring model modifications (shifted BK) or different model selection for negative-rate environments.

---

## Analytical tractability

This is the most consequential difference between the two models.

### Hull-White

| Quantity | Closed form? | Formula complexity |
|----------|:------------:|:------------------:|
| ZCB price $P(t,T)$ | Yes | Simple exponential-affine |
| ZCB yield $R(t,T)$ | Yes | Affine in $r_t$ |
| Bond option | Yes | Black-76 type (Gaussian) |
| Caplet | Yes | Via bond option |
| Swaption | Yes | Jamshidian + Gaussian |
| Cap calibration | Yes | Analytical inversion |

### Black-Karasinski

| Quantity | Closed form? | Numerical method |
|----------|:------------:|:----------------:|
| ZCB price $P(t,T)$ | No | Tree / FD / MC |
| ZCB yield $R(t,T)$ | No | Tree / FD / MC |
| Bond option | No | Tree / MC |
| Caplet | No | Tree / MC |
| Swaption | No | Tree / MC |
| Cap calibration | No | Iterative tree |

The speed difference is typically 2--3 orders of magnitude for a single pricing evaluation, and this compounds during calibration, which requires hundreds of pricing evaluations.

---

## Calibration comparison

### Hull-White calibration

The time-dependent drift $\theta^{HW}(t)$ has an analytical expression in terms of the initial forward rate curve:

$$
\theta^{HW}(t) = f_t(0,t) + af(0,t) + \frac{\sigma^2}{2a}(1 - e^{-2at})
$$

where $f(0,t)$ is the market instantaneous forward rate and $f_t(0,t) = \partial f(0,t)/\partial t$. This formula gives $\theta^{HW}(t)$ directly from market data --- no iteration needed.

Calibrating to swaption volatilities requires minimizing over the constant parameters $a$ and $\sigma$, with $\theta^{HW}(t)$ adjusted analytically at each trial.

### Black-Karasinski calibration

The function $\theta^{BK}(t)$ has no analytical formula. It must be extracted numerically by forward induction on a trinomial tree, solving a nonlinear equation at each time step. Calibrating to swaption volatilities requires:

1. For each trial $(a, \sigma)$: rebuild the entire tree and recalibrate $\theta^{BK}(t)$
2. Price all target swaptions on the tree
3. Compare to market prices and adjust $(a, \sigma)$

This nested iteration makes BK calibration significantly slower than Hull-White.

---

## Volatility structure

### Hull-White: absolute volatility

The standard deviation of $r_t - r_s$ is $\sigma\sqrt{(1 - e^{-2a(t-s)})/(2a)}$, independent of the rate level. Rate changes of \$\pm\$100bp are equally likely whether rates are at 1% or 10%. This produces a flat implied volatility smile in normal (basis-point) terms.

### Black-Karasinski: proportional volatility

The standard deviation of $\ln(r_t/r_s)$ is $\sigma\sqrt{(1-e^{-2a(t-s)})/(2a)}$, independent of level. This means percentage changes are level-independent, so absolute changes scale with the rate level. At 10% rates, 100bp is a 10% move; at 1% rates, 100bp is a 100% move. This produces a flat implied volatility smile in log-normal (percentage) terms.

!!! tip "Which volatility structure matches the market?"
    Empirical evidence suggests that neither pure normal nor pure log-normal volatility holds universally. In low-rate environments, normal volatility tends to be more stable; in high-rate environments, log-normal volatility is more stable. The SABR model or displaced diffusion models provide interpolation between the two extremes.

---

## Strengths and weaknesses summary

| Criterion | Hull-White advantage | Black-Karasinski advantage |
|-----------|:-------------------:|:-------------------------:|
| Pricing speed | Much faster (analytical) | --- |
| Calibration speed | Much faster | --- |
| Positive rates | --- | Guaranteed |
| Negative rate environments | Natural fit | Cannot handle |
| Term structure fit | Exact | Exact |
| Swaption vol smile | Limited (flat normal vol) | Better (log-normal skew) |
| Bermudan/callable pricing | Good (tree + analytical) | Good (tree) |
| Exotic path-dependent | MC feasible | MC feasible |
| Implementation complexity | Low | Moderate |
| Multi-curve extension | Straightforward | More complex |

---

## When to choose which

**Choose Hull-White when**:

- Speed is critical (real-time risk, CVA computation)
- Negative rates are possible or observed
- Vanilla European products dominate the book
- Multi-curve or multi-factor extensions are planned

**Choose Black-Karasinski when**:

- Positive rates are required (certain markets, ALM models)
- The swaption smile has significant log-normal skew
- Bermudan swaptions or callable bonds are the primary products
- Rate-level-dependent volatility better matches the market

---

## Summary

Hull-White and Black-Karasinski represent the two poles of one-factor short-rate modeling: analytical tractability with normal rates (Hull-White) versus numerical pricing with positive log-normal rates (Black-Karasinski). Both fit the initial term structure exactly through time-dependent drifts, but Hull-White extracts its drift analytically while BK requires iterative tree calibration. The choice between them depends on the application: Hull-White dominates for speed-sensitive vanilla pricing, while BK is preferred when rate positivity and log-normal volatility structure are essential. In practice, many desks maintain implementations of both models and select based on the product and market environment.

---

## Exercises

**Exercise 1.** Starting from the Hull-White SDE $dr_t = [\theta^{HW}(t) - ar_t]\,dt + \sigma\,dW_t$ and the Black-Karasinski SDE $d(\ln r_t) = [\theta^{BK}(t) - a\ln r_t]\,dt + \sigma\,dW_t$, apply Ito's lemma to derive the SDE for $r_t$ under the Black-Karasinski model. Show explicitly that the instantaneous volatility of $r_t$ is $\sigma r_t$ (proportional to the rate level), contrasting with the constant volatility $\sigma$ in Hull-White.

??? success "Solution to Exercise 1"
    Starting from the BK SDE for $x_t = \ln r_t$:

    $$
    dx_t = [\theta^{BK}(t) - a\ln r_t]\,dt + \sigma\,dW_t
    $$

    Apply Ito's lemma to $r_t = f(x_t) = e^{x_t}$. We need $f'(x) = e^x$ and $f''(x) = e^x$. Ito's formula gives

    $$
    dr_t = f'(x_t)\,dx_t + \frac{1}{2}f''(x_t)(dx_t)^2
    $$

    The quadratic variation is $(dx_t)^2 = \sigma^2\,dt$. Substituting:

    $$
    dr_t = e^{x_t}\left[\theta^{BK}(t) - a\ln r_t\right]dt + e^{x_t}\sigma\,dW_t + \frac{1}{2}e^{x_t}\sigma^2\,dt
    $$

    Since $e^{x_t} = r_t$:

    $$
    dr_t = r_t\left[\theta^{BK}(t) - a\ln r_t + \frac{1}{2}\sigma^2\right]dt + \sigma r_t\,dW_t
    $$

    The instantaneous volatility of $r_t$ (the diffusion coefficient) is $\sigma r_t$, which is proportional to the rate level. In contrast, the Hull-White SDE $dr_t = [\theta^{HW}(t) - ar_t]\,dt + \sigma\,dW_t$ has constant diffusion coefficient $\sigma$.

    This proportional volatility means that in the BK model, a rate at 10% has ten times the absolute volatility of a rate at 1% (for the same $\sigma$), while in Hull-White both rates have identical absolute volatility. The BK model thus captures the empirical observation that rate volatility tends to increase with the rate level.

---

**Exercise 2.** In the Hull-White model, the conditional distribution of $r_t$ given $r_s$ is Gaussian. Derive an expression for the probability $\mathbb{P}(r_t < 0 \mid r_s)$ in terms of the model parameters $a$, $\sigma$, $\theta^{HW}$, and the current rate $r_s$. For parameter values $a = 0.05$, $\sigma = 0.01$, $r_s = 0.5\%$, and a 10-year horizon, compute this probability numerically. Explain why this issue does not arise in the Black-Karasinski model.

??? success "Solution to Exercise 2"
    In the Hull-White model, given $r_s$, the rate at time $t$ is

    $$
    r_t \mid r_s \sim \mathcal{N}\!\left(\mu_{HW}(s,t),\;\frac{\sigma^2}{2a}(1 - e^{-2a(t-s)})\right)
    $$

    The conditional mean is $\mu_{HW}(s,t) = r_s e^{-a(t-s)} + \int_s^t e^{-a(t-u)}\theta^{HW}(u)\,du$. The probability of negative rates is

    $$
    \mathbb{P}(r_t < 0 \mid r_s) = \Phi\!\left(\frac{-\mu_{HW}(s,t)}{\sqrt{\sigma^2(1-e^{-2a(t-s)})/(2a)}}\right)
    $$

    where $\Phi$ is the standard normal CDF.

    For the numerical calculation with $a = 0.05$, $\sigma = 0.01$, $r_s = 0.005$, and $t - s = 10$ years, we need an estimate of $\mu_{HW}$. For simplicity, assume $\theta^{HW}(u)$ is approximately constant at a level that targets a long-run mean near $r_s$ (i.e., $\theta^{HW} \approx ar_s = 0.05 \times 0.005 = 0.00025$). Then

    $$
    \mu_{HW} \approx 0.005 \cdot e^{-0.5} + \frac{0.00025}{0.05}(1 - e^{-0.5}) = 0.005 \cdot 0.6065 + 0.005 \cdot 0.3935 = 0.005
    $$

    The conditional standard deviation is

    $$
    \nu = \sqrt{\frac{0.01^2}{2 \times 0.05}(1 - e^{-1.0})} = \sqrt{\frac{0.0001}{0.1} \times 0.6321} = \sqrt{0.000632} \approx 0.02514
    $$

    Then

    $$
    \mathbb{P}(r_t < 0) = \Phi\!\left(\frac{-0.005}{0.02514}\right) = \Phi(-0.1989) \approx 0.421
    $$

    This is a striking result: there is approximately a 42% probability of negative rates over a 10-year horizon when the current rate is only 0.5%, because the standard deviation (2.5%) far exceeds the current rate level.

    This issue does not arise in the Black-Karasinski model because $r_t = e^{x_t}$ where $x_t$ is Gaussian. The exponential function maps every real number to a strictly positive value, so $\mathbb{P}(r_t < 0) = 0$ identically, regardless of parameter values or the time horizon.

---

**Exercise 3.** The Hull-White drift function is given analytically by

$$
\theta^{HW}(t) = f_t(0,t) + a\,f(0,t) + \frac{\sigma^2}{2a}(1 - e^{-2at})
$$

Suppose $a = 0.03$, $\sigma = 0.008$, and the market instantaneous forward rate is $f(0,t) = 0.02 + 0.005t$. Compute $\theta^{HW}(5)$. Explain why no analogous closed-form expression exists for $\theta^{BK}(t)$.

??? success "Solution to Exercise 3"
    With $f(0,t) = 0.02 + 0.005t$, we have $f_t(0,t) = \partial f/\partial t = 0.005$. At $t = 5$:

    $$
    f(0,5) = 0.02 + 0.005 \times 5 = 0.045
    $$

    $$
    f_t(0,5) = 0.005
    $$

    Substituting into the Hull-White formula with $a = 0.03$ and $\sigma = 0.008$:

    $$
    \theta^{HW}(5) = f_t(0,5) + a\,f(0,5) + \frac{\sigma^2}{2a}(1 - e^{-2a \cdot 5})
    $$

    Computing each term:

    - $f_t(0,5) = 0.005$
    - $a\,f(0,5) = 0.03 \times 0.045 = 0.00135$
    - $\frac{\sigma^2}{2a} = \frac{0.000064}{0.06} = 0.001067$
    - $1 - e^{-0.30} = 1 - 0.7408 = 0.2592$
    - $\frac{\sigma^2}{2a}(1 - e^{-2a \cdot 5}) = 0.001067 \times 0.2592 = 0.000276$

    Therefore

    $$
    \theta^{HW}(5) = 0.005 + 0.00135 + 0.000276 = 0.006626
    $$

    No analogous closed-form expression exists for $\theta^{BK}(t)$ because the BK bond pricing expectation involves $\mathbb{E}^{\mathbb{Q}}[\exp(-\int_0^T e^{x_s}\,ds)]$, where $x_s$ is Gaussian but $e^{x_s}$ is log-normal. The integral of a log-normal process has no known closed-form moment-generating function. In contrast, the Hull-White expectation involves $\mathbb{E}^{\mathbb{Q}}[\exp(-\int_0^T r_s\,ds)]$ where $r_s$ is Gaussian, and the integral of a Gaussian process is Gaussian, whose moment-generating function is known explicitly. This Gaussian closure property is what yields the analytical formula for $\theta^{HW}(t)$.

---

**Exercise 4.** A desk needs to price 500 European swaptions for a CVA calculation, and each pricing is repeated under 1,000 Monte Carlo scenarios. Compare the computational cost of using Hull-White versus Black-Karasinski for this task, assuming that a single Hull-White swaption takes $10^{-4}$ seconds (analytical Jamshidian) and a single BK swaption takes $10^{-1}$ seconds (trinomial tree). What is the total time for each model?

??? success "Solution to Exercise 4"
    **Hull-White**: Each swaption is priced analytically (Jamshidian decomposition) in $10^{-4}$ seconds. The total number of pricing evaluations is $500 \times 1{,}000 = 500{,}000$.

    $$
    \text{Time}_{HW} = 500{,}000 \times 10^{-4}\text{ s} = 50\text{ seconds}
    $$

    **Black-Karasinski**: Each swaption requires a trinomial tree in $10^{-1}$ seconds. The same $500{,}000$ evaluations give

    $$
    \text{Time}_{BK} = 500{,}000 \times 10^{-1}\text{ s} = 50{,}000\text{ seconds} \approx 13.9\text{ hours}
    $$

    The ratio is

    $$
    \frac{\text{Time}_{BK}}{\text{Time}_{HW}} = \frac{50{,}000}{50} = 1{,}000
    $$

    Black-Karasinski is approximately 1,000 times slower for this task. The Hull-White calculation (50 seconds) is feasible for intraday CVA updates, while the BK calculation (nearly 14 hours) would require overnight batch processing or significant parallelization. This computational gap is one of the primary reasons Hull-White dominates for CVA and other large-scale risk calculations.

---

**Exercise 5.** Explain why the Hull-White model produces a flat implied volatility smile in normal (basis-point) terms while the Black-Karasinski model produces a flat smile in log-normal (percentage) terms. If the current short rate is $r_0 = 5\%$ and the BK model implies a log-normal volatility of $20\%$ per annum, what is the approximate corresponding normal (absolute) volatility in basis points?

??? success "Solution to Exercise 5"
    **Hull-White produces a flat normal smile** because $r_t$ is normally distributed. Conditional on $r_s$, the change $r_t - r_s$ has a distribution whose standard deviation depends only on the model parameters and the time horizon, not on the level $r_s$. This means the absolute (basis-point) volatility of rate changes is constant across rate levels. When pricing caplets at different strikes using Hull-White, the implied normal (Bachelier) volatility is the same for all strikes, producing a flat smile in basis-point terms.

    **Black-Karasinski produces a flat log-normal smile** because $\ln r_t$ is normally distributed. The percentage change $\ln(r_t/r_s)$ has a distribution whose standard deviation is level-independent. This means the log-normal (Black) implied volatility is constant across strikes, producing a flat smile in percentage terms.

    For the conversion, if the BK model implies a log-normal volatility of $\sigma_{\text{LN}} = 20\%$ and the current short rate is $r_0 = 5\%$, the approximate normal (absolute) volatility is

    $$
    \sigma_N \approx \sigma_{\text{LN}} \times r_0 = 0.20 \times 0.05 = 0.01 = 100\text{ bp}
    $$

    The approximate corresponding normal volatility is 100 basis points per annum. This conversion $\sigma_N \approx \sigma_{\text{LN}} \times r_0$ is a first-order approximation valid when the log-normal distribution is not too skewed (i.e., $\sigma_{\text{LN}}\sqrt{T}$ is moderate).

---

**Exercise 6.** During the period 2014--2022, several European government bond yields were negative. Discuss how a risk management system using Black-Karasinski would need to be modified to handle this environment. What is the "shifted BK" approach, and what parameter does it introduce? Compare this to the Hull-White model's natural handling of negative rates.

??? success "Solution to Exercise 6"
    With negative rates observed in European and Japanese bond markets, a risk management system using BK faces a fundamental limitation: the standard BK model has $r_t = e^{x_t} > 0$, so it cannot produce negative rates under any parameter configuration.

    **Required modifications**:

    1. **Shifted Black-Karasinski**: The most common approach defines the shifted rate $r_t^s = r_t + s$ where $s > 0$ is a displacement parameter. The BK model is applied to $r_t^s$:

        $$
        d(\ln r_t^s) = [\theta(t) - a \ln r_t^s]\,dt + \sigma\,dW_t
        $$

        Since $r_t^s = e^{x_t} > 0$, the actual rate $r_t = r_t^s - s = e^{x_t} - s$ can be negative when $e^{x_t} < s$. The parameter $s$ is the **shift** (or displacement), chosen to be larger than the most negative rate the model should accommodate (e.g., $s = 2\%$ if rates as low as $-2\%$ are expected).

    2. **New parameter**: The shift $s$ is an additional parameter that must be either calibrated or set exogenously. Common practice sets $s$ equal to the absolute value of the most negative observed rate plus a buffer.

    **Comparison with Hull-White**: Hull-White naturally handles negative rates because $r_t$ is Gaussian, so $\mathbb{P}(r_t < 0) > 0$ without any modification. No shift parameter is needed, and the model requires no structural changes. The pricing formulas, calibration procedures, and risk sensitivities all work identically for positive and negative rates.

    The shifted BK approach introduces complications: the shift affects the log-normal volatility structure (the proportional volatility is now relative to $r_t + s$, not $r_t$), calibration becomes sensitive to the choice of $s$, and the elegant positivity guarantee of the original BK model is deliberately broken. In a negative-rate environment, Hull-White's natural accommodation of negative rates is a significant practical advantage.

---

**Exercise 7.** A portfolio contains both vanilla caps (valued daily for P&L) and Bermudan swaptions (valued weekly for risk reporting). Using the strengths-and-weaknesses summary in this section, argue for a modeling strategy that uses both Hull-White and Black-Karasinski. What challenges arise from using two different models for related products, particularly regarding hedging consistency?

??? success "Solution to Exercise 7"
    **Argument for a dual-model strategy**:

    - **Vanilla caps with Hull-White**: Caps are valued daily, requiring fast pricing. Hull-White provides analytical caplet formulas (via bond option pricing), enabling real-time P&L computation. The flat normal volatility structure is acceptable for ATM caps, and calibration to cap volatilities is fast (analytical inversion).

    - **Bermudan swaptions with Black-Karasinski**: Bermudan swaptions are valued weekly, so the slower BK tree is computationally feasible. BK's advantages are relevant here: (i) positive rates may be required by risk policies, (ii) the log-normal volatility structure better captures the swaption smile, and (iii) trinomial trees naturally handle the early exercise decisions at each exercise date without requiring regression-based methods.

    **Challenges from using two models**:

    1. **Hedging inconsistency**: If a trader hedges a Bermudan swaption (priced with BK) using vanilla caps (priced with Hull-White), the hedge ratios (deltas, gammas) come from different models. The BK delta of the Bermudan will not perfectly offset the Hull-White delta of the cap hedge, creating residual P&L that is purely a model artifact.

    2. **Inconsistent Greeks**: The two models imply different rate distributions (normal vs. log-normal), so rate sensitivities (DV01, convexity) are computed on incompatible bases. Cross-product risk aggregation becomes unreliable.

    3. **Arbitrage between models**: For products that can be viewed as both a cap-like and a swaption-like instrument, the two models may give different prices, creating internal arbitrage opportunities that complicate risk management.

    4. **Parameter reconciliation**: The mean-reversion parameter $a$ should ideally be consistent across both models, but its interpretation differs (absolute vs. proportional dynamics). Calibrating $a$ separately for each model may produce conflicting views of the rate dynamics.

    5. **Operational complexity**: Maintaining two model implementations, two calibration pipelines, and two sets of Greeks increases the operational burden and the risk of errors.

    In practice, desks mitigate these issues by ensuring that both models are calibrated to overlapping instruments (e.g., ATM swaptions), using model-independent hedging metrics where possible (e.g., bucketed DV01), and monitoring the model-driven P&L residuals explicitly.
