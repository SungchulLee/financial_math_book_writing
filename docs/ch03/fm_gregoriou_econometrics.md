# Financial Econometrics: Derivatives & Hedge Funds

!!! info "Source"
    **Financial Econometrics: From Basics to Advanced Modeling Techniques** edited by Greg N. Gregoriou and Razvan Pascalau, Wiley, 2009.
    These notes are used for educational purposes.

## Hedge Funds and Derivatives Pricing

Part I
Derivatives Pricing and
Hedge Funds


1
The Operation of Hedge Funds:
Econometric Evidence, Dynamic
Modeling, and Regulatory
Perspectives
Willi Semmler and Raphaële Chappe
1.1
Introduction
The Madoff case has all the makings of a Ponzi scheme. Ponzi schemes
follow what Hyman Minsky described as Ponzi finance. Do hedge funds,
or at least some of them, follow a similar scheme? The best summary
of different financing practices, such as hedge, speculative, and Ponzi
financing, is given in Minsky (1986). Hedge finance is a situation where
operating cash flow can service all payment obligations associated with
the financing. Speculative finance involves situations where operating
cash flow supports interest payments but not repayment of principal.
Ponzi finance describes a situation where operating cash flow is insuf-
ficient to cover either principal or interest payments, which can be
financed only via an increase in liabilities, thus by a new inflow of funds.
This chapter shows a model that can be used to describe situations in
asset management where the use of leverage to generate above-average
returns may result in some hedge funds finding themselves, willingly
or unwillingly, embroiled in a Ponzi financing scheme. This chapter is
organized as follows. After reviewing the literature on hedge funds, this
chapter briefly examines empirical data on the structure of the indus-
try: size, assets under management, measures of returns, and leverage.
This chapter then proceeds to develop a dynamic model of the wealth-
generating process in a hedge fund. If the manager attracts investors by
promising high returns, the hedge fund is, in essence, borrowing at a
3

4
W. Semmler and R. Chappe
high interest rate. If actual returns do not exceed this high cost of bor-
rowing, on average the hedge fund persistently needs positive inflow of
fresh funds in order not to become insolvent. While hedge finance is
typically associated with a reasonable debt-to-equity ratio, and specu-
lative finance typically results in liabilities being rolled over, in Ponzi
financing the value of net equity is gradually reduced as the company is
in essence continually borrowing against the future. In Section 1.4, we
run a simulation of the impact of the sudden decline of inflow of funds
on the hedge funds, ultimately leading to insolvency.
An economy where Ponzi finance dominates is inherently fragile,
unstable, and conducive to financial crisis. The high level of risky credit
is unsustainable in the long run, and it is only a question of time
before borrowers start to default, potentially bringing the entire financial
system to the brink of collapse via contagion effects if there is suffi-
cient interconnectedness. The hedge-fund industry has been opaque,
with little regulatory oversight and no reporting requirements, cre-
ating opportunities for such Ponzi financing. Given the size of the
industry and the gradually increased exposure of ordinary investors
and the general public to hedge funds, if indeed some funds follow
a pattern of Ponzi financing, there are implications for systemic risk.
However, greater transparency is necessary on the part of hedge funds to
even begin to understand such implications. A new regulatory frame-
work is needed to that effect and has been proposed by the Obama
Administration.
1.2
The literature on hedge funds
The hedge-fund industry is largely unregulated. Hedge funds are under
no obligation to report net asset values or income statements, unlike
their counterparts in the mutual fund industry, which have to provide
daily net asset value calculations and quarterly filings. Hedge-fund man-
agers report performance information to different databases on a purely
voluntary basis. This has given rise to several biases and the issue of
distorted data, thoroughly examined in the literature. Survivorship bias
originates from lower returns being excluded from performance studies
if the hedge fund has failed (only surviving funds are analyzed). There
are different studies and estimates of survivorships bias in the literature,
analyzing different years and different funds. Amin and Kat (2003) esti-
mate survivorship bias at about 2 percent per year. Fung and Hsieh (2000)
have calculated that the survivorship bias is 3 percent annually with a
15 percent dropout rate. Malkiel and Saha (2004) found a bias averaging

The Operation of Hedge Funds
5
3.74 percent per year. Self-selecting bias is generated to the extent that
hedge-fund managers report performance after the fact and only have
an incentive to do so if the hedge fund has performed well. Hedge funds
might wait for a good track record before they start to report to a database.
Underperforming funds might decide to stop reporting to a database. It
is typically the case that hedge funds stop reporting during their last
months (as was the case, for example, with Long Term Capital Manage-
ment losses between October 1997 and October 1998, which were not
reported to data providers).
One example of self-selecting bias is the backfill bias (also called instant
history bias), which appears when hedge-fund managers add histor-
ical results to their files to give a more comprehensive view of the
fund’s performance once the fund begins reporting to a database. Since
fund managers have an incentive to begin reporting only with a good
track record, backfilled returns tend to be higher than contemporane-
ously reported returns. The backfill bias has been addressed for different
databases at different times. Fung and Hsieh (2000) estimated the backfill
bias to be 1.4 percent for the Tass database over the period 1994–1998.
Also on the basis of the Tass database, Posthuma and Van Der Sluis
(2003) have found that backfilled returns are on average 4 percent higher
annually than normal returns.
Much of the literature is focused on risk analytics for hedge funds.
One issue is that the risk/reward profile for most hedge funds is not
as well understood as that for traditional investments. It is well estab-
lished that there is typically a trade-off between risk and return. The
high (double-digit) returns historically earned by hedge funds may well
present underlying risk exposures that are not well identified and man-
aged by traditional risk-management tools. Lo (2001) has stressed the
need for a new set of risk analytics designed to address the unique fea-
tures of hedge funds and to go beyond traditional value-at-risk analysis.
Such unique features include survivorship bias, the non-normal distri-
bution of returns, and the enormous flexibility in trading enabled by
the absence of regulatory constraints and by the hedge-fund manager’s
ability to manage positions very actively. The need to replace traditional
risk measures has led to alternative performance measures, such as the
downside risk framework designed to take into account the asymmetry
of returns. Generally speaking, the downside risk framework attempts
to take into consideration returns which are inferior to a target rate
of return. Mamoghli and Daboussi (2009) attempt to study the impact
of downside risk measures on the performance measurement of hedge
funds. More detail can be found in Section 1.3.

6
W. Semmler and R. Chappe
Chan et al. (2006) have examined the risk of illiquidity exposure and
have attempted to develop quantitative measures of systemic risk. Illiq-
uid exposure is particularly relevant in the event of a forced liquidation,
which is a real threat for hedge funds due to the highly leveraged nature
of their positions. Quick withdrawals of credit, such as that resulting
from adverse changes in the market value of posted collaterals, can
directly lead to forced liquidations. In turn, the unwinding of large
positions over short periods can create significant market disruptions
and a breakdown of the financial system as a whole (systemic risk).
Getmansky et al. (2004) show that high levels of serial correlations can
be partly explained by illiquidity of the hedge fund’s portfolio. Chan
et al. (2006) argue that autocorrelation coefficients of the fund’s monthly
returns are useful indicators of liquidity exposure and show that hedge
funds display a significantly higher level of serial correlation than mutual
funds.1
There is also some analysis in the literature more specifically focused
on the factors that explain the failure of a hedge fund. Malkiel and Saha
(2004) have developed probit regression analysis to examine the proba-
bility of a fund’s survival. The results show that the fund’s performance in
the most recent four quarters is an important determinant of the fund’s
probability of survival, that large funds have a higher probability of sur-
vival, and that a high standard deviation of returns in the fund’s most
recent year has a negative impact on a fund’s probability of survival. Fur-
ther, Malkiel and Saha (2004) find that a fund is more likely to fail in the
first few years of operation and that once a fund has survived the first
years and has established a track record, its likelihood of failure declines
over time.
1.3
The empirics of hedge funds
The size of the hedge-fund industry has exploded in the past ten years. Its
growth, for the most part attributable to large returns generated through
high leverage and use of derivatives, has had a significant impact on
the structure of U.S. and global markets. The industry has grown into
a parallel financial universe – a shadow banking system. Hedge funds
are involved in virtually every kind of market and invest in every kind
of asset: from equity, loans, mortgages, and distressed debt to project
finance, derivatives, etc. But the industry is still to a large extent unreg-
ulated. As a result, it is an even greater factor of systemic risk than it was
in 1998 when the Fed intervened to prevent the near collapse of Long
Term Capital Management.

The Operation of Hedge Funds
7
The term “systemic risk” is used to describe the possibility that the
failure of one financial institution can disrupt the financial system as
a whole through a series of correlated defaults. For example, the bank-
ing panics in the USA during 1930–1933 caused many failures of banks
which were otherwise financially sound.2 Originally created as a tem-
porary regulatory agency under the Banking Act of 1933, the Federal
Deposit Insurance Corporation (FDIC) was designed to insure deposits
in all national banks. The coverage is limited to a given amount per
depositor, recently increased to $250,000 until December 31, 2013. By
protecting depositors from bank failures, the FDIC significantly reduces
the risk of bank runs and thus minimizes systemic risk. Yet the size and
evolution of the hedge-fund industry raises the question of whether it is
generating a new form of systemic risk: that of market disruptions caused
by hedge-fund failures.
There are different estimates of the current size of the hedge-fund
industry, partly due to the fact that there is no single definition of what
constitutes a hedge fund, resulting in different views of what comprises
the hedge-fund universe. Hedge Fund Intelligence has estimated total
assets under management to be at $1.808 trillion3 at the end of 2008,
while Hedge Fund Research (HFR) estimates a lower figure of $1.4 tril-
lion.4 As would be expected in light of recent market disruptions, the
year 2008 was a difficult one for the hedge-fund industry. Hedge funds
experienced losses and redemptions and saw $155 billion of net out-
flows.5 The outlook for 2010 is more promising. Deutsche Bank estimates
the industry to attract $222 billion of new funds, and thus nearly return
to pre-crisis levels.6
In spite of the recent downturn, these figures show that the industry
has grown approximately by a factor of five from $387 billion in 1998.
By comparison, over the same period, U.S. GDP has grown by only 64
percent and the mutual fund industry has grown by only 69 percent.7
Citadel Investment Group, which manages approximately $15 billion
of investment capital, accounts for nearly 10 percent of the daily trad-
ing volume of U.S. equities and is the largest market maker of options
in the U.S., executing approximately 30 percent of all equity options
trades daily (Griffin 2008). Further, ordinary investors and the gen-
eral public have been increasingly exposed to the hedge-fund industry.
This is due to new entities investing in hedge funds, such as pension
funds, universities, endowments, charitable organizations, foundations,
and “funds of hedge funds” that offer shares to the general public. In
addition, hedge funds have been somewhat loosening their investment
requirements.

8
W. Semmler and R. Chappe
As for other active investment portfolios, hedge-fund performance
is typically measured by alphas and betas, as well as by Sharpe ratios.
Hedge-fund returns are often characterized through the use of a model
giving the following expected return-beta expression: E(ri) = αi +βiE(rm),
where E(ri) is the expected return of the fund and E(rm) is the expected
return of the market as a whole. Alternatively, the model may use
only the return in excess of the risk-free rate. The beta coefficient mea-
sures the tendency of the return to rise or fall in correlation with the
market. The βiE(rm) term should correspond to the return that can be
obtained with any diversified investment, for example an index fund.
The alpha term captures the return in excess of this amount. Roughly,
the beta and alpha terms measure the passive and active components
of the return respectively. Normally the beta should be the right bench-
mark for a hedge fund, and one would expect to be paying fees only
for the alpha. However, this is not the case, as the compensation struc-
ture of hedge funds is unique, typically a 2 percent management fee
based on assets under management and a 20 percent performance fee
on total return.8 Presumably, it is the ability to deliver high alphas
that is responsible for the rise of the hedge-fund industry. While some
papers have confirmed statistically significant positive alphas, others
have shown that a substantial part of the return can be explained by
simple stock, bond, and cash betas (Ibbotson and Cheng 2005). Gilli
et al. (2010) even show it may be possible to replicate the attractive fea-
tures of hedge-fund returns using liquid assets. They are able to construct
a portfolio that closely follows the CSFB/Tremont Hedge Fund Index but
is less sensitive to adverse equity-market movements. This would allow
investors to avoid high management fees, limited liquidity, potential
redemption fees, and ultimately the lack of transparency associated with
hedge funds.
The beta term can also be defined as the coefficient in a multiple
regression on the return of the market portfolio (typically Standard &
Poor’s 500 or other index), with the alpha term the intercept (Cochrane
1999). Some alpha and beta estimates from the literature are presented
in Table 1.1. In addition, Ibbotson and Cheng (2005) have also estimated
a breakdown of return between the management and performance fee,
and the alpha and beta returns. Working on an equally weighted index
of 3,000 hedge funds over the period January 1995 to March 2004,9 they
estimated the pre-fee return from the fund to be 12.8 percent, which con-
sisted of 3.8 percent going to fees, 3.7 percent from the alpha, and 5.4
percent from the beta. Table 1.2 summarizes the findings of Cochrane
(2005), based on regressions using CFSB/Tremont indices.

The Operation of Hedge Funds
9
Table 1.1
Alpha and beta estimates
Source
Alpha
Beta
Database
used
Years
examined
Number
of hedge
funds
examined
Agarwal and
Naik (2000)
0.54 to 1.25
depending
on hedge
fund
strategy
N/A
Hedge
Fund
Research
January
1994 to
December
1998
1,000
Malkiel and
Saha (2004)
0.231
(contempo-
raneous
betas) 0.393
(lagged
betas)
TASS
1996–2003
2,024
Goetzmann
and Ross (2000)
0.3
N/A
TASS
January
1994 to
May 2000
1,221
Brunnermeier
and Nagel
(2004)
N/A
0.42
merged
database
of MAR,
TASS, and
HFR
April 1998
to
December
2000
N/A
Table 1.2
Alpha and beta estimates across investment styles
Style
Expected
Return
(%/mo)
a
b
a3
b3
Index
0.64
0.46
0.28
0.36
0.44
Std. errors
0.20
0.17
0.04
Short
−0.53
0.10
−0.94
0.13
−0.99
Emerging markets
0.39
0.00
0.58
−0.07
0.69
Event
0.61
0.46
0.22
0.38
0.37
Global Macro
0.93
0.82
0.17
0.74
0.31
Long/Short equity
0.73
0.42
0.47
0.32
0.65
Source: Cochrane (2005) regressions using CFSB/Tremont indices at hedgeindex.com.
The Sharpe ratio is widely used in financial analysis (Sharpe 1994).
The Sharpe ratio SR measures the ratio of the return of an investment
earned in excess of the risk-free rate (typically the appropriate T-bill rate)
over the return volatility (measured by the standard deviation), for a

10
W. Semmler and R. Chappe
given time period. Sharpe ratios are often characterized with the fol-
lowing expression: SR = E(Rt)−Rf
σ
, where E(Rt) is the expected return of
the fund portfolio between dates t −1 and t, Rf is the risk-free return
(or other benchmark) in that period, and σ the standard deviation of
the portfolio return (see Lo 2002). Roughly speaking, the ratio can be
described as the reward per unit of risk. Xiong (2009) finds that funds
with more assets tend to produce higher returns at lower levels of volatil-
ity, resulting in superior risk-adjusted performance. Lo (2002) has shown
that annualized hedge-fund Sharpe ratios figures, computed by multiply-
ing monthly Sharpe ratios by √12, are often overstated or understated by
as much as 65 percent due to positively or negatively serially correlated
returns. These estimation errors are attributable to approaches that do
not take into consideration the statistical properties of the underlying
returns. Lo (2002) shows that a more accurate measure of annualized
Sharpe ratios requires the use of appropriate statistical distributions for
the return history. There are many estimates of Sharpe ratios in the
literature. Tables 1.3 and 1.4 summarize a few findings.
One criticism is that the traditional measures of alphas, betas, and
Sharpe ratios are static in nature (i.e. based on return distributions at a
given point in time). Lo (2001) has identified the need for a new set of
risk analytics better suited to address the unique features of hedge-fund
Table 1.3
Sharpe ratio estimates
Source
Sharpe ratio
Risk-free
rate per
annum
Database
used
Years
exam-
ined
Number of
hedge
funds
examined
Agarwal
and Naik
(2000)
0.10
(quarterly
for
directional
strategies)
0.46
(quarterly
for non-
directional
strategies)
5%
Hedge
Fund
Research
January
1994 to
December
1998
1,000
Goetzmann
and Ross
(2000)
1.16
(annual)
US 30
day T-bill
TASS
January
1994 to
May 2000
1,221

The Operation of Hedge Funds
11
Table 1.4
Sharpe ratio estimates across investment styles
Annualized
Sharpe
ratio
Annual
adjusted
Sharpe
ratio
Mean
SD
Mean
SD
Database
used
Years
examined
Number
of hedge
funds
examined
Convertible
arbitrage
2.38
3.66
1.85
2.55
TASS
February 1977–
August 2004
176
Dedicated
short-seller
0.05
0.59
0.19
0.46
TASS
February 1977–
August 2004
29
Emerging
markets
0.86
1.63
0.84
1.31
TASS
February 1977–
August 2004
263
Equity
market
neutral
0.97
1.24
1.06
1.53
TASS
February 1977–
August 2004
260
Event driven
1.71
1.48
1.49
1.48
TASS
February 1977–
August 2004
384
Fixed-
income
arbitrage
2.59
9.16
2.29
5.86
TASS
February 1977–
August 2004
175
Global
macro
0.60
0.92
0.70
0.90
TASS
February 1977–
August 2004
232
Long/short
equity
0.82
1.06
0.81
1.07
TASS
February 1977–
August 2004
1,415
Managed
futures
0.34
0.91
0.50
0.88
TASS
February 1977–
August 2004
511
Multistrategy
1.67
2.16
1.49
2.05
TASS
February 1977–
August 2004
139
Fund of
funds
1.27
1.37
1.21
1.22
TASS
February 1977–
August 2004
952
Source: Chan et al. (2006).
investments as the “next challenge in the evolution of the hedge-fund
industry.” Lo (2008a) has proposed new measures of performance that
capture both static and dynamic aspects of decision making on the part
of the hedge-fund manager, in an attempt to consider forecasting skills
that are also essential to successful active investment strategies. This new
methodology decomposes a portfolio’s expected return into two distinct
components. The first is a static weighted average of individual securities’
expected returns, which measures the portion of expected return due to

12
W. Semmler and R. Chappe
static investments in the underlying securities. The second component
is the sum of covariances between returns and portfolio weights, which
captures the forecast power implicit in the manager’s dynamic invest-
ment choices. The key assumption is that at any given date portfolio
weights are functions of the manager’s prior information. Thus the cor-
relation between portfolio weights and returns is used as a measure of the
predictive power of the information used by the manager to select his
portfolio weights. This methodology is particularly relevant for hedge-
fund strategies where both components are significant contributors to
their expected returns.
Another criticism of the alpha, beta, and Sharpe ratios measures is that
hedge funds may display nonlinearities that are not captured by linear
regression models. The distribution of hedge-fund returns displays non-
normal characteristics, which have been analyzed in the literature. For
example, Brooks and Kat (2002) have found that published hedge-fund
indexes exhibit high kurtosis, indicating that the distribution has “fat”
tails. Examining data from the Tass database from 1995 to 2003 for vari-
ous hedge-fund categories, Malkiel and Saha (2004) have confirmed that
hedge-fund returns are characterized by high kurtosis and that many
hedge-fund categories have considerable negative skew, implying an
asymmetric distribution. The shape of the probability distribution of
returns affects the Sharpe ratio. For example, Bernardo and Ledoit (2000)
show that Sharpe ratios are misleading when the shape of the return
distribution is far from normal.
One possible approach is to accept these limitations, recognizing that
the measures are not robust to manipulations, and instead to focus
on identifying strategies that “game” these performance measures, for
example techniques for maximizing the Sharpe ratio. Other approaches
attempt to come up with alternatives to the Sharpe ratio, for example
stochastic-discount factor-based performance measures (Chen and Knez
1996), or downside variance, a new concept in risk analysis that can be
used even when return series are not normally distributed. Downside
risk analysis focuses on downward exposure rather than total volatility.
The basic premise is that the investor has a threshold of desired per-
formance called the minimum acceptable rate of return (MAR), which
can be an index or a risk-free rate. Downside volatility is the volatil-
ity of returns below this benchmark. The Sortino ratio can be formed
as the return in excess of the benchmark over the downside volatility
and used as an alternative to the Sharpe ratio. The Sortino ratio (Sortino
and Price 1994) is a measure of risk-adjusted return based on the MAR
of each investor. Mamoghli and Daboussi (2009) show that hedge-fund

The Operation of Hedge Funds
13
strategies change ranks when the performance measure changes from
the Sharpe ratio to the Sortino ratio or to other alternative performance
measures. The use of the Sortino ratio allows taking into account the
asymmetric nature of the returns, which is not captured by the measure
of variance in the Sharpe ratio. Investors are also using maximum draw-
down as a measure of expected loss. The maximum drawdown reflects
the biggest past loss as a percentage of the prior high watermark. It
makes no assumptions regarding distribution, and hence is robust to
skewed distributions. For an example of the use of maximum draw-
down to analyze performance of a fund of hedge funds, see Heidorn
et al. (2009).
The main source of leverage for hedge funds is collaterized borrow-
ing through repo markets and prime brokers. Because hedge funds have
been virtually unregulated, they are not required to report their use of
leverage and face no capital adequacy requirements. Leverage can be
defined in balance-sheet terms, as the ratio of borrowing to net worth
(equity). However, this definition fails to capture another implicit source
of leverage, the additional embedded leverage of derivative products in
which hedge funds have traditionally invested. This definition is also
static and fails to capture the links between the ease with which a hedge
fund can borrow and the fund assets’ market liquidity. Brunnermeier
and Pedersen (2009) provide a model that links an asset’s market liq-
uidity with traders’ funding liquidity, showing the interconnectedness
between the two. In this model, market liquidity is defined as the differ-
ence between the transaction price and the asset’s fundamental value,
while funding liquidity is defined as the ability to raise cash at short
notice. Brunnermeier and Pedersen (2009) show that a mechanism of
mutual reinforcement between market liquidity and funding liquidity
may result in liquidity spirals. For example, the tightening of funding
lowers market liquidity, leading to higher margin requirements, which
in turn further accelerates the tightening of funding standards (margins
are the difference between the security’s price and collateral value and
must be financed by the investor’s own capital). More generally, while
solvency itself is typically determined as a “stock” value, funding liq-
uidity can be expressed as a flow constraint, whereby at each point in
time money outflows are less than inflows and money held by the fund
(see for example Drehmann 2007 and Drehmann and Nikolaou 2009).
This flow constraint captures the liquidity spiral described by Brunner-
meier and Pedersen (2009). Further, leverage levels also rise and fall on
the basis of the fluctuations of the measured riskiness of existing assets,
which may be tied to macroeconomic cycles (see Adrian and Shin 2007).

14
W. Semmler and R. Chappe
In this sense, leverage and its evolution can be thought of in terms of
economic risk relative to capital.
For these reasons, it has been difficult to estimate accurate leverage
levels in the hedge-fund industry. In the absence of clear reporting of
hedge-fund leverage, the size of market positions managed by hedge
funds compared to funds received from investor subscriptions is a good
preliminary indicator of leverage. As a whole, hedge funds controlled
approximately $3.7 trillion of market positions as of the end of 2008,
indicating on average leverage at a ratio of 1 to 1.10 However, there
are potentially vast differences between funds: for example, Long Term
Capital Management was very highly leveraged at a ratio of 28 to 1 (debt
to equity) at the end of 1995,11 as part of a strategy to multiply profit
on very tiny spreads,12 while Paulson & Co., an investment advisory
firm that currently manages approximately $36 billion in assets, is only
leveraged up to 33 percent of its equity capital.13 Prior to the current
financial crisis, around 70 percent of hedge funds was levered at less than
2 to 1.14 The industry also experienced some deleveraging in 2009. In a
survey conducted by Deutsche Bank at the end of 2008, only 12 percent
of participants said that they used leverage, and only a further 4 percent
indicated that they were interested in doing so, as opposed to 24 percent
and 12 percent respectively 12 months before.15 Thus, on average, the
industry is not as levered as some of the banking institutions.16 This
said, leverage is undisclosed to investors and to the government, and, as
we have mentioned, additional leverage embedded in certain products
is not really being measured.
1.4
A dynamic model
In order to show how an unregulated hedge fund follow a speculative
or Ponzi financing as defined in Minsky (1986), we want to introduce
a stylized model. To study this problem in a simplified way (a more
sophisticated dynamic decision model is sketched in the Appendix),
we propose a dynamic model of wealth accumulation where the stochas-
tic returns take on the form of a Brownian motion with mean reverting.
This type of model has been used by, among others, Campbell and
Viceira (2002), Wachter (2002), Munk et al. (2004), Platen and Semm-
ler (2009), and Brunnermeier and Sannikov (2009). Details of such
a model can also be found in Chiarella et al. (2007). As it is modi-
fied here, it can be seen to reflect well the risk-taking operations of
hedge funds.

