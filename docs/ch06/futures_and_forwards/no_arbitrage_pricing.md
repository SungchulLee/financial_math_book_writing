# No-Arbitrage Pricing of Forwards

## A 30-Second Toy Arbitrage

Before any formula, watch the mechanism on a single set of numbers. Suppose gold trades at $S_0 = \$1{,}000$ per ounce, the risk-free rate is $r = 5\%$ (continuously compounded), and a one-year forward is quoted at $F_0 = \$1{,}100$. A trader can execute three trades at time $t = 0$:

1. Sell one forward (zero cost; obligated to deliver one ounce at $T = 1$ for $\$1{,}100$).
2. Buy one ounce of gold spot, paying $\$1{,}000$.
3. Borrow $\$1{,}000$ at $5\%$, repayable at $1{,}000 \, e^{0.05} \approx \$1{,}051.27$ in one year.

Net cash at $t = 0$ is zero. At $t = 1$, the trader delivers the ounce of gold through the forward, collects $\$1{,}100$, and repays the $\$1{,}051.27$ loan, pocketing

$$
1{,}100 - 1{,}051.27 \approx \$48.73
$$

**risk-free**, regardless of whether gold ends at $\$500$ or $\$2{,}000$ at maturity. The spot price $S_T$ cancels because the long stock leg pays $S_T$ and the short forward leg pays $-S_T$.

The arbitrage exists because $F_0 = \$1{,}100$ is strictly greater than $S_0 \, e^{rT} = \$1{,}051.27$. The whole theory of forward pricing is the observation that **the only quote that destroys this profit is $F_0 = S_0 \, e^{rT}$**. Everything in this section is a generalization of the three lines above.

---

## The Principle Behind the Toy

The forward price is not chosen by negotiation or forecasting. It is determined by a single, unforgiving constraint: **no arbitrage**. If any other price were quoted, a trader could lock in a risk-free profit with zero net investment. The forward price is the unique number that eliminates this possibility.

!!! info "Key Idea"
    The forward price is the unique price that eliminates arbitrage. It is determined entirely by the current spot price $S_0$, the risk-free rate $r$, and the time to maturity $T$. No forecast of the asset's future value is needed.

**Interpretation**: The forward price is simply today's spot price carried forward at the risk-free rate — nothing more. All the information needed is already in $S_0$ and $r$.

---

## Replication Argument

The central tool is **replication**: we construct a portfolio of traded instruments whose payoff at maturity matches that of the forward contract. By no-arbitrage, the cost of this replicating portfolio must equal the cost of entering the forward.

Consider the following strategy executed at time $t = 0$:

| Action at $t = 0$ | Cash flow at $t = 0$ | Position at $t = T$ |
|---|---|---|
| Buy one share of stock | $-S_0$ | Own stock worth $S_T$ |
| Borrow $S_0$ at rate $r$ | $+S_0$ | Owe $S_0 e^{rT}$ |
| **Net** | **$0$** | $S_T - S_0 e^{rT}$ |

The net initial investment is zero. At maturity, the portfolio delivers

$$
\text{Net payoff} = S_T - S_0 e^{rT}
$$

This is exactly the payoff of a long forward contract with delivery price $F_0 = S_0 e^{rT}$. Since a forward contract also costs zero to enter, the delivery price must be

$$
\boxed{F_0 = S_0 \, e^{rT}}
$$

Any other delivery price would allow a risk-free profit, as we now show.

---

## Formal Derivation

Let $F_0$ denote the forward price (delivery price set at inception so that the contract has zero value). Let $S_0$ be the current spot price, $r$ the continuously compounded risk-free rate, and $T$ the time to maturity.

A forward contract with delivery price $F_0$ has payoff at maturity

$$
\text{Payoff} = S_T - F_0
$$

for the long party. We claim $F_0 = S_0 e^{rT}$. The proof proceeds by contradiction: if $F_0$ differs from $S_0 e^{rT}$ in either direction, an arbitrage exists.

