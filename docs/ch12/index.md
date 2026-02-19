# Chapter 12: Implied Volatility

This chapter develops the theory of implied volatility—the market's consensus volatility extracted from observed option prices—as both a practical quoting convention and a window into the risk-neutral distribution. Starting from the definition as the inverse of the Black-Scholes pricing map, we study the implied volatility surface's shape (smile and skew), its static and dynamic arbitrage constraints, the model-free results connecting it to the risk-neutral density and variance swaps, and the asymptotic behavior in extreme regimes of strike and maturity.

## Key Concepts

**Definition and Existence**
The implied volatility $\sigma_{\text{imp}}(K,T)$ is defined as the unique $\sigma > 0$ solving $C_{\text{BS}}(S_0, K, T, r, \sigma) = C_{\text{market}}(K,T)$. Existence and uniqueness follow from the strict monotonicity of the Black-Scholes call price in $\sigma$ (since vega $\nu = S\sqrt{T}\,N'(d_1) > 0$) combined with the boundary behavior $C_{\text{BS}} \to (S-Ke^{-rT})^+$ as $\sigma \to 0$ and $C_{\text{BS}} \to S$ as $\sigma \to \infty$. The intermediate value theorem then guarantees a unique root for any arbitrage-free market price $C_{\text{market}} \in ((S-Ke^{-rT})^+, S)$. Implied volatility serves as an **inverse pricing map**: it re-parameterizes option prices through the Black-Scholes formula, converting dollar prices into a unit-free quantity that facilitates comparison across strikes, maturities, and underlyings. Newton-Raphson iteration $\sigma^{(n+1)} = \sigma^{(n)} - (C_{\text{BS}}(\sigma^{(n)}) - C_{\text{mkt}})/\nu(\sigma^{(n)})$ converges rapidly due to the smoothness and strict positivity of vega.

**The Implied Volatility Surface**
Plotting $\sigma_{\text{imp}}(K,T)$ reveals systematic patterns that violate the Black-Scholes constant-volatility assumption:

- **Smile**: for equity index options, implied volatility forms a convex curve in strike, with higher values for deep OTM puts and calls than for ATM options. The smile is interpreted as the market pricing heavier tails than the log-normal distribution
- **Skew** (or smirk): equity index options exhibit a pronounced negative skew—OTM puts are more expensive (higher implied vol) than OTM calls—reflecting the leverage effect and crash risk premium. The 25-delta risk reversal $\sigma_{25\Delta P} - \sigma_{25\Delta C}$ quantifies the skew
- **Term structure**: the smile flattens at longer maturities as the central limit theorem smooths the return distribution, while short-maturity smiles are steep and peaked

**Static Arbitrage Constraints**
The implied volatility surface must satisfy no-arbitrage conditions that restrict its shape independently of any model:

- **Butterfly constraint**: $\partial^2 C/\partial K^2 \geq 0$ ensures the risk-neutral density is non-negative, equivalent to requiring the total variance $w(k,T) = \sigma_{\text{imp}}^2 T$ to be convex in log-moneyness $k = \ln(K/F)$
- **Calendar spread constraint**: $\partial C/\partial T \geq 0$ requires total variance to be non-decreasing in maturity for each strike
- **No-crossing constraint**: total variance slices at different maturities must not cross, preventing calendar spread arbitrage

**Model-Free Results**
Several powerful results connect implied volatility to the risk-neutral distribution without assuming any model:

- **Breeden-Litzenberger formula**: the risk-neutral density is $f(K) = e^{rT}\partial^2 C/\partial K^2$, extracting the full state-price density from the second derivative of the call price surface. In terms of implied volatility, this involves both $\sigma_{\text{imp}}$ and its strike derivatives
- **Dupire's formula**: the local volatility surface $\sigma_{\text{loc}}^2(K,T) = \frac{\partial_T C + rK\partial_K C + qC}{\frac{1}{2}K^2\partial_{KK}C}$ is determined entirely by the market call price surface, bridging implied and local volatility (Chapter 13)
- **Variance swaps**: the fair strike of a variance swap is $K_{\text{var}} = \frac{2}{T}\int_0^{\infty}\frac{C(K,T)}{K^2}\,dK$, a model-free integral over the call price surface. This connects to the **VIX formula** $\text{VIX}^2 = \frac{2}{T}\sum_i \frac{\Delta K_i}{K_i^2}Q(K_i)$, providing a model-independent measure of expected integrated variance

**Smile Dynamics**
The **forward smile** $\sigma_{\text{imp}}(K, T_2; t, S_t)$ describes how the smile evolves conditional on future spot levels. Two stylized regimes:

- **Sticky strike**: implied volatility at a given strike $K$ is constant as spot moves—the smile is anchored in strike space. This is consistent with local volatility models
- **Sticky delta**: implied volatility at a given delta (moneyness) is constant as spot moves—the smile moves rigidly with the spot. This is more consistent with stochastic volatility models

Empirical evidence shows that neither regime holds exactly; real smile dynamics lie between the two, with the sticky-strike/sticky-delta ratio depending on the dominant risk factor (spot vs. vol). **Dynamic consistency** requires that the forward smile implied by today's surface be consistent with the smile observed when that future date arrives—a stringent constraint that most parametric models violate.

**Implied Volatility Asymptotics**
Option prices and implied volatility exhibit characteristic behavior in extreme regimes:

- **Short maturity** ($T \to 0$): ATM implied volatility converges to the instantaneous local volatility $\sigma_{\text{imp}}(S_0, 0^+) = \sigma_{\text{loc}}(S_0, 0)$; the OTM smile steepens as $\sigma_{\text{imp}}^2 T \to (\ln(K/S_0))^2/(2I(K))$ where $I(K)$ is a rate function from large deviations theory
- **Wing asymptotics** ($|k| \to \infty$): Roger Lee's moment formula relates the implied volatility wing slopes to the existence of moments of $S_T$: $\limsup_{k \to \infty} \sigma_{\text{imp}}^2(k) T / k = 2 - 4(\sqrt{p^* + p^{*2}} - p^*)$ where $p^* = \sup\{p : \mathbb{E}[S_T^{1+p}] < \infty\}$, and an analogous formula for the left wing involving put moments
- **ATM expansions**: $\sigma_{\text{imp}}(K,T) = \sigma_0 + \sigma_1(K - S_0) + \sigma_2(K - S_0)^2 + \cdots$ where the coefficients $\sigma_i$ depend on the model parameters (skew, kurtosis of the risk-neutral distribution)

**Implied Volatility Sensitivities and Hedging**
Vega $\nu = \partial C/\partial\sigma_{\text{imp}}$ quantifies the option's sensitivity to parallel shifts in implied volatility. In the presence of a smile, hedging requires distinguishing between the **sticky-strike** Greeks (holding $K$ fixed and bumping $\sigma_{\text{imp}}(K)$) and the **sticky-delta** Greeks (holding moneyness fixed). The smile-adjusted delta $\Delta_{\text{smile}} = \Delta_{\text{BS}} + \nu \cdot \partial\sigma_{\text{imp}}/\partial S$ corrects the Black-Scholes delta for the smile's dependence on spot. This correction can be substantial for barrier and digital options near the barrier, where the smile slope $\partial\sigma_{\text{imp}}/\partial S$ amplifies the vega contribution.

!!! note "Role in the Book"
    Implied volatility provides the empirical bridge between the Black-Scholes formula (Chapter 6) and the richer models that explain the smile. Dupire's formula connects directly to local volatility (Chapter 13), the smile's shape constrains stochastic volatility model calibration (Chapter 14, Chapter 16), and the VIX/variance swap theory provides model-free benchmarks for calibration (Chapter 17). The wing asymptotics and moment formulas connect to the characteristic function methods of Chapter 9 and the affine theory of Chapter 15.

---
