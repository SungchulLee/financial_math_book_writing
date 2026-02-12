# Martingales and No-Arbitrage

This section develops the deep connection between **no-arbitrage** and **martingale pricing**. The central insight of modern asset pricing theory is that absence of arbitrage is equivalent to the existence of a probability measure under which discounted prices are martingales.

!!! info "Prerequisites"
    This section assumes familiarity with:
    
    - [Local Martingales](local_martingale.md) — the distinction between local and true martingales
    - [Stochastic Exponential](stochastic_exponential.md) — the tool for constructing measure changes

!!! note "Roadmap"
    This section provides conceptual foundations. The technical machinery (Girsanov's theorem) and applications (risk-neutral pricing) follow in subsequent sections.

---

## The Setting: Continuous-Time Financial Markets

Consider a financial market with:

- A **money market account** (risk-free asset) with dynamics:

$$
dB_t = r_t B_t\,dt, \quad B_0 = 1
$$

For constant $r$: $B_t = e^{rt}$.

- A **risky asset** with price process $S_t$ following:

$$
dS_t = \mu_t S_t\,dt + \sigma_t S_t\,dW_t
$$

under the physical (real-world) probability measure $\mathbb{P}$.

The **discounted price process** is:

$$
\tilde{S}_t = \frac{S_t}{B_t} = e^{-\int_0^t r_s\,ds} S_t
$$

Using Itô's formula:

$$
d\tilde{S}_t = (\mu_t - r_t)\tilde{S}_t\,dt + \sigma_t \tilde{S}_t\,dW_t
$$

The drift term $(\mu_t - r_t)$ is called the **excess return** or **risk premium**.

---

## What is Arbitrage?

### Informal Definition

An **arbitrage opportunity** is "free money"—a trading strategy that:

1. Costs nothing to enter
2. Cannot lose money
3. Has a positive probability of making money

### Trading Strategies and Portfolios

A **trading strategy** is a pair of adapted processes $(\phi_t, \psi_t)$ representing holdings in the risky asset and money market account.

The **portfolio value** at time $t$ is:

$$
V_t = \phi_t S_t + \psi_t B_t
$$

!!! definition "Self-Financing Strategy"
    A strategy $(\phi, \psi)$ is **self-financing** if the portfolio value changes only due to asset price movements, not from injecting or withdrawing cash:

    $$
    dV_t = \phi_t\,dS_t + \psi_t\,dB_t
    $$
    
    Equivalently, in discounted terms:

    $$
    d\tilde{V}_t = \phi_t\,d\tilde{S}_t
    $$
    
    where $\tilde{V}_t = V_t/B_t$ is the discounted portfolio value.

The self-financing condition means all gains come from trading, not from external funding.

### The Gains Process

For a self-financing strategy, the **gains process** is:

$$
G_t(\phi) = \int_0^t \phi_s\,d\tilde{S}_s
$$

This is the cumulative profit (in discounted terms) from holding $\phi_s$ shares.

!!! definition "Admissible Strategy"
    A self-financing strategy $\phi$ is **admissible** if the gains process is bounded below:

    $$
    G_t(\phi) \geq -M \quad \text{for some } M > 0 \text{ and all } t \in [0,T]
    $$
    
    This rules out "doubling strategies" that require unlimited borrowing.

### Formal Definition of Arbitrage

!!! definition "Arbitrage Opportunity"
    An **arbitrage opportunity** is an admissible self-financing strategy $\phi$ with:
    
    1. $V_0 = 0$ (zero initial cost)
    2. $V_T \geq 0$ almost surely (no possibility of loss)
    3. $\mathbb{P}(V_T > 0) > 0$ (positive probability of gain)

### NFLVR: The Technically Correct Condition

In continuous time, the naive arbitrage definition above is insufficient. The correct condition is **NFLVR** (No Free Lunch with Vanishing Risk):

!!! definition "NFLVR"
    **NFLVR** holds if there is no sequence of admissible strategies $(\phi^n)$ such that:
    
    - $V_0^n = 0$ for all $n$
    - $V_T^n \geq -1/n$ (losses vanish)
    - $V_T^n \to f$ in probability, where $f \geq 0$ and $\mathbb{P}(f > 0) > 0$

NFLVR rules out not just exact arbitrages but also sequences of "approximate arbitrages" that converge to free money. This is necessary because in continuous time, exact arbitrages may not exist while approximate ones do.

For most practical purposes, we work with the simpler definition, but NFLVR is what appears in the rigorous FTAP statement.

---

## The Connection Between Drift and Arbitrage

Under the physical measure $\mathbb{P}$, the discounted price has drift:

$$
d\tilde{S}_t = \underbrace{(\mu - r)\tilde{S}_t\,dt}_{\text{systematic drift}} + \sigma \tilde{S}_t\,dW_t
$$

### Why Drift Matters

Drift in the discounted price process violates the martingale property:

$$
\mathbb{E}^{\mathbb{P}}[\tilde{S}_T \mid \mathcal{F}_t] \neq \tilde{S}_t
$$

For $\mu > r$, the discounted price drifts upward on average. This creates **expected profit** from holding the stock (financed by borrowing), which is the essence of a risk premium.

### From Expected Profit to Arbitrage

Expected profit is not the same as arbitrage (which requires riskless profit). However, drift enables arbitrage through limiting arguments:

**Intuition**: Consider a strategy that takes a small position when the drift is favorable and scales it up. In continuous time, one can construct sequences of such strategies where:

- The expected gain remains positive
- The variance of the gain shrinks to zero
- The probability of loss vanishes

This is precisely what NFLVR rules out.

### The Key Insight

$$
\boxed{
\text{Drift in discounted prices} \iff \text{Violation of martingale property} \iff \text{Potential for arbitrage}
}
$$

To eliminate arbitrage, we need discounted prices to have **no drift**—i.e., to be martingales under some equivalent measure.

---

## The Martingale Approach to No-Arbitrage

### Core Observation

If the discounted price $\tilde{S}_t$ is a martingale under some measure $\mathbb{Q}$, then for any admissible strategy $\phi$:

$$
G_t(\phi) = \int_0^t \phi_s\,d\tilde{S}_s
$$

is a **local martingale** under $\mathbb{Q}$ (as an Itô integral with adapted integrand).

### The Supermartingale Argument

If $G_t(\phi)$ is bounded below by $-M$ (admissibility), we can show it's a supermartingale:

**Step 1**: Define $H_t = G_t(\phi) + M \geq 0$.

**Step 2**: Since $G_t$ is a local martingale, so is $H_t = G_t + M$ (adding a constant preserves the local martingale property).

**Step 3**: A **non-negative local martingale is a supermartingale** (see [Local Martingales](local_martingale.md)).

**Step 4**: Therefore $H_t$ is a supermartingale, which means:

$$
\mathbb{E}^{\mathbb{Q}}[H_T] \leq H_0 = M
$$

**Step 5**: Thus $\mathbb{E}^{\mathbb{Q}}[G_T(\phi)] = \mathbb{E}^{\mathbb{Q}}[H_T] - M \leq 0$.

### Why This Rules Out Arbitrage

For an arbitrage, we need:
- $G_T(\phi) \geq 0$ almost surely
- $\mathbb{Q}(G_T(\phi) > 0) > 0$

But if $G_T \geq 0$ and $\mathbb{E}^{\mathbb{Q}}[G_T] \leq 0$, then we must have $G_T = 0$ almost surely.

Since $\mathbb{Q}$ is **equivalent** to $\mathbb{P}$ (they have the same null sets), $G_T = 0$ $\mathbb{P}$-almost surely as well.

**Conclusion**: No arbitrage is possible!

!!! theorem "Martingale Implies No Arbitrage"
    If there exists a probability measure $\mathbb{Q} \sim \mathbb{P}$ such that discounted asset prices are $\mathbb{Q}$-local martingales, then no arbitrage opportunities exist.

---

## Why "Equivalent" Measure?

The requirement $\mathbb{Q} \sim \mathbb{P}$ (equivalence) is crucial:

!!! note "Equivalent Measures"
    Two measures $\mathbb{P}$ and $\mathbb{Q}$ are **equivalent** ($\mathbb{Q} \sim \mathbb{P}$) if they have the same null sets:
    
    $$
    \mathbb{P}(A) = 0 \iff \mathbb{Q}(A) = 0
    $$

**Why equivalence matters**:

1. **Same "possible" outcomes**: If $\mathbb{Q}$ assigned zero probability to some $\mathbb{P}$-possible event, we could have $G_T > 0$ on that event under $\mathbb{P}$ but $\mathbb{Q}(G_T > 0) = 0$, breaking the argument.

2. **Economic interpretation**: An equivalent measure preserves which scenarios can occur; it only reweights their probabilities.

3. **Arbitrage detection**: The supermartingale argument relies on $G_T = 0$ $\mathbb{Q}$-a.s. implying $G_T = 0$ $\mathbb{P}$-a.s.

---

## Why "Local" Martingale?

In continuous time, discounted prices are typically **local martingales**, not necessarily true martingales.

### The Issue

Even under the risk-neutral measure, the gains process:

$$
G_t(\phi) = \int_0^t \phi_s\,d\tilde{S}_s
$$

is only guaranteed to be a local martingale (as an Itô integral with adapted integrand).

### When Does Local Suffice?

For **admissible** strategies (gains bounded below), local martingales that are bounded below are supermartingales. This is enough to rule out arbitrage, as shown above.

### When Local Fails: Bubbles

If the discounted price is a **strict local martingale** (local but not true martingale), then:

$$
\mathbb{E}^{\mathbb{Q}}[\tilde{S}_T] < \tilde{S}_0
$$

This corresponds to a **financial bubble**—the current price exceeds the expected discounted payoff. See [Local Martingales](local_martingale.md) for detailed examples and implications.

---

## The Fundamental Theorem of Asset Pricing

The converse is also true: if there's no arbitrage, then a martingale measure must exist.

!!! theorem "Fundamental Theorem of Asset Pricing (FTAP)"
    The following are equivalent:
    
    1. **No arbitrage** (NFLVR holds)
    2. **Existence of ELMM**: There exists a probability measure $\mathbb{Q} \sim \mathbb{P}$ such that discounted asset prices are $\mathbb{Q}$-local martingales
    
    The measure $\mathbb{Q}$ is called an **Equivalent Local Martingale Measure (ELMM)**.

**Direction 1** (ELMM ⟹ No Arbitrage): Proved above using the supermartingale argument.

**Direction 2** (No Arbitrage ⟹ ELMM): This is the hard direction, requiring functional analysis (Hahn–Banach theorem, separating hyperplanes). See [FTAP](../../ch01/fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md) for the full proof.

---

## How Measure Change Removes Drift

### What Changes Under $\mathbb{Q}$

A change from $\mathbb{P}$ to $\mathbb{Q}$ does **not** alter:

- The paths of asset prices (same sample space $\Omega$)
- The available trading strategies
- The economic payoffs

It **only** alters:

- The probabilities assigned to different scenarios
- The drift of stochastic processes

### The Mechanism

Under $\mathbb{P}$:

$$
d\tilde{S}_t = (\mu - r)\tilde{S}_t\,dt + \sigma \tilde{S}_t\,dW_t^{\mathbb{P}}
$$

Under $\mathbb{Q}$ (via Girsanov):

$$
d\tilde{S}_t = \sigma \tilde{S}_t\,dW_t^{\mathbb{Q}}
$$

where $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \int_0^t \theta_s\,ds$ is a $\mathbb{Q}$-Brownian motion, with $\theta_t = (\mu_t - r_t)/\sigma_t$.

The drift has been **absorbed** into the change of Brownian motion!

### The Market Price of Risk

The quantity:

$$
\theta_t = \frac{\mu_t - r_t}{\sigma_t}
$$

is called the **market price of risk** or **Sharpe ratio**. It measures the excess return per unit of volatility.

Girsanov's theorem says: shifting Brownian motion by $\int \theta\,dt$ removes the drift from discounted prices.

---

## Example: Black–Scholes Model

### Under the Physical Measure $\mathbb{P}$

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}
$$

