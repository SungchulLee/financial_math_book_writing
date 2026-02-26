# Bayesian Methods: Foundations & Regression

!!! info "Source"
    **Bayesian Methods in Finance** by Svetlozar T. Rachev, John S.J. Hsu, Biliana S. Bagasheva, and Frank J. Fabozzi, Wiley, 2008.
    These notes are used for educational purposes.

## Introduction to Bayesian Methods

CHAPTER1
Introduction
Q
uantitative financial models describe in mathematical terms the relation-
ships between financial random variables through time and/or across
assets. The fundamental assumption is that the model relationship is valid
independent of the time period or the asset class under consideration.
Financial data contain both meaningful information and random noise. An
adequate financial model not only extracts optimally the relevant informa-
tion from the historical data but also performs well when tested with new
data. The uncertainty brought about by the presence of data noise makes
imperative the use of statistical analysis as part of the process of financial
model building, model evaluation, and model testing.
Statistical analysis is employed from the vantage point of either
of the two main statistical philosophical traditions—‘‘frequentist’’ and
‘‘Bayesian.’’ An important difference between the two lies with the inter-
pretation of the concept of probability. As the name suggests, advocates of
frequentist statistics adopt a frequentist interpretation: The probability of
an event is the limit of its long-run relative frequency (i.e., the frequency
with which it occurs as the amount of data increases without bound). Strict
adherence to this interpretation is not always possible in practice. When
studying rare events, for instance, large samples of data may not be available
and in such cases proponents of frequentist statistics resort to theoretical
results. The Bayesian view of the world is based on the subjectivist inter-
pretation of probability: Probability is subjective, a degree of belief that is
updated as information or data are acquired.1
1The concept of subjective probability is derived from arguments for rationality of
the preferences of agents. It originated in the 1930s with the (independent) works of
Bruno de Finetti and Frank Ramsey, and was further developed by Leonard Savage
and Dennis Lindley. The subjective probability interpretation can be traced back to
the Scottish philosopher and economist David Hume, who also had philosophical
influence over Harry Markowitz (by Markowitz’s own words in his autobiography
1

2
BAYESIAN METHODS IN FINANCE
Closely related to the concept of probability is that of uncertainty.
Proponents of the frequentist approach consider the source of uncertainty
to be the randomness inherent in realizations of a random variable. The
probability distributions of variables are not subject to uncertainty. In
contrast, Bayesian statistics treats probability distributions as uncertain and
subject to modification as new information becomes available. Uncertainty
is implicitly incorporated by probability updating. The probability beliefs
based on the existing knowledge base take the form of the prior probability.
The posterior probability represents the updated beliefs.
Since the beginning of last century, when quantitative methods and
models became a mainstream tool to aid in understanding financial markets
and formulating investment strategies, the framework applied in finance
has been the frequentist approach. The term ‘‘frequentist’’ usually refers
to the Fisherian philosophical approach named after Sir Ronald Fisher.
Strictly speaking, ‘‘Fisherian’’ has a broader meaning as it includes not
only frequentist statistical concepts such as unbiased estimators, hypothesis
tests, and confidence intervals, but also the maximum likelihood estimation
framework pioneered by Fisher. Only in the last two decades has Bayesian
statistics started to gain greater acceptance in financial modeling, despite its
introduction about 250 years ago by Thomas Bayes, a British minister and
mathematician. It has been the advancements of computing power and the
development of new computational methods that has fostered the growing
use of Bayesian statistics in finance.
On the applicability of the Bayesian conceptual framework, consider an
excerpt from the speech of former chairman of the Board of Governors of
the Federal Reserve System, Alan Greenspan:
The Federal Reserve’s experiences over the past two decades make
it clear that uncertainty is not just a pervasive feature of the
monetary policy landscape; it is the defining characteristic of that
landscape. The term ‘‘uncertainty’’ is meant here to encompass
both ‘‘Knightian uncertainty,’’ in which the probability distribution
of outcomes is unknown, and ‘‘risk,’’ in which uncertainty of
outcomes is delimited by a known probability distribution. [. . . ]
This conceptual framework emphasizes understanding as much as
possible the many sources of risk and uncertainty that policymakers
face, quantifying those risks when possible, and assessing the costs
associated with each of the risks. In essence, the risk management
published in Les Prix Nobel (1991)). Holton (2004) provides a historical background
of the development of the concepts of risk and uncertainty.

Introduction
3
approach to monetary policymaking is an application of Bayesian
[decision-making].2
The three steps of Bayesian decision making that Alan Greenspan outlines
are:
1. Formulating the prior probabilities to reflect existing information.
2. Constructing the quantitative model, taking care to incorporate the
uncertainty intrinsic in model assumptions.
3. Selecting and evaluating a utility function describing how uncertainty
affects alternative model decisions.
While these steps constitute the rigorous approach to Bayesian decision-
making, applications of Bayesian methods to financial modeling often only
involve the first two steps or even only the second step. This tendency is a
reflection of the pragmatic Bayesian approach that researchers of empirical
finance often favor and it is the approach that we adopt in this book.
The aim of the book is to provide an overview of the theory of Bayesian
methods and explain their applications to financial modeling. While the
principles and concepts explained in the book can be used in financial
modeling and decision making in general, our focus will be on portfolio
management and market risk management since these are the areas in
finance where Bayesian methods have had the greatest penetration to date.3
A FEW NOTES ON NOTATION
Throughout the book, we follow the convention of denoting vectors and
matrices in boldface.
We make extensive use of the proportionality symbol, ‘∝’, to denote the
cases where terms constant with respect to the random variable of interest
have been dropped from that variable’s density function. To illustrate,
suppose that the random variable, X, has a density function
p(x) = 2x.
(1.1)
2Alan Greenspan made these remarks at the Meetings of the American Statistical
Association in San Diego, California, January 3, 2004.
3Bayesian methods have been applied in corporate finance, particularly in capital
budgeting. An area of Bayesian methods with potentially important financial appli-
cations is Bayesian networks. Bayesian networks have been applied in operational
risk modeling. See, for example, Alexander (2000) and Neil, Fenton, and Tailor
(2005).

4
BAYESIAN METHODS IN FINANCE
Then, we can write
p(x) ∝x.
(1.2)
Now suppose that we take the logarithm of both sides of (1.2). Since
the logarithm of a product of two terms is equivalent to the sum of the
logarithms of those terms, we obtain
log(p(x)) = const + log(x),
(1.3)
where const = log(2) in this case. Notice that it would not be precise to
write log(p(x)) ∝log(x). We come across the transformation in (1.3) in
Chapters 10 through 14, in particular.
OVERVIEW
The book is organized as follows. In Chapters 2 through 5, we provide
an overview of the theory of Bayesian methods. The depth and scope of
that overview are subordinated to the methodological requirements of the
Bayesian applications discussed in later chapters and, therefore, in certain
instances lacks the theoretical rigor that one would expect to find in a purely
statistical discussion of the topic.
In Chapters 6 and 7, we discuss the Bayesian approach to mean-variance
portfolio selection and its advantages over the frequentist approach. We
introduce a general framework for reflecting degrees of belief in an asset
pricing model when selecting the optimal portfolio. We close Chapter 7 with
a description of Bayesian model averaging, which allows the decision maker
to combine conclusions based on several competing quantitative models.
Chapter 8 discusses an emblematic application of Bayesian methods
to portfolio selection—the Black-Litterman model. We then show how the
Black-Litterman framework can be extended to active portfolio selection
and how trading strategies can be incorporated into it.
The focus of Chapter 9 is market efficiency and predictability. We
analyze and illustrate the computation of measures of market inefficiency.
Then, we go on to describe the way predictability influences optimal port-
folio selection. We base that discussion on a Bayesian vector autoregressive
(VAR) framework.
Chapters 10, 11, and 12 deal with volatility modeling. We devote
Chapter 10 to an overview of volatility modeling. We introduce the two
types of volatility models—autoregressive conditionally heteroskedastic
(ARCH)-type models and stochastic volatility (SV) models—and discuss
some of their important characteristics, along with issues of estimation

Introduction
5
within the boundaries of frequentist statistics. Chapters 11 and 12 cover,
respectively, ARCH-type and SV Bayesian model estimation. Our focus is
on the various numerical methods that could be used in Bayesian estimation.
In Chapter 13, we deal with advanced techniques for model selection,
notably, recognizing nonnormality of stock returns. We first investigate an
approach in which higher moments of the return distribution are explicitly
included in the investor’s utility function. We then go on to discuss an
extension of the Black-Litterman framework that, in particular, employs
minimization of the conditional value-at-risk (CVaR). In Appendix A of
that chapter, we present an overview of risk measures that are alternatives
to the standard deviation, such as value-at-risk (VaR) and CVaR.
Chapter 14 is devoted to multifactor models of stock returns. We discuss
risk attribution in both an analytical and a numerical setting and examine
how the multifactor framework provides a natural setting for a coherent
portfolio selection and risk management approach.


## The Bayesian Paradigm

CHAPTER2
The Bayesian Paradigm
Likelihood Function and Bayes’ Theorem
O
ne of the basic mechanisms of learning is assimilating the information
arriving from the external environment and then updating the existing
knowledge base with that information. This mechanism lies at the heart
of the Bayesian framework. A Bayesian decision maker learns by revising
beliefs in light of the new data that become available. From the Bayesian
point of view, probabilities are interpreted as degrees of belief. Therefore,
the Bayesian learning process consists of revising of probabilities.1 Bayes’
theorem provides the formal means of putting that mechanism into action;
it is a simple expression combining the knowledge about the distribution of
the model parameters and the information about the parameters contained
in the data.
In this chapter, we present some of the basic principles of Bayesian
analysis.
THE LIKELIHOOD FUNCTION
Suppose we are interested in analyzing the returns on a given stock and
have available a historical record of returns. Any analysis of these returns,
beyond a very basic one, would require that we make an educated guess
about (propose) a process that might have generated these return data.
Assume that we have decided on some statistical distribution and denote
it by
p

y | θ

,
(2.1)
1Contrast this with the way probability is interpreted in the classical (frequentist)
statistical theory—as the relative frequency of occurrence of an event in the limit,
as the number of observations goes to infinity.
6

The Bayesian Paradigm
7
where y is a realization of the random variable Y (stock return) and θ is a
parameter specific to the distribution, p. Assuming that the distribution we
proposed is the one that generated the observed data, we draw a conclusion
about the value of θ. Obviously, central to that goal is our ability to summa-
rize the information contained in the data. The likelihood function is a sta-
tistical construct with this precise role. Denote the n observed stock returns
by y1, y2, . . . , yn. The joint density function of Y, for a given value of θ, is2
f

y1, y2, . . . , yn | θ

.
We can observe that the function above can also be treated as a
function of the unknown parameter, θ, given the observed stock returns.
That function of θ is called the likelihood function. We write it as
L

θ | y1, y2, . . . , yn

= f

y1, y2, . . . , yn | θ

.
(2.2)
Suppose we have determined from the data two competing values of
θ, θ 1 and θ 2, and want to determine which one is more likely to be the
true value (at least, which one is closer to the true value). The likelihood
function helps us make that decision. Assuming that our data were indeed
generated by the distribution in (2.1), θ 1 is more likely than θ 2 to be the
true parameter value whenever L

y1, y2, . . . , yn | θ1

> L

y1, y2, . . . , yn | θ2

.
This observation provides the intuition behind the method most often
employed in ‘‘classical’’ statistical inference to estimate θ from the data
alone—the method of maximum likelihood. The value of θ most likely to
have yielded the observed sample of stock return data, y1, y2, . . . , yn, is the
maximum likelihood estimate, θ, obtained from maximizing the likelihood
function in (2.2).
To illustrate the concept of a likelihood function, we briefly discuss two
examples—one based on the Poisson distribution (a discrete distribution)
and another based on the normal distribution (one of the most commonly
employed continuous distributions).
The Poisson Distribution Likelihood Function
The Poisson distribution is often used to describe the random number of
events occurring within a certain period of time. It has a single parameter,
2By using the term ‘‘density function,’’ we implicitly assume that the distribution
chosen for the stock return is continuous, which is invariably the case in financial
modeling.

8
BAYESIAN METHODS IN FINANCE
θ, indicating the rate of occurrence of the random event, that is, how many
events happen on average per unit of time. The probability distribution of
a Poisson random variable, X, is described by the following expression:3
p

X = k

= θ k
k!e−θ,
k = 0, 1, 2, . . . .
(2.3)
Suppose we are interested to examine the annual number of defaults of
North American corporate bond issuers and we have gathered a sample of
data for the period from 1986 through 2005. Assume that these corporate
defaults occur according to a Poisson distribution. Denoting the 20 obser-
vations by x1, x2, . . . , x20, we write the likelihood function for the Poisson
parameter θ(the average rate of defaults) as4
L

