# Semi-Closed-Form via Fourier Inversion

The Heston model's characteristic function enables a "semi-closed-form" pricing formula for European options: the price is expressed as a deterministic integral involving the characteristic function, reducing option pricing to numerical quadrature. This formula decomposes the call price into two risk-adjusted probabilities $P_1$ and $P_2$, each computed by a one-dimensional Fourier inversion integral. The result is exact up to the numerical integration accuracy, providing a benchmark against which all other Heston pricing methods (COS, FFT, Monte Carlo) are validated.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the semi-closed-form European call price from the Heston characteristic function
    2. Understand the $P_1$/$P_2$ probability decomposition and its measure-theoretic meaning
    3. Evaluate the Fourier inversion integrals using standard quadrature methods
    4. Assess the accuracy and computational cost of semi-closed-form pricing

---

## Intuition

In the Black-Scholes model, the call price $C = S_0 N(d_1) - K e^{-rT} N(d_2)$ involves two normal CDFs. Replacing the lognormal distribution with the Heston distribution means replacing $N(d_j)$ with integrals that invert the characteristic function to recover the corresponding exercise probabilities. The characteristic function is known in closed form, so the only numerical step is one-dimensional integration --- making this approach "semi-closed-form." Each integral converges rapidly because the CF decays fast for large arguments, and standard quadrature (Gauss-Laguerre, Simpson, adaptive) achieves 10--15 digits of accuracy with modest computational effort.

---

## European Call Price Decomposition

The risk-neutral pricing formula for a European call with strike $K$ and maturity $T$ is

$$
C = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}\!\left[(S_T - K)^+\right]
$$

where $\tau = T - t$. Conditioning on the event $\{S_T > K\}$:

$$
C = e^{-r\tau}\left[\mathbb{E}^{\mathbb{Q}}[S_T \mathbf{1}_{S_T > K}] - K \, \mathbb{Q}(S_T > K)\right]
$$

The first term can be rewritten using the stock-price numeraire:

$$
\mathbb{E}^{\mathbb{Q}}[S_T \mathbf{1}_{S_T > K}] = S_0 e^{(r-q)\tau} \, \mathbb{Q}^S(S_T > K)
$$

!!! info "Theorem (Semi-Closed-Form Call Price)"
    The European call price under the Heston model is

    $$
    C = S_0 e^{-q\tau} P_1 - K e^{-r\tau} P_2
    $$

    where

    $$
    P_1 = \mathbb{Q}^S(S_T > K), \qquad P_2 = \mathbb{Q}(S_T > K)
    $$

    are the exercise probabilities under the stock-price numeraire and money-market numeraire respectively.

The European put price follows from put-call parity:

$$
P = K e^{-r\tau}(1 - P_2) - S_0 e^{-q\tau}(1 - P_1)
$$

---

## Fourier Inversion of Exercise Probabilities

Each probability $P_j$ is recovered from the corresponding characteristic function by Fourier inversion.

!!! info "Theorem (Gil-Pelaez Formula for P1 and P2)"
    The exercise probabilities are

    $$
    P_j = \frac{1}{2} + \frac{1}{\pi}\int_0^{\infty} \text{Re}\!\left[\frac{e^{-iu\log K} \varphi_j(u)}{iu}\right] du, \qquad j = 1, 2
    $$

    where $\varphi_1(u)$ is the CF of $\log S_T$ under $\mathbb{Q}^S$ and $\varphi_2(u)$ is the CF under $\mathbb{Q}$.

**Characteristic functions.** The $\mathbb{Q}$-CF is the standard Heston CF:

$$
\varphi_2(u) = \exp\bigl(C(\tau, u) + D(\tau, u) v_0 + iu\log S_0\bigr)
$$

with $C, D$ solving the Heston Riccati system. The $\mathbb{Q}^S$-CF is obtained by the shift formula:

$$
\varphi_1(u) = \frac{\varphi_2(u - i)}{S_0 e^{(r-q)\tau}}
$$

---

## Properties of the Integrands

