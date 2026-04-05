# Arbitrage-Free SABR

The Hagan implied volatility formula, while enormously useful, is an asymptotic approximation that can produce arbitrage opportunities in the tails of the strike distribution. Specifically, the implied density derived from the Hagan formula can become **negative** for deep out-of-the-money strikes, violating the fundamental requirement that probability densities are non-negative. This section explains the source of the problem, quantifies when it becomes material, and presents the three main approaches for constructing arbitrage-free SABR: the effective 1D PDE method of Hagan et al. (2014), the mixture model approach, and the free-boundary SABR of Antonov et al. (2015).

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Identify the source of arbitrage in the Hagan formula and detect it numerically
    2. Explain the Breeden--Litzenberger relationship between option prices and probability densities
    3. Describe the 1D effective PDE approach for arbitrage-free SABR pricing
    4. Outline the mixture model and free-boundary approaches
    5. Compare the methods in terms of accuracy, speed, and implementation complexity

---

## The Arbitrage Problem

### From Implied Volatility to Probability Density

The Breeden--Litzenberger formula connects option prices to the risk-neutral probability density of the forward at maturity:

$$
p(K) = e^{rT}\frac{\partial^2 C}{\partial K^2}(K)
$$

where $C(K)$ is the undiscounted call price as a function of strike $K$. Since $p(K)$ is a probability density, it must satisfy $p(K) \geq 0$ for all $K$. Any model that produces $p(K) < 0$ for some $K$ admits **butterfly arbitrage**: a butterfly spread centered at that strike has negative value, allowing riskless profit.

### How the Hagan Formula Fails

The Hagan formula is a first-order asymptotic expansion in $T$, accurate near the money. For strikes far from the money, the expansion breaks down in two ways:

1. **Negative implied volatility**: For very deep OTM options, the formula can produce $\sigma_B(K) < 0$, which is undefined.

2. **Negative implied density**: Even when $\sigma_B(K) > 0$ for all strikes, the curvature of the implied volatility smile may be such that the Breeden--Litzenberger density becomes negative. This happens when the smile is insufficiently convex in the wings.

The density derived from the Hagan formula is:

$$
p(K) = p_{\text{BS}}(K;\sigma_B(K)) + \text{corrections involving } \sigma_B'(K) \text{ and } \sigma_B''(K)
$$

The corrections can make $p(K) < 0$ when $|\sigma_B'(K)|$ is large (steep smile) or $\sigma_B''(K)$ is too negative (insufficiently convex wings).

!!! danger "Detecting Arbitrage"
    To check for butterfly arbitrage, compute the second derivative of the call price numerically:

    $$
    p(K) \approx e^{rT}\frac{C(K+\Delta K) - 2C(K) + C(K-\Delta K)}{(\Delta K)^2}
    $$

    If $p(K) < 0$ for any $K$, the model admits arbitrage at that strike. Additionally, the call price function $C(K)$ must be convex; any non-convexity signals arbitrage.

### When Does It Matter?

The arbitrage problem is most severe when:

- **Vol-of-vol is large**: $\nu > 0.5$ (common in short-expiry swaptions)
- **Maturity is long**: $T > 5$ years
- **Strikes are far from ATM**: more than 2--3 standard deviations OTM
- **Beta is small**: $\beta$ near 0 (normal SABR)

For typical swaption parameters with $T \leq 2$ years and strikes within $\pm$200 bps of ATM, the Hagan formula is usually arbitrage-free. The problem becomes material for long-dated options and for applications requiring accurate tail pricing (e.g., CMS products, digital options).

---

## Method 1: Effective 1D PDE (Hagan et al., 2014)

### Key Idea

Instead of using the asymptotic formula, Hagan, Lesniewski, and Woodward (2014) proposed solving a **one-dimensional PDE** for the marginal density of the forward. The idea is to integrate out the volatility direction analytically (using the small-time asymptotics) and obtain an effective 1D problem in the forward variable alone.

