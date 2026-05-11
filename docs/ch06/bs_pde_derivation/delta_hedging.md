# Black–Scholes PDE via Delta Hedging


This derivation removes the physical drift $\mu$ by **portfolio construction**: choosing the hedge ratio $\Delta = V_S$ eliminates all stochastic risk, and no-arbitrage forces the resulting riskless portfolio to earn the rate $r$. This is the original approach of Black and Scholes (1973), and remains the most direct route from market assumptions to the pricing equation.


## Setup


**Stock price.** The stock follows geometric Brownian motion under the physical measure:

$$dS_t = \mu S_t\, dt + \sigma S_t\, dW_t$$

with constant drift $\mu$, volatility $\sigma > 0$, and standard Brownian motion $W_t$.

**Risk-free asset.** A money market account grows at constant rate $r$:

$$dB_t = rB_t\, dt, \qquad B_0 = 1$$

**Derivative.** A European derivative with payoff $\Phi(S_T)$ at maturity $T$ has price $V(t, S)$ at time $t$ when the stock price is $S$. We assume $V \in C^{1,2}([0,T) \times (0,\infty))$.

In practice, a derivatives dealer typically **writes** (sells) the option, receiving the premium $V$, and then manages the resulting short exposure by holding stock. The hedging portfolio below reflects this realistic viewpoint.


## Step 1: Dynamics of the Derivative Price


Apply Itô's formula to $V(t, S_t)$:

$$dV = \frac{\partial V}{\partial t}\, dt + \frac{\partial V}{\partial S}\, dS + \frac{1}{2}\frac{\partial^2 V}{\partial S^2}\,(dS)^2$$

The quadratic variation is $(dS)^2 = \sigma^2 S^2\, dt$ (using the Itô rules $(dt)^2 = 0$, $dt\, dW = 0$, $(dW)^2 = dt$). Substituting $dS = \mu S\, dt + \sigma S\, dW$:

$$dV = \left(\frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right) dt + \sigma S \frac{\partial V}{\partial S}\, dW$$

Throughout, we write $V_t = \partial V/\partial t$, $V_S = \partial V/\partial S$, and $V_{SS} = \partial^2 V/\partial S^2$ when convenient.


## Step 2: The Hedging Portfolio


The dealer hedges the short option position by buying $\Delta$ shares. The resulting portfolio is

$$\Pi_t = -V_t + \Delta\, S_t$$

Over an infinitesimal interval $[t, t + dt]$, hold $\Delta$ **fixed** (it will be rebalanced at $t + dt$). The change in portfolio value is

$$d\Pi = -dV + \Delta\, dS$$

This implicitly assumes that any cash required to rebalance the hedge is borrowed or lent at the risk-free rate $r$. The precise relationship between this "freeze-and-rebalance" construction and the self-financing formulation is discussed in the admonition near the end of this page (and made fully rigorous in [self-financing replication](replication.md)).

Substituting the expressions for $dV$ and $dS$:

$$d\Pi = \left(-\frac{\partial V}{\partial t} - \mu S \frac{\partial V}{\partial S} - \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + \Delta \mu S\right) dt + \left(-\sigma S \frac{\partial V}{\partial S} + \Delta \sigma S\right) dW$$


## Step 3: Choose Δ to Eliminate Risk


We now choose $\Delta$ to eliminate the stochastic component. Set the coefficient of $dW$ to zero:

$$-\sigma S \frac{\partial V}{\partial S} + \Delta \sigma S = 0 \implies \Delta = \frac{\partial V}{\partial S}$$

This is the **delta** of the derivative. With this choice, the stochastic term vanishes and the portfolio becomes locally deterministic:

$$d\Pi = \left(-\frac{\partial V}{\partial t} - \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right) dt$$

The drift $\mu$ has cancelled. The drift term of the hedged portfolio involves only $V_t$ (time decay) and $V_{SS}$ (convexity), along with known coefficients $\sigma$ and $S$—not the stock's expected return.


## Step 4: No-Arbitrage Condition


Under the Black–Scholes assumptions, the hedged portfolio is instantaneously riskless. If it did not earn the risk-free rate, an arbitrage would arise. Therefore

$$d\Pi = r\Pi\, dt$$

Substituting $\Pi = -V + \frac{\partial V}{\partial S}\, S$:

$$-\frac{\partial V}{\partial t} - \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} = r\!\left(-V + S\frac{\partial V}{\partial S}\right)$$

Rearranging:

$$\boxed{\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0}$$

