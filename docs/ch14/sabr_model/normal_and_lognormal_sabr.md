# Normal SABR and Lognormal SABR

The two extreme values of the CEV exponent --- $\beta = 0$ (normal) and $\beta = 1$ (lognormal) --- produce qualitatively different models that correspond to distinct market conventions for quoting volatility. The choice between them has become particularly consequential since the emergence of negative interest rates in European and Japanese markets after 2014: the lognormal model is undefined for negative forwards, while the normal model handles them naturally. This section analyzes both limiting cases, derives their simplified Hagan formulas, establishes the conversion between Bachelier and Black implied volatilities, and introduces the shifted SABR extension.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Write down the SABR dynamics for $\beta = 0$ and $\beta = 1$ and describe their properties
    2. State the simplified Hagan formula for each case
    3. Convert between Bachelier (normal) and Black (lognormal) implied volatilities
    4. Explain when and why each convention is used in practice
    5. Define the shifted SABR model and explain its role in negative-rate environments

---

## Normal SABR (Beta = 0)

### Dynamics

Setting $\beta = 0$ in the SABR SDE system yields the **normal SABR model**:

$$
dF_t = \sigma_t\,dW_t^{(1)}
$$

$$
d\sigma_t = \nu\sigma_t\,dW_t^{(2)}
$$

$$
d\langle W^{(1)}, W^{(2)} \rangle_t = \rho\,dt
$$

The forward follows arithmetic Brownian motion with stochastic volatility. Because the diffusion coefficient $\sigma_t$ does not depend on $F_t$, the forward can take any real value --- including negative values. This is the fundamental reason normal SABR became the standard in EUR and JPY swaption markets after rates went negative.

### Properties

**No boundary at zero**: Unlike the general SABR with $\beta \in (0, 1)$, the normal model has no special behavior at $F = 0$. The forward passes through zero with positive probability, just as a standard Brownian motion crosses any level.

**Flat normal backbone**: The ATM normal (Bachelier) implied volatility is approximately:

$$
\sigma_N^{\text{ATM}} \approx \alpha\left[1 + \frac{2 - 3\rho^2}{24}\nu^2 T\right]
$$

This is independent of $F$ (to leading order), meaning the normal implied volatility does not change as the forward moves. The backbone is flat in normal vol space.

**ATM Black backbone**: Converting to Black implied volatility (when $F > 0$):

$$
\sigma_B^{\text{ATM}} \approx \frac{\alpha}{F}\left[1 + \left(\frac{\alpha^2}{24 F^2} + \frac{2 - 3\rho^2}{24}\nu^2\right)T\right]
$$

This has a steeply negative backbone: as $F$ decreases, the Black ATM vol increases as $1/F$.

### Hagan Formula for Beta = 0

The general Hagan formula simplifies considerably. The Black implied volatility is:

$$
\sigma_B(K) = \frac{\alpha}{(FK)^{1/2}\left[1 + \frac{1}{24}\ln^2\frac{F}{K} + \frac{1}{1920}\ln^4\frac{F}{K}\right]} \cdot \frac{z}{x(z)} \cdot \left[1 + \left(\frac{\alpha^2}{24(FK)} + \frac{2 - 3\rho^2}{24}\nu^2\right)T\right]
$$

where:

$$
z = \frac{\nu}{\alpha}(FK)^{1/2}\ln\frac{F}{K}, \qquad x(z) = \ln\!\left(\frac{\sqrt{1-2\rho z + z^2} + z - \rho}{1-\rho}\right)
$$

The normal implied volatility formula is even simpler:

$$
\sigma_N(K) = \alpha \cdot \frac{\hat{z}}{x(\hat{z})} \cdot \left[1 + \frac{2 - 3\rho^2}{24}\nu^2 T\right]
$$

where $\hat{z} = (\nu/\alpha)(F - K)$. Note the absence of the $(FK)^{(1-\beta)/2}$ factors when $\beta = 0$.