The Operation of Hedge Funds
15
1.4.1
Returns to size
Standard economic theory on wealth accumulation suggests that the dif-
ference in wealth arises from income differences (shocks) and differences
in saving rates, discount rates, and risk appetite and tax treatment.
Cagetti and De Nardi (2006) give a comprehensive overview of the stan-
dard intertemporal economic models and the standard causes for the
increase in wealth.
Here we want to use a dynamic portfolio approach of the Campbell
and Viceira type, which includes not only a wealth equation but also
Brownian motions for returns. Yet, we want to argue that there are scale
effects from wealth, which might have to be considered when sketch-
ing such a model. In general we could imagine three types of scale
effects:
First, some investors have more or better information about expected
returns than others. Though it is commonly assumed that markets are
efficient and that no money is to be made by forecasting (all information
is already built into asset prices and returns), industry, firm, and product
knowledge, as well as knowledge on innovations, product development,
and future market share, is likely to give rise to better information and
higher expected returns.17 This has often been the case in industry devel-
opments such as the oil boom before World War I (WWI), the boom in
the auto industry after WWI, the boom in the steel industry during and
after WWI, the high-tech boom in the 1990s, the commodity price boom
after 1995, the real-estate boom after 2001, and the recent banking and
finance industry boom. Note, however, that there is also often manip-
ulation of information, in particular when there are stock options as
remunerations for executives.
Second, for large investors there are scale advantages, not only with
respect to information but also with respect to leveraging. Investment
opportunities can be explored more extensively with greater access to,
and lower cost of, credit. Levering, and over-leveraging, up to a ratio of
roughly 30 to 1 (see Section 1.3) has become one of the most common
and well-known strategies to harvest large gains from traditional as well
as new financial instruments in the recent past.18 Yet, these gains are
often only temporarily harvested, as discussed in Section 1.3.
Third, one might reasonably assume that larger income will imply
lower consumption rates and higher saving rates. This will result in a
higher proportion of funds being reinvested with the fund. Numerous
studies in the literature have used this assumption, showing that the
wealth will be built up faster with higher saving ratios. The faster build-up

16
W. Semmler and R. Chappe
of wealth is an expected outcome of this strategy. There is lots of evidence
that higher income leads to higher saving rates.19
An important mechanism of faster accumulation of wealth works with
borrowing and lending schemes. As mentioned in the introduction,
Minsky (1986) has introduced the financing practices such as hedge
finance, speculative finance, and Ponzi finance. In recent times, in par-
ticular with the Madoff case, a Ponzi scheme has become a well-known
term to the public. In testifying in front of Congress, Frankel (2008)
mentions the following elements of the Ponzi scheme:
Ponzi schemes are simple. A con artist offers obligations that promise
very high returns at seemingly very low risk from a business that does
not in fact exist or a secret idea that does not work out. The con artist
helps himself to the investors’ money, and pays the promised high
return to earlier investors from the money handed over by these and
later investors. The scheme ends when there is no more money from
new investors. (Frankel 2008)
Ponzi schemes, by their very nature follow Ponzi financing. However,
Ponzi financing does not necessarily imply the existence of a Ponzi
scheme. Ponzi schemes are deceptive in nature, relying on fraudulent
misrepresentations, while Ponzi finance simply entails an inability, in
the long run, to sustain payments with operating cash flow. We are
interested to explore the possibility of funds adopting Ponzi financ-
ing. Let us explain how this works in terms of a dynamic model of
wealth accumulation. We can use a model with mean reversion in
returns where the expected returns move in the long run to some
mean. This is one of the most common assumptions in recent asset
return modeling (see Munk et al. 2004). Consumption is neglected
here. For a more complex extended version of the model, which incor-
porates stochastic consumption and portfolio choice and can only be
solved numerically with a dynamic programming algorithm, see the
Appendix.
1.4.2
The wealth-generating process
Let us first define the wealth-generating process. It starts with the investor
turning over funds to a hedge manager and paying a fee,20 ctWt, with
ct a percentage of the invested wealth, Wt. To explain the income and
wealth process we use, as stochastic processes, Brownian motions – a
process for wealth, a process of a mean-reverting asset returns and an
interest-rate process. Models with mean reversion in returns are now

The Operation of Hedge Funds
17
frequently used in the portfolio modeling literature. The simplified
dynamic model can be written as follows (see Munk et al. 2004 and
Wachter 2002):
dW = {[αt(rt + xt) + (1 −αt)rt]Wt −ctWt −rpWt}dt + σωWtdzt
(A.1)
dxt = λ(x −xt)dt + σxdzt
(A.2)
drt = k(θ −rt)dt + σrdzt
(A.3)
Hereby, rt, denotes the short term interest rate, αt, the fraction of
wealth invested in risky assets, xt is the premium on risky assets, x is an
expected mean of the premium, which is assumed to be constant. We
here have assumed a time-varying equity premium, following a mean
reversion process, as in Campbell and Viceira (1999). There is a stochastic
shock imposed on each dynamic equation. A similar model is used in
Campbell and Viceira (2002: Chapter 5), where, however, a constant
expected premium is used. Moreover, θ is the mean interest rate and λ
and κ are adjustment coefficients. They represent adjustment speeds of
the equity premium and interest rates toward the mean. Moreover, the
dzt are the increments in the Brownian motions, possibly different for
all three Brownian motions.
We can think of the wealth process of equation (A.1) as representing
(long) bonds, equity, real estate, options, or commodities which could be
managed by a hedge fund. In addition, some investment is undertaken
with a risk-free interest rate, rt. We then interpret the wealth as obtained
from accumulated assets, a fraction being invested in risky hedge-fund
assets, indicated by αt, and a fraction invested in a risk-free investment,
(1 −αt). Risk-free here means that the return is known over the holding
period. Thus, αt(rt + xt)Wt represents the expected return from risky
assets. On the other hand, the risk-free asset generates an expected return
of (1 −αt)rtWt. Moreover, rp is the return that the hedge fund promises
to pay the investor. We may assume, for example, that the hedge fund
attempts to attract investors by delivering high returns. Those promised
returns will have to be paid the next time period, at least on average, if
the hedge fund wants to be perceived as credible. This, however, means
that the hedge fund has actually borrowed at a rate rp.
Thus, in the long run, and on average, the wealth Wt of the hedge
fund grows if the positive returns on both the risky assets and the risky
free assets exceed the fee and the promised return rp. Yet, if mostly
the promised returns rp are set too high, on average the hedge fund

18
W. Semmler and R. Chappe
persistently needs positive inflow of fresh funds in order not to become
insolvent.
1.4.3
The hedge fund management
The hedge-fund manager can view the above equation in a different
way. As mentioned above, the hedge fund promises returns in order to
obtain an inflow of funds. If rp is set too high, the fund must persistently
achieve a higher return usual market return, rt + xt, which is the asset
return for risky assets (premium plus risk-free rate), in order to deliver the
promised return rp – or it must rely on a positive inflow of funds σ wWtdzt
to be able to survive. Thus, it must persistently attract investors to the
fund. But as mentioned above, this means that the promise to pay high
returns, to attract investors, turns into the actual payment to the existing
investors. The hedge fund thus has to pay the existing investors those
returns.
So, in fact, one can say that the hedge fund borrows funds from
investors (that guarantees returns for new investors) at a rate rp but
receives possibly only a smaller return, possibly in excess of rt, and below,
equal to, or above αt(rt + xt) + (1 −αt)rt. When, positive returns rt + xt
and rt are generated for the hedge fund, wealth rises for the investor on
average at the rate rt + xt. The value of the hedge fund can rise too as
long as the term in the Brownian motion σ wWtdzt is positive (or has an
expected mean greater than zero).
1.4.4
The collapse of the hedge fund
If indeed rp is set too high, when the inflow of new funds dries up and the
increment in Brownian motion σ wWtdzt on average becomes negative,
the hedge-fund wealth must necessarily decline, go to zero, and finally
turn negative. The latter results will hold when suddenly funds are with-
drawn. This actually happened since the middle of the year 2008. Figure
1.1 represents typical results of our simulations of equations (A.1)–(A.3).
Curve W (wealth) represents the evolution through time of the market
value of hedge-fund assets. Additional borrowing by the hedge fund from
capital markets can also come in.21 Curve D (debt) represents the evolu-
tion of hedge-fund borrowing over time. Figure 1.1 shows that although
the hedge fund starts positive, it will end up in insolvency. The higher the
promised returns are, the more likely it is that the hedge fund will become
insolvent. Depending on whether the fund is leveraged, insolvency will
come at different points in time. If the fund has borrowed from capital
markets, the fund is technically insolvent as soon as the market value of

The Operation of Hedge Funds
19
0.12
0.1
0.08
0.06
0.04
0.02
0
0
50
100
150
200
250
350
450
300
400
D
W
500
Figure 1.1
Simulation of the insolvency of the hedge fund
assets falls below the value of debt (where curve W intersects curve D). If
the fund has no leverage, insolvency happens when the market value of
assets falls close enough to zero that the fund cannot deliver promised
return rp.22 At this point, with no further borrowing available or no new
inflow of funds from new investors, original investors have lost their
initial investment as the market value of hedge-fund assets falls to zero.
The same results hold when there is a sudden decline of inflow of funds
or when large withdrawals occur. Finally, note that if hedge fund only
earns return at the rate of rt, or less, the bankruptcy will come earlier, as
in the Madoff case.
A recent article published in the Financial Times (Brewster 2008) evi-
denced that many investors in hedge funds had to withdraw funds
suddenly in the period of the financial market meltdown, 2008–2009.
This was due to other payment obligations, in order to make up for losses
somewhere else, or owing to forced deleveraging, making 2008 a record
year in its experience of such major redemptions. On the other hand, the
hedge funds have tried to impose “gates” against fast exits (for example,
some funds have split their assets into liquid and nonliquid baskets to
make it harder for investors to get money back immediately). The news
in the years 2008–2009 was full of those stories. If such a trend persists
continued withdrawals are likely to precipitate hedge-fund bankruptcies
and reveal the existence of Ponzi financing.

20
W. Semmler and R. Chappe
1.5
The regulatory context and implications
Having shown that promised high returns and use of leverage to generate
above-average returns can result in some hedge funds running a Ponzi
financing scheme, we turn to the regulatory context. The lack of regula-
tory reporting requirements facilitates such financing in that managers
have the ability to claim to deliver returns in excess of actual returns.
Further, as already described, the size of the hedge-fund industry raises
the question of whether a new form of systemic risk is present, with the
added issue that the risk profile of hedge funds is not fully understood.
A new set of risk analytics is required to develop more accurate quan-
titative measures of things such as performance, illiquidity exposure,
probability of the fund’s survival, and systemic risk. For this pur-
pose, transparency and access to information is critical. In his written
testimony to the U.S. House of Representatives, Andrew Lo (2008b)
emphasized that any attempt to understand and measure systemic risk
required greater transparency on the part of hedge funds, and he stressed
the need to develop a new regulatory framework to that effect:
The first order of business for designing new regulations is to develop
a formal definition of systemic risk and to construct specific mea-
sures that are sufficiently practical and encompassing to be used
by policymakers and the public. Such measures may require hedge
funds and other parts of the shadow banking system to provide
more transparency on a confidential basis to regulators, e.g., infor-
mation regarding their assets under management, leverage, liquidity,
counterparties, and holdings. (Lo 2008b: 2)
1.5.1
The hedge fund: definition and structure
There is no legal definition of a hedge fund. The term is absent from fed-
eral securities laws. As many as fourteen different definitions have been
identified in government and industry publications (Vaughan 2003). A
hedge fund can be thought of as a catch-all provision designating any
privately organized pooled investment vehicle administered by profes-
sional investment managers whose interests are not sold in a registered
public offering and which, as such, avoids registration under the Invest-
ment Company Act of 1940. The Dodd-Frank bill has now adopted this
catch-all approach (hedge funds are largely defined by what they are not)
and defines a hedge fund as any investment company that has avoided
regulation under the Investment Company Act of 1940.
Hedge funds are typically structured as limited partnerships, a legal
entity characterized by the presence of both general and limited partners,

The Operation of Hedge Funds
21
to achieve maximum separation of ownership and management. General
partners have the authority to legally bind the partnership. As opposed to
limited partners, general partners have joint and several liability for the
debts of the partnership. A general partner typically manages the fund
for a fixed fee (usually a percentage of assets under management) and
a percentage of the gross profits from the fund (the “carry” or “carried
interest”). The investors are limited partners with no managerial over-
sight. Investors might invest directly in the fund, or via another fund
called a feeder fund (itself an offshore or U.S. fund), thus resulting in a
layered structure that allows each investor to obtain the best possible tax
treatment while allowing the hedge-fund manager to keep all assets in a
single entity (the master fund).
1.5.2
Lack of regulatory oversight
The Investment Company Act is legislation passed by the U.S. Congress
dealing with the regulation of investment companies. It applies to any
fund that issues securities and “is or holds itself out as being engaged
primarily ... in the business of investing, reinvesting, or trading in secu-
rities.”23 Among other things, the Investment Company Act requires
registration with the Securities and Exchange Commission (SEC) and
sets reporting requirements to investors.
Unlike their mutual fund counterparts, most hedge funds fell out-
side the scope of the Investment Company Act by availing themselves
of applicable exemptions, such as having 100 or fewer beneficial own-
ers and not offering their securities in a public offering,24 or because
investors are all “qualified” high net-worth individuals or institutions.25
This explains why hedge funds have deliberately chosen not to raise
capital on public markets. Two recent examples of substantial private
initial offerings are that of Oaktree Capital Management LLC, which sold
approximately 14 percent of its equity for more than $800 million in May
2007, and Apollo Management LP, which privately raised $828 million
in August 2007. Both transactions listed equity securities on Goldman
Sachs & Co.’s nonpublic market, the GS Tradable Unregistered Equity
OTC Market (GSTRuE).26
Hedge-fund advisers have also been exempt from regulation under the
Investment Advisers Act of 1940.27 The Investment Advisers Act is a
companion statute to the Investment Company Act and was primar-
ily designed to introduce record keeping and antifraud standards to the
investment advisory profession. Under the Act, investment advisers must
register with the SEC. An investment adviser is someone who, for com-
pensation, engages in the business of advising others about the value of

22
W. Semmler and R. Chappe
securities or the advisability of investing in, purchasing, or selling secu-
rities.28 The SEC has authority to conduct audits and to examine the
records of investment advisers.29
Hedge-fund managers have been typically exempt from registration
under the private adviser exemption, whereby any investment adviser is
exempt from registration who during the course of 12 months (1) has
had fewer than fifteen clients and (2) neither holds himself out generally
to the public as an investment adviser nor acts as an investment adviser
to any investment company registered under the Investment Company
Act.30 For this purpose, only the hedge fund itself (as opposed to the
investors in the fund) is considered to be a client of the hedge-fund man-
ager. The rationale is that a hedge-fund manager will typically manage
the assets of the fund on the basis of collective investment objectives
rather than individual investors’ financial goals and profiles. Because
investors do not directly receive customized advice, it appears appro-
priate to view the fund itself rather than each investor as a client of
the manager. Because of this technical point, most hedge-fund man-
agers have been exempt from registration, because hedge-fund managers
usually run fewer than fifteen hedge funds.
1.5.3
The SEC’s attempt to impose mandatory registration
Concerned with the growth of the industry, and with the increased
exposure of ordinary investors to such funds, the SEC sought to estab-
lish greater transparency through mandatory registration of hedge-fund
advisers under the Advisers Act, taking the position that one can look
through to the investors in the fund as clients of the adviser for the
purposes of the private adviser exemption.31 Under this interpretation,
most hedge-fund managers would have had more than fifteen clients
and would have had to register by February 1, 2006.
The expectation was that through registration the SEC would be able
to gather “basic information about hedge fund advisers and the hedge
fund industry,” as well as “oversee hedge fund advisers,” and “deter or
detect fraud by unregistered hedge fund advisers.”32 Under this pro-
posal, advisers would have had to adopt record-keeping procedures
subject to periodic audits by the SEC and to supply information (financial
statements) to investors concerning their results of operations.
Challenged by a hedge-fund manager, the SEC was eventually struck
down for lack of statutory grounding by a DC circuit decision on June 23,
2006.33 The decision rejected the SEC’s interpretation of the word
“client” as establishing a direct client relationship between investors
and hedge-fund managers that would have been inconsistent with the

The Operation of Hedge Funds
23
Advisers Act as a whole. The Court also highlighted that regulating
investment companies on the basis of the number of investors would
appear somewhat misaligned with the SEC’s proclaimed concern with
the national scale of the fund’s activities. Reliance on some financial
metric, such as the volume of assets under management, or the level
of leverage, would seem more appropriate. This required comprehen-
sive new legislation rather than twisted interpretation of the existing
statutes.
1.5.4
Consequences of lack of regulatory oversight
One consequence of the lack of regulatory oversight has been that hedge
funds could participate in highly complex financial transactions inacces-
sible to other regulated market participants, thus furthering the growth
of the industry and exacerbating the potential for systemic risk. Another
consequence was that hedge funds typically remained secretive about
their positions and strategies, even to their own investors, asserting the
proprietary nature of trading techniques and algorithms.
Even though they were not obligated to, some hedge-fund managers
did voluntarily register with the SEC so as to give the market a higher
level of confidence and potentially to minimize the amount of due dili-
gence performed by new investors. It turns out that Madoff himself had
registered with the SEC in September 2006. One issue is that the SEC
may not have the resources needed to examine investment advisers on
a regular basis. If so, mandatory registration could lull investors into
a false sense of security. Madoff himself avoided attracting scrutiny in
spite of repeated letters to the SEC accusing him of running a large Ponzi
scheme. The SEC did not pay specific attention to the basic fact that
the fund relied on a small auditing firm with no other large clients and
no reputation on Wall Street. The SEC has tended to focus on funds
with high-risk profiles and high-risk trading strategies. Madoff avoided
drawing attention by supposedly engaging in plain-vanilla trading.
The issue is that in the absence of detailed financial statements and
the full disclosure of detailed trading strategies, there is typically not
enough information to allow investors to conduct basic due diligence
regarding the performance of funds. The lack of a regulatory framework
facilitated the ability for managers to claim to deliver returns in excess
of actual returns, in that there is no transparency regarding the fund’s
financials. One rationale for limited regulatory oversight of the hedge-
fund industry has traditionally been that high-stakes investors should be
capable of protecting themselves. However, this is untenable given the

24
W. Semmler and R. Chappe
trend toward retailization, the involvement of institutional investors,
and the potential contribution to systemic risk.
1.5.5
Guiding principles for regulatory reform
Today, in the context of the current financial crisis, in a post-Enron,
post-Worldcom, post-Madoff world, the trust in financial markets has
been severely damaged. There is no reason to believe that private-sector
actors such as lawyers, accountants, internal-risk managers, and external
rating agencies can on their own ensure the reliability of the system and
well-functioning markets. There are two distinct goals of financial regu-
lation. One goal is to maintain market integrity and to protect investors
from fraud. The other is to monitor systemic risk and to preserve the
stability of the financial system. Ponzi schemes of the magnitude of the
recent Madoff scandal have implications for both.
To elaborate on that point, hedge-fund failures can contribute to
destabilize the economy and the financial sector because of the size
of the industry and the potential liquidation and unloading of posi-
tions, which may contribute to creating and accelerating downward
price spiral. Kundro and Feffer (2008) and Christory et al. (2008) have
shown that a majority of hedge-fund failures occur because of oper-
ational issues or/and fraud (such as misappropriation of funds, false
valuations, and Ponzi schemes), rather than unsuccessful investment
strategy.
Both adequate protection against fraud and regulation of systemic risk
require that the regulator have access to better financial information.
Every financial firm of a significant size should be disclosing timely finan-
cials (balance sheets and profit-and-loss statements). Specifically, with
respect to hedge funds, transparency regarding valuation policies, per-
formance attributes, portfolio exposures, and risk metrics, and limited
disclosure of positions has also been suggested (Mertzger 2008). For this
purpose, new inspection systems need to be developed for the regulator
to be able to process this vast quantity of information.
One issue is whether there should be different regulators for protec-
tion against fraud and guaranteeing the stability of the financial system.
The general consensus is that the Fed is more inclined to monitor
systemic risk, whereas the SEC has traditionally been focused on pro-
viding investors with accurate financial information and the prevention
of fraud so as to protect investors. In some jurisdictions, in the U.K.
for example, there is a unique regulator for the entire financial services
industry, the Financial Services Authority (FSA). A single regulator may
be in a better position to address both fraud and systemic risk concerns

The Operation of Hedge Funds
25
more efficiently. Either way, all reported financial information should be
consolidated for the purpose of monitoring systemic risk.
The regulatory framework had been focused on form over substance
and had not kept up with the development of markets and sophistica-
tion of new products that have contributed to blurring the traditional
roles of firms in the financial sector. If hedge funds are performing bank-
ing functions (e.g., extending loans to troubled companies), they should
be regulated as such. If banks are operating like hedge funds (e.g., mer-
chant banking and proprietary trading), or have hedge funds as operating
branches, those activities should be subject to banking regulation as
well. It is inconceivable that the asset-management operations of Bear
Stearns were left essentially unregulated, with no strict requirements for
transparency, to ultimately bring the firm down.
1.5.6
Proposals under the Obama administration
The Obama administration has recently passed the Dodd-Frank Act, a
major legislation designed to reform the financial sector and prevent
future bailouts. The Dodd-Frank Act passed the House of Representa-
tives on June 30, 2010, and was approved by the Senate on July 15,
2010. There are now registration requirements for investment advis-
ers to private funds with assets under management of $150 million or
more. Hedge funds will now have to register with the SEC and disclose
assets under management, use of leverage (including off- balance sheet
leverage), counterparty credit risk exposures, trading practices, valua-
tion policies, types of assets held, and side arrangements or side letters
(whereby certain investors in a fund obtain more favorable rights or enti-
tlements than other investors). Hedge funds will also have to have assets
audited by public accountants. Finally, the Act also specifically contem-
plates that the SEC be empowered to collect systemic risk data, reports,
examinations and disclosures. The SEC would make this information
available to the Financial Services Oversight Council, a newly created
Council designed to look after the stability of the financial system as a
whole.
The Act also significantly restricts proprietary operations undertaken
by commercial banks (provision known as the Volcker rule). Banks can
place up to 3 percent of their Tier 1 capital in hedge fund and proprietary
trading investments. The other aspect of the rule is that banks are prohib-
ited from holding more than 3 percent of the total ownership interest
of any private equity investment or hedge fund. This falls short of a
complete disallowance of proprietary desks, which had been originally
suggested and would have been equivalent to restoring Glass-Steagall.

26
W. Semmler and R. Chappe
1.5.7
Proposals in the European Union
While systemic risk is cross-border in nature, in the European Union (EU)
regulatory oversight is still currently largely national. Data reporting is
voluntary and incomplete, and there is currently no mechanism for shar-
ing the information between regulators of member countries. Aware of
this issue, the European Commission has proposed a hedge-fund direc-
tive, the Directive on Alternative Investment Fund Managers that would
create a comprehensive regulatory and supervisory framework for hedge
funds at the European level. The proposed directive will provide har-
monized regulatory standards for all hedge funds (above a threshold of
D 100 million of assets) and managers. These should include minimum
standards in relation to governance, ongoing capital requirements, and
processes, as well as enhanced transparency requirements for supervisors
and the general public. More specifically, some of the key requirements
the directive provides for include
1. valuation of fund assets to be undertaken by an independent
appraiser;
2. an annual report to be made available to investors and the regulator
with audited balance sheet and income and expenditure account, as
well as a report on the activities of the financial year;
3. disclosure of uses and sources of leverage (to be aggregated and shared
with other regulators in the EU), as well as limits to the maximum
amount of leverage;
4. disclosure of investment strategies and objectives of the fund;
5. description of the fund’s liquidity risk management;
6. disclosure of dominant or controlling interests in listed or non-listed
companies.
Regulators are invited to communicate information to regulators of other
member states where this is relevant for monitoring systemic risk. Fur-
ther, aggregated information relating to the fund activities are to be
communicated on a quarterly basis by each regulator to the Economic
and Financial Committee for the Council of the European Union.
1.6
Conclusion
This chapter has shown a model that can be used to describe situations in
asset management where the use of leverage and the promise of above-
average returns to investors can result in some hedge funds following a
pattern of Ponzi financing. Unlike in a pure Ponzi scheme, this situation

