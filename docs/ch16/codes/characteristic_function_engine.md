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

??? success "Solution to Exercise 1"
    Given $\kappa = 2.0$, $\xi = 0.5$, $\rho = -0.7$, and $u = 5$, compute:

    $$
    \alpha = \kappa - i\rho\xi u = 2.0 - i(-0.7)(0.5)(5) = 2.0 + 1.75i
    $$

    Next compute $\alpha^2$:

    $$
    \alpha^2 = (2.0 + 1.75i)^2 = 4.0 + 7.0i - 3.0625 = 0.9375 + 7.0i
    $$

    The quadratic term in $u$:

    $$
    \beta = iu + u^2 = 5i + 25
    $$

    $$
    \xi^2 \beta = 0.25(25 + 5i) = 6.25 + 1.25i
    $$

    The argument of the square root:

    $$
    \alpha^2 + \xi^2\beta = (0.9375 + 7.0i) + (6.25 + 1.25i) = 7.1875 + 8.25i
    $$

    To compute $\gamma = \sqrt{7.1875 + 8.25i}$, write $z = 7.1875 + 8.25i$ in polar form:

    $$
    |z| = \sqrt{7.1875^2 + 8.25^2} = \sqrt{51.660 + 68.0625} = \sqrt{119.723} \approx 10.942
    $$

    $$
    \arg(z) = \arctan(8.25 / 7.1875) \approx 0.853 \text{ rad}
    $$

    $$
    \gamma = \sqrt{|z|} \cdot e^{i\arg(z)/2} = \sqrt{10.942} \cdot e^{i \cdot 0.4265} \approx 3.308 \cdot (\cos 0.4265 + i\sin 0.4265)
    $$

    $$
    \gamma \approx 3.308(0.9099 + 0.4147i) \approx 3.010 + 1.372i
    $$

    Since $\text{Re}(\gamma) \approx 3.010 > 0$, no sign flip is needed.

    **Why flipping to $-\gamma$ is valid:** The discriminant $\gamma$ is defined as a square root, so $\gamma$ and $-\gamma$ both satisfy $\gamma^2 = \alpha^2 + \xi^2\beta$. Squaring $-\gamma$ gives $(-\gamma)^2 = \gamma^2$, so the quadratic equation is unchanged. The Albrecher formulation requires $\text{Re}(\gamma) > 0$ to ensure $|g| < 1$; flipping the sign when $\text{Re}(\gamma) < 0$ simply selects the correct branch of the square root without altering the underlying Riccati solution.

---

**Exercise 2.**
Using the Albrecher formulation, compute the auxiliary ratio $g$ for $u = 10$, $\kappa = 2.0$, $\xi = 0.5$, $\rho = -0.7$. Verify that $|g| < 1$. Then compute $g$ using the original Heston (1993) formulation $\tilde{g} = 1/g$ and confirm that $|\tilde{g}| > 1$. Explain why $|\tilde{g}| > 1$ causes numerical instability for large $\tau$.

