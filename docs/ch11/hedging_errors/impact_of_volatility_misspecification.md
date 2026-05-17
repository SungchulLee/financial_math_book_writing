# Impact of Volatility Misspecification

If the hedger uses $\hat{\sigma}$ while true volatility is $\sigma$, replication fails systematically. Understanding this failure mode is central to practical options trading and motivates implied-vs-realized volatility strategies.

!!! tip "Toy mechanism: the gamma term is paid in the *realized* $\sigma^2$"
    The whole misspecification analysis is one substitution into the BS PDE. The hedger's portfolio is delta-neutral *under* $\hat\sigma$, so its theta satisfies $\hat\Theta + \tfrac{1}{2}\hat\sigma^2 S^2\hat\Gamma = r\hat V - rS\hat\Delta$. But the underlying actually moves with realized $\sigma$, so the hedged P&L picks up gamma at the *true* variance rate: $dP\&L = \hat\Theta\,dt + \tfrac{1}{2}\hat\Gamma\,\sigma^2 S^2\,dt$. Subtracting one from the other collapses to the single fundamental identity $dP\&L = \tfrac{1}{2}\hat\Gamma S^2(\sigma^2 - \hat\sigma^2)\,dt$. *The hedging P&L is proportional to the variance gap, weighted by gamma.* Implied–vs–realized vol strategies, robustness bounds, and the El Karoui–Jeanblanc result below are all corollaries of this one identity.

---

## The fundamental hedging P&L identity


Consider a delta-hedged European option position. The hedger computes delta using an assumed volatility $\hat{\sigma}$, but the underlying evolves with true (realized) volatility $\sigma$. Over an infinitesimal interval, the delta-hedged P&L is

$$
dP\&L_{\text{hedged}} = \hat{\Theta}\,dt + \frac{1}{2}\hat{\Gamma}\,\sigma^2 S^2\,dt
$$

where $\hat{\Theta}$ and $\hat{\Gamma}$ are theta and gamma computed under $\hat{\sigma}$. The Black–Scholes PDE under the hedge volatility gives

$$
\hat{\Theta} + \frac{1}{2}\hat{\sigma}^2 S^2 \hat{\Gamma} + rS\hat{\Delta} - r\hat{V} = 0
$$

Combining and integrating over $[0,T]$, the cumulative hedging error is

$$
\boxed{
\varepsilon = \frac{1}{2}\int_0^T \Gamma(t,S_t)\left(\sigma^2 - \hat{\sigma}^2\right)S_t^2\,\mathrm{d}t
}
$$

This is the **El Karoui–Jeanblanc–Shreve** (1998) result in its simplest form. Note that $\Gamma$ here is evaluated along the true path $S_t$, making $\varepsilon$ path-dependent.

---

## Sign analysis


For a standard long option position where $\Gamma > 0$ throughout:

| Scenario | Condition | Effect on hedging P&L |
|---|---|---|
| **Underestimate vol** | $\hat{\sigma} < \sigma$ | $\varepsilon > 0$: hedger gains (option was underpriced) |
| **Overestimate vol** | $\hat{\sigma} > \sigma$ | $\varepsilon < 0$: hedger loses (option was overpriced) |
| **Correct vol** | $\hat{\sigma} = \sigma$ | $\varepsilon = 0$: perfect replication |

From the perspective of the option **seller** who delta-hedges:

- Selling at implied vol $\hat{\sigma}$ and hedging while realized vol is $\sigma < \hat{\sigma}$ yields a profit.
- This is the basis of **short volatility** strategies: sell expensive implied vol and harvest the difference when realized vol is lower.

---

## Decomposition into dollar gamma


Define **dollar gamma** as

$$
\Gamma_\$ := \frac{1}{2}\Gamma S^2
$$

Then the hedging error becomes

$$
\varepsilon = \int_0^T \Gamma_\$(t,S_t)\left(\sigma^2 - \hat{\sigma}^2\right)\,\mathrm{d}t
$$

For small misspecification $\sigma = \hat{\sigma} + \delta\sigma$:

$$
\sigma^2 - \hat{\sigma}^2 \approx 2\hat{\sigma}\,\delta\sigma
$$