### The Effective PDE

The marginal density $p(F, T)$ satisfies an effective forward Kolmogorov equation:

$$
\frac{\partial p}{\partial T} = \frac{1}{2}\frac{\partial^2}{\partial F^2}\left[\sigma_{\text{eff}}^2(F, T)\,p\right]
$$

where the effective local volatility $\sigma_{\text{eff}}(F, T)$ is derived from the SABR parameters by integrating out the stochastic volatility:

$$
\sigma_{\text{eff}}^2(F, T) = \alpha^2 F^{2\beta}\left[1 + 2\rho\nu\alpha F^{\beta-1}\left(\frac{F^{1-\beta} - F_0^{1-\beta}}{(1-\beta)\alpha}\right) + \nu^2\left(\frac{F^{1-\beta} - F_0^{1-\beta}}{(1-\beta)\alpha}\right)^2\right]\left[1 + \varepsilon(F) T\right]
$$

The time correction $\varepsilon(F)$ is chosen so that the solution of the PDE reproduces the Hagan formula to the same asymptotic order.

### Properties

**Arbitrage-free by construction**: The PDE is a proper forward Kolmogorov equation, so its solution $p(F, T)$ is automatically non-negative and integrates to 1 (minus any absorbed mass at $F = 0$).

**Consistency with Hagan**: For short maturities and near-the-money strikes, the PDE solution agrees with the Hagan formula to first order in $T$.

**Improved wings**: For deep OTM strikes, the PDE solution produces a non-negative density that naturally decays in the tails, avoiding the negative density problem.

### Implementation

The PDE is solved numerically on a 1D grid in $F$:

1. Discretize $F$ on a grid $[0, F_{\max}]$ (or $[-s, F_{\max}]$ for shifted SABR)
2. Apply an absorbing boundary at $F = 0$ (for $\beta > 0$) and at $F = F_{\max}$
3. Use Crank--Nicolson or implicit Euler time stepping
4. Initialize with the delta function $p(F, 0) = \delta(F - F_0)$
5. Read off call prices: $C(K) = \int_K^{F_{\max}} (F - K)p(F, T)\,dF$

The 1D PDE is fast to solve (milliseconds on a standard workstation), making this approach practical for calibration.

---

## Method 2: Mixture Models

### Key Idea

Instead of correcting the Hagan formula or solving a PDE, the mixture approach constructs an arbitrage-free density by **mixing** simple distributions (e.g., normals or lognormals) whose weights and parameters are chosen to match the SABR smile.

### Normal Mixture

A mixture of $N$ normal densities:

$$
p(F) = \sum_{i=1}^N w_i\,\phi(F; \mu_i, \sigma_i^2)
$$

where $\phi$ is the Gaussian density, $w_i > 0$, $\sum w_i = 1$, and $\sum w_i \mu_i = F_0$ (martingale condition). The parameters $(w_i, \mu_i, \sigma_i^2)$ are calibrated to match the Hagan implied volatilities at a discrete set of strikes.

**Advantages**: The density is non-negative by construction. Option prices are available in closed form (sum of Bachelier prices). The method handles negative forwards naturally.

**Disadvantages**: The number of mixture components $N$ must be chosen, and the fit may oscillate between calibration strikes.

### Lognormal Mixture

For $\beta > 0$ where forwards are positive, a mixture of lognormals:

$$
p(F) = \sum_{i=1}^N w_i\,\phi_{\text{LN}}(F; m_i, s_i^2)
$$

provides a non-negative density with closed-form Black option prices.

---

## Method 3: Free-Boundary SABR (Antonov et al.)

### Key Idea

Antonov, Konikov, and Spector (2015) proposed solving the full 2D SABR PDE with an **absorbing boundary** at $F = 0$ (for $\beta > 0$). Rather than using asymptotic approximations, they compute the marginal density of $F_T$ by numerically integrating the exact 2D transition density over the volatility variable.

