# Portfolio Management & Market Risk

!!! info "Source"
    **Quantitative Finance for Physicists: An Introduction** by Belal E. Baaquie, Academic Press, 2004.
    These notes are used for educational purposes.

## Portfolio Management

Chapter 10
Portfolio Management
This chapter begins with the basic ideas of portfolio selection.
Namely, in Section 10.1, the combination of two risky assets and
the combination of a risky asset and a risk-free asset are considered.
Then two major portfolio management theories are discussed: the
capital asset pricing model (Section 10.2) and the arbitrage pricing
theory (Section 10.3). Finally, several investment strategies based on
exploring market arbitrage opportunities are introduced in Section
10.4.
10.1 PORTFOLIO SELECTION
Optimal investing is an important real-life problem that has been
translated into elegant mathematical theories. In general, opportun-
ities for investing include different assets: equities (stocks), bonds,
foreign currency, real estate, antique, and others. Here portfolios
that contain only financial assets are considered.
There is no single strategy for portfolio selection, because there is
always a trade-off between expected return on portfolio and risk of
portfolio losses. Risk-free assets such as the U.S. Treasury bills guar-
antee some return, but it is generally believed that stocks provide
higher returns in the long run. The trouble is that the notion of ‘‘long
run’’ is doomed to bear an element of uncertainty. Alas, a decade of
111

market growth may end up with a market crash that evaporates a
significant part of the equity wealth of an entire generation. Hence,
risk aversion (that is often well correlated with investor age) is an
important factor in investment strategy.
Portfolio selection has two major steps [1]. First, it is the selection
of a combination of risky and risk-free assets and, secondly, it is the
selection of risky assets. Let us start with the first step.
For simplicity, consider a combination of one risky asset and one
risk-free asset. If the portion of the risky asset in the portfolio is
a(a  1), then the expected rate of return equals
E[R] ¼ aE[Rr] þ (1  a)Rf ¼ Rf þ a(E[Rr]  Rf)
(10:1:1)
where Rf and Rr are rates of returns of the risk-free and risky assets,
respectively. In the classical portfolio management theory, risk is
characterized with the portfolio standard deviation, s.1 Since no
risk is associated with the risk-free asset, the portfolio risk in our
case equals
s ¼ asr
(10:1:2)
Substituting a from (10.1.2) into (10.1.1) yields
E[R] ¼ Rf þ s(E[Rr]  Rf)=sr
(10:1:3)
The dependence of the expected return on the standard deviation is
called the risk-return trade-off line. The slope of the straight line
(10.1.3)
s ¼ (E[Rr]  Rf)=sr
(10:1:4)
is the measure of return in excess of the risk-free return per unit of
risk. Obviously, investing in a risky asset makes sense only if s > 0,
that is, E[Rr] > Rf. The risk-return trade-off line defines the mean-
variance efficient portfolio, that is, the portfolio with the highest
expected return at a given risk level.
On the second step of portfolio selection, let us consider the port-
folio consisting of two risky assets with returns R1 and R2 and with
standard deviations s1 and s2, respectively. If the proportion of the
risky asset 1 in the portfolio is g(g  1), then the portfolio rate of
return equals
E[R] ¼ gE[R1] þ (1  g)E[R2]
(10:1:5)
112
Portfolio Management

