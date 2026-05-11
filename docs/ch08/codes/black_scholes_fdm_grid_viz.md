# Finite Difference Grid

## Background

Black Scholes Fdm Grid Viz

Educational script demonstrating black scholes fdm grid viz concepts.

---

## Code

```python
"""
Black Scholes Fdm Grid Viz

Educational script demonstrating black scholes fdm grid viz concepts.
"""

# ============================================================================
# black_scholes_FINITE_DIFFERENCE_GRID_VISUALIZATION.py
# ============================================================================
import black_scholes as bs
    
# Model parameters


if __name__ == "__main__":
    S0 = 100      # Current stock price
    K = 105       # Strike price
    T = 0.25      # 3 months to expiration
    r = 0.05      # 5% risk-free rate
    sigma = 0.2   # 20% volatility
    q = 0.02      # 2% dividend yield
    mu = 0.1
    
    bs.BlackScholes(S0=S0, K=K, T=T, r=r, sigma=sigma, q=q).plot_finite_difference_grid(M=8, N=6)
```


## Exercises

**Exercise 1.**
For an FDM grid with $M = 8$ spatial points and $N = 6$ time steps on $[0, 300] \times [0, 0.25]$, compute the grid spacings $\Delta S$ and $\Delta t$, and the total number of grid points.

??? success "Solution to Exercise 1"
    $\Delta S = 300 / 8 = 37.5$, $\Delta t = 0.25 / 6 \approx 0.04167$. Total grid points: $(M + 1) \times (N + 1) = 9 \times 7 = 63$. Each point $(S_i, t_j)$ stores $V(S_i, t_j)$ where $S_i = i \cdot \Delta S$ and $t_j = j \cdot \Delta t$.

---

**Exercise 2.**
Explain the role of interior, boundary, and terminal grid points in the finite difference scheme. Which are determined by conditions and which by the PDE?

??? success "Solution to Exercise 2"
    Terminal points at $t = T$ are set by the payoff: $V(S_i, T) = \max(S_i - K, 0)$ for calls. Boundary points at $S = 0$ and $S = S_{\max}$ are set by boundary conditions from option behavior at extreme prices. Interior points are computed by the finite difference approximation to the Black-Scholes PDE via backward induction from $t = T$ to $t = 0$.

---

**Exercise 3.**
Check the CFL condition for the explicit scheme with $M = 8$, $\sigma = 0.2$, $S_{\max} = 300$, and $\Delta t = 0.04167$.

??? success "Solution to Exercise 3"
    The CFL bound is $(\Delta S)^2 / (\sigma^2 S_{\max}^2) = 37.5^2 / (0.04 \times 90000) = 1406.25 / 3600 \approx 0.3906$. Since $\Delta t = 0.04167 < 0.3906$, the condition is satisfied. The coarse grid ($M = 8$) makes stability easy; finer grids require proportionally smaller $\Delta t$.

---

**Exercise 4.**
Propose a non-uniform spatial mesh using $S(\xi) = K + \alpha \sinh(\beta(\xi - \xi_0))$ that concentrates grid points near the strike $K = 105$. Explain the parameters $\alpha$ and $\beta$.

??? success "Solution to Exercise 4"
    With $\alpha = K/5 = 21$ and $\beta = 5$, the sinh function grows slowly near $\xi = \xi_0$ (concentrating points near $S = K$) and rapidly in the tails. The parameter $\xi_0$ is chosen so $S(0) = 0$: $\xi_0 = \frac{1}{\beta} \operatorname{arcsinh}(-K/\alpha)$. The concentration factor $\beta$ controls the density of points near the strike---larger $\beta$ means more clustering. The finite difference stencils must use non-uniform spacing $\Delta S_i = S_{i+1} - S_i$.