Discounted:

$$
d\tilde{S}_t = (\mu - r)\tilde{S}_t\,dt + \sigma \tilde{S}_t\,dW_t^{\mathbb{P}}
$$

This has drift $\mu - r \neq 0$ (typically), so the martingale property fails under $\mathbb{P}$.

### Under the Risk-Neutral Measure $\mathbb{Q}$

The market price of risk is constant: $\theta = (\mu - r)/\sigma$.

Define the Radon–Nikodym derivative:

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = \exp\left(-\theta W_T^{\mathbb{P}} - \frac{\theta^2 T}{2}\right)
$$

This is the stochastic exponential $\mathcal{E}(-\theta W^{\mathbb{P}})_T$.

Then $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \theta t$ is a $\mathbb{Q}$-Brownian motion, and:

$$
dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

Discounted:

$$
d\tilde{S}_t = \sigma \tilde{S}_t\,dW_t^{\mathbb{Q}}
$$

**No drift!** The discounted price is a $\mathbb{Q}$-martingale.

### Verification via Novikov

Since $\theta$ is constant:

$$
\mathbb{E}^{\mathbb{P}}\left[\exp\left(\frac{1}{2}\int_0^T \theta^2\,ds\right)\right] = e^{\theta^2 T/2} < \infty
$$