This is the **Black–Scholes PDE**, subject to the terminal condition $V(T, S) = \Phi(S)$.

!!! note "Sign convention"
    The sign convention for $\Pi$ (long or short the option) does not affect the PDE. The factor of $-1$ propagates through both sides of $d\Pi = r\Pi\, dt$ and cancels, leaving the same pricing equation. The PDE is a property of the price function $V$, not of which side of the trade you are on.

Continuous hedging is, of course, an idealization: in practice, portfolios are rebalanced at discrete intervals, and each rebalance incurs transaction costs. These frictions mean that exact replication is impossible, and the hedging error grows with the rebalancing interval. Exercise 5 below quantifies this effect.


## Why the Drift μ Disappears


The absence of $\mu$ from the PDE is the central economic insight of the derivation. The hedging portfolio eliminates all exposure to the stock's random fluctuations, so the stock's expected return becomes irrelevant—only the volatility (which determines the magnitude of fluctuations, and hence the cost of hedging) and the risk-free rate (which determines the opportunity cost) enter the equation.

This means investors with different views on the stock's future return all agree on the option price, provided they agree on the volatility. It is also the reason the PDE can be solved without specifying the physical drift, and why the solution coincides with the expectation under the risk-neutral measure.


## Extension: Continuous Dividend Yield


The continuous dividend yield $q$ is most natural for **broad equity indices** (where dividends from hundreds of constituents arrive nearly every business day) and for **foreign exchange** (where $q = r_f$, the foreign risk-free rate, gives the Garman–Kohlhagen formula). Setting $q = r$ recovers the Black (1976) model for options on futures. For individual stocks, $q$ is a convenient approximation; discrete-dividend methods (escrowed dividends, tree-based approaches) are preferred when a single ex-date dominates the option's life.


### Derivation

When the stock pays a continuous dividend yield $q$, two modifications are needed.

**Modified stock dynamics.** The stock price appreciates at rate $\mu - q$ (dividends reduce the capital gain):

$$dS_t = (\mu - q)S_t\, dt + \sigma S_t\, dW_t$$

**Modified portfolio dynamics.** The portfolio is still $\Pi = -V + \Delta S$, but being long $\Delta$ shares now earns dividend income $q \Delta S\, dt$. The total change over $[t, t+dt]$ is

$$d\Pi = -dV + \Delta\, dS + q\Delta S\, dt$$

Apply Itô's formula with the modified stock dynamics and set $\Delta = \partial V / \partial S$ to cancel the stochastic term:

$$d\Pi = \left(-\frac{\partial V}{\partial t} - \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + qS\frac{\partial V}{\partial S}\right) dt$$

The no-arbitrage condition $d\Pi = r\Pi\, dt = r(-V + S\partial V/\partial S)\, dt$ gives

$$-\frac{\partial V}{\partial t} - \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + qS\frac{\partial V}{\partial S} = -rV + rS\frac{\partial V}{\partial S}$$

Rearranging:

$$\boxed{\frac{\partial V}{\partial t} + (r - q)S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0}$$

The dividend yield replaces $r$ by $r - q$ in the first-order (drift) term, while the discounting term $-rV$ is unchanged.


??? note "On self-financing and rebalancing"
    This derivation holds $\Delta$ fixed over each infinitesimal interval $[t, t+dt]$ and then rebalances—a "freeze-and-rebalance" heuristic that avoids the machinery of self-financing strategies. In the standard Black–Scholes setting this leads to the same PDE as the rigorous self-financing replication argument (see the [rigorous version](replication.md)), which constructs $(\alpha_t, \beta_t)$ in the stock and bond satisfying $dV_t = \alpha_t\,dS_t + \beta_t\,dB_t$ with no external cash flows. The informal hedge ratio $\Delta = V_S$ used here and the rigorous stock holding $\alpha_t = V_S$ of the next page are the same object: the two pages differ in how the bond leg is treated, not in the stock leg.


## Summary


The derivation proceeds in three steps:

1. **Itô's formula** gives the dynamics of $V(t, S_t)$, decomposed into drift and diffusion.
2. **Delta choice**: setting $\Delta = V_S$ eliminates the $dW$ term and cancels the physical drift $\mu$.
3. **No-arbitrage**: the resulting deterministic portfolio must earn rate $r$, yielding the PDE.

The Black–Scholes PDE with terminal condition $V(T, S) = \Phi(S)$ is a **backward parabolic equation**: it is solved from $t = T$ back to $t = 0$.

