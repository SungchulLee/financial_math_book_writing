## Why So Many Derivations?

At first glance, deriving the same Black–Scholes PDE in five different ways may seem redundant. If every approach leads to the same equation, why not present just one?

Each derivation isolates a **different structural aspect of pricing theory** under the same set of model assumptions. The Black–Scholes PDE emerges as the unique pricing equation compatible with no-arbitrage and completeness under the diffusion assumptions of the model; each derivation is a different coordinate system on the same object.

---

### Mechanism: All Five Perspectives in One Binomial Step

Each viewpoint collapses to a one-line statement in a single binomial step where the stock today is $S_0$ and tomorrow is $S_0 u$ or $S_0 d$ with $d < 1+r < u$:

- **Delta hedging:** choose $\Delta = (V_u - V_d)/(S_0 u - S_0 d)$; the hedged portfolio is risk-free, hence earns $r$.
- **Self-financing replication:** the same $(\alpha, \beta) = (\Delta, V - \Delta S_0)/B$ replicates $V$ with no external cash flow.
- **Risk-neutral pricing:** reweight by $q = (1+r-d)/(u-d)$; then $V_0 = \mathbb{E}^{\mathbb{Q}}[V_1]/(1+r)$.
- **Change of numéraire:** measure $V/S$ instead of $V/B$; the up-weighted measure $\mathbb{Q}^S(\text{up}) = qu/(1+r)$ produces the same $V_0$.
- **Equilibrium / SDF:** state prices $\pi_u, \pi_d$ with $\pi_u + \pi_d = 1/(1+r)$ give $V_0 = \pi_u V_u + \pi_d V_d$; matching $\mathbb{Q}$ identifies $\pi_u/\pi_d = q/(1-q)$.

All five give the same $V_0$. The continuous theory is the differential analog: difference quotients become Itô derivatives, sums over states become integrals, and the same equivalence persists — but now expressed as the Black–Scholes PDE.

---

### Five Perspectives on the Same Object

Each derivation removes the dependence on the physical drift $\mu$, but does so through a fundamentally different mechanism:

| Approach                      | Core Idea                                              | How $\mu$ Disappears                              | What It Teaches                          |
| ----------------------------- | ------------------------------------------------------ | --------------------------------------------------- | ---------------------------------------- |
| **Delta Hedging (heuristic)** | Construct a locally riskless portfolio                 | Choose $\Delta = V_S$ to eliminate randomness     | Pricing via replication and no-arbitrage |
| **Delta Hedging (rigorous)**  | Self-financing replication                             | Martingale representation enforces $\alpha = V_S$ | Mathematical foundation of replication   |
| **Risk-Neutral Pricing**      | Discounted prices are martingales under $\mathbb{Q}$ | Girsanov removes drift $\mu \to r$                | Probability measure transformation       |
| **Change of Numéraire**       | Normalize prices by a traded asset                     | Drift shifts under new measure, cancels via Itô     | Pricing invariance across units          |
| **Equilibrium (SDF)**         | Prices reflect marginal utility                        | $\mu - \gamma\sigma^2 = r$ from preferences       | Economic origin of risk premia           |

---

### One Equation, Multiple Mechanisms

All five routes lead to the same PDE:

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0
$$

But the *reason* this equation holds is different in each case:

* In **hedging**, it is enforced by replication.
* In **risk-neutral pricing**, it is enforced by a martingale property.
* In **change of numéraire**, it is enforced by invariance under units.
* In **equilibrium**, it is enforced by preferences and market clearing.

---

### The Deeper Unification

``` mermaid
graph TD
    A["No-Arbitrage + Completeness"] --> B["Unique Pricing Rule"]
    B --> C["Hedging<br/>(trading)"]
    B --> D["Martingale Measure<br/>(probability)"]
    B --> E["Change of Numéraire<br/>(geometry)"]
    B --> F["Equilibrium / SDF<br/>(economics)"]
    C --> G["Black–Scholes PDE"]
    D --> G
    E --> G
    F --> G
```

These are not competing explanations—they are **different representations of the same underlying structure**:

> **No-arbitrage + completeness ⇔ existence of a unique pricing rule**

This rule can be expressed as:

* a **replicating strategy**,
* a **martingale measure**,
* a **change of numéraire**,
* or a **stochastic discount factor**.

Each framework encodes the same pricing logic in a different language:

* **Trading** (hedging),
* **Probability** (risk-neutral measure),
* **Geometry** (numéraire),
* **Economics** (equilibrium).

---

### How to Read These Derivations

* If you want **intuition about trading**, focus on delta hedging.
* If you want **computational tools**, focus on risk-neutral pricing.
* If you want **structural invariance**, focus on change of numéraire.
* If you want **economic meaning**, focus on equilibrium.
* If you want **mathematical foundations**, focus on the rigorous replication argument.

---

### Final Insight

The Black–Scholes PDE is the **unique equation consistent with all five perspectives simultaneously** under the diffusion assumptions of the model.

All five derivations agree because they are different expressions of the same underlying principle: **no-arbitrage in a complete market**. Each method strips away a different layer, until only that pricing rule remains.

!!! note "Equivalence depends on completeness"
    The agreement across the five perspectives is not automatic — it depends on **market completeness**. In incomplete markets, these perspectives no longer necessarily coincide: replication may fail, equivalent martingale measures may not be unique, and equilibrium considerations may influence pricing. Black–Scholes is the textbook case in which completeness holds (one Brownian motion, one risky asset), so the five frameworks collapse to a single pricing rule.

## Exercises

**Exercise 1.** Name the five perspectives on the Black-Scholes equation discussed in this section. For each perspective, write one sentence explaining its key insight.

