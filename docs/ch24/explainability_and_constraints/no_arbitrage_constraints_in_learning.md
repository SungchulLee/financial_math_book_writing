# No-Arbitrage Constraints in Learning


Learning-based financial models must respect **no-arbitrage constraints** to ensure economic consistency and prevent pathological behavior.

---

## Why constraints matter


Unconstrained learning may produce:

- negative option prices,
- arbitrage opportunities,
- violations of monotonicity or convexity.

Such outputs are unacceptable in pricing applications.

---

## Types of no-arbitrage constraints


Common constraints include:

- monotonicity in strike and maturity,
- convexity of option prices,
- absence of calendar and butterfly arbitrage.

These constraints encode fundamental financial laws.

---

## Enforcing constraints in learning


Approaches include:

- constrained optimization,
- penalty and regularization terms,
- architecture design (e.g., monotone networks).

Constraints improve robustness and generalization.

---

## Trade-offs


Imposing constraints:

- reduces hypothesis space,
- may slightly reduce in-sample fit,
- greatly improves out-of-sample stability.

This mirrors regularization effects.

---

## Key takeaways


- No-arbitrage constraints are essential.
- Learning must respect financial structure.
- Constraints improve robustness and trust.

---

## Further reading


- Ackerer et al., arbitrage-free learning.
- Buehler et al., deep hedging constraints.

---

## Exercises

**Exercise 1.** A neural network trained on European call option prices produces the following outputs for $T = 1$, $r = 0$: $C(K=90) = 12.5$, $C(K=100) = 8.0$, $C(K=110) = 5.5$. Check whether the convexity condition $C(K-\Delta K) - 2C(K) + C(K+\Delta K) \ge 0$ is satisfied (butterfly spread condition with $\Delta K = 10$). If not, explain what arbitrage opportunity this creates and how a convexity penalty in the loss function would prevent it.

??? success "Solution to Exercise 1"
    **Checking the butterfly spread (convexity) condition.**

    The butterfly spread condition for equally spaced strikes with spacing $\Delta K = 10$ centered at $K = 100$ is:

    $$
    C(K - \Delta K) - 2C(K) + C(K + \Delta K) \ge 0
    $$

    Substituting the given prices:

    $$
    C(90) - 2C(100) + C(110) = 12.5 - 2(8.0) + 5.5 = 12.5 - 16.0 + 5.5 = 2.0
    $$

    Since $2.0 > 0$, the convexity condition **is satisfied** for this set of prices. No butterfly arbitrage exists.

    **General discussion.** If the condition were violated (i.e., the result were negative), say $C(90) = 12.5$, $C(100) = 10.0$, $C(110) = 5.5$, giving $12.5 - 20.0 + 5.5 = -2.0 < 0$, then an arbitrageur could:

    - Buy 1 call at $K = 90$ (pay 12.5)
    - Sell 2 calls at $K = 100$ (receive 20.0)
    - Buy 1 call at $K = 110$ (pay 5.5)

    Net premium received: $20.0 - 12.5 - 5.5 = 2.0 > 0$. The payoff at expiry of this butterfly spread is non-negative for all $S_T$, so this constitutes a riskless profit---a clear arbitrage.

    **Convexity penalty.** To prevent such violations during training, one adds a penalty term to the loss function:

    $$
    \mathcal{L}_{\text{total}} = \mathcal{L}_{\text{data}} + \lambda \sum_{j} \max\!\Big(0,\; -\big[C(K_{j-1}) - 2C(K_j) + C(K_{j+1})\big]\Big)^2
    $$

    This penalizes any violation of convexity quadratically, pushing the network toward arbitrage-free outputs while maintaining differentiability for gradient-based optimization.

---

**Exercise 2.** A learned implied volatility surface must satisfy the no-calendar-arbitrage condition: total implied variance $w(K,T) = \sigma_{\text{imp}}^2(K,T) \cdot T$ must be non-decreasing in $T$ for fixed $K$. Design a neural network architecture that enforces $\partial w/\partial T \ge 0$ by construction. (Hint: Use a cumulative sum or integral of a positive function.) Compare this hard enforcement to a soft penalty $\lambda \sum_{j} \max(0, w(K,T_j) - w(K,T_{j+1}))^2$.

