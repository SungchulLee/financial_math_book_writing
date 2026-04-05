# COS and FFT Pricing Engines

The Gil-Pelaez inversion prices one option at a time: each strike requires a separate numerical integration. For calibration, where hundreds of options across dozens of strikes must be priced at every optimizer iteration, this per-strike cost is prohibitive. Two methods overcome this bottleneck. The **COS method** (Fang and Oosterlee, 2008) expands the density in a Fourier cosine series and evaluates the pricing formula analytically for each term, achieving exponential convergence with $N = 64$--$128$ terms. The **Carr-Madan FFT** (Carr and Madan, 1999) prices an entire grid of $N$ strikes simultaneously in $\mathcal{O}(N \log N)$ operations. This guide develops both methods and their implementations in [`cos_and_fft_pricing_engines.py`](cos_and_fft_pricing_engines.py). The COS method reference implementation is also available in [`heston_cos_method.py`](heston_cos_method.py).

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Implement the COS method for Heston European option pricing with proper truncation range selection
    2. Implement the Carr-Madan FFT method with the damping factor and grid constraints
    3. Choose between COS and FFT based on the pricing task (single maturity vs full surface)
    4. Validate both engines against Gil-Pelaez inversion results

!!! tip "Prerequisites"
    This section builds on the [characteristic function engine](characteristic_function_engine.md), the [COS method applied to Heston](../heston_cos/cos_applied_to_heston.md), and the [Carr-Madan FFT pricing](../european_pricing/carr_madan_fft_pricing.md).

---

## The COS Method

### Idea

The COS method approximates the risk-neutral density $f(y | x)$ of $Y = \ln(S_T/K)$ by a truncated Fourier cosine expansion on $[a, b]$:

$$
f(y) \approx \frac{2}{b - a} \sum_{k=0}^{N-1} {}' A_k \cos\!\left(k\pi \frac{y - a}{b - a}\right)
$$

where $\sum'$ means the first term is halved, and the Fourier coefficients $A_k$ are recovered from the characteristic function:

$$
A_k = \text{Re}\!\left[\varphi\!\left(\frac{k\pi}{b - a}\right) \exp\!\left(-i \frac{k\pi \, a}{b - a}\right)\right]
$$

The option price is then:

$$
V = e^{-r\tau} \frac{b - a}{2} \sum_{k=0}^{N-1} {}' A_k \, H_k
$$

where $H_k$ are the **payoff coefficients**---closed-form integrals of the payoff function against the cosine basis.

### Payoff Coefficients

For a European **call** with log-moneyness payoff on $[a, b]$:

$$
H_k^{\text{call}} = \frac{2}{b - a}\left(\chi_k(0, b) - \psi_k(0, b)\right)
$$

where the auxiliary functions are:

$$
\chi_k(c, d) = \frac{1}{1 + (k\pi/(b - a))^2}\left[\cos(\theta_d)e^d - \cos(\theta_c)e^c + \frac{k\pi}{b-a}\left(\sin(\theta_d)e^d - \sin(\theta_c)e^c\right)\right]
$$

$$
\psi_k(c, d) = \begin{cases} (d - c) & k = 0 \\[4pt] \dfrac{b - a}{k\pi}\left[\sin(\theta_d) - \sin(\theta_c)\right] & k \geq 1 \end{cases}
$$

with $\theta_c = k\pi(c - a)/(b - a)$ and $\theta_d = k\pi(d - a)/(b - a)$.

For a European **put**, replace the integration range with $[a, 0]$:

$$
H_k^{\text{put}} = \frac{2}{b - a}\left(\psi_k(a, 0) - \chi_k(a, 0)\right)
$$

### Truncation Range Selection

The interval $[a, b]$ must contain the bulk of the density. A standard choice uses the first four cumulants $c_1, c_2, c_3, c_4$ of $\ln(S_T/K)$:

$$
a = c_1 - L\sqrt{c_2 + \sqrt{c_4}}, \qquad b = c_1 + L\sqrt{c_2 + \sqrt{c_4}}
$$

where $L = 10$--$12$ provides sufficient coverage. The cumulants are obtained from the characteristic function:

