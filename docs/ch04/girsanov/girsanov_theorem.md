# Girsanov's Theorem


Girsanov's theorem is one of the most powerful tools in mathematical finance. It describes how a change of probability measure modifies the drift of a stochastic process while preserving its Brownian structure. This is essential for pricing derivatives via risk-neutral measures.

---

## Setting and Assumptions

Let $(\Omega, \mathcal{F}, \{\mathcal{F}_t\}, \mathbb{P})$ be a filtered probability space supporting a standard Brownian motion $W_t$.

Let $\theta_t$ be an **adapted process** (the **Girsanov kernel**) satisfying the **Novikov condition**:

$$
\mathbb{E}^{\mathbb{P}}\!\left[
\exp\!\left(\frac{1}{2} \int_0^T \theta_s^2 \,ds\right)
\right] < \infty
$$

This condition ensures that the exponential martingale does not explode and is a true martingale (not just a local martingale).

---

## The Exponential Martingale

Define the **Radon-Nikodym derivative** (also called the **exponential martingale**):

$$
\boxed{
Z_t = \exp\!\left(
-\int_0^t \theta_s\, dW_s
-\frac{1}{2} \int_0^t \theta_s^2 \,ds
\right)
}
$$

**Key properties:**

1. **Strictly positive:** $Z_t > 0$ almost surely for all $t$
2. **Martingale:** Under the original measure $\mathbb{P}$, $Z_t$ is a true martingale
3. **Unit expectation:** $\mathbb{E}^{\mathbb{P}}[Z_t] = 1$ for all $t$

**Why the form?** The specific structure $-\int \theta\,dW_s - \frac{1}{2}\int \theta^2 ds$ arises from Itô's lemma applied to exponential functions, ensuring the martingale property.

---

## The Measure Change

Define a new probability measure $\mathbb{Q}$ on $\mathcal{F}_T$ via:

$$
\boxed{
\frac{d\mathbb{Q}}{d\mathbb{P}}\Big|_{\mathcal{F}_T} = Z_T
}
$$

For any random variable $X$, the relationship between expectations under the two measures is:

$$
\mathbb{E}^{\mathbb{Q}}[X] = \mathbb{E}^{\mathbb{P}}[X \cdot Z_T]
$$

For events in the σ-algebra $\mathcal{F}_t$ (where $t \leq T$), since $Z_t$ is a martingale:

$$
\mathbb{Q}(A) = \mathbb{E}^{\mathbb{P}}[Z_T \cdot \mathbf{1}_A] = \mathbb{E}^{\mathbb{P}}[Z_t \cdot \mathbf{1}_A], \quad A \in \mathcal{F}_t
$$

---

## Statement of Girsanov's Theorem

**Theorem (Girsanov, 1960):** Under the new measure $\mathbb{Q}$, the process

$$
\boxed{
\widetilde{W}_t := W_t + \int_0^t \theta_s \,ds
}
$$

is a **standard Brownian motion**.

**Equivalently:** The original Brownian motion $W_t$ can be written as

$$
W_t = \widetilde{W}_t - \int_0^t \theta_s\,ds
$$

under $\mathbb{Q}$.

---

## Interpretation: The Drift Removal Mechanism

| Perspective | Under $\mathbb{P}$ (Original Measure) | Under $\mathbb{Q}$ (New Measure) |
|-------------|--------------------------------------|--------------------------------|
| Brownian motion | $W_t$ is standard | $\widetilde{W}_t$ is standard |
| Transformed BM | $\widetilde{W}_t = W_t + \int \theta\,ds$ has drift | Driftless |
| What changed | Original measure | Probability measure and interpretation |
| Information structure | Same filtration | Same filtration |
| Volatility | Unchanged | Unchanged |

**Key insight:** The theorem shows that drift can be removed by reweighting paths via a change of measure. The drift is not a fundamental property of the process—it's an artifact of how we assign probabilities to outcomes.