??? success "Solution to Exercise 2"
    **Hard enforcement via architectural design.**

    The no-calendar-arbitrage condition requires that total implied variance $w(K, T) = \sigma_{\text{imp}}^2(K, T) \cdot T$ is non-decreasing in $T$ for each fixed $K$.

    **Architecture:** Define a neural network that outputs an **increment function** $\delta_\theta(K, T) \ge 0$ for all inputs, and construct the total variance as a cumulative integral:

    $$
    w(K, T) = w_0(K) + \int_0^T \delta_\theta(K, s)\, ds
    $$

    where $w_0(K) \ge 0$ is a base term and $\delta_\theta(K, s)$ is parameterized to be non-negative by construction---for example, using a softplus output activation:

    $$
    \delta_\theta(K, s) = \log(1 + e^{h_\theta(K, s)})
    $$

    where $h_\theta$ is an unconstrained neural network. Since $\delta_\theta \ge 0$, the integral is non-decreasing in $T$, guaranteeing $\partial w / \partial T \ge 0$ by construction.

    In practice, the integral is approximated by a discrete cumulative sum over a maturity grid $T_1 < T_2 < \cdots < T_m$:

    $$
    w(K, T_j) = w_0(K) + \sum_{k=1}^{j} \delta_\theta(K, T_k) \cdot (T_k - T_{k-1})
    $$

    **Comparison with soft penalty.**

    The soft penalty approach adds:

    $$
    \mathcal{L}_{\text{penalty}} = \lambda \sum_{j} \max\!\big(0,\; w(K, T_j) - w(K, T_{j+1})\big)^2
    $$

    Advantages of hard enforcement:

    - **Guaranteed satisfaction:** The constraint holds exactly for all inputs, not just at training points.
    - **No tuning of $\lambda$:** The penalty approach requires careful selection of the regularization strength; too small and violations persist, too large and the model underfits the data.

    Advantages of soft penalty:

    - **Simpler architecture:** No need to restructure the network; any standard architecture can be used.
    - **Greater flexibility:** The unconstrained network can explore a larger hypothesis space and may achieve better data fit.
    - **Easier implementation:** Standard loss functions and optimizers apply directly.

    The hard enforcement is preferred when constraint satisfaction is critical (e.g., in production pricing systems), while the soft penalty may suffice for exploratory or research applications.

---

**Exercise 3.** Explain why unconstrained neural networks can produce negative option prices for deep out-of-the-money options. Describe three approaches to prevent this: (a) clipping the output with $\max(0, \cdot)$, (b) using softplus activation in the output layer, (c) adding a penalty for negative prices. Discuss the advantages and disadvantages of each approach in terms of gradient flow during training.

??? success "Solution to Exercise 3"
    **Why unconstrained networks produce negative prices.**

    Deep out-of-the-money (OTM) options have prices very close to zero. A neural network trained on data spanning a wide range of moneyness may produce slightly negative outputs for extreme OTM options because:

    - The training data in this region is sparse (few observations of deep OTM prices).
    - The network's output is a continuous function that can pass through zero without constraint.
    - Regression losses like MSE treat errors symmetrically---a prediction of $-0.01$ is penalized equally to $+0.01$---so the network has no incentive to stay non-negative.

    **Three approaches to prevent negative prices:**

    **(a) Output clipping: $\hat{C} = \max(0, f_\theta(\cdot))$.**

    - *Advantages:* Simple to implement; guarantees non-negative output.
    - *Disadvantages:* The gradient of $\max(0, \cdot)$ is zero when $f_\theta < 0$, creating a "dead zone" where the network receives no gradient signal for negative outputs. This can slow training and create flat regions in the loss landscape. The network may learn to produce moderately negative values that get clipped, without being pushed toward the correct small positive values.

    **(b) Softplus output activation: $\hat{C} = \frac{1}{\beta}\log(1 + e^{\beta \cdot f_\theta(\cdot)})$.**

    - *Advantages:* Smooth and differentiable everywhere, so gradients flow even for near-zero prices. For large $\beta$, it closely approximates $\max(0, \cdot)$ but without the zero-gradient problem. Output is strictly positive.
    - *Disadvantages:* For small prices, the softplus introduces a positive bias: $\text{softplus}(x) > 0$ for all $x$, so the model cannot produce exact zeros. The parameter $\beta$ must be tuned---too small and the approximation to $\max(0, \cdot)$ is poor; too large and numerical issues arise.

    **(c) Penalty for negative prices: $\mathcal{L} = \mathcal{L}_{\text{data}} + \lambda \sum_i \max(0, -f_\theta(x_i))^2$.**

    - *Advantages:* Does not modify the network architecture, so it is compatible with any model. Gradients are well-defined and push the network away from negative outputs.
    - *Disadvantages:* The penalty is enforced only at training points, not globally---the network may produce negative prices at unseen inputs. The strength $\lambda$ must be tuned: too small and violations persist, too large and the model prioritizes non-negativity over data fit. This is a soft constraint, not a hard guarantee.

    **Recommendation:** For production systems, softplus activation (b) provides the best balance: guaranteed positivity with smooth gradients. For research or when architectural changes are undesirable, the penalty approach (c) is a practical alternative with appropriate $\lambda$ tuning.

