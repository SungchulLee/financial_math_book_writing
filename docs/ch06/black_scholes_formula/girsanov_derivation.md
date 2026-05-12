# Pricing a European Call Option Using Girsanov's Theorem

We price a **European call option** on a stock whose price follows a geometric Brownian motion. We apply **Girsanov's theorem** to change from the real-world measure $\mathbb{P}$ to the risk-neutral measure $\mathbb{Q}$ under which the discounted asset price is a martingale.

!!! info "Where this fits"
    - **Roadmap row(s):** Replication, PDE, Measure change.
    - **Builds on:** [The Black-Scholes formula](bs_formula_statement.md) (the result to be derived).
    - **Feeds into:** [Probabilistic interpretation](probabilistic_interpretation.md) (the Girsanov drift shift $d_1 = d_2 + \sigma\sqrt{T}$) and [Properties and bounds](properties_and_bounds.md) (PDE structure underlying the Greeks).

!!! note "Prerequisites"
    This section assumes familiarity with Itô's formula, exponential (Doléans-Dade) martingales, equivalent measure changes, and the role of filtrations. Readers without this background may treat the derivation as a structural map and revisit after the stochastic-calculus chapter.

---

## 1 Model Setup

*Section goal: stock dynamics under the real-world measure $\mathbb{P}$ and the parameters used throughout.*

Let the stock price $S_t$ evolve under the real-world measure $\mathbb{P}$ as:

$$
dS_t = \mu S_t\, dt + \sigma S_t\, dW_t, \quad S_0 > 0
$$

Let:

- $K > 0$ be the strike price,
- $T > 0$ be the maturity,
- $r > 0$ be the risk-free interest rate,
- $\sigma > 0$ the volatility,
- $\mu$ the drift (real-world expected return).

The **European call option payoff** at time $T$ is:

$$
\max(S_T - K, 0) = (S_T - K)^+
$$

Our goal is to compute:

$$
C_0 := \mathbb{E}^{\mathbb{Q}} \left[ e^{-rT} (S_T - K)^+ \right]
$$

---

## 2 Step 1: Change of Measure Using Girsanov

*Section goal: constructing the equivalent measure $\mathbb{Q}$ under which the discounted stock is a martingale.*

We define the **market price of risk**:

$$
\theta := \frac{\mu - r}{\sigma}
$$

Girsanov's theorem tells us that under the new measure $\mathbb{Q}$ defined by:

$$
\left. \frac{d\mathbb{Q}}{d\mathbb{P}} \right|_{\mathcal{F}_T} = Z_T = \exp\left( -\theta W_T - \frac{1}{2} \theta^2 T \right)
$$

the process:

$$
\tilde{W}_t := W_t + \theta t
$$

is a **Brownian motion under $\mathbb{Q}$**. For validity, $Z$ must be a true martingale, not merely a local one; the **Novikov condition** $\mathbb{E}^{\mathbb{P}}\!\left[\exp\!\left(\frac{1}{2}\int_0^T \theta^2\,dt\right)\right] < \infty$ is the standard sufficient criterion. In the Black–Scholes setting $\theta$ is constant, so it reduces to $e^{\theta^2 T/2} < \infty$ and is automatic (see Exercise 7). Under $\mathbb{Q}$ the stock price satisfies:

$$
dS_t = r S_t\, dt + \sigma S_t\, d\tilde{W}_t
$$

This is the **risk-neutral dynamic**: the drift shifts from $\mu$ to $r$, while $\sigma$ is unchanged.

---

## 3 Step 2: Explicit Distribution of S_T under Q

*Section goal: the lognormal distribution of the terminal stock price under $\mathbb{Q}$.*

Solving the SDE under $\mathbb{Q}$:

$$
S_T = S_0 \exp\left( \left(r - \tfrac{1}{2} \sigma^2\right) T + \sigma \tilde{W}_T \right)
$$

Since $\tilde{W}_T \sim N(0, T)$ under $\mathbb{Q}$, we have:

$$
\log S_T \sim N\left( \log S_0 + \left(r - \tfrac{1}{2} \sigma^2\right)T,\; \sigma^2 T \right)
$$

