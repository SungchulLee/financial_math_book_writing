# Calibration to Cap Volatilities

Interest rate caps are the primary liquid instruments used to calibrate Black-Karasinski (BK) model volatility. A cap is a portfolio of caplets, each of which is a call option on a forward rate for a single accrual period. Market convention quotes caps in terms of implied (Black) volatilities, and calibrating the BK model means finding the mean-reversion speed $a$ and log-rate volatility $\sigma$ (or a time-dependent $\sigma(t)$) so that model-implied cap prices match market prices. Because the BK model has no closed-form caplet formula, calibration relies on the trinomial tree: the tree is built, $\theta(t)$ is calibrated to the yield curve, and caplets are priced by backward induction, all inside the optimizer's objective function evaluation.

!!! info "Prerequisites"

    - [Log-Normal Short Rate SDE](log_normal_short_rate_sde.md) (BK dynamics)
    - [Trinomial Tree Implementation](trinomial_tree_implementation.md) (tree construction and calibration of $\theta(t)$)
    - [No Closed-Form Bond Prices](no_closed_form_bond_prices.md) (numerical pricing necessity)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Define caplets and caps in terms of the short rate and forward LIBOR
    2. Price a caplet on the BK trinomial tree by backward induction
    3. Extract Black implied volatilities from model caplet prices
    4. Formulate the calibration objective function
    5. Implement a sequential and global calibration procedure for $\sigma(t)$
    6. Assess convergence, stability, and uniqueness of the calibrated parameters

---

## Cap and Caplet Definitions

### Caplet payoff

A caplet with reset date $T_i$, payment date $T_{i+1}$, strike $K$, and day-count fraction $\delta_i = T_{i+1} - T_i$ pays at $T_{i+1}$:

$$
\delta_i\left[L(T_i, T_i, T_{i+1}) - K\right]^+
$$

where $L(T_i, T_i, T_{i+1})$ is the spot LIBOR rate fixing at $T_i$ for the period $[T_i, T_{i+1}]$:

$$
L(T_i, T_i, T_{i+1}) = \frac{1}{\delta_i}\left[\frac{1}{P(T_i, T_{i+1})} - 1\right]
$$

### Cap as a portfolio of caplets

An interest rate cap with tenor dates $T_0, T_1, \ldots, T_n$ and strike $K$ is the sum of $n$ caplets:

$$
\text{Cap}(K) = \sum_{i=0}^{n-1} \text{Caplet}(T_i, T_{i+1}, K)
$$

The time-0 value of each caplet is

$$
V_{\text{cplt}}(0) = \mathbb{E}^{\mathbb{Q}}\!\left[\exp\!\left(-\int_0^{T_{i+1}} r_s\,ds\right)\,\delta_i\left[L(T_i, T_i, T_{i+1}) - K\right]^+\right]
$$

---

## Caplet Pricing on the Trinomial Tree

### Backward induction procedure

Given a calibrated BK trinomial tree (where $\theta(t_k)$ at each time step matches the market discount curve), a caplet with reset $T_i$ and payment $T_{i+1}$ is priced as follows:

**Step 1.** At all terminal nodes at time $T_{i+1}$, set the payoff:

$$
V(T_{i+1}, x_j) = \delta_i\left[L_j - K\right]^+
$$

where $L_j$ is the LIBOR rate implied by the one-period bond price at node $(T_i, x_j)$:

$$
L_j = \frac{1}{\delta_i}\left[\frac{1}{P_{\text{tree}}(T_i, T_{i+1}; x_j)} - 1\right]
$$

and $P_{\text{tree}}(T_i, T_{i+1}; x_j)$ is the price of a zero-coupon bond maturing at $T_{i+1}$, computed at node $(T_i, x_j)$ by one step of discounting on the tree.

**Step 2.** Roll backward from $T_{i+1}$ to time 0 using the standard tree recursion:

$$
V(t_k, x_j) = e^{-e^{x_j}\Delta t}\left[p_u\,V(t_{k+1}, x_{j+1}) + p_m\,V(t_{k+1}, x_j) + p_d\,V(t_{k+1}, x_{j-1})\right]
$$

**Step 3.** Read off $V(0, x_0)$ as the model caplet price.

!!! tip "Efficiency for Multiple Caplets"
    When pricing a full cap (multiple caplets), the tree is built once and the backward induction is performed for each caplet separately. The $\theta(t)$ calibration to the yield curve is shared across all caplets.

