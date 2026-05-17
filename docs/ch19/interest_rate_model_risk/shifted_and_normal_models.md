# Shifted and Normal Models

Classical interest rate option models assume lognormal dynamics, which confine rates to strictly positive values. The emergence of negative interest rates in EUR, CHF, JPY, and SEK markets after 2014 rendered these models inapplicable without modification. Two main alternatives have become standard practice: the **normal (Bachelier) model**, which allows rates to take any real value, and the **shifted lognormal (displaced diffusion) model**, which applies lognormal dynamics to a shifted rate. This section develops both models, derives their pricing formulas, compares their properties, and provides guidance on when to use which.

---

## The Lognormal Model and Its Failure

### Black's Model (Lognormal)

Recall (see [§ Caplet Pricing and Black's Formula](../lmm/caplet_pricing_black_formula.md)): in Black's (1976) framework $dF(t) = \sigma_{\text{LN}}\,F(t)\,dW(t)$ under the relevant forward measure, so $F(t) > 0$ a.s., $F(T)$ is lognormal, and the caplet price is given by Black's formula.

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

---

## Exercises

**Exercise 1.** Using the Bachelier (normal) caplet formula, price a caplet with forward rate $F = -0.15\%$, strike $K = 0\%$, normal volatility $\sigma_N = 0.45\%$, expiry $T = 3$ years, accrual $\delta = 0.5$, and discount factor $P(0, T_{i+1}) = 1.005$. Verify that the formula is well-defined despite the negative forward rate.

??? success "Solution to Exercise 1"

    **Parameters:** $F = -0.0015$, $K = 0$, $\sigma_N = 0.0045$, $T = 3$, $\delta = 0.5$, $P(0, T_{i+1}) = 1.005$.

    The Bachelier caplet formula is

    $$
    \text{Caplet} = \delta\,P(0, T_{i+1})\left[(F - K)\,N(d) + \sigma_N\sqrt{T}\,\phi(d)\right]
    $$

    where $d = \frac{F - K}{\sigma_N\sqrt{T}}$.

    **Step 1: Compute $d$.**

    $$
    d = \frac{-0.0015 - 0}{0.0045\sqrt{3}} = \frac{-0.0015}{0.0045 \times 1.7321} = \frac{-0.0015}{0.007794} = -0.19245
    $$

    **Step 2: Look up $N(d)$ and $\phi(d)$.**

    $$
    N(-0.19245) \approx 0.4237
    $$

    $$
    \phi(-0.19245) = \frac{1}{\sqrt{2\pi}}\exp\!\left(-\frac{0.19245^2}{2}\right) = \frac{1}{\sqrt{2\pi}}\exp(-0.01852) \approx 0.3970 \times 0.9817 \approx 0.3897
    $$

    **Step 3: Compute the bracket terms.**

    $$
    (F - K)\,N(d) = (-0.0015)(0.4237) = -0.0006356
    $$

    $$
    \sigma_N\sqrt{T}\,\phi(d) = (0.007794)(0.3897) = 0.003037
    $$

    $$
    \text{Bracket} = -0.0006356 + 0.003037 = 0.002401
    $$

    **Step 4: Final price.**

    $$
    \text{Caplet} = 0.5 \times 1.005 \times 0.002401 = 0.5025 \times 0.002401 = 0.001207
    $$

    The caplet price is approximately **0.1207%** of notional (about 12.07 bps times $\delta \cdot P$).

    **Verification of well-definedness:** Despite $F = -0.15\% < 0$, every quantity in the formula is real-valued. The difference $F - K = -0.0015$ is simply a real number, $d$ is a well-defined real number, and $N(\cdot)$ and $\phi(\cdot)$ accept any real argument. No logarithms or ratios appear in the Bachelier formula, so negativity of $F$ causes no issues whatsoever.

---

**Exercise 2.** For the shifted lognormal model with shift $s = 2\%$, forward rate $F = 0.5\%$, and shifted lognormal volatility $\sigma_{\text{SLN}} = 30\%$, compute the shifted forward $F + s$ and price an ATM caplet (strike $K = F$) with $T = 2$, $\delta = 0.25$, and $P(0, T_{i+1}) = 0.99$. Then convert the shifted lognormal vol to the equivalent normal vol using $\sigma_N \approx \sigma_{\text{SLN}} \cdot (F + s)$ and verify the price is approximately the same under the Bachelier formula.

??? success "Solution to Exercise 2"

    **Parameters:** $s = 0.02$, $F = 0.005$, $\sigma_{\text{SLN}} = 0.30$, $K = F = 0.005$ (ATM), $T = 2$, $\delta = 0.25$, $P(0, T_{i+1}) = 0.99$.

    **Step 1: Shifted forward rate.**

    $$
    F + s = 0.005 + 0.02 = 0.025
    $$

    **Step 2: Price using the shifted Black formula.** For an ATM option ($K = F$), we have $K + s = F + s = 0.025$, so $\ln\!\left(\frac{F+s}{K+s}\right) = \ln(1) = 0$:

    $$
    d_1 = \frac{0 + \frac{1}{2}(0.30)^2 \times 2}{0.30\sqrt{2}} = \frac{0.09}{0.4243} = 0.21213
    $$

    $$
    d_2 = d_1 - \sigma_{\text{SLN}}\sqrt{T} = 0.21213 - 0.4243 = -0.21213
    $$

    $$
    N(0.21213) \approx 0.5840, \qquad N(-0.21213) \approx 0.4160
    $$

    $$
    \text{Caplet}_{\text{SLN}} = 0.25 \times 0.99 \times [0.025 \times 0.5840 - 0.025 \times 0.4160]
    $$

    $$
    = 0.2475 \times 0.025 \times (0.5840 - 0.4160) = 0.2475 \times 0.025 \times 0.1680
    $$

    $$
    = 0.2475 \times 0.004200 = 0.001040
    $$

    **Step 3: Convert to normal vol.** Using the ATM approximation:

    $$
    \sigma_N \approx \sigma_{\text{SLN}} \cdot (F + s) = 0.30 \times 0.025 = 0.0075 = 75 \text{ bps}
    $$

    **Step 4: Price using Bachelier.** For ATM ($F = K$, so $d = 0$):

    $$
    \text{Caplet}_N = \delta\,P \cdot \sigma_N\sqrt{T} \cdot \phi(0) = 0.2475 \times 0.0075 \times \sqrt{2} \times \frac{1}{\sqrt{2\pi}}
    $$

    $$
    = 0.2475 \times 0.0075 \times 1.4142 \times 0.39894
    $$

    $$
    = 0.2475 \times 0.0075 \times 0.56419 = 0.2475 \times 0.004231 = 0.001047
    $$

    **Comparison:** The shifted Black price is $\approx 0.001040$ and the Bachelier price is $\approx 0.001047$. The difference is less than 1 bp, confirming that the ATM approximation $\sigma_N \approx \sigma_{\text{SLN}} \cdot (F + s)$ produces nearly identical prices. The small discrepancy arises because the ATM volatility conversion is exact only to first order; the lognormal and normal distributions differ slightly even when matched at ATM.

---

**Exercise 3.** Consider two choices of shift: $s_1 = 1\%$ and $s_2 = 3\%$. For a forward rate $F = 1\%$ and expiry $T = 5$, compute the shifted lognormal volatility in each case such that both models produce the same ATM caplet price. How do the implied volatility smiles differ for OTM strikes (e.g., $K = -0.5\%$ and $K = 3\%$)? Discuss the model risk implications.

??? success "Solution to Exercise 3"

    **Setup:** $F = 0.01$, $T = 5$, two shift values $s_1 = 0.01$ and $s_2 = 0.03$.

    **Step 1: Match ATM prices.** Both models must produce the same ATM caplet price. Using the ATM approximation for the Bachelier equivalent, the common normal vol is some $\sigma_N$. The shifted lognormal vols satisfy:

    $$
    \sigma_N \approx \sigma_{\text{SLN},1} \cdot (F + s_1) = \sigma_{\text{SLN},2} \cdot (F + s_2)
    $$

    $$
    \sigma_{\text{SLN},1} \cdot (0.01 + 0.01) = \sigma_{\text{SLN},2} \cdot (0.01 + 0.03)
    $$

    $$
    \sigma_{\text{SLN},1} \cdot 0.02 = \sigma_{\text{SLN},2} \cdot 0.04
    $$

    $$
    \sigma_{\text{SLN},1} = 2\,\sigma_{\text{SLN},2}
    $$

    For example, if we target $\sigma_N = 60$ bps $= 0.006$:

    $$
    \sigma_{\text{SLN},1} = \frac{0.006}{0.02} = 30\%, \qquad \sigma_{\text{SLN},2} = \frac{0.006}{0.04} = 15\%
    $$

    Both produce the same ATM caplet price by construction.

    **Step 2: OTM strikes.** Consider $K_1 = -0.5\% = -0.005$ (deep OTM floor / ITM cap) and $K_2 = 3\% = 0.03$ (OTM cap).

    For $K_1 = -0.005$: The shifted strikes are $K_1 + s_1 = 0.005$ and $K_1 + s_2 = 0.025$. Under model 1 ($s_1 = 1\%$), the ratio $(F+s_1)/(K_1+s_1) = 0.02/0.005 = 4.0$, corresponding to a deeply ITM option on the shifted rate with high moneyness. Under model 2 ($s_2 = 3\%$), the ratio is $0.04/0.025 = 1.6$, much less extreme. The lognormal distribution with a higher moneyness ratio assigns different tail probabilities, so the two models disagree on the price.

    For $K_2 = 0.03$: The shifted strikes are $K_2 + s_1 = 0.04$ and $K_2 + s_2 = 0.06$. Under model 1, $(F+s_1)/(K_2+s_1) = 0.02/0.04 = 0.5$; under model 2, it is $0.04/0.06 = 0.667$. Again, different moneyness ratios produce different lognormal tail probabilities.

    **Step 3: Model risk implications.** The two models agree at ATM but diverge away from the money. The smaller shift ($s_1$) produces a more skewed distribution (since the lognormal characteristic is more pronounced relative to the shifted rate level), leading to higher prices for deep OTM caps and lower prices for deep OTM floors compared to the larger shift ($s_2$). The model risk is that **the shift is a free parameter that materially affects OTM option prices**, and there is no market-implied unique value for $s$. Any exotic product sensitive to the tails of the rate distribution will have a price that depends on this unobservable parameter.

---

**Exercise 4.** Explain why the lognormal distribution has a heavier right tail than the normal distribution, while the normal distribution assigns more probability to extreme negative values. How does this affect the relative pricing of deep out-of-the-money caps versus deep out-of-the-money floors under the two models?

??? success "Solution to Exercise 4"

    **Right tail (high rates):** The lognormal distribution has a heavier right tail than the normal distribution. This is because a lognormally distributed rate $F(T) = F(0)\exp(-\frac{1}{2}\sigma_{\text{LN}}^2 T + \sigma_{\text{LN}} W(T))$ can grow exponentially for large positive realizations of $W(T)$, while the normally distributed rate $F(T) = F(0) + \sigma_N W(T)$ grows only linearly. Quantitatively, the lognormal distribution is right-skewed with a long upper tail, while the normal distribution is symmetric.

    **Left tail (negative rates):** The lognormal distribution is bounded below by zero --- it assigns exactly zero probability to $F(T) < 0$. The normal distribution is unbounded below and assigns positive probability to arbitrarily negative rates. Specifically, $P(F(T) < 0) = N(-F(0)/(\sigma_N\sqrt{T})) > 0$.

    **Impact on deep OTM caps (high strikes $K \gg F$):**

    A deep OTM cap pays $(F(T) - K)^+$ for $K \gg F$. The lognormal model assigns higher probability to extreme upward moves than the normal model (heavier right tail), so:

    $$
    \text{Lognormal OTM cap price} > \text{Normal OTM cap price}
    $$

    for sufficiently high strikes.

    **Impact on deep OTM floors (low/negative strikes $K \ll F$):**

    A deep OTM floor pays $(K - F(T))^+$. For $K < 0$, the lognormal model assigns zero probability to $F(T) < 0$, so the floor price is exactly zero. The normal model assigns positive probability to $F(T) < K < 0$, so the floor has a positive price:

    $$
    \text{Lognormal OTM floor price} = 0 < \text{Normal OTM floor price}
    $$

    for negative strikes.

    For strikes $0 < K \ll F$, the normal model typically assigns more probability to rates falling to $K$ (due to its symmetric Gaussian tails) than the lognormal model (where rates cluster away from zero for moderate $F$). Thus the normal model generally gives higher prices for deep OTM floors.

    In summary, the lognormal model overprices (relative to normal) deep OTM caps and underprices deep OTM floors, reflecting its right-skewed, non-negative distribution versus the symmetric, unbounded normal distribution.

---

**Exercise 5.** A swaption desk currently quotes in Black (lognormal) implied volatility. With EUR swap rates at $-0.20\%$, the desk needs to switch convention. Compare the advantages of quoting in (a) normal implied volatility versus (b) shifted lognormal implied volatility with a standard shift. Which convention is more stable as rates move through zero?

??? success "Solution to Exercise 5"

    With EUR swap rates at $-0.20\%$, the Black (lognormal) model cannot be applied since $\ln(F)$ is undefined for $F < 0$. The desk must switch conventions.

    **(a) Normal implied volatility:**

    - **Stability through zero:** Normal vol $\sigma_N$ is defined regardless of the sign of $F$. As rates move from $-0.20\%$ to $+0.20\%$ and back, the normal vol remains well-defined and continuous. There is no singularity or discontinuity at $F = 0$.
    - **Interpretability:** $\sigma_N$ measures the absolute magnitude of rate fluctuations (in bps). If rates move from $-0.20\%$ to $+0.30\%$, the normal vol interpretation is unaffected.
    - **Market adoption:** EUR, CHF, and JPY markets have broadly adopted normal vol quoting.
    - **Drawback:** Cannot capture smile/skew by itself (needs SABR or similar extension).

    **(b) Shifted lognormal implied volatility:**

    - **Depends on shift choice:** With shift $s$, the vol is $\sigma_{\text{SLN}} = \sigma_N / (F + s)$. If $s = 2\%$, then at $F = -0.20\%$, $\sigma_{\text{SLN}} = \sigma_N / 0.018$, which is well-defined.
    - **Instability risk:** If $F$ approaches $-s$ (the lower bound), $\sigma_{\text{SLN}}$ diverges. For example, if $s = 0.5\%$ and $F = -0.20\%$, then $F + s = 0.30\%$, and small movements in $F$ cause large percentage changes in $\sigma_{\text{SLN}}$.
    - **Shift dependence:** If the shift needs to be updated (e.g., rates fall further), all quoted vols change, disrupting time series and risk reports.
    - **Compatibility:** Easy to implement in existing Black vol infrastructure.

    **Which is more stable?** The **normal convention is more stable** as rates move through zero. Normal vol is invariant to the level of $F$ by construction (constant absolute volatility), so crossing zero is a non-event. Shifted lognormal vol depends on $F + s$, which creates level-dependence and potential instability if $F$ approaches $-s$. For a desk operating in a negative-rate environment with rates that may oscillate around zero, normal vol is the clearly superior choice for stability.

---

**Exercise 6.** In the shifted SABR model, the forward rate dynamics are $dF = \sigma_{\text{SLN}}(F + s)^\beta\,dW$ with $\beta = 0.5$ and $s = 2\%$. For $F = 0.3\%$ and $\sigma_{\text{SLN}} = 40\%$, compute the local volatility at $F$ and compare it with the $\beta = 1$ (pure shifted lognormal) and $\beta = 0$ (pure normal) cases. Discuss how $\beta$ controls the smile shape.

??? success "Solution to Exercise 6"

    **Parameters:** $F = 0.003$, $s = 0.02$, so $F + s = 0.023$, and $\sigma_{\text{SLN}} = 0.40$.

    The shifted SABR local volatility at the current forward level is given by the diffusion coefficient:

    $$
    \text{Local vol}(F) = \sigma_{\text{SLN}} \cdot (F + s)^\beta
    $$

    (Here $\sigma_{\text{SLN}}$ plays the role of the SABR $\alpha$ parameter, the initial stochastic volatility level.)

    **Case $\beta = 0.5$:**

    $$
    \text{Local vol} = 0.40 \times (0.023)^{0.5} = 0.40 \times 0.15166 = 0.06066
    $$

    So the local volatility is approximately **6.07%** (or equivalently, 607 bps in absolute terms applied to the shifted rate raised to the power 0.5).

    **Case $\beta = 1$ (pure shifted lognormal):**

    $$
    \text{Local vol} = 0.40 \times (0.023)^{1} = 0.40 \times 0.023 = 0.0092
    $$

    The local volatility is **0.92%** (92 bps absolute).

    **Case $\beta = 0$ (pure normal):**

    $$
    \text{Local vol} = 0.40 \times (0.023)^{0} = 0.40 \times 1 = 0.40
    $$

    The local volatility is **40%** (which, in the $\beta = 0$ case, is really $\alpha = \sigma_N = 40\%$ --- this would correspond to a normal vol of 4000 bps, which is unrealistically high; in practice, $\alpha$ would be recalibrated to a much smaller value for $\beta = 0$).

    **How $\beta$ controls the smile:**

    The parameter $\beta$ determines the **rate-level dependence** of volatility, which directly controls the **skew** of the implied volatility smile:

    - $\beta = 1$: Volatility is proportional to the shifted rate. This produces a smile with a particular skew pattern (negative normal vol skew, roughly flat shifted Black vol skew).
    - $\beta = 0$: Volatility is independent of the rate level. This produces a smile with a different skew (roughly flat normal vol, positive shifted Black vol skew).
    - $\beta = 0.5$: Intermediate behavior --- volatility scales as the square root of the shifted rate. The skew is between the two extremes.

    In general, higher $\beta$ produces more negative skew in normal vol terms (OTM receivers are more expensive relative to OTM payers), while lower $\beta$ flattens the normal vol smile. The choice of $\beta$ is often fixed (e.g., $\beta = 0.5$ is common in rates) and the remaining SABR parameters ($\alpha$, $\rho$, $\nu$) are calibrated to the market smile.

---

**Exercise 7.** A risk manager compares the delta of an ATM swaption under the normal model versus the lognormal model. In the normal model, delta is $\partial V / \partial F = \delta\,P\,N(d)$, while in the lognormal model it is $\partial V / \partial F = \delta\,P\,N(d_1)$. For $F = 2\%$, $\sigma_N = 0.60\%$, $\sigma_{\text{LN}} = 30\%$, and $T = 5$, compute both deltas and the difference. Does the choice of model materially affect the hedge ratio?

??? success "Solution to Exercise 7"

    **Parameters:** $F = K = 0.02$ (ATM), $\sigma_N = 0.006$, $\sigma_{\text{LN}} = 0.30$, $T = 5$.

    **Normal model delta:** For the ATM Bachelier model, $d = (F - K)/(\sigma_N\sqrt{T}) = 0$, so:

    $$
    \Delta_N = \delta\,P\,N(0) = \delta\,P \times 0.5
    $$

    **Lognormal model delta:** For the ATM Black model:

    $$
    d_1 = \frac{\ln(F/K) + \frac{1}{2}\sigma_{\text{LN}}^2 T}{\sigma_{\text{LN}}\sqrt{T}} = \frac{0 + \frac{1}{2}(0.09)(5)}{0.30\sqrt{5}} = \frac{0.225}{0.6708} = 0.33541
    $$

    $$
    \Delta_{\text{LN}} = \delta\,P\,N(d_1) = \delta\,P\,N(0.33541) = \delta\,P \times 0.6313
    $$

    **Difference:**

    $$
    \Delta_{\text{LN}} - \Delta_N = \delta\,P\,(0.6313 - 0.5000) = 0.1313\,\delta\,P
    $$

    In relative terms, the lognormal delta is about **26.3%** larger than the normal delta ($0.1313/0.5 = 0.2626$).

    **Does this materially affect the hedge ratio?** Yes, this is a significant difference. For a $\$100$ million notional swaption with $\delta\,P \approx 0.25$:

    $$
    \text{Delta difference} \approx 0.1313 \times 0.25 \times 100{,}000{,}000 = \$3{,}282{,}500
    $$

    This means the lognormal model prescribes hedging with approximately $\$3.3$ million more in the underlying swap than the normal model. The source of the discrepancy is that in the lognormal model, ATM corresponds to $d_1 > 0$ (not $d_1 = 0$) because the lognormal distribution is right-skewed. The median of the lognormal distribution is below its mean, so a call struck at-the-money-forward has $d_1 > 0$.

    For practical hedging, this model-dependent difference in delta is significant and represents genuine **model risk**. The correct delta lies somewhere between the two values, and the trader must decide which distributional assumption better reflects reality. In practice, the normal model delta is often considered more robust in low-rate environments, while the lognormal delta may be more appropriate when rates are comfortably positive.
