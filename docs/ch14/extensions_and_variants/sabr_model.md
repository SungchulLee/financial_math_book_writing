# SABR Model

The SABR model is a widely used **stochastic volatility model** designed to capture smile dynamics with a parsimonious parameterization. It is especially popular in interest-rate and FX markets due to its analytical implied volatility approximation, but its concepts generalize to equity volatility modeling.

---

## Model Definition

### Dynamics Under the Forward Measure

The SABR model specifies dynamics for a forward price $F_t$ (e.g., a forward rate or forward stock price):

$$
\begin{aligned}
dF_t &= \sigma_t F_t^{\beta}\,dW_t^F \\
d\sigma_t &= \nu\sigma_t\,dW_t^{\sigma} \\
d\langle W^F, W^{\sigma} \rangle_t &= \rho\,dt
\end{aligned}
$$

with initial conditions $F_0 = F$ and $\sigma_0 = \alpha$.

### Parameters

| Parameter | Symbol | Range | Interpretation |
|-----------|--------|-------|----------------|
| Initial forward | $F_0$ | $> 0$ | Current forward price |
| Initial volatility | $\alpha$ | $> 0$ | ATM volatility level |
| CEV exponent | $\beta$ | $[0, 1]$ | Backbone elasticity |
| Vol-of-vol | $\nu$ | $> 0$ | Volatility of volatility |
| Correlation | $\rho$ | $[-1, 1]$ | Forward-vol correlation |

### Key Features

1. **Driftless forward:** Under the $T$-forward measure, $F_t$ is a martingale
2. **Lognormal volatility:** $\sigma_t$ follows geometric Brownian motion
3. **CEV backbone:** $\beta$ interpolates between normal ($\beta = 0$) and lognormal ($\beta = 1$)
4. **No mean reversion:** Volatility can drift without bound

---

## Interpretation of Parameters

### The CEV Exponent (β)

The parameter $\beta$ controls the **backbone** of the smile—how ATM volatility changes with the forward level:

| $\beta$ | Behavior | ATM vol vs. $F$ |
|---------|----------|-----------------|
| 0 | Normal | Independent |
| 0.5 | Square-root | $\propto 1/\sqrt{F}$ |
| 1 | Lognormal | $\propto 1/F$ |

**In practice:** $\beta$ is often fixed based on market convention:

- Interest rates: $\beta = 0$ (normal) or $\beta = 0.5$
- FX: $\beta = 1$ (lognormal)
- Equity: $\beta = 1$ typically

### Volatility of Volatility (ν)

The parameter $\nu$ controls **smile curvature**:

- Higher $\nu$ → more convex smile
- $\nu = 0$ → no smile (CEV model only)

### Correlation (ρ)

The parameter $\rho$ controls **smile skew**:

- $\rho < 0$ → negative skew (equity-like)
- $\rho > 0$ → positive skew
- $\rho = 0$ → symmetric smile

**Typical equity values:** $\rho \in [-0.5, -0.9]$

### Initial Volatility (α)

The parameter $\alpha$ sets the **ATM implied volatility level**:

- Directly calibrated to ATM market quote
- For $\beta = 1$: $\alpha \approx \sigma_{\text{ATM}}$
- For $\beta \neq 1$: relationship is more complex

---

## Hagan's Implied Volatility Formula

### The Asymptotic Approximation

Hagan, Kumar, Lesniewski, and Woodward (2002) derived an **asymptotic formula** for implied volatility:

$$
\sigma_{\text{impl}}(K, F) = \sigma_B(K, F) \cdot \left[1 + \left(\frac{(1-\beta)^2}{24}\frac{\alpha^2}{(FK)^{1-\beta}} + \frac{\rho\beta\nu\alpha}{4(FK)^{(1-\beta)/2}} + \frac{2-3\rho^2}{24}\nu^2\right)T + O(T^2)\right]
$$

where the **base volatility** $\sigma_B$ is:

$$
\sigma_B(K, F) = \frac{\alpha}{(FK)^{(1-\beta)/2}\left[1 + \frac{(1-\beta)^2}{24}\log^2(F/K) + \frac{(1-\beta)^4}{1920}\log^4(F/K)\right]} \cdot \frac{z}{x(z)}
$$