---

## Lognormal SABR (Beta = 1)

### Dynamics

Setting $\beta = 1$ yields the **lognormal SABR model**:

$$
dF_t = \sigma_t F_t\,dW_t^{(1)}
$$

$$
d\sigma_t = \nu\sigma_t\,dW_t^{(2)}
$$

$$
d\langle W^{(1)}, W^{(2)} \rangle_t = \rho\,dt
$$

The forward follows geometric Brownian motion with stochastic volatility. The percentage returns $dF_t/F_t = \sigma_t\,dW_t^{(1)}$ have stochastic but $F$-independent volatility.

### Properties

**Strict positivity**: Since $F_t$ follows a geometric Brownian motion (with stochastic vol), $F_t > 0$ for all $t$ almost surely. There is no boundary issue at zero.

**Flat Black backbone**: The ATM Black implied volatility is approximately:

$$
\sigma_B^{\text{ATM}} \approx \alpha\left[1 + \left(\frac{\rho\nu\alpha}{4} + \frac{2 - 3\rho^2}{24}\nu^2\right)T\right]
$$

This is independent of $F$ to leading order --- the backbone is flat in Black vol space.

**Normal backbone**: Converting to normal implied volatility:

$$
\sigma_N^{\text{ATM}} \approx \alpha F\left[1 + \left(\frac{\rho\nu\alpha}{4} + \frac{2 - 3\rho^2}{24}\nu^2\right)T\right]
$$

The normal vol has a positive backbone: it increases linearly with $F$.

### Hagan Formula for Beta = 1

With $\beta = 1$, the general formula simplifies because $(FK)^{(1-\beta)/2} = 1$ and the logarithmic correction terms in the denominator vanish:

$$
\sigma_B(K) = \alpha \cdot \frac{z}{x(z)} \cdot \left[1 + \left(\frac{\rho\nu\alpha}{4} + \frac{2 - 3\rho^2}{24}\nu^2\right)T\right]
$$

where:

$$
z = \frac{\nu}{\alpha}\ln\frac{F}{K}, \qquad x(z) = \ln\!\left(\frac{\sqrt{1-2\rho z + z^2} + z - \rho}{1-\rho}\right)
$$

This is the simplest form of the Hagan formula. The smile is entirely encoded in the $z/x(z)$ factor.

---

## Converting Between Black and Bachelier Implied Volatilities

### The Conversion Formula

Black (lognormal) and Bachelier (normal) implied volatilities parameterize the same option price using different models. For a call option with forward $F$, strike $K$, and maturity $T$:

**Black price:** $C = DF\left[F\,\Phi(d_1) - K\,\Phi(d_2)\right]$ where $d_{1,2} = \frac{\ln(F/K) \pm \frac{1}{2}\sigma_B^2 T}{\sigma_B\sqrt{T}}$

**Bachelier price:** $C = DF\left[(F-K)\,\Phi(\tilde{d}) + \sigma_N\sqrt{T}\,\phi(\tilde{d})\right]$ where $\tilde{d} = \frac{F-K}{\sigma_N\sqrt{T}}$

Since both must give the same price, the two implied volatilities are related. At the money ($K = F$), the exact relationship simplifies to:

$$
\sigma_N = \sigma_B \cdot F
$$

For general strikes, the approximate conversion is:

$$
\sigma_N \approx \sigma_B \cdot (FK)^{1/2} \cdot \frac{\ln(F/K)}{F/K - 1} \cdot \frac{1}{\left[1 + \frac{1}{24}\ln^2(F/K)\right]}
$$

!!! tip "Which Convention to Use"
    The choice of quoting convention depends on the asset class and market:

    | Market | Convention | Reason |
    |--------|-----------|--------|
    | USD swaptions (pre-2014) | Black vol | Rates always positive |
    | EUR swaptions (post-2014) | Normal vol or shifted Black | Negative rates |
    | JPY swaptions | Normal vol | Deeply negative rates |
    | Equity options | Black vol | Positive stock prices |
    | FX options | Black vol | Positive exchange rates |