θ | x1, x2, . . . , x20

=
20

i=1
p

X = xi | θ

=
20

i=1
θ xi
xi!e−θ
= θ
20
i=1 xi
20
i=1 xi!
e−20θ.
(2.4)
As we see in later chapters, it is often customary to retain in the expressions
for the likelihood function and the probability distributions only the terms
that contain the unknown parameter(s); that is, we get rid of the terms
that are constant with respect to the parameter(s). Thus, (2.4) could be
written as
L

θ | x1, x2, . . . , x20

∝θ
20
i=1 xie−20θ,
(2.5)
where ∝denotes ‘‘proportional to.’’ Clearly, for a given sample of data, the
expressions in (2.4) and (2.5) are proportional to each other and therefore
contain the same information about θ. Maximizing either of them with
3The Poisson distribution is employed in the context of finance (most often, but not
exclusively, in the areas of credit risk and operational risk) as the distribution of
a stochastic process, called the Poisson process, which governs the occurrences of
random events.
4In this example, we assume, perhaps unrealistically, that θ stays constant through
time and that the annual number of defaults in a given year is independent from the
number of defaults in any other year within the 20-year period. The independence
assumption means that each observation of the number of annual defaults is regarded
as a realization from a Poisson distribution with the same average rate of defaults,
θ; this allows us to represent the likelihood function as the product of the mass
function at each observation.

The Bayesian Paradigm
9
Corporate Defaults
Probability
20
30
40
50
60
70
80
0.0
0.02
0.04
Likelihood
40
45
50
55
60
0.0 0.2 0.4 0.6 0.8 1.0
q
EXHIBIT 2.1
The poisson distribution function and likelihood function
Note: The graph on the left-hand side represents the plot of the distribution function
of the Poisson random variable evaluated at the maximum-likelihood estimate,
θ = 51.6. The graph on the right-hand side represents the plot of the likelihood
function for the parameter of the Poisson distribution.
respect to θ, we obtain that the maximum likelihood estimator of the
Poisson parameter, θ, is the sample mean, x:
θ = x =
20
i=1 xi
20
.
For the 20 observations of annual corporate defaults, we get a sample mean
of 51.6. The Poisson probability distribution function (evaluated at θ equal
to its maximum-likelihood estimate, θ = 51.6) and the likelihood function
for θ can be visualized, respectively, in the left-hand-side and right-hand-side
plots in Exhibit 2.1.
The Normal Distribution Likelihood Function
The normal distribution (also called the Gaussian distribution) has been the
predominant distribution of choice in finance because of the relative ease of
dealing with it and the availability of attractive theoretical results resting
on it.5 It is certainly one of the most important distributions in statistics.
Two parameters describe the normal distribution—the location parameter,
µ, which is also its mean, and the scale (dispersion) parameter, σ, also
5For example, in an introductory course in statistics students are told of the Central
Limit Theorem, which asserts that (under some conditions) the sum of independent
random variables has a normal distribution as the terms of the sum become infinitely
many.

10
BAYESIAN METHODS IN FINANCE
called standard deviation. The probability density function of a normally
distributed random variable Y is expressed as
f

y

=
1
√
2πσ
e−(y−µ)2
2σ2 ,
(2.6)
where y and µ could take any real value and σ can only take positive values.
We denote the distribution of Y by Y ∼N

µ, σ

. The normal density is
symmetric around the mean, µ, and its plot resembles a bell.
Suppose we have gathered daily dollar return data on the MSCI-
Germany Index for the period January 2, 1998, through December 31,
2003 (a total of 1,548 returns), and we assume that the daily return is
normally distributed. Then, given the realized index returns (denoted by y1,
y2, . . . , y1548), the likelihood function for the parameters µ and σ is written
in the following way:
L

µ, σ | y1, y2, . . . , y1548

=
1548

i=1
f

yi

=

1
√
2πσ
1548
e−1548
i=1
(yi−µ)2
σ2
∝σ −1548e−1548
i=1
(yi−µ)2
σ2
.
(2.7)
We again implicitly assume that the MSCI-Germany index returns are inde-
pendently and identically distributed (i.i.d.), that is, each daily return is a
realization from a normal distribution with the same mean and standard
deviation.
In the case of the normal distribution, since the likelihood is a function
of two arguments, we can visualize it with a three-dimensional surface as in
Exhibit 2.2. It is also useful to plot the so-called contours of the likelihood,
which we obtain by ‘‘slicing’’ the shape in Exhibit 2.2 horizontally at various
levels of the likelihood. Each contour corresponds to a pair of parameter
values (and the respective likelihood value). In Exhibit 2.3, for example, we
could observe that the pair (µ, σ) = (−0.23e −3, 0.31e −3), with a likeli-
hood value of 0.6, is more likely than the pair (µ, σ) = (0.096e −3, 0.33e −
3), with a likelihood value of 0.1, since the corresponding likelihood is larger.
THE BAYES’ THEOREM
Bayes’ theorem is the cornerstone of the Bayesian framework. Formally, it
is a result from introductory probability theory, linking the unconditional

The Bayesian Paradigm
11
−1
−0.5
0
0.5
1
1.5
x 10 −3
2.8
3
3.2
3.4
x 10−4
0
0.2
0.4
0.6
0.8
1
Mean (m)
Variance (s 2)
Likelihood
EXHIBIT 2.2
The likelihood function for the parameters of the normal
distribution
m
s2
−1
−0.5
0
0.5
1
1.5
x 10−3
2.8
2.9
3
3.1
3.2
3.3
3.4
x 10−4
Likelihood level = 0.1
Likelihood level = 0.6
EXHIBIT 2.3
The likelihood function for the parameters of the normal
distribution: contour plot

12
BAYESIAN METHODS IN FINANCE
distribution of a random variable with its conditional distribution. For
Bayesian proponents, it is the representation of the philosophical principle
underlying the Bayesian framework that probability is a measure of the
degree of belief one has about an uncertain event.6 Bayes’ theorem is a
rule that can be used to update the beliefs that one holds in light of new
information (for example, observed data).
We first consider the discrete version of Bayes’ theorem. Denote the
evidence prior to observing the data by E and suppose that a researcher’s
belief in it can be expressed as the probability P(E). The Bayes’ theorem tells
us that, after observing the data, D, the belief in E is adjusted according to
the following expression:
P(E | D) = P(D | E) × P(E)
P(D)
,
(2.8)
where:
1. P(D | E) is the conditional probability of the data given that the prior
evidence, E, is true.
2. P(D) is the unconditional (marginal) probability of the data, P(D) > 0;
that is, the probability of D irrespective of E, also expressed as
P(D) = P(D | E) × P(E) + P(D | Ec) × P(Ec),
where the subscript c denotes a complementary event.7
The probability of E before seeing the data, P(E), is called the prior
probability, whereas the updated probability, P(E | D), is called the posterior
probability.8 Notice that the magnitude of the adjustment of the prior
6Even among Bayesians there are those who do not entirely agree with the subjective
flavor this probability interpretation carries and attempt to ‘‘objectify’’ probability
and the inference process (in the sense of espousing the requirement that if two
individuals possess the same evidence regarding a source of uncertainty, they should
make the same inference about it). Representatives of this school of Bayesian thought
are, among others, Harold Jeffreys, Jos´e Bernardo, and James Berger.
7The complement (complementary event) of E, Ec, includes all possible outcomes
that could occur if E is not realized. The probabilities of an event and its complement
always sum up to 1: P(E) + P(Ec) = 1.
8The expression in (2.6) is easily generalized to the case when a researcher updates
beliefs about one of many mutually exclusive events (such that two or more of them
occur at the same time). Denote these events by E1, E2, . . . , EK. The events are such

The Bayesian Paradigm
13
probability, P(E), after observing the data is given by the ratio P(D | E)/P(D).
The conditional probability, P(D | E), when considered as a function of E
is in fact the likelihood function, as will become clear further below.
As an illustration, consider a manager in an event-driven hedge fund.
The manager is testing a strategy that involves identifying potential acqui-
sition targets and examines the effectiveness of various company screens, in
particular the ratio of stock price to free cash flow per share (PFCF). Let us
define the following events:
D = Company X’s PFCF has been more than three times lower than
the sector average for the past three years.
E = Company X becomes an acquisition target in the course of a given
year.
Independently of the screen, the manager assesses the probability of company
X being targeted at 40%. That is, denoting by Ec the event that X does not
become a target in the course of the year, we have
P(E) = 0.4
and
P(Ec) = 0.6.
Suppose further that the manager’s analysis suggests that the probability
a target company’s PFCF has been more than three times lower than the
sector average for the past three years is 75% while the probability that a
nontarget company has been having that low of a PFCF for the past three
years is 35%:
P(D | E) = 0.75
and
P(D | Ec) = 0.35.
that their probabilities sum up to 1: P(E1) + · · · + P(EK) = 1. Bayes’ theorem then
takes the form
P(Ek | D) =
P(D | Ek) × P(Ek)
P(D | E1) × P(E1) + P(D | E2) × P(E2) + · · · + P(D | EK) × P(EK)
for k = 1, . . . , K and P(D) > 0.

14
BAYESIAN METHODS IN FINANCE
If a bidder does appear on the scene, what is the chance that the targeted
company had been detected by the manager’s screen? To answer this
question, the manager needs to update the prior probability P(E) and
compute the posterior probability P(E | D). Applying (2.8), we obtain
P(E | D) =
0.75 × 0.4
0.75 × 0.4 + 0.35 × 0.6
≈0.59.
(2.9)
After taking into account the company’s persistently low PFCF, the proba-
bility of a takeover increases from 40% to 59%.
In financial applications, the continuous version of the Bayes’ theorem
(as follows later) is predominantly used. Nevertheless, the discrete form has
some important uses, two of which we briefly outline now.
Bayes’ Theorem and Model Selection
The usual approach to modeling of a financial phenomenon is to specify
the analytical and distributional properties of a process that one thinks
generated the observed data and treat this process as if it were the true
one. Clearly, in doing so, one introduces a certain amount of error into the
estimation process. Accounting for model risk might be no less important
than accounting for (within-model) parameter uncertainty, although it seems
to preoccupy researchers less often.
One usually entertains a small number of models as plausible ones. The
idea of applying the Bayes’ theorem to model selection is to combine
the information derived from the data with the prior beliefs one has about
the degree of model validity. One can then select the single ‘‘best’’ model
with the highest posterior probability and rely on the inference provided by
it or one can weigh the inference of each model by its posterior probability
and obtain an ‘‘averaged-out’’ conclusion. In Chapter 6, we discuss in detail
Bayesian model selection and averaging.
Bayes’ Theorem and Classification
Classification refers to assigning an object, based on its characteristics, into
one out of several categories. It is most often applied in the area of credit
and insurance risk, when a creditor (an insurer) attempts to determine
the creditworthiness (riskiness) of a potential borrower (policyholder).
Classification is a statistical problem because of the existence of information
asymmetry—the creditor’s (insurer’s) aim is to determine with very high
probability the unknown status of the borrower (policyholder). For example,

The Bayesian Paradigm
15
suppose that a bank would like to rate a borrower into one of three
categories: low risk (L), medium risk (M), and high risk (H). It collects data
on the borrower’s characteristics such as the current ratio, the debt-to-equity
ratio, the interest coverage ratio, and the return on capital. Denote these
observed data by the four-dimensional vector y. The dynamics of y depends
on the borrower’s category and is described by one of three (multivariate)
distributions,
f(y | C = L),
f(y | C = M),
or
f(y | C = H),
where C is a random variable describing the category. Let the bank’s belief
about the borrower’s category be π i, where
π1 = π(C = L),
π2 = π(C = M),
and
π3 = π(C = H).
The discrete version of Bayes’ theorem can be employed to evaluate the
posterior (updated) probability, π(C = i | y), i = L, M, H, that the borrower
belongs to each of the three categories.9
Let us now take our first steps in illustrating how Bayes’ theorem helps
in making inferences about an unknown distribution parameter.
Bayesian Inference for the Binomial Probability
Suppose we are interested in analyzing the dynamic properties of the intraday
price changes for a stock. In particular, we want to evaluate the probability
of consecutive trade-by-trade price increases. In an oversimplified scenario,
this problem could be formalized as a binomial experiment.
9See the appendix to Chapter 3 for details on the logistic regression, one of the most
commonly used econometric models in credit-risk analysis.

