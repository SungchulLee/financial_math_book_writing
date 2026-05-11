# Hybrid Model-Based / Data-Driven Approaches


**Hybrid approaches** combine traditional financial models with data-driven learning to leverage the strengths of both paradigms.

---

## Motivation for hybrid models


Pure model-based approaches:

- offer interpretability and structure,
- may be too rigid.

Pure data-driven approaches:

- offer flexibility,
- may violate financial principles.

Hybrid models bridge this gap.

---

## Forms of hybridization


Common strategies include:

- learning residuals on top of parametric models,
- using ML to calibrate or adapt model parameters,
- embedding financial models within neural architectures.

---

## Benefits in practice


Hybrid approaches:

- improve data efficiency,
- preserve no-arbitrage structure,
- enhance stability and interpretability.

They are widely adopted in practice.

---

## Applications


Examples include:

- volatility surface modeling,
- yield curve fitting,
- execution and impact modeling.

Hybrid models often outperform purely data-driven ones.

---

## Key takeaways


- Hybrid models balance structure and flexibility.
- They respect financial constraints.
- They are well-suited for regulated environments.

---

## Further reading


- Sirignano & Cont, universal features.
- Buehler et al., hybrid ML in finance.

---

## Exercises

**Exercise 1.** A hybrid volatility surface model uses Black-Scholes as a base and a neural network to learn the residual: $\hat{\sigma}(K,T) = \sigma_{\text{BS}}(K,T) + \mathcal{N}_\theta(K,T)$, where $\sigma_{\text{BS}}$ is a simple parametric fit and $\mathcal{N}_\theta$ captures the remaining structure. Explain why this residual learning approach is more data-efficient than training a neural network from scratch. What happens to the hybrid model's behavior in regions where market data is sparse?

??? success "Solution to Exercise 1"
    **Why residual learning is more data-efficient.**

    In the hybrid model $\hat{\sigma}(K,T) = \sigma_{\text{BS}}(K,T) + \mathcal{N}_\theta(K,T)$, the parametric base $\sigma_{\text{BS}}(K,T)$ already captures the dominant structure of the implied volatility surface---the approximate level, basic term structure, and rough moneyness dependence. The neural network $\mathcal{N}_\theta$ only needs to learn the **residual**: the difference between the true surface and the parametric approximation.

    This is more data-efficient than training from scratch for several reasons:

    1. **Reduced target complexity.** The residual $\sigma_{\text{market}}(K,T) - \sigma_{\text{BS}}(K,T)$ is typically much smaller in magnitude and smoother than the full surface $\sigma_{\text{market}}(K,T)$. A smaller, simpler target requires fewer parameters and fewer training examples to learn accurately.

    2. **Better initialization.** At initialization (before training), the hybrid model already produces reasonable implied volatilities via $\sigma_{\text{BS}}$. A from-scratch neural network starts from random weights and must learn the entire surface, including basic features like the ATM level, which is wasteful.

    3. **Reduced overfitting.** The neural network correction $\mathcal{N}_\theta$ can be kept small (few layers, few neurons, strong regularization) because it only needs to capture residual patterns. This reduces the risk of overfitting compared to a large network learning the full surface.

    **Behavior in data-sparse regions.**

    When market data is sparse (e.g., long-dated deep OTM options), the neural network receives few training signals and its output $\mathcal{N}_\theta(K,T)$ will be approximately zero (especially with L2 regularization or weight decay that shrinks the correction toward zero). Consequently, the hybrid model gracefully falls back to the parametric base:

    $$
    \hat{\sigma}(K,T) \approx \sigma_{\text{BS}}(K,T) \quad \text{in data-sparse regions}
    $$

    This is a critical advantage: the parametric model provides a sensible default based on financial theory, while the neural network improves the fit only where sufficient data supports a correction. A from-scratch neural network, by contrast, may produce erratic or financially implausible outputs in data-sparse regions.

---

