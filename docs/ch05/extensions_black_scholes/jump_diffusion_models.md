# Jump-Diffusion Models

Jump-diffusion models augment the continuous diffusion of Black-Scholes with **discontinuous jumps**, capturing sudden large moves in asset prices. This produces heavy tails, short-maturity smiles, and more realistic risk profiles for extreme events.

---

## Motivation

### Limitations of Pure Diffusion

1. **No sudden moves**: Diffusions have continuous paths
2. **Short-maturity smile**: Black-Scholes produces flat smile for $T \to 0$
3. **Heavy tails**: Market returns have fatter tails than log-normal
4. **Crash risk**: Large instantaneous drops are impossible in pure diffusion

### Evidence for Jumps

- Flash crashes, earnings announcements, geopolitical events
- Implied volatility smiles steepen dramatically at short maturities
- Option prices imply non-zero probability of large moves

---

## Merton's Jump-Diffusion Model

### Dynamics

$$
\boxed{
\frac{dS_t}{S_{t^-}} = (r - \lambda\kappa)\,dt + \sigma\,dW_t + dJ_t
}
$$

where:
- $W_t$: Brownian motion (continuous part)
- $J_t$: Compound Poisson process (jump part)
- $\lambda$: Jump intensity (expected number of jumps per year)
- $\kappa = \mathbb{E}[Y - 1]$: Expected relative jump size

### Jump Structure

Jumps arrive at Poisson times with intensity $\lambda$. At each jump:

$$
S_t = S_{t^-} \cdot Y
$$

where $Y$ is the random jump multiplier.

**Merton's choice**: $\log Y \sim N(\mu_J, \sigma_J^2)$

Then: $\kappa = \mathbb{E}[Y - 1] = e^{\mu_J + \sigma_J^2/2} - 1$

### Drift Adjustment

The term $-\lambda\kappa$ ensures the discounted price is a martingale:

$$
\mathbb{E}^{\mathbb{Q}}[dS_t/S_{t^-}] = r\,dt
$$

---

## The PIDE (Partial Integro-Differential Equation)

### Pricing Equation

The option price $V(t, S)$ satisfies:

$$
\boxed{
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} + (r - \lambda\kappa)S\frac{\partial V}{\partial S} - rV + \lambda\int_0^\infty [V(t, Sy) - V(t, S)]\nu(dy) = 0
}
$$

where $\nu(dy)$ is the jump size distribution (for Merton: log-normal).

### The Integral Term

$$
\lambda\int_0^\infty [V(t, Sy) - V(t, S)]\nu(dy)
$$

represents the expected change in option value due to jumps.

### Comparison with Black-Scholes

| Term | Black-Scholes | Merton |
|------|---------------|--------|
| Diffusion | $\frac{1}{2}\sigma^2 S^2 V_{SS}$ | Same |
| Drift | $rSV_S$ | $(r-\lambda\kappa)SV_S$ |
| Discount | $-rV$ | Same |
| Jump | — | $\lambda\int[V(Sy) - V]\nu(dy)$ |

---

## Merton's Formula

### Closed-Form Solution

For European options, Merton derived a semi-analytical formula:

$$
\boxed{
C_{\text{Merton}} = \sum_{n=0}^\infty \frac{e^{-\lambda'T}(\lambda'T)^n}{n!} C_{\text{BS}}(S, K, T, r_n, \sigma_n)
}
$$

where:
- $\lambda' = \lambda(1 + \kappa)$
- $r_n = r - \lambda\kappa + n(\mu_J + \sigma_J^2/2)/T$
- $\sigma_n^2 = \sigma^2 + n\sigma_J^2/T$

### Interpretation

The option price is a weighted average of Black-Scholes prices, with weights given by Poisson probabilities for $n$ jumps occurring.

---

## Kou's Double-Exponential Model

### Motivation

Log-normal jumps in Merton don't produce enough skew. Asymmetric jumps work better.

### Jump Distribution

$$
f_Y(y) = p \cdot \eta_1 e^{-\eta_1 y}\mathbf{1}_{y>0} + (1-p) \cdot \eta_2 e^{\eta_2 y}\mathbf{1}_{y<0}
$$

- $p$: Probability of upward jump
- $\eta_1 > 1$: Rate of upward jump decay
- $\eta_2 > 0$: Rate of downward jump decay

### Advantages

- Asymmetric jumps capture skew
- Memoryless property enables analytical tractability
- Better fit to equity index options