---

## Case 1: Overpriced Forward

**Claim.** If $F_0 > S_0 e^{rT}$, then a risk-free profit can be locked in.

**Strategy.** At time $t = 0$:

1. **Sell** (short) one forward contract at delivery price $F_0$. (Zero cost.)
2. **Buy** one share of stock at price $S_0$.
3. **Borrow** $S_0$ at the risk-free rate $r$ for maturity $T$.

| | Cash flow at $t = 0$ | Cash flow at $t = T$ |
|---|---|---|
| Short forward | $0$ | $F_0 - S_T$ |
| Buy stock | $-S_0$ | $+S_T$ |
| Borrow $S_0$ | $+S_0$ | $-S_0 e^{rT}$ |
| **Total** | **$0$** | $F_0 - S_0 e^{rT}$ |

The net investment at $t = 0$ is zero. The net payoff at $t = T$ is

$$
F_0 - S_0 e^{rT} > 0
$$

This is a guaranteed positive profit from zero investment -- an arbitrage.

### Worked Example (Overpriced Forward)

Suppose $S_0 = \$100$, $r = 5\%$ per annum (continuously compounded), $T = 1$ year, and the quoted forward price is $F_0 = \$108$.

The theoretical forward price is

$$
S_0 e^{rT} = 100 \times e^{0.05 \times 1} = 100 \times 1.05127 = \$105.13
$$

Since $F_0 = 108 > 105.13 = S_0 e^{rT}$, the forward is overpriced. Execute the strategy above:

| | $t = 0$ | $t = 1$ |
|---|---|---|
| Short forward | $0$ | $108 - S_1$ |
| Buy stock | $-100$ | $+S_1$ |
| Borrow \$100 at 5% | $+100$ | $-105.13$ |
| **Total** | **$0$** | **$\$2.87$** |

Regardless of the stock price $S_1$ at maturity, the arbitrageur earns a risk-free profit of

$$
108 - 105.13 = \$2.87
$$

The stock price $S_1$ cancels out completely. The profit is locked in at inception.

---

## Case 2: Underpriced Forward

**Claim.** If $F_0 < S_0 e^{rT}$, then a risk-free profit can also be locked in.

**Strategy.** At time $t = 0$:

1. **Buy** (go long) one forward contract at delivery price $F_0$. (Zero cost.)
2. **Short sell** one share of stock, receiving $S_0$.
3. **Lend** (invest) $S_0$ at the risk-free rate $r$ for maturity $T$.

| | Cash flow at $t = 0$ | Cash flow at $t = T$ |
|---|---|---|
| Long forward | $0$ | $S_T - F_0$ |
| Short stock | $+S_0$ | $-S_T$ |
| Lend $S_0$ | $-S_0$ | $+S_0 e^{rT}$ |
| **Total** | **$0$** | $S_0 e^{rT} - F_0$ |

The net investment at $t = 0$ is zero. The net payoff at $t = T$ is

$$
S_0 e^{rT} - F_0 > 0
$$

Again, a guaranteed positive profit from zero investment.

### Worked Example (Underpriced Forward)

Using the same parameters ($S_0 = \$100$, $r = 5\%$, $T = 1$), suppose the quoted forward price is $F_0 = \$103$.

Since $F_0 = 103 < 105.13 = S_0 e^{rT}$, the forward is underpriced. Execute the reverse strategy:

| | $t = 0$ | $t = 1$ |
|---|---|---|
| Long forward | $0$ | $S_1 - 103$ |
| Short stock | $+100$ | $-S_1$ |
| Lend \$100 at 5% | $-100$ | $+105.13$ |
| **Total** | **$0$** | **$\$2.13$** |

The arbitrageur earns a risk-free profit of

$$
105.13 - 103 = \$2.13
$$

independent of $S_1$. Once again, the stock price cancels.

---

## Why the Drift Does Not Matter

A striking feature of the forward pricing formula

$$
F_0 = S_0 \, e^{rT}
$$

