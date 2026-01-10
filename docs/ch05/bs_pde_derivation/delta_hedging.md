# Black-Scholes PDE via Delta Hedging

The **delta hedging derivation** is the most intuitive approach from a practitioner's perspective—it constructs a **risk-free portfolio** through continuous rebalancing and invokes the no-arbitrage principle. This method reveals why the Black-Scholes PDE must hold and demonstrates the fundamental connection between hedging and pricing.

---

## 1. Setup and Assumptions

We work under the Black-Scholes-Merton framework with the following assumptions:

### **Market Model**

**Stock price dynamics**:

The stock price $S_t$ follows **geometric Brownian motion**:

$$
dS_t = \mu S_t dt + \sigma S_t dW_t
$$

where:
- $\mu$ = drift (expected return)
- $\sigma > 0$ = volatility (constant)
- $W_t$ = standard Brownian motion

**Risk-free asset** (money market account):

$$
dB_t = r B_t dt, \quad B_0 = 1
$$

where $r$ is the constant risk-free rate.

### **Derivative Contract**

Consider a European derivative with:
- Payoff: $\Phi(S_T)$ at maturity $T$
- Price: $V(t, S_t)$ at time $t$, where $V$ is a smooth function of time and stock price

**Goal**: Derive the partial differential equation that $V(t,S)$ must satisfy.

---

## 2. Step 1: Apply Itô's Lemma

Since $V = V(t, S)$ is a function of both time $t$ and the stochastic process $S_t$, we apply **Itô's lemma**:

$$
dV = \frac{\partial V}{\partial t} dt + \frac{\partial V}{\partial S} dS + \frac{1}{2} \frac{\partial^2 V}{\partial S^2} (dS)^2
$$

### **Compute the Quadratic Variation**

Substituting $dS = \mu S dt + \sigma S dW$:

$$
(dS)^2 = (\mu S dt + \sigma S dW)^2
$$

Expanding and using the **Itô multiplication rules**:
- $(dt)^2 = 0$
- $dt \cdot dW = 0$
- $(dW)^2 = dt$

we get:

$$
(dS)^2 = \sigma^2 S^2 (dW)^2 = \sigma^2 S^2 dt
$$

### **Full Expression for $dV$**

Substituting into Itô's lemma:

$$
dV = \frac{\partial V}{\partial t} dt + \frac{\partial V}{\partial S} (\mu S dt + \sigma S dW) + \frac{1}{2} \frac{\partial^2 V}{\partial S^2} (\sigma^2 S^2 dt)
$$

Collecting the $dt$ and $dW$ terms:

$$
\boxed{dV = \left( \frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} \right) dt + \sigma S \frac{\partial V}{\partial S} dW}
$$

**Key observation**: $dV$ has both a **deterministic part** (drift, proportional to $dt$) and a **stochastic part** (diffusion, proportional to $dW$).

---

## 3. Step 2: Construct the Delta-Hedged Portfolio

To eliminate the randomness in $dV$, we construct a **self-financing portfolio** $\Pi_t$ consisting of:
- **Long position**: 1 unit of the derivative (value $V$)
- **Short position**: $\Delta$ units of the stock (value $\Delta S$)

### **Portfolio Value**

$$
\Pi_t = V_t - \Delta S_t
$$

### **Key Insight**

We will choose $\Delta$ strategically to **eliminate the stochastic term** in the portfolio dynamics, making $\Pi_t$ locally risk-free.

---

## 4. Step 3: Portfolio Dynamics

The change in portfolio value over an infinitesimal time interval is:

$$
d\Pi = dV - \Delta dS
$$

Substituting the expressions for $dV$ and $dS$:

$$
\begin{aligned}
d\Pi &= \left( \frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} \right) dt + \sigma S \frac{\partial V}{\partial S} dW \\
&\quad - \Delta(\mu S dt + \sigma S dW)
\end{aligned}
$$

Rearranging:

$$
d\Pi = \left( \frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - \Delta \mu S \right) dt + \left( \sigma S \frac{\partial V}{\partial S} - \Delta \sigma S \right) dW
$$

### **Eliminate the Stochastic Term**

To make the portfolio risk-free, we **choose**:

$$
\boxed{\Delta = \frac{\partial V}{\partial S}}
$$

This is the **delta** of the option—the sensitivity of the option price to changes in the stock price.

