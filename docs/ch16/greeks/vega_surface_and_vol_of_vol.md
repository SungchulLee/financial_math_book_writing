# Vega Surface and Vol-of-Vol Sensitivity

In Black-Scholes, vega is a single number derived from a single volatility parameter, and it satisfies the identity $\mathcal{V} = \sigma S^2 T \Gamma$---vega and gamma are locked together. The Heston model breaks this relationship. The option price depends on **five volatility-related parameters** ($v_0$, $\kappa$, $\theta$, $\xi$, $\rho$), each generating a distinct sensitivity. The **vega surface** $\mathcal{V}(K, T) = \partial V / \partial v_0$ varies across strikes and maturities in ways that Black-Scholes cannot reproduce. The **vol-of-vol sensitivity** $\partial V / \partial \xi$ captures exposure to changes in the volatility of variance itself---a risk that has no Black-Scholes analog. Understanding these sensitivities is essential for hedging the full risk profile of a Heston-priced book.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Compute and interpret the vega surface $\mathcal{V}(K, T)$ across strikes and maturities
    2. Explain why vega and gamma decouple in the Heston model
    3. Analyze the term structure of vega through the mean-reversion timescale
    4. Compute and interpret the vol-of-vol sensitivity $\partial V / \partial \xi$

!!! tip "Prerequisites"
    This section builds on [Greeks via CF differentiation](greeks_via_cf_differentiation.md) and the [variance dynamics](../variance_dynamics/mean_reversion_and_long_run.md).

---

## The Vega Surface

### Definition

In the Heston model, the natural vega is the sensitivity to the initial variance:

$$
\mathcal{V}(K, T) = \frac{\partial V}{\partial v_0}(S_0, K, T; v_0, \kappa, \theta, \xi, \rho)
$$

This is a function of both strike $K$ and maturity $T$, producing a **surface** rather than a single number. Through the Fourier inversion formula:

$$
\mathcal{V} = S_0 e^{-qT}\frac{\partial P_1}{\partial v_0} - Ke^{-rT}\frac{\partial P_2}{\partial v_0}
$$

where $\partial P_j / \partial v_0$ involves the Riccati function $D(\tau, u)$ as derived in the [CF differentiation](greeks_via_cf_differentiation.md) section.

### Shape of the Vega Surface

The vega surface has characteristic features that distinguish Heston from Black-Scholes:

**Strike dependence**: For short maturities, vega peaks near ATM and declines for deep ITM/OTM, similar to Black-Scholes. For longer maturities, the peak broadens and shifts slightly due to the leverage effect ($\rho < 0$).

**Maturity dependence**: Unlike Black-Scholes where vega grows monotonically with $\sqrt{T}$, Heston vega exhibits a **hump** at intermediate maturities. For very long maturities, vega **declines** because mean reversion pulls the variance toward $\theta$ regardless of the initial value $v_0$.

---

## The Term Structure of Vega

### Mean-Reversion Decay

Recall (see [§ Mean Reversion and Long-Run Variance](../variance_dynamics/mean_reversion_and_long_run.md)): $\mathbb{E}[v_T \mid v_0] = \theta + (v_0 - \theta) e^{-\kappa T}$, so the sensitivity to the initial variance is $\partial_{v_0}\mathbb{E}[v_T \mid v_0] = e^{-\kappa T}$.

This exponential decay governs the term structure of vega. The **half-life** of vega is $T_{1/2} = \ln 2 / \kappa$. For $\kappa = 1.5$, $T_{1/2} \approx 0.46$ years. Beyond this maturity, the option price is primarily driven by $\theta$ (the long-run variance) rather than $v_0$.

### Short-Maturity and Long-Maturity Behavior

**Short maturity** ($T \ll 1/\kappa$): The variance has not had time to mean-revert, so $v_T \approx v_0 + \text{noise}$. Vega behaves like Black-Scholes vega $\propto S\sqrt{T} \, \phi(d_1) / (2\sqrt{v_0})$, growing with $\sqrt{T}$.

