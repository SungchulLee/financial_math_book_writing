# Stock-Price Numeraire Measure

The stock-price numeraire measure $\mathbb{Q}^S$ uses the stock price $S_t$ as the numeraire instead of the money-market account $B_t = e^{rt}$. Under $\mathbb{Q}^S$, the probability $P_1 = \mathbb{Q}^S(S_T > K)$ appears naturally in the Heston call pricing formula as the delta-related component $C = S_0 e^{-q\tau} P_1 - K e^{-r\tau} P_2$. This section derives the measure change from $\mathbb{Q}$ to $\mathbb{Q}^S$, obtains the Heston characteristic function under the new measure, and applies it to price digital calls and compute the probability $P_1$.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the Radon-Nikodym derivative for the change from $\mathbb{Q}$ to $\mathbb{Q}^S$
    2. Obtain the Heston SDE and characteristic function under $\mathbb{Q}^S$
    3. Relate $P_1$ to the exercise probability under the stock-price numeraire
    4. Apply the $\mathbb{Q}^S$ framework to price asset-or-nothing digital calls

---

## Intuition

In the Black-Scholes model, the call formula $C = S_0 N(d_1) - K e^{-rT} N(d_2)$ involves two probabilities: $N(d_2) = \mathbb{Q}(S_T > K)$ is the exercise probability under the risk-neutral measure, while $N(d_1) = \mathbb{Q}^S(S_T > K)$ is the exercise probability under the stock-price numeraire. The second probability weights outcomes by the stock price, making high-stock-price states more likely. In the Heston model, this measure change transforms the variance dynamics: the mean-reversion speed decreases by $\rho\xi$ (since high stock prices correlate with low variance through $\rho < 0$), tilting the variance distribution.

---

## Numeraire Change: General Theory

Let $N_t$ be a positive $\mathbb{Q}$-martingale (after discounting). The numeraire measure $\mathbb{Q}^N$ associated with numeraire $N_t$ is defined by the Radon-Nikodym derivative

$$
\frac{d\mathbb{Q}^N}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{N_T / N_0}{B_T / B_0}
$$

where $B_t = e^{rt}$ is the money-market account.

!!! info "Proposition (Stock-Price Numeraire)"
    For the stock-price numeraire $N_t = S_t e^{qt}$ (the reinvested stock), the Radon-Nikodym derivative is

    $$
    \frac{d\mathbb{Q}^S}{d\mathbb{Q}}\bigg|_{\mathcal{F}_T} = \frac{S_T e^{qT}}{S_0 e^{qT} \cdot e^{(r-q)T}} \cdot \frac{B_0}{1} = \frac{S_T}{S_0 e^{(r-q)T}}
    $$

    where we used the fact that the discounted reinvested stock $S_t e^{qt}/B_t$ is a $\mathbb{Q}$-martingale.

---

## Girsanov Shift for the Stock-Price Numeraire

Under $\mathbb{Q}$, the stock dynamics are

$$
dS_t = (r - q)S_t \, dt + \sqrt{v_t} \, S_t \, dW_t^{(1), \mathbb{Q}}
$$

The Radon-Nikodym density process is

$$
Z_t = \frac{S_t}{S_0 e^{(r-q)t}} = \mathcal{E}\!\left(\int_0^t \sqrt{v_s} \, dW_s^{(1),\mathbb{Q}}\right)
$$

where $\mathcal{E}$ denotes the stochastic exponential. By Girsanov's theorem:

$$
dW_t^{(1), \mathbb{Q}^S} = dW_t^{(1), \mathbb{Q}} - \sqrt{v_t} \, dt
$$

$$
dW_t^{(2), \mathbb{Q}^S} = dW_t^{(2), \mathbb{Q}} - \rho\sqrt{v_t} \, dt
$$

The second equation follows because $W^{(2),\mathbb{Q}}$ has correlation $\rho$ with $W^{(1),\mathbb{Q}}$, so the Girsanov drift for $W^{(2)}$ picks up a factor of $\rho$.

---