??? success "Solution to Exercise 2"
    With $u = 10$, $\kappa = 2.0$, $\xi = 0.5$, $\rho = -0.7$:

    $$
    \alpha = \kappa - i\rho\xi u = 2.0 - i(-0.7)(0.5)(10) = 2.0 + 3.5i
    $$

    $$
    \alpha^2 = (2.0 + 3.5i)^2 = 4.0 + 14.0i - 12.25 = -8.25 + 14.0i
    $$

    $$
    \xi^2(iu + u^2) = 0.25(10i + 100) = 25.0 + 2.5i
    $$

    $$
    \alpha^2 + \xi^2\beta = 16.75 + 16.5i
    $$

    $$
    |z| = \sqrt{16.75^2 + 16.5^2} = \sqrt{280.5625 + 272.25} = \sqrt{552.8125} \approx 23.511
    $$

    $$
    \gamma = \sqrt{23.511} \cdot e^{i\arctan(16.5/16.75)/2} \approx 4.849 \cdot e^{i \cdot 0.3916}
    $$

    $$
    \gamma \approx 4.849(0.9241 + 0.3822i) \approx 4.481 + 1.853i
    $$

    The auxiliary ratio $g$ (Albrecher formulation):

    $$
    g = \frac{\alpha - \gamma}{\alpha + \gamma} = \frac{(2.0 + 3.5i) - (4.481 + 1.853i)}{(2.0 + 3.5i) + (4.481 + 1.853i)} = \frac{-2.481 + 1.647i}{6.481 + 5.353i}
    $$

    Computing the magnitude:

    $$
    |g| = \frac{|\alpha - \gamma|}{|\alpha + \gamma|} = \frac{\sqrt{2.481^2 + 1.647^2}}{\sqrt{6.481^2 + 5.353^2}} = \frac{\sqrt{6.155 + 2.713}}{\sqrt{42.003 + 28.654}} = \frac{\sqrt{8.868}}{\sqrt{70.657}} = \frac{2.978}{8.406} \approx 0.354
    $$

    Indeed $|g| \approx 0.354 < 1$, confirming the Albrecher formulation's stability property.

    For the original Heston (1993) formulation, $\tilde{g} = 1/g$:

    $$
    |\tilde{g}| = 1/|g| \approx 1/0.354 \approx 2.825 > 1
    $$

    **Why $|\tilde{g}| > 1$ causes instability:** In the original formulation, the $C$ function contains a term involving $\ln(1 - \tilde{g} e^{+\gamma\tau})$. Since $|\tilde{g}| > 1$ and $|e^{+\gamma\tau}| = e^{\text{Re}(\gamma)\tau}$ grows exponentially, the product $\tilde{g} e^{+\gamma\tau}$ has magnitude $|\tilde{g}| \cdot e^{\text{Re}(\gamma)\tau}$, which grows without bound as $\tau$ increases. The argument of the logarithm $1 - \tilde{g} e^{+\gamma\tau}$ will eventually cross the negative real axis (the branch cut of the complex logarithm), causing a $2\pi i$ discontinuity in $C(u, \tau)$. This discontinuity corrupts the Fourier integral, producing incorrect option prices. By contrast, the Albrecher term $1 - g e^{-\gamma\tau}$ involves a decaying exponential ($|g e^{-\gamma\tau}| \to 0$ as $\tau \to \infty$), so the logarithm argument remains safely away from the branch cut.

---

**Exercise 3.**
The Gil-Pelaez inversion uses the trapezoidal rule with $u_{\max} = 100$ and $N = 4096$. Compute the grid spacing $\Delta u$. Using the Heston parameters $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.5$, $\rho = -0.7$, $\tau = 1.0$, estimate the magnitude $|\varphi(u_{\max}, \tau)|$ by noting that $|\varphi(u)| \sim \exp(-c u^2 \tau)$ for large $u$ where $c \approx v_0/2$. Is $u_{\max} = 100$ sufficient to make the truncation error negligible?

??? success "Solution to Exercise 3"
    The grid spacing is:

    $$
    \Delta u = \frac{u_{\max}}{N} = \frac{100}{4096} \approx 0.02441
    $$

    To estimate $|\varphi(u_{\max}, \tau)|$ at $u_{\max} = 100$, use the asymptotic decay $|\varphi(u)| \sim \exp(-c u^2 \tau)$ where $c \approx v_0 / 2 = 0.02$:

    $$
    |\varphi(100, 1.0)| \approx \exp(-0.02 \times 100^2 \times 1.0) = \exp(-200) \approx 1.38 \times 10^{-87}
    $$

    This is astronomically small---far below machine epsilon ($\approx 10^{-16}$). The characteristic function has effectively decayed to zero long before $u = 100$.

    A more refined estimate of the effective decay rate: for the Heston model, the CF decays as $|\varphi(u)| \sim \exp(-\bar{v}\tau u^2 / 2)$ where $\bar{v}$ is an average variance. With $v_0 = \theta = 0.04$ and $\tau = 1$:

    $$
    |\varphi(u)| \approx \exp(-0.04 \times 1.0 \times u^2 / 2) = \exp(-0.02 u^2)
    $$

    The integrand becomes negligible (below $10^{-16}$) when $0.02 u^2 > 36.8$, i.e., $u > 42.9$. So $u_{\max} = 100$ provides a very generous margin---the truncation error is essentially zero. Even $u_{\max} = 50$ would be more than sufficient for these parameters.

    The conclusion: $u_{\max} = 100$ is far more than sufficient, making the truncation error negligible compared to other error sources (discretization, machine precision).

