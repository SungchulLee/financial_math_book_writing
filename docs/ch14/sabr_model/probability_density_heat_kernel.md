# Probability Density via Heat Kernel Expansion

The deepest insight into the SABR model comes from recognizing that its dynamics define a diffusion on a **Riemannian manifold** --- specifically, a surface related to the hyperbolic plane. The transition density of this diffusion is the **heat kernel** on the manifold, and its short-time asymptotic expansion yields the Hagan implied volatility formula as a direct consequence. This geometric perspective, developed by Henry-Labordere (2008) and Lesniewski (2002), not only provides a rigorous derivation of the Hagan formula but also reveals the mathematical structure that governs the accuracy of the approximation and guides the construction of higher-order corrections.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Identify the Riemannian metric induced by the SABR diffusion
    2. Compute the geodesic distance on the SABR manifold
    3. Write down the leading-order heat kernel expansion
    4. Explain how the heat kernel leads to the Hagan implied volatility formula
    5. Describe the role of the hyperbolic plane in the SABR geometry

---

## Motivation

The standard approach to computing transition densities for SDEs is to solve the Fokker--Planck PDE. For two-dimensional problems like SABR, this requires numerical methods that are computationally expensive and provide limited analytical insight. The geometric approach offers an alternative: by interpreting the diffusion as Brownian motion on a curved surface, we can leverage the rich theory of heat kernels on Riemannian manifolds. The leading-order heat kernel involves only the geodesic distance between two points --- a purely geometric quantity --- and already captures the main features of the SABR smile. Higher-order terms (the Van Vleck determinant and curvature corrections) refine the approximation systematically.

---

## Riemannian Geometry of the SABR Diffusion

### From SDE to Metric

Consider the general SABR model after the coordinate transformation $y = F^{1-\beta}/(1-\beta)$ (for $\beta \neq 1$):

$$
dy_t = -\frac{\beta}{2}\frac{\sigma_t^2}{y_t^{1/(1-\beta)}}\,dt + \sigma_t\,dW_t^{(1)}
$$

$$
d\sigma_t = \nu\sigma_t\,dW_t^{(2)}
$$

Dropping the drift (which contributes only at higher order in the short-time expansion), the diffusion matrix in the coordinates $\mathbf{x} = (y, \sigma)$ is:

$$
\mathbf{a}(\mathbf{x}) = \begin{pmatrix} \sigma^2 & \rho\nu\sigma^2 \\ \rho\nu\sigma^2 & \nu^2\sigma^2 \end{pmatrix}
$$

The associated Riemannian metric is the **inverse** of the diffusion matrix:

$$
g_{ij} = (a^{-1})_{ij} = \frac{1}{(1-\rho^2)\sigma^2}\begin{pmatrix} 1 & -\rho/\nu \\ -\rho/\nu & 1/\nu^2 \end{pmatrix}
$$

### The Line Element

The Riemannian distance element is:

$$
ds^2 = g_{ij}\,dx^i\,dx^j = \frac{1}{(1-\rho^2)\sigma^2}\left(dy^2 - \frac{2\rho}{\nu}\,dy\,d\sigma + \frac{1}{\nu^2}\,d\sigma^2\right)
$$

For the uncorrelated case ($\rho = 0$), this simplifies to:

$$
ds^2 = \frac{dy^2}{\sigma^2} + \frac{d\sigma^2}{\nu^2\sigma^2}
$$

### Connection to the Hyperbolic Plane

The metric for $\rho = 0$ is recognized as the **Poincare upper half-plane** metric (up to a rescaling). The Poincare half-plane $\mathbb{H}^2$ has the metric:

$$
ds_{\mathbb{H}^2}^2 = \frac{dx^2 + dz^2}{z^2}
$$

Identifying $x = y$ and $z = \sigma/\nu$, the SABR metric becomes:

$$
ds^2 = \frac{dy^2 + (d\sigma/\nu)^2}{\sigma^2/\nu^2} = \frac{dy^2 + dz^2}{z^2} \cdot \frac{1}{\nu^2}
$$

which is $1/\nu^2$ times the hyperbolic metric. The **hyperbolic plane** is a surface of constant **negative Gaussian curvature** $\mathcal{K} = -\nu^2$. This negative curvature is responsible for the "spreading" of geodesics and the characteristic shape of the SABR smile.