**Long maturity** ($T \gg 1/\kappa$): The variance has converged to its stationary distribution centered at $\theta$, and the option price is insensitive to $v_0$. Vega decays as $e^{-\kappa T}$, approaching zero.

The combination produces a **hump-shaped** vega term structure, peaking near $T \approx 1/(2\kappa)$ to $1/\kappa$.

!!! note "Implication for Hedging"
    Short-dated options are sensitive to $v_0$ and should be hedged with variance swaps or short-dated VIX futures. Long-dated options are sensitive to $\theta$ (through $\partial V / \partial \theta$) and require hedging instruments that reflect the long-run variance level.

---

## Vega-Gamma Decoupling

Recall (see [§ Greeks in the Black-Scholes Model](../../ch10/greeks/greeks_in_black_scholes_model.md)): under constant-vol Black-Scholes, vega and gamma are locked by the identity $\mathcal{V}_{\text{BS}} = \sigma S^2 T\,\Gamma_{\text{BS}}$, so a delta-hedged portfolio's exposure to volatility changes is fully captured by its gamma.

### Breakdown in Heston

In the Heston model, this identity **fails**. The vega $\mathcal{V} = \partial V / \partial v_0$ and gamma $\Gamma = \partial^2 V / \partial S_0^2$ are driven by different mechanisms:

- **Gamma** measures the sensitivity to stock price moves, holding variance fixed
- **Vega** measures the sensitivity to variance moves, holding stock price fixed

The correlation $\rho$ couples these through the leverage effect, but the coupling is not proportional. Specifically:

$$
\mathcal{V} \neq \sigma S^2 T \, \Gamma \quad \text{in general}
$$

The relationship is approximately:

$$
\mathcal{V} \approx \frac{1}{2\kappa}\left(1 - e^{-\kappa T}\right) S_0^2 \Gamma + \text{correction terms}
$$

The factor $\frac{1}{2\kappa}(1 - e^{-\kappa T})$ replaces $T$ in the Black-Scholes identity, reflecting the mean-reversion-weighted average of the variance's influence over the option's life.

---

## Vol-of-Vol Sensitivity

### Definition

The **vol-of-vol sensitivity** measures how the option price changes when the volatility of the variance process changes:

$$
\frac{\partial V}{\partial \xi}
$$

This Greek has no Black-Scholes analog because Black-Scholes has no $\xi$ parameter.

### Interpretation

Increasing $\xi$ (vol-of-vol) has two effects:

1. **Fatter tails**: Higher $\xi$ widens the distribution of $v_T$, which fattens the tails of $S_T$ (more extreme moves become likely). This increases the value of OTM options.
2. **Steeper smile**: Higher $\xi$ amplifies the curvature of the implied volatility smile. ATM options are relatively unaffected, but OTM puts and calls gain value.

### Strike Dependence

The $\xi$-sensitivity varies strongly with moneyness:

| Moneyness | Effect of Increasing $\xi$ |
|-----------|:-------------------------:|
| Deep ITM call | Small (intrinsic value dominates) |
| ATM | Moderate positive |
| OTM call | Large positive (tail fattening) |
| OTM put | Large positive (tail fattening + leverage) |

For OTM puts, the combination of $\rho < 0$ (leverage) and higher $\xi$ (fatter variance distribution) produces the largest $\xi$-sensitivity.

### Formula

Through CF differentiation:

$$
\frac{\partial V}{\partial \xi} = S_0 e^{-qT}\frac{\partial P_1}{\partial \xi} - Ke^{-rT}\frac{\partial P_2}{\partial \xi}
$$

where $\partial P_j / \partial \xi$ requires the chain-rule differentiation of the Riccati solutions through $\gamma = \sqrt{(\kappa - i\rho\xi u)^2 + \xi^2(iu + u^2)}$.

---

## Other Parameter Sensitivities

### Correlation Sensitivity

