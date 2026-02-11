# COS Method

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

### COS Method

$$
\begin{array}{lll}
\displaystyle
V(t_0,x_0)
&=&\displaystyle
e^{-r\tau}\mathbb{E^Q}[V(T,x)|{\cal F}(t_0)]\\
&=&\displaystyle
e^{-r\tau}\int_\mathbb{R}V(T,x)f_X(x,T;x_0,t_0)dx\\
&:=&\displaystyle
e^{-r\tau}\int_\mathbb{R}V(T,x)f(x)dx\\
&\approx&\displaystyle
e^{-r\tau}\int_a^bV(T,x)f(x)dx\\
&=&\displaystyle
e^{-r\tau}\frac{b-a}{2}\sum_{k=0}^\infty\mathop{}'A_k\frac{2}{b-a}\int_a^bV(T,x)\cos\left(k\pi\frac{x-a}{b-a}\right)dx\\
&:=&\displaystyle
e^{-r\tau}\frac{b-a}{2}\sum_{k=0}^\infty\mathop{}'A_kH_k\\
&\approx&\displaystyle
e^{-r\tau}\frac{b-a}{2}\sum_{k=0}^{n-1}\mathop{}'A_kH_k\quad\quad\color{red}{\text{Converges Extremely Fast}}\\
\end{array}
$$
where
$$
\begin{array}{llllllllllll}
\displaystyle
A_k
=
\frac{2}{b-a}\mathbb{Re}\left[\varphi\left(\frac{k\pi}{b-a}\right)e^{-i\frac{k\pi a}{b-a}}\right]&&\color{red}{\text{Piece of Cake}}&&\text{if ChF available}\\
&&&&\quad\quad\quad\uparrow\\
&&&&\color{red}{\text{Duffie-Pan-Singleton}}\\
\displaystyle
H_k
=
\frac{2}{b-a}\int_a^bV(T,x)\cos\left(k\pi\frac{x-a}{b-a}\right)dx&&\color{red}{\text{Closed Form Formula available}}&&\text{for Plain and Digital Payoff}\\
\end{array}
$$

### Closed Form Formula

$$
\displaystyle
x = x(T) = \log \frac{S(T)}{K}
$$

$$\begin{array}{lll}
\displaystyle
\chi_k(c,d)
&:=&\displaystyle
\int_c^d e^x\cos\left(k\pi\frac{x-a}{b-a}\right)dx\\
&=&\displaystyle
\frac{1}{1+\left(\frac{k\pi}{b-a}\right)^2}
\left[
\cos\left(k\pi\frac{d-a}{b-a}\right)e^d
-\cos\left(k\pi\frac{c-a}{b-a}\right)e^c
\right.\\
&&\displaystyle\quad\quad\quad\quad\quad
\left.
+\frac{k\pi}{b-a}\sin\left(k\pi\frac{d-a}{b-a}\right)e^d
-\frac{k\pi}{b-a}\sin\left(k\pi\frac{c-a}{b-a}\right)e^c
\right]\\
\end{array}$$

$$\begin{array}{lll}
\displaystyle
\psi_k(c,d)
&:=&\displaystyle
\int_c^d \cos\left(k\pi\frac{y-a}{b-a}\right)dy\\
&=&\displaystyle
\left\{\begin{array}{ll}
\displaystyle
\left[
\sin\left(k\pi\frac{d-a}{b-a}\right)
-\sin\left(k\pi\frac{c-a}{b-a}\right)
\right]\frac{b-a}{k\pi}&\text{for}\quad k\neq 0\\
d-c&\text{for}\quad k=0
\end{array}\right.
\end{array}$$

$$\begin{array}{lll}
\displaystyle
H_k
&=&\displaystyle
\frac{2}{b-a}\int_a^bV(T,x)\cos\left(k\pi\frac{x-a}{b-a}\right)dx
\end{array}$$

For call

$$\begin{array}{lll}
\displaystyle
H_k
&=&\displaystyle
\frac{2}{b-a}\int_a^bV(T,x)\cos\left(k\pi\frac{x-a}{b-a}\right)dx\\
&=&\displaystyle
\frac{2}{b-a}\int_{\log K}^b(e^x-K)\cos\left(k\pi\frac{x-a}{b-a}\right)dx\\
&=&\displaystyle
\frac{2}{b-a}\chi_k(\log K,b)
-\frac{2}{b-a}\cdot K\cdot\psi_k(\log K,b)\\
\end{array}$$

For put

$$\begin{array}{lll}
\displaystyle
H_k
&=&\displaystyle
\frac{2}{b-a}\int_a^bV(T,x)\cos\left(k\pi\frac{x-a}{b-a}\right)dx\\
&=&\displaystyle
\frac{2}{b-a}\int_a^{\log K}(K-e^x)\cos\left(k\pi\frac{x-a}{b-a}\right)dx\\
&=&\displaystyle
\frac{2}{b-a}\cdot K\cdot\psi_k(a,\log K)
-\frac{2}{b-a}\chi_k(a,\log K)\\
\end{array}$$

## Python Demo

See `cos_method_CALL_PUT.py` and `cos_method_CASH_OR_NOTHING.py` in the Python codes appendix.