16
BAYESIAN METHODS IN FINANCE
The binomial experiment is a setting in which the source of randomness
is a binary one (only takes on two alternative modes/states) and the proba-
bility of both states is constant throughout.10 The binomial random variable
is the number of occurrences of the state of interest. In our illustration, the
two states are ‘‘the consecutive trade-by-trade price change is an increase’’
and ‘‘the consecutive trade-by-trade price change is a decrease or null.’’ The
random variable is the number of consecutive price increases. Denote it by
X. Denote the probability of a consecutive increase by θ. Our goal is to
draw a conclusion about the unknown probability, θ.
As an illustration, we consider the transaction data for the AT&T stock
during the two-month period from January 4, 1993, through February 26,
1993 (a total of 55,668 price records). The diagram in Exhibit 2.4 shows
how we define the binomial random variable given six price observations,
P1, . . . , P6. (Notice that the realizations of the random variable are one less
than the number of price records.) A consecutive price increase is ‘‘encoded’’
as A = 2 and its probability is θ = P(A = 2); all other realizations of A (A
= −2, −1, 0 or 1) have a probability of 1 −θ. We say that the number of
P1
P2
P3
P4
P5
P6
D1 = −1, 0, 1
D2 = −1, 0, 1
…..
D5 = −1, 0, 1
A1 = D1 + D2
A2 = D2
D3
+
. . .
A4 = D4
D5
+
where
Note: X = number of occurences of A = 2 within the sample period
Di = −1  if Pi+1< Pi
Di = 0   if Pi+1 = Pi
Di = 1   if Pi+1> Pi
EXHIBIT 2.4
The number of consecutive trade-by-trade price
increases
10The binomial experiment is formally characterized by these and a few additional
requirements. As a reference, see any introductory statistics text.

The Bayesian Paradigm
17
consecutive price increases, X, is distributed as a binomial random variable
with parameter θ. The probability mass function of X is represented by the
expression
P(X = x | θ) =
 n
x

θ x(1 −θ)n−x,
x = 0, 1, 2, . . . , n,
(2.10)
where n is the sample size (the number of trade-by-trade price changes;
a price change could be zero) and
 n
x

=
n!
x!(n−x)!. During the sample
period, there are X = 176 trade-by-trade consecutive price increases. This
information is embodied in the likelihood function for θ:
L

θ | X = 176

= θ 176(1 −θ)55667−176.
(2.11)
We would like to combine that information with our prior belief about
what the probability of a consecutive price increase is. Before we do that, we
recall the notational convention we stick to throughout the book. We denote
the prior distribution of an unknown parameter θ by π(θ), the posterior
distribution of θ by π(θ|data), and the likelihood function by L(θ | data).
We consider two prior scenarios for the probability of consecutive price
increases, θ:
1. We do not have any particular belief about the probability θ. Then,
the prior distribution could be represented by a uniform distribution on
the interval [0, 1]. Note that this prior assumption implies an expected
value for θ of 0.5. The density function of θ is given by
π(θ) = 1,
0 ≤θ ≤1.
2. Our intuition suggests that the probability of a consecutive price increase
is around 2%. A possible choice of a prior distribution for θ is the beta
distribution.11 The density function of θ is then written as
π(θ | α, β) =
1
B(α, β)θ α−1(1 −θ)β−1,
0 ≤θ ≤1,
(2.12)
11The beta distribution is the conjugate distribution for the parameter, θ, of the
binomial distribution. See Chapter 3 for more details on conjugate prior distribu-
tions.

18
BAYESIAN METHODS IN FINANCE
Prior Density
0.0
0.2
0.4
0.6
0.8
1.0
0.0
0.5
1.0
1.5
q
Prior Density
0.0
0.02
0.04
0.06
0
10
20
30
40
50
60
q
EXHIBIT 2.5
Density curves of the two prior distributions for the binomial
parameter, θ
Note: The density curve on the left-hand side is the uniform density, while the one
on the right-hand side is the beta density.
where α > 0 and β > 0 are the parameters of the beta distribution and
B(α, β) is the so-called beta function. We set the parameters α and β to 1.6
and 78.4, respectively, and we postpone the discussion of prior specification
until the next chapter.
Exhibit 2.5 presents the plots of the two prior densities. Notice that
under the uniform prior, all values of θ are equally likely, while under the
beta prior, we assert higher prior probability for some values and lower
prior probability for others.

The Bayesian Paradigm
19
Combining the sample information with the prior beliefs, we obtain θ’s
posterior distribution. We rewrite Bayes’ theorem with the notation in the
current discussion:
p(θ | x) = L(θ | x)π(θ)
f(x)
,
(2.13)
where f(x) is the unconditional (marginal) distribution of the random
variable X, given by
f(x) =
	
L(θ | x)π(x) dθ.
(2.14)
Since f(x) is obtained by averaging over all possible values of θ, it does
not depend on θ. Therefore, we can rewrite (2.8) as
π(θ | x) ∝L(θ | x)π(θ).
(2.15)
The expression in (2.15) provides us with the posterior density of θ up to
some unknown constant. However, in certain cases we would still be able
to recognize the posterior distribution as a known distribution, as we see
shortly.12 Since both assumed prior distributions of θ are continuous, the
posterior density is also continuous and (2.13) and (2.15), in fact, represent
the continuous version of Bayes’ theorem.
Let us see what the posterior distribution for θ is under each of the two
prior scenarios.
1. The posterior of θ under the uniform prior scenario is written as
π(θ | x) ∝L(θ | x) × 1
∝θ 176(1 −θ)55667−176
= θ 177−1(1 −θ)55492−1,
(2.16)
where the first ∝refers to omitting the marginal data distribution term
in (2.14), while the second ∝refers to omitting the constant term from
the likelihood function.
The expression θ 177−1(1 −θ)55492−1 above resembles the density
function of the beta distribution in (2.12). The missing part is the term
B(177, 55492), which is a constant with respect to θ. We call θ α−1
12When the posterior distribution is not recognizable as a known distribution, infer-
ence about θ is accomplished with the help of numerical methods, the foundations
of which we discuss in Chapter 3.

20
BAYESIAN METHODS IN FINANCE
(1 −θ)β−1 the kernel of a beta distribution with parameters α and β.
Obtaining it is sufficient to identify uniquely the posterior of θ as a beta
distribution with parameters α = 177 and β = 55492.
2. The beta distribution is the conjugate prior distribution for the binomial
parameter θ. This means that the posterior distribution of θ is also a
beta distribution (of course, with updated parameters):
π(θ | x) ∝L(θ | x)π(θ)
∝θ 176(1 −θ)55667−176θ 1.6−1(1 −θ)78.4−1
= θ 177.6−1(1 −θ)55569.4−1,
(2.17)
where again we omit any constants with respect to θ. As expected, we
recognize the expression in the last line above as the kernel of a beta
distribution with parameters α = 177.6 and β = 55569.4.
Finally, we might want to obtain a single number as an estimate of θ. In
the classical (frequentist) setting, the usual estimator of θ is the maximum
likelihood estimator (the value maximizing the likelihood function in (2.11)),
which happens to be the sample proportion θ:
θ =
176
55667 = 0.00316
(2.18)
or 0.316%.
In the Bayesian setting, one possible estimate of θ is the posterior mean,
that is, the mean of θ’s posterior distribution. Since the mean of the beta
distribution is given by α/(α + β), the posterior mean of θ(the expected
probability of consecutive trade-by-trade increase in the price of the AT&T
stock) under the uniform prior scenario is

θU =
177
177 + 55492 = 0.00318
or 0.318%, while the posterior mean of θ under the beta prior scenario is

θB =
177.6
177.6 + 55569.4 = 0.00319
or 0.319%.

The Bayesian Paradigm
21
The two posterior estimates and the maximum-likelihood estimate are
the same for all practical purposes. The reason is that the sample size is so
large that the information contained in the data sample ‘‘swamps out’’ the
prior information. In Chapter 3, we further illustrate and comment on the
role sample size plays in posterior inference.
SUMMARY
In this chapter we laid the foundations of Bayesian analysis, emphasizing
its practical rather than philosophical and methodological aspects. The
objective is to employ its framework for representing the uncertainty arising
in various scenarios through combining information derived from different
sources—the observed data and prior beliefs. We introduced Bayes’ theorem
and the concepts of likelihood functions, prior distributions, and posterior
distributions. In the next chapter, we discuss the nature of prior information
and delve deeper into Bayesian inference.


## Prior and Posterior Information

CHAPTER3
Prior and Posterior Information,
Predictive Inference
I
n this chapter, we focus on the essentials of Bayesian inference. Formalizing
the practitioner’s knowledge and intuition into prior distributions is a key
part of the inferential process. Especially when the data records are not
abundant, the choice of prior distributions can influence greatly posterior
conclusions. After presenting an overview of some approaches to prior
specification, we focus on the elements of posterior analysis. Posterior and
predictive results can be summarized in a few numbers, as in the classical
statistical approach, but one could also easily examine and draw conclusions
about all other aspects of the posterior and predictive distributions of the
(functions of the) parameters.
PRIOR INFORMATION
In the previous chapter, we explained why the prior distribution for the
model parameters is an integral component of the Bayesian inference process.
The updated (posterior) beliefs are the result of the trade-off between the
prior and data distributions. For ease of exposition, we rewrite below the
continuous form of Bayes’ theorem given in (2.15) in Chapter 2:
p(θ | y) ∝L(θ | y)π(θ),
(3.1)
where:
θ = unknown parameter whose inference we are interested in.
y = a vector (or a matrix) of recorded observations.
π(θ) = prior distribution of θ depending on one or more
parameters, called hyperparameters.
L(θ|y) = likelihood function for θ.
p(θ|y) = posterior (updated) distribution of θ.
22

Prior and Posterior Information, Predictive Inference
23
Two factors determine the degree of posterior trade-off—the strength
of the prior information and the amount of data available. Generally,
unless the prior is very informative (in a sense that will become clear), the
more observations, the greater the influence of the data on the posterior
distribution. On the contrary, when very few data records are available, the
prior distribution plays a predominant role in the updated beliefs.
How to translate the prior information about a parameter into the ana-
lytical (distributional) form, π(θ), and how sensitive the posterior inference
is to the choice of prior have been questions of considerable interest in
the Bayesian literature.1 There is, unfortunately, no ‘‘best’’ way to specify
the prior distribution and translating subjective views into prior values for
the distribution parameters could be a difficult undertaking.
Before we review some commonly used approaches to prior elicitation,
we make the following notational and conceptual note. It is often convenient
to represent the posterior distribution, p(θ | y), in a logarithmic form. Then,
it is easy to see that the expression in (3.1) is transformed according to
log (p(θ | y)) = const + log (L(θ | y)) + log (π(θ)) ,
where const is the logarithm of the constant of proportionality.
Informative Prior Elicitation
Prior beliefs are informative when they modify substantially the informa-
tion contained in the data sample so that the conclusions we draw about
the model parameters based on the posterior distribution and on the data
distribution alone differ. The most commonly used approach to represent-
ing informative prior beliefs is to select a distribution for the unknown
parameter and specify the hyperparameters so as to reflect these beliefs.
Informative Prior Elicitation for Location and Scale Parameters
Usually,
when we think about the average value that a random variable takes,
we have the typical value in mind. Therefore, we hold beliefs about the
median of the distribution rather than its mean.2 This distinction does not
1See Chapter 3 in Berger (1985), Chapter 3 in Leonard and Hsu (1999), Berger
(1990, 2006), and Garthwaite, Kadane, and O’Hagan (2005), among others.
2The median is a measure of the center of a distribution alternative to the mean,
defined as the value of the random variable, which divides the probability mass in
halves. The median is the typical value the random variable takes. It is a more robust
measure than the mean as it is not affected by the presence of extreme observations
and, unless the distribution is symmetric, is not equal to the mean.

24
BAYESIAN METHODS IN FINANCE
matter in the case of symmetric distributions, since then the mean and
the median coincide. However, when the distribution we selected is not
symmetric, care must be taken to ensure that the prior parameter values
reflect our beliefs. Formulating beliefs about the spread of the distribution
is less intuitive. The easiest way is to do so is to ask ourselves questions such
as: Which value of the random variable do a quarter of the observations
fall below/above? Denoting the random variable by X, the answers to these
questions give us the following probability statements:
P(X < x0.25) = 0.25
and
P(X > x0.75) = 0.25,
where x0.25 and x0.75 are the values we have subjectively determined and are
referred to as the first and third quartiles of the distribution, respectively.
Other similar probability statements can be formulated, depending on the
prior beliefs.
As an example, suppose that we model the behavior of the monthly
returns on some financial asset and the normal distribution, N(µ, σ 2) (along
with the assumption that the returns are independently and identically
distributed), describes their dynamics well. Assume for now that the variance
is known, σ 2 = σ 2*, and thus we only need to specify a prior distribution for
the unknown mean parameter, µ. We believe that a symmetric distribution
is an appropriate choice and go for the simplicity of a normal prior:
µ ∼N(η, τ 2),
(3.2)
where η is the prior mean and τ 2 is the prior variance of µ; to fully
specify µ’s prior, we need to (subjectively) determine their values. We
believe that the typical monthly return is around 1%, suggesting that the
median of µ’s distribution is 1%. Therefore, we set η to 1%. Further,
suppose we (subjectively) estimate that there is about a 25% chance that
the average monthly return is less than 0.5% (i.e., µ0.25 = 0.5%). Then,
using the tabulated cumulative probability values of the standard normal
distribution, we find that the implied variance, τ 2, is approximately equal to
0.742.3 Our choice for the prior distribution of µ is thus π(µ) = N(1, 0.742).
3A random variable, X ∼N(µ, σ 2), is transformed into a standard normal random
variable, Z ∼N(0, 1), by subtracting the mean and dividing by its standard
deviation:
Z = X −µ
σ
.