$$
c_1 = -i\varphi'(0), \qquad c_2 = -\varphi''(0) + c_1^2, \qquad c_n = (-i)^n \frac{d^n}{du^n}\ln\varphi(u)\bigg|_{u=0}
$$

For practical purposes, the first two cumulants (mean and variance) suffice, and a simpler rule is:

$$
a = x_0 - L\sqrt{v_0 \tau + \theta \tau}, \qquad b = x_0 + L\sqrt{v_0 \tau + \theta \tau}
$$

where $x_0 = \ln(S_0/K) + (r - q)\tau$ and $L = 10$.

### Implementation

```python
def heston_cos_price(model, K, tau, N=128, L=10, cp="call"):
    """
    Price European options using the COS method.

    Parameters
    ----------
    model : HestonModel
    K : array_like
        Strikes
    tau : float
        Time to maturity
    N : int
        Number of COS terms (64-256 typical)
    L : float
        Truncation range parameter
    cp : str
        "call" or "put"
    """
    K = np.atleast_1d(np.asarray(K, dtype=float))
    x0 = np.log(model.S0 / K) + (model.r - model.q) * tau

    # Truncation range (per-strike)
    std_approx = np.sqrt((model.v0 + model.theta) * tau)
    a = -L * std_approx
    b = L * std_approx

    # Fourier frequencies
    k = np.arange(N)
    k_pi = k * np.pi / (b - a)

    # Density coefficients from characteristic function
    cf_vals = heston_cf(k_pi, tau, model.S0, model.v0, model.kappa,
                        model.theta, model.xi, model.rho,
                        model.r, model.q)
    A_k = (2 / (b - a)) * np.real(cf_vals * np.exp(-1j * k_pi * a))
    A_k[0] *= 0.5  # prime summation

    # Payoff coefficients
    prices = []
    for x, K_i in zip(x0, K):
        chi_k, psi_k = _compute_chi_psi(a, b, N, cp)
        H_k = _compute_H_k(chi_k, psi_k, b - a, cp)
        price = np.exp(-model.r * tau) * (b - a) / 2 * np.sum(A_k * H_k)
        prices.append(price)

    return np.array(prices)
```

!!! note "Convergence Rate"
    The COS method achieves **exponential convergence** in $N$ for smooth densities. For the Heston model, $N = 64$ typically gives 4--6 digits of accuracy, and $N = 128$ gives 8--10 digits. This is far more efficient than the trapezoidal rule in Gil-Pelaez inversion, which converges only polynomially.

---

## The Carr-Madan FFT Method

### Idea

The Carr-Madan method computes call prices on an equally-spaced grid of **log-strikes** $k_n = k_0 + n\Delta k$ for $n = 0, 1, \ldots, N-1$ using a single FFT. The method introduces a **damping factor** $e^{\alpha k}$ to ensure integrability of the Fourier transform of the call price.

### The Damped Call Price Transform

Define the modified call price $c_\tau(k) = e^{\alpha k} C(K, \tau)$ where $k = \ln K$ and $\alpha > 0$ is the damping parameter. Its Fourier transform is:

$$
\Psi(\nu) = \int_{-\infty}^{\infty} e^{i\nu k} c_\tau(k) \, dk = \frac{e^{-r\tau} \varphi(\nu - (\alpha+1)i, \tau)}{\alpha^2 + \alpha - \nu^2 + i(2\alpha+1)\nu}
$$

where $\varphi$ is the Heston CF. The call price is recovered by inverse Fourier transform:

$$
C(K_n, \tau) = \frac{e^{-\alpha k_n}}{\pi} \text{Re}\!\left[\sum_{j=0}^{N-1} e^{-i\nu_j k_0} \Psi(\nu_j) \, e^{-i \frac{2\pi}{N} jn} \Delta\nu\right]
$$

This sum is exactly the **discrete Fourier transform** (DFT), computed via FFT in $\mathcal{O}(N\log N)$ operations.

### Grid Constraints

The frequency and log-strike grids are linked by:

$$
\Delta\nu \cdot \Delta k = \frac{2\pi}{N}
$$

