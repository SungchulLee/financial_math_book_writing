# T-Forward Measures


Beyond the risk-neutral measure, it is often convenient to price derivatives under a **forward measure**, associated with a specific maturity \(T\).

---

## Definition of the T-forward measure


Let \(P(t,T)\) be the zero-coupon bond maturing at \(T\).
The **T-forward measure** \(\mathbb{Q}^T\) is defined by choosing \(P(t,T)\) as numéraire.

Under \(\mathbb{Q}^T\),

\[
\frac{S_t}{P(t,T)} \text{ is a martingale}
\]


for any tradable asset \(S_t\) that pays off at or before \(T\).

---

## Pricing under the forward measure


For a payoff \(V_T\) at time \(T\),

\[
V_t = P(t,T)\,\mathbb{E}^{\mathbb{Q}^T}[V_T \mid \mathcal{F}_t].
\]



Discounting disappears because the numéraire already matures at \(T\).

---

## Dynamics under the forward measure


Changing from \(\mathbb{Q}\) to \(\mathbb{Q}^T\):
- alters drift terms,
- leaves volatilities unchanged,
- simplifies pricing of forwards, FRAs, and caps.

Many rates become martingales under their natural forward measures.

---

## Practical importance


Forward measures are especially useful for:
- caplets and floorlets,
- forward-starting contracts,
- simplifying drift terms in HJM and LMM.

---

## Key takeaways


- Forward measures use zero-coupon bonds as numeraires.
- Pricing simplifies to expectation without discounting.
- Measure choice is a powerful modeling tool.

---

## Further reading


- Brigo & Mercurio, forward measures.
- Jamshidian, numéraire techniques.

---

## QuantPie Derivation: Change of Numeraire

### Instantaneous Forward Rate Dynamics under Different Measures

**Risk Neutral Measure:**

