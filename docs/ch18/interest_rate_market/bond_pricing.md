# Bond Pricing

The price of a bond is the present value of its future cash flows, discounted at appropriate interest rates. This fundamental principle connects the bond market to the discount factor curve $P(t,T)$ and provides the basis for yield curve construction, interest rate risk management, and derivative pricing. This section develops the pricing framework from zero-coupon bonds through yield-to-maturity, duration, and convexity.

---

## Zero-coupon bond pricing

A **zero-coupon bond** (or discount bond) with maturity $T$ pays exactly one unit of currency at time $T$ and nothing before. Its price at time $t < T$ is the discount factor $P(t,T)$.

### Continuous compounding

Under continuous compounding, the zero-coupon bond price is related to the continuously compounded zero rate $R(t,T)$ by

$$
P(t,T) = e^{-R(t,T)(T-t)}
$$

Equivalently, the zero rate extracted from the bond price is

$$
R(t,T) = -\frac{\ln P(t,T)}{T - t}
$$

The zero rate $R(t,T)$ represents the constant rate of interest that, when compounded continuously over the interval $[t, T]$, reproduces the bond price.

### Discrete compounding

Under simple (money market) compounding with day count fraction $\delta = \tau(t, T)$, the bond price satisfies

$$
P(t,T) = \frac{1}{1 + L(t,T) \cdot \delta}
$$

where $L(t,T)$ is the simply compounded spot rate. For annual compounding with $n$ periods per year:

$$
P(t,T) = \frac{1}{\left(1 + \frac{y}{n}\right)^{n(T-t)}}
$$

where $y$ is the annually compounded yield.

!!! note "Compounding conventions"
    Different markets use different conventions. US Treasury bills use simple (money market) compounding with ACT/360 day count. US Treasury bonds use semi-annual compounding ($n = 2$) with ACT/ACT day count. The choice of convention affects the numerical value of the yield but not the bond price or discount factor.

---

## Present value of a cash flow stream

The price of any bond---zero-coupon or coupon-bearing---follows from the **value additivity principle**: the price equals the sum of present values of individual cash flows, each discounted by the appropriate discount factor.

### General pricing formula

Consider a bond that pays cash flows $c_1, c_2, \ldots, c_n$ at times $T_1 < T_2 < \cdots < T_n$. Its price at time $t < T_1$ is

$$
B(t) = \sum_{k=1}^{n} c_k \, P(t, T_k)
$$

This formula requires no model assumptions beyond the absence of arbitrage: it holds in any market where zero-coupon bonds (or equivalently, discount factors) of all relevant maturities exist.

### Coupon bond

A coupon bond with face value $N$, coupon rate $c$ (per period), and payment dates $T_1, \ldots, T_n$ pays $Nc$ at each coupon date and $N$ at maturity $T_n$. Its price is

$$
B(t) = Nc \sum_{k=1}^{n} P(t, T_k) + N \, P(t, T_n)
$$

Separating the coupon annuity from the principal repayment clarifies the two components of bond value. When the bond trades at par ($B(t) = N$), the coupon rate equals the par yield:

$$
c = y_{\mathrm{par}} = \frac{1 - P(t, T_n)}{\sum_{k=1}^{n} P(t, T_k)}
$$

---

## Yield to maturity

The **yield to maturity** (YTM) is the single discount rate that, applied uniformly to all cash flows, reproduces the observed bond price. It compresses the entire discount factor curve into a single number.

### Definition

For a bond with price $B$, cash flows $c_1, \ldots, c_n$ at times $T_1, \ldots, T_n$, the YTM $y$ is the solution of

$$
B = \sum_{k=1}^{n} \frac{c_k}{(1 + y/m)^{m(T_k - t)}}
$$

where $m$ is the compounding frequency ($m = 2$ for semi-annual, the US Treasury convention). In continuously compounded form:

$$
B = \sum_{k=1}^{n} c_k \, e^{-y(T_k - t)}
$$

The YTM equation is a polynomial of degree $n$ in the variable $x = (1 + y/m)^{-1}$. For a standard bond with positive cash flows, there is a unique positive solution by Descartes' rule of signs.

### Computation

The YTM is computed numerically by solving the pricing equation. Newton-Raphson iteration is standard:

$$
y^{(k+1)} = y^{(k)} - \frac{B(y^{(k)}) - B_{\mathrm{mkt}}}{\partial B / \partial y \big|_{y^{(k)}}}
$$

Since $\partial B / \partial y < 0$ (bond prices decrease with yield), the iteration is well-behaved and converges in 3--5 steps from a reasonable starting value.

