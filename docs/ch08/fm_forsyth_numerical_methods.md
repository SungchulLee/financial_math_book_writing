# Monte Carlo & Finite Difference Methods

!!! info "Source"
    **An Introduction to Computational Finance Without Agonizing Pain** by Peter Forsyth, 2007.
    These notes are used for educational purposes.

## Monte Carlo Methods

Now, assuming that equation (4.30) holds, then from equations (4.32-4.35) we have
ˆp(y1, y2)
=
√
2π e−y2
1/2
√
2π e−y2
2/2
(4.36)
so that (y1, y2) are independent, normally distributed random variables, with mean zero and variance one,
or
y1 ∼N(0, 1)
;
y2 ∼N(0, 1) .
(4.37)
This gives the following algorithm for generating normally distributed random numbers (given uniformly
distributed numbers):
Box Muller Algorithm
Repeat
Generate u1 ∼U(0, 1), u2 ∼U(0, 1)
θ = 2πu2, ρ = √−2 log u1
z1 = ρ cos θ; z2 = ρ sin θ
End Repeat
(4.38)
This has the effect that Z1 ∼N(0, 1) and Z2 ∼N(0, 1).
Note that we generate two draws from a normal distribution on each pass through the loop.
4.3.1
An improved Box Muller
The algorithm (4.38) can be expensive due to the trigonometric function evaluations.
We can use the
following method to avoid these evaluations. Let
U1 ∼U[0, 1]
;
U2 ∼U[0, 1]
V1 = 2U1 −1
;
V2 = 2U2 −1
(4.39)
which means that (V1, V2) are uniformly distributed in [−1, 1] × [−1, 1]. Now, we carry out the following
procedure
Rejection Method
Repeat
If ( V 2
1 + V 2
2 < 1 )
Accept
Else
Reject
Endif
End Repeat
(4.40)
which means that if we define (V1, V2) as in equation (4.39), and then process the pairs (V1, V2) using
algorithm (4.40) we have that (V1, V2) are uniformly distributed on the disk centered at the origin, with
radius one, in the (V1, V2) plane. This is denoted by
(V1, V2)
∼
D(0, 1) .
(4.41)
If (V1, V2) ∼D(0, 1) and R2 = V 2
1 + V 2
2 , then the probability of finding R in [R, R + dR] is
p(R) dR
=
2πR dR
π(1)2
=
2R dR .
(4.42)
From the fundamental law of transformation of probabilities, we have that
p(R2)d(R2)
=
p(R)dR
=
2R dR
(4.43)
so that
p(R2)
=
2R
d(R2)
dR
=
(4.44)
so that R2 is uniformly distributed on [0, 1], (R2 ∼U[0, 1]).
As well, if θ = tan−1(V2/V1), i.e. θ is the angle between a line from the origin to the point (V1, V2) and
the V1 axis, then θ ∼U[0, 2π]. Note that
cos θ
=
V1
p
V 2
1 + V 2
sin θ
=
V2
p
V 2
1 + V 2
.
(4.45)
Now in the original Box Muller algorithm (4.38),
ρ =
p
−2 log U1
;
U1 ∼U[0, 1]
θ = 2ΠU2
;
U2 ∼U[0, 1] ,
(4.46)
but θ = tan−1(V2/V1) ∼U[0, 2π], and R2 = U[0, 1]. Therefore, if we let W = R2, then we can replace θ, ρ
in algorithm (4.38) by
θ
=
tan−1
V2
V1

ρ
=
p
−2 log W .
(4.47)
Now, the last step in the Box Muller algorithm (4.38) is
Z1
=
ρ cos θ
Z2
=
ρ sin θ ,
(4.48)
but since W = R2 = V 2
1 + V 2
2 , then cos θ = V1/R, sin θ = V2/R, so that
Z1
=
ρ V1
√
W
Z2
=
ρ V2
√
W
.
(4.49)
This leads to the following algorithm
Polar form of Box Muller
Repeat
Generate U1 ∼U[0, 1], U2 ∼U[0, 1].
Let
V1
=
2U1 −1
V2
=
2U2 −1
W
=
V 2
1 + V 2
If( W < 1) then
Z1
=
V1
p
−2 log W/W
Z2
=
V2
p
−2 log W/W
(4.50)
End If
End Repeat
Consequently, (Z1, Z2) are independent (uncorrelated), and Z1 ∼N(0, 1), and Z2 ∼N(0, 1). Because of the
rejection step (4.40), about (1 −π/4) of the random draws in [−1, +1] × [−1, +1] are rejected (about 21%),
but this method is still generally more efficient than brute force Box Muller.
4.4
Speeding up Monte Carlo
Monte Carlo methods are slow to converge, since the error is given by
Error
=
O(
√
M
)
where M is the number of samples.
There are many methods which can be used to try to speed up
convergence. These are usually termed Variance Reduction techniques.
Perhaps the simplest idea is the Antithetic Variable method. Suppose we compute a random asset path
Si+1
=
Siµ∆t + Siσφi√
∆t
where φi are N(0, 1). We store all the φi, i = 1, ..., for a given path. Call the estimate for the option price
from this sample path V +. Then compute a second sample path where (φi)′ = −φi, i = 1, ...,. Call this
estimate V −. Then compute the average
¯V
=
V + + V −
,
and continue sampling in this way. Averaging over all the ¯V , slightly faster convergence is obtained. Intu-
itively, we can see that this symmetrizes the random paths.
Let X+ be the option values obtained from all the V + simulations, and X−be the estimates obtained
from all the V −simulations. Note that V ar(X+) = V ar(X−) (they have the same distribution). Then
V ar(X+ + X−
)
=
4V ar(X+) + 1
4V ar(X−) + 1
2Cov(X+, X−)
=
2V ar(X+) + 1
2Cov(X+, X−)
(4.51)
which will be smaller than V ar(X+) if Cov(X+, X−) is nonpositive. Warning: this is not always the case.
For example, if the payoffis not a monotonic function of S, the results may actually be worse than crude
Monte Carlo. For example, if the payoffis a capped call
payoff
=
min(K2, max(S −K1, 0))
K2 > K1
then the antithetic method performs poorly.
Note that this method can be used to estimate the mean. In the MC error estimator (4.13), compute the
standard deviation of the estimator as ω =
q
V ar( X++X−
).
However, if we want to estimate the distribution of option prices (i.e. a probability distribution), then
we should not average each V + and V −, since this changes the variance of the actual distribution.
If we want to know the actual variance of the distribution (and not just the mean), then to compute the
variance of the distribution, we should just use the estimates V +, and compute the estimate of the variance
in the usual way. This should also be used if we want to plot a histogram of the distribution, or compute
the Value at Risk.
4.5
Estimating the mean and variance
An estimate of the mean ¯x and variance s2
M of M numbers x1, x2, ..., xM is
s2
M
=
M −1
M
X
i=1
(xi −¯x)2
¯x
=
M
M
X
i=1
xi
(4.52)
Alternatively, one can use
s2
M
=
M −1


M
X
i=1
x2
i −1
M
 M
X
i=1
xi
!2

(4.53)
which has the advantage that the estimate of the mean and standard deviation can be computed in one loop.
In order to avoid roundoff, the following method is suggested by Seydel (R. Seydel, Tools for Computa-
tional Finance, Springer, 2002). Set
α1 = x1 ;
β1 = 0
(4.54)
then compute recursively
αi
=
αi−1 + xi −αi−1
i
βi
=
βi−1 + (i −1)(xi −αi−1)2
i
(4.55)
so that
¯x
=
αM
s2
M
=
βM
M −1
(4.56)
4.6
Low Discrepancy Sequences
In a effort to get around the
√
M , (M = number of samples) behaviour of Monte Carlo methods, quasi-Monte
Carlo methods have been devised.
These techniques use a deterministic sequence of numbers (low discrepancy sequences). The idea here
is that a Monte Carlo method does not fill the sample space very evenly (after all, its random). A low
discrepancy sequence tends to sample the space in a orderly fashion. If d is the dimension of the space, then
the worst case error bound for an LDS method is
Error
=
O
(log M)d
M