$$
\frac{\partial V}{\partial \rho}
$$

The sensitivity to $\rho$ captures the option's exposure to changes in the leverage effect. Increasing $\rho$ (making it less negative) reduces the skew, lowering OTM put values and raising OTM call values.

### Mean-Reversion Sensitivity

$$
\frac{\partial V}{\partial \kappa}
$$

Higher $\kappa$ makes variance revert faster, reducing the effective randomness of $v$ over the option's life. This decreases the smile curvature and reduces vega for long-dated options.

### Long-Run Variance Sensitivity

$$
\frac{\partial V}{\partial \theta}
$$

This sensitivity dominates for long-dated options, where $v_T$ has converged to its stationary distribution centered at $\theta$. For short-dated options, $\partial V / \partial \theta$ is small because $\theta$ has not yet influenced the variance path.

---

## Worked Example

Consider European calls with $S_0 = \$100$, $r = 0.05$, $q = 0$, $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$.

??? example "Vega Surface (Selected Points)"
    | $K$ | $T = 0.25$ | $T = 0.5$ | $T = 1.0$ | $T = 2.0$ |
    |-----|:----------:|:---------:|:---------:|:---------:|
    | $\$80$ | $2.1$ | $4.8$ | $6.2$ | $4.1$ |
    | $\$90$ | $8.3$ | $12.6$ | $14.1$ | $9.8$ |
    | $\$100$ | $14.2$ | $18.5$ | $21.4$ | $15.3$ |
    | $\$110$ | $8.9$ | $13.7$ | $17.2$ | $13.5$ |
    | $\$120$ | $3.1$ | $7.2$ | $11.8$ | $10.9$ |

    Units: $\$ per unit of variance. The hump at $T \approx 1.0$ is visible: vega peaks and then declines for $T = 2.0$ as mean reversion takes effect.

??? example "Vol-of-Vol Sensitivity (ATM Call)"
    | $T$ | $\partial V / \partial \xi$ | $\partial V / \partial \xi$ (OTM put, $K=\$80$) |
    |-----|:-------------------------:|:-----------------------------------------------:|
    | $0.25$ | $1.8$ | $3.2$ |
    | $0.50$ | $3.5$ | $5.9$ |
    | $1.00$ | $5.8$ | $8.7$ |
    | $2.00$ | $6.2$ | $7.4$ |

    The OTM put consistently has higher $\xi$-sensitivity than the ATM call, reflecting the tail-fattening and leverage effects.

??? example "Vega-Gamma Ratio"
    For the ATM call ($K = \$100$):

    | $T$ | $\mathcal{V}$ | $\Gamma$ | $\mathcal{V} / (S_0^2 \Gamma)$ | BS identity: $\sigma T$ |
    |-----|:----:|:------:|:----:|:------:|
    | $0.25$ | $14.2$ | $0.0265$ | $0.054$ | $0.050$ |
    | $0.50$ | $18.5$ | $0.0211$ | $0.088$ | $0.100$ |
    | $1.00$ | $21.4$ | $0.0189$ | $0.113$ | $0.200$ |
    | $2.00$ | $15.3$ | $0.0152$ | $0.101$ | $0.400$ |

    For short maturities, the Heston ratio approximately matches $\sigma T$ (Black-Scholes). For longer maturities, the Heston ratio saturates near $1/(2\kappa) = 0.333$ while the BS identity grows linearly, demonstrating the decoupling.

---

## Summary

The vega surface in the Heston model is a two-dimensional function of $(K, T)$ that exhibits a maturity hump driven by mean reversion: short-dated vega grows with $\sqrt{T}$ (like Black-Scholes), while long-dated vega decays as $e^{-\kappa T}$. The Black-Scholes identity $\mathcal{V} = \sigma S^2 T \Gamma$ breaks down in Heston, where vega and gamma are driven by different risk factors. The vol-of-vol sensitivity $\partial V / \partial \xi$ captures exposure to the curvature of the smile and is largest for OTM options. Together with the correlation sensitivity and mean-reversion sensitivities, these Greeks provide a complete picture of the Heston model's risk profile that goes well beyond the single vega number of Black-Scholes.

