# Black–Scholes PDE via Equilibrium Pricing


The Black–Scholes PDE can be derived as a consequence of **general equilibrium** in a representative-agent economy, without any direct no-arbitrage or hedging argument. In this approach, the pricing equation emerges from the optimal consumption–investment behavior of an agent with CRRA preferences, combined with market clearing. The key equilibrium output is the **stochastic discount factor** (pricing kernel), which determines the relationship between the stock's physical drift $\mu$, the risk-free rate $r$, and the risk aversion parameter $\gamma$—and once this relationship is imposed, the Black–Scholes PDE follows.

This derivation is fundamentally different from the [delta-hedging](delta_hedging.md) and [change-of-numéraire](change_of_numeraire.md) approaches because it **explains** the risk-free rate and the equity risk premium as endogenous quantities, rather than taking them as given.


## The Representative-Agent Economy


A representative agent maximizes expected lifetime utility over consumption:

$$\max_{(C_t, \pi_t)} \; \mathbb{E}\!\left[\int_0^\infty e^{-\rho t}\, U(C_t)\, dt\right]$$

with CRRA utility $U(C) = C^{1-\gamma}/(1-\gamma)$ for $\gamma > 0$, $\gamma \neq 1$ (where $\gamma$ is the coefficient of relative risk aversion and $\rho > 0$ is the rate of time preference).

The agent allocates wealth $W_t$ between a risky stock ($dS_t = \mu S_t\, dt + \sigma S_t\, dW_t$) and a risk-free bond ($dB_t = rB_t\, dt$). If $\pi_t$ is the fraction invested in stock, the wealth dynamics are

$$dW_t = \bigl[rW_t + \pi_t W_t(\mu - r) - C_t\bigr]\, dt + \pi_t W_t \sigma\, dW_t$$

The solution to this stochastic control problem (Merton, 1969, 1971) gives the optimal portfolio allocation and consumption rate:

$$\pi^* = \frac{\mu - r}{\gamma \sigma^2}, \qquad C^* = \alpha\, W$$

where $\alpha > 0$ is a constant determined by the model primitives $(\rho, \gamma, r, \mu, \sigma)$. The portfolio rule $\pi^*$ is the **Merton rule**: the optimal risky-asset share is the Sharpe ratio divided by the product of risk aversion and volatility.


## Market Clearing and the Equilibrium Risk Premium


In a Lucas (1978) endowment economy, the stock represents the agent's entire productive wealth, and the bond is in **zero net supply**. Market clearing therefore requires the representative agent to hold all wealth in the stock:

$$\pi^* = 1$$

Substituting into the Merton rule:

$$1 = \frac{\mu - r}{\gamma \sigma^2} \qquad \Longrightarrow \qquad \boxed{\mu - r = \gamma \sigma^2}$$

This is the **equilibrium risk premium**: the stock's expected excess return equals risk aversion times the variance of returns. It is the continuous-time version of the consumption CAPM—in this economy where consumption growth is perfectly correlated with stock returns, the risk premium is proportional to risk aversion times the covariance of consumption growth with the stock return.

This equation is the central output of the equilibrium and will be the bridge from the "physical-drift" pricing kernel to the Black–Scholes PDE.


## The Stochastic Discount Factor


In equilibrium, any asset with price process $P_t$ must satisfy the **Euler equation**: the process $M_t P_t$ is a martingale, where the **stochastic discount factor** (SDF) is

$$M_t = e^{-\rho t}\, U'(C^*_t) = e^{-\rho t}\, (C^*_t)^{-\gamma}$$

Since market clearing gives $C^*_t \propto W_t = S_t$, we have (up to a positive constant that cancels in pricing ratios)

$$M_t = e^{-\rho t}\, S_t^{-\gamma}$$

### Dynamics of $M_t$

Apply Itô's formula to $S_t^{-\gamma}$ with $f(S) = S^{-\gamma}$:

$$d(S_t^{-\gamma}) = -\gamma S_t^{-\gamma-1}\, dS_t + \frac{1}{2}\gamma(\gamma + 1)\, S_t^{-\gamma-2}\, (dS_t)^2$$

$$= S_t^{-\gamma}\!\left[\bigl(-\gamma\mu + \tfrac{1}{2}\gamma(\gamma+1)\sigma^2\bigr)\, dt - \gamma\sigma\, dW_t\right]$$

Since $e^{-\rho t}$ has zero quadratic variation, the product rule gives

$$\frac{dM_t}{M_t} = -\underbrace{\bigl[\rho + \gamma\mu - \tfrac{1}{2}\gamma(\gamma+1)\sigma^2\bigr]}_{\displaystyle =:\, \kappa}\, dt - \gamma\sigma\, dW_t$$

### Equilibrium Risk-Free Rate

The bond price $B_t = e^{rt}$ must satisfy the martingale condition: $M_t B_t$ is a martingale, so $d(M_t B_t)$ has zero drift. Since $dB_t = rB_t\, dt$ (zero quadratic variation), the drift of $M_t B_t$ is

$$M_t B_t(-\kappa + r)\, dt = 0$$

Therefore

$$\boxed{r = \kappa = \rho + \gamma\mu - \tfrac{1}{2}\gamma(\gamma+1)\sigma^2}$$