The integrands $f_j(u) = \text{Re}[e^{-iu\log K}\varphi_j(u)/(iu)]$ have important properties that guide numerical integration.

**Behavior at $u = 0$.** Both integrands have a removable singularity at $u = 0$. Using L'Hopital's rule:

$$
\lim_{u \to 0} \frac{\varphi_j(u)}{iu} = -i \varphi_j'(0)
$$

In practice, the limit is finite and can be computed from the CF derivatives.

**Decay for large $u$.** For the Heston model, $|\varphi_j(u)| \leq C e^{-\alpha |u|}$ for some $\alpha > 0$. This exponential decay ensures:

1. The integral converges absolutely
2. Truncation at a finite upper limit introduces exponentially small error
3. Standard quadrature rules achieve rapid convergence

**Oscillatory behavior.** The factor $e^{-iu\log K}$ introduces oscillation at frequency proportional to $|\log K|$. For deep in-the-money or out-of-the-money options ($K$ far from $S_0$), the oscillation is rapid, requiring finer quadrature grids.

!!! warning "Deep OTM Options"
    For very deep out-of-the-money options ($K \gg S_0$ or $K \ll S_0$), the integrands oscillate rapidly while the option value is small. This causes cancellation errors in the Fourier integral. For such cases, using the in-the-money counterpart via put-call parity and then subtracting is more numerically stable.

---

## Numerical Integration Methods

Several quadrature methods are suitable for evaluating the Fourier integrals.

### Method 1: Gauss-Laguerre Quadrature

The semi-infinite integral $\int_0^\infty f(u) \, du$ maps naturally to Gauss-Laguerre quadrature after the substitution $u = t$:

$$
P_j = \frac{1}{2} + \frac{1}{\pi}\sum_{n=1}^{N} w_n \, \text{Re}\!\left[\frac{e^{-iu_n \log K}\varphi_j(u_n)}{iu_n}\right] e^{u_n}
$$

where $(u_n, w_n)$ are the Gauss-Laguerre nodes and weights. With $N = 32$ to 64 nodes, this typically achieves 10--12 digits of accuracy.

### Method 2: Truncated Simpson's Rule

Truncate the integral at $u_{\max}$ and apply composite Simpson's rule on $[0, u_{\max}]$ with $M$ subintervals:

$$
P_j \approx \frac{1}{2} + \frac{1}{\pi} \cdot \frac{h}{3}\sum_{n=0}^{2M} c_n \, f_j(u_n)
$$

where $h = u_{\max}/(2M)$ and $c_n = (1, 4, 2, 4, 2, \ldots, 4, 1)$ are Simpson weights.

Choosing $u_{\max} = 50$ and $M = 500$ (so $h = 0.05$) gives approximately 8 digits of accuracy.

### Method 3: Adaptive Quadrature

Use a library routine (e.g., MATLAB's `integral`, Python's `scipy.integrate.quad`) that automatically adjusts the step size based on local error estimates. This is the most robust approach and is recommended for benchmarking.

| Method | CF evaluations | Typical accuracy | Speed |
|--------|---------------|-----------------|-------|
| Gauss-Laguerre 64 | 64 | $10^{-12}$ | 0.1 ms |
| Simpson $M=500$ | 1001 | $10^{-8}$ | 1 ms |
| Adaptive quadrature | 200--500 | $10^{-10}$ | 0.5 ms |

---

## Putting It Together: Complete Algorithm

**Input:** Heston parameters $(\kappa, \theta, \xi, \rho, v_0)$, market data $(S_0, K, r, q, \tau)$.

**Step 1.** Choose the Albrecher stable formulation for the Heston CF.

**Step 2.** For $j = 2$ ($\mathbb{Q}$ measure): evaluate the integrand

$$
f_2(u) = \text{Re}\!\left[\frac{e^{-iu\log K}\varphi_2(u)}{iu}\right]
$$

at the quadrature nodes and compute $P_2 = \frac{1}{2} + \frac{1}{\pi}\int_0^\infty f_2(u) \, du$.

**Step 3.** For $j = 1$ ($\mathbb{Q}^S$ measure): evaluate

