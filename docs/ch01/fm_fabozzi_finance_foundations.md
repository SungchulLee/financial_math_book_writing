# Finance Foundations & Mathematical Prerequisites

!!! info "Source"
    **The Mathematics of Financial Modeling and Investment Management** by Sergio M. Focardi and Frank J. Fabozzi, Wiley, 2004.
    These notes are used for educational purposes.

## From Art to Engineering in Finance

I 
CHAPTER 1 
From Art to Engineering in 
Finance 
t is often said that investment management is an art, not a science. 
However since early 1990s the market has witnessed a progressive 
shift towards a more industrial view of the investment management pro-
cess. There are several reasons for this change. First, with globalization 
the universe of investable assets has grown many times over. Asset man-
agers might have to choose from among several thousand possible 
investments from around the globe. The S&P 500 index is itself chosen 
from a pool of 8,000 investable U.S. stocks. Second, institutional inves-
tors, often together with their investment consultants, have encouraged 
asset management firms to adopt an increasingly structured process 
with documented steps and measurable results. Pressure from regulators 
and the media is another factor. Lastly, the sheer size of the markets 
makes it imperative to adopt safe and repeatable methodologies. The 
volumes are staggering. With the recent growth of the world’s stock 
markets, total market capitalization is now in the range of tens of tril-
lions of dollars1 while derivatives held by U. S. commercial banks 
topped $65.8 trillion in the second quarter of 2003.2 
1 Exact numbers are difficult to come up with as information about many markets is 
missing and price fluctuations remain large. 
2 Office of the Comptroller of the Currency, Quarterly Derivatives Report, Second 
Quarter 2003. 
1 

2 
The Mathematics of Financial Modeling and Investment Management 
INVESTMENT MANAGEMENT PROCESS 
The investment management process involves the following five steps: 
Step 1: Setting investment objectives 
Step 2: Establishing an investment policy 
Step 3: Selecting an investment strategy 
Step 4: Selecting the specific assets 
Step 5: Measuring and evaluating investment performance 
The overview of the investment management process described below 
should help in understanding the activities that the portfolio manager 
faces and the need for the analytical tools that are described in the chap-
ters that follow in this book. 
Step 1: Setting Investment Objectives 
The first step in the investment management process, setting investment 
objectives, begins with a thorough analysis of the investment objectives 
of the entity whose funds are being managed. These entities can be clas-
sified as individual investors and institutional investors. Within each of 
these broad classifications is a wide range of investment objectives. 
The objectives of an individual investor may be to accumulate funds 
to purchase a home or other major acquisitions, to have sufficient funds to 
be able to retire at a specified age, or to accumulate funds to pay for col-
lege tuition for children. An individual investor may engage the services of 
a financial advisor/consultant in establishing investment objectives. 
In Chapter 3 we review the different types of institutional investors. 
We will also see that in general we can classify institutional investors into 
two broad categories—those that must meet contractually specified liabil-
ities and those that do not. We can classify those in the first category as 
institutions with “liability-driven objectives” and those in the second cat-
egory as institutions with “nonliability driven objectives.” Some institu-
tions have a wide range of investment products that they offer investors, 
some of which are liability driven and others that are nonliability driven. 
Once the investment objective is understood, it will then be possible to (1) 
establish a “benchmark” or “bogey” by which to evaluate the performance 
of the investment manager and (2) evaluate alternative investment strate-
gies to assess the potential for realizing the specified investment objective. 
Step 2: Establishing an Investment Policy 
The second step in the investment management process is establishing 
policy guidelines to satisfy the investment objectives. Setting policy 

3 
From Art to Engineering in Finance 
begins with the asset allocation decision. That is, a decision must be 
made as to how the funds to be invested should be distributed among 
the major classes of assets. 
Asset Classes 
Throughout this book we refer to certain categories of investment prod-
ucts as an “asset class.” From the perspective of a U.S. investor, the con-
vention is to refer the following as traditional asset classes:
 ■ U.S. common stocks
 ■ Non-U.S. (or foreign) common stocks
 ■ U.S. bonds
 ■ Non-U.S. (or foreign) bonds
 ■ Cash equivalents
 ■ Real estate 
Cash equivalents are defined as short-term debt obligations that have 
little price volatility and are covered in Chapter 2. 
Common stocks and bonds are further divided into asset classes. 
For U.S. common stocks (also referred to as U.S. equities), the following 
are classified as asset classes: 
■ Large capitalization stocks
 ■ Mid-capitalization stocks
 ■ Small capitalization stocks
 ■ Growth stocks
 ■ Value stocks 
By “capitalization,” it is meant the market capitalization of the com-
pany’s common stock. This is equal to the total market value of all of 
the common stock outstanding for that company. For example, suppose 
that a company has 100 million shares of common stock outstanding 
and each share has a market value of $10. Then the capitalization of 
this company is $1 billion (100 million shares times $10 per share). The 
market capitalization of a company is commonly referred to as the 
“market cap” or simply “cap.” 
For U.S. bonds, also referred to as fixed-income securities, the fol-
lowing are classified as asset classes:
 ■ U.S. government bonds
 ■ Investment-grade corporate bonds
 ■ High-yield corporate bonds 

4 
The Mathematics of Financial Modeling and Investment Management
 ■ U.S. municipal bonds (i.e., state and local bonds)
 ■ Mortgage-backed securities
 ■ Asset-backed securities 
All of these securities are described in Chapter 2, where what is meant by 
“investment grade” and “high yield” are also explained. Sometimes, the 
first three bond asset classes listed above are further divided into “long 
term” and “short term.” 
For non-U.S. stocks and bonds, the following are classified as asset 
classes:
 ■ Developed market foreign stocks
 ■ Emerging market foreign stocks
 ■ Developed market foreign bonds
 ■ Emerging market foreign bonds 
In addition to the traditional asset classes, there are asset classes 
commonly referred to as alternative investments. Two of the more pop-
ular ones are hedge funds and private equity. 
How does one define an asset class? One investment manager, Mark 
Kritzman, describes how this is done as follows: 
... some investments take on the status of an asset class simply 
because the managers of these assets promote them as an asset 
class. They believe that investors will be more inclined to allocate 
funds to their products if they are viewed as an asset class rather 
than merely as an investment strategy.3 
He then goes on to propose criteria for determining asset class status. 
We won’t review the criteria he proposed here. They involve concepts 
that are explained in later chapters. After these concepts are explained it 
will become clear how asset class status is determined. However, it 
should not come as any surprise that the criteria proposed by Kritzman 
involve the risk, return, and the correlation of the return of a potential 
asset class with that of other asset classes. 
Along with the designation of an investment as an asset class comes 
a barometer to be able to quantify performance—the risk, return, and 
the correlation of the return of the asset class with that of another asset 
class. The barometer is called a “benchmark index,” “market index,” or 
simply “index.” 
3 Mark Kritzman, “Toward Defining an Asset Class,” The Journal of Alternative In-
vestments (Summer 1999), p. 79. 

5 
From Art to Engineering in Finance 
Constraints 
There are some institutional investors that make the asset allocation deci-
sion based purely on their understanding of the risk-return characteristics 
of the various asset classes and expected returns. The asset allocation 
will take into consideration any investment constraints or restrictions. 
Asset allocation models are commercially available for assisting those 
individuals responsible for making this decision. 
In the development of an investment policy, the following factors 
must be considered:
 ■ Client constraints
 ■ Regulatory constraints 
■ Tax and accounting issues 
Client-Imposed Constraints Examples of client-imposed constraints would 
be restrictions that specify the types of securities in which a manager 
may invest and concentration limits on how much or little may be 
invested in a particular asset class or in a particular issuer. Where the 
objective is to meet the performance of a particular market or custom-
ized benchmark, there may be a restriction as to the degree to which the 
manager may deviate from some key characteristics of the benchmark. 
Regulatory Constraints There are many types of regulatory constraints. 
These involve constraints on the asset classes that are permissible and 
concentration limits on investments. Moreover, in making the asset allo-
cation decision, consideration must be given to any risk-based capital 
requirements. For depository institutions and insurance companies, the 
amount of statutory capital required is related to the quality of the 
assets in which the institution has invested. There are two types of risk-
based capital requirements: credit risk-based capital requirements and 
interest rate-risk based capital requirements. The former relates statu-
tory capital requirements to the credit-risk associated with the assets in 
the portfolio. The greater the credit risk, the greater the statutory capi-
tal required. Interest rate-risk based capital requirements relate the stat-
utory capital to how sensitive the asset or portfolio is to changes in 
interest rates. The greater the sensitivity, the higher the statutory capital 
required. 
Tax and Accounting Issues Tax considerations are important for several rea-
sons. First, in the United States, certain institutional investors such as pen-
sion funds, endowments, and foundations are exempt from federal income 
taxation. Consequently, the assets in which they invest will not be those 
that are tax-advantaged investments. Second, there are tax factors that 

6 
The Mathematics of Financial Modeling and Investment Management 
must be incorporated into the investment policy. For example, while a pen-
sion fund might be tax-exempt, there may be certain assets or the use of 
some investment vehicles in which it invests whose earnings may be taxed. 
Generally accepted accounting principles (GAAP) and regulatory 
accounting principles (RAP) are important considerations in developing 
investment policies. An excellent example is a defined benefit plan for a 
corporation. GAAP specifies that a corporate pension fund’s surplus is 
equal to the difference between the market value of the assets and the 
present value of the liabilities. If the surplus is negative, the corporate 
sponsor must record the negative balance as a liability on its balance 
sheet. Consequently, in establishing its investment policies, recognition 
must be given to the volatility of the market value of the fund’s portfolio 
relative to the volatility of the present value of the liabilities. 
Step 3: Selecting a Portfolio Strategy 
Selecting a portfolio strategy that is consistent with the investment 
objectives and investment policy guidelines of the client or institution is 
the third step in the investment management process. Portfolio strate-
gies can be classified as either active or passive. 
An active portfolio strategy uses available information and forecast-
ing techniques to seek a better performance than a portfolio that is sim-
ply diversified broadly. Essential to all active strategies are expectations 
about the factors that have been found to influence the performance of 
an asset class. For example, with active common stock strategies this 
may include forecasts of future earnings, dividends, or price-earnings 
ratios. With bond portfolios that are actively managed, expectations 
may involve forecasts of future interest rates and sector spreads. Active 
portfolio strategies involving foreign securities may require forecasts of 
local interest rates and exchange rates. 
A passive portfolio strategy involves minimal expectational input, 
and instead relies on diversification to match the performance of some 
market index. In effect, a passive strategy assumes that the marketplace 
will reflect all available information in the price paid for securities. 
Between these extremes of active and passive strategies, several strategies 
have sprung up that have elements of both. For example, the core of a 
portfolio may be passively managed with the balance actively managed. 
In the bond area, several strategies classified as structured portfolio 
strategies have been commonly used. A structured portfolio strategy is 
one in which a portfolio is designed to achieve the performance of some 
predetermined liabilities that must be paid out. These strategies are fre-
quently used when trying to match the funds received from an invest-
ment portfolio to the future liabilities that must be paid. 

7 
From Art to Engineering in Finance 
Given the choice among active and passive management, which 
should be selected? The answer depends on (1) the client’s or money 
manager’s view of how “price-efficient” the market is, (2) the client’s 
risk tolerance, and (3) the nature of the client’s liabilities. By market-
place price efficiency we mean how difficult it would be to earn a greater 
return than passive management after adjusting for the risk associated 
with a strategy and the transaction costs associated with implementing 
that strategy. Market efficiency is explained in Chapter 3. 
Step 4: Selecting the Specific Assets 
Once a portfolio strategy is selected, the next step is to select the specific 
assets to be included in the portfolio. It is in this phase of the investment 
management process that the investor attempts to construct an efficient 
portfolio. An efficient portfolio is one that provides the greatest 
expected return for a given level of risk or, equivalently, the lowest risk 
for a given expected return. 
Inputs Required 
To construct an efficient portfolio, the investor must be able to quantify 
risk and provide the necessary inputs. As will be explained in the next 
chapter, there are three key inputs that are needed: future expected 
return (or simply expected return), variance of asset returns, and correla-
tion (or covariance) of asset returns. All of the investment tools 
described in the chapters that follow in this book are intended to provide 
the investor with information with which to estimate these three inputs. 
There are a wide range of approaches to obtain the expected return 
of assets. Investors can employ various analytical tools that will be dis-
cussed throughout this book to derive the future expected return of an 
asset. For example, we will see in Chapter 18 that there are various 
asset pricing models that provide expected return estimates based on 
factors that historically have been found to systematically affect the 
return on all assets. Investors can use historical average returns as their 
estimate of future expected returns. Investors can modify historical 
average returns with their judgment of the future to obtain a future 
expected return. Another approach is for investors to simply use their 
intuition without any formal analysis to come up with the future 
expected return. 
In Chapter 16, the reason why the variance of asset returns should 
be used as a measure of an asset’s risk will be explained. This input can 
be obtained for each asset by calculating the historical variance of asset 
returns. There are sophisticated time series statistical techniques that 
can be used to improve the estimated variance of asset returns that are 

8 
The Mathematics of Financial Modeling and Investment Management 
discussed in Chapter 18. Some investors calculate the historical variance 
of asset returns and adjust them based on their intuition. 
The covariance (or correlation) of returns is a measure of how the 
return of two assets vary together. Typically, investors use historical 
covariances of asset returns as an estimate of future covariances. But 
why is a covariance of asset returns needed? As will be explained in 
Chapter 16, the covariance is important because the variance of a port-
folio’s return depends on it and the key to diversification is the covari-
ance of asset returns. 
Approaches to Portfolio Construction 
Constructing an efficient portfolio based on the expected return for a 
portfolio (which depends on the expected return of all the asset returns 
in the portfolio) and the variance of the portfolio’s return (which 
depends on the variance of the return of all of the assets in the portfolio 
and the covariance of returns between all pairs of assets in the portfolio) 
are referred to as “mean-variance” portfolio management. The term 
“mean” is used because the expected return is equivalent to the “mean” 
or “average value” of returns. This approach also allows for the inclu-
sion of constraints such as lower and upper bounds on particular assets 
or assets in particular industries or sectors. The end result of the analy-
sis is a set of efficient portfolios—alternative portfolios from which the 
investor can select—that offer the maximum expected portfolio return 
for a given level of portfolio risk. 
There are variations on this approach to portfolio construction. 
Mean-variance analysis can be employed by estimating risk factors that 
historically have explained the variance of asset returns. The basic princi-
ple is that the value of an asset is driven by a number of systematic factors 
(or, equivalently, risk exposures) plus a component unique to a particular 
company or industry. A set of efficient portfolios can be identified based 
on the risk factors and the sensitivity of assets to these risk factors. This 
approach is referred to the “multifactor risk approach” to portfolio con-
struction and is explained in Chapter 19 for common stock portfolio 
management and Chapter 21 for fixed-income portfolio management. 
With either the full mean-variance approach or the multifactor risk 
approach there are two variations. First, the analysis can be performed 
by investors using individual assets (or securities) or the analysis can be 
performed on asset classes. 
The second variation is one in which the input used to measure risk is 
the tracking error of a portfolio relative to a benchmark index, rather 
than the variance of the portfolio return. By a benchmark index it is 
meant the benchmark that the investor’s performance is compared against. 

9 
From Art to Engineering in Finance 
As explained in Chapter 19, tracking error is the variance of the difference 
in the return on the portfolio and the return on the benchmark index. 
When this “tracking error multifactor risk approach” to portfolio con-
struction is applied to individual assets, the investor can identify the set of 
efficient portfolios in terms of a portfolio that matches the risk profile of 
the benchmark index for each level of tracking error. Selecting assets that 
intentionally cause the portfolio’s risk profile to differ from that of the 
benchmark index is the way a manager actively manages a portfolio. In 
contrast, indexing means matching the risk profile. “Enhanced” indexing 
basically means that the assets selected for the portfolio do not cause the 
risk profile of the portfolio constructed to depart materially from the risk 
profile of the benchmark. This tracking error multifactor risk approach to 
common stock and fixed-income portfolio construction will be explained 
and illustrated in Chapters 19 and 21, respectively. 
At the other extreme of the full mean-variance approach to portfolio 
management is the assembling of a portfolio in which investors ignore all 
of the inputs—expected returns, variance of asset returns, and covariance 
of asset returns—and use their intuition to construct a portfolio. We refer 
to this approach as the “seat-of-the-pants approach” to portfolio con-
struction. In a rising stock market, for example, this approach is too often 
confused with investment skill. It is not an approach we recommend. 
Step 5: Measuring and Evaluating Performance 
The measurement and evaluation of investment performance is the last step 
in the investment management process. Actually, it is misleading to say that 
it is the last step since the investment management process is an ongoing 
process. This step involves measuring the performance of the portfolio and 
then evaluating that performance relative to some benchmark. 
Although a portfolio manager may have performed better than a 
benchmark, this does not necessarily mean that the portfolio manager 
satisfied the client’s investment objective. For example, suppose that a 
financial institution established as its investment objective the maximi-
zation of portfolio return and allocated 75% of its funds to common 
stock and the balance to bonds. Suppose further that the manager 
responsible for the common stock portfolio realized a 1-year return that 
was 150 basis points greater than the benchmark.4 Assuming that the 
risk of the portfolio was similar to that of the benchmark, it would 
appear that the manager outperformed the benchmark. However, sup-
pose that in spite of this performance, the financial institution cannot 
4 A basis point is equal to 0.0001 or 0.01%. This means that 1% is equal to 100 basis 
points. 

10 
The Mathematics of Financial Modeling and Investment Management 
meet its liabilities. Then the failure was in establishing the investment 
objectives and setting policy, not the failure of the manager. 
FINANCIAL ENGINEERING IN HISTORICAL PERSPECTIVE 
In its modern sense, financial engineering is the design (or engineering) 
of contracts and portfolios of contracts that result in predetermined 
cash flows contingent to different events. Broadly speaking, financial 
engineering is used to manage investments and risk. The objective is the 
transfer of risk from one entity to another via appropriate contracts. 
Though the aggregate risk is a quantity that cannot be altered, risk can 
be transferred if there is a willing counterparty. Just why and how risk 
transfer is possible will be discussed in Chapter 23 on risk management. 
Financial engineering came to the forefront of finance in the 1980s, 
with the broad diffusion of derivative instruments. However the concept 
and practice of financial engineering are quite old. Evidence of the use 
of sophisticated cross-border instruments of credit and payment dating 
from the time of the First Crusade (1095–1099) has come down to us 
from the letters of Jewish merchants in Cairo. The notion of the diversi-
fication of risk (central to modern risk management) and the quantifica-
tion of insurance risk (a requisite for pricing insurance policies) were 
already understood, at least in practical terms, in the 14th century. The 
rich epistolary of Francesco Datini, a 14th century merchant, banker 
and insurer from Prato (Tuscany, Italy), contains detailed instructions to 
his agents on how to diversify risk and insure cargo.5 It also gives us an 
idea of insurance costs: Datini charged 3.5% to insure a cargo of wool 
from Malaga to Pisa and 8% to insure a cargo of malmsey (sweet wine) 
from Genoa to Southampton, England. These, according to one of 
Datini’s agents, were low rates: He considered 12–15% a fair insurance 
premium for similar cargo. 
What is specific to modern financial engineering is the quantitative 
management of uncertainty. Both the pricing of contracts and the opti-
mization of investments require some basic capabilities of statistical 
modeling of financial contingencies. It is the size, diversity, and effi-
ciency of modern competitive markets that makes the use of modeling 
imperative. 
5 Datini wrote the richest medieval epistolary that has come down to us. It includes 
500 ledgers and account books, 300 deeds of partnership, 400 insurance policies, 
and 120,000 letters. For a fascinating portrait of the business and private life of a 
medieval Italian merchant, see Iris Onigo, The Merchant of Prato (London: Penguin 
Books, 1963). 

11 
From Art to Engineering in Finance 
THE ROLE OF INFORMATION TECHNOLOGY 
Advances in information technology are behind the widespread adop-
tion of modeling in finance. The most important advance has been the 
enormous increase in the amount of computing power, concurrent with 
a steep fall in prices. Government agencies have long been using com-
puters for economic modeling, but private firms found it economically 
justifiable only as of the 1980s. Back then, economic modeling was con-
sidered one of the “Grand Challenges” of computational science.6 
In the late 1980s, firms such as Merrill Lynch began to acquire super-
computers to perform derivative pricing computations. The overall cost 
of these supercomputing facilities, in the range of several million dollars, 
limited their diffusion to the largest firms. Today, computational facilities 
ten times more powerful cost only of a few thousand dollars. 
To place today’s computing power in perspective, consider that a 
1990 run-of-the-mill Cray supercomputer cost several million U.S. dol-
lars and had a clock cycle of 4 nanoseconds (i.e., 4 billionths of a sec-
ond or 250 million cycles per second, notated as 250 MHz). Today’s fast 
laptop computers are 10 times faster with a clock cycle of 2.5 GHz and, 
at a few thousand dollars, cost only a fraction of the price. Supercom-
puter performance has itself improved significantly, with top computing 
speed in the range of several teraflops7 compared to the several mega-
flops of a Cray supercomputer in the 1990s. In the space of 15 years, 
sheer performance has increased 1,000 times while the price-perfor-
mance ratio has decreased by a factor of 10,000. Storage capacity has 
followed similar dynamics. 
The diffusion of low-cost high-performance computers has allowed 
the broad use of numerical methods. Computations that were once per-
formed by supercomputers in air-conditioned rooms are now routinely 
6 Kenneth Wilson, “Grand Challenges to Computational Science,” Future Genera-
tion Computer Systems 5 (1989), p. 171. The term “Grand Challenges” was coined 
by Kenneth Wilson, recipient of the 1982 Nobel Prize in Physics, and later adopted 
by the U.S. Department Of Energy (DOE) in its High Performance Communications 
and Computing Program which included economic modeling among the grand chal-
lenges. Wilson was awarded the Nobel Prize in Physics for discoveries he made in 
understanding how bulk matter undergoes “phase transition,” i.e., sudden and pro-
found structural changes. The mathematical techniques he introduced—the renor-
malization group theory—is one of the tools used to understand economic phase 
transitions. Wilson is an advocate of computational science as the “third way” of do-
ing science, after theory and experiment. 
7 A flops (Floating Point Operations Per Second) is a measure of computational 
speed. A Teraflop computer is a computer able to perform a trillion floating point 
operations per second. 

12 
The Mathematics of Financial Modeling and Investment Management 
performed on desk-top machines. This has changed the landscape of 
financial modeling. The importance of finding closed-form solutions and 
the consequent search for simple models has been dramatically reduced. 
Computationally-intensive methods such as Monte Carlo simulations 
and the numerical solution of differential equations are now widely 
used. As a consequence, it has become feasible to represent prices and 
returns with relatively complex models. Nonnormal probability distri-
butions have become commonplace in many sectors of financial model-
ing. It is fair to say that the key limitation of financial econometrics is 
now the size of available data samples or training sets, not the computa-
tions; it is the data that limits the complexity of estimates. 
Mathematical modeling has also undergone major changes. Tech-
niques such as equivalent martingale methods are being used in deriva-
tive pricing (Chapter 15) and cointegration (Chapter 11), the theory of 
fat-tailed processes (Chapter 13), and state-space modeling (including 
ARCH/GARCH and stochastic volatility models) are being used in 
econometrics (Chapter 11). 
Powerful specialized mathematical languages and vast statistical 
software libraries have been developed. The ability to program sequences 
of statistical operations within a single programming language has been 
a big step forward. Software firms such as Mathematica and Math-
works, and major suppliers of statistical tools such as SAS, have created 
simple computer languages for the programming of complex sequences 
of statistical operations. This ability is key to financial econometrics 
which entails the analysis of large portfolios.8 
Presently only large or specialized firms write complex applications 
from scratch; this is typically done to solve specific problems, often in 
the derivatives area. The majority of financial modelers make use of 
high-level software programming tools and statistical libraries. It is dif-
ficult to overestimate the advantage brought by these software tools; 
they cut development time and costs by orders of magnitude. 
In addition, there is a wide range of off-the-shelf financial applica-
tions that can be used directly by operators who have a general under-
standing of the problem but no advanced statistical or mathematical 
training. For example, powerful complete applications from firms such as 
Barra and component applications from firms such as FEA make sophisti-
cated analytical methods available to a large number of professionals. 
Data have, however, remained a significant expense. The diffusion 
of electronic transactions has made available large amounts of data, 
8 A number of highly sophisticated statistical packages are available to economists. 
These packages, however, do not serve the needs of the financial econometrician who 
has to analyze a large number of time series. 

13 
From Art to Engineering in Finance 
including high-frequency data (HFD) which gives us information at the 
transaction level. As a result, in budgeting for financial modeling, data 
have become an important factor in deciding whether or not to under-
take a new modeling effort. 
A lot of data are now available free on the Internet. If the required 
granularity of data is not high, these data allow one to study the viabil-
ity of models and to perform rough tuning. However, real-life applica-
tions, especially applications based on finely grained data, require data 
streams of a higher quality than those typically available free on the 
Internet. 
INDUSTRY’S EVALUATION OF MODELING TOOLS 
A recent study by The Intertek Group9 tried to assess how the use of 
financial modeling in asset management had changed over the highly 
volatile period from 2000 to 2002. Participants in the study included 44 
heads of asset management firms in Europe and North America; more 
than half were from the biggest firms in their home markets. 
The study found that the role of quantitative methods in the invest-
ment decision-making process had increased at almost 75% of the firms 
while it had remained stable at about 15% of the firms; five reported 
that their process was already essentially quantitative. Demand pull and 
management push were among the reasons cited for the growing role of 
models. The head of risk management and product control at an inter-
national firm said, “There is genuinely a portfolio manager demand pull 
plus a top-down management push for a more systematic, robust pro-
cess.” Many reported that fund managers have become more eager con-
sumers of modeling. “Fund managers now perceive that they gain 
increased insights from the models,” the head of quantitative research at 
a large northern European firm commented. 
In another finding, over one half of the participants evaluated that 
models had performed better in 2002 than two years ago; some 20% 
evaluated 2002 model performance to be stable with respect to the previ-
ous two years while another 20% considered that performance worsened. 
Performance was widely considered to be model-dependent. Among 
those that believed that model performance had improved, many attrib-
uted better performance to a better understanding of models and the 
modeling process at asset management firms. Some firms reported hav-
9 Caroline Jonas and Sergio Focardi, Trends in Quantitative Methods in Asset Man-
agement, 2003, The Intertek Group, Paris, 2003. 

14 
The Mathematics of Financial Modeling and Investment Management 
ing in place a formal process in which management was systematically 
trained in modeling and mathematical methods. 
The search for a silver bullet typical of the early days of “rocket sci-
ence” in finance has passed; modeling is now widely perceived as an 
approximation, with the various models shedding different light on the 
same phenomena. Just under 60% of the participants in the 2002 study 
indicated having made significant changes to their modeling approach 
from 2000 to 2002; for many others, it was a question of continuously 
recalibrating and adapting the models to the changing environment.10 
Much of the recent attention on quantitative methods has been 
focused on risk management—a relatively new function at asset man-
agement firms. More than 80% of the firms participating in the Intertek 
study reported a significant evolution of the role of risk management 
from 2000 to 2002. Some of the trends revealed by the study included 
daily or real-time risk measurement and the splitting of the role of risk 
management into two separate functions, one a support function to the 
fund managers, the other a central control function reporting to top 
management. These issues will be discussed in Chapter 23. 
In another area which is a measure of an increasingly systematic 
process, more than 60% of the firms in the 2002 study reported having 
formalized procedures for integrating quantitative and qualitative input, 
though half mentioned that the process had not gone very far and 30% 
reported no formalization at all. One way the integration is being han-
dled is through management structures for decision-making. A source at 
a large player in the bond market said, “We have regularly scheduled 
meetings where views are expressed. There is a good combination of 
views and numbers crunched. The mix between quantitative and quali-
tative input will depend on the particular situation. For example, if 
models are showing a 4 or 5 standard deviation event, fundamental 
analysis would have to be very strong before overriding the models.” 
Many firms have cast integration in a quantitative framework. The 
head of research at a large European firm said, “One year ago, the inte-
gration was totally fuzzy, but during the past year we have made the 
integration extremely rigorous. All managers now need to justify their 
statements and methods in a quantitative sense.” Some firms are priori-
tizing the inputs from various sources. A business manager at a Swiss 
firm said, “We have recently put in place a scoring framework which 
pulls together the gut feeling of the fund manager and the quantitative 
10 Financial models are typically statistical models that have to be estimated and cal-
ibrated. The estimation and calibration of models will be discussed in Chapter 23. 
The above remarks reflect the fact that financial models are not “laws of nature” but 
relationships valid only for a limited span of time. 

15 
From Art to Engineering in Finance 
models. We will be taking this further. The objective is to more tightly 
link the various inputs, be they judgmental or model results.” 
Some firms see the problem as one of model performance evalua-
tion. “The integration process is becoming more and more institutional-
ized,” said the head of quantitative research at a big northern European 
firm. “Models are weighted in terms of their performance: if a model 
has not performed so well, its output is less influential than that of mod-
els which have performed better.” 
In some cases, it is the portfolio manager himself who assigns weights 
to the various inputs. A source at a large firm active in the bond markets 
said, “Portfolio managers weight the relative importance of quantitative 
and qualitative input in function of the security. The more complex the 
security, the greater the quantitative weighting; the more macro, long-
term, the less the quantitative input counts: Models don’t really help 
here.” Other firms have a fixed percentage, such as 50/50, as corporate 
policy. Outside of quantitatively run funds, the feeling is that there is a 
weight limit in the range of 60–80% for quantitative input. “There will 
always be a technical and a tactical element,” said one source. 
Virtually all firms reported a partial automation in the handling of 
qualitative information, with some 30% planning to add functionality over 
and above the filtering and search functionality now typically provided by 
the suppliers of analyst research, consensus data and news. About 25% of 
the participants said that they would further automate the handling of 
information in 2003. The automatic summarization and analysis of news 
and other information available electronically was the next step for several 
firms that had already largely automated the investment process. 
INTEGRATING QUALITATIVE AND QUANTITATIVE INFORMATION 
Textual information has remained largely outside the domain of quanti-
tative modeling, having long been considered the domain of judgment. 
This is now changing as financial firms begin to tackle the problem of 
what is commonly called information overload; advances in computer 
technology are again behind the change.11 
Reuters publishes the equivalent of three bibles of (mostly financial) 
news daily; it is estimated that five new research documents come out of 
Wall Street every minute; asset managers at medium-sized firms report 
receiving up to 1,000 e-mails daily and work with as many as five 
11 Caroline Jonas and Sergio Focardi, Leveraging Unstructured Data in Investment 
Management, The Intertek Group, Paris, 2002. 

16 
The Mathematics of Financial Modeling and Investment Management 
screens on their desk. Conversely, there is also a lack of “digested” 
information. It has been estimated that only one third of the roughly 
10,000 U.S. public companies are covered by meaningful Wall Street 
research; there are thousands of companies quoted on the U.S. 
exchanges with no Wall Street research at all. It is unlikely the situation 
is better relative to the tens of thousands of firms quoted on other 
exchanges throughout the world. Yet increasingly companies are pro-
viding information, including press releases and financial results, on 
their Web sites, adding to the more than 3.3 billion pages on the World 
Wide Web as of mid-2003. 
Such unstructured (textual) information is progressively being 
transformed into self-describing, semistructured information that can be 
automatically categorized and searched by computers. A number of 
developments are making this possible. These include:
 ■ The development of XML (eXtensible Markup Language) standards 
for tagging textual data. This is taking us from free text search to que-
ries on semi-structured data.
 ■ The development of RDF (Resource Description Framework) stan-
dards for appending metadata. This provides a description of the 
content of documents.
 ■ The development of algorithms and software that generate taxonomies 
and perform automatic categorization and indexation.
 ■ The development of database query functions with a high level of 
expressive power.
 ■ The development of high-level text mining functionality that allows 
“discovery.” 
The emergence of standards for the handling of “meaning” is a 
major development. It implies that unstructured textual information, 
which some estimates put at 80% of all content stored in computers, 
will be largely replaced by semistructured information ready for 
machine handling at a semantic level. Today’s standard structured data-
bases store data in a prespecified format so that the position of all ele-
mentary information is known. For example, in a trading transaction, 
the date, the amount exchanged, the names of the stocks traded and so 
on are all stored in predefined fields. However, textual data such as 
news or research reports, do not allow such a strict structuring. To 
enable the computer to handle such information, a descriptive metafile 
is appended to each unstructured file. The descriptive metafile is a struc-
tured file that contains the description of the key information stored in 
the unstructured data. The result is a semistructured database made up 
of unstructured data plus descriptive metafiles. 

17 
From Art to Engineering in Finance 
Industry-specific and application-specific standards are being devel-
oped around the general-purpose XML. At the time of this writing, 
there are numerous initiatives established with the objective of defining 
XML standards for applications in finance, from time series to analyst 
and corporate reports and news. While it is not yet clear which of the 
competing efforts will emerge as the de facto standards, attempts are 
now being made to coordinate standardization efforts, eventually 
adopting the ISO 15022 central data repository as an integration point. 
Technology for handling unstructured data has already made its 
way into the industry. Factiva, a Dow Jones-Reuters company, uses 
commercially available text mining software to automatically code and 
categorize more than 400,000 news items daily, in real time (prior to 
adopting the software, they manually coded and categorized some 
50,000 news articles daily). Users can search the Factiva database which 
covers 118 countries and includes some 8,000 publications, and more 
than 30,000 company reports with simple intuitive queries expressed in 
a language close to the natural language. Suppliers such as Multex use 
text mining technology in their Web-based research portals for clients 
on the buy and sell sides. Such services typically offer classification, 
indexation, tagging, filtering, navigation, and search. 
These technologies are helping to organize research flows. They 
allow to automatically aggregate, sort, and simplify information and 
provide the tools to compare and analyze the information. In serving to 
pull together material from myriad sources, these technologies will not 
only form the basis of an internal knowledge management system but 
allow to better structure the whole investment management process. 
Ultimately, the goal is to integrate data and text mining in applications 
such as fundamental research and event analysis, linking news, and 
financial time series. 
PRINCIPLES FOR ENGINEERING A SUITE OF MODELS 
Creating a suite of models to satisfy the needs of a financial firm is engi-
neering in full earnest. It begins with a clear statement of the objectives. 
In the case of financial modeling, the objective is identified by the type of 
decision-making process that a firm wants to implement. The engineering 
of a suite of financial models requires that the process on which decisions 
are made is fully specified and that the appropriate information is sup-
plied at every step. This statement is not as banal as it might seem. 
We have now reached the stage where, in some markets, financial 
decision–making can be completely automated through optimizers. As we 