The Operation of Hedge Funds
27
could develop inadvertently without necessarily involving fraudulent
misrepresentation. The illiquidity of some positions, the computation of
the most accurate mark of a security under mark-to-market accounting
rules, for example, might lead to a declared return that in the end exceeds
actual return. This issue is further accentuated when there are biases
in the data and a lack of transparency regarding valuation policies and
leverage. Given that hedge funds are investing in every kind of assets, and
that the size of assets under management has exploded in the past ten
years, this situation carries systemic risk that is not properly understood
nor measured. In that respect, the new regulatory framework developed
by the Obama administration is a welcome development.
One main challenge, going forward, is the measuring and monitor-
ing of systemic risk. The data-gathering effort proposed by the Obama
Administration would allow the regulator to consider the financial
system as a whole, potentially aggregating the information across insti-
tutions to develop systemic scenario analyses. However, regardless of
which regulatory agency is in charge on monitoring systemic risk (for
example, a new entity such as the Financial Services Oversight Council),
some key issues will include the ability to streamline the collection of a
comprehensive consolidated systemic-risk database and to develop new
formal measures of systemic risk.
Appendix: A stochastic dynamic model with preferences
The background of the stochastic dynamic model of wealth accumula-
tion by a hedge fund in Section 1.4 is an intertemporal decision model
with preferences that allows for consumption choice. In the model, we
have modeled the payoffs ctWt and rpWt as well as the fraction allocated
to risky assets, as determined by some law of motion depending on time.
Yet the payoffs as well as the fraction allocated to risky assets can be deter-
mined by an intertemporal decision model. In doing so, we use, as in
Section 1.4, a model with mean reversion in returns where the expected
returns move in the long run to some mean. This is one of the most com-
mon assumptions in recent asset return modeling (see Munk et al. 2004).
We want to discuss here a stochastic consumption and portfolio choice
model with preferences which has two choice variables and three state
variables. The basics of such model are analytically treated in Semmler
(2006: Chapter 16). The herein presented extended version, as compared
to the model in Section 1.4, also needs to be solved numerically, yet by a
dynamic programming algorithm. As state equations, we again can use
three Brownian motions as stochastic processes, a process for wealth,

28
W. Semmler and R. Chappe
a mean-reverting interest-rate process, and an equity premium process.
This model explores consumption and portfolio choices at each point of
the state space. We hereby can obtain the decision variables. To avoid a
third state equation one could presume a constant expected equity pre-
mium as in Campbell and Viceira (2002: Chapter 3), see also Semmler
(2006), Munk et al. (2004), and Wachter (2002). Next, let us introduce
the full dynamic model, which can be written for power utility as:
max
α,C
 ∞
0
e−δt (ctWt)1−γ
1 −γ
dt
(A.4)
s.t.
dW = {[αt(rt + xt) + (1 −αt)rt]Wt −ctWt −rpWt}dt + σωWtdzt
(A.5)
dxt = λ(x −xt)dt + σxdzt
(A.6)
drt = κ(θ −rt)dt + σrdzt
(A.7)
Hereby, Wt denotes total wealth, rt, the short term interest rate, αt,
the fraction of wealth held as equity, xt, the equity premium, and xt, an
expected mean equity premium which we assume to be a constant (with
a stochastic shock imposed on it). The parameter θ is the mean interest
rate, λ and κ are adjustment coefficients, and dzt the increment in Brow-
nian motion. The terms ctWt and rpWt represent the payoffs for con-
sumption and guaranteed returns. Such a model can be solved through
dynamic programming (see Semmler 2006). Section 1.4 has introduced
and solved a simplified version of this model without choice variables.
Acknowledgments
This chapter was presented at the International Business and Economy
Conference (IBEC) 2010 and awarded the Best Finance Paper Award. This
chapter was also presented at the Eastern Economic Association 36th
Annual Conference.
Notes
1. Illiquidity exposure can induce serially correlated returns to the extent that
mark-to-market accounting requires that a market value be assigned to
portfolio securities, even when there is no active market and comparable
transactions as is the case for illiquid investments. There is some discretion
on the part of the hedge-fund manager to compute the most accurate mark
for the security. Returns calculated on the basis of such computations typi-
cally exhibit lower volatility and higher serial correlation than true economic

The Operation of Hedge Funds
29
returns. There is the issue of “smoothed” returns, where, for example, a hedge-
fund manager might obtain different quotes for a given illiquid security from
different broker-dealers, and pick a linear average as the most accurate mark,
thereby minimizing volatility. There is the issue of serial correlation if the
broker-dealers do not frequently update their quotes, as is likely when there
is a low trading volume. Another source of serial correlation is performance
smoothing, where hedge-fund managers deliberately fail to report a portion
of gains in profitable months to offset potential future losses.
2. This led to major regulatory overhaul designed to restore confidence in capital
markets, to promote the disclosure of important market-related information,
and to protect investors against fraud. The Securities Act of 1933 was the first
major legislation to regulate the new issue of securities to the general public
and to protect investors against fraud. The Securities Exchange Act of 1934,
designed to regulate secondary markets, created the Securities and Exchange
Commission and required ongoing disclosure for publicly traded securities.
3. Hedge Fund Intelligence March 2009.
4. HFR Global Hedge Fund Industry Report, Fourth Quarter, 2008.
5. HFR Global Hedge Fund Industry Report, Fourth Quarter 2008.
6. Deutsche Bank, 2010 Alternative Investment Survey.
7. As per the Bureau of Economic Analysis, U.S. GDP was $8.793 trillion in 1998
and $14.441 trillion in 2008.
8. This has been described as having option-like features in that the manager
has an incentive for volatility in returns (Cochrane 2005).
9. Using the TASS database.
10. On the basis of HFR industry report through 2008, Q3, and Credit Suisse for
2008, Q4, projections, Lo (2008b) estimated $1.6 trillion of net assets and
$3.7 trillion of total market positions at the end of 2008.
11. The firm’s equity had grown to $3.6 billion while assets had grown to $102
billion at the end of 1995. See Lowenstein (2001) p78.
12. See Lowenstein (2001) p26: from the very start, it was always contemplated
that Long Term Capital Management would be heavily leveraged, twenty to
thirty times of capital or more, in order to make a decent profit on very tiny
spreads.
13. John Paulson’s verbal testimony to the U.S. House of Representatives, Com-
mittee on Oversight and Government Reform, November 13, 2008 Hearing
on Hedge Funds.
14. UBS Hedge Fund Report (February 2009).
15. The participants in the survey are investors in hedge funds that collectively
manage more than $1.1 trillion in hedge-fund assets.
16. See to that effect Philip Falcone’s verbal testimony to the US House of Rep-
resentatives, Committee on Oversight and Government Reform, November
13, 2008, Hearing on Hedge Funds.
17. Information flux could include insider information obtained through infor-
mal networks, as the recent case of the Galleon Group may demonstrate. The
FBI arrested the founder of this hedge fund on allegations of insider trading.
18. There is the well-known Paradox pointing to those scale effects: “The people
who most need the money are worst credits risks and thus cannot get a loan,
whereas people who least need the money are best credit risks and thus once
again the rich get richer” (Tooby and Leda 1996).

30
W. Semmler and R. Chappe
19. Early contributions include Fisher 1930; Keynes 1936; Vickrey 1947; Duesen-
berry 1949; Hicks 1950; Pigou 1951; Friedman 1957; Friend and Kravis 1957;
and Modigliani and Ando 1960. For more recent work, see for example Saltz
1999; Dynan et al. 2004; and Chakrabarty et al. 2008.
20. Typically between 1% and 2% of assets under management. Performance-
based fees can be up to 20% of returns.
21. Indeed, we have seen in Section 1.3 that hedge funds use leverage, albeit
in more limited proportions than banks. Prior to the current financial crisis,
around 70 percent of hedge funds were levered less than 2 to 1. At the end of
2008, on average, the hedge-fund industry had a 1-to-1 debt-to-equity ratio.
But there are great differences in leverage ratios between funds, sometimes
going up to 30 to 1.
22. We use the term “insolvency” rather loosely in that technically the fund is
not insolvent simply because it cannot deliver promised returns to investors.
However, as we have discussed, if the hedge fund wants to be perceived as
credible, on average it is committed to delivering rp to investors. In essence,
in terms of understanding long-term sustainability of the fund, this can be
interpreted as the hedge fund having borrowed at a rate of rp.
23. 15 USC ß 80a-3 (a) (1) (A).
24. 15 USC ß 80a-3(c)(1).
25. 15 USC ß 80a-3(c) (7).
26. Apollo subsequently announced it would transfer the securities to the New
York Stock Exchange. It has been suggested that Apollo’s GSTRuE offering
may therefore have been a transitory step designed to save time initially and
to delay the time-consuming registration process until after capital had been
raised (Davidoff 2008).
27. 15 USC ß 80b-1.
28. 15 USC ß 80b-2 (11).
29. 15 USC ß 80b-4.
30. 15 USC ß 80b-3 (b) (3).
31. See Rule 203 (b) (3)–2 under the Investment Advisers Act, 17 CFR ß 275.203
(b) (3)–2.
32. Id.
33. Goldstein v. SEC, 451 F.3d 873 (DC Cir. 2006). Interestingly enough, the Fed
was opposed to this mandatory registration proposal. The SEC subsequently
tightened restrictions on investors who could invest in both hedge funds
and private-equity funds (investors must have owned at least $2.5 million
in investments). This measure failed to address systemic risk and was only
concerned with individual risk to investors.
References
Adrian, T., and Shin, H. S. (2008) “Liquidity, Financial Cycles and Monetary Policy:
Current Issues and Economics and Finance,” Federal Reserve Bank of New York,
14 (1).
Agarwal, V. and Naik, N. (2000) “On Taking the ‘Alternative’ Route: The Risks,
Rewards, and Performance of Persistence of Hedge Funds,” Journal of Alternative
Investments, 2 (2): 6–23.

The Operation of Hedge Funds
31
Amin, G. and Kat, H. (2003) “Stocks, Bonds and Hedge Funds: Not a Free Lunch!”
Journal of Portfolio Management, 29 (4): 113–118.
Brewster, D. (2008) “Money Flows Out of Hedge Funds at Record Rate,” Financial
Times, December 30.
Brooks, C. and Kat, H. (2002) “The Statistical Properties of Hedge Fund Index
Returns and Their Implications for Investors,” Journal of Alternative Investments,
5 (3): 26–44.
Brunnermeier, M. and Nagel, S. (2004) “Hedge Funds and the Technology Bubble,”
The Journal of Finance, 59 (5): 2013–2040.
Brunnermeier, M and Pedersen, L. (2009) “Market Liquidity and Funding Liquid-
ity,” Review of Financial Studies, 22 (6): 2201–2238.
Brunnermeier, M. and Sannikov, Y. (2009) “A Macroeconomic Model with a
Financial Sector,” Working Paper, Princeton University, Princeton, NJ.
Bernardo, A. E. and Ledoit, O. (2000) “Gain, Loss, and Asset Pricing,” Journal of
Political Economy, 108 (1): 144–172.
Cagetti, M. and De Nardi, M. (2006) “Entrepreneurship, Frictions, and Wealth,”
Journal of Political Economy, 114 (5): 835–870.
Campbell, J. and Viceira, L. (1999) “Consumption and Portfolio Decisions When
Expected Returns Are Time Varying,” The Quarterly Journal of Economics, 114
(2): 433–495.
Campbell, J. and Viceira, L. (2002) Strategic Asset Allocation, Oxford: Oxford
University Press.
Chakrabarty, H., Katayama, H. and Maslen, H. (2008) “Why Do the Rich Save
More? A Theory and Australian Evidence,” Economic Record, Supplement, 84:
S32–S44.
Chan, N., Getmansky, M., Haas, S., and Lo, A. (2006) “Do Hedge Funds Increase
Systemic Risk?” Economic Review, 91 (4): 49–80.
Chen, Z. W. and Knez, P. J. (1996) “Portfolio Performance Measurement: Theory
and Evidence,” Review of Financial Studies, 9 (2): 551–556.
Chiarella C., Hsiao, C. and Semmler, W. (2007) “Intertemporal Investment Strate-
gies under Inflation Risk,” Research Paper Series 192, Quantitative Finance
Research Centre, University of Technology, Sydney.
Christory C., Daul, S. and Giraud, J. R. (2006) “Quantification of Hedge Fund
Default Risk,” The Journal of Alternative Investments, 9 (2): 71–86.
Cochrane, J. (1999) “New Facts in Finance,” Economic Perspectives, 23 (3):
36–58.
Cochrane,
J.
(2005)
“Betas,
Options,
and
Portfolios
of
Hedge
Funds,”
available online at http://www.slidefinder.net/B/Betas_Options_ Portfolios_
Hedge_Funds/2799231 (accessed September 18, 2009).
Davidoff, S. (2008) “Paradigm Shift: Federal Securities Regulation in The New
Millennium,” Brook. J. Corp. Fin. & Com. L. 339 (367).
Drehmann, M. (2007) “Discussion on Banks, Markets and Liquidity by F. Allen
and E. Carletti,” in C. Kent and J. Lawson, The Structure and Resilience of
the Financial System, Reserve Bank of Australia RBA Annual Conference Vol-
ume 2007, available at http://ideas.repec.org/s/rba/rbaacv.html (accessed on
September 18, 2010).
Drehmann, M. and Nikolaou, K. (2009) “Funding Liquidity Risk: Definition
and Measurement,”
ECB Working Paper No.
1024.
Available online at
http://ssrn.com/abstract=1338092 (accessed September 18, 2010).

32
W. Semmler and R. Chappe
Duesenberry, J. (1949) Income, Saving, and the Theory of Consumer Behavior,
Cambridge, Mass.: Harvard University Press.
Dynan, K., Skinner, J., and Zeldes, S. (2004) “Do The Rich Save More?” Journal of
Political Economy, 112 (2): 397–444.
Fisher, I. (1930) The Theory of Interest, New York: Macmillan.
Frankel, T. (2009) Statement before the Committee on Financial Services of the
US House of Representatives, Washington, DC, January 5.
Friedman, M. (1953) “Choice, Chance, and the Personal Distribution of Income,”
Journal of Political Economy, 42 (4): 277–290.
Friend, I. and Kravis, I. B. (1957) “Consumption Patterns and Permanent Income,”
American Economic Review, 47 (2): 536–555.
Fung, W. and Hsieh, D. (2000) “Performance Characteristics of Hedge Funds and
CTA Funds: Natural versus Spurious Biases,” Journal of Quantitative and Financial
Analysis, 35 (3): 291–307.
Getmansky, M., Lo, A. and Makarov, I. (2004) “An Econometric Model of
Serial Correlation and Illiquidity in Hedge Fund Returns,” Journal of Financial
Economics, 74 (3): 529–609.
Gilli, M., Schumann, E., Cabej, G., and Lula, J. (2010) “Replicating Hedge
Fund Indices with Optimization Heuristics,” May 6. Available online at
http://ssrn.com/abstract=1601708 (accessed September 18, 2010).
Goetzmann, W. and Ross, S. (2000) “Hedge Funds: Theory and Performance,” Yale
School of Management Working Paper No. F-52B, New Haven, Conn.
Goetzmann, W., Ingersoll, J., Spiegel, M., and Welch, I. (2003) “Sharpening Sharpe
Ratios,” Financial Planning, 33 (1): 49–58.
Griffin, K. (2008) “Testimony to the House Committee on Oversight and Gov-
ernment Reform,” Prepared for the US House of Representatives, Committee
on Oversight and Government Reform, Hearing on Hedge Funds, Washington,
DC, November 13.
Heidorn, T., Kaiser, D. and Roder, C. (2009) “Performance Measurement of
Hedge Funds Portfolios in a Downside Risk Framework,” The Journal of Wealth
Management, 12 (2): 101–112.
Hicks, J. R. (1950) A Contribution to the Theory of the Trade Cycle, London: Oxford
University Press.
Ibbotson, R. and Cheng, P. (2005) “Sources of Hedge Fund Returns: Alphas, Betas,
and Costs,” Yale ICF Working Paper No. 05–17, New Haven, Conn.
Keynes, J. M. (1936) The General Theory of Employment, Interest, and Money, New
York: Harcourt, Brace.
Kundro, C. and Feffer, S. (2003) “Hedge Funds Fail Due to Operational Risk,”
study by Capco, abstract available at http://www.edge-fund.com/Capco03.pdf
(accessed September 18, 2010).
Lo, A. (2001) “Risk Management for Hedge Funds: Introduction and Overview,”
Financial Analysts Journal, 57 (6): 16–33.
Lo, A. (2002) “The Statistics of Sharpe Ratios,” Financial Analysts Journal, 58 (4):
36–52.
Lo, A. (2005) “The Dynamics of the Hedge Fund Industry,” CFA Digest, 35 (4):
87–90.
Lo, A. (2008a) “Where Do Alphas Come From? A New Measure of the Value of
Active Investment Management,” Journal of Investment Management, 6 (3): 6–34.

The Operation of Hedge Funds
33
Lo, A. (2008b) “Hedge Funds, Systemic Risk, and the Financial Crisis of 2007,”
written testimony prepared for the U.S. House of Representatives, Committee
on Oversight and Government Reform, Hearing on Hedge Funds, Washington,
DC, November 13.
Lowenstein, R. (2001) When Genius Failed: The Rise and Fall of Long-Term Capital
Management, New York: Random House.
Malkiel, B. and Saha, A. (2004) “Hedge Funds: Risk and Return,” Princeton
University Working Paper, Princeton, NJ.
Mamoghli, C. and Daboussi, S. (2009) “Performance Measurement of Hedge Funds
Portfolios in a Downside Risk Framework,” The Journal of Wealth Management,
12 (2): 101–112.
Minsky, H. (1986) Stabilizing an Unstable Economy, New Haven, Conn.: Yale
University Press.
Modigliani, F. and Ando, A. (1960) “The ‘Permanent Income’ and ‘Life Cycle’
Hypothesis of Saving Behavior: Comparison and Tests,” in Irwin Friend and
Robert Jones (eds.), Consumption and Saving, Philadelphia, Pa.: University of
Pennsylvania, vol. II, pp. 49–174.
Munk, C., Sørensen, C., and Nygaard Vinther, T. (2004) “Dynamic Asset
Allocation under Mean-Reverting Returns, Stochastic Interest Rates and Infla-
tion Uncertainty: Are Popular Recommendations Consistent with Rational
Behavior?” International Review of Economics and Finance, 13 (2): 141–166.
Pigou, A. C. (1951) “Professor Duesenberry on Income and Savings,” Economic
Journal, 61 (244): 883–885.
Platen, E. and Semmler, W. (2009) “Asset Markets and Monetary Policy,” Research
Paper Series 247, Quantitative Finance Research Centre, University of Technol-
ogy, Sydney.
Posthuma, N. and Van der Sluis, P. (2003) “A Reality Check on Hedge Fund
Returns,” Free University Amsterdam.
Ruder, D. (2008) “Testimony to the House Committee on Oversight and Govern-
ment Reform,” prepared for the U.S. House of Representatives, Committee on
Oversight and Government Reform, Hearing on Hedge Funds, Washington,
DC, November 13.
Saltz, I. (1999) “An Examination of the Causal Relationship between Savings and
Growth in the Third World,” Journal of Economics and Finance, 23 (1): 90.
Semmler, W. (2006) Asset Prices, Booms, and Recessions, Heidelberg and New York:
Springer.
Sharpe, W. (1994) “The Sharpe Ratio,” Journal of Portfolio Management, 21 (1):
49–58.
Sortino, F., and Price, L. (1994) “Performance Measurement in a Downside Risk
Framework,” Journal of Investing, 3 (3): 59–64.
Tooby, J. and Cosmides, L. (1996) “Friendship and the Banker’s Paradox: Other
Pathways to the Evolution of Adaptations for Altruism,” Proceedings of the British
Academy, 8 (2): 119–143.
Vaughan, D. (2003) “SEC Roundtable on Hedge Funds,” May 13, comments avail-
able online at http://www.sec.gov/spotlight/hedgefunds/hedge-vaughn.htm
(accessed September 18, 2010).
Vickrey, W. (1947) “Resource Distribution Patterns and the Classification of
Families,” Studies in Income and Wealth, NBER, Volume 10.

34
W. Semmler and R. Chappe
Wachter, J. (2002) “Portfolio and Consumption Decisions under Mean-Reverting
Returns: An Exact Solution for Complete Markets,” Journal of Financial and
Quantitative Analysis, 37 (1): 63–91.
Xiong, J. (2009) “Impact of Size and Flows on Performance for Funds of Hedge
Funds,” Journal of Portfolio Management, 35 (2): 120–130.

2
Inferring Risk-Averse Probability
Distributions from Option Prices
Using Implied Binomial Trees
Tom Arnold, Timothy Falcon Crack, and Adam Schwartz
2.1
Introduction
We generalize the Rubinstein (1994) risk-neutral implied binomial tree
(R-IBT) model to a physical-world risk-averse implied binomial tree
(RA-IBT) model. The R-IBT and RA-IBT trees are bound together via a
relationship requiring a risk premium (or a risk-adjusted discount rate)
on the underlying asset at any node. The RA-IBT provides a powerful
numerical platform for many empirical financial option and real option
applications; these include probabilistic inference, pricing, and utility
theory applications.
For ease of exposition, we have estimated a constant risk premium1 RA-
IBT using Standard & Poor’s 500 index options. In our implied tree, this is
consistent with assuming a representative agent with a power-like utility
function where the constant relative risk aversion (CRRA) parameter is
allowed to vary across states and through time. With these assumptions,
we estimate the pricing kernel (marginal rate of substitution) and implied
relative risk aversion (RRA) of our agent and compare and contrast our
results with other authors’ findings. Other empirical applications can be
found in Arnold et al. (2009).
2.2
Motivation and literature review
2.2.1
Motivation/introduction of risk-averse trees
The traditional binomial tree model of Cox, Ross, and Rubinstein
(CRR) (1979) is very powerful, but it is constrained in many respects.
The CRR model cannot, for example, reproduce some well-known
35

36
T. Arnold, T. F. Crack, and A. Schwartz
empirical results (e.g., fat tails, skewness, volatility smiles, etc.), and any
probabilistic inferences from a CRR tree must be risk-neutral inferences
not risk-averse probability inferences from the physical economy.
The Rubinstein (1994) implied binomial tree (R-IBT) generalizes the
CRR model to fit the prices of a series of traded options of the same matu-
rity. The R-IBT allows significant deviations from lognormality of prices
(and from normality of continuously compounded returns), allows the
up-jump probability to vary throughout the tree, and allows the local
volatility structure to vary throughout the tree. The R-IBT model is still
constrained, however, in that the probability structure is risk-neutral;
and, therefore, like the CRR model, it does not allow probabilistic
inferences about the physical economy.
In this chapter, we begin with a generalization of the risk-neutral CRR
model to a risk-averse binomial tree (RA-BT). We then present a general-
ization of the risk-averse RA-BT to a risk-averse implied binomial tree
(RA-IBT). Like the R-IBT model, the RA-IBT model captures volatility
smiles and varying local volatility. It should be noted, however, that
both the RA-BT and the RA-IBT have one extra input compared with the
CRR and R-IBT models: The risk-averse trees need to be supplied with
a risk premium (or a risk-adjusted discount rate) at every node to make
them estimable. This risk premium feeds into a relationship that drives
a transformation from the risk-neutral trees to the risk-averse trees.
For empirical ease, we impose a constant risk premium in the RA-
IBT estimations in this chapter. Whether the risk premium is imposed
directly, or derived from utility assumptions for a representative agent, to
each such risk premium function over the nodes of an RA-IBT there cor-
responds a different implied risk-averse probability distribution for the
future prices of the underlying asset; this, in turn, implies a unique, fully
specified stochastic process for the underlying asset prices. Sensitivity
analysis is thus essential for any inferences.
The CRR, RA-BT, R-IBT, and RA-IBT models can each be used to value
and hedge both European-style and American-style options. Neither the
R-IBT model nor the RA-IBT model (under the conditions we develop in
this chapter) can be calibrated using American-style options.
2.2.2
Literature review
Rubinstein (1994: 793, footnote 25) describes implied trees developed by
Hayne Leland (1980) that use “subjective probabilities” (i.e., an individ-
ual investor’s non-risk-neutral probabilities). Stutzer (1996) also infers
“subjective” (i.e., risk-averse) probability densities from options data.
Stutzer differs from us, however, in that he uses diffusions rather than
binomial trees, he requires historical data that are not needed here, and

