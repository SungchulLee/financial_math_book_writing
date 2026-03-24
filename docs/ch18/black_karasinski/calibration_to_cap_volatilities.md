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
V_{\text{cplt}} = \delta_i\,P(0, T_{i+1})\left[F_i\,\Phi(d_1) - K\,\Phi(d_2)\right]
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

---

**Exercise 2.** Explain why calibrating $\theta(t)$ to the market yield curve must be done *before* (or simultaneously with) pricing caplets on the BK tree. What would go wrong if $\theta(t)$ were set to a constant instead of being calibrated to match market discount factors?

---

**Exercise 3.** A model caplet price is $V_{\text{cplt}} = 0.00215$, the forward LIBOR rate is $F_i = 4.5\%$, the strike is $K = 4.5\%$ (at-the-money), the discount factor is $P(0, T_{i+1}) = 0.9560$, and $\delta_i = 0.25$, $T_i = 2$. Using Black's caplet formula for ATM options (where $d_1 = \frac{1}{2}\sigma^{\text{Black}}\sqrt{T_i}$ and $d_2 = -d_1$), set up the equation that determines $\sigma^{\text{Black}}$ and describe how Newton-Raphson would be used to solve it.

---

**Exercise 4.** In the sequential (bootstrap) calibration procedure, suppose the 1Y ATM cap market volatility is 18% and the 2Y ATM cap market volatility is 20%. After step 1, you have calibrated $\sigma_1$. Explain precisely which caplets depend on $\sigma_2$ in step 2 and why fixing $\sigma_1$ from step 1 makes the problem one-dimensional.

---

**Exercise 5.** Consider the calibration objective function

$$
\min_{a,\,\sigma(\cdot)}\;\sum_{j=1}^{M} w_j\left[\sigma^{\text{model}}_j - \sigma^{\text{mkt}}_j\right]^2
$$

with uniform weights $w_j = 1$. If there are $M = 10$ ATM caps (maturities 1Y through 10Y) and piecewise-constant $\sigma(t)$ with 10 breakpoints, how many free parameters does the global calibration have? Why might a practitioner choose to fix $a$ from swaption data rather than calibrating it jointly with the $\sigma_i$?

---

**Exercise 6.** You calibrate the BK model at two tree resolutions: 50 steps per year and 100 steps per year. For a particular volatility segment, you find $\sigma_3^{(50)} = 0.1425$ and $\sigma_3^{(100)} = 0.1418$. Is this level of convergence acceptable for a tolerance $\epsilon = 0.001$? Estimate the computational cost ratio between the two resolutions, assuming cost scales as $O(N_t^2)$.

---

**Exercise 7.** Explain why the map from $\sigma_i$ to ATM cap implied volatility is monotone, and give an intuitive argument for why this monotonicity may break down for deep out-of-the-money caps. How does the potential for multiple local minima affect the choice between sequential and global calibration strategies?
