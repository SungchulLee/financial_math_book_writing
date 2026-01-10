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

## Credit Spreads as

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

## Common Structure

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

### 1. Key Properties of

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

## Comparison

| Feature | Short Call Spread | Short Put Spread |
|------|------------------|------------------|
| Bias | Bearish / Neutral | Bullish / Neutral |
| Sold Option | Call | Put |
| Profit If | Price stays below short call | Price stays above short put |
| Risk | Upside | Downside |

---

## When to Use Credit

Credit spreads are well-suited when:

- You expect **range-bound** or mildly trending markets
- Implied volatility is **moderate to high**
- You want **defined risk income strategies**
- You prefer probability-based trading over large directional bets

---

## Key Takeaways

- Credit spreads are **vertical spreads entered for a net credit**
- The two canonical forms are:
  - **Short Call Spread (Bear Call)**
  - **Short Put Spread (Bull Put)**
- Risk and reward are **known in advance**
- Time decay is your ally, but strong directional moves are your enemy

> Credit spreads are best understood as **controlled income strategies**, not directional speculation.