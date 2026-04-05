# Correlation and Leverage Effect

A defining feature of equity markets is the **leverage effect**: negative returns are associated with rising volatility. In stochastic volatility models, this is captured by the **correlation** between price and volatility shocks. This single parameter has profound effects on option prices and the shape of implied volatility surfaces.

---

## Correlated Brownian Motions

### Mathematical Setup

In two-factor stochastic volatility models, we allow the driving Brownian motions to be correlated:

$$
d\langle W^S, W^V \rangle_t = \rho\,dt
$$

with correlation coefficient $\rho \in [-1, 1]$.

**Decomposition:** The correlated pair can be written as:

$$
W_t^V = \rho W_t^S + \sqrt{1-\rho^2}\, W_t^{\perp}
$$

where $W^S$ and $W^{\perp}$ are independent standard Brownian motions.

**Joint increment distribution:**

$$
\begin{pmatrix} \Delta W^S \\ \Delta W^V \end{pmatrix} \sim \mathcal{N}\left(\begin{pmatrix} 0 \\ 0 \end{pmatrix}, \begin{pmatrix} \Delta t & \rho\Delta t \\ \rho\Delta t & \Delta t \end{pmatrix}\right)
$$

### Instantaneous Covariation

For the Heston model with $dS_t = (r-q)S_t\,dt + \sqrt{V_t}S_t\,dW_t^S$ and $dV_t = \kappa(\theta-V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V$:

$$
d\langle S, V \rangle_t = \rho \xi V_t S_t\,dt
$$

The **instantaneous covariance** between log-returns and variance changes is:

$$
\text{Cov}\left(\frac{dS_t}{S_t}, dV_t\right) = \rho \xi V_t\,dt
$$

---

## The Leverage Effect in Equity Markets

### Empirical Definition

The **leverage effect** refers to the empirically observed negative correlation between equity returns and subsequent volatility changes:

$$
\text{Corr}(r_t, \sigma_{t+\Delta}^2 - \sigma_t^2) < 0
$$

where $r_t$ is the return and $\sigma_t$ is volatility.

### Quantitative Evidence

**Cross-sectional estimates:**

| Market | Correlation estimate | Source |
|--------|---------------------|--------|
| S&P 500 index | $-0.7$ to $-0.8$ | Bouchaud et al. |
| Individual US stocks | $-0.3$ to $-0.5$ | Figlewski & Wang |
| Euro Stoxx 50 | $-0.6$ to $-0.7$ | Cont & da Fonseca |
| FX (EUR/USD) | $\approx 0$ | Carr & Wu |
| Commodities | Mixed | Schwartz |

**Key observations:**
- The leverage effect is strongest for equity indices
- Individual stocks show weaker but still negative correlation
- FX markets exhibit near-zero correlation
- Commodities vary by type (energy vs. agricultural)

### Time Scale Dependence

The correlation depends on the measurement horizon:

$$
\rho(\Delta) = \text{Corr}\left(r_{[t, t+\Delta]}, \Delta\sigma_{[t+\Delta, t+2\Delta]}^2\right)
$$

Empirically:
- Strongest at daily/weekly frequencies: $\rho \approx -0.7$
- Weakens at monthly frequencies: $\rho \approx -0.4$
- Near zero at annual frequencies

This suggests the leverage effect is a **short-term** phenomenon.

---

## Economic Explanations

### Balance Sheet Leverage

**Mechanism:** When a firm's equity value falls, its debt-to-equity ratio (leverage) increases, making the firm riskier.

**Formalization:** Let $A = E + D$ be assets, with equity $E$ and debt $D$. If $A$ falls:

$$
\text{Leverage} = \frac{D}{E} \uparrow \quad \Rightarrow \quad \text{Equity volatility} \uparrow
$$

**Critique:** This explains firm-level volatility but less clearly applies to indices or portfolios.

### Volatility Feedback Effect

**Mechanism:** An increase in expected volatility raises the required return, causing prices to fall immediately.

**Formalization:** Under CAPM-type reasoning:

$$
\mathbb{E}[r] = r_f + \lambda \cdot \sigma \quad \Rightarrow \quad \uparrow \sigma \Rightarrow \uparrow \mathbb{E}[r] \Rightarrow \downarrow P_0
$$

**French, Schwert, Stambaugh (1987):** Found evidence consistent with volatility feedback, but the effect is smaller than pure leverage would predict.

### Behavioral Asymmetry

**Mechanism:** Investors react more strongly to losses than gains, causing panic selling during downturns that amplifies volatility.

**Evidence:**
- Volume spikes more during sell-offs
- VIX responds asymmetrically to returns
- Options markets show demand imbalance for puts

### Risk Premium Channel

**Mechanism:** Negative returns signal deteriorating economic conditions, increasing aggregate risk aversion and risk premia, which manifests as higher volatility.

This view connects the leverage effect to macroeconomic fundamentals rather than mechanical leverage.

---

## Impact on Implied Volatility Smile

### Skew Generation

The correlation $\rho$ is the primary determinant of **implied volatility skew**.

**Intuition:** When $\rho < 0$:
- Price falls → Volatility rises → Further price decline more likely
- Price rises → Volatility falls → Further price rise less explosive

This asymmetry makes downward moves more extreme than upward moves, creating a left-skewed return distribution.

### Analytical Approximation

For small vol-of-vol and short maturities, the implied volatility skew can be approximated:

$$
\sigma_{\text{impl}}(k) \approx \sigma_{\text{ATM}} + \text{Skew} \cdot k + \frac{1}{2}\text{Convexity} \cdot k^2
$$

where $k = \log(K/F)$ is log-moneyness.

**First-order expansion (Heston):**

$$
\text{Skew} \approx \frac{\rho \xi}{2\sigma_{\text{ATM}}}
$$

This shows:
- $\text{Skew} \propto \rho$: correlation directly controls skew sign and magnitude
- $\text{Skew} \propto \xi$: higher vol-of-vol amplifies skew
- $\text{Skew} \propto 1/\sigma_{\text{ATM}}$: skew is more pronounced in low-vol environments

### Smile Shape by Correlation

| $\rho$ | Smile shape | Typical market |
|--------|-------------|----------------|
| $\rho < 0$ | Negative skew | Equity indices |
| $\rho \approx 0$ | Symmetric smile | FX |
| $\rho > 0$ | Positive skew | Some commodities |

**Quantitative example (Heston):**

For $\sigma_{\text{ATM}} = 20\%$, $\xi = 30\%$:
- $\rho = -0.7$ → Skew $\approx -5.25\%$ per unit log-moneyness
- $\rho = 0$ → Skew $= 0$
- $\rho = +0.3$ → Skew $\approx +2.25\%$ per unit log-moneyness

---

## Calibration of Correlation

### From Options Data

The correlation $\rho$ can be estimated by:

1. **Fitting the smile:** Minimize implied volatility errors, treating $\rho$ as a free parameter
2. **Skew matching:** Directly match the ATM skew: $\rho \approx \frac{2\sigma_{\text{ATM}} \cdot \text{Skew}}{\xi}$
3. **Risk reversal pricing:** The 25-delta risk reversal price is highly sensitive to $\rho$

### From Historical Data

Direct estimation from returns and realized variance changes:

$$
\hat{\rho} = \frac{\sum_t (r_t - \bar{r})(\Delta RV_t - \overline{\Delta RV})}{\sqrt{\sum_t (r_t - \bar{r})^2 \sum_t (\Delta RV_t - \overline{\Delta RV})^2}}
$$

**Caveat:** Historical $\rho^{\mathbb{P}}$ and risk-neutral $\rho^{\mathbb{Q}}$ may differ due to risk premia.

### Typical Calibrated Values

| Market | $\rho$ from options |
|--------|-------------------|
| S&P 500 | $-0.6$ to $-0.8$ |
| Individual stocks | $-0.3$ to $-0.6$ |
| Euro Stoxx 50 | $-0.5$ to $-0.7$ |
| Nikkei 225 | $-0.4$ to $-0.6$ |
| EUR/USD | $-0.2$ to $+0.2$ |

---

## Dynamic Behavior

### Correlation Stability

Empirical studies find that $\rho$ is relatively stable over time, unlike other parameters:

- Less sensitive to market regime than vol-of-vol
- Consistent sign (negative for equities)
- Magnitude varies within a range but doesn't flip sign

### State Dependence

Some evidence suggests $\rho$ varies with market conditions:

$$
\rho(t) = \rho_0 + \rho_1 \cdot \mathbf{1}_{\text{crisis}}
$$

During crises:
- Correlation may become more negative
- Volatility and returns become more tightly coupled
- Flight-to-quality effects amplify the relationship

---

## Implications for Hedging

### Delta Under Stochastic Volatility

With $\rho \neq 0$, the delta hedge must account for correlation:

$$
\Delta^{\text{SV}} = \frac{\partial C}{\partial S} + \rho \frac{\xi}{\sigma} \frac{\partial C}{\partial V}
$$

The second term corrects for the correlation between price and volatility moves.

### Vanna Exposure

**Vanna** (cross-gamma) measures sensitivity to joint price-volatility moves:

$$
\text{Vanna} = \frac{\partial^2 C}{\partial S \partial \sigma} = \frac{\partial \Delta}{\partial \sigma}
$$

When $\rho < 0$:
- Long OTM puts have positive vanna
- A price drop increases implied vol, which increases delta magnitude
- This amplifies hedging requirements during sell-offs

---

## Key Takeaways

- Correlation between price and volatility shocks is essential in stochastic volatility models
- The leverage effect ($\rho < 0$) is a robust empirical fact for equities
- Negative correlation generates the characteristic negative implied volatility skew
- Skew is approximately linear in $\rho$ for small perturbations
- Multiple economic mechanisms explain the leverage effect
- Calibrated $\rho$ values for equity indices typically range from $-0.6$ to $-0.8$

---

## Further Reading

- Black, F. (1976). *Studies of stock price volatility changes*. Proceedings of the Business and Economics Section, ASA.
- Christie, A. (1982). *The stochastic behavior of common stock variances*. Journal of Financial Economics.
- French, K., Schwert, G., & Stambaugh, R. (1987). *Expected stock returns and volatility*. Journal of Financial Economics.
- Bouchaud, J.-P., Matacz, A., & Potters, M. (2001). *Leverage effect in financial markets*. Physical Review Letters.
- Gatheral, J. (2006). *The Volatility Surface: A Practitioner's Guide*. Wiley.
- Carr, P. & Wu, L. (2007). *Stochastic skew in currency options*. Journal of Financial Economics.

---

## Exercises

**Exercise 1.** Given correlated Brownian motions with $\langle W^S, W^V\rangle_t = \rho t$, use the decomposition $W_t^V = \rho W_t^S + \sqrt{1-\rho^2}\,W_t^{\perp}$ to compute $\text{Var}[W_t^V]$ and $\text{Cov}[W_t^S, W_t^V]$ directly from this representation, confirming that the decomposition correctly reproduces the correlation structure.

??? success "Solution to Exercise 1"
    Using the decomposition $W_t^V = \rho W_t^S + \sqrt{1-\rho^2}\,W_t^{\perp}$ where $W^S$ and $W^{\perp}$ are independent:

    **Variance:**

    $$
    \text{Var}[W_t^V] = \text{Var}\!\left[\rho W_t^S + \sqrt{1-\rho^2}\,W_t^{\perp}\right]
    $$

    By independence of $W^S$ and $W^{\perp}$:

    $$
    = \rho^2\,\text{Var}[W_t^S] + (1-\rho^2)\,\text{Var}[W_t^{\perp}] = \rho^2 t + (1-\rho^2)t = t
    $$

    This confirms $W_t^V$ is a standard Brownian motion.

    **Covariance:**

    $$
    \text{Cov}[W_t^S, W_t^V] = \text{Cov}\!\left[W_t^S, \rho W_t^S + \sqrt{1-\rho^2}\,W_t^{\perp}\right]
    $$

    $$
    = \rho\,\text{Cov}[W_t^S, W_t^S] + \sqrt{1-\rho^2}\,\text{Cov}[W_t^S, W_t^{\perp}]
    $$

    Since $W^S$ and $W^{\perp}$ are independent, $\text{Cov}[W_t^S, W_t^{\perp}] = 0$:

    $$
    = \rho \cdot t + 0 = \rho t
    $$

    Therefore $\text{Corr}[W_t^S, W_t^V] = \rho t / \sqrt{t \cdot t} = \rho$, confirming the decomposition correctly reproduces the correlation structure.

---

**Exercise 2.** In the Heston model with parameters $\sigma_{\text{ATM}} = 20\%$, $\xi = 0.35$, and $\rho = -0.65$, use the first-order skew approximation

$$
\text{Skew} \approx \frac{\rho\xi}{2\sigma_{\text{ATM}}}
$$

to estimate the implied volatility skew per unit log-moneyness. If the 90% strike corresponds to $k = \log(0.90) \approx -0.105$, estimate the implied volatility at the 90% strike. Compare with the case $\rho = 0$ and comment on the magnitude of the leverage effect.

??? success "Solution to Exercise 2"
    Applying the first-order skew approximation with $\sigma_{\text{ATM}} = 0.20$, $\xi = 0.35$, and $\rho = -0.65$:

    $$
    \text{Skew} \approx \frac{\rho\xi}{2\sigma_{\text{ATM}}} = \frac{(-0.65)(0.35)}{2 \times 0.20} = \frac{-0.2275}{0.40} = -0.569
    $$

    The skew is approximately $-0.569$ per unit log-moneyness.

    For the 90% strike with $k = \log(0.90) \approx -0.105$:

    $$
    \sigma_{\text{impl}}(k) \approx \sigma_{\text{ATM}} + \text{Skew} \cdot k = 0.20 + (-0.569)(-0.105) = 0.20 + 0.0597 \approx 25.97\%
    $$

    When $\rho = 0$, $\text{Skew} = 0$ and $\sigma_{\text{impl}}(-0.105) \approx 20\%$ (flat smile at first order).

    The difference is approximately 6 percentage points of implied volatility at the 90% strike. This demonstrates the substantial effect of the leverage effect: the negative correlation between price and volatility shocks inflates the implied volatility of out-of-the-money puts by nearly 30% relative to ATM levels.

---

**Exercise 3.** The balance-sheet leverage explanation predicts that if a firm's assets drop by 10% and debt is fixed at $D$, the new leverage ratio $D/(E - 0.10 A)$ increases. For a firm with $A = 100$, $D = 60$, $E = 40$, compute the percentage increase in the leverage ratio when assets drop by 5%, 10%, and 20%. Explain why this mechanism implies a nonlinear (convex) relationship between returns and volatility changes.

??? success "Solution to Exercise 3"
    Initial values: $A = 100$, $D = 60$, $E = 40$, so initial leverage $= D/E = 60/40 = 1.5$.

    When assets drop, equity absorbs the loss (debt is fixed):

    **5% asset drop:** $A' = 95$, $E' = 95 - 60 = 35$, leverage $= 60/35 \approx 1.714$. Percentage increase: $(1.714 - 1.5)/1.5 \approx 14.3\%$.

    **10% asset drop:** $A' = 90$, $E' = 90 - 60 = 30$, leverage $= 60/30 = 2.0$. Percentage increase: $(2.0 - 1.5)/1.5 \approx 33.3\%$.

    **20% asset drop:** $A' = 80$, $E' = 80 - 60 = 20$, leverage $= 60/20 = 3.0$. Percentage increase: $(3.0 - 1.5)/1.5 = 100\%$.

    The leverage ratio as a function of the asset return $r_A$ is:

    $$
    L(r_A) = \frac{D}{E + r_A \cdot A} = \frac{60}{40 + 100 r_A}
    $$

    This is a **convex** function of $r_A$ (since $L''(r_A) > 0$). As a result, the leverage increase from a negative return is always larger in magnitude than the leverage decrease from an equally sized positive return. Since equity volatility scales with leverage (equity is a leveraged claim on assets), this convexity implies that volatility increases from negative returns exceed the volatility decreases from positive returns of the same magnitude. This nonlinearity is a key feature of the balance-sheet leverage explanation.

---

**Exercise 4.** The following calibrated correlation values are obtained from equity index options:

| Index | $\rho$ |
|-------|--------|
| S&P 500 | $-0.72$ |
| FTSE 100 | $-0.68$ |
| Nikkei 225 | $-0.55$ |
| DAX | $-0.65$ |

For each index, predict the sign and relative steepness of the implied volatility skew. Which index would you expect to have the steepest skew, and why? Why might the Nikkei 225 have a less negative $\rho$ than the S&P 500?

??? success "Solution to Exercise 4"
    Since $\text{Skew} \approx \rho\xi/(2\sigma_{\text{ATM}})$, more negative $\rho$ produces steeper negative skew. All four indices have $\rho < 0$, so all exhibit negative implied volatility skew (OTM puts more expensive than OTM calls).

    **Ranking by skew steepness** (most to least steep, assuming similar $\xi$ and $\sigma_{\text{ATM}}$):

    1. **S&P 500** ($\rho = -0.72$): steepest skew
    2. **FTSE 100** ($\rho = -0.68$): second steepest
    3. **DAX** ($\rho = -0.65$): third
    4. **Nikkei 225** ($\rho = -0.55$): least steep

    The S&P 500 has the steepest skew because it has the most negative correlation, meaning the leverage effect is strongest.

    The Nikkei 225 may have a less negative $\rho$ than the S&P 500 for several reasons:

    - **Market structure:** The Japanese equity market has different investor composition, with large institutional cross-holdings that may dampen feedback effects
    - **Corporate leverage:** Japanese firms may have different capital structures affecting the balance-sheet leverage channel
    - **Currency effects:** The yen tends to appreciate during equity sell-offs, partially offsetting the leverage effect for international investors
    - **Policy intervention:** The Bank of Japan's active role in equity markets (ETF purchases) may reduce the asymmetric volatility response

---

**Exercise 5.** The stochastic-volatility delta is given by

$$
\Delta^{\text{SV}} = \frac{\partial C}{\partial S} + \rho\frac{\xi}{\sigma}\frac{\partial C}{\partial V}
$$

For an ATM call with Black–Scholes delta $\partial C/\partial S = 0.52$, vega sensitivity $\partial C/\partial V = 15$, $\rho = -0.7$, $\xi = 0.3$, and $\sigma = 0.20$, compute the stochastic-volatility delta. Is it larger or smaller than the Black–Scholes delta? Interpret the sign of the correction term.

??? success "Solution to Exercise 5"
    Computing the stochastic-volatility delta:

    $$
    \Delta^{\text{SV}} = \frac{\partial C}{\partial S} + \rho\frac{\xi}{\sigma}\frac{\partial C}{\partial V}
    $$

    Substituting the given values:

    $$
    \Delta^{\text{SV}} = 0.52 + (-0.7) \times \frac{0.3}{0.20} \times 15 = 0.52 + (-0.7)(1.5)(15) = 0.52 - 15.75
    $$

    This result appears too large because $\partial C/\partial V = 15$ is likely expressed in terms of **dollar vega** (price change per unit change in variance). To interpret correctly, we need consistent units. Assuming $\partial C/\partial V$ is the sensitivity per unit variance (dimensionless in the context of the option price relative to the stock price), the correction term is:

    $$
    \text{Correction} = (-0.7) \times \frac{0.3}{0.20} \times 15 = -15.75
    $$

    However, if $\partial C/\partial V$ is in the standard vega convention (price change per 0.01 change in volatility, or per unit change in variance where $V \sim 0.04$), we should note the scale. Taking the formula at face value with the given numbers:

    $$
    \Delta^{\text{SV}} = 0.52 + (-0.7) \times 1.5 \times 15 = 0.52 - 15.75
    $$

    This suggests the units of $\partial C/\partial V$ need to be small. If instead $\partial C/\partial V = 0.15$ (per unit variance, normalized to stock price), then:

    $$
    \Delta^{\text{SV}} = 0.52 + (-0.7)(1.5)(0.15) = 0.52 - 0.1575 = 0.3625
    $$

    The stochastic-volatility delta ($\approx 0.36$) is **smaller** than the Black–Scholes delta (0.52).

    **Interpretation:** The correction term is negative because $\rho < 0$ and $\partial C/\partial V > 0$ (calls gain value when volatility rises). When $\rho < 0$, a price increase tends to coincide with a volatility decrease, which partially offsets the call's price increase. The hedge ratio accounts for this by reducing the delta — fewer shares are needed because the correlated volatility decline dampens the option's price response.

---

**Exercise 6.** Explain why the leverage effect is observed at daily and weekly frequencies but weakens at annual frequencies. Consider a mean-reverting volatility process $dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V$ with $\kappa = 3.0$. Compute the half-life $t_{1/2} = \ln(2)/\kappa$ of volatility shocks. How does this half-life relate to the time-scale dependence of the leverage effect?

??? success "Solution to Exercise 6"
    The half-life of volatility shocks in the mean-reverting process $dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V$ is:

    $$
    t_{1/2} = \frac{\ln 2}{\kappa} = \frac{0.693}{3.0} \approx 0.231 \text{ years} \approx 58 \text{ days}
    $$

    This means that a volatility shock decays to half its initial magnitude in about 2 months.

    **Connection to time-scale dependence:** The leverage effect measures the correlation between returns over a horizon $\Delta$ and subsequent volatility changes. At short horizons (daily/weekly), a volatility shock triggered by a price drop persists long enough to be measured before it decays. The correlation between the return and the contemporaneous or near-future volatility change is strong.

    At longer horizons (monthly/annual), the measurement window spans multiple half-lives of volatility. A volatility spike induced by a price drop at the beginning of the period has largely mean-reverted by the end. The return over the full period aggregates many small shocks, and the net volatility change is dominated by mean reversion rather than the correlation effect.

    Formally, for a horizon $\Delta$ much larger than $t_{1/2}$, the change $V_{t+\Delta} - V_t$ is driven primarily by mean reversion toward $\theta$, which is independent of the return $r_{[t, t+\Delta]}$. For $\Delta \ll t_{1/2}$, the correlation structure of the diffusions dominates, and the leverage effect is fully visible.

    With $t_{1/2} \approx 58$ days, the leverage effect should be clearly visible at daily and weekly frequencies but substantially attenuated at quarterly and annual frequencies, consistent with empirical observations.

---

**Exercise 7.** Consider an FX market (e.g., EUR/USD) where the empirical price-volatility correlation is $\rho \approx 0$. Using the skew formula $\text{Skew} \approx \rho\xi/(2\sigma_{\text{ATM}})$, what implied volatility pattern would you predict? How does this differ from equity markets? Explain why FX markets tend to show a more symmetric smile rather than a skew, and relate this to the absence of a "leverage effect" in currency markets.

??? success "Solution to Exercise 7"
    With $\rho \approx 0$, the skew formula gives:

    $$
    \text{Skew} \approx \frac{0 \cdot \xi}{2\sigma_{\text{ATM}}} = 0
    $$

    The first-order skew vanishes, predicting a **symmetric** implied volatility pattern. The remaining smile shape is determined by higher-order terms (convexity from vol-of-vol $\xi$), producing a U-shaped **smile** that is approximately symmetric around ATM.

    This differs from equity markets where $\rho \approx -0.7$ produces a pronounced negative skew (downward-sloping from OTM puts to OTM calls).

    **Why FX markets lack a leverage effect:**

    1. **No balance-sheet leverage channel:** Currencies are not claims on levered firms. A depreciation of EUR/USD does not mechanically increase the "leverage" of the euro, unlike a stock price decline increasing a firm's debt-to-equity ratio.

    2. **Symmetry of positions:** In FX, being long EUR/USD is equivalent to being short USD/EUR. A decline in EUR/USD is a rise in USD/EUR. There is no inherent asymmetry — one party's loss is another's gain in the same currency pair, so there is no systematic directional bias in volatility response.

    3. **No volatility feedback:** Unlike equities where higher volatility raises required returns and depresses prices, there is no clear mechanism by which currency volatility feeds back asymmetrically into the exchange rate.

    4. **Institutional demand:** Equity markets have systematic demand for downside protection (put buying), which inflates OTM put prices and creates apparent negative skew. FX markets have more balanced hedging demand on both sides.

    The result is that FX implied volatility surfaces typically show a **smile** (elevated wings on both sides of ATM) rather than a **skew**, and risk reversals (the difference between OTM call and OTM put implied vols) are small and can be positive or negative depending on the currency pair.
