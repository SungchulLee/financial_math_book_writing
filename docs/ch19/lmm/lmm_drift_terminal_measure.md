# LMM Drift in Terminal Measure

The LIBOR Market Model (LMM) is the standard framework for pricing interest rate derivatives across multiple tenors simultaneously. A crucial technical aspect is the drift correction required when changing the numeraire to a specific maturity, enabling efficient calibration and pricing under different term structures.

## Key Concepts

**LIBOR Dynamics in Spot Measure**
Define forward LIBOR $L_k(t)$ for tenor $[T_k, T_{k+1}]$ with accrual $\delta_k$:
$$dL_k(t) = \mu_k^{\text{spot}}(t) dt + \sigma_k(t) dB_k(t)$$

The spot measure uses the rolling bank account as numeraire:
$$N_t^{\text{spot}} = \prod_{j: T_j \leq t} (1 + \delta_j L_j(T_j))$$

**Terminal Measure Change**
The terminal measure uses the zero-coupon bond maturing at time $T_N$ as numeraire:
$$N_t^{N} = P(t, T_N)$$

Under terminal measure:
$$dL_k(t) = \mu_k^N(t) dt + \sigma_k(t) dB_k^N(t)$$

The Brownian motion has changed to $B_k^N$ reflecting the new measure.

**Drift Correction Formula**
The drift correction relates spot and terminal measure drifts:
$$\mu_k^N(t) = \mu_k^{\text{spot}}(t) + \sigma_k(t) \sum_{j=k+1}^{N} \frac{\delta_j \sigma_j(t) \rho_{k,j}}{1 + \delta_j L_j(t)}$$

Key features:
- Correction term is positive (martingale property enforced)
- Depends on instantaneous correlation $\rho_{k,j}$ between rate curves
- Involves future rates for indices $j > k$ in terminal measure

**Intuition**
The drift correction arises because:
1. Zero-coupon bond price depends on all future rates
2. When changing numeraire to $P(t, T_N)$, relative pricing changes
3. Girsanov theorem ensures the SDE coefficient structure remains proportional to $\sigma_k$
4. Only drift changes, volatility structure preserved

**Practical Implementation**
LMM calibration proceeds in terminal measure:
1. Specify volatility structure $\sigma_k(t)$ (typically piecewise constant or deterministic)
2. Specify correlation matrix $\rho_{i,j}$ for all rate pairs
3. Drift is automatically computed from formula
4. Simulate forward rates under terminal measure
5. Compute prices by averaging discounted payoffs

**Efficient Calibration**
Terminal measure enables efficient calibration:
- Caplets/floorlets prices depend on individual rate volatilities $\sigma_k$
- Swaptions prices depend on rate correlation structure
- Two-stage calibration: fit volatilities to caps, correlations to swaptions
- Avoids explicit specification of spot measure drifts

**Connection to Swap Measure**
Alternative: swap measure uses annuity as numeraire
$$N_t^{\text{swap}} = A_t = \sum_{j=k}^{N} \delta_j P(t, T_j)$$

Swap measure drift is different from terminal measure, optimized for swaption pricing.

!!! note "Practical Insights"
    Terminal measure provides:
    - Computational efficiency through direct calibration
    - Intuitive interpretation: numeraire is final cash received
    - Stability in long-dated simulations
    - Effective handling of multiple correlated rates simultaneously

## QuantPie Derivation: LIBOR Market Model Spot Measure

### Definition of LIBOR and Spot Measure

**LIBOR Definition**

$$\begin{array}{ccccccc}
\displaystyle
L_n\left(t\right)P\left(t,T_{n}\right)
=
\frac{1}{\delta}
\left(
P\left(t,T_{n-1}\right)-P\left(t,T_{n}\right)
\right)
&\Rightarrow&\displaystyle
L_n\left(t\right)
=
\frac{1}{\delta}
\left(
\frac{P\left(t,T_{n-1}\right)-P\left(t,T_{n}\right)}{P\left(t,T_{n}\right)}
\right)\\
\end{array}$$

is tradable, where $L_n\left(t\right)P\left(t,T_{n}\right)$ is the value of tradable assets.

### Bank Account (Spot Measure Numeraire)

$$\begin{array}{llllllll}
\displaystyle
M(t)
&:=&
\displaystyle
\frac{P(t,T_{\bar{m}(t)})}{\prod_{k=1}^{\bar{m}(t)}P(T_{k-1},T_k)}\\
\end{array}$$

where

$$
\bar{m}(t)=\text{min}\left(i:t\le T_i\right)
$$

### Bond Price and Accrual

When current time $t$ is $T_0$ or $T_k$:

$$\begin{array}
\displaystyle
B(T_n)=\prod_{i=0}^{n-1}\left(1+\delta L(T_i,T_i)\right)\\
\displaystyle
P(T_0,T_n)=\prod_{i=0}^{n-1}\frac{1}{1+\delta L(T_0,T_i)}\\
\displaystyle
P(T_k,T_n)=\prod_{i=k}^{n-1}\frac{1}{1+\delta L(T_k,T_i)}\\
\end{array}$$

