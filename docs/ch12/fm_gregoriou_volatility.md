# Volatility Modeling & Estimation

!!! info "Source"
    **Financial Econometrics: From Basics to Advanced Modeling Techniques** edited by Greg N. Gregoriou and Razvan Pascalau, Wiley, 2009.
    These notes are used for educational purposes.

## Volatility Estimation and Modeling

76
Y. D. Tangman, R. Boojhawon, A. Gopaul and M. Bhuruth
4.3.2
Merton’s jump diffusion
In order to solve the PIDE for Merton’s jump diffusion, we realize, as
in Carr and Mayo (2007), that the integral F =

ℜV(x + z,τ)g(z)dz is
equivalent to the solution of a heat problem, and, for µJ ̸= 0, this
solution is translated by µJ such that the PDE satisfied by F is the
convection-diffusion equation
∂F
∂τ = ∂2F
∂x2 + 2µJ
σ 2
J
∂F
∂x ,
−∞< x < ∞,
0 ≤τ ≤
σ 2
J
2 ,
with same initial and linear boundary conditions as for the European call
problem (4.8). Hence, using the one-step exponential integration after
discretizing the spatial operator to obtain the semi-discretization matrix
B = D2x +

2 µJ
σ 2
J

D1x, we get
F = e
B
	
σ2
J
2

V(x,0),
as the solution to the convection-diffusion problem which is also an
approximation to the integral term. Thus the European option price
will be
V(T) = e(A+FM)TV(0),
(4.11)
where FM = λexp(Bσ 2
J /2). Here, we require a double matrix exponen-
tiation, and we will explain in Section 4.4 how this is done efficiently
by taking advantage of the commutativity feature of the differential and
integral operator.
4.3.3
Carr-German-Madan-Yor (CGMY) model
For the CGMY model, we also consider the PIDE (4.5), but here we
need to split the infinite domain of integration into z = x and
z∗\z where z∗is an extension of our domain such that the trun-
cation error of the integral approximation on the unbounded domain
is negligible. For example, we can take the domains Z = (−2,2) and
Z∗= (−4,4). For jump processes such as in Merton’s model, a sim-
ple composite trapezoidal discretization of the integral part will give
second-order convergence (Tangman et al. 2008b). However, it is well
known that a lower convergence rate is observed for infinite activity
processes and the quadrature methods used in (Wang et al. 2007) are
essential in order to obtain second-order convergence. In general, a spe-
cial treatment of the singularity in the integrand at z = 0 is required

A General Efficient Framework for Pricing Options
77
(Cont and Voltchkova 2005), and we further need to split the integral
domain as 0 = {z : |z| ≤z/2},1 = z\0 and 2 = z∗\(1 ∪0).
Then approximating the integro term in the PIDE (4.5) over z∗gives
FDVz∗−λ(z)V(x,τ) −κ(z)Vx(x,τ) + ˆσ(z)
2
Vxx(x,τ),
where λ(z) = 
zj∈z∗g(zj), κ(z) = 
zj∈z∗g(zj)(ezj −1), Vz∗rep-
resents the option values in z∗,
ˆσ(z) =
 z
2
−z
2
(ez −1)2g(z)dz (see
Tangman et al. 2010 for details) and
FDVz∗= FLV−
2 + FMV0∪1 + FRV+
2 ,
where FL, FM and FR are Toeplitz matrices. Here −
2 and +
2 represent
negative and positive nodes of 2 respectively and can be approximated
by the asymptotic option values for V2.
Then we can formulate (4.5) as the semi-discrete linear system
V′(τ) = (A + FM)V(τ) + b(τ),
0 ≤τ ≤T,
(4.12)
where A is constructed in a way similar to equation (4.10) as
A = σ 2 + ˆσ(z)
2
D2
x +
	
r −δ −σ 2 + ˆσ(z)
2
−κ(z)

D1
x −(r + λ(z))Ix,
(4.13)
and the remaining integral term b(τ) = FLV−
2 +FRV+
2 . For a call option,
V−
2 = 0 and V+
2 = Eex −Ee−rτ . Integrating (4.12) with respect to time
gives
V(T) = e(A+FM)TV(0) + e(A+FM)T
 T
0
e−(A+FM)τ b(τ)dτ.
(4.14)
The special structure of the vector b(τ) allows a closed-form expression
for the integral term in (4.14). It is easy to prove that the second term
on the right hand side of (4.14) becomes
h = Tφ1 ((A + FM)T)(FRε1) −((A + FM) + rI)−1
e(A+FM)T −e−rT
(FRε2),
where ε1 = Ee+
2 and ε2 is a vector with entries equal to E.
4.3.4
Stochastic volatility and stochastic volatility with jumps
In the SV and SVJ models, we can define the computational grid on y
and, hence, the difference matrices D1y, D2y and Iy. Then, by using the

78
Y. D. Tangman, R. Boojhawon, A. Gopaul and M. Bhuruth
Kronecker product ⊗we can easily approximate the spatial operator in
equation (4.7) to obtain the block tridiagonal matrix A ∈ℜm2×m2 as
A = 1
2y

Iy ⊗D2
x

+ 1
2γ 2y

D2
y ⊗Ix

+ ργ y

Iy ⊗D1
x

D1
y ⊗Ix

+

r −δ −λκ −1
2y

Iy ⊗D1
x‘

+ α

β −y

D1
y ⊗Ix

−(r + λ)

Iy ⊗Ix

,
(4.15)
and construct V ∈ℜm2×1 if m grid points are also used for y. Including
jumps will also be trivial using FM =

Iy ⊗λexp(Bσ 2
j /2)

and the solution
is given by equation (4.11).
4.3.5
American options
Finally, to solve American options, we will combine ETI with the opera-
tor splitting technique proposed in Ikonen and Toivanen (2004). Their
method is based on transforming the inequalities in equation (4.9) into
equalities by the addition of an auxiliary term p(τ)and for an American
option under the jump-diffusion model, this results in
Vτ = (A + FM)V + b + p(τ),
where b represents a constant vector since for American options, the pay-
off values are used for V2. On the other hand, b = 0 if the method given
by Carr and Mayo (2007) is used. Then the constraints are enforced as
[V(x,τ) −V(X,0)] · p(τ) = 0,
V(X,τ) ≥V(X,0),
p(τ) ≥0.
The term p(τ) acts as a penalty term, which is positive if the American
constraint is not satisfied and zero otherwise. Using the exponential
forward Euler scheme (4.2), we get
V(τj+1) = ϕ0 ((A + FM)τ)V(τj) + τ ϕ1 ((A + FM)τ)

b + p(τj)

,
(4.16)
as a first step split solution with τj+1 = τj + T/n. Then the American
option price and the new penalty term are computed by
V(τj+1) = max

V(τ0),V(τj+1) + τ p(τj)

,
p(τj+1) = p(τj) + 1
τ

V(τj+1) −V(τj+1)

.
(4.17)

A General Efficient Framework for Pricing Options
79
It is obvious that the most important part of the implementation will
require the evaluation of the different ϕl(A) functions for l = 0,1 or, more
precisely, their action on the vector V.
4.4
The matrix exponential
In this section, to describe the method for evaluating ϕ, we assume with
no confusion that A is already scaled by τ. Since Moler and Van Loan
(2003), most exponential-type integrators use Padé approximation with
scaling and squaring for computing the ϕl functions as suggested in
Beylkin et al. (1998) and Minchev and Wright (2005). The same tech-
nique is used by the “expm” function in MATLAB®, and, in our case,
since the semi-discretization matrix A is already scaled by τ, the method
works faster since less scaling and squaring is required. Recently, Ashi
et al. (2009) compared the accuracy and computational time of sev-
eral methods, and the scaling and squaring technique was found to be
efficient. However, the amount of work required is about O(m3). This
approach works well for matrices of moderate dimension, but in practice,
when A is large and sparse, we prefer methods that simply approximate
the action of the matrix function ϕl(A) on the vector V. In this set-
ting, one of the most promising techniques is based on best rational
approximations.
4.4.1
Best rational approximations via
Carathéodory–Fejér points
For the semi-discretization matrix A with eigenvalues in the left-half
plane, it is sufficient to study an approximation for ez on z ∈(−∞,0]
in order to compute ϕl(A)V (Schmelzer and Trefethen 2007). Evaluating
the matrix exponentiation based on best rational approximation com-
puted via Carathéodory–Fejér (Trefethen et al. 2006) is very promising
since sparse direct solvers can efficiently be used to solve the resulting
shifted linear systems of the form (zjI −A)xj = V. Following (Schmelzer
and Trefethen 2007; Trefethen et al. 2006) and using the fact that a ratio-
nal approximation can be interpreted as a quadrature formula or vice
versa, we represent the rational approximation as the partial fraction
expansion
ϕ0(A)V ≈
η
j=1 cj(A −zjI)−1V.
The residues cj and poles zj can be computed via Carathéodory-Fejér
approximations and a MATLAB® code based on a singular value decom-
position of a Hankel matrix is given in Trefethen et al. (2006). In

80
Y. D. Tangman, R. Boojhawon, A. Gopaul and M. Bhuruth
Schmelzer and Trefethen (2007), the code further considers the poles and
residues for all ϕl functions showing even better accuracy as l increases.
Instead of computing cj and zj for ϕ1, Schmelzer and Trefethen (2007)
used the common poles and residues of ϕ0 and obtained the relation
ϕ1(A)V ≈
η
j=1 cjz−1
j
(A −zjI)−1V.
(4.18)
Although this procedure is less accurate, yet it achieves reasonable accu-
racy for η ≥8. This means that we need to solve the same set of linear
systems for both ϕ0 and ϕ1. Also, since for financial problems the
matrices that arise are real, the poles and residues come in complex con-
jugate pairs. Thus, only η/2 shifted linear systems solutions are required,
making rational approximation very efficient. Furthermore, to evalu-
ate equation (4.14), we can thus make use of the Carathéodory–Fejér
approximation
	
eAτ −e−rτ I
Aτ + rτI

V ≈
η

k=1
ck
zk + rτ (Aτ −zkI)−1V.
For Merton’s model, we note that it can prove costly to calculate equation
(4.11) directly since the second exponential will have a dense matrix as
argument due to the first matrix exponential. Instead, using the fact that
integral and differential operators are commutative, we can approximate
the two spatial operators in equation (4.11) as
V(T) = eAT+FMTV(0) ≈eFMTeATV(0),
= exp(λT exp(Bσ 2
J /2))[exp(AT)V(0)].
For the Carathéodory–Fejér method, this means that we need only solve
sparse shifted linear systems and thus gain in computational efficiency.
To obtain the Carathéodory–Fejér points for the double exponential, we
need to modify the MATLAB® code in Trefethen et al. (2006) as
F = exp(λT exp(scl(t −1)/(t + 1 + 1e−16))) −1,
to obtain v2 = exp(FMT)v1 −v1 where v1 = exp(AT)V(0) and FM is as in
(4.11). Hence V(T) is the sum of v1 and v2, t is the Chebychev points,
and scl represents the scaling factor for stability. Another possibility to
prevent the dense matrix inversion is to use the regular matrix splitting
(Almendral and Oosterlee 2005) and to solve the linear system using the
fixed point iteration
Vk = (AT −zkI)−1[V(0) −(FMT)Vk−1].

A General Efficient Framework for Pricing Options
81
We can even use FFT to perform the dense matrix vector multiplication
in O(mlogm) for FM as in equations (4.11) or (4.12). We now give the
general algorithm for option pricing using ETI.
Algorithm 4.1: General algorithm for option
pricing using ETI
1. Problem start
a. Set the model parameters.
b. Construct x, y and .
2. Spatial discretization
c. Set D1x,D2x,Ix,D1y,D2y,Iy using one-sided approximations if neces-
sary.
d. Implement any linear boundary condition Vxx = Vx.
e. Build A using either equation (4.10), (4.13), or (4.15).
f. Implement any other boundary conditions such as, for example,
A1,1 = −rfor a European call and Am+1,1:m+1 = 0,A1:m+1,m+1 = 0,
for an up-and-out barrier.
3. Integral approximation
g. Form FM = λexp(Bσ 2
J /2) for Merton’s jump-diffusion model.
h. Form FL,FM,FR and compute V−
2 , V+
2 and ε1, ε2 for the CGMY
model.
4. Matrix exponential
i. viii. For the Carathéodory–Fejér method, use η = 8 to compute cj,
zj and use (4.18) for odd j.
5. Solution process: European
j. Set τ = T.
k. For Black–Scholes, SV, compute V(T) = exp(Aτ)V(0).
l. For Merton’s model, compute (4.11).
m. For CGMY, compute (4.14).
n. For SVJ, compute (4.11) with FM = [Iy ⊗λexp(Bσ 2
J /2)].
6. Solution process: American
o. Set n and compute τ = T/n.
p. for j = 1,...,n, compute equations (4.16) and (4.17).
4.5
Numerical experiments
We now present the results of our numerical experiments which were
carried out using MATLAB®. For all test cases, we use a computer with
1 GB RAM and 2.21 GHZ AMD Athlon X2 processor. Implementation
on other machines and using other programming languages will give

82
Y. D. Tangman, R. Boojhawon, A. Gopaul and M. Bhuruth
Table 4.1
CPU(s) time in seconds and error at spot price for all methods for
pricing a European call option
m
Crank–
Nicolson
ETIExpm
ETICF
Error
m
Crank–
Nicolson ETIExpm
ETICF
Error
27
0.1720
0.0310
0.0160
0.0060
210
1.3120
30.422
0.0470
9.42e-5
28
0.3280
0.4690
0.0220
0.0015
211
2.6250
241.86
0.0780
2.36e-5
29
0.6410
3.9060
0.0310
3.77e-4
212
5.7190
−
0.1570
5.89e-6
somewhat different results. Unless specified otherwise, we will use the
following table of parameters.
S0 = 100,σ = 0.2,τ = 0.05,δ = 0,E = 100,T = 1,SB = 160,
µJ = 0,σJ = 0.2,λ = 1,ρ = 0.1,α = 5,β = 0.16,xB = 0.8
For SV and SVJ models: T = 0.25,E = 1
For the CGMY model: C = 0.5,G = 10,M = 10
For American call options: δ = 0.07
Table 4.1 shows the speed of execution of different algorithms based on
ETI and the Crank–Nicolson scheme for solving a European call option
and also include the error at S0. Clearly, all algorithms will have almost
the same accuracy as m varies since the ETI method is exact in time,
and, for a sufficiently refined time step, Crank–Nicolson will contain
only spatial discretization error. However, we emphasize the huge com-
putational speed improvements of the ETI scheme combined with the
Carathéodory–Fejér method that also outperforms, by far, the Crank–
Nicolson method. It is observed that the increase in computational time
is linearly related to the increasing number of spatial steps, confirm-
ing that ETICF has indeed O(ηm/2) complexity. This is not the case of
ETIExpm, which is O(m3) and thus has the worst CPU timing. This
code could not be run for the last value of m due to the huge storage
requirements needed by the “expm” function. Since the Crank–Nicolson
method lacks L0 stability, it is essential to restrict the time-step size at
least as O(x), and, for a fair comparison, we will choose τ such that
the error is approximately the same for all methods. Hence, the Crank–
Nicolson scheme, which is O(nm) for n time steps, is slower since it needs
to solve much more than the six linear systems required by the ETICF
algorithm if η = 12. Actually, our intensive numerical experiments have
shown that only four shifted linear systems solution are needed to obtain