(4.57)
where M is the number of samples used. Clearly, if d is small, then this error bound is (at least asymptotically)
better than Monte Carlo.
LDS methods generate numbers on [0, 1]. We cannot use the Box-Muller method in this case to produce
normally distributed numbers, since these numbers are deterministic. We have to invert the cumulative
normal distribution in order to get the numbers distributed with mean zero and standard deviation one on
[−∞, +∞]. So, if F(x) is the inverse cumulative normal distribution, then
xLDS
=
uniformly distributed on [0, 1]
yLDS
=
F(xLDS) is N(0, 1) .
(4.58)
Another problem has to do with the fact that if we are stepping through time, i.e.
Sn+1
=
Sn + Sn(r∆t + φσ
√
∆t)
φ = N(0, 1)
(4.59)
with, say, N steps in total, then we need to think of this as a problem in N dimensional space. In other
words, the k −th timestep is sampled from the k −th coordinate in this N dimensional space. We are trying
to uniformly sample from this N dimensional space.
Let ˆx be a vector of LDS numbers on [0, 1], in N dimensional space
ˆx =


x1
x2
|
xN

.
(4.60)
So, an LDS algorithm would proceed as follows, for the j′th trial
• Generate ˆxj (the j′th LDS number in an N dimensional space).
• Generate the normally distributed vector ˆyj by inverting the cumulative normal distribution for each
component
ˆyj =


F(xj
1)
F(xj
2)
|
F(xj
N)


(4.61)
• Generate a complete sample path k = 0, ..., N −1
Sk+1
j
=
Sk
j + Sk
j (r∆t + ˆyj
k+1σ
√
∆t)
(4.62)
• Compute the payoffat S = SN
j
The option value is the average of these trials.
There are a variety of LDS numbers: Halton, Sobol, Niederrieter, etc. Our tests seem to indicate that
Sobol is the best.
Note that the worst case error bound for the error is given by equation (4.57). If we use a reasonable
number of timesteps, say 50 −100, then, d = 50 −100, which gives a very bad error bound. For d large, the
numerator in equation (4.57) dominates. The denominator only dominates when
M
≃
ed
(4.63)
which is a very large number of trials for d ≃100. Fortunately, at least for path-dependent options, we have
found that things are not quite this bad, and LDS seems to work if the number of timesteps is less than
100 −200. However, once the dimensionality gets above a few hundred, convergence seems to slow down.
4.7
Correlated Random Numbers
In many cases involving multiple assets, we would like to generate correlated, normally distributed random
numbers. Suppose we have i = 1, ..., d assets, and each asset follows the simulated path
Sn+1
i
=
Sn
i + Sn
i (r∆t + φn
i σi
√
∆t)
(4.64)
where φn
i is N(0, 1) and
E(φn
i φn
j )
=
ρij
(4.65)
where ρij is the correlation between asset i and asset j.
Now, it is easy to generate a set of d uncorrelated N(0, 1) variables. Call these ϵ1, ..., ϵd. So, how do we
produce correlated numbers? Let
[Ψ]ij = ρij
(4.66)
be the matrix of correlation coefficients. Assume that this matrix is SPD (if not, one of the random variables
is a linear combination of the others, hence this is a degenerate case). Assuming Ψ is SPD, we can Cholesky
factor Ψ = LLt, so that
ρij
=
X
k
LikLt
kj
(4.67)
Let ¯φ be the vector of correlated normally distributed random numbers (i.e. what we want to get), and let
¯ϵ be the vector of uncorrelated N(0, 1) numbers (i.e. what we are given).
¯φ =


φ1
φ2
|
φd

; ¯ϵ =


ϵ1
ϵ2
|
ϵd


(4.68)
So, given ¯ϵ, we have
E(ϵiϵj)
=
δij
where
δij
=
0 ;
if i ̸= j
=
1 ;
if i = j .
since the ϵi are uncorrelated. Now, let
φi
=
X
j
Lijϵj
(4.69)
which gives
φiφk
=
X
j
X
l
LijLklϵlϵj
=
X
j
X
l
LijϵlϵjLt
lk .
(4.70)
Now,
E(φiφk)
=
E

X
j
X
l
LijϵlϵjLt
lk


=
X
j
X
l
LijE(ϵlϵj)Lt
lk
=
X
j
X
l
LijδljLt
lk
=
X
l
LilLt
lk
=
ρij
(4.71)
So, in order to generate correlated N(0, 1) numbers:
• Factor the correlation matrix Ψ = LLt
• Generate uncorrelated N(0, 1) numbers ϵi
• Correlated numbers φi are given from
¯φ
=
L¯ϵ
4.8
Integration of Stochastic Differential Equations
Up to now, we have been fairly slack about defining what we mean by convergence when we use forward
Euler timestepping (4.2) to integrate
dS = µS dt + σS dZ .
(4.72)
The forward Euler algorithm is simply
Si+1
=
Si + Si(µh + φi√
h)
(4.73)
where h = ∆t is the finite timestep. For a good overview of these methods, check out (“An algorithmic
introduction to numerical simulation of stochastic differential equations,” by D. Higham, SIAM Review vol.
43 (2001) 525-546). This article also has some good tips on solving SDEs using Matlab, in particular, taking
full advantage of the vectorization of Matlab. Note that eliminating as many for loops as possible (i.e.
computing all the MC realizations for each timestep in a vector) can reduce computation time by orders of
magnitude.
Before we start defining what we mean by convergence, let’s consider the following situation. Recall that
dZ = φ
√
dt
(4.74)
where φ is a random draw from a normal distribution with mean zero and variance one. Let’s imagine
generating a set of Z values at discrete times ti, e.g. Z(ti) = Zi, by
Zi+1
=
Zi + φ
√
∆t .
(4.75)
Now, these are all legitimate points along a Brownian motion path, since there is no timestepping error here,
in view of equation (2.53). So, this set of values {Z0, Z1, ..., } are valid points along a Brownian path. Now,
recall that the exact solution (for a given Brownian path) of equation (4.72) is given by equation (2.57)
S(T) = S(0) exp[(µ −σ2
2 )t + σ(Z(T) −Z(0))]
(4.76)
where T is the stopping time of the simulation.
Now if we integrate equation (4.72) using forward Euler, with the discrete timesteps ∆t = ti+1 −ti, using
the realization of the Brownian path {Z0, Z1, ..., }, we will not get the exact solution (4.76). This is because
even though the Brownian path points are exact, time discretization errors are introduced in equation (4.73).
So, how can we systematically study convergence of algorithm (4.73)? We can simply take smaller timesteps.
However, we want to do this by filling in new Z values in the Brownian path, while keeping the old values
(since these are perfectly legitimate values). Let S(T)h represent the forward Euler solution (4.73) for a
fixed timestep h. Let S(T) be the exact solution (4.76). As h →0, we would expect S(T)h →S(T), for a
given path.
4.8.1
The Brownian Bridge
So, given a set of valid Zk, how do we refine this path, keeping the existing points along this path? In
particular, suppose we have two points Zi, Zk, at (ti, tk), and we would like to generate a point Zj at tj,
with ti < tj < tk. How should we pick Zj? What density function should we use when generating Zj, given
that Zk is known?
Let x, y be two draws from a normal distribution with mean zero and variance one. Suppose we have the
point Z(ti) = Zi and we generate Z(tj) = Zj, Z(tk) = Zk along the Wiener path,
Zj
=
Zi + x
p
tj −ti
(4.77)
Zk
=
Zj + y
p
tk −tj
(4.78)
Zk = Zi + x
p
tj −ti + y
p
tk −tj .
(4.79)
So, given (x, y), and Zi, we can generate Zj, Zk. Suppose on the other hand, we have Zi, and we generate
Zk directly using
Zk
=
Zi + z√tk −ti ,
(4.80)
where z is N(0, 1). Then how do we generate Zj using equation (4.77)? Since we are now specifying that
we know Zk, this means that our method for generating Zj is constrained. For example, given z, we must
have that, from equations (4.79) and (4.80)
y
=
z√tk −ti −x√tj −ti
√tk −tj
.
(4.81)
Now the probability density of drawing the pair (x, y) given z, denoted by p(x, y|z) is
p(x, y|z)
=
p(x)p(y)
p(z)
(4.82)
where p(..) is a standard normal distribution, and we have used the fact that successive increments of a
Brownian process are uncorrelated.
From equation (4.81), we can write y = y(x, z), so that p(x, y|z) = p(x, y(x, z)|z)
p(x, y(x, z)|z)
=
p(x)p(y(x, z))
p(z)
=
√
2π exp