Novikov's condition is satisfied, so the stochastic exponential is a true martingale, and $\mathbb{Q}$ is a valid probability measure equivalent to $\mathbb{P}$.

See [Novikov and Kazamaki Conditions](novikov_kazamaki_conditions.md) for general criteria.

---

## Economic Interpretation

### Two Perspectives on Prices

| Measure | Interpretation | Use |
|---------|----------------|-----|
| $\mathbb{P}$ (Physical) | Real-world probabilities; reflects beliefs and risk preferences | Forecasting, risk management |
| $\mathbb{Q}$ (Risk-Neutral) | Pricing probabilities; reflects no-arbitrage constraints | Derivative pricing |

### What $\mathbb{Q}$ Does NOT Mean

The risk-neutral measure $\mathbb{Q}$ does **not** imply:

- Investors are actually risk-neutral
- Expected returns equal the risk-free rate in reality
- $\mathbb{Q}$-probabilities are "correct" forecasts

### What $\mathbb{Q}$ DOES Mean

The measure $\mathbb{Q}$ encodes the **prices** that prevent arbitrage:

- $\mathbb{Q}$-expectations give arbitrage-free prices
- $\mathbb{Q}$ adjusts probabilities so that fair prices emerge
- $\mathbb{Q}$ is determined by market prices of traded instruments, not by beliefs

