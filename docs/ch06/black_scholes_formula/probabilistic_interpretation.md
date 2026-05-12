# Probabilistic Interpretation of the Black-Scholes Formula


The Black-Scholes formula is not merely a mathematical expression—it has deep **probabilistic meaning**. The terms $\mathcal{N}(d_1)$ and $\mathcal{N}(d_2)$ represent probabilities under different measures, and the formula can be understood as a weighted average of terminal payoffs.

This section reveals the probabilistic structure underlying the option pricing formula.

!!! info "Where this fits"
    - **Roadmap row(s):** Probability, Measure change.
    - **Builds on:** [The Black-Scholes formula](bs_formula_statement.md) (statement and notation).
    - **Feeds into:** [Properties and bounds](properties_and_bounds.md) (delta as $\mathcal{N}(d_1)$) and [Digital option pricing](digital_option_pricing.md) (strike differentiation extracts the implied density).

---

## Risk-Neutral Expectation

*Section goal: pricing as a discounted expectation under the risk-neutral measure $\mathbb{Q}$.*

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


**Throughout this section, $W_t$ denotes a Brownian motion under the risk-neutral measure $\mathbb{Q}$.** Under $\mathbb{Q}$, the terminal stock price is

$$
S_T = S_0 e^{(r - \frac{1}{2}\sigma^2)T + \sigma W_T}
$$

so $W_T \sim \mathcal{N}(0, T)$. After the measure change to $\mathbb{Q}^S$ below, we will work with $\widetilde{W}_t = W_t - \sigma t$ instead, which is Brownian under $\mathbb{Q}^S$ by Girsanov's theorem.

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

## The Meaning of N(d_2)

*Section goal: $\mathcal{N}(d_2)$ as the risk-neutral exercise probability $\mathbb{Q}(S_T > K)$.*

### 1. **Exercise Probability Under Q**


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