and the portfolio standard deviation is
s2 ¼ g2s1
2 þ (1  g)2s2
2 þ 2g(1  g)s12
(10:1:6)
In (10.1.6), s12 is the covariance between the returns of asset 1 and
asset 2. For simplicity, it is assumed further that the asset returns are
uncorrelated, that is, s12 ¼ 0. The value of g that yields minimal risk
for this portfolio equals
gm ¼ s22=(s12 þ s22),
(10:1:7)
This value yields the minimal portfolio risk sm
sm
2 ¼ s1
2s2
2=(s1
2 þ s2
2)
(10:1:8)
Consider an example with E[R1] ¼ 0:1, E[R2] ¼ 0:2, s1 ¼ 0:15,
s2 ¼ 0:3. If g ¼ 0:8, then s  0:134 < s1 and E[R] ¼ 0:12 > E[R1].
Hence, adding the more risky asset 2 to asset 1 decreases the portfolio
risk and increases the portfolio return. This somewhat surprising
outcome demonstrates the advantage of portfolio diversification.
Finally, let us combine the risk-free asset with a portfolio that
contains two risky assets. The optimal combination of the risky
asset portfolio and the risk-free asset can be found at the tangency
point between the straight risk-return trade-off line with the intercept
E[R] ¼ Rf and the risk-return trade-off curve for the risky asset
portfolio (see Figure 10.1). For the portfolio with two risky uncorrel-
ated assets, the proportion g at the tangency point T equals
gT ¼ (E[R1]  Rf)s2
2={(E[R1]  Rf)s2
2 þ (E[R2]  Rf)s1
2}
(10:1:9)
Substituting gT from (10.1.9) into (10.1.5) and (10.1.6) yields the
coordinates of the tangency point (i.e., E[RT] and sT). A similar
approach can be used in the general case with an arbitrary number
of risky assets. The return E[RT] for a given portfolio with risk sT is
‘‘as good as it gets.’’ Is it possible to have returns higher than E[RT]
while investing in the same portfolio? In other words, is it possible to
reach say point P on the risk-return trade-off line depicted in Figure.
10.1? Yes, if you borrow money at rate Rf and invest it in the portfolio
with g ¼ gT. Obviously, the investment risk is then higher than that of
sT.
Portfolio Management
113

10.2 CAPITAL ASSET PRICING MODEL (CAPM)
The Capital Asset Pricing Model (CAPM) is based on the portfolio
selection approach outlined in the previous section. Let us consider
the entire universe of risky assets with all possible returns and risks.
The set of optimal portfolios in this universe (i.e., portfolios with
maximal returns for given risks) forms what is called a efficient
frontier. The straight line that is tangent to the efficient frontier and
has intercept Rf is called the capital market line.2 The tangency point
between the capital market line and the efficient frontier corresponds
to the so-called super-efficient portfolio.
In CAPM, it is assumed that all investors have homogenous expect-
ations of returns, risks, and correlations among the risky assets. It is
also assumed that investors behave rationally, meaning they all hold
optimal mean-variance efficient portfolios. This implies that all invest-
ors have risky assets in their portfolio in the same proportions as the
entire market. Hence, CAPM promotes passive investing in the index
0
0.04
0.08
0.12
0.16
0
0.04
0.08
0.12
0.16
sigma
E[R]
RF
T
P
Figure 10.1 The return-risk trade-off lines: portfolio with the risk-free
asset and a risky asset (dashed line); portfolio with two risky assets (solid
line); Rf ¼ 0:05, s1 ¼ 0:12, s2 ¼ 0:15, E[R1] ¼ 0:08, E[R2] ¼ 0:14.
114
Portfolio Management

mutual funds. Within CAPM, the optimal investing strategy is simply
choosing a portfolio on the capital market line with acceptable risk
level. Therefore, the difference among rational investors is determined
only by their risk aversion, which is characterized with the proportion
of their wealth allocated to the risk-free assets. Within the CAPM
assumptions, it can be shown that the super-efficient portfolio consists
of all risky assets weighed with their market values. Such a portfolio is
called a market portfolio.3
CAPM defines the return of a risky asset i with the security market
line
E[Ri] ¼ Rf þ bi(E[RM]  Rf)
(10:2:1)
where RM is the market portfolio return and parameter beta bi equals
bi ¼ Cov[Ri, RM]=Var[RM]
(10:2:2)
Beta defines sensitivity of the risky asset i to the market dynamics.
Namely, bi > 1 means that the asset is more volatile than the entire
market while bi < 1 implies that the asset has a lower sensitivity to the
market movements. The excess return of asset i per unit of risk (so-
called Sharpe ratio) is another criterion widely used for estimation of
investment performance
Si ¼ (E[Ri]  Rf)=si
(10:2:3)
CAPM, being the equilibrium model, has no time dependence. How-
ever, econometric analysis based on this model can be conducted
providing that the statistical nature of returns is known [2]. It is
often assumed that returns are independently and identically distrib-
uted. Then the OLS method can be used for estimating bi in the
regression equation for the excess return Zi ¼ Ri  Rf
Zi(t) ¼ ai þ biZM(t) þ ei(t)
(10:2:4)
It is usually assumed that ei(t) is a normal process and the S&P 500
Index is the benchmark for the market portfolio return RM(t). More
details on the CAPM validation and the general results for the mean-
variance efficient portfolios can be found in [2, 3].
As indicated above, CAPM is based on the belief that investing in
risky assets yields average returns higher than the risk-free return.
Hence, the rationale for investing in risky assets becomes question-
able in bear markets. Another problem is that the asset diversification
Portfolio Management
115

