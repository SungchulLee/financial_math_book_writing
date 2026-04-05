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

??? success "Solution to Exercise 1"
    We are given $\Delta_{\text{Black}} = 0.55$, $\text{Vega}_{\text{Black}} = 0.25$, and $\partial\sigma_B/\partial F = -3.5$. The SABR delta is:

    $$
    \Delta_{\text{SABR}} = \Delta_{\text{Black}} + \text{Vega}_{\text{Black}} \cdot \frac{\partial\sigma_B}{\partial F}
    $$

    Substituting:

    $$
    \Delta_{\text{SABR}} = 0.55 + 0.25 \times (-3.5) = 0.55 - 0.875 = -0.325
    $$

    Wait --- let us reconsider the units. In interest rate markets, strikes and forwards are in decimal (e.g., $F = 0.03$), and $\partial\sigma_B/\partial F$ has units of (vol / forward), which can be large in absolute terms. However, the vega is typically expressed in price units per unit of volatility. With the values as stated, the smile correction is $-0.875$, which seems very large.

    This highlights an important practical point: the magnitude of $\partial\sigma_B/\partial F$ depends on the convention for $F$. If $F$ is expressed in percentage points (e.g., $F = 3$) rather than decimal ($F = 0.03$), the derivative is 100 times smaller. Assuming the values are given in a consistent unit system, the computation is:

    $$
    \Delta_{\text{SABR}} = 0.55 + 0.25 \times (-3.5) = -0.325
    $$

    However, if the exercise intends $\partial\sigma_B/\partial F = -0.035$ (in decimal forward units with vega in natural units), then:

    $$
    \Delta_{\text{SABR}} = 0.55 + 0.25 \times (-0.035) = 0.55 - 0.00875 \approx 0.541
    $$

    Taking the problem at face value with the given numbers:

    $$
    \Delta_{\text{SABR}} = 0.55 - 0.875 = -0.325
    $$

    The SABR delta is **smaller** than the Black delta. The correction is negative because $\partial\sigma_B/\partial F < 0$: when the forward increases, implied volatility decreases (the backbone effect for $\beta < 1$). This reduction in vol partially offsets the direct increase in the call price from a higher forward, so the true sensitivity of the call to $F$ is lower than the Black delta suggests. Equivalently, the negative skew generated by $\beta < 1$ means that the smile "slides down" as $F$ rises, dampening the option's response to $F$.

---

**Exercise 2.** The Bartlett correction further adjusts the delta to account for the instantaneous correlation between $F$ and $\sigma$. The corrected delta is approximately $\Delta_{\text{Bartlett}} = \Delta_{\text{SABR}} + \text{Vega}_{\text{Black}} \cdot \rho\nu/\alpha \cdot (\partial\sigma_B/\partial\alpha)$. Explain intuitively why the Bartlett correction improves hedging performance: when $\rho < 0$ and $F$ drops, $\sigma$ tends to increase simultaneously, and the delta should account for this correlation.

