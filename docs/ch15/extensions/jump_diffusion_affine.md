# Jump-Diffusion Affine Models

Pure diffusion models, however sophisticated, cannot capture the sudden large moves --- earnings surprises, flash crashes, central bank announcements --- that punctuate financial time series. The affine jump-diffusion framework extends the theory by adding **compound Poisson jumps** with state-dependent intensity to the continuous dynamics, while preserving the exponential-affine characteristic function. The jump contribution enters the Riccati system through an additional term involving the moment generating function of the jump size distribution, and the entire pricing machinery --- Fourier inversion, bond pricing, calibration --- carries over with minimal modification. This section derives the extended Riccati equations, presents the Bates model as the canonical example, and discusses the choice of jump size distributions.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Write down the SDE for an affine jump-diffusion and identify the jump compensator
    2. Derive the extended Riccati system incorporating jump contributions
    3. Explain why affine jump intensity and exponential moment generating functions preserve the affine structure
    4. Formulate the Bates model (Heston + Merton jumps) and compute its characteristic function
    5. Compare log-normal, double-exponential, and self-exciting jump specifications

---

## Motivation

### Why Jumps Matter

The Black-Scholes and Heston models produce continuous sample paths. However, empirical asset returns exhibit:

- **Excess kurtosis** far beyond what stochastic volatility alone can generate at short maturities
- **Short-maturity implied volatility smiles** that are too steep to be explained by diffusion models
- **Discontinuous price gaps** at market open, around earnings announcements, and during crises

Jumps provide a natural mechanism for these features. At random Poisson times, the asset price experiences an instantaneous multiplicative shock, generating heavy tails in the return distribution and steep short-maturity smiles. The key question is: can we add jumps without destroying the analytical tractability of the affine framework?

The answer is yes, provided the jump intensity and the jump size distribution satisfy specific conditions that maintain the affine structure of the generator.

---

## The Affine Jump-Diffusion SDE

### General Specification

!!! info "Definition: Affine Jump-Diffusion"
    A $d$-dimensional affine jump-diffusion $X_t$ on $D = \mathbb{R}_+^m \times \mathbb{R}^{d-m}$ satisfies

    $$
    dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t + dJ_t
    $$

    where:

    - $\mu(x) = b_0 + Bx$ is the affine drift (including jump compensation)
    - $\sigma(x)\sigma(x)^\top = a_0 + \sum_i \alpha_i x^{(i)}$ is the affine diffusion
    - $J_t$ is a jump process with **affine compensator**:

    $$
    \nu(X_t, dz, dt) = \left(\lambda_0\,\nu_0(dz) + \sum_{i=1}^d \lambda_i\,X_t^{(i)}\,\nu_i(dz)\right)dt
    $$

    Here $\lambda_0 \geq 0$ and $\lambda_i \geq 0$ are intensity coefficients, and $\nu_0, \nu_1, \ldots, \nu_d$ are probability distributions on $\mathbb{R}^d \setminus \{0\}$ describing jump sizes.

The total jump intensity is $\Lambda(x) = \lambda_0 + \sum_i \lambda_i x^{(i)}$, which is affine in the state. The jump size distribution can depend on which component triggers the jump (through the index $i$) but not on the state value $x$.

### Compensated Jump Martingale

The jump process is decomposed as

$$
dJ_t = \int_{\mathbb{R}^d \setminus \{0\}} z\,\tilde{N}(dt, dz) + \int_{\mathbb{R}^d \setminus \{0\}} z\,\nu(X_{t^-}, dz)\,dt
$$

where $\tilde{N}(dt, dz) = N(dt, dz) - \nu(X_{t^-}, dz)\,dt$ is the compensated Poisson random measure. The deterministic part (the compensator) is absorbed into the drift $\mu(x)$.

---

## Extended Riccati System with Jumps

### The Key Result

!!! info "Theorem: Riccati System for Affine Jump-Diffusions"
    The conditional characteristic function of an affine jump-diffusion has the exponential-affine form

    $$
    \mathbb{E}\!\left[e^{u^\top X_T} \mid X_t = x\right] = \exp\!\bigl(\phi(\tau, u) + \psi(\tau, u)^\top x\bigr)
    $$

    where $\phi$ and $\psi$ satisfy the extended Riccati system:

    $$
    \frac{d\psi_i}{d\tau} = R_i(\psi) = (B^\top\psi)_i + \frac{1}{2}\psi^\top\alpha_i\psi + \lambda_i\!\left(\int e^{\psi^\top z}\,\nu_i(dz) - 1\right)
    $$

    $$
    \frac{d\phi}{d\tau} = F(\psi) = b_0^\top\psi + \frac{1}{2}\psi^\top a_0\psi + \lambda_0\!\left(\int e^{\psi^\top z}\,\nu_0(dz) - 1\right)
    $$

    with $\psi(0, u) = u$ and $\phi(0, u) = 0$.

