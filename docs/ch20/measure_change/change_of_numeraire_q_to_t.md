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

---

**Exercise 2.** Show that the forward rate $f(t,T)$ is a martingale under the $\mathbb{T}$-measure by verifying that $df(t,T) = \sigma(t,T)dW^{\mathbb{T}}(t)$ has zero drift. Explain why this property is useful for derivative pricing.

---

**Exercise 3.** Compute $\theta^{\mathbb{T}}(t)$ explicitly in terms of $\theta(t)$ and the bond volatility $\sigma_P(t,T)$. For a Hull-White model with $\sigma = 0.01$ and $\lambda = 0.05$, evaluate the drift adjustment $\frac{\sigma}{\lambda}\sigma_P(t,T)$ at $t = 2$ and $T = 10$.

---

**Exercise 4.** Verify that the variance $\sigma_r^2(t_0, t) = -\frac{1}{2}\sigma^2 B(2(t-t_0))$ is the same under both $\mathbb{Q}$ and $\mathbb{T}$. Explain why Girsanov's theorem preserves the diffusion coefficient but changes the drift.

---

**Exercise 5.** The bond dynamics under $\mathbb{T}$ have drift $r(t) + \sigma_P^2(t,T)$ instead of $r(t)$. Explain the economic meaning of the extra drift term $\sigma_P^2(t,T)$ in terms of the risk premium associated with the change of numeraire.

---

**Exercise 6.** Consider the $x(t)$ process under $\mathbb{Q}$: $dx(t) = -\lambda x(t)dt + \sigma dW^{\mathbb{Q}}(t)$. Derive the $x(t)$ process under $\mathbb{T}$ by substituting $dW^{\mathbb{Q}}(t) = dW^{\mathbb{T}}(t) + \sigma_P(t,T)dt$ and simplify.

---

**Exercise 7.** For the conditional distribution $r(t)|r(t_0) \sim N(\mu^{\mathbb{T}}_r(t_0,t), \sigma_r^2(t_0,t))$ under the $T$-forward measure, compute $\mu^{\mathbb{T}}_r(0, 5)$ for $r(0) = 0.04$, $\sigma = 0.01$, $\lambda = 0.05$, and $T = 10$ with a flat forward curve $f^M(0,t) = 0.04$. Compare with the $\mathbb{Q}$-measure mean and explain the direction of the difference.
