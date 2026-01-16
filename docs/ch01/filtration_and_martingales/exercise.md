# Exercises: Filtrations and Martingales

Throughout these exercises, let $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \ge 0}, \mathbb{P})$ denote a filtered probability space satisfying the usual conditions, and let $(W_t)_{t \ge 0}$ denote a standard Brownian motion.

---

## Part I: Filtrations and Information

### Exercise 1.1: Filtration Basics

(a) Prove that if $\mathcal{F}_s \subseteq \mathcal{F}_t$ for all $s \le t$, then $\bigcup_{t \ge 0} \mathcal{F}_t$ is an algebra but not necessarily a $\sigma$-algebra.

(b) Show that the natural filtration $\mathcal{F}_t^W = \sigma(W_s : 0 \le s \le t)$ satisfies $\mathcal{F}_s^W \subseteq \mathcal{F}_t^W$ for $s \le t$.

(c) Give an example of a random variable that is $\mathcal{F}_1$-measurable but not $\mathcal{F}_0$-measurable.

### Exercise 1.2: Adapted Processes

(a) Prove that if $X_t$ and $Y_t$ are adapted to $(\mathcal{F}_t)$, then so is $X_t + Y_t$.

(b) Show that $W_{t+1}$ is **not** adapted to the natural filtration $(\mathcal{F}_t^W)$.

(c) Let $X_t = \int_0^t W_s \, ds$. Prove that $X_t$ is adapted to $(\mathcal{F}_t^W)$.

### Exercise 1.3: Right-Continuity

(a) Explain intuitively why right-continuity of filtrations ($\mathcal{F}_t = \bigcap_{s > t} \mathcal{F}_s$) is useful for stopping time theory.

(b) Give an example of a filtration that is not right-continuous.

(c) Prove that if $\tau$ is a stopping time with respect to a right-continuous filtration, then $\{\tau < t\} \in \mathcal{F}_t$ for all $t$.

### Exercise 1.4: Progressive Measurability

(a) State the definition of a progressively measurable process.

(b) Prove that every left-continuous adapted process is progressively measurable.

(c) Why is progressive measurability sufficient (but predictability preferred) for defining stochastic integrals?

---

## Part II: Martingales — Definitions and Examples

### Exercise 2.1: Verifying Martingales

Determine whether each process is a martingale, submartingale, or supermartingale. Prove your answers.

(a) $M_t = W_t^2 - t$

(b) $M_t = e^{W_t}$

(c) $M_t = W_t^3 - 3tW_t$

(d) $M_t = \sin(W_t)$

(e) $M_t = W_t^4 - 6tW_t^2 + 3t^2$

### Exercise 2.2: The Doob Martingale

Let $X \in L^1(\mathcal{F})$ and define $M_t = \mathbb{E}[X \mid \mathcal{F}_t]$.

(a) Prove that $(M_t)$ is a martingale using the tower property.

(b) Show that if $X = W_T$ for some $T > 0$, then $M_t = W_{t \wedge T}$.

(c) Find $M_t$ when $X = W_T^2$ for $t \le T$.

### Exercise 2.3: Transforms of Martingales

(a) Prove that if $M_t$ is a martingale and $\varphi$ is a convex function with $\mathbb{E}|\varphi(M_t)| < \infty$, then $\varphi(M_t)$ is a submartingale.

(b) Deduce that $|W_t|$, $W_t^2$, and $(W_t)^+$ are all submartingales.

(c) Is $\log(1 + W_t^2)$ a submartingale? Prove or disprove.

### Exercise 2.4: Discrete Martingales

Let $\xi_1, \xi_2, \ldots$ be i.i.d. with $\mathbb{P}(\xi_i = 1) = p$ and $\mathbb{P}(\xi_i = -1) = 1-p$.

(a) For what value of $p$ is $S_n = \sum_{k=1}^n \xi_k$ a martingale?

(b) For general $p$, find a function $f$ such that $f(S_n, n)$ is a martingale.

(c) Show that $M_n = \left(\frac{1-p}{p}\right)^{S_n}$ is a martingale when $p \neq 1/2$.

