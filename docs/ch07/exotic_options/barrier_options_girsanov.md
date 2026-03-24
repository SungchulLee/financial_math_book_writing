# Barrier Option Pricing via Girsanov and Reflection Principle

## Payoff Structure

An **up-and-out barrier call option** knocks out (expires worthless) if the underlying asset price hits or exceeds a barrier level $H > S_0$ at any time before maturity:

$$
\text{Payoff} = (S_T - K)^+ \cdot \mathbf{1}_{\left\{\sup_{0 \le t \le T} S_t < H\right\}}
$$

This is a **path-dependent** payoff: the option value depends not only on the terminal price $S_T$, but on the entire path trajectory.

---

## Log-Price Representation under Q

Under the risk-neutral measure $\mathbb{Q}$ (obtained via Girsanov's theorem), the stock price satisfies:

$$
dS_t = r S_t \, dt + \sigma S_t \, d\tilde{W}_t
$$

Taking $X_t := \log S_t$:

$$
X_t = x + \left(r - \tfrac{1}{2}\sigma^2\right)t + \sigma \tilde{W}_t
$$

where $x := \log S_0$. Define the key quantities:

$$
b := \log H, \quad k := \log K, \quad \mu := r - \tfrac{1}{2}\sigma^2
$$

The pricing problem becomes:

$$
C_{\text{UO}} = \mathbb{E}^{\mathbb{Q}}\left[e^{-rT}(e^{X_T} - K)^+ \cdot \mathbf{1}_{\left\{\sup_{t \le T} X_t < b\right\}}\right]
$$

---

## The Reflection Principle

The key tool for evaluating the barrier condition is the **reflection principle** for Brownian motion with drift.

### Joint Distribution of Maximum and Terminal Value

For a drifted Brownian motion $X_t = x + \mu t + \sigma \tilde{W}_t$, the joint density of the maximum $M_T := \sup_{0 \le t \le T} X_t$ and terminal value $X_T$ involves reflecting paths that cross the barrier.

The reflection principle states that the probability of a Brownian path reaching level $b$ and ending at $y < b$ can be related to paths starting from the **reflected point** $2b - x$:

$$
\mathbb{Q}\left(\sup_{t \le T} X_t \ge b, \; X_T \in dy\right) = e^{2\mu(b-x)/\sigma^2} \cdot \mathbb{Q}_{2b-x}(X_T \in dy)
$$

This is the **image method**: for each path that crosses the barrier and ends at $y$, there exists a corresponding "image" path starting from $2b - x$.

---

## Derivation of the Pricing Formula

### Step 1: Decomposition

The up-and-out call price can be decomposed as:

$$
C_{\text{UO}} = C_{\text{BS}}(S_0, K, T) - C_{\text{cross}}
$$

where $C_{\text{BS}}$ is the standard Black–Scholes call price and $C_{\text{cross}}$ accounts for paths that cross the barrier.

### Step 2: Image Pricing

Using the reflection principle, the contribution from barrier-crossing paths is:

$$
C_{\text{cross}} = \left(\frac{S_0}{H}\right)^{2\lambda - 2} C_{\text{BS}}\left(\frac{H^2}{S_0}, K, T\right)
$$

where:

$$
\lambda = \frac{r}{\sigma^2} + \frac{1}{2}
$$

The factor $\left(\frac{S_0}{H}\right)^{2\lambda - 2}$ arises from the Girsanov-type change of measure needed to account for the drift when applying the reflection principle to drifted Brownian motion.

### Step 3: The Reflected Spot Price

The argument $H^2 / S_0$ in the second Black–Scholes term is the **reflected spot price**. Under the log transformation:

$$
\log\left(\frac{H^2}{S_0}\right) = 2\log H - \log S_0 = 2b - x
$$

This is precisely the image point of $x = \log S_0$ reflected about the barrier $b = \log H$.

---

## Final Result

$$
\boxed{C_{\text{UO}} = C_{\text{BS}}(S_0, K, T) - \left(\frac{S_0}{H}\right)^{2\lambda - 2} C_{\text{BS}}\left(\frac{H^2}{S_0}, K, T\right)}
$$

where:

- $C_{\text{BS}}(S, K, T) = S\,\Phi(d_1) - Ke^{-rT}\,\Phi(d_2)$ is the standard Black–Scholes call price
- $\lambda = \dfrac{r}{\sigma^2} + \dfrac{1}{2}$
- $H$ is the barrier level with $H > S_0$ and $H > K$

---

## Properties and Limiting Cases

### As H → ∞

$$
C_{\text{UO}} \to C_{\text{BS}}(S_0, K, T)
$$

The barrier becomes unreachable and the option reduces to a standard European call.

### As H → S_0^+

$$
C_{\text{UO}} \to 0
$$

The barrier is immediately hit, so the option is worth nothing.

### In-Out Parity

For barrier options with the same strike and barrier:

$$
C_{\text{up-and-in}} + C_{\text{up-and-out}} = C_{\text{BS}}
$$

Therefore:

$$
C_{\text{UI}} = \left(\frac{S_0}{H}\right)^{2\lambda - 2} C_{\text{BS}}\left(\frac{H^2}{S_0}, K, T\right)
$$

---

## Down-and-Out Call Option

For a **down-and-out call** with barrier $H < S_0$ (and $H < K$):

$$
C_{\text{DO}} = C_{\text{BS}}(S_0, K, T) - \left(\frac{S_0}{H}\right)^{2\lambda - 2} C_{\text{BS}}\left(\frac{H^2}{S_0}, K, T\right)
$$

The formula has the same structure, but the reflection is about a lower barrier.

---

## The Role of Girsanov's Theorem

The reflection principle applies directly only to **driftless** Brownian motion. Under $\mathbb{Q}$, the log-price has drift $\mu = r - \frac{1}{2}\sigma^2 \neq 0$, so a pure reflection argument does not work.

The resolution involves a **Girsanov-type measure change** that removes the drift:

1. Define a new measure $\hat{\mathbb{Q}}$ under which $X_t$ is a driftless Brownian motion
2. Apply the reflection principle under $\hat{\mathbb{Q}}$
3. Transform back to $\mathbb{Q}$, picking up the Radon–Nikodým factor

The exponent $2\lambda - 2$ in the pricing formula encodes exactly this measure change. The factor:

$$
\left(\frac{S_0}{H}\right)^{2\lambda - 2} = \exp\left[(2\lambda - 2)(\log S_0 - \log H)\right]
$$

is the Radon–Nikodým derivative evaluated at the reflected starting point.

---

## Practical Considerations

### Continuous vs. Discrete Monitoring

The formula above assumes **continuous barrier monitoring**. In practice, barriers are often checked at discrete intervals (daily close), which makes the option more valuable since the asset can briefly cross the barrier undetected.

**Broadie–Glasserman correction** adjusts for discrete monitoring:

$$
H_{\text{adjusted}} = H \cdot e^{\pm \beta \sigma \sqrt{\Delta t}}
$$

where $\beta \approx 0.5826$ and $\Delta t$ is the monitoring interval.

### Near-Barrier Behavior

As $S_t$ approaches the barrier $H$, the option's delta and gamma exhibit extreme behavior, making hedging challenging near the knockout level.

---

## Exercises

**Exercise 1.** Starting from the risk-neutral dynamics $dS_t = rS_t\,dt + \sigma S_t\,d\tilde{W}_t$, derive the log-price process $X_t = \log S_t$ using Ito's lemma. Verify that $X_t = x + \mu t + \sigma \tilde{W}_t$ where $\mu = r - \frac{1}{2}\sigma^2$ and $x = \log S_0$.

---

**Exercise 2.** The up-and-out call formula is $C_{\text{UO}} = C_{\text{BS}}(S_0, K, T) - (S_0/H)^{2\lambda - 2} C_{\text{BS}}(H^2/S_0, K, T)$ with $\lambda = r/\sigma^2 + 1/2$. Verify the two limiting cases: (a) Show that as $H \to \infty$, $C_{\text{UO}} \to C_{\text{BS}}(S_0, K, T)$. (b) Show that as $H \to S_0^+$, $C_{\text{UO}} \to 0$. For part (b), you may assume $C_{\text{BS}}$ is continuous in its first argument.

---

**Exercise 3.** Explain why the reflection principle cannot be applied directly to drifted Brownian motion $X_t = x + \mu t + \sigma W_t$ when $\mu \neq 0$. Describe the Girsanov-type measure change that removes the drift, and show that the Radon-Nikodym derivative produces the factor $(S_0/H)^{2\lambda - 2}$ in the pricing formula.

---

**Exercise 4.** The "reflected spot price" $H^2/S_0$ appears as the first argument of $C_{\text{BS}}$ in the barrier correction term. (a) Show that $\log(H^2/S_0) = 2b - x$ where $b = \log H$ and $x = \log S_0$, confirming this is the image point of $x$ reflected about $b$. (b) For $S_0 = 100$ and $H = 120$, compute $H^2/S_0$ and interpret it geometrically in log-price space.

---

**Exercise 5.** Using in-out parity, derive the up-and-in call formula $C_{\text{UI}} = (S_0/H)^{2\lambda - 2} C_{\text{BS}}(H^2/S_0, K, T)$. For $S_0 = 100$, $K = 100$, $H = 130$, $T = 1$, $r = 0.05$, $\sigma = 0.25$, compute $\lambda$ and the reflected spot price $H^2/S_0$, then explain qualitatively whether $C_{\text{UI}}$ is large or small relative to $C_{\text{BS}}$.

---

**Exercise 6.** The Broadie-Glasserman correction for discrete monitoring adjusts the barrier as $H_{\text{adjusted}} = H \cdot e^{\pm \beta \sigma \sqrt{\Delta t}}$. Explain the sign convention: when should the $+$ sign be used versus the $-$ sign? Relate this to whether discrete monitoring makes a knock-out option more or less valuable compared to continuous monitoring.
