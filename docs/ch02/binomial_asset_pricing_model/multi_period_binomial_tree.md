# Multi-Period Binomial Tree

The one-period model extends naturally to \(N\) steps, producing the **binomial tree** and introducing **dynamic replication**.

---

## 1. Model

Let \(\Delta t = T/N\). Define a grid:


\[
t_n = n\Delta t,\qquad n=0,1,\dots,N.
\]





Stock evolution:


\[
S_{n+1} =
\begin{cases}
u S_n & \text{up} \\
d S_n & \text{down}
\end{cases}
\]





Bank account:


\[
B_{n+1} = (1+r) B_n
\quad\Rightarrow\quad
B_n = (1+r)^n.
\]





---

## 2. Backward Induction Pricing

Let the claim payoff at time \(N\) be \(H(S_N)\). Define:


\[
V_n = V(t_n,S_n).
\]





Then:


\[
\boxed{
V_n = \frac{1}{1+r}\Big(q V_{n+1}^{(u)} + (1-q)V_{n+1}^{(d)}\Big),
}
\]




where \(q = \frac{(1+r)-d}{u-d}\).

---

## 3. Dynamic Delta

At each node \((n,S_n)\),


\[
\boxed{
\Delta_n = \frac{V_{n+1}^{(u)} - V_{n+1}^{(d)}}{(u-d)S_n}.
}
\]





This is discrete-time delta hedging.