---

## 4 Step 3: Compute the Call Option Price

*Section goal: evaluating $\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+]$ in closed form by Gaussian integration.*

Define:

$$
d_1 := \frac{\log(S_0/K) + (r + \frac{1}{2} \sigma^2)T}{\sigma \sqrt{T}}, \quad
d_2 := d_1 - \sigma \sqrt{T}
$$

Then the **Black–Scholes formula** gives:

$$
C_0 = S_0 \mathcal{N}(d_1) - K e^{-rT} \mathcal{N}(d_2)
$$

where $\mathcal{N}(\cdot)$ is the standard normal cumulative distribution function.

### Interpretation of the Terms

- $\mathcal{N}(d_2) = \mathbb{Q}(S_T > K)$: the risk-neutral probability that the option expires in the money.
- $\mathcal{N}(d_1) = \mathbb{Q}^S(S_T > K)$: the probability under the **stock numéraire measure** that the option expires in the money.

### Derivation Sketch

Split the discounted call payoff into a stock-receipt term and a strike-payment term:

$$
C_0 = e^{-rT}\mathbb{E}^{\mathbb{Q}}\!\left[(S_T - K)^+\right] = \underbrace{e^{-rT}\mathbb{E}^{\mathbb{Q}}\!\left[S_T\,\mathbf{1}_{\{S_T > K\}}\right]}_{\text{stock term}} - \underbrace{Ke^{-rT}\,\mathbb{Q}(S_T > K)}_{\text{strike term}}
$$

The strike term is immediate from the lognormal distribution of $S_T$ under $\mathbb{Q}$:

$$
Ke^{-rT}\,\mathbb{Q}(S_T > K) = Ke^{-rT}\,\mathcal{N}(d_2)
$$

For the stock term, change numéraire from the money-market account to the stock itself. Define the **stock numéraire measure** $\mathbb{Q}^S$ by

$$
\frac{d\mathbb{Q}^S}{d\mathbb{Q}} = \frac{e^{-rT}S_T}{S_0}
$$

(the discounted terminal stock value, normalised so that $\mathbb{E}^{\mathbb{Q}}[d\mathbb{Q}^S/d\mathbb{Q}] = 1$ by the martingale property of the discounted stock). Pulling this weight into the expectation,

$$
e^{-rT}\mathbb{E}^{\mathbb{Q}}\!\left[S_T\,\mathbf{1}_{\{S_T > K\}}\right] = S_0\,\mathbb{E}^{\mathbb{Q}^S}\!\left[\mathbf{1}_{\{S_T > K\}}\right] = S_0\,\mathbb{Q}^S(S_T > K) = S_0\,\mathcal{N}(d_1)
$$