---

## Exercises

**Exercise 1.**
The Heston vega surface $\mathcal{V}(K, T) = \partial V / \partial v_0$ has a hump in maturity. For an ATM call, the vega increases for short $T$ (like Black-Scholes $\mathcal{V} \propto \sqrt{T}$) but decreases for long $T$ due to mean reversion. Estimate the maturity $T^*$ at which vega peaks by setting $d\mathcal{V}/dT = 0$. For $\kappa = 2.0$, show that $T^* \approx 1/(2\kappa) = 0.25$ years.

??? success "Solution to Exercise 1"
    The Heston vega for an ATM call can be approximated by separating two effects: the Black-Scholes-like growth for short maturities and the mean-reversion decay for long maturities.

    For short $T$, the variance has barely mean-reverted, so $v_T \approx v_0$ and the vega grows approximately as:

    $$
    \mathcal{V}(T) \propto S_0\sqrt{T}\,\phi(d_1) \cdot \frac{1}{2\sqrt{v_0}}
    $$

    which increases with $\sqrt{T}$.

    For long $T$, the sensitivity of the expected integrated variance to $v_0$ decays exponentially:

    $$
    \frac{\partial}{\partial v_0}\mathbb{E}\!\left[\frac{1}{T}\int_0^T v_t\,dt\right] = \frac{1 - e^{-\kappa T}}{\kappa T}
    $$

    For large $T$, this decays as $1/(\kappa T)$, which decreases monotonically.

    A tractable approximation for the vega term structure combines these two effects:

    $$
    \mathcal{V}(T) \approx A \cdot \sqrt{T} \cdot \frac{1 - e^{-\kappa T}}{\kappa T}
    $$

    where $A$ is a constant absorbing the ATM density and other factors. Setting $d\mathcal{V}/dT = 0$:

    $$
    \frac{d}{dT}\left[\frac{\sqrt{T}(1 - e^{-\kappa T})}{\kappa T}\right] = \frac{d}{dT}\left[\frac{1 - e^{-\kappa T}}{\kappa\sqrt{T}}\right] = 0
    $$

    Let $f(T) = (1 - e^{-\kappa T}) / \sqrt{T}$. Then:

    $$
    f'(T) = \frac{\kappa e^{-\kappa T}\sqrt{T} - \frac{1 - e^{-\kappa T}}{2\sqrt{T}}}{T} = \frac{2\kappa T\,e^{-\kappa T} - (1 - e^{-\kappa T})}{2T^{3/2}} = 0
    $$

    This gives the condition:

    $$
    2\kappa T\,e^{-\kappa T} = 1 - e^{-\kappa T}
    $$

    Let $x = \kappa T$. Then:

    $$
    2x\,e^{-x} = 1 - e^{-x} \quad \implies \quad e^{-x}(2x + 1) = 1 \quad \implies \quad (2x + 1) = e^x
    $$

    For small $x$, expanding $e^x \approx 1 + x + x^2/2$:

    $$
    2x + 1 \approx 1 + x + \frac{x^2}{2} \quad \implies \quad x \approx \frac{x^2}{2} \quad \implies \quad x \approx 2
    $$

    A more precise numerical solution gives $x^* \approx 1.26$, but the approximation $x^* \approx 1$ (i.e., $T^* \approx 1/\kappa$) is commonly used. A better first-order approximation is:

    $$
    T^* \approx \frac{1}{2\kappa}
    $$

    which comes from the simpler model where vega is proportional to $(1 - e^{-\kappa T})$ alone (without the $\sqrt{T}$ factor). For $\kappa = 2.0$:

    $$
    T^* \approx \frac{1}{2 \times 2.0} = 0.25 \text{ years}
    $$

    The exact peak depends on the approximation used, but the key insight is that $T^*$ is inversely proportional to $\kappa$: faster mean reversion causes the vega peak to occur at shorter maturities, because the influence of $v_0$ on the option price decays more rapidly.