A General Efficient Framework for Pricing Options
83
very satisfactory accurate prices. Henceforth, for option pricing under
the ETI framework, we will use the ETICF with 8 Carathéodory–Fejér
points.
With the striking low speed of the ETICF method, we now turn our-
selves to the pricing of an American put option in the Black–Scholes
framework. Since simple solutions do not exist for this option, we use
the monotonically convergent binomial method of Leisen and Reimer
(1996) with 15,001 steps as benchmark. Here the free-boundary value
problem is solved by enforcing the American constraint at each time
step. We consider a short (T = 0.5) and a long (T = 3) maturity example
and compare the ETICF with the operator splitting technique (ETIC-
FOS) with the commonly used Crank–Nicolson with projected successive
over-relaxation method (CNPSOR) and Crank–Nicolson with operator
splitting (CNOS).
Table 4.2 shows that PSOR converges very slowly for both short and
long maturities. Both the ETICFOS and CNOS schemes seem very effi-
cient as they are not only faster, but also give accurate option prices
and the two hedging parameters, delta and gamma. In addition, we can
see that doubling the number of spatial nodes approximately doubles
the CPU time showing that both are algorithms with linear computa-
tional complexity (Tangman, Gopaul and Bhuruth, 2008a). This is of
p(τ)
 ≤rE S0 for CNOS for each time step. This is why CNOS is about
ten times faster than ETICFOS for short maturity options. However, for
longer T, we can see that CNOS requires more time steps in order to
achieve approximately, the same error as ETICFOS. Basically, the opera-
tor splitting technique used here is composed of two split steps. In the
first one, we need to solve the BS PDE in time and the second step consists
of enforcing the American constraint through the addition of a penalty
term. While ETI performs the first step exactly in time even for large
V = (4V(2N+1)−V(2N))/3, CN will need more time steps to be accurate
over large T. Thus for longer maturity, the computational speed is almost
the same for both methods.
We note that the ETI scheme solves the PDE part exactly in time and
therefore, it is unconditionally stable. Furthermore, adding a penalty
term which is always bounded as
p(τ)
 ≤rE will not affect the sta-
bility of our method. Hence, we can use an extrapolation method to
improve the accuracy of the ETICF method. We show in Table 4.3, the
absolute extrapolated error at S0 for pricing European, American and Bar-
rier options under Black-Scholes, Merton’s jump-diffusion, Heston’s SV
and Bates SVJ models. The cpu(s) required to calculate the most accurate
extrapolated value V = (4V(2N+1) −V(2N))/3, is also given.

Table 4.2
Error for American put option with σ = 0.4,r = 0.07,δ = 0.03,E = 100. The errors for the options (ε) and (ε) for
m = 720 and m = 800 respectively are also shown
ETICFOS
CNPSOR
CNOS
M
Error
Rate
CPU (s)
Error
Rate
CPU (s)
Error
rate
CPU (s)
T = 0.5 uniform grid.
50
0.0308
–
0.1880
0.0306
–
0.8750
0.0307
–
0.0160
100
0.0079
1.9686
0.3280
0.0078
1.9816
2.9370
0.0076
1.9757
0.0320
200
0.0020
1.9985
0.5930
0.0019
2.0106
13.344
0.0019
2.0070
0.0620
400
4.64e−4
2.0841
1.1410
4.66e−4
2.0453
81.484
4.52e−4
2.1017
0.1100
800
9.26e−5
2.3252
2.2810
1.02e−4
2.1869
571.92
7.37e−5
2.6186
0.2190
ε = 6.69e −6
ε = 1.28e −7
ε = 2.10e −6
ε = 2.90e −7
ε = 3.53e −6
ε = 1.34e −7
reference values
V = 10.23868
 = −0.42294
 = 0.01437
T = 3.0 nonuniform grid.
45
0.0219
–
0.4220
0.0216
–
2.3280
0.0216
–
0.4530
90
0.0053
2.0379
0.7040
0.0051
2.0825
7.9540
0.0051
2.0852
0.7500
180
0.0013
1.9940
1.2970
0.0012
2.0875
37.140
0.0012
2.1446
1.3430
360
3.16e−4
2.0823
2.4370
2.62e−4
2.1955
232.95
2.02e−4
2.5127
2.4690
720
3.01e−5
3.3891
4.8750
2.92e−5
3.1656
1674.1
3.66e−5
2.4640
4.8120
ε = 2.63e −6
ε = 4.86e −8
ε = 2.82e −6
ε = 7.44e −8
ε = 5.88e −6
ε = 2.32e −7
reference values
V = 20.79322
 = −0.33145
 = 0.00630

Table 4.3
Extrapolated absolute error for pricing call options under different models
European
Barrier
American
Black–Scholes geometric Brownian motion model
Grid
Error
Ext.Err
Error
Ext.Err
Grid
Error
Ext.Err
26 × 1
0.0242
–
0.0287
–
26 × 29
0.0252
–
27 × 1
0.0060
2.56e-5
0.0072
6.46e-6
27 × 29
0.0064
1.18e-4
28 × 1
0.0015
1.78e-7
0.0018
2.90e-7
28 × 29
0.0016
3.33e-6
CPU(s)
0.0310
0.0310
1.8740
Merton’s jump-diffusion model
Grid
Error
Ext.Err
Error
Ext.Err
Grid
Error
Ext.Err
26 × 1
0.0207
–
0.0805
–
26 × 29
0.0458
–
27 × 1
0.0052
2.06e-5
0.0201
7.78e-5
27 × 29
0.0114
7.32e-5
28 × 1
0.0013
6.06e-7
0.0050
4.74e-6
28 × 29
0.0016
3.69e-5
CPU(s)
0.1250
0.1250
1.2340
Heston’s stochastic volatility model
Grid
Error
Ext.Err
Error
Ext.Err
Grid
Error
Ext.Err
24 × 25 × 1
0.0035
–
0.0031
–
24 × 25 × 26
0.0036
–
25 × 25 × 1
8.44e-4
5.81e-5
7.32e-4
7.31e-5
25 × 25 × 26
8.09e-4
1.06e-4
26 × 25 × 1
2.15e-4
3.42e-7
1.46e-4
4.99e-5
26 × 25 × 26
1.55e-4
6.26e-5
CPU(s)
3.6100
1.1560
5.0010
Bates’s stochastic volatility model
Grid
Error
Ext.Err
Error
Ext.Err
Grid
Error
Ext.Err
24 × 25 × 1
0.0056
–
0.0028
–
24 × 25 × 26
0.0035
–
25 × 25 × 1
0.0013
1.61e-5
5.92e-4
1.38e-4
25 × 25 × 26
7.88e-4
1.10e-4
26 × 25 × 1
3.15e-4
3.21e-7
9.82e-5
6.66e-5
26 × 25 × 26
1.49e-4
6.41e-5
CPU(s)
4.7350
3.8450
5.0120

86
Y. D. Tangman, R. Boojhawon, A. Gopaul and M. Bhuruth
101
100
10–1
10–2
10–3
Absolute error
10–4
10–5
101
100
10–1
10–2
10–3
Absolute error
10–4
10–5
100
10–1
10–2
10–3
Absolute error
10–4
10–5
101
102
103
m
104
Y=–1
Y=1.1
Y=1.8
Y=0.6
ETICGMY
O(m2)
101
102
103
m
104
101
102
103
m
104
101
102
103
m
104
101
100
10–1
10–2
10–3
Absolute error
10–4
10–5
ETICGMY
O(m2)
ETICGMY
O(m2)
ETICGMY
O(m2)
Figure 4.1
Convergence Rates of ETI for The CGMY Process With C = 0.5,
G = 10,M = 10
For the CGMY model, we use T = 0.5 and give the convergence plot
of a European call option in Figure 4.1 for various values of Y. For Kou’s
model (Y = −1), there is no need to split the integral domain near zero,
but for Y ∈(0,2), we need to make use of the quadrature used by Wang
et al. (2007) to obtain second-order convergence as seen in Figure 4.1.
Here, good convergence rates are observed because of the better tem-
poral accuracy of the ETI scheme and also because we did not require
any interpolation in S since the integro and PDE grids coincide. But, as
observed in Wang et al. (2007), the convergence decays as Y →2. Due to
space limitations, we do not report in detail on computed option prices
that have been seen to work well for the simple Richardson extrapolation
technique also.
The case Y = 0,σ = 0 results in the VG model (Madan et al. 1998),
and the PIDE becomes convectively dominated. Almendral and Oosterlee
(2006) suggested the use of a simple Lax–Wendroff update by adding the
diffusive term
τ
2

r −δ −1
2(σ 2 + ˆσ(z)) −κ(z)
2
Vxx(x,τ),

A General Efficient Framework for Pricing Options
87
Table 4.4
Convergence ratio for European under VG model, American and
barrier options
European VG
American (Y = 0.5)
Barrier (Y = 0.1)
M
Value
Ratio
Value
Ratio
Value
Ratio
25
0.3292
–
5.4351
–
7.2414
–
26
0.3795
–
6.0171
–
7.2758
–
27
0.3966
2.9357
6.1427
4.6353
7.2843
4.0390
28
0.4010
3.9509
6.1729
4.1520
7.2854
4.0586
29
0.4021
3.7236
6.1805
3.9737
7.2869
4.1226
210
0.4024
4.0399
6.1824
4.0181
7.2871
4.2661
Reference value
0.40239
6.18275
–
to obtain more accurate solutions. Another approach is to combine the
semi-Lagrangian discretization (d’Halluin et al. 2005; Wang et al. 2007).
However, we do not pursue this here and show in Table 4.4 that the Lax–
Wendroff update does improve the accuracy and convergence ratio. We
also give in the same table the convergence ratio for an American option
with the benchmark solution obtained by using the extrapolated FFT
method for Bermudan options (Lord et al. 2008). The convergence ratio
for a double knockout barrier at |x| = 0.5 is also included to show that
second order is achieved for infinite activity processes. This option has
not been priced before, and this is why we did not include any reference
value. The numerical results obtained for the large variety of models and
options characterizes the ETICF scheme as a method of choice for fast
option pricing.
4.6
Conclusion
The ETI framework is shown to be general and robust enough to price
a variety of options under various models used in literature. Using
a recently developed method for matrix functions, only four sparse
tridiagonal shifted linear systems are required to be solved to obtain accu-
rate option prices for European and barrier options. Together with an
operator splitting technique, American options can also be priced very
efficiently. Further accuracy improvements can be obtained by using
a simple Richardson extrapolation formula. With a general, fast, and
accurate pricing algorithm, the calibration task can now be performed.
Current investigations include a study of other spatial discretization
such as finite element and spectral methods (Tangman et al. 2008b)

88
Y. D. Tangman, R. Boojhawon, A. Gopaul and M. Bhuruth
together with ETICF. The implementation of efficient solvers for shifted
linear systems (Frommer 2003; Simoncini 2003) is primordial, especially
for multidimensional option pricing problems.
Acknowledgments
The authors thank Thomas Schmelzer for his help concerning the
efficient computations of the matrix exponentials for Merton’s model.
References
Almendral, A. and Oosterlee, C. W. (2006) “Highly Accurate Evaluation of Euro-
pean and American Options under the Variance Gamma Process,” Journal of
Computational Finance, 10 (1): 21–42.
Almendral, A. and Oosterlee, C. W. (2007) “Accurate Evaluation of European
and American Options under the CGMY Process,” SIAM Journal of Scientific
Computing, 29 (1): 93–117.
Almendral, A. and Oosterlee, C. W. (2005) “Numerical Valuation of Options with
Jumps in the Underlying,” Applied Numerical Mathematics, 53 (1): 1–18.
Ashi, H. A., Cummings, L. J., and Matthews, P. C. (2009) “Comparison of
Methods for Evaluating Functions of a Matrix Exponential,” Applied Numerical
Mathematics, 59 (3–4): 468–486.
Bates, D. (1996) “Jump and Stochastic Volatility: Exchange Rate Processes Implicit
in Deutsche Mark in Options,” Review of Financial Studies, 9 (1): 69–107.
Beylkin, G., Keiser, J. M., and Vozovoi, L. (1998) “A New Class of Time Discretiza-
tion Schemes for the Solution of Nonlinear PDEs,” Journal of Computational
Physics, 147 (2): 362–387.
Black, F. and Scholes, M. (1973) “The Pricing of Options and Other Corporate
Liabilities,” Journal of Political Economics, 81 (3): 637–654.
Carr, P. and Mayo, A. (2007) “On the Numerical Evaluation of Option Prices in
Jump Processes,” The European Journal of Finance, 13 (4): 353–372.
Carr, P., Geman, H., Madan, D. B., and Yor, M. (2002) “The Fine Structure of Assets
Returns: An Empirical Investigation,” Journal of Business, 75 (2): 305–332.
Cont, R. and Tankov, P. (2004) Financial Modelling with Jump Processes, Boca Raton,
Fla.: Chapman & Hall/CRC Press.
Cont, R. and Voltchkova, E. (2005) “Finite Difference Methods for Option Pricing
in Jump-Diffusion and Exponential Lévy Models,” SIAM Journal of Numerical
Analysis, 43 (4): 1596–1626.
Cox, S. M. and Matthews, P. C. (2002) “Exponential Time Differencing for Stiff
Systems,” Journal of Computational Physics, 176 (2): 430–455.
d’Halluin, Y., Forsyth, P. A. and Vetzal, K. R. (2005) “Robust Numerical Meth-
ods for Contingent Claims under Jump Diffusion Processes,” Journal Numerical
Analysis, 25 (1): 87–112.
Frommer, A. (2003) “BiCGStab (l) for Families of Shifted Linear Systems,”
Computing, 70 (2): 87–109.

