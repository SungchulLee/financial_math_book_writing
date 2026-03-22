# Smile Dynamics Under Local Volatility

The local volatility model perfectly reproduces today's implied volatility surface by construction. However, a model's value lies not only in fitting today's prices but in predicting how those prices change tomorrow. Smile dynamics -- the way the implied volatility surface moves in response to changes in the underlying spot price -- represent the model's prediction for the joint behavior of spot and implied volatility. Under local volatility, this prediction takes a specific and empirically problematic form: the smile dynamics are approximately **sticky strike**, meaning the smile is anchored to fixed strike levels rather than moving with the spot. This section develops the mathematics of smile dynamics under local volatility, contrasts them with the empirical sticky delta behavior, and explains the hedging consequences.

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Define sticky strike, sticky delta, and sticky local volatility regimes
    - Derive the smile dynamics implied by the local volatility model
    - Compute the local volatility delta and compare it with the Black-Scholes delta
    - Explain why local volatility produces sticky strike behavior
    - Quantify the implied spot-volatility correlation under local volatility
    - Describe the hedging P&L consequences of incorrect smile dynamics

## Smile Dynamics: Three Regimes

### Sticky Strike

Under **sticky strike** dynamics, the implied volatility of a fixed-strike option does not change when the spot price moves:

$$
\frac{\partial \sigma_{\text{imp}}(K, T)}{\partial S_0}\bigg|_{\text{sticky strike}} = 0
$$

The implied volatility is a function of the absolute strike $K$ alone. When the spot rises from $S_0$ to $S_0 + \Delta S$, the ATM strike shifts to $S_0 + \Delta S$, and the ATM implied volatility changes because the model reads off the smile at a new strike level. For a typical equity skew (downward-sloping in $K$), a spot increase shifts ATM to a higher strike, where implied volatility is lower.

### Sticky Delta

Under **sticky delta** (or sticky moneyness) dynamics, the implied volatility of a fixed-moneyness option does not change when the spot moves:

$$
\frac{\partial \sigma_{\text{imp}}(K/S_0, T)}{\partial S_0}\bigg|_{\text{sticky delta}} = 0
$$

The implied volatility depends on the relative strike $K/S_0$ (or equivalently, the delta of the option). When the spot rises, the entire smile shifts to the right, maintaining its shape relative to the new spot level. The ATM implied volatility remains unchanged.

### Sticky Local Volatility

Under **sticky local volatility**, the local volatility surface $\sigma_{\text{loc}}(S, t)$ is fixed, and implied volatilities change as a consequence of the spot moving through this fixed surface. This is precisely the regime that the local volatility model produces.

## Smile Dynamics Under Local Volatility

### The Key Result

**Theorem 13.3.5** (Local Volatility Smile Dynamics).
Under the local volatility model, the implied volatility surface evolves approximately in the sticky strike regime. More precisely, for short time intervals $\Delta t$ and small spot moves $\Delta S$:

$$
\sigma_{\text{imp}}(K, T; S_0 + \Delta S) \approx \sigma_{\text{imp}}(K, T; S_0) + \frac{\partial \sigma_{\text{imp}}}{\partial S_0} \Delta S
$$

where:

$$
\frac{\partial \sigma_{\text{imp}}}{\partial S_0} \approx -\frac{\partial \sigma_{\text{imp}}}{\partial K}
$$

This relation means that the effect of a unit increase in spot on implied volatility is approximately equal to the effect of a unit decrease in strike.

*Proof.* From the BBF approximation $\sigma_{\text{imp}}(K, T) \approx \sigma_{\text{loc}}((S_0 + K)/2, T/2)$, differentiate with respect to $S_0$:

$$
\frac{\partial \sigma_{\text{imp}}}{\partial S_0} = \frac{1}{2}\frac{\partial \sigma_{\text{loc}}}{\partial S}\bigg|_{S = (S_0+K)/2}
$$

Similarly, differentiating with respect to $K$:

$$
\frac{\partial \sigma_{\text{imp}}}{\partial K} = \frac{1}{2}\frac{\partial \sigma_{\text{loc}}}{\partial S}\bigg|_{S = (S_0+K)/2}
$$

Therefore:

$$
\frac{\partial \sigma_{\text{imp}}}{\partial S_0} = \frac{\partial \sigma_{\text{imp}}}{\partial K}
$$

This is the characteristic signature of sticky strike dynamics: shifting $S_0$ by $+\Delta S$ has the same effect on implied volatility as shifting $K$ by $+\Delta S$. Equivalently, the implied volatility of a fixed-strike option changes by $\approx (\partial_K \sigma_{\text{imp}})\Delta S$ when spot moves by $\Delta S$, which means the smile slides along the strike axis in lockstep with spot. $\square$

