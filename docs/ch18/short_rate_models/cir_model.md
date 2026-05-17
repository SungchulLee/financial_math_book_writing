# The Cox-Ingersoll-Ross (CIR) Model

The Cox-Ingersoll-Ross model (1985) is a mean-reverting short-rate model with **square-root** diffusion. Under the risk-neutral measure $\mathbb{Q}$:

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t^{\mathbb{Q}}
$$

Unlike Vasicek, CIR can ensure non-negative interest rates under the Feller condition while retaining analytical tractability. This short overview places the model in the general short-rate framework; all detailed derivations live in the dedicated **CIR model** folder.

---

## Where to find each topic

Recall (see [§ General Short-Rate Framework](general_short_rate_framework.md)): the bond pricing PDE and the expectation representation $P(t,T) = \mathbb{E}^{\mathbb{Q}}_t[\exp(-\int_t^T r_s\,ds)]$ apply to any Markov short-rate model.

Recall (see [§ Affine Term Structure](affine_term_structure.md)): CIR is the canonical square-root affine model, with bond price $P(t,T) = A(\tau)\exp(-B(\tau)r_t)$ obtained from a quadratic Riccati ODE for $B$ (since $\sigma(r)^2 = \sigma^2 r$ is affine in $r$).

| Topic | Canonical location |
|-------|--------------------|
| SDE and square-root process | [§ CIR SDE and Square-Root Process](../cir_model/cir_sde_and_square_root_process.md) |
| Feller condition $2\kappa\theta \geq \sigma^2$ and boundary at zero | [§ Feller Condition and Boundary](../cir_model/feller_condition_and_boundary.md) |
| Non-central $\chi^2$ transition density | [§ Transition Density](../cir_model/transition_density.md) |
| Zero-coupon bond pricing (Riccati ODEs, $A$ and $B$, $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$) | [§ Zero-Coupon Bond Pricing](../cir_model/zero_coupon_bond_pricing.md) |
| Named functions and Riccati derivation | [§ Named Functions and Riccati](../cir_model/named_functions_and_riccati.md) |
| Yield curve dynamics | [§ Yield Curve Dynamics](../cir_model/yield_curve_dynamics.md) |
| Bond options via non-central $\chi^2$ | [§ Bond Options](../cir_model/bond_options.md) |
| Caplet and swaption formulas | [§ Caplet and Swaption Formulas](../cir_model/caplet_and_swaption_formulas.md) |
| Change of measure | [§ Change of Measure](../cir_model/change_of_measure.md) |
| Calibration | [§ Calibration](../cir_model/calibration.md) |
| Exact simulation and Euler pitfalls | [§ Exact Simulation and Euler Pitfalls](../cir_model/exact_simulation_and_euler_pitfalls.md) |
| Monte Carlo simulation | [§ Monte Carlo Simulation](../cir_model/monte_carlo_simulation.md) |

For side-by-side comparison with Vasicek and Hull-White (including conditional moments and tractability), see [§ Vasicek vs CIR vs Hull-White](../model_comparison/vasicek_vs_cir_vs_hull_white.md).

---

## Key takeaways

- CIR: $dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t$.
- Feller condition $2\kappa\theta \geq \sigma^2$ ensures $r_t > 0$.
- Conditional distribution is scaled non-central $\chi^2$.
- Affine bond prices $P = A(\tau)e^{-B(\tau)r}$ with $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$.

---

## Further reading

- Cox, Ingersoll & Ross (1985), "A Theory of the Term Structure of Interest Rates".
- Brigo & Mercurio, *Interest Rate Models*, Chapter 3.
