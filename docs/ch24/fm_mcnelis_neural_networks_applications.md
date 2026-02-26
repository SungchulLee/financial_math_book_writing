# Neural Networks in Finance: Applications

!!! info "Source"
    **Neural Networks in Finance: Gaining Predictive Edge in the Market** by Paul D. McNelis, Academic Press, 2005.
    These notes are used for educational purposes.

## Estimating and Forecasting with Artificial Data

108
4. Evaluation of Network Estimation
value0 = feval(fun,beta);
vec1 = zeros(1,k);
for i = 1:k,
vec2 = vec1;
vec2(i) = max(lambda, lambda *beta(i));
betax = beta + vec2;
value1 = feval(fun,betax);
jac(i) = (value1 - value0) ./ lambda;
end
4.3.5
Bootstrapping for Assessing Significance
Assessing the statistical significance of an input variable in the neural net-
work processes is straightforward. Suppose we have a model with several
input variables. We are interested, for example, in whether or not govern-
ment spending growth affects inflation. In a linear model, we can examine
the t statistic. With nonlinear neural network estimation, however, the
number of network parameters is much larger. As was mentioned, likelihood
ratio statistics are often unreliable.
A more reliable but time-consuming method is to use the boostrapping
method originally due to Efron (1979, 1983) and Efron and Tibshirani
(1993). This bootstrapping method is different from the .632 bootstrap
method for in-sample bias. In this method, we work with the original date,
with the full sample, [y, x], obtain the best predicted value with a neural
network, y, and obtain the set of residuals, e = y −y. We then randomly
sample this vector, e, with replacement and obtain the first set of shocks for
the first bootstrap experiment, eb1. With this set of first randomly sampled
shocks from the base of residuals, eb1, we generate a new dependent variable
for the first bootstrap experiment, yb1 = y+ eb1, and use the new data set
[yb1 x] to re-estimate a neural network and obtain the partial derivatives
and other statistics of interest from the nonlinear estimation. We then
repeat this procedure 500 or 1000 times, obtaining ebi and ybi for each
experiment, and redo the estimation. We then order the set of estimated
partial derivatives (as well as other statistics) from lowest to highest values,
and obtain a probability distribution of these derivatives. From this we can
calculate bootstrap p-values for each of the derivatives, giving the proba-
bility of the null hypothesis that each of these derivatives is equal to zero.
The disadvantage of the bootstrap method, as should be readily appar-
ent, is that it is more time-consuming than likelihood ratio statistics, since
we have to resample from the original set of residuals and re-estimate the
network 500 or 1000 times. However, it is generally more reliable. If we can
reject the null hypothesis that a partial derivative is equal to zero, based on
resampling the original residuals and re-estimating the model 500 or 1000
times, we can be reasonably sure that we have found a significant result.

4.4 Implementation Strategy
109
4.4
Implementation Strategy
When we face the task of estimating a model, the preceding material indi-
cates that we have a large number of choices to make at all stages of the
process, depending on the weights we put on in-sample or out-of-sample
performance and the questions we bring to the research. For example, do
we take logarithms and first-difference the data? Do we deseasonalize the
data? What type of data scaling function should we use: the linear func-
tion, compressing the data between zero or one, or another one? What type
of neural network specification should we use, and how should we go about
estimating the model? When we evaluate the results, which diagnostics
should we take more seriously and which ones less seriously? Do we have
to do out-of-sample forecasting with a split-sample or a real-time method?
Should we use the bootstrap method? Finally, do we have to look at the
partial derivatives?
Fortunately, most of these questions generally take care of themselves
when we turn to particular problems. In general, the goal of neural network
research is to evaluate its performance relative to the standard linear model,
or in the case of classification, to logit or probit models. If logarithmic
first-differencing is the norm for linear forecasting, for example, then neu-
ral networks should use the same data transformation. For deciding the lag
structure of the variables in a time-series context, the linear model should
be the norm. Usually, lag section is based on repeated linear estimation
of the in-sample or training data set for different lag lengths of the vari-
ables, and the lag structure giving the lowest value of the Hannan-Quinn
information criterion is the one to use.
The simplest type of scaling should be used first, namely, the linear [0,1]
interval scaling function. After that, we can check the robustness of the
overall results with respect to the scaling function. Generally, the simplest
neural network alternative should be used, with a few neurons to start. A
good start would be the simple feedforward model or the jump-connection
network which uses a combination of the linear and logsigmoid connections.
For estimation, there is no simple solution; the genetic algorithm gen-
erally has to be used. It may make sense to use the quasi-Newton
gradient-descent methods for a limited number of iterations and not wait
for full converge, particularly if there are a large number of parameters.
For evaluating the in-sample criteria, the first goal is to see how well the
linear model performs. We would like a linear model that looks good, or
at least not too bad, on the basis of the in-sample criteria, particularly in
terms of autocorrelation and tests of nonlinearity. Very poor performance
on the basis of these tests indicates that the model is not well specified. So
beating a poorly specified model with a neural network is not a big deal.
We would like to see how well a neural network performs relative to the
best specified linear model.

110
4. Evaluation of Network Estimation
Generally a network model should do better in terms of overall explana-
tory power than a linear model. However, the acid test of performance is
out-of-sample performance. For macro data, real-time forecasting is the
sensible way to proceed, while split-sample tests are the obvious way to
proceed for cross-section data.
For obtaining the out-of-sample forecasts with the network models, we
recommend the thick model approach advocated by Granger and Jeon
(2002). Since no one neural network gives the same results if the start-
ing solution parameters or the scaling functions are different, it is best to
obtain an ensemble of predictions each period and to use a trimmed mean
of the multiple network forecasts for a thick model network forecast.
For comparing the linear and thick model network forecasts, the root
mean squared error criteria and Diebold-Mariano tests are the most widely
used for assessing predictive accuracy. While there is no harm in using
the bootstrap method for assessing overall performance of the linear and
neural net models, there is no guarantee of consistency between out-of-
sample accuracy through Diebold-Mariano tests and bootstrap dominance
for one method or the other. However, if the real world is indeed captured
by the linear model, then we would expect that linear models would domi-
nate the nonlinear network alternatives under the real-time forecasting and
bootstrap criteria.
In succeeding chapters we will illustrate the implementation of network
estimation for various types of data and relate the results to the theory of
this chapter.
4.5
Conclusion
Evaluation of the network performance relative to the linear approaches
should be with some combination of in-sample and out-of-sample criteria,
as well as by common sense criteria. We should never be afraid to ask
how much these models add to our insight and understanding. Of course,
we may use a neural network simply to forecast or simply to evaluate
particular properties of the data, such as the significance of one or more
input variables for explaining the behavior of the output variable. In this
case, we need not evaluate the network with the same weighting applied
to all three criteria. But in general we would like to see a model that has
good in-sample diagnostics also forecast out-of-sample well and make sense
and add to our understanding of economic and financial markets.
4.5.1
MATLAB Program Notes
Many of the programs are available for web searches and are also embedded
in popular software programs such as EViews, but several are not.

4.5 Conclusion
111
For in-sample diagnostics, for the Ljung-Box and McLeod-Li tests, the
program qstatlb.m should be used. For symmetry, I have written engleng.m,
and for normality, jarque.m. The Lee-White-Granger test is implemented
with wnntest1.m, and the Brock-Deckert-Scheinkman test is given by
bds1.m
For out-of-sample performance, the Diebold-Mariano test is given by
dieboldmar.m, and the Pesaran-Timerman directional accuracy test is given
by datest.m.
For evaluating first and second derivatives by finite differences, I have
written myjacobian.m and myhessian.m.
4.5.2
Suggested Exercises
For comparing derivatives obtained by finite differences with exact ana-
lytical derivatives, I suggest again using the MATLAB Symbolic Toolbox.
Write in a function that has an exact derivative and calculate the expres-
sion symbolically using funtool.m. Then create a function and find the
finite-difference derivative with myjacobian.m.


Part II
Applications and
Examples
113


5
Estimating and Forecasting with
Artificial Data
5.1
Introduction
This chapter applies the models and methods presented in the previous
chapters to artificially generated data. This is done to show the power of
the neural network approach, relative to autoregressive linear models, for
forecasting relatively complex, though artificial, statistical processes.
The primary motive for using artificial data is that there are no limits
to the size of the sample! We can estimate the parameters from a training
set with sufficiently large degrees of freedom, and then forecast with a rela-
tively ample test set. Similarly, we can see how well the fit and forecasting
performance of a given training and test set from an initial sample or real-
ization of the true stochastic process matches another realization coming
from the same underlying statistical generating process.
The first model we examine is the stochastic chaos (SC) model, the sec-
ond is the stochastic volatility/jump diffusion (SVJD) model, the third
is the Markov regime switching (MRS) model, the fourth is a volatil-
ity regime switching (VRS) model, the fifth is a distorted long-memory
(DLM) model, and the last is the Black-Scholes options pricing (BSOP)
model. The SC model is widely used for testing predictive accuracy of var-
ious forecasting models, the SVJD and VRS models are commonly used
models for representing volatile financial time series, and the MRS model
is used for analyzing GDP growth rates. The DLM model may be used to

116
5. Estimating and Forecasting with Artificial Data
represent an economy subject to recurring bubbles. Finally, the BSOP
model is the benchmark model for calculating the arbitrage-free prices
for options, under the assumption of the log normal distribution of asset
returns. This chapter shows how well neural networks, estimated with the
hybrid global-search genetic algorithm and local gradient approach, approx-
imate the data generated by these models relative to the linear benchmark
model.
In some cases, the structure is almost linear, so that the network should
not perform much better than the linear model — but it also should not
perform too much worse. In one case, the model is simply a martingale, in
which case the best predictor of yt+1 is yt. Again, the linear and network
models should not diverge too much in this case. We assume in each of
these cases that the forecasting agent does not know the true structure.
Instead, the agent attempts to learn the true data generating process from
linear and nonlinear neural network estimation, and forecast on the basis
of these two methods.
In each case, we work with stationary data. Thus, the variables are
first-differenced if there is a unit root. While the Dickey-Fuller unit root
tests, discussed in the previous chapter, are based on linear autoregressive
processes, we use these tests since they are standard and routinely used in
the literature.
When we work with neural networks and wish to compare them with
linear autoregressive models, we normally want to choose the best network
model relative to the best linear model. The best network model may well
have a different lag structure than the best linear model. We should choose
the best specifications for each model on the basis of in-sample criteria,
such as the Hannan-Quinn information criterion, and then see which one
does better in terms of out-of-sample forecasting performance, either in
real-time or in bootstrap approaches, or both. In this chapter, however, we
either work with univariate series generated with simple one-period lags
or with a cross-section series. We simply compare the benchmark linear
model against a simple network alternative, with the same lag structure
and three neurons in one hidden layer, in the standard “plain vanilla”
multilayer perceptron or feedforward network.
For choosing the best linear specification, we use an ample lag structure
that removes traces of serial dependence and minimizes the Hannan-Quinn
information criterion. To evaluate the linear model fairly against the net-
work alternative, the lag length should be sufficient to remove any obvious
traces of specification error such as serial dependence. Since the artificial
data in this chapter are intended to replicate properties of higher-frequency
daily data, we select a lag length of four, on the supposition that forecasters
would initially use such a lag structure (representing a year for quarterly
data, or almost a full business week for daily data) for estimation and
forecasting.

5.2 Stochastic Chaos Model
117
5.2
Stochastic Chaos Model
The stochastic chaos (SC) model has the following representation:
yt = 4 · ςt · yt−1 · (1 −yt−1)
ςt˜U(0, 1)
y0 = .5
(5.1)
The stochastic term ςt is a draw from a random uniform distribution. The
variable yt depends on its own lag, yt−1, as well as on (yt−1), multiplied
by a factor of 4. One realization appears in Figure 5.1. An easy code for
generating this series is given by the following list of MATLAB commands:
T = 500;
z = rand(T,1);
y(1,:) = .5;
for i = 2:T, y(i,:) = 4 * z(i,:) * y(i-1,:) * (1-y(i-1,:)); end
Notice that there are periods of consistent high volatility followed by flat
stable intervals, indicating a series of nonlinear events. We also see that
the stochastic model generates only positive values, since the shock comes
from a uniform distribution. Such a stochastic chaos process may be useful
for modeling either implied volatility or observed volatility processes rather
than rate-of-return processes in financial markets, since volatility processes
have, by definition, positive values. Figure 5.1 pictures one such realization
of a stochastic chaos process.
Chaos theory has been widely studied in applications to finance to see
if there are hidden chaotic properties within financial market data. One of
the properties of the stochastic process is that, for a given set of shocks
{ςt}, the set of outcomes {yt} does not vary much, after a suitable interval,
for any initial condition y0, provided that 0 < y0 < 1. However, before
that suitable interval has passed, the system dynamics vary quite a bit
for the given set of shocks {ςt}. Figure 5.2 pictures three stochastic chaos
processes for the same shocks, for y0 = [.001, .5, .99]. We see that the
dashed and dotted curves, processes generated by the initial conditions
y0 = [.5, .99], converge after five periods, whereas the process generated
by y0 = [.001] takes about 15 periods to converge to the same values as
generated by y0 = [.5, .99]. Thus, effects of the initial conditions wear off
with different speeds and show different volatilities for the same sets of
shocks and same laws of motion.
For values y0 = 0 or y0 = 1, of course, the process remains at zero, and
for y0 < 0 and y0 > 1, the process diverges very quickly. Thus, the process

118
5. Estimating and Forecasting with Artificial Data
0
50
100
150
200
250
300
350
400
450
500
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
FIGURE 5.1. Stochastic chaos process
has an extreme sensitivity to very small changes in the initial condition,
when the initial condition is in the neighborhood of zero or one.
5.2.1
In-Sample Performance
To fit the neural network and a linear model to this data set, we used both
the genetic algorithm global search and the quasi-Newton local gradient
methods. We withheld the last 20% (100 observations) as the out-of-sample
test set, for real-time forecasting. We also used the bootstrap forecasting
test.1
The in-sample performance of the linear model for the stochastic chaos
model is summarized in Table 5.1.
Table 5.1 tells us that the linear model explains 29% of the varia-
tion of the in-sample data set, while the corresponding statistic of the
1The data generated by this model are estimated by neural network methods with
the program nnetjump.m, available on the webpage of the author.

5.2 Stochastic Chaos Model
119
0
5
10
15
20
25
30
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
y0 = .001
y0 = .5 
y0 = .99 
FIGURE 5.2. Stochastic chaos process for different initial conditions
TABLE 5.1. In-Sample Diagnostics: Stochastic
Chaos Model (Structure: 4 Lags, 3 Neurons)
Diagnostic
Linear Model (Network Model)
Estimate
R2
.29 (.53)
HQIF
1534 (1349)
L-B∗
.251
M-L∗
.0001
E-N∗
.0000
J-B∗
.55
L-W-G
1000
B-D-S∗
.0000
∗marginal significance levels
network model, appearing in parentheses, explains 53%. The Hannan-
Quinn information criterion favors, not surprisingly, the network model.
The significance test of the Q statistic shows that we cannot reject serial
independence of the regression residuals. By all other criteria, the linear

120
5. Estimating and Forecasting with Artificial Data
0
50
100
150
200
250
300
350
400
−0.6
−0.4
−0.2
0
0.2
0.4
0.6
0.8
Linear Model
Network Model
FIGURE 5.3. In-sample errors: stochastic chaos model
specification suffers from serious specification error. There is evidence of
serial correlation in squared errors, as well as non-normality, asymmetry,
and neglected nonlinearity in the residuals. Such indicators would suggest
the use of nonlinear models as alternatives to the linear autoregressive
structure.
Figure 5.3 pictures the error paths predicted by the linear and network
models. The linear model errors are given by the solid curve and the net-
work errors by dotted paths. As expected, we see that the dotted curves
generally are closer to zero.
5.2.2
Out-of-Sample Performance
The path of the out-of-sample prediction errors appears in Figure 5.4. The
solid path represents the forecast error of the linear model while the dotted
curves are for the network forecast errors. This shows the improved per-
formance of the network relative to the linear model, in the sense that its
errors are usually closer to zero.
Table 5.2 summarizes the out-of-sample statistics. These are the root
mean squared error statistics (RMSQ), the Diebold-Mariano statistics for
lags zero through four (DM-0 to DM-4), the success ratio for percentage

5.2 Stochastic Chaos Model
121
0
10
20
30
40
50
60
70
80
90
100
−0.6
−0.4
−0.2
0
0.2
0.4
0.6
0.8
Linear Model
Network Model
FIGURE 5.4. Out-of-sample prediction errors: stochastic chaos model
TABLE 5.2. Forecast Tests: Stochastic Chaos Model
(Structure: 5 Lags, 4 Neurons)
Diagnostic
Linear
Neural Net
RMSQ
.147
.117
DM-0∗
—
.000
DM-1∗
—
.004e-5
DM-2∗
—
.032e-5
DM-3∗
—
.115e-5
DM-4∗
—
.209e-5
SR
1
1
B-Ratio
—
.872
∗marginal significance levels
of correct sign predictions (SR), and the bootstrap ratio (B-Ratio), which
is the ratio of the network bootstrap error statistic to the linear boot-
strap error measure. A value less than one, of course, represents a gain for
network estimation.

122
5. Estimating and Forecasting with Artificial Data
The results show that the root mean squared error statistic of the network
model is almost 20% lower than that of the linear model. Not surprisingly,
the Diebold-Mariano tests with lags zero through four are all significant.
The success ratio for both models is perfect, since all of the returns in
the stochastic chaos model are positive. The final statistic is the boot-
strap ratio, the ratio of the network bootstrap error relative to the linear
bootstrap error. We see that the network reduces the bootstrap error by
almost 13%.
Clearly, if underlying data were generated by a stochastic process,
networks are to be preferred over linear models.
5.3
Stochastic Volatility/Jump Diffusion Model
The SVJD model is widely used for representing highly volatile asset
returns in emerging markets such as Russia or Brazil during periods
of extreme macroeconomic instability. The model combines a stochastic
volatility component, which is a time-varying variance of the error term,
as well as a jump diffusion component, which is a Poisson jump process.
Both the stochastic volatility component and the Poisson jump components
directly affect the mean of the asset return process. They are realistic para-
metric representations of the way many asset returns behave, particularly
in volatile emerging-market economies.
Following Bates (1996) and Craine, Lochester, and Syrtveit (1999), we
present this process in continuous time by the following equations:
dS
S = (µ −λk) · dt +
√
V · dZ + k · dq
(5.2)
dV = (α −βV ) · dt + σv
√
V · dZv
(5.3)
Corr(dZ, dZv) = ρ
(5.4)
prob(dq = 1) = λ · dt
(5.5)
ln(1 + k) ∼φ(ln[1 + k] −.5κ, κ2)
(5.6)
where dS/S is the rate of return on an asset, µ is the expected rate of
appreciation, λ the annual frequency of jumps, and k is the random per-
centage jump conditional on the jump occurring. The variable ln(1 + k) is
distributed normally with mean ln[1+k]−.5κ and variance κ2. The symbol
φ represents the normal distribution. The advantage of the continuous time
representation is that the time interval can become arbitrarily smaller and
approximate real time changes.

5.3 Stochastic Volatility/Jump Diffusion Model
123
TABLE 5.3. Parameters for SVJD Process
Mean return
µ
.21
Mean volatility
α
.0003
Mean reversion of volatility
β
.7024
Time interval (daily)
dt
1/250
Expected jump
k
.3
Standard deviation of percentage jump
κ
.0281
Annual frequency of jumps
λ
2
Correlation of Weiner processes
ρ
.6
The instantaneous conditional variance V
follows a mean-reverting
square root process. The parameter α is the mean of the conditional vari-
ance, while β is the mean-reversion coefficient. The coefficient σv is the
variance of the volatility process, while the noise terms dZ and dZv are the
standard continuous-time white noise Weiner processes, with correlation
coefficient ρ.
Bates (1996) points out that this process has two major advantages.
First, it allows systematic volatility risk, and second, it generates an “ana-
lytically tractable method” for pricing options without sacrificing accuracy
or unnecessary restrictions. This model is especially useful for option
pricing in emerging markets.
The parameters used to generate the SVJD process appear in Table 5.3.
In this model, St+1 is equal to St+[St·(µ−λk)] ·dt, and for a small value
of dt will be unit-root nonstationary. After first-differencing, the model will
be driven by the components of dV and k·dq, which are random terms. We
should not expect the linear or neural network model to do particularly well.
Put another way, we should be suspicious if the network model significantly
outperforms a rather poor linear model.
One realization of the SVJD process, after first-differencing, appears in
Figure 5.5. As in the case of the stochastic chaos model, there are periods
of high volatility followed by more tranquil periods. Unlike the stochastic
chaos model, however, the periods of tranquility are not perfectly flat.
We also notice that the returns in the SVJD model are both positive and
negative.
5.3.1
In-Sample Performance
Table 5.4 gives the in-sample regression diagnostics of the linear model.
Clearly, the linear approach suffers serious specification error in the error
structure. Although the network multiple correlation coefficient is higher
than that of the linear model, the Hannan-Quinn information criterion
only slightly favors the network model. The slight improvement of the R2
statistic does not outweigh by too much the increase in complexity due to

124
5. Estimating and Forecasting with Artificial Data
0
50
100
150
200
250
300
350
400
450
500
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
FIGURE 5.5. Stochastic volatility/jump diffusion process
TABLE 5.4. In-Sample Diagnostics: First-Differenced
SVJD Model (Structure: 4 Lags, 3 Neurons)
Diagnostic
Linear Model (Network Model)
Estimate
R2
.42 (.45)
HQIF
935 (920)
L-B∗
.783
M-L∗
.025
E-N∗
.0008
J-B∗
0
L-W-G
11
B-D-S∗
.0000
∗marginal significance levels
the larger number of parameters to be estimated. While the Lee-White-
Granger test does not turn up evidence of neglected nonlinearity, the BDS
test does. Figure 5.6 gives in-sample errors for the SVJD realizations. We
do not see much difference.

5.4 The Markov Regime Switching Model
125
0
50
100
150
200
250
300
350
400
−0.8
−0.6
−0.4
−0.2
0
0.2
0.4
0.6
Linear
Network 
FIGURE 5.6. In-sample errors: SVJD model
5.3.2
Out-of-Sample Performance
Figure 5.7 pictures the out-of-sample errors of the two models. As expected,
we do not see much difference in the two paths.
The out-of-sample statistics appearing in Table 5.5 indicate that the
network model does slightly worse, but not significantly worse, than the lin-
ear model, based on the Diebold-Mariano statistic. Both models do equally
well in terms of the success ratio for correct sign predictions, with slightly
better performance by the network model. The bootstrap ratio favors the
network model, reducing the error percentage of the linear model by slightly
more than 3%.
5.4
The Markov Regime Switching Model
The Markov regime switching model is widely used in time-series analysis
of aggregate macro data such as GDP growth rates. The basic idea of the

126
5. Estimating and Forecasting with Artificial Data
0
10
20
30
40
50
60
70
80
90
100
−0.6
−0.5
−0.4
−0.3
−0.2
−0.1
0
0.1
0.2
0.3
0.4
Linear Model
Network Model
FIGURE 5.7. Out-of-sample prediction errors: SVJD model
TABLE 5.5. Forecast Tests: SVJD Model (Structure:
4 Lags, 3 Neurons)
Diagnostic
Linear
Neural Net
RMSQ
.157
.167
DM-0∗
—
.81
DM-1∗
—
.74
DM-2∗
—
.73
DM-3∗
—
.71
DM-4∗
—
.71
SR
.646
.656
B-Ratio
—–
.968
∗marginal significance levels
regime switching model is that the underlying process is linear. However,
the process follows different regimes when the economy is growing and
when the economy is shrinking. Originally due to Hamilton (1990), it was
applied to GDP growth rates in the United States.

