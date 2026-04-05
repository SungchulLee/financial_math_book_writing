# Hull-White Caplet and Floor Formula

## Caplet/Floorlet Payoff

$$\begin{array}{lll}
\text{Time}&\text{Action}\\
T_{k-1}&\text{Forward Rate Determined $l_k(T_{k−1})=l(T_{k−1}; T_{k−1}, T_k)$ }\\
T_k&\text{Caplet Paid $N\tau_k \max(l_k(T_{k−1})-K,0))$}\\
&\text{Floorlet Paid $N\tau_k \max(K-l_k(T_{k−1}),0))$}
\end{array}$$

where $\tau_k=T_k-T_{k-1}$.

## Change of Numeraire

$$\begin{array}{llllllll}
\displaystyle
V^\text{CL}(t_0)
&=&\displaystyle
M(t_0)\mathbb{E^Q}\left[
\frac{N\tau_k\text{max}(l_k(T_{k-1})-K,0)}{M(T_k)}\Big{|}{\cal F}(t_0)
\right]
&=&\displaystyle
N\tau_kP(t_0,T_k)\mathbb{E}^{\mathbb{T_k}}\left[
\text{max}(l_k(T_{k-1})-K,0)\Big{|}{\cal F}(t_0)
\right]
\end{array}$$

## Forward Rate l_k is a T_k-Martingale

Since $l_k(t)=\frac{1}{\tau_k}\frac{P(t,T_{k-1})-P(t,T_k)}{P(t,T_k)}$ and since $P(t,T_{k-1})$ and $P(t,T_{k})$ are prices of tradable assets,

$$\begin{array}{lll}
\displaystyle
\mathbb{E}^{\mathbb{T_k}}\left[l_k(t)\Big{|}{\cal F}(s)\right]
=l_k(s)
\end{array}$$

## Black's Formula

Assume that the libor rate follows a lognormal distribution:

$$\begin{array}{lll}
\displaystyle
dl_k(t)
=
\sigma_kl_k(t)dW^{\mathbb{T_k}}(t)
\end{array}$$

Then, we can use the Black–Scholes computation with interest rate 0:

$$\begin{array}{lll}
\displaystyle
{\bf\text{Caplet}}^{\text{Black}}(t,T_{k-1},T_k,N,K,\sigma_k)
&=&\displaystyle
N\tau_kP(t,T_k)\left[
l_k(t)N(d_1)-KN(d_2)
\right]\\
\displaystyle
{\bf\text{Floorlet}}^{\text{Black}}(t,T_{k-1},T_k,N,K,\sigma_k)
&=&\displaystyle
N\tau_kP(t,T_k)\left[
-l_k(t)N(-d_1)+KN(-d_2)
\right]\\
\end{array}$$

where

$$\begin{array}{lll}
\displaystyle
d_1
&=&\displaystyle
\frac{1}{v_k}\log\left(\frac{l_k(t)}{K}\right)+\frac{1}{2}v_k\\
\displaystyle
d_2&=&\displaystyle
\frac{1}{v_k}\log\left(\frac{l_k(t)}{K}\right)-\frac{1}{2}v_k\\
v_k&=&\sigma_k\sqrt{T_{k-1}-t}\\
\end{array}$$

## Hull-White Caplet Formula (Using T_k Measure)

Let $t_0$, $T_{k-1}$, $T_k$ be current, reset date, maturity, respectively.

$$\begin{array}{lllll}
\displaystyle
V^\text{CPL}(t_0,T)
=
N P(t_0,T_k)e^{-A(\tau_k)}\left[e^{\frac{1}{2}B^2(\tau_k)\sigma_r^2(t_0,T_{k-1})-B(\tau_k)\mu^{\mathbb{T_k}}_r(t_0,T_{k-1})}N(d_1)-K_{\text{hat}}N(d_2)\right]
\end{array}$$