−1
2(x2 + y2 −z2)

(4.83)
or (after some algebra, using equation (4.81))
p(x|z)
=
√
2π exp

−1
2(x −αz)2/β2

α =
r
tj −ti
tk −ti
β =
r
tk −tj
tk −ti
(4.84)
so that x is normally distributed with mean αz and variance β2. Since
z
=
Zk −Zi
√tk −ti
(4.85)
we have that x has mean
E(x)
=
√tj −ti
tk −ti
(Zk −Zi)
(4.86)
and variance
E[(x −E(x))2]
=
tk −tj
tk −ti
(4.87)
Now, let
x
=
√tj −ti
tk −ti
(Zk −Zi) + φ
r
tk −tj
tk −ti
(4.88)
where φ is N(0, 1). Clearly, x satisfies equations (4.86) and (4.88). Substituting equation (4.88) into (4.77)
gives
Zj
=
tk −tj
tk −ti

Zi +
 tj −ti
tk −ti

Zk + φ
s
(tj −ti)(tk −tj)
(tk −ti)
(4.89)
where φ is N(0, 1). Equation (4.89) is known as the Brownian Bridge.
Figure 4.1 shows different Brownian paths constructed for different timestep sizes. An initial coarse path
is constructed, then the fine timestep path is constructed from the coarse path using a Brownian Bridge. By
construction, the final timestep path will pass through the coarse timestep nodes.
Figure 4.2 shows the asset paths integrated using the forward Euler algorithm (4.73) fed with the Brow-
nian paths in Figure 4.1. In this case, note that the fine timestep path does not coincide with the coarse
timestep nodes, due to the timestepping error.
4.8.2
Strong and Weak Convergence
Since we are dealing with a probabilistic situation here, it is not obvious how to define convergence. Given
a number of points along a Brownian path, we could imagine refining this path (using a Brownian Bridge),
and then seeing if the solution converged to exact solution. For the model SDE (4.72), we could ask that
E

|S(T) −Sh(T)|

≤
Const. hγ
(4.90)
where the expectation in equation (4.90) is over many Brownian paths, and h is the timestep size. Note
that S(T) is the exact solution along a particular Brownian path; the same path used to compute Sh(T).
Criterion (4.90) is called strong convergence. A less strict criterion is
|E [S(T)] −E

Sh(T)

|
≤
Const. hγ
(4.91)
Time
Brownian Path
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
-0.5
-0.4
-0.3
-0.2
-0.1
0.1
0.2
0.3
0.4
0.5
Time
Brownian Path
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
-0.5
-0.4
-0.3
-0.2
-0.1
0.1
0.2
0.3
0.4
0.5
Figure 4.1: Effect of adding more points to a Brownian path using a Brownian bridge. Note that the small
timestep points match the coarse timestep points. Left: each coarse timestep is divided into 16 substeps.
Right: each coarse timestep divided into 64 substeps.
Time
Asset Price
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
80
90
100
110
120
Time
Asset Price
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
80
90
100
110
120
Figure 4.2: Brownian paths shown in Figure 4.1 used to determine asset price paths using forward Euler
timestepping (4.73). In this case, note that the asset paths for fine and coarse timestepping do not agree at
the final time (due to the timestepping error). Eventually, for small enough timesteps, the final asset value
will converge to the exact solution to the SDE. Left: each coarse timestep is divided into 16 substeps. Right:
each coarse timestep divided into 64substeps.
T
.25
σ
.4
µ
.06
S0
Table 4.1: Data used in the convergence tests.
Timesteps
Strong Error (4.90)
Weak Error (4.91)
.0269
.00194
.0190
.00174
.0135
.00093
.0095
.00047
Table 4.2: Convergence results, 100,000 samples used. Data in Table 4.1.
It can be shown that using forward Euler results in weak convergence with γ = 1, and strong convergence
with γ = .5.
Table 4.1 shows some test data used to integrate the SDE (4.72) using method (4.73). A series of Brownian
paths was constructed, beginning with a coarse timestep path. These paths were systematically refined using
the Brownian Bridge construction. Table 4.2 shows results where the strong and weak convergence errors
are estimated as
Strong Error
=
N
N
X
i=1

|S(T)i −Sh(T)i|

(4.92)
Weak Error
=
| 1
N
N
X
i=1
[S(T)i] −1
N
N
X
i=1

Sh(T)i

| ,
(4.93)
where Sh(T)i is the solution obtained by forward Euler timestepping along the i′th Brownian path, and
S(T)i is the exact solution along this same path, and N is the number of samples. Note that for equation
(4.72), we have the exact solution
lim
N→∞
N
N
X
i=1
[S(T)i]
=
S0eµT
(4.94)
but we do not replace the approximate sampled value of the limit in equation (4.93) by the theoretical limit
(4.94). If we use enough Monte Carlo samples, we could replace the approximate expression
lim
N→∞
N
N
X
i=1
[S(T)i]
by S0eµT , but for normal parameters, the Monte Carlo sampling error is much larger than the timestepping
error, so we would have to use an enormous number of Monte Carlo samples. Estimating the weak error
using equation (4.93) will measure the timestepping error, as opposed to the Monte Carlo sampling error.
However, for normal parameters, even using equation (4.93) requires a large number of Monte Carlo samples
in order to ensure that the error is dominated by the timestepping error.
In Table 4.1, we can see that the ratio of the errors is about
√
2 for the strong error, and about two for
the weak error. This is consistent with a convergence rate of γ = .5 for strong convergence, and γ = 1.0 for
weak convergence.
4.9
Matlab and Monte Carlo Simulation
A straightforward implementation of Monte Carlo timestepping for solving the SDE
dS
=
µS dt + σS dZ
(4.95)
in Matlab is shown in Algorithm (4.96). This code runs very slowly.
Slow.m
randn(’state’,100);
T = 1.00;
% expiry time
sigma = 0.25;
% volatility
mu = .10;
% P measure drift
S_init = 100;
% initial value
N_sim = 10000;
%
number of simulations
N = 100;
%
number of timesteps
delt
= T/N;
%
timestep
drift = mu*delt;
sigma_sqrt_delt = sigma*sqrt(delt);
S_new = zeros(N_sim,1);
for m=1:N_sim
S = S_init;
for i=1:N % timestep loop
S = S + S*( drift + sigma_sqrt_delt*randn(1,1) );
S = max(0.0, S );
% check to make sure that S_new cannot be < 0
end % timestep loop
S_new(m,1) = S;
end % simulation loop
n_bin = 200;
hist(S_new, n_bin);
stndrd_dev = std(S_new);
disp(sprintf(’standard deviation:
%.5g\n’,stndrd_dev));
mean_S = mean(S_new);
disp(sprintf(’mean:
%.5g\n’,stndrd_dev));
(4.96)
Alternatively, we can use Matlab’s vectorization capabilities to interchange the timestep loop and the
simulation loop. The innermost simulation loop can be replaced by vector statements, as shown in Algorithm
(4.97). This runs much faster.
Fast.m
randn(’state’,100);
%
T = 1.00;
% expiry time
sigma = 0.25;
% volatility
mu = .10;
% P measure drift
S_init = 100;
% initial value
N_sim = 10000;
%
number of simulations
N = 100;
%
number of timesteps
delt
= T/N;
%
timestep
drift = mu*delt;
sigma_sqrt_delt = sigma*sqrt(delt);
S_old = zeros(N_sim,1);
S_new = zeros(N_sim,1);
S_old(1:N_sim,1) = S_init;
for i=1:N % timestep loop
% now, for each timestep, generate info for
% all simulations
S_new(:,1) = S_old(:,1) +...
S_old(:,1).*( drift + sigma_sqrt_delt*randn(N_sim,1) );
S_new(:,1) = max(0.0, S_new(:,1) );
% check to make sure that S_new cannot be < 0
S_old(:,1) = S_new(:,1);
%
%
end of generation of all data for all simulations
%
for this timestep
end % timestep loop
n_bin = 200;
hist(S_new, n_bin);
stndrd_dev = std(S_new);
disp(sprintf(’standard deviation:
%.5g\n’,stndrd_dev));
mean_S = mean(S_new);
disp(sprintf(’mean:
%.5g\n’,stndrd_dev));
(4.97)


