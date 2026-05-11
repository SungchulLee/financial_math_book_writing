# The Black-Scholes Formula


The **Black-Scholes formula**, derived independently by Fischer Black, Myron Scholes (1973), and Robert Merton (1973), provides a closed-form solution for pricing European options. It remains one of the most influential results in financial economics, earning Scholes and Merton the 1997 Nobel Prize in Economics.

This section presents the formula, its underlying assumptions, and the meaning of its components.

!!! info "Roadmap: Six Perspectives on the Black-Scholes Formula"
    The same closed-form result $C = S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)$ admits six different mathematical viewpoints. Each row below names a perspective, its central object, the equation that captures it, what it expresses about the option, and the sibling section in which it is developed. The remaining files in this section — [Put-call parity](put_call_parity.md), [Asymptotic behavior](asymptotic_behavior.md), and [Computational examples](computational_examples.md) — exploit these perspectives to derive constraints, limiting cases, and numerical implementation respectively.

    | Perspective | Central object | Main equation | Interpretation | Where developed |
    |---|---|---|---|---|
    | Replication | Self-financing portfolio | hedge equation $dV = \Delta\, dS + r(V - \Delta S)\, dt$ | eliminate risk by dynamic trading | [Girsanov derivation](girsanov_derivation.md) |
    | PDE | price function $V(S, t)$ | Black-Scholes PDE | local dynamics of $V$ | [Girsanov derivation](girsanov_derivation.md) |
    | Probability | risk-neutral expectation $\mathbb{E}^{\mathbb{Q}}[\,\cdot\,]$ | Feynman-Kac formula | discounted expected payoff | [Probabilistic interpretation](probabilistic_interpretation.md) |
    | Measure change | Radon-Nikodym derivative | Girsanov's theorem | drift transformation $\mathbb{P} \to \mathbb{Q} \to \mathbb{Q}^S$ | [Girsanov derivation](girsanov_derivation.md), [Probabilistic interpretation](probabilistic_interpretation.md) |
    | Geometry | convex payoff $(S_T - K)^+$ | $\Gamma > 0$ | optionality (Jensen's inequality) | [Properties and bounds](properties_and_bounds.md) |
    | Strike-space | strike second derivative $\partial^2 C / \partial K^2$ | Breeden-Litzenberger | implied risk-neutral density | [Digital option pricing](digital_option_pricing.md) |

    These are six coordinate systems on a single underlying object. The recurrence of $(d_1, d_2)$ across rows is the algebraic shadow of that unity: the same pair of numbers controls the exercise probability under $\mathbb{Q}$, the delta under $\mathbb{Q}^S$, the asymptotic limits, the strike derivative, and the Greeks.

---

## Model Setup and Assumptions

*Section goal: the geometric-Brownian-motion dynamics and the seven assumptions under which the formula is valid.*

### 1. **Asset Price Dynamics**


The underlying asset price $S_t$ follows **geometric Brownian motion** under the risk-neutral measure $\mathbb{Q}$:

$$
dS_t = rS_t dt + \sigma S_t dW_t
$$

where:

- $r$ = risk-free interest rate (continuously compounded, constant)
- $\sigma$ = volatility (constant)
- $W_t$ = standard Brownian motion under $\mathbb{Q}$

**Equivalent representation**:

$$
S_t = S_0 \exp\left(\left(r - \frac{1}{2}\sigma^2\right)t + \sigma W_t\right)
$$

### 2. **Fundamental Assumptions**


**Market structure:**

1. **Frictionless markets**: No transaction costs, taxes, or restrictions on short selling
2. **Continuous trading**: Assets can be traded continuously in time
3. **No arbitrage**: The market admits no risk-free profits

**Price dynamics:**

4. **Constant parameters**: Risk-free rate $r$ and volatility $\sigma$ are known constants
5. **Log-normal returns**: Log-returns $\log(S_t / S_0)$ are normally distributed
6. **No dividends**: The underlying asset pays no dividends during the option's life

**Contract:**

7. **European exercise**: Options can only be exercised at maturity $T$

### 3. **Contract Specifications**


- $S$ (or $S_0$) = current asset price
- $K$ = strike price (exercise price)
- $T$ = time to maturity (in years)

We price at time $0$ throughout, so $T$ plays the dual role of *maturity date* and *time remaining*. When discussing time evolution we use $T \to 0$ instead of $t \to T$.

---

## The Black-Scholes Formulas

*Section goal: the call and put pricing formulas, stated as a theorem with the rigour caveat.*

### 1. **European Call Option**


!!! note "Theorem (Black-Scholes Formula)"
    Under assumptions 1–7 above — together with the standard admissibility conditions on trading strategies and a Brownian filtration — the market is complete, the equivalent martingale measure $\mathbb{Q}$ is unique, and the unique arbitrage-free time-$0$ prices of European call and put options with strike $K$ and maturity $T$ are:

    $$\begin{array}{llrrr}
    C &=& S\mathcal{N}(d_1) &-& Ke^{-rT}\mathcal{N}(d_2)\\
    P &=& Ke^{-rT}\mathcal{N}(-d_2) &-& S\mathcal{N}(-d_1)
    \end{array}$$

    where

    $$
    d_1 
    = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}, \qquad 
    d_2 
    = \frac{\ln(S/K) + (r - \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}
    = d_1 - \sigma\sqrt{T}
    $$

    A fully rigorous proof requires the stochastic-calculus machinery (Itô's formula, Girsanov's theorem, martingale representation, admissibility) developed in later chapters; here we record the result and analyze its structure.



**Notation**: $\mathcal{N}(x)$ denotes the **cumulative distribution function** of the standard normal distribution:

$$
\mathcal{N}(x) = \mathbb{P}(Z \leq x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^x e^{-\frac{z^2}{2}} dz  \quad \text{where } Z \sim \mathcal{N}(0,1)
$$

---

## Component Analysis

*Section goal: decomposition and interpretation of the parameters $d_1$ and $d_2$.*

### 1. **The d_1 Parameter**


$$
d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}
$$

**Structure**:

- **Numerator**: Log-moneyness $\ln(S/K)$ plus drift-adjusted growth $(r + \frac{1}{2}\sigma^2)T$
- **Denominator**: Volatility-adjusted time $\sigma\sqrt{T}$

**Probabilistic interpretation (summary)**: $\mathcal{N}(d_2) = \mathbb{Q}(S_T > K)$ is the risk-neutral exercise probability, and $\mathcal{N}(d_1) = \mathbb{Q}^S(S_T > K)$ is the same exercise probability under the stock-numéraire measure. The relation $d_1 = d_2 + \sigma\sqrt{T}$ encodes the Girsanov drift shift between the two measures. See [probabilistic interpretation](probabilistic_interpretation.md) for the full derivation, including the conditional-expectation decomposition of the two-term formula and the connection to delta hedging.

### 2. **The d_2 Parameter**


$$
d_2 = d_1 - \sigma\sqrt{T}
$$

The gap $d_1 - d_2 = \sigma\sqrt{T}$ widens with volatility and time.

### 3. **Key Identity**


The normal density values at $d_1$ and $d_2$ satisfy a fundamental relation used throughout the Greeks derivations:

$$
S\,\phi(d_1) = Ke^{-rT}\phi(d_2)
$$

where $\phi(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$ is the standard normal density. This follows from $d_1^2 - d_2^2 = 2\left[\ln(S/K) + rT\right]$.

### 4. **The Normal CDF N(·)**


**Properties**:

- $\mathcal{N}(0) = 0.5$ (median)
- $\mathcal{N}(x) \to 1$ as $x \to \infty$
- $\mathcal{N}(x) \to 0$ as $x \to -\infty$
- $\mathcal{N}(-x) = 1 - \mathcal{N}(x)$ (symmetry)

**Computational note**: $\mathcal{N}(x)$ has no closed form in elementary functions, but it is exactly expressible through the error function via $\mathcal{N}(x) = \tfrac{1}{2}\!\left[1 + \mathrm{erf}\!\left(x/\sqrt{2}\right)\right]$, and is efficiently computed using polynomial approximations or built-in functions (e.g., `scipy.stats.norm.cdf`).

---

## Formula Structure

*Section goal: what the two-term form $S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)$ encodes.*

Both formulas decompose into a **stock term** and a **strike term**:

$$
C = \underbrace{S\mathcal{N}(d_1)}_{\text{stock term}} - \underbrace{Ke^{-rT}\mathcal{N}(d_2)}_{\text{strike term}}, \qquad P = \underbrace{Ke^{-rT}\mathcal{N}(-d_2)}_{\text{strike term}} - \underbrace{S\mathcal{N}(-d_1)}_{\text{stock term}}
$$

The two terms are the discounted $\mathbb{Q}$-expected payments received and paid conditional on exercise; the put expression mirrors the call via $\mathcal{N}(-x) = 1 - \mathcal{N}(x)$. Full pricing-by-conditional-expectation derivation is in [probabilistic interpretation](probabilistic_interpretation.md). The shared $d_1, d_2$ structure of both formulas reflects the underlying **put-call parity** relation derived in [put-call parity](put_call_parity.md).

---

## Moneyness Classification

*Section goal: naming conventions for ITM, ATM, and OTM and their probabilistic meanings.*

### 1. **Definitions**


For a call option with strike $K$:

- **In-the-money (ITM)**: $S > K$ 

  - Intrinsic value = $S - K > 0$
  - Would have positive payoff if exercised immediately

- **At-the-money (ATM)**: $S \approx K$

  - Intrinsic value $\approx 0$
  - Most sensitive to volatility changes

- **Out-of-the-money (OTM)**: $S < K$

  - Intrinsic value = $0$
  - Pure time value

For a put: ITM when $S < K$, OTM when $S > K$.

### 2. **Relationship to d_1 and d_2**


| Moneyness | $\ln(S/K)$ | $d_1, d_2$ | $\mathcal{N}(d_1), \mathcal{N}(d_2)$ |
|-----------|------------|------------|--------------------------------------|
| Deep OTM  | $\ll 0$    | Large negative | Close to 0 |
| OTM       | $< 0$      | Negative   | $< 0.5$ |
| ATM       | $\approx 0$ | Small      | $\approx 0.5$ |
| ITM       | $> 0$      | Positive   | $> 0.5$ |
| Deep ITM  | $\gg 0$    | Large positive | Close to 1 |

---

## Special Cases

*Section goal: limiting behaviour the formula reduces to in degenerate parameter regimes.*

Three special configurations are referenced repeatedly throughout the chapter. Each is derived rigorously in [asymptotic behavior](asymptotic_behavior.md); we record only the formulas here.

| Case | Condition | Call price |
|---|---|---|
| **ATM forward (ATMF)** | $S = Ke^{-rT}$ | $d_1 = \tfrac{\sigma\sqrt{T}}{2}$, $\;d_2 = -\tfrac{\sigma\sqrt{T}}{2}$; symmetric around $\mathcal{N}(0) = 0.5$ |
| **At maturity** | $T = 0$ | $C \to (S-K)^+$, $\;P \to (K-S)^+$ (recovers the terminal payoff) |
| **Zero volatility** | $\sigma \to 0$ | $C \to (S - Ke^{-rT})^+$ (forward value, no uncertainty premium) |

The ATMF case is the natural reference point for delta hedging and the $0.4\,S\sigma\sqrt{T}$ approximation; the at-maturity case verifies the formula's terminal boundary condition; the zero-volatility case isolates the deterministic ("forward") component of the price.

---

## Comparison with Binomial Model

*Section goal: how the discrete binomial price converges to Black-Scholes as $\Delta t \to 0$.*

The Black-Scholes formula is the **continuous-time limit** of the binomial model:

| Binomial Model | Black-Scholes Model |
|----------------|---------------------|
| Discrete time steps | Continuous time |
| Two possible outcomes per step | Infinitesimal changes |
| Risk-neutral probability $q$ | Risk-neutral measure $\mathbb{Q}$ |
| Backward induction | PDE or expectation |
| $\mathcal{N}(d_2) \approx$ binomial probability | $\mathcal{N}(d_2) = \lim_{n\to\infty}$ binomial |

As the number of time steps $n \to \infty$ in the binomial model with appropriate parameter scaling:

$$
\text{Binomial price} \to \text{Black-Scholes price}
$$

---

## The Black-Scholes PDE

*Section goal: the partial differential equation the price function $V(S, t)$ must satisfy.*

### 1. **PDE Formulation**


The Black-Scholes formula is the solution to a **partial differential equation**:

$$
\boxed{\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0}
$$

with **terminal condition**:

$$
V(S,T) = \text{Payoff}(S) = \begin{cases}
(S-K)^+ & \text{for call} \\
(K-S)^+ & \text{for put}
\end{cases}
$$

**Interpretation**: Any replicable derivative whose value is $V(S,t)$ must satisfy this PDE. The equation describes how the option value evolves over time given the stock price dynamics.

### 2. **Trivial Solutions**


Before solving for option prices, observe that simple portfolios satisfy the PDE:

**1. The stock itself**: $V = S$

Verify:

$$
\frac{\partial S}{\partial t} = 0, \quad \frac{\partial S}{\partial S} = 1, \quad \frac{\partial^2 S}{\partial S^2} = 0
$$

$$
0 + \frac{1}{2}\sigma^2 S^2 \cdot 0 + rS \cdot 1 - rS = 0 \quad \checkmark
$$

**2. The risk-free bond**: $V = e^{rt}$

Verify:

$$
\frac{\partial e^{rt}}{\partial t} = re^{rt}, \quad \frac{\partial e^{rt}}{\partial S} = 0, \quad \frac{\partial^2 e^{rt}}{\partial S^2} = 0
$$

$$
re^{rt} + 0 + 0 - re^{rt} = 0 \quad \checkmark
$$

These trivial solutions confirm that the PDE correctly describes basic traded assets. Any **linear combination** of stock and bond also satisfies the PDE, which forms the basis of the **replication argument**.

### 3. **Connection to Option Pricing**


The Black-Scholes call and put formulas are **non-trivial solutions** to this PDE with the appropriate terminal conditions, derived in subsequent sections by solving the PDE through several analytical techniques.

---

## Why This Formula?

*Section goal: four equivalent derivations of the same result (PDE, replication, expectation, martingale).*

The Black-Scholes formula can be derived via several mutually consistent methods:

1. **PDE approach**: Solve the Black-Scholes partial differential equation introduced above

2. **Risk-neutral expectation**: Compute $e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+]$ directly