**Exercise 2.** Consider a yield curve model where the Nelson-Siegel parametric form provides the base curve and a neural network corrects for mispricing. Write the hybrid model as $y(\tau) = y_{\text{NS}}(\tau; \beta_0, \beta_1, \beta_2, \lambda) + \mathcal{N}_\theta(\tau)$. Discuss how this preserves the interpretability of the Nelson-Siegel factors (level, slope, curvature) while allowing the neural network to capture anomalies. What regularization on $\mathcal{N}_\theta$ would you apply to keep corrections small?

??? success "Solution to Exercise 2"
    **Hybrid yield curve model.**

    The Nelson-Siegel parametric form is:

    $$
    y_{\text{NS}}(\tau; \beta_0, \beta_1, \beta_2, \lambda) = \beta_0 + \beta_1 \left(\frac{1 - e^{-\lambda\tau}}{\lambda\tau}\right) + \beta_2 \left(\frac{1 - e^{-\lambda\tau}}{\lambda\tau} - e^{-\lambda\tau}\right)
    $$

    where:

    - $\beta_0$ = long-run yield level
    - $\beta_1$ = slope (short-term vs long-term)
    - $\beta_2$ = curvature (medium-term hump)
    - $\lambda$ = decay rate controlling the location of the curvature peak

    The hybrid model is:

    $$
    y(\tau) = y_{\text{NS}}(\tau; \beta_0, \beta_1, \beta_2, \lambda) + \mathcal{N}_\theta(\tau)
    $$

    **Preservation of interpretability.** The Nelson-Siegel factors retain their economic interpretation regardless of the neural network correction:

    - A change in $\beta_0$ still represents a parallel shift in the yield curve.
    - A change in $\beta_1$ still represents a slope change (steepening/flattening).
    - A change in $\beta_2$ still represents a curvature change (butterfly movement).

    The neural network $\mathcal{N}_\theta(\tau)$ captures anomalies that the three-factor model misses: localized mispricing, liquidity effects at specific tenors, or regulatory-driven distortions (e.g., special repo rates affecting specific maturities).

    **Regularization to keep corrections small.** Several regularization strategies are appropriate:

    1. **L2 regularization on the correction:**

        $$
        \mathcal{L}_{\text{reg}} = \lambda_1 \int_0^{T_{\max}} |\mathcal{N}_\theta(\tau)|^2 \, d\tau \approx \lambda_1 \sum_j |\mathcal{N}_\theta(\tau_j)|^2
        $$

        This penalizes large deviations from the Nelson-Siegel base, ensuring the correction is small.

    2. **Smoothness penalty on the correction:**

        $$
        \mathcal{L}_{\text{smooth}} = \lambda_2 \int_0^{T_{\max}} |\mathcal{N}_\theta''(\tau)|^2 \, d\tau
        $$

        This prevents the neural network from introducing oscillations or non-smooth features into the yield curve.

    3. **Weight decay on network parameters:** Standard L2 regularization on $\theta$ shrinks the network toward zero output, providing implicit control on the correction magnitude.

    The combined loss is:

    $$
    \mathcal{L} = \sum_i \big[y_{\text{market}}(\tau_i) - y_{\text{NS}}(\tau_i) - \mathcal{N}_\theta(\tau_i)\big]^2 + \lambda_1 \|\mathcal{N}_\theta\|^2 + \lambda_2 \|\mathcal{N}_\theta''\|^2
    $$

    With appropriate $\lambda_1, \lambda_2 > 0$, the neural network correction remains small and smooth, activating only where the data strongly supports a deviation from the Nelson-Siegel model.

---

**Exercise 3.** A bank uses an ML model to dynamically calibrate the parameters of a Heston stochastic volatility model: $(\kappa, \bar{v}, \xi, \rho) = g_\theta(\text{market features})$, where $g_\theta$ is a neural network mapping observable market data to Heston parameters. Explain how this is a hybrid approach. What constraints should be placed on the output of $g_\theta$ to ensure the Heston model remains well-defined (e.g., Feller condition $2\kappa\bar{v} > \xi^2$)?