The final identity $\mathbb{Q}^S(S_T > K) = \mathcal{N}(d_1)$ holds because Girsanov shifts the stock drift from $r$ to $r + \sigma^2$ under $\mathbb{Q}^S$, which replaces $d_2 = \frac{\log(S_0/K) + (r - \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}$ by $d_1 = \frac{\log(S_0/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}$ in the standardisation (the full drift-shift calculation is in [Probabilistic interpretation](probabilistic_interpretation.md)). Combining,

$$
C_0 = S_0\,\mathcal{N}(d_1) - Ke^{-rT}\,\mathcal{N}(d_2)
$$

Each term pairs with its natural measure: $\mathcal{N}(d_2)$ is the exercise probability under the money-market numéraire $\mathbb{Q}$, and $\mathcal{N}(d_1)$ is the exercise probability under the stock numéraire $\mathbb{Q}^S$. Forcing both integrals to stay under $\mathbb{Q}$ also works — it just routes through a Gaussian-integral completing-the-square computation that produces $\mathcal{N}(d_1)$ algebraically rather than measure-theoretically; that route is carried out in Exercise 8.

---

## 5 Final Result

*Section goal: the Black-Scholes price recovered from the martingale viewpoint.*

The **European call price** under Girsanov (risk-neutral pricing) is:

$$
\boxed{
C_0 = S_0 \mathcal{N}(d_1) - K e^{-rT} \mathcal{N}(d_2)
}
$$

where:

$$
d_1 = \frac{\log(S_0/K) + (r + \frac{1}{2} \sigma^2)T}{\sigma \sqrt{T}}, \quad
d_2 = d_1 - \sigma \sqrt{T}
$$

---

## 6 Summary of the Logic

1. **Start under $\mathbb{P}$**: $dS_t = \mu S_t\, dt + \sigma S_t\, dW_t$

2. **Use Girsanov** to define $\mathbb{Q}$ via the exponential martingale:

$$
Z_T = \exp\left( -\theta W_T - \frac{1}{2} \theta^2 T \right), \quad \theta = \frac{\mu - r}{\sigma}
$$

3. **Under $\mathbb{Q}$**: the drift becomes $r$ instead of $\mu$, giving the risk-neutral SDE.

4. **Price the option** via risk-neutral expectation: $C_0 = e^{-rT}\,\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+]$.

5. **Evaluate the expectation** using the lognormal distribution of $S_T$ under $\mathbb{Q}$ to obtain the Black–Scholes formula.

!!! note "Key Insight"
    The real-world drift $\mu$ does **not** appear in the final pricing formula. Girsanov's theorem absorbs the drift difference $\mu - r$ into the change of measure, so that option prices depend only on $r$, $\sigma$, $S_0$, $K$, and $T$.

---

## 7 PDE Perspective: Feynman–Kac Bridge

*Section goal: identifying the same price as the Feynman-Kac solution to the Black-Scholes PDE.*

The same price arises from the *PDE side* via the **Feynman–Kac theorem** — the same answer through a different lens, tying together three formulations that recur in option pricing.

**Notation note**: here $V(t, S)$ denotes the option value at calendar time $t$ with terminal date $T$, so time remaining is $T - t$. Elsewhere in the chapter $T$ denotes time-to-maturity (evaluating at $t = 0$); setting $t = 0$ below recovers that form.


$$
\begin{array}{lcc}
\text{Black-Scholes Equation} & & \displaystyle \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0\\
\\
\text{Terminal Condition} & & \displaystyle V(T, S_T) = \Phi(S_T)\\
\\
\text{Risk-Neutral SDE} & & \displaystyle dS = rS\,dt + \sigma S\,d\tilde{W}_t\\
\\
\text{Feynman-Kac Result} & & \displaystyle V(t, S) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) | S_t = S]
\end{array}
$$

The verification below shows that any $C^{1,2}$ solution of the PDE produces a $\mathbb{Q}$-martingale after discounting, which forces it to equal the conditional expectation on the right-hand side — the same expectation we evaluated explicitly in Steps 2–3 above.

### Step 7.1: Itô's Lemma applied to $V(t, S_t)$

Assume $V$ satisfies the PDE:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
$$

**Apply Itô's Lemma** to $V(t, S_t)$ under the risk-neutral dynamics:

$$\begin{array}{lll}
dV 
&=&\displaystyle V_t dt + V_S dS + \frac{1}{2}V_{SS}(dS)^2\\
&=&\displaystyle V_t dt + V_S(rS\,dt + \sigma S\,d\tilde{W}_t) + \frac{1}{2}V_{SS}\sigma^2 S^2 dt\\
&=&\displaystyle \left(V_t + rSV_S + \frac{1}{2}\sigma^2S^2V_{SS}\right)dt + \sigma SV_S d\tilde{W}_t
\end{array}$$

**Substituting the PDE constraint** ($V_t + rSV_S + \frac{1}{2}\sigma^2S^2V_{SS} = rV$):

$$
dV = rV\,dt + \sigma SV_S d\tilde{W}_t
$$

### Step 7.2: Discounted value is a $\mathbb{Q}$-martingale

Define the **discounted option value:**

$$
\tilde{V}(t) = \frac{V(t, S_t)}{e^{rt}}
$$

**Computing the differential:**

