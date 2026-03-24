# SABR Greeks (Analytical)

Hedging options under the SABR model requires computing price sensitivities --- the **Greeks** --- that account for the fact that implied volatility itself changes when the forward moves. Unlike Black--Scholes, where the implied volatility is treated as constant, the SABR model provides an explicit dependence $\sigma_B(F, K; \alpha, \beta, \rho, \nu)$, and the chain rule through this dependence produces Greeks that differ materially from their Black--Scholes counterparts. This section derives the SABR delta, vega, and the second-order Greeks (vanna and volga) by differentiating the Hagan formula, presents the Bartlett correction for improved delta hedging, and discusses the practical implications for risk management.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Apply the chain rule to compute Greeks through the Hagan implied volatility formula
    2. Derive the SABR delta and compare it with the Black--Scholes delta
    3. Compute vega, vanna, and volga analytically
    4. Explain the Bartlett (2006) correction and its impact on hedging
    5. Identify the dominant Greeks for different option positions

---

## The Chain Rule Structure

### Option Price as a Composite Function

Under the SABR model, a European option price is computed in two steps:

1. The Hagan formula maps parameters to implied volatility: $\sigma_B = \sigma_B(F, K; \alpha, \beta, \rho, \nu, T)$
2. The Black formula maps implied volatility to price: $C = C_{\text{Black}}(F, K, T, \sigma_B)$

The option price is therefore a **composite function** $C = C_{\text{Black}}(F, K, T, \sigma_B(F, K; \cdot))$. The Greeks are computed by the chain rule through this composition.

### Total Derivative with Respect to Forward

The total derivative of the call price with respect to the forward $F$ is:

$$
\frac{dC}{dF} = \frac{\partial C_{\text{Black}}}{\partial F}\bigg|_{\sigma_B} + \frac{\partial C_{\text{Black}}}{\partial \sigma_B}\cdot\frac{\partial \sigma_B}{\partial F}
$$

The first term is the standard **Black delta** computed at the SABR implied volatility. The second term is the **smile adjustment** --- the correction arising from the fact that implied volatility changes when the forward moves.

!!! info "Key Principle"
    Every SABR Greek consists of a **Black Greek** (computed at the SABR implied vol) plus a **smile correction** involving the sensitivity of $\sigma_B$ to the relevant parameter. The smile correction is often the dominant term for delta and can be significant for other Greeks as well.

---

## SABR Delta

### Definition and Formula

The SABR delta is the total sensitivity of the option price to the forward:

$$
\Delta_{\text{SABR}} = \frac{\partial C_{\text{Black}}}{\partial F}\bigg|_{\sigma_B} + \frac{\partial C_{\text{Black}}}{\partial \sigma_B}\cdot\frac{\partial \sigma_B}{\partial F}
$$

$$
= \Delta_{\text{Black}}(\sigma_B) + \mathcal{V}_{\text{Black}}(\sigma_B)\cdot\frac{\partial \sigma_B}{\partial F}
$$

where $\Delta_{\text{Black}}$ is the Black delta and $\mathcal{V}_{\text{Black}}$ is the Black vega, both evaluated at $\sigma_B$.

The sensitivity $\partial\sigma_B/\partial F$ comes from differentiating the Hagan formula. At the money ($K = F$), this simplifies to:

$$
\frac{\partial\sigma_B}{\partial F}\bigg|_{K=F} \approx -\frac{(1-\beta)\alpha}{F^{2-\beta}} + O(\nu)
$$

The leading term is the **backbone contribution** from the CEV exponent. The full expression includes terms involving $\rho$ and $\nu$ that arise from the smile factor $z/x(z)$ and the time correction.

### Comparison with Black Delta

For an ATM call with $\beta < 1$ and $\rho < 0$:

| Delta Type | Typical Value | Source |
|------------|---------------|--------|
| $\Delta_{\text{Black}}$ at $\sigma_B$ | 0.50 | Standard Black formula |
| Smile correction | $-0.02$ to $-0.05$ | Backbone + correlation |
| $\Delta_{\text{SABR}}$ | 0.45--0.48 | Sum of above |

The SABR delta is typically **lower** than the Black delta for ATM calls when $\beta < 1$, because an increase in $F$ reduces the implied volatility (via the backbone), which reduces the call price.

### The Bartlett Correction

Bartlett (2006) showed that the standard SABR delta (differentiating the Hagan formula with respect to $F$ while holding $\alpha$ fixed) is **inconsistent** with the model dynamics. The reason is that in the SABR model, the volatility $\sigma_t$ is correlated with $F_t$ through $\rho$, so when $F$ moves, $\sigma$ also moves on average.

The **Bartlett-corrected delta** accounts for the conditional expectation of the volatility change:

$$
\Delta_{\text{Bartlett}} = \Delta_{\text{SABR}} + \mathcal{V}_{\text{Black}}\cdot\frac{\partial\sigma_B}{\partial\alpha}\cdot\frac{\rho\nu}{F^{\beta}}
$$

The additional term represents the expected change in $\alpha$ given a change in $F$, projected through the chain rule. The Bartlett correction is:

$$
\frac{d\alpha}{dF} = \frac{\rho\nu}{F^{\beta}}
$$

which follows from the instantaneous correlation structure: when $F$ increases by $dF = \sigma F^{\beta}\,dW^{(1)}$, the expected change in $\sigma$ is $\rho\nu\sigma\,dW^{(1)}\cdot(\text{coefficient})$.

!!! tip "Bartlett Delta in Practice"
    The Bartlett correction is small for $|\rho| \leq 0.2$ but significant for $|\rho| \geq 0.5$. In interest rate markets where $\rho \in [-0.7, -0.3]$, the Bartlett correction reduces the delta by 2--5% for ATM swaptions, leading to measurably better hedging performance. Most quant libraries now implement the Bartlett correction by default.

---

## SABR Vega

### Definition

The SABR vega measures sensitivity to the initial volatility parameter $\alpha$:

$$
\mathcal{V}_{\text{SABR}} = \frac{dC}{d\alpha} = \frac{\partial C_{\text{Black}}}{\partial\sigma_B}\cdot\frac{\partial\sigma_B}{\partial\alpha}
$$

The derivative $\partial\sigma_B/\partial\alpha$ from the Hagan formula is:

$$
\frac{\partial\sigma_B}{\partial\alpha}\bigg|_{K=F} \approx \frac{1}{F^{1-\beta}}\left[1 + \left(\frac{3(1-\beta)^2\alpha^2}{24 F^{2(1-\beta)}} + \frac{\rho\beta\nu}{4 F^{1-\beta}} + \frac{2-3\rho^2}{24}\nu^2\right)T\right]
$$

At the money, this is approximately $1/F^{1-\beta}$ times a correction near 1. So the SABR vega is approximately:

$$
\mathcal{V}_{\text{SABR}} \approx \frac{\mathcal{V}_{\text{Black}}(\sigma_B)}{F^{1-\beta}}
$$

### Vega Risk and Hedging

The SABR vega quantifies how much the option price changes when the overall volatility level shifts. A portfolio that is vega-neutral (hedged against parallel shifts in $\alpha$) is protected against the most common type of volatility move.

---

## Second-Order Greeks: Vanna and Volga

### Vanna

**Vanna** (also called DdeltaDvol) is the cross-derivative of the option price with respect to $F$ and $\sigma_B$:

$$
\text{Vanna} = \frac{\partial^2 C}{\partial F\,\partial\sigma_B} = \frac{\partial\Delta}{\partial\sigma_B} = \frac{\partial\mathcal{V}}{\partial F}
$$

Under SABR, the vanna has contributions from both the Black vanna and the smile:

$$
\text{Vanna}_{\text{SABR}} = \text{Vanna}_{\text{Black}}(\sigma_B) + \text{corrections from } \frac{\partial^2\sigma_B}{\partial F\,\partial\alpha}
$$

Vanna is important for options with significant exposure to the correlation between $F$ and $\sigma$ --- it measures the P&L from simultaneous moves in the forward and volatility.

### Volga

**Volga** (also called vomma or DvegaDvol) is the second derivative with respect to implied volatility:

$$
\text{Volga} = \frac{\partial^2 C}{\partial\sigma_B^2}
$$

Under SABR, volga is:

$$
\text{Volga}_{\text{SABR}} = \text{Volga}_{\text{Black}}(\sigma_B)\cdot\left(\frac{\partial\sigma_B}{\partial\alpha}\right)^2 + \mathcal{V}_{\text{Black}}(\sigma_B)\cdot\frac{\partial^2\sigma_B}{\partial\alpha^2}
$$

Volga measures the convexity of the option price in volatility. Positions with large volga benefit from realized volatility of volatility.

### Sensitivity to Rho and Nu

The sensitivities to $\rho$ and $\nu$ are also important for risk management:

$$
\frac{\partial C}{\partial\rho} = \mathcal{V}_{\text{Black}}(\sigma_B)\cdot\frac{\partial\sigma_B}{\partial\rho}
$$

$$
\frac{\partial C}{\partial\nu} = \mathcal{V}_{\text{Black}}(\sigma_B)\cdot\frac{\partial\sigma_B}{\partial\nu}
$$

where $\partial\sigma_B/\partial\rho$ and $\partial\sigma_B/\partial\nu$ are obtained by differentiating the Hagan formula with respect to $\rho$ and $\nu$ respectively.

---

## Greek Profiles

### Greeks as Functions of Strike

The SABR Greeks vary systematically across strikes:

| Greek | Deep OTM Put | ATM | Deep OTM Call |
|-------|-------------|-----|---------------|
| Delta | Near 0 | $\approx 0.47$ (with backbone) | Near 1 |
| Vega | Small | Maximum | Small |
| Vanna | Negative | Near 0 | Positive |
| Volga | Positive | Minimum | Positive |

The **vanna** changes sign at the money, reflecting the leverage effect: OTM puts have negative vanna (they benefit from the negative forward-vol correlation), while OTM calls have positive vanna.

