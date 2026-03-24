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

---

**Exercise 2.**
Under $\mathbb{Q}^S$, the variance parameters change to $\kappa^* = \kappa - \rho\xi$ and $\theta^* = \kappa\theta/\kappa^*$. For $\rho = -0.7$, $\xi = 0.3$, $\kappa = 1.5$, $\theta = 0.04$, verify the numerical example values $\kappa^* = 1.71$ and $\theta^* = 0.0351$. Now consider $\rho = +0.5$ (positive correlation). Compute $\kappa^*$ and $\theta^*$ and explain why the mean-reversion speed decreases and the long-run variance increases in this case.

---

**Exercise 3.**
The shift formula states $\varphi_1(u) = \varphi(u - i)/(S_0 e^{(r-q)\tau})$, which requires evaluating the Heston CF at $u - i$ (a complex argument with imaginary part $-1$). Show that this evaluation is well-defined provided $\mathbb{E}^{\mathbb{Q}}[S_T] < \infty$, which is equivalent to the first moment condition. What happens if you try to compute $\varphi(u - 2i)$, corresponding to $\mathbb{E}^{\mathbb{Q}}[S_T^2]$? Under what Heston parameter condition does this second moment exist?

---

**Exercise 4.**
For a European put, $\Delta_{\text{put}} = e^{-q\tau}(P_1 - 1)$ where $P_1 = \mathbb{Q}^S(S_T > K)$. Using the numerical example ($P_1 = 0.5748$, $q = 0$), compute $\Delta_{\text{put}}$ and verify that $\Delta_{\text{call}} - \Delta_{\text{put}} = e^{-q\tau}$ (put-call parity for deltas).

---

**Exercise 5.**
The $\mathbb{Q}^S$ measure weights high-stock-price outcomes more heavily, so $P_1 > P_2$ when $r > q$. Show this rigorously: $P_1 - P_2 = \mathbb{E}^{\mathbb{Q}}[(S_T/(S_0 e^{(r-q)\tau}) - 1)\mathbf{1}_{S_T > K}] > 0$. Why is the inequality strict? What happens to $P_1 - P_2$ as the strike $K \to \infty$ (deep OTM call)?

---

**Exercise 6.**
Consider an asset-or-nothing put, which pays $S_T$ if $S_T < K$. Show that its price is $S_0 e^{-q\tau}(1 - P_1)$ and verify this against the numerical example: $\text{AoN put} = 100(1 - 0.5748) = 42.52$. Use the decomposition $S_0 e^{-q\tau} = \text{AoN call} + \text{AoN put}$ to confirm consistency.

---

**Exercise 7.**
The Feller condition under $\mathbb{Q}^S$ requires $2\kappa^*\theta^* \geq \xi^2$. Since $\kappa^*\theta^* = \kappa\theta$ (verify this), the Feller condition under $\mathbb{Q}^S$ is identical to that under $\mathbb{Q}$. Prove this algebraically and discuss why measure changes within the affine family preserve the Feller condition.
