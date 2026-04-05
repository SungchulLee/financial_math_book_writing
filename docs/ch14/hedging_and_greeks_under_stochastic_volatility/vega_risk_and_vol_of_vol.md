# Vega Risk and Vol-of-Vol


Under stochastic volatility, option risk is no longer captured by delta alone. **Vega risk** and, more subtly, **volatility-of-volatility (vol-of-vol) risk** become central drivers of P&L and hedging performance.

---

## Vega in stochastic volatility models


In Black–Scholes, vega measures sensitivity to a single volatility parameter:

\[
\text{Vega} = \partial_{\sigma} P.
\]



In stochastic volatility models, volatility itself is random, so vega represents sensitivity to:
- the current variance level,
- the volatility state variable,
- the implied volatility surface.

Thus, vega is model- and state-dependent.

---

## Vol-of-vol risk


The parameter (or process) controlling volatility fluctuations—often denoted \(\xi\)—introduces **second-order volatility risk**.

Consequences:
- option prices depend on uncertainty of future volatility,
- convexity in volatility matters,
- products sensitive to smile curvature are especially exposed.

This risk cannot be hedged by delta or vega alone.

---

## Greeks beyond vega


Common higher-order sensitivities include:
- **Volga (vomma):** sensitivity of vega to volatility,
- **Vanna:** cross-sensitivity between spot and volatility,
- sensitivities to variance process parameters.

These Greeks are typically large for long-dated or exotic options.

---

## Practical implications


- Vega hedging with a single option is insufficient.
- Smile dynamics cause residual P&L even for delta–vega neutral portfolios.
- Vol-of-vol risk explains persistent hedging errors in practice.

---

## Key takeaways


- Vega risk is richer under stochastic volatility.
- Vol-of-vol introduces unhedgeable second-order effects.
- Understanding higher-order Greeks is essential for risk management.

---

## Further reading


- Taleb, *Dynamic Hedging*.
- Bergomi, *Stochastic Volatility Modeling*.

---

## Exercises

**Exercise 1.** In the Black-Scholes model, vega is $\partial C/\partial\sigma$, a sensitivity to a single constant parameter. In the Heston model, explain why there are multiple "vega-like" sensitivities: $\partial C/\partial V_0$ (spot variance), $\partial C/\partial\theta$ (long-run variance), and $\partial C/\partial\xi$ (vol-of-vol). For a short-maturity ATM call, which of these three is most important and why?

??? success "Solution to Exercise 1"
    In the Black-Scholes model, there is a single constant volatility parameter $\sigma$, and vega is simply $\partial C / \partial\sigma$. The entire volatility surface is flat, so one number characterizes all volatility risk.

    In the Heston model, the variance follows

    $$
    dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V
    $$

    and option prices depend on $V_0$ (current variance), $\theta$ (long-run variance), and $\xi$ (vol-of-vol) separately. Each generates a distinct sensitivity:

    - $\partial C / \partial V_0$: Sensitivity to the **current** variance level. This is the most direct analogue of Black-Scholes vega. It captures how the option price changes if today's instantaneous variance shifts.

    - $\partial C / \partial\theta$: Sensitivity to the **long-run** mean variance. This affects the option primarily through the expected future average variance over the option's life. It is more important for longer-dated options.

    - $\partial C / \partial\xi$: Sensitivity to **vol-of-vol**. This captures how the option price depends on the uncertainty of future volatility itself. It primarily affects the curvature (convexity) of the implied volatility smile.

    For a **short-maturity ATM call**, $\partial C / \partial V_0$ is the most important. Over a short horizon, the variance has little time to mean-revert toward $\theta$, so the current level $V_0$ dominates the expected integrated variance. The sensitivity to $\theta$ is small because mean reversion has minimal effect over short periods. The sensitivity to $\xi$ is also relatively small for short maturities because there is less time for variance to fluctuate. As maturity increases, the sensitivities to $\theta$ and $\xi$ become progressively more important.

