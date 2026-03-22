# Correlation Between Factors

The two-factor Hull-White model introduces richer dynamics through the interaction of two mean-reverting factors $x_t$ and $y_t$ driven by correlated Brownian motions with instantaneous correlation $\rho$. The correlation parameter controls how the short-rate and long-rate ends of the yield curve move together. Negative $\rho$ produces decorrelation between short and long rates, a feature essential for fitting the swaption volatility matrix. This section derives the correlation structure implied by the two-factor model and connects it to observable yield curve behavior.

## Two-Factor Short Rate Decomposition

Recall that the two-factor Hull-White short rate decomposes as

$$
r_t = x_t + y_t + \varphi(t)
$$

where $x_t$ and $y_t$ are mean-reverting processes:

$$
dx_t = -\lambda_1\,x_t\,dt + \sigma_1\,dW_t^{(1)}, \quad dy_t = -\lambda_2\,y_t\,dt + \sigma_2\,dW_t^{(2)}
$$

with $d\langle W^{(1)}, W^{(2)}\rangle_t = \rho\,dt$, $x_0 = y_0 = 0$.

The factor $x_t$ with smaller $\lambda_1$ reverts slowly and drives long-term rate movements, while $y_t$ with larger $\lambda_2$ reverts quickly and drives short-term fluctuations. The deterministic function $\varphi(t)$ absorbs the initial term structure.

## Variance and Covariance of Factors

Each factor is an Ornstein-Uhlenbeck process with known variance:

$$
\text{Var}(x_t) = \frac{\sigma_1^2}{2\lambda_1}\left(1 - e^{-2\lambda_1 t}\right)
$$

$$
\text{Var}(y_t) = \frac{\sigma_2^2}{2\lambda_2}\left(1 - e^{-2\lambda_2 t}\right)
$$

The cross-covariance between the two factors is

$$
\text{Cov}(x_t, y_t) = \frac{\rho\,\sigma_1\,\sigma_2}{\lambda_1 + \lambda_2}\left(1 - e^{-(\lambda_1 + \lambda_2)t}\right)
$$

???+ note "Proof"
    By the Ito isometry, $\text{Cov}(x_t, y_t) = \sigma_1\sigma_2\int_0^t e^{-\lambda_1(t-s)}e^{-\lambda_2(t-s)}\rho\,ds = \rho\sigma_1\sigma_2\int_0^t e^{-(\lambda_1+\lambda_2)(t-s)}\,ds = \frac{\rho\sigma_1\sigma_2}{\lambda_1+\lambda_2}(1-e^{-(\lambda_1+\lambda_2)t})$. $\square$

## Short Rate Variance

The total variance of the short rate is

$$
\text{Var}(r_t) = \text{Var}(x_t) + \text{Var}(y_t) + 2\,\text{Cov}(x_t, y_t)
$$

$$
= \frac{\sigma_1^2}{2\lambda_1}\left(1 - e^{-2\lambda_1 t}\right) + \frac{\sigma_2^2}{2\lambda_2}\left(1 - e^{-2\lambda_2 t}\right) + \frac{2\rho\,\sigma_1\sigma_2}{\lambda_1+\lambda_2}\left(1 - e^{-(\lambda_1+\lambda_2)t}\right)
$$

As $t \to \infty$, the stationary variance is

$$
\text{Var}(r_\infty) = \frac{\sigma_1^2}{2\lambda_1} + \frac{\sigma_2^2}{2\lambda_2} + \frac{2\rho\,\sigma_1\sigma_2}{\lambda_1+\lambda_2}
$$

For $\rho < 0$, the cross-term reduces the total variance, meaning the two factors partially cancel each other.

## Correlation Between Rate Changes at Different Maturities

The most important correlation structure is between yield changes at different maturities. The yield change at maturity $T$ over a small interval $\Delta t$ is approximately

$$
\Delta y(t, T) \approx \frac{B_x(t,T)}{T-t}\,\Delta x_t + \frac{B_y(t,T)}{T-t}\,\Delta y_t
$$

where $B_x(t,T) = (e^{-\lambda_1(T-t)}-1)/\lambda_1$ and $B_y(t,T) = (e^{-\lambda_2(T-t)}-1)/\lambda_2$.

The instantaneous correlation between yield changes at maturities $T_1$ and $T_2$ is