For alternative derivations that arrive at the same PDE via different reasoning, see [Black–Scholes PDE via Change of Numéraire](change_of_numeraire.md) (martingale condition on $V/S$) and [Risk-Neutral Pricing](../../ch01/numeraire_and_change_of_measure/numeraire_and_change_of_measure.md) (Feynman–Kac representation under the equivalent martingale measure).


## References

- Black, F. (1976). *The pricing of commodity contracts.* Journal of Financial Economics, 3(1–2), 167–179.

- Black, F. and Scholes, M. (1973). *The pricing of options and corporate liabilities.* Journal of Political Economy, 81(3), 637–654.

- Merton, R. C. (1973). *Theory of rational option pricing.* Bell Journal of Economics and Management Science, 4(1), 141–183.

- Shreve, S. E. (2004). *Stochastic Calculus for Finance II: Continuous-Time Models.* Springer.

- Björk, T. (2009). *Arbitrage Theory in Continuous Time.* 3rd edition, Oxford University Press.

---

## Exercises

**Exercise 1.** Carry out the full delta-hedging derivation using the short-option perspective. Starting from the portfolio $\Pi = -V + \Delta S$, apply Itô's lemma to $V(t, S_t)$, compute $d\Pi$, choose $\Delta = \partial V / \partial S$, and set $d\Pi = r\Pi \, dt$ to derive the Black-Scholes PDE.

??? success "Solution to Exercise 1"
    Define the portfolio $\Pi_t = -V(t, S_t) + \Delta\, S_t$. Apply Itô's formula to $V(t, S_t)$ with $dS_t = \mu S_t\, dt + \sigma S_t\, dW_t$:

    $$dV = \left(\frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right) dt + \sigma S \frac{\partial V}{\partial S}\, dW$$

    The change in portfolio value (holding $\Delta$ fixed over $[t, t+dt]$) is:

    $$d\Pi = -dV + \Delta\, dS = \left(-\frac{\partial V}{\partial t} - \mu S \frac{\partial V}{\partial S} - \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + \Delta \mu S\right) dt + \left(-\sigma S \frac{\partial V}{\partial S} + \Delta \sigma S\right) dW$$

    Choose $\Delta = \partial V / \partial S$ to eliminate the stochastic term:

    $$d\Pi = \left(-\frac{\partial V}{\partial t} - \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right) dt$$

    The portfolio is now locally riskless. By the no-arbitrage condition, it must earn the risk-free rate:

    $$d\Pi = r\Pi\, dt = r\!\left(-V + \frac{\partial V}{\partial S}\, S\right) dt$$

    Equating the two expressions for $d\Pi$:

    $$-\frac{\partial V}{\partial t} - \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} = -rV + rS\frac{\partial V}{\partial S}$$

    Rearranging:

    $$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0$$

    This is the Black–Scholes PDE.

---
**Exercise 2.** In the delta-hedging derivation, explain precisely where and how the physical drift $\mu$ cancels. If an investor has a different estimate $\hat{\mu} \neq \mu$ for the stock's expected return, does this affect the option price? Why or why not?

??? success "Solution to Exercise 2"
    The physical drift $\mu$ cancels at the step where we choose $\Delta = \partial V / \partial S$. In the expression for $d\Pi$, the drift contains the terms:

    $$-\mu S \frac{\partial V}{\partial S} + \Delta \mu S = \mu S\!\left(\Delta - \frac{\partial V}{\partial S}\right)$$

    Setting $\Delta = \partial V / \partial S$ makes this zero. The drift $\mu$ appears in both $dV$ (through the Itô expansion) and $\Delta\, dS$, and the choice of $\Delta$ eliminates $\mu$ from both the stochastic and the drift parts simultaneously.

    If an investor uses $\hat{\mu} \neq \mu$, this does **not** affect the option price. The reason is that the hedging argument eliminates all dependence on $\mu$: the delta hedge removes the stock's random fluctuations, and the no-arbitrage condition determines the portfolio's return as $r$. The resulting PDE depends only on $\sigma$ and $r$, not on $\mu$. Economically, two investors who disagree about $\mu$ but agree on $\sigma$ will agree on the option price, because the cost of replicating the option (through continuous delta hedging) depends on the magnitude of fluctuations ($\sigma$) but not their expected direction ($\mu$).

---
**Exercise 3.** The delta-hedging argument assumes $V \in C^{1,2}$, i.e., the option price is once differentiable in time and twice differentiable in the stock price. Identify a common option payoff for which this smoothness assumption fails at maturity, and explain how the Feynman-Kac representation handles this case even though the PDE derivation does not strictly apply.

