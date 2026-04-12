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

### Change of Measure: Radon–Nikodym Derivative

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

??? success "Solution to Exercise 1"
    Under the $T_2$-forward measure, $l_1(t)$ is a martingale (since $T_2$ is the maturity of the bond associated with the second forward rate). In the lognormal LMM, the dynamics are:

    $$
    dl_1(t) = \sigma_1(t)\,l_1(t)\,dW_1^2(t)
    $$

    where $W_1^2$ is a Brownian motion under $\mathbb{Q}^{T_2}$, and $\bar{\sigma}_1(t) = \sigma_1(t)\,l_1(t)$.

    To express the dynamics under the $T_1$-forward measure, we use the Girsanov transformation. From the change-of-measure formula:

    $$
    dW_1^{1}(t) = -\frac{\tau_2\,\bar{\sigma}_2(t)}{\tau_2\,l_2(t) + 1}\,dt + dW_1^{2}(t)
    $$

    Wait --- this relates $W^1$ to $W^2$ for the **second** Brownian component. For the first rate's Brownian motion, we need the change from $\mathbb{Q}^{T_2}$ to $\mathbb{Q}^{T_1}$. Since $T_1 < T_2$, moving from $\mathbb{Q}^{T_2}$ to $\mathbb{Q}^{T_1}$, the Girsanov kernel is:

    $$
    dW_1^{1}(t) = dW_1^{2}(t) + \frac{\tau_2\,\rho_{12}\,\bar{\sigma}_2(t)}{\tau_2\,l_2(t) + 1}\,dt
    $$

    Substituting $dW_1^2(t) = dW_1^1(t) - \frac{\tau_2\,\rho_{12}\,\bar{\sigma}_2(t)}{\tau_2\,l_2(t)+1}\,dt$ into the dynamics of $l_1$:

    $$
    dl_1(t) = \bar{\sigma}_1(t)\,dW_1^2(t) = \bar{\sigma}_1(t)\left(dW_1^1(t) - \frac{\tau_2\,\rho_{12}\,\bar{\sigma}_2(t)}{\tau_2\,l_2(t)+1}\,dt\right)
    $$

    $$
    dl_1(t) = -\frac{\bar{\sigma}_1(t)\,\tau_2\,\rho_{12}\,\bar{\sigma}_2(t)}{\tau_2\,l_2(t)+1}\,dt + \bar{\sigma}_1(t)\,dW_1^1(t)
    $$

    In the lognormal specification with $\bar{\sigma}_k(t) = \sigma_k(t)\,l_k(t)$:

    $$
    dl_1(t) = -\sigma_1(t)\,l_1(t)\,\frac{\tau_2\,\rho_{12}\,\sigma_2(t)\,l_2(t)}{\tau_2\,l_2(t)+1}\,dt + \sigma_1(t)\,l_1(t)\,dW_1^1(t)
    $$

    **The drift is negative.** This makes financial sense: moving from the $T_2$-forward measure to the $T_1$-forward measure (an earlier numeraire date), the drift becomes negative. Under $\mathbb{Q}^{T_1}$, the numéraire $P(t,T_1)$ grows faster relative to $P(t,T_2)$, which pushes $l_1$ downward in expectation relative to this measure.

---

**Exercise 2.** Under the terminal measure $\mathbb{Q}^m$ (with numéraire $P(t, T_m)$), the forward rate $l_i(t)$ has dynamics

$$
dl_i(t) = -l_i(t)\bar{\sigma}_i(t)\sum_{k=i+1}^{m}\frac{\tau_k\,\bar{\sigma}_k(t)\,l_k(t)}{\tau_k l_k(t) + 1}\,dt + l_i(t)\bar{\sigma}_i(t)\,dW_i^m(t)
$$

For $m = 4$, $i = 1$, and constant volatilities $\bar{\sigma}_k = 0.20$, rates $l_k(0) = 5\%$, and $\tau_k = 1$, compute the instantaneous drift of $l_1$ at time 0. Is the drift positive or negative, and why?

