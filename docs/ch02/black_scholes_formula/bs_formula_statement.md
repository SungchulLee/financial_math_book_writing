# The Black-Scholes Formula

The **Black-Scholes formula**, derived independently by Fischer Black, Myron Scholes (1973), and Robert Merton (1973), provides a closed-form solution for pricing European options. It remains one of the most influential results in financial economics, earning Scholes and Merton the 1997 Nobel Prize in Economics.

This section presents the formula, its underlying assumptions, and the meaning of its components.

---

## 1. Model Setup and Assumptions

### **Asset Price Dynamics**

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

### **Fundamental Assumptions**

1. **Frictionless markets**: No transaction costs, taxes, or restrictions on short selling

2. **Continuous trading**: Assets can be traded continuously in time

3. **Constant parameters**: Risk-free rate $r$ and volatility $\sigma$ are known constants

4. **No dividends**: The underlying asset pays no dividends during the option's life

5. **European exercise**: Options can only be exercised at maturity $T$

6. **Complete markets**: No arbitrage opportunities exist

7. **Log-normal distribution**: Asset returns are normally distributed

### **Contract Specifications**

- $S_0$ = current asset price (at time $t=0$)
- $K$ = strike price (exercise price)
- $T$ = time to maturity (in years)
- $\tau = T - t$ = time remaining (for pricing at time $t$)

---

## 2. The Black-Scholes Formulas

### **European Call Option**

The price of a European call option at time $t$ is:

$$
\boxed{C(S,t) = S\mathcal{N}(d_1) - Ke^{-r(T-t)}\mathcal{N}(d_2)}
$$

where:

$$
\boxed{d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)(T-t)}{\sigma\sqrt{T-t}}}
$$

$$
\boxed{d_2 = d_1 - \sigma\sqrt{T-t} = \frac{\ln(S/K) + (r - \frac{1}{2}\sigma^2)(T-t)}{\sigma\sqrt{T-t}}}
$$

**Notation**: $\mathcal{N}(x)$ denotes the **cumulative distribution function** of the standard normal distribution:

$$
\mathcal{N}(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^x e^{-\frac{z^2}{2}} dz = \mathbb{P}(Z \leq x) \quad \text{where } Z \sim \mathcal{N}(0,1)
$$

### **European Put Option**

The price of a European put option at time $t$ is:

$$
\boxed{P(S,t) = Ke^{-r(T-t)}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)}
$$

where $d_1$ and $d_2$ are defined identically as for the call.

**Alternative form** using $\mathcal{N}(-x) = 1 - \mathcal{N}(x)$:

$$
P(S,t) = Ke^{-r(T-t)}[1 - \mathcal{N}(d_2)] - S[1 - \mathcal{N}(d_1)]
$$

---

## 3. Component Analysis

### **The $d_1$ Parameter**

$$
d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)(T-t)}{\sigma\sqrt{T-t}}
$$

**Structure**:
- **Numerator**: Log-moneyness $\ln(S/K)$ plus drift-adjusted growth $(r + \frac{1}{2}\sigma^2)(T-t)$
- **Denominator**: Volatility-adjusted time $\sigma\sqrt{T-t}$

**Interpretation**: Measures how many standard deviations the expected log-price is above the strike (in standardized units).

**Components**:
1. $\ln(S/K)$: Current log-moneyness
   - $> 0$ if $S > K$ (in-the-money)
   - $= 0$ if $S = K$ (at-the-money)
   - $< 0$ if $S < K$ (out-of-the-money)

2. $(r + \frac{1}{2}\sigma^2)(T-t)$: Expected growth under risk-neutral measure
   - $r(T-t)$: Risk-free growth
   - $\frac{1}{2}\sigma^2(T-t)$: Volatility adjustment (Itô correction)

3. $\sigma\sqrt{T-t}$: Total uncertainty (volatility × $\sqrt{\text{time}}$)

### **The $d_2$ Parameter**

$$
d_2 = d_1 - \sigma\sqrt{T-t}
$$

**Relationship to $d_1$**: 
- $d_2$ is always less than $d_1$ by exactly the "volatility-time product"
- As volatility or time increases, the gap $d_1 - d_2$ widens

**Interpretation**: Related to the risk-neutral probability of exercise (explained in next section).

### **The Normal CDF $\mathcal{N}(\cdot)$**

**Properties**:
- $\mathcal{N}(0) = 0.5$ (median)
- $\mathcal{N}(x) \to 1$ as $x \to \infty$
- $\mathcal{N}(x) \to 0$ as $x \to -\infty$
- $\mathcal{N}(-x) = 1 - \mathcal{N}(x)$ (symmetry)

**Computational note**: $\mathcal{N}(x)$ has no closed-form expression but is efficiently computed using polynomial approximations or built-in functions in numerical software.

**Standard values**:
| $x$ | $\mathcal{N}(x)$ |
|-----|------------------|
| -3  | 0.0013 |
| -2  | 0.0228 |
| -1  | 0.1587 |
| 0   | 0.5000 |
| 1   | 0.8413 |
| 2   | 0.9772 |
| 3   | 0.9987 |

---

## 4. Formula Structure

### **Call Option Decomposition**

$$
C = \underbrace{S\mathcal{N}(d_1)}_{\text{Stock term}} - \underbrace{Ke^{-r(T-t)}\mathcal{N}(d_2)}_{\text{Strike term}}
$$

