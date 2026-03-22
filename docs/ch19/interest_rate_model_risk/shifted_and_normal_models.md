# Shifted and Normal Models

Classical interest rate option models assume lognormal dynamics, which confine rates to strictly positive values. The emergence of negative interest rates in EUR, CHF, JPY, and SEK markets after 2014 rendered these models inapplicable without modification. Two main alternatives have become standard practice: the **normal (Bachelier) model**, which allows rates to take any real value, and the **shifted lognormal (displaced diffusion) model**, which applies lognormal dynamics to a shifted rate. This section develops both models, derives their pricing formulas, compares their properties, and provides guidance on when to use which.

---

## The Lognormal Model and Its Failure

### Black's Model (Lognormal)

In Black's (1976) framework, the forward rate $F(t)$ follows geometric Brownian motion:

$$
dF(t) = \sigma_{\text{LN}} \, F(t) \, dW(t)
$$

where $\sigma_{\text{LN}}$ is the lognormal (Black) volatility. This implies:

- $F(t) > 0$ almost surely for all $t$
- The distribution of $F(T)$ is lognormal
- The call (caplet) price is given by Black's formula

### Why It Fails for Negative Rates

When the observed forward rate $F(0) < 0$:

- $\ln F(0)$ is undefined
- The SDE $dF = \sigma_{\text{LN}} F \, dW$ has no solution starting from $F(0) < 0$
- Black's formula produces complex-valued outputs

Even when $F(0)$ is small but positive, the lognormal distribution assigns near-zero probability to rates close to zero, causing poor calibration to market prices that reflect significant probability of negative outcomes.

---

## The Normal (Bachelier) Model

### Dynamics

The **Bachelier model** assumes that the forward rate follows arithmetic Brownian motion:

$$
dF(t) = \sigma_N \, dW(t)
$$

where $\sigma_N$ is the **normal (basis-point) volatility**. The rate is Gaussian:

$$
F(T) \sim N(F(0), \, \sigma_N^2 T)
$$

This model allows $F(T)$ to take any value in $(-\infty, +\infty)$, naturally accommodating negative rates.

### Bachelier Caplet Formula

Under the forward measure, the caplet price is:

$$
\boxed{\text{Caplet} = \delta \, P(0, T_{i+1}) \left[(F - K) \, N(d) + \sigma_N \sqrt{T} \, \phi(d)\right]}
$$

where:

$$
d = \frac{F - K}{\sigma_N \sqrt{T}}
$$

and $\phi(\cdot)$ is the standard normal PDF, $N(\cdot)$ is the standard normal CDF.

### Bachelier Floorlet Formula

$$
\text{Floorlet} = \delta \, P(0, T_{i+1}) \left[(K - F) \, N(-d) + \sigma_N \sqrt{T} \, \phi(d)\right]
$$

### ATM Approximation

For ATM options ($F = K$, so $d = 0$):

$$
\text{ATM Caplet} = \delta \, P(0, T_{i+1}) \, \sigma_N \sqrt{T} \, \phi(0) = \delta \, P(0, T_{i+1}) \, \sigma_N \sqrt{T} \cdot \frac{1}{\sqrt{2\pi}}
$$

### Properties

- **Symmetric payoff distribution:** Unlike the lognormal model, the normal model produces a symmetric smile (no inherent skew)
- **Constant absolute volatility:** A 1 bp rate move has the same probability regardless of the rate level
- **Negative rates possible:** Probability of $F(T) < 0$ is $N(-F(0)/(\sigma_N\sqrt{T}))$
- **Unbounded rates:** Arbitrarily large positive and negative rates have nonzero (though small) probability

!!! tip "Normal Vol Convention"
    Normal volatility $\sigma_N$ is quoted in **basis points per annum** (e.g., 60 bps). Black volatility $\sigma_{\text{LN}}$ is quoted as a **percentage** (e.g., 20%). The two are related at the ATM level by $\sigma_N \approx F \cdot \sigma_{\text{LN}}$.

---

## The Shifted Lognormal (Displaced Diffusion) Model

### Dynamics

The **shifted lognormal model** (or displaced diffusion model) applies lognormal dynamics to a shifted rate $F(t) + s$, where $s > 0$ is the **shift parameter**:

$$
d(F(t) + s) = \sigma_{\text{SLN}} \, (F(t) + s) \, dW(t)
$$

Equivalently:

$$
dF(t) = \sigma_{\text{SLN}} \, (F(t) + s) \, dW(t)
$$

The shifted rate $F(t) + s$ is lognormally distributed:

$$
F(T) + s = (F(0) + s) \exp\!\left(-\frac{1}{2}\sigma_{\text{SLN}}^2 T + \sigma_{\text{SLN}} W(T)\right)
$$

Since $F(T) + s > 0$ almost surely, the forward rate satisfies $F(T) > -s$. The shift $s$ sets the **lower bound** for the rate.

### Shifted Black Caplet Formula

The pricing formula is Black's formula applied to the shifted rate:

$$
\boxed{\text{Caplet} = \delta \, P(0, T_{i+1}) \left[(F + s) \, N(d_1) - (K + s) \, N(d_2)\right]}
$$

