# Affine Process

#### Affine Process

If

$$
\begin{array}{lll}
\displaystyle
d{\bf X}=\bar{\mu}({\bf X})dt+\bar{\sigma}({\bf X})d{\bf W}
\end{array}
$$

satisfies

$$
\begin{array}{lllllll}
\displaystyle \bar{\mu}({\bf X})&=&a_0+a_1{\bf X}&&\text{Linear in ${\bf X}$}\\
\displaystyle \bar{\sigma}({\bf X})\bar{\sigma}({\bf X})^T&=&c_0+c_1^T{\bf X}&&\text{Linear in ${\bf X}$}\\
\displaystyle r({\bf X})&=&r_0+r_1^T{\bf X}&&\text{Linear in ${\bf X}$}\\
\end{array}
$$

then $X$ is called a affine process.

#### Characteristic Funtion

If ${\bf X}_t$ is affine, the conditional discounted characteristic funtion of ${\bf X}_T$

$$
\begin{array}{lll}
\displaystyle
\varphi({\bf X}_t,t,T,{\bf u})
:=\mathbb{E^Q}\left[e^{-\int_t^Tr\left({\bf X}_s\right)ds}e^{i{\bf u}^T{\bf X}_T}\Big{|}F(t)\right]
\end{array}
$$

satisfies

