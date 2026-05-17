# Free vs Bounded Domains

The qualitative behavior of a Green's function depends on whether the domain is **free** (all of $\mathbb{R}$) or **bounded** with explicit boundary conditions. On free domains, heat diffuses to infinity and mass spreads without loss. On bounded domains, heat either leaks out through absorbing boundaries or bounces back off reflecting ones, producing a much richer structure. In finance this is exactly the distinction between vanilla options (free domain) and barrier options (bounded domain).

This page is the **geometry lens** on Green's functions; the operator/PDE lens is in [Green's Function for Parabolic PDEs](greens_function_parabolic.md), the probability lens in [Transition Density as Green's Function](transition_density_as_greens_function.md), and the eigenstructure lens in [Spectral Decomposition](spectral_decomposition.md).

---

## Free-Space Green's Function

Recall (see [§ Green's Function for Parabolic PDEs](greens_function_parabolic.md) and [§ Transition Density as Green's Function](transition_density_as_greens_function.md)): for $\partial_t u = \tfrac12\partial_{xx} u$ on $\mathbb{R}$, the Green's function (i.e., transition density) is the **Gaussian heat kernel**

$$
G_{\text{free}}(t,x;s,y) = \frac{1}{\sqrt{2\pi(t-s)}}\exp\!\left(-\frac{(x-y)^2}{2(t-s)}\right).
$$

Three features matter for the comparison below:

- **Mass conservation**: $\int_{\mathbb{R}} G_{\text{free}}\,dx = 1$ for all $t > s$.
- **Pointwise dispersion**: $G_{\text{free}} \to 0$ everywhere as $t \to \infty$.
- **Continuous spectrum**: no discrete eigenvalues; the Fourier transform provides the analog of spectral expansion.

Financially, this is the setting of standard Black-Scholes pricing with no barriers.

---

## Dirichlet Boundaries: Absorption

On $[0,L]$ with **absorbing** conditions $u(t,0) = u(t,L) = 0$, the Green's function must vanish at both endpoints. There are two complementary constructions.

### Method of Images

Place image sources outside the domain so their contributions cancel on the boundary. For a single absorbing wall at $x=0$ on the half-line,

$$
G_{\text{half}}(t,x;0,y) = G_{\text{free}}(t,x;0,y) - G_{\text{free}}(t,x;0,-y).
$$

The negative image at $-y$ kills $G$ at $x=0$ by symmetry. On $[0,L]$, enforcing both walls requires an infinite image lattice:

$$
G_{\text{Dir}}(t,x;0,y) = \sum_{k\in\mathbb{Z}}\bigl[G_{\text{free}}(t,x;0,y+2kL) - G_{\text{free}}(t,x;0,-y+2kL)\bigr].
$$

Each image pair enforces cancellation at $x=0$ and $x=L$ simultaneously. Images are the PDE translation of the **reflection principle** for Brownian motion: each reflected Gaussian accounts for paths that have crossed the barrier and should be removed (or cancelled) from the count.

### Spectral Representation

Recall (see [§ Spectral Decomposition](spectral_decomposition.md)): the same Green's function admits the sine expansion

$$
G_{\text{Dir}}(t,x;0,y) = \frac{2}{L}\sum_{n=1}^{\infty} e^{-n^2\pi^2 t/(2L^2)} \sin\!\left(\tfrac{n\pi x}{L}\right)\sin\!\left(\tfrac{n\pi y}{L}\right).
$$

The key facts for this lens are that the spectrum is **discrete** with $\lambda_n = n^2\pi^2/(2L^2)$, that mass leaks out ($\int_0^L G_{\text{Dir}}\,dx < 1$ and $\to 0$ as $t\to\infty$), and that the leakage rate is the principal eigenvalue $\lambda_1 = \pi^2/(2L^2)$.

### Images vs Spectral: the Time-Scale Trade-off

Both series represent the same object, but they converge at opposite ends of the time axis.

| Regime | Convergence | Why |
|---|---|---|
| Short time, $t \ll L^2$ | Images converge in 1-2 terms; spectral needs many | Process has not felt the far boundary yet; Gaussians from distant images have exponentially small overlap with the domain |
| Long time, $t \gg L^2$ | Spectral converges in 1-2 terms; images need many | High modes are suppressed by $e^{-\lambda_n t}$; the image lattice requires adding terms that all have comparable magnitude once diffusion has filled the domain |

The practical rule of thumb: **images for short time, spectral for long time**. Near the crossover $t \sim L^2/\pi^2$ either representation needs only a handful of terms. Numerical schemes for barrier options exploit this by switching representations based on time-to-maturity.

!!! tip "Short-time estimate"
    Using only the two-image approximation $G_{\text{free}}(t,x;0,y) - G_{\text{free}}(t,x;0,-y)$, one finds the survival probability $\mathbb{P}(\tau_0 > t \mid B_0 = y) = \operatorname{erf}(y/\sqrt{2t})$. For $y/\sqrt{t}$ large (the particle far from the wall in standard deviations), this is essentially $1$ and higher images are negligible.

---

## Neumann Boundaries: Reflection

On $[0,L]$ with **reflecting** conditions $u_x(t,0) = u_x(t,L) = 0$, the Neumann condition flips the sign convention: images are **positive** (same sign) so their derivatives cancel at the wall.

$$
G_{\text{Neu}}(t,x;0,y) = \sum_{k\in\mathbb{Z}}\bigl[G_{\text{free}}(t,x;0,y+2kL) + G_{\text{free}}(t,x;0,-y+2kL)\bigr].
$$

Recall (see [§ Spectral Decomposition](spectral_decomposition.md)): the spectral version contains a constant zero-eigenvalue mode plus cosines,

$$
G_{\text{Neu}}(t,x;0,y) = \frac{1}{L} + \frac{2}{L}\sum_{n=1}^{\infty} e^{-n^2\pi^2 t/(2L^2)}\cos\!\left(\tfrac{n\pi x}{L}\right)\cos\!\left(\tfrac{n\pi y}{L}\right).
$$

Mass is conserved: $\int_0^L G_{\text{Neu}}\,dx = 1$ for every $t$, and as $t\to\infty$ the density relaxes to the uniform $1/L$. Reflecting walls keep probability inside and drive it to equilibrium.

---

## Comparison

| Aspect | Free ($\mathbb{R}$) | Dirichlet ($[0,L]$) | Neumann ($[0,L]$) |
|---|---|---|---|
| Representation | Single Gaussian | Image series or sines | Image series or cosines |
| Spectrum | Continuous | Discrete, $\lambda_n > 0$ | Discrete, $\lambda_0 = 0$ |
| Mass | Conserved | Decays to 0 | Conserved |
| Long-time limit | Disperses to 0 | Absorbed to 0 at rate $\lambda_1$ | Uniform equilibrium |
| Finance analog | Vanilla option | Knock-out barrier | Reflecting band |

$$
\boxed{\text{Free: dispersion}\quad\text{Absorbing: decay}\quad\text{Reflecting: equilibrium}}
$$

---

## Financial Interpretation

**Vanilla options** live on the free domain. The log-price $X_t = \log S_t$ ranges over all of $\mathbb{R}$, and the free-space Green's function is the lognormal transition density that produces the Black-Scholes formula.

**Down-and-out barrier options** restrict $X$ to $(\log B, \infty)$ with Dirichlet condition at $\log B$. Using the single-barrier image construction,

$$
p_{\text{Dir}}(t,x;0,y) = G_{\text{free}}(t,x;0,y) - G_{\text{free}}(t,x;0,2\log B - y),
$$

so the barrier price is

$$
V_{\text{DO}}(t,S) = e^{-r(T-t)}\int_B^\infty g(S_T)\,p_{\text{Dir}}(T,\log S_T;t,\log S)\,\frac{dS_T}{S_T}.
$$

The subtracted reflected Gaussian removes paths that have crossed the barrier, so $V_{\text{DO}} < V_{\text{vanilla}}$.

**Double knock-outs** with barriers $B_l < B_u$ use the full Dirichlet Green's function on $[\log B_l,\log B_u]$. Short maturities are handled by a few image terms; long maturities by the first few spectral modes.

**Reflecting barriers** describe scenarios where prices cannot leave a band: FX target zones with central-bank intervention, rate floors/ceilings, or constrained wealth processes. Neumann boundaries relax to the uniform long-run distribution rather than being absorbed.

---

## Domain Truncation for Numerics

In practice the free domain $\mathbb{R}$ must be truncated to a finite grid. Three common strategies:

1. **Large box with asymptotic Dirichlet data** -- set $u$ to the known far-field behavior at $x_{\min}, x_{\max}$.
2. **Zero Dirichlet** -- conservative, slightly underprices but simple.
3. **Linear extrapolation** -- impose $\partial_{xx} u = 0$ at the cutoff.

!!! warning "Truncation error"
    The truncation error is $O(\exp(-(x_{\max}-x_0)^2/(2T)))$ -- exponentially small once the box extends several standard deviations beyond the payoff support. For Black-Scholes with $\sigma = 0.2$ and $T = 1$, taking $x_{\max} = x_0 + 5\sigma\sqrt{T}$ is generally sufficient.

---

## See Also

- [Green's Function for Parabolic PDEs](greens_function_parabolic.md)
- [Transition Density as Green's Function](transition_density_as_greens_function.md)
- [Spectral Decomposition](spectral_decomposition.md)

---

## Exercises

**Exercise 1.**
Starting from the free-space heat kernel $G_{\text{free}}(t,x;0,y) = (2\pi t)^{-1/2}\exp(-(x-y)^2/(2t))$, verify that $\int_{\mathbb{R}} G_{\text{free}}\,dx = 1$ for every $t > 0$.

??? success "Solution to Exercise 1"
    Substitute $z = (x-y)/\sqrt{t}$, so $dx = \sqrt{t}\,dz$ and

    $$
    \int_{\mathbb{R}} \frac{1}{\sqrt{2\pi t}} e^{-(x-y)^2/(2t)}\,dx = \int_{\mathbb{R}} \frac{1}{\sqrt{2\pi}} e^{-z^2/2}\,dz = 1.
    $$

    Total mass is independent of $t$: on the free domain, no probability leaks away even though the density flattens pointwise.

---

**Exercise 2.**
For a down-and-out barrier option on a log-price, the domain is $[B,\infty)$ with Dirichlet condition at $x=B$. Explain why placing a negative image at $y' = 2B - y$ enforces the boundary condition, and interpret the subtracted term probabilistically.

??? success "Solution to Exercise 2"
    The candidate is $G(t,x;0,y) = G_{\text{free}}(t,x;0,y) - G_{\text{free}}(t,x;0,2B-y)$. At $x=B$, $(B-y)^2 = (B-(2B-y))^2 = (y-B)^2$, so the two Gaussians are equal and $G(t,B;0,y) = 0$.

    Probabilistically, by the reflection principle for Brownian motion the density of paths that have ever touched $B$ and ended at some $x > B$ equals $G_{\text{free}}(t,x;0,2B-y)$. Subtracting this removes all barrier-crossing trajectories, leaving the density of paths that stay strictly above $B$ throughout $[0,t]$ -- the survival density relevant to a down-and-out option.

---

**Exercise 3.**
Compare images vs spectral expansions quantitatively on $[0,1]$ with Dirichlet conditions. Estimate how many terms each representation needs for $10^{-6}$ accuracy at (a) $t = 0.01$, (b) $t = 1$.

??? success "Solution to Exercise 3"
    **Spectral**: the $n$-th term decays as $e^{-n^2\pi^2 t/2}$. Setting this to $10^{-6}$ gives $n^2 > 2\log(10^6)/(\pi^2 t)$.

    - $t=1$: need $n^2 > 2.8$, so $n=2$ suffices. One or two modes is plenty.
    - $t=0.01$: need $n^2 > 280$, i.e. $n\geq 17$. Many modes required.

    **Images**: a Gaussian image at distance $d$ from the domain contributes $O(\exp(-d^2/(2t)))$. The $k$-th image pair sits at distance $\sim 2kL = 2k$, contributing $O(\exp(-2k^2/t))$.

    - $t=0.01$: $\exp(-2k^2/0.01) = \exp(-200 k^2)$; the $k=1$ term is already $\sim e^{-200}$, so one image pair is overkill.
    - $t=1$: $\exp(-2k^2)$; need $k^2 > 6.9$, so $k\geq 3$. Still manageable.

    The crossover sits near $t\sim L^2/\pi^2 \approx 0.1$. Images dominate for short time, spectral for long time -- the rule of thumb in the table above.

---

**Exercise 4.**
Explain, in both PDE and probabilistic language, why the Dirichlet Green's function loses mass while the Neumann one conserves it.

??? success "Solution to Exercise 4"
    **PDE view**: The total mass evolves as $\frac{d}{dt}\int_0^L u\,dx = \tfrac12\int_0^L u_{xx}\,dx = \tfrac12[u_x]_0^L$.

    - Dirichlet ($u = 0$ on the boundary) still has $u_x \neq 0$, and typically $u_x(L) < 0$, $u_x(0) > 0$, so $[u_x]_0^L < 0$ and mass leaks out.
    - Neumann ($u_x = 0$ on the boundary) makes the boundary term identically zero, so $\int u\,dx$ is conserved.

    **Probabilistic view**: the process is killed on contact with a Dirichlet boundary -- the surviving probability $\int G_{\text{Dir}}\,dx$ is the probability of not yet having been absorbed, which strictly decreases. A Neumann boundary reflects the process elastically; no paths are removed, so total probability stays at $1$ and the limit is the equilibrium (uniform) distribution.

---

**Exercise 5.**
Give a financial example where reflecting (Neumann) barriers are the appropriate modeling choice, and contrast it with a standard knock-out example where Dirichlet is appropriate.

??? success "Solution to Exercise 5"
    **Reflecting (Neumann)**: an FX rate inside a central-bank target zone, e.g. the classical European Exchange Rate Mechanism. When the rate reaches the band edge, intervention pushes it back without ending the process. Other examples: regulated short rates with a zero lower bound, constrained wealth processes rebalanced at a minimum guarantee. In all cases the process continues indefinitely, probability is conserved, and the long-run distribution is a specific equilibrium on the band.

    **Absorbing (Dirichlet)**: a down-and-out call with barrier $B$. If the underlying touches $B$ before maturity, the option is extinguished: no rebate, no further evolution. The price solves the Black-Scholes PDE on $(B,\infty)$ with $V(t,B) = 0$. Surviving mass decays as $T - t$ grows because more paths get knocked out, and long-maturity prices decay at spectral rate $\lambda_1 + r$.

---

**Exercise 6.**
A double-barrier option has $B_l = 80$, $B_u = 120$, $S_0 = 100$. In log-space the corridor has width $L = \log(B_u/B_l) = \log(3/2) \approx 0.405$. (a) Compute $\lambda_1$ for this corridor. (b) Estimate the maturity beyond which a single spectral mode gives $10^{-3}$ accuracy.

??? success "Solution to Exercise 6"
    (a) $\lambda_1 = \pi^2/(2L^2) = \pi^2/(2\cdot 0.405^2) \approx 9.87/0.328 \approx 30.1$.

    (b) The leading spectral error after one mode is $O(e^{-(\lambda_2 - \lambda_1)T}) = O(e^{-3\lambda_1 T})$ since $\lambda_n = n^2 \lambda_1$. Setting $e^{-3\lambda_1 T} = 10^{-3}$ gives

    $$
    T > \frac{\log 1000}{3\lambda_1} \approx \frac{6.91}{90.3} \approx 0.077\ \text{years},
    $$

    about one month. Past this horizon, a single mode prices the double-barrier option to three decimals -- while the image series would still need many terms since $T\gg L^2$ is already firmly in the spectral regime. For maturities below a month, the image representation is preferable.
