# Put-Call Parity


**Put-call parity** is a fundamental relationship between European call and put option prices. It is a **no-arbitrage condition** that must hold in frictionless markets, and provides a powerful tool for pricing, hedging, and detecting arbitrage opportunities.

This section derives put-call parity, verifies it for the Black-Scholes formula, and explores its applications.

---

## Statement of Put-Call Parity


### 1. **The Parity Relationship**


For European options on a non-dividend-paying stock with the same strike $K$ and maturity $T$:

$$
\boxed{C - P = S - Ke^{-r(T-t)}}
$$

or equivalently at time $t=0$:

$$
\boxed{C_0 - P_0 = S_0 - Ke^{-rT}}
$$

**In words**: The difference between call and put prices equals the difference between the current stock price and the present value of the strike.

### 2. **Alternative Forms**


Rearranging gives equivalent expressions:

$$
C = P + S - Ke^{-rT}
$$

$$
P = C - S + Ke^{-rT}
$$

$$
S = C - P + Ke^{-rT}
$$

$$
Ke^{-rT} = S + P - C
$$

Each form is useful for different applications.

---

## No-Arbitrage Derivation


Put-call parity can be derived purely from **no-arbitrage arguments**, independent of any model assumptions (like constant volatility or log-normal returns).

### 1. **Portfolio Construction**


Consider two portfolios at time $t=0$:

**Portfolio A**: 
- Long 1 call with strike $K$
- Long 1 zero-coupon bond paying $K$ at time $T$

**Portfolio B**:
- Long 1 put with strike $K$
- Long 1 share of stock

### 2. **Initial Values**


$$
V_0^A = C_0 + Ke^{-rT}
$$

$$
V_0^B = P_0 + S_0
$$

### 3. **Terminal Values**


At maturity $T$, consider two cases:

**Case 1: $S_T > K$** (stock above strike)

- **Portfolio A**:
 
      - Call payoff: $S_T - K$
      - Bond payoff: $K$
      - Total: $(S_T - K) + K = S_T$

- **Portfolio B**:

      - Put payoff: $0$ (expires worthless)
      - Stock value: $S_T$
      - Total: $0 + S_T = S_T$

**Case 2: $S_T \leq K$** (stock at or below strike)

- **Portfolio A**:

      - Call payoff: $0$ (expires worthless)
      - Bond payoff: $K$
      - Total: $0 + K = K$

- **Portfolio B**:

      - Put payoff: $K - S_T$
      - Stock value: $S_T$
      - Total: $(K - S_T) + S_T = K$

**Observation**: In both cases, $V_T^A = V_T^B$.

### 4. **No-Arbitrage Conclusion**


Since the two portfolios have **identical terminal payoffs** in all states, they must have **identical initial values** (otherwise arbitrage exists):

$$
C_0 + Ke^{-rT} = P_0 + S_0
$$

Rearranging:

$$
\boxed{C_0 - P_0 = S_0 - Ke^{-rT}}
$$

This is put-call parity.

---

## Verification with Black-Scholes


### 1. **Black-Scholes Formulas**


Recall:

$$
C = S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)
$$

$$
P = Ke^{-rT}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)
$$

### 2. **Compute C - P**


$$
\begin{aligned}
C - P &= \left[S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)\right] - \left[Ke^{-rT}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)\right] \\
&= S\mathcal{N}(d_1) + S\mathcal{N}(-d_1) - Ke^{-rT}\mathcal{N}(d_2) - Ke^{-rT}\mathcal{N}(-d_2) \\
&= S\left[\mathcal{N}(d_1) + \mathcal{N}(-d_1)\right] - Ke^{-rT}\left[\mathcal{N}(d_2) + \mathcal{N}(-d_2)\right]
\end{aligned}
$$

### 3. **Use Symmetry Property**


For the standard normal CDF:

$$
\mathcal{N}(x) + \mathcal{N}(-x) = 1
$$

Therefore:

$$
C - P = S \cdot 1 - Ke^{-rT} \cdot 1 = S - Ke^{-rT}
$$

**Verified**: Put-call parity holds exactly for the Black-Scholes formula. ✓

---

## Arbitrage Opportunities


If put-call parity is violated, **arbitrage opportunities** exist.

### 1. **Case 1: C - P > S - Ke^-rT** (Call overpriced relative to put)


**Arbitrage strategy**:

1. **Sell** call (receive $C$)
2. **Buy** put (pay $P$)
3. **Buy** stock (pay $S$)
4. **Borrow** $Ke^{-rT}$ at rate $r$