with:

$$
z = \frac{\nu}{\alpha}(FK)^{(1-\beta)/2}\log(F/K)
$$

$$
x(z) = \log\left(\frac{\sqrt{1-2\rho z + z^2} + z - \rho}{1-\rho}\right)
$$

### ATM Formula (K = F)

At the money, the formula simplifies significantly:

$$
\sigma_{\text{ATM}} = \frac{\alpha}{F^{1-\beta}}\left[1 + \left(\frac{(1-\beta)^2}{24}\frac{\alpha^2}{F^{2(1-\beta)}} + \frac{\rho\beta\nu\alpha}{4F^{1-\beta}} + \frac{2-3\rho^2}{24}\nu^2\right)T\right]
$$

**For $\beta = 1$ (lognormal):**

$$
\sigma_{\text{ATM}} = \alpha\left[1 + \frac{2-3\rho^2}{24}\nu^2 T\right]
$$

### Skew and Curvature

Taking derivatives of the Hagan formula:

**Skew (first derivative):**

$$
\frac{\partial \sigma_{\text{impl}}}{\partial k}\bigg|_{k=0} \approx \frac{\rho\nu}{2\sigma_{\text{ATM}}} - \frac{(1-\beta)}{2F}
$$

where $k = \log(K/F)$.

**Curvature (second derivative):**

$$
\frac{\partial^2 \sigma_{\text{impl}}}{\partial k^2}\bigg|_{k=0} \approx \frac{\nu^2(1-\rho^2)}{2\sigma_{\text{ATM}}} + \text{(corrections)}
$$

---

## Calibration

### Standard Approach

**Step 1:** Fix $\beta$ (often to market convention)

**Step 2:** Set $\alpha$ from ATM implied volatility (approximately)

**Step 3:** Fit $\rho$ and $\nu$ to OTM options using least squares:

$$
\min_{\rho, \nu} \sum_i \left(\sigma_{\text{impl}}^{\text{market}}(K_i) - \sigma_{\text{impl}}^{\text{SABR}}(K_i; \alpha, \beta, \rho, \nu)\right)^2
$$

### Typical Calibrated Values

| Market | $\beta$ | $\rho$ | $\nu$ |
|--------|---------|--------|-------|
| USD rates | 0–0.5 | $-0.3$ to $0.3$ | 0.3–0.8 |
| EUR rates | 0–0.5 | $-0.2$ to $0.2$ | 0.3–0.7 |
| FX | 1 | $-0.3$ to $-0.1$ | 0.2–0.5 |
| Equity | 1 | $-0.7$ to $-0.4$ | 0.3–0.6 |

### Dealing with β

**Fixing $\beta$:** Reduces degrees of freedom; improves stability

**Fitting $\beta$:** More flexible but may overfit; creates identifiability issues with $\alpha$

**Rule of thumb:** Fix $\beta$ and recalibrate $(\alpha, \rho, \nu)$ daily

---

## Properties and Limitations

### Strengths

1. **Parsimonious:** Only 4 parameters (3 if $\beta$ fixed)
2. **Closed-form smile:** Hagan formula is fast to evaluate
3. **Intuitive parameters:** Direct control over skew and curvature
4. **Industry standard:** Widely used for rates and FX

### Limitations

1. **Approximation accuracy:** Hagan formula breaks down for:
   - Long maturities ($T > 5$ years)
   - Deep OTM options
   - Low rates / negative rates
   
2. **No mean reversion:** Volatility can drift to zero or infinity

3. **Absorbing boundary:** $F = 0$ is absorbing when $\beta < 1$

4. **No arbitrage concerns:** Hagan formula can produce negative densities for extreme parameters

5. **Dynamic inconsistency:** Forward smile dynamics may not match market behavior

### Arbitrage-Free Corrections

**Obloj (2008):** Modified formula with improved wing behavior

**Antonov et al. (2015):** Free boundary SABR for negative rates

**Hagan & Lesniewski (2017):** Improved arbitrage-free formula

---

## SABR for Negative Rates

### The Problem

When rates can go negative ($F < 0$ possible), the standard SABR model fails:

- $F^{\beta}$ undefined for $F < 0$ and $0 < \beta < 1$
- Lognormal ($\beta = 1$) excludes negative rates

