# Change of Numeraire: Deep Dive

You're right to be skeptical - let me show you why change of numeraire is actually a **genuinely profound alternative perspective** that reveals deep geometric structure in derivative pricing. It's not just another reformulation of no-arbitrage.

## Part I: The Fundamental Theorem

### 1.1 Numeraire and Equivalent Martingale Measure

**Definition:** A **numeraire** is any strictly positive tradable asset $N_t > 0$ that can be used as a unit of account.

**Fundamental Theorem (Geman-El Karoui-Rochet, 1995):**

If $N_t$ is a numeraire, there exists a unique equivalent probability measure $\mathbb{Q}^N$ (the **$N$-forward measure**) such that for any tradable asset $X_t$:


$$\frac{X_t}{N_t} \text{ is a } \mathbb{Q}^N\text{-martingale}$$



**This is the key:** Different numeraires induce different probability measures, but all are related by the fundamental pricing formula.

### 1.2 Change of Measure Formula

**Radon-Nikodym Derivative:**

Given two numeraires $N_t$ and $M_t$ with associated measures $\mathbb{Q}^N$ and $\mathbb{Q}^M$:


$$\boxed{\frac{d\mathbb{Q}^M}{d\mathbb{Q}^N}\Big|_{\mathcal{F}_T} = \frac{M_T/M_0}{N_T/N_0}}$$



**Proof sketch:** Both $\frac{X_t}{N_t}$ and $\frac{X_t}{M_t}$ must give the same price $X_0$:


$$X_0 = N_0 \mathbb{E}^{\mathbb{Q}^N}\left[\frac{X_T}{N_T}\right] = M_0 \mathbb{E}^{\mathbb{Q}^M}\left[\frac{X_T}{M_T}\right]$$



This determines the relationship between measures. $\square$

### 1.3 Abstract Change of Numeraire Theorem

**Theorem:** For any claim with payoff $H$ at time $T$:


$$\boxed{\frac{V_t}{N_t} = \mathbb{E}^{\mathbb{Q}^N}\left[\frac{H}{N_T} \Big| \mathcal{F}_t\right]}$$



This holds for **any** numeraire $N_t$. Different choices of $N_t$ give different (but equivalent) computational approaches.

---

## Part II: The Three Classical Numeraires

### 2.1 Money Market Account Numeraire (Risk-Neutral Measure)

**Numeraire:** $B_t = e^{rt}$

**Measure:** $\mathbb{Q} = \mathbb{Q}^B$ (the standard risk-neutral measure)

**Pricing formula:**


$$V_t = B_t \mathbb{E}^{\mathbb{Q}}\left[\frac{H}{B_T} \Big| \mathcal{F}_t\right] = \mathbb{E}^{\mathbb{Q}}\left[e^{-r(T-t)} H \Big| \mathcal{F}_t\right]$$



**Stock dynamics under $\mathbb{Q}$:**


$$dS_t = rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}$$



### 2.2 Stock Numeraire (Stock Measure)

**Numeraire:** $N_t = S_t$

**Measure:** $\mathbb{Q}^S$ (the stock measure)

**Pricing formula:**


$$\boxed{\frac{V_t}{S_t} = \mathbb{E}^{\mathbb{Q}^S}\left[\frac{H}{S_T} \Big| \mathcal{F}_t\right]}$$



**Change of measure:** The Radon-Nikodym derivative is:


$$\frac{d\mathbb{Q}^S}{d\mathbb{Q}}\Big|_{\mathcal{F}_T} = \frac{S_T/S_0}{B_T/B_0} = \frac{S_T}{S_0} e^{-rT}$$



### 2.3 Zero-Coupon Bond Numeraire (Forward Measure)

**Numeraire:** $P(t,T)$ = price at time $t$ of zero-coupon bond maturing at $T$

**Measure:** $\mathbb{Q}^T$ (the $T$-forward measure)

**Pricing formula:**


$$\boxed{V_t = P(t,T) \mathbb{E}^{\mathbb{Q}^T}\left[H \Big| \mathcal{F}_t\right]}$$



**Key property:** Under $\mathbb{Q}^T$, the forward price $F(t,T) = \frac{S_t}{P(t,T)}$ is a martingale.

---

## Part III: Deriving Stock Dynamics Under Stock Measure

### 3.1 Computing the Radon-Nikodym Derivative

Under $\mathbb{Q}$, the stock follows:


$$dS_t = rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}$$



Define:


$$Z_t = \frac{d\mathbb{Q}^S}{d\mathbb{Q}}\Big|_{\mathcal{F}_t} = \frac{S_t e^{-rt}}{S_0}$$