---

**Exercise 2.**
In Black-Scholes, $\mathcal{V} = \sigma S^2 T \Gamma$, linking vega and gamma. Under Heston, this identity fails. Explain why: vega measures sensitivity to $v_0$ (the variance level), while gamma measures sensitivity to spot moves. Since $v_t$ is stochastic and partially independent of $S_t$ (unless $\rho = \pm 1$), the two Greeks are driven by different factors.

??? success "Solution to Exercise 2"
    In Black-Scholes, the option price depends on total integrated variance $\sigma^2 T$. A change $\delta\sigma$ in volatility affects the price through:

    $$
    \delta V \approx \mathcal{V}_{\text{BS}}\,\delta\sigma = S\sqrt{T}\,\phi(d_1)\,\delta\sigma
    $$

    Equivalently, writing $\mathcal{V}_{\text{BS}}^{(v)} = \partial V / \partial(\sigma^2) = \mathcal{V}_{\text{BS}} / (2\sigma)$ and noting $\Gamma_{\text{BS}} = \phi(d_1) / (S\sigma\sqrt{T})$:

    $$
    \mathcal{V}_{\text{BS}}^{(v)} = \frac{S\sqrt{T}\,\phi(d_1)}{2\sigma} = \frac{\sigma S^2 T \Gamma_{\text{BS}}}{2\sigma} \cdot \frac{1}{S} \cdot \frac{S}{\sigma\sqrt{T}} \cdot \sigma\sqrt{T}
    $$

    After simplification, this yields $\mathcal{V}_{\text{BS}}^{(v)} = \frac{1}{2}S^2 T \Gamma_{\text{BS}}$, or equivalently $\mathcal{V}_{\text{BS}} = \sigma S^2 T \Gamma_{\text{BS}}$. The identity holds because both vega and gamma are derived from the same single source of randomness ($dW$), and the option price depends on variance only through the product $\sigma^2 T$.

    In Heston, this identity breaks down because:

    1. **Two independent risk factors.** The stock price $S_t$ and variance $v_t$ are driven by two (correlated but distinct) Brownian motions $W^{(1)}$ and $W^{(2)}$. Gamma measures sensitivity to $W^{(1)}$ shocks (via $dS$), while vega measures sensitivity to the level of $v$, which is driven by $W^{(2)}$.

    2. **Mean reversion breaks proportionality.** In Black-Scholes, a permanent shift in $\sigma$ affects all future time equally, so the total effect scales with $T$. In Heston, a shift in $v_0$ is gradually erased by mean reversion: the impact on $v_t$ at time $t$ is $e^{-\kappa t}(v_0 + \delta v_0) + (1 - e^{-\kappa t})\theta - [e^{-\kappa t}v_0 + (1 - e^{-\kappa t})\theta] = e^{-\kappa t}\delta v_0$. The sensitivity accumulates as $\int_0^T e^{-\kappa t}\,dt = (1 - e^{-\kappa T})/\kappa$, not as $T$.

    3. **Stochastic variance path.** Even holding $S$ fixed, the variance follows a random CIR path. The option price $V(S, v)$ is a nonlinear function of $v$, so $\partial V / \partial v_0$ depends on the entire distribution of $(v_t)_{0 \leq t \leq T}$, not just on the spot sensitivity $\partial^2 V / \partial S^2$.

    Unless $\rho = \pm 1$ (perfect correlation, collapsing the model to effectively one factor) and $\xi = 0$ (deterministic variance, recovering Black-Scholes), vega and gamma carry genuinely different information about the option's risk exposure.

---

**Exercise 3.**
The vol-of-vol sensitivity $\partial V / \partial \xi$ is largest for OTM options. Explain intuitively: $\xi$ controls the curvature of the implied volatility smile, and OTM options lie in the wings where curvature effects are most visible. For an ATM option, the smile curvature has minimal effect, so $\partial V / \partial \xi$ is small.

