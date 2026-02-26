# Portfolio Management & CAPM

!!! info "Source"
    **Mathematics for Finance: An Introduction to Financial Engineering** by Marek Capinski and Tomasz Zastawniak, Springer, 2003.
    These notes are used for educational purposes.

## Portfolio Management

92
Mathematics for Finance
out to be a convenient measure of risk.
Exercise 5.1
Compute the risk Var(K1), Var(K2) and Var(K3) in each of the following
three investment projects, where the returns K1, K2 and K3 depend on
the market scenario:
Scenario
Probability
Return K1
Return K2
Return K3
ω1
0.25
12%
11%
2%
ω2
0.75
12%
13%
22%
Which of these is the most risky and the least risky project?
Exercise 5.2
Consider two scenarios, ω1 with probability 1
4 and ω2 with probability 3
4.
Suppose that the return on a certain security is K1(ω1) = −2% in the
first scenario and K1(ω2) = 8% in the second scenario. If the return on
another security is K2(ω1) = −4% in the first scenario, find the return
K2(ω2) in the other scenario such that the two securities have the same
risk.
In some circumstances the standard deviation σK =

Var(K) of the return
is a more convenient measure of risk. If a quantity is measured in certain units,
then the standard deviation will be expressed in the same units, so it can be
related directly to the original quantity, in contrast to variance, which will be
expressed in squared units.
Example 5.1
Let the return on an investment be K = 3% or −1%, both with probability
0.5. Then the risk is
Var(K) = 0.0004
or
σK = 0.02,
depending on whether we choose the variance or standard deviation. Now sup-
pose that the return on another investment is double that on the first invest-
ment, being equal to 2K = 6% or −2%, also with probability 0.5 each. Then
the risk of the second investment will be
Var(2K) = 0.0016
or
σ2K = 0.04.
The risk as measured by the variance is quadrupled, while the standard devi-
ation is simply doubled.

5. Portfolio Management
93
This illustrates the following general rule:
Var(aK) = a2Var(K),
σaK = |a| σK
for any real number a.
Remark 5.1
Another natural way to quantify risk would be to use the variance Var(k) (or
the standard deviation σk) of the logarithmic return k. The choice between K
and k is dictated to a large extent by the properties needed to handle the task
in hand. For example, if one is interested in a sequence of investments following
one another in time, then the variance of the logarithmic return may be more
useful as a measure of risk. This is because of the additivity of risks based on
logarithmic returns:
Var(k(0, n)) = Var(k(1)) + · · · + Var(k(n)),
where k(i) is the logarithmic return in time step i = 1, . . . , n and k(0, n) is the
logarithmic return over the whole time interval from 0 to n, provided that the
k(i) are independent. The above formula holds because k(0, n) = k(1) + · · · +
k(n) by Proposition 3.2, and the variance of a sum of independent random
variables is the sum of their variances. (This is not necessarily so without
independence.)
However, in the present chapter we shall be concerned with a portfolio of
several securities held simultaneously over a single time step. The properties
of E(K) and Var(K), where K is the ordinary return on the portfolio (see
formulae (5.4) and (5.5) below), are much more convenient for this purpose
than those for the logarithmic return.
Exercise 5.3
Consider two risky securities with returns K1 and K2 given by
Scenario
Probability
Return K1
Return K2
ω1
0.5
10.53%
7.23%
ω2
0.5
13.87%
10.57%
Compute the corresponding logarithmic returns k1 and k2 and compare
Var(k1) with Var(k2) and Var(K1) with Var(K2).

94
Mathematics for Finance
5.2 Two Securities
We begin a detailed discussion of the relationship between risk and expected
return in the simple situation of a portfolio with just two risky securities.
Example 5.2
Suppose that the prices of two stocks behave as follows:
Scenario
Probability
Return K1
Return K2
ω1
0.5
10%
−5%
ω2
0.5
−5%
10%
If we split our money equally between these two stocks, then we shall earn 5%
in each scenario (losing 5% on one stock, but gaining 10% on the other). Even
though an investment in either stock separately involves risk, we have reduced
the overall risk to nil by splitting the investment between the two stocks. This is
a simple example of diversification, which is particularly effective here because
the returns are negatively correlated.
In addition to the description of a portfolio in terms of the number of shares
of each security held (developed in Section 4.1), we shall introduce another very
convenient notation to describe the allocation of funds between the securities.
Example 5.3
Suppose that the prices of two kinds of stock are S1(0) = 30 and S2(0) = 40
dollars. We prepare a portfolio worth V (0) = 1, 000 dollars by purchasing
x1 = 20 shares of stock number 1 and x2 = 10 shares of stock number 2. The
allocation of funds between the two securities is
w1 = 30 × 20
1, 000 = 60%,
w2 = 10 × 40
1, 000 = 40%.
The numbers w1 and w2 are called the weights. If the stock prices change to
S1(1) = 35 and S2(1) = 39 dollars, then the portfolio will be worth V (1) =
20 × 35 + 10 × 39 = 1, 090 dollars. Observe that this amount is no longer split
between the two securities as 60% to 40%, but as follows:
20 × 35
1, 090
∼= 64.22%,
10 × 39
1, 090
∼= 35.78%,
even though the actual number of shares of each stock in the portfolio remains
unchanged.

5. Portfolio Management
95
The weights are defined by
w1 = x1S1(0)
V (0) ,
w2 = x2S2(0)
V (0) ,
where x1 and x2 are share numbers of stock 1 and 2 in the portfolio. This
means that wk is the percentage of the initial value of the portfolio invested in
security number k. Observe that the weights always add up to 100%,
w1 + w2 = x1S1(0) + x2S2(0)
V (0)
= V (0)
V (0) = 1.
(5.1)
If short selling is allowed, then one of the weights may be negative and the
other one greater than 100%.
Example 5.4
Suppose that a portfolio worth V (0) = 1, 000 dollars is constructed by taking
a long position in stock number 1 and a short position in stock number 2 in
Example 5.3 with weights w1 = 120% and w2 = −20%. The portfolio will
consist of
x1 = w1
V (0)
S1(0) = 120% × 1, 000
30
= 40,
x2 = w2
V (0)
S2(0) = −20% × 1, 000
40
= −5
shares of type 1 and 2. If the stock prices change as in Example 5.3, then this
portfolio will be worth
V (1) = x1S1(1) + x2S2(1) = V (0)
	
w1
S1(1)
S1(0) + w2
S2(1)
S2(0)

= 1, 000
	
120% × 35
30 −20% × 39
40

= 1, 205
dollars, benefiting from both the rise of the price of stock 1 and the fall of
stock 2. However, a small investor may have to face some restrictions on short
selling. For example, it may be necessary to pay a security deposit equal to
50% of the sum raised by shorting stock number 2. The deposit, which would
amount to 50% × 200 = 100 dollars, can be borrowed at the risk-free rate and
the interest paid on this loan will need to be subtracted from the final value
V (1) of the portfolio.

96
Mathematics for Finance
Exercise 5.4
Compute the value V (1) of a portfolio worth initially V (0) = 100
dollars that consists of two securities with weights w1 = 25% and
w2 = 75%, given that the security prices are S1(0) = 45 and S2(0) = 33
dollars initially, changing to S1(1) = 48 and S2(1) = 32 dollars.
We can see in Example 5.4 and Exercise 5.4 that V (1)/V (0) depends on
the prices of securities only through the ratios S1(1)/S1(0) = 1 + K1 and
S2(1)/S2(0) = 1 + K2. This indicates that the return on the portfolio should
depend only on the weights w1, w2 and the returns K1, K2 on each of the two
securities.
Proposition 5.1
The return KV on a portfolio consisting of two securities is the weighted average
KV = w1K1 + w2K2,
(5.2)
where w1 and w2 are the weights and K1 and K2 the returns on the two
components.
Proof
Suppose that the portfolio consists of x1 shares of security 1 and x2 shares of
security 2. Then the initial and final values of the portfolio are
V (0) = x1S1(0) + x2S2(0),
V (1) = x1S1(0)(1 + K1) + x2S2(0)(1 + K2)
= V (0) (w1(1 + K1) + w2(1 + K2)) .
As a result, the return on the portfolio is
KV = V (1) −V (0)
V (0)
= w1K1 + w2K2.
Exercise 5.5
Find the return on a portfolio consisting of two kinds of stock with
weights w1 = 30% and w2 = 70% if the returns on the components are