$$
\text{Corr}(\Delta y_{T_1}, \Delta y_{T_2}) = \frac{\sigma_1^2 b_x^{(1)}b_x^{(2)} + \sigma_2^2 b_y^{(1)}b_y^{(2)} + \rho\sigma_1\sigma_2(b_x^{(1)}b_y^{(2)} + b_x^{(2)}b_y^{(1)})}{\sqrt{[\sigma_1^2(b_x^{(1)})^2 + \sigma_2^2(b_y^{(1)})^2 + 2\rho\sigma_1\sigma_2 b_x^{(1)}b_y^{(1)}][\sigma_1^2(b_x^{(2)})^2 + \sigma_2^2(b_y^{(2)})^2 + 2\rho\sigma_1\sigma_2 b_x^{(2)}b_y^{(2)}]}}
$$

where $b_x^{(k)} = B_x(t, T_k)/(T_k - t)$ and $b_y^{(k)} = B_y(t, T_k)/(T_k - t)$.

!!! tip "One-Factor Limit"
    In the one-factor model ($\sigma_2 = 0$), $\text{Corr}(\Delta y_{T_1}, \Delta y_{T_2}) = 1$ for all $T_1, T_2$. This is the fundamental limitation: the one-factor model produces perfectly correlated yield changes across all maturities. The second factor breaks this perfect correlation.

## Role of the Correlation Parameter

The parameter $\rho$ has a direct economic interpretation:

- **$\rho = 0$**: the two factors are independent. Short-end and long-end yield changes are partially decorrelated, but not negatively correlated
- **$\rho < 0$**: when the first factor increases (pushing yields up), the second factor tends to decrease (pushing short-end yields down), creating a yield curve twist. This is the most common calibrated value
- **$\rho > 0$**: both factors tend to move together, reducing the decorrelation benefit of the second factor

**Proposition.** For $\rho < 0$ and $\lambda_2 \gg \lambda_1$, the correlation between short-rate changes and long-rate changes decreases with the maturity gap:

$$
\text{Corr}(\Delta r_t, \Delta y_{T}) \to \frac{\sigma_1^2}{\sqrt{\sigma_1^2 + \sigma_2^2 + 2\rho\sigma_1\sigma_2}} \quad \text{as } T \to \infty
$$

which is less than $1$ whenever $\sigma_2 > 0$.

## Implied Correlation from Swaptions

The implied correlation between forward rates at different maturities can be inferred from swaption prices. A swaption on a long-tenor swap depends on rate movements across the full tenor range, making it sensitive to the correlation structure.

The two-factor model implies that the correlation between the $\tau_1$-maturity and $\tau_2$-maturity forward rates is

$$
\rho_{\text{implied}}(\tau_1, \tau_2) = \frac{\sigma_1^2 e^{-\lambda_1(\tau_1+\tau_2)} + \sigma_2^2 e^{-\lambda_2(\tau_1+\tau_2)} + \rho\sigma_1\sigma_2[e^{-\lambda_1\tau_1-\lambda_2\tau_2} + e^{-\lambda_2\tau_1-\lambda_1\tau_2}]}{\sqrt{V(\tau_1)\,V(\tau_2)}}
$$

where $V(\tau) = \sigma_1^2 e^{-2\lambda_1\tau} + \sigma_2^2 e^{-2\lambda_2\tau} + 2\rho\sigma_1\sigma_2 e^{-(\lambda_1+\lambda_2)\tau}$ is the instantaneous forward rate variance.

For well-separated maturities ($|\tau_1 - \tau_2| \gg 1/\lambda_2$), the implied correlation decreases, capturing the empirically observed decorrelation between short and long ends of the yield curve.

???+ example "Correlation Structure"
    With $\lambda_1 = 0.01$, $\lambda_2 = 0.3$, $\sigma_1 = 0.005$, $\sigma_2 = 0.008$, $\rho = -0.5$:

    - Corr(1Y, 2Y) $\approx 0.95$: nearby maturities are highly correlated
    - Corr(1Y, 10Y) $\approx 0.75$: moderate decorrelation
    - Corr(1Y, 30Y) $\approx 0.60$: significant decorrelation

    The one-factor model would give Corr $= 1.0$ for all pairs.

## Summary

The correlation parameter $\rho$ in the two-factor Hull-White model controls the decorrelation between yield changes at different maturities. Negative $\rho$ produces the empirically observed pattern where short and long rates do not move in perfect lockstep. The implied correlation decreases with maturity gap, a feature the one-factor model cannot capture (it produces correlation $1$ everywhere). The covariance structure $\text{Cov}(x_t, y_t) = \rho\sigma_1\sigma_2(1-e^{-(\lambda_1+\lambda_2)t})/(\lambda_1+\lambda_2)$ determines the cross-maturity correlation structure, which is the primary diagnostic for the two-factor model's added value over its one-factor counterpart.