**Net cash flow at $t=0$**:

$$
C - P - S + Ke^{-rT} > 0
$$

(positive cash inflow = free money)

**At maturity $T$**:

- If $S_T > K$: Exercise call against you (deliver stock for $K$), put expires, repay loan $K$. Net: $0$
- If $S_T \leq K$: Call expires, exercise put (sell stock for $K$), repay loan $K$. Net: $0$

**Result**: Guaranteed profit at $t=0$, zero cash flow at $T$ → **Arbitrage**

### 2. **Case 2: C - P < S - Ke^-rT** (Put overpriced relative to call)


**Arbitrage strategy** (reverse of above):

1. **Buy** call (pay $C$)
2. **Sell** put (receive $P$)
3. **Short** stock (receive $S$)
4. **Lend** $Ke^{-rT}$ at rate $r$

**Net cash flow at $t=0$**:

$$
-C + P + S - Ke^{-rT} > 0
$$

**At maturity $T$**: All positions close with zero net cash flow.

**Result**: Guaranteed profit at $t=0$ → **Arbitrage**

---

## Applications


### 1. **Synthetic Positions**


Put-call parity allows creation of **synthetic** positions:

$$
\begin{array}{lll}
\text{Synthetic Call} &=& P + S - Ke^{-rT} \\
\text{Synthetic Put} &=& C - S + Ke^{-rT} \\
\text{Synthetic Stock} &=& C - P + Ke^{-rT} \\
\text{Synthetic Bond} &=& S + P - C
\end{array}
$$

These are useful when an option is illiquid or mispriced, or when only one option trades actively (compute the other via $P = C - S + Ke^{-rT}$).

### 2. **Early Exercise of American Options**


For American options on **non-dividend-paying stocks**, put-call parity implies:

$$
C_{\text{Am}} - P_{\text{Am}} \geq S - Ke^{-r(T-t)}
$$

Since $C_{\text{Am}} = C_{\text{Eu}}$ (call not exercised early), this shows American puts can trade at a premium to European puts.

### 3. **Arbitrage Detection and Implied Rates**


Compare observed market prices to put-call parity. Define the deviation:

$$
\Delta = (C_{\text{market}} - P_{\text{market}}) - (S_{\text{market}} - Ke^{-rT_{\text{market}}})
$$

If $|\Delta|$ exceeds transaction costs, an arbitrage opportunity exists. Conversely, if call, put, and stock prices are known, one can extract the **implied risk-free rate**:

$$
r = -\frac{1}{T}\log\left(\frac{K}{S + P - C}\right)
$$

---

## Generalizations


### 1. **With Continuous Dividends**


If the stock pays dividends at continuous rate $q$:

$$
\boxed{C - P = Se^{-q(T-t)} - Ke^{-r(T-t)}}
$$

**Derivation**: Replace $S$ with $Se^{-qT}$ (present value of stock after dividend payments).

### 2. **With Discrete Dividends**


If the stock pays known dividends $D$ at time $t_d < T$:

$$
\boxed{C - P = \left(S - De^{-rt_d}\right) - Ke^{-rT}}
$$

**Derivation**: Subtract the present value of dividends from the stock price.

### 3. **Foreign Currency Options (Garman-Kohlhagen)**


For options on foreign exchange rate $X$ (domestic per foreign):

$$
\boxed{C - P = Xe^{-r_f T} - Ke^{-r_d T}}
$$

where $r_d$ = domestic rate, $r_f$ = foreign rate.

### 4. **Futures Options**


For options on futures contracts with futures price $F$:

$$
\boxed{C - P = e^{-rT}(F - K)}
$$

Since futures require no initial payment, this simplifies further.

---

## Numerical Example


**Market data**:

- Stock price: $S_0 = 50$
- Strike: $K = 50$
- Time to maturity: $T = 0.5$ years
- Risk-free rate: $r = 4\%$
- Call price: $C_0 = 4.50$

**Question**: What should the put price be?

**Solution**:

From put-call parity:

$$
P_0 = C_0 - S_0 + Ke^{-rT}
$$

$$
P_0 = 4.50 - 50 + 50 \times e^{-0.04 \times 0.5}
$$

$$
P_0 = 4.50 - 50 + 50 \times e^{-0.02}
$$

$$
P_0 = 4.50 - 50 + 50 \times 0.9802
$$

$$
P_0 = 4.50 - 50 + 49.01 = 3.51
$$