---

**Exercise 4.** A monotone network enforces that the call price is non-increasing in strike $K$ by constraining all weights in the $K$-path to be non-positive. Describe how this architectural constraint works mathematically. What is the tradeoff in terms of network expressiveness? Show that for a European call with $S = 100$, monotonicity in $K$ is equivalent to $-1 \le \partial C/\partial K \le 0$ (assuming discounted prices).

??? success "Solution to Exercise 4"
    **Monotone network architecture.**

    A feedforward network computes $f(x) = W_L \sigma(\cdots \sigma(W_1 x + b_1) \cdots) + b_L$ where $\sigma$ is the activation function. The output is monotonically non-increasing in input $x_j$ if every path from $x_j$ to the output transmits a non-positive signal.

    For the call price as a function of strike $K$, this is achieved by:

    1. Constraining all weights connecting $K$ through the network to be **non-positive** (i.e., $W^{(l)}_{K\text{-path}} \le 0$ at each layer).
    2. Using a monotone non-decreasing activation function $\sigma$ (e.g., ReLU, sigmoid, softplus).

    **Mathematical justification.** If $\sigma$ is non-decreasing and all weights in the $K$-path are non-positive, then by the chain rule:

    $$
    \frac{\partial f}{\partial K} = \prod_{\text{layers}} W^{(l)}_{K\text{-path}} \cdot \sigma'(\cdot) \le 0
    $$

    Each $\sigma'(\cdot) \ge 0$ (non-decreasing activation) and each $W^{(l)}_{K\text{-path}} \le 0$, so the product of an odd number of non-positive terms with non-negative terms yields a non-positive derivative. More carefully, in a multilayer network the derivative involves sums of such products, and constraining all weights to be non-positive in the relevant paths ensures the overall derivative is non-positive.

    **Tradeoff in expressiveness.** The non-positive weight constraint restricts the set of functions the network can represent. It cannot learn non-monotone relationships between $K$ and $C$---which is correct from a financial standpoint, since call prices must be non-increasing in strike. However, the constraint also limits flexibility in how the network combines $K$ with other features, potentially reducing the network's ability to capture complex cross-feature interactions.

    **Proving $-1 \le \partial C / \partial K \le 0$ for European calls.**

    For a European call with $S = 100$, $r = 0$ (for simplicity), and payoff $(S_T - K)^+$:

    $$
    C(K) = \mathbb{E}[(S_T - K)^+] = \int_K^\infty (s - K) f_{S_T}(s)\, ds
    $$

    Differentiating under the integral:

    $$
    \frac{\partial C}{\partial K} = -\int_K^\infty f_{S_T}(s)\, ds = -\mathbb{P}(S_T > K)
    $$

    Since $0 \le \mathbb{P}(S_T > K) \le 1$, we have:

    $$
    -1 \le \frac{\partial C}{\partial K} \le 0
    $$

    This confirms that call prices are non-increasing in strike, and the rate of decrease is bounded by the probability of finishing in the money. For discounted prices with $r \neq 0$, the result becomes $-e^{-rT} \le \partial C / \partial K \le 0$.

---

**Exercise 5.** Put-call parity states $C - P = S - Ke^{-rT}$. A learning model produces call and put prices independently. Propose a method to enforce put-call parity: (a) learn only the call price and derive the put, (b) add a parity penalty to the loss, or (c) parameterize the model to produce the call-put difference directly. Discuss which approach is most robust and why.

