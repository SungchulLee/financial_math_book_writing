# Martingale Properties of Brownian Motion

The martingale property is one of the defining features of Brownian motion and underpins its role in stochastic calculus, financial modeling, and diffusion theory. In this section, we explore the various martingales associated with Brownian motion, beginning with foundational definitions and gradually building up to polynomial and exponential martingales.

---

## Definition of martingales

Recall that a filtered probability space \((\Omega, \mathcal{F}, (\mathcal{F}_t)_{t\ge 0}, \mathbb{P})\) consists of a probability space together with a filtration—an increasing family of \(\sigma\)-algebras representing information available up to time \(t\).

A stochastic process \(X = \{X_t\}_{t\ge 0}\) is a **martingale** with respect to the filtration \(\{\mathcal{F}_t\}\) if:

1. **Adaptedness**: \(X_t\) is \(\mathcal{F}_t\)-measurable for all \(t \ge 0\),
2. **Integrability**: \(\mathbb{E}|X_t| < \infty\) for all \(t \ge 0\),
3. **Martingale property**: For all \(0 \le s < t\):


   $$
   \mathbb{E}[X_t \mid \mathcal{F}_s] = X_s
   $$



**Interpretation**: A martingale represents a "fair game"—the best prediction of the future value \(X_t\), given all information up to time \(s\), is simply the current value \(X_s\).

**Submartingales and supermartingales**: If the equality is replaced by \(\mathbb{E}[X_t \mid \mathcal{F}_s] \ge X_s\), we have a **submartingale** (drifts upward on average). If \(\mathbb{E}[X_t \mid \mathcal{F}_s] \le X_s\), we have a **supermartingale** (drifts downward on average).

---

## Brownian motion as a martingale

Let \(B_t\) be a standard Brownian motion with respect to its natural filtration \(\mathcal{F}_t = \sigma(B_s: 0 \le s \le t)\). We verify that \(B_t\) is a martingale.

**Proof**: For \(0 \le s < t\), write:


$$
\mathbb{E}[B_t \mid \mathcal{F}_s]
= \mathbb{E}[B_s + (B_t - B_s) \mid \mathcal{F}_s]
= B_s + \mathbb{E}[B_t - B_s \mid \mathcal{F}_s]
$$



Since \(B_t - B_s\) is independent of \(\mathcal{F}_s\) (by the independent increments property) and has zero mean:


$$
\mathbb{E}[B_t - B_s \mid \mathcal{F}_s] = \mathbb{E}[B_t - B_s] = 0
$$



Therefore:


$$
\mathbb{E}[B_t \mid \mathcal{F}_s] = B_s
$$




$$
\boxed{B_t \text{ is a martingale with respect to its natural filtration.}}
$$



This fundamental property—that Brownian motion is a martingale—is central to stochastic calculus and mathematical finance. It formalizes the idea that Brownian motion has "no drift" and exhibits purely random fluctuations.

---

## Polynomial martingales

Simple polynomial functions of Brownian motion can be adjusted to yield martingales. We establish two key examples.

### $B_t^2 - t$ is a martingale

**Claim**: The process \(M_t = B_t^2 - t\) is a martingale.

**Proof**: For \(0 \le s < t\), we compute:


$$
\mathbb{E}[B_t^2 \mid \mathcal{F}_s]
= \mathbb{E}[(B_s + (B_t - B_s))^2 \mid \mathcal{F}_s]
$$



Expanding:


$$
= \mathbb{E}[B_s^2 + 2B_s(B_t - B_s) + (B_t - B_s)^2 \mid \mathcal{F}_s]
$$



Since \(B_s\) is \(\mathcal{F}_s\)-measurable and \(B_t - B_s\) is independent of \(\mathcal{F}_s\):


$$
= B_s^2 + 2B_s \cdot \mathbb{E}[B_t - B_s] + \mathbb{E}[(B_t - B_s)^2]
$$



Using \(\mathbb{E}[B_t - B_s] = 0\) and \(\text{Var}(B_t - B_s) = t - s\):


$$
= B_s^2 + 0 + (t - s) = B_s^2 + (t - s)
$$



Therefore:


$$
\mathbb{E}[B_t^2 - t \mid \mathcal{F}_s] = B_s^2 + (t - s) - t = B_s^2 - s
$$



Hence:


$$
\boxed{B_t^2 - t \text{ is a martingale.}}
$$



**Interpretation**: While \(B_t^2\) grows on average (since \(\mathbb{E}[B_t^2] = t\)), subtracting the deterministic term \(t\) removes this trend, yielding a martingale.

### $B_t^3 - 3tB_t$ is a martingale

**Claim**: The process \(M_t = B_t^3 - 3tB_t\) is a martingale.

**Sketch of proof**: Using the binomial expansion and properties of Brownian increments:


$$
\mathbb{E}[B_t^3 \mid \mathcal{F}_s]
= \mathbb{E}[(B_s + (B_t - B_s))^3 \mid \mathcal{F}_s]
$$



Expanding and using independence:


$$
= B_s^3 + 3B_s^2 \cdot \mathbb{E}[B_t - B_s] + 3B_s \cdot \mathbb{E}[(B_t - B_s)^2] + \mathbb{E}[(B_t - B_s)^3]
$$



Since \(\mathbb{E}[B_t - B_s] = 0\), \(\mathbb{E}[(B_t - B_s)^2] = t - s\), and \(\mathbb{E}[(B_t - B_s)^3] = 0\) (by symmetry):


