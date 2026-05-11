# Infinite-Dimensional SDEs


Because HJM models the forward rate curve for all maturities, it naturally leads to **infinite-dimensional stochastic differential equations**.

---

## Infinite-dimensional state space


At each time $t$, the state is the function

$$
T \mapsto f(t,T)
$$


an element of a function space (e.g., a Hilbert space).

This contrasts with finite-dimensional short-rate models.

---

## Mathematical formulation


Formally, HJM can be written as an SDE in a function space:

$$
df_t = \alpha_t\,dt + \Sigma_t\,dW_t
$$


where:

- $f_t$ is a curve,
- $\Sigma_t$ is a linear operator.

Rigorous treatment uses stochastic calculus in Hilbert spaces.

---

## Finite-dimensional realizations


In practice, one often restricts to:

- separable volatility structures,
- finite-factor representations,
- basis expansions in maturity.

These yield **finite-dimensional realizations** consistent with HJM.

---

## Numerical implementation


Common approaches include:

- maturity discretization (time–maturity grids),
- factor models for volatility,
- projection onto basis functions.

Trade-offs arise between realism and tractability.

---

## Key takeaways


- HJM is intrinsically infinite-dimensional.
- Practical models use finite-factor approximations.
- Mathematical rigor guides stable implementation.

---

## Further reading


- Filipović, *Consistency Problems for HJM Models*.
- Da Prato & Zabczyk, infinite-dimensional SDEs.

---

## Exercises

**Exercise 1.** The HJM state at time $t$ is the entire forward rate curve $T \mapsto f(t, T)$. Explain why this is an element of a function space rather than $\mathbb{R}^n$. If you discretize the maturity axis into $N$ equally spaced points $T_1, \ldots, T_N$, what is the dimension of the resulting finite-dimensional approximation? For a 30-year curve with quarterly spacing, how many state variables does this produce?

??? success "Solution to Exercise 1"

    **Part 1: Why $f(t, T)$ is an element of a function space.**

    At each time $t$, the state of the HJM model is $T \mapsto f(t, T)$ for all maturities $T \geq t$. This is a real-valued function defined on the interval $[t, t + T_{\max}]$ (or $[t, \infty)$ in theory). To specify this state, one must provide a value for every $T$ in a continuum, which requires infinitely many real numbers. No finite collection of numbers $\{x_1, \ldots, x_n\} \in \mathbb{R}^n$ can specify a generic function on a continuous domain. The appropriate state space is a function space, such as $L^2([0, T_{\max}])$ (square-integrable functions) or a weighted Sobolev space $H^1$ (functions with square-integrable first derivatives).

    **Part 2: Dimension of the discretized approximation.**

    If we discretize the maturity axis into $N$ equally spaced points $T_1, \ldots, T_N$, then the state becomes the vector $(f(t, T_1), \ldots, f(t, T_N)) \in \mathbb{R}^N$. The dimension is $N$.

    **Part 3: Quarterly spacing over 30 years.**

    With quarterly spacing ($\Delta T = 0.25$ years) over a 30-year horizon:

    $$
    N = \frac{30}{0.25} = 120
    $$

    This produces **120 state variables** at each time step, which is a substantial but computationally feasible number. This illustrates the practical challenge of infinite-dimensional models: even a modest discretization leads to a high-dimensional state.

---

**Exercise 2.** A separable volatility structure takes the form $\sigma(t, T) = g(t)\,h(T)$ for some functions $g$ and $h$. Show that under this specification, the HJM forward rate $f(t, T)$ can be expressed as $f(t, T) = f(0, T) + \alpha_{\text{det}}(t, T) + h(T)\,X_t$, where $X_t$ is a one-dimensional stochastic process. Identify $X_t$ and its dynamics. This demonstrates a finite-dimensional realization.

