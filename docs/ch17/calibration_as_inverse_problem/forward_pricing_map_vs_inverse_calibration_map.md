# Forward Pricing Map vs Inverse Calibration Map


Calibration is best understood as an **inverse problem**: we observe market prices (or implied volatilities) and seek model parameters that reproduce them. This section formalizes the *forward* and *inverse* maps and highlights why the inverse map is delicate.

---

## The forward pricing map


Let a parametric model be indexed by a parameter vector

\[
\theta \in \Theta \subset \mathbb{R}^d.
\]


Given a set of traded instruments \(\{I_j\}_{j=1}^m\) (e.g., vanilla options across strikes/maturities), the model produces prices

\[
P_j(\theta) := \text{ModelPrice}(I_j;\theta).
\]



Define the **forward pricing map**

\[
F:\Theta \to \mathbb{R}^m,\qquad
F(\theta) := (P_1(\theta),\dots,P_m(\theta)).
\]



### 1. Practical choices of data space


Depending on conventions and numerical stability, calibration may target:

- **Option prices** \(P^{\text{mkt}}_j\)
- **Implied volatilities** \(\sigma^{\text{impl}}_j\) (via a Black–Scholes inversion)
- **Normalized prices** (e.g., by forward/discount factor)
- **Local or total variance** (e.g., \(w=T\sigma^2\))

To unify notation, let

\[
y \in \mathbb{R}^m
\]


denote the chosen market data representation, and let \(F(\theta)\) output the matching model representation.

---

## The inverse calibration map


In an ideal world, calibration would mean “invert the map”:

\[
\theta = F^{-1}(y).
\]


But \(F\) is rarely invertible globally, and even when it is locally invertible, inversion can be unstable.

Instead, calibration is typically formulated as an **optimization problem**:

\[
\hat\theta \in \arg\min_{\theta\in\Theta} \; \mathcal{L}(F(\theta), y),
\]


where \(\mathcal{L}\) is a loss (misfit) function.

Common choices include:

- **Least squares on prices**

  \[
  \mathcal{L}(F(\theta),y)=\frac12\sum_{j=1}^m w_j\,(P_j(\theta)-P^{\text{mkt}}_j)^2
  \]


- **Least squares on implied vols**

  \[
  \mathcal{L}(F(\theta),y)=\frac12\sum_{j=1}^m w_j\,(\sigma^{\text{impl}}_j(\theta)-\sigma^{\text{impl,mkt}}_j)^2
  \]


- **Robust losses** (Huber, \(\ell_1\)) to reduce sensitivity to outliers

---

## Local linearization and sensitivity


A key lens is the Jacobian of the forward map:

\[
J(\theta) := \nabla_\theta F(\theta) \in \mathbb{R}^{m\times d}.
\]



Near a reference \(\theta_0\), we have

\[
F(\theta_0+\Delta\theta) \approx F(\theta_0) + J(\theta_0)\Delta\theta.
\]



If \(J\) has small singular values, small perturbations in data (e.g., bid/ask noise) can induce large changes in \(\Delta\theta\). This is the core mechanism behind instability of inverse calibration.

---

## Typical “inverse” workflow (static)


1. **Choose instruments** (smile slices, maturities, liquidity filters)
2. **Choose data representation** (prices vs implied vols)
3. **Choose objective** \(\mathcal{L}\) and weights \(w_j\)
4. **Solve optimization** (local/global methods)
5. **Validate** (out-of-sample instruments, stability checks, hedging impact)

---

## Key takeaways


- Pricing is the **forward** map \(F(\theta)\); calibration seeks the **inverse**.
- The inverse is usually posed as **optimization**, not explicit inversion.
- The Jacobian/singular values of \(J\) govern **sensitivity** and motivate **regularization** (next sections).

---

## Further reading


- Inverse problems and regularization: Tikhonov & Arsenin; Engl, Hanke & Neubauer.
- Calibration in quantitative finance: Gatheral (*The Volatility Surface*); Cont & Tankov (*Financial Modelling with Jump Processes*).

---

## Exercises

**Exercise 1.** Consider a model with parameter vector $\theta = (\sigma, \rho) \in \mathbb{R}^2$ and three traded instruments whose model prices are given by

$$
P_1(\theta) = \sigma^2, \quad P_2(\theta) = \sigma \rho, \quad P_3(\theta) = \rho^2
$$