---

## Calibration

### Parameters

| Parameter | Effect |
|-----------|--------|
| $\sigma$ | ATM volatility (continuous part) |
| $\lambda$ | Overall smile level |
| $\mu_J$ | Skew (asymmetry) |
| $\sigma_J$ | Smile convexity |

### Challenges

1. **Separation of $\sigma$ and $\lambda$**: Both affect total variance
2. **Term structure**: Jumps dominate short maturities, diffusion dominates long
3. **Stability**: Many local minima in optimization

### Typical Approach

1. Fit short-maturity smile to get jump parameters
2. Fit long-maturity level to get $\sigma$
3. Refine jointly

---

## Incomplete Markets

### The Issue

Jumps introduce another source of risk that cannot be hedged with the underlying alone.

### Hedging in Jump-Diffusion

- **Delta hedging**: Addresses diffusion risk only
- **Gamma hedging**: Addresses diffusion convexity only
- **Jump risk**: Requires options or other jump-sensitive instruments

### Risk-Neutral Measure

The jump intensity $\lambda$ and distribution $\nu$ under $\mathbb{Q}$ are not uniquely determined. Calibration to options implicitly selects a risk-neutral measure.

---

## Numerical Methods

### Fourier/FFT Methods

The characteristic function for Merton is known:

$$
\phi(u) = \exp\left[iuX_0 + (iu\omega - \frac{1}{2}u^2\sigma^2 + \lambda(\phi_Y(u) - 1))T\right]
$$

where $\phi_Y$ is the characteristic function of $\log Y$.

**FFT pricing**: Fast and accurate for European options.

### PIDE Methods

Discretize the integral term:

$$
\int V(Sy)\nu(dy) \approx \sum_k w_k V(Sy_k)
$$

Use implicit schemes for the differential part, explicit for the integral.

### Monte Carlo

```python
for i in range(N):
    # Diffusion part
    dW = sqrt(dt) * randn()
    S_diff = S[i] * exp((r - 0.5*sigma**2 - lambda*kappa)*dt + sigma*dW)
    
    # Jump part
    n_jumps = poisson(lambda * dt)
    if n_jumps > 0:
        J = prod(exp(mu_J + sigma_J * randn(n_jumps)))
    else:
        J = 1
    
    S[i+1] = S_diff * J
```

---

## Impact on Greeks

### Delta

Jumps reduce delta near the money (smile effect):

$$
\Delta_{\text{Merton}} < \Delta_{\text{BS}} \quad \text{(for ATM calls)}
$$

### Gamma

Concentrated near barriers and strikes due to jump risk.

### Vega

Decomposes into diffusion vega and jump vega:

$$
\mathcal{V}_{\text{total}} = \mathcal{V}_{\sigma} + \mathcal{V}_{\lambda} + \mathcal{V}_{\mu_J} + \mathcal{V}_{\sigma_J}
$$

---

## Extensions

### Stochastic Volatility + Jumps (SVJ)

Combine Heston with Merton:

$$
\begin{aligned}
dS_t &= (r - \lambda\kappa)S_t\,dt + \sqrt{v_t}S_t\,dW_t^{(1)} + S_t\,dJ_t \\
dv_t &= \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}
\end{aligned}
$$

### Jumps in Volatility

Some models include jumps in the variance process as well (SVJJ models).

### Lévy Processes

Generalize to infinite-activity jump processes (Variance Gamma, CGMY, NIG).

---

## Summary

$$
\boxed{
\frac{dS_t}{S_{t^-}} = (r - \lambda\kappa)\,dt + \sigma\,dW_t + dJ_t
}
$$

| Feature | Description |
|---------|-------------|
| **Jump process** | Compound Poisson with intensity $\lambda$ |
| **Jump size** | Log-normal (Merton) or double-exponential (Kou) |
| **Pricing** | PIDE with integral term |
| **Short-maturity smile** | Captured naturally |
| **Hedging** | Incomplete—jump risk unhedgeable with stock alone |

$$
\boxed{
C_{\text{Merton}} = \sum_{n=0}^\infty \frac{e^{-\lambda'T}(\lambda'T)^n}{n!} C_{\text{BS}}(S, K, T, r_n, \sigma_n)
}
$$

**Jump-diffusion models capture sudden large moves and short-maturity smiles that pure diffusion models cannot, at the cost of market incompleteness and more complex pricing equations.**
