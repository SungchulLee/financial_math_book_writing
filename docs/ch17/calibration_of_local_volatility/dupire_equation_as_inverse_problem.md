# Dupire Equation as an Inverse Problem


Local volatility models provide an *exact* fit (in principle) to a continuum of vanilla option prices. This exactness comes at a cost: constructing the local volatility surface is a **highly ill-posed inverse problem** because it requires differentiating noisy market data.

---

## The local volatility model


In the (risk-neutral) local volatility model, the underlying $S_t$ follows

$$
dS_t = (r-q)S_t\,dt + \sigma_{\text{loc}}(t,S_t)\,S_t\,dW_t
$$


where $r$ is the risk-free rate, $q$ is the dividend yield (or convenience yield), and
$\sigma_{\text{loc}}(t,S)$ is the **local volatility** function to be calibrated.

Given $\sigma_{\text{loc}}$, the model implies a unique surface of European option prices $C(K,T)$.

---

## Dupire’s forward equation


Let $C(K,T)$ denote the time-0 price of a European call with strike $K$ and maturity $T$.
Under standard smoothness assumptions, Dupire derived a forward PDE relating $C$ and $\sigma_{\text{loc}}$.

A common (simplified) form is:

$$
\partial_T C(K,T)
= \frac12\,\sigma_{\text{loc}}^2(T,K)\,K^2\,\partial_{KK} C(K,T)

- (r-q)K\,\partial_K C(K,T)
+ q\,C(K,T)
$$


where derivatives are with respect to strike.

Solving this equation *forward* is the pricing problem.

---

## Inverting Dupire: extracting local volatility


Rearranging the forward equation yields an expression for local variance

$$
\sigma_{\text{loc}}^2(T,K)
= \frac{2\left(\partial_T C + (r-q)K\partial_K C - q C\right)}
{K^2\,\partial_{KK} C}
$$



This reveals why calibration is an inverse problem:

- it requires $\partial_T C$ and $\partial_{KK} C$,
- these are *derivatives* of market prices, which are observed only at discrete points and contaminated by noise.

Thus, the mapping

$$
C(\cdot,\cdot) \longmapsto \sigma_{\text{loc}}(\cdot,\cdot)
$$


is an unstable inversion involving differentiation and division by curvature.

---

## Relationship to implied volatility


Market data are often given as implied vol $\sigma_{\text{impl}}(K,T)$, not prices.
One may:

1. convert implied vol to prices via Black–Scholes,
2. interpolate to a smooth surface,
3. apply Dupire to the smoothed price surface.

Alternatively, Dupire can be written directly in terms of implied vol or total variance, but the same inverse-problem issues remain: derivatives are needed.

---

## Key takeaways


- Dupire provides a *theoretical* route from a smooth call price surface to $\sigma_{\text{loc}}(T,K)$.
- Calibration is an inverse problem because it requires **differentiating noisy, discrete data**.
- Practical implementation requires smoothing, arbitrage filtering, and careful numerics.

---

## Further reading


- Dupire (1994), “Pricing with a Smile”.
- Gatheral, *The Volatility Surface* (local vol and implied vol geometry).
- Fengler, *Semiparametric Modeling of Implied Volatility* (surface construction).

---

## Exercises

**Exercise 1.** Starting from Dupire's forward PDE

$$
\partial_T C = \frac{1}{2}\sigma_{\text{loc}}^2(T,K)\,K^2\,\partial_{KK}C - (r-q)K\,\partial_K C + qC
$$

derive the inversion formula for $\sigma_{\text{loc}}^2(T,K)$ by solving algebraically for the local variance. State explicitly which quantity appears in the denominator and explain why its sign is guaranteed under no-arbitrage conditions.

