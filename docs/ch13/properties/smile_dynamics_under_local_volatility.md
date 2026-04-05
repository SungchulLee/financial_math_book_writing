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

---

## Exercises

**Exercise 1.** Define sticky strike and sticky delta smile dynamics. For each regime, state what happens to the implied volatility of a fixed-strike call option when the spot price increases by \$1. Which regime does the local volatility model produce, and why?

??? success "Solution to Exercise 1"
    **Sticky strike:** The implied volatility of a fixed-strike option is a function of the absolute strike $K$ only and does not change when the spot moves. When the spot increases by \$1, the implied volatility at a fixed strike $K$ remains unchanged: $\Delta\sigma_{\text{imp}}(K) = 0$. However, the ATM implied volatility changes because the ATM strike shifts to $S_0 + 1$, where the smile has a different value.

    **Sticky delta:** The implied volatility of a fixed-moneyness option (e.g., 25-delta put) does not change when the spot moves. Equivalently, the smile is a function of $K/S_0$ rather than $K$. When the spot increases by \$1, the entire smile translates to the right by \$1, and the implied volatility at any fixed strike $K$ changes by approximately $\partial_K \sigma_{\text{imp}} \cdot \Delta S$.

    **For a fixed-strike call when spot increases by \$1:**

    - Under sticky strike: $\Delta\sigma_{\text{imp}}(K) = 0$
    - Under sticky delta: $\Delta\sigma_{\text{imp}}(K) \approx -\frac{\partial \sigma_{\text{imp}}}{\partial K} \cdot 1$ (for negative skew, this is positive -- vol at fixed $K$ increases as spot rises past it, because the option becomes more OTM put-like in moneyness)

    **The local volatility model produces sticky strike behavior.** This is because the BBF approximation gives $\partial_{S_0}\sigma_{\text{imp}} \approx \partial_K \sigma_{\text{imp}}$, which means a unit increase in spot changes implied vol at fixed strike by approximately $\partial_K \sigma_{\text{imp}}$. Since the implied vol changes by the same amount whether the strike decreases or the spot increases, the smile is effectively anchored to absolute strike levels. This arises because local volatility is a deterministic function of $S$ and $t$ -- there is no independent randomness in volatility, so the spot uniquely determines the volatility.

---

**Exercise 2.** Under sticky strike dynamics, the ATM implied volatility changes by approximately $2(\partial_K \sigma_{\text{imp}}) \cdot \Delta S$ when spot moves by $\Delta S$. For an equity index with implied volatility skew $\partial_K \sigma_{\text{imp}} = -0.0008$ per unit of $K$ and a spot move of $\Delta S = +5$, compute the change in ATM implied volatility. Is this increase or decrease consistent with the empirical "leverage effect"?

??? success "Solution to Exercise 2"
    Under sticky strike (local volatility) dynamics, the ATM implied volatility changes by:

    $$
    \Delta\sigma_{\text{imp}}^{\text{ATM}} \approx 2 \frac{\partial \sigma_{\text{imp}}}{\partial K}\bigg|_{K=S_0} \cdot \Delta S
    $$

    With $\partial_K \sigma_{\text{imp}} = -0.0008$ and $\Delta S = +5$:

    $$
    \Delta\sigma_{\text{imp}}^{\text{ATM}} \approx 2(-0.0008)(5) = -0.008
    $$

    The ATM implied volatility decreases by 0.8 percentage points (e.g., from $20\%$ to $19.2\%$).

    **Yes, this is consistent with the leverage effect.** The leverage effect is the empirical observation that equity volatility tends to increase when stock prices fall and decrease when stock prices rise. Here, a \$5 spot increase produces a decrease in ATM implied volatility, which matches this stylized fact. The negative skew ($\partial_K \sigma_{\text{imp}} < 0$) encodes the leverage effect: lower strikes (associated with price declines) carry higher implied volatility. The local volatility model reproduces this directionally, though it overstates the magnitude (the factor of 2 makes the response too aggressive compared to empirical data).

---

**Exercise 3.** Compute the local volatility delta for a European call with the following data: $S_0 = 100$, $K = 105$ (5% OTM), $T = 1.0$, $\sigma_{\text{imp}} = 0.18$, $\partial_K \sigma_{\text{imp}} = -0.0010$, Black-Scholes delta $\Delta_{\text{BS}} = 0.42$, and Black-Scholes vega $\text{Vega}_{\text{BS}} = 35.2$. How much does the smile adjustment change the delta relative to Black-Scholes?

