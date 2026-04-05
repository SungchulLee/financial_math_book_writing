# Black–Scholes PDE via Equilibrium Pricing


This derivation removes the physical drift $\mu$ by **preferences and market clearing**: equilibrium pins $\mu - \gamma\sigma^2 = r$, so that the SDF absorbs the risk premium and the pricing PDE depends only on $r$ and $\sigma$. Instead of eliminating risk by trading or changing probability, we explain why the risk premium exists in the first place. The risk-neutral drift is not imposed—it emerges from preferences.

The argument proceeds in three stages: (1) specify an economy with CRRA preferences, (2) derive the stochastic discount factor from the Euler equation and market clearing, and (3) apply Itô's formula to the SDF-weighted option price to obtain the PDE.

The Black–Scholes PDE can be derived as a consequence of **general equilibrium** in a representative-agent economy, without explicitly constructing a replicating portfolio or hedging strategy (though the framework still relies on no-arbitrage and market completeness). The key equilibrium output is the **stochastic discount factor** (pricing kernel), which determines the relationship between the stock's physical drift $\mu$, the risk-free rate $r$, and the risk aversion parameter $\gamma$—and once this relationship is imposed, the Black–Scholes PDE follows. This is fundamentally different from the [delta-hedging](delta_hedging.md) and [change-of-numéraire](change_of_numeraire.md) approaches because it provides a **model-based explanation** of the risk-free rate and the equity risk premium as endogenous quantities, rather than taking them as given.

Note, however, that the equilibrium Euler equation implicitly embeds the absence of arbitrage—the SDF framework prices all assets consistently precisely because no-arbitrage holds. Indeed, the SDF and the risk-neutral measure are two representations of the same pricing object: $M_t = (d\mathbb{Q}/d\mathbb{P})\, e^{-rt}$. One weights states by marginal utility; the other reweights probabilities—both encode the same pricing rule. The distinction is one of *method* (preferences and market clearing vs. replication), not of underlying economic content.

