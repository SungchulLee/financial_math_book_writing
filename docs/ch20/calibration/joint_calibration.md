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

---

**Exercise 2.** The Pareto frontier traces the achievable trade-offs between cap error and swaption error as $\alpha$ varies. Describe how to compute this frontier numerically. If the frontier has a sharp elbow, what does this indicate about the model's ability to fit both markets?

---

**Exercise 3.** Explain the proposition that swaption errors have steeper dependence on $\lambda$ than cap errors. Why does this mean the joint-calibrated $\lambda$ is more strongly influenced by the swaption component, even when $\alpha = 0.5$?

---

**Exercise 4.** For application-driven weighting targeting a Bermudan swaption, describe how you would choose $\alpha$ and the individual instrument weights. Would you include all available cap maturities and swaption expiry-tenor pairs, or focus on a subset? Justify your answer.

---

**Exercise 5.** The text lists three extensions for improving the joint fit: piecewise constant $\sigma(t)$, two-factor model, and time-dependent $\lambda(t)$. For each, explain which dimension of the calibration it improves (expiry, tenor, or both) and what the trade-off is in terms of model complexity and interpretability.

---

**Exercise 6.** Describe relative error weighting $e_k^{\text{rel}} = (\sigma_k^{\text{HW}} - \sigma_k^{\text{market}})/\sigma_k^{\text{market}}$ versus absolute error weighting. When would relative weighting be preferable? Give an example where absolute weighting could lead to a poor calibration outcome.

---

**Exercise 7.** Compute the Jacobian $J$ of the residual vector $\mathbf{e}(\lambda, \sigma)$ with respect to $(\lambda, \sigma)$ for a simplified setup with two instruments: one 2-year caplet and one $2 \times 5$ swaption. Describe how the condition number of $J^{\top}J$ relates to parameter identifiability.