---

## Complete vs. Incomplete Markets

### Complete Markets

A market is **complete** if every contingent claim can be replicated by a self-financing strategy.

!!! theorem "Second Fundamental Theorem"
    An arbitrage-free market is **complete** if and only if the ELMM $\mathbb{Q}$ is **unique**.

In complete markets:

- Every derivative has a unique arbitrage-free price
- Hedging is perfect (zero residual risk)
- The Martingale Representation Theorem holds: every martingale is a stochastic integral w.r.t. traded assets

**Example**: Black–Scholes model (one stock driven by one Brownian motion)

### Incomplete Markets

When markets are incomplete:

- **Multiple ELMMs exist**
- Derivative prices lie in an interval $[\underline{V}, \overline{V}]$
- Additional criteria needed to select a price (utility maximization, variance-optimal, minimal entropy)

**Example**: Stochastic volatility models (two sources of randomness—stock and volatility—but only stock is traded)

The connection to the Martingale Representation Theorem: incompleteness means some martingales cannot be represented as integrals w.r.t. traded assets, so perfect hedging is impossible.

See [Martingale Representation Theorem](martingale_representation_theorem.md) for the mathematical details.

---

## Summary: The No-Arbitrage ⟺ Martingale Connection

$$
\boxed{
\text{No Arbitrage (NFLVR)} \iff \exists\, \mathbb{Q} \sim \mathbb{P} : \tilde{S}_t \text{ is a } \mathbb{Q}\text{-local martingale}
}
$$