### Implications for SABR Calibration

The choice of $\beta$ and the quoting convention are closely linked:

- $\beta = 0$ with normal vol: Calibrate $\alpha$ from normal ATM vol directly ($\alpha \approx \sigma_N^{\text{ATM}}$)
- $\beta = 1$ with Black vol: Calibrate $\alpha$ from Black ATM vol directly ($\alpha \approx \sigma_B^{\text{ATM}}$)
- Intermediate $\beta$: Convert between conventions as needed

---

## Shifted SABR

### Motivation

When the forward rate $F$ is negative (as occurred in EUR and CHF markets), the standard SABR model with $\beta > 0$ is undefined because $F^{\beta}$ is not real for $F < 0$. Two solutions exist: use $\beta = 0$ (normal SABR), or introduce a shift.

### Definition

The **shifted SABR model** replaces $F$ with $F + s$ where $s > 0$ is the shift parameter:

$$
d(F_t + s) = \sigma_t(F_t + s)^{\beta}\,dW_t^{(1)}
$$

$$
d\sigma_t = \nu\sigma_t\,dW_t^{(2)}
$$

Equivalently, defining $\tilde{F}_t = F_t + s$:

$$
d\tilde{F}_t = \sigma_t\tilde{F}_t^{\beta}\,dW_t^{(1)}
$$

The shifted forward $\tilde{F}_t$ must be positive, requiring $F_t > -s$ for all $t$. The shift $s$ is chosen large enough to ensure this holds (e.g., $s = 3\%$ when the most negative possible rate is $-3\%$).

### Shifted Hagan Formula

The Hagan formula applies unchanged to the shifted forward:

$$
\sigma_B^{\text{shifted}}(K) = \text{Hagan}(\tilde{F},\, K + s,\, \alpha,\, \beta,\, \rho,\, \nu,\, T)
$$

The resulting Black implied volatility is quoted against the shifted forward $\tilde{F} = F + s$ and shifted strike $\tilde{K} = K + s$. To convert back to an unshifted Black vol (when $F > 0$ and $K > 0$), the standard Black–to–shifted-Black conversion applies.

!!! warning "Shift Is Not a Model Parameter"
    The shift $s$ is a **convention**, not a model parameter. It is fixed by the market or by the desk and should not be calibrated. Changing $s$ changes the meaning of all other parameters ($\alpha$, $\rho$, $\nu$), making them non-comparable across different shifts. Within a single institution, the shift should be consistent across all expiries and tenors.

---

## Comparison of Normal and Lognormal SABR

| Feature | Normal SABR ($\beta=0$) | Lognormal SABR ($\beta=1$) |
|---------|--------------------------|----------------------------|
| Forward dynamics | Arithmetic BM | Geometric BM |
| Can handle $F < 0$ | Yes | No |
| Flat backbone in | Normal vol | Black vol |
| ATM normal vol | $\approx \alpha$ | $\approx \alpha F$ |
| ATM Black vol | $\approx \alpha/F$ | $\approx \alpha$ |
| Boundary at 0 | No boundary | Not attainable |
| Hagan formula | Simplest in normal vol | Simplest in Black vol |
| Primary market | EUR/JPY swaptions | Equity/FX options |

!!! example "Numerical Comparison"
    Consider $F = 2\%$, $T = 1$Y, $\rho = -0.3$, $\nu = 0.4$.

    **Normal SABR** ($\beta = 0$, $\alpha = 0.006$ = 60 bps normal vol):

    - ATM normal vol: 60.3 bps
    - ATM Black vol: $\approx 0.006/0.02 = 30.0\%$
    - 1% strike normal vol: 62.1 bps (slightly higher due to skew)

    **Lognormal SABR** ($\beta = 1$, $\alpha = 0.30$ = 30% Black vol):

    - ATM Black vol: 30.2%
    - ATM normal vol: $\approx 0.30 \times 0.02 = 60$ bps
    - 1% strike Black vol: 33.5% (higher due to skew)

    Both models produce similar option prices when calibrated to the same ATM level, but they differ in how the smile evolves as the forward moves (the backbone).

