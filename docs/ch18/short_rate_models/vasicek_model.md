# The Vasicek Model

The Vasicek model (1977) is the foundational mean-reverting short-rate model in the affine class. Under the risk-neutral measure $\mathbb{Q}$, the short rate follows an Ornstein-Uhlenbeck process:

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t^{\mathbb{Q}}
$$

This short overview places the model in the general short-rate framework. All detailed derivations live in the dedicated **Vasicek model** folder.

---

## Where to find each topic

Recall (see [§ General Short-Rate Framework](general_short_rate_framework.md)): the bond pricing PDE and the expectation $P(t,T) = \mathbb{E}^{\mathbb{Q}}_t[\exp(-\int_t^T r_s\,ds)]$ apply to any Markov short-rate model, including Vasicek.

Recall (see [§ Affine Term Structure](affine_term_structure.md)): Vasicek is the canonical Gaussian affine model, with bond price $P(t,T) = \exp(A(\tau) - B(\tau)r_t)$ arising from Riccati ODEs (linear in this case since $\sigma$ is constant in $r$).

| Topic | Canonical location |
|-------|--------------------|
| SDE and OU representation | [§ Vasicek SDE and OU Process](../vasicek_model/vasicek_sde_and_ou_process.md) |
| Explicit solution and Gaussian distribution of $r_t$ | [§ Explicit Solution and Distribution](../vasicek_model/explicit_solution_and_distribution.md) |
| Zero-coupon bond pricing (PDE, ansatz, $A$ and $B$ formulas) | [§ Zero-Coupon Bond Pricing](../vasicek_model/zero_coupon_bond_pricing.md) |
| Yield curve shapes and inversions | [§ Yield Curve Shapes and Inversions](../vasicek_model/yield_curve_shapes_and_inversions.md) |
| Change of measure and market price of risk | [§ Change of Measure](../vasicek_model/change_of_measure.md) |
| Bond options via Jamshidian | [§ Bond Options (Jamshidian)](../vasicek_model/bond_options_jamshidian.md) |
| Caplets and swaptions | [§ Caplet and Swaption Formulas](../vasicek_model/caplet_and_swaption_formulas.md) |
| Negative rates | [§ Negative Rate Problem](../vasicek_model/negative_rate_problem.md) |
| Calibration | [§ Calibration](../vasicek_model/calibration.md) |
| Monte Carlo simulation | [§ Monte Carlo Simulation](../vasicek_model/monte_carlo_simulation.md) |

For Hull-White's time-dependent drift extension that fits the initial curve exactly, see [§ Hull-White Model](hull_white_model.md). For side-by-side comparisons with CIR and Hull-White, see [§ Vasicek vs CIR vs Hull-White](../model_comparison/vasicek_vs_cir_vs_hull_white.md).

---

## Key takeaways

- Vasicek: $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$, Ornstein-Uhlenbeck dynamics.
- Short rate is Gaussian: closed forms but negative rates possible.
- Affine bond prices: $P(t,T) = \exp(A(\tau) - B(\tau)r_t)$ with $B(\tau) = (1 - e^{-\kappa\tau})/\kappa$.
- Hull-White extends Vasicek with $\theta(t)$ for exact curve fit.

---

## Further reading

- Vasicek, O. (1977), "An Equilibrium Characterization of the Term Structure".
- Hull & White (1990), "Pricing Interest-Rate-Derivative Securities".
- Brigo & Mercurio, *Interest Rate Models*, Chapter 3.
