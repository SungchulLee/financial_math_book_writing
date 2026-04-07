# From Forwards to Options

!!! tip "Key Idea"
    Forwards are easy because the payoff is linear. Options are hard because the payoff is nonlinear. This single distinction---linearity versus nonlinearity---explains why forward pricing requires only algebra and static replication, while option pricing demands the full machinery of stochastic calculus.

The previous sections developed forward and futures pricing from first principles: no-arbitrage, cost of carry, and the replication argument. Every result rested on the fact that the forward payoff $S_T - K$ is a **linear** function of the terminal stock price. This linearity made replication simple and pricing elegant. We now examine what happens when linearity breaks down, and why that breakdown leads directly to the Black-Scholes theory.

---

## Linear Payoff and Static Replication

The forward contract pays $S_T - K$ at maturity. This payoff is linear in $S_T$: for every \$1 increase in the stock price, the forward's value increases by exactly \$1. The replication strategy follows immediately from this linearity.

To replicate a long forward with delivery price $K$ and maturity $T$:

1. **Buy one share** of the underlying at cost $S_0$.
2. **Borrow** $Ke^{-rT}$ at the risk-free rate.

At maturity, the share is worth $S_T$ and the loan requires repayment of $K$, producing a net payoff of $S_T - K$. This is a **static** replication: the portfolio is constructed once at time $0$ and held without adjustment until maturity. The no-arbitrage forward price then follows:

$$
F_0 = S_0 e^{rT}
$$

The crucial observation is that this derivation required no assumptions about the stock's volatility $\sigma$, no model for the stock price dynamics, and no stochastic calculus. Linearity of the payoff made the problem purely algebraic.

---

## Nonlinear Payoff and the Need for Dynamic Replication

Now consider a European call option with the same strike $K$ and maturity $T$. Its payoff is

$$
(S_T - K)^+ = \max(S_T - K, \, 0)
$$

This payoff is **nonlinear** in $S_T$. The $\max$ operator introduces a kink at $S_T = K$: the payoff rises one-for-one with $S_T$ above the strike but is flat (zero) below it. Unlike the forward, a static portfolio of stock and bonds cannot replicate this kinked payoff for all possible values of $S_T$.

Why not? A portfolio of $\phi$ shares and $\psi$ bonds has terminal value $\phi S_T + \psi e^{rT}$, which is always linear in $S_T$. No fixed choice of $(\phi, \psi)$ can match a function that is linear on one piece and flat on another. The replication strategy must therefore **change over time** as the stock price moves---it must be **dynamic**.

In a dynamic replication strategy, the portfolio weights $\phi_t$ and $\psi_t$ are adjusted continuously (or at least frequently) in response to changes in $S_T$. At each instant, the portfolio is rebalanced to maintain a local match with the option's payoff profile. This continuous adjustment is called **delta hedging**, and it is the mechanism through which option pricing becomes tied to the volatility $\sigma$ of the underlying asset.

---

## Put-Call Parity: The Bridge

The connection between the linear world of forwards and the nonlinear world of options is made precise by **put-call parity**. For European options on a non-dividend-paying stock:

$$
C - P = S_0 - Ke^{-rT}
$$

where $C$ is the call price, $P$ is the put price, $S_0$ is the current stock price, and $K$ is the common strike. The right-hand side is exactly the value of a forward contract with delivery price $K$:

$$
C - P = e^{-rT}(F_0 - K)
$$

Put-call parity says that a **long call and short put** with the same strike and maturity replicates a forward. This is not surprising once we observe the payoff identity:

$$
(S_T - K)^+ - (K - S_T)^+ = S_T - K
$$

The nonlinear pieces---the call and the put---combine to produce a linear payoff. Individually, each option is nonlinear and difficult to price. Together, their nonlinearities cancel perfectly. Put-call parity is therefore the algebraic bridge between forward pricing and option pricing: it shows that the *difference* between a call and a put is a forward, and the *individual* prices carry the additional complexity of nonlinearity.

---

## Convexity, Gamma, and Continuous Hedging

The kink in the call payoff $(S_T - K)^+$ at $S_T = K$ is the source of all the additional mathematical complexity in option pricing. To understand why, consider the option's value $C(S, t)$ as a function of the current stock price $S$.

Far above the strike, the call behaves almost like a forward: $C \approx S - Ke^{-r(T-t)}$, and the hedge ratio (delta) is close to 1. Far below the strike, the call is nearly worthless and delta is close to 0. Near the strike, delta transitions rapidly from 0 to 1. The rate of this transition is measured by **gamma**:

$$
\Gamma = \frac{\partial^2 C}{\partial S^2}
$$

Gamma is largest near the strike and near expiration. It quantifies the **convexity** (curvature) of the option price with respect to the stock price. A forward contract, by contrast, has $\Gamma = 0$ everywhere because its value is linear in $S$.

Nonzero gamma means that delta changes as the stock price moves, which is precisely why the hedge must be continuously adjusted. Each small move $dS$ in the stock price changes the option's delta by approximately $\Gamma \, dS$, requiring a rebalancing trade of $\Gamma \, dS$ shares. The cost of maintaining this hedge over the option's life depends on how much the stock price fluctuates---that is, on the **volatility** $\sigma$.

This is the fundamental reason that forward prices depend on $r$ alone while option prices depend on both $r$ and $\sigma$:

- **Forwards**: $\Gamma = 0$, static hedge, price depends on $r$ only.
- **Options**: $\Gamma \neq 0$, dynamic hedge, price depends on $r$ and $\sigma$.

---

## What Comes Next