5.4 The Markov Regime Switching Model
127
Following Tsay (2002, p. 135–137), we simulate the following model rep-
resenting the rate of growth of GDP for the U.S. economy for two states in
the economy, S1 and S2:
xt = cc +
p

i−1
φ1,ixt−i + ε1,i, ε1˜φ(0, σ2
1), if S = S1
= c2 +
p

i−1
φ2,ixt−i + ε2,i ε2˜φ(0, σ2
2) if S = S2
(5.7)
where φ represents the Gaussian density function. These states have the
following transition matrix, P, describing the probability of moving from
one state to the next, from time (t −1) to time t:
P =
 (S1
t,|S1
t−1,) (S1
t,|S2
t−1,)
(S2
t,|S1
t−1,) (S2
t,|S2
t−1,)

=

(1 −w2) w2
w1 (1 −w1)

(5.8)
The MRS model is essentially a combination of two linear models with
different coefficients, with a jump or switch pushing the data-generating
mechanism from one model to the other. So there is only a small degree
of nonlinearity in this system. The parameters used for generating 500
realizations of the MRS model appear in Table 5.6.
Notice that in the specification of the transition probabilities, as Tsay
(2002) points out, “it is more likely for the U.S. GDP to get out of a
contraction period than to jump into one” [Tsay (2002), p. 137]. In our
simulation of the model, the transition probability matrix is called from
a uniform random number generator. If, for example, in state S = S1, a
random value of .1 is drawn, the regime will switch to the second state,
S = S2. If a value greater than .118 is drawn, then the regime will remain
in the first state, S = S1.
TABLE 5.6. Parameters for MRS Process
Parameter
State 1
State 2
ci
.909
−.420
φi,1
.265
.216
φi,2
.029
.628
φi,3
−.126
−.073
φi,4
−.110
−.097
σi
.816
1.01
wi
.118
.286

128
5. Estimating and Forecasting with Artificial Data
0
50
100
150
200
250
300
350
400
450
500
−6
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
FIGURE 5.8. Markov switching process
The process {xt} exhibits periodic regime changes, with different dynam-
ics in each regime or state. Since the representative forecasting agent does
not know that the true data-generating mechanism for {xt} is a Markov
regime switching model, a unit root test for this variable cannot reject an
I(1) or nonstationary process. However, work by Lumsdaine and Papell
(1997) and Cook (2001) has drawn attention to the bias of unit root tests
when structural breaks take place. We thus approximate the process {xt}
as a stationary process.
The underlying data-generating mechanism is, of course, near linear,
so we should not expect great improvement from neural network approxi-
mation. One realization, for 500 observations, appears in Figure 5.8.
5.4.1
In-Sample Performance
Table 5.7 gives the in-sample regression diagnostics of the linear model.
The linear regression model does not do a bad job, up to a point: there is
no significant evidence of serial correlation in the residuals, and we cannot

5.4 The Markov Regime Switching Model
129
TABLE 5.7. In-Sample Diagnostics:
MRS
Model (Structure: 4 Lags, 3 Neurons)
Diagnostic
Linear Model (Network Model)
Estimate
R2
.35 (.38)
HQIF
3291 (3268)
L-B∗
.91
M-L∗
.0009
E-N∗
.0176
J-B∗
.36
L-W-G
13
B-D-S∗
.0002
∗marginal significance levels
reject normality in the distribution of the residuals. The BDS test shows
some evidence of neglected nonlinearity, but the LWG test does not.
Figure 5.9 pictures the error paths generated by the linear and neural net
models. While the overall explanatory power or R2 statistic of the neural
0
50
100
150
200
250
300
350
400
−4
−3
−2
−1
0
1
2
3
4
Linear
Network 
FIGURE 5.9. In-sample errors: MRS model

130
5. Estimating and Forecasting with Artificial Data
TABLE 5.8. Forecast Tests: MRS Model (Structure:
1 Lag, 3 Neurons)
Diagnostic
Linear
Neural Net
RMSQ
1.122
1.224
DM-0∗
—
.27
DM-1∗
—
.25
DM-2∗
—
.15
DM-3∗
—
.22
DM-4∗
—
.24
SR
.77
.72
B-Ratio
—
.982
∗marginal significance levels
net is slightly higher and the Hannan-Quinn information criterion indicates
that the network model should be selected, there is not much noticeable
difference in the two paths relative to the actual series.
5.4.2
Out-of-Sample Performance
The forecast statistics appear in Table 5.8. We see that the root mean
squared error is slightly higher for the network, but the Diebold-Mariano
statistics indicate that the difference in the prediction errors is not statis-
tically significant. The bootstrap error ratio shows that the network model
gives a marginal improvement relative to the linear benchmark.
The paths of the linear and network out-of-sample errors appear in
Figure 5.10.
We see, not surprisingly, that both the linear and network models deliver
about the same accuracy in out-of-sample forecasting. Since the MRS is
basically a linear model with a small probability of a switch in the coeffi-
cients of the linear data-generating process, the network simply does about
as well as the linear model.
What will be more interesting is the forecasting of the switches in volatil-
ity, rather than the return itself, in this series. We return to this subject in
the following section.
5.5
Volatility Regime Switching Model
Building on the stochastic volatility and Markov regime switching models
and following Tsay [(2002), p. 133], we use a simple autoregressive model
with a regime switching mechanism for its volatility, rather than the return

5.5 Volatility Regime Switching Model
131
0
10
20
30
40
50
60
70
80
90
100
−3
−2
−1
0
1
2
3
Linear
Network
FIGURE 5.10. Out-of-sample prediction errors: MRS model
process itself. Specifically, we simulate the following model, similar to the
one Tsay estimated as a process representing the daily log returns, including
dividend payments, of IBM stock:2
rt = .043 −.022rt−1 + σt + ut
(5.9)
ut = σtεt, εt˜φ(0, 1)
(5.10)
σ2
t = .098u2
t−1 + .954σ2
t−1 if ut−1 ≤0
= .060 + .046u2
t−1 + .8854σ2
t−1 if ut−1 > 0
(5.11)
where φ(0, 1) is the standard normal or Gaussian density. Notice that this
VRS model will have drift in its volatility when the shocks are positive,
but not when the shocks are negative. However, as Tsay points out, the
2Tsay (2002) omits the GARCH-in-Mean term .5σt in his specification of the
returns rt.

132
5. Estimating and Forecasting with Artificial Data
0
50
100
150
200
250
300
350
400
450
500
−6
−4
−2
0
2
4
6
8
0
50
100
150
200
250
300
350
400
450
500
0
1
2
3
4
5
First-Differenced Returns 
Volatility
FIGURE 5.11. First-differenced returns and volatility of the VRS model
model essentially follows an IGARCH (integrated GARCH) when shocks
are negative, since the coefficients sum to a value greater than unity.
Figure 5.11 pictures the first-differenced series of {rt}, since we could
not reject a unit-root process, as well as the volatility process {σ2
t }.
5.5.1
In-Sample Performance
Table 5.9 gives the linear regression results for the returns. We see that
the in-sample explanatory power of both models is about the same. While
the tests for serial dependence in the residuals and squared residuals, as
well as for symmetry and normality in the residuals, are not significant,
the BDS test for neglected nonlinearity is significant. Figure 5.12 pictures
the in-sample error paths of the two models.
5.5.2
Out-of-Sample Performance
Figure 5.13 and Table 5.10 show the out-of-sample performance of the
two models. Again, there is not much to recommend the network model

5.5 Volatility Regime Switching Model
133
TABLE
5.9. In-Sample
Diagnostics:
VRS
Model (Structure: 4 Lags, 3 Neurons)
Diagnostic
Linear Model (Network Model)
Estimate
R2
.422 (.438)
HQIF
3484 (3488)
L-B∗
.85
M-L∗
.13
E-N∗
.45
J-B∗
.22
L-W-G
6
B-D-S∗
.07
∗marginal significance levels
0
50
100
150
200
250
300
350
400
−6
−4
−2
0
2
4
6
Linear
Network 
FIGURE 5.12. In-sample errors: VRS model
for return forecasting, but in its favor, it does not perform worse in any
noticeable way than the linear model.
While these results do not show overwhelming support for the superiority
of network forecasting for the volatility regime switching model, they do

134
5. Estimating and Forecasting with Artificial Data
0
10
20
30
40
50
60
70
80
90
100
−3
−2
−1
0
1
2
3
4
5
Network 
Linear
FIGURE 5.13. Out-of-sample prediction errors: VRS model
TABLE 5.10. Forecast Tests: VRS Model
(Structure: 4 Lags, 3 Neurons)
Diagnostic
Linear
Neural Net
RMSQ
1.37
1.38
DM-0∗
—
.58
DM-1∗
—
.58
DM-2∗
—
.57
DM-3∗
—
.56
DM-4∗
—
.55
SR
.76
.76
B-Ratio
—
.99
∗marginal significance levels
show improved out-of-sample performance both by the root mean squared
error and the bootstrap criteria. It should be noted once more that the
return process is highly linear by design. While the network does not do
significantly better by the Diebold-Mariano test, it does buy a forecasting
improvement at little cost.

5.6 Distorted Long-Memory Model
135
5.6
Distorted Long-Memory Model
Originally put forward by Kantz and Schreiber (1997), the distorted long-
memory (DLM) model was recently analyzed for stochastic neural network
approximation by Lai and Wong (2001). The model has the following form:
yt = x2
t−1xt
(5.12)
xt = .99xt−1 + ϵt
(5.13)
ϵ ∼N(0, σ2)
(5.14)
Following Lai and Wong, we specify σ = .5 and x0 = .5. One realization
appears in Figure 5.14. It pictures a market or economy subject to bubbles.
Since we can reject a unit root in this series, we analyze it in levels rather
than in first differences.3
0
50
100
150
200
250
300
350
400
450
500
−20
0
20
40
60
80
100
120
140
160
FIGURE 5.14. Returns of DLM model
3We note, however, the unit root tests are designed for variables emanating from a
linear data-generating process.

136
5. Estimating and Forecasting with Artificial Data
TABLE
5.11. In-Sample
Diagnostics:
DLM
Model (Structure: 4 Lags, 3 Neurons)
Diagnostic
Linear Model
R2
.955 (.957)
HQIF
4900(4892)
L-B∗
.77
M-L∗
.0000
E-N∗
.0000
J-B∗
.0000
L-W-G
1
B-D-S∗
.000001
∗marginal significance levels
0
50
100
150
200
250
300
350
400
−30
−20
−10
0
10
20
30
Linear
Network 
FIGURE 5.15. Actual and in-sample predictions: DLM model
5.6.1
In-Sample Performance
The in-sample statistics and time paths appear in Table 5.11 and
Figure 5.15, respectively. We see that the in-sample power of the linear

5.7 Black-Sholes Option Pricing Model: Implied Volatility Forecasting
137
TABLE 5.12. Forecast Tests: DLM Model
(Structure: 4 Lags, 3 Neurons)
Diagnostic
Linear
Neural Net
RMSQ
6.81
6.58
DM-0∗
—–
.09
DM-1∗
—–
.09
DM-2∗
—–
.05
DM-3∗
—–
.01
DM-4∗
—–
.02
SR
1
1
B-Ratio
—–
.99
∗marginal significance levels
model is quite high. The network model is slightly higher, and it is favored
by the Hannan-Quinn criterion. Except for insignificant tests for serial inde-
pendence, however, the diagnostics all indicate lack of serial independence,
in terms of serial correlation of the squared errors, as well as non-normality,
asymmetry, and neglected nonlinearity (given by the BDS test result). Since
the in-sample predictions of the linear and neural network models so closely
track the actual path of the dependent variable, we cannot differentiate the
movements of these variables in Figure 5.15.
5.6.2
Out-of-Sample Performance
The relevant out-of-sample statistics appear in Table 5.12 and the predic-
tion error paths are in Figure 5.16. We see that the root mean squared errors
are significantly lower, while the success ratio for the sign predictions are
perfect for both models. The network bootstrap error is also practically
identical. Thus, the network gives a significantly improved performance
over the linear alternative, on the basis of the Diebold-Mariano statistics,
even when the linear alternative gives a very high in-sample fit.
5.7
Black-Sholes Option Pricing Model: Implied
Volatility Forecasting
The Black-Sholes (1973) option pricing model is a well-known method
for calculating arbitrage-free prices for options. As Peter Bernstein (1998)
points out, this formula was widely in use by practitioners before it was
recognized through publication in academic journals.

138
5. Estimating and Forecasting with Artificial Data
0
10
20
30
40
50
60
70
80
90
100
−20
−15
−10
−5
0
5
10
15
20
FIGURE 5.16. Out-of-sample prediction errors: DLM model
A call option is an agreement in which the buyer has the right, but not
the obligation, to buy an asset at a particular strike price, X, at a preset
future date. A put option is a similar agreement, with the right to sell an
asset at a preset strike price. The options-pricing problem comes down to
the calculation of an arbitrage-free price for the seller of the option. What
price should the seller charge so that the seller will not systematically lose?
The calculation of the arbitrage-free price of the option in the Black-
Sholes framework rests on the assumption of log-normal distribution of
stock returns. Under this assumption, Black and Sholes obtained a closed-
form solution for the calculation of the arbitrage-free price of an option.
The solution depends on five variables: the market price of the underlying
asset, S; the agreed-upon strike price, X; the risk-free interest rate, rf;
the maturity of the option, τ; and the annualized volatility or standard
deviation of the underlying returns, σ. The maturity parameter τ is set
at unity for annual, .25 for quarterly, .125 for monthly, and .004 for daily
horizons.
The basic Black-Sholes formula yields the price of a European option.
This type of option can be executed or exercised only at the time of
maturity of the option. This formula has been extended to cover American

5.7 Black-Sholes Option Pricing Model: Implied Volatility Forecasting
139
options, in which the holder of the option may execute it at any time up
to the expiration date of the option, as well as for options with ceilings or
floors, which limit the maximum payout of the option.4
Options, of course, are widely traded on the market, so their price will
vary from moment-to-moment. The Black-Sholes formula is particularly
useful for calculating the issue price of new options. A newly issued option
that is mispriced will be quickly arbitraged by market traders. In addition,
the formula is often used for calculating the shadow price of different types
of risk exposure. For example, a company expecting to receive revenue in
British sterling over the next year, but that has costs in U.S. dollars, may
wish to “price” their risk exposure. One price, of course, would be the cost
of an option to cover their exposure to loss through a collapse of British
sterling.5
Following Campbell, Lo, and MacKinlay (1997), the formula for pricing
a call option is given by the following three equations:
C(S, X, τ, σ) = S · Φ(d1) −X · exp(−r · τ) · Φ(d2)
(5.15)
d1 =
ln
 S
X

+

r + σ2
2

τ
σ√τ
(5.16)
d2 =
ln
 S
X

+

r −σ2
2

τ
σ√τ
(5.17)
where Φ(d1) and Φ(d2) are the standard normal cumulative distribution
functions of the variables d1 and d2. C(S, X, τ, σ) is the call option price of
an underlying asset with a current market price S, with exercise price X,
maturity τ, and annualized volatility σ.
Figure 5.17 pictures randomly generated values of S, X, r, τ, and σ as
well as the calculated call option price from the Black-Scholes formula.
The call option data represent a random cross section for different types
of assets, with different current market rates, exercise prices, risk-free rates,
maturity horizons, and underlying volatility. We are not working with time-
series observations in this approximation exercise. The goal of this exercise
is to see how well a neural network, relative to a linear model, can approxi-
mate the underlying true Black-Sholes option pricing formula for predicting
the not-call option price, given the observations on S, X, r, τ, and σ, but
4See Neft¸ci (2000) for a concise treatment of the theory and derivation of option-
pricing models.
5The firm may also enter into a forward contract on foreign exchange markets. While
preventing loss due to a collapse of sterling, the forward contract also prevents any gain
due to an appreciation of sterling.

140
5. Estimating and Forecasting with Artificial Data
0
200
400
600
800
1000
0
20
40
60
0
200
400
600
800
1000
80
90
100
110
120
0
200
400
600
800
1000
90
100
110
120
0
200
400
600
800
1000
0
0.05
0.1
0.15
0.2
0
200
400
600
800
1000
0
0.5
1
1.5
0
200
400
600
800
1000
0
0.5
1
1.5
CALL 
MARKET PRICE 
STRIKE PRICE 
RISK FREE RATE 
MATURITY
VOLATILITY 
FIGURE 5.17.
rather the implied volatility from market data on option prices, as well as
on S, X, r, τ.
Hutchinson, Lo, and Poggio (1994) have extensively explored how well
neural network methods (including both radial basis and feedforward net-
works) approximate call option prices.6 As these authors point out, were we
working with time-series observations, it would be necessary to transform
the independent variables S, X,and C into ratios, St/Xt and Ct/Xt.
5.7.1
In-Sample Performance
Table 5.13 gives the in-sample statistics. The R2 statistic is relatively high,
while all of the diagnostics are acceptable, except the Lee-White-Granger
test for neglected nonlinearity.
6Hutchinson, Lo, and Poggio (1994) approximate the ratio of the call option price to
the strike price, as a function of the ratio of the stock price to the strike price, and the
time to maturity. They take the volatility and the risk-free rate of interest as given.

5.7 Black-Sholes Option Pricing Model: Implied Volatility Forecasting
141
TABLE 5.13. In-Sample Diagnostics:
BSOP
Model Structure:
Diagnostic
Linear Model (Network Model)
Estimate
R2
.91(.99)
HQIF
246(−435)
L-B∗
—
M-L∗
—
E-N∗
.22
J-B∗
.33
L-W-G
997
B-D-S∗
.47
∗marginal significance levels
The in-sample error paths appear in Figure 5.18. The paths of both the
network and linear models closely track the actual volatility path. While
the R2 for the network is slightly higher, there is not much appreciable
difference.
0
50
100
150
200
250
300
350
400
−0.2
−0.15
−0.1
−0.05
0
0.05
0.1
0.15
0.2
0.25
0.3
Linear
Network 
FIGURE 5.18. In-sample errors: BSOP model


## Exchange Rate Volatility

142
5. Estimating and Forecasting with Artificial Data
TABLE 5.14. Forecast Tests: BSOP Model
Diagnostic
Linear
Neural Net
RMSQ
.0602
.0173
DM-0∗
—
0
DM-1∗
—
0
DM-2∗
—
0
DM-3∗
—
0
DM-4∗
—
0
SR
1
1
B-Ratio
—
.28
∗marginal significance levels
5.7.2
Out-of-Sample Performance
The superior out-of-sample performance of the network model over the
linear model is clearly shown in Table 5.14 and in Figure 5.18. We see that
the root mean squared error is reduced by more than 80% and the bootstrap
error is reduced by more than 70%. In Figure 5.19, the network errors are
closely distributed around zero, whereas there are large deviations with the
linear approach.
5.8
Conclusion
This chapter evaluated the performance of alternative neural network mod-
els relative to the standard linear model for forecasting relatively complex
artificially generated time series. We see that relatively simple feedforward
neural nets outperform the linear models in some cases, or do not do worse
than the linear models. In many cases we would be surprised if the neural
networks did much better than the linear model, since the underlying data
generating processes were almost linear.
The results of our investigation of these diverse stochastic experiments
suggest that the real payofffrom neural networks will come from volatility
forecasting rather than pure return forecasting in financial markets, as we
see in the high payofffrom the implied volatility forecasting exercise with
the Black-Sholes option pricing model. Since the neural networks never do
appreciably worse than linear models, the only cost for using these methods
is the higher computational time.
5.8.1
MATLAB Program Notes
The main script functions, as well as subprograms, are available on the web-
site. The programs are forecast onevar scmodel new1.m (for the stochastic

5.8 Conclusion
143
0
10
20
30
40
50
60
70
80
90
100
−0.2
−0.15
−0.1
−0.05
0
0.05
0.1
0.15
0.2
0.25
Linear
Network 
FIGURE 5.19. Out-of-sample prediction errors: BSOP model
chaos model), forecast onevar svjdmodel new1.m (for the stochastic volatil-
ity jump diffusion model), forecast onevar markovmodel new1.m (for the
Markov regime switching model), and forecast onevar dlm new1.m (for the
distorted long-memory model).
5.8.2
Suggested Exercises
The programs in the previous section can be modified to generate alterna-
tive series of artificial data, extend the length of the sample, and modify the
network models used for estimation and forecasting performance against
the linear model. I invite the reader to continue these experiments with
artificial data.


6
Times Series: Examples from Industry
and Finance
This chapter moves the analysis away from artificially generated data to
real-world data, to see how well the neural network model performs rela-
tive to the linear model. We focus on three examples: one from industry,
the quantity of automobiles manufactured in the United States; one from
finance, the spreads and the default rate on high-yield corporate bonds; and
one from macroeconomics, forecasting inflation rates. In all three cases we
use monthly observations.
Neural networks, of course, are routinely applied to forecasting very
high-frequency data, such as daily exchange rates or even real-time share-
market prices. However, in this chapter we show how the neural network
performs when applied to more commonly used, and more widely accessible,
data sets. All of the data sets are raw data sets, requiring adjustment for
stationarity.
6.1
Forecasting Production in the Automotive
Industry
The market for automobiles is a well-developed one, and there is a wealth
of research on the theoretical foundations and the empirical behavior of this
market. Since Chow (1960) demonstrated that this is one of the more stable
consumer durable markets, empirical analysis has focused on improving the

146
6. Times Series: Examples from Industry and Finance
aggregate and disaggregated market forecasting with traditional time series
as well as with pooled time-series cross-sectional methodologies, such as the
study by McCarthy (1996).
The structure of the automobile market (for new vehicles) is recursive.
Manufacturers evaluate and forecast the demand for the stock of automo-
biles, the number of retirements, and their market share. Adding a dose of
strategic planning, they decide how much to produce. These decisions occur
well before production and distribution take place. Manufacturers are pro-
viding a flow of capital goods to augment an existing stock. For their part,
consumers decide at the time of purchase, based on their income, price, and
utility requirements, what stock is optimal. To the extent that consumer
decisions to expand the stock of the asset coincide with or exceed the
amount of production by manufacturers, prices will adjust to revise the
optimal stock and clear the market. To the extent they fall short, the num-
ber of retirements of automobiles will increase and the price of new vehicles
will fall to clear the market. Chow (1960), Hess (1977), and McCarthy
(1996) show how forecasting the demand in the markets is a sufficient
proxy to modeling the optimal stock decision.
Both the general stability in the underlying market structure and the
recursive nature of producer versus consumer decision making have made
this market amenable to less complex estimation methods. Since research
suggests this is precisely the kind of market in which linear time-series
forecasting will perform rather well, it is a good place to test the usefulness
of the alternative of neural networks for forecasting.1
6.1.1
The Data
We make use of quantity and price data for automobiles, as well as an
interest rate and a disposable income as aggregate variables. The quantity
variable represents the aggregate production of new vehicles, excluding
heavy trucks and machinery, obtained from the Bureau of Economic Anal-
ysis of the Department of Commerce. The price variable is an index
appearing in the Bureau of Labor Statistics. The interest rate argument
is the home mortgage rate available from the Board of Governors of the
U.S. Federal Reserve System, while the income argument is personal dis-
posable income, also obtained from the Bureau of Economic Analysis of
the Department of Commerce. Home mortgage rates were chosen as the
relevant interest rate following Hess (1977), who shows that consumers con-
sider housing and automobile decisions jointly. Personal disposable income
was generated from consumption and savings data. The consumption series
1These points were made in a joint work with Gerald Nickelsburg. See McNelis and
Nickelsburg (2002).

