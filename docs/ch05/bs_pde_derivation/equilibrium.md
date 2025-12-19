# Consumption-Based Asset Pricing: Deep Dive

This is genuinely different because it derives asset prices from **economic equilibrium** - agent optimization plus market clearing - rather than starting with no-arbitrage. The Black-Scholes PDE emerges as a consequence of optimal behavior in general equilibrium.

## Part I: The Representative Agent Framework

### 1.1 The Optimization Problem

Consider a representative agent in a continuous-time economy with preferences over consumption streams. The agent maximizes expected lifetime utility:


$$\max \mathbb{E}\left[\int_0^\infty e^{-\rho t} U(C_t) dt\right]$$



where:
- $C_t$ is consumption at time $t$
- $\rho > 0$ is the subjective time preference rate (impatience)
- $U(\cdot)$ is the instantaneous utility function, assumed strictly increasing and strictly concave

**Standard specifications:**
- **CRRA (Constant Relative Risk Aversion):** $U(C) = \frac{C^{1-\gamma}}{1-\gamma}$ for $\gamma > 0, \gamma \neq 1$
- **Logarithmic (limiting case $\gamma = 1$):** $U(C) = \ln C$

where $\gamma$ is the coefficient of relative risk aversion.

### 1.2 Budget Constraint

The agent has wealth $W_t$ which can be invested in:
- A risky asset (stock) with price $S_t$ following $dS_t = \mu S_t dt + \sigma S_t dW_t$
- A riskless bond with price $B_t$ satisfying $dB_t = r B_t dt$

Let $\pi_t$ denote the fraction of wealth invested in the risky asset. The wealth dynamics are:


$$dW_t = [\pi_t W_t \mu + (1-\pi_t)W_t r - C_t] dt + \pi_t W_t \sigma dW_t$$



**Rewritten:**


$$dW_t = [r W_t + \pi_t W_t(\mu - r) - C_t] dt + \pi_t W_t \sigma dW_t$$



### 1.3 The Control Problem

The agent chooses $(C_t, \pi_t)$ to maximize expected utility subject to the wealth dynamics. This is a **stochastic optimal control problem**.

---

## Part II: Dynamic Programming and HJB Equation

### 2.1 Value Function

Define the value function:


$$J(W, t) = \max_{(C_s, \pi_s)_{s \geq t}} \mathbb{E}\left[\int_t^\infty e^{-\rho (s-t)} U(C_s) ds \Big| W_t = W\right]$$



In infinite horizon with time-homogeneous dynamics, we have $J(W,t) = e^{-\rho t} J(W, 0) = e^{-\rho t} J(W)$, so we can write:


$$J(W) = \max_{(C_s, \pi_s)} \mathbb{E}\left[\int_0^\infty e^{-\rho s} U(C_s) ds \Big| W_0 = W\right]$$



### 2.2 Hamilton-Jacobi-Bellman Equation

The value function must satisfy the HJB equation:


$$\rho J(W) = \max_{C, \pi} \left\{U(C) + \mathcal{L}^{C,\pi} J(W)\right\}$$



where $\mathcal{L}^{C,\pi}$ is the infinitesimal generator of the wealth process:


$$\mathcal{L}^{C,\pi} J(W) = [rW + \pi W(\mu - r) - C] J'(W) + \frac{1}{2}\pi^2 W^2 \sigma^2 J''(W)$$



**Full HJB equation:**


