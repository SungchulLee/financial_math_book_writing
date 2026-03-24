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

---

**Exercise 2.** A learned implied volatility surface must satisfy the no-calendar-arbitrage condition: total implied variance $w(K,T) = \sigma_{\text{imp}}^2(K,T) \cdot T$ must be non-decreasing in $T$ for fixed $K$. Design a neural network architecture that enforces $\partial w/\partial T \ge 0$ by construction. (Hint: Use a cumulative sum or integral of a positive function.) Compare this hard enforcement to a soft penalty $\lambda \sum_{j} \max(0, w(K,T_j) - w(K,T_{j+1}))^2$.

---

**Exercise 3.** Explain why unconstrained neural networks can produce negative option prices for deep out-of-the-money options. Describe three approaches to prevent this: (a) clipping the output with $\max(0, \cdot)$, (b) using softplus activation in the output layer, (c) adding a penalty for negative prices. Discuss the advantages and disadvantages of each approach in terms of gradient flow during training.

---

**Exercise 4.** A monotone network enforces that the call price is non-increasing in strike $K$ by constraining all weights in the $K$-path to be non-positive. Describe how this architectural constraint works mathematically. What is the tradeoff in terms of network expressiveness? Show that for a European call with $S = 100$, monotonicity in $K$ is equivalent to $-1 \le \partial C/\partial K \le 0$ (assuming discounted prices).

---

**Exercise 5.** Put-call parity states $C - P = S - Ke^{-rT}$. A learning model produces call and put prices independently. Propose a method to enforce put-call parity: (a) learn only the call price and derive the put, (b) add a parity penalty to the loss, or (c) parameterize the model to produce the call-put difference directly. Discuss which approach is most robust and why.

---

**Exercise 6.** In a constrained optimization framework, the learning problem is $\min_\theta \mathcal{L}_{\text{data}}(\theta)$ subject to no-arbitrage constraints $g_i(\theta) \le 0$. Describe how the augmented Lagrangian method converts this to an unconstrained problem with penalty: $\min_\theta \mathcal{L}_{\text{data}}(\theta) + \sum_i \mu_i g_i(\theta) + \frac{\rho}{2}\sum_i \max(0, g_i(\theta))^2$. What role do the multipliers $\mu_i$ play, and how are they updated during training?

---

**Exercise 7.** Discuss the regularization effect of no-arbitrage constraints. A neural network trained without constraints has test error of 2.5%, while the constrained version has test error of 2.2% despite higher training error. Explain this phenomenon using the bias-variance tradeoff: the constraints reduce the hypothesis space (adding bias) but significantly reduce variance. Under what market conditions (e.g., illiquid markets with noisy data) would constraints be most beneficial?
