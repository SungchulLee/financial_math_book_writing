# Calibration to Cap Volatilities

Interest rate caps are among the most liquid volatility instruments in the market, making them the primary calibration target for the Hull-White model's volatility parameters. A cap is a portfolio of caplets, and each caplet has a closed-form price under Hull-White. Calibration proceeds by matching model-implied caplet volatilities to market-quoted Black volatilities. Since the Hull-White model has only two volatility parameters ($\lambda$ and $\sigma$), it cannot fit the entire caplet volatility term structure exactly, but it can achieve a best fit in a least-squares sense. This section derives the Hull-White caplet volatility, describes the stripping of cap volatilities into caplet volatilities, and presents the calibration algorithm.

## Market Cap Volatility Conventions

Caps are quoted in terms of flat (or spot) Black volatilities. A cap with maturity $T_n$ and strike $K$ is priced as a sum of caplets, each valued using Black's formula with a single volatility $\sigma_{\text{cap}}(T_n)$:

$$
\text{Cap}(T_n, K) = \sum_{k=1}^{n} \text{Caplet}^{\text{Black}}(T_{k-1}, T_k, K, \sigma_{\text{cap}}(T_n))
$$

The flat volatility $\sigma_{\text{cap}}(T_n)$ is the single number that reproduces the market cap price when applied uniformly to all caplets in the cap.

## Stripping Caplet Volatilities

Individual caplet volatilities $\sigma_k^{\text{cplt}}$ (also called spot or forward volatilities) are more informative for calibration. They are extracted from the cap volatility curve by a bootstrap procedure.

**Algorithm (Cap Vol Stripping).**

1. From the market cap with maturity $T_1$ (a single caplet), read $\sigma_1^{\text{cplt}} = \sigma_{\text{cap}}(T_1)$
2. For $n = 2, 3, \ldots$:
    - Compute the cap price: $\text{Cap}(T_n) = \sum_{k=1}^{n} \text{Caplet}^{\text{Black}}(T_{k-1}, T_k, K, \sigma_{\text{cap}}(T_n))$
    - Subtract the contribution of already-stripped caplets: $\text{Caplet}_n = \text{Cap}(T_n) - \sum_{k=1}^{n-1} \text{Caplet}^{\text{Black}}(T_{k-1}, T_k, K, \sigma_k^{\text{cplt}})$
    - Invert Black's formula to find $\sigma_n^{\text{cplt}}$ from $\text{Caplet}_n$

The result is a term structure of caplet volatilities $\{\sigma_1^{\text{cplt}}, \sigma_2^{\text{cplt}}, \ldots, \sigma_n^{\text{cplt}}\}$.

## Hull-White Caplet Volatility

Recall (see [§ HW Caplet/Floorlet via Bond Option](../derivatives_pricing/caplet_floorlet_formula.md)): a caplet on $L(T_{k-1}, T_k)$ is a put option on the ZCB $P(T_{k-1}, T_k)$, priced by the Hull-White ZCB option formula. The bond price volatility entering that formula is

$$
\sigma_P(T_{k-1}, T_k) = \frac{\sigma}{\lambda}\left(1 - e^{-\lambda\delta_k}\right)\sqrt{\frac{1 - e^{-2\lambda T_{k-1}}}{2\lambda}}
$$

with $\delta_k = T_k - T_{k-1}$.

The implied Black caplet volatility under Hull-White is approximately

$$
\sigma_k^{\text{HW}} \approx \frac{\sigma_P(T_{k-1}, T_k)}{\delta_k\,\ell_k(0)\,\sqrt{T_{k-1}}}
$$

where $\ell_k(0) = \frac{1}{\delta_k}\left(\frac{P(0, T_{k-1})}{P(0, T_k)} - 1\right)$ is the initial forward rate.

!!! tip "Parameter Roles"
    The volatility $\sigma$ scales the overall level of caplet volatilities. The mean-reversion $\lambda$ controls the term structure shape: higher $\lambda$ causes caplet volatilities to decay faster with maturity, producing a downward-sloping volatility curve. With $\lambda = 0$ (Ho-Lee limit), the volatility curve is increasing in $\sqrt{T}$.

## Calibration Objective

The calibration minimizes the weighted sum of squared differences between model and market caplet volatilities:

$$
\min_{\lambda, \sigma} \sum_{k=1}^{n} w_k \left(\sigma_k^{\text{HW}}(\lambda, \sigma) - \sigma_k^{\text{market}}\right)^2
$$