---

**Exercise 2.** Volga (or vomma) is defined as

$$
\text{Volga} = \frac{\partial^2 C}{\partial\sigma^2} = \frac{\partial\,\text{Vega}}{\partial\sigma}
$$

For a Black-Scholes call, $\text{Volga} = S\sqrt{T}\,n(d_1)\,\frac{d_1 d_2}{\sigma}$ where $n$ is the standard normal density. Compute volga for an ATM call with $S = 100$, $K = 100$, $T = 1$, $\sigma = 0.20$, $r = 0.03$. Is volga positive or negative for ATM options? How does it change for deep OTM options?

??? success "Solution to Exercise 2"
    For an ATM call, $K = S = 100$, $T = 1$, $\sigma = 0.20$, $r = 0.03$. First compute $d_1$ and $d_2$:

    $$
    d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}} = \frac{0 + (0.03 + 0.02) \times 1}{0.20 \times 1} = \frac{0.05}{0.20} = 0.25
    $$

    $$
    d_2 = d_1 - \sigma\sqrt{T} = 0.25 - 0.20 = 0.05
    $$

    The standard normal density at $d_1 = 0.25$ is

    $$
    n(0.25) = \frac{1}{\sqrt{2\pi}}\,e^{-0.25^2/2} = \frac{1}{\sqrt{2\pi}}\,e^{-0.03125} \approx 0.3867
    $$

    Now compute volga:

    $$
    \text{Volga} = S\sqrt{T}\,n(d_1)\,\frac{d_1\,d_2}{\sigma} = 100 \times 1 \times 0.3867 \times \frac{0.25 \times 0.05}{0.20}
    $$

    $$
    = 100 \times 0.3867 \times \frac{0.0125}{0.20} = 100 \times 0.3867 \times 0.0625 \approx 2.417
    $$

    For ATM options, volga is **positive** (since $d_1 > 0$ and $d_2 > 0$ when $r > 0$, making $d_1 d_2 > 0$). When ATM is defined as $d_1 d_2 > 0$, volga is positive, meaning vega increases as volatility rises — the option has convexity in volatility.

    For **deep OTM options**, both $|d_1|$ and $|d_2|$ are large and have the same sign (both large and negative for OTM calls). The product $d_1 d_2$ is large and positive, making volga large. However, $n(d_1)$ decays exponentially for large $|d_1|$, creating a competing effect. In practice, the product $n(d_1) d_1 d_2 / \sigma$ is typically larger for OTM options than for ATM options, so **deep OTM options have higher volga**. This is why OTM options are most sensitive to vol-of-vol and exhibit the strongest smile effects.

---

**Exercise 3.** Vanna measures the cross-sensitivity between spot and volatility:

$$
\text{Vanna} = \frac{\partial^2 C}{\partial S\,\partial\sigma} = \frac{\partial\Delta}{\partial\sigma}
$$

Explain why vanna is especially important when $\rho < 0$ (leverage effect). If the S&P 500 drops 5% and volatility simultaneously increases by 3 vol points, estimate the additional delta change for a portfolio with vanna exposure of $0.05$. Should a trader who is long vanna be worried about a market crash?

