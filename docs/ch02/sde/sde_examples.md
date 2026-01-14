# SDE Examples in Quantitative Finance


This section presents canonical SDEs used in quantitative finance, with complete mathematical derivations and properties.

---

## Geometric Brownian Motion (GBM)


### 1. The Model


**SDE:**

$$
\boxed{
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t
}
$$

where:
- $S_t$ = asset price at time $t$
- $\mu$ = drift (expected return)
- $\sigma$ = volatility (standard deviation of returns)
- $W_t$ = standard Brownian motion

### 2. Derivation of the Solution


Apply Itô's lemma to $f(S) = \log S$:

$$
\frac{\partial f}{\partial S} = \frac{1}{S}, \quad \frac{\partial^2 f}{\partial S^2} = -\frac{1}{S^2}
$$

Therefore:

$$
\begin{align}
d(\log S_t) &= \frac{1}{S_t}dS_t + \frac{1}{2}\left(-\frac{1}{S_t^2}\right)(dS_t)^2 \\
&= \frac{1}{S_t}(\mu S_t\,dt + \sigma S_t\,dW_t) - \frac{1}{2S_t^2} \cdot \sigma^2 S_t^2\,dt \\
&= \mu\,dt + \sigma\,dW_t - \frac{\sigma^2}{2}\,dt \\
&= \left(\mu - \frac{\sigma^2}{2}\right)dt + \sigma\,dW_t
\end{align}
$$

Integrating from $0$ to $t$:

$$
\log S_t - \log S_0 = \left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t
$$

**Solution:**

$$
\boxed{
S_t = S_0 \exp\left[\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t\right]
}
$$

### 3. Properties


**Distribution:** $\log S_t$ is normally distributed:

$$
\log S_t \sim \mathcal{N}\left(\log S_0 + \left(\mu - \frac{\sigma^2}{2}\right)t, \sigma^2 t\right)
$$

Therefore, $S_t$ has a **log-normal distribution**.

**Moments:**

$$
\mathbb{E}[S_t] = S_0 e^{\mu t}
$$

**Derivation:**

$$
\begin{align}
\mathbb{E}[S_t] &= S_0 \mathbb{E}\left[\exp\left(\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t\right)\right] \\
&= S_0 e^{(\mu - \sigma^2/2)t} \mathbb{E}\left[e^{\sigma W_t}\right] \\
&= S_0 e^{(\mu - \sigma^2/2)t} \cdot e^{\sigma^2 t/2} \\
&= S_0 e^{\mu t}
\end{align}
$$

where we used $\mathbb{E}[e^{aX}] = e^{a^2/2}$ for $X \sim \mathcal{N}(0,1)$ and $W_t \sim \mathcal{N}(0,t)$.

**Variance:**

$$
\text{Var}[S_t] = S_0^2 e^{2\mu t}(e^{\sigma^2 t} - 1)
$$

**Derivation:**

$$
\begin{align}
\mathbb{E}[S_t^2] &= S_0^2 \mathbb{E}\left[\exp\left(2\left(\mu - \frac{\sigma^2}{2}\right)t + 2\sigma W_t\right)\right] \\
&= S_0^2 e^{(2\mu - \sigma^2)t} \mathbb{E}[e^{2\sigma W_t}] \\
&= S_0^2 e^{(2\mu - \sigma^2)t} \cdot e^{2\sigma^2 t} \\
&= S_0^2 e^{2\mu t + \sigma^2 t}
\end{align}
$$

Therefore:

$$
\text{Var}[S_t] = \mathbb{E}[S_t^2] - (\mathbb{E}[S_t])^2 = S_0^2 e^{2\mu t}(e^{\sigma^2 t} - 1)
$$

### 4. Financial Interpretation


- GBM is the foundation of the **Black-Scholes model**
- Assumes **constant volatility** and **log-normal returns**
- **Self-financing property:** Relative changes $dS_t/S_t$ are independent of the level
- Returns over non-overlapping intervals are independent (Markov property)

### 5. Limitations


- Cannot model **mean reversion** (e.g., interest rates, volatility)
- Cannot guarantee **positivity constraints** for all processes
- Constant volatility is unrealistic for many assets

---

## Ornstein-Uhlenbeck (OU) Process


### 1. The Model


**SDE:**

$$
\boxed{
dX_t = \kappa(\theta - X_t)\,dt + \sigma\,dW_t
}
$$

