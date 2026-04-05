# Noise Amplification and Smoothing


Local volatility calibration is notoriously sensitive because the Dupire inversion uses **second derivatives in strike** and **first derivatives in maturity**. Differentiation amplifies noise, so smoothing is not optional—it is the core of a stable pipeline.

---

## Why differentiation amplifies noise


Suppose market call prices are observed with noise:

\[
C^{\text{obs}}(K,T) = C^{\star}(K,T) + \varepsilon(K,T).
\]



Finite differences approximate derivatives, e.g.

\[
\partial_{KK}C(K,T) \approx \frac{C(K+h,T)-2C(K,T)+C(K-h,T)}{h^2}.
\]



The division by \(h^2\) means:
- as you refine the grid (smaller \(h\)),
- noise \(\varepsilon\) is magnified like \(1/h^2\).

Thus, “more data points” can paradoxically make the raw Dupire estimate *worse* unless smoothing increases as resolution increases.

---

## Smoothing as regularization


Instead of differentiating raw quotes, one typically:

1. constructs a smooth surface \(\tilde C(K,T)\) (or \(\tilde\sigma_{\text{impl}}(K,T)\)),
2. applies Dupire differentiation to the smooth surface.

This is a form of **regularization**: you restrict attention to smooth surfaces compatible with data.

Common smoothing approaches:

- **Spline fits** per maturity (in strike or log-moneyness)
- **SVI** or other parametric smiles
- **Kernel regression / local polynomials**
- **Penalized least squares** with roughness penalty:

  \[
  \min \sum_j w_j(\tilde C_j - C^{\text{obs}}_j)^2 + \lambda \int |\partial_{KK}\tilde C|^2
  \]



---

## Arbitrage-aware smoothing


Smoothing must respect no-arbitrage conditions, otherwise the denominator \(\partial_{KK}C\) can become negative or near-zero, producing unstable or imaginary local vol.

Useful constraints include:

- **monotonicity in strike:** \(\partial_K C \le 0\),
- **convexity in strike:** \(\partial_{KK} C \ge 0\),
- **calendar monotonicity:** call price should not decrease with maturity (under standard assumptions).

In practice:
- remove violations before smoothing,
- fit a constrained surface,
- or adjust bid/ask bands until constraints are satisfied.

---

## Smoothing in total variance coordinates


A common stabilization trick is to smooth **total implied variance**

\[
w(k,T) = T\sigma_{\text{impl}}^2(k,T),
\quad k=\log(K/F_T),
\]


because \(w\) behaves more linearly across \(T\) and facilitates calendar-arbitrage checks.

One can:
- fit \(w(k,T)\) smoothly in both directions,
- compute model-consistent prices from the fitted \(w\),
- then apply Dupire.

---

## Practical pipeline (robust version)


1. convert raw quotes to consistent coordinates (forward, discounting, log-moneyness),
2. filter illiquid/outlier points,
3. build an arbitrage-clean surface in implied vol or total variance,
4. compute a smooth call surface,
5. apply Dupire with stable numerical differentiation,
6. post-smooth local vol if needed (mildly) to remove residual roughness.

---

## Key takeaways


- Dupire inversion is derivative-heavy; noise is amplified strongly.
- Smoothing is a *regularization step*, not cosmetic.
- Arbitrage-aware smoothing is critical to keep \(\partial_{KK}C\ge 0\).
- Total variance coordinates often improve stability.

---

## Further reading


- Gatheral, *The Volatility Surface*.
- Fengler, *Semiparametric Modeling of Implied Volatility*.
- Andersen & Piterbarg (practical surface construction and stability).

---

## Exercises

**Exercise 1.** Let $\varepsilon_i \sim N(0, \delta^2)$ be independent noise on observed call prices at equally spaced strikes with spacing $h$. Show that the central finite-difference approximation to $\partial_{KK}C$ at a point has variance $6\delta^2/h^4$. If bid-ask noise is $\delta = 0.05$ and strike spacing is $h = 5$, compute the standard deviation of the estimated second derivative.

