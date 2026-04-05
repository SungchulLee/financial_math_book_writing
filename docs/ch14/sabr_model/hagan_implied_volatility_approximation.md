# Hagan et al. Implied Volatility Approximation

The defining practical advantage of the SABR model is the existence of a closed-form approximation for the Black implied volatility as a function of the model parameters and strike. Derived by Hagan, Kumar, Lesniewski, and Woodward (2002) using singular perturbation methods, this formula allows traders to convert instantly between SABR parameters and implied volatilities without solving PDEs or performing Monte Carlo simulations. This section presents the complete Hagan approximation, derives its ATM specialization, discusses its accuracy limits, and demonstrates its application through worked examples.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State the Hagan implied volatility formula for general strikes
    2. Derive the ATM simplification and use it to determine $\alpha$ from the ATM quote
    3. Identify the regions where the approximation breaks down
    4. Handle numerical edge cases (ATM limit, small $\nu$, extreme strikes)
    5. Apply the formula to compute a complete implied volatility smile

---

## Motivation

In interest rate markets, a single swaption cube may contain tens of thousands of option prices across different expiries, tenors, and strikes. For risk management and real-time quoting, the model must produce implied volatilities in microseconds. Numerical methods such as PDE solvers or Monte Carlo are far too slow for this purpose. The Hagan approximation reduces SABR pricing to the evaluation of a single algebraic expression, making it feasible to calibrate the model to every expiry in real time and to compute Greeks by analytic differentiation. This speed is the primary reason the SABR model became the industry standard for interest rate smile modeling.

---

## The General Hagan Formula

### Black Implied Volatility

The Hagan approximation gives the Black (lognormal) implied volatility $\sigma_B(K)$ for a European option with strike $K$, forward $F$, and time to expiry $T$:

$$
\sigma_B(K) = \frac{\alpha}{(FK)^{(1-\beta)/2}\left[1 + \frac{(1-\beta)^2}{24}\ln^2\!\frac{F}{K} + \frac{(1-\beta)^4}{1920}\ln^4\!\frac{F}{K}\right]} \cdot \frac{z}{x(z)} \cdot \left[1 + \varepsilon T\right]
$$

where the auxiliary quantities are:

**Log-moneyness variable:**

$$
z = \frac{\nu}{\alpha}(FK)^{(1-\beta)/2}\ln\frac{F}{K}
$$

**Mapping function:**

$$
x(z) = \ln\!\left(\frac{\sqrt{1 - 2\rho z + z^2} + z - \rho}{1 - \rho}\right)
$$

**Time correction:**

$$
\varepsilon = \frac{(1-\beta)^2 \alpha^2}{24(FK)^{1-\beta}} + \frac{\rho\beta\nu\alpha}{4(FK)^{(1-\beta)/2}} + \frac{2 - 3\rho^2}{24}\nu^2
$$

!!! info "Structure of the Formula"
    The Hagan formula has three multiplicative components:

    1. **Leading term** $\alpha / (FK)^{(1-\beta)/2}$: the CEV backbone contribution
    2. **Smile factor** $z / x(z)$: encodes the skew and curvature from stochastic volatility and correlation
    3. **Time correction** $1 + \varepsilon T$: a first-order-in-$T$ correction that improves accuracy for longer maturities

    The formula is exact to first order in $T$ (i.e., the error is $O(T^2)$) and to all orders in the moneyness $\ln(F/K)$.

### Normal (Bachelier) Implied Volatility

The corresponding formula for the normal (Bachelier) implied volatility $\sigma_N(K)$ is:

$$
\sigma_N(K) = \frac{\alpha(F-K)}{(FK)^{(1-\beta)/2}\left[1 + \frac{(1-\beta)^2}{24}\ln^2\!\frac{F}{K} + \frac{(1-\beta)^4}{1920}\ln^4\!\frac{F}{K}\right]\ln\frac{F}{K}} \cdot \frac{z}{x(z)} \cdot \left[1 + \varepsilon_N T\right]
$$

where $z$ and $x(z)$ are the same as above, and:

$$
\varepsilon_N = \frac{-(1-\beta)^2\alpha^2}{24(FK)^{1-\beta}} + \frac{\rho\beta\nu\alpha}{4(FK)^{(1-\beta)/2}} + \frac{2 - 3\rho^2}{24}\nu^2
$$

The normal formula is preferred in negative-rate environments where $\beta = 0$ is used.

---

## ATM Implied Volatility

### The ATM Limit

At the money ($K = F$), the general formula simplifies considerably because $\ln(F/K) = 0$ and $z = 0$. Taking the limit carefully (since $z/x(z) \to 1$ as $z \to 0$):

$$
\sigma_B^{\text{ATM}} = \frac{\alpha}{F^{1-\beta}}\left[1 + \left(\frac{(1-\beta)^2\alpha^2}{24 F^{2(1-\beta)}} + \frac{\rho\beta\nu\alpha}{4 F^{1-\beta}} + \frac{2-3\rho^2}{24}\nu^2\right)T\right]
$$

The leading term $\alpha / F^{1-\beta}$ is the CEV backbone. The correction terms are $O(T)$ and typically small for maturities up to a few years.

### Solving for Alpha from the ATM Quote

In calibration, the ATM implied volatility $\sigma_{\text{ATM}}^{\text{mkt}}$ is known from the market. Given $(\beta, \rho, \nu)$, we solve for $\alpha$. Ignoring the $O(T)$ correction gives the leading-order estimate:

$$
\alpha_0 = \sigma_{\text{ATM}}^{\text{mkt}} \cdot F^{1-\beta}
$$

For a more accurate value, we solve the cubic equation obtained by substituting $\sigma_B^{\text{ATM}} = \sigma_{\text{ATM}}^{\text{mkt}}$ into the ATM formula. Defining $c_1 = (1-\beta)^2 T / (24 F^{2(1-\beta)})$, $c_2 = \rho\beta\nu T / (4 F^{1-\beta})$, and $c_3 = (2-3\rho^2)\nu^2 T / 24$, the equation becomes:

$$
\frac{\alpha}{F^{1-\beta}}(1 + c_1\alpha^2 + c_2\alpha + c_3) = \sigma_{\text{ATM}}^{\text{mkt}}
$$

This is a cubic in $\alpha$, typically solved by Newton's method starting from $\alpha_0$.

### Normal ATM Implied Volatility

The ATM normal implied volatility simplifies to:

$$
\sigma_N^{\text{ATM}} = \alpha F^{\beta}\left[1 + \left(\frac{-(1-\beta)^2\alpha^2}{24 F^{2(1-\beta)}} + \frac{\rho\beta\nu\alpha}{4 F^{1-\beta}} + \frac{2-3\rho^2}{24}\nu^2\right)T\right]
$$

---

## Derivation Sketch

### Singular Perturbation Approach

The Hagan formula is derived using a **singular perturbation expansion** in the small parameters $\varepsilon = \nu \sqrt{T}$ and $\delta = \alpha F^{\beta-1}\sqrt{T}$. The key steps are:

1. **Change of variables**: Transform the SABR forward $F$ to a new variable $y$ that absorbs the CEV exponent:

$$
y = \int_F \frac{du}{u^{\beta}} = \frac{F^{1-\beta}}{1-\beta} \quad (\beta \neq 1)
$$

2. **Heat kernel on hyperbolic geometry**: In the $(y, \sigma)$ coordinates, the SABR dynamics define a diffusion on a two-dimensional Riemannian manifold with the metric induced by the diffusion coefficients. The transition density is approximated using the **heat kernel expansion** on this manifold.

3. **Geodesic distance**: The leading-order term of the heat kernel involves the geodesic distance $d(y_0, \sigma_0; y, \sigma)$ between the initial and terminal points on the manifold. For the SABR geometry, this distance can be computed in closed form, leading to the $z/x(z)$ factor.

4. **Integration over terminal volatility**: The implied volatility is obtained by integrating the heat kernel over all possible terminal volatility values $\sigma_T$, yielding the correction terms.

5. **Inversion to implied volatility**: The option price is converted to implied volatility using the leading-order Black–Scholes or Bachelier inversion.

The result is accurate to $O(\varepsilon^2)$ in the perturbation parameter, which translates to $O(T^2)$ error in calendar time.

---