---

## Part III: The Exponential Martingale

### Exercise 3.1: Verification

(a) Prove directly that $Z_t^\theta = \exp(\theta W_t - \frac{\theta^2 t}{2})$ is a martingale for any $\theta \in \mathbb{R}$.

(b) Compute $\mathbb{E}[Z_t^\theta]$ and $\text{Var}(Z_t^\theta)$.

(c) Show that $Z_t^\theta \to 0$ almost surely as $t \to \infty$ for $\theta \neq 0$.

### Exercise 3.2: Generating Polynomial Martingales

(a) Expand $\exp(\theta W_t - \frac{\theta^2 t}{2})$ as a power series in $\theta$ up to order 4.

(b) Identify the coefficient of $\theta^4$ and verify it is a martingale.

(c) State the general pattern: what is the martingale corresponding to $\theta^n$?

### Exercise 3.3: Two-Sided Exponential

Consider $Z_t = \cosh(\theta W_t) \exp(-\frac{\theta^2 t}{2})$.

(a) Prove that $Z_t$ is a martingale.

(b) Express $Z_t$ in terms of exponential martingales with parameters $\pm\theta$.

(c) Find the analogous martingale involving $\sinh$.

---

## Part IV: Stopping Times

### Exercise 4.1: Stopping Time Verification

Determine which of the following are stopping times. Justify your answers.

(a) $\tau = \inf\{t \ge 0 : W_t = 1\}$

(b) $\tau = \sup\{t \le 1 : W_t = 0\}$

(c) $\tau = \inf\{t \ge 0 : W_t > W_s \text{ for all } s < t\}$

(d) $\tau = \inf\{t \ge 0 : \int_0^t W_s \, ds \ge 1\}$

(e) $\tau = \inf\{t \ge 1 : W_t = W_{t-1}\}$

### Exercise 4.2: Operations on Stopping Times

Let $\sigma$ and $\tau$ be stopping times.

(a) Prove that $\sigma \wedge \tau$ is a stopping time.

(b) Prove that $\sigma + \tau$ is a stopping time (assuming both are finite a.s.).

(c) Give a counterexample showing that $\sigma - \tau$ need not be a stopping time.

### Exercise 4.3: The $\sigma$-Algebra $\mathcal{F}_\tau$

Let $\tau = \inf\{t : W_t = 1\}$.

(a) Show that $W_\tau$ is $\mathcal{F}_\tau$-measurable.

(b) Is $W_{\tau + 1}$ $\mathcal{F}_\tau$-measurable?

(c) Describe $\mathcal{F}_\tau$ in words.

### Exercise 4.4: Strong Markov Property

(a) State the strong Markov property for Brownian motion.

(b) Let $\tau_a = \inf\{t : W_t = a\}$. Use the strong Markov property to show that $\tau_a + \tau_b \circ \theta_{\tau_a}$ has the same distribution as $\tau_{a+b}$, where $\theta$ is the shift operator.

(c) Derive the reflection principle: $\mathbb{P}(\sup_{s \le t} W_s \ge a) = 2\mathbb{P}(W_t \ge a)$ for $a > 0$.

---

## Part V: Optional Sampling

### Exercise 5.1: Bounded Stopping Times

Let $\tau = \inf\{t : W_t \notin (-1, 1)\}$.

(a) Apply the optional sampling theorem to $W_t$ to find $\mathbb{E}[W_\tau]$.

(b) Apply optional sampling to $W_t^2 - t$ to find $\mathbb{E}[\tau]$.

(c) Find $\mathbb{P}(W_\tau = 1)$.

### Exercise 5.2: Gambler's Ruin

A gambler starts with $\$k$ and bets $\$1$ on each fair coin flip. They stop when they reach $\$0$ or $\$N$.

(a) Model this as a martingale problem and find the probability of reaching $\$N$.

(b) Find the expected number of bets.

(c) Generalize to an unfair coin with $\mathbb{P}(\text{heads}) = p \neq 1/2$.

### Exercise 5.3: Wald's Identities