5. Portfolio Management
97
as follows:
Scenario
Return K1
Return K2
ω1
12%
−4%
ω2
10%
7%
Remark 5.2
A similar formula to (5.2) holds for logarithmic returns,
ekV = w1ek1 + w2ek2.
(5.3)
However, this is not particularly useful if the expectations and variances or
standard deviations of returns need to be related to the weights. On the other
hand, as will be seen below, formula (5.2) lends itself well to this task.
Exercise 5.6
Verify formula (5.3).
5.2.1 Risk and Expected Return on a Portfolio
The expected return on a portfolio consisting of two securities can easily be
expressed in terms of the weights and the expected returns on the components,
E(KV ) = w1E(K1) + w2E(K2).
(5.4)
This follows at once from (5.2) by the additivity of mathematical expectation.
Example 5.5
Consider three scenarios with the probabilities given below (a trinomial model).
Let the returns on two different stocks in these scenarios be as follows:
Scenario
Probability
Return K1
Return K2
ω1 (recession)
0.2
−10%
−30%
ω2 (stagnation)
0.5
0%
20%
ω3 (boom)
0.3
10%
50%
The expected returns on stock are
E(K1) = −0.2 × 10% + 0.5 × 0% + 0.3 × 10% = 1%,
E(K2) = −0.2 × 30% + 0.5 × 20% + 0.3 × 50% = 19%.

98
Mathematics for Finance
Suppose that w1 = 60% of available funds is invested in stock 1 and 40% in
stock 2. The expected return on such a portfolio is
E(KV ) = w1E(K1) + w2E(K2)
= 0.6 × 1% + 0.4 × 19% = 8.2%.
Exercise 5.7
Compute the weights in a portfolio consisting of two kinds of stock if
the expected return on the portfolio is to be E(KV ) = 20%, given the
following information on the returns on stock 1 and 2:
Scenario
Probability
Return K1
Return K2
ω1 (recession)
0.1
−10%
10%
ω2 (stagnation)
0.5
0%
20%
ω3 (boom)
0.4
20%
30%
To compute the variance of KV we need to know not only the variances
of the returns K1 and K2 on the components in the portfolio, but also the
covariance between the two returns.
Theorem 5.2
The variance of the return on a portfolio is given by
Var(KV ) = w2
1Var(K1) + w2
2Var(K2) + 2w1w2Cov(K1, K2).
(5.5)
Proof
Substituting KV = w1K1 + w2K2 and collecting the terms with w2
1, w2
2 and
w1w2, we compute
Var(KV ) = E(K2
V ) −E(KV )2
= w2
1[E(K2
1) −E(K1)2] + w2
2[E(K2
2) −E(K2)2]
+2w1w2[E(K1K2) −E(K1)E(K2)]
= w2
1Var(K1) + w2
2Var(K2) + 2w1w2Cov(K1, K2).

5. Portfolio Management
99
To avoid clutter, we introduce the following notation for the expectation
and variance of a portfolio and its components:
µV = E(KV ),
σV =

Var(KV ),
µ1 = E(K1),
σ1 =

Var(K1),
µ2 = E(K2),
σ2 =

Var(K2).
We shall also use the correlation coefficient
ρ12 = Cov(K1, K2)
σ1σ2
.
(5.6)
Formulae (5.4) and (5.5) can be written as
µV = w1µ1 + w2µ2,
(5.7)
σ2
V = w2
1σ2
1 + w2
2σ2
2 + 2w1w2ρ12σ1σ2.
(5.8)
Remark 5.3
For risky securities the returns K1 and K2 are always assumed to be non-
constant random variables. Because of this σ1, σ2 > 0 and ρ12 is well defined,
since the denominator σ1σ2 in (5.6) is non-zero.
Example 5.6
We use the following data:
Scenario
Probability
Return K1
Return K2
ω1 (recession)
0.4
−10%
20%
ω2 (stagnation)
0.2
0%
20%
ω3 (boom)
0.4
20%
10%
We want to compare the risk of a portfolio such that w1 = 40% and w2 =
60% with the risks of its components as measured by the variance. Direct
computations give
σ2
1 ∼= 0.0184,
σ2
2 ∼= 0.0024,
ρ12 ∼= −0.96309.
By (5.8)
σ2
V ∼= (0.4)2 × 0.0184 + (0.6)2 × 0.0024
+2 × 0.4 × 0.6 × (−0.96309) ×
√
0.0184 ×
√
0.0024
∼= 0.000736.
Observe that the variance σ2
V is smaller than σ2
1 and σ2
2.

100
Mathematics for Finance
Example 5.7
Consider another portfolio with weights w1 = 80% and w2 = 20%, all other
things being the same as in Example 5.6. Then
σ2
V ∼= (0.8)2 × 0.0184 + (0.2)2 × 0.0024
+2 × 0.8 × 0.2 × (−0.96309) ×
√
0.0184 ×
√
0.0024
∼= 0.009824,
which is between σ2
1 and σ2
2.
Proposition 5.3
The variance σ2
V of a portfolio cannot exceed the greater of the variances σ2
1
and σ2
2 of the components,
σ2
V ≤max{σ2
1, σ2
2},
if short sales are not allowed.
Proof
Let us assume that σ2
1 ≤σ2
2. If short sales are not allowed, then w1, w2 ≥0 and
w1σ1 + w2σ2 ≤(w1 + w2)σ2 = σ2.
Since the correlation coefficient satisfies −1 ≤ρ12 ≤1, it follows that
σ2
V = w2
1σ2
1 + w2
2σ2
2 + 2w1w2ρ12σ1σ2
≤w2
1σ2
1 + w2
2σ2
2 + 2w1w2σ1σ2
= (w1σ1 + w2σ2)2 ≤σ2
2.
If σ2
1 ≥σ2
2, the proof is analogous.
Example 5.8
Now consider a portfolio with weights w1 = −50% and w2 = 150% (allowing
short sales of security 1), all the other data being the same as in Example 5.6.
The variance of this portfolio is
σ2
V ∼= (−0.5)2 × 0.0184 + (1.5)2 × 0.0024
+2 × (−0.5) × 1.5 × (−0.96309) ×
√
0.0184 ×
√
0.0024
∼= 0.0196,
which is greater than both σ2
1 and σ2
2.

5. Portfolio Management
101
Exercise 5.8
Using the data in Example 5.6, find the weights in a portfolio with
expected return µV = 46% and compute the risk σ2
V of this portfolio.
The correlation coefficient always satisfies −1 ≤ρ12 ≤1. The next propo-
sition is concerned with the two special cases when ρ12 assumes one of the
extreme values 1 or −1, which means perfect positive or negative correlation
between the securities in the portfolio.
Proposition 5.4
If ρ12 = 1, then σV = 0 when σ1 ̸= σ2 and
w1 = −
σ2
σ1 −σ2
,
w2 =
σ1
σ1 −σ2
.
(5.9)
(Short sales are necessary, since either w1 or w2 is negative.)
If ρ12 = −1, then σV = 0 for
w1 =
σ2
σ1 + σ2
,
w2 =
σ1
σ1 + σ2
.
(5.10)
(No short sales are necessary, since both w1 and w2 are positive.)
Proof
Let ρ12 = 1. Then (5.8) takes the form
σ2
V = w2
1σ2
1 + w2
2σ2
2 + 2w1w2σ1σ2 = (w1σ1 + w2σ2)2
and σ2
V = 0 if and only if w1σ1 + w2σ2 = 0. This is equivalent to σ1 ̸= σ2 and
(5.9) because w1 + w2 = 1.
Now let ρ12 = −1. Then (5.8) becomes
σ2
V = w2
1σ2
1 + w2
2σ2
2 −2w1w2σ1σ2 = (w1σ1 −w2σ2)2
and σ2
V = 0 if and only if w1σ1 −w2σ2 = 0. The last equality is equivalent to
(5.10) because w1 + w2 = 1.
Each portfolio can be represented by a point with coordinates σV and µV
on the σ, µ plane. Figure 5.1 shows two typical lines representing portfolios
with ρ12 = −1 (left) and ρ12 = 1 (right). The bold segments correspond to
portfolios without short selling.

