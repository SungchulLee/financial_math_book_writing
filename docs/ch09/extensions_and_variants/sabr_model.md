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

### The CEV Exponent ($\beta$)

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

### Volatility of Volatility ($\nu$)

The parameter $\nu$ controls **smile curvature**:
- Higher $\nu$ → more convex smile
- $\nu = 0$ → no smile (CEV model only)

### Correlation ($\rho$)

The parameter $\rho$ controls **smile skew**:
- $\rho < 0$ → negative skew (equity-like)
- $\rho > 0$ → positive skew
- $\rho = 0$ → symmetric smile

**Typical equity values:** $\rho \in [-0.5, -0.9]$

### Initial Volatility ($\alpha$)

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

### ATM Formula ($K = F$)

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

### Dealing with $\beta$

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

### Normal SABR ($\beta = 0$)

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
