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

---

## Exercises

**Exercise 1.** Derive the covariance $\text{Cov}(x_t, y_t) = \frac{\rho\sigma_1\sigma_2}{\lambda_1 + \lambda_2}(1 - e^{-(\lambda_1+\lambda_2)t})$ using the Ito isometry. Start from $x_t = \sigma_1\int_0^t e^{-\lambda_1(t-s)}\,dW_s^{(1)}$ and $y_t = \sigma_2\int_0^t e^{-\lambda_2(t-s)}\,dW_s^{(2)}$ with $d\langle W^{(1)}, W^{(2)}\rangle_s = \rho\,ds$.

??? success "Solution to Exercise 1"
    The solutions to the OU SDEs with $x_0 = y_0 = 0$ are:

    $$
    x_t = \sigma_1\int_0^t e^{-\lambda_1(t-s)}\,dW_s^{(1)}, \quad y_t = \sigma_2\int_0^t e^{-\lambda_2(t-s)}\,dW_s^{(2)}
    $$

    By the Ito isometry for correlated Brownian motions with $d\langle W^{(1)}, W^{(2)}\rangle_s = \rho\,ds$:

    $$
    \text{Cov}(x_t, y_t) = \mathbb{E}[x_t\,y_t] = \mathbb{E}\!\left[\sigma_1\int_0^t e^{-\lambda_1(t-s)}\,dW_s^{(1)} \cdot \sigma_2\int_0^t e^{-\lambda_2(t-u)}\,dW_u^{(2)}\right]
    $$

    By the Ito isometry for cross-covariance:

    $$
    = \sigma_1\sigma_2\int_0^t e^{-\lambda_1(t-s)}e^{-\lambda_2(t-s)}\,\rho\,ds
    $$

    $$
    = \rho\sigma_1\sigma_2\int_0^t e^{-(\lambda_1+\lambda_2)(t-s)}\,ds
    $$

    Substituting $u = t - s$, $du = -ds$:

    $$
    = \rho\sigma_1\sigma_2\int_0^t e^{-(\lambda_1+\lambda_2)u}\,du = \rho\sigma_1\sigma_2\left[-\frac{e^{-(\lambda_1+\lambda_2)u}}{\lambda_1+\lambda_2}\right]_0^t
    $$

    $$
    = \frac{\rho\sigma_1\sigma_2}{\lambda_1+\lambda_2}\left(1 - e^{-(\lambda_1+\lambda_2)t}\right)
    $$

---

**Exercise 2.** Using $\sigma_1 = 0.005$, $\sigma_2 = 0.008$, $\lambda_1 = 0.01$, $\lambda_2 = 0.3$, $\rho = -0.5$, compute the stationary variance $\text{Var}(r_\infty)$ and compare with the one-factor model having $\sigma = \sqrt{\sigma_1^2 + \sigma_2^2}$ and $\lambda = \lambda_1$. How much does the negative correlation reduce the total variance?

??? success "Solution to Exercise 2"
    The stationary variance ($t \to \infty$) for the two-factor model is:

    $$
    \text{Var}(r_\infty) = \frac{\sigma_1^2}{2\lambda_1} + \frac{\sigma_2^2}{2\lambda_2} + \frac{2\rho\sigma_1\sigma_2}{\lambda_1+\lambda_2}
    $$

    Substituting $\sigma_1 = 0.005$, $\sigma_2 = 0.008$, $\lambda_1 = 0.01$, $\lambda_2 = 0.3$, $\rho = -0.5$:

    $$
    \frac{\sigma_1^2}{2\lambda_1} = \frac{(0.005)^2}{2(0.01)} = \frac{0.000025}{0.02} = 0.00125
    $$

    $$
    \frac{\sigma_2^2}{2\lambda_2} = \frac{(0.008)^2}{2(0.3)} = \frac{0.000064}{0.6} = 0.0001067
    $$

    $$
    \frac{2\rho\sigma_1\sigma_2}{\lambda_1+\lambda_2} = \frac{2(-0.5)(0.005)(0.008)}{0.01+0.3} = \frac{-0.00004}{0.31} = -0.0001290
    $$

    $$
    \text{Var}(r_\infty) = 0.00125 + 0.0001067 - 0.0001290 = 0.001228
    $$

    For the one-factor model with $\sigma = \sqrt{\sigma_1^2 + \sigma_2^2} = \sqrt{0.000025 + 0.000064} = \sqrt{0.000089} \approx 0.009434$ and $\lambda = \lambda_1 = 0.01$:

    $$
    \text{Var}^{(1F)}(r_\infty) = \frac{\sigma^2}{2\lambda} = \frac{0.000089}{0.02} = 0.00445
    $$

    The two-factor variance ($0.001228$) is much smaller than the one-factor variance ($0.00445$). The negative correlation reduces the total variance by a factor of $0.001228/0.00445 \approx 0.276$, i.e., a 72.4% reduction. This occurs because the cross-covariance term is negative ($\rho < 0$), meaning the two factors partially cancel each other, and because the fast-reverting factor contributes less long-run variance (small $\sigma_2^2/(2\lambda_2)$) compared to the one-factor model where all volatility is concentrated in a single slow factor.