!!! warning "YTM assumes flat term structure"
    The YTM implicitly assumes that all cash flows are discounted at the same rate. This is equivalent to a flat term structure, which rarely holds in practice. Two bonds with the same maturity but different coupon structures will generally have different YTMs even if they are priced off the same discount curve. For this reason, the zero-coupon yield curve $R(t,T)$ is preferred for pricing and risk management.

---

## Duration

Duration measures the sensitivity of a bond's price to changes in yield. It provides a first-order approximation for interest rate risk.

### Macaulay duration

The **Macaulay duration** is the weighted average time to payment, where the weights are the present values of individual cash flows:

$$
D_{\mathrm{Mac}} = \frac{1}{B} \sum_{k=1}^{n} (T_k - t) \cdot \frac{c_k}{(1 + y/m)^{m(T_k - t)}}
$$

For a zero-coupon bond, $D_{\mathrm{Mac}} = T - t$ (the time to maturity). For a coupon bond, $D_{\mathrm{Mac}} < T_n - t$ because intermediate coupon payments pull the average payment date forward.

The Macaulay duration has units of time (years) and represents the point at which the reinvestment risk and the price risk of a coupon bond exactly offset---the immunization horizon.

### Modified duration

The **modified duration** connects directly to yield sensitivity:

$$
D_{\mathrm{mod}} = \frac{D_{\mathrm{Mac}}}{1 + y/m}
$$

The price change for a small yield shift $\Delta y$ is approximately

$$
\frac{\Delta B}{B} \approx -D_{\mathrm{mod}} \cdot \Delta y
$$

This is the first-order Taylor expansion of the price-yield relationship. For continuously compounded yields, $D_{\mathrm{mod}} = D_{\mathrm{Mac}}$.

???+ note "Derivation"

    The bond price as a function of yield is $B(y) = \sum_k c_k (1 + y/m)^{-m(T_k - t)}$. Differentiating:

    $$
    \frac{dB}{dy} = -\frac{1}{1 + y/m} \sum_{k=1}^{n} (T_k - t) \cdot \frac{c_k}{(1 + y/m)^{m(T_k - t)}} = -\frac{D_{\mathrm{Mac}} \cdot B}{1 + y/m}
    $$

    Dividing both sides by $B$:

    $$
    \frac{1}{B}\frac{dB}{dy} = -\frac{D_{\mathrm{Mac}}}{1 + y/m} = -D_{\mathrm{mod}}
    $$

    $\square$

### Dollar duration and DV01

The **dollar duration** is $DD = D_{\mathrm{mod}} \cdot B$, giving the absolute price change per unit yield shift: $\Delta B \approx -DD \cdot \Delta y$. The **DV01** (dollar value of one basis point) is

$$
\mathrm{DV01} = \frac{DD}{10{,}000} = D_{\mathrm{mod}} \cdot B \cdot 0.0001
$$

representing the dollar price change for a one-basis-point (0.01%) move in yield.

---

## Convexity

Duration provides only a linear approximation. For large yield changes, the curvature of the price-yield relationship matters.

### Definition

The **convexity** is the second derivative of the price with respect to yield, normalized by the price:

$$
C = \frac{1}{B} \frac{d^2 B}{dy^2} = \frac{1}{B} \sum_{k=1}^{n} \frac{(T_k - t)(T_k - t + 1/m)}{(1 + y/m)^2} \cdot \frac{c_k}{(1 + y/m)^{m(T_k - t)}}
$$

For continuously compounded yields, the formula simplifies:

$$
C = \frac{1}{B} \sum_{k=1}^{n} (T_k - t)^2 \cdot c_k \, e^{-y(T_k - t)}
$$

### Price approximation with convexity

The second-order Taylor expansion gives a more accurate price approximation:

$$
\frac{\Delta B}{B} \approx -D_{\mathrm{mod}} \cdot \Delta y + \frac{1}{2} C \cdot (\Delta y)^2
$$

Since $C > 0$ for standard bonds (the price-yield curve is convex), the convexity correction is always positive: large yield moves in either direction produce smaller price declines (or larger price increases) than the duration approximation predicts.

!!! tip "Convexity as a desirable property"
    Convexity benefits the bondholder: if yields fall, the bond gains more than duration predicts; if yields rise, the bond loses less. Two bonds with the same duration but different convexities will have different prices when the yield curve shifts. The bond with higher convexity is worth more, and the yield difference (the convexity premium) compensates for this advantage.

---