6.1 Forecasting Production in the Automotive Industry
147
1992
1993
1994
1995
1996
1997
1998
1999
2000
2001
−0.05
0
0.05
1992
1993
1994
1995
1996
1997
1998
1999
2000
2001
−0.02
0
0.02
1992
1993
1994
1995
1996
1997
1998
1999
2000
2001
−0.1
0
0.1
1992
1993
1994
1995
1996
1997
1998
1999
2000
2001
−0.5
0
0.5
Rate of Growth of Automobile Production
Rate of Growth of Automotive Prices 
Change in Mortgage Rates 
Rate of Growth of Disposable Income 
FIGURE 6.1. Automotive industry data
was the average over the quarter to reflect more accurately the permanent
income concept.
Figure 6.1 pictures the evolution of the four variables we use in this exam-
ple: annualized rates of change of the quantity and price indices obtained
from the U.S. automotive industry, as well as the corresponding annual
changes in the U.S. mortgage rates and the annualized rate of growth of
U.S. disposable income.
We note some interesting features of the data: there has been no sharp
rise in the rate of growth of prices since the mid-90s, while the peak year
for automobile production growth took place between 1999 and 2000; and
disposable income growth has been generally positive, with the exception
of the recession at the end of the first Gulf War between 1992 and 1993.
Table 6.1 presents a statistical summary of these data.
We see that for the decade as a whole, there has been about a 4.5%
annual growth in automobile production, whereas the price growth has
been slightly less than 1% and disposable income growth has been about
0.5%. We also do not see a strong contemporaneous correlation between the
variables. In fact, there are two “wrong” signs: a negative contemporaneous

148
6. Times Series: Examples from Industry and Finance
TABLE 6.1. Summary of Automotive Industry Data
Annualized Growth Rates: 1992–2001
Quantity
Price
Mortgage Rates
Disposable Income
Mean
0.0450
0.0077
−0.0012
0.0050
Std. Dev.
0.1032
0.0188
0.0092
0.0335
Correlation Matrix
Quantity
Price
Mortgage Rates
Disposable Income
Quantity
1.0000
Price
0.2847
1.0000
Mortgage Rates
0.1248
0.1646
1.0000
0.2142
Disp. Income
−0.1703
−0.3304
0.2142
1.0000
correlation between disposable income growth and quantity growth, and a
positive contemporaneous correlation between changes in mortgage rates
and quantity growth.
6.1.2
Models of Quantity Adjustment
We use three models: a linear model, a smooth-transition regime switching
model, and a neural network smooth-transition regime switching model
(discussed in Section 2.5). We are working with monthly data. We are
interested in the year-to-year changes in these data. When forecasting,
we are interested in the annual or twelve-month forecast of the quantity
of automobiles produced because investors are typically interested in the
behavior of a sector over a longer horizon than one month or one quarter.
Given the nature of lags in investment and time-to-build considerations,
production over the next few months will have little to do with decisions
made at time t.
Letting Qt represent the quantity of automobiles produced at time t, we
forecast the following variable:
∆hqt+h = qt+h −qt
(6.1)
qt = ln(Qt)
(6.2)
where h = 12, for an annualized forecast with monthly data.
The dependent variable ∆qt+h depends on the following set of current
variables xt
xt = [∆12qt, ∆12pt, ∆12rt, ∆12yt]
(6.3)

6.1 Forecasting Production in the Automotive Industry
149
∆12pt = ln(Pt) −ln(Pt−12)
(6.4)
∆12rt = ln(Rt) −ln(Rt−12)
(6.5)
∆12yt = ln(Yt) −ln(Yt−12)
(6.6)
where Pt, Rt, and Yt signify the price index, the gross mortgage rate, and
disposable income at time t. Although we can add further lags for ∆qt,
we keep the set of regressions limited to the 12-month backward-looking
horizon. The current value of ∆qt looks back over 12 months while the
dependent variable looks forward over 12 months. We consider this a suffi-
ciently ample lag structure. We also wish to avoid the problem of searching
for different optimal lag structures for the three different models.
The linear model has the following specification:
∆qt+h = αxt + ηt
(6.7)
ηt = ϵt + γ(L)ϵt−1
(6.8)
ϵt ∼N(0, σ2)
(6.9)
The disturbance term ηt consists of a current period white-noise shock
ϵt in addition to eleven lagged values of this shock, weighted by the vector
γ. We explicitly model serial dependence as a moving average process since
it is well known that whenever the forecast horizon exceeds the sampling
interval, temporal dependence is induced in the disturbance term.
We compare this model with the smooth-transition regime switch-
ing (STRS) model and then with the neural network smooth-transition
regime switching (NNSTRS) model. The STRS model has the following
specification:
∆qt+h = Ψtα1xt + (1 −Ψt)α2xt + ηt
(6.10)
Ψt = Ψ(θ · ∆yt −c)
(6.11)
= 1/[1 + exp(θ · ∆yt −c)]
(6.12)
ηt = ϵt + γ(L)ϵt−1
(6.13)
ϵt ∼N(0, σ2)
(6.14)
where Ψt is a logistic or logsigmoid function of the rate of growth of dis-
posable income, ∆yt, as well as the threshold parameter c and smoothness
parameter θ. For simplicity, we set c = 0, thus specifying two regimes, one
when disposable income is growing and the other when it is shrinking.

150
6. Times Series: Examples from Industry and Finance
The NNSTRS model has the following form:
∆qt+h = αxt + β[ΨtG(xt; α1) + (1 −Ψt)H(xt; α2)] + ηt
(6.15)
Ψt = Ψ(θ · ∆yt −c)
(6.16)
= 1/[1 + exp(θ · ∆yt −c)]
(6.17)
G(xt; α1) = 1/[1 + exp(−α1xt)]
(6.18)
H(xt; α2) = 1/[1 + exp(−α2xt)]
(6.19)
ηt = ϵt + γ(L)ϵt−1
(6.20)
ϵt ∼N(0, σ2)
(6.21)
In the NNSTRS model, Ψt appears again as the transition function.
The functions G(xt; α1) and H(xt; α2) are logsigmoid transformations of
the exogenous variables xt, weighted by parameter vector α1 in regime
G and by vector α2 in regime H. We note that the NNSTRS model has
a direct linear component in which the exogenous variables are weighted
by parameter vector α, and a nonlinear component, given by time-varying
combinations of the two neurons, weighted by the parameter β.
The linear model is the simplest model, and the NNSTRS model is the
most complex. We see that the NNSTRS nests the linear model. If the
nonlinear regime switching effects are not significant, the parameter β = 0,
so that it reduces to the linear model. The STRS model is almost linear,
in the sense that the only nonlinear component is the logistic smooth-
transition component Ψt. However, the STRS model nests the linear model
only in a very special sense. With θ = c = 0, Ψt = .5 for all t, so that the
dependent variable is a linear combination of two linear models and thus a
linear model. However, the NNSTRS does not nest the STRS model.
We estimate these three models by maximum likelihood methods. The
linear model and the STRS models are rather straightforward to estimate.
However, for the NNSTRS model the parameter set is larger. For this
reason we make use of the hybrid evolutionary search (genetic algorithm)
method and quasi-Newton gradient-descent methods. We then evaluate the
relative performance of the three models by in-sample diagnostic checks,
out-of-sample forecast accuracy, and the broader meaning and significance
of the results.
6.1.3
In-Sample Performance
We first estimate the model for the whole sample period and assess the per-
formance of the three models. Figure 6.2 pictures the errors of the models.
The smooth lines represent the linear model, the dashed are for the STRS

6.1 Forecasting Production in the Automotive Industry
151
1994
1995
1996
1997
1998
1999
2000
2001
2002
−0.3
−0.25
−0.2
−0.15
−0.1
−0.05
0
0.05
0.1
0.15
0.2
Linear
STRS
NNSTRS 
FIGURE 6.2. In-sample performance: rate of growth of automobile production
model, and the dotted curves are for the NNSTRS model. We see that the
errors of the linear model are the largest, but they all are highly correlated
with each other.
Table 6.2 summarizes the overall in-sample performance of the three
models. We see that the NNSTRS model does not dominate the other
STRS on the basis of the Hannan-Quinn selection criterion. For all three
models we cannot reject serial independence, both in the residuals and
in the squared residuals. Furthermore, the diagnostics on neglected non-
linearity are weakest on the linear model, but not by much, relative to
the nonlinear models. All three models reject normality in the regression
residuals.
6.1.4
Out-of-Sample Performance
We divided the sample in half and re-estimated the model in a recursive
fashion for the last 53 observations. The real-time forecast errors appear
in Figure 6.3. Again, the solid curves are for the linear errors, the dashed
curves for the STRS model and the dotted curves are for the NNSTRS
model. We see, for the most part, the error paths are highly correlated.

152
6. Times Series: Examples from Industry and Finance
TABLE 6.2. In-sample Diagnostics of Alternative Models (Sample: 1992–2002,
Monthly Data)
Diagnostics
Models
Linear
STRS
NNRS
SSE
0.615
0.553
0.502
RSQ
0.528
0.612
0.645
HQIF
−25.342
−22.714
−32.989
LB*
0.922
0.958
0.917
ML*
0.532
0.553
0.715
JB*
0.088
0.008
0.000
EN*
0.099
0.256
0.431
BDS*
0.045
0.052
0.051
LWG
0
0
0
*: prob value
NOTE:
SSE: Sum of squared errors
RSQ: R-squared
HIQF: Hannan-Quinn information criterion
LB: Ljung-Box Q statistic on residuals
ML: McLeod-Li Q statistic on squared residuals
JB: Jarque-Bera statistic on normality of residuals
EN: Engle-Ng test of symmetry of residuals
BDS:Brock-Deckert-Scheinkman test of nonlinearity
LWG: Lee-White-Granger test of nonlinearity
Table 6.3 summarizes the out-of-sample forecasting statistics of the three
models. The root mean squared error statistics show the STRS model is
the best, while the success ratio for correct sign prediction shows that the
NNSTRS model is the winner. However, the differences between the two
alternatives to the linear model are not very significant.
Table 6.3 has three sets of Diebold-Mariano statistics which compare,
pair-wise, the three models against one another. Not surprisingly, given the
previous information, the STRS and the NNSTRS errors are significantly
better than the linear model, but they are not significantly different from
each other.
6.1.5
Interpretation of Results
What do the models tell us in terms of economic understanding of the deter-
minants of automotive production? To better understand the message of
the models, we calculated the partial derivatives based on three states: the
beginning of the sample, the mid-point, and the final observation. We also
used the bootstrapping method to determine the statistical significance of
these estimates.

6.1 Forecasting Production in the Automotive Industry
153
1997
1997.5
1998
1998.5
1999
1999.5
2000
2000.5
2001
2001.5
2002
−0.5
−0.4
−0.3
−0.2
−0.1
0
0.1
0.2
0.3
0.4
Linear
STRS 
NNSTRS 
FIGURE 6.3.
TABLE 6.3. Out-of-Sample Forecasting Accuracy
Diagnostics
Models
Linear
STRS
NNSTRS
RMSQ
0.180
0.122
0.130
SR
0.491
0.679
0.698
Diebold-
Linear vs.
Linear vs.
STRS vs.
Mariano Test
STRS
NNSTRS
NNSTRS
DM-1*
0.000
0.000
0.941
DM-2*
0.000
0.002
0.899
DM-3*
0.000
0.005
0.874
DM-4*
0.000
0.009
0.857
DM-5*
0.000
0.013
0.853
*: prob value
RMSQ: Root mean squared error
SR: Success ratio on sign correct sign predictions
DM: Diebold-Mariano Test
(correction for autocorrelation, lags 1-5)

154
6. Times Series: Examples from Industry and Finance
TABLE 6.4. Partial Derivatives of NNSTRS Model
Period
Arguments
Production
Price
Interest
Income
Mean
0.143
0.089
−0.450
0.249
1992
0.140
0.090
−0.458
0.249
1996
0.137
0.091
−0.455
0.248
2001
0.144
0.089
−0.481
0.250
Period
Statistical Significance of Estimates Arguments
Production
Price
Interest
Income
Mean
0.981
0.571
0.000
0.015
1992
0.968
0.558
0.000
0.001
1996
0.956
0.573
0.000
0.008
2001
0.958
0.581
0.000
0.008
The results appear in Table 6.4 for the NNSTRS model. We see that
the partial derivatives of the mortgage rate and disposable income have
the expected correct sign values and are statistically significant (based
on bootstrapping) at the beginning, mid-point, and end-points of the
sample, as well as for the mean values of the regressors. However, the
partial derivatives of both the lagged production and the price are statis-
tically significant. The message of the NNSTRS model is that aggregate
macroeconomic variables are more important for predicting developments
in automobile production than are price or lagged production developments
within the industry itself.
The results from the STRS models are very similar, both in magnitude
and tests of significance. These results appear in Table 6.5.
Finally, what information can we glean from the behavior of the smooth
transition neurons in the two regime switching models? How do they behave
relative to changes in disposable income? Figure 6.4 pictures the behav-
ior of these three variables. We see that disposable income only becomes
negative at the mid-point of the sample but at several points it is close
to zero. The NNSTRS and STRS neurons give about equal weight to
the growth/recession states, but the NNSTRS neuron shows slightly more
volatility throughout the sample.
Given the superior performance of the STRS and NNSTRS models rela-
tive to the linear model, the information in Figure 6.4 indicates that most
of the nonlinearity in the automotive industry has not experienced major
switches in regimes. However, the neurons in both the STRS and NNSTRS
model appear to detect nonlinearities which aid in forecasting performance.

6.1 Forecasting Production in the Automotive Industry
155
TABLE 6.5. Partial Derivatives of STRS Model
Period
Arguments
Production
Price
Interest
Income
Mean
0.187
0.094
−0.448
0.296
1992
0.186
0.096
−0.449
0.291
1996
0.185
0.098
−0.450
0.286
2001
0.188
0.092
−0.448
0.299
Period
Statistical Significance of Estimates Arguments
Production
Price
Interest
Income
Mean
0.903
0.587
0.000
0.000
1992
0.905
0.575
0.000
0.000
1996
0.891
0.581
0.000
0.000
2001
0.893
0.589
0.000
0.000
1994
1995
1996
1997
1998
1999
2000
2001
2002
−0.04
−0.02
0
0.02
0.04
0.06
1994
1995
1996
1997
1998
1999
2000
2001
2002
0.44
0.46
0.48
0.5
0.52
0.54
0.56
Rate of Growth of Disposable Income 
Transition Neurons 
NNSTRS Model
STRS Model
FIGURE 6.4. Regime transitions in STRS and NNSTRS models


## Risk Premium in Foreign Exchange

156
6. Times Series: Examples from Industry and Finance
6.2
Corporate Bonds: Which Factors Determine
the Spreads?
The default rates of high-risk corporate bonds and the evolution of the
spreads on the returns on these bonds, over ten-year government bond
yields, appear in Figure 6.5.
What is most interesting about the evolution of both of these variables is
the large upswing that took place at the time of the Gulf War recession in
1991, with the default rate appearing to lead the return spread. However,
after 1992, both of these variables appear to move in tandem, without any
clear lead or lag relation, with the spread variable showing slightly greater
volatility after 1998. One fact emerges: the spreads declined rapidly in the
early 90s, after the Gulf War recession, and started to increase in the late
1990s, after the onset of the Asian crisis in late 1997. The same is true of
the default rates.
What is the cause of the decline in the spreads and the subsequent
upswing of this variable? The process of financial market development may
lead to increased willingness to take risk, as lenders attempt to achieve
1986
1988
1990
1992
1994
1996
1998
2000
2002
0
0.02
0.04
0.06
0.08
0.1
0.12
0.14
0.16
0.18
Spreads
Default Rates
FIGURE 6.5. Corporate bond spreads and default rates

6.2 Corporate Bonds: Which Factors Determine the Spreads?
157
gains by broader portfolio diversification, which could explain a gradual
decline, as lenders become less risk averse. Another factor may be the
spillover effects from increases or decreases in the share market, as well
as increased optimism or pessimism from the rate of growth of industrial
production or from changes in confidence in the economy. These latter two
variables represent business climate effects.
Collin-Dufresne, Goldstein, and Martin (2000) argue against macroeco-
nomic determinants of credit spread changes in the U.S. corporate bond
market. Their results suggest that the “corporate bond market is a seg-
mented market driven by corporate bond specific supply/demand shocks”
[Collin-Dufresne, Goldstein, and Martin (2000), p. 2]. In their view, the
corporate default rates, representing “bond specific shocks,” should be the
major determinant of changes in spreads. They do find, however, that share
market returns are negative and statistically significant determinants of
the spreads. Like many previous studies, their analysis is based on linear
regression methods.
6.2.1
The Data
We are interested in determining how these spreads respond to their own
and each other’s lagged values, to bond specific shocks such as default rates,
as well as to key macroeconomic variables often taken as leading indicators
of aggregate economic activity or the business climate: the real exchange
rate, the index of industrial production (IIP), the National Association of
Product Manufacturers’ Index (NAPM), and the Morgan Stanley Capital
International Index of the U.S. Share Market (MSCI). All of these variables,
presented as annualized rates of change, appear in Figure 6.6.
Table 6.6 contains a statistical summary of these data. As in the previous
example, we transform the spreads and default rates as annualized changes.
We see in this table that over the 15-year period, 1987–2002, the average
annualized change in the spread and the default rate is not very much.
However, the volatility of the default rate is about three times higher. Of
the macroeconomic and business climate indicators, we see that the largest
growth, by far, took place in the MSCI index during this period of time. It
also has the highest volatility.
The correlation matrix in Table 6.6 shows that the spreads are most
highly negatively correlated with the NAPM index and most highly posi-
tively correlated with the default rate. In turn, the default rate is negatively
correlated with changes in the index of industrial production (IIP).
6.2.2
A Model for the Adjustment of Spreads
We again use three models: a linear model, a smooth-transition regime
switching model, and a neural network smooth-transition regime switching

158
6. Times Series: Examples from Industry and Finance
1988
1990
1992
1994
1996
1998
2000
2002
−0.2
0
0.2
1988
1990
1992
1994
1996
1998
2000
2002
−0.5
0
0.5
1988
1990
1992
1994
1996
1998
2000
2002
−0.5
0
0.5
1988
1990
1992
1994
1996
1998
2000
2002
−0.1
0
0.1
NAPM Index 
Real Exchange Rate
MSCI Share Market Index 
Index of Industrial Production 
FIGURE 6.6. Annualized rates of change of macroeconomic indicators
TABLE 6.6. Annualized Changes of Financial Sector Indicators, 1987–2002
Spread Default Rate Real. Ex. Rate NAPM Index MSCI Index
IIP
Mean
0.0021
0.0007
0.0129
−0.0181
0.1012
0.0288
Std. Dev.
0.0175
0.0363
0.0506
0.1334
0.1466
0.0317
Correlation Matrix
Spread Default Rates Real. Ex. Rate NAPM Index MSCI Index
IIP
Spread
1
Default Rate
0.3721
1
Real. Ex. Rate
0.1221
0.0286
1
NAPM Index −0.6502
−0.2335
−0.0277
1
MSCI Index
−0.0838
0.0067
0.2427
0.1334
1
IIP
−0.1444
−0.4521
−0.1181
0.3287
0.4258
1
model (discussed in Section 2.5). Again we are working with monthly data,
and we are interested in the year-on-year changes in these data. When
forecasting the spread, financial market participants are usually interested
in one-month or even shorter horizons.

6.2 Corporate Bonds: Which Factors Determine the Spreads?
159
Letting st represent the spread between corporate and U.S. government
bonds at time t, we forecast the following variable:
∆st+h = st+1 −st
(6.22)
where h = 1 for a one-period forecast with monthly data.
The dependent variable ∆st+h depends on the following set of current
variables xt
xt = [∆12drt, ∆st, ∆12rext, ∆12iipt, ∆12mscit, ∆12napmt] (6.23)
∆drt = drt −drt−1
(6.24)
∆12rext = ln(REXt) −ln(REXt−12)
(6.25)
∆12iipt = ln(IIPt) −ln(IIPt−12)
(6.26)
∆12mscit = ln(MSCIt) −ln(MSCIt−12)
(6.27)
∆12iipt = ln(NAPMt) −ln(NPAMt−12)
(6.28)
where ∆12drt, ∆st, ∆12rext, ∆12iipt, ∆12mscit, and ∆12napmt signify the
currently observed changes in the default rate, the spreads, the index of
industrial production, the MSCI stock index, and the NAPM index at time
t. Since we work with monthly data, we use 12-month changes for the main
macroeconomic indicators to smooth out seasonal factors.
The linear model has the following specification:
∆qt+h = αxt + ηt
(6.29)
ηt = ϵt + γ(L)ϵt−1
(6.30)
ϵt ∼N(0, σ2)
(6.31)
The disturbance term ηt consists of a current period white-noise shock
ϵt in addition to eleven lagged values of this shock, weighted by the vector
γ. We explicitly model serial dependence as a moving average process as in
the previous case.
We compare this model with the smooth-transition regime switch-
ing (STRS) model and then with the neural network smooth-transition
regime switching (NNSTRS) model.
The STRS model has the following
specification:
∆qt+h = Ψtα1xt + (1 −Ψt)α2xt + ηt
(6.32)

160
6. Times Series: Examples from Industry and Finance
Ψt = Ψ(θ · ∆yt −c)
(6.33)
= 1/[1 + exp(θ · ∆yt −c)]
(6.34)
ηt = ϵt + γ(L)ϵt−1
(6.35)
ϵt ∼N(0, σ2)
(6.36)
where Ψt is a logistic or logsigmoid function of the rate of growth of dis-
posable income, ∆yt, as well as the threshold parameter c and smoothness
parameter θ. For simplicity, we set c = 0, thus specifying two regimes, one
when disposable income is growing and the other when it is shrinking.
The NNSTRS model has the following form:
∆qt+h = αxt + β[ΨtG(xt; α1) + (1 −Ψt)H(xt; α2)] + ηt
(6.37)
Ψt = Ψ(θ · ∆yt −c)
(6.38)
= 1/[1 + exp(θ · ∆yt −c)]
(6.39)
G(xt; α1) = 1/[1 + exp(−α1xt)]
(6.40)
H(xt; α2) = 1/[1 + exp(−α2xt)]
(6.41)
ηt = ϵt + γ(L)ϵt−1
(6.42)
ϵt ∼N(0, σ2)
(6.43)
6.2.3
In-Sample Performance
Figure 6.7 pictures the in-sample performance of the three models. We
see that the linear predictions are clear outliers with respect to the two
alternative models, especially at the time of the first Gulf War in late 1991.
The diagnostics appear in Table 6.7. We see a drastic improvement in
performance as we abandon the linear model in favor of either the STRS or
NNSTRS models. The Ljung-Box statistics indicate the presence of serial
correlation in the linear model while we cannot reject independence in the
alternatives. Both the Brock-Deckert-Scheinkman and Lee-White-Granger
tests indicate the presence of neglected nonlinearities in the residuals of the
linear model, but not in the residuals of the alternative models.
6.2.4
Out-of-Sample Performance
We again divided the sample in half and re-estimated the model in a
recursive fashion for the last 86 observations. The real-time forecast errors
appear in Figure 6.8. Again, the solid curves are for the linear errors, the
dashed curves for the STRS model, and the dotted curves for the NNSTRS
model. We see, for the most part, the error paths are highly correlated

6.2 Corporate Bonds: Which Factors Determine the Spreads?
161
1988
1990
1992
1994
1996
1998
2000
2002
−0.025
−0.02
−0.015
−0.01
−0.005
0
0.005
0.01
0.015
0.02
0.025
NNRS
Model
Linear Model
STRS Model
FIGURE 6.7. In-sample performance, change in bond spreads
with the two alternative models. However, large prediction error differences
emerge in the mid-1990s, late 1990s, and late 2001.
Table 6.8 summarizes the out-of-sample forecasting statistics of the three
models. The root mean squared error statistics show the STRS models as
the best, while the success ratio for correct sign predictions (for the pre-
dicted change in the corporate bond spreads) shows that the STRS model
is also the winner. However, the differences between the two alternatives
to the linear model are not very significant.
Table 6.8 has three sets of Diebold-Mariano statistics which compare,
pair-wise, the three models against one another. Again, the STRS and the
NNSTRS errors are significantly better than the linear model, but they are
not significantly different from each other.
6.2.5
Interpretation of Results
What do the models tell us in terms of economic understanding of the deter-
minants of automotive production? To better understand the message of
the models, we calculated the partial derivatives based on three states: the
beginning of the sample, the mid-point, and the final observation. We also

