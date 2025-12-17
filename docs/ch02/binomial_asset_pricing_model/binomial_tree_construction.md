# Binomial Tree Construction

This page focuses on the *mechanics* of the binomial tree: how stock prices populate the tree, how to choose the up/down factors \((u,d)\), and how the **risk-neutral probability** arises from no-arbitrage.

> Notation note. In pricing, we typically reserve \(q\) (or \(p^\ast\)) for the **risk-neutral** up probability, to distinguish it from a “physical” probability under \(\mathbb{P}\).  
> In this chapter we will use \(q\) for the **risk-neutral up probability** unless stated otherwise.

---

## 1. Stock Price Evolution on a Tree

Fix a time step \(\Delta t\). The binomial model assumes that over each step, the stock price either

- goes **up** by a factor \(u>1\), or
- goes **down** by a factor \(d<1\).

Let \(S_0\) be the initial stock price. Then after one step,


\[
S_1 =
\begin{cases}
S_0 u & \text{up}\\
S_0 d & \text{down}.
\end{cases}
\]



After two steps, the possible prices are


\[
S_2 \in \{S_0 u^2,\; S_0 u d,\; S_0 d^2\}.
\]



More generally, after \(n\) steps, if the path has \(j\) up-moves and \(n-j\) down-moves, then


\[
\boxed{
S_n = S_0 u^j d^{\,n-j}.
}
\]



If one assigns an **up probability** \(p\) (under some measure), the probability of exactly \(j\) up-moves in \(n\) steps is binomial:


\[
\mathbb{P}(\text{#up}=j) = {n\choose j} p^j (1-p)^{n-j}.
\]



For pricing, however, the key probability is the **risk-neutral** one, derived from no-arbitrage (Section 3 below).

---

## 2. How to Choose \(u\) and \(d\)

There are several common parameterizations. Let \(\sigma\) be volatility and \(\Delta t\) the step size.

### 2.1 Linear factors (Wilmott-style)

\[
u = 1 + \sigma\sqrt{\Delta t},\qquad d = 1 - \sigma\sqrt{\Delta t}.
\]



**Pros**
- Simple and fast to compute.

**Cons**
- Can be inaccurate for large \(\sigma\) or \(\Delta t\).
- If \(\sigma\sqrt{\Delta t} > 1\), then \(d\) becomes negative (not acceptable for stock prices).

---

### 2.2 Exponential factors (Cox–Ross–Rubinstein, CRR)

\[
\boxed{
u = e^{\sigma\sqrt{\Delta t}},\qquad d = e^{-\sigma\sqrt{\Delta t}}.
}
\]



**Pros**
- Always positive.
- Matches the lognormal structure of geometric Brownian motion (GBM) in the small-step limit.

**Cons**
- Slightly more computation (usually negligible).

---

### 2.3 Drift-adjusted exponential factors (Jarrow–Rudd / lognormal matching)
One may incorporate a drift-like centering term:

\[
u = e^{(r - \tfrac12\sigma^2)\Delta t + \sigma\sqrt{\Delta t}},\qquad
d = e^{(r - \tfrac12\sigma^2)\Delta t - \sigma\sqrt{\Delta t}}.
\]



**Pros**
- Can improve matching of certain moments in discrete approximations.

**Cons**
- More moving parts; be careful about which drift (\(\mu\) vs \(r\)) you intend to match.

> For **risk-neutral pricing**, the drift in the *continuous* limit is \(r\), but the discrete tree is driven by \(u,d\) and the risk-neutral probability \(q\).

---

## 3. Risk-Neutral Probability from No-Arbitrage

Let the per-step risk-free growth factor be

\[
R := e^{r\Delta t}
\quad\text{(or } R \approx 1+r\Delta t\text{ for small }\Delta t\text{)}.
\]



**No-arbitrage** requires

\[
d < R < u.
\]



Under this condition, define the **risk-neutral up probability** \(q\) by forcing the *expected* one-step growth of the stock to match the risk-free rate:


\[
\mathbb{E}^{\mathbb{Q}}[S_{n+1} \mid \mathcal{F}_n]
= q(uS_n) + (1-q)(dS_n)
= R S_n.
\]



Solving for \(q\) gives:


\[
\boxed{
q = \frac{R - d}{u-d} = \frac{e^{r\Delta t} - d}{u-d}.
}
\]



Then \(q\in(0,1)\), and discounted prices become martingales under \(\mathbb{Q}\):


\[
\mathbb{E}^{\mathbb{Q}}\left[\frac{S_{n+1}}{R} \mid \mathcal{F}_n\right] = S_n.
\]



This is the discrete-time version of “risk-neutral pricing.”

---

## 4. Pricing by Backward Induction (One Line Preview)

If \(V_{n+1}^{(u)}\) and \(V_{n+1}^{(d)}\) are the option values at the up/down children of a node, then:


\[
\boxed{
V_n = e^{-r\Delta t}\Big(q V_{n+1}^{(u)} + (1-q) V_{n+1}^{(d)}\Big).
}
\]



We develop this more systematically in `multi_period_binomial_tree.md`.

---

## 5. Python Example: Visualize a Binomial Tree

Below is a compact example that:

- computes \(u,d,q\) (CRR / JR / Wilmott-style),
- builds the stock tree,
- visualizes the tree.

```python
import numpy as np
import matplotlib.pyplot as plt


class BinomialParameter:
    def __init__(self, r, sigma, T, M, model='CRR'):
        self.r = r
        self.sigma = sigma
        self.T = T
        self.M = M
        self.model = model

        self.dt = T / M
        self.U, self.D, self.q_u, self.q_d = self._compute()

    def _compute(self):
        dt = self.dt
        sqrt_dt = np.sqrt(dt)
        r, sigma = self.r, self.sigma

        if self.model == 'Wilmott':
            u, d = 1 + sigma * sqrt_dt, 1 - sigma * sqrt_dt
        elif self.model == 'CRR':
            u, d = np.exp(sigma * sqrt_dt), np.exp(-sigma * sqrt_dt)
        elif self.model == 'JR':
            drift = (r - 0.5 * sigma ** 2) * dt
            u = np.exp(drift + sigma * sqrt_dt)
            d = np.exp(drift - sigma * sqrt_dt)
        else:
            raise ValueError("Invalid model")

        q_u = (np.exp(r * dt) - d) / (u - d)
        return u, d, q_u, 1 - q_u


class BinomialPlotter:
    def __init__(self, S0, params: BinomialParameter):
        self.S0 = S0
        self.params = params

    def plot_tree(self):
        M, U, D = self.params.M, self.params.U, self.params.D
        S0 = self.S0
        tree = []

        for i in range(M + 1):
            nodes = [(S0 * (U ** j) * (D ** (i - j))) for j in range(i + 1)]
            tree.append(nodes)

        fig, ax = plt.subplots(figsize=(12, 6))

        for i in range(M):
            for j in range(i + 1):
                x, y = i, tree[i][j]
                ax.plot([x, x + 1], [y, tree[i + 1][j + 1]], lw=1)
                ax.plot([x, x + 1], [y, tree[i + 1][j]], lw=1)

        for i in range(M + 1):
            for j in range(i + 1):
                x, y = i, tree[i][j]
                ax.scatter(x, y, s=40, zorder=5)
                ax.text(x, y, f'{y:.2f}', fontsize=9, ha='left', va='bottom')

        ax.set_title('Binomial Tree for Stock Price Evolution', fontsize=14)
        ax.set_xlabel('Time Step')
        ax.set_ylabel('Stock Price')
        for spine in ["top", "right", "left"]:
            ax.spines[spine].set_visible(False)
        ax.set_yticks([])
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    S0 = 100
    T = 1/12
    r = 0.03
    sigma = 0.3
    M = 5

    params = BinomialParameter(r, sigma, T, M, model='CRR')
    BinomialPlotter(S0, params).plot_tree()
```

---

## 6. Summary

- The binomial tree organizes stock prices as \(S_n = S_0 u^j d^{n-j}\).
- Common choices of \(u,d\): linear (Wilmott), exponential (CRR), drift-adjusted (JR).
- No-arbitrage implies \(d < e^{r\Delta t} < u\), and this yields a **unique** risk-neutral probability
  \(q = \frac{e^{r\Delta t}-d}{u-d}\).
- Pricing follows by discounting the risk-neutral conditional expectation.
