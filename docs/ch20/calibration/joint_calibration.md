# Joint Calibration to Caps and Swaptions

In practice, a trading desk often needs to price both cap/floor products and swaption products using the same Hull-White model. Calibrating separately to caps and swaptions typically yields different parameter pairs $(\lambda, \sigma)$, creating inconsistency in the hedging book. Joint calibration resolves this by fitting both instrument classes simultaneously. Since the one-factor Hull-White model has only two free parameters, the joint problem is overconstrained, requiring careful weighting and trade-off decisions. This section formulates the joint calibration objective, discusses weighting strategies, and presents the optimization procedure.

## Joint Objective Function

The joint calibration minimizes a combined objective that includes both cap and swaption errors:

$$
\min_{\lambda, \sigma}\; \alpha \sum_{k=1}^{n_{\text{cap}}} w_k^{\text{cap}}\left(e_k^{\text{cap}}\right)^2 + (1-\alpha) \sum_{j=1}^{n_{\text{swap}}} w_j^{\text{swap}}\left(e_j^{\text{swap}}\right)^2
$$

where

$$
e_k^{\text{cap}} = \sigma_k^{\text{HW,cap}}(\lambda, \sigma) - \sigma_k^{\text{market,cap}}
$$

$$
e_j^{\text{swap}} = \sigma_j^{\text{HW,swap}}(\lambda, \sigma) - \sigma_j^{\text{market,swap}}
$$

and $\alpha \in [0,1]$ is the mixing parameter controlling the relative importance of caps versus swaptions.

**Special cases.** Setting $\alpha = 1$ reduces to pure cap calibration; $\alpha = 0$ reduces to pure swaption calibration. The choice $\alpha = 0.5$ gives equal weight to both instrument classes in aggregate.

## Weighting Strategies

The within-class weights $w_k^{\text{cap}}$ and $w_j^{\text{swap}}$ and the mixing parameter $\alpha$ significantly affect the calibration outcome. Common approaches include:

**Uniform weights.** Set $w_k = w_j = 1$ and choose $\alpha$ to balance the number of instruments:

$$
\alpha = \frac{n_{\text{cap}}}{n_{\text{cap}} + n_{\text{swap}}}
$$

This gives each instrument equal contribution to the total error.

**Vega weights.** Set $w_k^{\text{cap}} = \nu_k^{\text{cap}}$ and $w_j^{\text{swap}} = \nu_j^{\text{swap}}$ where $\nu$ is the Black vega. This gives more weight to instruments where the model's pricing error has a larger dollar impact.

**Relative weights.** Use percentage errors instead of absolute errors:

$$
e_k^{\text{cap,rel}} = \frac{\sigma_k^{\text{HW,cap}} - \sigma_k^{\text{market,cap}}}{\sigma_k^{\text{market,cap}}}
$$

This prevents high-volatility instruments from dominating the calibration.

**Application-driven weights.** When the model will be used primarily for Bermudan swaption pricing, set $\alpha$ close to $0$ (swaption-dominated) and concentrate the swaption weights on co-terminal entries.

!!! warning "Overconstrained Problem"
    With two parameters and typically 10--30 calibration instruments, the joint problem is highly overconstrained. The residual errors are a feature of the model's limited flexibility, not a failure of the optimization. The goal is to minimize the most important errors, not to eliminate all errors.

## Sensitivity Analysis

The sensitivity of the calibrated parameters to the mixing weight $\alpha$ reveals the tension between cap and swaption fitting:

$$
\frac{\partial \lambda^*}{\partial \alpha}, \quad \frac{\partial \sigma^*}{\partial \alpha}
$$

Typically, cap calibration prefers lower $\lambda$ (to match the relatively flat caplet volatility term structure), while swaption calibration prefers higher $\lambda$ (to produce sufficient tenor-dependent decorrelation). The joint calibrated $\lambda$ is a compromise between these two preferences.

**Proposition.** If the model-implied cap volatilities are less sensitive to $\lambda$ than the swaption volatilities (which is typically true for at-the-money instruments), then the joint calibrated $\lambda$ is more strongly influenced by the swaption component, even for $\alpha = 0.5$.