### The Approach

The joint density $p(F, \sigma, T)$ satisfies the 2D forward Kolmogorov equation:

$$
\frac{\partial p}{\partial T} = \frac{1}{2}\frac{\partial^2}{\partial F^2}(\sigma^2 F^{2\beta} p) + \rho\nu\frac{\partial^2}{\partial F\,\partial\sigma}(\sigma^2 F^{\beta} p) + \frac{\nu^2}{2}\frac{\partial^2}{\partial\sigma^2}(\sigma^2 p)
$$

with boundary condition $p(0, \sigma, T) = 0$ (absorbing) for $\beta \in (0, 1)$ and initial condition $p(F, \sigma, 0) = \delta(F - F_0)\delta(\sigma - \alpha)$.

Antonov et al. solved this equation semi-analytically by:

1. Expanding in the eigenfunctions of the $\sigma$-direction operator
2. Reducing to a 1D problem in $F$ for each eigenfunction
3. Summing the contributions using a series involving Bessel functions

### Properties

**Exact in principle**: The method produces the exact SABR density (up to numerical truncation of the series).

**Arbitrage-free**: The absorbing boundary ensures non-negative density and proper probability mass accounting.

**Handles absorption**: The probability mass absorbed at $F = 0$ is computed explicitly, providing correct put prices for low strikes.

**Computational cost**: More expensive than the 1D PDE method (seconds rather than milliseconds), but still practical for calibration.

!!! tip "Choosing a Method"
    | Criterion | 1D PDE | Mixture | Free-Boundary |
    |-----------|--------|---------|---------------|
    | Arbitrage-free | Yes | Yes | Yes |
    | Consistency with Hagan | Exact (to $O(T)$) | Approximate | Exact |
    | Handles $F = 0$ absorption | Partially | No | Yes |
    | Speed | Fast (ms) | Fast (ms) | Moderate (s) |
    | Implementation complexity | Low | Low | High |
    | Best for | General use | Quick fix | Benchmarking |

---

## Practical Considerations

### Wing Extrapolation

For very deep OTM strikes beyond the calibration region, all methods require an extrapolation strategy. Common approaches:

- **Flat extrapolation**: Freeze the implied volatility at the value of the last calibrated strike
- **Linear extrapolation**: Extrapolate the implied volatility linearly in $\ln K$
- **Lee's moment formula**: Use the asymptotic bound $\sigma_B^2(K) \leq 2|{\ln K}|/T$ for large $|{\ln K}|$ to cap the extrapolation

### Impact on CMS Pricing

Constant Maturity Swap (CMS) products are particularly sensitive to the arbitrage issue because their pricing involves integrating over the entire strike domain:

$$
V_{\text{CMS}} = \int_0^{\infty} g(K)\,C''(K)\,dK
$$

Negative densities in the tails can cause material mispricing of CMS caps, floors, and CMS spread options. For CMS products, an arbitrage-free SABR method is essential.

---

## Summary

The Hagan implied volatility formula can produce negative probability densities for deep out-of-the-money strikes, creating butterfly arbitrage. Three families of fixes exist. The 1D effective PDE method (Hagan et al., 2014) replaces the asymptotic formula with a numerically solved forward equation that is arbitrage-free by construction while remaining consistent with Hagan to first order. Mixture models construct non-negative densities from sums of simple distributions calibrated to the SABR smile. The free-boundary SABR (Antonov et al., 2015) solves the full 2D SABR PDE with absorbing boundaries, providing exact results at higher computational cost. For most practical applications, the 1D PDE method offers the best balance of accuracy, speed, and implementation simplicity. CMS products and other tail-sensitive instruments require arbitrage-free methods.

---

## Further Reading