??? success "Solution to Exercise 2"

    **Step 1: Write the HJM dynamics with separable volatility.**

    With $\sigma(t, T) = g(t)\,h(T)$, the drift condition gives:

    $$
    \alpha(t, T) = g(t)\,h(T) \int_t^T g(t)\,h(u)\,du = g(t)^2\,h(T)\int_t^T h(u)\,du
    $$

    The forward rate SDE is:

    $$
    df(t, T) = g(t)^2\,h(T)\int_t^T h(u)\,du\,dt + g(t)\,h(T)\,dW_t
    $$

    **Step 2: Factor out $h(T)$.**

    Notice that both the drift and diffusion terms contain $h(T)$ as a factor. Define:

    $$
    H(t, T) = \int_t^T h(u)\,du
    $$

    Then:

    $$
    df(t, T) = h(T)\left[g(t)^2 H(t, T)\,dt + g(t)\,dW_t\right]
    $$

    **Step 3: Integrate.**

    $$
    f(t, T) = f(0, T) + h(T)\int_0^t g(s)^2 H(s, T)\,ds + h(T)\int_0^t g(s)\,dW_s
    $$

    The stochastic part depends on $T$ only through $h(T)$. Define:

    $$
    X_t = \int_0^t g(s)\,dW_s
    $$

    Then:

    $$
    f(t, T) = f(0, T) + \underbrace{h(T)\int_0^t g(s)^2 H(s, T)\,ds}_{\alpha_{\text{det}}(t, T)} + h(T)\,X_t
    $$

    **Step 4: Identify $X_t$ and its dynamics.**

    $X_t$ is a one-dimensional Ito process satisfying:

    $$
    dX_t = g(t)\,dW_t, \quad X_0 = 0
    $$

    It is a Gaussian martingale with variance $\text{Var}(X_t) = \int_0^t g(s)^2\,ds$.

    **Remark on the deterministic term:** The term $\alpha_{\text{det}}(t, T)$ still depends on $T$ through $H(s, T) = \int_s^T h(u)\,du$, so it is not purely a function of $X_t$. However, it is fully deterministic (no randomness), so the forward curve $f(t, T)$ at time $t$ is determined by the single stochastic state variable $X_t$ plus deterministic functions. This is a **finite-dimensional realization**: one scalar random variable suffices to describe the entire stochastic evolution of the curve.

---

**Exercise 3.** Consider the volatility $\sigma(t, T) = \sigma_0 e^{-\kappa(T-t)}$. Show that the resulting HJM model has a finite-dimensional realization by expressing $f(t, T)$ in terms of a single state variable $r_t = f(t, t)$ plus a deterministic function of $t$ and $T$. Identify this as the Hull--White model.

??? success "Solution to Exercise 3"

    **Step 1: Write the forward rate dynamics.**

    With $\sigma(t, T) = \sigma_0 e^{-\kappa(T-t)}$, the drift condition gives:

    $$
    \alpha(t, T) = \frac{\sigma_0^2}{\kappa}e^{-\kappa(T-t)}\bigl(1 - e^{-\kappa(T-t)}\bigr)
    $$

    Integrating the SDE:

    $$
    f(t, T) = f(0, T) + \int_0^t \alpha(s, T)\,ds + \int_0^t \sigma_0 e^{-\kappa(T-s)}\,dW_s
    $$

    **Step 2: Factor out the $T$-dependence.**

    The stochastic integral can be written as:

    $$
    \int_0^t \sigma_0 e^{-\kappa(T-s)}\,dW_s = \sigma_0 e^{-\kappa T}\int_0^t e^{\kappa s}\,dW_s = e^{-\kappa(T-t)} \cdot \sigma_0 e^{-\kappa t}\int_0^t e^{\kappa s}\,dW_s \cdot e^{\kappa t}
    $$

    More carefully:

    $$
    \sigma_0\int_0^t e^{-\kappa(T-s)}\,dW_s = \sigma_0 e^{-\kappa(T-t)}\int_0^t e^{-\kappa(t-s)}\,dW_s
    $$

    **Step 3: Identify the short rate.**

    Setting $T = t$:

    $$
    r_t = f(t, t) = f(0, t) + \int_0^t \alpha(s, t)\,ds + \sigma_0\int_0^t e^{-\kappa(t-s)}\,dW_s
    $$

    The last integral is exactly the Ornstein--Uhlenbeck stochastic integral. By Ito's lemma, the process $Y_t = \sigma_0\int_0^t e^{-\kappa(t-s)}\,dW_s$ satisfies $dY_t = -\kappa Y_t\,dt + \sigma_0\,dW_t$.

    **Step 4: Express $f(t, T)$ in terms of $r_t$.**

    The forward rate can be written as:

    $$
    f(t, T) = \underbrace{f(0, T) + \int_0^t \alpha(s, T)\,ds - e^{-\kappa(T-t)}\left[f(0, t) + \int_0^t \alpha(s, t)\,ds\right]}_{\text{deterministic function of } t, T} + e^{-\kappa(T-t)}\,r_t
    $$

    This shows that $f(t, T)$ is a deterministic function of $(t, T)$ plus $e^{-\kappa(T-t)}\,r_t$, confirming a **finite-dimensional realization** with the single state variable $r_t$.

    **Step 5: Identify as Hull--White.**

    The short rate $r_t$ satisfies the mean-reverting SDE:

    $$
    dr_t = \bigl(\theta(t) - \kappa\,r_t\bigr)\,dt + \sigma_0\,dW_t
    $$

    for a deterministic function $\theta(t)$ determined by the initial curve $f(0, \cdot)$. This is precisely the **Hull--White model**. $\square$