???+ note "Proof sketch"
    The gradient of the cap error with respect to $\lambda$ involves $\partial \sigma_P / \partial \lambda$, which is proportional to $(1-e^{-\lambda\delta_k})/\lambda^2$. For short-dated caplets ($\delta_k$ small), this sensitivity is small. The gradient of the swaption error involves $\partial B(T_0, T_i)/\partial\lambda$, which is proportional to $(T_i - T_0)e^{-\lambda(T_i-T_0)}/\lambda^2$ and is large for long tenors. Therefore, the swaption error has a steeper dependence on $\lambda$, making the optimizer effectively more responsive to the swaption component. $\square$

## Optimization Algorithm

**Algorithm (Joint Calibration).**

1. **Initialize**: use parameters from a cap-only calibration as starting point
2. **Define objective**: combine cap and swaption errors with chosen weights and $\alpha$
3. **Optimize**: use Levenberg-Marquardt (for least-squares structure) or L-BFGS-B (with box constraints $\lambda > 0$, $\sigma > 0$):

$$
(\lambda^*, \sigma^*) = \arg\min_{\lambda > 0,\, \sigma > 0}\; f(\lambda, \sigma)
$$

4. **Report**: print the residual errors for each instrument to assess fit quality

The Jacobian of the residual vector $\mathbf{e}(\lambda, \sigma) = (e_1^{\text{cap}}, \ldots, e_{n_\text{cap}}^{\text{cap}}, e_1^{\text{swap}}, \ldots, e_{n_\text{swap}}^{\text{swap}})^{\top}$ can be computed by finite differences or, for the approximate volatility formulas, analytically.

???+ example "Joint Calibration Implementation"
    ```python
    def main():
        hw = HullWhite(sigma=0.01, lambd=0.05, P=P_market)

        # Market data
        cap_maturities = [1, 2, 3, 5, 7, 10]
        cap_vols = [0.25, 0.24, 0.23, 0.20, 0.18, 0.16]
        swap_expiries = [1, 2, 5, 10]
        swap_tenors = [5, 5, 5, 5]
        swap_vols = [0.22, 0.20, 0.18, 0.15]

        alpha = 0.5

        def objective(params):
            lambd, sigma = params
            hw.lambd = lambd
            hw.sigma = sigma

            cap_err = [hw.implied_caplet_vol(T) - s
                       for T, s in zip(cap_maturities, cap_vols)]
            swap_err = [hw.implied_swaption_vol(T0, tn) - s
                        for T0, tn, s in zip(swap_expiries, swap_tenors, swap_vols)]

            return (alpha * np.sum(np.array(cap_err)**2)
                    + (1-alpha) * np.sum(np.array(swap_err)**2))

        from scipy.optimize import minimize
        result = minimize(objective, [0.05, 0.01],
                         method='L-BFGS-B',
                         bounds=[(0.001, 1.0), (0.0001, 0.1)])
        print(f"lambda={result.x[0]:.4f}, sigma={result.x[1]:.6f}")
    ```

## Pareto Frontier

By varying $\alpha$ from $0$ to $1$, the joint calibration traces out a Pareto frontier in the (cap error, swaption error) plane. Each point on the frontier represents an optimal trade-off: reducing the cap error necessarily increases the swaption error, and vice versa.

The Pareto frontier provides useful diagnostic information:

- If the frontier is steep near $\alpha = 0$, then a small sacrifice in swaption fit yields a large improvement in cap fit
- If the frontier is flat, then the model fits both instruments roughly equally well regardless of $\alpha$
- A large gap between the two axes indicates that the two-parameter model cannot fit both markets well, motivating extensions

## Extensions for Better Joint Fit

When the two-parameter model's joint fit is inadequate, several extensions can help:

1. **Piecewise constant $\sigma(t)$**: adds degrees of freedom along the time dimension, improving cap fit without affecting the swaption tenor structure
2. **Two-factor model**: adds parameters $(\lambda_2, \sigma_2, \rho)$ that independently control tenor-dependent decorrelation, dramatically improving swaption matrix fit
3. **Time-dependent $\lambda(t)$**: rarely used because it makes the model non-stationary and harder to interpret

## Summary

