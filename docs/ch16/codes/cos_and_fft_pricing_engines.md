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
