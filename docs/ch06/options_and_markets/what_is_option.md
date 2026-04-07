# What is an Option?

An option is a financial derivative giving the holder the **right, but not the obligation**, to buy or sell an underlying asset at a predetermined price. This asymmetry — the holder chooses, the writer must comply — is the defining feature of options and the source of their mathematical richness.

---

## Call and Put Options

There are two fundamental types:

**Call option**: The right to **buy** the underlying asset at the strike price $K$ on or before the maturity date $T$.

**Put option**: The right to **sell** the underlying asset at the strike price $K$ on or before the maturity date $T$.

| | Call | Put |
|---|---|---|
| Holder's right | Buy at $K$ | Sell at $K$ |
| Holder benefits when | $S_T > K$ | $S_T < K$ |
| Maximum loss (holder) | Premium paid | Premium paid |

---

## Contract Terms

Every option contract specifies:

- **Underlying asset**: The stock, index, commodity, or other instrument the option is written on
- **Strike price** $K$: The predetermined price at which the holder may buy (call) or sell (put)
- **Maturity** $T$: The date at which the option expires
- **Exercise style**: European (exercise only at $T$) or American (exercise at any time $t \leq T$)

Throughout this text, we focus primarily on **European options**, which can only be exercised at maturity. This restriction is not just a simplification — it makes the pricing problem analytically tractable and leads directly to the Black-Scholes formula.

---

## Buyer vs Writer

Every option trade has two sides:

**Buyer (holder)**: Pays the premium upfront. Has the right to exercise. Maximum loss is the premium.

**Writer (seller)**: Receives the premium. Is obligated to fulfill the contract if the holder exercises. Faces potentially unlimited loss (for a naked call writer).

This asymmetry explains why writers must post **margin** — a deposit guaranteeing their ability to meet the obligation. The buyer's loss is bounded; the writer's is not.

---

## Moneyness

An option's relationship to the current stock price is classified as:

| Classification | Call ($S$ vs $K$) | Put ($S$ vs $K$) | Intrinsic value |
|---|---|---|---|
| **In-the-money (ITM)** | $S > K$ | $S < K$ | Positive |
| **At-the-money (ATM)** | $S \approx K$ | $S \approx K$ | Near zero |
| **Out-of-the-money (OTM)** | $S < K$ | $S > K$ | Zero |

Moneyness determines how sensitive an option is to changes in the underlying and plays a central role in the behavior of the Greeks.

---

## Exercises

**Exercise 1.** A European call option has strike $K = 100$ and maturity $T = 1$ year. At maturity, the stock price is $S_T = 115$. Should the holder exercise? What is the profit if the premium paid was \$8?

??? success "Solution to Exercise 1"
    The holder should exercise because $S_T = 115 > K = 100$. By exercising, the holder buys the stock at \$100 and can immediately sell at \$115, receiving a payoff of $S_T - K = 15$.

    The profit is payoff minus premium: $15 - 8 = \$7$.

---

**Exercise 2.** A European put option has strike $K = 50$ and maturity $T = 6$ months. At maturity, $S_T = 42$. What is the payoff? If $S_T = 55$ instead, what is the payoff?

??? success "Solution to Exercise 2"
    When $S_T = 42 < K = 50$: the holder exercises, selling at \$50 an asset worth \$42. Payoff $= K - S_T = 50 - 42 = \$8$.

    When $S_T = 55 > K = 50$: the holder does not exercise (selling at \$50 is worse than selling at the market price \$55). Payoff $= 0$.

---

**Exercise 3.** Explain why the maximum loss for the buyer of a call option is the premium paid, while the maximum loss for the writer of a naked call is theoretically unlimited. Relate this asymmetry to the option's payoff structure.

??? success "Solution to Exercise 3"
    The buyer pays the premium $C_0$ upfront. At maturity, the payoff is $(S_T - K)^+ \geq 0$. The worst case is $S_T \leq K$, where the payoff is zero and the buyer loses only the premium $C_0$.

    The writer receives $C_0$ but is obligated to pay $(S_T - K)^+$ at maturity. Since $S_T$ has no upper bound, neither does the writer's obligation. If $S_T \to \infty$, the writer's loss $S_T - K - C_0 \to \infty$. This unbounded loss potential is why naked call writing is considered one of the riskiest positions in finance.

---

**Exercise 4.** Classify the following options as ITM, ATM, or OTM: (a) Call with $K = 100$, current $S = 105$. (b) Put with $K = 80$, current $S = 80$. (c) Call with $K = 60$, current $S = 45$. (d) Put with $K = 70$, current $S = 55$.

??? success "Solution to Exercise 4"
    (a) Call with $S = 105 > K = 100$: **ITM** (the call would have positive payoff if exercised now).

    (b) Put with $S = 80 = K = 80$: **ATM** (the put is at the boundary of having value).

    (c) Call with $S = 45 < K = 60$: **OTM** (exercising would mean buying at \$60 what is worth \$45).

    (d) Put with $S = 55 < K = 70$: **ITM** (the holder could sell at \$70 what is worth \$55, payoff $= 15$).