With this choice, the stochastic terms cancel:

$$
\sigma S \frac{\partial V}{\partial S} dW - \frac{\partial V}{\partial S} \cdot \sigma S dW = 0
$$

The portfolio dynamics simplify to:

$$
d\Pi = \left( \frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - \frac{\partial V}{\partial S} \mu S \right) dt
$$

$$
= \left( \frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} \right) dt
$$

**Key result**: The drift $\mu$ has **disappeared**! The portfolio is now **locally risk-free** (deterministic).

---

## 5. Step 4: No-Arbitrage Argument

Since $\Pi$ is a **risk-free portfolio** (no stochastic component), the **no-arbitrage principle** requires that it must earn the risk-free rate $r$:

$$
d\Pi = r \Pi dt
$$

### **Express $\Pi$ in Terms of $V$ and $S$**

$$
\Pi = V - \Delta S = V - \frac{\partial V}{\partial S} S
$$

Therefore:

$$
r \Pi dt = r\left(V - S\frac{\partial V}{\partial S}\right) dt
$$

---

## 6. Step 5: Derive the Black-Scholes PDE

Equating the two expressions for $d\Pi$:

$$
\left( \frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} \right) dt = r\left(V - S\frac{\partial V}{\partial S}\right) dt
$$

Dividing both sides by $dt$ and rearranging:

$$
\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} = rV - rS\frac{\partial V}{\partial S}
$$

Rearranging to standard form:

$$
\boxed{\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0}
$$

**This is the Black-Scholes PDE.**

---

## 7. Terminal Condition

The PDE must be solved subject to the **terminal condition** (boundary condition at maturity):

$$
V(T, S) = \Phi(S)
$$

where $\Phi(S)$ is the option payoff at expiration.

### **Examples**

**European call option**:
$$
\Phi(S) = \max(S - K, 0) = (S - K)^+
$$

**European put option**:
$$
\Phi(S) = \max(K - S, 0) = (K - S)^+
$$

**Digital (binary) call**:
$$
\Phi(S) = \mathbf{1}_{\{S > K\}}
$$

The Black-Scholes PDE is solved **backward in time** from $t = T$ to $t = 0$, using the terminal payoff as the boundary condition.

---

## 8. Extension: Incorporating Continuous Dividends

In many practical applications, the underlying asset pays dividends. For stocks with regular dividend payments, we can model this as a **continuous dividend yield** $q$.

### **Modified Stock Price Dynamics**

With a continuous dividend yield $q$, the stock price dynamics become:

$$
\boxed{dS_t = (\mu - q) S_t dt + \sigma S_t dW_t}
$$

**Interpretation**:
- The dividend yield $q$ acts as a **negative drift**
- Stockholders receive dividends, reducing the capital appreciation rate
- The effective drift is $\mu - q$ instead of $\mu$

### **Re-derive the PDE with Dividends**

Following the same steps as before:

**Step 1**: Apply Itô's lemma with $dS_t = (\mu - q)S_t dt + \sigma S_t dW_t$:

$$
dV = \left( \frac{\partial V}{\partial t} + (\mu - q) S \frac{\partial V}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} \right) dt + \sigma S \frac{\partial V}{\partial S} dW
$$

**Step 2**: Construct portfolio $\Pi = V - \Delta S$ with $\Delta = \frac{\partial V}{\partial S}$:

$$
d\Pi = \left( \frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} \right) dt
$$

(The $\mu - q$ drift cancels out just as $\mu$ did before)

**Step 3**: Apply no-arbitrage condition:

The portfolio must earn the risk-free rate, but now we must account for the **dividend income**:
- Holding $\Delta$ shares short means we owe dividends at rate $q\Delta S$

The portfolio earns:

$$
d\Pi = (r\Pi + q\Delta S) dt = \left(r\Pi + qS\frac{\partial V}{\partial S}\right) dt
$$

Equating with the Itô result:

$$
\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} = rV - rS\frac{\partial V}{\partial S} + qS\frac{\partial V}{\partial S}
$$

### **Dividend-Adjusted Black-Scholes PDE**

$$
\boxed{\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + (r - q) S \frac{\partial V}{\partial S} - rV = 0}
$$

**Key change**: The drift term becomes $(r - q)S\frac{\partial V}{\partial S}$ instead of $rS\frac{\partial V}{\partial S}$.

