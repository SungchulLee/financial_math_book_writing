# Calibration to Swaption Volatilities

Swaptions are the most liquid volatility instruments for longer-dated interest rate derivatives. The swaption volatility matrix, indexed by expiry and underlying swap tenor, provides a rich calibration target that constrains the mean-reversion parameter $\lambda$ more tightly than caps alone. Under the Hull-White model, European swaptions are priced via Jamshidian's trick, yielding model-implied swaption volatilities that depend on both $\lambda$ and $\sigma$. This section derives the Hull-White swaption volatility formula, describes the structure of the swaption volatility matrix, and presents calibration algorithms for fitting $(\lambda, \sigma)$ to market swaption data.

## Swaption Volatility Matrix

Market swaption volatilities are quoted as a matrix with rows indexed by option expiry $T_0$ and columns indexed by swap tenor $T_n - T_0$:

$$
\begin{array}{c|ccccc}
 & 1\text{Y} & 2\text{Y} & 5\text{Y} & 10\text{Y} & 20\text{Y} \\
\hline
1\text{Y} & \sigma_{1\times1} & \sigma_{1\times2} & \sigma_{1\times5} & \sigma_{1\times10} & \sigma_{1\times20} \\
2\text{Y} & \sigma_{2\times1} & \sigma_{2\times2} & \sigma_{2\times5} & \sigma_{2\times10} & \sigma_{2\times20} \\
5\text{Y} & \sigma_{5\times1} & \sigma_{5\times2} & \sigma_{5\times5} & \sigma_{5\times10} & \sigma_{5\times20} \\
10\text{Y} & \sigma_{10\times1} & \sigma_{10\times2} & \sigma_{10\times5} & \sigma_{10\times10} & \sigma_{10\times20}
\end{array}
$$

Each entry $\sigma_{m \times n}$ is the Black (or normal) volatility for an $m$-year option on an $n$-year swap.

The **co-terminal** swaptions (along the anti-diagonal where $T_0 + \text{tenor} = \text{const}$) are particularly important for Bermudan swaption pricing, as they represent the value of exercise at each possible exercise date.

## Hull-White Swaption Price via Jamshidian

A European payer swaption with expiry $T_0$ on a swap with payment dates $T_1, \ldots, T_n$ and fixed rate $K$ has the payoff

$$
\max\!\left(\sum_{i=1}^{n} c_i\,P(T_0, T_i) - 1,\; 0\right)
$$

where $c_i = K\delta_i$ for $i < n$ and $c_n = 1 + K\delta_n$.

By Jamshidian's trick, since $P(T_0, T_i)$ is a decreasing function of $r_{T_0}$ in the Hull-White model, there exists a unique $r^*$ solving

$$
\sum_{i=1}^{n} c_i\,P(T_0, T_i; r^*) = 1
$$

The swaption decomposes into a portfolio of ZCB options:

$$
V_{\text{swaption}} = \sum_{i=1}^{n} c_i\,\text{Call}(0; T_0, T_i, K_i)
$$

where $K_i = P(T_0, T_i; r^*) = \exp(A(T_0, T_i) + B(T_0, T_i)\,r^*)$ and each call uses the Hull-White ZCB option formula.

## Hull-White Implied Swaption Volatility

The model-implied Black swaption volatility $\sigma_S^{\text{HW}}$ is obtained by inverting Black's formula from the Hull-White swaption price:

$$
V_{\text{swaption}}^{\text{HW}} = A_{\text{mn}}(0)\left[S_0\,N(d_1) - K\,N(d_2)\right]
$$

where $A_{\text{mn}}(0) = \sum_{i=1}^{n} \delta_i\,P(0, T_i)$ is the annuity factor, $S_0$ is the forward swap rate, and

$$
d_{1,2} = \frac{\ln(S_0/K) \pm \frac{1}{2}(\sigma_S^{\text{HW}})^2 T_0}{\sigma_S^{\text{HW}}\sqrt{T_0}}
$$

An approximate closed-form expression for the Hull-White swaption volatility is

$$
(\sigma_S^{\text{HW}})^2 T_0 \approx \sum_{i=1}^{n} \sum_{j=1}^{n} w_i\,w_j\,\sigma^2\,B(T_0, T_i)\,B(T_0, T_j)\,\frac{1 - e^{-2\lambda T_0}}{2\lambda}
$$