Write down the forward pricing map $F:\Theta \to \mathbb{R}^3$. Compute the Jacobian $J(\theta)$ and determine for which values of $\theta$ the Jacobian fails to have full column rank. What does this imply about the invertibility of $F$ near those points?

??? success "Solution to Exercise 1"
    The forward pricing map is

    $$
    F:\Theta \to \mathbb{R}^3, \quad F(\sigma, \rho) = (\sigma^2, \, \sigma\rho, \, \rho^2)
    $$

    The Jacobian is obtained by differentiating each component with respect to $\sigma$ and $\rho$:

    $$
    J(\theta) = \begin{pmatrix} \dfrac{\partial P_1}{\partial \sigma} & \dfrac{\partial P_1}{\partial \rho} \\[8pt] \dfrac{\partial P_2}{\partial \sigma} & \dfrac{\partial P_2}{\partial \rho} \\[8pt] \dfrac{\partial P_3}{\partial \sigma} & \dfrac{\partial P_3}{\partial \rho} \end{pmatrix} = \begin{pmatrix} 2\sigma & 0 \\ \rho & \sigma \\ 0 & 2\rho \end{pmatrix}
    $$

    For $J$ to have full column rank (rank 2), we need its two columns to be linearly independent. Consider the $2 \times 2$ minors:

    - Rows 1 and 2: determinant $= 2\sigma \cdot \sigma - 0 \cdot \rho = 2\sigma^2$
    - Rows 1 and 3: determinant $= 2\sigma \cdot 2\rho - 0 = 4\sigma\rho$
    - Rows 2 and 3: determinant $= \rho \cdot 2\rho - \sigma \cdot 0 = 2\rho^2$

    The Jacobian fails to have full column rank if and only if all three minors vanish simultaneously, which requires $\sigma = 0$ **and** $\rho = 0$.

    At $\theta = (0, 0)$, the Jacobian becomes the zero matrix and has rank 0. Near this point, the forward map is degenerate: $F(0,0) = (0, 0, 0)$ and the linearization provides no information about the parameters. By the inverse function theorem (applied to the square subsystem formed by any two rows of $J$), the map $F$ is locally invertible (onto its image) at every $\theta$ with $\sigma \neq 0$ or $\rho \neq 0$, but **not** at the origin. At $(0,0)$, infinitely many parameter vectors in a neighborhood map to nearly the same prices, so the calibration inverse problem is locally degenerate.

---

**Exercise 2.** Suppose we calibrate to $m = 5$ implied volatilities using a model with $d = 3$ parameters. The singular values of the Jacobian at the calibrated point are $\sigma_1 = 12.4$, $\sigma_2 = 3.1$, $\sigma_3 = 0.002$. Compute the condition number $\kappa$ of $J$. Suppose the market data are perturbed by $\|\varepsilon\| = 0.5$ vol points. Provide an upper bound on $\|\Delta\theta\|$ using the linearized sensitivity relation and comment on the practical implication.

??? success "Solution to Exercise 2"
    The condition number of the Jacobian is

    $$
    \kappa(J) = \frac{\sigma_1}{\sigma_3} = \frac{12.4}{0.002} = 6200
    $$

    From the linearized sensitivity relation, a data perturbation $\varepsilon$ induces a parameter perturbation bounded by

    $$
    \|\Delta\theta\| \le \|J^\dagger\| \cdot \|\varepsilon\|
    $$

    where $J^\dagger$ is the pseudoinverse. Since $J$ has full column rank ($d = 3 \le m = 5$), we have $J^\dagger = (J^\top J)^{-1} J^\top$ and $\|J^\dagger\|_2 = 1/\sigma_3 = 1/0.002 = 500$. Therefore

    $$
    \|\Delta\theta\| \le 500 \times 0.5 = 250
    $$

    This means a perturbation of merely 0.5 volatility points in the market data can induce a parameter shift of up to 250 in norm. The direction corresponding to the smallest singular value $\sigma_3 = 0.002$ is nearly unidentifiable: parameters can shift enormously along this direction with almost no effect on model prices. In practice, this implies:

    - The calibrated parameters are unreliable in the weakly constrained direction.
    - Regularization (e.g., Tikhonov penalty) or fixing one parameter is necessary.
    - Day-to-day parameter stability will be poor unless the ill-conditioned direction is addressed.

---