Inferring Risk-Averse Probability Distributions
37
he uses the risk-averse density to estimate the risk-neutral density for
risk-neutral pricing (the focus of his paper), whereas our focus is the
risk-averse density itself.
Jackwerth and Rubinstein (1996) infer probabilities from option prices
using binomial trees. However, Jackwerth and Rubinstein differ from us
because they use risk-neutral probabilities, whereas we use risk-averse
probabilities. We do though use their “smooth” objective function in
estimating our R-IBT.
Jackwerth (2000) recovers risk-neutral densities from S&P 500 options
and uses historical realized index returns to approximate subjective (i.e.,
risk-averse) densities. Jackwerth is thus able to infer aggregate absolute
risk-aversion functions for different states. When comparing pre- and
post-Crash of 1987 data, changes in the implied risk-neutral densities
that are not accompanied by changes in the risk-averse densities imply
changes in absolute risk-aversion functions that appear inconsistent with
any sensible economic theory (e.g., Jackwerth finds significantly negative
absolute risk aversion). Jackwerth suggests that overpriced put options
may explain the inconsistency, and he is able to construct profitable
trading strategies that appear to exploit this potential mispricing. Jack-
werth (1999) acknowledges that another explanation for inconsistent
risk-aversion functions is that his risk-averse distributions built using his-
torical observations may differ from true ex-ante risk-averse distributions
(Jackwerth 1999: 445–446). However, he rejects this as an explanation
because his trading strategies appear profitable (supporting the hypothe-
sis that his inconsistent risk-aversion functions are driven by exploitable
mispriced options, not by poor estimates of subjective probability). In
contrast, we show that we get wholly positive risk-aversion functions
for the same period and underlying index as Jackwerth’s, but using
implied techniques for both the risk-averse and risk-neutral densities (see
Section 5 for details).
Jackwerth (2004) is an expanded and updated version of Jackwerth
(1999). Jackwerth (2004) also has an expanded section on implied risk
aversion and useful summary tables of categorized literature. Jackwerth
(2004) labels his earlier findings (i.e., those in Jackwerth 2000) as a “pric-
ing kernel puzzle.” The puzzle is that, although the implied marginal
utility of wealth function should be monotonically decreasing in wealth,
Jackwerth’s empirical estimates of it after the Crash of 1987 are locally
increasing in wealth near the initial wealth level. This suggests that, in
these ranges of wealth, the representative agent is risk-seeking not risk-
averse. Ait-Sahalia and Lo (2000: 36, Fig. 3) find a similar locally humped
plot of the scaled marginal rate of substitution using S&P 500 futures
prices. Our chapter is similar to Jackwerth (2000, 2004) and Ait-Sahalia

38
T. Arnold, T. F. Crack, and A. Schwartz
and Lo (2000) in that we recover both risk-neutral and risk-averse dis-
tributions and compare them, but we differ in that we infer our ex-ante
risk-averse distributions from option prices using the RA-IBT rather than
from a backward-looking historical time series of the underlying, as do
these authors.
Another strand of the literature includes Bliss and Panigirtzoglou
(2004) and Alonso et al. (2009) and several other papers they cite. Like
Ziegler (2007), these authors exploit the Breeden and Litzenberger (1978)
result, rather than implied binomial trees, to derive risk-neutral densi-
ties. They then calibrate the parameters of a chosen utility function that
is used to risk-adjust the risk-neutral density. The objective of the cali-
bration is that the risk-averse density should best explain subsequently
realized returns (see further discussion in Section 5). This allows them to
discuss implied risk aversion. Their work is closely related to our own,
except that rather than use implied binomial trees, they use numeri-
cal smoothing techniques to account for volatility smiles over a range
of option strikes, and they use the Breeden and Litzenberger (1978)
result. Our approach has two advantages over these approaches. First,
our implied tree is guaranteed to be arbitrage-free (assuming there are
no-arbitrage opportunities among the quoted option prices), whereas
the Bliss and Panigirtzoglou (2004) numerical smoothing techniques are
not guaranteed to be arbitrage-free. Second, our approach uses a sim-
ple numerical estimation without splines or smoothing (we estimate an
R-IBT and then apply a simple direct transformation to it).
Blackburn (2006) focuses on the time-series properties of risk aversion
and whether the representative agent’s utility is time-separable or not.
Like Bliss and Panigirtzoglou (2004) and Alonso et al. (2009), he exploits
the Breeden and Litzenberger (1978) result and uses splines to derive
the risk-neutral density. Unlike these authors, Blackburn argues that a
calibration that maximizes the forecast ability of the risk-averse density
is inappropriate (because it looks ahead in a way not possible when the
agent is making decisions). Instead, Blackburn obtains a risk-aversion
estimate using five years of historical data. Blackburn (2006) thus differs
from us in that he does not use trees at all, and he uses historical data to
estimate the risk-aversion parameter.
2.3
A risk-averse binomial tree (RA-BT) model
We now derive the RA-BT model, so that the implied version (i.e., the RA-
IBT) can be developed in Section 4. We begin by noting that generating
the RA-BT or RA-IBT trees relies upon three interrelated technical steps.
First, we derive the functional form of the transformation between the

Inferring Risk-Averse Probability Distributions
39
risk-neutral and risk-averse trees. Second, we need to generate a risk pre-
mium or risk-adjusted discount rate at every node of the RA-IBT to feed
into the transformation in the first step. Third, we need to combine
the first two steps and propagate risk-averse probabilities through the
risk-averse tree.
To work our way toward establishing the first two steps in the case of
the RA-BT, recall that a continuous-time option pricing model using the
risk-adjusted probability measure requires a stochastic path-dependent
risk-adjusted discount rate; no single risk-adjusted discount rate can cap-
ture the changes in the option’s risk associated with the moneyness
of the option.2 Black and Scholes recognize this with their “instanta-
neous CAPM” approach to deriving the Black–Scholes partial differential
equation (Black and Scholes 1973: 645–646; Ingersoll 1987: 323–324).
However, the (Black–Scholes) model that emerges is difficult to interpret
with respect to the physical world because the risk-averse probability
parameters fall out of the calculation.
The risk-averse RA-BT model is similar to a discretized version of
the original Black–Scholes instantaneous CAPM derivation that allows
for changing risk-adjusted discount rates. The numerical discretization
allows us to infer physical-world parameters from the tree – an infer-
ence not explicitly available in the closed-form continuous-time (i.e.,
the Black–Scholes world) limit of the RA-BT pricing model.
To generate the RA-BT model, begin with the assumptions of the CRR
model as follows. Consider an asset with spot price St at time t. From time
t to time t +t, the asset price either moves up by a multiplicative growth
factor u = eσ
√
t, or moves down by a multiplicative growth factor d =
e−σ
√
t. Assume a constant continuously compounded riskless interest
rate r, so the riskless growth factor is R = ert over the time step. Let Vt be
the time–t price of a European-style derivative that, at time t +t, has the
value Vu in the up state and Vd in the down state. Let q =

R −d

/

u −d

denote the fixed CRR risk-neutral probability of an up-move. Then, to
avoid arbitrage, the CRR model says that equation (2.1) holds for the
value of the European-style derivative over the time step t:
Vt = 1
RERN

Vt+t

= 1
R

qVu +

1 −q

Vd

= 1
R
R −d
u −d

Vu +
u −R
u −d

Vd

,
(2.1)
where ERN (·) is the risk-neutral probability expectations operator.

40
T. Arnold, T. F. Crack, and A. Schwartz
Arnold et al. (2009) give both equilibrium and no-arbitrage derivations
to show that, if K = ekt is a risk-adjusted compounding factor over
time step t, then p =

K −d

/

u −d

is the risk-averse probability of the
up state and equation (2.2) holds for the value of the European-style
derivative over the time step t:
Vt = 1
R

E

Vt+t

−
Vu −Vd
u −d

(K −R)

= 1
R
	
pVu +

1 −p

Vd

−
Vu −Vd
u −d

(K −R)

(2.2)
where E(·) is the risk-averse probability expectations operator. That is,
given an estimated CRR tree and a risk-adjusted discount rate k (or a
risk premium k −r), we can deduce the risk-averse probability p for any
up-move in the CRR tree. The derivative pricing is identical between
equations (2.1) and (2.2), but the probabilities are risk-neutral in (2.1)
and risk-averse in (2.2).
Equation (2.2) is, essentially, a certainty equivalent formula. It is
derived from the relationship in equation (1), and it forms the basis for
our first technical step. It provides a means of deducing risk-averse prob-
abilities to overlay on the price structure of an underlying risk-neutral
tree. Our RA-BT tree is, thus, a CRR tree transformed by replacing risk-
neutral probabilities with risk-averse probabilities (see Arnold et al. 2009
for more details and Arnold and Crack 2004 for an application).
The second step is to generate a risk premium or risk-adjusted discount
rate to feed into each node of the no-arbitrage transformation between
risk-neutral and risk-averse trees. The risk premium can be derived from
an asset pricing model, such as the CAPM. In the case of a macro asset
(e.g., the S&P 500 index portfolio), a representative agent argument frees
us of the CAPM assumptions, and the risk-adjusted discount rates that
feed into each node of this transformation can be derived using gen-
eral assumed utility functions for the representative agent (Arnold et al.
2009).
Note that, for any given node, each admissible k produces the same
option valuation at that node (admissible k requires −σ
√
t < kt <
σ
√
t or, equivalently, d < K < u to avoid negative risk-averse probabili-
ties). That is, the risk-adjusted discount rate k determines the risk-averse
probability p and, by construction, k and p offset each other within the
pricing equation to leave the option value unchanged. In fact, one must
be cautious in interpreting p as the risk-averse probability of an up-move
at a node, because any admissible k produces the same option valuation
at that node (see Arnold et al. 2009 for more details). This leads us to a

Inferring Risk-Averse Probability Distributions
41
clause. The fidelity with which p reproduces the true risk-averse proba-
bility of an up-move at a given node of a one-step RA-BT tree depends
upon the accuracy in the choice of k as the true risk-adjusted discount
rate for the underlying security.
This fidelity clause is both a major strength and a slight weakness of
our chapter. It is a major strength because, once supplied with the risk-
adjusted discount rate k at any node, we can take that node on an existing
risk-neutral tree and transform it into a node on a risk-adjusted tree, while
retaining the derivatives pricing at that node. That is, we get existence
of a solution to the risk-averse tree driven by existence of a solution to
the no-arbitrage-driven risk-neutral tree, and we get it via a no-arbitrage
transformation between the two trees at that node. The fidelity clause is
a slight weakness because the risk-averse probabilities inferred from the
RA-BT (and subsequently from the RA-IBT, as discussed below) are only as
good as the discount rate fed into the transformation between the trees.
The third step is to propagate probabilities through the tree. It is almost
trivial in the case of the RA-BT. The multi-period RA-BT model follows
immediately from the single-period model in equation (2.2) simply by
applying the single-period model iteratively backwards through the tree.
The values for the underlying asset price in the risk-averse tree are iden-
tical to the values for the underlying asset price in the CRR tree. In the
special case where k = r at every node or, equivalently, K = R at every
node, the risk-averse model reduces to the CRR model. In the limit where
step size tends to zero, Black–Scholes-world pricing is obtained.
Assuming a constant risk premium in the multi-period RA-BT places a
restriction on the most general form of the RA-BT, where the risk pre-
mium varies freely with state and time. A constant risk premium in
the RA-BT is consistent with assuming power utility for a representative
agent.
2.4
The risk-averse implied binomial tree (RA-IBT)
We need to establish the same three technical steps that we established
for the RA-BT in building an RA-IBT. We establish the first two steps by
starting with an R-IBT. Rubinstein’s R-IBT is a multi-step binomial tree.
Each step in the R-IBT is a one-step CRR model (though it need not pos-
sess the traditional CRR property that u = 1/d). The R-IBT (and thus each
of the one-step CRR trees of which it is composed) is estimated using a
calibration to market prices of traded European-style options. This cali-
bration allows the parameters of each one-step CRR model to be different
at every node within the R-IBT. By doing so, the final distribution of asset

42
T. Arnold, T. F. Crack, and A. Schwartz
prices in an R-IBT need not be lognormal, even when step sizes tend to
zero. The R-IBT is well behaved and robust (Chriss 1997: 431). In prac-
tice, as long as no arbitrage violations exist among the option prices,
then a solution exists for the R-IBT (Rubinstein 1994: 783).
We can both establish that a solution to the risk-averse implied bino-
mial tree (RA-IBT) model exists and demonstrate how the solution is
related to the other binomial trees by asking what happens if, at each
node within an R-IBT, we transform the one-step CRR model there into
a one-step RA-BT model. That is, given risk-adjusted discount rate k at
that node and focusing on just one internal node of the tree, we replace
risk-neutral probability of an up-move q =

R −d

/

u −d

with risk-averse
probability of an up-move p =

K −d

/

u −d

, where R and K are as
defined earlier. We do not change u or d, or the values of the under-
lying, or the value of the derivative at this node, just the probabilities.
The valuation formula at this node, looking ahead to the next two nodes,
then changes from equation (2.1) to equation (2.2). This is the first step
we needed to establish.
If we do exactly the same transformation for every internal node in the
tree, we create a new tree full of one-step risk-averse tree (RA-BT) models.
The new tree provides the same pricing as the R-IBT at each node. That
is, the underlying asset and any derivative have the same values at each
node on the new tree as they had in the R-IBT we started with – we
have a new tree that has risk-averse probabilities of an up-jump at any
step, risk-adjusted discount rates for the underlying, and a new pricing
formula (equation [2.2]) at each node. This new tree is our RA-IBT. If
a solution exists for the R-IBT (and we note above that it does in the
absence of arbitrage opportunities between the options), then we can
build our new RA-IBT tree using the transformation described above and
in detail in Arnold et al. (2009).
The second step is generation of the risk premium at each node to
feed into the transformation at the first step. We assume a constant risk
premium throughout the tree. This is not a requirement of the model
but rather an empirical restriction imposed here for ease of exposition.
This restriction is consistent with a representative agent that possesses a
power-like utility function (i.e., power utility where the CRRA parameter
varies with the state).
This new RA-IBT tree captures volatility smiles and excess skewness
and kurtosis. The probability structure in this tree is, however, no longer
risk-neutral but risk-averse. It has all the benefits of the R-IBT but without
the restriction to risk-neutral probabilities. Of course, where the risk
premium is zero, the RA-IBT reduces to an R-IBT.

Inferring Risk-Averse Probability Distributions
43
We have not yet mentioned explicitly how the ending nodal risk-averse
probabilities are generated in our RA-IBT. In the original Rubinstein
R-IBT, an optimization is performed, and the ending nodal risk-neutral
probabilities are the choice variables that are estimated. Rubinstein
(1994: 790) supplies a backward recursion that starts at these ending
nodal probabilities and works backward through the tree to deduce all
the u, d, and q parameters, which typically vary at each node (with
constant discount rate r for both the underlying and the option). In our
RA-IBT, something quite different is needed. Having already solved for an
R-IBT and propagated its ending nodal probabilities backward through
the R-IBT, we then apply the transformation described above to arrive at
the u, d, and p parameters, which typically vary at each node through the
RA-IBT. Recall that the transformation needs a risk-adjusted discount rate
k for the underlying at each node either from an assumed utility func-
tion or imposed (with utility consequences). The u and d parameters in
the RA-IBT tree are unchanged from those in the R-IBT tree. We may
then propagate the up-step probabilities p forward through the RA-IBT
to obtain nodal probabilities at each node, out to the ending nodes of
the RA-IBT. Arnold et al. (2009) demonstrate the propagation algorithm
in detail. This completes the derivation of the RA-IBT.
We now discuss another distinction between the R-IBT and the RA-IBT.
Rubinstein’s R-IBT possesses binomial path independence (BPI). That is,
each path leading to any given node arrives there with equal probability
(Chriss 1997: 417). The nodal probability at any node in an R-IBT is thus
simply the path probability times the number of paths arriving at that
node. Our transformation from the risk-neutral R-IBT to the risk-adjusted
RA-IBT does not, however, preserve BPI. It is not true that paths through
our risk-averse RA-IBT tree have equal path probability. Rubinstein forces
his R-IBT tree to have BPI so as to reduce the degrees of freedom enough to
be able to solve the problem and arrive at a solution that propagates natu-
rally backwards through his R-IBT tree. The fact that Rubinstein enforces
BPI in his tree yields his solution, which guarantees the existence of ours.
Our direct transformation of Rubinstein’s tree to ours is followed by a for-
ward propagation of the probabilities without ever needing to explicitly
work out path probabilities.
In summary, we rely upon three distinct but interrelated technical
steps. The first step is the derivation of the functional form of the trans-
formation that binds the risk-neutral and risk-averse trees. At any given
node in the tree, this transformation is a function of the risk-adjusted
discount rate or risk premium at that node. The second step is the ability
to derive this risk-adjusted discount rate at any given node. The third

44
T. Arnold, T. F. Crack, and A. Schwartz
step is our demonstration of how to combine and implement these first
two steps and how to propagate risk-adjusted probabilities through the
risk-averse binomial tree.
2.5
Empirical analysis
2.5.1
The options data
We use intraday data on S&P 500 index options over the period from
January 1993 to September 1995. Twenty out of 33 possible sets are usable
after we eliminate data that do not provide an adequate cross-section of
prices.
Each month we select 10 call option quotes, with bid and ask prices in
excess of $0.50. The options are of different strikes but the same matu-
rity (two months, but varying between 59 and 61 days throughout the
period). We select options that are closest to the money and as close as
possible to 11:00 A.M. CST. For a given calibration, all of the quotes are
usually collected within a quarter of an hour. The index level is sam-
pled as close as possible to 11:00 A.M. CST. The index level is adjusted for
dividends (i.e., the discounted value of future dividends during the life
of the option is subtracted from the index price based on historic div-
idend payouts collected from the S&P 500 Information Bulletin). Given
the short maturity of the options and the stability of the index over this
time period, using the actual dividends as a substitute for anticipated div-
idends appears reasonable. Further, for the same reason, the riskless rate
is used to discount the dividends. The effect of using an assumed higher
discount rate corresponding to the index for discounting the dividends
is negligible. Finally, we screen option quotes for arbitrage violations,
using a risk-free rate inferred from closing quote midpoints of US Trea-
sury securities that straddle the option maturity date (collected from the
Wall Street Journal).
Given the criteria for the data, 20 sets of options are available for
empirical analysis. Using a 200-step binomial tree, the RA-IBT model is
estimated using imposed risk premiums of 0.0 percent (this is the R-IBT),
3.7 percent, 7.5 percent, and 11.3 percent (i.e., RA-IBTs consistent with
power utility with varying CRRA). In total, 20 binomial trees are esti-
mated via optimization using 10 option quotes each (these are the R-IBT
trees); an additional 60 RA-IBT trees are derived as transformations of
the R-IBTs (three different risk premiums for each R-IBT). A CRR tree
for each of the 20 sets of options data is also computed for comparison
purposes.

Inferring Risk-Averse Probability Distributions
45
Table 2.1
Model price comparison with bid and
ask quotes of 60-day options (January 19, 1993)
Strike price
Bid price
Model price
Ask price
405
32.0000
32.7518
34.0000
410
27.3750
27.9949
29.3750
415
23.0000
23.4068
25.0000
420
19.0625
19.0629
19.8125
425
15.0000
15.0581
16.0000
430
11.2500
11.4714
12.2500
435∗
8.1250
8.3688
8.6250
440
5.1250
5.7877
6.1250
445
3.3750
3.7434
3.8750
450
1.7500
2.2497
2.2500
∗Indicates the at-the-money option. The risk-free rate is
2.88 percent per annum. The annual implied volatil-
ity is 11.2 percent. The objective function is minimized
to a value of 0.0000425. These model prices are from a
200-step R-IBT using a lower bound on nodal probabili-
ties of 0.0000005. Identical model prices (to more than
10 decimal places) are obtained from the three RA-IBT
models with different risk premiums.
All the risk-averse RA-IBT models in this chapter are estimated by trans-
forming the solution to a risk-neutral Rubinstein R-IBT. The Rubinstein
R-IBT is estimated using an optimization routine that minimizes the
Jackwerth and Rubinstein (1996) smooth objective function subject to
pricing the traded options within the spread. In practice, the pricing is
very good. Of the 200 options we price in calibrating the R-IBTs (i.e., 10
options priced in each of 20 periods), only two are not priced within the
spread. One is priced at 1/1000th of a penny below the bid and the other
at 12/1000ths of a penny below the bid. Otherwise, all other options
are priced strictly within the spread. The RA-IBTs, by construction as
direct transformations of the R-IBTs, produce identical pricing to the
R-IBTs from which they are derived. Table 2.1 displays, as an example,
the R-IBT prices versus the bid and ask prices for the first set of options
(January 19, 1993). The dividend adjusted level of the S&P 500 around
11:00 a.m. CST was 433.78.
2.5.2
Marginal rate of substitution and implied relative
risk-aversion
We now consider the relationships between utility functions and prob-
ability densities. There are many reasons for doing this. For example,

46
T. Arnold, T. F. Crack, and A. Schwartz
stochastic volatility type and jump diffusion type option pricing models
typically have skewed and kurtotic return distributions for the under-
lying security. In these models, a utility function is necessary to map
from the theoretical risk-averse probability return distribution of the
underlying security to the associated risk-neutral return distribution.
Generally, the utility function is chosen with convenience in mind and
not necessarily due to a particular economic rationale. Empirical work
that harvests information about aggregate utility from option prices can
help to shape the assumptions made in such models.
To use our estimated density functions for the S&P 500 to make infer-
ences about representative agent utility functions, we assume that some
unspecified equilibrium asset pricing model holds, that it applies in a
representative agent setting, and that the S&P 500 as a broad market
index serves as a proxy for aggregate consumption. For related discus-
sion, see Ait-Sahalia and Lo (2000), who in turn cite Brown and Gibbons
(1985) and also discuss the limits of these assumptions; see also Bliss and
Panigirtzoglou (2004).
Let fR−IBT(ST) and fRA−IBT(ST) denote the implied risk-neutral and
risk-averse density functions, respectively, that are inferred from our
IBTs for the future level ST of the S&P 500.3 We exploit two relationships
between utility functions and probability densities. The first relationship
is that the ratio of the risk-neutral density to the risk-averse density gives
up to a constant that is independent of the index level, the marginal
rate of substitution (MRS) of the representative agent between consump-
tion at time T and time t, as shown in equation (2.3) (Ingersoll 1987:
187; Ait-Sahalia and Lo 2000: 27; Jackwerth 1999: 72, 2000: 436, and
2004: 53):
fR−IBT(ST)/fRA−IBT(ST) ∝U′(ST)/U′(St) = MRS
(2.3)
The MRS is the “pricing kernel.” We will use the terms “MRS” and
“pricing kernel” interchangeably.
If the representative agent is risk-neutral, then we expect the MRS to
be unity. If the representative agent is risk-averse, we expect the MRS to
be downward-sloping as a function of wealth. Jackwerth (2000, 2004)
reports several authors finding that the MRS is locally upward-sloping
for some wealth levels near the initial wealth– a “pricing kernel puzzle”
because it means the representative investor is locally risk-seeking.
We find that the MRS is downward-sloping and well behaved for each
level of risk premium fed into the RA-IBT model (see Figure 2.1 for the 7.5
percent risk premium case). The time period for our data sample encom-
passes that of Ait-Sahalia and Lo (2000). Our results for the MRS are

Inferring Risk-Averse Probability Distributions
47
0.0
0.5
1.0
1.5
2.0
2.5
3.0
–8.0%
–6.0%
–4.0%
–2.0%
0.0%
2.0%
4.0%
6.0%
8.0%
Percentage change in S&P500 over next two months
Scaled MRS
MRS
+2SE
–2SE
Figure 2.1
Scaled marginal rate of substitution (RP = 7.5%)
Note: For the 7.5 percent risk premium case, and for each of the 20 months’
optimizations from 1993 to 1995, we estimate the scaled marginal rate of substi-
tution (MRS) (i.e., the pricing kernel) as the ratio fR−IBT(ST)/fRA−IBT(ST). We then
average these MRS numbers across the 20 months’ estimations by first associating
each with the percentage change in the S&P 500 relative to that month’s dividend
adjusted index level S∗. We calculate the average only where each individual den-
sity possesses a contiguous range of values that does not use the optimization’s
lower bound on the density of 0.0000005. Each tree’s ending nodes are different;
so, for each return level on the plot, we linearly interpolate between the individ-
ual estimates before taking the average. We show the average plus and minus two
empirical standard errors of the mean (SE).
quite similar to those in Ait-Sahalia and Lo (2000: 36, figure 3), though
their confidence interval is bordering on negative territory at high val-
ues of the index, whereas ours is clearly positive everywhere. Our results
are, however, quite unlike the oddly shaped, locally increasing pricing
kernels in Jackwerth (2004: 57, figure 11). The Jackwerth (2004) data are
from a much later time period than ours, and this could partially explain
differences in results.
The Ait-Sahalia and Lo (2000) MRS is calculated using nonparametric
techniques for the numerator and historical data for the denominator
in equation (2.3). The Jackwerth (2004) MRS is calculated using IBTs
for the numerator and historical data for the denominator in equation
(2.3). We differ from each of these authors in that we are the first to use

48
T. Arnold, T. F. Crack, and A. Schwartz
wholly implied techniques for both numerator and denominator. Our
MRS results are much smoother than Ait-Sahalia and Lo’s and wholly
downward-sloping, unlike Jackwerth (2004).
The second relationship between utility and probability densities we
exploit is that we can estimate the implied Arrow–Pratt measure of RRA
using equation (2.6) (Ingersoll 1987: 38–39):4
RRA = ST

f ′
RA−IBT(ST)/fRA−IBT(ST) −f ′
R−IBT(ST)/fR−IBT(ST)