where:

$$
d_1 = \frac{\ln\!\left(\frac{F + s}{K + s}\right) + \frac{1}{2}\sigma_{\text{SLN}}^2 T}{\sigma_{\text{SLN}} \sqrt{T}}
$$

$$
d_2 = d_1 - \sigma_{\text{SLN}} \sqrt{T}
$$

### Choosing the Shift

The shift parameter $s$ must satisfy:

- $s > -F(0)$ so that the initial shifted rate is positive
- $s$ large enough that $F(T) > -s$ with near-certainty (i.e., the lower bound is never binding in practice)

Common choices:

| Market | Typical Shift |
|---|---|
| EUR (post-2015) | 1% to 3% |
| JPY | 1% to 2% |
| USD (2020) | 0.5% to 1% |
| CHF | 1% to 3% |

The shift is typically chosen to ensure all observed market rates satisfy $F + s > 0$.

### Properties

- **Bounded below:** Rates cannot fall below $-s$, which may or may not be realistic
- **Lognormal skew on shifted rate:** The model inherits the lognormal skew (positive skew for the shifted rate)
- **Converges to Black:** When $s = 0$, the shifted lognormal model reduces to the standard lognormal model
- **Converges to normal:** When $s \to \infty$ and $\sigma_{\text{SLN}} \to 0$ such that $\sigma_{\text{SLN}} \cdot s \to \sigma_N$, the shifted lognormal model converges to the normal model

---

## Model Comparison

### Volatility Conventions and Conversion

The three models use different volatility conventions that are related by:

**At the ATM level ($K = F$):**

$$
\sigma_N \approx \sigma_{\text{LN}} \cdot F \approx \sigma_{\text{SLN}} \cdot (F + s)
$$

More precisely, matching ATM option prices:

$$
\sigma_N = \sigma_{\text{LN}} \cdot F \cdot \frac{\phi(0)}{\phi(0)} = \sigma_{\text{LN}} \cdot F
$$

$$
\sigma_N \approx \sigma_{\text{SLN}} \cdot (F + s)
$$

### Smile and Skew Comparison

| Feature | Lognormal | Normal | Shifted Lognormal |
|---|---|---|---|
| Smile shape | Flat (by construction) | Flat (by construction) | Flat (by construction) |
| Implied vol skew | Positive (in LN terms) | Negative (in LN terms) | Adjustable via $s$ |
| Rate domain | $(0, +\infty)$ | $(-\infty, +\infty)$ | $(-s, +\infty)$ |
| Probability of negative rates | 0 | Positive | 0 (but $F > -s$) |

All three are single-parameter models (given the shift) and produce **flat** smiles in their own volatility metric. The observed market smile (in any convention) requires extensions like SABR.

### Behavior Near Zero

As the forward rate $F \to 0$:

- **Lognormal:** Black vol $\sigma_{\text{LN}}$ explodes (since $\sigma_N \approx \sigma_{\text{LN}} \cdot F$)
- **Normal:** Normal vol $\sigma_N$ remains well-behaved
- **Shifted lognormal:** Shifted vol $\sigma_{\text{SLN}}$ increases but remains finite (scales as $1/(F+s)$)

This behavior has practical implications for calibration near the zero lower bound.

---

## Worked Example: Comparing the Three Models

??? example "Caplet Pricing Across Models"

    **Parameters:**

    - Forward rate: $F = 0.50\% = 0.005$
    - Strike: $K = 0.50\%$ (ATM)
    - Time to expiry: $T = 2.0$ years
    - Day count: $\delta = 0.25$
    - Discount factor: $P(0, T_{i+1}) = 0.990$
    - Target caplet price: 0.000300 (30.0 bps of $\delta \cdot P$)

    **Bachelier model:**

    Solve: $\sigma_N \sqrt{T} / \sqrt{2\pi} = 0.000300 / (\delta \cdot P)$

    $\sigma_N \sqrt{2} / \sqrt{2\pi} = 0.000300 / 0.2475 = 0.001212$

    $\sigma_N = 0.001212 \times \sqrt{\pi} = 0.001212 \times 1.2533 = 0.001519 = 15.19$ bps

    So $\sigma_N \approx 15.2$ bps/year.

    **Black model (lognormal):**

    $\sigma_{\text{LN}} \approx \sigma_N / F = 0.001519 / 0.005 = 30.4\%$

    At $F = 0.50\%$, the Black vol is extremely high, reflecting that a 15 bp normal move is proportionally large relative to a 50 bp rate.

    **Shifted lognormal ($s = 2\%$):**

    $\sigma_{\text{SLN}} \approx \sigma_N / (F + s) = 0.001519 / 0.025 = 6.08\%$

    The shifted lognormal vol is a moderate 6.08%, much more stable than the pure Black vol.

    **Key insight:** The normal and shifted lognormal volatilities remain stable and interpretable in the low-rate environment, while the lognormal volatility becomes very large and highly sensitive to the rate level.

---

## Model Risk Considerations

### Rate-Level Dependence of Volatility