Joint calibration to caps and swaptions minimizes a combined objective $\alpha\,\text{cap error} + (1-\alpha)\,\text{swaption error}$ with the mixing parameter $\alpha$ controlling the trade-off. The two-parameter model is overconstrained, and the Pareto frontier reveals the achievable trade-offs. Cap calibration primarily constrains $\sigma$, while swaption calibration constrains $\lambda$ through tenor-dependent bond volatility. Application-driven weighting (e.g., co-terminal swaptions for Bermudan pricing) focuses the fit on the most relevant instruments. When the joint fit is inadequate, piecewise constant volatility or the two-factor extension provides additional flexibility.

---

## Exercises

**Exercise 1.** The joint objective uses a mixing parameter $\alpha \in [0,1]$. If the cap market quotes 8 caplet volatilities and the swaption market quotes 6 swaption volatilities, what value of $\alpha$ gives each individual instrument equal weight? Show that $\alpha = n_{\text{cap}}/(n_{\text{cap}} + n_{\text{swap}})$ achieves this.

??? success "Solution to Exercise 1"
    With $n_{\text{cap}} = 8$ caplet volatilities and $n_{\text{swap}} = 6$ swaption volatilities, the joint objective is

    $$
    \alpha \sum_{k=1}^{8} w_k^{\text{cap}} (e_k^{\text{cap}})^2 + (1 - \alpha) \sum_{j=1}^{6} w_j^{\text{swap}} (e_j^{\text{swap}})^2
    $$

    With uniform within-class weights $w_k^{\text{cap}} = w_j^{\text{swap}} = 1$, the total contribution of the cap term is $\alpha \times 8 \times \text{(average squared error)}$ and the swaption term is $(1-\alpha) \times 6 \times \text{(average squared error)}$.

    For each individual instrument to have equal weight, we need:

    $$
    \alpha \cdot w_k^{\text{cap}} = (1-\alpha) \cdot w_j^{\text{swap}} \quad \text{for all } k, j
    $$

    With $w_k = w_j = 1$, this requires $\alpha = 1 - \alpha \cdot n_{\text{cap}} / n_{\text{swap}}$... Let us think more carefully. Each cap instrument contributes $\alpha \cdot 1 \cdot (e_k^{\text{cap}})^2$ to the objective, and each swaption instrument contributes $(1-\alpha) \cdot 1 \cdot (e_j^{\text{swap}})^2$. For equal per-instrument weight, we need:

    $$
    \alpha = 1 - \alpha \implies \text{(this only works if } n_{\text{cap}} = n_{\text{swap}}\text{)}
    $$

    More precisely, the effective weight on each cap instrument is $\alpha$ and on each swaption instrument is $(1-\alpha)$. For these to be equal:

    $$
    \alpha = 1 - \alpha \implies \alpha = 0.5
    $$

    But this does not account for the different number of instruments. The total weight allocated to caps is $\alpha \cdot n_{\text{cap}}$ and to swaptions is $(1-\alpha) \cdot n_{\text{swap}}$. For each instrument to receive the same share of the total weight $\alpha \cdot n_{\text{cap}} + (1-\alpha) \cdot n_{\text{swap}}$, we need the per-instrument weight to be equal:

    $$
    \alpha = 1 - \alpha \quad \Longleftrightarrow \quad \alpha = \frac{1}{2}
    $$

    However, the formulation $\alpha = n_{\text{cap}}/(n_{\text{cap}} + n_{\text{swap}})$ achieves a different kind of balance. With this choice:

    $$
    \alpha = \frac{8}{8 + 6} = \frac{8}{14} = \frac{4}{7}
    $$

    The total cap contribution is $\frac{8}{14} \times \sum_{k=1}^{8}(e_k^{\text{cap}})^2$ and the total swaption contribution is $\frac{6}{14} \times \sum_{j=1}^{6}(e_j^{\text{swap}})^2$. The effective per-instrument weight is:

    $$
    \text{Cap: } \frac{\alpha}{n_{\text{cap}}} = \frac{8/14}{8} = \frac{1}{14}, \quad \text{Swaption: } \frac{1-\alpha}{n_{\text{swap}}} = \frac{6/14}{6} = \frac{1}{14}
    $$

    Each instrument receives weight $1/(n_{\text{cap}} + n_{\text{swap}}) = 1/14$, confirming equal per-instrument contribution. The formula $\alpha = n_{\text{cap}}/(n_{\text{cap}} + n_{\text{swap}})$ normalizes the mixing parameter so that the per-instrument weight is the same regardless of how many instruments are in each class.