$$
= B_s^3 + 3B_s(t - s)
$$



Therefore:


$$
\mathbb{E}[B_t^3 - 3tB_t \mid \mathcal{F}_s]
= B_s^3 + 3B_s(t - s) - 3tB_s
= B_s^3 - 3sB_s
$$



Hence:


$$
\boxed{B_t^3 - 3tB_t \text{ is a martingale.}}
$$



**General pattern**: Higher-order polynomial martingales follow similar constructions. The correction terms arise from the moments of Brownian increments.

---

## Exponential martingale

One of the most important martingales in stochastic analysis is the **exponential martingale**:


$$
\boxed{Z_t = \exp\left( \theta B_t - \frac{1}{2} \theta^2 t \right)}
$$



For any \(\theta \in \mathbb{R}\), the process \(Z_t\) is a strictly positive \(\mathcal{F}_t\)-martingale.

**Verification**: For \(0 \le s < t\), write:


$$
Z_t = \exp\left( \theta(B_s + (B_t - B_s)) - \frac{1}{2}\theta^2 t \right)
= Z_s \cdot \exp\left( \theta(B_t - B_s) - \frac{1}{2}\theta^2(t - s) \right)
$$



Taking conditional expectation:


$$
\mathbb{E}[Z_t \mid \mathcal{F}_s]
= Z_s \cdot \mathbb{E}\left[\exp\left( \theta(B_t - B_s) - \frac{1}{2}\theta^2(t - s) \right)\right]
$$



Since \(B_t - B_s \sim N(0, t-s)\) is independent of \(\mathcal{F}_s\):


$$
\mathbb{E}\left[\exp(\theta(B_t - B_s))\right] = \exp\left(\frac{1}{2}\theta^2(t - s)\right)
$$



(This is the moment-generating function of a normal random variable.) Therefore:


$$
\mathbb{E}[Z_t \mid \mathcal{F}_s]
= Z_s \cdot \exp\left(\frac{1}{2}\theta^2(t - s) - \frac{1}{2}\theta^2(t - s)\right)
= Z_s
$$



Thus:


$$
\boxed{Z_t = \exp\left( \theta B_t - \frac{1}{2} \theta^2 t \right) \text{ is a martingale.}}
$$



**Applications**:

- **Girsanov's theorem**: \(Z_t\) serves as the Radon–Nikodym derivative for measure changes, allowing us to transform drift in stochastic differential equations.
- **Risk-neutral pricing**: In financial mathematics, exponential martingales are used to change from the physical measure to the risk-neutral measure.
- **Wald's identity**: The exponential martingale plays a key role in optional stopping theorems and the analysis of first-passage times.

---

## Connection via Taylor expansion

The polynomial and exponential martingales are intimately connected. Expanding the exponential martingale in powers of \(\theta\):


$$
\exp\left( \theta B_t - \frac{1}{2} \theta^2 t \right)
= \sum_{n=0}^\infty \frac{1}{n!} \left( \theta B_t - \frac{1}{2} \theta^2 t \right)^n
$$



Since the entire expression is a martingale, **the coefficient of each power of \(\theta\) must also be a martingale** (by linearity of conditional expectation). Collecting terms:


$$
\begin{array}{lll}
\displaystyle
\text{Power of } \theta^0:&&\displaystyle 1&&\text{Martingale}\\
\\
\text{Power of } \theta^1:&&\displaystyle B_t&&\text{Martingale}\\
\\
\text{Power of } \theta^2:&&\displaystyle \frac{B_t^2}{2} - \frac{t}{2} \quad \Rightarrow \quad B_t^2 - t&&\text{Martingale}\\
\\
\text{Power of } \theta^3:&&\displaystyle \frac{B_t^3}{6} - \frac{3tB_t}{6} \quad \Rightarrow \quad B_t^3 - 3tB_t&&\text{Martingale}\\
\\
\vdots
\end{array}
$$



This elegant observation shows that:

1. All polynomial martingales arise naturally from the exponential martingale,
2. The correction terms (like \(-t\) in \(B_t^2 - t\)) are determined by the variance structure,
3. Higher-order polynomial martingales follow a systematic pattern.

This connection extends to Itô's formula, where the exponential martingale's form reveals the quadratic variation structure of Brownian motion.

---

## Summary

The martingale properties of Brownian motion form a cornerstone of stochastic analysis:

- **Brownian motion itself**: \(B_t\) is a martingale, formalizing its "fair game" nature.
- **Polynomial martingales**: Simple polynomials corrected by deterministic drift terms:


  $$
  B_t^2 - t, \quad B_t^3 - 3t B_t, \quad \ldots
  $$



- **Exponential martingale**: The process


  $$
  Z_t = \exp\left( \theta B_t - \frac{1}{2} \theta^2 t \right)
  $$



  is central to measure change (Girsanov's theorem) and risk-neutral pricing.

- **Unified structure**: All polynomial martingales emerge as coefficients in the Taylor expansion of the exponential martingale, revealing deep connections between seemingly different constructions.

These martingales serve as building blocks for:

- Stochastic integration (Itô calculus)
- Change of measure techniques
- Option pricing and hedging strategies
- Analysis of stopping times and first-passage problems

In the sections that follow, we develop the theory of stopping times and the Optional Sampling Theorem, which allow us to systematically study these martingales at random times.