3. **Replication**: Construct a self-financing portfolio that replicates the option payoff

4. **Martingale theory**: Apply Girsanov's theorem and martingale pricing

!!! note "Equivalence of Perspectives"
    The PDE, risk-neutral expectation, and replication approaches are **mathematically equivalent**: each leads to the same Black-Scholes formula. The PDE characterizes local dynamics, the expectation gives a global probabilistic view, and replication reveals the hedging strategy. All three are unified by the no-arbitrage principle.

---

## Summary


The Black-Scholes formula for European options:

**Call**: $C = S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)$

**Put**: $P = Ke^{-rT}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)$

where

$$
d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}, \quad d_2 = d_1 - \sigma\sqrt{T}
$$

**Key features**:

- Closed-form solution (no numerical iteration needed)
- Depends on five observable inputs: $S$, $K$, $T$, $r$, $\sigma$
- $\mathcal{N}(d_1)$ and $\mathcal{N}(d_2)$ have probabilistic interpretations
- Decomposes into "stock term" and "strike term"
- Satisfies put-call parity, boundary conditions, and no-arbitrage constraints

The formula's elegance and practical utility have made it ubiquitous in financial markets, despite its simplifying assumptions.

---

## Exercises

**Exercise 1.** A European call option has the following parameters: $S_0 = 80$, $K = 85$, $r = 3\%$, $\sigma = 25\%$, and $T = 0.5$ years. Compute $d_1$, $d_2$, and the Black-Scholes call price $C_0$. Classify the option as ITM, ATM, or OTM.