This is the **density process** for the measure change.

### 3.2 Dynamics of the Density Process

Apply Itô's lemma to $Z_t = S_t e^{-rt}/S_0$:


$$\begin{array}{lll}
dZ_t 
&=&\displaystyle \frac{e^{-rt}}{S_0} dS_t + S_t \frac{d(e^{-rt})}{S_0} + \frac{e^{-rt}}{S_0} dS_t \cdot d(e^{-rt})\\
&=&\displaystyle \frac{e^{-rt}}{S_0}(rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}) - \frac{r e^{-rt} S_t}{S_0} dt\\
&=&\displaystyle \frac{S_t e^{-rt}}{S_0} \sigma dW_t^{\mathbb{Q}} = Z_t \sigma dW_t^{\mathbb{Q}}
\end{array}$$



So:


$$\boxed{\frac{dZ_t}{Z_t} = \sigma dW_t^{\mathbb{Q}}}$$



This is a **local martingale** (in fact, a true martingale since $\mathbb{E}[Z_T] = 1$).

### 3.3 Girsanov's Theorem Application

By Girsanov's theorem, define:


$$W_t^{\mathbb{Q}^S} = W_t^{\mathbb{Q}} - \int_0^t \sigma ds = W_t^{\mathbb{Q}} - \sigma t$$



Then $W_t^{\mathbb{Q}^S}$ is a $\mathbb{Q}^S$-Brownian motion.

### 3.4 Stock Dynamics Under $\mathbb{Q}^S$

Rewrite the stock dynamics:


$$\begin{array}{lll}
dS_t 
&=&\displaystyle rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}\\
&=&\displaystyle rS_t dt + \sigma S_t (dW_t^{\mathbb{Q}^S} + \sigma dt)\\
&=&\displaystyle (r + \sigma^2)S_t dt + \sigma S_t dW_t^{\mathbb{Q}^S}
\end{array}$$



**Key result:**


$$\boxed{dS_t = (r + \sigma^2)S_t dt + \sigma S_t dW_t^{\mathbb{Q}^S}}$$



The drift under the stock measure is $r + \sigma^2$ instead of $r$!

---

## Part IV: Money Market Account Under Stock Measure

### 4.1 Money Market Dynamics

Under $\mathbb{Q}$: $dB_t = rB_t dt$

Under $\mathbb{Q}^S$, we need $\frac{B_t}{S_t}$ to be a martingale.

### 4.2 Apply Itô to $B_t/S_t$


$$\begin{array}{lll}
\displaystyle d\left(\frac{B_t}{S_t}\right) 
&=&\displaystyle \frac{dB_t}{S_t} - \frac{B_t}{S_t^2}dS_t + \frac{B_t}{S_t^3}(dS_t)^2\\
&=&\displaystyle \frac{rB_t dt}{S_t} - \frac{B_t}{S_t^2}\left[(r+\sigma^2)S_t dt + \sigma S_t dW_t^{\mathbb{Q}^S}\right] + \frac{B_t}{S_t^3}\sigma^2 S_t^2 dt\\
&=&\displaystyle \frac{B_t}{S_t}\left[r dt - (r+\sigma^2)dt - \sigma dW_t^{\mathbb{Q}^S} + \sigma^2 dt\right]\\
&=&\displaystyle \frac{B_t}{S_t}\left[-\sigma dW_t^{\mathbb{Q}^S}\right]
\end{array}$$



**Verification:** The drift vanishes, so $B_t/S_t$ is indeed a $\mathbb{Q}^S$-martingale! ✓

---

## Part V: Pricing Derivatives via Stock Measure

### 5.1 General Pricing Formula

For a European option with payoff $h(S_T)$:


$$V(S_t, t) = S_t \mathbb{E}^{\mathbb{Q}^S}\left[\frac{h(S_T)}{S_T} \Big| \mathcal{F}_t\right]$$



### 5.2 Example: Digital Option

Consider a **digital (binary) option** paying $\mathbf{1}_{\{S_T > K\}}$.

**Under risk-neutral measure:**


$$V_t = e^{-r(T-t)} \mathbb{Q}(S_T > K | \mathcal{F}_t)$$



**Under stock measure:**


$$V_t = S_t \mathbb{E}^{\mathbb{Q}^S}\left[\frac{\mathbf{1}_{\{S_T > K\}}}{S_T} \Big| \mathcal{F}_t\right]$$



This simplifies in certain cases...

### 5.3 Connection to Black-Scholes Formula