**Interpretation**:
- **Stock term** $S\mathcal{N}(d_1)$: Expected present value of receiving the stock if exercised
- **Strike term** $Ke^{-r(T-t)}\mathcal{N}(d_2)$: Expected present value of paying the strike if exercised

The call value is the difference: value received minus value paid.

### **Put Option Decomposition**

$$
P = \underbrace{Ke^{-r(T-t)}\mathcal{N}(-d_2)}_{\text{Strike term}} - \underbrace{S\mathcal{N}(-d_1)}_{\text{Stock term}}
$$

**Interpretation**:
- **Strike term** $Ke^{-r(T-t)}\mathcal{N}(-d_2)$: Expected present value of receiving the strike if exercised
- **Stock term** $S\mathcal{N}(-d_1)$: Expected present value of giving up the stock if exercised

The put value is the difference: value received minus value given up.

### **Symmetry**

Notice the structural symmetry:
- Call uses $\mathcal{N}(d_1)$ and $\mathcal{N}(d_2)$
- Put uses $\mathcal{N}(-d_1)$ and $\mathcal{N}(-d_2)$
- Both involve the same $d_1$ and $d_2$ parameters

This symmetry reflects the underlying **put-call parity** relationship.

---

## 5. Moneyness Classification

### **Definitions**

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

### **Relationship to $d_1$ and $d_2$**

| Moneyness | $\ln(S/K)$ | $d_1, d_2$ | $\mathcal{N}(d_1), \mathcal{N}(d_2)$ |
|-----------|------------|------------|--------------------------------------|
| Deep OTM  | $\ll 0$    | Large negative | Close to 0 |
| OTM       | $< 0$      | Negative   | $< 0.5$ |
| ATM       | $\approx 0$ | Small      | $\approx 0.5$ |
| ITM       | $> 0$      | Positive   | $> 0.5$ |
| Deep ITM  | $\gg 0$    | Large positive | Close to 1 |

---

## 6. Special Cases

### **At-the-Money Forward (ATMF)**

When $S = Ke^{-r(T-t)}$ (current price equals discounted strike):

$$
d_1 = \frac{\frac{1}{2}\sigma^2(T-t)}{\sigma\sqrt{T-t}} = \frac{\sigma\sqrt{T-t}}{2}
$$

$$
d_2 = -\frac{\sigma\sqrt{T-t}}{2}
$$

The call and put have **symmetric probabilities** around $\mathcal{N}(0) = 0.5$.

### **At Maturity** ($T - t = 0$)

As $t \to T$:
- If $S > K$: $d_1, d_2 \to +\infty$, so $C \to S - K$, $P \to 0$
- If $S < K$: $d_1, d_2 \to -\infty$, so $C \to 0$, $P \to K - S$
- If $S = K$: $d_1, d_2$ undefined, but limits give $C \to 0$, $P \to 0$

This recovers the **terminal payoff**: $C(S,T) = (S-K)^+$, $P(S,T) = (K-S)^+$.

### **Zero Volatility** ($\sigma \to 0$)

The formulas reduce to the **intrinsic value discounted at the risk-free rate**:

$$
C = \max(S - Ke^{-r(T-t)}, 0)
$$

$$
P = \max(Ke^{-r(T-t)} - S, 0)
$$

This is the **forward value** with no uncertainty premium.

---

## 7. Comparison with Binomial Model

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

## 8. The Black-Scholes PDE

### **PDE Formulation**

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

### **Trivial Solutions**

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

### **Connection to Option Pricing**

The Black-Scholes call and put formulas are **non-trivial solutions** to this PDE with the appropriate terminal conditions. Section 2.4 will derive the formula by solving this PDE using various analytical techniques.

---

## 9. Why This Formula?

The Black-Scholes formula can be derived via multiple methods (covered in subsequent sections):

1. **PDE approach** (Section 2.4): Solve the Black-Scholes partial differential equation (introduced in Section 8 above)

2. **Risk-neutral expectation** (Section 2.5): Compute $e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+]$ using various analytical methods

3. **Replication** (Section 2.4): Construct a self-financing portfolio that replicates the option payoff

4. **Martingale theory** (Section 2.2): Apply Girsanov's theorem and martingale pricing

Each method provides different insights into **why** this particular formula emerges from the no-arbitrage principle.

---

## 10. Summary

The Black-Scholes formula for European options:

**Call**: $C = S\mathcal{N}(d_1) - Ke^{-r(T-t)}\mathcal{N}(d_2)$

**Put**: $P = Ke^{-r(T-t)}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)$

where

$$
d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)(T-t)}{\sigma\sqrt{T-t}}, \quad d_2 = d_1 - \sigma\sqrt{T-t}
$$

**Key features**:
- Closed-form solution (no numerical iteration needed)
- Depends on five observable inputs: $S$, $K$, $T-t$, $r$, $\sigma$
- $\mathcal{N}(d_1)$ and $\mathcal{N}(d_2)$ have probabilistic interpretations
- Decomposes into "stock term" and "strike term"
- Satisfies put-call parity, boundary conditions, and no-arbitrage constraints

The formula's elegance and practical utility have made it ubiquitous in financial markets, despite its simplifying assumptions.