---

## Summary

Normal SABR ($\beta = 0$) and lognormal SABR ($\beta = 1$) represent the two fundamental limiting cases of the model. Normal SABR produces a flat backbone in Bachelier implied volatility and naturally handles negative rates, making it the standard for post-2014 EUR and JPY swaption markets. Lognormal SABR produces a flat backbone in Black implied volatility and ensures positive forwards, making it suitable for equity and FX markets. The conversion between Bachelier and Black implied volatilities is exact at ATM ($\sigma_N = \sigma_B F$) and approximate off the money. The shifted SABR model extends the $\beta > 0$ cases to negative-rate environments by applying a fixed displacement to the forward. The choice of $\beta$ is a modeling convention that should be consistent across the trading desk.

---

## Further Reading

- Hagan, P. et al. (2002). *Managing smile risk*. Wilmott Magazine, 1, 84--108.
- Antonov, A., Konikov, M., & Spector, M. (2015). *The free boundary SABR: Natural extension to negative rates*. SSRN preprint.
- Bartlett, B. (2006). *Hedging under SABR model*. Wilmott Magazine, July, 2--4.
- Kienitz, J. & Wetterau, D. (2012). *Financial Modelling: Theory, Implementation and Practice with MATLAB Source*. Wiley.

---

## Exercises

**Exercise 1.** For normal SABR ($\beta = 0$), the forward dynamics are $dF_t = \sigma_t\,dW_t^{(1)}$. Show that $F_T | \int_0^T \sigma_s^2\,ds = I$ is Gaussian with mean $F_0$ and variance $I$. Why does this imply that the normal SABR can handle negative forwards naturally?

??? success "Solution to Exercise 1"
    With $\beta = 0$, the forward dynamics are $dF_t = \sigma_t\,dW_t^{(1)}$. Conditional on the entire volatility path (equivalently, conditional on $W^{(2)}$), the forward is driven solely by $W^{(1)}$. The stochastic integral:

    $$
    F_T = F_0 + \int_0^T \sigma_s\,dW_s^{(1)}
    $$

    Conditional on $\{\sigma_s : 0 \leq s \leq T\}$, the integrand is a deterministic function of $s$ (since $\sigma_s$ depends only on $W^{(2)}$, which is independent of $W^{(1)}$ after the Cholesky decomposition removes the correlated part). Using the Cholesky decomposition $W^{(1)} = \rho W^{(2)} + \sqrt{1-\rho^2}B$, the integral becomes a sum of a $W^{(2)}$-measurable term and a Gaussian term from $B$.

    For the case $\rho = 0$ (or conditioning on the full $\sigma$ path), $\int_0^T \sigma_s\,dW_s^{(1)}$ conditional on $\sigma$ is Gaussian with mean zero and variance $I = \int_0^T \sigma_s^2\,ds$. Therefore:

    $$
    F_T \mid I \sim \mathcal{N}(F_0, I)
    $$

    Since the conditional distribution is Gaussian with mean $F_0$, the forward can take any real value including negative values. Specifically, the probability of $F_T < 0$ is:

    $$
    \mathbb{P}(F_T < 0 \mid I) = \Phi\!\left(\frac{-F_0}{\sqrt{I}}\right) > 0
    $$

    whenever $I > 0$. This is strictly positive for any non-degenerate volatility path, confirming that the normal SABR naturally accommodates negative forwards. There is no boundary issue at $F = 0$.

---