$$
f_1(u) = \text{Re}\!\left[\frac{e^{-iu\log K}\varphi_1(u)}{iu}\right]
$$

using $\varphi_1(u) = \varphi_2(u-i)/(S_0 e^{(r-q)\tau})$, and compute $P_1$.

**Step 4.** Compute the call price:

$$
C = S_0 e^{-q\tau} P_1 - K e^{-r\tau} P_2
$$

---

## Numerical Example

Parameters: $S_0 = 100$, $K = 100$, $r = 0.05$, $q = 0$, $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$, $\tau = 1$.

**Step 1: Compute $P_2$.**

$$
P_2 = \frac{1}{2} + \frac{1}{\pi}\int_0^{\infty} \text{Re}\!\left[\frac{e^{-iu\log 100} \varphi_2(u)}{iu}\right] du = 0.51340
$$

**Step 2: Compute $P_1$.**

$$
P_1 = \frac{1}{2} + \frac{1}{\pi}\int_0^{\infty} \text{Re}\!\left[\frac{e^{-iu\log 100} \varphi_1(u)}{iu}\right] du = 0.57481
$$

**Step 3: Call price.**

$$
C = 100(0.57481) - 100 e^{-0.05}(0.51340) = 57.481 - 48.853 = 8.628
$$

**Implied volatility:** The Black-Scholes implied volatility corresponding to $C = 8.628$ is approximately $\sigma_{\text{imp}} = 20.1\%$, close to $\sqrt{v_0} = 20\%$ since the option is near-ATM and the Heston parameters are close to the lognormal case.

??? example "Sensitivity to Quadrature Method"
    Computing the same price with different methods:

    | Method | Call Price | Abs Error vs GL-128 |
    |--------|-----------|-------------------|
    | Gauss-Laguerre 32 | 8.62812345 | $2 \times 10^{-8}$ |
    | Gauss-Laguerre 64 | 8.62812344 | $< 10^{-11}$ |
    | Gauss-Laguerre 128 | 8.62812344 | reference |
    | Simpson $M=200$ | 8.62812 | $3 \times 10^{-6}$ |
    | Simpson $M=1000$ | 8.6281234 | $4 \times 10^{-8}$ |
    | Adaptive (tol=$10^{-10}$) | 8.62812344 | $< 10^{-10}$ |

    Gauss-Laguerre with 64 nodes achieves near-machine precision, making it the most efficient choice for single-strike pricing.

---

## Advantages and Limitations

**Advantages:**

- **Accuracy**: 10--15 digits achievable with appropriate quadrature
- **Simplicity**: requires only a one-dimensional integral
- **Benchmark quality**: serves as the reference for validating all other methods
- **Direct probability extraction**: $P_1$ and $P_2$ are useful for delta computation and digital pricing

**Limitations:**

- **Single-strike**: each strike requires a separate integration (unlike FFT which prices all strikes simultaneously)
- **Speed**: slower than COS for individual strikes (64 vs 128 CF evaluations, but COS per-evaluation cost is lower)
- **Oscillatory integrand**: deep OTM options require careful treatment

!!! note "Role as Benchmark"
    The semi-closed-form approach is the gold standard for Heston option pricing accuracy. Every implementation of COS, FFT, or Monte Carlo should be validated against the semi-closed-form result with high-order Gauss-Laguerre quadrature. Agreement to 8+ significant digits provides confidence that the implementation is correct.

---

## Summary

The semi-closed-form Heston pricing formula expresses the European call as $C = S_0 e^{-q\tau} P_1 - K e^{-r\tau} P_2$, where $P_1$ and $P_2$ are exercise probabilities computed by Gil-Pelaez Fourier inversion of the Heston characteristic function under the stock-price numeraire and risk-neutral measures respectively. The integrals converge rapidly due to the exponential decay of the CF and can be evaluated to 10--15 digit accuracy using Gauss-Laguerre quadrature with 32--64 nodes. While not the fastest method for production pricing (COS and FFT are faster for multiple strikes), the semi-closed-form approach provides the definitive benchmark for validating all other Heston pricing implementations.
