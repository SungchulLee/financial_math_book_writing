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

Under the Hull-White model, a caplet with reset date $T_{k-1}$ and payment date $T_k$ is a put option on the zero-coupon bond $P(T_{k-1}, T_k)$. The Hull-White caplet price is given by the ZCB option formula, and the implied Black volatility can be expressed in terms of the model parameters.

The Hull-White bond price volatility for the caplet is

$$
\sigma_P(T_{k-1}, T_k) = \frac{\sigma}{\lambda}\left(1 - e^{-\lambda\delta_k}\right)\sqrt{\frac{1 - e^{-2\lambda T_{k-1}}}{2\lambda}}
$$

where $\delta_k = T_k - T_{k-1}$ is the accrual period.

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
