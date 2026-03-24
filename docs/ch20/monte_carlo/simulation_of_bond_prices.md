# Simulation of Bond Prices

In the Hull-White model, the zero-coupon bond price $P(t,T)$ is available in closed form as an exponential-affine function of the short rate $r_t$. This means that once we simulate a short rate path $\{r_{t_0}, r_{t_1}, \ldots, r_{t_N}\}$, we can compute the corresponding bond prices at every time step without additional simulation or discretization error. This section develops the machinery for computing $P(t_i, T)$ along simulated paths and shows how to use these path-wise bond prices for portfolio valuation and derivative pricing.

## Bond Price Along a Simulated Path

Recall from the bond pricing section that in the one-factor Hull-White model, the zero-coupon bond price takes the affine form

$$
P(t,T) = \exp\!\bigl(A(t,T) + B(t,T)\,r_t\bigr)
$$

where

$$
B(t,T) = \frac{e^{-\lambda(T-t)} - 1}{\lambda}
$$

and the function $A(t,T)$ is determined by the no-arbitrage condition to fit the initial market curve $P^M(0,T)$.

Given a simulated short rate value $r_{t_i}$ at time $t_i$, the bond price for any maturity $T > t_i$ is computed directly from this formula. There is no approximation involved: the affine structure gives the exact bond price conditional on $r_{t_i}$.

!!! tip "Key Advantage of Affine Models"
    Unlike general HJM models where bond prices require simulating the entire forward curve, affine short rate models such as Hull-White reduce bond price computation to evaluating a deterministic function of a single state variable $r_t$. This makes Monte Carlo simulation significantly more efficient.

## Path-Wise Bond Price Computation

Consider a time grid $0 = t_0 < t_1 < \cdots < t_N = T_{\max}$ and a set of maturities $T_1, T_2, \ldots, T_M$ at which we need bond prices. Along each simulated path $\omega$, the short rate trajectory $\{r_{t_0}(\omega), r_{t_1}(\omega), \ldots, r_{t_N}(\omega)\}$ is generated using exact simulation:

$$
r_{t_{i+1}} = r_{t_i}\,e^{-\lambda \Delta t} + \lambda \int_{t_i}^{t_{i+1}} \theta(s)\,e^{-\lambda(t_{i+1}-s)}\,ds + \sigma \int_{t_i}^{t_{i+1}} e^{-\lambda(t_{i+1}-s)}\,dW_s
$$

Since the stochastic integral is Gaussian with mean zero and variance $\frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda \Delta t})$, the transition is sampled exactly as

$$
r_{t_{i+1}} = \mu(t_i, t_{i+1}) + \sigma_r(t_i, t_{i+1})\,Z_{i+1}
$$

where $Z_{i+1} \sim N(0,1)$, $\mu(t_i, t_{i+1}) = r_{t_i}\,e^{-\lambda \Delta t} + \lambda \int_{t_i}^{t_{i+1}} \theta(s)\,e^{-\lambda(t_{i+1}-s)}\,ds$, and $\sigma_r^2(t_i, t_{i+1}) = \frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda \Delta t})$.

At each time step $t_i$ and for each required maturity $T_j > t_i$, the bond price is

$$
P(t_i, T_j) = \exp\!\bigl(A(t_i, T_j) + B(t_i, T_j)\,r_{t_i}\bigr)
$$

The functions $A(t_i, T_j)$ and $B(t_i, T_j)$ depend only on model parameters and the initial curve, so they can be precomputed before the simulation begins.

## Money Market Account

The discretely-compounded money market account along a simulated path is

$$
M(t_n) = \exp\!\left(\sum_{i=0}^{n-1} r_{t_i}\,\Delta t_i\right)
$$

where $\Delta t_i = t_{i+1} - t_i$. The discount factor from time $t_n$ back to time $0$ is $1/M(t_n)$.

For pricing a derivative with payoff $g$ at time $T$, the Monte Carlo estimator is

$$
\hat{V}_0 = \frac{1}{N_{\text{paths}}} \sum_{k=1}^{N_{\text{paths}}} \frac{g\bigl(r_T^{(k)}\bigr)}{M^{(k)}(T)}
$$

where the superscript $(k)$ indexes the simulated path.

## Yield Curve Simulation

A powerful application of path-wise bond price computation is simulating future yield curves. At a future time $t$, the yield for maturity $\tau$ is

$$
y(t, t+\tau) = -\frac{\ln P(t, t+\tau)}{\tau} = -\frac{A(t, t+\tau) + B(t, t+\tau)\,r_t}{\tau}
$$

Since all yields are affine functions of $r_t$, each simulated value of $r_t$ determines an entire yield curve. This produces parallel-shift-like movements: yield curves across different paths differ only through the realized value of $r_t$, a well-known limitation of one-factor models.

???+ example "Simulating Future Yield Curves"
    For each simulated path at time $t = 10$:

    1. Generate $r_{10}^{(k)}$ using the exact simulation scheme
    2. For each tenor $\tau \in \{0.25, 0.5, 1, 2, 5, 10, 20, 30\}$, compute $y^{(k)}(10, 10+\tau) = -[A(10, 10+\tau) + B(10, 10+\tau)\,r_{10}^{(k)}]/\tau$
    3. Plot the resulting yield curves to visualize the distribution of future term structures

## Consistency Check via Monte Carlo

The simulated bond prices must be consistent with the initial market curve. The Monte Carlo estimate of $P(0, T)$ using the money market account is

$$
\hat{P}(0, T) = \frac{1}{N_{\text{paths}}} \sum_{k=1}^{N_{\text{paths}}} \frac{1}{M^{(k)}(T)}
$$

