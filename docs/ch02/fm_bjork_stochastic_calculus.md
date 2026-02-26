# Stochastic Integrals & Differential Equations

!!! info "Source"
    **Arbitrage Theory in Continuous Time** by Tomas Björk, Oxford University Press, 2nd ed., 2004.
    These notes are used for educational purposes.

## Stochastic Integrals

COMPLETENESS 
31 
we must have n(1; X) = X. Plugging this into the equation above we have the 
following result. 
Proposition 3.7 Consider a given claim X .  In onler to avoid arbitrage, X 
must then be priced acconling to the formula 
whew Q is a martingale measure for the underlying market. 
We see that this formula extends the corresponding risk neutral pricing 
formula (3.4) for the underlying assets. 
The pricing formula (3.5) looks very nice, but there is a problem: if there exist 
several different martingale measures then we will have several possible arbit- 
rage free prices for a given claim X. This has to do with the (possible lack of) 
completeness of the market. 
3.4 Completeness 
In this section, we will discuss how it is possible to generate payment streams at 
t = 1 by forming portfolios in the underlying. 
Assumption 3.4.1 We assume that the market S1,. . . , SN is arbitrage free and 
that there exists a risk free asset. 
Definition 3.8 Consider a contingent claim X .  If there exists a portfolio h, 
based on the underlying assets, such that 
V! 
= X, 
with probability 1. 
(3.6) 
then we say that X is replicated, or hedged by h. Such a portfolio h is called 
a replicating, or hedging portfolio. If every contingent claim can be replicated, we 
say that the market is complete. 
It is easy to characterize completeness in our market, and we have the 
following result. 
Proposition 3.9 The market is complete if and only i f  the rows of the matrix 
D span R ~ ,  
i.e. if and only if D has rank M .  
Proof For any portfolio h, we view the random variable V: 
as a row vector 
[v,~(wI), 
. . . , v ~ ( w ~ ) ]  
and with this notation we have 
V: = hD. 

32 
A MORE GENERAL ONE PERIOD MODEL 
The market is thm complete if and only if, for every random variable X, (viewed 
as a row vector in RM) the equation 
has a solution. But hD is exactly a linear combination of the rows of D with the 
components of h as coefficients. 
The concept of a replicating portfolio gives rise to an alternative way of 
pricing contingent claims. Assume namely that the claim X can be replicated by 
the portfolio h. Then there is an obvious candidate as the price (at time t = 0) 
for X, namely the market price, at t = 0, of the replicating portfolio. We thus 
propose the natural pricing f o d a  
Here there is a possibility that may get us into trouble. There may very well 
exist two different hedging portfolios f and g, and it could in principle happen 
that Vt # Vt. It is, however, easy to see that this would lead to an arbitrage 
possibility (how?) so we may disregard that possibility. 
The pricing formula (3.8) can also be written in another way, so let us assume 
that h replicates X. Then, by definition, we have 
and from (3.8) we obtain 
However, on our arbitrage free market we also have the pricing formula (3.4) 
1 
s o  = i ; 4 r ? i ~ Q [ ~ x ] .  
(3.11) 
,,i 
Combining this with (3.9)-(3.10) we obtain the pricing formula 
which is exactly the formula given by, Proposition 3.7. Thus the two pricing 
approaches coincide on the set of hedgable claims. 
In Proposition 3.9 we obtained one characterization of complete markets. 
There is another characterization which connects completeness to martingale 
measures. This result, which we give below in our simple setting, is known as 
"the second fundamental theorem of mathematical finance". 