??? success "Solution to Exercise 1"
    Starting from the Dupire forward PDE

    $$
    \partial_T C = \frac{1}{2}\sigma_{\text{loc}}^2(T,K)\,K^2\,\partial_{KK}C - (r-q)K\,\partial_K C + qC
    $$

    we isolate the term containing $\sigma_{\text{loc}}^2$ by moving all other terms to the left-hand side:

    $$
    \partial_T C + (r-q)K\,\partial_K C - qC = \frac{1}{2}\sigma_{\text{loc}}^2(T,K)\,K^2\,\partial_{KK}C
    $$

    Dividing both sides by $\frac{1}{2}K^2\,\partial_{KK}C$ yields the inversion formula:

    $$
    \sigma_{\text{loc}}^2(T,K) = \frac{2\bigl(\partial_T C + (r-q)K\,\partial_K C - qC\bigr)}{K^2\,\partial_{KK}C}
    $$

    The denominator is $K^2\,\partial_{KK}C$. Since $K^2 > 0$ always, the critical factor is $\partial_{KK}C$.

    Under no-arbitrage conditions, $\partial_{KK}C \ge 0$ is guaranteed by the **butterfly spread condition**. To see this, consider the butterfly payoff at strikes $K - h$, $K$, $K + h$:

    $$
    \text{Butterfly} = C(K-h) - 2C(K) + C(K+h) \ge 0
    $$

    This non-negativity holds because the butterfly payoff $(S_T - (K-h))^+ - 2(S_T - K)^+ + (S_T - (K+h))^+$ is non-negative for all $S_T$, and a non-negative payoff must have a non-negative price under no-arbitrage. Dividing by $h^2$ and taking $h \to 0$ gives $\partial_{KK}C \ge 0$.

    Moreover, strict convexity ($\partial_{KK}C > 0$) holds whenever the risk-neutral density is strictly positive, since $\partial_{KK}C$ equals the discounted risk-neutral density $e^{-rT}q(K)$ at that strike. This ensures the denominator is strictly positive, making the Dupire inversion well-defined.

---

**Exercise 2.** Consider a flat implied volatility surface $\sigma_{\text{impl}}(K,T) = \sigma_0$ for all $K, T$. Compute $\partial_T C$ and $\partial_{KK} C$ from the Black--Scholes formula, and show that the Dupire formula recovers $\sigma_{\text{loc}}(T,K) = \sigma_0$ everywhere.

??? success "Solution to Exercise 2"
    Under a flat implied volatility surface $\sigma_{\text{impl}}(K,T) = \sigma_0$, the call price is given by the Black--Scholes formula:

    $$
    C(K,T) = S_0 e^{-qT}N(d_1) - K e^{-rT}N(d_2)
    $$

    where $d_1 = \frac{\ln(S_0/K) + (r - q + \frac{1}{2}\sigma_0^2)T}{\sigma_0\sqrt{T}}$ and $d_2 = d_1 - \sigma_0\sqrt{T}$.

    **Computing $\partial_T C$:** By the Black--Scholes PDE in forward variables, we have

    $$
    \partial_T C = \frac{S_0 e^{-qT}\sigma_0 \,\phi(d_1)}{2\sqrt{T}} + qS_0 e^{-qT}N(d_1) - rKe^{-rT}N(d_2)
    $$

    where $\phi(\cdot)$ is the standard normal density.

    **Computing $\partial_{KK} C$:** Taking the first derivative with respect to $K$:

    $$
    \partial_K C = -e^{-rT}N(d_2)
    $$

    Taking the second derivative:

    $$
    \partial_{KK} C = e^{-rT}\frac{\phi(d_2)}{K\sigma_0\sqrt{T}}
    $$

    **Substituting into Dupire's formula:**

    $$
    \sigma_{\text{loc}}^2 = \frac{2\bigl(\partial_T C + (r-q)K\partial_K C - qC\bigr)}{K^2\,\partial_{KK}C}
    $$

    For the numerator, using the relation $S_0 e^{-qT}\phi(d_1) = K e^{-rT}\phi(d_2)$ (which follows from the log-normal structure), we substitute:

    $$
    \partial_T C + (r-q)K\partial_K C - qC
    $$

    $$
    = \frac{Ke^{-rT}\phi(d_2)\sigma_0}{2\sqrt{T}} + qS_0 e^{-qT}N(d_1) - rKe^{-rT}N(d_2)
    $$

    $$
    \quad - (r-q)Ke^{-rT}N(d_2) - q\bigl(S_0 e^{-qT}N(d_1) - Ke^{-rT}N(d_2)\bigr)
    $$

    The terms involving $N(d_1)$ cancel: $qS_0 e^{-qT}N(d_1) - qS_0 e^{-qT}N(d_1) = 0$. The terms involving $N(d_2)$ also cancel: $-rKe^{-rT}N(d_2) - (r-q)Ke^{-rT}N(d_2) + qKe^{-rT}N(d_2) = Ke^{-rT}N(d_2)(-r - r + q + q) = -2(r-q)Ke^{-rT}N(d_2)$... Let us proceed more carefully by collecting all $N(d_2)$ terms:

    $$
    -rKe^{-rT}N(d_2) - (r-q)Ke^{-rT}N(d_2) + qKe^{-rT}N(d_2) = Ke^{-rT}N(d_2)(-r - r + q + q) = 0
    $$

    since $-r -(r-q)+q = -2r+2q$... Actually, let us recount: $-r -(r-q)+q = -r -r +q +q = -2r+2q$. This is zero only when $r=q$.

    A cleaner approach uses the Black--Scholes PDE directly. The call price satisfies

    $$
    \partial_T C = \frac{1}{2}\sigma_0^2 K^2 \partial_{KK}C - (r-q)K\partial_K C + qC
    $$

    This is precisely Dupire's forward equation with $\sigma_{\text{loc}}^2(T,K)$ replaced by $\sigma_0^2$. Substituting into the Dupire inversion formula:

    $$
    \sigma_{\text{loc}}^2(T,K) = \frac{2\bigl(\partial_T C + (r-q)K\partial_K C - qC\bigr)}{K^2\,\partial_{KK}C}
    $$

    $$
    = \frac{2 \cdot \frac{1}{2}\sigma_0^2 K^2 \partial_{KK}C}{K^2\,\partial_{KK}C} = \sigma_0^2
    $$

    Therefore $\sigma_{\text{loc}}(T,K) = \sigma_0$ everywhere, confirming that the Dupire formula correctly recovers a constant local volatility from a flat implied volatility surface.