162
6. Times Series: Examples from Industry and Finance
TABLE 6.7. In-Sample Diagnostics of Alternative Models
(Sample: 1988–2002, Monthly Data)
Diagnostics
Models
Linear
STRS
NNRS
SSE
0.009
0.003
0.003
RSQ
0.826
0.940
0.943
HQIF
−763.655
−932.234
−937.395
LB*
0.000
0.980
0.948
ML*
0.276
0.792
0.875
JB*
0.138
0.000
0.000
EN*
0.005
0.712
0.769
BDS*
0.000
0.338
0.297
LWG
798
0
0
*: prob value
NOTE:
SSE: Sum of squared errors
RSQ: R-squared
HIQF: Hannan-Quinn Information Criterion
LB: Ljung-Box Q statistic on residuals
ML: McLeod-Li Q statistic on squared residuals
JB: Jarque-Bera statistic on normality of residuals
EN: Engle-Ng test of symmetry of residuals
BDS:Brock-Deckert-Scheinkman test of nonlinearity
LWG: Lee-White-Granger test of nonlinearity
used the bootstrapping method to determine the statistical significance of
these estimates.
The results appear in Table 6.9 for the NNSTRS model. We see signifi-
cant and relatively strong persistence in the spread, in that current spreads
have strong positive effects on the next period’s spreads. We see that the
effect of defaults is small and insignificant. The real exchange rate and
industrial production effects are both positive and significant, while the
effects of changes in the MSCI and NAPM indices are negative. In the
NNSTRS model, however, the MSCI effect is not significant.
The message of the NNSTRS model is that aggregate macroeconomic
variables are as important for predicting developments in spreads as
are market-specific developments, since both the real exchange rate and
changes in the NAPM, IIP, and lagged spreads play a significant role.
The results from the STRS models are very similar, both in magnitude
and tests of significance. The only difference appears in the significance of
the MSCI effect, which is significant in this model. This result is consistent
with the findings of Collin-Dufresne, Goldstein, and Martin (2000). These
results appear in Table 6.10.

6.2 Corporate Bonds: Which Factors Determine the Spreads?
163
1995
1996
1997
1998
1999
2000
2001
2002
−0.05
−0.04
−0.03
−0.02
−0.01
0
0.01
0.02
0.03
0.04
NNSTRS
Model
STRS Model
Linear Model
FIGURE 6.8. Forecasting performance of models
TABLE 6.8. Out-of-Sample Forecasting Accuracy
Diagnostics
Models
Linear
STRS
NNSTRS
RMSQ
0.015
0.006
0.007
SR
0.733
0.917
0.905
Diebold-Mariano
Linear vs.
Linear vs.
STRS vs.
Test
STRS
NNSTRS
NNSTRS
DM-1*
0.000
0.000
0.942
DM-2*
0.000
0.000
0.943
DM-3*
0.000
0.000
0.939
DM-4*
0.001
0.001
0.936
DM-5*
0.002
0.002
0.897
*: prob value
RMSQ: Root mean squared error
SR: Success ratio on correct sign predictions
DM: Diebold-Mariano Test
(correction for autocorrelation, lags 1–5)

164
6. Times Series: Examples from Industry and Finance
TABLE 6.9. Partial Derivatives of NNSTRS Model
Period
Arguments
Default
Spread
REXR
IIP
MSCI
NAPM
Mean
0.033
0.771
0.063
0.134
−0.068
−0.066
1989
0.033
0.769
0.060
0.137
−0.065
−0.068
1996
0.030
0.777
0.071
0.128
−0.073
−0.061
2001
0.036
0.756
0.043
0.151
−0.053
−0.080
Statistical Significance of Estimates
Period
Arguments
Default
Spread
REXR
IIP
MSCI
NAPM
Mean
0.853
0.000
0.000
0.000
0.678
0.059
1989
0.844
0.000
0.000
0.000
0.688
0.055
1996
0.846
0.000
0.000
0.000
0.680
0.063
2001
0.848
0.000
0.000
0.000
0.684
0.055
TABLE 6.10. Partial Derivatives of STRS Model
Period
Arguments
Default
Spread
REXR
IIP
MSCI
NAPM
Mean
0.017
0.749
0.068
0.125
−0.139
−0.096
1989
0.010
0.752
0.070
0.128
−0.139
−0.098
1996
0.027
0.746
0.065
0.121
−0.138
−0.090
2001
−0.005
0.757
0.074
0.135
−0.140
−0.106
Statistical Significance of Estimates
Period
Arguments
Default
Spread
REXR
IIP
MSCI
NAPM
Mean
0.678
0.000
0.000
0.000
0.080
0.000
1989
0.699
0.000
0.000
0.000
0.040
0.000
1996
0.636
0.000
0.011
0.000
0.168
0.000
2001
0.693
0.000
0.000
0.000
0.057
0.000
Finally, we can ask what information we can glean from the behav-
ior of the smooth transition neurons in the two regime switching models.
How do they behave relative to changes in the IIP as the economy
switches from growth to recession? Figure 6.9 pictures the behavior of these

6.3 Conclusion
165
1988
1990
1992
1994
1996
1998
2000
2002
−0.1
−0.05
0
0.05
0.1
1988
1990
1992
1994
1996
1998
2000
2002
0.4
0.45
0.5
0.55
0.6
0.65
Rate of Growth of Index of Industrial Production 
Smooth Transition Neurons 
STRS Model
NNSTRS Model
FIGURE 6.9. Regime transitions in STRS and NNSTRS models
three variables. We see sharper changes in the IIP index than in dispos-
able income. The NNSTRS and STRS neurons give about equal weight to
the growth/recession states, but the NNSTRS neuron shows slightly more
volatility, and thus more information, throughout the sample about the
likelihood of switching from one regime to another.
6.3
Conclusion
The examples we studied in this chapter are not meant, by any means, to
be conclusive. The models are very simple and certainly capable of more
elaborate extension, both in terms of the specification of the variables and
in the specification of the nonlinear neural network alternatives to the linear
model. However both of the examples illustrate the gains from using the
nonlinear neural network specification, even in a simple alternative model.
We get greater accuracy in forecasting and results with respectable in-
sample diagnostics, which can lead to meaningful economic interpretation.

166
6. Times Series: Examples from Industry and Finance
6.3.1
MATLAB Program Notes
The complete estimation program for the automobile industry and
the spread forecasting exercises is called carlos may2004.m. Subfunc-
tions are linearmodfun.m, nnstrsfun.m, and strsfun.m, with the spec-
ification of a moving average process, for the linear, neural network
smooth-transition regime switching, and smooth-transition regime switch-
ing models.
The data for the corporate bond spreads are given in
carlos spread may2004 run1.mat, while the automobile industry data are
given in jerryauto may2004 run1.mat.
6.3.2
Suggested Exercises
The reader is invited to modify the MATLAB programs and to forecast
price adjustment, rather than quantity adjustment, in the automotive
industry, and to forecast default rates, rather than corporate bond spreads,
with the financial times-series data.

7
Inflation and Deflation: Hong Kong
and Japan
This chapter applies neural network methods to the Hong Kong and
Japanese experiences of inflation and deflation. Understanding the dynam-
ics of inflation and how to forecast inflation more accurately is not simply of
interest to policymakers at a central bank. Proper pricing of rates of return
over the medium-term horizon requires accurate estimates of inflation in
the coming quarters. Similarly, many decisions about lending or borrow-
ing at short- or long-term interest rates requires a reasonable forecast of
what succeeding short-term interest rates will be. These short-term interest
rates, of course, will likely follow future inflationary developments, if the
central bank is doing its job as a guardian of price stability. Forecasting
inflation accurately means a better forecast of future interest rates and
actions of the monetary authority.
Deflation poses a special problem. While at first glance the idea of falling
prices appears to be good news, the zero lower bound on nominal inter-
est rates means that real interest rates will start to rise sharply after the
nominal interest rate hits its zero lower bound, if the deflation process con-
tinues. Rising real interest rates mean, of course, less investment and a
fall in demand in the economy. Furthermore, a deflation process can gen-
erate self-fulfilling expectations. Once prices start to fall, people refrain
from buying in the expectation that prices will continue to fall. The lack
of buying, of course, causes prices to fall even more.

168
7. Inflation and Deflation: Hong Kong and Japan
The dynamics of deflation raise many questions about the overall sta-
tistical process of inflation. When inflation is positive, we expect rising
interest rates to reduce the inflationary pressures in the economy. However,
in deflation, interest rates cannot fall below zero to reverse the deflationary
pressure. There is an inherent asymmetry in the price adjustment process
as we move from an inflationary regime to a deflationary regime. This is
where we can expect nonlinear approximation methods to be of help.
While most studies of deflation have looked back to the Great Depression
era, we have the more recent experiences of Hong Kong and Japan as new
sources of information about how deflationary processes come about. While
there has been great debate about the experiences of these countries, and
no shortage of proposed policy remedies, there has been little examination
of the inflationary/deflationary dynamics with nonlinear neural network
approximation methods.
7.1
Hong Kong
Although much has been written (amid much controversy and debate)
about deflation in Japan, which we discuss in Section 7.2, Hong Kong is of
special interest. First, the usual response of expansionary monetary policy
is not an option for Hong Kong, since its currency board arrangement pre-
cludes active policy directed at inflation or deflation. Second, Hong Kong is
a smaller but much more open economy than Japan, and is thus more sus-
ceptible to external factors. Finally, Hong Kong, as a special administrative
region, is in the process of increasing market integration with mainland
China. However, there are some important similarities. Both Japan and
Hong Kong have experienced significant asset-price deflation, especially in
property prices, and more recently, negative output-gap measures.
Ha and Fan (2002) examined panel data for assessing price conver-
gence between Hong Kong and mainland China. While convergence is far
from complete, they showed that the pace has accelerated in recent years.
However, comparing price dynamics between Hong Kong and Shenzhen,
Schellekens (2003) argued that the role of price equalization as a source of
deflation is minor, and contended that deflation is best explained by wealth
effects.
Genberg and Pauwels (2003) found that both wages and import prices
have significant causal roles, in addition to property rental prices. These
three outperform measures of excess capacity as forcing variables for defla-
tion. Razzak (2003) also called attention to the role of unit labor costs and
productivity dynamics for understanding deflation. However, making use
of a vector autoregressive model (VAR), Genberg (2003) also reported that
external factors account for more than 50% of unexpected fluctuations in
the real GDP deflator at horizons of one to two years.

7.1 Hong Kong
169
1986
1988
1990
1992
1994
1996
1998
2000
2002
−0.08
−0.06
−0.04
−0.02
0
0.02
0.04
0.06
0.08
0.1
0.12
FIGURE 7.1. CPI inflation: Hong Kong
Most of these studies have relied on linear extensions and economet-
ric implementation of the Phillips curve or New Keynesian Phillips curve.
While such linear applications are commonly used and have been successful
for many economies, we show in this chapter that a nonlinear smooth-
transition neural network regime switching method outperforms the linear
model on the basis of in-sample diagnostics and out-of-sample forecasting
accuracy.
7.1.1
The Data
Figure 7.1 pictures the rate of inflation in Hong Kong. We see that the
deflation process set in around 1998, reaching a rate of negative 6% by
1999. The country has not yet moved out of this pattern.
In this chapter, we examine the output gap, the rates of growth of import
prices and unit labor costs, two financial sector indicators — the rates of
growth of the Hang Seng index and residential property prices — and the
price gap between Hong Kong and mainland China.
The output gap, which measures either excess demand or slack in
the economy, comes from the World Economic Outlook of the IMF.

170
7. Inflation and Deflation: Hong Kong and Japan
1986
1988
1990
1992
1994
1996
1998
2000
2002
−0.05
−0.04
−0.03
−0.02
−0.01
0
0.01
0.02
0.03
0.04
0.05
FIGURE 7.2. Output gap: Hong Kong
This variable was interpolated from annual to quarterly frequency.
Figure 7.2 pictures the evolution of this variable. We see that measures
of the output gap show that the economy has been well below potential for
most of the time since late 1998.
The behavior of import prices and unit labor costs, both important for
understanding the supply-side or costs factors of inflationary movements,
shows considerably different patterns of volatility. Figure 7.3 pictures the
rate of growth of import prices and Figure 7.4 shows the corresponding
movement in labor costs. The collapse of import prices in the year 2001
is mainly due to the world economic downturn following the burst of the
bubble in the high-technology sectors.
Figure 7.5 pictures the financial sector variables, the rates of growth of
the share price index (the Hang Seng index), and the residential property
price index. Not surprisingly, the growth rate of the share price index shows
much more volatility than the corresponding growth rate of the property
price index.
Finally, as a measure of structural market integration and price con-
vergence with mainland China, we picture the evolution of a price gap.

1986
1988
1990
1992
1994
1996
1998
2000
2002
−0.8
−0.6
−0.4
−0.2
0
0.2
0.4
0.6
0.8
FIGURE 7.3. Rate of growth of import prices: Hong Kong
1986
1988
1990
1992
1994
1996
1998
2000
2002
0
0.05
0.1
0.15
0.2
0.25
0.3
0.35
FIGURE 7.4. Rate of growth of unit labor costs: Hong Kong


## Forecasting Financial Time Series

172
7. Inflation and Deflation: Hong Kong and Japan
1986
1988
1990
1992
1994
1996
1998
2000
2002
2004
−0.8
−0.6
−0.4
−0.2
0
0.2
0.4
0.6
0.8
Rate of growth of 
residential property 
prices 
Rate of growth of 
Hang Seng Index 
FIGURE 7.5. Financial market indicators: Hong Kong
The gap is defined as the logarithmic difference between the Hong Kong
CPI and mainland China CPI. The latter is converted to the Hong Kong
dollar basis using the market exchange rate. If there is significant conver-
gence taking place, we expect a negative relationship between the price gap
and inflation. If there is an unexpected and large price differential between
Hong Kong and China, ceteris paribus, the inflation rate in Hong Kong
should fall over time to close the gap. This variable appears in Figure 7.6.
Figure 7.6 shows that the price gap after 1998 is slowly but steadily
falling. The jump in 1994 is due to the devaluation of the Chinese Renminbi
against the U.S. dollar.
Table 7.1 contains a statistical summary of the data we use in our analy-
sis. We use quarterly observations from 1985 until 2002. Table 7.1 lists the
means, standard deviations, and contemporaneous correlations of annual-
ized rates of inflation, the price and output gap measures, and the rates of
growth of import prices, the property price index, the share price index,
and unit labor costs.
The highest volatility rates (measured by the standard deviations of the
annualized quarterly data) are for the rates of growth of the share market

7.1 Hong Kong
173
1986
1988
1990
1992
1994
1996
1998
2000
2002
−0.1
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
FIGURE 7.6. Price gap: Hong Kong and mainland China
and residential property price indices, as well as the price gap. However,
the price gap volatility is due in large part to the once-over Renminbi
devaluation in 1994.
Table 7.1 also shows that highest correlations of inflation are with rates of
growth of unit labor costs and property prices, followed closely by the out-
put gap. Finally, Table 7.1 shows a strong correlation between the growth
rates of the share price and the residential property price indices.
In many studies relating to monetary policy and overall economic activ-
ity, bank lending appears as an important credit channel for assessing
inflationary or deflationary impulses. Gerlach and Peng (2003) examined
the interaction between banking credit and property prices in Hong Kong.
They found that property prices are weakly exogenous and determine bank
lending, while bank lending does not appear to influence property prices
[Gerlach and Peng (2003), p. 11]. They argued that changes in bank lending
cannot be regarded as the source of the boom and bust cycle in Hong Kong.
They hypothesized that “changing beliefs about future economic prospects
led to shifts in the demand for property and investments.” With a higher
inelastic supply schedule, this caused price swings, and with rising demand

174
7. Inflation and Deflation: Hong Kong and Japan
TABLE 7.1. Statistical Summary of Data
Hong Kong Quarterly Data, 1985–2002
Property
Price Output Imp Price
Price
HSI
ULC
Inflation
Gap
Gap
Growth
Growth
Growth Growth
Mean
0.055
0.511
0.004
0.023
0.088
0.127
0.102
Std. Dev.
0.049
0.258
0.024
0.051
0.215
0.272
0.062
Correlation Matrix
Property
Price Output Imp Price
Price
HSI
ULC
Inflation
Gap
Gap
Growth
Growth
Growth Growth
Inflation
1.00
Price Gap
−0.39
1.00
Output Gap
0.56
−0.29
1.00
Imp Price Growth
0.15
−0.37
0.05
1.00
Property Price Growth
0.57
−0.42
0.36
0.23
1.00
HSI Growth
0.06
−0.04
−0.15
0.43
0.56
1.00
ULC Growth
0.59
−0.84
0.48
0.29
0.38
−0.09
1.00
for loans, “bank lending naturally responded” [Gerlach and Peng (2003),
p. 11]. For this reason, we leave out the growth rate of bank lending as a
possible determinant of inflation or deflation in Hong Kong.1,2
7.1.2
Model Specification
We draw upon the standard Phillips curve framework used by Stock and
Watson (1999) for forecasting inflation in the United States. They define
the inflation as an h-period ahead forecast. For our quarterly data set, we
set h = 4 for an annual inflation forecast:
πt+h = ln(pt+h) −ln(pt)
(7.1)
1In Japan, the story is different: banking credit and land prices show bidirectional
causality or feedback. The collapse of land prices reduces bank lending, but the collapse
of bank lending also leads to a fall in land prices. Hofmann (2003) also points out, with a
sample of 20 industrialized countries, that “long run causality runs from property prices
to bank lending” but short-run bidirectional causality cannot be ruled out.
2Goodhard and Hofmann (2003) support the finding of Gerlach and Peng with results
from a wider sample of 12 countries.

7.1 Hong Kong
175
We thus forecast inflation as an annual forecast (over the next four quar-
ters), rather than as a one-quarter ahead forecast. We do so because
policymakers are typically interested in the inflation prospects over a longer
horizon than one quarter. For the most part, inflation over the next quarter
is already in process, and changes in current variables will not have much
effect at so short a horizon.
In this model, inflation depends on a set of current variables xt, includ-
ing current inflation πt, lags of inflation, and a disturbance term ηt. This
term incorporates a moving average process with innovations ϵt, normally
distributed with mean zero and variance σ2 :
πt+h = f(xt) + ηt
(7.2)
πt = ln(pt) −ln(pt−h)
(7.3)
ηt = ϵt + γ(L)ϵt−1
(7.4)
ϵt ∼N(0, σ2)
(7.5)
where γ(L) are lag operators. Besides current and lagged values of inflation,
πt, . . . , πt−k, the variables contained in xt include measures of the output
gap, ygap
t
, defined as the difference between actual output yt and potential
output ypot
t
, the (logarithmic) price gap with mainland China pgap
t
, the
rate of growth of unit labor costs (ulc), and the rate of growth of import
prices (imp). The vector xt also includes two financial-sector variables:
changes in the share price index (spi) and the residential property price
index (rpi):
xt = [πt, πt−1, πt−2, . . . , πt−k, ygap
t
, pgap
t
, . . . ,
∆hulct, ∆himpt, ∆hspit, ∆hrpit]
(7.6)
pgap
t
= pHK
t
−pCHINA
t
(7.7)
The operator ∆h for a variable zt represents simply the difference over h
periods. Hence ∆h zt = zt −zt−h. The rates of growth of unit labor costs,
the import price index, the share price index, and the residential property
price index thus represent annualized rates of growth for h = 4 in our
analysis. We do this for consistency with our inflation forecast, which is
a forecast over four quarters. In addition, taking log differences over four
quarters helps to reduce the influence of seasonal factors in the inflation
process.
The disturbance term ηt consists of a current period shock ϵt in addition
to lagged values of this shock. We explicitly model serial dependence, since
it is well known that when the forecasting interval h exceeds the sampling

176
7. Inflation and Deflation: Hong Kong and Japan
interval (in this case we are forecasting for one year but we sample with
quarterly observations), temporal dependence is induced in the disturbance
term. For forecasting four quarters ahead with quarterly data, the error
process is a third-order moving average process.
We specify four lags for the dependent variable. For quarterly data, this
is equivalent to a 12-month lag for monthly data, used by Stock and Watson
(1999) for forecasting inflation.
To make the model operational for estimation, we specify the following
linear and neural network regime switching (NNRS) alternatives.
The linear model has the following specification:
πt+h = αxt + ηt
(7.8)
ηt = ϵt + γ(L)ϵt−1
(7.9)
ϵt ∼N(0, σ2)
(7.10)
We compare this model with the smooth-transition regime switch-
ing (STRS) model and then with the neural network smooth-transition
regime switching (NNSTRS) model. The STRS model has the following
specification:
πt+h = Ψtα1xt + (1 −Ψt)α2xt + ηt
(7.11)
Ψt = Ψ(θ · πt−1 −c)
(7.12)
= 1/[1 + exp(θ · πt−1 −c)]
(7.13)
ηt = ϵt + γ(L)ϵt−1
(7.14)
ϵt ∼N(0, σ2)
(7.15)
The transition function depends on the value of lagged inflation πt−1 as well
as the parameter vector θ and threshold c, with c = 0. We use a logistic or
logsigmoid specification for Ψ(πt−1; θ, c).
We also compare the linear specification within a more general NNRS
model:
πt+h = αxt + β{[Ψ(πt−1; θ, c)]G(xt; κ)
+ [1 −Ψ(πt−1; θ, c)]H(xt; λ)} + ηt
(7.16)
ηt = ϵt + γ(L)ϵt−1
(7.17)
ϵt ∼N(0, σ2)
(7.18)

7.1 Hong Kong
177
The NNRS model is similar to the smooth-transition autoregressive
model discussed in Franses and van Dijk (2000), originally developed by
Ter¨asvirta (1994), and more generally discussed in van Dijk, Ter¨asvirta,
and Franses (2000). The function Ψ(πt−1; θ, c) is the transition function for
two alternative nonlinear approximating functions G(xt; κ) and H(xt; λ).
The transition function is the same as the one used on the STRS model.
Again, for simplicity we set the threshold parameter c = 0, so that the
regimes divide into periods of inflation and deflation. As Franses and van
Dyck (2000) point out, the parameter θ determines the smoothness of
the change in the value of this function, and thus the transition from the
inflation to deflation regime.
The functions G(xt; κ) and H(xt; λ) are also logsigmoid and have the
following representations:
G(xt; κ) =
1
1 + exp[−κxt]
(7.19)
H(xt; λ) =
1
1 + exp[−λxt]
(7.20)
The inflation model in the NNRS model has a core linear component,
including autoregressive terms, a moving average component, and a non-
linear component incorporating switching regime effects, which is weighted
by the parameter β.
7.1.3
In-Sample Performance
Figure 7.7 pictures the in-sample paths of the regression errors. We see that
there is little difference, as before, in the error paths of the two alternative
models to the linear model.
Table 7.2 contains the in-sample regression diagnostics for the three
models. We see that the Hannan-Quinn criteria only very slightly favors
the STRS model over the NNRS model. We also see that the Ljung-Box,
McLeod-Li, Brock-Deckert-Scheinkman, and Lee-White-Granger tests all
call into question the specification of the linear model relative to the STRS
and NNRS alternatives.
7.1.4
Out-of-Sample Performance
Figure 7.8 pictures the out-of-sample forecast errors of the three models.
We see that the greatest prediction errors took place in 1997 (at the time of
the change in the status of Hong Kong to a Special Administrative Region
of the People’s Republic of China).
The out-of-sample statistics appear in Table 7.3. We see that the root
mean squared error statistic of the NNRS model is the lowest. Both the