---

**Exercise 2.** The Pareto frontier traces the achievable trade-offs between cap error and swaption error as $\alpha$ varies. Describe how to compute this frontier numerically. If the frontier has a sharp elbow, what does this indicate about the model's ability to fit both markets?

??? success "Solution to Exercise 2"
    **Computing the Pareto frontier numerically:**

    1. Choose a grid of $\alpha$ values: $\alpha \in \{0.0, 0.05, 0.10, \ldots, 0.95, 1.0\}$
    2. For each $\alpha$, solve the joint calibration:

    $$
    (\lambda^*(\alpha), \sigma^*(\alpha)) = \arg\min_{\lambda, \sigma} \; \alpha \sum_k (e_k^{\text{cap}})^2 + (1-\alpha) \sum_j (e_j^{\text{swap}})^2
    $$

    3. Evaluate the two individual error components at the optimum:

    $$
    E_{\text{cap}}(\alpha) = \sum_k (e_k^{\text{cap}}(\lambda^*(\alpha), \sigma^*(\alpha)))^2
    $$

    $$
    E_{\text{swap}}(\alpha) = \sum_j (e_j^{\text{swap}}(\lambda^*(\alpha), \sigma^*(\alpha)))^2
    $$

    4. Plot the points $(E_{\text{cap}}(\alpha), E_{\text{swap}}(\alpha))$ in the cap-error vs. swaption-error plane. The resulting curve is the Pareto frontier.

    The frontier is convex (or at least non-crossing) because each point represents an optimal trade-off: no feasible parameter pair can reduce both errors simultaneously below the frontier.

    **Interpretation of a sharp elbow**: A sharp elbow in the Pareto frontier indicates that there exists a natural compromise point where both errors are reasonably small. Near the elbow:

    - Moving along the frontier in the cap-reducing direction gives a large reduction in cap error for a small increase in swaption error
    - Moving in the swaption-reducing direction gives a large reduction in swaption error for a small increase in cap error

    A sharp elbow suggests the model can fit both markets reasonably well with the right $\alpha$, and the optimal operating point is near the elbow. Conversely, if the frontier is smooth without a clear elbow, the trade-off is gradual, and there is no natural compromise --- the choice of $\alpha$ becomes a subjective decision about which market to prioritize.

---

**Exercise 3.** Explain the proposition that swaption errors have steeper dependence on $\lambda$ than cap errors. Why does this mean the joint-calibrated $\lambda$ is more strongly influenced by the swaption component, even when $\alpha = 0.5$?

??? success "Solution to Exercise 3"
    The proposition states that swaption errors have steeper dependence on $\lambda$ than cap errors. The key sensitivities are:

    **Cap sensitivity to $\lambda$**: The caplet bond price volatility involves

    $$
    \frac{\partial \sigma_P}{\partial \lambda} \propto \frac{\partial}{\partial \lambda}\left[\frac{1 - e^{-\lambda\delta_k}}{\lambda}\right]
    $$

    For short-dated caplets with $\lambda\delta_k \ll 1$, the Taylor expansion gives $(1 - e^{-\lambda\delta_k})/\lambda \approx \delta_k - \lambda\delta_k^2/2$, so the derivative is approximately $-\delta_k^2/2$, which is small for typical accrual periods $\delta_k \leq 1$.

    **Swaption sensitivity to $\lambda$**: The swaption volatility involves $B(T_0, T_i) = (e^{-\lambda(T_i - T_0)} - 1)/\lambda$, and

    $$
    \frac{\partial B(T_0, T_i)}{\partial \lambda} = \frac{-(T_i - T_0)e^{-\lambda(T_i - T_0)}}{\lambda} - \frac{e^{-\lambda(T_i - T_0)} - 1}{\lambda^2}
    $$

    For long tenors (large $T_i - T_0$), this derivative is of order $(T_i - T_0)/\lambda^2$, which is much larger than the cap sensitivity.

    **Consequence for joint calibration**: At the optimum $(\lambda^*, \sigma^*)$, the first-order condition is

    $$
    \alpha \sum_k 2e_k^{\text{cap}} \frac{\partial e_k^{\text{cap}}}{\partial \lambda} + (1-\alpha) \sum_j 2e_j^{\text{swap}} \frac{\partial e_j^{\text{swap}}}{\partial \lambda} = 0
    $$

    Since $|\partial e_j^{\text{swap}}/\partial \lambda| \gg |\partial e_k^{\text{cap}}/\partial \lambda|$, the swaption term dominates this equation even when $\alpha = 0.5$ (equal mixing). The optimizer effectively adjusts $\lambda$ primarily to reduce swaption errors because the gradient from the swaption component is steeper. The cap component has little influence on $\lambda$ because cap prices are relatively insensitive to it. In other words, the swaption data acts as a stronger constraint on $\lambda$, and the joint-calibrated $\lambda$ is pulled toward the swaption-only optimal value.

