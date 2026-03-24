# Infinite-Dimensional SDEs


Because HJM models the forward rate curve for all maturities, it naturally leads to **infinite-dimensional stochastic differential equations**.

---

## Infinite-dimensional state space


At each time \(t\), the state is the function

\[
T \mapsto f(t,T),
\]


an element of a function space (e.g., a Hilbert space).

This contrasts with finite-dimensional short-rate models.

---

## Mathematical formulation


Formally, HJM can be written as an SDE in a function space:

\[
df_t = \alpha_t\,dt + \Sigma_t\,dW_t,
\]


where:
- \(f_t\) is a curve,
- \(\Sigma_t\) is a linear operator.

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

---

**Exercise 2.** A separable volatility structure takes the form $\sigma(t, T) = g(t)\,h(T)$ for some functions $g$ and $h$. Show that under this specification, the HJM forward rate $f(t, T)$ can be expressed as $f(t, T) = f(0, T) + \alpha_{\text{det}}(t, T) + h(T)\,X_t$, where $X_t$ is a one-dimensional stochastic process. Identify $X_t$ and its dynamics. This demonstrates a finite-dimensional realization.

---

**Exercise 3.** Consider the volatility $\sigma(t, T) = \sigma_0 e^{-\kappa(T-t)}$. Show that the resulting HJM model has a finite-dimensional realization by expressing $f(t, T)$ in terms of a single state variable $r_t = f(t, t)$ plus a deterministic function of $t$ and $T$. Identify this as the Hull--White model.

---

**Exercise 4.** For numerical implementation, the forward rate curve is discretized on a time--maturity grid $(t_i, T_j)$ with $0 = t_0 < t_1 < \cdots < t_M$ and $T_j = t_i + j\Delta T$. Describe how the HJM drift condition $\alpha(t_i, T_j) = \sigma(t_i, T_j)\sum_{k=i}^{j-1}\sigma(t_i, T_k)\,\Delta T$ is computed at each grid point. What is the computational complexity per time step if there are $N$ maturity points?

---

**Exercise 5.** Explain the concept of a **Musiela parameterization**, where $r_t(x) = f(t, t+x)$ with $x \geq 0$ representing time-to-maturity rather than calendar maturity. Write down the SDE for $r_t(x)$ and identify the additional "transport" term $\partial r_t(x)/\partial x$ that arises. Why is this parameterization more natural for infinite-dimensional analysis?

---

**Exercise 6.** A principal component analysis (PCA) of historical yield curve changes reveals that the first three factors explain 98% of the total variance, with factor loadings $e_1(T)$ (level), $e_2(T)$ (slope), and $e_3(T)$ (curvature). Describe how to construct a three-factor HJM model using $\sigma_i(t, T) = \lambda_i\,e_i(T-t)$, where $\lambda_i$ are scalar weights. Discuss the trade-off between the number of factors and computational cost in Monte Carlo simulation.
