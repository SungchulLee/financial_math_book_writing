# Martingales and No-Arbitrage

In the [unifying framework](../martingale/unifying_principle.md) of this section, no-arbitrage is the **requirement that demands control** — it is the economic reason we must upgrade local martingales to true martingales.

This section develops the deep connection between **no-arbitrage** and **martingale pricing**. The central insight of modern asset pricing theory is that absence of arbitrage is equivalent to the existence of a probability measure under which discounted prices are **local martingales**; upgrading to true martingales is what makes pricing via expectations well-defined.

!!! info "Prerequisites"
    This section assumes familiarity with:
    
    - [Local Martingales](../martingale/local_martingale.md) — the distinction between local and true martingales
    - [Stochastic Exponential](../martingale/stochastic_exponential.md) — the tool for constructing measure changes

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

!!! info "Self-Financing Strategy"
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

!!! info "Admissible Strategy"
    A self-financing strategy $\phi$ is **admissible** if the gains process is bounded below:

    $$
    G_t(\phi) \geq -M \quad \text{for some } M > 0 \text{ and all } t \in [0,T]
    $$
    
    This rules out "doubling strategies" that require unlimited borrowing.

### Formal Definition of Arbitrage

!!! info "Arbitrage Opportunity"
    An **arbitrage opportunity** is an admissible self-financing strategy $\phi$ with:
    
    1. $V_0 = 0$ (zero initial cost)
    2. $V_T \geq 0$ almost surely (no possibility of loss)
    3. $\mathbb{P}(V_T > 0) > 0$ (positive probability of gain)

### NFLVR: The Technically Correct Condition

In continuous time, the naive arbitrage definition above is insufficient. The correct condition is **NFLVR** (No Free Lunch with Vanishing Risk):

!!! info "NFLVR"
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

**Heuristic argument** (full proof via Delbaen-Schachermayer FTAP): Consider a strategy that takes a small position when the drift is favorable and scales it up. In continuous time, one can construct sequences of such strategies where:

- The expected gain remains positive
- The variance of the gain shrinks to zero
- The probability of loss vanishes

This is precisely what NFLVR rules out. The rigorous statement is given by the Fundamental Theorem of Asset Pricing (Delbaen and Schachermayer, 1994), which establishes that NFLVR holds if and only if there exists an equivalent local martingale measure.

### The Key Insight

$$
\boxed{
\text{Drift in discounted prices} \iff \text{Violation of martingale property} \iff \text{Potential for arbitrage}
}
$$

To eliminate arbitrage, discounted prices must be **local martingales under an equivalent measure**. Upgrading to true martingales is what makes expectation-based pricing work — without this upgrade, the pricing formula $V_t = \mathbb{E}^{\mathbb{Q}}[e^{-r(T-t)}\Phi]$ may fail even though no-arbitrage holds.

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

**Step 3**: A **non-negative local martingale is a supermartingale** (see [Local Martingales](../martingale/local_martingale.md)).

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

!!! tip "Martingale Implies No Arbitrage"
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

### When Local Fails: Bubbles (Central Failure Mode)

If the discounted price is a **strict local martingale** (local but not true martingale), then:

$$
\mathbb{E}^{\mathbb{Q}}[\tilde{S}_T] < \tilde{S}_0
$$

This is the **central pathology** of continuous-time finance: the model is arbitrage-free (an ELMM exists), yet expectation-based pricing breaks because the discounted price loses mass. The current price exceeds its expected discounted future payoff — a **financial bubble**. Put-call parity fails, and the risk-neutral valuation formula $V_t = \mathbb{E}^{\mathbb{Q}}[e^{-r(T-t)}\Phi \mid \mathcal{F}_t]$ no longer gives the correct price for claims that depend on the stock level. See [Local Martingales](../martingale/local_martingale.md) for detailed examples and implications.

!!! warning "The gap between no-arbitrage and pricing"
    No-arbitrage (NFLVR) requires only an equivalent **local** martingale measure. Valid expectation-based pricing requires discounted prices to be **true** martingales. These are distinct conditions — a model can satisfy the first while violating the second.