**Answer**: The put should be priced at **\$3.51**.

**Check**: $C - P = 4.50 - 3.51 = 0.99$ and $S - Ke^{-rT} = 50 - 49.01 = 0.99$ ✓

---

## Put-Call Parity and Option Strategies


### 1. **Conversion**


Buy stock + Buy put + Sell call = Synthetic bond position

**Payoff at $T$**:

- If $S_T > K$: $S_T + 0 - (S_T - K) = K$
- If $S_T \leq K$: $S_T + (K - S_T) - 0 = K$

**Result**: Guaranteed payoff of $K$ regardless of stock price.

**Profit**: $(S_0 + P_0 - C_0) - Ke^{-rT}$ should be zero by parity.

### 2. **Reversal**


Short stock + Sell put + Buy call = Negative bond position

**Payoff at $T$**: Always $-K$ (borrow $K$)

**Relation to parity**: The reverse of conversion.

### 3. **Box Spread**


Combination of conversion and reversal with different strikes:
- Buy call at $K_1$ + Sell call at $K_2$
- Sell put at $K_1$ + Buy put at $K_2$

**Payoff**: Always $K_2 - K_1$ (risk-free)

**Price**: Should equal $(K_2 - K_1)e^{-rT}$ by no-arbitrage.

---

## Historical Note


Put-call parity was first rigorously derived by **Hans Stoll** in 1969, before the Black-Scholes model. Key insights:

1. **Model-independent**: Requires only no-arbitrage, not specific price dynamics
2. **Broader applicability**: Works even when Black-Scholes assumptions fail
3. **Market efficiency**: Violations are quickly arbitraged away in liquid markets

In practice, put-call parity holds very tightly for liquid, exchange-traded options with transaction costs explaining small deviations.

---

## Summary


Put-call parity establishes the fundamental relationship:

$$
\boxed{C - P = S - Ke^{-r(T-t)}}
$$

**Key points**:

1. **Derivation**: Pure no-arbitrage argument (portfolio replication)

2. **Verification**: Satisfied exactly by Black-Scholes formula

3. **Applications**:
   - Create synthetic positions
   - Price one option from another
   - Detect arbitrage opportunities
   - Infer implied interest rates

4. **Generalizations**: Extends to dividends, foreign exchange, futures

5. **Robustness**: Holds regardless of underlying asset dynamics (unlike Black-Scholes formula)

6. **Practical importance**: One of the most reliable relationships in option markets

Put-call parity is more fundamental than any specific pricing model—it follows directly from the law of one price and must hold in any arbitrage-free market.

---

## Exercises

**Exercise 1.** A stock trades at $S_0 = 75$. A European call with $K = 80$, $T = 0.25$, and $r = 5\%$ is priced at $C_0 = 2.80$. Using put-call parity, determine the price of the corresponding European put.

??? success "Solution to Exercise 1"
    **Given**: $S_0 = 75$, $K = 80$, $T = 0.25$, $r = 0.05$, $C_0 = 2.80$.

    From put-call parity:

    $$
    P_0 = C_0 - S_0 + Ke^{-rT}
    $$

    $$
    = 2.80 - 75 + 80 \times e^{-0.05 \times 0.25}
    $$

    $$
    = 2.80 - 75 + 80 \times e^{-0.0125}
    $$

    $$
    = 2.80 - 75 + 80 \times 0.9876
    $$

    $$
    = 2.80 - 75 + 79.01 = 6.81
    $$

    The European put price is $\$6.81$.

    **Verification**: $C_0 - P_0 = 2.80 - 6.81 = -4.01$ and $S_0 - Ke^{-rT} = 75 - 79.01 = -4.01$ ✓

---
**Exercise 2.** Verify put-call parity algebraically for the Black-Scholes formulas. Starting from $C - P = [S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)] - [Ke^{-rT}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)]$, use the identity $\mathcal{N}(x) + \mathcal{N}(-x) = 1$ to show that $C - P = S - Ke^{-rT}$.

??? success "Solution to Exercise 2"
    Starting from:

    $$
    C - P = [S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)] - [Ke^{-rT}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)]
    $$

    Expand:

    $$
    C - P = S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2) - Ke^{-rT}\mathcal{N}(-d_2) + S\mathcal{N}(-d_1)
    $$

    Group terms:

    $$
    = S[\mathcal{N}(d_1) + \mathcal{N}(-d_1)] - Ke^{-rT}[\mathcal{N}(d_2) + \mathcal{N}(-d_2)]
    $$

    Apply the identity $\mathcal{N}(x) + \mathcal{N}(-x) = 1$ for all $x$:

    $$
    = S \cdot 1 - Ke^{-rT} \cdot 1 = S - Ke^{-rT}
    $$

    Therefore $C - P = S - Ke^{-rT}$, confirming put-call parity holds exactly for the Black-Scholes formulas.