The fundamental difference among the models is how instantaneous volatility scales with the rate level:

| Model | Instantaneous Vol | Rate-Level Dependence |
|---|---|---|
| Lognormal | $\sigma_{\text{LN}} \cdot F$ | Proportional |
| Normal | $\sigma_N$ | Constant |
| Shifted Lognormal | $\sigma_{\text{SLN}} \cdot (F + s)$ | Proportional to shifted rate |

This has consequences for **hedging**:

- In the lognormal model, the hedge ratio (delta) is independent of the rate level
- In the normal model, the delta is independent but the dollar exposure (DV01) is constant
- The shifted lognormal model interpolates between these behaviors

### Extrapolation Risk

!!! warning "Model Divergence at Extreme Rates"
    The three models agree closely near the current market level but diverge significantly in the tails:

    - **Far out-of-the-money payers** (high strikes): The lognormal model assigns higher probability to extreme rate increases than the normal model
    - **Deep OTM receivers** (low/negative strikes): The normal model assigns positive probability to very negative rates; the shifted lognormal bounds rates above $-s$; the lognormal model assigns zero probability to negative rates

    For exotic products with barrier or digital features at extreme rate levels, the model choice can produce materially different prices.

### Shift Selection Risk

The shifted lognormal model introduces the shift $s$ as an additional parameter:

- **Too small:** The model behaves like the lognormal model and may fail when rates approach $-s$
- **Too large:** The model behaves like the normal model and provides little benefit over Bachelier
- **Time-varying shifts:** Some practitioners update $s$ as market conditions change, but this complicates backtesting and hedging

There is no theoretically correct shift; it is a pragmatic choice that should be viewed as part of the model risk.

---

## When to Use Which Model

### Decision Framework

!!! info "Model Selection Guide"

    **Use the normal (Bachelier) model when:**

    - Rates are near zero or negative
    - The primary concern is robustness across rate levels
    - The market quotes volatilities in normal (bp) terms
    - Simplicity and transparency are prioritized

    **Use the shifted lognormal model when:**

    - Rates are low but positive, and the shift provides a comfortable buffer
    - Existing infrastructure is built around Black's formula (minimal code changes)
    - The market convention is shifted Black vol (common in EUR swaptions post-2015)
    - A moderate amount of lognormal skew is desired

    **Use the standard lognormal (Black) model when:**

    - Rates are comfortably positive (e.g., USD rates above 2%)
    - The market quotes in lognormal (Black) vol terms
    - Backward compatibility with legacy systems is important
    - The product is not sensitive to the zero-rate boundary

### Market Practice (as of 2024)

| Market | Standard Convention |
|---|---|
| EUR caps/swaptions | Shifted Black ($s = 50$--$300$ bps) or Normal |
| USD caps/swaptions | Black (pre-2020), Normal or Shifted Black (post-2020) |
| JPY swaptions | Normal or Shifted Black ($s = 100$--$200$ bps) |
| GBP swaptions | Black or Shifted Black |

The trend has been a gradual shift from lognormal to normal conventions, accelerated by negative rate environments.

---

## SABR Extensions

### SABR with Shift

The SABR model can be combined with the shifted lognormal framework to capture the smile:

$$
dF = \alpha (F + s)^\beta \, dW_1
$$

$$
d\alpha = \nu \alpha \, dW_2
$$

$$
dW_1 \cdot dW_2 = \rho \, dt
$$

For $\beta = 0$: shifted normal SABR. For $\beta = 1$: shifted lognormal SABR.

### Normal SABR

Setting $\beta = 0$ and $s = 0$:

$$
dF = \alpha \, dW_1
$$

This is the **normal SABR** model, which is increasingly popular for negative rate environments. The Hagan et al. approximation provides analytical implied normal volatilities as a function of strike.

---

## Key Takeaways

- The **lognormal (Black) model** requires strictly positive rates and fails when rates are zero or negative
- The **normal (Bachelier) model** allows any real-valued rate, with dynamics $dF = \sigma_N dW$ and a Gaussian terminal distribution
- The **shifted lognormal model** applies Black's formula to $F + s$, bounding rates above $-s$ while preserving lognormal tractability
- **Volatility conversions:** $\sigma_N \approx \sigma_{\text{LN}} \cdot F \approx \sigma_{\text{SLN}} \cdot (F + s)$ at the ATM level
- Models agree near current rates but **diverge in the tails**, creating material differences for OTM options and exotics
- The **shift parameter** is a pragmatic choice, not a fundamental quantity, and its selection is part of model risk
- Market convention has shifted toward normal and shifted lognormal quoting since the negative rate era began in 2014

---

## Further Reading

- Bachelier (1900), *Theorie de la Speculation* (the original normal model)
- Black (1976), "The Pricing of Commodity Contracts"
- Brigo & Mercurio (2006), *Interest Rate Models: Theory and Practice*, Chapter 1
- Hagan et al. (2002), "Managing Smile Risk" (SABR model)
- Andersen & Piterbarg (2010), *Interest Rate Modeling*, Volume I, Chapter 5
