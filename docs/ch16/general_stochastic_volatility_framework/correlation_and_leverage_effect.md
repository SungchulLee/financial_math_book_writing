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