<figure markdown="span">
  ![Girsanov measure change visualization](./image/girsanov_theorem_demo.png){ width="100%" }
  <figcaption>
    <strong>Figure 1 — Girsanov's theorem visualized on 60 simulated paths
    (μ = −1.5, σ = 1, T = 1).</strong>
    <em>Top-left:</em> Paths under the physical measure ℙ with equal weights; the sample mean
    (amber dashed) tracks the theoretical drift μt.
    <em>Top-center:</em> The same paths reweighted by the Radon-Nikodym derivative
    Z<sub>T</sub> = exp(−θW<sub>T</sub> − ½θ²T) — bright green = high weight,
    dark red ≈ zero weight, making the measure change explicit.
    <em>Top-right:</em> Sorted bar chart of relative Z<sub>T</sub> weights; the amber dashed
    line marks equal weight (Z̄ = 1), confirming 𝔼<sup>ℙ</sup>[Z<sub>T</sub>] ≈ 1 (Novikov condition).
    <em>Bottom-left/center:</em> Running means under ℙ (drifts at rate μ) vs. the
    Z<sub>T</sub>-weighted mean under ℚ (collapses to zero), confirming drift removal.
    <em>Bottom-right:</em> Histogram of Z<sub>T</sub> values — right-skewed lognormal distribution
    centred near 1, consistent with the martingale property.
  </figcaption>
</figure>

---

## Connection to SDEs: Removing Drift

**Original SDE under $\mathbb{P}$:**

$$
dX_t = \mu(t)\,dt + \sigma(t)\,dW_t
$$

where $\mu(t)$ is the drift.

**Choose Girsanov kernel:** $\theta_t = \frac{\mu(t)}{\sigma(t)}$ (assuming $\sigma(t) \neq 0$)

**Under $\mathbb{Q}$:** Since $W_t = \widetilde{W}_t - \int_0^t \theta_s\,ds$:

$$
dX_t = \mu(t)\,dt + \sigma(t)\left(d\widetilde{W}_t - \theta_t\,dt\right)
$$

$$
= \mu(t)\,dt + \sigma(t)\,d\widetilde{W}_t - \sigma(t)\theta_t\,dt
$$

$$
= \left(\mu(t) - \sigma(t)\theta_t\right)dt + \sigma(t)\,d\widetilde{W}_t
$$

$$
= 0\,dt + \sigma(t)\,d\widetilde{W}_t
$$

$$
= \sigma(t)\,d\widetilde{W}_t
$$

**Result:** The drift has been completely removed under $\mathbb{Q}$!

---

## Financial Application: Risk-Neutral Pricing

**Problem:** Price a derivative given the stock price dynamics under the physical measure $\mathbb{P}$:

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t
$$

The risk $\mu$ and risk-free rate $r$ are different, so this is not a martingale.

**Solution via Girsanov:**

1. **Choose Girsanov kernel:** $\theta = \frac{\mu - r}{\sigma}$ (market price of risk)

2. **Define numeraire-relative measure $\mathbb{Q}$:** Use $Z_T = \exp\left(-\int_0^T \theta\,dW_s - \frac{1}{2}\int_0^T \theta^2\,ds\right)$

3. **Under $\mathbb{Q}$:** The discounted stock price becomes a martingale:

$$
d(e^{-rt}S_t) = 0\,dt + e^{-rt}\sigma S_t\,d\widetilde{W}_t
$$

4. **Option price:** Risk-neutral expectation:

$$
C(t, S_t) = e^{-r(T-t)} \mathbb{E}^{\mathbb{Q}}[(S_T - K)^+ | \mathcal{F}_t]
$$

This is the foundation of the Black-Scholes pricing formula.

---

## Example 1: Drifted Brownian Motion

**Original process under $\mathbb{P}$:**

$$
dX_t = \mu\,dt + \sigma\,dW_t, \quad X_0 = 0
$$