(2.4)
Typical empirical estimates of the RRA range from about 0 to 55 (see
good summaries of prior findings in Ait-Sahalia and Lo 2000: 39, Table 5;
and Jackwerth 2004: 53–54). Jackwerth finds, however, clearly negative
values for absolute (and thus also for relative) risk aversion near initial
levels of wealth (Jackwerth 2000: 442, figure 3: 442). Negative RRA ties in
with locally upward-sloping MRS and forms his pricing kernel puzzle –
inconsistent with economic theory.
Our implied RRA numbers are wholly positive across all levels of
wealth, and they are of the order of 3–9, 7–18, and 9–27 for the 3.7
percent, 7.5 percent, and 11.3 percent risk premium cases, respectively
(middle case only shown). Our implied RRA numbers (Figure 2.2) are
similar to Ait-Sahalia and Lo’s (2000: 38, figure 4) in sign, size, and
behavior across states, but our plots are, again, much smoother than
theirs. Like Ait-Sahalia and Lo, we find economically and statistically
significant evidence against CRRA, and we find that RRA increases with
increasing wealth beyond current levels. Of course, varying CRRA is con-
sistent with our assumption of an imposed constant risk premium. Our
results are quite different from the clearly negative results in Jackwerth
(2000: 442, figure 3). Unlike our MRS results, the time period that Jackw-
erth uses to calculate his risk aversion in Panel D of his figure 3 (Jackwerth
2000: 442) overlaps substantially with the time period we use. Therefore,
different time periods are not the explanation.
The major difference between our analysis and Jackwerth’s is that we
use implied trees for the risk-averse density estimation and he uses his-
torical data. Although Jackwerth (2000: 445–446) dismisses his use of
historical data to estimate the risk-averse density as a cause of the puz-
zle, we suspect that this may be, at least in part, responsible for his
economically unintuitive results.
Ait-Sahalia and Lo (1998) criticize IBTs as possessing inherently nonsta-
tionary estimates relative to nonparametric techniques, but we certainly
do not see that in the results we present. In particular, in comparing our

Inferring Risk-Averse Probability Distributions
49
0
5
10
15
20
25
–8.0%
–6.0%
–4.0%
–2.0%
0.0%
2.0%
4.0%
6.0%
8.0%
Percentage change in the S&P500 over the next two months
Implied risk aversion
Implied RA
+2SE
–2SE
Figure 2.2
Implied Arrow–Pratt relative risk aversion (RP = 7.5%)
Note: For the 7.5 percent risk premium case and for each of the 20 months’
optimizations from 1993 to 1995, we estimate the implied Arrow–Pratt RRA for
each two-month-ahead level ST of the S&P 500 as ST[f ′
RA−IBT(ST)/fRA−IBT(ST) −
f ′
R−IBT(ST)/fR−IBT(ST)]. We average these estimates over the 20 months’ estima-
tions by first putting them on an equal footing by associating each with the
percentage change in the S&P 500 relative to that month’s dividend adjusted
index level S∗. We calculate the mean only where each month’s density (and its
slope estimate) possesses a contiguous range of values that does not use the opti-
mization’s lower bound on the density (0.0000005). Each tree’s ending nodes are
different; so, for each return level on the plot, we linearly interpolate between
the individual estimates before taking the average. We show the average plus and
minus two empirical standard errors of the mean.
MRS and RRA estimations with those in Ait-Sahalia and Lo (2000), we
note that our plots are much smoother. This difference in smoothness
may be because their nonparametric kernel estimations use a bandwidth
that is too small, though Jackwerth suggests that they may in fact have
oversmoothed their results (Jackwerth 2004: 54). Alternatively, the dif-
ference in smoothness may be because Ait-Sahalia and Lo estimate their
plots as a snapshot over one year, whereas we re-estimate our trees
20 times over three years and then average the results. Our averaging
may produce smoother results than their nonparametric technique, but
we would not expect this if our IBTs were inherently nonstationary, as
suggested by Ait-Sahalia and Lo.

50
T. Arnold, T. F. Crack, and A. Schwartz
Bliss and Panigirtzoglou (2004) approach the stationarity issue from
yet another angle. Rather than using implied binomial trees, they use
Breeden and Litzenberger’s well-known result (1978) to deduce risk-
neutral densities from option prices. They then assume a utility function
(either power or exponential) and use it to obtain a risk-adjusted den-
sity function. By fixing the utility function and allowing the density
functions to be time-varying, they avoid having to assume that the den-
sity functions are stationary. The aim of their chapter is to calibrate the
parameters of the utility function so as not to be able to reject the risk-
adjusted implied densities as forecasts of subsequently realized returns
distributions. They find RRA estimates that decrease with increasing
horizon and little evidence of pricing kernel anomalies.
The bottom line is that we find no pricing kernel puzzle using wholly
implied techniques. Therefore, the representative agent is risk-averse
with no local risk-seeking behavior. We do find significant variation
in RRA across states that is inconsistent with an assumption of CRRA.
We also find that risk aversion increases with increasing wealth beyond
current wealth.
2.6
Conclusion
Our risk-averse implied binomial tree (RA-IBT) model generalizes Rubin-
stein’s risk-neutral implied binomial tree (R-IBT) model by allowing for
a nonzero risk premium on the underlying asset. The RA-IBT accom-
modates a risk premium that is time-varying and/or state-dependent,
depending upon either the assumed utility function of the representative
agent (in the case of a macro asset such as the S&P 500 index portfolio)
or a CAPM beta (in the case of an individual stock). We have imposed a
constant risk premium in our empirical work with S&P 500 index options
(consistent with assumed power utility with varying CRRA for a repre-
sentative agent). Our S&P 500 index options data run between 1993 and
1995. We estimate the pricing kernel (marginal rate of substitution) and
implied RRA and compare and contrast our results with other researchers’
results. In particular, we are the first to use implied techniques for both
the risk-neutral and risk-averse densities, and we find no “pricing kernel
puzzle” using these techniques (compared with other authors who use
historical data to generate the risk-averse density).
Acknowledgments
We thank David Alexander, Ravi Bansal, Alex Butler, Scott Chaput,
Robin Grieves, Robert Hauswald, Jimmy Hilliard, Stewart Mayhew,

Inferring Risk-Averse Probability Distributions
51
Susan Monaco, Sanjay Nawalkha, Mark Rubinstein, Louis Scott, Richard
Shockley, seminar participants at the University of Georgia and Univer-
sity of Otago, and an anonymous referee. Any errors are ours.
Notes
1. In Arnold, Crack and Schwartz (2009) we show how to relax the constant
risk premium assumption and generate a risk premium at any node using an
assumed utility function of a representative agent, and we provide examples
for power utility and negative exponential utility.
2. Cox and Rubinstein (1985: 324) discuss a related problem with a discount rate
that is correct on average.
3. Strictly speaking, our discrete trees yield discrete probability masses associated
with ending discrete nodal values of the index. For our 200-step trees, we
associate the probability mass with the width of a range of index values about
the node, and we deduce the density f as the constant value of mass/width
over that range about that node.
4. In fact, we use RRA = (1 + ρ)[f ′
RA−IBT(ρ)/fRA−IBT(ρ) −f ′
R−IBT(ρ)/fR−IBT(ρ)],
where ρ = ST/S∗−1 is the simple net return, so that we can put each of
the 20 months’ estimations on an equal footing and average across them to
get the mean RRA and its empirical standard error. This form of the RRA is
mathematically identical to equation (2.4)—although we have never seen it
published.
References
Ait-Sahalia, Y. and Lo, A. W. (1998) “Nonparametric Estimation of State-Price
Densities Implicit in Financial Asset Prices,” Journal of Finance, 53 (2): 499–547.
Ait-Sahalia, Y. and Lo, A. W. (2000) “Nonparametric Risk Management and Implied
Risk Aversion,” Journal of Econometrics, 94 (1/2): 9–51.
Alonso, F., Blanco R., and Rubio, G. (2009) “Option-Implied Preferences Adjust-
ments, Density Forecasts, and the Equity Risk Premium,” Spanish Economic
Review, 11 (2): 141–164.
Arnold, T. and Crack, T. F. (2004) “Using the WACC to Value Real Options,”
Financial Analysts Journal, 60 (6): 78–82.
Arnold, T., Crack T. F., and Schwartz, A. (2009) “Inferring Risk-Averse Probability
Distributions from Options Prices Using Implied Binomial Trees: Additional
Theory, Empirics, and Extensions,” Working paper. Available online at SSRN:
http://ssrn.com/abstract=749904 (accessed June 2, 2009).
Black, F. and Scholes, M. (1973) “The Pricing of Options and Corporate Liabilities,”
Journal of Political Economy, 81 (3): 637–659.
Blackburn,
D. W. (2006) “Option Implied Risk Aversion and Elasticity of
Intertemporal Substitution,”
Working paper.
Available online at SSRN:
http://ssrn.com/abstract=927440 (accessed June 2, 2009).
Bliss, R. R. and Panigirtzoglou, N. (2004) “Option-Implied Risk Aversion Esti-
mates,” Journal of Finance, 59 (1): 407–446.

52
T. Arnold, T. F. Crack, and A. Schwartz
Breeden, D. T. and Litzenberger, R. H. (1978) “Prices of State-Contingent Claims
Implicit in Options Prices,” Journal of Business, 51 (4): 621–651.
Brown, D. P. and Gibbons, M. R. (1985) “A Simple Econometric Approach for
Utility-Based Asset Pricing Models,” Journal of Finance, 40 (2): 359–381.
Chriss, N. A. (1997) Black–Scholes and Beyond: Option Pricing Models, New York:
McGraw-Hill.
Cox, J. C., Ross, S., and Rubinstein, M. (1979) “Option Pricing: A Simplified
Approach,” Journal of Financial Economics, 7 (3): 229–263.
Cox, J. C. and Rubinstein, M. (1985) Options Markets, Englewood Cliffs, NJ:
Prentice-Hall, Inc.
Ingersoll, J. E. (1987) Theory of Financial Decision Making, Savage, Md.: Rowman &
Littlefield.
Jackwerth, J. C. (1999) “Option-Implied Risk-Neutral Distributions and Implied
Binomial Trees: A Literature Review,” Journal of Derivatives, 7 (2): 66–82.
Jackwerth, J. C. (2000) “Recovering Risk Aversion from Option Prices and Realized
Returns,” Review of Financial Studies, 13 (2): 433–451.
Jackwerth, J. C. (2004) Option-Implied Risk-Neutral Distributions and Risk Aversion,
Charlottesville, VA: AIMR Research Foundation Monograph (CFA Institute).
Jackwerth J. C. and Rubinstein, M. (1996) “Recovering Probability Distributions
from Option Prices,” Journal of Finance, 51 (5): 1611–1631.
Leland, H. E. (1980) “Who Should Buy Portfolio Insurance?” Journal of Finance, 35
(2): 581–594.
Rubinstein, M. (1994) “Implied Binomial Trees,” Journal of Finance, 49 (3):
771–818.
Stutzer, M. (1996) “A Simple Nonparametric Approach to Derivative Security
Valuation,” Journal of Finance, 51 (5): 1633–1652.
Ziegler, A. (2007) “Why Does Implied Risk Aversion Smile?” Review of Financial
Studies, 20 (3): 859–904.


## Risk-Averse Distributions from Options

The Operation of Hedge Funds
33
Lo, A. (2008b) “Hedge Funds, Systemic Risk, and the Financial Crisis of 2007,”
written testimony prepared for the U.S. House of Representatives, Committee
on Oversight and Government Reform, Hearing on Hedge Funds, Washington,
DC, November 13.
Lowenstein, R. (2001) When Genius Failed: The Rise and Fall of Long-Term Capital
Management, New York: Random House.
Malkiel, B. and Saha, A. (2004) “Hedge Funds: Risk and Return,” Princeton
University Working Paper, Princeton, NJ.
Mamoghli, C. and Daboussi, S. (2009) “Performance Measurement of Hedge Funds
Portfolios in a Downside Risk Framework,” The Journal of Wealth Management,
12 (2): 101–112.
Minsky, H. (1986) Stabilizing an Unstable Economy, New Haven, Conn.: Yale
University Press.
Modigliani, F. and Ando, A. (1960) “The ‘Permanent Income’ and ‘Life Cycle’
Hypothesis of Saving Behavior: Comparison and Tests,” in Irwin Friend and
Robert Jones (eds.), Consumption and Saving, Philadelphia, Pa.: University of
Pennsylvania, vol. II, pp. 49–174.
Munk, C., Sørensen, C., and Nygaard Vinther, T. (2004) “Dynamic Asset
Allocation under Mean-Reverting Returns, Stochastic Interest Rates and Infla-
tion Uncertainty: Are Popular Recommendations Consistent with Rational
Behavior?” International Review of Economics and Finance, 13 (2): 141–166.
Pigou, A. C. (1951) “Professor Duesenberry on Income and Savings,” Economic
Journal, 61 (244): 883–885.
Platen, E. and Semmler, W. (2009) “Asset Markets and Monetary Policy,” Research
Paper Series 247, Quantitative Finance Research Centre, University of Technol-
ogy, Sydney.
Posthuma, N. and Van der Sluis, P. (2003) “A Reality Check on Hedge Fund
Returns,” Free University Amsterdam.
Ruder, D. (2008) “Testimony to the House Committee on Oversight and Govern-
ment Reform,” prepared for the U.S. House of Representatives, Committee on
Oversight and Government Reform, Hearing on Hedge Funds, Washington,
DC, November 13.
Saltz, I. (1999) “An Examination of the Causal Relationship between Savings and
Growth in the Third World,” Journal of Economics and Finance, 23 (1): 90.
Semmler, W. (2006) Asset Prices, Booms, and Recessions, Heidelberg and New York:
Springer.
Sharpe, W. (1994) “The Sharpe Ratio,” Journal of Portfolio Management, 21 (1):
49–58.
Sortino, F., and Price, L. (1994) “Performance Measurement in a Downside Risk
Framework,” Journal of Investing, 3 (3): 59–64.
Tooby, J. and Cosmides, L. (1996) “Friendship and the Banker’s Paradox: Other
Pathways to the Evolution of Adaptations for Altruism,” Proceedings of the British
Academy, 8 (2): 119–143.
Vaughan, D. (2003) “SEC Roundtable on Hedge Funds,” May 13, comments avail-
able online at http://www.sec.gov/spotlight/hedgefunds/hedge-vaughn.htm
(accessed September 18, 2010).
Vickrey, W. (1947) “Resource Distribution Patterns and the Classification of
Families,” Studies in Income and Wealth, NBER, Volume 10.

34
W. Semmler and R. Chappe
Wachter, J. (2002) “Portfolio and Consumption Decisions under Mean-Reverting
Returns: An Exact Solution for Complete Markets,” Journal of Financial and
Quantitative Analysis, 37 (1): 63–91.
Xiong, J. (2009) “Impact of Size and Flows on Performance for Funds of Hedge
Funds,” Journal of Portfolio Management, 35 (2): 120–130.

2
Inferring Risk-Averse Probability
Distributions from Option Prices
Using Implied Binomial Trees
Tom Arnold, Timothy Falcon Crack, and Adam Schwartz
2.1
Introduction
We generalize the Rubinstein (1994) risk-neutral implied binomial tree
(R-IBT) model to a physical-world risk-averse implied binomial tree
(RA-IBT) model. The R-IBT and RA-IBT trees are bound together via a
relationship requiring a risk premium (or a risk-adjusted discount rate)
on the underlying asset at any node. The RA-IBT provides a powerful
numerical platform for many empirical financial option and real option
applications; these include probabilistic inference, pricing, and utility
theory applications.
For ease of exposition, we have estimated a constant risk premium1 RA-
IBT using Standard & Poor’s 500 index options. In our implied tree, this is
consistent with assuming a representative agent with a power-like utility
function where the constant relative risk aversion (CRRA) parameter is
allowed to vary across states and through time. With these assumptions,
we estimate the pricing kernel (marginal rate of substitution) and implied
relative risk aversion (RRA) of our agent and compare and contrast our
results with other authors’ findings. Other empirical applications can be
found in Arnold et al. (2009).
2.2
Motivation and literature review
2.2.1
Motivation/introduction of risk-averse trees
The traditional binomial tree model of Cox, Ross, and Rubinstein
(CRR) (1979) is very powerful, but it is constrained in many respects.
The CRR model cannot, for example, reproduce some well-known
35

36
T. Arnold, T. F. Crack, and A. Schwartz
empirical results (e.g., fat tails, skewness, volatility smiles, etc.), and any
probabilistic inferences from a CRR tree must be risk-neutral inferences
not risk-averse probability inferences from the physical economy.
The Rubinstein (1994) implied binomial tree (R-IBT) generalizes the
CRR model to fit the prices of a series of traded options of the same matu-
rity. The R-IBT allows significant deviations from lognormality of prices
(and from normality of continuously compounded returns), allows the
up-jump probability to vary throughout the tree, and allows the local
volatility structure to vary throughout the tree. The R-IBT model is still
constrained, however, in that the probability structure is risk-neutral;
and, therefore, like the CRR model, it does not allow probabilistic
inferences about the physical economy.
In this chapter, we begin with a generalization of the risk-neutral CRR
model to a risk-averse binomial tree (RA-BT). We then present a general-
ization of the risk-averse RA-BT to a risk-averse implied binomial tree
(RA-IBT). Like the R-IBT model, the RA-IBT model captures volatility
smiles and varying local volatility. It should be noted, however, that
both the RA-BT and the RA-IBT have one extra input compared with the
CRR and R-IBT models: The risk-averse trees need to be supplied with
a risk premium (or a risk-adjusted discount rate) at every node to make
them estimable. This risk premium feeds into a relationship that drives
a transformation from the risk-neutral trees to the risk-averse trees.
For empirical ease, we impose a constant risk premium in the RA-
IBT estimations in this chapter. Whether the risk premium is imposed
directly, or derived from utility assumptions for a representative agent, to
each such risk premium function over the nodes of an RA-IBT there cor-
responds a different implied risk-averse probability distribution for the
future prices of the underlying asset; this, in turn, implies a unique, fully
specified stochastic process for the underlying asset prices. Sensitivity
analysis is thus essential for any inferences.
The CRR, RA-BT, R-IBT, and RA-IBT models can each be used to value
and hedge both European-style and American-style options. Neither the
R-IBT model nor the RA-IBT model (under the conditions we develop in
this chapter) can be calibrated using American-style options.
2.2.2
Literature review
Rubinstein (1994: 793, footnote 25) describes implied trees developed by
Hayne Leland (1980) that use “subjective probabilities” (i.e., an individ-
ual investor’s non-risk-neutral probabilities). Stutzer (1996) also infers
“subjective” (i.e., risk-averse) probability densities from options data.
Stutzer differs from us, however, in that he uses diffusions rather than
binomial trees, he requires historical data that are not needed here, and

Inferring Risk-Averse Probability Distributions
37
he uses the risk-averse density to estimate the risk-neutral density for
risk-neutral pricing (the focus of his paper), whereas our focus is the
risk-averse density itself.
Jackwerth and Rubinstein (1996) infer probabilities from option prices
using binomial trees. However, Jackwerth and Rubinstein differ from us
because they use risk-neutral probabilities, whereas we use risk-averse
probabilities. We do though use their “smooth” objective function in
estimating our R-IBT.
Jackwerth (2000) recovers risk-neutral densities from S&P 500 options
and uses historical realized index returns to approximate subjective (i.e.,
risk-averse) densities. Jackwerth is thus able to infer aggregate absolute
risk-aversion functions for different states. When comparing pre- and
post-Crash of 1987 data, changes in the implied risk-neutral densities
that are not accompanied by changes in the risk-averse densities imply
changes in absolute risk-aversion functions that appear inconsistent with
any sensible economic theory (e.g., Jackwerth finds significantly negative
absolute risk aversion). Jackwerth suggests that overpriced put options
may explain the inconsistency, and he is able to construct profitable
trading strategies that appear to exploit this potential mispricing. Jack-
werth (1999) acknowledges that another explanation for inconsistent
risk-aversion functions is that his risk-averse distributions built using his-
torical observations may differ from true ex-ante risk-averse distributions
(Jackwerth 1999: 445–446). However, he rejects this as an explanation
because his trading strategies appear profitable (supporting the hypothe-
sis that his inconsistent risk-aversion functions are driven by exploitable
mispriced options, not by poor estimates of subjective probability). In
contrast, we show that we get wholly positive risk-aversion functions
for the same period and underlying index as Jackwerth’s, but using
implied techniques for both the risk-averse and risk-neutral densities (see
Section 5 for details).
Jackwerth (2004) is an expanded and updated version of Jackwerth
(1999). Jackwerth (2004) also has an expanded section on implied risk
aversion and useful summary tables of categorized literature. Jackwerth
(2004) labels his earlier findings (i.e., those in Jackwerth 2000) as a “pric-
ing kernel puzzle.” The puzzle is that, although the implied marginal
utility of wealth function should be monotonically decreasing in wealth,
Jackwerth’s empirical estimates of it after the Crash of 1987 are locally
increasing in wealth near the initial wealth level. This suggests that, in
these ranges of wealth, the representative agent is risk-seeking not risk-
averse. Ait-Sahalia and Lo (2000: 36, Fig. 3) find a similar locally humped
plot of the scaled marginal rate of substitution using S&P 500 futures
prices. Our chapter is similar to Jackwerth (2000, 2004) and Ait-Sahalia

38
T. Arnold, T. F. Crack, and A. Schwartz
and Lo (2000) in that we recover both risk-neutral and risk-averse dis-
tributions and compare them, but we differ in that we infer our ex-ante
risk-averse distributions from option prices using the RA-IBT rather than
from a backward-looking historical time series of the underlying, as do
these authors.
Another strand of the literature includes Bliss and Panigirtzoglou
(2004) and Alonso et al. (2009) and several other papers they cite. Like
Ziegler (2007), these authors exploit the Breeden and Litzenberger (1978)
result, rather than implied binomial trees, to derive risk-neutral densi-
ties. They then calibrate the parameters of a chosen utility function that
is used to risk-adjust the risk-neutral density. The objective of the cali-
bration is that the risk-averse density should best explain subsequently
realized returns (see further discussion in Section 5). This allows them to
discuss implied risk aversion. Their work is closely related to our own,
except that rather than use implied binomial trees, they use numeri-
cal smoothing techniques to account for volatility smiles over a range
of option strikes, and they use the Breeden and Litzenberger (1978)
result. Our approach has two advantages over these approaches. First,
our implied tree is guaranteed to be arbitrage-free (assuming there are
no-arbitrage opportunities among the quoted option prices), whereas
the Bliss and Panigirtzoglou (2004) numerical smoothing techniques are
not guaranteed to be arbitrage-free. Second, our approach uses a sim-
ple numerical estimation without splines or smoothing (we estimate an
R-IBT and then apply a simple direct transformation to it).
Blackburn (2006) focuses on the time-series properties of risk aversion
and whether the representative agent’s utility is time-separable or not.
Like Bliss and Panigirtzoglou (2004) and Alonso et al. (2009), he exploits
the Breeden and Litzenberger (1978) result and uses splines to derive
the risk-neutral density. Unlike these authors, Blackburn argues that a
calibration that maximizes the forecast ability of the risk-averse density
is inappropriate (because it looks ahead in a way not possible when the
agent is making decisions). Instead, Blackburn obtains a risk-aversion
estimate using five years of historical data. Blackburn (2006) thus differs
from us in that he does not use trees at all, and he uses historical data to
estimate the risk-aversion parameter.
2.3
A risk-averse binomial tree (RA-BT) model
We now derive the RA-BT model, so that the implied version (i.e., the RA-
IBT) can be developed in Section 4. We begin by noting that generating
the RA-BT or RA-IBT trees relies upon three interrelated technical steps.
First, we derive the functional form of the transformation between the

Inferring Risk-Averse Probability Distributions
39
risk-neutral and risk-averse trees. Second, we need to generate a risk pre-
mium or risk-adjusted discount rate at every node of the RA-IBT to feed
into the transformation in the first step. Third, we need to combine
the first two steps and propagate risk-averse probabilities through the
risk-averse tree.
To work our way toward establishing the first two steps in the case of
the RA-BT, recall that a continuous-time option pricing model using the
risk-adjusted probability measure requires a stochastic path-dependent
risk-adjusted discount rate; no single risk-adjusted discount rate can cap-
ture the changes in the option’s risk associated with the moneyness
of the option.2 Black and Scholes recognize this with their “instanta-
neous CAPM” approach to deriving the Black–Scholes partial differential
equation (Black and Scholes 1973: 645–646; Ingersoll 1987: 323–324).
However, the (Black–Scholes) model that emerges is difficult to interpret
with respect to the physical world because the risk-averse probability
parameters fall out of the calculation.
The risk-averse RA-BT model is similar to a discretized version of
the original Black–Scholes instantaneous CAPM derivation that allows
for changing risk-adjusted discount rates. The numerical discretization
allows us to infer physical-world parameters from the tree – an infer-
ence not explicitly available in the closed-form continuous-time (i.e.,
the Black–Scholes world) limit of the RA-BT pricing model.
To generate the RA-BT model, begin with the assumptions of the CRR
model as follows. Consider an asset with spot price St at time t. From time
t to time t +t, the asset price either moves up by a multiplicative growth
factor u = eσ
√
t, or moves down by a multiplicative growth factor d =
e−σ
√
t. Assume a constant continuously compounded riskless interest
rate r, so the riskless growth factor is R = ert over the time step. Let Vt be
the time–t price of a European-style derivative that, at time t +t, has the
value Vu in the up state and Vd in the down state. Let q =

