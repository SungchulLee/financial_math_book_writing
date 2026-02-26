# Bayesian Portfolio Selection & Asset Pricing

!!! info "Source"
    **Bayesian Methods in Finance** by Svetlozar T. Rachev, John S.J. Hsu, Biliana S. Bagasheva, and Frank J. Fabozzi, Wiley, 2008.
    These notes are used for educational purposes.

## Bayesian Portfolio Selection

60
BAYESIAN METHODS IN FINANCE
where the degrees of freedom parameter is ν* =T −K + N + 1 and the
scale matrix is S = (Y −XB)′(Y −XB).
A full Bayesian informative prior approach to estimation of the multi-
variate linear regression model would require one to specify proper prior
distributions for the regression coefficients, β, and the covariance matrix, .
The conjugate prior scenario is invariably the scenario of choice so as to
keep the regression estimation within analytically manageable boundaries.
That scenario consists of a multivariate normal prior for β and inverted
Wishart for . See Chapters 6 and 7 for further details.
SUMMARY
In this chapter, we discussed Bayesian inference for the univariate and mul-
tivariate linear regression models. In a normal setting and under conjugate
priors, the posterior and predictive results are standard. Increased flexibility
can be achieved by employing alternative distributional assumptions. Model
estimation then is aided by numerical computational methods. We cover
the most important posterior simulation and approximation methods in the
next chapter; many of them we extend in the following chapters.

CHAPTER5
Bayesian Numerical Computation
T
he advances in numerical computation methods in the last two decades
have been the driving force behind the growing popularity of the Bayesian
framework in empirical statistical and financial research. These methods
provide a very flexible computational setting for estimating complex mod-
els in which the traditional, frequentist framework sometimes requires
much more effort and may encounter estimation problems. The goal of
the numerical computational framework is to generate samples from the
posterior distribution of the parameters as well as the predictive distribution
in situations when analytical results are unavailable. Increased model man-
ageability comes at a cost, however. Careful design of the sampling schemes
is required to ensure that posterior and predictive inference are reliable.
In this chapter, we lay the foundation for the numerical computation
framework. We revisit different aspects of it in the following chapters—in
the context of particular financial applications.
MONTE CARLO INTEGRATION
In (natural) conjugate scenarios, such as the ones discussed in Chapters 2
and 3 (normal-inverse gamma and binomial beta), the posterior parameter
distributions and the predictive distributions are recognizable as known
distributions. If one is, for example, interested in estimating the posterior
(predictive) mean, analytical expressions for it are readily available. Equiva-
lently, the integral defining the posterior mean can be computed analytically.
Denoting the unknown parameter vector by θ and the observed data by y,
the posterior mean of a function g(θ) is given by
Eg(θ) | y) =

g(θ) p(θ | y) dθ,
(5.1)
where p(θ | y) is θ’s posterior distribution. In the general case, it might not be
possible to evaluate the integral in (5.1) analytically. Then, one can compute
61

62
BAYESIAN METHODS IN FINANCE
an approximation of it which, by a fundamental result in statistics, called
the Law of Large Numbers, can be made arbitrarily close to the integral
above. Suppose we have been able to obtain a sample θ (1), θ (2), . . . , θ (M)
from p(θ | y).1 The quantity

gM(θ) = 1
M
M

m=1
g

θ (m)
(5.2)
can be shown to converge to Eg(θ) | y) as M goes to infinity.2 That is, the
larger the sample from θ’s posterior distribution, the more accurately we
can approximate (estimate) the expected value of g(θ). This approxima-
tion procedure lies at the center of Monte Carlo integration. The Monte
Carlo approximation, 
gM(θ), is nothing more than a sample average. Using
results from asymptotical statistics, one could evaluate the quality of the
approximation (i.e., what the imprecision in estimating Eg(θ) | y) is from
using only a finite sample of observations). The asymptotic variance of

gM(θ) is σ 2/M.3 The variance of g(θ), σ 2, can be estimated with the sample
variance,
s2
M =



 1
M
M

m=1

g(θ (m)) −
gM(θ)
2.
The measure of numerical accuracy is then provided by the Monte Carlo
Standard Error (MCSE),4
MCSE =
	
S2
M
M .
(5.3)
1The Law of Large Numbers requires that θ(i) are independent realizations (sim-
ulations) from the distribution of θ. Similar results hold, however, for dependent
realizations as well, as will be the case with the Markov Chain Monte Carlo
simulations that we discuss later in the chapter.
2The convergence is in probability, given the sample of realizations y and provided
the expectation in (5.1) exists. See any text in basic probability theory such as Feller
(2001) and Chung (2000).
3The
asymptotic
distribution
of
the
estimator
of
g(θ),

gM(θ),
is
normal,
N(g(θ), σ 2/M).
4The expression in (5.3) could be used as a practical indication for the number
of draws, M, necessary for an adequate approximation to g(θ). For example, M =
10,000 means that the error due to approximation is 1% of the standard deviation
of g(θ)’s posterior distribution.

Bayesian Numerical Computation
63
The usefulness of Monte Carlo approximation becomes apparent when
one considers the fact that probabilities can be expressed as expectations.
For example, the probability of some subset A of values of θ is expressed as
the expectation
P(θ is in A) = E

I{A}(θ)

,
where I{A}(θ) is an indicator function taking value of 1 if θ is in A and a value
of 0 if θ is not in A. The Monte Carlo approximation of the expectation
above would give
P(θ is in A) ≈1
M
M

m=1
I{A}(θ (m)).
That is, to approximate the probability, one would simply compute the
proportion of times θ takes a value in A in the simulated sample of size M.
Even though the Monte Carlo approximation might seem like an
easy way to deal with complicated situations, it turns out not to be
the best approach in practice. First, the estimators produced as a result
do not necessarily have the smallest approximation error. Second, while
obtaining samples from standard distributions is usually easy, the posterior
distributions one comes across in practice are often not of familiar form.
Direct simulation from the posterior (as above) is then not possible, and
posterior and predictive inferences require the use of simulation algorithms.
We discuss posterior simulations next.
ALGORITHMS FOR POSTERIOR SIMULATION
Algorithms for simulation from the posterior distribution can be divided
into categories:
■Independent simulation. Algorithms that produce an independent and
identically distributed (i.i.d.) sample from the posterior.5
■Dependent simulation. Algorithms whose output (after convergence) is
a sample of (nearly) identically distributed (but not independent) draws
from the posterior.
5Although, formally, the direct posterior simulation is a member of this category,
here we only include algorithms targeted at cases when the posterior cannot be
sampled directly.

64
BAYESIAN METHODS IN FINANCE
The algorithms from the first category can be seen as precursors to the
ones from the second category. Posterior simulation in practice frequently
uses a mixture of the algorithms in the two categories, as we see in the
chapters ahead.
Representatives of the first category are importance sampling and
rejection sampling. In the second category fall all algorithms based on
generation (simulation) of a Markov chain—the so-called Markov Chain
Monte Carlo (MCMC) methods. We discuss both categories next.
Rejection Sampling
Rejection sampling, one of the early algorithms for posterior simulation,
rests on a simple idea: find an ‘‘envelope’’ of the posterior density, obtain
draws from the envelope, and discard those that do not belong to the
posterior distribution. In order to employ the rejection sampling algorithm,
the posterior must be known (up to a constant of proportionality), although
not recognizable as a standard distribution. Recall that the constant of
proportionality is given by the denominator of the ratio in the Bayes’
theorem (see Chapter 3).
More formally, suppose that a function h(θ) is available, such that
p(θ | y) ≤Kh(θ),
where K is a constant greater than 1. Then, h(θ) plays the role of the
envelope function. Notice that h(θ) could be a density function itself, but
this is not necessary.6 The role of K is to make sure that the inequality is
satisfied for all values of θ.
The rejection sampling algorithm procedure for obtaining one draw
from the posterior of θ consists of the following steps:
1. Draw θ from h(θ) and denote the draw by θ ∗.
2. Compute the ratio
a = p(θ ∗| y)
Kh(θ ∗) .
(5.4)
3. With probability a, accept the draw θ ∗as a draw from the posterior,
p(θ | y). If θ ∗is rejected, go back to step (1). To decide whether to accept
6In Chapter 12, for example, in the context of stochastic volatility modeling, we
mention the adaptive rejection algorithm of Gilks and Wild (1992) for a univariate
posterior, in which h(θ) is a piecewise linear approximation to the posterior and is
not a density.

Bayesian Numerical Computation
65
−15
−10
−5
0
5
10
15
20
0
0.05
0.1
0.15
0.2
0.25
 
Target density
Envelope
Accepted draws
Rejected draws
EXHIBIT 5.1
The rejection sampling algorithm
or not, draw one observation, u, from the uniform distribution on (0, 1)
U(0, 1) if u ≤a, accept θ ∗. If u > a, reject θ ∗.
We can observe that the greater is K, the bigger the ‘‘discrepancy’’
between p(θ | y) and the lower the probability of accepting draws from h(θ).
Finally, repeating the steps of the rejection sampling algorithm many times
produces a sample exactly from the posterior density. This is graphically
illustrated in Exhibit 5.1 for the univariate case. Draws of θ, corresponding
to points under the posterior density curve (the filled circles on the graph),
are accepted, while draws corresponding to points falling in the area outside
of the posterior density curve (the empty circles on the graph) are rejected.
The acceptance probability, a, represents the ratio of the heights of the
posterior density curve and the envelope curve at a particular value of θ.
Importance Sampling
An algorithm, related to rejection sampling, for approximating expectations
is the importance sampling algorithm. Its underlying idea is to increase the
accuracy (decrease the variance) of an estimator by weighting more the sim-
ulations that are more important (likely), hence its name. Unlike the
rejection sampling algorithm, importance sampling draws are obtained

66
BAYESIAN METHODS IN FINANCE
from a density approximating the posterior density. The posterior density
kernel (unnormalized posterior density) is, as before, denoted as p(θ | y).
Suppose h(θ) is a probability density function, sampling from which is easy.
(It may be a function of the data y, but we suppress this notationally.) As
explained earlier, many quantities of interest (such as probabilities) can be
expressed as expectations; therefore, here we simply suppose that the pos-
terior expectation of a function g(θ) needs to be evaluated. The expectation
is written as7
E

g(θ) | y

=

g(θ)p(θ | y) d θ

p(θ | y) d θ
=

g(θ)h(θ)p(θ | y)/h(θ) d θ

p(θ | y)h(θ)/h(θ) d θ
.
(5.5)
The expression in (5.5) becomes more palatable when we define the follow-
ing ratio, called the ‘‘importance weight,’’
ω(θ) = p(θ | y)
h(θ) ,
(5.6)
which is the same as a in (5.4) above. Then (5.5) becomes
E

g(θ) | y

=

g(θ)h(θ)ω(θ) d θ

h(θ)ω(θ) d θ
≈
1
M
M
m=1 g

θ (m)
ω

θ (m)
1
M
M
m=1 ω

θ (m)
,
where θ (m), m = 1, . . . , M, are (i.i.d.) simulations from h(θ). The estimator
above has a smaller approximation variance the less variable the weights,
ω(θ (m)), are. Therefore, the choice of approximating density, h(θ), is essential.
In practice, one would select h(θ) so as to match the mode and shape (scale)
of the target density. (See the discussion of the Independence-Chain M-H
algorithm later in this chapter.)
MCMC Methods
Simulating i.i.d. draws from a complicated posterior density (or from an
appropriately chosen approximating density) is not always possible. The
posterior simulation algorithms, collectively known as MCMC methods,
provide iterative procedures to approximately sample from complicated
7Notice that, since p(θ | y) is unnormalized, it is not possible to evaluate the
expectation unless we know the constant of proportionality—the integral in the
denominator of (5.5). We can, however, approximate it together with the numerator,
as we see shortly.

Bayesian Numerical Computation
67
posterior densities (including in high-dimensional settings) by avoiding the
independence assumption. At each step, the algorithm attempts to find
parameter values with higher posterior probability, so that the approxima-
tion moves closer to the target (posterior) density. The purpose of applying
the algorithms remains the same—to approximate the expectations of func-
tions of interest with their sample averages. The difference is that the
simulations of θ, at which the sample averages are computed, are obtained
as the realizations of Markov chains.8 In fact, the Markov chain needs
to run for a sufficiently long time in order to ensure that the simulations
are indeed draws from θ’s posterior distribution.9 Then, we say that the
chain has converged. We discuss some practical rules to determine whether
convergence has occurred later in the chapter. We now proceed with a
closer look at the two most commonly employed MCMC methods—the
Metropolis-Hastings algorithm and the Gibbs sampler.
The Metropolis-Hastings Algorithm
The Metropolis-Hastings (M-H) algo-
rithm is related to both rejection sampling and importance sampling
discussed earlier.10 Let p(θ | y) again denote the unnormalized posterior
density, sampling from which is not possible. Here, we consider the general
case in which θ is a K-dimensional parameter vector, θ = (θ1, θ2, . . . , θK).
Denote by q(θ | θ (t−1)) the approximating density, called the ‘‘proposal den-
sity’’ or the ‘‘candidate-generating density.’’ The purpose of the proposal
8A Markov chain is a random process in discrete time (a sequence of random
variables) such that any state of the process depends on the previous state only and
not on any earlier state. We say that the process possesses the Markov property.
Denoting the random process by {Xn}∞
n=1, the Markov property is expressed as
P(Xn = xn | Xn−1 = xn−1, Xn−2 = xn−2, . . . , X1 = x1) = P(Xn = xn | Xn−1 = xn−1).
The collection of all possible values of the process is called the state space. In the
context of posterior simulations, the state space is the parameter space. For more
information on Markov Chains, see, for example, Norris (1998).
9A Markov chain has to satisfy a number of properties (such as irreducibility and
ergodicity) in order to be able to converge to its so-called ‘‘stationary distribution’’
(and for its stationary distribution to exist at all). Generally, these properties mean
that the chain can reach any state from any other state in a finite number of steps
(including a single step). See any probability text for rigorous definitions of the
properties of Markov chains. Usually, the chains arising in MCMC satisfy these
prerequisites.
10The algorithm was developed by Metropolis, Rosenbluth, Rosenbluth, Teller, and
Teller (1953) and extended by Hastings (1970).

68
BAYESIAN METHODS IN FINANCE
density is to randomly generate a realization of θ given the value at the
previous iteration of the algorithm.
The algorithm consists of two basic stages: first, a draw from the
proposal density is obtained and second, that draw is either retained or
rejected. More precisely, to obtain a sample from the posterior of θ, the
M-H algorithm iterates the following sequence of steps 2 through 5:
1. Initiate the algorithm with a value θ (0) from the parameter space of θ.
2. At iteration t, draw a (multivariate) realization, θ ∗, from the proposal
density, q(θ | θ (t−1)), where θ (t−1) is the parameter value at the previous
step.
3. Compute the acceptance probability, given by
a

θ ∗, θ (t−1)
= min

1,
p

θ ∗
/ q

θ ∗| θ (t−1)
p

θ (t−1)
/ q

θ (t−1) | θ ∗

,
(5.7)
where we suppress notationally the dependence on the data, y, for
simplicity.
4. Draw u from the uniform distribution on (0, 1), U(0, 1). Then,
■If u ≤a

θ (t), θ (t−1)
, set θ (t) = θ ∗.
■Otherwise, set θ (t) = θ (t−1).
5. Go back to step 2.
The algorithm is iterated (steps 2 through 5 repeated) a large number of
times. Only the simulations obtained after the chain converges are regarded
as an approximate sample from the posterior distribution and used for
posterior inference. (See the discussion on convergence diagnostics later in
the chapter for further details.) Notice that knowledge of the constant of
proportionality of θ’s posterior density is not necessary; since the constant
is present in both the numerator and the denominator in (5.7), it cancels
out anyway.
The adequate selection of proposal densities has been the focus of
considerable research efforts. We outline two main classes of proposal
densities, giving rise to two versions of the M-H algorithm.
Random Walk M-H Algorithm
Suppose one does not have in mind a distri-
bution that could be regarded as a good approximation of the posterior
density. Then, one would simply want to construct a chain that can explore
the parameter space well (visit areas of both high and low posterior proba-
bility). The relation between successive states of the chain (realizations of θ)
could be described by
θ (t+1) = θ (t) + ϵ(t+1),
(5.8)

Bayesian Numerical Computation
69
where ϵ(t+1) is a (K-dimensional) zero-mean random variable distributed
with q. The proposed draw of θ at each iteration of the algorithm is then
equal to the current draw plus random noise. The choice of ϵ’s distribution
is driven by convenience and most often a multivariate normal distribution.
The proposal distribution is then11
q

θ ∗|θ (t−1)
= N

θ (t−1), 

(5.9)
When the proposal distribution, q, is symmetric (which is not required,
although usually the case), the acceptance probability in (5.7) is simplified to
a

θ ∗, θ (t−1)
= min

1,
p

θ ∗
p

θ (t−1)

.
(5.10)
The algorithm can now be given an intuitive explanation: When the pro-
posed draw has a higher posterior probability than the current draw, it is
always accepted (a is then equal to 1); when the proposed draw has a lower
posterior probability than the current draw, it is accepted with probability a.
The simplicity of the random walk M-H algorithm might be deceptive.
If the jumps the chain makes are ‘‘too’’ large, chances are that the generated
(proposed) draws come from areas of the parameter space that have low
posterior probability. Then the acceptance probability would be very low
and most proposed draws would be rejected. The chain would ‘‘get stuck’’
at a particular value of θ and move only rarely. If the jumps the chain makes
are too small, then the chain would tend to remain in the same area of the
parameter space (of either high or low posterior probability). The acceptance
probability would then be very high and most proposed draws would be
accepted. Clearly, both scenarios are not desirable since, in order to achieve
convergence of the chain, one would have to waste substantial computing
time. The quantity that regulates the jump size and requires careful tuning
is the covariance matrix, , of the proposal distribution in (5.9).
The easiest way to select  is to set it equal to the scaled covariance
matrix, S, where S is estimated as the negative inverse Hessian evaluated
at the mode (see the discussion of the independence chain M-H algorithm
below),
 = cS.
The scale constant, c, is the tuning parameter that can be adjusted to
yield a reasonable acceptance rate (proportion of accepted draws of θ). It
11See the appendix to Chapter 3 for the definition of the multivariate normal
distribution.

70
BAYESIAN METHODS IN FINANCE
has been shown that when the proposal distribution is one-dimensional,
the optimal acceptance rate is around 0.5, whereas when it is multidi-
mensional, the optimal acceptance rate is around 0.23.12 We should note
that these rates are asymptotic results and might not be achieved if, for
instance, the chain has been run for an insufficient amount of time. How-
ever, they are useful as guidelines. In practice, one should perform any
tuning of the covariance of the proposal distribution (by increasing or
decreasing c, so as to match the desired acceptance probability) in a pre-
liminary run of the algorithm; then, using fixed  = cS, run the chain until
its convergence. (Otherwise, adjusting c during the algorithm’s main run
might result in the chain converging to a distribution different from the
posterior.)
Independence Chain M-H Algorithm
In contrast to the random walk M-H
algorithm, where the proposal distribution at each iteration is centered at
the most recent draw, the independence chain M-H algorithm, candidate
draws are obtained regardless of the chain’s current state. Employing this
version of the M-H algorithm is appropriate when an adequate approximat-
ing density has been determined. The multivariate normal and multivariate
Student’s t-distributions are the common choices for a proposal density
(and they, of course, best approximate unimodal and nearly symmet-
ric posteriors13). In fact, when a diffuse prior has been specified for the
model parameters, and especially when the data sample is not large, the
multivariate Student’s t-distribution is preferable to the multivariate nor-
mal distribution, as it can better approximate the tails of the posterior
distribution.
The next step after selecting the proposal density is to center it and scale
it to match the posterior as closely as possible. To do this, one needs to:
1. Find the posterior mode, θ, of the (unnormalized) posterior distribu-
tion.14 Since, most often, the posterior density is complicated, one would
have to resort to numerical optimization, which can be performed with
most commercial software products.15
2. Compute the Hessian, H, of the logarithm of the (unnormalized)
posterior density, evaluated at θ. The Hessian is simply the matrix of
12See Gelman, Roberts, and Gilks (1996) and Roberts, Gelman, and Gilks (1997).
13See Geweke (1989) for a discussion of the so-called ‘‘split–normal’’ and
‘‘split-Student’s t’’ distributions designed to accommodate skewed posteriors.
14The mode is the value of θ that maximizes the posterior. In practice, it is easier to
maximize the logarithm of the posterior distribution.
15For instance, MATLAB, S-PLUS or SAS/IML.

Bayesian Numerical Computation
71
second partial derivatives of a function. In this case, H is the matrix of
second derivatives of log(p(θ | y)) with respect to the components of θ.
The Hessian (evaluated at the mode) is usually provided by commercial
software products as a byproduct of the numerical optimization routine
for finding the maximum-likelihood estimate, θ.
The multivariate normal proposal density becomes16
q

θ | θ (t−1)
= q (θ) = N
θ, −H−1
.
(5.11)
In order to ensure that the proposal density adequately envelops the
posterior density, it might be a good idea to scale up (inflate) the normal
covariance matrix in (5.11). The scale could be employed, as explained
earlier, to adjust the acceptance rate. For example, Geweke (1994) uses a
factor of 1.22, so that the covariance matrix becomes −1.22 H−1.
The multivariate Student’s t proposal density is written as17
q

θ | θ (t−1)
= q (θ) = t

ν, θ, −(H)−1(ν −2)/ν

,
(5.12)
where the degrees-of-freedom parameter, ν, is usually set at a low value
such as ν = 5 (thus producing a heavy-tailed proposal density).18 To sample
from the proposal distribution in (5.12), draw θ from the (standardized)
multivariate Student’s t with ν degrees of freedom, centered around 0 and
with scale equal to the identity matrix, t

ν, 0, IK

. Then, transform θ by
scaling and centering to obtain the draw of θ,
θ = θ + θ

−(H)−1(ν −2)/ν

.
16This result comes from maximum likelihood theory. The multivariate normal
distribution in (5.11) is the asymptotic distribution of the maximum-likelihood
estimator, θ.
17In Chapter 3, we adopted the notation t(ν, µ, S) for the multivariate Stu-
dent’s t-distribution, where S is the distribution’s scale matrix and ν is the
degrees-of-freedom parameter. The quantity −H−1 is the estimator of the (asymp-
totic) covariance matrix of the maximum-likelihood estimator, θ, while the covari-
ance matrix of the multivariate Student’s t-distribution is given by  = Sν/(ν −2).
Whence, the form of the scale matrix in (5.12).
18Recall that when ν is equal to 2 or less, the Student’s t-distribution is so
heavy-tailed that its covariance does not exist. As ν increases, the tails become
thinner and for values of ν exceeding 30, the univariate Student’s t-distribution
behaves approximately like a normal distribution. (In general, for a given dimension
of the random variable, the higher ν is, the closer the Student’s t is to the normal
distribution.)

72
BAYESIAN METHODS IN FINANCE
We can observe that, in the case of the independence chain M-H
algorithm, the acceptance probability, a

θ ∗, θ (t−1)
, becomes
a

θ ∗, θ (t−1)
= min

1,
ω(θ ∗)
ω

θ (t−1)

,
(5.13)
where ω(θ) = p(θ)/q(θ) is the importance weight in (5.6).
Block Structure M-H Algorithm
Finally, as a transition to our discussion of
an important special case of the M-H algorithm, the Gibbs sampler, we
consider one M-H algorithm’s implementation issue. Most often than not,
it is not possible to identify an adequate proposal (approximating) density,
q(θ), for the posterior distribution of the whole parameter vector, θ. Instead,
one can easily specify proposals for blocks of the parameter vector. Suppose,
for example, that θ is partitioned as
θ =

θ1, θ2

,
where the blocks, θi, i = 1, 2, could be vectors themselves or scalars.
Further, suppose that one determines two suitable proposals for the
conditional posterior densities p1

θ1 | θ2, y

and p2

θ2 | θ1, y

. Denote the
respective proposal densities by
q1

θ1 |θ (t−1)
1
, θ2

and
q2

θ2 |θ (t−1)
2
, θ1

.
Certainly, q1 and q2 could be independent of θ (t−1)
1
and θ (t−1)
2
, respectively,
as is the case in the independent chain M-H algorithm. It can be shown
that successive sampling from these two proposal densities produces an
approximate sample from the joint posterior density, p(θ | y). Steps 2
through 4 at iteration t of the M-H algorithm outlined earlier are modified
as follows to accommodate this successive sampling. At iteration t,
1. Draw a realization θ ∗
1 from the conditional proposal density, q1

θ1 | θ (t−1)
1
,
θ (t−1)
2

, where θ (t−1)
i
, i = 1, 2, are the values of the two blocks at the
previous iteration of the algorithm.
2. Compute the acceptance probability in (5.7) modified in the obvious
way.
3. Accept or reject θ ∗
1 as explained earlier.

Bayesian Numerical Computation
73
4. Draw a realization θ ∗
2 from the conditional proposal density, q2

θ2 | θ (t)
1 ,
θ (t−1)
2

