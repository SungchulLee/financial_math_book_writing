# Filtering and Bayesian Updating


**Filtering** and **Bayesian updating** provide principled frameworks for sequential inference when model parameters or states are latent.

---

## State-space models


Consider a state-space model:

$$
x_{t+1} = g(x_t) + \varepsilon_t, \quad
y_t = h(x_t) + \eta_t
$$



The latent state $x_t$ evolves over time and must be inferred from observations.

---

## Bayesian updating


Bayesian inference updates beliefs via

$$
p(x_t \mid y_{1:t}) \propto p(y_t \mid x_t) p(x_t \mid y_{1:t-1})
$$



This recursion underlies all filtering methods.

---

## Filtering techniques


Common filters include:
- Kalman filter (linear-Gaussian),
- Extended and Unscented Kalman filters,
- Particle filters for nonlinear/non-Gaussian models.

Choice depends on model complexity and accuracy needs.

---

## Financial applications


Filtering is widely used for:
- stochastic volatility estimation,
- latent factor models,
- regime-switching detection.

---

## Key takeaways


- Filtering performs sequential Bayesian inference.
- It handles latent states and noisy observations.
- Particle methods trade accuracy for computation.

---

## Further reading


- Kalman, linear filtering.
- Doucet et al., particle filtering.

---

## Exercises

**Exercise 1.** For a linear-Gaussian state-space model $x_{t+1} = 0.95 x_t + \varepsilon_t$ with $\varepsilon_t \sim N(0, 0.01)$ and $y_t = x_t + \eta_t$ with $\eta_t \sim N(0, 0.04)$, write down the Kalman filter prediction and update equations. Starting from $\hat{x}_0 = 0$ and $P_0 = 1$, compute the first two Kalman filter updates given observations $y_1 = 0.5$ and $y_2 = 0.3$.

??? success "Solution to Exercise 1"
    The linear-Gaussian state-space model is:

    - State equation: $x_{t+1} = 0.95\, x_t + \varepsilon_t$, with $\varepsilon_t \sim N(0, 0.01)$
    - Observation equation: $y_t = x_t + \eta_t$, with $\eta_t \sim N(0, 0.04)$

    In the standard Kalman filter notation: $A = 0.95$, $Q = 0.01$, $C = 1$, $R = 0.04$.

    **Kalman filter equations:**

    *Prediction step:*

    $$
    \hat{x}_{t|t-1} = A\,\hat{x}_{t-1|t-1} = 0.95\,\hat{x}_{t-1|t-1}
    $$

    $$
    P_{t|t-1} = A^2 P_{t-1|t-1} + Q = 0.9025\, P_{t-1|t-1} + 0.01
    $$

    *Update step:*

    $$
    S_t = P_{t|t-1} + R = P_{t|t-1} + 0.04
    $$

    $$
    K_t = \frac{P_{t|t-1}}{S_t} = \frac{P_{t|t-1}}{P_{t|t-1} + 0.04}
    $$

    $$
    \hat{x}_{t|t} = \hat{x}_{t|t-1} + K_t(y_t - \hat{x}_{t|t-1})
    $$

    $$
    P_{t|t} = (1 - K_t) P_{t|t-1}
    $$

    **First update ($t = 1$):** Starting from $\hat{x}_0 = 0$, $P_0 = 1$.

    Prediction:

    $$
    \hat{x}_{1|0} = 0.95 \times 0 = 0
    $$

    $$
    P_{1|0} = 0.9025 \times 1 + 0.01 = 0.9125
    $$

    Innovation and gain:

    $$
    S_1 = 0.9125 + 0.04 = 0.9525
    $$

    $$
    K_1 = \frac{0.9125}{0.9525} \approx 0.9580
    $$

    Update with $y_1 = 0.5$:

    $$
    \hat{x}_{1|1} = 0 + 0.9580 \times (0.5 - 0) = 0.4790
    $$

    $$
    P_{1|1} = (1 - 0.9580) \times 0.9125 = 0.04198 \times 0.9125 \approx 0.03831
    $$

    **Second update ($t = 2$):** Prediction:

    $$
    \hat{x}_{2|1} = 0.95 \times 0.4790 = 0.4551
    $$

    $$
    P_{2|1} = 0.9025 \times 0.03831 + 0.01 = 0.03457 + 0.01 = 0.04457
    $$

    Innovation and gain:

    $$
    S_2 = 0.04457 + 0.04 = 0.08457
    $$

    $$
    K_2 = \frac{0.04457}{0.08457} \approx 0.5270
    $$

    Update with $y_2 = 0.3$:

    $$
    \hat{x}_{2|2} = 0.4551 + 0.5270 \times (0.3 - 0.4551) = 0.4551 + 0.5270 \times (-0.1551) = 0.4551 - 0.08174 \approx 0.3733
    $$

    $$
    P_{2|2} = (1 - 0.5270) \times 0.04457 = 0.4730 \times 0.04457 \approx 0.02108
    $$

    Notice how the Kalman gain dropped from $0.958$ to $0.527$ between the first and second steps: as the posterior becomes more concentrated (smaller $P_{t|t}$), new observations receive less weight relative to the prior.