R −d

/

u −d

denote the fixed CRR risk-neutral probability of an up-move. Then, to
avoid arbitrage, the CRR model says that equation (2.1) holds for the
value of the European-style derivative over the time step t:
Vt = 1
RERN

Vt+t

= 1
R

qVu +

1 −q

Vd

= 1
R
R −d
u −d

Vu +
u −R
u −d

Vd

,
(2.1)
where ERN (·) is the risk-neutral probability expectations operator.

40
T. Arnold, T. F. Crack, and A. Schwartz
Arnold et al. (2009) give both equilibrium and no-arbitrage derivations
to show that, if K = ekt is a risk-adjusted compounding factor over
time step t, then p =

K −d

/

u −d

is the risk-averse probability of the
up state and equation (2.2) holds for the value of the European-style
derivative over the time step t:
Vt = 1
R

E

Vt+t

−
Vu −Vd
u −d

(K −R)

= 1
R
	
pVu +

1 −p

Vd

−
Vu −Vd
u −d

(K −R)

(2.2)
where E(·) is the risk-averse probability expectations operator. That is,
given an estimated CRR tree and a risk-adjusted discount rate k (or a
risk premium k −r), we can deduce the risk-averse probability p for any
up-move in the CRR tree. The derivative pricing is identical between
equations (2.1) and (2.2), but the probabilities are risk-neutral in (2.1)
and risk-averse in (2.2).
Equation (2.2) is, essentially, a certainty equivalent formula. It is
derived from the relationship in equation (1), and it forms the basis for
our first technical step. It provides a means of deducing risk-averse prob-
abilities to overlay on the price structure of an underlying risk-neutral
tree. Our RA-BT tree is, thus, a CRR tree transformed by replacing risk-
neutral probabilities with risk-averse probabilities (see Arnold et al. 2009
for more details and Arnold and Crack 2004 for an application).
The second step is to generate a risk premium or risk-adjusted discount
rate to feed into each node of the no-arbitrage transformation between
risk-neutral and risk-averse trees. The risk premium can be derived from
an asset pricing model, such as the CAPM. In the case of a macro asset
(e.g., the S&P 500 index portfolio), a representative agent argument frees
us of the CAPM assumptions, and the risk-adjusted discount rates that
feed into each node of this transformation can be derived using gen-
eral assumed utility functions for the representative agent (Arnold et al.
2009).
Note that, for any given node, each admissible k produces the same
option valuation at that node (admissible k requires −σ
√
t < kt <
σ
√
t or, equivalently, d < K < u to avoid negative risk-averse probabili-
ties). That is, the risk-adjusted discount rate k determines the risk-averse
probability p and, by construction, k and p offset each other within the
pricing equation to leave the option value unchanged. In fact, one must
be cautious in interpreting p as the risk-averse probability of an up-move
at a node, because any admissible k produces the same option valuation
at that node (see Arnold et al. 2009 for more details). This leads us to a

Inferring Risk-Averse Probability Distributions
41
clause. The fidelity with which p reproduces the true risk-averse proba-
bility of an up-move at a given node of a one-step RA-BT tree depends
upon the accuracy in the choice of k as the true risk-adjusted discount
rate for the underlying security.
This fidelity clause is both a major strength and a slight weakness of
our chapter. It is a major strength because, once supplied with the risk-
adjusted discount rate k at any node, we can take that node on an existing
risk-neutral tree and transform it into a node on a risk-adjusted tree, while
retaining the derivatives pricing at that node. That is, we get existence
of a solution to the risk-averse tree driven by existence of a solution to
the no-arbitrage-driven risk-neutral tree, and we get it via a no-arbitrage
transformation between the two trees at that node. The fidelity clause is
a slight weakness because the risk-averse probabilities inferred from the
RA-BT (and subsequently from the RA-IBT, as discussed below) are only as
good as the discount rate fed into the transformation between the trees.
The third step is to propagate probabilities through the tree. It is almost
trivial in the case of the RA-BT. The multi-period RA-BT model follows
immediately from the single-period model in equation (2.2) simply by
applying the single-period model iteratively backwards through the tree.
The values for the underlying asset price in the risk-averse tree are iden-
tical to the values for the underlying asset price in the CRR tree. In the
special case where k = r at every node or, equivalently, K = R at every
node, the risk-averse model reduces to the CRR model. In the limit where
step size tends to zero, Black–Scholes-world pricing is obtained.
Assuming a constant risk premium in the multi-period RA-BT places a
restriction on the most general form of the RA-BT, where the risk pre-
mium varies freely with state and time. A constant risk premium in
the RA-BT is consistent with assuming power utility for a representative
agent.
2.4
The risk-averse implied binomial tree (RA-IBT)
We need to establish the same three technical steps that we established
for the RA-BT in building an RA-IBT. We establish the first two steps by
starting with an R-IBT. Rubinstein’s R-IBT is a multi-step binomial tree.
Each step in the R-IBT is a one-step CRR model (though it need not pos-
sess the traditional CRR property that u = 1/d). The R-IBT (and thus each
of the one-step CRR trees of which it is composed) is estimated using a
calibration to market prices of traded European-style options. This cali-
bration allows the parameters of each one-step CRR model to be different
at every node within the R-IBT. By doing so, the final distribution of asset

42
T. Arnold, T. F. Crack, and A. Schwartz
prices in an R-IBT need not be lognormal, even when step sizes tend to
zero. The R-IBT is well behaved and robust (Chriss 1997: 431). In prac-
tice, as long as no arbitrage violations exist among the option prices,
then a solution exists for the R-IBT (Rubinstein 1994: 783).
We can both establish that a solution to the risk-averse implied bino-
mial tree (RA-IBT) model exists and demonstrate how the solution is
related to the other binomial trees by asking what happens if, at each
node within an R-IBT, we transform the one-step CRR model there into
a one-step RA-BT model. That is, given risk-adjusted discount rate k at
that node and focusing on just one internal node of the tree, we replace
risk-neutral probability of an up-move q =

R −d

/

u −d

with risk-averse
probability of an up-move p =

K −d

/

u −d

, where R and K are as
defined earlier. We do not change u or d, or the values of the under-
lying, or the value of the derivative at this node, just the probabilities.
The valuation formula at this node, looking ahead to the next two nodes,
then changes from equation (2.1) to equation (2.2). This is the first step
we needed to establish.
If we do exactly the same transformation for every internal node in the
tree, we create a new tree full of one-step risk-averse tree (RA-BT) models.
The new tree provides the same pricing as the R-IBT at each node. That
is, the underlying asset and any derivative have the same values at each
node on the new tree as they had in the R-IBT we started with – we
have a new tree that has risk-averse probabilities of an up-jump at any
step, risk-adjusted discount rates for the underlying, and a new pricing
formula (equation [2.2]) at each node. This new tree is our RA-IBT. If
a solution exists for the R-IBT (and we note above that it does in the
absence of arbitrage opportunities between the options), then we can
build our new RA-IBT tree using the transformation described above and
in detail in Arnold et al. (2009).
The second step is generation of the risk premium at each node to
feed into the transformation at the first step. We assume a constant risk
premium throughout the tree. This is not a requirement of the model
but rather an empirical restriction imposed here for ease of exposition.
This restriction is consistent with a representative agent that possesses a
power-like utility function (i.e., power utility where the CRRA parameter
varies with the state).
This new RA-IBT tree captures volatility smiles and excess skewness
and kurtosis. The probability structure in this tree is, however, no longer
risk-neutral but risk-averse. It has all the benefits of the R-IBT but without
the restriction to risk-neutral probabilities. Of course, where the risk
premium is zero, the RA-IBT reduces to an R-IBT.

Inferring Risk-Averse Probability Distributions
43
We have not yet mentioned explicitly how the ending nodal risk-averse
probabilities are generated in our RA-IBT. In the original Rubinstein
R-IBT, an optimization is performed, and the ending nodal risk-neutral
probabilities are the choice variables that are estimated. Rubinstein
(1994: 790) supplies a backward recursion that starts at these ending
nodal probabilities and works backward through the tree to deduce all
the u, d, and q parameters, which typically vary at each node (with
constant discount rate r for both the underlying and the option). In our
RA-IBT, something quite different is needed. Having already solved for an
R-IBT and propagated its ending nodal probabilities backward through
the R-IBT, we then apply the transformation described above to arrive at
the u, d, and p parameters, which typically vary at each node through the
RA-IBT. Recall that the transformation needs a risk-adjusted discount rate
k for the underlying at each node either from an assumed utility func-
tion or imposed (with utility consequences). The u and d parameters in
the RA-IBT tree are unchanged from those in the R-IBT tree. We may
then propagate the up-step probabilities p forward through the RA-IBT
to obtain nodal probabilities at each node, out to the ending nodes of
the RA-IBT. Arnold et al. (2009) demonstrate the propagation algorithm
in detail. This completes the derivation of the RA-IBT.
We now discuss another distinction between the R-IBT and the RA-IBT.
Rubinstein’s R-IBT possesses binomial path independence (BPI). That is,
each path leading to any given node arrives there with equal probability
(Chriss 1997: 417). The nodal probability at any node in an R-IBT is thus
simply the path probability times the number of paths arriving at that
node. Our transformation from the risk-neutral R-IBT to the risk-adjusted
RA-IBT does not, however, preserve BPI. It is not true that paths through
our risk-averse RA-IBT tree have equal path probability. Rubinstein forces
his R-IBT tree to have BPI so as to reduce the degrees of freedom enough to
be able to solve the problem and arrive at a solution that propagates natu-
rally backwards through his R-IBT tree. The fact that Rubinstein enforces
BPI in his tree yields his solution, which guarantees the existence of ours.
Our direct transformation of Rubinstein’s tree to ours is followed by a for-
ward propagation of the probabilities without ever needing to explicitly
work out path probabilities.
In summary, we rely upon three distinct but interrelated technical
steps. The first step is the derivation of the functional form of the trans-
formation that binds the risk-neutral and risk-averse trees. At any given
node in the tree, this transformation is a function of the risk-adjusted
discount rate or risk premium at that node. The second step is the ability
to derive this risk-adjusted discount rate at any given node. The third

44
T. Arnold, T. F. Crack, and A. Schwartz
step is our demonstration of how to combine and implement these first
two steps and how to propagate risk-adjusted probabilities through the
risk-averse binomial tree.
2.5
Empirical analysis
2.5.1
The options data
We use intraday data on S&P 500 index options over the period from
January 1993 to September 1995. Twenty out of 33 possible sets are usable
after we eliminate data that do not provide an adequate cross-section of
prices.
Each month we select 10 call option quotes, with bid and ask prices in
excess of $0.50. The options are of different strikes but the same matu-
rity (two months, but varying between 59 and 61 days throughout the
period). We select options that are closest to the money and as close as
possible to 11:00 A.M. CST. For a given calibration, all of the quotes are
usually collected within a quarter of an hour. The index level is sam-
pled as close as possible to 11:00 A.M. CST. The index level is adjusted for
dividends (i.e., the discounted value of future dividends during the life
of the option is subtracted from the index price based on historic div-
idend payouts collected from the S&P 500 Information Bulletin). Given
the short maturity of the options and the stability of the index over this
time period, using the actual dividends as a substitute for anticipated div-
idends appears reasonable. Further, for the same reason, the riskless rate
is used to discount the dividends. The effect of using an assumed higher
discount rate corresponding to the index for discounting the dividends
is negligible. Finally, we screen option quotes for arbitrage violations,
using a risk-free rate inferred from closing quote midpoints of US Trea-
sury securities that straddle the option maturity date (collected from the
Wall Street Journal).
Given the criteria for the data, 20 sets of options are available for
empirical analysis. Using a 200-step binomial tree, the RA-IBT model is
estimated using imposed risk premiums of 0.0 percent (this is the R-IBT),
3.7 percent, 7.5 percent, and 11.3 percent (i.e., RA-IBTs consistent with
power utility with varying CRRA). In total, 20 binomial trees are esti-
mated via optimization using 10 option quotes each (these are the R-IBT
trees); an additional 60 RA-IBT trees are derived as transformations of
the R-IBTs (three different risk premiums for each R-IBT). A CRR tree
for each of the 20 sets of options data is also computed for comparison
purposes.

Inferring Risk-Averse Probability Distributions
45
Table 2.1
Model price comparison with bid and
ask quotes of 60-day options (January 19, 1993)
Strike price
Bid price
Model price
Ask price
405
32.0000
32.7518
34.0000
410
27.3750
27.9949
29.3750
415
23.0000
23.4068
25.0000
420
19.0625
19.0629
19.8125
425
15.0000
15.0581
16.0000
430
11.2500
11.4714
12.2500
435∗
8.1250
8.3688
8.6250
440
5.1250
5.7877
6.1250
445
3.3750
3.7434
3.8750
450
1.7500
2.2497
2.2500
∗Indicates the at-the-money option. The risk-free rate is
2.88 percent per annum. The annual implied volatil-
ity is 11.2 percent. The objective function is minimized
to a value of 0.0000425. These model prices are from a
200-step R-IBT using a lower bound on nodal probabili-
ties of 0.0000005. Identical model prices (to more than
10 decimal places) are obtained from the three RA-IBT
models with different risk premiums.
All the risk-averse RA-IBT models in this chapter are estimated by trans-
forming the solution to a risk-neutral Rubinstein R-IBT. The Rubinstein
R-IBT is estimated using an optimization routine that minimizes the
Jackwerth and Rubinstein (1996) smooth objective function subject to
pricing the traded options within the spread. In practice, the pricing is
very good. Of the 200 options we price in calibrating the R-IBTs (i.e., 10
options priced in each of 20 periods), only two are not priced within the
spread. One is priced at 1/1000th of a penny below the bid and the other
at 12/1000ths of a penny below the bid. Otherwise, all other options
are priced strictly within the spread. The RA-IBTs, by construction as
direct transformations of the R-IBTs, produce identical pricing to the
R-IBTs from which they are derived. Table 2.1 displays, as an example,
the R-IBT prices versus the bid and ask prices for the first set of options
(January 19, 1993). The dividend adjusted level of the S&P 500 around
11:00 a.m. CST was 433.78.
2.5.2
Marginal rate of substitution and implied relative
risk-aversion
We now consider the relationships between utility functions and prob-
ability densities. There are many reasons for doing this. For example,

46
T. Arnold, T. F. Crack, and A. Schwartz
stochastic volatility type and jump diffusion type option pricing models
typically have skewed and kurtotic return distributions for the under-
lying security. In these models, a utility function is necessary to map
from the theoretical risk-averse probability return distribution of the
underlying security to the associated risk-neutral return distribution.
Generally, the utility function is chosen with convenience in mind and
not necessarily due to a particular economic rationale. Empirical work
that harvests information about aggregate utility from option prices can
help to shape the assumptions made in such models.
To use our estimated density functions for the S&P 500 to make infer-
ences about representative agent utility functions, we assume that some
unspecified equilibrium asset pricing model holds, that it applies in a
representative agent setting, and that the S&P 500 as a broad market
index serves as a proxy for aggregate consumption. For related discus-
sion, see Ait-Sahalia and Lo (2000), who in turn cite Brown and Gibbons
(1985) and also discuss the limits of these assumptions; see also Bliss and
Panigirtzoglou (2004).
Let fR−IBT(ST) and fRA−IBT(ST) denote the implied risk-neutral and
risk-averse density functions, respectively, that are inferred from our
IBTs for the future level ST of the S&P 500.3 We exploit two relationships
between utility functions and probability densities. The first relationship
is that the ratio of the risk-neutral density to the risk-averse density gives
up to a constant that is independent of the index level, the marginal
rate of substitution (MRS) of the representative agent between consump-
tion at time T and time t, as shown in equation (2.3) (Ingersoll 1987:
187; Ait-Sahalia and Lo 2000: 27; Jackwerth 1999: 72, 2000: 436, and
2004: 53):
fR−IBT(ST)/fRA−IBT(ST) ∝U′(ST)/U′(St) = MRS
(2.3)
The MRS is the “pricing kernel.” We will use the terms “MRS” and
“pricing kernel” interchangeably.
If the representative agent is risk-neutral, then we expect the MRS to
be unity. If the representative agent is risk-averse, we expect the MRS to
be downward-sloping as a function of wealth. Jackwerth (2000, 2004)
reports several authors finding that the MRS is locally upward-sloping
for some wealth levels near the initial wealth– a “pricing kernel puzzle”
because it means the representative investor is locally risk-seeking.
We find that the MRS is downward-sloping and well behaved for each
level of risk premium fed into the RA-IBT model (see Figure 2.1 for the 7.5
percent risk premium case). The time period for our data sample encom-
passes that of Ait-Sahalia and Lo (2000). Our results for the MRS are

Inferring Risk-Averse Probability Distributions
47
0.0
0.5
1.0
1.5
2.0
2.5
3.0
–8.0%
–6.0%
–4.0%
–2.0%
0.0%
2.0%
4.0%
6.0%
8.0%
Percentage change in S&P500 over next two months
Scaled MRS
MRS
+2SE
–2SE
Figure 2.1
Scaled marginal rate of substitution (RP = 7.5%)
Note: For the 7.5 percent risk premium case, and for each of the 20 months’
optimizations from 1993 to 1995, we estimate the scaled marginal rate of substi-
tution (MRS) (i.e., the pricing kernel) as the ratio fR−IBT(ST)/fRA−IBT(ST). We then
average these MRS numbers across the 20 months’ estimations by first associating
each with the percentage change in the S&P 500 relative to that month’s dividend
adjusted index level S∗. We calculate the average only where each individual den-
sity possesses a contiguous range of values that does not use the optimization’s
lower bound on the density of 0.0000005. Each tree’s ending nodes are different;
so, for each return level on the plot, we linearly interpolate between the individ-
ual estimates before taking the average. We show the average plus and minus two
empirical standard errors of the mean (SE).
quite similar to those in Ait-Sahalia and Lo (2000: 36, figure 3), though
their confidence interval is bordering on negative territory at high val-
ues of the index, whereas ours is clearly positive everywhere. Our results
are, however, quite unlike the oddly shaped, locally increasing pricing
kernels in Jackwerth (2004: 57, figure 11). The Jackwerth (2004) data are
from a much later time period than ours, and this could partially explain
differences in results.
The Ait-Sahalia and Lo (2000) MRS is calculated using nonparametric
techniques for the numerator and historical data for the denominator
in equation (2.3). The Jackwerth (2004) MRS is calculated using IBTs
for the numerator and historical data for the denominator in equation
(2.3). We differ from each of these authors in that we are the first to use

48
T. Arnold, T. F. Crack, and A. Schwartz
wholly implied techniques for both numerator and denominator. Our
MRS results are much smoother than Ait-Sahalia and Lo’s and wholly
downward-sloping, unlike Jackwerth (2004).
The second relationship between utility and probability densities we
exploit is that we can estimate the implied Arrow–Pratt measure of RRA
using equation (2.6) (Ingersoll 1987: 38–39):4
RRA = ST

f ′
RA−IBT(ST)/fRA−IBT(ST) −f ′
R−IBT(ST)/fR−IBT(ST)

(2.4)
Typical empirical estimates of the RRA range from about 0 to 55 (see
good summaries of prior findings in Ait-Sahalia and Lo 2000: 39, Table 5;
and Jackwerth 2004: 53–54). Jackwerth finds, however, clearly negative
values for absolute (and thus also for relative) risk aversion near initial
levels of wealth (Jackwerth 2000: 442, figure 3: 442). Negative RRA ties in
with locally upward-sloping MRS and forms his pricing kernel puzzle –
inconsistent with economic theory.
Our implied RRA numbers are wholly positive across all levels of
wealth, and they are of the order of 3–9, 7–18, and 9–27 for the 3.7
percent, 7.5 percent, and 11.3 percent risk premium cases, respectively
(middle case only shown). Our implied RRA numbers (Figure 2.2) are
similar to Ait-Sahalia and Lo’s (2000: 38, figure 4) in sign, size, and
behavior across states, but our plots are, again, much smoother than
theirs. Like Ait-Sahalia and Lo, we find economically and statistically
significant evidence against CRRA, and we find that RRA increases with
increasing wealth beyond current levels. Of course, varying CRRA is con-
sistent with our assumption of an imposed constant risk premium. Our
results are quite different from the clearly negative results in Jackwerth
(2000: 442, figure 3). Unlike our MRS results, the time period that Jackw-
erth uses to calculate his risk aversion in Panel D of his figure 3 (Jackwerth
2000: 442) overlaps substantially with the time period we use. Therefore,
different time periods are not the explanation.
The major difference between our analysis and Jackwerth’s is that we
use implied trees for the risk-averse density estimation and he uses his-
torical data. Although Jackwerth (2000: 445–446) dismisses his use of
historical data to estimate the risk-averse density as a cause of the puz-
zle, we suspect that this may be, at least in part, responsible for his
economically unintuitive results.
Ait-Sahalia and Lo (1998) criticize IBTs as possessing inherently nonsta-
tionary estimates relative to nonparametric techniques, but we certainly
do not see that in the results we present. In particular, in comparing our

Inferring Risk-Averse Probability Distributions
49
0
5
10
15
20
25
–8.0%
–6.0%
–4.0%
–2.0%
0.0%
2.0%
4.0%
6.0%
8.0%
Percentage change in the S&P500 over the next two months
Implied risk aversion
Implied RA
+2SE
–2SE
Figure 2.2
Implied Arrow–Pratt relative risk aversion (RP = 7.5%)
Note: For the 7.5 percent risk premium case and for each of the 20 months’
optimizations from 1993 to 1995, we estimate the implied Arrow–Pratt RRA for
each two-month-ahead level ST of the S&P 500 as ST[f ′
RA−IBT(ST)/fRA−IBT(ST) −
f ′
R−IBT(ST)/fR−IBT(ST)]. We average these estimates over the 20 months’ estima-
tions by first putting them on an equal footing by associating each with the
percentage change in the S&P 500 relative to that month’s dividend adjusted
index level S∗. We calculate the mean only where each month’s density (and its
slope estimate) possesses a contiguous range of values that does not use the opti-
mization’s lower bound on the density (0.0000005). Each tree’s ending nodes are
different; so, for each return level on the plot, we linearly interpolate between
the individual estimates before taking the average. We show the average plus and
minus two empirical standard errors of the mean.
MRS and RRA estimations with those in Ait-Sahalia and Lo (2000), we
note that our plots are much smoother. This difference in smoothness
may be because their nonparametric kernel estimations use a bandwidth
that is too small, though Jackwerth suggests that they may in fact have
oversmoothed their results (Jackwerth 2004: 54). Alternatively, the dif-
ference in smoothness may be because Ait-Sahalia and Lo estimate their
plots as a snapshot over one year, whereas we re-estimate our trees
20 times over three years and then average the results. Our averaging
may produce smoother results than their nonparametric technique, but
we would not expect this if our IBTs were inherently nonstationary, as
suggested by Ait-Sahalia and Lo.

50
T. Arnold, T. F. Crack, and A. Schwartz
Bliss and Panigirtzoglou (2004) approach the stationarity issue from
yet another angle. Rather than using implied binomial trees, they use
Breeden and Litzenberger’s well-known result (1978) to deduce risk-
neutral densities from option prices. They then assume a utility function
(either power or exponential) and use it to obtain a risk-adjusted den-
sity function. By fixing the utility function and allowing the density
functions to be time-varying, they avoid having to assume that the den-
sity functions are stationary. The aim of their chapter is to calibrate the
parameters of the utility function so as not to be able to reject the risk-
adjusted implied densities as forecasts of subsequently realized returns
distributions. They find RRA estimates that decrease with increasing
horizon and little evidence of pricing kernel anomalies.
The bottom line is that we find no pricing kernel puzzle using wholly
implied techniques. Therefore, the representative agent is risk-averse
with no local risk-seeking behavior. We do find significant variation
in RRA across states that is inconsistent with an assumption of CRRA.
We also find that risk aversion increases with increasing wealth beyond
current wealth.
2.6
Conclusion
Our risk-averse implied binomial tree (RA-IBT) model generalizes Rubin-
stein’s risk-neutral implied binomial tree (R-IBT) model by allowing for
a nonzero risk premium on the underlying asset. The RA-IBT accom-
modates a risk premium that is time-varying and/or state-dependent,
depending upon either the assumed utility function of the representative
agent (in the case of a macro asset such as the S&P 500 index portfolio)
or a CAPM beta (in the case of an individual stock). We have imposed a
constant risk premium in our empirical work with S&P 500 index options
(consistent with assumed power utility with varying CRRA for a repre-
sentative agent). Our S&P 500 index options data run between 1993 and
1995. We estimate the pricing kernel (marginal rate of substitution) and
implied RRA and compare and contrast our results with other researchers’
results. In particular, we are the first to use implied techniques for both
the risk-neutral and risk-averse densities, and we find no “pricing kernel
puzzle” using these techniques (compared with other authors who use
historical data to generate the risk-averse density).
Acknowledgments
We thank David Alexander, Ravi Bansal, Alex Butler, Scott Chaput,
Robin Grieves, Robert Hauswald, Jimmy Hilliard, Stewart Mayhew,