$$
d\tilde{V} 
= \frac{dV}{e^{rt}} - r\frac{V}{e^{rt}}dt 
= \frac{rV\,dt + \sigma SV_S d\tilde{W}_t}{e^{rt}} - r\frac{V}{e^{rt}}dt
= \frac{\sigma SV_S}{e^{rt}}d\tilde{W}_t 
= \sigma S\left(\frac{V_S}{e^{rt}}\right)d\tilde{W}_t
$$

**The drift term vanishes!** Therefore $\tilde{V}(t)$ is a **martingale under** $\mathbb{Q}$.

### Step 7.3: Martingale property implies risk-neutral pricing

Since $\tilde{V}(t)$ is a martingale:

$$
\tilde{V}(t) = \mathbb{E}^{\mathbb{Q}}[\tilde{V}(T) | \mathcal{F}_t]
$$

$$
\frac{V(t, S_t)}{e^{rt}} = \mathbb{E}^{\mathbb{Q}}\left[\frac{V(T, S_T)}{e^{rT}} \,\Big|\, \mathcal{F}_t\right]
$$

$$
\frac{V(t, S_t)}{e^{rt}} = \mathbb{E}^{\mathbb{Q}}\left[\frac{\Phi(S_T)}{e^{rT}} \,\Big|\, S_t = S\right]
$$

$$
\boxed{V(t, S) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) | S_t = S]}
$$

### Step 7.4: Why the real-world drift $\mu$ does not appear

The PDE derivation, like the direct Girsanov derivation in Sections 2–3, never uses $\mu$. The reason is now visible: the martingale property of $\tilde{V}(t)$ in Step 7.2 holds under $\mathbb{Q}$, and the conditional expectation in Step 7.3 is taken under $\mathbb{Q}$. The drift $\mu$ enters only via the Radon–Nikodym derivative

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\Big|_{\mathcal{F}_T} = \exp\!\left(-\frac{\mu - r}{\sigma}W_T - \frac{1}{2}\left(\frac{\mu-r}{\sigma}\right)^2 T\right)
$$

— it changes the measure under which we compute, but the final price is an integral against the $\mathbb{Q}$-density, in which $\mu$ does not appear. This is the *drift-neutral* property: option prices depend only on $\sigma$, $r$, and the option structure, not on traders' beliefs ($\mu$) about future stock returns. Consistently with this, Exercise 5 shows two traders with different $\mu$ produce identical option prices.

---

## Exercises

**Exercise 1.** Suppose the real-world drift is $\mu = 12\%$, the risk-free rate is $r = 3\%$, and the volatility is $\sigma = 20\%$. Compute the market price of risk $\theta = \frac{\mu - r}{\sigma}$ and write down the Radon–Nikodym derivative $Z_T$ explicitly for $T = 1$ year.

??? success "Solution to Exercise 1"
    The market price of risk is:

    $$
    \theta = \frac{\mu - r}{\sigma} = \frac{0.12 - 0.03}{0.20} = \frac{0.09}{0.20} = 0.45
    $$

    The Radon–Nikodym derivative for $T = 1$ is:

    $$
    Z_T = \exp\left(-\theta W_T - \frac{1}{2}\theta^2 T\right) = \exp\left(-0.45\, W_1 - \frac{1}{2}(0.45)^2 \cdot 1\right)
    $$

    $$
    = \exp\left(-0.45\, W_1 - 0.10125\right)
    $$

    where $W_1 \sim \mathcal{N}(0, 1)$ under $\mathbb{P}$. This random variable converts $\mathbb{P}$-expectations to $\mathbb{Q}$-expectations: $\mathbb{E}^{\mathbb{Q}}[X] = \mathbb{E}^{\mathbb{P}}[Z_T X]$ for any $\mathcal{F}_T$-measurable $X$.

    Note that $\theta = 0.45$ represents the excess return per unit of risk. The Sharpe ratio of the stock is $0.45$, meaning investors earn $0.45$ units of excess return for each unit of volatility risk they bear.

---
**Exercise 2.** Starting from the real-world SDE $dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$ and the Girsanov change $\tilde{W}_t = W_t + \theta t$, substitute $dW_t = d\tilde{W}_t - \theta \, dt$ to verify that the risk-neutral SDE becomes $dS_t = r S_t \, dt + \sigma S_t \, d\tilde{W}_t$.