## Accuracy and Limitations

### Where the Approximation Works Well

The Hagan formula is highly accurate under the following conditions:

- **Short to moderate maturities**: $T \leq 5$ years for typical parameters
- **Near the money**: $|{\ln(F/K)}| \leq 1$ (roughly within $\pm$1 standard deviation)
- **Moderate vol-of-vol**: $\nu\sqrt{T} \leq 1$
- **Moderate correlation**: $|\rho| \leq 0.9$

Under these conditions, the approximation error is typically less than 0.5 basis points in implied volatility.

### Where the Approximation Breaks Down

The Hagan formula can produce inaccurate or even unphysical results in several regimes:

**Deep out-of-the-money strikes**: For $K \ll F$ or $K \gg F$, the approximation can produce negative implied volatilities, which is mathematically impossible. This occurs because the asymptotic expansion is valid only near the money.

**Long maturities with high vol-of-vol**: When $\nu\sqrt{T} \gg 1$, the $O(T^2)$ error terms become large, and the first-order correction $1 + \varepsilon T$ can exceed reasonable bounds.

**Negative probability density**: The implied density $p(K)$ derived from the Hagan formula (via the Breeden–Litzenberger formula) can become negative in the wings. This is a direct consequence of the asymptotic nature of the expansion and creates arbitrage opportunities.

!!! danger "Arbitrage in the Wings"
    The Hagan formula can produce implied volatilities that correspond to a **negative probability density** for extreme strikes. Specifically, the Breeden–Litzenberger relation:

    $$
    p(K) = e^{rT}\frac{\partial^2 C}{\partial K^2}
    $$

    can yield $p(K) < 0$ for deep OTM options. This is the primary motivation for the arbitrage-free SABR extensions discussed in a later section.

**Near-zero forward**: When $F \to 0$ with $\beta > 0$, the formula involves $F^{1-\beta} \to 0$ in the denominator, causing numerical instability. The normal SABR ($\beta = 0$) variant avoids this issue.

### Comparison with Exact Results

For the special case $\beta = 0$, $\rho = 0$ (the uncorrelated normal SABR), exact solutions are available via the McKean heat kernel. Comparisons show:

| Moneyness | Maturity | Hagan Error (bps) |
|-----------|----------|--------------------|
| ATM | 1Y | < 0.1 |
| $\pm$1 std dev | 1Y | < 0.5 |
| $\pm$2 std dev | 1Y | 1--5 |
| ATM | 5Y | < 1 |
| $\pm$2 std dev | 5Y | 5--20 |
| ATM | 10Y | 1--5 |
| $\pm$2 std dev | 10Y | 20--100 |

---

## Numerical Stability

### The ATM Limit (z approaching 0)

When $K \to F$, both $z \to 0$ and $\ln(F/K) \to 0$. The ratio $z/x(z)$ has the well-defined limit:

$$
\lim_{z \to 0} \frac{z}{x(z)} = 1
$$

However, naive computation of $z/x(z)$ using the general formula produces $0/0$. A Taylor expansion gives:

$$
\frac{z}{x(z)} = 1 - \frac{\rho}{2}z + \frac{3\rho^2 - 1}{12}z^2 + O(z^3)
$$

Implementations should switch to this Taylor expansion when $|z| < 10^{-6}$ (or a similar threshold).

### The Rho = 1 Limit

When $\rho \to 1$, the mapping function $x(z)$ simplifies:

$$
x(z)\big|_{\rho=1} = \ln\!\left(\frac{|1-z|+z-1}{0}\right)
$$

This is singular. The correct limit is:

$$
\lim_{\rho \to 1} \frac{z}{x(z)} = \frac{z}{\ln(1/(1-z))} \quad \text{for } z < 1
$$

In practice, $|\rho| < 1$ is always enforced, but implementations should handle $|\rho| > 0.9999$ with care.

### The Beta = 1 Limit

When $\beta = 1$, the CEV exponent vanishes and:

$$
z = \frac{\nu}{\alpha}\ln\frac{F}{K}
$$

The denominator simplifies: $(FK)^{(1-\beta)/2} = 1$ and the logarithmic correction terms vanish. The formula becomes:

$$
\sigma_B(K) = \alpha \cdot \frac{z}{x(z)} \cdot (1 + \varepsilon T)
$$

with $\varepsilon = \rho\nu\alpha/4 + (2-3\rho^2)\nu^2/24$.

---

## Worked Example

!!! example "Computing the SABR Smile"
    **Setup:** Consider a 1-year European swaption with forward swap rate $F = 3\%$, and SABR parameters $\beta = 0.5$, $\alpha = 0.035$, $\rho = -0.25$, $\nu = 0.40$.

    **Step 1: ATM implied volatility** ($K = F = 0.03$).

    The leading term is $\alpha / F^{1-\beta} = 0.035 / 0.03^{0.5} = 0.2021$ (20.21%).

    The correction: $c_1 = (0.5)^2(0.035)^2/(24 \cdot 0.03) = 4.25 \times 10^{-4}$, $c_2 = (-0.25)(0.5)(0.4)(0.035)/(4 \cdot 0.03^{0.5}) = -2.53 \times 10^{-3}$, $c_3 = (2 - 3(0.0625))(0.16)/24 = 1.22 \times 10^{-2}$.

    So $\sigma_B^{\text{ATM}} \approx 0.2021 \times (1 + 4.25 \times 10^{-4} - 2.53 \times 10^{-3} + 1.22 \times 10^{-2}) \approx 0.2041$ (20.41%).

    **Step 2: OTM put** ($K = 0.02$, one percentage point below ATM).

    Compute $z = (0.4/0.035)(0.03 \cdot 0.02)^{0.25}\ln(0.03/0.02) = 11.43 \times 0.1565 \times 0.4055 = 0.725$.

    Compute $x(z) = \ln((\sqrt{1+0.5\cdot0.725+0.725^2}+0.725+0.25)/1.25) = 0.643$.

    The smile factor $z/x(z) = 0.725/0.643 = 1.128$.

    After including the denominator and time correction, $\sigma_B(0.02) \approx 23.1\%$, which is higher than ATM --- reflecting the negative skew from $\rho < 0$.

    **Step 3: OTM call** ($K = 0.04$, one percentage point above ATM).

    A similar calculation yields $\sigma_B(0.04) \approx 18.8\%$, which is lower than ATM --- the other side of the skew.

    The implied volatility smile shows a characteristic downward-sloping shape driven by $\rho < 0$.

---

## Summary

The Hagan implied volatility approximation is the analytical formula that makes the SABR model practical for real-time applications. The formula decomposes into a CEV backbone term, a smile factor $z/x(z)$ encoding stochastic volatility effects, and a first-order time correction. At the money, the formula simplifies to give $\alpha$ directly from the ATM quote. The approximation is accurate for moderate moneyness and maturities but breaks down in the wings, where it can produce negative densities --- a limitation addressed by the arbitrage-free extensions. Numerical stability requires careful handling of the $z \to 0$, $\rho \to \pm 1$, and $\beta \to 1$ limits.

---

## Further Reading

- Hagan, P., Kumar, D., Lesniewski, A., & Woodward, D. (2002). *Managing smile risk*. Wilmott Magazine, 1, 84--108.
- Obloj, J. (2008). *Fine-tune your smile: Correction to Hagan et al.* Wilmott Magazine, March/April.
- Paulot, L. (2009). *Asymptotic implied volatility at the second order with application to the SABR model*. SSRN preprint.
- Gatheral, J. (2006). *The Volatility Surface*. Wiley, Chapter 7.

---

## Exercises

**Exercise 1.** Using the ATM Hagan formula for general $\beta$:

$$
\sigma_{\text{ATM}} = \frac{\alpha}{F^{1-\beta}}\left[1 + \left(\frac{(1-\beta)^2}{24}\frac{\alpha^2}{F^{2(1-\beta)}} + \frac{\rho\beta\nu\alpha}{4F^{1-\beta}} + \frac{2-3\rho^2}{24}\nu^2\right)T\right]
$$

compute $\sigma_{\text{ATM}}$ for $F = 0.03$, $\alpha = 0.025$, $\beta = 0.5$, $\rho = -0.3$, $\nu = 0.4$, $T = 1$. Identify the contribution of each correction term separately.