??? success "Solution to Exercise 2"
    Under the terminal measure $\mathbb{Q}^4$ with $m = 4$, $i = 1$, constant $\bar{\sigma}_k = 0.20$, $l_k(0) = 0.05$, and $\tau_k = 1$, the drift is:

    $$
    \mu_1^4(0) = -l_1(0)\,\bar{\sigma}_1\sum_{k=2}^{4}\frac{\tau_k\,\bar{\sigma}_k\,l_k(0)}{\tau_k\,l_k(0)+1}
    $$

    In the lognormal specification, with $\bar{\sigma}_k = 0.20$ as proportional volatilities, we have $\bar{\sigma}_k(t) = 0.20 \cdot l_k(t)$ for the absolute volatility. However, examining the given formula:

    $$
    dl_i(t) = -l_i(t)\bar{\sigma}_i(t)\sum_{k=i+1}^{m}\frac{\tau_k\,\bar{\sigma}_k(t)\,l_k(t)}{\tau_k l_k(t) + 1}\,dt + l_i(t)\bar{\sigma}_i(t)\,dW_i^m(t)
    $$

    Here $\bar{\sigma}_k$ appears to be the proportional volatility. Let us interpret $\bar{\sigma}_k = 0.20$ as the proportional volatility. Then:

    Each term in the sum at $t = 0$:

    $$
    \frac{\tau_k\,\bar{\sigma}_k\,l_k(0)}{\tau_k\,l_k(0)+1} = \frac{1 \times 0.20 \times 0.05}{1 \times 0.05 + 1} = \frac{0.01}{1.05} = 0.009524
    $$

    The sum runs from $k = 2$ to $k = 4$, so there are 3 terms, each equal to $0.009524$:

    $$
    \sum_{k=2}^{4}\frac{\tau_k\,\bar{\sigma}_k\,l_k(0)}{\tau_k\,l_k(0)+1} = 3 \times 0.009524 = 0.028571
    $$

    The drift of $l_1$ at time 0 is:

    $$
    \mu_1^4(0) = -l_1(0) \times \bar{\sigma}_1 \times 0.028571 = -0.05 \times 0.20 \times 0.028571 = -0.000286
    $$

    That is, $\mu_1^4(0) \approx -2.86$ basis points per year (in absolute terms).

    **The drift is negative.** This is because under the terminal measure $\mathbb{Q}^4$, forward rates with indices well below the terminal index acquire negative drifts. The larger the gap between $i$ and $m$, the more terms in the sum and the larger the (negative) drift correction. Intuitively, moving to the terminal measure changes the numéraire to $P(t, T_4)$, which is a product of all forward discount factors; this systematic adjustment pushes earlier rates downward to maintain the no-arbitrage condition.

---

**Exercise 3.** The relationship between the bond price ratio and the LIBOR rate is $P(t, T_{i-1})/P(t, T_i) = 1 + \tau_i l_i(t)$. Verify this by expressing $l_i(t)$ in terms of the bond prices. Then show that the forward LIBOR rate is a martingale under $\mathbb{Q}^{T_i}$ by identifying it as a ratio of tradable assets divided by the numéraire $P(t, T_i)$.

??? success "Solution to Exercise 3"
    **Expressing $l_i(t)$ in terms of bond prices:**

    By definition:

    $$
    l_i(t) = \frac{1}{\tau_i}\left(\frac{P(t, T_{i-1})}{P(t, T_i)} - 1\right) = \frac{P(t, T_{i-1}) - P(t, T_i)}{\tau_i\,P(t, T_i)}
    $$

    Rearranging:

    $$
    \frac{P(t, T_{i-1})}{P(t, T_i)} = 1 + \tau_i\,l_i(t)
    $$

    which confirms the bond-price-to-LIBOR relationship.

    **Showing $l_i(t)$ is a martingale under $\mathbb{Q}^{T_i}$:**

    Under $\mathbb{Q}^{T_i}$ (the forward measure with numéraire $P(t, T_i)$), any price process divided by $P(t, T_i)$ is a martingale (provided the price process represents a tradable asset or a portfolio thereof).

    Consider the portfolio: long one $T_{i-1}$-bond, short one $T_i$-bond. Its value at time $t$ is:

    $$
    V(t) = P(t, T_{i-1}) - P(t, T_i)
    $$

    This is the value of a self-financing trading strategy involving tradable zero-coupon bonds. Dividing by the numéraire $P(t, T_i)$:

    $$
    \frac{V(t)}{P(t, T_i)} = \frac{P(t, T_{i-1}) - P(t, T_i)}{P(t, T_i)} = \frac{P(t, T_{i-1})}{P(t, T_i)} - 1 = \tau_i\,l_i(t)
    $$

    Since $V(t)/P(t, T_i)$ is a martingale under $\mathbb{Q}^{T_i}$, and $\tau_i$ is a constant:

    $$
    \mathbb{E}^{T_i}\bigl[l_i(T_{i-1}) \mid \mathcal{F}(t)\bigr] = l_i(t)
    $$

    Therefore $l_i(t)$ is a $\mathbb{Q}^{T_i}$-martingale.

