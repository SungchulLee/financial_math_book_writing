# Density Recovery using Characteristic Function

### Main Assumption on Probability Density Function $f$

The the probability density function $f$ is supported on the interval $[a,b]$.

$$
\begin{array}{lll}
\displaystyle
\int_A f(x)dx
=
\int_{A\cap [a,b]} f(x)dx
\end{array}
$$

### Density Recovery using Its Chracteristic Function

If the probability density function $f$ is supported on the interval $[a,b]$, then

$$
\begin{array}{lllcl}
\displaystyle
f(x)
&\approx&\displaystyle
\sum_{k=0}^{n-1}\mathop{}'  &A_k&\displaystyle\cos\left(k\pi\frac{x-a}{b-a}\right)\\
&&&\uparrow&\\
&&&\displaystyle\frac{2}{b-a}\mathbb{Re}\left[\varphi\left(\frac{k\pi}{b-a}\right)e^{-i\frac{k\pi a}{b-a}}\right]&\\
\end{array}
$$

### Proof

### Cosine Expansion

We do the cosine expansion.

$$
\begin{array}{lll}
\displaystyle
f(x)
=
\sum_{k=0}^\infty  A_k\cos\left(k\pi\frac{x-a}{b-a}\right)
\end{array}
$$

where for $k\ge 1$

$$
\begin{array}{rcl}
\displaystyle
A_k
=
\frac{2}{b-a}\int_a^bf(x)\cos\left(k\pi\frac{x-a}{b-a}\right)dx
=
\frac{2}{b-a}\mathbb{Re}\left[\varphi\left(\frac{k\pi}{b-a}\right)e^{-i\frac{k\pi a}{b-a}}\right]
\end{array}
$$

and where

$$
\begin{array}{rcl}
\displaystyle
A_0
=
\frac{1}{b-a}\int_a^bf(x)dx
=
\frac{1}{b-a}\mathbb{Re}\left[\varphi\left(0\right)\right]
\end{array}
$$

If we know the characteristic function $\varphi$ of the density function $f$,
we don't need compute any integration at all to get the cosine series coefficients.
we find these coefficients by just plugging certain values into the characteristic function.
That is the point.

### Coefficient Computation

With $t=k\pi/(b-a)$ and $\xi=k\pi(-a)/b-a$
$$
\begin{array}{rcl}
\displaystyle
\varphi(t)e^{i\xi}=\int_a^b e^{i(tx+\xi)}f(x)dx
\quad\Rightarrow\quad
\mathbb{Re}\varphi(t)e^{i\xi}
=\int_a^b f(x)\cos(&\displaystyle \color{red}{t}x+\color{red}{\xi}&\displaystyle)dx
=\int_a^bf(x)\cos\left(k\pi\frac{x-a}{b-a}\right)dx\\
\displaystyle
A_k
=
\frac{2}{b-a}\int_a^bf(x)\cos\left(\right.&\displaystyle \color{red}{k\pi}\frac{x\color{red}{-a}}{\color{red}{b-a}}&\displaystyle \left.\right)dx
=
\frac{2}{b-a}\mathbb{Re}\varphi\left(\frac{k\pi}{b-a}\right)e^{-i\frac{k\pi a}{b-a}}\\
\displaystyle
A_0
=
\frac{1}{b-a}\int_a^bf(x)\cos\left(\right.&\displaystyle \color{red}{0\pi}\frac{x\color{red}{-a}}{\color{red}{b-a}}&\displaystyle \left.\right)dx
=
\frac{2}{b-a}\mathbb{Re}\varphi\left(\frac{0\pi}{b-a}\right)e^{-i\frac{0\pi a}{b-a}}\\
\end{array}
$$

## Python Demo

See `cos_method_NORMAL_PDF_RECOVERY.py` and `cos_method_LOGNORMAL_PDF_RECOVERY.py` in the Python codes appendix.