---

## Black Implied Volatility Extraction

### Black's caplet formula

Market convention quotes caplet prices in terms of Black's formula. Given a caplet price $V_{\text{cplt}}$, the Black implied volatility $\sigma^{\text{Black}}$ satisfies:

$$
V_{\text{cplt}} = \delta_i\,P(0, T_{i+1})\left[F_i\,\mathcal{N}(d_1) - K\,\mathcal{N}(d_2)\right]
$$

where $F_i = L(0, T_i, T_{i+1})$ is the forward LIBOR rate, and

$$
d_1 = \frac{\ln(F_i/K) + \frac{1}{2}(\sigma^{\text{Black}})^2 T_i}{\sigma^{\text{Black}}\sqrt{T_i}}, \qquad d_2 = d_1 - \sigma^{\text{Black}}\sqrt{T_i}
$$

### Inversion

Given a model caplet price from the tree, invert Black's formula numerically (e.g., Newton-Raphson on the vega-weighted equation) to obtain $\sigma^{\text{Black}}_{\text{model}}(T_i, K)$.

---

## Calibration Objective Function

### Formulation

Let $\sigma^{\text{mkt}}_j$ denote the market-quoted Black cap volatility for the $j$-th cap (maturity $T_{n_j}$, strike $K_j$), and let $\sigma^{\text{model}}_j(a, \sigma(\cdot))$ denote the model-implied cap volatility obtained by:

1. Building the BK tree with parameters $(a, \sigma(\cdot))$
2. Calibrating $\theta(t)$ to the market yield curve
3. Pricing each constituent caplet by backward induction
4. Summing caplet prices to get the cap price
5. Inverting Black's formula to get the model cap implied volatility

The objective function is:

$$
\min_{a,\,\sigma(\cdot)}\;\sum_{j=1}^{M} w_j\left[\sigma^{\text{model}}_j(a, \sigma(\cdot)) - \sigma^{\text{mkt}}_j\right]^2
$$

Weights $w_j$ are typically inverse-vega or uniform. The parameter $\sigma(\cdot)$ is either a scalar (flat volatility) or a piecewise-constant function with breakpoints at cap maturities.

### Piecewise-constant volatility

For maximum flexibility, define $\sigma(t) = \sigma_i$ for $t \in [T_{i-1}, T_i)$, with one volatility level per cap tenor period. This gives $N$ volatility parameters plus the global mean-reversion $a$: a total of $N + 1$ free parameters.

---

## Calibration Procedures

### Sequential (bootstrap) calibration

When $\sigma(t)$ is piecewise-constant with breakpoints matching cap maturities, the calibration can proceed sequentially:

1. **1Y cap**: Solve for $\sigma_1$ (one-dimensional root-finding) matching the 1Y cap volatility
2. **2Y cap**: Fix $\sigma_1$; solve for $\sigma_2$ matching the 2Y cap (which depends on both $\sigma_1$ and $\sigma_2$ through its constituent caplets)
3. **Continue** for each subsequent maturity

This reduces an $(N+1)$-dimensional optimization to $N$ one-dimensional root-finding problems (plus a separate optimization for $a$, or $a$ is fixed a priori).

### Global calibration

For joint calibration to caps at multiple strikes (a volatility smile), a global optimizer (Levenberg-Marquardt, differential evolution) is used. The tree must be rebuilt at each function evaluation, making this computationally intensive.

| Method | Parameters | Instruments | Cost per evaluation |
|--------|-----------|-------------|-------------------|
| Sequential | $\sigma_1, \ldots, \sigma_N$ (given $a$) | ATM caps | $N$ tree builds |
| Global | $a, \sigma_1, \ldots, \sigma_N$ | ATM + OTM caps | 1 tree build |

---

## Convergence and Stability

### Tree refinement

The accuracy of calibrated parameters depends on the tree granularity:

- **Time steps**: Finer $\Delta t$ improves caplet pricing accuracy but increases computation time as $O(N_t^2)$
- **Convergence check**: Calibrate at two resolutions (e.g., 50 and 100 steps per year) and verify that $|\sigma_i^{(100)} - \sigma_i^{(50)}| < \epsilon$

### Uniqueness

