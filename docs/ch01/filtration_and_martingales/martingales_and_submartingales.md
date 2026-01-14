# Martingales


## Conditional


Let \(\mathcal{G}\subseteq\mathcal{F}\) be a sub-\(\sigma\)-algebra and \(X\in L^1(\Omega)\). The conditional expectation \(\mathbb{E}[X\mid \mathcal{G}]\) is the unique (a.s.) \(\mathcal{G}\)-measurable random variable satisfying


$$
\int_G \mathbb{E}[X\mid \mathcal{G}]\,\mathrm{d}\mathbb{P}
=
\int_G X\,\mathrm{d}\mathbb{P}
\quad\text{for all }G\in\mathcal{G}.
$$





---

## Martingale


An integrable adapted process \(M=\{M_t\}_{t\ge 0}\) is a **martingale** if for all \(0\le s\le t\),


$$
\boxed{
\mathbb{E}[M_t\mid \mathcal{F}_s] = M_s.
}
$$




Interpretation: “fair game” given current information.

A process is a **supermartingale** if


$$
\mathbb{E}[M_t\mid \mathcal{F}_s] \le M_s,
$$




and a **submartingale** if


$$
\mathbb{E}[M_t\mid \mathcal{F}_s] \ge M_s.
$$





---

## Examples


### 1. Brownian motion



$$
\mathbb{E}[W_t\mid \mathcal{F}_s]=W_s,
\quad 0\le s\le t,
$$




so \(\{W_t\}\) is a martingale.

### 2. Quadratic marting

Using Itô calculus later, one shows


$$
\boxed{
W_t^2 - t \text{ is a martingale.}
}
$$





### 3. Conditional expec

For fixed \(X\in L^1(\Omega)\), the process


$$
M_t := \mathbb{E}[X\mid \mathcal{F}_t]
$$




is a martingale (Doob martingale).

---

## Martingale


For a martingale \(M_t\),


$$
\mathbb{E}[M_t-M_s\mid\mathcal{F}_s]=0.
$$




The increments need not be independent; martingales generalize independence.

---

## Doob decomposition


In discrete time, every integrable adapted process \(X_n\) can be decomposed as


$$
X_n = M_n + A_n,
$$




where \(M_n\) is a martingale and \(A_n\) is predictable with finite variation. In continuous time, this becomes the semimartingale decomposition (finite variation part + local martingale part), which is the structural class behind Itô calculus.

---

## Martingale


Martingale theory is powerful because of maximal inequalities and convergence theorems. Examples include:

- Doob’s \(L^p\) maximal inequality:


$$
\left\|\sup_{0\le s\le t}|M_s|\right\|_{L^p}
\le
\frac{p}{p-1}\|M_t\|_{L^p},
\qquad p>1,
$$




for nonnegative submartingales (and versions for martingales).

These tools will be useful when proving existence/uniqueness and studying stochastic exponentials.
