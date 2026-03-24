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

---

**Exercise 2.** Consider a yield curve model where the Nelson-Siegel parametric form provides the base curve and a neural network corrects for mispricing. Write the hybrid model as $y(\tau) = y_{\text{NS}}(\tau; \beta_0, \beta_1, \beta_2, \lambda) + \mathcal{N}_\theta(\tau)$. Discuss how this preserves the interpretability of the Nelson-Siegel factors (level, slope, curvature) while allowing the neural network to capture anomalies. What regularization on $\mathcal{N}_\theta$ would you apply to keep corrections small?

---

**Exercise 3.** A bank uses an ML model to dynamically calibrate the parameters of a Heston stochastic volatility model: $(\kappa, \bar{v}, \xi, \rho) = g_\theta(\text{market features})$, where $g_\theta$ is a neural network mapping observable market data to Heston parameters. Explain how this is a hybrid approach. What constraints should be placed on the output of $g_\theta$ to ensure the Heston model remains well-defined (e.g., Feller condition $2\kappa\bar{v} > \xi^2$)?

---

**Exercise 4.** Compare three approaches to modeling option prices: (a) pure Black-Scholes with constant implied volatility, (b) a pure neural network $V_\theta(S, K, T, r)$, and (c) a hybrid model $V_\theta = V_{\text{BS}}(\sigma_{\text{NN}}(K,T))$ where the neural network learns an implied volatility function fed into the Black-Scholes formula. Discuss each approach's strengths in terms of no-arbitrage guarantees, data efficiency, and flexibility. Why does approach (c) automatically satisfy put-call parity?

---

**Exercise 5.** In a market impact model, the Almgren-Chriss framework provides the base: $\text{Impact} = \eta v + \gamma |v|$ (temporary + permanent), and an ML correction accounts for nonlinear effects. Propose a hybrid architecture and discuss what additional input features (order size, time of day, volatility, spread) the ML component might use. How would you ensure that the hybrid model preserves the sign of impact (buying pushes prices up)?

---

**Exercise 6.** Explain why hybrid models are particularly well-suited for regulated environments. A regulator requires that a pricing model be explainable and consistent with no-arbitrage theory. How does the hybrid structure allow the institution to point to the parametric base model for structural soundness while using the ML component for improved accuracy? What validation procedures would you recommend for the ML correction component?

---

**Exercise 7.** Design a hybrid credit risk model where the base model is a logistic regression $PD = \sigma(\beta^\top x)$ and the ML component is a gradient-boosted tree that captures nonlinear interactions. The final model is $\widehat{PD} = \alpha \cdot PD_{\text{logistic}} + (1-\alpha) \cdot PD_{\text{GBT}}$ with $\alpha \in [0,1]$. Discuss how to choose $\alpha$ (e.g., via cross-validation), the interpretability of the blended model, and how to decompose the model's predictions for regulatory reporting (e.g., adverse action reasons in consumer lending).