advocated by CAPM is helpful if returns of different assets are
uncorrelated. Unfortunately, correlations between asset returns may
grow in bear markets [4]. Besides the failure to describe prolonged
bear markets, another disadvantage of CAPM is its high sensitivity to
proxy for the market portfolio. The latter drawback implies that
CAPM is accurate only conditionally, within a given time period,
where the state variables that determine economy are fixed [2]. Then
it seems natural to extend CAPM to a multifactor model.
10.3 ARBITRAGE PRICING THEORY (APT)
The CAPM equation (10.2.1) implies that return on risky assets is
determined only by a single non-diversifiable risk, namely by the risk
associated with the entire market. The Arbitrage Pricing Theory
(APT) offers a generic extension of CAPM into the multifactor
paradigm.
APT is based on two postulates. First, the return for an asset i
(i ¼ 1, . . . , N) at every time period is a weighed sum of the risk factor
contributions fj(t) (j ¼ 1, . . . , K, K < N) plus an asset-specific com-
ponent ei(t)
Ri(t) ¼ ai þ bi1f1 þ bi2f2 þ . . . þ biKfK þ ei(t)
(10:3:1)
In (10.3.1), bij are the factor weights (betas). It is assumed that the
expectations of all factor values and for the asset-specific innovations
are zero
E[f1(t)] ¼ E[f2(t)] ¼ . . . ¼ E[fK(t)] ¼ E[ei(t)] ¼ 0
(10:3:2)
Also, the time distributions of the risk factors and asset-specific
innovations are independent
Cov[fj(t), fj(t0)] ¼ 0, Cov[ei(t), ei(t0)] ¼ 0, t 6¼ t0
(10:3:3)
and uncorrelated
Cov[fj(t), ei(t)] ¼ 0
(10:3:4)
Within APT, the correlations between the risk factors and the asset-
specific
innovations
may
exist,
that
is
Cov[fj(t), fk(t)]
and
Cov[ei(t), ej(t)] may differ from zero.
116
Portfolio Management

The second postulate of APT requires that there are no arbitrage
opportunities. This implies, in particular, that any portfolio in which
all factor contributions are canceled out must have return equal to
that of the risk-free asset (see Exercise 3). These two postulates lead to
the APT theorem (see, e.g., [5]). In its simple form, it states that there
exist such K þ 1 constants l0, l1, . . . lK (not all of them equal zero)
that
E[Ri(t)] ¼ l0 þ bi1l1 þ . . . þ biKlK
(10:3:5)
While l0 has the sense of the risk-free asset return, the numbers lj are
named the risk premiums for the j-th risk factors.
Let us define a well-diversified portfolio as a portfolio that consists
of N assets with the weights wi where P
N
i¼1
wi ¼ 1, so that wi < W=N
and W  1 is a constant. Hence, the specific of a well-diversified
portfolio is that it is not overweighed by any of its asset components.
APT turns out to be more accurate for well-diversified portfolios
than for individual stocks. The general APT states that if the return of
a well-diversified portfolio equals
R(t) ¼ a þ b1f1 þ b2f2 þ . . . þ bKfK þ e(t)
(10:3:6)
where
a ¼
X
N
i¼1
wiai, bi ¼
X
N
k¼1
wkbik
(10:3:7)
then the expected portfolio return is
E[R(t)] ¼ l0 þ b1l1 þ . . . þ bKlK
(10:3:8)
In addition, the returns of the assets that constitute the portfolio
satisfy the simple APT (10.3.5).
APT does not specify the risk factors. Yet, the essential sources of
risk are well described in the literature [6]. They include both macro-
economic factors including inflation risk, interest rate, and corporate
factors, for example, Return on Equity (ROE).4 Development of
statistically reliable multifactor portfolio models poses significant
challenges [2]. Yet, multifactor models are widely used in active
portfolio management.
Portfolio Management
117