Prior and Posterior Information, Predictive Inference
25
Informative Prior Elicitation for the Binomial Probability
Let us return to our
discussion on Bayesian inference for the binomial probability parameter, θ,
in Chapter 2. One of the prior assumptions we made there was that θ
is distributed with a beta distribution with parameters α = 1.6 and β =
78.4. We determined these prior values so as to match our prior beliefs that
on average around 2% of the consecutive trade-by-trade price changes are
increases and that there is around a 30% chance that the proportion of the
consecutive price increases is less than 1%, that is4
α
α + β = 0.02
and
P(θ < 0.01) = 0.3,
where
α
α+β is the expression for the mean of a beta-distributed random
variable. Since there are two unknown hyperparameters (α and β), the two
expressions above uniquely determine their values.
Noninformative Prior Distributions
In many cases, our prior beliefs are vague and thus difficult to translate
into an informative prior. We therefore want to reflect our uncertainty
about the model parameter(s) without substantially influencing the posterior
parameter inference. The so-called noninformative priors, also called vague
or diffuse priors, are employed to that end.
Most often, the noninformative prior is chosen to be either a uniform
(flat) density defined on the support of the parameter or the Jeffreys’ prior.5
The noninformative distribution for a location parameter, µ, is given by a
uniform distribution on its support ((−∞, ∞)), that is,6
π(µ) ∝1.
(3.3)
4Notice that this choice of hyperparameter values implies that the probability of the
proportion of consecutive price increases being greater than 5% is around 5%. If this
contradicts substantially our prior beliefs, we might want to reconsider the choice
of the beta distribution as a prior distribution. In general, once we have selected a
certain distribution to represent our beliefs, we lose some flexibility in reflecting the
beliefs as accurately as possible.
5Reference priors are another class of noninformative priors developed by Berger
and Bernardo (1992); see also Bernardo and Smith (1994). Their derivation is
somewhat involved and applications in the field of finance are rare. One exception
is Aguilar and West (2000).
6Suppose a density has the form f(x −µ). The parameter µ is called the location
parameter if it only appears within the expression (x −µ). The density, f, is then
called a location density. For example, the normal density, N(µ, σ 2∗), is a location
density when σ 2∗is fixed.

26
BAYESIAN METHODS IN FINANCE
The noninformative distribution for a scale parameter, σ (defined on the
interval (0, ∞)) is7
π(σ) ∝1
σ .
(3.4)
Notice that the prior densities in both (3.3) and (3.4) are not proper
densities, in the sense that they do not integrate to one:
 ∞
−∞
1 dµ = ∞
and
 ∞
0
1
σ dσ = ∞.
Even though the resulting posterior densities are usually proper, care
must be taken to ensure that this is indeed the case. In Chapter 11,
for example, we see that an improper prior for the degrees-of-freedom
parameter, ν, of the Student’s t-distribution leads to an improper posterior.
To avoid impropriety of the posterior distributions, one could employ
proper prior distributions but make them noninformative, as we discuss
further on.
When one is interested in the joint posterior inferences for µ and σ,
these two parameters are often assumed independent, giving the joint prior
distribution
π(µ, σ) ∝1
σ .
(3.5)
The prior in (3.5) is often referred to as the Jeffreys’ prior.8
Prior ignorance could also be represented by a (proper) standard dis-
tribution with a very large dispersion—the so-called flat or diffuse proper
7Suppose a density has the form 1
σ f( x
σ ). The parameter σ is the scale parameter. For
example, the normal density, N(µ*, σ 2), is a scale density when the mean is fixed at
some µ*.
8See Jeffreys (1961). In general, Jeffreys’ prior of a parameter (vector), θ, is given by
π(θ) = |I(θ)|1/2,
where I(θ) is the so-called Fisher’s information matrix for θ, given by
I(θ) = −E
∂2 log f(x | θ)
∂θ∂θ′

,

Prior and Posterior Information, Predictive Inference
27
prior distribution. Let us turn again to the example for the monthly returns
for some financial asset we considered earlier and suppose that we do not
have particular prior information about the range of typical values the mean
monthly return could take. To reflect this ignorance, we might center the nor-
mal distribution of µ around 0 (a neutral value, so to speak) and fix the stan-
dard deviation, τ, at a large value such as 106, that is, π(µ) = N(0, (106)2).
The prior of µ could take alternative distributional forms. For instance,
a symmetric Student’s t-distribution could be asserted. A standard Student’s
t-distribution has a single parameter, the degrees of freedom, ν, which
one can use to regulate the heaviness of the prior’s tails—the lower ν is,
the flatter the prior distribution. Asserting a scaled Student’s t-distribution
with a scale parameter, σ, provides additional flexibility in specifying the
prior of µ.9 It can be argued that eliciting heavy-tailed prior distributions
(with tails heavier than the tails of the data distribution), increases the
posterior’s robustness, that is, lowers the sensitivity of the posterior to the
prior specification.
Conjugate Prior Distributions
In many situations, the choice of a prior distribution is governed by the
desire to obtain analytically tractable and convenient posterior distribution.
Thus, if one assumes that the data have been generated by a certain
class of distributions, employing the class of the so-called ‘‘conjugate prior
distributions’’ guarantees that the posterior distribution is of the same class
as the prior distribution.10 Although the prior and posterior distributions
have the same form, their parameters differ—the parameters of the posterior
distribution reflects the trade-off between prior and sample information. We
now consider the case of the normal data distribution, since it is central to
our discussions of financial applications. Any other conjugate scenarios we
come across is discussed in the respective chapters.
If the data, x, are assumed to come from a normal distribution, the
conjugate priors for the normal mean, µ, and variance, σ 2, are, respectively,
and the expectation is with respect to the random variable X, whose density function
is f(x | θ). Notice that applying the expression for π(θ) to, for example, the normal
distribution, one obtains the joint prior π(µ, σ) ∝1/σ 2, instead of the one in (3.5).
Nevertheless, Jeffreys advocated the use of (3.5) since he assumed independence of
the location and scale parameters.
9The Student’s t-distribution has heavier tails than the normal distribution. For
values of ν less than 2, its variance is not defined. See the appendix to this chapter
for the definition of the Student’s t-distribution.
10Technically speaking, for the parameters of all distributions belonging to the
exponential family there are conjugate prior distributions.

28
BAYESIAN METHODS IN FINANCE
a normal distribution and an inverted χ 2 distribution (see (3.28)),11
π(µ | σ 2) = N

η, σ 2
T

and
π(σ 2) = Inv −χ 2(ν0, c2
0),
(3.6)
where Inv −χ 2(ν, c2) denotes the inverted χ 2 distribution with ν0 degrees of
freedom and a scale parameter c2
0.12 The prior parameters (hyperparameters)
that need to be (subjectively) specified in advance are η, T, ν0, and c2
0. The
parameter T plays the role of a discount factor, reflecting the degree of
uncertainty about the distribution of µ. Usually, T is greater than one since
one naturally holds less uncertainty about the distribution of the mean, µ,
(with variance σ 2/T) than the data, x (with variance σ 2).
In our discussions of various financial applications in the following
chapters, we see that the normal distribution is often not the most appropri-
ate assumption for a data-generation process in view of various empirical
features that financial data exhibit. Alternative distributional choices most
often do not have corresponding conjugate priors and the resulting posterior
distributions might not be recognizable as any known distributions. Then,
numerical methods are applied to compute the posteriors. (See, for example,
Chapter 4.)
In general, eliciting conjugate priors should be preceded by an analysis
of whether prior beliefs would be adequately represented by them.
Empirical Bayesian Analysis
So far in this chapter, we took care to emphasize the subjective manner in
which prior information is translated into a prior distribution. This involves
specifying the prior hyperparameters (if an informative prior is asserted)
before observing/analyzing the set of data used for model evaluation. One
approach for eliciting the hyperparameters parts with this tradition—the
11Notice that µ and σ 2 are not independent in (3.6). This prior scenario is the
so-called natural conjugate prior scenario. Natural conjugate priors are priors
whose functional form is the same as the likelihood’s. The joint prior density of
µ and σ 2, π(µ, σ 2) can be represented as the product of a conditional and a
marginal density: π(µ, σ 2) = π(µ|σ 2)π(σ 2). If the dependence of the normal mean
and variance is deemed inappropriate for the particular application, it is possible to
make them independent and still benefit from the convenience of their functional
forms—by eliciting a prior for µ as in (3.2).
12See the appendix to this chapter for details on the inverted χ2 distribution.

Prior and Posterior Information, Predictive Inference
29
so-called ‘‘empirical Bayesian approach.’’ In it, sample information is used
to compute the values of the hyperparameters. Here we provide an example
with the natural conjugate prior for a normal data distribution.
Denote the sample of n observations by x =

x1, x2, . . . , xn

. It can be
shown that the normal likelihood function can be expressed in the following
way:
L(µ, σ 2 | x) =

2πσ 2−n/2 exp

−
n
i = 1(xi −µ)2
2σ 2

=

2πσ 2−n/2 exp

−1
2σ 2

νs2 + n(µ −ˆµ)2
,
(3.7)
where
ˆµ =
n
i = 1 xi
n
,
ν = n −1,
and
s2 =
n
i = 1(xi −ˆµ)2
n −1
.
(3.8)
The quantities ˆµ and s2 are, respectively, the unbiased estimators of the
mean, µ, and the variance, σ 2, of the normal distribution.13 It is now easy
to see that the likelihood in (3.7) can be viewed as the product of two
distributions—a normal distribution for µ conditional on σ 2,
µ | σ ∼N

ˆµ, σ 2
n

and an inverted χ 2 distribution for σ 2,
σ 2 ∼Inv-χ 2 
ν, s2
,
which become the prior distributions under the empirical Bayesian approach.
We can observe that these two distributions are, of course, the same as the
ones in (3.6). Their parameters are functions of the two sufficient statistics
for the normal distribution, instead of subjectively elicited quantities. The
sample size, n, above plays the role of the discount factor, T, in (3.6)—the
more data available, the less uncertain one is about the prior distribution of
µ (its prior variance decreases).
13An unbiased estimator of a parameter θ is a function of the data (a statistic),
whose expected value is θ. The statistics ˆµ and s2 are the so-called sufficient statistics
for the normal distribution—knowing them is sufficient to uniquely determine the
normal distribution which generated the data. In empirical Bayesian analysis, the
hyperparameters are usually functions of the sufficient statistics of the sampling
distribution.

30
BAYESIAN METHODS IN FINANCE
We now turn to a discussion of the fundamentals of posterior inference.
Later in this chapter, we provide an illustration of the effect various prior
assumptions have on the posterior distribution.
POSTERIOR INFERENCE
The posterior distribution of a parameter (vector) θ given the observed
data x is denoted as p(θ | x) and obtained by applying the Bayes’ theorem
discussed in Chapter 2 (see also (3.2)). Being a combination of the data
and the prior, the posterior contains all relevant information about the
unknown parameter θ. One could plot the posterior distribution, as we did
in the illustration involving the binomial probability in Chapter 2, in order
to visualize how the posterior probability mass is distributed.
Posterior Point Estimates
Although the benefit of being able to visualize the whole posterior distribu-
tion is unquestionable, it is often more practical to report several numerical
characteristics describing the posterior, especially if reporting the results
to an audience used to the classical (frequentist) statistical tradition. Com-
monly used for this purpose are the point estimates, such as the posterior
mean, the posterior median, and the posterior standard deviation.14 When
the posterior is available in closed form, these numerical summaries can also
be expressed in closed form. For example, we computed analytically the
posterior mean of the binomial probability, θ, in Chapter 2. The posterior
parameters in the natural conjugate prior scenario with a normal sampling
density (see (3.6)) are also available analytically. The mean parameter, µ,
of the normal distribution has a normal posterior, conditional on σ 2,
p

µ | x, σ 2
= N

µ∗,
σ 2
T + n