102
Mathematics for Finance
Figure 5.1
Typical portfolio lines with ρ12 = −1 and 1
Suppose that ρ12 = −1. It follows from the proof of Proposition 5.4 that
σV = |w1σ1 −w2σ2|. In addition, µV = w1µ1 + w2µ2 by (5.7) and w1 + w2 = 1
by (5.1). We can choose s = w2 as a parameter. Then 1 −s = w1 and
σV = |(1 −s)σ1 −sσ2| ,
µV = (1 −s)µ1 + sµ2.
These parametric equations describe the line in Figure 5.1 with a broken seg-
ment between (σ1, µ1) and (σ2, µ2). As s increases, the point (σV , µV ) moves
along the line in the direction from (σ1, µ1) to (σ2, µ2).
If ρ12 = 1, then σV = |w1σ1 + w2σ2|. We choose s = w2 as a parameter
once again, and obtain the parametric equations
σV = |(1 −s)σ1 + sσ2| ,
µV = (1 −s)µ1 + sµ2
of the line in Figure 5.1 with a straight segment between (σ1, µ1) and (σ2, µ2).
If no short selling is allowed, then 0 ≤s ≤1 in both cases, which corresponds
to the bold line segments.
Exercise 5.9
Suppose that there are just two scenarios ω1 and ω2 and consider two
risky securities with returns K1 and K2. Show that K1 = aK2 + b for
some numbers a ̸= 0 and b, and deduce that ρ12 = 1 or −1.
Our next task is to find a portfolio with minimum risk for any given ρ12
such that −1 < ρ12 < 1. Again, we take s = w2 as a parameter. Then (5.7)

5. Portfolio Management
103
and (5.8) take the form
µV = (1 −s)µ1 + sµ2,
(5.11)
σ2
V = (1 −s)2σ2
1 + s2σ2
2 + 2s(1 −s)ρ12σ1σ2.
(5.12)
Obviously, µV as a function of s is a straight line and σ2
V is a quadratic function
of s with a positive coefficient at s2 (namely σ2
1 + σ2
2 −2ρ12σ1σ2 > σ2
1 + σ2
2 −
2σ1σ2 = (σ1 −σ2)2 ≥0). The problem of minimising the variance σ2
V (or,
equivalently, the standard deviation σV ) of a portfolio is solved in the next
theorem. First we find the minimum without any restrictions on short sales.
If short sales are not allowed, we shall have to take into account the bounds
0 ≤s ≤1 on the parameter.
Theorem 5.5
For −1 < ρ12 < 1 the portfolio with minimum variance is attained at
s0 =
σ2
1 −ρ12σ1σ2
σ2
1 + σ2
2 −2ρ12σ1σ2
.
(5.13)
If short sales are not allowed, then the smallest variance is attained at
smin =



0
if s0 < 0,
s0
if 0 ≤s0 ≤1,
1
if 1 < s0.
Proof
We compute the derivative of σ2
V with respect to s and equate it to 0:
−2 (1 −s) σ2
1 + 2sσ2
2 + 2(1 −s)ρ12σ1σ2 −2sρ12σ1σ2 = 0.
Solving for s gives the above s0. The second derivative is positive,
2σ2
1 + 2σ2
2 −4ρ12σ1σ2 > 2σ2
1 + 2σ2
2 −4σ1σ2 = 2 (σ1 −σ2)2 ≥0,
which shows that there is a minimum at s0. It is a global minimum because
σ2
V is a quadratic function of s.
If short sales are not allowed, then we need to find the minimum for 0 ≤
s ≤1. If 0 ≤s0 ≤1, then the minimum is at s0. If s0 < 0, then the minimum
is at 0, and if s0 > 1, then it is at 1, since σ2
V is a quadratic function of s with
a positive coefficient at s2. This is illustrated in Figure 5.2. The bold parts of
the curve correspond to portfolios with no short selling.

104
Mathematics for Finance
Figure 5.2
The minimum of σ2
V as a function of s
The line on the σ, µ plane defined by the parametric equations (5.11) and
(5.12) represents all possible portfolios with given σ1, σ2 > 0 and −1 ≤ρ12 ≤1.
The parameter s can be any real number whenever there are no restrictions on
short selling. If short selling is not allowed, then 0 ≤s ≤1 and we only obtain a
segment of the line. As s increases from 0 to 1, the corresponding point (σV , µV )
travels along the line in the direction from (σ1, µ1) to (σ2, µ2). Figure 5.3 shows
two typical examples of such lines, with ρ12 close to but greater than −1 (left)
and with ρ12 close to but smaller than 1 (right). Portfolios without short selling
are indicated by the bold line segments.
Figure 5.3
Typical portfolio lines with −1 < ρ12 < 1
Figure 5.4 illustrates the following corollary.
Corollary 5.6
Suppose that σ1 ≤σ2. The following three cases are possible:
1) If −1 ≤ρ12 < σ1
σ2 , then there is a portfolio without short selling such that
σV < σ1 (lines 4 and 5 in Figure 5.4);
2) If ρ12 = σ1
σ2 , then σV ≥σ1 for each portfolio (line 3 in Figure 5.4);

5. Portfolio Management
105
3) If
σ1
σ2 < ρ12 ≤1, then there is a portfolio with short selling such that
σV < σ1, but for each portfolio without short selling σV ≥σ1 (lines 1 and 2
in Figure 5.4).
Figure 5.4
Portfolio lines for various values of ρ12
Proof
1) If −1 ≤ρ12 < σ1
σ2 , then
σ1
σ1+σ2 > s0 > 0. But
σ1
σ1+σ2 < 1, so 0 < s0 < 1,
which means that the portfolio with minimum variance, which corresponds to
the parameter s0, involves no short selling and satisfies σV < σ1.
2) If ρ12 = σ1
σ2 , then s0 = 0. As a result, σV ≥σ1 for every portfolio because
σ2
1 is the minimum variance.
3) Finally, if σ1
σ2 < ρ12 ≤1, then s0 < 0. In this case the portfolio with
minimum variance that corresponds to s0 involves short selling of security 1
and satisfies σV < σ1. For s ≥s0 the variance σV is an increasing function of s,
which means that σV > σ1 for every portfolio without short selling.
The above corollary is important because it shows when it is possible to
construct a portfolio with risk lower than that of any of its components. In
case 1) this is possible without short selling. In case 3) this is also possible, but
only if short selling is allowed. In case 2) it is impossible to construct such a
portfolio.
Example 5.9
Suppose that
σ2
1 = 0.0041,
σ2
2 = 0.0121,
ρ12 = 0.9796.
Clearly, σ1 < σ2 and σ1
σ2 < ρ12 < 1, so this is case 3) in Corollary 5.6. Our task
will be to find the portfolio with minimum risk with and without short selling.