## Heston Dynamics Under the Stock-Price Numeraire

Substituting the Girsanov shifts into the $\mathbb{Q}$-dynamics:

**Stock price:**

$$
dS_t = (r - q)S_t \, dt + \sqrt{v_t} S_t \left(dW_t^{(1),\mathbb{Q}^S} + \sqrt{v_t} \, dt\right)
$$

$$
= (r - q + v_t) S_t \, dt + \sqrt{v_t} S_t \, dW_t^{(1), \mathbb{Q}^S}
$$

**Variance:**

$$
dv_t = \kappa(\theta - v_t) \, dt + \xi\sqrt{v_t}\left(dW_t^{(2),\mathbb{Q}^S} + \rho\sqrt{v_t}\,dt\right)
$$

$$
= \left[\kappa\theta - (\kappa - \rho\xi)v_t\right] dt + \xi\sqrt{v_t} \, dW_t^{(2),\mathbb{Q}^S}
$$

!!! info "Theorem (Heston Under Stock-Price Numeraire)"
    Under $\mathbb{Q}^S$, the Heston dynamics are

    $$
    dS_t = (r - q + v_t) S_t \, dt + \sqrt{v_t} S_t \, dW_t^{(1), \mathbb{Q}^S}
    $$

    $$
    dv_t = \kappa^*(\theta^* - v_t) \, dt + \xi\sqrt{v_t} \, dW_t^{(2), \mathbb{Q}^S}
    $$

    with modified mean-reversion parameters:

    $$
    \kappa^* = \kappa - \rho\xi, \qquad \theta^* = \frac{\kappa\theta}{\kappa - \rho\xi}
    $$

    The vol-of-vol $\xi$ and correlation $\rho$ are unchanged.

!!! note "Effect of Negative Correlation"
    For the empirically relevant case $\rho < 0$: $\kappa^* = \kappa + |\rho|\xi > \kappa$ (faster mean reversion) and $\theta^* = \kappa\theta/(\kappa + |\rho|\xi) < \theta$ (lower long-run variance). This makes intuitive sense: the $\mathbb{Q}^S$ measure weights high-stock-price scenarios more heavily, and negative correlation implies these scenarios have lower variance.

---

## Characteristic Function Under the Stock-Price Numeraire

The CF of $\log S_T$ under $\mathbb{Q}^S$ has the same affine structure but with modified parameters.

!!! info "Proposition (CF Under Stock-Price Numeraire)"
    The characteristic function under $\mathbb{Q}^S$ is

    $$
    \varphi_1(u) = \exp\bigl(C_1(\tau, u) + D_1(\tau, u) v_0 + iu\log S_0\bigr)
    $$

    where $C_1$ and $D_1$ solve the same Riccati system as the $\mathbb{Q}$-CF but with $\kappa$ replaced by $\kappa^* = \kappa - \rho\xi$ and $\theta$ replaced by $\theta^* = \kappa\theta/\kappa^*$.

    Alternatively, $\varphi_1$ can be obtained from the $\mathbb{Q}$-CF by the **shift formula**:

    $$
    \varphi_1(u) = \frac{\varphi(u - i)}{S_0 e^{(r-q)\tau}}
    $$

    where $\varphi$ is the standard Heston CF under $\mathbb{Q}$.

**Proof of the shift formula.** By definition:

$$
\varphi_1(u) = \mathbb{E}^{\mathbb{Q}^S}[e^{iu\log S_T}] = \mathbb{E}^{\mathbb{Q}}\!\left[\frac{S_T}{S_0 e^{(r-q)\tau}} e^{iu\log S_T}\right] = \frac{\mathbb{E}^{\mathbb{Q}}[e^{(iu+1)\log S_T}]}{S_0 e^{(r-q)\tau}}
$$

$$
= \frac{\varphi(u - i)}{S_0 e^{(r-q)\tau}}
$$

where we used $e^{\log S_T} e^{iu\log S_T} = e^{i(u-i)\log S_T}$ and $\varphi(u-i) = \mathbb{E}^{\mathbb{Q}}[e^{i(u-i)\log S_T}]$. $\square$

