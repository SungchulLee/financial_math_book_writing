# Option Premium

Having defined what options are and characterized their payoffs at maturity, we now turn to a more fundamental question: how much should one pay to acquire an option *today*? The payoff at expiration is a random variable that depends on the future stock price, but the purchase happens now, at a definite price. This price — the **option premium** — is the central object of option pricing theory.

---

## Premium as the Price of Optionality

The **premium** is the price paid by the buyer to the writer at the time the option contract is initiated. In return, the buyer acquires the right (but not the obligation) to exercise the option at maturity. The writer, having received the premium, assumes the obligation to fulfill the contract if exercised.

It is essential to distinguish **premium** from **payoff**. The payoff of a European call at maturity is $(S_T - K)^+$, but this quantity is realized only at time $T$ and may be zero. The premium $C_0$ is paid at time $t = 0$ regardless of what happens later. An option can have a positive payoff yet still result in a net loss if the payoff does not exceed the premium:

$$
\text{Profit} = \text{Payoff} - \text{Premium} = (S_T - K)^+ - C_0
$$

A holder who pays \$12 for a call and receives a payoff of \$8 at maturity has exercised the option profitably in isolation, but has incurred a net loss of \$4. Conversely, letting an option expire worthless means losing exactly the premium — nothing more.

---

## Intrinsic Value and Time Value

The premium decomposes naturally into two components:

$$
\text{Premium} = \text{Intrinsic Value} + \text{Time Value}
$$

The **intrinsic value** is the payoff the option would yield if exercised immediately:

$$
\text{Intrinsic value (call)} = \max(S_t - K,\, 0) = (S_t - K)^+
$$

$$
\text{Intrinsic value (put)} = \max(K - S_t,\, 0) = (K - S_t)^+
$$

An in-the-money call with $S_t = 105$ and $K = 100$ has an intrinsic value of \$5. An out-of-the-money option has zero intrinsic value.

The **time value** (also called *extrinsic value*) is the remainder:

$$
\text{Time Value} = \text{Premium} - \text{Intrinsic Value}
$$

Time value reflects the possibility that the underlying price may move favorably before expiration. Even an out-of-the-money option commands a positive premium because there is still time for the stock price to cross the strike. As maturity approaches, this possibility diminishes, and the time value decays to zero — a phenomenon known as **time decay**. At expiration, the premium equals the intrinsic value exactly: all time value has vanished.

---

## Factors Affecting the Premium

Five quantities govern the option premium. Their influence can be summarized qualitatively before any pricing formula is derived.

| Factor | Symbol | Effect on call premium | Effect on put premium |
|---|---|---|---|
| Stock price | $S$ | Increases | Decreases |
| Strike price | $K$ | Decreases | Increases |
| Time to maturity | $T - t$ | Increases | Increases |
| Volatility | $\sigma$ | Increases | Increases |
| Risk-free rate | $r$ | Increases | Decreases |

The first two are immediate: a call becomes more valuable as the underlying rises (moving it deeper in the money) and less valuable as the strike rises (making exercise less likely). Greater time to maturity increases the premium for both calls and puts because it enlarges the range of possible outcomes.

Volatility $\sigma$ is perhaps the most important determinant. Higher volatility means larger potential swings in $S_T$, which benefits the option holder: upside gains grow while the downside remains bounded at zero payoff. This asymmetry makes options more valuable in volatile markets, a feature that will be made precise through the Black-Scholes formula.

The risk-free rate $r$ enters because exercising a call at maturity is equivalent to deferring purchase of the stock. A higher rate reduces the present value of the strike payment $K e^{-r(T-t)}$, making the call more valuable. The effect is reversed for puts.

---

## Premium as Discounted Expected Payoff

There is a deeper interpretation of the premium that foreshadows the risk-neutral pricing framework developed in subsequent sections. Under certain assumptions (no arbitrage, complete markets), the fair premium equals the **discounted expected payoff under a risk-neutral probability measure** $\mathbb{Q}$:

$$
C_0 = e^{-rT}\, \mathbb{E}^{\mathbb{Q}}\!\left[(S_T - K)^+\right]
$$

$$
P_0 = e^{-rT}\, \mathbb{E}^{\mathbb{Q}}\!\left[(K - S_T)^+\right]
$$