!!! tip "Geometric Intuition"
    On a flat surface (like the Black--Scholes model), the heat kernel is a simple Gaussian whose width grows as $\sqrt{t}$. On a negatively curved surface, geodesics diverge faster than on a flat surface, causing the heat kernel to spread more rapidly in certain directions. This enhanced spreading in the SABR geometry produces the heavier tails and more pronounced smile that distinguish SABR from the CEV model.

### The Correlated Case

When $\rho \neq 0$, the metric includes off-diagonal terms. The geometry is still a surface of constant negative curvature, but the coordinate system is **oblique**. The off-diagonal terms can be removed by a rotation:

$$
\tilde{y} = y - \frac{\rho}{\nu}\sigma, \qquad \tilde{\sigma} = \frac{\sqrt{1-\rho^2}}{\nu}\sigma
$$

In these coordinates, the metric becomes diagonal and proportional to the hyperbolic metric. The correlation $\rho$ acts as a **shear** in the geometry, tilting the geodesics and breaking the left-right symmetry of the smile.

---

## Geodesic Distance

### Definition

The geodesic distance $d(\mathbf{x}_0, \mathbf{x})$ is the length of the shortest path between two points on the manifold. For the heat kernel expansion, this distance is the key quantity: the leading-order density is proportional to $\exp(-d^2/(2T))$.

### Formula for the SABR Manifold

For the SABR model in coordinates $(y, \sigma)$ with $y = F^{1-\beta}/(1-\beta)$, the geodesic distance between $(y_0, \sigma_0)$ and $(y, \sigma)$ is:

$$
d^2 = \frac{1}{1-\rho^2}\left[\ln^2\!\left(\frac{\sigma}{\sigma_0}\right) - 2\rho\nu\ln\!\left(\frac{\sigma}{\sigma_0}\right)\frac{y - y_0}{\bar{\sigma}} + \nu^2\frac{(y - y_0)^2}{\bar{\sigma}^2}\right]
$$

where $\bar{\sigma}$ is an appropriate average of $\sigma_0$ and $\sigma$ along the geodesic. For the uncorrelated case, this simplifies significantly.

### Uncorrelated Geodesic Distance (Rho = 0)

When $\rho = 0$, the geodesic distance on the SABR manifold reduces to:

$$
\cosh(\nu\,d) = 1 + \frac{\nu^2(y - y_0)^2 + (\sigma - \sigma_0)^2}{2\sigma_0\sigma}
$$

This is the standard **hyperbolic distance formula** on the Poincare half-plane (with the identification $z = \sigma/\nu$). The geodesics are semicircles orthogonal to the $\sigma = 0$ axis.

!!! info "Theorem: Geodesic Distance on the Uncorrelated SABR Manifold"
    For $\rho = 0$, the geodesic distance between $(y_0, \sigma_0)$ and $(y, \sigma)$ on the SABR manifold is:

    $$
    d = \frac{1}{\nu}\cosh^{-1}\!\left(1 + \frac{\nu^2(y - y_0)^2 + (\sigma - \sigma_0)^2}{2\sigma_0\sigma}\right)
    $$

    where $y = F^{1-\beta}/(1-\beta)$ and $y_0 = F_0^{1-\beta}/(1-\beta)$.

### Connection to the z/x(z) Factor

The geodesic distance in the Hagan formula appears through the $z/x(z)$ factor. Recall that:

$$
z = \frac{\nu}{\alpha}(FK)^{(1-\beta)/2}\ln\frac{F}{K}
$$

and $x(z) = \ln((\sqrt{1 - 2\rho z + z^2} + z - \rho)/(1 - \rho))$. The quantity $x(z)$ is (to leading order) the geodesic distance between the initial and terminal points, evaluated at $\sigma = \sigma_0 = \alpha$. The ratio $z/x(z)$ is the **Jacobian** of the mapping from the flat (Euclidean) parameterization to the geodesic (hyperbolic) parameterization.

---

## The Heat Kernel Expansion

### General Framework

The heat kernel $p(T, \mathbf{x}_0, \mathbf{x})$ is the fundamental solution of the heat equation on the Riemannian manifold:

$$
\frac{\partial p}{\partial T} = \frac{1}{2}\Delta_g\,p
$$

where $\Delta_g$ is the Laplace--Beltrami operator associated with the metric $g$. The short-time asymptotic expansion of the heat kernel is:

$$
p(T, \mathbf{x}_0, \mathbf{x}) = \frac{1}{2\pi T}\frac{\Delta_{\text{VV}}(\mathbf{x}_0, \mathbf{x})}{\sqrt{\det g(\mathbf{x})}}\exp\!\left(-\frac{d^2(\mathbf{x}_0, \mathbf{x})}{2T}\right)\left[1 + a_1(\mathbf{x}_0, \mathbf{x})\,T + O(T^2)\right]
$$

The components are:

**Leading exponential**: $\exp(-d^2/(2T))$ where $d$ is the geodesic distance. This is the analog of the Gaussian kernel on flat space.

**Van Vleck determinant**: $\Delta_{\text{VV}}$ accounts for the focusing or defocusing of geodesics. On the hyperbolic plane, geodesics diverge, so $\Delta_{\text{VV}} < 1$ (the density is suppressed relative to flat space).

**Volume element**: $\sqrt{\det g}$ is the Riemannian volume form, ensuring the density integrates to 1.

**Correction terms**: The coefficients $a_1, a_2, \ldots$ involve the Ricci curvature and its derivatives, providing systematic improvements.

### Application to SABR

For the SABR manifold with constant negative curvature $\mathcal{K} = -\nu^2$, the heat kernel on the hyperbolic plane has the exact representation (McKean, 1970):

$$
p_{\mathbb{H}^2}(T, d) = \frac{\sqrt{2}}{(2\pi T)^{3/2}}\,e^{-\nu^2 T/8}\int_d^{\infty} \frac{s\,e^{-s^2/(2T)}}{\sqrt{\cosh(\nu s) - \cosh(\nu d)}}\,ds
$$

This exact formula involves a one-dimensional integral that can be evaluated numerically. The short-time expansion of this integral recovers the Hagan formula.

---

## From Heat Kernel to Implied Volatility

### The Density-to-Price-to-IV Pipeline

The connection from the heat kernel to the Hagan implied volatility formula follows this sequence:

1. **Transition density**: The heat kernel gives $p(F_T, \sigma_T \mid F_0, \sigma_0; T)$
2. **Marginal density**: Integrate over terminal volatility $\sigma_T$ to obtain $p(F_T \mid F_0, \sigma_0; T)$
3. **Option price**: $C(K, T) = \int_K^{\infty}(F - K)\,p(F, T)\,dF$
4. **Implied volatility**: Invert the Black (or Bachelier) formula to obtain $\sigma_{\text{impl}}(K)$

The asymptotic expansion at each step preserves the order of accuracy. The $O(T)$ Hagan correction arises from the integration over $\sigma_T$ and the curvature corrections in the heat kernel.

### Leading-Order Result

At leading order (ignoring the $O(T)$ correction), the implied volatility is determined entirely by the geodesic distance:

$$
\sigma_B(K) \approx \frac{\alpha}{(FK)^{(1-\beta)/2}} \cdot \frac{z}{x(z)}
$$

This shows that the smile shape is a **purely geometric** quantity, determined by the geodesic structure of the SABR manifold. The $z/x(z)$ factor is the ratio of the "Euclidean distance" $z$ to the "geodesic distance" $x(z)$ in the $(y, \sigma)$ plane.

---

## Higher-Order Corrections

### The First Correction Term

The $O(T)$ correction in the Hagan formula:

$$
\varepsilon = \frac{(1-\beta)^2\alpha^2}{24(FK)^{1-\beta}} + \frac{\rho\beta\nu\alpha}{4(FK)^{(1-\beta)/2}} + \frac{2-3\rho^2}{24}\nu^2
$$

arises from three sources:

1. **Drift correction**: The first term $\propto \alpha^2$ comes from the drift that was dropped in the leading-order geometric analysis
2. **Cross-term**: The second term $\propto \rho\nu\alpha$ comes from the correlation-induced asymmetry
3. **Curvature**: The third term $\propto \nu^2$ is a pure curvature correction from the Ricci scalar of the manifold