??? success "Solution to Exercise 2"
    Starting with the real-world SDE: $dS_t = \mu S_t\, dt + \sigma S_t\, dW_t$.

    The Girsanov change defines $\tilde{W}_t = W_t + \theta t$ where $\theta = \frac{\mu - r}{\sigma}$. Therefore:

    $$
    dW_t = d\tilde{W}_t - \theta\, dt
    $$

    Substituting into the SDE:

    $$
    dS_t = \mu S_t\, dt + \sigma S_t(d\tilde{W}_t - \theta\, dt)
    $$

    $$
    = \mu S_t\, dt + \sigma S_t\, d\tilde{W}_t - \sigma\theta S_t\, dt
    $$

    $$
    = (\mu - \sigma\theta) S_t\, dt + \sigma S_t\, d\tilde{W}_t
    $$

    Substituting $\theta = \frac{\mu - r}{\sigma}$:

    $$
    \mu - \sigma\theta = \mu - \sigma \cdot \frac{\mu - r}{\sigma} = \mu - (\mu - r) = r
    $$

    Therefore:

    $$
    dS_t = r S_t\, dt + \sigma S_t\, d\tilde{W}_t
    $$

    This is the risk-neutral SDE, confirming that under $\mathbb{Q}$, the stock grows at the risk-free rate $r$ instead of the real-world drift $\mu$.

---
**Exercise 3.** Under the risk-neutral measure $\mathbb{Q}$, write the explicit solution for $S_T$ and verify that $\log S_T$ is normally distributed. State the mean and variance of $\log S_T$ under $\mathbb{Q}$ and confirm that the expected value $\mathbb{E}^{\mathbb{Q}}[S_T] = S_0 e^{rT}$.

??? success "Solution to Exercise 3"
    Under $\mathbb{Q}$, the SDE $dS_t = rS_t\, dt + \sigma S_t\, d\tilde{W}_t$ has the explicit solution:

    $$
    S_T = S_0 \exp\left[\left(r - \frac{1}{2}\sigma^2\right)T + \sigma\tilde{W}_T\right]
    $$

    Taking logarithms:

    $$
    \log S_T = \log S_0 + \left(r - \frac{1}{2}\sigma^2\right)T + \sigma\tilde{W}_T
    $$

    Since $\tilde{W}_T \sim \mathcal{N}(0, T)$ under $\mathbb{Q}$:

    $$
    \log S_T \sim \mathcal{N}\left(\log S_0 + \left(r - \frac{1}{2}\sigma^2\right)T,\; \sigma^2 T\right)
    $$

    **Mean**: $\mathbb{E}^{\mathbb{Q}}[\log S_T] = \log S_0 + (r - \frac{1}{2}\sigma^2)T$.

    **Variance**: $\text{Var}^{\mathbb{Q}}(\log S_T) = \sigma^2 T$.

    **Expected value of $S_T$**: Since $S_T$ is log-normal, $\mathbb{E}^{\mathbb{Q}}[S_T] = \exp(\text{mean} + \frac{1}{2}\text{variance})$:

    $$
    \mathbb{E}^{\mathbb{Q}}[S_T] = \exp\left[\log S_0 + \left(r - \frac{1}{2}\sigma^2\right)T + \frac{1}{2}\sigma^2 T\right] = S_0 e^{rT}
    $$

    This confirms that under the risk-neutral measure, the stock's expected return is the risk-free rate $r$, as required by the martingale property of the discounted asset price.

---
**Exercise 4.** Using the Feynman-Kac connection, show that if $V(t, S)$ satisfies the Black-Scholes PDE with terminal condition $V(T, S_T) = (S_T - K)^+$, then the discounted process $\tilde{V}(t) = e^{-rt} V(t, S_t)$ is a martingale under $\mathbb{Q}$. Verify by applying Ito's lemma to $\tilde{V}(t)$ and showing the drift vanishes.