??? success "Solution to Exercise 3"
    The smoothness assumption $V \in C^{1,2}$ fails at maturity for the standard **European call** (or put) payoff $\Phi(S) = (S - K)^+$. At $t = T$, the payoff function has a kink at $S = K$: the first derivative $\Phi'(S)$ jumps from 0 to 1 at $S = K$, so $\Phi''(S)$ does not exist at $S = K$ in the classical sense (it is a Dirac delta).

    This means the PDE derivation via Itô's formula does not strictly apply at the terminal time. However, the **Feynman–Kac representation** handles this case under mild conditions: the payoff $\Phi$ must be measurable, satisfy a polynomial growth bound (e.g., $|\Phi(S)| \leq C(1 + S^p)$ for some constants $C, p$) to ensure integrability against the transition density, and the coefficients of the SDE must be sufficiently regular (Lipschitz continuity suffices for GBM). The pricing formula

    $$V(t, S) = e^{-r(T-t)}\, \mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]$$

    is well-defined for any integrable payoff, and the resulting function $V(t, S)$ is smooth ($C^{1,2}$) for $t < T$ even when $\Phi$ is not smooth. The smoothing effect of the diffusion (the heat kernel) regularizes the terminal data: for any $t < T$, the probability of landing exactly at the kink $S_T = K$ is zero, and the conditional expectation is an integral against a smooth Gaussian density. The PDE holds for all $t < T$, and the non-smooth terminal condition is approached in the limit $t \to T^-$.

---
**Exercise 4.** Modify the delta-hedging derivation to account for a continuous dividend yield $q$ paid by the stock. Use the short-option portfolio $\Pi = -V + \Delta S$, noting that the long stock position earns dividend income $q \Delta S\, dt$. Show that the modified PDE is $\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + (r-q)S\frac{\partial V}{\partial S} - rV = 0$.

??? success "Solution to Exercise 4"
    With a continuous dividend yield $q$, the stock dynamics under $\mathbb{P}$ become $dS_t = (\mu - q)S_t\, dt + \sigma S_t\, dW_t$. Form the portfolio $\Pi = -V + \Delta S$. Since we are long $\Delta$ shares, we earn dividends at rate $q\Delta S\, dt$. The portfolio change is:

    $$d\Pi = -dV + \Delta\, dS + q\Delta S\, dt$$

    Apply Itô's formula to $V(t, S_t)$:

    $$dV = \left(\frac{\partial V}{\partial t} + (\mu - q)S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right)dt + \sigma S \frac{\partial V}{\partial S}\, dW$$

    Set $\Delta = \partial V/\partial S$ to eliminate the $dW$ term. After cancellation of $(\mu - q)S\, \partial V/\partial S$ from $-dV$ and $\Delta\, dS$:

    $$d\Pi = \left(-\frac{\partial V}{\partial t} - \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + qS\frac{\partial V}{\partial S}\right)dt$$

    The no-arbitrage condition $d\Pi = r\Pi\, dt = r(-V + S\partial V/\partial S)\, dt$ gives:

    $$-\frac{\partial V}{\partial t} - \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + qS\frac{\partial V}{\partial S} = -rV + rS\frac{\partial V}{\partial S}$$

    Rearranging:

    $$\frac{\partial V}{\partial t} + (r-q)S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0$$

    The dividend yield $q$ replaces $r$ by $r - q$ in the drift term, while the discounting term $-rV$ is unchanged.

---
**Exercise 5.** The derivation assumes continuous rebalancing. In practice, the portfolio is rebalanced at discrete intervals $\Delta t$. Show that the hedging error per step is approximately $\frac{1}{2}\Gamma(\Delta S)^2 - \frac{1}{2}\Gamma \sigma^2 S^2 \Delta t$, where $\Gamma = \frac{\partial^2 V}{\partial S^2}$. What is the expected hedging error, and what is its variance?

