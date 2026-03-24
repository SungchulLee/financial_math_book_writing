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

---

## Exercises

**Exercise 1.** The fractional kernel $K(t) = t^{H-1/2}$ with $H = 0.1$ controls the roughness of the volatility process. Compute $K(t)$ at $t = 0.01, 0.1, 1.0, 10.0$ and compare with the exponential kernel $K_{\text{exp}}(t) = e^{-\kappa t}$ with $\kappa = 2$. Which kernel decays faster at short time scales? At long time scales? How does this difference affect the autocorrelation structure of volatility increments?

---

**Exercise 2.** In the rough Bergomi model, the log-variance is given by

$$
\log V_t = \log V_0 + \eta\int_0^t (t-s)^{H-1/2}\,dW_s - \frac{\eta^2}{2}t^{2H}
$$

For $H = 0.1$, compute the variance of $\log V_t$ at $t = 1/252$ (one day), $t = 1/12$ (one month), and $t = 1$ (one year). How does the scaling $\text{Var}[\log V_t] = \eta^2 t^{2H}/(2H)$ differ from the classical diffusion scaling $\text{Var} \propto t$?

---

**Exercise 3.** The ATM implied volatility skew in rough volatility models scales as $T^{H-1/2}$ for short maturities, versus $T^{-1/2}$ in classical models. For $H = 0.1$, compute the ratio of 1-week to 1-year skew under both scaling laws. Which model produces steeper short-maturity skews? This is one of the key empirical signatures of rough volatility.

---

**Exercise 4.** Rough volatility models are non-Markovian because $V_t$ depends on the entire past of the driving Brownian motion. Explain why this makes Monte Carlo simulation more expensive than for Markovian models like Heston. Specifically, if a Heston simulation with $n$ time steps costs $O(n)$, what is the cost of a naive rough volatility simulation, and why?

---

**Exercise 5.** Empirical evidence suggests that the Hurst parameter for equity index volatility is approximately $H \approx 0.1$, far below the Markovian value $H = 0.5$. Explain what $H < 0.5$ means in terms of path regularity: are paths smoother or rougher than Brownian motion? What empirical test would you use to estimate $H$ from a time series of realized volatility?

---

**Exercise 6.** A practitioner considers using a rough volatility model for pricing 1-week options and a Heston model for 1-year options. Discuss whether this "hybrid" approach is internally consistent. What problems might arise at intermediate maturities? Would a multi-factor model with fast and slow components be a better compromise?