??? success "Solution to Exercise 3"
    Vanna measures how delta changes with volatility:

    $$
    \text{Vanna} = \frac{\partial\Delta}{\partial\sigma} = \frac{\partial^2 C}{\partial S\,\partial\sigma}
    $$

    When $\rho < 0$ (leverage effect), spot declines are associated with volatility increases. This means that when the market drops, two things happen simultaneously: (1) the spot moves down, changing delta through gamma, and (2) volatility rises, changing delta through vanna. If the trader ignores vanna, the delta adjustment from the spot move alone underestimates the true change in the option's delta.

    For the given scenario with vanna exposure of $0.05$:

    The additional delta change from the volatility move is

    $$
    \Delta(\text{additional}) = \text{Vanna} \times d\sigma = 0.05 \times 0.03 = 0.0015
    $$

    per unit of notional. This adds to the gamma-induced delta change. For a portfolio, the dollar impact depends on the notional. For example, with 1000 options, the additional delta is $1000 \times 0.0015 = 1.5$ shares of equivalent exposure.

    A trader who is **long vanna** has $\partial\Delta/\partial\sigma > 0$: when volatility increases, delta increases (becomes more positive). In a market crash ($dS < 0$, $d\sigma > 0$), the long-vanna position becomes more delta-positive (or less delta-negative) precisely when the market is falling. This means the position **gains additional long exposure** into a falling market, amplifying losses. Yes, a trader who is long vanna should be concerned about a crash scenario because the vanna effect moves delta in the wrong direction during the most dangerous market moves.

---

**Exercise 4.** A delta-vega hedged portfolio has zero exposure to both spot price changes and parallel shifts in implied volatility. However, the portfolio still has P&L risk. Identify at least three sources of residual risk and explain which stochastic volatility parameters they relate to. For each source, name a potential hedging instrument.

??? success "Solution to Exercise 4"
    A delta-vega hedged portfolio has $\Delta_{\text{total}} = 0$ and $\text{Vega}_{\text{total}} = 0$. Despite this, residual P&L risk comes from at least three sources:

    1. **Vanna risk** ($\partial^2 C / \partial S\,\partial\sigma$): When spot and volatility move simultaneously (governed by the correlation $\rho$ in Heston), the cross-term $\text{Vanna}\,dS\,d\sigma$ generates P&L. Delta-vega hedging does not neutralize this second-order effect. *Related parameter:* $\rho$ (spot-vol correlation). *Hedging instrument:* Risk reversals (long OTM put, short OTM call) have significant vanna and can offset this exposure.

    2. **Volga risk** ($\partial^2 C / \partial\sigma^2$): Large volatility moves create P&L through the convexity term $\frac{1}{2}\text{Volga}\,(d\sigma)^2$. The vega hedge neutralizes first-order vol moves but not second-order effects. *Related parameter:* $\xi$ (vol-of-vol). *Hedging instrument:* Butterfly spreads or strangles, which have high volga, can be used. Alternatively, VIX options provide direct vol-of-vol exposure.

    3. **Gamma risk from discrete rebalancing**: Delta is neutralized at a point in time, but gamma causes delta to change with the spot. Discrete rebalancing leads to gamma P&L $\frac{1}{2}\Gamma(dS)^2$ that is not perfectly offset. *Related parameter:* Instantaneous variance $V_t$. *Hedging instrument:* Matching gamma by choosing the hedging option with gamma close to that of the hedged position, or adding a second option to flatten gamma.

    Additional sources include **term-structure risk** (the vega hedge option and the hedged position may have different maturities, so parallel vol shifts do not perfectly offset), **mean-reversion risk** (sensitivity to $\kappa$, affecting how quickly variance reverts), and **jump risk** (if jumps are present in the model extension).

---

**Exercise 5.** The vol-of-vol parameter $\xi$ in the Heston model controls the curvature of the implied volatility smile. Consider two portfolios: (a) a short butterfly spread (short wings, long center) and (b) a long straddle. Which portfolio has greater exposure to changes in $\xi$? Explain using the relationship between smile curvature and butterfly prices.