**Exercise 3.** A practitioner calibrates to option prices and obtains $\hat\theta_{\text{price}}$. She then re-calibrates using implied volatilities as the data representation and obtains $\hat\theta_{\text{vol}}$. Explain why $\hat\theta_{\text{price}}$ and $\hat\theta_{\text{vol}}$ may differ even though the underlying market data are the same. Which representation is more natural for out-of-the-money options and why?

??? success "Solution to Exercise 3"
    The two calibrations target different objective functions even though the underlying market data are identical. Specifically:

    **Price-based calibration** minimizes

    $$
    \mathcal{L}_{\text{price}} = \frac{1}{2}\sum_j (P_j(\theta) - P_j^{\text{mkt}})^2
    $$

    **Implied-vol-based calibration** minimizes

    $$
    \mathcal{L}_{\text{vol}} = \frac{1}{2}\sum_j (\sigma_j^{\text{impl}}(\theta) - \sigma_j^{\text{impl,mkt}})^2
    $$

    These differ because the map from prices to implied volatilities is **nonlinear** (it involves inverting the Black--Scholes formula). Consequently:

    1. **Different weighting:** In price space, deep out-of-the-money (OTM) options have very small prices, so price differences are small in absolute terms even when the implied volatility mismatch is large. Conversely, at-the-money (ATM) options have large prices and dominate the price-based objective. Implied-vol calibration weights all options more equally.

    2. **Different curvature:** The loss landscapes have different shapes, leading optimizers to different local minima or different points along a flat valley.

    3. **Nonlinear distortion:** Equal weights in price space correspond to Vega-dependent weights in implied-vol space (and vice versa), so the two objectives emphasize different parts of the smile.

    **For OTM options,** the implied volatility representation is more natural because:

    - OTM option prices are very small (often fractions of a cent for far OTM), making absolute price errors numerically meaningless.
    - Implied volatilities normalize for moneyness and time to expiry, putting all options on a comparable scale.
    - Bid-ask spreads in implied vol space are more uniform than in price space.
    - Traders quote and think in terms of implied volatility for OTM options.

---

**Exercise 4.** Let the forward map be $F(\theta) = A\theta + b$ for a matrix $A \in \mathbb{R}^{m \times d}$ and vector $b \in \mathbb{R}^m$. Show that the weighted least-squares calibration problem

$$
\min_\theta \frac{1}{2}(A\theta + b - y)^\top W (A\theta + b - y)
$$

has a unique solution if and only if $A^\top W A$ is invertible, and derive the closed-form expression for $\hat\theta$.

??? success "Solution to Exercise 4"
    With the affine forward map $F(\theta) = A\theta + b$, the weighted least-squares objective is

    $$
    \mathcal{L}(\theta) = \frac{1}{2}(A\theta + b - y)^\top W (A\theta + b - y)
    $$

    Setting the gradient to zero:

    $$
    \nabla_\theta \mathcal{L} = A^\top W (A\theta + b - y) = 0
    $$

    This yields the **normal equations**:

    $$
    A^\top W A \,\theta = A^\top W (y - b)
    $$

    This linear system has a unique solution if and only if $A^\top W A \in \mathbb{R}^{d \times d}$ is invertible. When it is, the closed-form solution is

    $$
    \hat\theta = (A^\top W A)^{-1} A^\top W (y - b)
    $$

    To confirm this is a minimum (not a maximum or saddle point), note that the Hessian is

    $$
    \nabla^2_\theta \mathcal{L} = A^\top W A
    $$

    Since $W$ is positive definite (it is a diagonal matrix of positive weights), $A^\top W A$ is positive semidefinite, and it is positive definite precisely when $A$ has full column rank (i.e., $A^\top W A$ is invertible). Thus uniqueness of the solution and strict convexity of the objective are equivalent conditions.

---

**Exercise 5.** Consider two loss functions for calibration: (i) least squares on prices, and (ii) least squares on implied volatilities. Let $\text{Vega}_j = \partial P_j / \partial \sigma_j^{\text{impl}}$ denote the Black-Scholes vega of the $j$-th option. Show that, to first order, calibrating on prices with equal weights $w_j = 1$ is equivalent to calibrating on implied volatilities with weights proportional to $\text{Vega}_j^2$.

