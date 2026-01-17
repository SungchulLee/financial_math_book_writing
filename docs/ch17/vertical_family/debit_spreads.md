# Debit Spreads


## Overview


A **debit spread** is a type of **vertical spread** that is entered for a **net premium paid**.  
It consists of buying one option and selling another option of the **same type** (calls or puts), with:

- the same underlying
- the same expiration
- different strike prices

Debit spreads are primarily used to express a **directional view** while limiting risk and capital outlay.

They have **defined risk and defined reward**.

---

## Debit Spreads as Vertical Spreads
All debit spreads are **vertical spreads**, but not all vertical spreads are debit spreads.

```
Vertical Spreads
├── Debit Spreads
│   ├── Long Call Spread (Bull Call)
│   └── Long Put Spread (Bear Put)
└── Credit Spreads
    ├── Short Call Spread (Bear Call)
    └── Short Put Spread (Bull Put)
```

The key distinction is **cash flow at entry**:

- **Debit spread** → pay premium  
- **Credit spread** → receive premium  

---

## Common Structure and Setup
A debit spread always follows this pattern:

- **Buy the option closer to the money**
- **Sell the option further out of the money**
- Net result: **debit paid**

The short option reduces cost but caps the maximum profit.

---

## Long Call Spread


### 1. Market Outlook

- **Bullish**
- Expect the underlying to rise **moderately**

### 2. Structure

- Buy a call at a lower strike \( K_1 \)
- Sell a call at a higher strike \( K_2 > K_1 \)
- Same expiration

### 3. Payoff

- **Maximum Loss:** Net debit paid
- **Maximum Profit:**  
  \[
  (K_2 - K_1) - \text{Net Debit}
  \]
- **Break-even:**  
  \[
  K_1 + \text{Net Debit}
  \]

### 4. Intuition

You are betting on a **controlled upside move**.  
Compared to buying a naked call, this strategy lowers cost at the expense of capped upside.

---

## Long Put Spread


### 1. Market Outlook

- **Bearish**
- Expect the underlying to fall **moderately**

### 2. Structure

- Buy a put at a higher strike \( K_1 \)
- Sell a put at a lower strike \( K_2 < K_1 \)
- Same expiration

### 3. Payoff

- **Maximum Loss:** Net debit paid
- **Maximum Profit:**  
  \[
  (K_1 - K_2) - \text{Net Debit}
  \]
- **Break-even:**  
  \[
  K_1 - \text{Net Debit}
  \]

### 4. Intuition

You are betting on a **controlled downside move**.  
The sold put finances part of the long put while limiting profit.

---

## Risk and Reward


### 1. Key Properties Overview
| Feature | Debit Spreads |
|------|---------------|
| Directional Bias | Bullish or Bearish |
| Max Profit | Limited |
| Max Loss | Limited (debit paid) |
| Theta | Usually Negative |
| Vega | Positive |
| Capital Efficiency | Higher than naked options |

Debit spreads trade **limited reward for defined and reduced risk**.

---

## Implied Volatility Considerations


### Why IV Matters for Debit Spreads

Debit spreads are **long volatility positions** (net positive vega). This means:

1. **Lower IV at entry is favorable** – You pay less premium for the same spread
2. **IV expansion helps** – If IV rises after entry, your spread value increases
3. **IV contraction hurts** – If IV drops, your long option loses more than short option gains

### Optimal IV Environment

| IV Rank | Suitability | Rationale |
|---------|-------------|-----------|
| < 30% | Excellent | Options cheap, IV expansion potential |
| 30-50% | Good | Moderate premium, balanced risk |
| > 50% | Poor | Premium expensive, IV likely to contract |

### The Directional-Vol Trade-off

Debit spreads create a **dual bet**:
1. **Directional:** Stock must move in your favor
2. **Volatility:** Ideally, IV expands or stays stable

In high IV environments, consider:
- Using credit spreads instead (opposite direction)
- Waiting for IV to normalize
- Using shorter expirations to reduce vega exposure

---

## Greeks Profile


### Delta

- **Long call spread:** Positive delta (bullish)
- **Long put spread:** Negative delta (bearish)
- Delta magnitude is highest when underlying is between strikes

$$
\Delta_{\text{spread}} = \Delta_{\text{long}} - \Delta_{\text{short}}
$$

### Theta

Debit spreads typically have **negative theta** – time decay works against you.

$$
\Theta_{\text{spread}} = \Theta_{\text{long}} - \Theta_{\text{short}} < 0
$$

**Exception:** Deep ITM debit spreads can have positive theta as the short option's theta dominates.

### Vega

Debit spreads have **positive vega** – IV increases help you.

$$
\nu_{\text{spread}} = \nu_{\text{long}} - \nu_{\text{short}} > 0
$$

