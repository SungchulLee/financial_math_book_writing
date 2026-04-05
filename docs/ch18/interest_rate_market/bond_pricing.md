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

## Exercises

**Exercise 1.** A zero-coupon bond with face value \$100 and maturity $T = 2$ years has a market price of \$94.50. Compute the continuously compounded zero rate $R(0, 2)$, the semi-annually compounded yield, and the simply compounded rate. Verify that all three rates produce the same discount factor.

??? success "Solution to Exercise 1"

    We are given a zero-coupon bond with face value \$100, maturity $T = 2$ years, and price $B = 94.50$.

    **Continuously compounded zero rate.** From $P(0,2) = e^{-R_c \cdot 2}$ with $P(0,2) = 94.50/100 = 0.9450$:

    $$
    R_c = -\frac{\ln P(0,2)}{T} = -\frac{\ln(0.9450)}{2} = \frac{0.056570}{2} = 0.028285
    $$

    So $R_c \approx 2.8285\%$.

    **Semi-annually compounded yield.** From $P(0,2) = (1 + y/2)^{-2 \cdot 2} = (1 + y/2)^{-4}$:

    $$
    (1 + y/2)^4 = \frac{1}{0.9450} \implies 1 + y/2 = (1.05820)^{1/4} = 1.014285
    $$

    $$
    y = 2 \times 0.014285 = 0.028570
    $$

    So $y \approx 2.8570\%$.

    **Simply compounded rate.** From $P(0,2) = \frac{1}{1 + R_s \cdot 2}$:

    $$
    R_s = \frac{1 - P(0,2)}{2 \cdot P(0,2)} = \frac{1 - 0.9450}{2 \times 0.9450} = \frac{0.0550}{1.8900} = 0.029101
    $$

    So $R_s \approx 2.9101\%$.

    **Verification.** All three rates must produce the same discount factor $P(0,2) = 0.9450$:

    $$
    e^{-0.028285 \times 2} = e^{-0.056570} = 0.9450
    $$

    $$
    (1 + 0.028570/2)^{-4} = (1.014285)^{-4} = 0.9450
    $$

    $$
    \frac{1}{1 + 0.029101 \times 2} = \frac{1}{1.058201} = 0.9450
    $$

    All three agree, confirming that the rates differ only in compounding convention, not in economic content.

---

**Exercise 2.** A coupon bond with face value $N = 100$, annual coupon rate $c = 5\%$, and semi-annual payments matures in 3 years. The discount factors are $P(0, 0.5) = 0.985$, $P(0, 1.0) = 0.968$, $P(0, 1.5) = 0.950$, $P(0, 2.0) = 0.930$, $P(0, 2.5) = 0.910$, $P(0, 3.0) = 0.889$. Compute the bond price and the par yield for a 3-year semi-annual bond.

??? success "Solution to Exercise 2"

    The bond pays semi-annual coupons of $Nc/2 = 100 \times 0.05/2 = 2.50$ at each of the six payment dates, plus the face value $N = 100$ at maturity.

    **Bond price.** Using $B = Nc \sum_k P(0,T_k) + N \cdot P(0,T_n)$ with semi-annual coupons:

    $$
    B = 2.50 \times (0.985 + 0.968 + 0.950 + 0.930 + 0.910 + 0.889) + 100 \times 0.889
    $$

    $$
    B = 2.50 \times 5.632 + 88.9 = 14.08 + 88.9 = 102.98
    $$

    **Par yield.** The par yield $c_{\mathrm{par}}$ (per period) satisfies $B = N$ when the coupon rate equals $c_{\mathrm{par}}$:

    $$
    c_{\mathrm{par}} = \frac{1 - P(0, T_n)}{\sum_{k=1}^{n} P(0, T_k)} = \frac{1 - 0.889}{5.632} = \frac{0.111}{5.632} = 0.019709
    $$

    This is the semi-annual par coupon rate. The annualized par yield is $2 \times 0.019709 = 3.9418\%$. This means a 3-year semi-annual bond priced at par would have an annual coupon rate of approximately $3.94\%$.

---

**Exercise 3.** Derive the Newton-Raphson iteration for computing the yield to maturity of a coupon bond. For the bond in Exercise 2 with computed price $B$, perform two Newton-Raphson iterations starting from $y_0 = 0.04$ (semi-annual compounding). Show that the derivative $dB/dy$ involves the Macaulay duration.