The jump contribution to each equation is $\lambda_k(\hat{\nu}_k(\psi) - 1)$, where

$$
\hat{\nu}_k(u) = \int e^{u^\top z}\,\nu_k(dz) = \mathbb{E}_{\nu_k}\!\left[e^{u^\top Z}\right]
$$

is the moment generating function (MGF) of the jump size distribution $\nu_k$.

### Why the Structure Is Preserved

The affine structure of the Riccati system is maintained because:

1. The jump intensity $\Lambda(x) = \lambda_0 + \sum_i \lambda_i x^{(i)}$ is affine in $x$
2. The jump size MGF $\hat{\nu}_k(\psi)$ depends on $\psi$ but not on $x$
3. The product $\Lambda(x) \cdot (\hat{\nu}(\psi) - 1)$ is therefore affine in $x$: the constant part $\lambda_0(\hat{\nu}_0 - 1)$ enters $F(\psi)$, and the state-dependent parts $\lambda_i(\hat{\nu}_i - 1)$ enter $R_i(\psi)$

If either the jump intensity or the jump size distribution depended nonlinearly on $x$, the affine structure would break.

---

## Standard Jump Size Distributions

### Log-Normal Jumps (Merton)

The jump multiplier $Y = e^Z$ has $Z \sim N(\mu_J, \sigma_J^2)$. The MGF is

$$
\hat{\nu}(u) = \mathbb{E}[e^{uZ}] = \exp\!\left(\mu_J u + \frac{1}{2}\sigma_J^2 u^2\right)
$$

The jump contribution to the Riccati equation becomes

$$
\lambda\!\left(\exp\!\left(\mu_J\psi + \frac{1}{2}\sigma_J^2\psi^2\right) - 1\right)
$$

which is a smooth function of $\psi$ that can be evaluated in closed form.

### Double-Exponential Jumps (Kou)

The jump size has an asymmetric double-exponential distribution:

$$
\nu(dz) = \bigl(p\,\eta_1 e^{-\eta_1 z}\mathbf{1}_{\{z > 0\}} + (1-p)\,\eta_2 e^{\eta_2 z}\mathbf{1}_{\{z < 0\}}\bigr)dz
$$

with $\eta_1 > 1$ and $\eta_2 > 0$. The MGF is

$$
\hat{\nu}(u) = p\,\frac{\eta_1}{\eta_1 - u} + (1-p)\,\frac{\eta_2}{\eta_2 + u}
$$

defined for $-\eta_2 < \operatorname{Re}(u) < \eta_1$. The rational form of $\hat{\nu}$ leads to simpler Riccati equations than the log-normal case and admits analytical first-passage time distributions.

### Self-Exciting Jumps

In self-exciting (Hawkes-type) jump specifications, each jump increases the intensity of future jumps:

$$
d\Lambda_t = \kappa(\bar{\lambda} - \Lambda_t)\,dt + \delta\,dN_t
$$

where $N_t$ is the point process and $\delta > 0$ is the jump in intensity caused by each event. This specification is affine in the extended state $(X_t, \Lambda_t)$, placing it within the affine jump-diffusion framework at the cost of an additional state variable.

---

## The Bates Model

### Specification

The Bates (1996) model combines the Heston stochastic volatility model with Merton-type log-normal jumps in the log-price:

$$
d\log S_t = \left(r - \tfrac{1}{2}V_t - \lambda\bar{k}\right)dt + \sqrt{V_t}\left(\rho\,dW_t^{(1)} + \sqrt{1-\rho^2}\,dW_t^{(2)}\right) + Z_t\,dN_t
$$

$$
dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^{(1)}
$$

where $N_t$ is a Poisson process with constant intensity $\lambda$, $Z_t \sim N(\mu_J, \sigma_J^2)$ i.i.d., and $\bar{k} = e^{\mu_J + \sigma_J^2/2} - 1$ is the expected jump size.

### Affine Structure

With state $X_t = (V_t, \log S_t)^\top$, the Bates model is an $A_1(2)$ affine jump-diffusion:

- Drift: $b_0 = (\kappa\theta, r - \lambda\bar{k})^\top$, $B = \begin{pmatrix} -\kappa & 0 \\ -1/2 & 0 \end{pmatrix}$
- Diffusion: $a_0 = 0$, $\alpha_1 = \begin{pmatrix} \xi^2 & \rho\xi \\ \rho\xi & 1 \end{pmatrix}$
- Jumps: $\lambda_0 = \lambda$ (constant intensity), $\nu_0(dz) = N(\mu_J, \sigma_J^2)$ on the log-price component only

### Characteristic Function

The Riccati system for $\psi = (\psi_1, \psi_2)^\top$:

$$
\psi_2' = 0 \implies \psi_2(\tau) = u_2
$$

$$
\psi_1' = -\kappa\psi_1 - \frac{1}{2}u_2 + \frac{1}{2}\bigl(\xi^2\psi_1^2 + 2\rho\xi\psi_1 u_2 + u_2^2\bigr)
$$

$$
\phi' = \kappa\theta\psi_1 + (r - \lambda\bar{k})u_2 + \lambda\!\left(e^{\mu_J u_2 + \sigma_J^2 u_2^2/2} - 1\right)
$$

The equation for $\psi_1$ is exactly the Heston Riccati equation (independent of jumps). The jump term $\lambda(e^{\mu_J u_2 + \sigma_J^2 u_2^2/2} - 1)$ adds to the $\phi$ equation only, because the jump intensity is state-independent ($\lambda_0 = \lambda$, $\lambda_1 = 0$).

!!! tip "Separation of Diffusion and Jump Effects"
    In the Bates model, jumps affect only the $\phi$ equation, not the $\psi$ equation. This means the factor loading $\psi_1(\tau)$ (sensitivity to variance) is identical in Heston and Bates. The jump contribution modifies only the intercept $\phi(\tau)$. This separation makes calibration convenient: one can first fit the Heston parameters from the variance smile, then adjust the jump parameters to match short-maturity behavior.

---

## Impact on Pricing

### Short-Maturity Behavior

The most visible effect of jumps is at **short maturities**. For $\tau \to 0$, the diffusion contribution to option prices vanishes as $O(\sqrt{\tau})$, while the jump contribution is $O(\tau)$. This means:

- The short-maturity implied volatility smile width is controlled by jump parameters ($\lambda$, $\sigma_J$)
- The short-maturity skew is controlled by the mean jump size ($\mu_J$)
- Pure diffusion models (Heston without jumps) produce flat implied volatility at very short maturities

### Bond Pricing with Jumps

For the affine short rate $r_t = \rho_0 + \rho_1^\top X_t$ with jumps in the state, the bond price retains the exponential-affine form:

$$
P(t,T) = \exp\!\bigl(A(\tau) + B(\tau)^\top X_t\bigr)
$$

The Riccati system for $(A, B)$ incorporates both the discounting terms ($-\rho_0, -\rho_1$) and the jump terms ($\lambda_k(\hat{\nu}_k(B) - 1)$). In interest rate models with jump risk (e.g., jump-diffusion short-rate models), the jump term can generate yield curve features that pure diffusion models cannot, including sudden kinks at maturities corresponding to anticipated policy events.

---

## Summary

Affine jump-diffusions extend the continuous affine framework by adding compound Poisson jumps with state-dependent intensity $\Lambda(x) = \lambda_0 + \sum_i \lambda_i x^{(i)}$. The exponential-affine characteristic function is preserved because the jump contribution $\lambda_k(\hat{\nu}_k(\psi) - 1)$ enters the Riccati system additively, maintaining the separation between state-independent terms ($F$) and state-dependent terms ($R_i$). The Bates model combines Heston stochastic volatility with Merton log-normal jumps and illustrates the clean separation: jumps modify only the scalar function $\phi$, leaving the variance factor loading $\psi_1$ unchanged. Log-normal and double-exponential jump distributions are the standard choices, each with distinct analytical properties. Self-exciting jump specifications extend the framework at the cost of additional state variables. The practical value of affine jump-diffusions lies in their ability to match short-maturity implied volatility smiles that pure diffusion models cannot capture.

---

## Further Reading

- Bates, D. (1996). "Jumps and Stochastic Volatility: Exchange Rate Processes Implicit in Deutsche Mark Options." *Review of Financial Studies*, 9(1), 69--107.
- Duffie, D., Pan, J., and Singleton, K. (2000). "Transform Analysis and Asset Pricing for Affine Jump-Diffusions." *Econometrica*, 68(6), 1343--1376.
- Kou, S. (2002). "A Jump-Diffusion Model for Option Pricing." *Management Science*, 48(8), 1086--1101.
- Filipovic, D. (2009). *Term-Structure Models: A Graduate Course*. Springer.
