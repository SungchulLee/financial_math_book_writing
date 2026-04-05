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

??? success "Solution to Exercise 1"
    With $\lambda = 0.05$, $\sigma = 0.01$, flat market curve $P^M(0,T) = e^{-0.03T}$, $r_{10} = 0.045$, $t = 10$, $T = 15$:

    **Computing $B(10, 15)$:**

    $$
    B(10, 15) = \frac{e^{-\lambda(T-t)} - 1}{\lambda} = \frac{e^{-0.05 \times 5} - 1}{0.05} = \frac{e^{-0.25} - 1}{0.05} = \frac{0.77880 - 1}{0.05} = \frac{-0.22120}{0.05} = -4.4240
    $$

    **Computing $A(10, 15)$:** For the Hull-White model with flat market curve, $f^M(0,t) = 0.03$ for all $t$, so

    $$
    A(t,T) = \ln\frac{P^M(0,T)}{P^M(0,t)} + B(t,T)\,f^M(0,t) - \frac{\sigma^2}{4\lambda}B(t,T)^2\,(1 - e^{-2\lambda t})
    $$

    $$
    \ln\frac{P^M(0,15)}{P^M(0,10)} = \ln\frac{e^{-0.45}}{e^{-0.30}} = -0.15
    $$

    $$
    B(10,15)\,f^M(0,10) = (-4.4240)(0.03) = -0.13272
    $$

    $$
    \frac{\sigma^2}{4\lambda}B(t,T)^2(1 - e^{-2\lambda t}) = \frac{0.0001}{0.2}(19.572)(1 - e^{-1}) = 0.0005 \times 19.572 \times 0.63212 = 0.006186
    $$

    $$
    A(10,15) = -0.15 + (-0.13272) - 0.006186 = -0.28891
    $$

    **Bond price:**

    $$
    P(10,15) = \exp(A(10,15) + B(10,15)\,r_{10}) = \exp(-0.28891 + (-4.4240)(0.045))
    $$

    $$
    = \exp(-0.28891 - 0.19908) = \exp(-0.48799) \approx 0.6137
    $$

---

**Exercise 2.** The yield $y(t,T) = -[A(t,T) + B(t,T)r_t]/(T-t)$ is affine in $r_t$. Show that the yield curve at time $t$ is fully determined by $r_t$ in the one-factor model. Why does this imply that all yield curve movements are parallel shifts? How is this different from the two-factor model?

??? success "Solution to Exercise 2"
    The yield at time $t$ for maturity $T$ is

    $$
    y(t, T) = -\frac{A(t,T) + B(t,T)\,r_t}{T - t}
    $$

    This is an affine function of $r_t$: $y(t,T) = a(\tau) + b(\tau)\,r_t$ where $\tau = T - t$, $a(\tau) = -A(t,T)/\tau$, and $b(\tau) = -B(t,T)/\tau$.

    **Fully determined by $r_t$:** Since $a(\tau)$ and $b(\tau)$ are deterministic functions of the tenor $\tau$ (and time $t$ through the initial curve), the entire yield curve at time $t$ --- the function $\tau \mapsto y(t, t+\tau)$ --- is determined by the single number $r_t$.

    **Parallel shifts:** Consider two simulated values $r_t^{(1)}$ and $r_t^{(2)}$. The difference in yields is

    $$
    y^{(1)}(t, t+\tau) - y^{(2)}(t, t+\tau) = b(\tau)(r_t^{(1)} - r_t^{(2)})
    $$

    This difference depends on the tenor $\tau$ only through $b(\tau) = -B(t,t+\tau)/\tau$. Since $B$ is a smooth function of $\tau$, the yield curve movements are not exactly parallel (the coefficient $b(\tau)$ varies with $\tau$), but they are all driven by a single factor $r_t^{(1)} - r_t^{(2)}$. There is only one degree of freedom, so yield curves cannot exhibit independent twist or butterfly movements.

    **Two-factor model difference:** In the two-factor model, $y(t,T) = a(\tau) + b_x(\tau)\,x_t + b_y(\tau)\,y_t$, with two independent state variables $x_t$ and $y_t$. Since $b_x$ and $b_y$ have different shapes (decaying at rates $\lambda_1$ and $\lambda_2$), the model can generate:

    - Parallel shifts (when $x_t$ and $y_t$ move in the same direction)
    - Twists (when they move in opposite directions)
    - Butterfly movements (combinations that affect medium tenors differently from short and long)

---

**Exercise 3.** The Monte Carlo bond price estimator $\hat{P}(0,T) = \frac{1}{N_{\text{paths}}}\sum_{k=1}^{N_{\text{paths}}} 1/M^{(k)}(T)$ should equal $P^M(0,T)$. Explain why this is a necessary consistency check for the simulation. What are the most common implementation bugs that would cause this check to fail?

