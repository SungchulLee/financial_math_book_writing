# Characteristic Function Engine

The characteristic function (CF) is the computational backbone of the Heston model. Every Fourier-based pricing method---Gil-Pelaez inversion, COS, Carr-Madan FFT---begins by evaluating $\varphi(u, \tau)$ for a grid of Fourier frequencies $u$. Getting the CF computation right means getting the branch-cut handling and numerical precision right; a naive implementation produces discontinuities that silently corrupt option prices. This guide develops a robust CF engine based on the Albrecher formulation, explains the source of numerical instability in the original Heston (1993) formula, and walks through the implementation in [`characteristic_function_engine.py`](characteristic_function_engine.py).

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Implement the Heston characteristic function using the numerically stable Albrecher formulation
    2. Explain the branch-cut problem in the original Heston (1993) formula and why the Albrecher fix resolves it
    3. Evaluate the characteristic function on a frequency grid suitable for downstream Fourier pricing
    4. Validate the implementation against known analytical moments

!!! tip "Prerequisites"
    This section builds on the [derivation of the characteristic function](../heston_cf/derivation_of_characteristic_function.md), the [Riccati ODE system](../heston_cf/riccati_ode_system.md), and the [numerical stability analysis](../heston_cf/numerical_stability_and_branch_cuts.md). The model parameters come from the [`HestonModel` class](heston_model_class.md).

---

## The Heston Characteristic Function

The characteristic function of $\ln S_T$ under the risk-neutral measure is:

$$
\varphi(u, \tau) = \mathbb{E}\!\left[e^{iu \ln S_T} \,\middle|\, S_t, v_t\right] = \exp\!\left(C(u, \tau) + D(u, \tau) \, v_t + iu \ln S_t\right)
$$

where $\tau = T - t$ is the time to maturity and $C$, $D$ solve the Riccati system:

$$
D'(\tau) = \tfrac{1}{2}\xi^2 D^2 + (i\rho\xi u - \kappa)D + \tfrac{1}{2}(iu - u^2)
$$

$$
C'(\tau) = (r - q)iu + \kappa\theta \, D
$$

with $C(u, 0) = 0$ and $D(u, 0) = 0$.

---

## Closed-Form Solutions

### The Discriminant

Define the complex discriminant:

$$
\gamma = \sqrt{(\kappa - i\rho\xi u)^2 + \xi^2(iu + u^2)}
$$

The choice of branch for this square root is critical; we return to this below.

### Albrecher (Numerically Stable) Formulation

The Albrecher formulation defines an auxiliary ratio:

$$
g = \frac{\kappa - i\rho\xi u - \gamma}{\kappa - i\rho\xi u + \gamma}
$$

The Riccati solutions are:

$$
D(u, \tau) = \frac{\kappa - i\rho\xi u - \gamma}{\xi^2} \cdot \frac{1 - e^{-\gamma\tau}}{1 - g \, e^{-\gamma\tau}}
$$

$$
C(u, \tau) = (r - q)iu\tau + \frac{\kappa\theta}{\xi^2} \left[ (\kappa - i\rho\xi u - \gamma)\tau - 2\ln\!\left(\frac{1 - g \, e^{-\gamma\tau}}{1 - g}\right) \right]
$$

### Why $|g| < 1$ Ensures Stability

The key property is that $|g| < 1$ whenever $\text{Re}(\gamma) > 0$. Since $e^{-\gamma\tau}$ decays exponentially for $\text{Re}(\gamma) > 0$, the denominator $1 - g \, e^{-\gamma\tau}$ stays bounded away from zero for all $\tau > 0$. The logarithm argument $({1 - g \, e^{-\gamma\tau}})/({1 - g})$ never crosses the negative real axis, so the complex logarithm is continuous.

!!! warning "The Original Heston (1993) Formula"
    Heston's original formulation uses the reciprocal ratio $\tilde{g} = 1/g$, which has $|\tilde{g}| > 1$. The term $\tilde{g} \, e^{+\gamma\tau}$ grows exponentially, causing the logarithm argument to cross the branch cut for large $\tau$ or $|u|$. This produces discontinuous jumps in $C(u, \tau)$ that corrupt the Fourier integral. The Albrecher formulation avoids this entirely.

---

## Implementation

### Core Function

```python
def heston_cf(u, tau, S0, v0, kappa, theta, xi, rho, r, q=0.0):
    """
    Heston characteristic function (Albrecher formulation).

    Parameters
    ----------
    u : array_like (complex or real)
        Fourier frequency
    tau : float
        Time to maturity
    S0, v0, kappa, theta, xi, rho, r, q : float
        Model and market parameters

    Returns
    -------
    phi : ndarray (complex)
        Characteristic function values
    """
    i = 1j
    u = np.asarray(u, dtype=complex)

    # Discriminant
    alpha = kappa - i * rho * xi * u
    beta = i * u + u**2
    gamma = np.sqrt(alpha**2 + xi**2 * beta)

    # Ensure Re(gamma) > 0 for the correct branch
    gamma = np.where(np.real(gamma) < 0, -gamma, gamma)

    # Auxiliary ratio
    g = (alpha - gamma) / (alpha + gamma)

    # Riccati solutions
    exp_gt = np.exp(-gamma * tau)
    D = (alpha - gamma) / xi**2 * (1 - exp_gt) / (1 - g * exp_gt)
    C = (r - q) * i * u * tau + kappa * theta / xi**2 * (
        (alpha - gamma) * tau - 2 * np.log((1 - g * exp_gt) / (1 - g))
    )

    return np.exp(C + D * v0 + i * u * np.log(S0))
```

