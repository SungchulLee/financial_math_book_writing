# Impact of Volatility Misspecification


If the hedger uses \(\hat{\sigma}\) while true volatility is \(\sigma\), replication fails systematically. Understanding this failure mode is central to practical options trading and motivates implied-vs-realized volatility strategies.

---

## The fundamental hedging P&L identity


Consider a delta-hedged European option position. The hedger computes delta using an assumed volatility \(\hat{\sigma}\), but the underlying evolves with true (realized) volatility \(\sigma\). Over an infinitesimal interval, the delta-hedged P&L is

\[
dP\&L_{\text{hedged}} = \hat{\Theta}\,dt + \frac{1}{2}\hat{\Gamma}\,\sigma^2 S^2\,dt
\]

where \(\hat{\Theta}\) and \(\hat{\Gamma}\) are theta and gamma computed under \(\hat{\sigma}\). The Black–Scholes PDE under the hedge volatility gives

\[
\hat{\Theta} + \frac{1}{2}\hat{\sigma}^2 S^2 \hat{\Gamma} + rS\hat{\Delta} - r\hat{V} = 0
\]

Combining and integrating over \([0,T]\), the cumulative hedging error is

\[
\boxed{
\varepsilon = \frac{1}{2}\int_0^T \Gamma(t,S_t)\left(\sigma^2 - \hat{\sigma}^2\right)S_t^2\,\mathrm{d}t
}
\]

This is the **El Karoui–Jeanblanc–Shreve** (1998) result in its simplest form. Note that \(\Gamma\) here is evaluated along the true path \(S_t\), making \(\varepsilon\) path-dependent.

---

## Sign analysis


For a standard long option position where \(\Gamma > 0\) throughout:

| Scenario | Condition | Effect on hedging P&L |
|---|---|---|
| **Underestimate vol** | \(\hat{\sigma} < \sigma\) | \(\varepsilon > 0\): hedger gains (option was underpriced) |
| **Overestimate vol** | \(\hat{\sigma} > \sigma\) | \(\varepsilon < 0\): hedger loses (option was overpriced) |
| **Correct vol** | \(\hat{\sigma} = \sigma\) | \(\varepsilon = 0\): perfect replication |

From the perspective of the option **seller** who delta-hedges:

- Selling at implied vol \(\hat{\sigma}\) and hedging while realized vol is \(\sigma < \hat{\sigma}\) yields a profit.
- This is the basis of **short volatility** strategies: sell expensive implied vol and harvest the difference when realized vol is lower.

---

## Decomposition into dollar gamma


Define **dollar gamma** as

\[
\Gamma_\$ := \frac{1}{2}\Gamma S^2
\]

Then the hedging error becomes

\[
\varepsilon = \int_0^T \Gamma_\$(t,S_t)\left(\sigma^2 - \hat{\sigma}^2\right)\,\mathrm{d}t
\]

For small misspecification \(\sigma = \hat{\sigma} + \delta\sigma\):

\[
\sigma^2 - \hat{\sigma}^2 \approx 2\hat{\sigma}\,\delta\sigma
\]

so

\[
\varepsilon \approx 2\hat{\sigma}\,\delta\sigma \int_0^T \Gamma_\$(t,S_t)\,\mathrm{d}t
\]

This shows the hedging error scales linearly with volatility misspecification for small errors and is weighted by the path-integrated dollar gamma.

---

## Time-varying volatility


When the true volatility is stochastic or time-varying, \(\sigma = \sigma(t)\), the integral generalizes to

\[
\varepsilon = \frac{1}{2}\int_0^T \Gamma(t,S_t)\left(\sigma(t)^2 - \hat{\sigma}^2\right)S_t^2\,\mathrm{d}t
\]

Key consequences:

- **When** the volatility differs matters, not just the average difference. Misspecification during high-gamma periods (near strike, near expiry) has outsized impact.
- Even if \(\frac{1}{T}\int_0^T \sigma(t)^2\,dt = \hat{\sigma}^2\) (correct average variance), the hedging error need not vanish due to the \(\Gamma\)-weighting.

---

## Variance swap interpretation


The hedging error can be rewritten using the realized variance \(\sigma_R^2 = \frac{1}{T}\int_0^T \sigma(t)^2\,dt\):

\[
\varepsilon = T\left(\sigma_R^2 - \hat{\sigma}^2\right)\cdot \overline{\Gamma_\$}
\]

where \(\overline{\Gamma_\$}\) is the gamma-weighted average. This connects volatility misspecification hedging errors to **variance swap** payoffs and motivates the use of variance swaps as hedging instruments for volatility exposure.

---

## Implied volatility trading intuition


The hedging P&L identity provides the theoretical foundation for the core options trading heuristic:

- **Sell options** (collect premium) when you believe implied vol \(\hat{\sigma}\) exceeds expected future realized vol \(\sigma\).
- **Buy options** when you believe implied vol understates future realized vol.

The expected P&L from this trade is approximately

\[
\mathbb{E}[\text{P\&L}] \approx \bar{\Gamma}_\$ \cdot T \cdot \left(\sigma_{\text{implied}}^2 - \sigma_{\text{realized}}^2\right)
\]

This is sometimes called the **variance risk premium** when systematically exploited.

---

## Higher-order effects


The simple \(\Gamma(\sigma^2 - \hat{\sigma}^2)\) formula ignores several practical complications:

- **Path dependence of gamma**: \(\Gamma\) itself changes along the path, and the hedge ratios computed under \(\hat{\sigma}\) differ from those under \(\sigma\), introducing second-order errors.
- **Vega-gamma cross effects**: when volatility shifts discretely, both \(\Gamma\) and \(\Delta\) change simultaneously.
- **Discrete rebalancing**: in practice, rebalancing frequency interacts with volatility misspecification to amplify errors (see *Discrete-Time Hedging Error*).

A more precise expansion accounting for the mismatch in hedge ratios gives

\[
\varepsilon = \frac{1}{2}\int_0^T \hat{\Gamma}(t,S_t)\left(\sigma^2 - \hat{\sigma}^2\right)S_t^2\,dt + \text{higher-order path-dependent terms}
\]

where using \(\hat{\Gamma}\) (computed under the hedge model) versus \(\Gamma\) (true model) introduces corrections of order \((\sigma - \hat{\sigma})^2\).

---

## Robustness considerations


The sensitivity to volatility misspecification motivates several practical approaches:

- **Uncertain volatility models** (Avellaneda, Levy, Parás): assume \(\sigma \in [\sigma_{\min}, \sigma_{\max}]\) and solve for worst-case bounds.
- **Local volatility hedging**: use \(\sigma(t,S)\) fitted to the smile to reduce misspecification.
- **Vega hedging**: trade additional options to neutralize sensitivity to volatility changes, partially mitigating the impact of misspecification.
- **Frequent recalibration**: update \(\hat{\sigma}\) as new market data arrives.

---

## What to remember


- Gamma converts variance mismatch into systematic hedging P&L drift.
- The sign of the hedging error depends on whether realized vol exceeds or falls below the hedge vol, weighted by the gamma profile along the path.
- This motivates implied-vs-realized volatility trading intuition and the variance risk premium.
- When misspecification occurs matters as much as how much, due to gamma weighting.
- The framework connects naturally to variance swaps, uncertain volatility models, and robust hedging.
