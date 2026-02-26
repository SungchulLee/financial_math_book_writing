# Risk Management

!!! info "Source"
    **The Mathematics of Financial Modeling and Investment Management** by Sergio M. Focardi and Frank J. Fabozzi, Wiley, 2004.
    These notes are used for educational purposes.

## Risk Management

CHAPTER 23 
Risk Management 
R
isk means uncertainty. There is risk whenever there is uncertainty 
about future events. There are many different notions of risk. In busi-
ness, as well as in daily life, an endeavor is considered risky if it is diffi-
cult or if depends on many things that might go wrong. The notion of 
risk espoused by financial theory is that of pure probabilistic uncertainty, 
without any possibility of controlling the outcome. For example, an 
investor does not control market fluctuations. 
Though risk cannot be individually influenced it can be managed by 
diversification and risk transfer. The idea of transferring and reducing 
risk is not new. As observed in Chapter 1, the practice of insurance and 
of risk reduction through diversification was already well established in 
the Middle Ages. Diversification is an intuitive idea, easily conveyed by 
the saying, “Do not put all your eggs in the same basket.” 
However, the modern idea of measuring risk and of selectively 
transferring carefully calibrated portions of risk had to wait the devel-
opment of modern probability theory. As seen in Chapter 3, the founda-
tion of probability theory as a sound mathematical discipline was 
achieved only around 1930. 
The development of the mathematical theory of risk, initiated by 
Lundberg (see Chapter 3), led to the practice of modern insurance and 
to the development of the insurance business. Insurance is deeply rooted 
in the notion of diversification: Individuals protect themselves by pool-
ing risks together. If the number of uncorrelated risks is large, individual 
risk becomes negligible. 
In recent years, financial firms and insurance companies have taken 
the concept of risk management further in three different directions: (1) 
by recognizing that the shape of risk is an important determinant of the 
risk-return trade-off; (2) by engineering contracts able to transfer 
737 

738 
The Mathematics of Financial Modeling and Investment Management 
selected portions of risk; and (3) by trading these contracts. From a sta-
tistical point of view, a key innovation is the attention paid to the ratio 
between the bulk of the risk and the risk of the tails. The latter has 
become a key statistical determinant of risk management policies. 
Within the realm of finance, one has to make a broad distinction 
between the management of risk in investment management and in 
banking and finance at large. As we have seen in the previous chapters, 
investment management is essentially a question of determining a prob-
ability distribution of returns and engineering the optimal trade-off 
between risk and return as a function of individual preferences. There-
fore, risk management is intrinsic to investment management. 
The risk management function, which is often associated with the 
investment management process, has the objective of (1) controlling risk 
when the investment process is not fully automated; (2) taking into con-
sideration special risks such as the business or operational risk; and (3) 
controlling the global risk, especially the tails of the risk. 
Banks and financial firms, however, engage in financial operations 
other than pure investing. Many of these operations are profitable but 
risky and their risk must be managed or eliminated. For instance, a 
financial firm offering a customized derivative instrument to a client 
assumes a risk that, in itself, might be suboptimal or excessive. Hence, 
the need to transfer all or part of this risk to the market at large. The 
risk management function controls this process. 
The possibility of effectively controlling and managing risk depends 
on the availability of instruments that allow for the transfer of risk. A 
market is called complete if there are instruments able to cover any trad-
able risk. 
In this chapter we discuss market completeness, risk measures, and 
the notion of coherence of risk measures, and then present risk models 
and their use in investment management. We begin the chapter with the 
concept of market completeness because it is a necessary condition for 
effective risk management. We first introduced this concept in Chapter 
14, where we covered arbitrage pricing. 
MARKET COMPLETENESS 
In finance, the effectiveness of risk management is essentially related to 
the degree of market completeness. In a complete market any individual 
risky position can be completely hedged, that is, its risk can be com-
pletely eliminated by purchasing appropriate contracts. In intuitive 
terms, this means that any payoff, intended as a random variable, can 

Risk Management 
739 
be replicated by engineering appropriate portfolios. In other words, 
there is a market, and therefore a price, for every contingency. 
Markets in which this hedging is not possible are called incomplete 
markets. In incomplete markets there are contingencies that are not 
traded and cannot be priced and replicated. An investor who “owns” 
one of these contingencies is stuck with them and has no assurance that 
a buyer will be found. An incomplete market might be completed by 
adding appropriate assets provided that they are tradable. If the market 
is completed, every contingency becomes tradable. However, there is no 
guarantee that an arbitrary market can be completed. 
The question of market completeness is fairly complicated. There 
are two key aspects in the notion of market completeness: (1) the math-
ematics of market completeness and (2) the economic rationale as to 
why markets are complete or can be completed. We discuss each below. 
The Mathematics of Market Completeness 
The purely mathematical aspect of the completeness of a given market 
model is a widely studied subject. Some market models are complete 
while others are not. For instance, a market where stock prices evolve as 
geometric random walks and a risk-free asset is available is complete. 
On the other hand, a market represented by a stochastic volatility model 
is incomplete. 
A market is complete if any cash flow stochastic process can be rep-
licated by an appropriate self-financing trading strategy with some ini-
tial investment. Replication means that the self-financing trading 
strategy and the original cash flow process are equal processes. Recall 
that in Chapter 6 on probability theory we defined four notions of 
equality between stochastic processes. The weakest condition of equal-
ity requires that two processes have the same finite-dimensional distri-
butions. This concept of equality is insufficient to define replication. 
The strongest condition of equality requires that two processes have the 
same paths except for a set of measure zero. Replication requires that 
the original cash flow process and the replicating self-financing trading 
strategy are equal processes in this strongest sense. 
Recall also from Chapter 10 that there are two types of solutions of 
stochastic differential equations: strong solutions and weak solutions. 
Strong solutions are solutions built on given Brownian motions while 
weak solutions include their own Brownian motion. This notion, which 
might look abstract and remote, is however important from the point of 
view of a replicating strategy. If a replicating process is defined by a sto-
chastic differential equation, the difference between strong and weak 
solutions is important. 

740 
The Mathematics of Financial Modeling and Investment Management 
Market completeness entails that there is a core of price processes 
such that any cash flow stream can be engineered as a time-varying, but 
self-financing, portfolio made up of the core price processes. For example, 
in a complete market a complex derivative instrument can be replicated 
by a portfolio of simpler instruments. A bank that creates a credit deriva-
tive can always hedge its positions. 
As we have seen in Chapter 14 on arbitrage, in the finite-state, one-
step case, market completeness means that the number of linearly inde-
pendent price processes is equal to the number of states. In other words, 
a market is complete if there are as many linearly independent price pro-
cesses as states of the world. This notion can be easily expressed in 
terms of linear algebra. In the finite-state, discrete-time case the above 
conditions must be replaced by the notion of dynamically complete mar-
kets as assets can be traded at intermediate dates. In fact, the number of 
linearly independent price processes can be smaller than the number of 
states provided that assets can be traded repeatedly. As shown by Dar-
rell Duffie and Chi-Fu Huang1 and Hua He,2 what is needed, in this 
case, is that there are as many linearly independent price processes as 
there are branches leaving a node in the market information structure. 
Based on this, it can be demonstrated that the binomial model and its 
extension to multiple variables are complete. 
When we proceed to the continuous-state, continuous-time case this 
notion looses meaning. In this case there is a continuum of states and a 
continuum of instants. The infinite number of trading instants allows 
markets to be complete even if they are formed by a finite number of 
securities. There are restrictions to ensure that a market model is com-
plete. A fundamental theorem assures that, in the absence of arbitrage, 
market completeness is associated with the uniqueness of the equivalent 
martingale measure. In a complete market the equivalent martingale 
measure is unique, while an incomplete market is characterized by infi-
nite martingale measures. This happens because there are contingencies 
that cannot be priced by arbitrage. 
The condition of market completeness is violated in many important 
models. Two, in particular, have attracted attention: jump-diffusion mod-
els and stochastic volatility models. Jump-diffusion models are models 
formed by diffusions plus processes where finite jumps occur at random 
times, such as at those times represented by a Poisson process. Stochastic 
1 Darrell Duffie and Chi-Fu Huang, “Implementing Arrow-Debreu Equilibria by 
Continuous Trading of Few Long-Lived Securities,” Econometrica 53 (1985), pp. 
1337–1356 
2 Hua He, “Convergence from Discrete to Continuous Time Contingent Claims Pric-
es,” Review of Financial Studies 3, no. 4 (1990), pp. 523–546. 