??? success "Solution to Exercise 5"
    Let $P_j(\theta)$ be the model price and $\sigma_j^{\text{impl}}(\theta)$ the corresponding model implied volatility for option $j$. By definition, $P_j$ and $\sigma_j^{\text{impl}}$ are related through the Black--Scholes formula:

    $$
    P_j = \text{BS}(K_j, T_j, \sigma_j^{\text{impl}})
    $$

    Differentiating with respect to $\sigma_j^{\text{impl}}$:

    $$
    \frac{\partial P_j}{\partial \sigma_j^{\text{impl}}} = \text{Vega}_j
    $$

    Now consider a small perturbation $\delta\sigma_j^{\text{impl}}$ in implied volatility. To first order:

    $$
    \delta P_j \approx \text{Vega}_j \cdot \delta\sigma_j^{\text{impl}}
    $$

    The price-based least-squares loss with equal weights is

    $$
    \mathcal{L}_{\text{price}} = \frac{1}{2}\sum_{j=1}^m (P_j(\theta) - P_j^{\text{mkt}})^2
    $$

    Expressing the price residual in terms of the implied vol residual:

    $$
    P_j(\theta) - P_j^{\text{mkt}} \approx \text{Vega}_j \cdot (\sigma_j^{\text{impl}}(\theta) - \sigma_j^{\text{impl,mkt}})
    $$

    Substituting:

    $$
    \mathcal{L}_{\text{price}} \approx \frac{1}{2}\sum_{j=1}^m \text{Vega}_j^2 \, (\sigma_j^{\text{impl}}(\theta) - \sigma_j^{\text{impl,mkt}})^2
    $$

    This is precisely the implied-volatility least-squares loss with weights $w_j = \text{Vega}_j^2$:

    $$
    \mathcal{L}_{\text{price}} \approx \mathcal{L}_{\text{vol}}^{(w)}, \quad w_j = \text{Vega}_j^2
    $$

    Since Vega is largest for ATM options and decays for deep OTM/ITM options, price-based calibration with equal weights implicitly **overweights ATM options** and **underweights OTM options** relative to a uniform-weight implied-vol calibration.

---

**Exercise 6.** In the typical static calibration workflow, step 5 involves validation on out-of-sample instruments. Design a concrete validation procedure for a Heston model calibrated to S&P 500 options: specify what instruments you would hold out, what metrics you would evaluate, and what thresholds would indicate an acceptable calibration.

??? success "Solution to Exercise 6"
    A concrete validation procedure for a Heston model calibrated to S&P 500 options:

    **Holdout instruments:**

    - Reserve approximately 20--30% of the available option quotes as a test set. Specifically:
        - Hold out every third strike at each maturity (e.g., if calibrating to 10-delta through 90-delta, hold out the 20-delta, 50-delta, and 80-delta strikes).
        - Alternatively, hold out one or two entire maturities (e.g., the 2-month and 9-month expiries if calibrating to 1M, 3M, 6M, 1Y, 2Y).
        - Include at least some deep OTM puts (e.g., 5-delta puts) in the holdout set, as these are sensitive to the tail behavior the model may struggle with.

    **Metrics to evaluate:**

    1. **Root mean squared error (RMSE) in implied volatility** on the holdout set:

        $$
        \text{RMSE}_{\text{vol}} = \sqrt{\frac{1}{m_{\text{test}}}\sum_{j \in \text{test}} (\sigma_j^{\text{model}} - \sigma_j^{\text{mkt}})^2}
        $$

    2. **Maximum absolute implied volatility error** across the holdout set: $\max_j |\sigma_j^{\text{model}} - \sigma_j^{\text{mkt}}|$.

    3. **Weighted price error** relative to bid-ask spread: $|P_j^{\text{model}} - P_j^{\text{mid}}| / (\text{ask}_j - \text{bid}_j)$, measuring whether model prices fall within the bid-ask.

    4. **Smile shape diagnostics**: plot model vs. market implied volatility for each maturity to check for systematic bias (e.g., model underestimating skew or curvature).

    **Acceptability thresholds:**

    - $\text{RMSE}_{\text{vol}} < 0.5$ vol points (50 bps) for liquid maturities (1M--1Y).
    - Maximum error $< 1.5$ vol points for any individual option in the holdout set.
    - At least 80% of holdout prices within the bid-ask spread.
    - No systematic bias visible in smile plots (the residual pattern should look like noise, not a systematic over/undershoot in wings or at specific maturities).
    - Day-to-day parameter stability: recalibrate on 5 consecutive days and check that parameter variation is modest (e.g., $|\Delta\kappa/\kappa| < 20\%$, $|\Delta\rho| < 0.05$).

---