??? success "Solution to Exercise 1"
    With $F = 0.03$, $\alpha = 0.025$, $\beta = 0.5$, $\rho = -0.3$, $\nu = 0.4$, $T = 1$:

    **Leading term:**

    $$
    \frac{\alpha}{F^{1-\beta}} = \frac{0.025}{0.03^{0.5}} = \frac{0.025}{0.17321} = 0.14430 = 14.43\%
    $$

    **Correction term $c_1$** (backbone):

    $$
    \frac{(1-\beta)^2\alpha^2}{24 F^{2(1-\beta)}} = \frac{(0.5)^2(0.025)^2}{24(0.03)^1} = \frac{1.5625 \times 10^{-4}}{7.2 \times 10^{-1}} = 2.170 \times 10^{-4}
    $$

    **Correction term $c_2$** (correlation-beta):

    $$
    \frac{\rho\beta\nu\alpha}{4 F^{1-\beta}} = \frac{(-0.3)(0.5)(0.4)(0.025)}{4(0.03)^{0.5}} = \frac{-1.5 \times 10^{-3}}{0.6928} = -2.165 \times 10^{-3}
    $$

    **Correction term $c_3$** (curvature):

    $$
    \frac{2 - 3\rho^2}{24}\nu^2 = \frac{2 - 3(0.09)}{24}(0.16) = \frac{1.73}{24}(0.16) = 1.153 \times 10^{-2}
    $$

    **Total correction:** $c_1 + c_2 + c_3 = 2.170 \times 10^{-4} - 2.165 \times 10^{-3} + 1.153 \times 10^{-2} = 9.582 \times 10^{-3}$.

    $$
    \sigma_{\text{ATM}} = 0.14430 \times (1 + 9.582 \times 10^{-3}) = 0.14430 \times 1.00958 = 0.14568 = 14.57\%
    $$

    The curvature term ($c_3$) dominates the correction, contributing about $+1.15\%$ relative, while the correlation term ($c_2$) contributes about $-0.22\%$ relative and the backbone term ($c_1$) is negligible at $+0.02\%$.

---

**Exercise 2.** The Hagan formula involves the function $x(z) = \ln\!\bigl(\frac{\sqrt{1-2\rho z+z^2}+z-\rho}{1-\rho}\bigr)$. Show that $x(z)/z \to 1$ as $z \to 0$ (using L'Hopital's rule or Taylor expansion). Why is this limit important for the ATM case where $K = F$?

??? success "Solution to Exercise 2"
    Define $f(z) = x(z)/z$ and compute the limit as $z \to 0$. Since both $x(0) = 0$ and $z \to 0$, we apply L'Hopital's rule:

    $$
    \lim_{z \to 0}\frac{x(z)}{z} = \lim_{z \to 0} x'(z)
    $$

    Computing $x'(z)$: let $g(z) = \sqrt{1 - 2\rho z + z^2}$. Then:

    $$
    g'(z) = \frac{-\rho + z}{\sqrt{1 - 2\rho z + z^2}}
    $$

    $$
    x(z) = \ln\!\left(\frac{g(z) + z - \rho}{1 - \rho}\right)
    $$

    $$
    x'(z) = \frac{g'(z) + 1}{g(z) + z - \rho}
    $$

    At $z = 0$: $g(0) = 1$, $g'(0) = -\rho$, and $g(0) + 0 - \rho = 1 - \rho$. Therefore:

    $$
    x'(0) = \frac{-\rho + 1}{1 - \rho} = 1
    $$

    So $\lim_{z \to 0} x(z)/z = 1$, which means $\lim_{z \to 0} z/x(z) = 1$.

    This limit is critical for the ATM case because when $K = F$, the log-moneyness $\ln(F/K) = 0$, which forces $z = 0$. The ratio $z/x(z)$ appears as a multiplicative factor in the Hagan formula, and its limit of 1 at $z = 0$ ensures that the ATM implied volatility is determined solely by the backbone term $\alpha / F^{1-\beta}$ and the time correction, without the smile factor contributing. In numerical implementations, computing $z/x(z)$ directly at $z = 0$ produces $0/0$, so the Taylor expansion must be used.

---

