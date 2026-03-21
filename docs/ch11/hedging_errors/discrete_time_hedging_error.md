# Discrete-Time Hedging Error


Continuous-time delta hedging is an idealization. Discrete rebalancing introduces a random hedging error influenced by gamma.

---

## Setup


Consider hedging an option \(V(t,S)\) by holding \(\Delta(t_k, S_{t_k})\) shares at discrete times \(t_0 < t_1 < \cdots < t_N = T\) with \(\Delta t = t_{k+1} - t_k\).

The hedging portfolio value at \(t_{k+1}\) is:
\[
\Pi_{k+1} = \Pi_k e^{r\Delta t} + \Delta_k (S_{k+1} - S_k e^{r\Delta t})
\]

where \(\Delta_k = \Delta(t_k, S_k)\) is the delta computed at rebalancing time.

---

## Hedging error: rigorous derivation


The hedging error over \([t_k, t_{k+1}]\) is the difference between the option value change and the hedge portfolio change:

\[
\epsilon_k = (V_{k+1} - V_k) - (\Pi_{k+1} - \Pi_k)
\]

Using Taylor expansion of \(V\) and ignoring discounting:

\[
V_{k+1} - V_k \approx \Delta_k(S_{k+1} - S_k) + \Theta_k \Delta t + \frac{1}{2}\Gamma_k(S_{k+1} - S_k)^2
\]

The hedge P&L is \(\Delta_k(S_{k+1} - S_k)\), so:

\[
\boxed{\epsilon_k \approx \Theta_k \Delta t + \frac{1}{2}\Gamma_k(\Delta S_k)^2}
\]

Using the theta-gamma identity:

\[
\epsilon_k \approx \frac{1}{2}\Gamma_k\left[(\Delta S_k)^2 - \sigma^2 S_k^2 \Delta t\right]
\]

---

## Heuristic structure


The hedging error can be related to the replacement of quadratic variation by realized squared increments:

\[
\mathrm{HE} \approx
\frac{1}{2}\sum_k \Gamma(t_k,S_{t_k})(\Delta S_k)^2
-\frac{1}{2}\int_0^T \Gamma(t,S_t)\,\mathrm{d}\langle S\rangle_t
\]

The first term is the realized gamma P&L; the second is the continuous-time limit.

---

## Error variance


Under Black–Scholes dynamics, the hedging error per step has:

**Mean:**
\[
\mathbb{E}[\epsilon_k | \mathcal{F}_{t_k}] \approx 0
\]

**Variance:**
\[
\text{Var}(\epsilon_k | \mathcal{F}_{t_k}) \approx \frac{1}{2}\Gamma_k^2 S_k^4 \sigma^4 (\Delta t)^2
\]

**Cumulative error variance** (summing over \(N = T/\Delta t\) steps):

\[
\boxed{\text{Var}(\mathrm{HE}) \approx \frac{1}{2}\bar{\Gamma}^2 S^4 \sigma^4 T \cdot \Delta t}
\]

where \(\bar{\Gamma}\) is an average gamma. The variance scales linearly with \(\Delta t\).

**Standard deviation of hedging error:**
\[
\text{Std}(\mathrm{HE}) \sim \sqrt{\Delta t}
\]

---

## Central limit theorem for hedging error


For small \(\Delta t\), the cumulative hedging error is approximately Gaussian:

\[
\mathrm{HE} \xrightarrow{d} \mathcal{N}\left(0, \frac{1}{2}\int_0^T \Gamma^2 S^4 \sigma^4 dt \cdot \Delta t\right)
\]

This is the basis for asymptotic hedging error expansions:

\[
\mathrm{HE} = c_1 \sqrt{\Delta t} \cdot Z + \mathcal{O}(\Delta t)
\]

where \(Z \sim \mathcal{N}(0,1)\) and \(c_1 = \sqrt{\frac{1}{2}\int_0^T \Gamma^2 S^4 \sigma^4 dt}\).

---

## Frequency-error tradeoff


| Rebalancing | \(\Delta t\) | Error Std | Transaction Cost |
|:------------|:-------------|:----------|:-----------------|
| Daily | 1/252 yr | \(\mathcal{O}(0.06)\) | Low |
| Hourly | 1/6048 yr | \(\mathcal{O}(0.01)\) | Moderate |
| Continuous | 0 | 0 | Infinite |

More frequent rebalancing reduces hedging error but increases transaction costs.

---

## Numerical example


Consider an ATM call with \(S = K = 100\), \(\sigma = 20\%\), \(\tau = 0.25\) (3 months), \(r = 5\%\):

- \(\Gamma \approx 0.032\)
- \(\Gamma S^2 \sigma^2 = 0.032 \times 10000 \times 0.04 = 12.8\)

**Daily rebalancing** (\(\Delta t = 1/252\)):
\[
\text{Std}(\epsilon_{\text{daily}}) \approx \sqrt{\frac{1}{2}} \times 12.8 \times \frac{1}{252} \approx 0.036
\]

Over 63 trading days:
\[
\text{Std}(\mathrm{HE}) \approx 0.036 \times \sqrt{63} \approx 0.28
\]

**Weekly rebalancing** (\(\Delta t = 1/52\)):
\[
\text{Std}(\mathrm{HE}) \approx 0.28 \times \sqrt{5} \approx 0.63
\]

Weekly hedging has about \(\sqrt{5} \approx 2.2\times\) higher error standard deviation.

---

## Path dependence of hedging error


The hedging error is path-dependent through gamma:

1. **Volatile paths**: Higher \((\Delta S)^2\), larger errors
2. **Paths crossing strike**: Gamma spikes, error amplified
3. **Calm paths**: Lower errors

This path dependence is the source of "gamma risk" in practice.

---

## Model risk in hedging error


The analysis assumes correct model. In practice:

- **Volatility misspecification**: Changes the drift of hedging error (see Section 6.6)
- **Jump risk**: Causes large discrete errors that dominate diffusive terms
- **Correlation breakdown**: Hedging error in multi-asset positions

---

## What to remember


- Discrete hedging creates variance-like error terms
- Error variance scales as \(\Gamma^2 S^4 \sigma^4 T \cdot \Delta t\)
- Standard deviation scales as \(\sqrt{\Delta t}\)
- Near-expiry gamma blow-up magnifies the error
- More frequent rebalancing reduces error but increases costs
- The hedging error is approximately Gaussian for small \(\Delta t\) (CLT)