106
Mathematics for Finance
Using Theorem 5.5, we compute
s0 ∼= −1.1663,
smin = 0.
It follows that in the portfolio with minimum risk the weights of securities
should be w1 ∼= 2.1663 and w2 ∼= −1.1663 if short selling is allowed. Without
short selling w1 = 1 and w2 = 0.
Exercise 5.10
Compute the weights in the portfolio with minimum risk for the data in
Example 5.6. Does this portfolio involve short selling?
We conclude this section with a brief discussion of portfolios in which one of
the securities is risk-free. The variance of the risky security (a stock) is positive,
whereas that of the risk-free component (a bond) is zero.
Proposition 5.7
The standard deviation σV of a portfolio consisting of a risky security with
expected return µ1 and standard deviation σ1 > 0, and a risk-free security
with return rF and standard deviation zero depends on the weight w1 of the
risky security as follows:
σV = |w1| σ1.
Proof
Let σ1 > 0 and σ2 = 0. Then (5.7) reduces to σ2
V = w2
1σ2
1, and the formula for
σV follows by taking the square root.
Figure 5.5
Portfolio line for one risky and one risk-free security

5. Portfolio Management
107
The line on the σ, µ plane representing portfolios constructed from one risky
and one risk-free security is shown in Figure 5.5. As usual, the bold line segment
corresponds to portfolios without short selling.
5.3 Several Securities
5.3.1 Risk and Expected Return on a Portfolio
A portfolio constructed from n different securities can be described in terms of
their weights
wi = xiSi(0)
V (0) ,
i = 1, . . . , n,
where xi is the number of shares of type i in the portfolio, Si(0) is the initial
price of security i, and V (0) is the amount initially invested in the portfolio. It
will prove convenient to arrange the weights into a one-row matrix
w =

w1
w2
· · ·
wn

.
Just like for two securities, the weights add up to one, which can be written in
matrix form as
1 = uwT ,
(5.14)
where
u =

1
1
· · ·
1

is a one-row matrix with all n entries equal to 1, wT is a one-column matrix,
the transpose of w, and the usual matrix multiplication rules apply. The at-
tainable set consists of all portfolios with weights w satisfying (5.14), called
the attainable portfolios.
Suppose that the returns on the securities are K1, . . . , Kn. The expected
returns µi = E(Ki) for i = 1, . . . , n will also be arranged into a one-row matrix
m =

µ1
µ2
· · ·
µn

.
The covariances between returns will be denoted by cij = Cov(Ki, Kj). They
are the entries of the n × n covariance matrix
C =


c11
c12
· · ·
c1n
c21
c22
· · ·
c2n
...
...
...
...
cn1
cn2
· · ·
cnn

.

108
Mathematics for Finance
It is well known that the covariance matrix is symmetric and positive definite.
The diagonal elements are simply the variances of returns, cii = Var(Ki). In
what follows we shall assume, in addition, that C has an inverse C−1.
Proposition 5.8
The expected return µV = E(KV ) and variance σ2
V = Var(KV ) of a portfolio
with weights w are given by
µV = mwT ,
(5.15)
σ2
V = wCwT .
(5.16)
Proof
The formula for µV follows by the linearity of expectation,
µV = E(KV ) = E
 n

i=1
wiKi

=
n

i=1
wiµi = mwT .
For σ2
V we use the linearity of covariance with respect to each of its arguments,
σ2
V = Var(KV ) = Var
 n

i=1
wiKi

= Cov


n

i=1
wiKi,
n

j=1
wjKj

=
n

i,j=1
wiwjcij
= wCwT .
Exercise 5.11
Compute the expected return µV and standard deviation σV of a port-
folio consisting of three securities with weights w1 = 40%, w2 = −20%,
w3 = 80%, given that the securities have expected returns µ1 = 8%,
µ2 = 10%, µ3 = 6%, standard deviations σ1 = 1.5, σ2 = 0.5, σ3 = 1.2
and correlations ρ12 = 0.3, ρ23 = 0.0, ρ31 = −0.2.
We shall solve the following two problems:
1. To find a portfolio with the smallest variance in the attainable set. It will
be called the minimum variance portfolio.

5. Portfolio Management
109
2. To find a portfolio with the smallest variance among all portfolios in the
attainable set whose expected return is equal to a given number µV . The
family of such portfolios, parametrised by µV , is called the minimum vari-
ance line.
Since the variance is a continuous function of the weights, bounded below by 0,
the minimum clearly exists in both cases.
Proposition 5.9 (Minimum Variance Portfolio)
The portfolio with the smallest variance in the attainable set has weights
w =
uC−1
uC−1uT ,
provided that the denominator is non-zero.
Proof
We need to find the minimum of (5.16) subject to the constraint (5.14). To this
end we can use the method of Lagrange multipliers. Let us put
F(w, λ) = wCwT −λuwT ,
where λ is a Lagrange multiplier. Equating to zero the partial derivatives of F
with respect to the weights wi we obtain 2wC −λu = 0, that is,
w = λ
2 uC−1,
which is a necessary condition for a minimum. Substituting this into con-
straint (5.14) we obtain
1 = λ
2 uC−1uT ,
where we use the fact that C−1 is a symmetric matrix because C is. Solving
this for λ and substituting the result into the expression for w will give the
asserted formula.
Proposition 5.10 (Minimum Variance Line)
The portfolio with the smallest variance among attainable portfolios with ex-
pected return µV has weights
w =
!!!!
1
uC−1mT
µV
mC−1mT
!!!! uC−1 +
!!!!
uC−1uT
1
mC−1uT
µV
!!!! mC−1
!!!!
uC−1uT
uC−1mT
mC−1uT
mC−1mT
!!!!
,

110
Mathematics for Finance
provided that the determinant in the denominator is non-zero. The weights
depend linearly on µV .
Proof
Here we need to find the minimum of (5.16) subject to two constraints (5.14)
and (5.15). We take
G(w, λ, µ) = wCwT −λuwT −µmwT ,
where λ and µ are Lagrange multipliers. The partial derivatives of G with
respect to the weights wi equated to zero give a necessary condition for a
minimum, 2wC −λu −µm = 0, which implies that
w = λ
2 uC−1 + µ
2 mC−1.
Substituting this into the constraints (5.14) and (5.15), we obtain a system of
linear equations
1 = λ
2 uC−1uT + µ
2 uC−1mT ,
µV = λ
2 mC−1uT + µ
2 mC−1mT ,
to be solved for λ and µ. The asserted formula follows by substituting the
solution into the expression for w.
Example 5.10
(3 securities) Consider three securities with expected returns, standard devia-
tions of returns and correlations between returns
µ1 = 0.10,
σ1 = 0.28,
ρ12 = ρ21 = −0.10,
µ2 = 0.15,
σ2 = 0.24,
ρ23 = ρ32 =
0.20,
µ3 = 0.20,
σ3 = 0.25,
ρ31 = ρ13 =
0.25.
We arrange the µi’s into a one-row matrix m and 1’s into a one-row matrix u,
m =

0.10
0.15
0.20

,
u =

1
1
1

.
Next we compute the entries cij = ρijσiσj of the covariance matrix C, and
find the inverse matrix to C,
C ∼=


0.0784
−0.0067
0.0175
−0.0067
0.0576
0.0120
0.0175
0.0120
0.0625

, C−1 ∼=


13.954
2.544
−4.396
2.544
18.548
−4.274
−4.396
−4.274
18.051



5. Portfolio Management
111
From Proposition 5.9 we can compute the weights in the minimum variance
portfolio. Since
uC−1 ∼=

12.102
16.818
9.382

,
uC−1uT ∼= 38.302,
we obtain
w =
uC−1
uC−1uT ∼=

0.316
0.439
0.245

.
The expected return and standard deviation of this portfolio are
µV = mwT ∼= 0.146,
σV =
√
wCwT ∼= 0.162.
The minimum variance line can be computed using Proposition 5.10. To this
end we compute
uC−1 ∼=

12.102
16.818
9.382

,
mC−1 ∼=

0.898
2.182
2.530

,
uC−1uT ∼= 38.302,
mC−1mT ∼= 0.923,
uC−1mT = mC−1uT ∼= 5.609.
Substituting these into the formula for w in Proposition 5.10, we obtain the
weights in the portfolio with minimum variance among all portfolios with ex-
pected return µV :
w ∼=

1.578 −8.614µV
0.845 −2.769µV
−1.422 + 11.384µV