178
7. Inflation and Deflation: Hong Kong and Japan
1986
1988
1990
1992
1994
1996
1998
2000
2002
−0.04
−0.03
−0.02
−0.01
0
0.01
0.02
0.03
0.04
0.05
Linear
NNRS 
STRS 
FIGURE 7.7. In-sample paths of estimation errors
STRS and NNRS models have much higher success ratios in terms of correct
sign predictions for the dependent variable, inflation. Finally, the Diebold-
Mariano statistics show that the NNRS prediction error path is significantly
different from that of the linear model and from the STRS model.
7.1.5
Interpretation of Results
The partial derivatives and their statistical significant values (based on
bootstrapping) appear in Table 7.4. We see that the statistically significant
determinates of inflation are lagged inflation, the output gap, the price
gap, changes in imported prices, the residential property price index, and
the Hang Seng index. Only unit labor costs are not significant. We also
see that the import price and price gap effects both have become more
important, with the import price derivative increasing from a value of .05
to a value of .13, from 1985 until 2002. This, of course, may reflect the
growing integration of Hong Kong both with China and with the rest of
the world. Residential property price effects have remained about the same.

7.1 Hong Kong
179
TABLE 7.2. In-Sample Diagnostics of Alternative Models (Sample: 1985–2002,
Quarterly Data)
Diagnostics
Models
Linear
STRS
NNRS
SSE
0.016
0.002
0.002
RSQ
0.965
0.983
0.963
HQIF
−230.683
−324.786
−327.604
LB*
0.105
0.540
0.316
ML*
0.010
0.204
0.282
JB*
0.282
0.856
0.526
EN*
0.441
0.792
0.755
BDS*
0.099
0.929
0.613
LWG
738
7
17
*: prob value
Note:
SSE: Sum of squared errors
RSQ: R-squared
HIQF: Hannan-Quinn information criterion
LB: Ljung-Box Q statistic on residuals
ML: McLeod-Li Q statistic on squared residuals
JB: Jarque-Bera statistic on normality of residuals
EN: Engle-Ng test of symmetry of residuals
BDS:Brock-Deckert-Scheinkman test of nonlinearity
LWG: Lee-White-Granger test of nonlinearity
For the sake of comparison, Table 7.5 pictures the corresponding infor-
mation from the STRS model. The tests of significance are the same as in
the NNRS model. The main differences are that the residential property
price, import price, and output gap effects are stronger. But there is no
discernible trend in the values of the significant partial derivatives as we
move from the beginning of the sample period toward the end.
Figure 7.9 pictures the evolution of the smooth-transition neurons for the
two models as well as the rate itself. We see that the neuron for the STRS
model is more variable, showing a low probability of deflation in 1991, .4,
but a much higher probability of deflation, .55, in 1999. The NNRS model
has the probability remaining practically the same. This result indicates
that the NNRS model is using the two neurons with equal weight to pick
up nonlinearities in the overall inflation process independent of any regime
change. If there is any slight good news for Hong Kong, the STRS model
shows a very slight decline in the probability of deflation after 2000.

180
7. Inflation and Deflation: Hong Kong and Japan
1993
1994
1995
1996
1997
1998
1999
2000
2001
−0.08
−0.06
−0.04
−0.02
0
0.02
0.04
Linear
NNRS 
STRS
FIGURE 7.8. Out-of-sample prediction errors
TABLE 7.3. Out-of-Sample Forcasting Accuracy
Diagnostics
Models
Linear
STRS
NNRS
RMSQ
0.030
0.027
0.023
SR
0.767
0.900
0.867
Diebold-Mariano
Linear vs. STRS
Linear vs. NNRS
STRS vs. NNRS
Test
DM-1*
0.295
0.065
0.142
DM-2*
0.312
0.063
0.161
DM-3*
0.309
0.031
0.127
DM-4*
0.296
0.009
0.051
DM-5*
0.242
0.000
0.002
*: prob value
RMSQ: Root mean squared error
SR: Success ratio on sign correct sign predictions
DM: Diebold-Mariano test
(correction for autocorrelation. lags 1–5)

7.1 Hong Kong
181
TABLE 7.4. Partial Derivatives of NNSTRS Model
Period
Arguments
Inflation
Price
Output
Import
Res Prop
Hang Seng
Unit Labor
Gap
Gap
Price
Price
Index
Costs
Mean
0.300
−0.060
0.027
0.086
0.234
0.016
0.082
1985
0.294
−0.056
0.024
0.050
0.226
−0.015
0.072
1996
0.300
−0.060
0.027
0.091
0.235
0.020
0.084
2002
0.309
−0.067
0.032
0.130
0.244
0.053
0.093
Statistical Significance of Estimates
Period
Arguments
Inflation
Price
Output
Import
Res Prop
Hang Seng
Unit Labor
Gap
Gap
Price
Price
Index
Costs
Mean
0.000
0.000
0.015
0.059
0.000
0.032
0.811
1985
0.000
0.000
0.015
0.053
0.000
0.032
0.806
1996
0.000
0.000
0.013
0.034
0.000
0.029
0.819
2002
0.000
0.000
0.015
0.053
0.000
0.032
0.808
TABLE 7.5. Partial Derivatives of STRS Model
Period
Arguments
Inflation
Price
Output
Import
Res Prop
Hang Seng
Unit Labor
Gap
Gap
Price
Price
Index
Costs
Mean
0.312
−0.037
0.093
0.168
0.306
0.055
0.141
1985
0.295
−0.018
0.071
0.182
0.292
0.051
0.123
1996
0.320
−0.046
0.103
0.161
0.312
0.056
0.149
2002
0.289
−0.012
0.063
0.187
0.287
0.050
0.116
Statistical Significance of Estimates
Period
Arguments
Inflation
Price
Output
Import
Res Prop
Hang Seng
Unit Labor
Gap
Gap
Price
Price
Index
Costs
Mean
0.000
0.000
0.000
0.000
0.000
0.000
0.975
1985
0.000
0.000
0.000
0.000
0.000
0.000
0.964
1996
0.000
0.000
0.000
0.000
0.000
0.000
0.975
2002
0.000
0.000
0.000
0.000
0.000
0.000
0.966

182
7. Inflation and Deflation: Hong Kong and Japan
1986
1988
1990
1992
1994
1996
1998
2000
2002
−0.1
−0.05
0
0.05
0.1
0.15
1986
1988
1990
1992
1994
1996
1998
2000
2002
0.4
0.45
0.5
0.55
0.6
0.65
Inflation
Transition Neurons 
STRS
Model
NNRS Model
FIGURE 7.9. Regime transitions in STRS and NNRS models
7.2
Japan
Japan has been in a state of deflation for more than a decade. There is
no shortage of advice for Japanese policymakers from the international
community of scholars.
Krugman (1998) comments on this experience of Japan:
Sixty years after Keynes, a great nation — a country with a stable and
effective government, a massive net creditor, subject to none of the constraints
that lesser economies face — is operating far below its productive capacity,
simply because its consumers and investors do not spend enough. That should
not happen; in allowing it to happen, and to continue year after year, Japan’s
economic officials have subtracted value from their nation and the world as a
whole on a truly heroic scale [Krugman (1998), Introduction].
Krugman recommends expansionary monetary and fiscal policy to cre-
ate inflation. However, Yoshino and Sakakibara have taken issue with
Krugman’s remedies. They counter Krugman in the following way:
Japan has reached the limits of conventional macroeconomic policies.
Lowering interest rates will not stimulate the economy, because widespread

7.2 Japan
183
excess capacity has made private investment insensitive to interest rate changes.
Increasing government expenditure in the usual way will have small effects
because it will take the form of unproductive investment in the rural areas.
Cutting taxes will not increase consumption because workers are concerned
about job security and future pension and medical benefits [Yoshino and
Sakakibara (2002), p. 110].
Besides telling us what will not work, Yoshino and Sakakibara offer
alternative longer-term policy prescriptions, involving financial reform,
competition policy, and the reallocation of public investment:
In order for sustained economic recovery to occur in Japan, the government
must change the makeup and regional allocation of public investment, resolve the
problem of nonperforming loans in the banking system, improve the corporate
governance and operations of the banks, and strengthen the international
competitiveness of domestically oriented companies in the agriculture,
construction and service industries [Yoshino and Sakakibara (2002), p. 110].
Both Krugman and Yoshino and Sakakibara base their analyses and pol-
icy recommendations on analytically simple models, with reference to key
stylized facts observed in macroeconomic data.
Svensson (2003) reviewed many of the proposed remedies for Japan, and
put forward his own way. His “foolproof” remedy has three key ingredients:
first, an upward-sloping price level target path set by the central bank;
second, an initial depreciation followed by a “crawling peg;” and third, an
exit strategy with abandonment of the peg in favor of inflation or price-
level targeting when the price-level target path has been reached [Svensson
(2003), p. 15]. Other remedies include a tax on money holding proposed
by Goodfriend (2000) and Buiter and Panigirtzoglou (1999), as well as
targeting the interest rate on long-term government bonds, proposed by
Clouse et al. (2003) and Meltzer (2001).
The growth of low-priced imports from China has also been proposed
as a possible cause of deflation in Japan (as in Hong Kong). McKibbin
(2002) argued that monetary policy would be effective in Japan through
yen depreciation. He argued for a combination of a fiscal contraction with
a monetary expansion based on depreciation:
Combining a credible fiscal contraction that is phased in over three years with
an inflation target would be likely to provide a powerful macroeconomic
stimulus to the Japanese economy, through a weaker exchange rate and lower
long term real interest rates, and would sustain higher growth in Japan for a
decade [McKibbin (2002), p. 133].
In contrast to Krugman and Yoshino and Sakakibara, McKibbin based
his analysis and policy recommendations on simulation of the calibrated
G-cubed (Asia Pacific) dynamic general equilibrium model, outlined in
McKibbin and Wilcoxen (1998).

184
7. Inflation and Deflation: Hong Kong and Japan
1975
1980
1985
1990
1995
2000
2005
−0.03
−0.02
−0.01
0
0.01
0.02
0.03
0.04
0.05
0.06
0.07
FIGURE 7.10. CPI inflation: Japan
Sorting out the relative importance of monetary policy, stimulus packages
that affect overall demand (measured by the output gap), and the contribu-
tions of unit labor costs, falling imported goods prices, and financial-sector
factors coming from the collapse of bank lending and asset-price defla-
tion (measured by the negative growth rates of share price and land price
indices) is no easy task. These variables display considerable volatility, and
the response of inflation to these variables is likely to be asymmetric.
7.2.1
The Data
Figure 7.10 pictures the CPI inflation rate for Japan. We see that deflation
set in after 1995, with a slight recovery from deflation in 1998.
Figure 7.11 pictures the output gap, while Figures 7.12 and 7.13 contain
the rate of growth of the import price index and unit labor costs. We see
that the collapse of excess demand, measured as a positive output gap, goes
hand-in-hand with the onset of deflation. Unit labor costs also switched
from positive to negative growth rate at the same time. However there is
no noticeable collapse in the import price index at the time of the deflation.

1975
1980
1985
1990
1995
2000
2005
−0.04
0
0.02
−0.02
0.04
0.06
0.08
0.1
FIGURE 7.11. Output gap: Japan
1975
1980
1985
1990
1995
2000
2005
−0.6
−0.4
−0.2
0
0.2
0.4
0.6
0.8
FIGURE 7.12. Rate of growth of import prices: Japan

186
7. Inflation and Deflation: Hong Kong and Japan
1975
1980
1985
1990
1995
2000
2005
0
0.02
−0.02
0.04
−0.04
0.06
0.08
0.1
FIGURE 7.13. Rate of growth of unit labor costs: Japan
Figure 7.14 pictures the rate of growth of two financial market indicators:
the Nikkei index and the land price index. We see that the volatility of the
rate of growth of the Nikkei index is much greater than that of the land
price index.
Figure 7.15 pictures the evolution of two indicators of monetary policy:
the Gensaki interest rate and the rate of growth of bank lending. The
Gensaki interest rate is considered the main interest for interpreting the
stance of monetary policy in Japan. The rate of growth of bank lending is,
of course, an indicator of how banks may thwart expansionary monetary
policy by reducing their lending. We see the sharp collapse of the rate
of growth of bank lending at about the same time the Bank of Japan
raised the interest rates at the beginning of the 1990s. The well-documented
action was an attempt by the Bank of Japan to burst the bubble in the
stock market. Figure 7.14, of course, shows that the Bank of Japan did
indeed succeed in bursting this bubble. After that, however, overall demand
showed a steady decline.
Table 7.6 gives a statistical summary of the data we have examined.
The highest volatility rates (measured by the standard deviations of the

1975
1980
1985
1990
1995
2000
2005
−0.8
−0.6
−0.4
−0.2
0
0.2
0.4
0.6
Rate of Growth
of Nikkei Index 
Rate of Growth of 
Land Price Index 
FIGURE 7.14. Financial market indicators: Japan
1975
1980
1985
1990
1995
2000
2005
−0.04
−0.02
0
0.02
0.04
0.06
0.08
0.1
0.12
Gensaki 
Interest 
Rate 
Rate of Growth of 
Bank Lending 
FIGURE 7.15. Monetary policy indicators: Japan


## Classification in Finance

188
7. Inflation and Deflation: Hong Kong and Japan
TABLE 7.6. Statistical Summary of Data
Inflation Gensaki
Y-gap
Imp
Ulo
Lpi
Spi
Loan
Growth Growth Growth Growth Growth
Mean
0.034
0.052
0.000
0.016
0.004
0.035
0.068
0.077
Std. Dev.
0.043
0.036
0.017
0.193
0.014
0.074
0.202
0.054
Correlation Matrix
Inflation Gensaki
Y-gap
Imp
Ulo
Lpi
Spi
Loan
Growth Growth Growth Growth Growth
Inflation
1.000
Gensaki
0.607
1.000
Y-gap
−0.211
0.309
1.000
Imp Growth
0.339
0.550
0.225
1.000
Ulo Growth
0.492
0.198
−0.052
0.328
1.000
Lpi Growth
0.185
0.777
0.591
0.345
−0.057
1.000
Spi Growth
−0.069
−0.011
−0.286 −0.349
−0.176
0.081
1.000
Loan Growth
0.489
0.823
0.310
0.279
−0.016
0.848
0.245
1.000
annualized quarterly data) are for the rates of growth of the share market
and import price indices.
Table 7.6 shows that the highest correlation of inflation is with the
Gensaki rate, but that it is positive rather than negative. This is another
example of the well-known price puzzle, recently analyzed by Giordani
(2001). This puzzle is also a common finding of linear vector autoregressive
(VAR) models, which show that an increase in the interest rate has positive,
rather than negative, effects on the price level in impulse-response analysis.
Sims (1992) proposed that the cause of the prize puzzle may be unobserv-
able contemporaneous supply shocks. The policymakers observe the shock
and think it will have positive effects on inflation, so they raise the interest
rates in anticipation of countering higher future inflation. Sims found that
this puzzle disappears in U.S. data when we include a commodity price
index in a more extensive VAR model.
Table 7.6 also shows that the second and third highest correlations of
inflation are with unit labor costs and bank lending, followed by import
price growth. The correlations of inflation with the share-price growth rate
and the output gap are negative but insignificant.
Finally, what is most interesting from the information given in Table 7.6
is the very high correlation between the growth rate of bank lending and
the growth rate of the land price index, not the growth rate of the share
price index. It is not clear which way the causality runs: does the collapse
of land prices lead to a fall in bank lending, or does the collapse of bank
lending lead to a fall in land prices?

7.2 Japan
189
TABLE 7.7. Granger Test of Causality: LPI and Loan Growth
Loan Growth Does Not
LPI Growth Does Not
Cause LPI Growth
Cause Loan Growth
F-Statistic
2.429
3.061
P-Value
0.053
0.020
In Japan, the story is different: banking credit and land prices show
bidirectional causality or feedback. The collapse of land prices reduces bank
lending, but the collapse of bank lending also leads to a fall in land prices.
Table 7.7 gives the joint-F statistics and the corresponding P-values for a
Granger test of causality. We see that the results are somewhat stronger for
a causal effect from land prices to loan growth. However, the P-value for
causality from loan growth to land price growth is only very slightly above
5%. These results indicate that both variables have independent influences
and should be included as financial factors for assessing the behavior of
inflation.
7.2.2
Model Specification
We use the same model specification for the Hong Kong deflation as in
7.1.2 with two exceptions: we do not use a price gap variable measur-
ing convergence with mainland China, and we include both the domestic
Gensaki interest rate and the rate of growth of bank lending as further
explanatory variables for the evolution of inflation. As before, we forecast
over a one-year horizon, and all rates of growth are measured as annual
rates of growth, with ∆hxt = xt −xt−h and with h = 4.
7.2.3
In-Sample Performance
Figure 7.16 pictures the in-sample performance of the three models. The
solid curve is for the error path of the linear model while similar dashed
and dotted paths are the errors for alternative STRS and NNRS models.
Both alternatives improve upon the performance of the linear model.
Adding a bit of complexity greatly improves the statistical in-sample fit.
Table 7.8 gives the in-sample diagnostic statistics of the three models.
We see that the STRS and NNRS models outperform the linear model,
not only on the basis if goodness-of-fit measures, but also on specification
tests. We can reject neither serial independence in the residuals nor the
squared residuals for both alternative models. Similarly, we cannot reject
normality in the residuals of both alternatives to the linear model. Finally,
the Brock-Deckert-Scheinkman and Lee-White-Granger tests show there is
very little or no evidence of neglected nonlinearity in the NNRS model.

190
7. Inflation and Deflation: Hong Kong and Japan
1975
1980
1985
1990
1995
2000
2005
−0.08
−0.06
−0.04
−0.02
0
0.02
0.04
0.06
Linear
STRS
NNRS
FIGURE 7.16. In-sample paths of estimation errors
The information from Table 7.8 gives strong support for abandoning a
linear approach for understanding inflation/deflation dynamics in Japan.
7.2.4
Out-of-Sample Performance
Figure 7.17 gives the out-of-sample error paths of the three models. The
solid curve is for the linear prediction errors, the dashed path is for the
STRS prediction errors, and the dotted path is for the NNRS errors. We
see that the NNRS models outperforms both the STRS and linear models.
What is of interest, however, is that all three models generate negative
prediction errors in 1997, the time of the onset of the Asian crisis. The
models’ negative errors, in which the errors represent differences between
the actual and predicted outcomes, are indicators that the models do not
incorporate the true depth of the deflationary process taking place in Japan.
Table 7.9 gives the out-of-sample test statistics of the three models. We
see that the NNRS model has a much higher success ratio (in terms of
percentage correct sign predictions of the dependent variable), and outper-
forms the linear model as well as the STRS model in terms of the root
mean squared error statistic. The Diebold-Mariano statistics indicate that

7.2 Japan
191
TABLE 7.8. In-Sample Diagnostics of Alternative Models (Sample 1978–2002,
Quarterly Data)
Diagnostics
Models
Linear
STRS
NNRS
SSE
0.023
0.003
0.003
RSQ
0.240
0.900
0.910
HQIF
−315.552
−466.018
−467.288
LB*
0.067
0.458
0.681
ML*
0.864
0.254
0.200
JB*
0.002
0.172
0.204
EN*
0.531
0.092
0.084
BDS*
0.012
0.210
0.119
LWG
484
56
3
*: prob value
Note:
SSE: Sum of squared errors
RSQ: R-squared
HIQF: Hannan-Quinn information criterion
LB: Ljung-Box Q statistic on residuals
ML: McLeod-Li Q statistic on squared residuals
JB: Jarque-Bera statistic on normality of residuals
EN: Engle-Ng test of symmetry of residuals
BDS: Brock-Deckert-Scheinkman test of nonlinearity
LWG: Lee-White-Granger test of nonlinearity
the NNRS prediction errors are statistically different from the linear model.
However, the STRS prediction errors are not statistically different from
either the linear or the NNRS model.
7.2.5
Interpretation of Results
The partial derivatives of the model for Japan, as well as the tests of
significance based on bootstrapping methods, appear in Table 7.10. We see
that the only significant variables determining future inflation are current
inflation, the interest rate, and the rate of growth of the land price index.
The output gap is almost, but not quite, significant. Unit labor costs and
the Nikkei index are both insignificant and have the wrong sign.
The significant but wrong sign of the interest rate may be explained by
the fact that the Bank of Japan is constrained by the zero lower bound
of interest rates. They were lowering interest rates, but not enough during
the period of deflation, so that real interest rates were in fact increasing.
We see this in Figure 7.18.

192
7. Inflation and Deflation: Hong Kong and Japan
1988
1990
1992
1994
1996
1998
2000
2002
−0.04
−0.03
−0.02
−0.01
0
0.01
0.02
0.03
0.04
0.05
Linear
NNRS 
STRS
FIGURE 7.17. Out-of-sample prediction errors
TABLE 7.9. Out-of-Sample Forecasting Accuracy
Diagnostics
Models
Linear
STRS
NNRS
RMSQ
0.018
0.017
0.013
SR
0.511
0.489
0.644
Diebold-Mariano
Linear vs. STRS
Linear vs. NNRS
STRS vs. NNRS
Test
DM-1*
0.276
0.011
0.233
DM-2*
0.304
0.016
0.271
DM-3*
0.310
0.007
0.285
DM-4*
0.306
0.001
0.289
DM-5*
0.301
0.001
0.288
*: prob value
RMSQ: Root mean squared error
SR: Success ratio on sign correct sign predictions
DM: Diebold-Mariano test
(correct for autocorrelation, lags 1–5)

7.2 Japan
193
TABLE 7.10. Partial Derivatives of NNRS Model
Period
Arguments
Inflation Interest Import Lending Nikkei Land Price Output Unit Labor
Rate
Price
Growth
Index
Index
Gap
Costs
Mean
0.182
0.212
0.113
0.025
−0.088
0.122
0.015
−0.075
1978
0.190
0.217
0.123
0.039
−0.089
0.112
0.019
−0.092
1995
0.183
0.212
0.114
0.026
−0.088
0.121
0.015
−0.077
2002
0.181
0.211
0.112
0.023
−0.087
0.124
0.015
−0.074
Statistical Significance of Estimates
Period
Arguments
Inflation Interest Import Lending Nikkei Land Price Output Unit Labor
Rate
Price
Growth
Index
Index
Gap
Costs
Mean
0.000
0.000
0.859
0.935
0.356
0.000
0.149
1.000
1978
0.000
0.000
0.819
0.933
0.288
0.000
0.164
1.000
1995
0.000
0.000
0.840
0.931
0.299
0.000
0.164
1.000
2002
0.000
0.000
0.838
0.935
0.293
0.000
0.149
1.000
1975
1980
1985
1990
1995
2000
2005
0
0.02
−0.02
0.04
−0.04
0.06
0.08
0.1
Real Interest 
Rates 
Inflation
FIGURE 7.18. Real interest rates and inflation in Japan

