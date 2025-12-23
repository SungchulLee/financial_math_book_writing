# Binomial Option Pricing via Classical Hedging

## Purpose of This Chapter

The goal of this chapter is to derive option prices using the following logic:

> **Hedging → risk-free portfolio → pricing**

We do **not** begin with probability measures or martingales.  
Instead, prices are determined by constructing portfolios that eliminate risk and invoking the risk-free rate.

Risk-neutral probabilities will appear **only as a convenient reformulation**, not as an assumption.

---

## 1. Market Setup

We consider a one-period market with times \(t=0,dt\).

### Risk-Free Asset

The bank account evolves according to continuous compounding:

\[
B_0 = 1, \qquad B_{dt} = e^{r dt}
\]

---

### Stock

The stock price evolves as

\[
S_{dt} =
\begin{cases}
u S_0 & \text{(up move)} \\
d S_0 & \text{(down move)}
\end{cases}
\qquad 0 < d < e^{r dt} < u
\]

The inequality \(d < e^{r dt} < u\) ensures that neither the stock nor the bank dominates the other, ruling out trivial arbitrage.

---

## 2. The Option Payoff

Let an option have terminal payoff

\[
H =
\begin{cases}
H_u & \text{if the stock goes up} \\
H_d & \text{if the stock goes down}
\end{cases}
\]

We denote the option price at time 0 by \(V_0\).

Our task is to determine \(V_0\).

---

## 3. Hedging Idea

The option payoff depends on the stock price and is therefore risky.

To eliminate this risk, we combine the option with a position in the stock.  
The idea is to choose the stock position so that **stock-price fluctuations cancel out**.

This is the essence of **classical hedging**.

---

## 4. Construction of a Hedged Portfolio

Consider a portfolio consisting of:

* one **short** option,
* \(\Delta\) shares of the stock.

The value of this portfolio at maturity is

\[
\Pi_{dt} =
\begin{cases}
\Delta u S_0 - H_u & \text{(up)} \\
\Delta d S_0 - H_d & \text{(down)}
\end{cases}
\]

---

## 5. Elimination of Stock Risk

We choose \(\Delta\) so that the portfolio has the **same value in both states**:

\[
\Delta u S_0 - H_u
=
\Delta d S_0 - H_d
\]

Solving for \(\Delta\),

\[
\boxed{
\Delta = \frac{H_u - H_d}{(u-d)S_0}
}
\]

With this choice, the terminal value of the portfolio becomes

\[
\Pi_{dt} = \frac{u H_d - d H_u}{u-d}
\]

which is **deterministic**.

The portfolio is therefore **risk-free**.

---

## 6. Risk-Free Pricing Principle

A fundamental economic principle is:

> **Any risk-free portfolio must earn the risk-free rate.**

Let \(\Pi_0\) denote the initial value of the hedged portfolio:

\[
\Pi_0 = \Delta S_0 - V_0
\]

Since the portfolio is risk-free,

\[
\Pi_0 = e^{-rdt} \Pi_{dt}
\]

That is,

\[
\Delta S_0 - V_0
=
e^{-rdt}\frac{u H_d - d H_u}{u-d}
\]

---

## 7. Option Pricing Formula

Substituting the expression for \(\Delta\) and solving for \(V_0\), we obtain

\[
\boxed{
V_0
=
e^{-r}\left(
\frac{e^{r dt} - d}{u-d} H_u
+
\frac{u - e^{r dt}}{u-d} H_d
\right)
}
\]

This is the **arbitrage-free price** of the option.

---

## 8. Interpretation: Emergence of Risk-Neutral Probability

Define

\[
\boxed{
q := \frac{e^{r dt} - d}{u-d}
}
\]

Then the pricing formula can be written compactly as

\[
V_0 = e^{-r}\big(q H_u + (1-q) H_d\big)
\]

The number \(q\) lies in \((0,1)\) and can be interpreted as a probability.

---

### Important Remark

The probability \(q\) is **not** a real-world probability and is **not assumed** in advance.

It arises naturally from the requirement that a hedged portfolio be risk-free and earn the risk-free rate.

For this reason, \(q\) is called the **risk-neutral probability**.

---

## 9. Key Takeaways

* Hedging eliminates stock-price risk
* Risk-free portfolios must earn the risk-free rate
* Prices are determined by enforcing this principle
* Probability enters only as a representation, not as an axiom

---

## 10. Looking Ahead

In multi-period models, the same hedging argument is applied **locally at each node**, leading to dynamic delta hedging.

In the continuous-time limit, this logic yields the Black–Scholes equation.

---

> **Pricing is a consequence of hedging.  
> Probability is a language, not a foundation.**
