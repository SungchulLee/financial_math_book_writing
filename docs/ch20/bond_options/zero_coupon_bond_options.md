# Hull-White Zero Bond Options

Recall (see [§ HW Short Rate](../short_rate/short_rate_solution.md)): $x(t)$ under $\mathbb{Q}$ solves $dx(t)=-\lambda x(t)dt+\sigma dW^{\mathbb{Q}}(t)$ with $x(0)=0$.

Recall (see [§ HW Measure Change](../measure_change/risk_neutral_measure.md)): under the $T$-forward measure $\mathbb{T}$, $dx(t)=(-B(t,T)\sigma^2-\lambda x(t))dt+\sigma dW^{\mathbb{T}}(t)$, and $r(t)=x(t)+\alpha(t)$ is conditionally normal with mean $\mu^{\mathbb{T}}_r(s,t)$ and variance $\sigma_r^2(s,t)$.

## ZCB Call (α=1) and Put (α=-1)

Let $t_0$, $T$, $T_S$ be current, ZCB option maturity, ZCB maturity, respectively.
For the call:

$$\begin{array}{lllll}
\displaystyle
V^\text{ZCB}(t_0,T)
=
P(t_0,T)e^{A(\tau)}\left[e^{\frac{1}{2}B^2(\tau)\sigma_r^2(t_0,T)+B(\tau)\mu^\mathbb{T}_r(t_0,T)}N(d_1)-K_{\text{hat}}N(d_2)\right]
\end{array}$$

where

$$\begin{array}{lll}
K_{\text{hat}}&=&Ke^{-A(\tau)}\\
a&=&\frac{\log(K_{\text{hat}})-B(\tau)\mu^\mathbb{T}_r(t_0,T)}{B(\tau)\sigma_r(t_0,T)}\\
d_1&=&a-B(\tau)\sigma_r(t_0,T)\\
d_2&=&d_1+B(\tau)\sigma_r(t_0,T)
\end{array}$$

with $\tau = T_S - T$.

???+ note "Proof"

    Risk-neutral pricing (Recall, see [§ Risk-neutral](../../ch04/risk_neutral/martingale_and_no_arbitrage.md)) followed by change to the $T$-forward measure (Recall, see [§ Forward Measure](../../ch19/forward_measures/risk_neutral_measure.md)) gives

    $$
    V^\text{ZCB}(t_0,T)=P(t_0,T)\,\mathbb{E}^T\!\left[\max(\alpha(P(T,T_S)-K),0)\mid{\cal F}(t_0)\right].
    $$

    With $P(T,T_S)=e^{A(\tau)+B(\tau)r(T)}$ (Recall, see [§ HW Bond Pricing](../bond_pricing/bond_price_formula.md)) and $r(T)$ Gaussian under $\mathbb{T}$, the expectation reduces to a lognormal integral, yielding the Black-Scholes-type formula above.

## Discounted Characteristic Function of r(T)