---

**Exercise 4.** Explain the relationship between the forward measure change formula $dW_i^{i}(t) = \frac{\tau_{i+1}\bar{\sigma}_{i+1}(t)\,l_{i+1}(t)}{\tau_{i+1}l_{i+1}(t)+1}\,dt + dW_i^{i+1}(t)$ and Girsanov's theorem. Identify the Girsanov kernel and explain why it depends on the forward rate $l_{i+1}(t)$.

??? success "Solution to Exercise 4"
    **Girsanov's theorem** states that when changing from probability measure $\mathbb{Q}$ to $\tilde{\mathbb{Q}}$ via Radon--Nikodym derivative $\Lambda_t = d\tilde{\mathbb{Q}}/d\mathbb{Q}|_{\mathcal{F}_t}$, if $d\Lambda_t/\Lambda_t = \gamma_t\,dW_t$ (where $\gamma_t$ is the Girsanov kernel), then $\tilde{W}_t = W_t - \int_0^t \gamma_s\,ds$ is a Brownian motion under $\tilde{\mathbb{Q}}$.

    The Radon--Nikodym derivative from $\mathbb{Q}^{i+1}$ to $\mathbb{Q}^i$ is:

    $$
    \lambda_{i+1}^{i}(t) = \frac{P(t, T_i)/P(0, T_i)}{P(t, T_{i+1})/P(0, T_{i+1})} = \frac{P(0, T_{i+1})}{P(0, T_i)}\bigl(1 + \tau_{i+1}\,l_{i+1}(t)\bigr)
    $$

    Computing the dynamics:

    $$
    \frac{d\lambda_{i+1}^{i}(t)}{\lambda_{i+1}^{i}(t)} = \frac{\tau_{i+1}\,\bar{\sigma}_{i+1}(t)}{\tau_{i+1}\,l_{i+1}(t) + 1}\,dW_{i+1}^{i+1}(t)
    $$

    The **Girsanov kernel** is:

    $$
    \gamma_{i+1}(t) = \frac{\tau_{i+1}\,\bar{\sigma}_{i+1}(t)}{\tau_{i+1}\,l_{i+1}(t) + 1}
    $$

    By Girsanov's theorem, the Brownian motion transforms as:

    $$
    dW_i^{i}(t) = -\rho_{i,i+1}\,\gamma_{i+1}(t)\,dt + dW_i^{i+1}(t) = -\frac{\tau_{i+1}\,\rho_{i,i+1}\,\bar{\sigma}_{i+1}(t)}{\tau_{i+1}\,l_{i+1}(t) + 1}\,dt + dW_i^{i+1}(t)
    $$

    (The correlation $\rho_{i,i+1}$ enters because $W_i$ and $W_{i+1}$ are correlated.)

    **Why the kernel depends on $l_{i+1}(t)$:** The numéraire ratio $P(t,T_i)/P(t,T_{i+1}) = 1 + \tau_{i+1}l_{i+1}(t)$ depends directly on the forward rate $l_{i+1}$. Since the Girsanov kernel is the volatility of the numéraire ratio (relative to itself), it inherits the dependence on $l_{i+1}(t)$. The factor $\tau_{i+1}l_{i+1}(t)/(1 + \tau_{i+1}l_{i+1}(t))$ represents the fraction of the bond price ratio that is attributable to the forward rate --- it is the "leverage" of the forward rate in the bond price ratio.