---

**Exercise 4.**
The moment validation computes $\mathbb{E}[\ln S_T]$ both analytically and numerically via finite differences of the characteristic function. For $S_0 = 100$, $r = 3\%$, $q = 1\%$, $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.5$, $T = 1.0$, compute the analytical expected log-price:

$$
\mathbb{E}[\ln S_T] = \ln S_0 + (r - q)T - \frac{1}{2}\left[\theta T + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa}\right]
$$

??? success "Solution to Exercise 4"
    Given $S_0 = 100$, $r = 0.03$, $q = 0.01$, $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.04$, $T = 1.0$:

    $$
    \mathbb{E}[\ln S_T] = \ln S_0 + (r - q)T - \frac{1}{2}\left[\theta T + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa}\right]
    $$

    Compute each piece:

    $$
    \ln S_0 = \ln 100 = 4.60517
    $$

    $$
    (r - q)T = (0.03 - 0.01)(1.0) = 0.02
    $$

    For the variance integral term, since $v_0 = \theta = 0.04$:

    $$
    v_0 - \theta = 0
    $$

    So the second term in the bracket vanishes:

    $$
    \theta T + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa} = 0.04 \times 1.0 + 0 = 0.04
    $$

    Therefore:

    $$
    \mathbb{E}[\ln S_T] = 4.60517 + 0.02 - \frac{1}{2}(0.04) = 4.60517 + 0.02 - 0.02 = 4.60517
    $$

    The expected log-price equals $\ln S_0 = 4.60517$.

    This result is intuitive: since $v_0 = \theta$ (variance starts at its long-run level), the average integrated variance over $[0, T]$ is exactly $\theta T = 0.04$. The drift $(r - q)T = 0.02$ is exactly offset by the volatility drag $-\frac{1}{2}\bar{v}T = -0.02$. In the special case $v_0 = \theta$, the expected log-price is independent of $\kappa$, $\xi$, and $\rho$---these parameters affect higher moments but not the mean.

---

**Exercise 5.**
The CF under the stock-price numeraire is obtained as $\varphi_1(u) = \varphi(u - i) / \varphi(-i)$. Explain why this measure change is necessary for the Gil-Pelaez decomposition $C = S_0 e^{-qT} P_1 - K e^{-rT} P_2$. Verify that $\varphi(-i) = \mathbb{E}[S_T / S_0]$ by substituting $u = -i$ into the CF definition $\varphi(u) = \mathbb{E}[e^{iu\ln S_T}]$ (with $\ln S_0$ already factored out from the forward term).