$$\boxed{\rho J(W) = \max_{C, \pi} \left\{U(C) + [rW + \pi W(\mu - r) - C] J'(W) + \frac{1}{2}\pi^2 W^2 \sigma^2 J''(W)\right\}}$$



### 2.3 First-Order Conditions

**Optimality with respect to $C$:**


$$\frac{\partial}{\partial C}\left\{U(C) - C J'(W)\right\} = 0$$




$$\boxed{U'(C) = J'(W)}$$



This is the **envelope condition** - marginal utility of consumption equals marginal value of wealth.

**Optimality with respect to $\pi$:**


$$\frac{\partial}{\partial \pi}\left\{W(\mu - r)\pi J'(W) + \frac{1}{2}W^2 \sigma^2 \pi^2 J''(W)\right\} = 0$$




$$W(\mu - r) J'(W) + W^2 \sigma^2 \pi J''(W) = 0$$




$$\boxed{\pi^* = -\frac{(\mu - r) J'(W)}{\sigma^2 W J''(W)} = -\frac{\mu - r}{\sigma^2} \frac{J'(W)}{W J''(W)}}$$



Define the **relative risk aversion of the value function**:


$$R_J(W) = -\frac{W J''(W)}{J'(W)}$$



Then:


$$\boxed{\pi^* = \frac{\mu - r}{\sigma^2 R_J(W)}}$$



This is the **Merton portfolio rule**.

---

## Part III: Solving for Specific Utility Functions

### 3.1 Power Utility Case

For $U(C) = \frac{C^{1-\gamma}}{1-\gamma}$, guess a solution of the form:


$$J(W) = \frac{A W^{1-\gamma}}{1-\gamma}$$



where $A > 0$ is a constant to be determined.

**Derivatives:**


$$J'(W) = A W^{-\gamma}$$




$$J''(W) = -\gamma A W^{-\gamma-1}$$



**Relative risk aversion:**


$$R_J(W) = -\frac{W J''(W)}{J'(W)} = -\frac{W(-\gamma A W^{-\gamma-1})}{A W^{-\gamma}} = \gamma$$



So the value function has constant relative risk aversion equal to $\gamma$!

### 3.2 Optimal Portfolio and Consumption

**Optimal portfolio fraction:**


$$\pi^* = \frac{\mu - r}{\gamma \sigma^2}$$



**From FOC:** $U'(C) = J'(W)$


$$C^{-\gamma} = A W^{-\gamma}$$




$$\boxed{C^* = A^{-1/\gamma} W}$$



The optimal consumption is **proportional to wealth**, with propensity to consume $A^{-1/\gamma}$.

### 3.3 Determining the Constant $A$

Substitute optimal controls into the HJB equation:


$$\rho \frac{A W^{1-\gamma}}{1-\gamma} = \frac{(A^{-1/\gamma} W)^{1-\gamma}}{1-\gamma} + \left[rW + \frac{\mu - r}{\gamma \sigma^2} W(\mu - r) - A^{-1/\gamma} W\right] A W^{-\gamma}$$




$$+ \frac{1}{2}\left(\frac{\mu - r}{\gamma \sigma^2}\right)^2 W^2 \sigma^2 (-\gamma A W^{-\gamma-1})$$



Simplify and collect terms:


$$\rho A = A^{(1-\gamma)/\gamma} + A\left[r + \frac{(\mu-r)^2}{\gamma \sigma^2} - A^{-1/\gamma}\right] - \frac{(\mu-r)^2}{2\gamma \sigma^2} A$$



After algebra, we get:


$$\boxed{A = \left[\rho + \gamma A^{-1/\gamma} - \gamma r - \frac{(1-\gamma)(\mu-r)^2}{2\gamma \sigma^2}\right]^{-\gamma}}$$



This is a nonlinear equation for $A$, but the key point is that $A$ is determined by primitives $(\rho, \gamma, r, \mu, \sigma)$.

---

## Part IV: The Stochastic Discount Factor (Pricing Kernel)

### 4.1 Fundamental Asset Pricing Equation

In equilibrium, any asset with price $P_t$ and dividend yield $\delta_t$ must satisfy:


$$P_t = \mathbb{E}\left[\int_t^T M_{t,s} \delta_s ds + M_{t,T} P_T \Big| \mathcal{F}_t\right]$$



where $M_{t,s}$ is the **stochastic discount factor** (pricing kernel):


$$\boxed{M_{t,s} = e^{-\rho(s-t)} \frac{U'(C_s)}{U'(C_t)}}$$



**Economic interpretation:** Future payoffs are discounted by:
1. Time preference: $e^{-\rho(s-t)}$
2. Marginal utility ratio: $\frac{U'(C_s)}{U'(C_t)}$ (high consumption tomorrow means lower marginal value)

### 4.2 Pricing Kernel for Power Utility

For $U(C) = \frac{C^{1-\gamma}}{1-\gamma}$:


$$U'(C) = C^{-\gamma}$$



Therefore:


$$M_{t,s} = e^{-\rho(s-t)} \left(\frac{C_s}{C_t}\right)^{-\gamma}$$



Since $C^* = A^{-1/\gamma} W$ in equilibrium:


$$\boxed{M_{t,s} = e^{-\rho(s-t)} \left(\frac{W_s}{W_t}\right)^{-\gamma}}$$



### 4.3 Market Equilibrium Condition

In a **representative agent economy**, the agent holds all assets. Market clearing requires:


$$W_t = S_t$$



(assuming the stock represents the entire productive wealth).

Therefore, the pricing kernel becomes:


$$\boxed{M_{t,s} = e^{-\rho(s-t)} \left(\frac{S_s}{S_t}\right)^{-\gamma}}$$



This is the **key equilibrium relationship**.

---

## Part V: Dynamics of the Pricing Kernel

### 5.1 Applying Itô's Lemma

The stock follows $dS_t = \mu S_t dt + \sigma S_t dW_t$. We need to find the dynamics of:


$$M_t = e^{-\rho t} S_t^{-\gamma}$$



**First, find $d(S_t^{-\gamma})$:**

By Itô's lemma with $f(S) = S^{-\gamma}$:


$$d(S_t^{-\gamma}) = -\gamma S_t^{-\gamma-1} dS_t + \frac{1}{2}(-\gamma)(-\gamma-1) S_t^{-\gamma-2} (dS_t)^2$$




$$= -\gamma S_t^{-\gamma-1}(\mu S_t dt + \sigma S_t dW_t) + \frac{1}{2}\gamma(\gamma+1) S_t^{-\gamma-2} \sigma^2 S_t^2 dt$$




$$= S_t^{-\gamma}\left[-\gamma \mu dt - \gamma \sigma dW_t + \frac{1}{2}\gamma(\gamma+1)\sigma^2 dt\right]$$




$$= S_t^{-\gamma}\left[\left(-\gamma \mu + \frac{1}{2}\gamma(\gamma+1)\sigma^2\right) dt - \gamma \sigma dW_t\right]$$



### 5.2 Full Pricing Kernel Dynamics


$$M_t = e^{-\rho t} S_t^{-\gamma}$$




$$dM_t = d(e^{-\rho t}) S_t^{-\gamma} + e^{-\rho t} d(S_t^{-\gamma}) + d(e^{-\rho t}) d(S_t^{-\gamma})$$



The cross-variation term is zero, so:


$$dM_t = -\rho e^{-\rho t} S_t^{-\gamma} dt + e^{-\rho t} S_t^{-\gamma}\left[\left(-\gamma \mu + \frac{1}{2}\gamma(\gamma+1)\sigma^2\right) dt - \gamma \sigma dW_t\right]$$




$$= M_t \left[\left(-\rho - \gamma \mu + \frac{1}{2}\gamma(\gamma+1)\sigma^2\right) dt - \gamma \sigma dW_t\right]$$



**Define:**


$$\boxed{\kappa = \rho + \gamma \mu - \frac{1}{2}\gamma(\gamma+1)\sigma^2}$$



Then:


$$\boxed{dM_t = -\kappa M_t dt - \gamma \sigma M_t dW_t}$$



This is a crucial result: the pricing kernel follows a geometric Brownian motion with drift $-\kappa$ and volatility $-\gamma\sigma$.

---

## Part VI: Risk-Free Rate in Equilibrium

### 6.1 Pricing the Risk-Free Bond

A risk-free bond with price $B_t = e^{rt}$ must satisfy:


$$B_t = \mathbb{E}[M_{t,T} B_T | \mathcal{F}_t]$$



For an infinitesimal interval:


$$1 = \mathbb{E}[M_{t, t+dt} e^{r dt} | \mathcal{F}_t]$$




$$1 = \mathbb{E}\left[\left(1 - \kappa dt - \gamma\sigma dW_t\right)(1 + r dt)\right]$$



Expanding and keeping first-order terms:


$$1 = 1 + r dt - \kappa dt$$



Therefore:


$$\boxed{r = \kappa = \rho + \gamma \mu - \frac{1}{2}\gamma(\gamma+1)\sigma^2}$$



This is the **equilibrium risk-free rate**. It increases with:
- Impatience ($\rho$)
- Expected consumption growth ($\gamma\mu$, for patient investors)
- But decreases with consumption volatility (precautionary savings effect)

---

## Part VII: Deriving Asset Prices and the PDE

### 7.1 General Asset Pricing Formula

For any asset with terminal payoff $h(S_T)$ at time $T$, the price at time $t$ is:


$$V(S_t, t) = \mathbb{E}\left[M_{t,T} h(S_T) \Big| \mathcal{F}_t\right]$$




$$= \mathbb{E}\left[e^{-\rho(T-t)} \left(\frac{S_T}{S_t}\right)^{-\gamma} h(S_T) \Big| \mathcal{F}_t\right]$$



### 7.2 Rewrite Using Change of Measure

Define:


$$\xi_t = \frac{M_t}{\mathbb{E}[M_t]}$$



This is a martingale that defines an equivalent probability measure. We can show that under this measure, the "risk-adjusted" process has modified drift.

**Alternatively, use the martingale property directly:**

Define $\tilde{V}_t = M_t V(S_t, t)$. For this to be a martingale (no-arbitrage):


$$d(M_t V_t) = M_t dV_t + V_t dM_t + dM_t dV_t$$



must have zero drift.

### 7.3 Computing $d(M_t V_t)$

**From Itô:** 


$$dV_t = \left(\frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right) dt + \sigma S \frac{\partial V}{\partial S} dW_t$$




$$dM_t = -\kappa M_t dt - \gamma\sigma M_t dW_t$$



**Cross-variation:**


$$dM_t dV_t = (-\gamma\sigma M_t)(\sigma S \frac{\partial V}{\partial S}) dt = -\gamma\sigma^2 S M_t \frac{\partial V}{\partial S} dt$$



### 7.4 Martingale Condition


$$d(M_t V_t) = M_t dV_t + V_t dM_t + dM_t dV_t$$



The drift is:


$$M_t\left(\frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right) - \kappa M_t V_t - \gamma\sigma^2 S M_t \frac{\partial V}{\partial S}$$



For zero drift:


$$\frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - \kappa V - \gamma\sigma^2 S \frac{\partial V}{\partial S} = 0$$




$$\frac{\partial V}{\partial t} + S(\mu - \gamma\sigma^2) \frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - \kappa V = 0$$



Substituting $\kappa = r$:


$$\boxed{\frac{\partial V}{\partial t} + S(\mu - \gamma\sigma^2) \frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0}$$



### 7.5 Connection to Black-Scholes

Wait! This doesn't look quite like Black-Scholes yet. We have $(\mu - \gamma\sigma^2)$ instead of $r$ in the drift term.

**The key insight:** In equilibrium with $W_t = S_t$ (market clearing), the agent's optimal portfolio must be $\pi^* = 1$ (all wealth in stock). From Merton's rule:


$$1 = \frac{\mu - r}{\gamma\sigma^2}$$



Therefore:


$$\boxed{\mu - r = \gamma\sigma^2}$$



This is the **equilibrium risk premium**!

Substituting back:


$$\mu - \gamma\sigma^2 = r$$



And we get the **Black-Scholes PDE**:


$$\boxed{\frac{\partial V}{\partial t} + rS \frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0}$$



---

## Part VIII: Economic Insights

### 8.1 The Risk Premium

The equilibrium condition $\mu - r = \gamma\sigma^2$ says:

- **Left side:** Excess return on the risky asset
- **Right side:** Risk aversion $\times$ variance

This is the **consumption CAPM** prediction: risk premia are proportional to covariance with consumption growth (here, consumption = wealth = stock).

### 8.2 Why This Derivation is Fundamentally Different

This approach:

1. **Starts with preferences** ($\rho, \gamma$) not no-arbitrage
2. **Derives the risk-free rate** from equilibrium: $r = \rho + \gamma\mu - \frac{1}{2}\gamma(\gamma+1)\sigma^2$
3. **Derives the risk premium** from market clearing: $\mu - r = \gamma\sigma^2$
4. **PDE emerges** from optimal consumption/investment decisions

In contrast, Black-Scholes derivation:
- Takes $r$ and $\mu$ as given
- Uses no-arbitrage (doesn't need to know $\mu$!)
- Doesn't explain where $r$ comes from

### 8.3 The Lucas Tree Economy

This is essentially the **Lucas (1978) asset pricing model** in continuous time:

- The "tree" (stock) pays a "fruit" (dividend) stream
- Agents consume the fruit
- Asset prices are determined by consumption smoothing desires
- General equilibrium determines both prices and interest rates

---

## Part IX: Extensions and Generalizations

### 9.1 With Dividends

If the stock pays continuous dividends $\delta S_t dt$, the equilibrium condition becomes:


$$\mu + \delta - r = \gamma\sigma^2$$



The PDE becomes:


$$\frac{\partial V}{\partial t} + (r - \delta)S \frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0$$



### 9.2 Multi-Good Economy

With multiple consumption goods and a CES aggregator:


$$U(C_1, C_2) = \left[\sum_i \omega_i C_i^{(\epsilon-1)/\epsilon}\right]^{\epsilon/(\epsilon-1)}$$



where $\epsilon$ is the elasticity of substitution, we get multi-dimensional PDEs.

### 9.3 Heterogeneous Agents

With heterogeneous agents (different $\gamma_i, \rho_i$), we need to:
1. Solve each agent's problem
2. Impose market clearing: $\sum_i W_i^* = S_t$
3. The equilibrium pricing kernel becomes a wealth-weighted average

This can generate richer dynamics and explain phenomena like the equity premium puzzle.

### 9.4 Production Economy

If firms make investment decisions, $\mu$ and $\sigma$ become endogenous:

- Firms maximize value subject to production technology
- Investment creates volatility
- Equilibrium determines $(\mu, \sigma, r)$ jointly

---

## Summary: The Complete Picture

```
Agent Preferences (ρ, γ)
        ↓
Optimal Consumption/Portfolio (HJB)
        ↓
Pricing Kernel Dynamics
        ↓
Market Clearing (W = S)
        ↓
Equilibrium Risk Premium (μ - r = γσ²)
        ↓
Equilibrium Risk-Free Rate (r = ρ + γμ - ½γ(γ+1)σ²)
        ↓
Asset Pricing via Martingale
        ↓
Black-Scholes PDE
```

**The profound insight:** Black-Scholes is not just a no-arbitrage result - it's a **general equilibrium outcome** where agents optimally trade off consumption and risk, and prices adjust to clear markets.

What would you like to explore further? 
- The equity premium puzzle and why realistic $\gamma$ can't match observed risk premia?
- Connection to the CAPM and factor models?
- The Breeden-Litzenberger result on extracting risk-neutral densities?
- Extensions to stochastic volatility from preference heterogeneity?
