# Portfolio Dynamics, Arbitrage Pricing & Black-Scholes

!!! info "Source"
    **Arbitrage Theory in Continuous Time** by Tomas Björk, Oxford University Press, 2nd ed., 2004.
    These notes are used for educational purposes.

## Portfolio Dynamics & Arbitrage Pricing

PARTIAL DIFFERENTIAL EQUATIONS 
69 
Since, by assumption, F actually satisfies eqn (5.26), the time integral above will 
vanish. If furthermore the process cr(s, X,)(aF/dx)(s, X,) is sufficiently integ- 
rable and we take expected values, the stochastic integral will also vanish. The 
initial value Xt = x and the boundary condition F(T, x) = @(x) will eventually 
leave us with the formula 
F(t, $1 = Et,, [@ ( X T ) ~  
, 
where we have indexed the expectation operator in order to emphasize that the 
expected value is to be taken given the initial value Xt = x. Thus we have 
proved the following result, which is known as the Feynman-KaE stochastic 
representation formula. 
Proposition 5.5 (Feynman-KaE) Assume that F is a solution to the bound- 
ary value problem 
aF 
1 ,  
d 2F 
-(t,x) 
+p(t,x)-- + -u (t,x)-(t,x) 
= 0, 
ax 
2 
ax2 
F(T,x) = @(x). 
Assume furthermore that the process 
d F  
4 . 7  xs)z(s, 
x8) 
is in E2 (see Definition 4.3), where X is defined below. Then F has the 
F(t7 2) = Et,, [@ (XT)] 
(5.29) 
where X satisfies the SDE 
dXs = / l ( ~ ,  
Xs) ds + U(S, Xs) dWs, 
(5.30) 
Xt = X. 
(5.31) 
Note that we need the integrability assumption o ( s , ~ , ) g ( s , X , )  E L2 in 
order to guarantee that the expected value of the stochastic integral in (5.28) 
equals zero. In fact the generic situation is that a boundary value problem of the 
type a b o v e a  so-called parabolic problem-will have infinitely many solutions, 
(see John 1982). It will, however, only have one "nice" solution, the others being 
rather "wild", and the proposition above will only give us the "nice" solution. 
We may also consider the closely related boundary value problem 
d F  1 
d 2 F  
-(t,x) 
+p(t,x)- 
+ -02(t,x)-(t,x) 
- rF(t,x) = 0, 
ax2 
(5.32) 
ax 
2 
F(T,x)=@(x), (5.33) 

DIFFERENTIAL EQUATIONS 
where r is a given real number. Equations of this type appear over and over 
again in the study of pricing problems for financial derivatives. Inspired by the 
ODE technique of integrating factors we are led to multiply the entire eqn (5.32) 
by the factor erS, and if we then consider the process Z(s) = e-'" F (s, X(s)), 
where X as before is defined by (5.30)-(5.31), we obtain the following result. 
Proposition 5.6 (Feynman-KaE) Assume that F is a solution to the bound- 
ary value problem 
O F  
aF 1 
a2F 
-(t,x) 
+p(t,x)- + -u2(t,x)-(t,x) 
- rF(t,x) = 0, 
at 
ax 
2 
ax2 
F(T,x) = cP(x). 
(5.35) 
Assume furthermore that the process a(s, x,) 
(s, X,) is in it2, where X is 
defined below. Then F has the representation 
F(t , x) = e-r(T-t) E,,, [a (XT)] , 
where X satisfies the SDE 
dXs = p(~,X,)ds + a(~,Xs)dWs, 
xt 
= x. 
Example 5.7 Solve the PDE 
aF 
1 ,d2F 
a ( t , ~ ) + - ~  - i - ( t , ~ ) = O ,  
2 
6x 
F(T, x) = x2, 
where a is a constant. 
Solution: From Proposition 5.5 we immediately have 
F(t, 2) = Et,, [X$] 7 
where 
. [ # ,  ,: 
Xttf 
, .< 
dX, =O.ds+udW,, 
c 
xt = x. 
This equation can easily be solved, and we have 

PARTIAL DIFFERENTIAL EQUATIONS 
so XT has the distribution N[x, o
m
]
.
 
Thus we have the solution 
F(t, X )  = E [x$] 
= Var [XT] + { E  [ x T ] } ~  
= 0 2 ( ~  
- t) + x2. 
Up to now we have only treated the scalar case, but exactly the same 
arguments as above will give us the following result. 
Proposition 5.8 Take as given 
A (column-vector valued) function p : R+ x Rn + Rn. 
A function C : R+ x Rn -t M(n, n), which can be written in the form 
c(t, 
X )  = b(t, x)(T*(~, 
x), 
for some function u : R+ x Rn -t M(n, d). 
A real valued function @ : R" + R. 
A real number r. 
Assume that F : R+ x Rn -t R is a solution to the boundary value problem 
aF 
1 
a 2 ~  
- ( t , ~ ) +  E r ( t , ~ ) ~ ( t . x ) +  
5 C Cij(t.2)- 
(t, X )  - T F ( ~ ,  
X )  =o, 
i,j=l 
ax,axj 
F(T, x )  = @(x). 
Assume furthermore that the process 
n 
aF 
C o j ( s ,  xs)-(s, xs) 
i=l 
axi 
is in f2 (see Definition 4.3), where X is defined below. Then F has the 
F(t,x) = e-r(T-t)~t,, [a (XT)], 
(5.39) 
where X satisfies the SDE 
dXs = p(s, Xs) dt + U ( S ,  Xs) dWs, 
(5.40) 
Xt = X .  
(5.41) 
We end this section with a useful result. Given Lemma 4.9 the proof is easy and 
left to the reader. 

72 
DIFFERENTIAL EQUATIONS 
1 
Proposition 5.9 Consider as given a vector process X w 
a function F(t, x). Then, modulo some integrability COI 
ing hold: 
ith gene! 
rlditions, 
rator 
the 
The process F(t, X t )  is a martingale relative to the filtration FX if and 
onlu if F satisfies the PDE 
I 
The process F(t, X t )  is a martingale relative to the 
only if, for every (t,x) and T 2 t, we have 
F(t, 4 = Et,, [F(T, X T ) ~ .  
5.6 The Kolmogorov Equations 
We will now use the results of the previous section in order to derive some 
classical results concerning the transition probabilities for the solution to an 
SDE. The discussion has the nature of an overview, so we allow ourselves some 
latitude as to technical details. 
Suppose that X is a solution to the equation 
i 
dXt = At,&) dt + ~ ( t ,  
xt) dWt, 
(5.42) 
with infinitesimal generator d given by 
where as usual 
C(t,z) = a(t,x)u*(t, x). 
I 
I 
Now consider the boundary value problem 
($ + du) (s, ar) = 0, 
(8, Y) E (0, T) 
x Rn, 
I I 
~ ( T , ! / ) = I B ( Y ) ,  Y E R n ,  
where IB is the indicator fundion of the set B. From Proposition 5.8 we 
immediately have 
~ ( 3 ,  
Y )  = E*,, [ I B ( ~ T ) ]  
= ~ ( X T  
E B 1x8 = Y ), 
where X is a solution of (5.42). This argument can also be turned around, and 
we have thus (more or less) proved the following result. 

THE KOLMOGOROV EQUATIONS 
73 
Proposition 5.10 (Kolmogorov backward equation) Let X be a solu- 
tion to eqn (5.42). 
Then the transition probabilities P(s, y; t, B) = 
P (Xt E B IX(s) = y) are given as the solution to the equation 
(g 
+ M )  (3, Y; t, B) = 0, 
(s, Y) E (0, 
t) x Rn, 
(5.43) 
P(t, Y; t, B) = IB(Y). 
(5.44) 
Using basically the same reasoning one can also prove the following corresponding 
result for transition densities. 
Proposition 5.11 (Kolmogorov backward equation) Let X be a solution 
to eqn (5.42). Assume that the measure P(s, y; t, dx) has a density p(s, y; t, x) dx. 
Then we have 
(2 + AP) (s, Y; t, x) = 0, (s, r) E (0, t) x Rn, 
(5.45) 
p(s, y; t, x) -+ d,, 
as s -t t. 
(5.46) 
The reason that eqns (5.43) and (5.45) are called backward equations is that 
the differential operator is working on the "backward variables" (s, y). We will 
now derive a corresponding L'forward" equation, where the action of the differ- 
ential operator is on the "forward" variables (t, x). For simplicity we consider 
only the scalar case. 
We assume that X has a transition density. Let us then fix two points in time 
s and T with s < T. Now consider an arbitrary "test function", i.e. an infinite 
differentiable function h(t, x) with compact support in the set (s, T) x R. From 
the It6 formula we have 
ah 
* ah 
[ 
h ( ~ ,  
XT) = h(s, xS)+ J (% + h) (t, xt) dt + 
az(t9 x t )  dwt. 
Applying the expectation operator E,,, 1.1, and using the fact that, because of 
the compact support, h(T, x) = h(s, x) = 0, we obtain 
JW lT 
p(s, y; t, X) (: 
+ A) h(t, X) dz dt = 0. 
-00 
Partial integration with respect to t (for &) and with respect to x (for A) gives us 
IT 
h(t,x) (-: 
+A*) p(s,y; t,x) dxdt = 0, 
where the adjoint operator A* is defined by 
a 
(A* f )  (t, X) = -- 
1 a* 
ax C(t, x)f (t. x)l + 2 a [c2(t, x)f (t, 41 - 

74 
DIFFERENTIAL EQUATIONS 
Since this equation holds for all test functions we have shown the follow- 
ing result. 
Proposition 5.12 (Kolmogorov forward equation) Assume that the solu- 
tion X of eqn (5.42) has a transition density p(s, y; t, x). Then p will satisfy the 
Kolmogorov forward equation 
This equation is also known as the Fokker-Planck equation. The 
multidimensional version is readily obtained as 
a p  
~
(
s
,
 
s; t. 5) = A*P(s, 
Y; t, x), 
where the adjoint operator A* is defined by 
Example 5.13 Let us consider a standard Wiener process with constant 
diffusion coefficient o, i.e. the SDE 
dXt = u dWt. 
I 
I 
The Fokker-Planck equation for this process is 
and it is easily checked that the solution is given by the Gaussian 
densitv 
Example 5.14 Consider the GBM process 
The Fokker-Planck equation for this process is 

EXERCISES 
I 
, A change of variables of the form x = ey reduces this equation to an equation 
, with constant coefficients, which can be solved by Fourier methods. For us it is 
perhaps easier to get the transition density directly by solving the SDE above. 
See the exercises below. 
5.7 Exercises 
b, Exercise 5.1 Show that the scalar SDE 
has the solution 
X(t) = eat . xo + a 
ea(t-s) dWs, 
I' 
(5.49) 
by differentiating X as defined by eqn (5.49) and showing that X so defined 
actually satisfies the SDE: 
Hint: Write eqn (5.49) as 
where 
and first compute the differentials dZ, dY and dR. Then use the multidimen- 
sional It6 formula on the function f (y , z, r) = y + z . r. 
Exercise 5.2 Let A be an n x n matrix, and define the matrix exponential eA 
by the series 
E This series can be shown to converge uniformly. 
(a) Show, by taking derivatives under the summation sign, that 

76 
DIFFERENTIAL EQUATIONS 
(b) Show that 
eO = I, 
where 0 denotes the zero matrix, and I denotes the identity matrix. 
(c) Convince yourself that if A and B commute, i.e. AB = BA, then 
eA+B = eA . eB = eB . eA. 
Hint: Write the series expansion in detail. 
(d) Show that eA is invertible for every A, and that in fact 
[&I -' = .-A. 
(e) Show that for any A, t and s 
eA(t+8) = eAt . eAs 
(f) Show that 
(&)* = eA* 
Exercise 5.3 Use the exercise above to complete the details of the proof of 
Proposition 5.3. 
Exercise 5.4 Consider again the linear SDE (5.19). 
Show that the 
expected value function m(t) = E[X(t)], and the covariance matrix 
C(t) = {COV(X,(~),X~(~))}~,~ 
are given by 
m(t) = eAtzo + 
eA(t-s)b(s) ds, 
l 
C(t) = 
eA(t-8)u(s)u*(s)eA*(t-s) 
ds, 
where * denotes transpose. Lt 
Hint: Use the explicit solution above, and the fact that 
C(t) = E [XtX,*] 
- m(t)m*(t). 
Geometric Brownian motion constitutes a class of processes which is closed under 
a number of nice operations. Here are some examples. 
Exercise 5.5 Suppose that X sati&ea the SDE 
dXt = axt dt + uXt dWt . 
Now define Y by Yt = x!, where /3 is a real number. Then Y is also a GBM 
process. Compute dY and find out which SDE Y satisfies. 

EXERCISES 
Exercise 5.6 Suppose that X satisfies the SDE 
dXt = axt dt + axt dWt, 
and Y satisfies 
d& =y&dt+b&d%, 
where V is a Wiener process which is independent of W. Define Z by Z = X/Y 
and derive an SDE for Z by computing dZ and substituting Z for X/Y in the 
right hand side of dZ. If X is nominal income and Y describes inflation then Z 
describes real income. 
Exercise 5.7 Suppose that X satisfies the SDE 
dXt = axt dt + u X ~  
dWt, 
and Y satisfies 
d& = 7&dt+6&dWt. 
Note that now both X and Y are driven by the same Wiener process W. Define 
Z by Z = X/Y and derive an SDE for Z. 
Exercise 5.8 Suppose that X satisfies the SDE 
dXt = axt dt + axt dWt, 
and Y satisfies 
d& = y&dt+6xd&, 
where V is a Wiener process which is independent of W. Define Z by Z = X . Y 
and derive an SDE for Z. If X describes the price process of, for example, IBM 
in US$ and Y is the currency rate SEK/US$ then Z describes the dynamics of 
the IBM stock expressed in SEK. 
Exercise 5.9 Use a stochastic representation result in order to solve the 
following boundary value problem in the domain [0, T] x R: 
aF 
aF 1 
a2F 
- 
+ px- 
+ -&2- 
= 
at 
ax 
2 
ax2 
0, 
F(T, x) = ln(x2). 
Here p and a are assumed to be known constants. 
Exercise 5.10 Consider the following boundary value problem in the domain 
aF 
aF 
1 
a2F 
- 
+ p(t,x)- + -a2(t,x)- 
+ k(t,x) = 0, 
at 
ax 
2 
ax2 
F(T, x) = @(x). 
Here p, a, k and @ are assumed to be known functions. 

78 
DIFFERENTIAL EQUATIONS 
Prove that this problem has the stochastic representation formula 
F(t, 2) = Et,, [@(XT)] + 
Et,, [k(s, Xs)] ds, 
where as usual X has the dynamics 6' 
dX, = p(s, X,) ds + U(S, X,) dW,, 
xt = x. 
Hint: Define X as above, assume that F actually solves the PDE and 
consider the process Z, = F (s, X, ) . 
Exercise 5.11 Use the result of the previous exercise in order to solve 
aF 
1 
a2F 
- 
+ -x2- 
at 
2 
ax2 + x = o ,  
F(T, x )  = ln(x2). 
Exercise 5.12 Consider the following boundary value problem in the domain 
[O,T] x R. 
aF 
aF 
1 
a2F 
-+p(t,x)-+ 
-a2(t,x)-  
+r(t,x)F =0, 
at 
ax 
2 
8x2 
F(T,x) = @(x). 
Here p(t , x) , a(t , x )  , r (t , x )  and @(x) are assumed to be known functions. Prove 
that this problem has a stochastic representation formula of the form 
~ ( t ,  
x )  = E~~ F(xT)eJ: 
r(8J*)*8] , 
by considering the process Z, = F(s, X,) x exP [c r(u, Xu) du] on the time 
interval [t, TI. 
Exercise 5.13 Solve the boundary value problem 
aF 
1 ,d2F 
1 
d2F 
-(t, ~ , y )  
+ -a -(t,x,y) + -62-(t,x,y) 
= 0, 
at 
2 
ax2 
2 
a y 2  
F(T, x,y) = xy- 
Exercise 5.14 Go through the details in the derivation of the Kolmogorov 
forward equation. 
Exercise 5.15 Consider the SDE 
dXt = a d t  + udWt, 

NOTES 
79 
where a and a are constants. 
(a) Compute the transition density p(s, y; t, x), by solving the SDE. 
(b) Write down the Fokker-Planck equation for the transition density and 
check the equation is indeed satisfied by your answer in (a). 
Exercise 5.16 Consider the standard GBM 
i 
dXt = 
dt + gXt dWt 
and use the representation 
Xt = xs 
exp {[a - $a2] 
(t - s) + o [Wt - W,]) 
D in order to derive the transition density p(s, y; t, x) of GBM. Check that this 
density satisfies the Fokker-Planck equation in Example 5.14. 
5.8 Notes 
All the results in this chapter are standard and can be found in, for example, 
Karatzas and Shreve (1988), Revw and Yor (1991), Bksendal (1995). For an 
encyclopedic treatment of the probabilistic approach to parabolic PDEs see 
Doob (1984). 

m C I I S I  : Ape.!, ! i 
6 
PORTFOLIO DYNAMICS 
6.1 Introduction 
Let us consider a financial market consisting of different assets such as stocks, 
bonds with different maturities, or various kinds of financial derivatives. In this 
chapter we will take the price dynamics of the various assets as given, and the 
main objetive is that of deriving the dynamics of (the value of) a so-called self- 
financing portfolio. In continuous time this turns out to be a fairly delicate task, 
so we start by studying a model in discrete time. We will then let the length of 
the time step tend to zero, thus obtaining the continuous time analogs. It is to 
be stressed that this entire section is only motivating and heuristic. The formal 
definitions and the corresponding theory will be given in the next section. 
Let us thus study a financial market, where time is divided into periods of 
length At, and where trading only takes place at the discrete points in time 
nAt, n = 0,1, . . .. We consider a fixed period [t, t + At). This period (where 
of course t = nAt for some n) is henceforth referred to as "period t". In the 
sequel we will assume that all assets are stocks, but this is purely for linguistic 
convenience. 
Definition 6.1 
N = the number of different types of stocks. 
hi(t) = number of shares of type i held during the period [t, t + At). 
h(t) = the portfolio [hl (t), . . . , hN(t)] held during period t. 
c(t) = the amount of money spent on consumption per unit time 
during the period [t, t + At). 
Si(t) = the price of one share of type i during the period [t, t + At). 
V ( t )  = the value of the portfolio h at time t. 
The information and the decisions in the model are structured as follows: 
At time t ,  i.e. at the start of period t ,  we bring with us an "old" portfolio 
h(t - At) = {hi(t - At), i = 1,. . . , N) from the previous period t - At. 
At time t we can observe the price vector S(t) = (Sl(t), . . . , SN(t)). 
At time t, after having observed S(t), we choose a new portfolio h(t), to 
be held during period t. At the same time we also choose the consumption 
rate c(t) for the period t. Both h(t) and c(t) are assumed to be constant , 
over the period t. 

INTRODUCTION 
81 
Remark 6.1.1 Note that, so far, we only consider nondividend paying assets. 
The case of dividend paying assets is slightly more complicated, and since it will 
only be used in Chapter 16, we omit it from our main discussion. See Section 6.3 
for details. 
We will only consider so called self-financing portfolio-xonsumption pairs 
; (h, c), i.e. portfolios with no exogenous infusion or withdrawal of money (apart 
of course from the c-term). In other words, the purchase of a new portfolio, as 
well as all consumption, must be financed solely by selling assets already in the 
portfolio. 
To start the analysis we observe that our wealth V(t), i.e. the wealth at the 
start of period t, equals the value of the old portfolio h(t - At). Thus we have 
N 
V(t) = C hi (t - At)Si (t) = h(t - At)S(t), 
(6.1) 
a=1 
where we have used the notation 
for the inner product in RN. Equation (6.1) simply says that at the beginning 
of period t our wealth equals what we get if we sell our old portfolio at today's 
prices. We may now use the proceeds of this sale for two purposes: 
Reinvest in a new portfolio h(t). 
i 
Consume at the rate c(t) over the period t. 
G 
The cost of the new portfolio h(t), which has to be bought at today's prices, is 
given by 
N 
whereas the cost for the consumption rate c(t) is given by c(t)At. The budget 
equation for period t thus reads 
If we introduce the notation 
AX(t) = X(t) - X(t - At), 
for an arbitrary process X, we see that the budget equation (6.2) reads 

82 
PORTFOLIO DYNAMICS 
Since our goal is to obtain the budget equation in continuous time it is now 
tempting to let At -+ 0 in eqn (6.3) to obtain the formal expression 
S(t) dh(t) + c(t) dt = 0. 
This procedure is, however, not correct, and it is important to understand why 
that is so. The reasons are as follows: 
All stochastic differentials are to be interpreted in the It6 sense. 
The It6 integral 
g(t) dW(t) was defined as the limit of sums of the type 
C dtn) [W(tn+~) - W(tn)l, 
where it was essential that the W-increments were forward differences. 
In eqn (6.3) we have a backward h-difference. 
In order to get It6 differentials we thus have to reformulate eqn (6.3). This is 
done by adding and subtracting the term S(t - At)Ah(t) to the left-hand side, 
and the budget equation now reads 
S(t - At)Ah(t) + AS(t)Ah(t) + c(t)At = 0. 
Now, at last, we may let At + 0 in the budget equation (6.4), giving us 
S(t) dh(t) + dh(t) dS(t) + c(t) dt = 0. 
Letting At -+ 0 in eqn (6.1) gives us 
V(t> = h(t)S(t), 
and if we take the It6 differential of this expression we get 
dV(t) = h(t) dS(t) + S(t) dh(t) + dS(t) dh(t). 
To sum up, eqn (6.7) is the general equation for the dynamics of an arbitrary 
portfolio, and eqn (6.5) is the budget equation which holds for all self-financing 
portfolios. Substituting (6.5) into (6.7) thus gives us our desired object, namely 
the dynamics of (the wealth of) a self-financing portfolio. 
dV(t) = h(t) dS(t) - ~ ( t )  
dt. 
In particular we see that in a situation without any consumption we have the 
following V-dynamics: 
dV(t) = h(t) dS(t). 

SELF-FINANCING PORTFOLIOS 
83 
Remark 6.1.2 The natural economic interpretation of eqn (6.9) is of course 
that in a model without any exogenous income, all change of wealth is due to 
changes in asset prices. Thus (6.8) and (6.9) seem to be rather self-evident, and 
one may think that our derivation was rather unneccesary. This is, however, not 
' the case, which we realize if we recall that the stochastic differentials in (6.8) 
and (6.9) are to be interpreted in the It8 sense, where it is important that the 
integrator increment dS(t) is a forward increment. If we had chosen to define 
our stochastic integral in some other way, e.g. by using backward increments 
e done), the formal appearance of (6.8)-(6.9) would have 
The real content, on the other hand, would of course have 
6.2 Self-financing Portfolios 
Having gone through the derivations of the preceding section there are some 
natural questions. 
1. In which sense ( L ~ ,  
P-as., etc.) is the limiting procedure of letting At + 0 
to be interpreted? 
2. Equation (6.8) is supposed to be describing the dynamics of a self-financing 
portfolio in continuous time, but what is "continuous time trading" 
supposed to mean "in reality"? 
The answer to these questions is simply that the preceding reasoning has only 
been of a motivating nature. We now give a purely mathematical definition of 
the central concepts. The interpretations of the concepts are of course those of 
the preceding section. 
Definition 6.2 Let the N-dimensional price process {S(t); t 2 0 )  be given. 
1. A portfolio strategy (most often simply called a portfolio) is any 3:- 
adapted N-dimensional process {h(t); t 2 0). 
2. The portfolio h is said to be Markovian if it is of the form 
h(t) = h(t, S(t)), 
for some function h : R+ x R~ + RN. 
3. The value process vh wmsponding to the portfolio h is given by 
N 
vh(t) 
= C h,(t)~,(t). 
(6.10) 
i=l 
4. A consumption process is any 3:-adapted one-dimensional process 
onsumption pair (h, c) is called self-financing if the value 
process vh satisfies the condition 
N 
d v h ( t )  = C h,(t) dS,(t) - e(t) dt, 
(6.11) 
i=l 

84 
PORTFOLIO DYNAMICS 
i.e. if 
dvh (t) = h(t) dS(t) - c(t) dt. 
Remark 6.2.1 Note that, in general, the portfolio h(t) is allowed to depend 
upon the entire past price trajectory {S(U); u < t). In the sequel we will almost 
exclusively be dealing with Markovian portfolios, i.e. those portfolios for which 
the value at time t depends only on today's date t and today's value of the price 
vector S(t). 
For computational purposes it is often convenient to describe a portfolio in 
relative terms instead of in absolute terms as above. In other words, instead of 
specifying the absolute number of shares held of a certain stock, we specify the 
relative proportion of the total portfolio value which is invested in the stock. 
Definition 6.3 For a given portfolio h the corresponding relative portfolio u 
is given by 
where we have 
N 
i=l 
The self-financing condition can now easily be given in terms of the relative 
portfolio. 
Lemma 6.4 A portfolio-consumption pair (h, c) is self-financing if and only if 
N 
dvh(t) = vh(t) c ui(t)% 
- c(t) dt. 
i=l 
si(t) 
. 
In the future we will need the following slightly technical result which roughly 
says that if a process looks as if it is the value process of a self-financing portfolio, 
then it actually is such a value process. 
Lemma 6.5 Let c be a consumption process, and assume that there exist a scalar 
process Z and a vector process q = (ql, . . . , qN) such that 
Now define a portfolio h by 

DIVIDENDS 
85 
Then the value process vh is given by vh = 2, the pair (h, c) is self-financing, 
and the corresponding relative portfolio u is given by u = q. 
Proof By definition the value process vh is given by V h(t) = h(t)S(t), so 
eqns (6.15) and (6.16) give us 
Inserting (6.17) into (6.16) we see that the relative portfolio u corresponding to 
' 
hisgivenby u=q.Inserting (6.17) and (6.16) into (6.14) weobtain 
d v h ( t )  = C hi (t) dS* (t) - ~ ( t )  
dt, 
i=l 
I which shows that (h, c) is self-financing. 
6.3 Dividends 
This section is only needed for Chapter 16. We again consider the setup and 
notation of Section 6.1, with the addition that the assets now may pay dividends. 
Definition 6.6 W e  take as given the processes Dl (t), . . . , D N ( ~ ) ,  
where Di (t) 
denotes the cumulative dividends paid to the holder of one unit of asset i 
during the interval (0, t]. If Di has the structure 
dD; 
(t) = 6; (t) dt, 
1 
for some phcess hi, then we say that asset i pays a continuous dividend yield. 
The dividends paid to the holder of one unit of asset i during (s, t] are thus 
given by Di(t) - Di(s), and in the case of a dividend yield we have 
i 
t 
Di (t) = 1 6, (s) ds. 
I We assume that all the dividend processes have stochastic differentials. 
We now go on to derive the dynamics of a self-financing portfolio, and as 
usual we define the value process V by 
The difference between the present situation and the nondividend paying case 
is that the budget equation (6.2) now has to be modified. We have to take 

86 
PORTFOLIO DYNAMICS 
into account the fact that the money at our disposal at time t now consists of 
two terms: 
The value of our old portfolio, as usual given by 
h(t - At)S(t). 
The dividends earned during the interval (t - At, t]. These are given by 
N C hi (t - At) [Di(t) - Di 
(t - At)] = h(t - At) AD(t). 
i=l 
The relevant budget equation is thus given by 
h(t - At)S(t) + h(t - At)AD(t) = h(t)S(t) + c(t)At. 
Going through the same arguments as in Section 6.1 we end up with the 
following dynamics for a self-financing portfolio: 
N 
N 
dV(t) = 
hi (t) dSi (t) + 
hi (t) dDi (t) - c(t) dt, 
i=l 
i=l 
and we write this as a formal definition. 
Definition 6.7 
1. The value process vh is given by 
I 
N 
vh(t) = C hi(t)Si(t). 
d = l  
2. The (vector valued) gain process G is defined by 
G(t) = S(t) + D(t). 
3. The portfolio-consumption pair (h, c) is called self-financing if 
N 
dvh(t) = C hi(t) dGi (t) - ~ ( t )  
dt. 
2=1 
With notation as above we have the following obvious result. 

EXERCISE 
87 
Lemma 6.8 In terms of the relative portfolio weights, the dynamics of 
a self-financing portfolio can be expressed as 
N 
dvh (t) = V(t) . 
%(t) dC.0 - c(t) dt. 
(6.22) 
i=l 
Si(t) 
6.4 Exercise 
Exercise 6.1 Work out the details in the derivation of the dynamics of 
a self-financing portfolio in the dividend paying case. 
I 
1
.
c
 
~1oidi)'llqx:' ,I+ 1 " 
' 
7 
'a 
* I  
I
.
 
i ' 
I
,
 
( 
, I ,  r,,kj2 J. (?)'&Is 
, ,:ryi"$t 
& I  -. 
. 
c 
, 
i c;ris 4;hi;;'il 
v,,&:' 
. .  
, 
I 
, + . i ' ,  
= 
* j*v,*#rl: 
r , q + r ? ,  
,f f." 
' , ' I  
i 
, . 
', 3 
-.:+ 
"*>, , t" 
2_L7"rb,: 
, I 4 ,  . 
?
I
"
 
I 
$ 
, .  
1 

ARBITRAGE PRICING 
7.1 Introduction 
In this chapter, we will study a special case of the general model set out in the 
previous chapter. We will basically follow the arguments of Merton (1973), which 
only require the mathematical machinery presented in the previous chapters. For 
the full story see Chapter 10. 
Let us therefore consider a financial market consisting of only two assets: a 
risk free asset with price process B, and a stock with price process S. What, 
then, is a risk free asset? 
Definition 7.1 The price process B is the price of a risk free asset if it has 
the dynamics 
dB(t) = r(t)B(t) dt, 
(7.1) 
where r is any adapted process. 
The defining property of a risk free asset is thus that it has no driving 
dW-term. We see that we also can write the B-dynamics as 
so the B-process is given by the expression 
A natural interpretation of a riskless asset is that it corresponds to a bank with 
the (possibly stochastic) short rate of interest r. An important special case 
appears when r is a deterministic constant, in which case we can interpret B as 
the price of a bond. 
We assume that the stock price S is given by 
dS(t) = S(t)cr (t, S(t)) dt + S(t)a (t, S(t)) dW(t), 
(7.2) 
where w is a Wiener process and a and a are given deterministic functions. The 
reason for the notation W ,  instead of the simpler W, will become clear below. 
The function a is known as the volatility of S, while cr is the local mean rate 
of return of S .  

CONTINGENT CLAIMS AND ARBITRAGE 
89 
Remark 7.1.1 Note the difference between the risky stock price B, as modeled 
above, and the riskless asset B. The rate of return of B is formally given by 
This object is locally deterministic in the sense that, at time t, we have 
complete knowledge of the return by simply observing the prevailing short rate 
; r(t). Compare this to the rate of return on the stock S. This is formally given by 
and this is not observable at time t. It consists of the terms a (t, S(t)) and 
a (t, S(t)), which both are observable at time t, plus the "white noise" term 
( d ~ ( t ) / d t ) ,  
which is random. Thus, as opposed to the risk free asset, the stock 
, has a stochastic rate of return, even on the infinitesimal scale. 
The most important special case of the above model occurs when r, a and a 
are deterministic constants. This is the famous Black-Scholes model. 
Definition 7.2 The Black-Scholes model consists of two assets with dynam- 
ics given bg 
dB(t) = r B ( t )  dt, 
- 'i 
dS(t) = aS(t) dt + a S ( t )  d ~ ( t ) ,  
where r, a, and a are deterministic constants. 
7.2 Contingent Claims and Arbitrage 
We take as given the model of a financial market given by eqns (7.1)-(7.2), 
and we now approach the main problem to be studied in this book, namely the 
pricing of financial derivatives. Later we will give a mathematical definition, but 
let us at once present the single most important derivative-the European call 
option. 
Definition 7.3 A European call option with exercise price (or strike price) 
K and time of maturity (exercise date) T on the underlying asset S is a 
contract defined by the following clauses. 
. 
The holder of the option has, at time T ,  the right to buy one share of the 
underlying stock at the price K SEK from the underwriter of the option. 
The holder of the option is in no way obliged to buy the underlying stock. 
The right to buy the underlying stock at the price K can only be exercised 
at the precise time T. 

I 
90 
ARBITRAGE PRICING 
Note that the exercise price K and the time of maturity T are determined 
at the time when the option is written, which for us typically will be at t = 0. 
A European put option is an option which in the same way gives the holder 
the right to sell a share of the underlying asset at a predetermined strike price. 
For an American call option the right to buy a share of the underlying asset 
can be exercised at any time before the given time of maturity. The common 
factor of all these contracts is that they all are completely defined in terms of the 
underlying asset S, which makes it natural to call them derivative instruments 
or contingent claims. We will now give the formal definition of a contingent 
claim. 
Definition 7.4 Consider a financial market with vector price process S. 
A contingent claim with date of maturity (exercise date) T ,  also called 
a T-claim, is any stochastic variable X E 3;. A contingent claim X is called a 
simple claim if it is of the form 
X = @(S(T)). 
The function @ is called the contract function. 
The interpretation of this definition is that a contingent claim is a contract, 
which stipulates that the holder of the contract will obtain X SEK (which can be 
positive or negative) at the time of maturity T. The requirement that X E 3; 
simply means that, at time T, it will actually be possible to determine the 
amount of money to be paid out. We see that the European call is a simple 
contingent claim, for which the contract function is given by 
@(x) = max [x - K, 
01. 
The graphs of the contract functions for European calls and puts can be seen in 
Figs 7.1 and 7.2. It is obvious that a contingent claim, e.g. like a European call 
option, is a financial asset which will fetch a price on the market. Exactly how 
much the option is worth on the market will of course depend on the time t and 
on the price S(t) of the underlying stock. Our main problem is to determine a 
"fair" (in some sense) price for the claim, and we will use the standard notation 
w t ;  XI, 
for the price process of the claim X, 
where we sometimes suppress the X. In the 
case of a simple claim we will sometimes write n(t; a). 
If we start at time T the situation is simple. Let us first look at the particular 
case of a European call 
1. If S(T) 2 K we can make a certain profit by exercising the option in order 
to buy one share of the underlying stock. This will cost us K SEK. Then 

CONTINGENT CLAIMS AND ARBITRAGE 
FIG. 7.1. Contract function. European call, K = 100 
FIG. 7.2. Contract function. European put, K = 100 
! 
we immediately sell the asset on the stock exchange at the price S(T), 
thus giving us a net profit of S(T) - K SEK. 
2. If S(T) < K the option has no value whatsoever. 
Thus we see that the only reasonable price ll (T) for the option at time T is 
given by 
ll (T) = m a .  [S(T) - K, 01. 
(7.6) 

92 
ARBITRAGE PRICING 
Exactly the same way we see that for a more general contingent claim X, we 
have the relation 
n(T; X) = X, 
(7.7) 
and in the particular case of a simple claim 
For any time t < T it is, however, far from obvious what the correct price is for 
a claim X. On the contrary it seems to be obvious that there is no such thing 
as a "correct" or "fair" price. The price of an option, like the price of any other 
asset, is of course determined on the (option) market, and should therefore be 
an extremely complex aggregate of, for example, the various attitudes to risk 
on the market and expectations about the future stock prices. It is therefore an 
extremely surprising fact that, given some fairly mild assumptions, there is a 
formula (the BlackScholes formula) which gives the unique price of the option. 
The main assumption we will make is that the market is efficient in the sense 
that it is free of arbitrage possibilities. We now define this new and central 
E 
concept. 
Definition 7.5 A n  arbitrage possibility on a financial market is a sev-financed 
portfolio h such that 
W e  say that the market is arbitrage free if there are no arbitrage possibilities. 
An arbitrage possibility is thus essentially equivalent to the possibility of 
making a positive amount of money out of nothing without taking any risk. It 
is thus essentially a riskless money making machine or, if you will, a free lunch 
on the financial market. We interpet an arbitrage possibility as a serious case of 
mispricing in the market, and our main assumption is that the market is efficient 
in the sense that no arbitrage is possible. 
Assumption 7.2.1 W e  assume that the price process IT(t) is such that there 
are no arbitrage possibilities on the market consisting of ( B ( t ) ,  S(t), II (t)). 
A natural question now is how we can identify an arbitrage possibility. The 
general answer to this question requires quite a lot of fairly heavy probabilistic 
machinery which the more advanced reader will find in Chapter 10. Happily 
enough there is a partial result which is sufficient for our present purposes. 

CONTINGENT CLAIMS AND ARBITRAGE 
93 
Proposition 7.6 Suppose that there exists a self-financed portfolio h, such that 
the value process vh has the dynamics 
dvh(t) = k(t)vh(t) dt, 
(7.12) 
where k is an adapted process. Then it must hold that k(t) = r(t) for all t, or 
there exists an arbitrage possibility. 
Proof We sketch the argument, and assume for simplicity that k and r are 
constant and that k > r. Then we can borrow money from the bank at the 
I rate r. This money is immediately invested in the portfolio strategy h where it 
will grow at the rate k with k > r. Thus the net investment at t = 0 is zero, 
whereas our wealth at any time t > 0 will be positive. In other words we have an 
I arbitrage. If on the other hand r > k, we sell the portfolio h short and invest this 
money in the bank, and again there is an arbitrage. The cases with nonconstant 
and nondeterministic r and k are handled in the same way. 
The main point of the above is that if a portfolio has a value process whose 
dynamics contain no driving Wiener process, i.e. a locally riskless porfolio, 
then the rate of return of that portfolio must equal the short rate of interest. 
To put it in another way, the existence of a portfolio h is for practical purposes 
equivalent to the existence of a bank with k as its short rate of interest. We can 
then paraphrase the lemma above by saying that on an arbitrage free market 
there can only be one short rate of interest. 
We now return to the question of how the price process H(t; X) for a con- 
tingent claim X can behave, and the main idea is the following. Since the claim 
is defined entirely in terms of the underlying asset(s), we ought to be able to 
price it in terms of the price of the underlying asset(s) if arbitrage possibilities 
are to be avoided. Thus we are looking for a way to price the derivative in a way 
which is consistent with the price process of the underlying asset. 
I 
To take a simple example, it is quite obvious that for a European call we 
i must have the relation ll (t) 5 S(t) in an arbitrage free market, because no 
one in their right mind will buy an option to buy a share at a later date at 
price K if the share itself can be bought cheaper than the option. For a more 
formal argument, suppose that at some time t we actually have the relation 
n(t) > S(t). Then we simply sell one option. A part of that money can be 
used for buying the underlying stock and the rest is invested in the bank (i.e. 
we buy the riskless asset). Then we sit down and do nothing until time T. In 
this way we have created a self-financed portfolio with zero net investment at 
time t. At time T we will owe max [S(T) - K, 0] to the holder of the option, but 
this money can be paid by selling the stock. Our net wealth at time T will thus 
be S(T) - max [S(T) - K, 01, which is positive, plus the money invested in the 
bank. Thus we have an arbitrage. 
It is thus clear that the requirement of an arbitrage free market will impose 
some restrictions on the behavior of the price process H(t; X). This in itself is not 

94 
ARBITRAGE PRICING 
terribly surprising. What is surprising is the fact that in the market specified by 
eqns (7.1)-(7.2) these restrictions are so strong as to completely specify, for any 
given claim X, the unique price process n(t; X) which is consistent with absence 
of arbitrage. For the case of simple contingent claims the formal argument will 
be given in the next section, but we will now give the general idea. 
To start with, it seems reasonable to assume that the price II(t; X) at time 
I 
t in some way is determined by expectations about the future stock price S(T). 
Since S is a Markov process such expectations are in their turn based on the 
present value of the price process (rather than on the entire trajectory on [0, t]). 
I 
We thus make the following assumption. 
Assumption 7.2.2 We assume that 
1. The derivative instrument in question can be bought and sold on a market. 
2. The market is free of arbitrage. 
3. The price process for the derivative asset is of the form 
where F is some smooth function. 
Our task is to determine what F might look like if the market consisting of 
S(t), B(t) and II(t; X) is arbitrage free. Schematically we will proceed in the 
following manner: 
1. Consider a, a, a, F, and r as exogenously given. 
2. Use the general results from Section 6.2 to describe the dynamics of the 
value of a hypothetical self-financed portfolio based on the derivative 
instrument and the underlying stock (nothing will actually be invested 
in or loaned by the bank). 
3. It turns out that, by a clever choice, we can form a self-financed portfo- 
lio whose value process has a stochastic differential without any driving 
Wiener process. It will thus be of the form (7.12) above. 
4. Since we have assumed absence of arbitrage we must have k = r. 
5. The condition k = r will in fact have the form of a partial differential 
equation with F as the unknown function. In order for the market to be 
efficient F must thus solve this PDE. 
6. The equation has a unique solution, thus giving us the unique pricing 
formula for the derivative, which is consistent with absence of arbitrage. 
7.3 The Black-Scholes Equation 
In this section we will carry through the schematic argument given in the previous 
section. We assume that the a priori given market consists of two assets with 
dynamics given by 
dB(t) = rB(t) dt, 
(7.14) 
dS(t) = S(t)a (t, S(t)) dt + S(t)u (t, S(t)) d ~ ( t ) ,  
(7.15) 

THE BLACK-SCHOLES EQUATION 
95 
where the short rate of interest r is a deterministic constant. We consider a 
simple contingent claim of the form 
and we assume that this claim can be traded on a market and that its price 
process II (t) = II(t; @) has the form 
for some smooth function F. Our problem is to find out what F must look like 
in order for the market [S(t), B(t), II (t)] to be free of arbitrage possibilities. 
I 
We start by computing the price dynamics of the derivative asset, and the 
It8 formula applied to (7.17) and (7.15) g' ives us 
dII (t) = a, (t)II (t) dt + a, (t)H (t) d ~ ( t ) ,  
(7.18) 
I 
a 
i 
where the processes a,(t) and a,(t) are defined by 
- 
Here subscripts denote partial derivatives, and we have used a shorthand 
notation of the form 
and similarly for the other terms above. 
Let us now form a portfolio based on two assets: the underlying stock and 
the derivative asset. Denoting the relative portfolio by (us, u,) and using eqn 
(6.13) we obtain the following dynamics for the value V of the portfolio. 
d~ = V{U, [adt + u d ~ ]  
+u, [a,dt +aTdw]) 
(7.21) 
/ 
1 
where we have suppressed t. We now collect dt- and dl-terms to obtain 
dV = V [u,a + u,a,] 
dt + V [usu + u,ur] d l .  
(7.22) 
The point to notice here is that both brackets above are linear in the arguments 
us and u,. Recall furthermore that the only restriction on the relative portfolio 
is that we must have 
U, + u r  = 1, 

96 
ARBITRAGE PRICING 
for all t. Let us thus define the relative portfolio by the linear system of equations 
us +u, = 1, 
u,u + U,UT = 0. 
Using this portfolio we see that by its very definition the driving dw-term in 
the V-dynamics of eqn (7.22) vanishes completely, leaving us with the equation 
dV = V [u,a + u,a,] 
dt. 
Thus we have obtained a locally riskless portfolio, and because of the requirement 
that the market is free of arbitrage, we may now use Proposition 7.6 to deduce 
that we must have the relation 
usa + u,a, = r. 
This is thus the condition for absence of arbitrage, and we will now look more 
closely at this equation. 
It is easily seen that the system (7.23)-(7.24) has the solution 
0, 
us = - 
u, -a' 
-u 
u, = -, a, - a 
which, using (7.20), gives us the portfolio more explicitly as 
S(t)Fs(t, SO)) 
= S(t)F.(t, S(t)) - F(t, S(t)) ' 
%(t) = 
-F(t, S(t)) 
S(t)Fs(t, S(t)) - F(t, S(t)) ' 
Now we substitute (7.19), (7.29) and (7.30) into the absence of arbitrage 
condition (7.26). Then, after some calculations, we obtain the equation 
Ft (t, S(t)) + rS(t)F' (t, S(t)) + ;a2 (t, S(t)) S2(t)~ss 
(t, S(t)) - rF (t, S(t)) = 0. 
Furthermore, from the previous section we must have the relation 
II (T) = @(S(T)) . 
These two equations have to hold with probability 1 for each fixed t. Furthermore 
it can be shown that under very weak assumptions (which trivially are satisfied 
in the Black-Scholes model) the distribution of S(t) for every fixed t > 0 has 

THE BLACK-SCHOLES EQUATION 
97 
support on the entire positive real line. Thus S(t) can take any value whatsoever, 
eo F has to satisfy the following (deterministic) PDE. 
Ft(t, s) + rsF,(t, s) + !js2a2(t, s)F,,(t, s) - rF(t, s) = 0, 
F(T, s) = @(s). 
Summing up these results we have proved the following proposition, which is 
in fact one of the most central results in the book. 
Theorem 7.7 (Black-Scoles Equation) Assume that the market is specified 
by eqns (7.14)-(7.15) and that we want to price a contingent claim of the form 
(7.16). Then the only pricing function of the form (7.17) which is consistent 
with the absence of arbitrage is when F is the solution of the following boundary 
value problem in the domain [0, TI x R+. 
Ft(t,s) + rsF,(t, s) + ;s2a2(t, s)F,,(t, s) - rF(t, s) = 0, 
(7.31) 
F(T, s) = @(s). 
(7.32) 
Before we go on to a closer study of the pricing equation (7.31) let us make 
a few comments. 
First, it is important to stress the fact that we have obtained the price of the 
claim X in the form ll(t; X) = F(t, S(t)), i.e. the price of the claim is given as 
a function of the price of the underlying asset S. This is completely in line with 
the basic idea explained earlier, that the pricing of derivative assets is a question 
of pricing the derivative in a way which is consistent with the price of the 
underlying asset. We are thus not presenting an absolute pricing formula for 
X .  On the contrary, derivative pricing is all about relative pricing, i.e. pricing 
the derivative asset in terms of the price of the underlying asset. In particular 
this means that in order to use the technique of arbitrage pricing at all we must 
have one or several underlying price processes given a priori. 
Second, a word of criticism. At a first glance our derivation of the pricing 
equation (7.31) seems to be fairly convincing, but in fact it contains some rather 
weak points. The logic of the argument was that we assumed that the price 
of the derivative was a function F of t and S(t). Using this assumption we 
then showed that in an arbitrage free market F had to satisfy the Black-Scholes 
equation. The question now is if we really have good reasons to assume that 
the price is of the form F(t, S(t)). The Markovian argument given above sounds 
good, but it is not totally convincing. 
A much more serious objection is that we assume that there actually exists a 
' 
market for the derivative asset, and in particular that there exists a price process 
I 
for the derivative. This assumption of an existing market for the derivative is 
crucial for the argument since we are actually constructing a portfolio based on 
the derivative (and the underlying asset). If the derivative is not traded then the 

98 
ARBITRAGE PRICING 
portfolio cannot be formed and our argument breaks down. The assumption of 
an existing price for the derivative is of course innocent enough in the case of a 
standard derivative, like a European call option, which de facto is traded in large 
volumes. If, however, we want to price an OTC ("over the counter") instrument, 
i.e. an instrument which is not traded on a regular basis, then we seem to be in 
big trouble. 
Happily enough there is an alternative argument for the derivation of the 
pricing equation (7.31), and this argument (which will be given below) is not 
open to the criticism above. The bottom line is that the reader can feel safe: 
equation (7.31) really is the "correct" equation. 
Let us end by noting an extremely surprising fact about the pricing equa- 
tion, namely that it does not contain the local mean rate of return a(t, s) of 
the underlying asset. In particular this means that, when it comes to pricing 
derivatives, the local rate of return of the underlying asset plays no role whatso- 
ever. The only aspect of the underlying price process which is of any importance 
is the volatility u(t, s). Thus, for a given volatility, the price of a fixed derivat- 
ive (like a European call option) will be exactly the same regardless of whether 
the underlying stock has a lo%, a 50%, or even a -50% rate of return. At a 
first glance this sounds highly counter-intuitive and one is tempted to doubt the 
whole procedure of arbitrage pricing. There is, however, a natural explanation 
for this phenomenon, and we will come back to it later. At this point we can only 
say that the phenomenon is closely connected to the fact that we are pricing the 
derivative in terms of the price of the underlying asset. 
7.4 Risk Neutral Valuation 
Let us again consider a market given by the equations 
dB(t) = rB(t) dt, 
dS(t) = S(t)a (t, S(t)) dt + S(t)a (t, S(t)) d ~ ( t ) ,  
and a contingent claim of the form X = 3(S(T)). Then we know that the 
arbitrage free price is given by ll(t; *) = F(t, S(t)) where the function F is the 
solution of the pricing equations (7.31)-(7.32). We now turn to the question of 
actually solving the pricing equation and we notice that this equation is precisely 
of the form which can be solved using a stochastic representation formula B la 
Feynman-KG. Using the results from Section 5.5 we see that the solution is 
given by 
F(t, s) = e-r(T-t) E ~ ' S  
[*(X(T))I 9 
where the X process is defined by the dynamics 
dX(u) = rX(u) du + X(U)U(U, X(u)) dW(u), 
X(t) = s, 

RISK NEUTRAL VALUATION 
99 
I where W is a Wiener process. The important point to note here is that the SDE 
I 
(7.36) is of precisely the same form as that of the price process S. The only, but 
important, change is that whereas S has the local rate of return a, the X-process 
has the short rate of interest r as its local rate of return. 
The X-process above is logically just a technical tool, defined for the moment, 
1 
and in particular we can name it as we please. In view of the resemblance between 
1 
X and S it is rather tempting to call it S instead of X. This is perfectly acceptable 
as long as we do not confuse the "real" S-process of (7.34) with the "new" 
S-process, and one way to achieve this goal is by the following procedure. 
Let us agree to denote the "objective" probability measure which governs our 
real model (7.33)-(7.34) by the letter P. Thus we say that the P-dynamics of 
the S-process are that of (7.34). We now define another probability measure Q 
under which the S-process has a different probability distribution. This is done 
by defining the Q-dynamics of S as 
dS(t) = r S ( t )  dt + S(t)a (t, S(t)) dW(t), 
(7.38) 
where W is a Q-Wiener process. In order to distinguish the measure under which 
we take expectations we introduce some notational conventions. 
Notation convention 7.4.1 For the rest of the text, the following conventions 
a We identify the expectation operator by letting E denote expectations taken 
under the P-measure whereas EQ denotes expectations taken under the 
a We identify the Wiener process. T h w  w will denote a P- Wiener process, 
whereas W will denote a Q- Wiener process. 
The convention on W has the advantage that it is possible, at a glance, to 
decide under which measure a certain SDE is given. We will work much more 
often under Q than under P, and this is the reason why the Q-Wiener process 
/ 
W has a simpler notation than the P-Wiener pricess W. Using this notation we 
may now state the following central result for derivative pricing. 
Theorem 7.8 (Risk Neutral Valuation) The arbitrage free price of the 
claim 9 ( S ( T ) )  is given by n(t; 9) = F(t, S(t)), where F is given by the formula 
F (t , s) = e-r(T-t) E$ [@(S(T))], 
(7.39) 
where the Q-dynamics of S are those of (7.38). 
There is a natural economic interpretation of the formula (7.39). We see 
that the price of the derivative, given today's date t and today's stock price s, 
is computed by taking the expectation of the final payment E$ [@(S(T))] 
and 
then discounting this expected value to present value using the discount factor 
e-r(T-t). The important point to note is that when we take the expected value we 

100 
ARBITRAGE PRICING 
are not to do this using the objective probability measure P. Instead we shall 
use the Q-measure defined in (7.38). This Q-measure is sometimes called the 
risk adjusted measure but most often it is called the martingale measure, 
and this will be our terminology. The reason for the name is that under Q the 
normalized process ( S ( t ) / B ( t ) )  turns out to be a Q-martingale. In the deeper 
investigation of arbitrage pricing, which will be undertaken in Chapter 10, the 
Q-measure is the fundamental object of study. We formulate the martingale 
property as a separate result. 
Proposition 7.9 (The Martingale Property) In the Black-Scholes model, 
the price process II ( t )  for every traded asset, be it the underlying or derivative 
asset, has the property that the normalized price process 
is a martingale under the measure Q. 
Proof See the exercises. 
CI 
The formula (7.39) is sometimes referred to as the formula of risk neutral 
valuation. Suppose that all agents are risk neutral. Then all assets will command 
a rate of return equal to the short rate of interest, i.e. in a risk neutral world 
the stock price will actually have the Q-dynamics above (more precisely, in this 
case we will have Q = P). Furthermore, in a risk neutral world the present value 
of a future stochastic payout will equal the expected value of the net payments 
discounted to present value using the short rate of interest. Thus formula (7.39) 
is precisely the kind of formula which would be used for valuing a contingent 
claim in a risk neutral world. Observe, however, that we do not assume that 
the agents in our model are risk neutral. The formula only says that the value 
of the contingent claim can be calculated as if we live in a risk neutral world. 
In particular the agents are allowed to have any attitude to risk whatsoever, as 
long as they all prefer a larger amount of (certain) money to a lesser amount. 
Thus the valuation formula above is preference free in the sense that it is valid 
regardless of the specific form of the agents' preferences. 
7.5 T h e  Black-Scholes Formula 
In this section we specialize the model of the previous section to the case of the 
Black-Scholes model, 
dB(t) = rB(t) dt, 
(7.40) 
where cr and a are constants. From the results of the previous section we know 
that the arbitrage free price of a simple claim @(S(T)) is given by 

THE BLACK-SCHOLES FORMULA 
where the Q-dynamics of S are given by 
dS(u) = rS(u) du + oS(u) dW(u), 
(7.43) 
S(t) = s. 
(7.44) 
In this SDE we recognize our old friend GBM from Section 5.2. Using the results 
from Section 5.2 we can thus write S(T) explicitly as 
S(T) 
= sexp {(r - $a2) (T - t j  + o (W(T) - W(t))) . 
(7.45) 
Thus we have the pricing formula 
00 
F(t, s) = e-r(T-t) J__ @ (seZ) f (2) dz, 
(7.46) 
where Z is a stochastic variable with the distribution 
N [(r - f 02) (T - t), o
m
]
 
, 
and f is the corresponding density function. 
Formula (7.46) is an integral formula which, for a general choice of contract 
function a, must be evaluated numerically. There are, however, a few particular 
cases where we can evaluate (7.46) more or less analytically, and the best known 
of these is the case of a European call option, where @ has the form @(x) = 
max [x - K, 01. In this case we obtain 
00 
; E?~ [max [seZ - K, 0]] = 0 .  Q (seZ 5 K) + L(f) 
(seZ - K) f (z) dz. (7.47) 
After some standard calculations we are left with the following famous result 
which is known as the Black-Scholes formula. 
Proposition 7.10 The price of a European call option with strike price K and 
time of maturity T is given by the formula II (t) = F(t, S(t)), where 
F(t, s) = s N  [dl(t, s)] - e - r ( T - t ) ~ ~  
[d2(t, s)]. 
(7.48) 
Here N is the cumulative distribution function for the N [O,1] distribution and 
dl(t, 3) = o
m
 
{ln (a) + (r + i u 2 )  (T - t) ) , 
(7.49) 
d2(t, S) = dl(t, s).- o
m
.
 
(7.50) 
The graph of the Black-Scholes pricing function (the unit of time is chosen 
to be one year) is shown in Fig. 7.3. 

ARBITRAGE PRICING 
FIG. 7.3. The Black-Scholes price of a call option: 
K = 100, a = 0.2, T - t = 0.25 
7.6 Options on Futures 
The purpose of this section is to derive the Black formulas for options written 
on a futures contract. Our discussion here will be rather brief, and for more 
institutional and technical information the reader is referred to Chapter 26 (and 
the Notes), where the contracts are discussed in more detail. 
7.6.1 Forward Contracts 
Consider a standard Black-Scholes model, a simple T-claim X = @(ST), 
and 
assume that we are standing at time t. A forward contract on X, made at t, is 
a contract which stipulates that the holder of the contract pays the deterministic 
amount K at the delivery date T, and receives the stochastic amount X at T. 
Nothing is paid or received at the time t, when the contract is made. Note that 
forward price K is determined already at time t. It is customary to use the 
notation K = f (t; T, X), and our primary concern is to compute f (t; T, X). 
This is, however, easily done. We see that the entire forward contract is 
a contingent T-claim Y of the form 
and, by definition, the value of Y at the time t when the contract is made equals 
zero. Thus we have 
n(t; x - K )  = o, 
which leads to 
n(t; 
X) = n(t; K). 
rcjY 8i (78 

OPTIONS ON FUTURES 
103 
Using risk neutral valuation we immediately have II(t; K) = e-T(T-t)~ and 
i n(t; x) = e-~(T-t) x E?', [XI, so we have proved the first part of the following 
result. The second part is left as an exercise. 
Proposition 7.11 The forward price f (t; T, X), contracted at t, on the T-claim 
X is given by 
f (t; T, X) = EfS [XI. 
(7.51) 
In particular, if X = ST the corresponding forward price, denoted by f (t; T), is 
given by 
f (t; T) = er(T-t)~t. 
(7.52) 
Remark 7.6.1 Note the difference between the forward price f (t; T, X) which 
is a sum to be paid at T, for a forward contract entered at time t, and the spot 
price of the entire forward contract. This latter price is zero at the time t when 
the contract is made, but at any subsequent time s > t it will typically have a 
1 nonzero value. 
7.6.2 Futures Contracts and the Black Formula 
With the same setup as the previous section we will now discuss a futures 
contract on X. This contract is very close to the corresponding forward contract 
in the sense that it is still a contract for the delivery of X at T. The difference is 
that all the payments, from the holder of the contract to the underwriter, are no 
longer made at T. Let us denote the futures price by F(t; T, X); the payments 
are delivered continuously over time, such that the holder of the contract over 
the time interval [s, s + As] receives the amount 
F(s + As; T, X) - F(s; T, X) 
from the underwriter. Finally the holder will receive X, and pay F(T; T, X), at 
the delivery date T. By definition, the (spot) price (at any time) of the entire 
futures contract equals zero. Thus the cost of entering or leaving a futures con- 
tract is zero, and the only contractual obligation is the payment stream described 
above. See Chapter 26 for more details, and for a proof of the following result. 
Proposition 7.12 If the short rate is deterministic, then the forward and the 
futures price processes coincide, and we have 
We will now study the problem of pricing a European call option, with exer- 
cise date T, and exercise price K ,  on an underlying futures contract. The futures 
contract is a future on S with delivery date TI, with T < TI. Options of this 
kind are traded frequently, and by definition the holder of this option will, at the 

104 
ARBITRAGE PRICING 
exercise time T, obtain a long position in the futures contract, plus the stochastic 
amount 
X = max[F(T; T I )  - K, 01. 
Since the spot price of the futures contract equals zero, we may, for pricing 
purposes, forget about the long futures position embedded in the option, and 
identify the option with the claim in (7.54). 
We now go on to price the futures option, and we start by using 
Proposition 7.12 and eqn (7.52) in order to write 
X = e'(Tl -TI 
[ST - e-'(Tl -TI K, 01. 
Thus we see that the futures option consists of e'(Tl-T) call options on the 
underlying asset S, with exercise date T and exercise price e-r(T1-T)~. Denoting 
the price at T of the futures option by c, the stock price at t by s, and the futures 
price F(t; T I )  by F, we thus have, from the Black-Scholes formula, 
, 
= e~(Tl 
-TI IS 
[dl] - e-'(~-f Ie-'(T1 -TI KN [d2]] 
where dl and d2 are obtained from the Black-Scholes dl and dz by replacing k 
with e-r(Tl-T)~. Finally we may substitute s = ~ e - ' ( ~ l - ~ ) ,  
and simplify, to 
obtain the s*called "Black-76 formula". 
Proposition 7.13 (Black's formula) The price, at t, of a European call 
option, with exercise date T and exercise price K, on a futures contract (on 
an underlying asset price S) with delivery date TI is given by 
C = e-r(T-t) [FN[dl] - KN[d2]], 
where F is the fiturns price F = F(T; T I ) ,  and 
ln (f) + 3 a 2 ( ~  
- t )  
dl = 
u
r
n
 
, 
d2 = dl - 0-. 
7.7 Volatility 
In order to be able to use the theory derived above in a concrete situation, we 
need to have numerical estimates of all the input parameters. In the Black- 
Scholes model the input data consists of the string s ,  r ,  T, t, and u. Out of these 
five parameters, s, r, T, and t can be observed directly, which leaves us with the 
problem of obtaining an estimate of the volatility u. Here there are two basic 
approaches, namely to use "historic volatility" or "implied volatility". 

VOLATILITY 
Suppose that we want to value a European call with six months left to maturity. 
' An obvious idea is to use historical stock price data in order to estimate u. Since, 
in real life, the volatility is not constant over time, one standard practice is to 
use historical data for a period of the same length as the time to maturity, which 
in our case means that we use data for the last six months. 
In order to obtain an estimate of u we assume that we have the stand- 
ard Black-Scholes GBM model (7.4) under the objective measure P. We 
sample (observe) the stock price process S at n + 1 discrete equidistant points 
to, tl, . . . , t,, where At denotes the length of the sampling interval, i.e. At = 
ti - ti-1. 
We thus observe S(to), . . . , S(t,), and in order to estimate u we use the fact 
that S has a log-normal distribution. Let us therefore define € 1 .  . . . . E, bv 
Fkom (5.15) we see that 51,. . . ,En are independent, normally distributed random 
E [<,I = (a - iu2) At, 
Var[<,] = u 2 ~ t .  
Usine: elementarv statistical theorv we see that an estimate of u is given bv 
where the sample variance S! 
is given by 
The standard deviation. D, of the estimate u* is a~~roximativelv 
given bv 

ARBITRAGE PRICING 
106 
7.7.2 Implied Volatility 
Suppose again that we want to value a European call with six months left to 
maturity. An argument against the use of historical volatility is that in real life 
volatility is not constant, but changes over time, and thus we want an estimate 
of the volatility for the coming six months. Using historical volatility we will, 
however, only obtain an estimate for the volatility over the past six months. If, 
furthermore, our objective is to price our option consistently with respect to 
other assets which are already priced by the market, then we really should use 
the market expectation of the volatility for the next six months. 
One way of finding the market expectation of the volatility is by getting mar- 
ket price data for another six month "benchmark" option, written on the same 
underlying stock as the option which we want to value. Denoting the price of 
the benchmark option by p, the strike price by K, today's observed value of 
the underlying stock by s, and writing the Black-Scholes pricing formula for 
European calls by c(s, t, T, r, a, K), we then solve the following equation for a 
p = C(S, t, T, r, a, K). 
In other words, we try to find the value of a which the market has implicitly 
used for valuing the benchmark option. Ths value of a is called the implied 
volatility, and we then use the implied volatility for the benchmark in order to 
price our original option. Put another way, we price the original option in terms 
of the benchmark. 
We note that implied volatilities can be used to test (in a nonstandard way) 
the Black-Scholes model. Suppose, e.g. that we observe the market prices of a 
number of European calls with the same exercise date on a single underlying 
stock. If the model is correct (with a constant volatility) then, if we plot implied 
volatility as a function of the exercise price, we should obtain a horizontal straight 
line. Contrary to this, it is often empirically observed that options far out of 
the money or deep into the money are traded at higher implied volatilities than 
options at the money. The graph of the observed implied volatility function thus 
often looks like the smile of the Cheshire cat, and for this reason the implied 
volatility curve is termed the volatility smile. 
Remark 7.7.1 A call option is said to be "in the money" at time t if St > K, 
and "out of the money" if St < K. For put options the inequalities are reversed. 
If St = K the option is said to be "at the money". 
7.8 American options 
Up to now we have assumed that a contract, like a call option, can only be 
exercised exactly at the exercise time T. In real life a large number of options 
can in fact be exercised at any time prior to T. The choice of exercise time is 
thus left to the holder of the contract, and a contract with this feature is called 
an American contract. 

AMERICAN OPTIONS 
107 
To put it more formally, let us fix a final exercise date T and a contract 
function @. The European version of this contract will, as usual, pay the amount 
@(ST) at time T to the holder of the contract. If the contract, on the other hand, 
is of the American type, then the holder will obtain the amount @(St) if heishe 
chooses to exercise the contract at time t. The situation is complicated further by 
the fact that the exercise time t does not have to be chosen a priori (i.e. at t = 0). 
It can be chosen on the basis of the information generated by the stock price 
process, and thus the holder will in fact choose a random exercise time r. 
The exercise time (or rather exercise strategy) T has to be chosen such that the 
decision on whether to exercise the contract at time t or not, depends only upon 
the information generated by the price process up to time t. The mathematical 
formulation of this property is in terms of so called "stopping times", but we 
will not go further into this subject. 
American contracts are thus more complicated to analyze than their 
European counterparts, since the holder of the contract has to decide on an 
optimal exercise strategy. Mathematically this means that we have to solve 
the "optimal stopping problem" 
m u  [EQ [e-"@(ST)]], 
where T is allowed to vary over the class of stopping times. Problems of this kind 
are quite hard to solve, and analytically they lead to so called "free boundary 
value problems" (or variational inequalities) instead of the corresponding para- 
bolic PDEs for the European counterparts. The mathematics of this lies outside 
the scope of this book, but it may be of interest to know that for American 
contracts practically no analytical formulas are at hand. See the Notes below for 
One situation, however, is very easy to analyze, even for American contracts, 
and that is the case of an American call option on a nondividend paying under- 
lying stock. Let us consider an American call option with final exercise date T 
and exercise price K. We denote the pricing function for the American option 
by C(t, s) and the pricing function for the corresponding European option (with 
the same T and K) by c(t, s). 
First, we note that we have (why?) the trivial inequality 
C(t, s) L c(t, s). 
(7.56) 
Second, we have, for all t < T, the less obvious inequality 
c(t, s) 2 s - ~ e - ' ( ~ - ~ ) .  
(7.57) 
To see why this inequality holds it is sufficient to consider two portfolios, A 
and B. A consists of a long position in the European option, whereas B consists 
of a long position in the underlying stock and a loan expiring at T, with face 

108 
AItBITRAGE PRICING 
value K. Denoting the price of A and B at any time t by At and Bt respectively, 
it is easily seen that AT 2 BT regardless of the value of ST (analyze the two 
cases ST 2 K and ST < K). In order to avoid arbitrage possibilities we then 
must have At 2 Bt for all t 5 T, which is precisely the content of (7.57). 
Furthermore, assuming a positive rate of interest, we have the trivial 
inequality 
s - ~ e - ' ( ~ - ~ )  
> s - K, Vt < T, 
so we end up with the inequality 
C(t, s) > s - K, W < T. 
On the left-hand side we have the value of the American option at time t, 
whereas the right-hand side gives us the value of actually exercising the option at 
time t. Since the value of the option is strictly greater than the value of exercising 
the option, it can thus not be optimal to exercise the option at time t. Since this 
holds for all t < T, we see that it is in fact never optimal to exercise the option 
before T, and we have the following result. 
Proposition 7.14 Assume that r > 0. For an American call option, written on 
an underlying stock without dividends, the optimal exercise time I- is given by 
I- = T. Thw the pnce of the Arnericczn option coincides with the price of the 
corresponding European option. 
For American call options with discrete dividends, the argument above can 
be extended to show that it can only be optimal to exercise the option either at 
the final time T or at one of the dividend times. The American put option (even 
without dividends) presents a hard problem without an analytical solution. See 
the Notes below. 
7.9 Exercises 
Exercise 7.1 Consider the standard Blacl-Scholes model and a T-claim X of 
the form X = 3(S(T)). Denote the corresponding arbitrage free price process 
by II (t). 
(a) Show that, under the martingale measure Q, ll (t) has a local rate of 
return equal to the short rate of interest r. In other words show that 
ll (t) has a differential of the form 
dII (t) = r . II (t) dt + g(t) dW(t). 
Hint: Use the Q-dynamics of S together with the fact that F satisfies 
the pricing PDE. 
(b) Show that, under the martingale measure Q, the process Z(t) = 
(II (t) /B(t)) is a martingale. More precisely, show that the stochastic 
differential for Z has zero drift term, i.e. it is of the form 
dZ(t) = Z(t)uz(t) dW (t). 

EXERCISES 
109 
Determine also the diffusion process az(t) (in terms of the pricing 
function F and its derivatives). 
Exercise 7.2 Consider the standard Black-Scholes model. An innovative com- 
pany, F&H INC, has produced the derivative "the Golden Logarithm", 
henceforth abbreviated as the GL. The holder of a GL with maturity time 
T, denoted as GL(T), will, at time T, obtain the sum lnS(T). Note that if 
S(T) < 1 this means that the holder has to pay a positive amount to F&H INC. 
Determine the arbitrage free price process for the GL(T). 
Exercise 7.3 Consider the standard Black-Scholes model. Derive the Black- 
Scholes formula for the European call option. 
Exercise 7.4 Consider the standard Black-Scholes model. Derive the arbitrage 
free price process for the T-claim X where X is given by X = {s(T)}@. Here P 
is a known constant. 
Hint: For this problem you may find Exercises 5.5 and 4.4 useful. 
Exercise 7.5 A so called binary option is a claim which pays a certain amount 
if the stock price at a certain date falls within some prespecified interval. Oth- 
erwise nothing will be paid out. Consider a binary option which pays K SEK to 
the holder at date T if the stock price at time T is in the inerval [a, PI. Determine 
the arbitrage free price. The pricing formula will involve the standard Gaussian 
cumulative distribution function N. 
Exercise 7.6 Consider the standard Black-Scholes model. Derive the arbitrage 
free price process for the claim X where X is given by X = (S(Tl)/S(To)). The 
times To and TI are given and the claim is paid out at time TI. 
Exercise 7.7 Consider the American corporation ACME INC. The price 
process S for ACME is of course denoted in US$ and has the P-dynamics 
d S  = aSdt +aSdw1, 
where a and a are known constants. The currency ratio SEK/US$ is denoted by 
Y and Y has the dynamics 
dY = PY dt + 6Y dw2, 
where w2 is independent of w1. The broker firm F&H has invented the deriv- 
ative "Euler". The holder of a T-Euler will, at the time of maturity T, obtain 
x = ln [{z(T)}~] 
in SEK. Here Z(t) is the price at time t in SEK of the ACME stock. 
Compute the arbitrage free price (in SEK) at time t of a T-Euler, given 
that the price (in SEK) of the ACME stock is z. The Swedish short rate is 

-- 
110 
ARBITRAGE PRICING 
Exercise 7.8 Prove formula (7.52). 
Exercise 7.9 Derive a formula for the value, at s, of a forward contract on the 
T-claim X, where the forward contract is made at t, and t < s < T. 
7.10 Notes 
The classics in the field are Black and Scholes (1973), and Merton (1973). The 
modern martingale approach to arbitrage pricing was developed in Harrison and 
Kreps (1981), and Harrison and Pliska (1981). A deep study of the connections 
between (various formulations of) absence of arbitrage and the existence of a 
martingale measure can be found in Delbaen and Schachermeyer (1994). 
For a wealth of information on forward and futures contracts, see Hull (1997) 
and DufFie (1989). Black's formula was derived in Black (1976). For American 
options see Barone-Adesi and Elliott (1991), Geske and Johnson (1984) and 
Musiela and Rutkowski (1997). The standard reference for optimal stopping 
I 
problems is Shiryayev (1978), and a very readable exposition can be found in 
Bksendal (1995). Option pricing with stochastic volatility is discussed in Hull 
, 
and White (1987), and Leland (1985) studies the consequences of introducing 
transaction costs. 


## Martingale Approach to Arbitrage

"$4' " 
8 
c 
Y 
COMPLETENESS AND HEDGING 
8.1 Introduction 
In the previous chapter we noticed that our derivation of the pricing 
equation (7.31) was somewhat unsatisfactory, and a major criticism was that 
we were forced to assume that the derivative asset a priori possessed a price 
process and actually was traded on the market. In this chapter we will look 
at arbitrage pricing from a somewhat different point of view, and this altern- 
ative approach will have two benefits. First it will allow us to dispose of the 
annoying assumption above that the derivative is actually traded, and second it 
will provide us with an explanation of the surprising fact that the simple claims 
investigated earlier can be given a unique price. For a more detailed discussion 
see Chapters 10, 12, and 15. 
We start with a fairly general situation by considering a financial market with 
a price vector process S = (S1,. . . , SN), governed by an objective probability 
measure P. The process S is as usual interpreted as the price process of the 
exogenously given underlying assets and we now want to price a contingent 
T-claim X. We assume that all the underlying assets are traded on the market, 
but we do not assume that there exists an a priori market (or a price process) for 
the derivative. To avoid trivialities we also assume that the underlying market 
Definition 8.1 We say that a T-claim X can be replicated, alternatively that 
it is reachable or hedgeable, if there ezists a self-financing portfolio h such 
v h ( ~ )  
= X, P - a.s. 
(8.1) 
In this case we say that h is a hedge against X. Alternatively, h is called a 
replicating or hedging portfolio. If every contingent claim is reachable we say 
that the market is complete. 
Let us now consider a fixed T-claim X and let us assume that X can be replicated 
by a portfolio h. Then we can make the following mental experiment: 
I 1. Fix a point in time t with t 5 T. 
2. Suppose that we, at time t, possess vh(t) SEK. 
3. We can then use this money to buy the portfolio h(t). If furthermore we 
follow the portfolio strategy h on the time interval [t, T] this will cost us 
nothing, since h is self-financing. At time T the value of our portfolio will 
then be V h ( ~ )  
SEK. 

112 
COMPLETENESS AND HEDGING 
4. By the replication assumption the value, at time T, of our portfolio will 
thus be exactly X SEK, regardless of the stochastic price movements over 
the interval [t, TI. 
5. From a purely financial point of view, holding the portfolio h is thus 
equivalent to the holding of the contract X. 
6. The "correct" price of X at time t is thus given by n(t; X) = vh(t). 
For a hedgeable claim we thus have a natural price process, n(t; X) = Vh(t), 
and we may now ask if this has anything to do with absence of arbitrage. 
Proposition 8.2 Suppose that the claim X can be hedged using the portfolio h. 
Then the only price process n(t; X) which is consistent with no arbitrage is given 
by n(t; X) = vh(t). Furthermore, if X can be hedged by g as well as by h then 
Vg(t) = vh(t) holds for all t with probability 1. 
Proof If at some time t we have n(t; X) < vh(t) then we can make an arbitrage 
by selling the portfolio short and buying the claim, and vice versa if H(t; X) > 
Vh(t). A similar argument shows that we must have Vg(t) = vh(t). 
8.2 Completeness in t h e  Black-Scholes Model 
We will now investigate completeness for the generalized Black-Scholes model 
given by 
dB(t) = rB(t) dt, 
(8-2) 
dS(t) = S(t)a (t, S(t)) dt + S(t)a (t, S(t)) dW(t), 
(8.3) 
where we assume that a (t, s) > 0 for all (t, s). The main result is the following. 
Theorem 8.3 The model (8.2)-(8.3) is complete. 
The proof of this theorem requires some fairly deep results from probability the- 
ory and is thus outside the scope of this book. We will prove a weaker version of 
the theorem, namely that every simple claim can be hedged. This is often quite 
sufficient for practical purposes, and our proof of the restricted completeness 
also has the advantage that it gives the replicating portfolio in explicit form. We 
will use the notational convention h(t) = [ho (t), h* (t)] where h0 is the number 
of bonds in the portfolio, whereas h* denotes the number of shares in the under- 
lying stock. We thus fix a simple T-claim of the form X = (P(S(T)) and we now 
want to show that this claim can be hedged. Since the formal proof is of the form 
"consider the following odd construction", we will instead start by presenting a 
purely heuristic (but good) argument. This argument is, from a formal point of 
view, only of motivational nature and the logic of it is rather unclear. Since the 
argument is only heuristic the logical flaws do not matter, since in the end we 
will in fact present a rigorous statement and a rigorous proof. Before we start the 
heuristics, let us make more precise what we are looking for. Using Lemma 6.5 
we immediately have the following result. 

COMPLETENESS IN THE BLACK-SCHOLES MODEL 
113 
Lemma 8.4 Suppose that there exists an adapted process V and an adapted 
process u = [uO, u*] with 
u0 (t) + u* (t) = 1, 
(8.4) 
such that i 
dV(t) = V(t) {uo(t)r + u*(t)cw(t, S(t))) dt + V(t)u*(t)o(t, S(t)) d ~ ( t ) ,  
V(T) = @(S(T)). 
(8.5) 
Then the claim X = @(S(T)) can be replicated using u as the relative portfolio. 
The corresponding value process is given by the process V and the absolute 
portfolio h is given by 
hO(t) = uO(t)V(t) 
B(t) ' 
(8.6) 
i 
h*(t) = u* (t)V(t) 
S(t) 
- 
(8.7) 
(! ' Our strategy now is to look for a process V and a process u satisfying the 
conditions above. 
Begin Heuristics 
We assume what we want to prove, namely that X = @(S(T)) is indeed rep 
licable, and then we ponder on what the hedging strategy u might look like. 
Since the S-process and (trivially) the B-process are Markov processes it seems 
reasonable to assume that the hedging portfolio is of the form h(t) = h(t, S(t)) 
where, with a slight misuse of notation, the h in the right member of the equality 
is a deterministic function. Since, furthermore, the value process V (we suppress 
the superscript h) is defined as V(t) = hO(t)B(t) + h*(t)S(t) it will also be a 
function of time and stock price as 
V(t> = F(t, S(t)), 
(8.8; 
where F is some real valued deterministic function which we would like to knou 
more about. 
Assume therefore that (8.8) actually holds. Then we may apply the Iti 
formula to V in order to obtain the V-dynamics as 
dV = {Ft + aSFs + ~ u ~ s ~ F , , )  
dt + aSF, dW, 
(8.9' 
where we have suppressed the fact that V and S axe to be evaluated at time t 
whereas a, cr and F are to be evaluated at (t, S(t)). Now, in order to make (8.9 
look more like (8.5) we rewrite (8.9) as 
{Ft + oSF, + if S2F.. 
dV = V 
SF, 
v 
} dt + v ycrdW. 
(8.10 

114 
COMPLETENESS AND HEDGING 
Since we have assumed that X is replicated by V we see from (8.10) and (8.5) 
that u* must be given by 
(remember that we have assumed that V(t) = F(t, S(t)), and if we substitute 
(8.11) into (8.10) we get 
Comparing this expression to (8.5) we see that the natural choice for u0 is 
given by 
uo = Ft + ;a2s2 F,, 
r F  
7 
(8.13) 
but we also have to satisfy the requirement u0 + u* = 1 of (8.4). Using (8.11) 
and (8.13) this gives us the relation 
Ft+ia2S2F,, - F-SF, 
- 
r F  
F
'
 
which, after some manipulation, turns out to be the familiar Black-Scholes 
equation 
Ft + rSF, + $a2s2~,, 
- rF = 0. 
(8.15) 
Furthermore, in order to satisfy the relation F(T, S(T)) = iP(S(T)) of (8.5) 
(remember that we assume that V(t) = F (t, S(t))) we must have the boundary 
value 
F (T, s) = @(s), 
for all s E R+ . 
(8.16) 
End Heuristics 
Since at this point the reader may well be somewhat confused as to the logic 
of the reasoning, let us try to straighten things out. The logic of the reasoning 
above is basically as follows: 
We assumed that the claim X was replicable. 
Using this and some further (reasonable) assumptions we showed that they 
implied that the value process of the replicating portfolio was given as 
V(t) = F(t, S(t)) where F is a solution of the Black-Scholes equation. 
This is of course not at all what we wish to achieve. What we want to do is 
to prove that X really can be replicated. In order to do this we put the entire 
argument above within a logical parenthesis and formally disregard it. We then 
have the following result. 

COMPLETENESS IN THE BLACK-SCHOLES MODEL 
115 
Theorem 8.5 Consider the market (8.2)-(8.3), and a contingent claim of the 
form X = @(S(T)). Define F as the solution to the boundary value problem 
i 
Ft + rsF, + ~ a 2 s 2 ~ , ,  
- rF = 0, 
(8.17) 
F(T, s) = @(s). 
Then X can be replicated by the relative portfolio 
u O(t) = F(t, S(t)) - S(t)FS(t, S(t)) 
F(t, S(t)) 
7 
u*(t) = S(t)Fd(t, S(t)) 
F(t, S(t)) . 
The corresponding absolute portfolio is given by 
hO(t) = F(t, S ( t ) )  - S(t)Fs(t, S(t)) 
B(t) 
7 
(8.20) 
h*(t) = 
S(t)), 
(8.21) 
and the value process V h  is given by 
v h ( t )  = F(t, S(t)). 
(8.22) 
Proof Applying the It6 formula to the process V ( t )  defined by (8.22) and 
performing exactly the same calculations as in the heuristic argument above, 
will show that we can apply Lemma 8.4. 
The result above gives us an explanation of the surprising facts that there 
actually exists a unique price for a derivative asset in the Black-Scholes model 
and that this price does not depend on any particular assumptions about indi- 
vidual preferences. The arbitrage free price of a derivative asset is uniquely 
determined simply because in this model the derivative is superfluous. It can 
always be replaced by a corresponding "synthetic" derivative in terms of a 
replicating portfolio. 
Since the replication is done with P-probability 1, we also see that if a con- 
tingent claim X is replicated under P by a portfolio h and if P* is some other 
probability measure such that P and P* assign probability 1 to exactly the same 
events (such measures P and P* are said to be equivalent), then h will replicate 
X also under the measure P*. Thus the pricing formula for a certain claim will 
be exactly the same for all measures which are equivalent to P .  It is a well known 
fact (the Girsanov theorem) in the theory of SDEs that if we change the measure 
from P to some other equivalent measure, this will change the drift in the SDE, 
but the diffusion term will be unaffected. Thus the drift will play no part in the 

116 
COMPLETENESS AND HEDGING 
pricing equation, which explains why a does not appear in the Black-Scholes 
equation. 
Let us now list some popular claims and see which of them will fall into the 
framework above. 
X = max [S(T) - K, 0] 
(European call option) 
(8.23) 
X = S(T) - K 
(Forward contract) 
(8.24) 
T 
X = max 1; 1 S(t) dt - K, 0 
(Asian option) 
1 
L 
J 
X = S(T) - inf S(t) (Lookback contract) 
OStlT 
(8.26) 
We know from Theorem 8.3 that in fact all of the claims above can be replicated. 
For general claims this is, however, only an abstract existence result and we 
have no guarantee of obtaining the replicating portfolio in an explicit form. The 
point of Theorem 8.5 is precisely that, by restricting ourselves to simple claims, 
i.e. claims of the form X = @(S(T)), we obtain an explicit formula for the 
hedging portfolio. 
It is clear that the European call as well as the forward contract above are 
simple claims, and we may thus apply Theorem 8.5. The Asian option (also 
called a mean value option) as well as the lookback present harder problems 
since neither of these claims is simple. Instead of just being functions of the 
value of S at time T we see that the claims depend on the entire S-trajectory 
over the interval [0, TI. Thus, while we know that there exist hedging portfolios 
for both these claims, we have presently no obvious way of determining the shape 
of these portfolios. 
It is in fact quite hard to determine the hedging portfolio for the lookback, 
but the Asian option belongs to a class of contracts for which we can give a 
fairly explicit representation of the replicating portfolio, using very much the 
same technique as in Theorem 8.5. 
Proposition 8.6 Consider the model 
dB(t) = rB(t) dt, 
(8.27) 
dS(t) = S(t)a (t, S(t)) dt + S(t)a (t, S(t)) d ~ ( t ) ,  
(8.28) 
and let X be a T-claim of the fown 
where the process Z is defined by 

COMPLETENESS-ABSENCE OF ARBITRAGE 
117 
for some choice of the deterninistic function g. Then X can be replicated using 
a relative portfolio given by 
where F is the solution to the boundary value problem 
Ft +srF, + i s 2 a 2 ~ , ,  
+gFz - r F  = 0, 
F(T, s, z) = Q(s, z). 
' The corresponding value process V is given by V(t) = F(t, S(t), Z(t)), and F 
has the stochastic representation 
where the Q-dynamics are given by 
Proof The proof is left as an exercise for the reader. Use the same technique 
as in the proof of Theorem 8.5. 
Again we see that the arbitrage free price of a contingent claim is given as 
the expected value of the claim discounted to the present time. Here, as before, 
I the expected value is to be calculated using the martingale measure Q instead 
of the objective probability measure P. As we have said before, this general 
structure of arbitrage free pricing holds in much more general situations, and as 
a rule of thumb one can view the martingale measure Q as being defined by the 
property that all traded underlying assets have r as the rate of return under Q. 
It is important to stress that it is only traded assets which will have sr as the 
rate of return under Q. For models with nontraded underlying objects we have 
a completely different situation, which we will encounter below. 
8.3 Completeness- Absence of Arbitrage 
In this section, we will give some general rules of thumb for quickly determining 
whether a certain model is complete and/or free of arbitrage. The arguments 
will be purely heuristic. 

1 
118 
COMPLETENESS AND HEDGING 
Let us consider a model with M traded underlying assets plus the risk 
free asset (i.e. totally M + 1 assets). We assume that the price processes of 
the underlying assets are driven by R "random sources". We cannot give a precise 
definition of what constitutes a "random source" here, but the typical example 
is a driving Wiener process. If, e.g. we have five independent Wiener processes 
driving our prices, then R = 5. Another example of a random source would be 
a counting process such as a Poisson process. In this context it is important to 
note that if the prices are driven by a point process with different jump sizes 
I 
then the appropriate number of random sources equals the number of different 
jump sizes. 
When discussing completeness and absence of arbitrage it is important to 
I 
realize that these concepts work in opposite directions. Let the number of ran- 
dom sources R be fixed. Then every new underlying asset added to the model 
(without increasing R) will of course give us a potential opportunity of creating 
an arbitrage portfolio, so in order to have an arbitrage free market the number 
M of underlying assets must be small in comparison to the number of random 
sources R. 
On the other hand we see that every new underlying asset added to the model 
gives us new possibilities of replicating a given contingent claim, so completeness 
requires M to be great in comparison to R. 
We cannot formulate and prove a precise result here, but the following rule 
of thumb, or "mett+theorem", is nevertheless extremely useful. In concrete cases 
it can in fact be given a precise formulation and a precise proof. See Chapters 10 
and 14. We will later use the meta-theorem when dealing with problems con- 
nected with nontraded underlying assets in general and interest rate theory in 
particular. 
Meta-theorem 8.3.1 Let M denote the number of underlying traded assets in 
the model excluding the risk free asset, and let R denote the number of random 
sources. Generically we then have the following relations: 
1. ,The model is arbitrage free i f  and only if M 5 R. 
2. The model is complete if and only if M 1 R. 
3. The model is complete and arbitrage free if and only if M = R. 
As an example we take the Black-Scholes model, where we have one under- 
lying asset S plus the risk free asset so M = 1. We have one driving Wiener 
process, giving us R = 1, so in fact M = R. Using the meta-theorem above we 
thus expect the Black-Scholes model to be arbitrage free as well as complete and 
this is indeed the case. 
8.4 Exercises 
Exercise 8.1 Consider a model for the stock market where the short rate of 
interest r is a deterministic constant. We focus on a particular stock with price 

EXERCISES 
119 
process S. Under the objective probability measure P we have the following 
dynamics for the price process. 
dS(t) = aS(t) dt + oS(t) dW(t) + 6S(t-) dN(t). 
Here W is a standard Wiener process whereas N is a Poisson process with 
intensity A. We assume that a, o, 6 and X are known to us. The dN term is to 
be interpreted in the following way: 
Between the jump times of the Poisson process N, the S-process behaves 
just like ordinary geometric Brownian motion. 
1 
If N has a jump at time t this induces S to have a jump at time t. The 
, 
size of the S-jump is given by 
S(t) - S(t-) = 8 .  S(t-). 
Discuss the following questions: 
t 
(a) Is the model free of arbitrage? 
F (b) Is the model complete? 
(c) Is there a unique arbitrage free price for, say, a European call option? 
(d) Suppose that you want to replicate a European call option maturing in 
January 1999. Is it posssible (theoretically) to replicate this asset by a 
portfolio consisting of bonds, the underlying stock and European call 
option maturing in December 2001? 
Exercise 8.2 Use the Feynman-KaT: technique in order to derive a risk neutral 
valuation formula in connection with Proposition 8.6. 
Exercise 8.3 The fairly unknown company F&H INC. has blessed the market 
with a new derivative, "the Mean". With "effective period" given by [TI, T2] the 
holder of a Mean contract will, at the date of maturity T2, obtain the amount 
1 
T2 
- 
S(u) du. 
T2 - Tl , 
Determine the arbitrage free price, at time t, of the Mean contract. Assume 
that you live in a standard Black-Scholes world, and that t < TI. 
Exercise 8.4 Consider the standard Black-Scholes model, and n different 
simple contingent claims with contract functions @I,. . . ,a,. 
Let 
n 
v = 
hz (t)S.(t) 
i=l 
denote the value process of a self-financing, Markovian (see Definition 6.2) port- 
folio. Because of the Markovian assumption, V will be of the form V(t, S(t)). 
Show that V satisfies the Black-Scholes equation. 

COMPLETENESS AND HEDGING 
8.5 Notes 
Completeness is mathematically closely related to rather deep results about the 
possibility of representing martingales as sums of stochastic integrals. Using 
this connection, it can be shown that the market is complete if and only 
if the martingale measure is unique. This is developed in some detail in 
Chapters 10 and 14. See also Harrison and Pliska (1981) and Musiela and 
Rutkowski (1997). 
i 
--+$. 
:,i;;L{[,j ;,. .!.,. 2 ! .,:,. 
+,<I, , 
' .  
. 
I
,
,
 
. 
. . .  . .  
t (., 
.,. 
.\:<!, 
:J,.\::. 
1 3 . j ,  
l t x  , 
., :; ,;+>, 
. ; . i d ,  
,,, ,:j< ,,,. : 
, :, 
. 
I 
i 
, 
!,: 
. 
, . ,. 
! .. . . , ,- 8 
, '. /: ,;1:; 
!, . , 
;. 
I
:
 
i 
-
.
 
~. 
/
.
 , 
I ' b  . 
' 
C
'
 
- . 
I : ,  
., 
1 * ( :  ': >, 
s 3  
l~-,,>!,;;,:~:.' , !i,.,f : ,!,&<.::, 
, : ', 
? 
. .- 
.i s 
, 
1
.
 
, 
!~ , . ' t ,  
, 
> 
it:: <.,,:.,.-; 
.! . ,, 5%' 
,.;>',?a, 
8 
' 

9 
PARITY RELATIONS AND DELTA HEDGING 
9.1 Parity Relations 
Consider the standard Black-Scholes model. As we know from general theory 
(Theorem 8.3) this model allows us to replicate any contingent claim using a 
portfolio based on the underlying asset and the risk free asset. For a nontrivial 
claim the structure of the hedging portfolio is typically quite complicated, and 
in particular it is a portfolio which is continuously rebalanced. For practical 
purposes this continuous rebalancing presents a problem because in real life 
trading does have a cost. For managerial purposes it would be much nicer if we 
could replicate a given claim with a portfolio which did not have to be rebalanced, 
in other words a portfolio which is constant over time. Such a portfolio is known 
as a buy-and-hold portfolio. 
If we insist on using only B and S in our replicating portfolio we cannot rep 
licate any interesting claims using constant portfolios, but if we allow ourselves 
to include some derivative, like a European call option, in our hedging portfolio, 
then life becomes much simpler, and the basic result we will use is the following 
trivial linear property of pricing. 
Proposition 9.1 Let iP and !IJ 
be contract functions for the T-claims X = 
cP(S(T)) and Y = Q(S(T)). Then for any real numbers a and P we have the 
following price relation: 
n ( t ;  aiP + p.Ji) = aII(t; iP) + PII(t; 9 ) .  
(9.1) 
Proof This follows immediately from the risk neutral valuation formula (7.39) 
and the linear property of mathematical expectation. 
To set notation let c(t, s; K, T, r, a) and p(t, s; K, T, r, o) denote the price at 
time t given S(t) = s of a European call option and a European put option 
respectively. In both cases T denotes the time of maturity, K the strike price, 
whereas r and a indicate the dependence on model parameters. From time to 
time we will freely suppress one or more of the variables (t, s, K, T, r, a ) .  Let us 
furthermore consider the following "basic" contract functions: 
@s(x) = x, 
(9.2) 
iPB(x) 
1, 
(9.3) 
i P C , K ( ~ )  = max [x - K, O] . 
(9.4) 

122 
PARITY RELATIONS AND DELTA HEDGING 
The corresponding claims at the time of maturity give us one share of the stock, 
$1, and one European call with strike price K respectively. For these claims the 
prices are given by 
Let us now fix a time of maturity T and a T-claim X of the form X = 
@(S(T)), i.e. a simple claim. It is now clear that if @ is a linear combination of 
the basic contracts above, i.e. if we have 
then we may price @ in terms the prices of the basic contracts as 
Note also that in this case we may replicate the claim @ using a portfolio consist- 
ing of basic contracts that is constant over time, i.e. a "buy-and hold" portfolio. 
More precisely the replicating portfolio consists of 
a shares of the underlying stock, 
zero coupon T-bonds with face value $1, 
.yj European call options with strike price Ki, all maturing at T. 
The result above is of course interesting only if there is a reasonably large class 
of contracts which in fact can be written as linear combinations of the basic 
contracts given by (9.2), (9.3), and (9.4). This is indeed the case, and as a first 
example we consider the European put option with strike price K ,  for which the 
contract function cPpSK is defined by 
@ p , ~ ( x )  
= max [K - x, 01. 
(9.10) 
$5 
, h 
It is now easy to see (draw a figure!) that 
so we have the following secalled put-call parity relation. 

r 
THE GREEKS 
123 
Proposition 9.2 (Put-call parity) Consider a European call and a European 
put, both with strike price K and time of maturity T. Denoting the corresponding 
pricing functions by c(t, s) and p(t, s), we have the following relation: 
i In particular, the put option can be replicated with a constant (over time) port- 
folio consisting of a long position in a zero coupon T-bond with face value K, a 
long position in a European call option and a short position in one share of the 
underlying stock. 
I 
It is now natural to pose the following more general question. Which contracts 
can be replicated in this way using a constant portfolio consisting of bonds, call 
options and the underlying stock? The answer is very pleasing. 
Proposition 9.3 Fix an arbitrary continuous contract function 
with compact 
support. Then the corresponding contract can be replicated with arbitrary pre- 
cision (in sup-norm) using a constant portfolio consisting only of bonds, call 
options and the underlying stock. 
Proof It is easily seen that any affine function can be written as a linear 
combination of the basic contract functions. The result now follows from the 
: fact that any continuous function with compact support can be approximated 
uniformly by a piecewise linear function. 
9.2 The Greeks 
Let P(t, s )  denote the pricing function at time t for a portfolio based on a single 
underlying asset with price process St. The portfolio can thus consist of a pos- 
ition in the underlying asset itself, as well as positions in various options written 
on the underlying asset. For practical purposes it is often of vital importance to 
have a grip on the sensitivity of P with respect to the following. 
1. Price changes of the underlying asset. 
2. Changes in the model parameters. 
In case 1 above we want to obtain a measure of our risk exposure, i.e. how the 
value of our portfolio (consisting of stock and derivatives) will change given 
a certain change in the underlying price. At first glance case 2 seems self- 
contradictory, since a model parameter is by definition a given constant, and 
thus it cannot possibly change within the given model. This case is therefore not 
I 
t 
one of risk exposure but rather one of sensitivity with respect to misspecifications 
! 
of the model parameters. 
We introduce some standard notation. 

PARITY RELATIONS AND DELTA HEDGING 
Definition 9.4 
aP 
e = -  
at' 
All these sensitivity measures are known as "the greeks". This includes V, 
which in this case is given the Anglo-Hellenic pronounciation "vega" . A portfolio 
which is insensitive w.r.t. small changes in one of the parameters above is said to 
be neutral, and formally this means that the corresponding greek equals zero. A 
portfolio with zero delta is said to be delta neutral, and correspondingly for the 
other greeks. In the next section we will study various hedging schemes, based 
upon the greeks, but first we present the basic formulas for the case of a call 
option. See Figs 9.1-9.5 for graphs of the greeks as functions of the underlying 
stock price. 
Proposition 9.5 For a European call with strike price K and time of maturity 
T we have the following relations, with notation as in the Black-Scholes formula. 
FIG. 9.1. Delta for a European call 

THE GREEKS 

PARITY RELATIONS AND DELTA HEDGING 
FIG. 9.4. Theta for a European call 
0 
20 
40 
60 
80 
100 120 140 160 180 200 
FIG. 9.5. Rho for a European call 
Proof Use the Black-Scholes formula (7.48) and take derivatives. The (brave) 
reader is invited to carry this out in detail. The calculations are sometimes quite 
messy. 
9.3 Delta and Gamma Hedging 
As in the previous section, let us consider a given portfolio with pricing function 
P(t, s). The object is to immunize this portfolio against small changes in the 

DELTA AND GAMMA HEDGING 
underlying asset price s. If the portfolio already is delta neutral, i.e. if 
1 then we are done, but what can we do in the more interesting case when Ap # O? 
' One possibility is of course to sell the entire portfolio, and invest the sum thus 
obtained in the bank, but this is in most cases neither practically feasible, nor 
preferable. 
A more interesting idea is to add a derivative (e.g. an option or the underlying 
asset itself) to the portfolio. Since the price of a derivative is perfectly correlated 
with the underlying asset price, we should be able to balance the derivative 
against the portfolio in such a way that the adjusted portfolio becomes delta 
neutral. The reader will recognize this argument from the derivation of the Black- 
Scholes PDE, and the formal argument is as follows. 
We denote the pricing function of the chosen derivative by F(t, s), and 
x denotes the number of units of the derivative which we will add to the a priori 
given portfoli~. The value V of the adjusted portfolio is then given by 
/ In order to make this portfolio delta neutral we have to choose x such that 
aV/ds = 0, and this gives us the equation 
5 which, with obvious notation, has the solution 
Example 9.6 Let us assume that we have sold a particular derivative with 
pricing function F(t, s), and that we wish to hedge it using the underlying asset 
I itself. In (9.22) we now have P = -1 . F, whereas F is replaced by s, and we get 
1 the equation 
I 
I 
with the solution 
We thus see that the delta of a derivative gives us the number of units of the 
underlying stock that is needed in order to hedge the derivative. 
It is important to note that a delta hedge only works well for small changes in 
the underlying price, and thus only for a short time. In Example 9.6, what we did 

PARlTY RELATIONS AND DELTA HEDGING 
25 
20 - 
15 - 
10 - 
5 - 
FIG. 9.6. Linear apprcarimation of .a European call 
was to approximate the pricing function F(t, s) with its tangent, and in Fig. 9.6 
this is illustrated for the case when F is the pricing function of a European call 
option. AF equals the slope of the tangent. 
In Fig. 9.1 we have a graph of the delta of a European call, as a function of 
the underlying stock price. As time goes by the value of s (and t) will change, 
and thus we will be using an old, incorrect value of A. What is done in practice is 
to perform a discrete rebalanced delta hedge, which for the example above 
can be done dong the following lines: 
Sell one unit of the derivative at time t = 0 at the price F(0, s). 
Compute A and buy A shares. Use the income from the sale of the 
derivative, and if necessary borrow money from the bank. 
Wait one day (week, minute, second). The stock price has now changed 
and your old A is no longer correct. 
Compute the new value of A and adjust your stock holdings accordingly. 
Balance your account by borrowing from or lending to the bank. 
Repeat this procedure until the exercise time T. 
In this way the value of your stock and money holdings will approximately 
equal the value of the derivative. 
It is in fact not hard to prove (see the exercises) the following asymptotic result. 
Proposition 9.7 In a continuously rebalanced delta hedge, the value of the stock 
and money holdings will replicate the value of the derivative. 
In a (discrete) scheme of the kind above we face a dilemma concerning the 
frequency of the rebalancing points in time. If we rebalance often, we will 

DELTA AND GAMMA HEDGING 
129 
have a very good hedge, but we will also suffer from high transaction costs. 
The reason why we have to rebalance is that delta changes as the underlying 
price changes, and a measure of the sensitivity of A with respect to s is of course 
given by r = aA/as = a2P/as2. See Fig. 9.2 for a graph of the gamma of 
a European call. If gamma is high we have to rebalance often, whereas a low 
gamma will allow us to keep the delta hedge for a longer period. It is thus prefer- 
able to form a portfolio which, apart from being delta neutral, is also gamma 
neutral. 
In order to analyze this in some generality, let us again consider an a priori 
given portfolio with price function P(t, s). For future use we state the following 
trivial but important facts. 
Lemma 9.8 For the underlying stock, the delta and gamma are given by 
As = 1, 
rs = 0. 
From the fact that the gamma of the underlying stock equals zero, it follows that 
we cannot use the stock itself in order to change the gamma of the portfolio. Since 
we want the adjusted portfolio to be both delta and gamma neutral, it is also 
obvious that we need two different derivatives in the hedge. Let us thus ~IX two 
derivatives, e.g. two call options with different exercise prices or different times 
of maturity, with pricing functions F and G. We denote the number of units of 
the derivatives by XF and XG respectively, and the value of the hedged portfolio 
is now given by 
V = P(t, S) + XF . F(t, S) + XG . G(t, s). 
In order to make this portfolio both delta and gamma neutral we have to choose 
XF and XG such that the equations 
av 
-= 
as 
0, 
a2v 
-- 
as2 - O, 
are satisfied. With obvious notation we thus obtain the system 
A p + x F . A F + x G . A G = 0 ,  
(9.24) 
Fp+xF .rF + x G . r G  =0, 
(9.25) 
which can easily be solved. 

130 
PARITY RELATIONS AND DELTA HEDGING 
It is natural, and very tempting, to construct a delta and gamma neutral 
hedge by the following two step procedure: 
1. Choose XF such that the portfolio consisting of P and F is delta neutral. 
This portfolio will generally not be gamma neutral. 
2. Now add the derivative G in order to make the portfolio gamma neutral. 
The problem with this scheme is that the second step in general will destroy the 
delta neutrality obtained by the first step. In this context we may, however, use 
the fact that the stock itself has zero gamma and we can thus modify the scheme 
as follows: 
1. Choose XF such that the portfolio consisting of P and F is gamma neutral. 
This ~~ortfolio 
will generally not be delta neutral. 
2. Now add the underlying stock in order to make the portfolio delta neutral. 
Formally the value of the hedged portfolio will now be given by 
and, using the lemma above, we obtain the following system. 
This system is triangular, and thus much simpler than the system (9.24)-(9.25). 
The solution is given by 
Using the technique described above one can easily derive hedging schemes in 
order to make a given portfolio neutral with respect to any of the greeks above. 
This is, however, left to the reader. 
9.4 Exercises 
Exercise 9.1 Consider the standard Black-Scholes model. Fix the time of 
maturity T and consider the following T-claim X: 

EXERCISES 
131 
This contract can be replicated using a portfolio, consisting solely of bonds, stock 
and European call options, which is constant over time. Determine this portfolio 
I as well as the arbitrage free price of the contract. 
Exercise 9.2 The setup is the same as in the previous exercise. Here the 
contract is a secalled straddle, defined by 
Determine the constant replicating portfolio as well as the arbitrage free price 
of the contract. 
Exercise 9.3 The s e t u ~  
is the same as in the ~revious exercises. We will now 
I SD 
ext 
?d "bull spread" (see F 
take advantage of an 
pig. 9.7). with this 
increase in the ma: 
cont 
rket 
! car 
rhile 
1, to a 
being 
[ protected from a decrease. d he contract is defined by 
We have of course the relation A < B. Determine the constant replicating 
portfolio as well as the arbitrage free price of the contract. 
I 
Exercise 9.4 The setup and the problem are the same as in the previous 
exercises. The contract is defined by 

132 
PARITY RELATIONS AND DELTA HEDGING 
By definition the point C divides the interval [ A , q  in the middle, i.e B = 
(A + C)/2. 
Exercise 9.5 Suppose that you have a portfolio P with Ap = 2 and rp = 3. 
You want to make this portfolio delta and gamma neutral by using two deriv- 
atives F and G, with AF = -1, rF = 2, AG = 5 and I'G = -2. Compute the 
hedge. 
Exercise 9.6 Consider the same situation as above, with the difference that now 
you want to use the underlying S instead of G. Construct the hedge according 
r J 
to the two step scheme descibed in Section 9.3. 
I 
Exercise 9.7 Prove Proposition 9.7 by comparing the stock holdings in the 
continuously rebalanced portfolio to the replicating portfolio in Theorem 8.5 of 
the previous chapter. 
Exercise 9.8 Consider a self-financing Markovian portfolio (in continuous time) 
containing various derivatives of the single underlying asset in the Black-Scholes 
model. Denote the value (pricing function) of the portfolio by P(t, s). Show that 
the following relation must hold between the various greeks of P. 
Hint: Use Exercise 4. 
Exercise 9.9 Use the result in the previous exercise to show that if the portfolio 
is both delta and gamma neutral, then it replicates the risk free asset, i.e. it has 
a risk free rate of return which is equal to the short rate r. 
Exercise 9.10 Show that for a European put option the delta and gamma are 
given by 
Hint: Use put-all parity. 
Exercise 9.11 Take as given the usual portfolio P, and investigate how you can 
hedge it in order to make it both delta and vega neutral. 

- 
I 
I 
10 
THE MARTINGALE APPROACH 
TO ARBITRAGE THEORY* 
In this chapter, we consider a market model consisting of N + 1 a priori given 
asset price processes So, SI, . . . , SN. Typically we specify the model by giving the 
dynamics of the asset price processes under the objective probability measure P, 
and the main problems are as follows. 
Fundamental Problems 10.1 
1. Under what conditions is the market arbitrage free? 
2. Under what conditions is the market complete? 
We attack the fundamental problems above by presenting the "martingale 
approach" to financial derivatives. This is, so far, the most general approach 
existing for arbitrage pricing, and it is also extremely efficient from a computa- 
tional point of view. The answers to the problems above are given by the famous 
so called First and Second Fundamental Theorems of Mathematical Fin- 
ance, which will be .treated below. However; while these results are extremely 
general and powerful, they are also quite deep, necessarily involving hard results 
from functional analysis, so at some points we only present the main structural 
I 
ideas of the proofs. For full proofs the reader is directed to the references in the 
Notes. For the benefit of the reader who does not want to go deeply into the 
theory, we give a summary of the results in Section 10.7. That section can be 
read without reading the rest of the chapter. 
10.1 The Case with Zero Interest Rate 
We will start by considering the special case when one of the assets on the market 
is a risk free asset with zero rate of return. This may sound very restrictive, but 
we will later show how the general case easily can be reduced to this special case. 
As the basic setup we thus consider a financial market consisting of N exo- 
genously given risky traded assets, and the asset price vector is as usual 
S(t) = 
] . 
(10.1) 
We also assume that there exists a risk free asset with price process So(t). This 
will be our numeraire, and in this section we assume that in fact it is constant, 
i.e. it has zero rate of return. 

134 
THE MARTINGALE APPROACH TO ARBITRAGE THEORY 
Assumption 10.1.1 We assume that 
So(t) = 1, 
for all t 2 0. 
The So asset ean thus be interpreted as a money account in a bank with zero 
short rate. In the most general version of the theory, the risky price processes are 
allowed to be general semimartingales, but for our purposes it will be enough to 
assume that all price processes possess stochastic differentials with a finite num- 
ber of driving Wiener processes. Our fundamental problems are to find out under 
what conditions the market described above is free of arbitrage possibilities, and 
under what conditions it is complete. 
Before starting a formal discussion of this project we have to be a bit more 
precise about the set of admissible portfolios. Let us on a preliminary basis define 
a naive portfolio process as any adapted process h(t) = [ho(t), hl(t), . . . , h~(t)]. 
It then turns out that in order to construct a reasonable theory, the class of 
naive self financing portfolios is simply too big, and we have in fact the following 
strongly negative result. 
Theorem 10.1 If at least one of the assets S1,. . . , SN has a digusion term 
which is nonzero at all times, and if naive portfolio strategies are admitted, then 
the model admits arbitrage. 
Proof The idea of the proof is based upon the so called "doubling strategy" 
for the roulette. In this strategy you start by investing one dollar on black. If you 
win you stop, having won one dollar. If you lose, you bet another two dollars, 
and if you win in this bet your total gain is again one dollar. If you lose again 
you bet another four dollars, etc. Thus, as soon as you win you stop, and as 
long as you lose you double your bet. In this way, and as long as the roulette has 
positive probability for black coming up (it does not have to be evenly balanced), 
you will eventually (i.e. with probability one) win, and your net profit will be 
one dollar. 
This is an arbitrage on the roulette, and the reason that this does not work 
well in practice, like in Monte Carlo, is that it requires you to have unlimited 
credit, since at some points in the game you will have lost an enormous amount 
of money before eventually winning one dollar. Also, the time spent until you 
win is a priori unbounded although it is finite with probability one. Thus the 
probability is high that the sun (and you) has died until you get your dollar. 
In real life you do not have unlimited credit, but within our theoretical frarne- 
work credit is unlimited, and it is in fact quite simple to use our market model 
to imitate the Monte Carlo roulette wheel and the doubling strategy above in 
finite time. If you want the play to be over at t = 1 you simply invest at the 
discrete times 1 - lln; n = 1,2, . . . . You start by investing one dollar in the 
risky asset, financing by a bank loan, and then you stop as soon as you gain on 
the investment and you double your investment as long as you lose (all the time 
financing by a bank loan). It is then easy to see that you can in fact repeat this 

THE CASE WITH ZERO INTEREST RATE 
135 
arbitrage strategy an infinite number of times on any bounded interval, so with 
probability one you will become infinitely rich. 
In order to have a reasonable theory we must thus restrict the class of admis 
sible strategies to a smaller class where these doubling strategies are excluded. 
There are many ways of doing this and a commonly used one is given below. In 
order to have a compact notation we will use hs(t) as shorthand for the part of 
the portfolio which is connected to the risky assets, i.e. hs(t) = [hl(t), . . . , hN(t)], 
and we can thus write the entire portfolio h as h = [ho, hs]. 
Definition 10.2 
For any process h = [ho, hs], its value process V(t; h )  is defined by 
1 
P 
or in compact form 
C' 
An adapted process hs is called admissible if there exists a nonnegative 
real number a (which may depend on the choice of hs) such that 
l o  
hs(u) dS(u) L -a, 
for all t E [O, T]. 
(10.5) 
A process h(t) = [ho(t), hs(t)], is called an admissible portfolio process 
if hs is admissible. 
An admissible portfolio is said to be self-financing, if 
Comparing with Definition 6.2, we note that formally the self financing 
condition should be 
but since in our case So - 1, we have dSo = 0 so the self financing condition 
reduces to (10.7). This is a simple but important fact, which is highlighted by 
the following result. 

136 
THE MARTINGALE APPROACH TO ARBITRAGE THEORY 
Lemma 10.3 For any adapted process hs satisfying the admissibility condition 
(10.5)) and for any real number x, there exists a unique adapted process ho, 
such that: 
The portfolio h defined by h = [ho, hs] is self financing. 
The value process is given by 
In particular, the space KO of portfolio values, reachable at time T by means of 
a self financing portfolio with zero initial cost is given by 
h o  = { iT 
hs(t) dS(t) 1 hs is admissible 
. 1 
Proof Define ho by 
Then, by the definition of the value process, we obviously have 
and from this we obtain directly 
which shows that h is self financing. The last item is now obvious. 
We stress the fact, that the simple characterization of the zero cost reachable 
claims in (10.9) depends crucially on our assumption that So = 1. 
10.2 Absence of Arbitrage 
We consider the market model (10.1) over the finite time interval [0, TI, still with 
the assumption that So = 1. 
We now give the formal definition of a martingale measure. 
Definition 10.4 A probability measure Q on .FT is called an equivalent mar- 
tingale measure for the market model (10.1), the numeraire S1, and the time 
interval [0, TI, i f  it has the following properties: 
Q is equivalent to P on 3T. 
All price processes SO, S1, . . . , SN are martingales under Q on the time 
interval [0, TI. 

ABSENCE OF ARBITRAGE 
137 
An equzvalent martzngale measure will often be referred to as just "a martingale 
measure" or as "an EMM". If Q 
P has the property that So, SI, . . . , SN are 
local martingales, then Q is called a local martingale measure. 
1 We note that by our assumption above, So is trivially always a martingale. From 
an informal point of view, the main result of the entire arbitrage theory is the 
following not very precisely formulated Theorem. 
Theorem 10.5 (The First Fundamental Theorem) The model is arbitrage 
free essentially if and only if there exists a (local) martingale measure Q. 
This widely quoted result has the nature of a "Folk Theorem" in the sense 
that it is known to everyone and that, apart from the diffuse term "essentially", 
it is correct. Below we will discuss exactly what we mean with "essentially" in 
the formulation above, and we will also give more exact formulations of it. A 
full proof of a precise version of the First Fundamental Theorem is very hard 
and technical, and thus to a large extent outside the scope of the book. The 
main ideas, however, are quite simple and straightforward. We will present these 
ideas and we will also point out where the technical problems appear. The reader 
interested in the full story is referred to the Notes. 
10.2.1 
A Rough Sketch of the Proof 
In this section we will informally discuss the main ideas of the proof of the First 
Fundamental Theorem, and we will also point out the problems encountered. 
The proof consists of two parts: 
Existence of an EMM implies absence of arbitrage. 
Absence of arbitrage implies existence of an EMM. 
The first part is rather easy, whereas the second part is very hard. 
I: Existence of an EMM implies absence of arbitrage. This part is in 
fact surprisingly easy. To see this, let us assume that there does indeed exist a 
martingale measure Q. In our Wiener driven world this implies (see the Girsanov 
Theorem in Chapter 11) that all price processes have zero drift under Q, i.e. their 
Q dynamics are of the form 
dSi(t) = ~,(t)u,(t) 
dwQ(t), z = 1, . . . , N, 
(10.10) 
where WQ is some multidimensional Q-Wiener process and c, is some adapted 
row vector process. 
We now want to prove that there exist no arbitrage possibilities, so we assume 
that for some self financing process h, which we for the moment assume to be 

138 
THE MARTINGALE APPROACH TO ARBITRAGE THEORY 
uniformly bounded, the corresponding value process satisfies the relations 
We are thus viewing h as a potential arbitrage portfolio, and in order to prove 
absence of arbitrage we thus want to show that V(0, h) > 0. 
Since Q N P we see that we also have the relations 
Since h is self financing we have (remember that dSo = 0) 
and thus (by the boundedness assumptions) we see that V(t; h) is a Q-martingale. 
In particular we then have 
However, (10.13)-(10.14) imply that EQ [V(T; h)] > 0, so V(0; h) > 0. We 
have thus shown that (10.11)-(10.12) implies V(0; h) > 0, thereby proving the 
nonexistence of a bounded arbitrage portfolio. 
For the case of a possibly unbounded, but of course still admissible, portfolio 
we have to resort to more delicate arguments. One can then show that, since the 
value process is bounded from below it is in fact a supermartingale. Thus 
V(0; h) 2 E~ [V(T; h)] > 0, 
and the proof of this part is finished. 
11: Absence of arbitrage implies existence of an EMM. This is the really 
difficult part of the first fundamental theorem. It requires several hard results 
from functional analysis, but the basic ideas are as follows. 
In order to avoid integrability problems we assume that all asset price pro- 
cesses are bounded and we interpret "arbitrage" as "bounded arbitrage". We 
thus assume absence of arbitrage and we want to prove the existence of an 
EMM, or in more technical terms we would like to prove the existence of a 
Radon-Nikodym derivative L on 37- 
which will transform the P-measure into a 
martingale measure Q. Inspired from the simple one period model discussed in 
Chapter 3 it is natural to look for some sort of convex separation theorem, and to 

ABSENCE OF ARBITRAGE 
139 
this end we need to put our problem within a more functional analytical setting. 
Since the Radon-Nikodym derivative L should be in L1, it is natural to try to 
utilize duality between Lm and L1 so therefore we define the following sets, with 
L1 denoting L1 (52,FT, 
P) and Lm denoting Lm (R,FT, P). (Recall that ICo is 
the space of all claims which can be reached by a self financed portfolio at zero 
K : = K : ~ ~ L ~ ,  
(10.15) 
L y  = the nonnegative random variables in L*, 
(10.16) 
C = K: - Ly. 
(10.17) 
The space K: thus consists of all bounded claims which are reachable by a self 
financing portfolio at zero initial cost. The set C are those claims which are 
dominated by the claims in IC, so every claim in C can be reached by self-financing 
portfolio with zero initial cost if you also allow yourself to throw away money. 
Since we have assumed absence of arbitrage we deduce that 
c
n
~
~
 
= (0). 
(10.18) 
Now, both C and L T  are convex sets in Lm with only one point in common, so at 
this point (which is the crucial point of the argument, see below) one would like 
to refer to a convex separation theorem to guarantee the existence of a nonzero 
random variable L E L1 such that 
EP [LX] 2 0, for all X E L+w, 
(10.19) 
EP [LX] 5 0, for all X G C. 
(10.20) 
Assume for the moment that this part of the argument can be carried out. From 
(10.19) we can then deduce that in fact L 2 0, and by scaling we can choose 
L such that EP [L] = 1. We can thus use L as a Radon-Nikodym derivative 
to define a new measure Q by dQ = L d P  on FT, and Q is now our natural 
candidate as a martingale measure. 
Although the main ideas above are good, there are two hard technical 
problems which must be dealt with: 
Since L1 is not the dual of L" (in the norm topologies) we can not use a 
standard convex separation theorem. An application of a standard Banach 
space separation theorem would provide us with a linear functional L E 
(Lm )* such that (X, L) 2 0 for all X E LT and (X, L) 5 0 for all X in C, 
but since L1 is strictly included in (LOO)* we have no guarantee that L can 
be represented by an element in L1. We thus need a stronger separation 
theorem than the standard one. 
Supposing that the duality problem above can be resolved, it remains to 
prove that L is strictly positive (not only nonnegative), since otherwise we 
may only have Q << P but not Q - P. 

140 
THE MARTINGALE APPROACH TO ARBITRAGE THEORY 
10.2.2 Precise Results 
We now move on to a more formal discussion of the various versions of the First 
Fundamental Theorem. For the main proof we follow Delbaen-Schachermayer 
(1994). This will force us to use some results and concepts from functional ana- 
lysis which are outside the present text, and the reader is referred to Rudin (1991) 
for general information. The new ingredients of the full proof are as follows: 
We introduce a variation of the concept of no arbitrage, namely "No Free 
Lunch with Vanishing Risk". 
In order to obtain a duality between L1 and Lm we consider the weak* 
topologies instead of the norm topologies. 
We use the Kreps-Yan separation Theorem. 
As a first step, it turns out that the standard definition of absence of arbitrage 
is a bit too restrictive to allow us to deduce the existence of an EMM, so we 
need to modify this concept slightly. 
Definition 10.6 With notation as in the previous section, we say that the model 
admits 
No Arbitrage (NA) if 
CnL? = {O), 
No Free Lunch with Vanishing Risk (NFLVR) if 
where C denotes the closure of C in Lm. 
The no arbitrage condition is the same as before, whereas NFLVR is a slightly 
wider concept. If NFLVR does not hold then there will exist a nonzero claim 
X E L y  and a sequence Xn E C such that (Xn - XI < l l n  for all n, so in 
particular X, > -1ln. Thus; for each n there exists a self financing (zero ini- 
tial cost) portfolio generating a claim which is closer then l l n  to the arbitrage 
claim X, while the downside risk is less than lln. This is almost an arbitrage. 
As a second step we consider the weak* topology on LM generated by L1. 
It is well known (see Rudin (1991)) that with the weak* topology, the dual of 
Loo is L1 so we are now in a nice position to apply a separation theorem. More 
precisely we will need the following deep result. 
Theorem 10.7 (Kreps-Yan Separation Theorem) If C is weak* closed, 
and if 
C n L y = { o ) ,  
then there exists a random variable L E L1 such that L is P almost surely strictly 
positive, and 
E~ [L . X] 1 0, 
for all X E C. 

ABSENCE OF ARBITRAGE 
141 
Proof For a proof and references see Schachermayer (1994). 
We are now almost in business, and we see that in order for the Kreps-Yan 
Theorem to work we need to assume No Arbitrage and we also need assump 
tions which guarantee that C is weak* closed. Happily enough we have the 
following surprising result from Delbaen-Schachermayer (1994) which shows that 
the closedness of C in fact follows from NFLVR. The proof is very hard and 
therefore omitted. 
I Proposition 10.8 If the asset price processes are uniformly bounded, then the 
' condition NFLVR implies that C is weak* closed. 
I 
We can now state and prove the main result. 
Theorem 10.9 (First Fundamental Theorem) Assume that the asset price 
/ 
process S is bounded. Then there exists an equivalent martingale measure if and 
I only if the model satisfies NFLVR. 
Proof The only if part is the easy one, and the proof is already given in 
Section 10.2.1. Before going on we recall the definitions of IC and C and from 
(10.15)-(10.17). For the if part we assume NFLVR. This implies that C is weak* 
1 closed and it also (trivially) implies No Arbitrage, i.e. C n L y  = (0). We may 
thus apply the Kreps-Yan Separation to deduce the existence of a random 
variable L E L1 such that L is P almost surely strictly positive, and 
E P [ L . X ]  1 0 ,  for all X E C. 
(10.23) 
By scaling we can choose L such that E P  [L] = 1. We may thus use L as a 
Radon-Nikodym derivative to define a new measure Q by dQ = L d P  on 3 ~ ,  
and Q is now our natural candidate as a martingale measure. It follows from 
(10.23) and the definition of IC that E~ [LX] 5 0 for all X E K. Since K: is a 
linear subspace this implies that in fact EQ [XI = EP [ L X ]  = 0 for all X E IC. In 
order to prove the martingale property of Si for a fixed i, we choose fixed s and 
t with s < t, 
well as an arbitrary event A E 3,. 
Now consider the following 
self-financing portfolio strategy: 
Start with zero wealth and do nothing until time s. 
At time s buy IA units of asset No. i. Finance this by a loan in the bank. 
At time t sell the holdings of asset No. i and repay the loan. Put any 
surplus in the bank and keep it there until time T. 
Since the short rate equals zero, the initial loan (at time s) in the bank is 
paid back (at time t) by the same amount, so at time t the value of our portfolio 
is given by V(t; h) = IA [Si (t) - Si(s)]. Since the short rate equals zero this will 
also be the value of our portfolio at time T. Thus we have IA (Si(t) - Si(s)) E IC 
so we must have EQ [IA (Si(t) - Si(s))] = 0, and since this holds for all s, t and 
A E 3, we have proved that Si is a Q martingale. 

142 
THE MARTINGALE APPROACH TO ARBITRAGE THEORY 
In most applications, the assumption of a bounded S process is far to restrict- 
ive. The Delbaen-Schachermayer Theorem can however easily be extended to a 
more general case. 
Theorem 10.10 Assume that the asset price process S is locally bounded. Then 
there exists an equivalent local martingale measure zf and only if the model 
satisfies NFLVR. 
Remark 10.2.1 We note that in particular the result above will hold if the 
S process has continuous trajectories. It will also hold for an S process with 
jumps as long as the jumps are bounded. The case of an S process which is 
not locally bounded such as for example a process with lognormally distributed 
jumps at exponentially distributed times is much more difficult, and in such 
a case NFLVR is only equivalent to the existence of an equivalent measure Q 
such that S becomes a so called "sigma-martingale" under Q. See the Notes for 
references. 
10.3 The General Case 
We now relax the assumption that So E 1, and go on to consider a market model 
consisting of the price processes 
SO,~~,.-.,SN, 
i 
where we make the following assumption. 
Assumption 10.3.1 We assume that So(t) > 0 P-a.8. for all t 2 0. 
The main problem is to give conditions for absence of arbitrage in this model, 
and these are easily obtained by moving to the "normalized" economy where we 
use So as a numeraire. 
Thus: instead of looking at the price vector process S = [So, Sl, . . . , SN] we 
look at the relative price vector process S(t)/So(t), where we have used So as the 
numeraire price. This object will be studied in more detail in Chapter 24. 
Definition 10.11 The normalized economy (also referred to as the 
"2-economy ") is defined by the price vector process 2, where 
s(t> 
Z(t) = - 
So (t) ' 
i. e. 
The point of this is that in the Z economy we have a risk free asset 20 r 1, 
with zero rate of return, so the simple idea is to apply the results from the 
previous sections to the 2 economy. 
First, however, we have two price systems to keep track of: the S-system and 
the 2-system, and before going on we have to clarify the relations between these 

THE GENERAL CASE 
143 
systems. In particular, for any portfolio process h there will be associated two 
value processes, one in the S system and one in the Z system, and we thus need 
to introduce some notation. 
Definition 10.12 
A portfolio strategy is any adapted (n + 1)-dimensional process 
h(t) = [ho (t), hl (t) , . - - 7  hn (t)] 
I 
The S-value process vs(t; 
h )  corresponding to the portfolio h is given 
n 
vS(t; 
h )  = C h,(t)~,(t). 
(10.25) 
i=O 
J 
The Z-value process vZ(t; 
h )  corresponding to the portfolio h is given by 
( 
p 
A portfolio is said to be admissible if it is admissible in the sense of 
Definition 10.2 as a Z portfolio. 
1 
f., An admissible portfolio is said to be S-self-financing zf 
n 
d v s  (t; h )  = C hi (t) dSi (t). 
(10.27) 
i=O 
L 
An admissible portfolio is said to be Z-self-financing if 
n 
d v Z  (ti h )  = C hi(t) dZi(t). 
(10.28) 
i=O 
We can also make the obvious definitions of a given T-claim being S-reachable 
and Z-reachable, respectively. 
The intuitive feeling is that the concept of a self-financing portfolio should 
not depend upon the particular choice of numeraire. That this is indeed the case 
is shown by the following "Invariance Lemma". 
Lemma 10.13 (Invariance lemma) With assumptions and notation as 
above, the following hold: 
(i) A portfolio h is S-self-financing if and only i f  it is 2-self-financing. 
(ii) The value processes vS and vZ are connected by 
I 
vZ(t; 
h) = - 
1 
- vS(t; 
h). 
So (t) 

144 
THE MARTINGALE APPROACH TO ARBITRAGE THEORY 
(iii) A claim Y is S-reachable if and only if the claim 
is 2-reachable. 
The model is Z arbitrage free if and only zf it is S arbitrage free. 
Proof Items (ii) and (iii) are obvious. Thus it only remains to prove the self 
financing result, and for simplicity we assume that all processes possess stochastic 
differentials driven by a finite number of Wiener processes. Assume therefore that 
the portfolio h is S-self-financing. Denoting the scalar product between vectors 
by the "scalar dot" ., using the notation P = So, and suppressing the t-variable, 
we have from this assumption that 
1 
I 
2 = P-~S, 
(10.29) 
vS = h . ~ ,  
(10.30) 
vZ = p-fvS, 
(10.31) 
dvS = h . d ~ .  
(10.32) 
We now want to prove that in fact 
Using the It6 formula on Z = P-'S, we thus want to prove that 
d v Z  = /3-'h. dS + h s dp-' + h - dSdp-l. 
(10.33) 
Now, from- (10.31) we have 
Substituting (10.30) and (10.32) into this equation gives 
d v Z  = /3-'h . dS + h - s dp-' + dp-'h . dS, 
which is what we wanted to prove. 
We may now formulate and prove the main result concerning absence of 
arbitrage. 
Theorem 10.14 (The First Fundamental Theorem) Consider the market 
model So, S1,. . . , SN where we assume that So(t) > 0, P-a.s. for all t 2 0. 

COMPLETENESS 
145 
' 
Assume furthermore that So, S1,. . . , SN are locally bounded. Then the following 
I conditions are equivalent: 
The model satisfies NFLVR. 
There exists a measure Q N P such that the processes 
zo,zl,. .. ,ZN, 
defined through (lO.24), are local martingales under Q. 
Proof This follows directly from the Invariance Lemma and from 
p Theorem 10.10. 
Remark 10.3.1 From now on we will use the term "martingale measure" to 
/ denote the (not necessarily unique) local martingale measure of Theorem 10.14. 
; 10.4 Completeness 
In this section we assume absence of arbitrage, i.e. we assume that there exists a 
(local) martingale measure. We now turn to the possibility of replicating a given 
contingent claim in terms of a portfolio based on the underlying assets. This 
problem is most conveniently carried out in terms of normalized prices, and we 
have the following useful lemma, which shows that hedging is equivalent to the 
existence of a stochastic integral representation of the normalized claim. 
b Lemma 10.15 Consider a given T-claim X .  Fix a martingale measure Q and 
assume that the normalized claim X/So(T) is integrable. If the Q-martingale M ,  
defined bu 
admits an integral representation of the form 
then X can be hedged in the S-economy. Furthermore, the replicating portfolio 
, (ho, hl,. . . , h ~ )  
lis given by (10.35) for (hl,. . . , hK), whereas ho is given by 
: ho(t) = M(t) - c,N_I hi(t)Zi(t). 
Proof We want to hedge X in the S economy, i.e. we want to hedge X/So(T) in 
the Z economy. In terms of normalized prices, and using the Invariance Lemma, 
we are thus looking for a process h = (ho, hl, . . . , h ~ )  
such that 

146 
THE MARTINGALE APPROACH TO ARBITRAGE THEORY 
where the normalized value process is given by 
N 
vZ(t; 
h) = ho(t) 1 + C h,(t)&(t). 
i=l 
A reasonablk guess is that M = vZ, so we let M be defined by (10.34). 
Furthermore we define (hl, . . . , h N )  by (10.35), and we define ho by 
N 
ho(t) = M(t) - C hs(t)Z*(t). 
r=l 
Now, from (10.38) we obviously have M = vZ, 
and from (10.35) we get 
N 
dvZ = dM = C h, dZ,, 
i=l 
which shows that the portfolio is self financing. Furthermore we have 
which shows that X is replicated by h. 
We thus see that, modulo some integrability considerations, completeness is 
equivalent to the existence of a martingale representation theorem for the dis- 
counted price process. Thus we may draw on the deep results of Jacod (1979) 
from semimartingale theory which connect martingale representation properties 
for Z with the extremal points of the set of martingale measures. 
Theorem 10.16 (Jacod) Let M denote the (convex) set of equivalent mar- 
tingale measures. Then, for any fied Q € M ,  the following statements are 
equivalent. 
Every Q local martingale M has dynamics of the form 
N 
dM(t) = C hi (t) dZi(t). 
i=l 
Q is an extremal point of M .  
We then have the second fundamental theorem of mathematical finance. 
Theorem 10.17 (The Second Fundamental Theorem) Assume that the 
market is arbitrage free. Then the market is complete if and only if the martingale 
measure is unique. 

MARTINGALE PRICING 
147 
Proof If the martingale measure Q is unique then M is a singleton M = {Q) 
so Q is trivially an extremal point of M. Thus the Jacod Theorem provides 
us with a stochastic integral representation of every Q-martingale, and it then 
follows from Lemma 10.15 that the model is complete. The other implication 
follows easily from (10.56) of Proposition 10.25. 
Remark 10.4.1 The reader may find the proof given above rather abstract, 
and we provide two alternatives: 
A more functional analytic proof of the Second Fundamental Theorem 
would be roughly as follows: The market is unique if and only if the set C 
t 
of reachable claims at zero initial cost has codimension one, i.e. if 
Lw = C $ R . Y  
for some Y E Lm. This implies that the separating hyperplane implied 
by the Kreps-Yan Theorem (10.7) is ,unique and thus that the martingale 
measure is unique. 
In Section 14.3 we provide a self-contained and complete proof of the 
Second Fundamental Theorem for the special case of purely Wiener driven 
I 
models. 
10.5 Martingale Pricing 
We now turn to the pricing problem for contingent claims. In order to do this, 
we consider the "primary" market So, Sl, . . . , SN as given a priori, and we fix a 
T-claim X. Our task is that of determining a "reasonable" price process II(t; X) 
for X, and we assume that the primary market is arbitrage free. There are two 
main approaches: 
1 
The derivative should be priced in a way that is consistent with the 
prices of the underlying assets. More precisely we should demand that the 
extended market II( ; X )  , So, 4 , .  . . , SN is free of arbitrage possibilities. 
If the claim is attainable, with hedging portfolio h, then the only 
t 
reasonable price is given by n(t; X) = V(t; h). 
1 
In the first approach above, we thus demand that there should exist a martin- 
gale measure Q for the extended market II (X) , So, Sl, . . . , SN. Letting Q denote 
such a measure, assuming enough integrability, and applying the definition of a 
martingale measure we obtain 
We thus have the following result. 

148 
THE MARTINGALE APPROACH TO ARBITRAGE THEORY 
Theorem 10.18 (General Pricing Formula) The arbitrage free price pro- 
cess for the T-claim X is given by 
n(t; X )  = S O ( ~ ) E ~  - 
[ so?T) I .
I
 
(10.41) 
where Q is the (not necessarily unique) martingale measure for the a priori given 
market So, S1,. . . , S N ,  with So as the numemire . 
Note that different choices of Q will generically give rise to different price 
processes. 
In particular we note that if we assume that if SO is the money account 
where r is the shorturate, then (10.41) is reduced to the familiar "risk neutral 
valuation formula". 
Theorem 10.19 (Risk Neutral Valuation Formula) Assuming the ezist- 
ence of a short rate, the pricing formula takes the form 
, n(t; X )  = EO [e- 
r(s) d s ~ I  F~] 
, 
(10.42) 
where Q is a (not necessarily unique) martingale measure with the money account 
as the numemire. 
For the second approach to pricing let us assume that X can be replicated 
by h. Since the holding of the derivative contract and the holding of the replic- 
ating portfolio are equivalent from a financial point of view, we see that price of 
the derivative must be given by the formula 
n(t; X )  = V ( t ;  h). 
(10.43) 
One problem here is what will happen in a case when X can be replicated bv 1 
- - 
two different portfolios, and one would also like to know how this'formula is 
connected to (10.41). 
Defining n ( t ;  X )  by (10.43) we see that n(t; X )  /So(t) = V Z ( t )  and 
since, assuming enough integrability, vZ is a &-martingale, we see that also 
ll(t; X) /So(t) is a Q-martingale. Thus we again obtain the formula (10.41) and 
for a attainable claim we have in particular the formula 
V ( t ;  h) = so(t)EQ [ 14, 
(10.44) 
which will hold for any replicating portfolio and for any martingale measure Q. 
Thus we see that the two pricing approaches above do in fact coincide on the set 
of attainable claims. In Section 10.7 we will summarize our results. 
v 

STOCHASTIC DISCOUNT FACTORS 
149 
I 10.6 Stochastic Discount Factors 
I In the previous sections we have seen that we can price a contingent T-claim X 
' by using the formula 
1 where Q is a martingale measure with the money account as a numeraire. In some 
applications of the theory (in particular in asset pricing) it is common to write 
this expected value directly under the objective probability measure P instead 
I of under Q. This can easily be obtained by using the likelihood process L, where 
1 as usual L is defined on the interval [0, T] through 
I 
Using the Abstract Byes' Formula we can now write (10.45) as 
which naturally leads us to the following definition. 
Definition 10.20 Assume the existence of a short rate r. For any fixed martin- 
gale measure Q, let the likelihood process L be defined by (10.46). The stochastic 
discount factor (SDF) process A, corresponding to Q, is defined as 
We thus see that there is a one-to-one correspondence between martingale 
measures and SDFs. We have now more or less proved the following result. 
Proposition 10.21 Assume absence of arbitrage. With notation as above, the 
following hold: 
For any suficiently integrable T-claim X ,  the arbitrage free price is 
given by 
For any arbitrage free asset price process S(derivative or underlying) the 
process 
A(t>s(t) 
(10.49) 
is a (local) P-martingale. 

150 
THE MARTINGALE APPROACH TO ARBITRAGE THEORY 
The P-dynamics of A is given by 
Proof The remaining details of the proof are left to the reader. 
0 
Although SDFs and martingale measures are logically equivalent, it is often 
convenient to be able to switch from one to the other. The main advantage of 
using the martingale measure formalism is that it provides us with a canonical 
decomposition of the SDF as the (inverse) bank account multiplied by the like- 
lihood process L, and we can then use the deep and well established theory for 
likelihood processes (see Chapter 11). 
We may.,also, in the obvious way, define stochastic discount factors for other 
choices of the numeraire then the money account. 
An alternative approach to SDFs is to define an SDF as any nonnegative ran- 
dom process A possessing the property that S(t)A(t) is a (local) P-martingale for 
every asset price process S. The First Fundamental Theorem can then be restated 
as the equivalence between absence of arbitrage and the existence of an SDF. 
10.7 Summary for the Working Economist 
In this section we summarize the results for the martingale approach. We con- 
sider a market model consisting of the asset price processes So, Sl, . . . , SN on 
the time interval [O,T]. The "numeraire process" So is assumed to be strictly 
positive. Modulo some technicalities we then have the following results. The first 
provides conditions for absence of arbitrage. 
Theorem 10.22 (First Fundamental Theorem) The market model is f i e  
of arbitrage if and only if there exists a martingale measure, i.e. a measure 
Q N P such that the processes 
are (local) martingales under Q. 
For the case when the numeraire is the money account we have an alternative 
characterization of a martingale measure. The proof is a simple application of 
the It6 formula. 
Proposition 10.23 If the numeraire So is the money account, i.e. 
where r is the (possibly stochastic) short rate, and if we assume that all processes 
are Wiener driven, then a measure Q N P is a martingale measure if and only 


## Black-Scholes from Martingale Viewpoint

SUMMARY FOR THE WORKING ECONOMIST 
151 
if all assets So, S I ,  . . . , SN have the short rate as their local rates of return, i.e. 
if the Q-dynamics are of the form 
dSi(t) = Si(t)r(t) dt + Si(t)ai(t) d w Q ( t ) ,  
(10.51) 
where WQ is a (multidimensional) Q- Wiener process. 
The second result gives us conditions for market completeness. 
Theorem 10.24 (Second Fundamental Theorem) Assuming absence of 
arbitrage, the market model is complete if and only if the martingale measure 
Q is unique. 
As far as pricing of qontingent claims is concerned the theory can be 
summarized as fpllows. 
Proposition 10.25 
, 1. In order to avoid arbitrage, X must be priced according to the formula 
n(t; x) = so(t)~Q - 
[ so?T) I 
(10.52) 
e: 
where Q is a martingale measure for [So, &, . . . , SN], with So as the 
numeraire. 
2. In particular, we can choose the bank account B(t) as the numeraire. Then 
B has the dynamics 
dB(t) = r(t)B(t) dt, 
(10.53) 
where r is the (possibly stochastic) short rate process. In this case the 
pricing formula above reduces to 
n(t; X )  = EQ [e-s:r(s)ds~I F ~ ]  
. 
(10.54) 
3. Different choices of Q will generically give rise to diferent price processes 
for a jked claim X .  However, if X is attainable then all choices of Q will 
produce the same price process, which then is given by 
H(t; X )  = V(t; h), 
(10.55) 
5 
where h is the hedging portfolio. Different choices of hedging portfolios (zf 
such exist) will produce the same price process. 
4. In particular, for every replicable claim X it holds that 
~ ( t ;  
h) = EQ [ e - J T r ( s ) d s ~ I  
~
t
]
 
. 

152 
THE MARTINGALE APPROACH TO ARBITRAGE THEORY 
Summing up we see that in a complete market the price of any derivative 
will be uniquely determined by the requirement of absence of arbitrage. The 
price is unique precisely because the derivative is in a sense superfluous-it can 
equally well be replaced by its replicating portfolio. In particular we see that the 
price does not depend on any assumptions made about the risk-preferences of 
the agents in the market. The agents can have any attitude towards risk, as long 
as they prefer more (deterministic) money to less. 
In an incomplete market the requirement of no arbitrage is no longer suffi- 
cient to determine a unique price for the derivative. We have several martingale 
mevures, all of which can be used to price derivatives in a way consistent with 
no arbitr~ge. The question which martingale measure one should use for pricing 
has a very simple answer: The martingale measure is chosen by the market. 
Schematically speaking the price of a derivative is thus determined by two 
major factors. 
1. We require that the derivative should be priced in such a way as to 
not introduce arbitrage possibilities into the market. This requirement is 
reflected by the fact that all derivatives must be priced by formula (10.52) 
where the same Q is used for all derivatives. 
2. In an incomplete market the price is also partly determined by aggregate 
supply and demand on the market. Supply and demand for a specific deriv- 
ative are in turn determined by the aggregate risk aversion on the market, 
as well as by liquidity considerations and other factors. All these aspects 
are aggregated into the particular martingale measure used by the market. 
Let us now assume that we have specified some model under the objective 
probability measure P. This means that we have specified the P-dynamics of all 
asset prices in the primary market. We may also have specified the P-dynamics of 
some processes which are not price processes, like the inflation rate, the unem- 
ployment rate, or the outside temperature (which influences the demand for 
electric energy). 
In order to be able to apply the theory developed above, it is then clear that 
we need the following tools: 
We need to have full control of the class of equivalent measure transform- 
ations that can be made from a given objective measure P. 
Given an equivalent measure Q (a potential martingale measure), we must 
be able to write down the Q-dynamics of all processes under consideration. 
We need theorems which allow us to write certain stochastic variables (typ 
ically contingent claims) as stochastic integrals of some given processes 
(typically normalized asset prices). 
All these tools are in fact provided by the following mathematical results 
which are the objects under study in the next chapter. 
a The Martingale Representation Theorem for Wiener processes. 
The Girsanov Theorem. 

NOTES 
10.8 Notes 
The martingale approach to arbitrage pricing was developed in Harrison 
and Kreps (1979), Kreps (1981), and Harrison and Pliska (1981). It was 
then extended by, among others, Duffie and Huang (1986), Delbaen (1992), 
Schachermayer (1994), and Delbaen and Schachermayer (1994). In this chapter 
we follow closely Delbaen and Schachermayer (1994) for the case of loc- 
ally bounded price processes. The general case of unbounded price processes 
and its connection to sigma-martingales was finally resolved in Delbaen and 
Schachermayer (1998), which also contains further bibliographic information on 
this subject. Rudin (1991) is a standard reference on functional analysis, which 
is also treated in Royden (1988). 
Stochastic discount factors are treated in Duffie (2001), and in most modern 
textbooks on asset pricing such as Cochrane (2001). 
5 
I 
. I 
i 
'
I
 
11 
% 
B 
i 
\+&+ 
t I f S ! < . f i  
.,L3c {,i 
t 
1 
r 
.%>< .j -1,i 
+: 
$< 
&<. , 
3 '  
[ , ! ' f ,  
{ f ~ , - ( % 7 < s \  
6 7  ' 
3 
: 1 

THE MATHEMATICS OF THE 
MARTINGALE APPROACH* 
Iri this ,chapter, we will present the two main workhorses of the martingale 
approach to arbitrage theory. These are: 
The Martingale Representation Theorem, which shows that in a Wiener 
world every martingale can be written as a stochastic integral w.r.t. the 
underlying Wiener process. 
The Girsanov Theorem, which gives us complete control of all absolutely 
continuous measure transformations in a Wiener world. 
11.1 Stochastic Integral Representations 
Let us consider a fixed time interval [O,T], a probability space ( M , F ,  P), 
with some filtration {Ft't),,o, 
and an adapted vector Wiener process W = 
(WI,. . . , Wd)*. Now fix a vector process h = (hi,. . . , hd) which is "integrable 
enough" (e.g. h E E2 is enough) and a real number xo. If we now define the 
process M by 
then we know that M is a martingale. In other words: under mild integrability 
conditions, every stochastic integral w.r. t . a Wiener process is an Ft-martingale. 
A very natural and important question is now whether the converse holds, i.e. 
if every Ft-adapted martingale M can be written in the form (11.1). If this is 
indeed the case, then we say that M has a stochastic integral representation 
w.r.t. the Wiener process W. 
It is not hard to see that in the completely general case, there is no hope for 
a stochastic integral representation w.r.t. W for a general martingale M. As a 
counterexample, let W be scalar (i.e. d = 1) and consider, apart from W, also 
a Poisson process N, with constant intensity A, where N is independent of W. 
Now define the filtration by Ft = 3FN, i.e. Ft contains all the information 
generated by W and N over the interval [0, t]. 
It is now very easy to see that the process M defined by 
is an &-martingale. If we look at the trajectories of M, they consist of straight 
lines with downward slope A, interrupted at exponentially distributed points 

STOCHASTIC INTEGRAL REPRESENTATIONS 
155 
I in time by positive jumps of unit size. From this it is obvious that M can 
possess no stochastic integral representation of the form (11.1), since any such 
, representation implies that M has continuous trajectories. The intuitive reason 
is of course that since M is independent of W, we cannot use W in order to 
represent M. 
From this example it is clear that we can only hope for a stochastic integ- 
ral representation result in the case when {.Ft}t,o is the internal filtration 
1 generated by the Wiener process W itself. We start with the following basic 
1 representation for Wiener functionals, which in turn will give us our martingale 
representation result. 
Theorem 11.1 (Representation of Wiener Functionals) Let W 
be 
a 
d-dimensional Wiener process, and let X be a stochastic variable such that 
X E F F ,  
E [[XI] < m. 
Then there exist uniquely determined .Ftw-adapted processes hl, . . . , hd, such that 
X has the representation 
X = E [XI + 1 ' h, ( s )  d Wi (s) 
i=l 0 
Under the additional assumption 
f 
1 then hl, . . . , hd are in E2 
Proof We only give the proof for the L2 case, where we present the main ideas 
of a particularly nice proof from Steele (2001). For notational simplicity we only 
consider the scalar case. 
We start by recalling that the GBM equation 
has the solution 
X - -+u2t+uwt 
t - e  
Writing the SDE on integral form as 

156 
THE MATHEMATICS OF THE MARTINGALE APPROACH 
and plugging (11.3) into (11.4) we obtain, after some reshuffling of terms, 
Using the same argument we easily obtain, for s 5 t, 
where the important point is that the integral is only over the interval [s, t]. Thus 
any stochastic variable Z of the form 
Z = exp {a(Wt - W,)) 
will have a representation of the form 
where h E 0 outside [s, t]. From this it follows easily (see the exercises) that any 
variable Z of the form 
where 0 5 to 5 tl 5 . . . 5 t, 5 T, has a representation of the form 
It is now fairly straightforward to see that also any variable of the form 
n 
z = n exp {iok (WT. - WT.-,)} 
9 
(11.8) 
k=l 
where i is the imaginary unit, has a representation of the form (11.7). At this 
point we may use Fourier techniques to see that the set of variables of the form 
(11.8) is dense in the (complex) space L2(FT), and from this one can deduce 
that in fact every Z E L2(FT) has a representation of the form (11.7). See Steele 
(2001) for the details. 
From this result we now easily obtain the martingale representation theorem. 

STOCHASTIC INTEGRAL REPRESENTATIONS 
157 
Theorem 11.2 (The Martingale Representation Theorem) Let W be a 
d-dimensional Wiener process, and assume that the filtration % is defined as 
Let M be any Ft-adapted martingale. Then there exist uniquely determined 
Ft-adapted processes hl, . . . , hd such that M has the representation 
If the martingale M is square integrable, then hl, . . . , hd are in .H2. 
Proof From Theorem 11.1 we have 
The result now follows by taking conditional expectations and using the fact 
that M as well ai the stochastic integral is a martingale. 
It is worth noticing that the martingale representation theorem above is an 
abstract existence result. It guarantees the existence of the processes hl, . . . , hd, 
but it does not tell us what the h process looks like. In fact, in the general case 
we know very little about what exact form of h. The most precise description 
of h obtained so far is via the secalled Clarc-Ocone formula (see the Notes), 
but that requires the use and language of Malliavin calculus so it is outside the 
present text. 
In one special case, however, we have a rather explicit description of the integ- 
rand h. Let us therefore assume that we have some a priori given n-dimensional 
process X with dynamics of the form 
where W is as above, whereas p and a are adapted processes taking values in Rn 
and M(n, d), respectively. Let us now assume that the martingale M is of the 
very particular form M ( t )  = f (t, X ( t ) )  for some deterministic smooth function 
f (t , x) . From the It6 formula we then have 
where A is the usual Ito operator. Now; since f (t,Xt) was assumed to be a 
martingale, the drift must vanish, so in fact we have 

158 
THE MATHEMATICS OF THE MARTINGALE APPROACH 
Written out in more detail this becomes 
where ai is the ith row of a. In this particular case we thus have the explicit 
description of the integrand h as 
(t, X(t))ai (t), i = 1, . . . , d. 
11.2 The Girsanov Theorem: Heuristics 
We now start a discussion of the effect that an absolutely continuous measure 
transformation will have upon a Wiener process. This discussion will lead us to 
the Girsanov Theorem which is the central result of the next section. 
Assume therefore that our space (52, F, 
P, z) carries a scalar P-Wiener pre 
cess WP, and that for some fixed T we have changed to a new measure Q on 
FT by choosing a nonnegative random variable LT E FT and defining Q by 
This measure transformation will generate a likelihood process (see Section C.3) 
{Lt; t 2 0) defined by 
L~ = - 
dQ 
on F ~ ,  
d P  ' 
and from Proposition C.12 we know that L is a P-martingale. 
Since L is a nonnegative P-martingale, and since any (suitably integrable) 
stochastic integral w.r.t. W is a martingale, it is natural to define L as the 
solution of the SDE 
for some choice of the process cp. 
It thus seems that we can generate a large class of natural measure 
transformations from P to a new measure Q by the following prescription: 
Choose an arbitrary adapted process h. 
Define a likelihood process L by 

b 
THE GIRSANOV THEOREM: HEURISTICS 
Define a new measure Q by setting 
on Ft for all t E [0, TI. 
/ 
By applying the It6 formula we easily see that we can express L as 
L t - e  
- J:~.d~;-t.f,t~:ds, 
so L is nonnegative,kvhich is necessary if it is going to act as a likelihood pro- 
cess. If cp is integrable enough (see the Novikov condition below) it is also clear 
(why?) that L is a martingale and the initial condition Lo = 1 guarantees that 
EP [Lt] = 1. 
To see what the dynamics of WP are under Q, let us first recall that if a 
process X has the dynamics 
then the drift p and (squared) diffusion a has the interpretation of being the con- 
ditional drift and quadratic variation processes respectively. A bit more precisely, 
but still heuristically, we have 
EP [dXt I 3 t ]  = dt, 
E~ [(dxt121 K] = 02 dt, 
where we have the informal interpretation dXt = Xt+dt - Xt. Let us now define 
the process X by X = WP, i.e. we have p = 0 and a = 1 under P. Our task is 
to compute the drift and diffusion under Q and for that we will use the Abstract 
Bayes' Theorem (B.41). Using the fact that L is a P-martingale, and recalling 
that dXt E 3t+dt 
(see definition above), we obtain 
- 
- EP [Lt dXt + dLt dXt 1 Ft] 
Lt 
- 
- E' 
[Lt dXt 1 h] 
+ EP ( dLt dxt 1 3tI 
Lt 
Lt 
i Since L is adapted (so Lt E Ft) and X has zero drift under P, we have 

160 
THE MATHEMATICS OF THE MARTINGALE APPROACH 
Furthermore we have 
dLt dXt = Ltcpt dW; 
(0. dt + 1 - d~:) = Ltcpt (dw;)' 
= Ltpt dt. 
Using this and the fact that Ltvt E Ft we get 
EP [dLt dXtI3tl - Ltcpt 
Lt 
- -dt 
= cpt dt. 
Lt 
Using the fact that under P we have dX? = dt we can also easily compute 
the quadratic variation of X under Q as 
EQ [ ( d ~ t , '  I3t] = EP [~t+dt . (dxt12 IFt] 
. - - EP [~t+dt . d t l ~ t ]  
fit 
Lt 
Summing up we have thus obtained the formal relations 
EQ [dXtI 3t] = cpt dt, 
EQ [(dxt)'l fi] = 1 .  dt, 
or in other words: 
The process X = wP was, under P, a standard Wiener process with unit 
diffusion term and zero drift. 
o Under the probability measure Q defined above, the drift process for X 
has changed from zero to cp, while the diffusion term remains the same as 
under P (i.e. unit diffusion). 
11.3 The Girsanov Theorem 
Rephrasing the results of the previous discussion, we thus see that we should be 
able to write the P-Wiener process wP as 
where WQ is a Q-Wiener process. This is precisely the content of the Girsanov 
Theorem, which we now formulate. 
Theorem 11.3 (The Girsanov Theorem) Let WP be 
a d-dimensional 
standard P-Wiener process on (O,F, P,$) and let cp be any d-dimensional 

THE GIRSANOV THEOREM 
161 
j 
adapted column vector process. Choose a @ed T and define the process L on 
I 
10, TI by 
/ 
Assume that 
E~ [LT] = 1, 
and define the new probability measure Q on 3 T  by 
1 Then 
[ 
dw: 
= cpt dt + dw?, 
where WQ is a Q- Wiener process. 
Remark 11.3.1 An equivalent, but perhaps less suggestive, way of formulating 
the conclusion of the Girsanov Theorem is to say that the process WQ, defined by 
is a standard Q-Wiener process. 
Proof We only give the proof in the scalar case, the multidimensional case 
being a straightforward extension. Using the formulation in Remark 11.3.1 we 
thus have to show that, for s < t and under Q, the increment W? - W: 
is 
independent of FS, 
and normally distributed with zero mean and variance t - s. 
We start by considering the special case when s = 0 and we thus want ta show 
that, for any t, W? is normal with zero mean and variance t under Q. Using 
characteristic functions it is thus enough to show that for all t E R+ and u E R 
we have 
EQ [ e i ~ ~ F ]  
= e- $t 9 
To show this, let us choose any fixed u, and define the process Z by 

162 
THE MATHEMATICS OF THE MARTINGALE APPROACH 
The dynamics of Z are given by 
dzt = Lt . d(eiuwp) + eiuwpd~t 
+ d(eiuw?) . 
(11.21) 
From the definitions we have 
dLt = ptLt dw,P, 
dw? = dw; - cpe dt, 
so, remembering that wP is P-Wiener, the It6 formula gives us 
Plugging this, and the L-dynamics above into (11.21), we obtain 
u2 
dZt = iuZt dw; - iuZtcpt dt - -Zt dt + ptZt d ~ ;  
+ iucptZt dt 
2 
u2 
= {iuZt + cptZt) d w r  - - 
Zt dt. 
2 
i 
Since wP is P-Wiener, standard technique gives us 
I 
us 
E~ [Zt] = e - ~ ' ~ ,  
which finishes the proof in the special case when s = 0. 
In the general case we want to prove that for any s 5 t 
and this is equivalent (why?) to proving that 
for every A E 3,. To prove (11.22) we define, for fixed s and A E FS, 
the process 
{zt;t L s) by 
! 
Zt = Lt - IA - e iu(w,Q - w.Q) , 
and then we can proceed exactly as above. 
Remark 11.3.2 The process cp above will often be referred to as the Girsanov 
t 
kernel of the measure transformation. 

THE GIRSANOV THEOREM 
163 
Remark 11.3.3 In the formulation above we have used vector notation. 
Written on component form, and with obvious notation, the L-dynamics will 
have the form 
d 
dL(t) = L(t) C cp&) d ~ P ( t ) ,  
i=l 
and explicit form of L will be given by 
d 
t 
t d 
~ ( t )  
= exp ( ~ 1  
vi(s) ~WP(S) - / 
0 ~ ~ : ( s ) d s )  
j=l 
Since this process is so important it has a name of it's own: 
Definition 11.4 For any Wiener process W and any kernel process cp, the 
Doleans exponential process & is defined by 
& (cp * W) (t) = exp {l 
cp*(s) d ~ ( s )  
- ; 
Jdf llcp112(~) ds) 
(11.23) 
With notation as above we thus have 
L(t) = E (cp * W) (t). 
(11.24) 
Remark 11.3.4 Note that in the Girsanov Theorem we have to assume ad hoc 
that h is such that EP [LT] = 1 or, in other words, that L is a martingale. The 
problem is one of integrability on the process Lcp, since otherwise we have no 
guarantee that L will be a true martingale and in the general case it could in fact 
happen that EP [LT] < 1. A sufficient condition for E~ [LT] = 1 is of course that 
the process L . cp is in E2 but it is not easy to give a general a priori condition 
on cp only, which guarantees the martingale property of L. This problem used 
to occupy a minor industry, and the most general result so far is the "Novikov 
Condition" below. 
Lemma 11.5 (The Novikov Condition) Assume that the Girsanov kernel cp 
EP [e: I: 
It** ll'dt] < 
(11.25) 
Then L is a martingale and in particular E~ [LT] = 1. 
There are counter examples which show that the exponent $ in the Novikov 
condition cannot be improved. 

164 
THE MATHEMATICS OF THE MARTINGALE APPROACH 
11.4 The Converse of the Girsanov Theorem 
If we start with a measure P and perform a Girsanov transformation, according 
to (11.16)-(11.20), to defme a new measure Q, then we know that Q << P. 
A natural question to ask is now whether all absolutely continuous meas- 
ure transformations are obtained in this way, i.e. by means of a Girsanov 
transformation. 
It is clear that in a completely general situation, this cannot possibly be 
true, since the Girsanov transformation above is completely defined in terms 
of the Wiener process WP whereas there could be many other processes living 
on (R, 3, P, z). However, in the case where the filtration {3t}t>o is the one 
generated by the Wiener process itself, i.e. in the case when we have no other 
sources of randomness apart from wP, then we have a converse result of the 
I 
I 
Girsanov Theorem. 
Theorem 11.6 (The Converse of the Girsanov Theorem) Let WP be a 
d-dimensional standard (i.e. zero drift and unit variance independent wmpon- 
ents) P- Wiener process on (R, 3, P, 3) and assume that 
Assume that there exists a probability measure Q such that Q << P on FT. 
Then there exists an adapted process cp such that the likelihood process L has 
the dynamics 
Proof We know from Theorem C.12 that the likelihood process L is a 
P-martingale. Since the filtration is the one generated by WP we deduce from the 
Martingale Representation Theorem (11.2) that there exists a process g such that 
Now we simply define cp by 
1 
and the proof is basically finished. There remains a small problem, namely what 
happens when Lt = 0 but also this can be handled and we omit it. 
This converse result is very good news, since it implies that for the case of a 
Wiener filtration we have complete control of the class of absolutely continuous 
i 
measure transformations. 
I 
I 
11.5 Girsanov Transformations and Stochastic Differentials 
I 
1 
We will now discuss the effect that a Girsanov transformation has on the dynam- 
ics of a more general It6 process. Suppose therefore that, under the original 

MAXIMUM LIKELIHOOD ESTIMATION 
measure P, we have a process X with P-dynamics 
where w P  
is a (possible multidimensional) standard P-Wiener process, and 
where p and c are adapted and suitably integrable. Suppose furthermore that 
i we perform a Girsanov transformation with kernel process cp and transform from 
P to a new measure Q. The problem is to find out what the Q-dynamics of X 
look like. 
This problem is easily solved, since from the Girsanov Theorem we know that 
E we can write 
dw; = cpt dt + dw,&, 
where WQ is Q-Wiener. We now simply plug this expression into the X-dynamics 
above, collect the dt-terms and obtain 
dXt = {pt + ctcpt) dt + ctdw,& dt. 
'\ The moral of this is as follows: 
, 
The diffusion term is unchanged. 
The drift term is changed from p to p + acp. 
11.6 Maximum Likelihood Estimation 
In this section we give a brief introduction to maximum likelihood (ML) estim- 
ation for It6 processes. It is a bit outside the main scope of the book, but since 
ML theory is such an important topic and we already have developed most of 
the necessary machinery, we include it. 
We need the concept of a statistical model. 
Definition 11.7 A dynamic statistical model over a finite time interval [0, T] 
consists of the following objects: 
A measurable space (fl,3). 
A $ow of infornation on the space, formalized by a filtration T = {3t}t20. 
An indexed family of probability measures {Pa; a E A), defined on the 
space (R,F), where A is some index set and where all measures are 
assumed to be absolutely continuous on FT w.r.t. some base measure Pa,. 
In most concrete applications (see examples below) the parameter a will be 
a real number or a finite dimensional vector, i.e. A will be the real line or some 
finite dimensional Euclidian space. The filtration will typically be generated by 
some observation process X . 
The interpretation of all this is that the probability distribution is governed 
by some measure Pa, but we do not know which. We do have, however, access 
to a flow of information over time, and this is formalized by the filtration above, 

166 
THE MATHEMATICS OF THE MARTINGALE APPROACH 
so at time t we have the information contained in Ft. Our problem is to try to 
estimate a given this flow of observations, or more precisely: for every t we want 
an estimate at of a, based upon the information contained in 3t, 
i.e. based on the 
observations over the time interval [O,t]. The last requirement is formalized by 
requiring that the estimation process should be adapted to E, i.e. that at E Ft. 
One of the most common techniques used in this context is that of finding, 
for each t, the ML estimate of a. Formally the procedure works as follows. 
Compute, for each a the corresponding Likelihood process L(a) defined by 
dPa 
Lt (a) = - 
, on 3 t .  
dPaa 
For each fixed t ,  find the value of a which maximizes the likelihood 
ratio Lt (a). 
The optimal a is denoted by Bt and is called the ML estimate of a based 
on the information gathered over [0, t]. 
As the simplest possible example let us consider the problem of estimating 
the constant but unknown drift of a scalar Wiener process. In elementary terms 
we could naively formulate the model by saying that we can observe a process X 
with dynamics given by 
dXt = a d t  + dWt, 
Xo = 0. 
Here W is assumed to be Wiener under some given measure P and the drift a is 
some unknown real number. Since this example is so simple, we do in fact have 
an obvious candidate (why?) for the estimator process, namely 
In a naive formulation like this, we have a single underlying Wiener process, 
W under a single given probability measure P, and we see that for different 
choices of a we have different X-processes. In order to apply the ML techniques 
we must reformulate our problem, so that we instead have a single X-process 
and a family of measures. This is done as follows. 
Fix a process X which is Wiener under some probability measure Po. In 
other words: under Po, the process X has the dynamics 
where W0 is Po-Wiener. 

EXERCISES 
We assume that the information flow is the one generated by observations 
of X, 
so we define the filtration by setting Ft = 3:. For every real number a, 
we then define a Girsanov transformation to a new measure Pa by defining 
the likelihood process L(a) through 
dLt (a) = a Lt (a) dXt , 
Lo(a) = 1. 
From Girsanov's Theorem it now follows immediately that we can write 
dWt = a dt + dW,", where W" is a Pa Wiener process. Thus X will have 
the Pa dynamics 
dXt =adt+dW," 
I We now have a statistical model along the general lines above, and we notice 
I I that, as opposed to the case in the naive formulation, we have a single process X, 
1 but the driving Wiener processes are different for different values of a. 
To obtain the ML estimation process for a, we need to compute the likelihood 
process explicitly, i.e. we have to solve (11.26)-(11.27). This is easily done and 
we have 
Lt (a) = e ".x*-;ff2.t 
We may of course maximize In [Lt (a)] instead of maximize Lt (a) so our problem 
is to maximize (over a) the expression 
This trivial quadratic optimization problem can be solved by setting the 
a derivative equal to zero, and we obtain the optimal a as 
Thus we see that in this example the ML estimator actually coincides with our 
naive guess above. The point of using the ML technique is of course that in a 
more complicated situation (see the exercises) we may have no naive candidate, 
whereas the ML technique in principle is always applicable. 
11.7 Exercises 
Exercise 11.1 Complete an argument in the proof of Theorem 11.1 by proving 
that if X and Y are random variables of the form 
T 
x = x o + J d  9sdWs7 
T 

168 
THE MATHEMATICS OF THE MARTINGALE APPROACH 
and if g and h have disjoint support on the time axis, i.e. if 
gtht=O, 
P-a.s. O S t I T  
then 
T 
= XOYO + 1 1X.h. + Kg.] dWs. 
t 
Hint: Define the processes Xt and Yt by Xt 
= xo + So g. dWs and correspond- 
ingly for Y and use the It6 formula. 
Exercise 11.2 Consider the following SDE: 
dXt = af (Xt) dt + a(&) dWt , 
xo = 20. 
Here f and a are known functions, whereas a is an unknown parameter. We 
assume that the SDE possesses a unique solution for every fixed choice of a. 
Construct a dynamical statistical model for this problem and compute the 
ML estimator process 6t for a, based upon observations of X. 
11.8 Notes 
The results in this chapter can be found in any textbook on stochastic analysis 
such as Karatzas and Shreve (1988), Bksendal (1995), and Steele (2001). 

BLACK-SCHOLES FROM A MARTINGALE 
POINT OF VIEW* 
In this chaper we will discuss the standard Black-Scholes model from the 
martingale point of view. We thus choose a probability space (R, F ,  P,E) car- 
: rying a P-Wiener proces W, where the filtration 
is the one generated by W, 
i.e. Ft = Fy . On this space we define the model by 
dSt = aSt dt +  US^ dWt, 
dBt = rBt dt. 
Note that for ease of notation the P-Wiener process is denoted by w rather 
than by wP. 
12.1 Absence of Arbitrage 
We now want to see whether the model is arbitrage free on a finite interval [0, TI, 
and for that purpose we use the First Fundamental Theorem (10.22) which says 
that we have absence of arbitrage if and only if there exists a martingale measure 
I 
Q for our model. We then use the Girsanov Theorem to look for a Girsanov kernel 
process h such that the induced measure Q is a martingale measure. Defining, 
i 
as usual, the likelihood process L by 
i 
./ 
and setting dQ = LT d P  on FT, we know from Girsanov's Theorem that 
I 
where W is Q-Wiener. (For ease of notation we write W instead of the earlier 
wQ.) Inserting the above expression into the stock price dynamics we obtain, 
after a collection of terms, the Q-dynamics of S as 
In order for Q to be a martingale measure, we know from (10.51) that the local 
rate of return under Q must equal the short rate. Thus we want to determine 
the process h such that 
a + aht = T. 
(12.3) 

170 
BLACK-SCHOLES FROM A MARTINGALE POINT OF VIEW 
This equation has the simple solution 
and we see that the Girsanov kernel process h is in fact deterministic and 
constant. 
Furthermore, h has an important economic interpretation: In the quotient 
a - r 
- 
c ' 
the numerator a - r, commonly known as the "risk premium" of the stock, 
denotes the excess rate return of the stock over the risk free rate of return 
on the market. In the denominator we have the volatility of the stock, so the 
quotient above has an interpretation as "risk premium per unit volatility" or 
"risk premium per unit risk". This important concept will be discussed in some 
detail later on, and it is known in the literature as "the market price of risk". 
It is commonly denoted by A, so we have the following result. 
Lemma 12.1 The Girsanov kernel h is given by 
h=- X 
where the market price of risk X is defined by 
a- r  
A=-. 
u 
We have thus proved the existence of a martingale measure and from the First 
Fundamental Theorem we then have the following basic result for the Black- 
Scholes model. 
Theorem 12.2 The Black-Scholes model above is arbitrage free. 
We note in passing that instead of the standard Black-Scholes model above 
we could have considered a much more general model of the form 
dSt = atSt dt + utSt dWt, 
dBt = rtBt dt. 
where a, a, and r are allowed to be arbitrary adapted (but suitably integrable) 
processes with ut # 0 P-a.s. and for all t. The analysis of this more complicated 
model would be completely parallel to the one carried out above, with the only 
difference that the Girsanov kernel h would now be a stochastic process given 
by the formula 

-- 
PRICING 
171 
As long as this h satisfies the Novikov condition, the market would still be 
Remark 12.1.1 The formal reason for the condition ut # 0 is that otherwise 
the quotient in (12.6) is undefined. Being a bit more precise, and going back to 
the fundamental equation 
at + htut = rt, 
we see that we can in fact solve this equation (and thus guarantee absence of 
arbitrage) as long as the condition 
n t = Q  =$ at=rt. 
is valid. The economic interpretation of this condition is that if at = 0, then the 
stock price is locally riskless with dynamics dSt = Stat dt, so in order to avoid 
arbitrage with the money account B we must have at = rt. 
Consider the standard Black-Scholes model and a fixed T-claim X. F'rom 
Proposition 10.25 we immediately have the usual "risk-neutral" pricing formula 
II(t; X) = e-r(T-t) E~ [XI 
Ft] , 
(12.7) 
where the Q-dynamics of S are given as usual by 
dSt = rSr dt + uSt dWt. 
For a general claim we can not say so much more, but for the case of a simple 
claim of the form 
x = @(ST), 
we can of course, write down the Kolmogorov backward equation for the 
expectation and express the price as 
q t ;  X) 
= F(t, St), 
where the pricing function F solves the Black-Scholes equation. 
aF 
aF 1 
a2F 
- 
+ rs- 
+ -u2s2- 
- TF = 0, 
as 
2 
as2 . .; 
(12.8) 
F(T, s) = @(s). 
The moral of all this is that the fundamental object is the risk neutral 
valuation formula (12.7), which is valid for all possible claims, whereas the 
Black-Scholes PDE is only valid for the case of simple claims. 

172 
BLACK-SCHOLES FROM A MARTINGALE POINT O F  VIEW 
12.3 Completeness 
We now go on to investigate the completeness of the Black-Scholes model, and 
to this end we will use the Second Fundamental Theorem (10.24) which says 
that the market is complete if and only if the martingale measure is unique. We 
have seen in the previous section that there exists a martingale measure and the 
remaining question is whether this is the only martingale measure. 
In the present setting, where the filtration is the one generated by W we know 
from Theorem 11.6 that every absoluteIy continuous measure transformation is 
obtained from a Girsanov transformation, and since the basic equation (12.3) 
has a unique solution, we see that the martingale measure is in fact unique. The 
same argument is valid for the more general model above, and we have thus 
proved the following result. 
Theorem 12.3 The Black-Scholes model (12.1)-(12.2) zs complete. This also 
holds for the more general model (12.4)-(12.5). 
J+om an abstract point of view, the theorem above settles the completeness 
question, but since it is based on the second fundamental theorem, which in 
turn relies on rather abstract martingale theory, the argument is perhaps not 
overly instructive. We will therefore provide a more self contained completeness 
proof, which more clearly shows the use and central importance of the Martingale 
Representation Theorem 11.2. 
We will carry out the argument for the standard Black-Scholes model (12.1)- 
(12.2), but the argument goes through with very small changes also for the 
more general model above. We will use the technique in Lemma 10.15 and in 
terms of the notation of that lemma we identify the numeraire So with the 
money account B, and Sl with the stock price S. We then define the normalized 
processes Zo and Z1 
by 
Let Q be the (unique) martingale measure derived above, and consider an 
arbitrarv T-claim X with 
(For the standard Black-Scholes model we may of course take the factor l/B(T) 
out of the expectation.) We then define the Q-martingale M by 
and it now follows from Lemma 10.15 that the model is complete if we can find 
a process hl (t) such that 
dM(t) = hl (t) dZl (t). 
(12.10) 

COMPLETENESS 
173 
In order to prove the existence of such a process hl we use the Martingale 
I 
Representation Theorem 11.2 (under Q), which says that there exists a process 
g(t) such that 
dM(t) = g(t) dW(t), 
(12.11) 
where W is the Q-Wiener process defined earlier. With the purpose of connecting 
1 (12.11)-(12.10) we now use the Ito formula and the fact that Q is a martingale 
measure for the numeraire B to derive the Q-dynamics of Zl as 
dZl (t) = Zl (t)n dW(t). 
(12.12) 
We thus have 
1 
dW(t) = - 
21 (t). dZl (t), 
and plugging this into (12.11) we see that we in fact have (12.10) satisfied with hl 
defined by 
g(t) 
hl(t) = - 
.Zl (t) ' 
Again using Lemma 10.15, we have thus proved the following result. 
Theorem 12.4 In the Black-Scholes model (standard as well as extended), 
every T-claim X satisfying 
can be replicated. The replicating portfolio is given by 
where M is defined by (12.9) and g is defined by (12.11). 
This completeness result is much more general than the one derived in 
Chapter 8. The price that we have to pay for the increased generality is that 
we have to rely on the Martingale Representation Theorem which is an abstract 
existence result. Thus, for a general claim it is very hard (or virtually impossible) 
to compute the hedging portfolio in a reasonably explicit way. However, for the 
case of a simple claim of the form 
the situation is of course more manageable. In this case we have 

174 
BLACK-SCHOLES FROM A MARTINGALE POINT OF VIEW 
and from the Kolmogorov backward equation (or from a Feynman-KaE 
representation) we have M(t) = f (t, S(t)) where f solves the boundary value 
problem 
f (T, s) = e-rT@(s). 
Itd's formula now gives us 
so in terms of the notation above we have 
which gives us the replicating portfolio h as 
We have the interpretation f (t, S(t)) = VZ(t), i.e. f is the value of the nor- 
malized hedging portfolio, but it is natural to express everything in terms of 
the unnormalized value process V(t) rather than in terms of VZ. Therefore, 
we define F(t, s) by F(t, s) = ert f (t, s) which gives us the following result which 
we recognize from Chapter 8. 
Proposition 12.5 Consider the Black-Scholes model and a T-claim of the form 
X = @(S(T)). Then X can be replicated by the portfolio 
where F solves the Black-Scholes equation 
d F  
d F  1 
a2F 
- 
+ rs- + -u2s2- 
- rF = 0, 
[ at 
as 
2 
as2 
firthermore the value process for the replicating portfolio is given by 
V(t) = F(t, S(t)). 

9' 
f 
13 
MULTIDIMENSIONAL MODELS: CLASSICAL 
i r t,  
I LC) 
APPROACH 
13.1 Introduction 
In this chapter, we will generalize the Black-Scholes model to the case where, 
apart from the risk free asset, we have several underlying risky assets. In the 
present chapter we will carry out the analysis using the "classical" delta-hedging 
approach. In Chapter 14 we will then provide a more complete analysis using 
the martingale methods of Chapter 10. 
We assume that we have n a priori given risky assets ("stocks") with price 
processes Sl (t), . . . , S,(t). The entire asset price vector is denoted by S(t), and 
in matrix notation we will write it as a column vector 
so, = [ 1;:; ] . 
The main problems are those of pricing and hedging contingent claims of the form 
x = @(S(T)), 
where T as usual is a fixed exercise time. 
In the first sections we will analyze this problem in some detail using the 
"classical approach'' developed in Chapters 7 and 8. In Chapter 14 we will then 
use the martingale machinery developed in Chapter 10 to extend the analysis 
considerably. However, while from a formal point of view, all results obtained by 
the elementary approach in the present chapter are special cases of the results of 
Chapter 14, there is a substantial amount of economic intuition to be gathered 
from the classical approach, so the present chapter is not redundant even for the 
mathematically advanced reader. 
The first problem to be attacked is how to construct a "reasonable" math- 
ematical model for the dynamics of the asset price vector S, and in this context 
we have two demands. We of course want the model to be free of arbitrage pos- 
sibilities, and we also want the model to be such that we have a unique arbitrage 
free price process H(t; X) for any given claim X. 
From the meta-theorem 8.3.1 we know that we may generically expect absence 
of arbitrage if we have at least as many sources of randomness as we have under- 
lying assets, so it is natural to demand that the price vector S should be driven 
by at least n independent Wiener processes. 

176 
MULTIDIMENSIONAL MODELS: CLASSICAL APPROACH 
If, on the other hand, we want a unique price process for every claim, then 
we need a complete market model, and according to Meta-theorem 8.3.1 this will 
only occur if we have at least as many assets as we have sources of randomness. 
In order to obtain a nicely behaved model we are thus forced to model the stock 
price dynamics using exactly n independent Wiener processes, and we now go 
on to specify the formal model. 
Assumption 13.1.1 We assume the following: 
Under the objective probability measure P, the S-dynamics are given by 1 
dSi(t) = aj Si (t) dt + Si (t) ) 
~ i j  
dwj (t) , 
(13.1) I 
for i = 1,. . . , n. Here Wl, . . . , wn are independent P- Wiener processes. 
4 
The coefficients ai and u,i above are assumed to be known constants. 
The volitility matrix 
- 
--  
. -, 
> V , J X ,  
is nonsingular. 
We have the standard risk free asset with price process B, where 
dB(t) = rB(t) dt. 
(13.2) 
The assumption that the coefficients are constants is made for ease of expos- 
ition. Later on we will see that we may allow the coefficients to be functions of 
current time and current stock prices, i.e. ai = ai (t, S(t)), uij = oij (t, S(t)). 
In the seauel we will let ~ ( t )  
denote the column vector 
and it will be convenient to define the row vector ui as the ith row of the volatility 
matrix a, i.e. 
uj = [Uil,. . . ,Ujn]. 
With this notation we may write the stock price dynamics more compactly as 
dSj(t) = aiSi (t) dt + Si(t)ui dW(t). 
(13.3) 
It is in fact possible to write the S-dynamics even more compactly. For any 
n-vector x = (xl, . . . , x,) we let D [XI denote the diagonal matrix 

PRICING 
and we let a denote the column vector 
1 Using this notation we can write the S-dynamics as 
dS(t) = D[S(t)] a d t  + D[S(t)] udW(t). 
(13.6) 
13.2 Pricing 
We take the market model above as given and we consider a fixed T-claim of 
the form 
@(S(T)). 
, The problem is to find the arbitrage free price process II(t; X) for X, and we will 
' do this by using a slight variation of the technique for the one-dimensional case. 
As before we start by assuming that there actually is a market price process for 
the claim, and that the price process is of the form 
for some deterministic function 
Our problem is to find out what F must look like, in order not to intro- 
duce any arbitrage possibilities, if we are allowed to trade in the derivative 
as well as in the underlying assets. More precisely, we want the market 
[Sl(t), . . . , Sn(t), n(t; X)] to be free of arbitrage, and the basic scheme is as 
follows: 
Take the model for the underlying assets, the contract function @, and the 
pricing function F as given. 
Form a self-financing portfolio, based on SI, . . . , Sn, B and F. Since we 
have n + 2 assets, and the portfolio weights must add to unity, this will 
give us n + 1 degrees of freedom in our choice of weights. 
Choose the portfolio weights such that the driving Wiener processes are 
cancelled in the portfolio, thus leaving us with portfolio dynamics of 
, 
the form 
dV(t) = V(t)k(t) dt. 

178 
MULTIDIMENSIONAL MODELS: CLASSICAL APPROACH 
Since we have n driving Wiener processes this will "use up" n degrees of 
freedom. 
Use the remaining degree of freedom in order to force the value dynamics 
to be of the form 
dV(t) = (r + P) V(t) dt, 
where ,8 is some fixed nonzero real number. In the equation above we think 
of ,8 as being a positive real number, so we are in effect trying to "beat the 
risk free asset" B by constructing a synthetic risk free asset with higher 
rate of return than the money account. It turns out that this is technically 
possible if and only if a certain matrix is nonsingular. 
Since we assume that the market is free of arbitrage possibilities, it is 
impossible to beat the risk free asset in the way described above. Therefore, 
the matrix mentioned above has to be singular. 
The singularity condition of the matrix leads to a PDE for the pricing 
function F ,  and the solution of this PDE is thus the unique arbitrage free 
pricing function for the claim X. 
To put these ideas into action we start by computing the price dynamics of 
the derivative. The multidimensional It6 formula gives us (see Remark 4.7.1), 
after some reshuffling, 
d F =  ~ - a ~ d t + F . u ~ d ~ ,  
(13.7) 
where 
Here the arguments t and S(t) have been suppressed, and we have used the 
notation 
Note that Ft and Fi are scalar functions, whereas Fa, is an n x n matrix-valued 
function. 

PRICING 
179 
We now form a portfolio based on S1,. . . , Sn, B and F. For 5'1,. . . , Sn and F 
we use the notation u1, . . . , un and UF for the corresponding portfolio weights, 
which gives us the weight UB for the money account as 
The dynamics of, the value process for the corresponding self-financing 
portfolio are given by' 
and substituting the expression for UB above, as well as inserting the dynamics 
of the processes involved, gives us 
We now try to choose the weights so that, first of all, the value process is 
locally risk free, i.e. it has no driving Wiener process. This means that we want 
to solve the equation 
II 
Supposing for the moment that this can be done, we now have value dynamics 
of the form 
r n 
1 
and now we try to beat the market by choosing the weights such that we obtain 
a rate of return on the portfolio equaling r + P. Mathematically this means that 
we want to solve the equation 
In order to see some structure, we now write these equations in matrix form as 
a1-r ... a n- r a ~ - r  
[ 
u; 
... 
(13.10) 
4 4 

180 
MULTIDIMENSIONAL MODELS: CLASSICAL APPROACH 
(note that at is a column vector) where we have used the notation 
Let us now take a closer look at the coefficient matrix in eqn (13.10). Denoting 
this matrix by H, we see that it is an (n + 1) x (n + 1) matrix, and we have two 
possibilities to consider, namely whether H is invertible or not. 
If H is invertible, then the system (13.10) has a unique solution for every 
choice of p. In economic terms this means that we are able to form a self-financing 
portfolio with the dynamics 
dV(t) = (r + P)V(t) dt, 
which in turn means that we have constructed a "synthetic bank" with r + /3 as 
its rate of interest. This will of course lead to arbitrage opportunities. We just 
solve the system for, say, p = 0.10, then we borrow a (large) amount of money 
from the bank and invest it in the portfolio. By this arrangement our net outlays 
at t = 0 are zero, our debt to the bank will increase at the rate r, whereas the 
value of our portfolio will increase at a rate which is 10% higher. 
Since we assume absence of arbitrage we thus see that H must be singular, 
and in order to see the implications of this we choose, for readability reasons, to 
study its transpose H*, given by 
(recall that a, is a row vector). We can write this somewhat more compactly by 
defining the n-dimensional column vector 1, as 
With this notation we have 
Since H* is singular this means that the columns are linearly dependent, and 
since the matrix a was assumed to be nonsingular we draw the conclusion that 

PRICING 
181 
the first column of H* can be written as a linear combination of the other 
columns. Thus there exist real numbers XI, . . . , An such that 
where U F ~  denotes the jth component of the row vector OF. 
There is an economic interpretation of the multipliers A1,. . . , An as secalled 
"market prices of risk" (cf. standard CAPM theory), and later on we will discuss 
this in some detail. For the moment the main logical point is that eqn (13.14) 
is the equation which will determine the derivative pricing function F. In order 
to use this equation we need, however, to get hold of the A-vector, and as we 
shall see, this vector is determined by the system (13.13). 
Writing (13.13) in vector form we see that the vector 
is the solution of the n x n linear system 
and since a by assumption is nonsingular we see that X is in fact uniquely 
determined as 
X = a" [a - rl,]. 
(13.15) 
We now want to substitute this expression for X into (13.14), but first we 
rewrite (13.14) in vector form as 
and from the definition of UF in (13.9) we see that we may write UF more 
compactly as 
1 
CF = - [SIFl,. . . , SnFn] 
U. 
(13.17) 
F 
Inserting (13.15) and (13.17) into (13.16) and using uo-' 
3 I, we obtain the 
relation 
1 
CYF - T = - . [SlFl, . . . , SnFn] [Q - rl,], 
(13.18) 
F 

MULTIDIMENSIONAL MODELS: CLASSICAL APPROACH 
and finally we insert the expression for a~ from (13.8) into (13.18) to obtain, 
after some calculations, 
Note that this equation is a stochastic equation. For ease of reading we 
have suppressed most of the arguments, but if we backtrack we will see that, 
for example, the term rSiFi in the equation above is just shorthand for the 
exmession 
Thus eqn (13.19) must hold, at each t, with probability 1 for every possible value 
of the price vector S(t). Now, in our model for the price process it can be shown 
that the support (the set of possible values) for the vector S(t) is the entire set 
R"+ and thus eqn (13.19) must also hold for each deterministic t and s. By a 
standard argument we must also have F(T, S(T)) = @(S(T)), so we have proved 
our main pricing result. 
Theorem 13.1 Consider the contract X = %(S(T)). In order to avoid arbitrage 
possibilities, the pricing function F(t, s) must solve the boundary value problem 
Remark 13.2.1 To be more explicit we recall that we can write the quadratic 
term above as 
where 
Cij = [aa*]. 
.. 
23 
Remark 13.2.2 As in the onedimensional case we notice that the drift 
vector a, of the price process, does not appear in the pricing equation. Again we 
see that the only part of the underlying price process which influences the price of 
a financial derivative is the diffusion matrix a. The reason for this phenomenon 
is the same as in the scalar case and we refer the reader to our earlier discussion 
on the subject. A deeper understanding involves the Girsanov Theorem. See next 
chapter. 

RISK NEUTRAL VALUATION 
183 
Remark 13.2.3 In the derivation of the result above we have assumed that the 
drift vector a and the volatility matrix a in the price dynamics eqn (13.1) are 
constant. Going through the arguments it is, however, easily seen that we may 
allow the coefficients to be functions of current time and current stock price, 
i.e. they may be of the form 
(-Y = a(t, S(t)), 
a = a(t, S(t)). 
If we assume that the volatility matrix a(t, s) is invertible for each (t, s), then 
Theorem 13.1 will still hold, the only difference being that the term 
in the pricing equation is replaced by the term 
13.3 Risk Neutral Valuation 
As in the scalar case there is a natural economic interpretation of Theorem 13.1 
in terms of risk neutral valuation. From the Feynman-KaE representation 
theorem 5.8 we may immediately obtain a probabilistic formula for the solution 
to the pricing equation. 
Theorem 13.2 The pricing function F(t, s) of Theorem 13.1 has the following 
representation. 
F(t, s) = e-r(T-t)~Q 
t,s [3(S(T))1. 
Here the expectation is to be taken with respect to the martingale measure Q, 
defined by the fact that the Q-dynamics of the price process S are given by 
Adhering to the notational convention 7.4.1 the expression E$ [I indicates, as 
wual, that the expectation shall be taken under Q, given the initial condition 
S(t) = s. By the same convention, W is a Q- Wiener process. 
Again we see that the arbitrage free price of a derivative is given as the dis- 
counted expected value of the future cash flow, and again the main moral is that 
the expected value is not to be taken with respect to the objective probability 
measure P. Instead we must use the martingale measure Q. This martingale 
measure, or risk adjusted measure, is characterized by the following equivalent 
facts. The proof is left as an exercise to the reader. 

184 
MULTIDIMENSIONAL MODELS: CLASSICAL APPROACH 
Proposition 13.3 The martingale measure Q is characterized by any of the 
following equivalent conditions: 
1. Under Q every price process II (t), be it underlying or derivative, has the 
risk neutral valuation property 
II (t) = e-r(T-t)~zb [II (T)]. 
2. Under Q every price process JI (t), be it underlying or derivative, has the 
short rate of interest as its local mte of return, i.e. the Q-dynamics are of 
the form 
dII(t) = rII(t) dt + II(t) an (t) dW, 
where the volatility vector an is the same under Q as under P. 
3. Under Q every price process JI(t), be it underlying or derivative, has the 
property that the normalized price process 
is a martingale, i.e. it has a vanishing drift coeficient. 
As before we may summarize the moral as follows: 
When we compute arbitrage free prices of derivative assets, we can carry 
out the computations as if we live in a risk neutral world. 
This does not mean that we de facto live, or think that we live, in a risk 
neutral world. 
The formulas above hold regardless of the investor's preferences, and atti- 
tude towards risk, as long as he/she prefers more deterministic money 
to less. 
13.4 Reducing the State Space 
From Theorem 13.1 we see that in order to compute the price of a financial 
derivative based on n underlying assets, we have to solve a PDE with n state 
variables, and for a general case this has to be done by numerical methods. 
Sometimes it is, however, possible to reduce the dimension of the state space, and 
this can lead to a drastic simplification of the computational work, and in some 
cases even to analytical formulas. We will now present a theory which will allow 
us to obtain analytical pricing formulas for some nontrivial multidimensional 
claims which quite often occur in practice. The theory presented here is based on 
an analysis of the pricing PDE, but there also exists a corresponding probabilistic 
theory. See Chapter 24. 
Let us assume that we have the model 
n 
dSi(t)=o&(t)dt+~,(t)xo,d~j(t), i = l ,  ..., n. 
(13.21) 
j=1 

REDUCING THE STATE SPACE 
185 
j We consider a T-claim of the form X = @ (S(T)), and the crucial assumptions 
i are the following. 
Assumption 13.4.1 
For the rest of the section we assume that the contract function @ is 
homogeneous of degree 1, i.e. that 
@(t . s) = t . @(s), 
for allt > 0 and for all s E Rn. 
The volatility matrix o is constant. 
For a homogeneous @ we see that, by choosing t = s;', we have the relation 
@(sl,. . . , sn) = sn@ -, . . . , ", 
1). 
(: 
sn 
This naturally gives us the idea that perhaps also the corresponding pricing 
function F has the same homogeneity property, so we try the ansatz 
( :: 
sn-1 
F(t, sl, . . . ,an) = snG t, -, . . . , -) 
(13.22) 
an 
where G is some function 
G :  R+ x R~-' + R. 
First of all, if there is a solution to the pricing PDE of the form (13.22), then it 
has to satisfy the boundary condition 
F(T,s)=+(s), Vs, 
and translated into G this gives the boundary condition 
G(T,z)=\k(z), Vz, 
(13.23) 
where the function \k : Rn-l + R is defined by 
\k(zl,. . . , zn-1) = @(zl,. . . , zn-1, 1). 
(13.24) 
t 
The main problem is now to see whether there is a function G such that the 
ansatz (13.22) satisfies the pricing PDE. We therefore compute the various partial 
derivatives of F in terms of G, and substitute the result into the PDE. After some 

186 
MULTIDIMENSIONAL MODELS: CLASSICAL APPROACH 
tedious calculations we have the following relations, where for brevity z denotes 
the vector z = (sl/sn, . . . , 
Is,). Subscripts denotes partial derivatives. 
Ft(t, s) = snGt(t, z), 
Fi(t,s)=Gi(t,z), i=1, ..., n- 1, 
As in Remark 13.2.1 we write the pricing PDE as 
Substituting the expressions above for the partial derivatives of F into 
eqn (13.25) may look fairly forbidding, but in fact there will be many 
cancellations, and we end up with the following PDE for G. 
where 
Oij = ci j + Cnn + Gin + cnj. 
We have thus proved the following result. 
Proposition 13.4 Assume that the contract function 
is homogeneous of 
degree 1, and that the volatility matrix a is constant. Then the pricing function 
F is given by 
where G(t, 21,. . . , zn-l) solves the boundary value problem 

REDUCING THE STATE SPACE 
Here the matrix D is defined in (13.27), where C is given by Remark 13.2.1. 
The function Q is defined in (13.24). 
The point of this result is that, instead of having to solve a PDE with n 
state variables (and one time variable), we have reduced the problem to that of 
solving a PDE with only n - 1 state variables. 
Remark 13.4.1 The crucial assumption in Proposition 13.4 is of course the 
homogeneity of the contract function, but one may wonder where we used 
the assumption of a constant volatility matrix. The point is that, with a state 
dependent u, the PDE (13.26) is no longer a PDE in only the n - 1 state vari- 
ables zl, . . . ,z,-1, because the matrix D now depends on the entire price vector 
31,. . . , S,. 
It is interesting to note that the PDE satisfied by G is of parabolic type. 
By inspection we see that it can in fact be interpreted as the pricing PDE, in 
a world with zero interest rate, for a claim of the form Y = Q(Z(T)), where the 
, n - 1 underlying price processes satisfy an SDE of the form 
I 
where the drift vector p is as usual of no importance, the process w is an 
(n - 1)-dimensional standard P-Wiener process, and the covariance matrix 
: satisfies 
55* = D. 
Example 13.5 We illustrate the technique of state space reduction by a simple 
example of some practical importance. We consider a model with two underlying 
price processes Sl and S2, satisfying (under P) the following system of SDEs: 
As usual WI and W2 are independent, so in this model the price processes are 
also independent, but this is just for notational simplicity. 
The claim to be studied is an exchange option, which gives the holder the 
right, but not the obligation, to exchange one S2 share for one S1 share at time T. 
Formally this means that the claim is defined by X = max[Sl (T) - S2(T), 01, 
and we see that we have indeed a contract function which is homogeneous of 
degree 1. A straightforward application of Theorem 13.1 would give us the PDE 
Ft + rsiFi + rszF2 + ~ s ~ o f ~ l 1  
+ 4 s ; ~ : ~ ~ ~  
- rF = 0, 
F(T, sl, s2) = max [sl - s2, 01. 
I Using Proposition 13.4 we can instead write 

188 
MULTIDIMENSIONAL MODELS: CLASSICAL APPROACH 
I 
where G(t, z) satisfies 
1 
Gt(t, z )  + iz2Gzz (t, z) (o: + 0:) = 0, 
G(T, x) = max [z - 1,0]. 
We see that this is the pricing equation, in a world with short rate r = 0, for 
a European call option with strike price K = 1 written on a single stock with 
volatility d-2". 
Thus G can be obtained directly from the Black-Scholes 
formula, and after some minor calculations we get 
I 
where z = 51/52. N is as usual the cumulative distribution function for the I 
-. - 
N [O,1] distribution and 
I 
d2(t, z )  = dl (t, z) - \/(o: + oi)(T - t). 
13.5 Hedging 
1 
When we introduced the model 
1 
for the price vector process, one reason for the assumption of an invertible volat- 
ility matrix was that we wanted a complete market, and the goal of this section 
is to show that our model is in fact complete. From Chapter 8 we recall the 
following definition. 
I 
Definition 13.6 We say that a T-claim X can be replicated, alternatively 
that it is reachable or hedgeable, if there exists a self financing portfolio h 
such that 
vh(T) = X, 
P-a.s. 
(13.30) 
In this case we say that h is a hedge against X, alternatively a replicating 
portfolio for X. If every contingent claim is reachable we say that the market 
is complete. 
Since we are not using the full probabilistic machinery in this chapter, we 
will not be able to show that we can hedge every contingent T-claim X. As in 
the scalar case, we will "only" be able to prove completeness for simple claims, 
i.e. we will prove that every claim of the form 
can be replicated. For the full story see next chapter. 
1 

HEDGING 
189 
Let us thus fix a date of delivery T, and a claim X = (S(T)). We denote 
portfolio weights by uO,ul,. . . ,un, where ui is the weight on asset i for i = 
1,. . . , n, whereas u0 is the weight on the risk free asset. From Lemma 6.5 it is 
hlear that if we can find a process V, and weight processes uO, ul,. . . , un such that 
1 then uO, ul, . . . , un is a replicating portfolio for X, and V is the corresponding 
value process. For future use we note that eqns (13.32)-(13.33) can be written as 
The structure of the proof is that we will make an educated guess about 
the nature of the value process V, so we will make an ansatz. Given this 
ansatz we then compute the stochastic differential dV, and at last, compar- 
ing the expression thus obtained to (13.34), we identify the portfolio weights by 
inspection. 
We now go on to produce a natural candidate for the role as value process, 
and to this end we recall from Section 8.1 that, for a hedgeable claim, we should 
have the relation U(t; X) = V(t). 
Thus the obvious candidate as the value process for the replicating portfolio 
(if it exists at all) is the price process H(t; X) for the claim. On the other hand 
we have already computed the price process as 
I 
where F solves the pricing PDE of Theorem 13.1. 
Let us thus define F as the solution to the pricing PDE, and then define the 
/ 
process V by V(t) = F (t, S(t)). Our task is to show that V in fact is the value 
process of a replicating portfolio, i.e. to show that the relation (13.31) is satisfied, 
and that the dynamics for V can be written in the form (13.34). Equation (13.31) 
is obviously (why?) satisfied, and using the identity (by definition) F = V, we 
obtain from (13.7) 

190 
MULTIDIMENSIONAL MODELS: CLASSICAL APPROACH 
So, from (13.8)-(13.9) 
Comparing the diffusion part of (13.35) to that of (13.34) we see that the natural 
candidates as ul, . . . , un are given by 
I 
si Fi 
ua (t) = - 
F ' i=1, ..., n. 
Substituting these expressions into (13.35) gives us 
1 
and, using the fact that F satisfies the pricing PDE, we obtain 
1 
Again using the definition (13.36), this reduces to 
I 
which is exactly eqn (13.34). We have thus proved the second part of the following 
theorem. 
Theorem 13.7 Assume that the volatility matrix a is invertible. Then the 
following hold: 
The market is complete, i.e. every claim can be replicated. 
For a T-claim X of the form X = ( S ( T ) ) ,  the weights in the replicating 
portfolio are given by 
u0 (t) = 1 - E u' (t) , 
i=l 
where F by definition is the solution of the pricing PDE in Theorem 13.1. 
We have only proved that every simple contingent claim can be replicated, so 
we have not proved the first item above in full generality. It can in fact be proved 
that every (sufficiently integrable) claim can be replicated, but this requires the 
, 
use of more advanced probabilistic tools (the martingale representation theorem 
for Wiener filtrations) and is treated in the next section. 

