# Relationship to Implied Volatility

Local volatility and implied volatility are two distinct but intimately related descriptions of the option market. Implied volatility $\sigma_{\text{imp}}(K, T)$ is the constant volatility that equates the Black-Scholes formula to the observed market price at a single strike-maturity pair. Local volatility $\sigma_{\text{loc}}(K, T)$ is the instantaneous volatility the asset would have if it reached level $K$ at time $T$. The relationship between these two surfaces is central to both the theory and practice of local volatility models. This section develops the exact Gatheral formula connecting the two, the Berestycki-Busca-Florent (BBF) asymptotic approximation, and the key qualitative result that the local volatility smile is approximately twice as steep as the implied volatility smile.

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - State the exact formula connecting local and implied volatility (Gatheral's formula)
    - Derive the BBF approximation $\sigma_{\text{imp}}(K, T) \approx \sigma_{\text{loc}}(\frac{1}{2}(S_0 + K), \frac{1}{2}T)$
    - Prove the ATM time-average relation $\sigma_{\text{imp}}(S_0, T) \approx \frac{1}{T}\int_0^T \sigma_{\text{loc}}(S_0, t)\,dt$
    - Explain why the local volatility skew is steeper than the implied volatility skew
    - Apply the formulas to convert between local and implied volatility surfaces

## Exact Relationship: Gatheral's Formula

### From Dupire to Implied Volatility

The Dupire formula expresses local volatility in terms of derivatives of call prices:

$$
\sigma_{\text{loc}}^2(K, T) = \frac{\partial_T C + (r - q)K \partial_K C + qC}{\frac{1}{2}K^2 \partial_{KK} C}
$$

Since the call price $C(K, T) = C_{\text{BS}}(K, T; \sigma_{\text{imp}}(K, T))$ is determined by the implied volatility surface through the Black-Scholes formula, we can express all derivatives of $C$ in terms of $\sigma_{\text{imp}}$ and its derivatives. This yields an exact, model-free relationship.

### The Gatheral Formula

**Theorem 13.3.3** (Local Volatility in Terms of Implied Volatility).
Let $\sigma_{\text{imp}}(K, T)$ denote the implied volatility surface, and let $w(K, T) = \sigma_{\text{imp}}^2(K, T) T$ be the implied total variance. Define:

$$
d_1 = \frac{\log(S_0 e^{(r-q)T}/K) + \frac{1}{2}w}{\sqrt{w}}, \quad d_2 = d_1 - \sqrt{w}
$$

Then the local volatility is:

$$
\sigma_{\text{loc}}^2(K, T) = \frac{\sigma_{\text{imp}}^2 + 2\sigma_{\text{imp}} T \partial_T \sigma_{\text{imp}} + 2(r - q)K\sigma_{\text{imp}} T \partial_K \sigma_{\text{imp}}}{\left(1 + Kd_1\sqrt{T}\,\partial_K \sigma_{\text{imp}}\right)^2 + K^2 \sigma_{\text{imp}} T\left(\partial_{KK}\sigma_{\text{imp}} - d_1(\partial_K \sigma_{\text{imp}})^2 \sqrt{T}\right)}
$$

*Proof sketch.* Apply the chain rule to $C_{\text{BS}}(K, T; \sigma_{\text{imp}}(K, T))$. The key Black-Scholes sensitivities are:

$$
\frac{\partial C_{\text{BS}}}{\partial \sigma} = S_0 e^{-qT} \phi(d_1)\sqrt{T} \quad (\text{vega})
$$

$$
\frac{\partial^2 C_{\text{BS}}}{\partial K^2} = \frac{e^{-qT} S_0 \phi(d_1)}{K^2 \sigma_{\text{imp}}\sqrt{T}} \quad (\text{strike gamma})
$$

where $\phi$ is the standard normal density. The time derivative $\partial_T C$ involves the Black-Scholes theta plus the vega times $\partial_T \sigma_{\text{imp}}$. The strike derivatives $\partial_K C$ and $\partial_{KK} C$ involve the Black-Scholes delta-strike plus vega and vega-strike correction terms. Substituting into the Dupire formula and simplifying yields the result. $\square$

### Structure of the Formula

The Gatheral formula has a clear structure:

- **Numerator**: $\sigma_{\text{imp}}^2 + 2\sigma_{\text{imp}} T \partial_T \sigma_{\text{imp}} + 2(r-q)K\sigma_{\text{imp}} T \partial_K \sigma_{\text{imp}} = \partial_T w + 2(r-q)K\sigma_{\text{imp}} T \partial_K \sigma_{\text{imp}}$. The dominant term is the time derivative of total variance $\partial_T w$, which represents the forward instantaneous variance in the implied volatility term structure. The correction involves the implied vol skew scaled by the risk-neutral drift.

- **Denominator**: The denominator adjusts for the curvature of the implied volatility surface. When the surface is flat ($\partial_K \sigma_{\text{imp}} = \partial_{KK}\sigma_{\text{imp}} = 0$), the denominator equals 1, and $\sigma_{\text{loc}}^2 = \partial_T w = \sigma_{\text{imp}}^2 + 2\sigma_{\text{imp}} T \partial_T \sigma_{\text{imp}}$, which is the forward variance from the term structure alone.

## The Berestycki-Busca-Florent Formula

### Leading-Order Approximation

The BBF formula (2002) provides the leading-order asymptotic relationship between local and implied volatility for small time-to-maturity or near-the-money options.

**Theorem 13.3.4** (BBF Approximation).
For the local volatility model with smooth $\sigma_{\text{loc}}(S, t)$, the implied volatility satisfies:

$$
\sigma_{\text{imp}}(K, T) = \sigma_{\text{loc}}\left(\frac{S_0 + K}{2}, \frac{T}{2}\right) + O(T) + O\bigl((\log K/S_0)^2\bigr)
$$

as $T \to 0$ and $K \to S_0$.

*Proof sketch.* The BBF result follows from a WKB (Wentzel-Kramers-Brillouin) expansion of the heat kernel. In log-spot coordinates $x = \log S$, the transition density satisfies a parabolic PDE whose short-time asymptotics are controlled by the geodesic distance:

$$
d(x_0, x) = \int_{x_0}^{x} \frac{d\xi}{\sigma_{\text{loc}}(e^{\xi}, 0)}
$$

The leading-order implied volatility is determined by the harmonic mean of $\sigma_{\text{loc}}$ along the integration path from $\log S_0$ to $\log K$:

$$
\frac{1}{\sigma_{\text{imp}}(K, T)} \approx \frac{1}{\log(K/S_0)} \int_{\log S_0}^{\log K} \frac{d\xi}{\sigma_{\text{loc}}(e^{\xi}, T/2)}
$$

For $K$ close to $S_0$, the integral is well-approximated by evaluating $\sigma_{\text{loc}}$ at the midpoint, yielding $\sigma_{\text{imp}} \approx \sigma_{\text{loc}}((S_0 + K)/2, T/2)$. $\square$

**Interpretation.** The implied volatility at strike $K$ is approximately the local volatility evaluated at the **midpoint** in spot space $(S_0 + K)/2$ and **midpoint** in time $T/2$. This makes intuitive sense: the implied volatility is an average of the local volatility along the most probable path from $S_0$ to $K$ during $[0, T]$, and the midpoint is the center of this path.

### Refinements

Higher-order corrections to the BBF formula incorporate the gradient and curvature of the local volatility surface:

$$
\sigma_{\text{imp}}(K, T) = \bar{\sigma} + \frac{T}{24}\bar{\sigma}^3\left(\frac{\partial^2 \sigma_{\text{loc}}^2}{\partial S^2}\bigg|_{\bar{S}} \bar{S}^2 - \frac{1}{4}\left(\frac{\partial \sigma_{\text{loc}}^2}{\partial S}\bigg|_{\bar{S}} \bar{S}\right)^2 \frac{1}{\bar{\sigma}^2}\right) + O(T^2)
$$

where $\bar{S} = (S_0 + K)/2$ and $\bar{\sigma} = \sigma_{\text{loc}}(\bar{S}, T/2)$.

## ATM Relationships

### Time-Average Formula

At the money ($K = S_0$), the BBF formula simplifies to a time average.

**Proposition 13.3.3** (ATM Implied Volatility as Time Average).
For $K = S_0$ (at-the-money forward, ignoring the drift correction):

$$
\sigma_{\text{imp}}^2(S_0, T) \approx \frac{1}{T}\int_0^T \sigma_{\text{loc}}^2(S_0, t) \, dt
$$

*Proof.* At $K = S_0$, the most probable path stays near $S_0$ for the entire time interval $[0, T]$. The total implied variance $\sigma_{\text{imp}}^2 T$ is therefore the integral of the local variance along this path:

$$
\sigma_{\text{imp}}^2(S_0, T) \cdot T = \int_0^T \sigma_{\text{loc}}^2(S_0, t) \, dt
$$

Dividing by $T$ gives the result. Higher-order corrections involve the spatial derivatives of $\sigma_{\text{loc}}$ at $S_0$. $\square$

**Corollary.** The ATM implied volatility term structure $\sigma_{\text{imp}}(S_0, T)$ is a running average of the ATM local volatility. In particular:

$$
\sigma_{\text{loc}}^2(S_0, T) = \frac{\partial}{\partial T}\bigl[T \cdot \sigma_{\text{imp}}^2(S_0, T)\bigr] = \sigma_{\text{imp}}^2(S_0, T) + 2T \sigma_{\text{imp}}(S_0, T) \partial_T \sigma_{\text{imp}}(S_0, T)
$$

This shows that the local variance at time $T$ is the marginal increment to the total implied variance, analogous to the relationship between a forward rate and a spot rate in fixed income.

### Forward Variance Interpretation

The analogy with interest rates is precise:

| Fixed Income | Volatility |
|-------------|-----------|
| Spot rate $r(T)$ | $\sigma_{\text{imp}}^2(S_0, T)$ |
| Forward rate $f(T)$ | $\sigma_{\text{loc}}^2(S_0, T)$ |
| $\int_0^T f(t) \, dt = r(T) \cdot T$ | $\int_0^T \sigma_{\text{loc}}^2(S_0, t)\, dt = \sigma_{\text{imp}}^2(S_0, T) \cdot T$ |

Just as the forward rate is the marginal rate of return at time $T$, the local variance at the ATM level is the marginal rate of variance accumulation at time $T$.

## The Steepness Ratio

### Local Vol Skew vs Implied Vol Skew

A fundamental qualitative result is that the local volatility smile is approximately **twice as steep** as the implied volatility smile.

**Proposition 13.3.4** (Skew Doubling Rule).
For short maturities and near-the-money strikes:

$$
\frac{\partial \sigma_{\text{loc}}}{\partial K}\bigg|_{K = S_0} \approx 2 \frac{\partial \sigma_{\text{imp}}}{\partial K}\bigg|_{K = S_0}
$$

*Proof.* From the BBF formula $\sigma_{\text{imp}}(K, T) \approx \sigma_{\text{loc}}((S_0 + K)/2, T/2)$, differentiate with respect to $K$:

$$
\frac{\partial \sigma_{\text{imp}}}{\partial K} \approx \frac{1}{2}\frac{\partial \sigma_{\text{loc}}}{\partial S}\bigg|_{S = (S_0 + K)/2}
$$

At $K = S_0$, this gives:

$$
\frac{\partial \sigma_{\text{imp}}}{\partial K}\bigg|_{K = S_0} \approx \frac{1}{2}\frac{\partial \sigma_{\text{loc}}}{\partial S}\bigg|_{S = S_0}
$$

Rearranging: $\partial_K \sigma_{\text{loc}}|_{S_0} \approx 2 \partial_K \sigma_{\text{imp}}|_{S_0}$. $\square$

**Intuition.** Implied volatility is an average of local volatility along the path from $S_0$ to $K$. When $K$ changes by $\Delta K$, the path midpoint shifts by $\Delta K / 2$, so the change in the local volatility (evaluated at the midpoint) is halved. Conversely, the local volatility surface must have twice the slope of the implied volatility surface to produce the observed smile.

!!! warning "Practical Consequence"
    The steepness of the local volatility surface is a persistent source of calibration difficulty. Small errors in the implied volatility skew are amplified by a factor of two in the local volatility surface. This is one manifestation of the ill-posedness of the Dupire inversion.

### Convexity Relationship

Similarly, the convexity of the local volatility smile relates to the implied volatility convexity:

$$
\frac{\partial^2 \sigma_{\text{loc}}}{\partial K^2}\bigg|_{K = S_0} \approx 4\frac{\partial^2 \sigma_{\text{imp}}}{\partial K^2}\bigg|_{K = S_0} - 2\frac{(\partial_K \sigma_{\text{imp}})^2}{\sigma_{\text{imp}}}\bigg|_{K = S_0}
$$

The first term is the direct scaling (factor of 4 since each differentiation contributes a factor of 2), while the second is a nonlinear correction from the chain rule.

## Worked Example

??? example "Converting a Linear Implied Vol Skew to Local Vol"

    **Setup.** Let $\sigma_{\text{imp}}(K) = 0.20 - 0.0008(K - 100)$ for $T = 1$, with $r = 0.03$, $q = 0$, $S_0 = 100$.

    **At $K = 100$ (ATM):**

    - $\sigma_{\text{imp}} = 0.20$, $\partial_K \sigma_{\text{imp}} = -0.0008$, $\partial_{KK}\sigma_{\text{imp}} = 0$, $\partial_T \sigma_{\text{imp}} = 0$
    - $w = 0.04$, $d_1 = (0.03 + 0.02)/0.20 = 0.25$

    Numerator:

    $$
    0.04 + 0 + 2(0.03)(100)(0.20)(1)(-0.0008) = 0.04 - 0.00096 = 0.03904
    $$

    Denominator:

    $$
    \bigl(1 + 100(0.25)(1)(-0.0008)\bigr)^2 + 0 = (1 - 0.02)^2 = 0.9604
    $$

    So $\sigma_{\text{loc}}^2(100, 1) = 0.03904/0.9604 = 0.04065$, giving $\sigma_{\text{loc}}(100, 1) = 0.2016$.

    **At $K = 90$ (10% OTM put):**

    - $\sigma_{\text{imp}} = 0.208$, $\partial_K \sigma_{\text{imp}} = -0.0008$

    Using the BBF approximation: $\sigma_{\text{loc}}(90, 1) \approx \sigma_{\text{imp}}(95, 1) = 0.20 - 0.0008(-5) = 0.204$. But the exact Gatheral formula gives a higher value because the denominator correction further amplifies the skew.

    **Skew comparison:**

    The implied vol skew is $-0.0008$ per unit of $K$. The local vol skew from the BBF doubling rule is approximately $-0.0016$ per unit of $S$, confirming that the local volatility surface is roughly twice as steep.

## Inverse Problem: From Local to Implied

### Forward Integration

Given a local volatility surface $\sigma_{\text{loc}}(S, t)$, computing the implied volatility surface requires:

1. Solve the backward PDE $\partial_t V + \frac{1}{2}\sigma_{\text{loc}}^2 S^2 V_{SS} + (r-q)SV_S - rV = 0$ for each payoff
2. Or solve the forward PDE to get call prices for all strikes simultaneously
3. Invert the Black-Scholes formula to obtain $\sigma_{\text{imp}}(K, T)$ from $C(K, T)$

This forward problem is well-posed: smooth local volatility produces smooth call prices and hence a smooth implied volatility surface. The difficulty lies in the inverse direction (implied to local), which amplifies noise.

### Asymptotic Inversion

For practical purposes, the BBF formula and its higher-order corrections can be inverted to obtain an approximation:

$$
\sigma_{\text{loc}}(S, t) \approx \sigma_{\text{imp}}\bigl(2S - S_0, 2t\bigr) + O(t)
$$

This "mirror" formula maps the point $(S, t)$ in local vol space to the point $(2S - S_0, 2t)$ in implied vol space, reflecting the midpoint averaging inherent in the BBF relationship.

## Summary

The relationship between local and implied volatility is characterized by:

1. **Gatheral's formula**: An exact, model-free relationship expressing $\sigma_{\text{loc}}^2$ in terms of $\sigma_{\text{imp}}$ and its first and second derivatives with respect to $K$ and $T$.
2. **BBF approximation**: $\sigma_{\text{imp}}(K, T) \approx \sigma_{\text{loc}}((S_0 + K)/2, T/2)$ -- implied volatility is the local volatility evaluated at the midpoint of the path.
3. **ATM time average**: $\sigma_{\text{imp}}^2(S_0, T) \approx \frac{1}{T}\int_0^T \sigma_{\text{loc}}^2(S_0, t)\,dt$ -- the ATM implied variance is the running average of ATM local variance.
4. **Skew doubling**: The local volatility skew is approximately twice as steep as the implied volatility skew, a consequence of the midpoint averaging.
5. **Forward variance analogy**: Local variance plays the role of forward rate, while implied variance plays the role of spot rate.

---

## Exercises

**Exercise 1.** Using the BBF approximation $\sigma_{\text{imp}}(K, T) \approx \sigma_{\text{loc}}((S_0 + K)/2, T/2)$, compute the implied volatility at $K = 90$ and $T = 1$ if the local volatility surface is $\sigma_{\text{loc}}(S, t) = 0.25 - 0.001(S - 100)$. Verify that the implied volatility skew is approximately half as steep as the local volatility skew.

??? success "Solution to Exercise 1"
    Using the BBF approximation:

    $$
    \sigma_{\text{imp}}(K, T) \approx \sigma_{\text{loc}}\left(\frac{S_0 + K}{2}, \frac{T}{2}\right)
    $$

    With $S_0 = 100$, $K = 90$, $T = 1$, and $\sigma_{\text{loc}}(S, t) = 0.25 - 0.001(S - 100)$:

    The midpoint in spot is $\frac{S_0 + K}{2} = \frac{100 + 90}{2} = 95$. The midpoint in time is $\frac{T}{2} = 0.5$ (but $\sigma_{\text{loc}}$ does not depend on $t$ here).

    $$
    \sigma_{\text{imp}}(90, 1) \approx \sigma_{\text{loc}}(95, 0.5) = 0.25 - 0.001(95 - 100) = 0.25 + 0.005 = 0.255
    $$

    **Verifying the skew ratio.** The local volatility skew is:

    $$
    \frac{\partial \sigma_{\text{loc}}}{\partial S} = -0.001
    $$

    The implied volatility skew is found by differentiating the BBF relation with respect to $K$:

    $$
    \frac{\partial \sigma_{\text{imp}}}{\partial K} \approx \frac{1}{2}\frac{\partial \sigma_{\text{loc}}}{\partial S}\bigg|_{S=(S_0+K)/2} = \frac{1}{2}(-0.001) = -0.0005
    $$

    The implied volatility skew ($-0.0005$ per unit of $K$) is indeed half as steep as the local volatility skew ($-0.001$ per unit of $S$), confirming the skew doubling rule.

---

**Exercise 2.** The ATM time-average relation states $\sigma_{\text{imp}}^2(S_0, T) \approx \frac{1}{T}\int_0^T \sigma_{\text{loc}}^2(S_0, t) \, dt$. Suppose the ATM local volatility is $\sigma_{\text{loc}}(S_0, t) = 0.20 + 0.05 e^{-2t}$. Compute $\sigma_{\text{imp}}(S_0, T)$ for $T = 0.5$ and $T = 2.0$. Is the implied volatility term structure increasing or decreasing?

??? success "Solution to Exercise 2"
    The ATM time-average relation gives:

    $$
    \sigma_{\text{imp}}^2(S_0, T) \approx \frac{1}{T}\int_0^T \sigma_{\text{loc}}^2(S_0, t) \, dt
    $$

    With $\sigma_{\text{loc}}(S_0, t) = 0.20 + 0.05e^{-2t}$, the local variance is:

    $$
    \sigma_{\text{loc}}^2(S_0, t) = (0.20 + 0.05e^{-2t})^2 = 0.04 + 0.02e^{-2t} + 0.0025e^{-4t}
    $$

    The integral is:

    $$
    \int_0^T \sigma_{\text{loc}}^2(S_0, t) \, dt = 0.04T + 0.02 \cdot \frac{1 - e^{-2T}}{2} + 0.0025 \cdot \frac{1 - e^{-4T}}{4}
    $$

    $$
    = 0.04T + 0.01(1 - e^{-2T}) + 0.000625(1 - e^{-4T})
    $$

    **For $T = 0.5$:**

    $$
    = 0.02 + 0.01(1 - e^{-1}) + 0.000625(1 - e^{-2})
    $$

    $$
    = 0.02 + 0.01(0.6321) + 0.000625(0.8647)
    $$

    $$
    = 0.02 + 0.006321 + 0.000540 = 0.026861
    $$

    $$
    \sigma_{\text{imp}}^2(S_0, 0.5) = \frac{0.026861}{0.5} = 0.053722
    $$

    $$
    \sigma_{\text{imp}}(S_0, 0.5) = \sqrt{0.053722} \approx 0.2318
    $$

    **For $T = 2.0$:**

    $$
    = 0.08 + 0.01(1 - e^{-4}) + 0.000625(1 - e^{-8})
    $$

    $$
    = 0.08 + 0.01(0.9817) + 0.000625(0.9997)
    $$

    $$
    = 0.08 + 0.009817 + 0.000625 = 0.090442
    $$

    $$
    \sigma_{\text{imp}}^2(S_0, 2.0) = \frac{0.090442}{2.0} = 0.045221
    $$

    $$
    \sigma_{\text{imp}}(S_0, 2.0) = \sqrt{0.045221} \approx 0.2127
    $$

    **The implied volatility term structure is decreasing:** $\sigma_{\text{imp}}$ drops from $0.2318$ at $T = 0.5$ to $0.2127$ at $T = 2.0$. This is because the local volatility starts high ($\sigma_{\text{loc}}(S_0, 0) = 0.25$) and decays toward $0.20$ as $t \to \infty$. The running average of the local variance is dominated by the high early values at short maturities, producing a downward-sloping term structure.

---

**Exercise 3.** Prove the skew doubling rule: starting from $\sigma_{\text{imp}}(K, T) \approx \sigma_{\text{loc}}((S_0 + K)/2, T/2)$, differentiate with respect to $K$ and evaluate at $K = S_0$ to show:

$$
\frac{\partial \sigma_{\text{imp}}}{\partial K}\bigg|_{K=S_0} \approx \frac{1}{2}\frac{\partial \sigma_{\text{loc}}}{\partial S}\bigg|_{S=S_0}
$$

Explain the financial intuition: why does midpoint averaging halve the observed skew?

??? success "Solution to Exercise 3"
    Starting from the BBF approximation:

    $$
    \sigma_{\text{imp}}(K, T) \approx \sigma_{\text{loc}}\left(\frac{S_0 + K}{2}, \frac{T}{2}\right)
    $$

    Differentiate with respect to $K$:

    $$
    \frac{\partial \sigma_{\text{imp}}}{\partial K} = \frac{\partial \sigma_{\text{loc}}}{\partial S}\bigg|_{S = (S_0+K)/2} \cdot \frac{\partial}{\partial K}\left(\frac{S_0 + K}{2}\right) = \frac{1}{2}\frac{\partial \sigma_{\text{loc}}}{\partial S}\bigg|_{S = (S_0+K)/2}
    $$

    Evaluating at $K = S_0$ (so $S = (S_0 + S_0)/2 = S_0$):

    $$
    \frac{\partial \sigma_{\text{imp}}}{\partial K}\bigg|_{K = S_0} = \frac{1}{2}\frac{\partial \sigma_{\text{loc}}}{\partial S}\bigg|_{S = S_0}
    $$

    Rearranging:

    $$
    \frac{\partial \sigma_{\text{loc}}}{\partial S}\bigg|_{S = S_0} = 2\frac{\partial \sigma_{\text{imp}}}{\partial K}\bigg|_{K = S_0}
    $$

    **Financial intuition:** Implied volatility is an average of local volatility along the most probable path from $S_0$ to $K$. The BBF formula says this average is well-approximated by the local volatility at the midpoint $(S_0 + K)/2$. When the strike shifts by $\Delta K$, the midpoint shifts by only $\Delta K / 2$, so the implied volatility changes by half as much as the underlying local volatility. Equivalently, the local volatility surface must slope twice as steeply as the implied volatility smile to produce the observed market skew, because the averaging effect of integrating along the path dampens the slope by a factor of two.

---

**Exercise 4.** Given a linear implied volatility skew $\sigma_{\text{imp}}(K) = 0.22 - 0.0006(K - 100)$ with $S_0 = 100$, $T = 0.5$, and $r = 2\%$, $q = 0$, use the Gatheral formula to compute $\sigma_{\text{loc}}^2(100, 0.5)$. You may assume $\partial_T \sigma_{\text{imp}} = 0$ and $\partial_{KK} \sigma_{\text{imp}} = 0$.

??? success "Solution to Exercise 4"
    Given: $\sigma_{\text{imp}}(K) = 0.22 - 0.0006(K - 100)$, $S_0 = 100$, $T = 0.5$, $r = 0.02$, $q = 0$, $\partial_T \sigma_{\text{imp}} = 0$, $\partial_{KK}\sigma_{\text{imp}} = 0$.

    At $K = 100$: $\sigma_{\text{imp}} = 0.22$, $\partial_K \sigma_{\text{imp}} = -0.0006$.

    Compute the total variance and $d_1$:

    $$
    w = \sigma_{\text{imp}}^2 T = 0.0484 \times 0.5 = 0.0242
    $$

    $$
    d_1 = \frac{\log(S_0 e^{(r-q)T}/K) + \frac{1}{2}w}{\sqrt{w}} = \frac{\log(e^{0.01}) + 0.0121}{\sqrt{0.0242}} = \frac{0.01 + 0.0121}{0.15556} = \frac{0.0221}{0.15556} = 0.1421
    $$

    **Numerator** of the Gatheral formula:

    $$
    \sigma_{\text{imp}}^2 + 2\sigma_{\text{imp}} T \partial_T \sigma_{\text{imp}} + 2(r-q)K\sigma_{\text{imp}} T \partial_K \sigma_{\text{imp}}
    $$

    $$
    = 0.0484 + 0 + 2(0.02)(100)(0.22)(0.5)(-0.0006)
    $$

    $$
    = 0.0484 + 2(0.02)(100)(0.22)(0.5)(-0.0006)
    $$

    $$
    = 0.0484 - 0.000264 = 0.048136
    $$

    **Denominator** of the Gatheral formula (with $\partial_{KK}\sigma_{\text{imp}} = 0$):

    $$
    \left(1 + Kd_1\sqrt{T}\,\partial_K \sigma_{\text{imp}}\right)^2 + K^2\sigma_{\text{imp}} T\left(0 - d_1(\partial_K\sigma_{\text{imp}})^2\sqrt{T}\right)
    $$

    First term:

    $$
    1 + 100(0.1421)(\sqrt{0.5})(-0.0006) = 1 + 100(0.1421)(0.7071)(-0.0006) = 1 - 0.006028 = 0.993972
    $$

    $$
    (0.993972)^2 = 0.987980
    $$

    Second term:

    $$
    (100)^2(0.22)(0.5)\bigl(-0.1421 \times (0.0006)^2 \times 0.7071\bigr) = 10000 \times 0.11 \times (-0.1421 \times 3.6 \times 10^{-7} \times 0.7071)
    $$

    $$
    = 1100 \times (-3.617 \times 10^{-8}) = -3.98 \times 10^{-5}
    $$

    This is negligible. So the denominator is approximately $0.98798$.

    **Result:**

    $$
    \sigma_{\text{loc}}^2(100, 0.5) = \frac{0.048136}{0.98798} = 0.04872
    $$

    $$
    \sigma_{\text{loc}}(100, 0.5) = \sqrt{0.04872} \approx 0.2207
    $$

    The local volatility at ATM ($0.2207$) is slightly higher than the implied volatility ($0.22$), reflecting the denominator correction due to the implied volatility skew.

---

**Exercise 5.** The forward variance analogy equates local variance with the forward rate and implied variance with the spot rate. Given an ATM implied volatility term structure $\sigma_{\text{imp}}(S_0, T)$ at maturities $T = 0.25, 0.50, 1.0$ with values $22\%, 21\%, 20\%$, compute the ATM local variance at $T = 0.25, 0.50$, and $1.0$ using:

$$
\sigma_{\text{loc}}^2(S_0, T) = \frac{\partial}{\partial T}[T \cdot \sigma_{\text{imp}}^2(S_0, T)]
$$

Is the local variance term structure monotone?

??? success "Solution to Exercise 5"
    Using the forward variance formula:

    $$
    \sigma_{\text{loc}}^2(S_0, T) = \frac{\partial}{\partial T}[T \cdot \sigma_{\text{imp}}^2(S_0, T)]
    $$

    First compute the total implied variance $T \cdot \sigma_{\text{imp}}^2$ at each maturity:

    - $T = 0.25$: $0.25 \times 0.22^2 = 0.25 \times 0.0484 = 0.01210$
    - $T = 0.50$: $0.50 \times 0.21^2 = 0.50 \times 0.0441 = 0.02205$
    - $T = 1.00$: $1.00 \times 0.20^2 = 1.00 \times 0.0400 = 0.04000$

    Approximate the derivative using finite differences:

    **At $T = 0.25$:** Using forward difference from $T = 0$ (where total variance is 0) to $T = 0.25$:

    $$
    \sigma_{\text{loc}}^2(S_0, 0.25) \approx \frac{0.01210 - 0}{0.25 - 0} = 0.0484
    $$

    $$
    \sigma_{\text{loc}}(S_0, 0.25) = \sqrt{0.0484} = 0.220
    $$

    **At $T = 0.50$:** Using the interval from $T = 0.25$ to $T = 0.50$:

    $$
    \sigma_{\text{loc}}^2(S_0, 0.50) \approx \frac{0.02205 - 0.01210}{0.50 - 0.25} = \frac{0.00995}{0.25} = 0.03980
    $$

    $$
    \sigma_{\text{loc}}(S_0, 0.50) = \sqrt{0.03980} \approx 0.1995
    $$

    **At $T = 1.0$:** Using the interval from $T = 0.50$ to $T = 1.00$:

    $$
    \sigma_{\text{loc}}^2(S_0, 1.0) \approx \frac{0.04000 - 0.02205}{1.00 - 0.50} = \frac{0.01795}{0.50} = 0.03590
    $$

    $$
    \sigma_{\text{loc}}(S_0, 1.0) = \sqrt{0.03590} \approx 0.1895
    $$

    **The local variance term structure is monotonically decreasing:** $\sigma_{\text{loc}}^2$ drops from $0.0484$ at $T = 0.25$ to $0.0398$ at $T = 0.50$ to $0.0359$ at $T = 1.0$. The decreasing implied volatility term structure ($22\% \to 21\% \to 20\%$) implies that the marginal variance being added at later times is lower than the average, producing a declining local variance curve. This is analogous to a downward-sloping forward rate curve when the yield curve is downward-sloping.

---

**Exercise 6.** The "mirror" formula for inverting the BBF relationship is $\sigma_{\text{loc}}(S, t) \approx \sigma_{\text{imp}}(2S - S_0, 2t)$. Given an implied volatility surface $\sigma_{\text{imp}}(K, T) = 0.20 - 0.001(K - 100) + 0.01\sqrt{T}$ with $S_0 = 100$, compute the approximate local volatility at $(S, t) = (95, 0.5)$ and $(S, t) = (105, 0.5)$.

??? success "Solution to Exercise 6"
    Using the mirror formula $\sigma_{\text{loc}}(S, t) \approx \sigma_{\text{imp}}(2S - S_0, 2t)$ with $S_0 = 100$ and $\sigma_{\text{imp}}(K, T) = 0.20 - 0.001(K - 100) + 0.01\sqrt{T}$.

    **At $(S, t) = (95, 0.5)$:**

    $$
    K^* = 2(95) - 100 = 90, \quad T^* = 2(0.5) = 1.0
    $$

    $$
    \sigma_{\text{loc}}(95, 0.5) \approx \sigma_{\text{imp}}(90, 1.0) = 0.20 - 0.001(90 - 100) + 0.01\sqrt{1.0}
    $$

    $$
    = 0.20 + 0.01 + 0.01 = 0.22
    $$

    **At $(S, t) = (105, 0.5)$:**

    $$
    K^* = 2(105) - 100 = 110, \quad T^* = 2(0.5) = 1.0
    $$

    $$
    \sigma_{\text{loc}}(105, 0.5) \approx \sigma_{\text{imp}}(110, 1.0) = 0.20 - 0.001(110 - 100) + 0.01\sqrt{1.0}
    $$

    $$
    = 0.20 - 0.01 + 0.01 = 0.20
    $$

    The local volatility at $S = 95$ ($0.22$) is higher than at $S = 105$ ($0.20$), reflecting a downward-sloping local volatility in the spot direction. The local vol skew between these points is $(0.20 - 0.22)/(105 - 95) = -0.002$ per unit of $S$, which is twice the implied vol skew of $-0.001$ per unit of $K$, consistent with the skew doubling rule.