??? success "Solution to Exercise 3"
    The Monte Carlo bond price estimator $\hat{P}(0,T) = \frac{1}{N_{\text{paths}}}\sum_k 1/M^{(k)}(T)$ should converge to $P^M(0,T)$ by the risk-neutral pricing formula:

    $$
    P(0,T) = \mathbb{E}^{\mathbb{Q}}\!\left[\exp\!\left(-\int_0^T r_s\,ds\right)\right] = \mathbb{E}^{\mathbb{Q}}\!\left[\frac{1}{M(T)}\right]
    $$

    This is a necessary consistency check because:

    1. If the model is correctly calibrated, it must reproduce the initial curve by construction
    2. Any deviation indicates an implementation error, not a model limitation

    **Common implementation bugs:**

    - **Incorrect $\alpha(t)$ computation:** Errors in the formula $\alpha(t) = f^M(0,t) + \frac{\sigma^2}{2\lambda^2}(1-e^{-\lambda t})^2$, such as missing the squared term or incorrect signs, cause the short rate mean to drift from the market curve.
    - **Wrong transition variance:** Using $\sigma^2\Delta t$ (Euler) instead of $\frac{\sigma^2}{2\lambda}(1-e^{-2\lambda\Delta t})$ (exact) introduces a systematic bias in the simulated paths.
    - **Money market accumulation error:** Off-by-one errors in the summation index, using $r_{t_i}\Delta t$ instead of the trapezoidal rule, or accumulating $M(t)$ multiplicatively with incorrect factors.
    - **Inconsistent market curve:** Using a different market curve $P^M$ for $\alpha(t)$ computation versus the validation target.
    - **Numerical overflow/underflow:** For long maturities, $M(T)$ can become very large, causing $1/M(T)$ to underflow to zero.

---

**Exercise 4.** The forward bond price $F(t;T,S) = P(t,S)/P(t,T) = \exp([A(t,S) - A(t,T)] + [B(t,S) - B(t,T)]r_t)$ is a martingale under the $T$-forward measure. Verify this property numerically by simulating paths and checking that $\mathbb{E}^{Q^T}[F(t;T,S)] = F(0;T,S)$ for several values of $t$.

??? success "Solution to Exercise 4"
    Under the $T$-forward measure $\mathbb{Q}^T$, the forward bond price $F(t;T,S) = P(t,S)/P(t,T)$ is a martingale. To verify numerically:

    1. Simulate $N_{\text{paths}}$ short rate paths under the risk-neutral measure $\mathbb{Q}$.
    2. At each time step $t_i$, compute $F(t_i; T, S) = \exp([A(t_i,S) - A(t_i,T)] + [B(t_i,S) - B(t_i,T)]r_{t_i})$.
    3. To compute expectations under $\mathbb{Q}^T$, use the change-of-numeraire formula:

    $$
    \mathbb{E}^{\mathbb{Q}^T}[F(t;T,S)] = \frac{\mathbb{E}^{\mathbb{Q}}\!\left[\frac{F(t;T,S) \cdot P(t,T)}{M(t)}\right]}{\mathbb{E}^{\mathbb{Q}}\!\left[\frac{P(t,T)}{M(t)}\right]}
    $$

    Alternatively, since $F(0;T,S) = P(0,S)/P(0,T)$ is known, simply check that

    $$
    \frac{1}{N_{\text{paths}}}\sum_{k=1}^{N_{\text{paths}}} \frac{F(t;T,S)^{(k)} \cdot P(t,T;r_t^{(k)})}{M^{(k)}(t)} \approx F(0;T,S) \cdot P(0,T)
    $$

    for several values of $t < T$. Both sides should agree up to Monte Carlo sampling error, which decreases as $O(1/\sqrt{N_{\text{paths}}})$.

---

**Exercise 5.** The money market account is computed as $M(t_n) = \exp(\sum_{i=0}^{n-1} r_{t_i}\Delta t_i)$. This uses a left-Riemann sum for $\int_0^{t_n} r(s)ds$. Compare this with the trapezoidal rule approximation. For a typical time step $\Delta t = 0.1$ years, estimate the order of the quadrature error.