---
**Exercise 3.** The following prices are observed: $S_0 = 100$, $C_0 = 12.50$, $P_0 = 8.00$, $K = 100$, $T = 1$, $r = 3\%$. Check whether put-call parity holds. If it does not, describe the arbitrage strategy and compute the risk-free profit.

??? success "Solution to Exercise 3"
    **Given**: $S_0 = 100$, $C_0 = 12.50$, $P_0 = 8.00$, $K = 100$, $T = 1$, $r = 0.03$.

    **Put-call parity requires**: $C_0 - P_0 = S_0 - Ke^{-rT}$.

    Left side: $12.50 - 8.00 = 4.50$.

    Right side: $100 - 100 \times e^{-0.03} = 100 - 97.04 = 2.96$.

    Since $4.50 \neq 2.96$, parity is violated. The difference is $4.50 - 2.96 = 1.54 > 0$.

    Since $C_0 - P_0 > S_0 - Ke^{-rT}$, the call is overpriced relative to the put.

    **Arbitrage strategy**:

    1. Sell the call (receive $12.50$)
    2. Buy the put (pay $8.00$)
    3. Buy the stock (pay $100$)
    4. Borrow $Ke^{-rT} = 97.04$ at rate $r$

    **Net cash flow at $t = 0$**: $12.50 - 8.00 - 100 + 97.04 = 1.54$

    **At maturity ($T = 1$)**:

    - If $S_T > 100$: Call is exercised against us (deliver stock, receive $100$); put expires; repay loan $100$. Net: $100 - 100 = 0$.
    - If $S_T \leq 100$: Call expires; exercise put (sell stock at $100$); repay loan $100$. Net: $100 - 100 = 0$.

    **Risk-free profit**: $\$1.54$ received at $t = 0$ with zero net obligation at $T$.

---
**Exercise 4.** Derive put-call parity for a stock paying continuous dividends at rate $q$:

$$
C - P = Se^{-qT} - Ke^{-rT}
$$

Construct the two replicating portfolios and show their terminal values are identical.

??? success "Solution to Exercise 4"
    **Portfolio A**: Long 1 call + long bond paying $K$ at $T$.

    Cost: $C + Ke^{-rT}$.

    **Portfolio B**: Long 1 put + long $e^{-qT}$ shares of stock (reinvesting dividends).

    Cost: $P + Se^{-qT}$.

    The $e^{-qT}$ shares grow to $1$ share at $T$ (dividends are reinvested at rate $q$).

    **Terminal values**:

    If $S_T > K$: Portfolio A pays $(S_T - K) + K = S_T$. Portfolio B pays $0 + S_T = S_T$.

    If $S_T \leq K$: Portfolio A pays $0 + K = K$. Portfolio B pays $(K - S_T) + S_T = K$.

    Since terminal values are identical in all states:

    $$
    C + Ke^{-rT} = P + Se^{-qT}
    $$

    Rearranging:

    $$
    C - P = Se^{-qT} - Ke^{-rT}
    $$

---
**Exercise 5.** A box spread consists of buying a bull call spread ($K_1$, $K_2$) and buying a bear put spread ($K_1$, $K_2$). Show that its payoff at maturity is always $K_2 - K_1$, regardless of $S_T$, by using put-call parity applied at both strikes. What should the box spread cost at time $0$?