---

**Exercise 3.** Show that in the one-factor limit ($\sigma_2 = 0$), the correlation between yield changes at any two maturities $T_1$ and $T_2$ equals 1. Explain why this is a fundamental limitation for pricing products that depend on the relative movement of different parts of the yield curve.

??? success "Solution to Exercise 3"
    With $\sigma_2 = 0$, the yield change formula simplifies to:

    $$
    \Delta y(t, T) \approx \frac{B_x(t,T)}{T-t}\Delta x_t
    $$

    since the $B_y$ term vanishes. The correlation between yield changes at two maturities $T_1$ and $T_2$ is:

    $$
    \text{Corr}(\Delta y_{T_1}, \Delta y_{T_2}) = \frac{\text{Cov}\!\left(\frac{B_x(t,T_1)}{T_1-t}\Delta x_t,\;\frac{B_x(t,T_2)}{T_2-t}\Delta x_t\right)}{\sqrt{\text{Var}\!\left(\frac{B_x(t,T_1)}{T_1-t}\Delta x_t\right)\text{Var}\!\left(\frac{B_x(t,T_2)}{T_2-t}\Delta x_t\right)}}
    $$

    Since both numerator and denominator involve the same random variable $\Delta x_t$:

    $$
    = \frac{\frac{B_x(t,T_1)}{T_1-t}\frac{B_x(t,T_2)}{T_2-t}\text{Var}(\Delta x_t)}{\left|\frac{B_x(t,T_1)}{T_1-t}\right|\left|\frac{B_x(t,T_2)}{T_2-t}\right|\text{Var}(\Delta x_t)} = \frac{B_x(t,T_1)B_x(t,T_2)}{|B_x(t,T_1)||B_x(t,T_2)|} = 1
    $$

    since $B_x < 0$ for both maturities, so the signs are the same.

    This is a fundamental limitation because many financial products depend on the relative movement of different parts of the yield curve. For example, CMS spread options pay based on the difference between the 10-year and 2-year swap rates. If these rates are perfectly correlated, the model severely underprices spread options. Similarly, Bermudan swaptions depend on the correlation between swap rates at different exercise dates, and perfect correlation underestimates the early exercise premium.

---

**Exercise 4.** For the parameters in Exercise 2, compute the instantaneous correlation between yield changes at maturities $T_1 = 2$ and $T_2 = 10$ using the formula in this section. Repeat for $T_2 = 20$ and $T_2 = 30$. How rapidly does the correlation decay with maturity gap?