### Shifted SABR

Introduce a shift $s$:

$$
dF_t = \sigma_t (F_t + s)^{\beta}\,dW_t^F
$$

The shifted forward $\tilde{F} = F + s$ remains positive if $s$ is large enough.

**Calibration:** Choose $s$ such that $F_{\min} + s > 0$.

### Normal SABR (β = 0)

Setting $\beta = 0$:

$$
dF_t = \sigma_t\,dW_t^F
$$

Allows negative rates naturally (Bachelier-type model).

**Hagan formula for $\beta = 0$:**

$$
\sigma_{\text{impl}}^N(K, F) = \alpha\left[1 + \frac{2-3\rho^2}{24}\nu^2 T\right] \cdot \frac{z}{x(z)}
$$

where $z = \frac{\nu}{\alpha}(F - K)$ and $x(z)$ as before.

---

## Comparison with Heston

| Feature | SABR | Heston |
|---------|------|--------|
| Volatility dynamics | GBM | CIR (mean-reverting) |
| Mean reversion | No | Yes |
| Closed-form CF | No | Yes |
| Implied vol formula | Yes (approximate) | No |
| Calibration speed | Fast | Moderate |
| Long-dated accuracy | Poor | Good |
| Negative rates | Via shift | Naturally excluded |
| Industry use | Rates, FX | Equity |

---

## Implementation Notes

### Numerical Stability

**Issue:** $x(z)$ has numerical issues when $z \to 0$ or $\rho \to \pm 1$

**Solution:** Use series expansion for small $z$:

$$
x(z) \approx z\left(1 + \frac{\rho z}{2} + \frac{(2\rho^2 - 1)z^2}{6} + \cdots\right)
$$

### Python Implementation

```python
import numpy as np

def sabr_implied_vol(F, K, T, alpha, beta, rho, nu):
    """
    Hagan SABR implied volatility formula
    """
    if np.abs(F - K) < 1e-10:
        # ATM case
        FK_mid = F
        vol = alpha / FK_mid**(1-beta) * (
            1 + ((1-beta)**2/24 * alpha**2 / FK_mid**(2-2*beta) +
                 rho*beta*nu*alpha / (4*FK_mid**(1-beta)) +
                 (2-3*rho**2)/24 * nu**2) * T
        )
        return vol
    
    # General case
    FK = F * K
    log_FK = np.log(F / K)
    FK_mid = np.sqrt(FK)
    
    z = nu / alpha * FK_mid**(1-beta) * log_FK
    
    # x(z) with numerical care
    if np.abs(z) < 1e-10:
        x_z = 1
    else:
        sqrt_term = np.sqrt(1 - 2*rho*z + z**2)
        x_z = np.log((sqrt_term + z - rho) / (1 - rho)) / z
    
    # Base volatility
    denom = FK_mid**(1-beta) * (
        1 + (1-beta)**2/24 * log_FK**2 +
        (1-beta)**4/1920 * log_FK**4
    )
    sigma_B = alpha / denom * x_z
    
    # Correction terms
    correction = 1 + (
        (1-beta)**2/24 * alpha**2 / FK**(1-beta) +
        rho*beta*nu*alpha / (4 * FK_mid**(1-beta)) +
        (2-3*rho**2)/24 * nu**2
    ) * T
    
    return sigma_B * correction
```

---

## Key Takeaways

- SABR is a practical smile model with closed-form implied volatility
- The Hagan formula provides fast calibration but is approximate
- Parameters: $\alpha$ (level), $\beta$ (backbone), $\rho$ (skew), $\nu$ (curvature)
- Best suited for short/medium maturities near ATM
- For negative rates, use shifted SABR or $\beta = 0$
- No mean reversion limits dynamic consistency

---

## Further Reading

- Hagan, P., Kumar, D., Lesniewski, A., & Woodward, D. (2002). *Managing smile risk*. Wilmott Magazine.
- Obloj, J. (2008). *Fine-tune your smile: Correction to Hagan et al*. Working paper.
- Antonov, A., Konikov, M., & Spector, M. (2015). *SABR spreads its wings*. Risk Magazine.
- Rebonato, R. (2004). *Volatility and Correlation*, 2nd ed. Wiley.
- West, G. (2005). *Calibration of the SABR model in illiquid markets*. Applied Mathematical Finance.

