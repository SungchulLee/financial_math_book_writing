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

### Dynamics of M_t

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

### Itô Expansion of d(M_t V_t)

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

---

## Exercises

**Exercise 1.** In the representative-agent economy with CRRA utility $U(C) = C^{1-\gamma}/(1-\gamma)$, derive the optimal portfolio weight $\pi^* = (\mu - r)/(\gamma\sigma^2)$ by solving the first-order condition of the Merton problem. Verify that market clearing ($\pi^* = 1$) implies the equilibrium risk premium $\mu - r = \gamma\sigma^2$.

---

**Exercise 2.** Using the equilibrium condition $\mu - r = \gamma\sigma^2$ and the equity premium puzzle numbers ($\mu - r \approx 6\%$, $\sigma \approx 16\%$), compute the implied risk aversion parameter $\gamma$. Explain why this value is considered implausibly high and name one model extension that attempts to resolve this puzzle.

---

**Exercise 3.** The pricing kernel in the equilibrium model is $M_t = e^{-\rho t} S_t^{-\gamma}$. Show that the condition for $M_t V(t, S_t)$ to be a $\mathbb{P}$-martingale, combined with the equilibrium substitution $\mu - \gamma\sigma^2 = r$, yields the Black-Scholes PDE.

---

**Exercise 4.** Compare the equilibrium derivation with the delta-hedging derivation. The equilibrium approach "explains" $r$ and $\mu - r$ as endogenous quantities, while delta hedging takes them as given. Describe the advantages and limitations of each perspective for a practitioner pricing options.

---

**Exercise 5.** In the CRRA equilibrium, the risk-free rate is $r = \rho + \gamma\mu - \frac{1}{2}\gamma(\gamma+1)\sigma^2$. For $\gamma = 2$, $\mu = 0.10$, $\sigma = 0.20$, and $\rho = 0.03$, compute the equilibrium $r$ and the equity risk premium $\mu - r$. Verify that the Black-Scholes PDE holds with these values.

---

## Solutions