??? success "Solution to Exercise 4"
    Let $V(t, S)$ satisfy the Black-Scholes PDE:

    $$
    V_t + rSV_S + \frac{1}{2}\sigma^2 S^2 V_{SS} = rV
    $$

    Define $\tilde{V}(t) = e^{-rt}V(t, S_t)$. By Ito's lemma applied to $e^{-rt}V(t, S_t)$:

    $$
    d\tilde{V} = -re^{-rt}V\,dt + e^{-rt}dV
    $$

    Now apply Ito's lemma to $V(t, S_t)$ under $\mathbb{Q}$ where $dS_t = rS_t\,dt + \sigma S_t\,d\tilde{W}_t$:

    $$
    dV = V_t\,dt + V_S\,dS + \frac{1}{2}V_{SS}(dS)^2
    $$

    $$
    = V_t\,dt + V_S(rS\,dt + \sigma S\,d\tilde{W}) + \frac{1}{2}V_{SS}\sigma^2 S^2\,dt
    $$

    $$
    = \left(V_t + rSV_S + \frac{1}{2}\sigma^2 S^2 V_{SS}\right)dt + \sigma S V_S\,d\tilde{W}
    $$

    Using the PDE constraint $V_t + rSV_S + \frac{1}{2}\sigma^2 S^2 V_{SS} = rV$:

    $$
    dV = rV\,dt + \sigma S V_S\,d\tilde{W}
    $$

    Substituting back:

    $$
    d\tilde{V} = -re^{-rt}V\,dt + e^{-rt}(rV\,dt + \sigma S V_S\,d\tilde{W})
    $$

    $$
    = e^{-rt}\sigma S V_S\,d\tilde{W}
    $$

    The drift term vanishes, leaving only the stochastic integral with respect to $\tilde{W}$. Therefore $\tilde{V}(t) = e^{-rt}V(t, S_t)$ is a (local) martingale under $\mathbb{Q}$.

---
**Exercise 5.** Consider two traders who agree on all market parameters except the real-world drift: Trader A believes $\mu = 8\%$ while Trader B believes $\mu = 15\%$. Show that both traders arrive at the same Black-Scholes option price, and explain why the drift $\mu$ does not appear in the pricing formula despite appearing in the Radon–Nikodym derivative.

??? success "Solution to Exercise 5"
    **Trader A** ($\mu = 8\%$) computes:

    $$
    \theta_A = \frac{0.08 - r}{\sigma}
    $$

    **Trader B** ($\mu = 15\%$) computes:

    $$
    \theta_B = \frac{0.15 - r}{\sigma}
    $$

    Each trader defines a different Radon–Nikodym derivative:

    $$
    Z_T^A = \exp\left(-\theta_A W_T - \frac{1}{2}\theta_A^2 T\right), \quad Z_T^B = \exp\left(-\theta_B W_T - \frac{1}{2}\theta_B^2 T\right)
    $$

    However, both arrive at the **same** risk-neutral measure $\mathbb{Q}$ under which $dS_t = rS_t\,dt + \sigma S_t\,d\tilde{W}_t$. This is because the Girsanov transformation absorbs the entire drift difference:

    - Trader A's $\mathbb{P}_A$-Brownian motion $W_t^A$ satisfies $\tilde{W}_t = W_t^A + \theta_A t$
    - Trader B's $\mathbb{P}_B$-Brownian motion $W_t^B$ satisfies $\tilde{W}_t = W_t^B + \theta_B t$

    Both lead to the same $\tilde{W}_t$ under $\mathbb{Q}$, and hence the same risk-neutral distribution for $S_T$. The option price is:

    $$
    C_0 = e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+] = S_0\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)
    $$

    Since $d_1$ and $d_2$ depend only on $S_0$, $K$, $r$, $\sigma$, and $T$ (not $\mu$), both traders get the same price.

    The drift $\mu$ does not appear because risk-neutral pricing is based on **replication**, not forecasting. The option can be perfectly hedged using the stock and bond, and the cost of this hedge is determined by $\sigma$ (which governs how much the stock moves) and $r$ (which governs the cost of financing), not by $\mu$ (which governs the direction of expected moves). Different beliefs about $\mu$ lead to different Radon–Nikodym derivatives but the same pricing measure.

