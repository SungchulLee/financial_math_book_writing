# Volatility Smile and SABR (Preview)

!!! tip "Key Idea"
    The Black model assumes constant volatility, but market data shows that implied volatility depends on strike. This phenomenon is known as the volatility smile.

---

## The Volatility Smile

In practice, implied volatility varies with strike:

$$
\sigma_{\text{imp}} = \sigma(K)
$$

Typical pattern:

- higher vol for deep in/out-of-the-money options
- lower vol near at-the-money

---

### Shapes Observed

- **Smile:** symmetric around ATM
- **Skew:** asymmetric (common in rates markets)

---

## Why Does the Smile Exist?

The Black model assumes:

- lognormal distribution
- constant volatility

But real markets exhibit:

- stochastic volatility
- fat tails
- asymmetry

---

!!! quote "Interpretation"
    The volatility smile reflects the market's belief that extreme movements are more likely than predicted by a simple lognormal model.

---

## Implications

A flat volatility assumption leads to:

- mispricing of options
- hedging errors

Therefore, we need models that reproduce the observed smile.

---

## SABR Model (Overview)

Recall (see [§ SABR / Hagan Implied Volatility Approximation](../../ch14/sabr_model/hagan_implied_volatility_approximation.md)) the SABR specification

$$
\begin{aligned}
dS_t &= \sigma_t S_t^\beta dW_t^1, \quad d\sigma_t = \alpha \sigma_t dW_t^2, \quad dW_t^1 dW_t^2 = \rho\, dt
\end{aligned}
$$

with $S_t$ now interpreted as the **forward swap rate**, and the Hagan closed-form approximation $\sigma_{\text{SABR}}(K)$ used to fit the swaption smile. The parameter roles ($\alpha$ level, $\beta$ backbone, $\rho$ skew, $\nu$ curvature) carry over unchanged.

---

## Practical Use

SABR is used for:

- fitting volatility surfaces
- pricing exotic interest rate derivatives
- interpolating between strikes

---

## Connection to Black Model

- Black model = constant volatility
- SABR = stochastic volatility

Thus:

> SABR extends Black by allowing volatility itself to evolve randomly.

---

## Limitations

- approximation, not exact
- calibration can be unstable
- extreme strikes less reliable

---

!!! note "Big Picture"
    The progression is:

    - Black model → constant volatility
    - Market → volatility smile
    - SABR → model that matches smile

    This reflects a broader theme:

    > pricing models evolve to match observed market behavior, not the other way around.

---

## What Comes Next

More advanced frameworks include:

- local volatility models
- stochastic volatility models
- LIBOR Market Model (LMM)

These build on the same principles introduced here.

---

## Exercises

**Exercise 1.** Explain why the Black model produces a flat implied volatility smile. What assumption is responsible, and how does it relate to the distributional shape of the underlying?

??? success "Solution"
    The Black model assumes that the forward rate follows a geometric Brownian motion with
    **constant volatility** $\sigma$. Under this assumption the terminal distribution of the
    forward rate is lognormal, which is fully determined by a single volatility parameter.
    Because the same $\sigma$ is used regardless of strike $K$, inverting the Black formula
    for any option price recovered from this model returns exactly $\sigma$ for every $K$.
    Hence the implied volatility curve $\sigma_{\text{imp}}(K) = \sigma$ is flat.

    The root cause is the lognormal distributional assumption: it assigns fixed probabilities
    to tail events. In reality, market prices imply heavier tails and possible asymmetry,
    which manifest as strike-dependent implied volatility — the smile or skew.

---

**Exercise 2.** In the SABR model, identify which parameters primarily control the **skew** (asymmetry) and which control the **curvature** (smile convexity) of the implied volatility surface. Briefly explain the role of each.

??? success "Solution"

    - **$\rho$ (correlation)** is the primary driver of **skew**. When $\rho < 0$, a drop in the
      forward rate tends to coincide with a rise in volatility, making out-of-the-money puts
      more expensive and tilting the smile to the left (negative skew). Conversely, $\rho > 0$
      produces positive skew.
    - **$\nu$ (vol-of-vol)** is the primary driver of **curvature**. A larger $\nu$ means
      volatility itself is more volatile, which fattens both tails of the distribution and
      raises implied volatility for strikes far from ATM, increasing the convexity of the
      smile.
    - **$\beta$ (elasticity)** also influences skew through the backbone of the model — it
      controls how volatility scales with the level of the forward rate — but its effect is
      secondary once $\rho$ and $\nu$ are calibrated.
    - **$\alpha$** sets the overall ATM volatility level and shifts the entire smile up or down
      without materially changing its shape.

---

**Exercise 3.** Suppose the SABR parameters are $\alpha = 0.03$, $\beta = 0.5$, $\rho = -0.2$, $\nu = 0.4$, and the forward swap rate is $S = 0.05$. Using the leading-order SABR ATM approximation

$$
\sigma_{\text{ATM}} \approx \frac{\alpha}{S^{1-\beta}}
$$

compute the approximate ATM implied volatility.

??? success "Solution"
    At the money we have $K = S = 0.05$. Substituting into the leading-order formula:

    $$
    \sigma_{\text{ATM}} \approx \frac{\alpha}{S^{1-\beta}} = \frac{0.03}{0.05^{1-0.5}} = \frac{0.03}{0.05^{0.5}} = \frac{0.03}{\sqrt{0.05}}
    $$

    Computing the denominator:

    $$
    \sqrt{0.05} \approx 0.2236
    $$

    Therefore:

    $$
    \sigma_{\text{ATM}} \approx \frac{0.03}{0.2236} \approx 0.1342 = 13.42\%
    $$

    The approximate ATM implied volatility is about $13.4\%$.

---

**Exercise 4.** Explain conceptually why the volatility smile matters for hedging interest rate derivatives. What can go wrong if a trader ignores the smile and hedges using a single flat volatility?

??? success "Solution"
    The volatility smile encodes the market's view that implied volatility is
    strike-dependent, reflecting richer dynamics (stochastic volatility, fat tails,
    skewness) than the Black model captures. Hedging implications include:

    1. **Incorrect Greeks.** If a trader uses a flat volatility to compute delta and vega,
       those sensitivities will not account for the fact that volatility itself changes as the
       underlying moves. The delta from a smile-consistent model (e.g., SABR) differs from
       the flat-vol delta, so the hedge ratio is wrong.

    2. **Vega risk misallocation.** A flat-vol hedge assumes all strikes share the same
       volatility exposure. In reality, out-of-the-money options have different vega profiles
       under the smile, and ignoring this leads to residual vega risk after hedging.

    3. **P&L leakage.** As the forward rate moves, the smile shifts, and the flat-vol hedge
       does not adapt. Over time this produces systematic hedging errors and unexpected P&L
       swings, especially for portfolios with significant exposure to away-from-the-money
       strikes.

    In summary, ignoring the smile means the hedge is built on an incorrect model of how
    option prices respond to market moves, leading to under- or over-hedging and increased
    risk.
