# Credit Spreads


## Overview


A **credit spread** is a type of **vertical spread** that is entered for a **net premium received**.  
It consists of selling one option and buying another option of the **same type** (calls or puts), with:

- the same underlying
- the same expiration
- different strike prices

Credit spreads are primarily used to generate **income** and benefit from:
- time decay (positive theta)
- stable or moderately directional markets

They have **defined risk and defined reward**.

---

## Credit Spreads as Vertical Spreads
All credit spreads are **vertical spreads**, but not all vertical spreads are credit spreads.

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
A credit spread always follows this pattern:

- **Sell the option closer to the money**
- **Buy the option further out of the money**
- Net result: **credit received**

The long option limits risk by capping potential losses.

---

## Short Call Spread


### 1. Market Outlook

- Neutral to **bearish**
- Expect the underlying to stay **below the short call strike**

### 2. Structure

- Sell a call at a lower strike \( K_1 \)
- Buy a call at a higher strike \( K_2 > K_1 \)
- Same expiration

### 3. Payoff

- **Maximum Profit:** Net credit received
- **Maximum Loss:**  
  \[
  (K_2 - K_1) - \text{Net Credit}
  \]
- **Break-even:**  
  \[
  K_1 + \text{Net Credit}
  \]

### 4. Intuition

You are betting that the underlying will **not rise significantly**.  
Time decay works in your favor as long as price stays below the short call.

---

## Short Put Spread


### 1. Market Outlook

- Neutral to **bullish**
- Expect the underlying to stay **above the short put strike**

### 2. Structure

- Sell a put at a higher strike \( K_1 \)
- Buy a put at a lower strike \( K_2 < K_1 \)
- Same expiration

### 3. Payoff

- **Maximum Profit:** Net credit received
- **Maximum Loss:**  
  \[
  (K_1 - K_2) - \text{Net Credit}
  \]
- **Break-even:**  
  \[
  K_1 - \text{Net Credit}
  \]

### 4. Intuition

You are betting that the underlying will **not fall significantly**.  
Time decay benefits you as long as price remains above the short put.

---

## Risk and Reward


### 1. Key Properties Overview
| Feature | Credit Spreads |
|------|---------------|
| Directional Bias | Mild (bullish or bearish) |
| Max Profit | Limited |
| Max Loss | Limited |
| Theta | Positive |
| Vega | Negative |
| Margin Requirement | Defined |

Credit spreads trade **high probability for limited reward**.

---

## Implied Volatility Considerations


### Why IV Matters for Credit Spreads

Credit spreads are **short volatility positions**. This means:

1. **Higher IV at entry is favorable** – You receive more premium for the same spread width
2. **IV contraction helps** – If IV drops after entry, both options lose value (you want this)
3. **IV expansion hurts** – If IV rises, your short option loses more than your long option gains

### Optimal IV Environment

| IV Rank | Suitability | Rationale |
|---------|-------------|-----------|
| > 50% | Excellent | Premium rich, high probability of IV mean reversion |
| 30-50% | Good | Decent premium, moderate edge |
| < 30% | Poor | Premium too thin, risk/reward unfavorable |

### The IV-Skew Connection

For **short put spreads** (bull put spreads):
- OTM puts have elevated IV due to skew
- You're selling this "fear premium"
- Skew compression benefits you

For **short call spreads** (bear call spreads):
- OTM calls have lower IV than puts
- Less skew premium to capture
- Often used more for directional bets than pure IV plays

---

## Greeks Profile


### Delta

- **Short call spread:** Negative delta (bearish)
- **Short put spread:** Positive delta (bullish)
- Delta magnitude increases as underlying approaches short strike

$$
\Delta_{\text{spread}} = \Delta_{\text{short}} - \Delta_{\text{long}}
$$

### Theta

Credit spreads have **positive theta** – time decay works for you.

$$
\Theta_{\text{spread}} = \Theta_{\text{short}} - \Theta_{\text{long}} > 0
$$

Theta is maximized when:
- Short option is ATM
- Time to expiration is 30-45 days

### Vega

Credit spreads have **negative vega** – IV increases hurt you.

$$
\nu_{\text{spread}} = \nu_{\text{short}} - \nu_{\text{long}} < 0
$$