---

**Exercise 2.** Derive the Bayesian updating rule $p(x_t | y_{1:t}) \propto p(y_t | x_t) \, p(x_t | y_{1:t-1})$ from Bayes' theorem. Explain why the prediction step $p(x_t | y_{1:t-1}) = \int p(x_t | x_{t-1}) p(x_{t-1} | y_{1:t-1}) \, dx_{t-1}$ is computationally expensive for nonlinear models and how particle filters address this through Monte Carlo approximation.

??? success "Solution to Exercise 2"
    **Derivation of the Bayesian updating rule:**

    By Bayes' theorem, the posterior of the state given all observations up to time $t$ is:

    $$
    p(x_t \mid y_{1:t}) = \frac{p(y_t \mid x_t, y_{1:t-1})\, p(x_t \mid y_{1:t-1})}{p(y_t \mid y_{1:t-1})}
    $$

    The key assumption in state-space models is the conditional independence property: given $x_t$, the observation $y_t$ is independent of all past observations $y_{1:t-1}$. Therefore $p(y_t \mid x_t, y_{1:t-1}) = p(y_t \mid x_t)$, which yields:

    $$
    p(x_t \mid y_{1:t}) = \frac{p(y_t \mid x_t)\, p(x_t \mid y_{1:t-1})}{p(y_t \mid y_{1:t-1})}
    $$

    This is the update step, with $p(x_t \mid y_{1:t-1})$ serving as the prior (the prediction) and $p(y_t \mid x_t)$ as the likelihood.

    The **prediction step** expresses the prior using the Chapman-Kolmogorov equation:

    $$
    p(x_t \mid y_{1:t-1}) = \int p(x_t \mid x_{t-1})\, p(x_{t-1} \mid y_{1:t-1})\, dx_{t-1}
    $$

    This follows from marginalization over $x_{t-1}$ using the Markov property $p(x_t \mid x_{t-1}, y_{1:t-1}) = p(x_t \mid x_{t-1})$.

    **Why this is computationally expensive for nonlinear models:**

    The prediction integral requires evaluating a convolution of the transition density $p(x_t \mid x_{t-1})$ with the posterior $p(x_{t-1} \mid y_{1:t-1})$. For linear-Gaussian models, both are Gaussian and the integral yields another Gaussian (closed-form). For nonlinear models, $p(x_t \mid x_{t-1})$ may have a complex form, and the posterior $p(x_{t-1} \mid y_{1:t-1})$ may not belong to any tractable parametric family. The integral is generally intractable analytically.

    **How particle filters address this:** Particle filters approximate the posterior by a weighted sum of point masses:

    $$
    p(x_{t-1} \mid y_{1:t-1}) \approx \sum_{i=1}^N w_{t-1}^{(i)}\, \delta_{x_{t-1}^{(i)}}(x_{t-1})
    $$

    The prediction integral then becomes a finite sum: for each particle, draw $\tilde{x}_t^{(i)} \sim p(x_t \mid x_{t-1}^{(i)})$. This replaces the intractable integral with $N$ simulations from the transition kernel. The update step reweights particles by the likelihood: $w_t^{(i)} \propto p(y_t \mid \tilde{x}_t^{(i)})$. The accuracy improves as $N \to \infty$ at rate $O(N^{-1/2})$, regardless of the state dimension.

---

**Exercise 3.** The stochastic volatility model $\log \sigma_t^2 = \phi \log \sigma_{t-1}^2 + \eta_t$ with $r_t = \sigma_t \varepsilon_t$ is a nonlinear state-space model. Explain why the Kalman filter cannot be applied directly and describe how a particle filter with $N = 1000$ particles would estimate the latent volatility path. What is the resampling step and why is it necessary?