---

## Exercises

**Exercise 1.** Using the ATM Hagan formula for $\beta = 1$:

$$
\sigma_{\text{ATM}} = \alpha\left[1 + \frac{2-3\rho^2}{24}\nu^2 T\right]
$$

compute $\sigma_{\text{ATM}}$ for $\alpha = 0.20$, $\rho = -0.6$, $\nu = 0.4$, $T = 0.5$. Then solve inversely: given a market ATM implied vol of $22\%$ with the same $\rho$, $\nu$, and $T$, recover $\alpha$.

??? success "Solution to Exercise 1"
    We use the ATM formula for $\beta = 1$:

    $$
    \sigma_{\text{ATM}} = \alpha\left[1 + \frac{2 - 3\rho^2}{24}\nu^2 T\right]
    $$

    **Forward computation.** Substituting $\alpha = 0.20$, $\rho = -0.6$, $\nu = 0.4$, and $T = 0.5$:

    $$
    \frac{2 - 3\rho^2}{24} = \frac{2 - 3(0.36)}{24} = \frac{2 - 1.08}{24} = \frac{0.92}{24} \approx 0.03833
    $$

    $$
    \sigma_{\text{ATM}} = 0.20\left[1 + 0.03833 \times 0.16 \times 0.5\right] = 0.20\left[1 + 0.003067\right] \approx 0.20061
    $$

    So $\sigma_{\text{ATM}} \approx 20.06\%$.

    **Inverse computation.** Given $\sigma_{\text{ATM}} = 0.22$, solve for $\alpha$:

    $$
    0.22 = \alpha\left[1 + 0.03833 \times 0.16 \times 0.5\right] = \alpha \times 1.003067
    $$

    $$
    \alpha = \frac{0.22}{1.003067} \approx 0.21933
    $$

    The correction factor is close to 1, so $\alpha$ is close to $\sigma_{\text{ATM}}$, but not identical.

---

**Exercise 2.** The SABR skew formula at ATM is approximately

$$
\frac{\partial\sigma_{\text{impl}}}{\partial k}\bigg|_{k=0} \approx \frac{\rho\nu}{2\sigma_{\text{ATM}}} - \frac{(1-\beta)}{2F}
$$

For $F = 100$, $\beta = 1$, $\rho = -0.65$, $\nu = 0.45$, and $\sigma_{\text{ATM}} = 0.20$, compute the ATM skew. Then repeat with $\beta = 0.5$ and explain how the CEV exponent contributes additional skew even when $\rho = 0$.

??? success "Solution to Exercise 2"
    **ATM skew formula:**

    $$
    \frac{\partial\sigma_{\text{impl}}}{\partial k}\bigg|_{k=0} \approx \frac{\rho\nu}{2\sigma_{\text{ATM}}} - \frac{(1-\beta)}{2F}
    $$

    **Case $\beta = 1$.** With $F = 100$, $\rho = -0.65$, $\nu = 0.45$, $\sigma_{\text{ATM}} = 0.20$:

    $$
    \text{Skew} = \frac{(-0.65)(0.45)}{2(0.20)} - \frac{1-1}{2(100)} = \frac{-0.2925}{0.40} = -0.73125
    $$

    The skew is approximately $-0.731$ per unit log-strike.

    **Case $\beta = 0.5$.** Now the second term contributes:

    $$
    \text{Skew} = \frac{(-0.65)(0.45)}{2(0.20)} - \frac{1 - 0.5}{2(100)} = -0.73125 - 0.0025 = -0.73375
    $$

    **CEV contribution when $\rho = 0$.** Setting $\rho = 0$ with $\beta = 0.5$:

    $$
    \text{Skew} = 0 - \frac{0.5}{200} = -0.0025
    $$

    Even with zero correlation, the CEV exponent $\beta < 1$ generates negative skew. This is because when $F$ decreases, the local volatility $F^\beta$ decreases more slowly than $F$ itself, so the effective lognormal volatility increases. This leverage-like effect is purely geometric and does not require any correlation between the forward and its volatility.