Since the short option is closer to ATM, it has higher vega.

### Gamma

Credit spreads have **negative gamma** – large moves hurt you.

$$
\Gamma_{\text{spread}} = \Gamma_{\text{short}} - \Gamma_{\text{long}} < 0
$$

This is the "time bomb" of credit spreads: as expiration approaches, gamma increases dramatically.

---

## Strike Selection Strategy


### Width Selection

Wider spreads have:
- Higher max profit (more credit)
- Higher max loss
- Lower probability of profit
- Better risk/reward ratio

Narrower spreads have:
- Lower max profit
- Lower max loss
- Higher probability of profit
- Worse risk/reward ratio

### Distance from ATM

| Strike Selection | Probability | Credit | Risk/Reward |
|------------------|-------------|--------|-------------|
| 10-delta short | ~90% | Low | High prob, low return |
| 20-delta short | ~80% | Medium | Balanced |
| 30-delta short | ~70% | High | Lower prob, higher return |

### Practical Guidelines

1. **Income focus:** Sell 15-20 delta shorts, 1-2 strikes wide
2. **Balanced approach:** Sell 20-30 delta shorts, 2-3 strikes wide
3. **Higher return:** Sell 30-40 delta shorts, 3-5 strikes wide

---

## Position Management


### Profit Taking

- **50% of max profit:** Common exit target for consistent returns
- **75% of max profit:** More aggressive, captures most of the move
- **Hold to expiration:** Maximum profit but highest gamma risk

### Loss Management

- **1.5-2x credit received:** Stop loss level
- **200% of max profit:** Alternative stop level
- **Underlying crosses short strike:** Evaluate for adjustment

### Rolling Strategies

**Roll out (time):**
- Buy back current spread
- Sell new spread at same strikes, later expiration
- Used when position is threatened but thesis intact

**Roll out and away (time + strikes):**
- Buy back current spread
- Sell new spread at further strikes, later expiration
- Used to create more breathing room

---

## Comparison


| Feature | Short Call Spread | Short Put Spread |
|------|------------------|------------------|
| Bias | Bearish / Neutral | Bullish / Neutral |
| Sold Option | Call | Put |
| Profit If | Price stays below short call | Price stays above short put |
| Risk | Upside | Downside |

---

## When to Use Credit Spreads
Credit spreads are well-suited when:

- You expect **range-bound** or mildly trending markets
- Implied volatility is **moderate to high** (IV Rank > 30%)
- You want **defined risk income strategies**
- You prefer probability-based trading over large directional bets
- You have a **mild directional view** but don't want unlimited risk

**Avoid credit spreads when:**
- IV is very low (IV Rank < 20%)
- You expect large directional moves
- Major binary events are imminent (earnings, FDA, etc.)
- The underlying lacks liquidity

---

## Concrete Example


**Setup:**
- Stock XYZ trading at $100
- 45 DTE options
- IV Rank: 65%

**Bull Put Spread (expecting support at $95):**
- Sell $95 put @ $2.50
- Buy $90 put @ $1.00
- **Net credit: $1.50**

**Key Metrics:**
- Max profit: $1.50 (if stock > $95 at expiration)
- Max loss: $5.00 - $1.50 = $3.50 (if stock < $90)
- Break-even: $95 - $1.50 = $93.50
- Risk/reward ratio: 3.50:1.50 = 2.33:1
- Probability of profit: ~70%

**Management plan:**
- Take profit at $0.75 (50% of max)
- Stop loss if spread value reaches $3.00 (2x credit)
- Roll if stock drops below $96 with 2+ weeks remaining

---

## Key Takeaways and Summary
- Credit spreads are **vertical spreads entered for a net credit**
- The two canonical forms are:
  - **Short Call Spread (Bear Call)**
  - **Short Put Spread (Bull Put)**
- Risk and reward are **known in advance**
- Time decay is your ally, but strong directional moves are your enemy
- **IV environment matters:** Enter when IV Rank > 30%
- **Greeks:** Positive theta, negative vega, negative gamma
- **Management:** Take profits at 50%, cut losses at 2x credit

> Credit spreads are best understood as **controlled income strategies**, not directional speculation.