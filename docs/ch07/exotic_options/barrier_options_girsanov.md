# Barrier Option Pricing via Girsanov and Reflection Principle

## Payoff Structure

An **up-and-out barrier call option** knocks out (expires worthless) if the underlying asset price hits or exceeds a barrier level $H > S_0$ at any time before maturity:

$$
\text{Payoff} = (S_T - K)^+ \cdot \mathbf{1}_{\left\{\sup_{0 \le t \le T} S_t < H\right\}}
$$

This is a **path-dependent** payoff: the option value depends not only on the terminal price $S_T$, but on the entire path trajectory.

---

## Log-Price Representation under Q

Recall (see [Risk-Neutral Pricing](../../ch04/risk_neutral/risk_neutral_valuation_principle.md) and [Itô's Lemma](../../ch03/ito_lemma/taylor_expansion_linear.md)): under $\mathbb{Q}$, $dS_t = r S_t\,dt + \sigma S_t\,d\tilde{W}_t$ and $X_t := \log S_t = x + \mu t + \sigma \tilde{W}_t$ with $\mu := r - \tfrac{1}{2}\sigma^2$ and $x := \log S_0$.

Define the key quantities:

$$
b := \log H, \quad k := \log K
$$

The pricing problem becomes:

$$
C_{\text{UO}} = \mathbb{E}^{\mathbb{Q}}\left[e^{-rT}(e^{X_T} - K)^+ \cdot \mathbf{1}_{\left\{\sup_{t \le T} X_t < b\right\}}\right]
$$

---

## The Reflection Principle

Recall (see [Reflection Principle](../../ch02/brownian_motion/reflection_principle.md)): for drifted log-price $X_t = x + \mu t + \sigma \tilde{W}_t$, a Girsanov-type measure change yields

$$
\mathbb{Q}\left(\sup_{t \le T} X_t \ge b, \; X_T \in dy\right) = e^{2\mu(b-x)/\sigma^2} \cdot \mathbb{Q}_{2b-x}(X_T \in dy),
$$

i.e. each barrier-crossing path is associated with an "image" path starting from $2b - x$.

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

- $C_{\text{BS}}(S, K, T) = S\,\mathcal{N}(d_1) - Ke^{-rT}\,\mathcal{N}(d_2)$ is the standard Black–Scholes call price
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

Recall (see [§ In–Out Parity](barrier_options.md#inout-parity)): $V_{\text{knock-in}} + V_{\text{knock-out}} = V_{\text{vanilla}}$. Therefore:

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

Recall (see [§ Discrete vs. Continuous Monitoring](barrier_options.md#discrete-vs-continuous-monitoring)): under discrete monitoring at $m$ equally-spaced times, the Broadie–Glasserman–Kou correction $H_{\text{eff}} = H \cdot e^{\pm \beta \sigma \sqrt{T/m}}$ with $\beta \approx 0.5826$ shifts the barrier outward to match the continuous-monitoring price.

### Near-Barrier Behavior

As $S_t$ approaches the barrier $H$, the option's delta and gamma exhibit extreme behavior, making hedging challenging near the knockout level.

---

## Exercises

**Exercise 1.** Starting from the risk-neutral dynamics $dS_t = rS_t\,dt + \sigma S_t\,d\tilde{W}_t$, derive the log-price process $X_t = \log S_t$ using Ito's lemma. Verify that $X_t = x + \mu t + \sigma \tilde{W}_t$ where $\mu = r - \frac{1}{2}\sigma^2$ and $x = \log S_0$.

??? success "Solution to Exercise 1"
    Apply Ito's lemma to $f(S_t) = \log S_t$ with $dS_t = rS_t\,dt + \sigma S_t\,d\tilde{W}_t$.

    We have $f'(S) = 1/S$ and $f''(S) = -1/S^2$. By Ito's lemma:

    $$
    d(\log S_t) = f'(S_t)\,dS_t + \frac{1}{2}f''(S_t)\,(dS_t)^2
    $$

    Computing each term: $f'(S_t)\,dS_t = \frac{1}{S_t}(rS_t\,dt + \sigma S_t\,d\tilde{W}_t) = r\,dt + \sigma\,d\tilde{W}_t$ and $(dS_t)^2 = \sigma^2 S_t^2\,dt$ (keeping only the $dt$ order term), so $\frac{1}{2}f''(S_t)(dS_t)^2 = \frac{1}{2}\left(-\frac{1}{S_t^2}\right)\sigma^2 S_t^2\,dt = -\frac{1}{2}\sigma^2\,dt$.

    Combining:

    $$
    d(\log S_t) = \left(r - \tfrac{1}{2}\sigma^2\right)dt + \sigma\,d\tilde{W}_t
    $$

    Integrating from $0$ to $t$:

    $$
    \log S_t - \log S_0 = \left(r - \tfrac{1}{2}\sigma^2\right)t + \sigma \tilde{W}_t
    $$

    Setting $X_t = \log S_t$, $x = \log S_0$, and $\mu = r - \frac{1}{2}\sigma^2$:

    $$
    X_t = x + \mu t + \sigma \tilde{W}_t
    $$

    This confirms the log-price process as stated.

---


**Exercise 2.** The up-and-out call formula is $C_{\text{UO}} = C_{\text{BS}}(S_0, K, T) - (S_0/H)^{2\lambda - 2} C_{\text{BS}}(H^2/S_0, K, T)$ with $\lambda = r/\sigma^2 + 1/2$. Verify the two limiting cases: (a) Show that as $H \to \infty$, $C_{\text{UO}} \to C_{\text{BS}}(S_0, K, T)$. (b) Show that as $H \to S_0^+$, $C_{\text{UO}} \to 0$. For part (b), you may assume $C_{\text{BS}}$ is continuous in its first argument.

??? success "Solution to Exercise 2"
    **(a) As $H \to \infty$:** We have $(S_0/H)^{2\lambda - 2} \to 0$ since $S_0/H \to 0$ and $2\lambda - 2 = 2r/\sigma^2 > 0$ (assuming $r > 0$). Also, $H^2/S_0 \to \infty$, so $C_{\text{BS}}(H^2/S_0, K, T)$ remains bounded (it grows at most linearly). Therefore the correction term vanishes:

    $$
    \left(\frac{S_0}{H}\right)^{2\lambda - 2} C_{\text{BS}}\left(\frac{H^2}{S_0}, K, T\right) \to 0
    $$

    and $C_{\text{UO}} \to C_{\text{BS}}(S_0, K, T)$.

    **(b) As $H \to S_0^+$:** We have $S_0/H \to 1$, so $(S_0/H)^{2\lambda - 2} \to 1$. Also, $H^2/S_0 \to S_0^2/S_0 = S_0$. By continuity of $C_{\text{BS}}$ in its first argument:

    $$
    C_{\text{UO}} \to C_{\text{BS}}(S_0, K, T) - 1 \cdot C_{\text{BS}}(S_0, K, T) = 0
    $$

    This makes sense: when the barrier equals the current price, the option is immediately knocked out (since any upward movement triggers the barrier), so it is worthless.

---


**Exercise 3.** Explain why the reflection principle cannot be applied directly to drifted Brownian motion $X_t = x + \mu t + \sigma W_t$ when $\mu \neq 0$. Describe the Girsanov-type measure change that removes the drift, and show that the Radon–Nikodym derivative produces the factor $(S_0/H)^{2\lambda - 2}$ in the pricing formula.

??? success "Solution to Exercise 3"
    The reflection principle for **driftless** Brownian motion $B_t$ states that for a barrier at level $b$:

    $$
    \mathbb{P}\left(\sup_{t \leq T} B_t \geq b,\, B_T \leq y\right) = \mathbb{P}(B_T \geq 2b - y)
    $$

    This works because reflecting the portion of a path after it first hits $b$ produces a bijection between paths that cross $b$ and end at $y < b$ and paths that end at $2b - y > b$.

    For drifted Brownian motion $X_t = x + \mu t + \sigma W_t$ with $\mu \neq 0$, this bijection fails because reflecting a path changes the drift: the reflected segment has drift $-\mu$ instead of $+\mu$. The reflected paths are no longer equally likely under the original measure.

    To fix this, we define a new measure $\hat{\mathbb{Q}}$ under which $X_t$ has no drift. By Girsanov's theorem, the Radon–Nikodym derivative is:

    $$
    \frac{d\hat{\mathbb{Q}}}{d\mathbb{Q}} = \exp\left(-\frac{\mu}{\sigma}W_T - \frac{\mu^2}{2\sigma^2}T\right)
    $$

    Under $\hat{\mathbb{Q}}$, we apply the reflection principle. When transforming back to $\mathbb{Q}$, the reflected path starting at $2b - x$ acquires the factor:

    $$
    \exp\left(\frac{2\mu(b - x)}{\sigma^2}\right) = \exp\left(\frac{2\mu}{\sigma^2}\log\frac{H}{S_0}\right) = \left(\frac{H}{S_0}\right)^{2\mu/\sigma^2}
    $$

    Since $\mu = r - \frac{1}{2}\sigma^2$, we get $2\mu/\sigma^2 = 2r/\sigma^2 - 1 = 2\lambda - 2$. Therefore the correction factor is:

    $$
    \left(\frac{S_0}{H}\right)^{2\lambda - 2}
    $$

    which is exactly the factor appearing in the pricing formula.

---


**Exercise 4.** The "reflected spot price" $H^2/S_0$ appears as the first argument of $C_{\text{BS}}$ in the barrier correction term. (a) Show that $\log(H^2/S_0) = 2b - x$ where $b = \log H$ and $x = \log S_0$, confirming this is the image point of $x$ reflected about $b$. (b) For $S_0 = 100$ and $H = 120$, compute $H^2/S_0$ and interpret it geometrically in log-price space.

??? success "Solution to Exercise 4"
    **(a)** Direct computation:

    $$
    \log\left(\frac{H^2}{S_0}\right) = \log H^2 - \log S_0 = 2\log H - \log S_0 = 2b - x
    $$

    where $b = \log H$ and $x = \log S_0$. This confirms that $H^2/S_0$ is the exponential of the image point.

    **(b)** For $S_0 = 100$ and $H = 120$:

    $$
    \frac{H^2}{S_0} = \frac{120^2}{100} = \frac{14400}{100} = 144
    $$

    In log-price space: $x = \log 100 \approx 4.605$, $b = \log 120 \approx 4.787$, and $2b - x = 2(4.787) - 4.605 = 4.969 = \log 144$.

    Geometrically, in log-price space, the point $x = \log 100$ is reflected about the barrier $b = \log 120$. The distance from $x$ to $b$ is $b - x = 0.182$, and the image point is the same distance on the other side: $b + (b - x) = 4.969$. Converting back to price space: $e^{4.969} = 144$. The reflected spot price is "as far above the barrier as the actual price is below it" in the logarithmic metric.

---


**Exercise 5.** Using in-out parity, derive the up-and-in call formula $C_{\text{UI}} = (S_0/H)^{2\lambda - 2} C_{\text{BS}}(H^2/S_0, K, T)$. For $S_0 = 100$, $K = 100$, $H = 130$, $T = 1$, $r = 0.05$, $\sigma = 0.25$, compute $\lambda$ and the reflected spot price $H^2/S_0$, then explain qualitatively whether $C_{\text{UI}}$ is large or small relative to $C_{\text{BS}}$.

??? success "Solution to Exercise 5"
    By in-out parity: $C_{\text{UI}} + C_{\text{UO}} = C_{\text{BS}}$. Substituting the formula $C_{\text{UO}} = C_{\text{BS}}(S_0, K, T) - (S_0/H)^{2\lambda-2}C_{\text{BS}}(H^2/S_0, K, T)$:

    $$
    C_{\text{UI}} = C_{\text{BS}} - C_{\text{UO}} = \left(\frac{S_0}{H}\right)^{2\lambda - 2} C_{\text{BS}}\left(\frac{H^2}{S_0}, K, T\right)
    $$

    For $S_0 = 100$, $K = 100$, $H = 130$, $T = 1$, $r = 0.05$, $\sigma = 0.25$:

    $$
    \lambda = \frac{r}{\sigma^2} + \frac{1}{2} = \frac{0.05}{0.0625} + 0.5 = 0.8 + 0.5 = 1.3
    $$

    The reflected spot price:

    $$
    \frac{H^2}{S_0} = \frac{130^2}{100} = 169
    $$

    The power factor: $2\lambda - 2 = 2(1.3) - 2 = 0.6$, and $(S_0/H)^{0.6} = (100/130)^{0.6} = (0.7692)^{0.6} \approx 0.855$.

    Since $C_{\text{BS}}(169, 100, 1)$ is the price of a deep in-the-money call (spot 169, strike 100), it is approximately $169 - 100 e^{-0.05} \approx 169 - 95.12 \approx 73.88$.

    Thus $C_{\text{UI}} \approx 0.855 \times 73.88 \approx 63.2$. However, $C_{\text{BS}}(100, 100, 1) \approx 12.34$ (with $\sigma = 0.25$). Since in-out parity requires $C_{\text{UI}} \leq C_{\text{BS}}$, and the barrier at 130 is not too far above the current price, $C_{\text{UI}}$ is a moderate fraction of $C_{\text{BS}}$. Qualitatively, $C_{\text{UI}}$ is relatively large compared to $C_{\text{BS}}$ because the barrier at 130 is not extremely far from $S_0 = 100$, so there is a reasonable probability the stock reaches 130 during the year.

---


**Exercise 6.** The Broadie-Glasserman correction for discrete monitoring adjusts the barrier as $H_{\text{adjusted}} = H \cdot e^{\pm \beta \sigma \sqrt{\Delta t}}$. Explain the sign convention: when should the $+$ sign be used versus the $-$ sign? Relate this to whether discrete monitoring makes a knock-out option more or less valuable compared to continuous monitoring.

??? success "Solution to Exercise 6"
    **Sign convention:**

    - Use the **$+$ sign** for an **up barrier** (barrier above the current price): $H_{\text{adjusted}} = H \cdot e^{+\beta\sigma\sqrt{\Delta t}}$. The barrier is shifted **upward**.
    - Use the **$-$ sign** for a **down barrier** (barrier below the current price): $H_{\text{adjusted}} = H \cdot e^{-\beta\sigma\sqrt{\Delta t}}$. The barrier is shifted **downward**.

    In both cases, the correction shifts the barrier **outward** (away from the current price).

    **Relation to discrete vs. continuous monitoring value:**

    Discrete monitoring makes a **knock-out option more valuable** than continuous monitoring. This is because with discrete monitoring, the stock price might cross the barrier between observation times and return without being detected, so the option survives situations where continuous monitoring would have triggered a knockout. Since fewer paths are knocked out, the knock-out price is higher.

    Conversely, discrete monitoring makes a **knock-in option less valuable** because fewer paths are detected as crossing the barrier.

    The correction compensates for this by shifting the barrier outward to an effective level that makes the continuous-barrier formula match the discrete-barrier price. For a down-and-out call, lowering the barrier from $H$ to $H_{\text{adjusted}} < H$ makes the continuous formula produce a higher price (fewer knockouts), matching the discrete-monitoring behavior. For an up-and-out call, raising the barrier from $H$ to $H_{\text{adjusted}} > H$ similarly produces a higher price.
