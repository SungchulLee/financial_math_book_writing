# From Market to No-Arbitrage

An option is worth something — but how much? The previous sections defined payoffs, premiums, and trading mechanics. None of them answered the central question: **what is the correct price of an option today?** This question is not merely academic. If the market price deviates from the theoretically correct value, an arbitrageur can lock in a guaranteed profit with zero net investment. The purpose of option pricing theory is to determine the unique price at which no such opportunity exists.

This section shows, through concrete examples, that mispriced options create arbitrage. It then introduces the key idea — replicating an option's payoff with a portfolio of stock and cash — that transforms the pricing problem into a problem of differential equations.

---

## Mispricing Creates Arbitrage

**Key idea**: The option price is determined by replication, not by belief about where the stock is headed.

Consider a European call option with strike $K = 100$ maturing in one period. Suppose the stock currently trades at $S_0 = 100$, the risk-free rate is $r = 5\%$ per period, and the stock can move to either $S_u = 120$ or $S_d = 90$ at maturity. The call payoff is

$$
C_T = \max(S_T - K, 0) = \begin{cases} 20 & \text{if } S_T = 120 \\ 0 & \text{if } S_T = 90 \end{cases}
$$

We can replicate this payoff exactly by holding $\Delta$ shares of stock and lending $B$ dollars at the risk-free rate. The replication conditions are

$$
\Delta \cdot 120 + B \cdot 1.05 = 20
$$

$$
\Delta \cdot 90 + B \cdot 1.05 = 0
$$

Subtracting the second equation from the first gives $30\Delta = 20$, so $\Delta = 2/3$. Substituting back yields $B = -60/1.05 \approx -57.14$. The replicating portfolio costs

$$
C_0 = \Delta \cdot S_0 + B = \frac{2}{3} \cdot 100 - \frac{60}{1.05} \approx 9.52
$$

This is the only arbitrage-free price. If the market quotes any other price, a riskless profit is available:

- **If the market price $C^{\text{mkt}} > 9.52$**: Sell the call for $C^{\text{mkt}}$ and buy the replicating portfolio for \$9.52. The portfolio matches the call's payoff in every state, so the obligation is perfectly hedged. The difference $C^{\text{mkt}} - 9.52 > 0$ is a guaranteed profit.

- **If the market price $C^{\text{mkt}} < 9.52$**: Buy the call for $C^{\text{mkt}}$ and sell the replicating portfolio (short $2/3$ shares, lend \$57.14). At maturity, the call payoff exactly offsets the portfolio obligation. The difference $9.52 - C^{\text{mkt}} > 0$ is a guaranteed profit.

In both cases the profit is locked in at time zero with no risk. This is the hallmark of **arbitrage**: a self-financing strategy that starts with zero wealth and ends with positive wealth in at least one state, with no possibility of loss.

---

## Replication as a Pricing Principle

The example above illustrates a profound idea: the option price is determined not by investors' views on whether the stock will go up or down, but by the cost of replicating the option's payoff using traded instruments. This replication perspective and the risk-neutral expectation $V_0 = e^{-rT}\mathbb{E}^{\mathbb{Q}}[\text{Payoff}]$ introduced in the premium section are **mathematically equivalent** — two representations of the same no-arbitrage principle. The drift $\mu$ of the stock is irrelevant — only the volatility (which determines the range of possible outcomes) and the risk-free rate (which determines the cost of financing) matter.

In continuous time, the stock price is modeled by geometric Brownian motion, and the replicating portfolio must be adjusted continuously. At each instant $t$, the portfolio holds $\Delta_t$ shares of stock and invests the remainder in the risk-free bond. The quantity

$$
\Delta_t = \frac{\partial V}{\partial S}(t, S_t)
$$

is called the **delta** of the option, where $V(t, S)$ denotes the option price as a function of time and stock price. This is the continuous-time analogue of the ratio $\Delta = 2/3$ computed above: it measures the sensitivity of the option price to movements in the underlying, and it tells the hedger exactly how many shares to hold.

The strategy of continuously adjusting the stock position to maintain $\Delta_t$ shares is called **delta hedging**. If the option price function $V$ is correct, then the delta-hedged portfolio is locally riskless — its instantaneous return equals the risk-free rate. If $V$ is incorrect, the hedge leaks money (or prints it), creating arbitrage.

---

## The Road to a Differential Equation

The requirement that the delta-hedged portfolio earn the risk-free rate is not merely a financial condition — it is a **mathematical constraint** on the function $V(t, S)$. Applying Ito's lemma to $V$ and imposing the no-arbitrage condition produces a partial differential equation that $V$ must satisfy:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
$$

This is the **Black-Scholes PDE**. Every arbitrage-free option price — call, put, digital, or otherwise — must satisfy this equation. The specific contract enters only through the terminal condition $V(T, S) = \text{payoff}(S)$ and, where applicable, boundary conditions.

The next sections develop this derivation rigorously: we formalize the self-financing condition, apply Ito calculus to the hedged portfolio, and show that the no-arbitrage requirement leaves no room for the drift $\mu$ — only $r$, $\sigma$, and the payoff determine the price.

!!! note "Big Picture"
    Options derive their value from asymmetric payoffs. Their prices are determined not by beliefs about the future, but by the cost of replicating those payoffs in the market. This equivalence between replication and expectation transforms pricing into a mathematical problem — leading directly to the Black-Scholes equation.