??? success "Solution to Exercise 1"
    The representative agent solves the Merton problem: maximize $\mathbb{E}\!\left[\int_0^\infty e^{-\rho t}\, \frac{C_t^{1-\gamma}}{1-\gamma}\, dt\right]$ subject to the wealth dynamics:

    $$dW_t = \bigl[rW_t + \pi_t W_t(\mu - r) - C_t\bigr]\, dt + \pi_t W_t \sigma\, dW_t$$

    Using dynamic programming, the HJB equation for the value function $J(W)$ is:

    $$0 = \max_{\pi, C}\left\{e^{-\rho t}\frac{C^{1-\gamma}}{1-\gamma} + J'(W)\bigl[rW + \pi W(\mu - r) - C\bigr] + \frac{1}{2}J''(W)\pi^2 W^2 \sigma^2\right\}$$

    The first-order condition with respect to $\pi$ is:

    $$J'(W)W(\mu - r) + J''(W)\pi W^2 \sigma^2 = 0$$

    Solving for $\pi$:

    $$\pi^* = -\frac{J'(W)}{W J''(W)} \cdot \frac{\mu - r}{\sigma^2}$$

    For CRRA utility, the value function takes the form $J(W) = A W^{1-\gamma}/(1-\gamma)$ for some constant $A > 0$. Then $J'(W) = AW^{-\gamma}$ and $J''(W) = -\gamma A W^{-\gamma - 1}$, so:

    $$-\frac{J'(W)}{WJ''(W)} = -\frac{AW^{-\gamma}}{W(-\gamma A W^{-\gamma-1})} = \frac{1}{\gamma}$$

    Therefore:

    $$\pi^* = \frac{\mu - r}{\gamma \sigma^2}$$

    This is the Merton rule. Now impose market clearing: in the Lucas economy the bond is in zero net supply, so the agent must hold all wealth in the stock, i.e., $\pi^* = 1$:

    $$1 = \frac{\mu - r}{\gamma \sigma^2} \qquad \Longrightarrow \qquad \mu - r = \gamma \sigma^2$$

    This is the equilibrium risk premium.

??? success "Solution to Exercise 2"
    Using the equity premium puzzle numbers:

    $$\gamma = \frac{\mu - r}{\sigma^2} = \frac{0.06}{(0.16)^2} = \frac{0.06}{0.0256} \approx 2.34$$

    Wait—let us recompute carefully. With $\mu - r \approx 6\% = 0.06$ and $\sigma \approx 16\% = 0.16$:

    $$\gamma = \frac{0.06}{0.0256} \approx 2.34$$

    However, this calculation uses the **arithmetic** risk premium. The actual puzzle uses annualized data where the historical equity premium over Treasury bills is approximately 6% with $\sigma \approx 16\%$, but the Mehra–Prescott calibration involves consumption growth (not stock returns). In their calibration, consumption growth volatility is much lower ($\sigma_c \approx 3.3\%$), and with the CCAPM relation $\mu - r = \gamma \sigma_c^2$:

    $$\gamma = \frac{0.06}{(0.033)^2} \approx \frac{0.06}{0.00109} \approx 55$$

    In the simplified model of this chapter where consumption equals the stock (so $\sigma_c = \sigma$), we get $\gamma \approx 2.34$, which seems reasonable. The puzzle arises in richer models where consumption is much smoother than stock returns, requiring implausibly high $\gamma$ (values above 10–50 depending on the calibration) to match the observed premium.

    A risk aversion of $\gamma > 10$ is considered implausible because it implies extreme behavior: an agent with $\gamma = 50$ would pay nearly all of their wealth to avoid a fair 50-50 bet that doubles or halves their consumption.

    **Model extensions** that address the puzzle include: (i) **habit formation** (Campbell and Cochrane, 1999), where utility depends on consumption relative to a slow-moving habit, amplifying the effective risk aversion; (ii) **Epstein–Zin recursive utility**, which separates risk aversion from the elasticity of intertemporal substitution; (iii) **rare disaster models** (Barro, 2006), where a small probability of catastrophic consumption drops generates a large risk premium with moderate $\gamma$.

??? success "Solution to Exercise 3"
    The pricing kernel is $M_t = e^{-\rho t} S_t^{-\gamma}$. The equilibrium pricing condition requires $M_t V(t, S_t)$ to be a $\mathbb{P}$-martingale.

    **Step 1: Dynamics of $M_t$.** Apply Itô's formula to $S_t^{-\gamma}$:

    $$d(S_t^{-\gamma}) = -\gamma S_t^{-\gamma-1}\, dS_t + \frac{1}{2}\gamma(\gamma+1)S_t^{-\gamma-2}(dS_t)^2$$

    $$= S_t^{-\gamma}\!\left[\bigl(-\gamma\mu + \tfrac{1}{2}\gamma(\gamma+1)\sigma^2\bigr)\, dt - \gamma\sigma\, dW_t\right]$$

    Including the $e^{-\rho t}$ factor:

    $$\frac{dM_t}{M_t} = -\bigl[\rho + \gamma\mu - \tfrac{1}{2}\gamma(\gamma+1)\sigma^2\bigr]\, dt - \gamma\sigma\, dW_t$$

    Define $\kappa = \rho + \gamma\mu - \frac{1}{2}\gamma(\gamma+1)\sigma^2$. The equilibrium risk-free rate is $r = \kappa$.

    **Step 2: Dynamics of $V$.** By Itô's formula:

    $$dV = \left(\frac{\partial V}{\partial t} + \mu S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right)dt + \sigma S\frac{\partial V}{\partial S}\, dW$$

    **Step 3: Product rule for $d(M_t V_t)$.** The drift of $M_t V_t$ includes the cross-variation:

    $$dM_t\, dV_t = (-\gamma\sigma M_t)(\sigma S\, \partial_S V)\, dt = -\gamma\sigma^2 S\, M_t\, \partial_S V\, dt$$

    Setting the drift of $d(M_t V_t)$ to zero and dividing by $M_t$:

    $$\frac{\partial V}{\partial t} + \mu S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - \kappa V - \gamma\sigma^2 S\frac{\partial V}{\partial S} = 0$$

    This simplifies to:

    $$\frac{\partial V}{\partial t} + (\mu - \gamma\sigma^2)S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0$$

    **Step 4: Equilibrium substitution.** The equilibrium risk premium gives $\mu - \gamma\sigma^2 = r$. Substituting:

    $$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0$$

    This is the Black–Scholes PDE.

??? success "Solution to Exercise 4"
    **Equilibrium approach — advantages:**

    - **Explains** the risk-free rate $r$ and the equity risk premium $\mu - r$ as endogenous quantities determined by preferences ($\gamma$, $\rho$), expected returns ($\mu$), and volatility ($\sigma$).
    - Provides a structural model: if model parameters change (e.g., volatility increases), the equilibrium predicts how $r$ and $\mu - r$ adjust, which matters for scenario analysis and stress testing.
    - Connects option pricing to the broader macroeconomic and asset pricing literature (consumption CAPM, equity premium puzzle).

    **Equilibrium approach — limitations:**

    - Requires specifying investor preferences (CRRA with parameter $\gamma$), which are not directly observable and difficult to calibrate.
    - The representative-agent assumption is a strong simplification; real markets have heterogeneous investors.
    - The simple CRRA model produces counterfactual predictions (the equity premium puzzle), undermining confidence in the specific parameter values.
    - For a practitioner pricing options, the equilibrium model adds complexity without improving the price: if $r$ and $\sigma$ are observable, the Black–Scholes PDE is the same regardless of derivation.

    **Delta-hedging approach — advantages:**

    - Takes $r$ and $\sigma$ as market-observable inputs—no preference specification needed.
    - Directly operational: the derivation constructs the replicating strategy $\Delta = \partial V/\partial S$, which practitioners use daily.
    - Model-free in the sense that it does not depend on any particular equilibrium or agent behavior, only on the absence of arbitrage and the ability to trade continuously.

    **Delta-hedging approach — limitations:**

    - Takes $r$ and $\mu - r$ as exogenous; cannot explain why they take their observed values.
    - Assumes continuous hedging and zero transaction costs, which are idealizations.
    - Does not provide insight into how the pricing environment would change if market conditions shift (e.g., if volatility changes, the equilibrium risk-free rate might also change, but the delta-hedging approach treats $r$ as fixed).

    For a practitioner, the delta-hedging approach is more useful for day-to-day pricing and hedging, while the equilibrium approach provides structural understanding for longer-horizon questions about market dynamics and risk premia.

??? success "Solution to Exercise 5"
    Given: $\gamma = 2$, $\mu = 0.10$, $\sigma = 0.20$, $\rho = 0.03$.

    **Equilibrium risk-free rate:**

    $$r = \rho + \gamma\mu - \frac{1}{2}\gamma(\gamma+1)\sigma^2 = 0.03 + 2(0.10) - \frac{1}{2}(2)(3)(0.04)$$

    $$= 0.03 + 0.20 - 0.12 = 0.11$$

    So $r = 11\%$.

    **Equity risk premium:**

    $$\mu - r = 0.10 - 0.11 = -0.01$$

    Alternatively, using the equilibrium formula directly:

    $$\mu - r = \gamma\sigma^2 = 2 \times 0.04 = 0.08$$

    There is an apparent contradiction. Let us reconcile. The equilibrium risk premium formula $\mu - r = \gamma\sigma^2$ gives $\mu - r = 0.08$, so $r = \mu - 0.08 = 0.02$. Let us verify using the full formula:

    $$r = \rho + \gamma\mu - \frac{1}{2}\gamma(\gamma+1)\sigma^2 = 0.03 + 0.20 - \frac{1}{2}(2)(3)(0.04) = 0.23 - 0.12 = 0.11$$

    But $\mu - r = 0.10 - 0.11 = -0.01 \neq \gamma\sigma^2 = 0.08$. The issue is that both formulas must hold simultaneously in equilibrium, which constrains $\mu$. In the Lucas economy, $\mu$ is determined by the endowment process and is not a free parameter—market clearing determines all prices given the endowment dynamics. The formula $r = \rho + \gamma\mu - \frac{1}{2}\gamma(\gamma+1)\sigma^2$ and $\mu - r = \gamma\sigma^2$ together imply:

    $$\mu = r + \gamma\sigma^2 = \rho + \gamma\mu - \frac{1}{2}\gamma(\gamma+1)\sigma^2 + \gamma\sigma^2$$

    Solving for $r$: $r = \mu - \gamma\sigma^2 = 0.10 - 0.08 = 0.02$.

    The correct computation using the risk premium relation gives $r = 0.02$, and one can verify this is consistent:

    $$r = \rho + \gamma\mu - \frac{1}{2}\gamma(\gamma+1)\sigma^2 \;\Rightarrow\; 0.02 = 0.03 + 0.20 - 0.12 = 0.11$$

    This does not match, indicating the given parameters are not fully consistent with the equilibrium (they over-determine the system). Taking the risk premium relation as the binding constraint: $r = \mu - \gamma\sigma^2 = 0.10 - 0.08 = 0.02$ and $\mu - r = 0.08$.

    **Verification of the Black–Scholes PDE:** The PDE is:

    $$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0$$

    With $r = 0.02$ and $\sigma = 0.20$, this becomes:

    $$\frac{\partial V}{\partial t} + 0.02\, S\frac{\partial V}{\partial S} + \frac{1}{2}(0.04) S^2 \frac{\partial^2 V}{\partial S^2} - 0.02\, V = 0$$

    The drift coefficient is $r = 0.02 = \mu - \gamma\sigma^2$, confirming that the equilibrium substitution converts the physical drift $\mu = 0.10$ into the risk-neutral drift $r = 0.02$ in the PDE. The Black–Scholes PDE holds with these equilibrium values.