---

**Exercise 4.** For application-driven weighting targeting a Bermudan swaption, describe how you would choose $\alpha$ and the individual instrument weights. Would you include all available cap maturities and swaption expiry-tenor pairs, or focus on a subset? Justify your answer.

??? success "Solution to Exercise 4"
    For pricing a 10-year Bermudan swaption with annual exercise, the calibration should be designed to match the instruments most relevant to the Bermudan's value.

    **Choosing $\alpha$**: Set $\alpha$ close to $0$ (e.g., $\alpha = 0.1$ or even $\alpha = 0$), heavily favoring the swaption component. The Bermudan swaption's value depends on European swaption prices at each exercise date, not on caplet prices. Including a small cap component ($\alpha > 0$) can help stabilize the calibration by constraining $\sigma$ from the overall volatility level.

    **Instrument selection**: Do not include all available instruments. Focus on:

    1. **Co-terminal swaptions** (essential): $1\times9$, $2\times8$, $3\times7$, ..., $9\times1$, all terminating at year 10. Set $w_j^{\text{swap}} = 1$ for these and $w_j^{\text{swap}} = 0$ for non-co-terminal swaptions.
    2. **A few key caplets** (optional, for stability): Include 2--3 caplets at maturities that overlap with the Bermudan's exercise window (e.g., 2Y, 5Y, 10Y). Set their weights low relative to the swaptions.

    **Justification**: The Bermudan swaption at each exercise date $T_k$ compares the exercise value (determined by the $k \times (10-k)$ co-terminal swaption) against the continuation value. The model must price these co-terminal swaptions correctly to determine the optimal exercise boundary. Non-co-terminal swaptions (e.g., $5\times2$, terminating at year 7) do not correspond to any exercise decision and are irrelevant. Including them would distort the calibration by forcing the limited parameters to compromise between relevant and irrelevant instruments.

    Including all available cap maturities and the full swaption matrix would dilute the fit quality on the critical co-terminal instruments. With only two parameters, every additional instrument reduces the average quality of fit per instrument; concentrating on the most important instruments maximizes the calibration's effectiveness for the specific pricing task.

---

**Exercise 5.** The text lists three extensions for improving the joint fit: piecewise constant $\sigma(t)$, two-factor model, and time-dependent $\lambda(t)$. For each, explain which dimension of the calibration it improves (expiry, tenor, or both) and what the trade-off is in terms of model complexity and interpretability.