---

## The Fundamental Theorem of Asset Pricing

Recall (see [§ Fundamental Theorem of Asset Pricing](../../ch01/fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md)): NFLVR holds if and only if there exists $\mathbb{Q}\sim\mathbb{P}$ under which discounted asset prices are $\mathbb{Q}$-local martingales (an ELMM). The supermartingale argument above proves the easy direction (ELMM $\Rightarrow$ no arbitrage); the converse requires separating-hyperplane techniques and is covered in ch01.

---

## How Measure Change Removes Drift

A change from $\mathbb{P}$ to $\mathbb{Q}$ leaves the sample paths, trading strategies, and payoffs unchanged; it alters only the probability weights and hence the drift.

Recall (see [§ Drift Adjustment](../girsanov/girsanov_drift_adjustment.md)): with $\theta_t = (\mu_t - r_t)/\sigma_t$ the [market price of risk](market_price_of_risk.md), the Girsanov shift $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \int_0^t \theta_s\,ds$ absorbs $(\mu - r)$ into the change of Brownian motion, yielding a driftless discounted price under $\mathbb{Q}$.

---

Recall (see [§ Black-Scholes Example](examples.md#example-1-black-scholes-model-single-stock)): in the constant-coefficient model, $\theta=(\mu-r)/\sigma$ is constant, Novikov holds trivially, and $\tilde S_t$ becomes a true $\mathbb{Q}$-martingale.

---

## Economic Interpretation

### Two Perspectives on Prices

| Measure | Interpretation | Use |
|---------|----------------|-----|
| $\mathbb{P}$ (Physical) | Real-world probabilities; reflects beliefs and risk preferences | Forecasting, risk management |
| $\mathbb{Q}$ (Risk-Neutral) | Pricing probabilities; reflects no-arbitrage constraints | Derivative pricing |

### What Q Does NOT Mean

The risk-neutral measure $\mathbb{Q}$ does **not** imply:

- Investors are actually risk-neutral
- Expected returns equal the risk-free rate in reality
- $\mathbb{Q}$-probabilities are "correct" forecasts

### What Q DOES Mean

The measure $\mathbb{Q}$ encodes the **prices** that prevent arbitrage:

- $\mathbb{Q}$-expectations give arbitrage-free prices
- $\mathbb{Q}$ adjusts probabilities so that fair prices emerge
- $\mathbb{Q}$ is determined by market prices of traded instruments, not by beliefs

---

## Complete vs. Incomplete Markets

Recall (see [§ Complete Markets and Uniqueness](../../ch01/fundamental_theorem_of_asset_pricing/complete_markets_and_uniqueness.md)): an arbitrage-free market is complete iff the ELMM $\mathbb{Q}$ is unique; completeness is equivalent to the [Martingale Representation Theorem](../martingale/martingale_representation_theorem.md) holding for the traded assets. Incomplete markets (e.g. stochastic volatility — see [§ Heston Example](examples.md#example-4-incomplete-market-stochastic-volatility)) admit a pricing interval $[\underline V, \overline V]$ rather than a unique price.

---

## Summary: Three Levels of No-Arbitrage and Pricing

!!! abstract "FTAP Ladder"

    **Level 1 — Existence (No-Arbitrage):**

    $$
    \text{NFLVR}
    \;\Longleftrightarrow\;
    \exists\, \mathbb{Q} \sim \mathbb{P}
    \text{ such that }
    \tilde{S}_t \text{ is a local martingale}
    $$

    No arbitrage guarantees an Equivalent Local Martingale Measure (ELMM), but does
    not by itself validate expectation-based pricing.

    ---

    **Level 2 — Pricing (Validity):**

    If discounted prices are **true martingales** under $\mathbb{Q}$, then:

    $$
    V_t = \mathbb{E}^{\mathbb{Q}}\!\left[
    e^{-\int_t^T r_s\,ds}\,\Phi_T
    \;\middle|\; \mathcal{F}_t
    \right]
    $$

    Upgrading local martingales to true martingales is what makes pricing work.
    Without this upgrade, bubbles can appear and the formula fails.

    ---

    **Level 3 — Uniqueness (Completeness):**

    $$
    \text{Unique } \mathbb{Q}
    \;\Longleftrightarrow\;
    \text{market is complete}
    $$

    Unique $\mathbb{Q}$ gives a unique price; multiple $\mathbb{Q}$'s give a pricing
    interval.

---

## What Comes Next

!!! note "Subsequent Sections"
    
    - [**Risk-Neutral Valuation Principle**](risk_neutral_valuation_principle.md): How to use $\mathbb{Q}$ for pricing
    - [**Girsanov's Theorem**](../girsanov/girsanov_theorem.md): The technical machinery for measure change
    - [**Novikov & Kazamaki**](../martingale/novikov_kazamaki_conditions.md): When is the stochastic exponential a true martingale?
    - [**FTAP (Ch5)**](../../ch01/fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md): The complete proof

---

## Exercises

**Exercise 1.**
Let $V_t = \phi_t S_t + \psi_t B_t$ be a portfolio value.

(a) Apply the product rule to $d(\phi_t S_t)$ and $d(\psi_t B_t)$, then use the self-financing condition $dV_t = \phi_t\,dS_t + \psi_t\,dB_t$ to show:

$$
S_t\,d\phi_t + B_t\,d\psi_t = 0
$$

(b) Interpret this condition economically: what does it say about rebalancing the portfolio?

??? success "Solution to Exercise 1"
    **(a)** By the product rule:

    $$
    d(\phi_t S_t) = \phi_t\,dS_t + S_t\,d\phi_t + d\phi_t\,dS_t
    $$

    $$
    d(\psi_t B_t) = \psi_t\,dB_t + B_t\,d\psi_t + d\psi_t\,dB_t
    $$

    Since $\phi_t$ and $\psi_t$ are of bounded variation (trading strategies), the cross terms $d\phi_t\,dS_t$ and $d\psi_t\,dB_t$ vanish. Adding:

    $$
    dV_t = \phi_t\,dS_t + S_t\,d\phi_t + \psi_t\,dB_t + B_t\,d\psi_t
    $$

    The self-financing condition states $dV_t = \phi_t\,dS_t + \psi_t\,dB_t$. Subtracting:

    $$
    S_t\,d\phi_t + B_t\,d\psi_t = 0
    $$

    **(b)** This says that any rebalancing of the portfolio must be self-funding: if you buy more stock (increasing $\phi_t$), you must finance it by selling bonds (decreasing $\psi_t$), and vice versa. The total cost of rebalancing at current prices is zero — no external cash is injected or withdrawn.

---

**Exercise 2.**
Show that for a self-financing strategy, the discounted portfolio value satisfies:

$$
\tilde{V}_t = \tilde{V}_0 + \int_0^t \phi_s\,d\tilde{S}_s
$$

*Hint*: Use Itô's product rule on $\tilde{V}_t = V_t/B_t = V_t \cdot B_t^{-1}$.

??? success "Solution to Exercise 2"
    Define $\tilde{V}_t = V_t / B_t = V_t \cdot B_t^{-1}$. By Itô's product rule:

    $$
    d\tilde{V}_t = V_t\,d(B_t^{-1}) + B_t^{-1}\,dV_t + dV_t\,d(B_t^{-1})
    $$

    Since $B_t$ is differentiable (no stochastic term), the cross-variation vanishes: $dV_t\,d(B_t^{-1}) = 0$. Now $d(B_t^{-1}) = -r_t B_t^{-1}\,dt$, and by self-financing $dV_t = \phi_t\,dS_t + \psi_t\,dB_t$. Substituting:

    $$
    d\tilde{V}_t = -r_t V_t B_t^{-1}\,dt + B_t^{-1}(\phi_t\,dS_t + \psi_t\,dB_t)
    $$

    $$
    = -r_t \tilde{V}_t\,dt + \phi_t B_t^{-1}\,dS_t + \psi_t B_t^{-1} r_t B_t\,dt
    $$

    $$
    = -r_t \tilde{V}_t\,dt + \phi_t B_t^{-1}\,dS_t + r_t \psi_t\,dt
    $$

    Since $\tilde{V}_t = \phi_t \tilde{S}_t + \psi_t$, we have $r_t\tilde{V}_t = r_t\phi_t\tilde{S}_t + r_t\psi_t$. Thus:

    $$
    d\tilde{V}_t = -r_t\phi_t\tilde{S}_t\,dt + \phi_t B_t^{-1}\,dS_t
    $$

    Now $d\tilde{S}_t = d(S_t B_t^{-1}) = B_t^{-1}\,dS_t - r_t \tilde{S}_t\,dt$, so $B_t^{-1}\,dS_t = d\tilde{S}_t + r_t\tilde{S}_t\,dt$. Substituting:

    $$
    d\tilde{V}_t = -r_t\phi_t\tilde{S}_t\,dt + \phi_t(d\tilde{S}_t + r_t\tilde{S}_t\,dt) = \phi_t\,d\tilde{S}_t
    $$

    Integrating from $0$ to $t$:

    $$
    \tilde{V}_t = \tilde{V}_0 + \int_0^t \phi_s\,d\tilde{S}_s
    $$

---

**Exercise 3.**
Let $G_t$ be a local martingale with $G_t \geq -M$ for some $M > 0$.

(a) Define $H_t = G_t + M$. Show that $H_t$ is a non-negative local martingale.

(b) Use the fact that non-negative local martingales are supermartingales to conclude $\mathbb{E}[H_T] \leq H_0$.

(c) Deduce that $\mathbb{E}[G_T] \leq G_0$.

(d) If additionally $G_T \geq 0$ a.s. and $G_0 = 0$, show that $G_T = 0$ a.s.

??? success "Solution to Exercise 3"
    **(a)** Since $G_t \geq -M$, we have $H_t = G_t + M \geq 0$. Since $G_t$ is a local martingale with localizing sequence $\{\tau_n\}$, the stopped process $G_{t \wedge \tau_n}$ is a martingale. Then $H_{t \wedge \tau_n} = G_{t \wedge \tau_n} + M$ is also a martingale (adding a constant preserves the martingale property). Hence $H_t$ is a non-negative local martingale.

    **(b)** Since $H_t \geq 0$ is a non-negative local martingale, by Fatou's lemma:

    $$
    \mathbb{E}[H_T] = \mathbb{E}\left[\lim_{n \to \infty} H_{T \wedge \tau_n}\right] \leq \liminf_{n \to \infty} \mathbb{E}[H_{T \wedge \tau_n}] = \liminf_{n \to \infty} H_0 = H_0
    $$

    Therefore $\mathbb{E}[H_T] \leq H_0 = G_0 + M$.

    **(c)** Since $\mathbb{E}[H_T] = \mathbb{E}[G_T + M] = \mathbb{E}[G_T] + M \leq G_0 + M$, we get:

    $$
    \mathbb{E}[G_T] \leq G_0
    $$

    **(d)** If $G_T \geq 0$ a.s. and $G_0 = 0$, then from part (c): $\mathbb{E}[G_T] \leq 0$. But $G_T \geq 0$ a.s. implies $\mathbb{E}[G_T] \geq 0$. Together: $\mathbb{E}[G_T] = 0$. Since $G_T \geq 0$ a.s. and has zero expectation, we conclude $G_T = 0$ almost surely.

---

**Exercise 4.**
A discrete-time market has two periods and a stock that can go up by factor $u = 1.3$ or down by factor $d = 0.8$ each period. The risk-free rate per period is $R = 0.05$.

(a) Compute the risk-neutral probability $q = (1 + R - d)/(u - d)$.

(b) The stock starts at $S_0 = 100$. Compute the discounted stock price $\tilde{S}_t = S_t / (1+R)^t$ at all nodes of the tree.

(c) Verify that $\tilde{S}_t$ is a martingale under $\mathbb{Q}$: check $\mathbb{E}^{\mathbb{Q}}[\tilde{S}_1 \mid S_0] = \tilde{S}_0$ and $\mathbb{E}^{\mathbb{Q}}[\tilde{S}_2 \mid S_1] = \tilde{S}_1$ at each node.

??? success "Solution to Exercise 4"
    **(a)** The risk-neutral probability is

    $$
    q = \frac{1 + R - d}{u - d} = \frac{1.05 - 0.8}{1.3 - 0.8} = \frac{0.25}{0.50} = 0.5
    $$

    **(b)** The stock prices at each node are:

    - $t = 0$: $S_0 = 100$, so $\tilde{S}_0 = 100$.
    - $t = 1$: $S_1^u = 130$, $\tilde{S}_1^u = 130 / 1.05 \approx 123.81$. $S_1^d = 80$, $\tilde{S}_1^d = 80 / 1.05 \approx 76.19$.
    - $t = 2$: $S_2^{uu} = 169$, $\tilde{S}_2^{uu} = 169 / 1.05^2 \approx 153.29$. $S_2^{ud} = 104$, $\tilde{S}_2^{ud} = 104 / 1.1025 \approx 94.33$. $S_2^{dd} = 64$, $\tilde{S}_2^{dd} = 64 / 1.1025 \approx 58.05$.

    **(c)** At $t = 0$:

    $$
    \mathbb{E}^{\mathbb{Q}}[\tilde{S}_1] = q \cdot \tilde{S}_1^u + (1-q) \cdot \tilde{S}_1^d = 0.5 \times \frac{130}{1.05} + 0.5 \times \frac{80}{1.05} = \frac{0.5 \times 210}{1.05} = \frac{105}{1.05} = 100 = \tilde{S}_0 \;\checkmark
    $$

    At $t = 1$, node $u$:

    $$
    \mathbb{E}^{\mathbb{Q}}[\tilde{S}_2 \mid S_1 = 130] = 0.5 \times \frac{169}{1.1025} + 0.5 \times \frac{104}{1.1025} = \frac{0.5 \times 273}{1.1025} = \frac{136.5}{1.1025} = \frac{130}{1.05} = \tilde{S}_1^u \;\checkmark
    $$

    At $t = 1$, node $d$:

    $$
    \mathbb{E}^{\mathbb{Q}}[\tilde{S}_2 \mid S_1 = 80] = 0.5 \times \frac{104}{1.1025} + 0.5 \times \frac{64}{1.1025} = \frac{0.5 \times 168}{1.1025} = \frac{84}{1.1025} = \frac{80}{1.05} = \tilde{S}_1^d \;\checkmark
    $$

    The discounted stock price is a $\mathbb{Q}$-martingale at every node.

---

**Exercise 5.**
Consider a market with one traded stock driven by two independent Brownian motions:

$$
dS_t = \mu S_t\,dt + \sigma_1 S_t\,dW_t^1 + \sigma_2 S_t\,dW_t^2
$$

with risk-free rate $r$.

(a) Write the risk premium equation $\mu - r = \sigma_1\theta_1 + \sigma_2\theta_2$ and explain why it defines a line in $(\theta_1, \theta_2)$ space.

(b) Is this market complete or incomplete? Justify by counting assets and sources of risk.

(c) Pick two specific points on the line from (a) and explain why they define two different equivalent martingale measures, each producing a different price for a claim $\Phi(W_T^2)$ that depends only on the second Brownian motion.

??? success "Solution to Exercise 5"
    **(a)** Under $\mathbb{Q}^{\boldsymbol{\theta}}$, the discounted stock must have zero drift. The Girsanov shift $W_t^{i,\mathbb{Q}} = W_t^{i,\mathbb{P}} + \theta_i t$ removes the drift when

    $$
    \mu - r = \sigma_1\theta_1 + \sigma_2\theta_2
    $$

    This is one linear equation in two unknowns $(\theta_1, \theta_2)$, so the solution set is a line in $\mathbb{R}^2$ (an affine subspace of dimension 1).

    **(b)** The market is **incomplete**: there is one traded risky asset but two independent sources of randomness ($d = 2 > n = 1$). The volatility matrix $\Sigma = (\sigma_1, \sigma_2)$ is $1 \times 2$ with rank 1, so the system $\mu - r = \Sigma\boldsymbol{\theta}$ is underdetermined. By the Second Fundamental Theorem, the equivalent martingale measure is not unique, confirming incompleteness.

    **(c)** Choose $\theta_1 = 0$, giving $\theta_2 = (\mu - r)/\sigma_2$. Alternatively, choose $\theta_2 = 0$, giving $\theta_1 = (\mu - r)/\sigma_1$. Both satisfy the risk premium equation, so both define valid ELMMs.

    For a claim $\Phi(W_T^2)$: under the first measure ($\theta_1 = 0$, $\theta_2 = (\mu-r)/\sigma_2$), the risk-neutral $W^{2,\mathbb{Q}}$ has a nontrivial Girsanov shift, so $W_T^{2,\mathbb{P}} = W_T^{2,\mathbb{Q}} - \theta_2 T$ and the price depends on $\theta_2$. Under the second measure ($\theta_1 = (\mu-r)/\sigma_1$, $\theta_2 = 0$), the second Brownian motion is unchanged: $W^{2,\mathbb{Q}} = W^{2,\mathbb{P}}$, and the claim is priced using the original distribution of $W_T^2$.

    These two prices differ because $\Phi(W_T^2)$ has exposure to the non-traded factor $W^2$, and each ELMM reweights this factor differently. This is the pricing ambiguity inherent in incomplete markets.

---

**Exercise 6.**
Explain why the admissibility condition $G_t(\phi) \geq -M$ is necessary to rule out arbitrage. Consider the following "doubling strategy" in discrete time: at each step $k$, bet $2^k$ on a fair coin flip. If you win, stop. If you lose, double the bet.

(a) Show that this strategy has zero initial cost, always eventually wins, and produces a guaranteed profit of 1 unit.

(b) Explain why the gains process $G_t$ of this strategy is unbounded below.

(c) Relate this to the admissibility requirement in continuous time: why does the supermartingale argument from the text fail without a lower bound on $G_t$?

??? success "Solution to Exercise 6"
    **(a)** At step $k$, the bet is $2^k$ on a fair coin. If the first win occurs at step $n$, the cumulative losses from steps $0, \ldots, n-1$ are $1 + 2 + \cdots + 2^{n-1} = 2^n - 1$. The win at step $n$ pays $2^n$. Net profit: $2^n - (2^n - 1) = 1$. Since the coin is fair and independent, the probability of never winning is $\lim_{n \to \infty} (1/2)^n = 0$. The strategy eventually wins with probability 1, costing nothing to enter and guaranteeing a profit of 1. This is an apparent arbitrage.

    **(b)** Before winning, the cumulative loss after $n$ steps is $-(2^n - 1)$. This is unbounded: $G_n \leq -(2^n - 1) \to -\infty$ as $n \to \infty$. There is no finite $M$ such that $G_t \geq -M$ for all $t$. The strategy requires the ability to borrow arbitrary amounts.

    **(c)** The supermartingale argument in the text proceeds as follows: if $G_t \geq -M$, then $H_t = G_t + M \geq 0$ is a non-negative local martingale, hence a supermartingale, and $\mathbb{E}[G_T] \leq 0$. This rules out $G_T \geq 0$ with $\mathbb{P}(G_T > 0) > 0$.

    Without admissibility, we cannot form the non-negative process $H_t$. The gains process $G_t$ is a local martingale (under the fair-coin measure), but since it is not bounded below, it is not a supermartingale: $\mathbb{E}[G_T]$ may not be $\leq 0$, and in fact the strategy achieves $G_T = 1$ a.s. The supermartingale inequality fails precisely because the unbounded losses allow probability mass to leak through the negative tail, circumventing the no-arbitrage conclusion. Admissibility is therefore not a technical nicety but an economic necessity: it restricts attention to strategies with bounded credit exposure.

---

**Exercise 7.**
You cannot find any single arbitrage strategy, but you construct a sequence of strategies $\{\phi^n\}$ such that $V_0^n = 0$, $V_T^n \geq -1/n$, and $V_T^n \to f \geq 0$ in probability with $\mathbb{P}(f > 0) > 0$. Is the market arbitrage-free?

??? success "Solution to Exercise 7"
    No. This is precisely a violation of **NFLVR** (No Free Lunch with Vanishing Risk).

    The condition for NFLVR is that no such sequence exists: there should be no sequence of admissible strategies whose terminal values converge to a non-negative, non-trivially positive payoff while the lower bounds on intermediate losses vanish. The individual strategies are not arbitrage (each has $V_T^n \geq -1/n$, not $\geq 0$), but the limiting payoff is.

    By the Fundamental Theorem of Asset Pricing, NFLVR holds if and only if an equivalent local martingale measure exists. Since NFLVR is violated here, no ELMM exists, and the market admits arbitrage in the generalized sense — even though no single strategy is a classical arbitrage.

    This distinction between pointwise arbitrage and limiting arbitrage is why the FTAP uses NFLVR rather than the naive definition. Interviewers test this because candidates who use only the naive definition miss exactly this kind of failure.

---

**Exercise 8.**
Two quants price the same exotic derivative in an incomplete market. One gets \$12 and the other gets \$15. Both claim their prices are arbitrage-free. Is one of them wrong?

??? success "Solution to Exercise 8"
    Not necessarily — both can be correct.

    In an incomplete market, the equivalent martingale measure $\mathbb{Q}$ is **not unique**. Different choices of $\mathbb{Q}$ (corresponding to different specifications of the unhedgeable risk premium) lead to different but equally valid arbitrage-free prices. The set of all such prices forms an interval $[V_{\min}, V_{\max}]$, and any price in this interval is consistent with no-arbitrage.

    If both \$12 and \$15 lie within this interval, both are valid. Neither quant is "wrong" — they are implicitly using different equivalent martingale measures, which correspond to different risk preferences or calibration choices for the unspanned risk factors.

    The price becomes unique only when the market is **complete** (Second Fundamental Theorem), i.e., when there is a unique ELMM. In incomplete markets, arbitrage-free pricing alone does not pin down a single price — additional criteria (utility maximization, minimal entropy, variance-optimal hedging) are needed to select among the valid measures.

---

**Exercise 9.**
Suppose the discounted price process $\tilde{S}_t$ is a strict local martingale under $\mathbb{Q}$ with $\mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] = 0.95\,S_0$. Compute the bubble component $\beta_0$. Then, using the modified put-call parity $C - P = \mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] - Ke^{-rT}$, show that the classical put-call parity fails and determine the sign of the error.

??? success "Solution to Exercise 9"
    The **bubble component** is:

    $$
    \beta_0 = S_0 - \mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] = S_0 - 0.95\,S_0 = 0.05\,S_0
    $$

    So 5% of the current price is due to the bubble.

    For put-call parity, in the standard (true martingale) case:

    $$
    C - P = S_0 - Ke^{-rT}
    $$

    Under the strict local martingale setting, the modified put-call parity is:

    $$
    C - P = \mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] - Ke^{-rT} = 0.95\,S_0 - Ke^{-rT}
    $$

    Comparing with the classical formula:

    $$
    (C - P)_{\text{classical}} - (C - P)_{\text{actual}} = S_0 - 0.95\,S_0 = 0.05\,S_0 = \beta_0 > 0
    $$

    The classical put-call parity **overestimates** $C - P$ by the bubble component $\beta_0 = 0.05\,S_0$. Equivalently, the put price is higher than what classical parity would predict (it includes a "bubble premium"), while the call price is lower. The error is positive: $S_0 - Ke^{-rT} > C - P$.