.
The standard deviation of this portfolio is
σV =
√
wCwT ∼=

0.237 −2.885µV + 9.850µ2
V .
Exercise 5.12
Among all attainable portfolios constructed using three securities with
expected returns µ1 = 0.20, µ2 = 0.13, µ3 = 0.17, standard deviations of
returns σ1 = 0.25, σ2 = 0.28, σ3 = 0.20, and correlations between returns
ρ12 = 0.30, ρ23 = 0.00, ρ31 = 0.15, find the minimum variance portfolio.
What are the weights in this portfolio? Also compute the expected return
and standard deviation of this portfolio.
Exercise 5.13
Among all attainable portfolios with expected return µV = 20% con-
structed using the three securities in Exercise 5.12 find the portfolio with
the smallest variance. Compute the weights and the standard deviation
of this portfolio.

112
Mathematics for Finance
Example 5.11
(3 securities visualised) There are two convenient ways to visualise all portfolios
that can be constructed from the three securities in Example 5.10. One is
presented in Figure 5.6. Here two of the three weights, namely w2 and w3,
Figure 5.6
Attainable portfolios on the w2, w3 plane
are used as parameters. The remaining weight is given by w1 = 1 −w2 −
w3. (Of course any other two weights can also be used as parameters.) Each
point on the w2, w3 plane represents a different portfolio. The vertices of the
triangle represent the portfolios consisting of only one of the three securities. For
example, the vertex with coordinates (1, 0) corresponds to weights w1 = 0, w2 =
1 and w3 = 0, that is, represents a portfolio with all money invested in security
number 2. The lines through the vertices correspond to portfolios consisting of
two securities only. For example, the line through (1, 0) and (0, 1) corresponds to
portfolios containing securities 2 and 3 only. Points inside the triangle, including
the boundaries, correspond to portfolios without short selling. For example,
( 2
5, 1
2) represents a portfolio with 10% of the initial funds invested in security 1,
40% in security 2, and 50% in security 3. Points outside the triangle correspond
to portfolios with one or two of the three securities shorted. The minimum
variance line is a straight line because of the linear dependence of the weights
on the expected return. It is represented by the bold line in Figure 5.6.
Figure 5.7 shows another way to visualise attainable portfolios by plot-
ting the expected return of a portfolio against the standard deviation. This is
sometimes called the risk–expected return graph. The three points indicated
in this picture correspond to portfolios consisting of only one of the three
securities. For instance, the portfolio with all funds invested in security 2 is
represented by the point (0.24, 0.15). The lines passing through a pair of these
three points correspond to portfolios consisting of just two securities. These are
the two-security lines studied in detail in Section 5.2. For example, all portfo-

5. Portfolio Management
113
lios containing securities 2 and 3 only lie on the line through (0.24, 0.15) and
(0.25, 0.20). The three points and the lines passing through them correspond
to the vertices of the triangle and the straight lines passing through them in
Figure 5.6. The shaded area (both dark and light), including the boundary,
represents portfolios that can be constructed from the three securities, that is,
all attainable portfolios. The boundary, shown as a bold line, is the minimum
variance line. The shape of it is known as the Markowitz bullet. The darker
part of the shaded area corresponds to the interior of the triangle in Figure 5.6,
that is, it represents portfolios without short selling.
Figure 5.7
Attainable portfolios on the σ, µ plane
It is instructive to imagine how the whole w2, w3 plane in Figure 5.6 is
mapped onto the shaded area representing all attainable portfolios in Fig-
ure 5.7. Namely, the w2, w3 plane is folded along the minimum variance line, be-
ing simultaneously warped and stretched to attain the shape of the Markowitz
bullet. This means, in particular, that pairs of points on opposite sides of the
minimum variance line on the w2, w3 plane are mapped into single points on
the σ, µ plane. In other words, each point inside the shaded area in Figure 5.7
corresponds to two different portfolios. However, each point on the minimum
variance line corresponds to a single portfolio.
Example 5.12
(3 securities without short selling) For the same three securities as in Exam-
ples 5.10 and 5.11, Figure 5.8 shows what happens if no short selling is allowed.
All portfolios without short selling are represented by the interior and bound-
ary of the triangle on the w1, w2 plane and by the shaded area with boundary
on the σ, µ plane. The minimum variance line without short selling is shown
as a bold line in both plots. For comparison, the minimum variance line with
short selling is shown as a broken line.

114
Mathematics for Finance
Figure 5.8
Portfolios without short selling
Exercise 5.14
For portfolios constructed with and without short selling from the three
securities in Exercise 5.12 compute the minimum variance line parame-
trised by the expected return and sketch it a) on the w2, w3 plane and
b) on the σ, µ plane. Also sketch the set of all attainable portfolios with
and without short selling.
5.3.2 Efficient Frontier
Given the choice between two securities a rational investor will, if possible,
choose that with higher expected return and lower standard deviation, that is,
lower risk. This motivates the following definition.
Definition 5.1
We say that a security with expected return µ1 and standard deviation σ1
dominates another security with expected return µ2 and standard deviation σ2
whenever
µ1 ≥µ2
and
σ1 ≤σ2.
This definition readily extends to portfolios, which can of course be considered
as securities in their own right.
Remark 5.4
Given two securities such that one dominates the other, the dominated security
may appear quite redundant on first sight. Nevertheless, it can also be of some

5. Portfolio Management
115
use. Employing the techniques of Section 5.2, it may be possible to construct
portfolios consisting of the two securities with smaller risk than either of the
securities, as in Figure 5.9, in which the security with σ2, µ2 is dominated by
that with σ1, µ1.
Figure 5.9
Reduction of risk using a dominated security
Definition 5.2
A portfolio is called efficient if there is no other portfolio, except itself, that
dominates it. The set of efficient portfolios among all attainable portfolios is
called the efficient frontier.
Every rational investor will choose an efficient portfolio, always preferring
a dominating portfolio to a dominated one. However, different investors may
select different portfolios on the efficient frontier, depending on their individual
preferences. Given two efficient portfolios with µ1 ≤µ2 and σ1 ≤σ2, a cautious
person may prefer that with lower risk σ1 and lower expected return µ1, while
others may choose a portfolio with higher risk σ2, regarding the higher expected
return µ2 as compensation for increased risk.
In particular, an efficient portfolio has the highest expected return among
all attainable portfolios with the same standard deviation (the same risk),
and has the lowest standard deviation (the lowest risk) among all attainable
portfolios with the same expected return. As a result, the efficient frontier must
be a subset of the minimum variance line. To understand the structure of the
efficient frontier we shall first study the minimum variance line in more detail
and then select a suitable subset.
Proposition 5.11
Take any two different portfolios on the minimum variance line, with weights
w′ and w′′. Then the minimum variance line consists of portfolios with weights