18 
The Mathematics of Financial Modeling and Investment Management 
will see in the following chapters, one can define models able to construct 
a conditional probability distribution of returns. An optimizer will then 
translate the forecast into a tradable portfolio. The manager becomes a 
kind of high-level supervisor of an otherwise automated process. 
However, not all financial decision-making applications are, or can 
be, fully automated. In many cases, it is the human operator who makes 
the decision, with models supplying the information needed to arrive at 
the decision. Building an effective suite of financial models requires 
explicit decisions as to (1) what level of automation is feasible and 
desirable and (2) what information or knowledge is required. 
The integration of different models and of qualitative and quantita-
tive information is a fundamental need. This calls for integration of dif-
ferent statistical measures and points of view. For example, an asset 
management firm might want to complement a portfolio optimization 
methodology based on Gaussian forecasting with a risk management 
process based on Extreme Value Theory (see Chapter 13). The two pro-
cesses offer complementary views. In many cases, however, different 
methodologies give different results though they work on similar princi-
ples and use the same data. In these cases, integration is delicate and 
might run against statistical principles. 
In deciding which modeling efforts to invest in, many firms have in 
place a sophisticated evaluation system. “We look at the return on 
investment [ROI] of a model: How much will it cost to buy the data 
necessary to run the model? Then we ask ourselves: What are the factors 
that are remunerated? Our decision on what data to buy and where to 
spend on models is made in function of what indicators are the most 
‘remunerated,’” commented the head of quantitative management at a 
major European asset management firm. 
SUMMARY
 ■ The investment management process is becoming increasingly struc-
tured; the objective is a well-defined, repeatable investment process.
 ■ This requires measurable objectives and measurable results, financial 
engineering, risk control, feedback processes and, increasingly, knowl-
edge management.
 ■ In general, the five steps in the investment management process are set-
ting investment objectives, establishing an investment policy, selecting 
an investment strategy, selecting the specific assets, and measuring and 
evaluating investment performance. 

19
From Art to Engineering in Finance 
■ Changes in the investment management business are being driven by 
the explosion in the universe of investable assets brought about by glo-
balization, investors, and especially institutional investors and their 
consultants, pressure from regulators and the media, and the sheer size 
of the markets.
 ■ Given the size, diversity, and efficiency of modern markets, a more dis-
ciplined process can be achieved only in a quantitative framework.
 ■ Key to a quantitative framework is the measurement and management 
of uncertainty (i.e., risk) and financial engineering.
 ■ Modeling is the tool to achieve these objectives; advances in informa-
tion technology are the enabler.
 ■ Unstructured textual information is progressively being transformed 
into self-describing, semistructured information, allowing a better 
structuring of the research process.
 ■ After nearly two decades of experience with quantitative methods, 
market participants now more clearly perceive the benefits and the lim-
its of modeling; given today’s technology and markets, the need to bet-
ter integrate qualitative and quantitative information is clearly felt. 



## Financial Markets Overview

I 
CHAPTER 2 
Overview of Financial Markets, 
Financial Assets, and Market 
Participants 
n a market economy, the allocation of economic resources is driven by 
the outcome of many private decisions. Prices are the signals that 
direct economic resources to their best use. The types of markets in an 
economy can be divided into (1) the market for products (manufactured 
goods and services), or the product market; and (2) the market for the 
factors of production (labor and capital), or the factor market. Our pri-
mary application of the mathematical techniques presented in this book 
is to one part of the factor market, the market for financial assets, or, 
more simply, the financial market. In this chapter we review the basic 
characteristics and functions of financial assets and financial markets, 
the major players in the financial market, and the major financial assets 
(common stock, bonds, and derivatives). 
FINANCIAL ASSETS 
An asset is any possession that has value in an exchange. Assets can be 
classified as tangible or intangible. The value of a tangible asset depends 
on particular physical properties—examples include buildings, land, or 
machinery. Tangible assets may be classified further into reproducible 
assets such as machinery, or nonreproducible assets such as land, a 
mine, or a work of art. Intangible assets, by contrast, represent legal 
21 

22 
The Mathematics of Financial Modeling and Investment Management 
claims to some future benefit. Their value bears no relation to the form, 
physical or otherwise, in which the claims are recorded. 
Financial assets (also referred to as financial instruments, or securi-
ties) are intangible assets. For these instruments, the typical future bene-
fit comes in the form of a claim to future cash. The entity that agrees to 
make future cash payments is called the issuer of the financial asset; the 
owner of the financial asset is referred to as the investor. 
The claims of the holder of a financial asset may be either a fixed 
dollar amount or a varying, or residual, amount. In the former case, the 
financial asset is referred to as a debt instrument. Bonds and bank loans 
are examples of debt instruments. An equity claim (also called a residual 
claim) obligates the issuer of the financial asset to pay the holder an 
amount based on earnings, if any, after holders of debt instruments have 
been paid. Common stock is an example of an equity claim. A partner-
ship share in a business is another example. Some financial assets fall 
into both categories. Preferred stock, for example, represents an equity 
claim that entitles the investor to receive a fixed dollar amount. This 
payment is contingent, however, due only after payments to debt instru-
ment holders are made. Another instrument is convertible bonds, which 
allow the investor to convert debt into equity under certain circum-
stances. Both debt and preferred stock that pays a fixed dollar amount 
are called fixed income instruments. 
Financial assets serve two principal economic functions. First, finan-
cial assets transfer funds from those parties who have surplus funds to 
invest to those who need funds to invest in tangible assets. As their sec-
ond function, they transfer funds in such a way as to redistribute the 
unavoidable risk associated with the cash flow generated by tangible 
assets among those seeking and those providing the funds. However, the 
claims held by the final wealth holders generally differ from the liabili-
ties issued by the final demanders of funds because of the activity of 
entities operating in financial markets, called financial intermediaries, 
who seek to transform the final liabilities into different financial assets 
preferred by the public. We discuss financial intermediaries later in this 
chapter. 
Financial assets possess the following properties that determine or 
influence their attractiveness to different classes of investors: (1) money-
ness; (2) divisibility and denomination; (3) reversibility; (4) term to 
maturity; (5) liquidity; (6) convertibility; (7) currency; (8) cash flow and 
return predictability; and (9) tax status.1 
1 Some of these properties are taken from James Tobin, “Properties of Assets,” un-
dated manuscript, Yale University. 

23 
Overview of Financial Markets, Financial Assets, and Market Participants 
Some financial assets act as a medium of exchange or in settlement 
of transactions. These assets are called money. Other financial assets, 
although not money, closely approximate money in that they can be 
transformed into money at little cost, delay, or risk. Moneyness clearly 
offers a desirable property for investors. Divisibility and denomination 
divisibility relates to the minimum size at which a financial asset can be 
liquidated and exchanged for money. The smaller the size, the more the 
financial asset is divisible. 
Reversibility, also called round-trip cost, refers to the cost of invest-
ing in a financial asset and then getting out of it and back into cash 
again. For financial assets traded in organized markets or with “market 
makers,” the most relevant component of round-trip cost is the so-
called bid-ask spread, to which might be added commissions and the 
time and cost, if any, of delivering the asset. The bid-ask spread consists 
of the difference between the price at which a market maker is willing to 
sell a financial asset (i.e., the price it is asking) and the price at which a 
market maker is willing to buy the financial asset (i.e., the price it is bid-
ding). The spread charged by a market maker varies sharply from one 
financial asset to another, reflecting primarily the amount of risk the 
market maker assumes by “making” a market. This market-making risk 
can be related to two main forces. 
One is the variability of the price as measured, say, by some measure 
of dispersion of the relative price over time. The greater the variability, 
the greater the probability of the market maker incurring a loss in excess 
of a stated bound between the time of buying and reselling the financial 
asset. The variability of prices differs widely across financial assets. The 
second determining factor of the bid-ask spread charged by a market 
maker is what is commonly referred to as the thickness of the market, 
which is essentially the prevailing rate at which buying and selling orders 
reach the market maker (i.e., the frequency of transactions). A “thin 
market” sees few trades on a regular or continuing basis. Clearly, the 
greater the frequency of orders coming into the market for the financial 
asset (referred to as the “order flow”), the shorter the time that the finan-
cial asset must be held in the market maker’s inventory, and hence the 
smaller the probability of an unfavorable price movement while held. 
Thickness also varies from market to market. A low round-trip cost is 
clearly a desirable property of a financial asset, and as a result thickness 
itself is a valuable property. This attribute explains the potential advan-
tage of large over smaller markets (economies of scale), and a market’s 
endeavor to standardize the instruments offered to the public. 
The term to maturity, or simply maturity, is the length of the inter-
val until the date when the instrument is scheduled to make its final pay-
ment, or the owner is entitled to demand liquidation. Maturity is an 

24 
The Mathematics of Financial Modeling and Investment Management 
important characteristic of financial assets such as debt instruments. 
Equities set no maturity and are thus a form of perpetual instrument. 
Liquidity serves an important and widely used function, although no 
uniformly accepted definition of liquidity is presently available. A useful 
way to think of liquidity and illiquidity, proposed by James Tobin, is in 
terms of how much sellers stand to lose if they wish to sell immediately 
against engaging in a costly and time consuming search.2 Liquidity may 
depend not only on the financial asset but also on the quantity one 
wishes to sell (or buy). Even though a small quantity may be quite liq-
uid, a large lot may run into illiquidity problems. Note that liquidity 
again closely relates to whether a market is thick or thin. Thinness 
always increases the round-trip cost, even of a liquid financial asset. But 
beyond some point it becomes an obstacle to the formation of a market, 
and directly affects the illiquidity of the financial asset. 
An important property of some financial assets is their convertibility 
into other financial assets. In some cases, the conversion takes place 
within one class of financial assets, as when a bond is converted into 
another bond. In other situations, the conversion spans classes. For 
example, with a corporate convertible bond the bondholder can change 
it into equity shares. Most financial assets are denominated in one cur-
rency, such as U.S. dollars or yen or euros, and investors must choose 
them with that feature in mind. Some issuers have issued dual-currency 
securities with certain cash flows paid in one currency and other cash 
flows in another currency. 
The return that an investor will realize by holding a financial asset 
depends on the cash flow expected to be received, which includes divi-
dend payments on stock and interest payments on debt instruments, as 
well as the repayment of principal for a debt instrument and the 
expected sale price of a stock. Therefore, the predictability of the 
expected return depends on the predictability of the cash flow. Return 
predictability, a basic property of financial assets, provides the major 
determinant of their value. Assuming investors are risk averse, as we 
will see in later chapters, the riskiness of an asset can be equated with 
the uncertainty or unpredictability of its return. 
An important feature of any financial asset is its tax status. Govern-
mental codes for taxing the income from the ownership or sale of finan-
cial assets vary widely if not wildly. Tax rates differ from year to year, 
country to country, and even among municipalities or provinces within 
a country. Moreover, tax rates may differ from financial asset to finan-
cial asset, depending on the type of issuer, the length of time the asset is 
held, the nature of the owner, and so on. 
2 Tobin, “Properties of Assets.” 

25 
Overview of Financial Markets, Financial Assets, and Market Participants 
FINANCIAL MARKETS 
Financial assets are traded in a financial market. Below we discuss how 
financial markets can be classified and the functions of financial mar-
kets. 
Classification of Financial Markets 
There are five ways that one can classify financial markets: (1) nature of 
the claim, (2) maturity of the claims, (3) new versus seasoned claims, (4) 
cash versus derivative instruments, and (5) organizational structure of 
the market. 
The claims traded in a financial market may be either for a fixed 
dollar amount or a residual amount and financial markets can be classi-
fied according to the nature of the claim. As explained earlier, the 
former financial assets are referred to as debt instruments, and the 
financial market in which such instruments are traded is referred to as 
the debt market. The latter financial assets are called equity instruments 
and the financial market where such instruments are traded is referred 
to as the equity market or stock market. Preferred stock represents an 
equity claim that entitles the investor to receive a fixed dollar amount. 
Consequently, preferred stock has in common characteristics of instru-
ments classified as part of the debt market and the equity market. Gen-
erally, debt instruments and preferred stock are classified as part of the 
fixed income market. 
A second way to classify financial markets is by the maturity of the 
claims. For example, a financial market for short-term financial assets is 
called the money market, and the one for longer maturity financial 
assets is called the capital market. The traditional cutoff between short 
term and long term is one year. That is, a financial asset with a maturity 
of one year or less is considered short term and therefore part of the 
money market. A financial asset with a maturity of more than one year 
is part of the capital market. Thus, the debt market can be divided into 
debt instruments that are part of the money market, and those that are 
part of the capital market, depending on the number of years to matu-
rity. Because equity instruments are generally perpetual, a third way to 
classify financial markets is by whether the financial claims are newly 
issued. When an issuer sells a new financial asset to the public, it is said 
to “issue” the financial asset. The market for newly issued financial 
assets is called the primary market. After a certain period of time, the 
financial asset is bought and sold (i.e., exchanged or traded) among 
investors. The market where this activity takes place is referred to as the 
secondary market. 

26 
The Mathematics of Financial Modeling and Investment Management 
Some financial assets are contracts that either obligate the investor 
to buy or sell another financial asset or grant the investor the choice to 
buy or sell another financial asset. Such contracts derive their value 
from the price of the financial asset that may be bought or sold. These 
contracts are called derivative instruments and the markets in which 
they trade are referred to as derivative markets. The array of derivative 
instruments includes options contracts, futures contracts, forward con-
tracts, swap agreements, and cap and floor agreements. 
Although the existence of a financial market is not a necessary con-
dition for the creation and exchange of a financial asset, in most econo-
mies financial assets are created and subsequently traded in some type of 
organized financial market structure. A financial market can be classi-
fied by its organizational structure. These organizational structures can 
be classified as auction markets and over-the-counter markets. We 
describe each type later in this chapter. 
Economic Functions of Financial Markets 
The two primary economic functions of financial assets were already dis-
cussed. Financial markets provide three additional economic functions. 
First, the interactions of buyers and sellers in a financial market 
determine the price of the traded asset; or, equivalently, the required 
return on a financial asset is determined. The inducement for firms to 
acquire funds depends on the required return that investors demand, and 
this feature of financial markets signals how the funds in the economy 
should be allocated among financial assets. It is called the price discovery 
process. Whether these signals are correct is an issue that we discuss 
when we examine the question of the efficiency of financial markets. 
Second, financial markets provide a mechanism for an investor to 
sell a financial asset. This feature offers liquidity in financial markets, an 
attractive characteristic when circumstances either force or motivate an 
investor to sell. In the absence of liquidity, the owner must hold a debt 
instrument until it matures and an equity instrument until the company 
either voluntarily or involuntarily liquidates. Although all financial 
markets provide some form of liquidity, the degree of liquidity is one of 
the factors that differentiates various markets. 
The third economic function of a financial market reduces the 
search and information costs of transacting. Search costs represent 
explicit costs, such as the money spent to advertise the desire to sell or 
purchase a financial asset, and implicit costs, such as the value of time 
spent in locating a counterparty. The presence of some form of orga-
nized financial market reduces search costs. Information costs are 
incurred in assessing the investment merits of a financial asset, that is, 

27 
Overview of Financial Markets, Financial Assets, and Market Participants 
the amount and the likelihood of the cash flow expected to be gener-
ated. In an efficient market, prices reflect the aggregate information col-
lected by all market participants. 
Secondary Markets 
The secondary market is where already-issued financial assets are 
traded. The key distinction between a primary market and a secondary 
market is that in the secondary market the issuer of the asset does not 
receive funds from the buyer. Rather, the existing issue changes hands in 
the secondary market, and funds flow from the buyer of the asset to the 
seller. Below we explain the various features of secondary markets. 
These features are common to any type of financial instrument traded. 
It is in the secondary market where an issuer of securities, whether 
the issuer is a corporation or a governmental unit, may be provided 
with regular information about the value of the security. The periodic 
trading of the asset reveals to the issuer the consensus price that the 
asset commands in an open market. Thus, firms can discover what value 
investors attach to their stocks, and firms and noncorporate issuers can 
observe the prices of their bonds and the implied interest rates investors 
expect and demand from them. Such information helps issuers assess 
how well they are using the funds acquired from earlier primary market 
activities, and it also indicates how receptive investors would be to new 
offerings. 
The other service a secondary market offers issuers is that it pro-
vides the opportunity for the original buyers of the asset to reverse their 
investment by selling it for cash. Unless investors are confident that they 
can shift from one financial asset to another as they may deem neces-
sary, they would naturally be reluctant to buy any financial asset. Such 
reluctance would harm potential issuers in one of two ways: either issu-
ers would be unable to sell new securities at all or they would have to 
pay a high rate of return, as investors would demand greater compensa-
tion for the expected illiquidity of the securities. 
Investors in financial assets receive several benefits from a secondary 
market. Such a market obviously offers them liquidity for their assets as 
well as information about the assets’ fair or consensus values. Further, 
secondary markets bring together many interested parties and so can 
reduce the costs of searching for likely buyers and sellers of assets. 
Moreover, by accommodating many trades, secondary markets keep the 
cost of transactions low. By keeping the costs of both searching and 
transacting low, secondary markets encourage investors to purchase 
financial assets. 

28 
The Mathematics of Financial Modeling and Investment Management 
Perfect Market 
In order to explain the characteristics of secondary markets, we will first 
describe a “perfect market” for a financial asset. Then we can show how 
common occurrences in real markets keep them from being theoretically 
perfect. 
In general, a perfect market results when the number of buyers and 
sellers is sufficiently large, and all participants are small enough relative 
to the market so that no individual market agent can influence the com-
modity’s price. Consequently, all buyers and sellers are price takers, and 
the market price is determined where there is equality of supply and 
demand. This condition is more likely to be satisfied if the commodity 
traded is fairly homogeneous (for example, corn or wheat). 
There is more to a perfect market than market agents being price 
takers. It is also required that there are no transaction costs or impedi-
ments that interfere with the supply and demand of the commodity. 
Economists refer to these various costs and impediments as “frictions.” 
The costs associated with frictions generally result in buyers paying 
more than in the absence of frictions, and/or sellers receiving less. 
In the case of financial markets, frictions would include: 
■ Commissions charged by brokers.
 ■ Bid-ask spreads charged by dealers.
 ■ Order handling and clearance charges.
 ■ Taxes (notably on capital gains) and government-imposed transfer fees.
 ■ Costs of acquiring information about the financial asset.
 ■ Trading restrictions, such as exchange-imposed restrictions on the size 
of a position in the financial asset that a buyer or seller may take.
 ■ Restrictions on market makers.
 ■ Halts to trading that may be imposed by regulators where the financial 
asset is traded. 
Role of Brokers and Dealers in Real Markets 
Common occurrences in real markets keep them from being theoreti-
cally perfect. Because of these occurrences, brokers and dealers are nec-
essary to the smooth functioning of a secondary market. 
One way in which a real market might not meet all the exacting 
standards of a theoretically perfect market is that many investors may 
not be present at all times in the marketplace. Further, a typical investor 
may not be skilled in the art of the deal or completely informed about 
every facet of trading in the asset. Clearly, most investors in even 
smoothly functioning markets need professional assistance. Investors 
need someone to receive and keep track of their orders for buying or 

29 
Overview of Financial Markets, Financial Assets, and Market Participants 
selling, to find other parties wishing to sell or buy, to negotiate for good 
prices, to serve as a focal point for trading, and to execute the orders. 
The broker performs all of these functions. Obviously, these functions 
are more important for the complicated trades, such as the small or 
large trades, than for simple transactions or those of typical size. 
A broker is an entity that acts on behalf of an investor who wishes to 
execute orders. In economic and legal terms, a broker is said to be an 
“agent” of the investor. It is important to realize that the brokerage activ-
ity does not require the broker to buy and hold in inventory or sell from 
inventory the financial asset that is the subject of the trade. (Such activity 
is termed “taking a position” in the asset, and it is the role of the dealer.) 
Rather, the broker receives, transmits, and executes investors’ orders with 
other investors. The broker receives an explicit commission for these ser-
vices, and the commission is a “transaction cost” of the capital markets. 
A real market might also differ from the perfect market because of 
the possibly frequent event of a temporary imbalance in the number of 
buy and sell orders that investors may place for any security at any one 
time. Such unmatched or unbalanced flow causes two problems. First, 
the security’s price may change abruptly even if there has been no shift 
in either supply or demand for the security. Second, buyers may have to 
pay higher than market-clearing prices (or sellers accept lower ones) if 
they want to make their trade immediately. 
For example, suppose the consensus price for ABC security is $50, 
which was determined in several recent trades. Also suppose that a flow 
of buy orders from investors who suddenly have cash arrives in the mar-
ket, but there is no accompanying supply of sell orders. This temporary 
imbalance could be sufficient to push the price of ABC security to, say, 
$55. Thus, the price has changed sharply even though there has been no 
change in any fundamental financial aspect of the issuer. Buyers who 
want to buy immediately must pay $55 rather than $50, and this differ-
ence can be viewed as the price of “immediacy.” By immediacy, we 
mean that buyers and sellers do not want to wait for the arrival of suffi-
cient orders on the other side of the trade, which would bring the price 
closer to the level of recent transactions. 
The fact of imbalances explains the need for the dealer or market 
maker, who stands ready and willing to buy a financial asset for its own 
account (add to an inventory of the security) or sell from its own 
account (reduce the inventory of the security). At a given time, dealers 
are willing to buy a security at a price (the bid price) that is less than 
what they are willing to sell the same security for (the ask price). 
In the 1960s, economists George Stigler3 and Harold Demsetz4 ana-
lyzed the role of dealers in securities markets. They viewed dealers as the 
suppliers of immediacy—the ability to trade promptly—to the market. 

30 
The Mathematics of Financial Modeling and Investment Management 
The bid-ask spread can be viewed in turn as the price charged by dealers 
for supplying immediacy, together with short-run price stability (continu-
ity or smoothness) in the presence of short-term order imbalances. There 
are two other roles that dealers play: they provide better price informa-
tion to market participants, and in certain market structures they provide 
the services of an auctioneer in bringing order and fairness to a market.5 
The price-stabilization role relates to our earlier example of what 
may happen to the price of a particular transaction in the absence of 
any intervention when there is a temporary imbalance of order. By tak-
ing the opposite side of a trade when there are no other orders, the 
dealer prevents the price from materially diverging from the price at 
which a recent trade was consummated. 
Investors are concerned with immediacy, and they also want to 
trade at prices that are reasonable, given prevailing conditions in the 
market. While dealers cannot know with certainty the true price of a 
security, they do have a privileged position in some market structures 
with respect to the flow of market orders. They also have a privileged 
position regarding “limit” orders, the special orders that can be exe-
cuted only if the market price of the security changes in a specified way. 
Finally, the dealer acts as an auctioneer in some market structures, 
thereby providing order and fairness in the operations of the market. 
For example, the market maker on organized stock exchanges in the 
United States performs this function by organizing trading to make sure 
that the exchange rules for the priority of trading are followed. The role 
of a market maker in a call market structure is that of an auctioneer. 
The market maker does not take a position in the traded security, as a 
dealer does in a continuous market. 
One of the most important factors that determine the price dealers 
should charge for the services they provide (i.e., the bid-ask spread) is 
the order processing costs incurred by dealers, such as the costs of 
equipment necessary to do business and the administrative and opera-
tions staff. The lower these costs, the narrower the bid-ask spread. With 
the reduced cost of computing and better-trained personnel, these costs 
have declined over time. 
Dealers also have to be compensated for bearing risk. A dealer’s 
position may involve carrying inventory of a security (along position) or 
3 George Stigler, “Public Regulation of Securities Markets,” Journal of Business 
(April 1964), pp. 117–34. 
4 Harold Demsetz, “The Cost of Transacting,” Quarterly Journal of Economics 
(October 1968), pp. 35–6. 
5 Robert A. Schwartz, Equity Markets: Structure, Trading, and Performance (New 
York: Harper & Row Publishers, 1988), pp. 389–397. 

31 
Overview of Financial Markets, Financial Assets, and Market Participants 
selling a security that is not in inventory (a short position). There are 
three types of risks associated with maintaining a long or short position 
in a given security. First, there is the uncertainty about the future price 
of the security. A dealer who has a long position in the security is con-
cerned that the price will decline in the future; a dealer who is in a short 
position is concerned that the price will rise. 
The second type of risk has to do with the expected time it will take 
the dealer to unwind a position and its uncertainty. And this, in turn, 
depends primarily on the rate at which buy and sell orders for the secu-
rity reaches the market (i.e., the thickness of the market). Finally, while 
a dealer may have access to better information about order flows than 
the general public, there are some trades where the dealer takes the risk 
of trading with someone who has better information6 This results in the 
better-informed trader obtaining a better price at the expense of the 
dealer. Consequently, in establishing the bid-ask spread for a trade, a 
dealer will assess whether the trader might have better information. 
Some trades that we will discuss below can be viewed as “information-
less trades.” This means that the dealer knows or believes a trade is 
being requested to accomplish an investment objective that is not moti-
vated by the potential future price movement of the security. 
Market Price Efficiency 
The term “efficient” capital market has been used in several contexts to 
describe the operating characteristics of a capital market. There is a dis-
tinction, however, between an operationally (or internally) efficient mar-
ket and a pricing (or externally) efficient capital market.7 In this section 
we describe pricing efficiency. 
Pricing efficiency refers to a market where prices at all times fully 
reflect all available information that is relevant to the valuation of secu-
rities. That is, relevant information about the security is quickly 
impounded into the price of securities. In his seminal review article on 
pricing efficiency, Eugene Fama points out that in order to test whether 
a market is price efficient, two definitions are necessary.8 First, it is nec-
essary to define what it means that prices “fully reflect” information. 
Second, the “relevant” set of information that is assumed to be “fully 
reflected” in prices must be defined. 
6 Walter Bagehot, “The Only Game in Town,” Financial Analysts Journal (March-
April 1971), pp. 12–14, 22. 
7 Richard R. West, “Two Kinds of Market Efficiency,” Financial Analysts Journal 
(November–December 1975), pp. 30–34. 
8 Eugene F. Fama, “Efficient Capital Markets: A Review of Theory and Empirical 
Work,” Journal of Finance (May 1970), pp. 383–417. 

32 
The Mathematics of Financial Modeling and Investment Management 
Fama, as well as others, defines “fully reflects” in terms of the 
expected return from holding a security. The expected return over some 
holding period is equal to expected cash distributions plus the expected 
price change, all divided by the initial price. The price formation process 
defined by Fama and others is that the expected return one period from 
now is a stochastic (i.e., random) variable that already takes into 
account the “relevant” information set. 
In defining the “relevant” information set that prices should reflect, 
Fama classified the pricing efficiency of a market into three forms: weak, 
semistrong, and strong. The distinction between these forms lies in the 
relevant information that is hypothesized to be impounded in the price 
of the security. Weak efficiency means that the price of the security 
reflects the past price and trading history of the security. Semistrong effi-
ciency means that the price of the security fully reflects all public infor-
mation (which, of course, includes but is not limited to historical price 
and trading patterns). Strong-form efficiency exists in a market where 
the price of a security reflects all information, whether or not it is pub-
licly available. 
A price-efficient market has implications for the investment strategy 
that investors may wish to pursue. Throughout this book, we shall refer 
to various active strategies employed by investors. In an active strategy, 
investors seek to capitalize on what they perceive to be the mispricing of 
a security or securities. In a market that is price efficient, active strate-
gies will not consistently generate a return after taking into consider-
ation transaction costs and the risks associated with a strategy that is 
greater than simply buying and holding securities. This has lead inves-
tors in certain markets that empirical evidence suggests are price effi-
cient to pursue a strategy of indexing, which simply seeks to match the 
performance of some financial index. 
Operational Efficiency 
In an operationally efficient market, investors can obtain transaction 
services as cheaply as possible, given the costs associated with furnish-
ing those services. Commissions are only part of the cost of transacting 
as we noted above. The other part is the dealer spread. Bid-ask spreads 
for bonds vary by type of bond. Other components of transaction costs 
are discussed below. 
In an investment era where one-half of one percentage point can 
make a difference when an asset manager is compared against a perfor-
mance benchmark, an important aspect of the investment process is the 
cost of implementing an investment strategy. Transaction costs are more 

33 
Overview of Financial Markets, Financial Assets, and Market Participants 
than merely brokerage commissions—they consist of commissions, fees, 
execution costs, and opportunity costs.9 
Commissions are the fees paid to brokers to trade securities. Execu-
tion costs represent the difference between the execution price of a secu-
rity and the price that would have existed in the absence of the trade. 
Execution costs can be further decomposed into market (or price) 
impact and market-timing costs. Market impact cost is the result of the 
bid-ask spread and a price concession extracted by dealers to mitigate 
their risk that an investor’s demand for liquidity is information-moti-
vated. Market-timing cost arises when an adverse price movement of the 
security during the time of the transaction can be attributed in part to 
other activity in the security and is not the result of a particular transac-
tion. Execution costs, then, are related to both the demand for liquidity 
and the trading activity on the trade date. 
There is a distinction between information-motivated trades and 
informationless trades. Information-motivated trading occurs when inves-
tors believe they possess pertinent information not currently reflected in 
the security’s price. This style of trading tends to increase market impact 
because it emphasizes the speed of execution, or because the market 
maker believes a desired trade is driven by information and increases the 
bid-ask spread to provide some protection. It can involve the sale of one 
security in favor of another. Informationless trades are the result of either 
a reallocation of wealth or implementation of an investment strategy that 
utilizes only existing information. An example of the former is a pension 
fund’s decision to invest cash in the stock market. Other examples of 
informationless trades include portfolio rebalances, investment of new 
money, or liquidations. In these circumstances, the demand for liquidity 
alone should not lead the market maker to demand the significant price 
concessions associated with new information. 
The problem with measuring execution costs is that the true mea-
sure—which is the difference between the price of the security in the 
absence of the investor’s trade and the execution price—is not observ-
able. Furthermore, the execution prices are dependent on supply and 
demand conditions at the margin. Thus, the execution price may be 
influenced by competitive traders who demand immediate execution, or 
other investors with similar motives for trading. This means that the 
execution price realized by an investor is the consequence of the struc-
ture of the market mechanism, the demand for liquidity by the marginal 
9 For a further discussion of these costs, see Bruce M. Collins and Frank J. Fabozzi, 
“A Methodology for Measuring Transaction Costs,” Financial Analysts Journal 
(March-April 1991), pp. 27–36. 

34 
The Mathematics of Financial Modeling and Investment Management 
investor, and the competitive forces of investors with similar motiva-
tions for trading. 
The cost of not transacting represents an opportunity cost. Oppor-
tunity costs may arise when a desired trade fails to be executed. This 
component of costs represents the difference in performance between an 
investor’s desired investment and the same investor’s actual investment 
after adjusting for execution costs, commissions, and fees. Opportunity 
costs have been characterized as the hidden cost of trading, and it has 
been suggested that the shortfall in performance of many actively man-
aged portfolios is the consequence of failing to execute all desired 
trades.14 Measurement of opportunity costs is subject to the same prob-
lems as measurement of execution costs. The true measure of opportu-
nity cost depends on knowing what the performance of a security would 
have been if all desired trades had been executed at the desired time 
across an investment horizon. As these are the desired trades that the 
investor could not execute, the benchmark is inherently unobservable 
OVERVIEW OF MARKET PARTICIPANTS 
With an understanding of what financial assets are and the role of finan-
cial assets and financial markets, we can now identify who the players are 
in the financial markets. By this we mean the entities that issue financial 
assets and the entities that invest in financial assets. We will focus on one 
particular group of market players, called financial intermediaries, because 
of the key economic functions that they perform in financial markets. In 
addition to reviewing their economic function, we will set forth the basic 
asset/liability problem faced by managers of financial intermediaries. 
There are entities that issue financial assets, both debt instruments 
and equity instruments. There are investors who purchase these finan-
cial assets. This does not mean that these two groups are mutually 
exclusive—it is common for an entity to both issue a financial asset and 
at the same time invest in a different financial asset. 
A simple classification of these entities is as follows: (1) central gov-
ernments; (2) agencies of central governments; (3) municipal govern-
ments; (4) supranationals; (5) nonfinancial businesses; (6) financial 
enterprises; and (7) households. Central governments borrow funds for 
a wide variety of reasons. Many central governments establish agencies 
to raise funds to perform specific functions. Most countries have munic-
ipalities or provinces that raise funds in the capital market. A suprana-
tional institution is an organization that is formed by two or more 
central governments through international treaties. Businesses are classi-

35 
Overview of Financial Markets, Financial Assets, and Market Participants 
fied into nonfinancial and financial businesses. These entities borrow 
funds in the debt market and raise funds in the equity market. Nonfinan-
cial businesses are divided into three categories: corporations, farms, 
and nonfarm/noncorporate businesses. The first category includes cor-
porations that manufacture products (e.g., cars, steel, computers) and/or 
provide nonfinancial services (e.g., transportation, utilities, computer 
programming). In the last category are businesses that produce the same 
products or provide the same services but are not incorporated. 
Financial businesses, more popularly referred to as financial institu-
tions, provide services related to one or more of the following: 
1. Transforming financial assets acquired through the market and consti-
tuting them into a different and more preferable type of asset—which 
becomes their liability. This is the function performed by financial 
intermediaries, the most important type of financial institution. 
2. Exchanging financial assets on behalf of customers. 
3. Exchanging financial assets for their own account. 
4. Assisting in the creation of financial assets for their customers and then 
selling those financial assets to other market participants. 
5. Providing investment advice to other market participants. 
6. Managing the portfolios of other market participants. 
Financial intermediaries include: depository institutions that 
acquire the bulk of their funds by offering their liabilities to the public 
mostly in the form of deposits; insurance companies (life and property 
and casualty companies); pension funds; and finance companies. Later 
in this chapter we will discuss these entities. The second and third ser-
vices in the list above are the broker and dealer functions. The fourth 
service is referred to as securities underwriting. Typically, a financial 
institution that provides an underwriting service also provides a broker-
age and/or dealer service. 
Some nonfinancial businesses have subsidiaries that provide finan-
cial services. For example, many large manufacturing firms have subsid-
iaries that provide financing for the parent company’s customer. These 
financial institutions are called captive finance companies. 
Role of Financial Intermediaries 
Financial intermediaries obtain funds by issuing financial claims against 
themselves to market participants and then investing those funds. The 
investments made by financial intermediaries—their assets—can be in 
loans and/or securities. These investments are referred to as direct 
investments. As just noted, financial intermediaries play the basic role of 