??? success "Solution to Exercise 1"
    **Parameters**: $S_0 = 80$, $K = 85$, $r = 0.03$, $\sigma = 0.25$, $T = 0.5$.

    **Step 1: Compute $d_1$**

    $$
    d_1 = \frac{\ln(80/85) + (0.03 + 0.5 \times 0.0625) \times 0.5}{0.25\sqrt{0.5}}
    $$

    Numerator: $\ln(0.9412) + (0.03 + 0.03125) \times 0.5 = -0.06062 + 0.030625 = -0.02999$.

    Denominator: $0.25 \times 0.7071 = 0.17678$.

    $$
    d_1 = \frac{-0.02999}{0.17678} = -0.1697
    $$

    **Step 2: Compute $d_2$**

    $$
    d_2 = -0.1697 - 0.17678 = -0.3465
    $$

    **Step 3: Evaluate cumulative normal values**

    $$
    \mathcal{N}(d_1) = \mathcal{N}(-0.1697) \approx 0.4326
    $$

    $$
    \mathcal{N}(d_2) = \mathcal{N}(-0.3465) \approx 0.3645
    $$

    **Step 4: Compute call price**

    $$
    C_0 = 80 \times 0.4326 - 85 \times e^{-0.03 \times 0.5} \times 0.3645
    $$

    $$
    = 34.61 - 85 \times 0.9851 \times 0.3645 = 34.61 - 30.52 = 4.09
    $$

    **Classification**: Since $S_0 = 80 < K = 85$, the call is **out-of-the-money (OTM)**. The entire value of \$4.09 is time value.

