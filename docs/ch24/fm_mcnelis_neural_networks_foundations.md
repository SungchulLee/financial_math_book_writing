# Neural Networks in Finance: Foundations

!!! info "Source"
    **Neural Networks in Finance: Gaining Predictive Edge in the Market** by Paul D. McNelis, Academic Press, 2005.
    These notes are used for educational purposes.

## Introduction

xii
Preface
While the development of faster and faster computer hardware has helped
to minimize this problem, the specific way of conceptualizing problems
continues to play an important role in how quickly reliable results may be
obtained. Speed relates both to computational hardware and software.
Forecasting, classification of risk, and dimensionality reduction or distil-
lation of information from dispersed signals in the market, are three tools
for effective portfolio management and broader decision making in volatile
markets yielding “noisy” data. These are not simply academic exercises.
We want to forecast more accurately to make better decisions, such as to
buy or sell particular assets. We are interested in how to measure risk,
such as classifying investment opportunities as high or low risk, not only to
rebalance a portfolio from more risky to less risky assets, but also to price
or compensate for risk more accurately.
Even in a policy context, decisions have to be made in the context of
many disparate signals coming from volatile or evolving financial markets.
As Othmar Issing of the European Central Bank noted, “disturbances have
to be evaluated as they come about, according to their potential for propa-
gation, for infecting expectations, for degenerating into price spirals” [Issing
(2002), p. 21].
How can we efficiently distill information from these market signals for
better diversification and effective hedging, or even better stabilization
policy? All of these issues may be addressed very effectively with neural
network methods. Neural networks help us to approximate or “engineer”
data, which, in the words of Wolkenhauer, is both the “art of turn-
ing data into information” and “reasoning about data in the presence of
uncertainty” [Wolkenhauer (2001), p. xii]. This book is about predictive
accuracy with neural networks, encompassing forecasting, classification,
and dimensionality reduction, and thus involves data engineering.1
The benchmark against which we compare neural network performance
is the time-honored linear regression model. This model is the starting
point of any econometric modeling course, and is the standard workhorse in
econometric forecasting. While there are doubtless other nonlinear methods
against which we can compare the performance of neural network methods,
we choose the linear model simply because it is the most widely used and
most familiar method of applied researchers for forecasting. The neural
network is the nonlinear alternative.
Most of modern finance theory comes from microeconomic optimization
and decision theory under uncertainty. Economics was originally called the
“dismal science” in the wake of John Malthus’s predictions about the rel-
ative rates of growth of population and food supply. But economics can
be dismal in another sense. If we assume that our real-world observations
1Financial engineering more properly focuses on the design and arbitrage-free pricing
of financial products such as derivatives, options, and swaps.

Preface
xiii
come from a linear data generating process, that most shocks are from
an underlying normal distribution and represent small deviations around
a steady state, then the standard tools of classical regression are perfectly
appropriate. However, making use of the linear model with normally gen-
erated disturbances may lead to serious misspecification and mispricing of
risk if the real world deviates significantly from these assumptions of lin-
earity and normality. This is the dismal aspect of the benchmark linear
approach widely used in empirical economics and finance.
Neural network methods, coming from the brain science of cognitive
theory and neurophysiology, offer a powerful alternative to linear models for
forecasting, classification, and risk assessment in finance and economics. We
can learn once more that economics and finance need not remain “dismal
sciences” after meeting brain science.
However, switching from linear models to nonlinear neural network alter-
natives (or any nonlinear alternative) entails a cost. As we discuss in
succeeding chapters, for many nonlinear models there are no “closed form”
solutions. There is the ever-present danger of finding locally optimal rather
than globally optimal solutions for key problems. Fortunately, we now
have at our disposal evolutionary computation, involving the use of genetic
algorithms. Using evolutionary computation with neural network models
greatly enhances the likelihood of finding globally optimal solutions, and
thus predictive accuracy.
This book attempts to give a balanced critical review of these methods,
accessible to students with a strong undergraduate exposure to statistics,
econometrics, and intermediate economic theory courses based on calculus.
It is intended for upper-level undergraduate students, beginning gradu-
ate students in economics or finance, and professionals working in business
and financial research settings. The explanation attempts to be straightfor-
ward: what these methods are, how they work, and what they can deliver
for forecasting and decision making in financial markets. The book is not
intended for ordinary M.B.A. students, but tries to be a technical expos´e
of a state-of-the-art theme for those students and professionals wishing to
upgrade their technical tools.
Of course, readers will have to stretch, as they would in any good chal-
lenging course in statistics or econometrics. Readers who feel a bit lost
at the beginning should hold on. Often, the concepts become much clearer
when the applications come into play and when they are implemented com-
putationally. Readers may have to go back and do some further review of
their statistics, econometrics, or even calculus to make sense of and see the
usefulness of the material. This is not a bad thing. Often, these subjects
are best learned when there are concrete goals in mind. Like learning a lan-
guage, different parts of this book can be mastered on a need-to-know basis.
There are several excellent books on financial time series and finan-
cial econometrics, involving both linear and nonlinear estimation and

xiv
Preface
forecasting methods, such as Campbell, Lo, and MacKinlay (1997); Frances
and van Dijk (2000); and Tsay (2002). In additional to very careful and
user-friendly expositions of time series econometrics, all of these books have
introductory treatments of neural network estimation and forecasting. This
work follows up these works with expanded treatment, and relates neural
network methods to the concepts and examples raised by these authors.
The use of the neural network and the genetic algorithm is by its nature
very computer intensive. The numerical illustrations in this book are based
on the MATLAB programming code. These programs are available on the
website at Georgetown University, www.georgetown.edu/mcnelis. For those
who do not wish to use MATLAB but want to do computation, Excel add-in
macros for the MATLAB programs are an option for further development.
Making use of either the MATLAB programs or the Excel add-in pro-
grams will greatly facilitate intuition and comprehension of the methods
presented in the following chapters, and will of course enable the reader
to go on and start applying these methods to more immediate problems.
However, this book is written with the general reader in mind — there
is no assumption of programming knowledge, although a few illustrative
MATLAB programs appear in the text. The goal is to help the reader
understand the logic behind the alternative approaches for forecasting, risk
analysis, and decision-making support in volatile financial markets.
Following Wolkenhauer (2001), I struggled to impose a linear ordering
on what is essentially a web-like structure. I know my success in this can
be only partial. I encourage readers to skip ahead to find more illustrative
examples of the concepts raised in earlier parts of the book in succeeding
chapters.
I show throughout this book that the application of neural network
approximation coupled with evolutionary computational methods for esti-
mation have a predictive edge in out-of-sample forecasting. This predictive
edge is relative to standard econometric methods. I do not claim that
this predictive edge from neural networks will always lead to opportuni-
ties for profitable trading [see Qi (1999)], but any predictive edge certainly
enhances the chance of finding such opportunities.
This book grew out of a large and continuing series of lectures given in
Latin America, Asia, and Europe, as well as from advanced undergraduate
seminars and graduate-level courses at Georgetown University and Boston
College. In Latin America, the lectures were first given in S˜ao Paulo, Brazil,
under the sponsorship of the Brazilian Association of Commercial Bankers
(ABBC), in March 1996. These lectures were offered again in March 1997
in S˜ao Paulo, in August 1998 at Banco do Brasil in Brasilia, and later that
year in Santiago, Chile, at the Universidad Alberto Hurtado.
In Asia and Europe, similar lectures took place at the Monetary Policy
and Economic Research Department of Bank Indonesia, under the spon-
sorship of the United States Agency for International Development, in

Preface
xv
January 1996. In May 1997 a further series of lectures on this subject
took place under the sponsorship of the Programme for Monetary and
Financial Studies of the Department of Economics of the University of
Melbourne, and in March of 1998 a similar course was offered at the
Facultat d’Economia of the Universitat Ramon Llull sponsored by the
Callegi d’Economistes de Calalunya in Barcelona.
The Center for Latin American Economics of the Research Department
of the Federal Reserve Bank of Dallas provided the opportunity in the
autumn of 1997 to do some of the initial formal research for the financial
examples illustrated in this book. In 2003 and early 2004, the Hong Kong
Institute of Monetary Research was the center for a summer of research on
applications of neural network methods for forecasting deflationary cycles
in Hong Kong, and in 2004 the School of Economics and Social Sciences
at Singapore Management University and the Institute of Mathematical
Sciences at the National University of Singapore were hosts for a seminar
and for research on nonlinear principal components
Some of the most useful inputs for the material for this book came
from discussions with participants at the International Joint Conference
on Neural Networks (IJCNN) meetings in Washington, DC, in 2001, and
in Honolulu and Singapore in 2002. These meetings were eye-openers for
anyone trained in classical statistics and econometrics and illustrated the
breadth of applications of neural network research.
I wish to thank my fellow Jesuits at Georgetown University and in
Washington, DC, who have been my “company” since my arrival at George-
town in 1977, for their encouragement and support in my research under-
takings. I also acknowledge my colleagues and students at Georgetown
University, as well as economists at the universities, research institutions,
and central banks I have visited, for their questions and criticism over the
years. We economists are not shy about criticizing one another’s work,
but for me such criticism has been more gain than pain. I am particularly
grateful to the reviewers of earlier versions of this manuscript for Elsevier
Academic Press. Their constructive comments gave me new material to
pursue and enhanced my own understanding of neural networks.
I dedicate this book to the first member of the latest generation of my
clan, Reese Anthony Snyder, born June 18, 2002.


1
Introduction
1.1
Forecasting, Classification, and
Dimensionality Reduction
This book shows how neural networks may be put to work for more accurate
forecasting, classification, and dimensionality reduction for better decision
making in financial markets — particularly in the volatile emerging markets
of Asia and Latin America, but also in domestic industrialized-country asset
markets and business environments.
The importance of better forecasting, classification methods, and dimen-
sionality reduction methods for better decision making, in the light of
increasing financial market volatility and internationalized capital flows,
cannot be overexaggerated. The past two decades have witnessed extreme
macroeconomic instability, first in Latin America and then in Asia. Thus,
both financial analysts and decision makers cannot help but be interested
in predicting the underlying rates of return and spreads, as well as the
default rates, in domestic and international credit markets.
With the growth of the market in financial derivatives such as call and
put options (which give the right but not the obligation to buy or sell assets
at given prices at preset future periods), the pricing of instruments for hedg-
ing positions on underlying risky assets and optimal portfolio diversification
have become major activities in international investment institutions. One
of the key questions facing practitioners in financial markets is the correct
pricing of new derivative products as demand for these instruments grows.

2
1. Introduction
To put it bluntly, if practitioners in these markets do not wish to be “taken
to the cleaners” by international arbitrageurs and risk management spe-
cialists, then they had better learn how to price their derivative offerings
in ways that render them arbitrage-free. Correct pricing of risk, of course,
crucially depends on the correct understanding of the process driving the
underlying rates of return. So correct pricing requires the use of models
that give relatively accurate out-of-sample forecasts.
Forecasting simply means understanding which variables lead or help to
predict other variables, when many variables interact in volatile markets.
This means looking at the past to see what variables are significant lead-
ing indicators of the behavior of other variables. It also means a better
understanding of the timing of lead–lag relations among many variables,
understanding the statistical significance of these lead–lag relationships,
and learning which variables are the more important ones to watch as
signals for further developments in other returns.
Obviously, if we know the true underlying model generating the data we
observe in markets, we will know how to obtain the best forecasts, even
though we observe the data with measurement error. More likely, how-
ever, the true underlying model may be too complex, or we are not sure
which model among many competing ones is the true one. So we have to
approximate the true underlying model by approximating models. Once
we acknowledge model uncertainty, and that our models are approxima-
tions, neural network approaches will emerge as a strong competitor to the
standard benchmark linear model.
Classification of different investment or lending opportunities as accept-
able or unacceptable risks is a familiar task in any financial or business
organization. Organizations would like to be able to discriminate good from
bad risks by identifying key characteristics of investment candidates. In a
lending environment, a bank would like to identify the likelihood of default
on a car loan by readily identifiable characteristics such as salary, years in
employment, years in residence, years of education, number of dependents,
and existing debt. Similarly, organizations may desire a finer grid for dis-
criminating, from very low, to medium, to very high unacceptable risk, to
manage exposure to different types of risk. Neural nets have proven to be
very effective classifiers — better than the state-of-the-art methods based
on classical statistical methods.1
Dimensionality reduction is also a very important component in financial
environments. All too often we summarize information about large amounts
of data with averages, means, medians, or trimmed means, in which a given
1Of course, classification has wider applications, especially in the health sciences. For
example, neural networks have proven very useful for detection of high or low risks of
various forms of cancer, based on information from blood samples and imaging.

1.1 Forecasting, Classification, and Dimensionality Reduction
3
percentage of high and low extreme values are eliminated from the sam-
ple. The Dow-Jones Industrial Average is simply that: an average price of
industrial share prices. Similarly the Standard and Poor 500 is simply the
average price of the largest 500 share prices. But averages can be mislead-
ing. For example, one student receiving a B grade in all her courses has a
B average. Another student may receive A grades in half of his courses and
a C grade in the rest. The second student also has a B average, but the
performances of the two students are very different. While the grades of
the first student cluster around a B grade, the grades of the second student
cluster around two grades: an A and a C. It is very important to know
if the average reported in the news truly represents where the market is
through dimensionality reduction if it is to convey meaningful information.
Forecasting into the future, or out-of-sample predictions, as well as clas-
sification and dimensionality reduction models, must go beyond diagnostic
examination of past data. We use the coefficients obtained from past data
to fit new data and make predictions, classification, and dimensionality
reduction decisions for the future. As the saying goes, life must be under-
stood looking backwards, but must be lived looking forward. The past
is certainly helpful for predicting the future, but we have to know which
approximating models to use, in combination with past data, to predict
future events. The medium-term strategy of any enterprise depends on the
outlook in the coming quarters for both price and quantity developments
in its own industry. The success of any strategy depends on how well the
forecasts guiding the decision makers work.
Diagnostic and forecasting methods feed back in very direct ways to
decision-making environments. Knowing what determines the past, as well
as what gives good predictions for the future, gives decision makers better
information for making optimal decisions over time. In engineering terms,
knowing the underlying “laws of motion” of key variables in a dynamic
environment leads to the development of optimal feedback rules. Applying
this concept to finance, if the Fed raises the short-term interest rate, how
should portfolio managers shift their assets? Knowing how the short-term
rates affect a variety of rates of return and how they will affect the future
inflation rate can lead to the formulation of a reaction function, in which
financial officers shift from risky assets to higher-yield, risk-free assets. We
call such a policy function, based on the “laws of motion” of the system,
control. Business organizations by their nature are interested in diagnostics
and prediction so that they may formulate policy functions for effective
control of their own future welfare.
Diagnostic examination of past data, forecasting, and control are differ-
ent activities but are closely related. The policy rule for control, of course,
need not be a hard and fast mechanical rule, but simply an operational
guide for better decision making. With good diagnostics and forecasting,
for example, businesses can better assess the effects of changes in their

4
1. Introduction
prices on demand, as well as the likely response of demand to external
shocks, and thus how to reset their prices. So it should not be so surprising
that good predictive methods are at a premium in research departments
for many industries.
Accurate forecasting methods are crucial for portfolio management by
commercial and investment banks. Assessing expected returns relative
to risk presumes that portfolio strategists understand the distribution of
returns. Until recently, most of the control or decision-making analysis has
been based on linear dynamic models with normal or log-normal distri-
butions of asset returns. However, finding such a distribution in volatile
environments means going beyond simple assumptions of normality or log
normality used in conventional models of portfolio strategies. Of course,
when we let go of normality, we must get our hands dirty in numeri-
cal approximation, and can no longer plug numbers into quick formulae
based on normal distributions. But there are clear returns from this extra
effort.
The message of this book is that business and financial decision makers
now have available the computational power and methods for more accu-
rate diagnostics, forecasting, and control in volatile, increasingly complex,
multidimensional environments. Researchers need no longer confine them-
selves to linear or log-linear models, or assume that underlying stochastic
processes are Gaussian or normal in order to obtain forecasts and pinpoint
risk–return trade-offs. In short, we can go beyond linearity and normality
in our assumptions with the use of neural networks.
1.2
Synergies
The activities of formal diagnostics and forecasting and practical decision
making or control in business and finance complement one another, even
though mastering each of them requires different types of skills and the
exercise or use of different but related algorithms. Applying diagnostic
and predictive methods requires knowledge of particular ways to filter or
preprocess data for optimum convergence, as well as for estimation, to
achieve good diagnostics and out-of-sample accuracy. Decision making in
finance, such as buying or selling or setting the pricing of different types of
instruments, requires the use of specific assumptions about how to classify
risk and about the preferences of investors regarding risk–return trade-offs.
Thus, the outcomes crucially depend on the choice of the preference or
welfare index about acceptable risk and returns over time.
From one perspective, the influence is unidirectional, proceeding from
diagnostic and forecasting methods to business and financial decision mak-
ing. Diagnostics and forecasting simply provide the inputs or stylized facts
about expected rates of return and their volatility. These forecasts are the

1.2 Synergies
5
crucial ingredients for pricing decisions, both for firm products and for
financial instruments such as call or put options and other more exotic
types of derivatives.
From another perspective, however, there may be feedback or bidirec-
tional influence. Knowledge of the objective functions of managers, or their
welfare indices, from survey expectations of managers, may be useful lead-
ing indicators in forecasting models, particularly in volatile environments.
Similarly, the estimated risk, or volatility, derived from forecasting models
and the implied risk, given by the pricing decisions of call or put options or
swaps in financial markets, may sharply diverge when there is a great deal of
uncertainty about the future course of the economy. In both of these cases,
the information calculated from survey expectations or from the implied
volatilities given by prices of financial derivatives may be used as additional
instruments for improving the performance of forecasting models for the
underlying rates of return. We may even be interested in predicting the
implied volatilities coming from options prices.
Similarly, deciding what price index to use for measuring and forecast-
ing inflation may depend on what the end user of this information intends
to do. If the purpose is to help the monetary authority monitor inflation-
ary pressures for setting policy, then price indices that have a great deal
of short-term volatility may not be appropriate. In this case, the overly
volatile measure of the price level may induce overreactions in the setting
of short-term interest rates. By the same token, a price measure that is too
smooth may lead to a very passive monetary policy that fails to dampen
rising inflationary pressures. Thus, it is useful to distill information from
a variety of price indices, or rates of return, to find the movement of the
market or the fundamental driving force. This can be done very effectively
with neural network approaches.
Unlike hard sciences such as physics or engineering, the measurement
and statistical procedures of diagnostics and forecasting are not so cleanly
separable from the objectives of the researchers, decision makers, and
players in the market. This is a subtle but important point that needs
to be emphasized. When we formulate approximating models for the rates
of return in financial markets, we are in effect attempting to forecast the
forecasts of others. Rates of return rise or fall in reaction to changes in
public or private news, because traders are reacting to news and buying
or selling assets. Approximating the true underlying model means taking
into account, as we formulate our models, how traders — human beings like
us — actually learn, process information, and make decisions.
Recent research in macroeconomics by Sargent (1997, 1999), to be dis-
cussed in greater detail in the following section, has drawn attention to
the fact that the decision makers we wish to approximate with our mod-
els are not fully rational, and thus “all-knowing,” about their financial
environment. Like us, they have to learn what is going on. For this very

6
1. Introduction
reason, neural network methods are a natural starting point for approx-
imation in financial markets. Neural networks grew out of the cognitive
and brain science disciplines for approximating how information is pro-
cessed and becomes insight. We illustrate this point in greater detail
when we examine the structure of typical neural network frameworks.
Suffice it to say, neural network analysis is becoming a key compo-
nent of the epistemology (philosophy of knowledge) implicit in empirical
finance.
1.3
The Interface Problems
The goal of this study is to “break open” the growing literature on neural
networks to make the methods accessible, user friendly, and operational for
the broader population of economists, analysts, and financial professionals
seeking to become more efficient in forecasting. A related goal is to focus
the attention of researchers in the fields of neural networks and related
disciplines, such as genetic algorithms, to areas in which their tools may
have particular advantages over state-of-the-art methods in economics and
finance, and thus may make significant contributions to unresolved issues
and controversies.
Much of the early development of neural network analysis has been
within the disciplines of psychology, neurosciences, and engineering, often
related to problems of pattern recognition. Genetic algorithms, which we
use for empirically implementing neural networks, have followed a similar
pattern of development within applied mathematics, with respect to opti-
mization of dynamic nonlinear and/or discrete systems, moving into the
data engineering field.
Thus there is an understandable interface problem for students and pro-
fessionals whose early formation in economics has been in classical statistics
and econometrics. Many of the terms are simply not familiar, or sound odd.
For example, a model is known as an architecture, and we train rather than
estimate a network architecture. A researcher makes use of a training set
and a test set of data, rather than using in-sample and out-of-sample data.
Coefficients are called weights and constant terms are biases.
Besides these semantic or vocabulary differences, however, many of the
applications in the neural network (and broader artificial intelligence) lit-
erature simply are not relevant for financial professionals, or if relevant, do
not resonate well with the matters at hand. For example, pattern recog-
nition is usually applied to problems of identifying letters of the alphabet
for computational translation in linguistics research. A much more inter-
esting example would be to examine recurring patterns such as “bubbles”
in high-frequency asset returns data, or the pattern observed in the term
structure of interest rates.

1.3 The Interface Problems
7
Similarly, many of the publications on financial markets by neural net-
work researchers have an ad hoc flavor and do not relate to the broader
theoretical infrastructure and fundamental behavioral assumptions used in
economics and finance. For this reason, unfortunately, much of this research
is not taken seriously by the broader academic community in economics and
finance.
The appeal of the neural network approach lies in its assumption of
bounded rationality: when we forecast in financial markets, we are forecast-
ing the forecasts of others, or approximating the expectations of others.
Financial market participants are thus engaged in a learning process,
continually adapting prior subjective beliefs from past mistakes.
What makes the neural network approach so appealing in this respect is
that it permits threshold responses by economic decision makers to changes
in policy or exogenous variables. For example, if the interest rate rises
from 3 percent to 3.1 or 3.2 percent, there may be little if any reaction by
investors. However, if the interest rate continues to increase, investors will
take notice, more and more. If the interest rate crosses a critical threshold,
for example, of 5 percent, there may be a massive reaction or “meltdown,”
with a sell-offof stocks and a rush into government securities.
The basic idea is that reactions of economic decision makers are not
linear and proportionate, but asymmetric and nonlinear, to changes in
external variables. Neural networks approximate this behavior of economic
and financial decision making in a very intuitive way.
In this important sense neural networks are different from classical
econometric models. In the neural network model, one is not making
any specific hypothesis about the values of the coefficients to be esti-
mated in the model, nor, for that matter, any hypothesis about the
functional form relating the observed regressor x to an observed out-
put y. Most of the time, we cannot even interpret the meaning of the
coefficients estimated in the network, at least in the same way we can
interpret estimated coefficients in ordinary econometric models, with a
well-defined functional form. In that sense, the neural network differs from
the usual econometrics, where considerable effort is made to obtain accu-
rate and consistent, if not unbiased, estimates of particular parameters or
coefficients.
Similarly, when nonlinear models are used, too often economists make use
of numerical algorithms based on assumptions of continuous or “smooth”
data. All too often, these methods break down, or one must make use of
repeated estimation, to make sure that the estimates do not represent one
of several possible sets of local optimum positions. The use of the genetic
algorithm and other evolutionary search algorithms enable researchers to
work with discontinuities and to locate with greater probability the global
optimum. This is the good news. The bad news is that we have to wait a
bit longer to get these results.


## What Are Neural Networks?

8
1. Introduction
The financial sectors of emerging markets, in particular, but also in
markets with a great deal of innovation and change, represent a fertile
ground for the use of these methods for two reasons, which are interrelated.
One is that the data are often very noisy, due either to the thinness of the
markets or to the speed with which news becomes dispersed, so that there
are obvious asymmetries and nonlinearities that cannot be assumed away.
Second, in many instances, the players in these markets are themselves in
a process of learning, by trial and error, about policy news or about legal
and other changes taking place in the organization of their markets. The
parameter estimates of a neural network, by which market participants
forecast and make decisions, are themselves the outcome of a learning and
search process.
1.4
Plan of the Book
The next chapter takes up the question: What is a neural network? It also
takes up the relevance of the “black box criticism” directed against neural
network and nonlinear estimation methods. The succeeding chapters ask
how we estimate such networks, and then how we evaluate and interpret
the results of network estimation.
Chapters 2 through 4 cover the basic theory of neural networks. These
chapters, by far, are the most technical chapters of the book. They
are oriented to people familiar with classical statistics and linear regres-
sion. The goal is to relate recent developments in the neural network
and related genetic search literature to the way econometricians routinely
do business, particularly with respect to the linear autoregressive model.
It is intended as a refresher course for those who wish to review their
econometrics. However, in succeeding chapters we flesh out with specific
data sets the more technical points developed here. The less technically
oriented reader may skim through these chapters at the first reading
and then return to them as a cross-reference periodically, to clarify def-
initions of alternative procedures reported with the examples of later
chapters.
These chapters contrast the setup of the neural network with the stan-
dard linear model. While we do not elaborate on the different methods for
estimating linear autoregressive models, since these topics are extensively
covered in many textbooks on econometrics, there is a detailed treatment
of the nonlinear estimation process for neural networks. We also lay out
the basics of genetic algorithms as well as with more familiar gradient or
quasi-Newtonian methods based on the calculation of first- and second-
order derivatives for estimating the neural network models. Evolutionary
computation involves coupling the global genetic search methods with local
gradient methods.