where $w_i = c_i P(0, T_i) / \sum_j c_j P(0, T_j)$ are the annuity-weighted portfolio weights and $B(T_0, T_i) = (e^{-\lambda(T_i - T_0)} - 1)/\lambda$.

!!! tip "Role of Mean-Reversion"
    The mean-reversion $\lambda$ controls how swaption volatility varies across the tenor dimension. Higher $\lambda$ causes the bond price volatility $|B(T_0, T_i)|$ to saturate for long tenors, making long-tenor swaption volatilities relatively lower. This is the primary mechanism through which $\lambda$ is identified from the swaption matrix.

## Calibration Objective

The calibration minimizes the weighted squared error across the swaption matrix:

$$
\min_{\lambda, \sigma} \sum_{(m,n) \in \mathcal{S}} w_{mn}\left(\sigma_{m\times n}^{\text{HW}}(\lambda, \sigma) - \sigma_{m\times n}^{\text{market}}\right)^2
$$

where $\mathcal{S}$ is the set of market-quoted swaption expiry-tenor pairs and $w_{mn}$ are weights.

Common weighting schemes include:

- **Uniform weights**: $w_{mn} = 1$ for all $(m,n)$
- **Vega weights**: $w_{mn} = \text{vega}_{mn}$, giving more weight to swaptions with higher sensitivity to volatility
- **Co-terminal weights**: $w_{mn} = 1$ only along the co-terminal diagonal, appropriate when calibrating for Bermudan swaption pricing

## Calibration to Co-Terminal Swaptions

For pricing a Bermudan swaption expiring at $T_1, T_2, \ldots, T_{n-1}$ on an $n$-year swap, the relevant calibration instruments are the co-terminal swaptions: the $(T_1, n-1)$, $(T_2, n-2)$, ..., $(T_{n-1}, 1)$ swaptions, all sharing the terminal date $T_n$.

The calibration to co-terminal swaptions uses

$$
\min_{\lambda, \sigma} \sum_{k=1}^{n-1} w_k\left(\sigma_{k \times (n-k)}^{\text{HW}} - \sigma_{k \times (n-k)}^{\text{market}}\right)^2
$$

Since each co-terminal swaption depends differently on $\lambda$ (through the tenor-dependent bond volatility), the mean-reversion is well-identified from this subset of the matrix.

???+ example "Swaption Calibration"
    ```python
    def main():
        hw = HullWhite(sigma=0.01, lambd=0.05, P=P_market)

        # Co-terminal swaptions: 1x9, 2x8, 3x7, ..., 9x1
        expiries = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        tenors = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        sigma_mkt = [0.22, 0.21, 0.20, 0.19, 0.18, 0.17, 0.16, 0.15, 0.14]

        def objective(params):
            lambd, sigma = params
            hw.lambd = lambd
            hw.sigma = sigma
            errors = []
            for T0, tenor, s_mkt in zip(expiries, tenors, sigma_mkt):
                s_hw = hw.compute_swaption_implied_vol(T0, tenor)
                errors.append(s_hw - s_mkt)
            return np.sum(np.array(errors)**2)

        from scipy.optimize import minimize
        result = minimize(objective, [0.05, 0.01], method='Nelder-Mead')
        print(f"lambda={result.x[0]:.4f}, sigma={result.x[1]:.6f}")
    ```

## Limitations of Two-Parameter Fit

The Hull-White model with constant $\lambda$ and $\sigma$ produces a swaption volatility matrix with a specific structure: volatilities decrease along each row (as tenor increases, for fixed expiry) at a rate controlled by $\lambda$, and vary along each column (as expiry increases, for fixed tenor) at a rate controlled by the interplay of $\lambda$ and $\sigma$.

With only two parameters, the model cannot independently fit each entry of the volatility matrix. Typical misfits include:

- The model overestimates short-expiry/long-tenor volatilities while underestimating long-expiry/short-tenor volatilities, or vice versa
- The model cannot capture the hump in the expiry dimension (volatilities peaking at 2--5 year expiry) observed in some markets

These limitations motivate the use of piecewise constant $\sigma(t)$ (which helps along the expiry dimension) and the two-factor extension (which helps along the tenor dimension).