is what it does **not** contain. The expected growth rate $\mu$ of the stock -- often modeled as

$$
dS_t = \mu S_t \, dt + \sigma S_t \, dW_t
$$

under geometric Brownian motion -- is entirely absent. The forward price depends only on $S_0$, $r$, and $T$.

This is not a coincidence. It is a direct consequence of the replication argument. The hedging portfolio (buy stock, borrow cash) is constructed today using observed market prices. Its payoff at maturity is deterministic once $S_0$ and $r$ are known. No probability distribution for $S_T$ is needed, so neither $\mu$ nor $\sigma$ enters the formula.

Intuitively, any "optimistic" or "pessimistic" view about the stock's future is already reflected in today's spot price $S_0$. The forward price simply translates $S_0$ forward in time by the cost of financing.

---

## Connection to Risk-Neutral Pricing

Recall (see [§ Risk-Neutral Valuation Principle](../../ch04/risk_neutral/risk_neutral_valuation_principle.md)): under the risk-neutral measure $\mathbb{Q}$, the stock's drift is replaced by $r$, so $\mathbb{E}^{\mathbb{Q}}[S_T] = S_0 e^{rT}$. Comparing with the forward formula gives the identity

$$
F_0 = \mathbb{E}^{\mathbb{Q}}[S_T]
$$

The forward price equals the risk-neutral expectation of the future spot — a relationship that reappears throughout derivative pricing.

---

## Exercises

**Exercise 1.** A stock trades at $S_0 = \$50$. The continuously compounded risk-free rate is $r = 3\%$ and the forward maturity is $T = 0.5$ years. Compute the no-arbitrage forward price $F_0$.

??? success "Solution to Exercise 1"
    Applying the forward pricing formula:

    $$
    F_0 = S_0 \, e^{rT} = 50 \times e^{0.03 \times 0.5} = 50 \times e^{0.015} = 50 \times 1.01511 = \$50.76
    $$

---

**Exercise 2.** A stock trades at $S_0 = \$200$ and the continuously compounded risk-free rate is $r = 4\%$. A one-year forward contract on this stock is quoted at $F_0 = \$212$. Construct an explicit arbitrage strategy and compute the risk-free profit.

??? success "Solution to Exercise 2"
    The theoretical forward price is

    $$
    S_0 e^{rT} = 200 \times e^{0.04} = 200 \times 1.04081 = \$208.16
    $$

    Since $F_0 = 212 > 208.16$, the forward is overpriced. Execute the "Case 1" strategy:

    - Sell the forward at \$212
    - Buy the stock at \$200
    - Borrow \$200 at 4% for one year

    At maturity, deliver the stock through the forward and receive \$212, then repay the loan of \$208.16. The risk-free profit is

    $$
    212 - 208.16 = \$3.84
    $$

    independent of the stock price at maturity.

---

**Exercise 3.** A stock trades at $S_0 = \$80$ and the continuously compounded risk-free rate is $r = 6\%$. A six-month forward is quoted at $F_0 = \$81$. Construct an explicit arbitrage strategy and compute the risk-free profit.

??? success "Solution to Exercise 3"
    The theoretical forward price is

    $$
    S_0 e^{rT} = 80 \times e^{0.06 \times 0.5} = 80 \times e^{0.03} = 80 \times 1.03045 = \$82.44
    $$

    Since $F_0 = 81 < 82.44$, the forward is underpriced. Execute the "Case 2" strategy:

    - Buy the forward at \$81
    - Short sell the stock, receiving \$80
    - Lend \$80 at 6% for six months

    At maturity, receive \$82.44 from the investment, pay \$81 through the forward to acquire the stock, and return it to close the short position. The risk-free profit is

    $$
    82.44 - 81 = \$1.44
    $$

    independent of the stock price at maturity.

---

**Exercise 4.** Explain why the expected return $\mu$ of the stock does not appear in the forward pricing formula $F_0 = S_0 e^{rT}$. A friend argues: "If the stock is expected to grow at 15% per year, the forward price should be higher than if the stock is expected to grow at 5%." Identify the flaw in this reasoning.