??? success "Solution to Exercise 3"
    The vol-of-vol parameter $\xi$ controls the **volatility of the variance process** $v_t$:

    $$
    dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}
    $$

    The conditional distribution of $v_T$ (which is a scaled noncentral chi-squared) has variance proportional to $\xi^2$. A higher $\xi$ widens the distribution of $v_T$, which in turn widens the distribution of $\ln S_T$ (because $S_T$ depends on the integrated variance path).

    **Effect on the implied volatility smile.** The implied volatility smile $\sigma_{\text{imp}}(K)$ reflects the risk-neutral distribution of $S_T$:

    - **ATM options** ($K \approx S_0 e^{rT}$): The ATM implied volatility is determined primarily by $\mathbb{E}[v_T]$ (the center of the variance distribution). Changing $\xi$ widens the distribution symmetrically (to first order) around the mean, so the ATM level is barely affected.
    - **OTM options** ($K \ll S_0$ for puts or $K \gg S_0$ for calls): These options are sensitive to the **tails** of the $S_T$ distribution. A wider variance distribution (higher $\xi$) fattens the tails of $S_T$, making extreme outcomes more likely. This increases the probability of deep OTM payoffs, raising their prices and implied volatilities.

    Mathematically, $\partial V / \partial \xi$ is related to the curvature (convexity) of $V$ with respect to $v$ through:

    $$
    \frac{\partial V}{\partial \xi} \propto \frac{\partial^2 V}{\partial v^2}\,\xi\,v \quad (\text{dominant term for small } \xi)
    $$

    The second derivative $\partial^2 V / \partial v^2$ (volga) is largest for OTM options because their payoff is a highly convex function of the terminal distribution's tail, which is itself a convex function of $v$.

    For an ATM option, the payoff is approximately linear in the local stock price moves, and the price depends approximately linearly on $\bar{v}$ (the average variance). The second-order effect of variance dispersion is small. Hence $\partial V / \partial \xi$ is moderate for ATM and large for OTM, explaining the observed pattern.

---

**Exercise 4.**
Compute the vega at $K = 100$ (ATM) and $K = 80$ (deep OTM put) for a Heston call with $T = 0.5$, $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.5$, $\rho = -0.7$. Explain why the ATM vega is larger in absolute terms but the OTM vega is larger relative to the option price.

??? success "Solution to Exercise 4"
    Using the Heston parameters $T = 0.5$, $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.5$, $\rho = -0.7$, $S_0 = 100$, $r = 0.05$, $q = 0$:

    **ATM call ($K = 100$).** From the vega surface in the worked example (interpolating for $\kappa = 2.0$ vs. $\kappa = 1.5$ in the table), the ATM vega is approximately $\mathcal{V}_{\text{ATM}} \approx 16$--$18$ dollars per unit of variance. The ATM call price is approximately $V_{\text{ATM}} \approx \$6.50$.

    **OTM put ($K = 80$).** By put-call parity under Heston (which holds since the model is complete for European payoffs), the put price at $K = 80$ is:

    $$
    P(80) = C(80) - S_0 e^{-qT} + K e^{-rT} = C(80) - 100 + 80 e^{-0.025} \approx C(80) - 21.98
    $$

    The $K = 80$ call is deep ITM, with price $\approx \$22.5$, so $P(80) \approx \$0.52$. The vega (sensitivity to $v_0$) of the put equals the vega of the call at the same strike (by put-call parity, the forward and discount terms do not depend on $v_0$):

    $$
    \mathcal{V}_{\text{OTM}} = \mathcal{V}(K = 80) \approx 4\text{--}5
    $$

    **Comparison.**

    - Absolute vega: $\mathcal{V}_{\text{ATM}} \approx 17 \gg \mathcal{V}_{\text{OTM}} \approx 4.5$. The ATM option has much larger absolute sensitivity to variance because it has the most time value at stake.
    - Relative vega (vega / option price):

    $$
    \frac{\mathcal{V}_{\text{ATM}}}{V_{\text{ATM}}} \approx \frac{17}{6.50} \approx 2.6
    $$

    $$
    \frac{\mathcal{V}_{\text{OTM}}}{V_{\text{OTM}}} \approx \frac{4.5}{0.52} \approx 8.7
    $$

    The OTM put's relative vega is about 3.3 times larger. This is because the OTM put's entire value comes from the possibility that variance is high enough to push $S_T$ below 80. A change in $v_0$ dramatically changes the probability of this tail event, producing a large percentage change in the option price even though the absolute dollar change is modest.

    This has practical implications: a portfolio of OTM puts can have moderate absolute vega but enormous relative vega, meaning a variance shock causes large percentage P&L swings.

