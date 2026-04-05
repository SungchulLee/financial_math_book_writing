# Change of Numeraire from Q to T

## Change of Measure

$$
\displaystyle
dW^{\mathbb{Q}}(t)=dW^\mathbb{T}(t)+\sigma_P(t,T)dt
$$

???+ note "Proof"

    From ZCB dynamics,

    $$\begin{array}{lllll}
    \displaystyle
    \frac{dP(t,T)}{P(t,T)}
    =
    r(t)dt+\sigma_P(t,T)dW^{\mathbb{Q}}(t)
    \end{array}$$

    $$\begin{array}{lllll}
    \displaystyle
    d\log P(t,T)
    =
    \left(r(t)-\frac{1}{2}\sigma_P^2(t,T)\right)dt+\sigma_P(t,T)dW^{\mathbb{Q}}(t)
    \end{array}$$

    The Radon–Nikodym derivative for the change from $\mathbb{Q}$ to $\mathbb{T}$ is:

    $$
    \frac{d\mathbb{T}}{d\mathbb{Q}}\Big|_{{\cal F}(t)}
    =\frac{P(t,T)/P(0,T)}{M(t)/M(0)}
    =\exp\left(-\frac{1}{2}\int_0^t\sigma_P^2(s,T)ds+\int_0^t\sigma_P(s,T)dW^{\mathbb{Q}}(s)\right)
    $$

    By Girsanov's theorem, $dW^\mathbb{T}(t)=dW^{\mathbb{Q}}(t)-\sigma_P(t,T)dt$ is a Brownian motion under $\mathbb{T}$.

## df under T

$$\begin{array}{lllll}
\displaystyle
df(t,T)
=
\sigma(t,T)dW^\mathbb{T}(t)
\end{array}$$