---
**Exercise 2.** Verify that the Black-Scholes call formula satisfies the lower bound $C \geq \max(S - Ke^{-rT}, 0)$ for the parameters $S_0 = 100$, $K = 90$, $r = 5\%$, $\sigma = 30\%$, $T = 1$. Compute both sides explicitly.

??? success "Solution to Exercise 2"
    **Parameters**: $S_0 = 100$, $K = 90$, $r = 0.05$, $\sigma = 0.30$, $T = 1$.

    **Lower bound**: $\max(S_0 - Ke^{-rT}, 0) = \max(100 - 90e^{-0.05}, 0) = \max(100 - 85.61, 0) = 14.39$.

    **Compute Black-Scholes price**:

    $$
    d_1 = \frac{\ln(100/90) + (0.05 + 0.045) \times 1}{0.30} = \frac{0.10536 + 0.095}{0.30} = \frac{0.20036}{0.30} = 0.6679
    $$

    $$
    d_2 = 0.6679 - 0.30 = 0.3679
    $$

    $$
    \mathcal{N}(0.6679) \approx 0.7479, \quad \mathcal{N}(0.3679) \approx 0.6436
    $$

    $$
    C_0 = 100 \times 0.7479 - 90 \times e^{-0.05} \times 0.6436 = 74.79 - 85.61 \times 0.6436 = 74.79 - 55.10 = 19.69
    $$

    **Verification**:

    - Upper bound: $C_0 = 19.69 \leq 100 = S_0$ ✓
    - Lower bound: $C_0 = 19.69 \geq 14.39 = S_0 - Ke^{-rT}$ ✓

    Both bounds are satisfied.