**Exercise 3.** Compute the SABR implied volatility at strikes $K = 0.02, 0.025, 0.03, 0.035, 0.04$ using the Hagan formula with parameters $F = 0.03$, $\alpha = 0.025$, $\beta = 0.5$, $\rho = -0.3$, $\nu = 0.45$, $T = 1$. Plot or sketch the resulting smile. Identify the skew and curvature visually.

??? success "Solution to Exercise 3"
    Using $F = 0.03$, $\alpha = 0.025$, $\beta = 0.5$, $\rho = -0.3$, $\nu = 0.45$, $T = 1$:

    For each strike, compute $z$, $x(z)$, the denominator, and the time correction $\varepsilon$.

    **$K = 0.02$** (100 bps OTM put): $(FK)^{0.25} = (6 \times 10^{-4})^{0.25} = 0.15651$. $z = (0.45/0.025)(0.15651)\ln(1.5) = 18 \times 0.15651 \times 0.4055 = 1.142$. After computing $x(z)$ and the full formula, $\sigma_B \approx 18.8\%$.

    **$K = 0.025$** (50 bps OTM put): $z \approx 0.548$, $\sigma_B \approx 16.2\%$.

    **$K = 0.03$** (ATM): $z = 0$, $z/x(z) = 1$, $\sigma_B \approx 14.6\%$ (from Exercise 1 with adjusted $\nu$).

    **$K = 0.035$** (50 bps OTM call): $z \approx -0.497$, $\sigma_B \approx 13.6\%$.

    **$K = 0.04$** (100 bps OTM call): $z \approx -0.925$, $\sigma_B \approx 13.0\%$.

    The resulting smile shows clear **negative skew** driven by $\rho = -0.3$: OTM puts have higher implied vol than OTM calls. There is also visible **curvature** from $\nu = 0.45$: both wings are lifted relative to a purely linear skew. The skew is the dominant feature at moderate moneyness, while the curvature becomes more apparent at extreme strikes.

---

**Exercise 4.** The Hagan formula is an asymptotic expansion valid for small $\nu^2 T$ and moderate log-moneyness. Estimate the reliability by computing $\sigma_{\text{Hagan}}$ at $K/F = 0.5$ (deep OTM put) and $T = 10$ years, with $\alpha = 0.03$, $\beta = 0.5$, $\rho = -0.4$, $\nu = 0.5$. Is the correction term $O(\nu^2 T)$ small? At what point does the approximation become unreliable?

??? success "Solution to Exercise 4"
    With $F = 0.03$, $K/F = 0.5$ (so $K = 0.015$, deep OTM put), $T = 10$, $\alpha = 0.03$, $\beta = 0.5$, $\rho = -0.4$, $\nu = 0.5$:

    The $O(\nu^2 T)$ correction parameter is $\nu^2 T = 0.25 \times 10 = 2.5$. This is far from "small" --- the entire Hagan formula is built on the assumption that $\nu^2 T \ll 1$, meaning the correction factor $1 + \varepsilon T$ should be close to 1.

    With $\varepsilon T \approx 2.5$, the multiplicative correction is roughly $1 + 2.5 = 3.5$, which is an enormous departure from the leading-order estimate. The time correction term is no longer a small perturbation but dominates the result.

    At this moneyness ($\ln(F/K) = \ln 2 = 0.693$), the smile factor $z/x(z)$ also departs significantly from 1, and the higher-order terms in the denominator become material.

    The approximation becomes unreliable when $\nu^2 T \gtrsim 0.5$, which corresponds to $T \gtrsim 2$ years for $\nu = 0.5$ or $T \gtrsim 5$ years for $\nu = 0.3$. At $T = 10$ with $\nu = 0.5$, the Hagan formula is quantitatively unreliable and may even produce negative implied volatilities for deep OTM strikes. Exact solutions or PDE methods should be used instead.

---

**Exercise 5.** Derive the first-order skew at ATM:

$$
\frac{\partial\sigma_{\text{impl}}}{\partial k}\bigg|_{k=0} \approx \frac{\rho\nu}{2\sigma_{\text{ATM}}} - \frac{(1-\beta)}{2F}
$$

