# Probabilistic Interpretation of the Black-Scholes Formula


The Black-Scholes formula is not merely a mathematical expression—it has deep **probabilistic meaning**. The terms $\mathcal{N}(d_1)$ and $\mathcal{N}(d_2)$ represent probabilities under different measures, and the formula can be understood as a weighted average of terminal payoffs.

This section reveals the probabilistic structure underlying the option pricing formula.

---

## Risk-Neutral Expectation


### 1. **Fundamental Pricing Formula**


Under the risk-neutral measure $\mathbb{Q}$, the option price is:

$$
V_0 = e^{-rT}\mathbb{E}^{\mathbb{Q}}[\text{Payoff at } T]
$$

For a European call:

$$
C_0 = e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+]
$$

### 2. **Terminal Stock Price Distribution**


Under $\mathbb{Q}$, the terminal stock price is:

$$
S_T = S_0 e^{(r - \frac{1}{2}\sigma^2)T + \sigma W_T}
$$

where $W_T \sim \mathcal{N}(0, T)$ under $\mathbb{Q}$.

**Log-normal distribution**:

$$
\log S_T \sim \mathcal{N}\left(\log S_0 + \left(r - \frac{1}{2}\sigma^2\right)T, \sigma^2 T\right)
$$

### 3. **Decomposition of Call Expectation**


$$
\begin{aligned}
\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+] &= \mathbb{E}^{\mathbb{Q}}[S_T \cdot \mathbf{1}_{\{S_T > K\}}] - K\mathbb{E}^{\mathbb{Q}}[\mathbf{1}_{\{S_T > K\}}] \\
&= \mathbb{E}^{\mathbb{Q}}[S_T | S_T > K] \cdot \mathbb{Q}(S_T > K) - K \cdot \mathbb{Q}(S_T > K)
\end{aligned}
$$

This reveals two key probabilities we need to evaluate.

---

## The Meaning of $\mathcal{N}(d_2)$


### 1. **Exercise Probability Under $\mathbb{Q}$**


$$
\boxed{\mathcal{N}(d_2) = \mathbb{Q}(S_T > K)}
$$

**Interpretation**: $\mathcal{N}(d_2)$ is the **risk-neutral probability** that the option expires in-the-money.

### 2. **Derivation**


Under $\mathbb{Q}$:

$$\begin{array}{lll}
S_T > K 
&\iff&\displaystyle \log S_T > \log K\\
&\iff&\displaystyle  S_0 e^{(r - \frac{1}{2}\sigma^2)T + \sigma W_T} > K\\
&\iff&\displaystyle  \sigma W_T > \log(K/S_0) - \left(r - \frac{1}{2}\sigma^2\right)T\\
&\iff&\displaystyle  \frac{W_T}{\sqrt{T}} > \frac{\log(K/S_0) - (r - \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}
\end{array}$$

Since $\frac{W_T}{\sqrt{T}} \sim \mathcal{N}(0,1)$ under $\mathbb{Q}$:

$$
\mathbb{Q}(S_T > K) = \mathbb{Q}\left(Z > \frac{\log(K/S_0) - (r - \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}\right) = \mathcal{N}(d_2)
$$

where $Z \sim \mathcal{N}(0,1)$ and we used:

$$
d_2 = \frac{\log(S_0/K) + (r - \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}} = -\frac{\log(K/S_0) - (r - \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}
$$

### 3. **Intuition**


- If $d_2 > 0$: More than 50% probability of finishing ITM
- If $d_2 = 0$: Exactly 50% probability (ATM forward)
- If $d_2 < 0$: Less than 50% probability of finishing ITM

**Factors increasing $\mathcal{N}(d_2)$**:

- Higher current stock price $S_0$ (already ITM)
- Lower strike $K$ (easier to exceed)
- Higher risk-free rate $r$ (stock grows faster)
- Longer time $T$ (more drift accumulation)
- Higher volatility $\sigma$ (but weaker effect due to $-\frac{1}{2}\sigma^2$ term)

---

## The Meaning of $\mathcal{N}(d_1)$


### 1. **Stock Measure Probability**


$\mathcal{N}(d_1)$ is the probability of exercise under the **stock measure** $\mathbb{Q}^S$ (where the stock is used as numeraire):

$$
\boxed{\mathcal{N}(d_1) = \mathbb{Q}^S(S_T > K)}
$$

### 2. **Derivation via Measure Change**


Under the stock measure, the Radon-Nikodym derivative is:

$$
\frac{d\mathbb{Q}^S}{d\mathbb{Q}} = \frac{S_T e^{-rT}}{S_0}
$$

Under $\mathbb{Q}^S$, the stock price dynamics shift:

$$
S_T = S_0 e^{(r + \frac{1}{2}\sigma^2)T + \sigma \tilde{W}_T}
$$

where $\tilde{W}_T \sim \mathcal{N}(0, T)$ under $\mathbb{Q}^S$.

Following the same calculation as for $d_2$:

$$
\mathbb{Q}^S(S_T > K) = \mathcal{N}\left(\frac{\log(S_0/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}\right) = \mathcal{N}(d_1)
$$

### 3. **Alternative Interpretation: Delta**


$\mathcal{N}(d_1)$ also equals the option's **delta** (hedge ratio):

$$
\Delta = \frac{\partial C}{\partial S} = \mathcal{N}(d_1)
$$

This is **not a coincidence**—the delta naturally emerges as the stock-measure probability through the replication argument.

### 4. **Relationship Between $d_1$ and $d_2$**


$$
d_1 = d_2 + \sigma\sqrt{T}
$$

The difference $\sigma\sqrt{T}$ represents the **volatility-time effect** that shifts the probability when changing from risk-neutral to stock measure.

**Effect**: Since $d_1 > d_2$, we always have $\mathcal{N}(d_1) > \mathcal{N}(d_2)$ (higher probability under stock measure).

---

## The Two-Term Structure


### 1. **Call Option**


$$
C_0 = \underbrace{S_0\mathcal{N}(d_1)}_{\text{Expected stock receipt}} - \underbrace{Ke^{-rT}\mathcal{N}(d_2)}_{\text{Expected strike payment}}
$$

**Interpretation**:

1. **Strike term** $Ke^{-rT}\mathcal{N}(d_2)$:
   - Discounted strike $Ke^{-rT}$ multiplied by probability of exercise $\mathcal{N}(d_2)$
   - Expected present value of payment if exercised under $\mathbb{Q}$

2. **Stock term** $S_0\mathcal{N}(d_1)$:
   - Current stock price $S_0$ multiplied by $\mathcal{N}(d_1)$
   - This is **not** simply $\mathbb{E}^{\mathbb{Q}}[S_T | S_T > K]$
   - Rather, it equals $e^{-rT}\mathbb{E}^{\mathbb{Q}}[S_T \cdot \mathbf{1}_{\{S_T > K\}}]$ after evaluation

### 2. **Conditional Expectation Decomposition**


Define:
- $p = \mathbb{Q}(S_T > K) = \mathcal{N}(d_2)$
- $\bar{S} = \mathbb{E}^{\mathbb{Q}}[S_T | S_T > K]$ = conditional expected stock price

Then:

$$
\mathbb{E}^{\mathbb{Q}}[S_T \cdot \mathbf{1}_{\{S_T > K\}}] = \bar{S} \cdot p
$$

After calculation (completing the square in the Gaussian integral), it turns out:

$$
\bar{S} \cdot p = S_0 e^{rT} \mathcal{N}(d_1)
$$

Therefore:

$$
C_0 = e^{-rT}[\bar{S} \cdot p - K \cdot p] = e^{-rT}\bar{S} \cdot \mathcal{N}(d_2) - Ke^{-rT}\mathcal{N}(d_2)
$$

which simplifies to the BS formula.

### 3. **Put Option**


$$
P_0 = \underbrace{Ke^{-rT}\mathcal{N}(-d_2)}_{\text{Expected strike receipt}} - \underbrace{S_0\mathcal{N}(-d_1)}_{\text{Expected stock surrender}}
$$

**Interpretation**:

1. **Strike term** $Ke^{-rT}\mathcal{N}(-d_2)$:
   - Discounted strike received if $S_T < K$
   - $\mathcal{N}(-d_2) = \mathbb{Q}(S_T < K)$ = probability of exercise

2. **Stock term** $S_0\mathcal{N}(-d_1)$:
   - Value of stock surrendered if exercised
   - $\mathcal{N}(-d_1) = \mathbb{Q}^S(S_T < K)$ under stock measure

---

## Summary of Probabilities


| Term | Formula | Meaning | Measure |
|------|---------|---------|---------|
| $\mathcal{N}(d_2)$ | $\mathbb{Q}(S_T > K)$ | Prob. call finishes ITM | Risk-neutral $\mathbb{Q}$ |
| $\mathcal{N}(-d_2)$ | $\mathbb{Q}(S_T < K)$ | Prob. put finishes ITM | Risk-neutral $\mathbb{Q}$ |
| $\mathcal{N}(d_1)$ | $\mathbb{Q}^S(S_T > K)$ | Prob. call finishes ITM | Stock measure $\mathbb{Q}^S$ |
| $\mathcal{N}(-d_1)$ | $\mathbb{Q}^S(S_T < K)$ | Prob. put finishes ITM | Stock measure $\mathbb{Q}^S$ |

**Key insight**: Different measures give different probabilities for the same event. The stock measure "biases" probabilities toward higher stock prices because it uses the stock as numeraire.

---

## Numerical Example


Consider:
- $S_0 = 100$, $K = 100$ (ATM)
- $r = 5\%$, $\sigma = 20\%$, $T = 1$ year

**Step 1**: Compute $d_1$ and $d_2$

$$
d_1 = \frac{\ln(100/100) + (0.05 + 0.5 \times 0.04) \times 1}{0.2 \times 1} = \frac{0 + 0.07}{0.2} = 0.35
$$

$$
d_2 = 0.35 - 0.2 = 0.15
$$

**Step 2**: Evaluate probabilities

$$
\mathcal{N}(d_1) = \mathcal{N}(0.35) \approx 0.6368
$$

$$
\mathcal{N}(d_2) = \mathcal{N}(0.15) \approx 0.5596
$$

**Interpretation**:

- **Risk-neutral probability** of call finishing ITM: 55.96%
- **Stock measure probability** of call finishing ITM: 63.68%
- The 7.72 percentage point difference reflects the measure change

**Step 3**: Call price

$$
\begin{aligned}
C_0 &= 100 \times 0.6368 - 100 \times e^{-0.05} \times 0.5596 \\
&= 63.68 - 95.12 \times 0.5596 \\
&= 63.68 - 53.22 \\
&\approx 10.46
\end{aligned}
$$

---

## Why Two Different Probabilities?


### 1. **The Measure Change Effect**


The shift from $\mathbb{Q}$ to $\mathbb{Q}^S$ changes the drift of the stock price:

**Under $\mathbb{Q}$** (risk-neutral):

$$
dS_t = rS_t dt + \sigma S_t dW_t
$$
Expected return = risk-free rate $r$

**Under $\mathbb{Q}^S$** (stock measure):

$$
dS_t = (r + \sigma^2)S_t dt + \sigma S_t d\tilde{W}_t
$$
Expected return = $r + \sigma^2$ (higher!)

The stock measure gives more weight to paths where $S_T$ is large, increasing the probability of $S_T > K$.

### 2. **Girsanov's Theorem**


The Brownian motions under the two measures are related by:

$$
d\tilde{W}_t = dW_t + \sigma dt
$$

This drift adjustment of $\sigma dt$ shifts the distribution, causing:

$$
d_1 = d_2 + \sigma\sqrt{T}
$$

### 3. **Economic Intuition**


- **Risk-neutral measure**: Used for pricing—treats all investors as risk-neutral
- **Stock measure**: Used for hedging—gives the delta (hedge ratio)

The difference captures the **risk premium** embedded in the stock.

---

## Connection to Delta Hedging


The hedge ratio (delta) for a call is:

$$
\Delta_{\text{call}} = \frac{\partial C}{\partial S} = \mathcal{N}(d_1)
$$

**Interpretation**: To hedge a short call position, hold $\mathcal{N}(d_1)$ shares of stock.

**Why this equals the stock-measure probability**: The delta emerges naturally from the replication argument, where we solve:

$$
V = \Delta S + \beta
$$

The $\Delta$ that replicates the option is exactly the probability under the measure where $S$ is the numeraire.

---

## Limiting Cases


### 1. **Deep In-the-Money** ($S \gg K$)


- $d_1, d_2 \to +\infty$
- $\mathcal{N}(d_1), \mathcal{N}(d_2) \to 1$
- Both probabilities approach 100% (certain exercise)

Call price:

$$
C \to S - Ke^{-rT}
$$
(intrinsic value plus cost of carry)

### 2. **Deep Out-of-the-Money** ($S \ll K$)


- $d_1, d_2 \to -\infty$
- $\mathcal{N}(d_1), \mathcal{N}(d_2) \to 0$
- Both probabilities approach 0% (no exercise)

Call price:

$$
C \to 0
$$

### 3. **At-the-Money Forward** ($S = Ke^{-rT}$)


- $d_1 = \frac{\sigma\sqrt{T}}{2}$, $d_2 = -\frac{\sigma\sqrt{T}}{2}$
- $\mathcal{N}(d_1) = \mathcal{N}(-d_2) \approx 0.5 + \delta$
- $\mathcal{N}(d_2) = \mathcal{N}(-d_1) \approx 0.5 - \delta$

Both probabilities are near 50%, symmetrically distributed around 0.5.

---

## Summary


The Black-Scholes formula has a deep probabilistic structure:

1. **$\mathcal{N}(d_2)$** = Risk-neutral probability of exercise = $\mathbb{Q}(S_T > K)$

2. **$\mathcal{N}(d_1)$** = Stock-measure probability of exercise = $\mathbb{Q}^S(S_T > K)$ = Delta

3. **Two-term structure**:
   - Stock term: Expected stock value conditional on exercise (stock measure)
   - Strike term: Expected strike payment conditional on exercise (risk-neutral)

4. **Difference $d_1 - d_2 = \sigma\sqrt{T}$**: Reflects the measure change between $\mathbb{Q}$ and $\mathbb{Q}^S$

5. **Economic meaning**: 
   - $\mathbb{Q}$ for pricing (neutral to risk)
   - $\mathbb{Q}^S$ for hedging (captures risk exposure)

This probabilistic interpretation reveals that option pricing is fundamentally about **weighted expectations under carefully chosen probability measures**.