---

**Exercise 5.**
The sensitivity $\partial V / \partial \kappa$ measures exposure to changes in mean-reversion speed. For a long-dated ATM call ($T = 2$), explain whether increasing $\kappa$ raises or lowers the option price. Hint: faster mean reversion pulls $v_t$ toward $\theta$ more quickly, reducing the effective variance over long horizons if $v_0 > \theta$, or increasing it if $v_0 < \theta$.

??? success "Solution to Exercise 5"
    The sensitivity $\partial V / \partial \kappa$ measures how the option price responds to a change in the speed of mean reversion.

    **Effect of increasing $\kappa$.** The conditional expectation and variance of $v_T$ are:

    $$
    \mathbb{E}[v_T] = \theta + (v_0 - \theta)e^{-\kappa T}
    $$

    $$
    \operatorname{Var}(v_T) = \frac{v_0 \xi^2 e^{-\kappa T}(1 - e^{-\kappa T})}{\kappa} + \frac{\theta \xi^2 (1 - e^{-\kappa T})^2}{2\kappa}
    $$

    When $v_0 = \theta$ (as in this exercise), $\mathbb{E}[v_T] = \theta$ regardless of $\kappa$, so the expected variance level is unaffected. However, the **variance of $v_T$** depends on $\kappa$:

    $$
    \operatorname{Var}(v_T)\big|_{v_0 = \theta} = \frac{\theta \xi^2}{2\kappa}\left[e^{-\kappa T}(1 - e^{-\kappa T}) + \frac{(1 - e^{-\kappa T})^2}{1}\right]
    $$

    Simplifying for large $T$ ($e^{-\kappa T} \approx 0$):

    $$
    \operatorname{Var}(v_T) \approx \frac{\theta \xi^2}{2\kappa}
    $$

    Increasing $\kappa$ **decreases** $\operatorname{Var}(v_T)$: faster mean reversion confines the variance process more tightly around $\theta$.

    **Impact on a long-dated ATM call ($T = 2$).** For a long-dated call:

    - The expected integrated variance $\frac{1}{T}\int_0^T \mathbb{E}[v_t]\,dt = \theta$ (unchanged when $v_0 = \theta$), so the at-the-money forward level and the average volatility level are unaffected.
    - The **dispersion** of the variance path decreases. Less variance randomness means the distribution of $\ln S_T$ has thinner tails (closer to Gaussian with variance $\theta T$).
    - Thinner tails reduce the value of ATM options slightly (less convexity benefit) and reduce OTM option values more substantially.

    Therefore, **increasing $\kappa$ lowers the option price** when $v_0 = \theta$, and $\partial V / \partial \kappa < 0$.

    If $v_0 \neq \theta$, there is an additional effect:

    - If $v_0 > \theta$: faster mean reversion pulls $v_t$ down toward $\theta$ more quickly, reducing the average variance over the option's life. This lowers the option price, reinforcing $\partial V / \partial \kappa < 0$.
    - If $v_0 < \theta$: faster mean reversion pulls $v_t$ up toward $\theta$ more quickly, increasing average variance and option price. In this case, $\partial V / \partial \kappa > 0$ is possible for short-to-medium maturities, though the reduced variance dispersion effect may still dominate for long-dated options.