??? success "Solution to Exercise 5"
    **Put-call parity:** $C(K,T) - P(K,T) = S - Ke^{-rT}$.

    **Approach (a): Learn only the call and derive the put.**

    Train a neural network $C_\theta(S, K, T, r)$ to learn call prices. Then compute puts as:

    $$
    P_\theta(S, K, T, r) = C_\theta(S, K, T, r) - S + Ke^{-rT}
    $$

    - *Advantages:* Put-call parity is satisfied **exactly** by construction, with zero residual error. Only one model needs to be trained and maintained. The approach is simple and robust.
    - *Disadvantages:* Errors in the call model propagate directly to the put model. If the call model is poorly calibrated in certain regions, the derived put prices inherit those errors.

    **Approach (b): Add a parity penalty to the loss.**

    Train two separate models $C_\theta$ and $P_\theta$ with an augmented loss:

    $$
    \mathcal{L} = \mathcal{L}_{\text{call}} + \mathcal{L}_{\text{put}} + \lambda \sum_i \big[C_\theta(x_i) - P_\theta(x_i) - S_i + K_i e^{-r_i T_i}\big]^2
    $$

    - *Advantages:* Both models are trained on their respective data, potentially capturing nuances specific to calls and puts.
    - *Disadvantages:* Parity is only approximately satisfied, controlled by $\lambda$. Requires tuning $\lambda$, and residual violations may persist, especially at points not in the training set. Two models must be maintained.

    **Approach (c): Parameterize the call-put difference directly.**

    Define $D_\theta(S, K, T, r) = C_\theta - P_\theta$ and learn $D_\theta$ along with one of $C_\theta$ or $P_\theta$, enforcing $D_\theta = S - Ke^{-rT}$ analytically.

    - *Advantages:* The spread is exact by construction.
    - *Disadvantages:* Essentially equivalent to approach (a) but with a more complex parameterization that adds no benefit.

    **Recommendation:** Approach (a) is the most robust. It enforces parity exactly with no tuning parameters, reduces the number of models to maintain, and is the simplest to implement. This is a general principle in constrained learning: when a constraint can be enforced by **construction** (hard constraint), it is always preferable to enforcement by **penalty** (soft constraint), because the hard constraint holds everywhere---not just at training points---and requires no hyperparameter tuning.

---

**Exercise 6.** In a constrained optimization framework, the learning problem is $\min_\theta \mathcal{L}_{\text{data}}(\theta)$ subject to no-arbitrage constraints $g_i(\theta) \le 0$. Describe how the augmented Lagrangian method converts this to an unconstrained problem with penalty: $\min_\theta \mathcal{L}_{\text{data}}(\theta) + \sum_i \mu_i g_i(\theta) + \frac{\rho}{2}\sum_i \max(0, g_i(\theta))^2$. What role do the multipliers $\mu_i$ play, and how are they updated during training?

??? success "Solution to Exercise 6"
    **Augmented Lagrangian method.**

    The constrained optimization problem is:

    $$
    \min_\theta \mathcal{L}_{\text{data}}(\theta) \quad \text{subject to} \quad g_i(\theta) \le 0, \quad i = 1, \ldots, m
    $$

    The augmented Lagrangian converts this to a sequence of unconstrained problems:

    $$
    \min_\theta \; \mathcal{L}_{\text{AL}}(\theta, \mu, \rho) = \mathcal{L}_{\text{data}}(\theta) + \sum_{i=1}^m \mu_i g_i(\theta) + \frac{\rho}{2} \sum_{i=1}^m \max(0, g_i(\theta))^2
    $$

    **Components:**

    1. $\mathcal{L}_{\text{data}}(\theta)$: The standard data-fitting loss (e.g., MSE between model and market prices).

    2. $\sum_i \mu_i g_i(\theta)$: The **Lagrangian term**. The multipliers $\mu_i \ge 0$ represent the "price" of violating constraint $i$. A large $\mu_i$ means constraint $i$ is active and expensive to violate.

    3. $\frac{\rho}{2} \sum_i \max(0, g_i(\theta))^2$: The **quadratic penalty** term. It adds a direct cost proportional to the squared constraint violation. The parameter $\rho > 0$ controls the penalty strength.

    **Role of the multipliers $\mu_i$:**

    The multipliers serve as adaptive penalty weights that target specific constraints. Unlike a pure penalty method (which requires $\rho \to \infty$ to enforce constraints exactly, causing ill-conditioning), the augmented Lagrangian updates $\mu_i$ to absorb the constraint enforcement:

    **Update rule (after each optimization epoch or outer iteration):**

    $$
    \mu_i^{(k+1)} = \max\!\big(0,\; \mu_i^{(k)} + \rho \, g_i(\theta^{(k)})\big)
    $$

    If constraint $i$ is violated ($g_i > 0$), $\mu_i$ increases, making future violations more costly. If the constraint is satisfied ($g_i \le 0$), $\mu_i$ decreases (but remains non-negative). Over iterations, the multipliers converge to the optimal dual variables of the constrained problem, and $\rho$ can remain finite while constraints are satisfied exactly.

    **Advantages over pure penalty:**

    - Does not require $\rho \to \infty$, avoiding ill-conditioning.
    - The multipliers provide a principled, adaptive weighting of constraints.
    - Convergence is faster and more stable in practice.

    **In the no-arbitrage context:** Each $g_i(\theta) \le 0$ encodes a specific no-arbitrage condition (e.g., $g_i = -[C(K_{j-1}) - 2C(K_j) + C(K_{j+1})]$ for butterfly convexity). The multipliers $\mu_i$ automatically increase for constraints that are persistently violated, focusing the optimization on the most problematic regions of the surface.