??? success "Solution to Exercise 3"
    The stochastic volatility model has state equation $\log \sigma_t^2 = \phi \log \sigma_{t-1}^2 + \eta_t$ (linear in the log-variance state) and observation equation $r_t = \sigma_t \varepsilon_t$ (nonlinear in the state).

    **Why the Kalman filter cannot be applied directly:**

    The Kalman filter requires a linear observation equation of the form $y_t = C x_t + v_t$. Here, $r_t = \exp(\frac{1}{2}\log \sigma_t^2) \cdot \varepsilon_t$. The observation depends on $x_t = \log \sigma_t^2$ through the exponential function $\exp(x_t/2)$, which is nonlinear. Moreover, the noise $\varepsilon_t$ enters multiplicatively (not additively), so the observation noise variance itself depends on the state. Neither condition required for the Kalman filter is satisfied.

    **Particle filter with $N = 1000$ particles:**

    *Initialization:* Draw $x_0^{(i)} = \log \sigma_0^{2,(i)} \sim p(x_0)$ for $i = 1, \ldots, 1000$, e.g., from the stationary distribution $x_0^{(i)} \sim N(0, \sigma_\eta^2 / (1 - \phi^2))$. Set $w_0^{(i)} = 1/1000$.

    *At each time $t$:*

    1. **Propagate:** For each particle, sample the next state from the transition:

        $$
        x_t^{(i)} = \phi\, x_{t-1}^{(i)} + \eta_t^{(i)}, \quad \eta_t^{(i)} \sim N(0, \sigma_\eta^2)
        $$

    2. **Weight:** Compute the likelihood of the observed return given each particle's volatility:

        $$
        \tilde{w}_t^{(i)} = p(r_t \mid x_t^{(i)}) = \frac{1}{\sqrt{2\pi}} \exp\!\left(-\frac{x_t^{(i)}}{2} - \frac{r_t^2}{2 \exp(x_t^{(i)})}\right)
        $$

        Normalize: $w_t^{(i)} = \tilde{w}_t^{(i)} / \sum_j \tilde{w}_t^{(j)}$.

    3. **Estimate volatility:** $\hat{\sigma}_t^2 = \sum_{i=1}^{1000} w_t^{(i)} \exp(x_t^{(i)})$.

    **Resampling step:** Compute the effective sample size $N_{\text{eff}} = 1/\sum_i (w_t^{(i)})^2$. If $N_{\text{eff}} < 500$, the weights are too concentrated on a few particles. Resample: draw 1000 new particles from the current set with replacement, where particle $i$ is selected with probability $w_t^{(i)}$. After resampling, all weights are reset to $1/1000$.

    **Why resampling is necessary:** Without resampling, after a few time steps, almost all the weight concentrates on one or two particles (weight degeneracy). The approximation effectively uses only a tiny fraction of the computational budget. Resampling eliminates low-weight particles and duplicates high-weight ones, ensuring the particle population remains representative of the posterior. The cost is reduced diversity (duplicated particles), which is mitigated by the subsequent propagation step that adds noise.

---

**Exercise 4.** Compare the Extended Kalman Filter (EKF) and the Unscented Kalman Filter (UKF) for a nonlinear observation equation $y_t = x_t^2 + \eta_t$. The EKF linearizes via $h'(x_t) = 2x_t$, while the UKF uses sigma points. For $\hat{x}_t = 3$ and $P_t = 0.5$, compute the EKF and UKF predicted observation means and variances. Which is more accurate?