Both CAPM and APT consider only one time period and treat the
risk-free interest rate as an exogenous parameter. However, in real
life, investors make investing and consumption decisions that are in
effect for long periods of time. An interesting direction in the port-
folio theory (that is beyond the scope of this book) describes invest-
ment and consumption processes within a single framework. The risk-
free interest rate is then determined by the consumption growth and
by investor risk aversion. The most prominent theories in this direc-
tion are the intertemporal CAPM (ICAPM) and the consumption
CAPM (CCAPM) [2, 3, 7].
10.4 ARBITRAGE TRADING STRATEGIES
The simple investment strategy means ‘‘buy and hold’’ securities
of ‘‘good’’ companies until their performance worsens, then sell them
and buy better assets. A more sophisticated approach is sensitive to
changing economic environment and an investor’s risk tolerance,
which implies periodic rebalancing of the investor portfolio between
cash, fixed income, and equities. Proponents of the conservative
investment strategy believe that this is everything an investor should
do while investing for the ‘‘long run.’’ Yet, many investors are not
satisfied with the long-term expectations: they want to make money
at all times (and who could blame them?). Several concepts being
intensively explored by a number of financial institutions, particu-
larly by the hedge funds, are called market-neutral strategies.
In a nutshell, market-neutral strategy implies hedging the risk of
financial losses by combining long and short positions in the port-
folio. For example, consider two companies within the same industry,
A and B, one of which (A) yields consistently higher returns. The
strategy named pair trading involves simultaneously buying shares
A and short selling shares B. Obviously, if the entire sector rises,
this strategy does not bring as much money as simply buying
shares A. However, if the entire market falls, presumably shares B
will have higher losses than shares A. Then the profits from short
selling shares B would more than compensate for the losses from
buying shares A.
118
Portfolio Management

Specifics of the hedging strategies are not widely advertised for
obvious reasons: the more investors target the same market ineffi-
ciency, the faster it is wiped out. Several directions in the market-
neutral investing are described in the literature [8].
Convertible arbitrage. Convertible bonds are bonds that can be
converted into shares of the same company. Convertible bonds
often decline less in a falling market than shares of the same company
do. Hence, the idea of the convertible arbitrage is buying convertible
bonds and short selling the underlying stocks.
Fixed-income arbitrage. This strategy implies taking long and short
positions in different fixed-income securities. By watching the correl-
ations between different securities, one can buy those securities
that seem to become underpriced and sell short those that look
overpriced.
Mortgage-backed securities (MBS) arbitrage. MBS is actually a
form of fixed income with a prepayment option. Yet, there are so
many different MBS that this makes them a separate business.
Merger arbitrage. This form of arbitrage involves buying shares of a
company that is being bought and short selling the shares of the buying
company. The rationale behind this strategy is that companies are
usually acquired at a premium, which sends down the stock prices of
acquiring companies.
Equity hedge. This strategy is not exactly the market-neutral one, as
the ratio between long and short equity positions may vary depending
on the market conditions. Sometimes one of the positions is the stock
index future while the other positions are the stocks that constitute
this index (so-called index arbitrage). Pair trading also fits this
strategy.
Equity market-neutral strategy and statistical arbitrage. Nicholas
discerns these two strategies by the level of constraints (availability of
resources) imposed upon the portfolio manager [8]. The common
feature of these strategies is that (in contrast to the equity hedge),
they require complete offsetting of the long positions by the short
positions. Statistical arbitrage implies fewer constraints in the devel-
opment of quantitative models and hence a lower amount of the
portfolio manager’s discretion in constructing a portfolio.
Relative value arbitrage. This is a synthetic approach that may
embrace several hedging strategies and different securities including
Portfolio Management
119