where $w_k$ are weights (typically uniform or vega-weighted).

Alternatively, calibration can target cap prices directly:

$$
\min_{\lambda, \sigma} \sum_{k=1}^{n} w_k \left(\text{Cap}_k^{\text{HW}}(\lambda, \sigma) - \text{Cap}_k^{\text{market}}\right)^2
$$

**Proposition.** For fixed $\lambda$, the optimal $\sigma$ can be found in semi-closed form. The caplet price is linear in $\sigma^2$ (since $\sigma_P$ is linear in $\sigma$), so the sum of squared caplet price errors is a quadratic function of $\sigma^2$, minimized analytically. The outer optimization over $\lambda$ is then a one-dimensional problem.

???+ note "Proof sketch"
    The Hull-White caplet price depends on $\sigma$ only through $\sigma_P$, which is linear in $\sigma$. The Black-Scholes-type formula involves $N(d_\pm)$ where $d_\pm$ depends on $\sigma_P$, so the exact dependence is nonlinear. However, for at-the-money caplets where $d_\pm \approx \pm \sigma_P/2$, the price is approximately $\sigma_P \cdot \phi(0) \approx 0.4\,\sigma_P$, making the price nearly linear in $\sigma$. For exact calibration, numerical optimization over both $\lambda$ and $\sigma$ is needed. $\square$

## Calibration Algorithm

**Algorithm (Two-Parameter Cap Vol Calibration).**

1. **Strip** market cap volatilities into caplet volatilities $\{\sigma_k^{\text{market}}\}$
2. **Initialize**: $\lambda_0 = 0.05$, $\sigma_0 = 0.01$ (typical starting values)
3. **Optimize**: use Levenberg-Marquardt or Nelder-Mead to minimize

$$
f(\lambda, \sigma) = \sum_{k=1}^{n} w_k\left(\sigma_k^{\text{HW}}(\lambda, \sigma) - \sigma_k^{\text{market}}\right)^2
$$

4. **Check**: verify that $\lambda > 0$ and $\sigma > 0$, and that the residuals are acceptable

???+ example "Cap Vol Calibration"
    ```python
    def main():
        hw = HullWhite(sigma=0.01, lambd=0.05, P=P_market)

        # Market caplet volatilities (stripped from cap vols)
        T_reset = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 7.0, 10.0]
        sigma_mkt = [0.25, 0.24, 0.23, 0.22, 0.20, 0.18, 0.17, 0.16]

        # Objective function
        def objective(params):
            lambd, sigma = params
            hw.lambd = lambd
            hw.sigma = sigma
            errors = []
            for T_k, s_mkt in zip(T_reset, sigma_mkt):
                s_hw = hw.compute_implied_caplet_vol(T_k)
                errors.append(s_hw - s_mkt)
            return np.sum(np.array(errors)**2)

        from scipy.optimize import minimize
        result = minimize(objective, [0.05, 0.01], method='Nelder-Mead')
        print(f"Calibrated: lambda={result.x[0]:.4f}, sigma={result.x[1]:.6f}")
    ```

## Piecewise Constant Volatility Extension

When two parameters cannot fit the caplet term structure adequately, a natural extension uses piecewise constant $\sigma(t)$:

$$
\sigma(t) = \sigma_k \quad \text{for } t \in [T_{k-1}, T_k)
$$

With $n$ caplets and $n$ volatility parameters $\{\sigma_1, \ldots, \sigma_n\}$, each caplet can be fitted exactly by a bootstrap procedure:

1. Set $\sigma_1$ to match the first caplet volatility
2. For $k = 2, \ldots, n$: set $\sigma_k$ to match the $k$-th caplet, given $\sigma_1, \ldots, \sigma_{k-1}$ already determined

This produces a piecewise constant volatility function that exactly reproduces all market caplet volatilities.

!!! warning "Stability of Piecewise Calibration"
    The piecewise constant calibration can produce non-smooth or even negative $\sigma_k$ values if the input volatilities are noisy. Regularization (e.g., penalizing large jumps $|\sigma_{k+1} - \sigma_k|$) improves stability. The two-parameter calibration is more robust but less accurate.

## Summary

