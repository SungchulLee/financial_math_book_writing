# T-Forward Measures


Beyond the risk-neutral measure, it is often convenient to price derivatives under a **forward measure**, associated with a specific maturity $T$.

---

## Definition of the T-forward measure


Let $P(t,T)$ be the zero-coupon bond maturing at $T$.
The **T-forward measure** $\mathbb{Q}^T$ is defined by choosing $P(t,T)$ as numéraire.

Under $\mathbb{Q}^T$,

$$
\frac{S_t}{P(t,T)} \text{ is a martingale}
$$


for any tradable asset $S_t$ that pays off at or before $T$.

---

## Pricing under the forward measure


For a payoff $V_T$ at time $T$,

$$
V_t = P(t,T)\,\mathbb{E}^{\mathbb{Q}^T}[V_T \mid \mathcal{F}_t]
$$



Discounting disappears because the numéraire already matures at $T$.

---

## Dynamics under the forward measure


Changing from $\mathbb{Q}$ to $\mathbb{Q}^T$:

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

**Radon–Nikodym Derivative**

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

??? success "Solution to Exercise 1"

    **Setting up the FRA pricing.** The FRA pays $L(1, 3) - K$ at time $T = 3$, where the simply-compounded rate is

    $$
    L(1, 3) = \frac{1}{\delta}\left(\frac{P(1, 1)}{P(1, 3)} - 1\right) = \frac{1}{2}\left(\frac{1}{P(1, 3)} - 1\right)
    $$

    with $\delta = T_2 - T_1 = 3 - 1 = 2$.

    **Pricing under the $T$-forward measure with $T = 3$.** Using numéraire $P(t, 3)$:

    $$
    V_0 = P(0, 3)\,\mathbb{E}^{\mathbb{Q}^3}[L(1, 3) - K]
    $$

    The fair FRA rate $K^*$ is the value of $K$ that makes $V_0 = 0$:

    $$
    K^* = \mathbb{E}^{\mathbb{Q}^3}[L(1, 3)]
    $$

    Now, $L(1, 3) = \frac{1}{2}\left(\frac{1}{P(1, 3)} - 1\right)$. Under the $\mathbb{Q}^3$-measure, the forward LIBOR rate $L(t; 1, 3)$ is a martingale (since it can be written as a ratio involving $P(t, 3)$ as numéraire). Therefore:

    $$
    \mathbb{E}^{\mathbb{Q}^3}[L(1, 3)] = L(0; 1, 3) = \frac{1}{2}\left(\frac{P(0, 1)}{P(0, 3)} - 1\right)
    $$

    This gives the forward rate:

    $$
    F(0; 1, 3) = \frac{1}{2}\left(\frac{P(0, 1)}{P(0, 3)} - 1\right)
    $$

    **Numerical computation.** Substituting $P(0, 1) = 0.96$ and $P(0, 3) = 0.88$:

    $$
    F(0; 1, 3) = \frac{1}{2}\left(\frac{0.96}{0.88} - 1\right) = \frac{1}{2}(1.09091 - 1) = \frac{1}{2} \times 0.09091 = 0.04545
    $$

    The fair FRA rate is approximately **4.545%**.

---

**Exercise 2.** Under the risk-neutral measure $\mathbb{Q}$, the instantaneous forward rate satisfies