116
Mathematics for Finance
cw′ + (1 −c)w′′ for any c ∈R and only of such portfolios.
Proof
By Proposition 5.10 the minimum variance line consists of portfolios whose
weights are given by a certain linear function of the expected return µV on the
portfolio, w = aµV +b. If w′ and w′′ are the weights of two different portfolios
on the minimum variance line, then w′ = aµV ′ +b and w′′ = aµV ′′ +b for some
µV ′ ̸= µV ′′. Because numbers of the form cµV ′ + (1 −c)µV ′′ for c ∈R exhaust
the whole real line, it follows that portfolios with weights cw′ + (1 −c)w′′ for
c ∈R exhaust the whole minimum variance line.
This proposition is important. It means that the minimum variance line has
the same shape as the set of portfolios constructed from two securities, studied
in great detail in Section 5.2. It also means that the shape of the attainable
set on the σ, µ plane (the Markowitz bullet), which we have seen so far for
portfolios constructed from two or three securities, will in fact be the same for
any number of securities.
Once the shape of the minimum variance line is understood, distinguishing
the efficient frontier is easy, also in the case of n securities. This is illustrated
in Figure 5.10. The efficient frontier consists of all portfolios on the minimum
variance line whose expected return is greater than or equal to the expected
return on the minimum variance portfolio.
Figure 5.10
Efficient frontier constructed from several securities
The next proposition provides a property of the efficient frontier which will
prove useful in the Capital Asset Pricing Model.
Proposition 5.12
The weights w of any portfolio belonging to the efficient frontier (except for

5. Portfolio Management
117
the minimum variance portfolio) satisfy the condition
γwC = m −µu
(5.17)
for some real numbers γ > 0 and µ.
Proof
Let w be the weights of a portfolio, other than the minimum variance portfolio,
belonging to the efficient frontier. The portfolio has expected return µV =
mwT and standard deviation σV =
√
wCwT . On the σ, µ plane we draw the
tangent line to the efficient frontier through the point representing the portfolio.
This line will intersect the vertical axis at some point with coordinate µ, the
gradient of the line being mwT −µ
√
wCwT . This gradient is maximal among all lines
passing through the point on the vertical axis with coordinate µ and intersecting
the set of attainable portfolios. The maximum is to be taken over all weights w
subject to the constraint uwT = 1. We put
F(w, λ) = mwT −µ
√
wCwT −λuwT ,
where λ is a Lagrange multiplier. A necessary condition for a constrained max-
imum is that the partial derivatives of F with respect to the weights should be
zero. This gives
m −λσV u = µV −µ
σ2
V
wC.
Multiplying by wT on the right and using the constraint, we find that λ =
µ
σV .
For γ = µV −µ
σ2
V
this gives the asserted condition. Because the tangent line has
positive slope, we have µV > µ, that is, γ > 0.
Remark 5.5
An interpretation of γ and µ follows clearly from the proof: γσV is the gradient
of the tangent line to the efficient frontier at the point representing the given
portfolio, µ being the intercept of this tangent line on the σ, µ plane.
Exercise 5.15
In a market consisting of the three securities in Exercise 5.12, consider
the portfolio on the efficient frontier with expected return µV = 21%.
Compute the values of γ and µ such that the weights w in this portfolio
satisfy γwC = m −µu.

118
Mathematics for Finance
5.4 Capital Asset Pricing Model
In the days when computers where slow it was difficult to use portfolio theory.
For a market with n = 1, 000 traded securities the covariance matrix C will have
n2 = 1, 000, 000 entries. To find the efficient frontier we have to compute the
inverse matrix C−1, which is computationally intensive. Accurate estimation
of C may pose considerable problems in practice. The Capital Asset Pricing
Model (CAPM) provides a solution that is much more efficient computation-
ally, does not involve an estimate of C, but offers a deep, even if somewhat
oversimplified, insight into some fundamental economic issues.
Within the CAPM it is assumed that every investor uses the same values of
expected returns, standard deviation and correlations for all securities, making
investment decisions based only on these values. In particular, every investor
will compute the same efficient frontier on which to select his or her portfo-
lio. However, investors may differ in their attitude to risk, selecting different
portfolios on the efficient frontier.
5.4.1 Capital Market Line
Form now on we shall assume that a risk-free security is available in addition
to n risky securities. The return on the risk-free security will be denoted by rF .
The standard deviation is of course zero for the risk-free security.
Consider a portfolio consisting of the risk-free security and a specified risky
security (possibly a portfolio of risky securities) with expected return µ1 and
standard deviation σ1 > 0. By Proposition 5.7 all such portfolios form a broken
line on the σ, µ plane consisting of two rectilinear half-lines, see Figure 5.5. By
taking portfolios containing the risk-free security and a security with σ1, µ1
anywhere in the attainable set represented by the Markowitz bullet on the
σ, µ plane, we can construct any portfolio between the two half-lines shown
in Figure 5.11. The efficient frontier of this new set of portfolios, which may
contain the risk-free security, is the upper half-line tangent to the Markowitz
bullet and passing through the point with coordinates 0, rF . According to the
assumptions of the CAPM, every rational investor will select his or her portfolio
on this half-line, called the capital market line. This argument works as long
as the risk-free return rF is not too high, so the upper half-line is tangent to
the bullet. (If rF is too high, then the upper half-line will no longer be tangent
to the bullet.)
The tangency point with coordinates σM, µM plays a special role. Every
portfolio on the capital market line can be constructed from the risk-free se-
curity and the portfolio with standard deviation σM and expected return µM.

5. Portfolio Management
119
Figure 5.11
Efficient frontier for portfolios with a risk-free security
Since every investor will select a portfolio on the capital market line, everyone
will be holding a portfolio with the same relative proportions of risky securities.
But this means that the portfolio with standard deviation σM and expected
return µM has to contain all risky securities with weights equal to their rela-
tive share in the whole market. Because of this property it is called the market
portfolio. In practice the market portfolio is approximated by a suitable stock
exchange index.
The capital market line joining the risk-free security and the market port-
folio satisfies the equation
µ = rF + µM −rF
σM
σ.
(5.18)
For a portfolio on the capital market line with risk σ the term µM −rF
σM
σ is called
the risk premium. This additional return above the risk-free level provides
compensation for exposure to risk.
Example 5.13
We shall apply Proposition 5.12 to compute the market portfolio for a toy
market consisting of the three securities in Example 5.10 and a risk-free security
with return rF = 5%. The weights w in the market portfolio, which belongs to
the efficient frontier, satisfy condition (5.17), which implies that
γw = (m −µu)C−1.
From the proof of Proposition 5.12 we know that µ = rF because the capital
market line, tangent to the efficient frontier at the point representing the market
portfolio, intersects the µ axis at rF . Substituting the numerical values from
Example 5.10, we find that
γw ∼=

0.293
1.341
2.061

.

120
Mathematics for Finance
Since w must satisfy (5.14), it follows that γ ∼= 3.694 and the weights in the
market portfolio are
w ∼=

0.079
0.363
0.558

.
Exercise 5.16
Suppose that the risk-free return is rF = 5%. Compute the weights in the
market portfolio constructed from the three securities in Exercise 5.11.
Also compute the expected return and standard deviation of the market
portfolio.
5.4.2 Beta Factor
It is important to understand how the return KV on a given portfolio or a
single security will react to trends affecting the whole market. To this end we
can plot the values of KV for each market scenario against those of the return
KM on the market portfolio and compute the line of best fit, also known as the
regression line or the characteristic line. In Figure 5.12 the values of KM are
marked along the x axis and the values of KV along the y axis. The equation
of the line of best fit will be
y = βV x + αV .
Figure 5.12
Line of best fit
For any given β and α the values of the random variable α + βKM can be
regarded as predictions for the return on the given portfolio. The difference
ε = KV −(α + βKM) between the actual return KV and the predicted return

5. Portfolio Management
121
α + βKM is called the residual random variable. The condition defining the
line of best fit is that
E(ε2) = E(K2
V ) −2βE(KV KM) + β2E(K2
M) + α2 −2αE(KV ) + 2αβE(KM)
as a function of β and α should attain its minimum at β = βV and α = αV .
In other words, the line of best fit should lead to predictions that are as close
as possible to the true values of KV . A necessary condition for a minimum is
that the partial derivatives with respect to β and α should be zero at β = βV
and α = αV . This leads to the system of linear equations
αV E(KM) + βV E(K2
M) = E(KV KM),
αV + βV E(KM) = E(KV ),
which can be solved to find the gradient βV and intercept αV of the line of best
fit,
βV = Cov(KV , KM)
σ2
M
,
αV = µV −βV µM.
Here we employ the usual notation µV = E(KV ), µM = E(KM) and σ2
M =
Var(KM).
Exercise 5.17
Suppose that the returns KV on a given portfolio and KM on the market
portfolio take the following values in different market scenarios:
Scenario
Probability
Return KV
Return KM
ω1
0.1
−5%
10%
ω2
0.3
0%
14%
ω3
0.4
2%
12%
ω3
0.2
4%
16%
Compute the gradient βV and intercept αV of the line of best fit.
Definition 5.3
We call
βV = Cov(KV , KM)
σ2
M
the beta factor of the given portfolio or individual security.