??? success "Solution to Exercise 5"
    The left-Riemann sum uses

    $$
    M_{\text{left}}(t_n) = \exp\!\left(\sum_{i=0}^{n-1} r_{t_i}\,\Delta t_i\right)
    $$

    This approximates $\int_{t_i}^{t_{i+1}} r(s)\,ds \approx r(t_i)\,\Delta t_i$, which is a first-order quadrature (exact for constant functions). The local error per subinterval is $O(\Delta t^2)$, and the global error over $[0, T]$ is $O(\Delta t)$.

    The trapezoidal rule uses

    $$
    M_{\text{trap}}(t_n) = \exp\!\left(\sum_{i=0}^{n-1} \frac{r_{t_i} + r_{t_{i+1}}}{2}\,\Delta t_i\right)
    $$

    This is a second-order quadrature (exact for linear functions). The local error per subinterval is $O(\Delta t^3)$, and the global error over $[0, T]$ is $O(\Delta t^2)$.

    For $\Delta t = 0.1$ years, the quadrature error is:

    - Left-Riemann: $O(\Delta t) = O(0.1)$, roughly a 10% relative error in the exponent per unit time
    - Trapezoidal: $O(\Delta t^2) = O(0.01)$, roughly a 1% relative error in the exponent per unit time

    The trapezoidal rule is therefore an order of magnitude more accurate for the same time step, and should always be preferred.

---

**Exercise 6.** In the two-factor model, the bond price depends on two state variables: $P(t,T) = \exp(A^{(2)}(t,T) + B_x(t,T)x_t + B_y(t,T)y_t)$. Explain why this produces richer yield curve dynamics than the one-factor model. Describe the types of yield curve movements (parallel shift, twist, butterfly) that the two-factor model can generate.

??? success "Solution to Exercise 6"
    In the two-factor model, the bond price $P(t,T) = \exp(A^{(2)}(t,T) + B_x(t,T)x_t + B_y(t,T)y_t)$ depends on two state variables with different mean-reversion speeds $\lambda_1$ and $\lambda_2$.

    The yield at time $t$ for tenor $\tau$ is

    $$
    y(t, t+\tau) = -\frac{A^{(2)}(t,t+\tau) + B_x(t,t+\tau)x_t + B_y(t,t+\tau)y_t}{\tau}
    $$

    Since $B_x(t,t+\tau) = (e^{-\lambda_1\tau} - 1)/\lambda_1$ and $B_y(t,t+\tau) = (e^{-\lambda_2\tau} - 1)/\lambda_2$ have different decay profiles, the two factors affect different parts of the yield curve differently.

    **Types of yield curve movements:**

    - **Parallel shift:** Both $x_t$ and $y_t$ increase by the same proportion. All yields increase, but not uniformly due to the different $B_x$ and $B_y$ loadings.
    - **Twist (steepening/flattening):** If $\lambda_1 < \lambda_2$, factor $x$ has a slower decay and affects long-term yields more, while factor $y$ primarily affects short-term yields. When $x_t$ increases and $y_t$ decreases, the curve steepens. The reverse causes flattening.
    - **Butterfly (curvature):** Appropriate combinations of $x_t$ and $y_t$ changes can increase both short and long yields while decreasing medium-term yields (or vice versa), creating a butterfly pattern.

    This richness is impossible in the one-factor model, where all yield curve movements are driven by a single variable.

---

**Exercise 7.** Precomputing $A(t_i, T_j)$ and $B(t_i, T_j)$ for all time steps $t_i$ and maturities $T_j$ before the simulation improves efficiency. For a simulation with $N = 100$ time steps and $M = 10$ maturities, how many values must be precomputed? Describe the memory and computational trade-offs.

??? success "Solution to Exercise 7"
    For $N = 100$ time steps and $M = 10$ maturities:

    At each time step $t_i$ ($i = 0, 1, \ldots, N$), we need $A(t_i, T_j)$ and $B(t_i, T_j)$ for each maturity $T_j > t_i$. In the worst case (all maturities beyond all time steps), this requires $101 \times 10 = 1010$ values each for $A$ and $B$, giving $2 \times 1010 = 2020$ values total.

    More precisely, at time step $t_i$, only maturities $T_j > t_i$ are needed. If maturities are at $T_1, \ldots, T_{10}$ and time steps span $[0, T_{\max}]$, the exact count depends on the maturity schedule. In the worst case, all 10 maturities are beyond all 101 time steps, giving $101 \times 10 \times 2 = 2020$ precomputed values.

    **Memory:** Each value is a double-precision float (8 bytes), so $2020 \times 8 = 16{,}160$ bytes $\approx 16$ KB. This is negligible.

    **Computational trade-off:** Precomputing costs $O(N \times M)$ evaluations of the functions $A$ and $B$ (each involving exponentials and logarithms). Without precomputation, each path at each time step would need to evaluate $A$ and $B$, costing $O(N_{\text{paths}} \times N \times M)$ function evaluations total. With precomputation, the per-path cost is just array lookups, and the total cost is $O(N \times M + N_{\text{paths}} \times N \times M)$ multiplications (trivial).

    For $N_{\text{paths}} = 10{,}000$ paths, precomputation reduces function evaluations from $10{,}000 \times 100 \times 10 = 10^7$ to just $100 \times 10 = 10^3$ --- a factor of $10{,}000$ reduction. The memory overhead of 16 KB is entirely negligible compared to this computational saving.