$$\begin{array}{lllll}
\displaystyle
\phi(u;t,T)
=
\mathbb{E}^\mathbb{Q}\left[e^{-\int_t^Tr(t')dt'+iur(T)}\Big{|}{\cal F}(t)\right]
=
e^{A(u,\tau)+B(u,\tau)r(t)}
\end{array}$$

## Hull-White MC Agrees with Hull-White ZCB Option Formula

```python
def main():
    hw = HullWhite(sigma=0.02, lambd=0.02, P=P_market)

    K = 0.95
    T1 = 5.0   # option maturity
    T2 = 10.0  # ZCB maturity

    # Analytic price
    price_analytic = hw.compute_ZCB_Option_Price(K, T1, T2, CP=OptionType.CALL)

    # Monte Carlo price
    t, R, M = hw.generate_sample_paths(num_paths=50_000, num_steps=500, T=T1)
    P_T1_T2 = np.array([hw.compute_ZCB(T1, T2, r) for r in R[:, -1]])
    payoff = np.maximum(P_T1_T2 - K, 0)
    price_mc = np.mean(payoff / M[:, -1])

    print(f"Analytic: {price_analytic:.6f}")
    print(f"Monte Carlo: {price_mc:.6f}")
```

## QuantPie Derivation: Hull-White ZCB Option Formula

Recall (see [§ HW Bond Pricing](../bond_pricing/bond_price_formula.md)): the affine form $P(T,T_S)=e^{A(\tau)+B(\tau)r(T)}$ with $\tau=T_S-T$.

Recall (see [§ HW Named Functions](../named_functions/named_functions_definition.md)): $A(\tau)$, $B(\tau)$ in the negative-$B$ convention $B(\tau)=(e^{-\lambda\tau}-1)/\lambda<0$.

Recall (see [§ HW Measure Change](../measure_change/risk_neutral_measure.md)): under $\mathbb{Q}^T$, $r(T)\mid r(t_0)\sim N(\mu_r(t_0,T),v_r^2(t_0,T))$ with $v_r^2(t_0,T)=-\frac{\sigma^2}{2\lambda}(e^{-2\lambda(T-t_0)}-1)$.

The derivation: change to the $T$-forward measure (Recall, see [§ Forward Measure](../../ch19/forward_measures/risk_neutral_measure.md)), substitute the affine form, and evaluate the resulting one-dimensional Gaussian integral with $\hat{K}=Ke^{-A(\tau)}$ (a Black-Scholes-type computation, Recall, see [§ ch06](../../ch06/index.md)). The integration domain becomes $z<a$ because $B(\tau)<0$ flips the inequality. The result coincides with the formula displayed in the previous section.

---

## Exercises

**Exercise 1.** Consider a Hull-White model with $\sigma = 0.02$, $\lambda = 0.05$, and a flat forward rate curve $f^M(0,t) = 0.04$. A European call option on a zero-coupon bond has option maturity $T = 3$ years, ZCB maturity $T_S = 8$ years, and strike $K = 0.80$. Compute $B(\tau)$ where $\tau = T_S - T$, and verify that $B(\tau) < 0$.

??? success "Solution to Exercise 1"
    We have $\tau = T_S - T = 8 - 3 = 5$ years and $\lambda = 0.05$. The function $B(\tau)$ is

    $$
    B(\tau) = \frac{e^{-\lambda\tau} - 1}{\lambda} = \frac{e^{-0.05 \times 5} - 1}{0.05} = \frac{e^{-0.25} - 1}{0.05}
    $$

    Computing $e^{-0.25} \approx 0.7788$:

    $$
    B(5) = \frac{0.7788 - 1}{0.05} = \frac{-0.2212}{0.05} = -4.4240
    $$

    To verify $B(\tau) < 0$: for any $\tau > 0$, we have $0 < e^{-\lambda\tau} < 1$, so $e^{-\lambda\tau} - 1 < 0$. Since $\lambda > 0$, the ratio $(e^{-\lambda\tau} - 1)/\lambda < 0$. Therefore $B(\tau) < 0$ for all $\tau > 0$.

---

**Exercise 2.** Starting from the risk-neutral pricing formula

$$
V^{\text{ZCB}}(t_0, T) = \mathbb{E}^{\mathbb{Q}}\!\left[\frac{M(t_0)}{M(T)}\max\!\left(P(T,T_S) - K, 0\right)\,\Big|\,\mathcal{F}(t_0)\right]
$$

show that the change of numeraire from the money market account to the $T$-maturity bond yields

$$
V^{\text{ZCB}}(t_0, T) = P(t_0, T)\,\mathbb{E}^{T}\!\left[\max\!\left(P(T,T_S) - K, 0\right)\,\Big|\,\mathcal{F}(t_0)\right]
$$

Explain why this step simplifies the computation.

??? success "Solution to Exercise 2"
    Starting from the risk-neutral pricing formula:

    $$
    V^{\text{ZCB}}(t_0, T) = \mathbb{E}^{\mathbb{Q}}\!\left[\frac{M(t_0)}{M(T)}\max(P(T,T_S) - K, 0)\,\Big|\,\mathcal{F}(t_0)\right]
    $$

    The Radon–Nikodym derivative for the change from $\mathbb{Q}$ to the $T$-forward measure $\mathbb{Q}^T$ is

    $$
    \frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_{\mathcal{F}(T)} = \frac{P(T,T)}{P(t_0,T) \cdot M(T)/M(t_0)} = \frac{1}{P(t_0,T)} \cdot \frac{M(t_0)}{M(T)}
    $$

    Wait -- more directly, the $T$-forward measure $\mathbb{Q}^T$ uses $P(t, T)$ as numeraire. By the abstract Bayes formula, for any $\mathcal{F}(T)$-measurable payoff $X$:

    $$
    \mathbb{E}^{\mathbb{Q}}\!\left[\frac{M(t_0)}{M(T)} X\,\Big|\,\mathcal{F}(t_0)\right] = P(t_0, T)\,\mathbb{E}^{T}\!\left[X\,\Big|\,\mathcal{F}(t_0)\right]
    $$

    This is because $M(t_0)/M(T) = e^{-\int_{t_0}^T r(s)\,ds}$ is the stochastic discount factor, and the forward measure is defined precisely so that the bond $P(t,T)$ serves as the numeraire. Setting $X = \max(P(T,T_S) - K, 0)$:

    $$
    V^{\text{ZCB}}(t_0, T) = P(t_0, T)\,\mathbb{E}^{T}\!\left[\max(P(T,T_S) - K, 0)\,\Big|\,\mathcal{F}(t_0)\right]
    $$

    This simplifies the computation because under $\mathbb{Q}^T$, we no longer need to handle the stochastic discount factor $M(t_0)/M(T)$ inside the expectation. The payoff depends only on $r(T)$ (through $P(T,T_S)$), and $r(T)$ is normally distributed under $\mathbb{Q}^T$. This reduces the problem to a one-dimensional Gaussian integral, yielding the Black-Scholes-type formula directly.

---

**Exercise 3.** In the ZCB option formula, the integration boundary $a$ satisfies $e^{B(\tau)\mu_r(t_0,T) + B(\tau)v_r(t_0,T)z} > \hat{K}$ for $z < a$. Explain why the inequality direction reverses (compared to a standard Black-Scholes call) and relate this to the sign of $B(\tau)$.

??? success "Solution to Exercise 3"
    In the standard Black-Scholes call option on a stock, the payoff $\max(S_T - K, 0)$ is positive when $S_T > K$. Since $S_T = S_0 e^{(\mu - \sigma^2/2)T + \sigma\sqrt{T}z}$ is increasing in $z$, the integration region is $z > a$ for some boundary $a$.

    In the ZCB option, the payoff involves $P(T, T_S) = e^{A(\tau) + B(\tau)r(T)}$, and $B(\tau) < 0$. The bond price is a **decreasing** function of $r(T)$. Writing $r(T) = \mu_r^T + v_r z$ where $z \sim N(0,1)$ under $\mathbb{Q}^T$:

    $$
    e^{B(\tau)r(T)} = e^{B(\tau)\mu_r^T + B(\tau)v_r z}
    $$

    Since $B(\tau) < 0$, the exponent $B(\tau)v_r z$ is **decreasing** in $z$ (as $v_r > 0$). Therefore $P(T, T_S) > K$ corresponds to $B(\tau)v_r z > \log\hat{K} - B(\tau)\mu_r^T$, which gives:

    $$
    z < \frac{\log\hat{K} - B(\tau)\mu_r^T}{B(\tau)v_r} = a
    $$

    The inequality direction is $z < a$ (rather than $z > a$) because dividing by $B(\tau)v_r < 0$ reverses the inequality. This is why the integration runs from $-\infty$ to $a$ in the proof, opposite to the standard Black-Scholes case.

---

**Exercise 4.** Derive the put option price $V^{\text{ZCB,put}}(t_0, T)$ on a zero-coupon bond using put-call parity for bond options. Verify that the parity relation takes the form

$$
V^{\text{ZCB,call}} - V^{\text{ZCB,put}} = P(t_0, T_S) - K\,P(t_0, T)
$$

??? success "Solution to Exercise 4"
    The put option payoff is $\max(K - P(T, T_S), 0)$. By put-call parity for European options on a zero-coupon bond, the forward price of $P(T, T_S)$ at time $T$ under the $T$-forward measure is $P(t_0, T_S)/P(t_0, T)$. Therefore:

    $$
    V^{\text{ZCB,call}} - V^{\text{ZCB,put}} = P(t_0, T)\,\mathbb{E}^T\!\left[P(T, T_S) - K\,\Big|\,\mathcal{F}(t_0)\right]
    $$

    Under the $T$-forward measure, $P(T, T_S)/P(T, T) = P(T, T_S)$ is a martingale relative to the numeraire $P(t, T)$. Therefore:

    $$
    \mathbb{E}^T\!\left[P(T, T_S)\,\Big|\,\mathcal{F}(t_0)\right] = \frac{P(t_0, T_S)}{P(t_0, T)}
    $$

    Substituting:

    $$
    V^{\text{ZCB,call}} - V^{\text{ZCB,put}} = P(t_0, T)\left(\frac{P(t_0, T_S)}{P(t_0, T)} - K\right) = P(t_0, T_S) - K\,P(t_0, T)
    $$

    This confirms the put-call parity relation. The put price can therefore be obtained from the call price as:

    $$
    V^{\text{ZCB,put}} = V^{\text{ZCB,call}} - P(t_0, T_S) + K\,P(t_0, T)
    $$

---

**Exercise 5.** Using the Monte Carlo code provided, explain why the discount factor used is $1/M[:, -1]$ rather than $e^{-rT}$. What would happen to the Monte Carlo estimate if the number of paths were reduced from 50,000 to 500? Discuss the convergence behavior.

??? success "Solution to Exercise 5"
    The discount factor $1/M[:, -1]$ is used rather than $e^{-rT}$ because the interest rate $r(t)$ is stochastic in the Hull-White model. The money market account at time $T$ is:

    $$
    M(T) = \exp\!\left(\int_0^T r(t')\,dt'\right)
    $$

    This is path-dependent -- it depends on the entire trajectory of $r(t)$, not just the terminal value. The discount factor from $T$ back to $t_0 = 0$ is $M(0)/M(T) = 1/M(T)$. Using $e^{-rT}$ with a fixed $r$ would be incorrect because $r$ varies along each path.

    In the Monte Carlo simulation, `M[:, -1]` represents $M(T_1)$ for each path, accumulated as $M(T_1) = \exp(\sum_{i} r(t_i)\Delta t)$ along the discretized path.

    **Convergence with 500 paths:** Reducing from 50,000 to 500 paths increases the standard error by a factor of $\sqrt{50000/500} = 10$. If the standard error at 50,000 paths is approximately $\varepsilon$, at 500 paths it becomes $10\varepsilon$. For a typical ZCB option price, this means the relative error increases from roughly 0.5% to 5%, making the estimate unreliable for practical pricing. The Monte Carlo estimator converges at rate $O(1/\sqrt{N})$, so achieving the same accuracy with 500 paths is impossible without variance reduction techniques.

---

**Exercise 6.** Show that in the limit $\lambda \to 0$ (no mean reversion), the variance $v_r^2(t_0, T)$ reduces to $\sigma^2(T - t_0)$ and $B(\tau)$ reduces to $-\tau$. Interpret this limiting case in terms of the Ho-Lee model.

??? success "Solution to Exercise 6"
    Taking $\lambda \to 0$ in the variance formula:

    $$
    v_r^2(t_0, T) = -\frac{\sigma^2}{2\lambda}\left(e^{-2\lambda(T-t_0)} - 1\right) = \frac{\sigma^2}{2\lambda}\left(1 - e^{-2\lambda(T-t_0)}\right)
    $$

    Using the Taylor expansion $e^{-2\lambda(T-t_0)} \approx 1 - 2\lambda(T-t_0) + O(\lambda^2)$:

    $$
    v_r^2(t_0, T) \approx \frac{\sigma^2}{2\lambda} \cdot 2\lambda(T - t_0) = \sigma^2(T - t_0)
    $$

    For $B(\tau)$:

    $$
    B(\tau) = \frac{e^{-\lambda\tau} - 1}{\lambda}
    $$

    Using $e^{-\lambda\tau} \approx 1 - \lambda\tau + O(\lambda^2)$:

    $$
    B(\tau) \approx \frac{(1 - \lambda\tau) - 1}{\lambda} = -\tau
    $$

    In the Ho-Lee model, $dr(t) = \theta(t)\,dt + \sigma\,dW(t)$ (no mean reversion). The short rate is a Brownian motion with drift, so $r(T) - r(t_0)$ has variance $\sigma^2(T - t_0)$ and the bond price sensitivity to $r$ over a horizon $\tau$ is linear: $B(\tau) = -\tau$. The Hull-White model with $\lambda = 0$ is exactly the Ho-Lee model, and the formulas above confirm this correspondence.

---

**Exercise 7.** Consider the discounted characteristic function $\phi(u; t, T) = e^{A(u,\tau) + B(u,\tau)r(t)}$. Show that setting $u = 0$ recovers the zero-coupon bond price $P(t,T)$, and explain why $\phi$ can be used for Fourier-based option pricing in the Hull-White model.

??? success "Solution to Exercise 7"
    Setting $u = 0$ in the discounted characteristic function:

    $$
    \phi(0; t, T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r(t')\,dt' + i \cdot 0 \cdot r(T)}\,\Big|\,\mathcal{F}(t)\right] = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r(t')\,dt'}\,\Big|\,\mathcal{F}(t)\right]
    $$

    This is precisely the definition of the zero-coupon bond price:

    $$
    \phi(0; t, T) = P(t, T)
    $$

    Since the Hull-White model is affine, $\phi(0; t, T) = e^{A(0, \tau) + B(0, \tau)r(t)}$, and the functions $A(0, \tau)$ and $B(0, \tau)$ must coincide with the bond pricing functions.

    The discounted characteristic function $\phi(u; t, T)$ is useful for Fourier-based option pricing because it encodes both the discounting and the distribution of $r(T)$ in a single object. For a European option with payoff $g(r(T))$, the price is:

    $$
    V(t) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r(t')\,dt'} g(r(T))\,\Big|\,\mathcal{F}(t)\right]
    $$

    If $\hat{g}$ is the Fourier transform of $g$, then by the Fourier inversion theorem:

    $$
    V(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} \hat{g}(-u)\,\phi(u; t, T)\,du
    $$

    Since $\phi$ has the closed-form exponential-affine structure $e^{A(u,\tau) + B(u,\tau)r(t)}$ in the Hull-White model, this integral can be evaluated efficiently using FFT or numerical quadrature, providing a fast alternative to Monte Carlo for pricing interest rate derivatives.
