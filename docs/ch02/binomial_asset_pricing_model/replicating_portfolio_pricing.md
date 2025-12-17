# Replicating Portfolio and Pricing

A key feature of the binomial model is **completeness**: every payoff \(H(S_1)\) can be replicated by trading in \(S\) and \(B\).
This implies that the no-arbitrage price is **unique**.

---

## 1. Payoff and Replication

Let the claim payoff be

\[
H =
\begin{cases}
H_u := H(uS_0) & \text{up}\\
H_d := H(dS_0) & \text{down}.
\end{cases}
\]



We seek \((\Delta,\beta)\) such that the portfolio payoff matches \(H\) in both states:

\[
\Delta (uS_0) + \beta(1+r) = H_u,
\]



\[
\Delta (dS_0) + \beta(1+r) = H_d.
\]



---

## 2. Solve for the Hedge Ratio \(\Delta\)

Subtract the equations:

\[
\Delta(u-d)S_0 = H_u - H_d,
\]


so

\[
\boxed{
\Delta = \frac{H_u - H_d}{(u-d)S_0}.
}
\]



---

## 3. Solve for the Bond Position \(\beta\)

Plug \(\Delta\) into one equation:

\[
\beta(1+r) = H_u - \Delta uS_0,
\]


so

\[
\boxed{
\beta = \frac{H_u - \Delta uS_0}{1+r}.
}
\]



---

## 4. The Replication Price

The no-arbitrage price must equal the cost of the replicating portfolio:

\[
V_0 = \Delta S_0 + \beta.
\]



Using algebra, this can be rewritten as:

\[
\boxed{
V_0 = \frac{1}{1+r}\Big(qH_u + (1-q)H_d\Big),
}
\]


where \(q\) is the risk-neutral probability.

---

## 5. Why Replication Implies Uniqueness

If two different prices were assigned to the same payoff, one could buy the cheaper and sell the expensive version and lock in an arbitrage.  
Hence in a complete binomial model the no-arbitrage price is **unique**.