??? success "Solution to Exercise 3"
    The local volatility delta is:

    $$
    \Delta_{\text{LV}} = \Delta_{\text{BS}} + \text{Vega}_{\text{BS}} \cdot \frac{\partial \sigma_{\text{imp}}}{\partial K}
    $$

    Substituting the given values:

    $$
    \Delta_{\text{LV}} = 0.42 + 35.2 \times (-0.0010) = 0.42 - 0.0352 = 0.3848
    $$

    **The smile adjustment reduces the delta by $0.0352$**, a relative change of $0.0352/0.42 \approx 8.4\%$ compared to the Black-Scholes delta.

    The reduction occurs because the negative implied vol skew means that when the spot rises, the implied volatility at the fixed strike $K = 105$ decreases (the option moves further OTM and into a lower-vol region). This vol decrease partially offsets the directional gain from the spot increase, so the effective sensitivity to spot is lower than the Black-Scholes delta computed at constant volatility.

---

**Exercise 4.** The local volatility model implies a spot-volatility correlation of $\rho_{S, \sigma}^{\text{LV}} = -1$ for equity indices. Empirical values are typically $-0.5$ to $-0.8$. Explain why the local volatility model produces $|\rho| = 1$, and discuss the practical hedging consequences when the true correlation is only $-0.7$.

??? success "Solution to Exercise 4"
    **Why local volatility produces $|\rho| = 1$:** In the local volatility model, the instantaneous volatility is $\sigma_{\text{loc}}(S_t, t)$, a deterministic function of spot and time. There is no independent source of randomness driving the volatility -- it is completely determined by the spot path. Therefore, if you know $dS_t$, you know $d\sigma_{\text{loc}}$ exactly (via the chain rule). The implied volatility, being a functional of the local volatility surface and the spot level, also moves deterministically with spot. This means:

    $$
    d\sigma_{\text{imp}}^{\text{ATM}} \approx 2(\partial_K \sigma_{\text{imp}}) \cdot dS
    $$

    The ATM vol change is a deterministic (negative) multiple of the spot change, giving $\rho_{S,\sigma}^{\text{LV}} = -1$.

    **Hedging consequences when the true correlation is $-0.7$:** If the hedger uses the local volatility delta $\Delta_{\text{LV}} = \Delta_{\text{BS}} + \text{Vega} \cdot \partial_K \sigma_{\text{imp}}$, the smile adjustment term assumes $|\rho| = 1$. But if the true spot-vol correlation is only $-0.7$, only $70\%$ of the assumed vol change actually occurs in response to a spot move. The hedger over-corrects for the smile effect.

    The delta error is:

    $$
    \Delta_{\text{error}} = \text{Vega} \cdot \partial_K \sigma_{\text{imp}} \cdot (1 - 0.7) = 0.3 \cdot \text{Vega} \cdot \partial_K \sigma_{\text{imp}}
    $$

    This produces systematic hedging P&L leakage: the hedger holds too little delta (for negative skew), and each spot move generates a small but persistent loss. Over many rebalancing periods, this bias accumulates and can materially affect the total hedging P&L.

---

**Exercise 5.** The backbone of the implied volatility surface is $\Sigma(S) = \sigma_{\text{imp}}(K = S, T; S)$. Under local volatility, the backbone slope is approximately $d\Sigma/dS \approx 2 \partial_K \sigma_{\text{imp}}|_{K=S_0}$. If the implied volatility skew at $K = S_0$ is $-0.0012$ per unit, compute the backbone slope and interpret it: by how many volatility points does ATM implied volatility change for a \$10 move in the spot?

??? success "Solution to Exercise 5"
    The backbone slope under local volatility is:

    $$
    \frac{d\Sigma}{dS} \approx 2\frac{\partial \sigma_{\text{imp}}}{\partial K}\bigg|_{K = S_0}
    $$

    With $\partial_K \sigma_{\text{imp}}|_{K=S_0} = -0.0012$:

    $$
    \frac{d\Sigma}{dS} \approx 2(-0.0012) = -0.0024
    $$

    **Interpretation:** For a \$10 move in the spot:

    $$
    \Delta\sigma_{\text{imp}}^{\text{ATM}} \approx -0.0024 \times 10 = -0.024
    $$

    The ATM implied volatility changes by $-2.4$ percentage points (e.g., from $20\%$ to $17.6\%$) for a \$10 spot increase. Conversely, a \$10 spot decrease would increase ATM implied volatility by $2.4$ percentage points.

    This backbone slope of $-0.24\%$ of vol per \$1 of spot means the local volatility model predicts a strong inverse relationship between spot and ATM vol. In practice, empirical backbone slopes are typically flatter (e.g., $-0.15\%$ to $-0.18\%$ per \$1 for equity indices), reflecting the fact that real markets exhibit behavior between sticky strike and sticky delta.

---

