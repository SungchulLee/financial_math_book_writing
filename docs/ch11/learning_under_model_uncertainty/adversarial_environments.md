# Adversarial Environments

In **adversarial environments**, data-generating processes may react strategically to the learner’s actions, invalidating classical statistical assumptions.

---

## 1. From stochastic to adversarial settings

Traditional learning assumes:
- i.i.d. or stationary data.

Adversarial learning assumes:
- worst-case or adaptive opponents,
- no probabilistic structure.

This provides strong performance guarantees.

---

## 2. Online adversarial learning

Algorithms are designed to minimize regret:
- Hedge / multiplicative weights,
- online gradient descent,
- mirror descent.

They perform well against any adversarial sequence.

---

## 3. Financial relevance

Markets can behave adversarially:
- crowding effects,
- feedback from strategies,
- strategic counterparties.

Adversarial models capture these phenomena.

---

## 4. Costs and conservatism

Adversarial guarantees are:
- pessimistic,
- often overly conservative,
- data-inefficient in benign environments.

Hybrid stochastic–adversarial models are often preferred.

---

## 5. Key takeaways

- Adversarial models assume worst-case data.
- They provide strong guarantees.
- Conservatism is the price of robustness.

---

## Further reading

- Cesa-Bianchi & Lugosi, adversarial bandits.
- Hazan, online convex optimization.