A General Efficient Framework for Pricing Options
89
Heston, S. (1993) “A Closed-Form Solution for Options with Stochastic Volatility
with Applications to Bond and Currency Options,” Review of Financial Studies,
6 (2): 327–343.
Ikonen, S. and Toivanen, J. (2004) “Operator Splitting Methods for American
Option Pricing,” Applied Mathematical Letters, 17 (7): 809–814.
Kou, S. (2002) “A Jump Diffusion Model for Option Pricing,” Management Science,
48 (8): 1086–1101.
Leisen, D. and Reimer, M. (1996) “Binomial Models for Option Valuation-
Examining and Improving Convergence,” Applied Mathematical Finance, 3 (4):
319–349.
Lord, R., Fang, F., Bervoets, F., and Oosterlee, C. W. (2008) “A Fast and Accurate
FFT-Based Method for Pricing Early-Exercise Options under Lévy Processes,”
SIAM Journal of Scientific Computing, 30 (4): 1678–1705.
Madan, D. B., Carr, P., and Change, E. (1998) “The Variance Gamma Process and
Option Pricing,” European Finance Review, 2 (1): 79–105.
Merton, R. C. (1976) “Option Pricing when the Underlying Stocks Are Discontin-
uous,” Journal of Financial Economics, 3 (1–2): 125–144.
Minchev, B. V. and Wright, W. M. (2005) “A Review of Exponential Integrators for
First Order Semi-Linear Problems,” Technical Report: Norwegian University of
Science and Technology, Trondheim, Norway.
Moler, C. and Van Loan, C. (2003) “Nineteen Dubious Ways to Compute the
Exponential of a Matrix, Twenty-Five Years Later,” SIAM Review, 45 (1):
3–49.
Schmelzer, T. and Trefethen, L. N. (2007) “Evaluating Matrix Functions for
Exponential Integrators via Carathéodory–Fejér Approximation and Contour
Integrals,” Electronic Transactions on Numerical Analysis, 29 (2): 1–18.
Simoncini, V. (2003) “Restarted Full Orthogonalization Method for Shifted Linear
Systems,” BIT Numerical Mathematics, 43 (2): 459–466.
Tangman, D. Y., Gopaul, A., and Bhuruth, M. (2008a) “A Fast High-Order Finite
Difference Algorithm for Pricing American Options,” Journal of Computational
Applied Mathematics, 222 (1): 17–29.
Tangman, D. Y., Gopaul, A., and Bhuruth, M. (2008b) “Exponential Time Inte-
gration and Chebychev Discretisations Schemes for Fast Pricing of Options,”
Applied Numerical Mathematics, 58 (9): 1309–1319.
Tangman, D. Y., Peer, A. A. I., Rambeerich, N., and Bhuruth, M. (2010) “Fast Sim-
plified Approaches to Asian Option Pricing,” Journal of Computational Finance,
to appear.
Trefethen, L. N., Weideman, J. A., and Schmelzer, T. (2006) “Talbot Quadratures
and Rational Approximations,” BIT Numerical Mathematics, 46 (3): 653–670.
Wang, I. R., Wan, J. W., and Forsyth, P. A. (2007) “Robust Numerical Valua-
tion of European and American Options under the CGMY Process,” Journal
of Computational Finance, 10 (4): 31–69.
Yan, G. and Hanson, F. B. (2006) “Option Pricing for a Stochastic-Volatility Jump-
Diffusion Model with Log-Uniform Jump-Amplitudes,” Proceedings of American
Control Conference: 2989–2994.

5
Unconditional Mean, Volatility,
and the FOURIER–GARCH
Representation
Razvan Pascalau, Christian Thomann and Greg N. Gregoriou
5.1
Introduction
Recently there has been an upsurge interest in modeling the nonstation-
arities present in the volatility of financial data. The clustering and the
persistence of volatility of asset returns have been well documented. The
IGARCH model of Engle and Bollerslev (1986), for instance, describes
in a parsimonious way the high persistence in the conditional volatility
of stock returns while the underlying process remains strictly stationary.
Alternatively, Granger (1980) and Granger and Joyeux (1980) model the
long memory or the long-range dependence of a series of log returns as
a fractionally integrated process to allow the autocorrelation functions
to decay very slowly, in a fashion characteristic of stock returns. How-
ever, seminal papers from Granger and Joyeux (1986), Lamoureux and
Lastrapes (1990), and, more recently, from Diebold and Inoue (2001),
Mikosch and Starica (2004), Starica and Granger (2005), and Perron
and Qu (2007) argue that the high persistence close to unit root and
long memory both in the first and the second moments may actually be
caused by structural changes in the level or slope of an otherwise locally
stationary process of the long-run volatility. Diebold and Inoue (2001)
argue that this is due to switching regimes in the data. Mikosch and
Starica (2004) provide theoretical evidence that changes in the uncon-
ditional mean or variance induce the statistical tools (e.g., sample ACF,
periodogram) to behave the same way they would if used on stationary
long-range dependent sequences. Starica and Granger (2005) also deliver
evidence against global stationarity. Finally, Perron and Qu (2007) con-
clude that the Standard & Poor’s (S&P) 500 return series is best described
90

FOURIER–GARCH Representation
91
as a stationary short memory process contaminated by mean shifts.
These results imply that a good model for volatility should take into
account the possibility of a time-varying unconditional second moment
and, possibly, of a time-varying first moment as well.
Engle and Rangle (2008) propose the Spline-GARCH to model long-
run volatility non-parametrically using an exponential quadratic spline.
However, they do so only for the second moment. Further, Starica and
Granger (2005) use step functions to approximate nonstationary data
locally by stationary models. They apply their methodology to the S&P
500 series of returns covering a period of seventy years of market activity
and find that most of the dynamics are concentrated in shifts of the
unconditional variance.
However, these models pose several problems. While spline functions
may lead to overfitting, step functions may not give smooth approxima-
tions. Even major breaks, such as the stock-market crash of 1929 and the
oil-price shocks of the 1970s did not display their full impact immedi-
ately. Structural changes may take longer to extinguish, which suggests
they need to be modeled as smooth or gradually changing processes.
These arguments motivate the present study to propose a new approach
to model the long-run first and second moments as smooth processes.
This chapter denotes the new process Fourier–GARCH because it uses
the flexible Fourier transform of Gallant (1981) (i.e., an expansion of a
periodic function in terms of an infinite sum of sines and cosines). The
basic model can be extended to incorporate the long-run volatility in
the mean model. Flexible Fourier transforms have been used in the liter-
ature to approximate nonlinear structures in several ways. For instance,
Becker et al. (2001) use Fourier transforms to model inflation and money
demand as having smooth changes in the intercept. Also, Enders and Lee
(2006) and Becker et al. (2006) propose new unit root and stationarity
tests that use the Fourier approximation to model the unknown shape of
the structural breaks in macro time series. The main advantage is that the
issue of estimating the shape and location of the breaks reduces to select-
ing the proper frequency of the Fourier sine and cosine terms. A section
below details how Fourier transforms can be used to approximate various
types of breaks.
The study applies the new model to several of the largest stocks from
S&P 500 to estimate volatility persistence in stock returns. Based on the
discussion above, this chapter considers several competing models. The
basic Fourier–GARCH model specifies a constant first moment, while
the second moment changes smoothly over time. A first extension to
the basic model allows both the first and the second moments to vary

92
R. Pascalau, C. Thomann and G. N. Gregoriou
over time, while a second extension incorporates the long-run volatility
in the model for the mean. This chapter checks for each model the sum
of the estimated coefficients in the equation for conditional volatility to
assess the so-called long-memory effect. The results show that allowing
only the second moment to vary over time does not significantly reduce
the persistence effect. In fact, the difference between this model and
the simple GARCH(1,1) is negligible. However, the extended model that
allows the first moment to vary over time as well reduces the persistence
effect by more than half of the value suggested by GARCH(1,1). The evi-
dence suggests that the persistence effect seen in stock returns is mainly
a result of the misspecification of the model for the mean.
This chapter is structured as follows. Section 5.2 discusses in more
detail the performance of the Fourier series to approximate various types
of structural breaks. Section 5.3 introduces the basic Fourier–GARCH
model and its extensions. Section 5.4 discusses the empirical estimates
of the long memory effect using four different models, and Section 5.5
concludes.
5.2
Nonlinear trend approximation with
Fourier transforms
The general approach to account for breaks is to approximate them using
dummy variables. However, this approach has several undesirable con-
sequences. First, one has to know the exact number and location of
the breaks. These are not usually known and therefore need to be esti-
mated. This, in turn, introduces an undesirable preselection bias (see
Maddala and Kim 1998). Second, use of dummies suggests sharp and
sudden changes in the trend or level. However, for low-frequency data
it is more likely that structural changes take the form of large swings
in the data which cannot be captured well using only dummies. Breaks
should therefore be approximated as smooth processes (see Leybourne
et al. 1998 and Kapetianos et al. 2003).
Flexible Fourier transforms, originally introduced by Gallant (1981),
are able to capture the essential characteristics of one or more structural
breaks using only a small number of low-frequency components. This is
true because a break tends to shift the spectral density function toward
frequency zero. Below is illustrated the ability of Fourier transforms to
capture nonlinear trends.
Using a simple form for the mean model, one can allow the intercept
µt to be a deterministic function of time:
yt = µt + γt + εt
(5.1)

FOURIER–GARCH Representation
93
where the drift term is written as:
µt = c0 + s
k=1cksin
2πkt
T

+ s
k=1dk cos
2πkt
T

; s ≤T/2
(5.2)
In the above formulation, εt is a stationary disturbance term with vari-
ance σ 2s , s is the maximum number of frequencies, k is a particular
frequency, and T is the total number of observations. The drift term
represents the Fourier approximation written as a deterministic function
of sine and cosine terms. Note that by imposing αk = βk = 0 one gets the
constant mean or trend return specification. In contrast to other possi-
ble series expansions (e.g., Taylor series), the Fourier expansion has the
advantage of acting as a global approximation (see Gallant 1981). This
property is obtained even if one specifies a small number of frequencies.
In fact, Enders and Lee (2006) argue that a large value of s in a regres-
sion framework uses many of the degrees of freedom and leads to an
overfitting problem.
To illustrate the approximation properties of a Fourier series, this
chapter considers first a single frequency in the data-generating process
(DGP):
µt = c0 + ck sin
2πkt
T

+ dk sin
2πkt
T

(5.3)
where k is the single frequency selected in the approximation, and ck
and dk represent the magnitudes of the sinusoidal terms.
This study considers several possible patterns for the occurrence of a
break. Thus, for T = 500, this chapter simulates one break, two breaks,
and trend breaks both in the middle and toward the extremes. This
chapter illustrates the cases for temporary, permanent, and reinforc-
ing breaks. We display the results below in panels 1 through 9 (i.e.,
Figure 5.1). As in Enders and Lee (2006), Panels 1 and 2 illustrate approx-
imations for breaks toward the end of a series. In Panel 3, the series has a
temporary, though long-lasting break. Panels 4 and 5 display permanent
breaks in opposite directions while in Panel 6 the breaks are in the same
direction. Finally, Panels 7–9 depict breaks in the intercept and slope of a
trending series. This chapter estimates the coefficients of the sinusoidal
terms by performing a simple regression of yt on µt and a time trend.
One can draw several conclusions based on the visual inspection of the
graphs. First, a single frequency k = 1 or two cumulative frequencies n = 2
can approximate a large variety of breaks. Second, the Fourier transform
approximates well even when the breaks are asymmetric (see Panels 1
and 2). Third, a Fourier series works best when the break is smooth over

94
R. Pascalau, C. Thomann and G. N. Gregoriou
Series:
; One frequency:
; Two cumulative frequencies:
Panel 1: Break at T/2
100
200
300
400
500
–0.5
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Panel 2: Break at 3T/4
100
200
300
400
500
–1.0
–0.5
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Panel 3: Temporary break
100
200
300
400
500
–0.6
0.0
0.6
1.2
1.8
2.4
3.0
3.6
4.2
Panel 4: Breaks in opposite directions
100
200
300
400
500
–0.5
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
Panel 5: Short breaks in opposite
directions
100
200
300
400
500
–0.5
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Panel 6: Reinforcing breaks
50 100 150 200 250 300 350 400 450 500
–1
0
1
2
3
4
5
Panel 7: Trend breaks
100
200
300
400
500
0
50
100
150
200
250
300
350
400
Panel 8: Change in level and slope
100
200
300
400
500
–100
0
100
200
300
400
500
600
700
800
Panel 9: Temporary change in
level and slope
100
200
300
400
500
–250
0
250
500
750
1000
1250
1500
Figure 5.1
Approximation of structural breaks with Fourier Transforms
time, which means it may not be suited for abrupt and sharp breaks
of short duration (see Panel 5). An additional frequency of k = 2 can
improve the fit in this situation. Interested readers are referred to Enders
and Lee (2006) and Becker et al. (2006) who have a longer discussion on
the properties of the Fourier approximations. The next section introduces
a new model to approximate long-run volatility.
5.3
A new model for unconditional volatility
As the introductory part suggested, the simple GARCH (1,1) may not be
appropriate because it implies a long-run level of the volatility which
is constant. However, previous research regarding the presence of vari-
ous shifts in stock returns suggests that structural changes in the second
moment induce global nonstationarity. This invalidates the use of the
simple GARCH(1,1). It is known that breaks shift the spectral density
function toward frequency zero. This indicates that the frequencies

FOURIER–GARCH Representation
95
Fractions of Pi
0.0
0.2
0.4
0.6
0.8
1.0
0.1
1.0
10.0
100.0
0
25
50
75
100 125 150 175 200
–1.00
–0.75
–0.50
–0.25
0.00
0.25
0.50
0.75
1.00
CORRS
PARTIALS
Figure 5.2
Left: Sample spectrum of absolute returns of S&P 500; Right: Sample
ACF of returns of S&P 500
to be used are toward the low end of the spectrum (see Enders and
Lee 2006). A simple visual inspection of the autocorrelation function
and periodogram of absolute returns of S&P 500 confirms this fact
(see Figure 5.2).
As you can note from the graphs in Figure 5.2, the most important
frequencies that have an impact on the absolute returns are at the low
end of the sample spectrum, which is indicative of structural breaks.
Both graphs confirm the presence of long memory in financial returns –
slow decay with lags still significant at the 200th lag. These findings
suggest the use of the following model whose aim is to capture various
unknown shifts in long-run volatility. This chapter denotes it the basic
Fourier–GARCH:
rt = µ + υt

utht, where υt
It−1 ∼iid(0,1)
(5.4)
ht = (1 −α −β) + α (rt−1 −µ)2
ut−1
+ βht−1
(5.5)
ut = exp

a0 +
s

k=1

ak sin
2πkt
T

+ bk cos
2πkt
T

; s ≤T/2
(5.6)
The model preserves the parsimony of the GARCH(1,1) model while
it allows the unconditional expectation of the volatility to be a func-
tion of time and of cycles of different frequencies. A simple extension
allows the unconditional mean to be a function of time as well: higher
unconditional variance certainly requires higher unconditional mean.

96
R. Pascalau, C. Thomann and G. N. Gregoriou
The time-varying first moment is also approximated using a Fourier
representation:
µt = c0 +
s

k=1
ck sin
2πkt
T

+
s

k=1
dk cos
2πkt
T

(5.7)
Given its flexible setup, the Fourier–GARCH captures both short- and
long-run dynamics. Note that:
E(rt −µ)2 = E(υ2
t utht) = utE(ht) = ut
(5.8)
The study uses an exponential representation of the Fourier transform
to ensure its positivity. Goodness-of-fit measures such as the BIC or
AIC criteria are employed to choose the proper number of frequencies
exogenously. They are computed as follows:
AIC = −lnL + 2n,
L = −
T

t=1

ln(htut) + (r −µ)2
htut

(5.9)
BIC = −lnL + nln(T),
L = −
T

t=1