.
(3.9)
14In decision theory, loss functions are used to assess the impact of an action. In the
context of parameter inference, if θ* is the true parameter value, the loss associated
with employing the estimate θ instead of θ* is represented by the loss function
L(θ∗, θ). One approach to estimating θ is to determine the value that minimizes
the expected resulting loss. In Bayesian analysis, we minimize the expected posterior
loss—its expectation is computed with respect to θ’s posterior distribution. It can be
shown that the estimate of central tendency that minimizes the expected, posterior,
squared-error loss function, L(θ∗, θ) = (θ∗−θ)2, is the posterior mean, while
the estimate that minimizes the expected, posterior, absolute-error loss function,
L(θ∗, θ) = |θ∗−θ|, is the posterior median. The expectation of the loss function is
calculated with respect to θ’s posterior distribution.

Prior and Posterior Information, Predictive Inference
31
The posterior mean and variance of µ are, given, respectively, by
E(µ | x, σ 2)
≡
µ∗= ˆµ
n
σ 2
n
σ 2 + T
σ 2
+ η
T
σ 2
n
σ 2 + T
σ 2
= ˆµ
n
n + T + η
T
n + T
(3.10)
where ˆµ is the sample mean as given in (3.8) and
var(µ | x, σ 2) =
σ 2
T + n.
(3.11)
In practical applications, usually the emphasis is placed on obtaining the
posterior distribution of µ, not least because it is more difficult to formulate
prior beliefs about the variance, σ 2 (let alone the whole covariance matrix
in the multivariate setting). Often, then, the covariance matrix is estimated
outside of the regression model and then fed into it, as if it were the
‘‘known’’ covariance matrix.15 Nevertheless, for completeness, we provide
σ 2’s posterior distribution—an inverted χ 2,
p

σ 2 | x

= Inv-χ 2 
ν∗, c2∗
,
(3.12)
where
ν∗= ν0 + n,
(3.13)
c2∗= 1
ν∗

ν0c2
0 + (n −1)s2 +
Tn
T + n( ˆµ −η)2

,
(3.14)
and s2 is the unbiased sample estimator of the normal variance as given in
(3.8). Using (3.13) and (3.14), one can now compute the posterior mean
and variance of σ 2, respectively, as16
E(σ 2 | x) =
ν∗
ν∗−2c2∗
(3.15)
and
var(σ 2 | x) =
2ν∗2
(ν∗−2)2(ν∗−4)

c2∗2 .
(3.16)
15One example for such an approach is the Black-Litterman model, which we discuss
in Chapter 8.
16These are the expressions for expected value and variance of a random variable
with the inverted χ2 distribution; see the appendix for details.

32
BAYESIAN METHODS IN FINANCE
When the posterior is not of known form and is computed numerically
(through simulations), so are the posterior point estimates, as well as the
distributions of any functions of these estimates, as we will see in Chapter 4.
Bayesian Intervals
The point estimate for the center of the posterior distribution is not too
informative if the posterior uncertainty is significant. To assess the degree
of uncertainty, a posterior (1 −α) interval [a, b], called a credible interval,
can be constructed. The probability that the unknown parameter, θ, falls
between a and b is (1 −α),
P(a < θ < b | x) =
 b
a
p(θ | x) dθ = 1 −α.
For reasons of convenience, the interval bounds may be determined so that
an equal probability, α/2, is left in the tails of the posterior distribution.
For example, a could be chosen to be the 25th quantile, while b—the
75th quantile. The interpretation of the credible interval is often mistakenly
ascribed to the classical confidence interval. In the classical setting, (1 −α)
is a coverage probability—if arbitrarily many repeated samples of data
are recorded, 100(1 −α)% of the corresponding confidence intervals will
contain θ —a much less intuitive interpretation.
The credible interval is computed either analytically, by finding the
theoretical quantiles of the posterior distribution (when it is of known form),
or numerically, by finding the empirical quantiles using the simulations of
the posterior density (see Chapter 4).17
Bayesian Hypothesis Comparison
The title of this section18 abuses the usual terminology by intentionally
using ‘‘comparison’’ instead of ‘‘testing’’ in order to stress that the Bayesian
17A special type of Bayesian interval is the highest posterior density (HPD) interval.
It is built so as to include the values of θ that have the highest posterior probability
(the most likely values). When the posterior is symmetric and has a single peak
(is unimodal), credible and HPD intervals coincide. With very skewed posterior
distributions, however, the two intervals look very different. A disadvantage of HPD
intervals is that they could be disjoint when the posterior has more than one peak
(is multimodal). In unimodal settings, the Bayesian HPD interval obtained under
the assumptions of a noninformative prior corresponds to the classical confidence
interval.
18In this section, we emphasize a practical approach to Bayesian hypothesis testing.
For a rigorous description of Bayesian hypothesis testing, see, for example, Zellner
(1971).

Prior and Posterior Information, Predictive Inference
33
framework affords one more than the mere binary reject/do-not-reject
decision of the classical hypothesis testing framework. In the classical
setting, the probability of a hypothesis (null or alternative) is either 0
or 1 (since frequentist statistics considers parameters as fixed, although
unknown, quantities).
In contrast, in the Bayesian setting (where parameters are treated
as random variables), the probability of a hypothesis can be computed
(and is different from 0 or 1, in general), allowing for a true hypotheses
comparison.19
Suppose one wants to compare the null hypothesis
H0 : θ is in 0
with the alternative hypothesis
H1 : θ is in 1,
where 0 and 1 are sets of possible values for the unknown parameter
θ. As with point estimates and credible intervals, hypothesis comparison
is entirely based on θ’s posterior distribution. We compute the posterior
probabilities of the null and alternative hypotheses,
P(θ is in 0 | x) =

0
p(θ | x) dθ
(3.17)
and
P(θ is in 1 | x) =

1
p(θ | x) dθ,
(3.18)
respectively. These posterior hypotheses probabilities naturally reflect both
the prior beliefs and the data evidence about θ. An informed decision can
19In the classical setting, the decision to reject or not the null hypothesis is made on the
basis of the realization of a test statistic—a function of the data—whose distribution
is known. The p-value of the hypothesis test is the probability of obtaining a value
of the statistic as extreme or more extreme than the one observed. The p-value
is compared to the test’s significance level, which represents the predetermined
probability of rejecting the null hypothesis falsely. If the p-value is sufficiently small
(smaller than the significance level), the null hypothesis is rejected. The p-value
is often mistakenly given the interpretation of a posterior probability of the null
hypothesis. It has been suggested that a low p-value, interpreted by many as strong
evidence against the null hypothesis, could be in fact quite a misleading signal about
evidence strength. See, for example, Berger (1985) and Stambaugh (1999).

34
BAYESIAN METHODS IN FINANCE
now be made incorporating that knowledge. For example, the posterior
probabilities could be employed in scenario-generation—a tool of great
importance in risk analysis.
The Posterior Odds Ratio
Although the framework outlined the previous
section is generally sufficient to make an informed decision about the rele-
vance of hypotheses, we briefly discuss a somewhat more formal approach for
Bayesian hypothesis testing. That approach consists of summarizing the pos-
terior relevance of the two hypotheses into a single number—the posterior
odds ratio. The posterior odds ratio is the ratio of the weighted likelihoods
for the model parameters under the null hypothesis and under the alternative
hypothesis, multiplied by the prior odds. The weights are the prior parameter
distributions (thus, parameter uncertainty is taken into account).20
Denote the a priori probability of the null hypothesis by α. Then, the
prior odds are the ratio α/(1 −α). The posterior odds, denoted by PO, are
simply the prior odds updated with the information contained in the data
and are given by
PO =
α
1 −α ×

L(θ | x, H0) π(θ) dθ

L(θ | x, H1) π(θ) dθ ,
(3.19)
where L(θ | x, H0) is the likelihood function reflecting the restrictions
imposed by the null hypothesis and L(θ | x, H1) is the likelihood function
under the alternative hypothesis.
When no prior evidence in favor or against the null hypothesis exists,
the prior odds is usually set equal to one. A low value of the posterior odds
generally indicates evidence against the null hypothesis.
BAYESIAN PREDICTIVE INFERENCE
After performing Bayesian posterior inference about the parameters of the
data-generating process, one may use the process to predict the realizations
of the random variable ahead in time. The purpose of such a prediction
could be to test the predictive power of the model (for example, by analyzing
a metric for the distance between the model’s predictions and the actual
realizations) as part of a backtesting procedure or to directly use it in the
decision-making process.
As in the case of posterior inference, predictive inference provides more
than simply a point prediction—one has available the whole predictive
20The posterior odds ratio bears similarity to the likelihood ratio which is at the
center of most classical hypothesis tests. As its name suggests, the likelihood ratio is
the ratio of the likelihoods under the null and the alternative hypotheses.

Prior and Posterior Information, Predictive Inference
35
distribution (either analytically or numerically) and thus increased modeling
flexibility.21 The density of the predictive distribution is the sampling (data)
distribution weighted by the posterior parameter density. By averaging
out the parameter uncertainty (contained in the posterior), the predictive
distribution provides a superior description of the model’s predictive ability.
In contrast, the classical approach to prediction involves computing point
predictions or prediction intervals by plugging in the parameter estimates
into the sampling density, treating those estimates as if they were the true
parameter values.
Denoting the sampling and the posterior density by f(x | θ) and p(θ | x),
respectively, the predictive density one step ahead is given by22
f(x+1 | x) =

f(x+1 | θ)p(θ | x) dθ,
(3.20)
where x+1 denotes the one-step-ahead realization. Notice that since we inte-
grate (average) over the values of θ, the predictive distribution is independent
of θ and depends only on the past realizations of the random variable X—it
describes the process we assume has generated the data. The predictive den-
sity could be used to obtain a point prediction (for example, the predictive
mean) or an interval prediction (similar in spirit to the Bayesian interval
discussed above) or to perform a hypotheses comparison.
ILLUSTRATION: POSTERIOR TRADE-OFF AND THE
NORMAL MEAN PARAMETER
Using an illustration, we show the effects prior distributions have on
posterior inference. For simplicity, we look at the case of a normal data
distribution with a known variance, σ 2 = 1. That is, we need to elicit a prior
distribution of the mean parameter, µ, only. We investigate the following
prior assumptions:
1. A noninformative, improper prior (Jeffreys’ prior): π(µ) ∝1.
2. A noninformative, proper prior: π(µ) = N(η, τ 2), where η = 0 and τ =
106.
3. An informative conjugate prior with subjectively determined hyperpa-
rameters: π(µ) = N(η, τ 2), where η = 0.02 and τ = 0.1.
21The predictive density is usually of known (closed) form under conjugate prior
assumptions.
22Here, we assume that θ is continuous, which is the case in most financial
applications.

36
BAYESIAN METHODS IN FINANCE
As mentioned earlier in the chapter, the relative strengths of the prior and
the sampling distribution determine the degree of trade-off of prior and data
information in the posterior. When the amount of available data is large, the
sampling distribution dominates the prior in the posterior inference. (In the
limit, as the number of observations grows indefinitely, only the sampling
distribution plays a role in determining posterior results.23) To illustrate this
sample-size effect, we consider the following two samples of data:
1. The monthly return on the S&P 500 stock index for the period January
1999 through December 2005 (a total of 192 returns).
2. The monthly return on the S&P 500 stock index for the period January
2005 through December 2005 (a total of 12 returns).
Let us denote the return data by the n × 1 vector r = (r1, r2, . . . , rn),
where n = 192 or n = 12. We assume that the sampling (data) distribu-
tion is normal, R ∼N(µ, σ 2). Combining the normal likelihood and the
noninformative improper prior, we obtain for the posterior distribution
of µ
p

µ | r, σ 2 = 1

∝(2π)−n/2 exp

−
n
i = 1(ri −µ)2
2

∝exp

−n(µ −ˆµ)2
2

,
(3.21)
where ˆµ is the sample mean as given in (3.8). Therefore, the posterior of
µ is a normal distribution with mean ˆµ and variance 1/n. As expected, the
data completely determine the posterior distributions for both data samples,
since we assumed prior ignorance about µ.
When a normal prior for µ, N(η, τ 2), is asserted, the posterior can
be shown to be normal as well. In the generic case, for an arbitrary data
variance σ 2, we have
p

µ | r, σ 2
= (2πσ 2)−n/2 exp

−
n
i = 1(ri −µ)2
σ 2

× (2πτ 2)−1/2 exp

−(µ −η)2
2τ 2

∝exp

−(µ −µ∗)2
2τ 2∗

,
(3.22)
23This statement is valid only if one assumes that the data-generating process remains
unchanged through time.