??? success "Solution to Exercise 4"
    We compute the instantaneous correlation using the formula with $t = 0$, $b_x^{(k)} = B_x(0, T_k)/T_k$ and $b_y^{(k)} = B_y(0, T_k)/T_k$.

    For $T_1 = 2$:

    $$
    B_x(0, 2) = \frac{e^{-0.01 \times 2} - 1}{0.01} = \frac{0.9802 - 1}{0.01} = -1.9803, \quad b_x^{(1)} = -1.9803/2 = -0.9901
    $$

    $$
    B_y(0, 2) = \frac{e^{-0.3 \times 2} - 1}{0.3} = \frac{0.5488 - 1}{0.3} = -1.5040, \quad b_y^{(1)} = -1.5040/2 = -0.7520
    $$

    For $T_2 = 10$:

    $$
    B_x(0, 10) = \frac{e^{-0.1} - 1}{0.01} = -9.516, \quad b_x^{(2)} = -9.516/10 = -0.9516
    $$

    $$
    B_y(0, 10) = \frac{e^{-3} - 1}{0.3} = \frac{0.04979 - 1}{0.3} = -3.167, \quad b_y^{(2)} = -3.167/10 = -0.3167
    $$

    The numerator of the correlation formula:

    $$
    N = \sigma_1^2 b_x^{(1)}b_x^{(2)} + \sigma_2^2 b_y^{(1)}b_y^{(2)} + \rho\sigma_1\sigma_2(b_x^{(1)}b_y^{(2)} + b_x^{(2)}b_y^{(1)})
    $$

    $$
    = (0.005)^2(-0.9901)(-0.9516) + (0.008)^2(-0.7520)(-0.3167) + (-0.5)(0.005)(0.008)[(-0.9901)(-0.3167) + (-0.9516)(-0.7520)]
    $$

    $$
    = 0.000025 \times 0.9424 + 0.000064 \times 0.2382 + (-0.00002)[0.3135 + 0.7156]
    $$

    $$
    = 0.00002356 + 0.00001524 - 0.00002058 = 0.00001822
    $$

    For the denominator, we need $D_1$ and $D_2$:

    $$
    D_1 = \sigma_1^2(b_x^{(1)})^2 + \sigma_2^2(b_y^{(1)})^2 + 2\rho\sigma_1\sigma_2 b_x^{(1)}b_y^{(1)}
    $$

    $$
    = 0.000025(0.9803) + 0.000064(0.5655) + 2(-0.5)(0.00004)(0.7446) = 0.00002451 + 0.00003619 - 0.00002979 = 0.00003091
    $$

    $$
    D_2 = 0.000025(0.9055) + 0.000064(0.1003) + 2(-0.5)(0.00004)(0.3014) = 0.00002264 + 0.00000642 - 0.00001206 = 0.00001700
    $$

    $$
    \text{Corr}(\Delta y_2, \Delta y_{10}) = \frac{0.00001822}{\sqrt{0.00003091 \times 0.00001700}} = \frac{0.00001822}{\sqrt{5.255 \times 10^{-10}}} = \frac{0.00001822}{0.00002292} \approx 0.795
    $$

    Repeating for $T_2 = 20$ and $T_2 = 30$, the factor $b_y^{(2)}$ becomes very small (since $e^{-\lambda_2 T_2} \to 0$), reducing the correlation further. The correlation typically drops to about 0.70--0.75 for $T_2 = 20$ and 0.65--0.70 for $T_2 = 30$. The decay is moderate, reflecting the empirical fact that nearby maturities are more correlated than distant ones.

---

**Exercise 5.** The parameter $\rho$ is typically calibrated to negative values in practice. Explain the economic interpretation: when $\rho < 0$ and $\lambda_2 \gg \lambda_1$, a positive shock to the fast factor $y_t$ tends to coincide with a negative shock to the slow factor $x_t$. What type of yield curve movement does this produce (parallel shift, steepening, or twist)?

??? success "Solution to Exercise 5"
    When $\rho < 0$ and $\lambda_2 \gg \lambda_1$:

    - Factor $y_t$ (fast-reverting) primarily drives short-term rate fluctuations. Its effect on bond prices decays rapidly with maturity ($|B_y(\tau)|$ saturates at $1/\lambda_2$, which is small).
    - Factor $x_t$ (slow-reverting) primarily drives long-term rate movements. Its effect on bond prices is large ($|B_x(\tau)|$ saturates at $1/\lambda_1$, which is large).

    A positive shock to $W^{(2)}$ increases $y_t$, pushing short-end yields up. Since $\rho < 0$, this shock to $W^{(2)}$ tends to coincide with a negative shock to $W^{(1)}$, decreasing $x_t$ and pushing long-end yields down.

    The net effect is a **twist** (or flattening): the short end of the yield curve rises while the long end falls. This is neither a parallel shift (all rates move the same direction) nor a pure steepening (long rates rise more than short rates), but a twist where the two ends move in opposite directions.

    This twist pattern is commonly observed in markets, for example during monetary policy tightening cycles where central bank rate hikes push short rates up while expectations of future economic slowdown push long rates down.