## Continuous vs discrete compounding

The relationship between compounding conventions is essential for converting between market quotes and model inputs.

### Conversion formulas

Let $R_c$ denote the continuously compounded rate and $R_m$ the rate compounded $m$ times per year, both for the same maturity. Equating discount factors:

$$
e^{-R_c \cdot T} = \left(1 + \frac{R_m}{m}\right)^{-mT}
$$

Solving:

$$
R_c = m \ln\!\left(1 + \frac{R_m}{m}\right), \qquad R_m = m\left(e^{R_c / m} - 1\right)
$$

For simple compounding ($m = 1/T$, single period):

$$
R_c = \frac{1}{T} \ln(1 + R_s \cdot T), \qquad R_s = \frac{e^{R_c \cdot T} - 1}{T}
$$

### Forward rates under different conventions

The continuously compounded forward rate over $[T_1, T_2]$ is

$$
f_c(t; T_1, T_2) = \frac{R_c(t, T_2) \cdot T_2 - R_c(t, T_1) \cdot T_1}{T_2 - T_1} = -\frac{\ln P(t, T_2) - \ln P(t, T_1)}{T_2 - T_1}
$$

The simply compounded forward rate is

$$
F(t; T_1, T_2) = \frac{1}{T_2 - T_1}\left(\frac{P(t, T_1)}{P(t, T_2)} - 1\right)
$$

The two are related by $f_c = \frac{1}{T_2 - T_1} \ln(1 + F \cdot (T_2 - T_1))$.

---

## Bond price quoting conventions

Different bond markets use different fractional increments for price quotes. This section describes the conventions for US markets.

$$
\begin{array}{ll}
\text{corporate bonds} & \text{1/8 increments (decimalized in 1/8ths of a point)} \\
\text{government bills, notes, and bonds} & \text{1/32 increments}
\end{array}
$$

US Treasury prices are quoted in points and 32nds of a point, where one point equals \$1 per \$100 face value. For example, a quote of "99-21" means $99 + 21/32 = 99.65625$ per \$100 face value. Half-32nds are denoted with a plus sign or fraction: "99-21+" means $99 + 21.5/32 = 99.671875$, and "99-21$\frac{3}{4}$" means $99 + 21.75/32 = 99.6796875$.

You can see bonds prices quoted in 1/32nd increments [here](https://www.bloomberg.com/markets/rates-bonds/government-bonds/us). As a historical example, on 2011-10-23 the 5-year note with a 1% coupon was quoted at "99-21$\frac{3}{4}$" $= 99 + 21.75/32$, resulting in a yield of 1.07%.

[How can I understand "thirty-seconds of a dollar"?](https://english.stackexchange.com/questions/45977/how-can-i-understand-thirty-seconds-of-a-dollar)

### Clean price vs dirty price

The **clean price** (or flat price) is the quoted price. The **dirty price** (or full price, invoice price) includes accrued interest:

$$
B_{\mathrm{dirty}} = B_{\mathrm{clean}} + AI
$$

where the accrued interest is

$$
AI = Nc \cdot \frac{\text{days since last coupon}}{\text{days in coupon period}}
$$

The dirty price is the actual amount paid by the buyer. Clean prices are quoted because they eliminate the sawtooth pattern caused by accrued interest accumulating between coupon dates, making price comparisons across bonds more meaningful.

---

## Key relationships

The following diagram summarizes the relationships between the main quantities developed in this section.

$$
P(t,T) \xrightarrow{\text{invert}} R(t,T) \xrightarrow{\text{flat approx.}} y \xrightarrow{\text{sensitivity}} D_{\mathrm{mod}}, \; C
$$

The discount factor $P(t,T)$ is the fundamental quantity from which all others derive. Zero rates $R(t,T)$ provide the term structure. The yield to maturity $y$ compresses the curve into a single number for each bond. Duration and convexity measure the sensitivity of bond prices to yield changes.

!!! note "Connection to the short-rate framework"
    Under a short-rate model $dr_t = \mu(t, r_t) \, dt + \sigma(t, r_t) \, dW_t$, the zero-coupon bond price satisfies $P(t,T) = \mathbb{E}_t^{\mathbb{Q}}[e^{-\int_t^T r_s \, ds}]$. The deterministic discount factor framework of this section is recovered in the limit of zero volatility ($\sigma \to 0$), where $P(t,T) = e^{-\int_t^T f(t,s) \, ds}$ with $f(t,s)$ the deterministic forward rate. The stochastic generalization is developed in the short-rate model sections of this chapter.

---
