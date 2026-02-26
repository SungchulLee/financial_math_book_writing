# An Introduction to Lévy Processes and PIDEs

*By Nicola Cantarutti — with applications to Merton and Variance Gamma processes*

!!! abstract "Abstract"

    In this brief introduction I have tried to summarize all the most important concepts regarding Lévy's processes.
    The goal is to introduce the formalism and the tools necessary to derive the partial integro-differential equation (PIDE)
    for pricing financial derivatives, when the underlying stock price is modeled by the exponential of a Lévy process.
    These arguments are not simple and the reader is required to have a good knowledge of the basics of stochastic calculus and financial mathematics.
    However, a complete list of references and tutorials for beginners will be presented.

    At the end of the tutorial I will make a thorough presentation of the cases of the Merton and Variance Gamma process. I will also present the Black-Scholes PDE, which is a
    special case when the Lévy process under consideration is the Brownian motion.

---

Over the past thirty years, a lot of research has been done on processes with jumps and their applications to financial derivatives.
Let us start with the list of references.

A good tutorial for beginners is [Papapantoleon]. I really suggest to read this tutorial because it is very clear, compact, and gives a good overview of the theory and applications
of Lévy processes. The article can be found on the Arxiv web page: [https://arxiv.org/abs/0804.0482](https://arxiv.org/abs/0804.0482).

If you are looking for some more challenging references I suggest
[Sato, 1999], which is a reference book for the theory of Lévy processes, and
[Applebaum, 2009] that gives more emphasis on stochastic calculus and stochastic differential equations (SDEs). These two books are very rigorous mathematical books.

Comprehensive guides on applications of Lévy processes in finance are the books of
[Cont and Tankov, 2003] and [Schoutens, 2003]. These books are also accessible to beginners.

Among the most popular Lévy processes applied to finance, it is worth to mention:

- the Merton jump-diffusion model [Merton, 1976]
- the Kou jump-diffusion model [Kou, 2002]
- the $\alpha$-stable [Mandelbrot, 1963], [Cont et al., 1997], [Kabasinskas et al., 2009]
- the Variance-Gamma (VG) [Madan and Seneta, 1990], [Madan et al., 1998]
- the Normal-Inverse-Gaussian (NIG) [Barndorff-Nielsen, 1997]
- hyperbolic Lévy processes [Eberlein and Keller, 1995]
- Carr-Geman-Madan-Yor (CGMY) model [Carr et al., 2002]

We begin with the most important definitions concerning the theory of Lévy processes and the stochastic calculus applied to jump processes.

These definitions are very quite abstract. I encourage the reader to have a look at [Papapantoleon] for more practical examples, or to read
the first three chapters of [Cont and Tankov, 2003]. Sometimes it is enough to have a look at wikipedia, in order to clarify the ideas.
Here, I prefer to give a very short presentation of the main concepts, and dedicate more space to the second part of the tutorial.

In the second part we focus on the derivation of the PIDE for option pricing and on the exponential Lévy models used in this tutorial:
the *Merton* and *Variance Gamma* models.
In this part of the tutorial, I will present all the calculation step by step.

## 1. Basic Definitions

Let $\{X_t\}_{t \ge 0}$ be a stochastic process defined on a probability space $(\Omega,\mathcal{F},\{\mathcal{F}_t\}_{t \ge 0}, \mathbb{P})$,
where $\mathcal{F}_t$ is the filtration to which the process $\{X_t\}_{t \ge 0}$ is adapted and represents the accumulated "information" up to time $t$.

!!! info "Definition 1.1 — Lévy Process"

    We say that $\{X_t\}_{t \ge 0}$ is a **Lévy Process** if:

    - **(L1)** $X_{t=0} = 0$.
    - **(L2)** $\{X_t\}_{t \ge 0}$ has independent increments i.e. $X_t - X_s$ is independent of $\mathcal{F}_s$ for any $0 \leq s < t$.
    - **(L3)** $\{X_t\}_{t \ge 0}$ has stationary increments i.e. for any $s,t \geq 0$, the distribution of $X_{t+s} - X_t$ does not depend on $t$.
    - **(L4)** $\{X_t\}_{t \ge 0}$ is stochastically continuous i.e. for every $\epsilon > 0$ and $t \ge 0$

    $$\lim_{h\to 0} \mathbb{P}(|X_{t+h}-X_t| > \epsilon)=0.$$

It can be proven that Lévy processes have "càdlàg"
paths, i.e. paths which are right-continuous and have left limits.

!!! info "Definition 1.2 — Characteristic Function"

    Let $X: \Omega \to \mathbb{R}$ be a random variable.
    The **Characteristic function** $\phi_X:\mathbb{R} \to \mathbb{C}$ of $X$, is defined by

    $$\begin{aligned}
    \phi_{X}(u) &= \mathbb{E} [e^{iuX}] \\
                &= \int_{\Omega} e^{iuX} \mathbb{P}(d\omega) \\
                &= \int_{\mathbb{R}} e^{iux} f_X \, dx.
    \end{aligned}$$

    for each $u \in \mathbb{R}$. Where $\omega \in \Omega$, and we indicated with $f_X = \frac{d\mathbb{P}}{dx}$ the **probability density function** (pdf) of $X$.

For each $n \in \mathbb{N}$, if $\mathbb{E}\bigl[ |X^{n}| \bigr] < \infty$, then

$$
\mathbb{E}\bigl[ X^{n} \bigr] = i^{-n}\frac{\partial^n}{\partial u^{n}} \phi_X(u) \biggr|_{u=0} .
$$

With this property it is straightforward to compute the moments of all orders, as long as we know the analytic form
of the characteristic function.

### 1.1 Lévy-Khintchine Representation

We now present a beautiful formula, first established by Paul Lévy and A.Ya. Khintchine in the 1930s
which gives a characterization of every infinitely divisible random variable.

!!! info "Definition 1.3 — Lévy Measure"

    Let $\nu(dx)$ be a measure on $\mathbb{R}$. We say it is a **Lévy measure** if it satisfies

    $$\nu (\{ 0 \} ) = 0,$$

    $$\int_{\mathbb{R}} \min\{1, x^2\} \, \nu(dx) < \infty.$$

The characteristic function of a Lévy process at a fixed time $t\geq 0$ has the following **Lévy Khintchine representation**:

!!! tip "Theorem 1.1 — Lévy-Khintchine Representation"

    Let $X_t$ be the random value of a Lévy process at time $t\geq0$. Then there exist $b\in \mathbb{R}$, $\sigma>0$
    and a Lévy measure $\nu$ on $\mathbb{R}$, such that $\forall u \in \mathbb{R}$:

    $$\begin{aligned}
    \phi_{X_t}(u) &= \mathbb{E} [e^{iuX_t}] \\
         &= e^{t \eta(u)} \\
         &= \exp \left[ t \left( ibu - \frac{1}{2} \sigma^2 u^2 + \int_{\mathbb{R}}
             ( e^{iux} -1 -iux \mathbb{1}_{(|x|<1)}(x) ) \, \nu(dx) \right) \right].
    \end{aligned}$$

A proof can be found in [Applebaum, 2009] (Theorem 1.2.14).

- We call the map $\eta : \mathbb{R} \to \mathbb{C}$, the **Lévy symbol**.
- The triplet $(b, \sigma, \nu)$ is called **Lévy triplet**, and completely characterizes the Lévy process.

### 1.2 Random Measures

A convenient tool for analyzing the jumps of a Lévy process is the random
measure of the jumps of the process.
The jump process $\{\Delta X_t\}_{t \ge 0}$ associated to the Lévy process $\{X_t\}_{t \ge 0}$ is
defined, for each $t \geq 0$, by

$$
\Delta X_t = X_t - X_{t^-}
$$

where $X_{t^-} = \lim_{s\uparrow t} X_s$.

!!! info "Definition 1.4 — Random Measure"

    Consider an open set $A \subseteq \mathbb{R} \backslash \{ 0 \}$.
    We define the **random measure** of the jumps of the process $\{X_t\}_{t \ge 0}$ by

    $$\begin{aligned}
    N^X(t,A)(\omega) &= \# \{ s \in [0,t] \, : \; \Delta X_s(\omega) \in A  \} \\
               &= \sum_{0 \leq s \leq t} \mathbb{1}_A(\Delta X_s(\omega)) .
    \end{aligned}$$

For each $\omega \in \Omega$ and for each $0 \leq t < \infty$, the map

$$A \to N^X(t,A)(\omega)$$

is a counting measure i.e. it counts the number of jumps of the process $\{X_t\}_{t\geq0}$ with size in $A$ up to time $t$.
We say that $A$ is *bounded below* if $0 \not \in \bar A$ i.e. zero does not belong to the closure of $A$.

- For each $A$ bounded below, the process $\bigl \{ N^X(t,A)(\omega) \bigr \}_{t\geq 0}$ is a **Poisson process** with intensity

$$\nu(A) = \mathbb{E}[N^X(1,A) ]$$

- If $A_1, ..., A_m$ are disjoint subsets of $\mathbb{R} \backslash \{ 0 \}$ and bounded below and $t_1, ..., t_m$ are distinct non-negative times, then the random variables $N(t_1,A_1), ..., N(t_m,A_m)$ are independent.

A random measure satisfying the properties above is called **Poisson random measure**.
If $A$ is not bounded below, it is possible to have $\nu(A) = \infty$.

We can also define the **Compensated Poisson random measure**. For each $t \geq 0$ and $A$ bounded below, let us define:

$$
\tilde{N}(t,A) = N(t,A) - t\nu(A).
$$

This is a martingale-valued measure, i.e. for each $A$ the process $\bigl \{ \tilde{N}(t,A) \bigr \}_{t\geq 0}$ is a martingale.

Now we can define the integration with respect to a random measure:

!!! info "Definition 1.5 — Poisson Integral"

    Let $N$ be the Poisson random measure associated to a Lévy process $\{X_t\}_{t \geq 0}$, and let $f:\mathbb{R} \to \mathbb{R}$ be a measurable
    function. For any $A$ bounded below, we define the **Poisson integral** of $f$ as

    $$\int_A f(x) N(t,dx) = \sum_{x\in A} f(x) N(t,\{x\}).$$

Since $N(t,\{x\}) \neq 0 \Leftrightarrow \Delta X_s=x$ for at least one $s\in [0,t]$, we have

$$
\int_A f(x) N(t,dx) = \sum_{0 \leq s \leq t} f(\Delta X_s) \mathbb{1}_A(\Delta X_s).
$$

We can also define in the same way the **compensated Poisson integral**

$$
\int_A f(x) \tilde{N}(t,dx) := \int_A f(x) N(t,dx) - t \int_A f(x) \mu(dx),
$$

We can further define:

$$
\int_{|x|<1} f(x) \tilde N(t,dx) := \lim_{\epsilon \to 0} \int_{\epsilon < |x| < 1} f(x) \tilde N(t,dx),
$$

that represents the compensated sum of small jumps.

### 1.3 Lévy-Itô Decomposition

The following is a fundamental theorem which decomposes a general Lévy process in a superposition
of independent processes: a drift term, a Brownian motion, a Poisson process with "big jumps" and a compensated Poisson process with "small jumps".

!!! tip "Theorem 1.2 — Lévy-Itô Decomposition"

    Given a Lévy process $\{X_t\}_{t \ge 0}$, there exist $b\in \mathbb{R}$, a Brownian motion $W$ with variance $\sigma^2$, and an
    independent Poisson random measure $N$ on $[0,\infty) \times \mathbb{R}$ such that

    $$X_t = bt + \sigma W_t + \int_{|x|<1} x \tilde{N}(t,dx) + \int_{|x|\geq1} x N(t,dx).$$

    This is called **Lévy-Itô decomposition**.

For a proof the reader can look at Theorem 2.4.16 in [Applebaum, 2009].
A lot of information on the features of a Lévy process can be derived from the integrability conditions of its Lévy measure.
Let $\{X_t\}_{t\geq0}$ be a Lévy process with Lévy measure $\nu$. Then

1. For all $t\geq0$, $X_t$ has finite p-moment i.e.
$\mathbb{E}[|X_t|^p]<\infty$ for $p\geq0$ if and only if $\int_{|x| \geq 1} |x|^p \, \nu(dx) <\infty$.
2. For all $t\geq0$, $X_t$ has finite exponential p-moment i.e. $\mathbb{E}[\exp(pX_t)]<\infty$ for $p\in \mathbb{R}$ if and only if
$\int_{|x| \geq 1} e^{xp} \, \nu(dx) <\infty$.

The majority of Lévy processes used in finance have finite moments.
For practical reasons, it makes sense to assume finite mean and variance of the price process.
In this tutorial we will model the 1-dimensional dynamics of the prices with the exponential of a Lévy process,
i.e. $S_t = S_0 e^{X_t}$. Let us introduce the important assumption:

!!! warning "Assumption"

    We consider only Lévy processes with finite exponential second moment.
    Therefore it follows that:

    $$\mathbb{E}\bigl[ S_t^2 \bigr] < \infty \quad \Leftrightarrow  \quad \int_{|x| \geq 1} e^{2x} \, \nu(dx) <\infty$$

The existence of the exponential 2-moment implies that $\{X_t\}_{t \geq 0}$ has finite p-moment for all $p \in \mathbb{N}$.

If we assume that $\{X_t\}_{t \geq 0}$ has finite first moment, we can simplify the Lévy-Itô decomposition,
by adding and subtracting the finite term $\int_{|x| \geq 1} x t\, \nu(dx)$.
The decomposition has now the form:

$$
X_t = \biggl(  b+\int_{|x| \geq 1} x \, \nu(dx) \biggr)t + \sigma W_t + \int_{\mathbb{R}} x \tilde{N}(t,dx).
$$

Let us recall the definition of the *total variation* $TV(f)$ of a function $f : [a,b] \to \mathbb{R}$

$$
TV(f) = \sup_P \sum_{i=1}^n |f(t_i) - f(t_{i-1})|,
$$

where the supremum is taken over all $P$, the finite partitions $a=t_0 < t_1 < ... < t_n = b$ of the interval $[a,b]$.
A Lévy process is said to be of finite variation if its paths are of finite variation with probability 1.

The variation of any Lévy process is related with the behavior of the Lévy measure in the region $|x|<1$.
A Lévy process $\{X_t\}_{t \geq 0}$ with triplet $(b,\sigma,\nu)$ is of **finite variation** if and only if

$$
\sigma = 0 \quad \mbox{ and } \quad \int_{|x| < 1} |x| \, \nu(dx) < \infty.
$$

If we assume that $\{X_t\}_{t \geq 0}$ has finite variation, the Lévy-Itô decomposition
becomes

$$
X_t = \biggl(  b-\int_{|x| < 1} x \, \nu(dx) \biggr)t + \int_{\mathbb{R}} x N(t,dx).
$$

### 1.4 The Itô Formula and Infinitesimal Generator

Let us express the Lévy-Itô decomposition in the differential form:

$$
dX_t = b\,dt + \sigma \, dW_t + \int_{|z|<1} z \tilde{N}(dt,dz) + \int_{|z|\geq1} z N(dt,dz).
$$

Now we can introduce the most important formula in stochastic calculus: the **Itô formula**.

!!! tip "Theorem 1.3 — Itô Formula for Lévy Processes"

    If $X_t$ is the Lévy process with dynamics as above, for each $f \in C^2(\mathbb{R}^n)$ we have

    $$\begin{aligned}
    df(X_t) &=  \frac{\partial f}{\partial x}(X_{t^-}) b \, dt  +  \frac{\partial f}{\partial x}(X_{t^-}) \sigma \, dW_t
              + \frac{1}{2} \frac{\partial^2 f}{\partial x^2}(X_{t^-}) \sigma^2 \, dt \\
              &+ \int_{|z|\geq 1} \bigl[ f\bigl( X_{t^-} + z \bigr) - f( X_{t^-} ) \bigr] N(dt,dz) \\
              &+ \int_{|z|< 1} \bigl[ f\bigl( X_{t^-} + z \bigr) - f(X_{t^-}) \bigr] \tilde N(dt,dz) \\
              &+ \int_{|z|< 1} \bigl[ f\bigl( X_{t^-} + z \bigr) - f(X_{t^-}) - \frac{\partial f}{\partial x}(X_{t^-}) z \bigr] \nu(dz)\,dt.
    \end{aligned}$$

The terms in the first line are the same as the well known diffusion case. The other terms come from the discontinuous part of the process.

A Lévy process is a **Markov process**.
To be precise, a Lévy process is a **time homogeneous**, **translation invariant** Markov process. For more information on these topics, have a look at [Applebaum, 2009].

We can define the **infinitesimal generator** $\mathcal{L}^X : f \to \mathcal{L}^X f$ of the Lévy process $X$ with triplet $(b,\sigma,\nu)$:

$$\begin{aligned}
(\mathcal{L}^X f)(x) =& \; \lim_{t\to0} \frac{\mathbb{E} \bigl[ f(x + X_t) \bigr] - f(x) }{t}  \\
         =& \;  b \frac{\partial f}{\partial x}(x) +
\frac{1}{2} \sigma^2 \frac{\partial^2 f}{\partial x^2}(x)\\
       & + \int_{\mathbb{R}} \left( f(x+z) - f(x) - z \frac{\partial f}{\partial x}(x)
       \mathbb{1}_{\{ |z|<1 \}}(z) \right) \nu(dz).
\end{aligned}$$

This works for functions twice continuously differentiable, and with nice behavior at infinity (usually they are required to have compact support, or to vanish at infinity or even
polynomial growth).

If the Lévy process $\{X_t\}_{t \geq 0}$ has finite first moment i.e. with Lévy-Itô decomposition of the simplified form, the generator has form:

$$\begin{aligned}
(\mathcal{L}^X f)(x) =& \; b \frac{\partial f}{\partial x}(x) +
\frac{1}{2} \sigma^2 \frac{\partial^2 f}{\partial x^2}(x)\\
       & + \int_{\mathbb{R}} \left( f(x+z) - f(x) - z \frac{\partial f}{\partial x}(x) \right) \nu(dz).
\end{aligned}$$

## 2. Exponential Lévy Models

If we indicate with $S_t$ the stock price,
the name **exponential Lévy model** comes from the expression:

$$
S_t = S_0 e^{X_t} ,
$$

where $X_t$ is a one dimensional Lévy process with triplet $(b,\sigma,\nu)$.

### 2.1 Exponential Lévy SDE

In order to obtain an SDE for $S_t$, we apply the Itô formula and consider
the dynamics for $X_t$:

$$\begin{aligned}
d S_t \; &= S_0 e^{X_{t^-}} b \, dt \; + \; S_0 e^{X_{t^-}} \sigma \, dW_t \; + \; \frac{1}{2}S_0 e^{X_{t^-}}\sigma^2 \, dt \\
          &+ \int_{|x|\geq 1} (S_0 e^{X_{t^-}+x} - S_0 e^{X_{t^-}}) N(dt,dx) \\
          &+ \int_{|x|< 1} (S_0 e^{X_{t^-}+x} - S_0 e^{X_{t^-}}) \tilde N(dt,dx) \\
          &+ \int_{|x|< 1} (S_0 e^{X_{t^-}+x} - S_0 e^{X_{t^-}} - x S_0 e^{X_{t^-}}) \nu(dx) \, dt.
\end{aligned}$$

After some substitutions we get:

$$\begin{aligned}
\frac{d S_t}{S_{t^-}}  \; &= \left(b + \frac{1}{2}\sigma^2 \right) dt + \sigma \, dW_t \\
                          &+ \int_{|x|< 1} ( e^{x} - x - 1) \nu(dx) \, dt \\
                          &+ \int_{|x|\geq 1} (e^{x} - 1) N(dt,dx) + \int_{|x|< 1} (e^{x} - 1) \tilde N(dt,dx).
\end{aligned}$$

Thanks to the assumption on finite exponential second moments we can simplify this equation.
First we look at the integrability conditions:

- $\int_{|x|\geq 1}  e^{x} \, \nu(dx) < \infty$ by the assumption.
- $\int_{|x|\geq 1} 1\; \nu(dx) < \infty$ by definition of $\nu$.

We can add and subtract $\pm \int_{|x|\geq 1} ( e^{x} - 1) \, \nu(dx) \, dt$ and obtain the final form

$$\begin{aligned}
\frac{d S_t}{S_{t^-}}  \; &= \left(b + \frac{1}{2}\sigma^2 + \int_{\mathbb{R}} ( e^{x} - 1 -x\mathbb{1}_{|x|<1}) \, \nu(dx) \right) dt  \\
                          &+  \sigma \, dW_t \; + \int_{\mathbb{R}} (e^{x} - 1) \tilde N(dt,dx).
\end{aligned}$$

If we set

$$
\mu := b + \frac{1}{2}\sigma^2 + \int_{\mathbb{R}} ( e^{x} - 1 -x\mathbb{1}_{|x|<1}) \, \nu(dx)
$$

The SDE for $S_t$ becomes:

$$
d S_t = \; \mu S_{t^-} \, dt +  \sigma S_{t^-} \, dW_t \; + \int_{\mathbb{R}} S_{t^-} (e^{x} - 1) \tilde N(dt,dx).
$$

The same equation can be derived quickly by considering the Lévy-Itô form for $X_t$:

$$\begin{aligned}
d S_t \; =& \; S_0 e^{X_{t^-}} \biggl( b + \int_{|x|\geq 1}x \, \nu(dx) \biggr) dt \; + \; S_0 e^{X_{t^-}} \sigma \, dW_t \; + \; \frac{1}{2}S_0 e^{X_{t^-}}\sigma^2 \, dt \\
          &+ \int_{\mathbb{R}} (S_0 e^{X_{t^-}+x} - S_0 e^{X_{t^-}}) \tilde N(dt,dx) + \int_{\mathbb{R}} (S_0 e^{X_{t^-}+x} - S_0 e^{X_{t^-}} - x S_0 e^{X_{t^-}}) \nu(dx) \, dt \\
          =& \; S_{t^-} \biggl[ \mu \, dt +  \sigma \, dW_t \; + \int_{\mathbb{R}} (e^{x} - 1) \tilde N(dt,dx) \biggr].
\end{aligned}$$

### 2.2 The Merton Model

The first jump-diffusion model for the log-prices is the *Merton model*, presented in
[Merton, 1976]. In the same paper the author also obtains a closed form solution for the price of a European vanilla option.
The Merton model describes the log-price evolution with a Lévy process with a nonzero diffusion
component and a finite activity jump process with normal distributed jumps.

$$
X_t = \bar b t + \sigma W_t + \sum_{i=1}^{N_t} Y_i,
$$

where $N_t$ is a Poisson random variable counting the jumps of $X_t$ in $[0,t]$, and $Y_i \sim \mathcal{N}(\alpha, \xi^2)$ is the size of the jumps.
Using the Poisson integral notation (Definition 1.5), the process becomes

$$
X_t = \bar b t + \sigma W_t + \int_{\mathbb{R}} x N(t,dx)
$$

The previous equation corresponds to the Lévy-Itô decomposition for finite variation with an additional Brownian motion term,
and with

$$\bar b = b - \int_{|x|<1} x \, \nu(dx).$$

The Lévy measure of a finite activity Lévy process, can be factorized in the activity $\lambda$ of the Poisson process and
the pdf of the jump size:

$$\begin{aligned}
\nu(dx) &= \lambda f_Y(dx), \\
     &= \frac{\lambda}{\xi \sqrt{2\pi}} e^{- \frac{(x-\alpha)^2}{2\xi^2}} dx.
\end{aligned}$$

such that $\int_{\mathbb{R}} \nu(dx) = \lambda$.

Since $\int_{|x|<1} x \, \nu(dx)$ is finite, the jump process has **finite variation**. However,
the Merton process has infinite variation because $\sigma >0$.

The Lévy exponent has the following form:

$$
\eta(u) = i\bar b u - \frac{1}{2} \sigma^2 u^2 + \lambda \biggl( e^{i\alpha u -\frac{\xi^2 u^2}{2} }-1 \biggr).
$$

Using the formula for the moments we obtain:

$$\begin{aligned}
\mathbb{E}[X_t] &= t(\bar b+\lambda \alpha). \\
\text{Var}[X_t] &= t(\sigma^2 + \lambda \xi^2 + \lambda \alpha^2). \\
\text{Skew}[X_t] &= \frac{t\lambda (3\xi^2 \alpha + \alpha^3)}{\bigl(\text{Var}[X_t]\bigr)^{3/2}}. \\
\text{Kurt}[X_t] &= \frac{t \lambda (3\xi^3 +6\alpha^2\xi^2 +\alpha^4)}{\bigl(\text{Var}[X_t]\bigr)^2}.
\end{aligned}$$

### 2.3 The Variance Gamma Process

The *variance gamma* process is a pure jump Lévy process with infinite activity.
The first presentation with applications in finance is due to [Madan and Seneta, 1990].
The model presented in their paper is however a symmetric VG model,
where there is only an additional parameter which controls the kurtosis, while the skewness is still not considered.
The non-symmetric VG process is described in [Madan et al., 1998] where a closed form solution for European vanilla options is also presented.

If we consider a Brownian motion with drift $X_t = \theta t + \bar\sigma W_t$ and substitute the time variable with the gamma random variable
$T_t \sim \Gamma(t,\kappa t)$,
we obtain the **variance gamma** process:

$$
X_{T_t} = \theta T_t + \bar\sigma W_{T_t} .
$$

It depends on three parameters:

- $\bar\sigma$, the volatility of the Brownian motion
- $\kappa$, the variance of the Gamma process
- $\theta$, the drift of the Brownian motion

The VG is a process with **finite variation**.
The pdf of $X_t$ can be computed conditioning on the realization of $T_t$:

$$\begin{aligned}
f_{X_t}(x) &= \int_y f_{X_t,T_t}(x,y) \, dy = \int_y f_{X_t|T_t}(x|y) f_{T_t}(y) \, dy \\
         &= \int_0^{\infty} \frac{1}{\bar\sigma \sqrt{2\pi y}} e^{-\frac{(x -\theta y)^2}{2\bar\sigma^2 y}}
         \frac{y^{\frac{t}{\kappa} -1}}{\kappa^{\frac{t}{\kappa}} \Gamma(\frac{t}{\kappa})}
          e^{-\frac{y}{\kappa}} \, dy \\
         &= \frac{2 \exp\!\left(\frac{\theta x}{\bar\sigma^2}\right)}{\kappa^{\frac{t}{\kappa}} \sqrt{2\pi}\,\bar\sigma \, \Gamma\!\left(\frac{t}{\kappa}\right) }
            \biggl( \frac{x^2}{2\frac{\bar\sigma^2}{\kappa} + \theta^2} \biggr)^{\!\frac{t}{2\kappa}-\frac{1}{4}}
            K_{\frac{t}{\kappa}-\frac{1}{2}}
            \biggl( \frac{1}{\bar\sigma^2} \sqrt{x^2 \bigl(\tfrac{2\bar\sigma^2}{\kappa}+\theta^2 \bigr)} \biggr),
\end{aligned}$$

where the function $K$ is a modified Bessel function of the second kind (see [Madan et al., 1998] for explicit computations).
The characteristic function can be obtained from the composition of the Gamma moment generating function and the Normal characteristic functions:

$$\begin{aligned}
\phi_{X_t}(u) &= \biggl( 1- \kappa \bigl( i u\theta -\frac{1}{2}\bar\sigma^2 u^2 \bigr) \biggr)^{-\frac{t}{\kappa}} \\
           &= \biggl( 1-i\theta \kappa u + \frac{1}{2} \bar\sigma^2 \kappa u^2 \biggr)^{-\frac{t}{\kappa}}.
\end{aligned}$$

I will not prove the previous formula, but the interested reader can consult [Applebaum, 2009] (Proposition 1.3.17 and Example 1.3.31) or [Cont and Tankov, 2003] (Theorem 4.2).
The VG Lévy measure is

$$
\nu^{X_t}(dx) = \frac{e^{\frac{\theta x}{\bar\sigma^2}}}{\kappa|x|} \exp
\left( - \frac{\sqrt{\frac{2}{\kappa} + \frac{\theta^2}{\bar\sigma^4}}}{\bar\sigma} |x|\right) dx,
$$

and the Lévy exponent is

$$
\eta(u) = -\frac{1}{\kappa} \log\!\left(1-i\theta \kappa u + \frac{1}{2} \bar\sigma^2 \kappa u^2\right).
$$

Using the formula for the moments we obtain:

$$\begin{aligned}
\mathbb{E}[X_t] &= t\theta. \\
\text{Var}[X_t] &= t(\bar\sigma^2 + \theta^2 \kappa). \\
\text{Skew}[X_t] &= \frac{t (2\theta^3\kappa^2 + 3 \bar\sigma^2 \theta \kappa)}{\bigl(\text{Var}[X_t]\bigr)^{3/2}}. \\
\text{Kurt}[X_t] &= \frac{t (3\bar\sigma^4 \kappa + 12\bar\sigma^2 \theta^2 \kappa^2 +6\theta^4\kappa^3)}{\bigl(\text{Var}[X_t]\bigr)^2}.
\end{aligned}$$

The Lévy-Itô decomposition for any pure jump finite variation process,
can be written as

$$
X_t = \bar b t + \int_{\mathbb{R}} x N(t,dx)
$$

with $\bar b = b - \int_{|x|<1} x \, \nu(dx)$.

Let us consider the VG process. We can take its expectation

$$\mathbb{E}[X_{T_t}] = \theta \mathbb{E}[T_t] + \bar\sigma \mathbb{E}[W_{T_t}] = \theta t,$$

which must correspond to the expectation of the Lévy-Itô form. We obtain

$$\begin{aligned}
\mathbb{E}[X_t] &= \bar b t + \mathbb{E} \biggl[ \int_{\mathbb{R}} x N(t,dx)\biggr] \\
      &= t \biggl( \bar b + \int_{\mathbb{R}} x \, \nu(dx) \biggr),
\end{aligned}$$

and therefore $\bar b = \theta - \int_{\mathbb{R}} x \, \nu(dx)$.
Let us compute this integral using the explicit formula for the Lévy measure.
Let us call

$$A = \frac{\theta}{\bar\sigma^2} \hspace{2em} \mbox{and} \hspace{2em}
B=\frac{|\theta|}{\bar\sigma^2}\sqrt{1+\frac{2\bar\sigma^2}{\kappa \theta^2}}$$

with $A<B$, and solve the integral:

$$\begin{aligned}
\int_{\mathbb{R}} \frac{x}{\kappa |x|} e^{Ax-B|x|} &= \int_{0}^{\infty} \frac{1}{\kappa} e^{(A-B)x}
- \int_{-\infty}^0 \frac{1}{\kappa} e^{(A+B)x} \\
&= \frac{1}{\kappa} \frac{2A}{B^2-A^2} \\
&= \theta.
\end{aligned}$$

Interesting. We found that $\bar b = 0$.
The Lévy-Itô decomposition for the VG process is simply

$$
X_t = \int_{\mathbb{R}} x N(t,dx).
$$

All the information is contained in the Lévy measure,
which completely describes the process. Even if the process has been created by Brownian
subordination, it has no diffusion component.
The **Lévy triplet** is

$$
\biggl( \int_{|x|<1} x \, \nu(dx),\; 0,\; \nu \biggr).
$$

## 3. No-Arbitrage Pricing

In an arbitrage-free market, if the price process $\{S_t\}_{t\geq0}$ follows an exponential Lévy process,
we can express the price of any simple financial derivative as a function $V(t,s)$ of the current time
$t \in [0,T]$ and current stock price $s=S_t$.
In this section we show that $V(t,s)$ can be obtained by solving a partial integro-differential equation (PIDE).

Let us recall some useful definitions and theorems. For more information have a look at [Cont and Tankov, 2003].

The discount factor for $0 \leq s \leq t \leq T$ is defined as

$$
D(s,t) = e^{-\int_s^t r_u \, du}.
$$

In the following we assume a constant interest rate $r_u = r$ for all $u \in [0,T]$.
It is common to indicate with $\mathbb{P}$ the physical probability measure and with $\mathbb{Q}$ a risk neutral measure, also called equivalent martingale measure (EMM).

!!! info "Definition 3.1 — Equivalent Martingale Measure"

    Given the asset price process $\{S_t\}_{t\geq0}$ defined on the probability space
    $(\Omega,\mathcal{F},\{\mathcal{F}_{t}\}_{t\geq0},\mathbb{P})$, we say that the probability measure $\mathbb{Q}$ is an **EMM**
    if it verifies the following two properties:

    $$\mathbb{Q} \sim \mathbb{P} : \quad \forall A \in \mathcal{F} \quad \quad \mathbb{Q}(A) = 0 \Leftrightarrow \mathbb{P}(A) = 0,$$

    $$D(0,t) S_t = \mathbb{E}^{\mathbb{Q}} \bigl[ D(0,T) S_T \big| \mathcal{F}_t \bigr] \quad \mbox{for} \quad 0\leq t \leq T.$$

The concept of **arbitrage** is related with the existence of an equivalent martingale measure through the **first fundamental theorem of asset pricing**.

!!! tip "Theorem 3.1 — First Fundamental Theorem of Asset Pricing"

    A market model does not admit arbitrage if and only if there exists a risk-neutral probability measure.

Another important concept is the completeness of the market.

!!! info "Definition 3.2 — Complete Market"

    A market model is said to be **complete** if the payoff of every derivative security can be perfectly hedged.

In a complete market, the unique price of a financial derivative corresponds to the initial capital needed to set up a perfect hedge.
The completeness of a market is connected with the uniqueness of the EMM through the
**second fundamental theorem of asset pricing**.

!!! tip "Theorem 3.2 — Second Fundamental Theorem of Asset Pricing"

    Consider a market model that has a risk-neutral probability measure. The model is complete if and only if the risk-neutral probability measure is unique.

The ideal market assumed by Black-Scholes is complete.
However, the majority of the models used in finance are not.

In this tutorial, we analyze a market model based on exponential Lévy models, that is not complete.

In a complete market there is only one arbitrage-free way to price a financial derivative, and the price is defined as the cost to replicate the derivative's payoff.
In an incomplete market, instead, the notion of perfect replication does not exist.
In such a market, the class of EMM is infinite,
i.e. there are infinite EMMs such that the discounted stock prices are martingales.
This means that for every financial derivative there are infinite prices satisfying the condition of no-arbitrage.

In order to overcome this problem, there are several methods to select the best EMM (see [Cont and Tankov, 2003], chapter 10).
However, the best approach is to derive the model parameters directly from the prices of derivatives
already quoted in the market (usually European call and put options with different strikes and maturities).
The process of choosing the risk neutral parameters for a model that reproduces the prices in the market is called **model calibration**.

### 3.1 Derivation of the Pricing PIDE

Let $\{X_t\}_{t\geq0}$ be a Lévy process with Lévy triplet $(b,\sigma,\nu)$, satisfying the assumption on finite exponential second moments.
The process $\{S_t\}_{t\geq0}$ defined by $S_t = S_0 e^{X_t}$ is a martingale if and only if

$$
b +\frac{1}{2} \sigma^2  + \int_{\mathbb{R}} \bigl( e^z-1 -z\mathbb{1}_{\{ |z|<1 \}} \bigr) \nu(dz) = 0.
$$

In order to prove it, we just need to look at the exponential Lévy SDE. The exponential Lévy process is a martingale if and only if the drift is zero.

Let us consider a stock price process described by the *exponential Lévy model*

$$
S_t = S_0 e^{L_t} = S_0 e^{rt + X_t}
$$

where $\{X_t\}_{t\geq 0}$ is a Lévy process with Lévy triplet $(b,\sigma,\nu)$, and the process $\{L_t\}_{t\geq 0}$
is a Lévy process with triplet $(r+b,\sigma,\nu)$.
Under a risk neutral measure $\mathbb{Q}$, the discounted price is a $\mathbb{Q}$-martingale:

$$
\mathbb{E}^{\mathbb{Q}} \bigl[ e^{-rt} S_t \bigr| S_0 \bigr] =  \mathbb{E}^{\mathbb{Q}} \bigl[ S_0e^{X_t} \bigr| S_0 \bigr] = S_0,
$$

such that $\mathbb{E}^{\mathbb{Q}}[ e^{X_t} | X_0=0] = 1$.

We can repeat the same computation that led to the exponential Lévy SDE for the process $L_t = X_t + rt$ i.e.

$$\begin{aligned}
\frac{d S_t}{S_{t^-}}  \; &= \left(r + b + \frac{1}{2}\sigma^2 + \int_{\mathbb{R}} ( e^{z} - 1 -z\mathbb{1}_{|z|<1}) \, \nu(dz) \right) dt  \\
                          &+  \sigma \, dW_t \; + \int_{\mathbb{R}} (e^{z} - 1) \tilde N(dt,dz).
\end{aligned}$$

and define the new parameter

$$
\mu := r + b + \frac{1}{2}\sigma^2 + \int_{\mathbb{R}} ( e^{z} - 1 -z\mathbb{1}_{|z|<1}) \, \nu(dz)
$$

Using the martingale condition we obtain the fundamental relation

$$
\mu = r.
$$

The risk neutral dynamics is described by the SDE:

$$
d S_t = \; r S_{t^-} \, dt +  \sigma S_{t^-} \, dW_t \; + \int_{\mathbb{R}} S_{t^-} (e^{z} - 1) \tilde N(dt,dz).
$$

**Log variable:**
In order to obtain a simpler PIDE expression, it turns out that it is better to work with a Lévy process instead of its exponential.
So let us invert the exponential Lévy model
and consider $L_t = \log \left( \frac{S_t}{S_0} \right)$.
This is a Lévy process with finite moment of the simplified Lévy-Itô type.
The dynamics is described by the SDE:

$$
dL_t = \biggl( r + b + \int_{|z|\geq 1}z \, \nu(dz) \biggr) dt \; + \sigma \, dW_t + \int_{\mathbb{R}} z \tilde N(dt,dz).
$$

At this point, we can make the substitution for the parameter $b$ using the martingale condition:

$$
dL_t = \biggl( r -\frac{1}{2}\sigma^2 - \int_{\mathbb{R}} \bigl( e^z-1-z \bigr) \nu(dz) \biggr) dt \; + \sigma \, dW_t + \int_{\mathbb{R}} z \tilde N(dt,dz).
$$

Using the formula for the infinitesimal generator with finite first moment, the generator has the form

$$\begin{aligned}
\mathcal{L}^L f(x) =& \biggl( r-\frac{1}{2}\sigma^2 - \int_{\mathbb{R}} \bigl( e^z-1-z \bigr) \nu(dz) \biggr) \frac{\partial f(x)}{\partial x} \\
          &+ \frac{1}{2} \sigma^2 \frac{\partial^2 f(x)}{\partial x^2}
          + \int_{\mathbb{R}} \biggl( f(x+z)- f(x) - z \frac{\partial f(x)}{\partial x} \biggr) \nu(dz).
\end{aligned}$$

**Pricing PIDE:**
Let us recall the pricing formula for a derivative contract:

$$
V(t,x) = \mathbb{E}^{\mathbb{Q}}  \biggl[ D(t,T) V(T,X_T) \bigg| X_t = x \biggr] .
$$

The derivative pricing function $V(t,x)$ with $t \in [0,T]$ and $x \in \mathbb{R}$, can be obtained by solving a pricing PIDE according to the following theorem.

!!! tip "Theorem 3.3 — Pricing PIDE"

    Let us consider an arbitrage free market, where the underlying stock log-price follows the Lévy process described above.
    Let also assume that $V(t,x) \in C^{1,2}([t_0,T] \times \mathbb{R})$ and that the partial derivatives are all bounded.
    Therefore $V(t,x)$ satisfies the PIDE

    $$\begin{aligned}
    & \frac{\partial V(t,x)}{\partial t} + \mathcal{L} V(t,x) -r V(t,x) = 0 \\
    & V(T,x) = \Phi(x),
    \end{aligned}$$

    where $\mathcal{L}$ is the infinitesimal generator defined above.

I want to present the proof of this theorem because it is not presented in popular textbooks.
Since it involves advanced mathematical concepts, the reader can skip it, if not interested.

??? abstract "Proof"

    Let us consider the pricing formula.
    For any stopping time $\tau$ such that $0 \leq t \leq \tau \leq T$, we can use the law of iterated expectations:

    $$\begin{aligned}
    D(0,t) V(t,x) &= \mathbb{E}^{\mathbb{Q}}  \biggl[ \mathbb{E}^{\mathbb{Q}} \bigl[ D(0,T) V(T,X_T) \big| X_{\tau} \bigr] \bigg| X_t=x \biggr] \\
                 &= \mathbb{E}^{\mathbb{Q}} \bigl[ D(0,\tau) V(\tau,X_{\tau}) \big| X_t=x \bigr].
    \end{aligned}$$

    We can write $D(0,\tau) V(\tau,X_{\tau}) = D(0,t) V(t,x) + \int_t^{\tau} d\bigl(D(t,u) V(u,X_u)\bigr) du$.
    Using the Itô formula, we get:

    $$\begin{aligned}
    0 =& \; \mathbb{E}^{\mathbb{Q}} \biggl[ \int_t^{\tau} e^{-r(u-t)} \biggl( \frac{\partial V(u,X_{u^-})}{\partial u} + \mathcal{L} V(u,X_{u^-}) -r V(u,X_{u^-}) \biggr) du \bigg| X_t=x \biggr] & \quad (I)\\
     & + \mathbb{E}^{\mathbb{Q}} \biggl[ \int_t^{\tau} e^{-r(u-t)} \frac{\partial V(u,X_{u^-})}{\partial x} \sigma \; dW_u \; \bigg| X_t=x \biggr] & \quad (II) \\
     & + \mathbb{E}^{\mathbb{Q}} \biggl[ \int_t^{\tau} e^{-r(u-t)} \int_{\mathbb{R}} \bigl( V(u,X_{u^-} + z) - V(u,X_{u^-}) \bigr) \tilde N(du,dz) \; \bigg| X_t=x \biggr] & \quad (III)
    \end{aligned}$$

    where we introduced the explicit expression of the discount factor with constant $r$.
    The terms inside the expectations in the second and third lines are well defined if they are square integrable martingales (a martingale $\{M_t\}_{t\geq0}$ is square
    integrable if $\mathbb{E}[M_t^2] < \infty$ for every $t$). Now we verify that they are well defined by using the well known *Itô isometry*
    (for more information see Chapter 8 of [Cont and Tankov, 2003]).
    Let us look at the integrability condition for the term (II).

    $$\begin{aligned}
    & \mathbb{E}^{\mathbb{Q}} \biggl[ \int_t^{\tau} \big| e^{-r(u-t)} \frac{\partial V(u,X_{u^-})}{\partial x} \sigma \big|^2 du \; \bigg| X_t=x \biggr] \\
    & \leq \sigma^2 C^2\, \mathbb{E}^{\mathbb{Q}} \biggl[ \int_t^{\tau} \big| e^{-r(u-t)} \big|^2 du \; \bigg| X_t=x \biggr] < \infty
    \end{aligned}$$

    where we used the fact that the derivative is bounded by a constant $C$.
    Let us look at the integrability condition for the term (III).

    $$\begin{aligned}
    & \mathbb{E}^{\mathbb{Q}} \biggl[ \int_t^{\tau} \int_{\mathbb{R}} \bigg| e^{-r(u-t)} \bigl( V(u,X_{u^-} + z) - V(u,X_{u^-}) \bigr) \bigg|^2 \nu(dz) \, dt \; \bigg| X_t=x \biggr]  \\
    & \leq \mathbb{E}^{\mathbb{Q}} \biggl[ \int_t^{\tau} \int_{\mathbb{R}} \bigg| e^{-r(u-t)} C z \bigg|^2 \nu(dz) \, dt \; \bigg| X_t=x \biggr]  \\
    & \leq C^2 \int_{\mathbb{R}} z^2 \, \nu(dz) \; \int_t^{T} \bigg| e^{-r(u-t)} \bigg|^2 dt < \infty.
    \end{aligned}$$

    In the second line we used the Lipschitz property of $V(t,x)$. A $C^1(\mathbb{R})$ function $f$ with bounded derivative is Lipschitz. This can be easily proved:
    let $a,b \in \mathbb{R}$ with $a<b$, by the mean value theorem there exists $c\in [a,b]$ such that $f(b)-f(a) = f'(c) (b-a)$. Using $|f'(c)|\leq C$, we obtain the Lipschitz condition $f(b)-f(a) \leq C (b-a)$.

    In the third line, the integral $\int_{\mathbb{R}} z^2 \, \nu(dz)$ is finite thanks to the Lévy measure definition and the finite second moment assumption.
    We just verified that these terms are square integrable martingales. It follows that their expectation is zero!

    Now let us consider term (I).
    By definition, the terms inside the integral are all continuous and are all bounded by some linear function.
    We can divide both sides by $(\tau-t)$ and take the limit for $\tau \to t$. Using the mean value theorem, there exists $u \in [t,\tau]$ such that

    $$\lim_{u \to t} \mathbb{E}^{\mathbb{Q}} \biggl[ e^{-r(u-t)} \biggl( \frac{\partial V(u,X_u)}{\partial u} + \mathcal{L} V(u,X_u) -r V(u,X_u) \biggr) \bigg| X_t=x \biggr] = 0.$$

    When $\tau\to t$ also $u\to t$. Thanks to the dominated convergence theorem we can take the limit inside the expectation and conclude the proof.

In practice, the hypothesis of the theorem above are rarely satisfied.
The payoff $\Phi$ is usually not in the domain of $\mathcal{L}$ and sometimes is not even differentiable, e.g. call/put options.
For this reason, the option price should be considered a solution of the PIDE in a weaker sense.
The notion of *viscosity solution* allows to cover this case.
For a complete exposition on this topic, we refer to [Cont and Voltchkova, 2005b], where the authors prove that in a general setting,
option prices in exponential Lévy models correspond to viscosity solutions of the pricing PIDE.

The **pricing PIDE** is:

$$\begin{aligned}
&  \frac{\partial V(t,x)}{\partial t} - r V(t,x)
          + \biggl( r -\frac{1}{2}\sigma^2 - \int_{\mathbb{R}} \bigl( e^z-1-z \bigr) \nu(dz) \biggr) \frac{\partial V(t,x)}{\partial x} \\
          &+ \frac{1}{2} \sigma^2 \frac{\partial^2 V(t,x)}{\partial x^2}
          + \int_{\mathbb{R}} \bigl( V(t,x+z)- V(t,x) - z \frac{\partial V(t,x)}{\partial x} \bigr) \nu(dz)  = 0.
\end{aligned}$$

With boundary conditions:

**CALL:**

- Terminal: $V(T,x) = \max(e^x-K,0)$
- Lateral: $V(t, x) \underset{x \to -\infty}{=} 0 \quad \mbox{and} \quad V(t, x) \underset{x \to \infty}{\sim} e^x - Ke^{-r(T-t)}$

**PUT:**

- Terminal: $V(T,x) = \max(K-e^x,0)$
- Lateral: $V(t, x) \underset{x \to -\infty}{\sim} Ke^{-r(T-t)} \quad \mbox{and} \quad V(t, x) \underset{x \to \infty}{=} 0$

## 4. PIDEs

### 4.1 Black-Scholes PDE

The [Black and Scholes, 1973] model assumes a geometric Brownian motion for the dynamics of the underlying.
Let us consider a Lévy process $\{X_t\}_{t\geq 0}$ with triplet $(b,\sigma,0)$.
Using these values of the triplet, the pricing PDE is

$$
\frac{\partial  V(t,x)}{\partial t}
          + \biggl( r -\frac{1}{2}\sigma^2 \biggr) \frac{\partial V(t,x)}{\partial x}
          + \frac{1}{2} \sigma^2 \frac{\partial^2  V(t,x)}{\partial x^2} - r  V(t,x)  = 0.
$$

This is the Black-Scholes PDE in log-variables.
The Lévy measure is identically null and therefore there is no integral term.

### 4.2 Merton PIDE

The Merton model was presented in Section 2.2.
Let us recall that the jump component of the Merton process has finite activity, $\nu(\mathbb{R}) = \lambda < \infty$.
The pricing PIDE becomes:

$$\begin{aligned}
&  \frac{\partial V(t,x)}{\partial t} - r V(t,x)
          + \biggl( r -\frac{1}{2}\sigma^2 -m \biggr) \frac{\partial V(t,x)}{\partial x} \\
          &+ \frac{1}{2} \sigma^2 \frac{\partial^2 V(t,x)}{\partial x^2}
          + \int_{\mathbb{R}} V(t,x+z) \, \nu(dz) - \lambda V(t,x)  = 0.
\end{aligned}$$

with $m$ defined as

$$\begin{aligned}
m :=& \; \int_{\mathbb{R}} ( e^{x} - 1 ) \, \nu(dx) \\
    =& \; \lambda \bigl( \phi_X(-i) - 1 \bigr) \\
    =& \; \lambda \biggl( e^{\alpha + \frac{1}{2} \xi^2} -1 \biggr).
\end{aligned}$$

where $X \sim \mathcal{N}(\alpha, \xi^2)$.
Recall that the Lévy measure is a scaled normal distribution.
The previous equation is called **Merton PIDE**, in log-variables.

### 4.3 Variance Gamma PIDE

We introduced the Variance Gamma process in Section 2.3.
The VG process has infinite activity i.e.
$\nu(\mathbb{R}) = \infty$ and has the triplet presented earlier,
with $\nu$ as given in the VG Lévy measure.

From the general PIDE pricing formula, we obtain the **VG PIDE**:

$$
\frac{\partial V(t,x)}{\partial t} + (r-w) \frac{\partial V(t,x)}{\partial x}
+ \int_{\mathbb{R}} \bigl[ V(t,x+z) - V(t,x) \bigr] \nu(dz) = rV(t,x) .
$$

with $w$ defined as:

$$
w := \int_{\mathbb{R}} (e^x-1) \, \nu(dx) = - \frac{1}{\kappa} \log \left( 1-\theta \kappa -\frac{1}{2}\bar\sigma^2 \kappa \right).
$$

Here it is not possible to separate the integrands because the process has infinite activity, and they are both infinite.
However, since the VG process has finite variation, this integral is finite because $e^x-1 = x + \mathcal{O}(x^2)$.

In order to calculate the integral, we use the following relation between the Lévy measure and the transition probability $p_{0,t}(0,dx)$ (the
probability that the process starting from $0$ at time $0$, is inside the interval $dx$ at time $t$) of the process:

$$
\nu(dx) = \lim_{t\to 0} \frac{1}{t} p_{0,t}(0,dx).
$$

This relation is presented by [Cont and Tankov, 2003] in Chapter 3.6, and a proof can be found in Corollary 8.9 of [Sato, 1999].
Let us compute the expected value of the exponential VG process

$$\begin{aligned}
\mathbb{E}[ e^{X_t}] &= \phi_{X_t}(-i) = \exp \biggl( -\frac{t}{\kappa} \log\!\left(1-\theta \kappa -\frac{1}{2}\bar\sigma^2 \kappa \right) \biggr)\\
&= e^{w t}
\end{aligned}$$

where we called $w = - \frac{1}{\kappa} \log(1-\theta \kappa -\frac{1}{2}\bar\sigma^2 \kappa)$.
The integral becomes

$$\begin{aligned}
\int_{\mathbb{R}} (e^x-1) \, \nu(dx) &= \int_{\mathbb{R}} (e^x-1) \lim_{t\to 0} \frac{1}{t} p_{0,t}(0,dx) \\
         &= \lim_{t\to 0} \frac{1}{t} \mathbb{E}[ e^{X_t} - 1 ] \\
         &= \lim_{t\to 0} \frac{1}{t} \biggl( e^{w t} - 1 \biggr) \\
         &= w.
\end{aligned}$$

We can always take the limit outside the integral, because the integral is finite.

#### 4.3.1 Brownian Approximation

Unfortunately, it is not straightforward to solve the VG PIDE. The Lévy measure has a singularity in the origin,
that should be removed before any kind of discretization.

An idea to overcome this problem, that can be applied to any Lévy process with infinite activity, is presented in [Cont and Voltchkova, 2005a].
The authors propose to approximate the process $\{L_t\}_{t\geq0}$ by an
appropriate finite activity process with a modified diffusion component.
The "small jumps" martingale component is approximated by a Brownian motion with same variance.
After fixing a truncation parameter $\epsilon >0$, the integrals in the SDE are split in two domains: $\{|z|<\epsilon\}$ and $\{|z|\geq \epsilon\}$.
The integrand on the domain $\{ |z|<\epsilon \}$, is approximated by the Taylor expansion
$e^z-1-z = \frac{z^2}{2} + \mathcal{O}(z^3)$ such that

$$\begin{aligned}
dL_t =& \biggl( r -\frac{1}{2}\sigma^2 - \int_{\mathbb{R}} \bigl( e^z-1-z \bigr) \nu(dz) \biggr)dt + \sigma \, dW_t + \int_{\mathbb{R}} z \tilde N(dt,dz) \\
       =& \biggl( r - \frac{1}{2}\sigma^2 -\int_{|z|<\epsilon} (e^z-1-z) \, \nu(dz) -\int_{|z|\geq \epsilon} (e^z-1-z) \, \nu(dz)  \biggr) dt\\
        &+ \sigma \, dW_t + \underbrace{\int_{|z|< \epsilon} z \tilde N(dt,dz)}_{\approx\; \sigma_{\epsilon} dW_t} + \int_{|z| \geq \epsilon} z \tilde N(dt,dz) \\
       =& \biggl( r - \frac{1}{2} (\sigma^2 + \sigma_{\epsilon}^2) - w_{\epsilon} + \lambda_{\epsilon} \theta_{\epsilon}  \biggr) dt + \bigl( \sigma+\sigma_{\epsilon}\bigr) dW_t
       + \int_{|z|\geq \epsilon} z \tilde N(dt,dz) ,
\end{aligned}$$

where we defined the new parameters

$$\begin{aligned}
& \sigma_{\epsilon}^2 :=  \int_{|z| < \epsilon} z^2 \, \nu(dz), \quad \quad w_{\epsilon} := \int_{|z| \geq \epsilon} (e^z-1) \, \nu(dz), \\
& \lambda_{\epsilon} :=  \int_{|z| \geq \epsilon} \nu(dz), \quad \quad \theta_{\epsilon} := \frac{1}{\lambda_{\epsilon}} \int_{|z| \geq \epsilon} z \, \nu(dz) .
\end{aligned}$$

The process $\int_{|z|\geq \epsilon} z \tilde N(dt,dz)$ is a compensated Poisson process with finite activity $\lambda_{\epsilon}$.

For the VG process, where $\sigma = 0$, the approximated dynamics is thus

$$
dL_t = \biggl( r - \frac{1}{2} \sigma_{\epsilon}^2 - w_{\epsilon} + \lambda_{\epsilon} \theta_{\epsilon}  \biggr) dt
       + \sigma_{\epsilon} \, dW_t + \int_{|z|\geq \epsilon} z \tilde N(dt,dz),
$$

or the equivalent

$$
dL_t = \biggl( r - \frac{1}{2} \sigma_{\epsilon}^2 - w_{\epsilon}  \biggr) dt
       + \sigma_{\epsilon} \, dW_t + \int_{|z|\geq \epsilon} z N(dt,dz),
$$

where the parameters are obtained from the Lévy measure.

The **approximated VG PIDE** is:

$$\begin{aligned}
&  \frac{\partial V(t,x)}{\partial t} +
\bigl( r-\frac{1}{2}\sigma_{\epsilon}^2 - w_{\epsilon} \bigr) \frac{\partial V(t,x)}{\partial x}
+ \frac{1}{2}\sigma_{\epsilon}^2 \frac{\partial^2 V(t,x)}{\partial x^2} \\
&+ \int_{|z| \geq \epsilon} V(t,x+z) \, \nu(dz) = (\lambda_{\epsilon} + r) V(t,x).
\end{aligned}$$

It has the same "jump-diffusion" form of the Merton PIDE, except for the truncation in the integral.

## References

1. Applebaum, D. (2009). *Lévy Processes and Stochastic Calculus*. Cambridge University Press; 2nd edition.
2. Barndorff-Nielsen (1997). Processes of Normal Inverse Gaussian type. *Finance and Stochastics*, 2:41–68.
3. Black, F. and Scholes, M. (1973). The pricing of options and corporate liabilities. *The Journal of Political Economy*, 81(3):637–654.
4. Carr, P., Geman, H., D.B., M., and M., Y. (2002). The fine structure of asset returns: An empirical investigation. *Journal of Business*, 75(2):305–333.
5. Cont, R., Potters, M., and Bouchaud, J. (1997). Scaling in stock market data: stable laws and beyond. *Scale invariance and beyond, Springer*.
6. Cont, R. and Tankov, P. (2003). *Financial Modelling with Jump Processes*. Chapman and Hall/CRC; 1st edition.
7. Cont, R. and Voltchkova, E. (2005a). A finite difference scheme for option pricing in jump diffusion and exponential Lévy models. *SIAM Journal of Numerical Analysis*, 43(4):1596–1626.
8. Cont, R. and Voltchkova, E. (2005b). Integro-differential equations for option prices in exponential Lévy models. *Finance and Stochastics*, 9:299–325.
9. Eberlein, E. and Keller, U. (1995). Hyperbolic distributions in finance. *Bernoulli*, 1(3):281–299.
10. Kabasinskas, A., Rachev, S., Sakalauskas, L., Wei, S., and Belovas, I. (2009). Alpha-stable paradigm in financial markets. *Journal of Computational Analysis and Applications*, 11(4):641–669.
11. Kou, S. (2002). A jump-diffusion model for option pricing. *Management Science*, 48(8):1086–1101.
12. Madan, D., Carr, P., and Chang, E. (1998). The Variance Gamma process and option pricing. *European Finance Review*, 2:79–105.
13. Madan, D. and Seneta, E. (1990). The Variance Gamma (V.G.) model for share market returns. *The Journal of Business*, 63(4):511–524.
14. Mandelbrot, B. (1963). Modeling financial data with stable distributions. *Journal of Business*, XXXVI(1):392–417.
15. Merton, R. (1976). Option pricing when underlying stock returns are discontinuous. *Journal of Financial Economics*, 3:125–144.
16. Papapantoleon, A. An introduction to Lévy processes with applications in finance. *Available on [arXiv](https://arxiv.org/abs/0804.0482)*.
17. Sato, K. I. (1999). *Lévy processes and infinitely divisible distributions*. Cambridge University Press.
18. Schoutens, W. (2003). *Lévy processes in finance*. Wiley, First Edition.