**Exercise 6.** A hedger uses the local volatility delta $\Delta_{\text{LV}} = \Delta_{\text{BS}} + \text{Vega} \cdot \partial_K \sigma_{\text{imp}}$ but the true market dynamics are sticky delta (so the correct delta is $\Delta_{\text{BS}}$). The position has $\text{Vega} = 50$ and $\partial_K \sigma_{\text{imp}} = -0.001$. Compute the daily P&L leakage from the delta mismatch if the stock moves by $\Delta S = \pm 2$ each day.

??? success "Solution to Exercise 6"
    The hedger's delta error from the smile adjustment is:

    $$
    \Delta_{\text{error}} = \text{Vega} \cdot \partial_K \sigma_{\text{imp}} = 50 \times (-0.001) = -0.05
    $$

    The hedger holds $0.05$ fewer shares than the correct delta. When the stock moves by $\Delta S$, the P&L from this delta mismatch is:

    $$
    \text{P\&L}_{\text{error}} = -\Delta_{\text{error}} \cdot \Delta S = -(-0.05) \cdot \Delta S = 0.05 \cdot \Delta S
    $$

    Wait -- we need to be more careful. The hedger uses $\Delta_{\text{LV}} = \Delta_{\text{BS}} - 0.05$, but the correct delta (under sticky delta) is $\Delta_{\text{BS}}$. The hedge portfolio holds $\Delta_{\text{LV}}$ shares but should hold $\Delta_{\text{BS}}$ shares. The hedger is short $0.05$ shares relative to the correct hedge.

    The daily P&L leakage from the mismatch is:

    $$
    \text{P\&L}_{\text{leakage}} = (\Delta_{\text{BS}} - \Delta_{\text{LV}}) \cdot \Delta S = 0.05 \cdot \Delta S
    $$

    For $\Delta S = +2$: P&L leakage $= 0.05 \times 2 = \$0.10$ (the hedger loses because they are short delta).

    For $\Delta S = -2$: P&L leakage $= 0.05 \times (-2) = -\$0.10$ (the hedger gains).

    On any individual day, the P&L leakage is $\pm\$0.10$ depending on the direction of the move. However, if the position has negative gamma (typical for option sellers), the directional bias means the losses from the delta mismatch do not cancel over time. The expected daily P&L impact is zero only if moves are symmetric and independent. In practice, the systematic mispricing of smile dynamics leads to a persistent bias in the hedging P&L that accumulates over the life of the option.

---

**Exercise 7.** Compare the smile dynamics predictions of local volatility, the Heston stochastic volatility model, and SABR. For each model, state: (a) the smile regime (sticky strike, sticky delta, or intermediate), (b) the implied spot-vol correlation, and (c) the qualitative behavior of the forward smile.

??? success "Solution to Exercise 7"
    **(a) Smile regime:**

    - **Local volatility:** Sticky strike. The implied vol at a fixed strike does not change when spot moves; the smile is anchored to absolute strike levels. This follows from $\partial_{S_0}\sigma_{\text{imp}} \approx \partial_K \sigma_{\text{imp}}$.
    - **Heston:** Intermediate, closer to sticky delta. The stochastic volatility evolves semi-independently of spot (modulated by the correlation $\rho$), so the smile partially moves with spot. The exact behavior depends on $\rho$ and the vol-of-vol $\xi$.
    - **SABR:** Close to sticky delta for the standard parameterization with $\beta < 1$. The SABR model was specifically designed to produce realistic smile dynamics, and its backbone is flatter than local volatility.

    **(b) Implied spot-vol correlation:**

    - **Local volatility:** $\rho_{S,\sigma} = -1$ (for negative equity skew). The volatility is a deterministic function of spot, so spot and vol are perfectly correlated.
    - **Heston:** $\rho_{S,\sigma} = \rho$ (the model parameter), typically in the range $-0.5$ to $-0.9$ for equities. The correlation is a free parameter that can be calibrated to market data.
    - **SABR:** $\rho_{S,\sigma} = \rho$ (the model parameter). Like Heston, the correlation between the forward and its volatility is an input to the model.

    **(c) Forward smile behavior:**

    - **Local volatility:** The forward smile is too flat. As time progresses and the spot moves, the local volatility model predicts that the future implied volatility smile will be much flatter than today's smile. This is the well-known "flattening of the forward smile" under local volatility.
    - **Heston:** The forward smile is persistent. The stochastic nature of volatility ensures that the smile regenerates itself over time, because the vol-of-vol parameter $\xi > 0$ continually produces new curvature.
    - **SABR:** The forward smile is also persistent, similar to Heston. The stochastic volatility component ensures that the smile does not flatten excessively. This is one of the primary advantages of SABR over pure local volatility in pricing forward-starting and cliquet products.