- Hagan, P., Lesniewski, A., & Woodward, D. (2014). *Probability distribution in the SABR model of stochastic volatility*. In *Large Deviations and Asymptotic Methods in Finance*, Springer.
- Antonov, A., Konikov, M., & Spector, M. (2015). *The free boundary SABR: Natural extension to negative rates*. SSRN preprint.
- Rebonato, R. & Cardoso, M. (2004). *Unconstrained fitting of the SABR parameters*. RISK, March.
- Le Floc'h, F. & Kennedy, G. (2014). *Finite difference techniques for arbitrage-free SABR*. Journal of Computational Finance.

---

## Exercises

**Exercise 1.** The Breeden-Litzenberger formula gives the implied density as $f(K) = e^{rT}\partial^2 C/\partial K^2$. If the Hagan formula produces a call price function $C(K)$ that is not convex for extreme $K$, explain why $f(K) < 0$ at those strikes. What type of arbitrage does a negative density create? (Hint: consider butterfly spreads.)

??? success "Solution to Exercise 1"
    The Breeden--Litzenberger formula states that the risk-neutral density is the second derivative of the call price with respect to strike:

    $$
    f(K) = e^{rT}\frac{\partial^2 C}{\partial K^2}(K)
    $$

    For $f(K)$ to be a valid probability density, we need $f(K) \geq 0$ for all $K$, which requires $C(K)$ to be **convex** in $K$ (i.e., $\partial^2 C / \partial K^2 \geq 0$). When the Hagan formula produces a call price function that is not convex at extreme strikes, the second derivative becomes negative, and hence $f(K) < 0$ at those strikes.

    A negative density creates **butterfly arbitrage**. A butterfly spread centered at strike $K$ consists of buying calls at $K - \Delta K$ and $K + \Delta K$ while selling two calls at $K$:

    $$
    \Pi = C(K - \Delta K) - 2C(K) + C(K + \Delta K)
    $$

    In the limit as $\Delta K \to 0$, this payoff is proportional to $\partial^2 C / \partial K^2 \cdot (\Delta K)^2$. If $C''(K) < 0$, then $\Pi < 0$, meaning the butterfly spread has a negative price. Since the butterfly payoff $(K - \Delta K, K, K + \Delta K)$ is non-negative at maturity (it equals $\max(0, \Delta K - |F_T - K|)$), a negative price constitutes a riskless profit opportunity. One can buy this mispriced butterfly, collect a premium upfront, and face no downside at expiry.

    Physically, the negative density means the model assigns negative probability to certain forward rate outcomes, which is not just mathematically inconsistent but also creates exploitable trading opportunities via butterfly spreads at the affected strikes.

---

**Exercise 2.** For SABR parameters $\alpha = 0.035$, $\beta = 0.5$, $\rho = -0.5$, $\nu = 0.6$, $F = 0.03$, $T = 10$, compute the Hagan implied volatility at several deep OTM put strikes ($K = 0.005, 0.002, 0.001$). At what strike does the formula become unreliable? How would you detect this in practice?