where $\mu$ and $\sigma$ are constants.

**Choose Girsanov kernel:** $\theta = \frac{\mu}{\sigma}$ (constant)

**Check Novikov condition:**

$$
\mathbb{E}^{\mathbb{P}}\left[\exp\left(\frac{1}{2}\int_0^T \left(\frac{\mu}{\sigma}\right)^2 ds\right)\right] = \exp\left(\frac{\mu^2 T}{2\sigma^2}\right) < \infty \quad \checkmark
$$

**Exponential martingale:**

$$
Z_t = \exp\left(-\frac{\mu}{\sigma}W_t - \frac{\mu^2 t}{2\sigma^2}\right)
$$

**Under $\mathbb{Q}$ with $d\mathbb{Q}/d\mathbb{P} = Z_T$:**

$$
\widetilde{W}_t := W_t + \frac{\mu}{\sigma}t \text{ is a standard Brownian motion}
$$

**Therefore:** Substituting back into the original SDE:

$$
dX_t = \mu\,dt + \sigma\left(d\widetilde{W}_t - \frac{\mu}{\sigma}dt\right) = 0\,dt + \sigma\,d\widetilde{W}_t = \sigma\,d\widetilde{W}_t
$$

The drift has been **completely removed** under $\mathbb{Q}$!

**Under $\mathbb{Q}$:**

$$
X_t = \sigma\widetilde{W}_t \sim \mathcal{N}(0, \sigma^2 t)
$$

---

## Example 2: Geometric Brownian Motion (Stock Price)

**Original process under $\mathbb{P}$ (physical measure):**

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t
$$

where:
- $\mu$ = real-world drift (expected return)
- $\sigma$ = volatility
- $r$ = risk-free rate (assumed constant)

**Key observation:** The discounted stock price $e^{-rt}S_t$ is NOT a $\mathbb{P}$-martingale because:

$$
d(e^{-rt}S_t) = -re^{-rt}S_t\,dt + e^{-rt}dS_t
$$

$$
= -re^{-rt}S_t\,dt + e^{-rt}(\mu S_t\,dt + \sigma S_t\,dW_t)
$$

$$
= e^{-rt}S_t(\mu - r)\,dt + e^{-rt}\sigma S_t\,dW_t$$

The $dt$ coefficient is $(\mu - r)S_t e^{-rt} \neq 0$ (unless $\mu = r$), so this is not a martingale.

**Choose Girsanov kernel:** The market price of risk

$$
\theta = \frac{\mu - r}{\sigma}
$$

**Check Novikov condition:**

$$
\mathbb{E}^{\mathbb{P}}\left[\exp\left(\frac{1}{2}\int_0^T \left(\frac{\mu-r}{\sigma}\right)^2 ds\right)\right] = \exp\left(\frac{(\mu-r)^2 T}{2\sigma^2}\right) < \infty \quad \checkmark
$$

**Exponential martingale (Radon-Nikodym derivative):**

$$
Z_t = \exp\left(-\frac{\mu - r}{\sigma}W_t - \frac{(\mu-r)^2 t}{2\sigma^2}\right)
$$

**Under $\mathbb{Q}$ with $d\mathbb{Q}/d\mathbb{P} = Z_T$:**

$$
\widetilde{W}_t := W_t + \frac{\mu - r}{\sigma}t \text{ is a standard Brownian motion}
$$

**Transform the SDE:** Since $W_t = \widetilde{W}_t - \frac{\mu-r}{\sigma}t$:

$$
dS_t = \mu S_t\,dt + \sigma S_t\left(d\widetilde{W}_t - \frac{\mu-r}{\sigma}dt\right)
$$

$$
= \mu S_t\,dt + \sigma S_t\,d\widetilde{W}_t - (\mu - r)S_t\,dt
$$

$$
= rS_t\,dt + \sigma S_t\,d\widetilde{W}_t
$$