### Branch Selection

The line `gamma = np.where(np.real(gamma) < 0, -gamma, gamma)` enforces $\text{Re}(\gamma) > 0$. Since $\gamma^2$ is uniquely determined by the Riccati equation, $\gamma$ and $-\gamma$ are both valid square roots. Choosing the one with positive real part ensures $|g| < 1$ and $|e^{-\gamma\tau}| < 1$.

### Vectorized Evaluation

The function accepts arrays of frequencies `u`, enabling efficient evaluation on the integration grid:

```python
u_grid = np.linspace(0.01, 100, 4096)
phi_values = heston_cf(u_grid, tau=0.5, S0=100, v0=0.04,
                       kappa=2.0, theta=0.04, xi=0.5, rho=-0.7,
                       r=0.03, q=0.01)
```

---

## Gil-Pelaez Inversion

The CF engine's primary consumer is the Gil-Pelaez formula for European call prices:

$$
C = S_0 e^{-qT} P_1 - K e^{-rT} P_2
$$

where the risk-neutral probabilities are:

$$
P_j = \frac{1}{2} + \frac{1}{\pi} \int_0^{\infty} \text{Re}\!\left[\frac{e^{-iu\ln K} \varphi_j(u, \tau)}{iu}\right] du
$$

Here $\varphi_1$ is the CF under the stock-price numeraire and $\varphi_2 = \varphi$ is the CF under the money-market numeraire.

### Numerical Quadrature

The integral is computed via the **trapezoidal rule** on a truncated domain $[0, u_{\max}]$:

$$
P_j \approx \frac{1}{2} + \frac{1}{\pi} \sum_{n=1}^{N} \text{Re}\!\left[\frac{e^{-iu_n\ln K} \varphi_j(u_n)}{iu_n}\right] \Delta u
$$

where $u_n = n \Delta u$ and $\Delta u = u_{\max}/N$.

**Choosing $u_{\max}$**: The CF decays as $|\varphi(u)| \sim \exp(-c u^2)$ for large $u$ (where $c$ depends on $\tau$ and $v_0$). Setting $u_{\max} = 100$ and $N = 4096$ (giving $\Delta u \approx 0.024$) provides 10+ digits of accuracy for typical Heston parameters.

```python
def heston_call_price(K, tau, model, u_max=100, N=4096):
    """Price a European call via Gil-Pelaez inversion."""
    du = u_max / N
    u = np.arange(1, N + 1) * du

    # CF under money-market numeraire
    phi2 = heston_cf(u, tau, model.S0, model.v0, model.kappa,
                     model.theta, model.xi, model.rho, model.r, model.q)
    # CF under stock-price numeraire
    phi1 = heston_cf(u - 1j, tau, model.S0, model.v0, model.kappa,
                     model.theta, model.xi, model.rho, model.r, model.q)
    phi1 = phi1 / heston_cf(-1j, tau, model.S0, model.v0, model.kappa,
                            model.theta, model.xi, model.rho,
                            model.r, model.q)

    integrand1 = np.real(np.exp(-1j * u * np.log(K)) * phi1 / (1j * u))
    integrand2 = np.real(np.exp(-1j * u * np.log(K)) * phi2 / (1j * u))

    P1 = 0.5 + np.sum(integrand1) * du / np.pi
    P2 = 0.5 + np.sum(integrand2) * du / np.pi

    call = model.S0 * np.exp(-model.q * tau) * P1 - K * np.exp(-model.r * tau) * P2
    return call
```

---

## Validation via Moments

A useful sanity check is to verify that the CF reproduces the known analytical moments of $\ln S_T$.

### First Moment (Mean of Log-Price)

$$
\mathbb{E}[\ln S_T] = \ln S_0 + (r - q)T - \frac{1}{2}\left[\theta T + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa}\right]
$$

This should equal $-i \, \varphi'(0, T)$, the derivative of the CF at $u = 0$ (computed by finite differences).

### Second Moment (Variance of Log-Price)