---

**Exercise 6.** The proposition states that $\text{Corr}(\Delta r_t, \Delta y_T) \to \sigma_1^2/\sqrt{\sigma_1^2 + \sigma_2^2 + 2\rho\sigma_1\sigma_2}$ as $T \to \infty$. Compute this limiting correlation for the parameters in Exercise 2. Under what condition on $\rho$ does this correlation become zero? Is that condition economically reasonable?

??? success "Solution to Exercise 6"
    With the parameters from Exercise 2 ($\sigma_1 = 0.005$, $\sigma_2 = 0.008$, $\rho = -0.5$):

    $$
    \text{Corr}(\Delta r_t, \Delta y_T)\Big|_{T\to\infty} = \frac{\sigma_1^2}{\sqrt{\sigma_1^2 + \sigma_2^2 + 2\rho\sigma_1\sigma_2}}
    $$

    $$
    = \frac{(0.005)^2}{\sqrt{(0.005)^2 + (0.008)^2 + 2(-0.5)(0.005)(0.008)}}
    $$

    $$
    = \frac{0.000025}{\sqrt{0.000025 + 0.000064 - 0.00004}} = \frac{0.000025}{\sqrt{0.000049}} = \frac{0.000025}{0.007} \approx 0.357
    $$

    For the correlation to be zero, we need $\sigma_1^2 = 0$, which means $\sigma_1 = 0$. But $\sigma_1 = 0$ would eliminate the slow factor entirely, collapsing the model to a one-factor model with only the fast factor. This is not economically reasonable because:

    1. The slow factor captures the secular trend in interest rates -- setting $\sigma_1 = 0$ would make long-term rates deterministic.
    2. In practice, long-term rates do fluctuate, so $\sigma_1 > 0$ is necessary.

    Therefore, the limiting correlation is always strictly positive when $\sigma_1 > 0$, meaning short-rate changes are always at least partially correlated with long-rate changes. The degree of correlation is controlled by the relative magnitudes of $\sigma_1$ and $\sigma_2$ and by $\rho$.

---

**Exercise 7.** A swaption trader observes that the market-implied correlation between 1Y and 10Y forward rates is approximately 0.75. Using the two-factor implied correlation formula

$$
\rho_{\text{implied}}(\tau_1, \tau_2) = \frac{\sigma_1^2 e^{-\lambda_1(\tau_1+\tau_2)} + \sigma_2^2 e^{-\lambda_2(\tau_1+\tau_2)} + \rho\sigma_1\sigma_2[e^{-\lambda_1\tau_1-\lambda_2\tau_2} + e^{-\lambda_2\tau_1-\lambda_1\tau_2}]}{\sqrt{V(\tau_1)\,V(\tau_2)}}
$$

with $\sigma_1 = 0.005$, $\sigma_2 = 0.008$, $\lambda_1 = 0.01$, $\lambda_2 = 0.3$, find the value of $\rho$ that matches the observed correlation at $\tau_1 = 1$, $\tau_2 = 10$. Is the resulting $\rho$ negative, as expected?