This is the **equilibrium risk-free rate**. It increases with impatience ($\rho$) and expected consumption growth (which in this model has drift $\mu - \frac{1}{2}\sigma^2$ for $\ln S$), but decreases with consumption volatility through the precautionary savings term $-\frac{1}{2}\gamma(\gamma+1)\sigma^2$.


## Deriving the Black–Scholes PDE


Let $V(t, S)$ be the price of a European derivative with payoff $\Phi(S_T)$ at maturity $T$. The equilibrium pricing condition requires that $M_t\, V(t, S_t)$ is a martingale.

### Itô Expansion of $d(M_t V_t)$

By Itô's formula applied to $V(t, S_t)$:

$$dV = \left(\frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right) dt + \sigma S \frac{\partial V}{\partial S}\, dW$$

The product rule gives

$$d(M_t V_t) = M_t\, dV_t + V_t\, dM_t + dM_t\, dV_t$$

The cross-variation term is

$$dM_t\, dV_t = (-\gamma\sigma M_t)\!\left(\sigma S \frac{\partial V}{\partial S}\right) dt = -\gamma\sigma^2 S\, M_t \frac{\partial V}{\partial S}\, dt$$

### Zero-Drift Condition

Collecting the drift of $d(M_t V_t)$ and dividing by $M_t$:

$$\frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - \kappa V - \gamma\sigma^2 S \frac{\partial V}{\partial S} = 0$$

Grouping the first-order term:

$$\frac{\partial V}{\partial t} + (\mu - \gamma\sigma^2) S \frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0$$

where we used $\kappa = r$. The coefficient of $S\, \partial V / \partial S$ is $\mu - \gamma\sigma^2$. But the equilibrium risk premium gives $\mu - \gamma\sigma^2 = r$. Substituting:

$$\boxed{\frac{\partial V}{\partial t} + rS \frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0}$$

with terminal condition $V(T, S) = \Phi(S)$. This is the **Black–Scholes PDE**.

The equilibrium risk premium $\mu - r = \gamma\sigma^2$ plays the same role here as the Girsanov drift removal in the risk-neutral approach: it converts the physical drift $\mu$ into the risk-neutral drift $r$. But whereas the no-arbitrage derivation treats this as a consequence of the absence of arbitrage, the equilibrium derivation **explains** it as a consequence of optimal consumption–investment behavior and market clearing.


## What the Equilibrium Approach Adds


The equilibrium derivation yields three results that the no-arbitrage approach cannot provide:

**Endogenous risk-free rate.** The no-arbitrage derivation takes $r$ as an exogenous parameter. Here, $r = \rho + \gamma\mu - \frac{1}{2}\gamma(\gamma+1)\sigma^2$ is determined by preferences and the investment opportunity set.

**Endogenous risk premium.** The equity premium $\mu - r = \gamma\sigma^2$ is derived from market clearing, not assumed. The parameter $\gamma$ connects preferences to risk premia—this is the consumption CAPM in continuous time.

**Connection to the equity premium puzzle.** Empirically, $\mu - r \approx 6\%$ and $\sigma \approx 16\%$ for the US equity market, which implies $\gamma \approx 6\%/0.0256 \approx 234$—an implausibly high level of risk aversion. This discrepancy, identified by Mehra and Prescott (1985), shows that the simple representative-agent model with CRRA utility cannot simultaneously explain the level of equity returns and the low risk-free rate, motivating extensions to habit formation, recursive utility, rare disasters, and heterogeneous-agent models.


## Summary


The logical chain is:

1. **Agent optimization** (Merton problem): yields the optimal portfolio rule $\pi^* = (\mu - r)/(\gamma\sigma^2)$ and the pricing kernel $M_t = e^{-\rho t} S_t^{-\gamma}$.
2. **Market clearing** ($\pi^* = 1$): implies the equilibrium risk premium $\mu - r = \gamma\sigma^2$ and the equilibrium risk-free rate $r = \rho + \gamma\mu - \frac{1}{2}\gamma(\gamma+1)\sigma^2$.
3. **Martingale condition** ($M_t V_t$ is a martingale): yields a PDE with drift coefficient $\mu - \gamma\sigma^2$.
4. **Equilibrium substitution** ($\mu - \gamma\sigma^2 = r$): recovers the Black–Scholes PDE.

The Black–Scholes PDE is thus not merely a no-arbitrage condition—it is a **general equilibrium outcome** in which preferences, technology, and market clearing jointly determine asset prices.


## References

- Merton, R. C. (1969). *Lifetime portfolio selection under uncertainty: The continuous-time case.* Review of Economics and Statistics, 51(3), 247–257.

- Merton, R. C. (1971). *Optimum consumption and portfolio rules in a continuous-time model.* Journal of Economic Theory, 3(4), 373–413.

- Lucas, R. E. (1978). *Asset prices in an exchange economy.* Econometrica, 46(6), 1429–1445.

- Mehra, R. and Prescott, E. C. (1985). *The equity premium: A puzzle.* Journal of Monetary Economics, 15(2), 145–161.

- Cochrane, J. H. (2005). *Asset Pricing.* Revised edition, Princeton University Press.

- Björk, T. (2009). *Arbitrage Theory in Continuous Time.* 3rd edition, Oxford University Press.