---

**Exercise 7.** Discuss the regularization effect of no-arbitrage constraints. A neural network trained without constraints has test error of 2.5%, while the constrained version has test error of 2.2% despite higher training error. Explain this phenomenon using the bias-variance tradeoff: the constraints reduce the hypothesis space (adding bias) but significantly reduce variance. Under what market conditions (e.g., illiquid markets with noisy data) would constraints be most beneficial?

??? success "Solution to Exercise 7"
    **Bias-variance analysis of no-arbitrage constraints.**

    The expected test error decomposes as:

    $$
    \text{Test Error} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Noise}
    $$

    **Unconstrained network:** The unconstrained model has a large hypothesis space $\mathcal{H}$, so it can approximate the true pricing function closely (low bias). However, it also has high capacity to fit noise in the training data (high variance). Training error: low. Test error: 2.5%.

    **Constrained network:** No-arbitrage constraints restrict the hypothesis space to $\mathcal{H}_c \subset \mathcal{H}$, where $\mathcal{H}_c$ contains only functions satisfying monotonicity, convexity, and other financial constraints. This introduces bias if the true function lies outside $\mathcal{H}_c$---but since option prices genuinely satisfy these constraints, the bias introduced is zero or negligible. Meanwhile, the reduction in hypothesis space significantly reduces variance: the model cannot fit noise patterns that violate arbitrage conditions. Training error: higher (the model cannot fit noisy data as closely). Test error: 2.2% (lower because variance reduction exceeds any bias increase).

    Numerically:

    | | Unconstrained | Constrained |
    |---|---|---|
    | Training error | 1.8% | 2.0% |
    | Test error | 2.5% | 2.2% |
    | Generalization gap | 0.7% | 0.2% |

    The constrained model's smaller generalization gap confirms that variance has been reduced.

    **Market conditions where constraints are most beneficial:**

    1. **Illiquid markets with sparse data:** When option quotes are available only at a few strikes and maturities, the network must interpolate and extrapolate extensively. Without constraints, the model may produce wildly incorrect prices in data-sparse regions (e.g., negative prices for deep OTM options, non-convex surfaces). Constraints anchor the model to financially sensible behavior even where data is absent.

    2. **Noisy data environments:** In markets with wide bid-ask spreads (e.g., single-stock options, emerging market FX options), observed prices contain substantial noise. An unconstrained model fits this noise, producing arbitrage-violating surfaces. Constraints act as a filter, smoothing out noise while preserving structure.

    3. **Stressed markets:** During volatility spikes or liquidity crises, market data may be stale, inconsistent, or reflect temporary dislocations. Constraints ensure that the model's output remains economically coherent even when inputs are unreliable.

    4. **High-dimensional models:** When the input space is large (many strikes, maturities, underlyings), the curse of dimensionality makes overfitting more severe. Constraints reduce the effective dimensionality of the problem by eliminating large regions of the function space.

    **Conclusion:** No-arbitrage constraints function as domain-informed regularization. Unlike generic regularizers (L1, L2, dropout), they encode *correct prior knowledge* about the problem structure, making them highly effective at reducing variance without introducing meaningful bias. This is why constrained models often outperform unconstrained ones on test data in financial applications.