Let $S_n = \sum_{k=1}^n X_k$ where $X_k$ are i.i.d. with $\mathbb{E}[X_1] = 0$ and $\text{Var}(X_1) = \sigma^2$. Let $\tau$ be a stopping time with $\mathbb{E}[\tau] < \infty$.

(a) Prove Wald's first identity: $\mathbb{E}[S_\tau] = 0$.

(b) Prove Wald's second identity: $\mathbb{E}[S_\tau^2] = \sigma^2 \mathbb{E}[\tau]$.

(c) Apply these to the symmetric random walk stopped at $\pm a$.

### Exercise 5.4: Laplace Transform of Hitting Times

Let $\tau_a = \inf\{t : W_t = a\}$ for $a > 0$.

(a) Apply optional sampling to $\exp(\theta W_t - \frac{\theta^2 t}{2})$ with $\theta = \sqrt{2\lambda}$ to derive $\mathbb{E}[e^{-\lambda \tau_a}] = e^{-a\sqrt{2\lambda}}$.

(b) Invert the Laplace transform to find the density of $\tau_a$.

(c) Show that $\mathbb{E}[\tau_a] = \infty$ despite $\mathbb{P}(\tau_a < \infty) = 1$.

---

## Part VI: Doob's Inequalities

### Exercise 6.1: Maximal Inequality Applications

(a) Use Doob's $L^2$ inequality to show $\mathbb{E}[\sup_{t \le T} W_t^2] \le 4T$.

(b) Find an upper bound for $\mathbb{P}(\sup_{t \le 1} |W_t| \ge 3)$.

(c) Compare your bound in (b) with the exact value from the reflection principle.

### Exercise 6.2: $L^p$ Bounds

Let $M_t$ be a martingale with $\mathbb{E}[|M_T|^4] = C$.

(a) Use Doob's inequality to bound $\mathbb{E}[\sup_{t \le T} |M_t|^4]$.

(b) What happens to the constant as $p \to 1$?

(c) State and prove Doob's $L^1$ weak inequality.

### Exercise 6.3: Convergence Application

Let $M_n$ be a discrete martingale with $\sup_n \mathbb{E}[M_n^2] < \infty$.

(a) Use Doob's inequality to show $\sup_n |M_n| < \infty$ a.s.

(b) Deduce that $M_n$ converges a.s.

(c) Give an example where $\sup_n \mathbb{E}[|M_n|] < \infty$ but $M_n$ does not converge in $L^1$.

---

## Part VII: Martingale Convergence

### Exercise 7.1: Upcrossings

Let $M_n$ be a submartingale and let $U_N^{[a,b]}$ denote the number of upcrossings of $[a,b]$ by $M_0, \ldots, M_N$.

(a) State Doob's upcrossing inequality.

(b) Use the upcrossing inequality to prove: if $\sup_n \mathbb{E}[M_n^+] < \infty$, then $M_n$ converges a.s.

(c) Explain why the condition involves $M_n^+$ rather than $|M_n|$.

### Exercise 7.2: Uniform Integrability

(a) Prove that a family $\{X_\alpha\}$ is uniformly integrable if and only if it is $L^1$-bounded and satisfies: for all $\epsilon > 0$, there exists $\delta > 0$ such that $\mathbb{P}(A) < \delta$ implies $\sup_\alpha \mathbb{E}[|X_\alpha| \mathbf{1}_A] < \epsilon$.

(b) Show that $\{W_t : t \le T\}$ is uniformly integrable for any $T < \infty$.

(c) Show that $\{e^{W_t - t/2} : t \ge 0\}$ is **not** uniformly integrable.

### Exercise 7.3: Backward Martingales

Let $X_1, X_2, \ldots$ be i.i.d. with $\mathbb{E}[X_1] = \mu$ and let $\bar{X}_n = \frac{1}{n}\sum_{k=1}^n X_k$.

(a) Define $\mathcal{F}_{-n} = \sigma(\bar{X}_n, \bar{X}_{n+1}, \ldots)$. Show this is a decreasing sequence of $\sigma$-algebras.