**Result under $\mathbb{Q}$ (risk-neutral measure):**

$$
dS_t = rS_t\,dt + \sigma S_t\,d\widetilde{W}_t
$$

Now the discounted stock price is a martingale:

$$
d(e^{-rt}S_t) = -re^{-rt}S_t\,dt + e^{-rt}dS_t
$$

$$
= -re^{-rt}S_t\,dt + e^{-rt}(rS_t\,dt + \sigma S_t\,d\widetilde{W}_t)
$$

$$
= e^{-rt}\sigma S_t\,d\widetilde{W}_t \quad \text{(martingale!)}
$$

**Option pricing:** A European call option with strike $K$ and maturity $T$ has price:

$$
C(t, S_t) = e^{-r(T-t)} \mathbb{E}^{\mathbb{Q}}[(S_T - K)^+ | \mathcal{F}_t]
$$

where the expectation is under the **risk-neutral measure** $\mathbb{Q}$.

**Key insight:** Under $\mathbb{Q}$:
- The expected return of the stock is $r$ (risk-free rate)
- Investors are indifferent to risk
- This is why derivative prices don't depend on $\mu$!

---

## Example 3: Vasicek Model (Interest Rates)

**Original process under $\mathbb{P}$:**

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t
$$

where:
- $\theta$ = long-run mean interest rate
- $\kappa$ = mean reversion speed
- $\sigma$ = volatility

**Typical market price of risk:** $\lambda$ (constant or time-dependent)

**Choose Girsanov kernel:** $\theta = \lambda$

**Under the risk-neutral measure $\mathbb{Q}$:**

Define $\widetilde{W}_t = W_t + \lambda t$

$$
dr_t = [\kappa(\theta - r_t) - \lambda\sigma]\,dt + \sigma\,d\widetilde{W}_t
$$

The effective "long-run mean" becomes:

$$
\theta^* = \theta - \frac{\lambda}{\kappa}
$$

**Financial interpretation:** The market price of interest rate risk ($\lambda$) shifts the equilibrium level of rates from $\theta$ to $\theta^*$. The real-world view ($\mathbb{P}$) and the pricing view ($\mathbb{Q}$) differ precisely by this market price.

---

## Why Girsanov Matters in Finance

Girsanov's theorem is indispensable because:

1. **Separation of expectations from pricing:** The real-world drift $\mu$ (what market participants believe will happen) differs from the risk-neutral drift $r$ (what the market prices in)

2. **Universal pricing formula:** All derivatives can be priced via risk-neutral expectations, regardless of investors' actual beliefs

3. **Model calibration:** We can fit models to market prices using $\mathbb{Q}$ measures, then extract market prices of risk to understand investor preferences

4. **Consistent pricing across assets:** Girsanov ensures that a single choice of numeraire and measure prices all derivatives consistently

5. **Computational advantage:** Working under $\mathbb{Q}$ often simplifies calculations because many prices become martingales

---

## Python: Simulating the Measure Change

The following script reproduces Figure 1. It simulates drifted Brownian motion paths under $\mathbb{P}$,
computes the Radon-Nikodym weights $Z_T$, and visualizes the measure change in six panels.

**Dependencies:** `numpy`, `matplotlib`