$$\begin{array}{lll}
\mathbb{Q}(S_T > K) 
&=&\displaystyle \mathbb{Q}\left(Z > \frac{\log(K/S_0) - (r - \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}\right) \\
&=&\displaystyle \mathbb{Q}\left(Z < - \frac{\log(K/S_0) - (r - \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}\right) \\
&=&\displaystyle \mathcal{N}(d_2)
\end{array}$$

where $Z \sim \mathcal{N}(0,1)$.

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

## The Meaning of N(d_1)

*Section goal: $\mathcal{N}(d_1)$ as the same exercise event measured under the stock-numéraire $\mathbb{Q}^S$.*

### 1. **Stock Measure Probability**


$\mathcal{N}(d_1)$ is the probability of exercise under the **stock measure** $\mathbb{Q}^S$ (where the stock is used as numeraire):

$$
\boxed{\mathcal{N}(d_1) = \mathbb{Q}^S(S_T > K)}
$$

### 2. **Derivation via Measure Change**


Three pieces are now in play: the risk-neutral measure $\mathbb{Q}$, the stock-numéraire measure $\mathbb{Q}^S$, and the Radon–Nikodym derivative $d\mathbb{Q}^S/d\mathbb{Q}$ that links them. Writing $B_t = e^{rt}$ for the deterministic bond-account numéraire, the change-of-numéraire weight takes the canonical *ratio-of-numéraires* form

$$
\frac{d\mathbb{Q}^S}{d\mathbb{Q}} = \frac{S_T/S_0}{B_T/B_0} = \frac{S_T\, e^{-rT}}{S_0}
$$

The numerator $S_T/S_0$ is stock-denominated growth; the denominator $B_T/B_0$ is bond-denominated growth; their ratio is exactly the relative-performance weight that reweights the measure. The same template generalises to any numéraire pair $(N, M)$ via $\dfrac{d\mathbb{Q}^N}{d\mathbb{Q}^M} = \dfrac{N_T/M_T}{N_0/M_0}$. Substituting the explicit form of $S_T$ under $\mathbb{Q}$:

$$
\frac{d\mathbb{Q}^S}{d\mathbb{Q}} = \frac{S_0 e^{(r - \frac{1}{2}\sigma^2)T + \sigma W_T} \cdot e^{-rT}}{S_0} = \exp\!\left(\sigma W_T - \frac{1}{2}\sigma^2 T\right)
$$

This is the exponential martingale $\mathcal{E}(\sigma W)_T$. By Girsanov's theorem, the process $\tilde{W}_t = W_t - \sigma t$ is a Brownian motion under $\mathbb{Q}^S$, which shifts the stock price drift from $r$ to $r + \sigma^2$:

$$
S_T = S_0 e^{(r + \frac{1}{2}\sigma^2)T + \sigma \tilde{W}_T}
$$

where $\tilde{W}_T \sim \mathcal{N}(0, T)$ under $\mathbb{Q}^S$. Following the same standardization as for $d_2$:

$$
\begin{aligned}
S_T > K
&\iff S_0 e^{(r + \frac{1}{2}\sigma^2)T + \sigma\tilde{W}_T} > K \\[2mm]
&\iff \sigma\tilde{W}_T > \log(K/S_0) - \left(r + \frac{1}{2}\sigma^2\right)T \\[2mm]
&\iff \frac{\tilde{W}_T}{\sqrt{T}} > \frac{\log(K/S_0) - \left(r + \frac{1}{2}\sigma^2\right)T}{\sigma\sqrt{T}}
\end{aligned}
$$

Since $Z = \tilde{W}_T/\sqrt{T} \sim \mathcal{N}(0,1)$ under $\mathbb{Q}^S$:

$$
\begin{aligned}
\mathbb{Q}^S(S_T > K)
&= \mathbb{Q}^S\!\left(Z > \frac{\log(K/S_0) - \left(r + \frac{1}{2}\sigma^2\right)T}{\sigma\sqrt{T}}\right) \\[2mm]
&= \mathbb{Q}^S\!\left(Z < - \frac{\log(K/S_0) - \left(r + \frac{1}{2}\sigma^2\right)T}{\sigma\sqrt{T}}\right) \\[2mm]
&= \mathcal{N}(d_1)
\end{aligned}
$$

### 3. **Alternative Interpretation: Delta**


$\mathcal{N}(d_1)$ also equals the option's **delta** (hedge ratio):

$$
\Delta = \frac{\partial C}{\partial S} = \mathcal{N}(d_1)
$$

**Two distinct interpretations, one number.** Delta is a *replication coefficient*: the share count that locally replicates the option, defined by the self-financing condition. $\mathbb{Q}^S(S_T > K)$ is a *probability* under the stock-numéraire measure, defined by Girsanov's theorem. They happen to be equal in the Black–Scholes model — this is an algebraic fact, not a definition — but they live in different conceptual categories. Treating delta as "literally a probability" is a useful mnemonic but conflates a hedging quantity with a measure-theoretic one. The agreement is what makes the numéraire-change derivation of the formula clean; it is not the reason delta works as a hedge.

### 4. **Relationship Between d_1 and d_2**


$$
d_1 = d_2 + \sigma\sqrt{T}
$$

The difference $\sigma\sqrt{T}$ represents the **volatility-time effect** that shifts the probability when changing from risk-neutral to stock measure.

**Effect**: Since $d_1 > d_2$, we always have $\mathcal{N}(d_1) > \mathcal{N}(d_2)$ (higher probability under stock measure).

---

## The Two-Term Structure

*Section goal: how $S\mathcal{N}(d_1)$ and $Ke^{-rT}\mathcal{N}(d_2)$ split a conditional expectation across two measures.*

### 1. **Call Option**


$$
C_0 = \underbrace{S_0\mathcal{N}(d_1)}_{\text{Expected stock receipt}} - \underbrace{Ke^{-rT}\mathcal{N}(d_2)}_{\text{Expected strike payment}}
$$

**Interpretation**:

1. **Strike term** $Ke^{-rT}\mathcal{N}(d_2)$: discounted strike weighted by the risk-neutral exercise probability — the expected present value of payment if exercised under $\mathbb{Q}$.

2. **Stock term** $S_0\mathcal{N}(d_1)$: equals $e^{-rT}\mathbb{E}^{\mathbb{Q}}[S_T \cdot \mathbf{1}_{\{S_T > K\}}]$ (not the simpler $\mathbb{E}^{\mathbb{Q}}[S_T | S_T > K]$).

### 2. **Conditional Expectation Decomposition**


Define:

- $p = \mathbb{Q}(S_T > K) = \mathcal{N}(d_2)$
- $\bar{S} = \mathbb{E}^{\mathbb{Q}}[S_T | S_T > K]$ = conditional expected stock price

Then:

$$
\mathbb{E}^{\mathbb{Q}}[S_T \cdot \mathbf{1}_{\{S_T > K\}}] = \bar{S} \cdot p
$$

After calculation (completing the square in the Gaussian integral, exactly as in Exercise 4), it turns out:

$$
\bar{S} \cdot p = \mathbb{E}^{\mathbb{Q}}[S_T \cdot \mathbf{1}_{\{S_T > K\}}] = S_0\, e^{rT}\, \mathcal{N}(d_1)
$$

Note that this $\mathcal{N}(d_1)$ is *not* the same probability $p = \mathcal{N}(d_2)$ — the conditional-mean factor $\bar S$ shifts the relevant standardization by exactly $\sigma\sqrt{T}$, which is the Girsanov drift to the stock measure. Substituting both pieces back:

$$
C_0 = e^{-rT}\!\left[\bar{S} \cdot p - K \cdot p\right] = \underbrace{e^{-rT}\cdot S_0 e^{rT}\mathcal{N}(d_1)}_{S_0\,\mathcal{N}(d_1)} - Ke^{-rT}\mathcal{N}(d_2) = S_0\,\mathcal{N}(d_1) - Ke^{-rT}\,\mathcal{N}(d_2)
$$

This is the Black–Scholes formula. The two-term structure thus has a clean reading: the strike term carries $\mathcal{N}(d_2)$ (the bare exercise probability), and the stock term carries $\mathcal{N}(d_1)$ (the same exercise probability re-weighted by the conditional expected stock value).

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

*Section goal: a worked illustration that $\mathcal{N}(d_1) \neq \mathcal{N}(d_2)$ and quantification of the gap.*

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
C_0 
= 100 \times 0.6368 - 100 \times e^{-0.05} \times 0.5596 
\approx 10.46
$$

---

## Why Two Different Probabilities?

*Section goal: the Girsanov drift shift and why $d_1 - d_2 = \sigma\sqrt{T}$ encodes it.*

### 1. **The Measure Change Effect**


The shift from $\mathbb{Q}$ to $\mathbb{Q}^S$ raises the expected return of the stock from $r$ to $r + \sigma^2$:

$$
dS_t = rS_t dt + \sigma S_t dW_t \quad\longrightarrow\quad dS_t = (r + \sigma^2)S_t dt + \sigma S_t d\tilde{W}_t
$$

The likelihood ratio $\frac{d\mathbb{Q}^S}{d\mathbb{Q}} = \frac{S_T e^{-rT}}{S_0}$ is *exactly proportional to the terminal stock value*, so $\mathbb{Q}^S$ tilts $\mathbb{Q}$ by a factor linear in $S_T$ — and that linear weighting is precisely what Girsanov converts into the drift shift from $r$ to $r + \sigma^2$.

### 2. **Girsanov's Theorem**


The Brownian motions under the two measures are related by $d\tilde{W}_t = dW_t + \sigma dt$, and this $\sigma dt$ adjustment is what produces $d_1 = d_2 + \sigma\sqrt{T}$.

### 3. **Economic Intuition**


- **Risk-neutral measure**: Used for pricing—treats all investors as risk-neutral
- **Stock measure**: Used for hedging—gives the delta (hedge ratio)

The difference captures the **risk premium** embedded in the stock.

!!! note "Connection to the SDF / state-price density"
    The Radon–Nikodym derivative $\frac{d\mathbb{Q}}{d\mathbb{P}}$ is closely related to the **stochastic discount factor** $M_T$ (also called the pricing kernel or state-price density): up to discounting, $M_T = e^{-rT}\,\frac{d\mathbb{Q}}{d\mathbb{P}}$. So pricing under $\mathbb{Q}$ and pricing by SDF, $V_0 = \mathbb{E}^{\mathbb{P}}[M_T \cdot \text{Payoff}]$, are the same operation written in two languages — the first absorbs discounting and risk-adjustment into a measure change, the second into a per-state weight. The numéraire change to $\mathbb{Q}^S$ then corresponds to multiplying the SDF by $S_T$ before pricing — equivalently, expressing prices in units of stock.

---

## Connection to Delta Hedging

*Section goal: why $\Delta = \mathcal{N}(d_1)$ equals a probability without literally being one.*

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

*Section goal: what the two probabilities collapse to in degenerate parameter regimes.*

### 1. **Deep In-the-Money** (S ≫ K)


- $d_1, d_2 \to +\infty$
- $\mathcal{N}(d_1), \mathcal{N}(d_2) \to 1$
- Both probabilities approach 100% (certain exercise)

Call price:

$$
C \to S - Ke^{-rT}
$$

(intrinsic value plus cost of carry)

### 2. **Deep Out-of-the-Money** (S ≪ K)


- $d_1, d_2 \to -\infty$
- $\mathcal{N}(d_1), \mathcal{N}(d_2) \to 0$
- Both probabilities approach 0% (no exercise)

Call price:

$$
C \to 0
$$

### 3. **At-the-Money Forward** (S = Ke^-rT)


- $d_1 = \frac{\sigma\sqrt{T}}{2}$, $d_2 = -\frac{\sigma\sqrt{T}}{2}$
- $\mathcal{N}(d_1) = \mathcal{N}(-d_2) \approx 0.5 + \delta$
- $\mathcal{N}(d_2) = \mathcal{N}(-d_1) \approx 0.5 - \delta$

Both probabilities are near 50%, symmetrically distributed around 0.5.

---

## Summary


The Black-Scholes formula has a deep probabilistic structure:

1. $\mathcal{N}(d_2) = \mathbb{Q}(S_T > K)$ is the risk-neutral exercise probability; $\mathcal{N}(d_1) = \mathbb{Q}^S(S_T > K)$ is the stock-measure exercise probability and equals delta.

2. The two-term structure pairs each measure with its natural quantity: the strike term carries $\mathcal{N}(d_2)$ (bare exercise probability), the stock term carries $\mathcal{N}(d_1)$ (exercise probability re-weighted by conditional expected stock value).

3. The gap $d_1 - d_2 = \sigma\sqrt{T}$ encodes the Girsanov drift between $\mathbb{Q}$ (used for pricing) and $\mathbb{Q}^S$ (used for hedging).

Option pricing is fundamentally about **weighted expectations under carefully chosen probability measures**.

---

## Exercises

**Exercise 1.** Let $S_0 = 120$, $K = 110$, $r = 4\%$, $\sigma = 30\%$, $T = 0.75$ years. Compute $d_1$ and $d_2$, then evaluate $\mathcal{N}(d_1)$ and $\mathcal{N}(d_2)$. Interpret the numerical difference $\mathcal{N}(d_1) - \mathcal{N}(d_2)$ in terms of the measure change between $\mathbb{Q}$ and $\mathbb{Q}^S$.

??? success "Solution to Exercise 1"
    **Parameters**: $S_0 = 120$, $K = 110$, $r = 0.04$, $\sigma = 0.30$, $T = 0.75$.

    **Compute $d_1$**:

    $$
    d_1 = \frac{\ln(120/110) + (0.04 + 0.5 \times 0.09) \times 0.75}{0.30\sqrt{0.75}}
    $$

    $$
    = \frac{0.08701 + (0.04 + 0.045) \times 0.75}{0.25981} = \frac{0.08701 + 0.06375}{0.25981} = \frac{0.15076}{0.25981} = 0.5803
    $$

    **Compute $d_2$**:

    $$
    d_2 = 0.5803 - 0.25981 = 0.3205
    $$

    **Evaluate probabilities**:

    $$
    \mathcal{N}(d_1) = \mathcal{N}(0.5803) \approx 0.7191
    $$

    $$
    \mathcal{N}(d_2) = \mathcal{N}(0.3205) \approx 0.6257
    $$

    **Difference**: $\mathcal{N}(d_1) - \mathcal{N}(d_2) = 0.7191 - 0.6257 = 0.0934$.

    **Interpretation**: The 9.34 percentage point gap represents the effect of changing from the risk-neutral measure $\mathbb{Q}$ to the stock measure $\mathbb{Q}^S$. Under the stock measure, the stock's drift is $r + \sigma^2 = 0.04 + 0.09 = 0.13$ instead of $r = 0.04$, which tilts the distribution toward higher stock prices and increases the probability of finishing ITM. This gap is $\mathcal{N}(d_1) - \mathcal{N}(d_2) = \mathcal{N}(d_2 + \sigma\sqrt{T}) - \mathcal{N}(d_2)$, which is approximately $\phi(d_2) \cdot \sigma\sqrt{T} \approx 0.3790 \times 0.2598 \approx 0.0985$ (close to our exact value). The gap is larger when volatility and time to maturity are large, since these amplify the drift difference between the two measures.

---
**Exercise 2.** Prove that $\mathcal{N}(d_2) = \mathbb{Q}(S_T > K)$ by starting from the log-normal distribution of $S_T$ under $\mathbb{Q}$ and standardizing the inequality $S_T > K$ to obtain a standard normal probability. Show every algebraic step.

??? success "Solution to Exercise 2"
    Under $\mathbb{Q}$, $S_T = S_0 \exp\left((r - \frac{1}{2}\sigma^2)T + \sigma W_T\right)$ where $W_T \sim \mathcal{N}(0, T)$.

    The event $S_T > K$ is equivalent to:

    $$
    S_0 \exp\left(\left(r - \frac{1}{2}\sigma^2\right)T + \sigma W_T\right) > K
    $$

    Taking logarithms:

    $$
    \ln S_0 + \left(r - \frac{1}{2}\sigma^2\right)T + \sigma W_T > \ln K
    $$

    Isolating $W_T$:

    $$
    \sigma W_T > \ln K - \ln S_0 - \left(r - \frac{1}{2}\sigma^2\right)T
    $$

    $$
    W_T > \frac{\ln(K/S_0) - (r - \frac{1}{2}\sigma^2)T}{\sigma}
    $$

    Dividing both sides by $\sqrt{T}$ to standardize (since $Z = W_T/\sqrt{T} \sim \mathcal{N}(0,1)$):

    $$
    Z > \frac{\ln(K/S_0) - (r - \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}
    $$

    Now define:

    $$
    d_2 = \frac{\ln(S_0/K) + (r - \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}
    $$

    The right-hand side of the inequality is:

    $$
    \frac{\ln(K/S_0) - (r - \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}} = \frac{-[\ln(S_0/K) + (r - \frac{1}{2}\sigma^2)T]}{\sigma\sqrt{T}} = -d_2
    $$

    Therefore:

    $$
    \mathbb{Q}(S_T > K) = \mathbb{Q}(Z > -d_2) = 1 - \mathcal{N}(-d_2) = \mathcal{N}(d_2)
    $$

    where the last step uses the symmetry $1 - \mathcal{N}(-x) = \mathcal{N}(x)$.

---
**Exercise 3.** The stock measure $\mathbb{Q}^S$ is defined by the Radon–Nikodym derivative $\frac{d\mathbb{Q}^S}{d\mathbb{Q}} = \frac{S_T e^{-rT}}{S_0}$. Show that under $\mathbb{Q}^S$, the drift of the stock price becomes $r + \sigma^2$ instead of $r$. Use Girsanov's theorem to identify the new Brownian motion $\tilde{W}_t = W_t - \sigma t$.

??? success "Solution to Exercise 3"
    The Radon–Nikodym derivative is $\frac{d\mathbb{Q}^S}{d\mathbb{Q}} = \frac{S_T e^{-rT}}{S_0}$. Under $\mathbb{Q}$:

    $$
    S_T = S_0 e^{(r - \frac{1}{2}\sigma^2)T + \sigma W_T}
    $$

    So:

    $$
    \frac{d\mathbb{Q}^S}{d\mathbb{Q}} = \frac{S_0 e^{(r - \frac{1}{2}\sigma^2)T + \sigma W_T} \cdot e^{-rT}}{S_0} = e^{-\frac{1}{2}\sigma^2 T + \sigma W_T}
    $$

    This has the form of an exponential martingale $\mathcal{E}(\sigma W)_T = \exp(\sigma W_T - \frac{1}{2}\sigma^2 T)$.

    By Girsanov's theorem, under $\mathbb{Q}^S$, the process:

    $$
    \tilde{W}_t = W_t - \sigma t
    $$

    is a Brownian motion. Substituting $W_t = \tilde{W}_t + \sigma t$ into the risk-neutral SDE:

    $$
    dS_t = rS_t\,dt + \sigma S_t\,dW_t = rS_t\,dt + \sigma S_t(d\tilde{W}_t + \sigma\,dt)
    $$

    $$
    = (r + \sigma^2)S_t\,dt + \sigma S_t\,d\tilde{W}_t
    $$

    Therefore under $\mathbb{Q}^S$, the drift of $S_t$ is $r + \sigma^2$ instead of $r$.

---
**Exercise 4.** Verify the conditional expectation identity

$$
e^{-rT}\mathbb{E}^{\mathbb{Q}}[S_T \cdot \mathbf{1}_{\{S_T > K\}}] = S_0 \mathcal{N}(d_1)
$$

by writing $S_T = S_0 e^{(r - \frac{1}{2}\sigma^2)T + \sigma\sqrt{T} Z}$ with $Z \sim \mathcal{N}(0,1)$, substituting into the expectation, and completing the square in the exponent.

??? success "Solution to Exercise 4"
    We compute $e^{-rT}\mathbb{E}^{\mathbb{Q}}[S_T \cdot \mathbf{1}_{\{S_T > K\}}]$.

    Write $S_T = S_0 e^{(r - \frac{1}{2}\sigma^2)T + \sigma\sqrt{T}Z}$ with $Z \sim \mathcal{N}(0,1)$.

    The condition $S_T > K$ becomes $Z > -d_2$ (from Exercise 2).

    $$
    e^{-rT}\mathbb{E}^{\mathbb{Q}}[S_T \cdot \mathbf{1}_{\{Z > -d_2\}}] = e^{-rT} S_0 \int_{-d_2}^{\infty} e^{(r-\frac{1}{2}\sigma^2)T + \sigma\sqrt{T}z} \frac{1}{\sqrt{2\pi}}e^{-z^2/2}\,dz
    $$

    $$
    = S_0 \int_{-d_2}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2}\sigma^2 T + \sigma\sqrt{T}z - z^2/2}\,dz
    $$

    Complete the square in the exponent:

    $$
    -\frac{1}{2}\sigma^2 T + \sigma\sqrt{T}z - \frac{z^2}{2} = -\frac{1}{2}(z - \sigma\sqrt{T})^2
    $$

    Substituting $u = z - \sigma\sqrt{T}$, so $dz = du$ and when $z = -d_2$, $u = -d_2 - \sigma\sqrt{T} = -d_1$:

    $$
    = S_0 \int_{-d_1}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-u^2/2}\,du = S_0 \mathcal{N}(d_1)
    $$

    This confirms:

    $$
    e^{-rT}\mathbb{E}^{\mathbb{Q}}[S_T \cdot \mathbf{1}_{\{S_T > K\}}] = S_0\mathcal{N}(d_1)
    $$

---
**Exercise 5.** For a European put option, show that $\mathcal{N}(-d_2) = \mathbb{Q}(S_T < K)$ is the risk-neutral probability that the put finishes in-the-money. Using the parameters $S_0 = 90$, $K = 100$, $r = 2\%$, $\sigma = 25\%$, $T = 1$, compute the risk-neutral exercise probability for the put and compare it to the stock-measure probability $\mathcal{N}(-d_1)$.

??? success "Solution to Exercise 5"
    By the complementary probability, $\mathcal{N}(-d_2) = 1 - \mathcal{N}(d_2) = 1 - \mathbb{Q}(S_T > K) = \mathbb{Q}(S_T \leq K)$.

    Since $S_T$ has a continuous distribution (log-normal), $\mathbb{Q}(S_T = K) = 0$, so:

    $$
    \mathcal{N}(-d_2) = \mathbb{Q}(S_T < K)
    $$

    **Numerical computation** with $S_0 = 90$, $K = 100$, $r = 0.02$, $\sigma = 0.25$, $T = 1$:

    $$
    d_1 = \frac{\ln(90/100) + (0.02 + 0.03125) \times 1}{0.25} = \frac{-0.10536 + 0.05125}{0.25} = \frac{-0.05411}{0.25} = -0.2164
    $$

    $$
    d_2 = -0.2164 - 0.25 = -0.4664
    $$

    **Risk-neutral exercise probability for the put**: $\mathcal{N}(-d_2) = \mathcal{N}(0.4664) = 0.6795$.

    **Stock-measure probability**: $\mathcal{N}(-d_1) = \mathcal{N}(0.2164) = 0.5857$.

    The risk-neutral probability ($67.95\%$) exceeds the stock-measure probability ($58.57\%$). This is because the stock measure tilts the distribution toward higher stock prices (drift $r + \sigma^2$ vs. $r$), making it less likely that $S_T < K$. The difference of $8.38$ percentage points reflects the measure change effect, consistent with $d_1 - d_2 = \sigma\sqrt{T} = 0.25$.

---
**Exercise 6.** Show that the difference $d_1 - d_2 = \sigma\sqrt{T}$ implies that the gap between stock-measure and risk-neutral exercise probabilities is always positive and increasing in both $\sigma$ and $T$. Under what market conditions does this gap become negligible? When does it become large?

??? success "Solution to Exercise 6"
    Since $d_1 = d_2 + \sigma\sqrt{T}$, we have:

    $$
    \mathcal{N}(d_1) - \mathcal{N}(d_2) = \mathcal{N}(d_2 + \sigma\sqrt{T}) - \mathcal{N}(d_2)
    $$

    By the mean value theorem, this equals $\phi(c) \cdot \sigma\sqrt{T}$ for some $c \in (d_2, d_1)$, where $\phi > 0$. Since $\sigma > 0$ and $T > 0$, the gap is always **strictly positive**.

    **Increasing in $\sigma$**: The gap $\sigma\sqrt{T}$ between $d_1$ and $d_2$ increases linearly in $\sigma$. Since $\phi$ is bounded and positive, the gap $\mathcal{N}(d_1) - \mathcal{N}(d_2)$ generally increases with $\sigma$ (especially for moderate values of $d_2$).

    **Increasing in $T$**: Similarly, $\sigma\sqrt{T}$ increases with $T$, widening the gap.

    **When the gap is negligible**: When $\sigma\sqrt{T} \ll 1$ (either very low volatility or very short time to maturity), $d_1 \approx d_2$ and the two probabilities are nearly equal. The two measures are "close" because the Girsanov drift adjustment $\sigma\,dt$ has little cumulative effect over a short time or with small volatility.

    **When the gap is large**: When $\sigma\sqrt{T} \gg 1$ (high volatility, long maturity), the gap between $d_1$ and $d_2$ is large, and the stock measure assigns significantly more probability to high stock prices than the risk-neutral measure. This occurs in practice for long-dated options on volatile stocks, where the hedging ratio $\mathcal{N}(d_1)$ can substantially exceed the risk-neutral exercise probability $\mathcal{N}(d_2)$.

---
**Exercise 7.** Consider a deep out-of-the-money call with $S_0 = 50$, $K = 100$, $r = 5\%$, $\sigma = 40\%$, $T = 2$. Compute $\mathcal{N}(d_1)$, $\mathcal{N}(d_2)$, and the call price. Despite the option being far OTM, explain why the call still has significant value by referring to the probabilistic interpretation and the log-normal distribution of $S_T$.

??? success "Solution to Exercise 7"
    **Parameters**: $S_0 = 50$, $K = 100$, $r = 0.05$, $\sigma = 0.40$, $T = 2$.

    $$
    d_1 = \frac{\ln(50/100) + (0.05 + 0.08) \times 2}{0.40\sqrt{2}} = \frac{-0.6931 + 0.26}{0.5657} = \frac{-0.4331}{0.5657} = -0.7655
    $$

    $$
    d_2 = -0.7655 - 0.5657 = -1.3312
    $$

    $$
    \mathcal{N}(d_1) = \mathcal{N}(-0.7655) \approx 0.2220
    $$

    $$
    \mathcal{N}(d_2) = \mathcal{N}(-1.3312) \approx 0.0916
    $$

    **Call price**:

    $$
    C_0 = 50 \times 0.2220 - 100 \times e^{-0.10} \times 0.0916 = 11.10 - 90.48 \times 0.0916 = 11.10 - 8.29 = 2.81
    $$

    Despite the stock being at half the strike price, the call is worth $\$2.81$ (about $5.6\%$ of the stock price).

    **Why the call has significant value**: The risk-neutral probability of finishing ITM is $\mathcal{N}(d_2) = 9.16\%$, which is far from negligible. This is because $S_T$ follows a log-normal distribution, which is right-skewed. With $\sigma = 40\%$ and $T = 2$ years, the total uncertainty is $\sigma\sqrt{T} = 56.57\%$, meaning the stock price can easily double or more. Specifically, a $2$-standard-deviation upward move gives $S_T = 50 \times e^{0.26 + 2 \times 0.5657} \approx 50 \times e^{1.39} \approx 201$, far above the strike. The log-normal distribution places substantial probability on extreme upward moves, and these contribute disproportionately to the option's expected payoff since the payoff is linear in $S_T - K$ for $S_T > K$. The stock-measure probability $\mathcal{N}(d_1) = 22.2\%$ is even higher, reflecting the additional upward bias of the stock numéraire measure.