Prior and Posterior Information, Predictive Inference
37
where the posterior mean, µ*, is
µ∗= ˆµ
n
σ 2
n
σ 2 +
1
τ2
+ η
1
τ2
n
σ 2 +
1
τ2
(3.23)
and the posterior variance, τ 2*, is
τ 2∗=
1
n
σ 2 +
1
τ2
.
(3.24)
Notice that the posterior mean is a weighted average of the sample mean,
ˆµ, and the prior mean, η. The quantities 1/σ 2 and 1/τ 2 have self-explanatory
names: data precision and prior precision, respectively. The higher the
precision, the more concentrated the distribution around its mean value.24
Let us see how the information trade-off between the data and the prior is
reflected in the values of the posterior parameters.
In the case of the noninformative, proper prior, τ = 106. The right-
most term in (3.23) is then negligibly small and the posterior mean is
very close to the sample mean: µ∗≈ˆµ, while the posterior variance in
(3.24) is approximately equal to 1/n (substituting in σ 2 = 1). That is, for
both data samples, the noninformative proper prior produced posteriors
almost the same as in the case of the noninformative improper prior, as
expected.
Consider how the posterior is affected when informativeness of the
prior is increased, as in the third prior scenario. Exhibit 3.1 helps visualize
the posterior trade-off for the long and short data samples, respectively. The
smaller the amount of observed data, the larger the influence of the prior
on the posterior (the ‘‘closer’’ the posterior to the prior).
SUMMARY
In this chapter, Bayesian prior and posterior inference are described. We
discuss uninformative and informative priors. When a normal data density
is assumed, the choice of priors is often guided by arguments of analytical
tractability of the posterior distributions. Careful selection of the parameters
of the prior distributions is necessary to ensure that they accurately reflect the
24The posterior mean is an example for the shrinkage effect that combining prior
and data information has. See Chapter 6 for an extended discussion of shrinkage
estimators.

38
BAYESIAN METHODS IN FINANCE
−0.4
−0.3
−0.2
−0.1
0
0.1
0.2
0.3
0.4
0.5
Large sample
posterior
density
Small sample
posterior
density
Prior
density
EXHIBIT 3.1
Sample size and posterior trade-off for the normal mean parameter
researcher’s prior intuition. We look at both the full and empirical Bayesian
approaches to prior assertion. Posterior inference is straightforward when
the posteriors are analytically available.
In the next chapter, we discuss the univariate and multivariate linear
regression models, which, under the assumptions of normality of the regres-
sion disturbances and conjugate priors, are straightforward extensions of
this chapter’s framework.
APPENDIX: DEFINITIONS OF SOME UNIVARIATE
AND MULTIVARIATE STATISTICAL DISTRIBUTIONS
Here we review some statistical distributions commonly used in Bayesian
financial applications. Other distributions are defined in the chapters
where they are mentioned. See, for example, Chapter 13 for an overview
of several heavy-tailed and asymmetric distributions that have been

Prior and Posterior Information, Predictive Inference
39
employed
in
the
empirical
finance
literature
to
model
asset
returns.25
The Univariate Normal Distribution
A random variable, X, −∞< x < ∞, distributed with the normal (also
called Gaussian) distribution with mean µ and variance σ 2, has the density
function
f

x | µ, σ 2
=
1
√
2πσ
e
−(x−µ)2
2σ2 ,
(3.25)
where −∞< µ < ∞and σ > 0. The standard deviation, σ, is the scale of
the normal distribution. We denote the distribution by N

µ, σ 2
.
The Univariate Student’s t-Distribution
A random variable X, −∞< x < ∞, distributed with the Student’s
t-distribution with ν degrees of freedom, has the density function
f(x | ν, µ, σ) =
( ν+1
2 )
σ( ν
2)√νπ
	
1 + 1
ν
x −µ
σ
2
−(ν+1)/2
,
(3.26)
where  is the Gamma function, −∞< µ < ∞is the mode of X and σ > 0
is the scale parameter of X. We denote this distribution by t(ν, µ, σ). The
mean and variance of X are given, respectively, by
E(X) = µ
and
var(X) =
ν
ν −2σ 2.
(3.27)
The variance exists for values of ν greater than 2 and the mean—for ν
greater than 1.
The Inverted χ 2 Distribution
A random variable X, x > 0, distributed with the inverted χ 2 distribution
with ν degrees of freedom and scale parameter c, has the following density
25For details on the statistical properties of the distributions discussed below, see
Johnson, Kotz, and Balakrishnan (1995), Anderson (2003), Kotz, Balakrishnan, and
Johnson (2000), and Zellner (1971).

40
BAYESIAN METHODS IN FINANCE
function,
f(x | ν, c) =
1

 ν
2

ν
2
ν/2
cνx−( ν
2 +1) exp

−νc
2x

,
(3.28)
where ν > 0, c > 0, and x > 0. The inverted χ 2 distribution is denoted
as Inv−χ 2(ν, c). Its kernel consists of the nonconstant part of the density
function,
x−( ν
2 +1) exp

−νc
2x

.
The inverted χ 2 distribution is a particular case of the inverted gamma
distribution,
Inv-χ 2(ν, c) ≡IG
ν
2, νc
2

.
The mean (defined for ν > 2) and the variance (defined for ν > 4) of X are
given, respectively, by
E(X) =
ν
ν −2c
and
var(X) =
2ν2
(ν −2)2(ν −4)c2.
(3.29)
The Multivariate Normal Distribution
An n × 1 vector x = (x1, x2, . . . , xn)′, distributed with the multivariate
normal distribution, has a density
f(x | µ, ) = (2π)n/2||−1/2 exp

−1
2(x −µ)′−1(x −µ)

,
(3.30)
where the n × 1 vector of means is µ = (µ1, µ2, . . . , µn)′ and the n × n
matrix  is the (positive semidefinite) covariance matrix. The diagonal
elements of  are the variances of each of the components of x, while
the off-diagonal elements are the covariances, cov(xi, xj), i ̸= j, between
each two components of x. Since cov(xi, xj) is the same as cov(xj, xi),  is
symmetric and contains n(n −1)/2 distinct elements.
The Multivariate Student’s t-Distribution
An n × 1 vector x = (x1, x2, . . . , xn)′, distributed with the multivariate
(scaled, non-central) Student’s t-distribution, has the density
f(x | ν, µ, S) = C ×

ν + (x −µ)′S(x −µ)
−(n+ν)/2 ,

Prior and Posterior Information, Predictive Inference
41
where C = νν/2((ν+n)/2)|S|1/2
πn/2(ν/2)
, ν is the degrees-of-freedom parameter, regulating
the tail thickness, µ is the mean vector, and S is the scale matrix. We denote
the distribution by t(ν, µ, S). The covariance matrix of x is given by
 = S−1
ν
ν −2.
(3.31)
The covariance matrix exists for ν > 2, and the mean—for ν > 1.
The Wishart Distribution
Suppose we have observed a sample of N × 1 vectors, X1, . . . , Xt, . . . , XT.
The vectors are independently distributed with multivariate normal distribu-
tion, N(µ, ). The Wishart distribution arises in statistics as the distribution
of the quantity, Q,
Q =
T

i=1

Xt −X

Xt −X
′,
which is equal to T times the sample covariance matrix and X = 1
T
T
t=1 Xt.
If Q is a positive definite matrix, its density function is given by
f(Q | T, ) =
|Q|
1
2 (T−N−1)exp

−1
2tr−1Q

2NT/2 π N(N−1)/4 ||T/2 N
i=1 

(T + 1 −i)/2
.
(3.32)
The Wishart distribution is denoted by W(T −1, ).
The Inverted Wishart Distribution
In the Bayesian framework, the inverted Wishart distribution is the conjugate
prior distribution of the normal covariance matrix. Consider the positive
definite matrix Q above. Denote by S its inverse, S = Q−1. Its density is
given by
f(S | , ν) =
||ν/2
2νN/2 π N(N−1)/4 N
i=1 (ν −i + 1)/2
exp

−1
2trS−1

|S|(ν+n+1)/2
,
(3.33)
where  = −1 and ν is a (scalar) degrees-of-freedom parameter, such that
ν ≥N. We denote the distribution above as IW(, ν).26
26The notation W−1(, ν) is sometimes also used.

42
BAYESIAN METHODS IN FINANCE
The inverted Wishart distribution is a generalization of the inverted
gamma distribution to the multivariate case. The diagonal elements of
S have the inverted χ 2 distribution in (3.28).
The expectation of an inverted Wishart random variable is
E(S) = 
1
N −T −1.
(3.34)


## Bayesian Linear Regression Model

CHAPTER4
Bayesian Linear
Regression Model
R
egression analysis is one of the most common econometric tools
employed in the area of investment management. Since the follow-
ing chapters rely on it in the discussion of various financial applications,
here we review the Bayesian approach to estimation of the univariate and
multivariate regression models.
THE UNIVARIATE LINEAR REGRESSION MODEL
The univariate linear regression model attempts to explain the variability in
one variable (called the dependent variable) with the help of one or more
other variables (called explanatory or independent variables) by asserting a
linear relationship between them. We write the model as
Y = α + β1X1 + β2X2 + · · · βK −1XK −1 + ϵ,
(4.1)
where: Y = dependent variable.
Xk = independent (explanatory) variables, k = 1, . . . , K −1.
α = regression intercept.
βk = regression (slope) coefficients, k = 1, . . . , K −1, representing
the effect a unit change in Xk, k = 1, . . . , K −1, has on Y,
keeping the remaining independent variables, Xj, j ̸= k, fixed.
ϵ = regression disturbance.
The regression disturbance is the source of randomness about the lin-
ear (deterministic) relationship between the dependent and independent
43

44
BAYESIAN METHODS IN FINANCE
variables. Whereas α + β1X1 + · · · + βK−1XK−1 represents the part of Y’s
variability explained by Xk, k = 1, . . . , K −1, ϵ represents the variability in
Y left unexplained.1
Suppose that we have n observations of the dependent and the indepen-
dent variables available. These data are then described by
yi = α + β1x1, i + · · · + βK −1xK −1, i + ϵi
i = 1, . . . , n.
(4.2)
The subscript i, i = 1, . . . , n, refers to the ith observation of the respective
random variable. To describe the source of randomness, ϵ, one needs to
make a distributional assumption about it. For simplicity, assume that
ϵi, i = 1, . . . , n, are independently and identically distributed (i.i.d.)
with the normal distribution and have zero means and (equal) vari-
ances, σ 2. Then, the dependent variable, Y, has a normal distribution
as well,
yi ∼N(µi, σ 2),
(4.3)
where µi = α + β1x1,i + · · · + βK−1xK−1,i. Notice that the constant-variance
assumption in (4.3) is quite restrictive. We come back to this issue later in
the chapter.
The expression in (4.2) is often written in the following compact form:
y = Xβ + ϵ,
(4.4)
where y is a n × 1 vector,
y =


y1
y2
...
yn

,
β is a (K) × 1 vector,
β =


α
β1
...
βK −1

,
1We generally assume that the independent variables are fixed (nonstochastic).
However, see Chapter 7 for an application in which we do consider them random
and make distributional assumptions about them.

Bayesian Linear Regression Model
45
X is a n × (K) matrix whose first column consists of ones,
X =


1 x1, 1 · · · xK −1, 1
1 x1, 2 · · · xK −1, 2
...
...
...
...
1 x1, n · · · xK −1, n

,
and ϵ is a n × 1 vector,
ϵ =


ϵ1
ϵ2
...
ϵn

.
We write the normal distributional assumption for the regression dis-
turbances in compact form as
ϵ ∼N(0, σ 2In),
where In is a (n × n) identity matrix. The parameters in (4.4) we need
to estimate are β and σ 2. Assuming normally distributed disturbances, we
write the likelihood function for the model parameters as
L(α, β1, β2, σ | y, X) = (2πσ 2)−n/2
× exp

−1
2σ 2
n
	
i=1
(yi −α −β1x1, i −· · · −βK −1xK −1, i)2

.
Or, in vector notation, we have the likelihood function for the parame-
ters of a multivariate normal distribution,
L(β, σ | y, X) = (2πσ 2)−n/2 exp

−1
2σ 2 (y −Xβ)′(y −Xβ)

.
(4.5)
Bayesian Estimation of the Univariate Regression Model
In the classical setting, the regression parameters are usually estimated by
maximizing the model’s likelihood with respect to 
β and σ 2, for instance, the
likelihood in (4.5) if the normal distribution is assumed. When disturbances
are assumed to be normally distributed, the maximum likelihood and the

46
BAYESIAN METHODS IN FINANCE
ordinary least squares (OLS) methods produce identical parameter estimates.
It can be shown that the OLS estimator of the regression coefficients vector,
β, is given by
β = (X′X)−1Xy,
(4.6)
where the prime symbol (′) denotes a matrix transpose.2 The estimator of
σ 2 is3
σ 2 =
1
n −K

y −Xβ
′
y −Xβ

