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

---

**Exercise 2.** In the Hull-White model, the conditional distribution of $r_t$ given $r_s$ is Gaussian. Derive an expression for the probability $\mathbb{P}(r_t < 0 \mid r_s)$ in terms of the model parameters $a$, $\sigma$, $\theta^{HW}$, and the current rate $r_s$. For parameter values $a = 0.05$, $\sigma = 0.01$, $r_s = 0.5\%$, and a 10-year horizon, compute this probability numerically. Explain why this issue does not arise in the Black-Karasinski model.

---

**Exercise 3.** The Hull-White drift function is given analytically by

$$
\theta^{HW}(t) = f_t(0,t) + a\,f(0,t) + \frac{\sigma^2}{2a}(1 - e^{-2at})
$$

Suppose $a = 0.03$, $\sigma = 0.008$, and the market instantaneous forward rate is $f(0,t) = 0.02 + 0.005t$. Compute $\theta^{HW}(5)$. Explain why no analogous closed-form expression exists for $\theta^{BK}(t)$.

---

**Exercise 4.** A desk needs to price 500 European swaptions for a CVA calculation, and each pricing is repeated under 1,000 Monte Carlo scenarios. Compare the computational cost of using Hull-White versus Black-Karasinski for this task, assuming that a single Hull-White swaption takes $10^{-4}$ seconds (analytical Jamshidian) and a single BK swaption takes $10^{-1}$ seconds (trinomial tree). What is the total time for each model?

---

**Exercise 5.** Explain why the Hull-White model produces a flat implied volatility smile in normal (basis-point) terms while the Black-Karasinski model produces a flat smile in log-normal (percentage) terms. If the current short rate is $r_0 = 5\%$ and the BK model implies a log-normal volatility of $20\%$ per annum, what is the approximate corresponding normal (absolute) volatility in basis points?

---

**Exercise 6.** During the period 2014--2022, several European government bond yields were negative. Discuss how a risk management system using Black-Karasinski would need to be modified to handle this environment. What is the "shifted BK" approach, and what parameter does it introduce? Compare this to the Hull-White model's natural handling of negative rates.

---

**Exercise 7.** A portfolio contains both vanilla caps (valued daily for P&L) and Bermudan swaptions (valued weekly for risk reporting). Using the strengths-and-weaknesses summary in this section, argue for a modeling strategy that uses both Hull-White and Black-Karasinski. What challenges arise from using two different models for related products, particularly regarding hedging consistency?