1.4 Plan of the Book
9
Chapters 3 and 4, on estimation and evaluation, also review the basic met-
rics or statistical tests we use to evaluate the success of a model, whether
the model is the standard linear one or a nonlinear neural network. We also
treat the ways we need to filter, adjust, or preprocess data prior to statisti-
cal estimation and evaluation. It should be clear from this chapter that the
straw man or benchmark of this book is the standard linear or linear autore-
gressive model. Throughout the chapters, the criteria for success of neural
network forecasting is measured relative to the standard linear model.
The fifth chapter presents several applications for evaluating the perfor-
mance of alternative networks with artificial data to illustrate the points
made in the previous three chapters. The reason for using artificial data
is that we can easily verify the accuracy of the network model, relative
to other approaches, if we know the true model generating the data.
This chapter shows, in one example, how artificial data generated with
the Black-Scholes option pricing model, as well as with more advanced
option pricing formulae, may be closely matched, out of sample, by a neu-
ral network. Thus, the neural network may be used to complement more
complicated options or derivative pricing models for setting the initial mar-
ket price of such instruments. This section shows very clearly the relative
accuracy or predictive power of the neural network or genetic algorithm.
Following an application to artificial data, we apply, in Chapter 6, neural
network methods to actual forecasting problems: at the industrial level, in
the quantity of automobiles as a function of the price index as well as aggre-
gate interest rates and disposable income; at the financial level, predicting
spreads in corporate bonds (relative to 10-year U.S. Treasury bonds) as a
function of default rates, the real exchange rate, industrial production, the
share-market index, and indices of market expectations. The seventh chap-
ter examines inflation and deflation forecasting at the macroeconomic level,
with sample data from Hong Kong and Japan. Chapter 8 takes up classifi-
cation problems, specifically credit card default and banking intervention,
as functions of observed characteristics, using both categorical and more
familiar continuous variables as the inputs. Chapter 9 shows the usefulness
of neural networks for distilling information from market volatilities, for
obtaining an overall sense of market volatility and with nonlinear princi-
pal components, and evaluates the performance of this method relative to
linear principal component analysis.
While time-series analysis, classification, and dimensionality reduction
are taken up as separate tasks, frequently they can be synergistic. For
example, dimensionality reduction can be used to reduce the number of
regressors in a model for forecasting. Similarly, the forecasts of a time-
series model, representing expectations of inflation or future growth, may
be inputs at any given time in a classification model. Time-series fore-
casting, classification, and dimensionality reduction are very useful for
understanding a wide variety of financial market issues.

10
1. Introduction
Each of the chapters concludes not only with a short summary, but also
with discussion questions, references to MATLAB programs available on
the website, and suggestions for further exercises. The programs are written
especially for this book. Certainly they are not meant to be examples of
efficient programming code. There is the ever-present trade-offbetween
transparency and efficiency in writing programming code. My first goal in
writing these programs was to make the programs “transparent” to myself!
Readers are invited to change, amend, and mutate these programs to make
them even more efficient and transparent for themselves. These MATLAB
programs require the optimization and statistics toolbox. We also make use
of the symbolic toolbox for a few exercises.
There is much more that could be part of this book. There is no dis-
cussion, in particular, of estimation and forecasting with intra-daily or
real-time data. This is a major focus of recent financial market research,
particularly the new micro-structure exchange-rate economics. One reason
for bypassing the use of real-time data is that it is usually proprietary.
While estimation results can be reported in scholarly research, the data
sets, without special arrangements, cannot be made available to other
researchers for replication and further study. In this study, we want to
encourage the readers to use both the data sets and MATLAB programs
of this book to enhance their own learning. For this reason, we stay with
familiar examples as the best way to illustrate the predictive power that
comes from harnessing neural networks with evolutionary computation.
Similarly, there is no discussion of forecasting stock-market returns or
the rates of change of other asset prices or exchange rates. While many
researchers have tried to show the profitable use of trading strategies based
on neural network out-of-sample forecasting relative to other strategies [Qi
(1999)], a greater payoffof neural networks in financial markets may come
from volatility forecasting.

Part I
Econometric Foundations
11


2
What Are Neural Networks?
2.1
Linear Regression Model
The rationale for the use of the neural network is forecasting or predicting
a given target or output variable y from information on a set of observed
input variables x. In time series, the set of input variables x may include
lagged variables, the current variables of x, and lagged values of y. In
forecasting, we usually start with the linear regression model, given by the
following equation:
yt =

βkxk,t + ϵt
(2.1a)
ϵt ∼N(0, σ2)
(2.1b)
where the variable ϵt is a random disturbance term, usually assumed to be
normally distributed with mean zero and constant variance σ2, and {βk}
represents the parameters to be estimated. The set of estimated parameters
is denoted {βk}, while the set of forecasts of y generated by the model with
the coefficient set {βk} is denoted by {yt}. The goal is to select {βk} to
minimize the sum of squared differences between the actual observations y
and the observations predicted by the linear model, y.
In time series, the input and output variables, [y x], have subscript
t, denoting the particular observation date, with the earliest observation

14
2. What Are Neural Networks?
starting at t = 1.1 In the standard econometrics courses, there are a vari-
ety of methods for estimating the parameter set {βk}, under a variety of
alternative assumptions about the distribution of the disturbance term, ϵt,
about the constancy of its variance, σ2, as well as about the independence
of the distribution of the input variables xk with respect to the disturbance
term, ϵt.
The goal of the estimation process is to find a set of parameters for the
regression model, given by {βk}, to minimize Ψ, defined as the sum of
squared differences, or residuals, between the observed or target or output
variable y and the model-generated variable y, over all the observations.
The estimation problem is posed in the following way:
Min
β
Ψ =
T

t=1
ϵ2
t =
T

t=1
(yt −yt)2
(2.2)
s.t. yt =

βkxk,t + ϵt
(2.3)
yt =
 βkxk,t
(2.4)
ϵt ∼N(0, σ2)
(2.5)
A commonly used linear model for forecasting is the autoregressive
model:
yt =
k∗

i=1
βiyt−i +
k

j=1
γjxj,t + ϵt
(2.6)
in which there are k independent x variables, with coefficient γj for each xj,
and k∗lags for the dependent variable y, with, of course k+k∗parameters,
{β} and {γ}, to estimate. Thus, the longer the lag structure, the larger the
number of parameters to estimate and the smaller the degrees of freedom
of the overall regression estimates.2
The number of output variables, of course, may be more than one. But
in the benchmark linear model, one may estimate and forecast each output
variable yj, j = 1, . . . , j∗with a series of J∗independent linear models. For
j∗output or dependent variables, we estimate (J∗· K) parameters.
1In cross-section analysis, the subscript for [y x] can be denoted by an identifier i,
which refers to the particular individuals, households, or other economic entities being
examined. In cross-section analysis, the ordering of the observations with respect to
particular observations does not matter.
2In the time-series model this model is known as the linear ARX model, since there
are autoregressive components, given by the lagged y variables, as well as exogenous x
variables.

2.2 GARCH Nonlinear Models
15
The linear model has the useful property of having a closed-form solution
for solving the estimation problem, which minimizes the sum of squared
differences between y and y. The solution method is known as linear regres-
sion. It has the advantage of being very quick. For short-run forecasting,
the linear model is a reasonable starting point, or benchmark, since in many
markets one observes only small symmetric changes in the variable to be
predicted around a long-term trend. However, this method may not be
especially accurate for volatile financial markets. There may be nonlinear
processes in the data. Slow upward movements in asset prices followed by
sudden collapses, known as bubbles, are rather common. Thus, the linear
model may fail to capture or forecast well sharp turning points in data. For
this reason, we turn to nonlinear forecasting techniques.
2.2
GARCH Nonlinear Models
Obviously, there are many types of nonlinear functional forms to use as an
alternative to the linear model. Many nonlinear models attempt to capture
the true or underlying nonlinear processes through parametric assump-
tions with specific nonlinear functional forms. One popular example of this
approach is the GARCH-In-Mean or GARCH-M model.3 In this approach,
the variance of the disturbance term directly affects the mean of the depen-
dent variable and evolves through time as a function of its own past value
and the past squared prediction error. For this reason, the time-varying
variance is called the conditional variance. The following equations describe
a typical parametric GARCH-M model:
σ2
t = δ0 + δ1σ2
t−1 + δ2ϵ2
t−1
(2.7)
ϵt ≈φ(0, σ2
t )
(2.8)
yt = α + βσt + ϵt
(2.9)
where y is the rate of return on an asset, α is the expected rate of appreci-
ation, and ϵt is the normally distributed disturbance term, with mean zero
and conditional variance σ2
t , given by φ(0, σ2
t ). The parameter β represents
the risk premium effect on the asset return, while the parameters δ0, δ1,
and δ2 define the evolution of the conditional variance. The risk premium
reflects the fact that investors require higher returns to take on higher risks
in a market. We thus expect β > 0.
3GARCH stands for generalized autoregresssive conditional heteroskedasticity, and
was introduced by Bollerslev (1986, 1987) and Engle (1982). Engle received the Nobel
Prize in 2003 for his work on this model.

16
2. What Are Neural Networks?
The GARCH-M model is a stochastic recursive system, given the initial
conditions σ2
0 and ϵ2
0, as well as the estimates for α, β, δ0, δ1, and δ2. Once
the conditional variance is given, the random shock is drawn from the
normal distribution, and the asset return is fully determined as a function
of its own mean, the random shock, and the risk premium effect, determined
by βσt.
Since the distribution of the shock is normal, we can use maximum
likelihood estimation to come up with estimates for α, β, δ0, δ1, and δ2.
The likelihood function L is the joint probability function for yt = yt, for
t = 1, . . . , T. For the GARCH-M models, the likelihood function has the
following form:
Lt =
T

t=1

1
2πσ2
t
exp

−(yt −yt)2
2σ2
t

(2.10)
yt = α + βσt
(2.11)
ϵt = yt −yt
(2.12)
σ2
t = δ0 + δ1σ2
t−1 + δ2ϵ2
t−1
(2.13)
where the symbols α, β, δ0, δ1, and δ2 are the estimates of the underlying
parameters, and Π is the multiplication operator, Π2
i=1 xi = x1 · x2. The
usual method for obtaining the parameter estimates maximizes the sum
of the logarithm of the likelihood function, or log-likelihood function, over
the entire sample T, from t = 1 to t = T, with respect to the choice of
coefficient estimates, subject to the restriction that the variance is greater
than zero, given the initial condition σ2
0 and ϵ2
t−1:4
Max
{α,β,δ0,δ1,δ2}
T

t=1
ln(Lt) =
T

t=1

−.5 ln(2π) −.5 ln(σt) −.5
(yt −yt)2
σ2
t

(2.14)
s.t.
:
σ2
t > 0, t = 1, 2, . . . , T
(2.15)
The appeal of the GARCH-M approach is that it pins down the source
of the nonlinearity in the process. The conditional variance is a nonlinear
transformation of past values, in the same way that the variance measure
4Taking the sum of the logarithm of the likelihood function produces the same
estimates as taking the product of the likelihood function, over the sample, from
t = 1, 2, . . . , T.

2.2 GARCH Nonlinear Models
17
is a nonlinear transformation of past prediction errors. The justification
of using conditional variance as a variable affecting the dependent vari-
able is that conditional variance represents a well-understood risk factor
that raises the required rate of return when we are forecasting asset price
dynamics.
One of the major drawbacks of the GARCH-M method is that mini-
mization of the log-likelihood functions is often very difficult to achieve.
Specifically, if we are interested in evaluating the statistical significance
of the coefficient estimates, α, β, δ0, δ1, and δ2, we may find it difficult to
obtain estimates of the confidence intervals. All of these difficulties are
common to maximum likelihood approaches to parameter estimation.
The parametric GARCH-M approach to the specification of nonlinear
processes is thus restrictive: we have a specific set of parameters we want
to estimate, which have a well-defined meaning, interpretation, and ratio-
nale. We even know how to estimate the parameters, even if there is some
difficulty. The good news of GARCH-M models is that they capture a well-
observed phenomenon in financial time series, that periods of high volatility
are followed by high volatility and periods of low volatility are followed by
similar periods.
However, the restrictiveness of the GARCH-M approach is also its draw-
back: we are limited to a well-defined set of parameters, a well-defined
distribution, a specific nonlinear functional form, and an estimation method
that does not always converge to parameter estimates that make sense.
With specific nonlinear models, we thus lack the flexibility to capture
alternative nonlinear processes.
2.2.1
Polynomial Approximation
With neural network and other approximation methods, we approximate
an unknown nonlinear process with less-restrictive semi-parametric mod-
els. With a polynomial or neural network model, the functional forms are
given, but the degree of the polynomial or the number of neurons are
not. Thus, the parameters are neither limited in number, nor do they
have a straightforward interpretation, as the parameters do in linear or
GARCH-M models. For this reason, we refer to these models as semi-
parametric. While GARCH and GARCH-M models are popular models for
nonlinear financial econometrics, we show in Chapter 3 how well a rather
simple neural network approximates a time series that is generated by a
calibrated GARCH-M model.
The most commonly used approximation method is the polynomial
expansion. From the Weierstrass Theorem, a polynomial expansion around
a set of inputs x with a progressively larger power P is capable of approxi-
mating to a given degree of precision any unknown but continuous function

18
2. What Are Neural Networks?
y = g(x).5 Consider, for example, a second-degree polynomial approxima-
tion of three variables, [x1t, x2t, x3t], where g is unknown but assumed to be
a continuous function of arguments x1, x2, x3. The approximation formula
becomes:
yt = β0 + β1x1t + β2x2t + β3x3t + β4x2
1t + β5x2
2t + β6x2
3t + β7x1tx2t
+ β8x2tx3t + β9x1tx3t
(2.16)
Note that the second-degree polynomial approximation with three argu-
ments or dimensions has three cross-terms, with coefficients given by
{β7, β8, β9}, and requires ten parameters. For a model of several arguments,
the number of parameters rises exponentially with the degree of the polyno-
mial expansion. This phenomenon is known as the curse of dimensionality
in nonlinear approximation. The price we have to pay for an increasing
degree of accuracy is an increasing number of parameters to estimate, and
thus a decreasing number of degrees of freedom for the underlying statistical
estimates.
2.2.2
Orthogonal Polynomials
Judd (1999) discusses a wider class of polynomial approximators, called
orthogonal polynomials. Unlike the typical polynomial based on raising the
variable x to powers of higher order, these classes of polynomials are based
on sine, cosine, or alternative exponential transformations of the variable
x. They have proven to be more efficient approximators than the power
polynomial.
Before making use of these orthogonal polynomials, we must transform
all of the variables [y, x] into the interval [−1, 1]. For any variable x, the
transformation to a variable x∗is given by the following formula:
x∗=
2x
max(x) −min(x) −min(x) + max(x)
max(x) −min(x)
(2.17)
The exact formulae for these orthogonal polynomials are complicated [see
Judd (1998), p. 204, Table 6.3]. However, these polynomial approximators
can be represented rather easily in a recursive manner. The Tchebeycheff
5See Miller, Sutton, and Werbos (1990), p. 118.

2.2 GARCH Nonlinear Models
19
polynomial expansion T(x∗) for a variable x∗is given by the following
recursive system:6
T0(x∗) = 1
T1(x∗) = x∗
Ti+1(x∗) = 2x∗Ti(x∗) −Ti−1(x∗)
(2.18)
The Hermite expansion H(x∗) is given by the following recursive equations:
H0(x∗) = 1
H1(x∗) = 2x∗
Hi+1(x∗) = 2x∗Hi(x∗) −2iHi−1(x∗)
(2.19)
The Legendre expansion L(x∗) has the following form:
L0(x∗) = 1
L1(x∗) = 1 −x∗
Li+1(x∗) =
2i + 1
i + 1

Li(x∗) −
i
i + 1Li−1(x∗)
(2.20)
Finally, the Laguerre expansion LG(x∗) is represented as follows:
LG0(x∗) = 1
LG1(x∗) = 1 −x∗
LGi(x∗) =
2i + 1 −x∗
i + 1

LGi(x∗) −
i
i + 1LGi−1(x∗)
(2.21)
Once these polynomial expansions are obtained for a given variable x∗,
we simply approximate y∗with a linear regression. For two variables,
[x1, x2] with expansion P1 and P2 respectively, the approximation is given
by the following expression:
y∗
t =
P 1

i=1
P 2

j=1
βijTi(x∗
1t)Tj(x2t)
(2.22)
6There is a long-standing controversy about the proper spelling of the first polyno-
mial. Judd refers to the Tchebeycheffpolynomial, whereas Heer and Maussner (2004)
write about the Chebeyshev polynomal.

20
2. What Are Neural Networks?
To retransform a variable y∗back into the interval [min(y), max(y)], we
use the following expression:
y = (y∗+ 1)[max(y) −min(y)]
2
+ min(y)
The network is an alternative to the parametric linear, GARCH-M
models, and semi-parametric polynomial approaches for approximating a
nonlinear system. The reason we turn to the neural network is simple and
straightforward. The goal is to find an approach or method that forecasts
well data generated by often unknown and highly nonlinear processes, with
as few parameters as possible, and which is easier to estimate than para-
metric nonlinear models. Succeeding chapters show that the neural network
approach does this better — in terms of accuracy and parsimony — than the
linear approach. The network is as accurate as the polynomial approxima-
tions with fewer parameters, or more accurate with the same number of
parameters. It is also much less restrictive than the GARCH-M models.
2.3
Model Typology
To locate the neural network model among different types of models, we can
differentiate between parametric and semi-parametric models, and models
that have and do not have closed-form solutions. The typology appears in
Table 2.1.
Both linear and polynomial models have closed-form solutions for esti-
mation of the regression coefficients. For example, in the linear model
y = xβ, written in matrix form, the typical ordinary least squares (OLS)
estimator is given by β = (x′x)−1x′y. The coefficient vector β is a simple
linear function of the variables [y x]. There is no problem of convergence
or multiple solutions: once we know the variable set [y x], we know the
estimator of the coefficient vector, β. For a polynomial model, in which
the dependent variable y is a function of higher powers of the regressors
x, the coefficient vector is calculated in the same way as OLS. We sim-
ply redefine the regressors in terms of a matrix z, representing polynomial
TABLE 2.1. Model Typology
Closed-Form Solution
Parametric
Semi-Parametric
Yes
Linear
Polynomial
No
GARCH-M
Neural Network

2.4 What Is A Neural Network?
21
expansions of the regressors x, and calculate the polynomial coefficient
vector as β = (z′z)−1z′y.
Both the GARCH-M and the neural network models are examples of
models that do not have closed-form solutions for the coefficient vector
of the respective model. We discuss many of the methods for obtaining
solutions for the coefficient vector for these models in the following sections.
What is clear from Table 2.1, moreover, is that we have a clear-cut choice
between linear and neural network models. The linear model may be a very
imprecise approximation to the real world, but it gives very easy, quick,
exact solutions. The neural network may be a more precise approximation,
capturing nonlinear behavior, but it does not have exact, easy-to-obtain
solutions. Without a closed-form solution, we have to use approximate
solutions. In fact, as Michalewicz and Fogel (2002) point out, this polarity
reflects the difficulties in problem solving in general. It is difficult to obtain
good solutions to important problems, either because we have to use an
imprecise model approximation (such as a linear model) which has an exact
solution, or we have to use an approximate solution for a more precise,
complex model approximation [Michalewicz and Fogel (2002), p. 19].
2.4
What Is A Neural Network?
Like the linear and polynomial approximation methods, a neural network
relates a set of input variables {xi}, i = 1, . . . , k, to a set of one or more
output variables, {yj}, j = 1, . . . , k ∗. The difference between a neural
network and the other approximation methods is that the neural network
makes use of one or more hidden layers, in which the input variables are
squashed or transformed by a special function, known as a logistic or logsig-
moid transformation. While this hidden layer approach may seem esoteric,
it represents a very efficient way to model nonlinear statistical processes.
2.4.1
Feedforward Networks
Figure 2.1 illustrates the architecture on a neural network with one hidden
layer containing two neurons, three input variables {xi.}, i = 1, 2, 3, and
one output y.
We see parallel processing. In addition to the sequential processing of typ-
ical linear systems, in which only observed inputs are used to predict an
observed output by weighting the input neurons, the two neurons in the hid-
den layer process the inputs in a parallel fashion to improve the predictions.
The connectors between the input variables, often called input neurons,
and the neurons in the hidden layer, as well as the connectors between
the hidden-layer neurons and the output variable, or output neuron, are

22
2. What Are Neural Networks?
x1
x2
x3
n1
n2
y
Inputs - x
Hidden Layer
 neurons - n
Output - y
FIGURE 2.1. Feedforward neural network
called synapses.7 Most problems we work with, fortunately, do not involve
a large number of neurons engaging in parallel processing, thus the parallel
processing advantage, which applies to the way the brain works with its
massive number of neurons, is not a major issue.
This single-layer feedforward or multiperceptron network with one hid-
den layer is the most basic and commonly used neural network in economic
and financial applications. More generally, the network represents the way
the human brain processes input sensory data, received as input neurons,
into recognition as an output neuron. As the brain develops, more and
more neurons are interconnected by more synapses, and the signals of the
different neurons, working in parallel fashion, in more and more hidden
layers, are combined by the synapses to produce more nuanced insight and
reaction.
Of course, very simple input sensory data, such as the experience of
heat or cold, need not lead to processing by very many neurons in multiple
hidden layers to produce the recognition or insight that it is time to turn
up the heat or turn on the air conditioner. But as experiences of input
sensory data become more complex or diverse, more hidden neurons are
activated, and insight as well as decision is a result of proper weighting or
combining signals from many neurons, perhaps in many hidden layers.
A commonly used application of this type of network is in pattern recog-
nition in neural linguistics, in which handwritten letters of the alphabet are
decoded or interpreted by networks for machine translation. However, in
7The linear model, of course, is a special case of the feedforward network. In this
case, the one neuron in the hidden layer is a linear activation function which connects
to the one output layer with a weight on unity.

2.4 What Is A Neural Network?
23
economic and financial applications, the combining of the input variables
into various neurons in the hidden layer has another interpretation. Quite
often we refer to latent variables, such as expectations, as important driv-
ing forces in markets and the economy as a whole. Keynes referred quite
often to “animal spirits” of investors in times of boom and bust, and we
often refer to bullish (optimistic) or bearish (pessimistic) markets. While it
is often possible to obtain survey data of expectations at regular frequen-
cies, such survey data come with a time delay. There is also the problem
that how respondents reply in surveys may not always reflect their true
expectations.
In this context, the meaning of the hidden layer of different inter-
connected processing of sensory or observed input data is simple and
straightforward. Current and lagged values of interest rates, exchange rates,
changes in GDP, and other types of economic and financial news affect fur-
ther developments in the economy by the way they affect the underlying
subjective expectations of participants in economic and financial markets.
These subjective expectations are formed by human beings, using their
brains, which store memories coming from experiences, education, culture,
and other models. All of these interconnected neurons generate expecta-
tions or forecasts which lead to reactions and decisions in markets, in which
people raise or lower prices, buy or sell, and act bullishly or bearishly.
Basically, actions come from forecasts based on the parallel processing of
interconnected neurons.
The use of the neural network to model the process of decision mak-
ing is based on the principle of functional segregation, which Rustichini,
Dickhaut, Ghirardato, Smith, and Pardo (2002) define as stating that “not
all functions of the brain are performed by the brain as a whole” [Rustichini
et al. (2002), p. 3]. A second principle, called the principle of functional
integration, states that “different networks of regions (of the brain) are acti-
vated for different functions, with overlaps over the regions used in different
networks” [Rustichini et al. (2002), p. 3].
Making use of experimental data and brain imaging,
Rustichini,
Dickhaut, Ghirardato, Smith, and Pardo (2002) offer evidence that sub-
jects make decisions based on approximations, particularly when subjects
act with a short response time. They argue for the existence of a “special-
ization for processing approximate numerical quantities” [Rustichini et al.
(2002), p. 16].
In a more general statistical framework, neural network approximation
is a sieve estimator. In the univariate case, with one input x, an approx-
imating function of order m, Ψm, is based on a non-nested sequence of
approximating spaces:
Ψm = [ψm,0(x), ψm,1(x), . . . ψm,m(x)]
(2.23)

24
2. What Are Neural Networks?
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
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
FIGURE 2.2. Logsigmoid function
Beresteanu (2003) points out that each finite expansion, ψm,0(x), ψm,1(x),
. . . ψm,m(x), can potentially be based on a different set of functions
[Beresteanu (2003), p. 9]. We now discuss the most commonly used
functional forms in the neural network literature.
2.4.2
Squasher Functions
The neurons process the input data in two ways: first by forming lin-
ear combinations of the input data and then by “squashing” these linear
combinations through the logsigmoid function. Figure 2.2 illustrates the
operation of the typical logistic or logsigmoid activation function, also
known as a squasher function, on a series ranging from −5 to +5. The
inputs are thus transformed by the squashers before transmitting their
effects on the output.
The appeal of the logsigmoid transform function comes from its threshold
behavior, which characterizes many types of economic responses to changes
in fundamental variables. For example, if interest rates are already very low
or very high, small changes in this rate will have very little effect on the deci-
sion to purchase an automobile or other consumer durable. However, within
critical ranges between these two extremes, small changes may signal signif-
icant upward or downward movements and therefore create a pronounced
impact on automobile demand.
Furthermore, the shape of the logsigmoid function reflects a form of
learning behavior. Often used to characterize learning by doing, the func-
tion becomes increasingly steep until some inflection point. Thereafter the
function becomes increasingly flat and its slope moves exponentially to zero.