```python
"""
Girsanov's Theorem – Visualization
====================================
Simulates drifted BM paths under P, computes Radon-Nikodym weights Z_T,
and displays the measure change P → Q in six panels (reproduces Figure 1).
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.collections import LineCollection
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

# ── Parameters ────────────────────────────────────────────────────────────────
RNG      = np.random.default_rng(42)
N_PATHS  = 20        # number of simulated paths
N_STEPS  = 200       # discretisation steps
T        = 1.0       # terminal time
MU       = -1.5      # drift under P  (negative, as in the Wikipedia figure)
SIGMA    = 1.0       # diffusion coefficient
dt       = T / N_STEPS
t_grid   = np.linspace(0, T, N_STEPS + 1)

# ── Simulate paths under P: X_t = μt + σW_t ──────────────────────────────────
dW   = RNG.standard_normal((N_PATHS, N_STEPS)) * np.sqrt(dt)
W    = np.hstack([np.zeros((N_PATHS, 1)), np.cumsum(dW, axis=1)])
X_P  = MU * t_grid + SIGMA * W

# ── Girsanov kernel and Radon-Nikodym weights ─────────────────────────────────
# Choose θ = μ/σ so that the drift is completely removed under Q.
theta = MU / SIGMA                                      # = -1.5 here

# Z_T = exp(−θ W_T − ½ θ² T)   [constant θ → stochastic integral = θ·W_T]
Z_T   = np.exp(-theta * W[:, -1] - 0.5 * theta**2 * T)
Z_norm = Z_T / Z_T.mean()                              # relative weights (mean ≈ 1)

# ── Weighted mean under Q ─────────────────────────────────────────────────────
mean_P = X_P.mean(axis=0)
mean_Q = (X_P * Z_T[:, None]).sum(axis=0) / Z_T.sum()

# ── Figure layout ─────────────────────────────────────────────────────────────
DARK_BG  = "#0d0d0d"
PANEL_BG = "#141414"
AMBER_C  = "#f5a623"
BLUE_C   = "#4fb3d4"
GRID_C   = "#2a2a2a"

fig = plt.figure(figsize=(16, 10), facecolor=DARK_BG)
fig.suptitle(
    "Girsanov's Theorem  ·  Measure Change from  P  to  Q",
    fontsize=16, color="white", fontfamily="serif", y=0.98
)
gs = gridspec.GridSpec(2, 3, figure=fig,
                       hspace=0.42, wspace=0.35,
                       left=0.06, right=0.96, top=0.92, bottom=0.08)

ax_P    = fig.add_subplot(gs[0, 0])   # paths under P
ax_Q    = fig.add_subplot(gs[0, 1])   # reweighted paths (view under Q)
ax_wt   = fig.add_subplot(gs[0, 2])   # weight bar chart
ax_mean = fig.add_subplot(gs[1, :2])  # running mean P vs Q
ax_zd   = fig.add_subplot(gs[1, 2])   # Z_T histogram

for ax in [ax_P, ax_Q, ax_wt, ax_mean, ax_zd]:
    ax.set_facecolor(PANEL_BG)
    for spine in ax.spines.values():
        spine.set_color("#333")
    ax.tick_params(colors="#888", labelsize=8)
    ax.xaxis.label.set_color("#aaa")
    ax.yaxis.label.set_color("#aaa")
    ax.title.set_color("white")
    ax.grid(color=GRID_C, linewidth=0.4, linestyle="--")

# ── Helper: draw paths coloured by weight ────────────────────────────────────
def draw_paths(ax, paths, weights, title):
    cmap = plt.cm.RdYlGn
    norm = Normalize(vmin=0, vmax=weights.max())
    for i in range(N_PATHS):
        pts  = np.column_stack([t_grid, paths[i]])
        segs = np.stack([pts[:-1], pts[1:]], axis=1)
        lc   = LineCollection(segs,
                              colors=[cmap(norm(weights[i]))] * len(segs),
                              linewidths=0.8, alpha=0.85)
        ax.add_collection(lc)
    ax.set_xlim(0, T)
    ax.set_ylim(paths.min() - 0.1, paths.max() + 0.1)
    ax.set_title(title, fontsize=10, pad=6)
    ax.set_xlabel("time t", fontsize=8)
    sm = ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, fraction=0.04, pad=0.02)
    cbar.ax.tick_params(labelsize=7, colors="#888")
    cbar.set_label("Z_T weight", fontsize=7, color="#aaa")

# Panel 1 – Under P (equal weights)
draw_paths(ax_P, X_P, np.ones(N_PATHS), "Paths under P  (drift mu={})".format(MU))
ax_P.plot(t_grid, MU * t_grid, color=AMBER_C, lw=2, ls="--",
          label="E^P[X_t] = {}t".format(MU))
ax_P.legend(fontsize=7, loc="lower left", framealpha=0.3,
            labelcolor="white", facecolor=PANEL_BG)

# Panel 2 – Same paths reweighted by Z_T
draw_paths(ax_Q, X_P, Z_norm, "Same paths reweighted by Z_T  (view under Q)")
ax_Q.axhline(0, color=BLUE_C, lw=1.5, ls="--", label="E^Q[X_t] = 0")
ax_Q.legend(fontsize=7, loc="upper right", framealpha=0.3,
            labelcolor="white", facecolor=PANEL_BG)

# Panel 3 – Weight bar chart
sorted_idx  = np.argsort(Z_norm)
bar_colors  = plt.cm.RdYlGn(Normalize()(Z_norm[sorted_idx]))
ax_wt.bar(np.arange(N_PATHS), Z_norm[sorted_idx],
          color=bar_colors, width=0.9, edgecolor="none")
ax_wt.axhline(1.0, color=AMBER_C, lw=1, ls="--", label="Equal weight = 1")
ax_wt.set_title("Radon-Nikodym weights  Z_T / mean(Z_T)", fontsize=10)
ax_wt.set_xlabel("Path index (sorted)", fontsize=8)
ax_wt.set_ylabel("Relative weight", fontsize=8)
ax_wt.legend(fontsize=7, framealpha=0.3, labelcolor="white", facecolor=PANEL_BG)

# Panel 4 – Running mean comparison
ax_mean.plot(t_grid, MU * t_grid, color="#e8473f", lw=2, ls="--",
             label="Theoretical E^P[X_t] = {}t".format(MU))
ax_mean.plot(t_grid, mean_P, color="#e8473f", lw=1.5, alpha=0.7,
             label="Sample mean under P")
ax_mean.axhline(0, color=BLUE_C, lw=2, ls="--",
                label="Theoretical E^Q[X_t] = 0  (drift removed)")
ax_mean.plot(t_grid, mean_Q, color=BLUE_C, lw=1.5, alpha=0.7,
             label="Weighted mean under Q")
ax_mean.fill_between(t_grid,
                     np.percentile(X_P, 10, axis=0),
                     np.percentile(X_P, 90, axis=0),
                     color="#e8473f", alpha=0.08, label="10-90th pct (P)")
ax_mean.set_xlim(0, T)
ax_mean.set_title("Running mean: P-measure (drift mu) vs Q-measure (drift removed)", fontsize=10)
ax_mean.set_xlabel("time t", fontsize=9)
ax_mean.set_ylabel("X_t", fontsize=9)
ax_mean.legend(fontsize=7.5, loc="lower left", framealpha=0.3,
               labelcolor="white", facecolor=PANEL_BG, ncol=2)

# Annotation box
info = (
    "Girsanov kernel:  theta = mu/sigma = {:.2f}\n"
    "Z_T = exp(-theta*W_T - 0.5*theta^2*T)\n"
    "W_tilde = W_t + theta*t  is BM under Q"
).format(theta)
ax_mean.text(0.62, 0.97, info, transform=ax_mean.transAxes,
             fontsize=8, verticalalignment="top", color="#ccc",
             fontfamily="monospace",
             bbox=dict(boxstyle="round,pad=0.5", facecolor="#1e1e1e",
                       edgecolor="#444", alpha=0.9))

# Panel 5 – Z_T histogram
ax_zd.hist(Z_T, bins=20, color=BLUE_C, edgecolor=DARK_BG, alpha=0.85, density=True)
ax_zd.axvline(Z_T.mean(), color=AMBER_C, lw=1.5, ls="--",
              label="Mean Z_T = {:.3f}  (approx 1 by Novikov)".format(Z_T.mean()))
ax_zd.set_title("Distribution of Z_T  (Radon-Nikodym derivative)", fontsize=9)
ax_zd.set_xlabel("Z_T", fontsize=8)
ax_zd.set_ylabel("Density", fontsize=8)
ax_zd.legend(fontsize=7, framealpha=0.3, labelcolor="white", facecolor=PANEL_BG)

plt.savefig("./image/girsanov_theorem_demo.png", dpi=150,
            bbox_inches="tight", facecolor=DARK_BG)
plt.show()
```