194
7. Inflation and Deflation: Hong Kong and Japan
The fact that the land price index is significant while the Nikkei index is
not can be better understood by looking at Figure 7.14. The rate of growth
has shown a smooth steady decline, more in tandem with the inflation
process than with the much more volatile Nikkei index.
Table 7.11 gives the corresponding sets of partial derivatives and tests
of significance from the STRS model. The only difference we see from the
NNRS model is that the output gap variable is also significant.
Figure 7.19 pictures the evolution of inflation and the transition neurons
of the two models. As in the case of Hong Kong, the STRS transition neu-
ron gives more information, showing that the likelihood of remaining in
the inflation state is steadily decreasing as inflation switches to deflation
after 1995. The NNRS model’s transition neuron shows little or no action,
remaining close to 0.5. The result indicates that the NNRS model outper-
forms the linear and STRS model not by picking up a regime change per
se but rather by approximating nonlinear processes in the overall inflation
process.
The fact that bank lending does not appear as a significant determi-
nant of inflation (while output gap does — at least in the STRS model)
does not mean that bank lending is not important. Table 7.12 pictures the
results of a Granger causality test between the output gap and the rate of
growth of bank lending in Japan. We see strong evidence, at the 5% level
TABLE 7.11. Partial Derivatives of STRS Model
Period
Arguments
Inflation Interest Import Lending Nikkei Land Price Output Unit Labor
Rate
Price
Growth
Index
Index
Gap
Costs
Mean
0.149
0.182
0.054
−0.094
−0.032
0.208
0.028
−0.079
1978
0.138
0.163
0.055
−0.096
−0.032
0.232
0.030
−0.080
1995
0.138
0.163
0.055
−0.096
−0.032
0.232
0.030
−0.080
2002
0.133
0.156
0.056
−0.096
−0.032
0.242
0.030
−0.080
Statistical Significance of Estimates
Period
Arguments
Inflation Interest Import Lending Nikkei Land Price Output Unit Labor
Rate
Price
Growth
Index
Index
Gap
Costs
Mean
0.006
0.000
0.695
1.000
0.398
0.000
0.095
1.000
1978
0.006
0.000
0.695
1.000
0.398
0.000
0.095
1.000
1995
0.006
0.000
0.615
1.000
0.394
0.000
0.088
0.863
2002
0.002
0.000
0.947
1.000
0.739
0.000
0.114
1.000

7.2 Japan
195
1975
1980
1985
1990
1995
2000
2005
0
0.02
−0.02
0.04
−0.04
0.06
0.08
1975
1980
1985
1990
1995
2000
2005
0.46
0.48
0.5
0.52
0.54
0.56
0.58
Inflation 
Transition Neurons 
STRS Model
NNRS Model
FIGURE 7.19. Regime transitions in STRS and NNRS models
TABLE 7.12. Ganger Test of Causality: Loan Growth and the Output Gap
Hypothesis
Loan Growth Does Not
Output Gap Does Not
Cause the Output Gap
Cause Loan Growth
F-Statistic
2.5
2.4
P-Value
0.049
0.053
of significance, that the rate of growth of bank loans is a causal factor for
changes in the output gap. There is also evidence of reverse causality, from
the output gap to the rate of growth of bank lending, to be sure. These
results indicate that a reversal in bank lending will improve the output
gap, and such an improvement will call forth more bank lending, leading,
in turn, in a virtuous cycle, to further output-gap improvement and an
escape from the deflationary trap in Japan.

196
7. Inflation and Deflation: Hong Kong and Japan
7.3
Conclusion
The chapter illustrates how neural network regime switching models help
explain the evolution of inflation and deflation in Japan and Hong Kong.
The results for Hong Kong indicate that external prices and residential
property prices are the most important factors underlying inflationary
dynamics, whereas for Japan, interest rates and excess demand (prox-
ied by the output gap) appear to be more important. These results are
consistent with well-known stylized facts about both economies. Hong
Kong is a much smaller and more highly open economy than Japan, so
that the evolution of international prices and nontraded prices (prox-
ied by residential property prices) would be the driving forces behind
inflation. For Japan, a larger and less open economy, we would expect
policy variables and excess demand to be more important factors for
inflation.
Clearly, there are a large number of alternative nonlinear as well as neural
network specifications for approximating the inflation processes of different
countries. We used a regime switching approach since both Hong Kong and
Japan have indeed moved from inflationary to deflationary regimes. But for
most countries, the change in regime may be much different, such as an
implicit or explicit switch to inflation-targets for monetary policy. These
types of regime switches cannot be captured as easily as the switch from
inflation to deflation.
Since inflation is of such central importance for both policymakers and
decision makers in business, finance, and households, it is surprising that
more work using neural networks has not been forthcoming. Chen, Racine,
and Swanson (2001) have used a ridgelet neural network for forecasting
inflation in the United States. McNelis and McAdam (2004) used a thick
model approach (combining forecasts of different types of neural nets) for
both the Euro Zone and the United States. Both of these papers show the
improved forecasting performance from neural network methods. Hopefully,
more work will follow.
7.3.1
MATLAB Program Notes
The
same
programs
used
in
the
previous
chapter
were
used
for
the inflation/deflation studies.
The data are given in honkonginfla-
tion may2004 run8.mat and japdata may2004 run3.mat for Hong Kong
and Japan.
7.3.2
Suggested Exercises
The reader is invited to use data from other countries to see how well
the results from Japan or Hong Kong carry over to countries that did not

7.3 Conclusion
197
experience deflation as well as inflation. However, the threshold would have
to be changed from zero to a very low positive inflation level. What would
be of interest is the role of residential property prices as a key variable
driving inflation.


8
Classification: Credit Card Default
and Bank Failures
This chapter examines how well neural network methods compare with
more traditional methods based on discriminant analysis, as well as nonlin-
ear logit, probit, and Weibull methods, spelled out in Chapter 2, Section 7.
We examine two cases, one for classification of credit card default using
German data, and the other for banking intervention or closure, using
data from Texas in the 1980s. Both of these data sets and the results we
show are solely meant to be examples of neural network performance rel-
ative to more traditional econometric methods. There is no claim to give
new insight into credit card risk assessment or early warning signals for a
banking problem.
We see in both of the examples that classification problems involve the
use of numerical indicators for qualitative characteristics such as gender,
marital status, home ownership, or membership in the Federal Reserve
System. In this case, we are using crisp logic or crisp sets: a person is
either in one group or another. However, a related method for classification
involves fuzzy sets or fuzzy logic, in which a person may be partially in one
category or another (as in health studies, for example, one may be partially
overweight: partly in one set of “overweight” and partly in the other set of
“normal” weight). Much of the related artificial intelligence “neuro-fuzzy”
literature related to neural nets and fuzzy logic has focused on deriving rules
for making decisions, based on the outcome of classification schemes. In this
chapter, however, we will simply focus on the neural network approach with
respect to the traditional linear discriminant analysis and the nonlinear
logit, probit, and Weibull methods.

200
8. Classification: Credit Card Default and Bank Failures
When working with any nonlinear function, however, we should never
underestimate the difficulties of obtaining optima, even with simple probit
or Weibull models used for classification. The logit model, of course, is a
special case of the neural network, since a neural network with one logsig-
moid neuron reduces to the logit model. But the same tools we examined
in previous chapters — particularly hybridization or coupling the genetic
algorithm with quasi-Newton gradient methods — come in very handy.
Classification problems involving nonlinear functions have all of the same
problems as other models, especially when we work with a large number of
variables.
8.1
Credit Card Risk
For examining credit card risk, we make use of a data set used by Baesens,
Setiono, Mues, and Vanthienen (2003), on German credit card default rates.
The data set we use for classification of default/no default for German
credit cards consists of 1000 observations.
8.1.1
The Data
Table 8.1 lists the twenty arguments, a mix of categorical and continuous
variables. Table 8.1 also gives the maximum, minimum, and median values
of each of the variables. The dependent variable y takes on a value of 0 if
there is no default and a value of 1 if there is a default. There are 300 cases
of defaults in this sample, with y = 1. As we can see in the mix of variables,
there is considerable discretion about how to categorize the information.
8.1.2
In-Sample Performance
The in-sample performance of the five methods appears in Table 8.2. This
table pictures both the likelihood functions for the four nonlinear alter-
natives to the discriminant analysis and the error percentages of all five
methods. There are two types of errors, as taught from statistical decision
theory. False positives take place when we incorrectly label the dependent
variables as 1, with y = 1 when y = 0. Similarly, false negatives occur when
we have y = 0 when y = 1. The overall error ratio in Table 8.2 is simply a
weighted average of the two error percentages, with the weight set at .5.
In the real world, of course, decision makers attach differing weights to
the two types of errors. A false positive means that a credit agency or bank
incorrectly denies a credit card to a potentially good customer and thus
loses revenue from a reliable transaction. A false negative is more serious:
it means extending credit to a potentially unreliable customer, and thus
the bank assumes much higher default risk.

8.1 Credit Card Risk
201
TABLE 8.1. Attributes for German Credit Data Set
Variable
Definition
Type/Explanation
Max
Min
Median
1
Checking account
Categorical, 0 to 3
3
0
1
2
Term
Continuous
72
4
18
3
Credit history
Categorical, 0 to 4, from no history to delays
4
0
2
4
Purpose
Categorical, 0 to 9, based on type of purchase
10
0
2
5
Credit amount
Continuous
18424
250
2319.5
6
Savings account
Categorical, 0 to 4, lower to higher to unknown
4
0
1
7
Yrs in present employment
Categorical, 0 to 4, 1 unemployment, to longer years
4
0
2
8
Installment rate
Continuous
4
1
3
9
Personal status and gender
Categorical, 0 to 5, 1 male, divorced, 5 female, single
3
0
2
10
Other parties
Categorical, 0 to 2, none, 2 co-applicant, 3 guarantor
2
0
0
11
Yrs in present residence
Continuous
4
1
3
12
Property type
Categorical, 0 to 3, 0 real estate, 3 no property or unknown
3
0
2
13
Age
Continuous
75
19
33
14
Other installment plans
Categorical, 0 to 2, 0 bank, 1 stores, 2 none
2
0
0
15
Housing status
Categorical, 0 to 2, 0 rent, 1 own, 2 for free
2
0
2
16
Number of existing credits
Continuous
4
1
1
17
Job status
Categorical, 0 to 3, unemployed, 3 management
3
0
2
18
Number of dependents
Continuous
2
1
1
19
Telephone
Categorical, 0 to 1, 0 none, 1 yes, under customer name
1
0
0
20
Foreign worker
Categorical, 0 to 1, 0 yes, 1 no
1
0
0

202
8. Classification: Credit Card Default and Bank Failures
TABLE 8.2. Error Percentages
Method
Likelihood Fn.
False
False
Weighted
Positives
Negatives
Average
Discriminant analysis
na
0.207
0.091
0.149
Neural network
519.8657
0.062
0.197
0.1295
Logit
519.8657
0.062
0.197
0.1295
Probit
519.1029
0.062
0.199
0.1305
Weibull
516.507
0.072
0.189
0.1305
The neural network alternative to the logit, probit, and Weibull meth-
ods is a network with three neurons. In this case, it is quite similar to a
logit model, and in fact the error percentages and likelihood functions are
identical. We see in Table 8.2 a familiar trade-off. Discriminant analysis
has fewer false negatives, but a much higher percentage (by more than a
factor of three) of false positives.
8.1.3
Out-of-Sample Performance
To evaluate the out-of-sample forecasting accuracy of the alternative mod-
els, we used the 0.632 bootstrap method described in Section 4.2.8. To
summarize this method, we simply took 1000 random draws of data from
the original sample, with replacement, to do an estimation, and thus used
the excluded data from the original sample to evaluate the out-of-sample
forecast performance. We measured the out-of-sample forecast performance
by the error percentages of false positives or false negatives. We repeated
this process 100 times and examined the mean and distribution of the
error-percentages of the alternative models.
Table 8.3 gives the mean error percentages for each method, based on the
bootstrap experiments. We see that the neural network and logit models
give identical performance, in terms of out-of-sample accuracy. We also see
that discriminant analysis and the probit and Weibull methods are almost
mirror images of each other. Whereas discriminant analysis is perfectly
accurate in terms of false positives, it is extremely imprecise (with an error
rate of more than 75%) in terms of false negatives, while probit and Weibull
are quite accurate in terms of false negatives, but highly imprecise in terms
of false positives. The better choice would be to use logit or the neural
network method.
The fact that the network model does not outperform the logit model
should not be a major cause for concern. The logit model is a neural net
model with one neuron. The network we use is a model with three neu-
rons. Comparing logit and neural network models is really a comparison
of two alternative neural network specifications, one with one neuron and

8.1 Credit Card Risk
203
TABLE 8.3. Out-of-Sample Forecasting: 100 Draws Mean Error Percentages
(0.632 Bootstarp)
Method
False
False
Weighted
Positives
Negatives
Average
Discriminant analysis
0.000
0.763
0.382
Neural network
0.095
0.196
0.146
Logit
0.095
0.196
0.146
Probit
0.702
0.003
0.352
Weibull
0.708
0.000
0.354
another with three. What is surprising is that the introduction of the addi-
tional two neurons in the network does not cause a deterioration of the
out-of-sample performance of the model. By adding the two additional
neurons we are not overfitting the data or introducing nuisance param-
eters which cause a decline in the predictive performance of the model.
What the results indicate is that the class of parsimoniously specified neu-
ral network models greatly outperforms discriminant analysis, probit, and
Weibull specifications.
Figure 8.1 pictures the distribution of the weighted average (of false posi-
tives and negatives) for the two models over the 100 bootstrap experiments.
We see that they are identical.
8.1.4
Interpretation of Results
Table 8.4 gives information on the partial derivatives of the models as well
as the corresponding marginal significance or P-values of these estimates,
based on the bootstrap distributions. We see that the estimates of the
network and logit models are for all practical purposes identical. The probit
model results do not differ by much, whereas the Weibull estimates differ
by a bit more, but not by a large factor.
Many studies using classification methods are not interested in the par-
tial derivatives, since interpretation of specific categorical variables is not
as straightforward as continuous variables. However, the bootstrapped
P-values show that credit amount, property type, job status, and number
of dependents are not significant. Some results are consistent with expec-
tations: the greater the number of years in present employment, the lower
the risk of a default. Similarly for age, telephone, other parties, or status
as a foreign worker: older persons, who have telephones in their own name,
have partners in their account, and are not foreign are less likely to default,
We also see that having a higher installment rate or multiple installment
plans is more likely to lead to default.


## Nonlinear Principal Components

204
8. Classification: Credit Card Default and Bank Failures
0.125
0.13
0.135
0.14
0.145
0.15
0.155
0
20
40
60
80
0.125
0.13
0.135
0.14
0.145
0.15
0.155
0
20
40
60
80
NETWORK MODEL 
LOGIT MODEL 
FIGURE 8.1. Distribution of 0.632 bootstrap out-of-sample error percentages
While all three models give broadly consistent interpretations, this
should be reassuring rather than a cause of concern. These results indi-
cate that using two methods, logit and neural net, one as a check on the
other, may be sufficient for both accuracy and understanding.
8.2
Banking Intervention
Banking intervention, the need to close or to put a private bank under
state management, more extensive supervision, or to impose a change of
management, is, unfortunately, common enough both in developing and in
mature industrialized countries. We use the same binary or classification
methods to examine how well key characteristics of banks may serve as
early warning signals for a crisis or intervention of a particular bank.
8.2.1
The Data
Table 8.5 gives information about the dependent variables as well as
explanatory variables we use for our banking study. The data were obtained

8.2 Banking Intervention
205
TABLE 8.4.
Variable Definition
Partial Derivatives*
Prob Values**
Network Logit
Probit Weibull Network Logit Probit Weibull
1
Checking account
0.074
0.074
0.076
0.083
0.000
0.000 0.000
0.000
2
Term
0.004
0.004
0.004
0.004
0.000
0.000 0.000
0.000
3
Credit history
−0.078 −0.078 −0.077 −0.076
0.000
0.000 0.000
0.000
4
Propose
−0.007 −0.007 −0.007 −0.007
0.000
0.000 0.000
0.000
5
Credit amount
0.000
0.000
0.000
0.000
0.150
0.150 0.152
0.000
6
Savings account
−0.008 −0.008 −0.009 −0.010
0.020
0.020 0.020
0.050
7
Yrs in present
employment
−0.032 −0.032 −0.031 −0.030
0.000
0.000 0.000
0.000
8
Installment rate
0.053
0.053
0.053
0.049
0.000
0.000 0.000
0.000
9
Personal status
and gender
−0.052 −0.052 −0.051 −0.047
0.000
0.000 0.000
0.000
10
Other parties
−0.029 −0.029 −0.026 −0.020
0.010
0.010 0.020
0.040
11
Yrs in present
residence
0.008
0.008
0.008
0.004
0.050
0.050 0.040
0.060
12
Property type
−0.002 −0.002 −0.000
0.003
0.260
0.260 0.263
0.300
13
Age
−0.003 −0.003 −0.003 −0.002
0.000
0.000 0.000
0.010
14
Other installment
plans
0.057
0.057
0.062
0.073
0.000
0.000 0.000
0.000
15
Housing status
−0.047 −0.047 −0.050 −0.051
0.000
0.000 0.000
0.000
16
Number of
existing credits
0.057
0.057
0.055
0.053
0.000
0.000 0.000
0.000
17
Job status
0.003
0.003
0.006
0.012
0.920
0.920 0.232
0.210
18
Number of
dependents
0.032
0.032
0.030
0.022
0.710
0.710 0.717
0.030
19
Telephone
−0.064 −0.064 −0.065 −0.067
0.000
0.000 0.000
0.000
20
Foreign worker
−0.165 −0.165 −0.153 −0.135
0.000
0.000 0.000
0.000
*: Derivatives calculated as finite differences
**: Prob values calculated from bootstrap distributions
from the Federal Reserve Bank of Dallas using banking records from the
last two decades. The total percentage of banks that required interven-
tion, either by state or federal authorities, was 16.7. We use 12 variables
as arguments. The capital-asset ratio, of course, is the key component of
the well-known Basel accord for international banking standards.
While the negative number for the minimum of the capital-asset ratio
may seem surprising, the data set includes both sound and unsound banks.
When we remove the observations having negative capital-asset ratios, the
distribution of this variable shows that the ratio is between 5 and 10% for
most of the banks in the sample. The distribution appears in Figure 8.2.
8.2.2
In-Sample Performance
Table 8.6 gives information about the in-sample performance of the
alternative models.

206
8. Classification: Credit Card Default and Bank Failures
TABLE 8.5. Texas Banking Data
Max
Min
Median
1
Charter
1
0
0
2
Federal Reserve
1
0
1
3
Capital/asset %
30.9
−77.71
7.89
4
Agricultural loan/total loan ratio
0.822371
0
0.013794
5
Consumer loan/total loan ratio
0.982775
0
0.173709
6
Credit card loan/total loan ratio
0.322974
0
0
7
Installment loan/total loan ratio
0.903586
0
0.123526
8
Nonperforming loan/total loan - %
35.99
0
1.91
9
Return on assets - %
10.06
−36.05
0.97
10
Interest margin - %
10.53
−2.27
3.73
11
Liquid assets/total assets - %
96.54
3.55
52.35
12
U.S. total loans/U.S. gdp ratio
2.21
0.99
1.27
Dependent Variables: Bank closing or intervention
No observations: 12,605
% of Interventions/closings: 16.7
0
5
10
15
20
25
30
35
0
1000
2000
3000
4000
5000
6000
7000
8000
FIGURE 8.2. Distribution of capital-asset ratio (%)

8.2 Banking Intervention
207
TABLE 8.6. Error Percentages
Method
Likelihood Fn.
False
False
Weighted
Positives
Negatives
Average
Discriminant analysis
na
0.205
0.038
0.122
Neural network
65535
0.032
0.117
0.075
Logit
65535
0.092
0.092
0.092
Probit
4041.349
0.026
0.122
0.074
Weibull
65535
0.040
0.111
0.075
TABLE 8.7. Out-of-Sample Forecasting: 40 Draws Mean Error Percentages
(0.632 Bootstarp)
Method
False
False
Weighted
Positives
Negatives
Average
Discriminant analysis
0.000
0.802
0.401
Neural network
0.035
0.111
0.073
Logit
0.035
0.089
0.107
Probit
0.829
0.000
0.415
Weibull
0.638
0.041
0.340
Similar to the example with the credit card data, we see that discriminant
analysis gives more false positives than the competing nonlinear methods.
In turn, the nonlinear methods give more false negatives than the linear
discriminant method. For overall performance, the network, probit, and
Weibull methods are about the same, in terms of the weighted average
error score. We can conclude that the network model, specified with three
neurons, performs about as well as the most accurate method, for in-sample
estimation.
8.2.3
Out-of-Sample Performance
Table 8.7 gives the mean error percentages, based on the 0.632 bootstrap
method. The ratios are the averages over 40 draws, by the bootstrap
method. We see that discriminant analysis has a perfect score, zero per-
cent, on false positives, but has a score of over 80% on false negatives. The
overall best performance in this experiment is by the neural network, with
a 7.3% weighted average error score. The logit model is next, with a 10%
weighted average score. As in the previous example the neural network
family outperforms the other methods in terms of out-of-sample accuracy.

208
8. Classification: Credit Card Default and Bank Failures
0.068
0.07
0.072
0.074
0.076
0.078
0.08
0.082
0
2
4
6
8
10
12
0.07
0.08
0.09
0.1
0.11
0.12
0.13
0
5
10
15
NETWORK MODEL 
LOGIT MODEL 
FIGURE 8.3. Distribution of 0.632 bootstrap: out-of-sample error percentages
Figure 8.3 pictures the distribution of the out-of-sample weighted average
error scores of the network and logit models. While the average of the logit
model is about 10%, we see in this figure that the center of the distribution,
for most of the data, is between 11 and 12%, whereas the corresponding
center for the network model is between 7.2 and 7.3%. The network model’s
performance clearly indicates that it should be the preferred method for
predicting individual banking crises.
8.2.4
Interpretation of Results
Table 8.8 gives the partial derivatives as well as the corresponding P-values
(based on bootstrapped distributions). Unlike the previous example, we do
not have the same broad consistency about the signs or significance of
the key variables. However, what does emerge is the central importance
of the capital asset ratio as an indicator of banking vulnerability. The
higher this ratio, the lower the likelihood of banking fragility. Three of
the four models (network, logit, and probit) indicate that this variable
is significant, and the magnitude of the derivatives (calculated by finite
differences) is the same.

8.3 Conclusion
209
TABLE 8.8.
No. Definition
Partial Derivatives*
Prob Values**
Network
Logit
Probit
Weibull Network Logit Probit Weibull
1
Charter
0.000
0.000
−0.109 −0.109
0.767
0.833
0.267
0.533
2
Federal Reserve
0.082
0.064
0.031
0.031
0.100
0.167
0.000
0.400
3
Capital/asset %
−0.051
−0.036
−0.053 −0.053
0.000
0.000
0.000
0.367
4
Agricultural loan/
total loan ratio
0.257
0.065
−0.020 −0.020
0.133
0.200
0.000
0.600
5
Consumer loan/
total loan ratio
0.397
0.088
0.094
0.094
0.300
0.767
0.000
0.433
6
Credit card loan/
total loan ratio
1.049
−1.163
−0.012 −0.012
0.700
0.233
0.000
0.567
7
Installment loan/
total loan ratio
−0.137
0.187
−0.115 −0.115
0.967
0.233
0.000
0.600
8
Nonperforming
loan/total loan - %
0.004
0.001
0.010
0.010
0.167
0.167
0.067
0.533
9
Return on
assets - %
−0.042
−0.025
−0.032 −0.032
0.067
0.133
0.000
0.367
10
Interest margin - %
0.013
−0.029
0.018
0.018
0.967
0.933
1.000
0.567
11
Liquid assets/
total assets - %
0.001
0.002
0.001
0.001
0.067
0.667
0.000
0.533
12
U.S. total loans/
U.S. gdp ratio
0.149
0.196
0.118
0.118
0.000
0.033
0.000
0.333
*: Derivatives calculated as finite differences
**: Prob values calculated from bootstrap distributions
The same three models also indicate that the aggregate U.S. total loan
to total GDP ratio is also a significant determinant of an individual bank’s
fragility. Thus, both aggregate macro conditions and individual bank char-
acteristics matter, as informative signals for banking problems. Finally, the
network model (as well as the probit) show that return on assets is also
significant as an indicator, with a higher return, as expected, lowering the
likelihood of banking fragility.
8.3
Conclusion
In this chapter we examined two data sets, one on credit card default rates,
and the other on banking failures or fragilities requiring government inter-
vention. We found that neural nets either perform as well as or better than
the best nonlinear alternative, from the set of logit, probit, or Weibull
models, for classification. The hybrid evolutionary genetic algorithm and
classical gradient-descent methods were used to obtain the parameter esti-
mates for all of the nonlinear models. So we were not handicapping one
or another model with a less efficient estimation process. On the contrary,