ln(htut) + (r −µ)2
htut

(5.10)
Here, n denotes the number of parameters estimated by the model. The
advantage of using the AIC and BIC criteria is that they include a penalty
for the additional estimated parameters. Throughout the estimation, the
criteria employ only integer frequencies.
The advantage of using a time-varying first moment for a sample of
forty years of daily data of S&P 500 absolute returns is highlighted in
Figure 5.3.
Note the better fit of the second model, which augments the basic
Fourier–GARCH representation with a time-varying intercept as in
equation (5.7). However, given the presumption that a higher long-
run volatility requires a higher long-run return, this chapter proposes
the Fourier–M model which includes the unconditional time-varying
volatility in the equation for the mean:
rt = γ ut + υt

utht, where υt
It−1 ∼iid(0,1)
(5.11)
In this way, both the first and the second moment change over time
while the underlying model ensures a parsimonious representation.

FOURIER–GARCH Representation
97
Panel 1: Fourier-Garch(1,1) with constant
first moment
1963 1969 1975 1981 1987 1993 1999 2005
0.000
0.008
0.016
0.024
0.032
0.040
0.048
0.056
0.064
LCVAR
LUVAR
LCVAR
LUVAR2
Panel 2: Fourier-Garch(1,1) with varying
first moment
1963 1969 1975 1981 1987 1993 1999 2005
0.000
0.008
0.016
0.024
0.032
0.040
0.048
0.056
0.064
Figure 5.3
Panel 1:
LCVAR = conditional volatility;
LUVAR = unconditional
volatility;
Panel 2:
LCVAR = conditional volatility;
LUVAR2 = unconditional
volatility
One way to assess the persistence or long memory in stock returns is
to compute the sum of the slope coefficients in conditional volatility. If
the sum is close to one, then conditional volatility is said to be almost
integrated and it displays very slow time decay. However, the support
for long memory is weakened if one finds that a changing first and/or
second moment is responsible for the persistence effect. If the sum of
the coefficients is significantly less than one after one accounts for shifts
in the unconditional mean or volatility, then one can conclude that
the volatility process is stationary but suffers from structural shifts (see
Perron and Qu 2007).
A sample of daily returns on S&P 500 from 01/02/1963 to 02/30/2005
illustrates this discussion. The best representation is the one that specifies
a single frequency both for the mean and for the unconditional volatility
(see Figure 5.4).
Note the slow and gradual increase of long-run volatility from the
1960s until the 1980s. Also, note that the estimated long-run volatility of
the 1990s is lower than the one for previous decades, which is consistent
with market facts.

98
R. Pascalau, C. Thomann and G. N. Gregoriou
Panel 1: Fourier-Garch(1,1) with varying
first moment
1963 1969 1975 1981 1987 1993 1999 2005
0.000
0.008
0.016
0.024
0.032
0.040
0.048
0.056
0.064
LCVAR
LUVAR2
Panel 2: Long-Run Volatility
1963 1969 1975 1981 1987 1993 1999 2005
0.0065
0.0070
0.0075
0.0080
0.0085
0.0090
0.0095
0.0100
LUVAR2
Figure 5.4
Panel 1: LCVAR – conditional volatility, LUVAR2 – unconditional
volatility; Panel 2: LUVAR2 – unconditional volatility
5.4
Model validation and persistence effects
This chapter uses several representative stocks of S&P 500 to assess the
long-memory effect of stock returns using the new models. The first
12 stocks of the index are selected according to their market percent-
age participation as of March 2005. Table 5.1 shows their ticker, sector
classification and percentage of total assets.
The data has been obtained from the Center of Research in Security
Prices made available through the WRDS database. The longest sample
period available is 01/02/1926–12/30/2005 and corresponds to Exxon,
IBM, Chevron, Philip Morris, and General Electric. Other stock returns
have shorter sample periods (i.e., Procter & Gamble from January 2, 1929
onwards, Pfizer and Johnson & Johnson from 1944, and Intel from 1972;
while the rest start in 1986). For each stock return, the study chooses
exogenously an integer or cumulative frequencies according to the AIC
and BIC criteria. According to Enders and Lee (2006), a frequency greater
than 5 uses many of the degrees of freedom and leads to an overfitting
problem.

FOURIER–GARCH Representation
99
Table 5.1
Market capitalization of 13 companies on S&P 500 as of February 28,
2006
Ticker
Issue name
Sector
% of Total assets
XOM
Exxon Mobil Corp
Energy
3.19
GE
General Electric Co.
Industrials
3
MSFT
Microsoft Corp.
Industrials
2.12
C
Citigroup Inc
Financials
2.03
PG
Procter & Gamble
Consumer staples
1.73
PFE
Pfizer Inc.
Health care
1.67
AIG
American Intl. Group Inc.
Financials
1.49
JNJ
Johnson & Johnson
Health care
1.48
MO
Altria Group Inc.
Consumer staples
1.29
CVX
Chevron Corp New
Energy
1.09
IBM
International Business Mach.
Information
technology
1.09
INTC
Intel Corp
Information
technology
1.07
Table 5.2 displays the results from applying the AIC and BIC criteri-
ons to identify the best in sample fitting model. The above mentioned
criterions indicate that in most cases the best representation is the basic
Fourier-Garch(1,1) model. The coefficients of the sine and cosine terms
with up to 5 frequencies are significant at the 5% level both for the
basic and for the extended models. However, given that in the model
for the mean each additional frequency requires the estimation of two
more coefficients, the additional penalty increases the values of the
AIC and BIC criterions relative to the ones for the basic model. This
is not surprising given that the BIC criterion favors more parsimonious
representations. Several exceptions to the finding above are notewor-
thy. In the case of Microsoft for instance, both criterions select the
Fourier-M model to be the optimal representation. Also, the Fourier-M
model gives the best fit for Chevron as well. Note that the basic Fourier-
Garch(1,1) and the Fourier-M models have very close values for the BIC
and SBC criterions. This is true because they estimate the same num-
ber of parameters (i.e. six coefficients). In rest, the increased penalty
due to the additional coefficients that are estimated in the models with
two or more cumulative frequencies is greater than the better fit that
is obtained. Therefore, the single frequency representation fits the data
best for all models. Figures 5.5 through 5.7 show several graphs of the
conditional and long-run volatilities obtained using both a constant and
a time varying first moment. Note that for all series the long run volatility
changes smoothly over time.

Table 5.2
AIC, BIC, and the log-likelihood
(a)
AIG
Chevron
Citigroup
Exxon
General Electric
Frequencies
AIC
BIC
(ℓ)
AIC
BIC
(ℓ)
AIC
BIC
(ℓ)
AIC
BIC
(ℓ)
AIC
BIC
(ℓ)
1
0.989
40.287
11.011
0.044
47.720
11.956
1.609
40.512
10.391
0.003
47.679
11.997
0.048
47.724
11.952
2
4.987
61.217
11.013
4.035
67.603
11.965
5.634
57.505
10.386
4.005
67.574
11.995
4.076
67.643
11.924
3
8.987
79.275
11.013
8.034
87.495
11.965
9.617
74.456
10.383
8.005
87.465
11.995
8.046
87.506
11.954
4
12.987
97.332
11.013
12.035
107.387
11.965
13.614
91.420
10.387
12.005
107.357
11.995
12.047
107.398
11.953
5
16.987
115.390
11.013
16.035
127.278
11.965
17.615
108.389
10.385
16.005
127.249
11.995
16.046
127.290
11.954
1 (mean shifts)
5.132
61.363
10.868
4.645
68.213
11.354
5.936
57.807
10.064
5.488
69.056
10.512
4.375
67.943
11.625
1 (Fourier-M)
1.002
43.174
10.985
0.039
47.714
11.961
4.757
43.660
7.243
0.008
47.683
11.992
0.074
47.750
11.926
(b)
IBM
Intel
Johnson & Johnson
Microsoft
Pfizer
Frequencies
AIC
BIC
(ℓ)
AIC
BIC
(ℓ)
AIC
BIC
(ℓ)
AIC
BIC
(ℓ)
AIC
BIC
(ℓ)
1
0.028
47.704
11.972
1.142
48.818
10.858
0.334
46.290
11.66
1.532
40.631
10.468
0.361
46.396
11.639
2
4.026
65.594
11.974
5.153
61.383
10.847
4.334
65.609
11.666
5.629
57.762
10.371
4.379
65.759
11.621
3
8.027
87.487
11.973
9.153
79.441
10.847
8.334
84.927
11.666
9.615
74.558
10.385
8.362
86.087
11.638
4
12.026
107.378
11.974
13.152
97.498
10.848
12.334
104.246
11.666
13.507
91.706
10.493
12.361
104.431
11.639
5
16.026
127.270
11.974
17.150
115.554
10.850
16.333
123.565
11.666
17.539
108.771
10.461
16.360
123.775
11.639
1 (mean shifts)
4.930
68.498
11.070
5.366
61.597
10.634
5.257
66.532
10.743
5.696
57.829
10.304
6.810
68.190
9.190
1 (Fourier-M)
0.029
47.705
11.971
1.162
43.335
10.838
0.335
46.291
11.665
1.494
40.593
10.506
0.364
46.399
11.635
(c)
Phillip-Morris
Procter & Gamble
Frequencies
AIC
BIC
(ℓ)
AIC
BIC
(ℓ)
1
0.074
47.750
11.926
0.043
47.718
11.957
2
4.077
67.645
11.923
4.041
67.240
11.959
3
8.076
87.537
11.924
8.041
87.039
11.959
4
12.077
107.428
11.923
12.041
106.839
11.959
5
16.077
127.320
11.924
16.041
126.639
11.959
1 (mean shifts)
4.611
68.179
11.389
4.962
68.161
11.038
1 (Fourier-M)
0.079
47.755
11.921
0.047
47.446
11.953

FOURIER–GARCH Representation
101
Panel 1: Fourier-Garch(1,1) with constant
first moment
1973 1977 1981 1985 1989 1993 1997 2001 2005
0.00
0.01
0.02
0.03
0.04
0.05
0.06
Panel 2: Fourier-Garch(1,1) with varying
first moment
1973 1977 1981 1985 1989 1993 1997 2001 2005
0.00
0.01
0.02
0.03
0.04
0.05
0.06
LCVAR
LUVAR2
LCVAR
LUVAR1
Panel 1: Fourier-Garch(1,1) with constant
first moment
1926 1935 1944 1953 1962 1971 1980 1989 1998
0.00
0.01
0.02
0.03
0.04
0.05
0.06
LCVAR
LUVAR1
Panel 2: Fourier-Garch(1,1) with varying
first moment
1926 1935 1944 1953 1962 1971 1980 1989 1998
0.00
0.01
0.02
0.03
0.04
0.05
0.06
LCVAR
LUVAR2
Figure 5.5
Conditional and unconditional volatility for AIG and Chevron

102
R. Pascalau, C. Thomann and G. N. Gregoriou
Panel 1: Fourier-Garch(1,1) with constant
first moment
1926 1935 1944 1953 1962 1971 1980 1989 1998
0.00
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0.08
0.09
LCVAR
LUVAR1
Panel 2: Fourier-Garch(1,1) with varying
first moment
1926 1935 1944 1953 1962 1971 1980 1989 1998
0.00
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0.08
0.09
LCVAR
LUVAR2
Panel 1: Fourier-Garch(1,1) with constant
first moment
1926 1935 1944 1953 1962 1971 1980 1989 1998
0.00
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0.08
LCVAR
LUVAR1
Panel 2: Fourier-Garch(1,1) with varying
first moment
1926 1935 1944 1953 1962 1971 1980 1989 1998
0.00
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0.08
LCVAR
LUVAR2
Figure 5.6
Conditional and unconditional volatility for Exxon and General
Electric

FOURIER–GARCH Representation
103
Panel 1: Fourier-Garch(1,1) with constant
first moment
1926 1936 1946 1956 1966 1976 1986 1996
0.000
0.012
0.024
0.036
0.048
0.060
0.072
0.084
LCVAR
LUVAR1
LCVAR
LUVAR2
Panel 2: Fourier-Garch(1,1) with varying
first moment
1926 1936 1946 1956 1966 1976 1986 1996
0.000
0.012
0.024
0.036
0.048
0.060
0.072
0.084
Panel 1: Fourier-Garch(1,1) with constant
first moment
1973 1977 1981 1985 1989 1993 1997 2001 2005
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0.08
0.09
0.10
LCVAR
LUVAR1
Panel 2: Fourier-Garch(1,1) with varying
first moment
1973 1977 1981 1985 1989 1993 1997 2001 2005
0.01
0.02
0.03
0.04
0.05
0.06
0.07
0.08
0.09
0.10
LCVAR
LUVAR2
Figure 5.7
Conditional and unconditional volatility for IBM and Intel

104
R. Pascalau, C. Thomann and G. N. Gregoriou
Table 5.3
Persistence of financial volatility
M0: GARCH(1,1)
M1: Fourier-
Garch(1,1)
with
constant
mean
M2: Fourier-
Garch (1,1)
with time-
varying
mean
M3: Fourier-M
(1,1)
Companies
α + β
α + β
α + β
α + β
AIG
0.98024
0.98034
0.97753
0.96798
Chevron
0.98704
0.98373
0.75108
0.96577
Citigroup
1.00104
0.90388
0.57667
0.99360
Exxon
0.98333
0.95727
0.54307
0.95894
General
Electric
0.99256
0.99013
0.80713
0.99261
IBM
0.99180
0.96291
0.51090
0.95930
Intel
0.99185
0.99206
0.64818
0.98175
Johnson &
Johnson
0.95222
0.88250
0.01595
0.90133
Microsoft
0.06820
0.10247
0.22565
0.09550
Pfizer
0.97707
0.90421
0.40066
0.85240
Phillip-
Morris
0.99877
0.99251
0.75108
0.98887
Procter &
Gamble
0.99595
0.96786
0.29293
0.96698
Next, this chapter investigates whether the selected returns display the
long-memory property that is usually observed in financial data. To this
end, the study estimates four competing models:
1. the common GARCH(1,1) developed by denoted M0;
2. the basic Fourier–GARCH(1,1) with constant first moment, denoted
M1;
3. the Fourier–GARCH(1,1) with a time-varying first moment, denoted
M2;
4. the Fourier-M (1,1) with long-run volatility in the mean, denoted M3.
Table 5.3 shows the results. Clearly, model M2 provides the best reduc-
tion of the persistence effect for most series. For 10 of the 12 stock returns
considered, the long-memory effect is dramatically reduced in many
instances by half or even more (i.e., General Electric, Pfizer, IBM, Philip
Morris, Chevron, Intel, Procter & Gamble, Exxon, Johnson & Johnson,
and Citigroup).
Note that the basic representation (i.e. the M1 model above) has
only little impact on overall persistence in the short-run volatility. In