## Summary

Calibration to swaption volatilities fits the Hull-White parameters $(\lambda, \sigma)$ to the market swaption matrix by minimizing weighted squared errors between model and market implied volatilities. The model swaption price is computed via Jamshidian's trick, decomposing the swaption into ZCB options. The mean-reversion $\lambda$ is primarily identified from the tenor dimension of the matrix, controlling how bond price volatility saturates for long maturities. Co-terminal swaptions are the most important calibration subset for Bermudan swaption pricing. The two-parameter model cannot fit the full matrix, motivating extensions to piecewise constant volatility and multi-factor models.

---

## Exercises

**Exercise 1.** The swaption volatility matrix is indexed by expiry and tenor. Explain the difference between the $5 \times 10$ swaption (5-year expiry, 10-year tenor) and the $10 \times 5$ swaption (10-year expiry, 5-year tenor). Which has higher sensitivity to the mean-reversion parameter $\lambda$, and why?

??? success "Solution to Exercise 1"
    The $5 \times 10$ swaption is a 5-year option on a 10-year swap. At expiry ($T_0 = 5$), the holder enters a swap starting at year 5 and ending at year 15. The underlying swap has payment dates $T_1 = 6, T_2 = 7, \ldots, T_{10} = 15$.

    The $10 \times 5$ swaption is a 10-year option on a 5-year swap. At expiry ($T_0 = 10$), the holder enters a swap starting at year 10 and ending at year 15. The underlying swap has payment dates $T_1 = 11, T_2 = 12, \ldots, T_5 = 15$.

    **Sensitivity to $\lambda$**: The $5 \times 10$ swaption has higher sensitivity to $\lambda$. The mean-reversion parameter controls the bond price volatility through $B(T_0, T_i) = (e^{-\lambda(T_i - T_0)} - 1)/\lambda$. For the $5 \times 10$ swaption, the time differences $T_i - T_0$ range from 1 to 10 years. The function $|B(T_0, T_i)|$ grows with $T_i - T_0$ but saturates at $1/\lambda$ for large values. The long tenor (10 years) means the bond price volatilities span a wide range of maturities, and the rate of saturation (controlled by $\lambda$) significantly affects the swaption volatility.

    For the $10 \times 5$ swaption, the tenor is only 5 years, so $T_i - T_0$ ranges from 1 to 5 years. The function $|B(T_0, T_i)|$ is evaluated over a narrower range and does not reach the saturation region as much. The swaption volatility is therefore less sensitive to changes in $\lambda$.

    In general, swaptions with longer tenors provide more information about $\lambda$ because the exponential decay $e^{-\lambda(T_i - T_0)}$ is more differentiated across the payment dates.

---

**Exercise 2.** For a 10-year Bermudan swaption with annual exercise, identify the co-terminal swaptions that should be used for calibration. Explain why fitting these co-terminal instruments is more important than fitting the entire swaption matrix when the goal is to price the Bermudan.

??? success "Solution to Exercise 2"
    For a 10-year Bermudan swaption with annual exercise dates at $T_1 = 1, T_2 = 2, \ldots, T_9 = 9$, the terminal date is $T_{10} = 10$. The co-terminal swaptions all share this terminal date:

    - $1 \times 9$: 1-year expiry, 9-year swap (swap from year 1 to year 10)
    - $2 \times 8$: 2-year expiry, 8-year swap (swap from year 2 to year 10)
    - $3 \times 7$: 3-year expiry, 7-year swap (swap from year 3 to year 10)
    - $4 \times 6$: 4-year expiry, 6-year swap (swap from year 4 to year 10)
    - $5 \times 5$: 5-year expiry, 5-year swap (swap from year 5 to year 10)
    - $6 \times 4$: 6-year expiry, 4-year swap (swap from year 6 to year 10)
    - $7 \times 3$: 7-year expiry, 3-year swap (swap from year 7 to year 10)
    - $8 \times 2$: 8-year expiry, 2-year swap (swap from year 8 to year 10)
    - $9 \times 1$: 9-year expiry, 1-year swap (swap from year 9 to year 10)

    Co-terminal swaptions are more important than the full matrix because the Bermudan swaption's value at each exercise date $T_k$ is determined by the European swaption on the remaining swap from $T_k$ to $T_{10}$. This is exactly the $k \times (10-k)$ co-terminal swaption. The Bermudan swaption can be viewed as an optimal stopping problem where at each exercise date, the holder compares the exercise value (the intrinsic value of entering the remaining swap) against continuation.

    If the model correctly prices all co-terminal Europeans, it correctly prices the exercise value at each possible exercise date, which is the critical input for the Bermudan valuation. Fitting non-co-terminal swaptions (e.g., $5 \times 2$, which terminates at year 7) is irrelevant because these instruments do not correspond to any exercise decision in the Bermudan. Calibrating to the entire matrix would use the model's limited degrees of freedom to fit instruments that do not affect the Bermudan price, potentially degrading the fit on the instruments that do matter.