!!! quote "Big Picture"
    Forward pricing is the prototype for all derivative pricing. The principle is always the same: replicate the payoff, and no-arbitrage determines the price. For forwards, replication is static and the mathematics is elementary. Options add nonlinearity, which demands dynamic replication---and with it, the full machinery of stochastic calculus, Ito's lemma, and the Black-Scholes PDE.

The table below summarizes the conceptual transition from forwards to options:

| | **Forward** | **Option** |
|---|---|---|
| Payoff | $S_T - K$ (linear) | $(S_T - K)^+$ (nonlinear) |
| Replication | Static | Dynamic (delta hedging) |
| Key parameters | $r, T, S_0$ | $r, T, S_0, \sigma$ |
| Gamma | $0$ | $> 0$ (near the strike) |
| Pricing method | Algebraic no-arbitrage | Black-Scholes PDE / risk-neutral expectation |

!!! note "Section Summary (Futures and Forwards)"
    Forward pricing shows that derivative values can be determined entirely by replication under no-arbitrage. The payoff is linear, the hedge is static, and the mathematics is algebraic. This simplicity is not a limitation but a foundation: it reveals the core principle that price is determined by replication, not expectation. Options extend this principle to nonlinear payoffs, where replication becomes dynamic and pricing depends on volatility — the subject of the sections that follow.

---

## Exercises

**Exercise 1.** A European call and a European put on a non-dividend-paying stock share strike $K = 50$ and maturity $T = 1$ year. The current stock price is $S_0 = 52$ and the continuously compounded risk-free rate is $r = 0.04$. If the call is priced at $C = 5.50$, use put-call parity to determine the put price $P$.

??? success "Solution to Exercise 1"
    Put-call parity states

    $$
    C - P = S_0 - Ke^{-rT}
    $$

    Substituting the given values:

    $$
    5.50 - P = 52 - 50e^{-0.04} = 52 - 50 \times 0.9608 = 52 - 48.04 = 3.96
    $$

    Therefore

    $$
    P = 5.50 - 3.96 = 1.54
    $$

---

**Exercise 2.** Explain why a static portfolio consisting of $\phi$ shares of stock and $\psi$ units of a zero-coupon bond cannot replicate the payoff $(S_T - K)^+$ for all possible values of $S_T$. Your argument should be precise: state what the portfolio pays at maturity and why it cannot match the option payoff on both regions $S_T > K$ and $S_T \leq K$ simultaneously.

??? success "Solution to Exercise 2"
    A static portfolio of $\phi$ shares and $\psi$ bonds has terminal value

    $$
    V_T = \phi S_T + \psi e^{rT}
    $$

    which is a linear (affine) function of $S_T$. Suppose this portfolio replicates $(S_T - K)^+$ for all $S_T \geq 0$.

    For $S_T > K$, the payoff is $S_T - K$, so we need $\phi S_T + \psi e^{rT} = S_T - K$, giving $\phi = 1$ and $\psi = -Ke^{-rT}$.

    For $S_T \leq K$, the payoff is $0$, so we need $\phi S_T + \psi e^{rT} = 0$ for all $S_T \in [0, K]$. This requires $\phi = 0$ and $\psi = 0$.

    These two systems are contradictory: we cannot have $\phi = 1$ and $\phi = 0$ simultaneously. Therefore no static portfolio of stock and bonds can replicate the call payoff. The kink at $S_T = K$ makes the payoff piecewise linear with different slopes on the two regions, which a single affine function cannot match. $\square$

---

**Exercise 3.** Show that the payoff identity $(S_T - K)^+ - (K - S_T)^+ = S_T - K$ holds for all $S_T \geq 0$ by considering the two cases $S_T \geq K$ and $S_T < K$ separately.

??? success "Solution to Exercise 3"
    **Case 1: $S_T \geq K$.**

    In this case $(S_T - K)^+ = S_T - K$ and $(K - S_T)^+ = 0$, so

    $$
    (S_T - K)^+ - (K - S_T)^+ = (S_T - K) - 0 = S_T - K
    $$

    **Case 2: $S_T < K$.**

    In this case $(S_T - K)^+ = 0$ and $(K - S_T)^+ = K - S_T$, so

    $$
    (S_T - K)^+ - (K - S_T)^+ = 0 - (K - S_T) = S_T - K
    $$

    In both cases the result is $S_T - K$, establishing the identity for all $S_T \geq 0$. $\square$

---

**Exercise 4.** A forward contract has $\Gamma = 0$, while a European call option has $\Gamma > 0$ near the strike. Explain in plain language why $\Gamma = 0$ implies that a forward can be hedged with a static portfolio, and why $\Gamma > 0$ implies that an option requires continuous rebalancing. Relate your answer to the dependence (or independence) of the price on volatility $\sigma$.

??? success "Solution to Exercise 4"
    Gamma measures how much delta (the hedge ratio) changes when the stock price moves. For a forward, $\Gamma = 0$ means delta is constant: it is always exactly 1. A hedge of one share of stock perfectly offsets the forward's exposure to stock price movements at all times, regardless of where the stock trades. Since the hedge never needs adjustment, it is static, and the cost of maintaining it does not depend on how much the stock price fluctuates. This is why the forward price is independent of $\sigma$.

    For a call option, $\Gamma > 0$ means delta changes as the stock moves. When the stock rises, delta increases (the option becomes more sensitive to the stock), and the hedger must buy additional shares. When the stock falls, delta decreases, and the hedger must sell shares. The frequency and magnitude of these adjustments depend directly on how much the stock price moves---that is, on volatility $\sigma$. Higher volatility means more frequent and larger rebalancing trades, which in turn means higher hedging costs. These costs are reflected in the option price. This is why the call price depends on $\sigma$: volatility determines the cost of the dynamic hedge required to replicate the nonlinear payoff. $\square$