---

## Application: Exercise Probability P1

The European call price decomposes as

$$
C = S_0 e^{-q\tau} P_1 - K e^{-r\tau} P_2
$$

where $P_2 = \mathbb{Q}(S_T > K)$ and $P_1 = \mathbb{Q}^S(S_T > K)$.

The Gil-Pelaez formula gives

$$
P_1 = \frac{1}{2} + \frac{1}{\pi}\int_0^{\infty} \text{Re}\!\left[\frac{e^{-iu\log K}\varphi_1(u)}{iu}\right] du
$$

Since $\varphi_1(u) = \varphi(u-i)/(S_0 e^{(r-q)\tau})$, this can be evaluated using the same Heston CF code with a shifted argument.

!!! tip "Implementation Note"
    To compute $P_1$ from $\varphi$, evaluate $\varphi(u - i)$ for real $u$. This requires the CF at a complex argument with imaginary part $-1$. The Albrecher stable formulation handles this without modification, since the stability condition $|g| < 1$ extends to complex arguments satisfying $\text{Im}(u) \geq -1$ (which corresponds to the existence of the first moment $\mathbb{E}^{\mathbb{Q}}[S_T] < \infty$).

---

## Application: Asset-or-Nothing Digital Call

An asset-or-nothing call pays $S_T$ if $S_T > K$ and zero otherwise. Its price is

$$
V_{\text{AoN}} = e^{-r\tau} \mathbb{E}^{\mathbb{Q}}[S_T \mathbf{1}_{S_T > K}] = S_0 e^{-q\tau} \mathbb{Q}^S(S_T > K) = S_0 e^{-q\tau} P_1
$$

This shows that the $\mathbb{Q}^S$ measure is the natural pricing measure for asset-contingent payoffs.

---

## Numerical Example

Using $S_0 = 100$, $K = 100$, $r = 0.05$, $q = 0$, $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$, $\tau = 1$.

**Risk-neutral parameters ($\mathbb{Q}$):** $\kappa = 1.5$, $\theta = 0.04$.

**Stock-numeraire parameters ($\mathbb{Q}^S$):**

$$
\kappa^* = 1.5 - (-0.7)(0.3) = 1.5 + 0.21 = 1.71
$$

$$
\theta^* = \frac{1.5 \times 0.04}{1.71} = 0.0351
$$

**Probabilities:**

$$
P_2 = \mathbb{Q}(S_T > K) = 0.5134
$$

$$
P_1 = \mathbb{Q}^S(S_T > K) = 0.5748
$$

Note that $P_1 > P_2$ always holds for $r > q$, because the $\mathbb{Q}^S$ measure weights high-stock-price outcomes more heavily.

**Option prices:**

$$
C = 100(0.5748) - 100 e^{-0.05}(0.5134) = 57.48 - 48.85 = 8.63
$$

$$
\text{Asset-or-nothing call} = S_0 P_1 = 100 \times 0.5748 = 57.48
$$

$$
\text{Cash-or-nothing call} = e^{-r\tau} P_2 = 0.9512 \times 0.5134 = 0.4884
$$

??? example "Delta Interpretation"
    The delta of the European call is

    $$
    \Delta = e^{-q\tau} P_1 = 0.5748
    $$

    This is the expected value under $\mathbb{Q}^S$ of the exercise indicator. The delta is always between 0 and 1 for calls (and between $-1$ and 0 for puts), and it equals $P_1$ when $q = 0$.

---

## Summary