where:
- $\kappa > 0$ = mean reversion speed
- $\theta$ = long-term mean (equilibrium level)
- $\sigma$ = volatility

### 2. Derivation of the Solution


This is a **linear SDE** that can be solved using an **integrating factor**.

Rewrite as:

$$
dX_t + \kappa X_t\,dt = \kappa\theta\,dt + \sigma\,dW_t
$$

Multiply both sides by the integrating factor $e^{\kappa t}$:

$$
e^{\kappa t}dX_t + \kappa e^{\kappa t} X_t\,dt = d(e^{\kappa t} X_t)
$$

Using Itô's lemma on $Y_t = e^{\kappa t} X_t$:

$$
dY_t = \kappa e^{\kappa t} X_t\,dt + e^{\kappa t}dX_t
$$

Substituting the SDE:

$$
\begin{align}
dY_t &= \kappa e^{\kappa t} X_t\,dt + e^{\kappa t}[\kappa(\theta - X_t)\,dt + \sigma\,dW_t] \\
&= \kappa e^{\kappa t}\theta\,dt + \sigma e^{\kappa t}\,dW_t
\end{align}
$$

Integrating from $0$ to $t$:

$$
Y_t - Y_0 = \kappa\theta \int_0^t e^{\kappa s}\,ds + \sigma \int_0^t e^{\kappa s}\,dW_s
$$

$$
e^{\kappa t}X_t - X_0 = \theta(e^{\kappa t} - 1) + \sigma \int_0^t e^{\kappa s}\,dW_s
$$

**Solution:**

$$
\boxed{
X_t = X_0 e^{-\kappa t} + \theta(1 - e^{-\kappa t}) + \sigma \int_0^t e^{-\kappa(t-s)}\,dW_s
}
$$

Alternatively:

$$
X_t = e^{-\kappa t}X_0 + \theta(1 - e^{-\kappa t}) + \sigma e^{-\kappa t}\int_0^t e^{\kappa s}\,dW_s
$$

### 3. Properties


**Conditional Mean:**

$$
\mathbb{E}[X_t | X_0] = X_0 e^{-\kappa t} + \theta(1 - e^{-\kappa t})
$$

As $t \to \infty$: $\mathbb{E}[X_t | X_0] \to \theta$ (mean reversion).

**Conditional Variance:**

The stochastic integral has variance:

$$
\text{Var}\left[\int_0^t e^{-\kappa(t-s)}\,dW_s\right] = \int_0^t e^{-2\kappa(t-s)}\,ds = \frac{1 - e^{-2\kappa t}}{2\kappa}
$$

Therefore:

$$
\text{Var}[X_t | X_0] = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})
$$

As $t \to \infty$: $\text{Var}[X_t | X_0] \to \frac{\sigma^2}{2\kappa}$ (stationary variance).

**Stationary Distribution:**

When $t \to \infty$, $X_t$ converges in distribution to:

$$
X_\infty \sim \mathcal{N}\left(\theta, \frac{\sigma^2}{2\kappa}\right)
$$

**Covariance Function:**

For $s < t$:

$$
\text{Cov}[X_s, X_t] = \frac{\sigma^2}{2\kappa}e^{-\kappa(t-s)}(1 - e^{-2\kappa s})
$$

In the stationary regime ($s, t$ large):

$$
\text{Cov}[X_s, X_t] \approx \frac{\sigma^2}{2\kappa}e^{-\kappa|t-s|}
$$

This is an **exponentially decaying autocorrelation**.

### 4. Financial Applications


- **Interest rate models** (e.g., Vasicek model)
- **Pairs trading** (spread between two assets)
- **Commodity prices** with storage
- **Volatility models** (not directly, but as a component)

---

## Vasicek Model (Interest Rates)


### 1. The Model


**SDE:**

$$
\boxed{
dr_t = a(b - r_t)\,dt + \sigma\,dW_t
}
$$

This is structurally identical to the OU process with $\kappa = a$ and $\theta = b$.

### 2. Solution


$$
r_t = r_0 e^{-at} + b(1 - e^{-at}) + \sigma \int_0^t e^{-a(t-s)}\,dW_s
$$

### 3. Bond Pricing


The price at time $t$ of a zero-coupon bond maturing at $T$ is:

$$
P(t, T) = \mathbb{E}^{\mathbb{Q}}\left[\exp\left(-\int_t^T r_s\,ds\right) \Big| \mathcal{F}_t\right]
$$

For the Vasicek model, this can be computed explicitly:

$$
P(t, T) = A(t, T)e^{-B(t, T)r_t}
$$

where:

$$
B(t, T) = \frac{1 - e^{-a(T-t)}}{a}
$$

$$
A(t, T) = \exp\left[\left(b - \frac{\sigma^2}{2a^2}\right)(B(t, T) - (T-t)) - \frac{\sigma^2}{4a}B(t, T)^2\right]
$$

### 4. Advantages and Disadvantages


**Advantages:**
- Analytically tractable
- Mean-reverting (realistic for rates)
- Closed-form bond prices

**Disadvantages:**
- Interest rates can become **negative** (since $r_t$ is Gaussian)
- Constant volatility regardless of rate level

---

## Cox-Ingersoll-Ross (CIR) Model


### 1. The Model


**SDE:**

$$
\boxed{
dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t
}
$$

where:
- $\kappa > 0$ = speed of mean reversion
- $\theta > 0$ = long-term mean
- $\sigma > 0$ = volatility parameter
- $r_t \geq 0$ (interest rate remains non-negative)

### 2. Non-negativity: Feller Condition


**Theorem (Feller Condition):** If $2\kappa\theta \geq \sigma^2$, then $r_t > 0$ for all $t > 0$ almost surely.

If $2\kappa\theta < \sigma^2$, $r_t$ can reach $0$, but it is a reflecting boundary.

### 3. Transformation to Bessel Process


Let $X_t = \sqrt{r_t}$. Apply Itô's lemma:

$$
\frac{\partial f}{\partial r} = \frac{1}{2\sqrt{r}}, \quad \frac{\partial^2 f}{\partial r^2} = -\frac{1}{4r^{3/2}}
$$

$$
\begin{align}
dX_t &= \frac{1}{2\sqrt{r_t}}dr_t - \frac{1}{4r_t^{3/2}} \cdot \sigma^2 r_t\,dt \\
&= \frac{1}{2\sqrt{r_t}}[\kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t] - \frac{\sigma^2}{4\sqrt{r_t}}\,dt \\
&= \left[\frac{\kappa(\theta - r_t)}{2\sqrt{r_t}} - \frac{\sigma^2}{4\sqrt{r_t}}\right]dt + \frac{\sigma}{2}\,dW_t \\
&= \left[\frac{\kappa\theta - \sigma^2/4}{2X_t} - \frac{\kappa}{2}X_t\right]dt + \frac{\sigma}{2}\,dW_t
\end{align}
$$

This is related to the **squared Bessel process**.

### 4. Distribution


The CIR process does not have a simple closed-form solution like GBM or Vasicek. However, the **conditional distribution** is known:

$$
r_t | r_0 \sim \frac{\sigma^2(1 - e^{-\kappa t})}{4\kappa} \chi_{\nu}^2\left(\frac{4\kappa e^{-\kappa t}}{\sigma^2(1 - e^{-\kappa t})}r_0\right)
$$

where $\chi_{\nu}^2(\lambda)$ is a **non-central chi-squared distribution** with:
- Degrees of freedom: $\nu = \frac{4\kappa\theta}{\sigma^2}$
- Non-centrality parameter: $\lambda = \frac{4\kappa e^{-\kappa t}}{\sigma^2(1 - e^{-\kappa t})}r_0$

### 5. Moments


**Conditional Mean:**

$$
\mathbb{E}[r_t | r_0] = r_0 e^{-\kappa t} + \theta(1 - e^{-\kappa t})
$$

(same as Vasicek)

**Conditional Variance:**

$$
\text{Var}[r_t | r_0] = r_0 \frac{\sigma^2}{\kappa}(e^{-\kappa t} - e^{-2\kappa t}) + \theta\frac{\sigma^2}{2\kappa}(1 - e^{-\kappa t})^2
$$

### 6. Bond Pricing


Zero-coupon bond price:

$$
P(t, T) = A(t, T)e^{-B(t, T)r_t}
$$

where:

$$
B(t, T) = \frac{2(e^{\gamma(T-t)} - 1)}{(\gamma + \kappa)(e^{\gamma(T-t)} - 1) + 2\gamma}
$$