Choosing $N = 2^{12} = 4096$, $\Delta\nu = 0.01$ gives $\Delta k = 2\pi/(4096 \times 0.01) \approx 0.153$, covering a log-strike range of about $4096 \times 0.153 = 628$---far wider than needed.

### Damping Parameter

The damping parameter $\alpha$ must satisfy $\alpha > 0$ and $\varphi(u - (\alpha+1)i)$ must exist (i.e., $\mathbb{E}[S_T^{\alpha+1}] < \infty$). The moment explosion constraint requires $\alpha + 1 < p^*$ where $p^*$ is the critical moment exponent of the Heston model. Typical values: $\alpha = 1.5$ for standard parameters.

### Simpson's Rule Correction

The trapezoidal approximation can be improved by applying **Simpson's rule weights** to the FFT input:

$$
w_j = \frac{\Delta\nu}{3}\left(3 + (-1)^{j+1} - \delta_{j0}\right)
$$

where $\delta_{j0}$ is the Kronecker delta. This improves convergence from $\mathcal{O}(\Delta\nu^2)$ to $\mathcal{O}(\Delta\nu^4)$.

### Implementation

```python
def heston_fft_prices(model, tau, N=4096, alpha=1.5, d_nu=0.01):
    """
    Price European calls on a grid of strikes via Carr-Madan FFT.

    Returns
    -------
    log_strikes : ndarray
        Log-strike grid
    prices : ndarray
        Call prices on the grid
    """
    d_k = 2 * np.pi / (N * d_nu)
    k0 = -N * d_k / 2  # center the grid

    # Frequency grid
    nu = np.arange(N) * d_nu

    # Simpson weights
    w = d_nu / 3 * (3 + (-1)**np.arange(1, N + 1))
    w[0] = d_nu / 3

    # CF evaluation at shifted frequencies
    cf_vals = heston_cf(nu - (alpha + 1) * 1j, tau,
                        model.S0, model.v0, model.kappa, model.theta,
                        model.xi, model.rho, model.r, model.q)

    # Damped transform
    denom = alpha**2 + alpha - nu**2 + 1j * (2 * alpha + 1) * nu
    Psi = np.exp(-model.r * tau) * cf_vals / denom

    # FFT input
    fft_input = np.exp(-1j * nu * k0) * Psi * w

    # FFT
    fft_output = np.fft.fft(fft_input)

    # Log-strike grid and prices
    log_strikes = k0 + np.arange(N) * d_k
    prices = np.exp(-alpha * log_strikes) / np.pi * np.real(fft_output)

    return log_strikes, prices
```

---

## COS vs FFT: When to Use Which

| Feature | COS Method | Carr-Madan FFT |
|---|---|---|
| Strike flexibility | Any strikes (not restricted to grid) | Equally-spaced log-strike grid |
| Number of terms | $N = 64$--$128$ | $N = 2^{10}$--$2^{14}$ |
| Convergence | Exponential in $N$ | Polynomial ($\mathcal{O}(\Delta\nu^4)$ with Simpson) |
| Best use case | Pricing a few strikes at one maturity | Calibration: all strikes at one maturity |
| Greeks | Term-by-term differentiation | Finite differences on price grid |
| Multi-strike cost | $\mathcal{O}(N \cdot M)$ for $M$ strikes | $\mathcal{O}(N \log N)$ independent of $M$ |

**Calibration**: The FFT is preferred because it produces prices for all strikes in one shot, enabling fast objective function evaluation. At each maturity, a single FFT call replaces $M$ separate COS evaluations.

**Risk management**: The COS method is preferred for pricing individual trades at specific strikes, especially when Greeks are needed (since the cosine series can be differentiated analytically).

---

## Validation

Both engines should be validated against Gil-Pelaez inversion, which serves as a high-accuracy reference.

```python
# Reference: Gil-Pelaez
ref_price = heston_call_price(K=100, tau=0.5, model=model)

# COS method
cos_price = heston_cos_price(model, K=100, tau=0.5, N=128)

# FFT method (interpolate to K=100)
log_K, fft_prices = heston_fft_prices(model, tau=0.5)
fft_price = np.interp(np.log(100), log_K, fft_prices)

print(f"Gil-Pelaez: {ref_price:.8f}")
print(f"COS (N=128): {cos_price[0]:.8f}")
print(f"FFT (N=4096): {fft_price:.8f}")
```