FOURIER–GARCH Representation
105
most cases, its persistence is only slightly lower than the one of the
GARCH(1,1) representation. This is surprising given that this model gives
the best fit according the AIC and BIC criteria in 10 out of the 12 stocks
considered. Note that model M3 clearly outperforms model M1 in terms
of reduced long-memory effect as well. The main conclusion is that
allowing only for the second moment to vary over time is not enough
to account for the strong persistence effect observed in financial returns.
However, in contrast to the basic model, a time-varying first moment
in the equation for the mean reduces significantly the persistence in
short-run volatility.
5.5
Conclusion
This chapter proposes a new model to estimate the short- and long-run
dynamics in financial data that takes into account the possibility of a
time-varying first and second moment. The flexible Fourier transform of
Gallant (1981) approximates the unknown date and shape of any struc-
tural break in the first and second moment as smooth processes. The
study shows that Fourier series are able to approximate a wide variety of
breaks of an unknown form. The basic Fourier–GARCH representation
modifies the popular GARCH (1,1) to include a time-varying uncondi-
tional variance. This chapter proposes two extensions to the basic model.
The first extension specifies a time-varying first moment while the second
extension includes the long-run volatility in the equation for the mean.
The results suggest that persistence still remains significant in the short-
run volatility for the basic model. However, the so-called long-memory
effect disappears if one includes a time-varying first moment in the model
for the mean. This suggests that conditional volatility persistence is an
artifact of the misspecification of the model for the mean.
References
Becker, R., Enders, W., and Hurn, S. (2001) “Modelling Structural Change in
Money Demand Using a Fourier-Series Approximation,” Research Paper Series
67, Quantitative Finance Research Centre, University of Technology, Sydney.
Becker, R., Enders, W., and Lee, J. (2006) “A Stationarity Test in the Presence of
an Unknown Number of Smooth Breaks,” Journal of Time Series Analysis, 27 (3):
381–409.
Bollerslev, T. (1987) “A Conditionally Heteroskedastic Time Series Model for Spec-
ulative Prices and Rates of Return,” The Review of Economics and Statistics, 69
(3): 542–547.
Diebold, F. X. and Inoue, A. (2001) “Long Memory and Regime Switching,” Journal
of Econometrics, 105 (1): 131–159.

106
R. Pascalau, C. Thomann and G. N. Gregoriou
Enders, W. and Lee, J. (2006) “Testing for a Unit Root with a Nonlinear Fourier
Function,” Mimeo, University of Alabama, Tuscaloosa, Ala.
Engle, R. and Bollerslev, T. (1986) “Modeling the Persistence of Conditional
Variances,” Econometric Reviews, 5 (1): 1–50.
Engle, R. F. and Rangel, J. G. (2008) “The Spline-Garch Model for Low-Frequency
Volatility and its Global Macroeconomic Causes,” Review of Financial Studies,
21 (3): 1187–1222.
Gallant, R. (1981) “On the Basis in Flexible Functional Form and an Essentially
Unbiased Form: The Flexible Fourier Form,” Journal of Econometrics, 15 (2):
211–353.
Granger, C. W. J. (1980) “Long Memory Relationships and the Aggregation of
Dynamic Models,” Journal of Econometrics, 14 (2): 227–238.
Granger, C. W. J. and Joyeux, R. (1980) “An Introduction to Long Memory Time
Series and Fractional Differencing,” Journal of Time Series Analysis, 1 (1): 15–30.
Granger, C. W. J. and Joyeux, R. (1986) “Modeling the Persistence of the
Conditional Variances: A Comment,” Econometric Reviews, 5 (1): 51–56.
Kapetianos, G., Shin, Y., and Snell, A. (2003) “Testing for a Unit Root in the
Nonlinear STAR Framework,” Journal of Econometrics, 112 (2): 359–379.
Lamoureux, C. G. and Lastrapes, W. D. (1990) “Persistence in Variance, Structural
Change, and the Garch Model,” Journal of Business and Economic Statistics, 8 (2):
225–234.
Leybourne, S., Newbold, P., and Vougas, D. (1998) “Unit Roots and Smooth
Transitions,” Journal of Time Series Analysis, 19 (1): 83–97.
Maddala, G. and Kim, I.-M. (1998) Unit Roots, Cointegration and Structural Change,
Cambridge: Cambridge University Press.
Mikosch, T. and Starica, C. (2004) “Non-stationarities in Financial Time Series,
the Long Range Dependence and the IGARCH Effects,” Econometrics 0412005,
EconWPA.
Perron, P. and Qu, Z. (2007) “An Analytical Evaluation of the Log-Periodogram
Estimate in the Presence of Level Shifts,” Boston University – Economics
Department, wp2007-044.
Starica, C. and Granger, C. (2005) “Nonstationarities in Stock Returns,” The Review
of Economics and Statistics, 87 (3): 503–522.

6
Essays in Nonlinear Financial
Integration Modeling: The
Philippine Stock Market Case
Mohamed El-Hedi Arouri and Fredj Jawadi
6.1
Introduction
Emerging stock markets are one of the best areas for investment and have
become more accessible to investors in recent years thanks to successive
efforts to open up these markets. These markets not only offer investors
generous returns and opportunities but also enable them to better diver-
sify their portfolios. These efforts recently led to a significant increase in
capital flows toward the region and a rise in emerging market capitaliza-
tion that reached around 20 percent of world market capitalization in
2000. This also has a considerable impact on the emerging stock market
industry. Indeed, in addition to the significant increase in the finan-
cial integration of emerging markets into the world market (Bekaert and
Harvey 1995), the adjustment dynamics of their asset prices is almost
simultaneously governed by internal, regional, and external economic,
financial, and political factors (Adler and Qi 2003; Carrieri et al. 2007).
In this study, we focus on emerging Asian markets. Indeed, a large
number of these markets have launched a series of reforms, includ-
ing their modernization and liberalization. Consequently, integration
of Asian stock markets has emerged as an important body of literature
(Bekaert and Harvey 1995; Gérard et al. 2003; Carrieri et al. 2007). How-
ever, the intensity and efficiency of these reforms and the degree of
financial integration differ from one country to another. In addition, the
internal and external factors pertaining to the financial markets in this
region are also very different, suggesting perhaps multiple asymmetrical
regimes of financial integration and segmentation which are interesting
to apprehend and investigate.
107

108
M. El-Hedi Arouri and F. Jawadi
The main contribution of this chapter is to investigate whether emerg-
ing Asian stock markets are integrated into the world market or not. We
choose to focus our analysis on the Philippine case for diverse reasons.
First, the Philippines is characterized by an overvalued exchange rate, a
fragile banking system, and insufficient reserves with regard to the mone-
tary mass (Sachs et al. 1996), suggesting that it may benefit considerably
from further financial integration with the world market. Second, the
financial markets in the Philippines have only recently, although contin-
uously, been growing, and the Philippines’ trade-openness ratio reached
an average of 119 percent over the past decade. This is essentially due to
the smooth functioning of the ASEAN (Association of South-East Asian
Nations), created in 1965 by five countries (Indonesia, Malaysia, the
Philippines, Singapore, and Thailand). Furthermore, in order to promote
its integration into other international stock markets, the Philippine
market underwent several reforms: liberalization and privatization (in
1985) and the introduction of ADR and country funds (in 1989). The
Philippine stock market is thus expected to be better integrated during
the post-liberalization period than it was during the period prior to the
opening up of its market.
Several previous studies in the literature have focused on financial
integration in Asian and Latin emerging stock markets. However, the
authors’ conclusions are not unanimous, and their results are often het-
erogeneous, perhaps because they define financial integration differently
and test it also via different tools. For example, Bekaert and Harvey (1997)
and Carrieri et al. (2007) studied Asian and Latin American emerging
markets (the Philippines and other emerging countries) using a time-
varying partially integrated CAPM. Their main conclusion is that the
majority of emerging markets are partially integrated in the world mar-
ket and that their degrees of integration are time varying. However, these
results strongly depend on the validity of the CAPM.
Other studies focus on stock market integration in developed and
emerging countries, using cointegration techniques. Masih and Masih
(1997) show that the newly industrialized Asian countries of Honk Kong,
Singapore, Taiwan, and South Korea share a long-term relationship with
the developed markets (the USA, Japan, the UK, and Germany). More
recently, Masih and Masih (2001) found significant interdependencies
between the established OECD and the emerging Asian markets. Lim
et al. (2003) examined the linkages between stock markets in the Asian
region over the period 1988–2002 using nonparametric cointegration
techniques and found a common force that brings these markets together
in the long run. Similar results are suggested by Wang and Nguyen

Essays in Nonlinear Financial Integration Modeling
109
Thi (2007) and Iwatsubo and Inagaki (2007). Ratanapakon and Sharma
(2002) studied the short- and long-term relationships in five regional
stock indices from the pre-Asian crisis and the crisis period and found
that the degree of linkage increased during and after the crisis period.
More recently, Phylaktis and Ravazzolo (2005) investigated stock market
interactions of Pacific Basin countries over the period 1980–1998 and
showed that although linkages have increased in recent years, there is
still room for long-term gains when investing in Pacific Asian markets. By
contrast, Bilson et al. (2000) show that the regional integration among
stock markets in South Korea, Taiwan, Thailand, the Philippines, and
Malaysia is faster than their integration within the international mar-
ket. Roca and Selvanathan (2001) show neither short- nor long-term
linkages among the stock markets of Australia, Hong Kong, Singapore,
and Taiwan. Phylaktis and Ravazzolo (2000) also identify a lack of co-
movements during the 1980s for the free stock markets of Singapore and
Hong Kong. More interestingly, other recent studies show that the level
to which markets are integrated or segmented is not fixed but changes
gradually over time.
To sum up, this literature review shows some interdependencies
between emerging and developed stock markets, suggesting further evi-
dence of financial integration. However, it also suggests the difficulty
of arbitraging between the two polar cases of strict segmentation and
perfect integration. In fact, on the one hand, dynamic approaches
show that the financial integration dynamic can be assimilated with a
continuous process combining these two extreme cases as well as a con-
tinuum of intermediate states. This is even more valid for emerging stock
markets which are generally characterized by ongoing liberalization
processes.
On the other hand, analysis of the findings of previous studies shows
that they define financial integration differently and that they have
checked it using different methods. Indeed, they have often used lin-
ear modeling tools, even though some of them argue with the fact that
the financial integration seems to be time-varying and has tended to
increase over the past decade because of the rise in the number of inter-
national investors, the increase in new information and communication
technologies and market liberalization. However, usual linear techniques
yield invariant adjustment and are thus not usually suitable to repro-
duce dynamic and time-varying financial integration. Consequently, the
linear framework used in most previous studies fails to capture certain
types of financial integration which are time-varying, asymmetrical and
nonlinear, and persistent and irregular.

110
M. El-Hedi Arouri and F. Jawadi
Thus, in this chapter, we consider markets to be integrated if they
share a common trend and move together. Using linear and nonlinear
modeling, we study the stock price adjustment dynamic and financial
integration of the Philippine market into the world market. In particu-
lar, we propose using nonlinear econometric tools given by nonlinear
error correction models to investigate the Philippines’ emerging stock
market integration. Checking the hypothesis of financial integration
within nonlinear modeling enables the integration dynamics to be asym-
metrical, discontinuous, time-varying, and nonlinear. Moreover, the
nonlinear cointegration methodology not only allows integration to be
studied in a more general setting, taking into account the asymmetry,
persistence, and nonlinearity that characterizes the dynamics of stock
price adjustment, but also enables us to check and specify the degree of
integration in every regime as well as in the short and long run. This is
also interesting for a better understanding of the dynamism of finan-
cial markets and decision-making concerning international portfolio
diversification in the Asian region.
The article is organized as follows. Section 6.2 will briefly present the
econometric methodology. In Section 6.3, we will discuss the empirical
results, and Section 6.4 will conclude.
6.2
Checking financial integration within
nonlinear modeling
According to several stylized facts (financial crises and stock crashes) and
some previous studies, the stock integration dynamics may be nonlinear.
This nonlinearity can be differently explained by market imperfections:
information and segmentation barriers (Bekaert and Harvey 1995), dis-
tinct transaction costs (Anderson 1997), heterogeneous shareholders’
expectations (De Grauwe and Grimaldi 2006), etc. This implies an ongo-
ing financial integration process and a nonlinear time-varying correcting
mechanism which is adequately reproduced using the class of nonlinear
cointegration models. Among the nonlinear cointegration models, we
suggest using two nonlinear error correction models (NECM): the expo-
nential switching transition error correction model (ESTECM) and the
nonlinear error correction model-rational polynomial (NECM-RP) which
we briefly present in the following section.1
Formally, let yt and xt be respectively the stock prices of the Philippines
and the world market, where the long-run relationship corresponds to:
yt = α0 + α1xt + zt
(6.1)
where zt designates the residuals of the long-run relationship.

Essays in Nonlinear Financial Integration Modeling
111
The ESTECM is defined as follows:
yt = α0 + ρ1zt−1 +
q

i=0
βixt−i +
p

j=1
δjyt−j + ρ2zt−1
×

1 −exp

−γ

zt−1 −c
2
+ εt
(6.2)
Where ρ1,ρ2,γ , and c are respectively the adjustment term in the first and
the second regimes, the transition speed, and the threshold parameter.
The ESTECM enables the financial integration process to be different
per regime, thus defining two extreme regimes when the exponential
transition function nears the unity, and a central regime when it is
equal to zero, as well as a continuum of intermediate states. The tran-
sition between these regimes is assumed to be smooth and gradual,
and this specification is recommended to capture temporal paths gov-
erned by smooth changing regimes, accounting for a slow adjustment
mechanism.
The NECM-RP is defined as follows:
yt = α0 + ρ1zt−1 +
q

i=0
βixt−i +
p

j=1
δjyt−j + ρ2 ×

zt−1 + a
3 + b

zt−1 + c
2 + d
+ µt
(6.3)
Where: a, b, c, and d are the parameters of the rational polynomial
function.
As suggested by Chaouachi et al. (2004), the NECM-RP is a more
general nonlinear model which can take into account several poten-
tial sources of nonlinearities (i.e. abrupt changes in adjustment speeds,
the impact of negative and positive shocks on stock price adjustment,
multiple long-run attractors, etc.).
In practice, we carry these out to specification to examine the inte-
gration process of the Philippines’ stock market in several steps. First,
we apply the usual unit root tests (augmented Dickey–Fuller [ADF] and
Phillips–Perron [PP] tests) to check the integration order of the stock
price series. Second, we check the mixing hypothesis, applying KPSS
and R/S tests on the residual term (ˆzt) to test the nonlinear cointegra-
tion hypothesis. Third, accepting the mixing hypothesis suggests that
stock prices are nonlinearly mean-reverting and allows our NECM to be
estimated through the nonlinear least squares (NLS) method.