The **volga** is positive in the wings and minimal at the money. This means wing options are long volatility-of-volatility, which justifies the higher implied volatilities in the wings of the smile.

!!! example "Numerical Greek Calculation"
    **Setup**: $F = 3\%$, $\beta = 0.5$, $\alpha = 0.035$, $\rho = -0.3$, $\nu = 0.4$, $T = 1$Y.

    For an ATM call ($K = F = 3\%$):

    - $\sigma_B^{\text{ATM}} = 20.4\%$
    - $\Delta_{\text{Black}} = 0.500$
    - Smile correction: $\mathcal{V}_{\text{Black}} \times \partial\sigma_B/\partial F = -0.025$
    - $\Delta_{\text{SABR}} = 0.475$
    - Bartlett correction: $-0.015$
    - $\Delta_{\text{Bartlett}} = 0.460$

    The SABR delta is 4 percentage points below the Black delta, and the Bartlett correction adds another 1.5 percentage points. For a \$100M notional swaption, this amounts to a hedge ratio difference of \$5.5M --- far exceeding transaction costs.

---

## Summary

SABR Greeks are computed by applying the chain rule through the Hagan implied volatility formula to the Black pricing formula. The delta includes a **smile correction** from the backbone ($\partial\sigma_B/\partial F$) that typically reduces the delta below the Black value when $\beta < 1$. The **Bartlett correction** further adjusts the delta to account for the instantaneous correlation between $F$ and $\sigma$, improving hedging performance particularly when $|\rho|$ is large. Second-order Greeks --- vanna and volga --- capture the sensitivity to joint forward-volatility moves and volatility-of-volatility, respectively. These are material for risk management of swaption portfolios and form the basis of the vanna-volga pricing method used by many trading desks.

---

## Further Reading

- Bartlett, B. (2006). *Hedging under SABR model*. Wilmott Magazine, July, 2--4.
- Hagan, P. et al. (2002). *Managing smile risk*. Wilmott Magazine, 1, 84--108.
- Rebonato, R. (2004). *Volatility and Correlation*. Wiley, Chapter 13.
- Castagna, A. & Mercurio, F. (2007). *The vanna-volga method for implied volatilities*. RISK, January.

---

## Exercises

**Exercise 1.** The SABR delta is computed via the chain rule:

$$
\Delta_{\text{SABR}} = \Delta_{\text{Black}} + \text{Vega}_{\text{Black}} \cdot \frac{\partial\sigma_B}{\partial F}
$$

For a call with $\Delta_{\text{Black}} = 0.55$, $\text{Vega}_{\text{Black}} = 0.25$, and $\partial\sigma_B/\partial F = -3.5$ (from the Hagan formula), compute $\Delta_{\text{SABR}}$. Is the SABR delta larger or smaller than the Black delta? Explain the sign of the correction.

---

**Exercise 2.** The Bartlett correction further adjusts the delta to account for the instantaneous correlation between $F$ and $\sigma$. The corrected delta is approximately $\Delta_{\text{Bartlett}} = \Delta_{\text{SABR}} + \text{Vega}_{\text{Black}} \cdot \rho\nu/\alpha \cdot (\partial\sigma_B/\partial\alpha)$. Explain intuitively why the Bartlett correction improves hedging performance: when $\rho < 0$ and $F$ drops, $\sigma$ tends to increase simultaneously, and the delta should account for this correlation.

---

**Exercise 3.** The SABR vega $\partial C/\partial\alpha$ measures sensitivity to a parallel shift in the volatility level. Compute it using $\text{Vega}_{\text{SABR}} = \text{Vega}_{\text{Black}} \cdot \partial\sigma_B/\partial\alpha$. For an ATM swaption with $\text{Vega}_{\text{Black}} = 0.30$ and $\partial\sigma_B/\partial\alpha \approx 1/F^{1-\beta}$, compute the SABR vega for $F = 0.03$ and $\beta = 0.5$.

---

**Exercise 4.** Vanna measures the cross-sensitivity $\partial^2 C/(\partial F\,\partial\sigma_B)$. In the SABR model, vanna arises because $\sigma_B$ depends on $F$ through the backbone. Explain why a portfolio that is vanna-neutral is partially protected against simultaneous moves in $F$ and $\sigma$. For a swaption desk with large negative vanna, describe a hedging strategy using other swaptions.

---

**Exercise 5.** Volga measures $\partial^2 C/\partial\sigma_B^2$, the convexity of the option price in volatility. ATM options have small volga, while OTM options have large volga. Explain why this means OTM option prices are more sensitive to the vol-of-vol parameter $\nu$ in the SABR model. How does this connect to the smile curvature?

---

**Exercise 6.** Compare the hedging P&L of three delta strategies over a 1-month horizon: (a) Black delta with constant implied vol; (b) SABR delta (backbone-corrected); (c) Bartlett-corrected SABR delta. If the forward drops from 3% to 2.5% and implied vol increases by 2 vol points, rank the three strategies from best to worst hedging performance. Which correction matters most: the backbone or the Bartlett?