??? success "Solution to Exercise 1"
    The central finite-difference approximation to $\partial_{KK}C$ is

    $$
    \widehat{\partial_{KK}C} = \frac{\hat{C}(K+h) - 2\hat{C}(K) + \hat{C}(K-h)}{h^2}
    $$

    where $\hat{C}(K_i) = C(K_i) + \varepsilon_i$ and $\varepsilon_i \sim N(0, \delta^2)$ independently. The noise contribution is

    $$
    Z = \frac{\varepsilon_{+} - 2\varepsilon_0 + \varepsilon_{-}}{h^2}
    $$

    Since the $\varepsilon_i$ are independent, the variance of the linear combination in the numerator is

    $$
    \operatorname{Var}(\varepsilon_{+} - 2\varepsilon_0 + \varepsilon_{-}) = 1^2\delta^2 + (-2)^2\delta^2 + 1^2\delta^2 = 6\delta^2
    $$

    Dividing by $h^2$ in the denominator squares to $h^4$, so

    $$
    \operatorname{Var}(Z) = \frac{6\delta^2}{h^4}
    $$

    **Numerical computation:** With $\delta = 0.05$ and $h = 5$:

    $$
    \operatorname{Var}(Z) = \frac{6 \times (0.05)^2}{5^4} = \frac{6 \times 0.0025}{625} = \frac{0.015}{625} = 2.4 \times 10^{-5}
    $$

    The standard deviation is

    $$
    \operatorname{SD}(Z) = \sqrt{2.4 \times 10^{-5}} \approx 0.0049
    $$

    To put this in context, for a typical ATM option with $S_0 = 100$, the true value of $\partial_{KK}C$ is on the order of $e^{-rT}\phi(d_2)/(K\sigma\sqrt{T})$, which for $\sigma = 0.20$, $T = 0.5$ is roughly $0.02$. A standard deviation of $0.005$ represents about 25% relative noise---significant, but manageable with this particular strike spacing.

---

**Exercise 2.** A practitioner uses a cubic spline to smooth call prices across 15 strikes before applying the Dupire formula. The spline is fit by minimizing

$$
\sum_{j=1}^{15} w_j \bigl(\tilde{C}(K_j) - C_j^{\text{obs}}\bigr)^2 + \lambda \int_{K_{\min}}^{K_{\max}} \bigl(\tilde{C}''(K)\bigr)^2 \, dK
$$

Explain the role of the penalty parameter $\lambda$. What happens to the local volatility surface as $\lambda \to 0$? As $\lambda \to \infty$?

??? success "Solution to Exercise 2"
    The smoothing spline minimizes the penalized objective

    $$
    \sum_{j=1}^{15} w_j \bigl(\tilde{C}(K_j) - C_j^{\text{obs}}\bigr)^2 + \lambda \int_{K_{\min}}^{K_{\max}} \bigl(\tilde{C}''(K)\bigr)^2 \, dK
    $$

    The parameter $\lambda$ controls the trade-off between **fidelity to data** (first term) and **smoothness** (second term). The roughness penalty $\int (\tilde{C}'')^2\,dK$ measures the total curvature of the fitted surface.

    **As $\lambda \to 0$:** The penalty term becomes negligible, so the objective reduces to a pure least-squares interpolation problem. The spline will pass exactly through (or very close to) all data points. If the data contain noise, the spline will oscillate to match each noisy observation, producing wild oscillations in $\tilde{C}''(K)$. Since $\partial_{KK}C$ is the key input to Dupire's formula, these oscillations translate directly into a highly unstable, spiky local volatility surface. The local vol may even become negative where spurious concavity violations appear.

    **As $\lambda \to \infty$:** The penalty dominates, forcing $\tilde{C}''(K) \to 0$ everywhere. The only function with zero second derivative is a straight line (affine function): $\tilde{C}(K) = \alpha + \beta K$. This produces $\partial_{KK}\tilde{C} = 0$, which makes the Dupire denominator zero and the local variance undefined. The fit completely ignores the data, losing all information about the smile shape.

    **Optimal choice of $\lambda$:** The ideal $\lambda$ produces a smooth surface that captures the genuine shape of the smile while filtering out noise. In practice, $\lambda$ is chosen by:

    - **Cross-validation:** Leave out one data point at a time, fit to the remaining 14, and choose $\lambda$ minimizing prediction error at the held-out point.
    - **Generalized cross-validation (GCV):** An efficient approximation to leave-one-out CV.
    - **L-curve method:** Plot the data misfit versus the roughness penalty for varying $\lambda$; the optimal $\lambda$ is at the "corner" of the resulting L-shaped curve.

    The local volatility surface will be meaningful only for an intermediate $\lambda$ that yields a positive, smooth $\partial_{KK}\tilde{C}$.

---

**Exercise 3.** Given three call prices at strikes $K-h$, $K$, $K+h$ for a fixed maturity, and call prices at the same strike $K$ for maturities $T$ and $T + \Delta T$, write down the finite-difference approximations for $\partial_{KK}C(K,T)$ and $\partial_T C(K,T)$. Then express the Dupire local variance estimate $\hat{\sigma}_{\text{loc}}^2(T,K)$ in terms of these five market prices, $r$, $q$, $h$, and $\Delta T$.