Inferring Risk-Averse Probability Distributions
51
Susan Monaco, Sanjay Nawalkha, Mark Rubinstein, Louis Scott, Richard
Shockley, seminar participants at the University of Georgia and Univer-
sity of Otago, and an anonymous referee. Any errors are ours.
Notes
1. In Arnold, Crack and Schwartz (2009) we show how to relax the constant
risk premium assumption and generate a risk premium at any node using an
assumed utility function of a representative agent, and we provide examples
for power utility and negative exponential utility.
2. Cox and Rubinstein (1985: 324) discuss a related problem with a discount rate
that is correct on average.
3. Strictly speaking, our discrete trees yield discrete probability masses associated
with ending discrete nodal values of the index. For our 200-step trees, we
associate the probability mass with the width of a range of index values about
the node, and we deduce the density f as the constant value of mass/width
over that range about that node.
4. In fact, we use RRA = (1 + ρ)[f ′
RA−IBT(ρ)/fRA−IBT(ρ) −f ′
R−IBT(ρ)/fR−IBT(ρ)],
where ρ = ST/S∗−1 is the simple net return, so that we can put each of
the 20 months’ estimations on an equal footing and average across them to
get the mean RRA and its empirical standard error. This form of the RRA is
mathematically identical to equation (2.4)—although we have never seen it
published.
References
Ait-Sahalia, Y. and Lo, A. W. (1998) “Nonparametric Estimation of State-Price
Densities Implicit in Financial Asset Prices,” Journal of Finance, 53 (2): 499–547.
Ait-Sahalia, Y. and Lo, A. W. (2000) “Nonparametric Risk Management and Implied
Risk Aversion,” Journal of Econometrics, 94 (1/2): 9–51.
Alonso, F., Blanco R., and Rubio, G. (2009) “Option-Implied Preferences Adjust-
ments, Density Forecasts, and the Equity Risk Premium,” Spanish Economic
Review, 11 (2): 141–164.
Arnold, T. and Crack, T. F. (2004) “Using the WACC to Value Real Options,”
Financial Analysts Journal, 60 (6): 78–82.
Arnold, T., Crack T. F., and Schwartz, A. (2009) “Inferring Risk-Averse Probability
Distributions from Options Prices Using Implied Binomial Trees: Additional
Theory, Empirics, and Extensions,” Working paper. Available online at SSRN:
http://ssrn.com/abstract=749904 (accessed June 2, 2009).
Black, F. and Scholes, M. (1973) “The Pricing of Options and Corporate Liabilities,”
Journal of Political Economy, 81 (3): 637–659.
Blackburn,
D. W. (2006) “Option Implied Risk Aversion and Elasticity of
Intertemporal Substitution,”
Working paper.
Available online at SSRN:
http://ssrn.com/abstract=927440 (accessed June 2, 2009).
Bliss, R. R. and Panigirtzoglou, N. (2004) “Option-Implied Risk Aversion Esti-
mates,” Journal of Finance, 59 (1): 407–446.

52
T. Arnold, T. F. Crack, and A. Schwartz
Breeden, D. T. and Litzenberger, R. H. (1978) “Prices of State-Contingent Claims
Implicit in Options Prices,” Journal of Business, 51 (4): 621–651.
Brown, D. P. and Gibbons, M. R. (1985) “A Simple Econometric Approach for
Utility-Based Asset Pricing Models,” Journal of Finance, 40 (2): 359–381.
Chriss, N. A. (1997) Black–Scholes and Beyond: Option Pricing Models, New York:
McGraw-Hill.
Cox, J. C., Ross, S., and Rubinstein, M. (1979) “Option Pricing: A Simplified
Approach,” Journal of Financial Economics, 7 (3): 229–263.
Cox, J. C. and Rubinstein, M. (1985) Options Markets, Englewood Cliffs, NJ:
Prentice-Hall, Inc.
Ingersoll, J. E. (1987) Theory of Financial Decision Making, Savage, Md.: Rowman &
Littlefield.
Jackwerth, J. C. (1999) “Option-Implied Risk-Neutral Distributions and Implied
Binomial Trees: A Literature Review,” Journal of Derivatives, 7 (2): 66–82.
Jackwerth, J. C. (2000) “Recovering Risk Aversion from Option Prices and Realized
Returns,” Review of Financial Studies, 13 (2): 433–451.
Jackwerth, J. C. (2004) Option-Implied Risk-Neutral Distributions and Risk Aversion,
Charlottesville, VA: AIMR Research Foundation Monograph (CFA Institute).
Jackwerth J. C. and Rubinstein, M. (1996) “Recovering Probability Distributions
from Option Prices,” Journal of Finance, 51 (5): 1611–1631.
Leland, H. E. (1980) “Who Should Buy Portfolio Insurance?” Journal of Finance, 35
(2): 581–594.
Rubinstein, M. (1994) “Implied Binomial Trees,” Journal of Finance, 49 (3):
771–818.
Stutzer, M. (1996) “A Simple Nonparametric Approach to Derivative Security
Valuation,” Journal of Finance, 51 (5): 1633–1652.
Ziegler, A. (2007) “Why Does Implied Risk Aversion Smile?” Review of Financial
Studies, 20 (3): 859–904.


## Pricing Toxic Assets

3
Pricing Toxic Assets
Carolyn V. Currie
3.1
Introduction: The importance of pricing toxic assets
The term “toxic asset” is a nontechnical term used to describe certain
financial assets whose value has fallen significantly so that there is no
longer a functioning market for these assets. That is, there is no liquidity
in the market, and the market cannot clear. This term became common
during the financial crisis that began in August 2007 but predated the
global financial crisis, as it was used in 2006 by Angelo Mozilo, founder
of Countrywide Financial, who used the term “toxic” to describe certain
mortgage products in emails in spring of 2006, as revealed in SEC filings:1
“[The 100% loan-to-value subprime loan is] the most dangerous prod-
uct in existence and there can be nothing more toxic.” (March 28,
2006)
The majority of these assets were connected with residential mort-
gages which had been securitized, that is, bundled into groups of assets
and then onsold. The buyer could then borrow on the basis that these
assets had been assigned high credit ratings. Often they were onsold into
levered special-purpose vehicles, which had a mixture of equity, senior,
and junior debt, with subordinated debt. This subordinated debt was
then onsold into another special-purpose vehicle, which was similarly
structured. All derived their top credit ratings from the underlying par-
cel of mortgages. As a side effect, bets on credit ratings became rampant.
These credit derivatives were largely written by only three players – prin-
cipally a state-supervised insurance company, AIG. The value of these
assets was very sensitive to economic factors such as housing prices,
default rates, and financial-market liquidity. At the slightest faltering
of economic growth, the value of these assets started to deteriorate.
53

54
Carolyn V. Currie
The pricing problem with these assets is related to how to comply with
accounting standards demanding mark to market, which could have
resulted in huge write-downs and technical insolvency for some bank
and nonbank financial institutions. The term “zombie bank” was intro-
duced to describe banks that would have become bankrupt if their assets
had been revaluated at realistic levels.2 This resulted in a credit crunch
or in excessively speculative lending to compensate for past risk-taking.
The net result was a failure in the pricing mechanism, with buyers and
sellers unwilling to transact.
On March 23,
2009,
US Treasury Secretary Timothy Geithner
announced a public-private investment partnership (PPIP) to buy toxic
assets from banks’ balance sheets. The government hype was,
An attractive feature of the program is that it will allow the mar-
ketplace to establish values for the assets – based, of course, on the
auction mechanism that will signal what someone is willing to pay for
them – and thus might ease the virtual paralysis that has surrounded
those assets up to now. For a relatively small equity exposure, the
private investor thus stands to make a considerable return if prices
recover. The government will make a gain as well.3
The PPIP has two primary programs. The Legacy Loans Program
will attempt to buy residential loans from banks’ balance sheets. The
FDIC will provide nonrecourse loan guarantees for up to 85 percent of
the purchase price of legacy loans. Private-sector asset managers and
the US Treasury will provide the remaining assets. The second pro-
gram is called the Legacy Securities Program, which will buy residential
mortgage-backed securities (RMBS) that were originally rated AAA, and
commercial mortgage-backed securities (CMBS) and asset-backed securi-
ties (ABS), which are rated AAA. The funds will come in many instances in
equal parts from the US Treasury’s Troubled Asset Relief Program monies,
from private investors, and from loans from the Federal Reserve’s Term
Asset Lending Facility (TALF). The initial size of the PPIP is projected to be
$500 billion.4 Banking analyst Meridith Whitney argues that banks will
not sell bad assets at fair market values because they are reluctant to take
asset write-downs.5 Removing toxic assets would also reduce the upward
volatility of banks’ stock prices. Because stock is a call option on a firm’s
assets, this lost volatility will hurt the stock price of distressed banks.
Therefore, such banks will only sell toxic assets at above-market prices.6
Hence, the pricing issue is critical. Will the US Government set up a clear-
ing house? Or will it design some type of open outcry, or managed open

Pricing Toxic Assets
55
outcry?7 The pricing methodology will be the biggest factor in whether
the credit system recovers.8
3.2
Hedging the prices of agricultural and
mining products9
Agricultural protection plans are commonly used by banks to hedge
for price risk using commodity broking services strategies. The differ-
ent type of plans include commodity swaps, minimum priced contracts,
currency-protected commodity swaps, physical and forward sales, col-
lars, basis, limited liability commodity swaps, and commodity protected
commodity swaps.
A commodity swap plan is a derivative product formed by converting
the global price of the commodity into local weights and measures. In
the case of the commodity swap plan, contracts are mostly cash-settled. A
product can be easily bought and sold without having a commitment to
provide physical settlement. A commodity swap plan requires an under-
standing in initial and variation margins. Buyers get the right but not the
obligation to buy or sell an underlying commodity. A minimum priced
contract plan is designed as a minimum floor contract wherein clients
can design the floor.
Commodity price instability has a negative impact on economic
growth, income distribution, and the poor. Early attempts to deal with
commodity price volatility relying on direct government intervention
(for example, price stabilization schemes, floor prices, and guaranteed
prices) were generally unsuccessful. Although there may be a case for lim-
ited direct intervention in some circumstances, liberalization of markets
has resulted in the need for market-based instruments to help manage
commodity price volatility. Large commodity exchanges typically offer
such products (for example, futures and options), but there are substan-
tial barriers to developing these markets for all commodities and for
helping farmers to access existing markets. Key investments needed to
expand access to these services include public goods (price information
systems, data management systems), strengthening supply chain rela-
tionships, strengthening technical capacity in private service providers,
and educating potential users.
3.2.1
Managing commodity price risk
Governments in many countries have intervened in markets, often
through state economic enterprises, to insulate producers and consumers
from world prices. Most interventions have taken a nonmarket approach

56
Carolyn V. Currie
in the form of quota or buffer stock programs organized through state
marketing boards. However, government interventions have been costly
and have crowded out private-sector initiatives.
Price-risk management that relies on market-based products rather
than government guarantees and subsidies will involve a substantially
reduced overall role for government in administration. The long-term
objective must be for government to assume a regulatory role, oversee-
ing markets for risk management tools. However, the public sector can
facilitate initial development of these markets and/or improve access to
established foreign or international markets for these tools, thus ensuring
that needs of the poor are adequately addressed. Market-based systems
are most relevant for standardized commodities traded internationally in
large volumes, mainly coffee, cocoa, rubber, cotton, grains, sugar, and
oilseeds (and some livestock products). They are less applicable to high-
value, highly differentiated, or perishable products for which price risk is
managed through forward contracts, often in the context of integrated
supply chains.
The rationale and theoretical underpinnings of formal mechanisms
for managing price risk are reasonably simple. There are two basic
types of price-risk management tools: physical instruments and financial
instruments:
•
Physical instruments involve strategic pricing and timing of physical
purchases and sales (such as “back-to-back” trading), forward con-
tracts, minimum price forward contracts, price-to-be fixed contracts,
and long-term contracts with fixed or floating prices.
•
Financial instruments are exchange-traded futures and options, over
the counter (OTC) options and swaps, commodity-linked bonds, and
other commodity derivatives.
•
Futures contracts involve the buyer (or seller) of a futures contract
agreeing to purchase (or sell) a specified amount of a commodity at
a specified price on a specified date. Contract terms (for example,
amounts, grades, delivery dates) are standardized, and transactions
are handled only by organized exchanges. Profits and losses in trades
are settled daily through margin funds deposited in the exchange as
collateral. Futures contracts are usually settled before or at maturity,
and they do not generally involve physical delivery of the product.
•
Options contracts offer the right – but not the obligation – to purchase
or sell a specified quantity of an underlying futures contract at a pre-
determined price on or before a given date. Like futures contracts,
exchange-traded options are standardized, OTC options offered by
banks and commodity brokers. Purchase of an option is equivalent
to price insurance and therefore requires that a price (premium) be

Pricing Toxic Assets
57
paid. Options include calls (which give the buyer the right to buy the
underlying futures contract during a given period and are purchased
as insurance against price increases) and puts (which give the buyer
the right to sell the underlying futures contract during a given period
and are purchased as an insurance against price declines).
3.2.2
Benefits
Market-based price risk management instruments have the potential to
provide producers with more certainty about the minimum price they
will receive for their crop (at the cost of higher revenues forgone), and
they may help producers make more efficient farm-management deci-
sions regarding output mix and input use. The elimination of worst-price
scenarios can provide incentives for investment in promising sectors
(which are often high risk/high return). Reducing market distortions fos-
ters diversification to new and more profitable agricultural enterprises.
Further, eliminating the primary reason for nonrepayment of loans –
an adverse move in commodity prices – can reduce the risk exposure of
producers or market intermediaries in the eyes of lenders and is likely
to result in improved access to (and terms of) credit for the sector as a
whole.
3.2.3
Policy and implementation issues
Targeting use of nonmarket mechanisms. Reforming existing nonmarket
interventions (such as price bands and floors) so that they are minimally
distorting will enable the development of market-based mechanisms
that “price stabilization” has tended to impede. Key to success of such
nonmarket schemes is the ability to accurately define the threshold
price, maintain discipline in implementation and include specific sun-
set clauses. Such schemes are appropriate only when major barriers to
market-based alternatives will persist into the medium term and where
there is a true underlying competitive advantage for the commodity
selected for the price floor scheme.
Commodity exchanges.
Well-functioning commodity exchanges –
systems of price discovery – improve marketing efficiency for agricultural
products and open up new production and marketing opportunities to
producers. They reduce price risk (faced by both producers and buyers)
by improving overall market liquidity, enhancing stability of local trad-
ing networks and providing farmers with more certainty (through better
information) of expected future prices (upon which they can make better
managerial decisions).
However, out of all these schemes, by far the most popular is floor-plan
pricing.

58
Carolyn V. Currie
3.3
Floor-plan pricing
Floor-plan pricing mechanisms are hedging tools designed to assist in
mitigating the risk associated specifically with commodity price fluctu-
ations. This allows the farmer, subject to approval from the provider to
fix a price, to select a price range or to set a price floor/cap, up to three
years in advance for certain commodities. This may assist in planning
and budgeting with greater accuracy, achieving better control margins,
and reducing the time associated with monitoring price movements on
overseas commodity exchanges.
Key features include (worked for an Australian farmer):
1. a hedge limit based on a percentage of underlying production, trade
or procurement exposure;
2. the hedge can be established in either Australian dollars or other cur-
rency denominations. An Australian-dollar-denominated product will
eliminate the need to establish a foreign-exchange hedge as well (refer
table below);
3. a maximum hedge term of up to three years (refer table below);
4. firm intraday pricing in the local time zone;
5. no exchange-traded brokerage fees or daily margin calls;
6. no requirement to physically deliver your commodity;
7. up-to-date market intelligence sourced both domestically and from
abroad.
Strategy reports are provided on a regular basis to assist in making the
most effective hedging decisions relevant to your long-term business
objectives.
3.3.1
Agribusiness price risk management solutions
Contract Specifications
Commodity
Maximum
Term
(Years)
Minimum
Quantity
Unit of
Measure
Choice of
Currency
Pricing
Reference
(Futures /
Exchange)
Hedging
Strategies
Canola
3
50
metric
tonnes
AUD or
CAD
Winnipeg
Commodity
Exchange
(WCE)
Swap,
Floor,
Cap,
Collar,
Forward

Pricing Toxic Assets
59
Corn
3
100
metric
tonnes
AUD or
USD
Chicago
Board of
Trade (CBOT)
Swap,
Floor,
Cap,
Collar,
Forward
Cotton
3
100
bales
AUD or
USD
New York
Cotton
Exchange
(NYCE)
Swap,
Floor,
Cap,
Collar,
Forward
Sugar
3
100
metric
tonnes
AUD or
USD
Coffee Sugar
& Cocoa
Exchange
(CSCE)
Swap,
Floor,
Cap,
Collar,
Forward
Wheat
3
100
metric
tonnes
AUD or
USD
Chicago
Board of
Trade (CBOT)
or Kansas
City Board of
Trade
(KCBOT)
Swap,
Floor,
Cap,
Collar,
Forward
Wheat
2
100
metric
tonnes
AUD
ASX Milling
Wheat
Swap
3.4
An example of floor-plan pricing using cattle10
An example will help illustrate the total process of hedging risk using
floor plans. Suppose a cattleman who wants to sell a load of feeder
cattle in early October checks the options quotes in June and finds he
could purchase an October feeder cattle option to sell (a put) at $60/cwt
for $2.75/cwt. To further localize this strike price, he adds a $1.00/cwt
(basis) since he normally sells 600-pound steer calves slightly higher in
October than the October futures price. Commission and premium inter-
est cost will be about $0.25/cwt so the $60 put would provide an expected
minimum selling price of $60+$1.00−$2.75−$0.25 or $58/cwt. By com-
paring this with his other pricing alternatives and his production cost,
he decides that the purchase of this put would be an appropriate strat-
egy for the 83 steers he plans to sell in October. He calls his broker and
advises him that he wants to purchase one “$60 October feeder cattle
put at $2.75.” He then forwards a check for $1,450 (500 cwt × $2.75/cwt
plus $75 brokerage fee) to his broker.

60
Carolyn V. Currie
As October approaches, one of these three things will happen: prices
stay the same; prices rise above the option strike price; or prices fall,
making the option valuable.
Alternatives are described below in Tables and Figures:11
Table 1.
Feeder Cattle Price Decline Example
$70.00
$68.00
$66.00
$64.00
$62.00
$60.00
$58.00
$56.00
Actual net price received
Actual net price received
$54.00
$50.00
$55.00
too Pet
$3.00 From
Cash Market
Sell 83 hd. feeder steers
locally @ $56.00/cwt
Cash price + gain or loss in options market =
actual price received OR $56 + $2 = $58/cwt.
Figure 1. Possible outcomes when a $60
October put is purchased, +$1.00/cwt. basis.
Figure 2. Possible outcomes from a $64 and
$56 October feeder cattle put purchase,
+$1.00/cwt. basis
October feeder cattle futures trading at $55.
Sell $60 October put and collect $5 premium.
Offset premium received - original premium &
trading cost paid = $5 - $2.75 - $.25 = $2.00
Expect to sell 83 hd in early October,
Expected basis =+1.00, So
Expect minimum selling price of $58.00
(Strike price - premium & trade cost + basis)
Buy an October Feeder Cattle put option at a
$60 strike price for $2.75 per cwt.
Premium, trading cost $.25/cwt.
Feeder Cattle Option Market
June 1
October 10
Results
Trade Cort
$60.00
$65.00
$70.00
Actual market price
Actual market price
$70.00
$68.00
$66.00
$64.00
$62.00
$60.00
$58.00
$56.00
$54.00
$50.00
$55.00
$60.00
$65.00
$70.00
$54 Pet
$5.20 From
Trade Cort
$56 Pet
$1.60 From
Trade Cort
However, consider if the cattleman had sold a call as well at an upper
price: he would have then collared his price instability and provided for
future uncertainty. This method is used to hedge gold price uncertainty
associated with the time lags involved in mining gold in Australia.
3.5
Pricing of toxic assets
In this section, a suggested pricing model is expounded that com-
bines the above elements of floor-plan pricing with Basel II methods

Pricing Toxic Assets
61
of allocating capital to a risky portfolio. All that needs to change in the
model below is the default probabilities.
Given that the amount of capital allocated to a product, transac-
tion, business unit, or portfolio influences the ultimate profitability, in
terms of risk-adjusted return on capital, and given that capital is the
most expensive source of funds, capital allocation can be deemed to
be a principal driving force in a financial institution. This has been
the obstacle in the pricing of toxic assets – if such assets have to be
written down against capital then the pricing of risk premium has to
be adjusted upwards to compensate for the amount of capital allo-
cated. By combining the method of determining capital to be allocated
with a floor-plan pricing mechanism of puts and calls, it should be
possible to provide some certainty to the market and effectively to
unfreeze it.
We need to understand the concept of economic capital and the use of
risk contributions – the risk retained by a facility, or a sub-portfolio, post-
diversification – as the foundation of the capital allocation system. Risk
contributions can be absolute or marginal, the latter being the changes in
risk with and without an additional unit of exposure, a facility or a sub-
portfolio of facilities. Whereas absolute risk contributions are allocations
of the portfolio risk to the existing individual facilities or sub-portfolios,
being embedded in the correlation structure of the portfolio, marginal
risk contributions serve essentially for risk-based pricing with an ex-ante
view of risk decisions.
Because we need a system of monitoring and pricing risk and return
on the basis of risk adjustments (that makes performance comparison
across transactions or business units consistent), buyers and sellers of
toxic assets should consider systems of ex-post risk-adjusted performance
measurement (RAPM) or ex-ante risk-based pricing (RBP) as a method of
pricing in line with risk and with the overall profitability goal of a finan-
cial institution. In the first case, income is given, whereas the purpose
of RBP is to define what is its minimum level. The risk adjustments are
the risk contributions, which do not depend on the source of the risk.
The same calculations apply to market, credit, and operating risk con-
tributions and performance. The relationship of value at risk (VaR) and
risk-based capital is an essential consideration, as the VaR methodol-
ogy serves to define risk-based capital, or the capital required to absorb
potential unexpected losses at a preset confidence level, reflecting the risk
appetite of the bank. By definition, it is also the probability that the loss
exceeds the capital, triggering bank insolvency. That is, the confidence
level is equal to the default probability of the bank.

62
Carolyn V. Currie
So what is economic capital? It is the amount of capital that is needed
to protect an organization with a chosen level of certainty against insol-
vency due to unexpected losses over a given time period of, say, one year.
Hence, operational economic capital protects the company against insol-
vency due to unexpected operational losses. To determine the amount
of economic capital the firm must decide upon the level of certainty
with which it wishes to protect itself against insolvency – the higher
the chosen level of certainty, the greater the amount of economic cap-
ital required as well as the longer the period, the greater the amount
of economic capital needed. Economic capital is, hence, a number that
summarizes the current (market, credit, operational or overall) risk pro-
file of the company in a single figure. This figure serves as a measure for
understanding the absolute size of risk as well as the change in risk over
time, as well as enabling the comparison of risk across different business
units. Finally, it is the basis for assessing whether a sufficient return has
been earned given the size of the risk being taken.
3.5.1
Calculation of risk contributions12
The mechanisms for calculating risk contributions are similar for mar-
ket risk, credit risk, and operational risk. They require loss distributions
but do not depend on the source of the risk. Capital allocations are the
absolute risk contributions and sum to total overall portfolio risk, while
marginal risk contributions do not. The importance of capital alloca-
tions are their input to RAPM on an ex-post basis, while marginal risk
contributions are relevant for pricing purposes, i.e. to new transactions.
Capital allocation aims at assigning all types of risk to the business
units that generate them, providing top-down and bottom-up links. We
can disaggregate and aggregate risk contributions according to any crite-
ria, as long as individual transaction risk contributions are available. For
instance, if several business units deal with one client, we can allocate the
risk contributions into subsets relative to each business unit according
to the type of risk. We can define standalone risk of a facility, which is
the loss volatility (LV) of a single facility. Marginal risk is the change in
the portfolio LV when adding a new facility to the existing portfolio. The
absolute risk contribution is the covariance of the random loss of this
single facility with the entire portfolio. These definitions can be applied to
the people, processing, and external events that are or may be connected with
facilities and portfolios.
Of the three definitions above, the two first are intuitive, and the
third is mathematical. The absolute risk contribution captures the risk
of a facility given that other facilities diversify away a fraction of its

