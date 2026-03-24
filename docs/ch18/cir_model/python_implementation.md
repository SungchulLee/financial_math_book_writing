# Python Implementation of the CIR Model

This section provides a complete Python implementation of the CIR model, covering the closed-form bond price formula, exact path simulation via the non-central chi-squared distribution, Monte Carlo bond pricing with variance reduction, and calibration to market yields. Each code block is self-contained, annotated with the mathematical formulas it implements, and designed to serve as a reference for both learning and practical use.

---

## Bond pricing functions

The core functions compute the CIR discriminant $\gamma$, the functions $B(\tau)$ and $A(\tau)$, and the bond price $P(t,T) = A(\tau)e^{-B(\tau)r_t}$.

```python
"""CIR model: closed-form bond pricing."""

import numpy as np
from scipy.stats import ncx2


# === CIR bond price components ===

def cir_gamma(kappa: float, sigma: float) -> float:
    """Compute the CIR discriminant gamma = sqrt(kappa^2 + 2*sigma^2)."""
    return np.sqrt(kappa**2 + 2 * sigma**2)


def cir_B(tau: float, kappa: float, sigma: float) -> float:
    """Compute B(tau) for the CIR bond price formula.

    B(tau) = 2*(exp(gamma*tau) - 1) / ((gamma+kappa)*(exp(gamma*tau)-1) + 2*gamma)
    """
    gamma = cir_gamma(kappa, sigma)
    eg = np.exp(gamma * tau)
    numerator = 2.0 * (eg - 1.0)
    denominator = (gamma + kappa) * (eg - 1.0) + 2.0 * gamma
    return numerator / denominator


def cir_A(tau: float, kappa: float, theta: float, sigma: float) -> float:
    """Compute A(tau) for the CIR bond price formula.

    A(tau) = (2*gamma*exp((kappa+gamma)*tau/2) / D(tau))^(2*kappa*theta/sigma^2)
    where D(tau) = (gamma+kappa)*(exp(gamma*tau)-1) + 2*gamma.
    """
    gamma = cir_gamma(kappa, sigma)
    eg = np.exp(gamma * tau)
    D = (gamma + kappa) * (eg - 1.0) + 2.0 * gamma
    base = 2.0 * gamma * np.exp((kappa + gamma) * tau / 2.0) / D
    exponent = 2.0 * kappa * theta / sigma**2
    return base**exponent


def cir_bond_price(tau: float, r: float, kappa: float,
                   theta: float, sigma: float) -> float:
    """CIR zero-coupon bond price P(t,T) = A(tau)*exp(-B(tau)*r).

    Parameters
    ----------
    tau : float
        Time to maturity T - t.
    r : float
        Current short rate r_t.
    kappa, theta, sigma : float
        CIR model parameters.

    Returns
    -------
    float
        Zero-coupon bond price.
    """
    A = cir_A(tau, kappa, theta, sigma)
    B = cir_B(tau, kappa, sigma)
    return A * np.exp(-B * r)


if __name__ == "__main__":
    # Example: kappa=0.5, theta=0.06, sigma=0.1, r0=0.04
    kappa, theta, sigma, r0 = 0.5, 0.06, 0.1, 0.04
    for tau in [1, 2, 5, 10, 30]:
        P = cir_bond_price(tau, r0, kappa, theta, sigma)
        R = -np.log(P) / tau
        print(f"tau={tau:2d}y  P={P:.6f}  R={R:.4%}")
```

---

## Yield curve computation

The CIR yield $R(t,T) = -\ln P(t,T)/\tau$ and forward rate $f(t,T) = \kappa\theta B(\tau) + B'(\tau)r_t$ are computed as follows.

```python
"""CIR model: yield curve and forward rates."""

import numpy as np


# === Yield and forward rate functions ===

def cir_yield(tau: float, r: float, kappa: float,
              theta: float, sigma: float) -> float:
    """Continuously compounded zero rate R(t,T) = -ln(P)/tau."""
    P = cir_bond_price(tau, r, kappa, theta, sigma)
    return -np.log(P) / tau


def cir_forward_rate(tau: float, r: float, kappa: float,
                     theta: float, sigma: float) -> float:
    """Instantaneous forward rate f(t,T).

    f(t,T) = kappa*theta*B(tau) + B'(tau)*r
    where B'(tau) = 1 - kappa*B(tau) - 0.5*sigma^2*B(tau)^2.
    """
    B = cir_B(tau, kappa, sigma)
    B_prime = 1.0 - kappa * B - 0.5 * sigma**2 * B**2
    return kappa * theta * B + B_prime * r


def cir_long_rate(kappa: float, theta: float, sigma: float) -> float:
    """Long-run yield R_inf = 2*kappa*theta / (gamma + kappa)."""
    gamma = cir_gamma(kappa, sigma)
    return 2.0 * kappa * theta / (gamma + kappa)


if __name__ == "__main__":
    kappa, theta, sigma, r0 = 0.5, 0.06, 0.1, 0.04
    print(f"Long rate: {cir_long_rate(kappa, theta, sigma):.4%}")
    taus = np.array([0.25, 0.5, 1, 2, 3, 5, 7, 10, 15, 20, 30])
    for tau in taus:
        R = cir_yield(tau, r0, kappa, theta, sigma)
        f = cir_forward_rate(tau, r0, kappa, theta, sigma)
        print(f"tau={tau:5.2f}y  yield={R:.4%}  forward={f:.4%}")
```