---

**Exercise 3.** The approximate Hull-White swaption variance formula involves the sum $\sum_{i,j} w_i w_j \sigma^2 B(T_0, T_i) B(T_0, T_j) \frac{1 - e^{-2\lambda T_0}}{2\lambda}$. Show that this can be written as $\sigma^2 \left(\sum_i w_i B(T_0, T_i)\right)^2 \frac{1 - e^{-2\lambda T_0}}{2\lambda}$ and explain the simplification.

??? success "Solution to Exercise 3"
    The approximate swaption variance formula is

    $$
    (\sigma_S^{\text{HW}})^2 T_0 \approx \sum_{i=1}^{n} \sum_{j=1}^{n} w_i w_j \sigma^2 B(T_0, T_i) B(T_0, T_j) \frac{1 - e^{-2\lambda T_0}}{2\lambda}
    $$

    The key observation is that the factor $\sigma^2 \frac{1 - e^{-2\lambda T_0}}{2\lambda}$ does not depend on the indices $i$ or $j$, so it can be factored out of the double sum:

    $$
    (\sigma_S^{\text{HW}})^2 T_0 \approx \sigma^2 \frac{1 - e^{-2\lambda T_0}}{2\lambda} \sum_{i=1}^{n} \sum_{j=1}^{n} w_i w_j B(T_0, T_i) B(T_0, T_j)
    $$

    The remaining double sum is the square of a single sum:

    $$
    \sum_{i=1}^{n} \sum_{j=1}^{n} w_i w_j B(T_0, T_i) B(T_0, T_j) = \left(\sum_{i=1}^{n} w_i B(T_0, T_i)\right)\left(\sum_{j=1}^{n} w_j B(T_0, T_j)\right) = \left(\sum_{i=1}^{n} w_i B(T_0, T_i)\right)^2
    $$

    This factorization holds because the terms $w_i B(T_0, T_i)$ and $w_j B(T_0, T_j)$ are separable across the two indices. Therefore:

    $$
    (\sigma_S^{\text{HW}})^2 T_0 \approx \sigma^2 \left(\sum_{i=1}^{n} w_i B(T_0, T_i)\right)^2 \frac{1 - e^{-2\lambda T_0}}{2\lambda}
    $$

    The simplification arises from the one-factor structure of the Hull-White model: all bond prices are driven by a single Brownian motion, so their covariance matrix has rank one. In a multi-factor model, the bond volatilities would be vectors, and the double sum would involve inner products $\boldsymbol{B}_i^\top \boldsymbol{B}_j$ that do not factor as a perfect square. The ability to write the swaption variance as a single squared sum times a scalar is a direct consequence of perfect correlation between all bond price movements in the one-factor model.

---

**Exercise 4.** Describe the role of the annuity-weighted portfolio weights $w_i = c_i P(0,T_i) / \sum_j c_j P(0,T_j)$ in the swaption volatility formula. How do these weights change as the swap rate $K$ increases? What happens to the swaption volatility approximation for deep in-the-money versus deep out-of-the-money strikes?