by differentiating the Hagan formula with respect to $k = \ln(K/F)$. For $\beta = 0.5$, $F = 0.03$, $\rho = -0.4$, $\nu = 0.5$, $\sigma_{\text{ATM}} = 0.15$, compute the skew. Which term dominates: the correlation-induced skew or the backbone skew?

??? success "Solution to Exercise 5"
    Differentiating the Hagan formula with respect to $k = \ln(K/F)$ and evaluating at $k = 0$ (ATM):

    The leading-order Hagan formula near ATM can be written as $\sigma_B \approx (\alpha / F^{1-\beta}) \cdot (z/x(z)) \cdot (1 + \varepsilon T)$. At ATM, $z = (\nu/\alpha)(FK)^{(1-\beta)/2} \cdot k$, so $\partial z / \partial k|_{k=0} = (\nu/\alpha) F^{1-\beta}$. The backbone contribution to the skew comes from $\alpha / (FK)^{(1-\beta)/2}$, which gives $\partial / \partial k$ evaluated at $k = 0$ a factor of $-(1-\beta)/2$ from the geometric average.

    Combining all terms, the ATM skew is:

    $$
    \frac{\partial\sigma_{\text{impl}}}{\partial k}\bigg|_{k=0} \approx \frac{\rho\nu}{2\sigma_{\text{ATM}}} - \frac{(1-\beta)}{2F}
    $$

    The first term is the **correlation-induced skew** and the second is the **backbone skew**.

    With $\beta = 0.5$, $F = 0.03$, $\rho = -0.4$, $\nu = 0.5$, $\sigma_{\text{ATM}} = 0.15$:

    Correlation skew: $\frac{(-0.4)(0.5)}{2(0.15)} = \frac{-0.2}{0.3} = -0.667$

    Backbone skew: $-\frac{0.5}{2(0.03)} = -\frac{0.5}{0.06} = -8.333$

    The **backbone skew dominates** by more than an order of magnitude ($-8.33$ vs $-0.67$). This is typical for interest rate options where $F$ is a small number (e.g., 3%): the $1/F$ factor in the backbone skew amplifies it enormously. The correlation-induced skew is a secondary effect that fine-tunes the shape. This explains why $\beta$ (which controls the backbone) has a more dramatic effect on the overall smile than $\rho$ (which controls the correlation skew).

---

**Exercise 6.** The Obloj (2008) correction modifies the Hagan formula to improve accuracy in the wings. Without deriving the correction, explain qualitatively why the original formula can produce implied volatilities that decrease too rapidly for extreme strikes. What is the practical consequence of using the uncorrected formula for risk management of deeply OTM options?

??? success "Solution to Exercise 6"
    The original Hagan formula is an asymptotic expansion around the ATM point ($K = F$), valid to first order in the expansion parameter $\varepsilon \sim \nu\sqrt{T}$. For extreme strikes, the error grows as a power of $|\ln(F/K)|$. The expansion captures the **leading-order smile shape** but not the tail behavior.

    The formula can produce implied volatilities that decrease too rapidly in the wings because the perturbation expansion "overshoots" the curvature correction. Specifically, the $z/x(z)$ factor, while capturing the smile to leading order, does not correctly reproduce the tail asymptotics of the true SABR density. The true density decays as a power law (or modified Gaussian) in the far tails, but the Hagan formula can predict a faster decay that implies too little probability mass in the wings.

    In extreme cases, the formula produces $\sigma_B(K) < 0$ for very deep OTM strikes, which is mathematically impossible. Even when $\sigma_B(K)$ remains positive, the implied density (computed via the Breeden--Litzenberger formula $f(K) \propto \partial^2 C / \partial K^2$) can become negative, creating butterfly arbitrage.

    The practical consequences for risk management of deeply OTM options include:

    - **Underpricing of tail risk**: Deep OTM puts appear cheaper than they should be, leading traders to underestimate the cost of portfolio insurance.
    - **Arbitrage signals**: Risk systems may flag false arbitrage opportunities in the wings.
    - **CMS mispricing**: CMS products that integrate over the entire strike domain are sensitive to wing behavior and can be materially mispriced.
    - **Incorrect Greeks**: Delta and gamma computed from the uncorrected formula are unreliable for deep OTM positions.