??? success "Solution to Exercise 5"
    The characteristic function is defined as $\varphi(u) = \mathbb{E}[e^{iu\ln S_T}]$. Substituting $u = -i$:

    $$
    \varphi(-i) = \mathbb{E}[e^{i(-i)\ln S_T}] = \mathbb{E}[e^{\ln S_T}] = \mathbb{E}[S_T]
    $$

    Under the risk-neutral measure, $\mathbb{E}[S_T] = S_0 e^{(r-q)T}$, so:

    $$
    \varphi(-i) = S_0 e^{(r-q)T} = \mathbb{E}[S_T]
    $$

    Therefore $\varphi(-i) / S_0 = e^{(r-q)T} = \mathbb{E}[S_T/S_0]$.

    **Why the measure change is necessary:** The Gil-Pelaez decomposition writes the call price as:

    $$
    C = S_0 e^{-qT} P_1 - K e^{-rT} P_2
    $$

    Here $P_2 = \mathbb{Q}(S_T > K)$ is the exercise probability under the money-market numeraire (the usual risk-neutral measure), and $P_1 = \mathbb{Q}^S(S_T > K)$ is the exercise probability under the **stock-price numeraire**. Under the stock-price numeraire, the Radon–Nikodym derivative is:

    $$
    \frac{d\mathbb{Q}^S}{d\mathbb{Q}} = \frac{S_T}{S_0 e^{(r-q)T}} = \frac{S_T}{\mathbb{E}[S_T]}
    $$

    The CF under $\mathbb{Q}^S$ is:

    $$
    \varphi_1(u) = \mathbb{E}^{\mathbb{Q}^S}[e^{iu\ln S_T}] = \frac{\mathbb{E}^{\mathbb{Q}}[e^{iu\ln S_T} \cdot S_T]}{\mathbb{E}^{\mathbb{Q}}[S_T]} = \frac{\mathbb{E}[e^{i(u-i)\ln S_T}]}{\mathbb{E}[e^{\ln S_T}]} = \frac{\varphi(u - i)}{\varphi(-i)}
    $$

    This confirms the formula $\varphi_1(u) = \varphi(u - i) / \varphi(-i)$. The measure change is essential because the first term in the call price ($S_0 e^{-qT} P_1$) involves the **conditional expectation of $S_T$ given exercise**, which is naturally expressed as a probability under the stock numeraire. Without this decomposition, one would need to evaluate $\mathbb{E}[S_T \cdot \mathbf{1}_{S_T > K}]$ directly, which does not factor into a CF-based probability.

---

**Exercise 6.**
Suppose the CF engine produces a call price of $C = -0.02$ (negative) for a deep OTM call with $K = 200$, $S_0 = 100$, $T = 0.25$. This is clearly wrong. List three possible numerical causes: (a) branch-cut error, (b) integration truncation error, (c) insufficient grid resolution. For each, describe the diagnostic you would perform and the fix you would apply.

??? success "Solution to Exercise 6"
    A negative price $C = -0.02$ for a deep OTM call is impossible. Three numerical causes and their diagnostics:

    **(a) Branch-cut error:**

    If the CF implementation uses the original Heston (1993) formulation (with $|\tilde{g}| > 1$), the complex logarithm in $C(u, \tau)$ may cross its branch cut for certain frequencies $u$, introducing $2\pi i$ discontinuities. These corrupt the Fourier integrand, causing it to oscillate violently and integrate to a wrong (possibly negative) value.

    **Diagnostic:** Evaluate the CF at fine frequency resolution and plot $\text{Re}[\varphi(u)]$ and $\text{Im}[\varphi(u)]$. A branch-cut error manifests as a sudden jump in $\text{Im}[\varphi]$. Alternatively, compare the implementation against the Albrecher formulation.

    **Fix:** Switch to the Albrecher formulation with $\text{Re}(\gamma) > 0$ enforced. This eliminates all branch-cut issues.

    **(b) Integration truncation error:**

    For deep OTM options ($K = 200$, $S_0 = 100$, $T = 0.25$), the true price is extremely small (sub-penny). The Gil-Pelaez integrand $\text{Re}[e^{-iu\ln K}\varphi(u)/(iu)]$ oscillates rapidly because $\ln K = \ln 200 \approx 5.30$ is large. If $u_{\max}$ is too small, the truncated integral misses cancellations in the oscillating tail, yielding a biased result.

    **Diagnostic:** Increase $u_{\max}$ from 100 to 500 and compare results. If the price changes sign, truncation is the issue. Also check whether $|\varphi(u_{\max})|$ is already negligible.

    **Fix:** For deep OTM options, increase $u_{\max}$ or switch to the COS method, which handles the truncation more gracefully through its interval selection.

    **(c) Insufficient grid resolution:**

    With $N = 4096$ and $u_{\max} = 100$, the spacing $\Delta u \approx 0.024$ may be too coarse to capture the rapid oscillation of $e^{-iu\ln K}$ for large $\ln K$. The Nyquist sampling condition requires $\Delta u < \pi / \ln K \approx \pi / 5.30 \approx 0.593$, which is satisfied. However, for accuracy in the trapezoidal rule, much finer spacing may be needed.

    **Diagnostic:** Double $N$ to 8192 and compare results. If the price stabilizes, grid resolution was insufficient.

    **Fix:** Increase $N$ or use adaptive quadrature. Alternatively, apply the **Lewis (2001)** formulation, which reduces the oscillation by centering the integration around the forward moneyness.

    For this specific case ($K = 200$, $S_0 = 100$, $T = 0.25$), the true call price is extremely small (likely below $10^{-6}$). At this level, all three error sources can produce errors larger than the true price. The practical recommendation: use the COS method for individual deep OTM options, or price the corresponding put via the Fourier method and recover the call via put-call parity.