The measure $\mathbb{Q}$ is not the real-world probability — it is the unique measure under which discounted asset prices are martingales. We do not yet have the tools to construct $\mathbb{Q}$ or justify these formulas; that is the subject of later chapters. For now, the key insight is that the premium is not merely a market convention or a subjective assessment of risk. It is determined by a precise mathematical expectation, discounted at the risk-free rate. This expectation-based viewpoint transforms option pricing from a problem of forecasting into a problem of computing expectations — a shift that lies at the heart of mathematical finance.

---

## Exercises

**Exercise 1.** A European call option on a stock has strike $K = 50$ and premium $C_0 = \$6$. At maturity, the stock price is $S_T = 58$. Compute the payoff, the profit, and the return on the premium.

??? success "Solution to Exercise 1"
    The payoff is $(S_T - K)^+ = (58 - 50)^+ = \$8$.

    The profit is payoff minus premium: $8 - 6 = \$2$.

    The return on the premium is $\frac{2}{6} \approx 33.3\%$.

---

**Exercise 2.** Decompose the premium into intrinsic value and time value for the following European call options with strike $K = 100$: (a) $S_t = 110$, premium $= \$18$. (b) $S_t = 95$, premium $= \$4$. (c) $S_t = 100$, premium $= \$7$.

??? success "Solution to Exercise 2"
    (a) Intrinsic value $= (110 - 100)^+ = \$10$. Time value $= 18 - 10 = \$8$.

    (b) Intrinsic value $= (95 - 100)^+ = \$0$ (out of the money). Time value $= 4 - 0 = \$4$. The entire premium is time value.

    (c) Intrinsic value $= (100 - 100)^+ = \$0$ (at the money). Time value $= 7 - 0 = \$7$. Again, the entire premium is time value.

---

**Exercise 3.** Explain why an increase in volatility $\sigma$ raises the premium of both calls and puts, despite the fact that higher volatility increases the probability of both large gains and large losses for the underlying.

??? success "Solution to Exercise 3"
    The key is the asymmetry of the option payoff. For a call, the payoff is $(S_T - K)^+$: the holder benefits from upside moves beyond $K$ but loses nothing additional when $S_T$ falls below $K$ (the payoff is floored at zero). Higher volatility stretches the distribution of $S_T$, creating more probability mass in the profitable tail while the losing tail remains truncated at zero payoff.

    The same logic applies to puts via $(K - S_T)^+$: the put holder benefits from downside moves below $K$ and is unaffected by upside moves. Thus higher volatility always increases option value, regardless of type. This is a direct consequence of the convexity of the payoff function.

---

**Exercise 4.** A European put has strike $K = 80$, premium $P_0 = \$5$, and maturity $T = 1$ year. At what stock price $S_T$ does the holder break even? For what range of $S_T$ does the holder earn a positive profit?

??? success "Solution to Exercise 4"
    The profit of the put holder is $(K - S_T)^+ - P_0$. Break-even occurs when the profit is zero:

    $$
    (K - S_T)^+ - P_0 = 0
    $$

    For the put to have positive payoff, we need $S_T < K = 80$. In this region, $(K - S_T)^+ = K - S_T$, so:

    $$
    K - S_T = P_0 \implies S_T = K - P_0 = 80 - 5 = 75
    $$

    The holder breaks even at $S_T = \$75$. Positive profit occurs when $S_T < 75$.

---

**Exercise 5.** Suppose two European call options are identical except that option A has time to maturity $T_A = 3$ months and option B has $T_B = 9$ months. Using the decomposition into intrinsic and time value, argue that the premium of option B must be at least as large as the premium of option A, assuming both are on the same underlying with the same strike.

??? success "Solution to Exercise 5"
    Both options have the same underlying $S_t$ and the same strike $K$, so they share the same intrinsic value at time $t$:

    $$
    \text{Intrinsic value} = (S_t - K)^+
    $$

    The difference in premiums therefore comes entirely from the time value component. Option B has $T_B - t > T_A - t$, meaning there is more time remaining for the stock price to move favorably. A longer horizon weakly increases the set of favorable outcomes. Since time value is non-negative and increases with time to maturity (for European calls on non-dividend-paying stocks), option B has at least as much time value as option A. Therefore:

    $$
    C_B = \text{Intrinsic} + \text{Time value}_B \geq \text{Intrinsic} + \text{Time value}_A = C_A
    $$

    This argument relies on the fact that the underlying pays no dividends. For dividend-paying stocks, early exercise considerations (relevant for American options) can complicate the relationship.