!!! note "Sticky Strike is an Approximation"
    The result $\partial_{S_0}\sigma_{\text{imp}} = \partial_K \sigma_{\text{imp}}$ is exact only in the leading-order BBF approximation. At higher orders, there are corrections, and the local volatility model does not produce exactly sticky strike behavior. However, the leading-order result captures the dominant effect and is the primary qualitative feature of local volatility smile dynamics.

### ATM Volatility Response to Spot

For the ATM implied volatility ($K = S_0$), the response to a spot move is:

$$
\frac{d\sigma_{\text{imp}}^{\text{ATM}}}{dS_0} = \frac{\partial \sigma_{\text{imp}}}{\partial S_0}\bigg|_{K=S_0} + \frac{\partial \sigma_{\text{imp}}}{\partial K}\bigg|_{K=S_0} \cdot \frac{dK_{\text{ATM}}}{dS_0}
$$

Since $K_{\text{ATM}} = S_0$ (the ATM strike moves with spot), $dK_{\text{ATM}}/dS_0 = 1$, and using $\partial_{S_0}\sigma_{\text{imp}} \approx \partial_K \sigma_{\text{imp}}$:

$$
\frac{d\sigma_{\text{imp}}^{\text{ATM}}}{dS_0} \approx 2\frac{\partial \sigma_{\text{imp}}}{\partial K}\bigg|_{K=S_0}
$$

For a typical equity skew with $\partial_K \sigma_{\text{imp}} < 0$, the ATM implied volatility **decreases** when the spot rises, with a sensitivity approximately twice the implied volatility skew slope.

## The Local Volatility Delta

### Delta in the Presence of Smile

In the Black-Scholes model, the delta of a European call is $\Delta_{\text{BS}} = \partial C / \partial S_0$ evaluated at constant volatility. In the local volatility model, the spot move changes not only the payoff but also the entire implied volatility surface. The **local volatility delta** (also called the **smile-adjusted delta** or **minimum variance delta**) accounts for this:

$$
\Delta_{\text{LV}} = \frac{\partial C}{\partial S_0}\bigg|_{\sigma_{\text{loc}} \text{ fixed}}
$$

**Proposition 13.3.5** (Local Volatility Delta Decomposition).
The local volatility delta can be decomposed as:

$$
\Delta_{\text{LV}} = \Delta_{\text{BS}} + \text{Vega}_{\text{BS}} \cdot \frac{\partial \sigma_{\text{imp}}}{\partial S_0}
$$

where $\Delta_{\text{BS}}$ and $\text{Vega}_{\text{BS}}$ are the Black-Scholes delta and vega evaluated at the current implied volatility.

*Proof.* The call price depends on $S_0$ both directly (through the payoff) and indirectly (through the change in implied volatility as spot moves):

$$
\frac{\partial C}{\partial S_0} = \frac{\partial C_{\text{BS}}}{\partial S_0}\bigg|_{\sigma \text{ fixed}} + \frac{\partial C_{\text{BS}}}{\partial \sigma} \cdot \frac{\partial \sigma_{\text{imp}}}{\partial S_0}
$$

The first term is the Black-Scholes delta; the second is the vega times the sensitivity of implied vol to spot. $\square$

Under the sticky strike approximation ($\partial_{S_0}\sigma_{\text{imp}} \approx \partial_K \sigma_{\text{imp}}$):

$$
\Delta_{\text{LV}} \approx \Delta_{\text{BS}} + \text{Vega}_{\text{BS}} \cdot \frac{\partial \sigma_{\text{imp}}}{\partial K}
$$

For equity options with negative skew ($\partial_K \sigma_{\text{imp}} < 0$):

- **OTM puts** ($K < S_0$): $\text{Vega} > 0$ and $\partial_K \sigma_{\text{imp}} < 0$, so $\Delta_{\text{LV}} < \Delta_{\text{BS}}$ (more negative delta)
- **OTM calls** ($K > S_0$): The correction $\text{Vega} \cdot \partial_K \sigma_{\text{imp}} < 0$ reduces the delta

The local volatility delta is systematically different from the Black-Scholes delta, and this difference has direct P&L consequences for hedgers.

## Implied Spot-Volatility Correlation

### Definition

The implied correlation between spot returns and ATM implied volatility changes is:

$$
\rho_{S, \sigma} = \text{Corr}\left(\frac{dS}{S}, d\sigma_{\text{imp}}^{\text{ATM}}\right)
$$

### Under Local Volatility

Since $d\sigma_{\text{imp}}^{\text{ATM}} \approx 2(\partial_K \sigma_{\text{imp}})(dS/S) \cdot S$, the spot return and the ATM vol change are perfectly (negatively) correlated:

$$
\rho_{S, \sigma}^{\text{LV}} = -1 \quad (\text{for equity with negative skew})
$$

This is because local volatility is deterministic: knowing the spot move completely determines the volatility change. There is no independent source of randomness in the volatility.

### Empirical Evidence

Empirically, the spot-vol correlation is strong but not perfect:

$$
\rho_{S, \sigma}^{\text{market}} \approx -0.5 \text{ to } -0.8 \quad (\text{equity indices})
$$

The local volatility model overstates the magnitude of the spot-vol correlation. Stochastic volatility models naturally produce $|\rho_{S,\sigma}| < 1$ because the volatility has its own source of randomness.

## Comparison: LV vs Market vs Stochastic Volatility

### Summary Table

| Feature | Local Volatility | Market (empirical) | Stochastic Volatility |
|---------|-----------------|-------------------|---------------------|
| Smile regime | Sticky strike | Between sticky strike and sticky delta | Closer to sticky delta |
| Spot-vol correlation | $-1$ (deterministic) | $-0.5$ to $-0.8$ | $\rho$ (parameter) |
| ATM vol change per spot move | $2 \partial_K \sigma_{\text{imp}}$ (too large) | Moderate | Depends on vol-of-vol |
| Forward smile | Too flat | Persistent | Persistent |
| Vol-of-vol | Zero | Positive | $\xi > 0$ (parameter) |

### Hedging Consequences

The smile dynamics determine the **delta hedging P&L**. If a hedger uses the local volatility delta but the true dynamics are closer to sticky delta:

- The hedger over-adjusts for the smile effect on vol
- Systematic P&L leakage occurs on each rebalancing
- The error is proportional to the vega times the discrepancy between actual and predicted $\partial_{S_0}\sigma_{\text{imp}}$

??? example "Numerical Example: Delta Comparison"

    **Setup.** An equity index call option with:

    - $S_0 = 100$, $K = 90$ (10% ITM), $T = 0.5$
    - $\sigma_{\text{imp}}(90, 0.5) = 0.24$, $\partial_K \sigma_{\text{imp}} = -0.001$
    - $r = 0.03$, $q = 0.01$

    **Black-Scholes delta:** $\Delta_{\text{BS}} = N(d_1) \approx 0.82$

    **Vega:** $\text{Vega}_{\text{BS}} = S_0 \phi(d_1)\sqrt{T} \approx 22.5$

    **Local volatility delta:**

    $$
    \Delta_{\text{LV}} \approx 0.82 + 22.5 \times (-0.001) = 0.82 - 0.0225 = 0.798
    $$

    The local volatility model predicts a delta about 2.7% lower (in absolute terms) than Black-Scholes, reflecting the fact that a spot increase also reduces the implied vol, partially offsetting the directional gain.

    If the true smile dynamics are sticky delta (the smile moves with spot, so $\partial_{S_0}\sigma_{\text{imp}} = 0$), then the correct delta is $\Delta_{\text{BS}} = 0.82$, and the local vol hedger is short 0.022 units of delta -- a systematic bias.

## The Backbone of the Smile

### Definition

The **backbone** (or **spine**) of the implied volatility surface is the function that gives the ATM implied volatility as a function of the spot level:

$$
\Sigma(S) = \sigma_{\text{imp}}(K = S, T; S)
$$

Under local volatility, the backbone slope is:

$$
\frac{d\Sigma}{dS} = \frac{\partial \sigma_{\text{imp}}}{\partial S_0}\bigg|_{K=S_0} + \frac{\partial \sigma_{\text{imp}}}{\partial K}\bigg|_{K=S_0} \approx 2\frac{\partial \sigma_{\text{imp}}}{\partial K}\bigg|_{K=S_0}
$$

For typical equity skew ($\partial_K \sigma_{\text{imp}} \approx -0.001$ per unit of $K$), the backbone has a slope of approximately $-0.002$ per unit of $S$: a \$1 increase in the index reduces ATM vol by 0.2 percentage points.

Empirically, the backbone is flatter than local volatility predicts, reflecting the partial sticky delta behavior of real markets.

## Summary

The smile dynamics under local volatility have a distinctive and empirically testable character:

1. **Sticky strike approximation**: $\partial_{S_0}\sigma_{\text{imp}} \approx \partial_K \sigma_{\text{imp}}$. The implied volatility of a fixed-strike option changes when spot moves, with the smile anchored to absolute strike levels.
2. **ATM vol response**: ATM implied volatility changes by approximately $2(\partial_K \sigma_{\text{imp}}) \cdot \Delta S$ when spot moves by $\Delta S$, which is too aggressive compared to empirical data.
3. **Local vol delta**: $\Delta_{\text{LV}} = \Delta_{\text{BS}} + \text{Vega} \cdot \partial_K \sigma_{\text{imp}}$, systematically different from the Black-Scholes delta.
4. **Perfect spot-vol correlation**: Local volatility implies $\rho_{S,\sigma} = -1$, overstating the empirical correlation.
5. **Hedging implications**: Using the local volatility delta when the true dynamics are closer to sticky delta produces systematic P&L leakage proportional to vega times the dynamics mismatch.
6. **The backbone**: The ATM vol-vs-spot function under local volatility is steeper than empirically observed, reflecting the model's overstatement of the spot-vol link.