The stock-price numeraire measure $\mathbb{Q}^S$ is obtained from the risk-neutral measure $\mathbb{Q}$ by the Radon-Nikodym derivative $d\mathbb{Q}^S/d\mathbb{Q} = S_T / (S_0 e^{(r-q)\tau})$. Under $\mathbb{Q}^S$, the Heston variance process has modified mean-reversion parameters $\kappa^* = \kappa - \rho\xi$ and $\theta^* = \kappa\theta/\kappa^*$, while $\xi$ and $\rho$ are unchanged. The characteristic function under $\mathbb{Q}^S$ is obtained either by solving the Riccati system with modified parameters or by the shift formula $\varphi_1(u) = \varphi(u-i)/(S_0 e^{(r-q)\tau})$. The probability $P_1 = \mathbb{Q}^S(S_T > K)$ is the delta of the call (when $q = 0$) and prices asset-or-nothing digital options. The $\mathbb{Q}^S$ framework completes the two-probability decomposition of the Heston call price.

---

## Exercises

**Exercise 1.**
The Radon-Nikodym derivative is $d\mathbb{Q}^S/d\mathbb{Q} = S_T/(S_0 e^{(r-q)\tau})$. Verify that $\mathbb{E}^{\mathbb{Q}}[d\mathbb{Q}^S/d\mathbb{Q}] = 1$ by using the fact that $\mathbb{E}^{\mathbb{Q}}[S_T] = S_0 e^{(r-q)\tau}$ (the discounted stock is a $\mathbb{Q}$-martingale). Why is this expectation-one property necessary for $\mathbb{Q}^S$ to be a valid probability measure?

??? success "Solution to Exercise 1"
    We compute

    $$
    \mathbb{E}^{\mathbb{Q}}\!\left[\frac{d\mathbb{Q}^S}{d\mathbb{Q}}\right] = \mathbb{E}^{\mathbb{Q}}\!\left[\frac{S_T}{S_0 e^{(r-q)\tau}}\right] = \frac{\mathbb{E}^{\mathbb{Q}}[S_T]}{S_0 e^{(r-q)\tau}}
    $$

    Under $\mathbb{Q}$, the discounted reinvested stock price $e^{-(r-q)t}S_t$ is a martingale (since $dS_t = (r-q)S_t\,dt + \sqrt{v_t}S_t\,dW_t^{(1),\mathbb{Q}}$), so

    $$
    \mathbb{E}^{\mathbb{Q}}[S_T] = S_0 e^{(r-q)\tau}
    $$

    Therefore

    $$
    \mathbb{E}^{\mathbb{Q}}\!\left[\frac{d\mathbb{Q}^S}{d\mathbb{Q}}\right] = \frac{S_0 e^{(r-q)\tau}}{S_0 e^{(r-q)\tau}} = 1
    $$

    **Why this is necessary.** For $\mathbb{Q}^S$ to be a valid probability measure, it must assign total mass 1 to the sample space $\Omega$. The Radon-Nikodym derivative $Z = d\mathbb{Q}^S/d\mathbb{Q}$ defines $\mathbb{Q}^S$ via $\mathbb{Q}^S(A) = \mathbb{E}^{\mathbb{Q}}[Z\cdot\mathbf{1}_A]$ for any event $A$. For the full space $A = \Omega$:

    $$
    \mathbb{Q}^S(\Omega) = \mathbb{E}^{\mathbb{Q}}[Z] = 1
    $$

    If $\mathbb{E}^{\mathbb{Q}}[Z] \neq 1$, then $\mathbb{Q}^S$ would not be a probability measure. Additionally, $Z$ must be strictly positive almost surely for $\mathbb{Q}^S$ to be equivalent to $\mathbb{Q}$ (not just absolutely continuous). Since $S_T > 0$ almost surely in the Heston model (the geometric Brownian motion with stochastic volatility preserves positivity), $Z > 0$ a.s., confirming equivalence.

---

**Exercise 2.**
Under $\mathbb{Q}^S$, the variance parameters change to $\kappa^* = \kappa - \rho\xi$ and $\theta^* = \kappa\theta/\kappa^*$. For $\rho = -0.7$, $\xi = 0.3$, $\kappa = 1.5$, $\theta = 0.04$, verify the numerical example values $\kappa^* = 1.71$ and $\theta^* = 0.0351$. Now consider $\rho = +0.5$ (positive correlation). Compute $\kappa^*$ and $\theta^*$ and explain why the mean-reversion speed decreases and the long-run variance increases in this case.