---

**Exercise 4.** For numerical implementation, the forward rate curve is discretized on a time--maturity grid $(t_i, T_j)$ with $0 = t_0 < t_1 < \cdots < t_M$ and $T_j = t_i + j\Delta T$. Describe how the HJM drift condition $\alpha(t_i, T_j) = \sigma(t_i, T_j)\sum_{k=i}^{j-1}\sigma(t_i, T_k)\,\Delta T$ is computed at each grid point. What is the computational complexity per time step if there are $N$ maturity points?

??? success "Solution to Exercise 4"

    **Step 1: Discretized HJM drift.**

    At time $t_i$, for maturity $T_j = t_i + j\Delta T$, the discretized drift condition is:

    $$
    \alpha(t_i, T_j) = \sigma(t_i, T_j)\sum_{k=i}^{j-1}\sigma(t_i, T_k)\,\Delta T
    $$

    This is a Riemann sum approximation of $\sigma(t_i, T_j)\int_{t_i}^{T_j}\sigma(t_i, u)\,du$.

    **Step 2: Describe the computation.**

    At each time step $t_i$, for each maturity point $T_j$ (where $j$ ranges from $i+1$ to the maximum maturity index):

    1. Compute $\sigma(t_i, T_k)$ for all $k = i, \ldots, j-1$.
    2. Sum $S_j = \sum_{k=i}^{j-1}\sigma(t_i, T_k)\,\Delta T$ (the discretized bond volatility).
    3. Compute $\alpha(t_i, T_j) = \sigma(t_i, T_j) \cdot S_j$.
    4. Update the forward rate: $f(t_{i+1}, T_j) = f(t_i, T_j) + \alpha(t_i, T_j)\,\Delta t + \sigma(t_i, T_j)\,\sqrt{\Delta t}\,Z_i$ where $Z_i \sim N(0,1)$.

    **Step 3: Computational complexity.**

    The key observation is that the partial sums $S_j$ can be computed **incrementally**. Starting from $S_i = 0$:

    $$
    S_{j+1} = S_j + \sigma(t_i, T_j)\,\Delta T
    $$

    This means the cumulative sums for all $N$ maturity points require $O(N)$ additions. Each forward rate update is $O(1)$ once $S_j$ is known.

    Therefore, the **computational complexity per time step is $O(N)$** when using cumulative summation (not $O(N^2)$ as a naive implementation might suggest). Over $M$ time steps, the total cost is $O(MN)$ per simulation path.

---

**Exercise 5.** Explain the concept of a **Musiela parameterization**, where $r_t(x) = f(t, t+x)$ with $x \geq 0$ representing time-to-maturity rather than calendar maturity. Write down the SDE for $r_t(x)$ and identify the additional "transport" term $\partial r_t(x)/\partial x$ that arises. Why is this parameterization more natural for infinite-dimensional analysis?

??? success "Solution to Exercise 5"

    **Step 1: Define the Musiela parameterization.**

    Instead of indexing forward rates by calendar maturity $T$, define:

    $$
    r_t(x) := f(t, t + x), \quad x \geq 0
    $$

    Here $x = T - t$ is the **time-to-maturity**. The state at time $t$ is the function $x \mapsto r_t(x)$.

    **Step 2: Derive the SDE for $r_t(x)$.**

    Starting from $df(t, T) = \alpha(t, T)\,dt + \sigma(t, T)\,dW_t$, substitute $T = t + x$ where $x$ is held fixed:

    $$
    dr_t(x) = df(t, t+x) + \frac{\partial f(t, T)}{\partial T}\bigg|_{T=t+x} dt
    $$

    The second term arises because as $t$ increases by $dt$ with $x$ fixed, $T = t + x$ also increases by $dt$. By the chain rule:

    $$
    dr_t(x) = \left[\alpha(t, t+x) + \frac{\partial r_t(x)}{\partial x}\right]dt + \sigma(t, t+x)\,dW_t
    $$

    Using the drift condition $\alpha(t, t+x) = \sigma(t, t+x)\int_0^x \sigma(t, t+y)\,dy$ and writing $\tilde{\sigma}(t, x) = \sigma(t, t+x)$:

    $$
    dr_t(x) = \left[\frac{\partial r_t(x)}{\partial x} + \tilde{\sigma}(t, x)\int_0^x \tilde{\sigma}(t, y)\,dy\right]dt + \tilde{\sigma}(t, x)\,dW_t
    $$

    **Step 3: Identify the transport term.**

    The term $\frac{\partial r_t(x)}{\partial x}\,dt$ is the **transport** (or **shift**) term. It represents the aging of the forward rate: as time advances, a forward rate that had time-to-maturity $x$ now has time-to-maturity $x - dt$, causing the curve to shift leftward in the $x$ coordinate.

    **Step 4: Why this parameterization is more natural.**

    The Musiela parameterization is more natural for infinite-dimensional analysis because:

    1. The state $r_t(\cdot)$ always lives in the same function space (functions on $[0, \infty)$ or $[0, x_{\max}]$), regardless of $t$. In the original parameterization, $f(t, \cdot)$ is defined on $[t, \infty)$, a domain that shifts with $t$.
    2. The resulting SDE $dr_t = (\partial_x r_t + \ldots)\,dt + \ldots\,dW_t$ is a stochastic PDE (SPDE) on a fixed spatial domain, amenable to semigroup theory and functional analytic tools (e.g., the theory of Da Prato and Zabczyk).
    3. The transport term $\partial_x r_t$ generates a $C_0$-semigroup (the shift semigroup), providing a rigorous framework for existence and uniqueness of mild solutions.