For ATM caps, the map from $\sigma_i$ to model cap volatilities is monotone: higher $\sigma_i$ produces higher model cap implied volatility. This ensures uniqueness of the bootstrap solution. For OTM caps, the relationship is more complex and multiple local minima may exist in the global calibration.

!!! warning "Sensitivity to Mean Reversion"
    The parameter $a$ and the volatility levels $\sigma_i$ are partially correlated: increasing $a$ flattens the rate distribution, which can be offset by increasing $\sigma$. In practice, $a$ is often estimated from historical data or from swaption prices (which are more sensitive to mean reversion) and then held fixed during cap calibration.

---

## Summary

| Step | Description |
|------|-------------|
| **Input** | Market cap implied volatilities, yield curve |
| **Tree build** | BK trinomial tree in $x = \ln r$ space |
| **$\theta(t)$ calibration** | Forward induction matching market discount factors |
| **Caplet pricing** | Backward induction for each caplet payoff |
| **Implied vol extraction** | Invert Black's formula for model cap implied vol |
| **Optimization** | Minimize $\sum w_j(\sigma^{\text{model}}_j - \sigma^{\text{mkt}}_j)^2$ |
| **Output** | Calibrated $a$ and $\sigma(t)$ |

The calibrated BK model can then be used to price caps at non-standard strikes, floors (by put-call parity), and structured products. For swaption calibration under BK, see [Comparison with Hull-White](comparison_with_hull_white.md) for a discussion of relative strengths.

---

## Exercises

**Exercise 1.** A caplet resets at $T_i = 1$ year, pays at $T_{i+1} = 1.25$ years, has strike $K = 3\%$, and the one-period tree bond price at the reset node is $P_{\text{tree}}(T_i, T_{i+1}; x_j) = 0.9920$. Compute the spot LIBOR rate $L_j$ and the caplet payoff $\delta_i[L_j - K]^+$ at this node.

??? success "Solution to Exercise 1"
    The day-count fraction is $\delta_i = T_{i+1} - T_i = 1.25 - 1.0 = 0.25$. The spot LIBOR rate at node $(T_i, x_j)$ is

    $$
    L_j = \frac{1}{\delta_i}\left[\frac{1}{P_{\text{tree}}(T_i, T_{i+1}; x_j)} - 1\right] = \frac{1}{0.25}\left[\frac{1}{0.9920} - 1\right]
    $$

    Computing the inner term: $1/0.9920 = 1.008065$ (to six decimal places), so $1/0.9920 - 1 = 0.008065$. Then

    $$
    L_j = \frac{0.008065}{0.25} = 0.032258 \approx 3.226\%
    $$

    Since $L_j = 3.226\% > K = 3\%$, the caplet is in the money at this node. The payoff is

    $$
    \delta_i[L_j - K]^+ = 0.25 \times [0.03226 - 0.03]^+ = 0.25 \times 0.00226 = 0.000565
    $$

    The LIBOR rate is approximately 3.23% and the caplet payoff at this node is approximately $0.0565\%$ of notional.

---

**Exercise 2.** Explain why calibrating $\theta(t)$ to the market yield curve must be done *before* (or simultaneously with) pricing caplets on the BK tree. What would go wrong if $\theta(t)$ were set to a constant instead of being calibrated to match market discount factors?

??? success "Solution to Exercise 2"
    Calibrating $\theta(t)$ to the market yield curve must precede (or be simultaneous with) caplet pricing because the tree's discount factors at each node directly depend on $\theta(t)$. The time-dependent drift determines the short rate levels at each node via the branching structure, and these rates are used both for discounting during backward induction and for computing the LIBOR rates that define the caplet payoff.

    If $\theta(t)$ were set to a constant instead of being calibrated:

    1. **Yield curve mismatch**: The model discount factors $P^{\text{model}}(0, T)$ would not match $P^{\text{mkt}}(0, T)$. The model would imply a different term structure than what is observed in the market.

    2. **Incorrect forward rates**: Since $L(0, T_i, T_{i+1})$ is determined by $P(0, T_i)/P(0, T_{i+1}) - 1$, incorrect discount factors produce incorrect forward LIBOR rates. The caplet's at-the-money level would be wrong.

    3. **Arbitrage**: The cap price depends on the forward rate curve. A model that does not reproduce market discount factors introduces arbitrage between the model's implied bond prices and observable market prices. Any derivative priced on such a tree would be inconsistent with the underlying yield curve instruments.

    4. **Invalid implied volatility extraction**: The conversion between model caplet prices and Black implied volatilities uses market forward rates and discount factors. If the tree produces different discount factors, the implied volatility comparison between model and market becomes meaningless.

    In summary, $\theta(t)$ calibration ensures the tree is no-arbitrage with respect to the observed yield curve, which is a prerequisite for meaningful volatility calibration.