---

**Exercise 5.** In a three-rate LMM ($l_1, l_2, l_3$), write down the drift of each rate under the spot (rolling) measure, where the numéraire is the discretely-compounded money market account. Compare the drift structure with that under the terminal measure. Which measure leads to simpler simulation and why?

??? success "Solution to Exercise 5"
    **Three-rate LMM under the spot (rolling) measure:**

    The spot measure $\mathbb{Q}^M$ uses the discretely-compounded money market account as numéraire. The drift of each rate is:

    $$
    dl_i(t) = \bar{\sigma}_i(t)\sum_{k=\bar{m}(t)+1}^{i}\frac{\tau_k\,\bar{\sigma}_k(t)}{\tau_k\,l_k(t)+1}\,dt + \bar{\sigma}_i(t)\,dW_i^M(t)
    $$

    where $\bar{m}(t) = \min\{j : t \leq T_j\} - 1$.

    For $t < T_1$ (before the first reset), $\bar{m}(t) = 0$, so the drifts are:

    **Rate $l_1$** ($i = 1$): Sum from $k = 1$ to $1$:

    $$
    dl_1(t) = \bar{\sigma}_1(t)\frac{\tau_1\,\bar{\sigma}_1(t)}{\tau_1\,l_1(t)+1}\,dt + \bar{\sigma}_1(t)\,dW_1^M(t)
    $$

    **Rate $l_2$** ($i = 2$): Sum from $k = 1$ to $2$:

    $$
    dl_2(t) = \bar{\sigma}_2(t)\left(\frac{\tau_1\,\rho_{21}\,\bar{\sigma}_1(t)}{\tau_1\,l_1(t)+1} + \frac{\tau_2\,\bar{\sigma}_2(t)}{\tau_2\,l_2(t)+1}\right)dt + \bar{\sigma}_2(t)\,dW_2^M(t)
    $$

    **Rate $l_3$** ($i = 3$): Sum from $k = 1$ to $3$:

    $$
    dl_3(t) = \bar{\sigma}_3(t)\left(\frac{\tau_1\,\rho_{31}\,\bar{\sigma}_1(t)}{\tau_1\,l_1(t)+1} + \frac{\tau_2\,\rho_{32}\,\bar{\sigma}_2(t)}{\tau_2\,l_2(t)+1} + \frac{\tau_3\,\bar{\sigma}_3(t)}{\tau_3\,l_3(t)+1}\right)dt + \bar{\sigma}_3(t)\,dW_3^M(t)
    $$

    All drifts are **positive** under the spot measure.

    **Under the terminal measure $\mathbb{Q}^3$:**

    **Rate $l_3$** ($i = 3$): Martingale (drift = 0).

    **Rate $l_2$** ($i = 2$): Sum from $k = 3$ to $3$:

    $$
    dl_2(t) = -\bar{\sigma}_2(t)\frac{\tau_3\,\rho_{23}\,\bar{\sigma}_3(t)}{\tau_3\,l_3(t)+1}\,dt + \bar{\sigma}_2(t)\,dW_2^3(t)
    $$

    **Rate $l_1$** ($i = 1$): Sum from $k = 2$ to $3$:

    $$
    dl_1(t) = -\bar{\sigma}_1(t)\left(\frac{\tau_2\,\rho_{12}\,\bar{\sigma}_2(t)}{\tau_2\,l_2(t)+1} + \frac{\tau_3\,\rho_{13}\,\bar{\sigma}_3(t)}{\tau_3\,l_3(t)+1}\right)dt + \bar{\sigma}_1(t)\,dW_1^3(t)
    $$

    All non-martingale drifts are **negative** under the terminal measure.

    **Comparison:** Under the spot measure, the drift sum for $l_i$ runs from $k = 1$ (or $\bar{m}(t)+1$) **up to** $i$. Under the terminal measure, the sum runs from $k = i+1$ **up to** $m$. The spot measure is simpler for simulation because:

    - Rates can be simulated **in order** $l_1, l_2, l_3$: to compute $l_i$'s drift, one only needs $l_1, \ldots, l_i$, which have already been updated at the current step
    - Under the terminal measure, $l_1$'s drift depends on $l_2$ and $l_3$, creating a coupling that complicates the stepping order