??? success "Solution to Exercise 2"
    **Verification for $\rho = -0.7$:**

    $$
    \kappa^* = \kappa - \rho\xi = 1.5 - (-0.7)(0.3) = 1.5 + 0.21 = 1.71
    $$

    $$
    \theta^* = \frac{\kappa\theta}{\kappa^*} = \frac{1.5 \times 0.04}{1.71} = \frac{0.06}{1.71} = 0.0351
    $$

    Both match the numerical example.

    **For $\rho = +0.5$:**

    $$
    \kappa^* = 1.5 - (0.5)(0.3) = 1.5 - 0.15 = 1.35
    $$

    $$
    \theta^* = \frac{1.5 \times 0.04}{1.35} = \frac{0.06}{1.35} = 0.0444
    $$

    The mean-reversion speed **decreases** ($\kappa^* = 1.35 < \kappa = 1.5$) and the long-run variance **increases** ($\theta^* = 0.0444 > \theta = 0.04$).

    **Explanation.** The stock-price numeraire $\mathbb{Q}^S$ weights high-stock-price outcomes more heavily. The sign of the effect on variance parameters depends on the correlation $\rho$:

    - When $\rho < 0$ (leverage effect): high stock prices are associated with low variance. Under $\mathbb{Q}^S$, these low-variance states get more weight, so $\theta^*$ decreases and $\kappa^*$ increases (faster reversion to a lower level).
    - When $\rho > 0$ (positive correlation): high stock prices are associated with high variance. Under $\mathbb{Q}^S$, these high-variance states get more weight, so $\theta^*$ increases and $\kappa^*$ decreases (slower reversion to a higher level).

    The formula $\kappa^* = \kappa - \rho\xi$ makes this transparent: when $\rho > 0$, the subtracted term is positive, reducing $\kappa^*$.

---

**Exercise 3.**
The shift formula states $\varphi_1(u) = \varphi(u - i)/(S_0 e^{(r-q)\tau})$, which requires evaluating the Heston CF at $u - i$ (a complex argument with imaginary part $-1$). Show that this evaluation is well-defined provided $\mathbb{E}^{\mathbb{Q}}[S_T] < \infty$, which is equivalent to the first moment condition. What happens if you try to compute $\varphi(u - 2i)$, corresponding to $\mathbb{E}^{\mathbb{Q}}[S_T^2]$? Under what Heston parameter condition does this second moment exist?

??? success "Solution to Exercise 3"
    The shift formula requires evaluating $\varphi(u - i)$, which involves $\mathbb{E}^{\mathbb{Q}}[e^{i(u-i)\log S_T}] = \mathbb{E}^{\mathbb{Q}}[e^{iu\log S_T + \log S_T}] = \mathbb{E}^{\mathbb{Q}}[S_T e^{iu\log S_T}]$.

    For this to be well-defined, we need $\mathbb{E}^{\mathbb{Q}}[S_T] < \infty$. In the Heston model, $S_T$ has a lognormal-like distribution with stochastic variance, and $\mathbb{E}^{\mathbb{Q}}[S_T] = S_0 e^{(r-q)\tau} < \infty$. This is the first moment condition, and it is always satisfied because $S_t$ is a $\mathbb{Q}$-martingale after discounting.

    **For $\varphi(u - 2i)$:** This requires evaluating

    $$
    \varphi(u - 2i) = \mathbb{E}^{\mathbb{Q}}[e^{i(u-2i)\log S_T}] = \mathbb{E}^{\mathbb{Q}}[S_T^2 e^{iu\log S_T}]
    $$

    At $u = 0$, this gives $\mathbb{E}^{\mathbb{Q}}[S_T^2]$, the second moment of the stock price. In the Heston model, this exists if and only if the Riccati ODE for $D(\tau, u)$ does not explode when evaluated at $u = -2i$ (i.e., with the substitution $iu \to 2$).

    The relevant condition involves the discriminant of the Riccati equation. The characteristic exponent $D(\tau, u)$ solves

    $$
    \frac{dD}{d\tau} = \frac{1}{2}(iu)^2 - \frac{1}{2}(iu) + [\rho\xi(iu) - \kappa]D + \frac{1}{2}\xi^2 D^2
    $$

    Setting $w = iu$, for the second moment we need $w = 2$. The discriminant is

    $$
    d = (\kappa - \rho\xi w)^2 - \xi^2(w^2 - w) = (\kappa - 2\rho\xi)^2 - \xi^2(4 - 2) = (\kappa - 2\rho\xi)^2 - 2\xi^2
    $$

    The second moment exists for all $\tau > 0$ provided $D(\tau)$ remains finite, which requires $\kappa - 2\rho\xi > \xi\sqrt{2}$ (or more precisely, that the Riccati ODE does not blow up on $[0, \tau]$). For the numerical parameters $\kappa = 1.5$, $\rho = -0.7$, $\xi = 0.3$:

    $$
    \kappa - 2\rho\xi = 1.5 - 2(-0.7)(0.3) = 1.5 + 0.42 = 1.92
    $$

    $$
    \xi\sqrt{2} = 0.3\sqrt{2} = 0.424
    $$

    Since $1.92 > 0.424$, the second moment exists. In general, the condition for the $n$-th moment $\mathbb{E}^{\mathbb{Q}}[S_T^n] < \infty$ becomes more restrictive as $n$ increases, eventually failing for sufficiently large $n$ (the moment explosion phenomenon studied by Andersen and Piterbarg, 2007).

