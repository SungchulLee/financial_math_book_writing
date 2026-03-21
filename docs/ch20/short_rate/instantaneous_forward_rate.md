# Hull-White Instantaneous Forward Rate

## Hull-White Volatility of Instantaneous Forward Rate

$$\begin{array}{lllll}
\displaystyle
\sigma(t,T)=\sigma e^{-\lambda(T-t)}
\end{array}$$

## Hull-White Instantaneous Forward Rate Dynamics

$$\begin{array}{lllll}
\displaystyle
df(t,T)
=
\mu^\mathbb{Q}(t,T)dt+\sigma(t,T)dW^{\mathbb{Q}}(t)
\end{array}$$

where

$$\begin{array}{lllll}
\displaystyle
\mu^\mathbb{Q}(t,T)
=\frac{\sigma^2}{\lambda}e^{-\lambda(T-t)}\left(1-e^{-\lambda(T-t)}\right)
\end{array}$$

???+ note "Proof"

    $$\begin{array}{lllll}
    \displaystyle
    \mu(t,T)
    =\sigma(t,T)\int_t^T\sigma(t,T')dT'
    =\frac{\sigma^2}{\lambda}e^{-\lambda(T-t)}\left(1-e^{-\lambda(T-t)}\right)
    \end{array}$$