---

**Exercise 6.** Show that as the tenor $\tau_i \to 0$ (continuous limit), the LMM forward rate dynamics converge to the HJM instantaneous forward rate dynamics. Specifically, identify $l_i(t)\tau_i \approx \int_{T_{i-1}}^{T_i} f(t,u)\,du$ and show that the drift condition becomes the standard HJM drift condition $\alpha(t,T) = \sigma(t,T)\int_t^T \sigma(t,u)\,du$.

??? success "Solution to Exercise 6"
    **Continuous limit of the LMM:**

    Identify the discrete forward rate with the integral of the instantaneous forward rate:

    $$
    \tau_i\,l_i(t) \approx \int_{T_{i-1}}^{T_i} f(t, u)\,du
    $$

    As $\tau_i \to 0$, $l_i(t) \to f(t, T_{i-1})$ (the instantaneous forward rate at maturity $T_{i-1}$).

    The bond price ratio becomes:

    $$
    \frac{P(t, T_{i-1})}{P(t, T_i)} = 1 + \tau_i\,l_i(t) \approx 1 + \tau_i\,f(t, T_i) \approx \exp\left(\int_{T_{i-1}}^{T_i} f(t, u)\,du\right)
    $$

    The key term in the LMM drift under the terminal measure is:

    $$
    \frac{\tau_k\,\bar{\sigma}_k(t)\,l_k(t)}{1 + \tau_k\,l_k(t)} = \frac{\tau_k\,\sigma_k(t)\,l_k(t)\,l_k(t)}{1 + \tau_k\,l_k(t)}
    $$

    For the proportional volatility specification $\bar{\sigma}_k = \sigma_k\,l_k$, as $\tau_k \to 0$:

    $$
    \frac{\tau_k\,\sigma_k\,l_k^2}{1 + \tau_k\,l_k} \approx \tau_k\,\sigma_k\,l_k^2 \to 0
    $$

    Instead, work with the absolute volatility. In the HJM framework, $f(t, T)$ satisfies:

    $$
    df(t, T) = \alpha(t, T)\,dt + \sigma(t, T)\,dW(t)
    $$

    The LMM drift under the terminal measure for a single Brownian motion factor is:

    $$
    dl_i(t) = -\bar{\sigma}_i(t)\sum_{k=i+1}^{m}\frac{\tau_k\,\bar{\sigma}_k(t)}{\tau_k\,l_k(t)+1}\,dt + \bar{\sigma}_i(t)\,dW_i^m(t)
    $$

    In the continuous limit, the sum becomes an integral. Let $\sigma^{\text{HJM}}(t, T) = \bar{\sigma}_i(t)/\tau_i$ for $T \in [T_{i-1}, T_i)$. Then the drift term:

    $$
    \sum_{k=i+1}^{m}\frac{\tau_k\,\bar{\sigma}_k(t)}{\tau_k\,l_k(t)+1} \to \int_{T_i}^{T_m} \frac{\sigma^{\text{HJM}}(t, u)}{1 + 0}\,du = \int_{T_i}^{T_m}\sigma^{\text{HJM}}(t, u)\,du
    $$

    (since $\tau_k\,l_k \to 0$ as $\tau_k \to 0$). Under the terminal measure $\mathbb{Q}^{T_m}$, the drift of the instantaneous forward rate becomes:

    $$
    \alpha^{T_m}(t, T) = -\sigma(t, T)\int_T^{T_m}\sigma(t, u)\,du
    $$

    Converting to the risk-neutral measure (where $\mathbb{Q}^{T_m}$ becomes $\mathbb{Q}$ in the continuous limit), the standard HJM no-arbitrage drift condition is recovered:

    $$
    \alpha(t, T) = \sigma(t, T)\int_t^T \sigma(t, u)\,du
    $$

    This confirms that the LMM is a discretization of the HJM framework, and its drift structure converges to the HJM drift condition in the continuous tenor limit.