Calibrating the Hull-White model to cap volatilities involves stripping the cap volatility curve into individual caplet volatilities, computing the model-implied caplet volatility $\sigma_k^{\text{HW}}$ from the bond price volatility formula, and minimizing the weighted squared error. The two parameters $(\lambda, \sigma)$ control the level and slope of the caplet volatility term structure: $\sigma$ sets the overall level and $\lambda$ determines how rapidly volatility decays with maturity. For exact fitting, the piecewise constant $\sigma(t)$ extension matches each caplet individually via bootstrap. The next sections cover calibration to swaption volatilities and joint calibration strategies.

---

## Exercises

**Exercise 1.** Given a 3-year annual cap with flat Black volatility $\sigma_{\text{cap}}(3) = 0.20$ and caplet volatilities $\sigma_1^{\text{cplt}} = 0.22$, $\sigma_2^{\text{cplt}} = 0.21$ already stripped, describe the bootstrap step to extract $\sigma_3^{\text{cplt}}$. Why is this strip procedure sequential rather than simultaneous?

??? success "Solution to Exercise 1"
    The bootstrap step to extract $\sigma_3^{\text{cplt}}$ proceeds as follows:

    1. Compute the total 3-year cap price using the flat volatility:

    $$
    \text{Cap}(3) = \sum_{k=1}^{3} \text{Caplet}^{\text{Black}}(T_{k-1}, T_k, K, \sigma_{\text{cap}}(3) = 0.20)
    $$

    2. Compute the prices of the first two caplets using their already-stripped volatilities:

    $$
    C_1 = \text{Caplet}^{\text{Black}}(T_0, T_1, K, \sigma_1^{\text{cplt}} = 0.22)
    $$

    $$
    C_2 = \text{Caplet}^{\text{Black}}(T_1, T_2, K, \sigma_2^{\text{cplt}} = 0.21)
    $$

    3. Extract the residual third caplet price:

    $$
    C_3 = \text{Cap}(3) - C_1 - C_2
    $$

    4. Invert Black's formula to find $\sigma_3^{\text{cplt}}$ such that $\text{Caplet}^{\text{Black}}(T_2, T_3, K, \sigma_3^{\text{cplt}}) = C_3$.

    The procedure is sequential rather than simultaneous because each step depends on the results of previous steps. To extract caplet $k$, one needs the prices of all earlier caplets $1, \ldots, k-1$, which require knowledge of their individual volatilities $\sigma_1^{\text{cplt}}, \ldots, \sigma_{k-1}^{\text{cplt}}$. A simultaneous approach would require solving a system of nonlinear equations (one per caplet), which is unnecessary since the bootstrap structure makes the problem triangular: each caplet volatility can be determined one at a time in order.

---

**Exercise 2.** The Hull-White bond price volatility for a caplet is $\sigma_P(T_{k-1}, T_k) = \frac{\sigma}{\lambda}(1 - e^{-\lambda\delta_k})\sqrt{\frac{1 - e^{-2\lambda T_{k-1}}}{2\lambda}}$. Show that this formula reduces to $\sigma\delta_k\sqrt{T_{k-1}}$ in the Ho-Lee limit $\lambda \to 0$. What does this imply about the shape of the caplet volatility term structure when mean reversion is absent?

??? success "Solution to Exercise 2"
    We need to show that $\sigma_P(T_{k-1}, T_k) \to \sigma\delta_k\sqrt{T_{k-1}}$ as $\lambda \to 0$. Starting from

    $$
    \sigma_P(T_{k-1}, T_k) = \frac{\sigma}{\lambda}\left(1 - e^{-\lambda\delta_k}\right)\sqrt{\frac{1 - e^{-2\lambda T_{k-1}}}{2\lambda}}
    $$

    we expand each factor using the Taylor series $e^{-x} \approx 1 - x + x^2/2 - \cdots$ for small $x$.

    For the first factor:

    $$
    \frac{1 - e^{-\lambda\delta_k}}{\lambda} = \frac{1 - (1 - \lambda\delta_k + O(\lambda^2))}{\lambda} = \delta_k + O(\lambda)
    $$

    For the second factor:

    $$
    \frac{1 - e^{-2\lambda T_{k-1}}}{2\lambda} = \frac{1 - (1 - 2\lambda T_{k-1} + O(\lambda^2))}{2\lambda} = T_{k-1} + O(\lambda)
    $$

    Combining:

    $$
    \sigma_P(T_{k-1}, T_k) \to \sigma \cdot \delta_k \cdot \sqrt{T_{k-1}} \quad \text{as } \lambda \to 0
    $$

    The implied Black caplet volatility is approximately $\sigma_k^{\text{HW}} \approx \sigma_P / (\delta_k \ell_k(0) \sqrt{T_{k-1}})$. In the Ho-Lee limit, $\sigma_P = \sigma \delta_k \sqrt{T_{k-1}}$, so $\sigma_k^{\text{HW}} \approx \sigma / \ell_k(0)$. Since $\ell_k(0)$ is the forward rate and does not decrease with maturity in typical yield curve environments, the caplet volatility term structure is roughly flat or gently increasing. In particular, the $\sqrt{T_{k-1}}$ dependence in $\sigma_P$ is canceled by the $\sqrt{T_{k-1}}$ in the denominator. Without mean reversion, there is no mechanism to dampen long-dated volatilities, so the volatility curve does not slope downward.