??? success "Solution to Exercise 4"
    We have the nonlinear observation equation $y_t = x_t^2 + \eta_t$ with $\hat{x}_t = 3$ and $P_t = 0.5$.

    **EKF approach:** Linearize $h(x) = x^2$ around $\hat{x}_t = 3$:

    $$
    H_t = h'(\hat{x}_t) = 2\hat{x}_t = 6
    $$

    Predicted observation mean:

    $$
    \hat{y}_t^{\text{EKF}} = h(\hat{x}_t) = 3^2 = 9
    $$

    Predicted observation variance:

    $$
    S_t^{\text{EKF}} = H_t P_t H_t^\top + R = 6^2 \times 0.5 + R = 18 + R
    $$

    where $R = \text{Var}(\eta_t)$.

    **UKF approach:** For $n_x = 1$, we need $2(1) + 1 = 3$ sigma points. With parameter $\kappa$ (commonly $\kappa = 2$ for Gaussian), compute $\sqrt{(1 + \kappa)P_t} = \sqrt{3 \times 0.5} = \sqrt{1.5} \approx 1.2247$:

    $$
    \chi_0 = 3, \quad \chi_1 = 3 + 1.2247 = 4.2247, \quad \chi_2 = 3 - 1.2247 = 1.7753
    $$

    Propagate through $h(x) = x^2$:

    $$
    h(\chi_0) = 9, \quad h(\chi_1) = 17.848, \quad h(\chi_2) = 3.153
    $$

    With weights $w_0 = \kappa/(n_x + \kappa) = 2/3$ and $w_1 = w_2 = 1/(2(n_x + \kappa)) = 1/6$:

    Predicted observation mean:

    $$
    \hat{y}_t^{\text{UKF}} = w_0 \cdot 9 + w_1 \cdot 17.848 + w_2 \cdot 3.153 = 6 + 2.975 + 0.526 = 9.5
    $$

    Predicted observation variance (excluding $R$):

    $$
    S_t^{\text{UKF}} = w_0(9 - 9.5)^2 + w_1(17.848 - 9.5)^2 + w_2(3.153 - 9.5)^2 + R
    $$

    $$
    = \frac{2}{3}(0.25) + \frac{1}{6}(69.64) + \frac{1}{6}(40.27) + R = 0.167 + 11.607 + 6.712 + R = 18.486 + R
    $$

    **Comparison:** The true predicted observation mean is $\mathbb{E}[x_t^2] = \text{Var}(x_t) + (\mathbb{E}[x_t])^2 = P_t + \hat{x}_t^2 = 0.5 + 9 = 9.5$. The EKF predicts $\hat{y} = 9$, missing the variance contribution. The UKF predicts $\hat{y} = 9.5$, which is **exact**. The UKF is more accurate because it captures the second-order effect $\mathbb{E}[x^2] = \mu^2 + \sigma^2$ that the linearization misses. For the variance, the UKF also provides a better approximation by accounting for the curvature of $h(x) = x^2$.

---

**Exercise 5.** In a regime-switching model, the latent state $s_t \in \{1, 2\}$ follows a Markov chain. The Bayesian filter computes $P(s_t = i | y_{1:t})$ recursively. For transition matrix $P = \begin{pmatrix} 0.95 & 0.05 \\ 0.10 & 0.90 \end{pmatrix}$ and observation densities $p(y_t | s_t = 1) = N(0.05, 0.01)$ and $p(y_t | s_t = 2) = N(-0.10, 0.04)$, compute the filtered probability of being in regime 1 after observing $y_1 = -0.08$, starting from equal prior probabilities.

??? success "Solution to Exercise 5"
    **Setup:** Transition matrix $P = \begin{pmatrix} 0.95 & 0.05 \\ 0.10 & 0.90 \end{pmatrix}$, observation densities $p(y_t \mid s_t = 1) = N(0.05, 0.01)$ and $p(y_t \mid s_t = 2) = N(-0.10, 0.04)$, equal prior $\pi_0 = (0.5, 0.5)$.

    **Prediction step:** Compute the predicted regime probabilities using the transition matrix:

    $$
    P(s_1 = 1 \mid y_0) = P(s_1 = 1 \mid s_0 = 1)P(s_0 = 1) + P(s_1 = 1 \mid s_0 = 2)P(s_0 = 2)
    $$

    $$
    = 0.95 \times 0.5 + 0.10 \times 0.5 = 0.475 + 0.05 = 0.525
    $$

    $$
    P(s_1 = 2 \mid y_0) = 0.05 \times 0.5 + 0.90 \times 0.5 = 0.025 + 0.45 = 0.475
    $$

    **Update step with $y_1 = -0.08$:** Compute the likelihoods:

    $$
    p(y_1 = -0.08 \mid s_1 = 1) = \frac{1}{\sqrt{2\pi \times 0.01}} \exp\!\left(-\frac{(-0.08 - 0.05)^2}{2 \times 0.01}\right)
    $$

    $$
    = \frac{1}{0.2507} \exp\!\left(-\frac{0.0169}{0.02}\right) = 3.989 \exp(-0.845) = 3.989 \times 0.4296 \approx 1.714
    $$

    $$
    p(y_1 = -0.08 \mid s_1 = 2) = \frac{1}{\sqrt{2\pi \times 0.04}} \exp\!\left(-\frac{(-0.08 - (-0.10))^2}{2 \times 0.04}\right)
    $$

    $$
    = \frac{1}{0.5013} \exp\!\left(-\frac{0.0004}{0.08}\right) = 1.995 \exp(-0.005) \approx 1.995 \times 0.995 \approx 1.985
    $$

    The unnormalized filtered probabilities:

    $$
    \tilde{\pi}_1(1) = p(y_1 \mid s_1 = 1) \times P(s_1 = 1 \mid y_0) = 1.714 \times 0.525 = 0.8998
    $$

    $$
    \tilde{\pi}_1(2) = p(y_1 \mid s_1 = 2) \times P(s_1 = 2 \mid y_0) = 1.985 \times 0.475 = 0.9429
    $$

    Normalizing:

    $$
    P(s_1 = 1 \mid y_1) = \frac{0.8998}{0.8998 + 0.9429} = \frac{0.8998}{1.8427} \approx 0.4883
    $$

    $$
    P(s_1 = 2 \mid y_1) \approx 0.5117
    $$

    The filtered probability of being in regime 1 after observing $y_1 = -0.08$ is approximately **0.488**. The observation $-0.08$ is much more consistent with regime 2 (bear market, where $\mu_2 = -0.10$ and $\sigma_2 = 0.20$ give a near-center observation) than regime 1 (where $-0.08$ is $1.3$ standard deviations below the mean). Starting from equal priors, the posterior shifts slightly toward regime 2.