---

**Exercise 7.**
For calibration performance, the CF is evaluated at $N = 4096$ frequencies for each of 5 maturities per objective function evaluation. If the DE optimizer runs for 200 generations with population size 75, compute the total number of CF evaluations. Assuming each CF evaluation takes 0.5 microseconds (vectorized across frequencies), estimate the total compute time for CF evaluation alone. What fraction of the total calibration time does this represent if the full calibration takes 9 seconds?

??? success "Solution to Exercise 7"
    **Total CF evaluations:**

    At each objective function evaluation, the CF is evaluated at $N = 4096$ frequencies for each of 5 maturities:

    $$
    N_{\text{CF per eval}} = 5 \times 4096 = 20{,}480
    $$

    The DE optimizer with population size 75 and 200 generations performs:

    $$
    N_{\text{eval}} = 75 \times (200 + 1) = 15{,}075 \text{ evaluations}
    $$

    (Including the initial population.) Total CF evaluations:

    $$
    N_{\text{CF total}} = 15{,}075 \times 20{,}480 = 308{,}736{,}000 \approx 3.09 \times 10^8
    $$

    **Compute time for CF evaluation:**

    The 0.5 microsecond figure is per frequency **within a vectorized batch**, so the relevant measure is per-maturity per-evaluation: one batch of 4096 CF evaluations takes $4096 \times 0.5\mu s = 2.048$ ms. Actually, with vectorization, the cost is better measured per batch. Assuming 0.5 $\mu$s per element:

    $$
    t_{\text{CF total}} = 3.09 \times 10^8 \times 0.5 \times 10^{-6} \text{ s} = 154.4 \text{ s}
    $$

    However, this is the serial cost. With NumPy vectorization, the $N = 4096$ evaluations per maturity are performed as a single array operation, reducing the effective per-element cost. A more realistic estimate accounts for the fact that vectorized NumPy operations achieve throughput of roughly $4096 / 0.1\text{ms} = 4 \times 10^7$ CF evaluations per second. Then:

    $$
    t_{\text{CF total}} \approx \frac{3.09 \times 10^8}{4 \times 10^7} \approx 7.7 \text{ s}
    $$

    **Fraction of total calibration time:**

    If the full calibration takes 9 seconds:

    $$
    \text{CF fraction} \approx \frac{7.7}{9} \approx 85\%
    $$

    The CF evaluation dominates calibration cost. The remaining 15% accounts for FFT computation (in the Carr-Madan method), objective function overhead (weight computation, sum of squared residuals), and DE bookkeeping (population management, mutation, crossover). This confirms that optimizing the CF evaluation---through vectorization, caching, and possibly GPU acceleration---is the highest-impact performance improvement for the calibration pipeline.