---

**Exercise 3.** For Hull-White parameters $\lambda = 0.05$, $\sigma = 0.01$, and annual resets ($\delta_k = 1$), compute the bond price volatility $\sigma_P(T_{k-1}, T_k)$ for caplets with reset dates $T_{k-1} = 1, 2, 5, 10$ years. Describe how the volatility varies with maturity and explain the role of $\lambda$.

??? success "Solution to Exercise 3"
    Using $\lambda = 0.05$, $\sigma = 0.01$, and $\delta_k = 1$, the formula is

    $$
    \sigma_P(T_{k-1}, T_k) = \frac{0.01}{0.05}\left(1 - e^{-0.05 \cdot 1}\right)\sqrt{\frac{1 - e^{-0.10 \cdot T_{k-1}}}{0.10}}
    $$

    First, compute the common prefactor:

    $$
    \frac{\sigma}{\lambda}(1 - e^{-\lambda\delta_k}) = 0.2 \times (1 - e^{-0.05}) = 0.2 \times 0.04877 = 0.009754
    $$

    For $T_{k-1} = 1$:

    $$
    \sqrt{\frac{1 - e^{-0.10}}{0.10}} = \sqrt{\frac{0.09516}{0.10}} = \sqrt{0.9516} = 0.9755
    $$

    $$
    \sigma_P(1, 2) = 0.009754 \times 0.9755 = 0.009515
    $$

    For $T_{k-1} = 2$:

    $$
    \sqrt{\frac{1 - e^{-0.20}}{0.10}} = \sqrt{\frac{0.18127}{0.10}} = \sqrt{1.8127} = 1.3464
    $$

    $$
    \sigma_P(2, 3) = 0.009754 \times 1.3464 = 0.013133
    $$

    For $T_{k-1} = 5$:

    $$
    \sqrt{\frac{1 - e^{-0.50}}{0.10}} = \sqrt{\frac{0.39347}{0.10}} = \sqrt{3.9347} = 1.9836
    $$

    $$
    \sigma_P(5, 6) = 0.009754 \times 1.9836 = 0.019348
    $$

    For $T_{k-1} = 10$:

    $$
    \sqrt{\frac{1 - e^{-1.0}}{0.10}} = \sqrt{\frac{0.63212}{0.10}} = \sqrt{6.3212} = 2.5142
    $$

    $$
    \sigma_P(10, 11) = 0.009754 \times 2.5142 = 0.024523
    $$

    Summary: $\sigma_P(1,2) \approx 0.0095$, $\sigma_P(2,3) \approx 0.0131$, $\sigma_P(5,6) \approx 0.0194$, $\sigma_P(10,11) \approx 0.0245$.

    The bond price volatility increases with the reset date $T_{k-1}$, but at a decreasing rate. For short maturities, the growth is approximately $\propto \sqrt{T_{k-1}}$ (the Ho-Lee behavior). For long maturities, the growth slows because the factor $(1 - e^{-2\lambda T_{k-1}})/(2\lambda)$ saturates at $1/(2\lambda) = 10$, so $\sigma_P$ approaches the upper bound $0.009754 \times \sqrt{10} = 0.03085$. The mean-reversion parameter $\lambda$ controls this saturation: larger $\lambda$ causes faster saturation and thus a more pronounced flattening of the volatility curve at long maturities.

---

**Exercise 4.** The calibration objective $\min_{\lambda, \sigma}\sum_k w_k(\sigma_k^{\text{HW}} - \sigma_k^{\text{market}})^2$ has two parameters and typically 5--10 calibration instruments. Explain why the problem is overconstrained and describe what the residual errors reveal about the model's limitations.