, where θ (t)
1 is the value of θ1 obtained in step (4.1) and θ (t−1)
2
is the
value of θ2 at the previous iteration of the algorithm.
5. Compute the acceptance probability in (5.7) modified in the obvious
way.
6. Accept or reject θ ∗
2 as explained earlier.
Often, the estimated model itself suggests the block structure of the
parameter vector, θ. Functional characteristics of the parameters could
be one structure criterion. In a linear regression model, for example,
the regression parameter vector, β, could constitute one block and the
disturbance variance, σ 2 another.19
The Gibbs Sampler
The Gibbs sampler could be seen as a special version
of the M-H algorithm and, more specifically, an extension to the block
structure M-H algorithm discussed earlier. It requires that one be able
to sample directly from the (full) conditional posterior distributions of
the (blocks of) components of θ. Let the K-dimensional parameter vector
be partitioned into q components as θ = (θ1, θ2, . . . , θq). Then, the full
conditional posterior distribution of θi, i = 1, . . . , q, is given by
p(θi | θ1, . . . , θi−1, θi+1, . . . , θq, y) ≡p(θi | θ−i, y).
(5.14)
Assuming these are all standard distributions, the Gibbs sampler algo-
rithm is given by the following steps:
1. Initialize the chain by selecting the starting values for all components,
θ (0)
i , i = 1, . . . , q.
2. At iteration t, obtain the draw of θ = (θ1, θ2, . . . , θq) by drawing and
updating successively its components, as follows:
■Draw an observation, θ (t)
1 from p(θ1 | θ (t−1)
2
, θ (t−1)
3
, . . . , θ (t−1)
q
, y).
■Draw an observation, θ (t)
2 from p(θ2 | θ (t)
1 , θ (t−1)
3
, . . . , θ (t−1)
q
, y).
■Cycle through the rest of the components, θ3, . . . , θq, in a similar
way.
3. Repeat step (2) until convergence is achieved.
Knowledge of the full conditional posterior distributions amounts to
using an acceptance probability equal to one in the M-H algorithm, and
there is no need for a rejection step.
19See further the discussion of volatility models estimation in Chapters 11 and 12.

74
BAYESIAN METHODS IN FINANCE
In many situations, the full conditional posterior distribution of at least
one component would not be recognizable as a standard distribution. Then
a proposal density for that conditional posterior distribution needs to be
identified and the algorithm above modified by including a rejection step in
the manner discussed earlier in the chapter. We thus obtain a hybrid M-H
algorithm.
Predictive Inference
When one’s objective is to carry the model analysis
further than posterior inference and perform predictions for future periods,
simulation of the predictive distribution turns out to be straightforward,
given a posterior sample already obtained. Recall the definition of predictive
density from Chapter 3,
f(x+1 | x) =

f(x+1 | θ)π(θ | x) dθ,
where x+1 denotes the one-step-ahead realization of the random variable of
interest, f(x+1 | θ) is the density of the data distribution, and π(θ | x) is the
posterior density of θ. It can be shown that a draw from f(x+1 | x) can be
obtained as follows:
1. Draw from the posterior, π(θ | x), and denote the draw by θ ∗.
2. Draw from the data density, f(x+1 | θ ∗).
The first step is already accomplished in the posterior inference stage.
Simulating a sample from the predictive distribution, as well as performing
numerical analysis, such as predictive interval construction and hypothesis
comparison, then require minimal additional effort.
Convergence Diagnostics
Reliability of posterior inference based on a sim-
ulation algorithm depends mostly on whether the Markov chain has reached
convergence, so that the simulated sample is indeed a sample from the desired
posterior distribution.20 In posterior simulation, our goal is to construct a
Markov chain which explores the parameter space well, that is, a chain that
‘‘mixes’’ well. Situations in which the simulations get trapped in a certain
part of the parameter space for long periods of time are undesirable and can
occur when the autocorrelations between successive parameter draws are
high and decay slowly (simple autocorrelation plots would reveal if that is
the case). High autocorrelations would not prevent convergence. However,
20See Cowles and Carlin (1996) for a comparative review of various MCMC
convergence diagnostics.

Bayesian Numerical Computation
75
convergence might take longer to reach. Therefore, some adjustment of the
sampling scheme (for instance, a different partitioning of the parameter
vector and/or selection of different proposal distributions) is usually in
order. (See, for example, the discussion on stochastic volatility estimation
in Chapter 12.)
Because of the nature of the Markov chain (its Markov property in
particular), the influence of its starting point diminishes with an increasing
number of iterations and eventually vanishes. In order to minimize the effect
of the chain’s initial state, a fraction of the chain’s simulations, referred to as
burn-in fraction, is discarded and only the subsequent draws are employed
in posterior inference. There is no hard-and-fast rule to determine the size
of the burn-in fraction, which clearly depends on the chain’s mixing speed.
Fast-mixing chains might ‘‘forget their origin’’ after only several iterations,
while chains displaying high serial correlation of the draws might need up
to half of the iterations discarded (although that would demonstrate quite a
cautious approach). Convergence monitoring discussed below assumes that
the burn-in fraction of simulations has already been discarded.
Methods for assessing convergence rely on examining the stability
(through iterations) of the behavior of various quantities characterizing the
posterior distribution. Intuitively, if these quantities take very divergent
values at different points of the simulation sequence, then the chain has not
reached its stationary distribution yet.
Cumsum Convergence Monitoring
A simple monitoring tool is to visu-
ally inspect the plot of the standardized posterior means as functions of
the number of iterations—a stable dynamics indicates convergence.21 The
statistic is given by
CSi,m = 1
m
m
j=1

θ
(j)
i −θi

σi
,
(5.15)
for m = 1, . . . , M, where M is the after-burn-in number of simulations and
θi and σi are, respectively, the posterior mean and standard deviation of θ i.
The statistic CSi,m is expressed in terms of a parameter, θ i; one could, of
course, monitor convergence for the simulations of any function of θ i in the
same way. Convergence of the Markov chain is indicated by the statistic
settling to values close to zero.
Parallel Chains Convergence Monitoring
In less complicated models, when
simulations are not very computationally intensive, a widely recommended
approach is the one of Gelman and Rubin (1992). It is based on running
21See Yu and Mykland (1994) and Bauwens and Lubrano (1998).


## Bayesian Mean-Variance Analysis

76
BAYESIAN METHODS IN FINANCE
in parallel several independent chains, with pronouncedly different starting
values. Convergence is present when outputs from the chains are similar
enough. The degree of similarity is measured by how close the average
variance of the (after-burn-in) simulations for a particular chain is to the
variance of the posterior means across chains. To simplify notation, sup-
pose we are only interested in inference for one parameter, denoted by
θ (this could be a function of θ as well). Suppose that R parallel chains
are run. The ith (i = 1, . . . , M) simulation of θ from the rth (r = 1, . . . ,
R) chain is denoted by θ (i,r). The average within-sequence variation is esti-
mated by
W = 1
R
R

r=1

σ 2
r ,
(5.16)
where

σ 2
r =
M
i=1(θ (i,r) −θ (r))2
M −1
and
θ (r) =
M
i=1 θ (i,r)
M
.
(5.17)
The between-sequence variation is estimated by
B =
M
R −1
R

r=1
(θ (r) −θ)2,
(5.18)
where
θ = 1
R
R

r=1
θ (r).
(5.19)
The posterior variance of θ can be estimated in two ways. On the one
hand, one estimate is simply the within-sequence variation estimate, W. On
the other hand, the variance of θ can be estimated as a weighted average of
W and B,

var(θ) = M −1
M
W + 1
MB,
(5.20)
where we suppress notationally the conditioning on the data, y. Since
the chains are started from very far-apart initial parameter values, the

Bayesian Numerical Computation
77
between-sequence variation will be larger than the within-sequence varia-
tion before convergence. When convergence is present, one would expect
that

var(θ) is very close to W. Then one can compute the statistic,
Q =

var(θ)
W
,
(5.21)
whose value nears 1 at convergence. If the value of Q is much higher than
1, the chain run must be continued until convergence.
Linear Regression with Semiconjugate Prior
We now revisit the univariate regression model from Chapter 4 and illustrate
some of the posterior simulation techniques discussed above. We refer the
reader to Chapter 4 for the relevant notation.
In the previous chapter, in order to obtain analytically convenient
results, we considered the natural conjugate prior case for the parameters
of the normal regression model. In that scenario, the prior distribution of β
is conditional on the variance, σ 2, while its covariance matrix is often made
proportional to the matrix X′X (see Chapter 3)—assumptions that might
be considered unnecessarily restrictive.
Here, the prior variance of β is asserted independently of σ 2 and X,
while we still assume normal prior for β and inverted χ 2 prior for σ 2. These
assumptions give rise to the so-called ‘‘semiconjugate’’ prior scenario,
π(β) = N

β0, β

and
π(σ 2) = Inv-χ 2(ν0, c2
0),
(5.22)
where β0, β, ν0, and c2
0 are the hyperparameters determined in advance
(for example, estimated from running the model on a prior sample of data
or reflecting the researcher’s prior knowledge and intuition). Combining
(5.22) with the normal likelihood (see Chapter 3) gives the unnormalized
joint posterior of the model parameters,
p(β, σ 2) ∝(σ 2)−( n+ν0
2
+1)
× exp

−1
2σ 2