Typical agreement is 8+ digits for COS with $N = 128$ and 4--6 digits for FFT with $N = 4096$.

---

## Summary

The COS and FFT methods are the workhorses of Fourier-based Heston pricing. The COS method expands the density in a cosine series, converging exponentially with $N = 64$--$128$ terms, and excels at pricing individual options with high accuracy. The Carr-Madan FFT produces prices on an entire log-strike grid in $\mathcal{O}(N\log N)$ operations, making it the natural choice for calibration sweeps. Both methods rely on the characteristic function engine for their input and should be validated against Gil-Pelaez inversion before deployment.

---

## Exercises

**Exercise 1.**
For the COS method with Heston parameters $v_0 = 0.04$, $\theta = 0.06$, $\tau = 1.0$, $S_0 = 100$, $K = 100$, $r = 3\%$, $q = 1\%$, and $L = 10$, compute the truncation range $[a, b]$ using the simplified rule $a = x_0 - L\sqrt{(v_0 + \theta)\tau}$ and $b = x_0 + L\sqrt{(v_0 + \theta)\tau}$ where $x_0 = \ln(S_0/K) + (r - q)\tau$. How wide is the interval in terms of standard deviations of $\ln(S_T/K)$?

??? success "Solution to Exercise 1"
    Given $v_0 = 0.04$, $\theta = 0.06$, $\tau = 1.0$, $S_0 = 100$, $K = 100$, $r = 0.03$, $q = 0.01$, and $L = 10$.

    First, compute the center of the truncation range:

    $$
    x_0 = \ln(S_0/K) + (r - q)\tau = \ln(100/100) + (0.03 - 0.01)(1.0) = 0 + 0.02 = 0.02
    $$

    The standard deviation proxy:

    $$
    \text{std}_{\text{approx}} = \sqrt{(v_0 + \theta)\tau} = \sqrt{(0.04 + 0.06)(1.0)} = \sqrt{0.10} \approx 0.3162
    $$

    The truncation range (note that the simplified formula in the implementation centers at 0 and adds $x_0$ separately):

    $$
    a = -L \cdot \text{std}_{\text{approx}} = -10 \times 0.3162 = -3.162
    $$

    $$
    b = L \cdot \text{std}_{\text{approx}} = 10 \times 0.3162 = 3.162
    $$

    The interval width is $b - a = 6.324$.

    **How wide in standard deviations:** The actual standard deviation of $\ln(S_T/K)$ under Heston can be estimated from the integrated variance:

    $$
    \text{Var}[\ln(S_T/K)] \approx \bar{v}\tau = \left[\theta + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa T}\right]\tau
    $$

    Without specifying $\kappa$, a rough estimate uses $(v_0 + \theta)/2 = 0.05$, giving $\sigma_{\ln(S_T/K)} \approx \sqrt{0.05} \approx 0.224$. However, the formula uses $\sqrt{v_0 + \theta} = 0.316$ as a conservative overestimate, so the interval covers:

    $$
    \frac{b - a}{2\sigma_{\ln(S_T/K)}} \approx \frac{6.324}{2 \times 0.224} \approx 14.1 \text{ standard deviations on each side}
    $$

    This is extremely generous. Even $L = 6$ would capture $> 99.9999\%$ of the probability mass for a Gaussian distribution, and the Heston density has thinner tails than what $\sqrt{v_0 + \theta}$ implies. The conservative choice ensures that the COS method's truncation error is negligible relative to the series truncation error.

---

**Exercise 2.**
The COS method uses $N$ terms in the cosine expansion. If the method achieves exponential convergence with error $\sim e^{-cN}$ for some $c > 0$, how many digits of accuracy do you gain by doubling $N$ from 64 to 128? Compare this with the Carr-Madan FFT, which converges as $\mathcal{O}(\Delta\nu^4)$ with Simpson's rule: how many digits does the FFT gain by doubling $N$ from 4096 to 8192?