??? success "Solution to Exercise 4"
    The Hull-White model has two free parameters $(\lambda, \sigma)$, while the calibration typically uses 5--10 caplet volatilities. This means there are more equations (constraints) than unknowns, making the system overconstrained. The least-squares solution minimizes the total squared error but generally cannot make all individual errors zero.

    The residual errors $r_k = \sigma_k^{\text{HW}}(\lambda^*, \sigma^*) - \sigma_k^{\text{market}}$ reveal information about the model's structural limitations:

    1. **Systematic pattern in residuals**: If residuals are positive for short maturities and negative for long maturities (or vice versa), this indicates the model's functional form for the volatility term structure does not match the market shape. The Hull-White model produces a specific monotonic decay pattern controlled by $\lambda$, which cannot capture humps or other non-monotonic features.

    2. **Magnitude of residuals**: Large residuals indicate that the model's two-parameter structure is too restrictive. If residuals are of order 1--2 vol points (e.g., 0.01--0.02 in absolute volatility), this is typical for a two-parameter model. Much larger residuals suggest a fundamental mismatch.

    3. **Random residuals**: If the pattern appears random (no systematic bias), the model's functional form is appropriate but has insufficient flexibility to match noise in the data.

    The overconstrained nature is actually beneficial: with only two parameters, the model is parsimonious, stable, and interpretable. The residuals guide the decision of whether to extend the model (e.g., piecewise constant $\sigma(t)$) or accept the fit as adequate.

---

**Exercise 5.** Explain the proposition that for fixed $\lambda$, the optimal $\sigma$ can be found semi-analytically because the caplet price is approximately linear in $\sigma$. Under what conditions does this approximation break down? How would you implement the resulting one-dimensional outer optimization over $\lambda$?

??? success "Solution to Exercise 5"
    The Hull-White caplet price depends on the bond price volatility $\sigma_P(T_{k-1}, T_k)$, which is linear in $\sigma$:

    $$
    \sigma_P = \frac{\sigma}{\lambda}(1 - e^{-\lambda\delta_k})\sqrt{\frac{1 - e^{-2\lambda T_{k-1}}}{2\lambda}} = \sigma \cdot g(\lambda, T_{k-1}, \delta_k)
    $$

    where $g$ depends only on $\lambda$ and the time parameters. For fixed $\lambda$, the caplet price has the form of a Black-Scholes-type formula with input volatility $\sigma_P$. Near the money, the Black-Scholes price is approximately linear in $\sigma_P$:

    $$
    \text{Caplet} \approx \delta_k P(0, T_k) \cdot \ell_k(0) \cdot \sigma_P \cdot \phi(0) \cdot \sqrt{T_{k-1}} \approx 0.3989 \cdot \delta_k P(0, T_k) \ell_k(0) \sqrt{T_{k-1}} \cdot \sigma_P
    $$

    Since $\sigma_P$ is linear in $\sigma$, the price is approximately linear in $\sigma$, and the squared error is approximately quadratic in $\sigma$. Minimizing a quadratic function has a closed-form solution:

    $$
    \sigma^* = \frac{\sum_k w_k \sigma_k^{\text{market}} / g_k}{\sum_k w_k / g_k^2}
    $$

    (in the simplified linear approximation), reducing the two-dimensional optimization to a one-dimensional search over $\lambda$.

    This approximation breaks down in several cases:

    - **Deep out-of-the-money or in-the-money caplets**: The Black formula is highly nonlinear in $\sigma_P$ away from the money, so the price is no longer linear in $\sigma$.
    - **Very long-dated caplets**: The higher-order terms in the Taylor expansion of $N(d_\pm)$ become significant.
    - **Calibrating to prices rather than volatilities**: When the objective involves prices, the nonlinearity is amplified.

    The one-dimensional outer optimization over $\lambda$ can be implemented using Brent's method (a bracketed root-finding/minimization algorithm that combines bisection, secant, and inverse quadratic interpolation). One brackets $\lambda$ in a reasonable range (e.g., $[0.001, 0.5]$), and for each trial $\lambda$, computes the optimal $\sigma^*(\lambda)$ analytically, then evaluates the resulting error. This is efficient because each function evaluation is cheap (a closed-form $\sigma^*$ plus a sum of squared errors).

---

