# Option Premium

Picture an investor on Monday morning. A call with strike \$100 on a stock currently trading at \$98 is quoted at \$5. She pays the \$5 today, in certain currency. Three months later the stock closes at \$104, the option pays \$4, and her trade — profitable on paper at exercise — has lost \$1 overall. Had the stock instead closed at \$110, the same \$5 ticket would have returned \$10. The \$5 is the **premium**: a definite price paid *today* for an uncertain payoff *tomorrow*. Understanding what makes \$5 the right number — not \$3, not \$8 — is the entire problem of option pricing.

Having defined what options are and characterized their payoffs at maturity, we now turn to a more fundamental question: how much should one pay to acquire an option *today*? The payoff at expiration is a random variable that depends on the future stock price, but the purchase happens now, at a definite price. This price — the **option premium** — is the central object of option pricing theory.

---

## Premium as the Price of Optionality

**Key idea**: The premium reflects the asymmetric payoff structure and the uncertainty about the future — not the expected return of the underlying.

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

Recall (see [§ Moneyness](what_is_option.md#moneyness)): an option is ITM when its intrinsic value is positive, OTM when it is zero, and ATM at the boundary.

The **time value** (also called *extrinsic value*) is the remainder:

$$
\text{Time Value} = \text{Premium} - \text{Intrinsic Value}
$$

Time value reflects the possibility that the underlying price may move favorably before expiration. Even an out-of-the-money option commands a positive premium because there is still time for the stock price to cross the strike. As maturity approaches, this possibility diminishes, and the time value decays to zero — a phenomenon known as **time decay**. At expiration, the premium equals the intrinsic value exactly: all time value has vanished.

??? example "Intrinsic and Time Value: SPX Options"
    With the S&P 500 index at approximately 6,616, consider front-month call options (one month to expiration, \$100 multiplier):

    | Strike | Premium (pts) | Intrinsic value | Time value | Dollar cost |
    |---|---|---|---|---|
    | 6,500 (ITM) | $\approx 260$ | $6{,}616 - 6{,}500 = 116$ | $\approx 144$ | \$26,000 |
    | 6,600 (ATM) | $\approx 180$ | $6{,}616 - 6{,}600 = 16$ | $\approx 164$ | \$18,000 |
    | 6,700 (OTM) | $\approx 84$ | $0$ | $84$ | \$8,400 |

    The ATM option is almost entirely time value. As the option moves deeper ITM, intrinsic value grows but time value remains substantial — reflecting the possibility that the index could move even further. The OTM option has no intrinsic value at all; its entire premium is the market's assessment of the probability that the index will rise above 6,700 before expiration.

---

## Factors Affecting the Premium

Five quantities govern the option premium. Their **signs** can be read off the payoff structure before any pricing formula is derived; the magnitudes (the Greeks) are deferred forward.

| Factor | Symbol | Call | Put |
|---|---|---|---|
| Stock price | $S$ | $\uparrow$ | $\downarrow$ |
| Strike price | $K$ | $\downarrow$ | $\uparrow$ |
| Time to maturity | $T - t$ | $\uparrow$ | $\uparrow$ |
| Volatility | $\sigma$ | $\uparrow$ | $\uparrow$ |
| Risk-free rate | $r$ | $\uparrow$ | $\downarrow$ |

The signs follow from the asymmetric payoff: a longer horizon or higher volatility widens the distribution of $S_T$, and the holder benefits from favorable tails while the unfavorable tail is floored at zero.

Recall (see [§ The Greeks](../../ch10/greeks/delta_gamma_vega_theta_rho.md)): the partial derivatives $\Delta, \Gamma, \mathcal{V}, \Theta, \rho$ that quantify these sensitivities are developed in Chapter 10, after the Black-Scholes formula is in hand. The empirical pattern that OTM puts trade at higher implied volatilities than OTM calls — the **volatility skew** — is treated in [§ Implied Volatility Surface](../../ch12/implied_volatility_surface/empirical_smile_spx.md).

Recall (see [§ Why Pricing Matters](why_pricing_matters.md)): the fair premium is the cost of a replicating portfolio, equivalently a discounted expectation $e^{-rT}\mathbb{E}^{\mathbb{Q}}[\text{payoff}]$ under a risk-neutral measure $\mathbb{Q}$ derived from no-arbitrage. The construction of $\mathbb{Q}$ and the closed-form premia are developed in [§ Black-Scholes Formula](../black_scholes_formula/asymptotic_behavior.md).

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