---
**Exercise 3.** Starting from the Black-Scholes call formula $C = S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)$, derive the put formula

$$
P = Ke^{-rT}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)
$$

using put-call parity $C - P = S - Ke^{-rT}$ and the identity $\mathcal{N}(-x) = 1 - \mathcal{N}(x)$.

??? success "Solution to Exercise 3"
    Starting from put-call parity:

    $$
    C - P = S - Ke^{-rT}
    $$

    Solving for $P$:

    $$
    P = C - S + Ke^{-rT}
    $$

    Substituting the Black-Scholes call formula:

    $$
    P = S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2) - S + Ke^{-rT}
    $$

    Rearranging:

    $$
    P = -S[1 - \mathcal{N}(d_1)] + Ke^{-rT}[1 - \mathcal{N}(d_2)]
    $$

    Using the identity $\mathcal{N}(-x) = 1 - \mathcal{N}(x)$:

    $$
    1 - \mathcal{N}(d_1) = \mathcal{N}(-d_1), \quad 1 - \mathcal{N}(d_2) = \mathcal{N}(-d_2)
    $$

    Therefore:

    $$
    P = Ke^{-rT}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)
    $$

    This is exactly the Black-Scholes put formula.

---
**Exercise 4.** Consider the at-the-money forward case where $S = Ke^{-rT}$. Show that in this case $d_1 = \frac{\sigma\sqrt{T}}{2}$ and $d_2 = -\frac{\sigma\sqrt{T}}{2}$. Derive an approximate formula for the ATM forward call price when $\sigma\sqrt{T}$ is small, using the Taylor expansion $\mathcal{N}(x) \approx \frac{1}{2} + \frac{x}{\sqrt{2\pi}}$ for small $x$.

