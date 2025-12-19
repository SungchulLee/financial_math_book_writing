# One-Period Option Pricing

Having established the theoretical foundations—no-arbitrage bounds, replication, risk-neutral probability, and martingale pricing—we now apply these principles to price standard options in the one-period binomial model.

---

## 1. Setup and Option Payoffs

Recall the one-period market:

- **Risk-free asset**: $B_0 = 1$, $B_1 = 1+r$
- **Risky asset**: $S_0 > 0$, $S_1 \in \{uS_0, dS_0\}$ with $u > d > 0$
- **No-arbitrage condition**: $d < 1+r < u$

We consider two fundamental option types:

### **European Call Option**

Payoff at time 1:

$$
C_1 = (S_1 - K)^+ = \max(S_1 - K, 0)
$$



where $K > 0$ is the **strike price**.

In the binomial model:

$$
C_1 = 
\begin{cases}
(uS_0 - K)^+ & \text{if up} \\
(dS_0 - K)^+ & \text{if down}
\end{cases}
$$



### **European Put Option**

Payoff at time 1:

$$
P_1 = (K - S_1)^+ = \max(K - S_1, 0)
$$



In the binomial model:

$$
P_1 = 
\begin{cases}
(K - uS_0)^+ & \text{if up} \\
(K - dS_0)^+ & \text{if down}
\end{cases}
$$



---

## 2. Pricing via Replication

**Principle**: Find a portfolio $(\Delta, \beta)$ such that $V_1 = H$ in both states, where $H$ is the option payoff.

### **European Call**

We require:

$$
\begin{aligned}
\Delta \cdot uS_0 + \beta(1+r) &= (uS_0 - K)^+ \\
\Delta \cdot dS_0 + \beta(1+r) &= (dS_0 - K)^+
\end{aligned}
$$



Let $C_u = (uS_0 - K)^+$ and $C_d = (dS_0 - K)^+$. Solving:


$$
\boxed{\Delta = \frac{C_u - C_d}{(u-d)S_0}}
$$




$$
\boxed{\beta = \frac{uC_d - dC_u}{(u-d)(1+r)}}
$$



The **no-arbitrage price** is:

$$
\boxed{C_0 = \Delta S_0 + \beta = \frac{1}{1+r}\left[qC_u + (1-q)C_d\right]}
$$



where

$$
q = \frac{1+r-d}{u-d}
$$



is the **risk-neutral probability**.

### **European Put**

By identical reasoning with $P_u = (K - uS_0)^+$ and $P_d = (K - dS_0)^+$:


$$
\boxed{P_0 = \frac{1}{1+r}\left[qP_u + (1-q)P_d\right]}
$$



---

## 3. Pricing via Risk-Neutral Expectation

**Principle**: Under the risk-neutral probability $\mathbb{Q}$ (where $\mathbb{Q}(\text{up}) = q$), discounted asset prices are martingales.

### **General Formula**

For any contingent claim $H$:

$$
\boxed{V_0 = \frac{1}{1+r}\mathbb{E}^{\mathbb{Q}}[H]}
$$



### **Application**

**Call**:

$$
C_0 = \frac{1}{1+r}\mathbb{E}^{\mathbb{Q}}[(S_1 - K)^+] = \frac{1}{1+r}\left[q(uS_0-K)^+ + (1-q)(dS_0-K)^+\right]
$$



**Put**:

$$
P_0 = \frac{1}{1+r}\mathbb{E}^{\mathbb{Q}}[(K - S_1)^+] = \frac{1}{1+r}\left[q(K-uS_0)^+ + (1-q)(K-dS_0)^+\right]
$$



---

## 4. Numerical Example

Consider:

$$
S_0 = 100, \quad u = 1.2, \quad d = 0.9, \quad r = 0.05, \quad K = 105
$$



**Step 1**: Verify no-arbitrage

$$
d = 0.9 < 1.05 = 1+r < 1.2 = u \quad \checkmark
$$



**Step 2**: Compute risk-neutral probability

$$
q = \frac{1.05 - 0.9}{1.2 - 0.9} = \frac{0.15}{0.3} = 0.5
$$



### **Call Option Pricing**

Terminal stock prices and call payoffs:

$$
\begin{aligned}
S_1^u &= 120, \quad C_u = (120-105)^+ = 15 \\
S_1^d &= 90, \quad C_d = (90-105)^+ = 0
\end{aligned}
$$



**Call price**:

$$
C_0 = \frac{1}{1.05}\left[0.5 \cdot 15 + 0.5 \cdot 0\right] = \frac{7.5}{1.05} \approx 7.14
$$



**Replicating portfolio**:

$$
\Delta = \frac{15 - 0}{(1.2-0.9) \cdot 100} = \frac{15}{30} = 0.5
$$




$$
\beta = \frac{1.2 \cdot 0 - 0.9 \cdot 15}{0.3 \cdot 1.05} = \frac{-13.5}{0.315} \approx -42.86
$$



**Verification**:

$$
C_0 = 0.5 \cdot 100 + (-42.86) = 50 - 42.86 = 7.14 \quad \checkmark
$$



### **Put Option Pricing**

Put payoffs:

$$
\begin{aligned}
P_u &= (105-120)^+ = 0 \\
P_d &= (105-90)^+ = 15
\end{aligned}
$$



**Put price**:

$$
P_0 = \frac{1}{1.05}\left[0.5 \cdot 0 + 0.5 \cdot 15\right] = \frac{7.5}{1.05} \approx 7.14
$$



---

## 5. Put-Call Parity

A fundamental relationship exists between European call and put prices.

### **Derivation**

Consider two portfolios at time 0:

- **Portfolio A**: Long call + $K/(1+r)$ in bank
- **Portfolio B**: Long put + long stock

Values at time 0:

$$
\begin{aligned}
V_0^A &= C_0 + \frac{K}{1+r} \\
V_0^B &= P_0 + S_0
\end{aligned}
$$



Values at time 1:

| State | Portfolio A | Portfolio B |
|-------|-------------|-------------|
| Up | $(uS_0-K)^+ + K = \max(uS_0, K)$ | $(K-uS_0)^+ + uS_0 = \max(uS_0, K)$ |
| Down | $(dS_0-K)^+ + K = \max(dS_0, K)$ | $(K-dS_0)^+ + dS_0 = \max(dS_0, K)$ |

Since $V_1^A = V_1^B$ in all states, no-arbitrage implies:


$$
\boxed{C_0 - P_0 = S_0 - \frac{K}{1+r}}
$$



This is the **one-period put-call parity**.

### **Verification with Example**

From our numerical example:

$$
\begin{aligned}
C_0 - P_0 &= 7.14 - 7.14 = 0 \\
S_0 - \frac{K}{1+r} &= 100 - \frac{105}{1.05} = 100 - 100 = 0 \quad \checkmark
\end{aligned}
$$



---

## 6. Moneyness and Intrinsic Value

### **Moneyness Classification**

For a call option with strike $K$:

- **In-the-money (ITM)**: $S_0 > K$ (immediate exercise would yield positive payoff)
- **At-the-money (ATM)**: $S_0 \approx K$
- **Out-of-the-money (OTM)**: $S_0 < K$ (immediate exercise worthless)

For a put: ITM when $S_0 < K$, OTM when $S_0 > K$.

### **Intrinsic Value vs. Time Value**

The option price decomposes as:

$$
\text{Option Price} = \text{Intrinsic Value} + \text{Time Value}
$$



where:
- **Intrinsic value**: Payoff from immediate exercise = $(S_0 - K)^+$ for call, $(K - S_0)^+$ for put
- **Time value**: Additional value from the possibility of favorable price movement

In our example:

$$
\begin{aligned}
\text{Call intrinsic} &= (100-105)^+ = 0 \\
\text{Call time value} &= 7.14 - 0 = 7.14
\end{aligned}
$$



The call is OTM but has positive time value because there's a chance $S_1 = 120 > 105$.

---

## 7. Key Observations

1. **All methods agree**: Replication, risk-neutral expectation, and martingale pricing yield identical prices—they are merely different perspectives on the same no-arbitrage principle.

2. **Linearity**: Option pricing is linear in payoffs. If $H = \alpha H_1 + \beta H_2$, then $V_0(H) = \alpha V_0(H_1) + \beta V_0(H_2)$.

3. **Put-call parity** is a consequence of no-arbitrage, not an assumption.

4. **Replicating portfolio interpretation**: 
   - For calls: $\Delta > 0$ (long stock), $\beta < 0$ (borrow money)
   - For puts: $\Delta < 0$ (short stock), $\beta > 0$ (lend money)

5. **Risk-neutral probability** $q$ does *not* depend on the claim being priced—it's a property of the market model itself.

---

## Summary

The one-period binomial model demonstrates that option pricing reduces to:

1. Identifying the two possible payoffs $H_u$ and $H_d$
2. Computing the risk-neutral probability $q = \frac{1+r-d}{u-d}$
3. Discounting the expected payoff: $V_0 = \frac{1}{1+r}[qH_u + (1-q)H_d]$

This simple structure generalizes to multi-period trees via **backward induction**, which we explore next.