??? success "Solution to Exercise 5"
    **Piecewise constant $\sigma(t)$**:

    - **Dimension improved**: Expiry dimension. Each volatility segment $\sigma_k$ for $t \in [T_{k-1}, T_k)$ independently controls the model volatility for caplets resetting in that period. This adds $n-1$ extra degrees of freedom along the time axis.
    - **Limitation**: Does not help with the tenor dimension. The tenor-dependent decorrelation is still controlled by a single $\lambda$, so the swaption matrix misfit along the tenor direction persists.
    - **Trade-off**: More parameters ($n$ instead of 2) increase the risk of overfitting and reduce parameter stability. The piecewise constant function may be non-smooth. However, the model remains one-factor and analytically tractable.

    **Two-factor model** ($\lambda_1, \lambda_2, \sigma_1, \sigma_2, \rho$):

    - **Dimension improved**: Primarily the tenor dimension, and to some extent both. The two factors introduce imperfect correlation between rates at different maturities, allowing the model to fit the swaption matrix along the tenor direction. The two mean-reversion speeds create a richer decorrelation structure.
    - **Trade-off**: Five parameters instead of two; the model is more complex to implement and calibrate. Jamshidian's trick does not directly apply (since bond prices are not monotone functions of a single state variable), requiring numerical methods for swaption pricing. Parameter identifiability can be challenging with five parameters.

    **Time-dependent $\lambda(t)$**:

    - **Dimension improved**: In principle, both expiry and tenor, since $\lambda(t)$ affects the bond price volatility function $B(t, T)$ in a time-varying way.
    - **Trade-off**: The model becomes non-stationary, meaning the distribution of rates depends on the current time, not just the time-to-maturity. This complicates interpretation, hedging, and the construction of trees/grids. The function $\lambda(t)$ is difficult to calibrate stably, and different parameterizations can produce very different behavior. For these reasons, time-dependent $\lambda(t)$ is rarely used in practice; the other two extensions are preferred.

---

**Exercise 6.** Describe relative error weighting $e_k^{\text{rel}} = (\sigma_k^{\text{HW}} - \sigma_k^{\text{market}})/\sigma_k^{\text{market}}$ versus absolute error weighting. When would relative weighting be preferable? Give an example where absolute weighting could lead to a poor calibration outcome.

??? success "Solution to Exercise 6"
    **Relative error weighting** uses

    $$
    e_k^{\text{rel}} = \frac{\sigma_k^{\text{HW}} - \sigma_k^{\text{market}}}{\sigma_k^{\text{market}}}
    $$

    so the objective becomes $\sum_k w_k (e_k^{\text{rel}})^2 = \sum_k w_k \left(\frac{\sigma_k^{\text{HW}} - \sigma_k^{\text{market}}}{\sigma_k^{\text{market}}}\right)^2$.

    **Absolute error weighting** uses $e_k^{\text{abs}} = \sigma_k^{\text{HW}} - \sigma_k^{\text{market}}$ directly.

    **When relative weighting is preferable**: When the calibration instruments span a wide range of volatility levels. For example, if short-maturity caplet volatilities are around 25% and long-maturity caplet volatilities are around 10%, a 1-vol-point absolute error is 4% relative for the short caplet but 10% relative for the long caplet. Absolute weighting treats both errors equally, while relative weighting recognizes that the long-maturity error is proportionally more severe.

    **Example of poor absolute weighting**: Consider calibrating jointly to caps and swaptions where:

    - Short-maturity cap volatilities: $\sigma_1^{\text{market}} = 0.30$, $\sigma_2^{\text{market}} = 0.28$
    - Long-tenor swaption volatilities: $\sigma_3^{\text{market}} = 0.08$, $\sigma_4^{\text{market}} = 0.07$

    With absolute weighting, the optimizer focuses on minimizing errors for the high-volatility instruments (caps) because a given percentage misfit produces a larger absolute error. Suppose the calibrated model gives:

    - $\sigma_1^{\text{HW}} = 0.299$ (error $= -0.001$, or 0.3%)
    - $\sigma_2^{\text{HW}} = 0.279$ (error $= -0.001$, or 0.4%)
    - $\sigma_3^{\text{HW}} = 0.072$ (error $= -0.008$, or 10%)
    - $\sigma_4^{\text{HW}} = 0.062$ (error $= -0.008$, or 11%)

    The total absolute squared error is $2 \times 0.001^2 + 2 \times 0.008^2 = 0.000130$, dominated by the swaption errors. But the optimizer sees these as small because they are dwarfed by what could have been large cap errors. The result is that the low-volatility swaptions are poorly fit in percentage terms (10--11% error) while the high-volatility caps are very precisely fit (0.3--0.4% error). Relative weighting would equalize the percentage errors across instruments, producing a more balanced calibration.

---