??? success "Solution to Exercise 4"
    When $S = Ke^{-rT}$, we have $\ln(S/K) = -rT$.

    $$
    d_1 = \frac{-rT + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}} = \frac{\frac{1}{2}\sigma^2T}{\sigma\sqrt{T}} = \frac{\sigma\sqrt{T}}{2}
    $$

    $$
    d_2 = d_1 - \sigma\sqrt{T} = \frac{\sigma\sqrt{T}}{2} - \sigma\sqrt{T} = -\frac{\sigma\sqrt{T}}{2}
    $$

    Let $\epsilon = \frac{\sigma\sqrt{T}}{2}$, which is small when $\sigma\sqrt{T}$ is small. Using $\mathcal{N}(x) \approx \frac{1}{2} + \frac{x}{\sqrt{2\pi}}$:

    $$
    C = S\mathcal{N}(\epsilon) - Ke^{-rT}\mathcal{N}(-\epsilon)
    $$

    Since $S = Ke^{-rT}$, denote this common value by $F$:

    $$
    C = F\left(\frac{1}{2} + \frac{\epsilon}{\sqrt{2\pi}}\right) - F\left(\frac{1}{2} - \frac{\epsilon}{\sqrt{2\pi}}\right) = \frac{2F\epsilon}{\sqrt{2\pi}}
    $$

    Substituting back $\epsilon = \frac{\sigma\sqrt{T}}{2}$ and $F = Ke^{-rT}$:

    $$
    C_{\text{ATMF}} \approx \frac{Ke^{-rT} \sigma\sqrt{T}}{\sqrt{2\pi}} \approx 0.3989 \cdot Ke^{-rT} \cdot \sigma\sqrt{T}
    $$

---
**Exercise 5.** Show that the Black-Scholes formula recovers the correct terminal payoff. That is, prove that as $T \to 0$ (time-to-maturity vanishing):

$$
C \to (S - K)^+ \quad \text{and} \quad P \to (K - S)^+
$$

by analyzing the limits of $d_1$ and $d_2$ separately for the cases $S > K$, $S < K$, and $S = K$.

??? success "Solution to Exercise 5"
    As $T \to 0$:

    **Case 1: $S > K$**

    $$
    d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}
    $$

    Since $\ln(S/K) > 0$ is fixed and $\sigma\sqrt{T} \to 0$, we get $d_1 \to +\infty$. Similarly $d_2 \to +\infty$.

    $$
    C \to S \cdot 1 - K \cdot e^0 \cdot 1 = S - K = (S-K)^+
    $$

    $$
    P \to K \cdot 0 - S \cdot 0 = 0 = (K-S)^+
    $$

    **Case 2: $S < K$**

    Now $\ln(S/K) < 0$, so $d_1 \to -\infty$ and $d_2 \to -\infty$.

    $$
    C \to S \cdot 0 - K \cdot 0 = 0 = (S-K)^+
    $$

    $$
    P \to K \cdot 1 - S \cdot 1 = K - S = (K-S)^+
    $$

    **Case 3: $S = K$**

    $$
    d_1 = \frac{(r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}} = \frac{(r + \frac{1}{2}\sigma^2)\sqrt{T}}{\sigma} \to 0
    $$

    Similarly $d_2 \to 0$. So $\mathcal{N}(d_1), \mathcal{N}(d_2) \to \frac{1}{2}$.

    $$
    C \to K \cdot \frac{1}{2} - K \cdot 1 \cdot \frac{1}{2} = 0 = (S-K)^+
    $$

    $$
    P \to K \cdot \frac{1}{2} - K \cdot \frac{1}{2} = 0 = (K-S)^+
    $$

    In all three cases, $C \to (S-K)^+$ and $P \to (K-S)^+$ as $T \to 0$.