??? success "Solution to Exercise 5"
    Over a discrete time step $\Delta t$, the hedged portfolio is $\Pi = -V + \Delta S$ with $\Delta = \partial V/\partial S$ held fixed. The actual change in $V$ is:

    $$\Delta V \approx \frac{\partial V}{\partial t}\Delta t + \frac{\partial V}{\partial S}\Delta S + \frac{1}{2}\frac{\partial^2 V}{\partial S^2}(\Delta S)^2$$

    The portfolio change is $\Delta\Pi = -\Delta V + \frac{\partial V}{\partial S}\Delta S$, so:

    $$\Delta\Pi = -\frac{\partial V}{\partial t}\Delta t - \frac{1}{2}\Gamma(\Delta S)^2$$

    where $\Gamma = \partial^2 V/\partial S^2$. In the continuous limit, the Black–Scholes PDE gives $\frac{\partial V}{\partial t} = rV - rS\frac{\partial V}{\partial S} - \frac{1}{2}\sigma^2 S^2 \Gamma$, so the "theoretical" portfolio return is $r\Pi\, \Delta t$. Define the **hedging error** $\epsilon$ as the actual portfolio P&L minus the model-predicted risk-free return:

    $$\epsilon = \Delta\Pi - r\Pi\, \Delta t = -\frac{1}{2}\Gamma\bigl[(\Delta S)^2 - \sigma^2 S^2 \Delta t\bigr]$$

    A positive $\epsilon$ means the hedged portfolio earned more than the risk-free rate over the step; a negative $\epsilon$ means it earned less. The error is proportional to the difference between the realized quadratic variation $(\Delta S)^2$ and its expected value $\sigma^2 S^2 \Delta t$. For a dealer who is short the option (long gamma), $\Gamma > 0$ for a standard call or put, so the dealer loses ($\epsilon < 0$) when realized variance falls below implied variance, and gains when it exceeds it.

    **Expected hedging error:** Since $\mathbb{E}[(\Delta S)^2] = \sigma^2 S^2 \Delta t + O((\Delta t)^2)$, we have:

    $$\mathbb{E}[\epsilon] = 0 + O((\Delta t)^2)$$

    The expected hedging error is zero to leading order.

    **Variance of the hedging error:** We need $\text{Var}[(\Delta S)^2]$. Writing $\Delta S \approx \sigma S \sqrt{\Delta t}\, Z$ where $Z \sim \mathcal{N}(0,1)$ (to leading order), we get $(\Delta S)^2 \approx \sigma^2 S^2 \Delta t\, Z^2$. Since $\text{Var}[Z^2] = 2$:

    $$\text{Var}[\epsilon] = \frac{1}{4}\Gamma^2 \cdot \text{Var}[(\Delta S)^2] \approx \frac{1}{4}\Gamma^2 \cdot 2\sigma^4 S^4 (\Delta t)^2 = \frac{1}{2}\Gamma^2 \sigma^4 S^4 (\Delta t)^2$$

    The standard deviation of the hedging error per step is proportional to $\Gamma \sigma^2 S^2 \Delta t$, which decreases linearly with the rebalancing interval.

---
**Exercise 6.** Verify that $V = S$ (the stock) and $V = e^{r(t-T)}$ (a zero-coupon bond) both satisfy the Black-Scholes PDE. Interpret these "trivial" solutions in the context of the delta-hedging argument: what is the hedge ratio $\Delta$ for each?

??? success "Solution to Exercise 6"
    **Case 1: $V = S$ (the stock itself).**

    Compute the derivatives: $\partial V/\partial t = 0$, $\partial V/\partial S = 1$, $\partial^2 V/\partial S^2 = 0$. Substitute into the Black–Scholes PDE:

    $$0 + rS(1) + \frac{1}{2}\sigma^2 S^2(0) - rS = rS - rS = 0 \;\checkmark$$

    The hedge ratio is $\Delta = \partial V/\partial S = 1$. The hedging portfolio is $\Pi = -V + \Delta S = -S + S = 0$, which trivially earns $r \cdot 0 = 0$. Interpretation: to replicate the stock, hold the stock. No hedging is needed because the "derivative" is the underlying itself.

    **Case 2: $V = e^{r(t-T)}$ (a zero-coupon bond paying \$1 at time $T$).**

    Compute the derivatives: $\partial V/\partial t = re^{r(t-T)}= rV$, $\partial V/\partial S = 0$, $\partial^2 V/\partial S^2 = 0$. Substitute:

    $$rV + rS(0) + \frac{1}{2}\sigma^2 S^2(0) - rV = rV - rV = 0 \;\checkmark$$

    The hedge ratio is $\Delta = \partial V/\partial S = 0$. The hedging portfolio is $\Pi = -V + 0 \cdot S = -e^{r(t-T)}$, and $d\Pi = -rV\, dt = r\Pi\, dt$, confirming it earns the risk-free rate. Interpretation: a zero-coupon bond has no stock exposure, so no hedge is needed. The bond price grows deterministically at rate $r$.