112
M. El-Hedi Arouri and F. Jawadi
6.3
Empirical results
6.3.1
Data and preliminary analysis
Using monthly stock market indices from the Philippines and the world
market over the period December 1987 to January 2008, obtained from
Morgan Stanley Capital International (MSCI), which we express in US
dollars, we first test the order of integration of these series by ADF and PP
tests and show that both indices are I (1). Second, based on the matrix
of bilateral correlation between the Philippines and the world-market
indices, that we compute over two subperiods (January 1988–November
1994 and December 1994–January 2008) and over the period of study,2
we show that the bilateral correlations between the Philippines and
world stock markets are higher after 1994. This finding indicates that
the Philippines’ stock market has become more integrated in recent years
(see Table 6.1).
Third, we test the symmetry, normality hypotheses, and our find-
ings, presented in Table 6.2, suggest further evidence against normality
and symmetry for the Philippines’ stock returns since the Skewness, and
Kurtosis coefficients are statistically significant.
This may be assimilated with a sign of nonlinearity in the dynamics
of the Philippine stock market. We then estimate the relation (6.1) and
we test for the presence of a unit root in the residuals (zt) using the ADF
test. The hypothesis of linear cointegration is not rejected, suggesting
further evidence of integration between the Philippine and the world
Table 6.1
Matrix of bilateral correlations
Series
RPHI
RMSCI
Subperiod 1: January 1988–November 1994
RPHI
1.00
0.33
RMSCI
0.33
1.00
Subperiod 2: December 1994, January 2008
RPHI
1.00
0.44
RMSCI
0.44
1.00
All the period: January 1988–January 2008
RPHI
1.00
0.40
RMSCI
0.40
1.00
Note: This table shows bilateral correlations between the
stock returns of the world and the Philippines before
and after the 1990s. RMSCI and RPHI are respectively
the stock returns of the world and the Philippines.

Essays in Nonlinear Financial Integration Modeling
113
Table 6.2
Descriptive statistics and normality test
Series
Mean
Std. Dev. Maximum Minimum Skewness Kurtosis
Jarque-Bera
(Probability)
Philippines
0.0050
0.0927
0.3601
−0.3465
−0.0727
4.8155
33.31(0.0)
MSCI World
Index
0.0053
0.0398
0.1055
−0.1444
−0.5733
3.8673
20.75(0.0)
Note: This table presents the descriptive statistics between the stock returns of the world and
the Philippine stock markets.
stock markets. However, since several previously cited studies and our
correlation analysis indicated that the degree of financial integration is
time-varying, we propose testing this hypothesis using nonlinear coin-
tegration tests which are more powerful than linear cointegration tests.
6.3.2
Nonlinear cointegration tests for financial
stock market integration
To check for nonlinear cointegration between the Philippine and the
world stock market and to test the hypothesis of time-varying financial
integration, we apply two “mixing” tests which are more robust than the
ADF test: the KPSS and the R/S tests. Both tests check the null hypoth-
esis of “mixing” against its “nonmixing” alternative. For the KPSS, we
retain the values suggested by Schwert (1989) for the truncation parame-
ter: l4 = int

4
	
T
100

 1
4

and l12 = int

12
	
T
100

 1
4

where T is the number
of observations,3 while we retain the value of Andrews (1991) concern-
ing the choice of q for the R/S test which corresponds to the following
formula: qt = [KT], where KT =
	
3T
2

 1
3 	
2 ˆρ
1−ˆρ2

 2
3, [KT] = int(KT) and ˆρ
is the first-order autocorrelation coefficient. We summarize the results
obtained in Table 6.3. The null hypothesis of mixing is retained only at
10 percent according to the R/S test. According to the KPSS test, it is also
accepted but only for the second value of the truncation parameter (l12).
Accepting the mixing hypothesis confirms the hypothesis of nonlinear
cointegration and implies that the Philippine stock price is nonlinearly
mean-reverting toward the world market at 10 percent (perhaps over the
past decade). In a final step, we estimate both NECM: the ESTECM and
the NECM-RP.
6.3.3
Estimation of NECM
We estimate both NECMs following the steps proposed by Escribano and
Mira (2002) and Van Dijk et al. (2002). Firstly, we specify linear models

114
M. El-Hedi Arouri and F. Jawadi
Table 6.3
Mixing tests
KPSS
R/S
l4
l12
Andrews
0.72*
0.29
1.6*
Note: This table presents the results of mixing
tests.
* denotes the rejection of the null hypothesis
at the 5 percent significance level.
Table 6.4
NECM estimation results for the Philippines
Coefficients
ESTECM (1,1)
NECM-RP
α0
−0.0021 (−0.37)
0.0009 (0.90)
ρ1
−0.1815 (−1.02)
−0.0086 (−0.81)
ρ2
0.1624 (0.91)
−0.0053* (−2.329)
β0
0.2177* (3.55)
0.2086* (3.59)
δ1
0.9228* (6.82)
0.9224* (6.83)
γ
625.07 (0.49)
–
γ × σzt−d
219.53
–
C
−0.3319* (−16.36)
–
ADFGLS
−15.85
−15.85
R/S
2.5*
1.5
σNECM/σLECM
0.99
0.95
Note: This table presents the estimation results of NECM for the
Philippines. The values in brackets are the t-statistic of nonlinear esti-
mators.
* denotes the significance at 5 percent.
and determine the number of lags (p) for the NECMs on the basis of
the information criteria and the autocorrelation functions. The optimal
value retained is p = 1. We then estimate the NECMs by the NLS method
and we report the results in Table 6.4. Our findings show several con-
clusions regarding the hypothesis of financial integration. Firstly, the
current MSCI world index parameter is statistically significant, suggest-
ing the presence of statistical dependence of the Philippine stock market
on the world market (external factor). The first AR parameter is also sig-
nificant, which suggests that its index depends on its past tendencies
(local and internal factor). Secondly, our results show that ESTECM is not
appropriate to the Philippines. Neither the exponential function param-
eters nor the nonlinear adjustment terms are statistically significant and

Essays in Nonlinear Financial Integration Modeling
115
0.5
1.0
1.5
2.0
2.5
3.0
3.5
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.1
0.2
0.3
0.4
0.5
0.6
0.7
Figure 6.1
Histogram of the rational polynomial function for the Philippines
the residuals of the estimated model are not mixing. We therefore reject
this nonlinear representation for the Philippines.
The dynamics of the Philippine stock market is better apprehended
using the NECM-RP. This model, estimated under the following restric-
tions: a = c = d = 1 and b = 0, as in Chaouachi et al., (2004) in order to
simplify the algorithm convergence, seems more suited to capturing the
type of asymmetry inherent to the Philippines’ stock market. Overall, the
estimation results of this model suggest significant correlation between
the Philippine and the world stock markets.
More interestingly, from Figure 6.1, the persistence, asymmetry
and smoothness associated with the Philippine stock price adjustment
dynamics seem to be captured by the NECM-RP. Indeed, while the first
adjustment term is negative but statistically non-significant, the second
one is statistically significant and the sum of the two adjustment terms
is also negative suggestion a nonlinear and asymmetric mean reversion
in the stock price of the Philippines. More particularly, this means that
in the first regime the Philippine stock price may deviate from the equi-
librium and the stock market of the Philippine be segmented but a mean
reversion is activated when stock price deviations exceed some threshold.
In order to highlight the pattern of nonlinear and asymmetric behav-
ior characterizing this Asian stock market, we plot the histogram of
the rational polynomial function in accordance with the estimated mis-
alignment values (ˆzt−1). This confirms the rejection of normality and
linearity hypotheses. The NECM-RP also captures the asymmetry in the
integration process between the emerging and world markets. Indeed,
this figure shows a bimodal density and even several modes with two
modes of unequal heights. The presence of these unequal modes suggests
significant and extreme stock price deviations between the regimes of
segmentation and integration. This asymmetry in the distribution of the

116
M. El-Hedi Arouri and F. Jawadi
rational polynomial function also reflects the persistence and smooth-
ness of the integration process of this emerging stock market into the
world market. This asymmetry and persistence in the pace of the Philip-
pine stock market integration may perhaps be explained by the different
theoretical arguments discussed in the body of this chapter. Finally, our
findings are validated via misspecification tests that highlight that the
residuals of NECM-RP are mixing and stationary.
6.4
Conclusion
We investigated the hypothesis of time-varying financial integration
between the Philippine and the world stock markets over three decades
in a nonlinear framework. Our findings suggest further evidence of
asymmetrical and nonlinear cointegration between these markets. They
confirm the hypothesis of time-varying financial integration for the
Philippines and highlight the contribution of nonlinear error correc-
tion models in studying this hypothesis. Indeed, these tools enable the
extreme cases of financial integration to be reproduced (perfect integra-
tion and strict segmentation) as well as a continuum of intermediate
states relative to partial integration that characterizes most emerging
stock markets. This study may be extended by testing this approach for
other emerging and developed stock markets.
Notes
1. The NECM-RP methodology is based on the theorem of Escribano and Mira
(2002), whereas that of the ESTECM is developed by Van Dijk et al. (2002), who
adapt the methodology to the threshold models, thus defining a particular
kind of threshold cointegration model for which the adjustment is relatively
smooth and asymmetric. For more details regarding nonlinear cointegration
models, see Dufrénot and Mignon (2002).
2. See table1 in the appendices in which we also present all the empirical results.
3. Int [.] denotes the interior part.
References
Adler, M. and Qi, R. (2003) “Mexico’s Integration into the North American Capital
Market,” Emerging Economic Review, 4 (2): 91–120.
Anderson, H. M. (1997) “Transaction Costs and Nonlinear Adjustment towards
Equilibrium in the US Treasury Bill Markets,” Oxford Bulletin of Economics and
Statistics, 59 (4): 465–484.
Andrews, D. (1991) “Heteroscedasticity and Autocorrelation Consistent Covari-
ance Matrix Estimation,” Econometrica, 59 (3): 817–858.

Essays in Nonlinear Financial Integration Modeling
117
Beakert, G. and Harvey, C. (1997) “Emerging Equity Market Volatility,” Journal of
Financial Economics, 43 (1): 29–77.
Bekaert, G. and Harvey, C. (1995) “Time Varying World Market Integration,”
Journal of Finance, 50 (2): 403–444.
Bekaert, G., Harvey, C., and Ng, A. (2005) “Market Integration and Contagion,”
Journal of Business, 78 (1): 39–69.
Bilson, C., Hooper, V., and Jaugietis, M. (2000) “The Impact of Liberalisation and
Regionalism upon Capital Markets in Emerging Asian Economies,” International
Finance Review, 1 (1): 219–255.
Carrieri, F., Errunza, V., and Hogan, K. (2007) “Characterizing World Market Inte-
gration through Time,” Journal of Financial and Quantitative Analysis, 41 (2):
511–540.
Chaouachi, S., Dufrénot, G., and Mignon V. (2004) “Modelling the Misalign-
ments of the Dollar-Sterling Real Exchange Rate: A Nonlinear Cointegration
Perspective,” Economics Bulletin, 3 (19): 1–11.
De Grauwe, P. and Grimaldi, M. (2006) “Heterogeneity of Agents, Transaction
Costs and the Exchange Rate,” Journal of Economic Dynamics and Control, 29 (4):
691–719.
Dufrénot, G. and Mignon, V. (2002) Recent Developments in Nonlinear Cointegration
with Applications in Macroeconomics and Finance, Boston, Mass.: Kluwer.
Escribano, A. and Mira, S. (2002) “Nonlinear Error Correction Models,” Journal of
Time Series Analysis, 23 (1): 509–522.
Gerard, B., Thanyalakpark, K., and Batten, J. (2003) “Are the East Asian Markets
Integrated? Evidence from the ICAPM,” Journal of Economics and Business, 55
(2): 585–607.
Iwatsubo, K., and Inagaki, K. (2007) “Measuring Financial Market Contagion
Using Dually-Traded Stocks of Asian Firms,” CEI Working Paper Series No. 14,
Institute of Economic Research, Hitotsubashi University, Tokyo, Japan.
Lim, K., Lee, H., and Liew, K. (2003) “International Diversification Benefits in
Asian Stock Markets: A Revisit,” Mimeo, Lebuan School of International Business
and Finance, Sabah, Malaysia.
Lo, A. W. (1991) “Long-Term Memory in Stock Market Prices,” Econometrica, 59
(5): 1279–1313.
Masih, A. and Masih, R. (1997) “A Comparative Analysis of the Propagation of
Stock Market Fluctuations in Alternative Models of Dynamic Causal Linkages,”
Applied Financial Economics, 7 (1): 59–74.
Masih, A. and Masih, R. (2001) “Long and Short Term Dynamic Causal Transmis-
sion amongst International Stock Markets,” Journal of International Money and
Finance, 20 (4): 563–587.
Phylaktis, K. and Ravazzolo, F. (2000) “Stock Prices and Exchange Rate Dynamics,”
Mimeo, City University Business School, London.
Phylaktis, K. and Ravazzolo, F. (2005) “Stock Market Linkages in Emerging
Markets: Implication for International Portfolio Diversification,” Journal of
International Markets and Institutions, 15 (2): 91–106.
Ratanapakon, O. and Sharma, S. (2002) “Interrelationships among Regional Stock
Indices,” Review of Financial Economics, 11 (1): 91–108.
Roca, E. and Selvanathan, E. (2001) “Australian and the Three Little Dragons:
Are Their Equity Markets Interdependent?” Applied Economic Letters, 8 (3):
203–207.

118
M. El-Hedi Arouri and F. Jawadi
Sachs, J., Tornell, A., and Velasco, A. (1996) “Financial Crises in Emerging Markets:
The Lessons from 1995,” Brookings Papers on Economic Activity, 1: 147–198.
Schwert, G. W. (1989) “Tests for Unit Roots: A Monte Carlo Investigation,” Journal
of Business and Economic Statistics, 7 (2): 147–159.
Van Dijk, D., Teräsvirta, T., and Franses, P. H. (2002) “Smooth Transition Autore-
gressive Models: A Survey of Recent Developments,” Econometric Reviews, 21
(1): 1–47.
Wang, K. M. and Nguyen Thi, T. B. (2007) “Testing for Contagion under Asym-
metric Dynamics: Evidence from the Stock Markets between US and Taiwan,”
Physica A, 376 (15): 422–432.

Part II
Term Structure Models


7
A Macroeconomic Analysis of the
Latent Factors of the Yield Curve:
Curvature and Real Activity
Matteo Modena
7.1
Introduction
Examining the relation between yields at different maturities is crucial
for both macroeconomists and financial economists. From a macro-
economic perspective, the short rate is the policy instrument under
the control of the monetary authority; however, from a financial per-
spective, movements in short-term rates are analyzed to forecast longer
yields’ dynamics, since yields on long-term bonds are the expected aver-
age of risk-adjusted future spot rates. Moreover, the dynamics of the
term structure (TS) is influenced both by monetary policy actions and
by expectations about policy announcements; while, on the other hand,
economists infer the future path of macro variables from different shapes
of the yield curve.
Including macro variables in TS models is a quite recent phenomenon;
in this chapter we focus on the interpretation of curvature which has
been mostly ignored by previous analysis.
We consider the US bond market between March 1987 and December
2007, thus focusing on a sample characterized by price stability and a rel-
atively homogeneous monetary regime: explicit interest-rate targeting.
Data evidence suggests that almost all TS movements can be summa-
rized by few underlying factors, namely level, slope, and curvature. The
terminology refers to the effect that a shock to these unobservable vari-
ables exerts on the shape of the yield curve (Litterman and Scheinkman
1991). When interest rates of all maturities change by the same amount,
the yield curve is subject to a level shock; hence, a perturbation of this
kind causes a parallel shift of the entire yield curve. A shock to the slope
121