---
**Exercise 6.** Verify that $V(S, t) = S$ (holding the stock) and $V(S, t) = e^{rt}$ (the risk-free bond) both satisfy the Black-Scholes PDE

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
$$

by computing each partial derivative and substituting.

??? success "Solution to Exercise 6"
    **For $V(S,t) = S$:**

    $$
    \frac{\partial V}{\partial t} = 0, \quad \frac{\partial V}{\partial S} = 1, \quad \frac{\partial^2 V}{\partial S^2} = 0
    $$

    Substituting into the PDE:

    $$
    0 + \frac{1}{2}\sigma^2 S^2 \cdot 0 + rS \cdot 1 - rS = rS - rS = 0 \quad \checkmark
    $$

    **For $V(S,t) = e^{rt}$:**

    $$
    \frac{\partial V}{\partial t} = re^{rt}, \quad \frac{\partial V}{\partial S} = 0, \quad \frac{\partial^2 V}{\partial S^2} = 0
    $$

    Substituting into the PDE:

    $$
    re^{rt} + \frac{1}{2}\sigma^2 S^2 \cdot 0 + rS \cdot 0 - re^{rt} = re^{rt} - re^{rt} = 0 \quad \checkmark
    $$

    Both trivial solutions satisfy the Black-Scholes PDE.

---
**Exercise 7.** In the zero-volatility limit $\sigma \to 0$, explain why the call price reduces to $C = \max(S - Ke^{-rT}, 0)$. What happens to $d_1$ and $d_2$ in this limit when $S > Ke^{-rT}$? When $S < Ke^{-rT}$? Relate your answer to the deterministic evolution of the stock price when $\sigma = 0$.

??? success "Solution to Exercise 7"
    When $\sigma = 0$, the stock evolves deterministically: $S_T = Se^{rT}$. There is no randomness, so the option payoff is known with certainty.

    **When $S > Ke^{-rT}$**, equivalently $Se^{rT} > K$:

    $$
    d_1 = \frac{\ln(S/K) + rT}{\sigma\sqrt{T}} + \frac{\sigma\sqrt{T}}{2}
    $$

    The numerator $\ln(S/K) + rT = \ln(Se^{rT}/K) > 0$ since $Se^{rT} > K$. Dividing by $\sigma\sqrt{T} \to 0^+$ gives $d_1 \to +\infty$. Similarly $d_2 \to +\infty$.

    $$
    C \to S \cdot 1 - Ke^{-rT} \cdot 1 = S - Ke^{-rT}
    $$

    **When $S < Ke^{-rT}$**, equivalently $Se^{rT} < K$:

    The numerator $\ln(Se^{rT}/K) < 0$, so dividing by $\sigma\sqrt{T} \to 0^+$ gives $d_1 \to -\infty$ and $d_2 \to -\infty$.

    $$
    C \to S \cdot 0 - Ke^{-rT} \cdot 0 = 0
    $$

    Combining: $C \to \max(S - Ke^{-rT}, 0)$.

    This makes sense because with $\sigma = 0$, the stock grows deterministically at rate $r$, reaching $Se^{rT}$ at maturity. The call payoff is $(Se^{rT} - K)^+ = (S - Ke^{-rT})^+ \cdot e^{rT}$, and discounting back gives $\max(S - Ke^{-rT}, 0)$. Without randomness, there is no option premium beyond the forward intrinsic value.