For a call option $h(S_T) = (S_T - K)^+$:


$$\begin{array}{lll}
C_t 
&=&\displaystyle S_t \mathbb{E}^{\mathbb{Q}^S}\left[\frac{(S_T - K)^+}{S_T} \Big| \mathcal{F}_t\right]\\
&=&\displaystyle S_t \mathbb{E}^{\mathbb{Q}^S}\left[\left(1 - \frac{K}{S_T}\right)^+ \Big| \mathcal{F}_t\right]\\
&=&\displaystyle S_t \mathbb{E}^{\mathbb{Q}^S}\left[\mathbf{1}_{\{S_T > K\}}\left(1 - \frac{K}{S_T}\right) \Big| \mathcal{F}_t\right]\\
&=&\displaystyle S_t \mathbb{Q}^S(S_T > K | \mathcal{F}_t) - K \mathbb{E}^{\mathbb{Q}^S}\left[\frac{\mathbf{1}_{\{S_T > K\}}}{S_T} \Big| \mathcal{F}_t\right]
\end{array}$$



The second term equals:


$$\mathbb{E}^{\mathbb{Q}^S}\left[\frac{\mathbf{1}_{\{S_T > K\}}}{S_T} \Big| \mathcal{F}_t\right] = \frac{1}{S_t} e^{-r(T-t)} \mathbb{Q}(S_T > K | \mathcal{F}_t)$$



Therefore:


$$\boxed{C_t = S_t \mathbb{Q}^S(S_T > K | \mathcal{F}_t) - K e^{-r(T-t)} \mathbb{Q}(S_T > K | \mathcal{F}_t)}$$



This is the **alternative representation** of Black-Scholes:
- $\mathbb{Q}^S(S_T > K)$ is the probability under the stock measure (corresponds to $N(d_1)$)
- $\mathbb{Q}(S_T > K)$ is the probability under the risk-neutral measure (corresponds to $N(d_2)$)

---

## Part VI: Deriving the PDE via Change of Numeraire

### 6.1 The Martingale Property

Under $\mathbb{Q}^S$, the process $\frac{V(S_t, t)}{S_t}$ must be a martingale.

Define:


$$u(S, t) = \frac{V(S,t)}{S}$$



Then $u(S_t, t)$ is a $\mathbb{Q}^S$-martingale.

### 6.2 Infinitesimal Generator Under $\mathbb{Q}^S$

The stock follows under $\mathbb{Q}^S$:


$$dS_t = (r+\sigma^2)S_t dt + \sigma S_t dW_t^{\mathbb{Q}^S}$$



The infinitesimal generator is:


$$\mathcal{L}^{\mathbb{Q}^S} f(S) = (r+\sigma^2)S \frac{\partial f}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 f}{\partial S^2}$$



### 6.3 Extended Generator for Time-Dependent Functions

For $u(S,t)$ to be a martingale, its extended generator must vanish:


$$\frac{\partial u}{\partial t} + \mathcal{L}^{\mathbb{Q}^S} u = 0$$




$$\boxed{\frac{\partial u}{\partial t} + (r+\sigma^2)S \frac{\partial u}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 u}{\partial S^2} = 0}$$



### 6.4 Transform Back to $V(S,t)$

Since $V(S,t) = S \cdot u(S,t)$, we compute derivatives:


$$\frac{\partial V}{\partial t} = S \frac{\partial u}{\partial t}$$




$$\frac{\partial V}{\partial S} = u + S \frac{\partial u}{\partial S}$$




$$\frac{\partial^2 V}{\partial S^2} = 2\frac{\partial u}{\partial S} + S \frac{\partial^2 u}{\partial S^2}$$



Solving for derivatives of $u$:


$$\frac{\partial u}{\partial t} = \frac{1}{S}\frac{\partial V}{\partial t}$$




$$\frac{\partial u}{\partial S} = \frac{1}{S}\frac{\partial V}{\partial S} - \frac{V}{S^2}$$




$$\frac{\partial^2 u}{\partial S^2} = \frac{1}{S}\frac{\partial^2 V}{\partial S^2} - \frac{2}{S^2}\frac{\partial V}{\partial S} + \frac{2V}{S^3}$$



### 6.5 Substitute into PDE for $u$


$$\frac{1}{S}\frac{\partial V}{\partial t} + (r+\sigma^2)S\left(\frac{1}{S}\frac{\partial V}{\partial S} - \frac{V}{S^2}\right) + \frac{1}{2}\sigma^2 S^2\left(\frac{1}{S}\frac{\partial^2 V}{\partial S^2} - \frac{2}{S^2}\frac{\partial V}{\partial S} + \frac{2V}{S^3}\right) = 0$$