### **Applications**

**1. Stock options with dividends**:
- Most mature stocks pay regular dividends
- Use estimated continuous yield $q$ based on dividend schedule
- Example: S&P 500 stocks average $q \approx 2\%$

**2. Exchange-Traded Funds (ETFs)**:
- ETFs hold baskets of dividend-paying stocks
- Aggregate dividend yield can be modeled as continuous rate
- Simplifies pricing framework

**3. Foreign exchange options**:
- Foreign currency earns foreign interest rate $r_f$
- Treat $q = r_f$ (foreign rate acts like dividend yield)
- Leads to Garman-Kohlhagen formula

**4. Commodity futures options**:
- Futures contracts don't pay dividends, but storage costs act like negative dividends
- Use $q < 0$ for convenience yield models

---

## 9. Key Insights

### **1. Market Completeness**

The stock and bond **span all risk**, allowing perfect replication of any derivative:
- Any derivative payoff can be synthesized using stock + bond
- The delta-hedged portfolio demonstrates this explicitly
- Completeness ensures unique pricing

### **2. Risk-Neutral Valuation**

The drift $\mu$ **does not appear** in the Black-Scholes PDE:
- Only volatility $\sigma$ and risk-free rate $r$ (and dividend yield $q$ if applicable) matter for pricing
- Investors with different expected return assumptions agree on option prices
- This is the essence of **risk-neutral valuation**

**Why $\mu$ disappears**: The hedging portfolio eliminates exposure to the stock's drift. The no-arbitrage condition then pins down the option price uniquely.

### **3. Dynamic Hedging**

The delta position $\Delta = \frac{\partial V}{\partial S}$ must be **continuously rebalanced**:
- As $S$ changes, delta changes (gamma effect)
- As time passes, delta changes (theta effect)
- Continuous adjustment is needed to maintain the hedge

**In practice**: Hedging is done discretely (daily, hourly), creating **hedging error**. The continuous model is an idealization.

### **4. Self-Financing Portfolio**

The hedging strategy requires **no external cash injection**:
- Rebalancing is done by trading stock against the money market account
- Buying more stock → borrow from money market
- Selling stock → lend to money market
- The portfolio is **self-financing** by construction

### **5. Path Independence**

The PDE derivation shows that the option value depends on:
- Current stock price $S_t$
- Current time $t$
- Parameters: $\sigma$, $r$, $q$, $K$, $T$

It does **not** depend on:
- The path taken to reach $S_t$
- The historical stock prices
- The actual drift $\mu$

This is why European options are **Markovian**—the future depends only on the present state, not the history.

---

## 10. Summary

The delta hedging derivation establishes the Black-Scholes PDE through the following logical chain:

**1. Stock dynamics** → Geometric Brownian motion $dS = \mu S dt + \sigma S dW$

**2. Itô's lemma** → Option price dynamics $dV$ has drift and diffusion

**3. Construct portfolio** → $\Pi = V - \Delta S$ with $\Delta = \frac{\partial V}{\partial S}$

**4. Eliminate randomness** → Choose delta to cancel stochastic term

**5. No-arbitrage** → Risk-free portfolio earns risk-free rate

**6. Derive PDE** → Black-Scholes equation emerges

**Result**:

$$
\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
$$

**With dividends**:

$$
\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + (r - q) S \frac{\partial V}{\partial S} - rV = 0
$$

**Why this approach is powerful**:
- Intuitive (hedging is how traders think)
- Reveals economic mechanism (replication)
- Shows why $\mu$ doesn't matter (hedging eliminates it)
- Demonstrates market completeness
- Natural for practitioners

The delta hedging derivation is called the **"hedger's approach"**—it shows that option pricing is fundamentally about constructing a replicating portfolio, and the PDE is simply the mathematical expression of this hedging strategy combined with the no-arbitrage principle.

---

## Related Derivations

The Black-Scholes PDE can also be derived via:
- **Risk-neutral measure**: Direct use of martingale pricing (see Section 2.5.2)
- **Change of numeraire**: Using stock as numeraire (see Section 2.5.3)
- **Equilibrium approach**: CAPM-based derivation (see Section 2.5.4)

Each method provides different insights, but all lead to the same PDE, demonstrating the robustness and fundamental nature of the Black-Scholes framework.