36 
The Mathematics of Financial Modeling and Investment Management 
transforming financial assets that are less desirable for a large part of 
the public into other financial assets—their own liabilities—which are 
preferred more by the public. This transformation involves at least one 
of four economic functions: (1) providing maturity intermediation; (2) 
risk reduction via diversification; (3) reducing the costs of contracting 
and information processing; and (4) providing a payments mechanism. 
Maturity intermediation involves a financial intermediary issuing lia-
bilities against itself that have a maturity different from the assets it 
acquires with the fund raised. An example is a commercial bank that 
issues short-term liabilities (i.e., deposits) and invests in assets with a 
longer maturity than those liabilities. Maturity intermediation has two 
implications for financial markets. First, investors have more choices con-
cerning maturity for their investments; borrowers have more choices for 
the length of their debt obligations. Second, because investors are reluctant 
to commit funds for a long period of time, they will require that long-term 
borrowers pay a higher interest rate than on short-term borrowing. In con-
trast, a financial intermediary will be willing to make longer-term loans, 
and at a lower cost to the borrower than an individual investor would, by 
counting on successive deposits providing the funds until maturity 
(although at some risk as discussed below). Thus, the second implication is 
that the cost of longer-term borrowing is likely to be reduced. 
To illustrate the economic function of risk reduction via diversifica-
tion, consider an investor who invests in a mutual fund. Suppose that 
the mutual fund invests the funds received in the stock of a large num-
ber of companies. By doing so, the mutual fund has diversified and 
reduced its risk. Investors who have a small sum to invest would find it 
difficult to achieve the same degree of diversification because they 
would not have sufficient funds to buy shares of a large number of com-
panies. Yet by investing in the investment company for the same sum of 
money, investors can accomplish this diversification, thereby reducing 
risk. This economic function of financial intermediaries—transforming 
more risky assets into less risky ones—is called diversification. While 
individual investors can do it on their own, they may not be able to do it 
as cost effectively as a financial intermediary, depending on the amount 
of funds they have to invest. Attaining cost-effective diversification in 
order to reduce risk by purchasing the financial assets of a financial 
intermediary is an important economic benefit for financial markets. 
Investors purchasing financial assets should develop skills necessary 
to understand how to evaluate an investment. Once those skills are 
developed, investors should apply them to the analysis of specific finan-
cial assets that are candidates for purchase (or subsequent sale). Inves-
tors who want to make a loan to a consumer or business will need to 
write the loan contract (or hire an attorney to do so). While there are 

37 
Overview of Financial Markets, Financial Assets, and Market Participants 
some people who enjoy devoting leisure time to this task, most of us 
find that leisure time is in short supply, so to sacrifice it, we have to be 
compensated. The form of compensation could be a higher return 
obtained from an investment. In addition to the opportunity cost of the 
time to process the information about the financial asset and its issuer, 
there is the cost of acquiring that information. All these costs are called 
information processing costs. The costs of writing loan contracts are 
referred to as contracting costs. Another dimension to contracting costs 
is the cost of enforcing the terms of the loan agreement. There are econ-
omies of scale in contracting and processing information about financial 
assets, because of the amount of funds managed by financial intermedi-
aries. The lower costs accrue to the benefit of the investor who pur-
chases a financial claim of the financial intermediary and to the issuers 
of financial assets, who benefit from a lower borrowing cost. 
While the previous three economic functions may not have been 
immediately obvious, this last function should be. Most transactions 
made today are not done with cash. Instead, payments are made using 
checks, credit cards, debit cards, and electronic transfers of funds. These 
methods for making payments are provided by certain financial interme-
diaries. The ability to make payments without the use of cash is critical 
for the functioning of a financial market. In short, depository institu-
tions transform assets that cannot be used to make payments into other 
assets that offer that property. 
Institutional Investors 
Managers of the funds of financial entities manage those funds to meet 
specified investment objectives. For many institutional investors (insur-
ance companies, pension funds, investment companies, depository institu-
tions, and endowments and foundations), those objectives are dictated by 
the nature of their liabilities. It is within the context of the asset/liability 
problem faced by managers of institutional funds that investment vehicles 
and investment strategies make any sense. Therefore, in this section we 
provide an overview of the investment objectives of institutional investors 
and the constraints imposed on managers of the funds of these entities. 
Nature of Liabilities 
The nature of an institutional investor’s liabilities will dictate the gen-
eral investment strategy to pursue. Depository institutions, for example, 
seek to generate income by the spread between the return that they earn 
on their assets and the cost of their funds. Life insurance companies are 
in the spread business. Pension funds are not in the spread business, in 
that they themselves do not raise funds in the market. Certain types of 

38 
The Mathematics of Financial Modeling and Investment Management 
pension funds seek to cover the cost of pension obligations at a mini-
mum cost to the plan sponsor. Most investment companies face no 
explicit costs for the funds they acquire and must satisfy no specific lia-
bility obligations, the exception being target-term trusts. 
A liability is a cash outlay that must be made at a specific time to 
satisfy the contractual terms of an obligation. An institutional investor 
is concerned with both the amount and timing of liabilities, because its 
assets must produce the cash flow to meet any payments it has promised 
to make in a timely way. In fact, liabilities are classified according to the 
degree of certainty of their amount and timing, as shown in Exhibit 2.1. 
This exhibit assumes that the holder of the obligation will not cancel it 
prior to any actual or projected payout date. 
The descriptions of cash outlays as either known or uncertain are 
undoubtedly broad. When we refer to a cash outlay as being uncertain, 
we do not mean that it cannot be predicted. There are some liabilities 
where the “law of large numbers” makes it easier to predict the timing 
and/or amount of cash outlays. This work is typically done by actuaries, 
but even actuaries have difficulty predicting natural catastrophes such 
as floods and earthquakes. 
In our description of each type of risk category, it is important to note 
that, just like assets, there are risks associated with liabilities. Some of 
these risks are affected by the same factors that affect asset risks. 
A Type I liability is one for which both the amount and timing of 
the liabilities are known with certainty. An example would be when an 
institution knows that it must pay $8 million six months from now. 
Banks and thrifts know the amount that they are committed to pay 
(principal plus interest) on the maturity date of a fixed-rate certificate of 
deposit (CD), assuming that the depositor does not withdraw funds 
prior to the maturity date. Type I liabilities, however, are not limited to 
depository institutions. A product sold by life insurance companies is a 
guaranteed investment contract, popularly referred to as a GIC (dis-
cussed below). The obligation of the life insurance company under this 
contract is that, for a sum of money (called a premium), it will guaran-
tee an interest rate up to some specified maturity date. 
EXHIBIT 2.1 
Classification of Liabilities of Institutional Investors 
Liability Type 
Amount of Outlay 
Timing of Cash Outlay 
Type I 
Known 
Known 
Type II 
Known 
Uncertain 
Type III 
Uncertain 
Known 
Type IV 
Uncertain 
Uncertain 

39 
Overview of Financial Markets, Financial Assets, and Market Participants 
A Type II liability is one for which the amount of the cash outlay is 
known, but the timing of the cash outlay is uncertain. The most obvious 
example of a Type II liability is a life insurance policy. There are many 
types of life insurance policies, but the most basic type provides that, for 
an annual premium, a life insurance company agrees to make a specified 
dollar payment to policy beneficiaries upon the death of the insured. 
Naturally, the timing of the insured’s death is uncertain. 
A Type III liability is one for which the timing of the cash outlay is 
known, but the amount is uncertain. A 2-year, floating-rate CD for 
which the interest rate resets quarterly, based on some market interest 
rate, is an example. 
A Type IV liability is one for which there is uncertainty as to both the 
amount and the timing of the cash outlay. There are numerous insurance 
products and pension obligations in this category. Probably the most 
obvious examples are automobile and home insurance policies issued by 
property and casualty insurance companies. When, and if, a payment will 
have to be made to the policyholder is uncertain. Whenever damage is 
done to an insured asset, the amount of the payment that must be made is 
uncertain. The liabilities of pension plans can also be Type IV liabilities. 
In defined benefit plans, retirement benefits depend on the participant’s 
income for a specified number of years before retirement and the total 
number of years the participant worked. This will affect the amount of 
the cash outlay. The timing of the cash outlay depends on when the 
employee elects to retire, and whether the employee remains with the 
sponsoring plan until retirement. Moreover, both the amount and the tim-
ing will depend on how the employee elects to have payments made— 
over only the employee’s life or those of the employee and spouse. 
Overview of Asset/liability Management 
The two goals of a financial institution are (1) to earn an adequate 
return on funds invested and (2) to maintain a comfortable surplus of 
assets beyond liabilities. The task of managing funds of a financial insti-
tution to accomplish these goals is referred to as asset/liability manage-
ment or surplus management. This task involves a trade-off between 
controlling the risk of a decline in the surplus and taking on acceptable 
risks in order to earn an adequate return on the funds invested. With 
respect to the risks, the manager must consider the risks of both the 
assets and the liabilities. 
Institutions may calculate three types of surpluses: economic, account-
ing, and regulatory. The method of valuing assets and liabilities greatly 
affects the apparent health of a financial institution. Unrealistic valuation, 

40 
The Mathematics of Financial Modeling and Investment Management 
although sometimes allowable under accounting procedures and regula-
tions, is not sound investment practice. 
The economic surplus of any entity is the difference between the mar-
ket value of all its assets and the market value of its liabilities. That is, 
Economic surplus = Market value of assets – Market value of liabilities 
The market value of the liabilities is simply the present value of the lia-
bilities, where the liabilities are discounted at an appropriate interest rate. 
Institutional investors must prepare periodic financial statements. 
These financial statements must be prepared in accordance with “gener-
ally accepted accounting principles” (GAAP). Thus, the assets and lia-
bilities reported are based on GAAP accounting and the resulting 
surplus is referred to as accounting surplus. 
Institutional investors that are regulated at the state or federal levels 
must also provide financial reports to regulators based on regulatory 
accounting principles (RAP). RAP accounting for a regulated institution 
need not use the same rules as set forth in GAAP accounting. Liabilities 
may or may not be reported at their present value, depending on the 
type of institution and the type of liability. The surplus, as measured 
using RAP accounting, is called regulatory surplus or statutory surplus, 
and, as in the case of accounting surplus, may be materially different 
from economic surplus. 
Benchmarks for Nonliability Driven Entities 
Thus far, our discussion has focused on institutional investors that face 
liabilities. However, not all financial institutions face liabilities. An 
investment company (discussed later) is an example. Also, while an 
entity such as a pension plan may face liabilities, it may engage external 
asset managers and set for those managers an objective that is unrelated 
to the pension fund’s liabilities. For such asset managers who do not 
face liabilities, the objective is to outperform some client-designated 
benchmark. In bond portfolio management, the benchmark may be one 
of the bond indexes described in Chapter 21. In general, the perfor-
mance of the money manager will be measured as follows: 
Return on the portfolio – Return on the benchmark 
Active money management involves creating a portfolio that will 
earn a return (after adjusting for risk) greater than the benchmark. In 
contrast, a strategy of indexing is one in which an asset manager creates 
a portfolio that only seeks to match the return on the benchmark. 

41 
Overview of Financial Markets, Financial Assets, and Market Participants 
From our discussion of asset/liability management and the manage-
ment of funds in the absence of liabilities, we can see that the invest-
ment strategy of one institutional investor may be inappropriate for 
another. As with investment strategies, a security or asset class that may 
be attractive for one institutional investor may be inappropriate for the 
portfolio of another. 
In the remainder of this section we look at the investment objective 
of the major institutional investors. For each entity, the nature of the 
liabilities and the strategies they use to accomplish their investment 
objectives are also reviewed, as well as regulations that influence invest-
ment decisions. 
Insurance Companies 
Insurance companies are financial intermediaries that, for a price, will 
make a payment if a certain event occurs. They function as risk bearers. 
There are two types of insurance companies: life insurance companies 
(“life companies”) and property and casualty insurance companies 
(“P&C companies”). The principal event that the former insures against 
is death. Upon the death of a policyholder, a life insurance company 
agrees to make either a lump sum payment or a series of payments to 
the beneficiary of the policy. Life insurance protection is not the only 
financial product sold by these companies; a major portion of the busi-
ness of life companies is in the area of providing retirement benefits. In 
contrast, P&C companies insure against a wide variety of occurrences. 
Two examples are automobile insurance and home insurance. 
The key distinction between life and P&C companies lies in the dif-
ficulty of projecting whether a policyholder will be paid off and, if so, 
how much the payment will be. While this is no simple task for either 
type of insurance company, from an actuarial perspective it is easier for 
a life company. The amount and timing of claims on P&C companies 
are more difficult to predict because of the randomness of natural catas-
trophes and the unpredictability of court awards in liability cases. This 
uncertainty about the timing and amount of cash outlays to satisfy 
claims affects the investment strategies used by the managers of P&C 
companies’ funds. 
Pension Funds 
A pension plan is a fund that is established for the payment of retire-
ment benefits. The entities that establish pension plans—called plan 
sponsors—are private business entities acting for their employees, state 
and local entities on behalf of their employees, unions on behalf of their 
members, and individuals for themselves. In the United States, corporate 

42 
The Mathematics of Financial Modeling and Investment Management 
pension plans are governed by the Employee Retirement Income Secu-
rity Act of 1974 (ERISA). Pension funds are exempt from taxation. 
There are two basic and widely used types of pension plans: defined 
contribution plans and defined benefit plans. In a defined contribution 
plan, the plan sponsor is responsible only for making specified contribu-
tions into the plan on behalf of qualifying participants. The payments 
that will be made to qualifying participants upon retirement will depend 
on the growth of the plan assets; that is, payment is determined by the 
investment performance of the assets in which the pension fund is 
invested. Therefore, in a defined contribution plan, the employee bears 
all the investment risk. In a defined benefit plan, the plan sponsor agrees 
to make specified dollar payments to qualifying employees at retirement 
(and some payments to beneficiaries in case of death before retirement). 
The retirement payments are determined by a formula that usually takes 
into account both the length of service and the earnings of the 
employee. The pension obligations are effectively the liability of the 
plan sponsor, who assumes the risk of having insufficient funds in the 
plan to satisfy the contractual payments that must be made to retired 
employees. Thus, unlike a defined contribution plan, in a defined benefit 
plan, all the investment risks are borne by the plan sponsor. 
Investment Companies 
Investment companies sell shares to the public and invest the proceeds 
in a diversified portfolio of securities. Each share they sell represents a 
proportionate interest in a portfolio of securities. The securities pur-
chased could be restricted to specific types of assets such as common 
stock, government bonds, corporate bonds, or money market instru-
ments. The investment strategies followed by investment companies 
range from high-risk active portfolio strategies to low-risk passive port-
folio strategies. 
There are two types of managed investment companies: open-end 
funds and closed-end funds. An open-end fund, more popularly referred 
to as a mutual fund, continually stands ready to sell new shares to the 
public and to redeem its outstanding shares on demand at a price equal 
to an appropriate share of the value of its portfolio, which is computed 
daily at the close of the market. A mutual fund’s share price is based on 
its net asset value (NAV) per share, which is found by subtracting from 
the market value of the portfolio the mutual fund’s liabilities and then 
dividing by the number of mutual fund shares outstanding. 
In contrast to mutual funds, closed-end funds sell shares like any 
other corporation and usually do not redeem their shares. Shares of 
closed-end funds sell on either an organized exchange, such as the New 

43 
Overview of Financial Markets, Financial Assets, and Market Participants 
York Stock Exchange, or in the over-the-counter market. The price of a 
share in a closed-end fund is determined by supply and demand, so the 
price can fall below or rise above the net asset value per share. 
Depository Institutions 
Depository institutions are financial intermediaries that accept deposits. 
They include commercial banks (or simply banks), savings and loan 
associations (S&Ls), savings banks, and credit unions. It is common to 
refer to depository institutions other than banks as “thrifts.” Deposi-
tory institutions are highly regulated and supervised because of the 
important role that they play in the financial system. 
The asset/liability problem that depository institutions face is quite 
simple to explain—although not necessarily easy to solve. A depository 
institution seeks to earn a positive spread between the assets it invests in 
(loans and securities) and the cost of its funds (deposits and other 
sources). This difference between income and cost is referred to as spread 
income or margin income. The spread income should allow the institu-
tion to meet operating expenses and earn a fair profit on its capital. 
In generating spread income a depository institution faces several 
risks. These include credit risk, regulatory risk, and interest rate risk. 
Regulatory risk is the risk that regulators will change the rules so as to 
adversely impact the earnings of the institution. Simply put, interest rate 
risk is the risk that a depository institution’s spread income and capital 
will suffer because of changes in interest rates. This kind of risk can be 
explained best by an illustration. To illustrate the impact on spread 
income, suppose that a depository institution raises $100 million by 
issuing a certificate of deposit that has a maturity of one year and by 
agreeing to pay an interest rate of 7%. Ignoring for the time being the 
fact that the depository institution cannot invest the entire $100 million 
because of reserve requirements, suppose that $100 million is invested 
in a U.S. Treasury security that matures in 15 years paying an interest 
rate of 9%. Because the funds are invested in a U.S. Treasury security, 
there is no credit risk. 
It seems at first that the depository institution has locked in a spread 
of 2% (9% minus 7%). This spread can be counted on only for the first 
year, though, because the spread in future years will depend on the 
interest rate this depository institution will have to pay depositors in 
order to raise $100 million after the 1-year certificate of deposit 
matures. If interest rates decline, the spread income will increase 
because the depository institution has locked in the 9% rate. If interest 
rates rise, however, the spread income will decline. In fact, if this depos-
itory institution must pay more than 9% to depositors for the next 14 

44 
The Mathematics of Financial Modeling and Investment Management 
years, the spread income will be negative. That is, it will cost the depos-
itory institution more to finance the purchase of the Treasury security 
than it will earn on the funds invested in that security. 
In our example, the depository institution has “borrowed short” (bor-
rowed for one year) and “lent long” (invested for 15 years). This invest-
ment policy will benefit from a decline in interest rates, but suffer if 
interest rates rise. Suppose the institution could have borrowed funds for 
15 years at 7% and invested in a U.S. Treasury security maturing in one 
year earning 9%—borrowing long (15 years) and lending short (one year). 
A rise in interest rates will benefit the depository institution because it can 
then reinvest the proceeds from the maturing 1-year government security 
in a new 1-year government security offering a higher interest rate. In this 
case a decline in interest rates will reduce the spread income. If interest 
rates fall below 7%, there will be a negative spread income. 
All depository institutions face this interest rate risk problem. Man-
agers of a depository institution who have particular expectations about 
the future direction of interest rates will seek to benefit from these expec-
tations. Those who expect interest rates to rise may pursue a policy to 
borrow funds long term and lend funds short term. If interest rates are 
expected to drop, managers may elect to borrow short and lend long. 
The problem of pursuing a strategy of positioning a depository insti-
tution based on expectations is that considerable adverse financial conse-
quences will result if those expectations are not realized. The evidence on 
interest rate forecasting suggests that it is a risky business. We doubt if 
there are managers of depository institutions who have the ability to 
forecast interest rate moves so consistently that the institution can bene-
fit with any regularity. The goal of management should be to lock in a 
spread as best as possible, not to wager on interest rate movements. 
Some interest rate risk, however, is inherent in any balance sheet of 
a depository institution. Managers must be willing to accept some inter-
est rate risk, but they can take various measures to address the interest 
rate sensitivity of the institution’s liabilities and its assets. A depository 
institution should have an asset/liability committee that is responsible 
for monitoring the exposure to interest rate risk. There are several asset/ 
liability strategies for controlling interest rate risk. 
Because of the special role that depository institutions play in the 
financial system, they are highly regulated and supervised by either fed-
eral and/or state government entities. Regulators have placed restric-
tions on the types of securities that depository institutions can take a 
position in for their investment portfolio. There are risk-based capital 
requirements for depository institutions that specify capital require-
ments based on their credit risk and the interest rate risk exposures. 

45 
Overview of Financial Markets, Financial Assets, and Market Participants 
Endowments and Foundations 
Endowments and foundations include colleges, private schools, muse-
ums, and hospitals. The investment income generated from the funds 
invested by endowments and foundations is used for the operation of 
the entity. In the case of a college, the investment income is used to meet 
current operating expenses and capital expenditures (i.e., the construc-
tion of new buildings or sports facilities). 
As with pension funds, qualified endowments and foundations are 
exempt from taxation. The board of trustees, just like the plan sponsor 
for a pension fund, specifies the investment objectives and the accept-
able investment alternatives. Typically, the managers of endowments 
and foundations invest in long-term assets and have the primary goal of 
safeguarding the principal of the entity. The second goal, and an impor-
tant one, is to generate a stream of earnings that allow the endowment 
or foundation to perform its functions of supporting certain operations. 
There is a constraint imposed on an endowment or foundation in that it 
must maintain its tax-exempt status. 
COMMON STOCK 
Common stocks are also called equity securities. Equity securities repre-
sent an ownership interest in a corporation. Holders of equity securities 
are entitled to the earnings of the corporation when those earnings are 
distributed in the form of dividends; they are also entitled to a pro rata 
share of the remaining equity in case of liquidation. 
Trading Locations 
In the United States, the secondary market that trades in common stocks 
has occurred in two ways. The first is on organized exchanges, which 
are specific geographical locations called trading floors, where represen-
tatives of buyers and sellers physically meet. The trading mechanism on 
exchanges is the auction system, which results from the presence of 
many competing buyers and sellers assembled in one place. The second 
type is via over-the-counter (OTC) trading, which results from geo-
graphically dispersed traders or market-makers linked to one another 
via telecommunication systems. That is, there is no trading floor. This 
trading mechanism is a negotiated system whereby individual buyers 
negotiate with individual sellers. 
Exchange markets are called central auction specialist systems and 
OTC markets are called multiple market maker systems. In recent years 
a new method of trading common stocks via independently owned and 