## Finite Difference Methods

• An amount in a risk-free bank account B(t).
The hedge portfolio P(t) is then
P(t) = −V + αhS + βI + B(t)
Assuming that we buy and hold αh shares and β of the secondary instrument at the beginning of each
hedging interval, then we require that
∂P
∂S
=
−∂V
∂S + αh + β ∂I
∂S = 0
∂P
∂σ
=
−∂V
∂σ + β ∂I
∂σ = 0
(8.6)
Note that if we assume that σ is constant when pricing the option, yet do not assume σ is constant when
we hedge, this is somewhat inconsistent. Nevertheless, we can determine the derivatives in equation (8.6)
numerically (solve the pricing equation for several different values of σ, and then finite difference the solu-
tions).
In practice, we would sell the option priced using our best estimate of σ (today). This is usually based on
looking at the prices of traded options, and then backing out the volatility which gives back today’s traded
option price (this is the implied volatility). Then as time goes on, the implied volatility will likely change.
We use the current implied volatility to determine the current hedge parameters in equation (8.6). Since
this implied volatility has likely changed since we last rebalanced the hedge, there is some error in the hedge.
However, taking into account the change in the hedge portfolio through equations (8.6) should make up for
this error. This procedure is called delta-vega hedging.
In fact, even if the underlying process is a stochastic volatility, the vega hedge computed using a constant
volatility model works surprisingly well (Hull and White, The pricing of options on assets with stochastic
volatilities, J. of Finance, 42 (1987) 281-300).
Jump Diffusion
Recall that if
dS
=
µSdt + σS dZ
(9.1)
then from Ito’s Lemma we have
d[log S]
=
[µ −σ2
2 ] dt + σ dZ.
(9.2)
Now, suppose that we observe asset prices at discrete times ti, i.e. S(ti) = Si, with ∆t = ti+1 −ti. Then
from equation (9.2) we have
log Si+1 −log Si
=
log(Si+1
Si
)
≃
[µ −σ2
2 ] ∆t + σφ
√
∆t
(9.3)
where φ is N(0, 1). Now, if ∆t is sufficiently small, then ∆t is much smaller than
√
∆t, so that equation
(9.3) can be approximated by
log(Si+1 −Si + Si
Si
)
=
log(1 + Si+1 −Si
Si
)
≃
σφ
√
∆t.
(9.4)
Define the return Ri in the period ti+1 −ti as
Ri
=
Si+1 −Si
Si
(9.5)
so that equation (9.4) becomes
log(1 + Ri)
≃
Ri = σφ
√
∆t.
Consequently, a plot of the discretely observed returns of S should be normally distributed, if the as-
sumption (9.1) is true. In Figure 9.1 we can see a histogram of monthly returns from the S&P500 for the
period 1982 −2002. The histogram has been scaled to zero mean and unit standard deviation. A standard
normal distribution is also shown. Note that for real data, there is a higher peak, and fatter tails than
the normal distribution. This means that there is higher probability of zero return, or a large gain or loss
compared to a normal distribution.
−1.4
−1.2
−1
−0.8
−0.6
−0.4
−0.2
0.2
0.4
0.6
5
15
Figure 9.1: Probability density functions for the S&P 500 monthly returns 1982 −2002, scaled to zero mean
and unit standard deviation and the standardized Normal distribution.
As ∆t →0, Geometric Brownian Motion (equation (9.1)) assumes that the probability of a large return
also tends to zero. The amplitude of the return is proportional to
√
∆t, so that the tails of the distribution
become unimportant.
But, in real life, we can sometimes see very large returns (positive or negative) in small time increments.
It therefore appears that Geometric Brownian Motion (GBM) is missing something important.
9.1
The Poisson Process
Consider a process where most of the time nothing happens (contrast this with Brownian motion, where
some changes occur at any time scale we look at), but on rare occasions, a jump occurs. The jump size does
not depend on the time interval, but the probability of the jump occurring does depend on the interval.
More formally, consider the process dq where, in the interval [t, t + dt],
dq
=
1 ;
with probability λdt
=
0 ;
with probability 1 −λdt.
(9.6)
Note, once again, that size of the Poisson outcome does not depend on dt. Also, the probability of a jump
occurring in [t, t + dt] goes to zero as dt →0, in contrast to Brownian motion, where some movement always
takes place (the probability of movement is constant as dt →0), but the size of the movement tends to zero
as dt →0. For future reference, note that
E[dq]
=
λ dt · 1 + (1 −λ dt) · 0
=
λ dt
(9.7)
and
V ar(dq)
=
E[(dq −E[dq])2]
=
E[(dq −λ dt)2]
=
(1 −λ dt)2 · λ dt + (0 −λ dt)2 · (1 −λ dt)
=
λ dt + O((dt)2) .
(9.8)
Now, suppose we assume that, along with the usual GBM, occasionally the asset jumps, i.e. S →JS,
where J is the size of a (proportional) jump. We will restrict J to be non-negative.
Suppose a jump occurs in [t, t + dt], with probability λdt. Let’s write this jump process as an SDE, i.e.
[dS]jump
= (J −1)S dq
since, if a jump occurs
Safter jump
=
Sbefore jump + [dS]jump
=
Sbefore jump + (J −1)Sbefore jump
=
JSbefore jump
(9.9)
which is what we want to model. So, if we have a combination of GBM and a rare jump event, then
dS
=
µS dt + σS dZ + (J −1)S dq
(9.10)
Assume that the jump size has some known probability density g(J), i.e. given that a jump occurs, then the
probability of a jump in [J, J + dJ] is g(J) dJ, and
Z +∞
−∞
g(J) dJ
=
Z ∞
g(J) dJ = 1
(9.11)
since we assume that g(J) = 0 if J < 0. For future reference, if f = f(J), then the expected value of f is
E[f] =
Z ∞
f(J)g(J) dJ .
(9.12)
The process (9.10) is basically geometric Brownian motion (a continuous process) with rare discontinuous
jumps. Some example realizations of jump diffusion paths are shown in Figure 9.2.
Figure 9.3 shows the price followed by a listed drug company. Note the extreme price changes over very
small periods of time.
9.2
The Jump Diffusion Pricing Equation
Now, form the usual hedging portfolio
P
=
V −αS .
(9.13)
Now, consider
[dP]total
=
[dP]Brownian + [dP]jump
(9.14)
0
0.05
0.1
0.15
0.2
0.25
60
100
140
180
Time (years)
Asset Price
Figure 9.2: Some realizations of a jump diffusion process which follows equation (9.10).
Figure 9.3: Actual price of a drug company stock. Compare with simulation of a jump diffusion in Figure
9.2.
where, from Ito’s Lemma
[dP]Brownian
=
[Vt + σ2S2
VSS]dt + \[VS −αS\](µS dt + σS dZ)
(9.15)
and, noting that the jump is of finite size,
[dP]jump
=
[V (JS, t) −V (S, t)] dq −α(J −1)S dq .
(9.16)
If we hedge the Brownian motion risk, by setting α = VS, then equations (9.14-9.16) give us
dP
=
[Vt + σ2S2
VSS]dt + [V (JS, t) −V (S, t)]dq −VS(J −1)S dq .
(9.17)
So, we still have a random component (dq) which we have not hedged away. Let’s take the expected value
of this change in the portfolio, e.g.
E(dP)
=
[Vt + σ2S2
VSS]dt + E[V (JS, t) −V (S, t)]E[dq] −VSSE[J −1]E[dq]
(9.18)
where we have assumed that probability of the jump and the probability of the size of the jump are inde-
pendent. Defining E(J −1) = κ, then we have that equation (9.18) becomes
E(dP)
=
[Vt + σ2S2
VSS]dt + E[V (JS, t) −V (S, t)]λ dt −VSSκλ dt .
(9.19)
Now, we make a rather interesting assumption. Assume that an investor holds a diversified portfolio of
these hedging portfolios, for many different stocks. If we make the rather dubious assumption that these
jumps for different stocks are uncorrelated, then the variance of this portfolio of portfolios is small, hence
there is little risk in this portfolio. Hence, the expected return should be
E[dP]
=
rP dt .
(9.20)
Now, equating equations (9.19 and (9.20) gives
Vt + σ2S2
VSS + VS[rS −Sκλ] −(r + λ)V + E[V (JS, t)]λ = 0 .
(9.21)
Using equation (9.12) in equation (9.21) gives
Vt + σ2S2
VSS + VS[rS −Sκλ] −(r + λ)V + λ
Z ∞
g(J)V (JS, t) dJ = 0 .
(9.22)
Equation (9.22) is a Partial Integral Differential Equation (PIDE).
A common assumption is to assume that g(J) is log normal,
g(J) =
exp

−(log(J)−ˆµ)2
2γ2

√
2πγJ
.
(9.23)
where, some algebra shows that
E(J −1) = κ = exp(ˆµ + γ2/2) −1 .
(9.24)
Now, what about our dubious assumption that jump risk was diversifiable?
In practice, we can regard
σ, ˆµ, γ, λ as parameters, and fit them to observed option prices. If we do this, (see L. Andersen and J.
Andreasen, Jump-Diffusion processes: Volatility smile fitting and numerical methods, Review of Derivatives
Research (2002), vol 4, pages 231-262), then we find that σ is close to historical volatility, but that the fitted
values of λ, ˆµ are at odds with the historical values. The fitted values seem to indicate that investors are
pricing in larger more frequent jumps than has been historically observed. In other words, actual prices seem
to indicate that investors do require some compensation for jump risk, which makes sense. In other words,
these parameters contain a market price of risk.
Consequently, our assumption about jump risk being diversifiable is not really a problem if we fit the
jump parameters from market (as opposed to historical) data, since the market-fit parameters will contain
some effect due to risk preferences of investors.
One can be more rigorous about this if you assume some utility function for investors. See (Alan Lewis,
Fear of jumps, Wilmott Magazine, December, 2002, pages 60-67) or (V. Naik, M. Lee, General equilibrium
pricing of options on the market portfolio with discontinuous returns, The Review of Financial Studies, vol
3 (1990) pages 493-521.)
9.3
An Alternate Derivation of the Pricing Equation for Jump Diffusion
We will give a pure hedging argument in this section, in order to derive the PIDE for jump diffusion. Initially,
we suppose that there is only one possible jump size J, i.e. after a jump, S →JS, where J is a known
constant. Suppose
dS
=
a(S, t)dt + b(S, t)dZ + (J −1)S dq,
(9.25)
where dq is the Poisson process. Consider a contract on S, F(S, t), then
dF
=

aFS + b2
2 FSS + Ft

dt + bFSdZ + [F(JS, t) −F(S, t)] dq,
(9.26)
or, in more compact notation
dF
=
µ dt + σ∗dZ + ∆F dq
µ = aFS + b2
2 FSS + Ft
σ∗= bFS
∆F = [F(JS, t) −F(S, t)] .
(9.27)
Now, instead of hedging with the underlying asset, we will hedge one contract with another. Suppose we
have three contracts F1, F2, F3 (they could have different maturities for example).
Consider the portfolio Π
Π = n1F1 + n2F2 + n3F3
(9.28)
so that
dΠ
=
n1 dF1 + n2 dF2 + n3 dF3
=
n1(µ1 dt + σ∗
1 dZ + ∆F1 dq)
+n2(µ2 dt + σ∗
2 dZ + ∆F2 dq)
+n3(µ3 dt + σ∗
3 dZ + ∆F3 dq)
=
(n1µ1 + n2µ2 + n3µ3) dt
+(n1σ∗
1 + n2σ∗
2 + n3σ∗
3) dZ
+(n1∆F1 + n2∆F2 + n3∆F3) dq .
(9.29)
Eliminate the random terms by setting
(n1∆F1 + n2∆F2 + n3∆F3)
=
(n1σ∗
1 + n2σ∗
2 + n3σ∗
3)
=
0 .
(9.30)
This means that the portfolio is riskless, hence
dΠ
=
rΠ dt ,
(9.31)
hence (using equations (9.29-9.31))
(n1µ1 + n2µ2 + n3µ3)
=
(n1F1 + n2F2 + n3F3)r .
(9.32)
Putting together equations (9.30) and (9.32), we obtain


σ∗
σ∗
σ∗
∆F1
∆F2
∆F3
µ1 −rF1
µ2 −rF2
µ3 −rF3




n1
n2
n3


=


0

.
(9.33)
Equation (9.33) has a nonzero solution only if the rows are linearly dependent. There must be λB(S, t), λJ(S, t)
such that
(µ1 −rF1)
=
λBσ∗
1 −λJ∆F1
(µ2 −rF2)
=
λBσ∗
2 −λJ∆F2
(µ3 −rF3)
=
λBσ∗
3 −λJ∆F3 .
(9.34)
(We will show later on that λJ ≥0 to avoid arbitrage). Dropping subscripts, we have
(µ −rF)
=
λBσ∗−λJ∆F
(9.35)
and substituting the definitions of µ, σ∗, ∆F, from equations (9.27), we obtain
Ft + b2
2 FSS + (a −λBb)FS −rF + λJ[F(JS, t) −F(S, t)] = 0 .
(9.36)
Note that λJ will not be the real world intensity of the Poisson process, but J will be the real world jump
size.
In the event that, say, F3 = S is a traded asset, we note that in this case
σ∗
=
b
µ3
=
a
∆F3
=
(J −1)S .
(9.37)
From equation (9.34) we have that
(µ3 −rF3)
=
λBσ∗
3 −λJ∆F3 ,
(9.38)
or, using equation (9.37),
a −λBb
=
rS −λJ(J −1)S .
(9.39)
Substituting equation (9.39) into equation (9.36) gives
Ft + b2
2 FSS + [r −λJ(J −1)]SFS −rF + λJ[F(JS, t) −F(S, t)] = 0 .
(9.40)
Note that equation (9.36) is valid if the underlying asset cannot be used to hedge, while equation (9.40) is
valid only if the underlying asset can be used as part of the hedging portfolio.
Let τ = T −t, and set a = 0, b = 0, r = 0 in equation (9.36), giving
Fτ
=
λJ[F(JS, t) −F(S, t)] .
(9.41)
Now, suppose that
F(S, τ = 0)
=
0 ;
if S ≥K
=
1 ;
if S < K .
(9.42)
Now, consider the asset value S∗> K, and let J = K/(2 ∗S∗). Imagine solving equation (9.41) to an
infinitesimal time τ = ϵ ≪1. We will obtain the following value for F,
F(S∗, ϵ)
≃
ϵλJ .
(9.43)
Since the payoffis nonnegative, we must have λJ ≥0 to avoid arbitrage.
Now, suppose that there are a finite number of jump states, i.e. after a jump, the asset may jump to to
any state JiS
S
→JiS ;
i = 1, ..., n .
(9.44)
Repeating the above arguments, now using n + 2 hedging instruments in the hedging portfolio
Π =
i=n+2
X
i=1
niFi
(9.45)
so that the diffusion and jumps are hedged perfectly, we obtain the following PDE
Ft + b2
2 FSS + (a −λBb)FS −rF +
i=n
X
i=1
λi
J[F(JiS, t) −F(S, t)] = 0 .
(9.46)
If we can use the underlying to hedge, then we get the analogue of equation (9.40)
Ft + b2
2 FSS + (rS −
i=n
X
i=1
λi
JS(Ji −1))FS −rF +
i=n
X
i=1
λi
J[F(JiS, t) −F(S, t)] = 0 .
(9.47)
Now, let
p(Ji)
=
λi
J
Pi=n
i=1 λi
J
λ∗
=
i=n
X
i=1
λi
J
(9.48)
then we can write equation (9.46) as
Ft + b2
2 FSS + (a −λBb)FS −rF + λ∗
i=n
X
i=1
p(Ji)[F(JiS, t) −F(S, t)] = 0 .
(9.49)
Note that since λi
J ≥0, p(Ji) ≥0, and λ∗≥0.
Taking the limit as the number of jump states tends to infinity, then p(J) tends to a continuous distri-
bution, so that equation (9.49) becomes
Ft + b2
2 FSS + (a −λBb)FS −rF + λ∗
Z ∞
p(J)[F(JS, t) −F(S, t)] dJ = 0 .
(9.50)
It is convenient to rewrite equation (9.50) in a slightly different form. Suppose we redefine λB as follows
λB
=
λ′
B + λ∗E[J −1]S
b
(9.51)
where
E[J −1] =
Z ∞
p(J)(J −1) dJ .
(9.52)
Substituting equation (9.51) into equation (9.50) gives
Ft + b2
2 FSS + (a −λ′
Bb −λ∗E[J −1]S)FS −rF + λ∗
Z ∞
p(J)[F(JS, t) −F(S, t)] dJ = 0 .
(9.53)
Note that in the case that VSS = 0 (which would normally be the case for S →∞), then equation (9.53)
reduces to
Ft + b2
2 FSS + (a −λBb)FS −rF = 0 ,
(9.54)
so that the term λ∗E[J −1]S in the drift term cancels the integral term, leaving the equation independent
of λ∗. This is very convenient for applying numerical boundary conditions. The PIDE (9.53) can also be
written as
Ft + b2
2 FSS + (a −λ′
Bb)FS −rF + λ∗
Z ∞
p[J][F(JS, t) −F(S, t) −(J −1)SFS] dJ = 0
(9.55)
which is valid for infinite activity processes.
In the case where we can hedge with the underlying asset S, we obtain
Ft + b2
2 FSS + (r −λ∗E[J −1])SFS −rF + λ∗
Z ∞
p(J)[F(JS, t) −F(S, t)] dJ = 0 .
(9.56)
Note that λ∗and p(J) are not the real arrival rate and real jump size distributions, since they are based
on hedging arguments which eliminate the risk. Consequently, λ∗, p(J) must be obtained by calibration to
market data.
Regime Switching
Of course, volatility is not constant in the real world. It is possible to combine jumps in the asset price with
jumps in volatility and stochastic volatility. This leads to a two factor pricing PIDE for the option price.
A simpler approach is to assume that the volatility jumps between a number of regimes or volatility
states. Let the value of a contingent claim be given by F(σ, S, t), where we have allowed the volatility σ to
vary. Suppose
dS
=
a dt + b dZ + (JS −1)S dq
dσ
=
(Jσ −1)σ dq ,
(10.1)
where dq is a Poisson process and dZ is the increment of a Weiner process. Note that the same dq drives
the jump in S and the jump in σ. Following the same steps as in deriving equation (9.27) we obtain
dF
=
µ dt + σ∗dZ + ∆F dq
µ = aFS + b2
2 FSS + Ft
σ∗= bFS
∆F = [F(Jσσ, JSS, t) −F(σ, S, t)] .
(10.2)
We follow the same steps as in the derivation of the jump diffusion PIDE in equations (9.29-9.36), i.e. we
construct a hedge portfolio with three contracts F1, F2, F3, and we do not assume that we can trade in the
underlying. Eliminating the random terms gives rise to the analogue of equation (9.33) and hence a solution
exists only if one of the equations is a linear combination of the other equations, which results in
(µ −rF)
=
λBσ∗−λJ∆F
(10.3)
and substituting the definitions of σ∗, µ from equation (10.2) gives
Ft + b2
2 FSS + (a −λBb)FS −rF + λJ[F(Jσσ, JSS, t) −F(σ, S, t)] = 0 .
(10.4)
In the event that, say, F3 = S is a traded asset, we note that in this case
σ∗
=
b
µ3
=
a
∆F3
=
(JS −1)S .
(10.5)
Substituting equation (10.5) into equation (10.3) gives
a −λBb
=
rS −λJ(JS −1)S .
(10.6)
Substituting equation (10.6) into equation (10.4) gives
Ft + b2
2 FSS + [r −λJ(JS −1)]SFS −rF + λJ[F(Jσσ, JSS, t) −F(σ, S, t)] = 0 .
(10.7)
Note that if JS = 1 (no jump in S, but a regime switch) then the term λJ(JS −1) disappears in the drift
term.
We can repeat the above arguments with jumps from a given regime with volatility σ to several possible
regimes Ji
σσ, i = 1, . . . , p. Each possible transition σ →Ji
σσ is driven by a Poisson process dqi. We assume
that dqi and dqj are independent. In this case, we have
dS
=
a dt + b dZ +
i=p
X
i=1
(Ji
S −1)S dqi
dσ
=
i=p
X
i=1
(Jσ −1)σ dqi ,
(10.8)
Following the by now familiar steps, we obtain
Ft + b2
2 FSS + (a −λBb)FS −rF +
X
i
λi
J[F(Ji
σσ, Ji
SS, t) −F(σ, S, t)] = 0 .
(10.9)
Note that in general λi
J = λi
J(σ, S), Ji
σ = Ji
σ(σ, S), Ji
S = Ji
S(σ, S), and λB = λB(σ, S). Now, suppose we
have only a finite number of possible regimes σk, k = 1, . . . , p. Let
λk
B(σk, S)
=
λk
B(S))
F(σk, S, t)
=
F k(S, t)
λi
J(σk, S, t)
=
λk→i
J
Ji
σ(σk, S, t)
=
Jk→i
σ
Ji
S(σk, S, t)
=
Jk→i
S
.
(10.10)
Rewriting equation (10.9) using equation (10.10) gives
F k
t + b2
k
2 F k
SS + (ak −λk
Bbk)F k
S −rF k +
X
i
λk→i
J
[F i(Jk→i
S
S, t) −F k(S, t)] = 0 .
(10.11)
If we can hedge with the underlying, then the usual arguments give
ak −λk
Bbk
=
rS −
X
i
λk→i
J
(Jk→i
S
−1)S .
(10.12)
Substituting equation (10.12) into equation (10.11) gives
F k
t + b2
k
2 F k
SS + (r −
X
i
λk→i
J
(Jk→i
S
−1))SF k
S −rF k +
X
i
λk→i
J
[F i(Jk→i
S
S, t) −F k(S, t)] = 0 .
(10.13)
If we have only a small number of regimes, we are effectively solving a small number of coupled 1-d PDEs.
In principle, the Jk→i
S
, σk are P measure parameters, while the λk→i
J
is a Q measure parameter. We can also
determine the σk, Jk→i
S
, λk→i
J
by calibration to market prices.
Mean Variance Portfolio Optimization
An introduction to Computational Finance would not be complete without some discussion of Portfolio
Optimization. Consider a risky asset which follows Geometric Brownian Motion with drift
dS
S
=
µ dt + σ dZ ,
(11.1)
where as usual dZ = φ
√
dt and φ ∼N(0, 1). Suppose we consider a fixed finite interval ∆t, then we can
write equation (11.1) as
R
=
µ′ + σ′φ
R = ∆S
S
µ′ = µ∆t
σ′ = σ
√
∆t ,
(11.2)
where R is the actual return on the asset in [t, t + ∆t], µ′ is the expected return on the asset in [t, t + ∆t],
and σ′ is the standard deviation of the return on the asset in [t, t + ∆t].
Now consider a portfolio of N risky assets. Let Ri be the return on asset i in [t, t + ∆t], so that
Ri
=
µ′
i + σ′
iφi
(11.3)
Suppose that the correlation between asset i and asset j is given by ρij = E[φiφj]. Suppose we buy xi of
each asset at t, to form the portfolio P
P
=
i=N
X
i=1
xiSi .
(11.4)
Then, over the interval [t, t + ∆t]
P + ∆P
=
i=N
X
i=1
xiSi(1 + Ri)
∆P
=
i=N
X
i=1
xiSiRi
∆P
P
=
i=N
X
i=1
wiRi
wi =
xiSi
Pj=N
j=1 xjSj
(11.5)
In other words, we divide up our total wealth W = Pi=N
i=1 xiSi into each asset with weight wi. Note that
Pi=N
i=1 wi = 1.
To summarize, given some initial wealth at t, we suppose that an investor allocates a fraction wi of this
wealth to each asset i. We assume that the total wealth is allocated to this risky portfolio P, so that
i=N
X
i=1
wi
=
P
=
i=N
X
i=1
xiSi
Rp = ∆P
P
=
i=N
X
i=1
wiRi .
(11.6)
The expected return on this portfolio Rp in [t, t + ∆t] is
Rp
=
i=N
X
i=1
wiµ′
i ,
(11.7)
while the variance of Rp in [t, t + ∆t] is
V ar(Rp)
=
i=N
X
i=1
j=N
X
j=1
wiwjσ′
iσ′
jρij .
(11.8)
11.1
Special Cases
Suppose the assets all have zero correlation with one another, i.e. ρij ≡0, ∀i ̸= j (of course ρii = 1). Then
equation (11.8) becomes
V ar(Rp)
=
i=N
X
i=1
(σ′
i)2(wi)2 .
(11.9)
Now, suppose we equally weight all the assets in the portfolio, i.e. wi = 1/N, ∀i. Let maxiσ′
i = σ′
max, then
V ar(Rp)
=
N 2
i=N
X
i=1
(σ′
i)2
≤
N(σ′
max)2
N 2
=
O
 1