2.4 What Is A Neural Network?
25
Following the same example, as interest rates begin to increase from low
levels, consumers will judge the probability of a sharp uptick or downtick
in the interest rate based on the currently advertised financing packages.
The more experience they have, up to some level, the more apt they are to
interpret this signal as the time to take advantage of the current interest
rate, or the time to postpone a purchase. The results are markedly dif-
ferent from those experienced at other points on the temporal history of
interest rates. Thus, the nonlinear logsigmoid function captures a thresh-
old response characterizing bounded rationality or a learning process in the
formation of expectations.
Kuan and White (1994) describe this threshold feature as the fundamen-
tal characteristic of nonlinear response in the neural network paradigm.
They describe it as the “tendency of certain types of neurons to be qui-
escent of modest levels of input activity, and to become active only after
the input activity passes a certain threshold, while beyond this, increases
in input activity have little further effect” [Kuan and White (1994), p. 2].
The following equations describe this network:
nk,t = ωk,0 +
i∗

i=1
ωk,ixi,t
(2.24)
Nk,t = L(nk,t)
(2.25)
=
1
1 + e−nk,t
(2.26)
yt = γ0 +
k∗

k=1
γkNk,t
(2.27)
where L(nk,t) represents the logsigmoid activation function with the form
1
1+e−nk,t . In this system there are i∗input variables {x}, and k∗neu-
rons. A linear combination of these input variables observed at time t,
{xi,t}, i = 1, . . . , i∗, with the coefficient vector or set of input weights ωk,i,
i = 1, . . . , i∗, as well as the constant term, ωk,0, form the variable nk,t.
This variable is squashed by the logistic function, and becomes a neuron
Nk,t at time or observation t. The set of k∗neurons at time or observa-
tion index t are combined in a linear way with the coefficient vector {γk},
k = 1, . . . , k∗, and taken with a constant term γ0, to form the forecast yt
at time t. The feedforward network coupled with the logsigmoid activation
functions is also known as the multi-layer perception or MLP network. It is
the basic workhorse of the neural network forecasting approach, in the sense
that researchers usually start with this network as the first representative
network alternative to the linear forecasting model.

26
2. What Are Neural Networks?
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
−1
−0.8
−0.6
−0.4
−0.2
0
0.2
0.4
0.6
0.8
1
FIGURE 2.3. Tansig function
An alternative activation function for the neurons in a neural network is
the hyperbolic tangent function. It is also known as the tansig or tanh func-
tion. It squashes the linear combinations of the inputs within the interval
[−1, 1], rather than [0, 1] in the logsigmoid function. Figure 2.3 shows the
behavior of this alternative function.
The mathematical representation of the feedforward network with the
tansig activation function is given by the following system:
nk,t = ωk,0 +
i∗

i=1
ωk,ixi,t
(2.28)
Nk,t = T(nk,t)
(2.29)
= enk,t −e−nk,t
enk,t + e−nk,t
(2.30)
yt = γ0 +
k∗

k=1
γkNk,t
(2.31)
where T(nk,t) is the tansig activation function for the input neuron nk,t.
Another commonly used activation function for the network is the famil-
iar cumulative Gaussian function, commonly known to statisticians as the

2.4 What Is A Neural Network?
27
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
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Cumulative
Gaussian
Function 
Logsigmoid
Function 
FIGURE 2.4. Gaussian function
normal function. Figure 2.4 pictures this function as well as the logsigmoid
function.
The Gaussian function does not have as wide a distribution as the logsig-
moid function, in that it shows little or no response when the inputs
take extreme values (below −2 or above +2 in this case), whereas the
logsigmod does show some response. Moreover, within critical changes,
such as [−2, 0] and [0, 2], the slope of the cumulative Gaussian func-
tion is much steeper. The mathematical representation of the feedforward
network with the Gaussian activation functions is given by the following
system:
nk,t = ωk,0 +
i∗

i=1
ωk,ixi,t
(2.32)
Nk,t = Φ(nk,t)
(2.33)
=
	 nk,t
−∞

1
2π e−.5n2
k,t
(2.34)

28
2. What Are Neural Networks?
yt = γ0 +
k∗

k=1
γkNk,t
(2.35)
where Φ(nk,t) is the standard cumulative Gaussian function.8
2.4.3
Radial Basis Functions
The radial basis network function (RBF) network makes use of the radial
basis or Gaussian density function as the activation function, but the struc-
ture of the network is different from the feedforward or MLP networks we
have discussed so far. The input neuron may be a linear combination of
regressors, as in the other networks, but there is only one input signal, only
one set of coefficients of the input variables x. The signal from this input
layer is the same to all the neurons, which in turn are Gaussian transfor-
mations, around k∗different means, of the input signals. Thus the input
signals have different centers for the radial bases or normal distributions.
The differing Gaussian transformations are combined in a linear fashion for
forecasting the output.
The following system describes a radial basis network:
Min
<ω,µ,γ>
T

t=0
(yt −yt)2
(2.36)
nt = ω0 +
i∗

i=1
ωixi,t
(2.37)
Rk,t = φ(nt; µk)
(2.38)
=
1
2πσn−µk
exp
−[nt −µk]
σn−µk
2
(2.39)
yt = γ0 +
k∗

k=1
γkNk,t
(2.40)
where x again represents the set of input variables and n represents the
linear transformation of the input variables, based on weights ω. We choose
k∗different centers for the radial basis transformation, µk, k = 1, . . . , k∗,
calculate the k∗standard error implied by the different centers, µk, and
8The Gaussian function, used as an activation function in a multilayer perceptron
or feedforward network, is not a radial basis function network. We discuss that func-
tion next.

2.4 What Is A Neural Network?
29
obtain the k∗different radial basis functions, Rk. These functions in turn
are combined linearly to forecast y with weights γ (which include a constant
term). Optimizing the radial basis network involves choosing the coefficient
sets {ω} and {γ} as well as the k∗centers of radial basis functions {µ}.
Haykin (1994) points out a number of important differences between
the RBF and the typical multilayer perceptron network; we note two.
First, the RBF network has at most one hidden layer, whereas an MLP
network may have many (though in practice we usually stay with one hid-
den layer). Second, the activation function of the RBF network computes
the Euclidean norm or distance (based on the Gaussian transformation)
between the signal from the input vector and the center of that unit,
whereas the MLP or feedforward network computes the inner products
of the inputs and the weights for that unit.
Mandic and Chambers (2001) point out that both the feedforward
or multilayer perceptron networks and radial basis networks have good
approximation properties, but they note that “an MLP network can always
simulate a Gaussian RBF network, whereas the converse is true only for
certain values of the bias parameter” [Mandic and Chambers (2001), p. 60].
2.4.4
Ridgelet Networks
Chen, Racine, and Swanson (2001) have shown the ridgelet function to be
a useful and less-restrictive alternative to the Gaussian activation functions
used in the “radial basis” type sieve network. Such a function, denoted by
R(·), can be chosen for a suitable value of m as ∇m−1φ, where ∇represents
the gradient operator and φ is the standard Gaussian density function.
Setting m = 6, the ridgelet function is defined in the following way:
R(x) = ∇m−1φ
m = 6 =⇒R(x) =

−15x + 10x3 −x5
exp

−.5x2
The curvature of this function, for the same range of input values,
appears in Figure 2.5.
The ridgelet function, like the Gaussian density function, has very low
values for the extreme values of the input variable. However, there is more
variation in the derivative values in the ranges [−3, −1], and [1, 3] than
in a pure Gaussian density function. The mathematical representation of
the ridgelet sieve network is given by the following system, with i∗input
variables and k∗ridgelet sieves:
y∗
t =
i∗

i=1
ωixi,t
(2.41)

30
2. What Are Neural Networks?
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
−6
−4
−2
0
2
4
6
FIGURE 2.5. Ridgelet function
nk,t = α−1
k
(βk · y∗
t −β0,k)
(2.42)
Nk,t = R(nk,t)
(2.43)
yt = γ0 +
k∗

k=1
γk
√αk
Nk,t
(2.44)
where αk represents the scale while β0,k and βk stand for the location and
direction of the network, with |βl| = 1.
2.4.5
Jump Connections
One alternative to the pure feedforward network or sieve network is a
feedforward network with jump connections, in which the inputs x have
direct linear links to output y, as well as to the output through the hid-
den layer of squashed functions. Figure 2.6 pictures a feedforward jump

2.4 What Is A Neural Network?
31
x1
x2
x3
n1
n2
y
Inputs
Hidden Layer
Output
FIGURE 2.6. Feedforward neural network with jump connections
connection network with three inputs, one hidden layer, and two neurons
(i∗= 3, k∗= 2):
The mathematical representation of the feedforward network pictured in
Figure 2.1, for logsigmoid activation functions, is given by the following
system:
nk,t = ωk,0 +
i∗

i=1
ωk,ixi,t
(2.45)
Nk,t =
1
1 + e−nk,t
(2.46)
ˆyt = γ0 +
k∗

k=1
γkNk,t +
i∗

i=1
βixi,t
(2.47)
Note that the feedforward network with the jump connections increases
the number of parameters in the network by j∗, the number of inputs. An
appealing advantage of the feedforward network with jump connections
is that it nests the pure linear model as well as the feedforward neural
network. It allows the possibility that a nonlinear function may have a linear
component as well as a nonlinear component. If the underlying relationship
between the inputs and the output is a pure linear one, then only the direct
jump connectors, given by the coefficient set {βi}, i = 1, . . . , i∗, should
be significant. However, if the true relationship is a complex nonlinear
one, then one would expect the coefficient sets {ω} and {γ} to be highly
significant, and the coefficient set {β} to be relatively insignificant. Finally,
the relationship between the input variables {x} and the output variable

32
2. What Are Neural Networks?
{y} can be decomposed into linear and nonlinear components, and then
we would expect all three sets of coefficients, {β}, {ω}, and {γ}, to be
significant.
A practical use of the jump connection network is as a useful test for
neglected nonlinearities in a relationship between the input variables x
and the output variable y. We take up this issue in the discussion of the
Lee-White-Granger test. In this vein, we can also estimate a partitioned
network. We first do linear least squares regression of the dependent vari-
able y on the regressors, x, and obtain the residuals, e. We then set up
a feedforward network in which the residuals from the linear regression
become the dependent variable, while we use the same regressors as the
input variables for the network. If there are indeed neglected nonlinearities
in the linear regression, then the second-stage, partitioned network should
have significant explanatory power.
Of course, the jump connection network and the partitioned linear and
feedforward network should give equivalent results, at least in theory.
However, as we discuss in the next section, due to problems of conver-
gence to local rather than global optima, we may find that the results may
be different, especially for networks with a large number of regressors and
neurons in one or more hidden layers.
2.4.6
Multilayered Feedforward Networks
Increasing complexity may be approximated by making use of two or more
hidden layers in a network architecture. Figure 2.7 pictures a feedforward
network with two hidden layers, each having two neurons.
The representation of the network appearing in Figure 2.6 is given by
the following system, with i∗input variables, k∗neurons in the first hidden
x1
x2
x3
p1
p2
Inputs - x
Hidden Layer - 1
neurons - n1,n2
n1
y
Hidden Layer - 2
neurons - p1,p2
n2
Output
FIGURE 2.7. Feedforward network with two hidden layers

2.4 What Is A Neural Network?
33
layer, and l∗neurons in the second hidden layer:
nk,t = ωk,0 +
i∗

i=1
ωk,ixi,t
(2.48)
Nk,t =
1
1 + e−nk,t
(2.49)
pl,t = ρl,0 +
k∗

k=1
ρl,kNk,t
(2.50)
Pl,t =
1
1 + e−pl,t
(2.51)
yt = γ0 +
l∗

l=1
γlPl,t
(2.52)
It should be clear that adding a second hidden layer increases the number
of parameters to be estimated by the factor (k∗+ 1)(l∗−1) + (l∗+ 1),
since the feedforward network with one hidden layer, with i∗inputs and
k∗neurons, has (i∗+ 1)k∗+ (k∗+ 1) parameters, while a similar network
with two hidden layers, with l∗neurons in the second hidden layer, has
(i∗+ 1)k∗+ (k∗+ 1)l∗+ (l∗+ 1) hidden layers.
Feedforward networks with multiple hidden layers add complexity. They
do so at the cost of more parameters to estimate, which use up valuable
degrees of freedom if the sample size is limited, and at the cost of greater
training time. With more parameters, there is also the likelihood that the
parameter estimates may converge to a local, rather than global, optimum
(we discuss this problem in greater detail in the next chapter). There has
been a wide discussion about the usefulness of networks with more than
one hidden layer. Dayhoffand DeLeo (2001), referring to earlier work by
Hornik, Stinchcomb, and White (1989), make the following point on this
issue:
A general function approximation theorem has been proven for three-layer
neural networks. This result shows that artificial neural networks with two layers
of trainable weights are capable of approximating any nonlinear function. This is
a powerful computational property that is robust and has ramifications for many
different applications of neural networks. Neural networks can approximate a
multifactorial function in such a way that creating the functional form and
fitting the function are performed at the same time, unlike nonlinear regression
in which a fit is forced to a prechosen function. This capability gives neural
networks a decided advantage over traditional statistical multivariate regression
techniques.
[Dayhoffand DeLeo (2001), p. 1624].

34
2. What Are Neural Networks?
In most situations, we can work with multilayer perceptron or jump-
connection neural networks with one hidden layer and two or three neurons.
We illustrate the advantage of a very simple neural network against a set
of orthogonal polynomials in the next chapter.
2.4.7
Recurrent Networks
Another commonly used neural architecture is the Elman recurrent net-
work. This network allows the neurons to depend not only on the input
variables x, but also on their own lagged values. Thus the Elman network
builds “memory” in the evolution of the neurons. This type of network is
similar to the commonly used moving average (MA) process in time-series
analysis. In the MA process, the dependent variable y is a function of
observed inputs x as well as current and lagged values of an unobserved
disturbance term or random shock, ϵ. Thus, a q-th order MA process has
the following form:
yt = β0 +
i∗

i=1
βixi,t + ϵt +
q

j=1
νjϵt−j
(2.53)
ϵt−j = yt−j −yt−j
(2.54)
The q-dimensional coefficient set {νj}, j = 1, . . . , q, is estimated recur-
sively. Estimation starts with ordinary least squares, eliminating the set of
lagged disturbance terms, {ϵt−j}, j = 1, . . . , q. Then we take the set of resid-
uals for the initial regression, {ϵ}, as proxies for lagged {ϵt−j}, j = 1, . . . , q,
and estimate the parameters {βi}, i = 0, . . . , i∗, as well as the set of coeffi-
cients of the lagged disturbances, {νj}, j = 1, . . . , q. The process continues
over several steps until convergence is achieved and when further iterations
produce little or no change in the estimated coefficients.
In a similar fashion, the Elman network makes use of lagged as well as
current values of unobserved unsquashed neurons in the hidden layer. One
such Elman recurrent network appears in Figure 2.8, with three inputs,
two neurons in one hidden layer, and one output. In the estimation of
both Elman networks and MA processes, it is necessary to use a multi-
step estimation procedure. We start with initializing the vector of lagged
neurons with lagged neuron proxies from a simple feedforward network.
Then we estimate their coefficients and recalculate the vector of lagged
neurons. Parameter values are re-estimated in a recursive fashion. The
process continues until convergence takes place.
Note that the inputs, neurons, and output boxes have time labels for the
current period, t, or the lagged period, t −1. The Elman network is thus
a network specific to data that have a time dimension. The feedforward

2.4 What Is A Neural Network?
35
x1
x3
x2
n2(t-1)
n1(t-1)
N2(t)
N1(t)
Y(t)
FIGURE 2.8. Elman recurrent network
network, on the other hand, may be used for cross-section data, which are
not dimensioned by time, as well as time-series data.
The following system represents the recurrent Elman network illustrated
in Figure 2.8:
nk,t = ωk,0+ = ωk,0 +
i∗

i=1
ωk,ixi,t +
k∗

k=1
φknk,t−1
(2.55)
Nk,t =
1
1 + e−ni,t
(2.56)
yt = γ0 +
k∗

k=1
γkNk,t
Note that the recurrent Elman network is one in which the lagged hidden-
layer neurons feed back into the current hidden layer of neurons. However,
the lagged neurons do so before the logsigmoid activation function is applied
to them — they enter as lags in their unsquashed state. The recurrent
network thus has an indirect feedback effect from the lagged unsquashed
neurons to the current neurons, not a direct feedback from lagged neu-
rons to the level of output. The moving-average time-series model, on the
other hand, has a direct feedback effect, from lagged disturbance terms to
the level of output yt. Despite the recursive estimation process for obtain-
ing proxies of nonobserved data, the recurrent network differs in this one
important respect from the moving-average time-series model.

36
2. What Are Neural Networks?
The Elman network is a way of capturing memory in financial markets,
particularly for forecasting high-frequency data such as daily, intra-daily,
or even real-time returns in foreign exchange or share markets. While the
use of lags certainly is one way to capture memory, memory may also show
up in the way the nonlinear structure changes through time. The use of
the Elman network, in which the lagged neurons feed back into the current
neurons, is a very handy way to model this type of memory structure, in
which the hidden layer itself changes through time, due to feedback from
past neurons.
The Elman network is an explicit dynamic network. The feedforward
network is usually regarded as a static network, in which a given set of input
variables at time t are used to forecast a target output variable at time t. Of
course, the input variables used in the feedforward network may be lagged
values of the output variable, so that the feedforward network becomes
dynamic by redefinition of the input variables. The Elman network, by
contrast, allows another dynamic structure beyond incorporating lagged
dependent or output variables, yt−1, . . . , yt−k, as current input variables.
Moreover, as Mandic and Chambers (2001) point out, restricting memory
or dynamic structure in the feedforward network only to the input structure
may lead to an unnecessarily large number of parameters. While recurrent
networks may be functionally equivalent to feedforward networks with only
lagged input variables, they generally have far fewer parameters, which, of
course, speeds up the estimation or training process.
2.4.8
Networks with Multiple Outputs
Of course, a feedforward network (or Elman network) can have multiple
outputs. Figure 2.9 shows one such feedforward network architecture, with
three inputs, two neurons, and two outputs. The representation of the
feedforward network architecture is given by the following system:
nk,t = ωk,0 +
i∗

i=1
ωk,ixi,t
(2.57)
Nk,t =
1
1 + e−nk,t
(2.58)
y1,t = γ1,0 +
k∗

k=1
γ1,kNk,t
(2.59)
y2,t = γ2,0 +
k∗

k=1
γ2,kNk,t
(2.60)

2.4 What Is A Neural Network?
37
x1
x2
x3
n1
n2
y2
Inputs - x
Hidden Layer
neurons - n
Output - y1, y2
y1
FIGURE 2.9. Feedforward network multiple outputs
We see in this system that the addition of one additional output in
the feedforward network requires additional (k∗+ 1) parameters, equal to
the number of neurons on the hidden layer plus an additional constant
term. Thus, adding more output variables to be predicted by the network
requires additional parameters which depend on the number of neurons in
the hidden layer, not on the number of input variables.
By contrast, a linear model depending on k regressors or arguments
plus a constant would require additional k + 1 parameters — essentially a
new separate regression — for each additional output variable. Similarly,
a polynomial approximation would require a doubling of the number of
parameters for each additional output.
The use of a single feedforward network with multiple outputs makes
sense, of course, when the outputs of the network are closely related or
dependent on the same set of input variables. This type of network is
especially useful, as well as economical or parsimonious in terms of param-
eters, when we are forecasting a specific variable, such as inflation, at
different horizons. The set of input variables would be the usual determi-
nants of inflation, such as lags of inflation, and demand and cost variables.
The output variables could be inflation forecasts at one-month, quarterly,
six-month, and one-year horizons.
Another application would be a forecast of the term structure of interest
rates. The output variables would be forecasts of interest rates for matu-
rities of three months, six months, one year, and perhaps two years, while
the input variables would be the usual determinants of interest rates, such
as monetary growth rates, lagged inflation rates, and foreign interest rates.
Finally, classification networks, discussed below, are a very practical
application of multiple-output networks. In this type of model, for example,

38
2. What Are Neural Networks?
we may wish to classify outcomes as a probability of low, medium, or high
risk. We would have two outputs for the probability of low and medium risk,
and the high-risk case would simply be one minus the two probabilities.
2.5
Neural Network Smooth-Transition Regime
Switching Models
While the networks discussed above are commonly used approximators,
an important question remains: How can we adapt these networks for
addressing important and recurring issues in empirical macroeconomics and
finance? In particular, researchers have long been concerned with structural
breaks in the underlying data-generating process for key macroeconomic
variables such as GDP growth or inflation. Does one regime or structure
hold when inflation is high and another when inflation is low or even below
zero? Similarly, do changes in GDP have one process in recession and
another in recovery? These are very important questions for forecasting
and policy analysis, since they also involve determining the likelihood of
breaking out of a deflation or recession regime.
There have been many macroeconomic time-series studies based on
regime switching models. In these models, one set of parameters governs
the evolution of the dependent variable, for example, when the economy is
in recovery or positive growth, and another set of parameters governs the
dependent variable when the economy is in recession or negative growth.
The initial models incorporated two different linear regimes, switching
between periods of recession and recovery, with a discrete Markov pro-
cess as the transition function from one regime to another [see Hamilton
(1989, 1990)]. Similarly, there have been many studies examining non-
linearities in business cycles, which focus on the well-observed asymmetric
adjustments in times of recession and recovery [see Ter¨asvirta and Anderson
(1992)]. More recently, we have seen the development of smooth-transition
regime switching models, discussed in Frances and van Dijk (2000), origi-
nally developed by Ter¨asvirta (1994), and more generally discussed in van
Dijk, Ter¨asvirta, and Franses (2000).
2.5.1
Smooth-Transition Regime Switching Models
The smooth-transition regime switching framework for two regimes has the
following form:
yt = α1xt · Ψ(yt−1; θ, c) + α2xt · [1 −Ψ(yt−1; θ, c)]
(2.61)
where xt is the set of regressors at time t, α1 represents the parameters in
state 1, and α2 is the parameter vector in state 2. The transition function Ψ,

2.5 Neural Network Smooth-Transition Regime Switching Models
39
which determines the influence of each regime or state, depends on the
value of yt−1 as well as a smoothness parameter vector θ and a threshold
parameter c. Franses and van Dijk (2000, p. 72) use a logistic or logsigmoid
specification for Ψ(yt−1; θ, c):
Ψ(yt−1; θ, c) =
1
1 + exp[−θ(yt−1 −c)]
(2.62)
Of course, we can also use a cumulative Gaussian function instead of
the logistic function. Measures of Ψ are highly useful, since they indicate
the likelihood of continuing in a given state. This model, of course, can be
extended to multiple states or regimes [see Franses and van Dijk (2000),
p. 81].
2.5.2
Neural Network Extensions
One way to model a smooth-transition regime switching framework with
neural networks is to adapt the feedforward network with jump connections.
In addition to the direct linear links from the inputs or regressors x to
the dependent variable y, holding in all states, we can model the regime
switching as a jump-connection neural network with one hidden layer and
two neurons, one for each regime. These two regimes are weighted by a
logistic connector which determines the relative influence of each regime or
neuron in the hidden layer. This system appears in the following equations:
yt = αxt + β{[Ψ(yt−1; θ, c)]G(xt; κ)+
[1 −Ψ(yt−1; θ, c)]H(xt; λ)} + ηt
(2.63)
where xt is the vector of independent variables at time t, and α rep-
resents the set of coefficients for the direct link. The functions G(xt; κ)
and H(xt; λ), which capture the two regimes, are logsigmoid and have the
following representations:
G(xt; κ) =
1
1 + exp[−κxt]
(2.64)
H(xt; λ) =
1
1 + exp[−λxt]
(2.65)
where the coefficient vectors κ and λ are the coefficients for the vector xt
in the two regimes, G(xt; κ) and H(xt; λ).
Transition function Ψ, which determines the influence of each regime,
depends on the value of yt−1 as well as the parameter vector θ and a
threshold parameter c. As Franses and van Dyck (2000) point out, the

40
2. What Are Neural Networks?
parameter θ determines the smoothness of the change in the value of this
function, and thus the transition from one regime to another regime.
This neural network regime switching system encompasses the linear
smooth-transition regime switching system. If nonlinearities are not signif-
icant, then the parameter β will be close to zero. The linear component may
represent a core process which is supplemented by nonlinear regime switch-
ing processes. Of course there may be more regimes than two, and this
system, like its counterpart above, may be extended to incorporate three
or more regimes. However, for most macroeconomic and financial studies,
we usually consider two regimes, such as recession and recovery in business
cycle models or inflation and deflation in models of price adjustment.
As in the case of linear regime switching models, the most important
payoffof this type of modeling is that we can forecast more accurately
not only the dependent variable, but also the probability of continuing in
the same regime. If the economy is in deflation or recession, given by the
H(xt; λ) neuron, we can determine if the likelihood of continuing in this
state, 1 −Ψ(yt−1; θ, c), is close to zero or one, and whether this likelihood
is increasing or decreasing over time.9
Figure 2.10 displays the architecture of this network for three input
variables.
X3
X1
X2
H
G
Y
1 − Ψ
Ψ
Linear System
Nonlinear System
Input Variables
Output
Variable
FIGURE 2.10. NNRS model
9In succeeding chapters, we compare the performance of the neural network smooth-
transition regime switching system with that of the linear smooth-transition regime
switching model and the pure linear model.