??? success "Solution to Exercise 5"
    A box spread consists of:

    - Bull call spread: buy call at $K_1$, sell call at $K_2$
    - Bear put spread: buy put at $K_2$, sell put at $K_1$

    Apply put-call parity at strike $K_1$: $C_1 - P_1 = S - K_1 e^{-rT}$.

    Apply put-call parity at strike $K_2$: $C_2 - P_2 = S - K_2 e^{-rT}$.

    Subtract the second from the first:

    $$
    (C_1 - C_2) - (P_1 - P_2) = (K_2 - K_1)e^{-rT}
    $$

    The left side is the cost of the box spread: $(C_1 - C_2) + (P_2 - P_1)$.

    **Payoff verification** at maturity:

    If $S_T \leq K_1$: Bull call pays $0$, bear put pays $(K_2 - S_T) - (K_1 - S_T) = K_2 - K_1$.

    If $K_1 < S_T \leq K_2$: Bull call pays $S_T - K_1$, bear put pays $K_2 - S_T$. Total: $K_2 - K_1$.

    If $S_T > K_2$: Bull call pays $(S_T - K_1) - (S_T - K_2) = K_2 - K_1$, bear put pays $0$. Total: $K_2 - K_1$.

    In all cases, the payoff is $K_2 - K_1$.

    **Fair cost at $t = 0$**: The box spread is equivalent to a zero-coupon bond paying $K_2 - K_1$ at $T$, so its price should be:

    $$
    (K_2 - K_1)e^{-rT}
    $$

---
**Exercise 6.** Using put-call parity, derive the implied risk-free rate from the following market data: $S_0 = 50$, $C_0 = 6.20$, $P_0 = 4.10$, $K = 50$, $T = 0.5$. Solve for $r$ and compare with prevailing treasury rates.

??? success "Solution to Exercise 6"
    **Given**: $S_0 = 50$, $C_0 = 6.20$, $P_0 = 4.10$, $K = 50$, $T = 0.5$.

    From put-call parity: $C_0 - P_0 = S_0 - Ke^{-rT}$.

    $$
    6.20 - 4.10 = 50 - 50e^{-0.5r}
    $$

    $$
    2.10 = 50(1 - e^{-0.5r})
    $$

    $$
    1 - e^{-0.5r} = \frac{2.10}{50} = 0.042
    $$

    $$
    e^{-0.5r} = 0.958
    $$

    $$
    -0.5r = \ln(0.958) = -0.04289
    $$

    $$
    r = \frac{0.04289}{0.5} = 0.08578 \approx 8.58\%
    $$

    The implied risk-free rate is approximately $8.58\%$. If prevailing treasury rates are significantly lower (e.g., $4\text{-}5\%$), this discrepancy could indicate mispricing in the options market, dividend expectations not accounted for, or credit/liquidity effects.

---
**Exercise 7.** Explain why put-call parity does not hold exactly for American options. Show that for American options on a non-dividend-paying stock, the following inequality holds:

$$
S - K \leq C_{\text{Am}} - P_{\text{Am}} \leq S - Ke^{-rT}
$$

Hint: use the fact that the American call equals its European counterpart, while the American put is worth at least as much as the European put.

??? success "Solution to Exercise 7"
    For American options on a non-dividend-paying stock:

    - $C_{\text{Am}} = C_{\text{Eu}}$ (American call equals European call, since early exercise is never optimal)
    - $P_{\text{Am}} \geq P_{\text{Eu}}$ (American put is worth at least as much as European put due to early exercise right)

    **Upper bound**: From European put-call parity, $C_{\text{Eu}} - P_{\text{Eu}} = S - Ke^{-rT}$.

    Since $C_{\text{Am}} = C_{\text{Eu}}$ and $P_{\text{Am}} \geq P_{\text{Eu}}$:

    $$
    C_{\text{Am}} - P_{\text{Am}} \leq C_{\text{Am}} - P_{\text{Eu}} = C_{\text{Eu}} - P_{\text{Eu}} = S - Ke^{-rT}
    $$

    **Lower bound**: Consider the following argument. At any time, the American put can be exercised to receive $K - S$ (if positive). But the American call, if exercised, would yield $S - K$. Therefore a portfolio of long American call and short American put satisfies:

    At maturity, the payoff is $(S_T - K)^+ - (K - S_T)^+ = S_T - K$.

    Since the put could be exercised early by its holder (when short the put, we face early exercise risk), the worst case is that the put is exercised immediately, giving payoff $-(K - S) = S - K$. Meanwhile we still hold the call.

    More formally: at any time $t$, the holder of "long call + short put" can always close by exercising the call (if $S > K$) or having the put exercised against them ($S < K$), netting $S_t - K$ in either case. So the minimum value of the call-put position is $S - K$:

    $$
    C_{\text{Am}} - P_{\text{Am}} \geq S - K
    $$

    Combining both bounds:

    $$
    S - K \leq C_{\text{Am}} - P_{\text{Am}} \leq S - Ke^{-rT}
    $$

    Put-call parity does not hold as an equality for American options because the early exercise feature of the American put creates an asymmetry: the put may be exercised early while the call will not be, breaking the replication argument that requires both options to be held to maturity.