---

**Exercise 3.** Compare the SABR and Heston models by filling in the following table with qualitative assessments:

| Feature | SABR advantage | Heston advantage |
|---------|---------------|-----------------|
| Short-maturity smile | ? | ? |
| Long-maturity term structure | ? | ? |
| Calibration speed | ? | ? |
| Dynamic consistency | ? | ? |
| Negative rates handling | ? | ? |

Justify each entry with a brief explanation.

??? success "Solution to Exercise 3"
    | Feature | SABR advantage | Heston advantage |
    |---------|---------------|-----------------|
    | Short-maturity smile | SABR excels | — |
    | Long-maturity term structure | — | Heston excels |
    | Calibration speed | SABR excels | — |
    | Dynamic consistency | — | Heston excels |
    | Negative rates handling | SABR excels | — |

    **Short-maturity smile.** SABR has a closed-form implied volatility approximation specifically designed for short maturities. The Hagan formula is most accurate for small $T$, while Heston relies on characteristic function inversion that can be less intuitive to tune for very short maturities.

    **Long-maturity term structure.** Heston's mean-reverting CIR volatility process ensures the variance stays bounded and converges to its long-run mean. SABR's GBM volatility can drift without bound, making the Hagan approximation unreliable for $T > 5$ years and producing unrealistic long-dated behavior.

    **Calibration speed.** The Hagan formula evaluates in microseconds, making SABR calibration essentially instantaneous. Heston requires numerical characteristic function inversion (Fourier integrals) for each option price, which is slower by orders of magnitude.

    **Dynamic consistency.** Heston is a fully specified diffusion model, so calibrated parameters today produce consistent dynamics for hedging over time. SABR is typically recalibrated daily, and the model does not guarantee that the forward smile dynamics match market realities, leading to potential hedging errors.

    **Negative rates handling.** SABR with $\beta = 0$ (normal backbone) or the shifted SABR extension handles negative rates naturally. Heston's CIR process ensures variance stays positive, but the lognormal asset dynamics exclude negative forward prices by construction.

---

**Exercise 4.** In the shifted SABR model, the forward dynamics are $dF_t = \sigma_t(F_t + s)^\beta\,dW_t^F$. For a market where the forward rate is $F = -0.3\%$ and the shift is $s = 3\%$, compute the shifted forward $\tilde{F} = F + s$. Using $\beta = 0.5$, $\alpha = 0.005$, $\nu = 0.4$, $\rho = 0.1$, compute the ATM implied volatility using the Hagan formula applied to $\tilde{F}$. Convert from lognormal to normal (Bachelier) volatility using $\sigma_N \approx \sigma_{\text{LN}} \cdot \tilde{F}$.

??? success "Solution to Exercise 4"
    **Shifted forward.** With $F = -0.3\% = -0.003$ and $s = 3\% = 0.03$:

    $$
    \tilde{F} = F + s = -0.003 + 0.03 = 0.027
    $$

    **ATM implied volatility.** Using the Hagan ATM formula applied to $\tilde{F}$ with $\beta = 0.5$, $\alpha = 0.005$, $\nu = 0.4$, $\rho = 0.1$, and $T = 1$:

    $$
    \sigma_{\text{ATM}} = \frac{\alpha}{\tilde{F}^{1-\beta}}\left[1 + \left(\frac{(1-\beta)^2}{24}\frac{\alpha^2}{\tilde{F}^{2(1-\beta)}} + \frac{\rho\beta\nu\alpha}{4\tilde{F}^{1-\beta}} + \frac{2-3\rho^2}{24}\nu^2\right)T\right]
    $$

    Computing the leading term with $\tilde{F}^{1-\beta} = 0.027^{0.5} = 0.16432$:

    $$
    \frac{\alpha}{\tilde{F}^{0.5}} = \frac{0.005}{0.16432} \approx 0.03043
    $$

    The correction terms:

    $$
    \frac{(0.5)^2}{24}\frac{(0.005)^2}{0.027} = \frac{0.25}{24}\times\frac{0.000025}{0.027} \approx 0.00000965
    $$

    $$
    \frac{(0.1)(0.5)(0.4)(0.005)}{4 \times 0.16432} \approx \frac{0.0001}{0.65728} \approx 0.0001522
    $$

    $$
    \frac{2 - 3(0.01)}{24}(0.16) = \frac{1.97}{24}\times 0.16 \approx 0.01313
    $$

    So the bracket is approximately $1 + 0.01330 \approx 1.01330$:

    $$
    \sigma_{\text{ATM}} \approx 0.03043 \times 1.01330 \approx 0.03083 = 3.08\%
    $$

    **Conversion to normal volatility:**

    $$
    \sigma_N \approx \sigma_{\text{LN}} \cdot \tilde{F} = 0.03083 \times 0.027 \approx 0.000832 = 8.32 \text{ bps}
    $$