2.6 Nonlinear Principal Components: Intrinsic Dimensionality
41
2.6
Nonlinear Principal Components: Intrinsic
Dimensionality
Besides forecasting specific target or output variables, which are deter-
mined or predicted by specific input variables or regressors, we may wish
to use a neural network for dimensionality reduction or for distilling a large
number of potential input variables into a smaller subset of variables that
explain most of the variation in the larger data set. Estimation of such net-
works is called unsupervised training, in the sense that the network is not
evaluated or supervised by how well it predicts a specific readily observed
target variable.
Why is this useful? Many times, investors make decisions on the basis
of a signal from the market. In point of fact, there are many markets
and many prices in financial markets. Well-known indicators such as the
Dow-Jones Industrial Average, the Standard and Poor 500, or the National
Association of Security Dealers’ Automatic Quotations (NASDAQ) are just
that, indices or averages of prices of specific shares or all the shares listed
on the exchanges. The problem with using an index based on an average
or weighted average is that the market may not be clustered around the
average.
Let’s take a simple example: grades in two classes. In one class, half of
the students score 80 and the other half score 100. In another class, all of
the students score 90. Using only averages as measures of student perfor-
mances, both classes are identical. Yet in the first class, half of the students
are outstanding (with a grade of 100) and the other half are average (with
a grade of 80). In the second class, all are above average, with a grade of
90. We thus see the problem of measuring the intrinsic dimensionality of
a given sample. The first class clearly needs two measures to explain sat-
isfactorily the performance of the students, while one measure is sufficient
for the second class.
When we look at the performance of financial markets as a whole, just
as in the example of the two classes, we note that single indices can be very
misleading about what is going on. In particular, the market average may
appear to be stagnant, but there may be some very good performers which
the overall average fails to signal.
In statistical estimation and forecasting, we often need to reduce the
number of regressors to a more manageable subset if we wish to have a
sufficient number of degrees of freedom for any meaningful inference. We
often have many candidate variables for indicators of real economic activity,
for example, in studies of inflation [see Stock and Watson (1999)]. If we use
all of the possible candidate variables as regressors in one model, we bump
up against the “curse of dimensionality,” first noted by Bellman (1961).
This “curse” simply means that the sample size needed to estimate a model

42
2. What Are Neural Networks?
with a given degree of accuracy grows exponentially with the number of
variables in the model.
Another reason for turning to dimensionality reduction schemes, espe-
cially when we work with high-frequency data sets, is the empty space
phenomenon. For many periods, if we use very small time intervals, many
of the observations for the variables will be at zero values. Such a set
of variables is called a sparse data set. With such a data set estimation
becomes much more difficult, and dimensionality reduction methods are
needed.
2.6.1
Linear Principal Components
The linear approach to reducing a larger set of variables into a smaller
subset of signals from a large set of variables is called principal components
analysis (PCA). PCA identifies linear projections or combinations of data
that explain most of the variation of the original data, or extract most
of the information from the larger set of variables, in decreasing order of
importance. Obviously, and trivially, for a data set of K vectors, K linear
combinations will explain the total variation of the data. But it may be the
case that only two or three linear combinations or principal components
may explain a very large proportion of the variation of the total data set,
and thus extract most of the useful information for making decisions based
on information from markets with large numbers of prices.
As Fotheringhame and Baddeley (1997) point out, if the underlying true
structure interrelating the data is linear, then a few principal components or
linear combinations of the data can capture the data “in the most succinct
way,” and the resulting components are both uncorrelated and independent
[Fotheringhame and Baddeley (1997), p. 1].
Figure 2.11 illustrates the structure of principal components mapping. In
this figure, four input variables, x1 through x4, are mapped into identical
output variables x1 through x4, by H units in a single hidden layer. The
H units in the hidden layer are linear combinations of the input variables.
The output variables are themselves linear combinations of the H units.
We can call the mapping from the inputs to the H-units a “dimensionality
reduction mapping,” while the mapping from the H-units to the output
variables is a “reconstruction mapping.”10
The method by which the coefficients linking the input variables to the
H units are estimated is known as orthogonal regression. Letting X =
[x1, . . . , xk] be a dimension T by k matrix of variables we obtain the fol-
lowing eigenvalues λx and eigenvectors νx through the process of orthogonal
10See Carreira-Perpinan (2001) for further discussion of dimensionality reduction in
the context of linear and nonlinear methods.

2.6 Nonlinear Principal Components: Intrinsic Dimensionality
43
x1
x4
x3
x2
x1
x2
x3
x4
Inputs
H-Units
Outputs
FIGURE 2.11. Linear principal components
regression through calculation of eigenvalues and eigenvectors:
[X′X −λxI]νx = 0
(2.66)
For a set of k regressors, there are, of course, at most k eigenvalues
and k eigenvectors. The eigenvalues are ranked from the largest to the
smallest. We use the eigenvector νx associated with the largest eigenvalue
to obtain the first principal component of the matrix X. This first principle
component is simply a vector of length T, computed as a weighted average
of the k-columns of X, with the weighting coefficients being the elements of
νx. In a similar manner, we may find second and third principal components
of the input matrix by finding the eigenvector associated with the second
and third largest eigenvalues of the matrix X, and multiplying the matrix
by the coefficients from the associated eigenvectors.
The following system of equations shows how we calculate the princi-
ple components from the ordered eigenvalues and eigenvectors of a T-by-k
dimension matrix X:


X′X −


λ1
x
0
0 . . . 0
0
λ2
x
0 . . . 0
0
0
0 . . . λk
x

· Ik


[ν1
x ν2
x . . . νk
x] = 0
The total explanatory power of the first two or three sets of principal
components for the entire data set is simply the sum of the two or three
largest eigenvalues divided by the sum of all of eigenvalues.


## Training Neural Networks

44
2. What Are Neural Networks?
x1
x2
x3
x4
Inputs
x2
x4
x1
x3
Inputs
c11
c22
c21
c12
H-Units
FIGURE 2.12. Neural principal components
2.6.2
Nonlinear Principal Components
The neural network structure for nonlinear principal components anal-
ysis (NLPCA) appears in Figure 2.12, based on the representation in
Fotheringhame and Baddeley (1997).
The four input variables in this network are encoded by two intermediate
logsigmoid units, C11 and C12, in a dimensionality reduction mapping.
These two encoding units are combined linearly to form H neural principal
components. The H-units in turn are decoded by two decoding logsigmoid
units C21 and C22, in a reconstruction mapping, which are combined
linearly to regenerate the inputs as the output layers.11 Such a neural
network is known as an auto-associative mapping, because it maps the
input variables x1, . . . , x4 into themselves.
Note that there are two logsigmoidal unities, one for the dimensionality
reduction mapping and one for the reconstruction mapping.
Such a system has the following representation, with EN as an encod-
ing neuron and DN as a decoding neuron. Letting X be a matrix with
K columns, we have J encoding and decoding neurons, and P nonlinear
principal components:
ENj =
K

k=1
αj,kXk
ENj =
1
1 + exp(−ENj)
11Fotheringhame and Baddeley (1997) point out that although it is not strictly
required, networks usually have equal numbers in the encoding and decoding layers.

2.6 Nonlinear Principal Components: Intrinsic Dimensionality
45
Hp =
J

j=1
βp,jENj
DNj =
P

p=1
γj,pHp
DNj =
1
1 + exp(−DNj)

Xk =
J

j=1
δk,jDNj
The coefficients of the network link the input variables x to the encoding
neurons C11 and C12, and to the nonlinear principal components. The
parameters also link the nonlinear principal components to the decoding
neurons C21 and C22, and the decoding neurons to the same input vari-
ables x. The natural way to start is to take the sum of squared errors for
each of the predicted values of x, denoted by x and the actual values. The
sum of the total squared errors for all of the different x’s is the object of
minimization, as shown in Equation 2.67:
Min
k

j=1
T

t=1
[xjt −xjt]2
(2.67)
where k is the number of input variables and T is the number of obser-
vations. This procedure in effect gives an equal weight to all of the input
categories of x. However, some of the inputs may be more volatile than
others, and thus harder to accurately predict as than others. In this case,
it may not be efficient to give equal weight to all of the variables, since
the computer will be working equally hard to predict inherently less pre-
dictable variables as it is for more predictable variables. We would like the
computer to spend more time where there is a greater chance of success. In
robust regression, we can weight the different squared errors of the input
variables differently, giving less weight to those inputs that are inherently
more volatile or less predictable and more weight to those that are less
volatile and thus easier to predict:
Min[vΣ−1v′]
(2.68)
where αj is the weight given to each of the input variables. This weight
is determined during the estimation process itself. As each of the errors is

46
2. What Are Neural Networks?
computed for the different input variables, we form the matrix Σ during
the estimation process:
E =


e11e21 . . . ek1
e12e22 . . . ek2
... ...
e1T e2T . . . ekT


(2.69)
Σ = E′E
(2.70)
where Σ is the variance–covariance matrix of the residuals and v is the row
vector of the sum of squared errors:
vt = [e1te2t . . . ekt]
(2.71)
This type of robust estimation, of course, is applicable to any model
having multiple target or output variables, but it is particularly useful for
nonlinear principal components or auto-associative maps, since valuable
estimation time will very likely be wasted if equal weighting is given to
all of the variables. Of course, each ekt will change during the course of
the estimation process or training iterations. Thus Σ will also change and
initially not reflect the true or final covariance weighting matrix. Thus, for
the initial stages of the training, we set Σ equal to the identity matrix of
dimension k, Ik. Once the nonlinear network is trained, the output is the
space spanned by the first H nonlinear principal components.
Estimation of a nonlinear dimensionality reduction method is much
slower than that of linear principal components. We show, however, that
this approach is much more accurate than the linear method when we
have to make decisions in real time. In this case, we do not have time
to update the parameters of the network for reducing the dimension of a
sample. When we have to rely on the parameters of the network from the
last period, we show that the nonlinear approach outperforms the linear
principal components.
2.6.3
Application to Asset Pricing
The H principal component units from linear orthogonal regression or neu-
ral network estimation are particularly useful for evaluating expected or
required returns for new investment opportunities, based on the capital
asset pricing model, better known as the CAPM. In its simplest form, this
theory requires that the minimum required return for any asset or portfolio
k, rk, net of the risk-free rate rf, is proportional, by a factor βk, to the

2.6 Nonlinear Principal Components: Intrinsic Dimensionality
47
difference between the observed market return, rm, less the risk-free rate:
rk = rf + βk[rm −rf]
(2.72)
βk = Cov(rk, rm)
V ar(rm)
(2.73)
rk,t = rk,t + ϵt
(2.74)
The coefficient βk is widely known as the CAPM beta for an asset or
portfolio return k, and is computed as the ratio of the covariance of the
returns on asset k with the market return, divided by the variance of the
return on the market. This beta, of course, is simply a regression coefficient,
in which the return on asset k, rk, less the risk-free rate, rf, is regressed
on the market rate, rm, less the same risk-free rate. The observed market
return at time t, rk,t, is assumed to be the sum of two components: the
required return, rk,t, and an unexpected noise or random shock, ϵt. In this
CAPM literature, the actual return on any asset rk,t is a compensation
for risk. The required return rk,t represents diversifiable risk in financial
markets, while the noise term represents nondiversifiable idiosyncratic risk
at time t.
The appeal of the CAPM is its simplicity in deriving the minimum
expected or required return for an asset or investment opportunity. In
theory, all we need is information about the return of a particular asset k,
the market return, the risk-free rate, and the variance and covariance of
the two return series. As a decision rule, it is simple and straightforward:
if the current observed return on asset k at time t, rk,t, is greater than the
required return, rk, then we should invest in this asset.
However, the limitation of the CAPM is that it identifies the market
return with only one particular market return. Usually the market return
is an index, such as the Standard and Poor or the Dow-Jones, but for many
potential investment opportunities, these indices do not reflect the relevant
or benchmark market return. The market average is not a useful signal
representing the news and risks coming from the market. Not surprisingly,
the CAPM model does not do very well in explaining or predicting the
movement of most asset returns.
The arbitrage pricing theory (APT) was introduced by Ross (1976) as an
alternative to the CAPM. As Campbell, Lo, and MacKinlay (1997) point
out, the APT provides an approximate relation for expected or required
asset returns by replacing the single benchmark market return with a num-
ber of unidentified factors, or principal components, distilled from a wide
set of asset returns observed in the market.
The intertemporal capital asset pricing model (ICAPM) developed by
Merton (1973) differs from the APT in that it specifies the benchmark

48
2. What Are Neural Networks?
market return index as one argument determining the required return, but
allows additional arguments or state variables, such as the principal com-
ponents distilled from a wider set of returns. These arise, as Campbell,
Lo, and MacKinlay (1997) point out, from investors’ demand to hedge
uncertainty about further investment opportunities.
In practical terms, as Campbell, Lo, and MacKinlay also note, it is
not necessary to differentiate the APT from the ICAPM. We may use one
observed market return as one variable for determining the required return.
But one may include other arguments as well, such as macroeconomic indi-
cators that capture the systematic risk of the economy. The final remaining
arguments can be the principal components, either from the linear or neural
estimation, distilled from a wide set of observed asset returns.
Thus, the required return on asset k, rk, can come from a regression of
these returns, on one overall market index rate of return, on a set of macro-
economic variables (such as the yield spread between long- and short-term
rates for government bonds, the expected and unexpected inflation rates,
industrial production growth, and the yield between corporate high and
low-grade bonds) and on a reasonably small set of principal components
obtained from a wide set of returns observed in the market. Campbell, Lo,
and MacKinlay cite research that suggests that five would be an adequate
number of principal components to compute from the overall set of returns
observed in the market.
We can of course combine the forecasts of the CAPM, the APT, and
the nonlinear autoassociative maps associated with the nonlinear principal
component forecasts with a thick model. Granger and Jeon (2001) describe
thick modeling as “using many alternative specifications of similar quality,
using each to produce the output required for the purpose of the modeling
exercise,” and then combining or synthesizing the results [Granger and
Jeon (2001), 3].
Finally, as we discuss later, a very useful application — likely the most
useful application — of nonlinear principal components is to distill infor-
mation about the underlying volatility dynamics from observed data on
implied volatilities in markets for financial derivatives. In particular, we
can obtain the implied volatility measures on all sorts of options, and swap-
options or “swaptions” of maturities of different lengths, on a daily basis.
What is important for market participants to gauge is the behavior of the
market as a whole: From these diverse signals, volatilities of different matu-
rities, is the riskiness of the market going up or down? We show that for
a variety of implied volatility data, one nonlinear principal component can
explain a good deal of the overall market riskiness, where it takes two or
more linear principal components to achieve the same degree of explanatory
power. Needless to say, one measure for summing up market developments
is much better than two or more.
While the CAPM, APT, and ICAPM are used for making decisions about
required returns, nonlinear principal components may also be used in a

2.7 Neural Networks and Discrete Choice
49
dynamic context, in which lagged variables may include lagged linear or
nonlinear principal components for predicting future rates of return for any
asset. Similarly, the linear or nonlinear principal component may be used
to reduce a larger number of regressors to a smaller, more manageable
number of regressors for any type of model. A pertinent example would
be to distill a set of principal components from a wide set of candidate
variables that serve as leading indicators for economic activity. Similarly,
linear or nonlinear principal components distilled from the wider set of
leading indicators may serve as the proxy variables for overall aggregate
demand in models of inflation.
2.7
Neural Networks and Discrete Choice
The analysis so far assumes that the dependent variable, y, to be predicted
by the neural network, is a continuous random variable rather than a dis-
crete variable. However, there are many cases in financial decision making
when the dependent variable is discrete. Examples are easy to find, such as
classifying potential loans as low and acceptable risk or high and unaccept-
able. Another is the likelihood that a particular credit card transaction is
a true or a fraudulent charge.
The goal of this type of analysis is to classify data, as accurately as
possible, into membership in two groups, coded as 0 or 1, based on observed
characteristics. Thus, information on current income, years in current job,
years of ownership of a house, and years of education, may help classify a
particular customer as an acceptable or high-risk case for a new car loan.
Similarly, information about the time of day, location, and amount of a
credit card charge, as well as the normal charges of a particular card user,
may help a bank security officer determine if incoming charges are more
likely to be true and classified as 0, or fraudulent and classified as 1.
2.7.1
Discriminant Analysis
The classical linear approach for classification based on observed char-
acteristics is linear discriminant analysis. This approach takes a set of
k-dimensional characteristics from observed data falling into two groups, for
example, a group that paid its loans on schedule and another that became
arrears in loan payments. We first define the matrices X1, X2, where the
rows of each Xi represent a series of k-different characteristics of the mem-
bers of each group, such as a low-risk or a high-risk group. The relevant
characteristics may be age, income, marital status, and years in current
employment. Discriminant analysis proceeds in three steps:
1. Calculate the means of the two groups, X1, X2, as well as the
variance–covariance matrices, Σ1, Σ2.

50
2. What Are Neural Networks?
2. Compute the pooled variance, Σ =

n1−1
n1+n2−2

Σ1 +

n2−1
n1+n2−2

Σ2,
where n1, n2 represent the population sizes in groups 1 and 2.
3. Estimate the coefficient vector, β = Σ−1 
X1 −X2

.
4. With the vector β, examine the characteristics of a new set of charac-
teristics for classification in either the low-risk or high-risk sets, X1 or
X2. Defining the net set of characteristics, xi, we calculate the value:
βxi. If this value is closer to βX1 than to βX2, then we classify xi
as belonging to the low-risk group X1. Otherwise, it is classified as
being a member of X2.
Discriminant analysis has the advantage of being quick, and has been
widely used for an array of interesting financial applications.12 However, it
is a simple linear method, and does not take into account any assumptions
about the distribution of the dependent variable used in the classification.
It classifies a set of characteristics 
X as belonging to group 1 or 2 simply
by a distance measure. For this reason it has been replaced by the more
commonly used logistic regression.
2.7.2
Logit Regression
Logit analysis assumes the following relation between probability pi of the
binary dependent variable yi, taking values zero or one, and the set of k
explanatory variables x:
pi =
1
1 + e−[xiβ+β0]
(2.75)
To estimate the parameters β and β0, we simply maximize the following
log-likelihood function Λ with respect to the parameter vector β:
Max
<β> Λ =

(pi)yi (1 −pi)1−yi
(2.76)
=
 
1
1 + e−[xiβ+β0]
yi 
e−[xiβ+β0]
1 + e−[xiβ+β0]
1−yi
(2.77)
where yi represents the observed discrete outcomes.
12For example, see Altman (1981).

2.7 Neural Networks and Discrete Choice
51
For optimization, it is sometimes easier to optimize the log-likelihood
function ln(Λ) :
Max
<β> ln(Λ) = yi ln(pi) + (1 −yi) ln (1 −pi)
(2.78)
The k dimensional coefficient vector β does not represent a set of partial
derivatives with respect to characteristics xk. The partial derivative comes
from the following expression:
∂pi
∂xi,k
=
exiβ+β0
(1 + exiβ+β0)2 βk
(2.79)
The partial derivatives are of particular interest if we wish to identify
critical characteristics that increase or decrease the likelihood of being in
a particular state or category, such as representing a risk of default on a
loan.13,14
The usual way to evaluate this logistic model is to examine the percentage
of correct predictions, both true and false, set at 1 and 0, on the basis of
the expected value. Setting the estimated pi at 0 or 1 depends on the choice
of an appropriate threshold value. If the estimated probability or expected
value pi is greater than .5, then pi is rounded to 1, and expected to take
place. Otherwise, it is not expected to occur.15
2.7.3
Probit Regression
Probit models are also used: these models simply use the cumulative
Gaussian normal distribution rather than the logistic function for calcu-
lating the probability of being in one category or not:
pi = Φ(xiβ + β0)
=
	 xiβ+β0
−∞
φ(t)dt
where the symbol Φ is simply the cumulative standard distribution, while
the lower case symbol, φ, as before, represents the standard normal den-
sity function. We maximize the same log-likelihood function. The partial
13In many cases, a risk-averse decision maker may take a more conservative approach.
For example, if the risk of having serious cancer exceeds .3, the physician may wish to
diagnose the patient as a “high risk,” warranting further diagnosis.
14More discussion appears in Section 2.7.4 about the computation of partial deriva-
tives in nonlinear neural network regression.
15Further discussion appears in Section 2.8 about evaluating the success of a nonlinear
regression.

52
2. What Are Neural Networks?
derivatives, however, come from the following expression:
∂pi
∂xi,k
= φ(xiβ + β0)βk
(2.80)
Greene (2000) points out that the logistic distribution is similar to the
normal one, except in the tails. However, he points out that it is difficult to
justify the choice of one distribution or another on “theoretical grounds,”
and for most cases, “it seems not to make much difference” [Greene (2000),
p. 815].
2.7.4
Weibull Regression
The Weibull distribution is an asymmetric distribution, strongly negatively
skewed, approaching zero only slowly, and 1 more rapidly than the probit
and logit models:
pi = 1 −exp(−exp(xiβ + β0))
(2.81)
This distribution is used for classification in survival analysis and comes
from “extreme value theory.” The partial derivative is given by the following
equation:
∂pi
∂xi,k
= exp(xiβ + β0) exp(−(xiβ + β0))βk
(2.82)
This distribution is also called the Gompertz distribution and the regression
model is called the Gompit model.
2.7.5
Neural Network Models for Discrete Choice
Logistic regression is a special case of neural network regression for binary
choice, since the logistic regression represents a neural network with one
hidden neuron. The following adapted form of the feedforward network
may be used for a discrete binary choice model, predicting probability pi
for a network with k∗input characteristics and j∗neurons:
nj,i = ωj,0 +
k∗

k=1
ωj,kxk,i
(2.83)
Nj,i =
1
1 + e−nj,i
(2.84)
pi =
j∗

j=1
γjNj,i
(2.85)

2.7 Neural Networks and Discrete Choice
53
j∗

j=1
γj = 1, γj ≥0
Note that the probability pi is a weighted average of the logsigmoid neu-
rons Nj,i, which are bounded between 0 and 1. Since the final probability
is also bounded in this way, the final probability is a weighted average of
these neurons. As in logistic regression, the coefficients are obtained by
maximizing the product of likelihood function, given the preceding (or the
sum of the log-likelihood function).
The partial derivatives of the neural network discrete choice models are
given by the following expression:
∂pi
∂xi,k
=
j∗

j=1
γjNj,i(1 −Nj,i)ωj,k
2.7.6
Models with Multinomial Ordered Choice
It is straightforward to extend the logit and neural network models to
the case of multiple discrete choices or classification into three or more
outcomes. In this case, logit regression is known as logistic estimation. For
example, a credit officer may wish to classify potential customers into safe,
low-risk, and high-risk categories based on a net of characteristics, xk.
One direct approach for such a classification is a nested classification.
One can use the logistic or neural network model to separate the normal
categories from the absolute default or high-risk categories, with a first-
stage estimation. Then, with the remaining normal data, one can separate
the categories into low-risk and higher-risk categories.
However, there are many cases in financial decision making where there
are multiple categories. Bond ratings, for example, are often in three or
four categories. Thus, one might wish to use logistic or neural network
classification to predict which type of category a particular firm’s bond may
fall into, given the characteristics of the particular firm, from observable
market data and current market classifications or bond ratings.
In this case, using the example of three outcomes, we use the softmax
function to compute p1, p2, p3 for each observation i:
P1,i =
1
1 + e−[xiβ1+β10]
(2.86)
P2,i =
1
1 + e−[xiβ2+β20]
(2.87)
P3,i =
1
1 + e−[xiβ3+β30]
(2.88)

54
2. What Are Neural Networks?
The probabilities of falling in category 1, 2, or 3 come from the
cumulative probabilities:
p1,i =
P1,i
3
j=1 Pj,i
(2.89)
p2,i =
P2,i
3
j=1 Pj,i
(2.90)
p3,i =
P3
3
j=1 Pj,i
(2.91)
Neural network models yield the cumulative probabilities in a similar
manner. In this case there are m∗neurons in the hidden layer, k∗inputs,
and j probability outputs at each observation i, for i∗observations:
nm,i = ωm,0 +
k∗

k=1
ωj,kxk,i
(2.92)
Nm,i =
1
1 + enm,i
(2.93)
Pj,i =
m∗

m=1
γm,iNj,i,
for j = 1, 2, 3
(2.94)
m∗

m=1
γm,i = 1, γm,i ≥0
(2.95)
pj,i =
Pj,i
3
j=1 Pj,i
(2.96)
The parameters of both the logistic and neural network models are
estimated by maximizing a similar likelihood function:
Λ =
i=i∗

i=0
(p1,i)y1,i (p2,i)y2,i (p3,i)y3,i
(2.97)
The success of these alternative models is readily tabulated by the
percentage of correct predictions for particular categories.