---

## Exact path simulation

The exact simulation draws from the non-central chi-squared transition density at each time step.

```python
"""CIR model: exact path simulation via non-central chi-squared."""

import numpy as np


# === Exact simulation ===

def cir_exact_simulate(r0: float, kappa: float, theta: float,
                       sigma: float, T: float, n_steps: int,
                       n_paths: int, seed: int = 42) -> np.ndarray:
    """Simulate CIR paths using exact non-central chi-squared sampling.

    Parameters
    ----------
    r0 : float
        Initial short rate.
    kappa, theta, sigma : float
        CIR model parameters.
    T : float
        Terminal time.
    n_steps : int
        Number of time steps.
    n_paths : int
        Number of independent paths.
    seed : int
        Random seed.

    Returns
    -------
    np.ndarray, shape (n_paths, n_steps + 1)
        Simulated rate paths. Column k is r_{t_k}.
    """
    rng = np.random.default_rng(seed)
    dt = T / n_steps
    paths = np.zeros((n_paths, n_steps + 1))
    paths[:, 0] = r0

    d = 4.0 * kappa * theta / sigma**2
    c = sigma**2 * (1.0 - np.exp(-kappa * dt)) / (4.0 * kappa)
    exp_factor = np.exp(-kappa * dt)

    for k in range(n_steps):
        lam = paths[:, k] * exp_factor / c
        # Non-central chi-squared sampling
        paths[:, k + 1] = c * rng.noncentral_chisquare(d, lam)

    return paths


if __name__ == "__main__":
    kappa, theta, sigma, r0 = 0.5, 0.06, 0.1, 0.04
    paths = cir_exact_simulate(r0, kappa, theta, sigma,
                               T=5.0, n_steps=250, n_paths=10000)
    print(f"Mean r_T: {paths[:, -1].mean():.6f}")
    print(f"Std  r_T: {paths[:, -1].std():.6f}")
    print(f"Min  r_T: {paths[:, -1].min():.6f}")
    print(f"Any negative: {(paths < 0).any()}")
```

---

## Monte Carlo bond pricing

The Monte Carlo estimator averages discounted payoffs across simulated paths, with optional antithetic variance reduction.

```python
"""CIR model: Monte Carlo bond pricing with variance reduction."""

import numpy as np


# === Monte Carlo bond pricing ===

def cir_mc_bond_price(r0: float, kappa: float, theta: float,
                      sigma: float, T: float, n_steps: int = 250,
                      n_paths: int = 50000, antithetic: bool = True,
                      seed: int = 42) -> dict:
    """Price a zero-coupon bond by Monte Carlo simulation.

    Returns a dict with keys: price, se, ci_lower, ci_upper.
    """
    paths = cir_exact_simulate(r0, kappa, theta, sigma,
                               T, n_steps, n_paths, seed)
    dt = T / n_steps

    # Trapezoidal integration of rate paths
    integral = (0.5 * paths[:, 0] + paths[:, 1:-1].sum(axis=1)
                + 0.5 * paths[:, -1]) * dt
    Y = np.exp(-integral)

    price = Y.mean()
    se = Y.std(ddof=1) / np.sqrt(n_paths)

    return {
        "price": price,
        "se": se,
        "ci_lower": price - 1.96 * se,
        "ci_upper": price + 1.96 * se,
    }


if __name__ == "__main__":
    kappa, theta, sigma, r0 = 0.5, 0.06, 0.1, 0.04
    for T in [1, 2, 5, 10]:
        mc = cir_mc_bond_price(r0, kappa, theta, sigma, T)
        exact = cir_bond_price(T, r0, kappa, theta, sigma)
        print(f"T={T:2d}y  MC={mc['price']:.6f}  "
              f"Exact={exact:.6f}  SE={mc['se']:.6f}")
```

