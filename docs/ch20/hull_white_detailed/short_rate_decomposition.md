# Hull-White Short Rate Decomposition

## Decomposition of Short Rate

Decompose the short rate $r(t)$ as

$$\begin{array}{lllll}
\displaystyle
r(t)
=
\tilde{r}(t)+\psi(t)
\end{array}$$

Then,

$$\begin{array}{lllll}
\displaystyle
d\tilde{r}(t)
=
-\lambda\tilde{r}(t) dt+\sigma dW^{\mathbb{Q}}(t),\quad
\tilde{r}(0)=0
\end{array}$$

???+ note "Proof"

    $$\begin{array}{lllll}
    \displaystyle
    d\psi(t)
    &=&\displaystyle
    -\lambda r_0e^{-\lambda t}dt
    -\lambda^2\left[\int_0^t\theta(t')e^{-\lambda(t-t')}dt'\right]dt
    +\lambda \theta(t)dt
    \\
    &=&\displaystyle
    -\lambda \psi(t)dt
    +\lambda \theta(t)dt
    \end{array}$$

    Therefore,

    $$\begin{array}{lllll}
    \displaystyle
    dr(t)=d\tilde{r}(t)+d\psi(t)
    \end{array}$$

    gives

    $$\begin{array}{lllll}
    \displaystyle
    d\tilde{r}(t)
    &=&\displaystyle
    dr(t)-d\psi(t)\\
    &=&\displaystyle
    \lambda(\theta(t)-r(t))dt+\sigma dW^{\mathbb{Q}}(t)-(-\lambda\psi(t)+\lambda\theta(t))dt\\
    &=&\displaystyle
    -\lambda(r(t)-\psi(t))dt+\sigma dW^{\mathbb{Q}}(t)\\
    &=&\displaystyle
    -\lambda\tilde{r}(t)dt+\sigma dW^{\mathbb{Q}}(t)
    \end{array}$$

## Discounted Characteristic Function via Decomposition

$$\begin{array}{lllll}
\displaystyle
\phi(u;t,T)
=
\mathbb{E}^\mathbb{Q}\left[e^{-\int_t^Tr(t')dt'+iur(T)}\Big{|}{\cal F}(t)\right]
=
e^{-\int_t^T\psi(t')dt'+iu\psi(T)}
\text{exp}\left(\tilde{A}(u,\tau)+\tilde{B}(u,\tau)\tilde{r}(t)\right)
\end{array}$$

???+ note "Proof"

    $$\begin{array}{lllll}
    \displaystyle
    \phi(u;t,T)
    &=&\displaystyle
    \mathbb{E}^\mathbb{Q}\left[e^{-\int_t^Tr(t')dt'+iur(T)}\Big{|}{\cal F}(t)\right]\\
    &=&\displaystyle
    \mathbb{E}^\mathbb{Q}\left[e^{-\int_t^T\left(\tilde{r}(t')+\psi(t')\right)dt'+iu\left(\tilde{r}(T)+\psi(T)\right)}\Big{|}{\cal F}(t)\right]\\
    &=&\displaystyle
    e^{-\int_t^T\psi(t')dt'+iu\psi(T)}
    \mathbb{E}^\mathbb{Q}\left[e^{-\int_t^T\tilde{r}(t')dt'+iu\tilde{r}(T)}\Big{|}{\cal F}(t)\right]\\
    \end{array}$$

    The remaining expectation involves only $\tilde{r}$, which follows a simple Ornstein–Uhlenbeck process without the time-dependent $\theta$, making the computation tractable.

## ZCB Price via Decomposition

$$
\displaystyle
P(t,T)=e^{A(\tau)+B(\tau)r(t)}
$$

???+ note "Proof"

    Setting $u=0$:

    $$\begin{array}{lllll}
    \displaystyle
    P(0,T)
    &=&\displaystyle
    \phi(u=0;t=0,T=T)\\
    &=&\displaystyle
    \text{exp}\left(-\int_0^T\psi(z)dz+\tilde{A}(0,\tau)+\tilde{B}(0,\tau)\tilde r(0)\right)\\
    &=&\displaystyle
    \text{exp}\left(
    -\int_0^T\left[r_0e^{-\lambda z}+\lambda\int_0^z\theta(z')e^{-\lambda(z-z')}dz'\right]dz+\tilde{A}(0,\tau)\right)
    \end{array}$$

## Final Form of $\psi$

$$\begin{array}{lllll}
\displaystyle
\psi(T)
=
f(0,T)+\frac{\sigma^2}{2\lambda}\left(e^{-\lambda T}-1\right)^2\\
\end{array}$$

???+ note "Proof"

    By matching the analytic ZCB price $P(0,T)$ from the characteristic function with the market ZCB price, and noting that the decomposition separates the deterministic $\psi$ component from the stochastic $\tilde{r}$ component, we obtain the closed-form expression for $\psi(T)$.