??? success "Solution to Exercise 3"

    **Newton-Raphson derivation.** The YTM $y$ solves $B(y) = B_{\mathrm{mkt}}$ where, under semi-annual compounding:

    $$
    B(y) = \sum_{k=1}^{n} \frac{c_k}{(1 + y/2)^{2T_k}}
    $$

    The Newton-Raphson update is:

    $$
    y^{(j+1)} = y^{(j)} - \frac{B(y^{(j)}) - B_{\mathrm{mkt}}}{B'(y^{(j)})}
    $$

    The derivative is:

    $$
    B'(y) = \frac{dB}{dy} = -\sum_{k=1}^{n} \frac{T_k \cdot c_k}{(1 + y/2)^{2T_k + 1}} = -\frac{1}{1 + y/2} \sum_{k=1}^{n} T_k \cdot \frac{c_k}{(1 + y/2)^{2T_k}}
    $$

    Recognizing that $D_{\mathrm{Mac}} = \frac{1}{B}\sum_k T_k \cdot \frac{c_k}{(1+y/2)^{2T_k}}$, we have:

    $$
    B'(y) = -\frac{D_{\mathrm{Mac}} \cdot B}{1 + y/2} = -D_{\mathrm{mod}} \cdot B
    $$

    So the Newton-Raphson iteration is $y^{(j+1)} = y^{(j)} + \frac{B(y^{(j)}) - B_{\mathrm{mkt}}}{D_{\mathrm{mod}}(y^{(j)}) \cdot B(y^{(j)})}$.

    **Numerical iterations** with $B_{\mathrm{mkt}} = 102.98$ and $y_0 = 0.04$.

    *Iteration 1:* The cash flows are $c_k = 2.50$ for $k = 1,\ldots,5$ and $c_6 = 102.50$, at times $T_k = 0.5, 1.0, 1.5, 2.0, 2.5, 3.0$.

    $$
    B(0.04) = \frac{2.50}{(1.02)^1} + \frac{2.50}{(1.02)^2} + \frac{2.50}{(1.02)^3} + \frac{2.50}{(1.02)^4} + \frac{2.50}{(1.02)^5} + \frac{102.50}{(1.02)^6}
    $$

    $$
    = 2.4510 + 2.4029 + 2.3558 + 2.3096 + 2.2643 + 91.0000 = 102.7836
    $$

    Computing the Macaulay duration at $y = 0.04$:

    $$
    D_{\mathrm{Mac}} = \frac{1}{102.7836}\bigl(0.5(2.4510) + 1.0(2.4029) + 1.5(2.3558) + 2.0(2.3096) + 2.5(2.2643) + 3.0(91.0000)\bigr)
    $$

    $$
    = \frac{1.2255 + 2.4029 + 3.5337 + 4.6192 + 5.6608 + 273.0000}{102.7836} = \frac{290.4421}{102.7836} = 2.8258
    $$

    $$
    D_{\mathrm{mod}} = \frac{2.8258}{1.02} = 2.7704
    $$

    $$
    y_1 = 0.04 + \frac{102.7836 - 102.98}{2.7704 \times 102.7836} = 0.04 + \frac{-0.1964}{284.7460} = 0.04 - 0.000690 = 0.039310
    $$

    *Iteration 2:* Recomputing $B(0.039310)$ and repeating the procedure yields a further correction of order $10^{-6}$, demonstrating the rapid quadratic convergence of Newton-Raphson. The YTM converges to approximately $y \approx 3.93\%$, consistent with the par yield computed in Exercise 2.

---

**Exercise 4.** A 10-year bond with 6% annual coupon (paid semi-annually) and face value \$100 has a yield to maturity of 5%. Compute the Macaulay duration, modified duration, and DV01. If the yield increases by 25 basis points, estimate the percentage price change using the duration approximation.

??? success "Solution to Exercise 4"

    The bond has $N = 100$, coupon $= 6\%$ paid semi-annually (so $c = 3$ per period), $n = 20$ periods over 10 years, and $y = 5\%$ (i.e., $y/2 = 2.5\%$ per period).

    **Bond price.** First compute:

    $$
    B = 3 \sum_{k=1}^{20} \frac{1}{(1.025)^k} + \frac{100}{(1.025)^{20}}
    $$

    Using the annuity formula $\sum_{k=1}^{20}(1.025)^{-k} = \frac{1 - (1.025)^{-20}}{0.025}$:

    $$
    (1.025)^{20} = 1.63862, \quad (1.025)^{-20} = 0.61027
    $$

    $$
    \sum_{k=1}^{20}(1.025)^{-k} = \frac{1 - 0.61027}{0.025} = 15.5892
    $$

    $$
    B = 3 \times 15.5892 + 100 \times 0.61027 = 46.7676 + 61.0271 = 107.7946
    $$

    **Macaulay duration.**

    $$
    D_{\mathrm{Mac}} = \frac{1}{B} \sum_{k=1}^{20} \frac{k/2 \cdot c_k}{(1.025)^k}
    $$

    where $c_k = 3$ for $k = 1,\ldots,19$ and $c_{20} = 103$. Using the standard identity for the weighted sum:

    $$
    \sum_{k=1}^{20} \frac{k}{2} \cdot \frac{3}{(1.025)^k} = \frac{3}{2}\sum_{k=1}^{20} \frac{k}{(1.025)^k}
    $$

    The sum $\sum_{k=1}^{n} k \cdot v^k = \frac{v(1 - (n+1)v^n + nv^{n+1})}{(1-v)^2}$ with $v = 1/1.025$, $n = 20$ gives $\sum_{k=1}^{20} k \cdot v^k = 166.207$. Then:

    $$
    \frac{3}{2} \times 166.207 = 249.311
    $$

    For the principal term: $\frac{20}{2} \cdot \frac{100}{(1.025)^{20}} = 10 \times 61.027 = 610.271$.

    $$
    D_{\mathrm{Mac}} = \frac{249.311 + 610.271}{107.7946} = \frac{859.582}{107.7946} \approx 7.974 \text{ years}
    $$

    **Modified duration.**

    $$
    D_{\mathrm{mod}} = \frac{D_{\mathrm{Mac}}}{1 + y/2} = \frac{7.974}{1.025} \approx 7.779 \text{ years}
    $$

    **DV01.**

    $$
    \mathrm{DV01} = D_{\mathrm{mod}} \times B \times 0.0001 = 7.779 \times 107.7946 \times 0.0001 \approx 0.08387
    $$

    This means a one-basis-point yield increase causes a price decline of approximately \$0.084 per \$100 face value.

    **Price change for 25 bp increase.** With $\Delta y = 0.0025$:

    $$
    \frac{\Delta B}{B} \approx -D_{\mathrm{mod}} \times \Delta y = -7.779 \times 0.0025 = -0.01945
    $$

    The bond price decreases by approximately $1.945\%$, or about $\Delta B \approx -0.01945 \times 107.79 \approx -\$2.10$ per \$100 face value.

---

**Exercise 5.** Compute the convexity of the bond in Exercise 4. Using the second-order approximation $\Delta B / B \approx -D_{\text{mod}}\Delta y + \frac{1}{2}C(\Delta y)^2$, estimate the price change for a 100 basis point yield increase. Compare this to the duration-only estimate and explain the source of the difference.

??? success "Solution to Exercise 5"

    **Convexity computation.** Using the semi-annual compounding formula:

    $$
    C = \frac{1}{B} \sum_{k=1}^{20} \frac{(k/2)(k/2 + 1/2)}{(1.025)^2} \cdot \frac{c_k}{(1.025)^k}
    $$

    This simplifies to:

    $$
    C = \frac{1}{B \cdot (1.025)^2} \sum_{k=1}^{20} \frac{k(k+1)}{4} \cdot \frac{c_k}{(1.025)^k}
    $$

    Computing the sum term by term (with $c_k = 3$ for $k \leq 19$ and $c_{20} = 103$):

    $$
    \sum_{k=1}^{19} \frac{k(k+1)}{4} \cdot \frac{3}{(1.025)^k} + \frac{20 \cdot 21}{4} \cdot \frac{103}{(1.025)^{20}}
    $$

    The coupon terms contribute: $\frac{3}{4}\sum_{k=1}^{19} k(k+1) v^k$ where $v = (1.025)^{-1}$. Using standard power series identities, this evaluates to approximately $2{,}102.4$. The principal term is $\frac{420}{4} \times 61.027 = 105 \times 61.027 = 6{,}407.8$. The total sum is approximately $8{,}510.2$.

    $$
    C = \frac{8{,}510.2}{107.7946 \times 1.050625} \approx \frac{8{,}510.2}{113.252} \approx 75.14
    $$

    **Second-order price approximation for $\Delta y = 0.01$ (100 bp).**

    $$
    \frac{\Delta B}{B} \approx -D_{\mathrm{mod}} \cdot \Delta y + \frac{1}{2} C \cdot (\Delta y)^2 = -7.779 \times 0.01 + \frac{1}{2} \times 75.14 \times (0.01)^2
    $$

    $$
    = -0.07779 + 0.003757 = -0.074033
    $$

    **Duration-only estimate:**

    $$
    \frac{\Delta B}{B} \approx -D_{\mathrm{mod}} \cdot \Delta y = -0.07779
    $$

    **Comparison.** The duration-only estimate predicts a $7.779\%$ decline, while the second-order estimate predicts a $7.403\%$ decline. The difference of $0.376\%$ is the convexity correction $\frac{1}{2}C(\Delta y)^2$. This correction is always positive because the price-yield relationship is convex: the bond's price curve lies above its tangent line. For large yield moves, the linear (duration) approximation overestimates losses and underestimates gains. Convexity captures this curvature and provides a more accurate estimate.

---

**Exercise 6.** Two bonds have the same modified duration of 7 years but different convexities: Bond A has $C_A = 60$ and Bond B has $C_B = 90$. Both are priced at par. Which bond is more valuable and why? Compute the price difference for a parallel yield shift of $\pm 200$ basis points using the second-order approximation.

??? success "Solution to Exercise 6"

    **Which bond is more valuable?** Bond B (higher convexity) is more valuable. Both bonds have the same modified duration, so for infinitesimal yield changes they behave identically. However, for any finite yield shift, convexity matters: the bond with higher convexity gains more when yields fall and loses less when yields rise. This asymmetric advantage makes Bond B strictly preferable.

    **Price difference for $\Delta y = +0.02$ (200 bp increase).**

    $$
    \frac{\Delta B_A}{B_A} \approx -7 \times 0.02 + \frac{1}{2} \times 60 \times (0.02)^2 = -0.14 + 0.012 = -0.128
    $$

    $$
    \frac{\Delta B_B}{B_B} \approx -7 \times 0.02 + \frac{1}{2} \times 90 \times (0.02)^2 = -0.14 + 0.018 = -0.122
    $$

    Since both are at par ($B = 100$), the price difference is $100 \times (-0.122 + 0.128) = \$0.60$ in favor of Bond B.

    **Price difference for $\Delta y = -0.02$ (200 bp decrease).**

    $$
    \frac{\Delta B_A}{B_A} \approx -7 \times (-0.02) + \frac{1}{2} \times 60 \times (0.02)^2 = 0.14 + 0.012 = 0.152
    $$

    $$
    \frac{\Delta B_B}{B_B} \approx -7 \times (-0.02) + \frac{1}{2} \times 90 \times (0.02)^2 = 0.14 + 0.018 = 0.158
    $$

    The price difference is $100 \times (0.158 - 0.152) = \$0.60$ in favor of Bond B.

    In both cases, Bond B outperforms Bond A by $\$0.60$ per $\$100$ face value. The outperformance equals $\frac{1}{2}(C_B - C_A)(\Delta y)^2 \times B = \frac{1}{2}(90 - 60)(0.02)^2 \times 100 = 0.60$. This is symmetric in the sign of the yield shift: convexity benefits the holder regardless of the direction of the move. In equilibrium, Bond B trades at a slightly lower yield (the **convexity premium**) to compensate for this advantage.

---

**Exercise 7.** A US Treasury note is quoted at "101-16+" with a 3% coupon (semi-annual) and 5 years to maturity. The last coupon was paid 45 days ago in a 182-day coupon period. Convert the quote to a decimal clean price, compute the accrued interest, and determine the dirty price (invoice price) per \$100 face value.

??? success "Solution to Exercise 7"

    **Decimal clean price.** The quote "101-16+" means $101$ points plus $16.5$ thirty-seconds:

    $$
    B_{\mathrm{clean}} = 101 + \frac{16.5}{32} = 101 + 0.515625 = 101.515625
    $$

    **Accrued interest.** The semi-annual coupon is $Nc/2 = 100 \times 0.03/2 = 1.50$. With 45 days elapsed in a 182-day coupon period:

    $$
    AI = 1.50 \times \frac{45}{182} = 1.50 \times 0.24725 = 0.37088
    $$

    **Dirty price (invoice price).**

    $$
    B_{\mathrm{dirty}} = B_{\mathrm{clean}} + AI = 101.515625 + 0.37088 = 101.88650
    $$

    The buyer pays approximately $\$101.887$ per $\$100$ face value. The clean price is quoted in the market because it removes the sawtooth pattern of accrued interest, but the dirty price is the actual settlement amount.
