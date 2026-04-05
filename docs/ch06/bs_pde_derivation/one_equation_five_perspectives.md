## Why So Many Derivations?

At first glance, deriving the same Black–Scholes PDE in five different ways may seem redundant. If every approach leads to the same equation, why not present just one?

The answer is that each derivation reveals a **different structural aspect of pricing theory**. The Black–Scholes equation is not tied to a single argument—it is a point where multiple deep principles converge. Each derivation is therefore not an alternative—but a different coordinate system on the same object.

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

The Black–Scholes PDE is not a model-specific accident. It is the **unique equation consistent with all of these perspectives simultaneously**.

Understanding each derivation is not repetition—it is seeing the same object from different angles, until its structure becomes unavoidable.

All five derivations are equivalent not because they resemble each other, but because they are different expressions of the same underlying principle: **no-arbitrage in a complete market**. The Black–Scholes equation is not derived—it is *revealed* as the unique pricing rule consistent with no-arbitrage in a complete market. Each method strips away a different layer, until only that rule remains.
