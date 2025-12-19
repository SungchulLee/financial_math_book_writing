# Exercises: Binomial Asset Pricing Model



---

## 1. No-Arbitrage Condition

Let \(S_0=100\), \(u=1.2\), \(d=0.9\), and \(r=0.05\). 
 
1) Check whether \(d < 1+r < u\) holds.  
2) If it fails, describe an arbitrage strategy.

---

## 2. Risk-Neutral Probability

Using Exercise 1 parameters, compute

\[
q = \frac{(1+r)-d}{u-d}.
\]


Verify \(q\in(0,1)\).

---

## 3. One-Period European Call (Replication)

Let \(K=105\) and \(H=(S_1-K)^+\).  

1) Compute \(H_u\), \(H_d\).  
2) Find \(\Delta\) and \(\beta\).  
3) Compute \(V_0\).

---

## 4. One-Period European Put (Risk-Neutral Pricing)

Price \(H=(K-S_1)^+\) using

\[
V_0 = \frac{1}{1+r}\,\mathbb{E}^{\mathbb{Q}}[H].
\]



---

## 5. Put–Call Parity

Show:

\[
C_0 - P_0 = S_0 - \frac{K}{1+r}.
\]



---

## 6. Two-Step Tree (Backward Induction)

With \(N=2\) steps and strike \(K=105\), price a European call by backward induction.

---

## 7. Node-by-Node Delta

In Exercise 6, compute:

1) \(\Delta_0\) at time 0,  
2) the deltas at time 1 in each node.

Interpret the difference.

---

## 8. Completeness (Conceptual)

Explain why the binomial model is complete.  
Describe one modification that would make a discrete-time market incomplete.