This is smaller than a naked long option's vega because the short option offsets.

### Gamma

Debit spreads have **positive gamma** – acceleration of delta as price moves favorably.

$$
\Gamma_{\text{spread}} = \Gamma_{\text{long}} - \Gamma_{\text{short}} > 0
$$

Gamma is maximized near the long strike.

---

## Strike Selection Strategy


### Width Selection

Wider spreads have:
- Higher max profit potential
- Higher cost (more capital at risk)
- Lower probability of achieving max profit
- Better absolute return potential

Narrower spreads have:
- Lower max profit potential
- Lower cost
- Higher probability of some profit
- Better percentage return potential

### Long Strike Selection

| Strike Selection | Cost | Break-even | Risk/Reward |
|------------------|------|------------|-------------|
| ATM long | High | Near current price | Better R/R |
| Slightly OTM long | Medium | Moderate move needed | Balanced |
| Deep OTM long | Low | Large move needed | Lottery ticket |

### Practical Guidelines

1. **High conviction:** ATM/ITM long, 3-5 strikes wide
2. **Moderate conviction:** Slightly OTM long, 2-3 strikes wide
3. **Speculative:** OTM long, 1-2 strikes wide

---

## Position Management


### Profit Taking

- **50% of max profit:** Early exit preserves capital for next trade
- **Break-even move achieved:** Evaluate theta vs. remaining upside
- **Hold to expiration:** Only if deep ITM and confident in continued move

### Loss Management

- **50% of debit paid:** Common stop loss level
- **Underlying breaks key support/resistance:** Exit regardless of spread value
- **Time stop:** Exit if 50%+ of time passed with no favorable move

### Rolling Strategies

**Roll up (strikes):**
- Sell current spread (at profit)
- Buy new spread at higher strikes
- Used to lock in profits while maintaining upside exposure

**Roll out (time):**
- Sell current spread
- Buy new spread at same strikes, later expiration
- Used when thesis intact but time running out

---

## Comparison


| Feature | Long Call Spread | Long Put Spread |
|------|------------------|----------------|
| Bias | Bullish | Bearish |
| Bought Option | Call | Put |
| Profit If | Price rises | Price falls |
| Risk | Downside | Upside |

---

## When to Use Debit Spreads
Debit spreads are well-suited when:

- You have a **directional conviction** (moderately bullish or bearish)
- You want to reduce option premium cost vs. buying naked options
- Implied volatility is **low to moderate** (IV Rank < 50%)
- You prefer defined-risk directional strategies
- You expect a **moderate move** (not a large breakout)

**Avoid debit spreads when:**
- IV is very high (IV Rank > 60%) – premium too expensive
- You expect a very large move (naked options or backspreads better)
- Time to expiration is too short (< 14 days) – theta decay too aggressive
- The underlying lacks liquidity

---

## Concrete Example


**Setup:**
- Stock XYZ trading at $100
- 45 DTE options
- IV Rank: 25% (relatively cheap)
- Bullish outlook targeting $110

**Bull Call Spread:**
- Buy $100 call @ $5.00
- Sell $110 call @ $1.50
- **Net debit: $3.50**

**Key Metrics:**
- Max profit: $10.00 - $3.50 = $6.50 (if stock > $110 at expiration)
- Max loss: $3.50 (if stock < $100 at expiration)
- Break-even: $100 + $3.50 = $103.50
- Risk/reward ratio: 3.50:6.50 = 0.54:1 (favorable)
- Required move to break-even: +3.5%

**Management plan:**
- Take profit at $5.00 (77% of max)
- Stop loss if spread value drops to $1.75 (50% loss)
- Roll out if at 14 DTE with stock between $103-$108

---

## Debit Spread vs. Credit Spread Decision


| Factor | Favor Debit Spread | Favor Credit Spread |
|--------|-------------------|---------------------|
| IV Level | Low (< 30%) | High (> 50%) |
| Direction | Strong conviction | Mild expectation |
| Time Horizon | Want time on your side | Want to collect theta |
| Risk Preference | Pay upfront, unlimited time value | Receive upfront, fight time |

---

## Key Takeaways and Summary
- Debit spreads are **vertical spreads entered for a net debit**
- The two canonical forms are:
  - **Long Call Spread (Bull Call)**
  - **Long Put Spread (Bear Put)**
- Risk is limited to the premium paid
- Profit is capped but capital efficiency is improved
- **IV environment matters:** Enter when IV Rank < 50%
- **Greeks:** Positive delta (directional), negative theta, positive vega, positive gamma
- **Management:** Take profits at 50-75%, cut losses at 50%

> Debit spreads are best viewed as **cost-efficient directional trades**, not volatility bets.