so

$$
\varepsilon \approx 2\hat{\sigma}\,\delta\sigma \int_0^T \Gamma_\$(t,S_t)\,\mathrm{d}t
$$

This shows the hedging error scales linearly with volatility misspecification for small errors and is weighted by the path-integrated dollar gamma.

---

## Time-varying volatility


When the true volatility is stochastic or time-varying, $\sigma = \sigma(t)$, the integral generalizes to

$$
\varepsilon = \frac{1}{2}\int_0^T \Gamma(t,S_t)\left(\sigma(t)^2 - \hat{\sigma}^2\right)S_t^2\,\mathrm{d}t
$$

Key consequences:

- **When** the volatility differs matters, not just the average difference. Misspecification during high-gamma periods (near strike, near expiry) has outsized impact.
- Even if $\frac{1}{T}\int_0^T \sigma(t)^2\,dt = \hat{\sigma}^2$ (correct average variance), the hedging error need not vanish due to the $\Gamma$-weighting.

---

## Variance swap interpretation


The hedging error can be rewritten using the realized variance $\sigma_R^2 = \frac{1}{T}\int_0^T \sigma(t)^2\,dt$:

$$
\varepsilon = T\left(\sigma_R^2 - \hat{\sigma}^2\right)\cdot \overline{\Gamma_\$}
$$

where $\overline{\Gamma_\$}$ is the gamma-weighted average. This connects volatility misspecification hedging errors to **variance swap** payoffs and motivates the use of variance swaps as hedging instruments for volatility exposure.

---

## Implied volatility trading intuition


The hedging P&L identity provides the theoretical foundation for the core options trading heuristic:

- **Sell options** (collect premium) when you believe implied vol $\hat{\sigma}$ exceeds expected future realized vol $\sigma$.
- **Buy options** when you believe implied vol understates future realized vol.

The expected P&L from this trade is approximately

$$
\mathbb{E}[\text{P\&L}] \approx \bar{\Gamma}_\$ \cdot T \cdot \left(\sigma_{\text{implied}}^2 - \sigma_{\text{realized}}^2\right)
$$

This is sometimes called the **variance risk premium** when systematically exploited.

---

## Higher-order effects


The simple $\Gamma(\sigma^2 - \hat{\sigma}^2)$ formula ignores several practical complications:

- **Path dependence of gamma**: $\Gamma$ itself changes along the path, and the hedge ratios computed under $\hat{\sigma}$ differ from those under $\sigma$, introducing second-order errors.
- **Vega-gamma cross effects**: when volatility shifts discretely, both $\Gamma$ and $\Delta$ change simultaneously.
- **Discrete rebalancing**: in practice, rebalancing frequency interacts with volatility misspecification to amplify errors (see *Discrete-Time Hedging Error*).

A more precise expansion accounting for the mismatch in hedge ratios gives

$$
\varepsilon = \frac{1}{2}\int_0^T \hat{\Gamma}(t,S_t)\left(\sigma^2 - \hat{\sigma}^2\right)S_t^2\,dt + \text{higher-order path-dependent terms}
$$

where using $\hat{\Gamma}$ (computed under the hedge model) versus $\Gamma$ (true model) introduces corrections of order $(\sigma - \hat{\sigma})^2$.

---

## Robustness considerations


The sensitivity to volatility misspecification motivates several practical approaches:

- **Uncertain volatility models** (Avellaneda, Levy, Parás): assume $\sigma \in [\sigma_{\min}, \sigma_{\max}]$ and solve for worst-case bounds.
- **Local volatility hedging**: use $\sigma(t,S)$ fitted to the smile to reduce misspecification.
- **Vega hedging**: trade additional options to neutralize sensitivity to volatility changes, partially mitigating the impact of misspecification.
- **Frequent recalibration**: update $\hat{\sigma}$ as new market data arrives.

---

## What to remember


- Gamma converts variance mismatch into systematic hedging P&L drift.
- The sign of the hedging error depends on whether realized vol exceeds or falls below the hedge vol, weighted by the gamma profile along the path.
- This motivates implied-vs-realized volatility trading intuition and the variance risk premium.
- When misspecification occurs matters as much as how much, due to gamma weighting.
- The framework connects naturally to variance swaps, uncertain volatility models, and robust hedging.