---

## Exercises

**Exercise 1.** In the one-period binomial model above ($S_0 = 100$, $S_u = 120$, $S_d = 90$, $r = 5\%$), find the arbitrage-free price of a European **put** with strike $K = 100$.

??? success "Solution to Exercise 1"
    The put payoff is $P_T = \max(K - S_T, 0)$: it pays $0$ if $S_T = 120$ and $10$ if $S_T = 90$.

    The replication conditions are

    $$
    \Delta \cdot 120 + B \cdot 1.05 = 0
    $$

    $$
    \Delta \cdot 90 + B \cdot 1.05 = 10
    $$

    Subtracting the first from the second: $-30\Delta = 10$, so $\Delta = -1/3$.
    Substituting back: $B = (120/3)/1.05 = 40/1.05 \approx 38.10$.

    The put price is

    $$
    P_0 = \Delta \cdot S_0 + B = -\frac{1}{3}\cdot 100 + \frac{40}{1.05} = -33.33 + 38.10 \approx 4.76
    $$

---

**Exercise 2.** Using the call and put prices from Exercise 1 and the text, verify that **put-call parity** holds: $C_0 - P_0 = S_0 - K\,e^{-rT}$, where $e^{-rT} = 1/1.05$ in this one-period model.

??? success "Solution to Exercise 2"
    From the text, $C_0 \approx 9.52$. From Exercise 1, $P_0 \approx 4.76$.

    $$
    C_0 - P_0 \approx 9.52 - 4.76 = 4.76
    $$

    On the other side:

    $$
    S_0 - \frac{K}{1.05} = 100 - \frac{100}{1.05} = 100 - 95.24 = 4.76
    $$

    The two sides agree, confirming put-call parity. This is not a coincidence — it follows from the linearity of the replication argument. Any pair of call and put prices that violate this relation admits arbitrage.

---

**Exercise 3.** Suppose the market quotes the call from the text at \$12 instead of \$9.52. Describe the exact arbitrage strategy and compute the profit in each state.

??? success "Solution to Exercise 3"
    The call is overpriced ($12 > 9.52$), so we sell the call and buy the replicating portfolio.

    **At time 0**: Sell the call, receive \$12. Buy $2/3$ shares at \$100 each, costing \$66.67. Borrow \$54.67 at $5\%$ (net cash flow: $12 - 66.67 + 54.67 = 0$).

    More precisely, the replicating portfolio costs $C_0 = 9.52$, so we invest \$9.52 in the replicating portfolio and pocket $12 - 9.52 = \$2.48$, which we invest at the risk-free rate.

    **If $S_T = 120$**: The call is exercised against us; we owe $20$. The replicating portfolio pays $(2/3)(120) + (-60/1.05)(1.05) = 80 - 60 = 20$. Net from hedge: $0$. We still have $2.48 \times 1.05 = \$2.60$ from the initial profit.

    **If $S_T = 90$**: The call expires worthless. The replicating portfolio pays $(2/3)(90) + (-60/1.05)(1.05) = 60 - 60 = 0$. We still have $2.48 \times 1.05 = \$2.60$.

    In both states, the profit is \$2.60. This is a riskless arbitrage.

---

**Exercise 4.** Explain in your own words why the stock's expected return $\mu$ does not appear in the arbitrage-free option price. What parameters **do** determine the price?

??? success "Solution to Exercise 4"
    The arbitrage-free price is determined by replication: we find a portfolio of stock and bond that matches the option payoff in every state. The cost of this portfolio depends on (i) the current stock price $S_0$, (ii) the range of possible future stock prices (determined by $\sigma$), (iii) the risk-free rate $r$ (which determines the cost of borrowing in the replicating portfolio), and (iv) the strike $K$ and maturity $T$ (which determine the payoff).

    The drift $\mu$ does not appear because the replicating portfolio matches the option in **every** state, regardless of which state is more likely. An optimistic investor (high $\mu$) and a pessimistic investor (low $\mu$) must agree on the option price, because any deviation from the replication cost creates an arbitrage that neither investor's beliefs can override.

    The parameters that determine the price are: $S_0$, $K$, $T$, $r$, and $\sigma$.

---

**Exercise 5.** In the continuous-time setting, the delta of a European call satisfies $0 \leq \Delta_t \leq 1$. Give an intuitive explanation for each bound. What does $\Delta_t \approx 1$ mean for the replicating portfolio?

??? success "Solution to Exercise 5"
    The call payoff $(S_T - K)^+$ is a non-decreasing function of $S_T$ (higher stock price means higher payoff), so the option price $V$ is non-decreasing in $S$. This gives $\Delta_t = \partial V / \partial S \geq 0$.

    The call payoff increases at most dollar-for-dollar with the stock price (the slope of $(S_T - K)^+$ is at most $1$), so the option price cannot increase faster than the stock price itself. This gives $\Delta_t \leq 1$.

    When $\Delta_t \approx 1$, the option is deep in-the-money and behaves almost like the stock itself. The replicating portfolio holds close to one full share and a large short bond position (borrowing nearly $Ke^{-r(T-t)}$), reflecting the near-certainty that the option will be exercised.