??? success "Solution to Exercise 2"
    With the given parameters $\alpha = 0.035$, $\beta = 0.5$, $\rho = -0.5$, $\nu = 0.6$, $F = 0.03$, and $T = 10$, the Hagan formula becomes unreliable at deep OTM put strikes for the following reasons.

    **Numerical computation.** The Hagan implied volatility formula involves the quantity:

    $$
    z = \frac{\nu}{\alpha}(FK)^{(1-\beta)/2}\ln\frac{F}{K}
    $$

    and

    $$
    x(z) = \ln\frac{\sqrt{1 - 2\rho z + z^2} + z - \rho}{1 - \rho}
    $$

    At $K = 0.005$: $\ln(F/K) = \ln(6) \approx 1.79$, so $z \approx (0.6/0.035)(0.03 \times 0.005)^{0.25} \times 1.79 \approx 3.8$. At this large value of $z$, the asymptotic expansion degrades.

    At $K = 0.002$: $\ln(F/K) = \ln(15) \approx 2.71$, giving an even larger $z$ value. At $K = 0.001$: $\ln(F/K) = \ln(30) \approx 3.40$.

    **Signs of unreliability.** The formula becomes unreliable when:

    - The implied volatility becomes negative ($\sigma_B(K) < 0$), which is undefined
    - The implied density $f(K) = e^{rT}\partial^2 C / \partial K^2$ becomes negative
    - The correction terms in the Hagan expansion exceed the leading-order term, indicating the asymptotic series has broken down

    With $\nu = 0.6$ (high vol-of-vol) and $T = 10$ (long maturity), the product $\nu^2 T = 3.6$ is large, making the $O(T)$ correction term dominant rather than perturbative. The formula is expected to become unreliable around $K = 0.005$ or above for this parameter set.

    **Detection in practice.** One should:

    1. Check that $\sigma_B(K) > 0$ for all strikes
    2. Compute the implied density numerically via the finite difference $f(K) \approx e^{rT}[C(K+h) - 2C(K) + C(K-h)]/h^2$ and verify $f(K) \geq 0$
    3. Check that the call price function $C(K)$ is convex and monotonically decreasing
    4. Verify that the correction term $[\cdots]T$ in the Hagan formula is small relative to 1 (say, less than 0.5)

    When these checks fail, one should switch to an arbitrage-free SABR method such as the 1D effective PDE or free-boundary SABR.

---

**Exercise 3.** The 1D effective PDE method (Hagan et al., 2014) replaces the Hagan formula with a numerically solved forward Kolmogorov equation. Explain why solving the forward equation guarantees a non-negative density (since the transition density of a well-posed diffusion is non-negative). How does this approach preserve consistency with the Hagan formula near ATM?

??? success "Solution to Exercise 3"
    **Why the forward equation guarantees non-negative density.** The 1D effective PDE has the form of a forward Kolmogorov (Fokker--Planck) equation:

    $$
    \frac{\partial p}{\partial T} = \frac{1}{2}\frac{\partial^2}{\partial F^2}\left[\sigma_{\text{eff}}^2(F, T)\,p\right]
    $$

    with initial condition $p(F, 0) = \delta(F - F_0)$ and appropriate boundary conditions. This equation describes the evolution of the probability density of a diffusion process with local volatility $\sigma_{\text{eff}}(F, T)$. By the general theory of parabolic PDEs, if $\sigma_{\text{eff}}^2 > 0$ (i.e., the diffusion coefficient is strictly positive), then the solution satisfies:

    1. **Non-negativity**: $p(F, T) \geq 0$ for all $F$ and $T > 0$. This follows from the maximum principle for parabolic equations: a solution that starts non-negative (a delta function is the limit of non-negative functions) remains non-negative.
    2. **Conservation of mass**: $\int p(F, T)\,dF = 1$ (minus any mass absorbed at boundaries), ensuring the density integrates to a proper probability measure.

    Therefore, by solving the PDE numerically rather than using an asymptotic expansion, we obtain option prices $C(K) = \int_K^{\infty} (F - K) p(F, T)\,dF$ that are automatically convex in $K$, and the Breeden--Litzenberger density is non-negative by construction.

    **Consistency with the Hagan formula near ATM.** The effective local volatility $\sigma_{\text{eff}}(F, T)$ is constructed by integrating out the stochastic volatility variable using the same asymptotic expansion that underlies the Hagan formula. Specifically, $\sigma_{\text{eff}}^2$ includes a time-correction term $\varepsilon(F)T$ that is calibrated so that the PDE solution, when converted to implied volatility, matches the Hagan formula to $O(T)$. Near ATM ($K \approx F$), the Hagan formula is an accurate asymptotic approximation, and the PDE solution reproduces it to the same order. The difference only becomes apparent in the deep wings, where the PDE solution provides a physically consistent (non-negative) density while the Hagan formula may not.

---