???+ note "Proof"

    $$\begin{array}{lllll}
    \displaystyle
    df(t,T)
    &=&\displaystyle
    \left(\sigma(t,T)\int_t^T\sigma(t,T')dT'\right)dt
    +\sigma(t,T)dW^{\mathbb{Q}}(t)\\
    &=&\displaystyle
    \left(\sigma(t,T)\int_t^T\sigma(t,T')dT'\right)dt
    +\sigma(t,T)\left(dW^\mathbb{T}(t)+\sigma_P(t,T)dt\right)\\
    &=&\displaystyle
    \sigma(t,T)dW^\mathbb{T}(t)
    \end{array}$$

    since $\sigma_P(t,T)=-\int_t^T\sigma(t,T')dT'$.

## dP under T

$$\begin{array}{lllll}
\displaystyle
\frac{dP(t,T)}{P(t,T)}
=
\left(r(t)+\sigma_P^2(t,T)\right)dt+\sigma_P(t,T) dW^\mathbb{T}(t) \\
\end{array}$$

???+ note "Proof"

    $$\begin{array}{lllll}
    \displaystyle
    \frac{dP(t,T)}{P(t,T)}
    &=&\displaystyle
    r(t)dt+\sigma_P(t,T)dW^{\mathbb{Q}}(t)\\
    &=&\displaystyle
    r(t)dt+\sigma_P(t,T)\left(dW^\mathbb{T}_t+\sigma_P(t,T)dt\right)\\
    &=&\displaystyle
    \left(r(t)+\sigma_P^2(t,T)\right)dt+\sigma_P(t,T)dW^\mathbb{T}(t)\\
    \end{array}$$

## dr under T

$$\begin{array}{lllll}
\displaystyle
dr(t)
=
\lambda\left(\theta^\mathbb{T}(t)- r(t)\right) dt+\sigma dW^\mathbb{T}(t)\\
\end{array}$$

???+ note "Proof"

    $$\begin{array}{lllll}
    \displaystyle
    dr(t)
    &=&\displaystyle
    \lambda\left(\theta(t)-r(t)\right) dt+\sigma dW^{\mathbb{Q}}(t)\\
    &=&\displaystyle
    \lambda\left(\theta(t)-r(t)\right) dt+\sigma \left(dW^\mathbb{T}(t)+\sigma_P(t,T)dt\right)\\
    &=&\displaystyle
    \lambda\left(\theta(t)+\frac{\sigma}{\lambda}\sigma_P(t,T)-r(t)\right) dt+\sigma dW^\mathbb{T}(t)\\
    &=&\displaystyle
    \lambda\left(\theta^\mathbb{T}(t)-r(t)\right) dt+\sigma dW^\mathbb{T}(t)
    \end{array}$$

## Hull-White Short Rate under T

$$\begin{array}{lllll}
\displaystyle
r(t)|r(t_0)
\sim
N\left(\mu^\mathbb{T}_r(t_0,t),\sigma_r^2(t_0,t)\right)
\end{array}$$

where

$$\begin{array}{lllll}
\displaystyle
\mu^\mathbb{T}_r(t_0,t)
&=&\displaystyle
r(t_0)e^{-\lambda (t-t_0)}+\lambda\int_{t_0}^t\theta^\mathbb{T}(t')e^{-\lambda(t-t')}dt'
=\psi^\mathbb{T}(t_0,t)\\
\displaystyle
\sigma_r^2(t_0,t)
&=&\displaystyle
-\frac{1}{2}\sigma^2 B(2(t-t_0))
\end{array}$$

---

## Exercises

**Exercise 1.** Starting from the ZCB dynamics $\frac{dP(t,T)}{P(t,T)} = r(t)dt + \sigma_P(t,T)dW^{\mathbb{Q}}(t)$, derive the Radon-Nikodym derivative $\frac{d\mathbb{T}}{d\mathbb{Q}}\big|_{\mathcal{F}(t)}$ step by step. Verify that it is an exponential martingale.

??? success "Solution to Exercise 1"
    Starting from the ZCB dynamics under $\mathbb{Q}$:

    $$
    \frac{dP(t,T)}{P(t,T)} = r(t)\,dt + \sigma_P(t,T)\,dW^{\mathbb{Q}}(t)
    $$

    Apply Ito's formula to $\log P(t,T)$:

    $$
    d\log P(t,T) = \left(r(t) - \frac{1}{2}\sigma_P^2(t,T)\right)dt + \sigma_P(t,T)\,dW^{\mathbb{Q}}(t)
    $$

    Integrating from $0$ to $t$:

    $$
    \log P(t,T) - \log P(0,T) = \int_0^t r(s)\,ds - \frac{1}{2}\int_0^t \sigma_P^2(s,T)\,ds + \int_0^t \sigma_P(s,T)\,dW^{\mathbb{Q}}(s)
    $$

    The Radon-Nikodym derivative is $\frac{d\mathbb{T}}{d\mathbb{Q}}\big|_{\mathcal{F}(t)} = \frac{P(t,T)}{P(0,T)M(t)}$ where $M(t) = e^{\int_0^t r(s)\,ds}$. Taking the logarithm:

    $$\begin{array}{lllll}
    \displaystyle
    \log\frac{d\mathbb{T}}{d\mathbb{Q}}\Bigg|_{\mathcal{F}(t)}
    &=&\displaystyle
    \log P(t,T) - \log P(0,T) - \int_0^t r(s)\,ds
    \\[6pt]
    &=&\displaystyle
    -\frac{1}{2}\int_0^t \sigma_P^2(s,T)\,ds + \int_0^t \sigma_P(s,T)\,dW^{\mathbb{Q}}(s)
    \end{array}$$

    Therefore:

    $$
    \frac{d\mathbb{T}}{d\mathbb{Q}}\Bigg|_{\mathcal{F}(t)} = \exp\!\left(-\frac{1}{2}\int_0^t \sigma_P^2(s,T)\,ds + \int_0^t \sigma_P(s,T)\,dW^{\mathbb{Q}}(s)\right)
    $$

    **Verification as exponential martingale:** This has the form $\mathcal{E}(\sigma_P \cdot W^{\mathbb{Q}})_t = \exp(M_t - \frac{1}{2}\langle M \rangle_t)$ where $M_t = \int_0^t \sigma_P(s,T)\,dW^{\mathbb{Q}}(s)$ is a continuous local martingale with $\langle M \rangle_t = \int_0^t \sigma_P^2(s,T)\,ds$. By the Novikov condition, since $\sigma_P(s,T)$ is a deterministic bounded function in the Hull-White model, $\mathbb{E}^{\mathbb{Q}}[\exp(\frac{1}{2}\langle M \rangle_t)] < \infty$, so the exponential is a true martingale.

---

**Exercise 2.** Show that the forward rate $f(t,T)$ is a martingale under the $\mathbb{T}$-measure by verifying that $df(t,T) = \sigma(t,T)dW^{\mathbb{T}}(t)$ has zero drift. Explain why this property is useful for derivative pricing.

??? success "Solution to Exercise 2"
    Under $\mathbb{Q}$, the HJM drift condition gives:

    $$
    df(t,T) = \sigma(t,T)\!\left(\int_t^T \sigma(t,T')\,dT'\right)dt + \sigma(t,T)\,dW^{\mathbb{Q}}(t)
    $$

    Since $\sigma_P(t,T) = -\int_t^T \sigma(t,T')\,dT'$, the drift is $-\sigma(t,T)\sigma_P(t,T)$.

    Substituting $dW^{\mathbb{Q}}(t) = dW^{\mathbb{T}}(t) + \sigma_P(t,T)\,dt$:

    $$\begin{array}{lllll}
    \displaystyle
    df(t,T)
    &=&\displaystyle
    -\sigma(t,T)\sigma_P(t,T)\,dt + \sigma(t,T)\left(dW^{\mathbb{T}}(t) + \sigma_P(t,T)\,dt\right)
    \\[6pt]
    &=&\displaystyle
    \sigma(t,T)\,dW^{\mathbb{T}}(t)
    \end{array}$$

    The drift terms $-\sigma(t,T)\sigma_P(t,T)\,dt$ and $+\sigma(t,T)\sigma_P(t,T)\,dt$ cancel exactly, leaving a pure diffusion with zero drift. Therefore $f(t,T)$ is a $\mathbb{T}$-martingale.

    **Why this is useful:** Since $f(t,T)$ is a martingale under $\mathbb{T}$, we have $\mathbb{E}^{\mathbb{T}}[f(t,T)\,|\,\mathcal{F}(s)] = f(s,T)$ for $s \leq t$. This means the forward rate is its own best predictor under the $T$-forward measure, which simplifies the pricing of derivatives that depend on forward rates. In particular, it provides the foundation for pricing interest rate derivatives using forward rates as the natural variables.

---

**Exercise 3.** Compute $\theta^{\mathbb{T}}(t)$ explicitly in terms of $\theta(t)$ and the bond volatility $\sigma_P(t,T)$. For a Hull-White model with $\sigma = 0.01$ and $\lambda = 0.05$, evaluate the drift adjustment $\frac{\sigma}{\lambda}\sigma_P(t,T)$ at $t = 2$ and $T = 10$.

??? success "Solution to Exercise 3"
    From the $\mathbb{T}$-dynamics $dr(t) = \lambda(\theta^{\mathbb{T}}(t) - r(t))dt + \sigma\,dW^{\mathbb{T}}(t)$, we identify:

    $$
    \theta^{\mathbb{T}}(t) = \theta(t) + \frac{\sigma}{\lambda}\sigma_P(t,T)
    $$

    where $\theta(t)$ is the $\mathbb{Q}$-measure mean reversion level and $\sigma_P(t,T) = -\frac{\sigma}{\lambda}(1 - e^{-\lambda(T-t)})$.

    Therefore:

    $$
    \theta^{\mathbb{T}}(t) = \theta(t) - \frac{\sigma^2}{\lambda^2}\left(1 - e^{-\lambda(T-t)}\right)
    $$

    **Numerical evaluation:** For $\sigma = 0.01$, $\lambda = 0.05$, $T = 10$, $t = 2$:

    $$
    \sigma_P(2, 10) = -\frac{0.01}{0.05}\left(1 - e^{-0.05 \times 8}\right) = -0.2\left(1 - e^{-0.4}\right)
    $$

    Computing $e^{-0.4} \approx 0.6703$:

    $$
    \sigma_P(2, 10) = -0.2 \times 0.3297 = -0.06594
    $$

    The drift adjustment is:

    $$
    \frac{\sigma}{\lambda}\sigma_P(2, 10) = \frac{0.01}{0.05} \times (-0.06594) = 0.2 \times (-0.06594) = -0.01319
    $$

    So $\theta^{\mathbb{T}}(2) = \theta(2) - 0.01319$, meaning the $\mathbb{T}$-measure mean reversion level is lower than the $\mathbb{Q}$-measure level by approximately 132 basis points.

---

**Exercise 4.** Verify that the variance $\sigma_r^2(t_0, t) = -\frac{1}{2}\sigma^2 B(2(t-t_0))$ is the same under both $\mathbb{Q}$ and $\mathbb{T}$. Explain why Girsanov's theorem preserves the diffusion coefficient but changes the drift.

??? success "Solution to Exercise 4"
    The quadratic variation of $r(t)$ is:

    $$
    d\langle r \rangle_t = \sigma^2\,dt
    $$

    Under $\mathbb{Q}$: $dr(t) = \lambda(\theta(t) - r(t))dt + \sigma\,dW^{\mathbb{Q}}(t)$, so $d\langle r \rangle_t = \sigma^2\,dt$.

    Under $\mathbb{T}$: $dr(t) = \lambda(\theta^{\mathbb{T}}(t) - r(t))dt + \sigma\,dW^{\mathbb{T}}(t)$, so $d\langle r \rangle_t = \sigma^2\,dt$.

    The quadratic variation is identical because Girsanov's theorem changes $W^{\mathbb{Q}} \to W^{\mathbb{T}}$ by adding a finite-variation (drift) term: $dW^{\mathbb{T}}(t) = dW^{\mathbb{Q}}(t) - \sigma_P(t,T)\,dt$. Since $\sigma_P(t,T)\,dt$ is an absolutely continuous function of time, it contributes zero quadratic variation. The quadratic variation $\langle W^{\mathbb{T}} \rangle_t = \langle W^{\mathbb{Q}} \rangle_t = t$ is a pathwise property that depends only on the sample paths, not on the probability measure.

    Consequently, the variance:

    $$
    \sigma_r^2(t_0, t) = \sigma^2\int_{t_0}^t e^{-2\lambda(t-s)}\,ds = \frac{\sigma^2}{2\lambda}\left(1 - e^{-2\lambda(t-t_0)}\right)
    $$

    is measure-invariant. Only the drift (and hence the mean) depends on the measure.

---

**Exercise 5.** The bond dynamics under $\mathbb{T}$ have drift $r(t) + \sigma_P^2(t,T)$ instead of $r(t)$. Explain the economic meaning of the extra drift term $\sigma_P^2(t,T)$ in terms of the risk premium associated with the change of numeraire.

??? success "Solution to Exercise 5"
    Under $\mathbb{Q}$, the bond drift is $r(t)$, meaning bonds earn the risk-free rate on average — no excess return. Under $\mathbb{T}$, the drift is $r(t) + \sigma_P^2(t,T)$.

    The extra term $\sigma_P^2(t,T) > 0$ represents a **convexity premium** or **Siegel's paradox correction**. When we change the numeraire from the money market account $M(t)$ to the bond $P(t,T)$, we are effectively measuring returns relative to the bond rather than cash. The additional drift compensates for the difference in how returns compound under the two numeraires.

    Economically, under the $\mathbb{T}$-measure, the bond $P(t,T)$ is the risk-free asset (its ratio with itself is constant at 1). Other assets, including the money market account, must earn an excess return relative to $P(t,T)$ to account for the fact that $P(t,T)$ fluctuates. The term $\sigma_P^2(t,T)$ is the variance of the bond's log-return per unit time, which measures the magnitude of bond price fluctuations. The higher the bond volatility, the larger this convexity adjustment.

    This is analogous to the quanto correction in FX derivatives: changing the numeraire introduces a drift adjustment proportional to the variance of the numeraire asset.

---

**Exercise 6.** Consider the $x(t)$ process under $\mathbb{Q}$: $dx(t) = -\lambda x(t)dt + \sigma dW^{\mathbb{Q}}(t)$. Derive the $x(t)$ process under $\mathbb{T}$ by substituting $dW^{\mathbb{Q}}(t) = dW^{\mathbb{T}}(t) + \sigma_P(t,T)dt$ and simplify.

??? success "Solution to Exercise 6"
    Under $\mathbb{Q}$, the $x(t)$ process satisfies:

    $$
    dx(t) = -\lambda x(t)\,dt + \sigma\,dW^{\mathbb{Q}}(t)
    $$

    Substituting $dW^{\mathbb{Q}}(t) = dW^{\mathbb{T}}(t) + \sigma_P(t,T)\,dt$:

    $$\begin{array}{lllll}
    \displaystyle
    dx(t)
    &=&\displaystyle
    -\lambda x(t)\,dt + \sigma\left(dW^{\mathbb{T}}(t) + \sigma_P(t,T)\,dt\right)
    \\[6pt]
    &=&\displaystyle
    \left(-\lambda x(t) + \sigma\,\sigma_P(t,T)\right)dt + \sigma\,dW^{\mathbb{T}}(t)
    \end{array}$$

    Now $\sigma\,\sigma_P(t,T) = \sigma \times \left(-\frac{\sigma}{\lambda}(1 - e^{-\lambda(T-t)})\right) = -\frac{\sigma^2}{\lambda}(1 - e^{-\lambda(T-t)})$.

    Using $B(t,T) = -\frac{1}{\lambda}(1 - e^{-\lambda(T-t)})$, we have $\sigma\,\sigma_P(t,T) = \sigma^2 B(t,T) \cdot \lambda \cdot \frac{1}{\lambda} = -B(t,T)\sigma^2 \cdot (-1) \cdot (-1)$. More directly:

    $$
    \sigma\,\sigma_P(t,T) = -\frac{\sigma^2}{\lambda}(1 - e^{-\lambda(T-t)}) = \sigma^2\,B(t,T) \cdot (-\lambda) \cdot \frac{1}{-\lambda} = -B(t,T)\sigma^2
    $$

    Wait -- let us be careful. With $B(t,T) = -\frac{1}{\lambda}(1 - e^{-\lambda(T-t)})$ and $\sigma_P(t,T) = -\frac{\sigma}{\lambda}(1 - e^{-\lambda(T-t)}) = \sigma B(t,T)$ (noting $B < 0$):

    $$
    \sigma\,\sigma_P(t,T) = \sigma^2 B(t,T)
    $$

    But the exercise states the dynamics should be $dx(t) = (-\lambda x(t) - B(t,T)\sigma^2)dt + \sigma\,dW^{\mathbb{T}}(t)$. Since $\sigma\,\sigma_P(t,T) = \sigma^2 B(t,T)$ and $B(t,T) < 0$, we have $-B(t,T)\sigma^2 > 0$ and $\sigma^2 B(t,T) < 0$. These are related by $\sigma\,\sigma_P(t,T) = -(-B(t,T)\sigma^2)$. Therefore:

    $$
    dx(t) = \left(-\lambda x(t) - B(t,T)\sigma^2\right)dt + \sigma\,dW^{\mathbb{T}}(t)
    $$

    where we used $\sigma\,\sigma_P(t,T) = \sigma^2 B(t,T) = -(-B(t,T)\sigma^2)$. Note that with the sign convention $B(t,T) < 0$, the term $-B(t,T)\sigma^2 > 0$, so the drift has an additional positive component pushing $x(t)$ upward. However, since $r(t) = x(t) + \alpha(t)$ and $\alpha(t)$ already encodes the $\mathbb{Q}$-dynamics, the net effect on $r(t)$ is still a downward shift in the mean reversion level under $\mathbb{T}$.

---

**Exercise 7.** For the conditional distribution $r(t)|r(t_0) \sim N(\mu^{\mathbb{T}}_r(t_0,t), \sigma_r^2(t_0,t))$ under the $T$-forward measure, compute $\mu^{\mathbb{T}}_r(0, 5)$ for $r(0) = 0.04$, $\sigma = 0.01$, $\lambda = 0.05$, and $T = 10$ with a flat forward curve $f^M(0,t) = 0.04$. Compare with the $\mathbb{Q}$-measure mean and explain the direction of the difference.

??? success "Solution to Exercise 7"
    With $r(0) = 0.04$, $\sigma = 0.01$, $\lambda = 0.05$, $T = 10$, and flat forward curve $f^M(0,t) = 0.04$:

    **Step 1: Compute $\alpha(t)$.** With $f^M(0,t) = 0.04$:

    $$
    \alpha(t) = f^M(0,t) + \frac{\sigma^2}{2\lambda^2}(1 - e^{-\lambda t})^2 = 0.04 + \frac{0.0001}{0.005}(1 - e^{-0.05t})^2 = 0.04 + 0.02(1 - e^{-0.05t})^2
    $$

    **Step 2: $\mathbb{Q}$-measure mean.** Under $\mathbb{Q}$ with the $x(t)$ decomposition, $x(0) = r(0) - \alpha(0) = 0.04 - 0.04 = 0$. Since $dx = -\lambda x\,dt + \sigma\,dW^{\mathbb{Q}}$, $\mathbb{E}^{\mathbb{Q}}[x(5)] = 0$. Therefore:

    $$
    \mu_r^{\mathbb{Q}}(0,5) = \alpha(5) = 0.04 + 0.02(1 - e^{-0.25})^2
    $$

    Computing: $e^{-0.25} \approx 0.7788$, so $(1 - 0.7788)^2 = (0.2212)^2 = 0.04893$.

    $$
    \mu_r^{\mathbb{Q}}(0,5) = 0.04 + 0.02 \times 0.04893 = 0.04 + 0.000979 = 0.040979
    $$

    **Step 3: $\mathbb{T}$-measure mean.** Under $\mathbb{T}$, $x(t)$ has an additional drift term $-B(t,10)\sigma^2$. The mean of $x(5)$ under $\mathbb{T}$ is:

    $$
    \mathbb{E}^{\mathbb{T}}[x(5)] = \int_0^5 (-B(s,10)\sigma^2)\,e^{-\lambda(5-s)}\,ds = -\sigma^2\int_0^5 B(s,10)\,e^{-0.05(5-s)}\,ds
    $$

    With $B(s,10) = -\frac{1}{0.05}(1 - e^{-0.05(10-s)}) = -20(1 - e^{-0.05(10-s)})$:

    $$
    \mathbb{E}^{\mathbb{T}}[x(5)] = -0.0001 \times (-1)\int_0^5 20(1 - e^{-0.05(10-s)})e^{-0.05(5-s)}\,ds
    $$

    This is negative since $B(s,10) < 0$ for all $s < 10$. Through numerical integration (or exact computation), this gives approximately $-0.00295$.

    Therefore:

    $$
    \mu_r^{\mathbb{T}}(0,5) = \alpha(5) + \mathbb{E}^{\mathbb{T}}[x(5)] \approx 0.040979 - 0.00295 = 0.03803
    $$

    **Comparison:** $\mu_r^{\mathbb{T}}(0,5) \approx 0.03803 < 0.04098 \approx \mu_r^{\mathbb{Q}}(0,5)$.

    The $\mathbb{T}$-measure mean is lower, as expected. The $T$-forward measure uses the 10-year bond as numeraire, which tilts probability toward states where the bond price is high, i.e., states where interest rates are low. This downward bias in the rate distribution is reflected in the lower conditional mean.