122
Mathematics for Finance
The beta factor is an indicator of expected changes in the return on a
particular portfolio or individual security in response to the behaviour of the
market as a whole. Since µV = βV µM + αV , the return on a security with
a positive beta factor tends to increase as the return on the market portfolio
increases, while the return on a security with a negative beta factor tends to
increase if the return on the market portfolio goes down.
In what follows we discuss another interpretation of the beta factor. The
risk σ2
V = Var(KV ) of a security or portfolio can be written as
σ2
V = Var(εV ) + β2
V σ2
M.
This formula is easy to verify upon substituting the expression εV = KV −
(αV +βV KM) for the residual random variable. The first term Var(εV ) is called
the residual variance or diversifiable risk. It vanishes for the market portfolio,
Var(εM) = 0. This part of risk can ‘diversified away’ by investing in the market
portfolio. The second term β2
V σ2
M is called the systematic or undiversifiable
risk. The market portfolio involves only this kind of risk. The beta factor βV
can be regarded as a measure of systematic risk associated with a security or
portfolio.
This interpretation of the beta factor is of crucial importance. In the CAPM
systematic risk, measured by βV , will be linked to the expected return µV
and hence to the pricing of individual securities and portfolios: The higher
the systematic risk, the higher the return required by investors as a premium
for exposure to this kind of risk. However, diversifiable risk will attract no
additional premium, having no effect on µV . This is because diversifiable risk
can be eliminated by spreading an investment in a portfolio of many securities
and, in particular, by investing in the market portfolio. The next section is
devoted to establishing the link between βV and µV .
Exercise 5.18
Show that the beta factor βV of a portfolio consisting of n securities with
weights w1, . . . , wn is given by βV = w1β1 +· · ·+wnβn, where β1, . . . , βn
are the beta factors of the securities.
5.4.3 Security Market Line
Consider an arbitrary portfolio with weights wV . The weights in the market
portfolio will be denoted by wM. The market portfolio belongs to the efficient
frontier of the attainable set of portfolios consisting of risky securities. Thus,
by Proposition 5.12
γwMC = m −µu

5. Portfolio Management
123
for some numbers γ > 0 and µ. The beta factor of the portfolio with weights
wV can, therefore, be written as
βV = Cov(KV , KM)
σ2
M
= wMCwT
V
wMCwT
M
= γ(m −µu)wT
V
γ(m −µu)wT
M
= µV −µ
µM −µ.
To find µ consider the risk-free security, with return rF and beta factor βF = 0.
Substituting βF and rF for βV and µV in the above equation, we find that
µ = rF . We have proved the following remarkable property.
Theorem 5.13
The expected return µV on a portfolio (or an individual security) is a linear
function of the beta coefficient βV of the portfolio,
µV = rF + (µM −rF )βV .
(5.19)
The expected return plotted against the beta coefficient of any portfolio or
individual security will form a straight line on the β, µ plane, called the security
market line. This is shown in Figure 5.13, in which the security market line is
plotted next to the capital market line for comparison. A number of different
portfolios and individual securities are indicated by dots in both graphs.
Figure 5.13
Capital market line and security market line
Similarly as in formula (5.18) for the capital market line, the term (µM −
rF )βV in (5.19) is the risk premium, interpreted as compensation for exposure
to systematic risk. However, (5.18) applies only to portfolios on the capital
market line, whereas (5.19) is much more general: It applies to all portfolios
and individual securities.
Exercise 5.19
Show that the characteristic lines of all securities intersect at a common
point in the CAPM. What are the coordinates of this point?

124
Mathematics for Finance
The CAPM describes a state of equilibrium in the market. Everyone is
holding a portfolio of risky securities with the same weights as the market
portfolio. Any trades that may be executed by investors will only affect their
split of funds between the risk-free security and the market portfolio. As a
result, the demand and supply of all securities will be balanced. This will remain
so as long as the estimates of expected returns and beta factors satisfy (5.19).
However, as soon as some new information about the market becomes avail-
able to investors, it may affect their estimates of expected returns and beta
factors. The new estimated values may no longer satisfy (5.19). Suppose, for
example, that
µV > rF + (µM −rF )βV
for a particular security. In this case investors will want to increase their relative
position in this security, which offers a higher expected return than required as
compensation for systematic risk. Demand will exceed supply, the price of the
security will begin to rise and the expected return will decline. On the other
hand, if the reverse inequality
µV < rF + (µM −rF )βV
holds, investors will want to sell the security. In this case supply will exceed
demand, the price will fall and the expected return will increase. This will
continue until the prices and with them the expected returns of all securities
settle at a new level, restoring equilibrium.
The above inequalities are important in practice. They send a clear signal
to investors whether any particular security is underpriced or, respectively,
overpriced, that is, whether it should be bought or sold.

6
Forward and Futures Contracts
6.1 Forward Contracts
A forward contract is an agreement to buy or sell an asset on a fixed date
in the future, called the delivery time, for a price specified in advance, called
the forward price. The party to the contract who agrees to sell the asset is
said to be taking a short forward position. The other party, obliged to buy the
asset at delivery, is said to have a long forward position. The principal reason
for entering into a forward contract is to become independent of the unknown
future price of a risky asset. There are a variety of examples: a farmer wishing
to fix the sale price of his crops in advance, an importer arranging to buy
foreign currency at a fixed rate in the future, a fund manager who wants to sell
stock for a price known in advance. A forward contract is a direct agreement
between two parties. It is typically settled by physical delivery of the asset on
the agreed date. As an alternative, settlement may sometimes be in cash.
Let us denote the time when the forward contract is exchanged by 0, the
delivery time by T, and the forward price by F(0, T). The time t market price
of the underlying asset will be denoted by S(t). No payment is made by either
party at time 0, when the forward contract is exchanged. At delivery the party
with a long forward position will benefit if F(0, T) < S(T). They can buy the
asset for F(0, T) and sell it for the market price S(T), making an instant profit
of S(T) −F(0, T). Meanwhile, the party holding a short forward position will
suffer a loss of S(T) −F(0, T) because they will have to sell below the market
price. If F(0, T) > S(T), then the situation will be reversed. The payoffs at
125

126
Mathematics for Finance
delivery are S(T) −F(0, T) for a long forward position and F(0, T) −S(T) for
a short position; see Figure 6.1.
Figure 6.1
Payofffor long and short forward positions at delivery
If the contract is initiated at time t < T rather than 0, then we shall write
F(t, T) for the forward price, the payoffat delivery being S(T) −F(t, T) for a
long forward position and F(t, T) −S(T) for a short position.
6.1.1 Forward Price
The No-Arbitrage Principle makes it possible to obtain formulae for the forward
prices of assets of various kinds. We begin with the simplest case.
Stock Paying No Dividends. Consider a security that can be stored at no
cost and brings no profit (except perhaps for capital gains arising from random
price fluctuations). A typical example is a stock paying no dividends. We shall
denote by r the risk-free rate under continuous compounding and assume that
it is constant throughout the period in question.
An alternative to taking a long forward position in stock with delivery at
time T and forward price F(0, T) is to borrow S(0) dollars to buy the stock
at time 0 and keep it until time T. The amount S(0)erT to be paid to settle
the loan with interest at time T is a natural candidate for the forward price
F(0, T). The following theorem makes this intuitive argument formal.
Theorem 6.1
For a stock paying no dividends the forward price is
F(0, T) = S(0)erT ,
(6.1)
where r is a constant risk-free interest rate under continuous compounding. If
the contract is initiated at time t ≤T, then
F(t, T) = S(t)er(T −t).
(6.2)