??? success "Solution to Exercise 4"
    The annuity-weighted portfolio weights are

    $$
    w_i = \frac{c_i P(0, T_i)}{\sum_{j=1}^{n} c_j P(0, T_j)}
    $$

    where $c_i = K\delta_i$ for $i < n$ and $c_n = 1 + K\delta_n$. These weights represent the present-value contribution of each cash flow to the total bond portfolio $\sum_i c_i P(0, T_i)$.

    **Role in the volatility formula**: The swaption volatility approximation expresses the swap rate volatility as a weighted average of individual bond price volatilities. The weights $w_i$ determine how much each bond's volatility contributes to the overall swap rate volatility. This is analogous to a portfolio variance formula where the variance of the portfolio return is a weighted sum of individual asset variances (with the simplification to a perfect square due to the one-factor structure).

    **Effect of increasing $K$**: As the fixed rate $K$ increases, all coupon cash flows $c_i = K\delta_i$ increase proportionally, but the principal repayment component of $c_n = 1 + K\delta_n$ becomes relatively less important. For large $K$, the weights $w_i$ become more uniform across all payment dates (since the $K\delta_i$ terms dominate and are all roughly equal). For small $K$, the weight $w_n$ on the final payment (which includes the principal) dominates.

    **Deep in-the-money swaptions** (low $K$): The weights concentrate on the final payment $c_n \approx 1$, making the swaption volatility approximately equal to the volatility of a single zero-coupon bond $P(T_0, T_n)$. The approximation remains accurate because the swap behaves like a zero-coupon bond.

    **Deep out-of-the-money swaptions** (high $K$): The weights spread more evenly across all payment dates. The approximation based on the linear expansion of the swap rate around the forward rate may become less accurate because the higher-order terms in the expansion become more significant. Additionally, for deep OTM options, the price is more sensitive to the tails of the distribution, where the lognormal approximation underlying the formula may break down.

---

**Exercise 5.** The text states that the model overestimates short-expiry/long-tenor volatilities while underestimating long-expiry/short-tenor volatilities (or vice versa). Explain the source of this misfit in terms of the one-factor structure and the specific functional form of $B(T_0, T_i)$.

??? success "Solution to Exercise 5"
    The source of the misfit lies in the one-factor structure and the specific form of $B(T_0, T_i) = (e^{-\lambda(T_i - T_0)} - 1)/\lambda$.

    In the one-factor model, the swaption volatility at expiry $T_0$ for tenor $T_n - T_0$ is determined by:

    $$
    (\sigma_S^{\text{HW}})^2 T_0 \approx \sigma^2 \left(\sum_{i=1}^{n} w_i B(T_0, T_i)\right)^2 \frac{1 - e^{-2\lambda T_0}}{2\lambda}
    $$

    The term $(1 - e^{-2\lambda T_0})/(2\lambda)$ depends only on the expiry $T_0$, producing a specific pattern along each column (increasing, concave function of $T_0$). The squared sum $(\sum_i w_i B(T_0, T_i))^2$ depends on the tenor through $B(T_0, T_i)$, producing a specific pattern along each row (increasing, saturating function of tenor).

    The critical constraint is that **a single $\lambda$ controls both patterns simultaneously**. If the market swaption matrix has a volatility pattern where:

    - Short-expiry swaptions have a steep tenor slope (suggesting high $\lambda$)
    - Long-expiry swaptions have a flatter tenor slope (suggesting low $\lambda$)

    then no single $\lambda$ can fit both. The optimizer compromises, leading to overestimation at short-expiry/long-tenor (where the model's $\lambda$ is too low relative to the market) and underestimation at long-expiry/short-tenor (where the model's $\lambda$ is too high relative to the market), or vice versa.

    Furthermore, the one-factor model implies perfect correlation between all rates, so the swaption volatility is entirely determined by the portfolio's exposure to the single factor. The market swaption matrix reflects imperfect correlations between rates at different tenors, which the one-factor model cannot capture. This is the fundamental reason why the two-factor extension (which introduces decorrelation) dramatically improves the matrix fit.

---

**Exercise 6.** Implement a simple calibration: given co-terminal swaption volatilities $\sigma_{1\times9} = 0.22$, $\sigma_{5\times5} = 0.18$, and $\sigma_{9\times1} = 0.14$, find $(\lambda, \sigma)$ that minimizes the sum of squared errors. Describe your optimization approach and discuss whether three instruments suffice to identify both parameters.