---

## Exercises

**Exercise 1.** A trader sells a 3-month ATM call ($S = K = 100$, $\tau = 0.25$) at implied vol $\hat{\sigma} = 0.22$ and delta-hedges. The realized volatility turns out to be $\sigma = 0.18$. Using the El Karoui-Jeanblanc-Shreve formula with constant $\Gamma \approx 0.03$ and $S \approx 100$, estimate the cumulative hedging P&L. Is this a profit or a loss for the option seller?

??? success "Solution to Exercise 1"
    The trader is short the call, so the P&L from delta-hedging is:

    $$
    \text{P\&L}_{\text{seller}} = -\frac{1}{2}\int_0^T \Gamma(t,S_t)(\sigma^2 - \hat{\sigma}^2)S_t^2\,dt
    $$

    The negative sign reflects the short option position (the seller receives the premium and hedges the liability). Using constant approximations $\Gamma \approx 0.03$, $S \approx 100$, $T = 0.25$:

    $$
    \sigma^2 - \hat{\sigma}^2 = (0.18)^2 - (0.22)^2 = 0.0324 - 0.0484 = -0.0160
    $$

    The buyer's (long gamma) hedging error is:

    $$
    \varepsilon = \frac{1}{2}(0.03)(10000)(-0.0160)(0.25) = 150 \times (-0.0160) \times 0.25 = -0.60
    $$

    For the seller (short gamma), the P&L is:

    $$
    \text{P\&L}_{\text{seller}} = -\varepsilon = +0.60
    $$

    The option seller profits approximately $\$0.60$. This is a profit because the realized volatility ($18\%$) was below the implied volatility ($22\%$) at which the call was sold. The seller collected more premium than was needed to cover the actual hedging cost.

---

**Exercise 2.** The hedging error is $\varepsilon = \frac{1}{2}\int_0^T \Gamma(t,S_t)(\sigma^2 - \hat{\sigma}^2)S_t^2\,dt$. Explain why the sign of $\varepsilon$ depends on whether the trader is long or short gamma. For a long put position (positive gamma), what happens to the hedging error if realized vol exceeds implied vol?

??? success "Solution to Exercise 2"
    The hedging error formula $\varepsilon = \frac{1}{2}\int_0^T \Gamma(t,S_t)(\sigma^2 - \hat{\sigma}^2)S_t^2\,dt$ has sign determined by the product $\Gamma \times (\sigma^2 - \hat{\sigma}^2)$.

    **Long gamma** ($\Gamma > 0$, e.g., long option):

    - If $\sigma > \hat{\sigma}$ (realized > implied): $\varepsilon > 0$, the hedger gains. The option was "cheap" and the excess realized volatility generates P&L through gamma.
    - If $\sigma < \hat{\sigma}$ (realized < implied): $\varepsilon < 0$, the hedger loses.

    **Short gamma** ($\Gamma < 0$, e.g., short option):

    - The signs reverse. The seller profits when realized vol is below implied vol.

    For a **long put position** (positive gamma), if realized vol exceeds implied vol:

    $$
    \varepsilon = \frac{1}{2}\int_0^T \underbrace{\Gamma}_{>0} \underbrace{(\sigma^2 - \hat{\sigma}^2)}_{>0} S_t^2\,dt > 0
    $$

    The hedging error is positive, meaning the long put holder gains. The put was underpriced relative to the volatility that actually materialized, and the gamma exposure converts the excess realized variance into profit.

---

**Exercise 3.** Even if the average realized variance equals the hedge variance ($\frac{1}{T}\int_0^T \sigma(t)^2\,dt = \hat{\sigma}^2$), the hedging error can be nonzero due to gamma weighting. Construct a simple example with two time periods where the average variance is correct but the hedging error is nonzero because higher volatility coincides with higher gamma.