2.8 The Black Box Criticism and Data Mining
55
2.8
The Black Box Criticism and Data Mining
Like polynomial approximation, neural network estimation is often criti-
cized as a black box. How do we justify the number of parameters, neurons,
or hidden layers we use in a network? How does the design of the net-
work relate to “priors” based on underlying economic or financial theory?
Thomas Sargent (1997), quoting Lucas’s advice to researchers, reminds us
to beware of economists bearing “free parameters.” By “free,” we mean
parameters that cannot be justified or restricted on theoretical grounds.
Clearly, models with a large number of parameters are more flexible than
models with fewer parameters and can explain more variation in the data.
But again, we should be wary. A criticism closely related to the black box
issue is even more direct: a model that can explain everything, or nearly
everything, in reality explains nothing. In short, models that are too good
to be true usually are.
Of course, the same criticism can be made, mutatis mutandis, of linear
models. All too often, the lag length of autoregressive models is adjusted to
maximize the in-sample explanatory power or minimize the out-of-sample
forecasting errors. It is often hard to relate the lag structure used in many
linear empirical models to any theoretical priors based on the underlying
optimizing behavior of economic agents.
Even more to the point, however, is the criticism of Wolkenhauer (2001):
“formal models, if applicable to a larger class of processes are not specific
(precise) enough for a particular problem, and if accurate for a particular
problem they are usually not generally applicable” [Wolkenhauer (2001),
p. xx].
The black box criticism comes from a desire to tie down empirical
estimation with the underlying economic theory. Given the assumption
that households, firms, and policy makers are rational, these agents or
actors make decisions in the form of optimal feedback rules, derived from
constrained dynamic optimization and/or strategic interaction with other
players. The agents fully know their economic environment, and always act
optimally or strategically in a fully rational manner.
The case for the use of neural networks comes from relaxing the assump-
tion that agents fully know their environment. What if decision makers
have to learn about their environment, about the nature of the shocks and
underlying production, the policy objectives and feedback rules of the gov-
ernment, or the ways other players formulate their plans? It is not too hard
to imagine that economic agents have to use approximations to capture and
learn the way key variables interact in this type of environment.
From this perspective, the black box attack could be turned around.
Should not fundamental theory take seriously the fact that economic
decision makers are in the process of learning, of approximating their envi-
ronment? Rather than being characterized as rational and all knowing,

56
2. What Are Neural Networks?
economic decision makers are boundedly rational and have to learn by
working with several approximating models in volatile environments. This
is what Granger and Jeon (2001) mean by “thick modeling.”
Sargent (1999) himself has shown us how this can be done. In his book
The Conquest of American Inflation, Sargent argues that inflation policy
“emerges gradually from an adaptive process.” He acknowledges that his
“vindication” story “backs away slightly from rational expectations,” in
that policy makers used a 1960 Phillips curve model, but they “recurrently
re-estimated a distributed lag Phillips curve and used it to reset a target
inflation–unemployment rate pair” [Sargent (1999), pp. 4–5].
The point of Sargent’s argument is that economists should model the
actors or agents in their environments not as all-knowing rational angels
who know the true model but rather in their own image and likeness, as
econometricians who have to approximate, in a recursive or ongoing pro-
cess, the complex interactions of variables affecting them. This book shows
how one form of approximation of the complex interactions of variables
affecting economic and financial decision makers takes place.
More broadly, however, there is the need to acknowledge model uncer-
tainty in economic theory. As Hansen and Sargent (2000) point out, to say
that a model is an approximation is to say that it approximates another
model. Good theory need not work under the “communism of models,”
that the people being modeled “know the model” [Hansen and Sargent
(2000), p. 1]. Instead, the agents must learn from a variety of models, even
misspecified models.
Hansen and Sargent invoke the Ellsberg paradox to make this point.
In this setup, originally put forward by Daniel Ellsberg (1961), there is
a choice between two urns, one that contains 50 red balls and 50 black
balls, and the second urn, in which the mix is unknown. The players can
choose which urn to use and place bets on drawing red or black balls,
with replacement. After a series of experiments, Ellsberg found that the
first urn was more frequently chosen. He concluded that people behave in
this way to avoid ambiguity or uncertainty. They prefer risk in which the
probabilities are known to situations of uncertainty, when they are not.
However, Hansen and Sargent ask, when would we expect the second urn
to be chosen? If the agents can learn from their experience over time, and
readjust their erroneous prior subjective probabilities about the likelihood
of drawing red or black from the second urn, there would be every reason
to choose the second urn. Only if the subjective probabilities quickly con-
verged to 50-50 would the players become indifferent. This simple example
illustrates the need, as Hansen and Sargent contend, to model decision
making in dynamic environments, with model approximation error and
learning [Hansen and Sargent (2000), p. 6].
However, there is still the temptation to engage in data mining, to
overfit a model by using increasingly complex approximation methods.

2.9 Conclusion
57
The discipline of Occam’s razor still applies: simpler more transparent
models should always be preferred over more complex less transparent
approaches. In this research, we present simple neural network alterna-
tives to the linear model and assess the performance of these alternatives
by time-honored statistical criteria as well as the overall usefulness of these
models for economic insight and decision making. In some cases, the sim-
ple linear model may be preferable to more complex alternatives; in others,
neural network approaches or combinations of neural network and linear
approaches clearly dominate. The point we wish to make in this research is
that neural networks serve as a useful and readily available complement to
linear methods for forecasting and empirical research relating to financial
engineering.
2.9
Conclusion
This chapter has presented a variety of networks for forecasting, for dimen-
sionality reduction, and for discrete choice or classification. All of these
networks offer many options to the user, such as the selection of the num-
ber of hidden layers, the number of neurons or nodes in each hidden layer,
and the choice of activation function with each neuron. While networks can
easily get out of hand in terms of complexity, we show that the most useful
network alternatives to the linear model, in terms of delivering improved
performance, are the relatively simple networks, usually with only one hid-
den layer and at most two or three neurons in the hidden layer. The network
alternatives never do worse, and sometimes do better, in the examples with
artificial data (Chapter 5), with automobile production, corporate bond
spreads, and inflation/deflation forecasting (Chapters 6 and 7).
Of course, for classification, the benchmark models are discriminant anal-
ysis, as well as nonlinear logit, probit, and Weibull methods. The neural
network performs at least as well as or better than all of these more famil-
iar methods for predicting default in credit cards and in banking-sector
fragility (Chapter 8).
For dimensionality reduction, the race is between linear principal compo-
nents and the neural net auto-associate mapping. We show, in the example
with swap-option cap-floor volatility measures, that both methods are
equally useful for in-sample power but that the network outperforms the
linear methods for out-of-sample performance (Chapter 9).
The network architectures can mutate, of course. With a multilayer per-
ceptron or feedforward network with several neurons in a hidden layer,
it is always possible to specify alternative activation functions for the
different neurons, with a logsigmoid function for one neuron, a tansig func-
tion for another, a cumulative Gaussian density for a third. But most

58
2. What Are Neural Networks?
researchers have found the “plain vanilla” multilayer perceptron network
with logsigmoid activation functions fairly reliable and as accurate as more
complex alternatives.
2.9.1
MATLAB Program Notes
The MATLAB program for estimating a multilayer perceptron or feedfor-
ward network on my webpage is the program ffnet9.m and uses the sub-
function ffnet9fun.m. There are similar programs for recurrent Elman net-
works and jump connection networks: ffnet9 elman.m, ffnet9fun elman.m,
ffnet9 jump.m, and ffnet9fun jump.m. The programs have instructions for
the appropriate input arguments as well as descriptions of the outputs of
the program.
For implementing a GARCH model, there is a program mygarch.m,
which invokes functions supplied by the MATLAB Garch Toolbox.
For linear estimation, there is the ols.m program. This program has
several subfunctions for diagnostics.
The classification models use the following programs: classnet.m, class-
netfun.m, logit.m, probit.m, gompit.m.
For principal components, the programs to use are nonlinpc.m and
nonlinpcfun.m. These functions in turn invoke the MATLAB program,
princomp.m, which is part of the MATLAB Statistics Toolbox.
2.9.2
Suggested Exercises
For deriving the ridgelet network function, described in Section 2.4.4, you
can use the MATLAB Symbolic Toolbox. It is easy to use and saves a lot
of time and trouble. At the very least, in writing code, you can simply cut
and paste the derivative formulae from this Toolbox to your own programs.
Simply type in the command funtool.m, and in the box beside “f=”
type in the standard normal Gaussian formula, “inv(2 *pi) * exp(−x ˆ2)”
(no need for parentheses). Then click on the derivative button, “df/dx,”
five times until you arrive at the formula given for the ridgelet network.
Repeat the above exercise for the logsigmoid function, setting in the for-
mula next of “f=” “inv(1+exp(−x))”. After taking the derivatives a number
of times, compare the graph of the function, in the interval [−2 pi, 2 pi]
with that of the corresponding (n−1) derivative of the Gaussian function.
Why do they start to look alike?

3
Estimation of a Network with
Evolutionary Computation
If the specification of the neural network for approximation appears to
be inspired by biology, the reader will no doubt suspect that the best
way to estimate or train a network is inspired by genetics and evolution.
Estimating a nonlinear model is always tricky business. The programs may
fail to converge, or they may converge to locally, rather than globally,
optimal estimates. We show that the best way to estimate a network, to
implement the network, is to harness the power of evolutionary genetic
search algorithms.
3.1
Data Preprocessing
Before moving to the actual estimation, however, the first order of business
is to adjust or scale the data and to remove nonstationarity. In other words,
the first task is data preprocessing. While linear models also require that
data be stationary and seasonally adjusted, scaling is critically important
for nonlinear estimation, since such scaling reduces the search space for
finding the optimal coefficient estimates.
3.1.1
Stationarity: Dickey-Fuller Test
Before starting work with any time series as a dependent variable, we
must ensure that the data represent covariance stationary time series.

60
3. Estimation of a Network with Evolutionary Computation
This means that the first and second moments — means, variances, and
covariances — are constant through time. Since statistical inference is based
on the assumption of fixed means, variances, and covariances, it is essential
to ensure that the variables in question are indeed stationary.
The most commonly used test is the one proposed by Dickey and Fuller
(1979), for a given series {yt}:
∆yt = ρyt−1 + α1∆yt−1 + α2∆yt−2 + · · · + αk∆yt−k + εt
(3.1)
where ∆yt = yt −yt−1, ρ, α1, . . . , αk are coefficients to be estimated, and
εt is a random disturbance term with mean zero and constant variance.
Thus, E(εt) = 0, and E(ε2
t) = σ2.
The null hypothesis under this test is ρ = 0. In this case, the regression
model reduces to the following expression:
yt = yt−1 + α1∆yt−1 + α2∆yt−2 + · · · + αk∆yt−k + εt
(3.2)
Under this null hypothesis, yt at any moment will be equal to yt−1 plus
or minus the effect of the terms given by the sum of αi∆yt−i, i = 1, . . . , k.
In this case, the long-run expected value of the series, when yt = yt−1,
becomes indeterminate. Or perhaps more succinctly, the mean at any given
time is conditional on past values of yt. With ρ = 0, the series is called
nonstationary, or a unit root process.
The relevant alternative hypothesis is ρ < 0. With ρ = −1, the model
reduces to the following expression:
yt = α1∆yt−1 + α2∆yt−2 + · · · + αk∆yt−k + εt
(3.3)
In the long run, with yt = yt−1, by definition, ∆yt−i = 0, for i = i, . . . , k,
so that the expected value of yt, Eyt = E(εt) = 0.
If there is some persistence in the model, with ρ falling in the interval
between [−1, 0], the relevant regression becomes:
yt = (1 + ρ)yt−1 + α1∆yt−1 + α2∆yt−2 + · · · + αk∆yt−k + εt
(3.4)
In this case, in the long run, with yt = yt−1, it is still true that ∆yt−i = 0,
for i = i, . . . , k. The only difference is that the expression for the long-run
mean reduces to the following expression, with ρ∗= (1 + ρ):
yt(1 −ρ∗) = εt
(3.5)
In this case, the expected value of yt, Eyt, is equal to E(εt)/(1 −ρ∗).
It is thus crucial to ensure that the coefficient ρ is significantly less than
zero for stationarity. The tests of Dickey and Fuller are essentially modi-
fied, one-sided t-tests of the hypothesis of ρ < 0 in a linear regression.

3.1 Data Preprocessing
61
Augmented Dickey-Fuller tests allow the presence of constant and trend
terms in the preceding regressions.
The stationarity tests of Dickey and Fuller led to the development of
the Phillips and Perron (1988) test. This test goes beyond Dickey and
Fuller in that it permits a joint test of significance of the coefficients of
the autoregressive term as well as the trend and constant terms.1 Further
work on stationarity has involved tests for structural breaks in univariate
nonstationarity time series [see, for example, Benerjee, Lumsdaine, and
Stock (1992); Lumsdaine and Papell (1997); Perron (1989); and Zivot and
Andrews (1992)].
Fortunately, for most financial time-series data such as share prices,
nominal money supply, and gross domestic product, logarithmic first differ-
encing usually transforms these nonstationarity time series into stationarity
series. Logarithmic first differencing simply involves taking the logarithmic
value of a series Z, and then taking its first difference.
∆zt = ln(Zt) −ln(Zt−1)
(3.6)
zt ≡ln(Zt)
(3.7)
3.1.2
Seasonal Adjustment: Correction for Calendar Effects
A further problem with time-series data arises from seasonal or calendar
effects. With quarterly or monthly data, there are obvious end-of-year
December spikes in consumer spending. With daily data, there are effects
associated with particular months, days of the week, and holidays. The
danger of not adjusting the data for these seasonal factors in nonlinear
neural network estimation is overfitting the data. The nonlinear estima-
tion process will continue to fine tune the fitting of the model or look for
needlessly complex representations to account for purely seasonal factors.
Of course, the danger of any form of seasonal adjustment is that one may
extract useful information from the data. It is thus advisable to work with
the raw, seasonally unadjusted series as a benchmark.
Fortunately, for quarterly or monthly data, one may use a simple dummy
variable regression method. For quarterly data, for example, one estimates
the following regression:
∆z = Q′β + u
(3.8)
1See Hamilton (1994), Chapter 17, for a detailed discussion of unit roots and tests
for stationarity in time series.

62
3. Estimation of a Network with Evolutionary Computation
where ∆zt is the stationarity raw series, the matrix Q = [Q2, Q3, Q4] rep-
resents dummy variables for the second, third, and fourth quarters of the
year, and u is the residual, or everything in the raw series that cannot be
explained by the quarterly dummy variables. These dummy variables take
on values of 1 when the observation falls in the respective quarter, and zero
otherwise.
A similar procedure is performed for monthly data, with eleven monthly
dummy variables.2
For daily data, the seasonal filtering regression is more complicated.
Gallant, Rossi, and Tauchen (1992) propose the following sets of regressors:
1. Day-of-week dummies for Tuesday through Friday
2. Dummy variables for each of the number of nontrading days preceding
the current trading day3
3. Dummy variables for the months of March, April, May, June, July,
August, September, October, and November
4. Dummy variables for each week of December and January
In the Gallant-Rossi-Tauchen procedure, one first regresses the sta-
tionarity variable ∆zt on the set of adjustment variables At, where A is
the matrix of dummy variables, for days of the week, months, weeks in
December and January, and the number of nontrading days preceding the
current trading day:
∆z = A′β + u
(3.9)
Gallant, Rossi, and Tauchen also allow the variance, as well as the mean,
of the data, to be adjusted for the calendar effects. One simply does a
regression of the logarithm of u2 on the set of dummy calendar variables,
A, and the trend terms [t t2], where t = 1, 2, . . . , T, with T representing
the number of observations. The regression equation becomes:
ln(u2) = A′γ + ϵ
(3.10)
A = [A t t2]
(3.11)
2In both cases, omit one dummy variable to avoid collinearity with the constant term
in the regressions.
3Fortunately, most financial websites have information on holidays in most countries,
so that one may obtain the relevant data for the number of nontrading days preceding
each date.

3.1 Data Preprocessing
63
TABLE 3.1. Gallant-Rossi-Tauchen Procedure for Calendar Adjustment
Step
Operation
Define and quantify calendar dummy matrix, A
[A]
Regress dependent variables on dummy matrix
∆z = A′β + u
Form expanded dummy matrix
A = [A t t2]
Regress squared residuals on expanded matrix
ln(u2) = A′γ + ϵ
Transform residuals u to ∆z∗
∆z∗= a + b


u
exp

A′γ
2



They also propose a final linear transformation so that the adjusted
series ∆z∗has the same sample mean and variances as the original raw
series:
∆z∗= a + b


u
exp

A′γ
2



(3.12)
with the variables a and b chosen to ensure that the sample means and
variances of the two series are identical.
Table 3.1 summarizes the Gallant-Rossi-Tauchen procedure for calendar
adjustment.
Of course, seasonal adjustment is also done through smoothing of the
original data series, usually through moving average filters. Many series
available in national income accounts in fact are already seasonally adjusted
by such smoothing methods.
The advantages of different seasonal adjustment procedures depends on
the goal of the research. If the focus is on reliable parameter estimates
of an econometric model, the dummy variable approach is superior.4 In
all of this calendar adjustment, we are replacing the original series with
artificially adjusted data. There may be resistance by decision makers to
this approach, for example, in options pricing, if the underlying adjusted
return series does not match closely the actual observed return series. For
this reason, it is a good strategy to examine the results of the models
with the actual and the calendar-adjusted series. We would expect greater
precision with the adjusted series, and quicker convergence, but the overall
results should not be drastically different.
4See Beck (1981) for a discussion of different types of seasonal adjustment for
econometric model estimation.

64
3. Estimation of a Network with Evolutionary Computation
3.1.3
Data Scaling
When input variables {xt} and stationary output variables {yt} are used
in a neural network, preprocessing or scaling facilitates the nonlinear
estimation process. The reason scaling is helpful, even crucial, is that the
use of very high or low numbers, or series with a few very high or very
low outliers, can cause underflow or overflow problems, with the computer
stopping, or as Judd [(1998), p. 99] points out, the computer continuing
by assigning a value of zero to the values being minimized.
When logsigmoid or tansigmoid neurons are used, to be sure, scaling is
a necessary step. If the data are not scaled to a reasonable interval, such
as [0, 1] or [−1, 1], then the neurons will set reasonably large values simply
at 1, and reasonably low values at 0 (for logsigmoid neurons) or −1 (for
tansig neurons). Without scaling, a great deal of information from the data
is likely to be lost, since the neurons will simply transmit values of minus
one, zero, or plus one for many values of the input data.
There are two main numeric ranges the network specialists use in linear
scaling functions: zero to one, denoted [0, 1], and minus one to plus one
denoted by [−1, 1].
Linear scaling functions make use of the maximum and minimum values
of the series [y x]. The linear scaling function for zero to one transforms a
variable xk into x∗
k in the following way:
x∗
k,t =
xk,t −min(xk)
max(xk) −min(xk)
(3.13)
The linear scaling function for [−1, 1], transforming a variable xk into
x∗∗
k , has the following form:
x∗∗
k,t = 2 ·
xk,t −min(xk)
max(xk) −min(xk) −1
(3.14)
A nonlinear scaling method proposed by Dr. Helge Petersohn of the
University of Leipzig, transforming a variable xk to zk, allows one to specify
the range 0 < zk,t < 1, or ⟨0, 1⟩. The Petersohn scaling function works in
the following way:
zk,t =
1
1+exp
ln[z−1
k −1]−ln[z−1
k −1]
max(xk)−min(xk)

[xk,t−min(xk)]+ln[z−1
k −1]−1

(3.15)
Finally, James DeLeo of the National Institutes of Health suggests scaling
the data in a two-step procedure: first, standardizing a series x, to obtain z,

3.2 The Nonlinear Estimation Problem
65
and then taking the logsigmoid transformation of the standardized
series z:
x∗=
1
1 + exp(−z)
(3.16)
z = x −x
σx
(3.17)
Which type of scaling function works best depends on the quality of
the results. There is no way to decide which scaling function works best,
on a priori grounds, given the features of the data. The best strategy is
to estimate the model with different types of scaling functions to find out
which one gives the best performance, based on in-sample criteria discussed
in the following section.
3.2
The Nonlinear Estimation Problem
Finding the coefficient values for a neural network, or any nonlinear model,
is not an easy job — certainly not as easy as parameter estimation with
a linear approximation. A neural network is a highly complex nonlinear
system. There may be a multiplicity of locally optimal solutions, none
of which deliver the best solution in terms of minimizing the differences
between the model predictions y and the actual values of y. Thus, neural
network estimation takes time and involves the use of alternative methods.
Briefly, in any nonlinear system, we need to start the estimation pro-
cess with initial conditions, or guesses of the parameter values we wish to
estimate. Unfortunately, some guesses may be better than others for mov-
ing the estimation process to the best coefficients for the optimal forecast.
Some guesses may lead us to a local optimum, that is, the best forecast in
the neighborhood of the initial guess, but not the coefficients for giving the
best forecast if we look a bit further afield from the initial guesses for the
coefficients.
Figure 3.1 illustrates the problem of finding globally optimal or globally
minimal points on a highly nonlinear surface.
As Figure 3.1 shows, an initial set of weight values anywhere on the x
axis may lie near to a local or global maximum rather than a minimum,
or near to a saddle point. A minimum or maximum point has a slope or
derivative equal to zero. At a maximum point, the second derivative, or
change in the slope, is negative, while at a minimum point, the change in
the slope is positive. At a saddle point, both the slope and the change in
the slope are zero.

66
3. Estimation of a Network with Evolutionary Computation
Maximum
Saddle point
Maximum
Global minimum 
Local minimum
ERROR
Function
Weight value
FIGURE 3.1. Weight values and error function
As the weights are adjusted, one can get stuck at any of the many posi-
tions where the derivative is zero, or the curve has a flat slope. Too large an
adjustment in the learning parameter may bring one’s weight values from
a near-global minimum point to a maximum or to a saddle point. However,
too small an adjustment may keep one trapped near a saddle point for
quite some time during the training period.
Unfortunately, there is no silver bullet for avoiding the problems of local
minima in nonlinear estimation. There are only strategies involving re-
estimation or stochastic evolutionary search.
For finding the set of coefficients or weights Ω= {ωk,i, γk} in a network
with a single hidden layer, or Ω= {ωk,i, ρl,k, γl} in a network with two
hidden layers, we minimize the loss function Ψ, defined again as the sum of
squared differences between the actual observed output y and y, the output
predicted by the network:
min
ΩΨ(Ω) =
T

t=1
(yt −yt)2
(3.18)
yt = f(xt; Ω)
(3.19)
where T is the number of observations of the output vector y, and f(xt; Ω)
is a representation of the neural network.
Clearly, Ψ(Ω) is a nonlinear function of Ω. All nonlinear optimization
starts with an initial guess of the solution, Ω0, and searches for better solu-
tions, until finding the best possible solution within a reasonable amount
of searching.

3.2 The Nonlinear Estimation Problem
67
We discuss three ways to minimize the function Ψ(Ω):
1. A local gradient-based search, in which we compute first- and second-
order derivatives of Ψ with respect to elements of the parameter vector
Ω, and continue with updating of the initial guess of Ω, by derivatives,
until stopping criteria are reached
2. A stochastic search, called simulated annealing, which does not rely
on the use of first- and second-order derivatives, but starts with
an initial guess Ω0, and proceeds with random updating of the ini-
tial coefficients until a “cooling temperature” or stopping criterion is
reached
3. An evolutionary stochastic search, called the genetic algorithm, which
starts with a population of p initial guesses, [Ω01, Ω02 . . . Ω0p], and
updates the population of guesses by genetic selection, breeding, and
mutation, for many generations, until the best coefficient vector is
found among the last-generation population
All of this discussion is rather straightforward for students of computer
science or engineering. Those not interested in the precise details of non-
linear optimization may skip the next three subsections without fear of
losing their way in succeeding sections.
3.2.1
Local Gradient-Based Search: The Quasi-Newton
Method and Backpropagation
To minimize any nonlinear function, we usually begin by initializing the
parameter vector Ωat any initial value, Ω0, perhaps at randomly chosen
values. We then iterate on the coefficient set Ωuntil Ψ is minimized, by
making use of first- and second-order derivatives of the error metric Ψ with
respect to the parameters. This type of search, called a gradient-based
search, is for the optimum in the neighborhood of the initial parameter
vector, Ω0. For this reason, this type of search is a local search.
The usual way to do this iteration is through the quasi-Newton algorithm.
Starting with the initial set of the sum of squared errors, Ψ(Ω0), based on
the initial coefficient vector Ω0, a second-order Taylor expansion is used to
find Ψ(Ω1) :
Ψ(Ω1) = Ψ(Ω0) + ∇0(Ω1 −Ω0) + .5(Ω1 −Ω0)′H0(Ω1 −Ω0)
(3.20)
where ∇0 is the gradient of the error function with respect to the parameter
set Ω0 and H0 is the Hessian of the error function.

68
3. Estimation of a Network with Evolutionary Computation
Letting Ω0 = [Ω0,1, . . . , Ω0,k], be the initial set of k parameters used in
the network, the gradient vector ∇0 is defined as follows:
∇0 =







Ψ(Ω0,1+h1,...,Ω0,k)−Ψ(Ω0,1,...,Ω0,k)
h1
Ψ(Ω0,1,...,Ω0,i+hi,...,Ω0,k)−Ψ(Ω0,1,...,Ω0,k)
hi
.
.
Ψ(Ω0,1,...,Ω0,i,...,Ω0,k+hk)−Ψ(Ω0,1,...,Ω0,k)
hk







(3.21)
The denominator hi is usually set at max(ϵ, ϵΩ0,i), with ϵ = 10−6.
The Hessian H0 is the matrix of second-order partial derivatives of Ψ
with respect to the elements of Ω0, and is computed in a similar manner as
the Jacobian or gradient vector. The cross-partials or off-diagonal elements
of the matrix H0 are given by the formula:
∂2Ψ
∂Ω0,i∂Ω0,j
=
1
hjhi
×

{Ψ(Ω0,1,...,Ω0,i+hi,Ω0,j +hj,...,Ω0,k)−Ψ(Ω0,1,...,Ω0,i,...,Ω0,j +hj,...,Ω0,k)}
−{Ψ(Ω0,1,...,Ω0,i+hi,Ω0,j,...,Ω0,k)−Ψ(Ω0,1,...,Ω0,k)}

(3.22)
while the direct second-order partials or diagonal elements are given by:
∂2Ψ
∂Ω2
0,i
= 1
h2
i

