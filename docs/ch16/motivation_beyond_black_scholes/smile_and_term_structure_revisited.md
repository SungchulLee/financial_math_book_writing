# Smile and Term Structure Revisited

One of the most visible failures of the Black–Scholes model is the presence of a **volatility smile** and a non-flat **term structure of implied volatility**. These phenomena summarize how markets deviate from constant-volatility assumptions and encode rich information about risk-neutral distributions.

> **Cross-reference:** This section builds on the implied volatility concepts developed in Chapter 7. Here we focus on how these phenomena motivate stochastic volatility models.

---

## The Implied Volatility Surface

Given a market price $C^{\text{mkt}}(K, T)$ for a European call option, the **implied volatility** $\sigma_{\text{impl}}(K, T)$ is defined as the unique value solving:

$$
C^{\text{BS}}(S_0, K, T, r, q, \sigma_{\text{impl}}) = C^{\text{mkt}}(K, T).
$$

If the Black–Scholes model were correct, $\sigma_{\text{impl}}(K, T) = \sigma$ would be constant. Instead, market data reveal a two-dimensional surface with systematic patterns.

**Parameterizations:**

Rather than strike $K$, practitioners often use:
- **Log-moneyness:** $k = \log(K/F)$ where $F = S_0 e^{(r-q)T}$ is the forward
- **Delta:** The Black–Scholes delta of the option
- **Standardized moneyness:** $m = k/(\sigma_{\text{ATM}}\sqrt{T})$

---

## Smile Patterns

### Equity Index Smile (Skew)

For equity indices (S&P 500, Euro Stoxx 50), the dominant feature is **negative skew**:

$$
\sigma_{\text{impl}}(K_1) > \sigma_{\text{impl}}(K_2) \quad \text{for } K_1 < K_2.
$$

**Typical characteristics:**

| Feature | S&P 500 (typical) |
|---------|-------------------|
| ATM implied vol | 15%–20% |
| 25-delta put vol | ATM + 3% to 8% |
| 25-delta call vol | ATM − 0.5% to 1% |
| Skew (per 10% moneyness) | 1.5%–4% |

The asymmetry reflects:
1. **Crash risk:** Markets assign higher probability to large downward moves
2. **Leverage effect:** Volatility increases when prices fall
3. **Demand imbalance:** Strong demand for downside protection (puts)

### Single-Stock Smiles

Individual equities exhibit more varied patterns:
- Generally less steep skew than indices
- Can show upward-sloping wings for speculative stocks
- Earnings and events create localized smile distortions

### FX Smiles

Currency options typically show a more symmetric **smile** (not skew):

$$
\sigma_{\text{impl}}(K) \approx \sigma_{\text{ATM}} + a(K - K_{\text{ATM}})^2.
$$

Both OTM puts and OTM calls have elevated implied volatility, reflecting tail risk in both directions.

### Commodity Smiles

Commodities exhibit varied patterns depending on:
- Supply/demand asymmetries
- Storage costs and convenience yields
- Seasonality

---

## Term Structure of Implied Volatility

Implied volatility varies systematically with maturity:

$$
\sigma_{\text{impl}}(T_1) \neq \sigma_{\text{impl}}(T_2) \quad \text{for } T_1 \neq T_2.
$$

### Common Term Structure Shapes

**Upward sloping (contango):** Short-term vol < Long-term vol
- Typical in calm markets
- Reflects uncertainty increasing with horizon
- Mean reversion of volatility is not yet "priced in"

**Downward sloping (backwardation):** Short-term vol > Long-term vol
- Common during stress periods
- Current high volatility expected to mean-revert
- VIX term structure in 2008, 2020 exhibited strong backwardation

**Humped:** Peak at intermediate maturity
- Event risk (earnings, elections) at specific dates
- Regulatory deadlines or macro announcements

### Quantitative Relationships

For ATM options, empirical regularities include:

**Variance additivity (approximately):**
$$
\sigma_{\text{impl}}^2(T) \cdot T \approx \int_0^T \mathbb{E}^{\mathbb{Q}}[V_s]\,ds
$$

**Mean reversion signature:**
Under a mean-reverting volatility process with speed $\kappa$ and long-run level $\bar{\sigma}$:
$$
\sigma_{\text{impl}}^2(T) \approx V_0 \cdot \frac{1 - e^{-\kappa T}}{\kappa T} + \bar{\sigma}^2 \cdot \left(1 - \frac{1 - e^{-\kappa T}}{\kappa T}\right)
$$

This interpolates between $V_0$ (short term) and $\bar{\sigma}^2$ (long term).