122
M. Modena
exerts different intensity on the maturity spectrum of interest rates. A
positive slope shock decreases short rates more than long rates, enlarging
the spread and steepening the yield curve. Finally, a positive curvature
shock increases yields at medium-term maturities, impressing a more
accentuated hump-shaped form to the yield curve. For its peculiar effect
on the maturity field, curvature has been labeled the butterfly factor.
An important strand of literature has recently focused on the macro-
economic interpretation of these factors. The existing empirical literature
associates the level to some measures of inflation. Rudebusch and Wu
(2004), as well as Bekaert et al. (2005), suggest level reflecting the infla-
tion rate targeted by the monetary authority, also known as the long-run
equilibrium inflation rate. Dewachter et al. (2006) provide evidence that
the level is an indicator of the central tendency of inflation. There is also
general consensus about the interpretation of the slope, which is believed
to be a monetary policy factor. Rudebusch and Wu (2004) provide evi-
dence that the slope factor tracks a fitted Taylor-type monetary policy
rule; Bekaert et al. (2005) relate the slope to monetary policy shocks. A
negative slope shock reduces the spread flattening TS, that is, what gen-
erally occurs when monetary policy tightens. More controversial seems
to be the interpretation of curvature. It has been argued that curvature
is either related to monetary policy shocks (Bekaert et al. 2005) or to the
real stance of monetary policy1 (Dewachter et al. 2006), or, eventually, to
the expected future path of interest rates (Giese 2008). Finally, Hordahl
et al. (2006) emphasize the effect of both inflation and output shocks on
medium-term maturities of the yield curve.
The empirical analysis worked out in this chapter finds its inspiration
in the diagrams of Figure 7.1, where grey shaded areas highlight National
Bureau of Economic Research recessions. The left panel plots the level
factor together with the CPI inflation rate and the slope factor with the
effective federal funds rate. The constant decline of the level might be due
either to the augmented credibility of the monetary regime or to the con-
solidation of the monetary authority’s reputation over time, or to both.
The central and the left panels of Figure 7.1 plot curvature together
with different measures of the business cycle. The series appear to dis-
play important co-movements; in particular, a visual inspection suggests
curvature dropping during slowdown in economic activity. Curvature
is positively related to the growth of industrial production (henceforth
IP), the Hodrick-Prescott filtered series of log IP, the log total capacity
utilization, the 6-month lagged growth rate in real consumption expen-
ditures. Finally, the dynamics of curvature is inversely related to that of
unemployment.

Latent Factors of the Yield Curve
123
86 88 90 92 94 96 98 00 02 04 06 08
level
CPI-inflation
slope
ffr
86 88 90 92 94 96 98 00 02 04 06 08
curvature
IP growth
IP gap (HP)
86 88 90 92 94 96 98 00 02 04 06 08
curvature
TCU (ln)
real cons. growth (-6)
unemployment
Figure 7.1
Curvature and macroeconomic variables
Notes: Level: level factor of the TS; slope: slope factor of the TS; CPI inflation:
consumer price index rate of change; ffr: effective federal funds rate; curvature:
curvature factor of the TS; IP growth: industrial production rate of growth; IP
gap (HP): Hodrick–Prescott filter gap of IP; real cons. growth: real consump-
tion expenditure rate of growth; TCU (ln): log series of total capacity utilization;
unemployment: unemployment rate.
In this chapter we provide evidence supporting the interpretation of
curvature as a cyclical indicator. We analyze curvature obtained from
both nominal and real TS. It has been argued (Harvey 1988; Chapman
1997) that there exists a significant relationship between real TS of inter-
est rates and consumption growth. Harvey (1988) provides evidence that
the expected real TS helps predict consumption growth. We find evidence
which is consistent with this story. In particular, despite the fact that cur-
vature from the nominal TS seems unrelated to consumption growth, we
find a significant inverse correlation between consumption growth and
curvature from real TS.

124
M. Modena
The rest of this chapter is organized as follows. Section 7.2 presents
a brief review of the literature. Data are presented in Section 7.3. In
Section 7.4 we outline the Nelson–Siegel latent factor model. The core of
the empirical analysis is contained in Sections 7.5, 7.6, and 7.7, where
we provide evidence to support the macro-interpretation of curvature. In
particular, Section 7.5 shows that curvature reflects the cyclical behavior
of the economy. In Section 7.6 we estimate a cyclical model for curvature,
while in Section 7.7 we develop and estimate a joint macroeconometric
model for curvature and real activity. Section 7.8 concludes.
7.2
Literature review
Arbitrage-free affine TS models have been largely adopted in the literature
to examine yield curve dynamics. Affine models are appealing since they
summarize TS information in few state variables, or latent factors, given
that most of TS movements are due to the effect of few components. Dai
and Singleton (2000) show that 99 percent of the variations in the yield
curve can be attributed to three factors. A second important group of
TS models is the Nelson–Siegel class, where yields are assumed to be a
function of factors through Laguerre functions of their maturities.
In a seminal article, Ang and Piazzesi (2003) show that incorporat-
ing macro factors into TS models improves the ability to forecast yields’
movements both in- and out-of-sample. Approximately 85 percent of
bond yields variation is attributable to the impact of macro factors; in
particular, macro variables explain movements at short- and medium-
term maturities (up to one year), while, movements of long-term yields
depends upon the effect of financial factors. Hordahl et al. (2006) sug-
gest that inflationary shocks mostly affect yields at medium maturities
increasing the TS curvature. Monetary policy shocks, instead, seem to
affect the short end of the yield curve; risk premia tend to respond to
output gap shocks. Rudebusch and Wu (2004) focus on only two latent
factors. The level turns put to be associated with the central bank’s long-
run inflation target, while the slope reflects the central bank’s reaction
function à la Taylor (1993).
Dewachter et al. (2004), using a continuous-time affine TS model find
that macroeconomic variables are not capable of explaining movements
at the long end of the yield curve. The variability of the long-term yields is
related to the central tendency of inflation. Medium-term interest rates,
from six months to two years, appear to respond to the real rate central
tendency; both observable and unobservable components influence risk
premia and bond excess returns.

Latent Factors of the Yield Curve
125
Diebold and Li (2003), Diebold et al. (2005), and Diebold et al. (2006)
employ the Nelson–Siegel interpolant to examine bond pricing. All these
studies document a good forecasting performance of the Nelson–Siegel
method. The most recent strand of literature has mixed the TS model
with modern macroeconomic theory, including latent factor dynam-
ics into New Keynesian general equilibrium frameworks. Bekaert et al.
(2005) develop a model combining structural New Keynesian macroe-
conomics and no-arbitrage TS theory. This line of research has been
followed by Wachter (2006) and Garcia and Luger (2007) who consider
a consumption-based equilibrium macro-finance model.
7.3
Data
All data have monthly frequency, from March 1987 to December 2007.
US yields data between March 1987 and December 1998 are from both
the McCulloch–Kown database (three, six, and 120 months) and from
the Fama–Bliss dataset (one, two, three, four, and five years). After
January 1999, all yields are from Datastream (ZCB yields). The effec-
tive federal funds rate is from the Federal Reserve Economic Data (FRED)
database. Table 7.1 reports some descriptive statistics of yields. The mean
is increasing with maturity suggesting a positive liquidity, or risk, pre-
mium. The standard deviation tends to be large at short to medium matu-
rities. Long-term yields are more persistent than short yields. The Jarque
and Bera suggest short-term yields being normally distributed around the
mean. Autocorrelations decay fast; the partial autocorrelation function
suggests the first-order autoregressive structure of yields. AR(1) regres-
sions for each yield return coefficients of approximately 0.98; however,
Table 7.1
Descriptive statistics of yields
Yields
maturity
ffr
3
6
12
24
36
60
120
mean
5.323
5.173
5.324
5.593
5.963
6.232
6.575
7.054
std dev
2.395
2.152
2.189
2.225
2.179
2.102
2.008
1.885
skew
0.088
0.009
0.049
0.129
0.391
0.556
0.825
1.004
kurt
2.598
2.720
2.871
3.030
3.377
3.542
3.875
4.041
JB norm
(0.323)
(0.631)
(0.856)
(0.668)
(0.012)
(0.000)
(0.000)
(0.000)
ADF
(0.141)** (0.082)** (0.093)** (0.064)** (0.051)** (0.051)** (0.040)** (0.021)**
KPSS
0.096**
0.089**
0.093**
0.095**
0.105**
0.115**
0.140**
0.166**
Notes: Normality and ADF tests: p-values in parenthesis. Exogenous included: **Intercept and
trend.

126
M. Modena
the Wald test rejects the null of unity coefficient. Both the augmented
Dickey–Fuller (ADF) and the Kwiatkowski–Phillips–Schmidt–Shin (KPSS)
suggest the series are stationary.2
Inflation is the annual change of the seasonally adjusted (SA) Con-
sumer Price Index for all urban consumers (FRED, Bureau of Labour
Statistics). M1 is the SA money stock from FRED (Federal Board of Gover-
nors). The monthly SA series of IP is from FRED. Different measures of the
output gap have been generated: the growth rate of log IP; the Hodrick–
Prescott filtered log IP; the Baxter–King and the Christiano–Fitzgerald
cyclical component of log IP. All cyclical indicators are highly correlated.
The SA civilian unemployment rate series is from FRED (Bureau of Labour
Statistics) as well as the SA real personal consumption expenditures
(Bureau of Economic Analysis).
7.4
The Nelson–Siegel factor model
The factor model is based on the approach pioneered by Nelson and
Siegel (1987). Their method has become increasingly popular among
financial economists for its relatively simple tractability and the fairly
good fit. The yield on a bond with maturity n is a polynomial function
of maturity:
y(n) = Lt + St
1 −exp{−λn}
λn

+ Ct
1 −exp{−λn}
λn
−exp{−λn}

(7.1)
Parameter λ governs the exponential decay.3 The first loading is a con-
stant, that is the unity coefficient multiplying Lt. The second loading
is an exponential function that starts at one and decays monotonically
toward zero. Finally, the third loading starts at zero, increases with matu-
rity n and then gradually decays approaching zero. The path followed by
these loadings allows interpreting them as level, slope, and curvature,
respectively.
Factors are stacked in the state vector Ft which is assumed to follow a
first-order VAR process. Differently from standard assumptions in canon-
ical affine TS models (Dai and Singleton 2000), we do not restrict the
transition matrix (NS) to be lower triangular. Hence, we allow the actual
value of each factor to depend on the first lag of all other factors. We con-
sider nine yields with maturities at one, three, six, 12, 24, 36, 48, 60, and
120 months, offering a dense representation of the maturity spectrum
domain. The transition equation of the state-space representation is:
Ft = µF + NS · Ft−1 + ωt,F
(7.2)

Latent Factors of the Yield Curve
127
ωt,F0 is i.i.d. Normal with zero mean and diagonal covariance matrix ().
The initial state vector F0 is orthogonal to the disturbances ωt,F0 of the
transition equation. The observation equation is:
yt = ℵFt + νt
(7.3)
The noise term is i.i.d. Normal with zero mean and variance σ 2. The white
noise transition disturbances νt are orthogonal to the initial state vector
F0. The measurement equation is:


y(1)
t
y(3)
t
...
y(120)
t


=


1
1 −exp(−λ)
λ
1 −exp(−λ)
λ
−exp(−λ)
1
1 −exp(−3λ)
3λ
1 −exp(−3λ)
3λ
−exp(−3λ)
...
...
...
1
1 −exp(−120λ)
120λ
1 −exp(−120λ)
120λ
−exp(−120 · λ)


·


Lt
St
Ct

+


νt,1
νt,3
...
νt,120


(7.4)
Estimations suggest that the cross-factor dynamics is weak. The first
autoregressive coefficients of the latent factors from the nominal TS are
0.98, 0.92, and 0.92 for Lt, St, and Ct respectively. The most persistent
factor becomes curvature when estimating the real TS; the autoregres-
sive coefficients of Lt, St, and Ct from the real TS are 0.93, 0.92, and 0.96
respectively.
7.5
Curvature and business cycle fluctuations
A better understanding of TS dynamics can be achieved by exploring the
macroeconomic underpinning of the yield curve. A certain consensus
exists on the interpretation of the level and the slope; however, so far
the interpretation of curvature is still controversial. In this section we
provide evidence suggesting that curvature is related to the fluctuations
of real activity. A curvature shock affects medium-term maturities of the
yield curve. A positive shock increases medium-term yields, while a neg-
ative shock generates an inverted hump-shaped yield curve, which is
sometimes observed in the data. Figure 7.1 shows that a significant neg-
ative curvature shock hits the yield curve each quarter preceding NBER

128
M. Modena
recessions. We point out that the relationship between curvature and the
economic cycle is not in contrast with previous evidence suggesting that
the TS slope is a good predictor of future economic activity (Stock and
Watson 1989; Estrella and Hardouvelis 1991).
Intermediate maturities have been largely ignored so far; thus, we try to
achieve a more general and comprehensive examination of TS dynamics.
Any shock affecting the short end of the yield curve, typically a mon-
etary policy shock, generates only a moderate and delayed reaction of
long yields, which are smooth and persistent, so that any shock affecting
the short end of TS can be considered a shock to the slope. Our interest
in medium maturities arises from the idea that medium-term yields rep-
resent an important link between the extremely dynamic short end and
the smooth long end of TS. In particular, we argue that the propagation
of shocks from the short to the long end of the yield curve reflects the
evolution of economic conditions over the business cycle.
The empirical macro-finance literature has proposed different the-
oretical measures of curvature.4 The correlation coefficients of these
components are positive but not always as high as expected. Cur-
vature is positively correlated to IP growth computed over different
horizons, from a quarter to three years. Curvature shares also impor-
tant co-movements with different measures of the output gap. Curvature
is inversely correlated with the variation of unemployment over time
(Figure 7.2).
A sharp reduction of curvature occurs immediately before economic
slowdowns. Data evidence seems to support the conjecture that curva-
ture is informative beyond the slope about business cycle fluctuations.
We speculate that negative shocks to curvature seem either to anticipate
or to accompany a decline in economic activity. Moreover, available
empirical evidence is consistent with the idea that the curvature effect
complements the transition from an upward-sloping to a flat yield curve.
It has been argued that the curvature factor is either related to mon-
etary policy shocks (Cho et al. 2005), or to the real stance of monetary
policy (Dewachter et al. 2006), or again to the expected future path of
interest rates (Giese 2007). In the following analysis we show that cur-
vature (Ct) is more closely related to the condition of the real economy
than to monetary variables. We thus estimate two different equations.
The monetary model (M) is:
Ct = δ0 + δ1ffrt,t−12 + δ2M1t,t−12 + δ3πt + εt,M
(7.5)
ffrt,t−12 is the annual change in the fed funds; M1t,t−12 is the annual
rate of growth of M1; πt represents CPI inflation. The real-variable model