Ψ(Ω0,1, . . . , Ω0,i + hi, . . . , Ω0,k) −2Ψ(Ω0,1, . . . , Ω0,k)
+Ψ(Ω0,1, . . . , Ω0,i −hi, . . . , Ω0,k)

(3.23)
To find the direction of a change of the parameter set from iteration 0
to iteration 1, one simply minimizes the error function Ψ(Ω1) with respect
to (Ω1 −Ω0). The following formula gives the evolution of the parameter
set Ωfrom the initial specification at iteration 0 to its value at iteration 1.
(Ω1 −Ω0) = −H−1
0 ∇0
(3.24)
The algorithm continues in this way, from iteration 1 to 2, 2 to 3, n −1
to n, until the error function is minimized. One can set a tolerance criterion,
stopping when there are no further changes in the error function below a
given tolerance value. Alternatively, one may simply stop when a specified
maximum number of iterations is reached.
The major problem with this method, as in any nonlinear optimization
method, is that one may find local rather than global solutions, or a saddle-
point solution for the vector Ω∗, which minimizes the error function.

3.2 The Nonlinear Estimation Problem
69
Where the algorithm ends in the optimization process crucially depends
on the choice of the initial parameter vector Ω0. The most commonly used
approach is to start with one random vector, iterate until convergence is
achieved, and begin again with another random parameter vector, iterate
until converge, and compare the final results with the initial iteration.
Another strategy is to repeat this minimization many times until it reaches
a potential global minimum value over the set of minimum values.
Another problem is that as iterations progress, the Hessian matrix H
at iteration n∗may also become nonsingular, so that it is impossible
to obtain H−1
n∗at iteration n∗. Commonly used numerical optimization
methods approximate the Hessian matrix at various iteration periods.
The BFGS (Boyden-Fletcher-Goldfarb-Shanno) algorithm approximates
H−1
n
at step n on the basis of the size of the change in the gradient
∇n-∇n−1 relative to the change in the parameters Ωn −Ωn−1. Other algo-
rithms available are the Davidon-Fletcher-Powell (D-F-P) and Berndt,
Hall, Hall, and Hausman (BHHH). [See Hamilton (1994), p. 139.]
All of these approximation methods frequently blow up when there are
large numbers of parameters or if the functional form of the neural net-
work is sufficiently complex. Paul John Werbos (1994) first developed
the backpropagation method in the 1970s as an alternative for estimat-
ing neural network coefficients under gradient-search. Backpropagation is
a very manageable way to estimate a network without having to iterate and
invert the Hessian matrices under the BFGS, DFP, and BHHH routines. It
remains the most widely used method for estimating neural networks. In
this method, the inverse Hessian matrix, −H−1
0 , is replaced by an identity
matrix, with its dimension equal to the number of coefficients, k, multiplied
by a learning parameter, ρ:
(Ω1 −Ω0) = −H−1
0 ∇0
(3.25)
= −ρ · ∇0
(3.26)
Usually, the learning parameter ρ is specified at the start of the estima-
tion, usually at small values, in the interval [.05, .5], to avoid oscillations.
The learning parameters can be endogenous, taking on different values as
the estimation process appears to converge, when the gradients become
smaller. Extensions of the backpropagation method allow different learn-
ing rates for different parameters. However, efficient as backpropagation
may be, it still suffers from the trap of local rather than global minima,
or saddle point convergence. Moreover, while low values of the learning
parameters avoid oscillations, they may needlessly prolong the convergence
process.
One solution for speeding up the process of backpropagation toward con-
vergence is to add a momentum term to the above process, after a period

70
3. Estimation of a Network with Evolutionary Computation
of n training periods:
(Ωn −Ωn−1) = −ρ · ∇n−1 + µ(Ωn−1 −Ωn−2)
(3.27)
The effect of adding the moment effect, with µ usually set to .9, is to
enable the adjustment of the coefficients to roll or move more quickly over
a plateau in the “error surface” [Essenreiter (1996)].
3.2.2
Stochastic Search: Simulated Annealing
In neural network estimation, where there are a relatively large number
of parameters, Newton-based algorithms are less likely to be useful. It is
difficult to invert the Hessian matrices in this case. Similarly, the initial
parameter vector may not be in the neighborhood of the best solution, so
a local search may not be very efficient.
An alternative search method for optimization is simulated annealing.
It does not require taking first- or second-order derivatives. Rather, it is a
stochastic search method. Originally due to Metropolis et al. (1953), later
developed by Kirkpatrick, Gelatt, and Vecchi (1983), it originates from
the theory of statistical mechanics. According to Sundermann (1996), this
method is based on the analogy between the annealing of solids and solving
optimization.
The simulated annealing process is described in Table 3.2. The basic
message of this approach is well summarized by Haykin (1994): “when opti-
mizing a very large and complex system (i.e. a system with many degrees
of freedom), instead of always going downhill, try to go downhill most of
the time” [Haykin (1994), p. 315].
As Table 3.2 shows, we again start with a candidate solution vector,
Ω0, and the associated error criterion, Ψ0. A shock to the solution vector is
then randomly generated, Ω1, and we calculate the associated error metric,
Ψ1. We always accept the new solution vector if the error metric decreases.
However, since the initial guess Ω0 may not be very good, there is a small
chance that the new vector, even if it does not reduce the error metric,
may be moving in the right direction to a more global solution. So with
a probability P(j), conditioned by the Metropolis ratio M(j), the new
vector may be accepted, even though the error metric actually increases.
The rationale for accepting a new vector Ωi even if the error Ψi is greater
than Ψi−1, is to avoid the pitfall of being trapped in a local minimum point.
This allows us to search over a wider set of possibilities.
As Robinson (1995) points out, simulated annealing consists of run-
ning the accept/reject algorithm between the temperature extremes. Many
changes are proposed, starting at the high temperatures, which explore
the parameter space. With gradually decreasing temperature, however, the

3.2 The Nonlinear Estimation Problem
71
TABLE 3.2. Simulated Annealing for Local Optimization
Definition
Operation
Specify temperature and cooling schedule
parameter T
T(j) =
T
1 + ln(j)
Start random process at j = 0, continue till
j = (1,2,...,T)
Initialize solution vector and error metric
Ω0, Ψ0
Randomly perturbate solution vector, obtain
error metric
Ωj,Ψj
Generate P(j) from uniform distribution
0≤P(j) ≤1
Compute metropolis ratio M(j)
M(j) = exp


−

Ψj −Ψj−1

T(j)


Accept new vector Ωj = Ωj unconditionally
Ωj = Ωj ⇔

Ψj −Ψj−1

< 0
Accept new vector Ωj = Ωj conditionally
P(j) ≤M(j)
Continue process till j = T
algorithm becomes “greedy.” As the temperature T(j) cools, changes are
more and more likely to be accepted only if the error metric decreases.
To be sure, simulated annealing is not strictly a global search. Rather it
is a random search for helping to escape a likely local minimum and move
to a better minimum point. So it is best used after we have converged to a
given point, to see if there are better minimum points in the neighborhood
of the initial minimum.
As we see in Table 3.2, the current state of the system, or coefficient
vector Ωj, depends only on the previous state Ωj−1, and a transition prob-
ability P(j −1) and is thus independent of all previous outcomes. We say
that such a system has the Markov chain property. As Haykin (1994) notes,
an important property of this system is asymptotic convergence, for which
Geman and Geman (1984) gave us a mathematical proof. Their theorem,
summarized from Haykin (1994, p. 317), states the following:
Theorem 1 If the temperature T(k) employed in executing the k-th step
satisfies the bound T(k) ≥T/ log(1+k) for every k, where T is a sufficiently
large constant independent of k, then with probability 1 the system will
converge to the minimum configuration.
A similar theorem has been derived by Aarts and Korst (1989).
Unfortunately, the annealing schedule given in the preceding theorem would
be extremely slow — much too slow for practical use. When we resort
to finite-time approximation of the asymptotic convergence properties,

72
3. Estimation of a Network with Evolutionary Computation
we are no longer guaranteed that we will find the global optimum with
probability one.
For implementing the algorithm in finite-time approximation, we have
to decide on the key parameters in the annealing schedule. Van Laarhoven
and Aarts (1988) have developed more detailed annealing schedules than
the one presented in Table 3.2. Kirkpatrick, Gelatt, and Vecchi (1983)
offered suggestions for the starting temperature T (it should be high
enough to ensure that all proposed transitions are accepted by algo-
rithm), a linear alternative for the temperature decrement function, with
T(k) = αT(k −1), .8 ≤α ≤.99, as well as a stopping rule (the system
is “frozen” if the desired number of acceptances is not achieved at three
successive temperatures). Adaptive simulated annealing is a further devel-
opment which has proven to be faster and has become more widely used
[Ingber (1989)].
3.2.3
Evolutionary Stochastic Search: The Genetic
Algorithm
Both the Newton-based optimization (including backpropagation) and sim-
ulated annealing (SA) start with one random initialization vector Ω0. It
should be clear that the usefulness of both of these approaches to opti-
mization crucially depends on how good this initial parameter guess really
is. The genetic algorithm or GA helps us come up with a better guess for
using either of these search processes.
The GA reduces the likelihood of landing in a local minimum. We no
longer have to approximate the Hessians. Like simulated annealing, it is a
statistical search process, but it goes beyond SA, since it is an evolutionary
search process.
The GA proceeds in the following steps.
Population Creation
This method starts not with one random coefficient vector Ω, but with
a population N ∗(an even number) of random vectors. Letting p be the
size of each column vector, representing the total number of coefficients to
be estimated in the neural network, we create a population N ∗of p by 1
random vector.








Ω1
Ω2
Ω3
.
.
Ωp








1








Ω1
Ω2
Ω3
.
.
Ωp








2








Ω1
Ω2
Ω3
.
.
Ωp








i
. . .








Ω1
Ω2
Ω3
.
.
Ωp








N∗
(3.28)

3.2 The Nonlinear Estimation Problem
73
Selection
The next step is to select two pairs of coefficients from the population at
random, with replacement. Evaluate the fitness of these four coefficient
vectors, in two pair-wise combinations, according to the sum of squared
error function. Coefficient vectors that come closer to minimizing the sum
of squared errors receive better fitness values.
This is a simple fitness tournament between the two pairs of vectors:
the winner of each tournament is the vector with the best fitness. These
two winning vectors (i, j) are retained for “breeding” purposes. While not
always used, it has proven to be extremely useful for speeding up the
convergence of the genetic search process.








Ω1
Ω2
Ω3
.
.
Ωp








i








Ω1
Ω2
Ω3
.
.
Ωp








j
Crossover
The next step is crossover, in which the two parents “breed” two children.
The algorithm allows crossover to be performed on each pair of coefficient
vectors i and j, with a fixed probability p > 0. If crossover is to be per-
formed, the algorithm uses one of three difference crossover operations,
with each method having an equal (1/3) probability of being chosen:
1. Shuffle crossover. For each pair of vectors, k random draws are made
from a binomial distribution. If the kth draw is equal to 1, the
coefficients Ωi,p and Ωj,p are swapped; otherwise, no change is made.
2. Arithmetic crossover. For each pair of vectors, a random number is
chosen, ω ∈(0, 1). This number is used to create two new parameter
vectors that are linear combinations of the two parent factors, ωΩi,p+
(1 −ω)Ωj,p,(1 −ωΩi,p + ω)Ωj,p.
3. Single-point crossover. For each pair of vectors, an integer I is ran-
domly chosen from the set [1, k −1]. The two vectors are then
cut at integer I and the coefficients to the right of this cut point,
Ωi,I+1, Ωj,I+1 are swapped.
In binary-encoded genetic algorithms, single-point crossover is the stan-
dard method. There is no consensus in the genetic algorithm literature on
which method is best for real-valued encoding.

74
3. Estimation of a Network with Evolutionary Computation
Following the crossover operation, each pair of parent vectors is asso-
ciated with two children coefficient vectors, which are denoted C1(i) and
C2(j). If crossover has been applied to the pair of parents, the children
vectors will generally differ from the parent vectors.
Mutation
The fifth step is mutation of the children. With some small probability pr,
which decreases over time, each element or coefficient of the two children’s
vectors is subjected to a mutation. The probability of each element is sub-
ject to mutation in generation G = 1, 2, . . . , G∗, given by the probability
pr = .15 + .33/G.
If mutation is to be performed on a vector element, we use the following
nonuniform mutation operation, due to Michalewicz (1996).
Begin by randomly drawing two real numbers r1 and r2 from the [0, 1]
interval and one random number s from a standard normal distribution.
The mutated coefficient Ωi,p is given by the following formula:
Ωi,p =



Ωi,p + s[1 −r(1−G/G∗)b
2
] if r1 > .5
Ωi,p −s[1 −r(1−G/G∗)b
2
] if r1 ≤.5



(3.29)
where G is the generation number, G∗is the maximum number of genera-
tions, and b is a parameter that governs the degree to which the mutation
operation is nonuniform. Usually we set b = 2. Note that the probability of
creating via mutation a new coefficient that is far from the current coeffi-
cient value diminishes as G →G∗, where G∗is the number of generations.
Thus, the mutation probability itself evolves through time.
The mutation operation is nonuniform since, over time, the algorithm is
sampling increasingly more intensively in a neighborhood of the existing
coefficient values. This more localized search allows for some fine tuning
of the coefficient vector in the later stages of the search, when the vectors
should be approaching close to a global optimum.
Election Tournament
The last step is the election tournament. Following the mutation opera-
tion, the four members of the “family” (P1, P2, C1, C2) engage in a fitness
tournament. The children are evaluated by the same fitness criterion used
to evaluate the parents. The two vectors with the best fitness, whether
parents or children, survive and pass to the next generation, while the two
with the worst fitness value are extinguished. This election operator is due
to Arifovic (1996). She notes that this election operator “endogenously con-
trols the realized rate of mutation” in the genetic search process [Arifovic
(1996), p. 525].

3.2 The Nonlinear Estimation Problem
75
We repeat the above process, with parents i and j returning to the
population pool for possible selection again, until the next generation is
populated by N ∗vectors.
Elitism
Once the next generation is populated, we can introduce elitism (or not).
Evaluate all the members of the new generation and the past generation
according to the fitness criterion. If the best member of the older genera-
tion dominated the best member of the new generation, then this member
displaces the worst member of the new generation and is thus eligible for
selection in the coming generation.
Convergence
One continues this process for G∗generations. Unfortunately, the literature
gives us little guidance about selecting a value for G∗. Since we evaluate
convergence by the fitness value of the best member of each generation, G∗
should be large enough so that we see no changes in the fitness values of
the best for several generations.
3.2.4
Evolutionary Genetic Algorithms
Just as the genetic algorithm is an evolutionary search process for finding
the best coefficient set Ωof p elements, the parameters of the genetic algo-
rithm, such as population size, probability of crossover, initial mutation
probability, use of elitism or not, can evolve themselves. As Michalewicz
and Fogel (2002) observe, “let’s admit that finding good parameter values
for an evolutionary algorithm is a poorly structured, ill-defined, complex
problem. But these are the kinds of problems for which evolutionary algo-
rithms are themselves quite adept” [Michalewicz and Fogel (2002), p. 281].
They suggest two ways to make a genetic algorithm evolutionary. One,
as we suggested with the mutation probability, is to use a feedback rule
from the state of the system which modifies a parameter during the search
process. Alternatively, we can incorporate the training parameters into the
solution by modifying Ωto include additional elements such as population
size, use of elitism, or crossover probability. These parameters thus become
subject to evolutionary search along with the solution set Ωitself.
3.2.5
Hybridization: Coupling Gradient-Descent,
Stochastic, and Genetic Search Methods
The gradient-descent methods are the most commonly used optimization
methods in nonlinear estimation. However, as previously noted, there is a

76
3. Estimation of a Network with Evolutionary Computation
strong danger of getting stuck in a local rather than a global minimum for
a vector w, or in a saddlepoint. Furthermore, if using a Newton algorithm,
the Hessian matrix may fail to invert, or become “near-singular,” leading
to imprecise or even absurd results for the coefficient vector of the neural
network. When there are a large number of parameters, the statistically
based simulated annealing search is a good alternative.
The genetic algorithm does not involve taking gradients or second deriva-
tives and is a global and evolutionary search process. One scores the
variously randomly generated coefficient vectors by the objective function,
which does not have to be smooth and continuous with respect to the
coefficient weights Ω. De Falco (1998) applied the genetic algorithm to
nonlinear neural network estimation and found that his results “proved the
effectiveness” of such algorithms for neural network estimation.
The main drawback of the genetic algorithm is that it is slow. For even
a reasonable size or dimension of the coefficient vector Ω, the various com-
binations and permutations of elements of Ωthat the genetic search may
find optimal or close to optimal at various generations may become very
large. This is another example of the well-known curse of dimensionality in
nonlinear optimization. Thus, one needs to let the genetic algorithm run
over a large number of generations — perhaps several hundred — to arrive
at results that resemble unique and global minimum points.
Since the gradient-descent and simulated annealing methods rely on an
arbitrary initialization of Ω, the best procedure for estimation may be
a hybrid approach. One may run the genetic algorithm for a reasonable
number of generations, say 100, and then use the final weight vector Ω
as the initialization vector for the gradient-descent or simulated annealing
minimization. One may repeat this process once more, with the final coeffi-
cient vector from the gradient-descent estimation entering a new population
pool for selection, breeding, and mutation. Even this hybrid procedure is
no sure thing, however.
Quagliarella and Vicini (1998) point out that hybridization may lead to
better solutions than those obtainable using the two methods individually.
These authors suggest the following alternative approaches:
1. The gradient-descent method is applied only to the best fit individual
after many generations.
2. The gradient descent method is applied to several individuals,
assigned by a selection operator.
3. The gradient descent method is applied to a number of individu-
als after the genetic algorithm has run many generations, but the
selection is purely random.

3.3 Repeated Estimation and Thick Models
77
Quagliarella and Vicini argue that it is not necessary to carry out the
gradient-descent optimization until convergence, if one is going to repeat
the process several times. The utility of the gradient-descent algorithm is
its ability to improve the “individuals it treats” so “its beneficial effects
can be obtained just performing a few iterations each time” [Quagliarella
and Vicini (1998), p. 307].
The genetic algorithm and the hybridization method fit into a broader
research agenda of evolutionary algorithms used not only for optimization
but also for classification, or explaining the pattern or markets or organi-
zations through time [see B¨ack (1996)]. This is the estimation method used
throughout this book. To level the playing field, we use this method not
only for the neural network models but also for the competing models that
require nonlinear estimation.
3.3
Repeated Estimation and Thick Models
The world of nonlinear estimation is a world full of traps, where we can
get caught in local minimal or saddle points very easily. Thus, repeated
estimation through hybrid genetic algorithm and gradient descent methods
may be the safest check for the robustness of results after one estimation
exercise with the hybrid approach.
For obtaining forecasts of particular variables, we must remember that
neural network estimation, coupled with the genetic algorithm, even with
the same network structure, never produces identical results, so that we
should not put too much faith in particular point forecasts. Granger and
Jeon (2002) have suggested “thick modeling” as a strategy for neural net-
works, particularly for forecasting. The idea is simple and straightforward.
We should repeatedly estimate a given data set with a neural network.
Since any neural network structure never gives identical results, we can use
the same network specification, or we can change the specification of the
network, or the scaling function, or even the estimation method, for differ-
ent iterations on the network. What Granger and Jeon suggest is that we
take a mean or trimmed mean of the forecasts of these alternative networks
for our overall network forecast. They call this forecast a thick model fore-
cast. We can also use this method for obtaining intervals for our forecasts
of the network.
Granger and Jeon have pointed out an intriguing result from their studies
of neural network performance, relative to linear models, for macroeco-
nomic time series. They found that individual neural network models did
not outperform simple linear models for most macro data, but thick mod-
els based on different neural networks uniformly outperformed the linear
models for forecasting accuracy.

78
3. Estimation of a Network with Evolutionary Computation
This approach is similar to bagging predictors in the broader artificial
intelligence and machine learning literature [see Breiman (1996)]. With
bagging, we can take a simple mean of various point forecasts coming
from an ensemble of models. For classification, we take a plurality vote
of the forecasts of multiple models. However, bagging is more extensive.
The alternative forecasts may come not from different models per se, but
from bootstrapping the initial training set. As we discuss in Section 4.2.8,
bootstrapping involves resampling the original training set with replace-
ment, and then taking repeated forecasts. Bagging is particularly useful if
the data set exhibits instability or structural change. Combining the fore-
casts based on different randomly sampled subsets of the training set may
give greater precision to the forecasting.
3.4
MATLAB Examples: Numerical
Optimization and Network Performance
3.4.1
Numerical Optimization
To make these concepts about optimization more concrete and clear, we can
take a simple problem, for which we can calculate an analytical solution.
Assume we wish to optimize the following function with respect to inputs
x and y:
z = .5x2 + .5y2 −4x −4y −1
(3.30)
The solution can readily be obtained analytically, with x∗= y∗= 4, for
the local minimum. A three-dimensional graph appears in Figure 3.2, with
the solution for x∗= y∗= 4, illustrated by the arrow on the (x, y) grid.
A simple MATLAB program for calculating the global genetic algorithm
search solution, the local simulated annealing solution, and the local quasi-
Newton based on the BFGS algorithm appear, is given by the following
sets of commands:
% Define simple function
z = inline(’.5 * x(1) ˆ2 + .5 * x(2) ˆ2 - 4 * x(1) - 4 * x(2) - 1’);
% Use random initialization
x0 = randn(1,2);
% Genetic algorithm parameters and execution-popsize, no. of
generations
maxgen = 100; popsize = 40;
xy genetic = gen7f(z, x0, popsize,maxgen);
% Simulated annealing procedure (define temperature)

3.4 MATLAB Examples: Numerical Optimization
79
−20
−15
−10
−5
0
0
2
4
6
8
0
1
2
3
4
5
6
7
8
z
x 
y
FIGURE 3.2. Sample optimization
TEMP = 500;
xy simanneal = simanneal(z, xy genetic, TEMP);
% BFGS Quasi-Newton Optimization Method
xy bfgs = fminunc(z, xy simanneal);
The solution for all three solution methods, the global genetic algorithm,
the local search (using the initial conditions based on the genetic algorithm)
and the quasi-Newton BFGS algorithm all yield results almost exactly equal
to 4 for both x and y. While this should not be surprising, it is a useful
exercise to check the accuracy of numerical methods by verifying how well
they produce the true results obtained by analytical solution.
Of course, we use numerical methods precisely because we cannot obtain
results analytically. Consider the following optimization problem, only
slightly different from the previous function:
z = .5 | x |1.5 +.5 | x |2.5 + · · ·
.5 | y |1.5 +.5 | y |2.5 −4x −4y −1
(3.31)


## Evaluation of Network Estimation

80
3. Estimation of a Network with Evolutionary Computation
Taking the partial derivatives with respect to x and y, we find the following
first-order conditions:
.5 · 1.5 | x |.5 +.5· | x |1.5 −4 = 0
(3.32)
.5 · 1.5 | y |.5 +.5· | y |1.5 −4 = 0
It should be clear that the optimal values x and y do not have closed-
form or exact analytical solutions. The following MATLAB code solves
this problem by the three algorithms:
% MATLAB Program for Minimization for Inline function z
z = inline(’.5 * abs(x(1)) ˆ1.5 + .5 *abs(x(1)) ˆ2.5 + ...
.5 * abs(x(2)) ˆ1.5 + .5 * abs(x(2))ˆ2.5 - 4 * x(1) - 4 * x(2) - 1’);
% Initial guess of solution based on random numbers
x0 = randn(1,2);
% Initialization for Genetic Algorithm
maxgen = 100; popsize(50);
% Solution for genetic algorithm
xy genetic = gen7f(z,x0, popsize, maxgen);
% Temperature for simulated annealing
TEMP = 500;
% Solution for simulated annealing
xy simanneal = simanneal(z, xy genetic, TEMP);
% BFGS Solution
xy bfgs = fminunc(z, xy simanneal);
Theoretically the solution values should be identical to each other. The
results we obtain by the MATLAB process for the hybrid method of using
the genetic algorithm, simulated annealing, and the quasi-Newton method,
give values of x = 1.7910746, y = 1.7910746.
3.4.2
Approximation with Polynomials and
Neural Networks
We can see how efficient neural networks are relative to linear and poly-
nomial approximations with a very simple example. We first generate a
standard normal random variable x of sample size 1000, and then generate
a variable y = [sin(x)]2 + e−x. We can then do a series of regressions with
polynomial approximators and a simple neural network with two neurons,
and compare the multiple correlation coefficients. We do this with the fol-
lowing set of MATLAB commands, which access the following functions for
the orthogonal polynomials: chedjudd.m, hermiejudd.m, legendrejudd.m,
and laguerrejudd.m, as well as the feedforward neural network program,
ffnet9.m.

