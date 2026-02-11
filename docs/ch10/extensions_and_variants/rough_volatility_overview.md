# Rough Volatility (Overview)


Empirical evidence suggests that volatility exhibits **rough behavior**, with paths much less smooth than classical diffusion models predict. **Rough volatility models** address this by incorporating fractional dynamics.

---

## Empirical motivation


High-frequency data show that:
- volatility has very low Hölder regularity,
- volatility increments are highly persistent,
- classical diffusions are too smooth.

This motivates models driven by fractional Brownian motion.

---

## Basic rough volatility idea


A prototypical rough volatility model takes the form

\[
\sigma_t = \sigma_0 + \int_0^t K(t-s)\,dW_s,
\]


where the kernel \(K\) behaves like

\[
K(t) \sim t^{H-\frac12}, \quad H \in (0,\tfrac12).
\]



Small Hurst parameter \(H\) implies rough paths.

---

## Consequences for option pricing


Rough volatility models naturally explain:
- steep short-maturity smiles,
- fast decay of ATM skew,
- empirical scaling laws.

These features are difficult to reproduce with classical stochastic volatility.

---

## Practical challenges


- non-Markovian dynamics,
- higher computational cost,
- calibration complexity,
- limited closed-form pricing results.

As a result, rough volatility is often used in simplified or approximated form.

---

## Key takeaways


- Volatility is empirically rough.
- Rough models improve short-maturity behavior.
- Practical use requires approximation or dimension reduction.

---

## Further reading


- Gatheral, Jaisson & Rosenbaum, *Volatility is Rough*.
- Bayer, Friz & Gatheral, rough volatility surveys.