By the risk-neutral pricing formula, $\hat{P}(0,T) \to P^M(0,T)$ as $N_{\text{paths}} \to \infty$. This provides a sanity check for the simulation implementation.

???+ example "Monte Carlo Bond Price vs Analytic Formula"
    ```python
    def main():
        hw = HullWhite(sigma=0.01, lambd=0.01, P=P_market)
        t, R, M = hw.generate_sample_paths(
            num_paths=20_000, num_steps=100, T=30, seed=42
        )

        dt = t[1] - t[0]
        T_grid = [1, 2, 5, 10, 20, 30]

        for T_i in T_grid:
            idx = int(T_i / dt)
            P_mc = np.mean(1.0 / M[:, idx])
            P_market_val = P_market(T_i)
            print(f"T={T_i:2d}: MC={P_mc:.6f}, Market={P_market_val:.6f}")
    ```

## Forward Bond Price Simulation

The forward bond price $F(t; T, S) = P(t, S) / P(t, T)$ for $t \leq T \leq S$ represents the price at time $T$ of a bond maturing at $S$, as seen from time $t$. Under the $T$-forward measure, $F(t; T, S)$ is a martingale.

Along a simulated path, the forward bond price is computed as

$$
F(t_i; T, S) = \frac{P(t_i, S)}{P(t_i, T)} = \exp\!\bigl([A(t_i, S) - A(t_i, T)] + [B(t_i, S) - B(t_i, T)]\,r_{t_i}\bigr)
$$

This quantity is useful for pricing forward-starting derivatives and for computing forward rates along paths.

## Two-Factor Bond Price Simulation

In the two-factor Hull-White model with $r_t = x_t + y_t + \varphi(t)$, the bond price depends on both state variables:

$$
P(t, T) = \exp\!\bigl(A^{(2)}(t,T) + B_x(t,T)\,x_t + B_y(t,T)\,y_t\bigr)
$$

where $B_x(t,T) = (e^{-\lambda_1(T-t)} - 1)/\lambda_1$ and $B_y(t,T) = (e^{-\lambda_2(T-t)} - 1)/\lambda_2$. Path-wise computation requires simulating both factors $(x_{t_i}, y_{t_i})$ at each time step, then evaluating the two-factor affine formula.

The two-factor model produces richer yield curve dynamics: different paths can exhibit not only parallel shifts but also twist and butterfly movements, since the two factors decay at different rates $\lambda_1$ and $\lambda_2$.

## Summary

Bond price simulation in the Hull-White model exploits the affine structure to compute exact bond prices at each simulated time step. The short rate path is generated using exact Gaussian transitions, and bond prices follow from the closed-form affine formula $P(t,T) = \exp(A(t,T) + B(t,T)\,r_t)$. Key applications include yield curve simulation, consistency verification against the initial market curve, and path-wise valuation of interest rate portfolios. The two-factor extension enriches the dynamics by introducing a second state variable while preserving the exponential-affine bond price structure.

---

## Exercises

**Exercise 1.** Given a simulated short rate value $r_{10} = 0.045$ at time $t = 10$, compute the bond price $P(10, 15)$ using the affine formula. Use $\lambda = 0.05$, $\sigma = 0.01$, and a flat market curve $P^M(0,T) = e^{-0.03T}$. Compute $B(10,15)$ and $A(10,15)$ explicitly.

---

**Exercise 2.** The yield $y(t,T) = -[A(t,T) + B(t,T)r_t]/(T-t)$ is affine in $r_t$. Show that the yield curve at time $t$ is fully determined by $r_t$ in the one-factor model. Why does this imply that all yield curve movements are parallel shifts? How is this different from the two-factor model?

---

**Exercise 3.** The Monte Carlo bond price estimator $\hat{P}(0,T) = \frac{1}{N_{\text{paths}}}\sum_{k=1}^{N_{\text{paths}}} 1/M^{(k)}(T)$ should equal $P^M(0,T)$. Explain why this is a necessary consistency check for the simulation. What are the most common implementation bugs that would cause this check to fail?

---

**Exercise 4.** The forward bond price $F(t;T,S) = P(t,S)/P(t,T) = \exp([A(t,S) - A(t,T)] + [B(t,S) - B(t,T)]r_t)$ is a martingale under the $T$-forward measure. Verify this property numerically by simulating paths and checking that $\mathbb{E}^{Q^T}[F(t;T,S)] = F(0;T,S)$ for several values of $t$.

---

**Exercise 5.** The money market account is computed as $M(t_n) = \exp(\sum_{i=0}^{n-1} r_{t_i}\Delta t_i)$. This uses a left-Riemann sum for $\int_0^{t_n} r(s)ds$. Compare this with the trapezoidal rule approximation. For a typical time step $\Delta t = 0.1$ years, estimate the order of the quadrature error.

---

**Exercise 6.** In the two-factor model, the bond price depends on two state variables: $P(t,T) = \exp(A^{(2)}(t,T) + B_x(t,T)x_t + B_y(t,T)y_t)$. Explain why this produces richer yield curve dynamics than the one-factor model. Describe the types of yield curve movements (parallel shift, twist, butterfly) that the two-factor model can generate.

---

**Exercise 7.** Precomputing $A(t_i, T_j)$ and $B(t_i, T_j)$ for all time steps $t_i$ and maturities $T_j$ before the simulation improves efficiency. For a simulation with $N = 100$ time steps and $M = 10$ maturities, how many values must be precomputed? Describe the memory and computational trade-offs.