y −Xβ
′(y −Xβ

−1
2

β −β0
′−1
β

β −β0

−ν0c2
0
σ 2

,
(5.23)

78
BAYESIAN METHODS IN FINANCE
where n is the number of data records. The joint posterior density does
not assume a convenient analytical form as in the natural conjugate case.
However, if we consider it as a function of β (for a fixed σ 2) and as a
function of σ 2 (for a fixed β), we can obtain the full conditional posterior
distributions of β and σ 2 which do have standard distributional forms. The
conditional posterior of β can be shown to be multivariate normal,
p(β | σ 2, y, X) = N

β∗, Vβ

,
(5.24)
where
Vβ =
 1
σ 2 X′X + −1
β
−1
(5.25)
and
β∗= Vβ
 1
σ 2 X′X
β + −1
β β0

.
(5.26)
The conditional posterior of σ 2 is an inverted χ 2 distribution,
p(σ 2 | β, y, X) = Inv-χ 2
ν∗, c2∗
,
(5.27)
where
ν∗= n + ν0
(5.28)
and
c2∗= ν0c2
0 +

y −Xβ
′(y −Xβ

ν∗
.
(5.29)
The availability of the parameters’ full conditionals means that we can
now employ the Gibbs sampler to generate a sample from the joint posterior
distribution of β and σ 2 in (5.23).
Illustration
To illustrate the posterior simulation, we use the same set of
data as in the regression illustration in Chapter 4 and regress the returns
on the small-cap/small-BM portfolio on the returns on the five factors with
greatest explanatory power, obtained with principal components analysis.
The sample consists of 132 observations for each variable. In addition,
we use data recorded in an earlier period to compute the values of the
hyperparameters. We run the Gibbs sampler for 10,000 iterations, discard
the first 1,000 (the burn-in iterations), and use the rest to compute the
posterior means and numerical standard errors. Part A of Exhibit 5.2
presents these, as well as the 5th and 95th numerical percentiles. To
visualize the posterior distributions better, we can plot the histogram of

Bayesian Numerical Computation
79
A.
Prior Mean
Posterior Mean
Posterior Standard
Deviation
b0.05
b0.95
B.
Prior Mean
Posterior Mean
Posterior Standard
Deviation
b0.05
b0.95
b1
Intercept
0.0037
0.0044
(0.0008)
0.003
0.0057
0.0037
0.0043
(0.0009)
0.003
0.0058
b2
Factor 1
−0.2952
−0.3051
(0.0038)
−0.3112
−0.2988
−0.2952
−0.3047
(0.0036)
−0.311
−0.2993
b3
Factor 2
−0.4217
−0.4084
(0.009)
−0.4232
−0.3937
−0.4217
−0.4093
(0.0084)
−0.4218
−0.3943
b4
Factor 3
0.038
0.0696
(0.0157)
0.0438
0.0956
0.038
0.0687
(0.0153)
0.0448
0.0949
b5
Factor 4
−0.2784
−0.3709
(0.023)
−0.4081
−0.3326
−0.2784
−0.3687
(0.0232)
−0.4062
−0.3339
b6
Factor 5
0.1063
0.0424
(0.0337)
−0.0139
0.0979
0.1063
0.0446
(0.0332)
−0.0097
0.0994
s2
1.67e-04
1.54e-04
(1.67e-05)
1.29e-04
1.83e-04
1.67e-04
1.47e-4
1.53e-05
1.24e-04
1.78e-04
EXHIBIT 5.2
Posterior summaries: Gibbs sampler and M-H algorithm
the simulated observations; the histogram of the posterior draws of σ 2, for
instance, together with the ‘‘raw’’ simulations, can be seen in Exhibit 5.3.
Although superfluous for our analysis, for the sake of illustration, we
consider a M-H sampling scheme as well, in particular, a random walk
M-H algorithm. We use a multivariate normal jumping distribution for the
regression coefficients, β, and a univariate normal jumping kernel for σ 2. To
account for the positivity restriction of σ 2, any negative draws are simply
discarded.22 Notice that the posterior means and numerical errors in Part B
of Exhibit 5.2 are very close to those resulting from the Gibbs sampler (and
provide an indication that both chains have converged; see below as well).
The acceptance proportion for this M-H sampling scheme turns out to be
just above 0.18.
As a visual check of whether the chains (in the Gibbs sampler case
and the M-H algorithm case) have reached convergence, we examine the
plots of the parameters’ standardized ergodic averages (computed using the
post-burn-in simulations) against the number of iterations. For example,
Exhibit 5.4 provides this plot (from the Gibbs output) for β4 on the bottom.
Based on it, convergence has been achieved. The second graph in Exhibit 5.4
22This is, in general, an easy way to deal with parameter restrictions. No equivalent
approach exists in the classical, frequentist setting. However, if a large number of
the draws for a given parameter violate the parameter restriction and need to be
discarded, this might be a signal that the model is misspecified.

80
BAYESIAN METHODS IN FINANCE
1
1.2
1.4
1.6
1.8
2
2.2
2.4
0
100
200
300
400
500
600
0
1000 2000 3000 4000 5000 6000 7000 8000 9000
1
1.2
1.4
1.6
1.8
2
2.2
2.4
Number of Iterations
s2
x 10−4
x 10−4
EXHIBIT 5.3
Posterior simulations from posterior distribution
of σ 2 using Gibbs sampler
is the plot of the sample autocorrelation of the simulated sequence from the
distribution of β4. Since the autocorrelations decay very fast, we conclude
that the chain in this simple model mixes very well. The plots for the
remaining parameters are very similar.

Bayesian Numerical Computation
81
0
5
10
15
20
−0.2
0
0.2
0.4
0.6
0.8
Lag
Sample Autocorrelation
0
1000
2000
3000
4000
5000
6000
7000
8000
9000
−0.4
−0.3
−0.2
−0.1
0
0.1
0.2
0.3
0.4
Number of Iterations
CUSUM Statistic
EXHIBIT 5.4
Convergence diagnostics for β4: Gibbs sampler

82
BAYESIAN METHODS IN FINANCE
APPROXIMATION METHODS: LOGISTIC REGRESSION
In this section, we consider the estimation of one type of nonlinear regression
model, the logistic regression, to illustrate the way approximation methods
work. The logistic regression’s most important financial application is in
credit-risk modeling and, in particular, in modeling the probability of
default.
Denote the probability of default of a company by θ. Then the odds of
default are defined as
θ
1 −θ .
The logistic regression models the logarithm of the odds ratio as a
linear combination of a number of explanatory variables.23 The underlying
dependent variable, Y, in the regression is a binary (categorical) variable.24
It manifests itself in two states—default or no default—and these two
states are observable. For convenience, it is common to denote them by
1 and 0, respectively. The objective of the logistic regression is to predict
the probability for the dependent variable falling into one of the two
categories,
P(Y = 1) = θ
and
P(Y = 0) = 1 −θ.
(5.30)
The explanatory variables (which presumably influence the proba-
bility of default) could be company-specific characteristics or macroeco-
nomic variables. Suppose we have observations of the dependent variable
23In the logistic regression, the probability of default is estimated indirectly, through
the log-odds ratio. The reason for that transformation is to remove the boundedness
of the support of θ (defined on the interval [0, 1]). The odds transformation converts
[0, 1] into [0, ∞), while the log transformation converts [0, ∞) into (−∞, ∞).
It is then possible to model the logarithm of the odds as a linear combination of
empirically observed variables taking values on the whole real line.
24The logistic regression is one of several types of models for analyzing binary
data but it is usually favored by practitioners because of the ease of parameter
interpretation. Another is the probit model. Models applicable to situations in
which the dependent variable can fall into more than two categories (polytomous
data) exist. See Chapter 5 in McCullagh and Nelder (1999).

Bayesian Numerical Computation
83
and the p−1 explanatory variables for n companies, y1, y2, . . . , yn and
x1, x2, . . . , xp−1, respectively. Then, the logistic regression is repre-
sented by
αi ≡log

θi
1 −θi

= β0 + β1xi,1 + . . . + βp−1xi,p−1 = x′
iβ,
(5.31)
for
i
=
1,
. . . ,
n,
where
xi = (1,
xi, 1,
xi, 2, . . . , xi, p−1)′
and β = (β0, β1, β2, . . . , βp−1)′.25 The probability of default is then given
by
θi =
exp

x′
iβ

1 + exp

x′
iβ
.
(5.32)
The coefficients of the logistic regression, βj, j = 1, . . . , p −1, take on
the interpretation of the amount of change in the log-odds ratio for a unit
increase in xj.26
The binary dependent variable, Y, has the Bernoulli distribution. There-
fore, the likelihood function for the vector of regression coefficients, β, is
L(β | y) ∝
n

i=1
θ
yi
i (1 −θi)1−yi
=
n

i=1

exp(x′
iβ)
1 + exp(x′
iβ)
yi 
1
1 + exp(x′
iβ)
1−yi
=
exp(t′β)
n
i=1[1 + exp(x′
iβ)] ,
(5.33)
where t = n
i=1 xiyi.
Let π(β) be the prior density of β. The (unnormalized) posterior
distribution of β is then given by
p(β | y) ∝L(β | y)π(β)
=
exp(t′β)
n
i=1[1 + exp(x′
iβ)] π(β).
(5.34)
Suppose we are interested in performing posterior inference with respect
to (functions of) the regression coefficients, βi, or the unknown probabilities,
25The log-odds ratio, log(θi/(1 −θi)), can also be written as logit(θi).
26Sometimes, the effect of a change in xj is termed ‘‘multiplicative’’ since the unit
increase in xj translates into multiplying the odds ratio, θ/(1 −θ), by exp(βj).

84
BAYESIAN METHODS IN FINANCE
θ i. Denote such a function by the generic g(β). The posterior mean of g(β)
is given by
Eg(β) | y) =

g(β)p(β | y) dβ
= c−1

g(β)
exp(t′β)
n
i=1[1 + exp(x′
iβ)]π(β)dβ,
(5.35)
where c is the constant of proportionality omitted in (5.34). That constant
needs to be known in order to compute the expectation above and can be
found by the p-dimensional integration,27
c =

exp(t′β)
n
i=1[1 + exp(x′
iβ)]π(β)dβ.
(5.36)
The p-dimensional integrals in (5.35) and (5.36) are in general not
straightforward to compute, and even more so for dimensions greater than
4 (p > 4).
In what follows, we discuss how to use the approximations to the
posterior density to compute the posterior moments of (functions of) the
parameters, as well as the parameter’s marginal posterior densities.
The Normal Approximation
The normal approximation to the posterior density relies on a Taylor
expansion of the logarithm of the posterior density around the posterior
mode.28 The posterior mode of complicated posterior densities is usually
found numerically, using a computer software package. Consider a generic
27Recall, from Chapter 3, that this is the denominator in the Bayes formula.
28In mathematics, the Taylor series of a function is an infinite sum of the derivatives
of the function, evaluated at a single point. Denote the function by f(x) and take a
point a. Then, under some conditions about f(x), the Taylor series of f(x) is given by
T(x, a, n) = f(a) + d f(x)
dx

x=a
(x −a) + 1
2
d2 f(x)
d x2

x=a
(x −a)2
+ 1
3!
d3 f(x)
d x3

x=a
(x −a)3 + . . . + 1
3!
1
n!
dn f(x)
d xn

x=a
(x −a)n,
where ! denotes factorial and
df(x)
dx

x=a is a notation for the first derivative of f(x)
with respect to x, evaluated at a (it could be written alternatively as f ′(a)). The

Bayesian Numerical Computation
85
posterior density function of a parameter vector, η, denoted by p(η | y).
Denote the posterior mode by η. Then, under certain regularity condi-
tions, the logarithm of the posterior density can be approximated by its
second-order Taylor expansion around η as follows,
log

p(η | y)

≈log

p(η | y)

+ d log

p(η | y)

d η

η=η

η −η

+1
2

η −η
′ d2 log

p(η | y)

d ηη′

η=η

η −η

.
(5.37)
The second term on the right-hand side above is zero, since it represents
the first derivative of a function evaluated at the function’s maximum,
while the first term on the right-hand side is a constant with respect to η.
Therefore, the log-posterior is approximated as
log

p(η | y)

= const + 1
2

η −η
′ d2 log

p(η | y)

d ηη′

η=η

η −η

.
The second derivative of the log-posterior with respect to the compo-
nents of η, evaluated at the posterior mode, is the Hessian matrix, H. Taking
the exponential on both sides above, we obtain
p(η | y) ∝exp

−1
2

η −η
′(−H)

η −η

,
(5.38)
which we can recognize as the kernel of a multivariate normal distribution
with mean the posterior mode, η, and covariance matrix—the negative of
notation of the remaining terms in the infinite sum has an analogous meaning. With
a few exceptions for f(x), we can write that
f(x) = T(x, a, n) + Rn,
where Rn is a remainder term which approaches zero as n becomes infinitely large.
The Taylor expansion above can be used to provide an approximation to f(x). In
practice, a second-order Taylor series approximation usually provides results with
sufficient accuracy,
f(x) ≈T(x, a, 2) = f(a) + d f(x)
dx

x=a
+ 1
2
d2 f(x)
d x2

x=a
(x −a)2.

86
BAYESIAN METHODS IN FINANCE
the inverse Hessian matrix, −H−1. Notice that this normal approximation is
the same as the normal proposal density used in the independence chain M-H
algorithm. Provided that the sample size is large enough, the approximation
turns out to be very accurate.
The posterior moments of any function, g(η), of the parameter vector
can now be computed easily. First, simulate η from the normal distribution
in (5.38) above, then compute the values of g(η) at those simulations, and,
finally, use Monte Carlo integration discussed earlier in the chapter.
Illustration
The normal approximation discussed above can be used to
approximate the posterior distribution of β with density given in (5.34)
in the logistic regression case. As an illustration, we consider the dataset
of Johnson and Wichern (2002) for 46 companies recorded in a particular
year—two years prior to the default of 21 of them. The four variables
used as predictors for the probability of default are the following financial
ratios: cash flow/total debt, net income/total assets, current assets/current
liabilities, and current assets/net sales. Their values are observed for each of
the 46 companies in the sample. We consider the logistic regression model in
(5.31). The two categories of the binary dependent variable, Y, are coded as
‘‘1 = default’’ and ‘‘0 = no default.’’ The vectors of explanatory variables,
xi, i = 1, . . . , 46, have 1 as their first component and the four financial ratios
as the remaining four components. The dataset is given in Exhibit 5.5.
We employ the logistic regression to investigate the relationship between
the explanatory variables and the probability of default, and to predict the
probability, θ, that a company k with a given set of financial ratios, xk,1,
xk,2, xk,3, xk,4, will default in two-years time.
Suppose that the prior for the regression coefficients, β, is an uninfor-
mative, improper prior,
π(β) ∝1.
(5.39)
The posterior mode found by numerical maximization of the posterior
of β in (5.34) is
ˆβ = (5.31, −7.06, 3.50, −3.41, 2.98)′,
while the negative inverse Hessian matrix evaluated at the posterior mode is


5.60
−7.70
15.86 −2.24 −2.04
−7.70
35.73 −70.60
2.89
1.87
15.86 −70.60 185.18 −7.05 −0.68
−2.24
2.89
−7.05
1.45 −1.22
−2.04
1.87
−0.68 −1.22
9.41


.

Bayesian Numerical Computation
87
Companies in Future Default
Companies in No Future Default
yi
xi,1
xi,2
xi,3
xi,4
yi
xi,1
xi,2
xi,3
xi,4
1
−0.45
−0.41
1.09
0.45
0
0.51
0.10
2.49
0.54
1
−0.56
−0.31
1.51
0.16
0
0.08
0.02
2.01
0.53
1
0.06
0.02
1.01
0.40
0
0.38
0.11
3.27
0.35
1
−0.07
−0.09
1.45
0.26
0
0.19
0.05
2.25
0.33
1
−0.10
−0.09
1.56
0.67
0
0.32
0.07
4.24
0.63
1
−0.14
−0.07
0.71
0.28
0
0.31
0.05
4.45
0.69
1
0.04
0.01
1.50
0.71
0
0.12
0.05
2.52
0.69
1
−0.06
−0.06
1.37
0.40
0
−0.02
0.02
2.05
0.35
1
0.07
−0.01
1.37
0.34
0
0.22
0.08
2.35
0.40
1
−0.13
−0.14
1.42
0.44
0
0.17
0.07
1.80
0.52
1
−0.22
−0.30
0.33
0.18
0
0.15
0.05
2.17
0.55
1
0.07
0.02
1.31
0.25
0
−0.10
−0.01
2.50
0.58
1
0.01
0.00
2.15
0.70
0
0.14
−0.03
0.46
0.26
1
−0.28
−0.23
1.19
0.66
0
0.14
0.07
2.61
0.52
1
0.15
0.05
1.88
0.27
0
0.15
0.06
2.23
0.56
1
0.37
0.11
1.99
0.38
0
0.16
0.05
2.31
0.20
1
−0.08
−0.08
1.51
0.42
0
0.29
0.06
1.84
0.38
1
0.05
0.03
1.68
0.95
0
0.54
0.11
2.33
0.48
1
0.01
−0.00
1.26
0.60
0
−0.33
−0.09
3.01
0.47
1
0.12
0.11
1.14
0.17
0
0.48
0.09
1.24
0.18
1
−0.28
−0.27
1.27
0.51
0
0.56
0.11
4.29
0.45
0
0.20
0.08
1.99
0.30
0
0.47
0.14
2.92
0.45
0
0.17
0.04
2.45
0.14
0
0.58
0.04
5.06
0.13
EXHIBIT 5.5
Logistic regression illustration: data
Then, using (5.38), these two quantities are, respectively, the mean and
the covariance matrix of the normal approximation to β’s posterior. The
marginal posterior distributions of each of the regression coefficients, βj, j =
0, . . . , 4, are straightforward to obtain. For example, the posterior density of
β0 is approximately normal with mean ˆβ0 = 5.31 and variance σ 2
0
∗= 5.60,
while that of β2 has a mean ˆβ2 = 3.50 and variance σ 2
2
∗= 185.18.
Using Exhibit 5.6, one can evaluate visually the quality of the normal
approximation for β0 and β2. The histograms are constructed using draws
obtained with the importance sampling algorithm. Because of the nature of
the importance sampling algorithm, they practically represent histograms of
draws from the exact distributions of β0 and β2. One can observe that the
normal approximations to the posteriors of the two regression coefficients
are not very good, possibly due to the small sample size in this illustration.
Suppose now that we would like to compute the posterior mean of the
probability of default of company k. Let the four financial ratios considered

88
BAYESIAN METHODS IN FINANCE
−5
0
5
10
15
0.0
0.05
0.10
0.15
b0
−60
−40
−20
0
20
40
60
0.0
0.010
0.020
0.030
b2
EXHIBIT 5.6
Approximations to the posterior densities of β0 and β2
Note: The solid curves represent density curves of the normal approximations to the
posteriors of β0 and β2. The dotted curves represent the Laplace approximations
to the posteriors. The histograms are constructed from draws obtained with the
importance sampling algorithm.
above have the following values for company k: xk,1 = 0.05, xk,2 = 0.05, xk,3
= 1.80, and xk,4 = 0.50. The probability of default, θ k, is then (by (5.32))
θk =
exp

β0 + 0.05β1 + 0.05β2 + 1.8β3 + 0.5β4

1 + exp

β0 + 0.05β1 + 0.05β2 + 1.8β3 + 0.5β4
.
(5.40)
One could compute the posterior distribution of θ k by substituting the
draws of β from the normal approximation into the expression above. The
posterior mean of θ k is thus found to be 0.42.

Bayesian Numerical Computation
89
Generally, when only a small data sample is available, a more adequate
approximation to the posterior distribution is provided by the Laplace
approximation, which we discuss next.
The Laplace Approximation
Consider again the generic parameter vector η with a posterior distribution
p(η | y). Suppose that one would like to approximate directly the marginal
posterior density of a component of η, η1, where the parameter vector is
partitioned as η = (η1, η2) and η2 = (η2, · · ·, ηp). The posterior density of η
is then written as
p(η | y) = p(η1, η2 | y)
and we can apply a second-order Taylor expansion of the log-posterior
around the conditional posterior mode of η2, that is, the value η that
maximizes p(η1, η2 | y) for a fixed η1. Based on the Taylor expansion, we can
write
log

p (η1, η2 | y)

≈log

p (η1, 
η2 | y)

+ d log

p (η1, η2 | y)

d η2

η2= 
η2
(η2 −
η2)
+1
2(η2 −
η2)′H(η2 −
η2),
where, for a fixed η1, the second term on the right-hand side is zero and H
is the Hessian matrix. Then the marginal posterior density of η1 is obtained
by computing the following integral:
p (η1 | y) =

p (η1, η2 | y) dη2
=

exp

log

p (η1, η2 | y)

dη2
≈

exp

log

p (η1, 
η2 | y)

−1
2(η2 −
η2)′(−H)(η2 −
η2)

dη2
= p (η1, 
η2 | y)

exp

−1
2(η2 −
η2)′(−H)(η2 −
η2)

dη2
(5.41)
∝p (η1, 
η2 | y)
−H−1−1/2 ,
(5.42)

90
BAYESIAN METHODS IN FINANCE
where the last line follows from recognizing the integrand in (5.41) as the
kernel of a multivariate normal distribution. The method for computing the
integral above is known as the Laplace method.29
The dotted curves in Exhibit 5.6 represent the density curves of the
approximated marginal posterior distributions of β0 and β2 in the logistic
regression illustration. We can observe that even for the small sample size,
the approximations are very accurate.
In conclusion, we briefly describe how Tierney and Kadane (1986) use
the Laplace method to compute the approximate posterior expectation of a
function g(η),
E (g(η) | y) =

g(η)p(η | y) dη
=

exp

log

g(η)

+ log

L(η | y)

+ log

π(η)

dη

exp

log

L(η | y)

+ log

π(η)

dη
≡

exp

h(η)∗
dη

exp

h(η)

dη ,
(5.43)
where L(η | y) and π(η) are, respectively, the likelihood function and the
prior distribution of η. The numerator and the denominator in (5.43) can
both be approximated using the Laplace method, as in (5.41) to obtain
E (g(η) | y) ≈
R∗1/2 exp

h(η∗)

|R|1/2 exp

h(η)
 ,
(5.44)
where R∗and R are the negative inverse Hessian matrices of h(η)∗and
h(η), respectively, and η∗and η are the maximal values of h(η)∗and h(η),
respectively.30
SUMMARY
The recent surge in popularity of the Bayesian framework among practition-
ers is undoubtedly due to the large strides made in developing computational
29See also Leonard (1982) for a derivation of the approximation to the marginal
posterior distribution of η1 in a related way.
30Leonard, Hsu, and Tsui (1989) and Kass, Tierney, and Kadane (1989) show how
to approximate the marginal posterior density of g(η). See also Hsu (1995) and
Leonard and Hsu (1999).

Bayesian Numerical Computation
91
algorithms and in the advancement of computing power. In this chapter,
we discussed the main methods for posterior simulation, along with those
for approximation.31 In the chapters that follow, we provide additional
details in the context of specific financial applications. We hope that we
conveyed the idea that even though the computational algorithms (especially
the MCMC methods) greatly facilitate estimation of complicated models,
they are not black-box solutions—thoughtful algorithm design, as well as
convergence monitoring, are necessary on part of the researcher.
31See Gilks, Richardson, and Spiegelhalter (1996) for more details on the application
of MCMC methods.

CHAPTER6
Bayesian Framework for
Portfolio Allocation
The Mean-Variance Setting
M
arkowitz’s 1952 paper set the foundations for what is now popularly
referred to as ‘‘modern portfolio theory’’ and had a profound impact
on the financial industry. Individual security selection lay at the heart of the
standard investment practice until then. Afterward, the focus shifted toward
diversification and assessment of the contribution of individual securities to
the risk-return profile of a portfolio. Mean-variance analysis rests on the
assumption that rational investors select among risky assets on the basis of
expected portfolio return and risk (as measured by the portfolio variance).
However, the reputation of this classical framework among practitioners
has suffered due to numerous implementation difficulties. Portfolio weights
derived from it are notoriously sensitive to the inputs,1 especially expected
returns, and often represent unintuitive or extreme allocations exposing an
investor to unintended risks.2 These inputs (expected returns, variances, and
covariances) are all subject to estimation errors that an optimizer picks up
and then leverages. Chopra and Ziemba,3 for example, examine the relative
impact of errors in the three groups of parameter inputs on optimal weights
and find that errors in the means can be up to 10 or 11 times more important
than errors in variances.4
1Best and Grauer (1991).
2Black and Litterman (1992).
3Chopra and Ziemba (1993).
4Merton (1980) points out that variances and covariances of return are more stable
over time than expected returns, and, therefore, estimation errors in them affect
portfolio choice less seriously than estimation errors in the means.
92

Bayesian Framework for Portfolio Allocation
93
Estimation risk must be, then, a component of any comprehensive
approach to the investment management process. The focus is on making the
portfolio selection problem more robust. Several extensions to the classical
mean-variance framework dealing with this issue have been developed.
Among them are extensions targeting estimation of the input parameters,
factor models, robust optimization techniques, and portfolio resampling.
All of them help address the errors intrinsic in parameter estimation.
Factor models describe the behavior of asset returns by means of a
small number (relative to the number of assets in a typical portfolio) of
factors (sources of risk). They are especially useful in the estimation of
the asset covariance matrix by reducing dramatically the dimension of the
estimation problem, introducing structure into the covariance estimator,
and improving it compared to the historical covariance estimator.
The robust approach to portfolio selection introduces the estimation
error directly into the optimization process. Robust optimization focuses
most often on estimation errors in the means than in the covariance matrix
(likely due to the greater relative importance of the errors in the means).
In its simplest form, the idea is to consider portfolio optimization as a
two-stage problem. In the first stage, expected utility is minimized with
respect to expected return (reflecting the ‘‘worst’’ estimate case that could
be realized). In the second stage, the minimum expected utility is maximized
with respect to the portfolio weights, for a given risk-aversion parameter.
Extensions of the robust framework to modeling of the estimation error
in other parameter inputs beyond expected returns and to accounting for
model risk exist.5
Portfolio resampling has emerged as a heuristic approach to partially
capture estimation error.6 It relies on a Monte Carlo simulation to obtain
a large number of samples from the distribution of historical returns,
treating the sample parameters as the true parameters. An efficient frontier
is computed for each of the samples and the average (resampled) frontier is
obtained. The portfolios on the resampled frontier are more diversified than
the portfolios on the traditional mean-variance frontier, thus addressing a
major weakness of mean-variance analysis. However, the estimation error
in the parameter estimates (of the mean and covariance, if normality is
assumed) is carried on to the resampled frontier.
The Bayesian approach addresses estimation risk from a conceptually
different perspective. Instead of treating the unknown true parameters as
fixed, it considers them random. The investor’s belief (prior knowledge)
5See Ben-Tal and Nemirovksi (1998, 1999), El Ghaoui and Lebret (1997), and
Goldfarb and Iyengar (2003), among others.
6See Jorion (1992), Michaud (1998), and Scherer (2002).

94
BAYESIAN METHODS IN FINANCE
about the parameter inputs, combined with the observed data, yield an
entire distribution of predicted returns which explicitly takes into account
the estimation and predictive uncertainty.
In this chapter, we begin with an overview of the classical portfolio
selection problem. Then, we examine the Bayesian approach to dealing
with estimation risk in portfolio optimization, briefly discussing shrinkage
estimators. Finally, we turn out attention to the case when assets with return
histories of unequal length compose the investment universe.
The next chapter focuses on a further refinement of the Bayesian
asset allocation approach, namely incorporating asset pricing models into
the investment decision-making framework, while Chapter 8 presents a
well-known example—the Black-Litterman model.
Chapter 13 extends the mean-variance optimization framework and dis-
cusses asset allocation assuming nonnormality of returns—higher moments,
as well as expected tail loss optimization, are considered.
CLASSICAL PORTFOLIO SELECTION
Mean-variance analysis presumes that return and risk (as measured by the
portfolio variance) are all investors consider when making portfolio-selection
decisions. Therefore, a rational investor would prefer a portfolio with a
higher expected return for a given level of risk. An equivalent way to
express the mean-variance principle is: a preferred portfolio is one that
minimizes risk for a given expected return level. The portfolios that are
optimal in these two equivalent senses make up the efficient frontier. No
rational investor would invest in a portfolio lying below the efficient frontier
since that would mean accepting a lower return for the same amount of risk
as an efficient portfolio (equivalently, undertaking greater risk for the same
expected return). How do we obtain the efficient frontier? It has been shown
that three formulations of the investor’s mean-variance problem provide the
same optimal portfolio solution, under some conditions generally satisfied
in practice.7
More formally, it is usually accepted that mean-variance analysis is
grounded in either of two conditions: asset returns have a multivariate
normal distribution or investor preferences are described by quadratic
utilities.8 (We discussed the multivariate normal distribution in Chapter 3.)
7See Rockafellar and Uryasev (2002) for the proof of equivalence of the three
portfolio problem formulations.
8In fact, Markowitz and Usmen (1996) point out that neither of the two conditions
is indispensable. Almost optimal asset allocations can be obtained using a variety

Bayesian Framework for Portfolio Allocation
95
We start with some portfolio selection preliminaries. Suppose that there
are N assets in which an investor may invest. Denote by Rt the excess returns
on the N assets at time t,
Rt = (R1, t, . . . , RN,t)′,
and assume that they have a multivariate normal distribution,
p (Rt | µ, ) = N (µ, ) ,
with mean and covariance matrix given by the N × 1 vector µ and the
N × N matrix , respectively. The portfolio weights are the proportions of
wealth invested in each of the N assets and are given by the N × 1 vector
ω = (ω1, . . . , ωN)′. A portfolio’s return at time t is then given by
Rp =
N

i=1
ωiRi,t = ω′Rt.
Its expected return and variance are defined, respectively, as
µp =
N

i=1
ωiµi = ω′µ,
where µi is the expected return on asset i and
σ 2
p =
N

i=1
N

j=1
ωiωjcov(Ri, Rj) = ω′ω.
where cov(Ri, Rj) is the covariance between the returns on assets i and j.
Portfolio Selection Problem Formulations
Suppose that the investor has a portfolio holding period of length τ. We
assume that the investor’s objective is to maximize his wealth at the end
of his investment horizon, T + τ, where T is the time of portfolio com-
position (equivalently, the last period for which return data are available).
of utility functions. The quadratic utility function approximates well several more
general utility functions, as explained in Chapter 2 in Fabozzi, Focardi, and Kolm
(2006). The multivariate normal distribution assumption can also be relaxed.
Rachev, Ortobelli, and Schwartz (2004) show that the so-called location-scale
family of distributions results in optimal solutions as well.

96
BAYESIAN METHODS IN FINANCE
The mean-variance principle can be expressed through the following dual
portfolio problems:
min
ω
σ 2
p = min
ω
ω′ T+τ ω
subject to
ω′µT+τ ≥µ∗
ω′1 = 1,
(6.1)
where 1 is a vector of ones compatible with ω, that is, of dimension N × 1,
and µ* is the portfolio’s minimum acceptable return, and
max
ω
µp = max
ω
ω′ µT+τ
subject to
ω′T+τω ≤σ 2 ∗
ω′1 = 1,
(6.2)
where σ* is the portfolio’s maximum acceptable risk. We have added the
subscripts T + τ in the notation for the expected returns and covariance
to stress that these refer to attributes of yet unobserved asset returns. For
an investor who pursues an indexing strategy (i.e., a strategy to replicate
or track the performance of a designated benchmark), µ* in (6.1) is the
benchmark’s return.
In its third formulation, the portfolio optimization problem is expressed
as the maximization of the investor’s expected utility of end-period portfolio
value,
max
ω
E

U

ω′RT+τ

= max
ω

U

ω′RT+τ

pT+τ (RT+τ | µ, ) dRT+τ
subject to
ω′1 = 1.
(6.3)
Notice that the expected utility is expressed with respect to the distribu-
tion of future returns, pT+τ. We can think of this as computing the weighted
sum of the utilities of portfolio returns, with the probabilities of future asset
returns serving as weights.
It can be shown that the expected quadratic utility function of investor’s
wealth at time T + τ has the form
E

U

ω′RT+τ

= µp −A
2 σ 2
p ,
(6.4)
where A is the relative risk aversion parameter, a measure for the rate at
which the investor is willing to accept additional risk for a one unit increase
in expected return.

Bayesian Framework for Portfolio Allocation
97
The composition of the investor’s optimal portfolio (vector of optimal
weights) is given by
ω∗=
−1
T+τ µT+τ
1′ −1
T+τ µT+τ
.
(6.5)
More constraints are usually added to the three optimization problems
just given. For example, many institutional investors are not permitted to
take short positions. In such cases, the portfolio weights are constrained to
be positive, ωi > 0, i = 1, . . . , N.9
Mean-Variance Efficient Frontier
By varying the values of A in (6.4), µ* in (6.1) or σ 2* in (6.2), we
obtain a sequence of optimal portfolios. Their corresponding risk-return
combinations, (σ 2
p , µp), are represented geometrically by the mean-variance
frontier. The upward-sloping portion of it is called the efficient frontier—the
geometric locus of the efficient portfolios, providing the highest return for a
given level of risk (lowest risk for a given level of return).
How do the portfolios on the efficient frontier compare with each other
and which one is the investor’s optimal portfolio? A measure of portfolio
performance, called the Sharpe ratio, can be used to help answer these
questions. The Sharpe ratio of a portfolio is its expected return per unit of
standard deviation (risk),10
SRP = µp
σp
=
ω′µ
√
ω′ω
.
(6.6)
It can be shown that the portfolio with the highest Sharpe ratio (among
the efficient portfolios) and, therefore, the most desirable to an investor,
is the portfolio corresponding to the risk-return combination such that the
efficient frontier and a line passing through the origin are tangent to each
other.11 Thus we can see that the selection of the optimal portfolios can be
viewed as a two-step process: first the efficient frontier is constructed and
then the optimal portfolio located. See Exhibit 6.1.
We emphasized earlier that, since we assume the investor’s objective
is maximization of the terminal portfolio value, the parameter inputs of
the portfolio problem pertain to the period of the investment horizon.
9See Chapter 4 in Fabozzi, Focardi, and Kolm (2006) for the portfolio constraints
commonly used in practice.
10See Sharpe (1994).
11The portfolio problem is sometimes also expressed as maximization of the Sharpe
ratio in (6.6).

98
BAYESIAN METHODS IN FINANCE
0
Portfolio Risk
Portfolio Expected Return
Global minimum
variance portfolio
Tangent
portfolio
Efficient
frontier
EXHIBIT 6.1
The efficient frontier
The classical mean-variance approach relies on the following two points.
First, the unknown parameters are estimated from the sample of available
data and the sample estimates are then treated as the true parameters.
Second, it is implicitly assumed that the distribution of returns at the time
of portfolio construction remains unchanged until the end of the portfolio
holding period. Usually, the sample estimates of µ and  are computed as
µ = 1
T
T

t=1
Rt,
(6.7)
and
 =
1
T −1
T

t=1

Rt −µ
Rt −µ
′.
(6.8)
These two estimates are unbiased. From statistical theory we know that
the maximum likelihood estimate of the mean coincides with µ, while the
maximum likelihood of the covariance is not unbiased,
mle = 1
T
T

t=1

Rt −µ
Rt −µ
′ = T −1
T
.
(6.9)

Bayesian Framework for Portfolio Allocation
99
We reexpress the vector of optimal portfolio positions in (6.5) as
ω∗
ce =
−1 µ
1′ −1 µ
.
(6.10)
The optimal solution, ω∗
ce, is known as the certainty-equivalence solution
since it treats the estimated parameters as if they were the true ones. Such an
approach fails to recognize the fact that µ and  may contain nonnegligible
amounts of estimation error. The resulting portfolio is quite often badly
behaved, leveraging on assets with high estimated mean returns and low
estimated risks, which are the ones most likely to contain high estimation
errors. To deal with this, practitioners usually impose tight constraints on
asset positions. However, this could lead to an optimal portfolio determined
by the constraints instead of the optimization procedure. Moreover, the
assumption that the return distribution remains the same till the investment
horizon, T + τ, can only be justified if the holding period, τ, is very short.
Illustration: Mean-Variance Optimal Portfolio with
Portfolio Constraints
As an illustration, we consider the daily excess returns on ten MSCI Euro-
pean country indexes—Denmark, Germany, Italy, the United Kingdom,
Portugal, the Netherlands, France, Sweden, Norway, and Ireland—for the
period January 2, 1998, through May 5, 2004, a total 1,671 observations
per country index. Their summary statistics (mean returns, standard devi-
ations, and correlations) are presented in Exhibit 6.2. In Exhibit 6.3, we
give the weights of the efficient portfolios in the cases when short sales are
allowed and when short sales are restricted. Notice the large long and short
positions when no short sales are allowed—some of these tilts do not seem
to bear direct correspondence to the returns summary statistics. When we
restrict short sales, we obtain a significant number of zero weights. For the
sole purpose of this illustration, we also provide optimal portfolio weights
when long and short positions are restricted to be no larger than 30%. It is,
of course, not a realistic restriction in practice. As in the case when no short
sales are allowed, the constraint results in a number of corner positions.
Explicit consideration of estimation risk is provided within the Bayesian
approach to portfolio selection, which uses the predictive distribution of
returns as an input to the portfolio problem. Furthermore, as we will
see in the next two chapters, combining information about the model
parameters from different sources helps to alleviate the problems with the
classical portfolio selection illustrated above. We turn next to discussing the
foundations of Bayesian portfolio selection.

100
BAYESIAN METHODS IN FINANCE
Mean
Return
St.
Dev.
Correlations
Denmark
20.7
0.51
0.51 0.47
0.48
0.54
0.55
0.51
0.51
0.46
Germany
27.2
0.74 0.69
0.52
0.77
0.81
0.65
0.48
0.45
Italy
23.0
0.68
0.57
0.76
0.81
0.62
0.50
0.47
UK
19.6
0.45
0.77
0.77
0.61
0.48
0.50
Portugal
20.0
0.51
0.56
0.48
0.43
0.43
Netherlands
24.3
0.85
0.65
0.55
0.50
France
23.6
0.71
0.53
0.49
Sweden
31.2
0.51
0.43
Norway
22.6
0.46
Ireland
2.3
−0.6
2.4
−2.3
−3.1
−3.3
4.0
5.2
−0.1
−1.7
21.2
1
1
1
1
1
1
1
1
1
1
EXHIBIT 6.2
Summary statistics of the monthly returns on the 10 MSCI country
indexes
Note: The summary statistics of the 10 MSCI country indexes are computed using
daily returns in excess of one-month LIBOR. The mean returns and standard
deviations are annualized percentages.
Target
Return
1.08%
1.59% 1.08%
3.16%
3.05% 3.16%
5.24%
5.24% 5.24%
Each
Weight
Within
± 
30%
Each
Weight
Within
± 
30%
Short
Sales
Allowed
No
Short
Sales
Short
Sales
Allowed
No
Short
Sales
Short
Sales
Allowed
No
Short
Sales
Each
Weight
Within
± 
30%
Denmark
35.0
30
39.8
30
Germany
0
−18.8
−24.3
−23.0
−24.2
Italy
20.8
30
26.0
30
UK
0
31.0
17.5
25.0
−0.1
Portugal
12.1
6.4
5.0
0
−8.5
Netherlands
−50.5
−30
−65.9
−30
France
42.5
30
62.2
30
Sweden
0
−4.2
6.4
−1.3
100
30
Norway
16.2
47.9
7.9
36.9
5.5
1.8
17.6
16.8
24.7
Ireland
30.2
−14.7
15.5
37.0
19.3
−35.1
22.8
−7.1
15.6
16.6
39.8
12.5
4.1
0
18.7
11.2
13.8
30
−15.2
15.7
30
19.7
−30
23.2
−6.8
15.8
17.6
16.0
0
0
0
0
0
16.5
15.4
0
0
0
0
0
0
0
0
18.0
EXHIBIT 6.3
Optimal portfolio weights under three different constraints
Note: Portfolio weights are in percentages. Weights might not sum up to 1 due to
rounding errors.

Bayesian Framework for Portfolio Allocation
101
BAYESIAN PORTFOLIO SELECTION
The effect of parameter uncertainty on optimal portfolio choice is nat-
urally accounted for by expressing the investor’s problem in terms of
the predictive distribution of the future excess returns. Recall, from
the discussion in Chapter 3, that the predictive distribution essentially
weighs the distribution of returns with the joint posterior density of the
parameters.
Denoting the (yet unobserved) next-period excess return data by RT+1,
we write the predictive return density as
p

RT+1 | R

∝

p

RT+1 | µ, 

p

µ,  | R

dµ d,
(6.11)
where: R = return data available up to period T—a T × N
matrix.
p (µ,  | R) = joint posterior density of the two parameters of the
multivariate normal distribution.
p (RT+1 | µ, ) = multivariate normal density.
∝= proportional to.
Notice that we account for estimation risk by averaging over the
posterior distribution of the parameters. Therefore, the distribution of RT+1
does not depend on the parameters, but only on the past return data, R.
When returns are assumed to have a multivariate normal distribution,
as in this chapter, the predictive density can be shown to be a known
distribution (given that standard prior distributional assumptions are made
as discussed further below). Once we depart from the normality assumption
the predictive density may not have a closed form. In both cases, however,
it is possible to evaluate the integral on the right-hand side of (6.11) as
explained in Chapter 4. Applications in which no analytical expressions
exist for the likelihood and some of the prior distributions are discussed in
Chapters 13 and 14.
Substituting in the predictive density of excess returns, the portfolio
problem in (6.3) becomes
max
ω
E

U

ω′RT+1

= max
ω

U

ω′RT+1

p

RT+1|R

dRT+1
subject to
ω′1 = 1.
(6.12)

102
BAYESIAN METHODS IN FINANCE
Let us denote the mean and covariance of next-period returns, RT+1, by
µ and , respectively. Then the problem in (6.1) is expressed as12
min
ω
σ 2
p = min
ω
ω′  ω
subject to
ω′ µ ≥µ∗
ω′1 = 1,
(6.13)
and the one in (6.2) is rewritten analogously. The expression for the optimal
portfolio weights in (6.5) becomes then
ω∗=
−1 µ
1′ −1 µ
.
(6.14)
In what follows, we outline two basic portfolio selection scenarios
depending on the amount of prior information the investor is assumed
to have about the parameters of the return distribution and we examine
their effects on optimal portfolio choice. We extend the prior distribution
framework in the next two chapters by including asset pricing models in it.
The likelihood function for the mean vector, µ, and covariance
matrix, , of a multivariate normal distribution, as shown in Chapter
3, is given by
L

µ,  | R

∝||−T/2exp
	
−1
2
T

t=1

Rt −µ
′−1
Rt −µ


,
(6.15)
where || is the determinant of the covariance matrix.
Prior Scenario 1: Mean and Covariance with Diffuse
(Improper) Priors
We consider the case when the investor is uncertain about the distribution
of both parameters, µ and , and has no particular prior knowledge of
them. This uncertainty can be represented by a flat (diffuse) prior, which is
12Notice a key difference between the Bayesian approach to portfolio selection
and the resampled frontier approach of Michaud (1998). In the Bayesian setting,
uncertainty is taken into account before solving the investor’s optimization problem
in (6.13)—µ and  already reflect the estimation error. In contrast, Michaud’s
approach involves solving a number of optimization problems, based on sample esti-
mates, and then, by averaging out the optimal allocations, incorporating parameter
uncertainty.

Bayesian Framework for Portfolio Allocation
103
typically taken to be the Jeffreys’ prior, discussed in Chapter 3,
p (µ, ) ∝||−(N+1)/2.
(6.16)
Note that µ and  are independent in the prior, and µ is not restricted as
to the values it can take. The prior is uninformative in the sense that small
changes in the data exert a large influence on the posterior distribution of
the parameters.
It can be shown that the predictive distribution of the excess returns is a
multivariate Student’s t-distribution with T −N degrees of freedom.13 The
predictive mean and covariance matrix of returns are, respectively,14
µ = µ
and
 =

1 + 1
T

T −1

T −N −2
,
where  is given in (6.8). The predictive covariance here represents the
sample covariance scaled up by a factor, reflecting estimation risk. For
a given number of assets N, parameter uncertainty decreases as more
return data become available (T grows). When a fixed number of historical
observations are considered (T is fixed), increasing the number of assets
leads to higher uncertainty and estimation risk, since the relative amount of
available data declines. (Statisticians would say that there are less degrees
of freedom to estimate the unknown parameters.
Prior Scenario 2: Mean and Covariance with Proper
Priors
Suppose now that the investor has informative beliefs about the mean
vector and the covariance matrix of excess returns. We consider the case of
conjugate priors.
13We assume that T −N ≥2 to ensure that the predictive distribution of returns
has a finite variance.
14Since the predictive distribution in scenario 1 is not normal, the assumption of a
concave utility function is needed for mean-variance optimization. In general, the
predictive distribution is normal when the covariance is assumed known and the
mean has a conjugate (normal) prior. When neither the mean nor the variance are
known and either a diffuse prior is assumed, as in scenario 1, or conjugate priors for
both are assumed, as in scenario 2 below, the predictive density is Student’s t.

104
BAYESIAN METHODS IN FINANCE
The conjugate prior for the unknown covariance matrix of the normal
distribution is the inverted Wishart distribution (see (3.66)), while the
conjugate prior for the mean vector of the normal distribution (conditional
on ) is multivariate normal:
µ |  ∼N

η, 1
τ 

 ∼IW

, ν

,
(6.17)
The prior parameter τ determines the strength of the confidence the investor
places on the value of η, while ν reflects the confidence about . The
lower τ and ν are, the higher the uncertainty about those values. When
τ = 0, the variance of µ is infinite and its prior distribution becomes
completely flat—the investor has no knowledge or intuition about the
mean and lets it vary uniformly from −∞to +∞. (This is another way to
inject ‘‘uninformativeness’’ in the prior distribution—just make the prior
covariance (determinant) very large.)
It is important to notice that µ and  are no longer independent in the
conjugate prior in (6.17), unlike scenario 1. This prior dependence might
not be unreasonable if the investor believes that higher risk could entail
greater expected returns.
The predictive distribution of next-period’s excess returns can be shown
to be multivariate Student’s t. The mean of the predicted excess returns and
their covariance matrix can be shown to be, respectively,
µ =
τ
T + τ η +
T
T + τ µ
(6.18)
and
 =
T + 1
T (ν + N −1)

 + (T −1)  +
Tτ
T + τ (η −µ) (η −µ)′

.
(6.19)
In contrast with scenario 1, the predictive mean and predictive covariance
matrix are not proportional to the sample estimates µ and . This is
characteristic of the impact ‘‘informativeness’’ of the prior distributions has
on Bayesian inference. We will see below how this difference from scenario 1
is reflected in the efficient frontier and the optimal portfolio choice. First,
let us briefly examine more closely the expressions in (6.18) and (6.19).
The predictive mean in (6.18) is a weighted average of the prior mean,
η, and the sample mean, µ—the sample mean is shrunk toward the prior
mean. The stronger the investor’s belief in the prior mean is (the higher
τ/(T + τ)
is), the larger the degree to which the prior mean influences
the predictive mean (the degree of shrinkage). In the extreme case, when

Bayesian Framework for Portfolio Allocation
105
the investor has 100% confidence in the prior mean, the predictive mean
is equal to the prior mean, µ = η, and the observed data in fact become
irrelevant to the determination of the predictive mean. Conversely, when an
investor is completely sceptical about the prior, only the data determine the
predictive mean and µ = µ—there is no correction for estimation risk in
the mean estimate in this case, as we are back to the certainty-equivalence
scenario of the classical mean-variance approach.
Notice that in scenario 1 the predictive expected return is not shrunk
towards the prior mean. Therefore, the full amount of any sampling error
in the sample mean is transferred to the predictive mean (the same is true
for the posterior mean). This scenario is, thus, appropriate to employ when
we do not suspect that the sample mean contains (substantial) estimation
errors. Otherwise, the informative proper prior of scenario 2 might be the
better prior alternative.
We learn more about the interplay between the strength of prior beliefs
and Bayesian inference in the next two chapters, where asset pricing models
enter into the picture to make the analysis more refined.
Next, we discuss how the efficient frontier and the optimal portfolio
choice change under the certainty-equivalence scenario and the two prior
scenarios outlined above.
The Efficient Frontier and the Optimal Portfolio
The vector of optimal portfolio positions, ω∗, is a function of the predictive
mean, µ, and the predictive covariance, , of future returns and is given
by (6.14). The efficient frontier is traced out by the optimal pairs

µ∗
p, σ 2
p
∗
,
where
µ∗
p = ω∗′ µ
and
σ 2
p
∗= ω∗′  ω∗,
for varying values of the risk-aversion parameter, A, in (6.4), the required
portfolio return, µ*, in (6.1) or the minimum portfolio variance, σ 2*,
in (6.2).
First, consider the certainty-equivalence scenario together with sce-
nario 1. In the classical mean-variance setting, the sample estimates, µ and
, are treated as the true values of the unknown mean and covariance.
In scenario 1, the moments of the predictive distributions are proportional
to the sample estimates (equivalently, the maximum-likelihood estimates);
the portfolio mean µp is unchanged, while the portfolio variance σ 2
p is just
scaled up with a constant. Consequently, the efficient frontier in scenario 1
is shifted to the right compared with the certainty-equivalence case.

106
BAYESIAN METHODS IN FINANCE
Incorporating parameter uncertainty into the investor problem leads to
a different perception of the risk and the risk-return trade-off. For each level
of expected portfolio return, the risk of holding the efficient portfolio is
higher than when parameter uncertainty is ignored. The investor faces not
only the risk originating from return variability but also the risk intrinsic in
the estimation process.
When informative prior beliefs are introduced into the portfolio prob-
lem, such as in scenario 2, no clear comparison can be made between the
composition of the efficient portfolios in the Bayesian setting and in the
classical (certainty-equivalence) setting—the predictive mean and variance
in (6.18) and (6.19), respectively, are no longer proportionate to the sample
moments. See the illustration that follows.
Illustration: Bayesian Portfolio Selection
We continue with our illustration based on the daily excess returns of the
ten MSCI country indexes. To elicit the hyperparameters in the Bayesian
scenario with proper priors, we obtain a presample of daily excess returns,
nonoverlapping with the data we use for portfolio optimization. The pre-
sample data consist of 520 observations. Denote these data by R−S, where
S is the length of the presample period. We choose the hyperparameters in
(6.17) as follows:
■η is equal to the a vector of zeros. The reason for not specifying η as
the sample mean of R−S instead is that we are sceptical that the mean
level of returns from the economic-upturn period of the mid-1990s is
representative of the mean-return level in our sample.
■τ is equal to 200. τ often takes on the interpretation of the size of a
hypothetical sample drawn from the prior distribution: the larger the
sample size, the greater our confidence in the prior parameter, η. We
have around 6.5 years of (calibration) data available. A τ of 200 could
be interpreted as weighting the prior on the mean of returns with about
one eighth of the weight of the sample data.
■ is equal to −S(ν −N −1), where the subscript of  refers to its
being estimated from the presample data, R−S.15
■ν is equal to 12. We choose a low value for the degrees of freedom
to make the prior for  uninformative and reflect our uncertainty
about .16
15 is distributed as IW(, ν). The prior mean of  is E() = /(ν −N −1). We
estimate E() with its sample counterpart, , given in (6.8).
16The mean of the inverse Wishart random variable exists if ν > N + 1.

Bayesian Framework for Portfolio Allocation
107
0.0094
0.0098
0.0102
−5
0
5
10
15
20
x 10−5
Portfolio Standard Deviation
Portfolio Expected Return
 
 
B2
CE
B1
EXHIBIT 6.4
Comparison of the efficient frontiers in the certainty-equivalence
setting and the two Bayesian scenarios
Note: CE = certainty-equivalence setting; B1 = Bayesian scenario with diffuse
(improper) priors; and B2 = Bayesian scenario with proper priors. The portfolio
expected returns and standard deviations are on a daily basis.
In Exhibit 6.4, we present plots of the efficient frontiers in the
certainty-equivalence scenario and the two Bayesian scenarios. Given our
earlier discussion, the plots appear as expected: The greater risk per-
ceived by the investor in the Bayesian setting is reflected by a shift of
the frontier to the right in the two Bayesian scenarios compared to the
certainty-equivalence case. The frontier in the Bayesian scenario 1 is very
close to the one in the certainty-equivalence setting because of the large
number of data points (1,671) available for portfolio optimization. Increas-
ing the amount of sample information even more will eventually make the
two frontiers coincide. The rate at which the frontier of scenario 2 moves
closer to the certainty-equivalence frontier depends on the strength of the
prior beliefs—the values of τ and ν. The degrees-of-freedom parameter, ν,
does not affect the risk-return trade-off, since only the predictive covariance
depends on it. Changes in it, however, will shift the efficient frontier in
a parallel fashion, as uncertainty about
the covariance matrix changes.

108
BAYESIAN METHODS IN FINANCE
The parameter τ does affect the relationship between the predictive mean
and the predictive covariance matrix in a nonlinear way, as can be seen
from the expressions in (6.18) and (6.19), with the consequence that the
effect on the efficient frontier is not clear a priori.
More illuminating about the difference between the classical and
Bayesian approaches is an illustration on the sensitivity of optimal allo-
cations to changes in the portfolio problem inputs. Suppose that the sample
mean of MSCI Germany is 10% higher than the value in Exhibit 6.1. We
perform portfolio optimization with all remaining inputs as before. The
efficient frontier is constructed from the expected return-standard devia-
tion pairs corresponding to eight portfolios, for varying rates of required
portfolio return. Exhibit 6.5 presents the result from our sensitivity check.
We can observe that the optimal weights under the certainty-equivalence
scenario are much more sensitive to the change in a single component of
µ than are the optimal weights derived under the Bayesian scenario—22
of the certainty-equivalence optimal weights changed by more than 30%,
compared to 0 of the Bayesian optimal weights. The reason for the diver-
gent sensitivities is the different treatment of the sample estimates in the
certainty-equivalence setting and in the Bayesian setting. In the former case,
the sample estimates are considered to be the true parameter values; in the
latter case, the sample estimates are considered for what they are—sample
estimates—and the uncertainty about the true parameter values is embodied
in the portfolio problem. The predictive mean, µ, and covariance, , reflect
the uncertainty and this serves as a cushion to soften the impact of the
change in the sample mean of MSCI Germany’s daily returns.
SHRINKAGE ESTIMATORS
A shrinkage estimator is a weighted average of the sample estimator and
another estimator. Stein (1956) showed that shrinkage estimators for
the mean, although not unbiased, possess more desirable qualities than
the sample mean. The so-called James-Stein estimator of the mean has the
general form:
µJS = (1 −κ) µ + κ1′µ0,
(6.20)
where the weight κ, called the shrinkage intensity, is given by
κ = min

1,
N −2
T (µ −1′µ0)′  (µ −1′µ0)

,
and 1 is a N × 1 vector of ones. It is interesting to notice that any point µ0
can serve as the shrinkage target. The resulting shrinkage estimator is still

Bayesian Framework for Portfolio Allocation
109
Bayesian Scenario 2
Target
Return
Target
Return
−1.8%
−0.9%
0.04%
1.0%
1.9%
2.8%
3.8%
4.7%
Denmark
0.00
−0.01
−0.03
−0.05
−0.07
−0.08
−0.10
−0.11
Germany
0.00
0.43
0.73
0.94
1.10
1.22
1.32
1.40
Italy
−0.00
0.04
0.04
0.04
0.04
0.04
0.04
0.04
UK
0.00
0.02
0.05
0.09
0.13
0.18
0.25
0.33
Portugal
0.00
0.03
0.09
0.17
0.29
0.48
0.83
1.68
Netherlands
−0.00
−0.12
−0.22
−0.28
−0.31
−0.34
−0.35
−0.37
France
0.00
0.18
−0.01
−0.04
−0.05
−0.06
−0.06
−0.06
Sweden
−0.00
−0.02
−0.02
−0.02
−0.02
−0.02
−0.02
−0.03
Norway
0.00
−0.01
−0.02
−0.03
−0.04
−0.05
−0.06
−0.07
Ireland
−0.00
−0.00
−0.01
−0.01
−0.01
−0.01
−0.02
−0.02
Certainty-Equivalence Scenario
−2.0% −1.0%
0.04%
1.1%
2.1%
3.2%
4.2%
5.2%
Denmark
−4.18
0.22
0.13
0.51
7.90
14.27
19.82
24.69
Germany
7.48
11.54
7.86
−2.84
−26.72
−27.47
−16.70
−2.19
Italy
−19.14
−3.11
−1.88
−1.48
−22.34
−44.56
−28.30
−15.33
UK
34.64
30.36
25.09
18.96
24.63
44.33
68.62
102.16
Portugal
−0.99
−7.44
−6.54
−1.94
17.39
48.57
107.47
272.63
Netherlands
34.26
31.64
17.29
14.50
29.90
40.59
48.46
54.48
France
64.79
−10.06
−1.88
−1.96
8.04
29.36
42.66
51.74
Sweden
3.14
−1.47
−1.32
4.01
65.72
254.3
786.81 2480.0
Norway
−6.89
−4.79
−3.61
−1.20
−0.95
−8.62
−24.15
−46.73
Ireland
−16.61
−14.68
−11.47
−5.93
−0.60
−3.32
−9.31
−16.84
EXHIBIT 6.5
Optimal weights sensitivity to changes in the sample means
Note: The table entries are the percentage changes in the optimal portfolio weights
resulting from a 10% increase in the sample mean of the daily MSCI Germany
return.
better than the sample mean. However, the closer µ0 is to the true mean µ,
the greater the gains are from using µJS in place of µ. Therefore, µ0 is often
chosen to be the prediction of a model for the unknown parameter µ—we
say, in this case, that µ0 has structure.
For example, in the context of portfolio selection, Jorion (1986) pro-
posed as a shrinkage target the return on the global-minimum-variance

110
BAYESIAN METHODS IN FINANCE
portfolio—the efficient portfolio with smallest risk (see Exhibit 6.1)—
given by17
µ0 = 1′−1
1′−11 µ.
(6.21)
The optimal portfolio is then shrunk toward this minimum-variance
portfolio. Jorion showed that the shrinkage estimator he proposed could
also be derived within a Bayesian setting. Several studies document that
employing a shrinkage estimator in mean-variance portfolio selection leads
to increased stability of optimal portfolio weights across time periods and,
possibly, improved portfolio performance.18
Recall that in scenario 2, the predictive mean of returns is in fact
a shrinkage estimator. The shrinkage target there was the prior mean η,
which, in the general case, does not need to have a particular structure. In
the two chapters that follow, we will see how to introduce structure into
the prior distribution.
Shrinkage estimators for the covariance matrix have also been devel-
oped. For example, Ledoit and Wolf (2003) propose that the covariance
matrix from the single-factor model of Sharpe (1963) (where the single
factor is the market) be used as a shrinkage target:
LW =

1 −κ

S + κ,
(6.22)
where S is the sample covariance matrix and  is the covariance matrix
estimated from the single-factor model. The shrinkage intensity κ can be
shown to be inversely proportional to number of return observations. The
constant of proportionality is dependent on the correlation between the
estimation error in S and the misspecification error in .
UNEQUAL HISTORIES OF RETURNS
Consider the tasks of constructing a portfolio of emerging market equities,
a portfolio of non-U.S. bonds, or a portfolio of hedge funds. Although of
completely different nature, these three endeavors have one common aspect:
All are likely to run into the problem of dealing with return series of different
lengths. An easy fix is to base one’s analysis only on the overlapping parts
of the series and to discard portions of the longer series. However, unless a
17Shrinkage estimators were introduced to the portfolio selection by Jobson, Korkie,
and Ratti (1979). See also Jobson and Korkie (1980) and Frost and Savarino (1986),
among others.
18See, for example, Jorion (1991), and Larsen and Resnick (2001).

Bayesian Framework for Portfolio Allocation
111
researcher is concerned that the return-generating process (or the distribu-
tion of returns) has changed during the longer sample period, this truncation
procedure is not desirable since the longer series may carry information use-
ful for estimation. It could be expected that using all of the available
data will help reduce uncertainty about the true parameters (which exists
by default in dealing with finite samples) and improve estimation results.
Stambaugh’s framework (Stambaugh (1997)) offers a way to do this.19
Suppose that there are a total of N assets available for investment:
1. For N1 of them, the return history spans T periods (from period 1 to
period T). Denote the return data by R1 (a N1 × T matrix).
2. The remaining N2 assets have returns recorded for S periods (from
period s to period T). Denote the return data by R2 (a N2 × S matrix).
3. Denote by RS the N1 + N2 × S matrix of overlapping data. That is,
RS =
 R1, S
R2

,
where R1, S is the matrix of returns of the N1 assets from the most recent
S periods.
Although, for simplicity, we discuss the case of only two starting dates, it
is possible to consider multiple starting dates as well, and even to model
the starting date as a random variable (see Stambaugh (1997) for these
extensions). In this section, our goal is to find out how the long return series
(or more precisely, the first T −S observations of them) can contribute in
obtaining more precise estimates for the mean and covariance of the short
series. Our starting point is to evaluate to what extent the short series and
the overlapping part of the long series covary (that is, how much of the
information content of the short series is explained by the long series). We
can expect that they are not independent if there are common factors that
influence them.
Before plunging into the details of the calculations, we outline the basic
steps of the approach:
Step 1: Analyze the dependence of the short series on the long series by
running ordinary least squares (OLS) regressions.
Step 2: Compute the maximum likelihood estimates (MLEs) of the
expected return and covariance of the short and long series. The
MLEs of the long series are computed in the usual way. The MLEs
19Stambaugh (1997) proposes both a frequentist and a Bayesian approach to
combining series of different lengths. Here, we only discuss the latter.

112
BAYESIAN METHODS IN FINANCE
of the short series have additional terms reflecting their dependence
on the long series.
Step 3: Compute the predictive mean and covariance of next-period
returns.
Step 4: Proceed to portfolio optimization as discussed earlier in the
chapter.
We discuss next each of the first three steps in detail.
Dependence of the Short Series on the Long Series
We regress, using OLS, each of the N2 short series in R2 on the truncated
long series in R1, S. The regressions have the general form
R2
j = αj + βj1R1, S
1
+ . . . + βjN1R1, S
N1 + ϵj,
(6.23)
where R2
j denotes the S returns on asset j (the jth row of R2, j = 1, . . . , N2),
R1, S
i
denotes the truncated long return history of asset i, i = 1, . . . , N1, and
βji denotes the ‘‘exposure’’ of the short series of asset j to the overlapping
portion of the long series of asset i.
Denote the matrix of estimated slope coefficients by B:
B =


β1,1
. . . β1,N1
...
...
...
βN2,1 . . . βN2,N1

.
(6.24)
The rows of the N2 × N1 matrix B will serve as weights on the information
from the long series that feeds through to the moment estimates of the short
series. Before we proceed to show this, we briefly outline the Bayesian setup.
Bayesian Setup
Assume that RS has a multivariate normal distribution, independent across
periods, with mean vector
E =
 E1
E2

,
where E1 and E2 are the mean vectors of R1, S and R2, respectively, and
covariance matrix
V =
 V11 V12
V21 V22

,

Bayesian Framework for Portfolio Allocation
113
where V11 and V22 are the covariance matrices of R1, S and R2, respec-
tively, and V12 = V21—the matrices of covariances of R1, S and R2. Consider
an uninformative Bayesian setup, such that, the joint prior density is as
in (6.16),
p (E, V) ∝|V|−(N+1)/2.
Recall, from the discussion in scenario 1 above, that (in the equal-history
case) the mean and covariance of the predictive density of next-period’s
returns (given by the N × 1 vector RT+1) are, respectively,
E = E = Emle
(6.25)
and
V = (1 + 1/T) (T −1)
T −N −2
V =
T + 1
T −N −2Vmle,
(6.26)
where E and V are the sample moments defined in (6.7) and (6.8), while
Vmle is given by (6.9).
The general form of the predictive moments in the unequal-history
setting is the same as in the two expressions above. However, the maximum-
likelihood estimators (MLEs) now reflect the ‘‘feed-through’’ effect the long
series have on the short series. Next, we analyze this effect.
Predictive Moments
Before proceeding to explain the predictive moments of next-period’s excess
returns, we review the MLEs of the mean and the covariance of returns.
Considering only the overlapping portions of the return series, we can
compute the so-called ‘‘truncated’’ MLEs (as we would do if we wanted an
easy but suboptimal fix to the problem of unequal histories). The truncated
MLE of the joint mean vector E is the usual sample mean of the truncated
return data RS, given by the N1 + N2 × 1 vector
Emle
S
=
	
Emle
1, S
Emle
2, S

= 1
SRS1S,
where 1S is a S × 1 vector of ones.
The truncated MLE of the covariance matrix of excess returns is
given by
Vmle
S
=
	
Vmle
11, S Vmle
12, S
Vmle
21, S Vmle
22, S

,

114
BAYESIAN METHODS IN FINANCE
where the Vmle
11, S and Vmle
22, S are the estimators of the covariance matrices of
the truncated long and short series, respectively, and Vmle
12, S = Vmle
21, S
′ is the
estimator of the covariance between the long and short series.
Most notable here is the use of a familiar result from the analysis of
multifactor models (see Chapter 14) to write the following decomposition
of the truncated covariance estimator of the short series of returns:
Vmle
22, S = B
′Vmle
11, S B + ,
(6.27)
which follows from the regression in (6.23). The first term in (6.27) is the
portion of the covariance of the short-series explained by the long series.
The second term is the unexplained, residual portion of the covariance of
the short series.
Combined-Sample MLE of the Mean
It can be demonstrated that, when one
takes the unequal histories into account and allows for dependencies of the
short series on the long series, the combined-sample MLE of the mean of
the short series is
Emle
2
= Emle
2, S −B

Emle
1, S −Emle
1

,
(6.28)
where
Emle
1
= 1
T R11T
(6.29)
is the combined-sample MLE of the mean of the long series and 1T is a T ×
1 vector of ones.
Let us take a closer look at the expression in (6.28). The first term is the
truncated MLE of the short series. The second term is an adjustment factor
reflecting the additional information that the long series carries. Since Emle
1
is estimated using a larger number of returns, it is a more precise estimate
of (is closer to) the true mean of returns than Emle
1, S. Therefore, the difference

Emle
1, S −Emle
1

represents the error in estimating the true mean by using Emle
1, S
instead of Emle
1 .
What portion of this error is fed through to the truncated MLE, Emle
2 ?
The exposure of the short series to the long series is given by the matrix of
regression slopes B in (6.24). Therefore, the portion of estimation error in
the long series reflected in the estimator of the short series is B

Emle
1, S −Emle
1

.
Notice that the adjustment factor in (6.28) is subtracted from Emle
2, S, not
added. When Emle
1
exceeds Emle
1, S and the long and short series are positively
correlated, Emle
2, S is adjusted upward since the information coming from the
long series is that the truncated estimator underestimates the true mean,

Bayesian Framework for Portfolio Allocation
115
compared to the full estimator. Conversely, when Emle
1
is lower than Emle
1, S
and the series are positively correlated, Emle
2, S is adjusted downward.
Combined-Sample MLE of the Covariance Matrix
The combined-sample MLE
of the covariance matrix of excess returns is given by
Vmle =
	
Vmle
11
Vmle
1, 2
Vmle
2,1 Vmle
2, 2

.
We now consider each of its components separately;
■Vmle
11 is the usual MLE of the covariance of the long series:
Vmle
11 = 1
T
T

t=1

R1
t −Emle
1
′ 
R1
t −Emle
1

,
(6.30)
where R1
t is the N1 × 1 vector of returns at time t, t, t = 1, . . . , T.
■Vmle
12 is given by
Vmle
12 = Vmle
12, S −B

Vmle
11, S −Vmle
11

;
(6.31)
■Vmle
22 can be shown to be
Vmle
22 = Vmle
22, S −B

Vmle
11, S −Vmle
11

B
′ = BVmle
11 B
′ + .
(6.32)
Suppose that we only have two assets: Asset 1 with a long return history
and asset 2 with a short return history. Then Vmle
11 is the MLE of the variance
of asset 1, Vmle
12, S is the truncated estimator of the covariance between the
two assets, and Vmle
22, S is the truncated estimator of the variance of asset 2.
The adjustment factors in (6.31) and (6.32) rest on a similar intuition
to that of the mean estimator in (6.28). When the variance of asset 1 in
the most recent S periods is higher (lower) than the variance over the entire
sample, Vmle
12, S and Vmle
22, S are corrected for this over-underestimation error.
The amount of the correction depends on the exposure asset 2 has to asset
1, as in (6.28).
Predictive Moments of Future Excess Returns
Finally, we are ready to put
all elements together to obtain the moments of the predictive distribution
of next-period’s returns.

116
BAYESIAN METHODS IN FINANCE
From (6.25), the predictive mean coincides with the MLE. The predictive
covariance matrix can be written as
V =
 V11 V12
V21 V22

.
(6.33)
Each of the components of V are given below:
V11 =

T + 1
T −N −2

Vmle
11 ,
(6.34)
V12 =

T + 1
T −N −2

Vmle
12 ,
(6.35)
and
V22 =

c +

T + 1
T −N −2

BVmle
11 B
′
,
(6.36)
where
c =

S
S−N2−2
 
1 + 1
S

1 +
T+1
T−N−2tr

Vmle
11, S
−1Vmle
11

+

Emle
1
−Emle
1, S
′
Vmle
11, S
−1 
Emle
1
−Emle
1, S

.
(6.37)
The components of the covariance matrix estimator in (6.34) (6.35),
and (6.36) are all, not surprisingly, scaled-up versions of the respective
MLEs (recall that we assumed diffuse priors). In the same way as in the
equal-histories setting, the difference between the predictive covariance and
the sample covariance (that is, the estimation error) decreases as more data
become available (T increases).
The combined-sample predictive moments of returns can now be sub-
stituted in (6.14) to compute the optimal portfolio positions in the N1 + N2
assets.
SUMMARY
In this chapter, we presented an overview of the mean-variance portfolio
selection and got acquainted with the basic framework of the Bayesian
portfolio selection. The classical framework uses the sample estimates of
the mean and the covariance of returns as if they were the true parameters.
This failure to account for parameter uncertainty leads to optimal portfolio

Bayesian Framework for Portfolio Allocation
117
weights that are too sensitive to small changes in the inputs of the portfolio
optimization problem. Casting the problem in a Bayesian framework helps
deal with this sensitivity. The advantages of applying Bayesian methods to
portfolio selection go beyond accounting for uncertainty, as we will see in
the chapters ahead—they provide a sound theoretical platform for combin-
ing information coming from different sources, while their computational
toolbox allows for great modeling flexibility.

CHAPTER7
Prior Beliefs and
Asset Pricing Models
S
tudents of financial theory and practice can be overwhelmed by
the multitude of financial models describing the behavior of asset
returns. Do they use a general equilibrium asset pricing model such as
the capital asset pricing model (CAPM), an econometric model such
as the Fama and French’s (FF) three-factor model (Fama and French,
1992), or an arbitrage pricing model such as arbitrage pricing theory
(APT)?
Being a theoretical abstraction, no single model provide’s a completely
accurate and infallible description of financial phenomena. Should decision
making then discard all models as worthless? In this chapter, we demon-
strate how the Bayesian framework conveniently allows an investor to
incorporate an asset pricing model into the analysis and combine it with
prior beliefs. In doing this, an investor is able to express varying degrees of
confidence in the validity of the model—from complete belief to complete
skepticism.
Moreover, decision making need not be constrained to utilizing a
single asset pricing model. Suppose that an investor entertains the CAPM
and the FF models as possible alternatives to model the returns on a
portfolio of risky assets. The Bayesian framework provides an elegant
tool to account for the uncertainty about which model is true and to
produce a return forecast which averages out the forecasts of the individual
models.
In this and the next chapters, we expand the simple Bayesian applica-
tions to portfolio selection discussed in Chapter 6. This chapter provides a
description of how to enrich prior beliefs with the implications of an asset
pricing model. We also explain model uncertainty. In the following chapter,
we present a prominent example which incorporates an equilibrium model
into portfolio selection, the Black-Litterman model.
118

Prior Beliefs and Asset Pricing Models
119
PRIOR BELIEFS AND ASSET PRICING MODELS
More than three decades ago, Treynor and Black1 demonstrated the integra-
tion of security analysis with Markowitz’s approach to portfolio selection.
An investor’s special insights about individual securities can be combined
with CAPM’s implication that a rational (market-neutral) investor holds the
market portfolio. Although Treynor and Black’s analysis did not involve
Bayesian estimation, it is clear that the problem they posed is a perfect
candidate for it. The ‘‘special insights’’ about securities could be based on
a bottom-up valuation analysis, an asset pricing model or simply intuition.
In all cases, this ‘‘extra market’’ information is easily combined with the
available data within a Bayesian framework. A prominent example of this
is the model developed by the Quantitative Resources Group at Goldman
Sachs Asset Management, which originated with the work of Black and
Litterman (1991). We examine it in the next chapter. Here we offer a
treatment of a more general methodology of combining prior beliefs and
asset pricing models. Our exposition is based on the frameworks by P´astor
(2000) and P´astor and Stambaugh (1999), with some modifications.
Preliminaries
Suppose that the CAPM is the true model of asset returns. Since it is
an equilibrium model and all market participants are assumed to possess
identical information, each investor optimally holds a combination of the
market portfolio and the risk-free asset. The allocation to the risk-free
asset in the optimal portfolio depends on the degree of risk aversion (more
generally, on the investment objectives).
An econometric model describes prices or returns as functions of exoge-
nous variables, called factors or factor portfolios, which are often measures
of risk. If a given econometric model is believed to be valid, the investor’s
optimal portfolio consists of a combination of the factor portfolios exposing
the investor only to known sources of risk priced by the model.
When a decision maker is completely skeptical with regards to an
asset pricing model and only wishes to account for the error intrinsic in
parameter estimation, he could accomplish a ‘‘no-frill’’ portfolio selection in
the manner described in Chapter 6. It is more likely, however, that although
aware of the deficiencies of pricing models, he is not prepared to discard
them altogether. Before we describe how to express in a quantitative way
the uncertainty about model validity, we briefly review both the CAPM and
a general factor model.
1Treynor and Black (1973).

120
BAYESIAN METHODS IN FINANCE
The CAPM is based on two categories of assumptions: (1) the way
investors make decisions and (2) the characteristics of the capital market.
Investors are assumed to be risk-averse and to make one-period investment
decisions based on the expected return and the variance of returns. Capital
markets are assumed to be perfectly competitive; it is assumed that a
risk-free asset exists at which investors can lend and borrow. Based on these
assumptions, the CAPM is written as
E(Ri) −Rf = βi(E(RM) −Rf),
(7.1)
where: E

Ri

= expected return of the risky asset i.
Rf = risk-free rate (assumed constant).
E

RM

= expected return on the market portfolio.
βi = measure of systematic risk of asset i (referred to as beta).
The CAPM states that, given the assumptions, the expected return of an
asset is a linear function of its measure of systematic risk (beta). No other
factors, apart from the market, should systematically affect the expected
asset return. Risk coming from all other sources can be diversified away.
The empirical analogue of the CAPM is written in the form of a linear
regression:
Ri,t −Rf = α + β

RM,t −Rf

+ ϵi,t,
(7.2)
for i = 1, . . . , K, where: Ri,t = asset i’s return at time t
RM,t = market portfolio’s return at time t
ϵi,t = asset i’s specific return at time t
A factor-based model states that the expected return of an asset is propor-
tional to a linear combination of premia on risk factors:
E(Ri) −Rf = βi,1

E

f1

−Rf

+ · · · + βi,k

E

fk

−Rf

,
(7.3)
where: E

fj

= expected return on factor j.
βi,j = sensitivity of the expected return of asset i to factor j.
To estimate the factor sensitivities, we write (7.3) in its empirical form as
Ri,t −Rf = α + βi,1

f1,t −Rf

+ · · · + βi,K

fK,t −Rf

+ ϵi,t.
(7.4)
The coefficient α in (7.2) and (7.4) are often referred to as alpha and in
the context of realized performance sometimes interpreted as an ex post

Prior Beliefs and Asset Pricing Models
121
measure of skill of an active portfolio manager.2 In the context of security
selection, a positive (negative) ex post α is a signal that an asset is under-
priced (overpriced). The investor would gain from a long position in an
asset with positive alpha and a short position in an asset with a negative
alpha.3 Ex ante, α is the forecast of the active stock (portfolio) return.
Quantifying the Belief about Pricing Model Validity
A correct asset pricing model prices the stock/portfolio of stocks exactly.
Therefore, if the model is valid, it is the case that the true (population) α is
zero. Equivalently, to use a tautology, we say that a correct model implies
no mispricing. Consider an investor who is skeptical about the pricing
implications in (7.1) and (7.3). This skepticism is reflected in a belief that
the pricing relationship is in fact ‘‘off’’ by some amount λ:
E(Ri) −Rf = λ + βi

E(RM) −Rf

or
E(Ri) −Rf = λ + β1

E

f1

−Rf

+ · · · + βk

E

fk

−Rf

.
That is, the investor’s subjective belief is expressed as a perturbation of the
‘‘ideal’’ model.
Perturbed Model
Our goal is to estimate the perturbed model in a Bayesian setting so as to
be able to reflect the investor’s uncertainty about the pricing power of a
model. Certainly, the observed data also provide (objective) validation of
the pricing model. The resulting predictive distribution of returns not only
reflects parameter estimation risk but also the investor’s prior uncertainty
updated with the data.
We are interested in modeling the excess return on a risky asset (an
individual stock or a portfolio of stocks). Throughout the rest of the chapter,
2In asset pricing, ex ante refers to expected or predicted quantities, and ex post—to
realized (observed) or estimated quantities. In Chapter 9, we come across the
important distinction between the two once again in the context of market efficiency
testing.
3The reason is that adding (shorting) an asset with a positive (negative) alpha to the
holding of the market portfolio increases (decreases) the resulting active portfolio’s
Sharpe ratio. (See equation (6.6) in Chapter 6.)

122
BAYESIAN METHODS IN FINANCE
we write ‘‘return’’ instead of ‘‘excess return’’ for simplicity—and denote the
asset’s return by Rt. In addition, we observe the returns on K benchmark
(factor) portfolios, f 1,t, f 2,t, . . . , f K,t. In the case of the CAPM, K = 1
since there is a single benchmark portfolio—the market portfolio. Data are
available for T periods, t = 1, . . . , T. The investor allocates funds between
the risky asset and the K benchmark portfolios. The model we estimate is
then given by
Rt = α + β1ft,1 + · · · + βK ft,K + ϵt.
(7.5)
To write (7.5) compactly in matrix notation, denote by R the T × 1
vector of excess returns on the risky asset. The T × K matrix of benchmark
excess returns is denoted by F. Then, we write
R = Xb + ϵ.
(7.6)
where X is defined as (1 F), 1 is a T × 1 vector of ones, and ϵ is the T × 1
vector of asset-specific returns (regression disturbances). The (K + 1) × 1
vector of regression coefficients b is expressed as
b =
 α
β

,
where β is the K × 1 vector of exposures of the risky asset to the K risk
sources, that is, the factor loadings.
As discussed in Chapter 3, estimation of (7.6) involves the following
steps: specification of the likelihood for the model parameters, expressing
subjective beliefs in the form of prior distributions, and deriving (computing)
theposteriordistributions.Wedescribeeachofthesestepsinthenextsections.
Likelihood Function
We adopt standard assumptions for the regression parameters in (7.6).
Disturbances are assumed uncorrelated with the regressors (the benchmark
return series) and independently and identically distributed (i.i.d.) with a
normal distribution, centered at zero and variance σ 2. Therefore, asset
returns are distributed normally with mean Xb and variance σ 2:
R ∼N(Xb, σ 2IT),
where IT is a T × T identity matrix. The likelihood function of the model
parameters, b and σ 2, is given (as in Chapter 3) by
L

b, σ |R, X

∝(σ 2)−T/2 exp

−1
2σ 2 (R −Xb)′(R −Xb)

.
(7.7)

Prior Beliefs and Asset Pricing Models
123
Now, the question of whether to treat the K benchmark returns (premia) in
F as nonstochastic (constants) or stochastic (random variables) arises. The
importance of this distinction is highlighted by some empirical evidence,
suggesting that estimation errors in the risk premia have a stronger impact
on the (im)precision in estimating the expected asset returns than estimation
errors in βk, k = 1, . . . , K.4 Therefore, in order to take the uncertainty about
the components of F into account, we make the assumption that benchmark
returns are stochastic and follow a multivariate normal distribution:
Ft ∼N(E, V),
where: Ft = 1 × K vector of benchmark returns at time t (the tth row of F).
E = 1 × K vector of expected benchmark returns.
V = K × K covariance matrix of the benchmark returns.
The likelihood function for E and V is written as
L (E, V | F) ∝|V|−K/2 exp

−1
2
T

t=1
(Ft −E)′V−1(Ft −E)

.
(7.8)
Prior Distributions
The perturbation of the ideal model discussed earlier is easily expressed as
a prior probability distribution on α. The mean of α is set equal to zero to
reflect the default scenario of no mispricing. The standard deviation of α, σ α,
is a parameter whose value is chosen by the investor to reflect the degree of
his confidence in the asset pricing model. Suppose, on the other hand, that,
instead of an asset pricing model, the investor would like to incorporate the
predictions of a stock analyst in his decision-making process. Then, α’s prior
distribution will be centered on those predictions, and σ α will represent the
confidence in them. The lower σ α is, the stronger the belief in the model’s
implications. At one extreme is σα = 0—the prior distribution of α degener-
ates to a single point, its mean of zero—the investor is certain that (7.1) ((7.3))
holds exactly. At the other extreme, σα = ∞, that is, the prior distribution of
α is completely flat (diffuse) and the investor rejects the model as worthless.
We assume that the model parameters (the regression coefficients and
the disturbance variance) have a natural conjugate prior distributions,
b |σ 2 ∼N(b0, σ 2 0)
(7.9)
σ 2 ∼Inv-χ 2
ν0, c2
0

,
(7.10)
4For example, see P´astor and Stambaugh (1999) and the references therein.

124
BAYESIAN METHODS IN FINANCE
where 0 is a positive definite matrix and Inv-χ 2
ν0, c2
0

denotes the scaled
inverted χ 2 distribution with degrees of freedom ν0 and scale parameter c2
0
given in (3.62).
The prior mean of the vector of regression coefficients is
b0 =
 α0
β0

,
(7.11)
with α0 = 0, as explained above, while 0 can be expressed as
0 =
 σ 2
α
1
σ 2
0
0
β

.
(7.12)
We set the off-diagonal elements in (7.12) equal to zero since we
do not have a priori reasons to believe that the intercepts are correlated
with the regression slopes—that is, that the mispricing is correlated with
the factor loadings. Since we are not interested in inference about the
factor loadings, β, we impose a weak prior on them by specifying β
as a diagonal matrix with large diagonal elements. Notice our choice
for the first diagonal element of 0—the aim of this formulation is to
make the variance of α equal to the investor-specified σ 2
α , which reflects
the skepticism about the pricing model’s implications. We soon investi-
gate the influence different choices of σ 2
α have on the optimal portfolio
composition.
The prior for the mean vector, E, and the covariance matrix, V, of the
benchmark returns is assumed to be Jeffreys’ prior (see Chapter 3),
E, V ∝|V|−(T+1)/2.
(7.13)
Posterior Distributions
Posterior Distribution of b, conditional on σ 2
Since we made natural con-
jugate prior assumptions about the parameters of the normal model, we
obtain posterior distributions of the same form as the prior distributions.
The posterior distribution of b, conditional on σ 2, is multivariate normal
with mean b
∗and covariance matrix σ 2∗,
b | σ 2, R, X ∝N

b
∗, σ 2∗
,
(7.14)
where (from (3.39) and (3.40))
∗=

−1
0 + X′X
−1
(7.15)


## Asset Pricing Models

Prior Beliefs and Asset Pricing Models
125
and
b
∗≡
 α∗
β∗

= ∗
−1
0 b0 + X′X 	b

.
(7.16)
In (7.16), 	b denotes the least-squares estimate of b, which is also
its maximum-likelihood estimate (MLE). The posterior mean, b
∗, is, as
expected, a shrinkage estimator of b—a weighted average of its prior
mean, b0, and its MLE, 	b. The weights are functions of the sample precision
(σ 2(X′X)−1)−1 and the prior precision (σ 20)−1, and reflect the shrinkage of
the sample estimate of b toward the prior mean.5
Posterior Distribution of σ 2
The posterior distribution of σ 2 is an inverted
χ 2 distribution,
σ 2 ∼Inv-χ 2
ν∗, c2∗
,
(7.17)
with the posterior parameters ν* and c2* given by (as in (3.42) and (3.43))
ν∗= T + ν0
(7.18)
and
c2∗= 1
ν∗

ν0c2
0 +

R −X	b
′
R −X	b

+

b0 −	b
′K

b0 −	b

.
(7.19)
where K =

0 + (X′X)−1−1.
Posterior Distributions of the Benchmark Parameters
The posterior distri-
butions of the moments of the benchmark returns are normal and inverted
Wishart,
E |V, F ∼N

	E, V
T

(7.20)
V |F ∼IW (, T −1) ,
(7.21)
5To see that, rewrite the expression for b∗in (7.16) as
b∗= σ 2∗
(σ 2)−1b0 + (σ 2(X′X)−1)−1	b

.
From standard results of multivariate regression analysis, we can recognize
σ 2(X′X)−1 as the covariance matrix of 	b.

126
BAYESIAN METHODS IN FINANCE
where
	E = 1
T
T

t=1
Ft
and
 =
T

t=1
(Ft −	E)′(Ft −	E).
Predictive Distributions and Portfolio Selection
In Chapter 6, we provided the foundations of Bayesian portfolio selection
and we explained that the key input for the portfolio problem is the
predictive distribution of next-period returns. The optimal portfolio weights
are as given in (6.14) in Chapter 6.
Denote by FT+1 the 1 × K vector of next-period’s benchmark returns. Let
RT+1 denote next-period excess return on the risky asset. Since the investor
allocates funds among the risky asset and the K benchmark portfolios, the
predictive moments, µ and , are in fact the joint predictive mean and
covariance of

RT+1, FT+1

.
Since we assume that benchmark returns are random variables them-
selves, we first need to predict FT+1 before we are able to predict RT+1.
As in Chapter 6, the predictive distribution of FT+1 is multivariate Stu-
dent’s t-distribution with T−K degrees of freedom. The predictive mean
and covariance of FT+1 are, respectively
EF = 	E
and
VF =
T + 1
T(T −K −2).
(7.22)
The predictive distribution of next-period’s returns is Student’s t with
T + ν0 degrees of freedom, with predictive mean given by
ER = EXb
∗
(7.23)
and variance
VR =
T + ν0
T + ν0 −2 c2∗
1 −EX∗EX

,
(7.24)
where EX is

1EF

. Finally, the predictive covariance between next-period’s
risky asset’s return, RT+1, and next-period’s return on benchmark j, Fj,T+1,

Prior Beliefs and Asset Pricing Models
127
is obtained from6
VR,F = β∗
j VF, jj,
(7.25)
where β∗
j is the posterior mean of the jth factor loading and VF,jj is the jth
diagonal component of VF.
Now, combining the results in (7.22), (7.23), (7.24) and (7.25), we
obtain the joint predictive mean and covariance used for portfolio optimiza-
tion,
µ =
 ER
EF

and
 =
 VR
VR, F
VR, F
VF

.
Applying (6.14), we compute the optimal portfolio weights. We stress that
we do not need to have analytical expressions for the posteriors nor the
predictive densities. As long as we are able to simulate from them, we can
compute the optimal portfolio weights. Appendix A of this chapter outlines
the step-by-step procedure to do so.
Prior Parameter Elicitation
The hyperparameters whose values we need to specify for the calculations
in the previous section are the vector of prior means, b0, and the prior
covariance matrix, 0, from the prior distribution of b, as well as the
degrees of freedom ν0 and the scale parameter c2
0 from the prior distribution
of σ 2.
■The first element of b0, α0, is set equal to 0 to reflect the ‘‘default’’ case
of no mispricing in the asset pricing model.
■The prior means of the benchmark loadings, β0, could be specified
to be zero as well, in case no other prior intuition exists about their
values. Presample estimates of the loadings could be employed as
well.
6Recall that an asset’s beta with respect to a risk factor is defined as the covariance
of the asset’s return with the factor’s return divided by the variance of the factor’s
return.

128
BAYESIAN METHODS IN FINANCE
■Since inference about σ 2 is not of particular interest to us in this chapter,
we could make its prior relatively uninformative (flat) by specifying a
small value (greater than 4) for the prior degrees of freedom parameter
ν0.7 Thus, we let the data dominate in determining the posterior
distribution of σ 2. The scale parameter c2
0 is determined indirectly from
the expression for the expectation of an inverse χ 2 random variable,
E(σ 2) = ν0c2
0/(ν0 −2). The expectation, E(σ 2), is estimated from the
presample data as the residual variance.
■Specifying the elements of the prior covariance matrix, σ 2
α and β, in
(7.12) requires only a small additional effort. As mentioned earlier, we
make the prior on the factor loadings uninformative by letting their
covariance, β, equal to a diagonal matrix with very large diagonal
elements, for example,
β = 100IK,
(7.26)
where IK is a K × K identity matrix. The value of σ 2
α depends on the
investor’s confidence in the validity of the asset pricing model. It ranges
from zero (full confidence) to infinity (complete skepticism).
Illustration: Incorporating Confidence about the
Validity of an Asset Pricing Model
In this section, we present an illustration of the previous discussion.8 We
consider an investor entertaining the CAPM as an asset-pricing model option
(corresponding to K = 1 in (7.6)). Our goal is to examine the asset allocation
decision for varying degrees of confidence in the pricing model. The investor
allocates his funds between the risky asset and the market portfolio. The
risky asset is represented by the monthly return on IBM stock. The data on
the stock and portfolios cover the period January 1996 to December 2005.
Exhibit 7.1 presents the posterior means of the intercept and the loading on
the market, as well as the optimal allocations for five different values of σ 2
α ,
representing five levels of scepticism about the model’s pricing power.
We can observe that as uncertainty about the pricing model increases,
the allocation to the risky asset increases—strong belief in the validity
of the pricing model implies that the stock is priced correctly and, therefore,
the investor optimally invests his whole wealth in the market portfolio;
conversely, as σ 2
α increases, the investor gives more credence to the positive
posterior alpha of IBM and reallocates funds to the IBM stock accordingly.
7An inverse χ2
ν random variable has a finite variance if its degrees of freedom
parameter, ν, is greater than 4.
8The illustration is based on an application in P´astor (2000).

Prior Beliefs and Asset Pricing Models
129
IBM Stock
Market
Skepticism
None
sa 0 = 0%
Small
sa = 1%
Medium
sa = 5%
Big
sa = 15%
Complete
sa = ∞
Sample
Means
ˆ
ˆ = 1.307
~ = 0.067
E
Prior
Means
a0 = 0
b0 = 0.617
b
a
-
Posterior
Means
~a = 0.0
~b = 1.296
~b = 1.296
~a = 0.001
~a = 0.017
~a = 0.052
~a = 0.068
~b = 1.293
~b = 1.286
~b = 1.292
~ = 0.067
E
Optimal
Allocation
0%
1.29%
26 .6%
86.5%
101%
= 0.068
(
)
EXHIBIT 7.1
Optimal allocation of the IBM stock given varying degrees of
uncertainty in the validity of the CAPM
Note: The standard deviations, values for alpha, as well as expected market returns
are annualized.
Next, we explicitly account for the uncertainty about which model is
the correct one and discuss portfolio choice based on the combined posterior
inference.
MODEL UNCERTAINTY
In the previous section, we considered separately two out of a number
of possible asset pricing models. Typically, data analysis is initiated by
selecting a single ‘‘best’’ model, which is then treated as the true one and
used for inferences and predictions. Sound familiar? This practice mirrors
on a magnified level the one of treating the sample estimate of a parameter as
the true parameter in inferences and predictions. No matter which model we
select to assist us in the decision-making process, we could never be certain
it is correctly specified to describe the true data-generating process. Since all
models employed in finance are inevitably only approximations, accounting
for model risk (i.e., the ambiguity associated with model selection) is an
important element of the inference process.9
9Treatment of model risk has not yet become the norm in the empirical finance liter-
ature. Cremers (2002) and Avramov (2002) discuss it in the context of predictability;
and P´astor and Stambaugh (1999) provide a brief overview in the context of asset
pricing models.

130
BAYESIAN METHODS IN FINANCE
Two principal sources of model risk in empirical finance are:
■Suppose a researcher analyzes a set of data and detects the presence
of a certain structure in it. It is possible that the data are in fact
nearly random and the apparent structure is due simply to a spurious
relationship.
■A common simplification is to specify a static model for the data, when
in fact they have been generated by a process with a time-varying
structure; if a dynamic model is assumed, there is a risk of misspecifying
the dynamic structure.
The first source of risk is due to the large degree of noise present in financial
data. The model could leverage this noise, interpreting it as a regularity
of the data. Consider, for example, the extensive debate in the empirical
finance literature about whether stock returns are predictable. The critics of
predictability have argued that the predictive relationships found between
stock returns and certain fundamental or macroeconomic variables are
spurious or the result of data mining.10 Even supporters of predictability
have not been able to achieve consensus—neither about the identity of
the predictive variables, nor about the combination of them that would
best describe the behavior of stock returns. No doubt both camps would
agree that model risk plays a major role in their analyses. (We examine
predictability in Chapter 9.)
The second source of error is often the more serious one. Consider
estimation of a financial model with quarterly data. Then, in order to collect
a large enough data sample, one has to consider a sufficiently long period of
financial data history. However, it is possible that the economic paradigm
has undergone changes during that period. A static model could be a misspec-
ification for the underlying time-varying, data-generating process, thus pro-
ducing large forecasting errors. One way of dealing with time-variation is by
means of regime-switching models. We discuss these models in Chapter 11.
In general, model risk is a factor that dilutes our inferences. We can
think of specifying a single model as giving up a part of our degrees of
freedom—there is less information left available to estimate the model
parameters. As a result, we end up with noisier parameter estimates and
predictions.
In the illustration in the previous section, we selected a model (the
CAPM) and discussed how to account for the uncertainty about its pricing
ability, that is, for the within-model uncertainty. In doing so, we implic-
itly conditioned our analysis on the single model. The Bayesian model
10See, for example, Lo and MacKinlay (1990).

Prior Beliefs and Asset Pricing Models
131
averaging (BMA) methodology allows one to explicitly incorporate model
uncertainty by conditioning on all models from the universe of models
considered. Each model is assigned a posterior probability, which serves as
a weight in the ‘‘mega’’ composite model. Thus we are able to evaluate the
between-model uncertainty and, more importantly, draw inferences based
on the composite model.
In the next section, we describe the systematic framework of BMA.11
Bayesian Model Averaging
It is helpful to think of the BMA setting as a hierarchical parameter
setting. We start at the highest level of the hierarchy with a true, unknown
model. We regard each of the candidate models as a perturbation of the
true model. Assuming we entertain N models as plausible, denote model
j by Mj, j = 1, . . . , N. Mj is a parameter associated with the particular model
that governs its ‘‘credibility share’’ of the true model. We assert a prior
distribution on Mj, based on our belief about how credible a candidate the
model is, we update the prior with the information contained in the data
sample and arrive at a posterior distribution reflecting the model’s updated
credibility. At the lower hierarchical level, we find the parameter vectors θj
of each model j. The updating procedure of their distributions is essentially
the one discussed earlier in the chapter.
Prior Distributions
The choice of prior model distributions is naturally
based on the existence of a particular intuition about the relative plausibility
of the models in consideration. For example, there is now little disagreement
among academics and practitioners that more than one pervasive factor
influence the comovement of stock returns. Therefore, a single-factor model
might get less of a prior weight than a multifactor model.
As in the previous section, let’s consider only two models—the CAPM
and the FF three-factor model—as potential candidates for the true asset
pricing model. Denote the prior probability of model j by pj ≡p (Mj),
where j = 1 refers to the CAPM and j = 2 corresponds to the FF model. It
is not unusual, in the absence of specific intuition about model plausibility,
to assume that the models are equally likely. Then, each of them will be
assigned a prior model probability pj = 1/2.12
11See Hoeting et al. (1999) for an introduction to BMA.
12In the context of predictability, Cremers (2002) suggests the following intuitive
approach to asserting a model prior. Suppose there are K variables which, one
believes, are potential predictors for the excess stock returns. The number of possible

132
BAYESIAN METHODS IN FINANCE
The prior distributions of the parameters under model j are conditional
on the model. Denote the prior by p(θj | Mj) = p(b | σ 2)p(σ 2), where θj is the
vector of parameters of model j, θj = (bj, σ 2). The vector b1 is a 2 × 1 vector,
consisting of the intercept, α1 and β1, the sensitivity of the risky asset to
market risk (the CAPM setting). The vector b2 is a 4 × 1 vector consisting of
the intercept α2 and the vector of exposures to the three factor risks, β2 (the
FF three-factor setting). Assume that the priors of the model parameters (the
elements of θ) are as given in (7.9) and (7.10). For simplicity, we consider
the factor returns nonstochastic in the current discussion.
Posterior Model Probabilities and Posterior Parameter Distributions
The
posterior model probabilities play a key role in deriving the posterior
parameter distributions. The posterior probability of model j is computed
using Bayes’ formula from Chapter 2:
p

Mj | R

=
p

R | Mj

p

Mj

2
k=1 p

R | Mk

p

Mk
.
(7.27)
In the following discussion, we suppress the dependence on X for
notational simplicity. The term p

R | Mj

in (7.27) is the marginal likelihood
of model j and is computed by integrating model j’s parameters from their
likelihood:
p

R | Mj

=

L(b, σ 2 | R, Mj) p (b, σ 2 | Mj) d b d σ 2,
(7.28)
where L(b, σ 2|R, Mj) is the likelihood for the parameters of model j (given in
(7.7)) and p(b, σ 2|Mj) is the joint prior distribution for model j’s parameters
(which factors into the densities given in (7.9) and (7.10)). See Appendix
B of this chapter for the computation of the likelihood of model j in the
setting of this chapter.
distinct combinations of these variables is 2K and there are as many (linear) models
that could describe the return-generating process. Let each variable’s inclusion in
a model is equally likely and independent, with probability ρ. Denote by 1 the
event that variable j is included in model i, and by 0 the event that it is not. This
describes a Bernoulli trial. The prior probability of model i can then be viewed
as the joint probability of the particular combination of variables or the Bernoulli
likelihood function (see Chapter 4). It is given by p (Mi) = ρκ(1 −ρ)K−κ, where κ
is the number of variables included in the ith model. Note that when ρ = 1/2, all
models are equally likely. It is easy to generalize this prior model probability and
assign different probabilities, ρ, to different (groups of) variables.

Prior Beliefs and Asset Pricing Models
133
Given a particular model, Mj, the posterior distribution of the parameter
vector is p(θj | R, Mj) and can be factored into
p (θj | R, Mj) = p(b | σ 2, R, Mj) p(σ 2 | R, Mj).
(7.29)
The marginal posterior distributions p (b | σ 2, R, Mj) and p (σ | R, Mj) are the
same as in (9.21) and (7.17), respectively.
To remove the conditioning on model j, and to obtain the overall
posterior distribution of θ, we average the posterior parameter distributions
across all models:
p (b | σ 2, R) =
2

j=1
p (b | σ 2, R, Mj) p (Mj | R)
(7.30)
and
p (σ 2 | R) =
2

j=1
p (σ 2 | R, Mj) p (Mj | R).
(7.31)
The posterior distribution under each model is weighted by the posterior
probability of the respective model. That represents one of the most attractive
featuresofBMA—theposteriormeanandvarianceofthemodelparametersb
and σ 2 are computed as averages over the posterior moments from all models.
The predictive ability is thus improved in comparison with using a single
model.13 Denote by b
∗
j and σ 2
j
∗the posterior means of b and σ 2 under model j.
The (unconditional) posterior means across all models are, respectively,
b
∗=
2

j=1
b
∗
j p (Mj | R),
(7.32)
and
σ 2∗=
2

j=1
σ 2
j
∗p (Mj | R).
(7.33)
Predictive Distribution and Portfolio Selection
The overall predictive distri-
bution of excess returns next period is a weighted average of the predictive
distributions of returns across the individual models:
p (RT+1 | R) =
2

j=1
p (Mj | R) p (RT+1 | R, Mj).
(7.34)
13See Madigan and Raftery (1994).

134
BAYESIAN METHODS IN FINANCE
Sampling from the overall predictive distribution is accomplished by sam-
pling from the predictive distribution under each model and then computing
the weighted average of the draws across models. The predictive mean and
variance are obtained as weighted averages as well (in the same way as the
posterior parameter moments were obtained earlier).
Illustration: Combining Inference from the CAPM
and the Fama and French Three-Factor Model
Here, we provide an example of computing posterior model probabilities
for two models—the CAPM and the Fama and French (FF) three-factor
model, using again IBM stock as the risky asset. Fama and French (1992)
assert that, in addition to the market, there are two more risk factors—value
and size—that drive stock returns and should, therefore, be priced by the
model. It has been empirically observed that small-capitalization stocks
and stocks with high book-to-market value outperform large-capitalization
stocks and stocks with low book-to-market value, respectively. To capture
these size and value premiums, the two risk factors are represented by
zero-investment (factor) portfolios. The size-factor portfolio consists of a
long position in small-capitalization stocks and a short position of equal
size in large-capitalization stocks. The value-factor portfolio is constructed
by going long in high book-to-market value stocks and going short in
low book-to-market value stocks. These factor portfolios have been called,
respectively, small minus big (SMB) and high minus low (HML). (For more
details on multifactor models, see Chapter 14.) Given the prior and data
assumptions made earlier in the chapter, we calculate the posterior model
probabilities; 98.9% for the CAPM and 1.11% for the FF model.
Simulating from the predictive distribution of IBM returns is accom-
plished using (7.34) and the simulation procedure in Appendix A, as follows.
First, select the CAPM with probability 98.9% and the FF model with prob-
ability 1.11%. To do this, draw an observation, U, from uniform [0,1]
distribution. If U ≤0.989, select the CAPM; if U ≤0.11, select the FF
model. Second, conditional on the selected model, draw from the posteriors
of b and σ 2. Third, draw RT+1 from its normal distribution.
We simulate a sample of 30,000 observations of RT+1 and obtain an
(annualized) predictive mean for the returns on IBM equal to 8.52%. These
are simulations from the composite model, thus accounting for model risk.
In a model with more than one risky asset, we could produce simulations
from the composite model in the way just described and then use these to
determine the optimal portfolio composition.

Prior Beliefs and Asset Pricing Models
135
SUMMARY
Combining prior beliefs with asset pricing models introduces structure and
economic justification into Bayesian portfolio selection. We continue along
these lines in the following two chapters. In Chapter 8, we review the
Black-Litterman model, while in Chapter 9 we explore market efficiency
and predictability.
Whenever possible, model uncertainty should be incorporated into the
decision-making process in order to reflect the risk investors face, in addition
to parameter uncertainty.
APPENDIX A: NUMERICAL SIMULATION OF THE
PREDICTIVE DISTRIBUTION
In this appendix, we outline the steps for simulating from the predictive dis-
tributions of next-period’s risky asset’s return, RT+1 and next-period’s bench-
mark
returns,
FT+1,
as
well
as
for
computing
their
predictive
moments.
We write the predictive distribution of RT+1 as
p

RT+1 | R

=

p

RT+1 | b, σ 2, XT+1, R

× p

b, σ 2 | R, X

p

FT+1 | F

dFT+1 db dσ 2,
(7.35)
where XT+1 is (1 FT+1), while R and F denote, respectively, the returns
on the risky asset and the benchmarks available up to time T. Since
FT+1 is random, it needs to be integrated out, together with the param-
eters, to compute the predictive density. Thus, not only the parameter
uncertainty about b and σ 2 is accounted for but the uncertainty about
FT+1 as well. All densities on the right-hand side in (7.35) are known
densities:
■p

RT+1 | b, σ, XT+1, R

is a normal density with mean zero and variance
σ 2. To see that, consider (7.6) and roll it forward one period.
■p

b, σ 2 | R, X

factors into p

b | σ 2, R, X

p

σ 2 | R, X

, which are the
posterior densities in (9.21) and (7.17).
■p

FT+1 | F

is the multivariate Student’s t predictive distribution of FT+1
with parameters given in (7.22).

136
BAYESIAN METHODS IN FINANCE
The predictive distribution of FT+1 is written in a similar way as
p

FT+1 | F

=

p

FT+1 | F, E, V

× p

E | V, F

p

V | F

dE dV.
(7.36)
The distributions on the right-hand side are known as well; p

FT+1 | F,
E, V

is a multivariate normal with mean E and covariance V, p

E | V, F

and p

V | F

are the posteriors given in (7.20) and (7.21), respectively.
Sampling from the Predictive Distribution
We turn now to sampling (simulation) from the joint predictive distribution
of

RT+1, FT+1

. We focus on the joint predictive distribution since the joint
mean and the joint covariance of

RT+1, FT+1

are required to solve the
portfolio optimization problem, as explained in the chapter. A draw from
the joint predictive distribution is obtained using the following sequence of
steps:
1. Draw a K × 1 vector FT+1 from the predictive distribution p

FT+1 | F

:
a. Draw V from its inverse Wishart posterior density in (7.21).
b. Conditional on the draw of V, draw E from its normal posterior
density in (7.21).
c. Conditional on the draws of V and E, draw FT+1 from the multivari-
ate normal distribution N

E, V

.
2. Draw RT+1 from its predictive distribution:
a. Draw σ 2 from its inverse χ 2 posterior density in (7.17).14
b. Conditional on the draw of σ 2, draw b from its normal posterior
density in (9.21).
c. Conditional on the draws of FT+1, b, and σ 2, draw RT+1 from the
normal distribution N

XT+1b, σ 2
.
Repeating the procedure a large number of times and collecting the
pairs

RT+1, FT+1

, we obtain a sample from the joint predictive distribution
of next-period’s excess returns, RT+1, and next-period’s returns on the K
benchmark portfolios, FT+1. We now explain how to compute the joint
predictive mean and covariance.
14To obtain a draw of σ 2 from its inverse χ2(ν*, c2*) distribution, we draw τ from
χ2
ν and set σ 2 equal to ν* c2*/τ. Notice also that drawing from χ2
ν is equivalent to
drawing from (ν/2, 1/2).

Prior Beliefs and Asset Pricing Models
137
Suppose we have obtained M draws from the joint predictive distribu-
tion. Denote by SM the M × (K + 1) matrix of simulated draws. The mth
row of SM is given by
SMm =

Rm
T+1, Fm
T+1
′
,
where Rm
T+1 and Fm
T+1 are the mth draws from their respective (marginal)
predictive distributions.
Joint Predictive Mean
The (K + 1) × 1 joint predictive mean vector, µ, is
computed by taking the average along the columns of the matrix SM:
µ =
 1
M
M

m=1
Rm
T+1, 1
M
M

m=1
Fm
T+1
′

.
(7.37)
Joint Predictive Covariance
Let’s recall two expressions for the variance
and covariance of random variables, which can be found in any intermediate
statistics textbook. The variance of a random variable Y is given by
var(Y) = E(Y2) −E(Y)2,
(7.38)
where E denotes the expectation. The covariance between two random
variables Y and Z is
cov(Y, Z) = E(YZ) −E(Y)E(Z).
(7.39)
The (K + 1) × (K + 1) joint predictive covariance matrix, , of

RT+1, FT+1

can be written as follows:
 =


1,1
1,2
. . .
1, K+1
...
...
...
...
K+1,1 K+1,2 . . . K+1, K+1

.
Let’s see how each of the elements of  is computed:
■1,1 denotes the predictive variance of RT+1. We use (7.38) to compute
1,1, but we replace the expectations with sample means:
1,1 = 1
M
M

m=1

Rm
T+1
2 −

1
M
M

m=1
Rm
T+1
2
,
(7.40)

138
BAYESIAN METHODS IN FINANCE
■j,j, j = 2, . . . , K + 1, denotes the predictive variance of the jth bench-
mark’s returns. For j = 2, . . . , K + 1, we compute each j,j as in (7.40),
substituting F
m, j−1
T+1
for Rm
T+1,
■1, j, j = 2, . . . , K + 1, denotes the predictive covariance between the
returns on the risky asset and the returns on the (j −1)st benchmark.
We use (7.39) to obtain
1, j = 1
M
M

m=1
Rm
T+1F
m, j−1
T+1 −

1
M
M

m=1
Rm
T+1
 
1
M
M

m=1
F
m,j
T+1

,
(7.41)
where F
m, j
T+1, denotes the mth draw of the predictive return on the
(j −1)st benchmark.
■i, j, i ̸= j, i, j > 1 denotes the predictive covariance between the returns
on the ith and jth benchmarks. Each of them is computed as in (7.41),
substituting Fm, i−1
T+1
for Rm
T+1.
The computations above are applications of Monte Carlo integra-
tion (see Chapter 5). Having obtained µ and , it is just a matter of
straightforward algebra to arrive at the optimal portfolio weights in (6.14).
APPENDIX B: LIKELIHOOD FUNCTION OF A CANDIDATE
MODEL
Here, we derive the likelihood of model j in (7.28). Let’s substitute the
likelihood for the parameters, b and σ 2, given in (7.7), and their full priors
into (7.28). We obtain
p

Mj | R, X

=
 
σ 2−T/2 exp

−1
2σ 2

R −Xb
′ 
R −Xb

×

σ 2−1/2||−1/2 exp

−1
2σ 2

b −b0
′ −1 
b −b0

×
 ν0
2
ν0/2

 ν0
2
 cν
0

σ 2−

ν0
2 +1

exp

−ν0c2
0
2σ 2

db dσ 2.
(7.42)
Notice that our objective is to compute a probability, not the kernel
of a density. Therefore, we do not discard the constants with respect to b
and σ 2 as we would do when deriving posterior or predictive distributions.

Prior Beliefs and Asset Pricing Models
139
Rearranging, we obtain
p

Mj | R, X

=
 
σ 2−

ν0+T+1
2
+1

Q
× exp

−1
2σ 2

S +

b −	b
′X′X

b −	b


× exp

−1
2σ 2

b −b0
′−1
b −b0

+ ν0c2
0


db dσ 2,
(7.43)
where we denote by Q the expression
||−1/2
 ν0
2
ν0/2

 ν0
2
 cν
0,
by 	b the least-squares estimate of b, we use the following result from linear
regression algebra:

R −Xb
′
R −Xb

=

R −X	b
′
R −X	b

+

b −	b
′X′X

b −	b

,
and we denote S =

R −X	b
′
R −X	b

.
Next, we combine the two quadratic forms in (7.43), involving b to get

b −b
∗′
−1 + X′X

b −b
∗
+
	b −b0
′
 +

X′X
−1−1	b −b0

(7.44)
where b
∗=

−1 + X′X
−1
−1b0 +

X′X
−1	b

.
It is easy now to recognize the kernel of a normal density with mean b
∗
and covariance σ 2M−1, where M =

−1 +

X′X

. The density integrates
to 1 and we are left with
p

Mj | R, X

= Q|M|1/2
 
σ 2−

ν+T
2 +1

× exp

−1
σ 2

R −X	b
′
R −X	b

× exp

−1
σ 2
	b −b0
′
 +

X′X
−1−1	b −b0

+ ν0c2
0

dσ 2.
(7.45)

140
BAYESIAN METHODS IN FINANCE
Recognizing the kernel of an inverse χ 2 distribution above, we finally obtain
the posterior probability of model j:
p

Mj | R, X

=
 ν0
2
ν0/2
 ν0+T
2

 ν0
2
 ν0+T
2
(ν0+T)/2 cν0
0 |M|1/2||−1/2
×

R −X	b
′
R −X	b

+
	b −b0
′
 +

X′X
−1−1	b −b0

+ ν0c2
0
−(ν+T)/2 .
(7.46)

CHAPTER8
The Black-Litterman Portfolio
Selection Framework
I
n the early 1990s, the Quantitative Resources Group at Goldman Sachs
proposed a model for portfolio selection (Black and Litterman, 1991,
1992). This model, popularly known as the Black-Litterman (BL) model, has
become the single most prominent application of the Bayesian methodology
to portfolio selection. Its appeal to practitioners because:
■Portfolio managers specify views on the expected returns on as many
or as few assets as they desire. Classical mean-variance optimization
requires that estimates for the means and (co)variances of all assets in
the investment universe be provided. Given the number of securities
available for investment, this task is impractical—portfolio managers
typically have knowledge and expertise to provide reliable forecasts of
the returns of only a few assets. This is arguably one of the major
reasons why portfolio managers opt out of mean-variance optimiza-
tion in favor of heuristic (nonquantitative) allocation schemes. The
BL model provides an easy to employ mechanism for incorporat-
ing the views of qualitative asset managers into the mean-variance
problem.
■Corner allocations in which only a few assets are assigned non-
zero weights are avoided. As explained in Chapter 6, traditional
mean-variance optimization is haunted by the problem of unrealis-
tic asset weights. The sample means and (co)variances are often plugged
in as inputs into the mean-variance optimizer, which overweights secu-
rities with large expected returns and low standard deviations and
underweights those with low expected returns and high standard devia-
tions. Therefore, large estimation errors in the inputs are automatically
propagated through to portfolio allocations. The Bayesian approach to
portfolio selection, and in particular the BL model, takes into account
the uncertainty in estimation.
141

142
BAYESIAN METHODS IN FINANCE
■If no views are expressed on given securities’ expected returns, these are
centered on the equilibrium expected returns. Bayesian methodology
is commonly criticized for the ‘‘arbitrariness’’ involved in the prior
parameters choice. The BL framework helps fend off this criticism by
using an asset pricing model as a reference point. The CAPM provides
the ‘‘center of gravity’’ for expected returns.
In Chapter 7, we discussed a related framework that incorporated
various degrees of confidence in the validity of an asset pricing model into
the investor’s prior beliefs. The BL model goes a step further and offers
the investor the opportunity to specify beliefs (views) exogenous to the
asset pricing model. At its core lies the recognition that an investor, who
is market-neutral with respect to all securities in his (or her) investment
universe, will make the rational choice of holding the market portfolio.
Only when he is more bullish or bearish than the market with respect to
a given security and/or he believes some relative mispricing exists in the
market, will his portfolio holdings differ from the market holdings.
Our first task in this chapter is a step-by-step description of the BL
methodology. Then we show how trading strategies could be integrated
into BL framework and how to translate the BL framework to an active
return-active risk setting. Finally, since the covariance matrix of asset returns
is an important input into the BL model, we briefly review Goldman Sachs’
approach to its estimation. In Chapter 13, we discuss two extensions of
the BL model that represent mechanisms for introducing distributional
assumptions other than normality into the portfolio allocation framework,
namely Meucci (2006) and Giacometti, Bertocchi, Rachev, and Fabozzi
(2007).
PRELIMINARIES
We now lay the groundwork for the discussion of the BL model and explain
its core inputs.
Equilibrium Returns
One of the basic assumptions of the BL model is that unless an investor has
specific views on securities, the securities’ expected returns are consistent
with market equilibrium returns. Therefore, an investor with no particular
views holds the market portfolio.
The expected equilibrium risk premiums, serving the role of the neutral
views, may be interpreted in either of two equivalent ways—as the expected

The Black-Litterman Portfolio Selection Framework
143
risk premiums produced by an equilibrium asset pricing model, such as
the capital asset pricing model (CAPM), or as the carrier of the prevailing
information on the capital markets (which are assumed to be in equilibrium).
The equivalence derives from the fact that, in equilibrium, all investors hold
the market portfolio combined with cash (or leverage). Let’s look at these
two interpretations within the context of the CAPM.
Suppose the asset universe (the market portfolio) consists of N assets.
Denote by  the N × 1 vector of equilibrium risk premiums:
 = R −Rf1,
where R is the N × 1 vector of asset returns, 1 is an N × 1 vector of ones,
and Rf is the risk-free rate.
Denote by ωeq the market-capitalization weights of the market portfolio.
Assuming the CAPM holds,  is given by1
 = β

RM −Rf

,
(8.1)
where:
RM −Rf is the market risk premium.
β = cov(R, R′ωeq)/σ 2
M is the N × 1 vector of asset betas, where R′ωeq is
the market return.
R is the N × 1 vector of asset returns.
ωeq is the N × 1 vector of market capitalization weights.
σ 2
M is the variance of the market return, i.e., σ 2
M = ω′
eqωeq, where  is
the asset return covariance matrix.2
Denote by δ the expression

RM −Rf

/σ 2
M. The vector of equilibrium
risk premiums, , can then be written as
 = δωeq.
(8.2)
We could rearrange (8.2) to obtain the expression
ωeq = 1
δ −1.
(8.3)
This is in fact the vector of market capitalization positions (unnor-
malized weights) and δ takes on the interpretation of the risk-aversion
1See Satchell and Scowcroft (2000) for this derivation.
2The covariance matrix, , is estimated outside of the BL model. We discuss its
estimation later in the chapter.

144
BAYESIAN METHODS IN FINANCE
parameter, A, from Chapter 6. The expression for market capitalization
weights given in (6.5) in Chapter 6 is obtained by dividing the right-hand
side of (8.3) by the sum of the portfolio positions (δ will cancel out in that
case).
The equivalent approach to the derivation of the equilibrium risk
premiums relies on the assumption that capital markets are in equilibrium
and clear. Solving the unconstrained portfolio problem from Chapter 6, 
can be obtained (backed out) from (6.5) in that chapter, where the optimal
weights are regarded as the market capitalization weights, ωeq.
Investor Views
Investors’ views are expressed as deviations from the equilibrium returns,
. Suppose the investment universe consists of four assets, A, B, C, and D.
An absolute view could be formulated as ‘‘next-period’s expected returns
of assets A and B are 7.4% and 5.5%.’’ A relative view is expressed
as ‘‘C will outperform A, B, and D by 2% next period.’’ It is easy to
see why relative views are likely to be the predominant type, especially
among qualitatively oriented portfolio managers. Many portfolio strate-
gies produce relative rankings of securities (securities are expected to
underperform/outperform other securities) rather than absolute expected
returns.
Views are expressed by means of the returns on portfolios com-
posed of the securities involved in the respective views. For example,
the absolute views above correspond to two view portfolios, one long
in asset A and the another long in asset B. Relative views are usually
expressed by means of zero-investment view portfolios, which are long in
the security expected to outperform and short in the security expected to
underperform.
Distributional Assumptions
In the following presentation, we outline the BL model’s original distribu-
tional assumptions. We assume that asset returns, R, follow a multivariate
normal distribution with mean vector µ and covariance matrix .
Market Information
Although we expect the market to be on average in
equilibrium, at any given point in time this equilibrium could be perturbed
by shocks; for example, shocks related to the arrival of information relevant
for the pricing of securities. Therefore, we write
µ =  + ϵ,

The Black-Litterman Portfolio Selection Framework
145
where the N × 1 vector ϵ embodies the perturbations to the equilibrium
and is assumed to have a multivariate normal distribution, so that the prior
distribution on µ is given by
µ ∼N

, τ

.
(8.4)
The prior covariance matrix of the mean is simply the scaled covariance
matrix of the sampling distribution. We can interpret the scale parameter, τ,
as reflecting the investor’s uncertainty that the CAPM holds. Alternatively,
τ represents the uncertainty in the accuracy with which  is estimated. A
small value of τ corresponds to a high confidence in the equilibrium return
estimates.3
Subjective Views
Suppose that an investor expresses K views and denote
the K × N matrix of view portfolios by P. Each row of P represents a
view portfolio, where an element of P is nonzero if the respective asset is
involved in the view and zero otherwise. Based on our earlier discussion,
when a relative view is expressed, the elements of a row sum up to zero;
when an absolute view is expressed, the corresponding row consists of a 1
in the place of asset C and zeros everywhere else—the sum of its elements is
1. Suppose that the investment universe consists of four assets, A, B, C, and
D, and consider the two absolute and one relative views above. The matrix
P becomes then the 3 × 4 matrix


1
0
0
0
0
1
0
0
−1/3 −1/3 1 −1/3

,
where equal weighting is used to form the third view portfolio (market-
capitalization weighting scheme can also be employed). The K × 1 vector
of expected returns on the view portfolios is then given by Pµ. Assuming it
is normally distributed, we obtain the distributional assumption regarding
the investor’s subjective views:
Pµ ∼N(Q, ).
(8.5)
3In Chapter 7, uncertainty about the validity of an asset pricing relationship
was represented with the help of a prior distribution on the intercept α in Ri =
α + βRM + ϵi, centered around zero (Ri and RM are excess returns). The prior
relation in (8.4) is an equivalent way to express the same source of uncertainty.
To see this, rewrite (8.4) as µ − ∼N

0, τ

and recognize that µ − is the
expected superior return (mispricing), α.

146
BAYESIAN METHODS IN FINANCE
The vector Q contains the investor’s views on the securities’ expected
returns. Continuing with our example,
Q =


7.4
5.5
2

.
The degree of confidence an investor has in his views is reflected in the
diagonal elements, ωkk, k = 1, . . . , K, of the K × K prior covariance matrix
. Its off-diagonal elements are usually set equal to zero, since views are
assumed to be uncorrelated. The value of ωkk is inversely proportional to
the strength of the investor’s confidence in the kth view.
COMBINING MARKET EQUILIBRIUM AND
INVESTOR VIEWS
Bayes’ theorem (see Chapter 2) is applied to combine the two sources of
information represented by the ‘‘objective information’’ embodied in (8.4)
and the subjective information in (8.5).
The posterior distribution of expected returns, µ, is normal with mean
and covariance given, respectively, by
M =

(τ)−1 + P′−1P
−1 
(τ)−1  + P′−1Q

=

(τ)−1 + P′−1P
−1 
(τ)−1  + P′−1P ˆµ

,
(8.6)
where ˆµ is the estimate of expected returns implied by the views, ˆµ =
(P′P)−1P′Q, and
V =

(τ)−1 + P′−1P
−1 .
(8.7)
When no views are expressed (P is a matrix consisting of zeros only), the
posterior estimate of the expected return becomes M = ; when the views
uncertainty (i.e., ωkk, k = 1, . . . , K) is very large, M is dominated by  (and
in the limit is equal to it). In those cases, a rational investor ends up holding
the market portfolio and the riskless asset. The efficient frontier representing
the investor’s risk-return trade-off, given his risk preferences, will simply
be the Markowitz efficient frontier resulting from classical mean-variance
optimization.
Observe that the posterior mean in (8.6) is the usual shrinkage estimator.
The lower investor’s confidence in his views, the closer expected returns are
to the ones implied by market equilibrium; conversely, the higher confidence

The Black-Litterman Portfolio Selection Framework
147
in subjective views causes expected returns to tilt away from equilibrium
expected returns.
The posterior covariance matrix in (8.7) is an expression involving
the prior precisions (inverse covariance matrices) of the expected returns
implied by market equilibrium and the expected returns implied by the
views (similar to the expression for the posterior covariance in (4.17) in
Chapter 4).
THE CHOICE OF τ AND ω
The choices of τ and ωii are the major roadblocks in practical applications
of the BL model—no guideline exists for the selection of their values. Since
uncertainty about the expected returns is less than the variability of returns
themselves, τ is usually set to a value less than 1. Black and Litterman (1992)
advocate a value close to 0, while Satchell and Scowcroft (2000) choose
τ = 1. Suppose that we take sequentially larger and larger samples of
data. We would expect that the larger the dataset, the less influential the
impact of the perturbations, ϵ, is and the more accurate our estimate of 
becomes—the value of τ decreases. Therefore, we could interpret τ as the
remaining uncertainty in the estimate of , given a sample of length T, and
set τ = 1/T. For example, a sample of length 10 years would correspond to
τ = 1/10.
To minimize the subjectivity in τ’s choice, a different approach would
be to calibrate τ from historical return data. Consider the distributional
assumption in (8.4). Simple statistical arguments show that the distribution
of the vector µ − is
µ − ∼N (0, τ) ,
(8.8)
where  is the covariance matrix of returns computed separately. To obtain
τ, we estimate the covariance matrix, V, of µ − using observed return
data and solve the equation4
||V|| = τ ||||.
(8.9)
4The norm of a p × q matrix, A, denoted by ||A|| is a number associated with A.
Different kinds of matrix norms exist. The simplest one is the so-called Euclidean
norm, also known as Frobenius norm and is simply given by the square root of the
sum of squared elements of A,
||A|| =

a2
11 + a2
12 + ··· + a2
pq.

148
BAYESIAN METHODS IN FINANCE
The matrix V is the covariance matrix of (Rs −s), where:
Rs = 1 × N vector of observed returns on N stocks at time s.
s = 1 × N vector of equilibrium returns on the N stocks at time s,
computed (using (8.2)) over a moving window of certain length;
for example, the length could be 250 days (equivalent to one year),
if daily data are employed.
The diagonal elements of , ωii, could also be computed through a
calibration (backtesting) procedure, which we explain later in the chapter.
Another possible approach is to make a statistical assumption about the
distribution of a view. For example, suppose that the portfolio manager
expresses the view that stock A will outperform stock B by 6% and, in
addition, he can evaluate his confidence that his projection will fall between
5% and 7% at 95%. If we assume that the view is normally distributed and
we treat the interval [5%, 7%] as a confidence interval with a confidence
level of 95%, we could use elementary statistical arguments to derive the
implied standard deviation of 0.5%. Therefore, we could set ωii = (0.5%)2
= 0.25%. This is, in fact, a customary approach to eliciting the parameters
of the prior distributions, as we discussed in Chapter 3.
THE OPTIMAL PORTFOLIO ALLOCATION
As discussed in Chapter 6, solving the investor’s mean-variance optimization
problem requires knowledge of the mean and covariance of the predictive
distribution of (future) excess returns. It can be shown that the mean of the
predictive returns distribution is the same as the posterior mean of expected
returns, while the covariance of the predictive distribution includes a term
reflecting the estimation error. The predictive mean and covariance are,
respectively,
µ = M
and
 =  + V.
(8.10)
The solution to the unconstrained investor’s portfolio problem is then given
by the vector of optimal portfolio positions,
ω∗= 1
A
−1µ.
(8.11)
As shown by He and Litterman (1999), (8.11) can be decomposed into
ω∗=
1
1 + τ

ωeq + P′

.
(8.12)

The Black-Litterman Portfolio Selection Framework
149
where ωeq = 1/A−1 are the market capitalization (equilibrium) positions
(see (8.3)). The elements of the K × 1 vector  represent the weights assigned
to each of the view portfolios.5
What the representation in (8.12) tells us is that the investor’s optimal
portfolio can essentially be viewed as a combination of two portfolios—the
market portfolio and a weighted sum of the view portfolios. In the absence
of particular views on assets’ expected returns, the investor optimally holds
a fraction of the market portfolio

ωeq/(1 + τ)

. The size of this fraction
is inversely proportional to the degree of investor’s skepticism about the
estimates of equilibrium returns (alternatively, about the CAPM).
Illustration: Black-Litterman Optimal Allocation
Next we illustrate the mechanism through which views affect the optimal
portfolio. Our data sample consists of daily returns and market capitaliza-
tions on the eight constituents of the MSCI World Index with the largest
market capitalization (as of the beginning of the sample period): United
Kingdom (UK), United States (US), Japan (JP), France (FR), Germany (DE),
Canada (CA), Switzerland (CH), and Australia (AU). The data span the
period from 1/2/1990 through 12/31/2003. Part A of Exhibit 8.1 contains
the sample covariance matrix of the eight return series, while the equilib-
rium implied expected returns for the eight country indices, as well as their
equilibrium-implied (market-capitalization) weights, are in Part B.
Purely as an illustration, we formulate two views:
■CH will outperform US by 5%.
■JP will return 10% on an annual basis.
The first view is a relative one, while the second view is an absolute
one. Thus, the view matrix, P, and the subjective expected returns vector,
Q, take the form,
P =
	 0 −1 0 0 0 0 1 0
0
0
1 0 0 0 0 0

and
Q =
	 0.05
0.1

,
5The elements of  are given by
 = 1
Aτ−1Q −S−1P

1 + τ ωeq −S−1 1
AP

1 + τ P′τ−1Q,
(8.13)
where S = /τ + P/(1 + τ)P′.

150
BAYESIAN METHODS IN FINANCE
UK
US
JP
FR
DE
CA
CH
AU
UK
0.0246
0.0081
0.0054
0.0204
0.0196
0.0085
0.0161
0.0055
US
0.0228
0.0019
0.0102
0.0121
0.0141
0.0072
0.0017
JP
0.0332
0.0064
0.0070
0.0034
0.0060
0.0079
FR
0.0350
0.0284
0.0110
0.0212
0.0060
DE
0.0438
0.0125
0.0234
0.0075
CA
0.0234
0.0075
0.0049
CH
0.0276
0.0052
A
AU
0.0246
B
0.0179
0.0188
0.0409
0.0214
0.0238
0.0160
0.0174
0.0122
weq
0.09
0.34
0.43
0.03
0.04
0.03
0.02
0.02
Π
EXHIBIT 8.1
MSCI sample and equilibrium-implied information
Note: The covariance and expected return entries are expressed on an annual basis.
Part A contains the covariance matrix of MSCI excess returns. Part B contains the
equilibrium-implied expected returns and market-capitalization weights.
where we use equal weighting of the relative view portfolio. Notice that
the view on JP implies a doubling of its equilibrium-implied expected
return (of 4.9% annually). The equilibrium expected returns imply that US
outperforms CH by 0.14% annually, in contrast to the relative view. In
our computations, we use a coefficient of risk aversion, A, equal to 2.5
and a scale parameter, τ, equal to 0.5. The matrix  reflecting the view
uncertainty is as follows,
 =
	 ω11
0
0
ω22

,
where ωH
11 = 0.0001 or ωL
11 = 0.04 and ω22 = 0.0004.
The subscripts H and L above refer to the high-confidence and
low-confidence cases with respect to the relative view that we consider.
The values of ω11, ωH
22, and ωL
22 are determined using the confidence-interval
argument outlined in our earlier discussion on the choice of τ and . When
we consider the absolute and relative views separately, P, Q, and  are
transformed accordingly.
In Exhibit 8.2 we can observe that since returns are correlated, views
expressed on only several assets would imply changes in the expected
returns on all assets. The mechanism for this propagation of views is

The Black-Litterman Portfolio Selection Framework
151
UK
US
JP
FR
DE
CA
CH
AU
Absolute View
Only
0.0271
0.022
0.0986
0.0324
0.0358
0.0216
0.0278
0.0256
Relative View
Only, High
Confidence
0.0291
–0.0026
0.0492
0.0368
0.0397
0.0068
0.0458
0.0174
Relative
View Only,
Low Confidence
0.0206
0.0136
0.0429
0.0251
0.0277
0.0137
0.0243
0.0135
Both Views
0.0292
0.0175
0.0987
0.0353
0.0388
0.0196
0.0334
0.0263
EXHIBIT 8.2
Views-implied expected returns
Note: The expected return entries are expressed on an annual basis.
the N × K matrix P′−1, which ‘‘maps’’ the K views onto the N secu-
rities through the term P′−1Q. Through this mapping, errors in the
investor’s forecasts of expected returns are spread out over all securities,
thus mitigating estimation error and preventing corner solutions (which
could be the case if only the expected returns on some securities are
adjusted).
Consider the optimal portfolio when only the absolute view on JP is
expressed. The outcome is illustrated in the left-hand side of Exhibit 8.3.
As expected, the portfolio loads on JP (relative to the market capitaliza-
tion weights). Since JP is positively correlated with the rest of the country
indices, their weights decrease proportionately to their market capitaliza-
tions. Notice the adjustment in the whole expected returns vector—the
expected returns on all assets increased, since they are all positively corre-
lated with JP.
We now compare the effect of the high-confidence and low-confidence
relative view on CH and US. See Exhibit 8.4. The optimal portfolio weight
of CH increases at the expense of the weight of US. The impact of the
high-confidence view is dramatic, while the low-confidence view has a more
moderate effect. In both cases, only the weights of the indexes involved
in the relative view change; the remaining weights are preserved at the
equilibrium values. All components of the vectors of expected returns in the
high-confidence and low-confidence cases are adjusted, as explained above.
Finally, the right-hand side of Exhibit 8.3 depicts the case when
both views are incorporated into the optimal portfolio construction (low

152
BAYESIAN METHODS IN FINANCE
UK
US
JP
FR
DE
CA
CH
AU
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
Market cap weights
BL weights
UK
US
JP
FR
DE
CA
CH
AU
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
Market cap weights
BL weights
EXHIBIT 8.3
Optimal portfolio weights: absolute view and both views together
Note: The plot on the left-hand side corresponds to the absolute view, while the plot
on the right-hand side reflects the joint impact on both the absolute and the relative
view.
UK
US
JP
FR
DE
CA
CH
AU
−1
−0.5
0
0.5
1
1.5
UK
US
JP
FR
DE
CA
CH
AU
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
Market cap weights
BL weights
Market cap weights
BL weights
EXHIBIT 8.4
Optimal portfolio weights: relative view
Note: The plot on the left-hand side corresponds to the high-confidence view, while
the plot on the right-hand side—to the low-confidence view.
confidence is assigned to the relative view). We can clearly see that the
resulting optimal portfolio is a combination of the effects we observed
in the individual cases above. Notice that since we only incorporate two
simple views and all country indices are positively correlated, the alloca-
tions reflecting both views are still very intuitive. This will likely not be
the case in more complicated situations; however, one can still be certain
that the investor’s views are accurately reflected in the optimal portfolio
weights.

The Black-Litterman Portfolio Selection Framework
153
INCORPORATING TRADING STRATEGIES INTO THE
BLACK-LITTERMAN MODEL
Trading strategies can be introduced into the BL framework. The sole
requirement for that is to be able to identify the components of the strategy
with the respective inputs of the BL model. Of course, the trading strategy
is simply a way to formulate the views of the portfolio manager. Let us
consider the momentum strategy example of Fabozzi, Focardi, and Kolm
(2006).
Momentum is the tendency of securities or equity indexes to preserve
their good (poor) performance for a certain period in the future.6 Empirical
findings show that stocks that outperformed (underperformed) the mar-
ket in the past 6 to 12 months continue to do so in the next 3 to 12
months. A cross-sectional momentum strategy would consist in ranking the
securities according to their past performance; then, a long-short portfo-
lio is formed by purchasing the ‘‘winners’’ and selling the ‘‘losers.’’ The
expected view return, Q, is then a scalar, equal to the expected return
on the long-short portfolio. The variance of the view could be deter-
mined through a backtesting procedure, which we explain in the following
paragraphs.
Fabozzi, Focardi, and Kolm (2006) use daily returns of the coun-
try indexes making up the MSCI World Index over a period of 24
years (1980 to 2004). The momentum (long-short) portfolio is con-
structed at a particular point in time, t (hence a ‘‘cross-sectional’’ strategy)
and held for one month. Winners and losers are determined on the
basis of their performance over the past nine months—the quantity
used to rank them is their normalized nine-month return (lagged by one
day):
zt, i = Pt−1, i −Pt−1−189, i
Pt−1−189, iσi
,
(8.14)
where:
Pt−1, i = price of country index i at time t −1.
Pt−1−189, i = price of country index i nine months (approximately, 189
days) before t −1.
σ i = volatility of country index i.
6The momentum phenomenon was first described by Jegadeesh and Titman (1993).
See also Rouwenhorst (1998).

154
BAYESIAN METHODS IN FINANCE
The top half and the bottom half of the country indexes are then
assigned weights, respectively, of
wi = 1
σiκ
and
wi = −1
σiκ .
(8.15)
That is, the view matrix, P, consists of a single row with elements one
of the two quantities above. Weights are dependent on a country indexes’
volatilities in order to avoid corner solutions. The parameter κ is a constant
whose role is to constrain the annual portfolio volatility to a certain level
(20% in the application of Fabozzi, Focardi, and Kolm).
The confidence in the view represented by the cross-sectional momentum
strategy could be determined through backtesting in the following way. For
each period t:
1. Construct the momentum portfolio using (8.14).
2. Hold the portfolio for one month and observe its return, RM,t, over the
holding period.
3. For the same holding period, observe the realized return, RA, t, on the
portfolio of the actual winners and losers.
4. Compute the ‘‘residual’’ return, Et = RM,t −RA,t.
5. Move the performance-evaluation period one month forward and repeat
the steps above.
Then, calculate the variance of the series of residuals, Et, and set
ωii = var(Et).
Fabozzi, Focardi, and Kolm compute the covariance matrix of returns,
, as the daily-returns, geometrically weighted covariance matrix. (See
the discussion later in the chapter on exponential (geometric)-weighting
schemes.)
Finally, the predictive mean and covariance of returns are computed
using (13.27) and the optimal portfolio constructed. Fabozzi, Focardi, and
Kolm use a scale parameter τ equal to 0.1. Exhibits 8.5 and 8.6 present,
respectively, the realized returns and volatilities of the optimized momentum
strategy and the MSCI World Index.
ACTIVE PORTFOLIO MANAGEMENT AND THE
BLACK-LITTERMAN MODEL
A fund manager generates return by undertaking two types of risk—market
risk and active risk. The market exposure comes as a result of the strategic

The Black-Litterman Portfolio Selection Framework
155
Portfolio
Index
Growth of Equity
01/01/85
01/01/80
01/01/90
01/01/95
01/01/00
01/01/05
25
20
15
10
5
0
EXHIBIT 8.5
Realized returns on the optimized momentum strategy and the MSCI
world index
01/01/80
0
2
4
6
8
10
12
14
16
18
20
01/01/85
01/01/90
01/01/95
01/01/00
01/01/05
Portfolio
Volatility (%)
Index
EXHIBIT 8.6
Realized volatilities on the optimized momentum strategy and the
MSCI world index

156
BAYESIAN METHODS IN FINANCE
allocation decision—how the funds available for investment are allocated
among the major asset classes. The active exposure depends on the risks
taken by a portfolio manager relative to the benchmark against which
performance is measured. There are two main reasons why an active
strategy might be capable of generating abnormal returns relative to the
benchmark: benchmark inefficiency and investment constraints. The more
inefficient a benchmark is and the less investment constraints there are, the
greater the opportunity for a skilled manager to achieve active returns.7
Active return is the return on a particular portfolio strategy minus
the return on the benchmark. Active return has two sources—one due to
benchmark exposure (and originating from market movements) and another
due to stock picking (the ‘‘residual return’’). The decomposition is given
by,8
RP,A = RP,R + βP,ARB,
(8.16)
where:
RP, A = active return of portfolio P.
RP, R = residual return on portfolio P.
βP,A = active beta.
RB = benchmark return.
Adjusting the benchmark exposure (the active beta) on a period-by-
period basis is what typically constitutes benchmark timing (‘‘loading’’ on
the benchmark in market upturns and ‘‘unloading’’ in market downturns).
Institutional investors usually do not engage in benchmark timing and
maintain an active beta of close to 1.0 relative to the benchmark. Then, all
active return comes from the skill of the portfolio manager at stock-picking
and coincides with the residual return; that is, the optimal portfolio is
market-neutral. We assume this is the case below and use ‘‘active return’’ to
refer to both active and residual return. The expected active return is called
alpha, while the standard deviation of the active return is the active risk,
commonly referred to as tracking error.
In this section, our focus is active portfolio management. We discuss
a modification of the BL model allowing an active manager to incorporate
his (or her) views (either qualitative or quantitative) into the allocation
process.
7See Winkelmann (2004).
8See, for example, Grinold and Kahn (1999). The decomposition of active return
into its two components is obtained by regressing it against the return on the
benchmark.

The Black-Litterman Portfolio Selection Framework
157
Views on Alpha and the Black-Litterman Model
The setup for the BL model modified for the active-returns case essentially
mirrors the setup for the ‘‘total-return’’ BL model discussed earlier. We
adopt the same distributional assumption for active returns as for total
returns earlier in the chapter,
RA ∼N

α, A

.
The source of neutral, equilibrium information is represented by a
normal distribution on alpha centered around zero. That is, the residual
return on the benchmark is not systematically different from zero unless
the benchmark is inefficient (see Chapter 9 for more details on market
efficiency),
α ∼N(0, τA),
(8.17)
where A is the covariance matrix of active returns, and the scaling factor
τ could be interpreted as the confidence in the benchmark’s efficiency. The
active manager expresses views on the assets’ alphas if he believes he could
outperform the benchmark. These views are described in distributional
terms by
Pα ∼N(Q, ),
(8.18)
where P, Q, and  take on the same interpretations as described previously.
When a manager is able to specify a level of confidence in his views, the
values of the diagonal elements of , ωii, can be computed as explained ear-
lier in the chapter. Herold (2003) suggests that fundamental managers, who
do not have quantitative insight (but rather simply express a bullish/bearish
view on an asset or a group of assets), set ωii equal to the respective diago-
nal element of the matrix PAP′.9 Since views can be represented by view
portfolios, the diagonal elements of PAP′ are, in fact, the tracking errors
of these view portfolios.
The posterior moments of α’s distribution, as well as the predictive
moments of the distribution of next-period’s active returns, are as given
in (8.6), (8.7), and (13.27) (with the obvious change in notation). The
unconstrained portfolio selection problem is expressed in terms of the
portfolio’s predictive alpha and tracking error,
max
ωA
	
ω′
Aα −A
2 ω′
AAωA

,
(8.19)
9The approach by He and Litterman (1999) is similar. They choose to calibrate the
ratio ωii/τ by setting it equal to pip′
i, where pi is the ith row of the P matrix.

158
BAYESIAN METHODS IN FINANCE
where A is the risk-aversion coefficient, ωA is the vector of active portfolio
weights, and α and A are, respectively, the predictive mean and covari-
ance of the active returns. Active managers are usually constrained as to
the maximum tracking error they can assume. Then, the active portfolio
selection problem can be represented as a maximization of ω′
Aα, subject to
the tracking error constraint as explained in Chapter 6.
Translating a Qualitative View into a Forecast for Alpha
To translate a qualitative view into a forecast value for alpha, a portfolio
manager could employ two fundamental concepts from the field of active
asset management—the information ratio and the information coefficient.10
The information ratio (IR) is a measure of the investment value of active
strategies, representing the amount of active return per unit of active risk.
The IR of a portfolio p is defined as
IRp = αp
ψp
,
(8.20)
where αp = ω′
AαωA is the portfolio’s alpha and ψp = ω′
AAω′
A is the portfo-
lio’s active risk. The IR is, then, a natural tool to employ in the selection of
portfolio managers. The information coefficient (IC) is defined as the corre-
lation between the forecast and the realized active return, and is considered
an indicator of the portfolio manager’s skill.
Grinold (1989) and Grinold and Kahn (1999) show that the information
ratio and the information coefficient are related through the following
(approximate) relationship:
IR ≈IC ×
√
BR,
(8.21)
where BR (breadth) is the number of independent, active bets made by
the portfolio manager in a period. We assume that IC is the same for all
forecasts. Since each view portfolio represents one active bet, BR = 1 and
IR = IC in our discussion. We obtain the forecast value of α, in fact, the
mean vector, Q, as
α = IC × ψ,
(8.22)
where ψ = diag() = diag(PP′) is the vector of tracking errors of the view
portfolios. A higher degree of uncertainty in the expressed views logically
corresponds to a lower value of the information coefficient, IC; therefore,
10See also Grinold and Kahn (1999).

The Black-Litterman Portfolio Selection Framework
159
IC could be manually adjusted to reflect uncertainty (as in Herold (2003)),
although, certainly, this procedure would lack mathematical rigor.
COVARIANCE MATRIX ESTIMATION
Variance (covariance matrix) is the input traditionally used as a measure of
risk in portfolio optimization, and financial practice in general. As expected
returns, the covariance matrix needs to be estimated from historical data.
It has been argued (Best and Grauer, 1991, 1992) that estimation errors
in expected returns affect mean-variance optimization to a much larger
degree than errors in the covariance matrix, while errors in variances are
about twice as important as errors in covariances. Nevertheless, the search
for a better estimate of the covariance matrix goes on. In this section,
we discuss some covariance matrix estimation techniques. (See also our
brief discussion in Chapter 6 on the shrinkage estimator of the covariance
matrix.)
The simplest approach to estimation of the covariance matrix of excess
returns, , relies on computing the sample estimates of variances and
covariances at time T, given, respectively, by

varT (rit) ≡σ T
ii =
T
t=0 r2
it
t −1
(8.23)
and

covT 
rit, rjt

≡σ T
ij =
T
t=0 ritrjt
t −1
,
(8.24)
where rit is the return on asset i at time t. We assume that the mean of each
return series is subtracted from the returns, so that they have a mean of
zero.
The major shortcoming of the estimators above is that they assign
equal weights to all return observations in the sample. This precludes the
possibility to account for the fact that variances and covariances might have
changed over time and data from the distant past might be less relevant
than more recent data.11
One way to take into account time variation is to compute variances
(covariances) as weighted sums of squared returns (products of returns). The
11There is an extensive literature documenting the time variability of volatilities and
correlations. See our discussions in Chapters 10, 11, and 12.

160
BAYESIAN METHODS IN FINANCE
expressions for the weighted estimators of the variances and covariances of
returns are, respectively,

varT (ri) ≡σ T
ii =
T
t=1 wtr2
i,t
T
t=1 wt
(8.25)
and

covT 
ri, rj

≡σ T
ij =
T
t=1 wtritrjt
T
t=1 wt
.
(8.26)
Notice that when weights are equal, (8.23) and (8.24) are the same as
(8.25) and (8.26). Generally, the weights reflect the length of return history
to which an investor attaches relatively greater importance. For example,
when daily data are used in estimating the covariance matrix, it is not
uncommon to weigh more heavily data that pertain to the most recent
month than data from, say, one year ago. That is, a weighting scheme with
decaying (declining with time) weights is employed. A term often used in
this context is half-life. A half-life of k periods means that an observation
from k periods ago receives half of the weight of an observation in the
current period. Alternatively, we talk of decay rate, defined as d ≡1 −
wt−1/wt. The decay rate d and the half-life k are related by
dk = 0.5.
For example, the decay rate such that data three months (36 business
days, if daily data is used) ago is given twice as little weight as current data
is approximately 0.98. That is, an observation at day t −1 receives 98% of
the weight of the following observation (at day t) for all t.12
Various refinements of volatility estimation have been developed and
applied in empirical work. We discuss generalized autoregressive het-
eroskedasticity (GARCH) and stochastic volatility models in chapters 10,
11, and 12. Factor models of returns are widely used to both provide
economic intuition about common forces driving expected returns, and to
12It is clear from (8.25) and (8.26) that the decay rate plays a key part in the
estimation of the return variances and covariances. Therefore, it is necessary to
select a decay rate that is ‘‘best’’ or optimal in some sense. From a statistical
viewpoint, the optimal rate could be the one that maximizes the likelihood function
of returns.

The Black-Litterman Portfolio Selection Framework
161
reduce the dimension of the problem of covariance matrix estimation.13 (See
Chapter 14 for more details on Bayesian factor model estimation.)
In recent years, a tremendous push has been made for employing
measures of risk other than variance, as well as higher moments, in portfolio
risk modeling. See Chapter 13 for a brief outline of these alternative risk
measures, as well as a discussion of some of advanced portfolio techniques.
SUMMARY
The Black-Litterman model allows for a smooth and elegant integration
of investors’ views about the expected returns of assets into the portfolio
optimization process. The basic idea of the model is that an asset’s expected
return should be consistent with market equilibrium unless an investor holds
views on it. Therefore, the asset allocations induced from the views repre-
sent tilts away from the neutral, equilibrium-implied, market-capitalization
weights. In the absence of views, the optimal portfolio is the market
portfolio.
We consider two extensions to the Black-Litterman model. The first
extension incorporates a momentum strategy; the second extension reflects
views on the expected active returns (alphas).
13Given N assets, the covariance matrix of returns contains N(N + 1)/2 distinct
elements that need to be estimated. A factor model reduces the number of unknown
elements to K(K + 1)/2 + N, where K is the number of factors in the model. The first
term gives the factor covariance matrix and the second one, the vector of specific
variances. In practical applications, K is a much smaller number than N.

CHAPTER9
Market Efficiency and Return
Predictability
M
arket efficiency is one of the paradigms of modern finance that has
created the most vibrant debate and prolific literature since Fama
(1970) coined the Efficient Market Hypothesis (EMH). Without doubt,
an engaging and controversial aspect of the debate is the presence of
predictable components in asset returns (or lack thereof). The most intuitive
implication of return predictability for asset allocation decisions is the ability
to ‘‘time’’ the market—buy assets when the market is up and sell assets
when it is down. The presence of return predictability also affects the way
return variance scales with the investment horizon. Suppose that returns are
negatively serially correlated—that is, a high return today is followed by a
low return tomorrow. We say that the daily return exhibits mean-reversion.
The variance of long-horizon returns is then smaller than the daily variance
multiplied by the horizon. A buy-and-hold investor would find a long-term
investment more attractive than a short-term one. The opposite is true
when returns are positively serially correlated (high return today is followed
by a high return tomorrow). In general, whether an investor decides to
pursue a passive or an active strategy within a certain asset class depends
on his belief that the market for this asset class is efficient. In an efficient
market, strategies designed to outperform a broad-based market index
cannot achieve consistently superior returns, after adjusting for risk and
transaction costs.
According to the EMH, the market is efficient if asset prices reflect
all available information at all times.1 This requirement is cast in terms
1Fama(1991) points out a more realistic version of this strong condition. In deter-
mining the amount of information that prices reflect, one takes into account the
trade-off between the costs of acquiring the information and the profits that could
be made from acting on it.
162

Market Efficiency and Return Predictability
163
of expected asset returns—random variables which adjust in response to
changes in the available information. Fama (1970) classified the efficiency
of a market into three forms, depending on the scope of information
reflected in prices: weak form, semistrong form, and strong form. Weak
efficiency means that past prices and trading information are incorporated
into asset prices and current price changes cannot be predicted from past
changes. The semistrong efficiency requires that prices reflect all publicly
available information. Finally, a market is strong efficient if prices reflect all
information, whether or not it is publicly available.
Tests of weak-form efficiency have the most controversial implications.
While early tests (up to the early 1980s) considered only the forecast
power of past returns, more recent studies focus on the predictive ability
of variables such as dividend yield (D/P), book value to market value ratio
(B/M), earnings-to-price ratio (E/P) or interest rates. Since predictability of
returns implies that the expected asset returns vary through time, these
tests are time-series tests. It is clear that expected returns play a very
important role in reaching conclusions about the presence and amount of
predictability. Expected returns are the ‘‘normal’’ returns against which
abnormal performance is gauged. Therefore, since expected return is the
return predicted from a pricing model, each test of market efficiency is in
fact a joint test of efficiency and the assumed pricing model. If we find that
returns are predictable, is this evidence against efficiency or evidence against
the validity of the pricing model? This so-called ‘‘joint hypothesis problem’’
makes it impossible to unequivocally prove or disprove the EMH. The
cross-sectional tests of predictability are tests on the validity of asset-pricing
models, such as the capital asset pricing model (CAPM) and the arbitrage
pricing theory (APT).
Some commonly found results are that past returns might help explain as
much as 40% of the variability of long-horizon (2- to 10-year) stock returns.
Predictive variables such as D/P and E/P also have long-horizon predictive
power, explaining around 25% of the variability of two- to five-year returns.
The overall evidence is that, after a shock, stock returns tend to return slowly
to their preshock levels, so that they exhibit mean-reversion.2
Both the time-series and the cross-sectional predictability tests are per-
formed with the help of regression analysis. For example, in time-series tests,
individual asset returns or portfolio returns are regressed on past returns
or on predictor variables to find out what their predictable component is.
Tests on pricing models typically employ a two-pass regression, which we
briefly review in this chapter.
2See Fama (1991) for a review of the literature on efficiency testing and predictability,
in the frequentist setting.

164
BAYESIAN METHODS IN FINANCE
Suppose that, based on regression evidence, a quantitative portfolio
manager designs a strategy that ‘‘beats’’ the market, with projected return,
after transaction costs, is 1.5%. Given that the regression coefficients are
estimated with error, how much confidence should the manager place on
the projection?
In this chapter, we offer the Bayesian perspective on testing for market
efficiency. We start with a brief discussion of a ‘‘classical’’ test of the
CAPM, and then move on to Bayesian tests of asset pricing models. Finally,
we discuss return predictability in the presence of uncertainty.
TESTS OF MEAN-VARIANCE EFFICIENCY
In Chapter 7, we saw that the empirical analogues of the CAPM and the
APT are given, respectively, by
Ri = α + βMRM + ϵi
(9.1)
and
Ri = α + β1f 1 + · · · + βKf K + ϵi
(9.2)
for i = 1, . . . , N, where: Ri = T × 1 vector of excess returns on asset i.
RM = T × 1 vector of excess returns on the
market portfolio.
f j = T × 1 vector of excess returns on risk
factor j.
βM = sensitivity of asset i’s return to the market
risk factor.
βj = sensitivity of asset i’s return to the jth risk
factor.
ϵi = T × 1 vector of specific returns on asset i.
α = intercept.
For the CAPM and the APT to hold, the intercept, α, in (9.1) and (9.2) must
be zero.
The classical tests of the CAPM and the APT are typically based on a
two-stage procedure. Here we will consider the tests of the CAPM. Tests
of the APT have a similar methodology. In the first stage, an estimate of
the sensitivity (beta) to the market risk factor is obtained for each asset.
For example, Fama and MacBeth (1973) propose that the stock beta be
estimated using a time-series regression of asset returns on the market

Market Efficiency and Return Predictability
165
portfolio. The beta represents the market risk of an asset (equivalently,
the contribution of an asset to the risk of the market portfolio). Since the
CAPM implies that the asset’s expected return is linear in beta, in the second
stage, a cross-sectional regression is run to find out if the betas explain the
variability in expected returns across assets, at a given point in time:3
Rt = b0 + b1β + ϵt,
(9.3)
where: Rt = N × 1 vector of excess asset returns at time t.
β = N × 1 vector of asset betas.
ϵt = N × 1 vector of asset specific returns at time t.
b0, b1 = parameters to be estimated.
The main implications of the CAPM that we can test are:
■The intercept, b0, in the cross-sectional regression is zero.
■The regression coefficient, b1, is equal to the market risk premium
(market excess return), RM.
A likelihood-ratio test is usually employed to test the first implication and
the hypothesis that b0 = 0 is most often rejected.
However, inference using classical hypothesis tests suffers from the
so-called ‘‘errors-in-variables’’ problem: The estimated rather than the true
values of the regression coefficients are used in the tests, potentially leading to
wrong inferences (conclusions). Moreover, the interpretation of the p-value
from a hypothesis test is somewhat counterintuitive. The p-value certainly
does not give the probability that b0 = 0, which is the information one would
really want to have. The Bayesian methodology deals with the problem of
uncertainty in the estimates of the regression parameters, and allows one to
compute the posterior probability of the hypothesis that b0 = 0.
Throughout our discussion of the CAPM tests, we refer often to the
‘‘market’’ or the ‘‘market portfolio.’’ A broad-based index, such as the
S&PII500 or the NYSE Composite Index, represents the market portfolio
in most of the empirical tests of the CAPM. The market portfolio in reality
is much broader in scope and includes global equity, as well as global bonds
and currencies. The benchmark portfolio used for testing the CAPM is,
thus, only an imperfect proxy for the unobservable market portfolio, and
objections can be raised about the validity of CAPM tests. This was one
3See Chapter 14 for a discussion of the fundamental multifactor model estimation,
which makes use of the Fama-MacBeth regressions.

166
BAYESIAN METHODS IN FINANCE
of the points of the famous CAPM critique by Roll (1977): If the market
portfolio is misspecified, the validity of the CAPM will be rejected; if the
market portfolio is correctly specified but the CAPM is wrong, its validity
will be rejected again. Therefore, is the CAPM testable at all?
It is easy to show that, since the CAPM is an equilibrium pricing model,
its pricing relationship,
E

Ri

= βiE(RM),
in fact says that ‘‘the market portfolio is mean-variance efficient’’; that is,
the market portfolio minimizes risk for a given level of expected return.
Therefore, an alternative way to test the implication of the CAPM is to
test whether the portfolio chosen to represent the market portfolio (i.e., the
proxy for the market portfolio) is ex ante efficient.4
In addition to dealing with parameter uncertainty, the Bayesian method-
ology offers another advantage. Suppose we are not interested in the rather
restrictive conclusion of a classical hypothesis test (reject or fail to reject the
hypothesis of mean-variance efficiency). Instead, we would prefer to explore
the degree of market inefficiency and its economic significance. (We will see
a way to do this within a Bayesian framework in this chapter.)
We could divide into two categories the Bayesian empirical tests of
mean-variance efficiency. The first category focuses on the intercepts in
(9.1). Since the hypothesis of efficiency of the market portfolio is analogous
to the hypothesis that there is zero mispricing in the model, we are in
fact interested in testing the same restriction, whose impact on portfolio
selection we explored in Chapter 7. These tests rely on the computation of a
posterior odds ratio to test the null hypothesis of mean-variance efficiency.5
We briefly discussed the posterior odds ratio approach to hypothesis testing
in Chapter 3. Tests in the second category are based on the computation of
the posterior distributions of measures of portfolio inefficiency. We discuss
these next.6
4Ex ante efficiency refers to mean-variance efficiency based on expected returns
and covariances. Contrast this with ex post efficiency, which is based on realized
(observed) returns. Since the CAPM is an equilibrium model of returns, we focus
on the ex ante efficiency of the market portfolio in testing it. An ex ante inefficient
benchmark portfolio shows a potential for an active portfolio manager to achieve
superior returns. Ex post, we are able to assess the contribution of a manager’s
active strategy to his performance. See, for example, Baks, Metrick, and Wachter
(2001) and Busse and Irvine (2006).
5See Harvey and Zhou (1990).
6Our discussion is based on Kandel, McCulloch, and Stambaugh (1987) and Wang
(1998).

Market Efficiency and Return Predictability
167
INEFFICIENCY MEASURES IN TESTING THE CAPM
Construction of the inefficiency measure for a certain benchmark portfolio
involves a comparison of that portfolio with a portfolio lying on the efficient
frontier (see Chapter 6). Implicit in building the efficient frontier is the choice
of risky assets. Different sets of risky assets give rise to different efficient
frontiers. Therefore, a robust test would require that the set of assets used
to construct the efficient frontier be widely diversified.
Suppose we are interested in testing the efficiency of portfolio p.
Denote the N × 1 vector of risky asset excess returns at time t by Rt =

R1, t, . . . , RN, t

. Portfolio p is one of the N risky assets. It is common
to select portfolios to represent the N risky assets for the purpose of
diversification mentioned already. Consider, for example, the size effect—an
‘‘anomaly’’ of asset return behavior which was historically uncovered in tests
of the CAPM: Firm size (market capitalization) helps to explain variations
in average stock returns beyond market betas—small stocks have higher
average returns than large stocks. Then firm size provides a criterion for
sorting stocks into portfolios. Another sorting criterion is the ratio of firms’
book value to market value.7 Our goal is to construct the efficient frontier
based on the N assets and then use one of the efficient portfolios to calculate
the measure of inefficiency for portfolio p.
Let’s first look at the case of no investment (holding) restrictions.
Denote by x the efficient portfolio with the same variance as p, σ 2
p = σ 2
x .
Then, µp < µx, if p is inefficient; and µp = µx, if p is efficient. The difference
between the expected returns of p and x can be interpreted as the expected
loss from holding the inefficient portfolio, p, instead of the efficient portfolio,
x, with the same risk as p. An intuitive measure of the inefficiency of p is
then8
 = µx −µp.
(9.4)
Better still, we could examine the difference between the risk-adjusted
returns:
R = µx
σx
−µp
σp
,
(9.5)
7See, for example, Fama and French (1992).
8There are other inefficiency measures, treated in the Bayesian literature, with roots
in the classical (frequentist) analysis. For example, one measure is based on the
maximum correlation ρ between p and an efficient portfolio with the same expected
return. If p is efficient, the maximum correlation, ρ, is one. Otherwise, ρ < 1. The
loss due to inefficiency of p is measured in terms of the ratio of standard deviations
of the two portfolios with equal means. See Kandel, McCulloch, and Stambaugh
(1987) and Harvey and Zhou (1990).

168
BAYESIAN METHODS IN FINANCE
where x is the portfolio with the best risk-return trade-off—the portfolio
with the maximal Sharpe ratio (see our discussion in Chapter 6). Portfolio
p is efficient if and only if  = 0 or R = 0. Therefore, the goal is to
compute and examine the posterior distribution of  (R). Geometrically,
 measures the vertical distance between p and the efficient frontier. Since
x is an efficient portfolio,  cannot be smaller than zero, while R is in
practice always positive. We would be skeptical about the efficiency of p if,
after computing ’s (R’s) distribution, we find that the greater part of its
mass is located far above zero.
Next, we turn to a discussion of the distributional assumptions and the
posterior distributions.
Distributional Assumptions and Posterior Distributions
Let us assume that the N × 1 vector of returns, Rt, t = 1, . . . , T, has a
multivariate normal distribution, independent across t, with mean µ and
covariance matrix . Assume that the parameters of the normal distribution
follow a diffuse prior (Jeffreys’) distribution (see Chapter 3),
µ,  ∼||−(N + 1)/2.
(9.6)
The posterior distributions of µ and  are given, respectively, by
 | R ∼IW

, T −1

(9.7)
and
µ | , R ∼N

µ, 1
T 

,
(9.8)
where R is the T × N matrix of asset return data, the N × 1 vector µ
denotes the sample mean of returns and  is a N × N matrix defined as9
 =
T

t = 1
(Rt −µ)′(Rt −µ).
The inefficiency measure, , is a nonlinear function of µ and . To see
this, consider the steps we need to compute it. First, using the techniques
from Chapter 6, we construct the efficient frontier. Second, we identify
the efficient portfolio, x, with the same risk as p. Finally, we compute the
difference between µx and µp. Therefore, no analytical expression of the
9See Chapter 4, as well as our discussion in Chapter 7.

Market Efficiency and Return Predictability
169
posterior density, p ( | µ, , R), of  is available. However, as discussed
in Chapter 5, we can simulate ’s (exact) posterior distribution by repeating
a large number of times the following algorithm:
1. Draw  from its posterior inverse Wishart distribution in (9.7).
2. Given the draw of , draw µ from its posterior normal distribution in
(9.8).
3. For each pair (µ, ), go through the three steps outlined in the previous
paragraph, and compute the corresponding value of  (R).
We now show how to incorporate investment constraints into the
analysis. The efficient frontier is, naturally, affected by constraints. Sharpe
(1991) shows that the market portfolio might be inefficient when short-sale
constraints are imposed. For example, restrictions on short sales reduce
the possibility to mitigate return variability and to manage risk efficiently.
Typically, a mutual fund’s manager would achieve a given expected return
at the expense of greater risk than a hedge fund’s manager. The average
loss from investing in an inefficient portfolio is then greater for an investor
under short-sale constraints.
Efficiency under Investment Constraints
The inefficiency measure,  (R), is easily adapted to account for investment
constraints. Wang (1998) proposes to modify it, in the case of short-sale
restrictions, as
˜ = max
xi

µx −µp | xi ≥0,
i = 1, . . . , = N

,
(9.9)
where xi, i = 1, . . . , N denotes asset i’s weight in portfolio x.
Consider a different constraint, one that applies to all margin accounts
at brokerage houses. The Federal Reserve Board’s Regulation T sets a 50%
margin requirement—a customer may borrow 50% of the cost of a new
asset position. We can incorporate a constraint reflecting a 50% margin
modifying (9.9) with xi ≥−0.5, i = 1, . . . , i = N.
As shown earlier, efficiency of the benchmark portfolio, p, is equivalent
to ˜ = 0. To compute the posterior distribution of ˜ under the investment
constraints, we follow the exact same steps as for the posterior distribution
of  with one difference: The efficient frontier is constructed subject to
the investment constraints that we would like to reflect. (We perform the
constrained optimization in (9.9) for each pair

µ, 

).
Now, we illustrate the computation of the posterior distribution of R
and analyze the implications for the efficiency of the market portfolio.

170
BAYESIAN METHODS IN FINANCE
Illustration: The Inefficiency Measure, R
The sample in this illustration10 consists of the monthly returns on 26
portfolios. The first 25 of them are the Fama-French portfolios. Stocks
in them are ranked in five brackets according to size (as measured by
market capitalization). Within each size bracket, stocks are ordered in
five categories, according their book-to-market ratio. Thus 25 portfolios
are constructed. The 26th portfolio is the value-weighted NYSE-AMEX
stock portfolio, whose efficiency we are interested in—portfolio p from the
previous section. The return on the one-month T-Bill is used as the risk-free
rate. The sample period starts in January 1995 and ends in December
2005. The histograms in Exhibit 9.1 are based on 1,000 draws from
the distribution of R computed as explained earlier, for the cases of no
investment constraints and of short-sale constraints. The values of R are
annualized, therefore, we can think of the histograms as representing the
annual loss (in terms of risk-adjusted return) from holding the NYSE-AMEX
10
15
20
25
30
35
0
50
100
150
200
250
Inefficiency
without short sale
constraints
Inefficiency
with short
sale
constraints
EXHIBIT 9.1
Distribution of the inefficiency measure, R
Note: The histograms are based on 1,000 draws from the distribution of R. The
values of R are annualized.
10The illustration is based on the illustrations in Kandel, McCulloch, and Stambaugh
(1987) and Wang (1998).

Market Efficiency and Return Predictability
171
portfolio, instead of the efficient portfolio. As expected, the loss under
short-sale constraints is greater than under no investment constraints.
TESTING THE APT
In the previous section, we discussed how to assess the efficiency of a
portfolio in terms of an inefficiency measure, R. We could also examine
the economic implications of the divergence between a (possibly) inefficient
portfolio p and an efficient portfolio x in terms of utility losses, thus
answering the question: How much does an investor value the validity of an
asset pricing model? One possible way to answer this question is to compare
the expected utilities of the investor’s optimal portfolio choice under the
scenarios of efficiency and inefficiency. Here we examine this approach in
the context of testing the APT.11
Rewriting the empirical form of the APT in (9.2) in vector form, we
obtain:
R = α + Fβ′ + ϵ,
(9.10)
where: R = T × N matrix of excess return data.
F = T × K matrix of excess factor returns (factor premiums).
β = N × K matrix of factor sensitivities.
α = N × 1 vector of intercepts.
ϵ = T × N matrix of stock-specific returns series.
See Chapter 14 for more details on multifactor models, in particular,
the types of factor models and their estimation.
A close parallel has been shown to exist between the mean-variance
efficiency concept in the context of the CAPM and the APT. Testing the
pricing implication of the APT (the linear restriction that α = 0) is equivalent
to testing for mean-variance efficiency of the portfolio composed of the K
factor portfolios in (9.2).
We denote the case when mean-variance efficiency holds (α = 0) as the
‘‘restricted case’’ and the case when mean-variance efficiency does not hold
(α ̸= 0) as the ‘‘unrestricted case.’’ The metric to assess the economic signif-
icance of α’s distance from 0 is provided by the difference in the maximum
expected utilities (of portfolio return) under the restricted case and the unre-
stricted case. Since different returns are generally associated with different
11Our discussion is based on McCulloch and Rossi (1990).

172
BAYESIAN METHODS IN FINANCE
risk levels, utilities cannot be compared directly. Instead, utilities need to be
computed using a uniform measurement unit called the certainty-equivalent
return. Suppose the annual expected return of asset A is 7% with volatility
(standard deviation of the return) of 13%. The certainty-equivalent rate of
return is the risk-free rate of return (the ‘‘certain’’ return), Rce, which provides
the same utility as the return from holding asset A,
U (Rce, 0%) = U (7%, 13%) ,
where the volatility of the risk-free return is 0%, and U denotes a generic
utility function of two variables (expected return and volatility). Comparison
between the certainty equivalent levels in the restricted and unrestricted cases
is equivalent to the comparison between the utility levels corresponding to
these two cases.
Distributional Assumptions, Posterior and Predictive
Distributions
In Chapter 6, we reviewed the Bayesian approach to portfolio selec-
tion. We apply it again here as an intermediate step in computing the
certainty-equivalent returns under the hypotheses of efficiency and ineffi-
ciency. We proceed as follows. First, we find the optimal portfolio under
each hypothesis; second, we compute the expected utility of next-period’s
return on the optimal portfolio; third, we compute and compare the
certainty-equivalent returns. We start with deriving the predictive distri-
bution of next-period’s returns.
Suppose that the disturbances ϵ in (9.10) have a multivariate normal
distribution with covariance matrix . Denote by E and E0, respectively,
the mean vector of excess returns, R, in the unrestricted and the restricted
cases. They are given, respectively, by
E = α + µFβ′
and
E0 = µFβ′,
where µF is the sample mean vector of the time-series of factor returns.
The covariance return matrix is the same in the restricted and unrestricted
cases:12
V = β F β′ + ,
12See Chapter 14.

