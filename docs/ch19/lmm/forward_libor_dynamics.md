# Forward LIBOR Dynamics

This section explores the principles and methods underlying forward libor dynamics, which form a critical component of modern financial mathematics.

## Key Concepts

The fundamental concepts in this area include:

- Theoretical foundations and mathematical framework
- Key definitions and notation
- Important theorems and results
- Connections to other areas of financial mathematics

!!! abstract "Learning Objectives"
    After completing this section, you should understand:

    - The core mathematical principles and their financial interpretations
    - How these concepts connect to practical applications
    - The relationship between theory and numerical implementation

---

## QuantPie Derivation: LIBOR Market Model Forward Measure

### Definition of the LIBOR Rate

$$\begin{array}{ccccccccccccccc}
\displaystyle
l_i(t)&=&l&\left(\right.&t&;&T_{i-1}&,&T_{i}&\left.\right)\\
&&&&\uparrow&&\uparrow&&\uparrow&\\
&&&&\text{Now}&&\text{Reset Date}&&\text{Maturity}&\\
&&&&&&\text{Fixing Date}&&&\\
&&&&&&\text{Expiry Date}&&&\\
\end{array}$$

### ZCB and LIBOR Relationship

$$\begin{array}{ccccccc}
\displaystyle
P\left(t,T_{i}\right)
&=&
\displaystyle
P\left(t,T_{i-1}\right)
&\displaystyle
\frac{1}{1+\tau_i l\left(t;T_{i-1},T_{i}\right)}\\
\uparrow&&\uparrow&\uparrow\\
\text{Discount from $T_i$ to $t$}&&\text{Discount from $T_{i-1}$ to $t$}&\text{Discount from $T_i$ to $T_{i-1}$}\\
\text{Observed today $t$}&&\text{Observed today $t$}&\text{Observed today $t$}\\
\end{array}$$

### Forward LIBOR Rate

$$\begin{array}{lll}
\displaystyle
l_i\left(t\right)
&=&\displaystyle
l\left(t;T_{i-1},T_{i}\right)\\
&=&\displaystyle
\frac{1}{\tau_i}
\left(\frac{P\left(t,T_{i-1}\right)-P\left(t,T_{i}\right)}{P\left(t,T_{i}\right)}\right)\\
&=&\displaystyle
\frac{1}{\tau_i}
\left(\frac{P\left(t,T_{i-1}\right)}{P\left(t,T_{i}\right)}-1\right)\\
\end{array}$$

### Dynamics of the LIBOR Rate

$$\begin{array}{ccccccc}
\displaystyle
dl_i(t)
&=&
\displaystyle
\bar{\mu}_i^\mathbb{P}(t)dt+\bar{\sigma}_i(t)dW_i^\mathbb{P}(t)
\end{array}$$

$$\begin{array}{ccccccc}
\displaystyle
dW_i^\mathbb{P}(t)dW_j^\mathbb{P}(t)
=\rho_{ij}dt
\end{array}$$

### LIBOR is an $T_i$-Martingale

Since $P\left(t,T_{i-1}\right)-P\left(t,T_{i}\right)$ is a price of tradable assets,
$l_i\left(t\right)$ is an $T_i$-martingale.

$$\begin{array}{ccccccc}
\displaystyle
\mathbb{E}^{T_i}\left[\frac{P\left(T_{i-1},T_{i-1}\right)}{P\left(T_{i-1},T_{i}\right)}\Big{|}{\cal F}(t)\right]
&=&
\displaystyle
\frac{P\left(t,T_{i-1}\right)}{P\left(t,T_{i}\right)}
\end{array}$$

$$\begin{array}{ccccccc}
\displaystyle
\mathbb{E}^{T_i}\left[1+\tau_il(T_{i-1};T_{i-1},T_i)\Big{|}{\cal F}(t)\right]
&=&
\displaystyle
1+\tau_il(t;T_{i-1},T_i)
\end{array}$$

$$\begin{array}{ccccccc}
\displaystyle
\mathbb{E}^{T_i}\left[l(T_{i-1};T_{i-1},T_i)\Big{|}{\cal F}(t)\right]
&=&
\displaystyle
l(t;T_{i-1},T_i)
\end{array}$$

### LIBOR Dynamics in Forward and Other Measures

Under the $T_i$-forward measure:

$$\begin{array}{ccccccc}
\displaystyle
dl_i(t)
=
\bar{\sigma}_i(t)dW_i^i(t)
\end{array}$$

Under a different forward measure $T_j$:

$$\begin{array}{ccccccc}
\displaystyle
dl_i(t)
=
\bar{\mu}_i^j(t)dt+\bar{\sigma}_i(t)dW_i^j(t)
\end{array}$$

### Lognormal LIBOR Market Model

Assume constant proportional volatility:

$$\begin{array}{ccccccc}
\displaystyle
\bar{\sigma}_i(t)
=
\sigma_i(t)l_i(t)
\quad\Rightarrow\quad
\frac{dl_i(t)}{l_i(t)}
=
\sigma_i(t)dW_i^i(t)
\end{array}$$

### Change of Measure: Radon-Nikodym Derivative

$$\begin{array}{ccccccc}
\displaystyle
\lambda_i^{i-1}(t)
&=&\displaystyle
\left.\frac{d\mathbb{Q}^{i-1}}{d\mathbb{Q}^{i}}\Big{|}{\cal F}(t)\right)\\
&=&\displaystyle
\frac{P(t,T_{i-1})/P(t_0,T_{i-1})}{P(t,T_{i})/P(t_0,T_{i})}\\
&=&\displaystyle
\frac{P(t_0,T_{i})}{P(t_0,T_{i-1})}(\tau_i l_i(t)+1)\\
\end{array}$$

$$\begin{array}{ccccccc}
\displaystyle
d\lambda_i^{i-1}(t)
&=&\displaystyle
\frac{P(t_0,T_{i})}{P(t_0,T_{i-1})}\tau_i dl_i(t)\\
&=&\displaystyle
\frac{P(t_0,T_{i})}{P(t_0,T_{i-1})}\tau_i \bar{\sigma}_i(t)dW_i^i(t)\\
&=&\displaystyle
\frac{\lambda_i^{i-1}(t)}{\tau_il_i(t)+1}\tau_i\bar{\sigma}_i(t)dW_i^i(t)\\
&=&\displaystyle
\lambda_i^{i-1}(t)\frac{\tau_i\bar{\sigma}_i(t)}{\tau_il_i(t)+1}dW_i^i(t)\\
\end{array}$$

$$\begin{array}{ccccccc}
\displaystyle
\frac{d\lambda_i^{i-1}(t)}{\lambda_i^{i-1}(t)}
=\frac{\tau_i\bar{\sigma}_i(t)}{\tau_il_i(t)+1}dW_i^i(t)\\
\end{array}$$

### Girsanov Transformation

$$\begin{array}{ccccccc}
\displaystyle
dW_i^{i-1}(t)
=
-\frac{\tau_i\bar{\sigma}_i(t)}{\tau_il_i(t)+1}dt +dW_i^i(t)
\end{array}$$

### LIBOR Under Different Measures

$$\begin{array}{llllll}
\displaystyle
dl_i(t)
&=&\displaystyle
\bar{\sigma}_i(t)dW_i^i(t)\\
&=&\displaystyle
\bar{\sigma}_i(t)\left(\frac{\tau_i\bar{\sigma}_i(t)}{\tau_il_i(t)+1}dt
+dW_i^{i-1}(t)\right)\\
&=&\displaystyle
\bar{\sigma}_i(t)\frac{\tau_i\bar{\sigma}_i(t)}{\tau_il_i(t)+1}dt
+\bar{\sigma}_i(t)dW_i^{i-1}(t)\\
\end{array}$$

### Terminal Measure

For the terminal measure $\mathbb{Q}^m$ with numeraire $P(t, T_m)$:

$$\begin{array}{lllll}
\displaystyle
dW_i^{i}(t)
&=&\displaystyle
-\frac{\tau_{i+1}\bar{\sigma}_{i+1}(t)}{\tau_{i+1}l_{i+1}(t)+1}dt +dW_i^{i+1}(t)\\
&=&\displaystyle
-\frac{\tau_{i+1}\bar{\sigma}_{i+1}(t)}{\tau_{i+1}l_{i+1}(t)+1}dt
+\left(-\frac{\tau_{i+2}\bar{\sigma}_{i+2}(t)}{\tau_{i+2}l_{i+2}(t)+1}dt +dW_i^{i+2}(t)\right)\\
&=&\displaystyle
-\sum_{k=i+1}^{i+2}\frac{\tau_{k}\bar{\sigma}_{k}(t)}{\tau_{k}l_{k}(t)+1}dt
+dW_i^{i+2}(t)\\
&=&\displaystyle
-\sum_{k=i+1}^{m}\frac{\tau_{k}\bar{\sigma}_{k}(t)}{\tau_{k}l_{k}(t)+1}dt
+dW_i^{m}(t)\\
\end{array}$$