N

,
(11.10)
so that in this special case, if we diversify over a large number of assets, the standard deviation of the
portfolio tends to zero as N →∞.
Consider another case: all assets are perfectly correlated, ρij = 1, ∀i, j. In this case
V ar(Rp)
=
i=N
X
i=1
j=N
X
j=1
wiwjσ′
iσ′
j
=


j=N
X
j=1
wjσ′
j


(11.11)
so that if sd(R) =
p
V ar(R) is the standard deviation of R, then, in this case
sd(Rp)
=
j=N
X
j=1
wjσ′
j ,
(11.12)
which means that in this case the standard deviation of the portfolio is simply the weighted average of the
individual asset standard deviations.
In general, we can expect that 0 < |ρij| < 1, so that the standard deviation of a portfolio of assets will
be smaller than the weighted average of the individual asset standard deviation, but larger than zero.
This means that diversification will be a good thing (as Martha Stewart would say) in terms of risk versus
reward. In fact, a portfolio of as little as 10 −20 stocks tends to reap most of the benefits of diversification.
11.2
The Portfolio Allocation Problem
Different investors will choose different portfolios depending on how much risk they wish to take. However,
all investors like to achieve the highest possible expected return for a given amount of risk. We are assuming
that risk and standard deviation of portfolio return are synonymous.
Let the covariance matrix C be defined as
[C]ij = Cij = σ′
iσ′
jρij
(11.13)
and define the vectors ¯µ = [µ′
1, µ′
2, ..., µ′
N]t, ¯w = [w1, w2, ..., wN]t. In theory, the covariance matrix should be
symmetric positive semi-definite. However, measurement errors may result in C having a negative eigenvalue,
which should be fixed up somehow.
The expected return on the portfolio is then
Rp = ¯wt¯µ ,
(11.14)
and the variance is
V ar(Rp)
=
¯wtC ¯w .
(11.15)
We can think of portfolio allocation problem as the following. Let α represent the degree with which
investors want to maximize return at the expense of assuming more risk. If α →0, then investors want
to avoid as much risk as possible. On the other hand, if α →∞, then investors seek only to maximize
expected return, and don’t care about risk. The portfolio allocation problem is then (for given α) find ¯w
which satisfies
min
¯
w
¯wtC ¯w −α ¯wt¯µ
(11.16)
subject to the constraints
X
i
wi
=
(11.17)
Li ≤
wi
≤Ui ;
i = 1, ..., N .
(11.18)
Constraint (11.17) is simply equation (11.6), while constraints (11.18) may arise due to the nature of the
portfolio. For example, most mutual funds can only hold long positions (wi ≥0), and they may also be
prohibited from having a large position in any one asset (e.g. wi ≤.20). Long-short hedge funds will not
have these types of restrictions. For fixed α, equations (11.16-11.18) constitute a quadratic programming
problem.
Let
sd(Rp)
=
standard deviation of Rp
=
q
V ar(Rp)
(11.19)
Standard Deviation
Expected Return
0.2
0.3
0.4
0.5
0.6
0.1
0.125
0.15
0.175
0.2
0.225
0.25
Efficient Frontier
Figure 11.1: A typical efficient frontier. This curve shows, for each value of portfolio standard deviation
SD(Rp), the maximum possible expected portfolio return Rp. Data in equation (11.20).
We can now trace out a curve on the (sd(Rp), Rp) plane. We pick various values of α, and then solve the
quadratic programming problem (11.16-11.18). Figure 11.1 shows a typical curve, which is also known as
the efficient frontier. The data used for this example is
¯µ =