---

## Joint Smile-Term Structure Dynamics

The smile and term structure interact in important ways:

### Smile Flattening with Maturity

Short-maturity smiles are typically steeper than long-maturity smiles:

$$
\left|\frac{\partial \sigma_{\text{impl}}}{\partial k}\right|_{T=0.1} > \left|\frac{\partial \sigma_{\text{impl}}}{\partial k}\right|_{T=1.0}
$$

**Scaling relationship:** Under diffusion models, the skew scales approximately as:

$$
\text{Skew}(T) \propto \frac{1}{\sqrt{T}}
$$

### Smile Dynamics

As the underlying moves, the smile shifts. Two limiting cases:

**Sticky strike:** $\sigma_{\text{impl}}(K, t)$ remains constant for fixed $K$
- Implies: as $S$ moves, the smile "slides" along the strike axis
- Inconsistent with most stochastic volatility models

**Sticky delta:** $\sigma_{\text{impl}}(\Delta, t)$ remains constant for fixed $\Delta$
- Implies: the smile moves with the forward
- More consistent with floating smile models

Empirically, reality lies between these extremes and varies by market regime.

---

## Economic Interpretation

The implied volatility surface encodes market beliefs and risk premia:

### Risk-Neutral Density

The Breeden–Litzenberger formula (Chapter 7) recovers the risk-neutral density:

$$
f^{\mathbb{Q}}(S_T = K) = e^{rT} \frac{\partial^2 C}{\partial K^2}\bigg|_{K}.
$$

A non-flat smile implies a non-Gaussian risk-neutral density:
- Steep put skew → heavy left tail → crash risk priced
- Elevated wings → fat tails → extreme moves priced

### Variance Risk Premium

The gap between implied and realized variance:

$$
VRP = \mathbb{E}^{\mathbb{Q}}[\sigma^2] - \mathbb{E}^{\mathbb{P}}[\sigma^2]
$$

is typically positive for equity indices (investors pay a premium for volatility protection). The term structure of VRP reveals:
- Short-term VRP tends to be larger
- VRP increases during stress
- Mean reversion of VRP itself

### Demand and Supply

The smile also reflects market microstructure:
- Institutional demand for OTM puts (portfolio insurance)
- Market makers' inventory and hedging costs
- Flow imbalances in specific strikes/maturities

---

## Implications for Stochastic Volatility Models

A viable stochastic volatility model must explain:

| Feature | Model requirement |
|---------|-------------------|
| Smile existence | Non-constant instantaneous volatility |
| Negative equity skew | Negative price-vol correlation ($\rho < 0$) |
| Smile curvature | Volatility of volatility ($\xi > 0$) |
| Skew decay with $T$ | Mean reversion of volatility |
| Term structure | Realistic volatility dynamics |

The Heston model (Section 9.3) addresses all these through:
- Stochastic variance $V_t$
- Correlation $\rho$ (skew)
- Vol-of-vol $\xi$ (curvature)
- Mean reversion $\kappa$ (term structure)

---

## Empirical Smile: S&P 500 Example

**Representative 1-month smile (normal conditions):**

| Strike (% of spot) | Implied Vol |
|-------------------|-------------|
| 90% | 22% |
| 95% | 18% |
| 100% (ATM) | 15% |
| 105% | 14% |
| 110% | 13.5% |

**Representative term structure (ATM):**

| Maturity | Implied Vol |
|----------|-------------|
| 1 week | 14% |
| 1 month | 15% |
| 3 months | 16% |
| 6 months | 17% |
| 1 year | 18% |
| 2 years | 19% |

These patterns vary with market conditions but the qualitative features persist.

---

## Key Takeaways

- The volatility smile is ubiquitous and persistent across asset classes
- Equity indices exhibit negative skew; FX shows more symmetric smiles
- Term structure reflects volatility mean reversion and risk premia
- Short-maturity smiles are steeper than long-maturity smiles
- The smile encodes risk-neutral beliefs about tail risk
- Any realistic model must explain smile, skew, and term structure jointly

---

## Further Reading

- Rubinstein, M. (1994). *Implied binomial trees*. Journal of Finance.
- Gatheral, J. (2006). *The Volatility Surface: A Practitioner's Guide*. Wiley.
- Carr, P. & Wu, L. (2009). *Variance risk premiums*. Review of Financial Studies.
- Bates, D. (2000). *Post-'87 crash fears in the S&P 500 futures options market*. Journal of Econometrics.
- Cont, R. & da Fonseca, J. (2002). *Dynamics of implied volatility surfaces*. Quantitative Finance.
