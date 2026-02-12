# Cosine Series

#### Cosine Series on $[0,\pi]$

We extend $f(\theta)$ on $[-\pi,\pi]$ and make it even.
Then, we have the cosine series of the function $f(\theta)$ on $[0,\pi]$.

$$
\begin{array}{lll}
\displaystyle
f(\theta)
=
\sum_{k=0}^\infty  A_k\cos(k\theta)
\end{array}
$$

where, for $k\ge 1$

$$
\begin{array}{lll}
\displaystyle
A_k
=\frac{1}{\pi}\int_{-\pi}^\pi f(\theta)\cos(k\theta)d\theta
=\frac{2}{\pi}\int_{0}^\pi f(\theta)\cos(k\theta)d\theta
\end{array}
$$

and where

$$
\begin{array}{lll}
\displaystyle
A_0
=\frac{1}{2\pi}\int_{-\pi}^\pi f(\theta)d\theta
=\frac{1}{\pi}\int_{0}^\pi f(\theta)d\theta
\end{array}
$$

#### Cosine Series on $[a,b]$

$$
\begin{array}{lll}
\displaystyle
f(x)
=
\sum_{k=0}^\infty  A_k\cos\left(k\pi\frac{x-a}{b-a}\right)
\end{array}
$$

where, for $k\ge 1$

$$
\begin{array}{lll}
\displaystyle
A_k
=
\frac{2}{b-a}\int_a^bf(x)\cos\left(k\pi\frac{x-a}{b-a}\right)dx
\end{array}
$$

and where

$$
\begin{array}{lll}
\displaystyle
A_0
=
\frac{1}{b-a}\int_a^bf(x)dx
\end{array}
$$