---

**Exercise 5.** Explain why the Hagan formula can produce negative probability densities for extreme parameters. Specifically, the implied density is $f(K) = e^{rT}\partial^2 C/\partial K^2$. If $\sigma_{\text{impl}}(K)$ is not a valid smile (e.g., it becomes negative at extreme strikes), $f(K) < 0$. For $\alpha = 0.30$, $\beta = 1$, $\rho = -0.9$, $\nu = 1.0$, $F = 100$, $T = 5$, explain which combination of parameter extremes is most likely to trigger this issue.

??? success "Solution to Exercise 5"
    The implied density is obtained via the Breeden-Litzenberger formula:

    $$
    f(K) = e^{rT}\frac{\partial^2 C}{\partial K^2}
    $$

    If we express call prices through the Black-Scholes formula with the SABR implied volatility $\sigma_{\text{impl}}(K)$, the density involves second derivatives of both the smile and the Black-Scholes vega/gamma terms.

    **Why negative densities arise.** The Hagan formula is an asymptotic expansion that is accurate near ATM and for small $T$. At extreme strikes, the approximation can produce:

    - Implied volatilities that decrease too steeply in the wings, or
    - Implied volatilities that become negative (unphysical).

    Either scenario leads to $\partial^2 C / \partial K^2 < 0$, violating the no-arbitrage requirement that the density be non-negative.

    **For the given parameters** ($\alpha = 0.30$, $\beta = 1$, $\rho = -0.9$, $\nu = 1.0$, $F = 100$, $T = 5$), the combination is extreme in multiple ways:

    - $|\rho| = 0.9$ near the boundary creates very steep skew,
    - $\nu = 1.0$ is a very high vol-of-vol, amplifying smile curvature,
    - $T = 5$ is long-dated, where the $O(T^2)$ remainder in the Hagan expansion becomes large.

    The most dangerous combination is **high $\nu$ with $|\rho|$ near 1 and large $T$**. The high $\nu$ makes the smile very curved, the extreme $\rho$ makes it very skewed, and the large $T$ pushes the asymptotic expansion well outside its range of validity. Together, these cause the Hagan approximation to overshoot in the put wing (low strikes), producing implied volatilities that are too low or even negative, and hence negative densities. The correction terms proportional to $\nu^2 T$ and $\rho\nu T$ dominate the base term, invalidating the perturbation expansion.

---

**Exercise 6.** A rates trader fixes $\beta = 0$ (normal SABR) and calibrates $(\alpha, \rho, \nu)$ to a 1-year swaption smile. She obtains $\alpha = 80$ bps, $\rho = 0.15$, $\nu = 0.50$. The next day, the forward rate moves from 3.5% to 3.0% but the smile shape remains similar. Will she need to recalibrate $\alpha$, or does the normal SABR model automatically adjust? Compare with $\beta = 1$ (lognormal SABR) where $\sigma_{\text{ATM}} \propto 1/F$.