??? success "Solution to Exercise 2"
    **COS method (exponential convergence):**

    With error $\sim e^{-cN}$, doubling $N$ from 64 to 128 reduces the error by a factor of:

    $$
    \frac{e^{-c \cdot 64}}{e^{-c \cdot 128}} = e^{64c}
    $$

    The number of additional digits gained is:

    $$
    \Delta_{\text{digits}} = \frac{64c}{\ln 10} \approx \frac{64c}{2.303}
    $$

    If $N = 64$ gives 5 digits of accuracy, then $e^{-64c} \approx 10^{-5}$, so $c \approx 5\ln 10/64 \approx 0.180$. Doubling to $N = 128$:

    $$
    \Delta_{\text{digits}} = \frac{64 \times 0.180}{2.303} \approx 5 \text{ additional digits}
    $$

    So doubling from $N = 64$ (5 digits) to $N = 128$ gives approximately 10 digits---doubling $N$ roughly doubles the accuracy in digits. This is the hallmark of exponential (spectral) convergence.

    **Carr-Madan FFT (polynomial convergence with Simpson's rule):**

    With Simpson's rule, the error scales as $\mathcal{O}(\Delta\nu^4)$. When $N$ doubles from 4096 to 8192, the frequency spacing halves: $\Delta\nu \to \Delta\nu/2$. The error ratio is:

    $$
    \frac{(\Delta\nu/2)^4}{\Delta\nu^4} = \frac{1}{16}
    $$

    In terms of digits gained:

    $$
    \Delta_{\text{digits}} = \log_{10}(16) \approx 1.2 \text{ digits}
    $$

    So doubling the FFT grid from 4096 to 8192 gains only about 1.2 additional digits of accuracy. This illustrates the vast efficiency difference: the COS method gains 5 digits per doubling versus 1.2 digits for the FFT. For a single-strike evaluation, the COS method is overwhelmingly more efficient. The FFT's advantage lies in producing an entire grid of strike prices simultaneously.

---

**Exercise 3.**
In the Carr-Madan FFT, the frequency and log-strike grids satisfy $\Delta\nu \cdot \Delta k = 2\pi / N$. With $N = 4096$ and $\Delta\nu = 0.01$, compute $\Delta k$ and the total log-strike range $[k_0, k_0 + N\Delta k]$. If $S_0 = 100$ and the FFT grid is centered at $\ln(S_0) = 4.605$, what are the minimum and maximum strikes (in dollar terms) on the grid? Are these reasonable for a calibration application?

??? success "Solution to Exercise 3"
    Given $N = 4096$, $\Delta\nu = 0.01$:

    $$
    \Delta k = \frac{2\pi}{N \cdot \Delta\nu} = \frac{2\pi}{4096 \times 0.01} = \frac{2\pi}{40.96} \approx 0.15340
    $$

    The log-strike grid is centered at $k_0 = -N\Delta k/2$:

    $$
    k_0 = -\frac{4096 \times 0.15340}{2} = -\frac{628.3}{2} = -314.16
    $$

    The grid spans from $k_0 = -314.16$ to $k_0 + N\Delta k = -314.16 + 628.3 = 314.16$.

    With $S_0 = 100$, the center is $\ln(S_0) = \ln(100) = 4.605$.

    The minimum and maximum strikes in dollar terms:

    $$
    K_{\min} = e^{k_0} = e^{-314.16} \approx 0 \text{ (essentially zero)}
    $$

    $$
    K_{\max} = e^{314.16} \approx \infty \text{ (astronomically large)}
    $$

    These extreme values are clearly unreasonable---no real option exists at these strikes. However, the grid does not need to be used at its extremes. The **usable** portion of the grid is centered near $\ln(S_0) = 4.605$, where the option prices are meaningful. For a calibration application, the relevant log-strike range is approximately $\ln(80) = 4.38$ to $\ln(120) = 4.79$, a range of about 0.41. With $\Delta k = 0.153$, this range contains only about $0.41/0.153 \approx 2.7$ grid points---very few!

    **Are these reasonable for calibration?** The grid spacing is actually the concern, not the range. With $\Delta k = 0.153$, the strikes are separated by a factor of $e^{0.153} \approx 1.166$, or about 16.6% apart. For calibration, market strikes are typically 2--5% apart, so the FFT grid is too coarse for direct use. The standard practice is to **interpolate** the FFT output to the market strikes using cubic spline interpolation on the log-strike grid. This adds some interpolation error but preserves the $\mathcal{O}(N\log N)$ scaling advantage.

    To achieve finer resolution, one can decrease $\Delta\nu$ (e.g., $\Delta\nu = 0.001$ gives $\Delta k = 0.00153$, or 0.15% strike spacing), at the cost of needing to evaluate the CF at more frequencies.

---

**Exercise 4.**
The damping parameter $\alpha$ in the Carr-Madan method must satisfy $\alpha + 1 < p^*$, where $p^*$ is the critical moment exponent. For Heston parameters $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.5$, $\rho = -0.7$, the critical exponent satisfies $p^* \approx 2 + 2\kappa/(\xi^2(1 - \rho^2))$. Compute $p^*$ and determine the maximum allowable $\alpha$. Explain what happens to the FFT prices if $\alpha$ is chosen too large (i.e., $\alpha + 1 > p^*$).

??? success "Solution to Exercise 4"
    For Heston parameters $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.5$, $\rho = -0.7$, the approximate critical moment exponent is:

    $$
    p^* \approx 2 + \frac{2\kappa}{\xi^2(1 - \rho^2)} = 2 + \frac{2 \times 2.0}{0.25 \times (1 - 0.49)} = 2 + \frac{4.0}{0.25 \times 0.51} = 2 + \frac{4.0}{0.1275} = 2 + 31.37 \approx 33.37
    $$

    (Note: this is an approximation; the exact $p^*$ is the solution to a more complex equation involving $\kappa$, $\xi$, $\rho$, and $T$.)

    The maximum allowable damping parameter:

    $$
    \alpha_{\max} = p^* - 1 \approx 33.37 - 1 = 32.37
    $$

    With $\alpha = 1.5$ (the typical choice), we have $\alpha + 1 = 2.5 \ll 33.37$, so the damping parameter is well within the safe range. Even $\alpha = 30$ would be permissible, though in practice values above 5 are rarely needed.

    **What happens if $\alpha + 1 > p^*$:** The condition $\alpha + 1 < p^*$ ensures that $\mathbb{E}[S_T^{\alpha+1}] < \infty$, which is necessary for the Fourier transform $\Psi(\nu)$ to exist. If $\alpha + 1 \geq p^*$, the moment $\mathbb{E}[S_T^{\alpha+1}]$ explodes (diverges to infinity), and the CF evaluated at $\nu - (\alpha+1)i$ becomes undefined. Numerically, the CF values blow up to `inf` or `nan`, and the FFT output produces garbage prices---typically large oscillating values with no relation to true option prices.

    For the parameters given, $p^* \approx 33$ is extremely large, meaning the Heston model's moment explosion is not a practical concern. However, for parameters with large $\xi$ and $\rho$ close to $-1$ (e.g., $\xi = 2.0$, $\rho = -0.95$), $p^*$ can drop to single digits, making the $\alpha$ constraint binding.

---

**Exercise 5.**
A calibration requires pricing $M = 35$ options at a single maturity. Compare the computational cost (in number of CF evaluations) for: (a) the COS method with $N = 128$ applied per-strike ($M \times N$ evaluations), and (b) the Carr-Madan FFT with $N = 4096$ (a single FFT). At what value of $M$ does the COS method become more expensive than the FFT? Consider also the cost of interpolating the FFT output to the exact market strikes.

??? success "Solution to Exercise 5"
    **(a) COS method at $N = 128$ per-strike:**

    Each strike requires $N = 128$ CF evaluations. For $M = 35$ strikes:

    $$
    N_{\text{CF}}^{\text{COS}} = M \times N = 35 \times 128 = 4{,}480 \text{ CF evaluations}
    $$

    **(b) Carr-Madan FFT at $N = 4096$:**

    A single FFT requires $N = 4096$ CF evaluations (one per frequency), regardless of how many strikes are on the grid:

    $$
    N_{\text{CF}}^{\text{FFT}} = 4{,}096 \text{ CF evaluations}
    $$

    **Crossover point:**

    The COS method is cheaper when $M \times 128 < 4096$, i.e., $M < 32$. For $M \geq 32$ strikes at a single maturity, the FFT is cheaper in terms of CF evaluations. With $M = 35$, the COS method ($4{,}480$ evaluations) is slightly more expensive than the FFT ($4{,}096$ evaluations).

    However, the comparison is not purely about CF counts:

    1. **FFT interpolation cost:** The FFT produces prices on a fixed log-strike grid, not at the market strikes. Interpolation (cubic spline) introduces a small error (typically $< 0.1$ bps) and has negligible computational cost.

    2. **COS method flexibility:** The COS method can evaluate at the exact market strikes with no interpolation error. For Greeks computation (where interpolation errors amplify), this is a significant advantage.

    3. **Vectorization:** The FFT evaluates all $N = 4096$ CF values in a single vectorized call, while the COS method can also batch its $N = 128$ evaluations. But the COS loop over $M = 35$ strikes involves computing separate payoff coefficients for each strike.

    4. **Accuracy at the crossover:** At $M = 35$, both methods have comparable cost, but the FFT achieves only 4--6 digits of accuracy (polynomial convergence) while the COS with $N = 128$ achieves 8--10 digits (exponential convergence). If accuracy matters more than speed, the COS method is preferable even when it uses slightly more CF evaluations.

    For calibration (where speed dominates and 4-digit accuracy suffices), the FFT is preferred when $M > 32$. For risk management or Greeks (where accuracy matters), the COS method is preferred regardless of $M$.

---

**Exercise 6.**
Implement the payoff coefficients for a European call. For $k = 0$, show that $\psi_0(0, b) = b$ and compute $\chi_0(0, b)$ in closed form. For general $k \geq 1$, verify the formula:

$$
\chi_k(0, b) = \frac{1}{1 + (k\pi/(b-a))^2}\left[\cos\!\left(\frac{k\pi(b-a)}{b-a}\right)e^b - 1 + \frac{k\pi}{b-a}\sin\!\left(\frac{k\pi(b-a)}{b-a}\right)e^b\right]
$$

by simplifying $\theta_c = k\pi(0 - a)/(b-a)$ and $\theta_d = k\pi(b - a)/(b-a) = k\pi$.

??? success "Solution to Exercise 6"
    For $k = 0$:

    **$\psi_0(0, b)$:** By the definition, for $k = 0$:

    $$
    \psi_0(c, d) = d - c
    $$

    So $\psi_0(0, b) = b - 0 = b$.

    **$\chi_0(0, b)$:** For $k = 0$, compute $\theta_c = 0 \cdot \pi(0 - a)/(b - a) = 0$ and $\theta_d = 0 \cdot \pi(b - a)/(b - a) = 0$. The formula gives:

    $$
    \chi_0(0, b) = \frac{1}{1 + 0}\left[\cos(0)e^b - \cos(0)e^0 + 0\right] = e^b - 1
    $$

    **For general $k \geq 1$:**

    With $c = 0$ and $d = b$, we have:

    $$
    \theta_c = \frac{k\pi(0 - a)}{b - a} = \frac{-k\pi a}{b - a}
    $$

    $$
    \theta_d = \frac{k\pi(b - a)}{b - a} = k\pi
    $$

    Substituting into the $\chi_k$ formula:

    $$
    \chi_k(0, b) = \frac{1}{1 + (k\pi/(b-a))^2}\left[\cos(k\pi)e^b - \cos\!\left(\frac{-k\pi a}{b-a}\right)e^0 + \frac{k\pi}{b-a}\left(\sin(k\pi)e^b - \sin\!\left(\frac{-k\pi a}{b-a}\right)e^0\right)\right]
    $$

    Since $\cos(k\pi) = (-1)^k$ and $\sin(k\pi) = 0$:

    $$
    \chi_k(0, b) = \frac{1}{1 + (k\pi/(b-a))^2}\left[(-1)^k e^b - \cos\!\left(\frac{k\pi a}{b-a}\right) + \frac{k\pi}{b-a}\sin\!\left(\frac{k\pi a}{b-a}\right)\right]
    $$

    Note that $\cos(-x) = \cos(x)$ and $\sin(-x) = -\sin(x)$ were used.

    This matches the formula given in the exercise, since $\cos(k\pi(b-a)/(b-a)) = \cos(k\pi) = (-1)^k$ and $\sin(k\pi(b-a)/(b-a)) = \sin(k\pi) = 0$, so the term $\frac{k\pi}{b-a}\sin(k\pi)e^b$ vanishes. The formula simplifies to:

    $$
    \chi_k(0, b) = \frac{(-1)^k e^b - \cos\!\left(\frac{k\pi a}{b-a}\right) + \frac{k\pi}{b-a}\sin\!\left(\frac{k\pi a}{b-a}\right)}{1 + (k\pi/(b-a))^2}
    $$

    For the symmetric case $a = -b$ (as occurs when the COS range is centered at zero), $a/(b-a) = -b/(2b) = -1/2$, so $\cos(k\pi a/(b-a)) = \cos(-k\pi/2) = \cos(k\pi/2)$ and $\sin(k\pi a/(b-a)) = \sin(-k\pi/2) = -\sin(k\pi/2)$.

---

**Exercise 7.**
You need to price 200 options across 5 maturities (40 strikes per maturity) for a Heston calibration. Design an optimal pricing strategy that mixes COS and FFT methods. For which maturities would you use the FFT, and for which would you use COS? Justify your answer based on the number of strikes, desired accuracy, and total computational cost. Estimate the total number of CF evaluations for your strategy.

??? success "Solution to Exercise 7"
    **Optimal mixed strategy for 200 options across 5 maturities (40 strikes each):**

    Since there are 40 strikes per maturity, and the crossover point is at $M = 32$ (where COS cost $= M \times 128$ equals FFT cost $= 4096$), the FFT is more cost-effective for all maturities.

    **Recommended: Use FFT for all 5 maturities.**

    Each maturity requires a single FFT with $N = 4096$ CF evaluations:

    $$
    N_{\text{CF}}^{\text{FFT, total}} = 5 \times 4096 = 20{,}480 \text{ CF evaluations}
    $$

    For comparison, using COS for all maturities would require:

    $$
    N_{\text{CF}}^{\text{COS, total}} = 5 \times 40 \times 128 = 25{,}600 \text{ CF evaluations}
    $$

    The FFT saves about 20% in CF evaluations while producing prices for the entire log-strike grid (not just the 40 market strikes).

    **When a mixed strategy makes sense:**

    If the number of strikes varied significantly across maturities, a mixed strategy would be beneficial. For example, if the distribution were:

    | Maturity | Strikes | COS cost ($M \times 128$) | FFT cost (4096) | Choice |
    |---|---|---|---|---|
    | $T_1$ | 10 | 1,280 | 4,096 | COS |
    | $T_2$ | 20 | 2,560 | 4,096 | COS |
    | $T_3$ | 40 | 5,120 | 4,096 | FFT |
    | $T_4$ | 60 | 7,680 | 4,096 | FFT |
    | $T_5$ | 70 | 8,960 | 4,096 | FFT |

    Total CF evaluations (mixed): $1{,}280 + 2{,}560 + 4{,}096 + 4{,}096 + 4{,}096 = 16{,}128$.

    vs. all-FFT: $5 \times 4{,}096 = 20{,}480$.

    vs. all-COS: $10 \times 128 + 20 \times 128 + 40 \times 128 + 60 \times 128 + 70 \times 128 = 25{,}600$.

    The mixed strategy saves 21% over all-FFT and 37% over all-COS.

    **For the original problem (40 strikes per maturity, uniform):** Use FFT for all 5 maturities. Total CF evaluations: 20,480. After the FFT, interpolate to the 40 market strikes per maturity using cubic splines on the log-strike grid. The interpolation cost is negligible ($\mathcal{O}(N)$ for the spline construction plus $\mathcal{O}(M)$ for evaluation), and the interpolation error is well below 0.1 bps for typical parameter ranges.