46 
The Mathematics of Financial Modeling and Investment Management 
operated electronic communications networks (ECNs) has developed 
and is growing quickly. 
In the United States there are two national stock exchanges: the New 
York Stock Exchange (NYSE) and the American Stock Exchange (AMEX 
or ASE). In addition to the national exchanges, there are regional stock 
exchanges in Boston, Chicago (called the Midwest Exchange), Cincinnati, 
San Francisco (called the Pacific Coast Exchange) and Philadelphia. 
Regional exchanges primarily trade stocks from corporations based within 
their region. The major OTC market in the United States is NASDAQ (the 
National Association of Securities Dealers Automated Quotation System. 
In 1998, NASDAQ and AMEX merged to form the NASDAQ-AMEX 
Market Group, Inc. 
Stock Market Indicators 
Stock market indicators have come to perform a variety of functions, 
from serving as benchmarks for evaluating the performance of profes-
sional money managers to answering the question, “How did the mar-
ket do today?” Thus, stock market indicators (indexes or averages) have 
become a part of everyday life. Even though many of the stock market 
indicators are used interchangeably, it is important to realize that each 
indicator applies to, and measures, a different facet of the stock market. 
The most commonly quoted stock market indicator is the Dow 
Jones Industrial Average (DJIA). Other popular stock market indicators 
cited in the financial press are the Standard & Poor’s 500 Composite 
(S&P 500), the New York Stock Exchange Composite Index (NYSE 
Composite), the NASDAQ Composite Index, and the Value Line Com-
posite Average (VLCA). There are a myriad of other stock market indi-
cators such as the Wilshire stock indexes and the Russell stock indexes, 
which are followed primarily by institutional money managers. 
In general, market indexes rise and fall in fairly similar patterns. 
Although the correlations among indexes are high, the indexes do not 
move in exactly the same way at all times. The differences in movement 
reflect the different manner in which the indexes are constructed. Three 
factors enter into that construction: the universe of stocks represented by 
the sample underlying the index, the relative weights assigned to the stocks 
included in the index, and the method of averaging across all the stocks. 
Some indexes represent only stocks listed on an exchange. Examples 
are the DJIA and the NYSE Composite, which represent only stocks 
listed on the NYSE or Big Board. By contrast, the NASDAQ includes 
only stocks traded over the counter. A favorite of professionals is the 
S&P 500 because it is a broader index containing both NYSE-listed and 
OTC-traded shares. Each index relies on a sample of stocks from its 

47 
Overview of Financial Markets, Financial Assets, and Market Participants 
universe, and that sample may be small or quite large. The DJIA uses 
only 30 of the NYSE-traded shares, while the NYSE Composite includes 
every one of the listed shares. The NASDAQ also includes all shares in 
its universe, while the S&P 500 has a sample that contains only 500 of 
the more than 8,000 shares in the universe it represents. 
The stocks included in a stock market index must be combined in cer-
tain proportions, and each stock must be given a weight. The three main 
approaches to weighting are: (1) weighting by the market capitalization, 
which is the value of the number of shares times price per share; (2) 
weighting by the price of the stock; and (3) equal weighting for each 
stock, regardless of its price or its firm’s market value. With the exception 
of the Dow Jones averages (such as the DJIA) and the VLCA, nearly all of 
the most widely used indexes are market-value weighted. The DJIA is a 
price-weighted average, and the VLCA is an equally weighted index. 
Stock market indicators can be classified into three groups: (1) those 
produced by stock exchanges based on all stocks traded on the 
exchanges; (2) those produced by organizations that subjectively select 
the stocks to be included in indexes; and (3) those where stock selection 
is based on an objective measure, such as the market capitalization of 
the company. The first group includes the New York Stock Exchange 
Composite Index, which reflects the market value of all stocks traded on 
the NYSE. While it is not an exchange, the NASDAQ Composite Index 
falls into this category because the index represents all stocks traded on 
the NASDAQ system. 
The three most popular stock market indicators in the second group 
are the Dow Jones Industrial Average, the Standard & Poor’s 500, and 
the Value Line Composite Average. The DJIA is constructed from 30 of 
the largest blue chip industrial companies traded on the NYSE. The 
companies included in the average are those selected by Dow Jones & 
Company, publisher of the Wall Street Journal. The S&P 500 represents 
stocks chosen from the two major national stock exchanges and the 
over-the-counter market. The stocks in the index at any given time are 
determined by a committee of Standard & Poor’s Corporation, which 
may occasionally add or delete individual stocks or the stocks of entire 
industry groups. The aim of the committee is to capture present overall 
stock market conditions as reflected in a very broad range of economic 
indicators. The VLCA, produced by Value Line Inc., covers a broad 
range of widely held and actively traded NYSE, AMEX, and OTC issues 
selected by Value Line. 
In the third group we have the Wilshire indexes produced by 
Wilshire Associates (Santa Monica, California) and Russell indexes pro-
duced by the Frank Russell Company (Tacoma, Washington), a consult-
ant to pension funds and other institutional investors. The criterion for 

48 
The Mathematics of Financial Modeling and Investment Management 
inclusion in each of these indexes is solely a firm’s market capitalization. 
The most comprehensive index is the Wilshire 5000, which actually 
includes more than 6,700 stocks now, up from 5,000 at its inception. 
The Wilshire 4500 includes all stocks in the Wilshire 5000 except for 
those in the S&P 500. Thus, the shares in the Wilshire 4500 have 
smaller capitalization than those in the Wilshire 5000. The Russell 3000 
encompasses the 3,000 largest companies in terms of their market capi-
talization. The Russell 1000 is limited to the largest 1,000 of those, and 
the Russell 2000 has the remaining smaller firms. 
Two methods of averaging may be used. The first and most common 
is the arithmetic average. An arithmetic mean is just a simple average of 
the stocks, calculated by summing them (after weighting, if appropriate) 
and dividing by the sum of the weights. The second method is the geo-
metric mean, which involves multiplication of the components, after 
which the product is raised to the power of 1 divided by the number of 
components. 
Trading Arrangements 
Below we describe the key features involved in trading stocks. 
Types of Orders 
When an investor wants to buy or sell a share of common stock, the 
price and conditions under which the order is to be executed must be 
communicated to a broker. The simplest type of order is the market 
order, an order to be executed at the best price available in the market. 
The danger of a market order is that an adverse move may take 
place between the time the investor places the order and the time the 
order is executed. To avoid this danger, the investor can place a limit 
order that designates a price threshold for the execution of the trade. 
The key disadvantage of a limit order is that there is no guarantee that it 
will be executed at all; the designated price may simply not be obtain-
able. The limit order is a conditional order: It is executed only if the 
limit price or a better price can be obtained. 
Another type of conditional order is the stop order, which specifies 
that the order is not to be executed until the market moves to a desig-
nated price, at which time it becomes a market order. There are two 
dangers associated with stop orders. Stock prices sometimes exhibit 
abrupt price changes, so the direction of a change in a stock price may 
be quite temporary, resulting in the premature trading of a stock. Also, 
once the designated price is reached, the stop order becomes a market 
order and is subject to the uncertainty of the execution price noted ear-
lier for market orders. A stop-limit order, a hybrid of a stop order and a 

49 
Overview of Financial Markets, Financial Assets, and Market Participants 
limit order, is a stop order that designates a price limit. In contrast to 
the stop order, which becomes a market order if the stop is reached, the 
stop-limit order becomes a limit order if the stop is reached. The stop-
limit order can be used to cushion the market impact of a stop order. 
The investor may limit the possible execution price after the activation 
of the stop. As with a limit order, the limit price may never be reached 
after the order is activated, which therefore defeats one purpose of the 
stop order—to protect a profit or limit a loss. 
Short Selling 
Short selling involves the sale of a security not owned by the investor at 
the time of sale. The investor can arrange to have her broker borrow the 
stock from someone else, and the borrowed stock is delivered to imple-
ment the sale. To cover her short position, the investor must subsequently 
purchase the stock and return it to the party that lent the stock. The 
investor benefits if the price of the of the security sold short declines. Two 
costs will reduce the profit on a short sale. First, a fee will be charged by 
the lender of the stock. Second, if there are any dividends paid, the short 
seller must pay those dividends to the lender of the security. 
Exchanges impose restrictions as to when a short sale may be exe-
cuted; these so-called tick-test rules are intended to prevent investors 
from destabilizing the price of a stock when the market price is falling. 
A short sale can be made only when either (1) the sale price of the par-
ticular stock is higher than the last trade price (referred to as an “uptick 
trade”), or (2) if there is no change in the last trade price of the particu-
lar stock (referred to as a “zero uptick”), the previous trade price must 
be higher than the trade price that preceded it. 
Margin Transactions 
Investors can borrow cash to buy securities and use the securities them-
selves as collateral. A transaction in which an investor borrows to buy 
shares using the shares themselves as collateral is called buying on mar-
gin. By borrowing funds, an investor creates financial leverage. The 
funds borrowed to buy the additional stock will be provided by the bro-
ker, and the broker gets the money from a bank. The interest rate that 
banks charge brokers for these funds is the call money rate (also labeled 
the broker loan rate). The broker charges the borrowing investor the 
call money rate plus a service charge. 
The brokerage firm is not free to lend as much as it wishes to the 
investor to buy securities. The Securities Exchange Act of 1934 prohib-
its brokers from lending more than a specified percentage of the market 
value of the securities. The initial margin requirement is the proportion 

50 
The Mathematics of Financial Modeling and Investment Management 
of the total market value of the securities that the investor must pay as 
an equity share, and the remainder is borrowed from the broker. The 
1934 act gives the Board of Governors of the Federal Reserve (the Fed) 
the responsibility to set initial margin requirements. The initial margin 
requirement has been below 40% and is 50% as of this writing. 
The Fed also establishes a maintenance margin requirement. This is 
the minimum proportion of (1) the equity in the investor’s margin 
account to (2) the total market value. If the investor’s margin account 
falls below the minimum maintenance margin (which would happen if 
the share price fell), the investor is required to put up additional cash. 
The investor receives a margin call from the broker specifying the addi-
tional cash to be put into the investor’s margin account. If the investor 
fails to put up the additional cash, the broker has the authority to sell 
the securities in the investor’s account. 
Trading Arrangements Used by Institutional Investors 
With the increase in trading by institutional investors, trading arrange-
ments more suitable to these investors were developed. Institutional 
needs included trading in large size and trading groups of stocks, both 
at a low commission and with low market impact. This has resulted in 
the evolution of special arrangements for the execution of certain types 
of orders commonly sought by institutional investors: (1) orders requir-
ing the execution of a trade of a large number of shares of a given stock 
and (2) orders requiring the execution of trades in a large number of dif-
ferent stocks at as near the same time as possible. The former types of 
trades are called block trades; the latter are called program trades. 
On the NYSE, block trades are defined as either trades of at least 
10,000 shares of a given stock, or trades of shares with a market value 
of at least $200,000, whichever is less. Program trades involve the buy-
ing and/or selling of a large number of names simultaneously. Such 
trades are also called basket trades because effectively a “basket” of 
stocks is being traded. The NYSE defines a program trade as any trade 
involving the purchase or sale of a basket of at least 15 stocks with a 
total value of $1 million or more. 
The institutional arrangement that has evolved to accommodate 
these two types of institutional trades is the development of a network 
of trading desks of the major securities firms and other institutional 
investors that communicate with each other by means of electronic dis-
play systems and telephones. This network is referred to as the “upstairs 
market.” Participants in the upstairs market play a key role by (1) pro-
viding liquidity to the market so that such institutional trades can be 

51 
Overview of Financial Markets, Financial Assets, and Market Participants 
executed, and (2) by arbitrage activities that help to integrate the frag-
mented stock market. 
BONDS 
In its simplest form, a bond is a financial obligation of an entity that 
promises to pay a specified sum of money at specified future dates. The 
entity that promises to make the payment is called the bond issuer and is 
referred to as the borrower. Bond issuers include central governments, 
municipal/provincial governments, supranational (e.g., the World 
Bank), and corporations. The investor who purchases bond is said to be 
the lender or creditor. The promised payments that the bond issuer 
agrees to make at the specified dates consist of two components: interest 
payments and repayment of the amount borrowed. 
Prior to the 1980s, bonds were simple investment vehicles. Holding 
aside default by the bond issuer, the investor knew how much interest 
would be received periodically and when the amount borrowed would 
be repaid. Moreover, most investors purchased bonds with the intent of 
holding them to their maturity date. Beginning in the 1980s, the bond 
world changed. First, bond structures became more complex. There are 
features in many bonds that make it difficult to determine when the 
amount borrowed will be repaid. For some bonds it is difficult to 
project the amount of interest that will be received periodically. Second, 
the hold-to-maturity investor has been replaced by the institutional 
investor who actively trades bonds. These new product design features 
in bonds and the shift in trading strategies have lead to the increased use 
of the mathematical techniques described in later chapters. 
Maturity 
The term to maturity of a bond is the number of years over which the 
issuer has promised to meet the conditions of the obligation. The matu-
rity of a bond refers to the date that the debt will cease to exist, at 
which time the bond issuer will redeem the bond by paying the amount 
borrowed. The maturity date of a bond is always identified when 
describing a bond. For example, a description of a bond might state 
“due 12/1/2020.” The practice in the bond market is to refer to the 
“term to maturity” of a bond as simply its “maturity” or “term.” As we 
explain later, there may be provisions in the bond agreement that allow 
either the bond issuer or bondholder to alter a bond’s term to maturity. 
There are three reasons why the term to maturity of a bond is 
important. The most obvious is that it indicates the time period over 

52 
The Mathematics of Financial Modeling and Investment Management 
which the bondholder can expect to receive interest payments and the 
number of years before the principal will be paid in full. The second rea-
son is that the yield on a bond depends on it. Finally, the price of a bond 
will fluctuate over its life as interest rates in the market change. The 
price volatility of a bond is dependent on its maturity. More specifically, 
with all other factors constant, the longer the maturity of a bond, the 
greater the price volatility resulting from a change in interest rates. We 
will demonstrate these two properties in Chapter 4 as an application of 
calculus. 
Par Value 
The par value of a bond is the amount that the issuer agrees to repay the 
bondholder by the maturity date. This amount is also referred to as the 
principal, face value, redemption value, or maturity value. Bonds can 
have any par value. 
Because bonds can have a different par value and currency (e.g., 
U.S. dollar, euro, pound sterling), the practice is to quote the price of a 
bond as a percentage of its par value. A value of 100 means 100% of 
par value. So, for example, if a bond has a par value of $1,000 and the 
issue is selling for $900, this bond would be said to be selling at 90. If a 
bond with a par value of Eur 5,000 is selling for Eur 5,500, the bond is 
said to be selling for 110. 
Coupon Rate 
The coupon rate, also called the nominal rate, is the interest rate that 
the bond issuer agrees to pay each year. The annual amount of the inter-
est payment made to bondholders during the term of the bond is called 
the coupon. The coupon is determined by multiplying the coupon rate 
by the par value of the bond. For example, a bond with an 8% coupon 
rate and a par value of $1,000 will pay annual interest of $80. 
When describing a bond of an issuer, the coupon rate is indicated along 
with the maturity date. For example, the expression “6s of 12/1/2020” 
means a bond with a 6% coupon rate maturing on 12/1/2020. 
In the United States, the usual practice is for the issuer to pay the cou-
pon in two semiannual installments. Outside the U.S., bond payments 
with semiannual and annual payments are found. For certain sectors of 
the bond market—mortgage-backed and asset-backed securities—pay-
ments are made monthly. If the bondholder sells a bond between coupon 
payments and the buyer holds it until the next coupon payment, then the 
entire coupon interest earned for the period will be paid to the buyer of 
the bond since the buyer will be the holder of record. The seller of the 
bond gives up the interest from the time of the last coupon payment to the 

53 
Overview of Financial Markets, Financial Assets, and Market Participants 
time until the bond is sold. The amount of interest over this period that 
will be received by the buyer, even though it was earned by the seller, is 
called accrued interest. In the United States and in many countries, the 
bond buyer must pay the bond seller the accrued interest. The amount 
that the buyer pays the seller is the agreed-upon price for the bond plus 
accrued interest. This amount is called the dirty price. The agreed-upon 
bond price without accrued interest is called the clean price. 
In addition to indicating the coupon payments that the investor 
should expect to receive over the term of the bond, the coupon rate also 
affects the bond’s price sensitivity to changes in market interest rates. As 
illustrated later, all other factors constant, the higher the coupon rate, 
the less the price will change in response to a change in market interest 
rates. Again, this property will be demonstrated as an application of cal-
culus in Chapter 4. 
Not all bonds make periodic coupon payments. Bonds that are not 
contracted to make periodic coupon payments are called zero-coupon 
bonds. The holder of a zero-coupon bond realizes interest by buying the 
bond substantially below its par value. Interest then is paid at the matu-
rity date, with the interest being the difference between the par value 
and the price paid for the bond. So, for example, if an investor pur-
chases a zero-coupon bond for 70, the interest is 30. This is the differ-
ence between the par value (100) and the price paid (70). 
The coupon rate on a bond need not be fixed over the bond’s term. 
Floating-rate securities have coupon payments that reset periodically 
according to some reference rate. The typical formula for the coupon 
rate at the dates when the coupon rate is reset is: 
Reference rate + Quoted margin 
The quoted margin is the additional amount that the issuer agrees to 
pay above the reference rate. For example, suppose that the reference 
rate is the 1-month London interbank offered rate (LIBOR). Suppose 
that the quoted margin is 100 basis points. Then the coupon reset for-
mula is: 
1-month LIBOR + 100 basis points 
So, if 1-month LIBOR on the coupon reset date is 5%, the coupon rate 
is reset for that period at 6% (5% plus 100 basis points). 
The reference rate for most floating-rate securities is an interest rate 
or an interest rate index. There are some issues where this is not the 
case. Instead, the reference rate is some financial index such as the 
return on the Standard & Poor’s 500 or a nonfinancial index such as the 

54 
The Mathematics of Financial Modeling and Investment Management 
price of a commodity. Through financial engineering, issuers have been 
able to structure floating-rate securities with almost any reference rate. 
In several countries, there are government bonds whose coupon reset 
formula is tied to an inflation index. 
A floating-rate security may have a restriction on the maximum cou-
pon rate that will be paid at a reset date. The maximum coupon rate is 
called a cap. Because a cap restricts the coupon rate from increasing, a 
cap is an unattractive feature for the investor. In contrast, there could be 
a minimum coupon rate specified for a floating-rate security. The mini-
mum coupon rate is called a floor. If the coupon reset formula produces 
a coupon rate that is below the floor, the floor is paid instead. Thus, a 
floor is an attractive feature for the investor. 
Financial engineering has also allowed bond issuers to create inter-
esting floating-rate structures. These include the following:
 ■ Inverse floaters. Typically, the coupon reset formula on floating-rate 
securities is such that the coupon rate increases when the reference rate 
increases, and decreases when the reference rate decreases. With an 
inverse floater the coupon rate moves in the opposite direction from the 
change in the reference rate. A general formula for an inverse floater is 
K – L (Reference rate) with a floor of zero.
 ■ Range notes. A range note is a bond whose coupon rate is equal to the 
reference rate as long as the reference rate is within a certain range at 
the reset date. If the reference rate is outside of the range, the coupon 
rate is zero for that period. For example, a 3-year range note might 
specify that the reference rate is 1-year LIBOR and that the coupon rate 
resets every year. The coupon rate for the year will be 1-year LIBOR as 
long as 1-year LIBOR at the coupon reset date falls within the range as 
specified below: 
Year 1 
Year 2 
Year 3 
Lower limit of range 
4.5% 
5.25% 
6.00% 
Upper limit of range 
5.5% 
6.75% 
7.50% 
If 1-year LIBOR is outside of the range, the coupon rate is zero.
 ■ Stepup notes. There are bonds whose coupon rate increases over time. 
These securities are called stepup notes because the coupon rate “steps 
up” over time. For example, a 5-year stepup note might have a coupon 
rate that is 5% for the first 2 years and 6% for the last 3 years. Or, the 
stepup note could call for a 5% coupon rate for the first 2 years, 5.5% 

55 
Overview of Financial Markets, Financial Assets, and Market Participants 
for the third and fourth years, and 6% for the fifth year. When there is 
only one change (or stepup), as in our first example, the issue is 
referred to as a single stepup note. When there is more than one 
increase, as in our second example, the issue is referred to as a multiple 
stepup note. 
Provisions for Paying off Bonds 
The bond issuer of a bond agrees to repay the principal by the stated 
maturity date. The issuer can agree to repay the entire amount bor-
rowed in one lump sum payment at the maturity date. That is, the issuer 
is not required to make any principal repayments prior to the maturity 
date. Such bonds are said to have a bullet maturity. Bonds backed by 
pools of loans (mortgage-backed securities and asset-backed securities) 
often have a schedule of principal repayments. Such bonds are said to be 
amortizing securities. For many loans, the payments are structured so 
that when the last loan payment is made, the entire amount owed is 
fully paid off. 
There are bond issues that have a provision granting the bond issuer 
an option to retire all or part of the issue prior to the stated maturity 
date. This feature is referred to as a call feature and a bond with this 
feature is said to be a callable bond. If the issuer exercises this right, the 
issuer is said to “call the bond.” The price that the bond issuer must pay 
to retire the issue is referred to as the call price. Typically, there is not 
one call price but a call schedule, which sets forth a call price based on 
when the issuer can exercise the call option. When a bond is issued, typ-
ically the issuer may not call the bond for a number of years. That is, 
the issue is said to have a deferred call. 
A bond issuer generally wants the right to retire a bond issue prior 
to the stated maturity date because it recognizes that at some time in the 
future the general level of interest rates may fall sufficiently below the 
issue’s coupon rate so that redeeming the issue and replacing it with 
another issue with a lower coupon rate would be economically benefi-
cial. This right is a disadvantage to the bondholder since proceeds 
received must be reinvested at a lower interest rate. As a result, an issuer 
who wants to include this right as part of a bond offering must compen-
sate the bondholder when the issue is sold by offering a higher coupon 
rate, or equivalently, accepting a lower price than if the right is not 
included. 
If a bond issue does not have any protection against early call, then 
it is said to be a currently callable issue. But most new bond issues, even 
if currently callable, usually have some restrictions against certain types 
of early redemption. The most common restriction is prohibiting the 

56 
The Mathematics of Financial Modeling and Investment Management 
refunding of the bonds for a certain number of years. Refunding a bond 
issue means redeeming bonds with funds obtained through the sale of a 
new bond issue. Call protection is much more absolute than refunding 
protection. While there may be certain exceptions to absolute or com-
plete call protection in some cases, it still provides greater assurance 
against premature and unwanted redemption than does refunding pro-
tection. Refunding prohibition merely prevents redemption only from 
certain sources of funds, namely the proceeds of other debt issues sold 
at a lower cost of money. The bondholder is only protected if interest 
rates decline, and the borrower can obtain lower-cost money to pay off 
the debt. 
For amortizing securities that are backed by loans and have a sched-
ule of principal repayments, individual borrowers typically have the 
option to pay off all or part of their loan prior to the scheduled date. 
Any principal repayment prior to the scheduled date is called a prepay-
ment. The right of borrowers to prepay is called the prepayment option. 
Basically, the prepayment option is the same as a call option. However, 
unlike a call option, there is not a call price that depends on when the 
borrower pays off the issue. Typically, the price at which a loan is pre-
paid is par value. 
Options Granted to Bondholders 
A bond issue may include a provision that gives either the bondholder 
and/or the issuer an option to take some action against the other party. 
The most common type of option embedded in a bond is a call feature, 
which was discussed earlier. This option is granted to the issuer. There 
are two options that can be granted to the bondholder: the right to put 
the issue and the right to convert the issue. 
An issue with a put provision grants the bondholder the right to sell 
the issue back to the issuer at a specified price on designated dates. The 
bond with this feature is called a putable bond and the specified price is 
called the put price. The advantage of the put provision to the bondholder 
is that if after the issue date market rates rise above the issue’s coupon 
rate, the bondholder can force the issuer to redeem the bond at the put 
price and then reinvest the proceeds at the prevailing higher rate. 
A convertible bond is an issue giving the bondholder the right to 
exchange the bond for a specified number of shares of common stock. 
Such a feature allows the bondholder to take advantage of favorable 
movements in the price of the bond issuer’s common stock. An 
exchangeable bond allows the bondholder to exchange the issue for a 
specified number of shares of common stock of a corporation different 
from the issuer of the bond. 

57 
Overview of Financial Markets, Financial Assets, and Market Participants 
FUTURES AND FORWARD CONTRACTS 
A futures contract is an agreement that requires a party to the agree-
ment either to buy or sell something at a designated future date at a pre-
determined price. Futures contracts are products created by exchanges. 
To create a particular futures contract, an exchange must obtain 
approval from the Commodity Futures Trading Commission (CFTC), a 
government regulatory agency. When applying to the CFTC for 
approval to create a futures contract, the exchange must demonstrate 
that there is an economic purpose for the contract. Futures contracts are 
categorized as either commodity futures or financial futures. Commod-
ity futures involve traditional agricultural commodities (such as grain 
and livestock), imported foodstuffs (such as coffee, cocoa, and sugar), 
and industrial commodities. Futures contracts based on a financial 
instrument or a financial index are known as financial futures. Financial 
futures can be classified as (1) stock index futures, (2) interest rate 
futures, and (3) currency futures. 
A party to a futures contract has two choices on liquidation of the 
position. First, the position can be liquidated prior to the settlement 
date. For this purpose, the party must take an offsetting position in the 
same contract. For the buyer of a futures contract, this means selling the 
same number of identical futures contracts; for the seller of a futures 
contract, this means buying the same number of identical futures con-
tracts. The alternative is to wait until the settlement date. At that time 
the party purchasing a futures contract accepts delivery of the underly-
ing (financial instrument, currency, or commodity) at the agreed-upon 
price; the party that sells a futures contract liquidates the position by 
delivering the underlying at the agreed-upon price. For some futures 
contracts settlement is made in cash only. Such contracts are referred to 
as cash-settlement contracts. 
Associated with every futures exchange is a clearinghouse, which 
performs two key functions. First, the clearinghouse guarantees that the 
two parties to the transaction will perform. It does so as follows. When 
an investor takes a position in the futures market, the clearinghouse 
takes the opposite position and agrees to satisfy the terms set forth in 
the contract. Because of the clearinghouse, the investor need not worry 
about the financial strength and integrity of the party taking the oppo-
site side of the contract. After initial execution of an order, the relation-
ship between the two parties ends. The clearinghouse interposes itself as 
the buyer for every sale and the seller for every purchase. Thus investors 
are free to liquidate their positions without involving the other party in 
the original contract, and without worry that the other party may 
default. In addition to the guarantee function, the clearinghouse makes 

58 
The Mathematics of Financial Modeling and Investment Management 
it simple for parties to a futures contract to unwind their positions prior 
to the settlement date. 
When a position is first taken in a futures contract, the investor 
must deposit a minimum dollar amount per contract as specified by the 
exchange. This amount is called the initial margin and is required as 
deposit for the contract. The initial margin may be in the form of an 
interest-bearing security such as a Treasury bill. As the price of the 
futures contract fluctuates, the value of the investor’s equity in the posi-
tion changes. At the end of each trading day, the exchange determines 
the settlement price for the futures contract. This price is used to mark 
to market the investor’s position, so that any gain or loss from the posi-
tion is reflected in the investor’s equity account. 
Maintenance margin is the minimum level (specified by the 
exchange) by which an investor’s equity position may fall as a result of 
an unfavorable price movement before the investor is required to 
deposit additional margin. The additional margin deposited is called 
variation margin, and it is an amount necessary to bring the equity in 
the account back to its initial margin level. Unlike initial margin, varia-
tion margin must be in cash not interest-bearing instruments. Any 
excess margin in the account may be withdrawn by the investor. If a 
party to a futures contract who is required to deposit variation margin 
fails to do so within 24 hours, the futures position is closed out. 
Although there are initial and maintenance margin requirements for 
buying securities on margin, the concept of margin differs for securities and 
futures. When securities are acquired on margin, the difference between the 
price of the security and the initial margin is borrowed from the broker. 
The security purchased serves as collateral for the loan, and the investor 
pays interest. For futures contracts, the initial margin, in effect, serves as 
“good faith” money, an indication that the investor will satisfy the obliga-
tion of the contract. Normally no money is borrowed by the investor. 
Futures versus Forward Contracts 
A forward contract, just like a futures contract, is an agreement for the 
future delivery of something at a specified price at the end of a desig-
nated period of time. Futures contracts are standardized agreements as 
to the delivery date (or month) and quality of the deliverable, and are 
traded on organized exchanges. A forward contract differs in that it is 
usually nonstandardized (that is, the terms of each contract are negoti-
ated individually between buyer and seller), there is no clearinghouse, 
and secondary markets are often nonexistent or extremely thin. Unlike a 
futures contract, which is an exchange-traded product, a forward con-
tract is an over-the-counter instrument. 

59 
Overview of Financial Markets, Financial Assets, and Market Participants 
Futures contracts are marked to market at the end of each trading 
day. Consequently, futures contracts are subject to interim cash flows as 
additional margin may be required in the case of adverse price move-
ments, or as cash is withdrawn in the case of favorable price move-
ments. A forward contract may or may not be marked to market, 
depending on the wishes of the two parties. For a forward contract that 
is not marked to market, there are no interim cash flow effects because 
no additional margin is required. 
Finally, the parties in a forward contract are exposed to credit risk 
because either party may default on the obligation. Credit risk is mini-
mal in the case of futures contracts because the clearinghouse associated 
with the exchange guarantees the other side of the transaction. 
Other than these differences, most of what we say about futures 
contracts applies equally to forward contracts. 
Risk and Return Characteristics of Futures Contracts 
When an investor takes a position in the market by buying a futures 
contract, the investor is said to be in a long position or to be long 
futures. If, instead, the investor’s opening position is the sale of a 
futures contract, the investor is said to be in a short position or short 
futures. The buyer of a futures contract will realize a profit if the futures 
price increases; the seller of a futures contract will realize a profit if the 
futures price decreases; if the futures price decreases, the buyer of the 
futures contract realizes a loss while the seller of a futures contract real-
izes a profit. Notice that the risk-return is symmetrical for a favorable 
and adverse price movement. 
When a position is taken in a futures contract, the party need not 
put up the entire amount of the investment. Instead, only initial margin 
must be put up. Thus a futures contract, as with other derivatives, 
allows a market participant to create leverage. While the degree of 
leverage available in the futures market varies from contract to contract, 
the leverage attainable is considerably greater than in the cash market 
by buying on margin. While at first the leverage available in the futures 
market may suggest that the market benefits only those who want to 
only speculate on price movements. This is not true. Futures markets 
can be used to reduce price risk. Without the leverage possible in futures 
transactions, the cost of reducing price risk using futures would be too 
high for many market participants. 
Pricing of Futures Contracts 
In later chapters we will see how the mathematical tools presented in 
this book can be applied to valuing complex financial instruments. 

60 
The Mathematics of Financial Modeling and Investment Management 
However, the pricing of futures contracts does not require any high level 
mathematical analysis. Rather it is based on simple arbitrage arguments 
discussed in Chapter 14. To see this, let’s derive the theoretical price of a 
futures contract using simple algebra. All we need to know is the fol-
lowing:
 ■ The price that the underlying asset for the futures contract is selling for 
in the cash market.
 ■ The cash yield earned on the underlying asset until the settlement date.
 ■ The interest rate for borrowing and lending until the settlement date. 
Let 
r = financing cost 
y = cash yield on underlying asset 
P = cash market price ($) of the underlying asset 
F = futures price ($) 
Now consider the following strategy, referred to as a cash and carry 
trade:
 ■ Sell the futures contract at F
 ■ Purchase the underlying asset in the cash market for P
 ■ Borrow P until the settlement date at the financing cost of r 
The outcome at the settlement date then is: 
1. From Settlement of the Futures Contract 
Proceeds from sale of the underlying asset to settle the 
= F 
futures contract 
Payment received from investing in the underlying asset for = yP 
3 months 
Total proceeds 
= F + yP 
2. From the Loan 
Repayment of the principal of loan 
= P 
Interest on loan 
= rP 
Total outlay 
= P + rP 
The profit will equal: 

61 
Overview of Financial Markets, Financial Assets, and Market Participants 
Profit = Total proceeds – Total outlay 
= F + yP – (P + rP) 
The theoretical futures price is where the profit from this strategy is 
zero. Thus, to have equilibrium, the following must hold: 
0 = F + yP – (P + rP) 
Solving for the theoretical futures price, we have: 
F = P + P (r – y) 
Alternatively, consider the following strategy called a reverse cash 
and carry trade:
 ■ Buy the futures contract at F
 ■ Sell (short) the underlying asset for P
 ■ Invest (lend) P at r until the settlement date 
The outcome at the settlement date would be: 
1. From Settlement of the Futures Contract 
Price paid for purchase of the underlying asset to settle 
= F 
futures contract 
Payment to lender of the underlying asset in order to borrow = yP 
the asset 
Total outlay 
= F + yP 
2. From the Loan 
Proceeds received from maturing of the loan investment 
= P 
Interest earned 
= rP 
Total proceeds 
= P + rP 
The profit will equal: 
Profit = Total proceeds – Total outlay 
= P + rP – (F + yP) 
Setting the profit equal to zero so that there will be no arbitrage profit 
and solving for the futures price, we would obtain the same equation for 
the theoretical futures price as given from the cash and carry trade. 

62 
The Mathematics of Financial Modeling and Investment Management 
The theoretical futures price may be at a premium to the cash market 
price (higher than the cash market price) or at a discount from the cash 
market price (lower than the cash market price) depending on P(r – y). 
The term r – y, which reflects the difference between the cost of financing 
and the asset’s cash yield, is called the net financing cost. The net financ-
ing cost is more commonly called the cost of carry or, simply, carry. Posi-
tive carry means that the yield earned is greater than the financing cost; 
negative carry means that the financing cost exceeds the yield earned. 
At the delivery date, the futures price must be equal to the cash market 
price. Thus, as the delivery date approaches, the futures price will con-
verge to the cash market price. This can be seen by looking at the equation 
for the theoretical futures price. As the delivery date approaches, the 
financing cost approaches zero, and the yield that can be earned by hold-
ing the investment approaches zero. Hence the cost of carry approaches 
zero, and the futures price will approach the cash market price. 
To derive the theoretical futures price using the arbitrage argument, 
several assumptions are made. When the assumptions are violated, there 
will be a divergence between the actual futures price and the theoretical 
futures price as derived above; that is, the difference between the two 
prices will differ from carry. The reasons for the deviation of the actual 
futures price from the theoretical futures price are as follows. 
First, no interim cash flows due to variation margin are assumed. In 
addition, any cash flows payments from the underlying asset are assumed 
to be paid at the delivery date rather than at an interim date. However, we 
know that interim cash flows can occur for both of these reasons. Because 
we assume no variation margin, the theoretical price for the contract is 
technically the theoretical price for a forward contract that is not marked 
to market, not the theoretical price for a futures contract. This is because, 
unlike a futures contract, a forward contract that is not marked to market 
at the end of each trading day does not require additional margin. 
Second, in deriving the theoretical futures price it is assumed that 
the borrowing rate and lending rate are equal. Typically, however, the 
borrowing rate is greater than the lending rate. Letting rB denote the 
borrowing rate and rL denote the lending rate, then the following 
boundaries would exist for the theoretical futures price: 
Upper boundary: F = P + P(rB – y) 
Lower boundary: F = P + P(rL – y) 
Third, in determining the theoretical futures price, transaction costs 
involved in establishing the positions are ignored. In actuality, there are 

63 
Overview of Financial Markets, Financial Assets, and Market Participants 
transaction costs of entering into and closing the cash position as well 
as round-trip transactions costs for the futures contract that do affect 
the theoretical futures price. Transaction costs widen the boundaries for 
the theoretical futures price. 
In the strategy involving short-selling of the underlying asset, it is 
assumed that the proceeds from the short sale are received and rein-
vested. In practice, for individual investors, the proceeds are not 
received, and, in fact, the individual investor is required to put up mar-
gin (securities margin not futures margin) to short-sell. For institutional 
investors, the asset may be borrowed, but there is a cost to borrowing. 
This cost of borrowing can be incorporated into the model by reducing 
the yield on the asset. 
In our derivation, we assumed that only one asset is deliverable. 
There are futures contracts, such as the government bond futures con-
tract in the United States and other countries, where the short has the 
option of delivering one of several acceptable issues to satisfy the 
futures contract. Thus, the buyer of a futures contract with this feature 
does not know what the deliverable asset will be. This leads to the 
notion of the “cheapest to deliver asset.” It is not difficult to value this 
option granted to the short. 
Finally, the underlying for some futures contracts is not a single 
asset but a basket of assets, or an index. Stock index futures contracts 
are an example. The problem in arbitraging these futures contracts on 
an index is that it is too expensive to buy or sell every asset included in 
the index. Instead, a portfolio containing a smaller number of assets 
may be constructed to “track” the index. The arbitrage, however, is no 
longer risk-free because there is the risk that the portfolio will not track 
the index exactly. All of this leads to higher transaction costs and uncer-
tainty about the outcome of the arbitrage. 
The Role of Futures in Financial Markets 
Without financial futures, investors would have only one trading loca-
tion to alter portfolio positions when they get new information that is 
expected to influence the value of assets—the cash market. If economic 
news that is expected to impact the value of an asset adversely is 
received, investors can reduce their price risk exposure to that asset. The 
opposite is true if the new information is expected to impact the value 
of that asset favorably: an investor would increase price-risk exposure 
to that asset. There are, of course, transaction costs associated with 
altering exposure to an asset—explicit costs (commissions), and hidden 
or execution costs (bid-ask spreads and market impact costs). 

64 
The Mathematics of Financial Modeling and Investment Management 
Futures provide another market that investors can use to alter their 
risk exposure to an asset when new information is acquired. An investor 
will transact in the market that is the more efficient to use in order to 
achieve the objective. The factors to consider are liquidity, transaction 
costs, taxes, and leverage advantages of the futures contract. The mar-
ket that investors feel is the one that is more efficient to use to achieve 
their investment objective should be the one where prices will be estab-
lished that reflect the new economic information. That is, this will be 
the market where price discovery takes place. Price information is then 
transmitted to the other market. It is in the futures market that it is eas-
ier and less costly to alter a portfolio position. Therefore, it is the 
futures market that will be the market of choice and will serve as the 
price discovery market. It is in the futures market that investors send a 
collective message about how any new information is expected to 
impact the cash market. 
How is this message sent to the cash market? We know that the 
futures price and the cash market price are tied together by the cost of 
carry. If the futures price deviates from the cash market price by more 
than the cost of carry, arbitrageurs (in attempting to obtain arbitrage 
profits) would pursue a strategy to bring them back into line. Arbitrage 
brings the cash market price into line with the futures price. It is this 
mechanism that assures that the cash market price will reflect the infor-
mation that has been collected in the futures market. 
OPTIONS 
An option is a contract in which the writer of the option grants the buyer 
of the option the right, but not the obligation, to purchase from or sell to 
the writer something at a specified price within a specified period of time 
(or at a specified date). The writer, also referred to as the seller, grants 
this right to the buyer in exchange for a certain sum of money, which is 
called the option price or option premium. The price at which the asset 
may be bought or sold is called the exercise or strike price. The date after 
which an option is void is called the expiration date. 
When an option grants the buyer the right to purchase the desig-
nated instrument from the writer (seller), it is referred to as a call 
option, or call. When the option buyer has the right to sell the desig-
nated instrument to the writer, the option is called a put option, or put. 
Buying calls or selling puts allows the investor to gain if the price of the 
underlying asset rises. Selling calls and buying puts allows the investor 
to gain if the price of the underlying asset falls. 

65 
Overview of Financial Markets, Financial Assets, and Market Participants 
An option is also categorized according to when the option buyer may 
exercise the option. There are options that may be exercised at any time up 
to and including the expiration date. Such an option is referred to as an 
American option. There are options that may be exercised only at the 
expiration date. An option with this feature is called a European option. 
There are no margin requirements for the buyer of an option once 
the option price has been paid in full. Because the option price is the 
maximum amount that the investor can lose, no matter how adverse the 
price movement of the underlying asset, there is no need for margin. 
Because the writer of an option has agreed to accept all of the risk (and 
none of the reward) of the position in the underlying asset, the writer is 
generally required to put up the option price received as margin. In 
addition, as price changes occur that adversely affect the writer’s posi-
tion, the writer is required to deposit additional margin (with some 
exceptions) as the position is marked to market. 
Options, like other financial instruments, may be traded either on 
an organized exchange or in the over-the-counter market. An exchange 
that wants to create an options contract must obtain approval from 
either the Commodities Futures Trading Commission or the Securities 
and Exchange Commission. Exchange-traded options have three advan-
tages. First, the exercise price and expiration date of the contract are 
standardized. Second, as in the case of futures contracts, the direct link 
between buyer and seller is severed after the order is executed because 
of the interchangeability of exchange-traded options. The clearinghouse 
associated with the exchange where the option trades performs the same 
function in the options market that it does in the futures market. 
Finally, the transaction costs are lower for exchange-traded options 
than for OTC options. The higher cost of an OTC option reflects the 
cost of customizing the option for the many situations where an institu-
tional investor needs to have a tailor-made option because the standard-
ized exchange-traded option does not satisfy its investment objectives. 
Some commercial and investment and banking firms act as principals as 
well as brokers in the OTC options market. OTC options are sometimes 
referred to as dealer options. 
OTC options can be customized in any manner sought by an institu-
tional investor. Basically, if a dealer can reasonably hedge the risk asso-
ciated with the opposite side of the option sought, it will create the 
option desired by a customer. OTC options are not limited to European 
or American type expiration designs. An option can be created in which 
the option can be exercised at several specified dates as well as the expi-
ration date of the option. Such options are referred to as limited exer-
cise options, Bermuda options, and Atlantic options. 

66 
The Mathematics of Financial Modeling and Investment Management 
Risk-Return for Options 
The maximum amount that an option buyer can lose is the option price. 
The maximum profit that the option writer can realize is the option 
price. The option buyer has substantial upside return potential, while 
the option writer has substantial downside risk. 
Notice that, unlike in a futures contract, one party to an option con-
tract is not obligated to transact—specifically, the option buyer has the 
right but not the obligation to transact. The option writer does have the 
obligation to perform. In the case of a futures contract, both buyer and 
seller are obligated to perform. Of course, a futures buyer does not pay 
the seller to accept the obligation, while an option buyer pays the seller 
an option price. 
Consequently, the risk/reward characteristics of the two contracts are 
also different. In the case of a futures contract, the buyer of the contract 
realizes a dollar-for-dollar gain when the price of the futures contract 
increases and suffers a dollar-for-dollar loss when the price of the futures 
contract drops. The opposite occurs for the seller of a futures contract. 
Options do not provide this symmetric risk/reward relationship. The most 
that the buyer of an option can lose is the option price. While the buyer of 
an option retains all the potential benefits, the gain is always reduced by the 
amount of the option price. The maximum profit that the writer may real-
ize is the option price; this is offset against substantial downside risk. This 
difference is extremely important because investors can use futures to pro-
tect against symmetric risk and options to protect against asymmetric risk. 
The Option Price 
Determining the value of an option is not as simple as the value of a 
futures contract. In Chapter 15 we will present a model employing sto-
chastic calculus and arbitrage arguments to determine the theoretical 
price of an option. In this section we simply present the factors that 
affect the valuation of an option. 
Basic Components of the Option Price 
The option price is a reflection of the option’s intrinsic value and any 
additional amount over its intrinsic value. The premium over intrinsic 
value is often referred to as the time premium. 
The intrinsic value of an option is the economic value of the option 
if it is exercised immediately, except that if there is no positive economic 
value that will result from exercising immediately then the intrinsic 
value is zero. The intrinsic value of a call option is the difference 
between the current price of the underlying asset and the strike price if 
positive; it is otherwise zero. For example, if the strike price for a call 

67 
Overview of Financial Markets, Financial Assets, and Market Participants 
option is $100 and the current asset price is $105, the intrinsic value is 
$5. That is, an option buyer exercising the option and simultaneously 
selling the underlying asset would realize $105 from the sale of the 
asset, which would be covered by acquiring the asset from the option 
writer for $100, thereby netting a $5 gain. 
When an option has intrinsic value, it is said to be “in the money.” 
When the strike price of a call option exceeds the current asset price, the 
call option is said to be “out of the money”; it has no intrinsic value. An 
option for which the strike price is equal to the current asset price is 
said to be “at the money.” Both at-the-money and out-of-the-money 
options have an intrinsic value of zero because it is not profitable to 
exercise the option. Our call option with a strike price of $100 would 
be: (1) in the money when the current asset price is greater than $100; 
(2) out of the money when the current asset price is less than $100; and
(3) at the money when the current asset price is equal to $100.
For a put option, the intrinsic value is equal to the amount by which 
the current asset price is below the strike price. For example, if the strike 
price of a put option is $100 and the current asset price is $92, the intrin-
sic value is $8. That is, the buyer of the put option who exercises the put 
option and simultaneously sells the underlying asset will net $8 by exer-
cising. The asset will be sold to the writer for $100 and purchased in the 
market for $92. For our put option with a strike price of $100, the option 
would be: (1) in the money when the asset price is less than $100; (2) out 
of the money when the current asset price exceeds the strike price; and (3) 
at the money when the strike price is equal to the asset’s price. 
The time premium of an option is the amount by which the option 
price exceeds its intrinsic value. The option buyer hopes that, at some 
time prior to expiration, changes in the market price of the underlying 
asset will increase the value of the rights conveyed by the option. For 
this prospect, the option buyer is willing to pay a premium above the 
intrinsic value. For example, if the price of a call option with a strike 
price of $100 is $9 when the current asset price is $105, the time pre-
mium of this option is $4 ($9 minus its intrinsic value of $5). Had the 
current asset price been $90 instead of $105, then the time premium of 
this option would be the entire $9 because the option has no intrinsic 
value. Clearly, other things being equal, the time premium of an option 
will increase with the amount of time remaining to expiration. 
There are two ways in which an option buyer may realize the value 
of a position taken in the option. First is to exercise the option. The sec-
ond is by selling the call option for $9. In the first example above, sell-
ing the call is preferable because the exercise of an option will realize a 
gain of only $5—it will cause the immediate loss of any time premium. 
There are circumstances under which an option may be exercised prior 

68 
The Mathematics of Financial Modeling and Investment Management 
to the expiration date; they depend on whether the total proceeds at the 
expiration date would be greater by holding the option or exercising 
and reinvesting any cash proceeds received until the expiration date. 
Factors that Influence the Option Price 
There are six factors that influence the option price: 
1. Current price of the underlying asset. 
2. Strike price. 
3. Time to expiration of the option. 
4. Expected return volatility of the underlying asset over the life of the 
option. 
5. Short-term risk-free interest rate over the life of the option. 
6. Anticipated cash payments on the underlying asset over the life of the 
option. 
The impact of each of these factors may depend on whether the option 
is a call or a put, and whether the option is an American option or a 
European option. A summary of the effect of each factor on put and call 
option prices is presented in Exhibit 2.2. 
Option Pricing Models 
Earlier we illustrated that the theoretical price of a futures contract can 
be determined on the basis of arbitrage arguments. Theoretical bound-
ary conditions for the price of an option also can be derived through 
arbitrage arguments. For example, using arbitrage arguments it can be 
shown that the minimum price for an American call option is its intrin-
sic value; that is: 
EXHIBIT 2.2 
Summary of Factors that Affect the Price of an Option 
Effect of an Increase of Factor on 
Factor 
Call Price 
Put Price 
Current price of underlying asset 
Increase 
Decrease 
Strike price 
Decrease 
Increase 
Time to expiration of option 
Increase 
Increase 
Expected price volatility 
Increase 
Increase 
Short-term interest rate 
Increase 
Decrease 
Anticipated cash payments 
Decrease 
Increase 

69 
Overview of Financial Markets, Financial Assets, and Market Participants 
Call option price = ≥ Max (0, Price of asset – Strike price) 
This expression says that the call option price will be greater than or 
equal to the difference between the price of the underlying asset and the 
strike price (intrinsic value), or zero, whichever is higher. 
The boundary conditions can be “tightened” by using arbitrage argu-
ments coupled with certain assumptions about the cash distribution of the 
asset.10 The extreme case is an option pricing model that uses a set of 
assumptions to derive a single theoretical price, rather than a range. Deriv-
ing a theoretical option price is much more complicated than deriving a 
theoretical futures price, because the option price depends on the expected 
return volatility of the underlying asset over the life of the option. 
Several models have been developed to determine the theoretical 
value of an option. The most popular one was developed by Fischer 
Black and Myron Scholes in 1973 for valuing European call options.11 
Several modifications to their model have followed since then. We shall 
discuss the Black-Scholes model and its assumptions in Chapter 15. 
Basically, the idea behind the arbitrage argument is that if the payoff 
from owning a call option can be replicated by purchasing the asset 
underlying the call option and borrowing funds, the price of the option 
is then (at most) the cost of creating the replicating strategy. 
SWAPS 
A swap is an agreement whereby two parties (called counterparties) 
agree to exchange periodic payments. The dollar amount of the pay-
ments exchanged is based on some predetermined dollar principal, 
which is called the notional principal amount or notional amount. The 
dollar amount each counterparty pays to the other is the agreed-upon 
periodic rate times the notional principal amount. The only dollars that 
are exchanged between the parties are the agreed-upon payments, not 
the notional principal amount. In a swap, there is the risk that one of 
the parties will fail to meet its obligation to make payments (default). 
This is referred to as counterparty risk. 
Swaps are classified based on the characteristics of the swap payments. 
There are four types of swaps: interest rate swaps, interest rate-equity 
swaps, equity swaps, and currency swaps. In an interest rate swap, the 
10 See Chapter 4 in John C. Cox and Mark Rubinstein, Option Markets (Englewood 
Cliffs, N.J.: Prentice Hall, 1985), Chapter 4. 
11 Fischer Black and Myron Scholes, “The Pricing of Corporate Liabilities,” Journal 
of Political Economy (May–June 1973), pp. 637–659. 

70 
The Mathematics of Financial Modeling and Investment Management 
counterparties swap payments in the same currency based on an interest 
rate. For example, one of the counterparties can pay a fixed-interest rate 
and the other party a floating interest rate. The floating-interest rate is 
commonly referred to as the reference rate. In an interest rate-equity swap, 
one party is exchanging a payment based on an interest rate and the other 
party based on the return of some equity index. The payments are made in 
the same currency. In an equity swap, both parties exchange payments in 
the same currency based on some equity index. Finally, in a currency swap, 
two parties agree to swap payments based on different currencies. 
A swap is not a new derivative instrument. Rather, it can be decom-
posed into a package of forward contracts. While a swap may be nothing 
more than a package of forward contracts, it is not a redundant contract 
for several reasons. First, in many markets where there are forward and 
futures contracts, the longest maturity does not extend out as far as that of 
a typical swap. Second, a swap is a more transactionally efficient instru-
ment. By this we mean that in one transaction an entity can effectively 
establish a payoff equivalent to a package of forward contracts. The for-
ward contracts would each have to be negotiated separately. Third, the 
liquidity of some swap markets is now better than many forward con-
tracts, particularly long-dated (i.e., long-term) forward contracts. 
CAPS AND FLOORS 
There are agreements available in the financial market whereby one 
party, for a fee (premium), agrees to compensate the other if a desig-
nated reference is different from a predetermined level. The party that 
will receive payment if the designated reference differs from a predeter-
mined level and pays a premium to enter into the agreement is called the 
buyer. The party that agrees to make the payment if the designated ref-
erence differs from a predetermined level is called the seller. 
When the seller agrees to pay the buyer if the designated reference 
exceeds a predetermined level, the agreement is referred to as a cap. The 
agreement is referred to as a floor when the seller agrees to pay the 
buyer if a designated reference falls below a predetermined level. The 
designated reference could be a specific interest rate such as LIBOR or 
the prime rate, the rate of return on some domestic or foreign stock 
market index such as the S&P 500 or the DAX, or an exchange rate 
such as the exchange rate between the U.S. dollar and the Japanese yen. 
The predetermined level is called the strike. As with a swap, a cap and a 
floor have a notional principal amount. Only the buyer of a cap or a 
floor is exposed to counterparty risk. 

71 
Overview of Financial Markets, Financial Assets, and Market Participants 
In general, the payment made by the seller of the cap to the buyer 
on a specific date is determined by the relationship between the desig-
nated reference and the strike. If the former is greater that the latter, 
then the seller pays the buyer: 
Notional principal amount × [Actual value of designated reference – Strike] 
If the designated reference is less than or equal to the strike, then the 
seller pays the buyer nothing. 
For a floor, the payment made by the seller to the buyer on a specific 
date is determined as follows. If the designated reference is less than the 
strike, then the seller pays the buyer: 
Notional principal amount × [Strike – Actual value of designated reference] 
If the designated reference is greater than or equal to the strike, then the 
seller pays the buyer nothing. 
In a cap or floor, the buyer pays a fee which represents the maxi-
mum amount that the buyer can lose and the maximum amount that the 
seller of the agreement can gain. The only party that is required to per-
form is the seller. The buyer of a cap benefits if the designated reference 
rises above the strike because the seller must compensate the buyer. The 
buyer of a floor benefits if the designated reference falls below the strike 
because the seller must compensate the buyer. 
In essence the payoff of these contracts is the same as that of an 
option. A call option buyer pays a fee and benefits if the value of the 
option’s underlying asset (or equivalently, designated reference) is 
higher than the strike price at the expiration date. A cap has a similar 
payoff. A put option buyer pays a fee and benefits if the value of the 
option’s underlying asset (or equivalently, designated reference) is less 
than the strike price at the expiration date. A floor has a similar payoff. 
An option seller is only entitled to the option price. The seller of a cap 
or floor is only entitled to the fee. Thus, a cap and a floor can be viewed 
as simply a package of options. As with a swap, a complex contract can 
be seen to be a package of basic contracts (forward contracts in the case 
of swaps and options in the case of caps and floors). 
SUMMARY
 ■ The claims of the holder of a financial asset may be either a fixed dollar 
amount (fixed income instrument or bond) or a varying, or residual, 
amount (common stock). 

72 
The Mathematics of Financial Modeling and Investment Management
 ■ The two principal economic functions of financial assets are to (1) 
transfer funds from those parties who have surplus funds to invest to 
those who need funds to invest in tangible assets; and (2) transfer funds 
in such a way as to redistribute the unavoidable risk associated with 
the cash flow generated by tangible assets among those seeking and 
those providing the funds. 
■ Financial assets possess the following properties that determine or 
influence their attractiveness to different classes of investors: (1) mon-
eyness; (2) divisibility and denomination; (3) reversibility; (4) term to 
maturity; (5) liquidity; (6) convertibility; (7) currency; (8) cash flow 
and return predictability; and (9) tax status.
 ■ There are five ways to classify financial markets: (1) nature of the 
claim; (2) maturity of the claims; (3) new versus seasoned claims; (4) 
cash versus derivative instruments; and (5) organizational structure of 
the market.
 ■ Financial markets provide the following economic functions: (1) They 
signal how the funds in the economy should be allocated among finan-
cial assets (i.e., price discovery); (2) they provide a mechanism for an 
investor to sell a financial asset (i.e., provide liquidity); and (3) they 
reduce search and information costs of transacting.
 ■ Pricing efficiency refers to a market where prices at all times fully 
reflect all available information that is relevant to the valuation of 
securities.
 ■ Financial intermediaries obtain funds by issuing financial claims 
against themselves to market participants, then investing those funds. 
■ Asset managers manage funds to meet specified investment objectives— 
either based on a market benchmark or based on liabilities.
 ■ Common stocks, also called equity securities, represent an ownership 
interest in a corporation; holders of this types of security are entitled to 
the earnings of the corporation when those earnings are distributed in 
the form of dividends.
 ■ A bond is a financial obligation of an entity that promises to pay a 
specified sum of money at specified future dates; a bond may include a 
provision that grants the issuer or the investor an option to alter the 
effective maturity.
 ■ A futures contract and forward contract are agreements that require a 
party to the agreement either to buy or sell the underlying at a desig-
nated future date at a predetermined price.
 ■ Futures contracts are standardized agreements as to the delivery date 
and quality of the deliverable, and are traded on organized exchanges; 
a forward contract differs in that it is usually nonstandardized, there is 
no clearinghouse (and therefore counterparty risk), and secondary 
markets are often nonexistent or extremely thin. 

73
Overview of Financial Markets, Financial Assets, and Market Participants 
■ An option is a contract in which the writer of the option grants the 
buyer of the option the right, but not the obligation, to purchase from 
the writer (a call option) or sell to the writer (a put option) the underly-
ing at the strike (or exercise) price within a specified period of time (or 
at a specified date); the option price is a reflection of the option’s intrin-
sic value and any additional amount over its intrinsic value. 
■ A swap is an agreement whereby the counterparties agree to exchange 
periodic payments; the dollar amount of the payments exchanged is 
based on a notional amount.
 ■ A cap and a floor are agreements whereby one party, for a fee (pre-
mium), agrees to compensate the other if a designated reference is dif-
ferent from a predetermined level. 



## Milestones in Financial Modeling

CHAPTER 3 
Milestones in Financial Modeling 
and Investment Management 
T
he mathematical development of present-day economic and finance 
theory began in Lausanne, Switzerland at the end of the nineteenth 
century, with the development of the mathematical equilibrium theory by 
Leon Walras and Wilfredo Pareto.1 Shortly thereafter, at the beginning of 
the twentieth century, Louis Bachelier in Paris and Filip Lundberg in Upp-
sala (Sweden) made two seminal contributions: they developed sophisti-
cated mathematical tools to describe uncertain price and risk processes. 
These developments were well in advance of their time. Further 
progress was to be made only much later in the twentieth century, thanks 
to the development of digital computers. By making it possible to com-
pute approximate solutions to complex problems, digital computers 
enabled the large-scale application of mathematics to business problems. 
A first round of innovation occurred in the 1950s and 1960s. Ken-
neth Arrow and Georges Debreu introduced a probabilistic model of 
markets and the notion of contingent claims. (We discuss their contribu-
tions in Chapter 6.) In 1952, Harry Markowitz described mathemati-
cally the principles of the investment process in terms of utility 
optimization. In 1961, Franco Modigliani and Merton Miller clarified 
the nature of economic value, working out the implications of absence 
of arbitrage. Between 1964 and 1966, William Sharpe, John Lintner, 
1 References for some of the works cited in this chapter will be provided in later chap-
ters in this book. For an engaging description of the history of capital markets see 
Peter L. Bernstein, Capital Ideas (New York: The Free Press, 1992). For a history of 
the role of risk in business and investment management, see Peter L. Bernstein, 
Against the Gods (New York: John Wiley & Sons, 1996). 
75 

76 
The Mathematics of Financial Modeling and Investment Management 
and Jan Mossin developed a theoretical model of market prices based 
on the principles of financial decision-making laid down by Markowitz. 
The notion of efficient markets was introduced by Paul Samuelson in 
1965, and five years later, further developed by Eugene Fama. 
The second round of innovation started at the end of the 1970s. In 
1973, Fischer Black, Myron Scholes, and Robert Merton discovered how to 
determine option prices using continuous hedging. Three years later, 
Stephen Ross introduced arbitrage pricing theory (APT). Both were major 
developments that were to result in a comprehensive mathematical method-
ology for investment management and the valuation of derivative financial 
products. At about the same time, Merton introduced a continuous-time 
intertemporal, dynamic optimization model of asset allocation. Major 
refinements in the methodology of mathematical optimization and new 
econometric tools were to change the way investments are managed. 
More recently, the diffusion of electronic transactions has made 
available a huge amount of empirical data. The availability of this data 
created the hope that economics could be given a more solid scientific 
grounding. A new field—econophysics—opened with the expectation 
that the proven methods of the physical sciences and the newly born sci-
ence of complex systems could be applied with benefit to economics. It 
was hypothesized that economic systems could be studied as physical 
systems with only minimal a priori economic assumptions. Classical 
econometrics is based on a similar approach; but while the scope of 
classical econometrics is limited to dynamic models of time series, 
econophysics uses all the tools of statistical physics and complex sys-
tems analysis, including the theory of interacting multiagent systems. 
THE PRECURSORS: PARETO, WALRAS, AND THE 
LAUSANNE SCHOOL 
The idea of formulating quantitative laws of economic behavior in ways 
similar to the physical sciences started in earnest at the end of the nineteenth 
century. Though quite accurate economic accounting on a large scale dates 
back to Assyro-Babylonian times, a scientific approach to economics is a 
recent endeavor. 
Leon Walras and Wilfredo Pareto, founders of the so-called Lausanne 
School at the University of Lausanne in Switzerland, were among the first 
to explicitly formulate quantitative principles of market economies, stating 
the principle of economic equilibrium as a mathematical theory. Both 
worked at a time of great social and economic change. In Pareto’s work in 
particular, pure economics and political science occupy a central place. 

77 
Milestones in Financial Modeling and Investment Management 
Convinced that economics should become a mathematical science, 
Walras set himself the task of writing the first mathematical general 
equilibrium system. The British economist Stanley Jevons and the Aus-
trian economist Carl Menger had already formulated the idea of eco-
nomic equilibrium as a situation where supply and demand match in 
interrelated markets. Walras’s objective—to prove that equilibrium was 
indeed possible—required the explicit formulation of the equations of 
supply-and-demand equilibrium. 
Walras introduced the idea of tatonemment (French for groping) as a 
process of exploration by which a central auctioneer determines equilib-
rium prices. A century before, in 1776, in his book An Inquiry into the 
Nature and Causes of the Wealth of Nations, Adam Smith had introduced 
the notion of the “invisible hand” that coordinates the activity of inde-
pendent competitive agents to achieve desirable global goals.2 Walras was 
to make the hand “visible” by defining the process of price discovery. 
Pareto followed Walras in the Chair of Economics at the University of 
Lausanne. Pareto’s focus was the process of economic decision-making. He 
replaced the idea of supply-and-demand equilibrium with a more general 
idea of the ordering of preferences through utility functions.3 Equilibrium 
is reached where marginal utilities are zero. The Pareto system hypothe-
sized that agents are able to order their preferences and take into account 
constraints in such a way that a numerical index—“utility” in today’s ter-
minology—can be associated to each choice.4 Economic decision-making 
is therefore based on the maximization of utility. As Pareto assumed utility 
to be a differentiable function, global equilibrium is reached where mar-
ginal utilities (i.e., the partial derivatives of utility) vanish. 
Pareto was especially interested in the problem of the global opti-
mum of utility. The Pareto optimum is a state in which nobody can be 
better off without making others worse off. A Pareto optimum does not 
imply the equal division of resources; quite the contrary, a Pareto opti-
mum might be a maximally unequal distribution of wealth. 
2 In the modern parlance of complex systems, the “invisible hand” would be called 
an “emerging property” of competitive markets. Much recent work on complex sys-
tems and artificial life has focused on understanding how the local interaction of in-
dividuals might result in complex and purposeful global behavior. 
3 Pareto used the word “ophelimity” to designate what we would now call utility. 
The concept of ophelimity is slightly different from the concept of utility insofar as 
ophelimity includes constraints on people’s preferences. 
4 It was not until 1944 that utility theory was formalized in a set of necessary and 
sufficient axioms by von Neumann and Morgenstern and applied to decision-making 
under risk and uncertainty. See John von Neumann and Oskar Morgenstern, Theory 
of Games and Economic Behavior (Princeton, NJ: Princeton University Press, 
1944). 

78 
The Mathematics of Financial Modeling and Investment Management 
A lasting contribution of Pareto is the formulation of a law of 
income distribution. Known as the Pareto law, this law states that there 
is a linear relationship between the logarithm of the income I and the 
number N of people that earn more than this income: 
Log N = A + s log I 
where A and s are appropriate constants. 
The importance of the works of Walras and Pareto were not appre-
ciated at the time. Without digital computers, the equilibrium systems 
they conceived were purely abstract: There was no way to compute 
solutions to economic equilibrium problems. In addition, the climate at 
the turn of the century did not allow a serene evaluation of the scientific 
merit of their work. The idea of free markets was at the center of heated 
political debates; competing systems included mercantile economies 
based on trade restrictions and privileges as well as the emerging cen-
trally planned Marxist economies. 
PRICE DIFFUSION: BACHELIER 
In 1900, the Sorbonne University student Louis Bachelier presented a 
doctoral dissertation, Théorie de la Spéculation, that was to anticipate 
much of today’s work in finance theory. Bachelier’s advisor was the 
great French mathematician Henri Poincaré. There were three notable 
aspects in Bachelier’s thesis:
 ■ He argued that in a purely speculative market stock prices should be 
random.
 ■ He developed the mathematics of Brownian motion.
 ■ He computed the prices of several options. 
To appreciate the importance of Bachelier’s work, it should be 
remarked that at the beginning of the 20th century, the notion of proba-
bility was not yet rigorous; the formal mathematical theory of probabil-
ity was developed only in the 1930s (see Chapter 6). In particular, the 
precise notion of the propagation of information essential for the defini-
tion of conditional probabilities in continuous time had not yet been 
formulated. 
Anticipating the development of the theory of efficient markets 60 
years later, the key economic idea of Bachelier was that asset prices in a 
speculative market should be a fair game, that is, a martingale process 
such that the expected return is zero (see Chapter 15). According to Bach-

79 
Milestones in Financial Modeling and Investment Management 
elier, “The expectation of the speculator is zero.” The formal concept of a 
martingale (i.e., of a process such that its expected value at any moment 
coincides with the present value) had not yet been introduced in probabil-
ity theory. In fact, the rigorous notion of conditional probability and fil-
tration (see Chapter 6) were developed only in the 1930s. In formulating 
his hypothesis on market behavior, Bachelier relied on intuition. 
Bachelier actually went much further. He assumed that stock prices 
evolve as a continuous-time Markov process. This was a brilliant intu-
ition: Markov was to start working on these problems only in 1906. 
Bachelier established the differential equation for the time evolution of 
the probability distribution of prices, noting that this equation was the 
same as the heat diffusion equation. Five years later, in 1905, Albert 
Einstein used the same diffusion equation for the Brownian motion (i.e., 
the motion of a small particle suspended in a fluid). Bachelier also made 
the connection with the continuous limit of random walks, thus antici-
pating the work of the Japanese mathematician Kiyosi Itô at the end of 
the 1940s and the Russian mathematician and physicist Ruslan L. Stra-
tonovich on stochastic integrals at the end of the 1950s. 
By computing the extremes of Brownian motion, Bachelier computed 
the price of several options. He also computed the distributions of a 
number of functionals of Brownian motion. These were remarkable 
mathematical results in themselves. Formal proof was given only much 
later. Even more remarkable, Bachelier established option pricing formu-
las well before the formal notion of absence of arbitrage was formulated. 
Though the work of Bachelier was correctly assessed by his advisor 
Poincaré, it did not bring him much recognition at the time. Bachelier 
succeeded in getting several books on probability theory published, but 
his academic career was not very successful. He was offered only minor 
positions in provincial towns and suffered a major blow when in 1926, 
at the age of 56, he was refused a permanent chair at the University of 
Dijon under the pretext (false) that his 1900 thesis contained an error.5 
Bachelier’s work was outside the mainstream of contemporary 
mathematics but was too mathematically complex for the economists of 
his time. It wasn’t until the formal development of probability theory in 
1930s that his ideas became mainstream mathematics and only in the 
1960s, with the development of the theory of efficient markets, that his 
ideas became part of mainstream finance theory. In an efficient market, 
asset prices should, in each instant, reflect all the information available 
at the time, and any event that causes prices to move must be unex-
5 The famous mathematician Paul Levy who, apparently in bona fide, initially en-
dorsed the claim that Bachelier’s thesis contained an error, later wrote a letter of 
apology to Bachelier. 

80 
The Mathematics of Financial Modeling and Investment Management 
pected (i.e., a random disturbance). As a consequence, prices move as 
martingales, as argued by Bachelier. Bachelier was, in fact, the first to 
give a precise mathematical structure in continuous time to price pro-
cesses subject to competitive pressure by many agents. 
THE RUIN PROBLEM IN INSURANCE: LUNDBERG 
In Uppsala, Sweden, in 1903, three years after Bachelier defended his 
doctoral dissertation in Paris, Filip Lundberg defended a thesis that was 
to become a milestone in actuarial mathematics: He was the first to 
define a collective theory of risk and to apply a sophisticated probabilis-
tic formulation to the insurance ruin problem. The ruin problem of an 
insurance company in a nonlife sector can be defined as follows. Sup-
pose that an insurance company receives a stream of sure payments 
(premiums) and is subject to claims of random size that occur at random 
times. What is the probability that the insurer will not be able to meet 
its obligations (i.e., the probability of ruin)? 
Lundberg solved the problem as a collective risk problem, pooling 
together the risk of claims. To define collective risk processes, he intro-
duced marked Poisson processes. Marked Poisson processes are pro-
cesses where the random time between two events is exponentially 
distributed. The magnitude of events is random with a distribution inde-
pendent of the time of the event. Based on this representation, Lundberg 
computed an estimate of the probability of ruin. 
Lundberg’s work anticipated many future developments of probability 
theory, including what was later to be known as the theory of point pro-
cesses. In the 1930s, the Swedish mathematician and probabilist Harald 
Cramer gave a rigorous mathematical formulation to Lundberg’s work. A 
more comprehensive formal theory of insurance risk was later developed. 
This theory now includes Cox processes—point processes more general 
than Poisson processes—and fat-tailed distributions of claim size. 
A strong connection between actuarial mathematics and asset pric-
ing theory has since been established.6 In well-behaved, complete mar-
kets (see Chapter 23), establishing insurance premiums entails principles 
that mirror asset prices. In the presence of complete markets, insurance 
would be a risk-free business: There is always the possibility of reinsur-
ance. In markets that are not complete—essentially because they make 
unpredictable jumps—hedging is not possible; risk can only be diversi-
6 Paul Embrechts, Claudia Klüppelberg, and Thomas Mikosch, Modelling Extremal 
Events for Insurance and Finance (Berlin: Springer, 1996). 

81 
Milestones in Financial Modeling and Investment Management 
fied and options are inherently risky. Option pricing theory again mir-
rors the setting of insurance premiums. 
Lundberg’s work went unnoticed by the actuarial community for 
nearly 30 years, though this did not stop him from enjoying a successful 
career as an insurer. Both Bachelier and Lundberg were in advance of 
their time; they anticipated, and probably inspired, the subsequent 
development of probability theory. But the type of mathematics implied 
by their work could not be employed in full earnest prior to the devel-
opment of digital computers. It was only with digital computers that we 
were able to tackle complex mathematical problems whose solutions go 
beyond closed-form formulas. 
THE PRINCIPLES OF INVESTMENT: MARKOWITZ 
Just how an investor should allocate his resources has long been 
debated. Classical wisdom suggested that investments should be allo-
cated to those assets yielding the highest returns, without the consider-
ation of correlations. Before the modern formulation of efficient 
markets, speculators widely acted on the belief that positions should be 
taken only if they had a competitive advantage in terms of information. 
A large amount of resources were therefore spent on analyzing financial 
information. John Maynard Keynes suggested that investors should 
carefully evaluate all available information and then make a calculated 
bet. The idea of diversification was anathema to Keynes, who was actu-
ally quite a successful investor. 
In 1952, Harry Markowitz, then a graduate student at the University 
of Chicago, and a student member of the Cowles Commission,7 published a 
seminal article on optimal portfolio selection that upset established wis-
dom. He advocated that, being risk adverse, investors should diversify their 
portfolios.8 The idea of making risk bearable through risk diversification 
was not new: It was widely used by medieval merchants. Markowitz under-
stood that the risk-return trade-off of investments could be improved by 
diversification and cast diversification in the framework of optimization. 
7 The Cowles Commission is a research institute founded by Alfred Cowles in 1932. 
Originally based in Colorado Springs, the Commission later moved to the University 
of Chicago and thereafter to Yale University. Many prominent American economists 
have been associated with the Commission. 
8 See Harry M. Markowitz, “Portfolio Selection,” Journal of Finance (March 1952), 
pp. 77–91. The principles in Markowitz’s article were then expanded in his book 
Portfolio Selection, Cowles Foundation Monograph 16 (New York: John Wiley, 
1959). 

82 
The Mathematics of Financial Modeling and Investment Management 
Markowitz was interested in the investment decision-making pro-
cess. Along the lines set forth by Pareto 60 years earlier, Markowitz 
assumed that investors order their preferences according to a utility 
index, with utility as a convex function that takes into account inves-
tors’ risk-return preferences. Markowitz assumed that stock returns are 
jointly normal. As a consequence, the return of any portfolio is a nor-
mal distribution, which can be characterized by two parameters: the 
mean and the variance. Utility functions are therefore defined on two 
variables—mean and variance—and the Markowitz framework for 
portfolio selection is commonly referred to as mean-variance analysis. 
The mean and variance of portfolio returns are in turn a function of a 
portfolio’s weights. Given the variance-covariance matrix, utility is a 
function of portfolio weights. The investment decision-making process 
involves maximizing utility in the space of portfolio weights. 
After writing his seminal article, Markowitz joined the Rand Corpo-
ration, where he met George Dantzig. Dantzig introduced Markowitz to 
computer-based optimization technology.9 The latter was quick to appre-
ciate the role that computers would have in bringing mathematics to bear 
on business problems. Optimization and simulation were on the way to 
becoming the tools of the future, replacing the quest for closed-form solu-
tions of mathematical problems. 
In the following years, Markowitz developed a full theory of the invest-
ment management process based on optimization. His optimization theory 
had the merit of being applicable to practical problems, even outside of the 
realm of finance. With the progressive diffusion of high-speed computers, 
the practice of financial optimization has found broad application.10 
9 The inputs to the mean-variance analysis include expected returns, variance of re-
turns, and either covariance or correlation of returns between each pair of securities. 
For example, an analysis that allows 200 securities as possible candidates for port-
folio selection requires 200 expected returns, 200 variances of return, and 19,900 
correlations or covariances. An investment team tracking 200 securities may reason-
ably be expected to summarize their analyses in terms of 200 means and variances, 
but it is clearly unreasonable for them to produce 19,900 carefully considered corre-
lation coefficients or covariances. It was clear to Markowitz that some kind of model 
of the covariance structure was needed for the practical application of the model. He 
did little more than point out the problem and suggest some possible models of co-
variance for research to large portfolios. In 1963, William Sharpe suggested the sin-
gle index market model as a proxy for the covariance structure of security returns 
(“A Simplified Model for Portfolio Analysis,” Management Science (January 1963), 
pp. 277–293). 
10 In Chapter 16 we illustrate one application. For a more detailed discussion, see 
Frank J. Fabozzi, Francis Gupta, and Harry M. Markowitz, “The Legacy of Modern 
Portfolio Theory,” Journal of Investing (Summer 2002), pp. 7–22. 

83 
Milestones in Financial Modeling and Investment Management 
UNDERSTANDING VALUE: MODIGLIANI AND MILLER 
At about the same time that Markowitz was tackling the problem of 
how investors should behave, taking asset price processes as a given, 
other economists were trying to understand how markets determine 
value. Adam Smith had introduced the notion of perfect competition 
(and therefore perfect markets) in the second half of the eighteenth cen-
tury. In a perfect market, there are no impediments to trading: Agents 
are price takers who can buy or sell as many units as they wish. The 
neoclassical economists of the 1960s took the idea of perfect markets as 
a useful idealization of real free markets. In particular, they argued that 
financial markets are very close to being perfect markets. The theory of 
asset pricing was subsequently developed to explain how prices are set 
in a perfect market. 
In general, a perfect market results when the number of buyers and 
sellers is sufficiently large, and all participants are small enough relative 
to the market so that no individual market agent can influence a com-
modity’s price. Consequently, all buyers and sellers are price takers, and 
the market price is determined where there is equality of supply and 
demand. This condition is more likely to be satisfied if the commodity 
traded is fairly homogeneous (for example, corn or wheat). 
There is more to a perfect market than market agents being price 
takers. It is also required that there are no transaction costs or impedi-
ments that interfere with the supply and demand of the commodity. 
Economists refer to these various costs and impediments as “frictions.” 
The costs associated with frictions generally result in buyers paying 
more than in the absence of frictions, and/or sellers receiving less. In the 
case of financial markets, frictions include: 
■ Commissions charged by brokers.
 ■ Bid-ask spreads charged by dealers.
 ■ Order handling and clearance charges.
 ■ Taxes (notably on capital gains) and government-imposed transfer fees.
 ■ Costs of acquiring information about the financial asset.
 ■ Trading restrictions, such as exchange-imposed restrictions on the size 
of a position in the financial asset that a buyer or seller may take.
 ■ Restrictions on market makers.
 ■ Halts to trading that may be imposed by regulators where the financial 
asset is traded. 

84 
The Mathematics of Financial Modeling and Investment Management 
Modigliani-Miller Irrelevance Theorems and the 
Absence of Arbitrage 
A major step was taken in 1958 when Franco Modigliani and Merton 
Miller published a then-controversial article in which they maintained 
that the value of a company does not depend on the capital structure of 
the firm.11 (The capital structure of a firm is the mix of debt and equity.) 
The traditional view prior to the publication of the article by 
Modigliani and Miller was that there existed a capital structure that 
maximized the value of the firm (i.e., there is an optimal capital struc-
ture). Modigliani and Miller demonstrated that in the absence of taxes 
and in a perfect capital market, the capital structure was irrelevant (i.e., 
the capital structure does not affect the value of a firm).12 
In 1961, Modigliani and Miller published yet another controversial 
article where they argued that the value of a company does not depend 
on the dividends it pays but on its earnings.13 The basis for valuing a 
firm—earnings or dividends—had always attracted considerable atten-
tion. Because dividends provide the hard cash which remunerates inves-
tors, they were considered by many as key to a firm’s value. 
Modigliani and Miller’s challenge to the traditional view that capi-
tal structure and dividends matter when determining a firm’s value was 
founded on the principle that the traditional views were inconsistent 
with the workings of competitive markets where securities are freely 
traded. In their view, the value of a company is independent of its finan-
cial structure: from a valuation standpoint, it does not matter whether 
the firm keeps its earnings or distributes them to shareholders. 
Known as the Modigliani-Miller theorems, these theorems paved the 
way for the development of arbitrage pricing theory. In fact, to establish 
their theorems, Modigliani and Miller made use of the notion of absence 
of arbitrage. Absence of arbitrage means that there is no possibility of 
making a risk-free profit without an investment. This implies that the 
same stream of cash flows should be priced in the same way across dif-
11 Franco Modigliani and Merton H. Miller, “The Cost of Capital, Corporation Fi-
nance, and the Theory of Investment,” American Economic Review (June 1958), 
pp. 261–297. In a later article, they corrected their analysis for the impact of corpo-
rate taxes: Franco Modigliani and Merton H. Miller, “Corporate Income Taxes and 
the Cost of Capital: A Correction,” American Economic Review (June 1963), pp. 
433–443. 
12 By extension, the irrelevance principle applies to the type of debt a firm may select 
(e.g., senior, subordinated, secured, and unsecured). 
13 Merton H. Miller and Franco Modigliani, “Dividend Policy, Growth, and the Val-
uation of Shares,” Journal of Business (October 1961), pp. 411–433. 

85 
Milestones in Financial Modeling and Investment Management 
ferent markets. Absence of arbitrage is the fundamental principle for rel-
ative asset pricing; it is the pillar on which derivative pricing rests. 
EFFICIENT MARKETS: FAMA AND SAMUELSON 
Absence of arbitrage entails market efficiency. Shortly after the Modigliani-
Miller theorems had been established, Paul Samuelson in 196514 and 
Eugene Fama in 197015 developed the notion of efficient markets: A 
market is efficient if prices reflect all available information. Bachelier 
had argued that prices in a competitive market should be random condi-
tionally to the present state of affairs. Fama and Samuelson put this 
concept into a theoretical framework, linking prices to information. 
As explained in the previous chapter, in general, an efficient market 
refers to a market where prices at all times fully reflect all available infor-
mation that is relevant to the valuation of securities. That is, relevant infor-
mation about the security is quickly impounded into the price of securities. 
Fama and Samuelson define “fully reflects” in terms of the expected 
return from holding a security. The expected return over some holding 
period is equal to expected cash distributions plus the expected price 
change, all divided by the initial price. The price formation process 
defined by Fama and Samuelson is that the expected return one period 
from now is a stochastic variable that already takes into account the “rel-
evant” information set. They argued that in a market where information 
is shared by all market participants, prices should fluctuate randomly. 
A price-efficient market has implications for the investment strategy 
that investors may wish to pursue. In an active strategy, investors seek 
to capitalize on what they perceive to be the mispricing of financial 
instruments (cash instruments or derivative instruments). In a market 
that is price efficient, active strategies will not consistently generate a 
return after taking into consideration transaction costs and the risks 
associated with a strategy that is greater than simply buying and hold-
ing securities. This has lead investors in certain sectors of the capital 
market where empirical evidence suggests the sector is price efficient to 
pursue a strategy of indexing, which simply seeks to match the perfor-
mance of some financial index. However Samuelson was careful to 
remark that the notion of efficient markets does not make investment 
analysis useless; rather, it is a condition for efficient markets. 
14 Paul A. Samuelson, “Proof the Properly Anticipated Prices Fluctuate Randomly,” 
Industrial Management Review (Spring 1965), pp. 41–50. 
15 Eugene F. Fama, “The Behavior of Stock Market Prices,” Journal of Business (Jan -
uary 1965), pp. 34–105. 

86 
The Mathematics of Financial Modeling and Investment Management 
Another facet in this apparent contradiction of the pursuit of active 
strategies despite empirical evidence on market efficiency was soon to be 
clarified. Agents optimize a risk-return trade-off based on the stochastic 
features of price processes. Price processes are not simply random but 
exhibit a rich stochastic behavior. The objective of investment analysis 
is to reveal this behavior (see Chapters 16 and 19). 
CAPITAL ASSET PRICING MODEL: SHARPE, LINTNER, AND 
MOSSIN 
Absence of arbitrage is a powerful economic principle for establishing 
relative pricing. In itself, however, it is not a market equilibrium model. 
William Sharpe (in 1964),16 John Lintner (in 1965),17 and Jan Mossin 
(in 1966),18 developed a theoretical equilibrium model of market prices 
called the Capital Asset Pricing Model (CAPM). As anticipated 60 years 
earlier by Walras and Pareto, Sharpe, Lintner, and Mossin developed the 
consequences of Markowitz’s portfolio selection into a full-fledged sto-
chastic general equilibrium theory. 
Asset pricing models categorize risk factors into two types. The first 
type is risk factors that cannot be diversified away via the Markowitz 
framework. That is, no matter what the investor does, the investor can-
not eliminate these risk factors. These risk factors are referred to as sys-
tematic risk factors or nondiversifiable risk factors. The second type is 
risk factors that can be eliminated via diversification. These risk factors 
are unique to the asset and are referred to as unsystematic risk factors 
or diversifiable risk factors. 
The CAPM has only one systematic risk factor—the risk of the over-
all movement of the market. This risk factor is referred to as “market 
risk.” This is the risk associated with holding a portfolio consisting of 
all assets, called the “market portfolio.” In the market portfolio, an 
asset is held in proportion to its market value. So, for example, if the 
total market value of all assets is $X and the market value of asset j is 
$Y, then asset j will comprise $Y/$X of the market portfolio. 
16 William F. Sharpe, “Capital Asset Prices,” Journal of Finance (September 1964), 
pp. 425–442. 
17 John Lintner, “The Valuation of Risk Assets and the Selection of Risky Invest -
ments in Stock Portfolio and Capital Budgets,” Review of Economics and Statistics 
(February 1965), pp. 13–37. 
18 Jan Mossin, “Equilibrium in a Capital Asset Market,” Econometrica (October 
1966), pp. 768–783. 

87 
Milestones in Financial Modeling and Investment Management 
The expected return for an asset i according to the CAPM is equal to 
the risk-free rate plus a risk premium. The risk premium is the product of 
(1) the sensitivity of the return of asset i to the return of the market port-
folio and (2) the difference between the expected return on the market 
portfolio and the risk-free rate. It measures the potential reward for tak-
ing on the risk of the market above what can be earned by investing in an 
asset that offers a risk-free rate. Taken together, the risk premium is a 
product of the quantity of market risk and the potential compensation of 
taking on market risk (as measured by the second component). 
The CAPM was highly appealing from the theoretical point of view. 
It was the first general-equilibrium model of a market that admitted 
testing with econometric tools. A critical challenge to the empirical test-
ing of the CAPM is the identification of the market portfolio.19 
THE MULTIFACTOR CAPM: MERTON 
The CAPM assumes that the only risk that an investor is concerned with 
is uncertainty about the future price of a security. Investors, however, 
are usually concerned with other risks that will affect their ability to 
consume goods and services in the future. Three examples would be the 
risks associated with future labor income, the future relative prices of 
consumer goods, and future investment opportunities. 
Recognizing these other risks that investors face, in 1976 Robert 
Merton extended the CAPM based on consumers deriving their optimal 
lifetime consumption when they face these “extra-market” sources of 
risk.20 These extra-market sources of risk are also referred to as “fac-
tors,” hence the model derived by Merton is called a multifactor CAPM. 
The multifactor CAPM says that investors want to be compensated 
for the risk associated with each source of extra-market risk, in addition 
to market risk. In the case of the CAPM, investors hedge the uncertainty 
associated with future security prices by diversifying. This is done by 
holding the market portfolio. In the multifactor CAPM, in addition to 
investing in the market portfolio, investors will also allocate funds to 
something equivalent to a mutual fund that hedges a particular extra-
market risk. While not all investors are concerned with the same sources 
of extra-market risk, those that are concerned with a specific extra-mar-
ket risk will basically hedge them in the same way. 
19 Richard R. Roll, “A Critique of the Asset Pricing Theory’s Tests,” Journal of Fi-
nancial Economics (March 1977), pp. 129–176. 
20 Robert C. Merton, “An Intertemporal Capital Asset Pricing Model,” Econometri-
ca (September 1973), pp. 867–888. 

88 
The Mathematics of Financial Modeling and Investment Management 
The multifactor CAPM is an attractive model because it recognizes 
nonmarket risks. The pricing of an asset by the marketplace, then, must 
reflect risk premiums to compensate for these extra-market risks. Unfor-
tunately, it may be difficult to identify all the extra-market risks and to 
value each of these risks empirically. Furthermore, when these risks are 
taken together, the multifactor CAPM begins to resemble the arbitrage 
pricing theory model described next. 
ARBITRAGE PRICING THEORY: ROSS 
An alternative to the equilibrium asset pricing model just discussed, an 
asset pricing model based purely on arbitrage arguments, was derived 
by Stephen Ross.21 The model, called the Arbitrage Pricing Theory 
(APT) Model, postulates that an asset’s expected return is influenced by 
a variety of risk factors, as opposed to just market risk as assumed by 
the CAPM. The APT model states that the return on a security is lin-
early related to H systematic risk factors. However, the APT model does 
not specify what the systematic risk factors are, but it is assumed that 
the relationship between asset returns and the risk factors is linear. 
The APT model as given asserts that investors want to be compen-
sated for all the risk factors that systematically affect the return of a secu-
rity. The compensation is the sum of the products of each risk factor’s 
systematic risk and the risk premium assigned to it by the capital market. 
Proponents of the APT model argue that it has several major advan-
tages over the CAPM. First, it makes less restrictive assumptions about 
investor preferences toward risk and return. As explained earlier, the 
CAPM theory assumes investors trade off between risk and return solely 
on the basis of the expected returns and standard deviations of prospec-
tive investments. The APT model, in contrast, simply requires that some 
rather unobtrusive bounds be placed on potential investor utility func-
tions. Second, no assumptions are made about the distribution of asset 
returns. Finally, since the APT model does not rely on the identification 
of the true market portfolio, the theory is potentially testable. The 
model simply assumes that no arbitrage is possible. That is, using no 
additional funds (wealth) and without increasing risk, it is not possible 
for an investor to create a portfolio to increase return. 
The APT model provides theoretical support for an asset pricing 
model where there is more than one risk factor. Consequently, models of 
21 Stephen A. Ross, “The Arbitrage Theory of Capital Asset Pricing,” Journal of Economic 
Theory (December 1976), pp. 343–362. 

89 
Milestones in Financial Modeling and Investment Management 
this type are referred to as multifactor risk models. These models are 
applied to portfolio management. 
ARBITRAGE, HEDGING, AND OPTION THEORY: BLACK, SCHOLES, 
AND MERTON 
The idea of arbitrage pricing can be extended to any price process. A 
general model of asset pricing will include a number of independent 
price processes plus a number of price processes that depend on the first 
process by arbitrage. The entire pricing structure may or may not be 
cast in a general equilibrium framework. 
Arbitrage pricing allowed derivative pricing. With the development 
of derivatives trading, the requirement of a derivative valuation and 
pricing model made itself felt. The first formal solution of the option 
pricing model was developed independently by Fisher Black and Myron 
Scholes in 1976,22 working together, and in the same year by Robert 
Merton.23 
The solution of the option pricing problem proposed by Black, 
Scholes, and Merton was simple and elegant. Suppose that a market 
contains a risk-free bond, a stock, and an option. Suppose also that the 
market is arbitrage-free and that stock price processes follow a continu-
ous-time geometric Brownian motion (see Chapter 8). Black, Scholes, 
and Merton demonstrated that it is possible to construct a portfolio 
made up of the stock plus the bond that perfectly replicates the option. 
The replicating portfolio can be exactly determined, without anticipa-
tion, solving a partial differential equation. 
The idea of replicating portfolios has important consequences. 
Whenever a financial instrument (security or derivative instrument) pro-
cess can be exactly replicated by a portfolio of other securities, absence 
of arbitrage requires that the price of the original financial instrument 
coincide with the price of the replicating portfolio. Most derivative pric-
ing algorithms are based on this principle: to price a derivative instru-
ment, one must identify a replicating portfolio whose price is known. 
Pricing by portfolio replication received a powerful boost with the 
discovery that calculations can be performed in a risk-neutral probabil-
ity space where processes assume a simplified form. The foundation was 
thus laid for the notion of equivalent martingales, developed by Michael 
22 Fischer Black and Myron Scholes, “The Pricing of Options and Corporate Liabil-
ities,” Journal of Political Economy (1973), pp. 637–654. 
23 Robert C. Merton, “Theory of Rational Option Pricing,” Bell Journal of Econom-
ics and Management Science (1973), pp. 141–183. 

90 
The Mathematics of Financial Modeling and Investment Management 
Harrison and David Kreps24 and Michael Harrison and Stanley Pliska25 
in the late 1970s and early 1980s. Not all price processes can be 
reduced in this way: if price processes do not behave sufficiently well 
(i.e., if the risk does not vanish with the vanishing time interval), then 
replicating portfolios cannot be found. In these cases, risk can be mini-
mized but not hedged. 
SUMMARY
 ■ The development of mathematical finance began at the end of the nine-
teenth century with work on general equilibrium theory by Walras and 
Pareto.
 ■ At the beginning of the twentieth century, Bachelier and Lundberg 
made a seminal contribution, introducing respectively Brownian 
motion price processes and Markov Poisson processes for collective 
risk events.
 ■ The advent of digital computers enabled the large-scale application of 
advanced mathematics to finance theory, ushering in optimization and 
simulation.
 ■ In 1952, Markowitz introduced the theory of portfolio optimization 
which advocates the strategy of portfolio diversification.
 ■ In 1961, Modigliani and Miller argued that the value of a company is 
based not on its dividends and capital structure, but on its earnings; 
their formulation was to be called the Modigliani-Miller theorem.
 ■ In the 1960s, major developments include the efficient market hypothe-
sis (Samuelson and Fama), the capital asset pricing model (Sharpe, 
Lintner, and Mossin), and the multifactor CAPM (Merton).
 ■ In the 1970s, major developments include the arbitrage pricing theory 
(Ross) that lead to multifactor models and option pricing formulas 
(Black, Scholes, and Merton) based on replicating portfolios which are 
used to price derivatives if the underlying price processes are known. 
24 J. Michael Harrison and David M. Kreps, “Martingale and Arbitrage in Multipe-
riod Securities Markets,” Journal of Economic Theory 20 (1979), pp. 381–408. 
25 Michael Harrison and Stanley Pliska, “Martingales and Stochastic Integrals in the 
Theory of Continuous Trading,” Stochastic Processes and Their Applications 
(1981), pp. 313–316. 


## Matrix Algebra

CHAPTER 5 
Matrix Algebra 
O
rdinary algebra deals with operations such as addition and multiplica-
tion performed on individual numbers. In many applications, however, 
it is useful to consider operations performed on ordered arrays of num-
bers. This is the domain of matrix algebra. Ordered arrays of numbers are 
called vectors and matrices while individual numbers are called scalars. In 
this chapter, we will discuss the basic operations of matrix algebra. 
VECTORS AND MATRICES DEFINED 
Let’s now define precisely the concepts of vector and matrix. Though 
vectors can be thought of as particular matrices, in many cases it is use-
ful to keep the two concepts—vectors and matrices—distinct. In partic-
ular, a number of important concepts and properties can be defined for 
vectors but do not generalize easily to matrices.1 
Vectors 
An n-dimensional vector is an ordered array of n numbers. Vectors are 
generally indicated with bold-face lower case letters. Thus a vector x is 
an array of the form 
x = [x1…x ]
n 
The numbers xi are called the components of the vector x. 
A vector is identified by the set of its components. Consider the vec-
tors x = [x1…xn] and y = [y1…ym]. Two vectors are said to be equal if 
1 Vectors can be thought as the elements of an abstract linear space while matrices 
are operators that operate on linear spaces. 
141 

142 
The Mathematics of Financial Modeling and Investment Management 
and only if they have the same dimensions n = m and the same compo-
nents: 
x = y ⇔ xi = yi, i = 1, …, n 
Vectors can be row vectors or column vectors. If the vector compo-
nents appear in a horizontal row, then the vector is called a row vector, 
as for instance the vector 
x = [1 2 8 7] 
Here are two examples. Suppose that we let wn be a risky asset’s 
weight in a portfolio. Assume that there are N risky assets. Then the fol-
lowing vector, w, is a row vector that represents a portfolio’s holdings of 
the N risky assets: 
w 
w1 w2 ……… wN 
= 
As a second example of a row vector, suppose that we let rn be the 
excess return for a risky asset. (The excess return is the difference 
between the return on a risky asset and the risk-free rate.) Then the fol-
lowing row vector is the excess return vector: 
r 
r1 r2 ……… rN 
= 
If the vector components are arranged in a column, then the vector 
is called a column vector as, for instance, the vector 
x = 
1 
2 
8 
7 
For example, as explained in Chapter 19, a portfolio’s excess return 
will be affected by what can be different characteristics or attributes that 
affect all asset prices. A few examples would be the price-earnings ratio, 
market capitalization, and industry. We can denote for a particular 
attribute a column vector, a, that shows the exposure of each risky asset 
to that attribute: 

Matrix Algebra 
143 
a = 
a1 
a2 
· 
· 
aN 
where an is the exposure of asset n to attribute a. 
Vector components can be either real or complex numbers. Return-
ing to the row vector w of a portfolio of holdings, a positive value for 
wn would mean that some of the risky asset n is held in the portfolio; a 
value of zero would mean that the risky asset n is not held in the portfo-
lio. If the value of wn is negative, this means that there is a short posi-
tion in risky asset n. 
While in most applications in economics and finance vector compo-
nents are real numbers, recall that a complex number is a number which 
can be represented in the form 
c = a + bi
 
where i is the imaginary unit. One can operate on complex numbers2 as if 
they were real numbers but with the additional rule: i2 = –1. In the follow-
ing we will assume that vectors have real components unless we explicitly 
state the contrary. 
Vectors admit a simple graphic representation. Consider an n-dimensional 
Cartesian space. An n-dimensional vector is represented by a segment 
that starts from the origin and such that its projections on the n-th axis 
are equal to the n-th component of the vector. The direction of the vec-
tor is assumed to be from the origin to the tip of the segment. Exhibit 
5.1 illustrates this representation in the case of the usual three spatial
dimensions x,y,z. 
The (Euclidean) length of a vector x, also called the norm of a vec-
tor, denoted as x , is defined as the square root of the sum of the 
squares of its components: 
2
2 
x = 
x1 + … + xn 
2 In rigorous mathematical terms, complex numbers are defined as ordered pairs of 
real numbers. Operations on complex numbers are defined as operations on pairs of 
real numbers. The representation with the imaginary unit is a shorthand based on a 
rigorous definition of complex numbers. 

144 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 5.1 
Graphical Representation of Vectors 
Matrices 
An n×m matrix is a bidimensional ordered array of n×m numbers. 
Matrices are usually indicated with bold-face upper case letters. Thus, 
the generic matrix A is an n×m array of the form 
·
· 
, 
a1 1
a1, j
a1, m 
·
 ·
·
·
 ·
 
·
·
A = ai, 1 
ai j
ai m
,
, 
·
 ·
·
·
 ·
 
·
· a
an, 1 
an j
n m
,
, 
Note that the first subscript indicates rows while the second sub-
script indicates columns. The entries aij—called the elements of the 
matrix A—are the numbers at the crossing of the i-th row and the j-th 
column. The commas between the subscripts of the matrix entries are 
omitted when there is no risk of confusion: ai j ≡aij . A matrix A is often 
, 
indicated by its generic element between brackets: 
A = {
}nm or A = [
]nm 
aij
aij

Matrix Algebra 
145 
where the subscripts nm are the dimensions of the matrix. 
The elements of a matrix can be either real numbers or complex 
numbers. In the following, we will assume that elements are real num-
bers unless explicitly stated otherwise. If the matrix entries are real 
numbers, the matrix is called a real matrix; if the aij are complex num-
bers, the matrix is called a complex matrix. 
Two matrices are said to be equal if they are of the same dimensions 
and have the same elements. Consider two matrices A = {aij}nm and B = 
{bij}nm of the same order n×m: 
A = B means {
}nm = 
bij
aij
{
}nm 
Vectors are matrices with only one column or only one row. An n-
dimensional row vector is an n×1 matrix, an n-dimensional column vec-
tor is a 1×n matrix. A matrix can be thought of as an array of vectors. 
Denote by aj the column vector formed by the j-th column of the matrix 
A. The matrix A can then be written as A = [
] . This notation can be
aj
generalized. Suppose that the two matrices B, C have the same number 
n of rows and mB, mC columns respectively. The matrix A = [B C] is the 
matrix whose first mB columns are formed by the matrix B and the fol-
lowing mC columns are formed by the matrix C. 
SQUARE MATRICES 
There are several types of matrices. First there is a broad classification 
of square and rectangular matrices. A rectangular matrix can have dif-
ferent numbers of rows and columns; a square matrix is a rectangular 
matrix with the same number n of rows as of columns. 
Diagonals and Antidiagonals 
An important concept for a square matrix is the diagonal. The diagonal 
includes the elements that run from the first row, first column to the last 
row, last column. For example, consider the following square matrix: 
·
· 
, 
a1 1
a1, j
a1, n 
·
 ·
·
·
 ·
 
·
· 
,
, 
A = ai, 1 
ai j
ai n
·
 ·
·
·
 ·
 
·
· a
an, 1 
an j
n n
,
, 
The diagonal terms are the aj,j terms. 

146 
The Mathematics of Financial Modeling and Investment Management 
The antidiagonals of a square matrix are the other diagonals that do 
not run from the first row, first column to the last row, last column. For 
example, consider the following 4×4 square matrix: 
5 9 14 8 
2 6 12 11 
17 21 42 2 
19 73 7 8 
The diagonal terms include 5, 6, 42, 8. One antidiagonal is 2, 9. Another 
antidiagonal is 17, 6, 14. Note that there are antidiagonal terms in rect-
angular matrices. 
Identity Matrix 
The n×n identity matrix, indicated as the matrix In, is a square matrix 
whose diagonal elements (i.e., the entries with the same row and column 
suffix) are equal to one while all other entries are zero: 
1  0 · · · 0  
0  1 · · · 0  
· · ·  
·  
I
= 
n 
· ·  ·  ·  
· ·  
· ·  
0  0 · · · 1  
A matrix whose entries are all zero is called a zero matrix. 
Diagonal Matrix 
A diagonal matrix is a square matrix whose elements are all zero except 
the ones on the diagonal: 
a11
0  · · ·  0  
0 a22 · · ·  0  
A = 
·
·
· 
· 
·
· 
· 
· 
·
· 
·
· 
0  0  · · ·  ann 
Given a square n×n matrix A, the matrix dg A is the diagonal matrix 
extracted from A. The diagonal matrix dg A is a matrix whose elements 

Matrix Algebra 
147 
are all zero except the elements on the diagonal that coincide with those 
of the matrix A: 
· · ·  
a11
0  · · ·  0
a11 a12 
a1n 
· · ·  
· · ·  0
a21 a22 
a2n 
0 a22 
A = 
·
·
·
· 
· 
⇒ dgA = 
· 
·
· 
·
·
·
· 
·
·
·
· 
·
·
·
· 
·
·
·
· 
an1 an2 · · ·  ann 
0  0  · · ·  ann 
The trace of a square matrix A is the sum of its diagonal elements: 
n 
trA = ∑ aii 
i = 1 
A square matrix is called symmetric if the elements above the diago-
nal are equal to the corresponding elements below the diagonal: aij = aji. 
A matrix is called skew-symmetric if the diagonal elements are zero and 
the elements above the diagonal are the opposite of the corresponding 
elements below the diagonal: aij = –aji, i ≠ j, aii = 0. 
The most commonly used symmetric matrix in finance and econo-
metrics is the covariance matrix, also referred to as the variance-covari-
ance matrix. (See Chapter 6 for a detailed explanation of variances and 
covariances.) For example, suppose that there are N risky assets and 
that the variance of the excess return for each risky asset and the covari-
ances between each pair of risky assets are estimated. As the number of 
credit risky assets is N there are N2 elements, consisting of N variances 
(along the diagonal) and N2 – N covariances. Symmetry restrictions 
reduce the number of independent elements. In fact the covariance σij(t) 
between risky asset i and risky asset j will be equal to the covariance 
between risky asset j and risky asset i. We can therefore arrange the 
variances and covariances in the following square matrix V: 
, 
σ1 1 · σ1, i · σ1, N 
·
·
·
·
 ·
 
,
, 
V = 
σ1, i · σi i · σi N
·
·
·
·
 ·
 
σ1, N · σi N · σN N
,
, 
Notice that V is a symmetric matrix. 

148 
The Mathematics of Financial Modeling and Investment Management 
Upper and Lower Triangular Matrix 
A matrix A is called upper triangular if aij = 0, i > j. In other words, an 
upper triangular matrix is a matrix whose elements in the triangle below 
the diagonal are all zero as is illustrated below:
·
· 
, 
a1 1
a1, i
a1, n 
·
 ·
·
·
 ·
 
A = 
0
·
 ai i · ai n  [upper triangular]
,
, 
·
 ·
·
·
 ·
 
0
·
0
·
 
an n
, 
A matrix A is called lower triangular if aij = 0, i < j. In other words, 
a lower triangular matrix is a matrix whose elements in the triangle 
above the diagonal are zero as is illustrated below: 
a1 1 ·
0
·
 0
 
, 
·
·
·
·
·
 
A = 
·
·
 
ai i ·
0
 [lower triangular]
, 
·
 ·
·
·
 ·
 
·
· a
an, 1 
an i
n n
,
, 
DETERMINANTS 
Consider a square, n×n, matrix A. The determinant of A, denoted A , is 
defined as follows: 
n 
= ∑(–1)
t j1, …, j )
( 
n
A 
∏ aij 
i = 1 
where the sum is extended over all permutations (j1,…,jn) of the set (1, 
2,…,n) and t(j1,…,jn) is the number of transpositions (or inversions of 
positions) required to go from (1,2,…,n) to (j1,…,jn). 
Otherwise stated, a determinant is the sum of all different products 
formed taking exactly one element from each row with each product 
multiplied by 
(–1)
t j1, …, j )
( 
n 

Matrix Algebra 
149 
Consider, for instance, the case n = 2, where there is only one possi-
ble transposition: 1,2 ⇒ 2,1. The determinant of a 2×2 matrix is there-
fore computed as follows: 
1
A = (–1)0 a11a22 + (–1) a12a21 = a11a22 – a12a21 
Consider a square matrix A of order n. Consider the matrix Mij 
obtained by removing the ith row and the jth column. The matrix Mij is 
a square matrix of order (n – 1). The determinant 
of the matrix
Mij
Mij is called the minor of aij. The signed minor 
+
(–1)(i
j) Mij 
is called the cofactor of aij and is generally denoted as αij. The r-minors 
of the n×m rectangular matrix A are the determinants of the matrices 
formed by the elements at the crossing of r different rows and r different 
columns of A. 
A square matrix A is called singular if its determinant is equal to 
zero. An n×m matrix A is of rank r if at least one of its (square) r-minors 
is different from zero while all (r + 1)-minors, if any, are zero. A non-
singular square matrix is said to be of full rank if its rank r is equal to 
its order n. 
SYSTEMS OF LINEAR EQUATIONS 
A system of n linear equations in m unknown variables is a set of n 
simultaneous equations of the following form: 
a1 1x1 + … + a1, mx
= b1
, 
m 
…………………… 
an, 1x1 + … + a1, mxm = bm 
The n×m matrix 
·
· 
, 
a1 1
a1, j
a1, m 
·
 ·
·
·
 ·
 
A = ai, 1 · ai j · ai m
,
, 
·
 ·
·
·
 ·
 
·
· a
an, 1 
an j
n m
,
, 

150 
The Mathematics of Financial Modeling and Investment Management 
formed with the coefficients of the variables is called the coefficient 
matrix. The terms bi are called the constant terms. The augmented 
matrix [A b]—formed by adding to the coefficient matrix a column 
formed with the constant term—is represented below: 
· 
, 
a1 1
a1, j · a1, m b1 
·
 ·
·
·
 ·
 
,
,
[A b] = ai, 1 · ai j · ai m bi 
·
 ·
·
·
 ·
 
·
· a
,
, 
an, 1 
an j
n m bn 
If the constant terms on the right side of the equations are all zero, the 
system is called homogeneous. If at least one of the constant terms is dif-
ferent from zero, the system is called nonhomogeneous. A system is called 
consistent if it admits a solution, i.e., if there is a set of values of the vari-
ables that simultaneously satisfy all the equations. A system is called 
inconsistent if there is no set of numbers that satisfy the system equations. 
Let’s first consider the case of nonhomogeneous linear systems. The 
fundamental theorems of linear systems state that: 
■ Theorem 1. A system of n linear equations in m unknowns is consistent 
(i.e., it admits a solution) if and only if the coefficient matrix and the 
augmented matrix have the same rank. 
■ Theorem 2. If a consistent system of n equations in m variables is of 
rank r < m, it is possible to choose n–r unknowns so that the coefficient 
matrix of the remaining r unknowns is of rank r. When these m–r vari-
ables are assigned any arbitrary value, the value of the remaining vari-
ables is uniquely determined. 
An immediate consequence of the fundamental theorems is that (1) a 
system of n equations in n unknown variables admits a solution and (2) the 
solution is unique if and only if both the coefficient matrix and the aug-
mented matrix are of rank n. 
Let’s now examine homogeneous systems. The coefficient matrix and 
the augmented matrix of a homogeneous system always have the same 
rank and thus a homogeneous system is always consistent. In fact, the 
trivial solution x1 = … = xm = 0 always satisfies a homogeneous system. 
Consider now a homogeneous system of n equations in n unknowns. 
If the rank of the coefficient matrix is n, the system has only the trivial 
solution. If the rank of the coefficient matrix is r < n, then Theorem 2 
ensures that the system has a solution other than the trivial solution. 

Matrix Algebra 
151 
LINEAR INDEPENDENCE AND RANK 
Consider an n×m matrix A. A set of p columns extracted from the 
matrix A 
·
·
·
a1, i1 
a1, ip 
·
·
·
·
· 
·
·
·
·
· 
·
·
·
·
· 
·
·
·
an i, 1 
an i, p 
are said to be linearly independent if it is not possible to find p constants 
βs, s = 1,…,p such that the following n equations are simultaneously sat-
isfied: 
+
β1a1, i1 + …
βpa1, ip = 0 
…………………… 
+
β1an i, 1 + …
βpan i
= 0 
, p 
Analogously, a set of q rows extracted from the matrix A are said to 
be linearly independent if it is not possible to find q constants λs, s  = 
1,…,q, such that the following m equations are simultaneously satisfied: 
+
λ1ai1, 1 + …
λqaiq, 1 = 0 
…………………… 
+
λ1ai1, m + …
λqaiq, m = 0 
It can be demonstrated that in any matrix the number p of linearly 
independent columns is the same as the number q of linearly indepen-
dent rows. This number is equal, in turn, to the rank r of the matrix. 
Recall that an n×m matrix A is said to be of rank r if at least one of its 
(square) r-minors is different from zero while all (r+1)-minors, if any, 
are zero. The constant, p, is the same for rows and for columns. We can 
now give an alternative definition of the rank of a matrix: 
Given an n×m matrix A, its rank, denoted rank(A), is the number r of 
linearly independent rows or columns. This definition is meaningful 
because the row rank is always equal to the column rank. 

152 
The Mathematics of Financial Modeling and Investment Management 
HANKEL MATRIX 
For the theoretical analysis of the autoregressive integrated moving 
averages (ARMA) processes described in Chapter 11, it is important to 
understand a special type of matrix, a Hankel matrix. A Hankel matrix 
is a matrix where for each antidiagonal the element is the same. For 
example, consider the following square Hankel matrix: 
17 16 15 24 
16 15 24 33 
15 24 33 72 
24 33 72 41 
Each antidiagonal has the same value. Now consider the elements of the 
antidiagonal running from the second row, first column and first row, 
second column. Both elements have the value 16. Consider another 
antidiagonal running from the fourth row, second column to the second 
row, fourth column. All of the elements have the value 33. 
An example of a rectangular Hankel matrix would be 
72 60 55 43 30 21 
60 55 43 30 21 10 
55 43 30 21 10 80 
Notice that a Hankel matrix is a symmetric matrix.3 
Consider an infinite sequence of square n×n matrices: 
H0, H1, …, Hi, … 
The infinite Hankel matrix H is the following matrix: 
3 A special case of a Hankel matrix is when the values for the elements in the first 
row of the matrix are repeated in each successive row such that its value appears one 
column to the left. For example, consider the following square Hankel matrix: 
41 32 23 14 
32 23 14 41 
23 14 41 32 
14 41 32 23 
This type of Hankel matrix is called an anticirculant matrix. 

Matrix Algebra 
153 
H0 H1 H2 … 
H1 H2 … …  
H = H2 … … …  
… 
… 
The rank of a Hankel matrix can be defined in three different ways: 
1. The  column rank is the largest number of linearly independent 
sequence columns. 
2. The row rank is the largest number of linearly independent sequence 
rows. 
3. The rank is the superior of the ranks of all finite matrices of the type: 
H0 
H1
· 
HN' 
H1 
H2
· 
· 
=
HN N'
, 
·
·
·
· 
HN 
·
· 
HN
N'
+ 
As in the finite-dimensional case, the three definitions are equivalent in 
the sense that the three numbers are equal, if finite, or they are all three 
infinite. 
VECTOR AND MATRIX OPERATIONS 
Let’s now introduce the most common operations performed on vectors 
and matrices. An operation is a mapping that operates on scalars, vectors, 
and matrices to produce new scalars, vectors, or matrices. The notion of 
operations performed on a set of objects to produce another object of the 
same set is the key concept of algebra. Let’s start with vector operations. 
Vector Operations 
The following operations are usually defined on vectors: (1) transpose, 
(2) addition, and (3) multiplication.
Transpose 
The transpose operation transforms a row vector into a column vector and 
vice versa. Given the row vector x = [x1…x ] its transpose, denoted as xT 
n
or x′, is the column vector: 

154 
The Mathematics of Financial Modeling and Investment Management 
x1 
· 
T 
x = 
· 
· 
xn 
Clearly the transpose of the transpose is the original vector: 
(x T)
T = x 
Addition 
Two row (or column) vectors x = [x1…xn], y = [y1…yn] with the same 
number n of components can be added. The addition of two vectors is a 
new vector whose components are the sums of the components: 
+
x
y = [x1 + y1…x + yn]
n 
This definition can be generalized to any number N of summands: 
N 
N
N 
∑ xi = ∑ x1i… ∑ yni 
i = 1 
i = 1 
i = 1 
The summands must be both column or row vectors; it is not possible to 
add row vectors to column vectors. 
It is clear from the definition of addition that addition is a commu-
tative operation in the sense that the order of the summands does not 
matter: x + y = y + x. Addition is also an associative operation in the 
sense that x + (y + z) = (x + y) + z. 
Multiplication 
We define two types of multiplication: (1) multiplication of a scalar and 
a vector and (2) scalar multiplication of two vectors (inner product).4 
The multiplication of a scalar λ and a row (or column) vector x, 
denoted as λx, is defined as the multiplication of each component of the 
vector by the scalar: 
4 Different types of products between vectors can be defined: the vector product be-
tween vectors produces a third vector and the outer product produces a matrix. We 
do not define them here, as, though widely used in the physical sciences, they are not 
typically used in economics. 

Matrix Algebra 
155 
λx = [λx1…λx ]
n 
As an example of the multiplication of a vector by a scalar, consider 
the vector of portfolio weights w = [w1…wn]. If the total portfolio value 
at a given moment is P, then the holding in each asset is the product of 
the value by the vector of weights: 
Pw = [Pw1…Pw ]
n 
A similar definition holds for column vectors. It is clear from this defini-
tion that 
ax = a x 
and that multiplication by a scalar is associative as 
a(x
y)
+ 
= ax + ay 
The scalar (or inner) product of two vectors of the same dimensions 
x, y, denoted as x · y, is defined between a row vector and a column vec-
tor. The scalar product between two vectors produces a scalar according 
to the following rule: 
n 
⋅
x y = ∑ xiyi 
i = 1 
For example, consider the column vector a of a particular attribute dis-
cussed earlier and the row vector w of portfolio weights. Then a · w is a 
scalar that shows the exposure of the portfolio to the particular 
attribute. That is, 
a w
⋅ 
a1 
a2 
· 
· 
aN 
w1 w2 …… wN 
= 
N 
= ∑ anwN 
n = 1 

156 
The Mathematics of Financial Modeling and Investment Management 
As another example, a portfolio’s excess return is found by taking 
the transpose of the excess return vector, r, and multiplying it by the 
vector of portfolio weights, w. That is, 
r T w
⋅ 
r1 
r2 
· 
· 
rN 
w1 w2 …… wN 
= 
N 
= ∑rnwN 
n = 1 
Two vectors x, y are said to be orthogonal if their scalar product is 
zero. The scalar product of two vectors can be interpreted geometrically 
as an orthogonal projection. In fact, the inner product of vectors x and 
y, divided by the square norm of y, can be interpreted as the orthogonal 
projection of x onto y. The following two properties are an immediate 
consequence of the definitions: 
x = 
x ⋅x 
ax
( 
) ⋅by
( 
) = abx y
⋅ 
Matrix Operations 
The following five operations on matrices are usually defined: (1) trans-
pose, (2) addition, (3) multiplication, (4) inverse, and (5) adjoint. 
Transpose 
The definition of the transpose of a matrix is an extension of the trans-
pose of a vector. The transpose operation consists in exchanging rows 
with columns. Consider the n×m matrix 
A = {
}nm 
aij
The transpose of A, denoted AT or A′ is the m×n matrix whose ith row is 
the ith column of A: 
AT = {
}mn 
aji

Matrix Algebra 
157 
The following should be clear from this definition: 
(AT)
T = A 
and that a matrix is symmetric if and only if 
AT = A 
Addition 
Consider two n×m matrices 
A = {
}nm 
aij
and 
B = {
}nm 
bij 
The sum of the matrices A and B is defined as the n×m matrix obtained 
by adding the respective elements: 
+
A
B = {aij + bij}nm 
Note that it is essential for the definition of addition that the two matri-
ces have the same order n×m. 
The operation of addition can be extended to any number N of 
summands as follows: 
N 
N 

∑Ai = ∑asij 
 
s = 1 
s = 1 
nm 
where a
 is the generic i,j element of the sth summand.
sij 
The following properties of addition are immediate from the defini-
tion of addition: 
A
B
+ 
= 
+ 
B
A
+ (
+
+ 
+
+
A
 B
C
 
) = (A
B) + C = A
B
C

158 
The Mathematics of Financial Modeling and Investment Management 
+
tr(A
B) = trA + trB 
The operation of addition of vectors defined above is clearly a special 
case of the more general operation of addition of matrices. 
Multiplication 
Consider a scalar c and a matrix: 
A = {
}nm 
aij
The product cA = Ac is the n×m matrix obtained by multiplying each 
element of the matrix by c: 
cA = Ac = {
 }nm 
caij 
Multiplication of a matrix by a scalar is associative with respect to 
matrix addition: 
+
c(A
B) = cA + cB 
Let’s now define the product of two matrices. Consider two matrices: 
A = {
}np 
ait
and 
B = {
 }pm 
bsj 
The product C = AB is defined as follows: 
p

 
C = AB
 
= {
} = ∑aitbtj
cij

t = 1 
The product C = AB is therefore a matrix whose generic element {cij} is 
the scalar product of the ith row of the matrix A and the jth column of 
the matrix B. This definition generalizes the definition of scalar product 
of vectors: The scalar product of two n-dimensional vectors is the product 
of an n×1 matrix (a row vector) for a 1×n matrix (the column vector). 
Following the above definition, the matrix product operation is per-
formed rows by columns. Therefore, two matrices can be multiplied 

Matrix Algebra 
159 
only if the number of columns (i.e., the number of elements in each row) 
of the first matrix equals the number of rows (i.e., the number of ele-
ments in each column) of the second matrix. 
The following two distributive properties hold: 
(
C A  + B) = CA + CB 
+
(A
B)C = AC
 
+ BC
 
The associative property also holds: 
(
(AB)C = A
 
BC
 
) 
However, the matrix product operation is not commutative. In fact, if A 
and B are two square matrices, in general AB ≠BA. Also AB = 0 does 
not imply A = 0 or B = 0. 
Inverse and Adjoint 
Consider two square matrices of order n, A and B. If AB = BA = I, then 
the matrix B is called the inverse of A and is denoted as A–1. It can be 
demonstrated that the two following properties hold:
 ■ Property 1. A square matrix A admits an inverse A–1 if and only if it is 
nonsingular, i.e., if and only if its determinant is different from zero. 
Otherwise stated, a matrix A admits an inverse if and only if it is of full 
rank.
 ■ Property 2. The inverse of a square matrix, if it exists, is unique. This 
property is a consequence of the property that, if A is nonsingular, then 
AB = AC implies B = C. 
Consider now a square matrix of order n A = {aij} and consider its 
cofactors αij. Recall that the cofactors αij are the signed minors 
+
(–1)(i
j)
of the matrix A. The adjoint of the matrix A, denoted as
Mij 
Adj(A), is the following matrix: 
, 
,
, 
α1 1 · α1, j · α1, n
T 
α1 1 · α2 1 · αn, 1 
·
·
·
·
·
 
·
·
·
·
·
 
Adj A
,
,
(
) = αi, 1 · αi j · αi n
= α1, i · α2, i · αn i, 
·
·
·
·
·
 
·
·
·
·
·
 
αn, 1 · αn j · α
, 
n n
α1, n · α2, n · αn n
,
, 

160 
The Mathematics of Financial Modeling and Investment Management 
The adjoint of a matrix A is therefore the transpose of the matrix 
obtained by replacing the elements of A with their cofactors. 
If the matrix A is nonsingular, and therefore admits an inverse, it 
can be demonstrated that 
A –1 
Adj A
(
)
 
= ------------------
A 
A square matrix A of order n is said to be orthogonal if the follow-
ing property holds: 
AA′ = A′A = In 
Because in this case A must be of full rank, the transpose of an orthogo-
nal matrix coincides with its inverse: A–1 = A′. 
EIGENVALUES AND EIGENVECTORS 
Consider a square matrix A of order n and the set of all n-dimensional 
vectors. The matrix A is a linear operator on the space of vectors. This 
means that A operates on each vector producing another vector and that 
the following property holds: 
A(ax + by) = aAx + bAy 
Consider now the set of vectors x such that the following property 
holds: 
Ax = λx 
Any vector such that the above property holds is called an eigenvector 
of the matrix A and the corresponding value of λ is called an eigenvalue. 
To determine the eigenvectors of a matrix and the relative eigenval-
ues, consider that the equation Ax = λx can be written as follows: 
(A – λI)x = 0 
which can, in turn, be written as a system of linear equations: 

Matrix Algebra 
161 
, 
a1 1 – λ · a1, j 
· 
a1, n
x1 
·
·
·
·
· 
· 
(A – λI)x = 
ai, 1
· ai i – λ · 
ai n
xi = 0 
,
, 
·
·
·
·
· 
· 
an, 1
· an j
· an n – λ x
,
, 
n 
This system of equations has nontrivial solutions only if the matrix A – 
λI is singular. To determine the eigenvectors and the eigenvalues of the 
matrix A we must therefore solve the equation 
a1 1 – λ ·
· 
, 
a1, j
a1, n 
· 
·
·
· 
· 
A – λI = 
= 0
ai, 1
· ai i – λ · 
ai n
,
, 
· 
·
·
· 
· 
an, 1
· an j
· an n – λ 
,
, 
The expansion of this determinant yields a polynomial φ(λ) of 
degree n known as the characteristic polynomial of the matrix A. The 
equation φ(λ) = 0 is known as the characteristic equation of the matrix 
A. In general, this equation will have n roots λs which are the eigenval-
ues of the matrix A. To each of these eigenvalues corresponds a solution 
of the system of linear equations as illustrated below: 
a1 1 – λ ·
· 
a1, n
x1
, 
s
a1, j
s 
·
·
·
·
· 
· 
ai, 1
· ai i – λ · 
ai n
xi
= 0
, 
s 
, 
s 
·
·
·
·
· 
· 
· a
x
,
, 
an, 1
· 
an j
n n – λs 
ns 
Each solution represents the eigenvector xs corresponding to the eigen-
vector λs. As we will see in Chapter 12, the determination of eigenvalues 
and eigenvectors is the basis for principal component analysis. 
DIAGONALIZATION AND SIMILARITY 
Diagonal matrices are much easier to handle than fully populated matri -
ces. It is therefore important to create diagonal matrices equivalent (in a 
sense to be precisely defined) to a given matrix. Consider two square 

162 
The Mathematics of Financial Modeling and Investment Management 
matrices A and B. The matrices A and B are called similar if there exists 
a nonsingular matrix R such that 
B = R–1AR 
The following two theorems can be demonstrated:
 ■ Theorem 1. Two similar matrices have the same eigenvalues. 
■ Theorem 2. If yi is an eigenvector of the matrix B = R–1AR corre-
sponding to the eigenvalue λ i, then the vector xi = Ryi is an eigenvector 
of the matrix A corresponding to the same eigenvalue λ i. 
A diagonal matrix of order n always has n linearly independent eigen-
vectors. Consequently, a square matrix of order n has n linearly inde-
pendent eigenvectors if and only if it is similar to a diagonal matrix. 
Suppose the square matrix of order n has n linearly independent 
eigenvectors xi and n distinct eigenvalues λ i. This is true, for instance, if 
A is a real, symmetric matrix of order n. Arrange the eigenvectors, 
which are column vectors, in a square matrix: P = {xi}. It can be demon-
strated that P–1AP is a diagonal matrix where the diagonal is made up of 
the eigenvalues: 
λ 1 0
0
0
0
 
0
 ·
 0
0
0
 
P –1AP = 
0
0
 λ i 0
0
 
0
0
0
·
0
 
0
0
0
0
 λ n 
SINGULAR VALUE DECOMPOSITION 
Suppose that the n× m matrix A with m ≥ n has rank(A) = r > 0. It can be 
demonstrated that there exists three matrices U, W, V such that the fol-
lowing decomposition, called singular value decomposition, holds: 
A = UWV′
and such that U is n× r with U′ U = Ir; W is diagonal, with non-negative 
diagonal elements; and V is m× r with V′ V = Ir. 

Matrix Algebra 
163 
SUMMARY 
 ■ In representing and modeling economic and financial phenomena it is 
useful to consider ordered arrays of numbers as a single mathematical 
object.
 ■ Ordered arrays of numbers are called vectors and matrices; vectors are 
a particular type of matrix.
 ■ It is possible to consistently define operations on vectors and matrices 
including the multiplication of matrices by scalars, sum of matrices, 
product of matrices, and inversion of matrices.
 ■ Determinants are numbers associated with square matrices defined as 
the sum of signed products of elements chosen from different rows and 
columns.
 ■ A matrix can be inverted only if its determinant is not zero.
 ■ The eigenvectors of a square matrix are those vectors that do not 
change direction when multiplied by the matrix. 



## Concepts of Probability

CHAPTER 6 
Concepts of Probability 
P
robability is the standard mathematical representation of uncertainty in 
finance. In this chapter we present concepts in probability theory that 
are applied in many areas in financial modeling and investment manage-
ment. Here are just a few applications: The set of possible economic states 
is represented as a probability space; prices, cash flows, and other eco-
nomic quantities subject to uncertainty are represented as time-dependent 
random variables (i.e., stochastic processes); conditional probabilities are 
used in representing the dynamics of asset prices; and, probability distribu-
tions are used in finding the optimal risk-return tradeoff. 
REPRESENTING UNCERTAINTY WITH MATHEMATICS 
Because we cannot build purely deterministic models of the economy, we 
need a mathematical representation of uncertainty. Probability theory is the 
mathematical description of uncertainty that presently enjoys the broadest 
diffusion. It is the paradigm of choice for mainstream finance theory. But it 
is by no means the only way to describe uncertainty. Other mathematical 
paradigms for uncertainty include, for example, fuzzy measures.1 
Though probability as a mathematical axiomatic theory is well 
known, its interpretation is still the subject of debate. There are three 
basic interpretations of probability:
 ■ Probability as “intensity of belief” as suggested by John Maynard 
Keynes.2 
1 Lotfi A. Zadeh, “Fuzzy Sets,” Information and Control 8 (1965), pp. 338–353. 
2 John Maynard Keynes, Treatise on Probability (McMillan Publishing, 1921). 
165 

166 
The Mathematics of Financial Modeling and Investment Management
 ■ Probability as “relative frequency” as formulated by Richard von Mises.3
 ■ Probability as an axiomatic system as formulated by Andrei N. Kol-
4
mogorov. 
The idea of probability as intensity of belief was introduced by John 
Maynard Keynes in his Treatise on Probability. In science as in our daily 
lives, we have beliefs that we cannot strictly prove but to which we 
attribute various degrees of likelihood. We judge not only the likelihood of 
individual events but also the plausibility of explanations. If we espouse 
probability as intensity of belief, probability theory is then a set of rules 
for making consistent probability statements. The obvious difficulty here is 
that one can judge only the consistency of probability reasoning, not its 
truth. Bayesian probability theory (which we will discuss later in the chap-
ter) is based on the interpretation of probability as intensity of belief. 
Probability as relative frequency is the standard interpretation of 
probability in the physical sciences. Introduced by Richard Von Mises in 
1928, probability as relative frequency was subsequently extended by 
Hans Reichenbach.5 Essentially, it equates probability statements with 
statements about the frequency of events in large samples; an unlikely 
event is an event that occurs only a small number of times. The difficulty 
with this interpretation is that relative frequencies are themselves uncer-
tain. If we accept a probability interpretation of reality, there is no way 
to leap to certainty. In practice, in the physical sciences we usually deal 
with very large numbers—so large that nobody expects probabilities to 
deviate from their relative frequency. Nevertheless, the conceptual diffi-
culty exists. As the present state of affairs might be a very unlikely one, 
probability statements can never be proved empirically. 
The two interpretations of probability—as intensity of belief and as 
relative frequency—are therefore complementary. We make probability 
statements such as statements of relative frequency that are, ultimately, 
based on an a priori evaluation of probability insofar as we rule out, in 
practice, highly unlikely events. This is evident in most procedures of 
statistical estimation. A statistical estimate is a rule to choose the proba-
bility scheme in which one has the greatest faith. In performing statisti-
cal estimation, one chooses the probabilistic model that yields the 
3 Richard von Mises, Wahrscheinlichkeitsrechnung, Statistik unt Wahrheit (Vienna: 
Verlag von Julius Spring, 1928). (English edition published in 1939, Probability, Sta -
tistics and Truth.) 
4 Andrei N. Kolmogorov, Grundbegriffe der Wahrscheinlichkeitsrechnung (Berlin: 
Springer, 1933). (English edition published in 1950, Foundations of the Theory of 
Probability.) 
5 At the time, both were German professors working in Constantinople.  

167 
Concepts of Probability 
highest probability on the observed sample. This is strictly evident in 
maximum likelihood estimates but it is implicit in every statistical esti-
mate. Bayesian statistics allow one to complement such estimates with 
additional a priori probabilistic judgment. 
The axiomatic theory of probability avoids the above problems by 
interpreting probability as an abstract mathematical quantity. Devel-
oped primarily by the Russian mathematician Andrei Kolmogorov, the 
axiomatic theory of probability eliminated the logical ambiguities that 
had plagued probabilistic reasoning prior to his work. The application 
of the axiomatic theory is, however, a matter of interpretation. 
In economics and finance theory, probability might have two differ-
ent meanings: (1) as a descriptive concept and (2) as a determinant of 
the agent decision-making process. As a descriptive concept, probability 
is used in the sense of relative frequency, similar to its use in the physical 
sciences: the probability of an event is assumed to be approximately 
equal to the relative frequency of its occurrence in a large number of 
experiments. There is one difficulty with this interpretation, which is 
peculiar to economics: empirical data (i.e., financial and economic time 
series) have only one realization. Every estimate is made on a single 
time-evolving series. If stationarity (or a well-defined time process) is 
not assumed, performing statistical estimation is impossible. 
PROBABILITY IN A NUTSHELL 
In making probability statements we must distinguish between outcomes 
and events. Outcomes are the possible results of an experiment or an obser-
vation, such as the price of a security at a given moment. However, proba-
bility statements are not made on outcomes but on events, which are sets of 
possible outcomes. Consider, for example, the probability that the price of 
a security be in a given range, say from $10 to $12, in a given period. 
In a discrete probability model (i.e., a model based on a finite or at 
most a countable number of individual events), the distinction between 
outcomes and events is not essential as the probability of an event is the 
sum of the probabilities of its outcomes. If, as happens in practice, 
prices can vary by only one-hundredth of a dollar, there are only a 
countable number of possible prices and the probability of each event 
will be the sum of the individual probabilities of each admissible price. 
However, the distinction between outcomes and events is essential 
when dealing with continuous probability models. In a continuous proba-
bility model, the probability of each individual outcome is zero though the 
probability of an event might be a finite number. For example, if we repre-

168 
The Mathematics of Financial Modeling and Investment Management 
sent prices as continuous functions, the probability that a price assumes 
any particular real number is strictly zero, though the probability that 
prices fall in a given interval might be other than zero. 
Probability theory is a set of rules for inferring the probability of an 
event from the probability of other events. The basic rules are surprisingly 
simple. The entire theory is based on a few simple assumptions. First, the 
universe of possible outcomes or measurements must be fixed. This is a 
conceptually important point. If we are dealing with the prices of an 
asset, the universe is all possible prices; if we are dealing with n assets, the 
universe is the set of all possible n-tuples of prices. If we want to link n 
asset prices with k economic quantities, the universe is all possible (n + 
k)-tuples made up of asset prices and values of economic quantities. 
Second, as our objective is to interpret probability as relative frequen-
cies (i.e., percentages), the scale of probability is set to the interval [0,1]. 
The maximum possible probability is one, which is the probability that 
any of the possible outcomes occurs. The probability that none of the out-
comes occurs is 0. In continuous probability models, the converse is not 
true as there are nonempty sets of measure zero. In other words, in con-
tinuous probability models, a probability of one is not equal to certainty. 
Third, and last, the probability of the union of disjoint events is the 
sum of the probabilities of individual events. 
All statements of probability theory are logical consequences of these 
basic rules. The simplicity of the logical structure of probability theory 
might be deceptive. In fact, the practical difficulty of probability theory 
consists in the description of events. For instance, derivative contracts 
link in possibly complex ways the events of the underlying with the events 
of the derivative contract. Though the probabilistic “dynamics” of the 
underlying phenomena can be simple, expressing the links between all 
possible contingencies renders the subject mathematically complex. 
Probability theory is based on the possibility of assigning a precise 
uncertainty index to each event. This is a stringent requirement that 
might be too strong in many instances. In a number of cases we are sim-
ply uncertain without being able to quantify uncertainty. It might also 
happen that we can quantify uncertainty for some but not all events. 
There are representations of uncertainty that drop the strict requirement 
of a precise uncertainty index assigned to each event. Examples include 
fuzzy measures and the Dempster-Schafer theory of uncertainty.6 The 
latter representations of uncertainty have been widely used in Artificial 
6 See G. Schafer, A Mathematical Theory of Evidence (Princeton, NJ: Princeton Uni-
versity Press, 1976); Judea Pearl, Probabilistic Reasoning in Intelligent Systems: Net-
works of Plausible Beliefs (San Mateo, CA: Morgan Kaufmann, 1988); and, Zadeh, 
“Fuzzy Sets.” 

169 
Concepts of Probability 
Intelligence and engineering applications, but their use in economics 
and finance has so far been limited. 
Let’s now examine probability as the key representation of uncer-
tainty, starting with a more formal account of probability theory. 
OUTCOMES AND EVENTS 
The axiomatic theory of probability is based on three fundamental con-
cepts: (1) outcomes, (2) events, and (3) measure. The outcomes are the 
set of all possible results of an experiment or an observation. The set of 
all possible outcomes is often written as the set Ω. For instance, in the 
dice game a possible outcome is a pair of numbers, one for each face, 
such as 6 + 6 or 3 + 2. The space Ω is the set of all 36 possible out-
comes. 
Events are sets of outcomes. Continuing with the example of the 
dice game, a possible event is the set of all outcomes such that the sum 
of the numbers is 10. Probabilities are defined on events, not on out-
comes. To render definitions consistent, events must be a class ℑ of sub-
sets of Ω with the following properties: 
■ Property 1. ℑ is not empty
 ■ Property 2. If A ∈ ℑ then AC ∈ ℑ; AC is the complement of A with 
respect to Ω, made up of all those elements of Ω that do not belong to 
A
∞
 ■ Property 3. If Ai ∈ ℑ for i = 1,2,… then ∪ Ai 
ℑ 
∈ 
i = 1 
Every such class is called a σ-algebra. Any class for which Property 3 is 
valid only for a finite number of sets is called an algebra. 
Given a set Ω and a σ-algebra G of subsets of Ω, any set A ∈ G is said 
to be measurable with respect to G. The pair (Ω,G) is said to be a mea-
surable space (not to be confused with a measure space, defined later in 
this chapter). Consider a class G of subsets of Ω and consider the small-
est σ-algebra that contains G, defined as the intersection of all the σ-
algebras that contain G. That σ-algebra is denoted by σ{G} and is said 
to be the σ-algebra generated by G. 
A particularly important space in probability is the Euclidean space. 
Consider first the real axis R (i.e., the Euclidean space R1 in one dimen-
sion). Consider the collection formed by all intervals open to the left and 
closed to the right, for example, (a,b]. The σ-algebra generated by this 

170 
The Mathematics of Financial Modeling and Investment Management 
set is called the 1-dimensional Borel σ-algebra and is denoted by B . The 
sets that belong to B are called Borel sets. 
Now consider the n-dimensional Euclidean space Rn, formed by n-
tuples of real numbers. Consider the collection of all generalized rectan-
gles open to the left and closed to the right, for example, ((a1,b1] × ... 
×(an,bn]). The σ-algebra generated by this collection is called the n-
dimensional Borel σ-algebra and is denoted by B n. The sets that belong 
to B n are called n-dimensional Borel sets. 
The above construction is not the only possible one. The B n, for any 
value of n, can also be generated by open or closed sets. As we will see 
later in this chapter, B n is fundamental to defining random variables. It 
defines a class of subsets of the Euclidean space on which it is reasonable 
to impose a probability structure: the class of every subset would be too 
big while the class of, say, generalized rectangles would be too small. The 
B n is a sufficiently rich class. 
PROBABILITY 
Intuitively speaking, probability is a set function that associates to every 
event a number between 0 and 1. Probability is formally defined by a 
triple (Ω,ℑ,P) called a probability space, where Ω is the set of all possi-
ble outcomes, ℑ the event σ-algebra, and P a probability measure. 
A probability measure P is a set function from ℑ to R (the set of real 
numbers) that satisfies three conditions: 
■ Condition 1. 0 ≤ P(A), for all A ∈ ℑ
 ■ Condition 2. P(Ω) = 1
 ■ Condition 3. P(∪ Ai) = ∑P(Ai) for every finite or countable collection 
of disjoint events {Ai} such that Ai ∈ ℑ 
ℑ does not have to be a σ-algebra. The definition of a probability space 
can be limited to algebras of events. However it is possible to demon-
strate that a probability defined over an algebra of events ℵ can be 
extended in a unique way to the σ-algebra generated by ℵ. 
Two events are said to be independent if: 
P(A ∩ B) = P(A)P(B) 
The (conditional) probability of event A given event B, written as P(A|B), 
is defined as follows: 

171 
Concepts of Probability 
P A  ∩B)
(
B) = ------------------------
P B
P A
( 
(
)
 
It is possible to deduct from simple properties of set theory and from the 
disjoint additivity of probability that 
P(A ∪B) = P(A) + P(B) – P(A ∩B) ≤P(A) + P(B) 
P(A) = 1 – P(AC) 
Bayes theorem is a rule that links conditional probabilities. It can be 
stated in the following way: 
P A
(
)
P A  ∩B) 
P A  ∩B)P A
( 
( 
(
)
(
P A
( 
A)------------
(
)
 
P B
(
)
 
B) = ------------------------ = ------------------------------------- = P B  
P B
(
)
P B
(
)P A
Bayes theorem allows one to recover the probability of the event A 
given B from the probability of the individual events A, B, and the prob-
ability of B given A. 
Discrete probabilities are a special instance of probabilities. Defined 
over a finite or countable set of outcomes, discrete probabilities are non-
zero over each outcome. The probability of an event is the sum of the 
probabilities of its outcomes. In the finite case, discrete probabilities are 
the usual combinatorial probabilities. 
MEASURE 
A measure is a set function defined over an algebra or σ-algebra of sets, 
denumerably additive, and such that it takes value zero on the empty set 
but can otherwise assume any positive value including, conventionally, 
an infinite value. A probability is thus a measure of total mass 1 (i.e., it 
takes value 1 on the set Ω). 
A measure can be formally defined as a function M(A) from an alge-
bra or a σ-algebra ℑto R (the set of real numbers) that satisfies the fol-
lowing three properties:
 ■ Property 1. 0 ≤M(A), for every A ∈ ℑ
 ■ Property 2. M(∅) = 0 

172 
The Mathematics of Financial Modeling and Investment Management
 ■ Property 3. M(∪ Ai) = ∑M(Ai) for every finite or countable collection 
of disjoint events {Ai} such that Ai ∈ ℑ 
If M is a measure defined over a σ-algebra ℑ, the triple (Ω,ℑ,M) is 
called a measure space (this term is not used if ℑ is an algebra). Recall 
that the pair (Ω,ℑ) is a measurable space if ℑ is a σ-algebra. Measures in 
general, and not only probabilities, can be uniquely extended from an 
algebra to the generated σ-algebra. 
RANDOM VARIABLES 
Probability is a set function defined over a space of events; random vari-
ables transfer probability from the original space Ω into the space of 
real numbers. Given a probability space (Ω,ℑ,P), a random variable X is 
a function X(ω) defined over the set Ω that takes values in the set R of 
real numbers such that 
(ω: X(ω) ≤ x) ∈ ℑ 
for every real number x. In other words, the inverse image of any inter-
val (–∞,x] is an event. It can be demonstrated that the inverse image of 
any Borel set is also an event. 
A real-valued set function defined over Ω is said to be measurable 
with respect to a σ-algebra ℑ if the inverse image of any Borel set 
belongs to ℑ. Random variables are real-valued measurable functions. A 
random variable that is measurable with respect to a σ-algebra cannot 
discriminate between events that are not in that σ-algebra. This is the 
primary reason why the abstract and rather difficult concept of measur-
ability is important in probability theory. By restricting the set of events 
that can be identified by a random variable, measurability defines the 
“coarse graining” of information relative to that variable. A random 
variable X is said to generate G if G is the smallest σ-algebra in which it 
is measurable. 
INTEGRALS 
In Chapter 4 on calculus we defined the integral of a real-valued function 
on the real line. However, the notion of the integral can be generalized to 
a general measure space. Though a bit technical, these definitions are 
important in the context of probability theory. 

173 
Concepts of Probability 
For each measure M, the integral is a number that is associated to 
every integrable function f. It is defined in the following two steps:
 ■ Step 1. Suppose that f is a measurable, non-negative function and con-
sider a finite decomposition of the space Ω, that is to say a finite collection 
of disjoint subsets Ai ⊂ Ω whose union is Ω: 
Ai ⊂ Ω such that Ai ∩ Ai = ∅ for i ≠ j and ∪ Ai = Ω 
Consider the sum 
(
): ω ∈ Ai )M Ai
∑inf(f ω
(
)
 
i 
The integral 
f M
d
∫ 
Ω 
is defined as the supremum, if it exists, of all these sums over all possible 
decompositions of Ω. Suppose that f is bounded and non-negative and 
M(Ω) < ∞. Let’s call 
(
)M Ai
S– = sup
∑(inf f ω
(
))

ω ∈ Ai
i 
the lower integral and 
 
(
)M Ai
S+ = inf∑(sup f ω
(
))
 
i ω ∈ Ai 
the upper integral. It can be demonstrated that if the integral exists then 
S+ = S–. It is possible to define the integral as the common value S = S+ = 
S–. This approach is the Darboux-Young approach to integration.7
 ■ Step 2. Given a measurable function f not necessarily non-negative, 
consider its decomposition in its positive and negative parts f = f + – f –. 
The integral of f is defined as the difference, if a difference exists, 
between the integrals of its positive and negative parts. 
7 See Patrick Billingsley, Probability and Measure, Second edition (New York: Wiley, 
1985). 

174 
The Mathematics of Financial Modeling and Investment Management 
The integral can be defined not only on Ω but on any measurable 
set G. In order to define the integral over a measurable set G, consider 
the indicator function IG, which assumes value 1 on each point of the 
set G and 0 elsewhere. Consider now the function f · IG. The integral 
over the set G is defined as 
d 
⋅
f M = ∫ f IG M
d 
∫ 
G 
Ω 
The integral 
f M  is called the indefinite integral of f.
d
∫ 
G 
Given a σ-algebra ℑ, suppose that G and M are two measures and 
that a function f exists such that for A ∈ ℑ 
(
)
 = 
f M
d
G A
∫ 
A 
In this case G is said to have density f with respect to M. 
The integrals in the sense of Riemann and in the sense of Lebesgue-
Stieltjes (see Chapter 4 on calculus) are special instances of this more 
general definition of the integral. Note that the Lebesgue-Stieltjes inte-
gral was defined in Chapter 4 in one dimension. Its definition can be 
extended to n-dimensional spaces. In particular, it is always possible to 
define the Lebesgue-Stieltjes integral with respect to a n-dimensional dis-
tribution function. We omit the definitions which are rather technical.8 
Given a probability space (Ω,ℑ,P) and a random variable X, the 
expected value of X is its integral with respect to the probability measure P 
E[X] = X P
d
∫ 
Ω 
where integration is extended to the entire space. 
DISTRIBUTIONS AND DISTRIBUTION FUNCTIONS 
Given a probability space (Ω,ℑ,P) and a random variable X, consider a set 
A ∈ B 1. Recall that a random variable is a real-valued measurable func-
8 For details, see Yuan Shih Chow and Henry Teicher, Probability Theory: Second 
Edition (New York: Springer, 1988). 

175 
Concepts of Probability 
tion defined over the set of outcomes. Therefore, the inverse image of A, 
X–1(A) belongs to ℑ and has a well-defined probability P(X–1(A)). 
The measure P thus induces another measure on the real axis called 
distribution or distribution law of the random variable X given by: 
µX(A) = P(X–1(A)). It is easy to see that this measure is a probability 
measure on the Borel sets. A random variable therefore transfers the 
probability originally defined over the space Ω to the set of real numbers. 
The function F defined by: F(x) = P(X ≤ x) for x ∈ R is the cumula-
tive distribution function (c.d.f.), or simply distribution function (d.f.), 
of the random variable X. Suppose that there is a function f such that 
x 
( )  = 
f y
d
F x
∫ 
–∞ 
or F′(x) = f(x), then the function f is called the probability density func-
tion of the random variable X. 
RANDOM VECTORS 
After considering a single random variable, the next step is to consider 
not only one but a set of random variables referred to as random vectors. 
Random vectors are formed by n-tuples of random variables. Consider a 
probability space (Ω,ℑ,P). A random variable is a measurable function 
from Ω to R1; a random vector is a measurable function from Ω to Rn . 
We can therefore write a random vector X as a vector-valued function 
f(ω) = [f1(ω) f2(ω) ... fn(ω)] 
Measurability is defined with respect to the Borel σ-algebra B n. It can 
be demonstrated that the function f is measurable ℑ if and only if each 
component function fi(ω) is measurable ℑ. 
Conceptually, the key issue is to define joint probabilities (i.e., the 
probabilities that the n variables are in a given set). For example, con-
sider the joint probability that the inflation rate is in a given interval 
and the economic growth rate in another given interval. 
Consider the Borel σ-algebra B n on the real n-dimensional space Rn . 
It can be demonstrated that a random vector formed by n random vari-
ables Xi, i = 1,2,...,n induces a probability measure over B n. In fact, the 
set (ω ∈ Ω: (X1(ω),X2(ω),...,Xn(ω)) ∈ H; H ∈ B n) ∈ ℑ (i.e., the inverse 
image of every set of the σ-algebra B n belongs to the σ-algebra ℑ). It is 

176 
The Mathematics of Financial Modeling and Investment Management 
therefore possible to induce over every set H that belongs to B n a prob-
ability measure, which is the joint probability of the n random variables 
Xi. The function 
(
(
F x1, …, x ) = P X1 ≤x1, …, X ≤x )
n 
n
n 
where xi ∈R is called the n-dimensional cumulative distribution func-
tion or simply n-dimensional distribution function (c.d.f. or d.f.). Sup-
pose there exists a function f(x1,...,xn) for which the following relationship 
holds: 
x1 
xn 
( 
f u1, …, u )du1…du
F x1, …, xn) = ∫… ∫( 
n
n 
–∞ 
–∞ 
The function f(x1,...,xn) is called the n-dimensional probability density 
function (p.d.f.) of the random vector X. Given a n-dimensional probabil-
ity density function f(x1,...,xn), if we integrate with respect to all variables 
except the j-th variable, we obtain the marginal density of that variable: 
∞
∞ 
y
(
fXj( ) = 
f u1, …, u )du1 ⋅duj – 1duj + 1 ⋅du
∫… ∫ 
n
n 
–∞ 
–∞ 
Given a n-dimensional d.f. we define the marginal distribution func-
y
(
tion with respect to the j-th variable, FX ( ) = P Xj ≤y) as follows: 
j 
Fxj( ) = lim F x1, …, xj – 1 y xj + 1, …, xn)
y
( 
,
 ,
 
xi →∞ 
i
j
≠ 
If the distribution admits a density we can also write 
y 
y
u
FXj( ) = 
fXj( ) u
d 
∫ 
–∞ 
These definitions can be extended to any number of variables. Given 
a n-dimensional p.d.f., if we integrate with respect to k variables 
(xi1, …, xik) over Rk, we obtain the marginal density functions with 
respect to the remaining variables. Marginal distribution functions with 
respect to any subset of variables can be defined taking the infinite limit 
with respect to all other variables. 

177 
Concepts of Probability 
y
Any d.f. FXj( ) defines a Lebesgue-Stieltjes measure and a Lebesgue-
Stieltjes integral. For example, as we have seen in Chapter 4, in the 1-dimen-
sional case, the measure is defined by the differences FXj(
) – FX (xi – 1) .
xi
j
We can now write expectations in two different, and more useful, ways. 
In an earlier section in this chapter, given a probability space (Ω,ℑ,P), we 
defined the expectation of a random variable X as the following integral 
[
] = 
X P
d
E X
∫ 
Ω 
Suppose now that the random variable X has a d.f. FX(u). It can be dem-
onstrated that the following relationship holds: 
∞ 
d 
∫ 
u
[
] = 
X P = 
u F
d X( )
E X
∫ 
Ω 
–∞ 
where the last integral is intended in the sense of Riemann-Stieltjes. If, 
in addition, the d.f. FXj( ) has a density fX u
u
u
( ) = FX 
′ ( ) , then we can 
write the expectation as follows: 
∞
∞ 
E X
∫
d 
∫ 
( ) u
d 
[
] = 
X P = 
u F
d X( ) = 
uf u
u
∫ 
Ω 
–∞ 
–∞ 
where the last integral is intended in the sense of Riemann. More in gen-
eral, given a measurable function g the following relationship holds: 
∞
∞ 
[ (
)] = 
g u
( )f u
E g X
( )dFX( ) = 
g u
( ) u
d 
∫ 
u
∫ 
–∞ 
–∞ 
This latter expression of expectation is the most widely used in practice. 
In general, however, knowledge of the distributions and of distribu-
tion functions of each random variable is not sufficient to determine the 
joint probability distribution function. As we will see later in this chap-
ter, the joint distribution is determined by the marginal distributions 
plus the copula function. 
Two random variables X,Y are said to be independent if 
P(X ∈A,Y ∈B) = P(X ∈A)P(Y ∈B) 

178 
The Mathematics of Financial Modeling and Investment Management 
for all A ∈B , B ∈B . This definition generalizes in obvious ways to any 
number of variables and therefore to the components of a random vec-
tor. It can be shown that if the components of a random vector are inde-
pendent, the joint probability distribution is the product of distributions. 
Therefore, if the variables (X1,...,Xn) are all mutually independent, we 
can write the joint d.f. as a product of marginal distribution functions: 
n 
F x1,
 ,
 
xn) = ∏FX (
)
(
…
j xj
j = 1 
It can also be demonstrated that if a d.f. admits a joint p.d.f., the 
joint p.d.f. factorizes as follows: 
n 
f x1,
 ,
 
xn) = ∏fX (
)
(
…
j xj
j = 1 
Given the marginal p.d.f.s the joint d.f. can be recovered as follows: 
x1 
xn 
(
…
(
…
F x1,
 ,
 
xn) = 
… 
f u1,
 ,
 
un)du1…du
∫
∫ 
n 
–∞ 
–∞ 
x1 
xn
n 
… ∫∏fX (
) du1…du
= ∫ 
j uj
n 
–∞ 
–∞ j = 1 
n 
xj 
uj
fX (
)duj 
= ∏∫
j 
j = 1 –∞ 
n 
= ∏FX (
)
xj
j 
j = 1 
STOCHASTIC PROCESSES 
Given a probability space (Ω,ℑ,P) a stochastic process is a parameterized 
collection of random variables {Xt}, t ∈[0,T] that are measurable with 
respect to ℑ. The parameter t is often interpreted as time. The interval in 
which a stochastic process is defined might extend to infinity in both 
directions. 

179 
Concepts of Probability 
When it is necessary to emphasize the dependence of the random 
variable from both time t and the element ω, a stochastic process is 
explicitly written as a function of two variables: X = X(t,ω). Given ω, 
the function X = Xt(ω) is a function of time that is referred to as the 
path of the stochastic process. 
The variable X might be a single random variable or a multidimen-
sional random vector. A stochastic process is therefore a function X  = 
X(t,ω) from the product space [0,T] × Ω into the n-dimensional real space 
Rn. Because to each ω corresponds a time path of the process—in general 
formed by a set of functions X = Xt(ω)—it is possible to identify the space 
Ω with a subset of the real functions defined over an interval [0,T]. 
Let’s now discuss how to represent a stochastic process X = X(t,ω) 
and the conditions of identity of two stochastic processes. As a stochas-
tic process is a function of two variables, we can define equality as 
pointwise identity for each couple (t,ω). However, as processes are 
defined over probability spaces, pointwise identity is seldom used. It is 
more fruitful to define equality modulo sets of measure zero or equality 
with respect to probability distributions. In general, two random vari-
ables X,Y will be considered equal if the equality X(ω) = Y(ω) holds for 
every ω with the exception of a set of probability zero. In this case, it is 
said that the equality holds almost everywhere (denoted a.e.). 
A rather general (but not complete) representation is given by the 
finite dimensional probability distributions. Given any set of indices 
t1,...,tm, consider the distributions 
H
[(
µt1, …, t (
)
 = P
Xt1, …, Xt ) ∈ H, H ∈ Bn ]
m
m 
These probability measures are, for any choice of the ti, the finite-
dimensional joint probabilities of the process. They determine many, 
but not all, properties of a stochastic process. For example, the finite 
dimensional distributions of a Brownian motion do not determine 
whether or not the process paths are continuous. 
In general, the various concepts of equality between stochastic pro-
cesses can be described as follows:
 ■ Property 1. Two stochastic processes are weakly equivalent if they have 
the same finite-dimensional distributions. This is the weakest form of 
equality.
 ■ Property 2. The process X = X(t,ω) is said to be equivalent or to be a 
modification of the process Y = Y(t,ω) if, for all t, 

180 
The Mathematics of Financial Modeling and Investment Management 
P(Xt = Yt) = 1
 ■ Property 3. The process X = X(t,ω) is said to be strongly equivalent to 
or indistinguishable from the process Y = Y(t,ω) if 
P(Xt = Yt, for all t) = 1 
Property 3 implies Property 2, which in turn implies Property 1. 
Implications do not hold in the opposite direction. Two processes hav-
ing the same finite distributions might have completely different paths. 
However it is possible to demonstrate that if one assumes that paths are 
continuous functions of time, Properties 2 and 3 become equivalent. 
PROBABILISTIC REPRESENTATION OF FINANCIAL MARKETS 
We are now in the position to summarize the probabilistic representation 
of financial markets. From a financial point of view, an asset is a contract 
which gives the right to receive a distribution of future cash flows. In the 
case of a common stock, the stream of cash flows will be uncertain. It 
includes the common stock dividends and the proceeds of the eventual 
liquidation of the firm. A debt instrument is a contract that gives its 
owner the right to receive periodic interest payments and the repayment 
of the principal by the maturity date. Except in the case of debt instru-
ments of governments whose risk of default is perceived as extremely 
low, payments are uncertain as the issuing entity might default. 
Suppose that all payments are made at the trading dates and that no 
transactions take place between trading dates. Let’s assume that all 
assets are traded (i.e., exchanged on the market) at either discrete fixed 
dates, variable dates or continuously. At each trading date there is a 
market price for each asset. Each asset is therefore modeled with two 
time series, a series of market prices and a series of cash flows. As both 
series are subject to uncertainty, cash flows and prices are time-depen-
dent random variables (i.e., they are stochastic processes). The time 
dependence of random variables in this probabilistic setting is a delicate 
question and will be examined shortly. 
Following Kenneth Arrow9 and using a framework now standard, 
the economy and the financial markets in a situation of uncertainty are 
described with the following basic concepts: 
9 Kenneth Arrow, “The Role of Securities in the Optimal Allocation of Risk Bear-
ing,” Review of Economic Studies (April 1964), pp. 91–96. 

181
Concepts of Probability 
■ It is assumed that the economy is in one of the states of a probability 
space (Ω,ℑ,P).
 ■ Every security is described by two stochastic processes formed by two 
time-dependent random variables St(ω) and dt(ω) representing prices 
and cash flows of the asset. 
This representation is completely general and is not linked to the 
assumption that the space of states is finite. 
INFORMATION STRUCTURES 
Let’s now turn our attention to the question of time. The previous dis-
cussion considered a space formed by states in an abstract sense. We 
must now introduce an appropriate representation of time as well as 
rules that describe the evolution of information, that is, information 
propagation, over time. The concepts of information and information 
propagation are fundamental in economics and finance theory. 
The concept of information in finance is different from both the 
intuitive notion of information and that of information theory in which 
information is a quantitative measure related to the a priori probability 
of messages.10 In our context, information means the (progressive) reve-
lation of the set of events to which the current state of the economy 
belongs. Though somewhat technical, this concept of information sheds 
light on the probabilistic structure of finance theory. The point is the 
following. Assets are represented by stochastic processes, that is, time-
dependent random variables. But the probabilistic states on which these 
random variables are defined represent entire histories of the economy. 
To embed time into the probabilistic structure of states in a coherent 
way calls for information structures and filtrations (a concept we 
explain in the next section). 
Recall that it is assumed that the economy is in one of many possible 
states and that there is uncertainty on the state that has been realized. 
Consider a time period of the economy. At the beginning of the period, 
there is complete uncertainty on the state of the economy (i.e., there is 
complete uncertainty on what path the economy will take). Different 
events have different probabilities, but there is no certainty. As time 
passes, uncertainty is reduced as the number of states to which the econ-
10 There is indeed a deep link between information theory and econometrics embod-
ied in concepts such as the Fisher Information Matrix, see Chapter 12. 

182 
The Mathematics of Financial Modeling and Investment Management 
omy can belong is progressively reduced. Intuitively, revelation of infor-
mation means the progressive reduction of the number of possible states; 
at the end of the period, the realized state is fully revealed. In continuous 
time and continuous states, the number of events is infinite at each 
instant. Thus its cardinality remains the same. We cannot properly say 
that the number of events shrinks. A more formal definition is required. 
The progressive reduction of the set of possible states is formally 
expressed in the concepts of information structure and filtration. Let’s 
start with information structures. Information structures apply only to 
discrete probabilities defined over a discrete set of states. At the initial 
instant T0, there is complete uncertainty on the state of the economy; 
the actual state is known only to belong to the largest possible event 
(that is, the entire space Ω). At the following instant T1, assuming that 
instants are discrete, the states are separated into a partition, a partition 
being a denumerable class of disjoint sets whose union is the space 
itself. The actual state belongs to one of the sets of the partitions. The 
revelation of information consists in ruling out all sets but one. For all 
the states of each partition, and only for these, random variables assume 
the same values. 
Suppose, to exemplify, that only two assets exist in the economy 
and that each can assume only two possible prices and pay only two 
possible cash flows. At every moment there are 16 possible price-cash 
flow combinations. We can thus see that at the moment T1 all the states 
are partitioned into 16 sets, each containing only one state. Each parti-
tion includes all the states that have a given set of prices and cash distri-
butions at the moment T1. The same reasoning can be applied to each 
instant. The evolution of information can thus be represented by a tree 
structure in which every path represents a state and every point a parti-
tion. Obviously the tree structure does not have to develop as symmetri-
cally as in the above example; the tree might have a very generic 
structure of branches. 
FILTRATION 
The concept of information structure based on partitions provides a 
rather intuitive representation of the propagation of information through 
a tree of progressively finer partitions. However, this structure is not suffi-
cient to describe the propagation of information in a general probabilistic 
context. In fact, the set of possible events is much richer than the set of 
partitions. It is therefore necessary to identify not only partitions but also 
a structure of events. The structure of events used to define the propaga-

183 
Concepts of Probability 
tion of information is called a filtration. In the discrete case, however, the 
two concepts—information structure and filtration—are equivalent. 
The concept of filtration is based on identifying all events that are 
known at any given instant. It is assumed that it is possible to associate 
to each trading moment t a σ-algebra of events ℑt ⊂ ℑ formed by all 
events that are known prior to or at time t. It is assumed that events are 
never “forgotten,” that is, that ℑt ⊂ ℑs, if t < s. An ordering of time is 
thus created. This ordering is formed by an increasing sequence of σ-
algebras, each associated to the time at which all its events are known. 
This sequence is a filtration. Indicated as {ℑt}, a filtration is therefore an 
increasing sequence of all σ-algebras ℑt, each associated to an instant t. 
In the finite case, it is possible to create a mutual correspondence 
between filtrations and information structures. In fact, given an infor-
mation structure, it is possible to associate to each partition the algebra 
generated by the same partition. Observe that a tree information struc-
ture is formed by partitions that create increasing refinement: By going 
from one instant to the next, every set of the partition is decomposed. 
One can then conclude that the algebras generated by an information 
structure form a filtration. 
On the other hand, given a filtration {ℑt}, it is possible to associate a 
partition to each ℑt. In fact, given any element that belongs to Ω, con-
sider any other element that belongs to Ω such that, for each set of ℑt, 
both either belong to or are outside this set. It is easy to see that classes 
of equivalence are thus formed, that these create a partition, and that 
the algebra generated by each such partition is precisely the ℑt that has 
generated the partition. 
A stochastic process is said to be adapted to the filtration {ℑt} if the 
variable Xt is measurable with respect to the σ-algebra ℑt. It is assumed 
that the price and cash distribution processes St(ω) and dt(ω) of every 
asset are adapted to {ℑt}. This means that, for each t, no measurement 
of any price or cash distribution variable can identify events not 
included in the respective algebra or σ-algebra. Every random variable 
is a partial image of the set of states seen from a given point of view and 
at a given moment. 
The concepts of filtration and of processes adapted to a filtration 
are fundamental. They ensure that information is revealed without 
anticipation. Consider the economy and associate at every instant a par-
tition and an algebra generated by the partition. Every random variable 
defined at that moment assumes a value constant on each set of the par-
tition. The knowledge of the realized values of the random variables 
does not allow identifying sets of events finer than partitions. 
One might well ask: Why introduce the complex structure of σ-alge-
bras as opposed to simply defining random variables? The point is that, 

184 
The Mathematics of Financial Modeling and Investment Management 
from a logical point of view, the primitive concept is that of states and 
events. The evolution of time has to be defined on the primitive struc-
ture—it cannot simply be imposed on random variables. In practice, fil-
trations become an important concept when dealing with conditional 
probabilities in a continuous environment. As the probability that a 
continuous random variable assumes a specific value is zero, the defini-
tion of conditional probabilities requires the machinery of filtration. 
CONDITIONAL PROBABILITY AND CONDITIONAL EXPECTATION 
Conditional probabilities and conditional averages are fundamental in 
the stochastic description of financial markets. For instance, one is gen-
erally interested in the probability distribution of the price of an asset at 
some date given its price at an earlier date. The widely used regression 
models are an example of conditional expectation models. 
The conditional probability of event A given event B was defined 
earlier as 
P A ∩B)
(
P A
( 
B) = ------------------------
P B
(
)
 
This simple definition cannot be used in the context of continuous ran-
dom variables because the conditioning event (i.e., one variable assum-
ing a given value) has probability zero. To avoid this problem, we 
condition on σ-algebras and not on single zero-probability events. In 
general, as each instant is characterized by a σ-algebra ℑ, the condition-
t
ing elements are the ℑt. 
The general definition of conditional expectation is the following. 
Consider a probability space (Ω,ℑ,P) and a σ-algebra G contained in ℑ 
and suppose that X is an integrable random variable on (Ω,ℑ,P). We 
define the conditional expectation of X with respect to G, written as 
E[X|G], as a random variable measurable with respect to G such that 
E X
[ 
G]dP = 
X P
d
∫ 
∫ 
G
G 
for every set G ∈G. In other words, the conditional expectation is a 
random variable whose average on every event that belongs to G is 
equal to the average of X over those same events, but it is G-measurable 

185 
Concepts of Probability 
while X is not. It is possible to demonstrate that such variables exist and 
are unique up to a set of measure zero. 
Econometric models usually condition a random variable given 
another variable. In the previous framework, conditioning one random 
variable X with respect to another random variable Y means condition-
ing X given σ{Y} (i.e., given the σ-algebra generated by Y). Thus E[X|Y] 
means E[X|σ{Y}]. 
This notion might seem to be abstract and to miss a key aspect of 
conditioning: intuitively, conditional expectation is a function of the 
conditioning variable. For example, given a stochastic price process, X ,t
one would like to visualize conditional expectation E[X Xs], s < t as a
t
function of Xs that yields the expected price at a future date given the 
present price. This intuition is not wrong insofar as the conditional 
expectation E[XY] of X given Y is a random variable function of Y. 
For example, the regression function that will be explained later in this 
chapter is indeed a function that yields the conditional expectation. 
However, we need to specify how conditional expectations are 
formed, given that the usual conditional probabilities cannot be applied 
as the conditioning event has probability zero. Here is where the above 
definition comes into play. The conditional expectation of a variable X 
given a variable Y is defined in full generality as a variable that is measur-
able with respect to the σ-algebra σ(Y) generated by the conditioning 
variable Y and has the same expected value of Y on each set of σ(Y). Later 
in this section we will see how conditional expectations can be expressed 
in terms of the joint p.d.f. of the conditioning and conditioned variables. 
One can define conditional probabilities starting from the concept 
of conditional expectations. Consider a probability space (Ω,ℑ,P), a sub-
σ-algebra G of ℑ, and two events A ∈ ℑ, B ∈ ℑ. If IA,IB are the indicator 
functions of the sets A,B (the indicator function of a set assumes value 1 
on the set, 0 elsewhere), we can define conditional probabilities of the 
event A, respectively, given G or given the event B as 
P(AG) = E[IAG] 
P(AB) = E[IAIB] 
Using these definitions, it is possible to demonstrate that given two ran-
dom variables X and Y with joint density f(x,y), the conditional density 
of X given Y is 
f x  y  )
( ,
f x
( y) = ---------------
fY y
( )  
where the marginal density, defined as 

186 
The Mathematics of Financial Modeling and Investment Management 
∞ 
fY y
( ,
( ) = 
f x y  )dx
∫ 
–∞ 
is assumed to be strictly positive. 
In the discrete case, the conditional expectation is a random variable 
that takes a constant value over the sets of the finite partition associated 
to ℑt. Its value for each element of Ωis defined by the classical concept of 
conditional probability. Conditional expectation is simply the average 
over a partition assuming the classical conditional probabilities. 
An important econometric concept related to conditional expecta-
tions is that of a martingale. Given a probability space (Ω,ℑ,P) and a fil-
tration {ℑ}, a sequence of ℑi-measurable random variables Xi is called a
t
martingale if the following condition holds: 
[ 
ℑ] =
E Xi + 1 
i 
Xi 
A martingale translates the idea of a “fair game” as the expected value 
of the variable at the next period is the present value of the same value. 
MOMENTS AND CORRELATION 
If X is a random variable on a probability space (Ω,ℑ,P), the quantity 
p
E X
[ 
] , p > 0 is called the p-th absolute moment of X. If k is any posi-
tive integer, E[Xk], if it exists, is called the k-th moment. In the general 
case of a probability measure P we can therefore write:
p P
■ E X
[ 
p] = 
X d , p > 0, is the p-th absolute moment.
∫ 
Ω 
■ E Xk] = 
XkdP , if it exists for k positive integer, is the k-th moment. 
[ 
∫ 
Ω 
In the case of discrete probabilities pi, Σpi = 1 the above expressions 
become 
p
E X
[ 
p] = ∑ 
p
xi 
i 
and 

187 
Concepts of Probability 
[ 
k
E Xk] = ∑x pi
i 
respectively. If the variable X is continuous and has a density p(x) such 
that 
∞ 
p x
( )dx = 1
∫ 
–∞ 
we can write 
∞ 
∫ 
p
E X
[ 
p] = 
x p x
( )dx
–∞ 
and 
∞ 
E Xk] = 
x p x
[ 
( )dx
∫
k 
–∞ 
respectively. 
The centered moments are the moments of the fluctuations of the 
variables around its mean. For example, the variance of a variable X is 
defined as the centered moment of second order: 
(
) = σ2 = σ (
) = E
X
 X
 
) ]
var X
2 X
[( 
– 
2 
x 
∞
∞ 
∞ 
2 
(x
X)
2 p x
( )dx –
– 
( )dx = 
x 2 p x
xp x
( )dx
= ∫
∫ 
∫ 
–∞ 
–∞ 
–∞ 
where X = E X
[
] . 
The positive square root of the variance, σ
is called the standard
x
deviation of the variable. 
We can now define the covariance and the correlation coefficient of 
a variable. Correlation is a quantitative measure of the strength of the 
dependence between two variables. Intuitively, two variables are depen-
dent if they move together. If they move together, they will be above or 
below their respective means in the same state. Therefore, in this case, 
the product of their respective deviations from the means will have a 
positive mean. We call this mean the covariance of the two variables. 

188 
The Mathematics of Financial Modeling and Investment Management 
The covariance divided by the product of the standard deviations is a 
dimensionless number called the correlation coefficient. 
Given two random variables X,Y with finite expected values and 
finite variances, we can write the following definitions:
 ■ cov(X Y) = 
, 
= E
X
 X
 
)(Y
Y)] is the covariance of X,Y.
, 
[( 
–
–
σX Y
σX Y
, 
, 
■ ρX Y = ------------- is the correlation coefficient of X,Y. 
σXσY 
The correlation coefficient can assume values in the interval [–1,1]. 
If two variables X,Y are independent, their correlation coefficient van-
ishes. However, uncorrelated variables, that is, variables whose correla-
tion coefficient is zero, are not necessarily independent. 
It can be demonstrated that the following property of variances holds: 

 
 
i 
(
) + ∑cov(Xi, Xj)
var∑X = ∑var Xi
i
i 
i
j
≠ 
Further, it can be demonstrated that the following properties hold: 
[ 
[
]E Y
= E XY] – E X
[
]
σX Y
, 
= σY X
σX Y
,
, 
= abσY X
σaX bY 
,
, 
σX
Y, Z = σX Z + σY Z
+ 
,
, 

 
cov∑a Xi, ∑bjYj= ∑∑aibjcov(Xi, Yj)
 
i

i
i 
i
j 
COPULA FUNCTIONS 
Understanding dependences or functional links between variables is a 
key theme of modern econometrics. In general terms, functional depen-
dences are represented by dynamic models. As we will see in Chapter 
11, many important models are linear models whose coefficients are 

189 
Concepts of Probability 
correlations coefficients. In many instances, in particular in risk man-
agement, it is important to arrive at a quantitative measure of the 
strength of dependencies. 
The correlation coefficient provides such a measure. In many instances, 
however, the correlation coefficient might be misleading. In particular, there 
are cases of nonlinear dependencies that result in a zero correlation coeffi-
cient. From the point of view of risk management this situation is particu-
larly dangerous as it leads to substantially underestimated risk. 
Different measures of dependence have been proposed, in particular 
copula functions. We will give only a brief introduction to copula func-
tions.11 Copula functions are based on the Theorem of Sklar. Sklar dem-
onstrated12 that any joint probability distribution can be written as a 
functional link, i.e., a copula function, between its marginal distribu-
tions. Let’s suppose that F(x1,x2,...,xn) is a joint multivariate distribu-
tion function with marginal distribution functions F1(x1), F2(x2), ..., 
Fn(xn). Then there is a copula function C such that the following rela-
tionship holds: 
F x1,
 ,
 ,
 
x ) = C F1 x1
(
),
 
,
 
F (
)]
( 
x2 …
[
(
), F2 x2
…
x
n 
n
n
The joint probability distribution contains all the information 
related to the co-movement of the variables. The copula function allows 
to capture this information in a synthetic way as a link between mar-
ginal distributions. We will see an application of the concept of copula 
functions in Chapter 22 on credit risk modeling. 
SEQUENCES OF RANDOM VARIABLES 
Consider a probability space (Ω,ℑ,P). A sequence of random variables is an 
infinite family of random variables Xi on (Ω,ℑ,P) indexed by integer num-
bers: i = 0,1,2,...,n... If the sequence extends to infinity in both directions, it 
is indexed by positive and negative integers: i = ...,–n,..., 0,1,2,...,n....
 A sequence of random variables can converge to a limit random 
variable. Several different notions of the limit of a sequence of random 
variables can be defined. The simplest definition of convergence is that 
11 The interested reader might consult the following reference: P. Embrechts, F. Lind-
skog, and A. McNeil, “Modelling Dependence with Copulas and Applications to 
Risk Management,” Chapter 8 in S.T. Rachev (ed.), Handbook of Heavy Tailed Dis-
tributions in Finance (Amsterdam: North Holland, 2003). 
12 A. Sklar, “Random Variables, Joint Distribution Functions and Copulas,” Kyber-
netika 9 (1973), pp. 449–460. 

190 
The Mathematics of Financial Modeling and Investment Management 
of pointwise convergence. A sequence of random variables Xi, i ≥1 on 
(Ω,ℑ,P), is said to converge almost surely to a random variable X, 
denoted 
a.s. 
Xi →X 
if the following relationship holds: 
(
) = X ω
P{ω: lim Xi ω
(
)} = 1 
i →∞ 
In other words, a sequence of random variables converges almost surely 
to a random variable X if the sequence of real numbers Xi(ω) converges 
to X(ω) for all ω except a set of measure zero. 
A sequence of random variables Xi, i ≥1 on (Ω,ℑ,P), is said to con-
verge in mean of order p to a random variable X if 
p
[ 
(
) – X ω
lim E Xi ω
(
) ] = 0 
i →∞ 
provided that all expectations exist. Convergence in mean of order one 
and two are called convergence in mean and convergence in mean 
square, respectively. 
A weaker concept of convergence is that of convergence in probabil-
ity. A sequence of random variables Xi, i ≥1 on (Ω,ℑ,P), is said to con-
verge in probability to a random variable X, denoted 
P 
Xi →X 
if the following relationship holds: 
lim P{ω: 
(
) – X ω
Xi ω
(
) ≤ε} = 1 , ∀ε > 0 
i →∞ 
It can be demonstrated that if a sequence converges almost surely 
then it also convergences in probability while the converse is not gener-
ally true. It can also be demonstrated that if a sequence converges in 
mean of order p > 0, then it also convergences in probability while the 
converse is not generally true. 
A sequence of random variables Xi, i ≥1 on (Ω,ℑ,P) with distribution 
functions FXi is said to converge in distribution to a random variable X 
with distribution function FX, denoted 

191 
Concepts of Probability 
d 
Xi →X 
if 
x
( )
∈ 
, 
C
lim FXi( ) = FX x
x 
i →∞ 
where C is the set of points where all the functions FXi and FX are con-
tinuous. 
It can be demonstrated that if a sequence converges almost surely 
(and thus converges in probability) it also converges in distribution 
while the converse is not true in general. 
INDEPENDENT AND IDENTICALLY DISTRIBUTED SEQUENCES 
Consider a probability space (Ω,ℑ,P). A sequence of random variables Xi 
on (Ω,ℑ,P) is called a sequence of independent and identically distributed 
(IID) sequence if the variables Xi have all the same distribution and are 
all mutually independent. An IID sequence is the strongest form of white 
noise, that is, of a completely random sequence of variables. Note that in 
many applications white noise is defined as a sequence of uncorrelated 
variables. This is a weaker definition as an uncorrelated sequence might 
be forecastable. 
An IID sequence is completely unforecastable in the sense that the 
past does not influence the present or the future in any possible sense. In 
an IID sequence all conditional distributions are identical to uncondi-
tional distributions. Note, however, that an IID sequence presents a sim-
ple form of reversion to the mean. In fact, suppose that a sequence Xi 
assumes at a given time t a value larger than the common mean of all 
variables: Xt > E[X]. By definition of mean it is more likely that Xt be 
followed by a smaller value: P(Xt+1 < Xt) > P(Xt+1 > Xt). 
Note that this type of mean reversion does not imply forecastability 
as the probability distribution of asset returns at time t + 1 is indepen-
dent from the distribution at time t. 
SUM OF VARIABLES 
Given two random variables X(ω), Y(ω) on the same probability space 
(Ω,ℑ,P), the sum of variables Z(ω) = X(ω) + Y(ω) is another random 
variable. The sum associates to each state ω a value Z(ω) equal to the 

192 
The Mathematics of Financial Modeling and Investment Management 
sum of the values taken by the two variables X,Y. Let’s suppose that the 
two variables X(ω), Y(ω) have a joint density p(x,y) and marginal densi-
ties pX(x) and pY(x), respectively. Let’s call H the cumulative distribu-
tion of the variable Z. The following relationship holds 
H u
[ (
) ≤u] = 
p x  y  )d
y
( ) = P Z  ω
( , 
xd
∫∫ 
A 
A = {y ≤–x + u} 
In other words, the probability that the sum X + Y be less than or equal 
to a real number u is given by the integral of the joint probability distri-
bution function in the region A. The region A can be described as the 
region of the x,y plane below the straight line y = –x + u. 
If we assume that the two variables are independent, then the distri-
bution of the sum admits a simple representation. In fact, under the 
assumption of independence, the joint density is the product of the mar-
ginal densities: p(x,y) = pX(x)pY(x). Therefore, we can write 
∞
u
y
– 

( ) = P Z  ω
( , 
xd 
( ) x
d pY y
H u
[ (
) ≤u] = ∫∫p x  y  )d
y = ∫
∫pX x
( ) y
d 

A 
–∞ 
–∞ 
We can now use a property of integrals called the Leibnitz rule, 
which allows one to write the following relationship: 
∞ 
dH 
( ) = 
pX(u
y)pY y
-------- = pZ u
– 
( ) y
d 
∫
du 
–∞ 
Recall from Chapter 4 that the above formula is a convolution of 
the two marginal distributions. This formula can be reiterated for any 
number of summands: the density of the sum of n random variables is 
the convolution of their densities. 
Computing directly the convolution of a number of functions might 
be very difficult or impossible. However, if we take the Fourier transforms 
of the densities, PZ(s), PX(s), PY(s) computations are substantially simpli-
fied as the transform of the convolution is the product of the transforms: 
∞ 
pZ u
– 
( ) y
d ⇒PZ s
( ) × PY s
( ) = 
pX(u
y)pY y
( ) = PX s
( )
∫ 
–∞ 

193 
Concepts of Probability 
This relationship can be extended to any number of variables. 
In probability theory, given a random variable X, the following 
expectation is called the characteristic function (c.f.) of the variable X 
ϕX t
[
( ) = E eitX] = E[cos tX
 
] + iE[sin tX] 
If the variable X admits a d.f. FX(y), it can be demonstrated that the 
following relationship holds: 
∞
∞ 
∞ 
∫
itX
ϕX t
[ 
x
x
( ) = E eitX] = 
e 
dFX( ) = 
cos tx dFX( ) + ∫sin tx dFX( )
x
∫ 
–∞ 
–∞ 
–∞ 
In this case, the characteristic function therefore coincides with the Fou-
rier-Stieltjes transform. It can be demonstrated that there is a one-to-one 
correspondence between c.d.s and d.f.s. In fact, it is well known that the 
Fourier-Stieltjes transform can be uniquely inverted. 
In probability theory convolution is defined, in a more general way, 
as follows. Given two d.f.s FX(y) and FY(y), their convolution is defined 
as: 
∞ 
F* u
u
∫ 
– 
( )
( ) = (FX*FY)( ) = 
FX(u
y)dFY y
–∞ 
It can be demonstrated that the d.f. of the sum of two variables X,Y 
with d.f.s FX(y) and FY(y) is the convolution of their respective d.f.s: 
∞ 
( 
u
( ) = (FX*FY)( ) = 
FX(u
y)dFY y
P X  + Y ≤u) = 
( ) = F* u
– 
( )
+
FX
Y
u
∫ 
–∞ 
If the d.f.s admits p.d.f.s, then the inversion formulas are those estab-
lished earlier. Inversion formulas also exist in the case that the d.f.s do 
not admit densities but these are more complex and will not be given 
here.13 
We can therefore establish the following property: the characteristic 
function of the sum of n independent random variables is the product of 
the characteristic functions of each of the summands. 
13 See Chow and Teicher, Probability Theory. 

194 
The Mathematics of Financial Modeling and Investment Management 
GAUSSIAN VARIABLES 
Gaussian random variables are extremely important in probability the-
ory and statistics. Their importance stems from the fact that any phe-
nomenon made up of a large number of independent or weakly 
dependent variables has a Gaussian distribution. Gaussian distributions 
are also known as normal distributions. The name Gaussian derives 
from the German mathematician Gauss who introduced them. 
Let’s start with univariate variables. A normal variable is a variable 
whose probability distribution function has the following form: 

 
1 
(x – µ)2  
f x
( 
,
µ σ2) = --------------exp– -------------------  
2σ2 
σ 2π
 

 
The univariate normal distribution is a distribution characterized by 
only two parameters, (µ,σ2), which represent, respectively, the mean and 
the variance of the distribution. We write X ∼N(µ,σ2) to indicate that 
the variable X has a normal distribution with parameters (µ,σ2). We 
define the standard normal distribution as the normal distribution with 
zero mean and unit variance. It can be demonstrated by direct calcula-
tion that if X ∼N(µ,σ2) then the variable 
X – µ
Z = -------------
σ 
is standard normal. The variable Z is called the score or Z-score. The 
cumulative distribution of a normal variable is generally indicated as 
– µ 
F x
------------
( ) = Φ
x 

σ  
where Φ(x) is the cumulative distribution of the standard normal. 
It can be demonstrated that the sum of n independent normal distribu-
tions is another normal distribution whose expected value is the sum of 
the expected values of the summands and whose variance is the sum of the 
variances of the summands. 
The normal distribution has a typical bell-shaped graph symmetrical 
around the mean. Exhibit 6.1 shows the graph of a normal distribution. 

195 
Concepts of Probability 
EXHIBIT 6.1 
Graph of a Normal Variable with Zero Mean and σ = 100 
Multivariate normal distributions are characterized by the same 
exponential functional form. However, a multivariate normal distribu-
tion in n variables is identified by n means, one for each axis, and by a 
n×n symmetrical variance-covariance matrix. For instance, a bivariate 
normal distribution is characterized by two expected values, two vari-
ances and one covariance. We can write the general expression of a 
bivariate normal distribution as follows: 
 1 
 
exp – --Q 
 2 

( ,
f x y) = -----------------------------------------
2πσXσY 1 – ρ2 
1 
 x – µX2 
 x – µX y – µY
 y – µY2  
Q = -------------- --------------- – 2ρ --------------- --------------- +  --------------- 
σX  

σX  σY  

σY 
1 – ρ2 
where ρ is the correlation coefficient.  

196 
The Mathematics of Financial Modeling and Investment Management 
This expression generalizes to the case of n random variables. Using 
matrix notation, the joint normal probability distributions of the random 
n vector V = {Xi}, i = 1,2,...,n has the following expression: 
V = {
} ∼N (µ Σ)
Xi
n 
, 
where 
µ = E Xi
[
]
i 
and Σ is the variance-covariance matrix of the {Xi} 
Σ = E[(V – µ)(V – µ)T] 
–¹₂
f v
( ) = [(2π)n Σ ]
exp[(–¹₂)(v – µ)TΣ–1(v – µ)] 
where Σ = detΣ , the determinant of Σ. 
For n = 2 we find the previous expression for bivariate normal, tak-
ing into account that variances and correlation coefficients have the fol-
lowing relationship 
σij = ρijσiσj 
It can be demonstrated that a linear combination 
n 
W = ∑αiXi 
i = 1 
of n jointly normal random variables Xi ∼N(µi, σ2) with cov(Xi,Xj) =
i 
∼ 
W) where
σij is a normal random variable W
N(µW, σ2 
n 
µ
= ∑αiµ
W
i 
i = 1 
n
n 
2
σW = ∑∑αiαjσij 
i = 1 j = 1 

197 
Concepts of Probability 
THE REGRESSION FUNCTION 
Given a probability space (Ω,ℑ,P), consider a set of p + 1 random variables. 
Let’s suppose that the random vector {X Z1 ... Zp} ≡{X Z}, Z = {Z1 ... Z }
p
has the joint multivariate probability density function: 
f xz1…zp) = f x, z) , z = {z1…zp}
(
( 
Let’s consider the conditional density 
f x
( z1, …, zp) = f x,
( 
z) 
and the marginal density of Z, 
∞ 
(
( ) = 
f x, z)dx
fz z
∫ 
–∞ 
Recall from an earlier section that the joint multivariate density f(x,z) 
factorizes as 
f x, z) = f x
(
( z)f ( )
z
z 
Let’s consider now the conditional expectation of the variable X given Z 
= z = {z1 ... zp}: 
∞ 
( ) = E X
g z
[ 
Z = z] = 
vf v
( z)dv
∫ 
–∞ 
The function g, that is, the function which gives the conditional expec-
tation of X given the variables Z, is called the regression function. Oth-
erwise stated, the regression function is a real function of real variables 
which is the locus of the expectation of the random variable X given 
that the variables Z assume the values z. 
Linear Regression 
In general, the regression function depends on the joint distribution of 
[X Z1 ... Zp]. In financial econometrics it is important to determine 
what joint distributions produce a linear regression function. It can be 

198 
The Mathematics of Financial Modeling and Investment Management 
demonstrated that joint normal distributions produce a linear regression 
function. Consider the joint normal distribution 
1 
– --
1
f v
( ) = [(2π)n Σ ]
2exp – --(v – µ)TΣ–1(v – µ)
2 
where parameters are those defined in an earlier section in this chapter. 
Let’s partition the parameters as follows: 



 
σ
σ

x 
µx 
x x
z, x
,
v = , µ = 
, Σ = 
 
z
µ
 


 
σx, z Σz 
z
where µ , µz are respectively a scalar and a p-vector of expected values,
x
σx,x, σx,z, σz,x, and Σz are respectively a scalar, p-vectors and a p×p
2
matrix of variances and covariances and σx x = σ2 , σzi, zi = σ . It can 
, 
x 
zi
be demonstrated that the variable (X|Z = z) is normally distributed with 
the following parameters: 
–1
(X Z = z) ∼N[µx – (Σ–1σz, x)' (µ – z), σx x – σx, zΣz σ
+]
z
z 
, 
z, x 
From the above expression we can conclude that the conditional 
expectation is linear in the conditioning variables. Let’s call 
α = µx – (Σ– 
z 
1σz, x)' µ  and β = Σz 
–1σz, x
z 
We can therefore write 
( ) = E X
g z
[ 
Z = z] = α 
β′z
+ 
If the matrix Σ is diagonal, the random variables (X,Z1,...,Zp) are 
independent, such that σz,x = 0 and β = Σz 
–1σ
= 0 and therefore the
z, x 
regression function is a constant that does not depend on the condition-
ing variables. If the matrix Σz is diagonal but σ ,z, σz,x do not vanish,
x
then the linear regression takes the following form 
p
p
σ
σ
, i 
x z
x z
, i
( ) = E X
g z
[ 
Z = z] = µ – ∑-----------µ
+ ∑-----------zi
x 
i = 1 σ2 
zi 
i = 1 σ2 
zi 
zi 

199 
Concepts of Probability 
In particular, a bivariate normal distribution factorizes in a linear 
regression as follows: 
)2
σ
(σ ,
x z
x z
,
(X Z = z) ∼N µ – ----------(µ – z), σ2 – -----------------
x 
z 
x 
σ2 
σ2 
z
z 
σ
σ
x z
x z
,
,
( ) = E X
g z
[ 
Z = z] = µx – ----------µ + ----------z
z 
σ2 
σ2 
z
z 
SUMMARY
 ■ Probability is a set function defined over a class of events where events 
are sets of possible outcomes of an experiment. A probability space is a 
triple formed by a set of outcomes, a σ-algebra of events, and a proba-
bility measure.
 ■ A random variable is a real-valued function defined over the set of out-
comes such that the inverse image of any interval is an event. n-dimen-
sional random vectors are functions from the set of outcomes into the 
n-dimensional Euclidean space with the property that the inverse image 
of n-dimensional generalized rectangles is an event.
 ■ Stochastic processes are time-dependent random variables.
 ■ An information structure is a collection of partitions of events associ-
ated to each instant of time that become progressively finer with the 
evolution of time. A filtration is an increasing collection of σ-algebras 
associated to each instant of time.
 ■ The states of the economy, intended as full histories of the economy, 
are represented as a probability space. The revelation of information 
with time is represented by information structures or filtrations. Prices 
and other financial quantities are represented by adapted stochastic 
processes.
 ■ By conditioning is meant the change in probabilities due to the acqui-
sition of some information. It is possible to condition with respect to 
an event if the event has nonzero probability. In general terms, condi-
tioning means conditioning with respect to a filtration or an informa-
tion structure.
 ■ A martingale is a stochastic process such that the conditional expected 
value is always equal to its present value. It embodies the idea of a fair 
game where today’s wealth is the best forecast of future wealth. 

200 
The Mathematics of Financial Modeling and Investment Management
 ■ The variance of a random variable measures the average size of its fluc-
tuations around the mean.
 ■ The correlation coefficient between two variables is a number that 
measures how the two variables move together. It is zero for inde-
pendent variables, plus/minus one for linearly dependent determin-
istic variables. 
■ An infinite sequence of random variables might converge to a limit ran-
dom variable. Different types of convergence can be defined: pointwise 
convergence, convergence in probability, or convergence in distribu-
tion.
 ■ Random variables can be added to produce another random variable. 
■ The characteristic function of the sum of two random variables is the 
product of the characteristic functions of each random variable.
 ■ Given a multivariate distribution, the regression function of one ran-
dom variable with respect to the others is the conditional expectation 
of that random variable given the values of the others.
 ■ Joint normal distributions admits a linear regression function. 