??? success "Solution to Exercise 3"
    **Hybrid nature of the approach.**

    The model $(\kappa, \bar{v}, \xi, \rho) = g_\theta(\text{market features})$ is hybrid because:

    - The **pricing engine** is the classical Heston stochastic volatility model, which provides a theoretically grounded, no-arbitrage framework for option pricing.
    - The **calibration step** is replaced by a neural network $g_\theta$ that maps observable market features (e.g., ATM implied volatility, skew slope, term structure shape, recent returns) directly to Heston parameters.

    This combines the structural guarantees of Heston (correct asymptotic behavior, no-arbitrage, well-understood Greeks) with the speed and adaptability of neural network inference (avoiding the expensive iterative optimization of traditional calibration).

    **Constraints on the output of $g_\theta$.**

    The Heston model is well-defined only when its parameters satisfy certain conditions. The output layer of $g_\theta$ must enforce:

    1. **Mean-reversion speed:** $\kappa > 0$. Use softplus activation: $\kappa = \log(1 + e^{h_\kappa})$.

    2. **Long-run variance:** $\bar{v} > 0$. Use softplus: $\bar{v} = \log(1 + e^{h_{\bar{v}}})$.

    3. **Vol-of-vol:** $\xi > 0$. Use softplus: $\xi = \log(1 + e^{h_\xi})$.

    4. **Correlation:** $\rho \in (-1, 1)$. Use tanh activation: $\rho = \tanh(h_\rho)$.

    5. **Feller condition:** $2\kappa\bar{v} > \xi^2$ ensures the variance process does not hit zero. This is a joint constraint that cannot be enforced by individual activations alone. Options include:

        - **Reparameterization:** Instead of outputting $\xi$ directly, output $\alpha \in (0, 1)$ and set $\xi = \alpha \sqrt{2\kappa\bar{v}}$, which guarantees $\xi^2 = \alpha^2 \cdot 2\kappa\bar{v} < 2\kappa\bar{v}$.
        - **Penalty term:** Add $\lambda \cdot \max(0, \xi^2 - 2\kappa\bar{v} + \epsilon)^2$ to the loss, where $\epsilon > 0$ is a safety margin.

    6. **Reasonable parameter ranges:** Even beyond mathematical validity, parameters should lie in economically sensible ranges (e.g., $\kappa \in [0.1, 10]$, $\bar{v} \in [0.01, 1]$). This can be enforced via sigmoid activations scaled to the desired range.

---

**Exercise 4.** Compare three approaches to modeling option prices: (a) pure Black-Scholes with constant implied volatility, (b) a pure neural network $V_\theta(S, K, T, r)$, and (c) a hybrid model $V_\theta = V_{\text{BS}}(\sigma_{\text{NN}}(K,T))$ where the neural network learns an implied volatility function fed into the Black-Scholes formula. Discuss each approach's strengths in terms of no-arbitrage guarantees, data efficiency, and flexibility. Why does approach (c) automatically satisfy put-call parity?