???+ note "Proof"

    $$\begin{array}{lll}
    \displaystyle
    V^\text{CPL}(t_0)
    &=&\displaystyle
    N\tau_kP(t_0,T_k)\mathbb{E}^{\mathbb{T_{k}}}\left[
    \text{max}(l_k(T_{k-1})-K,0)\Big{|}{\cal F}(t_0)
    \right]\\
    &=&\displaystyle
    N(1+\tau_k K)P(t_0,T_k)\mathbb{E}^{\mathbb{T_{k}}}\left[
    \text{max}\left(\frac{1}{1+\tau_k K}-P(T_{k-1},T_k),0\right)\Big{|}{\cal F}(t_0)
    \right]
    \end{array}$$

    This is a put option on the ZCB $P(T_{k-1},T_k)$ with strike $\frac{1}{1+\tau_k K}$, which can be priced using the Hull-White ZCB option formula.

## Cap and Floor

$$\begin{array}{lll}
\displaystyle\text{Cap}&=&\displaystyle\sum\text{Caplet}\\
\displaystyle\text{Floor}&=&\displaystyle\sum\text{Floorlet}\\
\end{array}$$

## Effect of Hull-White Model Parameters on Implied Volatilities

```python
def main():
    # Vary sigma and lambda to see effect on implied vol
    hw = HullWhite(sigma=0.01, lambd=0.01, P=P_market)

    K_grid = np.linspace(0.01, 0.10, 20)
    T_reset = 5.0
    T_pay = 5.5

    for sigma in [0.005, 0.01, 0.02]:
        hw.sigma = sigma
        implied_vols = []
        for K in K_grid:
            price = hw.compute_Caplet_Floorlet_Price(1, K, T_reset, T_pay, OptionType.CALL)
            iv = compute_Implied_Volatility_using_Black76(price, K, T_reset, S_0, OptionType.CALL)
            implied_vols.append(iv)
        plt.plot(K_grid, implied_vols, label=f'sigma={sigma}')
```

## QuantPie Derivation: Caplet as ZCB Put

### Caplet is ZCB Put (Using T_k-1 Measure)

$$\begin{array}{lll}
\displaystyle
V^\text{CPL}(t_0)
=
\hat{N}P(t_0,T_{k-1})\mathbb{E}^{T_{k-1}}\left[
\text{max}\left(\hat{K}-P(T_{k-1},T_k),0\right)\Big{|}{\cal F}(t_0)
\right]\\
\end{array}$$

where

$$\begin{array}{lll}
\displaystyle
\hat{N}
&:=&\displaystyle
N(1+\tau_k K)\\
\displaystyle
\hat{K}&:=&\displaystyle
\frac{1}{1+\tau_k K}\\
\end{array}$$

### Proof