---
**Exercise 6.** For the parameters $S_0 = 100$, $K = 105$, $r = 5\%$, $\sigma = 25\%$, $T = 0.5$, carry out the full Girsanov derivation: compute $d_1$, $d_2$, evaluate $\mathcal{N}(d_1)$ and $\mathcal{N}(d_2)$, and obtain the call price $C_0 = S_0 \mathcal{N}(d_1) - K e^{-rT} \mathcal{N}(d_2)$.

??? success "Solution to Exercise 6"
    **Parameters**: $S_0 = 100$, $K = 105$, $r = 0.05$, $\sigma = 0.25$, $T = 0.5$.

    **Step 1: Compute $d_1$**

    $$
    d_1 = \frac{\ln(100/105) + (0.05 + 0.5 \times 0.0625) \times 0.5}{0.25\sqrt{0.5}}
    $$

    $$
    = \frac{-0.04879 + (0.05 + 0.03125) \times 0.5}{0.17678} = \frac{-0.04879 + 0.04063}{0.17678} = \frac{-0.00817}{0.17678} = -0.0462
    $$

    **Step 2: Compute $d_2$**

    $$
    d_2 = -0.0462 - 0.17678 = -0.2230
    $$

    **Step 3: Evaluate $\mathcal{N}(d_1)$ and $\mathcal{N}(d_2)$**

    $$
    \mathcal{N}(-0.0462) \approx 0.4816
    $$

    $$
    \mathcal{N}(-0.2230) \approx 0.4118
    $$

    **Step 4: Compute call price**

    $$
    C_0 = 100 \times 0.4816 - 105 \times e^{-0.025} \times 0.4118
    $$

    $$
    = 48.16 - 105 \times 0.9753 \times 0.4118 = 48.16 - 42.18 = 5.98
    $$

    The European call price is approximately $\$5.98$.

---
**Exercise 7.** The Novikov condition $\mathbb{E}^{\mathbb{P}}\left[\exp\left(\frac{1}{2}\theta^2 T\right)\right] < \infty$ guarantees that the Girsanov change of measure is well-defined. Show that this condition is automatically satisfied when $\theta$ is a constant. Discuss what could go wrong if $\theta$ were a stochastic process that grows too fast.

??? success "Solution to Exercise 7"
    When $\theta$ is a constant, the Novikov condition becomes:

    $$
    \mathbb{E}^{\mathbb{P}}\left[\exp\left(\frac{1}{2}\theta^2 T\right)\right] = \exp\left(\frac{1}{2}\theta^2 T\right) < \infty
    $$

    Since $\theta$ and $T$ are finite constants, $\frac{1}{2}\theta^2 T$ is a finite number, and the exponential of a finite number is finite. Therefore the Novikov condition is automatically satisfied for any constant $\theta$. ✓

    **When $\theta_t$ is stochastic**: The Novikov condition generalizes to:

    $$
    \mathbb{E}^{\mathbb{P}}\left[\exp\left(\frac{1}{2}\int_0^T \theta_t^2\, dt\right)\right] < \infty
    $$

    If $\theta_t$ grows too fast (e.g., if $\theta_t$ itself depends on $W_t$ in a way that makes $\int_0^T \theta_t^2\, dt$ have heavy tails), this expectation can diverge.

    **What goes wrong**: If the Novikov condition fails, the exponential martingale $Z_t = \exp(-\int_0^t \theta_s\, dW_s - \frac{1}{2}\int_0^t \theta_s^2\, ds)$ may fail to be a true martingale (it could be only a supermartingale with $\mathbb{E}[Z_T] < 1$). In this case, $\mathbb{Q}$ defined by $d\mathbb{Q}/d\mathbb{P} = Z_T$ would not be a valid probability measure (it would not integrate to $1$). The Girsanov change of drift would be invalid, and the resulting "risk-neutral" pricing could produce incorrect option prices or even allow arbitrage in the model. This is a genuine concern in stochastic volatility models where the market price of volatility risk can be unbounded.