$$
df(t, T) = \sigma(t, T)\int_t^T \sigma(t, T')\,dT'\,dt + \sigma(t, T)\,dW^{\mathbb{Q}}(t)
$$

Show that under the $T$-forward measure $\mathbb{Q}^T$, the drift vanishes and $f(t, T)$ satisfies $df(t, T) = \sigma(t, T)\,dW^T(t)$. Identify the Girsanov kernel used in the change of measure.

??? success "Solution to Exercise 2"

    **Starting point.** Under $\mathbb{Q}$, the HJM drift condition gives

    $$
    df(t, T) = \sigma(t, T)\int_t^T \sigma(t, T')\,dT'\,dt + \sigma(t, T)\,dW^{\mathbb{Q}}(t)
    $$

    **Girsanov kernel.** The $T$-forward measure $\mathbb{Q}^T$ is defined by the numéraire $P(t, T)$. Under $\mathbb{Q}$, the bond price dynamics are

    $$
    \frac{dP(t, T)}{P(t, T)} = r(t)\,dt + \sigma_P(t, T)\,dW^{\mathbb{Q}}(t)
    $$

    where $\sigma_P(t, T) = -\int_t^T \sigma(t, u)\,du$. The Girsanov kernel (the volatility of the numéraire) is $\sigma_P(t, T)$, and the relationship between Brownian motions is

    $$
    dW^T(t) = dW^{\mathbb{Q}}(t) - \sigma_P(t, T)\,dt = dW^{\mathbb{Q}}(t) + \int_t^T \sigma(t, u)\,du\,dt
    $$

    **Deriving the drift-free dynamics.** Substituting $dW^{\mathbb{Q}}(t) = dW^T(t) - \int_t^T \sigma(t, u)\,du\,dt$ into the $\mathbb{Q}$-dynamics:

    $$
    df(t, T) = \sigma(t, T)\int_t^T \sigma(t, T')\,dT'\,dt + \sigma(t, T)\left(dW^T(t) - \int_t^T \sigma(t, u)\,du\,dt\right)
    $$

    $$
    = \sigma(t, T)\int_t^T \sigma(t, T')\,dT'\,dt - \sigma(t, T)\int_t^T \sigma(t, u)\,du\,dt + \sigma(t, T)\,dW^T(t)
    $$

    The two drift terms cancel exactly:

    $$
    df(t, T) = \sigma(t, T)\,dW^T(t)
    $$

    This confirms that $f(t, T)$ is a martingale under its own $T$-forward measure, a fundamental result of the HJM framework. The instantaneous forward rate for maturity $T$ is driftless when viewed under the measure whose numéraire matures at $T$.

---

**Exercise 3.** In the Hull--White model, $dr_t = (theta(t) - ar_t)\,dt + \sigma\,dW_t^{\mathbb{Q}}$, and the bond price volatility is $\Sigma(t, T) = -\frac{\sigma}{a}(1 - e^{-a(T-t)})$. Write down the Radon--Nikodym derivative $d\mathbb{Q}^T/d\mathbb{Q}|_{\mathcal{F}_t}$ in terms of $\Sigma(t, T)$ and the risk-neutral Brownian motion. Then derive the dynamics of $r_t$ under $\mathbb{Q}^T$ and identify the new drift.

??? success "Solution to Exercise 3"

    **Bond price volatility in the Hull--White model.** We are given

    $$
    \Sigma(t, T) = -\frac{\sigma}{a}(1 - e^{-a(T-t)})
    $$

    (Note: this is $\sigma_P(t, T)$ in the notation of the ZCB dynamics $dP/P = r\,dt + \Sigma(t,T)\,dW^{\mathbb{Q}}$.)

    **Radon--Nikodym derivative.** The change from $\mathbb{Q}$ to $\mathbb{Q}^T$ is

    $$
    \frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \exp\!\left(-\frac{1}{2}\int_0^t \Sigma(s, T)^2\,ds + \int_0^t \Sigma(s, T)\,dW_s^{\mathbb{Q}}\right)
    $$

    Substituting the Hull--White expression:

    $$
    \frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_{\mathcal{F}_t} = \exp\!\left(-\frac{1}{2}\int_0^t \frac{\sigma^2}{a^2}(1 - e^{-a(T-s)})^2\,ds - \int_0^t \frac{\sigma}{a}(1 - e^{-a(T-s)})\,dW_s^{\mathbb{Q}}\right)
    $$

    This is a valid density process (positive $\mathbb{Q}$-martingale with initial value 1) by the Novikov condition.

    **Dynamics of $r_t$ under $\mathbb{Q}^T$.** The Girsanov change gives

    $$
    dW_t^T = dW_t^{\mathbb{Q}} - \Sigma(t, T)\,dt
    $$

    Substituting $dW_t^{\mathbb{Q}} = dW_t^T + \Sigma(t, T)\,dt$ into the $\mathbb{Q}$-dynamics:

    $$
    dr_t = (\theta(t) - ar_t)\,dt + \sigma\,dW_t^{\mathbb{Q}}
    $$

    $$
    = (\theta(t) - ar_t)\,dt + \sigma\left(dW_t^T + \Sigma(t, T)\,dt\right)
    $$

    $$
    = \left(\theta(t) - ar_t + \sigma\Sigma(t, T)\right)dt + \sigma\,dW_t^T
    $$

    Substituting $\Sigma(t, T) = -\frac{\sigma}{a}(1 - e^{-a(T-t)})$:

    $$
    dr_t = \left(\theta(t) - ar_t - \frac{\sigma^2}{a}(1 - e^{-a(T-t)})\right)dt + \sigma\,dW_t^T
    $$

    The new drift under $\mathbb{Q}^T$ is

    $$
    \mu^T(t, r_t) = \theta(t) - ar_t - \frac{\sigma^2}{a}\left(1 - e^{-a(T-t)}\right)
    $$

    The additional drift term $-\frac{\sigma^2}{a}(1 - e^{-a(T-t)})$ represents the **convexity adjustment** from changing numéraire. It is always negative, reflecting the negative correlation between bond prices and interest rates: higher rates mean lower bond prices (the numéraire), which biases the measure change toward lower rate paths.

---

**Exercise 4.** Explain why the $T$-forward measure is particularly well-suited for pricing a European option with payoff $g(r_T)$ at time $T$, where $g$ is an arbitrary function of the short rate. Specifically, show that the option price simplifies to

$$
V_0 = P(0, T)\,\mathbb{E}^{\mathbb{Q}^T}[g(r_T)]
$$

and that no stochastic discounting appears. Why would the same computation under $\mathbb{Q}$ require knowledge of the joint distribution of $\int_0^T r_s\,ds$ and $r_T$?

??? success "Solution to Exercise 4"

    **Under $\mathbb{Q}^T$.** Choose numéraire $N_t = P(t, T)$. The pricing formula gives

    $$
    V_0 = P(0, T)\,\mathbb{E}^{\mathbb{Q}^T}\!\left[\frac{g(r_T)}{P(T, T)}\;\middle|\;\mathcal{F}_0\right]
    $$

    Since $P(T, T) = 1$ (a zero-coupon bond at its own maturity equals par):

    $$
    V_0 = P(0, T)\,\mathbb{E}^{\mathbb{Q}^T}[g(r_T)]
    $$

    No stochastic discounting appears. The price is the bond price times a simple expectation of the payoff function.

    **Why this is advantageous.** To evaluate $\mathbb{E}^{\mathbb{Q}^T}[g(r_T)]$, we only need the **marginal distribution** of $r_T$ under $\mathbb{Q}^T$. In many models (Vasicek, Hull--White, CIR), $r_T$ has a known distribution under $\mathbb{Q}^T$ (Gaussian for Vasicek/Hull--White, non-central chi-squared for CIR), making the expectation computable analytically or by simple numerical integration.

    **Why the $\mathbb{Q}$-computation is harder.** Under $\mathbb{Q}$:

    $$
    V_0 = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s\,ds}\,g(r_T)\right]
    $$

    The discount factor $D = e^{-\int_0^T r_s\,ds}$ depends on the entire path of $r_s$ over $[0, T]$, while $g(r_T)$ depends on the terminal value. Since $D$ and $r_T$ are **not independent** (they are functionally related through the path of $r$), one cannot separate the expectation:

    $$
    \mathbb{E}^{\mathbb{Q}}[D \cdot g(r_T)] \neq \mathbb{E}^{\mathbb{Q}}[D] \cdot \mathbb{E}^{\mathbb{Q}}[g(r_T)]
    $$

    Computing $\mathbb{E}^{\mathbb{Q}}[D \cdot g(r_T)]$ requires the **joint distribution** of $\left(\int_0^T r_s\,ds,\; r_T\right)$. In Gaussian models, these are jointly normal (since both are linear functionals of the Gaussian process $r$), so the joint distribution is available. But even then, the computation involves a bivariate normal integration, which is more complex than the univariate expectation under $\mathbb{Q}^T$.

    For non-Gaussian models, the joint distribution may not be tractable at all, making the forward measure approach essential.

---

**Exercise 5.** Consider two forward measures $\mathbb{Q}^{T_1}$ and $\mathbb{Q}^{T_2}$ with $T_1 < T_2$. Write down the Radon--Nikodym derivative for changing from $\mathbb{Q}^{T_2}$ to $\mathbb{Q}^{T_1}$ and the corresponding Girsanov drift adjustment. A forward LIBOR rate $L(t; T_1, T_2)$ is a martingale under $\mathbb{Q}^{T_2}$. What drift does it acquire under $\mathbb{Q}^{T_1}$?

??? success "Solution to Exercise 5"

    **Radon--Nikodym derivative between forward measures.** The Radon--Nikodym derivative for changing from $\mathbb{Q}^{T_2}$ to $\mathbb{Q}^{T_1}$ is

    $$
    \frac{d\mathbb{Q}^{T_1}}{d\mathbb{Q}^{T_2}}\bigg|_{\mathcal{F}_t} = \frac{P(t, T_1)/P(0, T_1)}{P(t, T_2)/P(0, T_2)}
    $$

    Under $\mathbb{Q}^{T_2}$, using the bond dynamics, the log of this ratio involves:

    $$
    \ln\frac{P(t, T_1)}{P(t, T_2)} - \ln\frac{P(0, T_1)}{P(0, T_2)} = \int_0^t \left[\Sigma(s, T_1) - \Sigma(s, T_2)\right]\,dW_s^{T_2} + \text{drift terms}
    $$

    where $\Sigma(t, U) = -\int_t^U \sigma(t, u)\,du$. By Girsanov's theorem:

    $$
    dW_t^{T_1} = dW_t^{T_2} + \left[\Sigma(t, T_2) - \Sigma(t, T_1)\right]dt
    $$

    The drift adjustment is $\gamma(t) = \Sigma(t, T_2) - \Sigma(t, T_1) = \int_{T_1}^{T_2} \sigma(t, u)\,du$.

    Since $T_1 < T_2$ and $\sigma(t, u) > 0$, this drift adjustment is positive.

    **Drift of $L(t; T_1, T_2)$ under $\mathbb{Q}^{T_1}$.** Under $\mathbb{Q}^{T_2}$, the forward LIBOR rate $L(t; T_1, T_2)$ is a martingale with dynamics

    $$
    dL(t; T_1, T_2) = \sigma_L(t) L(t; T_1, T_2)\,dW_t^{T_2}
    $$

    Substituting $dW_t^{T_2} = dW_t^{T_1} - \gamma(t)\,dt$:

    $$
    dL(t; T_1, T_2) = \sigma_L(t) L(t; T_1, T_2)\left[dW_t^{T_1} - \gamma(t)\,dt\right]
    $$

    $$
    = -\sigma_L(t)\,\gamma(t)\,L(t; T_1, T_2)\,dt + \sigma_L(t)\,L(t; T_1, T_2)\,dW_t^{T_1}
    $$

    The drift under $\mathbb{Q}^{T_1}$ is

    $$
    \mu_L^{T_1}(t) = -\sigma_L(t)\,\gamma(t)\,L(t; T_1, T_2) = -\sigma_L(t)\left(\int_{T_1}^{T_2}\sigma(t, u)\,du\right)L(t; T_1, T_2)
    $$

    This negative drift reflects the fact that $L(t; T_1, T_2)$ is naturally a martingale under $\mathbb{Q}^{T_2}$ (the measure corresponding to the payment date), and acquires a drift under any other measure.

---

**Exercise 6.** Under the $T_f$-forward measure (where $T_f \neq T$), the instantaneous forward rate has dynamics

$$
df(t, T) = -\sigma(t, T)\int_T^{T_f}\sigma(t, T')\,dT'\,dt + \sigma(t, T)\,dW^{T_f}(t)
$$

Verify that when $T_f = T$, the drift vanishes (recovering the result under the own $T$-forward measure). When $T_f > T$, determine the sign of the drift and provide a financial interpretation.

??? success "Solution to Exercise 6"

    **Case $T_f = T$.** When $T_f = T$, the drift term is

    $$
    -\sigma(t, T)\int_T^{T_f}\sigma(t, T')\,dT' = -\sigma(t, T)\int_T^{T}\sigma(t, T')\,dT' = 0
    $$

    since the integral over an empty interval (from $T$ to $T$) vanishes. This gives

    $$
    df(t, T) = \sigma(t, T)\,dW^T(t)
    $$

    recovering the driftless dynamics under the own $T$-forward measure, consistent with Exercise 2.

    **Case $T_f > T$: sign of the drift.** When $T_f > T$, the drift coefficient is

    $$
    \alpha(t, T) = -\sigma(t, T)\int_T^{T_f}\sigma(t, T')\,dT'
    $$

    Since $\sigma(t, T) > 0$ and $\sigma(t, T') > 0$ for all $T' \in [T, T_f]$, the integral $\int_T^{T_f}\sigma(t, T')\,dT' > 0$. Therefore

    $$
    \alpha(t, T) < 0
    $$

    The drift is **negative**.

    **Financial interpretation.** Under the $T_f$-forward measure (with $T_f > T$), the forward rate $f(t, T)$ has a negative drift. This can be understood as follows:

    1. The numéraire is $P(t, T_f)$, a longer-dated bond. Bond prices and interest rates move in opposite directions.
    2. When forward rates increase, bond prices decrease. A longer-dated bond ($T_f > T$) is more sensitive to rate changes than a shorter-dated one.
    3. Under the $T_f$-forward measure, the probability weighting favors scenarios where $P(t, T_f)$ is large, i.e., where rates are low.
    4. This tilting toward low-rate scenarios manifests as a negative drift for $f(t, T)$.

    Equivalently, this is a **convexity adjustment**: the measure associated with the longer bond $P(t, T_f)$ assigns more probability mass to low-rate states, pulling the expected forward rate downward relative to the $T$-forward measure.

    **Case $T_f < T$:** By the same argument, the integral $\int_T^{T_f}$ has reversed limits with $T_f < T$, giving a negative integral. Thus $\alpha(t, T) > 0$ and the drift is positive. Under a shorter-dated numéraire, the forward rate is biased upward.