Multiply through by $S$:


$$\frac{\partial V}{\partial t} + (r+\sigma^2)\frac{\partial V}{\partial S} - (r+\sigma^2)\frac{V}{S} + \frac{1}{2}\sigma^2 S\frac{\partial^2 V}{\partial S^2} - \sigma^2 \frac{\partial V}{\partial S} + \sigma^2 \frac{V}{S} = 0$$



Collect terms:


$$\frac{\partial V}{\partial t} + \left[(r+\sigma^2) - \sigma^2\right]\frac{\partial V}{\partial S} + \left[-r - \sigma^2 + \sigma^2\right]\frac{V}{S} + \frac{1}{2}\sigma^2 S\frac{\partial^2 V}{\partial S^2} = 0$$




$$\frac{\partial V}{\partial t} + r\frac{\partial V}{\partial S} - r\frac{V}{S} + \frac{1}{2}\sigma^2 S\frac{\partial^2 V}{\partial S^2} = 0$$



Multiply by $S$:


$$\boxed{\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0}$$



**We've recovered the Black-Scholes PDE!**

---

## Part VII: The Forward Measure Approach

### 7.1 Forward Price as Numeraire

Consider pricing in terms of the **forward price**:


$$F(t,T) = \frac{S_t}{P(t,T)}$$



where $P(t,T)$ is the zero-coupon bond price.

### 7.2 T-Forward Measure

Under the $T$-forward measure $\mathbb{Q}^T$:
- $F(t,T)$ is a martingale
- Numeraire is $P(t,T)$

**Pricing formula:**


$$V(t) = P(t,T) \mathbb{E}^{\mathbb{Q}^T}[h(S_T) | \mathcal{F}_t]$$



### 7.3 Forward Price Dynamics

The forward price satisfies:


$$dF(t,T) = \sigma F(t,T) d\tilde{W}_t^T$$



where $\tilde{W}_t^T$ is a $\mathbb{Q}^T$-Brownian motion.

**Key insight:** Under the forward measure, the forward price is a martingale with **no drift**!

### 7.4 Connection to Black's Formula

For constant rates, $F(t,T) = S_t e^{r(T-t)}$, and the dynamics become:


$$dF = \sigma F dW_t^{\mathbb{Q}^T}$$



This leads directly to **Black's (1976) formula** for options on forwards:


$$C_t = P(t,T)[F_t N(d_1) - K N(d_2)]$$



where:


$$d_1 = \frac{\ln(F_t/K) + \frac{1}{2}\sigma^2(T-t)}{\sigma\sqrt{T-t}}, \quad d_2 = d_1 - \sigma\sqrt{T-t}$$



---

## Part VIII: Geometric Interpretation

### 8.1 The Space of Equivalent Martingale Measures

All equivalent martingale measures form a **convex set** in the space of probability measures. Change of numeraire provides a **parameterization** of this set.

**Geometric picture:**
- Each numeraire $N$ corresponds to a point (measure $\mathbb{Q}^N$) in this space
- The map $N \mapsto \mathbb{Q}^N$ is one-to-one (in complete markets)
- Different numeraires are like different coordinate systems

### 8.2 Gauge Symmetry

Change of numeraire exhibits a **gauge symmetry** analogous to electromagnetism:

- Prices are "gauge invariant" (same value regardless of numeraire)
- Probability measures transform covariantly
- The Radon-Nikodym derivative is the "gauge transformation"

**Formal analogy:**


$$\text{Electromagnetism: } A_\mu \to A_\mu + \partial_\mu \Lambda$$




$$\text{Finance: } \mathbb{Q}^N \to \mathbb{Q}^M \text{ via } \frac{dQ^M}{dQ^N} = \frac{M_T/M_0}{N_T/N_0}$$



### 8.3 Why This Perspective Matters

1. **Computational advantage:** Some problems are simpler in certain numeraires
   - Interest rate derivatives → forward measure
   - Quanto options → foreign stock measure
   - Exchange options → one asset as numeraire

2. **Conceptual clarity:** Reveals the **relativity** of probability measures
   - No single "correct" measure
   - Choice of numeraire is conventional, like choice of units

3. **Symmetry:** Exposes hidden symmetries in pricing formulas
   - Put-call parity is a numeraire transformation
   - Duality relationships between options

---

## Part IX: Advanced Applications

### 9.1 Foreign Exchange and Quanto Options