---

**Exercise 3.** Suppose observed call prices are contaminated by additive noise: $\hat{C}(K_i, T_j) = C(K_i, T_j) + \varepsilon_{ij}$ where $\varepsilon_{ij} \sim N(0, \delta^2)$. Using a finite-difference approximation for $\partial_{KK}C$ with strike spacing $\Delta K$, show that the variance of the estimated second derivative scales as

$$
\operatorname{Var}\!\left(\widehat{\partial_{KK}C}\right) \sim \frac{\delta^2}{(\Delta K)^4}
$$

Explain why this makes the Dupire inversion ill-posed and discuss the trade-off between bias and variance as $\Delta K$ varies.

??? success "Solution to Exercise 3"
    Let the observed prices be $\hat{C}(K_i, T_j) = C(K_i, T_j) + \varepsilon_{ij}$ with $\varepsilon_{ij} \sim N(0, \delta^2)$ independent. The central finite-difference approximation for the second derivative in strike is

    $$
    \widehat{\partial_{KK}C}(K,T) = \frac{\hat{C}(K+\Delta K,T) - 2\hat{C}(K,T) + \hat{C}(K-\Delta K,T)}{(\Delta K)^2}
    $$

    Substituting the noisy observations:

    $$
    \widehat{\partial_{KK}C} = \frac{(C_{+} + \varepsilon_{+}) - 2(C_0 + \varepsilon_0) + (C_{-} + \varepsilon_{-})}{(\Delta K)^2}
    $$

    $$
    = \underbrace{\frac{C_{+} - 2C_0 + C_{-}}{(\Delta K)^2}}_{\text{true value}+O((\Delta K)^2)} + \frac{\varepsilon_{+} - 2\varepsilon_0 + \varepsilon_{-}}{(\Delta K)^2}
    $$

    The noise term is $Z = (\varepsilon_{+} - 2\varepsilon_0 + \varepsilon_{-})/(\Delta K)^2$. Since the $\varepsilon$ terms are independent with variance $\delta^2$:

    $$
    \operatorname{Var}(Z) = \frac{1^2 + (-2)^2 + 1^2}{(\Delta K)^4}\,\delta^2 = \frac{6\delta^2}{(\Delta K)^4}
    $$

    This confirms that $\operatorname{Var}(\widehat{\partial_{KK}C}) \sim \delta^2/(\Delta K)^4$ (with proportionality constant 6).

    **Why this makes Dupire ill-posed:** The Dupire formula divides by $\partial_{KK}C$, so the estimated local variance inherits the noise from this estimate. As $\Delta K \to 0$, the variance of the estimated second derivative grows as $1/(\Delta K)^4$, which diverges rapidly. This means that refining the strike grid does not improve accuracy---it makes it worse.

    **Bias-variance trade-off:** The total error in estimating $\partial_{KK}C$ has two components:

    - **Bias** (truncation error): $\sim C^{(4)}(\Delta K)^2/12$, which decreases as $\Delta K \to 0$.
    - **Variance** (noise amplification): $\sim 6\delta^2/(\Delta K)^4$, which increases as $\Delta K \to 0$.

    There is an optimal $\Delta K$ that balances these. Setting the derivative of the total mean squared error to zero gives

    $$
    (\Delta K)^{\star} \sim \left(\frac{\delta}{|C^{(4)}|}\right)^{1/3}
    $$

    Below this optimal spacing, noise dominates; above it, truncation error dominates. This fundamental trade-off is the hallmark of ill-posed inverse problems.

---

