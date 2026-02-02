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

**Remark**: In continuous time, the technically correct condition is **NFLVR** (No Free Lunch with Vanishing Risk), which handles limiting arguments. For our purposes, the definition above suffices.

---

## Why Drift Creates Arbitrage Opportunities

Under the physical measure $\mathbb{P}$, the discounted price has drift:
$$
d\tilde{S}_t = \underbrace{(\mu - r)\tilde{S}_t\,dt}_{\text{systematic drift}} + \sigma \tilde{S}_t\,dW_t
$$

### Example: Exploiting Positive Drift

Suppose $\mu > r$ (the stock has higher expected return than the risk-free rate).

**Strategy**: Buy the stock, financed by borrowing at rate $r$.

- Initial: Borrow $S_0$ at rate $r$, buy one share. Net value $V_0 = 0$.
- At time $T$: Own stock worth $S_T$, owe $S_0 e^{rT}$.

The discounted P&L is:
$$
\tilde{V}_T = \tilde{S}_T - \tilde{S}_0 = \int_0^T d\tilde{S}_s = \int_0^T (\mu - r)\tilde{S}_s\,ds + \int_0^T \sigma \tilde{S}_s\,dW_s
$$

The first integral is **positive** (when $\mu > r$), creating systematic expected profit.

This isn't quite arbitrage (there's still randomness), but it shows that drift creates exploitable opportunities. With continuous rebalancing and leverage, these can be amplified.

### The Key Insight

$$
\boxed{
\text{Systematic drift in discounted prices} \longleftrightarrow \text{Potential for arbitrage}
}
$$

To eliminate arbitrage, we need discounted prices to have **no drift**—i.e., to be martingales.

---

## The Martingale Approach to No-Arbitrage

### Core Observation

If the discounted price $\tilde{S}_t$ is a martingale under some measure $\mathbb{Q}$, then for any admissible strategy $\phi$:
$$
G_t(\phi) = \int_0^t \phi_s\,d\tilde{S}_s
$$
is a **local martingale** under $\mathbb{Q}$.

If additionally $G_t(\phi)$ is bounded below (admissibility), then it's a **supermartingale**:
$$
\mathbb{E}^{\mathbb{Q}}[G_T(\phi)] \leq G_0(\phi) = 0
$$

### Why This Rules Out Arbitrage

For an arbitrage, we need $G_T(\phi) \geq 0$ a.s. and $\mathbb{Q}(G_T(\phi) > 0) > 0$.

But if $G_T \geq 0$ and $\mathbb{E}^{\mathbb{Q}}[G_T] \leq 0$, then $G_T = 0$ a.s.

Since $\mathbb{Q}$ is equivalent to $\mathbb{P}$ (same null sets), $G_T = 0$ $\mathbb{P}$-a.s. as well.

**Conclusion**: No arbitrage is possible!

!!! theorem "Martingale Implies No Arbitrage"
    If there exists a probability measure $\mathbb{Q} \sim \mathbb{P}$ such that discounted asset prices are $\mathbb{Q}$-local martingales, then no arbitrage opportunities exist.

---

## Why "Local" Martingale?

In continuous time, discounted prices are typically **local martingales**, not true martingales.

### The Issue

Even under the risk-neutral measure, the gains process:
$$
G_t(\phi) = \int_0^t \phi_s\,d\tilde{S}_s
$$
is only guaranteed to be a local martingale (as an Itô integral with adapted integrand).

### When Does Local Suffice?

For **admissible** strategies (bounded below), local martingales that are bounded below are supermartingales. This is enough to rule out arbitrage.

### When Local Fails

If the discounted price is a **strict local martingale** (local but not true martingale), then:
$$
\mathbb{E}^{\mathbb{Q}}[\tilde{S}_T] < \tilde{S}_0
$$

This corresponds to a **financial bubble**—see [Local Martingales](local_martingale.md) for details.

---

## The Fundamental Theorem of Asset Pricing

The converse is also true: if there's no arbitrage, then a martingale measure must exist.

!!! theorem "Fundamental Theorem of Asset Pricing (FTAP)"
    The following are equivalent:
    
    1. **No arbitrage** (more precisely, NFLVR holds)
    2. **Existence of ELMM**: There exists a probability measure $\mathbb{Q} \sim \mathbb{P}$ such that discounted asset prices are $\mathbb{Q}$-local martingales
    
    The measure $\mathbb{Q}$ is called an **Equivalent Local Martingale Measure (ELMM)**.

**Direction 1** (ELMM $\Rightarrow$ No Arbitrage): Proved above using the supermartingale argument.

**Direction 2** (No Arbitrage $\Rightarrow$ ELMM): This is the hard direction, requiring functional analysis (Hahn-Banach theorem, separating hyperplanes). See [FTAP](../../ch05/fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md) for the full proof.

---

## How Measure Change Removes Arbitrage

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

where $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \int_0^t \frac{\mu_s - r_s}{\sigma_s}\,ds$ is a $\mathbb{Q}$-Brownian motion.

The drift has been **absorbed** into the change of Brownian motion!

### The Market Price of Risk

The quantity:
$$
\theta_t = \frac{\mu_t - r_t}{\sigma_t}
$$

is called the **market price of risk** or **Sharpe ratio**. It measures the excess return per unit of volatility.

Girsanov's theorem says: shifting Brownian motion by $\int \theta\,dt$ removes the drift.

---

## Example: Black-Scholes Model

### Under the Physical Measure $\mathbb{P}$

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}
$$

Discounted:
$$
d\tilde{S}_t = (\mu - r)\tilde{S}_t\,dt + \sigma \tilde{S}_t\,dW_t^{\mathbb{P}}
$$

This has drift $\mu - r \neq 0$ (typically), so arbitrage opportunities may exist.