210
8. Classification: Credit Card Default and Bank Failures
we did the best to find, as closely as possible, the global optima when
maximizing the likelihood functions.
There are clearly many interesting examples to study with this method-
ology. The work on early warning signals for currency crises would be
amenable to this methodology. Similarly, further work comparing neural
networks to standard models can be done on classification problems involv-
ing more than two categories, or on discrete ordered multinomial problems,
such as student evaluation rankings of professors on a scale of one through
five [see Evans and McNelis (2000)].
The methods in this chapter could be extended into more elaborate net-
works in which the predictions of different models, such as discriminant,
logit, probit, and Weibull, are fed in as inputs to a complex neural net-
work. Similarly, forecasting can be done in a thick modeling or bagging
approach: all of the models can be used, and a mean or trimmed mean can
be the forecast from a wide set of models, including a variety of neural nets
specified with different numbers of neurons in the hidden layer. But in this
chapter we wanted to keep the “race” simple, so we leave the development
of more elaborate networks for further exploration.
8.3.1
MATLAB Program Notes
The programs for these two country experiences are germandefault prog.m
for German credit card default rates, and texasfinance prog.m for the
Texas bank failures. The data are given in germandefault run4.mat and
texasfinance run9.mat.
8.3.2
Suggested Exercises
An interesting sensitivity analysis would be to reduce the number of
explanatory variables used in this chapter’s examples to smaller sets of
regressors to see if the same variables remain significant in the modified
models.

9
Dimensionality Reduction and Implied
Volatility Forecasting
In this chapter we apply the methodologies of linear and nonlinear principal
component dimensionality reduction to observed volatilities on Hong Kong
and United States swap options of differing maturities, of one to ten years,
to see if these methods help us to find the underlying volatility signal from
the market. The methods are presented in Section 2.6.
Obtaining an accurate measure of the market volatility, when in fact
there are many different market volatility measures or alternative nonmar-
ket measures of volatility to choose from, is a major task for effective option
pricing and related hedging activities. A major focus in financial market
research today is volatility, rather than return, forecasting. Volatilities, as
proxies of risk, are asymmetric and perhaps nonlinear processes, at the very
least, to the extent that they are bounded by zero from below. So nonlinear
approximation methods such as neural networks may have a payoffwhen
we examine such processes.
We compare and contrast the implied volatility measures for Hong Kong
and the United States, since we expect both of these to have similar fea-
tures, due to the currency peg of the Hong Kong dollar to the U.S. dollar.
But there may also be some differences, since Hong Kong was more vul-
nerable to the Asian financial crisis which began in 1997, and also had
the SARS crisis in 2003. We discuss both of these experiences in turn,
and apply the linear and nonlinear dimensionality reduction methods for
in-sample as well as for out-of-sample performance.

212
9. Dimensionality Reduction and Implied Volatility Forecasting
1997
1998
1999
2000
2001
2002
2003
2004
10
20
30
40
50
60
70
FIGURE 9.1. Hong Kong implied volatility measures, maturity 2, 3, 4, 5, 7,
10 years
9.1
Hong Kong
9.1.1
The Data
The implied volatility measures, for daily data from January 1997 till July
2003, obtained from Reuters, appear in Figure 9.1. We see the sharp
upturn in the measures with the onset of the Asian crisis in late 1997.
There are two other spikes: one around the third quarter of 2001, and
another after the start of 2002. Both of these jumps, no doubt, reflect
uncertainty in the world economy in the wake of the September 11 terrorist
attacks and the start of the war in Afghanistan. The continuing volatility
in 2003 may also be explained by the SARS epidemic in Hong Kong and
East Asia.
Table 9.1 gives a statistical summary of the data appearing in Figure 9.1.
There are a number of interesting features coming from this summary. One
is that both the mean of the implied volatilities, as well as the standard

9.1 Hong Kong
213
TABLE 9.1. Hong Kong Implied Volatility Estimates; Daily Data: Jan. 1997–
July 2003
Statistic
Maturity in Years
2
3
4
5
7
10
Mean
28.581
26.192
24.286
22.951
21.295
19.936
Median
27.500
25.000
23.500
22.300
21.000
20.000
Std. Dev.
12.906
10.183
8.123
6.719
5.238
4.303
Coeff. Var
0.4516
0.3888
0.33448
0.2927
0.246
0.216
Skewness
0.487
0.590
0.582
0.536
0.404
0.584
Kurtosis
2.064
2.235
2.302
2.242
2.338
3.553
Max
60.500
53.300
47.250
47.500
47.500
47.500
Min
11.000
12.000
12.250
12.750
12.000
11.000
deviation of the implied volatility measures, or volatility of the volatilities,
decline as the maturity increases. Related to this feature is that the range,
or difference between maximum and minimum values, is greatest for the
short maturity of two years. The extent of the variability decline in the
data can best be captured by the coefficient of variation, defined as the
ratio of the standard deviation to the mean. We see that this measure
declines by more than 50% as we move from two-year to ten-year maturities.
Finally, there is no excess kurtosis in these measures, whereas rates of
return typically have this property.
9.1.2
In-Sample Performance
Figure 9.2 pictures the evolution of the two principal component measures.
The solid curve comes from the linear method. The broken curve comes
from an auto-associative map or neural network. We estimate the network
with five encoding neurons and five decoding neurons. For ease of compar-
ison, we scaled each series between zero and one. What is most interesting
about Figure 9.2 is how similar both curves are. The linear principal com-
ponent shows a big spike in mid-1999, but the overall volatility of the
nonlinear principal component is slightly greater. The standard deviations
of the linear and nonlinear components are, respectively, .233 and .272,
where their respective coefficients of variation are .674 and .724.
How well do these components explain the variation of the data, for the
full sample? Table 9.2 gives simple goodness-of-fit R2 measures for each of
the maturities. We see that the nonlinear principal component better fits
the more volatile 2-year maturity, whereas the linear component fits much,
much better at 5, 7, and 10-year maturities.

214
9. Dimensionality Reduction and Implied Volatility Forecasting
1997
1998
1999
2000
2001
2002
2003
2004
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
Linear
Principal
Component
Nonlinear
Principal
Component
FIGURE 9.2. Hong Kong linear and nonlinear principal component measures
TABLE 9.2. Hong Kong Implied Volatility Estimates Goodness of Fit: Linear
and Nonlinear Components, Multiple Correlation Coefficient
Maturity in Years
2
3
4
5
7
10
Linear
0.965
0.986
0.990
0.981
0.923
0.751
Nonlinear
0.988
0.978
0.947
0.913
0.829
0.698
9.1.3
Out-of-Sample Performance
To evaluate the out-of-sample performance of each of the models, we did
a recursive estimation of the principal components. First, we took the
first 80% of the data, estimated the principal component coefficients and
nonlinear functions for extracting one component, brought in the next
observation, and applied these coefficients and functions for estimating the
new principal component. We used this new forecast principal component

9.1 Hong Kong
215
2002.2
2002.4
2002.6
2002.8
2003
2003.2
2003.4
2003.6
2003.8
2002.2
2002.4
2002.6
2002.8
2003
2003.2
2003.4
2003.6
2003.8
−15
−10
−5
0
5
10
15
−10
−5
0
5
10
15
Linear Principal Component
Nonlinear Principal Component
FIGURE 9.3. Hong Kong recursive out-of-sample principal component prediction
errors
to explain the six observed volatilities at that observation. We then con-
tinued this process, adding in one observation each period, updating the
sample, and re-estimating the coefficients and nonlinear functions, until
the end of the data set.
The forecast errors of the recursively updated principal components
appear in Figure 9.3. It is clear that the errors of the nonlinear princi-
pal component forecasting model are generally smaller than those of the
linear principal component model. The most noticeable jump in the non-
linear forecast errors takes place in early 2003, at the time of the SARS
epidemic in Hong Kong.
Are the forecast errors significantly different from each other? Table 9.3
gives the root mean squared error statistics as well as Diebold-Mariano tests
of significance for these forecast errors, for each of the volatility measures.
The results show that the nonlinear principal components do significantly
better than the linear principal components at maturities of 2, 3, 7, and
10 years.

216
9. Dimensionality Reduction and Implied Volatility Forecasting
TABLE 9.3. Hong Kong Implied Volatility Estimates: Out-of-Sample Prediction
Performance, Root Mean Squared Error
Maturity in Years
2
3
4
5
7
10
Linear
4.195
2.384
1.270
2.111
4.860
7.309
Nonlinear
1.873
1.986
2.598
2.479
1.718
1.636
Diebold-Mariano Tests∗
Maturity in Years
2
3
4
5
7
10
DM-0
0.000
0.000
1.000
0.762
0.000
0.000
DM-1
0.000
0.000
1.000
0.717
0.000
0.000
DM-2
0.000
0.000
1.000
0.694
0.000
0.000
DM-3
0.000
0.000
1.000
0.678
0.000
0.000
DM-4
0.000
0.000
1.000
0.666
0.000
0.000
Note: ∗P-values
DM-0 to DM-4: tests at autocorrelations 0 to 4.
9.2
United States
9.2.1
The Data
Figure 9.4 pictures the implied volatility measures for the same time period
as the Hong Kong data, for the same maturities. While the general pattern
is similar, we see that there is less volatility in the volatility measures in
1997 and 1998. There is a spike in the data in late 1998. The jump in
volatility in later 2001 is of course related to the September 11 terrorist
attacks, and the further increased volatility beginning in 2002 is related to
the start of hostilities in the Gulf region and Afghanistan.
The statistical summary of these data appear in Table 9.4. The overall
volatility indices of the volatilities, measured by the standard deviations
and the coefficients of variation, are actually somewhat higher for the
United States than for Hong Kong. But otherwise, we observe the same
general properties that we see in the Hong Kong data set.
9.2.2
In-Sample Performance
Figure 9.5 pictures the linear and nonlinear principal components for the
U.S. data. As in the case of Hong Kong, the volatility of the nonlinear
principal component is greater than that of the linear principal component.

9.2 United States
217
1997
1998
1999
2000
2001
2002
2003
2004
10
20
30
40
50
60
70
FIGURE 9.4. U.S. implied volatility measures, maturities 2, 3, 4, 5, 7, 10 years
TABLE 9.4. U.S. Implied Volatility Estimates, Daily Data: Jan. 1997–July 2003
Statistic
Maturity in Years
2
3
4
5
7
10
Mean
24.746
23.864
22.799
21.866
20.360
18.891
Median
17.870
18.500
18.900
19.000
18.500
17.600
Std. Dev.
14.621
11.925
9.758
8.137
6.106
4.506
Coeff. Var
0.591
0.500
0.428
0.372
0.300
0.239
Skewness
1.122
1.214
1.223
1.191
1.092
0.952
Kurtosis
2.867
3.114
3.186
3.156
3.023
2.831
Max
66.000
59.000
50.000
44.300
37.200
31.700
Min
10.600
12.000
12.500
12.875
12.750
12.600

218
9. Dimensionality Reduction and Implied Volatility Forecasting
1997
1998
1999
2000
2001
2002
2003
2004
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
Nonlinear
Principal
Component
Linear
Principal
Component
FIGURE 9.5. U.S. linear and nonlinear principal component measures
TABLE 9.5. U.S. Implied Volatility Estimates Goodness of Fit: Linear and
Nonlinear Components Multiple Correlation Coefficient
Maturity in Years
2
3
4
5
7
10
Linear
0.983
0.995
0.997
0.998
0.994
0.978
Nonlinear
0.995
0.989
0.984
0.982
0.977
0.969
The goodness-of-fit R2 measures appear in Table 9.5. We see that there
is not as great a drop-offin the explanatory power of the two components,
as in the case of Hong Kong, as we move up the maturity scale.
9.2.3
Out-of-Sample Performance
The recursively estimated out-of-sample prediction errors of the two com-
ponents appear in Figure 9.6. As in the case of Hong Kong, the prediction
errors of the nonlinear component appear to be more tightly clustered.

9.3 Conclusion
219
2002.2
2002.4
2002.6
2002.8
2003
2003.2
2003.4
2003.6
2003.8
2002.2
2002.4
2002.6
2002.8
2003
2003.2
2003.4
2003.6
2003.8
−15
−10
−5
0
5
10
15
−10
−5
0
5
10
15
Linear Principle Component
Nonlinear Principle Component
FIGURE 9.6. U.S. recursive out-of-sample principal component prediction errors
There are noticeable jumps in the nonlinear prediction errors in mid-2002
and in 2003 at the end of the sample.
The root mean squared error statistics as well as the Diebold-Mariano
tests of significance appear in Table 9.5. For the United States, the nonlin-
ear component outperforms the linear component for all maturities except
for four years.1
9.3
Conclusion
In this chapter we examined the practical uses of linear and nonlinear com-
ponents for analyzing volatility measures in financial markets, particularly
the swap option market. We see that the principal component extracts by
1For the three-year maturity the linear root mean squared error is slightly lower than
the error of the nonlinear component. However, the slightly higher linear statistic is due
to a few jumps in the nonlinear error. Otherwise, the nonlinear error remains much closer
to zero. This explains the divergent results of the squared error and Diebold-Mariano
statistics.


## Neural-Network GARCH Models

220
9. Dimensionality Reduction and Implied Volatility Forecasting
TABLE 9.5. U.S. Implied Volatility Estimates: Out-of-Sample Prediction Per-
formance Root Mean Squared Error
Maturity in Years
2
3
4
5
7
10
Linear
5.761
2.247
1.585
3.365
5.843
7.699
Nonlinear
1.575
2.249
2.423
2.103
1.504
1.207
Diebold-Mariano Tests∗
Maturity in Years
2
3
4
5
7
10
DM-0
0.000
0.000
0.997
0.000
0.000
0.000
DM-1
0.000
0.002
0.986
0.000
0.000
0.000
DM-2
0.000
0.006
0.971
0.000
0.000
0.000
DM-3
0.000
0.011
0.956
0.000
0.000
0.000
DM-4
0.000
0.017
0.941
0.001
0.000
0.000
Note: ∗P-values
DM-0 to DM-4: tests at autocorrelations 0 to 4.
the nonlinear auto-associative mapping are much more effective for out-of-
sample predictions than the linear component. However, both components,
for both countries, follow broadly similar patterns. Doing a simple test of
causality, we find that both the U.S. components, whether linear or non-
linear, can help predict the linear or nonlinear Hong Kong components,
but not vice-versa. This should not be surprising, since the U.S. market is
much larger and many of the pricing decisions would be expected to follow
U.S. market developments.
9.3.1
MATLAB Program Notes
The main MATLAB program for this chapter is neftci capfloor prog.m. The
final output and data are in USHKCAPFLOOR ALL run77.mat.
9.3.2
Suggested Exercises
An interesting extension would be to find one principal component for the
combined set of U.S. and Hong Kong cap-floor volatilities. Following this,
the reader could compare the one principal component for the combined
set with the corresponding principal component for each country. Are there
any differences?

Bibliography
Aarts, E., and J. Korst (1989), Simulated Annealing and Boltzmann
Machines: A Stochastic Approach to Combinatorial Optimization and
Neural Computing. New York: John Wiley and Sons.
Akaike, H. (1974), “A New Look At Statistical Model Identification,” IEEE
Transactions on Automatic Control, AC-19, 46: 716–723.
Altman,
Edward (1981),
Applications of Classification Procedures in
Business, Banking and Finance. Greenwich, CT: JAI Press.
Arifovic, Jasmina (1996), “The Behavior of the Exchange Rate in the
Genetic Algorithm and Experimental Economies,” Journal of Political
Economy 104: 510–541.
B¨ack, T. (1996), Evolutionary Algorithms in Theory and Practice. Oxford:
Oxford University Press.
Baesens, Bart, Rudy Setiono, Christophe Mues, and Jan Vanthienen
(2003), “Using Neural Network Rule Extraction and Decision Tables
for Credit-Risk Evaluation.” Management Science 49: 312–329.
Banerjee, A, R.L. Lumsdaine, and J. H. Stock (1992), “Recursive and
Sequential Tests of the Unit Root and Trend-Break Hypothesis:
Theory and International Evidence,”
Journal of Business and
Economic Statistics 10: 271–287.

222
Bibliography
Bates, David S. (1996), “Jumps and Stochastic Volatility: Exchange Rate
Processes Implicit in Deutsche Mark Options,” Review of Financial
Studies 9: 69–107.
Beck, Margaret (1981), “The Effects of Seasonal Adjustment in Economet-
ric Models.” Discussion Paper 8101, Reserve Bank of Australia.
Bellman, R. (1961), Adaptive Control Processes: A Guided Tour. Princeton,
NJ: Princeton University Press.
Beltratti, Andrea, Serio Margarita, and Pietro Terna (1996), Neural Net-
works for Economic and Financial Modelling. Boston: International
Thomson Computer Press.
Beresteanu,
Ariel (2003),
“Nonparametric Estimation of Regression
Functions
under
Restrictions
on
Partial
Derivatives.”
Working
Paper,
Department of Economics,
Duke University.
Webpage:
www.econ.duke.edu/˜arie/shape.pdf.
Bernstein, Peter L. (1998), Against the Gods: The Remarkable Story of
Risk. New York: John Wiley and Sons.
Black, Fisher, and Myron Sholes (1973), “The Pricing of Options and
Corporate Liabilities,” Journal of Political Economy 81: 637–654.
Bollerslev,
Timothy (1986),
“Generalized Autoregressive Conditional
Heteroskedasticity,” Journal of Econometrics, 31: 307–327.
——— (1987), “A Conditionally Heteroskedastic Time Series Model for
Speculative Prices and Rates of Return,” Review of Economics and
Statistics 69: 542–547.
Breiman,
Leo (1996),
“Bagging Predictors,”
Machine Learning
24:
123–140.
Brock, W., W. Deckert, and J. Scheinkman (1987), “A Test for Inde-
pendence Based on the Correlation Dimension,” Working Paper,
Department of Economics, University of Wisconsin at Madison.
———, and B. LeBaron (1996), “A Test for Independence Based on the
Correlation Dimension.” Econometric Reviews 15: 197–235.
Buiter, Willem, and Nikolaos Panigirtazoglou (1999), “Liquidity Traps:
How to Avoid Them and How to Escape Them.”
Webpage:
www.cepr.org/pubs/dps/DP2203.dsp.

Bibliography
223
Campbell, John Y., Andrew W. Lo, and A. Craig MacKinlay (1997),
The Econometrics of Financial Markets. Princeton, NJ: Princeton
University Press.
Carreira-Perpinan, M.A. (2001), Continuous Latent Variable Models for
Dimensionality Reduction. University of Sheffield, UK: Ph.D. Thesis.
Webpage: www.cs.toronto.edu/˜miguel/papers.html.
Chen, Xiaohong, Jeffery Racine, and Norman R. Swanson (2001), “Semi-
parametric ARX Neural Network Models with an Application to
Forecasting Inflation,” IEEE Transactions in Neural Networks 12:
674–683.
Chow, Gregory (1960), “Statistical Demand Functions for Automobiles and
Their Use for Forecasting,” in Arnold Harberger (ed.), The Demand
for Durable Goods. Chicago: University of Chicago Press, 149–178.
Clark, Todd E., and Michael W. McCracken (2001), “Tests of Fore-
cast Accuracy and Encompassing for Nested Models,” Journal of
Econometrics 105: 85–110.
Clark, Todd E., and Kenneth D. West (2004), “Using Out-of-Sample Mean
Squared Prediction Errors to Test the Martingale Difference Hypoth-
esis.” Madison, WI: Working Paper, Department of Economics,
University of Wisconsin.
Clouse, James, Dale Henderson, Athanasios Orphanides, David Small,
and Peter Tinsley (2003), “Monetary Policy when the Nominal Short
Term Interest Rate is Zero,” in Topics in Macroeconomics. Berkeley
Electronic Press: www.bepress.com.
Collin-Dufresne, Pierre, Robert Goldstein, and J. Spencer Martin (2000),
“The Determinants of Credit Spread Changes.” Working Paper, Grad-
uate School of Industrial Administration, Carnegie Mellon University.
Cook, Steven (2001), “Asymmetric Unit Root Tests in the Presence of
Structural Breaks Under the Null,” Economics Bulletin: 1–10.
Corradi, Valentina, and Norman R. Swanson (2002), “Some Recent Devel-
opments in Predictive Accuracy Testing with Nested and (Generic)
Nonlinear Alternatives.” New Brunswick, NJ: Working Paper, Depart-
ment of Economics, Rutgers University.
Craine, Roger, Lars A. Lochester, and Knut Syrtveit (1999), “Estima-
tion of a Stochastic-Volatility Jump Diffusion Model.” Unpublished

224
Bibliography
Manuscript,
Department of Economics,
University of California,
Berkeley.
Dayhoff, Judith E., and James M. DeLeo (2001), “Artificial Neural
Networks: Opening the Black Box.” Cancer 91: 1615–1635.
De Falco, Ivanoe (1998), “Nonlinear System Identification by Means
of Evolutionarily Optimized Neural Networks,” in Quagliarella, D.,
J. Periaux, C. Poloni, and G. Winter (eds.), Genetic Algorithms
and Evolution Strategy in Engineering and Computer Science: Recent
Advances and Industrial Applications. West Sussex, England: John
Wiley and Sons.
Dickey, D.A., and W.A. Fuller (1979), “Distribution of the Estimators
for Autoregressive Time Series With a Unit Root,” Journal of the
American Statistical Association 74: 427–431.
Diebold, Francis X., and Roberto Mariano (1995), “Comparing Predictive
Accuracy,” Journal of Business and Economic Statistics, 3: 253–263.
Engle, Robert (1982), “Autoregressive Conditional Heterskedasticity with
Estimates of the Variance of United Kingdom Inflation,” Econometrica
50: 987–1007.
———,
and Victor Ng (1993),
“Measuring the Impact of News on
Volatility,” Journal of Finance 48: 1749–1778.
Essenreiter, Robert (1996), Geophysical Deconvolution and Inversion with
Neural Networks. Department of Geophysics, University of Karlsruhe,
www-gpi.physik.uni-karlsruhe.de.
Evans, Martin D., and Paul D. McNelis (2000), “Student Evaluations and
the Assessment of Teaching Effectiveness: What Can We Learn from
the Data.” Webpage: www.georgetown.edu/faculty/mcnelisp/Evans-
McNelis.pdf.
Fotheringhame, David, and Roland Baddeley (1997), “Nonlinear Principal
Components Analysis of Neuronal Spike Tran Data.” Working Paper,
Department of Physiology, University of Oxford.
Franses, Philip Hans, and Dick van Dijk (2000), Non-linear Time Series
Models in Empirical Finance. Cambridge, UK: Cambridge University
Press.
Gallant, A. Ronald, Peter E. Rossi, and George Tauchen (1992), “Stock
Prices and Volume.” Review of Financial Studies 5: 199–242.