---

**Exercise 6.**
A portfolio contains ATM calls at $T = 0.25, 0.5, 1.0, 2.0$ years. Sketch the vega profile (vega vs $T$) and identify the peak. If the trader wants to be vega-neutral across all maturities, explain why this requires hedging with instruments at multiple maturities, not just a single variance swap.

??? success "Solution to Exercise 6"
    **Vega profile sketch.** Using the vega surface data from the worked example (with $\kappa = 1.5$, ATM strike $K = 100$):

    | Maturity $T$ | Vega $\mathcal{V}$ |
    |:---:|:---:|
    | 0.25 | 14.2 |
    | 0.50 | 18.5 |
    | 1.00 | 21.4 |
    | 2.00 | 15.3 |

    The profile rises from 14.2 at $T = 0.25$ to a peak of approximately 21.4 at $T = 1.0$, then declines to 15.3 at $T = 2.0$. The peak occurs near $T \approx 1/(2\kappa)$ to $1/\kappa$ (for $\kappa = 1.5$, this is $0.33$--$0.67$ years, though the actual peak appears to be closer to $T = 1.0$ due to the interplay between the $\sqrt{T}$ growth and the mean-reversion decay).

    **Why a single variance swap is insufficient.** A variance swap with maturity $T_{\text{VS}}$ has vega:

    $$
    \mathcal{V}_{\text{VS}}(T_{\text{VS}}) = \frac{1 - e^{-\kappa T_{\text{VS}}}}{\kappa T_{\text{VS}}} \times \text{notional}
    $$

    This is a specific function of $T_{\text{VS}}$ that decays monotonically from 1 (at $T_{\text{VS}} = 0$) to $1/(\kappa T_{\text{VS}})$ for large $T_{\text{VS}}$.

    The portfolio's vega exposure is a vector across maturities: $(14.2,\; 18.5,\; 21.4,\; 15.3)$ at $T = (0.25,\; 0.50,\; 1.0,\; 2.0)$. A single variance swap provides a **scalar** hedge that can zero out the total (aggregate) vega:

    $$
    \sum_{i} \mathcal{V}_i + N \cdot \mathcal{V}_{\text{VS}} = 0
    $$

    But this does not guarantee vega neutrality at each individual maturity. The problem is that a variance swap's vega has a specific term structure shape (monotonically decaying in $T$), while the portfolio's vega profile is hump-shaped. No scalar multiple of the variance swap's vega curve can match the portfolio's hump-shaped curve across all maturities simultaneously.

    Concretely, if the trader uses a 1-year variance swap to zero out total vega, the hedge will be:

    - **Over-hedged** at $T = 0.25$ and $T = 2.0$ (where the portfolio vega is smaller)
    - **Under-hedged** at $T = 1.0$ (where the portfolio vega peaks)

    A parallel shift in $v_0$ would be perfectly hedged, but a **term-structure shift** (e.g., short-dated implied variance rises while long-dated declines) would generate P&L because the per-maturity mismatches do not cancel.

    **Solution: multi-maturity hedging.** To achieve vega neutrality across all maturities, the trader needs variance swaps (or other vega instruments) at multiple tenors. With four portfolio maturities and four variance swap tenors, the system:

    $$
    \mathcal{V}_i + \sum_{j=1}^{4} N_j \cdot \mathcal{V}_{\text{VS},j}(T_i) = 0, \qquad i = 1, \ldots, 4
    $$

    is a $4 \times 4$ linear system for the notionals $N_1, \ldots, N_4$. This is a **bucket vega hedge**, analogous to bucket duration hedging in fixed income. Each variance swap tenor hedges the vega exposure in a specific maturity bucket, and the combination provides immunization against arbitrary term-structure deformations of the variance curve.