Consider pricing a call on a foreign stock $S_t^f$ in domestic currency.

**Three natural numeraires:**
- Domestic money market: $B_t^d$
- Foreign money market: $B_t^f$  
- Foreign stock itself: $S_t^f$

Each gives different computational simplifications!

**Siegel's paradox** (1972): Forward exchange rates differ depending on which currency you choose as numeraire. Change of numeraire resolves this elegantly.

### 9.2 Stochastic Interest Rates

With stochastic rates, $P(t,T)$ is random. The forward measure $\mathbb{Q}^T$ simplifies pricing:

**Heath-Jarrow-Morton framework:**

Under $\mathbb{Q}^T$:


$$dF(t,T,T^*) = \sigma(t,T^*) \cdot \int_t^T \sigma(t,s) ds \, dt + \sigma(t,T^*) \cdot dW_t^T$$



The drift is **determined by no-arbitrage** and the choice of numeraire.

### 9.3 LIBOR Market Models

The **LIBOR market model** (Brace-Gatarek-Musiela, 1997) uses change of numeraire critically:

- Each forward LIBOR rate is a martingale under its own forward measure
- Caplets price exactly like Black's formula under appropriate numeraire
- Swaptions require additional measure changes

---

## Part X: Why This IS a Genuine Derivation

### 10.1 What Makes It Different

The change of numeraire approach:

1. **Doesn't start with delta hedging** - begins with measure theory
2. **Emphasizes measure transformation** - the Radon-Nikodym derivative as fundamental object
3. **Reveals structural properties** - gauge symmetry, relativity of measures
4. **Provides computational flexibility** - choose numeraire to simplify calculations

### 10.2 The Logical Structure

```
Fundamental Theorem (numeraire → measure)
        ↓
Choose specific numeraire (e.g., stock S_t)
        ↓
Compute Radon-Nikodym derivative
        ↓
Apply Girsanov to find dynamics under new measure
        ↓
Impose martingale property of V/N
        ↓
Extended generator vanishes → PDE
```

This is **fundamentally different** from:
- Delta hedging (replication argument)
- Risk-neutral pricing (starts with money market numeraire)

### 10.3 The Deep Insight

Change of numeraire reveals that:

- **All numeraires are created equal** (gauge symmetry)
- The "risk-neutral measure" is just one choice (money market numeraire)
- Pricing is **coordinate-independent** (manifestly invariant)
- The PDE changes form but encodes the same information

---

## Part XI: Connection to Differential Geometry

### 11.1 Fiber Bundle Structure

The space of contingent claims forms a **fiber bundle**:
- **Base space:** Time interval $[0,T]$
- **Fibers:** At each $t$, the space of $\mathcal{F}_t$-measurable random variables
- **Connection:** The martingale property defines a connection

Different numeraires correspond to different **trivializations** of this bundle.

### 11.2 The Radon-Nikodym Derivative as Gauge Field

The Radon-Nikodym derivative:


$$\eta_t^{M,N} = \frac{d\mathbb{Q}^M}{d\mathbb{Q}^N}\Big|_{\mathcal{F}_t}$$



acts like a **gauge field** connecting different trivializations:


$$\eta_t^{M,N} \cdot \eta_t^{N,P} = \eta_t^{M,P}$$



This is the **cocycle condition** from differential geometry!

### 11.3 Martingale as Parallel Transport

Under measure $\mathbb{Q}^N$, saying $\frac{V_t}{N_t}$ is a martingale means it's **parallel transported** along the time direction with respect to the connection defined by the numeraire.

---

## Summary: The Power of Change of Numeraire

### Key Insights

1. **Relativity:** No privileged probability measure; choice of numeraire is conventional
2. **Symmetry:** Gauge symmetry reveals deep structure
3. **Flexibility:** Choose numeraire to simplify specific problems
4. **Geometry:** Exposes fiber bundle structure of contingent claims

### Why It's a Genuine Alternative

- **Different starting point:** Measure theory and Radon-Nikodym derivatives
- **Different toolkit:** Girsanov theorem, measure transformations
- **Different insights:** Symmetry, relativity, geometric structure
- **Different applications:** Simplifies problems with stochastic rates, FX, etc.

The Black-Scholes PDE emerges not from replication, but from the requirement that **normalized prices are martingales under the appropriate measure**.

---

What would you like to explore further?
- The connection to quantum field theory (gauge theories)?
- Detailed applications to interest rate derivatives?
- The mathematical theory of equivalent martingale measures (Delbaen-Schachermayer)?
- The relationship between numeraire choice and hedging strategies?