**Exercise 7.** Suppose the forward map satisfies $F(\theta_1) = F(\theta_2)$ for $\theta_1 \neq \theta_2$. Prove that the unregularized least-squares problem

$$
\min_\theta \|F(\theta) - y\|^2
$$

cannot have a unique global minimizer for any $y \in \mathrm{Range}(F)$. How does adding a Tikhonov penalty $\lambda \|\theta - \theta_{\text{prior}}\|^2$ resolve this issue?

??? success "Solution to Exercise 7"
    **Part 1: Non-uniqueness of the unregularized problem.**

    Suppose $F(\theta_1) = F(\theta_2)$ with $\theta_1 \neq \theta_2$. Let $y \in \mathrm{Range}(F)$, so there exists $\theta^\star$ with $F(\theta^\star) = y$.

    **Case 1:** If $y = F(\theta_1) = F(\theta_2)$, then both $\theta_1$ and $\theta_2$ achieve $\|F(\theta) - y\|^2 = 0$, which is the global minimum. Since $\theta_1 \neq \theta_2$, the minimizer is not unique.

    **Case 2:** If $y \neq F(\theta_1)$, let $y = F(\theta^\star)$ for some $\theta^\star$. Consider the map $G: \theta \mapsto \|F(\theta) - y\|^2$. We know $G(\theta^\star) = 0$ is the global minimum. Now, by hypothesis, there exist $\theta_1 \neq \theta_2$ with $F(\theta_1) = F(\theta_2)$. Define $\tilde{y} = F(\theta_1) = F(\theta_2)$. For the data value $\tilde{y}$, both $\theta_1$ and $\theta_2$ are global minimizers (with zero loss). Since this holds for every $y \in \mathrm{Range}(F)$, specifically for $y = \tilde{y}$, non-uniqueness is established.

    More precisely, for **any** $y \in \mathrm{Range}(F)$, non-uniqueness follows from this argument: since $F$ is not injective, there exist $\theta_1 \neq \theta_2$ with $F(\theta_1) = F(\theta_2) = \tilde y$. Taking $y = \tilde y$, both are global minimizers with loss zero.

    To strengthen this to arbitrary $y \in \mathrm{Range}(F)$: let $y = F(\theta^\star)$. The set of global minimizers is $F^{-1}(\{y\}) = \{\theta : F(\theta) = y\}$. We need to show this preimage always has more than one element. Note that non-injectivity of $F$ does not automatically imply that *every* level set has multiple elements. However, in the typical continuous/smooth setting of calibration, the level sets $F^{-1}(\{c\})$ vary continuously, and the set of $y$ for which $F^{-1}(\{y\})$ is a singleton is generically of measure zero. In the finite-dimensional smooth case, if $F$ is not injective and $\Theta$ is connected, then for a dense set of $y \in \mathrm{Range}(F)$, the preimage contains multiple points.

    Strictly speaking, the cleanest statement is: there exist values $y \in \mathrm{Range}(F)$ for which the global minimizer is not unique, namely $y = F(\theta_1) = F(\theta_2)$.

    **Part 2: Tikhonov regularization resolves non-uniqueness.**

    The regularized problem is

    $$
    \min_\theta \; \|F(\theta) - y\|^2 + \lambda \|\theta - \theta_{\text{prior}}\|^2
    $$

    Suppose $\theta_1 \neq \theta_2$ both satisfy $F(\theta_1) = F(\theta_2) = y$. Then:

    $$
    \|F(\theta_1) - y\|^2 + \lambda\|\theta_1 - \theta_{\text{prior}}\|^2 = \lambda\|\theta_1 - \theta_{\text{prior}}\|^2
    $$

    $$
    \|F(\theta_2) - y\|^2 + \lambda\|\theta_2 - \theta_{\text{prior}}\|^2 = \lambda\|\theta_2 - \theta_{\text{prior}}\|^2
    $$

    Unless $\|\theta_1 - \theta_{\text{prior}}\| = \|\theta_2 - \theta_{\text{prior}}\|$ (which is non-generic), the regularization term breaks the tie by selecting the parameter vector closest to the prior $\theta_{\text{prior}}$. More generally, the Tikhonov penalty makes the objective **strictly convex** in the linearized setting: if $F$ is approximately affine near the minimizer, the regularized normal equations become $(J^\top J + \lambda I)\Delta\theta = \ldots$, and $J^\top J + \lambda I$ is always positive definite for $\lambda > 0$, guaranteeing a unique local minimizer regardless of the rank of $J$.