---

**Exercise 6.** Describe how a Kalman filter can be used to estimate time-varying hedge ratios. If the hedge ratio $\beta_t$ follows a random walk $\beta_{t+1} = \beta_t + w_t$ and the observation is $r_t^Y = \beta_t r_t^X + \varepsilon_t$, set up the state-space model and derive the Kalman filter equations for $\hat{\beta}_t$. How does the Kalman gain adapt as the signal-to-noise ratio changes?

??? success "Solution to Exercise 6"
    **State-space model setup:**

    - **State:** $x_t = \beta_t$ (the time-varying hedge ratio, scalar)
    - **State equation:** $\beta_{t+1} = \beta_t + w_t$, with $w_t \sim N(0, Q)$ (random walk)
    - **Observation equation:** $r_t^Y = \beta_t\, r_t^X + \varepsilon_t$, with $\varepsilon_t \sim N(0, R)$

    In standard Kalman filter form: $A_t = 1$, $B_t = 1$, $C_t = r_t^X$ (time-varying observation matrix), $Q_t = Q$, $R_t = R$.

    **Kalman filter equations for $\hat{\beta}_t$:**

    *Prediction:*

    $$
    \hat{\beta}_{t|t-1} = \hat{\beta}_{t-1|t-1}
    $$

    $$
    P_{t|t-1} = P_{t-1|t-1} + Q
    $$

    *Innovation:*

    $$
    e_t = r_t^Y - r_t^X \hat{\beta}_{t|t-1}
    $$

    $$
    S_t = (r_t^X)^2 P_{t|t-1} + R
    $$

    *Update:*

    $$
    K_t = \frac{P_{t|t-1}\, r_t^X}{S_t} = \frac{P_{t|t-1}\, r_t^X}{(r_t^X)^2 P_{t|t-1} + R}
    $$

    $$
    \hat{\beta}_{t|t} = \hat{\beta}_{t|t-1} + K_t\, e_t
    $$

    $$
    P_{t|t} = (1 - K_t\, r_t^X) P_{t|t-1}
    $$

    **How the Kalman gain adapts with signal-to-noise ratio:**

    The signal-to-noise ratio (SNR) is $(r_t^X)^2 P_{t|t-1} / R$. Rewriting the gain:

    $$
    K_t = \frac{P_{t|t-1}\, r_t^X}{(r_t^X)^2 P_{t|t-1} + R} = \frac{r_t^X}{\frac{R}{P_{t|t-1}} + (r_t^X)^2}
    $$

    - **High SNR** (large $|r_t^X|$ or large $P_{t|t-1}/R$): $K_t \approx 1/r_t^X$, so $K_t e_t \approx (r_t^Y - r_t^X \hat{\beta})/r_t^X$. The observation is highly informative and the estimate updates substantially.
    - **Low SNR** (small $|r_t^X|$ or small $P_{t|t-1}/R$): $K_t \approx P_{t|t-1} r_t^X / R \approx 0$. The observation is noisy and uninformative, so the estimate barely changes.

    This is the key advantage over OLS: when the hedging instrument has a small move ($r_t^X \approx 0$), the Kalman filter automatically recognizes the observation carries little information about $\beta$ and downweights it. When $r_t^X$ is large, the observation is informative and receives more weight. Additionally, $P_{t|t-1}$ grows by $Q$ each step (reflecting parameter uncertainty from drift), which gradually increases the gain over time, ensuring the filter remains adaptive to parameter changes.