$$
A(t, T) = \left[\frac{2\gamma e^{(\kappa + \gamma)(T-t)/2}}{(\gamma + \kappa)(e^{\gamma(T-t)} - 1) + 2\gamma}\right]^{2\kappa\theta/\sigma^2}
$$

with $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$.

### 7. Advantages over Vasicek


- **Non-negative interest rates** (more realistic)
- **State-dependent volatility**: higher rates → higher volatility
- Still analytically tractable for bond pricing

---

## Constant Elasticity of Variance (CEV) Model


### 1. The Model


**SDE:**

$$
\boxed{
dS_t = \mu S_t\,dt + \sigma S_t^\beta\,dW_t
}
$$

where $\beta \in \mathbb{R}$ is the **elasticity parameter**.

### 2. Special Cases


- $\beta = 1$: **Geometric Brownian Motion** (Black-Scholes)
- $\beta = 0$: **Bachelier model** (arithmetic Brownian motion)
- $\beta = 1/2$: **Square-root process** (volatility decreases with price)

### 3. Properties


For $\beta < 1$, the model exhibits **leverage effect**: volatility increases as price decreases.

For $\beta = 1/2$:

$$
dS_t = \mu S_t\,dt + \sigma \sqrt{S_t}\,dW_t
$$

This is similar to the CIR process and can reach zero but is reflecting.

### 4. Implied Volatility Smile


The CEV model can produce an **implied volatility skew**, making it more realistic than GBM for equity options.

---

## Heston Stochastic Volatility Model


### 1. The Model


**System of SDEs:**

$$
\boxed{
\begin{cases}
dS_t = \mu S_t\,dt + \sqrt{V_t} S_t\,dW_t^1 \\
dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^2
\end{cases}
}
$$

with correlation:

$$
d\langle W^1, W^2 \rangle_t = \rho\,dt, \quad \rho \in [-1, 1]
$$

where:
- $S_t$ = asset price
- $V_t$ = instantaneous variance
- $\kappa$ = mean reversion speed of variance
- $\theta$ = long-term variance
- $\xi$ = volatility of volatility (vol-of-vol)
- $\rho$ = correlation between price and volatility shocks

### 2. Implementation of Correlation


In practice, we write:

$$
dW_t^2 = \rho\,dW_t^1 + \sqrt{1 - \rho^2}\,dZ_t
$$

where $Z_t$ is a Brownian motion independent of $W_t^1$.

The system becomes:

$$
\begin{cases}
dS_t = \mu S_t\,dt + \sqrt{V_t} S_t\,dW_t^1 \\
dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}(\rho\,dW_t^1 + \sqrt{1-\rho^2}\,dZ_t)
\end{cases}
$$

### 3. Feller Condition


To ensure $V_t > 0$ for all $t$:

$$
2\kappa\theta \geq \xi^2
$$

### 4. Advantages


- **Stochastic volatility** captures volatility clustering
- **Correlation $\rho < 0$** produces **leverage effect** (volatility increases when price drops)
- **Semi-analytical option pricing** via characteristic functions
- Can fit the **volatility surface** better than Black-Scholes

### 5. Characteristic Function


The Heston model has a **semi-closed-form characteristic function**, which enables efficient option pricing via Fourier inversion.

For $u \in \mathbb{C}$:

$$
\phi(u; t, S_t, V_t) = \mathbb{E}\left[e^{iu \log S_T} \Big| S_t, V_t\right]
$$

This can be computed in closed form using the solution to a system of Riccati ODEs.

---

## Merton Jump-Diffusion Model


### 1. The Model


**SDE with jumps:**

$$
\boxed{
\frac{dS_t}{S_{t-}} = \mu\,dt + \sigma\,dW_t + dJ_t
}
$$

where $J_t$ is a **compound Poisson process**:

$$
J_t = \sum_{i=1}^{N_t} (Y_i - 1)
$$

with:
- $N_t$ = Poisson process with intensity $\lambda$
- $Y_i$ = i.i.d. jump sizes with $\log Y_i \sim \mathcal{N}(\mu_J, \sigma_J^2)$

### 2. Interpretation


- Between jumps, $S_t$ follows GBM
- At random times (Poisson arrivals), the price **jumps** by a random percentage
- Models **rare events** (crashes, earnings announcements)

### 3. Compensated Jump Process


To make $S_t$ a martingale under $\mathbb{Q}$, we use:

$$
dS_t = (r - \lambda k)\,S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}} + S_{t-}\,dJ_t
$$

where $k = \mathbb{E}[Y - 1]$ is the expected jump size.

---

## SABR Model


### 1. The Model


Used extensively for **interest rate derivatives** and **FX options**:

$$
\boxed{
\begin{cases}
dF_t = \sigma_t F_t^\beta\,dW_t^1 \\
d\sigma_t = \alpha \sigma_t\,dW_t^2
\end{cases}
}
$$

with $d\langle W^1, W^2 \rangle_t = \rho\,dt$.

where:
- $F_t$ = forward rate
- $\sigma_t$ = stochastic volatility
- $\beta \in [0, 1]$ = elasticity (often 0, 0.5, or 1)
- $\alpha$ = volatility of volatility
- $\rho$ = correlation

### 2. SABR Implied Volatility Formula


The SABR model has an **approximate closed-form formula** for implied volatility, making it highly practical for calibration to market data.

---

## Hull-White Model (Extended Vasicek)


### 1. The Model


**Time-dependent parameters:**

$$
\boxed{
dr_t = [\theta(t) - a(t)r_t]\,dt + \sigma(t)\,dW_t
}
$$

This extends Vasicek to allow **calibration to the current yield curve**.

### 2. Solution


$$
r_t = r_0 e^{-\int_0^t a(s)\,ds} + \int_0^t \theta(s) e^{-\int_s^t a(u)\,du}\,ds + \int_0^t \sigma(s) e^{-\int_s^t a(u)\,du}\,dW_s
$$

### 3. Calibration


By choosing $\theta(t)$ appropriately, the model can **perfectly fit the initial term structure**.

---

## Black-Karasinski Model


### 1. The Model


**Log-normal short rate:**

$$
d\log r_t = [\theta(t) - a(t)\log r_t]\,dt + \sigma(t)\,dW_t
$$

This ensures $r_t > 0$ for all $t$.

### 2. Properties


- **Non-negative rates** (advantage over Vasicek and Hull-White)
- **No closed-form bond prices** (requires numerical methods)
- Popular for **Bermudan swaptions** and other complex rate derivatives

---

## Summary Table


| Model | SDE | Key Feature | Application |
|-------|-----|-------------|-------------|
| **GBM** | $dS_t = \mu S_t dt + \sigma S_t dW_t$ | Exponential growth | Stocks (Black-Scholes) |
| **OU** | $dX_t = \kappa(\theta - X_t)dt + \sigma dW_t$ | Mean reversion | Spreads, rates |
| **Vasicek** | $dr_t = a(b - r_t)dt + \sigma dW_t$ | Gaussian rates | Simple rate model |
| **CIR** | $dr_t = \kappa(\theta - r_t)dt + \sigma\sqrt{r_t} dW_t$ | Non-negative rates | Interest rates |
| **CEV** | $dS_t = \mu S_t dt + \sigma S_t^\beta dW_t$ | Leverage effect | Equity options |
| **Heston** | $dS_t = \mu S_t dt + \sqrt{V_t}S_t dW_t^1$<br>$dV_t = \kappa(\theta - V_t)dt + \xi\sqrt{V_t}dW_t^2$ | Stochastic vol | Vol surface fitting |
| **Merton** | $dS_t/S_{t-} = \mu dt + \sigma dW_t + dJ_t$ | Jump diffusion | Crash risk |
| **SABR** | $dF_t = \sigma_t F_t^\beta dW_t^1$<br>$d\sigma_t = \alpha\sigma_t dW_t^2$ | Stochastic vol (rates) | Interest rate options |
| **Hull-White** | $dr_t = [\theta(t) - ar_t]dt + \sigma dW_t$ | Yield curve fitting | Interest rate derivatives |

---

## Choosing the Right Model


**Considerations:**

1. **Asset class**: Equities favor GBM/Heston, rates favor CIR/Hull-White
2. **Analytical tractability**: Need closed forms? Use GBM, Vasicek, CIR
3. **Calibration**: Need to fit market? Use Heston, SABR, Hull-White
4. **Non-negativity**: Rates should use CIR, Black-Karasinski
5. **Jumps**: Expect rare events? Use Merton, Kou models
6. **Computational budget**: Complex models require Monte Carlo

Each model represents a trade-off between **realism**, **tractability**, and **computational cost**.