??? success "Solution to Exercise 1"
    The five perspectives are: (1) the hedging/replication argument, which shows the option price satisfies a PDE because a self-financing portfolio can replicate the payoff; (2) the risk-neutral pricing formula, which expresses the price as a discounted expected payoff under the risk-neutral measure; (3) the Feynman-Kac connection, which links the PDE solution to a conditional expectation; (4) the martingale approach, which identifies the discounted option price as a martingale; and (5) the change-of-numeraire technique, which simplifies the pricing formula by choosing a convenient numeraire.

---

**Exercise 2.** Explain in your own words why these five perspectives, despite their different starting points, all lead to the same pricing formula.

??? success "Solution to Exercise 2"
    All five perspectives are mathematically equivalent characterizations of the same no-arbitrage condition. The hedging argument constructs the replicating portfolio directly; risk-neutral pricing reformulates the same condition using measure theory; Feynman-Kac provides the analytical bridge between PDEs and expectations; the martingale approach captures the no-arbitrage condition in its most abstract form; and the change of numeraire is a computational simplification that preserves the underlying equivalence. Each perspective emphasizes a different mathematical tool but encodes the same economic content: the absence of arbitrage uniquely determines the option price.

---

**Exercise 3.** For each row of the table, state the single mathematical fact that makes $\mu$ drop out (e.g. choosing $\Delta = V_S$, Girsanov's theorem, the equilibrium relation $\mu - \gamma\sigma^2 = r$). Then identify which of these facts depend on market completeness.

??? success "Solution to Exercise 3"
    The drift-removal mechanisms are: (1) **delta hedging** — choosing $\Delta = V_S$ cancels the diffusion term, hence the $\mu$-dependent drift; (2) **self-financing replication** — the martingale representation theorem forces $\alpha_t = V_S$, achieving the same cancellation rigorously; (3) **risk-neutral pricing** — Girsanov's theorem shifts $\mu \to r$ via the market price of risk $\theta = (\mu - r)/\sigma$; (4) **change of numéraire** — Girsanov from $\mathbb{Q}$ to $\mathbb{Q}^S$, then the $\sigma^2$ terms cancel on transforming back; (5) **equilibrium** — market clearing yields $\mu - \gamma\sigma^2 = r$, so the SDF absorbs the risk premium. All five depend on **completeness**: hedging requires the replicating strategy to exist (MRT), Girsanov's theorem produces a *unique* equivalent martingale measure only when one Brownian motion is matched by one risky asset, and the equilibrium identification of $r$ with the SDF drift relies on the same dimensional matching.

---

**Exercise 4.** Construct a simple incomplete-market example (e.g. two independent Brownian motions, one risky asset) and explain how each of the five perspectives breaks down or becomes ambiguous.

??? success "Solution to Exercise 4"
    Consider $dS_t = \mu S_t\,dt + \sigma_1 S_t\,dW_t^{(1)} + \sigma_2 S_t\,dW_t^{(2)}$ with two independent Brownian motions but a single tradable stock. Then: (1)/(2) **hedging / replication** fail — a single stock cannot eliminate two independent risks, so $\alpha_t = V_S$ leaves residual $dW^{(2)}$ exposure and no self-financing replicating strategy exists for a general payoff; (3) **risk-neutral pricing** — Girsanov requires two drift parameters $(\theta_1, \theta_2)$ satisfying one linear constraint, so there is a one-parameter family of equivalent martingale measures (no unique price); (4) **change of numéraire** — still produces a valid measure, but it merely selects one element of this family; (5) **equilibrium** — pricing now depends explicitly on preferences and market clearing, since arbitrage alone does not fix the price. The five perspectives no longer coincide because completeness fails.

---

**Exercise 5.** Why does *one* derivation suffice mathematically but multiple derivations are valuable pedagogically? Give one specific scenario where each of the five perspectives is the most useful starting point.

??? success "Solution to Exercise 5"
    Mathematically the five derivations produce the same PDE, so one suffices. Pedagogically they isolate distinct tools and intuitions: (1) **delta hedging** is most useful for explaining a trading desk's daily P&L attribution (gamma, vega); (2) **self-financing replication** is most useful for a rigorous treatment of admissibility, MRT, and uniqueness; (3) **risk-neutral pricing** is most useful for Monte Carlo simulation and Feynman–Kac numerics; (4) **change of numéraire** is most useful for FX, quanto, and LIBOR-market-model calculations where a non-cash numéraire simplifies the formula; (5) **equilibrium** is most useful for analyzing the equity premium puzzle, term structure of interest rates, and macro-finance questions where preferences matter.

---

**Exercise 6.** List the invariant object in each framework (e.g. replicating strategy, martingale, relative price, pricing kernel). Argue that these are all manifestations of the same no-arbitrage pricing rule.

??? success "Solution to Exercise 6"
    The invariants are:

    | Framework | invariant object |
    | --- | --- |
    | Hedging / replication | self-financing strategy $(\alpha_t, \beta_t)$ |
    | Risk-neutral measure | $\mathbb{Q}$-martingale $e^{-rt}V_t$ |
    | Change of numéraire | $\mathbb{Q}^S$-martingale $V_t/S_t$ |
    | Equilibrium / SDF | $\mathbb{P}$-martingale $M_t V_t$ |

    Under no-arbitrage and completeness these are isomorphic: the strategy $(\alpha_t, \beta_t)$ encodes the same information as the discounted-price martingale, which is the Bayes-rule image of the $V/S$ martingale, which equals the SDF-weighted price via $M_t = (d\mathbb{Q}/d\mathbb{P})e^{-rt}$. They are four representations of the unique pricing rule pinned down by no-arbitrage in a complete market.