| Concept | Mathematical Statement |
|---------|----------------------|
| Arbitrage-free | NFLVR holds |
| Risk-neutral measure | ELMM $\mathbb{Q}$ exists |
| Drift removal | $d\tilde{S} = \sigma \tilde{S}\,dW^{\mathbb{Q}}$ (no $dt$ term) |
| Market price of risk | $\theta = (\mu - r)/\sigma$ |
| Complete market | $\mathbb{Q}$ is unique |
| Incomplete market | Multiple $\mathbb{Q}$'s exist |

---

## What Comes Next

!!! note "Subsequent Sections"
    
    - [**Risk-Neutral Valuation Principle**](risk_neutral_valuation_principle.md): How to use $\mathbb{Q}$ for pricing
    - [**Girsanov's Theorem**](../girsanov/girsanov_theorem.md): The technical machinery for measure change
    - [**Novikov & Kazamaki**](novikov_kazamaki_conditions.md): When is the stochastic exponential a true martingale?
    - [**FTAP (Ch5)**](../../ch01/fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md): The complete proof

---

## Exercises

### Exercise 1: Self-Financing Condition

Let $V_t = \phi_t S_t + \psi_t B_t$ be a portfolio value.

(a) Apply the product rule to $d(\phi_t S_t)$ and $d(\psi_t B_t)$, then use the self-financing condition $dV_t = \phi_t\,dS_t + \psi_t\,dB_t$ to show:

$$
S_t\,d\phi_t + B_t\,d\psi_t = 0
$$

(b) Interpret this condition economically: what does it say about rebalancing the portfolio?

### Exercise 2: Discounted Gains Process

Show that for a self-financing strategy, the discounted portfolio value satisfies:

$$
\tilde{V}_t = \tilde{V}_0 + \int_0^t \phi_s\,d\tilde{S}_s
$$

*Hint*: Use Itô's product rule on $\tilde{V}_t = V_t/B_t = V_t \cdot B_t^{-1}$.

### Exercise 3: Supermartingale Argument

Let $G_t$ be a local martingale with $G_t \geq -M$ for some $M > 0$.

(a) Define $H_t = G_t + M$. Show that $H_t$ is a non-negative local martingale.

(b) Use the fact that non-negative local martingales are supermartingales to conclude $\mathbb{E}[H_T] \leq H_0$.

(c) Deduce that $\mathbb{E}[G_T] \leq G_0$.

(d) If additionally $G_T \geq 0$ a.s. and $G_0 = 0$, show that $G_T = 0$ a.s.

### Exercise 4: Market Price of Risk

In the Black–Scholes model with $\mu = 0.10$, $r = 0.02$, $\sigma = 0.20$:

(a) Compute the market price of risk $\theta$.

(b) Write down the Radon–Nikodym derivative $d\mathbb{Q}/d\mathbb{P}|_{\mathcal{F}_T}$ for $T = 1$.

(c) Verify Novikov's condition is satisfied.

(d) Under $\mathbb{Q}$, what is the drift of $S_t$?