**Exercise 2.** The ATM Bachelier (normal) implied volatility for $\beta = 0$ SABR is $\sigma_N^{\text{ATM}} = \alpha[1 + \frac{2-3\rho^2}{24}\nu^2 T]$. The ATM Black (lognormal) implied volatility for $\beta = 1$ SABR is $\sigma_B^{\text{ATM}} = \alpha[1 + \frac{2-3\rho^2}{24}\nu^2 T]$. Despite the identical form, these are fundamentally different quantities. For $\alpha = 80$ bps, $\rho = -0.2$, $\nu = 0.45$, $T = 1$, $F = 3\%$, compute both $\sigma_N$ and $\sigma_B$. Convert from Bachelier to Black using $\sigma_B \approx \sigma_N / F$ at ATM and verify consistency.

??? success "Solution to Exercise 2"
    With $\alpha = 80$ bps $= 0.008$, $\rho = -0.2$, $\nu = 0.45$, $T = 1$, $F = 3\% = 0.03$:

    **Normal SABR** ($\beta = 0$): The ATM Bachelier vol is:

    $$
    \sigma_N^{\text{ATM}} = \alpha\left[1 + \frac{2-3\rho^2}{24}\nu^2 T\right] = 0.008\left[1 + \frac{2 - 3(0.04)}{24}(0.2025)\right]
    $$

    $$
    = 0.008\left[1 + \frac{1.88}{24}(0.2025)\right] = 0.008\left[1 + 0.01586\right] = 0.008 \times 1.01586 = 0.008127
    $$

    So $\sigma_N = 81.27$ bps.

    **Lognormal SABR** ($\beta = 1$): The correction has the same form but with an additional $\rho\nu\alpha/4$ term:

    $$
    \sigma_B^{\text{ATM}} = \alpha\left[1 + \left(\frac{\rho\nu\alpha}{4} + \frac{2-3\rho^2}{24}\nu^2\right)T\right]
    $$

    But here $\alpha = 0.008$ would be interpreted as a Black vol parameter, meaning $\alpha = 0.8\%$. This is an unrealistically low Black vol. For a fair comparison, we use $\alpha = 0.008$ as the normal vol parameter for $\beta = 0$ and convert.

    Converting the normal ATM vol to Black: $\sigma_B \approx \sigma_N / F = 0.008127 / 0.03 = 0.2709 = 27.09\%$.

    **Verification of consistency:** Under lognormal SABR with $\beta = 1$, setting $\alpha_{\text{LN}} = 0.2709$ should give the same option price. The ATM Black vol would be:

    $$
    \sigma_B^{\text{ATM}} \approx 0.2709\left[1 + \left(\frac{(-0.2)(0.45)(0.2709)}{4} + \frac{1.88}{24}(0.2025)\right)\right]
    $$

    $$
    = 0.2709\left[1 + (-0.00610 + 0.01586)\right] = 0.2709 \times 1.00976 = 0.2736 = 27.36\%
    $$

    Converting back: $\sigma_N = 0.2736 \times 0.03 = 82.1$ bps, close to the 81.3 bps from the normal SABR. The small discrepancy arises from the $O(T)$ correction terms differing between the two conventions. The conversion $\sigma_B \approx \sigma_N / F$ is exact only at leading order.

---

**Exercise 3.** The shifted SABR model uses dynamics $dF_t = \sigma_t(F_t + s)^\beta\,dW_t^{(1)}$. For a EUR swaption with forward rate $F = -0.2\%$ and shift $s = 3\%$, compute the shifted forward $\tilde{F} = F + s = 2.8\%$. Using $\beta = 0.5$, $\alpha = 0.012$, $\rho = 0.1$, $\nu = 0.4$, $T = 5$, compute the ATM implied volatility via the Hagan formula applied to $\tilde{F}$.