The primary derivation below uses a **Lucas (1978) pure exchange economy**, which is self-contained and logically clean. An [alternative derivation via the Merton problem](#alternative-derivation-via-the-merton-problem) is presented afterward for readers more familiar with portfolio optimization.


## The Lucas-Tree Economy


Consider a **representative-agent, complete-markets equilibrium** in a pure exchange economy (Lucas, 1978) with:

- a single consumption good,
- a single risky asset (the "tree") paying a continuous dividend stream $D_t$,
- a risk-free asset in zero net supply,
- CRRA utility $U(C) = C^{1-\gamma}/(1-\gamma)$ for $\gamma > 0$, $\gamma \neq 1$ (where $\gamma$ is the coefficient of relative risk aversion and $\rho > 0$ is the rate of time preference).

The agent maximizes

$$\max_{C_t} \; \mathbb{E}\!\left[\int_0^\infty e^{-\rho t}\, \frac{C_t^{1-\gamma}}{1-\gamma}\, dt\right]$$

The economy is endowed with a stochastic dividend process

$$dD_t = \mu_D D_t\, dt + \sigma_D D_t\, dW_t$$

Market clearing requires that the agent consumes the entire endowment:

$$C_t = D_t$$

This is the crucial equilibrium condition. Consumption is **exogenous** (determined by the endowment), so no portfolio problem needs to be solved.


## Asset Prices and the Stochastic Discount Factor


Let $S_t$ denote the price of the tree. By the fundamental asset pricing relation:

$$S_t = \mathbb{E}_t\!\left[\int_t^\infty M_{t,s}\, D_s\, ds\right]$$

where the **stochastic discount factor** (SDF) is

$$M_t = e^{-\rho t}\, C_t^{-\gamma} = e^{-\rho t}\, D_t^{-\gamma}$$

In equilibrium, any asset with price process $P_t$ must satisfy the **Euler equation**: the process $M_t P_t$ is a martingale (under appropriate integrability conditions on $P_t$).

Since $D_t$ follows a GBM and utility is CRRA, the price-dividend ratio $S_t / D_t$ is a positive constant $\kappa$. This follows from solving the valuation integral and using homogeneity of CRRA utility: the integrand scales as $D_t$ times a deterministic function of $s - t$, so $S_t$ is proportional to $D_t$. Therefore

$$S_t = \kappa\, D_t$$

and the stock inherits the dividend dynamics:

$$\frac{dS_t}{S_t} = \mu_D\, dt + \sigma_D\, dW_t$$

So we identify $\mu = \mu_D$ and $\sigma = \sigma_D$. The key consequence is that **aggregate consumption is proportional to the stock price**: $C_t = D_t = S_t/\kappa$. This is not an assumption but a structural result of the Lucas-tree economy with GBM dividends and CRRA preferences. The pricing kernel becomes (up to a positive constant that cancels in pricing ratios)

$$M_t = e^{-\rho t}\, S_t^{-\gamma}$$

### Dynamics of M_t

Apply Itô's formula to $S_t^{-\gamma}$ with $f(S) = S^{-\gamma}$:

$$d(S_t^{-\gamma}) = -\gamma S_t^{-\gamma-1}\, dS_t + \frac{1}{2}\gamma(\gamma + 1)\, S_t^{-\gamma-2}\, (dS_t)^2$$

$$= S_t^{-\gamma}\!\left[\bigl(-\gamma\mu + \tfrac{1}{2}\gamma(\gamma+1)\sigma^2\bigr)\, dt - \gamma\sigma\, dW_t\right]$$

Since $e^{-\rho t}$ has zero quadratic variation, the product rule gives

$$\frac{dM_t}{M_t} = -\underbrace{\bigl[\rho + \gamma\mu - \tfrac{1}{2}\gamma(\gamma+1)\sigma^2\bigr]}_{\displaystyle =:\, \kappa}\, dt - \gamma\sigma\, dW_t$$


## Equilibrium Returns


### Equilibrium Risk-Free Rate

The bond price $B_t = e^{rt}$ must satisfy the martingale condition: $M_t B_t$ is a martingale, so $d(M_t B_t)$ has zero drift. Since $dB_t = rB_t\, dt$ (zero quadratic variation), the drift of $M_t B_t$ is

$$M_t B_t(-\kappa + r)\, dt = 0$$

Therefore

$$\boxed{r = \kappa = \rho + \gamma\mu - \tfrac{1}{2}\gamma(\gamma+1)\sigma^2}$$

This is the **equilibrium risk-free rate**. It increases with impatience ($\rho$) and with $\gamma\mu$, reflecting expected consumption growth under the equilibrium identification $C_t \propto S_t$. It decreases with consumption volatility through the precautionary savings term $-\frac{1}{2}\gamma(\gamma+1)\sigma^2$.

### Equilibrium Risk Premium

The Euler equation requires $M_t S_t$ to be a martingale. Applying Itô's product rule (the calculation mirrors the derivative pricing computation in the next section) yields

$$\boxed{\mu - r = \gamma\sigma^2}$$

This is the **equilibrium risk premium**: the stock's expected excess return equals risk aversion times the variance of returns. It is the continuous-time version of the consumption CAPM—in this economy where consumption growth is perfectly correlated with stock returns, the risk premium is proportional to risk aversion.


## Deriving the Black–Scholes PDE


**Proposition.** *In the Lucas-tree economy with CRRA utility and GBM dividends, the equilibrium pricing kernel is $M_t = e^{-\rho t} S_t^{-\gamma}$, and the price $V(t,S)$ of any European derivative with payoff $\Phi(S_T)$ satisfies the Black–Scholes PDE.*

Let $V(t, S)$ be the price of such a derivative, where we assume $V \in C^{1,2}([0,T) \times (0,\infty))$ with at most polynomial growth. The equilibrium pricing condition requires that $M_t\, V(t, S_t)$ is a $\mathbb{P}$-martingale. (Itô's formula makes $M_t V(t, S_t)$ a local martingale; in this Black–Scholes setting, the polynomial growth condition on $V$, combined with the finite moments of geometric Brownian motion, promotes it to a true martingale.)

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

where we used $\kappa = r$. Using the equilibrium relation $\mu - \gamma\sigma^2 = r$, this becomes:

$$\boxed{\frac{\partial V}{\partial t} + rS \frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0}$$

with terminal condition $V(T, S) = \Phi(S)$. This is the **Black–Scholes PDE**.

The equilibrium relation $\mu - \gamma\sigma^2 = r$ plays the same role as the Girsanov drift removal in the risk-neutral approach: it converts the physical drift $\mu$ into the risk-neutral drift $r$—but here the conversion is an equilibrium consequence, not an assumption.


## What the Equilibrium Approach Adds


The equilibrium derivation yields three results that the no-arbitrage approach cannot provide:

**Endogenous risk-free rate.** The no-arbitrage derivation takes $r$ as an exogenous parameter. Here, $r = \rho + \gamma\mu - \frac{1}{2}\gamma(\gamma+1)\sigma^2$ is determined by preferences and the investment opportunity set.

**Endogenous risk premium.** The equity premium $\mu - r = \gamma\sigma^2$ is derived from market clearing, not assumed. The parameter $\gamma$ connects preferences to risk premia—this is the consumption CAPM in continuous time.

**Connection to the equity premium puzzle.** Empirically, $\mu - r \approx 6\%$ and $\sigma \approx 16\%$ for the US equity market. In the model of this page, where consumption volatility equals stock volatility ($\sigma_c = \sigma$), the implied risk aversion is $\gamma = (\mu - r)/\sigma^2 \approx 0.06/0.0256 \approx 2.34$—which appears moderate. However, the Mehra and Prescott (1985) calibration uses **aggregate consumption growth** data, where volatility is much lower ($\sigma_c \approx 3.3\%$). In the consumption CAPM relation $\mu - r = \gamma\sigma_c^2$, this gives $\gamma \approx 0.06/0.00109 \approx 55$—an implausibly high level of risk aversion. The puzzle arises precisely because consumption is far smoother than stock returns in the data, so the simple representative-agent model with CRRA utility requires extreme $\gamma$ to match the observed equity premium. This motivates extensions to habit formation (Campbell and Cochrane, 1999), Epstein–Zin recursive utility, rare disasters (Barro, 2006), and heterogeneous-agent models.


## Alternative Derivation via the Merton Problem


The Lucas-tree derivation above is self-contained: consumption is exogenous, and no portfolio optimization is needed. An alternative—and more familiar—route uses the **Merton portfolio problem** to characterize optimal behavior, then imposes market clearing.

A representative agent allocates wealth $W_t$ between a risky stock ($dS_t = \mu S_t\, dt + \sigma S_t\, dW_t$) and a risk-free bond ($dB_t = rB_t\, dt$). The solution to this stochastic control problem (Merton, 1969, 1971) gives the optimal portfolio allocation:

$$\pi^* = \frac{\mu - r}{\gamma \sigma^2}$$

This is the **Merton rule**: the optimal risky-asset share is the Sharpe ratio divided by the product of risk aversion and volatility. Market clearing requires $\pi^* = 1$ (the bond is in zero net supply), which immediately gives $\mu - r = \gamma\sigma^2$—the same risk premium as above.

The Merton approach is more **pedagogically accessible** since it builds on the familiar portfolio optimization problem. But the logic is hybrid: a partial-equilibrium optimization (Merton) is grafted onto a general-equilibrium clearing condition (Lucas). Both routes yield the same PDE and the same economic content; the difference is one of logical architecture.


## Summary


The logical chain of the Lucas-tree derivation is:

1. **Market clearing** ($C_t = D_t$) and **CRRA homogeneity**: yield the pricing kernel $M_t = e^{-\rho t} S_t^{-\gamma}$ and the equilibrium risk premium $\mu - r = \gamma\sigma^2$.
2. **Martingale condition** ($M_t V_t$ is a martingale): yields a PDE with drift coefficient $\mu - \gamma\sigma^2$.
3. **Equilibrium substitution** ($\mu - \gamma\sigma^2 = r$): recovers the Black–Scholes PDE.

This yields a **consistent equilibrium characterization**: the Black–Scholes PDE is not merely a no-arbitrage condition—it is an **equilibrium outcome** in this complete-markets diffusion economy, where preferences, technology, and market clearing jointly determine asset prices.


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

---

**Exercise 2.** Using the equilibrium condition $\mu - r = \gamma\sigma^2$ and the equity premium puzzle numbers ($\mu - r \approx 6\%$, $\sigma \approx 16\%$), compute the implied risk aversion parameter $\gamma$. Explain why this value is considered implausibly high and name one model extension that attempts to resolve this puzzle.

??? success "Solution to Exercise 2"
    In the model of this page, consumption volatility equals stock volatility ($\sigma_c = \sigma$), so the equilibrium relation $\mu - r = \gamma\sigma^2$ gives:

    $$\gamma = \frac{\mu - r}{\sigma^2} = \frac{0.06}{(0.16)^2} = \frac{0.06}{0.0256} \approx 2.34$$

    This appears moderate. However, the equity premium puzzle of Mehra and Prescott (1985) uses **aggregate consumption growth** data, not stock returns. In the data, consumption growth is far smoother than stock returns, with volatility $\sigma_c \approx 3.3\%$. Using the consumption CAPM relation $\mu - r = \gamma \sigma_c^2$:

    $$\gamma = \frac{0.06}{(0.033)^2} \approx \frac{0.06}{0.00109} \approx 55$$

    The discrepancy between $\gamma \approx 2.34$ (using stock volatility) and $\gamma \approx 55$ (using consumption volatility) highlights that the puzzle arises precisely because consumption is much smoother than stock returns. The simplified model of this page sidesteps the puzzle by identifying $\sigma_c = \sigma$, but in practice, this identification fails.

    A risk aversion of $\gamma > 10$ is considered implausible because it implies extreme behavior: an agent with $\gamma = 50$ would pay nearly all of their wealth to avoid a fair 50-50 bet that doubles or halves their consumption.

    **Model extensions** that address the puzzle include: (i) **habit formation** (Campbell and Cochrane, 1999), where utility depends on consumption relative to a slow-moving habit, amplifying the effective risk aversion; (ii) **Epstein–Zin recursive utility**, which separates risk aversion from the elasticity of intertemporal substitution; (iii) **rare disaster models** (Barro, 2006), where a small probability of catastrophic consumption drops generates a large risk premium with moderate $\gamma$.

---

**Exercise 3.** The pricing kernel in the equilibrium model is $M_t = e^{-\rho t} S_t^{-\gamma}$. Show that the condition for $M_t V(t, S_t)$ to be a $\mathbb{P}$-martingale, combined with the equilibrium substitution $\mu - \gamma\sigma^2 = r$, yields the Black-Scholes PDE.

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

---

**Exercise 4.** Compare the equilibrium derivation with the delta-hedging derivation. The equilibrium approach "explains" $r$ and $\mu - r$ as endogenous quantities, while delta hedging takes them as given. Describe the advantages and limitations of each perspective for a practitioner pricing options.

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

---

**Exercise 5.** In the CRRA equilibrium, the risk-free rate is $r = \rho + \gamma\mu - \frac{1}{2}\gamma(\gamma+1)\sigma^2$ and the equilibrium risk premium is $\mu - r = \gamma\sigma^2$. For $\gamma = 0.5$, $\mu = 0.07$, $\sigma = 0.20$, and $\rho = 0.03$, verify that these parameters are mutually consistent, compute the equilibrium $r$ and the equity risk premium $\mu - r$, and write out the Black-Scholes PDE with the resulting numerical coefficients.

??? success "Solution to Exercise 5"
    Given: $\gamma = 0.5$, $\mu = 0.07$, $\sigma = 0.20$, $\rho = 0.03$.

    **Equilibrium risk-free rate via the risk premium formula:**

    $$r = \mu - \gamma\sigma^2 = 0.07 - 0.5 \times 0.04 = 0.07 - 0.02 = 0.05$$

    **Equity risk premium:**

    $$\mu - r = \gamma\sigma^2 = 0.5 \times 0.04 = 0.02$$

    **Consistency check via the SDF formula:**

    $$r = \rho + \gamma\mu - \frac{1}{2}\gamma(\gamma+1)\sigma^2 = 0.03 + 0.5(0.07) - \frac{1}{2}(0.5)(1.5)(0.04)$$

    $$= 0.03 + 0.035 - 0.015 = 0.05 \;\checkmark$$

    Both formulas give $r = 0.05$, confirming the parameters are mutually consistent. (In the Lucas economy, the four parameters $(\gamma, \mu, \sigma, \rho)$ are not all free—they must satisfy the consistency relation $\mu(1-\gamma) = \rho + \frac{1}{2}\gamma(1-\gamma)\sigma^2$, which can be verified: $0.07(0.5) = 0.035$ and $0.03 + \frac{1}{2}(0.5)(0.5)(0.04) = 0.03 + 0.005 = 0.035$. $\checkmark$)

    **Black–Scholes PDE with numerical coefficients:**

    $$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0$$

    becomes:

    $$\frac{\partial V}{\partial t} + 0.05\, S\frac{\partial V}{\partial S} + 0.02\, S^2 \frac{\partial^2 V}{\partial S^2} - 0.05\, V = 0$$

    The drift coefficient is $r = 0.05 = \mu - \gamma\sigma^2 = 0.07 - 0.02$, confirming that the equilibrium substitution converts the physical drift $\mu = 0.07$ into the risk-neutral drift $r = 0.05$ in the PDE.

---

**Exercise 6.** Show explicitly that the equilibrium SDF $M_t = e^{-\rho t}C_t^{-\gamma}$ satisfies $M_t = \frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_t} \cdot e^{-rt}$, where $\mathbb{Q}$ is the risk-neutral measure constructed via Girsanov's theorem with market price of risk $\theta = (\mu - r)/\sigma$. Use the equilibrium identification $C_t = S_t$ and the relation $r = \rho + \gamma\mu - \frac{1}{2}\gamma(\gamma+1)\sigma^2$.

??? success "Solution to Exercise 6"
    **Step 1: Express the SDF in terms of $S_t$.** With $C_t = S_t$ (market clearing) and $S_t = S_0\exp\!\left((\mu - \tfrac{1}{2}\sigma^2)t + \sigma W_t\right)$:

    $$M_t = e^{-\rho t}S_t^{-\gamma} = e^{-\rho t}S_0^{-\gamma}\exp\!\left(-\gamma(\mu - \tfrac{1}{2}\sigma^2)t - \gamma\sigma W_t\right)$$

    **Step 2: Express the Radon–Nikodym derivative.** The Girsanov density with $\theta = (\mu - r)/\sigma$ is:

    $$\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_t} = \exp\!\left(-\theta W_t - \frac{1}{2}\theta^2 t\right)$$

    So $\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_t} \cdot e^{-rt} = \exp\!\left(-\theta W_t - \frac{1}{2}\theta^2 t - rt\right)$.

    **Step 3: Match the Brownian terms.** The SDF has $W_t$ coefficient $-\gamma\sigma$. The Girsanov density has $W_t$ coefficient $-\theta = -(\mu - r)/\sigma$. Using $\mu - r = \gamma\sigma^2$:

    $$\theta = \frac{\gamma\sigma^2}{\sigma} = \gamma\sigma$$

    So both have $W_t$ coefficient $-\gamma\sigma$. $\checkmark$

    **Step 4: Match the deterministic terms.** From the SDF:

    $$-\rho - \gamma\!\left(\mu - \tfrac{1}{2}\sigma^2\right) = -\rho - \gamma\mu + \tfrac{1}{2}\gamma\sigma^2$$

    From $\frac{d\mathbb{Q}}{d\mathbb{P}} \cdot e^{-rt}$:

    $$-\frac{1}{2}\theta^2 - r = -\frac{1}{2}\gamma^2\sigma^2 - r$$

    Substituting $r = \rho + \gamma\mu - \frac{1}{2}\gamma(\gamma+1)\sigma^2$:

    $$-\frac{1}{2}\gamma^2\sigma^2 - \rho - \gamma\mu + \frac{1}{2}\gamma(\gamma+1)\sigma^2 = -\rho - \gamma\mu + \frac{1}{2}\gamma\sigma^2$$

    since $\frac{1}{2}\gamma(\gamma+1)\sigma^2 - \frac{1}{2}\gamma^2\sigma^2 = \frac{1}{2}\gamma\sigma^2$. This matches the SDF deterministic term. $\checkmark$

    **Conclusion.** Up to the constant $S_0^{-\gamma}$ (which normalizes $M_0 = S_0^{-\gamma}$ and is absorbed into $\mathbb{E}[M_0] = S_0^{-\gamma}$), we have $M_t = \frac{d\mathbb{Q}}{d\mathbb{P}}\big|_{\mathcal{F}_t} \cdot e^{-rt}$. The SDF and the discounted Radon–Nikodym derivative are the same object: one arises from marginal utility, the other from Girsanov's theorem, confirming the fundamental identity between the equilibrium and risk-neutral pricing frameworks. $\square$
