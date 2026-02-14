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