---

**Exercise 4.**
For a European put, $\Delta_{\text{put}} = e^{-q\tau}(P_1 - 1)$ where $P_1 = \mathbb{Q}^S(S_T > K)$. Using the numerical example ($P_1 = 0.5748$, $q = 0$), compute $\Delta_{\text{put}}$ and verify that $\Delta_{\text{call}} - \Delta_{\text{put}} = e^{-q\tau}$ (put-call parity for deltas).

??? success "Solution to Exercise 4"
    **Put delta:**

    $$
    \Delta_{\text{put}} = e^{-q\tau}(P_1 - 1) = (1)(0.5748 - 1) = -0.4252
    $$

    **Verification of put-call parity for deltas:**

    $$
    \Delta_{\text{call}} - \Delta_{\text{put}} = e^{-q\tau}P_1 - e^{-q\tau}(P_1 - 1) = e^{-q\tau}P_1 - e^{-q\tau}P_1 + e^{-q\tau} = e^{-q\tau}
    $$

    Numerically: $0.5748 - (-0.4252) = 1.0000 = e^{-0\cdot 1} = e^{-q\tau}$. Confirmed.

    This follows from put-call parity at the price level: $C - P = S_0 e^{-q\tau} - Ke^{-r\tau}$. Differentiating with respect to $S_0$:

    $$
    \frac{\partial C}{\partial S_0} - \frac{\partial P}{\partial S_0} = e^{-q\tau}
    $$

    which gives $\Delta_{\text{call}} - \Delta_{\text{put}} = e^{-q\tau}$. When $q = 0$, the call and put deltas always sum to 1 in absolute value.

---

**Exercise 5.**
The $\mathbb{Q}^S$ measure weights high-stock-price outcomes more heavily, so $P_1 > P_2$ when $r > q$. Show this rigorously: $P_1 - P_2 = \mathbb{E}^{\mathbb{Q}}[(S_T/(S_0 e^{(r-q)\tau}) - 1)\mathbf{1}_{S_T > K}] > 0$. Why is the inequality strict? What happens to $P_1 - P_2$ as the strike $K \to \infty$ (deep OTM call)?

