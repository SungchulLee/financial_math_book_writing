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

## Debit Spreads as

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

## Common Structure

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

### 1. Key Properties of

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

## Comparison

| Feature | Long Call Spread | Long Put Spread |
|------|------------------|----------------|
| Bias | Bullish | Bearish |
| Bought Option | Call | Put |
| Profit If | Price rises | Price falls |
| Risk | Downside | Upside |

---

## When to Use Debit

Debit spreads are well-suited when:

- You have a **directional conviction**
- You want to reduce option premium cost
- Implied volatility is **low to moderate**
- You prefer defined-risk directional strategies

---

## Key Takeaways

- Debit spreads are **vertical spreads entered for a net debit**
- The two canonical forms are:
  - **Long Call Spread (Bull Call)**
  - **Long Put Spread (Bear Put)**
- Risk is limited to the premium paid
- Profit is capped but capital efficiency is improved

> Debit spreads are best viewed as **cost-efficient directional trades**, not volatility bets.