??? success "Solution to Exercise 3"
    Consider a two-period example with $T = 2$, each period of length 1. An ATM option with strike $K = 100$ starts at $S_0 = 100$.

    **Period 1** ($t \in [0,1]$): $\sigma_1 = 0.30$, the option is ATM with high gamma, say $\Gamma_1 = 0.04$.

    **Period 2** ($t \in [1,2]$): $\sigma_2 = 0.10$, the stock has moved away from the strike, so $\Gamma_2 = 0.01$.

    The average variance is:

    $$
    \frac{1}{2}(\sigma_1^2 + \sigma_2^2) = \frac{1}{2}(0.09 + 0.01) = 0.05
    $$

    The hedge variance $\hat{\sigma}^2 = 0.05$, so the average variance matches.

    The hedging error is:

    $$
    \varepsilon = \frac{1}{2}\Gamma_1 S_1^2(\sigma_1^2 - \hat{\sigma}^2) \times 1 + \frac{1}{2}\Gamma_2 S_2^2(\sigma_2^2 - \hat{\sigma}^2) \times 1
    $$

    Using $S \approx 100$:

    $$
    \varepsilon \approx \frac{1}{2}(0.04)(10000)(0.09 - 0.05) + \frac{1}{2}(0.01)(10000)(0.01 - 0.05)
    $$

    $$
    = 200 \times 0.04 + 50 \times (-0.04) = 8.0 - 2.0 = 6.0
    $$

    Despite the average variance being correct, the hedging error is $+6.0$ because the **high volatility coincided with high gamma** (Period 1), which amplifies the positive contribution, while the low volatility occurred during the low-gamma period (Period 2), which has a smaller negative contribution. The gamma weighting breaks the averaging.

---

**Exercise 4.** The variance swap interpretation writes $\varepsilon = T(\sigma_R^2 - \hat{\sigma}^2)\overline{\Gamma_\$}$. If a trader wants to hedge the volatility misspecification risk of a short call position, explain how buying a variance swap with notional proportional to $\overline{\Gamma_\$}$ provides protection. What is the residual risk after this hedge?

??? success "Solution to Exercise 4"
    The variance swap pays $T(\sigma_R^2 - K_{\text{var}})$ at expiry, where $K_{\text{var}}$ is the strike and $\sigma_R^2$ is realized variance. The hedging error of a short call is:

    $$
    \varepsilon_{\text{seller}} = -\frac{1}{2}\int_0^T \Gamma S_t^2(\sigma^2(t) - \hat{\sigma}^2)\,dt = -T(\sigma_R^2 - \hat{\sigma}^2)\overline{\Gamma_\$}
    $$

    If the trader buys a variance swap with notional $\overline{\Gamma_\$}$ and strike $K_{\text{var}} = \hat{\sigma}^2$, the variance swap payoff is:

    $$
    \text{VS payoff} = T(\sigma_R^2 - \hat{\sigma}^2) \times \overline{\Gamma_\$}
    $$

    The combined position has P&L:

    $$
    \text{Total} = \varepsilon_{\text{seller}} + \text{VS payoff} = -T(\sigma_R^2 - \hat{\sigma}^2)\overline{\Gamma_\$} + T(\sigma_R^2 - \hat{\sigma}^2)\overline{\Gamma_\$} = 0
    $$

    The variance swap exactly offsets the average volatility misspecification risk.

    **Residual risk:** The hedge is imperfect because the formula $\varepsilon = T(\sigma_R^2 - \hat{\sigma}^2)\overline{\Gamma_\$}$ uses the gamma-weighted average $\overline{\Gamma_\$}$, which is itself path-dependent. The variance swap has a fixed notional, but $\overline{\Gamma_\$}$ varies with the realized path. The residual risk is the **covariance between gamma and realized variance** -- specifically, the risk that high realized variance coincides with high gamma (as in Exercise 3). This second-order "gamma-of-gamma" risk cannot be hedged with a single variance swap.

---

**Exercise 5.** For a small misspecification $\delta\sigma = \sigma - \hat{\sigma}$, the hedging error is approximately $2\hat{\sigma}\,\delta\sigma\int_0^T \Gamma_\$(t,S_t)\,dt$. Compute this for $\hat{\sigma} = 0.20$, $\delta\sigma = 0.03$, $\Gamma_\$ \approx 150$ (constant), $T = 0.5$. Compare the P&L with the option's vega times $\delta\sigma$.