??? success "Solution to Exercise 5"
    The vol-of-vol parameter $\xi$ controls the curvature (convexity) of the implied volatility smile. Higher $\xi$ produces a more pronounced smile with fatter tails in the risk-neutral distribution.

    **(a) Short butterfly spread** (short wings, long center): A butterfly spread's value is directly related to the probability density at the center strike relative to the wing strikes. The price of a butterfly at strike $K$ approximates the risk-neutral density at $K$:

    $$
    \text{Butterfly}(K) \approx e^{rT}\,f(K)\,(\Delta K)^2
    $$

    where $f(K)$ is the risk-neutral density. The wings of the butterfly are sensitive to the tails of the distribution. When $\xi$ increases, the smile curvature increases, which means the wings become relatively more expensive (higher OTM option prices) and the center relatively cheaper. A short butterfly (which is short the wings) benefits from flattening of the smile and loses when smile curvature increases.

    **(b) Long straddle**: A straddle (long ATM call + long ATM put) is primarily sensitive to the level of implied volatility (vega), not to the curvature. Its volga is relatively small near ATM.

    The **short butterfly** has **greater exposure to changes in $\xi$** because butterfly prices directly reflect smile curvature. The relationship is: butterfly price $\propto$ curvature of the implied vol smile $\propto$ vol-of-vol $\xi$. A short butterfly is short smile curvature and therefore short $\xi$ — it loses money when $\xi$ increases. The long straddle, by contrast, is primarily a directional bet on the volatility level and has much smaller sensitivity to $\xi$.

---

**Exercise 6.** A risk manager wants to decompose the daily P&L of a stochastic-volatility-priced option portfolio. Propose a decomposition into the following components and explain how each is computed:

$$
\text{Total P\&L} = \Delta\,dS + \text{Vega}\,d\sigma + \frac{1}{2}\Gamma(dS)^2 + \text{Vanna}\,dS\,d\sigma + \frac{1}{2}\text{Volga}(d\sigma)^2 + \text{Theta}\,dt + \text{Residual}
$$

If $dS = -2$, $d\sigma = +0.015$, $\Delta = 0.50$, $\Gamma = 0.02$, Vega $= 20$, Vanna $= 0.03$, Volga $= 1.5$, Theta $= -0.05$, and $dt = 1/252$, compute each component and the total P&L (assuming zero residual).

??? success "Solution to Exercise 6"
    The P&L decomposition is

    $$
    \text{Total P\&L} = \Delta\,dS + \text{Vega}\,d\sigma + \frac{1}{2}\Gamma(dS)^2 + \text{Vanna}\,dS\,d\sigma + \frac{1}{2}\text{Volga}(d\sigma)^2 + \text{Theta}\,dt
    $$

    Computing each component with the given values:

    **Delta P&L:**

    $$
    \Delta\,dS = 0.50 \times (-2) = -1.000
    $$

    **Vega P&L:**

    $$
    \text{Vega}\,d\sigma = 20 \times 0.015 = +0.300
    $$

    **Gamma P&L:**

    $$
    \frac{1}{2}\Gamma(dS)^2 = \frac{1}{2} \times 0.02 \times (-2)^2 = \frac{1}{2} \times 0.02 \times 4 = +0.040
    $$

    **Vanna P&L:**

    $$
    \text{Vanna}\,dS\,d\sigma = 0.03 \times (-2) \times 0.015 = -0.0009
    $$

    **Volga P&L:**

    $$
    \frac{1}{2}\text{Volga}(d\sigma)^2 = \frac{1}{2} \times 1.5 \times (0.015)^2 = \frac{1}{2} \times 1.5 \times 0.000225 = +0.000169
    $$

    **Theta P&L:**

    $$
    \text{Theta}\,dt = -0.05 \times \frac{1}{252} = -0.000198
    $$

    **Total P&L** (with zero residual):

    $$
    \text{Total} = -1.000 + 0.300 + 0.040 - 0.0009 + 0.000169 - 0.000198 \approx -0.661
    $$

    The dominant contributors are the delta term ($-1.000$) and the vega term ($+0.300$). The gamma term ($+0.040$) is a modest positive contribution reflecting the convexity gain from the spot move. The vanna, volga, and theta terms are all very small for a single-day move of this magnitude. The net P&L of approximately $-0.661$ is driven primarily by the spot decline, partially offset by the volatility increase — consistent with a long position that benefits from rising vol but suffers from falling spot.