??? success "Solution to Exercise 3"
    With $F = -0.2\% = -0.002$, $s = 3\% = 0.03$, the shifted forward is:

    $$
    \tilde{F} = F + s = -0.002 + 0.030 = 0.028 = 2.8\%
    $$

    Using the Hagan ATM formula with $\beta = 0.5$, $\alpha = 0.012$, $\rho = 0.1$, $\nu = 0.4$, $T = 5$:

    **Leading term:**

    $$
    \frac{\alpha}{\tilde{F}^{1-\beta}} = \frac{0.012}{0.028^{0.5}} = \frac{0.012}{0.16733} = 0.07170 = 7.17\%
    $$

    **Correction terms:**

    $$
    c_1 = \frac{(0.5)^2(0.012)^2}{24(0.028)^1} = \frac{3.6 \times 10^{-5}}{0.672} = 5.357 \times 10^{-5}
    $$

    $$
    c_2 = \frac{(0.1)(0.5)(0.4)(0.012)}{4(0.028)^{0.5}} = \frac{2.4 \times 10^{-4}}{0.6693} = 3.585 \times 10^{-4}
    $$

    $$
    c_3 = \frac{2 - 3(0.01)}{24}(0.16) = \frac{1.97}{24}(0.16) = 1.313 \times 10^{-2}
    $$

    Total correction: $\varepsilon = 5.357 \times 10^{-5} + 3.585 \times 10^{-4} + 1.313 \times 10^{-2} = 1.354 \times 10^{-2}$.

    $$
    \sigma_B^{\text{ATM}} = 0.07170 \times (1 + 0.01354 \times 5) = 0.07170 \times 1.06770 = 0.07655 = 7.66\%
    $$

    This is the shifted Black implied volatility, quoted against the shifted forward $\tilde{F} = 2.8\%$.

---

**Exercise 4.** Explain why the choice between $\beta = 0$ and $\beta = 1$ affects the backbone dynamics. If the forward rate drops from 3% to 2%, by how much does the ATM Bachelier vol change under normal SABR ($\beta = 0$) versus lognormal SABR ($\beta = 1$)? Which model predicts a larger change in Black implied vol?

??? success "Solution to Exercise 4"
    Under **normal SABR** ($\beta = 0$), the ATM Bachelier vol is approximately $\sigma_N \approx \alpha$ (independent of $F$ to leading order). When $F$ drops from 3% to 2%, $\sigma_N$ remains essentially unchanged. Converting to Black vol: $\sigma_B \approx \sigma_N / F$, so at $F = 3\%$, $\sigma_B \approx \alpha / 0.03$, and at $F = 2\%$, $\sigma_B \approx \alpha / 0.02$. The Black vol increases by a factor of $3/2 = 1.5$, a 50% increase. The Bachelier vol barely changes.

    Under **lognormal SABR** ($\beta = 1$), the ATM Black vol is approximately $\sigma_B \approx \alpha$ (independent of $F$ to leading order). When $F$ drops from 3% to 2%, $\sigma_B$ remains essentially unchanged. Converting to normal vol: $\sigma_N \approx \sigma_B \times F$, so at $F = 3\%$, $\sigma_N \approx 0.03\alpha$, and at $F = 2\%$, $\sigma_N \approx 0.02\alpha$. The normal vol decreases by one-third.

    **Lognormal SABR predicts zero change in Black vol** for a forward move, while **normal SABR predicts a large change** in Black vol ($+50\%$ for a 1% drop from 3% to 2%). Normal SABR predicts the larger change in Black implied vol because the backbone $\sigma_B \approx \alpha / F$ is steep. This matches the empirical observation in interest rate markets that Black vol increases when rates fall --- the leverage effect seen in rates.

---

**Exercise 5.** In post-2014 EUR markets, forward swap rates went negative. Explain why $\beta = 1$ SABR fails in this environment (the term $F^\beta$ is undefined for $F < 0$ when $\beta = 1$). Compare three solutions: (a) switching to $\beta = 0$; (b) using shifted SABR with $\beta = 0.5$; (c) using free-boundary SABR. What are the trade-offs for each approach?