??? success "Solution to Exercise 2"
    The Bartlett correction addresses a subtle inconsistency in the standard SABR delta. When we compute the SABR delta by differentiating the Hagan formula with respect to $F$ while holding $\alpha$ fixed, we are treating the initial volatility parameter $\alpha$ as independent of $F$. But in the SABR dynamics:

    $$
    dF_t = \sigma_t F_t^{\beta}\,dW_t^{(1)}, \qquad d\sigma_t = \nu\sigma_t\,dW_t^{(2)}, \qquad d\langle W^{(1)}, W^{(2)}\rangle_t = \rho\,dt
    $$

    the Brownian motions $W^{(1)}$ and $W^{(2)}$ are correlated with parameter $\rho$. When $\rho < 0$ and $F$ drops (driven by a negative realization of $W^{(1)}$), the correlated increment in $W^{(2)}$ is on average positive, so $\sigma$ tends to increase. This is the **leverage effect**: falling prices are associated with rising volatility.

    The standard SABR delta ignores this co-movement. The Bartlett correction accounts for it by including the expected change in $\alpha$ given a change in $F$:

    $$
    \frac{d\alpha}{dF} = \frac{\rho\nu}{F^{\beta}}
    $$

    This follows from the instantaneous regression of $d\sigma$ on $dF$. Conditional on a move $dF$, the expected move in $\sigma$ is:

    $$
    \mathbb{E}[d\sigma \mid dF] = \rho\nu\sigma\,\frac{dF}{\sigma F^{\beta}} = \frac{\rho\nu}{F^{\beta}}\,dF
    $$

    The corrected delta is:

    $$
    \Delta_{\text{Bartlett}} = \Delta_{\text{SABR}} + \mathcal{V}_{\text{Black}} \cdot \frac{\partial\sigma_B}{\partial\alpha} \cdot \frac{\rho\nu}{F^{\beta}}
    $$

    **Why this improves hedging**: Consider a scenario where $\rho = -0.5$ and $F$ drops. The standard SABR delta hedge accounts for the change in implied vol due to the backbone (the $F$-dependence of $\sigma_B$ at fixed $\alpha$), but not for the simultaneous increase in $\alpha$ caused by the correlation. The Bartlett correction adds this effect. Since $\rho < 0$, the correction term $\rho\nu/F^{\beta}$ is negative, meaning $\alpha$ decreases when $F$ rises and increases when $F$ falls. This additional vol sensitivity makes the delta more negative (for calls), leading to a hedge that sells more of the underlying. When $F$ drops and vol rises, this more aggressive hedge better captures the combined P&L from both the forward move and the vol move.

    In practice, the Bartlett correction reduces hedging P&L variance by 10--30% for swaptions with $|\rho| > 0.3$, and it is now standard in most quant libraries.

---

**Exercise 3.** The SABR vega $\partial C/\partial\alpha$ measures sensitivity to a parallel shift in the volatility level. Compute it using $\text{Vega}_{\text{SABR}} = \text{Vega}_{\text{Black}} \cdot \partial\sigma_B/\partial\alpha$. For an ATM swaption with $\text{Vega}_{\text{Black}} = 0.30$ and $\partial\sigma_B/\partial\alpha \approx 1/F^{1-\beta}$, compute the SABR vega for $F = 0.03$ and $\beta = 0.5$.

??? success "Solution to Exercise 3"
    We are given $\text{Vega}_{\text{Black}} = 0.30$, $F = 0.03$, and $\beta = 0.5$. The SABR vega is:

    $$
    \mathcal{V}_{\text{SABR}} = \text{Vega}_{\text{Black}} \cdot \frac{\partial\sigma_B}{\partial\alpha}
    $$

    At the money, the leading-order approximation for $\partial\sigma_B/\partial\alpha$ is:

    $$
    \frac{\partial\sigma_B}{\partial\alpha}\bigg|_{K=F} \approx \frac{1}{F^{1-\beta}}
    $$

    With $F = 0.03$ and $\beta = 0.5$:

    $$
    F^{1-\beta} = (0.03)^{0.5} = \sqrt{0.03} \approx 0.17321
    $$

    Therefore:

    $$
    \frac{\partial\sigma_B}{\partial\alpha} \approx \frac{1}{0.17321} \approx 5.774
    $$

    The SABR vega is:

    $$
    \mathcal{V}_{\text{SABR}} = 0.30 \times 5.774 \approx 1.732
    $$

    This means that a 1-unit increase in $\alpha$ produces approximately a 1.732-unit change in the option price. In practice, $\alpha$ is on the order of a few percent (e.g., $\alpha = 0.035$), so a 1 basis point increase in $\alpha$ (i.e., $\Delta\alpha = 0.0001$) changes the option price by approximately $1.732 \times 0.0001 = 0.000173$.

    The factor $1/F^{1-\beta}$ amplifies the SABR vega relative to the Black vega. For small forwards (as in low-rate environments), $F^{1-\beta}$ is small, making $\partial\sigma_B/\partial\alpha$ large. This reflects the fact that the SABR backbone converts $\alpha$ (a normal-like vol parameter) into $\sigma_B$ (a lognormal vol), and the conversion factor $1/F^{1-\beta}$ diverges as $F \to 0$ for $\beta < 1$.

