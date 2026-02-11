# Discounted Characteristic Function

#### Theorem (Duffie-Pann-Singleton)



If ${\bf X}_t$ is affine, the discounted characteristic function (ChF) has the following affine form:
$$
\begin{array}{lll}
\displaystyle
\varphi({\bf X}_t,t,T,{\bf u})
:=
\mathbb{E^Q}\left[e^{-\int_t^Tr\left({\bf X}_{t'}\right)dt'}e^{i{\bf u}^T{\bf X}_T}\Big{|}F(t)\right]
=
e^{A({\bf u},\tau)+{\bf B}({\bf u},\tau)^T{\bf X}_t}
\end{array}
$$
where $\tau=T−t$. Furthermore,
The coefficients $A$ and ${\bf B}$ satisfy the following Riccati Equation:
$$\begin{array}{lll}
\displaystyle
\frac{dA}{d\tau}
&=&\displaystyle
-r_0+{\bf B}^Ta_0+\frac{1}{2}{\bf B}^Tc_0{\bf B}\\
\displaystyle
\frac{d{\bf B}}{d\tau}
&=&\displaystyle
-r_1+a_1^T{\bf B}+\frac{1}{2}{\bf B}^Tc_1{\bf B}\\
\end{array}$$

with the initial condition

$$\begin{array}{lll}
\displaystyle
A({\bf u},0)
&=&\displaystyle
0\\
\displaystyle
{\bf B}({\bf u},0)
&=&\displaystyle
i{\bf u}^T\\
\end{array}$$


#### Example - BS Model

##### Discounted Characteristic Function



With the fixed $u$ and $T$,

$$
\begin{array}{lll}
\displaystyle
U(X,t)
:=\varphi(X,t,u,T)
:=e^{-r(T-t)}\mathbb{E^Q}\left[e^{iuX_T}\Big{|}F(t)\right]
=e^{-r(T-t)}\int e^{iuX_T} p(X,t,X_T,T)dX_T
\end{array}
$$

##### $U(X,t)$ Satisfies Black-Scholes PDE



Since $e^{-r(T-t)}\int \text{Payoff}(X_T)p(X,t,X_T,T)dX_T$
satisfies the Black-Scholes PDE,
$U(X,t)$ also satisfies the Black-Scholes PDE.
With change of variable $X=\log S$ and $\tau=T-t$,
the Black-Scholes PDE for $U(X,t)$ becomes  

$$
\begin{array}{lll}
\displaystyle
-\frac{\partial U}{\partial \tau}
+\left(r-\frac{1}{2}\sigma^2\right)\frac{\partial U}{\partial X}
+
\frac{1}{2}\sigma^2\frac{\partial^2 U}{\partial X^2}
-rU=0
\end{array}
$$

##### Affine Solution



By Duffie-Pan-Singleton, $U(X,t)$ has the following form:

$$
\begin{array}{lll}
\displaystyle
U(X,t)
=e^{A(\tau)+B(\tau)X}
\end{array}
$$

##### Riccati Equation



Plugging this to the Black-Scholes PDE, we have

$$
\begin{array}{lll}
\displaystyle
\left(-\frac{\partial A}{\partial \tau}
+\left(r-\frac{1}{2}\sigma^2\right)B
+\frac{1}{2}\sigma^2B^2
-r\right) -\left(\frac{\partial B}{\partial \tau}\right)X=0
\end{array}
$$

or

$$
\begin{array}{lllll}
\text{Collect Rest}&&
\displaystyle
\frac{dA}{d\tau}
=-r+\left(r-\frac{1}{2}\sigma^2\right)B+\frac{1}{2}\sigma^2B^2
&\Rightarrow&
\displaystyle
A=\left[-r+\left(r-\frac{1}{2}\sigma^2\right)iu-\frac{1}{2}\sigma^2u^2\right]\tau
\\
\text{Collect $X$ Term}&&\displaystyle
\frac{dB}{d\tau}
=0&\Rightarrow&
\displaystyle
B=iu\quad(\text{This is from the terminal condition})\\
\end{array}
$$

##### Discounted Characteristic Function From BS PDE



$$
\begin{array}{lll}
\displaystyle
\varphi(X_t,t,u,T)
&:=&\displaystyle
\mathbb{E^Q}\left[e^{-\int_t^Tr\left({\bf X}_s\right)ds}e^{i{\bf u}^T{\bf X}_T}\Big{|}F(t)\right]\\
&=&\displaystyle
e^{A(\tau,{\bf u})+{\bf B}^T(\tau,{\bf u}){\bf X}_t}\\
&=&\displaystyle
exp\left(
\left[-r+\left(r-\frac{1}{2}\sigma^2\right)iu-\frac{1}{2}\sigma^2u^2\right]\tau
+
iuX_t\right)
\end{array}
$$