??? success "Solution to Exercise 5"
    We compute $P_1 - P_2$ using the definition of $\mathbb{Q}^S$:

    $$
    P_1 - P_2 = \mathbb{Q}^S(S_T > K) - \mathbb{Q}(S_T > K)
    $$

    $$
    = \mathbb{E}^{\mathbb{Q}}\!\left[\frac{S_T}{S_0 e^{(r-q)\tau}}\mathbf{1}_{S_T > K}\right] - \mathbb{E}^{\mathbb{Q}}[\mathbf{1}_{S_T > K}]
    $$

    $$
    = \mathbb{E}^{\mathbb{Q}}\!\left[\left(\frac{S_T}{S_0 e^{(r-q)\tau}} - 1\right)\mathbf{1}_{S_T > K}\right]
    $$

    **Why this is strictly positive when $r > q$.** On the event $\{S_T > K\}$, the stock price is above the strike. The integrand $\left(\frac{S_T}{S_0 e^{(r-q)\tau}} - 1\right)\mathbf{1}_{S_T > K}$ can be positive or negative depending on whether $S_T$ is above or below $S_0 e^{(r-q)\tau}$. However, the key insight is that conditional on $S_T > K$, the values of $S_T$ above $S_0 e^{(r-q)\tau}$ are weighted by $(S_T/(S_0 e^{(r-q)\tau}) - 1) > 0$, and these large-$S_T$ outcomes contribute more in absolute terms than the deficit from outcomes where $K < S_T < S_0 e^{(r-q)\tau}$.

    More rigorously, define $F = S_0 e^{(r-q)\tau}$ (the forward price). Then

    $$
    P_1 - P_2 = \frac{1}{F}\mathbb{E}^{\mathbb{Q}}[(S_T - F)\mathbf{1}_{S_T > K}]
    $$

    Since $\mathbb{E}^{\mathbb{Q}}[S_T - F] = 0$ (martingale property), we have $\mathbb{E}^{\mathbb{Q}}[(S_T - F)\mathbf{1}_{S_T \leq K}] = -\mathbb{E}^{\mathbb{Q}}[(S_T - F)\mathbf{1}_{S_T > K}]$. On $\{S_T \leq K\}$, $S_T - F$ is mostly negative (for reasonable $K$), so $\mathbb{E}^{\mathbb{Q}}[(S_T - F)\mathbf{1}_{S_T \leq K}] < 0$, which means $\mathbb{E}^{\mathbb{Q}}[(S_T - F)\mathbf{1}_{S_T > K}] > 0$. Hence $P_1 - P_2 > 0$.

    The inequality is strict because $S_T$ has a continuous distribution (no atoms) and $\mathbb{Q}(S_T > K) > 0$ for any finite $K$.

    **Behavior as $K \to \infty$.** Both $P_1$ and $P_2$ converge to 0 (the call goes deep OTM and is almost never exercised). The difference $P_1 - P_2$ also converges to 0, but $P_1/P_2$ can diverge because $P_1$ decays more slowly than $P_2$. Intuitively, the $\mathbb{Q}^S$ measure overweights the extreme right tail of $S_T$, so the probability of exercising a deep OTM call is relatively higher under $\mathbb{Q}^S$ than under $\mathbb{Q}$.

---

**Exercise 6.**
Consider an asset-or-nothing put, which pays $S_T$ if $S_T < K$. Show that its price is $S_0 e^{-q\tau}(1 - P_1)$ and verify this against the numerical example: $\text{AoN put} = 100(1 - 0.5748) = 42.52$. Use the decomposition $S_0 e^{-q\tau} = \text{AoN call} + \text{AoN put}$ to confirm consistency.