??? success "Solution to Exercise 6"
    **Normal SABR ($\beta = 0$).** The ATM normal implied volatility is approximately:

    $$
    \sigma_{\text{ATM}}^N \approx \alpha\left[1 + \frac{2 - 3\rho^2}{24}\nu^2 T\right]
    $$

    This does not depend on $F$. When the forward rate moves from 3.5% to 3.0%, the normal ATM volatility remains approximately 80 bps (since $\alpha = 80$ bps and the correction is $F$-independent). The trader does not need to recalibrate $\alpha$ for a parallel shift in the forward rate; the model automatically accommodates level changes.

    **Lognormal SABR ($\beta = 1$).** The ATM lognormal implied volatility is:

    $$
    \sigma_{\text{ATM}}^{\text{LN}} \approx \frac{\alpha}{F^{1-\beta}} = \alpha
    $$

    for $\beta = 1$, but the corresponding normal volatility is $\sigma_N \approx \sigma_{\text{LN}} \cdot F$. So when $F$ drops from 3.5% to 3.0%, the normal volatility drops proportionally:

    $$
    \sigma_N^{\text{new}} \approx \alpha \times 0.030 = 0.030\alpha
    $$

    versus $\sigma_N^{\text{old}} \approx 0.035\alpha$. This is a $14.3\%$ decline in normal volatility, which may not match the market observation that the smile shape remains similar.

    **Conclusion.** For interest rate markets where normal volatility is approximately stable across rate levels, $\beta = 0$ is the more appropriate choice. It provides a natural "sticky normal vol" behavior, whereas $\beta = 1$ implies "sticky lognormal vol" which translates to changing normal vol as rates move.

---

**Exercise 7.** The SABR model has no mean reversion in the volatility process ($d\sigma_t = \nu\sigma_t\,dW_t^\sigma$). Explain why this causes problems for long-dated options. Specifically, compute the expected value and variance of $\sigma_T$ under this GBM dynamics for $\sigma_0 = 0.2$, $\nu = 0.4$, $T = 10$. What is the probability that $\sigma_T > 1$ (100% vol)? Is this economically realistic?

??? success "Solution to Exercise 7"
    The volatility follows GBM: $d\sigma_t = \nu\sigma_t\,dW_t^\sigma$. By Ito's lemma:

    $$
    \sigma_T = \sigma_0\exp\!\left(-\frac{\nu^2}{2}T + \nu W_T\right)
    $$

    **Expected value.** Since $\sigma_T$ is a geometric Brownian motion (driftless, as the $dt$ coefficient is zero):

    $$
    \mathbb{E}[\sigma_T] = \sigma_0 = 0.2
    $$

    **Variance.** Using $\mathbb{E}[\sigma_T^2] = \sigma_0^2 e^{\nu^2 T}$:

    $$
    \text{Var}(\sigma_T) = \sigma_0^2\!\left(e^{\nu^2 T} - 1\right) = 0.04\!\left(e^{0.16 \times 10} - 1\right) = 0.04\!\left(e^{1.6} - 1\right)
    $$

    $$
    e^{1.6} \approx 4.953
    $$

    $$
    \text{Var}(\sigma_T) \approx 0.04 \times 3.953 = 0.15812
    $$

    The standard deviation is $\sqrt{0.15812} \approx 0.3976$, which is about twice the mean.

    **Probability that $\sigma_T > 1$.** We need:

    $$
    \mathbb{P}(\sigma_T > 1) = \mathbb{P}\!\left(\sigma_0 e^{-\nu^2 T/2 + \nu W_T} > 1\right)
    $$

    $$
    = \mathbb{P}\!\left(W_T > \frac{\ln(1/\sigma_0) + \nu^2 T/2}{\nu}\right)
    $$

    $$
    = \mathbb{P}\!\left(W_T > \frac{\ln 5 + 0.8}{0.4}\right) = \mathbb{P}\!\left(W_T > \frac{1.6094 + 0.8}{0.4}\right)
    $$

    $$
    = \mathbb{P}(W_T > 6.0236)
    $$

    Since $W_T \sim N(0, T) = N(0, 10)$, we standardize:

    $$
    \mathbb{P}\!\left(Z > \frac{6.0236}{\sqrt{10}}\right) = \mathbb{P}(Z > 1.904) \approx 2.85\%
    $$

    **Economic realism.** A $2.85\%$ probability of volatility exceeding 100% over 10 years is unrealistically high. In real markets, volatility exhibits strong mean reversion and rarely stays above 50% for extended periods, let alone reaching 100%. This illustrates the fundamental limitation of the SABR model for long-dated options: the GBM volatility dynamics produce excessively heavy tails in the volatility distribution, leading to option prices that overweight extreme volatility scenarios. Models with mean-reverting volatility (such as Heston) are far more appropriate for long-dated products.