equities, bonds, options, and foreign currencies. Looking for the arbi-
trage opportunities ‘‘across the board’’ is technically more challenging
but potentially rewarding.
Some academic research on efficiency of the arbitrage trading
strategies can be found in [9–12] and references therein. Note that
the research methodology in this field is itself a non-trivial problem
[13].
10.5 REFERENCES FOR FURTHER READING
A good introduction into the finance theory, including CAPM, is
given in [1]. For a description of the portfolio theory and investment
science with an increasing level of technical detail, see [5, 14].
10.6 EXERCISES
1. Consider a portfolio with two assets having the following
returns and standard deviations: E[R1] ¼ 0:15, E[R2] ¼ 0:1,
s1 ¼ 0:2, s2 ¼ 0:15. The proportion of asset 1 in the portfolio
g ¼ 0:5. Calculate the portfolio return and standard deviation.
The correlation coefficient between assets is (a) 0.5; (b) 0.5.
2. Consider returns of stock A and the market portfolio M in three
years:
A
7%
12%
26%
M
5%
9%
18%
Assuming the risk-free rate is 5%, (a) calculate b of stock A; and
(b) verify if CAPM describes pricing of stock A.
3. Providing the stock returns follow the two-factor APT:
Ri(t) ¼ ai þ bi1f1 þ bi2 f2 þ ei(t), construct a portfolio with
three stocks (i.e., define w1, w2, and w3 ¼ 1  w1  w2) that
yields return equal to that of the risk-free asset.
4. Providing the stock returns follow the two-factor simple APT,
derive the values of the risk premiums. Assume the expected
returns of two stocks and the risk-free rate are equal to R1, R2,
and Rf, respectively.
120
Portfolio Management


## Market Risk Management

Chapter 11
Market Risk Measurement
The widely used risk measure, value at risk (VaR), is discussed in
Section 11.1. Furthermore, the notion of the coherent risk measure is
introduced and one such popular measure, namely expected tail losses
(ETL), is described. In Section 11.2, various approaches to calculating
risk measures are discussed.
11.1 RISK MEASURES
There are several possible causes of financial losses. First, there is
market risk that results from unexpected changes in the market prices,
interest rates, or foreign exchange rates. Other types of risk relevant
to financial risk management include liquidity risk, credit risk, and
operational risk [1]. The liquidity risk closely related to market risk is
determined by a finite number of assets available at a given price (see
discussion in Section 2.1). Another form of liquidity risk (so-called
cash-flow risk) refers to the inability to pay off a debt in time. Credit
risk arises when one of the counterparts involved in a financial
transaction does not fulfill its obligation. Finally, operational risk is
a generic notion for unforeseen human and technical problems, such
as fraud, accidents, and so on. Here we shall focus exclusively on
measurement of the market risk.
In Chapter 10, we discussed risk measures such as the asset return
variance and the CAPM beta. Several risk factors used in APT were
121

also mentioned. At present, arguably the most widely used risk meas-
ure is value at risk (VaR) [1]. In short, VaR refers to the maximum
amount of an asset that is likely to be lost over a given period at a
specific confidence level. This implies that the probability density
function for profits and losses (P=L)1 is known. In the simplest case,
this distribution is normal
PN(x) ¼
1ffiffiffiffiffiffi
2p
p
s
exp [(x  m)2=2s2]
(11:1:1)
where m and s are the mean and standard deviation, respectively.
Then for the chosen confidence level a,
VAR(a) ¼ sza  m
(11:1:2)
The value of za can be determined from the cumulative distribution
function for the standard normal distribution (3.2.10)
Pr(Z < za) ¼
ðza
1
1ffiffiffiffiffiffi
2p
p
exp [z2=2]dz ¼ 1  a
(11:1:3)
Since za < 0 at a > 50%, the definition (11.1.2) implies that positive
values of VaR point to losses. In general, VaR(a) grows with the
confidence
level
a.
Sufficiently
high
values
of
the
mean
P=L (m > sza) for given a move VaR(a) into the negative region,
which implies profits rather than losses. Examples of za for typical
values of a ¼ 95% and a ¼ 99% are given in Figure 11.1. Note that
the return variance s corresponds to za ¼ 1 and yields a  84%.
The advantages of VaR are well known. VaR is a simple and
universal measure that can be used for determining risks of different
financial assets and entire portfolios. Still, VaR has some drawbacks
[2]. First, accuracy of VaR is determined by the model assumptions
and is rather sensitive to implementation. Also, VaR provides an
estimate for losses within a given confidence interval a but says
nothing about possible outcomes outside this interval. A somewhat
paradoxical feature of VaR is that it can discourage investment
diversification. Indeed, adding volatile assets to a portfolio may
move VaR above the chosen risk threshold. Another problem with
VaR is that it can violate the sub-additivity rule for portfolio risk.
According to this rule, the risk measure r must satisfy the condition
122
Market Risk Measurement