Risk Management 
741 
volatility models are models where prices are diffusion processes but the 
volatility term is driven by a separate process. In discrete time, all models 
make jumps while stochastic volatility models become the ARCH and 
GARCH models. Let’s briefly discuss completeness in relation to stochas-
tic volatility models. 
A standard geometric-diffusion model is complete as there is a 
unique equivalent martingale measure Q (see Chapter 15) under which 
the model can be written as 
dSt = rStdt + σStdBt 
where r is the risk-free rate, σ is the volatility constant, and B is a stan-
dard Brownian motion. If a stock price follows this model, any contingent 
claim can be uniquely replicated. In particular, options can be replicated 
as a portfolio formed with the stock and the risk-free asset. Options are 
redundant securities. Anyone who has underwritten an option can com-
pletely hedge its risk by constructing an appropriate self-financing repli-
cation strategy. 
The same reasoning can be applied in the case of N geometric 
Brownian motions. In this case, there is still a unique equivalent martin-
gale measure under which the model can be written as 
N 
i 
j
j
dSt = rSt
idt + ∑σjStdBt 
j = 1 
Suppose now that volatility is not constant but that it is a time-
dependent process. The simplest two-factor, stochastic-volatility model 
can be written, in the physical probability measure, as 
dSt = µStdt + σtStdBt 
dσt = a St, σt)dt + b St, σt)Bt
( 
(
σ 
σ
where Bt is another standard Brownian motion eventually correlated 
with Bt. In this case, however, there are infinite equivalent martingale 
measures in which the model can be written as 
dSt = rStdt + σtStdB˜ t 

742 
The Mathematics of Financial Modeling and Investment Management 
( 
˜ σ
dσt = a˜ (St, σt )dt + b St, σt )dBt 
The above stochastic volatility model can be completed3 by adding 
an asset Yt = C(t,σt,St) that follows the following process: 
( , 
ˆ
dYt = rYtdt + F t YtSt )dBt 
ˆ
where Bt is another Brownian motion eventually correlated with the 
other two. Note that mathematically there is an infinite family of these 
models. 
The question of what model applies to a new asset introduced for 
completing the market is an empirical one. Note that this new asset is 
contractually defined as a function of the stock price. In practice it is an 
option. The market will price the new asset according to some economic 
pricing principle which is not, however, a principle of absence of arbi-
trage. In this completed market, the underwriter of an option can com-
pletely hedge his/her position. However, the hedging will not be the 
same as in the case of constant volatility. 
Similar considerations can be repeated for the jump-diffusion mod-
els. Suppose that a lognormal diffusion is given. Consider a Poisson 
point process and add a finite jump to the diffusion at every occurrence 
of the Poisson process. The resulting model is generally incomplete. 
However, it can be completed by adding appropriate contracts. What 
type of contracts must be added in each case is not a trivial question. 
The Economics of Market Completeness 
In discussing market completeness it should be kept in mind that market 
completeness means that any risk can be completely hedged. In modern 
markets, hedging is typically achieved by taking positions in appropri-
ate contracts such as options or other derivative instruments. In this 
way risk is transferred to other entities and hedged. The key question is: 
why should there be other entities willing to take the opposite side of a 
risky position? 
Beside the mathematical details, this is the essence of market com-
pleteness. It means that there is always someone willing to trade, at a 
market price, any contingent claim. It is important to reconcile this 
notion with that of mathematical completeness. Let’s use the simple 
example of European stock options in a market with a risk-free asset 
3 M.H.A. Davis, Complete-Market Models of Stochastic Volatility, forthcoming in 
Proc. Royal Society London (A). 

Risk Management 
743 
and where stock prices evolve as geometrical Brownian motions. This is 
a complete market. Therefore any European option can be perfectly rep-
licated by a portfolio of the underlying stock plus the risk-free asset. 
In this market, investors can protect themselves from excessive 
losses by purchasing options. However, in case of large losses someone 
has to foot the bill. The risk transfer process is the following. Suppose 
that an investor who owns a stock wants to buy protection against large 
price movements of the stock by purchasing an option. In this way the 
owner of the stock transfers the risk of eventual large movements to the 
underwriter of the option. The underwriter might decide to bear the risk 
or to transfer the risk by purchasing an appropriate self-financing strat-
egy. In the latter case, the risk of large movements has been transferred 
in two steps from the initial investor to the option underwriter and then 
back to the market. 
In case of large negative movements, there will be a transfer of 
money from owners of long stock positions to the original investor who 
sought protection. The transfer will occur through the mechanism of 
short positions. It would be a mistake to think that by replication every-
one comes out of large negative market movement unscathed. In this 
case, in particular, if options are properly hedged, the final losers are 
those who hold stock positions without hedging them. 
Suppose, now, that price processes follow stochastic volatility dynam-
ics. In this case, markets are incomplete and options cannot be perfectly 
hedged. The key difference with respect to the previous case is that the 
underwriter of the options has to foot the bill of eventual large losses. In 
this case, underwriting options is a risky business, while in the previous 
case, ultimately the risk is borne by stock owners or stock “lenders.” 
In the case of stock markets, risk does not disappear in aggregate. 
Total market capitalization fluctuates and there is no way that this glo-
bal risk can be eliminated. In fact, on a global scale, no one profits if 
markets move down or loses if markets move up. Profits and losses of 
short and long positions are only local relative losses. In aggregate, 
investors lose if markets go down and gain if markets go up. 
However, the market as seen by each individual investor might be 
complete or not as a function of the dynamics of price processes. Com-
pleteness dictates that risk can be arbitrarily apportioned but does not 
change the fact that massive losses might occur in aggregate. In other 
markets, however, there is a level of aggregation at which risk does not 
exist or is very small. In this case, hedging has a different rationale as 
for each movement there are winners and losers. Hedging is a stabiliza-
tion device as risk can be mutually exchanged. In this case, market com-
pleteness acquires a different meaning. In fact, in a complete market, 

744 
The Mathematics of Financial Modeling and Investment Management 
risk can be eliminated by market mechanisms, while in an incomplete 
market this is not possible. 
It should be clear that the economic rationale for risk management 
is different in different cases. There are essentially three possibilities. 
First, risk can be transferred to firms that engineer a diversification ser-
vice. Insurance companies are the typical example. This means that 
diversification is possible; that is, in the aggregate the residual risk is 
very low simply because there are many uncorrelated events. For 
instance, the residual risk of significant short-term fluctuations of the 
average age of a population is very low except in exceptional cases (e.g., 
war or natural catastrophes). Thus life insurance is a statistically sound 
business. 
Second, risk can be transferred to “speculators” (e.g., persons or 
entities who have a different risk-return profile or an information 
advantage). Essentially, risks exist in aggregate but there are entities 
willing to make bets on some portions of it. Note that if markets were 
not correlated, there would be no risk in aggregate. 
Third, risk can be transferred because there are positions that offset 
each other in a true economic sense. In other words, there are “natural 
hedges.” This means that the fluctuations of some basic variables create 
simultaneous gains and losses approximately of the same size. This is 
the case of interest rates. There are other cases, with more or less com-
plete natural hedges. 
WHY MANAGE RISK? 
The basic motivation for risk management is financial optimization. In 
this sense, the motivation for risk management has to be found in the 
basic tenet of investment management: optimization of the risk-return 
trade-off. 
Financial optimization implies that a risk return trade-off indeed 
exists. If some risk can be eliminated in aggregate, the market cannot 
remunerate it. Therefore the assumption of that risk is always subopti-
mal and it should be eliminated. This is the case when risk can be diver-
sified away and when there are natural hedges, as in the case of interest 
rates. 
As risk management means the transfer of risk from one entity to 
another, clearly if there is risk in aggregate there are limits to the size of 
the risk management business. This is the case of the stock option busi-
ness. There is no natural hedge to stock market movements, at least 
none has been discovered thus far. No financial agent profits from mar-

Risk Management 
745 
ket plunges, so only small optimization adjustment is possible. There-
fore there are natural limits to the size of coverage that can be offered. 
On the other hand, in the case of interest rates if one entity loses 
another gains and risk transfer is effective. 
In fact, the elimination of interest rate risk forms the bulk of risk 
management. According to the U.S. Office of the Controller of the Cur-
rency Quarterly Derivatives Report, interest rate derivatives made up 
86% of all derivative contracts in the second quarter of 2003. Foreign-
exchange contracts were the second-largest category of derivatives, 
making up about 11% of all derivatives in the same period while equity, 
commodity, and credit derivatives made up about 3% of all contracts. 
Note that the size of the bond and equity markets are comparable. The 
huge notional volume of interest rate derivatives is partially due to for-
mal duplication of traded contracts. For instance, in a number of cases, 
instead of selling a swap agreement it might be easier to create a new 
swap agreement with opposite cash flows. Formal duplication, however, 
is possible just because there is no risk in aggregate. 
The situation would be different for an entity that had the ability to 
make reliable forecasts. Banks as well as industrial firms hedge interest 
rates because they do not feel sufficiently comfortable with interest rate 
forecasts. Unable to make sufficiently safe bets they prefer to eliminate 
the risk. Hence the huge market for covering interest rates fluctuations. 
RISK MODELS 
A risk model is a mathematical model of prices, returns, rates, and even-
tually other quantities that allows one to determine the probability dis-
tribution of the total value of portfolios held by a financial institution. 
Many different models have been proposed in different areas of finan-
cial risk. Let’s discuss each of them. 
Market Risk 
Perhaps the best known model of market risk is RiskMetrics, initially 
proposed by JP Morgan in 1994 and now commercialized by the Risk-
Metrics Group. Over 100.000 physical copies of the RiskMetrics soft-
ware are now in use at banks and asset management firms.4 
4 Information on the company and technical details on the product are available and 
can be downloaded from the RiskMetrics Group web site www.riskmetrics.com. 
Since inception JPMorgan has made technical details on the product broadly avail-
able. The RiskMetrics Group has continued this practice. 

746 
The Mathematics of Financial Modeling and Investment Management 
The basic idea of RiskMetrics is to represent the entire set of returns 
and rates as a multivariate normal variable. In other words, RiskMetrics 
is made up of a simple linear model with some robust estimation tech-
nique. JPMorgan provided daily the estimates of volatilities and correla-
tions essentially using empirical volatilities and correlations. Over the 
years the initial model has been extended to cover more complex cases, in 
particular derivative instruments. A suite of models for banks and asset 
managers is commercialized by The RiskMetrics Group. 
Multifactor models are often used to evaluate the market risk of 
equity portfolios. Commercially available models such as Barra or APT 
are now in use at many asset management firms to evaluate market risk. 
However, if portfolios include derivative instruments, multifactor mod-
els must be completed with additional modeling tools able to capture 
the behavior of these instruments. 
Risk models are often based on the idea of creating a relatively small 
number of scenarios, that is, paths of the key financial and economic 
variables. The Toronto-based firm Algorithmics pioneered the use of sce-
nario-based risk management as a commercial software implementation. 
Credit Risk 
Credit risk models are inherently more complex than market risk mod-
els as the normal distribution is not a good approximation of default 
distributions. A number of models have been proposed, in particular 
CreditRiskMetrics from the RiskMetrics Group. This model is based on 
an underlying process for ratings. Credit Suisse proposed an actuarial 
credit risk model, Creditrisk+ that represents default distributions as a 
mixture of Gaussians. Models of credit risk based on option theory have 
been proposed by the firm KMV which is now part of Moody’s. 
Kamakura Corporation has proposed models of credit risk based on the 
work of Robert Jarrow. Credit risk models were covered in Chapter 22. 
Operational Risk 
Operational risk can be broadly defined as risk related to processes; it 
generally falls under the responsibility of internal auditors or their 
equivalents, but in a number of instances it is under the responsibility of 
the risk manager. Determining its contribution to portfolio risk varies 
from firm to firm. Some firms attribute to human error (e.g., changing 
the benchmark and not informing) up to 75% of portfolio risk. 
Large investment banks such as the former Bankers Trust and Credit 
Suisse First Boston pioneered a quantitative approach to operational risk 
several years ago, but the data problem is more severe in asset management 

Risk Management 
747 
than in investment banking. Many asset management firms consider the 
occurrence of losses due to operational risk to be irrelevant. 
RISK MEASURES 
Risk is embodied in a probability distribution of returns or of possible 
losses. From a management point of view it is interesting to collapse this 
probability distribution in a single number. The problem of measuring 
risk with a single number has received much attention, even in contexts 
other than finance. 
Historically, the first measure of the risk contained in a distribution 
is its variance, or the standard deviation, which is the square root of the 
variance. The variance of a distribution gives an indication as to 
whether the distribution is concentrated around some value or spread 
over a large interval of values. If the standard deviation of a distribution 
is high, it means that there is a high probability that the variable might 
take values significantly different from its mean. A high standard devia-
tion, therefore, corresponds to a high risk. In the terminology of risk 
management, standard deviation represents unexpected loss (UL). 
Because risk is uncertainty (lack of information), the question of the 
information conveyed by a probability distribution has led to the con-
cept of information and to Information Theory. In the case of finite 
probabilities, information (I) in the sense of Information Theory is 
defined as the average of the logarithms of probabilities (pi): 
N 
I = ∑ pilog pi 
i = 1 
Information reaches its maximum when the probability is concen-
trated in only one outcome, that is, pi = 1 for i = k, pi = 0 for i ≠ k. In 
this case information is zero as the information of an outcome with 
probability zero is conventionally set to zero. Information reaches its 
minimum when all probabilities are equal, that is, when there is maxi-
mum uncertainty on the future outcome. In this case information is neg-
ative: I = –N log N. There is no lower bound to information. 
Information with a minus sign is well known in statistical physics as 
entropy, which is a measure of disorder: E = –I. The information associated 
with an equi-probable binary scheme, that is, the information associated 
with the choice between two equally probable possible outcome, is called 

748 
The Mathematics of Financial Modeling and Investment Management 
bit. As information is additive, it represents the number of bits necessary to 
characterize a choice. 
This definition of information can be extended to a continuous 
probability distribution. However, in the continuous case, information 
looses its meaning.5 For this and for other reasons, information cannot 
be used effectively as a measure of risk.6 
When JP Morgan released its RiskMetrics model in 1994, it proposed 
a measure of risk called Value at Risk (VaR).7 Defined as a confidence 
interval, VaR is the maximum loss that can be incurred with a given prob-
ability. Suppose we choose a confidence level of 95%. We say that a port-
folio has a given VaR, say $1 million, if there is a 95% probability that 
losses above $1 million will not be incurred. This does not mean that the 
given portfolio cannot lose more than $1 million, it means only that 
losses above $1 million will happen with a probability of 5%. If we trans-
late probabilities into relative frequencies, this means, in turn, that losses 
above $1 million will happen approximately 5 times every 100. If we 
measure VaR daily this means 5 days out of 100 days. 
As a measure of risk, VaR has many drawbacks. It does not specify 
the amount of losses exceeding VaR. Different distributions might have 
the same VaR but totally different distributions of extreme values. For 
instance, in the above example of a VaR of $1 million at 95%, 5 times 
every 100 a portfolio might lose just above $1 million or a much larger 
amount. Perhaps the most serious drawback of VaR is the fact that it is 
not subadditive. The VaR of aggregated portfolios might be larger than 
the sum of individual VaRs. This is unreasonable as one expects risk to 
decrease in aggregate due to diversification and anticorrelations. Despite 
these drawbacks, and despite the fact that confidence intervals are ulti-
mately a rather complex probabilistic concept, VaR has become 
extremely popular as a risk measure. 
In 1998 Artzner, Delbaen, Eber, and Heath8 published an important 
paper where they defined the conditions for risk measures to be coher-
5 This fact is well known in statistical physics where the entropy associated with a 
continuous scheme is somewhat arbitrary. 
6 The pioneering work of Arnold Zellner has started a new strain of econometric lit-
erature based on Information Theory. See Arnold Zellner, “Bayesian Method of Mo-
ments (BMOM) Analysis of Mean and Regression Models,” in J.C. Lee, W.D. 
Johnson, and A. Zellner (eds.), Prediction and Modeling Honoring Seymour Geisser 
(New York: Springer, 1994), pp. 61–74. 
7 Note that RiskMetrics and VaR are not related. The concept of VaR can be applied 
to any probability distribution of return and not only to RiskMetrics. 
8 Philippe Artzner, Freddy Delbaen, Jean-Marc Eber, and David Heath, “Coherent 
Measures of Risk,” Mathematical Finance 9 (1999), pp. 203–228. 

Risk Management 
749 
ent. A coherent risk measure must satisfy a number of properties includ-
ing sub-additivity conditions, monotonicity conditions, risk-free 
conditions, and diversification conditions. To solve the problems inher-
ent in the noncoherence of VaR, Artzner et al. proposed a coherent mea-
sure of risk known as expected shortfall (ES); Rockafellar and Uryasev9 
call the measure conditional VaR (CVaR). The ES at a given confidence 
level α is defined as the expected loss given that the loss exceeds VaR at 
the confidence level α. If the loss distribution is continuous, the VaR and 
the ES or CVaR can be written as follows. 
VaR at the 100(1 – α) percent confidence level is the upper 
100α percentile of the loss distribution. If we denote the 
VaR at the 100(1 – α) percent confidence level as VaRα(L), 
where L is the random variable of loss, then the expected 
shortfall at the 100(1 – α) percent confidence level ESα(L) 
is defined by the following equation: 
(
) = E L
ESα L
[ 
L ≥VaRα L
(
)] 
If the distribution is not continuous, the definition of ES is slightly 
more complicated. Acerbi and Tasche,10 and Rockafellar and Uryasev 
provide a thorough discussion of the definitions of ES and CVaR under 
different distributional assumptions. It can be demonstrated that at the 
same confidence levels, the ES and VaR are equivalent measures for nor-
mal distributions in the sense that ES can be inferred from VaR and vice 
versa. However other distributions, and in particular those with fat-
tails, might exhibit the same VaR but different ES and vice versa. It has 
been demonstrated that ES is a coherent risk measure while VaR is not. 
Yamai and Yoshiba11 offer a comparison of ES and VaR under a number 
of assumptions. 
9 Tyrrell R. Rockafellar and Stanislav Uryasev, “Optimization of Conditional Value- 
at-Risk,” Journal of Risk 2, no. 3 (2000), pp. 21–41. 
10 Carlo Acerbi and Dirk Tasche, “On the Coherence of Expected Shortfall,” work -
ing Paper, Center for Mathematical Sciences, Munich University of Technology, 
2001. 
11 Yasuhiro Yamai and Toshinao Yoshiba, “On the Validity of Value-at-Risk: Com -
parative Analyses with Expected Shortfall,” Monetary and Economic Studies 20, no. 
1 (published by Institute for Monetary and Economic Studies, Bank of Japan, 2002), 
pp. 57–86. A number of papers discuss the use of ES as a risk measure in portfolio 
optimization. See, for example, Rockafellar and Uryasev, “Optimization of Condi -
tional Value-at-Risk.” 

750 
The Mathematics of Financial Modeling and Investment Management 
A different way of measuring risk consists in computing different pos-
sible scenarios and defining risk as the maximum loss that can be incurred 
in any of these scenarios. This technique is used in the SPAN system devel-
oped by the Chicago Mercantile Exchange which computes 16 scenarios, 
two of which are extreme scenarios. Risk is the largest maximum loss in 
the 14 scenarios or 35% of the loss in the two extreme scenarios. 
The idea of analyzing risk under different scenarios is widely used in 
practice, often together with quantile measures such as VaR. Extreme 
scenarios can be computed in different ways, in particular with the use 
of Extreme Value Theory (EVT), which we covered in Chapter 13. As 
we noted in that chapter, and as we will see in the following sections, 
the use of EVT is still in its infancy. 
Risk measures can be seen, from a different point of view, as sensitivi-
ties to given factors. In this case, rather than capture the uncertainty of a 
given distribution it captures the amount of fluctuation of a given quantity 
as a function of the fluctuations of another quantity. We have already 
encountered most of these measures. In the analysis of stock prices, the 
coefficients of factor models, the betas, capture the sensitivity of returns to a 
number of factors. As we have seen in Chapters 11 and 12 on financial 
econometrics, sensitivities apply to a static as well as to a dynamic frame-
work. A dynamic framework is generally represented as a state-space model. 
In the analysis of bond prices, duration captures the sensitivity of 
bond prices to parallel shifts in the term structure of interest rates. Con-
vexity, which is defined as the first derivative of duration, captures the 
sensitivity of bond prices to the curvature of the term structure. 
In the analysis of derivative instruments, a number of sensitivities 
are used to capture the sensitivity of their prices to changes in different 
parameters. These sensitivities are usually indicated with specific Greek 
letters. Hence, they are called the “Greeks.” The most common Greeks 
are listed below: 
Vega 
Theta 
Delta 
Gamma 
Sensitivity to a 
Sensitivity to a 
Sensitivity to a 
Linearized rate 
change in 
change in time 
change in the 
of change of 
volatility 
remaining 
price of underlying 
delta 
A concept related to risk measures is the Sharpe ratio developed by 
William Sharpe.12 Sharpe himself called this ratio the “Reward to Vari-
12 William F. Sharpe, “Mutual Fund Performance,” Journal of Business (January 
1966), pp. 119–138; and William F. Sharpe, “Adjusting for Risk in Portfolio Perfor-
mance Measurement,” Journal of Portfolio Management (Winter 1975), pp. 29–34. 

Risk Management 
751 
ability Ratio.” The Sharpe ratio is to evaluate expected returns in a risk-
weighted framework. Given a portfolio, the ex ante Sharpe ratio is 
defined as the ratio between the expected excess return (measured rela-
tive to the risk-free rate) and volatility: 
Expected return – Risk-free rate 
Sharpe ratio = ---------------------------------------------------------------------------------
Standard deviation of return 
A number of other measures similar to the Sharpe ratio have been 
introduced, in particular the Sortino ratio13 which uses only downside 
volatility. 
A variant of the Sharpe ratio commonly used to assess the perfor-
mance of a portfolio manager is the information ratio. The information 
ratio is the ratio of the excess return over a designated benchmark 
divided by the tracking error, the standard deviation of the difference 
between portfolio return and the benchmark market (see Chapter 19). 
The excess return over the benchmark is referred to as the “alpha” or 
“active return.” The information ratio is typically calculated on an ex 
post basis as follows: 
Portfolio return – Benchmark return 
Information ratio = ---------------------------------------------------------------------------------------------
Tracking error 
RISK MANAGEMENT IN ASSET AND PORTFOLIO MANAGEMENT 
Risk has different facets in asset and portfolio management. In particu-
lar, risk can be characterized as (1) market risk; (2) risk of underperfor-
mance relative to a benchmark; or (3) business risk. Ultimately, risk is 
market risk. The question is: Who bears it? Asset management firms 
define their risk as the risk of underperformance relative to a bench-
mark: the client assumes the market risk implicit in the portfolio; the 
asset manager assumes the benchmark risk. However, the asset manage-
ment function is concerned essentially with market risk. 
Some nuance is required. If a firm manages the assets of the parent 
company (e.g., an insurance company or investment bank), it is exposed 
to market risk as an investor. Also, volatility of returns or a loss of cap-
ital might be unacceptable to some institutional or retail investors, forc-
13 See Frank Sortino and Robert Van Meer, “Downside Risk,” Journal of Portfolio 
Management (Summer 1991), pp. 27–32. 

752 
The Mathematics of Financial Modeling and Investment Management 
ing asset managers to accept market risk as they devise guaranteed-
return funds or convex strategies to protect the investor against down-
side risk. The type of quantitative methods used and the extent of risk 
modeling is largely determined by the risk—relative or absolute—that 
the asset management firm is exposed to; other important factors 
include the prevailing culture and the competitive environment. 
Some asset management firms are now defining their risk more 
broadly as business risk. Market risk and the failure to deliver a mandate 
are only two facets of business risk. Others include process flows and 
fraud and come under the general heading of operational risk. Opera-
tional risk has been moved up on the agenda by management consultants 
and, more recently, by the European Commission with proposals to 
extend to the asset management subsidiaries of larger financial organiza-
tions the new Basel rules on capital charges to cover business risk. 
Factors Driving Risk Management 
One of the major contributions of quantitative methods to asset man-
agement is widely considered to be in the area of risk. For the more 
quantitatively-oriented firms, ex ante risk measurement has enabled 
risk-return optimization as prescribed by modern finance theory, the 
dynamic management of risk, and the ability to handle structured prod-
ucts; for others, it means the ability to “look back” on risk. 
Several factors are behind the focus on risk:
 ■ Regulatory and reporting frameworks have put risk on the agenda of 
institutional investors.
 ■ Pension consultants are pressing for more measures of risk and tying 
performance to risk. 
■ Growing sophistication on the part of trustees and institutional inves-
tors is also a driver behind the demands for risk measures including 
VaR.
 ■ The growing complexity of assets in portfolios (e.g., global assets, 
structured products) is adding to risk and the need to monitor and con-
trol it.
 ■ The recent volatility in both asset classes and investment styles is 
increasing the need to monitor tracking error in an effort to limit 
downside risk.
 ■ The contribution risk modeling makes in defining mandates. 
Risk Measurement in Practice 
In practice, as noted previously, a whole battery of risk measures are 
being used. A number of considerations can be made. The more complex 

Risk Management 
753 
the probability distribution, the more measures required. Over a period 
of several months—a typical time horizon for asset management—distri-
butions are assumed to be Gaussian and that one risk measure suffices. 
But phenomena such as volatility clustering, trend reversals, large move-
ments, and structural breaks produce distributions that are not Gaussian. 
There is a need to measure what might happen at the extremes. It is not 
infrequent that single risk measures such as variance or VaR are being 
complemented by scenario analysis to evaluate the risk of extreme move-
ments. 
In addition, a single measure might not be equally appropriate for 
all investment styles. For example, firms focused on emerging markets 
might use information ratios, which reflect returns on assets, to comple-
ment tracking error. Multiple measures might be required by (institu-
tional) clients. Tracking error and information ratios or volatility are 
considered standard in some markets and an increasing number of cli-
ents are asking for VaR. VaR is required in managing funds for endow-
ments and foundations with a statutory requirement to generate positive 
returns; in Germany, VaR measures are now regulatory for funds man-
aging the investments of depository institutions. Multiple measures 
might be requested by fund managers themselves, in an attempt to 
improve their performance. 
In some instances, it’s important to understand in absolute terms 
how much money might be lost. This is the case with guaranteed-return 
funds or funds being managed for the parent company, for example, an 
insurance firm or investment bank. A few firms are using EVT; the 
objective is to ensure the ability to survive a market crash. One might 
want to be able to take into account different aspects or different views. 
VaR allows a uniform measure of risk across asset classes. Though with 
time horizons of 2–3 months volatility clustering phenomena disappear, 
ARCH-GARCH models are being used at some firms to gain an under-
standing of the clustering of risk. 
Getting Down to the Lowest Level 
Risk and performance are increasingly being measured at lower levels. 
Instead of looking at sector levels (e.g., geographical areas, currency or 
industry sector), firms are beginning to look at the single-asset level. 
While most firms are not there yet, this is the declared goal. 
There is also a tendency at producing risk numbers daily, with daily 
reporting to fund managers, monthly to management, and (typically) 
quarterly to clients. Investment consultants and regulators consider it 
fundamental that asset managers be aware of the risk at all times, but 
not everyone agrees that crunching out the numbers daily is appropriate 

754 
The Mathematics of Financial Modeling and Investment Management 
for all funds. Among the concerns voiced is the fact that risk measure-
ment loses significance if the covariance matrix is changed daily. Also, if 
the wrong measure is used, its use on a daily basis might exacerbate the 
problem, leading to a too frequent rebalancing of portfolios. 
Regulatory Implications of Risk Measurement 
To protect the financial system and, ultimately, the broad public of 
investors, financial intermediation and asset management are highly reg-
ulated, though regulations governing risk management are different for 
banks and asset management firms. In many countries, an asset manage-
ment firm’s procedures are highly regulated; the firm must exhibit mini-
mum requisites of financial prowess, the ability to process transactions, 
and moral qualities of its management. Asset managers are also required 
to demonstrate the ability to measure risk and to communicate to the 
investor the level of risk implied by their management. 
Risk management has strong regulatory implications, especially for 
banks. Banks are obliged to keep an amount of liquid and safe capital to 
shoulder eventual adverse market movements. The amount of bank 
reserves is subject to strict regulation. There are many facets related to 
the amount of reserve capital that banks are obliged to maintain. Con-
sider that the amount of liquid bank reserves is a fundamental quantity 
in the process of money creation and the management of the monetary 
mass. A new dimension of the reserve management process is the man-
agement of the ratio between the amount of risky capital and the 
amount of safe reserves. The modern view of this aspect is that regula-
tors decide the desired ratio between risky capital and safe reserves but, 
under appropriate conditions, let banks measure the amount of risk they 
are running with internal measurement systems. This is a substantial 
novelty with respect to the past when banks where obliged to keep a 
fixed percentage in liquid reserves. The point of view of the U.S. Federal 
Reserve is that 
By substituting banks’ internal risk measurement models 
for broad, uniform regulatory measures of risk exposure, 
[the new rule] should lead to capital charges that more 
accurately reflect individual banks’ true risk exposures.14 
14 Darryll Hendricks and Beverly Hirtle, “Bank Capital Requirements for Market 
Risk: The Internal Models Approach,” Federal Reserve Bank of New York, Eco-
nomic Policy Review (December 1997). 

Risk Management 
755 
Clearly banks must show the ability to measure risk which the Fed-
eral Reserve prescribes measuring as VaR. The Federal Reserve then 
controls the quality of a bank’s ability to forecast adverse movements. If 
adverse movements occur more frequently than anticipated by a given 
bank’s risk management system, then that bank is obliged to increase its 
liquid reserve. The implications of these new regulations from both the 
business and the macroeconomic points of view will be analyzed in the 
coming years. 
SUMMARY
 ■ Diversification and risk transfer through financial engineering are the 
key tools of risk management.
 ■ Estimating the shape of loss distributions is central to modern financial 
risk management.
 ■ A market is complete if every possible contingency can be traded.
 ■ In a complete market, risk can be perfectly hedged.
 ■ Multivariate geometric diffusion models are complete.
 ■ Stochastic volatility models are not complete, but can be completed.
 ■ If risk does not exist in aggregate, it can be eliminated; if it exists in 
aggregate, it can only be transferred.
 ■ Off-the-shelf market and credit risk models are commercially available.
 ■ Risk can be measured in numerous ways: unexpected loss, value-at-
risk, expected shortfall, and sensitivities.
 ■ Client demand and management push are behind the growing use of 
risk management in investment management. 


Index 
Abramowitz, Milton, 249 
Absolute summation, 289, 293 
Abstract factors, 534–537 
Accounting 
issues, 5–6 
surplus, 40 
Accrued interest, 53 
Accumulation point, 100 
Acerbi, Carlo, 749 
Active bond strategies, 651 
Active investing, 566–577 
bottom-up approaches, 567–568 
top-down approaches, 566–567 
Active management. See Full-
blown active management 
fundamental law, 568–571 
risk factor mismatches, 650 
Active portfolio 
management, passive portfolio 
management 
(contrast), 
552–553 
return, 569 
strategy, 6. See also High-risk 
active portfolio strategies 
Active return, 552, 554, 751 
Active reward-to-active risk, 570 
Active risk, 579, 582 
decomposition, 579–580 
Active systematic-active residual risk 
decomposition, 580–581 
Actual tracking error, 555 
Addition operation, 154, 157–158 
ADF. See Augmented Dickey-
Fuller 
Adjoint operation, 159–160 
Adjustment models, 285 
Adler, R.J., 355, 389 
Agent decision-making process, 
determinant, 167 
Aggregation, distribution iden-
tity, 386 
AIC. See Akaike Information 
Criteria 
Aigner, D.J., 334 
Akaike, H., 318 
Akaike Information Criteria (AIC), 
318 
Aldous, David, 327 
Alexander, Carol O., 344, 545, 
565 
Algebra, 169–173, 183–185. See 
also Matrices 
sequence, 226 
Algorithms, development, 16 
Alpha, 552, 576, 751 
Amaral, Luis A.N., 390, 522 
American options, 65, 68 
valuation, 429 
American securities, valuation, 429 
American Stock Exchange (AMEX/ 
ASE), 46 
Analytic tractability, absence, 695 
Andersen, T.G., 346 
Anderson, Philip W., 380 
Annual tracking error, 554 
Anson, Mark J.P., 679, 695, 710, 
714, 734 
Anticipation, admitting, 224 
Antidiagonals, 145–146 
Antinomies, 93 
Aoki, Masanao, 309, 538 
Aoyama, H., 388 
Approximation schemes, usage, 264 
APT. See Arbitrage pricing the-
ory; Asset pricing theory 
Arbitrage, 89–90. See also Sta-
tistical arbitrage 
absence, 84–85, 414, 467, 605 
implications, 467 
arguments, 60, 66, 68–69 
usage, 607 
avoidance, 640 
models, 634. See also No-
arbitrage models 
opportunities, 431, 711 
absence, 434 
recognition, 606 
principle, 393–395 
profits, obtaining, 64 
Arbitrage pricing, 89, 393, 441. 
See also Continuous time; 
Continuous-state contin-
uous-time; Discrete-time 
continuous-state setting; 
Multiperiod 
finite-state 
setting; One-period set-
ting 
computation, 445 
development. See Continuous-
state arbitrage pricing 
models, 511 
payoff rate, 466–467 
principle, 446 
Arbitrage pricing theory (APT), 
76, 88–89, 396, 529 
models, 435–438 
testing, 436–438 
Arbitrage-free market, 433 
Arbitrage-free models, equilib-
rium models (contrast), 
634–635 
Arbitrage-free pricing, theory, 639 
Arbitrage-free value, 606 
spot rates, usage. See Bonds 
ARCH 
behavior, 574 
method, 547 
models, 12, 286, 288 
usage, 345–347, 741 
processes, 312, 382–383 
ARDL. See Auto Regressive 
Distributed Lag; Autore-
gressive Distributed Lag 
ARIMA. See Autoregressive inte-
grated moving average 
Arithmetic Brownian motion, 
279, 280, 326, 447 
Arithmetic random walk, 326, 
340 
ARMA. See Autoregressive mov-
ing average 
Arrays. See Ordered arrays 
Arrow, Kenneth, 180 
Arthur, W.B., 380 
Artificial probability measure, 414 
Artzner, Philippe, 748 
Asset allocation decision 
application, 494–507 
inputs, 495–499 
Asset pricing theory (APT) mod-
els, 335 
Asset-backed securities (ABSs), 
4, 55, 653 
Asset/liability management, over-
view, 39–40 
Asset/liability problem, 43 
Assets. See Nonreproducible assets; 
Reproducible assets 
allocation model, extensions, 
507–508 
757 

758 
Index 
Assets (Cont.) 
cash distribution, 69 
classes, 3–4. See also Tradi -
tional asset classes 
inclusion, 503–507 
return distribution, 508 
volatility, 752 
complexity, 752 
covariance, 514 
defaulting, 728 
probability, 725 
expected return, 87 
inputs, requirement, 7–8 
liquidity, 27 
management, 13 
risk management, usage, 
751–755 
market value, 40 
package, 393 
position. See Underlying asset 
price, 67 
cointegration, evidence, 344 
riskiness, 24 
selection, 2. See also Invest -
ment management process 
methodologies, 324 
types, 42 
value, influence, 63 
volatility, 694 
Asymmetric risk, 66 
Asymptotic normality, 376 
Asymptotically self-similar sta -
tionary sequence, 388 
Atlantic options, 65 
Attraction, domain, 361 
Augmented Dickey-Fuller (ADF) 
test, 312–313, 340 
Augmented matrix, 150 
Autocorrelation, 287 
function, 382. See also Time- 
independent autocorrela -
tion function 
Autocovariance function, 302. 
See also Time-dependent 
autocovariance function 
Autocross 
correlations, 
evi -
dence, 344 
Autopredictive model, 285 
Autoregressive case, 298 
Autoregressive Distributed Lag 
(ARDL), 342, 540 
Autoregressive equation, 296 
Autoregressive form. See Infi -
nite autoregressive form 
Autoregressive integrated moving 
average (ARIMA), 152, 300 
process, 301 
Autoregressive models, 288. See 
also Vectors 
combination, 333 
Autoregressive moving average 
(ARMA), 297, 311–312, 
379 
models, 304–305, 317. See 
also Nonstationary multi-
variate ARMA models; 
Nonstationary univariate 
ARMA models; Station-
ary multivariate ARMA 
models; Stationary univari-
ate ARMA models 
processes, 299–302, 548. See 
also Heavy-tailed ARMA 
processes 
representation, 297–305 
equivalence, 308–309 
stationary processes, 300 
Autoregressive 
representation. 
See Causal autoregres-
sive representation; Time 
series 
Axiomatic set theory, 93 
Axiomatic system, 166 
Axiomatic theory, 165. See also 
Probability 
Bachelier, Louis, 75, 78–79, 81, 
326 
Backward-looking tracking errors, 
558, 651 
forward-looking tracking errors, 
contrast, 555–556 
Bader, Lawrence N., 508 
Bagehot, Walter, 31 
Baillie, R., 344 
Balance sheet, usage, 685 
Bamberg, G., 353 
Bank/dealer counterparties, 717 
Bankers Trust, 746 
Banz, Rolf, 520 
Barbell portfolio, 671 
Barra, 578, 581 
E3 factor model, 582 
fundamental multifactor risk 
model, 533 
Barrier option, 695 
Barrier structural model, 694–696 
Basis points, 125 
Basket, 50 
default probability, 721 
default swaps 
pricing model, 718–721 
valuation, 718–734 
market. See Default basket 
market 
model, 720 
pricing. See Credit default swaps 
swaps. See First-to-default 
basket swap; Second-to- 
default basket swap 
Basu, Sanjoy, 520 
Bauer, D., 345, 538, 544 
Bayesian Information Criteria 
(BIC), 318 
Bayesian statistics, 316 
Beebower, Gilbert, 494 
Behavioral finance, 502 
Belief, intensity, 165 
Bellman, R., 214 
Bellman’s Dynamic Program -
ming, 214 
Benchmarks. See Nonliability 
driven entities 
characteristics, 5 
establishment, 2 
exposure, 657 
index, 4, 651. See also Portfo -
lios 
risk profile, 553 
volatility, 558 
risk, 579, 582, 751 
volatility, impact, 556–560 
Bermuda options, 65 
Bernardo, Josè M., 316 
Bernoulli, Jacob, 100 
Bernoulli distribution. See Joint 
Bernoulli distribution 
Bernstein, Peter L., 75, 526 
Berry, Michael A., 436 
Beta, 524–525 
characteristics, 565 
distributions, 367 
portfolio. See Zero-beta port -
folio 
usage, 517, 530–533 
Bias-variance trade-off, 376 
Bid-ask spread, 23, 30, 64, 575 
charge. See Dealers 
dealer charge, 28 
establishment, 31 
Billingsley, Patrick, 173 
Binomial models, 423–427 
one-period interval, 699 
risk-neutral probabilities, 426– 
427 
Birge, J.R., 202 
Bivariate diffusion, 729 
Bivariate normal, 196 
probability functions, 693 
Black, Fischer, 69, 76, 89–90, 
451, 477, 499, 521, 637, 
638, 684, 695 
Black box, 307 
representation, 307 
Black-Derman-Toy Model, 635, 
638 
Black-Karasinski Model, 635, 
637–638 
Black-Scholes equation, 260 
Black-Scholes 
option 
pricing 
formula, 446, 449–452 
Girsanov theorem, applica -
tion, 462–463 
Black-Scholes-Merton 
(BSM) 
Model, 684–690 
implications, 690 
Blanchard, O.J., 334 
Block trades, 50 
Bogey, establishment, 2 
Bohr, Niels, 444 
Bollerslev, Tim, 344, 346, 382 

Index 
759 
Bond equivalent yield (BEY), 
597, 608 
Bond valuation. See Cash flow 
equation, 122 
formulas, 112–113 
continuous time, 618–623 
option valuation, relation-
ship, 626–627 
Bondholders, options, 56 
Bonds, 21, 51–56 
agreed-upon price, 53 
analysis, application, 112– 
120, 122–126 
arbitrage-free value, spot rates 
(usage), 606 
convexity measure, 125 
coupon rate, 52–55 
market index, contrast. See 
Management 
maturity, 51–52 
options, term structure mod-
eling/valuation, 593 
par value, 52 
payment provisions, 55–56 
portfolio 
management, 40, 122, 649 
optimization, 674 
strategies, relationship. See 
Tracking errors 
prices, observation, 701 
pricing equation, 643 
refunding, 56 
risk-free nature, 453 
term structure modeling/valu- 
ation, 593 
term to maturity, 51 
yield to value (usage), limita -
tions, 602–603 
Book/market factor, 520 
Book/price ratios, 532 
Bootstrapping, 603 
approach, 377 
Borel algebra, 175 
Borel sets, 170. See also n- 
dimensional Borel sets 
Bossaerts, Peter, 539, 574 
Bottom-up 
approaches. 
See 
Active investing 
Boudhaud, J.-P., 329 
Boundary conditions, 454 
Boundary values, 254 
Bounded elementary function, 
233–234 
Bounded variation, 105–106, 129 
Box algebra, 273 
Box-Jenkins methodology, 318 
Brace, Alan, 644 
Brace-Gatarek-Musiela (BGM) 
Model, 643–644 
Brennan, Michael J., 638 
Brinson, Gary L., 494 
Briys, Eric, 695 
Broad-based bond market indexes, 
649 
Brock, W., 574 
Brock, W.A., 258, 259 
Brokers 
commissions, 28, 83 
function, 29 
loan rate, 49 
role. See Real markets 
Bromwich integral, 135 
Brownian motion, 221, 227. See 
also Arithmetic Brown -
ian motion; Fractional 
Brownian motion; Geo -
metric Brownian motion 
binomial approximation, 675 
correlation, 742 
defining, 219 
definition, 225–230 
extremes, calculation, 79 
filtration, 460 
finite dimensional distribu -
tions, 179 
functional, computation, 313 
increments, 223 
modifications, 628 
paths, 230 
properties, 230–232 
stochastic differential equa -
tion, 628 
usage, 455 
Bryson, M.C., 353 
Buetow, Jr., Gerald W., 635 
Buffet, Warren, 567 
Bullet maturity, 55 
Burmeister, Edwin, 436 
Burr distribution, 366 
Businesses, classification, 34–35 
Buy-and-hold strategy, 564 
Cadlag functions, 227 
Calculus. See Variations 
fundamental theorem, 132– 
133 
principles, 91 
usage. See Variables 
Calculus of variations. See Vari-
ations 
Call feature, 55 
Call option, 686 
buyer, 71 
exercising, 55 
price, 69 
Call protection, 56 
Callable bond, 55 
value, 117 
Campbell, John Y., 327, 344, 
345, 574 
Canonical Brownian motion, 229 
Capital 
expenditures, 45 
structure, 84 
Capital Asset Pricing Model 
(CAPM), 86–87, 334, 
511. See also Condi -
tional CAPM; Multifac -
tor CAPM 
assumptions, 512–513 
Black modifications, 521–522 
empirical tests, findings, 520 
Merton modifications, 521– 
522 
random matrices, relation -
ship, 522–523 
role. See Investment 
testing, 518–523 
tests, critique, 520–521 
usage, 478, 529, 684 
Capital gains, taxes, 28, 83 
Capital market, 25 
transaction costs, 29 
Capital market line (CML), 477– 
482 
derivation, 478–481 
empirical analogue, deriva -
tion, 518–519 
empirical implications, 519 
equation, 518–519 
risk premium, 482 
usage, 484. See Optimal port -
folio 
Capitalization (Cap), 54. See also 
Markets 
agreements, 26 
approach, 564 
portfolio, 558 
stocks, 3 
Caps, 70–71 
Captive finance companies, 35 
Captured value, 551 
Cartesian space. See n-dimen- 
sional Cartesian space 
Cash 
derivative instruments, con-
trast, 25 
distribution. See Assets 
equivalents, 3 
instruments, 85 
market price, 62–64 
outlays, 395 
descriptions, 38 
payments, anticipation, 68 
product, 711 
reinvestment. See Excess cash 
risk-free return, 559 
Cash and carry trade. See Reverse 
cash and carry trade 
Cash flow 
package, bond valuation, 603 
predictability, 22, 24 
present value, 604 
production, 38 
rate. See Continuous cash flow 
reinvestment, 598–599 
stream. See Continuous cash 
flow 
Cash flow matching (CFM), 664– 
667 
formulation, 665 
framework, 669 
Cash-settlement contracts, 57 
Categorization variables, 563 
Cauchy distribution, 366 

760 
Index 
Cauchy initial value problem, 
260, 263 
Causal autoregressive represen -
tation, 299 
Causal time series, 289 
Cell matching, 650 
Cellular method, 564 
Central auction specialist sys -
tems, 45–46 
Central limit theorem, 358–360 
Cerchi, Marlene, 574 
Certificate of deposit (CD), 38. 
See also Fixed-rate CD; 
Floating-rate CD 
issuance, 43 
Chain rule, 109. See also Inte -
gration 
application, 115–118 
Chaitin, Gregory J., 318 
Change, instantaneous rate, 91 
Chaos, 256–259. See also Non -
linear dynamics 
characteristics, 257–258 
Characteristic equation, 161, 
298. See also Inverse 
characteristic equation 
Characteristic 
function. 
See 
Variables 
Characteristic line, 517 
estimation, 518 
Characteristic polynomial, 161 
Chartists, 571 
Cheapest to deliver 
asset, 63 
concept, 681 
Chen, Nai-Fu, 436 
Chen, Ren-Raw, 679, 695, 700, 
701, 710, 711, 714, 722, 
724, 734 
Chobanov, G., 389 
Choudhry, Moorad, 632, 633, 
679, 695, 710, 714, 734 
Chow, Yuan Shih, 174, 193 
Christensen, Peter F., 664, 667 
Cizeau, P., 329 
Claims. See Seasoned claims 
contrast, 25 
maturity, 25 
Clark, P.K., 383 
Classical economic theories. See 
Term structure 
Clean price, 53 
Clearinghouse 
association, 59 
purpose, 57–58 
Client-designated benchmark, 40 
Client-imposed constraints, 5 
Closed-end funds, sale, 42–43 
Closed-form 
solutions, 
693, 
703. See also Ordinary 
differential equations 
Clustering, 562 
Coefficient matrix, 150 
rank, 400 
Coefficient of determination. 
See Determination 
Coefficients, restrictions (absence), 
296 
Coherent risk measure, 749 
Cointegrated indexes, search -
ing, 577 
Cointegrated models, 286 
Cointegrated systems, estima- 
tion/testing, 543–544 
Cointegration, 12, 339–345. 
See also Index; Polyno-
mial cointegration; State-
space cointegration 
approach. See Dynamic Coin-
tegration Approach 
definition, 341 
empirical evidence. See Equity 
equivalence, 541 
evidence, 545. See also Assets 
financial time series, relation -
ship, 544–546 
Cointegration-based strategies, 574 
Collective risk problem, 80 
Collins, Bruce M., 33 
Colored noise, 379 
Column rank, 151–153 
Column vectors, 142 
Commercial mortgages, 653 
Commissions, 33. See also Bro -
kers 
Commodity, price, 53–54 
Commodity futures, 57 
Commodity Futures Trading Com -
mission (CFTC), 57, 65 
Common factor risks, 578 
Common risks, 582 
Common stocks, 3, 21, 42, 45– 
51. See also Non-U.S. 
common stocks 
common trends, multifactor 
models (usage), 529 
institutional investors, 50–51 
orders, types, 48–49 
trading 
arrangements, 48–51 
locations, 45–46 
Common trends, 341, 344. See 
also n-r common trends 
searching, 577 
Common-trend cointegrated model, 
543 
Company specific effect, 722 
Company-specific risk, 515 
Complete markets, 399–402 
equivalent Martingale mea-
sures, usage, 463 
Complex matrix, 145 
Complex numbers, definition, 143 
Component zero-coupon instru -
ments, total value, 603 
Composite function, 101, 109, 
129 
Compound option, 690–691 
model. See Geske compound 
option model 
Compound return, 325 
Computer-based 
optimization 
theory, 82 
Computer-generated 
indepen -
dent arithmetic random 
walks, 544 
Computers, price-performance 
ratio, 11–12 
Conditional CAPM, 511, 523–524 
Conditional default probability, 701 
Conditional distributions, 284 
Conditional expectation, 184– 
186, 197, 630 
Conditional order, 48 
Conditional probability, 184–186 
definition, 78–79 
Conditional VaR (CVaR), 749 
Consensus investors, 566 
Constant interest rates, convexity, 
120 
Constant terms, 150 
Constrained optimization prob -
lem, 476 
Consumption 
CAPM, 511 
infinite stream, 493 
process, 404 
Continuity, 103–105 
Continuous cash flow 
rate, 620 
stream, 622 
present value, 640 
Continuous compounding, 112– 
113 
Continuous function, 103–104. 
See also Discontinuous 
function; Left continuous 
function; Right continu-
ous function 
Continuous quantities, 99 
Continuous spot rate curve, 
construction, 605 
Continuous time. See Bonds; 
Interest rates 
arbitrage principle, 441–445 
usage, 608 
Continuous time-path, 223 
Continuous trading, 443 
Continuously compounding con -
stant interest rate, convex -
ity, 120 
Continuous-state arbitrage pric -
ing, development, 430 
Continuous-state continuous-time 
arbitrage pricing, 445–446 
models, 441 
Continuous-state setting, 430, 442 
Radon-Nikodym derivative, 
usage, 465 
Continuous-time finance, 445 
Continuous-time Markov pro -
cess, 79 

Index 
761 
Continuous-time processes, 284 
Continuous-time white noise, 268 
Continuum, 99 
Contracting costs, 37 
Contrarian strategies, 576 
Contribution risk modeling, 752 
Control theory, 213. See also 
Optimal control theory 
Convergence, interval, 122 
Convertibility, 22 
Convertible bonds, 22, 56 
Convexity. See Constant interest 
rates; Continuously com-
pounding constant interest 
rate; Variable interest rates 
measure. See Bonds 
Convolution, 136–137, 193 
closure property, 355 
product, 291 
Copula functions, 188–189, 732–733 
Corporate bonds. See High-yield 
corporate bonds; Invest-
ment-grade corporate bonds 
Correlated default processes, mod -
eling process, 722–734 
Correlated random walks, 285– 
286 
Correlation, 327–329. See also 
Moments/correlation; 
Returns 
coefficient, 188–189, 195–196, 
328 
default time correlation, com -
parison. See Defaults 
definition, 187 
factors, 433 
matrix, 433 
Cost-effective diversification, 36 
Counterparty 
risk, 69, 718, 720. See also 
Default swap 
analysis, 696 
exposure, 70 
swap payments, 70 
Counting measure, 372 
Coupon 
payment, 52 
interval, 620 
rate. See Bonds 
Coupon-paying instruments, 623 
Covariance, 8. See also Returns; 
Variables 
definition, 187–188 
matrix, 147, 276, 328, 654 
change, 754 
usage, 658 
Covered call, 686 
Cowles, Alfred, 81 
Cowles Commission, 81 
Cox, D.R., 371 
Cox, John C., 69, 616, 637, 
695, 709 
Cox process, 697 
Cox-Ingersoll-Ross (CIR) Model, 
635, 637, 709 
Cramer, Harald, 80 
Cramer-Rao bound, 319–320, 322 
Cray supercomputer, usage, 11 
Credit default swaps, 679–683. 
See also Senior basket 
credit default swaps; Sub-
ordinate 
basket 
credit 
default swaps 
baskets, pricing, 734 
pricing. See Single-name credit 
default swaps 
formulation, 714 
termination value, 680 
value, 713–715 
Credit derivatives, legal docu-
mentation, 683 
Credit event, 680 
Credit risk, 59, 746 
management, 711 
Credit risk modeling, 679 
reduced form models, 696–710 
structural models, 683–696 
Credit risk Value-at-Risk (CrVaR), 
391–392 
Credit risk-based capital require-
ments, 5 
Credit Suisse First Boston, 746 
Creditor, definition, 51 
Creditrisk+, 746 
CreditRiskMetrics, 746 
Critical point, 203 
Cross acceleration, 683 
Cross default, 683 
Csake, F., 318 
Cumulative distribution function, 
175, 352 
Cumulative normal probability, 687 
Cumulative payoff rate processes, 
444 
Cumulative tracking error, cal -
culation, 658 
Currency, 22 
swap, 70 
Currently callable issue, 55–56 
Dacorogna, M.M., 377, 389 
Dahl, Henrik, 491, 666 
Daniel, Kent, 344 
Danielsson, J., 377 
Dantzig, Georg, 82, 201 
Darboux-Young approach. See 
Integration 
Data generation process (DGP), 
285, 332, 345 
modeling, 378 
nonlinear function, 547 
schemes, 547 
Database query functions, devel-
opment, 16 
Datini, Francesco, 10 
Davis, M.H.A., 742 
DAX, 70 
Day convention, 681 
de Haan, L., 377 
de Varenne, Francois, 695 
de Vries, C.G., 377 
Dealers 
bid-ask spread charge, 83 
role. See Real markets 
DeBondt, Werner, 572 
Debreu, Georges, 75 
Debt 
contract, 700 
default probability, 692 
market, 25 
obligations, investment. See 
Short-term debt obliga -
tions 
value, 688 
Debt instruments, 22. See also 
One-period debt instru-
ment 
definition, 180 
valuation principles, 594–595 
Dechert, W.D., 259 
Decision making, management 
structures, 14 
Dedicated portfolio strategy, 664 
Default basket market, 719 
Default basket swap contract, 718 
Default prediction, 711 
Default probability, 689. See 
also 
Forward 
default 
probability 
curves, 711 
equation, 691–692 
forward curve, 685, 711 
Default swap, 719 
contract, total protection value, 
715 
counterparty risk, 717–718 
delivery option, 716 
tenor, 734 
valuation. See Baskets 
value, 718 
Default time 
correlation, 730–733 
distribution, 698 
Defaultable zero-coupon bond, 696 
Default-free payoff, 707 
Defaults 
correlation, default time cor-
relation 
(comparison), 
733–734 
distribution, specification. See 
Joint defaults 
processes, modeling process. 
See Correlated default 
processes 
Deferred call, 55 
Defined contribution plan, 42 
Dekkers, A.L.M., 377 
Delbaen, F., 467 
Delbaen, Freddy, 748 
Deliverable obligation, 680 
Delivery option. See Default swap 
Delta, 117 
Dembo, Ron, 672 
Dempster, A.P., 348 
Demsetz, Harold, 29, 30 

762 
Index 
Densities 
Fourier transform, 192–193 
process, 465. See also Equiva-
lent Martingales 
Depository institutions, 43–44 
investments, 753 
Derivative instruments, 26, 70, 
85, 742 
contrast. See Cash 
value, 423 
Derivatives, 21. See also Higher 
order derivatives; n par-
tial derivatives 
application. See First deriva-
tive; Second derivative 
computation, rules, 107–111 
market, 26 
pricing, 12, 89. See also Inter- 
est rates 
valuation. See European sim-
ple derivatives 
Derivatives (calculus), 91 
Derman, Emanuel, 638. See also 
Black-Derman-Toy Model 
Descriptive metafile, 16 
Descriptors, 532 
Determinants, 148–149 
Determination, coefficient, 518 
Deterministic environment, 218, 640 
Deterministic equivalents, 676 
Deterministic series, 296 
Deterministic short-term inter- 
est rates, 619 
Deterministic trend, 309 
Dhrymes, Phoebus J., 436 
Diaconis, Persi, 327 
Diagonal matrices, creation, 161– 
162 
Diagonal 
variance-covariance 
matrix, 534 
Diagonalization/similarity, 161–162 
Diagonals, 145–146. See also 
Antidiagonals 
matrices, 146–147 
Dickey-Fuller (DF) test, 312– 
313. See also Augmented 
Dickey-Fuller test 
Diebold, Francis X., 346, 378 
Difference equations, 239. See 
also Recursive difference 
equations 
Difference method. See Finite 
difference method 
Difference quotient, 106, 255 
Difference stationary series, 310 
Differentiable function, 106–107 
Differential equations, 239. See 
also Linear differential 
equation; Ordinary dif-
ferential equations; Par-
tial differential equations; 
Stochastic 
differential 
equations 
definition, 240 
degree, 241 
first-order system, 243 
general solution, 242–243 
solution, 92 
Differentiation, 92, 106–111 
rule. See Termwise differenti-
ation 
Diffusion 
equation, 259–261 
solution, 261–263 
invariance principle, 461–462 
models. See Spread-based dif-
fusion models 
volatility, 447 
Dimensional distributions, 228 
Dimensionality 
curse, 345 
reduction, 309 
Dimensions, generalization, 276–278 
Dimitriu, Anca, 344, 545 
Dirac delta, 228 
function, 628 
Dirac measure, 371 
Direct investments, 35–36 
Discontinuous function, 104–105 
Discount bond. See Pure risk- 
free discount bond 
Discount factor. See Risk-free 
discount factor 
Discount function, 606–607, 625 
Discrete probabilities, 171 
Discrete quantities, 99 
Discrete random variables, col -
lection, 407 
Discrete random walk, 225 
Discrete-state discrete-time envi -
ronment, 623 
Discrete-state discrete-time setting, 
445 
Discrete-time 
continuous-state 
setting, arbitrage pricing, 
430–434 
Discrete-time models, 283 
Discrete-time processes, 671 
Discretization scheme, 263 
Disjoint additivity. See Probability 
Distances, 96–100 
Distributed sequences. See Identi -
cally distributed sequences; 
Independent 
distributed 
sequences 
Distributions, 174–175. See also 
Fat-tailed 
distributions; 
Max-stable distributions; 
Stable distributions 
functions, 174–175 
law, 175 
Distributive properties, 159 
Diversifiable risk, 515, 525 
Diversification, 36, 472–474. 
See also Cost-effective 
diversification 
quantification, 472 
usage, 81 
Dividends 
factor, 520 
payment, 49 
usage, 45 
yield, 519 
Divisibility/denomination, 22 
Dodd, David, 567 
Dollar convexity, 119, 122 
Dollar duration, 113–114, 122 
Domain of attraction. See Attraction 
Dorfleitner, D., 353 
Dow Jones Industrial Average 
(DJIA), 46–47, 545 
Dow Jones-Reuters, 17 
Down-and-out barrier option, 695 
Downside dollar, 502 
Downside risk, 66 
Drees, H., 377 
Duda, Richard O., 562 
Duffie, Darrell, 625, 685, 687, 
696, 706, 729, 740 
Duffie-Singleton Model, 697, 
706–710 
Duration. See Dollar duration; 
Effective duration; Rate 
duration 
usage, 115–116 
Durlaf, S.N., 380 
Dynamic cointegration, 540 
Dynamic Cointegration Approach, 342 
Dynamic market models. See Returns 
Dynamic models. See Prices 
Dynamic nonlinear self-rein- 
forcing cascades, 380 
Dynamic trading, 427 
Dynkin, Lev, 651, 652, 654, 
656, 657, 660, 662, 663 
EAFE index, 497–498 
EAFE international equity, 504–506 
Earnings growth. See Estimated 
earnings growth 
Earnings yield, 589 
Eber, Jean-Marc, 748 
Econometrics, 337–338. See also 
Financial econometrics 
models, 511 
Economic activity, 593 
Economic behavior, quantitative 
laws, 76–78 
Economic growth rate, 175 
Economic modeling, 11 
Economic quantities, 168. See 
also Time-variable eco-
nomic quantities 
Economic theories. See Term 
structure 
Economic value, 66–67 
Economic variables, prima facie 
trends, 287 
Econophysics, 78 
Edwards, Mark, 551 
Effective duration, 118 

Index 
763 
Efficiency. See Semistrong effi-
ciency; Strong-form effi-
ciency; Weak efficiency 
Efficient frontier, 473. See also 
Markowitz efficient frontier 
Efficient markets, 85–86 
theory, 79 
Efficient portfolios, 472. See 
also Markowitz efficient 
portfolios 
set, 474 
solving, 499 
Eichhorn, David, 507 
Eigenvalues, 
160–161, 
293– 
294, 330. See also Vari-
ance-covariance matrix 
number, 343, 522–523 
Eigenvectors, 160–161, 332 
usage, 523, 536 
Electronic communication net-
works (ECNs), 46 
Electronic transactions, diffu-
sion, 12–13, 76, 284 
Elementary functions, 222, 233. 
See also Bounded ele-
mentary function 
stochastic integral, definition, 234 
Elements. See Matrices 
Embedded call option, 116 
Embedded option, value, 117 
Embrechts, Paul, 80, 189, 329, 
353, 355, 385, 388 
Empirical analogue, derivation. 
See Capital market line 
Empirical data, 167 
Empirical distribution function, 370 
Employee Retirement Income 
Security Act (ERISA) of 
1974, 42 
Empty sets, 95 
Endowments, 45 
Endpoint. See Right endpoint 
Engle, R.F., 334, 346, 540, 543, 
548 
Engle-Granger method, 543 
Enhanced index portfolio, 554 
tracking error, 555 
Enhanced indexing, 9, 553 
matching risk factors, 650 
minor risk factor mismatches, 
650 
strategy, 650 
Entities, classification, 34–35 
Entropy, 747 
maximization, principle, 492 
Equality constraints, 207, 211 
Equality modulo sets, 179 
Equilibrium market price. See Risk 
Equilibrium models, 637 
contrast. See Arbitrage-free 
models 
Equilibrium system. See General 
equilibrium system 
Equilibrium theories. See Gen-
eral Equilibrium Theories 
Equity 
claim, 22 
indexes, types, 93–94 
investment styles, 560 
log-price processes, set, 544 
long-term expected return, 508 
management, depth/goodness, 
569 
market, 25 
portfolio management, 551 
process, integration, 551–552 
prices, cointegration (empiri-
cal evidence), 343–345 
REIT, 587 
securities, 45 
volatility, 694 
Equity styles 
classification system, 562–564 
management, 560–564 
types, 560–562 
Equivalent Martingales, 89–90 
measures, 414–415, 446, 457– 
463 
density process, 419 
usage, 455, 468. See also 
Complete markets; State 
prices 
Equivalent probability measures, 
concept, 415 
Error Correction Model (ECM), 
341–342 
usage, 539 
Error term, 559. See also Non-
factor error term 
Estimated earnings growth, 532 
Estimation, 315, 373–378, 384–385 
Estimator. See Hill estimator; 
Pickand estimator 
efficiency, 319–320 
unbiasedness, 319–320 
Euclidean length. See Vectors 
Euclidean space, 169. See also n-
dimensional 
Euclidean 
space; Three-dimensional 
Euclidean space 
Euler, Leonard, 213 
Euler approximation, 250, 645 
Euler condition, 493 
Euler-Lagrange equation, 213 
European call options, valuation, 
69 
European derivative instrument, 429 
European options, 65, 68, 447, 639 
pricing, generalizing, 452–454 
European simple derivatives, 
valuation, 427–429 
European stock options, 742–743 
Events. See Outcomes/events 
algebra, 441 
dynamic nonlinear self-rein-
forcing cascades, 380 
indicator function, 729 
Ex ante Markowitz efficient 
frontier, 520 
Ex ante tracking error, 556 
Exceedances, 
point 
process, 
371–373, 373 
Excess cash, reinvestment, 664 
Excess return. See Total excess 
return 
Excess risk. See Total excess risk 
Exchange rate, 70 
Exchangeable bond, 56 
Exchange-imposed restrictions, 
28, 83 
Exchange-traded option, 65 
Execution 
costs, 33, 64 
measurement, 34 
speed, 32 
Exercise options, 65 
Exercise price, 64 
Existence, theorem, 274 
Exogenous factors, 532–534, 546 
Expansion periods, 347 
Expectation. See Conditional 
expectation; 
Homoge-
neous expectations 
theories, 613–618. See also 
Local expectations theory; 
Pure expectation theory; 
Return-to-maturity expec-
tations theory; Unbiased 
expectations theory 
Expectation Maximization (EM) 
algorithm, 348 
Expected excess return, 751 
Expected return, 7. See also 
Future expected return 
volatility, 68 
Expected shortfall (ES), 749 
Expected Shortfall Risk (ESR), 391 
Expiration date, 64 
Explanatory model, 285 
Exponential distribution, 698 
eXtensible 
Markup 
Language 
(XML), development, 16–17 
Extra-market risks, 88 
Extra-market sources, 87 
Extremal events, 353 
Extremal random variables, 365 
Extreme point, 209 
Extreme value distributions. See 
Generalized extreme value 
distributions; 
Standard 
extreme value distributions 
Extreme Value Theory (EVT), 
353, 373, 491–492. See 
also 
Independent 
and 
identically distributed 
applicability. See Finance 
usage, 750 
Fabozzi, Frank J., 33, 82, 85, 494, 
497, 500, 503–508, 532, 
556–558, 582, 583, 586, 
588, 590, 635, 637, 664, 
667, 679, 695, 710, 714, 
734. See also Kalotay Will-
iams and Fabozzi Model 

764 
Index 
Fabozzi (Cont.) 
(ed.), 494, 497, 500, 503–508, 
532, 551, 552, 557, 558, 
582, 583, 586, 588. 590, 
593, 610, 632, 633, 649– 
652, 656, 657, 662–664 
Face value, 52 
owning, 686 
Factiva, usage, 17 
Factor variance-covariance matrix, 
values, 577 
Factors, 87, 336. See also Abstract 
factors; Exogenous factors 
analysis, 338 
determination, 532–537 
market, 21 
models, 286, 335–338 
realizations, 654 
Falconer, J., 385 
Fama, Eugene F., 31, 85–86, 326, 
344, 481, 519, 520, 523 
Fat tails, 258, 351–353 
evidence. See Financial vari-
ables 
Fat-tailed distributions, 232, 351, 
353–358 
generation, 383 
Fat-tailed IID sequences, 380 
Fat-tailed innovations, 382 
FEA (firm), 12 
Feasible basic solution, 209 
Feasible region, determination, 207 
Feasible set, 473 
Federal Reserve (Fed), Board of 
Governors, 50 
Feldman, R.E., 355, 389 
Feynman-Kac formula, 627–632 
application, 631 
extension, 634, 640 
Filter rules, 571 
Filtration, 182–184 
concept, 225–226 
usage, 226 
Finance, extreme value theory 
(applicability), 391–392 
Finance 
theory, 
probabilistic 
theory, 181 
Financial assets, 21–24 
creation, assistance, 35 
illiquidity, impact, 24 
issuers, 37 
overview, 21 
tax status, 24 
transformation, 35 
Financial businesses, 34–35 
Financial decision-making appli-
cations, automation, 18 
Financial econometrics, 283, 315, 518 
models, 259 
Financial engineering, history, 10 
Financial futures, 57 
Financial instrument, 57 
Financial intermediaries 
function, 35 
liabilities, issuance, 36 
role, 35–37 
Financial markets, 21, 25–34 
buyers/sellers, interaction, 26 
classification, 25–26 
economic functions, 26–27 
futures, role, 63–64 
overview, 21 
probabilistic representation, 
180–181 
Financial modeling, milestones, 75 
Financial models, 17 
Financial obligation, 51 
Financial optimization, 744 
Financial theory, connection, 539 
Financial time series 
linear models, 324 
nonstationary models, 345–348 
relationship. See Cointegration 
stylized facts, 286–288 
Financial variables 
fat tails, evidence, 388–390 
prima facie trends, 287 
Finite difference method, 249–256 
Finite variation, 105–106 
Finite-dimension distributions, 
set, 458 
Finite-dimensional distributions, 
284, 739 
Finite-state models, 393 
Finite-state probability, 417 
Finite-state setting, 403 
arbitrage pricing. See Multi-
period finite-state setting 
Finite-variance case, 382 
Finite-variance random vari-
able, 452, 463 
Firm size factor, 520 
Firm-value models, 684 
First boundary value problem, 260 
First Crusade (1095-1099), 10 
First derivative, application, 113–115 
First-order conditions. See Port-
folios 
First-order immunization condi-
tions, 672 
First-order linear equation, 250 
First-to-default basket, 718–719 
price, 725, 727 
swap, 681 
Fischer, S., 334 
Fisher, L., 667 
Fisher information matrix, 320, 
322 
Fisher score function, 322 
Fisher-Tippett theorem, 364 
Fixed income instruments, 22 
Fixed income market, 25 
Fixed-income portfolio manage-
ment, 8 
Fixed-income trading, calibra-
tion, 698, 699 
Floating point operations per 
second (flops), 11 
Floating-rate CD, 39 
Floating-rate securities, 53 
Floors, 54, 70–71 
agreements, 26 
Focardi, Sergio, 13, 15 
Fokker-Planck equation, 628– 
629 
Fong, Gifford, 507 
Fons, Jerome, 690 
Foreign stocks. See Non-U.S. 
foreign stocks 
developing/emerging, 4 
Forni, M., 334 
Forward contracts, 26, 57–64 
contrast. See Futures contracts 
Forward curve. See Default 
probability 
Forward default probability, 712– 
713 
Forward Kolmogorov equation, 
628–629 
Forward LIBOR interest rate, 644 
Forward operator (F), 289–290 
Forward rates, 607–608 
continuous case, 625–626 
curve. See Short-term for-
ward rates 
Forward-looking tracking errors, 
558, 651, 661–662 
contrast. See Backward-look-
ing tracking errors 
Fourier integrals, 262 
Fourier transforms, 134, 137– 
138. See also Densities; 
Inverse Fourier transform 
Foward default probability, 701– 
702 
Fractals, 258–259 
dimension, 2231 
Fractional Brownian motion, 387 
Fractional recovery model, 706 
Frank Russell Company, 48, 563 
1000 index, 95–96, 561, 563 
2000 index, 48, 94, 561, 563 
2500 index, 561 
3000 index, 48, 94, 95, 561 
Midcap Index, 94 
stock indexes, 46 
Top 200 index, 561 
Frechet distribution, 362–363, 
365, 367 
MDA, 366 
French, Kenneth R., 344, 520, 523 
Frictions, 83 
Friedman, Milton, 444 
Friend, Irwin, 436 
Functions, 100–101. See also 
Cadlag functions; Com-
posite function; Continu-
ous 
function; 
Copula 
functions; Distributions; 
Inverse function; Regres-
sion function 
derivative, 91 

Index 
765 
Functions (Cont.) 
domain, 100 
indefinite integral, 132 
primitive integral, 132 
range, 100 
Fundamental multifactor risk 
model, 568 
Fundamental solutions, 622 
usage, 279 
Future expected return, 7 
Futures 
price, 61. See also Theoretical 
futures price 
role. See Financial markets 
Futures contracts, 57–64 
forward contracts, contrast, 
58–59 
marked to market, 59 
pricing, 59–63 
risk/return characteristics, 59 
settlement date, 58 
theoretical price, 62 
Fuzziness, concept, 92 
GARCH. See Integrated GARCH 
behavior, 574 
method, 547 
models, 12, 286, 288 
results (set), availability, 385 
usage, 345–347, 741 
processes, 312, 382–383 
Gatarek, Dariusz, 644. See also 
Brace-Gatarek-Musiela 
Model 
Gaussian 
distribution, 
194, 
353, 355, 361. See also 
Stable inverse Gaussian 
distributions 
exception, 362 
Gaussian H-sssi process, 387 
Gaussian processes, 387 
Gaussian variables, 194–196 
General equilibrium system, 77 
General Equilibrium Theories 
(GET), 511, 536 
Generalized extreme value (GEV) 
distributions, 
368. 
See 
also Standard General-
ized Extreme Value Distri-
bution 
Generally accepted accounting 
principles (GAAP), 6, 40 
Generating function, 294 
Geometric Brownian motion, 
273–274, 280–282, 447– 
449, 451 
stochastic differential equa-
tion, 629 
Geometric return, 98 
Geometric-diffusion model, 741 
Geske, Robert, 690 
Geske compound option model, 
690–694, 700 
Geweke, J.F., 334 
Ghysels, E., 383 
Girsanov theorem, 459–463, 687 
application. See Black-Scholes 
option pricing formula 
Glivenko-Cantelli theorem, 370 
Global equilibrium, 77 
Global probabilistic framework. 
See Portfolios 
Global VAR model, 543 
Globally equal expected-hold-
ing-period return theory, 
616 
Gobbout, Marie-Jose, 545 
Goldberger, A.S., 334 
Goldie, C.M., 355, 368 
Gopikrishnan, Parameswaran, 
390, 522 
Gourieroux, 
Christian, 
303, 
317, 383 
Government bonds. See U.S. 
government bonds 
issuance. See Repurchase agree-
ment 
Government yield curves, com-
parisons, 611 
Government-imposed 
transfer 
fees, 28, 83 
Graham, Benjamin, 567 
Granger, C.W.J., 341, 540, 543 
method. See Engle-Granger 
method 
Granger Representation Theo-
rem, 540 
Greene, William H., 312 
Green’s function, 263 
Grinold, Richard, 568 
Growth stocks, 3 
Guaranteed interest rate, 667 
Guhr, Thomas, 522 
Gultekin, N. Bulent, 436 
Gumbel distribution, 362–363, 365 
MDA, 367–368 
Gupta, Francis, 82, 494, 497, 
500, 503–506 
Hallin, M., 334 
Hamilton, J.D., 347, 348 
Hamilton models, 286, 347–348. 
See also Markov switch-
ing Hamilton models 
Hankel matrices, 152–153, 305, 308 
Harrison, J. Michael, 89–90, 457 
Havenner, Arthurf, 574309 
Hazard rates, 730 
calibration, 716 
term structure, 731 
He, Hua, 427, 740 
Heart, Peter E., 562 
Heath, David, 640, 709, 748 
Heath-Jarrow-Morton 
(HJM) 
Model, 640, 709. See 
also Term structure 
Heavy-tailed ARMA processes, 
381–382 
Heavy-tailed distributions, 352 
Hedging, 89–90, 448–449 
Helwege, Jean, 690 
Hendricks, Darryll, 754 
Hendry, D.F., 317 
Hessian determinant, 203–204 
Hessian matrix, 203 
Heuristic computational proce-
dures, 324 
Higher order derivatives, 111–120 
High-frequency 
data 
(HFD), 
usage, 13 
High-frequency 
data 
studies 
(Olsen & Associates), 389 
High-level text mining function-
ality, development, 16 
High-risk active portfolio strat-
egies, 42 
High-yield corporate bonds, 3 
Hilburn, Robert C., 574 
Hill estimator, 376–378 
Hirtle, Beverly, 754 
Historical risk premiums, 500 
Ho, Thomas, 635 
Ho-Lee Model, 635 
Hommes, C., 259 
Homogeneous expectations, 482 
Homogeneous Poisson process, 371 
Homogeneous system, 150 
Hood, Randolph, 494 
Hosking, J.R.M., 375 
Hsieh, D., 258 
Huang, Chi-Fu, 740 
Huang, Jay, 695 
Huang, Jinzhi, 700 
Huang, Ming, 695 
Hull, John, 636, 687, 711, 717 
Hull-White Model, 635, 636 
Hyman, Jay, 651, 652, 654, 
656, 657, 662, 663 
Identically distributed sequences, 
191 
Identity matrix, 146 
IGARCH. See Integrated GARCH 
Imaginary unit, 143 
Immunization. See Multiple-
period 
immunization; 
Portfolios; Single period 
immunization 
conditions. 
See 
First-order 
immunization conditions; 
Second-order 
immuniza-
tion conditions 
constraints, 672 
Imprecision, concept, 92 
Improper integrals, 131–132 
Incomplete markets, 739 
Indefinite integrals, 131–132. 
See also Functions 
Independent and identically dis-
tributed (IID) 
alpha-stable laws, 381 
distributions, 379 
framework. 
See 
Non-IID 
framework 

766 
Index 
Independent and identically dis -
tributed (Cont.) 
processes, extreme value the -
ory, 362–378 
returns, 522 
assumption, 492 
variables, 362, 368, 437, 531 
sequence, 364 
Independent and identically dis -
tributed (IID) sequences, 
268, 325, 495. See also 
Fat-tailed IID sequences; 
Stationary IID sequence 
assumption, 378 
assumption, elimination, 376–388 
estimation procedures, 381 
normalized maxima, 374 
Independent distributed sequences, 
191 
Independently distributed (ID) 
variables, 359 
Indeterminacy principle, 243 
Index. See Benchmarks; Markets 
tracking/cointegration, 565 
Indexed portfolio, construction, 
564–565 
Indexing. See Enhanced indexing 
strategy, 564 
Indicator function. See Events 
Indifference curves, 482–484 
Individual investors, 2 
Inequality constraints, Markow -
itz mean-variance model 
(extension), 485–487 
Infinite autoregressive form, 295 
Infinite moving average. See Time 
series 
representation, 292, 301 
Infinite noncountable set, 99 
Infinite variation, 106 
Infinitesimal calculus, 107 
Infinitesimal notation, 109 
Infinitesimal quantities, calculus, 
107 
Inflation, 593 
Information. See Unstructured 
data/information 
acquisition, cost, 28, 83 
advantage, 744 
costs, 26–27 
criteria. See Akaike Informa -
tion Criteria; Bayesian 
Information Criteria 
overload, 15–16 
processing costs, 37 
propagation, 181, 402–403 
set, 85 
structures, 181–183 
technology, role, 11–13 
Information coefficient (IC), 568– 
570 
Information ratio (IR), 568, 570, 
751, 753 
Information Theory, 747 
Informationless trades, 33 
Ingersoll, Jonathan, 616, 637, 
709. See also Cox-Inger- 
soll-Ross Model 
Initial conditions, 295 
Initial margin, 58 
requirement, 49–50 
Inner product, 155 
Innovation. See Processes 
Inputs, requirement. See Assets 
Instantaneous interest rate, 219. 
See also Risk-free bank 
account 
Institutional investors, 2, 37–41. 
See also Common stocks 
Insurance 
companies, 41, 80 
premiums, establishment, 80 
ruin problem, 80–81 
Intangible assets, 21–22 
Integrals, 
172–174. 
See 
also 
Improper integrals; Indefi-
nite integrals; Lebesque-
Staieltjes integrals; Rie-
mann integrals 
definition. See Stochastic inte -
grals 
transforms, 134–138 
Integrated GARCH (IGARCH), 
347, 548 
Integrated nonstationary process, 
268 
Integrated processes, 311 
Integrated series, 309–313 
Integrated trends, 309–313 
Integration, 127–130 
chain rule, 129 
Darboux-Young approach, 173 
operation, linearity, 133 
process, 14–15 
Intensity of belief. See Belief 
Interest 
instantaneous rate, 620 
payments, receiving, 52 
risk-free rate, 447 
Interest rate risk, 599, 615 
exposure, 44 
problem, 44 
Interest rate-equity swap, 70 
Interest rate-risk based capital 
requirements, 5 
Interest rates. See Deterministic 
short-term interest rates; 
Guaranteed interest rate; 
Risk-free short-term con-
tinuously compounding 
interest rate 
calibration. 
See 
Random 
interest rates 
changes, 43, 716 
constancy, 119–120 
convexity. See Constant inter- 
est rates; Continuously 
compounding 
constant 
interest 
rate; 
Variable 
interest rates 
derivatives, pricing, 638–640 
parallel shift, 114, 668 
term structure, 126, 599–612 
continuous time, 623–638 
Interest ratio. See Short interest 
ratio 
Interest-rate derivatives, class 
(pricing), 639 
Interior-point algorithms, 210–211 
Interior-point methods, 208, 210– 
211 
International Swaps and Derivatives 
Association (ISDA), 683 
Credit Derivatives Definition 
(1999), 683 
Master Agreement, 683 
International treaties, 34–35 
Intertek Group, study, 13 
Inter-trades intervals, distribu -
tional properties, 383 
Interval of convergence. See 
Convergence 
Intrinsic value, 66–67. See also 
Stocks 
Inverse characteristic equation, 
297–298 
Inverse floaters, 54 
Inverse Fourier transform, 137 
Inverse function, 101 
Inverse Laplace transform, 249 
Inverse operation, 159–160 
Inverse operators, 291 
Inverted yield curve, 612 
Investing. See Active investing 
Investment. See Direct invest -
ments 
alternatives, 4, 45 
budget, constraint, 666 
companies, 42–43 
constraints, 5–6 
decision-making process, 13 
horizon, 502–503, 607. See 
also One-period invest -
ment horizon 
management 
applications, CAPM (role), 
525–526 
milestones, 75 
objectives, 64 
setup, 2 
opportunities, 569 
performance 
measurement/evaluation, 2 
monitoring, 552 
policy, establishment, 2–6 
principles, 81–82 
processes. See Semiautomated 
investment processes 
risk-return trade-off, 81 
strategy, 41 
selection, 2 
vehicles, 51 

Index 
767 
Investment management pro-
cess, 2–10 
assets, selection, 7–9 
investment 
objectives, setting, 2 
policy, establishing, 2–6 
performance, 
measurement/ 
evaluation, 9–10 
portfolio strategy, selection, 6–7 
Investment-grade corporate bonds, 
3 
Investors, 22. See also Consen-
sus 
investors; 
Institu-
tional investors; Risk-
averse investors; Individ-
ual investors 
risk-return preferences, 488 
Invisible hand, 77 
Irrational number, 98–99 
Irrelevance theorems, 84–85 
Isham, V., 371 
ISMA Center, 545, 565 
Issuer-specific risk, 653 
Iterative technique. See New-
ton-Raphson 
iterative 
technique 
Itô, Kiyosi, 79, 221, 224, 269 
Itô formula, 272. See also One-
dimensional Itô formula 
application, 281–282 
Itô lemma, 450, 461 
application, 453, 462 
usage, 641 
Itô processes, 271–272, 449, 
452. See also N-dimen-
sional Itô processes; Pos-
itive Itô process 
definition, 269–270 
discretization, 644–646 
function, 671 
reversibility, 629 
Itô stochastic integrals, 223, 
235–237 
Jacobs, Bruce, 568, 569 
Jagannathan, Ravi, 523 
Jarrow, Robert A., 640, 684, 
696, 698, 703, 709, 730. 
See also Heath-Jarrow-
Morton Model 
Jarrow-Turnbull Model, 698– 
703, 730 
calibration, 700–703 
Jensen, Michaell C., 519 
Jobst, Norbert J., 492 
Johansen, A., 390 
Johansen, S., 543 
Johansen methodology, 543 
Johnson, W.D., 748 
Joint 
Bernoulli 
distribution, 
722–724 
Joint defaults 
distribution, specification, 722– 
728 
modeling, common factors 
(usage), 729–730 
Joint density, 185, 192 
Joint multivariate normal distri-
bution, 531 
Joint multivariate probability 
density function, 197 
Joint Poisson process, 728–729 
Jonas, Caroline, 13, 15 
Jones, Frank J., 532, 556, 558, 
582, 583, 586, 588, 590 
Jordan, James V., 593, 616 
Jordan measure, 130 
JPMorgan, 746, 748 
Jump process, 729–730 
Jump-diffusion models, 740 
Kahn, Ronald N., 568, 569 
Kall, Peter, 202, 677 
Kalman, R.E., 538 
Kalman filter, 538 
Kalotay, Andrew J., 637 
Kalotay Williams and Fabozzi 
(KWF) Model, 635, 637 
Kanas, Angelos, 344, 546 
Karasinski, Piotr, 637. See also 
Black-Karasinski Model 
Karatzas, Ioannis, 275 
Kasa, Kenneth, 344, 545 
Kaufmann, E., 377 
k-dimensional vector, 306 
Kesten, H., 383 
Keynes, John Maynard, 81, 165 
Kim, In-Moo, 543 
Klüppelberg, Claudi, 80, 353, 
355, 385, 388 
Knock-in option, 695 
Knockout options, 695 
Kogelman, Stanley, 508 
Kolmogorov, Andrei N., 166– 
167, 318 
Kolmogorov backward equa-
tion, 629 
Kolmogorov extension theorem, 
227–228 
Konstantinovsky, Vadim, 651 
Kotz, N.L., 353 
Kouretas, Georgios P., 344, 546 
Kreps, David M., 90, 457 
Kritzman, Mark, 4 
k-th moment, 186 
kth upper order statistic, 369 
Kuhn, Thomas, 315 
Kunita, H., 221 
Labys, P., 346 
Lag operator (L), 289–292 
Lagrange, 213 
equation. See Euler-Lagrange 
equation 
multipliers, 204–206, 476 
Laherre, J., 390 
Laird, N.M., 348 
Lakonishok, J., 574 
Laloux, L., 329 
Lando, Daniel, 716 
Lando, David, 697, 703 
Lane, D.A., 380 
Laplace, Pierre-Simon, 243 
Laplace transform, 134–137. See 
also Two-sided Laplace 
transform 
Laplace-transform derivatives, 248 
Large capitalization stocks, 3 
Lau, Sheila, 516 
Lausanne School, 76–78 
Law of Large Numbers (LLN), 
38, 358–360, 380 
Law of one price, 394 
Learning 
complexity, 317–319 
Vapnik-Chervonenkis 
(VC) 
theory, 319, 547 
LeBaron, B., 258, 259, 574 
Lebesgue measures, 130 
Lebesgue-Stieltjes measure, 177 
Lebesque-Stieltjes integrals, 130, 177 
Ledermann, W., 375 
Lee, E.B., 214 
Lee, J.C., 748 
Lee, Sang Bin, 635. See also Ho-
Lee Model 
Left continuous function, 104 
Legal documentation. See Credit 
derivatives 
Lehman Aggregate index, 497 
Lehman Brothers U.S. Aggre-
gate Index, 649, 652, 653 
benchmark, 654 
information, 655 
Leibnitz, G.W., 91, 107 
Leibowitz, Martin L., 508 
Leland, Hayne E., 716 
Lender, definition, 51 
Lending rate, 62 
Length. See Vectors 
Leverage, creation, 59 
Leveraged portfolio, 479 
Levy, Kenneth, 568, 569 
Levy, Paul, 79 
Levy process, 227 
Levy-stable distributions, 351, 
361 
Levy-stable scaling regime, 385 
Li, David X., 732 
Liabilities 
classification, 38 
market value, 40 
nature, 37–39 
Liability-funding strategies, 661–677 
Liability-matching condition, 677 
Life companies, 37–41 
Likelihood estimate. See Maxi-
mum likelihood estimate 
Likelihood function, 321 
Likelihood Ratio methods, 438 
Lilien, D., 548 
Limit orders, 30, 48–49. See also 
Stop-limit order 

768 
Index 
Limit random variable, conver-
gence, 189–190 
Limits, 102–103 
Lindskog, Filip, 189, 329 
Linear conditional factor mod-
els, 531 
Linear differential equation, 247– 
249, 621 
Linear equations 
homogeneous system, 409 
systems, 149–150 
theorem, 150 
Linear independence/rank, 151 
Linear infinite moving average 
representation, 305 
Linear models. See Financial time 
series 
Linear moving average nonsta-
tionary models, 295–296 
Linear objective function, 206– 
207 
Linear ODE, 21 
Linear programming (LP), 201, 
206–208 
Linear regression, 197–199, 328 
model, 530 
Linear stochastic equations, 278 
Linear utility function, 489 
Lintner, John, 75, 86–87, 334, 
477, 512 
Lippi, M., 334 
Lipschitz condition, 242 
Liquidation firm, 706 
Liquidity, 22. See also Assets 
premium, 610, 617 
theory, 613, 617. See also 
Term structure 
Litterman, Robert, 399 
Litzenberger, Robert, 520 
Lo, Andrew W., 327, 344, 345, 
546, 574 
Local expectations theory, 616 
Location-scale dependent fam-
ily, 368 
Loftus, John S., 552 
Logarithmic utility function, 489 
Log-gamma distribution, 366 
Log-likelihood computation, 321 
Lognormal distribution, 531 
Lognormal model, usage, 692 
Lognormally distributed variable, 
539 
Log-prices, 538 
London Interbank Offered Rate 
(LIBOR), 608–610 
forward rate curve, 611 
interest rate. See Forward 
LIBOR interest rate 
one-month, 53 
one-year, 54 
spot rate curve, 611 
three-month, 609 
usage, 70 
Long-memory fractional mod-
els, 346 
Long-short equity portfolios, 545 
Long-short portfolios, 340 
Longstaff, Francis, 695 
Lookback option, 423 
Lorenz, Edward, 257 
Loss analysis, risk, 507 
Loss probability, 508 
Louveaux, F., 202 
Lower Riemann sum, 127 
Lower triangular matrix, 148 
Low-risk passive portfolio strat-
egies, 42 
Lucas, A., 344 
Lundberg, Filip, 75, 80–81 
Lynch, Peter, 567 
M3. See Monetary mass 
MacKinley, A. Craig, 327, 344, 
345, 546, 574 
Maclaurin expansion, f126 
Maclaurin power series, 122 
Macroeconomic 
econometric 
models, 259 
Macroeconomic effect, 722 
Macroeconomic factors, identi-
fication, 436 
Macroeconomic theory, 532 
Maddala, G.S., 543 
Maintenance margin, 50, 58 
requirements, 58 
Malevergne, Y., 331, 492 
Mandelbrot, Benoit, 231, 258, 389 
Mantegna, R.N., 390 
Marcus, L., 214 
Margin 
call, receiving, 50 
requirement, 59, 65. See also 
Initial margin requirement 
transactions, 49–50 
Marginal density, 176, 192 
Marginal distribution function, 
176–178 
Market. See Complete markets; 
Factor; Financial mar-
kets; 
Product 
market; 
Thin market 
capitalization, 3, 94–95. See 
also Total market capi-
talization 
completeness, 404, 738–744 
economics, 742–744 
mathematics, 739–742 
debt value, 689 
impact costs, 33, 63 
index, 4 
contrast. See Bonds 
makers, restrictions, 28, 83 
making, 23 
model, 524 
order, 48 
organizational structure, 25 
overreaction, 572–573 
participants, overview, 21, 
34–45 
portfolio, 86, 481, 525 
price efficiency, 7, 31–32 
risk, 86, 745–746 
reward per unit, 482 
segmentation theory, 613, 618 
thickness, 31 
timing costs, 33 
value. See Assets; Liabilities 
Market-clearing prices, 29 
Market-neutral strategies, 575– 
577 
Marketplace price efficiency, 7 
Markov chain, 705 
Markov coefficients, 293–294, 
304–305 
Markov models, 423 
Markov process. See Continu-
ous-time Markov process 
Markov switching 
method, 547 
models, 286, 347–348, 379, 384 
Markov switching Hamilton 
models, 496 
Markov-switching VAR, 548 
Markowitz, Harry M., 75, 81– 
83, 201, 471, 477, 494, 
497, 500, 503–506, 524, 
532, 557, 586. See also 
Mean-variance analysis 
(ed.), 494, 497, 500, 503–506, 
524, 532, 557, 558, 582, 
583, 586, 588, 590, 651 
Markowitz efficient frontier, 474, 
479. See also Ex ante 
Markowitz efficient frontier 
Markowitz efficient portfolios, 
474 
Marsh, T., 377 
Martellini, Lionel, 632, 633 
Martingale, 186 
conditions, system, 432 
measures. 
See 
Equivalent 
Martingale measures 
Marxist economics, 78 
Mateev, P., 389 
Mathematical 
programming 
problem, 201 
Matlab (software), 487 
Matrices, 141, 144–145. See 
also Covariance; Diago-
nals; Hankel matrices; 
Identity matrix; Lower 
triangular matrix; nxm 
matrix; Random matri-
ces; 
Square 
matrices; 
Transition matrix; Upper 
triangular matrix 
adjoint, 159–160 
algebra, 141, 208 
dimensions, 145 
elements, 144–145 
notation, 207 

Index 
769 
Matrices (Cont.) 
operations, 153, 156–160 
polynomial, 301 
product, 158 
operation, 159 
transpose, 156 
Maturity, 
23–24. 
See 
also 
Bonds; Bullet maturity; 
Claims; Term to maturity 
intermediation, 36 
value, 52 
Maxima, 202–204, 362–368, 490 
discovery, 205 
Maximum, usage, 99, 209 
Maximum domain of attrac-
tions (MDA), 366, 376. 
See also Frechet distribu-
tion; Gumbel distribu-
tion; Weibull distribution 
Maximum likelihood estimate 
(MLE), 319–324 
methods/techniques, 438, 534 
Maximum likelihood (ML), 320 
estimator, 321–323 
methodology, 375, 437 
Max-stable distributions, 368 
McElroy, Marjorie B., 436 
McEnnally, Richard W., 593, 616 
McNeil, Alexander, 189, 329 
Mean-reverting portfolio, 576 
Mean-variance analysis (M-V 
analysis) (Markowitz), 8, 
202, 211, 499. See also 
Portfolios 
extension, 508. See Inequality 
constraints 
usage, 471–477, 495 
Mean-variance model, 508 
Mean-variance pairs, selection, 476 
Mean-variance portfolio 
management, 8 
selection, 486 
Mean-variance-efficient portfolios, 
473 
Measurable function. See Real-
valued measurable function 
Measurable space, 173 
Measure, 171–172 
space, 172 
Meeraus, A., 666 
Mehta, M.L., 329 
Menger, Carl, 77 
Merrill Lynch Domestic Mar-
ket Index, 649 
Merton, Robert C., 76, 87–90, 
522, 684. See also Black-
Scholes-Merton Model 
Messages, probability, 181 
Metafile. See Descriptive metafile 
Meyer, M., 390 
Mid Cap 400 Index, 561 
Mid-capitalization stocks, 3 
Middle-of-the-road stocks, 563 
Midwest Exchange, 46 
Migration risk, 703 
Mikosch, Thomas, 80, 353, 
355, 385, 388 
Miller, Merton H., 75, 83–85, 
519. See also Modigliani-
Miller irrelevance theorem; 
Modigliani-Miller theorem 
Minima, 202–204, 490 
discovery, 205 
Minimum, usage, 99, 209 
Minimum variance portfolios, 473 
Mittnik, S., 389 
Mixed-integer programming (MIP), 
666 
Modeling. See Economic model-
ing; State-space modeling 
approaches, 14, 710 
tools, 
industry 
evaluation, 
13–15 
Models, 283. See also Asset 
pricing theory; Autore-
gressive moving average; 
Multifactor models 
complexity, 317–319 
problem, 318 
selection, 315–317 
suite, engineering principles, 
17–18 
unconstrained search, 316 
Modern Portfolio Theory (MPT), 
471 
Modigliani, Franco, 75, 83–85 
Modigliani-Miller 
irrelevance 
theorem, 84–85 
Modigliani-Miller theorem, 84 
Moment ratio estimator, 377 
Moments/correlation, 186–188 
Monetary mass (M3), 340 
Moneyness, 22 
Monfort, Alain, 303, 317 
Monte Carlo simulations, usage, 
494 
Monthly tracking error, 554 
Mortgage-backed securities (MBSs), 
4, 55 
prepayment risk, 653 
risk, 653 
volatility risk, 653 
Morton, Andrew J., 640, 709. 
See also Heath-Jarrow-
Morton Model 
Mossin, Jan, 76, 86–87, 334 
Moving average, 571–572. See 
also Stationary univari-
ate 
moving 
average; 
Time series 
process, 298 
representation. 
See 
Linear 
infinite moving average 
representation 
MSCI EM Free, 497 
Muller, Peter, 487, 491 
Muller, U.A., 377, 389 
Multex, usage, 17 
Multidimensional map, 278 
Multidimensional observations, 337 
Multidimensional trend station-
ary series, 311 
Multifactor CAPM, 87–88, 511 
Multifactor models, 332–338, 
333, 530–537, 746 
usage. See Common stocks 
Multifactor risk models, 532, 
555. See also Barra 
application, 577–589 
illustration, 654–661 
usage, 565, 578 
Multifactor term structure model, 
632–634 
Multiperiod finite-state setting, 
arbitrage pricing, 402–423 
Multiperiod stochastic optimi-
zation, 492–494 
Multiple market maker systems, 
45–46 
Multiple stepup note, 55 
Multiple-period immunization, 
668 
Multiplication operation, 154– 
156, 158–159 
Multiplicative state-space method, 
547 
Multiplicative state-space mod-
els, 384 
Multistage stochastic optimiza-
tion, description, 676 
Multistage stochastic program-
ming, 675–677 
Multivariate distribution, 732 
Multivariate function, 202–203 
Multivariate GARCH, 548 
Multivariate models. See Non-
stationary 
multivariate 
ARMA models; Station-
ary multivariate ARMA 
models 
Multivariate random walk model, 
327, 339 
Multivariate stationary series, 
293–295 
Multivariate time series, 285 
Multivariate white noise, 338 
Mulvey, John M., 392, 473 
Municipal 
bonds. 
See 
U.S. 
municipal bonds 
Municipal government bond 
issue, 663 
Musiela, Marek, 644. See also 
Brace-Gatarek-Musiela 
Model 
Mutual funds, 87 
investment, 36 
liabilities, 42 
Myopic one-period optimization 
models, 492 
Nagahara, Y., 388 
Naive set theory, 93 
NASDAQ-AMEX Market Group, 
Inc., 46 

770 
Index 
National Association of Insurance 
Commissioners 
(NAIC) 
scenarios, 675 
National Association of Securi-
ties Dealers Automated 
Quotation (NASDAQ) 
Composite index, 47 
system, 46–47 
Natural numbers, one-to-one 
relationship, 100 
NAV. See Net asset value 
n-dimensional Borel sets, 227– 
228 
N-dimensional Brownian motion, 
634 
n-dimensional Brownian motion, 
228 
n-dimensional Cartesian space, 143 
n-dimensional cumulative distri -
bution function, 176 
n-dimensional distribution func -
tion, 176 
n-dimensional Euclidean space, 170 
N-dimensional Itô process, 634, 638 
N-dimensional price process, 458 
n-dimensional probability den -
sity, 176 
n-dimensional real space, 179 
n-dimensional space, 175 
n-dimensional vector, 97, 158 
n-dimensional zero-mean white 
noise process, 293, 307 
Negative sign restriction, 208. 
See also Nonnegativity 
sign restriction 
Net asset value (NAV), 42 
Neural networks, usage, 345 
New York Stock Exchange (NYSE), 
42–43, 46 
Composite Index, 46, 94 
index, 521 
market capitalization, 95 
Newton, Isaac, 91 
Newton-Raphson iterative tech -
nique, 596 
Nielsen, Steen, 344 
No-arbitrage models, 634 
Noise. See Colored noise; White 
noise 
multiplicative nature, 383 
term, 328, 576 
Nominal rate, 52 
Nonanticipativity property, 215 
Noncorporate issuers, 27 
Non-decreasing function, 363 
Nondiversifiable risk factors, 86 
Nonequality constraints, 211 
Nonfactor error term, 533 
Nonfinancial businesses, 34–35 
Non-Gaussian processes, 387 
Nonhomogeneous system, 150 
Non-IID framework, 384 
Nonliability 
driven 
entities, 
benchmarks, 40–41 
Nonliability driven objectives, 2 
Nonlinear dynamics, 256–259 
chaos, 573–574 
development, 243 
models, 573–574. See Prices; 
Returns 
Nonlinear models, 288 
Nonlinear pattern recognition. 
See Statistical nonlinear 
pattern recognition 
Nonnegative adapted process, 404 
Non-negative diagonal elements, 
162 
Nonnegative integer values, 371 
Nonnegativity sign restriction, 207 
Nonobservability, consequences, 
521 
Nonreproducible assets, 21–22 
Nonsingular variance-covariance 
matrix, 293 
Nonstandard analysis, 107 
Nonstationary models. See Finan -
cial time series 
Nonstationary multivariate ARMA 
models, 304 
Nonstationary process. See Inte -
grated nonstationary process 
Nonstationary series, 295–297, 304 
Nonstationary univariate ARMA 
models, 300–301 
Nonsystematic factor risk, 652 
Nonsystematic risk, 513–516, 518 
exposure, 660 
reduction, 661 
Nonterm structure 
factors, 656 
risk factors, 653 
Nontrivial solutions, 161 
Non-U.S. bonds, 3 
Non-U.S. common stocks, 3 
Non-U.S. foreign stocks, 3 
Normal distribution, 194. See 
also 
Joint 
multivariate 
normal distribution; Stan-
dard normal distribution; 
Univariate normal distri-
bution 
Normal probability. See Cumu-
lative normal probability 
Normal random variable, 196–197 
Normal yield curve, 612 
Normality assumption, relax -
ation, 491–492 
Normally distributed IID vari-
ables, 534 
Normative theory, 471 
Notional amount, 69 
Notional principal amount, 69–71 
Nth to default swaps, 681–682 
n-tuples, 96–98, 168 
Null hypothesis, usage, 340 
Numeraire, definition, 101 
Numerical algorithms, 206–212 
Numerical solutions. See Ordi-
nary differential equa-
tions; Partial differential 
equations 
Numerical values, 101 
N-vector process, 460 
Objective function, 201 
Observations, definition, 306 
Observed information matrix, 322 
Odd lots, 664 
Office of the Comptroller of the 
Currency, 
Quarterly 
Derivatives Report, 1 
Ohlson, J.A., 574 
O’Kane, Dominic, 711 
Okazaki, M.P., 388 
Oksendal, Bernd, 268 
Olesen, Overgaard, Jan, 344 
Olsen & Associates. See High- 
frequency data studies 
One price, law. See Law of one 
price 
One-dimensional Brownian motion, 
228, 271 
One-dimensional Itô formula, 
272–274 
One-dimensional standard Brown -
ian motion, 226, 232 
One-dimensional 
zero-mean 
white noise process, 289 
One-factor equilibrium model, 636 
One-factor model, 632 
One-factor term structure mod -
els, examples, 635–638 
One-lag stationary VAR, 537 
One-period finite-state market, 399 
One-period investment horizon, 
513 
One-sided 
Laplace-transform, 
application, 248–249 
One-sided transform, 136 
Onigo, Iris, 10 
On-the-run maturities, 601 
On-the-run yield, estimation, 601 
Open-end funds, 42 
Operation, 153 
Operational efficiency, 32–34 
Operational risk, 746–747 
Opportunity costs, measurement, 
34 
Optimal control theory, 212–214 
Optimal portfolio 
CML, usage, 482–485 
selection, 484–485 
Optimal solution, 207 
Optimal value, 207 
Optimization, 201. See also 
Multiperiod 
stochastic 
optimization; Scenario 
algorithm, 660 
application, 660–661 
models. See Myopic one-period 
optimization models 

Index 
771 
Optimization (Cont.) 
performing, 500 
problem. See Constrained opti -
mization problem; Qua-
dratic optimization problem 
formulation, 665 
procedures, 324 
theory, 82. See also Computer- 
based optimization theory 
usage, 660 
Optimizers, 487, 490 
Option price, 64, 66–69 
components, 66–68 
factors, 68 
process, 451 
Option pricing, 447–454 
model, 68–69 
theory, 684 
Option-adjusted duration, 118 
Optionality risk, 653 
Option-free bond, 116 
value, 117–118 
Options, 64–69 
buyer, 66, 67 
premium, 64 
risk-return, 66 
theory, 89–90 
time premium, 67 
time to expiration, 68 
valuation, relationship. See 
Bond valuation 
Order 
flow, 23 
handling/clearance charges, 28, 83 
imbalance, 30 
integration, 310 
processing costs, 30 
statistics, 369–371 
Ordered arrays, 141 
Ordinary differential equations 
(ODE), 240–243, 261– 
262. See also Linear ODE 
closed-form solutions, 246–249 
numerical solutions, 249–256 
order/degree, 241 
solution, 241–243 
systems, 243–245 
Ordinary least square (OLS) 
estimates, 437–438 
method, 312, 323, 335 
Ornstein-Unlenbeck 
process, 
280–281, 636 
Orthogonal vector, 156 
Ouliaris, S., 544 
Outcomes/events, 169–170 
Outputs, definition, 306 
Overfitting, 317 
Overreaction hypothesis, 573 
Over-the-counter (OTC) 
instrument, 58 
markets, 26, 46, 65 
options, 65 
traded shares, 46 
trading, 45 
Pacific Coast Exchange, 46 
Pacific Investment Management 
Company (PIMCO), 552 
Pagan, Adrian, 524 
Pair trading, 574 
Par value. See Bonds 
relation, 597 
Pareto, Wilfredo, 75–78 
Pareto behavior, 376 
Pareto distribution, 366, 370, 531 
Pareto Law, 78, 389 
Pareto tail, 378 
Partial 
differential 
equations 
(PDE), 240, 259–265, 451 
numerical solutions, 263–265 
obeying, 628 
solving, 452 
Partial duration, technical differ-
ence. See Rate duration 
Partitions, 182–183 
Passive portfolio 
management, contrast. See 
Active portfolio 
strategy, 6. See also Low-risk 
passive portfolio strate-
gies 
Passive strategies, 564–565 
Path dependence models, 423 
Path dependent option, 695 
Pathwise Riemann-Stieltjes inte -
grals, 443 
Payaslioglu, Cem, 289 
Payment failure, 683 
Payoff price pair, 406 
Payoff rate, 616. See also Arbi -
trage 
processes, 442–445 
absence, 455 
introduction, 466 
Peaks over threshold, point pro-
cess, 371–373 
Pearl, Judea, 168 
Pension 
funds, 41–42, 45 
obligations, 42 
Perfect dependency, 724 
Perfect market, 28–30 
results, 83 
Performance. See Portfolios 
lowest 
level 
measurement, 
753–754 
measurement/evaluation. See 
Investment 
Perold, André F., 508 
Per-period default probabilities, 712 
Perpetual instrument, 24 
Pesaran, Hashem M., 540 
Pesaran, M.H., 342 
Petrov, B.N., 318 
Phillips, P.C.B., 544 
Physical settlement, 680 
Pickand estimator, 375–376 
Pictet, O.V., 377, 389 
Plan sponsors, 41–42 
Plerou, Vasiliki, 390, 522, 536 
Pliska, Stanley R., 90, 457 
Poincaré, Henri, 78 
Point process. See Exceedances; 
Extreme point; Peaks over 
threshold 
theory, 80 
Points. See Critical point; Sad -
dle point 
density, 99–100 
measure, 372 
processes, 697 
Poisson assumption, 731 
Poisson distribution, 707 
Poisson intensity, 699 
Poisson process, 80, 697–698, 
714, 740. See also Homo -
geneous Poisson process; 
Joint Poisson process 
Polynomial cointegration, 540 
Polynomial time, 211 
Polynomials 
restrictions, 302 
roots, 301 
Pontryagin’s Maximum Princi -
ple, 214 
Portfolio M, definition, 481 
Portfolio management. See Bonds; 
Mean-variance 
portfolio 
management 
contrast. See Active portfolio 
management 
engineered approach, 568 
risk management, usage, 751– 
755 
strategies, relationship. See 
Risk factors 
Portfolio risk 
control, 552 
measure, 659 
reduction, 513 
Portfolios 
assets, 63 
beta, 518, 559. See also Track -
ing errors 
tracking error, relationship 
(quantification), 559 
choice, 487–491, 566 
construction. 
See 
Indexed 
portfolio 
approaches, 8–9 
risk control, relationship, 582 
diversification, 435 
exposure, 657 
assessment, 583–586 
holdings, 660 
immunization, 667–672 
first-order conditions, 670 
managers 
benchmark index, 97 
modeling demands, 13 
performance, 9 
payoff, 394 
performance, 98, 578 
replication, 89–90 
risk-return report, 583 

772 
Index 
Portfolios (Cont.) 
selection, 500–503 
global probabilistic frame-
work, 490–491 
mean-variance analysis, 471 
size, impact, 556–560 
strategy. See Active portfolio; 
Dedicated portfolio strat-
egy; 
Passive 
portfolio; 
Structure portfolio 
selection. See Investment 
management process 
tilting, 587–589 
tracking errors, 558 
Positive Itô process, 455 
Positive theory, 472 
Poterba, J., 343 
Potters, M., 329 
Power laws 
distributions, 351 
absence. See Scaling 
truncation, 367 
Power series, 122, 290 
Power utility function, 489 
Power-law distributions, 356–358 
Power-law tail, 373 
Predicted tracking error, 556, 565 
Preferred habitat theory, 613, 618 
Preferred stock, 25 
Premium leg, 680 
Premium par yield, 598 
Prepayment, 56 
option, 56 
Priaulet, Philippe, 632, 633 
Priaulet, Stéphanie, 632, 633 
Price/earnings factor, 520 
Price/earnings ratio, 519, 532 
Prices. See Clean price; Dirty price 
ARDL models, 546 
diffusion, 78–80 
discovery process, 26 
dynamic models, 538–546 
exponential divergence, 539 
momentum, 572 
nonlinear dynamic models, 
546–549 
persistence, 572 
processes, sum, 444 
risk, reduction, 59 
Price-to-book value multiplier, 567 
Price-to-book value per share 
(P/B) ratio, 561, 563 
calculation, 562 
Price-to-earnings value multi -
plier, 567 
Pricing. See Arbitrage pricing 
generalizing. See European 
options 
model. See Baskets 
relationships, 405–414 
examples, 406–414 
theory, defining, 455 
Primal problem, 210 
Primal-dual gap, 210 
Primary market, 25 
Primitive integral. See Functions 
Principal, 52 
Principal components analysis (PCA) 
model, 335–338 
usage, 536 
Principal repayment, 56 
Probabilistic dynamics, 168 
Probabilistic judgments, 167 
Probabilistic representation. See 
Financial markets 
Probability, 170–171. See also 
Conditional probability 
axiomatic theory, 169 
concepts, 165 
curves. See Default probability 
density. 
See 
n-dimensional 
probability density 
function, time-evolution, 260 
disjoint additivity, 171 
distribution, evolution, 93 
explanation, 167–169 
framework, 92 
interpretations, 166–167 
measure, 441, 642. See also Arti -
ficial probability measure 
space, 165, 170, 178, 402 
representation, 430 
sum, 704 
theory, 165–173 
development, 80, 737 
Processes. See Stochastic pro -
cesses 
drif, 279 
innovation, 310–311 
stochastic interval, defining, 
220 
volatility, 279 
Product market, 21 
Product rule, 109 
Profit opportunities, reduction, 575 
Program trades, 50 
Proper subsets, 93–95 
Property and casualty (P&C) 
companies, 41 
Proportionality recovery assump -
tion, 709 
Protection buyer. See Lump-sum 
payment 
Protection leg, 680 
Pure bond index matching, 650 
Pure expectation theory, 613–617 
Pure growth stocks, 563 
Pure risk-free discount bond, 606 
Put option, 64 
Put price, 56 
Putable bond, 56 
Quadratic optimization prob -
lem, 486 
Quadratic Programming (QP), 
202, 211–212 
Quadratic utility function, 489 
Quadratic variation, 221–222 
Quah, D., 334 
Qualitiative information, inte -
gration, 15–17 
Quality risk, 653 
Quantile plot, 374 
Quantile transformation, 369 
Quantitative finance, 283 
Quantitative information, inte -
gration, 15–17 
Quantitative methods, usage, 14 
Quantitative phenomena, dynam -
ics, 96–97 
Quantities, 96–100 
Quantum physics, 444 
Quarterly Derivatives Report, 
U.S. Office of the Control-
ler of the Currency, 745 
Quotient rule, 109, 113 
Rachev, S.T., 189, 329, 389 
Radon-Nikodym derivative, 416– 
417, 464 
definition, 458 
usage, 467. See also Continu- 
ous-state setting 
Ramaswamy, Krishna, 520 
Rand Corporation, 82 
Random disturbance, 80 
Random interest rates, 716 
Random matrices, 329–332 
relationship. See Capital Asset 
Pricing Model 
Random Matrices Theory (RMT), 
329 
Random Matrix Theory (RMT), 
522 
Random phenomena, evolution, 93 
Random shocks 
accumulation, 217 
feedback, 220 
Random variables, 32, 172– 
175. See also Normal 
random variable 
convergence, 189–190 
distribution 
convergence, 190–191 
functions, 177 
joint probability, 176 
probability density, 352 
sequences, 189–191 
Random vectors, 175–178 
Random walk, 221. See also 
Arithmetic random walk; 
Computer-generated 
independent 
arithmetic 
random walks; Corre-
lated random walks; Dis-
crete random walk 
hypothesis, 343 
models, 324–327. See also Mul-
tivariate 
random 
walk 
model 
empirical adequacy, 327 
Range notes, 54 

Index 
773 
Ranks, 151–153 
Rank-size order property, 357 
Rate duration, partial duration 
(technical difference), 139 
Rational number, 98–99. See 
also Irrational number 
r-dimensional Brownian motion, 
278 
Read, S., 353 
Real estate, 3 
Real function, 101 
Real markets, brokers/dealers 
(role), 28–31 
Real matrix, 145 
Real numbers, one-to-one rela -
tionship, 99 
Real-valued function, 101, 134– 
136, 172 
Fourier transform, 137 
Real-valued measurable function, 
174–175 
Real-valued variables, 204 
Recession periods, 347 
Reconstitution, 606 
Recourse, concept, 202 
Recovery. See Stochastic recovery 
assumption. See Proportional-
ity recovery assumption 
fluctuation, 706 
model. See Fractional recov -
ery model 
payment, 698 
ratio, 698 
Rectangular matrix, 145 
Recursive difference equations, 249 
Recursive relationship, 276 
Reddington, F.M., 667 
Reduced form models, 684. See 
also Credit risk modeling 
observations, 710 
Redundant securities, 446 
Reference 
designation, 71 
entity, 679, 728 
defaults, 718 
obligation, 679–680 
value, 714 
rate, 54 
Refunding. See Bonds 
Regression. See Linear regression 
function, 197–199 
Regular deflator, 455 
Regulatory accounting princi -
ples (RAP), 6, 40 
Regulatory constraints, 5 
Regulatory surplus, 40 
Reichenbach, Hans, 166 
Reichlin, L., 334 
Reilly, Frank K., 649 
Reinvestment. See Yield 
risk, 499, 615 
Relative frequency, 166 
Relative prices, 699 
dispersion, 23 
Relative risk, 560 
Relative strength, 572 
Representations, 283. See also 
Autoregressive 
moving 
average; State-space rep-
resentation 
Reproducible assets, 21. See also 
Nonreproducible assets 
Repudiation, 683 
Repurchase agreement, 601 
market, 
government 
bond 
(issuance), 611 
Residential mortgages, 653 
Residual claim, 22 
Residual risk, 515, 579, 582 
decomposition. 
See 
Active 
systematic-active 
resid-
ual risk decomposition 
Resnick, S., 368, 385 
Resource Description Framework 
(RDF), development, 16 
Retirement payments, 42 
Return on investment (ROI), 
examination, 18 
Return/risk decisions. See Strate -
gic return/risk decisions 
Returns. See Compound return; 
Simple net return 
average value, 8 
correlation, 8 
covariance, 8 
dynamic market models, 537–538 
expectations, 552 
forecast, 487–488 
generation function, 532 
nonlinear dynamic models, 
546–549 
potential, 66 
predictability, 22 
rates, 575 
volatility, 287 
bounds, 575 
Return-to-maturity 
expecta -
tions theory, 616 
Return-to-maturity theory, 617 
Reverse cash and carry trade, 61 
Reversibility, 22, 23 
Reward to Variability Ratio, 
750–751 
Riemann, Bernhard, 127 
Riemann integrals, 127–129, 174 
properties, 129–130 
Riemann sum, 126–128. See also 
Lower 
Riemann 
sum; 
Upper Riemann sum 
Riemann-Stieltjes integral, 177. 
See also Pathwise Rie-
mann-Stieltjes integrals 
Right continuous function, 104 
Right endpoint, 363 
Risager, Ole, 344 
Risk. See Credit risk; Markets; 
Operational risk 
approach. See Tracking errors 
bearers, 41 
category, 38 
control, 738. See also Stock 
market 
relationship. See Portfolios 
decomposition, 577–582. See 
also Active risk; Active 
systematic-active 
resid-
ual risk decomposition; 
Residual risk; System-
atic-residual risk decom-
position; Total risk 
summary, 582 
equilibrium market price, 482 
increase, 88 
indices, 533 
lowest 
level 
measurement, 
753–754 
measurement, usage, 752–753 
measures, 747–751 
modeling. See Contribution 
risk modeling 
models, 745–747 
application. See Multifac-
tor risk models 
illustration. See Multifactor 
risk models 
premium, 88, 436. See also 
Capital market line; His -
torical risk premiums 
reduction. See Prices 
reward per unit. See Market 
shape, 737 
tolerance, 7 
types, 31 
Risk factors, 532, 652 
compensation, 88 
groups, 658 
portfolio management strate -
gies, relationship, 652–653 
statistical independence, 658 
Risk management, 737, 738, 754 
factors, 752 
policies, determinant, 738 
reasons, 744–745 
regulatory implications, 754–755 
usage. See Assets; Portfolio 
management 
Risk neutral measure, 687 
Risk-adjusted returns, produc -
tion, 569 
Risk-averse investors, 484, 490 
Risk-aversion parameter, 486 
Risk-free asset 
absence, 484 
existence, 512–513 
introduction, 480 
investment, 417 
purchase, 426 
replication, 741 
return, 519 
usage, 512 
zero variance, 477 
Risk-free bank account, deter- 
ministic 
instantaneous 
interest rate, 218 
Risk-free bond, 624 

774 
Index 
Risk-free borrowing, 447 
Risk-free coupon bond, 713 
Risk-free discount factor, 698 
Risk-free profit, 449 
Risk-free short-term continuously 
compounding interest rate, 
455 
RiskMetrics Group, 745, 748 
RiskMetrics model, 748 
Risk-neutral methodology, 717 
Risk-neutral pricing, scope, 716 
Risk-neutral probabilities, 398– 
399, 416–423. See also 
Binomial models 
computation, 401–402, 426 
determination, 416 
examples, 420–423 
existence, 712 
expectation, 640 
martingale relationship, 627 
measure, 625 
usage, 428 
Risk-of-loss analysis, 507 
Risk-premium form, 519 
Risk-return 
profile, 744 
symmetricality, 59 
trade-off, 473, 501, 538 
determinant, 737 
optimization, 86 
Risk/reward relationship. See 
Symmetric 
risk/reward 
relationship 
Risky asset, shorting, 426 
Risky debt, decomposition, 686 
r-minors, 149 
Robins, R., 548 
Robinson, Abraham, 107 
Rockafeller, Tyrrell R., 749 
Roll, Richard R., 87, 335, 436, 
519–521 
Ron, Uri, 610 
Rosenberg, Barr, 525, 574 
Rosenow, Bernd, 522 
Ross, Stephen A., 88–89, 335, 
435, 436, 616, 637, 709. 
See also Cox-Ingersoll-
Ross Model 
Round-trip cost, 23–24 
Round-trip transaction cost, 63 
Row rank, 53 
Row vectors, 142 
Rubin, D.B., 348 
Rubinstein, Mark, 69 
Runge-Kutta method, 252 
Russell. See Frank Russell Com-
pany 
Saddle point, 203 
Salomon Smith Barney Broad 
Investment-Grade Bond 
Index, 649 
Samorodnitsky, G., 387 
Samuelson, Paul A., 85–86, 326 
Sargent, T.J., 334 
Savings & loan (S&L) associa-
tions, 43 
Scalar product, 155, 336, 397 
Scalars, 141 
Scale, absence, 385 
Scaling, 351–362, 385–388 
laws, presence, 389 
property, 386 
power-law distribution, 386 
Scenario 
generation, 674–675 
optimization, 672–673 
Scenario-dependent constraints, 673 
Schachermayer, W., 467 
Schafer, G., 168 
Scheduled termination date, 680 
Scheinkman, J.A., 259 
Scholes, Myron S., 69, 76, 89– 
90, 451, 519, 684. See 
also Black-Scholes-Mer-
ton Model 
School of Copenhagen, 444 
Schrodinger’s cat, 243 
Schuermann, Til, 378 
Schwartz, Eduardo S., 638, 695 
Schwartz, Gideon, 318 
Schwartz, Robert A., 30 
Search costs, 26 
Second derivative, application, 
118–120 
Second order approximation, 122 
Secondary markets, 25, 27–34 
Second-order derivative, 111–112 
Second-order equations, 250–251 
Second-order immunization con-
ditions, 672 
Second-to-default basket swap, 682 
Sector risk, 653, 658 
Sector specific effect, 722 
Securities. See Floating-rate securi-
ties; Redundant securities 
analysis, 567 
margin, 63 
performance, 34 
price, 31 
difference, 33 
underwriting, 35 
Securities Exchange Act of 1934, 
49–50 
Security market line (SML), 516–518 
Segmentation theory. See Mar-
kets 
Self-financing conditions, 215, 677 
Self-financing trading strategy, 
445, 448–451 
creation, 452 
definition, 466 
Self-similarity, 258, 351, 385–388 
Semiautomated investment pro-
cesses, 324 
Semistrong efficiency, 32 
Senior basket credit default 
swaps, 681–683 
Senior basket default swaps, 682 
Separable variables, 246 
Separating Hyperplane Theo-
rem, 398 
Sequence, definition, 101 
Sets, 93–96. See also Empty 
sets; Proper subsets 
elementary properties, 96 
intersection, 95–96 
operations, 93–96 
union, 95 
Settlement date, 57–58. See also 
Futures contracts 
Sharpe, William F., 75, 82, 86– 
87, 334, 477, 512, 516, 
524, 750 
Shefrin, Hersh, 502 
Shin, Yongcheol, 342, 540 
Short interest ratio, 572 
Short selling, 49, 393 
Short-run price stability, 30 
Short-term 
debt 
obligations, 
investment, 614 
Short-term financial assets, 25 
Short-term fluctuations, 744 
Short-term forward rates 
behavior, 613 
curve, 608 
Short-term interest rate, 112, 632 
function, 624 
process, 627 
Short-term rate. See Variable 
short-term rates 
constancy, 614, 621 
function, 620 
Short-term risk-free borrowing, 415 
Short-term risk-free interest rate, 
68 
Short-term securities, 671 
Shreve, Steven E., 275, 625 
Sigman, K., 354, 356 
Similarity. See Diagonalization/ 
similarity 
Simon, Herbert, 315 
Simplex algorithm, 208–210 
Simplex method, 208, 210 
Single period immunization, 667 
Single stepup note, 55 
Single-name credit default swaps, 
680 
pricing, 710–718 
framework, 711–712 
Singleton, Kenneth J., 334, 685, 
696, 706, 729. See also 
Duffie-Singleton Model 
Single-valued standard Brown-
ian motion, 459 
Singular value decomposition, 162 
Skew-symmetric matrix, 147 
Sklar, A., 189 
Slack variable, 208 
Slowly varying function, 357 
Small Cap 600 Index, 561 
Small capitalization stocks, 3 

Index 
775 
Smith, Adam, 77, 83 
Smith, Adrian F.M., 316 
Smith, R.L., 375 
Sochacki, James, 635 
Software 
development, 16 
optimization packages, 212 
Solutions, stability, 256–258 
Solvers, usage, 206 
Sopranzetti, Ben J., 722, 724 
Sorbonne University, 78 
Sornette, D., 331, 390, 492 
Sortino, Frank, 751 
Souma, W., 388 
Sovereign risk, 611 
Spacings, 369 
Spanos, A., 531 
Specialized bond market indexes, 
649 
Specific risk, 578, 582 
Speculator, expectation, 79 
Splines, 643 
Spot interest rates, 625 
Spot rates, 623 
continuous case, 624–625 
curve. See Theoretical spot 
rate curve 
construction. See Continu-
ous spot rate curve 
obtaining, 
Treasury 
yield 
curve (usage), 603–605 
usage. See Bonds 
Spread-based diffusion models, 710 
Square integral, 223 
Square matrices, 145–148, 160. 
See also Symmetric square 
matrix 
Srom, S., 342 
Stability of solutions. See Solu-
tions 
Stable distributions, 360–362 
Stable inverse Gaussian distri-
butions, 361 
Stable laws, 351–362, 366 
application, 390 
Standard & Poor’s (S&P) 
classification, 536 
Composite Index, 561 
Standard & Poor’s (S&P) 500, 
70, 94–95, 332 
application, 345 
Composite, 46–47 
index, 497–498, 521, 561 
matching, 587 
Standard 
Brownian 
motion, 
447–448, 453. See also 
Single-valued 
standard 
Brownian motion 
correlation, 741 
drift, addition, 459 
equivalent martingale mea-
sure, 627, 639 
Standard extreme value distri-
butions, 365 
Standard form, transformation, 
207 
Standard Generalized Extreme 
Value Distribution, 368 
Standard normal distribution, 
194 
Standard notation, 109 
Stanley, H. Eugene, 390, 522 
Starica, C., 385 
State price deflator, 400, 404– 
405, 454 
computation, 409, 413 
definition, 456 
existence, 467 
linear combination, 434 
representation, 408 
usage, 457, 465 
yield, 410 
State prices, 397–398 
equivalent Martingale mea-
sures, usage, 464–466 
vector, 397 
normalization, 398 
States, real probabilities, 425 
State-space cointegration, 342 
State-space modeling, 12, 309, 
342 
linear form, 384 
State-space models, 286, 288, 
305, 379 
equivalence, 541 
estimation, 538 
State-space representation, 305– 
309 
equivalence, 308–309 
State-space system, 308 
Static replication, 710 
Static-factor model, 543 
Stationarity, condition, 292 
Stationary disturbance, 341, 342 
Stationary IID sequence, 268 
Stationary increments (sssi), 387 
Stationary multivariate ARMA 
models, 301–304 
Stationary processes. See Autore-
gressive moving average 
Stationary 
sequence. 
See 
Asymptotically self-simi-
lar stationary sequence 
Stationary series. See Difference 
stationary series; Multi-
variate stationary series; 
Trend stationary series 
Wold representation, 296 
Stationary time series, 285 
Stationary univariate ARMA 
models, 297–300 
Stationary univariate moving 
average, 292–293 
Stationary VAR model, 539 
Statistical arbitrage, 575–577 
Statistical nonlinear pattern rec-
ognition, 574 
Statutory surplus, 40 
Stegun, Irene A., 249 
Stepup notes, 54–55. See also 
Multiple 
stepup 
note; 
Single stepup note 
Stigler, George, 29, 30 
Stochastic calculus, 93 
Stochastic differential equation 
(SDE), 217, 240, 267, 
274–276. 
See 
also 
Brownian motion; Geo-
metric Brownian motion 
association, 630 
definition, 270–271 
intuition, 268–271 
solution, 278–282 
Stochastic discount function, 494 
Stochastic environment, 218 
Stochastic general equilibrium 
theory, 86 
Stochastic hazard rate, need, 716 
Stochastic integrals, 217 
defining. See Processes 
definition, 221, 223, 232– 
236. See also Elemen-
tary functions 
intuition, 219–224 
properties. See Ito stochastic 
integrals 
Stochastic integration, 217 
Stochastic 
optimization. 
See 
Multiperiod 
stochastic 
optimization 
Stochastic processes, 178–180 
adaptation, 183 
realization, 217 
vector, 277 
Stochastic programming, 202, 
213–215, 673–677. See 
also Multistage stochas-
tic programming 
Stochastic recovery, 703 
Stochastic trend, 310 
Stochastic variables, 32, 85 
Stochastic volatility models, 12, 
740–742 
Stock, James H., 334, 540, 543 
Stock market, 25 
index, risk control, 587 
indicators, 46–48 
short-term movements, 572 
Stock price 
binomial model, 424 
decreases, 287 
nonnegative numbers, 395 
position, 686 
processes, 447–448 
Stocks 
cointegrated pairs, searching, 
576–577 
indexes, types, 93–94 
intrinsic value, 567 
positions, hedging, 743 
returns, distribution, 287 
Stop-limit order, 48–49 
Stopping time, 429 
Stork, David G., 562 

776 
Index 
Strategic bond/equity mix, 498 
Strategic return/risk decisions, 508 
Stratified sampling, 650 
Stratonovich, Ruslan L., 79, 221, 
224, 269 
Strike price, 64, 68. See also 
Internal strike price 
value, 69 
Strong consistency, 376 
Strong Duality theorem, 210 
Strong Laws of Large Numbers 
(SLLN), 358, 360 
Strong solution, 275, 739 
Strong-form efficiency, 32 
Stroughair, John D., 378 
Structural form models, 696 
Structural models, 684. See also 
Barrier structural model 
advantages/drawbacks, 696 
binomial process, 700 
Structural-based models, 711 
Structured portfolio strategies, 6 
Stylized facts, 286 
Subexponential 
distributions, 
354–356 
Subexponentiality, indicators, 256 
Subordinate basket credit default 
swaps, 681–683 
Subordinate basket default swaps, 
682 
Subordinated models, 380 
Subordinated processes, 383–384 
Subsets. See Proper subsets 
Subspace algorithm, 538, 544 
Subspace-space algorithm, 544 
Sum rule, 109 
Summand 
derivatives, computation, 113 
number, restriction, 296 
second derivatives, calcula -
tion, 119 
Summation. See Absolute sum -
mation 
Summers, L., 343 
Supply-and-demand equilibrium, 77 
Supremum, usage, 99 
Survival function, 352 
Survival probability, 688, 698, 712– 
713, 719. See also One-year 
survival probability; Total 
survival probability 
computation, 713–715 
labeling, 719 
Swaps, 69–70. See also Credit 
default 
swaps; 
Default 
swap; Nth to default swaps 
agreements, 26 
curves, 608–612 
construction, maturity points, 
611 
market, government regulation, 610 
premium, 680 
Switching models. See Markov 
switching models 
Symmetric Cauchy distributions, 361 
Symmetric risk/reward relation -
ship, 66 
Symmetric square matrix, 147 
System, minimal size, 307 
Systematic risk, 513–517, 525, 
582. See also Nonsys-
tematic risk 
exposure, 656–660. See also 
Nonsystematic risk 
factors, 86, 652, 654. See also 
Unsystematic risk factors 
Systematic-residual risk decom-
position, 578–580 
Tails 
closure property, 360 
index, 356 
Takayama, Akira, 483 
Takayasu, H., 388 
Takayasu, M., 388 
Tangency portfolio, 485 
Tangible assets, 21–22. See also 
Intangible assets 
Taqqu, M.S., 355, 387, 389 
Tartaglia, Nunzio, 576 
Tasche, Dirk, 749 
Taxation, issues, 5–6 
Taxes. See Capital gains 
status, 22. See also Financial 
assets 
Taylor expansion, 367 
Taylor series 
expansion, 121–126 
usage, 124–125, 126 
Taylor’s theorem, 121 
t-distribution, 392 
Technical analysis, 567, 574 
strategies, 571–573 
Teicher, Henry, 174, 193 
Tempered distributions, 268 
Term structure. See Hazard 
rates; Interest rates; Yield 
determination, 625 
factors, 656 
HJM Model, 640–643 
liquidity theory, 617 
model. See Multifactor term 
structure model 
examples. See One-factor 
term structure models 
principal component analysis, 
632 
risk, 658 
factors, 653 
shape (determinants), classi-
cal economic theories, 
612–618 
Term to maturity, 22–24. See 
also Bonds 
Terminal payoff, 707 
Termination date, 680. See also 
Scheduled termination date 
Termination value. See Credit 
default swaps 
Termwise differentiation, rule, 
108–109 
Testing, 315 
Thaler, Richard, 572 
Theorem of existence. See Exist -
ence 
Theorem of uniqueness. See Unique-
ness 
Theoretical futures price, 61–62 
Theoretical spot rate curve, 603 
Thin market, 23 
Tick-test rules, 49 
Time correlation. See Defaults 
Time horizon, 731 
Time intervals, 247 
Time invariance, 294 
Time premium. See Options 
Time series, 335. See also Finan -
cial time series; Univari-
ate time series 
autoregressive representation, 
288–297 
concepts, 283–286 
infinite moving average, 288–297 
Time-dependent 
autocovari -
ance function, 294 
Time-independent autocorrela -
tion function, 303 
Time-path continuity, 234 
Time-separable utility function, 
492 
Time-variable economic quanti -
ties, 225 
Time-varying interest rates, con -
tinuous compounding, 246 
Tobin, James, 22, 24, 477 
Todd, Peter, 477 
Toft, Klaus Bjerre, 716 
Top-down approaches. See Active 
investing 
Top-down investing, macroeco -
nomic outlook, 567 
Top-down passive approaches, 
566 
Total excess return, 578 
Total excess risk, 578 
Total market capitalization, 1 
Total 
protection 
value. 
See 
Default swap 
Total risk, 515 
decomposition, 578 
Total survival probability, 712 
Total variation, 105–106 
Toy, William, 638. See also Black- 
Derman-Toy Model 
Tracking errors, 552–560, 654. See 
also Actual tracking error; 
Annual 
tracking 
error; 
Backward-looking 
track-
ing errors; Forward-looking 
tracking errors; Monthly 
tracking error; Portfolios 

Index 
777 
Tracking errors (Cont.) 
bond 
portfolio 
strategies, 
relationship, 651–652 
determinants, 654 
minimization, 558 
multi-factor risk approach, 9 
portfolio beta, 556–560 
Tracking portfolio, 564 
Trade horizon, 734 
Trading. See Pair trading 
activity, 532 
constraints, 664 
costs, control, 552 
date, 180 
gains, 443–445 
halts, 28 
restrictions, 28 
strategies, 403–404, 443–445 
Traditional asset classes, 3–4 
Training data, 318 
Transactions 
costs, 32, 63. See also Capital 
market 
frequency, 23 
Transforms. See Fourier trans-
forms; Integrals; Laplace 
transform 
Transition matrix, 542, 703–706 
Transpose. See Matrices 
operation, 153–154, 156–157 
Treasury yield curve. See U.S. 
Treasury yield curve 
Trend stationary series, 309. See 
also 
Multidimensional 
trend stationary series 
Trends. See Integrated trends 
Triangular matrix. See Lower 
triangular matrix; Upper 
triangular matrix 
Turnbull, Stuart, 684, 696, 698, 
703, 730. See also Jar- 
row-Turnbull Model 
Turner, Christopher, 690 
Two-factor stochastic volatility 
model, 741 
Two-sided Laplace transform, 
134–135 
Two-sided transform, 136 
Two-stage stochastic optimiza -
tion problem, 676–677 
Unbiased expectations theory, 
616–617 
Uncertainty, 737 
representation, mathematics 
(usage), 165–167 
Uncorrelated variables, 188 
Underlying asset 
current price, 68 
position, 65 
Underwriting. See Securities 
Undiversification, quantification, 
472 
Unexpected Loss (UL), 391, 747 
Unique risk, 515 
Uniqueness, theorem, 274 
Univariate ARMA models. See 
Nonstationary 
univariate 
ARMA models; Stationary 
univariate ARMA models 
Univariate marginal distribu -
tions, 732 
Univariate moving average. See 
Stationary univariate mov-
ing average 
Univariate normal distribution, 194 
Univariate stationary series, 288– 
289 
Univariate time series, 340 
University of Chicago, 81 
University of Dijon, 79 
University of Lausanne, 77 
Unstructured data/information, 16 
Unsystematic risk, 515 
elimination, 556 
factors, 86 
Upper Riemann sum, 127 
Upper triangular matrix, 148 
Upstairs market, 50 
Uryasev, Stanislav, 749 
U.S. bonds, 3
U.S. Department of Energy (DOE),
11 
U.S. Federal Reserve, 754–755
U.S. government bonds, 3
U.S. municipal bonds, 4
U.S. Office of the Controller of
the Currency. See Quar-
terly Derivatives Report 
U.S. Treasury bonds, 600, 606 
U.S. Treasury market, 632 
U.S. Treasury spot rates, 606 
U.S. Treasury strips, 667 
U.S. Treasury yield curve, 599 
construction, 600 
measurement, 601 
usage, 602. See also Spot rates 
U.S. 
 Treasury 
zero-coupon 
bonds, 667 
Utility functions, 77, 482–484, 
487–490. See also Linear 
utility function; Loga-
rithmic utility function; 
Power utility function; 
Quadratic utility func-
tion; Time-separable util-
ity function 
defining, 82 
Utility maximization framework, 
491 
Valuation. See American options; 
European simple derivatives 
formula, 429 
principles. See Debt instruments 
Value 
stocks, 3 
understanding, 83–85 
Value at Risk (VaR), 748. See 
also Conditional VaR 
noncoherence, 749 
Value Line Composite Average 
(VLCA), 46, 47 
Van Meer, Robert, 751 
van Norden, Simon, 545 
Vanguard Group, 650 
Vapnik, Vladimir N., 317, 319 
Vapnik-Chervonenkis (VC) the -
ory. See Learning 
Vardharaj, Raman, 532, 556, 558, 
582, 583, 586, 588. 590 
Variable interest rates, convex -
ity, 120 
Variable short-term rates, 619 
Variables, 101. See also Gaussian 
variables; Random vari-
ables; Stochastic variables; 
Uncorrelated variables 
calculus, usage, 138–139 
characteristic function, 193 
co-movement, 189 
covariance, 328 
definition, 101 
IID sequence, 537 
sum, 191–193 
Variance portfolios. See Mini-
mum variance portfolios 
Variance-covariance matrix, 82, 147, 
324, 329. See also Diagonal 
variance-covariance matrix; 
n×n symmetrical variance- 
covariance matrix 
eigenvalue, 336 
modeling, 347 
PCA, performing, 543 
usage, 335, 534 
values. See Factor variance- 
covariance matrix 
Variances 
growth, 277 
standard deviations, substitu -
tions, 481 
Variation margin, 58, 62 
Variational methodologies, 674 
Variational principle, 673–674 
Variations. See Total variation 
calculus, 201–202, 212–214 
VARMA model, 542 
Vasicek, Oldrich, 636 
Vasicek Model, 635, 636 
Vector Autoregressive (VAR). See 
One-lag stationary VAR 
models, 316, 338, 348. See 
also Global VAR model; 
Stationary VAR model 
usage, 541 
Vector support machines, 547 
Vectors, 141–144. See also Column 
vectors; Eigenvectors; Ran-
dom vectors; Row vectors 
autoregressive models, 338–339 
components, 141–142 
Euclidean length, 143 
norm, 143 
operations, 153–156 

778 
Index 
Vector-valued function, 175 
Vladimirou, Hercules, 473 
Volatility. See Assets; Equity 
clustering phenomena, 753 
decays, 378 
impact. See Benchmarks; White 
noise 
models. See Stochastic volatil-
ity models 
Volpert, Kenneth E., 650 
von Mises, Richard, 166 
Waeb-based researech portals, 
usage, 17 
Wagner, M., 345, 538, 544 
Wagner, N., 377 
Wagner, Wayne H., 416, 551 
Wallace, Anise, 525 
Wallace, Stein W., 202, 677 
Wallis, J.R., 375 
Walras, Leon, 75–78 
Wang, Zhenyu, 523 
Watanabe, S., 221 
Watson, Mark W., 334, 540, 543 
Weak consistency, 376 
Weak efficiency, 32 
Weak Laws of Large Numbers 
(WLLN), 358 
Weak solution, 275, 739 
Weibull distribution, 362–363, 365 
MDA, 367 
Weil, R.L., 667 
West, Richard R., 31 
White, Alan, 636, 711, 717. See 
also Hull-White Model 
White noise, 268. See also Con-
tinuous-time white noise; 
Multivariate white noise 
inputs, 308 
process. See n-dimensional zero-
mean white noise process; 
One-dimensional 
zero-
mean white noise process 
volatility, impact, 346–347 
Wiener process, 687 
Wigner, Eugene, 92 
Williams, George, 637 
Wilshire Associates, 46–48, 521 
Wilson, Kenneth, 11 
Wold representation. See Station-
ary series 
Wood, E.F., 375 
World Bank, 51 
Wright, David J., 649 
Wu, Wei, 652, 654, 656, 657, 
662, 663 
Yamai, Yasuhiro, 749 
Yield. See Premium par yield 
curve. See Inverted yield curve; 
Normal yield curve 
risk, 671 
term structure, 599–612 
reinvestment, 598–599 
Yield-maturity relationship, non-
uniqueness, 602 
Yield-to-maturity measure, 596–599 
Yield-to-maturity theory, 616, 617 
Yoshiba, Toshinao, 749 
Zadeh, Lotfi A., 165 
Zahlen, 97 
Zellner, Arnold, 748 
Zenios, Stavros, 487, 492, 666, 
671, 674, 676 
Zero matrix, 146 
Zero-beta portfolio, 522 
Zero-coupon bond, 53, 599, 619, 
639. See also Defaultable 
zero-coupon bond 
arbitrage-free prices, 638 
computation, 639 
expiration, 691 
two-year, 708 
value, 603 
yield, identification, 602 
Zero-coupon risk-free bond, 623 
Zero-coupon Treasury debt issues, 
603 
Zero-coupon Treasury securities, 
package, 604 
Zhou, Chunsheng, 695 
Zipf’s law, 357, 369 
statement, 370 