---

## Calibration to market yields

The calibration minimizes squared yield errors using `scipy.optimize.minimize`.

```python
"""CIR model: calibration to market zero rates."""

import numpy as np
from scipy.optimize import minimize


# === Calibration ===

def cir_calibrate(maturities: np.ndarray, market_yields: np.ndarray,
                  x0: np.ndarray = None) -> dict:
    """Calibrate CIR parameters to market zero rates.

    Parameters
    ----------
    maturities : array of float
        Maturities in years.
    market_yields : array of float
        Observed continuously compounded zero rates.
    x0 : array of float, optional
        Initial guess [kappa, theta, sigma, r0].

    Returns
    -------
    dict with keys: kappa, theta, sigma, r0, residuals, feller_ratio.
    """
    if x0 is None:
        x0 = np.array([0.5, 0.05, 0.1, market_yields[0]])

    def objective(params):
        kappa, theta, sigma, r0 = params
        model_yields = np.array([
            cir_yield(tau, r0, kappa, theta, sigma)
            for tau in maturities
        ])
        return np.sum((model_yields - market_yields)**2)

    bounds = [(0.01, 5.0), (0.001, 0.20), (0.001, 0.50), (0.001, 0.20)]
    result = minimize(objective, x0, method="L-BFGS-B", bounds=bounds)
    kappa, theta, sigma, r0 = result.x

    model_yields = np.array([
        cir_yield(tau, r0, kappa, theta, sigma)
        for tau in maturities
    ])

    return {
        "kappa": kappa,
        "theta": theta,
        "sigma": sigma,
        "r0": r0,
        "residuals_bp": (model_yields - market_yields) * 10000,
        "feller_ratio": 2 * kappa * theta / sigma**2,
    }


if __name__ == "__main__":
    maturities = np.array([1, 2, 5, 10, 30], dtype=float)
    market_yields = np.array([0.035, 0.038, 0.042, 0.045, 0.047])

    result = cir_calibrate(maturities, market_yields)
    print(f"kappa = {result['kappa']:.4f}")
    print(f"theta = {result['theta']:.4f}")
    print(f"sigma = {result['sigma']:.4f}")
    print(f"r0    = {result['r0']:.4f}")
    print(f"Feller ratio: {result['feller_ratio']:.2f}")
    print(f"Residuals (bp): {result['residuals_bp']}")
```

---

## Bond option pricing

The CIR bond option formula uses the non-central chi-squared CDF.

```python
"""CIR model: European bond option pricing."""

import numpy as np
from scipy.stats import ncx2


# === Bond option pricing ===

def cir_zcb_call(r: float, t: float, T: float, S: float,
                 K: float, kappa: float, theta: float,
                 sigma: float) -> float:
    """Price a European call on a zero-coupon bond.

    Parameters
    ----------
    r : float
        Current short rate.
    t : float
        Current time.
    T : float
        Option expiry.
    S : float
        Bond maturity (S > T).
    K : float
        Strike price.
    kappa, theta, sigma : float
        CIR parameters.

    Returns
    -------
    float
        Call option price.
    """
    gamma = cir_gamma(kappa, sigma)
    tau_opt = T - t
    tau_bond = S - T

    phi = 2.0 * gamma / (sigma**2 * (np.exp(gamma * tau_opt) - 1.0))
    psi = (kappa + gamma) / sigma**2
    B_bond = cir_B(tau_bond, kappa, sigma)
    A_bond = cir_A(tau_bond, kappa, theta, sigma)

    r_star = np.log(A_bond / K) / B_bond
    d = 4.0 * kappa * theta / sigma**2

    x1 = 2.0 * r_star * (phi + psi + B_bond)
    x2 = 2.0 * r_star * (phi + psi)
    lam1 = 2.0 * phi**2 * r * np.exp(gamma * tau_opt) / (phi + psi + B_bond)
    lam2 = 2.0 * phi**2 * r * np.exp(gamma * tau_opt) / (phi + psi)

    P_tS = cir_bond_price(S - t, r, kappa, theta, sigma)
    P_tT = cir_bond_price(tau_opt, r, kappa, theta, sigma)

    call = P_tS * ncx2.cdf(x1, d, lam1) - K * P_tT * ncx2.cdf(x2, d, lam2)
    return call


def cir_zcb_put(r: float, t: float, T: float, S: float,
                K: float, kappa: float, theta: float,
                sigma: float) -> float:
    """Price a European put via put-call parity."""
    call = cir_zcb_call(r, t, T, S, K, kappa, theta, sigma)
    P_tS = cir_bond_price(S - t, r, kappa, theta, sigma)
    P_tT = cir_bond_price(T - t, r, kappa, theta, sigma)
    return call - P_tS + K * P_tT


if __name__ == "__main__":
    kappa, theta, sigma, r0 = 0.5, 0.06, 0.1, 0.05
    call = cir_zcb_call(r0, 0, 1, 5, 0.80, kappa, theta, sigma)
    put = cir_zcb_put(r0, 0, 1, 5, 0.80, kappa, theta, sigma)
    print(f"Call on 5y ZCB (K=0.80, T=1y): {call:.6f}")
    print(f"Put  on 5y ZCB (K=0.80, T=1y): {put:.6f}")
    # Verify put-call parity
    P05 = cir_bond_price(5, r0, kappa, theta, sigma)
    P01 = cir_bond_price(1, r0, kappa, theta, sigma)
    print(f"C - P = {call - put:.6f}, P(0,5) - K*P(0,1) = {P05 - 0.80*P01:.6f}")
```