??? success "Solution to Exercise 4"
    **(a) Pure Black-Scholes with constant implied volatility.**

    $$
    V = V_{\text{BS}}(S, K, T, r, \sigma_{\text{const}})
    $$

    - *No-arbitrage:* Fully satisfied by construction---Black-Scholes prices are derived from a no-arbitrage framework and automatically satisfy monotonicity, convexity, put-call parity, and boundary conditions.
    - *Data efficiency:* Extremely high---only one parameter ($\sigma_{\text{const}}$) to calibrate.
    - *Flexibility:* Very low---cannot capture the implied volatility smile or term structure. Systematic mispricing for OTM and ITM options.

    **(b) Pure neural network $V_\theta(S, K, T, r)$.**

    - *No-arbitrage:* None guaranteed. The network may produce negative prices, violate monotonicity, break convexity, or violate put-call parity. All constraints must be imposed externally (penalties, architecture) at additional cost and complexity.
    - *Data efficiency:* Low---the network must learn the entire pricing function from data, including basic relationships (e.g., call price increases with $S$) that are known analytically.
    - *Flexibility:* Very high---can approximate any continuous pricing function, capturing complex smile dynamics and term structure effects.

    **(c) Hybrid model $V_\theta = V_{\text{BS}}(\sigma_{\text{NN}}(K, T))$.**

    The neural network learns an implied volatility surface $\sigma_{\text{NN}}(K, T)$, which is fed into the Black-Scholes formula to produce prices.

    - *No-arbitrage:* Partial guarantees. Since $V_{\text{BS}}$ is used as the pricing engine, certain properties are automatic:
        - **Put-call parity is automatically satisfied** because both the call and put are computed from the same Black-Scholes formula with the same $\sigma_{\text{NN}}(K,T)$, and Black-Scholes satisfies $C - P = S - Ke^{-rT}$ for any $\sigma > 0$.
        - **Positivity** is guaranteed since Black-Scholes prices are always positive for $\sigma > 0$.
        - However, **convexity and calendar arbitrage** constraints are not automatic---they depend on the shape of $\sigma_{\text{NN}}(K,T)$ and must still be enforced.
    - *Data efficiency:* High---the network only learns the implied volatility surface (a lower-dimensional, smoother object than the price surface), and the Black-Scholes formula encodes the known relationship between volatility and price.
    - *Flexibility:* Good---any smile shape can be captured through $\sigma_{\text{NN}}(K,T)$.

    **Why (c) automatically satisfies put-call parity.** The Black-Scholes formula gives:

    $$
    C_{\text{BS}}(S, K, T, r, \sigma) - P_{\text{BS}}(S, K, T, r, \sigma) = S - Ke^{-rT}
    $$

    for any $\sigma > 0$. Since the hybrid model uses the same $\sigma_{\text{NN}}(K,T)$ for both the call and put pricing, the parity relation holds identically regardless of the neural network's output. This is an example of how embedding financial structure into the architecture provides guarantees for free.

---

**Exercise 5.** In a market impact model, the Almgren-Chriss framework provides the base: $\text{Impact} = \eta v + \gamma |v|$ (temporary + permanent), and an ML correction accounts for nonlinear effects. Propose a hybrid architecture and discuss what additional input features (order size, time of day, volatility, spread) the ML component might use. How would you ensure that the hybrid model preserves the sign of impact (buying pushes prices up)?

??? success "Solution to Exercise 5"
    **Hybrid market impact model.**

    The Almgren-Chriss base model provides:

    $$
    \text{Impact}_{\text{base}}(v) = \eta \, v + \gamma \, |v|
    $$

    where $v$ is the trading rate, $\eta$ is the temporary impact coefficient, and $\gamma$ is the permanent impact coefficient. This captures the linear components of market impact.

    **Proposed hybrid architecture:**

    $$
    \text{Impact}(v, z) = \eta \, v + \gamma \, |v| + \mathcal{N}_\theta(v, z)
    $$

    where $z$ is a vector of additional features and $\mathcal{N}_\theta$ is a neural network capturing nonlinear effects.

    **Additional input features for $\mathcal{N}_\theta$:**

    - **Order size** $|v|$: nonlinear impact for large orders (concave square-root law $\sim |v|^{0.5}$)
    - **Time of day**: impact is higher near market open/close due to lower liquidity
    - **Current volatility** $\sigma$: impact increases in high-volatility regimes
    - **Bid-ask spread** $s$: wider spreads indicate lower liquidity and higher impact
    - **Order book depth** $d$: thinner books mean larger price impact per unit traded
    - **Recent volume** $V_{\text{recent}}$: participation rate relative to market volume affects impact
    - **Momentum signal**: trading in the direction of recent price movement may have different impact than contrarian trading

    **Ensuring the sign of impact.**

    The financial constraint is that buying ($v > 0$) should push prices up and selling ($v < 0$) should push prices down. Formally: $\text{sign}(\text{Impact}) = \text{sign}(v)$, or equivalently $v \cdot \text{Impact}(v, z) \ge 0$.

    Approaches to enforce this:

    1. **Factored architecture:** Write $\text{Impact}(v, z) = v \cdot h_\theta(|v|, z)$ where $h_\theta > 0$ is a neural network with softplus output activation. Since $v \cdot h_\theta$ has the same sign as $v$ and $h_\theta > 0$ ensures the impact magnitude is positive, the sign constraint is satisfied by construction.

    2. **Symmetric architecture with sign extraction:** Decompose as $\text{Impact}(v, z) = \text{sign}(v) \cdot g_\theta(|v|, z)$ where $g_\theta \ge 0$. This ensures the correct sign while allowing the magnitude to depend on all features.

    3. **Penalty approach:** Add $\lambda \cdot \sum_i \max(0, -v_i \cdot \text{Impact}(v_i, z_i))^2$ to the loss. This is softer but simpler to implement.

    The factored architecture (approach 1) is recommended because it provides a hard guarantee while remaining differentiable and expressive.