**Exercise 4.** CMS (Constant Maturity Swap) products are particularly sensitive to the tails of the forward distribution because the CMS convexity adjustment depends on $\mathbb{E}[(F_T - K)^+ / P(T)]$ for all $K$. Explain why using the standard Hagan formula (with potential negative densities in the tails) can lead to significant mispricing of CMS caps and floors. How much error might result for a 30-year CMS cap?

??? success "Solution to Exercise 4"
    **Why CMS products are sensitive to tails.** CMS (Constant Maturity Swap) products depend on the expectation of swap rates under the annuity measure. The CMS convexity adjustment involves integrals over the entire strike domain. Specifically, the CMS rate can be expressed using a static replication formula:

    $$
    \mathbb{E}^A[S_T \cdot g(S_T)] = g(F) + \int_0^F g''(K)\,P(K)\,dK + \int_F^{\infty} g''(K)\,C(K)\,dK
    $$

    where $g$ is a payoff function and $P(K)$, $C(K)$ are put and call prices. For CMS caps and floors, the relevant integrals extend to extreme strikes where the Hagan formula may produce negative densities. Since:

    $$
    V_{\text{CMS}} = \int_0^{\infty} g(K)\,C''(K)\,dK = \int_0^{\infty} g(K)\,e^{-rT} f(K)\,dK
    $$

    negative values of $f(K)$ directly subtract from the integral, causing systematic mispricing.

    **Magnitude of the error.** For a 30-year CMS cap, the underlying swap rate has a long tenor, meaning:

    - The vol-of-vol $\nu$ tends to be higher for longer maturities
    - The strike range over which the density is negative can be wider
    - The CMS convexity adjustment itself is larger, amplifying the impact of tail errors

    For typical parameters, the error from negative densities in a 30-year CMS cap can be on the order of 5--20 basis points of the CMS rate, or several percent of the option premium. This is material relative to bid-ask spreads of 1--5 bps on CMS products. For CMS spread options (which depend on the joint distribution of two swap rates), the tail sensitivity is even more pronounced.

    The solution is to use an arbitrage-free SABR method (1D PDE, free-boundary, or mixture model) that guarantees non-negative densities across the entire strike domain, ensuring that the CMS replication integrals are well-behaved.

---

**Exercise 5.** The free-boundary SABR of Antonov et al. (2015) solves the full 2D SABR PDE with absorbing boundary at $F = 0$. Compare this approach with the 1D effective PDE in terms of: (a) computational cost; (b) accuracy; (c) ability to handle negative rates; (d) implementation complexity. Which approach would you recommend for a rates trading desk?

??? success "Solution to Exercise 5"
    **(a) Computational cost.** The 1D effective PDE method solves a one-dimensional partial differential equation on a grid in the forward variable $F$. Using Crank--Nicolson or implicit Euler with a grid of $\sim$500 points and $\sim$100 time steps, this takes **milliseconds** on a standard workstation. The free-boundary SABR of Antonov et al. involves expanding the solution in eigenfunctions of the volatility-direction operator, computing Bessel function series, and summing contributions. This requires evaluating special functions and performing numerical integration for each strike, taking **seconds** per smile. The free-boundary method is roughly 100--1000 times slower than the 1D PDE.

    **(b) Accuracy.** The free-boundary SABR is **exact** in principle: it solves the full 2D SABR dynamics without asymptotic approximations (up to numerical truncation of the series expansion). The 1D PDE method is exact to $O(T)$, matching the Hagan formula's asymptotic order, but the PDE solution itself is exact for the effective 1D diffusion. Near ATM and for moderate maturities, both methods produce nearly identical results. For very long maturities ($T > 10$Y) or extreme strikes, the free-boundary SABR is more accurate because it does not rely on small-time asymptotics in the volatility direction.

    **(c) Handling negative rates.** The free-boundary SABR with absorbing boundary at $F = 0$ was specifically designed to handle the transition to negative rates via a shifted or free-boundary formulation. Antonov et al. extended their method to allow the forward to cross zero naturally, making it well-suited for EUR and JPY markets where negative rates occur. The 1D PDE method can also handle negative rates by shifting the grid to include negative values (shifted SABR), but the effective local volatility function $\sigma_{\text{eff}}(F)$ must be carefully specified near $F = 0$ to avoid numerical instabilities.

    **(d) Implementation complexity.** The 1D PDE method is straightforward: it requires implementing a standard finite-difference solver for a 1D parabolic PDE, which most quantitative libraries already provide. The free-boundary SABR is considerably more complex, requiring Bessel function evaluations, eigenfunction expansions, numerical quadrature, and careful handling of series truncation and convergence. The implementation and testing effort is substantially higher.

    **Recommendation for a rates trading desk.** For real-time pricing and calibration, the **1D effective PDE** is the recommended approach. Its millisecond computation time supports intraday recalibration and live pricing of swaption books. It is arbitrage-free, consistent with the Hagan formula, and straightforward to implement. The free-boundary SABR should be used as a **benchmark** for validating the 1D PDE results, particularly for long-dated products and negative-rate environments, but its computational cost makes it impractical as the primary production method for a desk that must price thousands of swaptions per second.