COMPLETENESS 
Proposition 3.10 (Second Fundamental Theorem) Assume that the model 
is arbitrage free. Then the market is complete i f  and only if the martingale 
1 
measure is unique. 
Proof From Proposition 3.9 we know that the market is complete if and only 
if the rows of D span the whole of RM, i.e. if and only if 
Im[D*] = R", 
I 
where we view the transpose matrix D* as a mapping from RN to RM. On the 
other hand, from Proposition 3.3 and the assumption of absence of arbitrage we 
know that there exists a solution (even a nonnegative one) to the equation 
so = Dz. 
This solution is unique if and only if the kernel (null spack) of'D is! trivial, i:e. 
if and only if 
Ker [Dl = 0. 
We now recall the following well known duality result: 
v 
(I~[D*J)?, Ker[D] . 
Thus Ker[D] = 0 if and only if Im[D*] = RM, i.e. the market is complete if and 
only if the martingale measure is unique. ' 
-$ 
. 
; 
We may now summarize our findings. 
Proposition 3.11 The following hold: 
' a  The market is arbitmge free if and only i f  there exists a martingale 
1 
measure Q. 
1 .a7 The market is complete if and only i f  the martingale measure is unique. 
' 
For any claim X ,  the only prices which are consistent with absence of 
arbitmge are of the form 
I 
ti 
1
,
 
.- 
9 
L ,  7 
I rjv, 
' 1 
II(0; X) = - 
E~ [XI , 
c 
?. l + R >  *, 
(3.13) 
where Q is a martingale measure for the underlying market. 
1 a If the market is incomplete, then different choices of martingale measures 
I 
Q in the formula (3.13) will generically give rise to different prices. 
., .. 
a If X is replicable then, even in an incomplete market, the price in (3.13) 
I 
, 
will not depend upon the particular choice of martingale measure Q. If X 
4, . 
is replicable, then 
1 
v," -.---.-EQ[Aq, 
PC 
l + R  
. 
for d l  martingale measures Q and for all replicating portfolios h. 
r 
- 
p
p
 

34 
A MORE GENERALSONE PEFlIOD MODEL 
3.5 Stochastic Discount Factors 
In the previous sections we have seen that we'can price finmcial derivatives by 
using martingale measures and the formula 
In some applications of the theory (in particular in asset pricing) it is common 
to write this expected value directly under the objective probability measure P 
instead of under Q. 
Recalling the notation pi = P(w,) and qi = Q(wi), i = 1,. . . , M, and the 
assumption that pi > 0 for i =  1,. . . , M, we may define a new random 
variable on R. 
Definition 3.12 The random variable L on R is defined by 
Thus L gives us the likelihood mtio between the measures P and Q, and 
in more general situations it is known as the Radon-Nikodym derivative of Q 
w.r.t. P. 
Definition 3.13 Assume absence of arbitrage, and fi a martingale measure Q. 
With notations as above, the stochastic discount factor (or "state price 
deflator") is the mndom variable A on 0 defined by 
We can now express our arbitrage free pricing formulas in a slightly 
different way. 
Proposition 3.14 The arbitrage free price of any claim X is given by the 
formula 
n(o;x) = E ~ [ A . x ] ,  
(3.15) 
whem A is a stochastic discount factor, 
h 
Proof Exercise for the reader: 
" 1,' 
We see that there is a on+twone correspondence between stochastic discount 
factors and martingale measures, and it is largely a matter of taste if you want 
to work with A or with Q. The advantage of working with A is that you form- 
ally stay with the objective measure P. The advantage with working under Q is 
that the decomposition of A in (3.14) gives us important structural information, 

EXERCISES 
35 
t
i
 
I \ and in more complicated situations there exists a deep theory (see "Girsanov 
I F 
transformations" later in the text) which allows us to have complete control over 
z ,  
1 
" the class of martingale measures. 
'1 
FIom an economic point of view, the stochastic discount factor is precisely an 
r 
Arrow-Debreu state price system, which gives the price A(w,) to the primitive 
i claim Xi which pays 1 if wi occurs, and zero otherwise. 
3.6 Exercises 
Exercise 3.1 Prove that Q in Proposition 3.7 is a martingale measure also for 
the price process n(t; X), i.e. show that 
i 
where B is the risk free asset. 
Exercise 3.2 Prove the last item in Proposition 3.11. 
I 
( 
Exercise 3.3 Prove Proposition 3.14. 

STOCHASTIC INTEGRALS 
4.1 Introduction 
The purpose of this book is to study asset pricing on financial markets in 
continuous time. We thus want to model asset prices as continuous time 
stochastic processes, and the most complete and elegant theory is obtained if 
we use diffusion processes and stochastic differential equations as our 
building blocks. What, then, is a diffusion? 
Loosely speaking we say that a stochastic process X is a diffusion if its 
local dynamics can be approximated by a stochastic difference equation of the 
following type: 
X ( t  + At) - X ( t )  = p (t, X ( t ) )  At + u (t, X ( t ) )  Z(t). 
(4.1) 
Here Z ( t )  is a normally distributed disturbance term which is independent of 
everything which has happened up to time t, while p and cr are given determ- 
inistic functions. The intuitive content of (4.1) is that, over the time interval 
[t, t + At], the X-process is driven by two separate terms. 
A locally deterministic velocity p (t, X(t)). 
A Gaussian disturbance term, amplified by the factor cr (t, X(t)). 
The function p is called the (local) drift term of the process, whereas a is 
called the diffusion term. In order to model the Gaussian disturbance terms we 
need the concept of a Wiener process. 
Definition 4.1 A stochastic process W is called a Wiener process if the 
following conditions hold: 
1. W ( 0 )  = 0. 
2. The process W has independent increments, i.e. if r < s I t < u then 
W ( u )  - W(t) and W ( s )  - W ( r )  are independent stochastic variables. 
3. For s < t the stochastic variable W(t)- W ( s )  has the Gaussian distribution 
N [0, -1. 
4. W has continuous trajectories. 
Remark 4.1.1 Note that we use a somewhat old fashioned notation, where 
N [p, cr] denotes a Gaussian distribution with expected value ,u and standard 
deviation a. 
In Fig. 4.1 a computer simulated Wiener trajectory is shown. 

- ---- 
1 
INTRODUCTION 
t 
0 
0.2 
0.4 
0.6 
0.8 
1 
1.2 
1.4' 
1.6 
1.8 
2 
F IG. 4.1. A Wiener trajectory 
We may now use a Wiener process in order to write (4.1) as 
X(t + At) - X(t) = p (t, X(t)) At + a (t, X(t)) AW(t), 
(4.2) 
where AW(t) is defined by 
AW(t) = W(t + At) - W(t). 
i 
Let us now try to make (4.2) a bit more precise. It is then tempting to divide 
the equation by At and let At tend to zero. Formally, we would obtain 
~ ( t )  
= P (t, X(t)) + a (t, X(t)) 
(4.3) 
X(O) = a, 
(4.4) 
dW 
u(t) = - 
dt 
is the formal time derivative of the Wiener process W .  
If u were an ordinary (and well defined) process we would now in principle 
be able to solve (4.3) as a standard ordinary differential equation (ODE) for 

38 
STOCHASTIC INTEGRALS 
each v-trajectory. However, it can be shown that with probability 1 a Wiener 
trajectory is nowhere differentiable (cf. Fig. 4.1), so the process v cannot even 
be defined. Thus this is a dead end. 
Another possibility of making eqn (4.2) more precise is to let At tend to 
zero without first dividing the equation by At. Formally we will then obtain the 
exwession 
dX(t) = p (t, X(t)) dt + u (t, X(t)) dW(t), 
X(0) = a, 
and it is now natural to interpret (4.5) as a shorthand version of the following 
integral equation 
t 
t 
~ ( t )  
= a + 1 p (s, X(s)) ds + 1 0 (9, X(s)) dW(s). 
(4.6) 
In eqn (4.6) we may interpret the ds-integral as an ordinary Riemann integral. 
The natural interpretation of the dW-integral is to view it as a Riemann-Stieltjes 
integral for each W-trajectory, but unfortunately this is not possible since one 
can show that the W-trajectories are of locally unbounded variation. Thus the 
stochastic dW-integral cannot be defined in a naive way. 
As long as we insist on giving a precise meaning to eqn (4.2) for each 
W-trajectory separately, we thus seem to be in a hopeless situation. If, 
however, we relax our demand that the dW-integral in eqn (4.6) should be 
defined trajectorywise we can still proceed. It is in fact possible to give a global 
(L2-)definition of integrals of the form 
for a large class of processes g. This new integral concept-the so called It6 
integral-will then give rise to a very powerful type of stochastic differential 
calculus-the It6 calculus. Our program for the future thus consists of the 
following steps: 
1. Define integrals of the type 
2. Develop the corresponding differential calculus. 
3. Analyze stochastic differential equations of the type (4.5) using the 
stochastic calculus above. 
4.2 Information 
Let X be any given stochastic process. In the sequel it will be important to 
define "the information generated by X" as time goes by. To do this in a rigorous 

INFORMATION 
39 
! fashion is outside the main scope of this book, but for most practical purposes 
the following heuristic definitions will do nicely. See the appendices for a precise 
treatment. 
Definition 4.2 The symbol 3: denotes "the information generated by X on the 
interval [0, t] ", or alternatively "what has happened to X over the interval [0, t] ". 
E 
If, based upon observations of the trajectory { X ( s ) ;  0 5 s 5 t ) ,  it is possible to 
: decide whether a given event A has occurred or not, then we write this as 
or say that "A is 3: -measurable". 
If the value of a given stochastic variable Z can be completely determined 
given observations of the trajectory { X ( s ) ;  0 5 s 5 t ) ,  then we also write 
z E 3:. 
a 
If Y is a stochastic process such that we have 
Y (t) E 3: 
for all t 2 0 then we say that Y is adapted to the filtration {F:),,~. - 
The above definition is only intended to have an intuitive content, since 
a precise definition would take us into the realm of abstract measure theory. 
Nevertheless it is usually extremely simple to use the definition, and we now 
give some fairly typical examples. 
1. If we define the event A by A = { X ( s )  < 3.14, for all s 5 9) then we have 
t 
A E 3:. 
e t2. For the event A = {X(10) > 8 )  we have A E 35. Note, however, that we 
do not have A E 3$, since it is impossible to decide if A has occurred or 
B ik ' 
not on the basis of having observed the X-trajectory only over the interval 
"\ 
[0,9]. 
: 
3. For the stochastic variable 2, defined by 
I 
5 
z = 1 X ( s ) d s ,  
A 
I 
we have Z E F:. 
6 
4. If W is a Wiener process and if the process X is defined by 
X (t) = sup W (s) , 
sst 
then X is adapted to the W-filtration. 

STOCHASTIC INTEGRALS 
5. With W as above, but with X defined as 
X(t) = sup W (s), 
s<t+l 
X is not adapted (to the W-filtration). 
4.3 Stochastic Integrals 
We now turn to the construction of the stochastic integral. For that purpose we 
consider as given a Wiener process W, and another stochastic process g. In order 
to guarantee the existence of the stochastic integral we have to impose some kind 
of integrability conditions on g, and the class J2 turns out to be natural. 
Definition 4.3 
(i) We say that the process g belongs to the class E2 [a, b] if the following 
conditions are satisfied. 
J: E [ ~ ~  
(s)] ds < m. 
The process g is adapted to the Fy -filtration. 
(22) 
We say that the process g belongs to the class E2 if g E E2 [O, t] for 
all t > 0. 
Our object is now to define the stochastic integral J: g(s) dW(s), for a process 
g E E2 [a, b], and this is carried out in two steps. 
Suppose to begin with that the process g E E2 [a, b] is simple, i.e. that there 
exist deterministic points in time a = to < tl < 
< tn = b, such that g is 
constant on each subinterval. In other words we assume that g(s) = g(tk) for 
s E Itk, tk+l). Then we define the stochastic integral by the obvious formula 
Remark 4.3.1 Note that in the definition of the stochastic integral we take 
so called forward increments of the Wiener process. More specifically, in the 
generic term g(tk) [W(tk+l) - W(tk)] of the sum the process g is evaluated at 
the left end tk of the interval [tk,tk+l] over which we take the W-increment. 
This is essential to the following theory both from a mathematical and (as we 
shall see later) from an economical point of view. 
For a general process g E E2 [a, b] which is not simple we may schematically 
proceed as follows: 
1. Approximate g with a sequence of simple processes gn such that 

STOCHASTIC INTEGRALS 
41 
2. For each n the integral J: gn(s) dW(s) is a well-defined stochastic variable 
Z,, and it is possible to prove that there exists a stochastic variable Z 
such that Zn + 2 (in L ~ )  
as n + oo. 
3. We now define the stochastic integral by 
= lim 
,,-m 
Ja gn(s) 
The most important properties of the stochastic integral are given by the 
following proposition. In particular we will use the property (4.12) over and 
over again. 
Proposition 4.4 Let g be a process satisfying the conditions 
g is adapted to the Fy-filtmtion. 
(4.11) 
I Then the following relations hold: 
ds. 
I 
Proof A full proof is outside the scope of this book, but the general strategy 
is to start by proving all the assertions above in the case when g is simple. This 
is fairly easily done, and then it "only" remains to go to the limit in the sense 
of (4.9). We illustrate the technique by proving (4.12) in the case of a simple g. 
We obtain 
1 
rn-1 
1 
k=O 
Since g is adapted, the value g(tk) only depends on the behavior of the Wiener 
process on the interval [0, tk]. Now, by definition W has independent increments, 
il so [W(tk+l) - W(tk)] (which is a forward increment) is independent of g(tk). 

STOCHASTIC INTEGRALS 
Remark 4.3.2 It is possible to define the stochastic integral for a process g 
satisfying only the weak condition 
For such a general g we have no guarantee that the properties (4.12) and (4.13) 
hold. Property (4.14) is, however, still valid. 
I 
4.4 Martingales 
The theory of stochastic integration is intimately connected to the theory of mar- 
tingales, and the modern theory of financial derivatives is in fact based mainly on 
martingale theory. Martingale theory, however, requires some basic knowledge 
of abstract measure theory, and a formal treatment is thus outside the scope of 
the more elementary parts of this book. 
Because of its great importance for the field, however, it would be unreason- 
able to pass over this important topic entirely, and the object of this section is 
to (informally) introduce the martingale concept. The more advanced reader is 
referred to the appendices for details. 
Let us therefore consider a given filtration ("flow of information") {Ft}t20, 
where, as before, the reader can think of Ft as the information generated by all 
observed events up to time t. For any stochastic variable Y we now let the symbol 
denote the "expected value of Y ,  given the information available at time t". 
A precise definition of this object requires measure theory, so we have to be con- 
tent with this informal description. Note that for a fixed t, the object E [Yl Ft] 
is a stochastic variable. If, for example, the filtration is generated by a single 
observed process X ,  then the information available at time t will of course depend 
upon the behavior of X over the interval [0, t], so the conditional expectation 
E [Yl Ft] will in this case be a function of all past X-values {X(s): s 5 t). We 
will need the following two rules of calculation. 
Proposition 4.5 
lf Y and Z are stochastic variables, and Z is Ft-measurable, then 
E [Z. 
Y(Ft] = Z. 
E [Y(&]. 

I 
MARTINGALES 
43 
If Y is a stochastic variable, and if s < t, then 
1 The first of these results should be obvious: in the expected value E [ Z  . Y I Ft] we 
condition upon all information available time t. If now Z E Ft, this means that, 
given the information Ft, we know exactly the value of Z, so in the conditional 
expectation Z can be treated as a constant, and thus it can be taken outside the 
expectation. The second result is called the "law of iterated expectations", and 
it is basically a version of the law of total probability. 
We can now define the martingale concept. 
Definition 4.6 A stochastic process X is called an (Ft)-martingale i f  the 
following conditions hold: 
X is adapted to the filtration {3t)t20. 
For all t 
E[lX(t)Il < 00. 
For all s and t with s 5 t the following relation holds: 
A process satisfying, for all s and t with s 5 t, the inequality 
is called a supermartingale, and a process satisfying 
is called a submartingale. 
The first condition says that we can observe the value X ( t )  at time t, and the 
second condition is just a technical condition. The really important condition is 
the third one, which says that the expectation of a future value of X, given the 
information available today, equals today's observed value of X. Another way of 
putting this is to say that a martingale has no systematic drift. 
It is possible to prove the following extension of Proposition 4.4. 
Proposition 4.7 For any process g E E2 [s, t] the following hold: 
i 
p- 
1 
As a corollary we obtain the following important fact. 

44 
STOCHASTIC INTEGRALS 
Corollary 4.8 For any process g E L2, 
the process X ,  defined by 
is an (3tw)-martingale. In other words, modulo an integrability condition, every 
stochastic integral is a martingale. 
Proof Fix s and t with s < t. We have 
The integral in the first expectation is, by Proposition 4.4, measurable w.r.t. 
37, so by Proposition 4.5 we have 
I 
[I' 
g(r) d W ( r )  3r = 
g(7) d W ( r ) ,  
I I I' 
Ftorn Proposition 4.4 we also see that E J~~ 
g(r) d W ( r )  1 3 ~ ]  
= 0, so we obtain I 
We have in fact the following stronger (and very useful) result. 
Lemma 4.9 Within the framework above, and assuming enough integrability, 
a stochastic process X (having a stochastic differential) is a martingale i f  and 
only if the stochastic differential has the form 
i. e. X has no dt-term. 
Proof We have already seen that if dX has no dt-term then X is a martingale. 
The reverse implication is much harder to prove, and the reader is referred to 
the literature cited in the notes below. 
O
1
 

STOCHASTIC CALCULUS AND THE ITO FORMULA 
45 
4.5 Stochastic Calculus and the It6 Formula 
Let X be a stochastic process and suppose that there exists a real number xo 
and two adapted processes p and u such that the following relation holds for 
all t 2 0. 
where a is some given real number. As usual W is a Wiener process. To use a less 
cumbersome notation we will often write eqn (4.16) in the following form: 
In this case we say that X has a stochastic differential given by (4.17) with 
an initial condition given by (4.18). Note that the formal string dX(t) = 
p(t) dt + u(t) dW(t) has no independent meaning. It is simply a shorthand ver- 
sion of the expression (4.16) above. From an intuitive point of view the stochastic 
differential is, however, a much more natural object to consider than the cor- 
responding integral expression. This is because the stochastic differential gives 
us the "infinitesimal dynamics" of the X-process, and as we have seen in Sec- 
tion 4.1, both the drift term p(s) and the diffusion term u(s) have a natural 
intuitive interpretation. 
k 
Let us assume that X indeed has the stochastic differential above. Loosely 
speaking we thus see that the infinitesimal increment dX(t) consists of a loc- 
ally deterministic drift term p(t) dt plus an additive Gaussian noise term 
u(t) dW(t). Assume furthermore that we are given a C1'2-function 
and let us now define a new process Z by 
I 
P 1 
Z(t) = f (t, X(t)). 
I We may now ask what the local dynamics of the Z-process look like, and at first it 
seems fairly obvious that, except for the case when f is linear in x, Z will not have 
a stochastic differential. Consider, for example, a discrete time example where 
X satisfies a stochastic difference equation with additive Gaussian noise in each 
step, and suppose that f (t, x) = ex. Then it is clear that Z will not be driven by 
;- additive Gaussian noise-the noise will in fact be multiplicative and log-normal. - 
i 
It is therefore extremely surprising that for continuous time models the stochastic 
differential structure with a drift term plus additive Gaussian noise will in fact be 
preserved even under nonlinear transformations. Thus the process Z will have 
t 
a stochastic differential, and the form of dZ is given explicitly by the famous 

STOCHASTIC INTEGRALS 
It6 formula below. Before turning to the It6 formula we have to take a closer 
look at some rather fine properties of the trajectories of the Wiener process. 
As we saw earlier the Wiener process is defined by a number of very simple 
probabilistic properties' It is therefore natural to assume that a typical Wiener 
trajectory is a fairly simple object, but this is not at all the case. On the 
contrary-one can show that, with probability 1, the Wiener trajectory will 
be a continuous function of time (see the definition above) which is nondifferen- 
tiable at every point. Thus a typical trajectory is a continuous curve consisting 
entirely of corners and it is of course quite impossible to draw a figure of such 
an object (it is in fact fairly hard to prove that such a curve actually exists). 
This lack of smoothness gives rise to an odd property of the quadratic variation 
of the Wiener trajectory, and since the entire theory to follow depends on this 
particular property we now take some time to study the Wiener increments a bit 
closer. 
Let us therefore fix two points in time, s and t with s < t, and let us use the 
handy notation 
Using well-known properties of the normal distribution it is fairly easy to obtain 
the following results, which we will use frequently 
E [AW] = 0, 
E[(Aw)~] = At, 
Var[AW] = At, 
(4.21) 
We see that the squared Wiener increment (Aw(t)12 has an expected value 
which equals the time increment At. The really important fact, however, is 
that, according to (4.22), the variance of [ A W ( ~ ) ] ~  
is negligible compared to its 
expected value. In other words, as At tends to zero [Aw(t)12 will of course also 
tend to zero, but the variance will approach zero much faster than the expected 
value. Thus [Aw(t)12 will look more and more "deterministic" and we are led 
to believe that in the limit we have the purely formal equality 
[dw(t)12 = dt. 
(4.23) 
The reasoning above is purely heuristic. It requires a lot of hard work to turn the 
I 
relation (4.23) into a mathematically precise statement, and it is of course even 
harder to prove it. We will not attempt either a precise formulation or a precise 
proof. In order to give the reader a flavor of the full theory we will, however, 
give another argument for the relation (4.23). 

STOCHASTIC CALCULUS AND THE ITO FORMULA 
47 
I 
Let us therefore fix a point in time t and subdivide the interval [0, t] into n 
equally large subintervals of the form [k;, (k + I):], 
where k = 0,1,. . . , n - 1. 
Given this subdivision, we now define the quadratic variation of the Wiener 
4 
and our goal is to see what happens to Sn as the subdivision becomes finer, i.e. 
as n -+ m. We immediately see that 
n 
= C [ii - (i-  l)?] =t. 
n 
i=l 
1 Using the fact that W has independent increments we also have 
Thus we see that E [Sn] = t whereas Var[S,] -t 0 as n -+ 
oo. In other words, as 
n -+ m we see that S, tends to the deterministic limit t. This motivates us 
write 
equivalently, 
[dw12 = dt. 
(4.26) 
Note again that all the reasoning above has been purely motivational. In this 
text we will have to be content with accepting (4.26) as a dogmatic truth, and 
now we can give the main result in the theory of stochastic calculus-the It6 
Fj formula. 
Theorem 4.10 (Itb's formula) Assume that the process X has a stochastic 
diferential given by 
1 
dX (t) = p(4) dt + u(t) dW (t) , 
(4.27) 
where p and a are adapted processes, and let f be a C192-function. Define the 
process Z by Z(t) = f (t, X ( t ) ) .  Then Z has a stochastic differential given by 

48 
STOCHASTIC INTEGMLS 
Remark 4.5.1 In the statement of the theorem above we have, for readability 
reasons, suppressed a lot of variables. The term p df ldx, for example, is 
shorthand notation for 
a f 
'(t) az (t' X(t)) 
and correspondingly fqr the other terms. 
Proof A full formal proof is outside the scope of this text, so we only give 
a heuristic proof (see Remark 4.5.2). If we make a Taylor expansion including 
second order terms we obtain 
af 
af 
1d2f 
2 
1d2f 
df=-dt+-dX+--(dX) 
+--(dt)2+a2fdtdX. 
(4.29) 1 
at 
ax 
2 ax2 
2 at2 
atax 
By definition we have 
dX(t) = p(t) dt + o(t) dW (t) , 
so, at least formally, we obtain 
(dx12 = p2 (dt12 + 2pu (dt)(dW) + u2 (dw12. 
The term containing (dt)2 above is negligible compared to the dt-term in (4.27), 
and it can also be shown that the (dt)(dW)-term is negligible compared to the 
dt-term. Furthermore we have ( d ~ ) ~  
= dt from (4.23), and plugging in all this 
into the Taylor expansion (4.29) gives us the result. 
It may be hard to remember the It6 formula, so for practical purposes it is 
often easier to copy our "proof" above and make a second order Taylor expansion. 
Proposition 4.11 (ItB's formula) With assumptions as in Theorem 4.10, d f 
is given by 
df 
d f  
1 a2f 
df = -dt+ 
- d ~ +  -- 
(dx12 
at 
dx 
2 dx2 
(4.30) 
whew. we use the following formal multiplication table. 
(dt12 = 0, 
dt . dW = 0, 
(dw12 = dt. 
Remark 4.5.2 As we have pointed out, the "proof" of the It6 formula above 
does not at all constitute a formal proof. We end this section by giving an outline 
of the full proof. What we have to prove is that, for all t, the following relation 
holds with probability one: 
(4.31) 
Bibliothek 
Bielefeld 


## Stochastic Differential Equations

STOCHASTIC CALCULUS AND THE ITO FORMULA 
49 
We therefore divide the interval [0, t] as 0 = to < tl < . < t, = t into n equal 
j 
subintervals. Then we have 
n-1 
f (t, X(t)) - f (0, X(0)) = C f (tk+l, ~(t*+1)) - f (tk, X(tk)) . 
(4.32) 
k=O 
Using Taylor's formula we obtain, with subscripts denoting partial derivatives 
i 
and obvious notation, 
f (tk+l, X(tk+l)) - f (tk, X(tk)) 
= ft (tk, X(tk)) At + fx (tkr X(tk)) Axk 
(4.33) 
) 
+ ifxx (tk, X(tk)) AX^)^ + Qk, 
where Qk is the remainder term. Furthermore, we have 
AXk = X(tk+l) - X(tk) = l:+' 
'(s) ds f rk+' 
U(S) dW(8) 
t 
t k  
(4.34) 
= p(tk)At + U(tk)AWk + S k ,  
where Sk is a remainder term. From this we obtain 
I 
( ~ x k ) ~  
= p2(tk) ( ~ t ) ~  
+ 2p(tk)~(tk)AtAWk + u2(tk) ( A W ~ ) ~  
+ p k ,  
(4.35) 
6 
where Pk is a remainder term. If we now substitute (4.33)-(4.35) into (4.32) we 
1 obtain, in shorthand notation, 
6 
f (t, X(t)) - f (0, X(0)) = I1 + 12 4- 13 + 314 + $Ki + K2 + R, 
L. 
I 
where 
f 
I1 = Ck ft(tk)At, 
12 = C k  fx(tk)~(tk)At, 
P 
13 = Ck fx(tk)u(tk)AWk7 
k k 
14 = x
k
 fxx(tk)u2(tk) (awk12 , 
Kl = Ck f ~ ~ ( t r ) p ~ ( t r )  , KZ = Ck fr~(tr)~(tr;)~(tle)AtAWk, 
: R = c ~ I Q ~ + ~ ~ + P ~ ) .  
I 
Letting n + oo we have, more or less by definition, 
I 
I 
I1 + 
f' (s,X(s)) d., 
I 2  - 
f x  (s, X(s)) P(S) ds, 
~3 Is 
fx (s, ~ ( s ) )  
~ ( s )  
d ~ ( s ) .  
Very much as when we proved earlier that C ( A W ~ ) ~  
-r t, it is possible to 
show that 

50 
STOCHASTIC INTEGRALS 
and it is fairly easy to show that K1 and Kz converge to zero. The really hard 
part is to show that the term R, which is a large sum of individual remainder 
terms, also converges to zero. This can, however, also be done and the proof 
is finished. 
4.6 Examples 
In order to illustrate the use of the It6 formula we now give some examples. All 
these examples are quite simple, and the results could have been obtained as 
well by using standard techniques from elementary probability theory. The full 
force of the It6 calculus will be seen in the following chapters. 
The first two examples illustrate a useful technique for computing expec- 
ted values in situations involving Wiener processes. Since arbitrage pricing to 
a large extent consists of precisely the computation of certain expected values 
this technique will be used repeatedly in the sequel. 
Suppose that we want to compute the expected value E [Y] where Y is some 
stochastic variable. Schematically we will then proceed as follows: 
1. Try to write Y as Y = Z(to) where to is some point in time and Z is 
a stochastic process having an It6 differential. 
2. Use the It6 formula to compute dZ as, for example, 
3. Write this expression in integrated form as 
4. Take expected values. Using Proposition 4.4 we see that the dW-integral 
will vanish. For the ds-integral we may move the expectation oper- 
ator inbide the integral sign (an integral is "just" a sum), and we 
thus have 
rt 
Now two cases can occur: 
(a) We may, by skill or pure luck, be able to calculate the expected 
value E[p(s)] explicitly. Then we only have to compute an ordin- 
ary Riemann integral to obtain E [Z(t)], and thus to read off E [Y] = 
E [Z(to)l 
(b) If we cannot compute E [p(s)] directly we have a harder problem, but 
in some cases we may convert our problem to that of solving an ODE. 

EXAMPLES 
51 
Example 4.12 Compute E [w4(t)]. 
Solution: Define Z by Z(t) = W4(t). Then we have Z(t) = f(t,X(t)) where 
X = W and f is given by f (t, x) = x4. Thus the stochastic differential of X 
is trivial, namely dX = dW, which, in the notation of the It6 formula (4.28), 
means that p = 0 and a = 1. Furthermore we have af/& = 0, af/ax = 4x3, 
and d2 f /ax2 = 12x2. Thus the It6 formula gives us 
dZ(t) = 6w2(t) dt + 4w3(t) dW(t), 
Z(0) = 0. 
I 
Written in integral form this reads 
t 
t 
Z(t) = O +  6 l  w2(s)ds + 4 1  w3(s)dW(s). 
I 
Now we take the expected values of both members of this expression. Then, by 
Proposition 4.4, the stochastic integral will vanish. Furthermore we may move 
the expectation operator inside the ds-integral, so we obtain 
I 
E (Z(t)] = 6 & E [w2(s)] ds. 
Now we recall that E [w2(s)] = s, so in the end we have our desired result 
t 
E [w4(t)] = E [ ~ ( t ) ]  
= 6 1  sds = 3t2. 
0 
Example 4.13 Compute E [eaw(t)]. 
a1 
r- 
Solution: Define Z by Z(t) = eaW(t). The It6 formula gives us 
I" 
dZ(t) = ia2eaW(t) dt + aeaw(t) dW(t), 
so we see that Z satisfies the stochastic differential equation 
dZ(t) = ;a22(t) dt + aZ(t) dW(t), 
E 
Z(0) ='I. 
In integral form this reads 
k 
l
t
 
t 
~ ( t )  
= 1 + -a2 Jo ~ ( s ) ( d s )  + a Jo ~ ( s )  
d ~ ( s ) .  
2 

52 
STOCHASTIC INTEGRALS 
Taking expected values will make the stochastic integral vanish. After moving 
the expectation within the integral sign in the ds-integral and defining m by 
m(t) = E [Z(t)] we obtain the equation 
1 
m(t) = 1 + -a2 l m(s) (ds). 
2 
This is an integral equation, but if we take the t-derivative we obtain the ODE 
Solving this standard equation gives us the answer 
E [effw(t)] = E [Z(t)] = m(t) = eff2'I2. 
It is natural to ask whether one can "compute" (in some sense) the value of 
a stochastic integral. This is a fairly vague question, but regardless of how it is 
interpreted, the answer is generally no. There are just a few examples where the 
stochastic integral can be computed in a fairly explicit way. Here is the most 
famous one. 
Example 4.14 Compute 
rt 
Solution: A natural guess is perhaps that 
W(s)dW(s) = W2(t)/2. Since 
It6 calculus does not coincide with ordinary calculus this guess cannot possibly 
be true, but nevertheless it seems natural to start by investigating the process 
Z(t) = W2(t). Using the It6 formula on the function f(t,x) = x2 and with 
X = W we get 
dZ(t) = dt + 2W(t) dW(t). 
In integrated form this reads 
so we get our answer 
We end with a useful lemma. 

THE MULTIDIMENSIONAL ITO FORMULA 
53 
Lemma 4.15 Let a(t) be a given deterministic function of time and define 
X(t) = & ~ ( s )  
dW(s). 
(4.36) 
Then X(t) has a normal distribution with zero mean, and variance given by 
t 
var[x(t)l= 
02(s) ds. 
0 
This is of course an expected result because the integral is "just" a linear 
combination of the normally distributed Wiener increments with deterministic 
coefficients. See the exercises for a hint of the proof. 
4.7 The Multidimensional It6 Formula 
Let us now consider a vector process X = (XI,. . . , Xn)*, where the component 
X, has a stochastic differential of the form 
d 
dXi (t) = p. (t) dt + 
oij (t) dW, (t) 
j-1 
and Wl, . . . , Wd are d independent Wiener processes. 
Defining the drift vector p by 
P =  [:I], 
Pn 
the d-dimensional vector Wiener process W by 
W =  ["', 
Wd 
and the n x d-dimensional diffusion matrix o by 
011 
012 . . - 
ffld 
.=[? 1 : :  ".I, 
ffnl ffn2 
0
.
 
ffnd 
we may write the X-dynamics as 
dX(t) = p(t) dt + u(t) dW(t). 

54 
STOCHASTIC INTEGRALS 
Let us furthermore define the process Z by 
where f : R+ x Rn 4 R is a C112 mapping. Then, using arguments as above, it 
can be shown that the stochastic differential d f is given by 
with the extended multiplication rule (see the exercises) 
(dWi) (dWj) = 0, 
for i # j. 
Written out in full (see the exercises) this gives us the following result. 
Theorem 4.16 (It6's formula) Let the n-dimensional process X have dynam- 
ics given by 
d X ( t )  = p(t) dt + n(t) dW(t), 
with notation as above. Then the following hold: 
The process f (t, X ( t ) )  has a stochastic diflerential given by 
Here the row vector ui is the ith row of the matrix a ,  i.e. 
gi = [ail,. . . g i d ] ,  
and the matrix C is defined by 
C = aa*, 
where * denotes transpose. 
Alternatively, the differential is given by the formula 
with the formal multiplication table 
(dt)2 = 0, 
dt . d W  = 0, 
(dwi12 = dt, 
i = 1 ,..., d, 
dWi .dWj = 0, i # j. 

CORRELATED WIENER PROCESSES 
55 
Remark 4.7.1 (ItB's formula) The It6 formula can also be written as 
af 
1 
d
f
{
+
p
i
+
t
r
*
H
l
 
z=1 
Xi 
where H denotes the Hessian matrix 
@ f 
H . . -  - 
a3 - axiaxj ' 
and tr denotes the trace of a matrix. The trace is defined, for any square 
matrix A, as the sum of the diagonal elements, i.e. 
t
r
~
 
= CA,. 
- 
i 
See the exercises for details. 
4.8 Correlated Wiener Processes 
Up to this point we have only considered independent Wiener processes, but 
sometimes it is convenient to'build models based upon Wiener processes which 
are correlated. In order to define such objects, let us therefore consider d 
independent standard (i.e. unit variance) Wiener processes Wl, . . . , Wd. Let 
furthermore a (deterministic and constant) matrix 
611 
612 . . . bid 
6 =  
6n1 bn2 . -. 6nd 
be given, and consider the n-dimensional processes W, defined by 
w = aw, 
w =  [". 
Wn 
d 
w,=C&wj, i = l ,  ..., n. 
j=1 

56 
STOCHASTIC INTEGRALS 
Let us now assume that the rows of 6 have unit length, i.e. 
=
l
 
i = 1 ,  ..., n, 
1
where the Euclidean norm is defined as usual by 
Then it is easy to see (how?) that each of the components Wl, . . . , W, separ- 
ately are standard (i.e. unit variance) Wiener processes. Let us now define the 
(instantaneous) correlation matrix p of W by 
We then obtain 
Definition 4.17 The process W ,  constructed as above, is called a vector of 
correlated Wiener processes, with correlation matrix p. 
Using this definition we have the following It6 formula for correlated Wiener 
processes. 
Proposition 4.18 (ItB's formula) Take a vector Wiener process W = 
(Wl, . . . , W,) with correlation matrix p as given, and assume that the vector pro- 
cess X = (XI,. . . , Xk)* has a stochastic differential. Then the following hold: 
For any C1t2 function f, the stochastic diferential of the process f (t, X ( t ) )  
is given by 

CORRELATED WIENER PROCESSES 
with the formal multiplication table 
(dt12 = 0, 
dt.dWi=O, 
i = l ,  ..., n, 
dWi. dWj = pijdt. 
I 
If, in particular, k = n and dX has the structure 
where pl, . . . , pn and u1,. . . , un are scalar processes, then the stochastic 
F 
diferential of the process f (t, X(t)) is given by 
2,3=1 
We end this section by showing how it is possible to translate between the 
two formalisms above. Suppose therefore that the n-dimensional process X has 
a stochastic differential of the form 
dX(t) = p(t) dt + u(t) dW (t), 
d 
= pi (t) dt + C oij (t) d Wi (t) 
j=1 
Thus the drift vector process p is given by 
and the diffusion matrix process u by 
W is assumed to be d-dimensional standard vector Wiener process (i.e. with 
indenendent com~onents) of the form 

58 
STOCHASTIC INTEGRALS 
The system (4.38) can also be written as 
1
dXi (t) = pi (t) dt + ui (t) dW (t), 
where, as usual, ui is the ith row of the matrix u. Let us now define n new scalar 
Wiener processes Wl, . . . , W,, by 
We can then write the X-dynamics as 
As is easily seen, each Wi 
is a standard scalar Wiener process, but Wl, . . . , ~d 
are of course correlated. The local correlation is easily calculated as 
Summing up we have the following result. 
Proposition 4.19 The system 
d 
dXi (t) = fi (t) dt + C gij (t) d Wi (t) , 
dt. 
where Wl, . . . , Wd are independent, may equivalently be written as 
where Wl, . . . , Wd have the local correlation matrix p. The connections 
between (4.41) and (4.42) are given by the following expressions: 

I 
EXERCISES 
4.9 Exercises 
Exercise 4.1 Compute the stochastic differential dZ when 
(b) Z(t) = 
g(s) dW(s), where g is an adapted stochastic process. 
, (d) Z(t) = eox(t), where X has the stochastic differential 
dX(t) = pdt + adW(t) 
(p and 0 are constants). 
(e) Z(t) = X2(t), where X has the stochastic differential 
dX(t) = aX(t) dt + aX(t) dW (t) . 
Exercise 4.2 Compute the stochastic differential for Z when Z(t) = l/X(t) 
and X has the stochastic differential 
dX (t) = cuX (t) dt + uX(t) d W (t) . 
By using the definition Z = X--l you can in fact express the right hand side of 
dZ entirely in terms of Z itself (rather than in terms of X). Thus Z satisfies 
a stochastic differential equation. Which one? 
Exercise 4.3 Let a(t) be a given deterministic function of time and define the 
X(t)= 
a(s)dW(s). 
I' 
(4.43) 
Use the technique described in Example 4.13 in order to show that the 
characteristic function of X(t) (for a fixed t) is given by 
E [ eiux(t) 1 = exp { - - 
U22 l g 2 ( 4 d s ) >  I 4  E ~1 
(4.44) 
thus showing that X(t) is normally distributed with zero mean and a variance 
t 
VW[X(~)] 
= J 02(s) ds. 
0 
Exercise 4.4 Suppose that X has the stochastic differential 
dX(t) = aX(t) dt + a(t) dW(t), 
where a is a real number whereas o(t) is any stochastic process. Use the technique 
in Example 4.13 in order to determine the function m(t) = E [X(t)] . 

60 
STOCHASTIC INTEGRALS 
Exercise 4.5 Suppose that the process X has a stochastic differential 
d X  (t) = p(t) dt + a(t) dW (t) , 
and that p(t) > 0 with probability one for all t. Show that this implies that X 
is a submartingale. 
Exercise 4.6 A function h(xl,. . . , x,) is said to be harmonic if it satisfies the 
condition 
d2h 
Ce =o. 
r=l 
It is subharmonic if it satisfies the condition 
" d2h 
C@ 20. 
a=1 
Let Wl, . . . , W, 
be independent standard Wiener processes, and define the 
process X by X(t) = h(Wl(t), . . . , Wn(t)). Show that X is a martingale (sub- 
martingale) if h is harmonic (subharmonic). 
Exercise 4.7 The. object of this exercise is to give an argument for the 
formal identity 
dWl . dW2 = 0, 
when Wl and W2 are independent Wiener processes. Let us therefore fix a time 
t, and divide the interval [0, t] into equidistant points 0 = to < tl < . . - < tn = t, 
where ti = 
t. We use the notation 
Awi(tk)=Wi(tk)-Wi(tk-l), 2=1,2. 
Now define Q, by 
n 
Qn = C ~ w l ( t k )  
. Aw2(tk). 
k=l 
Show that Qn -, 0 in L2, i.e. show that 
E(Qn1 = 0, 
Var[Qnl+ 0. 
Exercise 4.8 Let X and Y be given as the solutions to the following system of 
stochastic differential equations. 
dX=aXdt-YdW, 
X(0) =xo, 
dY =aYdt+XdW, 
Y(O)=yo. 

NOTES 
I Note that the initial values xo, yo are deterministic constants. 
(a) Prove that the process R defined by R(t) = X2(t)+Y2(t) is deterministic. 
" (b) Compute E [X(t)] . 
Exercise 4.9 For a n x n matrix-A, the trace of A is defined as 
(a) If B is n x d and C is d x n, then BC is n x n. Show that 
[ fi (b) With assumptions as above, show that 
!t & (c) Show that the It6 formula in Theorem 4.16 can be written as 
where H denotes the Hessian matrix 
1 
Exercise 4.10 Prove all claims in Section 4.8. 
4.10 Notes 
As a (far reaching) introduction to stochastic calculus and its applications, 
0ksendal (1995) and Steele (2001) can be recommended. Standard references 
on a more advanced level are Karatzas and Shreve (1988), and Revuz and Yor 
(1991). The theory of stochastic integration can be extended from the Wiener 
framework to allow for semimartingales as integrators, and a classic in this field 
is Meyer (1976). Standard references are Jacod and Shiryaev (1987), Elliott 
(1982), and Dellacherie and Meyer (1972). An alternative to the classic approach 
to semimartingale integration theory is presented in Protter (1990). 

P 
Exe 
- 
.3iW 
/ 
5 
DIFFERENTIAL EQUATIONS 
5.1 Stochastic Differential Equations 
Let M(n, d) denote the class of n x d matrices, and consider as given the following 
objects. 
A &dimensional (column-vector) Wiener process W. 
A (column-vector valued) function p : R+ x Rn + Rn. 
A function a : R+ x Rn + M(n, d). 
A real (column) vector xo E Rn. 
We now want to investigate whether there exists a stochastic process X which 
satisfies the SDE 
dXt = p (t, Xt) dt + a (t, Xt) dWt, 
xo = $0. 
i 
To be more precise we want to find a process X satisfying the integral equation 
xt = xo + lo 
p (s, XI) ds + 
u (s, X,) dW,, 
for all t 2 0. 
Jo 
(5.3) 
The standard method for proving the existence of a solution to the SDE above 
is to construct an iteration scheme of Cauchy-Picard type. The idea is to define 
a sequence of processes XO, X1, X2,. . . according to the recursive definition 
x:" 
= xo + 
p (s, X:) 
ds + 
u (s, X:) 
dW,. 
I 
Having done this one expects that the sequence {Xn)r=l will converge to some 
limiting process X, and that this X is a solution to the SDE. This construction 
can in fact be carried out, but as the proof requires some rather hard inequalities 
we only give the result. 
Proposition 5.1 Suppose that there exists a constant K such that the following 
conditions are satisfied for all x, y and t: 

GEOMETRIC BROWNIAN MOTION 
63 
k 
Then there exists a unique solution to the SDE (5.1)-(5.2). The solution has the 
following properties: 
1. X is FtW 
-adapted. 
1 
2. X has continuous trajectories. 
3. X is a Markov process. 
4. There exists a constant C such that 
f' 
1 
E [IlXtl12] 5 ceCt (1 + llxoIl2). 
(5.9) 
kg 
The fact that the solution X is 3y-adapted means that for each fixed t ,  
I 
the process value Xt is a functional of the Wiener trajectory on the interval 
(0, t] , and in this way an SDE induces a transformation of the space C[O, oo) 
into itself, where a Wiener trajectory W.(w) is mapped to the corresponding 
solution trajectory X.(w). Generically this transformation, which takes a Wiener 
trajectory into the corresponding X-trajectory, is enormously complicated and it 
Ph 
is extremely rare that one can "solve" an SDE in some LLexplicit" 
manner. There 
are, however, a few nontrivial interesting cases where it is possible to solve an 
t 
SDE, and the most important example for us is the equation below, describing 
'I 1 
1 the so-called geometric Brownian motion (GBM). 
2) 
5.2 Geometric Brownian Motion 
Pn 
Geometric Brownian motion will be one of our fundamental building blocks for 
i the modeling of asset prices, and it also turns up naturally in many other places. 
3) 
The equation is one of two natural generalizations of the simplest linear ODE 
and looks as follows: 
hre 
Geometric Brownian motion: 
ne 
dXt = aXt dt + o x t  dWt, 
(5.10) 
XO = 20. 
(5.11) 
Writing in a slightly sloppy form we can write the equation as 
xt = (a + owt) xt, 
where w is "white noise", i.e. the (formal) time derivative of the Wiener pro- 
cess. Thus we see that GBM can be viewed as a linear ODE, with a stochastic 
coefficient driven by white noise. See Fig. 5.1, for a computer simulation of GBM 
.2 and X(0) = 1. The smooth line is the graph of the expected 
t] = 1 .eat. For small values of u, the trajectory will (at least 
close to the expected value function, whereas a large value 
large random deviations. This can clearly be seen when we 
compare the simulated trajectory in Fig. 5.1 to the three simulated trajectories 
in Fig. 5.2 where we have u = 0.4. 

DIFFERENTIAL EQUATIONS 
I 
I 
I 
0 
0.2 
0.4 
0.6 
0.8 
1 
1.2 
1.4 
1.6 
1.8 
2 
FIG. 5.1. Geometric Brownian motion: a = 1, a = 0.2 
01 
I 
I 
0 
' 0.2 
0.4 
0.6 
0.8 
1 
1.2 
1.4 
1.6 
1.8 
2 
FIG. 5.2. Geometric Brownian motion: a = 1, a = 0.4 

GEOMETRTC BROWNIAN MOTION 
65 
E 
Inspired by the fact that the solution to the corresponding deterministic linear 
equation is an exponential function of time we are led to investigate the process 
2, defined by Zt = In Xt, where we assume that X is a solution and that X is 
strictly positive (see below). The It6 formula gives us 
1 
Thus we have the equation 
! This equation, however, is extremely simple: since the right-hand side does not 
I contain Z it can be integrated directly to 
which means that X is given by 
,- 
Strictly speaking there is a logical flaw in the reasoning above. In order for 
; Z to be well defined we have to assume that there actually exists a solution X 
to eqn (5.10) and we also have to assume that the solution is positive. As for the 
existence, this is covered by Proposition 5.1, but the positivity seems to present 
a bigger problem. We may actually avoid both these problems by regarding the 
calculations above as purely heuristic. Instead, we define the process X by the 
formula (5.12). Then it is an easy exercise to show that X thus defined actually 
satisfies the SDE (5.10)-(5.11). Thus we really have proved the first part of the 
following result, which will be used repeatedly in the sequel. The result about 
the expected value is an easy exercise, which is left to the reader. 
Proposition 5.2 The solution to the equation 
is given by 
X(t) = xo . exp {(a - +a2) t + uw(t)). 
(5.15) 
i The expected value is given by 
\ E [Xt] = xOePt. 
(5.16) 

I 
66 
DIFFERENTIAL EQUATIONS 
I 
5.3 The Linear SDE 
In this section, we will study the linear SDE, which in the scalar case has the 
form 
dXt = aXtdt + udWt, 
i 
(5.17) 
xo = so. 
This equation turns up in various physical applications, and we will also meet it 
below in connection with interest rate theory. 
In order to get some feeling for how to solve this equation we recall that the 
dxt 
-- 
dt - axt + ut, 
. 
where u is a deterministic function of time, has the solution 
1 
If we, for a moment, reason heuristically, then it is tempting to formally divide 
eqn (5.17) by dt. This would (formally) give us 
I 
and, by analogy with the ODE above. one is led to coniecture the formal solution 
Generally speaking, tricks like this will not work, since the solution of the 
ODE is based on ordinary calculus, whereas we have to use It6 calculus when 
dealing with SDEs. In this case, however, we have a linear structure, which 
means that the second order term in the It6 formula does not come into play. 
Thus the solution of the linear SDE is indeed given by the heuristically derived 
formula above. We formulate the result for a slightly more general situation, 
where we allow X to be vector-valued. 
Proposition 5.3 Consider the n-dimensional linear SDE - 
where A is an n x n matrix, b is an Rn-valued deterministic function (in column- 
vector form), a is a deterministic function taking values in M(n, d), and W a 
d-dimensional Wiener process. The solution of this eauation is aiven bu 

THE INFINITESIMAL OPERATOR 
67 
! Hew we have used the matrix exponential eAt, defined by 
Proof Defining the process X by (5.20) and using the It6 formula, it is easily 
seen that X satisfies the SDE (5.19). See the exercises for some details. 
In the exercises you will find results about the moments of Xt as well as 
details about the matrix exponential. 
5.4 The Infinitesimal Operator 
Consider, as in Section 5.1, the n-dimensional SDE 
I 
dXt = ,U (t, Xt) dt + u (t, Xt) dWt . 
(5.21) 
t Through the It6 formula, the process above is closely connected to a partial 
differential operator A, defined below. The next two sections are devoted to 
investigating the connections between, on the one hand, the analytical properties 
of the operator A, and on the other hand the probabilistic properties of the 
process X above. 
Definition 5.4 Given the SDE in (5.21), the partial diferential operator A, 
referred to as the infinitesimal operator of X, is defined, for any function 
h ( ~ )  
with h E c ~ ( R ~ ) ,  
by 
where as before 
C(t, x) = u(t, x)u*(t, 5). 
This operator is also known as the Dynkin operator, the It6 operator, 
or the Kolmogorov backward operator. We note that, in terms of the 
/ 
infinitesimal generator, the It6 formula takes the form 
i 
df(t,Xt) = {g + df) dt + [Vxf]udWt, 
where the gradient V, is defined for h E c'(R~) as 

68 
DIFFERENTIAL EQUATIONS 
5.5 Partial Differential Equations 
In this section, we will explore the intimate connection which exists between 
stochastic differential equations and certain parabolic partial differential equa- 
tions. Consider for example the following so-called Cauchy problem. 
We are given three scalar functions p(t, x), a(t, x) and @(x). Our task is to 
find a function F which satisfies the following boundary value problem on 
[0, T] 
x R: 
Now, instead of attacking this problem using purely analytical tools, we will pro- 
duce a so called stochastic representation formula, which gives the solution 
to (5.22)-(5.23) in terms of the solution to an SDE which is associated to (5.22)- 
(5.23) in a natural way. Thus we assume that there actually exists a solution F 
to (5.22)-(5.23). Let us now fix a point in time t and a point in space x. Having 
fixed these we define the stochastic process X on the time interval [t, T] as the 
solution to the SDE 
and the point is that the infinitesimal generator A for this process is given by 
which is exactly the operator appearing in the PDE above. Thus we may write 
the boundary value problem as 
Applying the It6 formula to the process F (s, X(s)) g' lves us 