When current time $t$ is $T_{q(t)-1}-\delta<t<T_{q(t)}$:

$$\begin{array}{lll}
\displaystyle
B(t)=P\left(t,T_{q(t)}\right)\prod_{i=0}^{q(t)-1}\left(1+\delta L(T_i,T_i)\right)\\
\displaystyle
P(t,T_n)=P\left(t,T_{q(t)}\right)\prod_{i=q(t)}^{n-1}\frac{1}{1+\delta L\left(T_{q(t)},T_i\right)}\\
\end{array}$$

### Radon-Nikodym Derivative for Spot Measure

$$\begin{array}{llllllll}
\displaystyle
\lambda_M^{\bar{n}(t)}(t)
&=&\displaystyle
\left.\frac{d\mathbb{Q}^{M}}{d\mathbb{Q}^{\bar{n}(t)}}\Big{|}{\cal F}(t)\right)\\
&=&\displaystyle
\frac{M(t)/M(t_0)}{P(t,T_{\bar{n}(t)})/P(t_0,T_{\bar{n}(t)})}\\
&=&\displaystyle
\frac{P(t,T_{\bar{m}(t)})}{P(t,T_{\bar{n}(t)})}
\frac{P(t_0,T_{\bar{n}(t)})}{M(t_0)}
\prod_{k=1}^{\bar{m}(t)}\frac{1}{P(T_{k-1},T_k)}\\
&:=&\displaystyle
\frac{P(t,T_{\bar{m}(t)})}{P(t,T_{\bar{n}(t)})}
\bar{P}\\
\end{array}$$

### Girsanov Transformation to Spot Measure

$$\begin{array}{lllll}
\displaystyle
dW_{\bar{n}(t)}^{M}(t)
&=&\displaystyle
-\frac{\tau_{\bar{n}(t)}\bar{\sigma}_{\bar{n}(t)}(t)}{\tau_{\bar{n}(t)}l_{\bar{n}(t)}(t)+1}dt
+dW_{\bar{n}(t)}^{\bar{n}(t)}(t)\\
\end{array}$$

### LIBOR Drift in Spot Measure

$$\begin{array}{lllll}
\displaystyle
dl_i(t)
&=&\displaystyle
\bar{\sigma}_i(t)\sum_{k=\bar{m}(t)+1}^{i}\frac{\tau_{k}\bar{\sigma}_{k}(t)}{\tau_{k}l_{k}(t)+1}dt
+\bar{\sigma}_i(t)dW_i^{M}(t)\\
\end{array}$$

### Special Case: Spot Measure Equals Forward Measure

**Spot Measure Radon-Nikodym Derivative**

$$\begin{array}{llllll}
\displaystyle
Z_t
:=
\mathbb{E}^{q(t)}\left[\frac{d\mathbb{P}_{S}}{d\mathbb{P}_{q(t)}}\Big{|}{\cal F}_t\right]
=
\frac{B(t)/B(0)}{P\left(t,T_{q(t)}\right)/P\left(0,T_{q(t)}\right)}\\
\end{array}$$

Since $\prod_{i=0}^{q(t)-1}\left(1+\delta L(T_i,T_i,T_{i+1})\right)$ is known at time $t$, let's call this constant $C_1$.

$$\begin{array}{llll}
\displaystyle
\frac{B(t)}{B(0)}
=
P(t,T_{q(t)})\prod_{i=0}^{q(t)-1}\left(1+\delta L(T_i,T_i,T_{i+1})\right)
=
C_1P(t,T_{q(t)})
\end{array}$$

Since $\prod_{i=0}^{q(t)-1}\left(1+\delta L(0,T_i,T_{i+1})\right)$ is known at time $t$,
let's call this constant $C_2$.

$$\begin{array}{llll}
\displaystyle
\frac{P(t,T_{q(t)})}{P(0,T_{q(t)})}
=
P(t,T_{q(t)})\prod_{i=0}^{q(t)-1}\left(1+\delta L(0,T_i,T_{i+1})\right)
=
C_2P(t,T_{q(t)})
\\
\end{array}$$

Since $Z_t$ is a Radon-Nykodym derivative, in particular we have $\mathbb{E}^{q(t)}[Z_t]=1$. Therefore,

$$\begin{array}{llllll}
\displaystyle
Z_t
=
\mathbb{E}^{q(t)}\left[\frac{d\mathbb{P}_{S}}{d\mathbb{P}_{q(t)}}\Big{|}{\cal F}_t\right]
=
\frac{B(t)/B(0)}{P\left(t,T_{q(t)}\right)/P\left(0,T_{q(t)}\right)}=\frac{C_1}{C_2}=1\\
\end{array}$$

This means

$$\begin{array}{lll}
\displaystyle
dW_t^{S}
=
dW_t^{q(t)}
\end{array}$$

### Equivalence of Spot and Forward Measures

$$\begin{array}{lll}
\displaystyle
\mathbb{P}_{S}
=
\mathbb{P}_{q(t)}
\end{array}$$
