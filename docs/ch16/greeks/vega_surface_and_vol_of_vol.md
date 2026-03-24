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

The conditional expectation of variance is:

$$
\mathbb{E}[v_T \mid v_0] = \theta + (v_0 - \theta) e^{-\kappa T}
$$

The sensitivity of this expectation to $v_0$ is:

$$
\frac{\partial}{\partial v_0}\mathbb{E}[v_T \mid v_0] = e^{-\kappa T}
$$

This exponential decay governs the term structure of vega. The **half-life** of vega is:

$$
T_{1/2} = \frac{\ln 2}{\kappa}
$$

For $\kappa = 1.5$, $T_{1/2} \approx 0.46$ years. Beyond this maturity, the option price is primarily driven by $\theta$ (the long-run variance) rather than $v_0$.

### Short-Maturity and Long-Maturity Behavior

**Short maturity** ($T \ll 1/\kappa$): The variance has not had time to mean-revert, so $v_T \approx v_0 + \text{noise}$. Vega behaves like Black-Scholes vega $\propto S\sqrt{T} \, \phi(d_1) / (2\sqrt{v_0})$, growing with $\sqrt{T}$.

**Long maturity** ($T \gg 1/\kappa$): The variance has converged to its stationary distribution centered at $\theta$, and the option price is insensitive to $v_0$. Vega decays as $e^{-\kappa T}$, approaching zero.

The combination produces a **hump-shaped** vega term structure, peaking near $T \approx 1/(2\kappa)$ to $1/\kappa$.

!!! note "Implication for Hedging"
    Short-dated options are sensitive to $v_0$ and should be hedged with variance swaps or short-dated VIX futures. Long-dated options are sensitive to $\theta$ (through $\partial V / \partial \theta$) and require hedging instruments that reflect the long-run variance level.

---

## Vega-Gamma Decoupling

### The Black-Scholes Identity

In Black-Scholes with constant volatility $\sigma$, the following identity holds exactly:

$$
\mathcal{V}_{\text{BS}} = \sigma S^2 T \, \Gamma_{\text{BS}}
$$

This means vega and gamma provide redundant information: knowing one determines the other. A delta-hedged portfolio's exposure to volatility changes is fully captured by its gamma.

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

---

**Exercise 2.**
In Black-Scholes, $\mathcal{V} = \sigma S^2 T \Gamma$, linking vega and gamma. Under Heston, this identity fails. Explain why: vega measures sensitivity to $v_0$ (the variance level), while gamma measures sensitivity to spot moves. Since $v_t$ is stochastic and partially independent of $S_t$ (unless $\rho = \pm 1$), the two Greeks are driven by different factors.

---

**Exercise 3.**
The vol-of-vol sensitivity $\partial V / \partial \xi$ is largest for OTM options. Explain intuitively: $\xi$ controls the curvature of the implied volatility smile, and OTM options lie in the wings where curvature effects are most visible. For an ATM option, the smile curvature has minimal effect, so $\partial V / \partial \xi$ is small.

---

**Exercise 4.**
Compute the vega at $K = 100$ (ATM) and $K = 80$ (deep OTM put) for a Heston call with $T = 0.5$, $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.5$, $\rho = -0.7$. Explain why the ATM vega is larger in absolute terms but the OTM vega is larger relative to the option price.

---

**Exercise 5.**
The sensitivity $\partial V / \partial \kappa$ measures exposure to changes in mean-reversion speed. For a long-dated ATM call ($T = 2$), explain whether increasing $\kappa$ raises or lowers the option price. Hint: faster mean reversion pulls $v_t$ toward $\theta$ more quickly, reducing the effective variance over long horizons if $v_0 > \theta$, or increasing it if $v_0 < \theta$.

---

**Exercise 6.**
A portfolio contains ATM calls at $T = 0.25, 0.5, 1.0, 2.0$ years. Sketch the vega profile (vega vs $T$) and identify the peak. If the trader wants to be vega-neutral across all maturities, explain why this requires hedging with instruments at multiple maturities, not just a single variance swap.