(b) Prove that $(\bar{X}_n, \mathcal{F}_{-n})$ is a backward martingale.

(c) Use backward martingale convergence to prove the strong law of large numbers.

---

## Part VIII: Doob–Meyer Decomposition

### Exercise 8.1: Discrete Decomposition

Let $X_n = \sum_{k=1}^n Y_k$ where $Y_k \ge 0$ and $\mathbb{E}[Y_k \mid \mathcal{F}_{k-1}] = c$ for some constant $c > 0$.

(a) Find the Doob decomposition $X_n = M_n + A_n$.

(b) Verify that $A_n$ is predictable and increasing.

(c) What is $X_n$ if not a martingale?

### Exercise 8.2: Compensator of Squared Brownian Motion

(a) Use Itô's formula to write $W_t^2 = M_t + A_t$ where $M_t$ is a martingale and $A_t$ is predictable increasing.

(b) Identify $A_t$ explicitly.

(c) Explain the connection to quadratic variation.

### Exercise 8.3: Compensator of $|W_t|$

The process $|W_t|$ is a submartingale.

(a) Explain why its Doob–Meyer compensator involves local time.

(b) State Tanaka's formula: $|W_t| = \int_0^t \text{sgn}(W_s) \, dW_s + L_t^0$.

(c) Identify the martingale and increasing parts.

---

## Part IX: Synthesis and Challenge Problems

### Exercise 9.1: First Passage with Drift

Let $X_t = W_t + \mu t$ (Brownian motion with drift $\mu > 0$). Let $\tau_a = \inf\{t : X_t = a\}$ for $a > 0$.

(a) Find a martingale involving $X_t$ by exponential tilting.

(b) Use optional sampling to find $\mathbb{E}[e^{-\lambda \tau_a}]$.

(c) Find $\mathbb{P}(\tau_a < \infty)$ for $\mu < 0$.

### Exercise 9.2: Two-Sided Exit

Let $\tau = \inf\{t : W_t \notin (-a, b)\}$ where $a, b > 0$.

(a) Find $\mathbb{P}(W_\tau = b)$.

(b) Find $\mathbb{E}[\tau]$.

(c) Find $\mathbb{E}[e^{-\lambda \tau}]$.

### Exercise 9.3: Maximum of Brownian Motion

Let $M_t = \sup_{s \le t} W_s$.

(a) Prove that $M_t - W_t \ge 0$ and is increasing in $t$.

(b) Show that $M_t$ and $M_t - W_t$ have the same distribution.

(c) Use this to find $\mathbb{P}(M_t \ge a, W_t \le b)$ for $a > b$.

### Exercise 9.4: Martingale Characterization of Brownian Motion

Prove **Lévy's characterization**: If $M_t$ is a continuous martingale with $M_0 = 0$ and $[M]_t = t$, then $M_t$ is a standard Brownian motion.

*Hint*: Show that $\exp(\theta M_t - \frac{\theta^2 t}{2})$ is a martingale for all $\theta$ and use uniqueness of moment generating functions.

### Exercise 9.5: The Martingale Problem

(a) State the martingale problem for Brownian motion: for which functions $f$ is $f(W_t) - \frac{1}{2}\int_0^t f''(W_s) \, ds$ a local martingale?

(b) Verify this for $f(x) = x^2$ and $f(x) = e^{\theta x}$.

(c) Explain the connection to the heat equation $\partial_t u = \frac{1}{2} \partial_{xx} u$.

---

## Solutions Hints

**Exercise 1.1(a)**: Countable unions of measurable sets need not be measurable.

**Exercise 2.1(b)**: Compute $\mathbb{E}[e^{W_t} \mid \mathcal{F}_s]$ using the MGF of $W_t - W_s \sim N(0, t-s)$.

**Exercise 5.2(a)**: Use the martingale $S_n = $ current wealth, stopping at $0$ or $N$.

**Exercise 9.1(a)**: The martingale is $\exp(\theta X_t - (\frac{\theta^2}{2} + \mu\theta)t)$.