### Under the Risk-Neutral Measure $\mathbb{Q}$

Define:
$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = \mathcal{E}\left(-\frac{\mu - r}{\sigma}W^{\mathbb{P}}\right)_T = \exp\left(-\frac{\mu-r}{\sigma}W_T^{\mathbb{P}} - \frac{(\mu-r)^2}{2\sigma^2}T\right)
$$

Then $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \frac{\mu - r}{\sigma}t$ is a $\mathbb{Q}$-Brownian motion, and:

$$
dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

Discounted:
$$
d\tilde{S}_t = \sigma \tilde{S}_t\,dW_t^{\mathbb{Q}}
$$

**No drift!** The discounted price is a $\mathbb{Q}$-martingale.

### Verification

Using Novikov's condition (since $\theta = (\mu-r)/\sigma$ is constant):
$$
\mathbb{E}^{\mathbb{P}}\left[\exp\left(\frac{1}{2}\int_0^T \theta^2\,ds\right)\right] = e^{\theta^2 T/2} < \infty
$$

So the stochastic exponential is a true martingale, and $\mathbb{Q}$ is a valid probability measure.

---

## Economic Interpretation

### Two Perspectives on Prices

| Measure | Interpretation | Use |
|---------|----------------|-----|
| $\mathbb{P}$ (Physical) | Real-world probabilities, reflects risk preferences | Forecasting, risk management |
| $\mathbb{Q}$ (Risk-Neutral) | Pricing probabilities, reflects no-arbitrage | Derivative pricing |

### What $\mathbb{Q}$ Does NOT Mean

The risk-neutral measure $\mathbb{Q}$ does **not** imply:

- Investors are actually risk-neutral
- Expected returns equal the risk-free rate in reality
- $\mathbb{Q}$-probabilities are "correct" forecasts

### What $\mathbb{Q}$ DOES Mean

The measure $\mathbb{Q}$ encodes the **prices** that prevent arbitrage:

- $\mathbb{Q}$-expectations give arbitrage-free prices
- $\mathbb{Q}$ adjusts probabilities so that fair prices emerge
- Different from beliefs, $\mathbb{Q}$ is determined by market prices

---

## Complete vs. Incomplete Markets

### Complete Markets

A market is **complete** if every contingent claim can be replicated by a self-financing strategy.

In complete markets:

- The ELMM $\mathbb{Q}$ is **unique**
- Every derivative has a unique arbitrage-free price
- Hedging is perfect

**Example**: Black-Scholes model (one stock, one Brownian motion)

### Incomplete Markets

When markets are incomplete:

- Multiple ELMMs exist
- Derivative prices are not unique (lie in an interval)
- Additional criteria needed to select a price

**Example**: Stochastic volatility models (two sources of randomness, one traded asset)

---

## Summary: The No-Arbitrage ↔ Martingale Connection

$$
\boxed{
\text{No Arbitrage} \iff \exists\, \mathbb{Q} \sim \mathbb{P} : \tilde{S}_t \text{ is a } \mathbb{Q}\text{-local martingale}
}
$$

| Concept | Mathematical Statement |
|---------|----------------------|
| Arbitrage-free | NFLVR holds |
| Risk-neutral measure | ELMM $\mathbb{Q}$ exists |
| Drift removal | $d\tilde{S} = \sigma \tilde{S}\,dW^{\mathbb{Q}}$ |
| Market price of risk | $\theta = (\mu - r)/\sigma$ |
| Complete market | $\mathbb{Q}$ unique |

---

## What Comes Next

!!! note "Subsequent Sections"
    
    - [**Risk-Neutral Valuation Principle**](risk_neutral_valuation_principle.md): How to use $\mathbb{Q}$ for pricing
    - [**Girsanov's Theorem**](../girsanov/girsanov_theorem.md): The technical machinery for measure change
    - [**Novikov & Kazamaki**](novikov_kazamaki_conditions.md): When is the stochastic exponential a true martingale?
    - [**FTAP (Ch5)**](../../ch05/fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md): The complete proof

---

## Exercises

### Exercise 1: Self-Financing Condition

Let $V_t = \phi_t S_t + \psi_t B_t$ be a portfolio value.

(a) Show that the self-financing condition $dV_t = \phi_t\,dS_t + \psi_t\,dB_t$ implies:
$$
d(\phi_t S_t) + d(\psi_t B_t) = \phi_t\,dS_t + \psi_t\,dB_t + S_t\,d\phi_t + B_t\,d\psi_t
$$
and hence $S_t\,d\phi_t + B_t\,d\psi_t = 0$.

(b) Interpret this condition economically.

### Exercise 2: Discounted Gains Process

Show that for a self-financing strategy, the discounted portfolio value satisfies:
$$
\tilde{V}_t = \tilde{V}_0 + \int_0^t \phi_s\,d\tilde{S}_s
$$

*Hint*: Use Itô's product rule on $\tilde{V}_t = V_t/B_t$.

### Exercise 3: Supermartingale Argument

Let $G_t$ be a local martingale with $G_t \geq -M$ for some $M > 0$.

(a) Show that $G_t + M$ is a non-negative local martingale, hence a supermartingale.

(b) Conclude that $\mathbb{E}[G_t] \leq G_0$ for all $t$.

(c) If additionally $G_T \geq 0$ a.s., show that $G_T = 0$ a.s.

### Exercise 4: Market Price of Risk

In the Black-Scholes model with $\mu = 0.10$, $r = 0.02$, $\sigma = 0.20$:

(a) Compute the market price of risk $\theta$.

(b) Write down the Radon-Nikodym derivative $d\mathbb{Q}/d\mathbb{P}|_{\mathcal{F}_T}$ for $T = 1$.

(c) Verify Novikov's condition is satisfied.