**Exercise 4.** A trader observes European call prices at strikes $K \in \{80, 90, 100, 110, 120\}$ and maturities $T \in \{0.25, 0.50\}$ with $S_0 = 100$, $r = 0.03$, $q = 0$. Using finite differences, write down explicit formulas for approximating $\partial_T C(K, T)$ and $\partial_{KK} C(K, T)$ at the grid point $(K=100, T=0.25)$. Identify which market quotes are needed.

??? success "Solution to Exercise 4"
    The trader needs to approximate two derivatives at the grid point $(K=100, T=0.25)$.

    **Approximation of $\partial_T C(100, 0.25)$:** Using a forward difference in maturity with $\Delta T = 0.50 - 0.25 = 0.25$:

    $$
    \partial_T C(100, 0.25) \approx \frac{C(100, 0.50) - C(100, 0.25)}{\Delta T} = \frac{C(100, 0.50) - C(100, 0.25)}{0.25}
    $$

    This requires the market quotes $C(100, 0.25)$ and $C(100, 0.50)$.

    **Approximation of $\partial_{KK}C(100, 0.25)$:** Using the central difference in strike with $h = 10$:

    $$
    \partial_{KK}C(100, 0.25) \approx \frac{C(110, 0.25) - 2C(100, 0.25) + C(90, 0.25)}{h^2} = \frac{C(110, 0.25) - 2C(100, 0.25) + C(90, 0.25)}{100}
    $$

    This requires the market quotes $C(90, 0.25)$, $C(100, 0.25)$, and $C(110, 0.25)$.

    **Approximation of $\partial_K C(100, 0.25)$** (needed for the full Dupire formula): Using the central difference:

    $$
    \partial_K C(100, 0.25) \approx \frac{C(110, 0.25) - C(90, 0.25)}{2h} = \frac{C(110, 0.25) - C(90, 0.25)}{20}
    $$

    **Summary of required quotes:** The five market prices needed are:

    - $C(90, 0.25)$, $C(100, 0.25)$, $C(110, 0.25)$ (for strike derivatives)
    - $C(100, 0.50)$ (for the time derivative)

    Note that $C(100, 0.25)$ is used in all three approximations. The quotes at $K \in \{80, 120\}$ are not directly needed for these first-order finite-difference formulas, although they could be used for higher-order stencils or for computing $\partial_K C$ and $\partial_{KK}C$ at neighboring strikes.

---

**Exercise 5.** The butterfly spread condition requires $\partial_{KK}C \ge 0$ for absence of arbitrage. Show that if this condition is violated at some point $(K_0, T_0)$ in the interpolated surface, the Dupire formula yields a negative local variance $\sigma_{\text{loc}}^2(T_0, K_0) < 0$. Propose a practical remedy using arbitrage filtering before applying the Dupire inversion.

??? success "Solution to Exercise 5"
    The Dupire inversion formula (with $r = q = 0$ for simplicity) is

    $$
    \sigma_{\text{loc}}^2(T_0, K_0) = \frac{2\,\partial_T C(K_0, T_0)}{K_0^2\,\partial_{KK}C(K_0, T_0)}
    $$

    The numerator $\partial_T C$ represents the time value of the option. Under no-arbitrage, call prices are non-decreasing in maturity (for $q = 0$), so $\partial_T C \ge 0$. Thus the numerator is non-negative.

    The denominator involves $K_0^2 > 0$ and $\partial_{KK}C$. If the butterfly spread condition is violated at $(K_0, T_0)$, then $\partial_{KK}C(K_0, T_0) < 0$.

    Combining a non-negative numerator with a negative denominator:

    $$
    \sigma_{\text{loc}}^2(T_0, K_0) = \frac{2\,\partial_T C}{K_0^2\,\partial_{KK}C} = \frac{(\ge 0)}{(< 0)} \le 0
    $$

    Since variance must be non-negative, a negative $\sigma_{\text{loc}}^2$ is unphysical and signals an arbitrage violation in the input data. More precisely, $\partial_{KK}C < 0$ means the risk-neutral density implied by the interpolated surface is negative at that point, which is impossible for a probability density.

    **Practical remedy using arbitrage filtering:**

    1. **Detection:** After constructing the interpolated call surface, compute $\partial_{KK}C$ at all grid points. Flag any point where $\partial_{KK}C \le 0$ (or below a small positive threshold $\epsilon$).

    2. **Local adjustment:** For isolated violations, adjust the call prices at and around the offending strikes to restore convexity. This can be done by solving a constrained optimization:

        $$
        \min_{\tilde{C}} \sum_i (\tilde{C}_i - C_i^{\text{obs}})^2 \quad \text{subject to} \quad \tilde{C}(K_{i-1}) - 2\tilde{C}(K_i) + \tilde{C}(K_{i+1}) \ge 0 \;\;\forall i
        $$

    3. **Global constrained fitting:** Fit a parametric model (such as SVI) that enforces convexity by construction. Since SVI total variance has $\partial_{kk}w > 0$ when $b > 0$ and $\sigma > 0$, the resulting call surface automatically satisfies the butterfly condition.

    4. **Bid-ask band approach:** Allow each quote to move within its bid-ask spread, then find the smoothest surface within these bands that satisfies all no-arbitrage constraints.

