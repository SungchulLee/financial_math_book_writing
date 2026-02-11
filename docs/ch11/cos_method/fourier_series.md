# Fourier Series

#### Fourier Series on $[-\pi,\pi]$

For a function $f(x)$ on $[-\pi,\pi]$,

$$
\begin{array}{lll}
\displaystyle
f(\theta)
=\sum_{k=0}^\infty  A_k\cos(k\theta)+\sum_{k=1}^\infty B_k\sin(k\theta)
\end{array}
$$

where, for $k\ge 1$

$$
\begin{array}{lll}
\displaystyle
A_k
=\frac{1}{\pi}\int_{-\pi}^\pi f(\theta)\cos(k\theta)d\theta\\
\displaystyle
B_k
=\frac{1}{\pi}\int_{-\pi}^\pi f(\theta)\sin(k\theta)d\theta\\
\end{array}
$$

and where

$$
\begin{array}{lll}
\displaystyle
A_0
=\frac{1}{2\pi}\int_{-\pi}^\pi f(\theta)d\theta
\end{array}
$$

#### Fourier Series on $[-\pi,\pi]$ for Even Function

If $g$ is even, $B_k=0$.
So,

$$
\begin{array}{lll}
\displaystyle
g(\theta)
=
\sum_{k=0}^\infty  A_k\cos(k\theta)
\end{array}
$$

## Python Demo

See `cos_method_FOURIER_SERIES.py` and `cos_method_FOURIER_SERIES_EVEN.py` in the Python codes appendix.