Bibliography
225
Geman, S., and D. Geman (1984), “Stochastic Relaxation, Gibbs Distri-
butions, and the Bayesian Restoration of Images,” IEEE Transactions
on Pattern Analysis and Machine Intelligence, PAMI-6: 721–741.
Genberg, Hans (2003), “Foreign Versus Domestic Factors as Sources of
Macroeconomics Fluctuations in Hong Kong.” HKIMR Working Paper
17/2003.
———, and Laurent Pauwels (2003), “Inflation in Hong Kong, SAR–In
Search of a Transmission Mechanism.” HKIMR Working Paper No.
01/2003.
Gerlach, Stefan, and Wensheng Peng (2003), “Bank Lending and Property
Prices in Hong Kong.” Hong Kong Institute of Economic Research,
Working Paper 12/2003.
Giordani, Paolo (2001) “An Alternative Explanation of the Price Puzzle.”
Stockholm: Sveriges Riksbank Working Paper Series No. 125.
Goodhard, Charles, and Boris Hofmann (2003), “Deflation, Credit and
Asset Prices.” HKIMR Working Paper 13/2003.
Goodfriend, Marvin (2000), “Overcoming the Zero Bound on Interest Rate
Policy,” Journal of Money, Credit, and Banking 32: 1007–1035.
Greene, William H. (2000), Econometric Analysis. Upper Saddle River,
NJ: Prentice Hall.
Granger, Clive W.J., and Yongil Jeon (2002), “Thick Modeling.” Unpub-
lished Manuscript, Department of Economics, University of California,
San Diego, Economic Modeling, forthcoming.
Ha, Jimmy, and Kelvin Fan (2002), “Price Convergence Between Hong
Kong and the Mainland.” Hong Kong Monetary Authority Research
Memoranda.
Hannan, E.J., and B.G. Quinn (1979), “The Determination of the Order
of an Autoregression,” Journal of the Royal Statistical Society B, 41:
190–195.
Hansen, Lars Peter, and Thomas J. Sargent (2000), “Wanting Robustness
in Macroeconomics.” Manuscript, Department of Economics, Stanford
University. Website: www.stanford.edu/˜sargent.
Hamilton, James D. (1989), “A New Approach to the Economic Anal-
ysis of Nonstationary Time Series Subject to Changes in Regime,”
Econometrica 57: 357–384.

226
Bibliography
——— (1990), “Analysis of Time Series Subject to Changes in Regime,”
Journal of Econometrics 45: 39–70.
——— (1994), Times Series Analysis. Princeton, NJ: Princeton University
Press.
Harvey, D, S. Leybourne, and P. Newbold (1997), “Testing the Equality of
Prediction Mean Squared Errors,” International Journal of Forecasting
13: 281–291.
Haykin, Simon (1994) Neural Networks: A Comprehensive Foundation.
Saddle River, NJ: Prentice-Hall.
Heer, Burkhard, and Alfred Maussner (2004), Dynamic General Equi-
librium Modelling-Computational Methods and Applications. Berlin:
Springer Verlag. Forthcoming.
Hess, Allan C. (1977), “A Comparison of Automobile Demand Functions,”
Econometrica 45: 683–701.
Hoffman,
Boris (2003),
“Bank Lending and Property Prices:
Some
International Evidence.” HKIMR Working Paper 22/2003.
Hornik, K., X. Stinchcomb, and X. White (1989), “Multilayer Feedforward
Networks are Universal Approximators.” Neural Net 2: 359–366.
Hsieh, D., and B. LeBaron (1988a), “Small Sample Properties of the BDS
Statistic, I,” in W. A. Brock, D. Hsieh, and B. LeBaron (eds.), Non-
linear Dynamics, Chaos, and Stability. Cambridge, MA: MIT Press.
——— (1988b), “Small Sample Properties of the BDS Statistic, II,” in
W. A. Brock, D. Hsieh, and B. LeBaron (eds.), Nonlinear Dynamics,
Chaos, and Stability. Cambridge, MA: MIT Press.
——— (1988c), “Small Sample Properties of the BDS Statistic, III,” in
W. A. Brock, D. Hsieh, and B. LeBaron (eds.), Nonlinear Dynamics,
Chaos, and Stability. Cambridge, MA: MIT Press.
Hutchinson, James M., Andrew W. Lo, and Tomaso Poggio (1994),
“A Nonparametric Approach to Pricing and Hedging Derivative
Securities Via Learning Networks,” Journal of Finance 49: 851–889.
Ingber, L. (1989), “Very Fast Simulated Re-Annealing,” Mathematical
Computer Modelling 12: 967–973.
Issing, Othmar (2002),“Central Bank Perspectives on Stabilization Policy.”
Federal Reserve Bank of Kansas City Economic Review, 87: 15–36.

Bibliography
227
Jarque, C.M., and A.K. Bera (1980), “Efficient Tests for Normality,
Homoskedasticity, and Serial Independence of Regression Residuals,”
Economics Letters 6: 255–259.
Judd, Kenneth L. (1998), Numerical Methods in Economics. Cambridge,
MA: MIT Press.
Kantz, H., and T. Schreiber (1997), Nonlinear Time Series Analysis.
Cambridge, UK: Cambridge University Press.
Kirkpatrick, S, C.D. Gelatt Jr., and M.P. Vecchi (1983), “Optimization
By Simulated Annealing,” Science 220: 671–680.
Ko˘cenda, E. (2001) An Alternative to the BDS Test: Integration Across
the Correlation Integral. Econometric Reviews 20, 337–351.
Krugman, Paul (1998), “Special Page on Japan: Introduction.” Webpage:
web.mit.edu/krugman/www/jpage.html.
Kuan, Chung-Ming, and Halbert White (1994), “Artifical Neural Networks:
An Econometric Perspective,” Econometric Reviews 13: 1–91.
Kuan, Chung-Ming, and Tung Liu (1995), “Forecasting Exchange Rates
Using Feedforward and Recurrent Neural Networks,”
Journal of
Applied Econometrics 10: 347–364.
Lai, Tze Leung, and Samuel Po-Shing Wong (2001), “Stochastic Neural
Networks with Applications to Nonlinear Time Series.” Journal of
the American Statistical Association 96: 968–981.
LeBaron, Blake (1998), “An Evolutionary Bootstrap Method for Selecting
Dynamic Trading Stratergies”, in A.-P. N. Refenes, A.N. Burgess and
J.D. Moody (eds.), Decision Technologies for Computational Finance,
Ansterdam: Kluwer Academic Publishers, 141–160.
Lee, T.H., H. White, and C.W.J. Granger (1992), “Testing for Neglected
Nonlinearity in Times Series Models: A Comparison of Neural Network
Models and Standard Tests,” Journal of Econometrics 56: 269–290.
Ljung, G.M., and G.E.P. Box (1978), “On a Measure of Lack of Fit in
Time Series Models.” Biometrika 65: 257–303.
Lumsdaine, Robin L., and D. H. Papell (1997), “Multiple Trend Breaks
and the Unit Root Hypothesis,” Review of Economics and Statistics:
212–218.
Mandic,
Danilo,
and Jonathan Chambers (2001),
Recurrent Neural
Networks for Prediction: Learning Algorithms, Architectures, and
Stability. New York: John Wiley and Sons.

228
Bibliography
McCarthy, Patrick S. (1996), “Market Price and Income Elasticities of
New Vehicles,” Review of Economics and Statistics 78: 543–548.
McKibbin, Warwick (2002), “Macroeconomic Policy in Japan,”
Asian
Economic Paper 1: 133–169.
———,
and Peter Wilcoxen (1998),
“The Theoretical and Empiri-
cal Structure of the G-Cubed Model,”
Economic Modelling 16:
123–148.
McLeod, A. I., and W.K. Li (1983), “Diagnostic Checking of ARMA Time
Series Models Using Squared-Residual Autocorrelations,” Journal of
Time Series Analysis 4: 269–273.
McNelis, P., and G. Nickelsburg (2002), “Forecasting Automobile Produc-
tion in the United States.” Manuscript, Economics Dept., Georgetown
University.
McNelis, Paul D., and Peter McAdam (2004), “Forecasting Inflation with
Thick Models and Neural Networks.” Working Paper 352, European
Central Bank. Webpage: www.ecb.int/pub/wp/ecbsp352.pdf.
Meltzer, Alan (2001), “Monetary Transmission at Low Inflation: Some
Clues from Japan,” Monetary and Economic Studies 19(S-1): 13–34.
Merton, Robert (1973), “An Intertemporal Capital Asset Pricing Model.”
Econometrica 41: 867–887.
Metropolis, N., A.W. Rosenbluth, M. N. Rosenbluth, A.H. Teller, and
E. Teller (1953), “Equation of State Calculations by Fast Computing
Machines,” Journal of Chemical Physics 21: 1087–1092.
Michalewicz, Zbigniew (1996), Genetic Algorithms + Data Structures =
Evolution Programs. Third Edition. New York: Springer-Verlag.
———, and David B. Fogel (2002), How to Solve It: Modern Heuristics.
New York: Springer-Verlag.
Miller, W. Thomas III, Richard S. Sutton, and Paul J. Werbos (1990),
Neural Networks for Control. Cambridge, MA: MIT Press.
Neft¸ci, Salih (2000), An Introduction to the Mathematics of Financial
Derivatives. San Diego, CA: Academic Press.
Perron, Pierre (1989), “The Great Crash, the Oil Price Shock, and the
Unit Root Hypothesis,” Econometrics 57: 1361–1401.

Bibliography
229
Pesaran, M.H., and A. Timmermann (1992), “A Simple Nonparametric
Test of Predictive Performance,” Journal of Business and Economic
Statistics 10: 461–465.
Qi, Min (1999), “Nonlinear Predictability of Stock Returns Using Finan-
cial and Economic Variables,” Journal of Business and Economics
Statistics 17: 419–429.
Quagliarella, Domenico, and Alessandro Vicini (1998), “Coupling Genetic
Algorithms
and
Gradient
Based
Optimization
Techniques,”
in
Quagliarella, D., J. Periaux, C. Poloni, and G. Winter (eds.), Genetic
Algorithms and Evolution Strategy in Engineering and Computer
Science: Recent Advances and Industrial Applications. West Sussex,
England: John Wiley and Sons, Ltd.
Quagliarella, D., J. Periaux, C. Poloni, and G. Winter (1998), Genetic
Algorithms and Evolution Strategy in Engineering and Computer
Science: Recent Advances and Industrial Applications. West Sussex,
England: John Wiley and Sons, Ltd.
Razzak, Weshah A. “Wage-Price Dynamics, the Labor Market, and
Deflation in Hong Kong.” HKIMR Working Paper 24/2003.
Rissanen, J. (1986a), “A Predictive Least-Squares Principle,” IMA Journal
of Mathematical Control and Information 3: 211–222.
——— (1986b),
“Stochastic Complexity and Modeling,”
Annals of
Statistics 14: 1080–1100.
Robinson,
Guy
(1995),
“Simulated
Annealing.”
Webpage:
www.npac.syr.edu/ copywrite/pcw/node252.
Ross, S. (1976), “The Arbitrage Theory of Capital Asset Pricing,” Journal
of Economic Theory 13: 341–360.
Rustichini, Aldo, John Dickhaut, Paolo Ghirardato, Kip Smith, and Jose
V. Pardo (2002), “A Brain Imaging Study of Procedural Choice,”
Working Paper, Department of Economics, University of Minnesota.
Webpage: http://www.econ.umn.edu/˜arust/ProcCh3.pdf.
Sargent, Thomas J. (1997), Bounded Rationalilty in Macroeconomics.
Oxford: Oxford University Press.
——— (1999), The Conquest of American Inflation. Princeton, NJ:
Princeton University Press.

230
Bibliography
Schwarz, G. (1978), “Estimating the Dimension of a Model,” Annals of
Statistics 6: 461–464.
Sims, Christopher (1992), “Interpreting the Macroeconomic Times Series
Facts: The Effects of Monetary Policy.” European Economic Review
36: 2–16.
———, and Mark W. Watson (1998), “A Comparison of Linear and
Nonlinear Univariate Models for Forecasting Macroeconomic Time
Series.” Cambridge, MA: National Bureau of Economic Research
Working Paper 6607. Website: www.nber.org/papers/w6607.
Stock, James H., and Mark W. Watson (1999), “Forecasting Inflation,”
Journal of Monetary Economics 44: 293–335.
Sundermann, Erik (1996), “Simulated Annealing.” Webpage: petaxp.rug.
ac.be/˜erik/research/research-part2.
Svensson, Lars E. O., (2003), “Escaping from a Liquidity Trap and
Deflation: The Foolproof Way and Others,” Journal of Economic
Perspectives.
Ter¨asvirta, T. (1994), “Specification, Estimation, and Evaluation of
Smooth-Transition Autogressive Models,” Journal of the American
Statistical Association 89: 208–218.
———, and H.M. Anderson (1992), “Characterizing Nonlinearities in
Business Cycles Using Smooth Transition Autoregressive Models,”
Journal of Applied Econometrics 7: S119–S136.
van Dijk,
Dick,
Timo Ter¨asvirta,
and Philip Hans Franses (2000),
“Smooth Transition Autoregressive Models—A Survey of Recent
Developments.” Research Report EI2000–23A. Rotterdam: Erasmus
University, Econometric Institute.
Tsay, Ruey S. (2002), Analysis of Financial Time Series. New York: John
Wiley and Sons, Inc.
van Laarhoven, P.J.M., and E.H.L. Aarts (1988), Simulated Annealing:
Theory and Applications. Boston, MA: Kluwer Academic Publishers.
Werbos, Paul John (1994), The Roots of Backpropagation: From Ordered
Derivatives to Neural Networks and Political Forecasting. New York:
Wiley Interscience.
White, Halbert (1980), “A Heteroskedasticity Covariance Matrix and a
Direct Test for Heteroskedasticity.” Econometrica 48: 817–838.

Bibliography
231
Wolkenhauer, Olaf (2001), Data Engineering. New York: John Wiley and
Sons.
Yoshino, Naoyuki and Eisuke Sakakibara (2002), “The Current State of
the Japanese Economy and Remedies,” Asian Economic Papers 1:
110–126.
Zivot, E., and D.W.K. Andrews (1992), “Further Evidence on the Great
Crash, the Oil Price Shock, and the Unit-Root Hypothesis,” Journal
of Business and Statistics 10: 251–270.


Index
Note: Page locators followed by
“n” refer to footnotes.
A
activation functions, 24–30
Gaussian, 26–28
radial basis, 28–29
ridgelet, 29–30
squasher, 24–28
tansig, 26
Akaike statistic, 86
American options, 138–139
analytic derivatives, 105–107
approximations in
decision-making, 23
arbitrage pricing theory (APT),
47–48, 116, 137–143
arithmetic crossover, 73
asset pricing
arbitrage pricing theory,
47–48, 116, 137–143
capital asset pricing model,
46–48
decision-making in, 46–49
in emerging markets,
122–125
intertemporal capital asset
pricing model, 47–48
thick modeling, 48
auto-associative mapping, 44, 46
autocorrelation coefficient, 87
automotive production
forecasting example,
145–155
data used in, 146–148
evaluation of, 150–152
interpretation of, 152–155
MATLAB program notes
for, 166
models used in, 148–150
autoregressive models, 14,
55, 177
B
backpropagation method, 69–70
bagging predictors, 78
banking intervention example,
204–209
bank lending, property prices
and, 173–174, 174n,
186–189, 195
233

234
Index
BFGS (Boyden-Fletcher-
Goldfarb-Shanno)
algorithm, 69, 78–80
black box criticism, 55–57
Black-Scholes options pricing
(BSOP) model, 116,
137–143
bond ratings, 53
bootstrapping methods
for assessing significance,
108
for in-sample bias, 101–102
for out-of-sample
performance, 202, 204
0.632 bootstrap test, 101–102,
202, 204
bounded rationality assumption,
7
Brock-Deckert-Scheinkman
(BDS) test, 91–92, 94
C
calendar effects, 61–63
call and put options, 1, 138–140
capital asset pricing model
(CAPM), 46–48
capital-asset ratio, 205–206
CAPM beta, 47
chaos theory, 117. See also
stochastic chaos (SC)
model
Chi-squared distribution, 87
Clark-West bias correction test,
98–99
classification networks, 37–38,
49–54, 58
classification problems, 2, 5,
199–210
closed form solutions, 20
conditional variance, 16–17
The Conquest of American
Inflation (Sargent), 56
control, 3
convergence
to absurd results, 105
in genetic algorithms, 75
local, 33–34, 68–71, 76, 105
corporate bonds example,
156–165
data in, 156–158
in-sample performance,
160–162
interpretation of results,
161–165
MATLAB program notes,
166
models used, 157–160
out-of-sample performance,
160–161
covariance stationary time
series, 59–61
credit card risk example,
200–205
crisp logic, 199
crossover, 73–74
cross-section analysis, 14n
cross-validation, 101
curse of dimensionality, 18,
41–42, 76
D
data preprocessing, 59–65
in corporate bonds example,
157–158
in out-of-sample evaluation,
95
scaling functions, 64–65, 84
seasonal adjustments, 61–63
stationarity, 59–61
data requirements, 102–103
data scaling, 64–65, 84, 109
decision-making
in asset pricing, 46–49
brain-imaging models of, 23
use of forecasting in, 3–5
deflation forecasting

Index
235
Hong Kong example,
168–182
importance of, 167–168
United States example,
174–175
DeLeo scaling function, 64–65
Dickey-Fuller test, 59–61
Diebold-Mariano test, 96–97
dimensionality reduction, 2–3,
41–46, 211–220
dimensionality reduction
mapping, 42, 44
directional accuracy test, 99–100
discrete choice, 49–54
discriminant analysis, 49–50
logit regression, 50–51
multinomial ordered choice,
53–54
neural network models for,
52–53
probit regression, 51–52
Weibull regression, 52
discriminant analysis, 49–50
in banking intervention
example, 207–209
in credit card risk example,
200–204
distorted long-memory (DLM)
model, 115–116,
135–137
dividend payments, 131
Durbin-Watson (DW) test, 87
E
economic bubbles, 135
election tournaments, 74–75
elitism, 75
Ellsberg paradox, 56
Elman recurrent network,
34–38, 58
emerging markets, use of neural
networks in, 8, 122–125
Engle-Ng test of symmetry of
residuals, 89, 94
Euclidean norm, 29
European options, 138
evaluation of network
estimation, 85–111
data requirements, 102–103
implementation strategy,
109–110
in-sample criteria, 85–94
interpretive criteria,
104–108
MATLAB programming
code for, 93–94,
107–108
out-of-sample criteria,
94–103
significance of results, 108
evolutionary genetic algorithms,
75
evolutionary stochastic search,
72–75
exchange rate forecasting,
100–101, 103
expanding window estimation,
95
expectations, subjective, 23
extreme value theory, 52
F
feedforward networks, 21–24
analytic derivatives and,
105–106
in discrete binary choice,
52–53
with Gaussian functions,
26–28
with jump connections,
30–32, 39–40
with logsigmoid functions,
24–28, 31
in MATLAB program,
80–82
multilayered, 32–34
with multiple outputs,
36–38

236
Index
feedforward networks, contd
in recurrent networks, 34–35
with tansig functions, 26
financial engineering, xii
financial markets
corporate bonds example,
156–165
intrinsic dimensionality in,
41–42
recurrent networks and
memory in, 36
sign of predictions for, 99
volatility forecasting
example, 211–220
finite-difference methods,
106–107
fitness tournaments, 73–75
forecasting, 2
automotive production
example, 145–155
corporate bonds example,
156–165
curse of dimensionality in,
18, 41–42, 76
data requirements in, 103
exchange rate, 100–101, 103
feedback in, 5
financial market volatility
example, 211–220
inflation, 37, 87, 104, 168–182
linear regression model in,
13–15
market volatility example,
211–220
multiple outputs in, 37
out-of-sample evaluation of,
95
predictive stochastic
complexity, 100–101
stochastic chaos model,
117–122
thick model, 77–78
use in decision-making, 3,
167–168
foreign exchange markets, 139n
forward contracts, 139n
“free parameters,” 55
fuzzy sets, 199
G
Gallant-Rossi-Tauchen
procedure, 62–63
GARCH nonlinear models,
15–20
development of, 15n
GARCH-M, 15–17
integrated, 132
model typology, 20–21
orthogonal polynomials,
18–20
polynomial approximation,
17–18
program notes for, 58
Gaussian function, 26–28, 51
Gaussian transformations, 28
GDP growth rates, 125–128
Geman and Geman theorem, 71
genetic algorithms, 72–75
development of, 6–7
evolutionary, 75
gradient-descent methods
with, 75–77
in MATLAB program,
78–80, 83–84
steps in, 72–75
Gensaki interest, 186–188
Gompertz distribution, 52
Gompit regression model, 52
goodness of fit, 86
gradient-descent methods, 75–77
Granger causality test, 195–196
H
Hang Seng index, 170, 172
Hannan-Quinn information
criterion, 85–86

Index
237
Harvey-Leybourne-Newbold size
correction, 97
health sciences, classification
in, 2n
Hermite polynomial expansion,
19
Hessian matrix, 67–69, 76
heteroskedasticity, 88–89, 91
hidden layers
jump connections and,
30–32
multilayered feedforward
networks in, 32–34
in principal components
analysis, 42
holidays, data adjustment for,
62–63, 62n
homoskedasticity tests, 88–89,
91
Hong Kong, inflation and
deflation example,
168–182
data for, 168–174
in-sample performance,
177–179
interpretation of results,
178–182
model specification, 174–177
out-of-sample performance,
177–178, 180
Hong Kong, volatility
forecasting example,
212–216
hybridization, 75–77
hyperbolic tangent function, 26
I
implementation strategy,
109–110
import prices, 170–171, 184–185
inflation forecasting
feedforward networks in, 37
Hong Kong example,
168–182
importance of, 167–168
moving averages in, 87
unemployment and, 104
in the United States,
174–175
initial conditions, 65, 118–119
input neurons, 21
in-sample bias, 101–102
in-sample evaluation criteria,
85–94
Brock-Deckert-Scheinkman
test, 91–92, 94
Engle-Ng test for symmetry,
89, 94
Hannan-Quinn information
statistic, 86
Jarque-Bera statistic,
89–90, 94
Lee-White-Granger test, 32,
90–91, 94
Ljung-Box statistic, 86–88,
94
MATLAB example of,
93–94
McLeod-Li statistic, 88–89,
94
in-sample evaluations
in automotive production
example, 150–151
in banking intervention
example, 205, 207
in Black-Sholes option
pricing models,
140–142
in corporate bond example,
160–162
in credit card risk example,
200–202
in distorted long-memory
models, 136–137
in Hong Kong inflation
example, 177–179

238
Index
in-sample evaluations, contd
in Hong Kong volatility
forecasting example,
213–214
in Japan inflation example,
189–191
in Markov regime switching
models, 128–130
in stochastic chaos models,
118–120
in stochastic volatility/jump
diffusion models,
123–124
in United States volatility
forecasting example,
216–218
in volatility regime
switching models, 132
interest rate forecasting, 37, 146
interpretive criteria, 104–108
intertemporal capital asset
pricing model
(ICAPM), 47–48
intrinsic dimensionality, 41–42
J
jacobian matrix, 107–108
Japan, inflation and deflation
model for, 182–196
data in, 184–189
in-sample performance,
189–190
interpretation of results,
191–196
model specification, 189
proposed remedies, 182–184
Jarque-Bera statistic,
89–90, 94
jump connections,
30–32, 39–40
K
kurtosis, 90
L
lagged values
in Elman recurrent network,
34–36
in evaluating models, 116
in implementation, 109
in Ljung-Box Q-statistic,
87–88
in nonlinear principal
components, 49
predictive stochastic
complexity, 100–101
Laguerre polynomial expansion,
19
land price index (Japan),
186–189, 193
latent variables, 23
learning parameters, 69
leave out one method, 101
Lee-White-Granger test, 32,
90–91, 94
Legendre polynomial expansion,
19
likelihood functions, 16–17
linear ARX model, 14n
linear discriminant analysis,
49–50
linear models, 13–15
advantages of, 15
in automotive production
forecasting, 148–152
as benchmark, xii
in corporate bond example,
159–165
in Hong Kong inflation
example, 176–180
in Japan inflation example,
189–192
use of residuals from, 32, 34
linear principal components
analysis (PCA), 42–43,
211–220
linear scaling functions, 64