3.4 MATLAB Examples: Numerical Optimization
81
for j = 1:1000,
% Matlab Program For Assessing Approximation
randn(’state’,j);
x1 = randn(1000,1);
y 1= sin(x1).ˆ2 + exp(-x1);
x = ((2 * x1) ./ (max(x1)-min(x1)))
- ((max(x1)+min(x1))/(max(x1)-min(x1)));
y = ((2 * y1) ./ (max(y1)-min(y1)))
- ((max(y1)+min(y1))/(max(y1)-min(y1)));
% Compute linear approximation
xols = [ones(1000,1) x];
bols = inv(xols’*xols)*xols’* y;
rsqols(j) = var(xols*bols)/var(y);
% Polynomial approximation
xp = [ones(1000,1) x x.ˆ2];
bp = inv(xp’*xp)*xp’*y;
rsqp(j) = var(xp*bp)/var(y);
% Tchebeycheff approximation
xt = [ones(1000,1) chebjudd(x,3)];
bt = inv(xt’*xt)*xt’*y;
rsqt(j) = var(xt * bt)/var(y);
% Hermite approximation
xh = [ones(1000,1) hermitejudd(x,3)];
bh = inv(xh’*xh)*xh’*y;
rsqh(j)= var(xh * bh)/var(y);
% Legendre approximation
xl = [ones(1000,1) legendrejudd(x,3)];
bl = inv(xl’*xl)*xl’*y;
rsql(j)= var(xl * bl)/var(y);
% Leguerre approximation
xlg = [ones(1000,1) laguerrejudd(x,3)];
blg = inv(xlg’*xlg)*xlg’*y;
rsqlg(j)= var(xlg * blg)/var(y);
% Neural Network Approximation
data = [y x];
position = 1; % column number of dependent variable
architecture = [1 2 0 0]; % feedforward network with one hidden
layer, with two neurons
geneticdummy = 1; % use genetic algorithm
maxgen =20; % number of generations for the genetic algorithm
percent = 1; % use 100 percent of data for all in-sample estimation
nlags = 0; % no lags for the variables
ndelay = 0; % no leads for the variables
niter = 20000; % number of iterations for quasi-Newton method
[sse, rsqnet01] = ffnet9(data, position, percent, nlags, ndelay,
architecture, ...

82
3. Estimation of a Network with Evolutionary Computation
0
100
200
300
400
500
600
700
800
900
1000
−4
−3
−2
−1
0
1
2
3
0
100
200
300
400
500
600
700
800
900
1000
0
5
10
15
20
25
x1=randn(1000,1)
y1=sin(x1)2 + exp(−x1)
FIGURE 3.3. Sample nonlinear realization
geneticdummy, maxgen, niter) ;
rsqnet0(j) = rsqnet01(2);
RSQ(j,:) = [rsqols(j) rsqp(j) rsqt(j) rsqh(j) rsql(j) rsqlg(j)
rsqnet0(j)]
end
One realization of the variables [y x] appears in Figure 3.3. While the
process for the variable x is a standard random realization, we see that the
process for y contains periodic jumps as well as periods of high volatility
followed by low volatility. Such properties are common in financial markets,
particularly in emerging market countries.
Table 3.3 gives the results for the goodness of fit or R2 statistics for
this base set of realizations, as well as the mean and standard deviations
of this measure for 1000 additional draws of the same sample length. We
compare second-order polynomials with a simple network with two neurons.
This table brings home several important results. First, there are definite
improvements in abandoning pure linear approximation. Second, the power
polynomial and the orthogonal polynomials give the same results. There is
no basis for preferring one over the other. Third, the neural network, a

3.5 Conclusion
83
TABLE 3.3. Goodness of Fit Tests of Approximation Methods
Approximation
R2: Base Run Mean R2 −1000 Draws
(std. deviation)
Linear
.49
.55 (.04)
Polynomial-Order 2
.85
.91 (.03)
TchebeycheffPolynomial-Order 2
.85
.91 (.03)
Hermite-Order 2
.85
.91 (.03)
Legendre-Order 2
.85
.91 (.03)
Laguerre-Order 2
.85
.91 (.03)
Neural Network: FF, 2 neurons, 1 layer .99
.99 (.005)
very simple neural network, is superior to the polynomial expansions, and
delivers a virtually perfect fit. Finally, the neural network is much more
precise, relative to the other methods, across a wide set of realizations.
3.5
Conclusion
This chapter shows how the introduction of nonlinearity makes the estima-
tion problem much more challenging and time-consuming than the case of
the standard linear model. But it also makes the estimation process much
more interesting. Given that we can converge to many different results or
parameter values, we have to find ways to differentiate the good from the
bad, or the better from a relatively worse set of estimates. Engineers have
been working with nonlinear optimization for many decades, and this chap-
ter shows how we can apply many of the existing evolutionary global or
hybrid search methods for neural network estimation. We need not resign
ourselves to the high risk of falling into locally optimal results.
3.5.1
MATLAB Program Notes
Optimization
software
is
quite
common.
The
MATLAB
function
fminunc.m, for unconstrained minimization, part of the Optimization Tool-
box, is the one used for the quasi-Newton gradient-based methods. It
has lots of options, such as the specification of tolerance criteria and the
maximum number of iterations. This function, like most software, is a min-
imization function. For maximizing a likelihood function, we minimize the
negative of the likelihood function.
The genetic algorithm used above is gen7f.m. The function requires four
inputs, including the name of the function being minimized. The function
being optimized, in turn, must have as its first output the criterion to be

84
3. Estimation of a Network with Evolutionary Computation
minimized, such as a sum of squared errors, or the negative of the likelihood
function.
The function simanneal.m requires the specification of the function, coef-
ficient matrix, and initial temperature. Finally, the orthogonal polynomial
operators, chedjudd.m, hermiejudd.m, legendrejudd.m, and laguerrejudd.m
are also available.
The scaling functions for transforming variables to ranges between [0,1]
or [−1,1] are in the MATLAB Neural Net Toolbox, premnmx.m.
The scaling function for the transformation suggested by Helge Petersohn
is given by hsquasher.m. The reverse transformation is given by helgeyx.m.
3.5.2
Suggested Exercises
As a follow-up to the exercises on minimization, we can do more com-
parisons of the accuracy of the simulated annealing and genetic algorithm
with benchmark true analytical solutions for a variety of functions. Simply
use the MATLAB Symbolic Toolbox funtool.m to find the true minimum
for a host of functions by setting the first derivative to zero. Then use
simanneal.m and gen7f.m to find the numerical approximate solutions.

4
Evaluation of Network Estimation
So far we have discussed the structure or architecture of a network, as
well as the ways of training or estimating the coefficients or weights of a
network. How do we interpret the results obtained from these networks,
relative to what we can obtain from a linear approximation?
There are three sets of criteria: in-sample criteria, out-of-sample criteria,
and common sense based on tests of significance and the plausibility of the
results.
4.1
In-Sample Criteria
When evaluating the regression, we first want to know how well a model
fits the actual data used to obtain the estimates of the coefficients. In
the neural network literature, this is known as supervised training. We
supervise the network, insofar as we evaluate it by how well it fits
actual data.
The first overall statistic is a measure of goodness of fit. The Hannan-
Quinn information is a method for handicapping this measure for compet-
ing models that have different numbers of parameters.
The other statistics relate to properties of the regression residuals. If
the model is indeed a good fit, and thus well specified, then there should
be nothing further to learn from the residuals. The residuals should sim-
ply represent “white noise,” or uncorrelated meaningless information — like
listening to a fan or air conditioner, which we readily and easily ignore.

86
4. Evaluation of Network Estimation
4.1.1
Goodness of Fit Measure
The most commonly used measure of overall goodness of fit of a model is
the multiple correlation coefficient, also known as the R-squared coefficient.
It is simply the ratio of the variance of the output predicted by the model
relative to the true or observed output:
R2 =
T
t=1(yt −yt)2
T
t=1(yt −yt)2
(4.1)
This value falls in the interval [0, 1] if there is a constant term in the model.
4.1.2
Hannan-Quinn Information Criterion
Of course, we can generate progressively higher values of the R2 statistic
by using a model with an increasingly larger number of parameters. One
way to modify the R2 statistic is to make use of the Hannan-Quinn (1979)
information criterion, which handicaps or “punishes” the performance of a
model for the number of parameters, k, it uses:
hqif =
&
ln
' T

t=1
(yt −yt)2
T
()
+ k{ln[ln(T)]}
T
(4.2)
The criterion is simply to choose the model with the lowest value. Note
that the hqif statistic punishes a given model by a factor of k{ln[ln(T)]}/T,
the logarithm of the logarithm of the number of observations, T, multi-
plied by the number of parameters, k, divided by T. The Akaike criterion
replaces the second term on the right-hand side of equation (4.2) with the
variable 2k/T, whereas the Schwartz criterion replaces the same term with
the value k[ln(T)]/T. We work with the Hannan-Quinn statistic rather
than the Akaike or Schwartz criteria, on the grounds that virtu stat in
media. The Hannan-Quinn statistic usually punishes a model with more
parameters more than the Akaike (1974) statistic, but not as severely as
the Schwartz (1978) statistic.1
4.1.3
Serial Independence: Ljung-Box and McLeod-Li Tests
If a model is well specified, the residuals should have no systematic pattern
in their first or second moments. Tests for serial independence and con-
stancy of variance, or homoskedasticity, are the first steps for evaluating
whether or not there is any meaningful information content in the residuals.
1The penalty factor attached to the number of parameters in a model is known as
the regularization term and represents a control or check over the effective complexity
of a model.

4.1 In-Sample Criteria
87
The most commonly used statistic tests for serial independence against
the alternative hypothesis of first-order autocorrelation is the well-known,
but elementary, Durbin-Watson (DW) test.
DW =
T
t=2[εt −εt−1]2
T
t=1 ε2
t
(4.3)
≈2 −2ρ1(ε)
(4.4)
where ρ1(ε) represents the first order autocorrelation coefficient.
In the absence of autocorrelation, each residual represents a surprise
which is unpredictable from the past data. The autocorrelation function is
given by the following formula, for different lag lengths m:
ρm(ε) =
T
t=m+1 εtεt−m
T
t=1 ε2
t
(4.5)
Ljung and Box (1978) put forward the following test statistic, known as
the Ljung-Box Q-statistic, for examining the joint significance of the first
M residual autocorrelations, with an asymptotic Chi-squared distribution
having M degrees of freedom:
Q(M) = (T)(T + 2)
M

m≡1
ρ2
m(ε)
(T −m)
(4.6)
∼χ2(M)
(4.7)
If a model does not pass the Ljung-Box Q test, there is usually a need
for correction. We can proceed in two ways. One is simply to add more lags
of the dependent variable as regressors or input variables. In many cases,
this takes care of serial dependence. An alternative is to respecify the error
structure itself as a moving average (MA process). In dynamic models,
in which we forecast the inflation rate over several quarters, we build in
by design a moving average process into the disturbance or innovation
terms. In this case, the inflation we forecast in January is the inflation
rate from next January to this January. In the next quarter, we forecast
the inflation rate from next April to this April. However, the forecast from
next April to this April will depend a great deal on the forecast error from
next January to this past January. Yet in forecasting exercises, often we
are most interested in forecasting over several periods rather than for one
period into the future, so purging the estimates of serial dependence is
extremely important before we do any assessment of the results. This is
especially true when we compare a linear model with the neural network

88
4. Evaluation of Network Estimation
alternative. The linear model first should be purged of serial dependence
either by the use of a liberal lag structure or by an MA specification for the
error term, before we can make any meaningful comparison with alternative
functional forms.
Adding more lags of the dependent variable is easy enough. The use
of the MA specification requires the following transformation of the error
term for a linear model with an MA component of order p:
yt =
K

k=0
βkxk,t + ϵt
(4.8a)
ϵt = ηt −ρ1ηt−1 −. . . ρpηt−p
(4.8b)
ηt˜N(0, σ2)
(4.8c)
Joint estimation of the coefficient set {βk} and {ρi} is done by maximum
likelihood estimation. Tsay (2002, p. 46) distinguishes between conditional
and exact likelihood estimation of the MA terms {ρi}. With conditional
estimation, for the first periods, {t = 1, . . . , t∗), with t∗≤p, we simply
assume that the error terms are zero. Exact estimation takes a more careful
approach. For period t = 1, the shocks ηt−i, i = 1, . . . , p, are set at zero.
However, for t = 2, ηt−1 is known, so the realized error is used, while the
other shocks ηt−i, i = 2, . . . , p, are set at zero. We follow a similar process
for the observations for t ≤p. For t > p, of course, we can use the realized
values of the errors. In many cases, as Tsay points out, the differences in
the coefficient values and resulting Q statistics from conditional and exact
likelihood estimation is very small.
Since the squared residuals of the model are used to compute standard
errors of estimates of the model, one can apply an extension of the Ljung-
Box Q statistic to test for homoskedasticity, or constancy of the variance, of
the residuals against an unspecified alternative. In a well-specified model,
the variance should be constant. This test is the McLeod and Li (1983), and
tests for autocorrelation of the squared residuals, with the same distribution
and degrees of freedom as the Q statistic.
McL(M) = (T)(T + 2)
M

m=1
ρ2
m(ε2)
(T −m)
(4.9)
∼χ2(M)
(4.10)
In many cases, we will find that correcting for the serial dependence in
the levels of the residuals is also a correction for serial dependence in the
squared residuals. Alternatively, a linear model may show a significant Q

4.1 In-Sample Criteria
89
TABLE 4.1. Engle-Ng Test of Symmetry of Residuals
Definition
Operation
Standardized errors
ϵτ = ϵτ/σϵτ
Squared standardized errors
{ϵ2
τ}
Positive indicators
ϵ +
τ = 1 if ϵτ > 0, 0 otherwise
Negative indicators
ϵ −
τ = 1 if ϵτ < 0, 0 otherwise
Positive valued errors
η+
τ = ϵτ ·ϵ +
τ
Negative valued errors
η−
τ = ϵτ ·ϵ −
τ
Regression
yτ=ϵ 2
τ , xτ = [1 ϵ −
τ η+
τ η−
τ ]
Engle-Ng LM statistic
LM = (T −1) · R2
Distribution
LM ∼χ2(3)
statistic for the McLeod-Li test whereas a neural network alternative may
not. The point is that for making a fair comparison between a linear and
network model, the most important issue is to correct the linear model
for serial dependence in the raw, rather than the squared, value of the
residuals.
4.1.4
Symmetry
In addition to serial independence and constancy of variance, symmetry
of the residuals is also a desired property if they indeed represent purely
random shocks. Symmetry is an important issue, of course, if the model is
going to be used for simulation with symmetric random shocks. However,
violation of the symmetry assumption is not as serious as violation of serial
independence or constancy of variance.
The test for symmetry of residuals proposed by Engle and Ng (1993) is
shown in Table 4.1.
4.1.5
Normality
Besides having properties of serial independence, constancy of variance,
and symmetry, residuals are usually assumed to come from a Gaussian or
normal distribution. One well-known test, the Jarque-Bera statistic, starts
from the assumption that a normal distribution has zero skewness and a
kurtosis of 3.
Given the residual vector ϵ, the Jarque-Bera (1980) statistic is given by
the following formula and distribution:
JB(ϵ ) = T −k
6
*
SK(ϵ )2 + .25(KR(ϵ ) −3)2+
(4.11)
∼χ2(2)

90
4. Evaluation of Network Estimation
where SK(ϵ ) and KR(ϵ ), for skewness and kurtosis, are defined as follows:
SK(ϵ ) = 1
T
T