$$
\text{Var}[\ln S_T] = -\varphi''(0, T) + [\varphi'(0, T)]^2
$$

The analytical expression involves $v_0$, $\theta$, $\kappa$, $\xi$, and $\rho$. Matching the numerical and analytical values to 8+ digits confirms the CF implementation is correct.

```python
# Numerical first moment via finite differences
eps = 1e-5
phi_p = heston_cf(eps, tau, S0, v0, kappa, theta, xi, rho, r, q)
phi_m = heston_cf(-eps, tau, S0, v0, kappa, theta, xi, rho, r, q)
mean_numerical = -1j * (phi_p - phi_m) / (2 * eps)
```

---

## Performance Considerations

### Vectorization

The CF evaluation is embarrassingly parallel across frequencies $u$. NumPy vectorization eliminates Python loops, and the entire $N = 4096$ grid is computed in a single batch of array operations.

### Complex Arithmetic

All intermediate quantities ($\gamma$, $g$, $D$, $C$) are complex. NumPy handles complex arithmetic natively, but care is needed with `np.sqrt` for complex inputs: NumPy uses the principal branch (non-negative real part), which happens to be the correct convention for the Albrecher formulation.

### Caching

For calibration (where the same $\tau$ is used for many parameter trials), the frequency grid and the $\ln K$ array can be precomputed. Only the CF evaluation depends on $\Theta$.

---

## Summary

The characteristic function engine is the most critical numerical component of the Heston implementation. The Albrecher formulation, which ensures $|g| < 1$ by choosing $\text{Re}(\gamma) > 0$, eliminates the branch-cut discontinuities that plague the original Heston (1993) formula. The implementation evaluates the CF on a vectorized frequency grid and feeds the result to the Gil-Pelaez integral (trapezoidal rule on $[0, u_{\max}]$) for European option pricing. Validation against analytical moments confirms numerical correctness before the engine is used in production pricing or calibration.

---

## Exercises

**Exercise 1.**
For Heston parameters $\kappa = 2.0$, $\xi = 0.5$, $\rho = -0.7$, compute the complex discriminant $\gamma$ at $u = 5$. That is, evaluate $\alpha = \kappa - i\rho\xi u$ and $\gamma = \sqrt{\alpha^2 + \xi^2(iu + u^2)}$. Verify that $\text{Re}(\gamma) > 0$. If $\text{Re}(\gamma) < 0$, explain why flipping the sign to $-\gamma$ is valid and does not change $\gamma^2$.

---

**Exercise 2.**
Using the Albrecher formulation, compute the auxiliary ratio $g$ for $u = 10$, $\kappa = 2.0$, $\xi = 0.5$, $\rho = -0.7$. Verify that $|g| < 1$. Then compute $g$ using the original Heston (1993) formulation $\tilde{g} = 1/g$ and confirm that $|\tilde{g}| > 1$. Explain why $|\tilde{g}| > 1$ causes numerical instability for large $\tau$.

---

**Exercise 3.**
The Gil-Pelaez inversion uses the trapezoidal rule with $u_{\max} = 100$ and $N = 4096$. Compute the grid spacing $\Delta u$. Using the Heston parameters $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.5$, $\rho = -0.7$, $\tau = 1.0$, estimate the magnitude $|\varphi(u_{\max}, \tau)|$ by noting that $|\varphi(u)| \sim \exp(-c u^2 \tau)$ for large $u$ where $c \approx v_0/2$. Is $u_{\max} = 100$ sufficient to make the truncation error negligible?

---

**Exercise 4.**
The moment validation computes $\mathbb{E}[\ln S_T]$ both analytically and numerically via finite differences of the characteristic function. For $S_0 = 100$, $r = 3\%$, $q = 1\%$, $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.5$, $T = 1.0$, compute the analytical expected log-price:

$$
\mathbb{E}[\ln S_T] = \ln S_0 + (r - q)T - \frac{1}{2}\left[\theta T + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa}\right]
$$

---

**Exercise 5.**
The CF under the stock-price numeraire is obtained as $\varphi_1(u) = \varphi(u - i) / \varphi(-i)$. Explain why this measure change is necessary for the Gil-Pelaez decomposition $C = S_0 e^{-qT} P_1 - K e^{-rT} P_2$. Verify that $\varphi(-i) = \mathbb{E}[S_T / S_0]$ by substituting $u = -i$ into the CF definition $\varphi(u) = \mathbb{E}[e^{iu\ln S_T}]$ (with $\ln S_0$ already factored out from the forward term).

---

**Exercise 6.**
Suppose the CF engine produces a call price of $C = -0.02$ (negative) for a deep OTM call with $K = 200$, $S_0 = 100$, $T = 0.25$. This is clearly wrong. List three possible numerical causes: (a) branch-cut error, (b) integration truncation error, (c) insufficient grid resolution. For each, describe the diagnostic you would perform and the fix you would apply.

---

**Exercise 7.**
For calibration performance, the CF is evaluated at $N = 4096$ frequencies for each of 5 maturities per objective function evaluation. If the DE optimizer runs for 200 generations with population size 75, compute the total number of CF evaluations. Assuming each CF evaluation takes 0.5 microseconds (vectorized across frequencies), estimate the total compute time for CF evaluation alone. What fraction of the total calibration time does this represent if the full calibration takes 9 seconds?