??? success "Solution to Exercise 3"
    **Finite-difference approximation for $\partial_{KK}C(K,T)$:** Using central differences with strike spacing $h$:

    $$
    \partial_{KK}C(K,T) \approx \frac{C(K+h,T) - 2C(K,T) + C(K-h,T)}{h^2}
    $$

    **Finite-difference approximation for $\partial_T C(K,T)$:** Using a forward difference with time step $\Delta T$:

    $$
    \partial_T C(K,T) \approx \frac{C(K, T+\Delta T) - C(K,T)}{\Delta T}
    $$

    **First derivative $\partial_K C(K,T)$:** Using central differences:

    $$
    \partial_K C(K,T) \approx \frac{C(K+h,T) - C(K-h,T)}{2h}
    $$

    **Dupire local variance estimate:** Substituting into the Dupire formula $\sigma_{\text{loc}}^2 = 2({\partial_T C + (r-q)K\partial_K C - qC})/({K^2\partial_{KK}C})$:

    $$
    \hat{\sigma}_{\text{loc}}^2(T,K) = \frac{2\left(\dfrac{C(K,T+\Delta T)-C(K,T)}{\Delta T} + (r-q)K\,\dfrac{C(K+h,T)-C(K-h,T)}{2h} - qC(K,T)\right)}{K^2\,\dfrac{C(K+h,T)-2C(K,T)+C(K-h,T)}{h^2}}
    $$

    Simplifying:

    $$
    \hat{\sigma}_{\text{loc}}^2(T,K) = \frac{2h^2\left(\dfrac{C(K,T+\Delta T)-C(K,T)}{\Delta T} + \dfrac{(r-q)K}{2h}\bigl(C(K+h,T)-C(K-h,T)\bigr) - qC(K,T)\right)}{K^2\bigl(C(K+h,T)-2C(K,T)+C(K-h,T)\bigr)}
    $$

    The **five required market prices** are:

    - $C(K-h, T)$, $C(K, T)$, $C(K+h, T)$ — same maturity, three strikes
    - $C(K, T+\Delta T)$ — same strike, next maturity
    - (The fifth is $C(K, T)$ itself, which appears in multiple terms)

    So four distinct market quotes are needed: $C(K-h,T)$, $C(K,T)$, $C(K+h,T)$, and $C(K,T+\Delta T)$.

---

**Exercise 4.** The no-arbitrage convexity condition requires $\partial_{KK}C \ge 0$. Construct a numerical example with three call prices at strikes $K \in \{90, 100, 110\}$ where the butterfly spread is negative (i.e., $C(90) - 2C(100) + C(110) < 0$). Show that the Dupire formula yields $\sigma_{\text{loc}}^2 < 0$ at this point. Describe how you would correct this violation in practice.

??? success "Solution to Exercise 4"
    **Constructing the example:** Consider European call prices at strikes $K \in \{90, 100, 110\}$ for some fixed maturity. We need $C(90) - 2C(100) + C(110) < 0$.

    Suppose $S_0 = 100$, $r = 0.03$, $q = 0$, $T = 0.5$. Normal Black--Scholes prices with $\sigma = 0.20$ would give approximately: $C(90) \approx 14.15$, $C(100) \approx 6.89$, $C(110) \approx 2.52$.

    The butterfly spread is $14.15 - 2(6.89) + 2.52 = 2.89 > 0$ (no violation).

    Now introduce a data error: suppose a quote error inflates $C(100)$ to $C(100) = 8.50$ while the wing quotes remain the same. Then:

    $$
    C(90) - 2C(100) + C(110) = 14.15 - 2(8.50) + 2.52 = 14.15 - 17.00 + 2.52 = -0.33 < 0
    $$

    The butterfly spread is negative, violating convexity.

    **Dupire formula gives negative local variance:** Using $h = 10$ and the simplified Dupire formula with $r = q = 0$ (and assuming $\partial_T C = 3.0$ for illustration):

    $$
    \partial_{KK}C(100) \approx \frac{-0.33}{100} = -0.0033
    $$

    $$
    \sigma_{\text{loc}}^2(T, 100) = \frac{2 \times 3.0}{100^2 \times (-0.0033)} = \frac{6.0}{-33} \approx -0.182
    $$

    This is negative, confirming that the Dupire formula yields $\sigma_{\text{loc}}^2 < 0$.

    **Practical correction:** Several approaches can restore the convexity condition:

    1. **Bid-ask adjustment:** Allow the offending quote $C(100)$ to move within its bid-ask spread. If the bid-ask is, say, $[8.30, 8.70]$, any value below $8.335 = (14.15 + 2.52)/2$ restores the butterfly condition.

    2. **Constrained re-interpolation:** Fit a smooth curve through the call prices subject to the constraint $\tilde{C}''(K) \ge 0$. This is a convex optimization problem (quadratic objective with linear constraints).

    3. **Parametric fitting:** Use an SVI or similar parametric model that guarantees convexity by construction.

    4. **Variance reduction:** Average multiple snapshots of the quote over a short window, reducing the probability of transient violations.