---

**Exercise 6.** Explain why hybrid models are particularly well-suited for regulated environments. A regulator requires that a pricing model be explainable and consistent with no-arbitrage theory. How does the hybrid structure allow the institution to point to the parametric base model for structural soundness while using the ML component for improved accuracy? What validation procedures would you recommend for the ML correction component?

??? success "Solution to Exercise 6"
    **Why hybrid models suit regulated environments.**

    Financial regulators require that pricing and risk models be:

    1. **Theoretically grounded:** The model should be consistent with established financial theory (no-arbitrage, risk-neutral pricing, etc.).
    2. **Explainable:** Stakeholders must understand the model's logic and be able to challenge its outputs.
    3. **Stable and robust:** The model should behave predictably under stress and not produce pathological outputs.

    A hybrid model satisfies all three requirements through its two-component structure:

    **Structural soundness via the parametric base.** The institution can point to the base model (e.g., Heston, Black-Scholes, Nelson-Siegel) and demonstrate that:

    - The model is derived from first principles (no-arbitrage, diffusion theory, etc.).
    - It satisfies known financial constraints by construction.
    - Its parameters have clear economic interpretation ($\kappa$ = mean reversion, $\rho$ = leverage effect, etc.).
    - It has been widely studied and validated in the academic literature.

    **Improved accuracy via the ML correction.** The neural network component captures residual patterns that the base model misses, improving pricing accuracy without abandoning the theoretical foundation. The institution can characterize the ML component as an "empirical correction" or "model enrichment" rather than a standalone black-box model.

    **Explainability decomposition.** For any output, the hybrid model provides a natural decomposition:

    $$
    \hat{y} = \underbrace{f_{\text{base}}(x)}_{\text{interpretable}} + \underbrace{\mathcal{N}_\theta(x)}_{\text{correction}}
    $$

    The base component is fully transparent, and the correction can be analyzed using standard ML interpretability tools (SHAP, partial dependence, etc.). If the correction is kept small via regularization, the model's behavior is dominated by the interpretable base.

    **Recommended validation procedures for the ML correction:**

    1. **Magnitude monitoring:** Track the ratio $|\mathcal{N}_\theta(x)| / |f_{\text{base}}(x)|$ across the input space. If the correction dominates the base, the hybrid is effectively a black box.
    2. **Stability testing:** Evaluate whether the correction changes significantly when retrained on slightly different data (bootstrap stability).
    3. **Out-of-domain behavior:** Test the hybrid model on inputs outside the training distribution (extreme strikes, long maturities). The correction should shrink toward zero, with the base model providing the fallback.
    4. **Backtesting:** Compare the hybrid model's performance against the base model alone on historical data to quantify the value of the ML correction.
    5. **Constraint verification:** Confirm that the combined model still satisfies no-arbitrage conditions, even after adding the correction.

---