.15
.20
.08


;
C =


.20
.05
−.01
.05
.30
.015
−.01
.015
.1


L =


0


;
U =


∞
∞
∞


(11.20)
We have restricted this portfolio to be long only. For a given value of the standard deviation of the
portfolio return (sd(Rp)), then any point below the curve is not efficient, since there is another portfolio
with the same risk (standard deviation) and higher expected return. Only points on the curve are efficient
in this manner. In general, a linear combination of portfolios at two points along the efficient frontier will be
feasible, i.e. satisfy the constraints. This feasible region will be convex along the efficient frontier. Another
way of saying this is that a straight line joining any two points along the curve does not intersect the curve
except at the given two points. Why is this the case? If this was not true, then the efficient frontier would
not really be efficient. (see Portfolio Theory and Capital Markets, W. Sharpe, McGraw Hill, 1970, reprinted
in 2000).
Figure 11.2 shows results if we allow the portfolio to hold up to .25 short positions in each asset. In other
words, the data is the same as in (11.20) except that
L =


−.25
−.25
−.25

.
(11.21)
In general, long-short portfolios are more efficient than long-only portfolios. This is the advertised advantage
of long-short hedge funds.
Since the feasible region is convex, we can actually proceed in a different manner when constructing the
efficient frontier. First of all, we can determine the maximum possible expected return (α = ∞in equation
Standard Deviation
Expected Return
0.2
0.3
0.4
0.5
0.6
0.1
0.125
0.15
0.175
0.2
0.225
0.25
Long Only
Long-Short
Figure 11.2: Efficient frontier, comparing results for long-only portfolio (11.20) and a long-short portfolio
(same data except that lower bound constraint is replaced by equation (11.21).
(11.16)),
min
¯
w −¯wt¯µ
X
i
wi = 1
Li ≤wi ≤Ui ;
i = 1, ..., N
(11.22)
which is simply a linear programming problem. If the solution weight vector to this problem is ( ¯w)max, then
the maximum possible expected return is (Rp)max = ¯wt
max¯µ.
Then determine the portfolio with the smallest possible risk, (α = 0 in equation (11.16) )
min
¯
w
¯wtC ¯w
X
i
wi = 1
Li ≤wi ≤Ui ;
i = 1, ..., N .
(11.23)
If the solution weight vector to this quadratic program is given by ¯wmin, then the minimum possible portfolio
return is (Rp)min = ¯wt
min¯µ. We then divide up the range [(Rp)min, (Rp)max] into a large number of discrete
portfolio returns (Rp)k; k = 1, ..., Npts. Let e = [1, 1, ..., 1]t, and
A =

¯µt
et

;
Bk =

(Rp)k

(11.24)
then, for given (Rp)k we solve the quadratic program
min
¯
w
¯wtC ¯w
A ¯w = Bk
Li ≤wi ≤Ui ;
i = 1, ..., N ,
(11.25)
with solution vector ( ¯w)k and hence portfolio standard deviation sd((Rp)k) =
p
( ¯w)t
kC( ¯w)k. This gives us
a set of pairs (sd((Rp)k), (Rp)k), k = 1, ..., Npts.
Standard Deviation
Expected Return
0.1
0.2
0.3
0.4
0.5
0.6
0.025
0.05
0.075
0.1
0.125
0.15
0.175
0.2
0.225
0.25
Efficient Frontier
All Risky Assets
Risk Free
Return
Market
Portfolio
Capital Market
Line
Lending
Borrowing
Figure 11.3: The efficient frontier from Figure 11.1 (all risky assets), and the efficient frontier with the same
assets as in Figure 11.1, except that we include a risk free asset. In this case, the efficient frontier becomes
a straight line, shown as the capital market line.
11.3
Adding a Risk-free asset
Up to now, we have assumed that each asset is risky, i.e. σ′
i > 0, ∀i. However, what happens if we add a
risk free asset to our portfolio? This risk-free asset must earn the risk free rate r′ = r∆t, and its standard
deviation is zero. The data for this case is (the risk-free asset is added to the end of the weight vector, with
r′ = .03).
¯µ =


.15
.20
.08
.03


;
C =


.20
.05
−.01
0.0
.05
.30
.015
0.0
−.01
.015
.1
0.0
0.0
0.0
0.0
0.0


L =


0
−∞


;
U =


∞
∞
∞
∞


(11.26)
where we have assumed that we can borrow any amount at the risk-free rate (a dubious assumption).
If we compute the efficient frontier with a portfolio of risky assets and include one risk-free asset, we get
the result labeled capital market line in Figure 11.3. In other words, in this case the efficient frontier is a
straight line. Note that this straight line is always above the efficient frontier for the portfolio consisting of
all risky assets (as in Figure 11.1). In fact, given the efficient frontier from Figure 11.1, we can construct the
efficient frontier for a portfolio of the same risky assets plus a risk free asset in the following way. First of all,
we start at the point (0, r′) in the (sd(Rp), Rp) plane, corresponding to a portfolio which consists entirely
of the risk free asset. We then draw a straight line passing through (0, r′), which touches the all-risky-asset
efficient frontier at a single point (the straight line is tangent the all-risky-asset efficient frontier). Let the
portfolio weights at this single point be denoted by ¯wM. The portfolio corresponding to the weights ¯wM
is termed the market portfolio. Let (Rp)M = ¯wt
M ¯µ be the expected return on this market portfolio, with
corresponding standard deviation sd((Rp)M). Let wr be the fraction invested in the risk free asset. Then,
any point along the capital market line has
Rp
=
wrr′ + (1 −wr)(Rp)M
sd(Rp)
=
(1 −wr) sd((Rp)M) .
(11.27)
If wr ≥0, then we are lending at the risk-free rate. If wr < 0, we are borrowing at the risk-free rate.
Consequently, given a portfolio of risky assets, and a risk-free asset, then all investors should divide their
assets between the risk-free asset and the market portfolio. Any other choice for the portfolio is not efficient.
Note that the actual fraction selected for investment in the market portfolio depends on the risk preferences
of the investor.
The capital market line is so important, that the equation of this line is written as Rp = r′+λM sd((Rp)),
where λM is the market price of risk. In other words, all diversified investors, at any particular point in
time, should have diversified portfolios which plot along the capital market line. All portfolios should have
the same Sharp ratio
λM
=
Rp −r′
sd(Rp) .
(11.28)
11.4
Criticism
Is mean-variance portfolio optimization the solution to all our problems? Not exactly. We have assumed
that µ′, σ′ are independent of time. This is not likely. Even if these parameters are reasonably constant,
they are difficult to estimate. In particular, µ′ is hard to determine if the time series of returns is not very
long. Remember that for short time series, the noise term (Brownian motion) will dominate. If we have a
long time series, we can get a better estimate for µ′, but why do we think µ′ for a particular firm will be
constant for long periods? Probably, stock analysts should be estimating µ′ from company balance sheets,
sales data, etc. However, for the past few years, analysts have been too busy hyping stocks and going to
lunch to do any real work. So, there will be lots of different estimates of µ′, C, and hence many different
optimal portfolios.
In fact, some recent studies have suggested that if investors simply use the 1/N rule, whereby initial
wealth is allocated equally between N assets, that this does a pretty good job, assuming that there is
uncertainty in the estimates of µ′, C.
We have also assumed that risk is measured by standard deviation of portfolio return. Actually, if I am
long an asset, I like it when the asset goes up, and I don’t like it when the asset goes down. In other words,
volatility which makes the price increase is good. This suggests that perhaps it may be more appropriate to
minimize downside risk only (assuming a long position).
Perhaps one of the most useful ideas that come from mean-variance portfolio optimization is that diver-
sified investors (at any point in time) expect that any optimal portfolio will produce a return
Rp
=
r′ + λMσ′
p
Rp = Expected portfolio return
r′ = risk-free return in period ∆t
λM = market price of risk
σ′
p = Portfolio volatility ,
(11.29)
where different investors will choose portfolios with different σ′
p (volatility), depending on their risk prefer-
ences, but λM is the same for all investors. Of course, we also have
RM
=
r′ + λMσ′
M .
(11.30)
Note: there is a whole field called Behavioural Finance, whose adherents don’t think much of mean-
variance portfolio optimization.
Another recent approach is to compute the optimal portfolio weights using using many different perturbed
input data sets.
The input data (expected returns, and covariances) are determined by resampling, i.e.
assuming that the observed values have some observational errors. In this way, we can get an some sort of
optimal portfolio weights which have some effect of data errors incorporated in the result. This gives us an
average efficient frontier, which, it is claimed, is less sensitive to data errors.
11.5
Individual Securities
Equation (11.30) refers to an efficient portfolio.
What is the relationship between risk and reward for
individual securities? Consider the following portfolio: divide all wealth between the market portfolio, with
weight wM and security i, with weight wi. By definition
wM + wi
=
1 ,
(11.31)
and we define
RM
=
expected return on the market portfolio
Ri
=
expected return on asset i
σ′
M
=
s.d. of return on market portfolio
σ′
i
=
s.d. of return on asset i
Ci,M
=
σ′
Mσ′
iρi,M
=
Covariance between i and M
(11.32)
Now, the expected return on this portfolio is
Rp = E[Rp]
=
wiRi + wMRM
=
wiRi + (1 −wi)RM
(11.33)
and the variance is
V ar(Rp)
=
(σ′
p)2 = w2
i (σ′
i)2 + 2wiwMCi,M + w2
M(σ′
M)2
=
w2
i (σ′
i)2 + 2wi(1 −wi)Ci,M + (1 −wi)2(σ′
M)2
(11.34)
For a set of values {wi}, equations (11.33-11.34) will plot a curve in expected return-standard deviation
plane (Rp, σ′
p) (e.g. Figure 11.3). Let’s determine the slope of this curve when wi →0, i.e. when this curve
intersects the capital market line at the market portfolio.
2(σ′
p)∂(σ′
p)
∂wi
=
2wi(σ′
i)2 + 2(1 −2wi)Ci,M + 2(wi −1)(σ′
M)2
∂Rp
∂wi
=
Ri −RM .
(11.35)
Now,
∂Rp
∂(σ′p)
=
∂Rp
∂wi
∂(σ′p)
∂wi
=
(Ri −RM)(σ′
p)
wi(σ′
i)2 + (1 −2wi)Ci,M + (wi −1)(σ′
M)2
.
(11.36)
Now, let wi →0 in equation (11.36), then we obtain
∂Rp
∂(σ′p)
=
(Ri −RM)(σ′
M)
Ci,M −(σ′
M)2
(11.37)
But this curve should be tangent to the capital market line, equation (11.30) at the point where the capital
market line touches the efficient frontier. If this curve is not tangent to the capital market line, then this
implies that if we choose wi = ±ϵ, then the curve would be above the capital market line, which should not
be possible (the capital market line is the most efficient possible portfolio). This assumes that positions with
wi < 0 in asset i are possible.
Assuming that the slope of the Rp portfolio is tangent to the capital market line gives (from equations
(11.30,11.37))
RM −r′
(σ′
M)
=
(Ri −RM)(σ′
M)
Ci,M −(σ′
M)2
(11.38)
or
Ri
=
r′ + βi(RM −r′)
βi = Ci,M
(σ′
M)2 .
(11.39)
The coefficient βi in equation (11.39) has a nice intuitive definition. Suppose we have a time series of returns
(Ri)k
=
Return on asset i, in period k
(RM)k
=
Return on market portfolio in period k .
(11.40)
Typically, we assume that the market portfolio is a broad index, such as the TSX 300. Now, suppose we try
to obtain a least squares fit to the above data, using the equation
Ri ≃αi + biRM .
(11.41)
Carrying out the usual least squares analysis (e.g. do a linear regression of Ri vs. RM), we find that
bi = Ci,M
(σ′
M)2
(11.42)
so that we can write
Ri ≃αi + βiRM .
(11.43)
This means that βi is the slope of the best fit straight line to a ((Ri)k, (RM)k) scatter plot. An example is
shown in Figure 11.4. Now, from equation (11.39) we have that
Ri
=
r′ + βi(RM −r′)
(11.44)
which is consistent with equation (11.43) if
Ri
=
αi + βiRM + ϵi
E[ϵi] = 0
αi = r′(1 −βi)
E[ϵi, RM] = 0 ,
(11.45)
since
E[Ri] = Ri
=
αi + βiRM .
(11.46)

