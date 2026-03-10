# Black–Scholes PDE via Delta Hedging



!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The delta-hedging derivation obtains the Black–Scholes PDE by constructing a portfolio of the derivative and the underlying stock, choosing the hedge ratio to eliminate stochastic risk, and invoking the no-arbitrage principle. This is the original approach of Black and Scholes (1973), and remains the most direct route from market assumptions to the pricing equation.


## Setup


**Stock price.** The stock follows geometric Brownian motion under the physical measure:

$$dS_t = \mu S_t\, dt + \sigma S_t\, dW_t$$

with constant drift $\mu$, volatility $\sigma > 0$, and standard Brownian motion $W_t$.

**Risk-free asset.** A money market account grows at constant rate $r$:

$$dB_t = rB_t\, dt, \qquad B_0 = 1$$

**Derivative.** A European derivative with payoff $\Phi(S_T)$ at maturity $T$ has price $V(t, S)$ at time $t$ when the stock price is $S$. We assume $V \in C^{1,2}([0,T) \times (0,\infty))$.


## Step 1: Dynamics of the Derivative Price


Apply Itô's formula to $V(t, S_t)$:

$$dV = \frac{\partial V}{\partial t}\, dt + \frac{\partial V}{\partial S}\, dS + \frac{1}{2}\frac{\partial^2 V}{\partial S^2}\,(dS)^2$$

The quadratic variation is $(dS)^2 = \sigma^2 S^2\, dt$ (using the Itô rules $(dt)^2 = 0$, $dt\, dW = 0$, $(dW)^2 = dt$). Substituting $dS = \mu S\, dt + \sigma S\, dW$:

$$dV = \left(\frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right) dt + \sigma S \frac{\partial V}{\partial S}\, dW$$


## Step 2: The Hedging Portfolio


Construct a portfolio consisting of one unit of the derivative and a short position of $\Delta$ shares of stock:

$$\Pi_t = V_t - \Delta\, S_t$$

Over an infinitesimal interval $[t, t + dt]$, hold $\Delta$ **fixed** (it will be rebalanced at $t + dt$). The change in portfolio value is

$$d\Pi = dV - \Delta\, dS$$

This implicitly assumes that any cash required to rebalance the hedge is borrowed or lent at the risk-free rate $r$. The precise relationship between this "freeze-and-rebalance" construction and the self-financing formulation is discussed in the section [On Self-Financing and Rebalancing](#on-self-financing-and-rebalancing) below.

Substituting the expressions for $dV$ and $dS$:

$$d\Pi = \left(\frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - \Delta \mu S\right) dt + \left(\sigma S \frac{\partial V}{\partial S} - \Delta \sigma S\right) dW$$


## Step 3: Choose Δ to Eliminate Risk


Set the coefficient of $dW$ to zero:

$$\Delta = \frac{\partial V}{\partial S}$$

This is the **delta** of the derivative. With this choice, the stochastic term vanishes and the portfolio becomes locally deterministic:

$$d\Pi = \left(\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right) dt$$

The drift $\mu$ has cancelled. The portfolio's instantaneous return depends only on the theta $\partial V/\partial t$ (time decay) and the gamma $\partial^2 V/\partial S^2$ (convexity of the price function), not on the stock's expected return.


## Step 4: No-Arbitrage Condition


A portfolio with no stochastic risk must earn the risk-free rate, else there is an arbitrage opportunity. Therefore

$$d\Pi = r\Pi\, dt$$

Substituting $\Pi = V - \frac{\partial V}{\partial S}\, S$:

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} = r\!\left(V - S\frac{\partial V}{\partial S}\right)$$

Rearranging:

$$\boxed{\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0}$$

This is the **Black–Scholes PDE**, subject to the terminal condition $V(T, S) = \Phi(S)$.


## Why the Drift μ Disappears


The absence of $\mu$ from the PDE is the central economic insight of the derivation. The hedging portfolio eliminates all exposure to the stock's random fluctuations, so the stock's expected return becomes irrelevant—only the volatility (which determines the magnitude of fluctuations, and hence the cost of hedging) and the risk-free rate (which determines the opportunity cost) enter the equation.

This means investors with different views on the stock's future return all agree on the option price, provided they agree on the volatility. It is also the reason the PDE can be solved without specifying the physical drift, and why the solution coincides with the expectation under the risk-neutral measure.


## Extension: Continuous Dividend Yield


### Why a Continuous Yield?

Real dividends are discrete cash payments on scheduled dates. For a single stock, modeling dividends as a continuous yield is a crude approximation: a company like Apple might pay quarterly dividends of known (or forecastable) size, and an option expiring between two ex-dividend dates sees at most one or two discrete jumps in the stock price. In practice, single-stock option pricing often handles dividends explicitly—either by adjusting the stock price downward at each ex-dividend date or by using a tree/PDE with discrete dividend nodes.

The continuous dividend yield $q$ becomes a genuinely natural model for **broad equity indices and ETFs**. An index such as the S&P 500 comprises hundreds of constituent stocks, each paying dividends on its own schedule. At the index level, dividends arrive on nearly every business day, and the aggregate flow is smooth enough to be well approximated by a constant yield. For example, if the S&P 500 has a trailing dividend yield of roughly 1.5% per annum, setting $q = 0.015$ captures the steady leakage of value from the index level to the dividend stream. The same logic applies to ETFs that track such indices (e.g., SPY, IVV), since their prices reflect the cum-dividend index value minus the accumulated distributions.

Beyond equity indices, the continuous-yield framework applies directly to two other important asset classes:

- **Foreign exchange options.** Holding a foreign currency earns interest at the foreign risk-free rate $r_f$. This is economically identical to a continuous dividend yield $q = r_f$, and leads to the Garman–Kohlhagen formula.

- **Futures and forwards.** An option on a futures contract can be priced by setting $q = r$ (the cost of carry is zero for a futures position), recovering the Black (1976) model.

The continuous dividend yield is therefore best understood not as a literal description of how any single stock pays dividends, but as an effective parameter for assets whose cash flows are frequent enough to be treated as a smooth rate.


### Derivation

When the stock pays a continuous dividend yield $q$, two modifications are needed.

**Modified stock dynamics.** The stock price appreciates at rate $\mu - q$ (dividends reduce the capital gain):

$$dS_t = (\mu - q)S_t\, dt + \sigma S_t\, dW_t$$

**Modified portfolio dynamics.** The portfolio $\Pi = V - \Delta S$ now incurs an additional cost: being short $\Delta$ shares requires paying dividends to the lender at rate $q \Delta S$. The total change in portfolio value over $[t, t+dt]$ is

$$d\Pi = dV - \Delta\, dS - q\Delta S\, dt$$

Apply Itô's formula with the modified stock dynamics and set $\Delta = \partial V / \partial S$ to cancel the stochastic term:

$$d\Pi = \left(\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - qS\frac{\partial V}{\partial S}\right) dt$$

The no-arbitrage condition $d\Pi = r\Pi\, dt$ then gives

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - qS\frac{\partial V}{\partial S} = rV - rS\frac{\partial V}{\partial S}$$

Rearranging:

$$\boxed{\frac{\partial V}{\partial t} + (r - q)S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0}$$

The dividend yield replaces $r$ by $r - q$ in the first-order (drift) term, while the discounting term $-rV$ is unchanged.


### Discrete vs. Continuous: When the Approximation Breaks Down

For individual stock options, especially short-dated ones near an ex-dividend date, the continuous-yield approximation can introduce meaningful pricing errors. A discrete dividend of size $D$ causes the stock price to drop by approximately $D$ on the ex-date, which creates a discontinuity that a smooth yield $q$ cannot capture. The effect is most pronounced for deep in-the-money calls (where early exercise to capture the dividend may be optimal for American options) and for short maturities (where a single dividend constitutes a large fraction of the total expected yield).

In practice, the most common approaches for individual stock options are:

- **Escrowed dividend model**: subtract the present value of known dividends from the current stock price, then apply the Black–Scholes formula to the adjusted price.
- **Piecewise constant yield**: use different effective yields for different periods between ex-dates.
- **Tree or finite-difference methods** with explicit dividend nodes that impose the price drop at each ex-date.

The continuous dividend yield $q$ should therefore be viewed as exact for the idealized case of a truly continuous cash flow (foreign interest, index dividends in aggregate) and as a convenient but approximate device for individual equities.


## On Self-Financing and Rebalancing

The derivation holds $\Delta$ fixed over each infinitesimal interval $[t, t+dt]$ and then rebalances. This is not the same as a self-financing portfolio in the strict sense of stochastic calculus, where the portfolio weights change continuously and the wealth process satisfies $d\Pi = \Delta^V\, dV + \Delta^S\, dS$ with no external cash flows. The two formulations are equivalent in the continuous-time limit, but the distinction matters conceptually: the delta-hedging argument is a "freeze-and-rebalance" construction that avoids the machinery of self-financing strategies, which is part of its appeal as a direct, intuitive derivation.

In the rigorous formulation, one constructs a self-financing strategy $(\alpha_t, \beta_t)$ in the stock and bond that replicates the derivative payoff. The replication condition $\alpha_T S_T + \beta_T B_T = \Phi(S_T)$ a.s., combined with the self-financing constraint, leads to the same PDE. This is the approach taken in the [FTAP framework](../../ch01/fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md).


## Summary


The derivation proceeds in three steps:

1. **Itô's formula** gives the dynamics of $V(t, S_t)$, decomposed into drift and diffusion.
2. **Portfolio construction and delta choice**: forming $\Pi = V - \frac{\partial V}{\partial S}\, S$ and choosing $\Delta = V_S$ simultaneously eliminates the $dW$ term and cancels the physical drift $\mu$—two consequences of a single choice.
3. **No-arbitrage**: the resulting deterministic portfolio must earn rate $r$, yielding the PDE.

The Black–Scholes PDE with terminal condition $V(T, S) = \Phi(S)$ is a **backward parabolic equation**: it is solved from $t = T$ back to $t = 0$.

For alternative derivations that arrive at the same PDE via different reasoning, see [Black–Scholes PDE via Change of Numéraire](change_of_numeraire.md) (martingale condition on $V/S$) and [Risk-Neutral Pricing](../../ch01/fundamental_theorem_of_asset_pricing/numeraire_and_change_of_measure.md) (Feynman–Kac representation under the equivalent martingale measure).


## References

- Black, F. (1976). *The pricing of commodity contracts.* Journal of Financial Economics, 3(1–2), 167–179.

- Black, F. and Scholes, M. (1973). *The pricing of options and corporate liabilities.* Journal of Political Economy, 81(3), 637–654.

- Merton, R. C. (1973). *Theory of rational option pricing.* Bell Journal of Economics and Management Science, 4(1), 141–183.

- Shreve, S. E. (2004). *Stochastic Calculus for Finance II: Continuous-Time Models.* Springer.

- Björk, T. (2009). *Arbitrage Theory in Continuous Time.* 3rd edition, Oxford University Press.