**Exercise 7.** Design a hybrid credit risk model where the base model is a logistic regression $PD = \sigma(\beta^\top x)$ and the ML component is a gradient-boosted tree that captures nonlinear interactions. The final model is $\widehat{PD} = \alpha \cdot PD_{\text{logistic}} + (1-\alpha) \cdot PD_{\text{GBT}}$ with $\alpha \in [0,1]$. Discuss how to choose $\alpha$ (e.g., via cross-validation), the interpretability of the blended model, and how to decompose the model's predictions for regulatory reporting (e.g., adverse action reasons in consumer lending).

??? success "Solution to Exercise 7"
    **Hybrid credit risk model.**

    The blended model is:

    $$
    \widehat{PD} = \alpha \cdot PD_{\text{logistic}} + (1 - \alpha) \cdot PD_{\text{GBT}}
    $$

    where $PD_{\text{logistic}} = \sigma(\beta^\top x) = \frac{1}{1 + e^{-\beta^\top x}}$ and $PD_{\text{GBT}} = \text{GBT}(x)$.

    **Choosing $\alpha$.**

    Use $k$-fold cross-validation (e.g., $k = 5$ or $k = 10$) with time-aware splits (to avoid leakage from future data):

    1. For each fold, train both the logistic regression and GBT on the training set.
    2. For a grid of $\alpha$ values $\{0, 0.05, 0.10, \ldots, 1.0\}$, compute the blended predictions on the validation set.
    3. Evaluate using an appropriate metric: AUC, log-loss, or Brier score.
    4. Select $\alpha^* = \arg\min_\alpha \text{CV-Loss}(\alpha)$.

    Alternatively, $\alpha$ can be learned as a parameter via maximum likelihood. The optimal $\alpha$ reflects the relative strengths of the two models: if the GBT substantially outperforms the logistic regression, $\alpha^*$ will be close to 0; if the data is well-captured by a linear model, $\alpha^*$ will be close to 1.

    **Interpretability of the blended model.**

    The blended model is partially interpretable:

    - The logistic component contributes $\alpha \cdot \sigma(\beta^\top x)$, which is fully transparent: each feature's contribution is proportional to its coefficient $\beta_j$.
    - The GBT component contributes $(1-\alpha) \cdot \text{GBT}(x)$, which is less transparent but can be explained using SHAP values (TreeSHAP is exact for tree ensembles).

    The overall interpretability depends on $\alpha$: larger $\alpha$ means the model is more interpretable. Even for small $\alpha$, the logistic component provides a "baseline explanation" that captures the dominant linear effects.

    **Decomposing predictions for regulatory reporting.**

    For adverse action notices under ECOA, the institution must provide specific reasons for denial. The decomposition proceeds as follows:

    1. **Logistic component attribution.** For the logistic regression, feature $j$'s contribution to the log-odds is $\beta_j x_j$. Convert to contributions to the PD scale using the chain rule:

        $$
        \Delta_j^{\text{logistic}} = \alpha \cdot \sigma(\beta^\top x) \cdot (1 - \sigma(\beta^\top x)) \cdot \beta_j x_j
        $$

        (This is approximate; an exact additive decomposition uses integrated gradients or Shapley values of the logistic model.)

    2. **GBT component attribution.** Apply TreeSHAP to the GBT model to obtain exact SHAP values $\phi_j^{\text{GBT}}$ for each feature.

    3. **Combined attribution.** The blended feature attribution is:

        $$
        \phi_j^{\text{blend}} = \alpha \cdot \phi_j^{\text{logistic}} + (1 - \alpha) \cdot \phi_j^{\text{GBT}}
        $$

        where $\phi_j^{\text{logistic}}$ is the SHAP value from the logistic model and $\phi_j^{\text{GBT}}$ is the SHAP value from the GBT.

    4. **Adverse action reasons.** Rank features by $\phi_j^{\text{blend}}$ (largest positive contributions to PD) and report the top $k$ (typically 4--5) as the reasons for denial.

    This approach ensures that the blended model's predictions can be decomposed into feature-level explanations that satisfy regulatory requirements, while leveraging the accuracy of the GBT component. The logistic regression coefficients provide an additional layer of transparency that can be presented to regulators as evidence of conceptual soundness.
