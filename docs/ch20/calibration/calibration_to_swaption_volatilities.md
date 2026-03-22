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