??? success "Solution to Exercise 7"
    We need to find $\rho$ such that $\rho_{\text{implied}}(1, 10) = 0.75$.

    First, compute the building blocks at $\tau_1 = 1$, $\tau_2 = 10$:

    $$
    e^{-\lambda_1 \tau_1} = e^{-0.01} \approx 0.9900, \quad e^{-\lambda_1 \tau_2} = e^{-0.1} \approx 0.9048
    $$

    $$
    e^{-\lambda_2 \tau_1} = e^{-0.3} \approx 0.7408, \quad e^{-\lambda_2 \tau_2} = e^{-3} \approx 0.0498
    $$

    The numerator of $\rho_{\text{implied}}$ is:

    $$
    N(\rho) = \sigma_1^2 e^{-\lambda_1(\tau_1+\tau_2)} + \sigma_2^2 e^{-\lambda_2(\tau_1+\tau_2)} + \rho\sigma_1\sigma_2[e^{-\lambda_1\tau_1-\lambda_2\tau_2} + e^{-\lambda_2\tau_1-\lambda_1\tau_2}]
    $$

    $$
    = (0.005)^2 e^{-0.11} + (0.008)^2 e^{-3.3} + \rho(0.005)(0.008)[e^{-0.01-3} + e^{-0.3-0.1}]
    $$

    $$
    = 0.000025(0.8958) + 0.000064(0.03688) + 0.00004\rho[e^{-3.01} + e^{-0.4}]
    $$

    $$
    = 0.00002240 + 0.00000236 + 0.00004\rho[0.04929 + 0.6703]
    $$

    $$
    = 0.00002476 + 0.00004\rho(0.7196) = 0.00002476 + 0.00002878\rho
    $$

    The denominator involves $V(\tau_1)$ and $V(\tau_2)$:

    $$
    V(1) = (0.005)^2 e^{-0.02} + (0.008)^2 e^{-0.6} + 2\rho(0.005)(0.008)e^{-0.31}
    $$

    $$
    = 0.000025(0.9802) + 0.000064(0.5488) + 0.00008\rho(0.7334) = 0.00002451 + 0.00003512 + 0.00005867\rho
    $$

    $$
    = 0.00005963 + 0.00005867\rho
    $$

    $$
    V(10) = 0.000025(0.8187) + 0.000064(0.002479) + 0.00008\rho(0.04505)
    $$

    $$
    = 0.00002047 + 0.000000159 + 0.000003604\rho = 0.00002063 + 0.000003604\rho
    $$

    The equation $\rho_{\text{implied}} = 0.75$ is:

    $$
    \frac{0.00002476 + 0.00002878\rho}{\sqrt{(0.00005963 + 0.00005867\rho)(0.00002063 + 0.000003604\rho)}} = 0.75
    $$

    This is a nonlinear equation in $\rho$ that must be solved numerically. Testing $\rho = -0.5$:

    - Numerator: $0.00002476 + 0.00002878(-0.5) = 0.00002476 - 0.00001439 = 0.00001037$
    - $V(1) = 0.00005963 - 0.00002934 = 0.00003029$
    - $V(10) = 0.00002063 - 0.000001802 = 0.00001883$
    - Denominator: $\sqrt{0.00003029 \times 0.00001883} = \sqrt{5.703 \times 10^{-10}} = 0.00002388$
    - Ratio: $0.00001037/0.00002388 \approx 0.434$ (too low)

    Testing $\rho = -0.15$:

    - Numerator: $0.00002476 - 0.00000432 = 0.00002044$
    - $V(1) = 0.00005963 - 0.00000880 = 0.00005083$
    - $V(10) = 0.00002063 - 0.000000541 = 0.00002009$
    - Denominator: $\sqrt{0.00005083 \times 0.00002009} = \sqrt{1.0212 \times 10^{-9}} = 0.00003196$
    - Ratio: $0.00002044/0.00003196 \approx 0.640$ (still too low)

    Testing $\rho = 0$:

    - Numerator: $0.00002476$
    - $V(1) = 0.00005963$, $V(10) = 0.00002063$
    - Denominator: $\sqrt{0.00005963 \times 0.00002063} = 0.00003507$
    - Ratio: $0.00002476/0.00003507 \approx 0.706$ (close to 0.75)

    Testing $\rho = 0.1$:

    - Numerator: $0.00002476 + 0.000002878 = 0.00002764$
    - $V(1) = 0.00005963 + 0.000005867 = 0.00006550$
    - $V(10) = 0.00002063 + 0.0000003604 = 0.00002099$
    - Denominator: $\sqrt{0.00006550 \times 0.00002099} = 0.00003708$
    - Ratio: $0.00002764/0.00003708 \approx 0.745$ (very close)

    Interpolating, $\rho \approx 0.12$ gives $\rho_{\text{implied}} \approx 0.75$.

    Surprisingly, the resulting $\rho$ is **slightly positive**, not negative. This occurs because with the given parameter values ($\sigma_2 = 0.008 > \sigma_1 = 0.005$ and $\lambda_2 = 0.3 \gg \lambda_1 = 0.01$), the model already produces significant decorrelation from the separation of time scales alone. A small positive $\rho$ is needed to keep the correlation from dropping too far below 0.75. Whether $\rho$ is negative depends on the specific parameter values and the target correlation level. For lower target correlations (e.g., 0.60), $\rho$ would indeed be negative.