.
(4.7)
To account for the parameters’ estimation risk and to incorporate prior
information, regression estimation can be cast in a Bayesian setting. Our
earlier discussion of prior elicitation applies with full force here. We consider
two prior scenarios: a diffuse improper prior and an informative conjugate
prior for the regression parameter vector, ((β, σ 2)).
Diffuse Improper Prior
The joint diffuse improper prior for β and σ 2 is
given by
π(β, σ 2) ∝1
σ 2 ,
(4.8)
where the regression coefficients can take any real value, −∞< βk < ∞,
for k = 1, . . . , K, and the disturbance variance is positive, σ 2 > 0.
Combining the likelihood in (4.5) and the prior above, we obtain the
posteriors of the model parameters as follows:
■The posterior distribution of β conditional on σ 2 is (multivariate)
normal:4
p

β | y, X, σ 2
= N
β, (X′X)−1σ 2
,
(4.9)
where β is the OLS estimate in (4.6) and (X′X)−1σ 2 is the covariance
matrix of β.
2In order for the inverse matrix in (4.6) to exist, it is necessary that X′X
be
nonsingular, that is, that the n × K matrix X have a rank K (all its columns be
linearly independent).
3The MLE of σ 2 is in fact
σ 2
MLE = 1
n

y −Xβ
′
y −X
β

.
However, as it is not unbiased, the estimator in (4.7) is more often employed.
4See the appendix to Chapter 3 for the definition of the multivariate normal
distribution.

Bayesian Linear Regression Model
47
■The posterior distribution of σ 2 is inverted χ 2:
p

σ 2 | y, X

= Inv-χ 2 
n −K,σ 2
,
(4.10)
where σ 2 is the estimator of σ 2 in (4.7).
It could be useful to obtain the marginal (unconditional) distribution of
β in order to characterize it independently of σ 2 (as in practical applications,
the variance is an unknown parameter).5 It can be shown, by integrating
the joint posterior distribution
p

β, σ 2 | y, X

= p

β | y, X, σ 2
p

σ 2 | y, X

with respect to σ 2, that β’s unconditional posterior distribution is a multi-
variate Student’s t-distribution with a kernel given by6
p (β | y, X) ∝

(n −K) + (β −
β)′ X′X
σ 2 (β −
β)
−n/2
.
(4.11)
Notice that integrating σ 2 out makes β’s distribution more heavy-tailed,
duly reflecting the uncertainty about σ 2’s true value. Although β’s mean
vector is unchanged, its variance increased (on average) by the term
ν/(ν −2):
β = σ 2(X′X)−1
ν
ν −2,
where ν = n −K is the degrees of freedom parameter of the multivariate
Student’s t-distribution.
In conclusion of our discussion of the posteriors in the diffuse improper
prior scenario, suppose we are interested particularly in one of the regression
coefficients, say βk. For example, βk could be the return on a factor (size,
value, momentum, etc.) in a multifactor model of stock returns. It can be
shown that the standardized βk has a Student’s t-distribution with n −K
5In fact, using the numerical methods in Chapter 5, it is possible to describe the
distribution of β, even without knowing its unconditional distribution, by employing
the Gibbs sampler and making inferences on the basis of samples drawn from β’s
and σ 2’s posterior distributions.
6See the appendix to Chapter 3 for the definition of the multivariate Student’s
t-distribution.

48
BAYESIAN METHODS IN FINANCE
degrees of freedom as its marginal posterior distribution,
βk −βk
(hk,k)1/2 | y, X ∼tn −K,
(4.12)
where hk,k is the kth diagonal element of σ 2(X′X)−1 and βk is the OLS
estimate of βk (the corresponding component of β). Bayesian intervals for
βk can then be constructed analytically.
Informative Prior
Under the normality assumption for the regression resid-
uals in (4.1), one can make use of the natural conjugate framework to reflect
the existing prior knowledge and to obtain convenient analytical posterior
results. Thus, let us assume that the regression coefficients vector, β, has a
normal prior distribution (conditional on σ 2) and σ 2—an inverted χ 2 prior
distribution:
β | σ ∼N(β0, σ 2A)
(4.13)
and
σ 2 ∼Inv-χ 2 
ν0, c2
0

.
(4.14)
Four parameters have to be determined a priori: β0, A, ν0, and c2
0. The
scale matrix A is often chosen to be τ −1(X′X)−1 in order to obtain a prior
covariance the same as the covariance matrix of the OLS estimator of β up
to a scaling constant. Varying the (scale) parameter, τ, allows one to adjust
the degree of confidence one has that β’s mean is β0—the smaller the value
of τ, the greater the degree of uncertainty about β.
The easiest way to assert the prior mean, β0, is to fix it at some
default value (such as 0, depending on the estimation context), unless
more specific prior information is available, or to set it equal to the OLS
estimate, β, obtained from running the regression (4.1) on a prior sample
of data.7
The parameters of the inverted χ 2 distribution could be asserted using
a prior sample of data as follows:
ν0 = n0 −K
c2
0 = 1
ν0

y0 −X0β0
′
y0 −X0β0

.
7Recall our earlier discussion of prior parameter assertion—the full Bayesian
approach calls for specifying the hyperprior parameters independently of the data
used for model estimation. In contrast, an empirical Bayesian approach would use
the OLS estimate, β, obtained from the data sample used for estimation.

Bayesian Linear Regression Model
49
where the subscript, 0, refers to the prior data sample. If no prior data
sample is available, the inverted χ 2 hyperparameters could be specified
by expressing beliefs about the prior mean and variance of σ 2, using the
expressions in (3.28) in Chapter 3.
The posterior distributions for the model parameters, β and σ 2 have the
same form as the prior distributions, however, their parameters are updated
to reflect the data information, along with the prior beliefs.
■The posterior for β is
p

β | y, X, σ 2
= N

β∗, β

,
(4.15)
where the posterior mean and covariance matrix of β are given by
β∗=

A−1 + X′X
−1 
A−1β0 + X′Xβ

(4.16)
and
β = σ 2 
A−1 + X′X
−1
.
(4.17)
We can observe that the posterior mean is a weighted average of the
prior mean and the OLS estimator of β, as noted earlier in the chapter
as well. See Chapter 6 for more details on this shrinkage effect.
■The inverted χ 2 posterior distribution of σ 2 is
p

σ 2 | y, X

= Inv-χ 2 
ν∗, c2∗
.
(4.18)
The parameters of σ 2’s posterior distribution are given by
ν∗= ν0 + n
(4.19)
and
ν∗c2∗= (n −K)σ 2 + (β0 −β)′H(β0 −
β) + ν0c2
0,
(4.20)
where H =

(X′X)−1 + A
−1
As done earlier, we can derive the marginal posterior distribution of β
by integrating σ 2 out of the joint posterior distribution. We obtain again a
multivariate Student’s t-distribution, t(t(ν∗, β∗, Q)),
p (β | y, X) ∝

ν∗+ (β −β∗)′Q(β −β∗)
−ν∗/2 ,
(4.21)
where Q =

A−1 + X′X

/c2∗.

50
BAYESIAN METHODS IN FINANCE
The mean of β remains the same, β∗(as it is independent of σ 2), while
its unconditional (with respect to σ 2) covariance matrix can be calculated
using (3.30) in Chapter 3. The marginal posterior distribution for a single
regression coefficient, βk, can be shown to be
βk −β∗
k
(qk,k)1/2 | y, X ∼tν0+n−K,
(4.22)
where qk,k is the kth diagonal element of Q−1 and β∗
k is the kth component
of β∗.
Prediction
Suppose that we would like to predict the dependent vari-
able, Y, p steps ahead in time and denote by the p × 1 vector y =
(yT+1, yT+2, . . . , yT+p) these future observations. We assume that the future
observations of the independent variables are known and given by X. Let
us use (3.20) in Chapter 3 to express the predictive density in the linear
regression context,
p(y | y, X, X) =

p(y | β, σ 2, X)p(β, σ 2 | y, X) dβ, σ 2,
(4.23)
where p(β, σ 2 | y, X) is the joint posterior distribution of β and σ 2.
It can be shown that the predictive distribution is multivariate Stu-
dent’s t. Under the diffuse improper prior scenario, the predictive distribu-
tion is
p(y | y, X, X) = t(n −K, X β, S),
(4.24)
where S = σ 2(Ip + X(X′X)−1X
′) and β is the posterior mean of β under the
diffuse improper scenario. In the case of the informative prior, the predictive
distribution of y is
p(y | y, X, X) = t(ν0 + n, X β∗, V),
(4.25)
where V = c2∗(Ip + X(A−1 + X′X)−1X
′) and β∗is the posterior mean of β in
(4.16).
Certainly, it is again possible to derive the distribution for the pre-
dictive distribution for a single component of y—a univariate Student’s
t-distribution—in the two scenarios, respectively,

yk −
Xkβk
s1/2
k, k
∼tn −K,
(4.26)

Bayesian Linear Regression Model
51
where 
Xk is the kth row of X (the observations of the independent variables
pertaining to the kth future period), and sk,k is the kth diagonal element of
the scale matrix, S, in (4.24), and

yk −
Xkβ∗
k
v1/2
k, k
∼tν0+n−K,
(4.27)
where vk,k is the kth diagonal element of the scale matrix, V, in (4.25).
The Case of Unequal Variances
We mentioned earlier in the chapter that
the equal-variance assumption in (4.3) might be somewhat restrictive. Two
examples would help clarify what that means. First, suppose that the n
observations of Y are collected through time. It is a common practice in
statistical estimation to use the longest available data record, likely spanning
many years. Changes in the underlying economic or financial paradigms,
the way data are recorded, and so on, that might have occurred during the
sample period might have caused the variance of the random variable (as
well as its mean, for that matter) to shift.8 The equal-variance assumption
would then lead to variance overestimation in the low-variance period(s) and
variance underestimation in the high-variance period(s). When the variance
(and/or mean) shifts permanently, the so-called ‘‘structural-break’’ models
can be employed to reflect it.9 In Chapter 11, we discuss the so-called
‘‘regime-switching’’ models, in which parameters are allowed to change
values according to the state of the world prevailing in a particular period
in time.
Second, if our estimation problem is based on observations recorded
at a particular point in time (producing a cross-sectional sample), the
equal-variance assumption might be violated again. All units in our sample
could potentially have different variances, so that var(yi) = σ 2
i , instead of
var (yi) = σ 2 as in (4.3), for i = 1, . . . , n. Estimation would then be
severely hampered because this would imply a greater number of unknown
parameters (variances and regression coefficients) than available data points.
In practice one would perhaps be able to identify groups of homoge-
neous sample units that can be assumed to have equal variances. Suppose, for
instance, that the cross-sectional sample consists of small-cap and large-cap
stock returns. One could then expect that the return variances (volatilities)
across the two groups differ but assume that companies within each group
8Returns on interest rate instruments and foreign exchange are particularly likely to
exhibit structural breaks.
9See, for example, Wang and Zivot (2000).

52
BAYESIAN METHODS IN FINANCE
have equal return volatilities. More generally, one could assume some form
of functional relation among the unknown variances—this would serve to
reduce the number of unknown parameters to estimate. We now provide
one possible way to address the variance inequality in the case when the
sample observations can be divided into two homogeneous (with respect to
their variances) groups or when a structural break (whose timing we know)
is present in the sample.10
Denote the observations from the two groups by y1 = (y1, 1, y1, 2, . . . , y1, n1)
and y2 = (y2, 1, y2, 2, . . . , y2, n2), so that y = (y1, y2) and n1 + n2 = n. The
univariate regression setup in (4.1) is modified as
y1 = X1β + ϵ1
y2 = X2β + ϵ2,
(4.28)
where X1 and X2 are, respectively, (n1 × K) and (n2 × K) matrices of
observations of the independent variables. The disturbances are assumed to
be independent and distributed as
ϵ1 ∼N(0, σ 2
1 In1)
ϵ2 ∼N(0, σ 2
2 In2),
(4.29)
where σ 2
1 ̸= σ 2
2 . The likelihood function for the model parameters, β, σ 2
1 ,
and σ 2
2 is given by
L

β, σ 2
1 , σ 2
2 | y, X1, X2

∝(σ 2
1 )−n1
2 (σ 2
2 )−n2
2
× exp

−1
2σ 2
1
(y1 −X1β)′(y1 −X1β)
−1
2σ 2
2
(y2 −X2β)′(y2 −X2β)

.
(4.30)
A noninformative diffuse prior can be asserted, as in (3.5), by assuming
that the parameters are independent. The prior is written, then, as
π(β, σ1, σ2) ∝
1
σ1σ2
.
It is straightforward to write out the joint posterior density of β, σ 2
1 ,
and σ 2
2 , which can be integrated with respect to the two variances to obtain
the marginal posterior distribution of the regression coefficients vector.
10See Chapter 4 in Zellner (1971).