Latent Factors of the Yield Curve
129
IP gap
0
2
4
6
8
10
–8
–6
–4
–2
0
2
4
unemployment
TCU (ln)
IP growth
–40
–20
0
20
40
60
NS curvature
NS curvature
NS curvature
NS curvature
NS curvature
NS curvature
unemployment growth
real cons. growth
Figure 7.2
Curvature and macroeconomic variables: scatter plots
Notes: NS curvature: curvature obtained with the Nelson–Siegel method; IP gap:
industrial production gap; unemployment: unemployment rate; TCU (ln): log
series of the total capacity utilization; IP growth: industrial production growth;
unemployment growth: rate of growth of the unemployment rate; real cons.
growth: real consumption expenditure rate of growth.
(R) relates curvature to some cyclical indicators:
Ct = ρ0 + ρ1IPt,t−12 + ρ2rct,t−12 + ρ3unt,t−12 + ρ4gapt−1 + εt,R
(7.6)
IPt,t−12 is the annual change of the seasonally adjusted IP; rct,t−12
represents the annual change in the real personal consumption expen-
ditures; unt,t−12 is the annual variation in unemployment; gapt is
either the Hodrick–Prescott or the Baxter–King de-trended series of log
IP. Estimation results are reported in Table 7.2.
To show our results are robust, the above equations have been esti-
mated both by OLS and by IV.5 OLS estimations have been performed
allowing different structures of the variance–covariance matrix of param-
eter estimates.6 Real consumption seems weakly related to curvature;
however, as we show later, consumption growth is significantly related
to curvature from the real TS. Evidence is in line with the idea that the
shape of the yield curve changes over the business cycle. We remark that

Table 7.2
Estimates of equations (7.5) and (7.6)
Curvature – Nominal TS
Model R – equation (7.6)
Model M – equation (7.5)
ρ0
ρ1
ρ2
ρ3
ρ4
χ2
δ0
δ1
δ2
δ3
χ2
OLS
−1.6088
0.7693
−0.2423
−0.1015
0.4909
−2.5250
0.8618
−0.1910
0.3713
WH
(0.236)
[−6.7]
(0.040)
[2.1]
(0.091)
[−2.7]
(0.010)
[−11]
(0.106)
[4.5]
55.54
(0.309)
[−8.2]
(0.279)
[3.1]
(0.021)
[−8.7]
(0.088)
[4.2]
108.1
HH (12)
(0.345)
[−4.6]
(0.846)
[0.9]
(0.190)
[−1.3]
(0.018)
[−5.4]
(0.265)
[1.8]
41.32
(0.947)
[−2.6]
(0.672)
[1.3]
(0.041)
[−4.6]
(0.230)
[1.6]
43.05
NW (18)
(0.352)
[−4.6]
(0.815)
[0.9]
(0.179)
[−1.3]
(0.018)
[−5.6]
(0.239)
[2.0]
35.05
(0.842)
[−2.9]
(0.630)
[1.3]
(0.038)
[−5.0]
(0.209)
[1.7]
48.07
s-HH
(0.827)
[−1.9]
(0.132)
[0.6]
(0.266)
[−0.9]
(0.026)
[−3.8]
(0.268)
[1.8]
24.88
(1.066)
[−2.5]
(0.737)
[1.2]
(0.054)
[−3.5]
(0.309)
[1.2]
20.31
R2
adj
0.48
R2
adj
0.38
ρ0
ρ1
ρ2
ρ3
ρ4
χ2
δ0
δ1
δ2
δ3
χ2
IV
−1.2650
0.7926
−0.3595
−0.1148
0.5345
−2.4316
0.7526
−0.2570
0.4067
(0.458)
[−2.7]
(0.816)
[−1.0]
(0.194)
[−1.8]
(0.017)
[−6.5]
(0.221)
[2.4]
38.45
(0.568)
[−4.2]
(0.498)
[1.5]
(0.036)
[−6.9]
(0.155)
[2.6]
42.17
R2
adj
0.47
R2
adj
0.35
Notes: Standard error in parenthesis; t-statistics in square brackets.

Latent Factors of the Yield Curve
131
the curvature effect is not incompatible with the fact that also the TS
slope varies across the business cycle.
A flat yield curve is usually interpreted as a sign of imminent reces-
sion since relative high short- to long-term rates are assumed to reflect
a severe monetary policy stance (Bernanke and Blinder 1992). On the
contrary, an upward-sloping yield curve reflects expectations about an
accommodative monetary policy and, thus, is indicative of a thriving
economy. Suppose the economy is growing fast so that strong aggregate
demand is likely to generate inflationary pressures. Suppose further the
monetary authority raises interest rates to preserve price stability. Two
effects may follow. On the one hand, the yield spread shrinks, since short
yields are likely to increase by a larger amount than long-term yields;
on the other hand, aggregate demand weakens, following the reduc-
tion of private investments. The adjustment process of the long end of
the yield curve following the shock affecting the short end implies an
intermediate step occurring at medium-term maturities, where the cor-
responding yields rise by more than long-term ones. The propagation
along the entire spectrum of TS maturities generates a temporary spike
in the medium end of the yield curve. Therefore, both the dynamics
of the yield curve and the evolution of the macroeconomic conditions
occur at the same time. Expectations may either accelerate or anticipate
the process. The contrary happens before a recession. Expectations of
accommodative monetary policy exert a negative pressure on TS medium
maturities thus causing curvature to drop (Figure 7.1). In this chapter
we do not intend to establish any causality relation between curvature
and real economy, we simply suggest that curvature reflects the cycli-
cal behavior of the economy. In short, the curvature effect seems to
accompany the transition of the yield curve from a positively sloped one,
prevailing during booms, to a flat one, which is believed to anticipate
recessions.
Estimations of the monetary equation (7.5) suggest curvature being
significantly related to the annual change of both the federal funds and
M1. Hence, evidence does not entirely reject the hypothesis that curva-
ture is related to monetary policy shocks. However, we provide evidence
that the link between curvature and the real economy is stronger than
the link between curvature and monetary policy variables.7 In line with
Rudebusch and Wu (2004, 2005), we suggest that the TS slope is more
closely related to a Taylor-type monetary policy reaction function.
Since we believe that curvature reflects the state of the economy rather
than the monetary conditions, we forecast curvature using both mod-
els. According to our results (Figure 7.3) model R, rather than model

132
M. Modena
–4
0
4
–12
–8
–4
0
4
88
90
92
94
96
98
00
02
04
06
NS curvature
forecast
std errors
forecast errors
Model R
Model M
–4
0
4
–8
–4
0
4
88
90
92
94
96
98
00
02
04
06
NS curvature
forecast
std errors
forecast errors
Figure 7.3
Forecasting performance of models (7.5) and (7.6)
Notes: NS curvature: curvature obtained with the Nelson–Siegel method; std errors:
standard errors; forecast: forecast of the curvature factor; forecast error: difference
between actual and predicted curvature.
M, returns a better fit. Both models return quite accurate forecasts, but
standard errors of model R are lower. In addition, forecast errors of
model R oscillate closer around the zero line. A battery of tests is per-
formed to prove that the predictive accuracy of model (R) is better than
that of model (M): Theil inequality, Diebold-Mariano, Morgan-Granger-
Newbold, Wilcoxon.
As a further robustness check, we examine whether also curvature
obtained from the real TS is related to the real economy. Removing the
effect of inflation from TS should not affect the curvature factor, since
inflation is mainly reflected in the long end of the yield curve. Ang et al.
(2008) point out that the real TS does not exhibit any trend, while the
typical upward-sloping shape of the nominal yield curve is due to a pos-
itive inflation risk premium which is incorporated in long-term yields.
Therefore, the medium part of the yield curve should be unaffected after
removing the effect of inflation. Hence, curvature extracted from the real
TS should track curvature obtained from the nominal TS.8 The correla-
tion coefficient between real TS curvature and nominal TS curvature is
very high indeed, about 0.95.
After ruling out inflation, we re-estimate both the monetary and the
real equations for the real TS curvature. Curvature is still significantly
explained by real variables, as reported in Table 7.3. Real TS curvature
is also significantly related to consumption growth; such result can be
interpreted consistently with previous findings in the literature (Harvey
1988; Chapman 1997).

Table 7.3
Estimates of equations (7.5) and (7.6) for the real TS curvature
Curvature – Real TS
Model R – equation (7.6)
Model M – equation (7.5)
ρ0
ρ1
ρ2
ρ3
ρ4
χ2
δ0
δ1
δ2
δ3
χ2
OLS
−0.4731
0.0636
−0.0937
−0.3403
0.1075
−0.8308
0.5617
−0.0419
0.1326
WH
(0.074)
[−6.3]
(0.011)
[5.6]
(0.024)
[−3.8]
(0.022)
[−15]
(0.025)
[4.2]
94.47
(0.092)
[−9.1]
(0.069)
[8.0]
(0.005)
[−7.1]
(0.024)
[5.4]
85.50
HH (12)
(0.166)
[−2.8]
(0.018)
[3.4]
(0.056)
[−1.7]
(0.048)
[−7.0]
(0.048)
[2.2]
83.95
(0.314)
[−2.6]
(0.201)
[2.7]
(0.012)
[−3.7]
(0.068)
[1.9]
40.00
NW (18)
(0.158)
[−2.9]
(0.018)
[3.4]
(0.056)
[−1.7]
(0.045)
[−7.4]
(0.048)
[2.2]
68.30
(0.283)
[−2.9]
(0.187)
[3.1]
(0.010)
[−4.2]
(0.064)
[2.1]
51.61
s-HH
(0.204)
[−2.3]
(0.033)
[1.9]
(0.060)
[−1.6]
(0.063)
[−5.3]
(0.067)
[1.6]
48.91
(0.262)
[−3.2]
(0.193)
[2.9]
(0.014)
[−2.9]
(0.080)
[1.6]
30.17
R2
adj
0.63
R2
adj
0.51
ρ0
ρ1
ρ2
ρ3
ρ4
χ2
δ0
δ1
δ2
δ3
χ2
IV
−0.4303
0.0649
−0.1097
−0.3779
0.0935
−0.8312
0.5390
−0.0474
0.1397
(0.172)
[−2.5]
(0.019)
[3.3]
(0.068)
[−1.6]
(0.040)
[−9.2]
(0.049)
[1.9]
70.41
(0.193)
[−4.3]
(0.129)
[4.1]
(0.009)
[−5.1]
(0.049)
[2.8]
42.50
R2
adj
0.63
R2
adj
0.51
Notes: Standard error in parenthesis; t-statistics in square brackets.

134
M. Modena
We thus use both models (7.5) and (7.6) to predict curvature obtained
from the real TS. Results support the thesis that model R performs bet-
ter than model M. During periods of economic slowdown, both models
tend to overestimate curvature. As before, a further robustness check is
provided by predictive accuracy tests.
Finally, we wish to verify whether the curvature factor is related to the
aggregate demand (AD) curve, which is usually assumed to describe the
state of the economy.



gapt = ψ0,g + ψ1,gEt

gapt+1

+

1 −ψ1,g

·

ψ2,g gapt−1

+ψ3,g

ffrt −Et

πt+1

+ εt,g
curt = ψ0,c + ψ1,c Et

curt+1

+

1 −ψ1,c

·

ψ2,c curt−1

+ψ3,c

ffrt −Et

πt+1

+ εt,c
(7.7)
A traditional AD (IS) curve implies that the output gap is a function of
its forward-looking component, its lagged realizations, and the expected
real interest rate. We jointly estimate equations (7.7) in order to compare
the coefficients obtained from the actual AD curve with those com-
ing from the curvature equation. The forward-looking real component
in the AD equation captures both consumption-smoothing behavior,
which is an empirical regularity, and the sentiment about the future
state of the economy. The system is GMM estimated, thus matching
a twofold objective. Instruments are necessary since expected future
(unobserved) variables appear in both equations; they are also required
to back generated regressors in the second equation. In both cases, vari-
ables may be eventually measured with errors, so that the GMM allows
obtaining robust estimates.9 In addition, GMM estimation handles with
heteroscedasticity and serial correlation of unknown forms.
Result of estimating system (7.7) is reported in Table 7.4. If estimated
coefficients of the first equation are similar to the respective coefficients
Table 7.4
Estimates of equations (7.7)
AD equation
IP gap
Curvature
ψ1,g
ψ1,g
ψ2,g
ψ3,g
ψ0,c
ψ1,c
ψ2,c
ψ3,c
GMM −0.0494
0.8931
0.8292
0.0246
−0.0608
0.7366
0.9711
0.0197
(0.035)
[−1.4]
(0.089)
[10]
(0.339)
[2.4]
(0.013)
[1.9]
(0.183)
[−0.3]
(0.292)
[2.5]
(0.209)
[4.6]
(0.042)
[0.5]
R2
adj
0.88
R2
adj
0.95
Notes: Standard errors in parenthesis; t-statistics in square brackets.

Latent Factors of the Yield Curve
135
of the second equation, we may presume that curvature can proxy the IP
gap, that is the curvature reflects the cyclical fluctuations of real activity.
The magnitude of coefficients are comparable. The better fit of the cur-
vature equation might be due to the higher persistence of the financial
factor. Residuals from both equations are serially uncorrelated and suf-
ficiently homoscedastic. Residuals’ correlograms is regularly distributed
around zero. The Wald test, used to check whether the estimated param-
eters in the IP gap equation are equal to the respective counterparts in
the curvature equation, supports both individual and joint coefficient
equality.
As a final check, we forecast the IP gap after replacing the dependent
variable of the curvature equation with the aforementioned variable,
thus imposing the IP gap to be a function of curvature and the real inter-
est rate. The forecast tracks quite well the actual series of the IP gap
reproducing the real pattern of business cycle fluctuations.
7.6
A cyclical model for curvature
In this section, we provide some more evidence relating curvature to the
cyclical component extracted from a structural time series model for IP
(Harvey 1989). IP is assumed to have a stochastic trend and a cyclical
component; the former represents the long-term movement in the time
series while the latter determines the entity of economic fluctuation, that
is the cycle dynamics. Two random walk processes underlie the stochastic
trend µt:
µt = µt−1 + βt + ηt
(7.8)
βt = βt−1 + ςt
(7.9)
ηt and ςt are white noise mutually uncorrelated disturbances with zero
mean and standard deviation σn and σς respectively. Both the upward
and downward movements of the trend are driven by the ηt component;
while the steepness of the trend depends on ςt. Whenever the variance
of the disturbances collapses to zero the stochastic trend turns into a
deterministic one; on the other hand, the larger the variances the greater
the stochastic movements of the trend.
The cycle ψt is technically constructed using the sine/cosine wave
functions. The length of a cycle is called the period, which represents
the time taken to go through its complete range of values (2π/λ); while
the frequency (λ) measures how often the cycle is repeated in the unit
of time. The cycle is then characterized by few other parameters, the