---

**Exercise 6.** A mixture model constructs an arbitrage-free density as a weighted sum of simple distributions: $f(K) = \sum_i w_i f_i(K)$ where each $f_i \geq 0$ and $\sum_i w_i = 1$ with $w_i \geq 0$. If the component distributions are lognormals with different volatilities, explain how the weights and volatilities can be chosen to match the SABR smile near ATM while ensuring non-negative densities everywhere. What is the main limitation of this approach?

??? success "Solution to Exercise 6"
    **Constructing the mixture.** A lognormal mixture density takes the form:

    $$
    f(K) = \sum_{i=1}^N w_i\,\phi_{\text{LN}}(K; m_i, s_i^2)
    $$

    where $\phi_{\text{LN}}$ is the lognormal density with location parameter $m_i$ and volatility $s_i$, and the weights satisfy $w_i \geq 0$, $\sum_i w_i = 1$. Since each component $\phi_{\text{LN}} \geq 0$ and the weights are non-negative, $f(K) \geq 0$ everywhere, guaranteeing no arbitrage.

    **Matching the SABR smile.** The calibration proceeds as follows:

    1. **Martingale constraint**: The mixture must satisfy $\mathbb{E}[F_T] = F_0$, which gives $\sum_i w_i \exp(m_i + s_i^2/2) = F_0$ (adjusting for lognormal mean parameterization), or equivalently $\sum_i w_i \mu_i = F_0$ where $\mu_i$ is the mean of the $i$-th component.
    2. **Moment matching at ATM**: Choose the component means $m_i$ and volatilities $s_i$ so that the mixture reproduces the ATM implied volatility and its first and second derivatives (the level, skew, and curvature of the smile).
    3. **Least-squares calibration**: For a mixture with $N$ components, there are $3N - 2$ free parameters (after the weight-sum and martingale constraints). These are calibrated by minimizing the squared difference between mixture-implied Black volatilities and the Hagan formula (or market) values at a discrete set of strikes.

    With $N = 3$ components, there are 7 free parameters, which is sufficient to match the SABR smile's level, slope, and curvature at ATM plus several wing points. The call prices under the mixture are available in closed form as a weighted sum of Black--Scholes call prices, making calibration fast.

    **Main limitation.** The principal limitation is **non-uniqueness and extrapolation sensitivity**. For a given number of components $N$, multiple parameter sets may produce equally good fits within the calibration strike range but different behavior in the wings. The mixture density can exhibit oscillations or multiple modes between calibration strikes that are not economically motivated. Additionally, increasing $N$ to improve the fit can lead to overfitting and instability. Unlike the SABR PDE methods, the mixture approach does not arise from a consistent stochastic model, so it does not provide a principled dynamics for how the smile evolves as the forward moves. This makes it less suitable for hedging applications that depend on smile dynamics.