Bayesian Linear Regression Model
53
Zellner (1971) shows that the marginal posterior of β is the product of two
multivariate Student’s t-densities (not a surprising result, since the likelihood
in (4.30) is the product of two normal likelihoods),
p(β | y, X1, X2) ∝t(ν1, 
β1, S1) × t(ν2, 
β2, S2),
where, for i = 1, 2, βi is the OLS estimator of β in the two expressions in
(4.28) viewed as separate regressions,
νi = ni −K,
Si = s2
i (X′
iXi),
and
s2
i =
1
ni −K(yi −Xiβi)′(yi −Xiβi).
Zellner shows that the marginal posterior of β above can be approximated
with a normal distribution (through a series of asymptotic expansions).
We conclude this discussion with a brief comment on a related violation
of the univariate regression assumptions outlined earlier in the chapter.
When analyzing data collected through time, it is more likely than not that
the data are serially correlated. That is, the assumption that the regression
disturbances are independent is violated. For example, dependence of returns
through time might be caused by time-dependence of the return volatility
(and/or the mean of returns). We discuss volatility modeling in Chapters 10,
11, and 12.
Illustration: The Univariate Linear Regression Model
We now illustrate the posterior and predictive inference in a univariate linear
regression model. We restrict our attention to the diffuse noninformative
prior and the informative prior discussed thus far in order to take advantage
of their analytical convenience. In the next chapter, we show how to employ
numerical computation to tackle inference when no analytical results are
available.
Our data consist of the monthly returns on 25 portfolios; the compa-
nies in each portfolio are ranked according to market capitalization and
book-to-market (BM) ratios. (See Chapter 9 for further details on this data
set.) The returns we use for model estimation span the period from January
1995 to December 2005 (a total of 132 time periods). We extract the factors
that best explain the variability of returns of the 25 portfolios using prin-
cipal components analysis. (See Chapter 14 for more details on multifactor
models.) The first five factors explain around 95% of the variability and
we use their returns as the independent variables in our linear regression

54
BAYESIAN METHODS IN FINANCE
model, making up the matrix X (the first column is a column of ones). The
return on the portfolio consisting of the companies with the smallest size
and BM ratios is the dependent variable y. In addition, returns recorded
for the months from January 1990 to December 1994 (a total of 60 time
periods) are employed to compute the hyperparameters of the informative
prior distributions, in the manner explained in the previous section. Our
interest centers primarily on the posterior inference for the regression coef-
ficients, βk, k = 1, . . . , 6—the intercept and the five factor exposures (in the
terminology of multifactor models).
Posterior Distributions
The prior and posterior parameter values for β
are given in Exhibit 4.1 Part A of the exhibit presents the results under
the diffuse improper prior assumption and Part B under the informative
prior assumption. In parentheses are the posterior standard deviations,
computed using the expression in (3.26) in Chapter 3. The OLS estimates
of the regression coefficients are, of course, given by the posterior means
in the diffuse prior scenario. Notice how the posterior mean of β under
the informative prior is shrunk away from the OLS estimate and toward
the prior value, for the chosen value of τ = 1. We could introduce more
uncertainty into the prior distribution of β (make it less informative) by
choosing a smaller value of τ —the posterior mean of β would then be
closer to the OLS estimate. Conversely, the stronger our prior belief about
the mean of β, the closer the posterior mean would be to the prior mean.
Credible Intervals
Since the marginal posterior distribution of βk, k =
1, . . . , 6, is of known form—Student’s t—we can compute analytically the
Bayesian confidence intervals for the regression coefficients. We provide
several quantiles from the distribution of each βk. For example, under
the diffuse improper prior, the 95% (symmetric) Bayesian interval for
β2 is (−0.3187, −0.3029), while, under the informative prior, the 99%
(symmetric) Bayesian interval for β6 is (−0.0162, 0.1180).11
Hypothesis Comparison
In the frequentist regression tradition, testing the
significance of the regression coefficients is of great interest—the validity
of the null hypothesis βk = 0 is examined. In the Bayesian setting, we
could evaluate and compare the posterior probabilities, P(βk⟩0 | y, X) and
P(βk < 0 | y, X) (given in Exhibit 4.1 for each factor exposure). We could
safely conclude that the exposures on Factor 1 through Factor 4 are different
from zero—the mass of their posterior distributions is concentrated on
11Notice that, since the Student’s t-distribution is unimodal, these (symmetric)
intervals are also the HPD intervals.

Bayesian Linear Regression Model
55
b2
b3
b4
b5
b6
Intercept
Factor1
Factor 2
Factor 3
Factor 4
Factor 5
Prior Mean
Posterior Mean
Posterior Standard
Deviation
b0.01
b0.05
b0.25
b0.75
b0.95
A.
b0.99
–
0.0048
(0.0011)
0.0021
0.0029
0.0040
0.0055
0.0067
0.0075
–
−0.3108
(0.0048)
−0.3219
−0.3187
−0.314
−0.3075
−0.3029
−0.2996
–
−0.3997
(0.0103)
−0.4238
−0.4168
−0.4067
−0.3928
−0.3827
−0.3757
–
0.0648
(0.0202)
0.0174
0.0312
0.0511
0.0784
0.0983
0.1121
–
−0.4132
(0.0297)
−0.4826
−0.4624
−0.4333
−0.3931
−0.364
−0.3438
−0.0042
(0.0410)
−0.1000
−0.0721
−0.0319
−0.0235
0.0636
–
0.0915
B.
Prior Mean
Posterior Mean
Posterior Standard
Deviation
b0.01
b0.05
b0.25
b0.75
b0.95
b0.99
0.0037
0.0042
(0.0008)
0.0024
0.0029
0.0037
0.0048
0.0056
0.0061
−0.2952
−0.303
(0.0033)
−0.3108
−0.3085
−0.3052
−0.3007
−0.2975
−0.2952
−0.4217
−0.4107
(0.0072)
−0.4276
−0.4226
−0.4156
−0.4059
−0.3986
−0.3939
0.038
0.0514
(0.0142)
0.0182
0.0280
0.0418
0.0609
0.0747
0.0844
−0.2784
−0.3458
(0.0208)
−0.3945
−0.3801
−0.3598
−0.3318
−0.3115
−0.2972
0.1063
0.0510
(0.0287)
−0.0162
0.0038
0.0318
0.0703
0.0983
0.1180
b1
EXHIBIT 4.1
Posterior inference for β
Note: Part A contains posterior results under the diffuse improper prior; Part B
contains posterior results under the informative prior.
either positive or negative values. For the exposure on Factor 5, the picture
is less than clear-cut. Under the diffuse, improper prior, a bit over 50%
of the posterior mass is below zero and the rest—above zero. Therefore,
one would perhaps take the pertinence of this factor for explaining the
variability of the return on the small-cap/small-BM portfolio with a grain
of salt. Notice, however, how the situation changes in the informative-prior
case. More than 95% of the posterior mass is above zero. The strong prior
beliefs about a positive mean of β6 lead to the conclusion that the exposure
of the portfolio returns to Factor 5 is not zero. Exhibit 4.2 further illustrates
these observations.

56
BAYESIAN METHODS IN FINANCE
−0.25 −0.2 −0.15 −0.1 −0.05
0
0.05
0.1
0.15
0.2
0
0.002
0.006
0.01
0.014
0.018
−0.1
−0.05
0
0.05
0.1
0.15
0.2
0.25
0
0.002
0.004
0.006
0.008
0.01
0.012
EXHIBIT 4.2
Posterior densities of β6 under the two prior
scenarios
Note: The plot on the top refers to the diffuse improper prior;
the plot on the bottom—to the informative prior.
THE MULTIVARIATE LINEAR REGRESSION MODEL
Quite often in finance, and especially in investment management, one is
faced with modeling data consisting of many assets whose returns or
other attributes are not independent. Casting the problem in a multivariate

Bayesian Linear Regression Model
57
framework is one way to tackle dependencies between assets.12 In this
section, we outline the basics of multivariate regression estimation within the
Bayesian setting. For applications to portfolio construction, see Chapters 6
through 9.
Suppose that T observations are available on N dependent variables.
We arrange these in the T × N matrix, Y,
Y =


y1
...
yt
...
yT


=


y1, 1 y1, 2 . . .
y1, N
. . . . . . . . . . . . . . . . . . .
yt, 1
yt, 2 . . .
yt, N
. . . . . . . . . . . . . . . . . . .
yT, 1 yT, 2 . . .
yT, N


.
The multivariate linear regression is written as
Y = XB + U,
(4.31)
where: X = T × K matrix of observations of the K independent variables,
X =


x1
...
xt
...
xT


=


x1, 1 x1, 2 . . .
x1, K
. . . . . . . . . . . . . . . . . . .
xt, 1
xt, 2 . . .
xt, K
. . . . . . . . . . . . . . . . . . .
xT, 1 xT, 2 . . . xT, K


,
B = K × N matrix of regression coefficients,
B =


α
β1
. . .
βK

=


α1
α2
. . .
αN
β1, 1 β1, 2 . . . β1, N
. . . . . . . . . . . . . . . . . . .
βK, 1 βK, 2 . . . βK, N

,
12We note, in passing, that although the multivariate normal distribution is usually
assumed because of its analytical tractability, dependencies among asset returns
could be somewhat more complex than what the class of elliptical distributions (to
which the normal distribution belongs) is able to describe. Alternative distributional
assumptions could be made at the expense of analytical convenience and occasional
substantial estimation problems (especially, in high-dimensional settings). A more
flexible way of dependence modeling is provided through the use of copulas.
Unfortunately, copula estimation could also suffer from estimation problems. We
briefly discuss copulas in Chapter 13.

58
BAYESIAN METHODS IN FINANCE
U = T × N matrix of regression disturbances,
U =


u1
...
ut
...
uT


=


u1, 1 u1, 2 . . . u1, N
. . . . . . . . . . . . . . . . . . .
ut, 1
ut, 2 . . .
ut, N
. . . . . . . . . . . . . . . . . . .
uT, 1 uT, 2 . . . uT, N


.
The first column of X usually consists of ones to reflect the presence of an
intercept. In the multivariate setting, the usual linear regression assumption
that the disturbances are i.i.d. means that each row of U is an independent
realization from the same N-dimensional multivariate distribution. We
assume that this distribution is multivariate normal with zero mean and
covariance matrix, ,
ut ∼N(0, ),
(4.32)
for t = 1, . . . , T. The off-diagonal elements of  are nonzero, as we assume
the dependent variables are correlated, and the covariance matrix contains
N variances and N(N −1)/2 distinct covariances.
Using the expression for the density of the multivariate normal distri-
bution in (3.28), we write the likelihood function for the unknown model
parameters, B and , as13
L(B, |Y, X) ∝||−T/2 exp

−1
2
T
	
t = 1
(yt −xtB)	−1(yt −xtB)′

,
(4.33)
where || is the determinant of the covariance matrix. We now turn to
specifying the prior distributional assumptions for B and .
Diffuse Improper Prior
The lack of specific prior knowledge about the elements of B and  can be
reflected by employing the Jeffreys’ prior, which in the multivariate setting
13The expression in the exponent in (4.33) could also be written as
−1
2tr(Y −XB)′(Y −XB)−1,
where tr denotes the trace operator, which sums the diagonal elements of a square
matrix.

Bayesian Linear Regression Model
59
takes the form14
π(B, ) ∝||−N+1
2 .
(4.34)
The posterior distributions parallel those in the univariate case. With the
risk of stating the obvious, note that B is a random matrix; therefore, its
posterior distribution, conditional on , will be a generalization of the
multivariate normal posterior distribution in (4.9). To describe it, we first
vectorize (expand column-wise) the matrix of regression coefficients, B, and
denote the resulting KN × 1 vector by β,
β = vec(B) =


α′
β′
1...
β′
K

,
by stacking vertically the columns of B′. It can be shown that β’s posterior
distribution, conditional on , is a multivariate normal given by
p (β | Y, X, ) = N
β,  ⊗(X′X)−1
,
(4.35)
where β = vec(B) = vec

(X′X)−1(X′Y)

is the vectorized OLS estimator of
B and ⊗denotes the Kronecker product.15
The posterior distribution of  can be shown to be the inverted Wishart
distribution (the multivariate analog of the inverted gamma distribution),16
p ( | Y, X) = IW (ν∗, S) ,
(4.36)
14As in the univariate case, we assume independence between (the elements of) B
and .
15The Kronecker product is an operator for direct multiplication of matrices (which
are not necessarily compatible). For two matrices, A of size m × n and B of size
p × q, the Kronecker product is defined as
A ⊗B =


a1,1B
a1,2B . . . a1,nB
. . . . . . . . . . . . . . . . . . . . .
am,1B am,2B . . . am,nB

,
resulting in an mp × nq block matrix.
16See the appendix to Chapter 3 for the definition of the inverted Wishart distribu-
tion.