$$\begin{array}{lllll}
\text{Risk Neutral}&&
\displaystyle
df(t,T)
&=&\displaystyle
\left(\sigma(t,T)\int_t^T\sigma(t,T')dT'\right)dt+\sigma(t,T)dW^\mathbb{Q}(t)\\
\end{array}$$

**T Forward Measure:**

$$\begin{array}{lllll}
\text{$T$ Forward}&&
\displaystyle
df(t,T)
&=&\displaystyle
\sigma(t,T)dW^T(t)\\
\end{array}$$

**$T_f$ Forward Measure:**

$$\begin{array}{lllll}
\text{$T_f$ Forward}&&
\displaystyle
df(t,T)
&=&\displaystyle
-\left(\sigma(t,T)\int_T^{T_f}\sigma(t,T')dT'\right)dt
+\sigma(t,T)dW^{T_f}(t)\\
\end{array}$$

### Forward Rate as a Markov Process

$f(t,T)$, as a function of $t$, is a Markov process.

$$\begin{array}{lllll}
\displaystyle
f(t,T)
=
f(0,T)+
\int_0^t\left(\sigma(t',T)\int_{t'}^T\sigma(t',T')dT'\right)dt'+\int_0^t\sigma(t',T)dW^\mathbb{Q}(t')
\end{array}$$

$$\begin{array}{lllll}
\displaystyle
f(t+\Delta,T)
=
f(0,T)+
\int_0^{t+\Delta}\left(\sigma(t',T)\int_{t'}^T\sigma(t',T')dT'\right)dt'+\int_0^{t+\Delta}\sigma(t',T)dW^\mathbb{Q}(t')
\end{array}$$

$$\begin{array}{lllll}
\displaystyle
f(t+\Delta,T)-f(t,T)
=
\int_t^{t+\Delta}\left(\sigma(t',T)\int_{t'}^T\sigma(t',T')dT'\right)dt'+\int_t^{t+\Delta}\sigma(t',T)dW^\mathbb{Q}(t')
\end{array}$$

### T-Forward Measure: Direct Computation

**Instantaneous Forward Rate Dynamics**

$$\begin{array}{lllll}
\displaystyle
df(t,T)
=
\mu^\mathbb{Q}(t,T)dt+\sigma(t,T)dW^{\mathbb{Q}}(t)
\end{array}$$

**ZCB Dynamics**

$$\begin{array}{lllll}
\displaystyle
\frac{dP(t,T)}{P(t,T)}
=
r(t)dt+\sigma_P(t,T)dW^{\mathbb{Q}}(t)
\end{array}$$

$$\begin{array}{lllll}
\displaystyle
d\log P(t,T)
=
\left(r(t)-\frac{1}{2}\sigma_P^2(t,T)\right)dt+\sigma_P(t,T)dW^{\mathbb{Q}}(t)\\
\end{array}$$

$$\begin{array}{lllll}
\displaystyle
\log P(t,T)-\log P(0,T)
=
\int_0^t\left(r(t')-\frac{1}{2}\sigma_P^2(t',T)\right)dt'+\int_0^t\sigma_P(t',T)dW^{\mathbb{Q}}(t')\\
\end{array}$$

$$\begin{array}{lllll}
\displaystyle
\frac{P(t,T)}{P(0,T)}
=
\text{exp}\left(\int_0^t\left(r(t')-\frac{1}{2}\sigma_P^2(t',T)\right)dt'+\int_0^t\sigma_P(t',T)dW^{\mathbb{Q}}(t')\right)
\end{array}$$

**Radon-Nikodym Derivative**

$$\begin{array}{lllll}
\displaystyle
\lambda_\mathbb{Q}^T(t)
&=&\displaystyle
\displaystyle
\frac{d\mathbb{Q}^T}{d\mathbb{Q}}\Big{|}_{{\cal F}(t)}\\
&=&\displaystyle
\frac{P(t,T)/P(0,T)}{M(t)/M(0)}\\
&=&\displaystyle
\text{exp}\left(
-\int_0^tr(t')dt'
+\int_0^t\left(r(t')-\frac{1}{2}\sigma_P^2(t',T)\right)dt'+\int_0^t\sigma_P(t',T)dW^{\mathbb{Q}}(t')\right)\\
&=&\displaystyle
\text{exp}\left(
-\frac{1}{2}\int_0^t\sigma_P^2(t',T)dt'+\int_0^t\sigma_P(t',T)dW^\mathbb{Q}(t')
\right)\\
\end{array}$$

**Girsanov Theorem**

$$\begin{array}{lllll}
\displaystyle
dW^T(t)=dW^{\mathbb{Q}}(t)-\sigma_P(t,T)dt
\end{array}$$

where

$$\begin{array}{lllll}
\displaystyle
\sigma_P(t,T)
=
-\int_t^T\sigma(t',T)dt'
\end{array}$$

**Forward Rate Dynamics under $\mathbb{Q}^T$**

$$\begin{array}{lllll}
\displaystyle
df(t,T)
&=&\displaystyle
\left(\sigma(t,T)\int_t^T\sigma(t,T')dT'\right)dt
+\sigma(t,T)dW^{\mathbb{Q}}(t)\\
&=&\displaystyle
\left(\sigma(t,T)\int_t^T\sigma(t,T')dT'\right)dt
+\sigma(t,T)\left(
dW^T(t)-\left(\int_t^T\sigma(t,T')dT'\right)dt
\right)\\
&=&\displaystyle
\sigma(t,T)dW^T(t)
\end{array}$$

---

## Exercises

**Exercise 1.** Let $P(0, 1) = 0.96$ and $P(0, 3) = 0.88$. A forward rate agreement (FRA) pays $L(1, 3) - K$ at time $T = 3$, where $L(1, 3)$ is the simply-compounded rate for the period $[1, 3]$. Using the $T$-forward measure with $T = 3$, show that the fair FRA rate equals the forward rate $F(0; 1, 3) = \frac{1}{2}\left(\frac{P(0,1)}{P(0,3)} - 1\right)$. Compute its numerical value.

---

**Exercise 2.** Under the risk-neutral measure $\mathbb{Q}$, the instantaneous forward rate satisfies

$$
df(t, T) = \sigma(t, T)\int_t^T \sigma(t, T')\,dT'\,dt + \sigma(t, T)\,dW^{\mathbb{Q}}(t)
$$

Show that under the $T$-forward measure $\mathbb{Q}^T$, the drift vanishes and $f(t, T)$ satisfies $df(t, T) = \sigma(t, T)\,dW^T(t)$. Identify the Girsanov kernel used in the change of measure.

---

**Exercise 3.** In the Hull--White model, $dr_t = (theta(t) - ar_t)\,dt + \sigma\,dW_t^{\mathbb{Q}}$, and the bond price volatility is $\Sigma(t, T) = -\frac{\sigma}{a}(1 - e^{-a(T-t)})$. Write down the Radon--Nikodym derivative $d\mathbb{Q}^T/d\mathbb{Q}|_{\mathcal{F}_t}$ in terms of $\Sigma(t, T)$ and the risk-neutral Brownian motion. Then derive the dynamics of $r_t$ under $\mathbb{Q}^T$ and identify the new drift.

---

**Exercise 4.** Explain why the $T$-forward measure is particularly well-suited for pricing a European option with payoff $g(r_T)$ at time $T$, where $g$ is an arbitrary function of the short rate. Specifically, show that the option price simplifies to

$$
V_0 = P(0, T)\,\mathbb{E}^{\mathbb{Q}^T}[g(r_T)]
$$

and that no stochastic discounting appears. Why would the same computation under $\mathbb{Q}$ require knowledge of the joint distribution of $\int_0^T r_s\,ds$ and $r_T$?

---

**Exercise 5.** Consider two forward measures $\mathbb{Q}^{T_1}$ and $\mathbb{Q}^{T_2}$ with $T_1 < T_2$. Write down the Radon--Nikodym derivative for changing from $\mathbb{Q}^{T_2}$ to $\mathbb{Q}^{T_1}$ and the corresponding Girsanov drift adjustment. A forward LIBOR rate $L(t; T_1, T_2)$ is a martingale under $\mathbb{Q}^{T_2}$. What drift does it acquire under $\mathbb{Q}^{T_1}$?

---

**Exercise 6.** Under the $T_f$-forward measure (where $T_f \neq T$), the instantaneous forward rate has dynamics

$$
df(t, T) = -\sigma(t, T)\int_T^{T_f}\sigma(t, T')\,dT'\,dt + \sigma(t, T)\,dW^{T_f}(t)
$$

Verify that when $T_f = T$, the drift vanishes (recovering the result under the own $T$-forward measure). When $T_f > T$, determine the sign of the drift and provide a financial interpretation.