---

**Exercise 6.** A principal component analysis (PCA) of historical yield curve changes reveals that the first three factors explain 98% of the total variance, with factor loadings $e_1(T)$ (level), $e_2(T)$ (slope), and $e_3(T)$ (curvature). Describe how to construct a three-factor HJM model using $\sigma_i(t, T) = \lambda_i\,e_i(T-t)$, where $\lambda_i$ are scalar weights. Discuss the trade-off between the number of factors and computational cost in Monte Carlo simulation.

??? success "Solution to Exercise 6"

    **Step 1: Construct the three-factor HJM model.**

    Given PCA eigenvectors $e_1, e_2, e_3$ and eigenvalues $\lambda_1, \lambda_2, \lambda_3$ (representing variances), set the HJM volatility functions to:

    $$
    \sigma_i(t, T) = \sqrt{\lambda_i}\,e_i(T - t), \quad i = 1, 2, 3
    $$

    Equivalently, using scalar weights $\lambda_i$ as stated in the problem:

    $$
    \sigma_i(t, T) = \lambda_i\,e_i(T - t)
    $$

    where the $\lambda_i$ are calibrated to match the observed eigenvalues. The forward rate dynamics are:

    $$
    df(t, T) = \alpha(t, T)\,dt + \sum_{i=1}^{3}\lambda_i\,e_i(T-t)\,dW_t^i
    $$

    with drift:

    $$
    \alpha(t, T) = \sum_{i=1}^{3}\lambda_i\,e_i(T-t)\int_t^T \lambda_i\,e_i(u-t)\,du = \sum_{i=1}^{3}\lambda_i^2\,e_i(T-t)\int_0^{T-t} e_i(y)\,dy
    $$

    **Step 2: Interpretation of the factors.**

    - Factor 1 (level): $e_1(\tau) \approx \text{const}$ --- parallel shifts of the curve.
    - Factor 2 (slope): $e_2(\tau)$ changes sign --- steepening/flattening.
    - Factor 3 (curvature): $e_3(\tau)$ is positive at extremes, negative in the middle --- butterfly movements.

    The model captures 98% of the observed yield curve variation.

    **Step 3: Trade-off between factors and computational cost.**

    In a Monte Carlo simulation with $d$ factors:

    - At each time step, one must generate $d$ independent standard normal random variables per path.
    - The forward rate update at each maturity point requires computing $d$ volatility loadings and $d$ drift contributions, so the per-maturity cost is $O(d)$.
    - With $N$ maturity grid points and $M$ time steps, the cost per path is $O(d \cdot M \cdot N)$.
    - Total cost for $P$ paths: $O(P \cdot d \cdot M \cdot N)$.

    The cost scales linearly in $d$. Going from 1 factor to 3 factors triples the computational cost. However, the improvement in accuracy is substantial: 1 factor captures ~80% of variance, 2 factors ~92--95%, and 3 factors ~96--99%.

    The practical trade-off: **2--3 factors** provide an excellent balance between accuracy and cost. Adding a 4th factor (explaining only 1--2% of variance) rarely justifies the 33% increase in computation. For instruments sensitive to curve shape (e.g., CMS spread options, butterfly spreads), 3 factors are typically necessary; for simpler instruments (e.g., vanilla caps), 1--2 factors often suffice.