---

**Exercise 3.** A model caplet price is $V_{\text{cplt}} = 0.00215$, the forward LIBOR rate is $F_i = 4.5\%$, the strike is $K = 4.5\%$ (at-the-money), the discount factor is $P(0, T_{i+1}) = 0.9560$, and $\delta_i = 0.25$, $T_i = 2$. Using Black's caplet formula for ATM options (where $d_1 = \frac{1}{2}\sigma^{\text{Black}}\sqrt{T_i}$ and $d_2 = -d_1$), set up the equation that determines $\sigma^{\text{Black}}$ and describe how Newton-Raphson would be used to solve it.

??? success "Solution to Exercise 3"
    For an ATM caplet ($F_i = K = 4.5\%$), we have $\ln(F_i/K) = 0$, so Black's formula simplifies. The $d_1$ and $d_2$ terms become

    $$
    d_1 = \frac{0 + \frac{1}{2}(\sigma^{\text{Black}})^2 T_i}{\sigma^{\text{Black}}\sqrt{T_i}} = \frac{1}{2}\sigma^{\text{Black}}\sqrt{T_i}
    $$

    $$
    d_2 = -\frac{1}{2}\sigma^{\text{Black}}\sqrt{T_i}
    $$

    Substituting into Black's formula with $\delta_i = 0.25$, $P(0, T_{i+1}) = 0.9560$, $F_i = K = 0.045$, $T_i = 2$:

    $$
    V_{\text{cplt}} = \delta_i P(0, T_{i+1}) \cdot F_i \left[\mathcal{N}(d_1) - \mathcal{N}(d_2)\right]
    $$

    Since $d_2 = -d_1$ for ATM, we have $\mathcal{N}(d_1) - \mathcal{N}(d_2) = \mathcal{N}(d_1) - \mathcal{N}(-d_1) = 2\mathcal{N}(d_1) - 1$. The equation to solve is

    $$
    0.00215 = 0.25 \times 0.9560 \times 0.045 \times \left[2\Phi\!\left(\tfrac{1}{2}\sigma^{\text{Black}}\sqrt{2}\right) - 1\right]
    $$

    The prefactor is $0.25 \times 0.9560 \times 0.045 = 0.01076$. So we need

    $$
    2\Phi\!\left(\tfrac{\sigma^{\text{Black}}}{\sqrt{2}} \cdot \tfrac{1}{\sqrt{2}} \cdot \sqrt{2}\right) - 1 = \frac{0.00215}{0.01076} = 0.1998
    $$

    Define $h = \frac{1}{2}\sigma^{\text{Black}}\sqrt{2}$. We need $2\Phi(h) - 1 = 0.1998$.

    **Newton-Raphson procedure**: Define the function

    $$
    F(\sigma) = \delta_i P(0, T_{i+1})\left[F_i \Phi(d_1(\sigma)) - K\Phi(d_2(\sigma))\right] - V_{\text{cplt}}
    $$

    The derivative with respect to $\sigma$ is the Black vega:

    $$
    F'(\sigma) = \delta_i P(0, T_{i+1}) F_i \sqrt{T_i}\,\phi(d_1)
    $$

    where $\phi$ is the standard normal density. The Newton update is

    $$
    \sigma_{n+1} = \sigma_n - \frac{F(\sigma_n)}{F'(\sigma_n)}
    $$

    Starting from an initial guess (e.g., $\sigma_0 = 0.20$), each iteration evaluates $\Phi$ and $\phi$ at $d_1(\sigma_n)$ and updates. Convergence is typically achieved in 3--5 iterations due to the near-linearity of Black's formula in $\sigma$ around the ATM point.

---

**Exercise 4.** In the sequential (bootstrap) calibration procedure, suppose the 1Y ATM cap market volatility is 18% and the 2Y ATM cap market volatility is 20%. After step 1, you have calibrated $\sigma_1$. Explain precisely which caplets depend on $\sigma_2$ in step 2 and why fixing $\sigma_1$ from step 1 makes the problem one-dimensional.

??? success "Solution to Exercise 4"
    A 1Y ATM cap consists of caplets resetting at quarterly dates in the first year (e.g., 3m, 6m, 9m caplets, depending on convention). A 2Y ATM cap consists of all the caplets from the 1Y cap plus additional caplets resetting in the second year.

    In step 1, $\sigma_1$ governs the BK volatility for $t \in [0, T_1)$ (the first year). All caplets resetting in year 1 depend on $\sigma_1$. Solving for $\sigma_1$ matches the 1Y cap market volatility of 18%.

    In step 2, we note the 2Y cap price is the sum of:

    - **Year 1 caplets**: These depend only on $\sigma_1$, which is already fixed. Their model prices do not change when we vary $\sigma_2$.
    - **Year 2 caplets**: Caplets resetting in the interval $[T_1, T_2)$ depend on the BK volatility $\sigma_2$ during that period. They also depend on $\sigma_1$ indirectly (through the tree structure and $\theta(t)$ calibration for earlier times), but since $\sigma_1$ is fixed, this dependence is frozen.

    The 2Y cap model volatility is a function of both $\sigma_1$ (fixed) and $\sigma_2$ (free). Since the 1Y cap portion is locked, the residual --- the 2Y cap price minus the 1Y cap price --- depends only on $\sigma_2$. This makes the calibration equation one-dimensional: find $\sigma_2$ such that the total 2Y cap model implied volatility equals 20%.

    The sequential structure works because piecewise-constant volatility with breakpoints at cap maturities creates a causal chain: $\sigma_k$ affects only caplets resetting in period $k$ and later. At step $k$, all earlier $\sigma_1, \ldots, \sigma_{k-1}$ are fixed, so only $\sigma_k$ is free, reducing each step to a one-dimensional root-finding problem.

---

**Exercise 5.** Consider the calibration objective function

$$
\min_{a,\,\sigma(\cdot)}\;\sum_{j=1}^{M} w_j\left[\sigma^{\text{model}}_j - \sigma^{\text{mkt}}_j\right]^2
$$

with uniform weights $w_j = 1$. If there are $M = 10$ ATM caps (maturities 1Y through 10Y) and piecewise-constant $\sigma(t)$ with 10 breakpoints, how many free parameters does the global calibration have? Why might a practitioner choose to fix $a$ from swaption data rather than calibrating it jointly with the $\sigma_i$?

??? success "Solution to Exercise 5"
    With 10 piecewise-constant volatility levels $\sigma_1, \ldots, \sigma_{10}$ (one per tenor period) plus the global mean-reversion speed $a$, the total number of free parameters is $10 + 1 = 11$.

    There are $M = 10$ ATM cap prices to match, so the problem is slightly underdetermined ($11$ parameters, $10$ constraints). However, this counting ignores the fact that $a$ affects all cap prices simultaneously while each $\sigma_i$ has localized influence.

    A practitioner might fix $a$ from swaption data for several reasons:

    1. **Identifiability**: The parameters $a$ and $\{\sigma_i\}$ are partially correlated. Increasing $a$ compresses the rate distribution (stronger mean reversion pulls rates toward the mean), and this effect can be offset by increasing $\sigma_i$. Joint calibration may produce poorly identified parameters with large confidence intervals.

    2. **Swaptions are more sensitive to $a$**: Swaptions depend on the distribution of swap rates over longer horizons, where mean reversion has a cumulative effect. Caps primarily depend on the marginal caplet distributions, which are more sensitive to $\sigma_i$ than to $a$. Estimating $a$ from swaptions exploits the instrument that is most informative about mean reversion.

    3. **Stability**: Fixing $a$ reduces the problem from $11$-dimensional to $10$-dimensional (one $\sigma_i$ per cap). This is exactly determined ($10$ parameters, $10$ constraints) and can be solved by the sequential bootstrap, which is fast and unique. Joint calibration with $a$ free requires a global optimizer, which is slower and may find local minima.

    4. **Regularization**: Historical estimates of $a$ (from time-series analysis of rate data) provide an independent anchor, reducing overfitting to a single cross-section of cap prices.

---

**Exercise 6.** You calibrate the BK model at two tree resolutions: 50 steps per year and 100 steps per year. For a particular volatility segment, you find $\sigma_3^{(50)} = 0.1425$ and $\sigma_3^{(100)} = 0.1418$. Is this level of convergence acceptable for a tolerance $\epsilon = 0.001$? Estimate the computational cost ratio between the two resolutions, assuming cost scales as $O(N_t^2)$.

??? success "Solution to Exercise 6"
    The difference between the two calibrated volatilities is

    $$
    |\sigma_3^{(50)} - \sigma_3^{(100)}| = |0.1425 - 0.1418| = 0.0007
    $$

    Since $0.0007 < \epsilon = 0.001$, this level of convergence is acceptable under the given tolerance.

    For the computational cost ratio, the tree has $N_t$ time steps, and at each step the number of nodes is proportional to $N_t$ (since $j_{\max} \propto 1/(a\Delta t) \propto N_t$). Hence the total cost scales as $O(N_t^2)$.

    With 50 steps per year, let the total steps be $N_{50}$. With 100 steps per year, the total steps double: $N_{100} = 2N_{50}$. The cost ratio is

    $$
    \frac{\text{Cost}(100)}{\text{Cost}(50)} = \frac{N_{100}^2}{N_{50}^2} = \frac{(2N_{50})^2}{N_{50}^2} = 4
    $$

    The 100-steps-per-year tree is approximately 4 times more expensive than the 50-steps-per-year tree. Since the convergence check passes ($0.0007 < 0.001$), the 50-step resolution may be sufficient for this particular segment, making the cheaper resolution preferable in production unless higher precision is required for other segments.

---

**Exercise 7.** Explain why the map from $\sigma_i$ to ATM cap implied volatility is monotone, and give an intuitive argument for why this monotonicity may break down for deep out-of-the-money caps. How does the potential for multiple local minima affect the choice between sequential and global calibration strategies?

??? success "Solution to Exercise 7"
    **Monotonicity for ATM caps**: When $\sigma_i$ increases, the log-rate volatility in the BK model increases during period $i$. This widens the distribution of $r_{T_i}$ (and hence the LIBOR rate $L(T_i, T_i, T_{i+1})$) around its forward value. For an ATM caplet, where the strike equals the forward rate, a wider distribution always increases the option value (since $\mathbb{E}[(L - K)^+]$ is increasing in the spread of $L$ when $K = \mathbb{E}[L]$). Higher caplet prices translate to higher Black implied volatilities. This monotonicity holds because:

    1. The caplet is a convex payoff centered at the forward rate.
    2. The BK model's log-normal rate distribution has its mean near the forward rate (after $\theta(t)$ calibration).
    3. Increasing $\sigma_i$ is a mean-preserving spread of the rate distribution, which increases the value of any convex payoff.

    **Breakdown for OTM caps**: For a deep out-of-the-money caplet (e.g., strike $K$ much larger than the forward rate $F_i$), the payoff region is far in the right tail. Two competing effects arise when $\sigma_i$ increases:

    - **Tail fattening**: Higher volatility pushes more probability mass into the payoff region $(L > K)$, increasing the caplet price.
    - **Forward rate shift**: The calibration condition requires that the model match the market discount factors. When $\sigma_i$ increases, $\theta(t)$ is recalibrated, which can shift the effective forward rate distribution. The log-normal convexity correction ($\mathbb{E}[r] = e^{\mu + \sigma^2/2}$) means that the forward rate implicit in the tree changes with $\sigma$.

    For deep OTM caplets, the second effect can dominate: the recalibration of $\theta(t)$ may shift the distribution in a way that reduces the probability mass beyond the strike, even though the distribution is wider. This creates a non-monotone relationship between $\sigma_i$ and OTM implied volatility.

    **Impact on calibration strategy**: The sequential (bootstrap) calibration relies on monotonicity to guarantee a unique root at each step. For ATM caps, this is ensured, making bootstrap reliable and efficient. For OTM caps, the potential non-monotonicity means that a one-dimensional root-finding step might have zero or multiple solutions. Global calibration with a robust optimizer (e.g., differential evolution or multi-start Levenberg-Marquardt) is therefore necessary when calibrating to OTM strikes, as it can navigate multiple local minima and find the globally best fit. The tradeoff is computational cost: global calibration requires rebuilding the tree at each function evaluation across all parameters simultaneously.