??? success "Solution to Exercise 6"
    **Optimization approach**: With three co-terminal swaption volatilities and two parameters $(\lambda, \sigma)$, we set up the least-squares objective:

    $$
    f(\lambda, \sigma) = (\sigma_{1\times9}^{\text{HW}} - 0.22)^2 + (\sigma_{5\times5}^{\text{HW}} - 0.18)^2 + (\sigma_{9\times1}^{\text{HW}} - 0.14)^2
    $$

    The model swaption volatilities are computed via the approximate formula involving $B(T_0, T_i)$ and the annuity weights.

    A practical optimization approach is:

    1. **Grid search**: Evaluate $f$ on a coarse grid, e.g., $\lambda \in \{0.01, 0.02, \ldots, 0.20\}$ and $\sigma \in \{0.005, 0.006, \ldots, 0.020\}$, to find a good starting point.
    2. **Local optimization**: Starting from the grid minimum, run Nelder-Mead or L-BFGS-B with bounds $\lambda \in (0.001, 1)$, $\sigma \in (0.0001, 0.1)$.

    **Identifiability with three instruments**: Three instruments provide an overconstrained system for two parameters (three equations, two unknowns). This is sufficient to identify both parameters, provided the instruments have different sensitivities to $(\lambda, \sigma)$.

    The three chosen co-terminal swaptions span a wide range of expiry-tenor combinations:

    - $1 \times 9$: short expiry, long tenor --- highly sensitive to $\lambda$ through the 9-year tenor
    - $5 \times 5$: medium expiry, medium tenor --- moderate sensitivity to both parameters
    - $9 \times 1$: long expiry, short tenor --- primarily sensitive to $\sigma$ (short tenor makes $B$ approximately linear in tenor, reducing $\lambda$ sensitivity)

    This diversity ensures that $\lambda$ and $\sigma$ are both well-identified. Two instruments would be the minimum needed (two equations, two unknowns), but with two instruments the system would be exactly determined, offering no redundancy to detect model misfit. Three instruments provide one degree of freedom for model validation: if the residual error is small, the model is adequate; if large, it signals the need for a more flexible model.

---

**Exercise 7.** Compare uniform weighting, vega weighting, and co-terminal weighting for swaption calibration. For pricing a 10-year Bermudan swaption, which weighting scheme is most appropriate? For hedging a portfolio of European swaptions across the matrix, which scheme is preferable?

??? success "Solution to Exercise 7"
    **Uniform weighting** ($w_{mn} = 1$): Treats all swaption expiry-tenor pairs equally. This is appropriate when no particular instrument is more important than another and the goal is to achieve the best overall fit across the matrix. However, it may lead to poor fits for liquid, high-vega instruments if there are many illiquid, low-vega instruments pulling the calibration.

    **Vega weighting** ($w_{mn} = \nu_{mn}$): Weights each instrument by its Black vega. Instruments with higher vega (typically near-the-money, intermediate-expiry swaptions) receive more weight. This is financially motivated: a 1-vol-point error on a high-vega instrument produces a larger dollar pricing error than the same vol error on a low-vega instrument. Vega weighting minimizes the total dollar-weighted pricing error.

    **Co-terminal weighting** ($w_{mn} = 1$ for co-terminal instruments, $0$ otherwise): Concentrates the fit on the anti-diagonal of the swaption matrix where expiry + tenor = constant. This uses only $n-1$ instruments out of the full matrix.

    **For pricing a 10-year Bermudan swaption**: Co-terminal weighting is most appropriate. The Bermudan swaption's value depends on the exercise value at each exercise date, which corresponds to the co-terminal European swaption at that date. Fitting non-co-terminal swaptions is irrelevant and wastes the model's limited degrees of freedom. Using co-terminal weights ensures the model accurately prices the instruments that directly determine the Bermudan's exercise boundary and value.

    **For hedging a portfolio of European swaptions across the matrix**: Vega weighting is preferable. The hedging portfolio contains swaptions at various expiry-tenor points, and the goal is to minimize the total hedging error in dollar terms. Vega weighting ensures that the calibration focuses on instruments where pricing errors translate into the largest P&L impact. Uniform weighting would give disproportionate influence to low-vega swaptions (e.g., very short or very long expiry) that contribute little to the portfolio's risk. Co-terminal weighting would neglect the non-co-terminal swaptions that are actually in the hedging book.