r(A þ B)  r(A) þ r(B)
(11:1:4)
which means the risk of owning the sum of two assets must not be
higher than the sum of the individual risks of these assets. The
condition (11.1.4) immediately yields an upper estimate of combined
risk. Violation of the sub-additivity rule may lead to several problems.
In particular, it may provoke investors to establish separate accounts
for every asset they have. Unfortunately, VaR satisfies (11.1.4) only if
the probability density function for P/L is normal (or, more generally,
elliptical) [3].
The generic criterions for the risk measures that satisfy the require-
ments of the modern risk management are formulated in [3]. Besides
the sub-additivity rule (11.1.4), they include the following conditions.
r(lA) ¼ lr(A), l > 0 (homogeneity)
(11:1:5)
r(A)  r(B), if A  B (monotonicity)
(11:1:6)
r(A þ C) ¼ r(A)  C (translation invariance)
(11:1:7)
In (11.1.7), C represents a risk-free amount. Adding this amount to
a risky portfolio should decrease the total risk, since this amount is
0
0.05
0.1
0.15
0.2
0.25
0.3
0.35
0.4
0.45
−5
−4
−3
−2
−1
0
1
2
3
4
5
VaR at 95%
z = −1.64
VaR at 99%
z = −2.33
VaR at 84%
z = −1
Figure 11.1 VaR for the standard normal probability distribution of P/L.
Market Risk Measurement
123

not subjected to potential losses. The risk measures that satisfy the
conditions (11.1.4)–(11.1.7) are called coherent risk measures. It can
be shown that any coherent risk measure represents the maximum of
the expected loss on a set of ‘‘generalized scenarios’’ where every such
scenario is determined with its value of loss and probability of occur-
rence [3]. This result yields the coherent risk measure called expected
tail loss (ETL):2
ETL ¼ E[LjL > VaR]
(11:1:8)
While VaR is an estimate of loss within a given confidence level,
ETL is an estimate of loss within the remaining tail. For a given
probability distribution of P/L and a given a, ETL is always higher
than VaR (cf. Figures 11.1 and 11.2).
ETL has several important advantages over VaR [2]. In short, ETL
provides an estimate for an average ‘‘worst case scenario’’ while VaR
only gives a possible loss within a chosen confidence interval. ETL
has all the benefits of the coherent risk measure and does not discour-
age risk diversification. Finally, ETL turns out to be a more conveni-
ent measure for solving the portfolio optimization problem.
0
0.05
0.1
0.15
0.2
0.25
0.3
0.35
0.4
0.45
−5
−4
−3
−2
−1
0
1
2
3
4
5
ETL at 95%
z = −2.06
ETL at 99%
z = −2.66
ETL at 84%
z = −1.52
Figure 11.2 ETL for the standard normal probability distribution of P/L.
124
Market Risk Measurement

