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

### 2. **Compute $C - P$**


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

### 1. **Case 1: $C - P > S - Ke^{-rT}$** (Call overpriced relative to put)


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

### 2. **Case 2: $C - P < S - Ke^{-rT}$** (Put overpriced relative to call)


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


### 1. **Application 1: Synthetic Positions**


Put-call parity allows creation of **synthetic** positions:

$$
\begin{array}{lll}
\text{Synthetic Call} &=& P + S - Ke^{-rT} \\
\text{Synthetic Put} &=& C - S + Ke^{-rT} \\
\text{Synthetic Stock} &=& C - P + Ke^{-rT} \\
\text{Synthetic Bond} &=& S + P - C
\end{array}
$$

**Use case**: If an option is illiquid or mispriced, create it synthetically using other instruments.

### 2. **Application 2: Pricing One Option from Another**


If you know the call price, you can immediately determine the put price:

$$
P = C - S + Ke^{-rT}
$$

This is useful when only one option trades actively.

### 3. **Application 3: Early Exercise of American Options**


For American options on **non-dividend-paying stocks**, put-call parity implies:

$$
C_{\text{Am}} - P_{\text{Am}} \geq S - Ke^{-r(T-t)}
$$

Since $C_{\text{Am}} = C_{\text{Eu}}$ (call not exercised early), this shows American puts can trade at a premium to European puts.

### 4. **Application 4: Arbitrage Detection**


In practice, compare observed market prices to put-call parity:

$$
\Delta = (C_{\text{market}} - P_{\text{market}}) - (S_{\text{market}} - Ke^{-rT_{\text{market}}})
$$

- If $|\Delta| > \text{transaction costs}$: Potential arbitrage
- If $|\Delta| < \text{transaction costs}$: No arbitrage after costs

### 5. **Application 5: Implied Interest Rate**


If call, put, and stock prices are known, solve for the **implied risk-free rate**:

$$
r = -\frac{1}{T}\log\left(\frac{K}{S + P - C}\right)
$$

This can be used to infer market expectations of interest rates.

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

**Answer**: The put should be priced at **$3.51**.

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