---

**Exercise 4.** Vanna measures the cross-sensitivity $\partial^2 C/(\partial F\,\partial\sigma_B)$. In the SABR model, vanna arises because $\sigma_B$ depends on $F$ through the backbone. Explain why a portfolio that is vanna-neutral is partially protected against simultaneous moves in $F$ and $\sigma$. For a swaption desk with large negative vanna, describe a hedging strategy using other swaptions.

??? success "Solution to Exercise 4"
    **Vanna as a cross-sensitivity**: Vanna measures how much the delta changes when volatility moves, or equivalently, how much the vega changes when the forward moves:

    $$
    \text{Vanna} = \frac{\partial^2 C}{\partial F\,\partial\sigma_B} = \frac{\partial\Delta}{\partial\sigma_B} = \frac{\partial\mathcal{V}}{\partial F}
    $$

    A portfolio with non-zero vanna is exposed to **simultaneous** moves in $F$ and $\sigma$. Under the SABR model, the forward and volatility are correlated (through $\rho$), so these simultaneous moves are the norm, not the exception.

    **Why vanna neutrality provides protection**: If a portfolio is vanna-neutral, its delta does not change when volatility moves, and its vega does not change when the forward moves. This means the portfolio is immunized against the first-order effect of the forward-volatility correlation. When $F$ drops and $\sigma$ rises (as is typical for $\rho < 0$), a vanna-neutral portfolio does not suffer the "double hit" of a worsening delta position compounded by the vol move.

    Formally, consider the second-order Taylor expansion of the P&L:

    $$
    \text{P\&L} \approx \Delta\,\delta F + \mathcal{V}\,\delta\sigma + \tfrac{1}{2}\Gamma\,(\delta F)^2 + \text{Vanna}\,\delta F\,\delta\sigma + \tfrac{1}{2}\text{Volga}\,(\delta\sigma)^2 + \cdots
    $$

    The vanna term $\text{Vanna}\,\delta F\,\delta\sigma$ is the cross term. When $\rho < 0$, $\delta F$ and $\delta\sigma$ tend to have opposite signs, so the sign of the vanna determines whether this cross term helps or hurts. A vanna-neutral portfolio eliminates this term entirely.

    **Hedging strategy for a desk with large negative vanna**: Negative vanna means the portfolio's delta becomes more negative as vol rises (or equivalently, vega decreases as the forward rises). To hedge this:

    1. **Buy OTM calls**: OTM calls have positive vanna (their delta increases with vol), which offsets the negative vanna of the existing portfolio.
    2. **Sell OTM puts**: OTM puts have negative vanna, so selling them adds positive vanna to the portfolio. However, this increases vol-of-vol exposure.
    3. **Risk reversals**: A common structure is to buy OTM calls and sell OTM puts (a risk reversal), which provides a large positive vanna while keeping the vega impact manageable.
    4. **Straddle/strangle adjustments**: Adjusting the strikes of existing hedges can fine-tune the vanna exposure.

    The choice among these strategies depends on the cost (the smile premium for OTM options), the liquidity of the instruments, and the residual exposures (gamma, volga) that the hedge introduces.

---

**Exercise 5.** Volga measures $\partial^2 C/\partial\sigma_B^2$, the convexity of the option price in volatility. ATM options have small volga, while OTM options have large volga. Explain why this means OTM option prices are more sensitive to the vol-of-vol parameter $\nu$ in the SABR model. How does this connect to the smile curvature?