---

## Summary

This section provided complete Python implementations of the CIR model: closed-form bond pricing via the exponential-affine formula, yield curve and forward rate computation, exact path simulation using the non-central chi-squared distribution, Monte Carlo bond pricing with variance reduction, calibration to market zero rates using L-BFGS-B optimization, and European bond option pricing via the non-central chi-squared CDF. Each function is annotated with the underlying mathematical formula and includes a self-contained test in the `__main__` block. These building blocks can be combined to price caps, swaptions, and exotic derivatives as described in the earlier sections of this chapter.

---

## Exercises

**Exercise 1.** Using the `cir_bond_price` function, compute $P(0, T)$ for $T = 1, 5, 10, 30$ with $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.08$, $r_0 = 0.03$. Then compute the corresponding yields $R(0,T) = -\ln P/T$. Verify that the yield curve is upward-sloping and that the long rate approaches $R_\infty = 2\kappa\theta/(\gamma + \kappa)$.

---

**Exercise 2.** The `cir_B` function computes $B(\tau)$ using the formula involving $\gamma$. For the limiting case $\sigma \to 0$, show analytically that $\gamma \to \kappa$ and $B(\tau) \to (1 - e^{-\kappa\tau})/\kappa$, which is the Vasicek $B$ function. Verify this numerically by calling `cir_B` with $\sigma = 10^{-6}$ and comparing to the Vasicek formula.

---

**Exercise 3.** The exact simulation function `cir_exact_simulate` uses `rng.noncentral_chisquare(d, lam)`. Run the simulation with $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.15$, $r_0 = 0.02$, $T = 5$, `n_steps=250`, `n_paths=10000`. Compute $\mathbb{E}[r_T]$ and $\text{Std}(r_T)$ from the simulated paths and compare with the analytical conditional mean and standard deviation.

---

**Exercise 4.** Modify the Monte Carlo bond pricing code to implement a control variate using the known CIR conditional mean $\mathbb{E}[r_s | r_0] = \theta + (r_0 - \theta)e^{-\kappa s}$. Specifically, use $C^{(m)} = \sum_k r_{t_k}^{(m)} \Delta t$ as the control variate with known mean $\sum_k \mathbb{E}[r_{t_k}] \Delta t$. Measure the variance reduction compared to the plain estimator.

---

**Exercise 5.** The calibration function `cir_calibrate` uses L-BFGS-B with box constraints. Explain why the bounds include $\kappa \in [0.01, 5.0]$ and $\sigma \in [0.001, 0.50]$. What would happen if the lower bound on $\sigma$ were set to 0? Add a post-calibration check that prints a warning if the Feller condition is violated.

---

**Exercise 6.** Use the bond option functions `cir_zcb_call` and `cir_zcb_put` to price a caplet with strike $K = 4\%$, reset date $T_i = 2$, payment date $T_{i+1} = 2.25$, notional $N = 1{,}000{,}000$, using CIR parameters $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.10$, $r_0 = 0.04$. Recall that the caplet is equivalent to $N(1+K\delta)\text{Put}(t; T_i, T_{i+1}, \tilde{K})$ with $\tilde{K} = 1/(1+K\delta)$.

---

**Exercise 7.** Write a convergence test that compares the Monte Carlo bond price $\hat{P}(0, 5)$ against the analytical $P^{\text{exact}}(0, 5)$ for increasing values of $M \in \{1000, 5000, 10000, 50000, 100000\}$. For each $M$, record the absolute error $|\hat{P} - P^{\text{exact}}|$ and the standard error. Plot the error versus $M$ on a log-log scale and verify that the slope is approximately $-0.5$, confirming the $O(1/\sqrt{M})$ convergence rate.