!!! note "Running the script"
    Save the script as `girsanov_demo.py` alongside your docs folder and run:
    ```bash
    pip install numpy matplotlib
    python girsanov_demo.py
    ```
    The output is saved to `./image/girsanov_theorem_demo.png` (Figure 1 above).

---

## Exercises

**Exercise 1.**
Let $W_t$ be a standard Brownian motion under $\mathbb{P}$ and let $\theta = 0.5$ (constant). Write the explicit form of the Radon-Nikodym derivative $Z_T$ for $T = 1$, verify that the Novikov condition holds, and define the shifted Brownian motion $\widetilde{W}_t$ under $\mathbb{Q}$.

---

**Exercise 2.**
Consider an SDE $dX_t = 3\,dt + 2\,dW_t$ under $\mathbb{P}$, with $X_0 = 0$. Determine the Girsanov kernel $\theta$ that removes the drift entirely. Write the SDE for $X_t$ under the new measure $\mathbb{Q}$ and describe the distribution of $X_t$ under $\mathbb{Q}$.

---

**Exercise 3.**
In the geometric Brownian motion example, a stock has parameters $\mu = 0.12$, $\sigma = 0.25$, and $r = 0.04$. Compute the market price of risk $\theta$. Then write the discounted stock price dynamics $d(e^{-rt}S_t)$ under $\mathbb{Q}$ and verify that the $dt$ term vanishes.