---

**Exercise 6.** Let the total implied variance be defined as $w(K,T) = \sigma_{\text{impl}}^2(K,T)\cdot T$. Show that Dupire's formula can be rewritten in terms of $w$ as

$$
\sigma_{\text{loc}}^2 = \frac{\partial_T w}{1 - \frac{y}{w}\partial_y w + \frac{1}{4}\left(-\frac{1}{4} - \frac{1}{w} + \frac{y^2}{w^2}\right)(\partial_y w)^2 + \frac{1}{2}\partial_{yy}w}
$$

where $y = \ln(K/F_T)$ is the log-moneyness. Discuss why working in the $(y, T)$ coordinate system can improve numerical stability compared to working directly with $(K, T)$.

??? success "Solution to Exercise 6"
    We start with Dupire's formula in $(K, T)$ coordinates and perform a change of variables to log-moneyness $y = \ln(K/F_T)$, where $F_T = S_0 e^{(r-q)T}$ is the forward price.

    **Change of variables:** Since $K = F_T e^y$, we have $\partial_K = (1/K)\partial_y$ and $\partial_{KK} = (1/K^2)(\partial_{yy} - \partial_y)$.

    The total implied variance is $w(y, T) = \sigma_{\text{impl}}^2(y, T)\cdot T$. The Black--Scholes call price can be written in terms of $w$ as

    $$
    C = F_T e^{-rT}\bigl[N(d_1) - e^{-y}N(d_2)\bigr]
    $$

    where $d_1 = -y/\sqrt{w} + \frac{1}{2}\sqrt{w}$ and $d_2 = d_1 - \sqrt{w}$.

    After careful computation of $\partial_T C$, $\partial_y C$, and $\partial_{yy}C$ in terms of $w$ and its derivatives, and substituting into Dupire's formula, one obtains (following Gatheral's derivation):

    $$
    \sigma_{\text{loc}}^2 = \frac{\partial_T w}{1 - \frac{y}{w}\partial_y w + \frac{1}{4}\left(-\frac{1}{4} - \frac{1}{w} + \frac{y^2}{w^2}\right)(\partial_y w)^2 + \frac{1}{2}\partial_{yy}w}
    $$

    **Derivation sketch:** The key identity is that the call price density (second derivative in strike) can be expressed via the Black--Scholes formula as a function of $w$ alone. The denominator arises from expressing $K^2\partial_{KK}C$ in terms of $w$, $\partial_y w$, and $\partial_{yy}w$ through the chain rule and the Black--Scholes vega/volga structure. The numerator $\partial_T C + (r-q)K\partial_K C - qC$ simplifies to a term proportional to $\partial_T w$ because the forward-measure discounting absorbs the drift terms.

    **Why $(y, T)$ coordinates improve numerical stability:**

    1. **Dimensionless variable:** Log-moneyness $y$ is dimensionless and centered at zero (ATM corresponds to $y = 0$), whereas $K$ has units and varies across a wide range. This improves the conditioning of interpolation and differentiation.

    2. **Smoother behavior:** Total implied variance $w(y, T)$ is more nearly linear in both $y$ and $T$ than call prices $C(K, T)$ are. This means that interpolation and differentiation introduce smaller errors.

    3. **Calendar arbitrage is transparent:** The condition $\partial_T w \ge 0$ for fixed $y$ directly ensures no calendar arbitrage, making it easy to check and enforce. In $(K, T)$ coordinates, the analogous condition on $C$ is less transparent.

    4. **Butterfly arbitrage is localized:** The denominator is a function of $w$ and its $y$-derivatives only (at fixed $T$), so convexity checks reduce to verifying that the denominator is positive, which can be done slice by slice.

    5. **Reduced sensitivity near ATM:** Near $y = 0$, the terms $y/w$ and $y^2/w^2$ are small, so the denominator is dominated by $1 + \frac{1}{2}\partial_{yy}w$, which is well-conditioned as long as the smile has positive curvature.