t=1
'
ϵi −ϵ
σϵ
(3
(4.12)
KR(ϵ ) = 1
T
T

t=1
'
ϵi −ϵ
σϵ
(4
(4.13)
while ϵ and σϵ represent the estimated mean and standard deviation of the
residual vector ϵ.
How important is the normality assumption, or how serious is a violation
of the normality assumption? The answer depends on the purpose of the
estimation. If the estimated model is going to be used for simulating models
subject to random normal disturbances, then it would be good to have
normal randomly distributed residuals in the estimated model.
4.1.6
Neural Network Test for Neglected Nonlinearity:
Lee-White-Granger Test
Lee, White, and Granger (1992) proposed the use of artificially generated
neural networks for testing for the presence of neglected nonlinearity in
the regression residuals of any estimated model. The test works with the
regressions residuals and the inputs of the model, and seeks to find out if
any of the residuals can be explained by nonlinear transformations of the
input variables. If they can be explained, there is neglected nonlinearity.
Since the precise form of the nonlinearity is unspecified, Lee, White,
and Granger propose a neural network approach, but they leave aside
the time-consuming estimation process for the neural network. Instead,
the coefficients or weights linking the inputs to the neurons are generated
randomly.
The Lee, White, Granger (L-W-G) test is rather straightforward, and
proceeds in six steps:
1. From the initial model, obtain the residuals and the input variables.
2. Generate a set of neuron regressors from the inputs, with randomly
generated weights for the input variables.
3. Regress the residuals on the neurons,
and obtain the multiple
correlation coefficients.
4. Repeat this process 1000 times.

4.1 In-Sample Criteria
91
TABLE 4.2. Lee-White-Granger Test of Neglected Nonlinearity
Definition
Operation
Obtain residuals and inputs
e, x
Randomly generate P sets of coefficients for x
βi
Generate P neurons n1, n2, . . . , np
np =
1
1+e−βpx
Regress e on the P neurons
e = b1n1+, . . . , bpnp
Obtain multiple correlation coefficient
R2
1
Repeat process 1000 times
R2
1, R2
2, . . . , R2
1000
Assess significance of coefficients
F(R2
1), . . . , F(R2
1000)
Count significant F statistics
Ii = 1 ⇔F(R2
1) > F ∗
Decision: Reject if more than 5% significant
5. Assess the significance of the multiple correlation coefficients by F
statistics.
6. If these coefficients are significant more than 5% of the time, there is
a case for neglected nonlinearity.
For convenience, these steps are summarized in Table 4.2.
This test is similar to the White (1980) test for heteroskedasticity. This
test is a regression of the squared residuals on a polynomial expansion of
the regressors or input variables. In the White test, we specify the power
of the polynomial, with the option to include or exclude the cross terms in
the polynomial expansion of the input variables.
The intuition behind the L-W-G test is that if there is any neglected
nonlinearity in the residuals, some combination of neural network trans-
formations of the inputs should be able to explain or detect it by
approximating it well, since neural networks are adept at approximating
unknown nonlinear functions. Since linear regressions of the residuals are
done on the randomly generated neurons, the test proceeds very rapidly. If,
after a large number of repeated trials with randomly generated neurons,
no significant relations between the neurons and the residuals emerge, one
can be confident that there are no neglected nonlinearities.
4.1.7
Brock-Deckert-Scheinkman Test for Nonlinear
Patterns
Brock, Deckert, and Scheinkman (1987), further elaborated in Brock,
Deckert, Scheinkman, and LeBaron (1996), propose a test for detecting
nonlinear patterns in time series. Following Kocenda (2001), the null
hypothesis is that the data are independently and identically distributed

92
4. Evaluation of Network Estimation
TABLE 4.3. BDS Test of IID Process
Definition
Operation
Form m-dimensional
vector, xm
t
xm
t = xt, . . . , xt+m, t = 1, . . . , Tm−1, Tm−1 = T −m
Form m-dimensional
vector, xm
s
xm
s = xs, . . . , xs+m, s = t + 1, . . . , Tm,Tm = T −m + 1
Form indicator function
Iε(xm
t , xm
s ) =
max
i=0,1,...,m−1 | xt+1 −xs+i |< ε
Calculate correlation
integral
Cm,T (ε) = 2 	Tm−1
t=1
	Tm
s=t+1
Iε(xm
t ,xm
s )
Tm(Tm−1−1)
Calculate correlation
integral
C1,T (ε) = 2 	T −1
t=1
	T
s=t+1
Iε(x1
t ,x1
s)
T (T −1)
Form Numerator
√
T [Cm,T (ε) −C1,T (ε)m]
Sample Standard Dev.
of Numerator
σm,T (ε)
Form BDS Statistic
BDSm,T (ε) =
√
T[Cm,T (ε)−C1,T (ε)m]
σm,T (ε)
Distribution
BDSm,T (ε) ∼N(0, 1)
(iid) processes. This test, known as the BDS test, is unique in its ability to
detect nonlinearities independently of linear dependencies in the data.
The test rests on the correlation integral, developed to distinguish
between chaotic deterministic systems and stochastic systems. The pro-
cedure consists of taking a series of m-dimensional vectors from a time
series, at time t = 1, 2, . . . , T −m, where T is the length of the time series.
Beginning at time t = 1 and s = t + 1, the pairs (xm
t , xm
s ) are evaluated by
an indicator function to see if their maximum distance, over the horizon
m, is less than a specified value ε. The correlation integral measures the
fraction of pairs that lie within the tolerance distance for the embedding
dimension m.
The BDS statistic tests the difference between the correlation integral
for embedding dimension m, and the integral for embedding dimension 1,
raised to the power m. Under the null hypothesis of an iid process, the
BDS statistic is distributed as a standard normal variate.
Table 4.3 summarizes the steps for the BDS test.
Kocenda (2002) points out that the BDS statistic suffers from one major
drawback: the embedding parameter m and the proximity parameter ε
must be chosen arbitrarily. However, Hsieh and LeBaron (1988a, b, c)
recommend choosing ε to be between .5 and 1.5 standard deviations of the
data. The choice of m depends on the lag we wish to examine for serial
dependence. With monthly data, for example, a likely candidate for m
would be 12.

4.1 In-Sample Criteria
93
4.1.8
Summary of In-Sample Criteria
The quest for a high measure of goodness of fit with a small number of
parameters with regression residuals that represent random white noise is
a difficult challenge. All of these statistics represent tests of specification
error, in the sense that the presence of meaningful information in the resid-
uals indicates that key variables are omitted, or that the underlying true
functional form is not well approximated by the functional form of the
model.
4.1.9
MATLAB Example
To give the preceding regression diagnostics clearer focus, the following
MATLAB code randomly generates a time series y = sin(x)2 + exp(−x) as
a nonlinear function of a random variable x, then uses a linear regression
model to approximate the model, and computes the in-sample diagnostic
statistics. This program makes use of functions ols1.m, wnnest1.m, and
bds.m, available on the webpage of the author.
% Create random regressors, constant term,
% and dependent variable
for i = 1:1000,
randn(’state’,i);
xxx = randn(1000,1);
x1 = ones(1000,1);
x = [x1 xxx];
y = sin(xxx).ˆ2 + exp(-xxx);
% Compute ols coefficients and diagnostics
[beta, tstat, rsq, dw, jbstat, engle, ...
lbox, mcli] = ols1(x,y);
% Obtain residuals
residuals = y - x * beta;
sse = sum(residuals .ˆ2);
nn = length(residuals);
kk = length(beta);
% Hannan-Quinn Information Criterion
k = 2;
hqif = log(sse/nn) + k * log(log(nn))/nn;
% Set up Lee-White-Granger test
neurons = 5;
nruns = 1000;
% Nonlinearity Test
[nntest, nnsum] = wnntest1(residuals, x, neurons, nruns);
% BDS Nonlinearity Test
[W, SIG] = bds1(residuals);
RSQ(i) = rsq;
DW(i) = dw;

94
4. Evaluation of Network Estimation
TABLE 4.4. Specification Tests
Test Statistic
Mean
% of Significant Tests
JB-Marginal significance
0
100
EN-Marginal significance
.56
3.7
LB-Marginal significance
.51
4.5
McL-Marginal Significance
.77
2.1
LWG-No. of Significant Regressions
999
99
BDS-Marginal Significance
.47
6.6
JBSIG(i) = jbstat(2);
ENGLE(i) = engle(2);
LBOX(i) = lbox(2);
MCLI(i) = mcli(2);
NNSUM(i) = nnsum;
BDSSIG(i) = SIG;
HQIF(i) = hqif;
SSE(i) = sse;
end
The model is nonlinear, and estimation with linear least squares clearly
is a misspecification. Since the diagnostic tests are essentially various types
of tests for specification error, we examine in Table 4.4 which tests pick up
the specification error in this example. We generate data series of sample
length 1000 for 1000 different realizations or experiments, estimate the
model, and conduct the specification tests.
Table 4.4 shows that the JB and the LWG are the most reliable for
detecting misspecification for this example. The others do not do nearly as
well: the BDS tests for nonlinearity are significant 6.6% of the time, and
the LB, McL, and EN tests are not even significant for 5% of the total
experiments. In fairness, the LB and McL tests are aimed at serial cor-
relation, which is not a problem for these simulations, so we would not
expect these tests to be significant. Table 4.4 does show, very starkly, that
the Lee-White-Granger test, making use of neural network regressions to
detect the presence of neglected nonlinearity in the regression residuals, is
highly accurate. The Lee-White-Granger test picks up neglected nonlinear-
ity in 99% of the realizations or experiments, while the BDS test does so
in 6.6% of the experiments.
4.2
Out-of-Sample Criteria
The real acid test for the performance of alternative models is its out-
of-sample forecasting performance. Out-of-sample tests evaluate how well

4.2 Out-of-Sample Criteria
95
competing models generalize outside of the data set used for estimation.
Good in-sample performance, judged by the R2 or the Hannan-Quinn
statistics, may simply mean that a model is picking up peculiar or idiosyn-
cratic aspects of a particular sample or over-fitting the sample, but the
model may not fit the wider population very well.
To evaluate the out-of-sample performance of a model, we begin by divid-
ing the data into an in-sample estimation or training set for obtaining the
coefficients, and an out-of-sample or test set. With the latter set of data,
we plug in the coefficients obtained from the training set to see how well
they perform with the new data set, which had no role in calculating of
the coefficient estimates.
In most studies with neural networks, a relatively high percentage of the
data, 25% or more, is set aside or withheld from the estimation for use in
the test set. For cross-section studies with large numbers of observations,
withholding 25% of the data is reasonable. In time-series forecasting, how-
ever, the main interest is in forecasting horizons of several quarters or one
to two years at the maximum. It is not usually necessary to withhold such
a large proportion of the data from the estimation set.
For time-series forecasting, the out-of-sample performance can be cal-
culated in two ways. One is simply to withhold a given percentage of
the data for the test, usually the last two years of observations. We esti-
mate the parameters with the training set, use the estimated coefficients
with the withheld data, and calculate the set of prediction errors coming
from the withheld data. The errors come from one set of coefficients, based
on the fixed training set and one fixed test set of several observations.
4.2.1
Recursive Methodology
An alternative to a once-and-for-all division of the data into training and
test sets is the recursive methodology, which Stock (2000) describes as a
series of “simulated real time forecasting experiments.” It is also known as
estimation with a “moving” or “sliding” window. In this case, period-by-
period forecasts of variable y at horizon h, yt+h, are conditional only on
data up to time t. Thus, with a given data set, we may use the first half of
the data, based on observations {1, . . . , t∗} for the initial estimation, and
obtain an initial forecast yt∗+h. Then we re-estimate the model based on
observations {1, . . . , t∗+ 1}, and obtain a second forecast error, yt∗+1+h.
The process continues until the sample is covered. Needless to say, as Stock
(2000) points out, the many re-estimations of the model required by this
approach can be computationally demanding for nonlinear models. We call
this type of recursive estimation an expanding window. The sample size, of
course, becomes larger as we move forward in time.
An alternative to the expanding window is the moving window. In this
case, for the first forecast we estimate with data observations {1, . . . , t∗},

96
4. Evaluation of Network Estimation
and obtain the forecast yt∗+h at horizon h. We then incorporate the obser-
vation at t∗+ 1, and re-estimate the coefficients with data observations
{2, . . . , t∗+ 1}, and not {1, . . . , t∗+ 1}. The advantage of the moving win-
dow is that as data become more distant in the past, we assume that they
have little or no predictive relevance, so they are removed from the sample.
The recursive methodology, as opposed to the once-and-for-all split of
the sample, is clearly biased toward a linear model, since there is only one
forecast error for each training set. The linear regression coefficients adjust
to and approximate, step-by-step in a recursive manner, the underlying
changes in the slope of the model, as they forecast only one step ahead.
A nonlinear neural network model, in this case, is challenged to perform
much better. The appeal of the recursive linear estimation approach is
that it reflects how econometricians do in fact operate. The coefficients
of linear models are always being updated as new information becomes
available, if for no other reason, than that linear estimates are very easy
to obtain. It is hard to conceive of any organization using information a
few years old to estimate coefficients for making decisions in the present.
For this reason, evaluating the relative performance of neural nets against
recursively estimated linear models is perhaps the more realistic match-up.
4.2.2
Root Mean Squared Error Statistic
The most commonly used statistic for evaluating out-of-sample fit is the
root mean squared error (rmsq) statistic:
rmsq =
τ ∗
τ=1(yτ −yτ)2
τ ∗
(4.14)
where τ ∗is the number of observations in the test set and {yτ} are the
predicted values of {yτ}. The out-of-sample predictions are calculated by
using the input variables in the test set {xτ} with the parameters estimated
with the in-sample data.
4.2.3
Diebold-Mariano Test for Out-of-Sample Errors
We should select the model with the lowest root mean squared error statis-
tic. However, how can we determine if the out-of-sample fit of one model is
significantly better or worse than the out-of-sample fit of another model?
One simple approach is to keep track of the out-of-sample points in which
model A beats model B.
A more detailed solution to this problem comes from the work of Diebold
and Mariano (1995). The procedure appears in Table 4.5.

4.2 Out-of-Sample Criteria
97
TABLE 4.5. Diebold-Mariano Procedure
Definition
Operation
Errors
{ϵτ}, {ητ}
Absolute differences
zτ = |ητ| −|ϵτ|
Mean
z =
τ∗
τ=1 zτ
τ∗
Covariogram
c = [Cov(zτ, zτ−p, ),Cov(zτ, zτ, ),Cov(zτ, zτ+p, )]
Mean
c = 	 c/(p + 1)
DM statistic
DM = z
c ∼N(0, 1), H0 : E(zτ) = 0
As shown above, we first obtain the out-of-sample prediction errors of
the benchmark model, given by {ϵτ}, as well as those of the competing
model, {ητ}.
Next, we compute the absolute values of these prediction errors, as well
as the mean of the differences of these absolute values, zτ. We then compute
the covariogram for lag/lead length p, for the vector of the differences of
the absolute values of the predictive errors. The parameter p < τ ∗is the
length of the out-of-sample prediction errors.
In the final step, we form a ratio of the means of the differences over
the covariogram. The DM statistic is distributed as a standard normal
distribution under the null hypothesis of no significant differences in the
predictive accuracy of the two models. Thus, if the competing model’s
predictive errors are significantly lower than those of the benchmark model,
the DM statistic should be below the critical value of −1.69 at the 5%
critical level.
4.2.4
Harvey, Leybourne, and Newbold Size Correction of
Diebold-Mariano Test
Harvey, Leybourne, and Newbold (1997) suggest a size correction to the
DM statistic, which also allows “fat tails” in the distribution of the forecast
errors. We call this modified Diebold-Mariano statistic the MDM statistic.
It is obtained by multiplying the DM statistic by the correction factor CF,
and it is asymptotically distributed as a Student’s t with τ ∗−1 degrees of
freedom. The following equation system summarizes the calculation of the
MDM test, with the parameter p representing the lag/lead length of the
covariogram, and τ ∗the length of the out-of-sample forecast set:
CF = τ ∗+ 1 −2p + p(1 −p)/τ ∗
τ ∗
(4.15)
MDM = CF · DM ∼tτ ∗−1(0, 1)
(4.16)

98
4. Evaluation of Network Estimation
4.2.5
Out-of-Sample Comparison with Nested Models
Clark and McCracken (2001), Corradi and Swanson (2002), and Clark
and West (2004) have proposed tests for comparing out-of-sample accuracy
for two models, when the competing models are nested. Such a test is
especially relevant if we wish to compare a feedforward network with jump
connections (containing linear as well as logsigmoid neurons) with a simple
restricted linear alternative, given by the following equations:
Restricted Model: yt =
K

k=1
αkxk,t + ϵt
(4.17)
Alternative Model: yt =
K

k=1
βkxk,t +
J

j=1
γjNj,t + ηt
(4.18)
Nj,t =
1
1 + exp[−(K
k=1 δj,kxk,t)]
(4.19)
where the first restricted equation is simply a linear function of K param-
eters, while the second unrestricted network is a nonlinear function with
K+JK parameters. Under the null hypothesis of equal predictive ability of
the two models, the difference between the squared prediction errors should
be zero. However, Todd and West point out that under the null hypothesis,
the mean squared prediction error of the null model will often or likely be
smaller than that of the alternative model [Clark and West (2004), p. 6].
The reason is that the mean squared error of the alternative model will be
pushed up by noise terms reflecting “spurious small sample fit” [Clark and
West (2004), p. 8]. The larger the number of parameters in the alternative
model, the larger the difference will be.
Clark and West suggest a procedure for correcting the bias in out-of-
sample tests. Their paper does not have estimated parameters for the
restricted or null model — they compare a more extensive model against
a simple random walk model for the exchange rate. However, their proce-
dure can be used for comparing a pure linear restricted model against a
combined linear and nonlinear alternative model as above. The procedure
is a correction to the mean squared prediction error of the unrestricted
model by an adjustment factor ψADJ, defined in the following way, for the
case of the neural network model.
The mean squared prediction errors of the two models are given by the
following equations, for forecasts τ = 1, . . . , T ∗:
σ2
RES =(T ∗)−1
T ∗

τ=1
&
yτ −
K

k=1
βkxk,τ
)2
(4.20)

4.2 Out-of-Sample Criteria
99
σ2
NET =(T ∗)−1
T ∗

τ=1

yτ −
K

k=1
αkxk,τ −
J

j=1
γj
'
1
1+exp[−(K
k=1 δj,kxk,τ)]
(

2
(4.21)
The null hypothesis of equal predictive performance is obtained by
comparing σ2
NET with the following adjusted mean squared error statistic:
σ2
ADJ = σ2
NET −ψADJ
(4.22)
The test statistic under the null hypothesis of equal predictive perfor-
mance is given by the following expression:
f = σ2
RES −σ2
ADJ
(4.23)
The approximate distribution of this statistic, multiplied by the square
root of the size of the out-of-sample set, is given by normal distribution
with mean 0 and variance V :
(T ∗).5 f˜ φ(0, V)
(4.24)
The variance is computed in the following way:
V = 4 · (T ∗)−1
T ∗

τ=1


'
yτ −
K

k=1
βkxk,τ
( 

J

j=1
γjNj,τ




2
(4.25)
Clark and West point out that this test is one-sided: if the restrictions
of the linear model were not true, the forecasts from the network model
would be superior to those of the linear model.
4.2.6
Success Ratio for Sign Predictions: Directional
Accuracy
Out-of-sample forecasts can also be evaluated by comparing the signs of
the out-of-sample predictions with the true sample. In financial time series,
this is particularly important if one is more concerned about the sign of
stock return predictions rather than the exact value of the returns. After
all, if the out-of-sample forecasts are correct and positive, this would be a
signal to buy, and if they are negative, a signal to sell. Thus, the correct
sign forecast reflects the market timing ability of the forecasting model.
Pesaran and Timmermann (1992) developed the following test of direc-
tional accuracy (DA) for out-of-sample predictions, given in Table 4.6.

100
4. Evaluation of Network Estimation
TABLE 4.6. Pesaran-Timmerman Directional Accuracy (DA) Test
Definition
Operation
Calculate out of sample predictions, m
periods
yn+j,j = 1, . . . , m
Compute indicator for correct sign
Ij = 1 if yn+j · yn+j > 0, 0 otherwise
Compute success ratio (SR)
SR =
1
m
	m
j=1 Ij
Compute indicator for true values
Itrue
j
= 1 if yn+j > 0, 0 otherwise
Compute indicator for predicted values
Ipred
j
= 1 if yn+j > 0, 0 otherwise
Compute means P, P
P =
1
m
	m
j=1 Itrue
j
, P =
1
m
	m
j=1 Ipred
j
Compute success ratio under
independence (SRI)
SRI = P · P −(1 −P) · (1 −P)
Compute variance for SRI
var(SRI) =
1
m(2 P −1)2P(1 −P)
+(2P −1)2 P(1 −P)
+ 4
mP · P(1 −P)(1 −P)]
Compute variance for SR
var(SR) =
1
mSRI(1 −SRI)
Compute DA statistic
DA =
SR−SRI
√
var(SR)−var(SRI)
a∼N(0, 1)
The DA statistic is approximately distributed as standard normal, under
the null hypothesis that the signs of the forecasts and the signs of the actual
variables are independent.
4.2.7
Predictive Stochastic Complexity
In choosing the best neural network specification, one has to make decisions
regarding lag length for each of the regressors, as well as the type of network
to be used, the number of hidden layers, and the number of networks in each
hidden layer. One can, of course, make a quick decision on the lag length
by using the linear model as the benchmark. However, if the underlying
true model is a nonlinear one being approximated by the neural network,
then the linear model should not serve this function.
Kuan and Liu (1995) introduced the concept of predictive stochastic com-
plexity (PSC), originally put forward by Rissanen (1986a, b), for selecting
both the lag and neural network architecture or specification. The basic
approach is to compute the average squared honest or out-of-sample pre-
diction errors and choose the network that gives the smallest PSC within a
class of models. If two models have the same PSC, the simpler one should
be selected.
Kuan and Liu applied this approach to exchange rate forecasting. They
specified families of different feedforward and recurrent networks, with
differing lags and numbers of hidden units. They make use of random

4.2 Out-of-Sample Criteria
101
specification for the starting parameters for each of the networks and choose
the one with the lowest out-of-sample error as the starting value. Then
they use a Newton algorithm and compute the resulting PSC values. They
conclude that nonlinearity in exchange rates may be exploited by neural
networks to “improve both point and sign forecasts” [Kuan and Liu (1995),
p. 361].
4.2.8
Cross-Validation and the .632 Bootstrapping Method
Unfortunately, many times economists have to work with time series lacking
a sufficient number of observations for both a good in-sample estima-
tion and an out-of-sample forecast test based on a reasonable number of
observations.
The reason for doing out-of-sample tests, of course, is to see how well a
model generalizes beyond the original training or estimation set or historical
sample for a reasonable number of observations. As mentioned above, the
recursive methodology allows only one out-of-sample error for each training
set. The point of any out-of-sample test is to estimate the in-sample bias
of the estimates, with a sufficiently ample set of data. By in-sample bias
we mean the extent to which a model overfits the in-sample data and lacks
ability to forecast well out-of-sample.
One simple approach is to divide the initial data set into k subsets of
approximately equal size. We then estimate the model k times, each time
leaving out one of the subsets. We can compute a series of mean squared
error measures on the basis of forecasting with the omitted subset. For k
equal to the size of the initial data set, this method is called leave out one.
This method is discussed in Stone (1977), Djkstra (1988), and Shao (1995).
LeBaron (1998) proposes a more extensive bootstrap test called the
0.632 bootstrap, originally due to Efron (1979) and described in Efron and
Tibshirani (1993). The basic idea, according to LeBaron, is to estimate the
original in-sample bias by repeatedly drawing new samples from the orig-
inal sample, with replacement, and using the new samples as estimation
sets, with the remaining data from the original sample not appearing in
the new estimation sets, as clean test or out-of-sample data sets. In each of
the repeated draws, of course, we keep track of which data points are in the
estimation set and which are in the out-of-sample data set. Depending on
the draws in each repetition, the size of the out-of-sample data set will vary.
In contrast to cross-validation, then, the 0.632 bootstrap test allows a ran-
domized selection of the subsamples for testing the forecasting performance
of the model.
The 0.632 bootstrap procedure appears in Table 4.7.2
2LeBaron (1998) notes that the weighting 0.632 comes from the probability that a
given point is actually in a given bootstrap draw, 1 −[1 −( 1
n)]n ≈1 −e−1 = 0.632.

102
4. Evaluation of Network Estimation
TABLE 4.7. 0.632 Bootstrap Test for In-Sample Bias
Obtain mean squared error from full
data set
MSSE0 = 1
n
	n
i=1 [yi −yi]2
Draw a sample of length n with
replacement
z1
Estimate coefficients of model
Ω1
Obtain omitted data from full
data set
z
Forecast out-of-sample with
coefficients Ω1
z1 = z1(Ω1)
Calculate mean squared error for
out-of-sample data
MSSE1 =
1
n1
	n1
i=1

z1 −z1
2
Repeat experiment B times
Calculate average mean squared error
for B boostraps
MSSE =
1
B
	B
b=1 MSSEb
Calculate bias adjustment
ϖ(0.632) = 0.632

MSSE0 −MSSE

Calculate adjusted error estimate
MSSE(0.632) = 0.368 · MSSE0
+0.632 · MSSE
In Table 4.7, MSSE is a measure of the average mean out-of-sample
squared forecast errors. The point of doing this exercise, of course, is to
compare the forecasting performance of two or more competing models,
to compare MSSE(0.632)
i
for models i = 1, . . . , m. Unfortunately, there
is no well-defined distribution of the MSSE(0.632), so we cannot test if
MSSE(0.632)
i
from model i is significantly different from MSSE(0.632)
j
of
model j. Like the Hannan-Quinn information criterion, we can use this for
ranking different models or forecasting procedures.
4.2.9
Data Requirements: How Large for Predictive
Accuracy?
Many researchers shy away from neural network approaches because they
are under the impression that large amounts of data are required to obtain
accurate predictions. Yes, it is true that there are more parameters to
estimate in a neural network than in a linear model. The more com-
plex the network, the more neurons there are. With more neurons, there
are more parameters, and without a relatively large data set, degrees
of freedom diminish rapidly in progressively more complex networks.

4.2 Out-of-Sample Criteria
103
In general, statisticians and econometricians work under the assump-
tion that the more observations the better, since we obtain more precise
and accurate estimates and predictions. Thus, combining complex esti-
mation methods such as the genetic algorithm with very large data
sets makes neural network approaches very costly, if not extravagant,
endeavors. By costly, we mean that we have to wait a long time to get
results, relative to linear models, even if we work with very fast hard-
ware and optimized or fast software codes. One econometrician recently
confided to me that she stays with linear methods because “life is too
short.”
Yes, we do want a relatively large data set for sufficient degrees of free-
dom. However, in financial markets, working with time series, too much
data can actually be a problem. If we go back too far, we risk using data
that does not represent very well the current structure of the market. Data
from the 1970s, for example, may not be very relevant for assessing foreign
exchange or equity markets, since the market conditions of the last decade
have changed drastically with the advent of online trading and information
technology. Despite the fact that financial markets operate with long mem-
ory, financial market participants are quick to discount information from
the irrelevant past. We thus face the issue of data quality when quantity
is abundant.
Walczak (2001) has examined the issue of length of the training set or
in-sample data size for producing accurate forecasts in financial markets.
He found that for most exchange-rate predictions (on a daily basis), a
maximum of two years produces the “best neural network forecasting model
performance” [Walczak (2001), p. 205]. Walczak calls the use of data closer
in time to the data that are to be forecast the times-series recency effect.
Use of more recent data can improve forecast accuracy by 5% or more while
reducing the training and development time for neural network models
[Walczak (2001), p. 205].
Walczak measures the accuracy of his forecasts not by the root mean
squared error criterion but by percentage of correct out-of-sample direc-
tion of change forecasts, or directional accuracy, taken up by Pesaran and
Timmerman (1992). As in most studies, he found that single-hidden-layer
neural networks consistently outperformed two-layer neural networks, and
that they are capable of reaching the 60% accuracy threshold [Walczak
(2001), p. 211].
Of course, in macro time series, when we are forecasting inflation or pro-
ductivity growth, we do not have daily data available. With monthly data,
ample degrees of freedom, approaching in sample length the equivalent of
two years of daily data, would require at least several decades. But the
message of Walczak is a good warning that too much data may be too
much of a good thing.

104
4. Evaluation of Network Estimation
4.3
Interpretive Criteria and Significance of
Results
In the final analysis, the most important criteria rest on the questions posed
by the investigators. Do the results of a neural network lend themselves to
interpretations that make sense in terms of economic theory and give us
insights into policy or better information for decision making? The goal
of computational and empirical work is insight as much as precision and
accuracy. Of course, how we interpret a model depends on why we are
estimating the model. If the only goal is to obtain better, more accurate
forecasts, and nothing else, then there is no hermeneutics issue.
We can interpret a model in a number of ways. One way is simply to sim-
ulate a model with the given initial conditions, add in some small changes
to one of the variables, and see how differently the model behaves. This is
akin to impulse-response analysis in linear models. In this approach, we set
all the exogenous shocks at zero, set one of them at a value equal to one
standard deviation for one period, and let the model run for a number of
periods. If the model gives sensible and stable results, we can have greater
confidence in the model’s credibility.
We may also be interested in knowing if some or any of the variables used
in the model are really important or statistically significant. For example,
does unemployment help explain future inflation? We can simply estimate a
network with unemployment and then prune the network, taking unemploy-
ment out, estimate the network again, and see if the overall explanatory
power or predictive performance of the network deteriorates after elimi-
nating unemployment. We thus test the significance of unemployment as
an explanatory variable in the network with a likelihood ratio statistic.
However, this method is often cumbersome, since the network may con-
verge at different local optima before and after pruning. We often get the
perverse result that a network actually improves after a key variable has
been omitted.
Another way to interpret an estimated model is to examine a few of
the partial derivatives or the effects of certain exogenous variables on the
dependent variable. For example, is unemployment more important for
explaining future inflation than the interest rate? Does government spend-
ing have a positive effect on inflation? With these partial derivatives, we
can assess, qualitatively and quantitatively, the relative strength of how
exogenous variables affect the dependent variable.
Again, it is important to proceed cautiously and critically. An estimated
model, usually an overfitted neural network, for example, may produce
partial derivatives showing that an increase in firm profits actually increases
the risk of bankruptcy! In complex nonlinear estimation such an absurd
possibility happens when the model is overfitted with too many parameters.

4.3 Interpretive Criteria and Significance of Results
105
The estimation process should be redone, by pruning the model to a simpler
network, to find out if such a result is simply a result of too few or too
many parameters in the approximation, and thus due to misspecification.
Absurd results can also come from the lack of convergence, or conver-
gence to a local optimum or saddle point, when quasi-Newton gradient-
descent methods are used for estimation.
In assessing the common sense of a neural network model it is important
to remember that the estimated coefficients or the weights of the network,
which encompass the coefficients linking the inputs to the neurons and
the coefficients linking the neurons to the output, do not represent partial
derivatives of the output y with respect to each of the input variables. As
was mentioned, the neural network estimation is nonparametric, in the
sense that the coefficients do not have a ready interpretation as behavioral
parameters. In the case of the pure linear model, of course, the coefficients
and the partial derivatives are identical.
Thus, to find out if an estimated network makes sense, we can read-
ily compute the derivatives relating changes in the output variable with
respect to changes in several input variables. Fortunately, computing such
derivatives is a relatively easy task. There are two approaches: analytical
and finite-difference methods.
Once we obtain the derivatives of the network, we can evaluate their
statistical significance by bootstrapping. We next take up the topics of ana-
lytical and finite differencing for obtaining derivatives, and bootstrapping
for obtaining significance, in turn.
4.3.1
Analytic Derivatives
One may compute the analytic derivatives of the output y with respect to
the input variables in a feedforward network in the following way. Given
the network:
nk,t = ωk,0 +
i∗

i=1
ωk,ixi,t
(4.26)
Nk,t =
1
1 + e−ni,t
(4.27)
yt = γ0 +
k∗

k=1
γkNk,t
(4.28)
the partial derivative of yt with respect to xi∗,t is given by:
∂yt
∂xi∗,t
=
k∗

k=1
γkNk,t(1 −Nk,t)ωk,i∗
(4.29)

106
4. Evaluation of Network Estimation
The above derivative comes from an application of the chain rule:
∂yt
∂xi∗,t
=
k∗

k=1
∂yt
∂Nk,t
∂Nk,t
∂nk,t
∂nk,t
∂xi∗,t
(4.30)
and from the fact that the derivative of a logsigmoid function N has the
following property:
∂Nk,t
∂nk,t
= Nk,t[1 −Nk,t]
(4.31)
Note that the partial derivatives in the neural network estimation are
indexed by t. Each partial derivative is state-dependent, since its value at
any time or observation index t depends on the index t values of the input
variables, xt. The pure linear model implies partial derivatives that are
independent of the values of x. Unfortunately, with nonlinear models one
cannot make general statements about how the inputs affect the output
without knowledge about the values of xt.
4.3.2
Finite Differences
A more common way to compute derivatives are finite-difference methods.
Given a neural network function, y = f(x), x = [x1, . . . , xi, . . . , xi∗], one
way to approximate fi,t is through the one-sided finite-difference formula:
∂y
∂xi
= f(x1, . . . , xi + hi, . . . , xi∗) −f(x1, . . . , xi, . . . , xi∗)
hi
(4.32)
where the denominator hi is set at max(ϵ, ϵ.xi), with ϵ = 10−6.
Second-order partial derivatives are computed in a similar manner.
Cross-partials are given by the formula:
∂2y
∂xi∂xj
=
1
hjhi

{f(x1,...,xi+hi,xj +hj,...,xi∗)−f(x1,...,xi,...,xj +hj,...,xi∗)}
−{f(x1,...,xi+hi,xj,...,xi∗)−f(x1,...,xi,...,xj,...,xi∗)}

(4.33)
while the direct second-order partials are given by:
∂2y
∂x2
i
= 1
h2
i
 f(x1, . . . , xi + hi, xj, . . . , xi∗) −2f(. . . xi, . . . , xj, . . . , xi∗)
+(x1, . . . , xi −hi, xj, . . . , xi∗)

(4.34)
where {hi, hj} are the step sizes for calculating the partial derivatives.
Following Judd (1998), the step size hi = max(εxi, ε), where the scalar ε
is set equal to the value 10−6.

4.3 Interpretive Criteria and Significance of Results
107
4.3.3
Does It Matter?
In practice, it does not matter very much. Knowing the exact functional
form of the analytical derivatives certainly provides accuracy. However, for
more complex functional forms, differentiation becomes more difficult, and
as Judd (1998, p. 38) points out, finite-difference methods avoid errors that
may arise from this source.
Another reason to use finite-difference methods for computing the partial
derivatives of a network is that one can change the functional form, or
the number of hidden layers in the network, without having to derive a
new expression. Judd (1998) points out that analytic derivatives are better
considered only when needed for accuracy reasons, or as a final stage for
speeding up an otherwise complete program.
4.3.4
MATLAB Example: Analytic and Finite Differences
To show how closely the exact analytical derivatives and the finite differ-
ences match numerically, consider the logsigmoid function of a variable x,
1/[1+exp(−x)]. Letting x take on values from −1 to +1 at grid points of .1,
we can compute the analytical and finite differences for this interval with
the following MATLAB program, which calls the program myjacobian.m:
x = -1:.1:1; % Define the range of the input variable
x = x’;
y = inv(1+exp(-x)); % Calculate the output variable
yprime exact = y .* (1-y); % Calculate the analytical derivative
fun = ’logsig’; % Define function
h = 10 * exp(-6); % Define h
rr = length(x);
for i = 1:rr, % Calculate the finite derivative
yprime finite(i,:) = myjacobian(fun, x(i,:), h);
end
% Obtain the mean of the squared error
meanerrorsquared = mean((yprime finite - yprime exact).ˆ 2);
The results show that the mean sum of squared differences between the
exact and finite difference solutions is indeed a very small value; to be
exact, 5.8562e-007.
The function myjacobian is given by the following code:
function jac = myjacobian(fun, beta, lambda);
% computes the jacobian matrix from the function;
% inputs: function, beta, lambda
% output: jacobian
[rr k] = size(beta);