$$\begin{array}{lll}
\displaystyle
V^\text{CPL}(t_0)
&=&\displaystyle
M(t_0)\mathbb{E^Q}\left[
\frac{N\tau_k\text{max}(l_k(T_{k-1})-K,0)}{M(T_k)}\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
M(t_0)\mathbb{E^Q}\left[\mathbb{E^Q}\left[
\frac{N\tau_k\text{max}(l_k(T_{k-1})-K,0)}{M(T_k)}\Big{|}{\cal F}(T_{k-1})
\right]\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
M(t_0)\mathbb{E^Q}\left[N\tau_k\text{max}(l_k(T_{k-1})-K,0)\mathbb{E^Q}\left[
\frac{1}{M(T_k)}\Big{|}{\cal F}(T_{k-1})
\right]\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
M(t_0)\mathbb{E^Q}\left[N\tau_k\text{max}(l_k(T_{k-1})-K,0)
\frac{P(T_{k-1},T_k)}{M(T_{k-1})}\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
M(t_0)\mathbb{E^Q}\left[N\tau_k\text{max}\left(\frac{1}{\tau_k}\left(\frac{1}{P(T_{k-1},T_k)}-1\right)-K,0\right)
\frac{P(T_{k-1},T_k)}{M(T_{k-1})}\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
M(t_0)\mathbb{E^Q}\left[N\text{max}\left(\frac{1}{P(T_{k-1},T_k)}-(1+\tau_k K),0\right)
\frac{P(T_{k-1},T_k)}{M(T_{k-1})}\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
M(t_0)\mathbb{E^Q}\left[N\text{max}\left(1-(1+\tau_k K)P(T_{k-1},T_k),0\right)
\frac{1}{M(T_{k-1})}\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
M(t_0)\mathbb{E^Q}\left[
N(1+\tau_k K)\text{max}\left(\frac{1}{(1+\tau_k K)}-P(T_{k-1},T_k),0\right)\frac{1}{M(T_{k-1})}\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
M(t_0)\mathbb{E}^{T_{k-1}}\left[
N(1+\tau_k K)\text{max}\left(\frac{1}{(1+\tau_k K)}-P(T_{k-1},T_k),0\right)\frac{1}{M(T_{k-1})}\frac{M(T_{k-1})/M(t_0)}{1/P(t_0,T_{k-1})}\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
N(1+\tau_k K)P(t_0,T_{k-1})\mathbb{E}^{T_{k-1}}\left[
\text{max}\left(\frac{1}{(1+\tau_k K)}-P(T_{k-1},T_k),0\right)\Big{|}{\cal F}(t_0)
\right]\\
&:=&\displaystyle
\hat{N}P(t_0,T_{k-1})\mathbb{E}^{T_{k-1}}\left[
\text{max}\left(\hat{K}-P(T_{k-1},T_k),0\right)\Big{|}{\cal F}(t_0)
\right]
\end{array}$$

## QuantPie Derivation: Hull-White Caplet Formula (Using T_k Measure)

### Hull-White Caplet Formula (Using T_k Measure)

Let $t_0$, $T_{k-1}$, $T_k$ be current, reset date, maturity, respectively.

$$\begin{array}{lllll}
\displaystyle
V^\text{CPL}(t_0,T)
=
N P(t_0,T_k)e^{-A(\tau_k)}\left[e^{\frac{1}{2}B^2(\tau_k)v_r^2(t_0,T_{k-1})-B(\tau_k)\mu_r(t_0,T_{k-1},\color{red}{T_k})}N(d_1)-\hat{K}N(d_2)\right]\\
\end{array}$$

where $A(\tau_k)$ and $B(\tau_k)$ are related with
the underlying ZCB price $P(T_{k-1},T_k)$ at option maturity $T_{k-1}$,
$\tau_k=T_k-T_{k-1}$, by

$$\begin{array}{lll}
\displaystyle
\theta(t)
&=&\displaystyle
f(0,t)+\frac{1}{\lambda}\frac{\partial f(0,t)}{\partial t}
-
\frac{\sigma^2}{2\lambda^2}\left(e^{-2\lambda t}-1\right)\\
\displaystyle
A(\tau_k)
&=&\displaystyle
-\frac{\sigma^2}{4\lambda^3}
\left(3-2\lambda\tau_k-4e^{-\lambda\tau_k}+e^{-2\lambda\tau_k}\right)
+
\lambda\int_0^{\tau_k}\theta(T_k-\tau')B(\tau')d\tau'
\\
\displaystyle
B(\tau_k)
&=&\displaystyle
\frac{e^{-\lambda\tau_k}-1}{\lambda}
\\
\displaystyle
P(T_{k-1},T_k)
&=&\displaystyle e^{A(\tau_k)+B(\tau_k)r(T_{k-1})}\\
\end{array}$$

where $\mu_r(t_0,T_{k-1},\color{red}{T_k})$ and $v_r^2(t_0,T_{k-1})$ are related with
the short rate $r(T_{k-1})$ at option maturity $T_{k-1}$
under $\mathbb{Q}^{\color{red}{T_{k}}}$, not $\mathbb{Q}^{\color{black}{T_{k-1}}}$ measure by

$$\begin{array}{lll}
\displaystyle
\theta^{\color{red}{T_{k}}}(t)
&=&\displaystyle\theta(t)+\frac{\sigma^2}{\lambda}B(\color{red}{T_{k}}-t)\\
dr(t)&=&\displaystyle
\lambda\left(\theta^{\color{red}{T_{k}}}(t)-r(t)\right) dt+\sigma dW^{\color{red}{T_{k}}}(t)\\
\displaystyle
r(T_{k-1})|r(t_0)&\sim&\displaystyle
N\left(\mu_r(t_0,T_{k-1},\color{red}{T_k}),v_r^2(t_0,T_{k-1})\right)\\
\mu_r(t_0,T_{k-1},\color{red}{T_k})&=&\displaystyle
r(t_0)e^{-\lambda(T_{k-1}-t_0)}
+\lambda\int_{t_0}^{T_{k-1}}\theta^{\color{red}{T_{k}}}(t')e^{-\lambda(T_{k-1}-t')}dt'\\
v_r^2(t_0,T_{k-1})&=&\displaystyle
-\frac{\sigma^2}{2\lambda}\left(e^{-2\lambda(T_{k-1}-t_0)}-1\right)\\
\end{array}$$

and where $\hat{K}$, $d_1$ and $d_2$ are constants from Black Scholes type integration computation:

$$\begin{array}{lll}
\hat{K}&=&(1+\tau_k K)e^{A(\tau_k)}\\
d_2&=&\displaystyle
\frac{\log\hat{K}+B(\tau_k)\mu_r(t_0,T_{k-1},\color{red}{T_k})}{B(\tau_k)v_r(t_0,T_{k-1})}\\
d_1&=&\displaystyle
d_2-B(\tau_k)v_r(t_0,T_{k-1})
\end{array}$$

### Proof

$$\begin{array}{lll}
\displaystyle
V^\text{CPL}(t_0)
&=&\displaystyle
M(t_0)\mathbb{E^Q}\left[
\frac{N\tau_k\text{max}(l_k(T_{k-1})-K,0)}{M(T_k)}\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
N\tau_kP(t_0,T_k)\mathbb{E}^{T_k}\left[
\text{max}(l_k(T_{k-1})-K,0)\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
N\tau_kP(t_0,T_k)\mathbb{E}^{T_k}\left[
\text{max}\left(\frac{1}{\tau_k}\left(\frac{1}{P(T_{k-1},T_k)}-1\right)-K,0\right)\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
N P(t_0,T_k)\mathbb{E}^{T_k}\left[
\text{max}\left(\frac{1}{P(T_{k-1},T_k)}-1-\tau_k K,0\right)\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
N P(t_0,T_k)\mathbb{E}^{T_k}\left[
\text{max}\left(e^{-A(\tau_k)-B(\tau_k)r(T_{k-1})}-1-\tau_k K,0\right)\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
N P(t_0,T_k)e^{-A(\tau_k)}\mathbb{E}^{T_k}\left[
\text{max}\left(e^{-B(\tau_k)r(T_{k-1})}-(1+\tau_k K)e^{A(\tau_k)},0\right)\Big{|}{\cal F}(t_0)
\right]\\
&:=&\displaystyle
N P(t_0,T_k)e^{-A(\tau_k)}\mathbb{E}^{T_k}\left[
\text{max}\left(e^{-B(\tau_k)r(T_{k-1})}-\hat{K},0\right)\Big{|}{\cal F}(t_0)
\right]\\
\end{array}$$

Now, by solving $dr(t)=\lambda\left(\theta^{\color{red}{T_k}}(t)-r(t)\right) dt+\sigma dW^{\color{red}{T_k}}(t)$

$$
\displaystyle
r(T_{k-1})|r(t_0)\sim N\left(\mu_r(t_0,T_{k-1},\color{red}{T_k}),v_r^2(t_0,T_{k-1})\right)
$$

With $B(\tau_k)=(e^{-\lambda\tau_k}-1)/\lambda$

$$
\displaystyle
-B(\tau_k)r(T_{k-1})\sim N\left(-B(\tau_k)\mu_r(t_0,T_{k-1},\color{red}{T_k}),B^2(\tau_k)v_r^2(t_0,T_{k-1})\right)
$$

Following Black Scholes computation, we have for the call
(remember $B(\tau)=(e^{-\lambda\tau}-1)/\lambda<0$)

$$\begin{array}{lll}
\displaystyle
V^\text{CPL}(t_0)
&=&\displaystyle
N P(t_0,T_k)e^{-A(\tau_k)}\mathbb{E}^{T_k}\left[
\text{max}\left(e^{-B(\tau_k)r(T_{k-1})}-\hat{K},0\right)\Big{|}{\cal F}(t_0)
\right]\\
&=&\displaystyle
N P(t_0,T_k)e^{-A(\tau_k)}
\int_{e^{-B(\tau_k)\mu_r(t_0,T_{k-1})+B(\tau_k)v_r(t_0,T_{k-1})z}>\hat{K}}
\left(e^{-B(\tau_k)\mu_r(t_0,T_{k-1})+B(\tau_k)v_r(t_0,T_{k-1})z}-\hat{K}\right)\frac{1}{\sqrt{2\pi}}e^{-z^2/2}dz\\
&=&\displaystyle
N P(t_0,T_k)e^{-A(\tau_k)}
\int^a_{-\infty}
\left(e^{-B(\tau_k)\mu_r(t_0,T_{k-1})+B(\tau_k)v_r(t_0,T_{k-1})z}-\hat{K}\right)\frac{1}{\sqrt{2\pi}}e^{-z^2/2}dz\\
&=&\displaystyle
N P(t_0,T_k)e^{-A(\tau_k)}\left[e^{\frac{1}{2}B^2(\tau_k)v_r^2(t_0,T_{k-1})-B(\tau_k)\mu_r(t_0,T_{k-1})}N(d_1)-\hat{K}N(d_2)\right]\\
\end{array}$$

where

$$\begin{array}{lll}
\hat{K}&=&(1+\tau_k K)e^{A(\tau_k)}\\
a&=&\displaystyle
\frac{\log\hat{K}+B(\tau_k)\mu_r(t_0,T_{k-1},\color{red}{T_k})}{B(\tau_k)v_r(t_0,T_{k-1})}\\
d_1&=&\displaystyle
a-B(\tau_k)v_r(t_0,T_{k-1})\\
d_2&=&a
\end{array}$$

---

## Exercises

**Exercise 1.** Show that a caplet with reset date $T_{k-1}$ and payment date $T_k$ is equivalent to a put option on the zero-coupon bond $P(T_{k-1}, T_k)$ with modified notional $\hat{N} = N(1 + \tau_k K)$ and strike $\hat{K} = \frac{1}{1 + \tau_k K}$.

??? success "Solution to Exercise 1"
    Starting from the risk-neutral pricing formula for the caplet payoff at $T_k$:

    $$
    V^{\text{CPL}}(t_0) = \mathbb{E}^{\mathbb{Q}}\!\left[\frac{M(t_0)}{M(T_k)}\,N\tau_k\max(l_k(T_{k-1}) - K, 0)\,\Big|\,\mathcal{F}(t_0)\right]
    $$

    Using the tower property to condition on $\mathcal{F}(T_{k-1})$ and the definition $l_k(T_{k-1}) = \frac{1}{\tau_k}\!\left(\frac{1}{P(T_{k-1},T_k)} - 1\right)$:

    $$
    V^{\text{CPL}}(t_0) = \mathbb{E}^{\mathbb{Q}}\!\left[\frac{M(t_0)}{M(T_{k-1})}\,N\tau_k\max(l_k(T_{k-1}) - K, 0)\,P(T_{k-1},T_k)\,\Big|\,\mathcal{F}(t_0)\right]
    $$

    Substituting the LIBOR definition and simplifying:

    $$
    N\tau_k\max(l_k(T_{k-1}) - K, 0)\,P(T_{k-1},T_k) = N\max\!\left(1 - (1+\tau_k K)P(T_{k-1},T_k),\,0\right)
    $$

    Factoring out $(1+\tau_k K)$:

    $$
    = N(1+\tau_k K)\max\!\left(\frac{1}{1+\tau_k K} - P(T_{k-1},T_k),\,0\right)
    $$

    Defining $\hat{N} = N(1+\tau_k K)$ and $\hat{K} = \frac{1}{1+\tau_k K}$:

    $$
    V^{\text{CPL}}(t_0) = \hat{N}\,\mathbb{E}^{\mathbb{Q}}\!\left[\frac{M(t_0)}{M(T_{k-1})}\max(\hat{K} - P(T_{k-1},T_k),\,0)\,\Big|\,\mathcal{F}(t_0)\right]
    $$

    The right-hand side is exactly $\hat{N}$ times the price of a European put option on the ZCB $P(T_{k-1},T_k)$ with option maturity $T_{k-1}$ and strike $\hat{K}$.

---

**Exercise 2.** In Black's formula, the forward LIBOR rate $l_k(t)$ is assumed lognormal under $\mathbb{Q}^{T_k}$. In the Hull-White model, the short rate is Gaussian. Explain why these two assumptions lead to different implied volatility structures across strikes.

??? success "Solution to Exercise 2"
    **Black's formula (lognormal assumption):** Under the $\mathbb{Q}^{T_k}$ measure, the forward LIBOR rate $l_k(t)$ is assumed to follow geometric Brownian motion $dl_k = \sigma_k l_k\,dW^{T_k}$. This means $l_k(T_{k-1})$ is lognormally distributed, which gives a constant implied volatility across all strikes (a flat smile).

    **Hull-White model (Gaussian assumption):** The short rate $r(t)$ follows an Ornstein-Uhlenbeck process, so $r(T_{k-1})$ is normally distributed. The caplet price depends on the ZCB price $P(T_{k-1},T_k) = e^{A(\tau_k) + B(\tau_k)r(T_{k-1})}$, which is the exponential of a Gaussian random variable, hence lognormally distributed.

    The forward LIBOR rate $l_k(T_{k-1}) = \frac{1}{\tau_k}\!\left(\frac{1}{P(T_{k-1},T_k)} - 1\right)$ is then a nonlinear function of a lognormal variable. When we invert Black's formula to extract the implied volatility from Hull-White prices, we obtain an implied vol that depends on the strike $K$, producing a volatility skew. The skew arises because the distribution of $l_k(T_{k-1})$ under the Hull-White model differs from the lognormal distribution: the tails behave differently, leading to higher implied volatilities for deep in-the-money or out-of-the-money strikes relative to at-the-money.

---

**Exercise 3.** For a caplet with $T_{k-1} = 4$, $T_k = 5$, $K = 0.04$, $N = 1{,}000{,}000$, compute $\hat{N}$ and $\hat{K}$. Using Hull-White parameters $\lambda = 0.05$ and $\sigma = 0.01$, describe the inputs needed for the ZCB put option formula.

??? success "Solution to Exercise 3"
    Given $T_{k-1} = 4$, $T_k = 5$, $K = 0.04$, $N = 1{,}000{,}000$, and $\tau_k = T_k - T_{k-1} = 1$:

    **Modified notional:**

    $$
    \hat{N} = N(1 + \tau_k K) = 1{,}000{,}000 \times (1 + 1 \times 0.04) = 1{,}040{,}000
    $$

    **Modified strike:**

    $$
    \hat{K} = \frac{1}{1 + \tau_k K} = \frac{1}{1.04} \approx 0.96154
    $$

    For the ZCB put option formula in the Hull-White model, the required inputs are:

    - **Option maturity:** $T_{k-1} = 4$ (the caplet reset date)
    - **Bond maturity:** $T_k = 5$
    - **Strike:** $\hat{K} = 0.96154$
    - **Hull-White parameters:** $\lambda = 0.05$, $\sigma = 0.01$
    - **Bond price function $B(\tau_k)$:** $B(1) = \frac{e^{-0.05 \times 1} - 1}{0.05} = \frac{0.9512 - 1}{0.05} \approx -0.9754$
    - **Conditional mean $\mu_r(t_0, T_{k-1}, T_k)$:** Requires the market yield curve (forward rates) and the drift adjustment for the $T_k$-measure
    - **Conditional variance $v_r^2(t_0, T_{k-1})$:** $v_r^2(0, 4) = \frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda \times 4}) = \frac{0.0001}{0.1}(1 - e^{-0.4}) \approx 0.001 \times 0.3297 \approx 0.0003297$, so $v_r(0,4) \approx 0.01816$

---

**Exercise 4.** The proof shows two derivation approaches: using the $T_{k-1}$-measure and the $T_k$-measure. Explain the key difference: which measure makes the caplet a put on the ZCB, and which measure keeps the discounting inside the expectation?

??? success "Solution to Exercise 4"
    **$T_{k-1}$-measure approach:** Using $P(t_0, T_{k-1})$ as numeraire, the caplet becomes

    $$
    V^{\text{CPL}}(t_0) = \hat{N}\,P(t_0, T_{k-1})\,\mathbb{E}^{T_{k-1}}\!\left[\max(\hat{K} - P(T_{k-1}, T_k),\,0)\,\Big|\,\mathcal{F}(t_0)\right]
    $$

    This is a put option on the ZCB $P(T_{k-1},T_k)$ priced under the $T_{k-1}$-forward measure. The discounting is handled by the numeraire $P(t_0, T_{k-1})$ outside the expectation. The distribution of $r(T_{k-1})$ under this measure uses the drift adjusted by $B(T_{k-1} - t)$.

    **$T_k$-measure approach:** Using $P(t_0, T_k)$ as numeraire, the caplet is

    $$
    V^{\text{CPL}}(t_0) = N\,P(t_0, T_k)\,e^{-A(\tau_k)}\,\mathbb{E}^{T_k}\!\left[\max(e^{-B(\tau_k)r(T_{k-1})} - \hat{K},\,0)\,\Big|\,\mathcal{F}(t_0)\right]
    $$

    Here the discounting uses $P(t_0, T_k)$ and the ZCB price appears as $e^{A(\tau_k)+B(\tau_k)r(T_{k-1})}$ inside the max. The distribution of $r(T_{k-1})$ uses the drift adjusted by $B(T_k - t)$ (note the different maturity in the drift adjustment).

    The key difference: the $T_{k-1}$-measure approach makes the caplet directly a put on $P(T_{k-1},T_k)$ with the discount factor $P(t_0,T_{k-1})$ cleanly outside, while the $T_k$-measure approach keeps the exponential structure inside the expectation and uses $P(t_0,T_k)$ for discounting.

---

**Exercise 5.** Verify the cap-floor parity: $\text{Cap}(t_0) - \text{Floor}(t_0) = \text{IRS}^{\text{Payer}}(t_0)$. Explain why this relationship is model-independent.

??? success "Solution to Exercise 5"
    **Cap-floor parity derivation:** For each individual caplet-floorlet pair:

    $$
    \text{Caplet}_k - \text{Floorlet}_k = N\tau_k\,\mathbb{E}^{\mathbb{Q}}\!\left[\frac{M(t_0)}{M(T_k)}(l_k(T_{k-1}) - K)\,\Big|\,\mathcal{F}(t_0)\right]
    $$

    since $\max(x,0) - \max(-x,0) = x$. The expectation of the forward rate under the $T_k$-forward measure gives $l_k(t_0)$, so:

    $$
    \text{Caplet}_k - \text{Floorlet}_k = N\tau_k\,P(t_0, T_k)(l_k(t_0) - K)
    $$

    Summing over all $k = 1, \ldots, n$ and using $l_k(t_0) = \frac{1}{\tau_k}\!\left(\frac{P(t_0,T_{k-1})}{P(t_0,T_k)} - 1\right)$:

    $$
    \text{Cap} - \text{Floor} = N\sum_{k=1}^n \left(P(t_0,T_{k-1}) - P(t_0,T_k)\right) - NK\sum_{k=1}^n \tau_k P(t_0,T_k)
    $$

    The first sum telescopes to $P(t_0,T_0) - P(t_0,T_n)$, giving:

    $$
    \text{Cap} - \text{Floor} = N(P(t_0,T_0) - P(t_0,T_n)) - NK\sum_{k=1}^n \tau_k P(t_0,T_k) = \text{IRS}^{\text{Payer}}(t_0)
    $$

    **Model independence:** This relationship is model-independent because it follows from the put-call parity for each caplet-floorlet pair, which is a no-arbitrage result. The key identity $\max(x,0) - \max(-x,0) = x$ holds pathwise for every outcome, so no distributional assumptions about $l_k$ are needed. The parity holds in any arbitrage-free model.

---

**Exercise 6.** The Hull-White model parameters affect the implied volatility smile produced by the caplet formula. Describe qualitatively how increasing $\sigma$ and increasing $\lambda$ each affect the level and shape of the implied volatility curve.

??? success "Solution to Exercise 6"
    **Effect of increasing $\sigma$:** Higher Hull-White volatility $\sigma$ increases the overall level of implied volatilities across all strikes. This is because the short rate has larger fluctuations, leading to greater uncertainty in bond prices and forward rates, which translates to higher option prices and hence higher Black implied vols.

    **Effect of increasing $\lambda$:** Higher mean reversion speed $\lambda$ decreases the level of implied volatilities, especially for longer-dated caplets. Mean reversion pulls the short rate toward $\theta(t)$, reducing the conditional variance of $r(T_{k-1})$:

    $$
    v_r^2(t_0, T_{k-1}) = \frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda(T_{k-1} - t_0)})
    $$

    For large $\lambda$, $v_r^2$ saturates at $\frac{\sigma^2}{2\lambda}$, which decreases with $\lambda$. This means the effective volatility of bond prices (and hence forward rates) is reduced.

    **Shape effect:** Since the Hull-White model has a Gaussian short rate, the implied volatility smile (as a function of strike) exhibits a skew. Increasing $\sigma$ amplifies this skew, while increasing $\lambda$ compresses it. The skew arises from the exponential mapping from Gaussian $r$ to bond prices, and stronger mean reversion reduces the range of $r$ values and hence the degree of non-linearity visible in the implied vol surface.

---

**Exercise 7.** In the Python code, the function `compute_Implied_Volatility_using_Black76` backs out Black implied volatilities from Hull-White caplet prices. Explain why the resulting implied vol may depend on the strike $K$, even though the Hull-White model has constant $\sigma$.

??? success "Solution to Exercise 7"
    The Hull-White model has a constant short-rate volatility $\sigma$, but the implied volatility backed out via Black's formula depends on the strike $K$ because the two models assume fundamentally different distributions for the underlying rate.

    **Black's formula** assumes $l_k(T_{k-1})$ is lognormal under $\mathbb{Q}^{T_k}$. A single $\sigma_k^{\text{Black}}$ produces a specific lognormal distribution for $l_k$.

    **The Hull-White model** assumes $r(T_{k-1})$ is Gaussian. The forward LIBOR rate is:

    $$
    l_k(T_{k-1}) = \frac{1}{\tau_k}\!\left(e^{-A(\tau_k) - B(\tau_k)r(T_{k-1})} - 1\right)
    $$

    which is a nonlinear (exponential) function of the Gaussian variable $r(T_{k-1})$. The resulting distribution of $l_k(T_{k-1})$ is not lognormal -- it has different skewness and kurtosis.

    When we compute Hull-White caplet prices at various strikes and invert Black's formula to find the implied volatility, we are fitting a lognormal distribution to match the Hull-White price at each strike separately. Since the true distribution differs from lognormal, a different $\sigma_k^{\text{Black}}$ is needed at each strike:

    - **ATM:** The lognormal and Hull-White distributions agree most closely, so the implied vol is near its "base" level.
    - **OTM/ITM:** The tail probabilities differ between the two distributions, so the implied vol adjusts to compensate, producing a strike-dependent smile or skew.

    This is why `compute_Implied_Volatility_using_Black76` returns a strike-dependent implied vol even though $\sigma$ is constant in the Hull-White model.
