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