**Exercise 7.** Compute the Jacobian $J$ of the residual vector $\mathbf{e}(\lambda, \sigma)$ with respect to $(\lambda, \sigma)$ for a simplified setup with two instruments: one 2-year caplet and one $2 \times 5$ swaption. Describe how the condition number of $J^{\top}J$ relates to parameter identifiability.

??? success "Solution to Exercise 7"
    The residual vector is $\mathbf{e}(\lambda, \sigma) = (e_1^{\text{cap}}, e_2^{\text{swap}})^\top$ where $e_1^{\text{cap}} = \sigma_{\text{caplet,2Y}}^{\text{HW}}(\lambda, \sigma) - \sigma_{\text{caplet,2Y}}^{\text{market}}$ and $e_2^{\text{swap}} = \sigma_{2\times5}^{\text{HW}}(\lambda, \sigma) - \sigma_{2\times5}^{\text{market}}$.

    The Jacobian is the $2 \times 2$ matrix:

    $$
    J = \begin{pmatrix} \frac{\partial e_1^{\text{cap}}}{\partial \lambda} & \frac{\partial e_1^{\text{cap}}}{\partial \sigma} \\ \frac{\partial e_2^{\text{swap}}}{\partial \lambda} & \frac{\partial e_2^{\text{swap}}}{\partial \sigma} \end{pmatrix}
    $$

    **Caplet row**: The 2-year caplet (reset at $T_{k-1} = 2$, payment at $T_k = 3$) has bond price volatility $\sigma_P = \frac{\sigma}{\lambda}(1 - e^{-\lambda})\sqrt{\frac{1 - e^{-4\lambda}}{2\lambda}}$. The derivatives are:

    $$
    \frac{\partial e_1}{\partial \sigma} = \frac{1}{\lambda}(1 - e^{-\lambda})\sqrt{\frac{1 - e^{-4\lambda}}{2\lambda}} \cdot C_1 > 0
    $$

    where $C_1$ is a positive constant from converting $\sigma_P$ to implied Black vol. The derivative $\partial e_1/\partial \lambda$ is more complex but typically small for short-dated caplets.

    **Swaption row**: The $2 \times 5$ swaption (expiry $T_0 = 2$, tenor 5 years) involves $B(2, T_i)$ for $T_i = 3, 4, 5, 6, 7$. The sensitivity $\partial e_2/\partial \lambda$ is large because the 5-year tenor creates significant variation in $B$ across the payment dates.

    $$
    \frac{\partial e_2}{\partial \sigma} \propto \frac{2\sigma \cdot (\text{bond vol terms})}{2\sigma_S^{\text{HW}}} > 0
    $$

    $$
    \frac{\partial e_2}{\partial \lambda} \propto \sum_{i} w_i \frac{\partial B(2, T_i)}{\partial \lambda} \cdot (\text{other terms})
    $$

    **Condition number and identifiability**: The matrix $J^\top J$ is $2 \times 2$ with eigenvalues $\lambda_{\max}$ and $\lambda_{\min}$. The condition number is $\kappa = \lambda_{\max}/\lambda_{\min}$.

    - **Small $\kappa$ (close to 1)**: The rows of $J$ are nearly orthogonal, meaning the two instruments constrain $\lambda$ and $\sigma$ in independent directions. Both parameters are well-identified, and small perturbations in market data produce small, predictable changes in the calibrated parameters.

    - **Large $\kappa$ ($\gg 1$)**: The rows of $J$ are nearly parallel, meaning both instruments provide similar information about the parameters. There exists a direction in $(\lambda, \sigma)$ space along which the objective function is nearly flat, so the parameters are poorly identified in that direction. Small market data perturbations can cause large swings in the calibrated parameters along the poorly-identified direction.

    For the caplet-swaption pair, the condition number is typically moderate because the caplet primarily constrains $\sigma$ (through the overall volatility level) while the swaption constrains a combination of $\lambda$ and $\sigma$ (through the tenor-dependent bond volatility). The two instruments provide somewhat complementary information, leading to reasonable identifiability. If both instruments were caplets of similar maturity, the condition number would be much larger because they would provide redundant information about $\sigma$ and little information about $\lambda$.