---
**Exercise 8.** Derive the Black–Scholes call price by direct Gaussian integration under $\mathbb{Q}$ alone (no change of numéraire). Substitute $S_T = S_0 e^{(r - \frac{1}{2}\sigma^2)T + \sigma\sqrt{T}\,Z}$ with $Z \sim \mathcal{N}(0,1)$ under $\mathbb{Q}$, show that $\{S_T > K\} = \{Z > -d_2\}$, split the resulting integral into a stock piece and a strike piece, and obtain the $\mathcal{N}(d_1)$ factor by completing the square in the exponent. Compare with the stock-numéraire derivation in the body: both must give the same answer.

??? success "Solution to Exercise 8"
    Under $\mathbb{Q}$, write $\tilde{W}_T = \sqrt{T}\,Z$ with $Z \sim \mathcal{N}(0,1)$, so

    $$
    S_T = S_0\,e^{(r - \frac{1}{2}\sigma^2)T + \sigma\sqrt{T}\,Z}
    $$

    The exercise condition $S_T > K$ is equivalent to

    $$
    Z > \frac{\log(K/S_0) - (r - \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}} = -d_2
    $$

    Therefore

    $$
    C_0 = e^{-rT}\int_{-d_2}^{\infty}\!\left(S_0\,e^{(r - \frac{1}{2}\sigma^2)T + \sigma\sqrt{T}\,z} - K\right)\frac{1}{\sqrt{2\pi}}e^{-z^2/2}\,dz
    $$

    Split into a stock integral $A$ and a strike integral $B$:

    $$
    A = e^{-rT}S_0\int_{-d_2}^{\infty} e^{(r - \frac{1}{2}\sigma^2)T + \sigma\sqrt{T}\,z}\,\frac{1}{\sqrt{2\pi}}e^{-z^2/2}\,dz
    $$

    $$
    B = Ke^{-rT}\int_{-d_2}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-z^2/2}\,dz
    $$

    The strike integral is the standard normal tail probability $\mathbb{P}(Z > -d_2) = \mathcal{N}(d_2)$:

    $$
    B = Ke^{-rT}\,\mathcal{N}(d_2)
    $$

    In the stock integral, the prefactor $e^{-rT}\cdot e^{rT} = 1$ cancels, leaving

    $$
    A = S_0\int_{-d_2}^{\infty}\frac{1}{\sqrt{2\pi}}\exp\!\left(-\tfrac{1}{2}\sigma^2 T + \sigma\sqrt{T}\,z - \tfrac{1}{2}z^2\right)dz
    $$

    Complete the square in the exponent:

    $$
    -\tfrac{1}{2}\sigma^2 T + \sigma\sqrt{T}\,z - \tfrac{1}{2}z^2 = -\tfrac{1}{2}(z - \sigma\sqrt{T})^2
    $$

    Substitute $u = z - \sigma\sqrt{T}$, $du = dz$. The lower limit shifts to $-d_2 - \sigma\sqrt{T} = -d_1$:

    $$
    A = S_0\int_{-d_1}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-u^2/2}\,du = S_0\,\mathcal{N}(d_1)
    $$

    Combining,

    $$
    C_0 = A - B = S_0\,\mathcal{N}(d_1) - Ke^{-rT}\,\mathcal{N}(d_2)
    $$

    **Comparison with the body derivation**: the stock-numéraire route produces $\mathcal{N}(d_1)$ as the probability $\mathbb{Q}^S(S_T > K)$ — a *measure-theoretic* statement. The route above produces the same $\mathcal{N}(d_1)$ as the result of completing the square in a Gaussian integral — an *algebraic* statement. The two routes are not just numerically equal: the completing-the-square step $-\tfrac{1}{2}(z - \sigma\sqrt{T})^2$ is exactly the Radon–Nikodym density $d\mathbb{Q}^S/d\mathbb{Q} = \exp(\sigma\tilde{W}_T - \tfrac{1}{2}\sigma^2 T)$ multiplied against the $\mathbb{Q}$-density, which is why the integration variable shifts by $\sigma\sqrt{T}$. The numéraire change makes structurally explicit what the integral computes by mechanical substitution.