---

**Exercise 4.**
In the Vasicek model under $\mathbb{P}$, $dr_t = 0.3(0.05 - r_t)\,dt + 0.02\,dW_t$ with market price of interest rate risk $\lambda = 0.2$. Compute the risk-neutral long-run mean $\theta^*$. Explain why $\theta^* < \theta$ when $\lambda > 0$ and interpret this economically.

---

**Exercise 5.**
Girsanov's theorem states that $\widetilde{W}_t = W_t + \int_0^t \theta_s\,ds$ is a Brownian motion under $\mathbb{Q}$. Show that for any two times $0 \leq s < t$, the increment $\widetilde{W}_t - \widetilde{W}_s$ has mean zero and variance $t - s$ under $\mathbb{Q}$.

---

**Exercise 6.**
Consider a two-dimensional Brownian motion $(W_t^1, W_t^2)$ and a Girsanov kernel $\boldsymbol{\theta} = (\theta_1, \theta_2)$. Write the vector form of the Radon-Nikodym derivative $Z_T$ and state the multivariate Novikov condition. Define the shifted Brownian motions $\widetilde{W}_t^1$ and $\widetilde{W}_t^2$ under $\mathbb{Q}$ and verify they are independent.

---

**Exercise 7.**
A derivative has payoff $\Phi(S_T) = S_T^2$ and the stock follows GBM with $\mu = 0.10$, $\sigma = 0.20$, $r = 0.03$, $T = 1$. Using the risk-neutral dynamics $dS_t = rS_t\,dt + \sigma S_t\,d\widetilde{W}_t$, compute $\mathbb{E}^{\mathbb{Q}}[S_T^2]$ and hence the price $V_0 = e^{-rT}\mathbb{E}^{\mathbb{Q}}[S_T^2]$. (Hint: find the distribution of $\ln S_T$ under $\mathbb{Q}$ and use the lognormal moment formula.)