??? success "Solution to Exercise 5"
    **Volga and the vol-of-vol parameter**: Volga measures the convexity of the option price with respect to implied volatility:

    $$
    \text{Volga} = \frac{\partial^2 C}{\partial\sigma_B^2}
    $$

    From the Black formula, the volga of a European option is:

    $$
    \text{Volga}_{\text{Black}} = \mathcal{V}_{\text{Black}} \cdot \frac{d_1 d_2}{\sigma_B}
    $$

    where $d_1$ and $d_2$ are the standard Black formula quantities. At the money, $d_1 \approx \sigma_B\sqrt{T}/2$ and $d_2 \approx -\sigma_B\sqrt{T}/2$, so $d_1 d_2 \approx -\sigma_B^2 T/4 < 0$, making the ATM volga small (and slightly negative for short maturities). For OTM options, both $|d_1|$ and $|d_2|$ are large, and $d_1 d_2 > 0$ (both have the same sign for deep OTM options), making the volga large and positive.

    **Connection to the vol-of-vol parameter $\nu$**: In the SABR model, the vol-of-vol parameter $\nu$ controls how much the stochastic volatility fluctuates. The effect of $\nu$ on the option price operates through the implied volatility smile. An increase in $\nu$ widens the smile (higher implied vols in the wings), which increases OTM option prices more than ATM option prices.

    The sensitivity of the option price to $\nu$ is:

    $$
    \frac{\partial C}{\partial\nu} = \mathcal{V}_{\text{Black}} \cdot \frac{\partial\sigma_B}{\partial\nu}
    $$

    From the Hagan formula, $\partial\sigma_B/\partial\nu$ is larger for OTM options than for ATM options, because $\nu$ primarily affects the curvature of the smile (the quadratic term in the smile expansion). But there is a deeper connection through volga.

    The vanna-volga pricing method shows that, to first order, the price of an exotic option relative to Black--Scholes can be decomposed into:

    $$
    C - C_{\text{BS}} \approx \text{Vanna} \times (\text{smile slope cost}) + \text{Volga} \times (\text{smile curvature cost})
    $$

    The volga term captures the "cost of convexity in vol." Since OTM options have large volga, they benefit disproportionately from vol-of-vol: when $\nu$ is high, realized volatility fluctuates more, and the convexity of the option payoff in vol means the option holder gains more from vol going up than they lose from vol going down. This is Jensen's inequality applied to the vol dimension.

    **Connection to smile curvature**: The smile curvature (the second derivative of $\sigma_B(K)$ with respect to $K$ at the money) is proportional to $\nu^2$ in the Hagan formula. Specifically, from the smile expansion:

    $$
    \sigma_B(K) \approx \sigma_B^{\text{ATM}}\left[1 + b_1\,\ln\frac{K}{F} + b_2\left(\ln\frac{K}{F}\right)^2 + \cdots\right]
    $$

    where $b_2$ depends on $\nu^2$ (among other terms). Higher $\nu$ produces more curvature, which means higher implied vols for OTM options. Options with large volga are precisely those that sit in the wings of the smile, so their prices are most sensitive to $\nu$ because they are most affected by the curvature that $\nu$ generates.

    In summary: OTM options have large volga, meaning their prices are convex in vol. The parameter $\nu$ drives the fluctuation in vol, and by Jensen's inequality, convexity in vol makes these options more valuable when vol fluctuates more. This is reflected in the smile as higher implied vols in the wings when $\nu$ is large.

---

**Exercise 6.** Compare the hedging P&L of three delta strategies over a 1-month horizon: (a) Black delta with constant implied vol; (b) SABR delta (backbone-corrected); (c) Bartlett-corrected SABR delta. If the forward drops from 3% to 2.5% and implied vol increases by 2 vol points, rank the three strategies from best to worst hedging performance. Which correction matters most: the backbone or the Bartlett?