Pricing Toxic Assets
63
stand-alone risk. Risk contributions also depend on the overall measure
of portfolio risk to which they contribute. The simplest risk contribu-
tions are the contributions to the LV of the portfolio loss. These risk
contributions have the attractive property of adding up to the LV of the
portfolio.
Since it is common to express capital as a multiple of this portfo-
lio LV, risk contributions are converted into capital allocations through
the same scaling factor. Since risk contributions sum to the LV, capi-
tal allocations also sum to the portfolio capital. Because they add up
to the portfolio risk measure post-diversification effects, the absolute
risk contributions are a convenient basis for the overall portfolio cap-
ital allocation to individual facilities. The concept of risk contribution is
intuitive, but calculations use technical formulas requiring us to specify
the notation. Risk contributions always refer to a facility of obligor iand a
reference portfolio P. There are several risk contributions defined below.
The portfolio P is made up of Nfacilities. Each facility irelates to a single
obligor. The notation applies to both default models and full valuation
mode models. However, all examples use calculations in default mode
only for simplicity.
3.5.2
Risk contribution definitions
The stand-alone risk is the LV of a single facility. The absolute risk con-
tribution to the LV of the portfolio is the contribution of an obligor ito
the overall LV. Absolute risk contributions to the portfolio LV differ from
the risk contributions to the portfolio capital, which are the capital allo-
cations. The capital allocations relate to the risk contributions through
the portfolio LV. To convert absolute risk contributions to portfolio LV
into absolute risk contributions to capital, we multiply them by the ratio
m(α) of capital to portfolio LV.
The marginal risk contribution to LV is the change in portfolio LV when
adding an additional unit of exposure, a new facility, a new obligor, or a
new portfolio. For instance, the marginal risk contribution of an obligor
f is the variation of the LV with and without the obligor f (or a subset aof
obligors).
3.5.3
Notation to measure risk contributions13
The marginal risk contribution to the portfolio LV and the marginal con-
tribution to capital differ. The first is the variation of the portfolio LV
when adding a facility or obligor, or any subset of facilities. The marginal
contribution to capital is the corresponding variation of capital. These
distinct marginal contributions do not relate in a simple way. The capital

64
Carolyn V. Currie
is K(α), with confidence level c The two marginal risk contributions are:
MRCP+f
f
(LVP) = LVP+f −LVP
MRCP+f
f
[K(α)] = K(α)P+f −K(α)P
Unless otherwise specified, we use marginal risk contribution as the
marginal change in LV of the portfolio. If the multiple m(α) does not
change significantly when the portfolio changes, the marginal contri-
bution to LV times the overall ratio of capital to portfolio LV is a proxy
of marginal risk contribution to capital. This approximation is not valid
whenever the portfolio changes significantly.
3.5.4
Basic properties of risk contributions
The absolute risk contributions serve to allocate capital. The absolute
risk contribution to the portfolio LV of a facility ito a portfolio Pis the
covariance of the random loss of this single facility iwith the aggregated
random portfolio loss over the entire portfolio (including i), divided by
the LV of this aggregated random loss. The formula for calculating absolute
risk contributions results from that of the variance of the portfolio. Absolute
risk contributions to LV, times the multiple of overall capital to overall portfolio
LV, sum exactly to the portfolio capital. This is the key property making them
the foundation for the capital allocation system solving the nonintuitive issue
of allocating risks.
Marginal risk contributions serve to make incremental decisions for
risk-based pricing. They provide a direct answer to questions such as:
What is the additional capital consumed by an additional facility?
What is the capital saved by withdrawing a facility or a sub-portfolio
from the current portfolio? Marginal contributions serve for pricing
purposes.
•
Pricing in such a way that the revenues of an additional facility equal the
target hurdle rate of return times the marginal risk contribution of the new
facility ensures that the target return of the portfolio on capital remains
equal to or above the minimum hurdle rate.
•
Marginal risk contributions to the portfolio LV are lower than absolute risk
contributions to the portfolio LV. However, marginal risk contributions to
the portfolio capital can be higher or lower than absolute contributions to
the portfolio capital.

Pricing Toxic Assets
65
The properties of absolute and marginal risk contributions serve to
address different issues. The key distinction is ex-post versus ex-ante
applications. Absolute risk contributions serve for ex-post alloca-
tions of capital based on effective usage of line, while marginal risk
contributions serve to make ex-ante risk-based pricing decisions.
3.5.5
Absolute and marginal risk contributions and their key
properties
To portfolio loss volatility LVp or capital Kp
Absolute risk contribution
• Sum up to LVp
ARC (ex post view)
• Capital allocation (ex post)
• Risk-based performance (ex post)
Marginal risk contribution
Do not sum up to LVp or Kp
MRC (ex ante view)
• Risk-based pricing (ex ante)
A simple example illustrates these properties, avoiding using complex
maths. However, we need to explain the concept of undiversifiable risk.
With an existing facility, the absolute risk contribution is proportional
to the stand-alone risk. The ratio of the risk contribution of a given facil-
ity to the facility LV is lower than 1. It measures the diversification effect
at the level of a facility. The ratio represents the “retained risk,” or the risk
retained within the portfolio as a percentage of the stand-alone risk of a
facility. This ratio, RR1, measures the undiversifiable risk of the facility
by the portfolio:
RRi = undiversifiable risk/standalone risk = ACRi/σi
Risk contributions and retained risk have several attractive properties
that we demonstrate below. The RR of an individual facility is simply
identical to its correlation coefficient with the entire portfolio. Since
all correlation coefficients are lower than or equal to 1, this demon-
strates the general result that the risk contribution is always lower than,
or equal to, the stand-alone risk. This is intuitively obvious since risk
contributions are post-diversification measures of risk.
The facility RR depends on the entire correlation structure with the
portfolio. The higher the RR ratio, the higher the undiversifiable risk of
the facility. It is important to track the retained risks to identify facilities

66
Carolyn V. Currie
contributing more to correlation risk. Conversely, for diversification pur-
poses, using low RR guides the choice toward transactions that increase
the diversification of the existing portfolio.
We will show in a practical example that the summation of all absolute
risk contributions is the aggregated LV of the portfolio. Using the retained
risk, this LV is:
σp =

i
RRi × σi
If all cross-correlations are zero, the absolute risk contribution reduces
to the variance of the LV squared of the facility over the variance of the
portfolio. For a portfolio, the diversification measure is simply the ratio
of the aggregated LV of the portfolio to the summation of all individual
facility loss volatilities or stand-alone risk.
We now use a simple example to calculate various loss statistics includ-
ing risk contributions. The example uses a pure default model, building
on the example of the two-obligor portfolio with 10 percent default cor-
relation. We do not replicate all detailed calculations. Rather, we detail
the comparison of stand-alone and portfolio risk measures.
The examples below provide the details of exposures and the loss
distribution.
Standalone default probabilities and default correlations
Default
Exposures XA
Probability
and XB
A
7.00%
100
B
5.00%
50
ρAB
10.00%
Loss distribution (default correlation 10%)
Cumulated
Confidence
Loss
Probabilities
Probabilities
level
A & B default
150
0.906%
100.000%
≥0.906%
A defaults
100
6.904%
99.094%
≥7.000%
B defaults
50
4.094%
93.000%
≥11.094%
Neither defaults
0
88.906%
88.906%
Not significant

Pricing Toxic Assets
67
The cumulated loss probabilities provide the loss percentiles. For
instance, the loss at the 7 percent confidence level is 50, and the loss
at the 0.906 percent confidence level is 100. When we use the second
percentile, we consider as a rough proxy of the loss at the 1 percent con-
fidence level. For confidence levels lower than or equal to 0.906 percent,
the loss is maximum, or 150. Between 7 percent and less than 0.906 per-
cent, the loss is 100. Between 11.094 percent and less than 7.00 percent,
the loss is 50.
3.5.6
Stand-alone expected losses and portfolio expected losses
The expected loss of obligor i is the default risk times the loss given
default in value. The expected loss for the portfolio of obligors is the sum
of individual obligor expected losses. The expected losses of A and B are
the default probabilities times the exposure, or 100 × 7 percent = 7 and
50×5 percent = 2.5 respectively for A and B. The portfolio expected loss
also results directly from the portfolio loss distribution considering all
four possible events, with single default probabilities lower than stand-
alone default probabilities. The probability-weighted average of the four
loss values is also 9.5.
Stand-alone Loss Volatility and Portfolio Loss Volatility
The stand-alone LV of obligor i in value is: LVi = σi = Xi ×

di × (1 −di).
The convention is that the exposure X is identical to the loss given default
or an exposure with a zero recovery rate. The loss volatilities of A and B are
LVA = 100×√7%×(1−7%) = 25.515 and LVB = 50×√5%×(1−5%) =
10.897. The unit exposure volatilities are = √P (A) [1 −P(A)] = 25.515%
for A and = √P (B) [1 −P(B)] = 21.794% for B.
Unit exposure volatilities and loss volatilities
Default
Unit exposure
Exposure weighted
Facility
Exposures
Probability
volatility
loss volatility
A
100
7%
25.515%
25.515
B
50
5%
21.794%
10.894
The direct calculation of loss statistics is replicated below. The LV is the
square root of the portfolio loss variance, or 28.73.

68
Carolyn V. Currie
Loss distribution statistics
EL
9.50
Loss volatility
28.73
Loss variance
825.36
3.5.7
Portfolio capital
Capital derives from the loss distributions and the loss percentiles at
various confidence levels. The portfolio loss percentile at 1 percent is
approximately L(1%) = 100. The expected losses of A and B are respec-
tively 7.0 and 2.5, totaling 9.5 for the portfolio. Capital is the loss
percentile in excess of expected loss, or 100−9.5 = 90.5. If the confidence
level changes the loss percentiles change as well.
3.6
Conclusion
Developing a market for caps, collars, and floors for toxic assets as well as
a uniform methodology to assess the risk contribution of such portfolios
to financial institutions will unfreeze the market and reduce the like-
lihood of more systemic shocks from write-downs. This, together with
regulatory intervention mandating the application of Basel II method-
ology for assessing capital adequacy, plus suspension of mark to market
would aid complete recovery to eventual stability.
Notes
1. “Mozilo knew hazardous waste when he saw it”, Los Angeles Times, 2009–06–
04, http://latimesblogs.latimes.com/money_co/2009/06/the-use-of-toxic-to-
describe-high-risk-mortgages-has-been-de-rigueur-for-the-last-two-years-now-
it-looks-like-countrywide.html
2. “All the President’s Zombies,” New York Times, February 23, 2009, available
online at http://www.nytimes.com/2009/02/23/opinion/23krugman.html.
(Accessed March 22, 2009.)
3. “Treasury Details Plan to Buy Risky Assets”, New York Times, Edmund L.
Andrews and Eric Dash March 23, 2009.
4. “Fact Sheet Public-Private Investment Program.”
US Treasury.
March
23, 2009. Available online at http://www.treas.gov/press/releases/reports/
ppip_fact_sheet.pdf. (Accessed March 26, 2009.)
5. “The Put Problem with Buying Toxic Assets.” SSRN.com. February 14, 2009.
Available
online
at
http://papers.ssrn.com/sol3/papers.cfm?abstract_id=
1343625. (Accessed February 15, 2009).
6. “The Put Problem with Buying Toxic Assets.”

Pricing Toxic Assets
69
7. Joe Weisenthal,
“Banks Still Pricing Toxic Assets Ridiculously High,”
March 25, 2009, available online at http://www.businessinsider.com/banks-
still-pricing-toxic-assets-ridiculously-high-2009–3.
8. Joseph Lazzaro,
“Pricing System for Toxic Assets Deemed Key to US
Treasury Bank Rescue Plan,”
February 11,
2009,
available online at
http://www.bloggingstocks.com/2009/02/11/pricing-system-for-toxic-assets-
deemed-key-to-u-s-treasury-bank.
9. This section is largely adapted from the website for National Australia Bank,
Agricultural Commodity Broking Services.
10. Adapted from J. C. McKissick, “Commodity Options as Price Insurance for
Cattlement,” The University Of Chicago Working Paper.
11. Sourced from Mckissick (2006:6).
12. Sourced from Bessis (2002: Chapter 51).
13. Sourced from Bessi (2002: 641–642).
References
Bawa, V. S. and Lindenberg, E. B. (1977) “Capital Market Equilibrium in a Mean-
Lower Partial Moment Framework,” Journal of Financial Economics, 5 (2): 189–
200.
Fabozzi, F. J., Focardi, S. N., and Kolm, P. N. (2006) Financial Modeling of the Equity
Market, Hoboken, NJ: John Wiley.
Hull, J. C. (2006) Options, Futures, and Other Derivatives, Upper Saddle River, NJ:
Prentice-Hall.
McDonald, R. L. (2006) Derivatives Markets, Boston, Mass.: Addison-Wesley.
McNeil, A. J., Frey, R., and P. Embrechts (2005) Quantitative Risk Management,
Princeton, NJ: Princeton University Press.
Nantell, T. J. and Price, B. (1979) “An Analytical Comparison of Variance and
Semivariance Capital Market Theories,” Journal of Financial and Quantitative
Analysis, 14 (2): 221–242.

4
A General Efficient Framework for
Pricing Options Using Exponential
Time Integration Schemes
Yannick Desire Tangman, Ravindra Boojhawon, Ashvin Gopaul,
and Muddun Bhuruth
4.1
Introduction
In numerical option pricing, spatial discretization of the pricing equation
leads to semi-discrete systems of the form
V′(τ) = AV(τ) + b(τ),
(4.1)
where A ∈ℜm×m is in general a negative semi-definite matrix and b(τ)
generally represents boundary condition implementations, a penalty
term for American option or approximation of integral terms on an
unbounded domain in models with jumps. With advances in the effi-
cient computation of the matrix exponential (Schmelzer and Trefethen
2007), exponential time integration (Cox and Matthews 2002) is likely
to be a method of choice for the solution of ODE systems of the form
(4.1). Duhamel’s principle states that the exact integration of (4.1) over
one time step gives
V(τj+1) = eAτ V(τj) + eAτj+1
 τj+1
τj
e−Atb(t)dt,
and approximation of the above equation by the exponential forward
Euler method leads to the scheme
Vj+1 = ϕ0(Aτ)Vj + τϕ1(Aτ)b(τj),
(4.2)
where ϕ0(z) = ez and ϕ1(z) = (ez −1)/z.
In a recent work (Tangman et al. 2008b), we investigated the use
of exponential time-integration schemes for the numerical pricing of
70

A General Efficient Framework for Pricing Options
71
European options under both the Black–Scholes model (Black and
Scholes 1973) and Merton’s jump-diffusion (MJD) model (Merton 1976)
using a onetime step computation of ϕ0. As we have noted, it is well
known that only fast evaluations of these ϕ functions will make imple-
mentation of exponential integrators (4.2) efficient. In this chapter, we
provide a more general and efficient framework for numerical pricing
of options for which the price process is allowed to follow a variety of
stochastic dynamics. Since most financial contracts usually have lin-
ear boundary conditions, we show that ETI can be easily adapted to
price a variety of options under various models and that it is very
competitive with existing numerical methods such as Crank–Nicolson.
We improve on our previous work by developing fast implementa-
tion of the ETI scheme for pricing barrier and American-type options
under various models including not only Black–Scholes and MJD but
also under stochastic volatility (SV) (Heston 1993), stochastic volatility
with jumps (SVJ) (Bates 1996) and CGMY (Carr et al. 2002) processes.
Our algorithms rely on efficient techniques for computing the matrix
exponential, and we present various numerical results indicating the
success of the framework developed here for pricing options. For Euro-
pean options, only four sparse linear systems are required to obtain
convergent option prices and hedging parameters making, ETI possi-
bly the fastest Black–Scholes partial differential equation (PDE) solver.
For pricing American options, we need to solve the linear comple-
mentarity problems (LCP) that arise. We make use here of an operator
splitting technique together with the exponential forward Euler scheme
to develop an algorithm with linear computational complexity. Extend-
ing to barrier options is straightforward by the simple implementation
of the boundary condition at the barrier level. Further improvements
in accuracy are achieved by employing a simple Richardson extrapo-
lation method, making ETI a robust framework for pricing financial
derivatives.
This chapter is structured as follows. In 4.2, we review the option pric-
ing problem formulation for European, barrier, and American options
under various models. Next, we describe the second order spatial dis-
cretization of the resulting PDEs or partial integro differential equations
(PIDEs) and implementation of the boundary condition that leads to
semi-discrete systems and show how to apply the ETI scheme. In 4.4,
we study efficient evaluation of the matrix exponentiation based on best
rational approximations (Schmelzer and Trefethen 2007; Trefethen et al.
2006). Numerical experiments are given in 4.5 followed by concluding
remarks in 4.6.

72
Y. D. Tangman, R. Boojhawon, A. Gopaul and M. Bhuruth
4.2
Option pricing problem
We consider an economy consisting of a single risky underlying asset
whose price dynamics are driven by different stochastic differential
equations, thus characterizing various models. First, if the price S follows
the geometric Brownian motion,
dSt = (r −δ)Stdt + σ St dWt,
(4.3)
where r is the interest rate, δ the amount of dividend, σ the volatility
and Wt is a standard Wiener process, then a European option which
gives the right but not the obligation to buy the asset at expiry T, solves
the initial-boundary value problem of the Black–Scholes type
∂V
∂τ = LV = 1
2σ 2 ∂2V
∂x2 +

r −δ −1
2σ 2
∂V
∂x −rV, −∞< x < ∞, 0 ≤τ ≤T,
(4.4)
after the log transformation x = log(S/E) where E is the strike price,
τ = T −t and L represents the spatial operator. The availability of closed
form solutions has made Black–Scholes a very popular model. However,
empirical evidence showed that this model cannot capture observed mar-
ket features such as the fat tails and high peaks (asymmetric leptokurtic).
Moreover, calibration with market prices showed that the volatility is not
constant, as assumed by the Black–Scholes model and that market prices
do jump. This is why many other models consisting of jumps (Merton
1976) and stochastic volatility (Bates 1996; Heston 1993) have appeared
in the literature.
Merton (1976) was the first to explore option pricing where the under-
lying stock returns are discontinuous. For the jump-diffusion model, the
dynamics of the stock price process are obtained by adding discontinuous
Poisson jumps to (4.3) as
dSt
St
= (r −δ −λκ)dt + σdWt + (η −1)dNt,
and the Black–Scholes PDE (4.4) becomes a PIDE of the form
∂V
∂τ = 1
2σ 2 ∂2V
∂x2 +

r −δ −1
2σ 2
 ∂V
∂x −rV
+
 ∞
−∞

V(x + z,τ) −V(x,τ) −(ez −1)∂V
∂x (x,τ)

g(z)dz.
(4.5)
This is just an extension of the Black–Scholes model and allows for sud-
den price movements (jumps) that can happen even over a small time

A General Efficient Framework for Pricing Options
73
step, dt. Naturally, when the mean arrival time λ of the independent
Poisson process dNt is zero, it reduces to the simple Black–Scholes model.
Here κ = E(η −1) and (η −1) represent the impulse function causing S to
jump to Sη. For Merton’s model, the jump size distribution is assumed
to follow the normal density function
g(z) =
λ
√
2πσJ
e−(z−µJ)2/(2σ 2
J ),
(4.6)
with mean µJ, variance σ 2
J and for this model, κ can be evaluated ana-
lytically as exp(µJ + σ 2
J /2) −1. A richer model was constructed in Carr
et al. (2002) based on the density function
g(z) = Ce−Mz
z1+Y Iz>0 + CeGz
|z|1+Y Iz<0,
leading to special cases of Kou’s double exponential model (Kou 2002)
for Y = −1, the VG process for Y = 0, infinite activity models with finite
variation for Y ∈[0, 1] and infinite activity with infinite variation for
Y ∈[1,2]. It is well known that the discontinuity of the kernel at z = 0
causes a lower order of convergence for difference schemes (Almendral
and Oosterlee 2007; Wang et al. 2007). In addition, for infinite activity
models, no diffusion (σ = 0) is required for the viscosity solution to con-
verge. For a detailed discussion about jump processes, we refer to Cont
and Tankov (2004). We confine ourselves to Merton’s Gaussian distri-
bution and the CGMY process right now, but the pricing methodology
easily extends to other processes as well. When solving Equation (4.5),
the important numerical issue is that the nonlocal nature of the convo-
lution integral term present causes a dense matrix inversion for implicit
schemes. Discretization of this convolution integral results in a Toeplitz
matrix, and it is well known that fast Fourier transform (FFT) needs to
be applied for computational efficiency. Carr and Mayo (2007) observed
that for Merton’s model, part of the integral in equation (4.5) represents
the solution to a heat problem. In the next section, we will show how
the ETI framework can fully exploit this idea.
Instead of adding a jump component to the stochastic differential
equation (4.3), others have preferred to consider a nonconstant volatil-
ity. Heston (1993) proposed a model that assumes correlation with the
stock process itself. This model is very popular among researchers since
it admits a closed-form formula for European options, and it is easy
to implement. However, it results in a multidimensional convection-
diffusion equation with second-order cross-derivative. While the SV

74
Y. D. Tangman, R. Boojhawon, A. Gopaul and M. Bhuruth
models give good calibrations for longer maturities, jumps are essential
to reflect the short maturity patterns. Thus, it seems logical that the most
generic model should be a combination of both SV and jump diffusion.
The SVJ model was introduced by Bates (1996) and the stochastic dif-
ferential equations governing the asset price process S and the variance
process y ≥0 are given by
dSt
St
= (r −δ −λκ)dt + √ytdW1
t + (η −1)dNt,
dyt = α(β −yt)dt + γ √ytdW2
t ,
where W1
t , W2
t are standard Brownian motions and γ is the volatility of
yt. Following Yan and Hanson (2006), the governing two-dimensional
PIDE becomes
∂V
∂τ = 1
2y ∂2V
∂x2 + 1
2γ 2y ∂2V
∂y2 + ργ y ∂2V
∂x∂y +

r −δ −λκ −1
2y
 ∂V
∂x
+ α(β −y)∂V
∂y −(r + λ)V + λ
 ∞
−∞
[V(x + z,y,τ)] g(z)dz,
(4.7)
where ρ ∈[−1,1] is the correlation coefficient and g(z) is given by (4.6).
For λ = 0, it reduces to Heston’s SV model, and if γ is also zero, we obtain
the simple Black–Scholes model.
It is the feature of each option that characterizes the condition at expiry
and the boundary conditions at the ends of our computational domain.
For a European call option, these conditions are
V(x,y,0) = max(Eex −E,0),
Vτ (x,y,τ) = −rV(x,y,τ),
x →−∞,
Vxx(x,y,τ) = Vx(x,y,τ),
x →∞,
(4.8)
and we can use one-sided approximations for the partial derivatives in
y at the boundaries. For PDEs and PIDEs in one dimension, we simply
omit the variable y.
A barrier option depends on whether the stock price hits a barrier or
not. For example, an up-and-out-call barrier has the same payoff and
lower boundary conditions as that of a European call option except for
an upper condition at the barrier xu as
V(xu,y,τ) = 0.
Nevertheless, most traded options are of American type, and for such
options no simple analytical solution exists. An American option that

A General Efficient Framework for Pricing Options
75
can be exercised at any time up to and including maturity, gives rise to
a linear complementary problem of the form
Vτ ≥LV, V(X,τ) ≥V(X,0),
(Vτ = LV) ∧(V(X,τ) = V(X,0)),
(4.9)
where X consists of all the spatial dimensions involved, for example in
the SVJ model, X = (x,y). Therefore, for no-arbitrage to hold, the LCP
states that the value of an American option must always be at least the
payoff due to the early exercise feature.
4.3
Exponential time integration schemes
4.3.1
Black–Scholes
To describe ETI schemes, we first consider a European call option under
the Black–Scholes model. For a finite difference discretization of the
spatial derivatives in equation (4.4), we need to truncate the infinite
x-domain (−∞, ∞) to a bounded domain x = (xmin,xmax). We therefore
consider a computational grid x ⊂x defined by
x =

xi ∈ℜ: xi = xmin + ix,i = 0,1,...,m,x = (xmax −xmin)/m

,
and define the central second-order approximations to the first- and
second-order spatial derivatives with respect to x by the difference
matrices
D1
x =
1
2xtridiag[−1,0,1] and D2
x =
1
(x)2 tridiag[1,−2,1],
respectively. Then, by discretizing the Black–Scholes operator L in (4.4),
we obtain the matrix
A = 1
2σ 2D2
x +

r −δ −1
2σ 2

D1
x −rIx,
(4.10)
where Ix ∈ℜm×m is the corresponding identity matrix for x. It is easy
to implement the boundary conditions for a European call option by
setting the only element in the first row of A as A1,1 = −r and the linear
boundary condition is implemented by using the one-sided second order
approximation
Vx(xmax,τ) = Vm−2 −4Vm−1 + 3Vm
2x
,
to find the last row of D1x and then equate the last row of D2x to that
of D1x.

