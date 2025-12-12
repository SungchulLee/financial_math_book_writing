# Black-Scholes PDE via Delta Hedging

The Delta Hedging derivation is the most intuitive approach from a practitioner's perspective—it constructs a **risk-free portfolio** through continuous rebalancing and invokes the no-arbitrage principle.

## Setup and Assumptions

We work under the Black-Scholes-Merton framework with the following assumptions:

**Market Model:**
- The stock price $S_t$ follows geometric Brownian motion:
$$dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$$
where $\mu$ is the drift, $\sigma > 0$ is the volatility, and $W_t$ is a standard Brownian motion.

- The risk-free asset (money market account) evolves as:
$$dB_t = r B_t \, dt, \quad B_0 = 1$$
where $r$ is the constant risk-free rate.

**Derivative Contract:**
Consider a European derivative with payoff $\Phi(S_T)$ at maturity $T$. The derivative price at time $t$ is some function $V(t, S_t)$ that we seek to determine.

## Step 1: Apply Itô's Lemma

Since $V = V(t, S)$ is a function of time and the stock price, we apply **Itô's lemma**:

$$dV = \frac{\partial V}{\partial t} dt + \frac{\partial V}{\partial S} dS + \frac{1}{2} \frac{\partial^2 V}{\partial S^2} (dS)^2$$

Substituting $dS = \mu S \, dt + \sigma S \, dW$ and using $(dW)^2 = dt$, $(dt)^2 = 0$, $dt \cdot dW = 0$:

$$(dS)^2 = \sigma^2 S^2 \, dt$$

Therefore:

$$dV = \left( \frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} \right) dt + \sigma S \frac{\partial V}{\partial S} \, dW$$

## Step 2: Construct the Delta-Hedged Portfolio

We construct a **self-financing portfolio** $\Pi_t$ consisting of:
- **Long position**: 1 unit of the derivative (value $V$)
- **Short position**: $\Delta$ units of the stock (value $\Delta S$)

The portfolio value is:
$$\Pi_t = V_t - \Delta S_t$$

The key insight: we choose $\Delta = \frac{\partial V}{\partial S}$ to **eliminate the stochastic term**.

## Step 3: Portfolio Dynamics

The change in portfolio value over an infinitesimal time interval is:

$$d\Pi = dV - \Delta \, dS$$

Substituting our expressions:

$$d\Pi = \left( \frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} \right) dt + \sigma S \frac{\partial V}{\partial S} \, dW - \Delta(\mu S \, dt + \sigma S \, dW)$$

Now **choose** $\Delta = \frac{\partial V}{\partial S}$. The stochastic terms cancel:

$$\sigma S \frac{\partial V}{\partial S} \, dW - \frac{\partial V}{\partial S} \cdot \sigma S \, dW = 0$$

We're left with:

$$d\Pi = \left( \frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - \Delta \mu S \right) dt$$

$$= \left( \frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} \right) dt$$

Notice: **the drift $\mu$ has disappeared!** This is the magic of delta hedging—the portfolio is now **locally risk-free**.

## Step 4: No-Arbitrage Argument

Since $\Pi$ is a **deterministic** (risk-free) portfolio, the no-arbitrage principle requires it must earn the risk-free rate $r$:

$$d\Pi = r \Pi \, dt$$

But we also have:
$$\Pi = V - \Delta S = V - \frac{\partial V}{\partial S} S$$

Therefore:
$$r \Pi \, dt = r\left(V - S\frac{\partial V}{\partial S}\right) dt$$

## Step 5: Derive the PDE

Equating the two expressions for $d\Pi$:

$$\left( \frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} \right) dt = r\left(V - S\frac{\partial V}{\partial S}\right) dt$$

Dividing by $dt$:

$$\boxed{\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0}$$

This is the **Black-Scholes PDE**!

## Terminal Condition

For a European option with payoff $\Phi(S_T)$:
$$V(T, S) = \Phi(S)$$

For example:
- **Call option**: $\Phi(S) = \max(S - K, 0) = (S - K)^+$
- **Put option**: $\Phi(S) = \max(K - S, 0) = (K - S)^+$

## Key Insights

1. **Market completeness**: The stock and bond span all risk, allowing perfect replication of any derivative.

2. **Risk-neutral valuation**: The drift $\mu$ doesn't appear in the PDE—only the volatility $\sigma$ and risk-free rate $r$ matter for pricing.

3. **Dynamic hedging**: The position $\Delta = \frac{\partial V}{\partial S}$ (the "delta") must be **continuously rebalanced** to maintain the hedge.

4. **Self-financing**: The hedging strategy requires no external cash injection—rebalancing is done by trading stock against the money market account.

This derivation reveals why the approach is called "delta hedging"—we hedge away all risk by holding exactly $\Delta$ units of stock per derivative, where $\Delta$ is the derivative's sensitivity to the underlying.

Would you like me to discuss any of the other three derivations (martingale/infinitesimal generator, consumption-based, or change of numeraire)?