??? success "Solution to Exercise 6"
    **Setup**: The forward drops from $F_0 = 3\%$ to $F_1 = 2.5\%$, so $\delta F = -0.005$. Implied vol increases by 2 vol points: $\delta\sigma_B = +0.02$.

    Consider an ATM call initially hedged with each delta strategy. The hedge consists of selling $\Delta$ units of the forward. The hedging P&L over the period is approximately:

    $$
    \text{P\&L}_{\text{hedge}} = \delta C - \Delta \cdot \delta F
    $$

    where $\delta C$ is the actual change in the option price. The actual change in the option price reflects both the forward move and the vol move:

    $$
    \delta C \approx \Delta_{\text{true}} \cdot \delta F + \mathcal{V} \cdot \delta\sigma_B + \tfrac{1}{2}\Gamma(\delta F)^2 + \text{Vanna}\cdot\delta F\cdot\delta\sigma_B + \cdots
    $$

    The hedging error for a strategy using delta $\hat{\Delta}$ is:

    $$
    \epsilon = \delta C - \hat{\Delta}\cdot\delta F = (\Delta_{\text{true}} - \hat{\Delta})\cdot\delta F + \mathcal{V}\cdot\delta\sigma_B + \text{higher order}
    $$

    The first term is the delta mismatch; the second term (vega P&L) is common to all strategies (since none of them hedge vega). We focus on the delta mismatch.

    **(a) Black delta**: $\hat{\Delta} = \Delta_{\text{Black}} = 0.50$. This ignores both the backbone and the correlation. When $F$ drops, the vol rises, but the Black delta did not anticipate this. The delta mismatch is $\Delta_{\text{true}} - 0.50$, which is significant.

    **(b) SABR delta (backbone-corrected)**: Using the example values from the text, $\hat{\Delta} = \Delta_{\text{SABR}} = 0.475$. This accounts for the backbone (the fact that vol increases when $F$ drops for $\beta < 1$), but not for the correlation-induced change in $\alpha$. The mismatch is smaller: $\Delta_{\text{true}} - 0.475$.

    **(c) Bartlett-corrected delta**: $\hat{\Delta} = \Delta_{\text{Bartlett}} = 0.460$. This accounts for both the backbone and the instantaneous correlation. The mismatch is smallest: $\Delta_{\text{true}} - 0.460$.

    **Ranking from best to worst hedging performance**:

    1. **(c) Bartlett-corrected SABR delta** --- best, because it captures both the backbone and the correlation effect.
    2. **(b) SABR delta** --- second, because it captures the backbone but misses the correlation.
    3. **(a) Black delta** --- worst, because it ignores both effects.

    **Which correction matters most?** In this scenario, the backbone correction reduces the delta from 0.500 to 0.475 (a reduction of 0.025), while the Bartlett correction further reduces it from 0.475 to 0.460 (a reduction of 0.015). The backbone correction is larger in absolute terms and therefore "matters most" for the delta level.

    However, the relative importance depends on the magnitude of $|\rho|$ and $\nu$. For markets with $|\rho| \geq 0.5$ and high vol-of-vol, the Bartlett correction can be comparable to or larger than the backbone correction. In the given scenario (moderate $\rho = -0.3$), the backbone dominates.

    The hedging P&L differences are proportional to $(\Delta_{\text{true}} - \hat{\Delta}) \times \delta F$. With $\delta F = -0.005$:

    - Black hedge error (delta component): $(0.460 - 0.500)\times(-0.005) = +0.0002$
    - SABR hedge error: $(0.460 - 0.475)\times(-0.005) = +0.000075$
    - Bartlett hedge error: $\approx 0$ (by construction)

    For a $\$100$M notional, the Black strategy has a delta hedging error of roughly $\$20{,}000$, the SABR strategy roughly $\$7{,}500$, and the Bartlett strategy is approximately zero (to first order). The backbone correction eliminates about $\$12{,}500$ of the error, while the Bartlett correction eliminates the remaining $\$7{,}500$. Both are significant, but the backbone correction has the larger impact in this parameter regime.