6. Forward and Futures Contracts
127
Proof
We shall prove formula (6.1). Suppose that F(0, T) > S(0)erT . In this case, at
time 0
• borrow the amount S(0) until time T;
• buy one share for S(0);
• take a short forward position, that is, agree to sell one share for F(0, T) at
time T.
Then, at time T
• sell the stock for F(0, T);
• pay S(0)erT to clear the loan with interest.
This will bring a risk-free profit of
F(0, T) −S(0)erT > 0,
contrary to the No-Arbitrage Principle. Next, suppose that F(0, T) < S(0)erT .
In this case we construct the opposite strategy to the one above. At time 0
• sell short one share for S(0);
• invest the proceeds at the risk-free rate;
• enter into a long forward contract with forward price F(0, T).
Then, at time T
• cash the risk-free investment with interest, collecting S(0)erT dollars;
• buy the stock for F(0, T) using the forward contract;
• close out the short position in stock by returning it to the owner.
You will end up with a positive amount
S(0)erT −F(0, T) > 0,
again a contradiction with the No-Arbitrage Principle.
The proof of (6.2) is similar. Simply replace 0 by t, observing that the time
elapsed between exchanging the forward contract and delivery is now T −t.
In a market with restrictions on short sales of stock the inequality F(0, T) <
S(0)erT does not necessarily lead to arbitrage opportunities.
Exercise 6.1
Suppose that S(0) = 17 dollars, F(0, 1) = 18 dollars, r = 8%, and short-
selling requires a 30% security deposit attracting interest at d = 4%. Is
there an arbitrage opportunity? Find the highest rate d for which there
is no arbitrage opportunity.

128
Mathematics for Finance
Exercise 6.2
Suppose that the price of stock on 1 April 2000 turns out to be 10%
lower than it was on 1 January 2000. Assuming that the risk-free rate
is constant at r = 6%, what is the percentage drop of the forward price
on 1 April 2000 as compared to that on 1 January 2000 for a forward
contract with delivery on 1 October 2000?
Remark 6.1
In the case considered here we always have F(t, T) = S(t)er(T −r) > S(t). The
difference F(t, T) −S(t), which is called the basis, converges to 0 as t ↗T.
Remark 6.2
Under periodic compounding the forward price is given by
F(0, T) = S(0)(1 + r
m)mT .
In terms of zero-coupon bond prices, this formula becomes
F(0, T) = S(0)B(0, T)−1.
The last formula is in fact more general, requiring no assumption about con-
stant interest rates.
Including Dividends. We shall generalise the formula for the forward price
to cover assets that generate income during the lifetime of the forward contract.
The income may be in the form of dividends or a convenience yield. We shall
also cover the case when the asset involves some costs (called the cost of carry),
such as storage or insurance, by treating the costs as negative income.
Suppose that the stock is to pay a dividend div at an intermediate time t
between initiating the forward contract and delivery. At time t the stock price
will drop by the amount of the dividend paid. The formula for the forward
price, which involves the present stock price, can be modified by subtracting
the present value of the dividend.
Theorem 6.2
The forward price of a stock paying dividend div at time t, where 0 < t < T, is
F(0, T) = [S(0) −e−rtdiv]erT .
(6.3)

6. Forward and Futures Contracts
129
Proof
Suppose that
F(0, T) > [S(0) −e−rtdiv]erT .
We shall construct an arbitrage strategy. At time 0
• enter into a short forward contract with forward price F(0, T) and delivery
time T;
• borrow S(0) dollars and buy one share.
At time t
• cash the dividend div and invest it at the risk-free rate for the remaining
time T −t.
At time T
• sell the share for F(0, T);
• pay S(0)erT to clear the loan with interest and collect er(T −t)div.
The final balance will be positive:
F(0, T) −S(0)erT + er(T −t)div > 0,
a contradiction with the No-Arbitrage Principle. On the other hand, suppose
that
F(0, T) < [S(0) −e−rtdiv]erT .
In this case, at time 0
• enter into a long forward contract with forward price F(0, T) and delivery
at time T;
• sell short one share and invest the proceeds S(0) at the risk-free rate.
At time t
• borrow div dollars and pay a dividend to the stock owner.
At time T
• buy one share for F(0, T) and close out the short position in stock;
• cash the risk-free investment with interest, collecting the amount S(0)erT ,
and pay er(T −t)div to clear the loan with interest.
The final balance will again be positive,
−F(0, T) + S(0)erT −er(T −t)div > 0,
completing the proof.

130
Mathematics for Finance
The formula can easily be generalised to the case when dividends are paid
more than once:
F(0, T) = [S(0) −div0]erT ,
(6.4)
where div0 is the present value of all dividends due during the lifetime of the
forward contract.
Exercise 6.3
Consider a stock whose price on 1 January is $120 and which will pay a
dividend of $1 on 1 July 2000 and $2 on 1 October 2000. The interest
rate is 12%. Is there an arbitrage opportunity if on 1 January 2000 the
forward price for delivery of the stock on 1 November 2000 is $131? If
so, compute the arbitrage profit.
Exercise 6.4
Suppose that the risk-free rate is 8%. However, as a small investor,
you can invest money at 7% only and borrow at 10%. Does either of
the strategies in the proof of Proposition 6.2 give an arbitrage profit if
F(0, 1) = 89 and S(0) = 83 dollars, and a $2 dividend is paid in the
middle of the year, that is, at time 1/2?
Dividend Yield. Dividends are often paid continuously at a specified rate,
rather than at discrete time instants. For example, in a case of a highly diversi-
fied portfolio of stocks it is natural to assume that dividends are paid continu-
ously rather than to take into account frequent payments scattered throughout
the year. Another example is foreign currency, attracting interest at the corre-
sponding rate.
We shall first derive a formula for the forward price in the case of foreign
currency. Let the price of one British pound in New York be P(t) dollars, and
let the risk-free interest rates for investments in British pounds and US dollars
be rGBP and rUSD, respectively. Let us compare the following strategies:
A: Invest P(0) dollars at the rate rUSD for time T.
B: Buy 1 pound for P(0) dollars, invest it for time T at the rate rGBP, and take
a short position in erGBPT pound sterling forward contracts with delivery
time T and forward price F(0, T).
Both strategies require the same initial outlay, so the final values should be
also the same:
P(0)erUSDT = erGBPT F(0, T).
It follows that
F(0, T) = P(0)e(rUSD−rGBP)T .
(6.5)

6. Forward and Futures Contracts
131
Next, suppose that a stock pays dividends continuously at a rate rdiv > 0,
called the (continuous) dividend yield. If the dividends are reinvested in the
stock, then an investment in one share held at time 0 will increase to become
erdivT shares at time T. (The situation is similar to continuous compounding.)
Consequently, in order to have one share at time T we should begin with e−rdivT
shares at time 0. This observation is used in the arbitrage proof below.
Theorem 6.3
The forward price for stock paying dividends continuously at a rate rdiv is
F(0, T) = S(0)e(r−rdiv)T .
(6.6)
Proof
Suppose that
F(0, T) > S(0)e(r−rdiv)T .
In this case, at time 0
• enter into a short forward contract;
• borrow the amount S(0)e−rdivT to buy e−rdivT shares.
Between time 0 and T collect the dividends paid continuously, reinvesting them
in the stock. At time T you will have 1 share, as explained above. At that time
• sell the share for F(0, T), closing out the short forward position;
• pay S(0)e(r−rdiv)T to clear the loan with interest.
The final balance F(0, T) −S(0)e(r−rdiv)T > 0 will be your arbitrage profit.
Now suppose that
F(0, T) < S(0)e(r−rdiv)T .
If this is the case, then at time 0
• take a long forward position;
• sell short a fraction e−rdivT of a share investing the proceeds S(0)e−rdivT
risk free.
Between time 0 and T you will need to pay dividends to the stock owner, raising
cash by shorting the stock. Your short position in stock will thus increase to 1
share at time T. At that time
• buy one share for F(0, T) and return it to the owner, closing out the long
forward position and the short position in stock;
• receive S(0)e(r−rdiv)T from the risk-free investment.
Again you will end up with a positive amount S(0)e(r−rdiv)T −F(0, T) > 0,
contrary to the No-Arbitrage Principle.