??? success "Solution to Exercise 5"
    With $\hat{\sigma} = 0.20$, $\delta\sigma = 0.03$, $\Gamma_\$ = 150$ (constant), $T = 0.5$:

    $$
    \varepsilon \approx 2\hat{\sigma}\,\delta\sigma \int_0^T \Gamma_\$\,dt = 2(0.20)(0.03)(150)(0.5)
    $$

    $$
    = 2 \times 0.20 \times 0.03 \times 75 = 0.90
    $$

    Now compare with the vega-based estimate. The vega of an ATM option is approximately $\nu \approx S\sqrt{\tau}\,\phi(d_1)$. For $S = 100$, $T = 0.5$:

    $$
    \nu \approx 100 \times \sqrt{0.5} \times 0.399 \approx 28.2
    $$

    The vega-based P&L estimate is:

    $$
    \nu \times \delta\sigma = 28.2 \times 0.03 = 0.846
    $$

    The two estimates are close ($\$0.90$ vs $\$0.85$). The small discrepancy arises because the vega approximation is a first-order sensitivity at a single point in time, while the integral formula accounts for the cumulative effect over $[0, T]$. For small $\delta\sigma$, both approaches give consistent answers, validating the linearization.

---

**Exercise 6.** An uncertain volatility model assumes $\sigma \in [0.15, 0.30]$. For a European call with $S = K = 100$, $\tau = 1$, $r = 0.03$, compute the Black--Scholes price at both endpoints. What is the width of the price bounds? If the trader prices at the midpoint and hedges with midpoint delta, estimate the maximum hedging error using the El Karoui formula.

??? success "Solution to Exercise 6"
    For a European call with $S = K = 100$, $\tau = 1$, $r = 0.03$:

    **At $\sigma = 0.15$:**

    $$
    d_1 = \frac{(0.03 + 0.01125)(1)}{0.15} = \frac{0.04125}{0.15} = 0.275
    $$

    $$
    d_2 = 0.275 - 0.15 = 0.125
    $$

    $$
    C_{\text{low}} = 100\,N(0.275) - 100\,e^{-0.03}\,N(0.125) \approx 100(0.6083) - 97.04(0.5498) \approx 60.83 - 53.35 = 7.48
    $$

    **At $\sigma = 0.30$:**

    $$
    d_1 = \frac{(0.03 + 0.045)(1)}{0.30} = \frac{0.075}{0.30} = 0.25
    $$

    $$
    d_2 = 0.25 - 0.30 = -0.05
    $$

    $$
    C_{\text{high}} = 100\,N(0.25) - 97.04\,N(-0.05) \approx 100(0.5987) - 97.04(0.4801) \approx 59.87 - 46.60 = 13.27
    $$

    **Width of price bounds:**

    $$
    C_{\text{high}} - C_{\text{low}} = 13.27 - 7.48 = 5.79
    $$

    The uncertainty band is approximately $\$5.79$.

    **Midpoint pricing.** The midpoint price is $(7.48 + 13.27)/2 \approx 10.38$, corresponding to the midpoint volatility $\hat{\sigma}_{\text{mid}} = (0.15 + 0.30)/2 = 0.225$.

    **Maximum hedging error.** The worst case occurs at the volatility endpoints. Using the El Karoui formula with $\Gamma \approx 0.022$ (approximate ATM gamma at midpoint vol) and $S = 100$, $T = 1$:

    $$
    |\varepsilon_{\max}| = \frac{1}{2}\Gamma S^2 |\sigma^2 - \hat{\sigma}_{\text{mid}}^2| \times T
    $$

    The worst case is $\sigma = 0.30$:

    $$
    \sigma^2 - \hat{\sigma}_{\text{mid}}^2 = 0.09 - 0.050625 = 0.039375
    $$

    $$
    |\varepsilon_{\max}| \approx \frac{1}{2}(0.022)(10000)(0.039375)(1) = 110 \times 0.039375 \approx 4.33
    $$

    The maximum hedging error is approximately $\$4.33$, which is a substantial fraction of the option price, underscoring the importance of accurate volatility estimation.