---

**Exercise 5.** Explain why working in total implied variance coordinates $w(k, T) = T\sigma_{\text{impl}}^2(k, T)$ with $k = \ln(K/F_T)$ facilitates calendar-arbitrage checking. Specifically, show that the condition $\partial_T w(k, T) \ge 0$ for fixed $k$ is necessary for absence of calendar arbitrage, and relate this to the positivity of the numerator in the Dupire formula.

??? success "Solution to Exercise 5"
    **Calendar arbitrage and total variance:** A calendar spread involves selling a shorter-dated option and buying a longer-dated option at the same strike. Under no-arbitrage, the longer-dated option must be at least as expensive: $C(K, T_2) \ge C(K, T_1)$ for $T_2 > T_1$ (assuming $q = 0$; for $q > 0$ the condition is on forward prices).

    In total implied variance coordinates $w(k, T) = T\sigma_{\text{impl}}^2(k, T)$, this monotonicity condition becomes $\partial_T w(k, T) \ge 0$ for fixed log-moneyness $k$. To see this, note that Black--Scholes call prices (expressed in forward moneyness) depend on implied vol only through total variance $w$. Since the Black--Scholes price is increasing in $w$ (positive vega), $C(k, T_2) \ge C(k, T_1)$ requires $w(k, T_2) \ge w(k, T_1)$, i.e., $\partial_T w \ge 0$.

    **Connection to Dupire numerator:** In the Dupire formula expressed in total variance coordinates:

    $$
    \sigma_{\text{loc}}^2 = \frac{\partial_T w}{\text{denominator}}
    $$

    The denominator is positive when butterfly arbitrage is absent (as shown by the $g(k) \ge 0$ condition). Therefore, $\sigma_{\text{loc}}^2 \ge 0$ requires $\partial_T w \ge 0$, which is exactly the calendar no-arbitrage condition.

    If $\partial_T w < 0$ at some $(k_0, T_0)$, the numerator is negative while the denominator (assuming no butterfly arbitrage) is positive, giving $\sigma_{\text{loc}}^2 < 0$---an unphysical result that signals calendar arbitrage.

    **Why total variance coordinates facilitate checking:** In $(k, T)$ coordinates, calendar arbitrage reduces to a simple monotonicity check: for each fixed $k$, verify that $w(k, T)$ is non-decreasing in $T$. This is straightforward to verify numerically: at each log-moneyness grid point, check $w(k, T_{i+1}) \ge w(k, T_i)$.

    By contrast, checking calendar arbitrage directly in call price space requires accounting for discounting, forward prices, and the non-trivial relationship between prices and maturities. The total variance formulation strips away these complications.

---

**Exercise 6.** Compare two smoothing approaches for a set of 50 option quotes across 5 maturities: (a) independent cubic spline per maturity, and (b) joint SVI parameterization across all maturities. Discuss which approach is more likely to satisfy calendar-spread arbitrage constraints and why. What additional steps are needed for approach (a) to ensure time-consistency?