**Exercise 6.** The piecewise constant $\sigma(t)$ extension can fit each caplet exactly but may produce non-smooth or negative $\sigma_k$ values. Describe a regularization approach that penalizes large jumps $|\sigma_{k+1} - \sigma_k|$ while preserving a good fit. How does this balance accuracy against stability?

??? success "Solution to Exercise 6"
    In the piecewise constant $\sigma(t)$ extension, the volatility function takes values $\sigma_k$ on each interval $[T_{k-1}, T_k)$. The bootstrap determines each $\sigma_k$ sequentially to match the $k$-th caplet exactly. However, noisy market data can cause instability.

    A regularized approach modifies the calibration objective to:

    $$
    \min_{\sigma_1, \ldots, \sigma_n} \sum_{k=1}^{n} \left(\sigma_k^{\text{HW}}(\sigma_1, \ldots, \sigma_k) - \sigma_k^{\text{market}}\right)^2 + \mu \sum_{k=1}^{n-1} (\sigma_{k+1} - \sigma_k)^2
    $$

    The first term measures the fit to market caplet volatilities; the second penalizes jumps between adjacent volatility levels, promoting smoothness.

    Implementation considerations:

    1. **Penalty structure**: The quadratic penalty $(\sigma_{k+1} - \sigma_k)^2$ acts like a spring connecting adjacent values. The total penalty is the sum of squared first differences, analogous to a discrete approximation of $\int |\sigma'(t)|^2\,dt$.

    2. **Choosing $\mu$**: Small $\mu$ gives near-exact fit but potentially noisy $\sigma_k$; large $\mu$ forces near-constant $\sigma(t)$ (recovering the two-parameter model). Cross-validation or the L-curve method can select $\mu$ optimally.

    3. **Optimization**: Unlike the pure bootstrap (which is sequential and exact), the regularized problem requires simultaneous optimization of all $\sigma_k$ values, typically via gradient-based methods (L-BFGS-B with positivity constraints $\sigma_k > 0$).

    4. **Positivity constraint**: Adding the constraint $\sigma_k > 0$ for all $k$ prevents the non-physical negative volatilities that can arise in the unregularized bootstrap.

    The trade-off is: accuracy (fitting each caplet exactly) is sacrificed for stability (a smooth, physically reasonable volatility function). In practice, the regularized fit typically differs from exact caplet prices by only a few basis points, which is within the bid-ask spread of most cap markets, making the loss of accuracy acceptable.

---

**Exercise 7.** Compare cap-based calibration with swaption-based calibration. Which parameter ($\lambda$ or $\sigma$) is better identified by cap data, and why? Under what circumstances would you prefer to calibrate to caps rather than swaptions?

??? success "Solution to Exercise 7"
    **Cap-based calibration** uses caplet volatilities (or equivalently, cap volatilities stripped into caplets) as calibration instruments. Each caplet depends on the short rate volatility over a single forward period.

    **Swaption-based calibration** uses swaption volatilities from the expiry-tenor matrix. Each swaption depends on the short rate volatility integrated over the swap's tenor.

    **Which parameter is better identified:**

    - $\sigma$ is well-identified by cap data because caplet volatilities are approximately proportional to $\sigma$. The relationship $\sigma_k^{\text{HW}} \propto \sigma$ means that the overall level of the caplet term structure directly determines $\sigma$.

    - $\lambda$ is less well-identified by cap data because, for short-dated caplets, the bond price volatility is approximately independent of $\lambda$ (since $(1 - e^{-\lambda\delta_k})/\lambda \approx \delta_k$ for small $\lambda\delta_k$). Only long-dated caplets provide information about $\lambda$, and the sensitivity is relatively weak.

    - In contrast, $\lambda$ is better identified by swaption data because the swaption volatility depends on $B(T_0, T_i) = (e^{-\lambda(T_i - T_0)} - 1)/\lambda$, and the tenor dimension creates strong differentiation in the sensitivity to $\lambda$. Long-tenor swaptions are much more sensitive to $\lambda$ than short-tenor ones, giving the optimizer a strong signal.

    **When to prefer cap calibration:**

    1. When the primary derivatives to be priced are caps, floors, and caplets
    2. When the cap market is more liquid than the swaption market (as in some currencies)
    3. When the model will be used for short-dated products where $\sigma$ matters more than $\lambda$
    4. When a simple, robust calibration is preferred (cap stripping is a well-conditioned bootstrap)
    5. When using the piecewise constant $\sigma(t)$ extension, which can be bootstrapped exactly from caplet data