??? success "Solution to Exercise 6"
    **Asset-or-nothing put price.** The asset-or-nothing put pays $S_T\mathbf{1}_{S_T < K}$. Its price is

    $$
    V_{\text{AoN put}} = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[S_T\mathbf{1}_{S_T < K}]
    $$

    We use the identity $\mathbf{1}_{S_T < K} = 1 - \mathbf{1}_{S_T > K}$ (ignoring the zero-probability event $S_T = K$):

    $$
    V_{\text{AoN put}} = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[S_T] - e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[S_T\mathbf{1}_{S_T > K}]
    $$

    $$
    = e^{-r\tau}S_0 e^{(r-q)\tau} - S_0 e^{-q\tau}P_1 = S_0 e^{-q\tau}(1 - P_1)
    $$

    **Numerical verification.** With $S_0 = 100$, $q = 0$, $P_1 = 0.5748$:

    $$
    V_{\text{AoN put}} = 100(1 - 0.5748) = 100 \times 0.4252 = 42.52
    $$

    **Consistency check.** The decomposition requires

    $$
    S_0 e^{-q\tau} = V_{\text{AoN call}} + V_{\text{AoN put}}
    $$

    since $S_T\mathbf{1}_{S_T > K} + S_T\mathbf{1}_{S_T < K} = S_T$ (the stock pays either above or below $K$). Numerically:

    $$
    V_{\text{AoN call}} + V_{\text{AoN put}} = S_0 P_1 + S_0(1 - P_1) = 57.48 + 42.52 = 100.00 = S_0 e^{-q\tau}
    $$

    Confirmed. This decomposition is the asset-or-nothing analogue of the forward price identity: the present value of receiving $S_T$ unconditionally is $S_0 e^{-q\tau}$, which splits into the AoN call (receive $S_T$ if exercised) and AoN put (receive $S_T$ if not exercised).

---

**Exercise 7.**
The Feller condition under $\mathbb{Q}^S$ requires $2\kappa^*\theta^* \geq \xi^2$. Since $\kappa^*\theta^* = \kappa\theta$ (verify this), the Feller condition under $\mathbb{Q}^S$ is identical to that under $\mathbb{Q}$. Prove this algebraically and discuss why measure changes within the affine family preserve the Feller condition.

??? success "Solution to Exercise 7"
    **Algebraic proof.** By definition:

    $$
    \kappa^*\theta^* = (\kappa - \rho\xi)\cdot\frac{\kappa\theta}{\kappa - \rho\xi} = \kappa\theta
    $$

    The factor $(\kappa - \rho\xi)$ cancels exactly, giving $\kappa^*\theta^* = \kappa\theta$ for any values of $\rho$, $\xi$, and $\kappa$.

    **Feller condition.** Under $\mathbb{Q}$, the Feller condition is $2\kappa\theta \geq \xi^2$. Under $\mathbb{Q}^S$, it is $2\kappa^*\theta^* \geq \xi^2$. Since $\kappa^*\theta^* = \kappa\theta$ and $\xi$ is unchanged:

    $$
    2\kappa^*\theta^* \geq \xi^2 \iff 2\kappa\theta \geq \xi^2
    $$

    The conditions are identical.

    **Why affine measure changes preserve the Feller condition.** The general pattern is as follows. The variance SDE under any measure in the affine family has the form

    $$
    dv_t = [\alpha - \beta v_t]\,dt + \xi\sqrt{v_t}\,dW_t
    $$

    The Feller condition is $2\alpha \geq \xi^2$. Both the $\mathbb{P} \to \mathbb{Q}$ measure change (with $\lambda_v = \lambda\sqrt{v_t}$) and the $\mathbb{Q} \to \mathbb{Q}^S$ measure change modify the drift by adding a term proportional to $v_t$:

    - $\mathbb{P} \to \mathbb{Q}$: adds $-\xi\lambda v_t\,dt$, changing $\beta$ but not $\alpha$
    - $\mathbb{Q} \to \mathbb{Q}^S$: adds $\rho\xi v_t\,dt$, changing $\beta$ but not $\alpha$

    In both cases, the constant term $\alpha = \kappa\theta$ in the drift is invariant. Since the Feller condition depends only on $\alpha$ and $\xi$ (both unchanged), it is preserved.

    This invariance holds because the Girsanov shift is proportional to the diffusion coefficient $\xi\sqrt{v_t}$, so the drift adjustment is proportional to $v_t$ (not to a constant or to $\sqrt{v_t}$). Any measure change that shifts the drift by a term proportional to $v_t$ preserves the constant part of the drift and hence the Feller condition. This is the structural reason why the specification $\lambda_v \propto \sqrt{v_t}$ (or the numeraire change induced by the stock) preserves both the affine form and the boundary behavior of the CIR process.