??? success "Solution to Exercise 5"
    When $F < 0$ and $\beta = 1$, the diffusion coefficient is $\sigma_t F_t$. Since $F_t < 0$, this means $F_t^{\beta} = F_t$ is negative, but the term $F_t^1$ in the SDE is simply $F_t$, which is well-defined. However, the standard SABR formula uses $F^{\beta}$ as a **positive** local volatility scaling, and the derivation assumes $F > 0$. The Hagan formula involves terms like $(FK)^{(1-\beta)/2}$ which for $\beta = 1$ reduce to 1 and are fine, but for fractional $\beta > 0$, the term $F^{\beta}$ is undefined for $F < 0$ (a fractional power of a negative number is not real-valued).

    **(a) Switching to $\beta = 0$:** The normal SABR dynamics $dF_t = \sigma_t\,dW_t^{(1)}$ have no $F$-dependence in the diffusion, so negative $F$ is handled naturally. **Trade-off**: The backbone becomes flat in normal vol (steep in Black vol), which may not match the dynamics of all markets. Also, the entire desk must switch quoting conventions.

    **(b) Shifted SABR with $\beta = 0.5$:** Replace $F$ with $F + s$ where $s$ is large enough that $F + s > 0$ always. The CEV dynamics $d(F+s) = \sigma_t(F+s)^{0.5}\,dW_t^{(1)}$ are well-defined as long as $F > -s$. **Trade-off**: Requires choosing $s$ (a convention, not a parameter), and all SABR parameters change when $s$ changes, making comparison across institutions difficult. The backbone shape is intermediate between normal and lognormal.

    **(c) Free-boundary SABR:** Solves the full 2D SABR PDE without restricting to $F > 0$, allowing the forward to pass through zero. **Trade-off**: Most complex to implement, no closed-form Hagan formula, requires numerical PDE or MC methods. However, it is the most theoretically consistent approach.

---

**Exercise 6.** A swaption trader quotes the 10Y-10Y swaption smile in Bachelier (basis point) volatility. The ATM normal vol is 65 bps, and the forward rate is 2.5%. Convert to Black (lognormal) implied volatility using the approximation $\sigma_B \approx \sigma_N / F$. For a 50 bp OTM put (strike = 2.0%), is the conversion formula still accurate? Explain why the conversion becomes less reliable for deep OTM options.

??? success "Solution to Exercise 6"
    At ATM ($K = F = 2.5\%$), the conversion is:

    $$
    \sigma_B = \frac{\sigma_N}{F} = \frac{0.0065}{0.025} = 0.26 = 26\%
    $$

    For the 50 bp OTM put at $K = 2.0\%$, the more general conversion formula is:

    $$
    \sigma_N \approx \sigma_B \cdot (FK)^{1/2} \cdot \frac{\ln(F/K)}{F/K - 1} \cdot \frac{1}{1 + \frac{1}{24}\ln^2(F/K)}
    $$

    Here $F/K = 1.25$, $\ln(F/K) = 0.2231$, $(FK)^{1/2} = (5 \times 10^{-4})^{1/2} = 0.02236$. The simple ATM conversion $\sigma_B = \sigma_N / F$ is no longer accurate because:

    1. The geometric mean $(FK)^{1/2} = 0.02236$ differs from $F = 0.025$
    2. The ratio $\ln(F/K)/(F/K - 1) = 0.2231/0.25 = 0.8924$ departs from 1
    3. The logarithmic correction factor contributes

    For deep OTM options, the relationship between $\sigma_N$ and $\sigma_B$ becomes highly nonlinear because the Bachelier and Black models distribute probability mass very differently in the tails. The Black model assigns probability through a lognormal distribution (right-skewed, bounded below by zero), while the Bachelier model assigns probability through a Gaussian distribution (symmetric, unbounded). For OTM puts (low strikes), these tails diverge, making the simple $\sigma_B \approx \sigma_N / F$ conversion increasingly inaccurate. The error can reach several percentage points for strikes more than 100 bps from ATM.