??? success "Solution to Exercise 4"
    The forward price is determined by a **replication argument**, not by expectations about future prices. The replicating portfolio -- buy stock at $S_0$ and borrow $S_0$ at rate $r$ -- costs zero today and delivers $S_T - S_0 e^{rT}$ at maturity, regardless of the stock's drift $\mu$.

    The flaw in the friend's reasoning is that differing growth expectations are already priced into the **current** spot price $S_0$. If market participants collectively expect 15% growth, they bid up $S_0$ today. The forward price $S_0 e^{rT}$ then reflects this higher starting point. There is no additional adjustment needed for $\mu$ because $S_0$ already incorporates all available information and expectations. The forward formula only adds the time value of money -- the cost of financing the purchase from now until maturity.

---

**Exercise 5.** Using the risk-neutral pricing identity $F_0 = \mathbb{E}^{\mathbb{Q}}[S_T]$, verify the forward pricing formula. Assume the stock follows geometric Brownian motion under $\mathbb{Q}$:

$$
dS_t = r S_t \, dt + \sigma S_t \, dW_t^{\mathbb{Q}}
$$

??? success "Solution to Exercise 5"
    Under the risk-neutral measure $\mathbb{Q}$, the solution to the GBM is

    $$
    S_T = S_0 \exp\!\left(\left(r - \tfrac{1}{2}\sigma^2\right)T + \sigma W_T^{\mathbb{Q}}\right)
    $$

    Taking the expectation under $\mathbb{Q}$ and using the fact that $W_T^{\mathbb{Q}} \sim \mathcal{N}(0, T)$:

    $$
    \mathbb{E}^{\mathbb{Q}}[S_T] = S_0 \exp\!\left(\left(r - \tfrac{1}{2}\sigma^2\right)T\right) \cdot \mathbb{E}^{\mathbb{Q}}\!\left[e^{\sigma W_T^{\mathbb{Q}}}\right]
    $$

    The moment generating function of a normal random variable $Z \sim \mathcal{N}(0, T)$ gives $\mathbb{E}[e^{\sigma Z}] = e^{\frac{1}{2}\sigma^2 T}$. Therefore:

    $$
    \mathbb{E}^{\mathbb{Q}}[S_T] = S_0 \exp\!\left(\left(r - \tfrac{1}{2}\sigma^2\right)T + \tfrac{1}{2}\sigma^2 T\right) = S_0 \, e^{rT} = F_0
    $$

    The $\sigma^2$ terms cancel, confirming that the forward price depends only on $S_0$, $r$, and $T$ -- not on volatility. $\square$

---

**Exercise 6.** A non-dividend-paying stock trades at $S_0 = \$120$ and the continuously compounded risk-free rate is $r = 5\%$. A trader observes that the 3-month forward is quoted at $F_0 = \$121.00$ while the 6-month forward is quoted at $F_0 = \$123.50$. Identify whether each quote is overpriced, underpriced, or fair, and describe any arbitrage available.

??? success "Solution to Exercise 6"
    Theoretical forward prices:

    $$
    F_0^{(3m)} = 120 \, e^{0.05 \times 0.25} = 120 \, e^{0.0125} \approx \$121.51
    $$

    $$
    F_0^{(6m)} = 120 \, e^{0.05 \times 0.5} = 120 \, e^{0.025} \approx \$123.04
    $$

    The 3-month forward quote $\$121.00 < 121.51$ is **underpriced**: execute Case 2 (long forward, short stock, lend) for a risk-free profit of $\$0.51$.

    The 6-month forward quote $\$123.50 > 123.04$ is **overpriced**: execute Case 1 (short forward, buy stock, borrow) for a risk-free profit of $\$0.46$.

    Both arbitrages can be combined into a single calendar-spread trade with combined profit of about $\$0.97$ per share at the respective maturities.