11.2 CALCULATING RISK
Two main approaches are used for calculating VaR and ETL [2].
First, there is historical simulation, a non-parametric approach that
employs historical data. Consider a sample of 100 P/L values as a
simple example for calculating VaR and ETL. Let us choose the
confidence level of 95%. Then VaR is the sixth smallest number in
the sample while ETL is the average of the five smallest numbers
within the sample. In the general case of N observations, VaR at the
confidence level a is the [N(1  a) þ 1] lowest observation and ETL is
the average of N(1  a) smallest observations.
The well-known problem with the historical simulation is handling
of old data. First, ‘‘too old’’ data may lose their relevance. Therefore,
moving data windows (i.e., fixed number of observations prior to
every new period) are often used. Another subject of concern is
outliers. Different data weighting schemes are used to address this
problem. In a simple approach, the historical data X(t  k) are multi-
plied by the factor lk where 0 < l < 1. Another interesting idea is
weighting the historical data with their volatility [4]. Namely, the asset
returns R(t) at time t used in forecasting VaR for time T are scaled
with the volatility ratio
R0(t) ¼ R(t)s(T)=s(t)
(11:2:1)
where s(t) is the historical forecast of the asset volatility.3 As a result,
the actual return at day t is increased if the volatility forecast at day T
is higher than that of day t, and vice versa. The scaled forecasts R0(t)
are further used in calculating VaR in the same way as the forecasts
R(t) are used in equal-weight historical simulation. Other more so-
phisticated non-parametric techniques are discussed in [2] and refer-
ences therein.
An obvious advantage of the non-parametric approaches is their
relative conceptual and implementation simplicity. The main disad-
vantage of the non-parametric approaches is their absolute depend-
ence on the historical data: Collecting and filtering empirical data
always comes at a price.
The parametric approach is a plausible alternative to historical
simulation. This approach is based on fitting the P/L probability
distribution to some analytic function. The (log)normal, Student
Market Risk Measurement
125

and extreme value distributions are commonly used in modeling P/L
[2, 5]. The parametric approach is easy to implement since the analytic
expressions can often be used. In particular, the assumption of the
normal distribution reduces calculating VaR to (11.1.2). Also, VaR
for time interval T can be easily expressed via VaR for unit time (e.g.,
via daily VaR (DVaR) providing T is the number of days)
VaR(T) ¼ DVaR
ffiffiffi
T
p
(11:2:2)
VaR for a portfolio of N assets is calculated using the variance of the
multivariate normal distribution
sN
2 ¼
X
N
i, j¼1
sij
(11:2:3)
If the P/L distribution is normal, ETL can also be calculated analyt-
ically
ETL(a) ¼ sPSN(Za)=(1  a)  m
(11:2:4)
The value za in (11.2.4) is determined with (11.1.3). Obviously, the
parametric approach is as good and accurate as the choice of the
analytic probability distribution.
Calculating VaR has become a part of the regulatory environment
in the financial industry [6]. As a result, several methodologies have
been developed for testing the accuracy of VaR models. The most
widely used method is the Kupiec test. This test is based on the
assumption that if the VaR(a) model is accurate, the number of the
tail losses n in a sample N is determined with the binomial distribu-
tion
PB(n; N, 1  a) ¼
N!
n!(N  n)! (1  a)na(Nn)
(11:2:5)
The null hypothesis is that n/N equals 1  a, which can be tested with
the relevant likelihood ratio statistic. The Kupiec test has clear mean-
ing but may be inaccurate for not very large data samples. Other
approaches for testing the VaR models are described in [2, 6] and
references therein.
126
Market Risk Measurement

11.3 REFERENCES FOR FURTHER READING
The Jorion’s monograph [1] is a popular reference for VaR-based
risk management. The Dowd’s textbook [2] is a good resource for the
modern risk measurement approaches beyond VaR.
11.4 EXERCISES
1. Consider a portfolio with two assets: asset 1 has current value $1
million and annual volatility 12%; asset 2 has current value $2
million and annual volatility 24%. Assuming that returns are
normally distributed and there are 250 working days per year,
calculate 5-day VaR of this portfolio with 99% confidence level.
Perform calculations for the asset correlation coefficient equal
to (a) 0.5 and (b) 0.5.
2. Verify (11.2.4).
*3. Implement the algorithm of calculating ETL for given P/L
density function. Analyze the algorithm accuracy as a function
of the number of integration points by comparing the calcula-
tion results with the analytic expression for the normal distribu-
tion (11.2.4).
Market Risk Measurement
127

This page intentionally left blank 