$$
\begin{array}{lll}
\text{(1) Terminal Condition}&&
\displaystyle
\varphi({\bf X}_T,T,T,{\bf u})=e^{i{\bf u}^T{\bf X}_T}\\
\\
\text{(2) Affine Form}&&
\displaystyle
\varphi({\bf X}_t,t,T,{\bf u})
=e^{A(\tau,{\bf u})+{\bf B}^T(\tau,{\bf u}){\bf X}_t\color{red}{\quad\leftarrow\quad\normalsize{\text{Linear in ${\bf X}$}}}}\\
\\
\text{(3) Riccati Equation}&&
\displaystyle
\left\{
\begin{array}{lll}
\displaystyle
\frac{dA}{d\tau}
=-r_0+{\bf B}^Ta_0+\frac{1}{2}{\bf B}^Tc_0{\bf B}\\
\displaystyle
\frac{d{\bf B}}{d\tau}
=-r_1+a_1^T{\bf B}+\frac{1}{2}{\bf B}^Tc_1{\bf B}\\
\end{array}
\right.
\end{array}
$$

#### Example - BS Model : $S$ is not Affine



$$\displaystyle\frac{dS}{S}=rdt+\sigma db^\mathbb{Q}$$

$$
\begin{array}{lllllll}
\displaystyle \bar{\mu}(S)&=&rS&&\text{Linear in $S$}\\
\displaystyle \bar{\sigma}(S)\bar{\sigma}(S)^T&=&\sigma^2 S^2&&\text{Not Linear in $S$}\\
\displaystyle r(S)&=&r&&\text{Linear in $S$}\\
\end{array}
$$

#### Example - BS Model : $X=\log S$ is Affine



Since $dS/S=rdt+\sigma db^\mathbb{Q}$, with $X=f(t,S)=\log S$

$$\begin{array}{lll}
\displaystyle
dX
&=&\displaystyle
f_tdt+f_sds+\frac{1}{2}f_{ss}(ds)^2\\
&=&\displaystyle
\frac{1}{s}ds-\frac{1}{2}\frac{1}{s^2}(ds)^2\\
&=&\displaystyle
\left(r-\frac{1}{2}\sigma^2\right)dt+\sigma db^\mathbb{Q}\\
\end{array}$$

$$
\begin{array}{lllllll}
\displaystyle \bar{\mu}(X)&=&\displaystyle r-\frac{1}{2}\sigma^2&&\text{Linear in $X$}\\
\displaystyle \bar{\sigma}(X)\bar{\sigma}(X)^T&=&\sigma^2 &&\text{Linear in $X$}\\
\displaystyle r(X)&=&r&&\text{Linear in $X$}\\
\end{array}
$$



##### Characteristic Funtion



$$
\begin{array}{lll}
\displaystyle
\varphi({\bf X}_t,t,T,{\bf u})
:=
\mathbb{E^Q}\left[e^{-\int_t^Tr\left({\bf X}_s\right)ds}e^{i{\bf u}^T{\bf X}_T}\Big{|}F(t)\right]
=
e^{A(\tau,{\bf u})+{\bf B}^T(\tau,{\bf u}){\bf X}_t}
\end{array}
$$

##### Riccati Equation



$$
\begin{array}{lllllllllll}
\displaystyle
\frac{dA}{d\tau}
=-r_0+{\bf B}^Ta_0+\frac{1}{2}{\bf B}^Tc_0{\bf B}
&\Rightarrow&\displaystyle
\frac{dA}{d\tau}
=-r+\left(r-\frac{1}{2}\sigma^2\right)B+\frac{1}{2}\sigma^2 B^2\\
\displaystyle
\frac{d{\bf B}}{d\tau}
=-r_1+a_1^T{\bf B}+\frac{1}{2}{\bf B}^Tc_1{\bf B}
&\Rightarrow&
\displaystyle
\frac{dB}{d\tau}
=0\\
\end{array}
$$

#### Heston Model

##### Under $\mathbb{Q}$



$$
\begin{array}{lll}
\displaystyle
dS=rSdt+\sqrt{v}SdW_x
\\
\displaystyle
dv=\kappa(\bar{v}-v)dt+\gamma\sqrt{v}dW_v
\\
dW_xdW_v=\rho dt
\end{array}
$$

##### With $X=log S$



$$
\begin{array}{lll}
\displaystyle
dX=\left(r-\frac{1}{2}v\right)dt+\sqrt{v}dW_x
\\
\displaystyle
dv=\kappa(\bar{v}-v)dt+\gamma\sqrt{v}dW_v
\\
dW_xdW_v=\rho dt
\end{array}
$$

##### $[X,v]^T$ Is Affine

##### Dynamics of $[X,v]^T$



$$
\begin{array}{lll}
\displaystyle
d\left[\begin{array}{c}X\\v\end{array}\right]
&=&\displaystyle
\left[\begin{array}{c}
r-\frac{1}{2}v\\
\kappa(\bar{v}-v)
\end{array}\right]dt+
\left[\begin{array}{cc}
\sqrt{v}&0\\
0&\gamma\sqrt{v}
\end{array}\right]
\left[\begin{array}{c}dW_x\\dW_v\end{array}\right]\\
&=&\displaystyle
\left[\begin{array}{c}
r-\frac{1}{2}v\\
\kappa(\bar{v}-v)
\end{array}\right]dt+
\left[\begin{array}{cc}
\sqrt{v}&0\\
0&\gamma\sqrt{v}
\end{array}\right]
\left[\begin{array}{cc}
1&0\\
\rho&\sqrt{1-\rho^2}
\end{array}\right]
\left[\begin{array}{c}d\tilde{W}_x\\d\tilde{W}_v\end{array}\right]\\
&=&\displaystyle
\left[\begin{array}{c}
r-\frac{1}{2}v\\
\kappa(\bar{v}-v)
\end{array}\right]dt+
\left[\begin{array}{cc}
\sqrt{v}&0\\
\rho\gamma\sqrt{v}&\sqrt{1-\rho^2}\gamma\sqrt{v}
\end{array}\right]
\left[\begin{array}{c}d\tilde{W}_x\\d\tilde{W}_v\end{array}\right]
\end{array}
$$

##### $\bar{\mu}({\bf X})$ Is Linear In ${\bf X}$



$$
\begin{array}{lll}
\displaystyle
\bar{\mu}({\bf X})
=
\left[\begin{array}{c}
r-\frac{1}{2}v\\
\kappa(\bar{v}-v)
\end{array}\right]
=
\left[\begin{array}{c}
r\\
\kappa\bar{v}
\end{array}\right]
+
\left[\begin{array}{cc}
0&-\frac{1}{2}\\
0&-\kappa
\end{array}\right]
\left[\begin{array}{c}X\\v\end{array}\right]
\end{array}
$$

##### $\bar{\sigma}({\bf X})\bar{\sigma}({\bf X})^T$ Is Linear In ${\bf X}$



$$
\begin{array}{lll}
\displaystyle
\bar{\sigma}({\bf X})\bar{\sigma}({\bf X})^T
&=&\displaystyle
\left[\begin{array}{cc}
\sqrt{v}&0\\
\rho\gamma\sqrt{v}&\sqrt{1-\rho^2}\gamma\sqrt{v}
\end{array}\right]
\left[\begin{array}{cc}
\sqrt{v}&0\\
\rho\gamma\sqrt{v}&\sqrt{1-\rho^2}\gamma\sqrt{v}
\end{array}\right]^T\\
&=&\displaystyle
\left[\begin{array}{cc}
\sqrt{v}&0\\
\rho\gamma\sqrt{v}&\sqrt{1-\rho^2}\gamma\sqrt{v}
\end{array}\right]
\left[\begin{array}{cc}
\sqrt{v}&\rho\gamma\sqrt{v}\\
0&\sqrt{1-\rho^2}\gamma\sqrt{v}
\end{array}\right]\\
&=&\displaystyle
\left[\begin{array}{cc}
v&\rho\gamma v\\
\rho\gamma v&\gamma^2 v
\end{array}\right]\\
&=&\displaystyle
\left[\begin{array}{cc}
\left[\begin{array}{cc}
0&1\\
0&\rho\gamma
\end{array}\right]
&
\left[\begin{array}{cc}
0&\rho\gamma \\
0&\gamma^2
\end{array}\right]
\end{array}\right]
\left[\begin{array}{c}X\\v\end{array}\right]\\
\end{array}
$$

##### $r({\bf X})$ Is Linear In ${\bf X}$



$$
r({\bf X})=r
$$