??? success "Solution to Exercise 6"
    **(a) Independent cubic spline per maturity:**

    - **Advantages:** Simple, flexible, can fit each slice well.
    - **Disadvantages:** Each maturity is treated independently, so there is no mechanism to enforce consistency across maturities. The spline at $T_2$ has no knowledge of the spline at $T_1$, so calendar arbitrage $w(k, T_2) \ge w(k, T_1)$ is not guaranteed.

    Even if each individual slice is butterfly-arbitrage-free (convex in $K$), two independently fitted slices can easily cross: one maturity may have higher implied vol in the wings while another has higher vol near ATM, leading to $w(k, T_2) < w(k, T_1)$ for some $k$.

    **(b) Joint SVI parameterization (SSVI):**

    - **Advantages:** By parameterizing the entire surface jointly, SSVI can enforce calendar monotonicity by construction. The SSVI formula $w(k, \theta_T) = \frac{\theta_T}{2}(1 + \rho\phi(\theta_T)k + \sqrt{(\phi(\theta_T)k + \rho)^2 + 1 - \rho^2})$ depends on $T$ only through $\theta_T$. Since $\theta_T$ is a non-decreasing function of $T$ (ATM total variance grows with maturity) and the formula is increasing in $\theta_T$ for reasonable parameter choices, calendar arbitrage is automatically avoided.
    - **Disadvantages:** Less flexible per-slice; may not fit each maturity as precisely. The parametric form may not capture all market smile features.

    **Approach (b) is more likely to satisfy calendar-spread arbitrage constraints** because the cross-maturity structure is built into the parameterization.

    **Additional steps for approach (a):** To ensure time-consistency with independent splines, one must:

    1. **Post-fitting monotonicity check:** At each $k$ grid point, verify $w(k, T_{i+1}) \ge w(k, T_i)$ for consecutive maturities.
    2. **Iterative adjustment:** If violations are found, adjust the offending spline coefficients. This can be done by solving a constrained optimization that minimizes the change to each spline while imposing $w(k, T_{i+1}) \ge w(k, T_i)$ pointwise.
    3. **Sequential fitting:** Fit maturities in order from shortest to longest, constraining each new slice to lie above the previous one at all $k$ values.
    4. **Interpolation in $T$:** After fitting individual slices, interpolate in $T$ using a monotone interpolation scheme (e.g., monotone piecewise cubic Hermite) applied pointwise at each $k$.

---

**Exercise 7.** Consider the penalized least-squares problem with a roughness penalty in both strike and maturity directions:

$$
\min_{\tilde{C}} \sum_j w_j\bigl(\tilde{C}_j - C_j^{\text{obs}}\bigr)^2 + \lambda_K \int (\partial_{KK}\tilde{C})^2 \, dK + \lambda_T \int (\partial_T \tilde{C})^2 \, dT
$$

Discuss why $\lambda_K$ and $\lambda_T$ may need to be chosen differently. If strikes are densely sampled but maturities are sparse, which penalty should be larger and why?

??? success "Solution to Exercise 7"
    The penalized least-squares problem is

    $$
    \min_{\tilde{C}} \sum_j w_j\bigl(\tilde{C}_j - C_j^{\text{obs}}\bigr)^2 + \lambda_K \int (\partial_{KK}\tilde{C})^2 \, dK + \lambda_T \int (\partial_T \tilde{C})^2 \, dT
    $$

    **Why $\lambda_K$ and $\lambda_T$ should differ:**

    The two penalty parameters regularize different directions of the surface, and the appropriate level of smoothing depends on the data density and noise structure in each direction.

    - **Strike direction:** Strikes are typically densely sampled (e.g., 10--30 strikes per maturity). Dense sampling means finite-difference estimates of $\partial_{KK}\tilde{C}$ are noisier (since $h$ is small, and noise amplification scales as $1/h^4$ for the second derivative). However, the dense data also provide more information to constrain the fit, so moderate smoothing suffices.

    - **Maturity direction:** Maturities are usually sparse (e.g., 5--10 standard expiries). The time derivative $\partial_T \tilde{C}$ is estimated with large step sizes, so noise amplification is less severe, but there is little data to constrain the fit, and the surface can vary wildly between maturities without being corrected by observations.

    **When strikes are dense but maturities are sparse:**

    $\lambda_T$ should be **larger** than $\lambda_K$. The reasoning is:

    1. **Sparse maturities require more regularization** because the data alone are insufficient to constrain the surface between observed maturities. Without a strong penalty on $\partial_T \tilde{C}$, the optimizer can introduce arbitrary oscillations in the time direction that are unconstrained by data.

    2. **Dense strikes provide natural regularization** through the sheer number of data points. The data term $\sum_j w_j(\tilde{C}_j - C_j^{\text{obs}})^2$ already constrains the strike-direction behavior at many points, so $\lambda_K$ can be smaller.

    3. **Dupire sensitivity:** The numerator of Dupire's formula involves $\partial_T C$, which is directly affected by the maturity smoothing. An unstable $\partial_T C$ estimate from sparse maturities propagates directly into local variance, so heavier time smoothing protects the calibration output.

    In practice, one might choose $\lambda_T / \lambda_K \sim (\Delta T / \Delta K)^2$ or similar scaling to account for the different sampling densities, and then fine-tune via cross-validation or the L-curve method applied to each direction.
