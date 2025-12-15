# Regret Bounds

**Regret** measures the performance loss of a learning algorithm relative to the best fixed strategy in hindsight.

---

## 1. Definition of regret

For a sequence of losses \(\ell_t\),
\[
\text{Regret}_T
= \sum_{t=1}^T \ell_t(a_t)
- \min_{a} \sum_{t=1}^T \ell_t(a).
\]

Low regret means the algorithm learns effectively.

---

## 2. Types of regret

Common notions include:
- static regret (vs best fixed action),
- dynamic regret (vs time-varying benchmark),
- policy regret (in control settings).

Each reflects different learning goals.

---

## 3. Regret bounds

Typical guarantees are:
- \(O(\sqrt{T})\) regret for convex losses,
- logarithmic regret for strongly convex problems.

Bounds are often worst-case.

---

## 4. Financial interpretation

In finance:
- regret corresponds to opportunity cost,
- low regret ensures competitive long-run performance,
- regret bounds provide model-free guarantees.

---

## 5. Key takeaways

- Regret quantifies learning performance.
- Sublinear regret implies convergence.
- Guarantees are conservative but robust.

---

## Further reading

- Shalev-Shwartz, online learning.
- Bubeck & Cesa-Bianchi, regret analysis.