### Systematic Improvement

The heat kernel expansion can be extended to $O(T^2)$ and beyond, producing higher-order corrections to the Hagan formula. Paulot (2009) derived the second-order correction, which is particularly important for:

- Long-maturity options ($T > 5$ years)
- High vol-of-vol ($\nu > 0.6$)
- Deep out-of-the-money strikes

Each additional order introduces more terms but maintains the same geometric structure.

---

## Summary

The probability density of the SABR model is the heat kernel on a Riemannian manifold of constant negative curvature. The Riemannian metric is determined by the SABR diffusion coefficients, and for $\rho = 0$ the manifold is isometric to the Poincare hyperbolic plane with curvature $-\nu^2$. The geodesic distance on this manifold directly yields the $z/x(z)$ smile factor in the Hagan formula, while the $O(T)$ correction arises from drift terms, correlation, and curvature. This geometric interpretation provides a rigorous foundation for the Hagan approximation and a systematic framework for computing higher-order corrections. The McKean heat kernel formula gives the exact density for the uncorrelated case, serving as a benchmark for all approximate and numerical methods.

---

## Further Reading

- Henry-Labordere, P. (2008). *Analysis, Geometry, and Modeling in Finance*. Chapman & Hall/CRC.
- McKean, H. P. (1970). *An upper bound to the spectrum of $\Delta$ on a manifold of negative curvature*. Journal of Differential Geometry.
- Lesniewski, A. (2002). *Notes on the SABR model*. Unpublished lecture notes.
- Paulot, L. (2009). *Asymptotic implied volatility at the second order with application to the SABR model*. SSRN preprint.

---

## Exercises

**Exercise 1.** The SABR model with $\rho = 0$ defines a diffusion on a surface isometric to the Poincare hyperbolic plane with curvature $-\nu^2$. Explain intuitively why the curvature is negative (the "geometry" is hyperbolic rather than Euclidean or spherical). What happens to the curvature as $\nu \to 0$? What does this limit correspond to in terms of the SABR model?

---

**Exercise 2.** The geodesic distance on the SABR manifold between the initial point $(F_0, \alpha)$ and the point $(K, \alpha)$ is related to the Hagan smile factor $z/x(z)$. For $\rho = 0$, the geodesic distance simplifies to $d = \frac{1}{\nu}\cosh^{-1}\!\bigl(1 + \frac{\nu^2}{2\alpha^2}\frac{(K-F)^2}{(FK)^{1-\beta}}\bigr)$ (schematic). Explain why a larger geodesic distance (corresponding to a further OTM strike) leads to a higher implied volatility through the heat kernel decay.

---

**Exercise 3.** The short-time heat kernel expansion gives the density as $p(t, x, y) \sim \frac{1}{t}\exp\bigl(-\frac{d^2(x,y)}{2t}\bigr) \cdot g(x,y)$ where $d$ is the geodesic distance and $g$ involves curvature corrections. Explain why the leading $\exp(-d^2/(2t))$ term becomes more concentrated around $x = y$ as $t \to 0$, and how the $O(t)$ corrections give rise to the skew and convexity terms in the Hagan formula.

---

**Exercise 4.** For the uncorrelated case $\rho = 0$, the McKean heat kernel provides the exact transition density. Explain why adding correlation ($\rho \neq 0$) breaks the simple hyperbolic geometry and requires perturbation methods. How does the Hagan formula handle the correlation: is $\rho$ included in the geodesic distance, the curvature correction, or both?

---

**Exercise 5.** The geometric approach yields higher-order corrections to the Hagan formula (Paulot 2009). The second-order correction improves accuracy from $O(\nu^2 T^2)$ to $O(\nu^2 T^3)$. For a 5-year swaption with $\nu = 0.5$, estimate the improvement factor $T$ in the error bound. Is the second-order correction worth implementing for practical applications?

---

**Exercise 6.** Compare the geometric (heat kernel) derivation of the Hagan formula with the direct PDE perturbation approach. Both yield the same leading-order formula. What additional insight does the geometric approach provide? Specifically, explain how the Riemannian metric interpretation helps determine when the approximation will fail (e.g., for strikes far from ATM on the manifold).
