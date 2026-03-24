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

### LIBOR is an T_i-Martingale

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

---

## Exercises

**Exercise 1.** Consider two forward LIBOR rates $l_1(t)$ and $l_2(t)$ on an annual grid ($T_0 = 0, T_1 = 1, T_2 = 2$). Under the $T_2$-forward measure, $l_1(t)$ is a martingale. Write down its dynamics $dl_1(t) = \bar{\sigma}_1(t)\,l_1(t)\,dW_1^2(t)$. Now express the dynamics of $l_1(t)$ under the $T_1$-forward measure using the Girsanov drift adjustment. What is the sign of the drift?

---

**Exercise 2.** Under the terminal measure $\mathbb{Q}^m$ (with numéraire $P(t, T_m)$), the forward rate $l_i(t)$ has dynamics

$$
dl_i(t) = -l_i(t)\bar{\sigma}_i(t)\sum_{k=i+1}^{m}\frac{\tau_k\,\bar{\sigma}_k(t)\,l_k(t)}{\tau_k l_k(t) + 1}\,dt + l_i(t)\bar{\sigma}_i(t)\,dW_i^m(t)
$$

For $m = 4$, $i = 1$, and constant volatilities $\bar{\sigma}_k = 0.20$, rates $l_k(0) = 5\%$, and $\tau_k = 1$, compute the instantaneous drift of $l_1$ at time 0. Is the drift positive or negative, and why?

---

**Exercise 3.** The relationship between the bond price ratio and the LIBOR rate is $P(t, T_{i-1})/P(t, T_i) = 1 + \tau_i l_i(t)$. Verify this by expressing $l_i(t)$ in terms of the bond prices. Then show that the forward LIBOR rate is a martingale under $\mathbb{Q}^{T_i}$ by identifying it as a ratio of tradable assets divided by the numéraire $P(t, T_i)$.

---

**Exercise 4.** Explain the relationship between the forward measure change formula $dW_i^{i}(t) = \frac{\tau_{i+1}\bar{\sigma}_{i+1}(t)\,l_{i+1}(t)}{\tau_{i+1}l_{i+1}(t)+1}\,dt + dW_i^{i+1}(t)$ and Girsanov's theorem. Identify the Girsanov kernel and explain why it depends on the forward rate $l_{i+1}(t)$.

---

**Exercise 5.** In a three-rate LMM ($l_1, l_2, l_3$), write down the drift of each rate under the spot (rolling) measure, where the numéraire is the discretely-compounded money market account. Compare the drift structure with that under the terminal measure. Which measure leads to simpler simulation and why?

---

**Exercise 6.** Show that as the tenor $\tau_i \to 0$ (continuous limit), the LMM forward rate dynamics converge to the HJM instantaneous forward rate dynamics. Specifically, identify $l_i(t)\tau_i \approx \int_{T_{i-1}}^{T_i} f(t,u)\,du$ and show that the drift condition becomes the standard HJM drift condition $\alpha(t,T) = \sigma(t,T)\int_t^T \sigma(t,u)\,du$.
