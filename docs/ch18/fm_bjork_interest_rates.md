# Interest Rates: Short Rate, Forward Rate & Market Models

!!! info "Source"
    **Arbitrage Theory in Continuous Time** by Tomas Björk, Oxford University Press, 2nd ed., 2004.
    These notes are used for educational purposes.

## Bonds and Interest Rates

STOCHASTIC OPTIMAL CONTROL 
Remark 19.3.2 By going through the arguments above, it is easily seen that 
we may allow the constraint set U to be time- and state-dependent. If we thus 
have control constraints of the form 
u(t,x) E U(t,x), W,x 
then the HJB equation still holds with the obvious modification of the 
supremum part. 
It is important to note that this theorem has the form of a necessary con- 
dition. It says that if V is the optimal value function, and if ii is the optimal 
control, then V satisfies the HJB equation, and Q(t,x) realizes the supremum 
in the equation. We also note that Assumption 19.3.1 is an ad hoc assumption. 
One would prefer to have conditions in terms of the initial data p, a, F, and 
which would guarantee that Assumption 19.3.1 is satisfied. This can in fact be 
done, but at a fairly high price in terms of technical complexity. The reader is 
referred to the specialist literature. 
A gratifying, and perhaps surprising, fact is that the HJB equation also acts 
as a sufficient condition for the optimal control problem. This result is known 
as the verification theorem for dynamic programming, and we will use it 
repeatedly below. Note that, as opposed to the necessary conditions above, the 
verification theorem is very easy to prove rigorously. 
Theorem 19.6 (Verification theorem) Suppose that we have two functions 
H(t,i) and g(t, x), such that 
a H is suficiently integrable (see Remark 19.3.4 below), and solves the HJB 
equation 
{ ~ ( t , x ) + ~ ~ ~ { F ( t , x , u ) + d u ~ ( t ~ x ) } = O ,  
v ( t , x ) ~ ( O , T ) x R ~  
H(T,x)=@(x), V X E  Rn. 
The function g is an admissible control law. 
a For each jixed (t, x), the supremum in the expression 
sup {F(t, x, u) + duH(t, 2)) 
UEU 
is attained by the choice u = g(t, x). 
Then the following hold: 
1. The optimal value function V to the control problem is given by 
V(t, x) = H(t, x). 
2. There exists an optimal control law u, and in fact u(t, x) = g(t, x). 

THE HAMILTON-JACOBI-BELLMAN EQUATION 
281 
Remark 19.3.3 Note that we have used the letter H (instead of V) in the HJB 
equation above. This is because the letter V by definition denotes the optimal 
value function. 
Proof Assume that H and g axe given as above. Now choose an arbitrary 
control law u E 24, and fix a point (t, x). We define the process X U  on the time 
interval [t, T] as the solution to the equation 
dX,U = pu (s, X,U) ds + uU (s, X,U) dW,, 
xt 
= x. 
Inserting the process X U into the function H and using the It6 formula we obtain 
1 Since H solves the HJB equation we see that 
! 
i for all u E U, 
and thus we have, for each s and P-a.s, the inequality 
g ( s ,  
at 
x:) 
+ (AUH) (a, x:) 
5 -FU(s, X:). 
From the boundary condition for the HJB equation we also have H(T, X;) 
= 
@(X!j?), so we obtain the inequality 
Taking expectations, and assuming enough integrability, we make the stochastic 
integral vanish, leaving us with the inequality 
Since the control law u was arbitrarily chosen this gives us 
H(t, x) 1 sup J(t, x, u) = V(t, x). 
UEU 

282 
STOCHASTIC OPTIMAL CONTROL 
To obtain the reverse inequality we choose the specific control law u(t, x) = 
g(t,x). Going through the same calculations as above, and using the fact that 
by assumption we have 
aH 
,(t,x) 
+ F
g(t,x) + dgH(t, x) = 0, 
we obtain the equality 
On the other hand we have the trivial inequality 
V(t, x) 2 J ( t ,  2, g), 
so, using (19.24)-(19.26), we obtain 
H(t, x) 2 V(t, x) 2 a t ,  2, g) = H(t, 2). 
This shows that in fact 
H(t,x) = V(t,x) = J ( t ,  2, g), 
which proves that H = V, and that gs is the optimal control law. 
Remark 19.3.4 The assumption that H is "sufficiently integrable" in the the- 
orem above is made in order for the stochastic integral in the proof to have 
expected value zero. This will be the case if, for example, H satisifes the condition 
V,H(s,X,U)aU(s, X4) 
E L2, 
for all admissible control laws. 
Remark 19.3.5 Sometimes, instead of a maximization problem, we consider a 
minimization problem. Of course we now make the obvious definitions for the 
value function and the optimal value function. It is then easily seen that all the 
results above still hold if the expression 
sup {F(t,x, u) + d
UV(t, x)) 
uEU 
in the HJB equation is replaced by the expression 
i d  (F(t, x, u) + A
UV(t, x)). 
uEU 
Remark 19.3.6 In the Verification Theorem we may allow the control con- 
straint set U to be state and time dependent, i.e. of the form U (t, x). 

HANDLING THE HJB EQUATION 
19.4 Handling the HJB Equation 
In this section we will describe the actual handling of the HJB equation, and in 
the next section we will study a classical example-the linear quadratic regulator. 
We thus consider our standard optimal control problem with the corresponding 
(
t
,
 
x) + ::g 
{F(t,x,u) + duV(t,x)} = 0, 
(19.27) 
V(T, x) = @(x). 
Schematically, we now proceed as follows: 
1. Consider the HJB equation as a PDE for an unknown function V. 
/ 
2. Fix an arbitrary point (t, x) E [0, TI x Rn and solve, for this fixed choice 
of (t, x) , the static optimization problem 
max [F(t, x, u) + AuV(t, x)] 
uEU 
Note that in this problem u is the only variable, whereas t and x are 
considered to be fixed parameters. The functions F, p, u, and V are 
considered as given. 
3. The optimal choice of u, denoted by G ,  will of course depend on our choice 
of t and x, but it will also depend on the function V and its various 
partial derivatives (which are hiding under the sign duV). To highlight 
I' 
these dependencies we write ii as 
5 
Q=Q(t,x;V). 
(19.28) 
4. The function 4 (t, x; V) is our candidate for the optimal control law, but 
since we do not know V this description is incomplete. Therefore we sub- 
stitute the expression for 4 in (19.28) into the PDE (19.27), giving us 
the PDE 
av 
-(t, 
x) + ~ ' ( t ,  x) + d ' ~ ( t ,  x) = 0, 
at 
(19.29) 
V(T,x) = @(x). 
(19.30) 
I , '  
5. Now we solve the PDE above! (See the remark below.) Then we put the 
solution V into expression (19.28). Using the verification theorem 19.6 we 
can now identify V as the optimal value function, and 4 as the optimal 
control law. 
Remark 19.4.1 The hard work of dynamic programming consists in solving the 
highly nonlinear PDE in step 5 above. There are of course no general analytic 

284 
STOCHASTIC OPTIMAL CONTROL 
methods available for this, so the number of known optimal control problems 
with an analytic solution is very small indeed. In an actual case one usually tries 
to guess a solution, i.e. we typically make an ansatz for V, parameterized by a 
finite number of parameters, and then we use the PDE in order to identify the 
parameters. The making of an ansatz is often helped by the intuitive observation 
that if there is an analytical solution to the problem, then it seems likely that 
V inherits some structural properties from the boundary function 
as well as 
from the instantaneous utility function F. 
For a general problem there is thus very little hope of obtaining an analytic 
solution, and it is worth pointing out that many of the known solved control 
problems have, to some extent, been "rigged" in order to be analytically solvable. 
19.5 The Linear Regulator 
We now want to put the ideas from the previous section into action, and for this 
purpose we study the most well known of all control problems, namely the linear 
quadratic regulator problem. In this classical engineering example we wish to 
minimize 
E [iT 
{ x : ~ X t  + u:Rut} dt + XhHXT , I 
(where I denotes transpose) given the dynamics 
One interpretation of this problem is that we want to control a vehicle in such 
a way that it stays close to the origin (the terms xtQx and xlHx) while at the 
same time keeping the "energy" utRu small. 
As usual Xt E Rn and ut E R ~ ,  
and we impose no control constraints on u. 
The matrices Q, R, H, A, B, and C are assumed to be known. Without loss of 
generality we may assume that Q, R, and H are symmetric, and we assume that 
R is positive definite (and thus invertible). 
The HJB equation now becomes 
(g 
(t, x) + inf {xtQx + ulRu + [V.V] (t, $) [Ax + Bu]} 
u€Rk 
For each fixed choice of (t, x) we now have to solve the static unconstrained 
optimization problem to minimize 
utRu + [V,V](t,x) [Az + Bu] . 

THE LINEAR REGULATOR 
285 
Since, by assumption, R > 0 we get the solution by setting the gradient equal 
to zero, thus giving us the equation 
which gives us the optimal u as 
Here we see clearly (compare point 2 in the scheme above) that in order to 
use this formula we need to know V, and we thus try to make an educated 
guess about the structure of V. From the boundary value function xtHx and 
the quadratic term xtQx in the instantaneous cost function it seems reasonable 
to assume that V is a quadratic function. Consequently we make the following 
ansatz: 
V(t, 2) = xfP(t)x + q(t), 
where we assume that P(t) is a deterministic symmetric matrix function of time, 
whereas q(t) is a scalar deterministic function. It would of course also be natural 
to include a linear term of the form L(t)x, but it turns out that this is not 
necessary. 
With this trial solution we have, suppressing the t-variable and denoting time 
derivatives by a dot, 
Inserting these expressions into the HJB equation we get 
We note that the last term above equals tr[CtPC], where tr denote the trace of 
a matrix, and furthermore we see that 2xfPAx = xtAtPx + xtPAx (this is just 
cosmetic). Collecting terms gives us 
If this equation is to hold for all x and all t then firstly the bracket must vanish, 
leaving us with the matrix ODE 
P = PBR-'B'P - A'P - PA - Q. 

286 
STOCHASTIC OPTIMAL CONTROL 
We are then left with the scalar equation 
We now need some boundary values for P and q, but these follow immediately 
from the boundary conditions of the HJB equation. We thus end up with the 
foll~wing pairs of equations: 
P = PBR-'B'P - A'P - PA - Q, 
P ( T )  = H. 
The matrix equation (19.32) is known as a Riccati equation, and there are 
powerful algorithms available for solving it numerically. The equation for q can 
then be integrated directly. 
Summing up we see that the optimal value function and the optimal control 
law are given by the following formulas. Note that the optimal control is linear 
in the state variable. 
19.6 Optimal Consumption and Investment 
19.6.1 A Generalization 
In many concrete applications, in particular in economics, it is natural to consider 
an optimal control problem, where the state variable is constrained to stay within 
a prespecified domain. As an example it may be reasonable to demand that the 
wealth of an investor is never allowed to become negative. We will now generalize 
our class of optimal control problems to allow for such considerations. 
Let us therefore consider the following controlled SDE: 
where as before we impose the control constraint ut E U. We also consider as 
given a fixed time interval [0, TI, and a fixed domain D G [0, TI x Rn, and the 
basic idea is that when the state process hits the boundary dD of D, then the 
activity is at an end. It is thus natural to define the stopping time T by 
7 = inf {t 2 01 (t, Xt ) E aD) 
A T, 

OPTIMAL CONSUMPTION AND INVESTMENT 
287 
i 
where x A y = min[x, y]. We consider as given an instantaneous utility function 
F(t, x, u )  and a "bequest function" @(t, x), i.e. a mapping @ : d D  -t R. The 
control problem to be considered is that of maximizing 
In order for this problem to be interesting we have to demand that Xo E D, and 
the interpretation is that when we hit the boundary aD, 
the game is over and 
we obtain the bequest @ (7, 
XT). We see immediately that our earlier situation 
corresponds to the case when D = [O,T] x Rn and when @ is constant in the 
i t-variable. 
' 
In order to analyze our present problem we may proceed as in the previous 
sections, introducing the value function and the optimal value function exactly 
as before. The only new technical problem encountered is that of considering 
a stochastic integral with a stochastic limit of integration. Since this will take 
us outside the scope of the present text we will confine ourselves to giving the 
results. The proofs are (modulo the technicalities mentioned above) exactly as 
before. 
Theorem 19.7 (HJB equation) Assume that 
The optimal value function V is in 
An optimal law u exists. 
Then the following hold: 
1. V satisifies the HJB equation 
[ $(t,.) 
+ sup {F(t,x,u) + AuV(t,x)} = 0, V(t,x) E D, 
UEU 
I 
V(t, 
X )  = @(t, 
x), V(t, X )  E dD. 
2. For each (t,x) E D the supremum in the HJB equation above is attained 
by 21 = a(t, X I .  
Theorem 19.8 (Verification theorem) Suppose that we have two functions 
H(t, x )  and g(t, x), such that 
H is suficiently integrable, and solves the HJB equation 
{~(t,x)+~m;{F(t,x,u)+AuH(t,x)}=O, 
V ( t , x ) € D ,  
H(t, x )  = @(t, 
x), V(t, x )  E dD. 
The function g is an admissible control law. 

288 
STOCHASTIC OPTIMAL CONTROL 
For each jixed (t, x), the supremum in the expression 
sup {F(t,x, u) + duH(t,x)} 
uEU 
is attained by the choice u = g(t, 2). 
Then the following hold: 
1. The optimal value function V to the control problem is given by 
2. There exists an optimal control law ii, and in fact u(t, x) = g(t, x). 
19.6.2 Optimal Consumption 
In order to illustrate the technique we will now go back to the optimal consump 
tion problem at the beginning of the chapter. We thus consider the problem of 
maximizing 
given the wealth dynamics 
As usual we impose the control constraints 
In a control problem of this kind it is important to be aware of the fact 
that one may quite easily formulate a nonsensical problem. To take a simple 
example, suppose that we have @ = 0, and suppose that F is increasing and 
unbounded in the c-variable. Then the problem above degenerates completely. It 
does not possess an optimal solution at all, and the reason is of course that the 
consumer can increase his/her utility to any given level by simply consuming an 
arbitrarily large amount at every t. The consequence of this hedonistic behavior 
is of course the fact that the wealth process will, with very high probability, 
become negative, but this is neither prohibited by the control constraints, nor 
punished by any bequest function. 
An elegant way out of this dilemma is to choose the domain D of the preceding 
section as D = [0, TI x { X ~ X  > 0). With T defined as above this means, in concrete 
terms, that 
r=inf{t>O(Xt=O}AT. 

OPTIMAL CONSUMPTION AND INVESTMENT 
A natural objective function in this case is thus given by 
which automatically ensures that when the consumer has no wealth, then all 
activity is terminated. 
We will now analyze this problem in some detail. Firstly we notice that we 
can get rid of the constraint uf + u: = 1 by defining a new control variable w as 
w = ul, and then substituting 1 - w for uO. This gives us the state dynamics 
dXt = wt [or - r] Xt dt + (rXt - ct ) dt + wuxt dwt , 
(19.42) 
and the corresponding HJB equation is 
We now specialize our example to the case when F is of the form 
where 0 < 7 < 1. The economic reasoning behind this is that we now have 
an infinite marginal utility at c = 0. This will force the optimal consumption 
plan to be positive throughout the planning period, a fact which will facilitate 
the analytical treatment of the problem. In terms of Remark 19.4.1 we are thus 
"rigging" the problem. 
The static optimization problem to be solved w.r.t. c and w is thus that of 
maximizing 
av 
av I , ,  ,3 
e-6tc7 + wx(a - r)- 
+ (rx - c)- 
+ -x w u 
ax 
ax 
2 
ax2 ' 
and, assuming an interior solution, the first-order conditions are 
-Vx 
a- r  
w=- 
.- 
2. vzx u2 ' 
where we have used subscripts to denote partial derivatives. 
We again see that in order to implement the optimal consumption-investment 
plan (19.43)-(19.44) we need to know the optimal value function V. We therefore 

290 
STOCHASTIC OPTIMAL CONTROL 
suggest a trial solution (see Remark 19.4.1), and in view of the shape of the 
instantaneous utility function it is natural to try a V-function of the form 
where, because of the boundary conditions, we must demand that 
h(T) = 0. 
(19.46) 
Given a V of this form we have (using to denote the time derivative) 
Inserting these expressions into (19.43)-(19.44) we get 
a- r  
~ ( t ,  
x) = a2(1 -y)' 
This looks very promising: we see that the candidate optimal portfolio is constant 
and that the candidate optimal consumption rule is linear in the wealth variable. 
In order to use the verification theorem we now want to show that a V-function 
of the form (19.45) actually solves the HJB equation. We therefore substitute the 
expressions (19.47)-(19.51) into the HJB equation. This gives us the equation 
where the constants A and B are given by 
If this equation is to hold for all x and all t, then we see that h must solve 
the ODE 

THE MUTUAL FUND THEOREMS 
291 
j 
An equation of this kind is known as a Bernoulli equation, and it can be 
solved explicitly (see the exercises). 
3 
Summing up, we have shown that if we define V as in (19.45) with h defined as 
! the solution to (19.52)-(19.53), and if we define w and 2 by (19.50)-(19.51), then 
I V satisfies the HJB equation, and dt, i: attain the supremum in the equation. The 
I 
verification theorem then tells us that we have indeed found the optimal solution. 
j 19.7 The Mutual Fund Theorems 
In this section we will briefly go through the "Merton mutual fund theorems", 
originally presented in Merton (1971). 
1 19.7.1 The Case with No Risk h
e
 Asset 
We consider a financial market with n asset prices S1, . . . , S,. To start with we 
do not assume the existence of a risk free asset, and we assume that the price 
vector process S(t) has the following dynamics under the objective measure P. 
Here W is a k-dimensional standard Wiener process, a is an n-vector, a is an 
8 
n x k matrix, and D(S) is the diagonal matrix 
D(S) = diag[S~, . . . , S,] . 
In more pedestrian terms this means that 
where oi is the ith row of the matrix a. 
We denote the investment strategy (relative portfolio) by w, and the con- 
sumption plan by c. If the pair (w, c) is self-financing, then it follows from the 
S-dynamics above, and from Lemma 6.4, that the dynamics of the wealth process 
X are given by 
dX = Xw'a dt - cdt + Xw'a dW. 
(19.55) 
We also take as given an instantaneous utility function F(t, c), and we basically 
want to maximize 
E [iT 
F(t,G)dt] , 
where T is some given time horizon. In order not to formulate a degenerate 
problem we also impose the condition that wealth is not allowed to become 
negative, and as before this is dealt with by introducing the stopping time 

292 
STOCHASTIC OPTIMAL CONTROL 
Our formal problem is then that of maximizing 
given the dynamics (19.54)-(19.55), and subject to the control constraints 
Instead of (19.56) it is convenient to write 
where e is the vector in Rn which has the number 1 in all components, i.e. 
ef = (1,. .. ,I). 
The HJB equation for this problem now becomes 
In the general case, when the parameters a and u are allowed to be functions 
of the price vector process S, the term AC~"V(t,x, 
s) turns out to be rather 
forbidding (see Merton's original paper). It will in fact involve partial derivatives 
to the second order with respect to all the variables x, 81,. . . ,s,. 
If, however, we assume that a and u are deterministic and constant over 
time, then we see by inspection that the wealth process X is a Markov process, 
and since the price processes do not appear, neither in the objective function nor 
in the definition of the stopping time, we draw the conclusion that in this case 
X itself will act as the state process, and we may forget about the underlying 
S-process completely. 
Under these assumptions we may thus write the optimal value function as 
V(t, x), with no s-dependence, and after some easy calculations the term AclwV 
turns out to be 
, av 
av 1 2 , a2v 
dcyWV 
= xw a- - c- + -x w Cw- 
ax 
ax 
2 
ax2 ' 
where the matrix C is given by 
We now summarize our assumptions. 

THE MUTUAL FUND THEOREMS 
Assumption 19.7.1 We assume that 
the vector o is constant and deterministic, 
the matrix a is constant and deterministic, 
the matrix u has rank n, and in particular the matrix C = out is positive 
definite and invertible. 
We note that, in terms of contingent claims analysis, the last assumption 
means that the market is complete. Denoting partial derivatives by subscripts 
we now have the following HJB equation 
sup 
{ ~ ( t ,  
c) + (xw'o - c)VX(t, x) + !~x~w'cwv,~(~, 
5)) =0, 
w'e=l,c20 
If we relax the constraint w'e = 1, the Lagrange function for the static 
optimization problem is given by 
L = F(t,c) + (xw'a - c)Vx(t,x) + ~ x 2 w ' ~ w ~ , , ( t ,  
x) + X (1 - w'e) 
Assuming the problem to be regular enough for an interior solution we see that 
the first order condition for c is 
The first order condition for w is 
xafVX + X~V~,W'C = Xe', 
so we can solve for w in order to obtain 
Using the relation e'w = 1 this gives X as 
and inserting this into (19.58) gives us, after some manipulation, 

294 
STOCHASTIC OPTIMAL CONTROL 
To see more clearly what is going on we can write this expression as 
w(t) = g,+ Y(t)h, 
(19.60) 
where the fixed vectors g and h are given by 
whereas Y is given by 
Y(t) = 
Vx(t, X(t)) 
X(t)Vxx(t, X(t)) ' 
Thus we see that the optimal portfolio is moving stochastically along the one 
dimensional "optimal portfolio line" 
9 + sh, 
in the (n - 1)-dimensional "portfolio hyperplane" A, where 
We now make the obvious geometric observation that if we fix two points on 
the optimal portfolio line, say the points wa = g + ah and wb = g + bh, then any 
point w on the line can be written as an f i n e  combination of the basis points 
wa and wb. An easy calculation shows that if ws = g + sh then we can write 
where 
S- b  
p = -  a- b' 
The point of all this is that we now have an interesting economic interpretation of 
the optimality results above. Let us thus fix wa and wb as above on the optimal 
portfolio line. Since these points are in the portfolio plane A we can interpret 
them as the relative portfolios of two fixed mutual funds. We may then write 
(19.60) as 
w(t) = p(t)wa + (1 - p(t))wb, 
(19.64) 
with 
Y (t) - b 
d t )  = a - b 
* 
Thus we see that the optimal portfolio w can be obtained as aUsuper portfolio" 
where we allocate resources between two fixed mutual funds. 

THE MUTUAL FUND THEOREMS 
'heorem 19.9 (Mutual fund theorem) Assume that the problem is regular 
nough to allow for an interior solution. Then there exists a one-dimensional 
urameterized family of mutual funds, given by wS = g + sh, where g and h are 
efined by (1 9.62)-(19.62), such that the following hold: 
1. For each fied s the relative portfolio wS stays fied over time. 
2. For any fied choice of a # b the optimal portfolio w(t) is, for all values 
of t, obtained by allocating a11 resources between the fied funds wa and 
wb, i.e. 
+(t) = pa(t)wa + pb(t)~b, 
pa(t) + pb(t) = 1. 
3. The relative proportions (pa, pb) of the portfolio wealth allocated to wa and 
wb respectively are given by 
Y(t) - b 
pa(t) = -, a - b  
a - Y (t) 
P ~ ( ~ )  
= a - b 
3 
where Y is given by (19.65'). 
19.7.2 The Case with a Risk flee Asset 
Again we consider the model 
dS = D(S)a dt + D(S)a dW(t), 
with the same assumptions as in the preceding section. We now also take as 
given the standard risk free asset B with dynamics 
dB = r B  dt. 
Formally we can denote this as a new asset by subscript zero, i.e. B = So, and 
then we can consider relative portfolios of the form w = (wO, w1,. . . , w,,)' where 
of course Ct w, = 1. Since B will play such a special role it will, however, be 
convenient to eliminate wo by the relation 
n 
W~=I-CW~, 
1 
and then use the letter w to denote the portfolio weight vector for the risky 
assets only. Thus we use the notation 
w = (wI,. .. ,wn)', 

296 
STOCHASTIC OPTIMAL CONTROL 
and we note that this truncated portfolio vector is allowed to take any value 
in Rn . 
Given this notation it is easily seen that the dynamics of a self-financing port- 
folio are given by 
That is, 
where as before e E Rn denotes the vector (1,1,. . . ,I)'. 
The HJB equation now becomes 
K ( t , x )  + 
sup 
{F(t,c) + dc9wV(t,x)) 
=0, 
c>O, wERn 
V(T, x )  = 0, 
V(t,O) =0, 
* ' ,  t 
where 
dcV = xwl(a - re)Vx(t, x )  + (rx - c)V,(t,x) + ~x2w1CwVx,(t, x). 
The first order conditions for the static optimization problem are 
' I  
8 F  
-(t, 
8c 
c) = Vx(t, x), 
w=-- 
+ 
Vx ~ - l ( n  
- re), 
xv,, 
and again we have a geometrically obvious economic interpretation. 
Theorem 19.10 (Mutual fund theorem) Given assumptions as above, the 
following hold: 
1. The optimal portfolio consists of an allocation between two fied mutual 
funds w0 and w f .  
2. The fund w0 consists only of the risk free asset. 
3. The fund w f  consists only of the risky assets, and is given by 
wf = ~ - ' ( a  - re). 

EXERCISES 
297 
4. At each t the optimal relative allocation of wealth between the funds is 
given by 
Vz(t, X(t)) 
'f(t) = - ~ ( t ) ~ , ( t ,  
~ ( t ) )  
' 
/JO(t) = 1 - 'f (t). 
Note that this result is not a corollary of the corresponding result from the 
previous section. Firstly it was an essential ingredient in the previous results 
that the volatility matrix of the price vector was invertible. In the case with a 
riskless asset the volatility matrix for the entire price vector (B, S1, . . . , S,) is of 
course degenerate, since its first row (having subscript zero) is identically equal 
to zero. Secondly, even if one assumes the results from the previous section, i.e. 
that the optimal portfolio is built up from two fixed portfolios, it is not at all 
obvious that one of these basis portfolios can be chosen so as to consist of the 
risk free asset alone. 
19.8 Exercises 
Exercise 19.1 Solve the problem of maximizing logarithmic utility 
. 
[lT 
e-'. 
In,,) 
dt + K . ,,(,) 
, 
given the usual wealth dynamics 
I 
dXt = Xt [U:T + u: a] dt - ct dt + u1 U X ~  
dWt , 
and the usual control constraints 
ct 2 0, vt 1 0 ,  
u;+u; =1, 
Vt10. 
Exercise 19.2 A Bernoulli equation is an ODE of the form 
xt + Atxt + Btx," = 0, 
where A and B are deterministic functions of time and a is a constant. 
If a = 1 this is a linear equation, and can thus easily be solved. Now consider 
the case a # 1 and introduce the new variable y by 
yt = X:-? 
Show that y satisfies the linear equation 
$t + (1 - a)Atyt + (1 - a)Bt = 0. 

298 
STOCHASTIC OPTIMAL CONTROL 
Exercise 19.3 Use the previous exercise in order to solve (19.52)-(19.53) 
explicitly. 
Exercise 19.4 The following example is taken from Bjork et al. (1987). We 
consider a consumption problem without risky investments, but with stochastic 
prices for various consumption goods. 
N = the number of consumption goods, 
pi(t) = price, at t, of good i (measured as dollars per unit per unit time), 
ci(t) = rate of consumption of good i, 
c(t) = [el (t), . - . cN(t)ll, 
1 
* 
X(t) = wealth process, 
1 
' 
r = short rate of interest, 
T = time horizon. 
. 
3 '  
We assume that the consumption price processes satisfy 
where Wl , . . . , W,, are independent. The X-dynamics become 
dX = rXdt - c'pdt, 
and the objective is to maximize expected discounted utility, as measured by 
E [lT 
~ ( t ,  
Q) dt] , 
where T is the time of ruin, i.e. 
(a) Denote the optimal value function by V(t,x,p) and write down the 
relevant HJB equation (including boundary conditions for t = T and 
x = 0). 
(b) Assume that F is of the form 

1 
EXERCISES 
299 
I 
where 6 > 0,O < ai < 1 and a = C? a+ < 1. Show that the optimal 
value function and the optimal control-have the structure 
V(t,x,p) = e-st x a a -aG ( t , ~ ) ,  
x ai 
4, 
x, P) = - - -A(p)'G(t, 
P), 
Pi 
a 
I 
where G solves the nonlinear equation 
If you find this too hard, then study the simpler case when N = 1. 
(c) Now assume that the price dynamics are given by GBM, i.e. 
k 
Try to solve the G-equation above by making the ansatz 
Warning: This becomes somewhat messy. 
Exercise 19.5 Consider as before state process dynamics 
and the usual restrictions for u. Our entire derivation of the HJB equation has 
so far been based on the fact that the objective function is of the form 
Sometimes it is natural to consider other criteria, like the expected exponential 
utility criterion 
For this case we define the optimal value function as the supremum of 

300 
STOCHASTIC OPTIMAL CONTROL 
Follow the reasoning in Section 19.3 in order to show that the HJB equation f o ~  
the expected exponential utility criterion is given by 
{$(., 
+ s, 
{V(t, x)F(t, x, u) + AUV(t,x)} = 0, 
V(T, x) = e @ ( ~ ) .  
Exercise 19.6 Solve the problem to minimize 
given the scalar dynamics 
where the control u is scalar and there are no control constraints. 
Hint: Make the ansatz 
Exercise 19.7 Study the general linear-exponential-qudratic control problem 
of minimizing 
given the dynamics 
dXt ={A&+ But) dt+CdWt. 
Exercise 19.8 The object of this exercise is to connect optimal control to 
martingale theory. Consider therefore a general control problem of minimizing 
given the dynamics 
dXt = P (t, Xt , ut) dt + 0 (t, Xt , ~ t )  
dWt , 
.i 
and the constraints 
u(t, x) E U. 

NOTES 
Now, for any control law u, define the total cost process C(t; u) by 
i.e. 
C(t; U) = 
F(s, X,U, us) ds + J(t, X,U, u). 
6' 
Use the HJB equation in order to prove the following claims: 
(a) If u is an arbitrary control law, then C is a submartingale. 
(b) If u is optimal, then C is a martingale. 
19.9 Notes 
Standard references on optimal control are Fleming and Rishel(1975) and Krylov 
(1980). A very clear exposition can be found in Bksendal(1995). For more recent 
work, using viscosity solutions, see Fleming and Soner (1993). The classical 
papers on optimal consumption are Merton (1969) and Merton (1971). See also 
Karatzas et al. (1987), and the survey paper DufEe (1994). For optimal trading 
under constraints, and its relation to derivative pricing see Cvitanib (1997) and 
references therein. See also the book by Korn (1997). There is also a "martingale 
approach" to optimal investment problems. See Cox and Huang (1989) for the 
complete market case. Basic papers on the incomplete market case are He and 
Pearson (1991), Karatzas et al. (1991), and Krarnkov and Schachermayer (1999). 
A very readable overview of the incomplete market case, containing an extensive 
bibliography, is given in Schachermayer (2002). 

BONDS AND INTEREST RATES 
20.1 Zero Coupon Bonds 
In this chapter, we will begin to study the particular problems which appear 
when we try to apply arbitrage theory to the bond market. The primary objects 
of investigation are zero coupon bonds, also known as pure discount bonds, 
of various maturities. All payments are assumed to be made in a fixed currency 
which, for convenience, we choose to be US dollars. 
Definition 20.1 A zero coupon bond with maturity date T, also called 
a T-bond, is a contract which guarantees the holder 1 dollar to be paid on the 
date T. The price at time t of a bond with maturity date T is denoted by p(t, T). 
The convention that the payment at the time of maturity, known as the 
principal value or face value, equals one is made for computational con- 
venience. Coupon bonds, which give the owner a payment stream during the 
interval [0, T] are treated below. These instruments have the common property, 
that they provide the owner with a deterministic cash flow, and for this reason 
they are also known as fixed income instruments. 
We now make an assumption to guarantee the existence of a sufficiently rich 
and regular bond market. 
Assumption 20.1.1 We assume the following: 
There exists a (frtctionless) market for T-bonds for every T > 0. 
The relation p(t, t) = 1 holds for all t. 
For each fied t, the bond price p(t,T) is differentiable w.r.t. time of 
maturity T. 
Note that the relation p(t, t) = 1 above is necessary in order to avoid arbitrage. 
The bond price p(t, T) is thus a stochastic object with two variables, t and T, 
and, for each outcome in the underlying sample space, the dependence upon 
these variables is very different. 
For a fked value of t, p(t, T) is a function of T. This function provides the 
prices, at the fixed time t, for bonds of all possible maturities. The graph 
of this function is called "the bond price curve at t", or "the term structure 
at t". Typically it will be a very smooth graph, i.e. for each t, p(t, T) will 
be differentiable w.r.t. T. The smoothness property is in fact a part of our 
assumptions above, but this is mainly for convenience. All models to be 
considered below will automatically produce smooth bond price curves. 
For a fixed maturity T, p(t, T) (as a function oft) will be a scalar stochastic 
process. This process gives the prices, at different times, of the bond with 

INTEREST RATES 
303 
fixed maturity T, and the trajectory will typically be very irregular (like a 
Wiener process). 
We thus see that (our picture of) the bond market is different from any other 
market that we have considered so far, in the sense that the bond market contains 
an infinite number of assets (one bond type for each time of maturity). The basic 
goal in interest rate theory is roughly that of investigating the relations between 
all these different bonds. Somewhat more precisely we may pose the following 
general problems, to be studied below: 
What is a reasonable model for the bond market above? 
a Which relations must hold between the price processes for bonds of different 
maturities, in order to guarantee an arbitrage free bond market? 
a Is it possible to derive arbitrage free bond prices from a specification of the 
dynamics of the short rate of interest? 
Given a model for the bond market, how do you compute prices of interest 
rate derivatives, such as a European call option on an underlying bond? 
20.2 Interest Rates 
20.2.1 Definitions 
Given the bond market above, we may now define a number of interest rates, 
and the basic construction is as follows. Suppose that we are standing at time t, 
and let us ~IX two other points in time, S and T, with t < S < T. The immediate 
project is to write a contract at time t which allows us to make an investment of 
one (dollar) at time S, and to have a deterministic rate of return, determined 
at the contract time t, over the interval [S, TI. This can easily be achieved as 
follows: 
1. At time t we sell one S-bond. This will give us p(t, S) dollars. 
2. We use this income to buy exactly p(t, S)/p(t,T) T-bonds. Thus our net 
investment at time t equals zero. 
3. At time S the S-bond matures, so we are obliged to pay out one dollar. 
4. At time T the T-bonds mature at one dollar a piece, so we will receive the 
amount p(t, S)/p(t, T) dollars. 
5. The net effect of all this is that, based on a contract at t, an investment 
of one dollar at time S has yielded p(t, S)/p(t, T) dollars at time T. 
6. Thus, at time t, we have made a contract guaranteeing a riskless rate of 
interest over the future interval [S, TI. Such an interest rate is called a 
forward rate. 
We now go on to compute the relevant interest rates implied by the con- 
struction above. We will use two (out of many possible) ways of quoting forward 
rates, namely as continuously compounded rates or as simple rates. 
The simple forward rate (or LIBOR rate) L, is the solution to the equation 

304 
BONDS AND INTEREST RATES 
whereas the continuously compounded forward rate R is the solution to the 
' 
eauation 
The simple rate notation is the one used in the market, whereas the continuously 
compounded notation is used in theoretical contexts. They are of course logically 
equivalent, and the formal definitions are as follows. 
Definition 20.2 
1. The simple forward rate for [S, TI contracted at t, henceforth referred 
to as the LIBOR forward mte, is defined as 
2. The simple spot rate for [S,T], henceforth referred to as the LIBOR 
spot rate, is defined as 
3. The continuously compounded forward rate for [S, TI contracted at t 
is defined as 
R(t; S, T )  = - 1% P(t, T) - 1% P(t, S) 
T - S  
4. The continuously compounded spot rate, R(S, T), for the period 
[S, TI is defined as 
R(S, T) = - 1% P(S, T )  
T - S  ' 
5. The instantaneous forward rate with maturity T, contracted at t, 
is defined by 
6. The instantaneous short rate at time t is defined by. 
We note that spot rates are forward rates where the time of contracting 
coincides with the start of the interval over which the interest rate is effective, 
i.e. t = S. The instantaneous forward rate, which will be of great importance 
below, is the limit of the continuously compounded forward rate when S + T. 
rt can thus be interpreted as the riskless rate of interest, contracted at t, over 
the infinitesimal interval [T, T + dT] . 
We now go on to define the money account process B. 

INTEREST RATES 
Definition 20.3 The money account process is defined by 
{ d ~ ( t )  
=r(t)B(t) dt, 
B(0) = 1. 
The interpretation of the money account is the same as before, i.e. you may 
think of it as describing a bank with a stochastic short rate of interest. It can 
also be shown (see below) that investing in the money account is equivalent to 
I 
investing in a self-financing "rolling over" trading strategy, which at each time t 
5 
consists entirely of "just maturing" bonds, i.e. bonds which will mature at t + dt. 
I 
As an immediate consequence of the definitions we have the following useful 
formulas. 
Lemma 20.4 For t 5 s 5 T we have 
If we wish to make a model for the bond market, it is obvious that this can 
be done in many different ways. 
a We may specify the dynamics of the short rate (and then perhaps try to 
derive bond prices using arbitrage arguments). 
a We may directly specify the dynamics of all possible bonds. 
a We may specify the dynamics of all possible forward rates, and then use 
Lemma 20.4 in order to obtain bond prices. 
i 
All these approaches are of course related to each other, and we now go on to 
present a small  toolbox^' of results to facilitate the analysis below. These results 
1 will not be used until Chapter 23, and the proofs are somewhat technical, so the 
next two subsections can be omitted at a first reading. 
1 20.2.2 Relations between d f (t, T), dp(t, T), and dr(t) 
We will consider dynamics of the following form: 
Short rate dynamics 

306 
BONDS AND INTEREST RATES 
Bond price dynamics 
Forward rate dynamics 
df (t, T) = a(t, T) dt + a(t, T) dW(t). 
(20.3) 
The Wiener process W is allowed to be vector valued, in which case the volat- 
ilities v(t, T) and a(t, T) are row vectors. The processes a(t) and b(t) are scalar 
adapted processes, whereas m(t, T) , v(t, T), a(t, T), and u(t, T) are adapted 
processes parameterized by time of maturity T. The interpretation of the bond 
price equation (20.2) and the forward rate equation(20.3) is that these are scalar 
stochastic differential equations (in the t-variable) for each fixed time of maturity 
T. Thus (20.2) and (20.3) are both infinite dimensional systems of SDEs. 
We will study the formal relations which must hold between bond prices and 
interest rates, and to this end we need a number of technical assumptions, which 
we collect below in an "operational" manner. 
Assumption 20.2.1 
1. For each fied w, t all the objects m(t,T), v(t,T), a(t,T) and u(t,T) are 
assumed to be wntinuously di.@erentiable in the T-variable. This partial 
T-derivative is sometimes denoted by mT(t, T), etc. 
2. All processes are assumed to be regular enough to allow us to differentiate 
under the integral sign as well as to interchange the order of integration. 
The main result is as follows. Note that the results below hold, regardless 
of the measure under consideration, and in particular we do not assume that 
markets are free of arbitrage. 
Proposition 20.5 
1. If p(t, T) satisfies (20.2), then for the fonuard rate dynamics we have 
df (t, T) = a(t, T) dt + a(t, T) dW(t), 
where a and a are given by 
a(t, T )  = UT(~, 
T) . ~ ( t ,  
T) - mT(t, T), 
u(t,T) = -vT(~, T). 
2. Iff (t, T) satisfies (20.3) then the short rate satisfies 
where 
a(t) = fT(t, t) + ~ ( t ,  
t), 
b(t) = o(t, t). 

INTEREST RATES 
3. If f (t, T) satisfies (20.3) then p(t, T) satisfies 
dp(t, T) = p(t, T) {r(t) + A(t, T) + 4 IIS(t, T)l12) dt + ~ ( t ,  
T)S(t, T) dW(t), 
where 11 - 11 denotes the Euclidean norm, and 
{ 
T 
A(t, T) = - 
a(t, s) ds, 
(20.6) 
S(t,T) = - f u ( t ,  s)ds. 
Proof The first part of the proposition is left to the reader (see the exercises). 
For the second part we integrate the forward rate dynamics to get 
t 
r(t) = f (0, t) + 
t) + /d ~ ( 8 ,  
t) dW(s)- 
(20.7) 
Now we can write 
a(s, t) = a(s, S) + 
~ T ( s ,  
u) du, 
1" 
r 
' I 
U(S, t) = U(S, S) + 
UT(S, u) du, 
l 
and, inserting this into (20.7), we have 
r(t) = f(0, t) + [ 
a(s, s) ds + [[ 
cxT(s, u) duds 
+&t u(s,s)dWs+ Jot l U ~ ( s , u ) d u d W s .  
Changing the order of integration and identifying terms we obtain the result. 
For the proof of the third part we give a slightly heuristic argument. The full 
formal proof, see Heath et al. (1987), is an integrated version of the proof given 
here, but the infinitesimal version below is (hopefully) easier to understand. 
Using the definition of the forward rates we may write 
p(t, T) = eY(t9T;! , 
(20.8) 
where Y is given by 
T 
Y(t,T) = -1 f(t,s)ds. 
(20.9) 
From the It6 formula we then obtain the bond dynamics as 
dp(t, T) = ~ ( t ,  
T) dY(t, T) + +p(t, T) ( d ~ ( t ,  
T ) ) ~ ,  
(20.10) 

308 
BONDS AND INTEREST RATES 
and it remains to compute dY (t, T). We have 
I 
and the problem is that in the integral the t-variable occurs in two places: as the 
lower limit of integration, and in the integrand f (t, s). This is a situation that is 
not covered by the standard It6 formula, but it is easy to guess the answer. The 
t appearing as the lower limit of integration should give rise to the term 
a 
at (dT 
f(t,,)dS) dt. 
Furthermore, since the stochastic differential is a linear operation, we should be 
allowed to move it inside the integral, thus providing us with the term 
(lT 
df (4 8) ds) - 
We have therefore arrived at 
1 
which, using the fundamental theorem of integral calculus, as well as the forward 
rate dynamics, gives us 
We now exchange dt and dWt with ds and recognize f (t, t) as the short rate r(t), 
thus obtaining 
dY(t,T) = r(t)dt +A(t,T)dt + S(t,T)dWt, 
with A and S as above. We therefore have 
( d ~ ( t ,  = IIS(t, T)1I2 dt, 
and, substituting all this into (20.10), we obtain our desired result. 
20.2.3 An Alternative View of the Money Account 
The object of this subsection is to show (heuristically) that the risk free asset B 
can in fact be replicated by a self-financing strategy, defined by "rolling over" 
just-maturing bonds. This is a "folklore" result, which is very easy to prove in 
discrete time, but surprisingly tricky in a continuous time framework. 

t 
COUPON BONDS, SWAPS, AND YIELDS 
309 
I;i 
k 
4 
Let us consider a self-financing portfolio which at each time t consists entirely 
of bonds maturing x units of time later (where we think of x as a small number). 
At time t the portfolio thus consists only of bonds with maturity t + x, so the 
value dynamics for this portfolio is given by 
where the constant 1 indicates that the weight of the t + x-bond in the portfolio 
equals one. We now want to study the behavior of this equation as x tends to 
1 zero, and to this end we use Proposition 20.5 to obtain 
I 
j Letting x tend to zero, (20.6) gives us 
1 . 
lim A(t, t + x) = 0, 
x+o 
lim S(t, t + x) = 0. 
x-0 
Furthermore we have 
' C  
limp(t,t +x) = 1, 
x-0 
and, substituting all this into eqn (20.11), we obtain the value dynamics 
dV(t) = r(t)V(t) dt, 
(20.12) 
which we recognize as the dynamics of the money account. 
The argument thus presented is of course only hewistical, and it requires 
some hard work to make it precise. Note, for example, that the rolling over port- 
folio above does not fall into the general framework of self-financing portfolios, 
developed earlier. The problem is that, although at each time t, the portfolio 
only consists of one particular bond (maturing at t + x), over an arbitrary short 
j time interval, the portfolio will use an infinite number of different bonds. In order 
to handle such a situation, we need to extend the portfolio concept to include 
measure valued portfolios. This is done in Bjork et al. (1997a), and in Bjork 
et al. (1997b) the argument above is made precise. 
20.3 Coupon Bonds, Swaps, and Yields 
In most bond markets, there are only a relative small number of zero coupon 
bonds traded actively. The maturities for these are generally short (typically 
between half a year and two years), whereas most bonds with a longer time to 
maturity are coupon bearing. Despite this empirical fact we will still assume the 
existence of a market for all possible pure discount bonds, and we now go on to 
introduce and price coupon bonds in terms of zero coupon bonds. 


## Short Rate Models

310 
BONDS AND INTEREST RATES 
20.3.1 Fixed Coupon Bonds 
The simplest coupon bond is the fixed coupon bond. This is a bond which, 
at some intermediary points in time, will provide predetermined payments 
(coupons) to the holder of the bond. The formal description is as follows: 
Fix a number of dates, i.e. points in time, To,,. . . , Tn. Here To is interpreted 
as the emission date of the bond, whereas TI, . . . , Tn are the coupon dates. 
At time Ti, i = 1,. . . , n, the owner of the bond receives the deterministic 
coupon 4. 
At time Tn the owner receives the face value K. 
We now go on to compute the price of this bond, and it is obvious that the 
coupon bond can be replicated by holding a portfolio of zero coupon bonds with 
maturities Ti, i = 1,. . . , n. More precisely we will hold 4 zero coupon bonds of 
maturity T,, i = 1, . . . , n - 1, and K + c, bonds with maturity T,, so the price, 
p(t), at a time t < TI, 
of the coupon bond is given by 
Very often the coupons are determined in terms of return, rather than in 
monetary (e.g. dollar) terms. The return for the ith coupon is typically quoted 
as a simple rate acting on the face value K, over the period [T,_l,Ti]. Thus, if, 
for example, the ith coupon has a return equal to ri, and the face value is K, 
this means that 
ci = ri(T, - Ti-f)K. 
For a standardized coupon bond, the time intervals will be equally spaced, i.e. 
and the coupon rates rl, . . . , rn will be equal to a common coupon rate r. The 
price p(t) of such a bond will, for t 5 TI, be given by 
20.3.2 Floating Rate Bonds 
There are various coupon bonds for which the value of the coupon is not fixed 
at the time the bond is issued, but rather reset for every coupon period. Most 
often the resetting is determined by some financial benchmark, like a market 
interest rate, but there are also bonds for which the coupon is benchmarked 
I 
against a nonfinancial index. 

COUPON BONDS, SWAPS, AND YIELDS 
311 
As an example (to be used in the context of swaps below), we will confine 
ourselves to discussing one of the simplest floating rate bonds , where the coupon 
rate ri is set to the spot LIBOR rate L(Ti-1, Ti). Thus 
and we note that L(Ti-1, Ti) is determined already at time Ti-l, but that ci is 
not delivered until at time Ti. We now go on to compute the value of this bond 
at some time t < To, in the case when the coupon dates are equally spaced, 
with Ti - Ti-1 = 6, and to this end we study the individual coupon Q. Without 
loss of generality we may assume that K = 1, and inserting the definition of the 
LIBOR rate (Definition 20.2) we have 
The value at t, of the term -1 (paid out at T,), is of course equal to 
-P@, Ti), 
and it remains to compute the value of the term l l ~ ( T ~ _ ~ , T i ) ,  
which is paid 
out at Ti. 
This is, however, easily done through the following argument: 
i 
a Buy, at time t, one T,-l-bond. This will cost p(t, Ti-1). 
a At time Ti-1 you will receive the amount 1. 
MJ 
! 
a Invest this unit amount in Ti-bonds. This will give you exactly l/p(T,-l, Ti) 
bonds. 
a At T, the bonds will mature, each at the face value 1. Thus, at time Ti, 
you will obtain the amount 
1 
p(Ti-1, Ti) ' 
This argument shows that it is possible to replicate the cash flow above, using 
a self-financing bond strategy, to the initial cost p(t, Ti-1). Thus the value at t, 
of obtaining l l ~ ( T i _ ~ , T ~ )  
at Ti, is given by p(t, Ti-1), and the value at t of the 
coupon ci is 
~ ( t ,  
Ti-1) - ~ ( t ,  
Ti). 
Summing up all the terms we finally obtain the following valuation formula 
for the floating rate bond: 
In particular we see that if t = To, then p(To) = 1. The reason for this (perhaps 
surprisingly easy) formula is of course that the entire floating rate bond can be 
replicated through a self-financing portfolio (see the exercises). 

312 
BONDS AND INTEREST RATES 
20.3.3 Interest Rate Swaps 
In this section we will discuss the simplest of all interest rate derivatives, the 
interest rate swap. This is basically a scheme where you exchange a payment 
stream at a fixed rate of interest, known as the swap rate, for a payment 
stream at a floating rate (typically a LIBOR rate). 
There are many versions of interest rate swaps, and we will study the forward 
swap settled in arrears, which is defined as follows. We denote the principal 
by K, and the swap rate by R. By assumption we have a number of equally 
spaced dates To, . . . , Tn, and payment occurs at the dates TI,. . . , Tn (not at To). 
If you swap a fixed rate for a floating rate (in this case the LIBOR spot rate), 
then, at time Ti, you will receive the amount 
which is exactly Kci, where q is the ith coupon for the floating rate bond in the 
previous section. At Ti you will pay the amount 
KbR. 
The net cash flow at Ti is thus given by 
[L(Ti-1, Ti) - R], 
and using our results from the floating rate bond, we can compute the value at 
t < To of this cash flow as 
"k' 
i ' .,: 
~ p ( t ,  
T,-I) - K(1+ 6 ~ ) p ( t ,  
T,). 
The total value ll (t), at t, of the swap is thus given by 
and we can simplify this to obtain the following result. 
Proposition 20.6 The price, for t < To, of the swap above is given by 
where 
The remaining question is how the swap rate R is determined. By definition 
it is chosen such that the value of the swap equals zero at the time when the 
contract is made. We have the following easy result. 

COUPON BONDS, SWAPS, AND YIELDS 
313 
Proposition 20.7 If, by convention, we assume that the contract is written at 
t = 0, the swap rate is given by 
In the case that To = 0 this formula reduces to 
20.3.4 Yield and Duration 
Consider a zero coupon T-bond with market price p(t, T). We now look for the 
bond's "internal rate of interest", i.e. the constant short rate of interest which 
will give the same value to this bond as the value given by the market. Denoting 
this value of the short rate by y, we thus want to solve the equation 
where the factor 1 indicates the face value of the bond. We are thus led to the 
following definition. 
Definition 20.8 The continuously compounded zero coupon yield, y(t, T), is 
given by 
For a &ed t , the function T c--, y (t, T) is called the (zero coupon) yield curve. 
We note that the yield y(t, T) is nothing more than the spot rate for the 
interval [t, TI. Now let us consider a fixed coupon bond of the form discussed in 
Section 20.3.1 where, for simplicity of notation, we include the face value in the 
coupon c,. We denote its market value at t by p(t). In the same spirit as above 
we now look for its internal rate of interest, i.e. the constant value of the short 
rate, which will give the market value of the coupon bond. 
Definition 20.9 The yield to maturity, y(t,T), of a &ed coupon bond at 
time t, with market price p, and payments Q at Ti for i = 1,. . . , n, is defined as 
the value of y which solves the equation 
An important concept in bond portfolio management is the "Macaulay 
duration
7'. Without loss of generality we may assume that t = 0. 

314 
BONDS AND INTEREST RATES 
Definition 20.10 For the @ed coupon bond above, with price p at t = 0, and 
yield to maturity y, the duration, D, is defined as 
The duration is thus a weighted average of the coupon dates of the bond, 
where the discounted values of the coupon payments are used as weights, and it 
will in a sense provide you with the "mean time to coupon payment". As such it 
is an important concept, and it also acts a measure of the sensitivity of the bond 
price w.r.t. changes in the yield. This is shown by the following obvious result. 
Proposition 20.11 With notation as above we have 
Thus we see that duration is essentially for bonds (w.r.t. yield) what delta (see 
Section 9.2) is for derivatives (w.r.t. the underlying price). The bond equivalent 
of the gamma is convexity, which is defined as 
20.4 Exercises 
Exercise 20.1 A forward rate agreement (FRA) is a contract, by convention 
entered into at t = 0, where the parties (a lender and a borrower) agree to let 
a certain interest rate, R*, act on a prespecified principal, K, over some future 
period [S, TI. Assuming that the interest rate is continuously compounded, the 
cash flow to the lender is, by definition, given as follows: 
At time S: -K. 
At time T: ~ e ~ * ( ~ - ~ ) .  
The cash flow to the borrower is of course the negative of that to the lender. 
(a) Compute for any time t < S, the value, II (t), of the cash flow above in 
terms of zero coupon bond prices. 
(b) Show that in order for the value of the FRA to equal zero at t = 0, the 
rate R* has to equal the forward rate R(0; S, T) (compare this result to 
the discussion leading to the definition of forward rates). 
Exercise 20.2 Prove the first part of Proposition 20.5. 
Hint: Apply the It6 formula to the process log p(t, T), write this in integrated 
form and differentiate with respect to T. 
Exercise 20.3 Consider a coupon bond, starting at To, with face value K, 
coupon payments at TI, . . . , T, and a fixed coupon rate r. Determine the coupon 
rate r, such that the price of the bond, at To, equals its face value. 

NOTES 
315 
I 
Exercise 20.4 Derive the pricing formula (20.15) directly, by constructing a 
self-financing portfolio which replicates the cash flow of the floating rate bond. 
Exercise 20.5 Let {y(O, T); T 2 0) denote the zero coupon yield curve at 
t = 0. Assume that, apart from the zero coupon bonds, we also have exactly 
one fixed coupon bond for every maturity T. We make no particular assump 
tions about the coupon bonds, apart from the fact that all coupons are positive, 
and we denote the yield to maturity, again at time t = 0, for the coupon bond 
with maturity T, by yM (0, T). We now have three curves to consider: the for- 
ward rate curve f (0, T), the zero coupon yield curve y(0, T), and the coupon 
T). The object of this exercise is to see how these curves are 
~ Y ( O ,  T) 
f (0, T) = ~ ( 0 ,  
T) + T 7. 
(b) Assume that the zero coupon yield cuve is an increasing function of T 
Show that this implies the inequalities 
YM (0, T) 5 y(O, T) 5 f (0, T), VT, 
I 
iU 
(with the opposite inequalities holding if the zero coupon yield curve i! 
decreasing). Give a verbal economic explanation of the inequalities. 
1 Exercise 20.6 Prove Proposition 20.11. 
Exercise 20.7 Consider a consol bond, i.e. a bond which will forever pay on1 
unit of cash at t = 1,2,. . . . Suppose that the market yield y is constant for al 
(a) Compute the price, at t = 0, of the consol. 
(b) Derive a formula (in terms of an infinite series) for the duration of th 
' (c) Use (a) and Proposition 20.11 in order to compute an analytical formul 
for the duration. 
4 (d) Compute the convexity of the consol. 

J 
21 
SHORT RATE MODELS 
21.1 Generalities 
In this chapter, we turn to the problem of how to model an arbitrage free family 
of zero coupon bond price processes {p(., T); T > 0). 
Since, at least intuitively, the price, p(t,T), should in some sense depend 
upon the behavior of the short rate of interest over the interval [t, TI, a natural 
starting point is to give an a priori specification of the dynamics of the short rate 
of interest. This has in fact been the "classical" approach to interest rate theory, 
so let us model the short rate, under the objective probability measure P, as the 
solution of an SDE of the form 
The short rate of interest is the only object given a priori, so the only exogenously 
given asset is the money account, with price process B defined by the dynamics 
dB(t) = r(t)B(t) dt. 
(21.2) 
As usual we interpret this as a model of a bank with the stochastic short rate 
of interest r. The dynamics of B can then be interpreted as the dynamics of 
the value of a bank account. To be quite clear let us formulate the above as a 
formalized assumption. 
Assumption 21.1.1 We assume the existence of one exogenously given (locally 
risk free) asset. The price, B, of this asset has dynamics given by eqn (21.2), 
where the dynamics of r ,  under the objective probability measure P, are given by 
eqn (21.1). 
As in the previous chapter, we make an assumption to guarantee the existence 
of a sufficiently rich bond market. 
Assumption 21.1.2 We assume that there exists a market for zero coupon 
T-bonds for every value of T. 
We thus assume that our market contains all possible bonds (plus, of course, 
the risk free asset above). Consequently, it is a market containing an infinite 
number of assets, but we again stress the fact that only the risk free asset is 
exogenously given. In other words, in this model the risk free asset is considered 
as the underlying asset whereas all bonds are regarded as derivatives of the 
"underlying" short rate r. Our main goal is broadly to investigate the relationship 
which must hold in an arbitrage free market between the price processes of bonds 

Quest ion: 
Are bond prices uniquely determined 
by the P-dynamics of the short rate r? 
GENERALITIES 
317 
with diierent maturities. As a second step we also want to obtain arbitrage free 
prices for other interest rate derivatives such as bond options and interest rate 
swaps. 
Since we view bonds as interest rate derivatives it is natural to ask whether 
the bond prices are uniquely determined by the given T dynamics in (21.1) and 
the condition that the bond market shall be free of arbitrage. This question, and 
its answer, are fundamental. 
r x  
d 
R 
L 
For the reader who has studied Chapter 15, this negative result should be 
fairly obvious. The arguments below are parallel to those of Section 15.2, and 
the results are in fact special cases of the general results in Section 15.4. If 
you have already studied these sections you can thus browse quickly through 
the text until the term structure equation (21.2). In order to keep this part of 
the book self-contained, and since the discussion is so important, we will (with 
some apologies) give the full argument. 
Let us start by viewing the bond market in the light of the meta- 
theorem 8.3.1. We see that in the present situation the number M of exogenously 
given traded assets excluding the risk free asset equals zero. The number R of 
random sources on the other hand equals one (we have one driving Wiener pro- 
cess). From the meta-theorem we may thus expect that the exogenously given 
market is arbitrage free but not complete. The lack of completeness is quite clear: 
since the only exogenously given asset is the risk free one we have no possibility 
of forming interesting portfolios. The only thing we can do on the a priori given 
market is simply to invest our initial capital in the bank and then sit down and 
wait while the portfolio value evolves according to the dynamics (21.2). It is 
thus impossible to replicate an interesting derivative, even such a simple one as 
a T-bond. 
Another way of seeing this problem appears if we try to price a certain T-bond 
using the technique used in Section 7.3. In order to imitate the old argument we 
would assume that the price of a certain bond is of the form F(t, r(t)). Then we 
Answer: 
Na!1 

,,SHORT RATE MODELS 
would like to form a risk free portfolio based on this bond and on the underlying 
asset. The rate of return of this risk free portfolio would then, by an arbitrage 
argument, have to equal the short rate of interest, thus giving us some kind 
of equation for the determination of the function F. Now, in the Black-Scholes 
model the underlying asset was the stock S, and at first glance this would corres- 
pond to r in the present situation. Here, however, we have the major difference 
between the Black-Scholes model and our present model. The short rate of 
interest r is not the price of a traded asset, i.e. there is no asset on the market 
whose price process is given by r. Thus it is meaningless to form a portfolio 
"based on r". Since there sometimes is a lot of confusion on this point let us 
elaborate somewhat. We observe then that the English word "price" can be used 
in two related but different ways. 
The first way occurs in everyday (informal) speech, and in this context it 
is not unusual (or unreasonable) to say that the short rate of interest reflects 
the price of borrowing money in the bank. In particular we often say that it is 
expensive to borrow money if the rate of interest is high, and cheap when the 
rate of interest is low. 
The second (formalized) use of the word "price" occurs when we are dealing 
with price systems in the context of, for example, general equilibrium theory. In 
this setting the word "price" has a much more precise and technical meaning than 
in everyday language. Firstly a price is now measured in a unit like, say, pounds 
sterling. The short rate of interest, on the contrary, is measured in the unit 
(time)-', though for numerical reasons it is sometimes given as a precentage. 
Secondly the price of an asset tells you how many pounds sterling you have to 
pay for one unit of the asset in question. If, say, the price of ACME INC. stock 
is 230 pounds this means that if you pay 230 pounds then you will obtain one 
share in ACME INC. If, on the other hand, the short rate of interest is 11%, 
this does not mean that you can pay 11 (units of what?) in order to obtain one 
unit of some asset (what would that be?). 
This does not at all imply that the everyday interpretation of the interest rate 
as "the price of borrowing money" is wrong. This aspect of the short rate already 
appears in fact in the equation, dB = r B  dt, for the money account, where it is 
obvious that if r is high, then our debt to the bank grows at a high rate. 
When we use the word "price" in this text it is exclusively as in the second 
formalized meaning above, and a sloppy usage will easily lead to nonsense and 
chaos. 
To sum up: 
The price of a particular bond will not be completely determined by the 
specification (21.1) of the r-dynamics and the requirement that the bond 
market is free of arbitrage. 
The reason for this fact is that arbitrage pricing is always a case of pricing 
a derivative in terms of the price of some underlying assets. In our market 
we do not have sufficiently many underlying assets. 

THE TERM STRUCTURE EQUATION 
319 
We thus fail to determine a unique price of a particular bond. Fortunately this 
(perhaps disappointing) fact does not mean that bond prices can take any form 
whatsoever. On the contrary we have the following basic intuition. 
Idea 21.1.1 
Prices of bonds with different maturities will have to satisfy certain 
internal consistency relations in order to avoid arbitrage possibilities 
on the bond market. 
If we take the price of one particular "benchmark" bond as given then 
the prices of all other bonds (with maturity prior to the benchmark) will 
, . 
be uniquely determined in terms of the price of the benchmark bond (and 
the r-dynamics). 
1 : This fact is in complete agreement with the metetheorem, since in the a priori 
given market consisting of one benchmark bond plus the risk free asset we will 
have R = M = 1 thus guaranteeing completeness. 
21.2 The Term Structure Equation 
To make the ideas presented in the previous section more concrete we now begin 
our formal treatment. 
Assumption 21.2.1 We assume that there is a market for T-bonds for every 
choice of Tand that the market is arbitrage free. We assume jbrthermore that, 
for every T ,  the price of a T-bond has the form 
where F is a smooth function of three real variables. 
Conceptually it is perhaps easiest to think of F as a function of only two 
variables, namely r and t, whereas T is regarded as a parameter. Sometimes we 
will therefore write F T(t, r )  instead of F(t, r; T). The main problem now is to 
find out what FT may look like on an arbitrage free market. 
Just as in the case of stock derivatives we have a simple boundary condition. 
At the time of maturity a T-bond is of course worth exactly 1 pound, so we have 
the relation 
F ( T , r ; T ) =  1, 
forallr. 
(21.4) 
Note that in the equation above the letter r denotes a real variable, while at 
the same time r is used as the name of the stochastic process for the short rate. 
To conform with our general notational principles we should really denote the 
stochastic process by a capital letter like R, and then denote an outcome of R 
by the letter r. Unfortunately the use of r as the name of the stochastic process 
seems to be so fixed that it cannot be changed. We will thus continue to use r 
as a name both for the process and for a generic outcome of the process. This is 
somewhat sloppy, but we hope that the meaning will be clear from the context. 
In order to implement the ideas above we will now form a portfolio consisting 
of bonds having different times of maturity. We thus fix two times of maturity S 

320 
SHORT RATE MODELS 
and T. From Assumption 21.2.1 and the It6 formula we get the following price 
dynamics for the T-bond, with corresponding equations for the S-bond. 
dFT = FTaT dt + FTnT dW, 
(21.5) 
where, with subindices r and t denoting partial derivatives, 
Denoting the relative portfolio by (us, uT) we have the following value dynamics 
for our portfolio. 
and inserting the differential from (21.5), as well as the corresponding equation 
for the S-bond, gives us, after some reshuffling of terms, 
Exactly as in Section 7.3 we now define our portfolio by the equations 
With this portfolio the dw-term in (21.9) will vanish, so the value dynamics 
reduce to 
dV = V { u T a ~  
+ u s a s )  dt. 
(21.12) 
The system (21.10)-(21.11) can easily be solved as 
and substituting this into (21.12) gives us 
Using Proposition 7.6, the assumption of no arbitrage now implies that this 
portfolio must have a rate of return equal to the short rate of interest. Thus we 
have the condition 
aSaT - aTaS = r(t), for all t, with probability 1, 
UT - US 

or, written differently, 
The interesting fact about eqn (21.17) is that on the left-hand side we have a 
stochastic process which does not depend on the choice of T, whereas on the 
right-hand side we have a process which does not depend on the choice of S. 
The common quotient will thus not depend on the choice of either T or S, so we 
have thus proved the following fundamental result. 
Proposition 21.1 Assume that the bond market is free of arbitrage. Then there 
exzsts a process X such that the relation 
holds for all t and for every choice of maturity time T. 
Observe that the process X is universal in the sense that it is the same X 
which occurs on the right-hand side of (21.18) regardless of the choice of T. Let 
us now take a somewhat closer look at this process. 
In the numerator of (21.18) we have the term aT (t) - r(t). By eqn (21.5), 
aT(t) is the local rate of return on the T-bond, whereas r is the rate of return 
of the risk free asset. The difference crT(t) - r(t) is thus the risk premium of 
the T-bond. It measures the excess rate of return for the risky T-bond over the 
riskless rate of return which is required by the market in order to avoid arbitrage 
possibilities. In the denominator of (21.18) we have uT (t), i.e. the local volatility 
of the T-bond. 
Thus we see that the process X has the dimension "risk premium per unit of 
volatility". The process X is known as the market price of risk, and we can 
paraphrase Proposition 21.1 by the following slogan: 
In a no arbitrage market all bonds will, regardless of maturity 
time, have the same market price of risk. 
Before we move on, a brief word of warning: the name "market price of risk" is 
in some sense rather appealing and reasonable, but it is important to realize that 
the market price of risk is not a price in the technical (general equilibrium) sense 
reserved for the word "price" in the rest of this text. We do not measure X in 
SEK, and X is not something which we pay in order to obtain some commodity. 
Thus the usage of the word "price" in this context is that of informal everyday 
language, and one should be careful not to overinterpret the words "market 
price of risk" by assuming that properties holding for price processes in general 
equilibrium theory also automatically hold for the process A. 
We may obtain even more information from eqn (21.18) by inserting our 
earlier formulas (21.6)-(21.7) for a~ and UT. After some manipulation we then 
obtain one of the most important equations in the theory of interest rates-the 

322 
SHORT RATE MODELS 
so called "term structure equation". Since this equation is so fundamental we 
formulate it as a separate result. 
Proposition 21.2 (Term structure equation) In an arbitrage free bond 
market, FT will satisfy the term structure equation 
F: 
+ { p -  Xu) F: 
+ i u 2 F 2  -rFT =0, 
F ~ ( T , ~ )  
= 1. 
The term structure equation is obviously closely related to the Black-Scholes 
i 
equation, but it is a more complicated object due to the appearance of the 
market price of risk A. It follows from eqns (21.6), (21.7), and (21.18) that X is 
I 
of the form X = A(t, r) so the term structure equation is a standard PDE, but 
the problem is that X is not determined within the model. In order to be able 
to solve the term structure equation we must specify X exogenously just as we 
have to specify p and a. 
Despite this problem it is not hard to obtain a Feynman-KaE representation 
of FT. This is done by fixing (t, r) and then using the process 
exp { - ls 
r(u)du) ~ ~ ( s ,  
r(s)). 
If we apply the It6 formula to (21.20) and use the fact that F~ satisfies the term 
structure equation then, by using exactly the same technique as in Section 5.5, 
we obtain the following stochastic representation formula. 
Proposition 21.3 (Risk neutral valuation) Bond prices are given by the 
formula p(t, T) = F(t, r(t); T) where 
Here the martingale measure Q and the subscripts t, r denote that the expectation 
shall be taken given the following dynamics for the short rate: 
I 
, 
The formula (21.21) has the usual natural economic interpretation, which is 
most easily seen if we write it as 
~ 
We see that the value of a T-bond at time t is given as the expected value of the 
I 
final payoff of one pound, discounted to present value. The deflator used is the 
T 
natural one, namely exp{- S, r(s) ds), but we observe that the expectation is 

THE TERM STRUCTURE EQUATION 
323 
not to be taken using the underlying objective probability measure P. Instead we 
must, as usual, use the martingale measure Q and we see that we have different 
martingale measures for different choices of A. 
The main difference between the present situation and the Black-Scholes 
setting is that in the Black-Scholes model the martingale measure is uniquely 
determined. It can be shown (see Chapters 13 and 15) that the uniqueness of the 
martingale measure is due to the fact that the Black-Scholes model is complete. 
In the present case our exogenously given market is not complete, so bond prices 
will not be uniquely determined by the given (P-)dynamics of the short rate r. 
To express this fact more precisely, the various bond prices will be determined 
partly by the P-dynamics of the short rate of interest, and partly by market 
forces. The fact that there are different possible choices of X simply means that 
there are different conceivable bond markets all of which are consistent with the 
given r-dynamics. Precisely which set of bond price processes will be realized by 
an actual market will depend on the relations between supply and demand for 
bonds in this particular market, and these factors are in their turn determined by 
such things as the forms of risk aversion possessed by the various agents on the 
market. In particular this means that if we make an ad hoc choice of X (e.g. such 
as X = 0) then we have implicitly made an assumption concerning the aggregate 
risk aversion on the market. 
We can also turn the argument around and say that when the market has 
determined the dynamics of one bond price process, say with maturity T, then 
the market has indirectly specified X by eqn (21.18). When X is thus deter- 
mined, all other bond prices will be determined by the term structure equation. 
Expressed in another way: all bond prices will be determined in terms of the 
basic T-bond and the short rate of interest. Again we see that arbitrage pricing 
always is a case of determining prices of derivatives in terms of some a priori 
given price processes. 
There remains one important and natural question, namely how we ought 
to choose X in a concrete case. This question will be treated in some detail, in 
Section 22.2, and the moral is that we must go to the actual market and, by 
using market data, infer the market's choice of A. 
The bonds treated above are of course contingent claims of a particularly 
simple type; they are deterministic. Let us close this section by looking at a 
more general type of contingent T-claim of the form 
x = *(r(T)), 
(21.25) 
where cP is some real valued function. Using the same type of arguments as above 
it is easy to see that we have the following result. 
Proposition 21.4 (General term structure equation) Let X be a contin- 
gent T-claim of the form X = cP(r(T)). In an arbitrage free market the price 
II(t; cP) will be given as 
w ;  @I = F(t, r(t)), 
(21.26) 

324 
SHORT RATE MODELS 
where F solves the boundary value problem 
Furthermore F has the stochastic representation 
where the martingale measure Q and the subscripts t, r denote that the expecta- 
tion shall be taken using the following dynamics: 
dr(s) = { p  - Xu)ds + crdW(s), 
(21.29) 
r(t) = r. 
(21.30) 
21.3 Exercises 
Exercise 21.1 We take as given an interest rate model with the following 
P-dynamics for the short rate. 
Now consider a T-claim of the form X = @(r(T)) with corresponding price 
process II (t). 
(a) Show that, under any martingale measure Q, the price process II (t) has 
a local rate of return equal to the short rate of interest. In other words, 
show that the stochastic differential of II (t) is of the form 
dII (t) = r (t)II (t) dt + anlI (t) dW(t). 
(b) Show that the normalized price process 
is a Q-martingale. 
Exercise 21.2 The object of this exercise is to connect the forward rates defined 
in Chapter 20 to the framework above. 
(a) Assuming that we are allowed to differentiate under the expectation sign, 
show that 
E:~,,, [.(TI exp {- JtT r(s) ds}] 
f (t, T )  = 
(b) Check that indeed r (t) = f (t , t) . 

NOTES 
325 
Exercise 21.3 (Swap a fixed rate vs. a short rate) Consider the following 
version of an interest rate swap. The contract is made between two parties, A 
and B, and the payments are made as follows: 
A (hypothetically) invests the principal amount K at time 0 and lets it 
grow at a fixed rate of interest R (to be determined below) over the time 
interval [0, TI. 
At time T the principal will have grown to KA SEK. A will then subtract 
the principal amount and pay the surplus K - KA to B (at time T). 
B (hypothetically) invests the principal at the stochastic short rate of 
interest over the interval [0, TI. 
At time T the principal will have grown to KB SEK. B will then subtract 
the principal amount and pay the surplus K - Kg to A (at time T). 
The swap rate for this contract is now defined as the value, R, of the fixed rate 
which gives this contract the value zero at t = 0. Your task is to compute the 
swap rate. 
Exercise 21.4 (Forward contract) Consider a model with a stochastic rate 
of interest. Fix a T-claim X of the form X = @(r(T)), 
and fix a point in time t, 
where t < T. From Proposition 21.4 we can in principle compute the arbitrage 
free price for X if we pay at time t. We may also consider a forward contract 
(see Section 7.6.1) on X contracted at t. This contract works as follows, where 
we assume that you are the buyer of the contract. 
At time T you obtain the amount X SEK. 
At time T you pay the amount K SEK. 
The amount K is determined at t. 
The forward price for X contracted at t is defined as the value of K which 
gives the entire contract the value zero at time t. Give a formula for the forward 
price. 
21.4 Notes 
The exposition in this chapter is standard. For further information, see the notes 
at the end of the next chapter. 

MARTINGALE MODELS FOR THE SHORT RATE 
22.1 &dynamics 
Let us again study an interest rate model where the P-dynamics of the short 
rate of interest are given by 
As we saw in the previous chapter, the term structure (i.e. the family of bond 
price processes) will, together with all other derivatives, be completely determ- 
ined by the general term structure equation 
as soon as we have specified the following objects: 
a The drift term p. 
a The diffusion term a. 
a The market price of risk A. 
Consider for a moment a to be given a priori. Then it is clear from (22.2) that 
it is irrelevant exactly how we specify p and X per se. The object, apart from u, 
that really determines the term structure (and all other derivatives) is the term 
p - Xu in eqn (22.2). Now, from Proposition 21.4 we recall that the term p - Xu is 
precisely the drift term of the short rate of interest under the martingale measure 
Q. This fact is so important that we stress it again. 
Result 22.1.1 The term structure, as well as the prices of all other interest rate 
derivatives, are completely determined by specifying the r-dynamics under the 
martingale measure Q. 
Instead of specifying p and X under the objective probability measure P 
we will henceforth specify the dynamics of the short rate r directly under the 
martingale meaure Q. This procedure is known as martingale modeling, and 
the typical assumption will thus be that r under Q has dynamics given by 
where p and a are given functions. From now on the letter p will thus always 
denote the drift term of the short rate of interest under the martingale measure Q. 

INVERSION OF THE YIELD CURVE 
327 
In the literature there are a large number of proposals on how to specify 
the Q-dynamics for r. We present a (far from complete) list of the most popular 
models. If a parameter is time dependent this is written out explicitly. Otherwise 
all parameters are constant. 
1. VasiEek 
dr=(b-ar)dt+adW, 
(a>O), 
(22.4) 
2. Cox-Ingersoll-Ross (CIR) 
3. Dothan 
dr = ardt +urdW, 
4. Black-Derman-Toy 
5. Ho-Lee 
dr = B(t)dt + adW, 
(22.8) 
' 6. Hull-White (extended VasiEek) 
I 
dr = (8(t) - a(t)r) dt + u(t) dW, 
(a(t) > O), 
(22.9) 
7. Hull-White (extended CIR) 
22.2 Inversion of the Yield Curve 
Let us now address the question of how we will estimate the various model 
parameters in the martingale models above. To take a specific case, assume 
that we have decided to use the VasiEek model. Then we have to get values for 
a, b, and a in some way, and a natural procedure would be to look in some 
textbook dealing with parameter estimation for SDEs. This procedure, however, 
is unfortunately completely nonsensical and the reason is as follows. 
We have chosen to model our r-process by giving the Q-dynamics, which 
means that a, b, and a are the parameters which hold under the martingale 
measure Q. When we make observations in the real world we are not observing r 
under the martingale measure Q, but under the objective measure P. This means 
that if we apply standard statistical procedures to our observed data we will not 
get our Q-parameters. What we get instead is pure nonsense. 
This looks extremely disturbing but the situation is not hopeless. It is in fact 
possible to show that the diffusion term is the same under P and under Q, so "in 
principle" it may be possible to estimate diffusion parameters using P-data. (The 
reader familiar with martingale theory will at this point recall that a Girsanov 
transformation will only affect the drift term of a diffusion but not the diffusion 
term.) 

328 
MARTINGALE MODELS FOR THE SHORT RATE 
When it comes to the estimation of parameters affecting the drift term of r 
we have to use completely different methods. 
From Section 15.6 we recall the following moral: 
Who chooses the martingale measure? 
The market! 
Thus, in order to obtain information about the Q-drift parameters we have 
to collect price information from the market, and the typical approach is that 
of inverting the yield curve which works as follows: (See the more detailed 
discussion in Section 15.6.) 
Choose a particular model involving one or several parameters. Let us 
denote the entire parameter vector by a. Thus we write the r-dynamics 
(under Q) as 
Solve, for every conceivable time of maturity T, the term structure equation 
In this way we have computed the theoretical term structure as 
p(t, T; a),= FT(t, r; a). 
Note that the form of the term structure will depend upon our choice of 
parameter vector. We have not made this choice yet. 
Collect price data from the bond market. In particular we may today (i.e. 
at t = 0) observe p(0, T) for all values of T. Denote this empirical term 
structure by {p*(O, T); T 2 0). 
Now choose the parameter vector a in such a way that the theoretical curve 
{p(O, T; a); T 2 0) fits the empirical curve {p*(O, T); T 2 0) as well as 
possible (according to some objective function). This gives us our estimated 
parameter vector a*. 

AFFINE TERM STRUCTURES 
329 
Insert a* into p and a. Now we have pinned down exactly which martingale 
measure we are working with. Let us denote the result of inserting a* into 
p and a by p* and a* respectively. 
We have now pinned down our martingale measure Q, and we can go on 
to compute prices of interest rate derivatives, like, say, X = I'(r(T)). The 
price process is then given by Il(t; l?) = G(t, r(t)) where G solves the term 
structure equation 
If the above program is to be carried out within reasonable time limits it is 
of course of great importance that the PDEs involved are easy to solve. It turns 
out that some of the models above are much easier to deal with analytically than 
the others, and this leads us to the subject of so called afFine term structures. 
22.3 Affine Term Structures 
22.3.1 Definition and Existence 
Definition 22.1 If the term structure {p(t,T); 0 5 t < T, T > 0) has the form 
where F has the form 
and where A and B are deterministic functions, then the model is said to possess 
an affine term structure (ATS). 
The functions A and B above are functions of the two real variables t and T, 
[ 
but conceptually it is easier to think of A and B as being functions oft, while T 
I serves as a parameter. It turns out that the existence of an d n e  term structure 
is extremely pleasing from an analytical and a computational point of view, so 
it is of considerable interest to understand when such a structure appears. In 
particular we would like to answer the following question: 
I 
For which choices of p and a in the Q-dynamics for r do we get an affine 
term structure? 
We will try to give at least a partial answer to this question, and we start by 
investigating some of the implications of an d n e  term structure. Assume then 
that we have the Q-dynamics 
and assume that this model actually possesses an ATS. In other words we assume 
that the bond prices have the form (22.15) above. Using (22.15) we may easily 

330 
MARTINGALE MODELS FOR THE SHORT RATE 
compute the various partial derivatives of F, and since F must solve the term 
structure equation (21.19), we thus obtain 
At(t,T) - (1 + Bt(t,T))r - p(t,r)B(t,T) + ;a2(t,r)B2(t,~) 
= 0. 
(22.17) 
' 
I 
The boundary value F(T, r; T) E 1 implies 
'I, 
Equation (22.17) gives us the relations which must hold between A, B, p, and a 
in order for an ATS to exist, and for a certain choice of p and a there may or may 
not exist functions A and B such that (22.17) is satisfied. Our immediate task is 
thus to give conditions on p and a which guarantee the existence of functions A 
and B solving (22.17). Generally speaking this is a fairly complex question, but 
we may give a very nice partial answer. We observe that if p and a2 are both 
affine (i.e. linear plus a constant) functions of r, with possibly time dependent 
coefficients, then eqn (22.17) becomes a separable differential equation for the 
unknown functions A and B. 
Assume thus that p and a have the form 
~ 
Then, after collecting terms, (22.17) transforms into 
This equation holds for all t, T, and r, so let us consider it for a fixed choice of 
T and t. Since the equation holds for all values of r the coefficient of r must be 
1 
equal to zero. Thus we have the equation 
B ~ ( ~ , T )  
+ a ( t ) ~ ( t , ~ )  
- ; . y ( t ) ~ 2 ( t , ~ )  
= -1: 
(22.21) 
Since the r-term in (22.20) is zero we see that the other term must also vanish, 
giving us the equation 
A t ( t , ~ )  
= p ( t ) ~ ( t , ~ )  
- ; b ( t ) ~ ~ ( t , ~ ) .  
(22.22) 
We may thus formulate our main result. 

AFFINE TERM STRUCTURES 
331 
Proposition 22.2 (Affine term structure) Assume that p and a are of 
~ ( t ,  
r) = 4 t h  + P(t), 
(22.23) 
u(t,r) = J-. 
Then the model admits an ATS of the form (22.15), where A and B satisfy the 
B&T) + (Y(~)B(~,T) 
- ; $ t ) ~ ~ ( t , ~ )  
= -1, 
(22.24) 
B(T, T) = 0. 
At@, T) = P(t)B(t, T) - ;6(t)B2(t, TI, 
(22.25) 
We note that eqn (22.24) is a Ricatti equation for the determination of B which 
does not involve A. Having solved eqn (22.24) we may then insert the solution 
B into eqn (22.25) and simply integrate in order to obtain A. 
An interesting question is if it is only for an affine choice of p and o2 that we 
get an ATS. This is not generally the case, but it can fairly easily be shown that 
if we demand that p and u2 are time independent, then a necessary condition 
for the existence of an ATS is that p and a2 are atline. Looking at the list of 
models in the previous section we see that all models except the Dothan and the 
Black-Derman-Toy models have an ATS. 
22.3.2 A Probabilistic Discussion 
There are good probabilistic reasons why some of the models in our list are 
easier to handle than others. We see that the models of VasiEek, Ho-Lee and 
Hull-White (extended VasiEek) all describe the short rate using a linear SDE. 
Such SDEs are easy to solve and the corresponding r-processes can be shown to 
be normally distributed. Now, bond prices are given by expressions like 
(22.26) 
and the normal property of r is inherited by the integral 
r(s) ds (an integral 
is just a sum). Thus we see that the computation of bond prices for a model with 
a normally distributed short rate boils down to the easy problem of computing 
the expected value of a log-normal stochastic variable. This purely probabilistic 
program can in fact be carried out for all the linear models above (the interested 
reader is invited to do this), but it turns out that from a computational point of 
view it is easier to solve the system of equations (22.24)-(22.25). 
In contrast with the linear models above, consider for a moment the Dothan 
model. This model for the short rate is the same as the Black-Scholes model for 
the underlying stock, so one is easily led to believe that computationally this 

I 
332 
MARTINGALE MODELS FOR THE SHORT RATE 
is the nicest model conceivable. This is, however, not the case. For the Dothan 
model the short rate will be log-normally distributed, which means that in order 
to compute band prices we are faced with determining the distribution of an 
integral fl r(s) ds of log-normal stochastic variables. It is, however, a sad fact 
that a sum (or an integral) of log-normally distributed variables is a particularly 
I 
nasty object, so this model leads to great computational problems. It also has 
the unreasonable property that the expected value of the money account equals 
plus infinity. 
I 
As for the Cox-Ingersoll-Ross model and the Hull-White extension, these 
i 
models for the short rate are roughly obtained by taking the square of the solution 
of a linear SDE, and can thus be handled analytically (see the exercises for a 
simplified example). They are, however, quite a bit messier to deal with than 
the normally distributed models. See the notes. 
From a computational point of view there is thus a lot to be said in favor of a 
linear SDE describing the short rate. The price we have to pay for these models 
is again the Gaussian property. Since the short rate will be normally distributed 
this means that for every t there is a positive probability that r(t) is negative, 
and this is unreasonable from an economic point of view. For the Dothan model 
on the other hand, the short rate is log-normal and thus positive with probabil- 
ity 1. It is also possible to show that the Cox-Ingersoll-Ross model will produce 
I 
l 
a strictly positive short rate process. See Rogers (1995) for a discussion on these 
problems. 
We end this section with a comment on the procedure of calibrating the model 
to data described in the previous section. If we want a complete fit between the 
theoretical and the observed bond prices this calibration procedure is formally 
that of solving the system of equations 
1 
p(0, T; a) = p*(O, T) for all T > 0. 
(22.27) 
I 
We observe that this is an infinite dimensional system of equations (one equation 
I 
for each T) with o as the unknown, so if we work with a model containing a 
R 
finite parameter vector a (like the VasiEek model) there is no hope of obtaining a 
perfect fit. Now, one of the main goals of interest rate theory is to compute prices 
of various derivatives, like, for example, bond options, and it is well known that 
the price of a derivative can be very sensitive with respect to the price of the 
underlying asset. For bond options the underlying asset is a bond, and it is thus 
disturbing if we have a model for derivative pricing which is not even able to 
~ 
correctly price the underlying asset. 
This leads to a natural demand for models which can be made to fit the 
observed bond data completely, and this is the reason why the Hull-White model 
has become so popular. In this model (and related ones), we introduce an infin- 
I 
ite dimensional parameter vector a by letting some or all parameters be time 
dependent. Whether it is possible to actually solve the system (22.27) for a con- 
crete model such as the Hull-White extension of the VasiEek model, and how 

SOME STANDARD MODELS 
333 
this is to be done in detail, is of course not clear a priori but has to be dealt 
with in a deeper study. We carry out this study for the Hull-White model in the 
next section. 
It should, however, be noted that the introduction of an infinite parameter, in 
order to fit the entire initial term structure, has its dangers in terms of numerical 
instability of the parameter estimates. 
There is also a completely different approach to the problem of obtaining a 
perfect fit between today's theoretical bond prices and today's observed bond 
prices. This is the Heath-Jarrow-Morton approach which roughly takes the 
observed term structure as an initial condition for the forward rate curve, thus 
automatically obtaining a perfect fit. This model will be studied in the next 
chapter. 
22.4 Some Standard Models 
In this section we will apply the ATS theory above, in order to study the most 
common afFine one factor models. 
22.4.1 The VasiEek Model 
To illustrate the technique we now compute the term structure for the VasiEek 
model 
dr = (b-ar)dt+adW. 
(22.28) 
Before starting the computations we note that this model has the property of 
being mean reverting (under Q) in the sense that it will tend to revert to the 
mean level bla. Equations (22.24)-(22.25) become 
Equation (22.29) is, for each fixed T, a simple linear ODE in the t-variable. It 
can easily be solved as 
Integrating eqn (22.30) we obtain 
and, substituting the expression for B above, we obtain the following result. 

334 
MARTINGALE MODELS FOR THE SHORT RATE 
Proposition 22.3 (The VasiEek t e r m  structure) In the VasiEek model, bond 
prices are given by 
p(t, T )  = eA(t,T)-B(t,T)'(t), 
where 
A(t, T )  = {B(t, T )  - 2' + t )  (ab - ia2) - a2B2(t, T )  
a2 
4a 
For the VasiEek model, there is also an explicit formula for European bond 
options. See Proposition 22.9. 
22.4.2 
The Ho-Lee Model 
For the Ho-Lee model the ATS equations become 
At(t,T) = @(t)B(t,T) - ; U ~ B ~ ( ~ , T ) ,  
A(T, T )  = 0. 
These are easily solved as 
It now remains to choose 8 such that the theoretical bond prices, at t = 0, fit 
the observed initial term structure {p*(O,T); T 2 0). We thus want to find 8 
such that p(0, T )  = p*(O, T )  for all T 2 0. This is left as an exercise, and the 
solution is given by 
@(t) = af^ (0, t) + 
aT 
where f*(O, t) denotes the observed forward rates. Plugging this expression into 
the ATS gives us the following bond prices. 
Proposition 22.4 ( T h e  Ho-Lee t e r m  structure) For the Ho-Lee model, the 
bond prices are given by 
'i 
{ 
u2 
p(t, T )  = 
exp (T - t ) f * ( ~ ,  
t) - 5 t ( ~  - t12 - (T - t)r(t) . 
P*(O, t) 
,., . t 
I 
For completeness we also give the pricing formula for a European call on an 
underlying bond. We will not derive this result by solving the pricing PDE (this 

SOME STANDARD MODELS 
335 
is in fact very hard), but instead we refer the reader to Chapter 24 where we will 
present a rather general option pricing formula (Proposition 24.11). It is then an 
easy exercise to obtain the result below as a special case. 
, Proposition 22.5 ( B o n d  options) For the Ho-Lee model, the price at t, of a 
i 
European call option with strike price K and exercise date T ,  on an underlying 
S-bond, we have the following p ~ c i n g  formula: 
1 
c(t, T, K, S )  = p(t, S ) N ( d )  - p(t, T )  K . N(d - a,), 
(22.33) 
C 
where 
22.4.3 The CIR Model 
The CIR model is much more difficult to handle than the VasiEek model, since 
1 we have to solve a Riccati equation. We cite the following result. 
Proposition 22.6 (The CIR t e r m  structure) The term structure for the 
CIR model is given by 
I where 
j and 
I 
It is possible to obtain closed form expressions for European call options on 
zero coupon bonds within the CIR framework. Since these formulas are rather 
complicated, we refer the reader to Cox-Ingersoll-Ross (19856). 
I 22.4.4 
The Hull-White Model 
1 In this section we will make a fairly detailed study of a simplified version of the 
i Hull-White extension of the VasiEek model. The Q-dynamics of the short rate 
are given by 
dr = {Q(t) - ar) dt + u d W ( t ) ,  
(22.36) 
where a and o are constants while 8 is a deterministic function of time. In this 
model we typically choose a and a in order to obtain a nice volatility structure 

336 
MARTINGALE MODELS FOR THE SHORT RATE 
whereas 8 is chosen in order to fit the theoretical bond prices {p(O, T); T > 0) 
to the observed curve {p*(O, T); T > 0). 
We have an d n e  structure so by Proposition 22.2 bond prices are given by 
where A and B solve 
The solutions to these equations are given by 
Now we want to fit the theoretical prices above to the observed prices and it 
is convenient to do this using the forward rates. Since there is a one-to-one 
correspondence (see Lemma 20.4) between forward rates and bond prices, we 
may just as well fit the theoretical forward rate curve {f (0, T); T > 0) to the 
observed curve { f * (0, T) ; T > 0) , where of course f * is defined by f* (t, T) = 
-(d logp*(t, T))/aT. In any affine model the forward rates are given by 
which, after inserting (22.40)-(22.41), becomes 
Given an observed forward rate structure f * our problem is to find a function 8 
which solves the equation 
u2 
f*(O,T) = e-aTr(~) + 
e-a(T-s)8(s)ds - - 
(1 - e-aT)2, VT > 0. 
2a2 
(22.44) 
One way of solving (22.44) is to write it as 

SOME STANDARD MODELS 
where x and g are defined by 
/ We now have 
i 
SO we have in fact proved the following result. 
Lemma 22.7 Fix an arbitrary bond curve W(O, T); T > 0), subject only to the 
condition that p*(O, T) is twice differentiable w.r.t. T. Choosing 8 according to 
(22.47) will then produce a term structure {p(O, T); T > 0) such that p(0, T) = 
p*(O, T) for all T > 0. 
1 By choosing C3 according to (22.47) we have, for a fixed choice of a and u, 
1 determined our martingale measure. Now we would like to compute the theoret- 
ical bond prices under this martingale measure, and in order to do this we have 
I to substitute our choice of 8 into eqn (22.41). Then we perform the integration 
1 and substitute the result as well as eqn (22.40) into eqn (22.37). This leads to 
1 some exceedingly boring calculations which (of course) are left to the reader. 
' The result is as follows. 
Proposition 22.8 (The Hull-White term structure) Consider the Hull- 
White model with a and a jixed. Having inverted the yield curve by choosing O 
according to (22.47) we obtain the bond prices as 
? 
where B is given by (22.40). 
We end this section by giving, for the Hull-White, as well as for the VasiEek 
model, the pricing formula for a European call option with time of maturity T 
and strike price K on an S-bond, where of course T < S. We denote this price 
by c(t, T, K, 
S). At the present stage the reader is not encouraged to derive the 
formula below. In Chapter 24 we will instead present a technique which will 
greatly simplify computations of this kind, and the formula will be derived with 
relative ease in Section 24.6 (see Proposition 24.13). Note that the bond prices 
p(t, T) and p(t, S) below do not have to be computed at time t, since they can 
be observed directly on the market. 

338 
MARTINGALE MODELS FOR THE SHORT RATE 
Proposition 22.9 (Bond options) Using notation as above we have, both for 
the Hull-White and the VasiEek models, the following bond option formula: 
where 
22.5 Exercises 
Exercise 22.1 Consider the VasiEek model, where we always assume that a > 0. 
(a) Solve the VasiEek SDE explicitly, and determine the distribution of r(t). 
Hint: The distribution is Gaussian (why?), so it is enough to compute 
the expected value and the variance. 
(b) As t -, oo, the distribution of r(t) tends to a limiting distribution. Show 
that this is the Gaussian distribution N[b/a, u/$%]. Thus we see that, 
in the limit, r will indeed oscillate around its mean reversion level bla. 
(c) Now assume that r(0) is a stochastic variable, independent of the Wiener 
process W, and by definition having the Gaussian distribution obtained 
in (b). Show that this implies that r(t) has the limit distribution in (b), 
for all values oft. Thus we have found the stationary distribution for the 
VasiEek model. 
(d) Check that the density function of the limit distribution solves the time 
invariant Fokker-Planck equation, i.e. the Fokker-Planck equation with 
the (dl%)-term equal to zero. 
Exercise 22.2 Show directly that the VasiEek model has an &ne term struc- 
ture without using the methodology of Proposition 22.2. Instead use the 
characterization of p(t, T) as an expected value, insert the solution of the SDE 
for r, and look at the structure obtained. 
Exercise 22.3 Try to carry out the program outlined above for the Dothan 
model and convince yourself that you will only get a mess. 
Exercise 22.4 Show that for the Dothan model you have EQ [B(t)] = oo. 
Exercise 22.5 Consider the Ho-Lee model 
Assume that the observed bond prices at t = 0 are given by {p*(O, T); t 2 0). 
Assume furthermore that the constant cr is given. Show that this model can be 
fitted exactly to today's observed bond prices with 8 as 

NOTES 
339 
where f* denotes the observed forward rates. (The observed bond price curve is 
assumed to be smooth.) 
Hint: Use the afFine term structure, and fit forward rates rather than bond 
prices (this is logically equivalent). 
Exercise 22.6 Use the result of the previous exercise in order to derive the 
bond price formula in Proposition 22.4. 
Exercise 22.7 It is often considered reasonable to demand that a forward rate 
curve always has an horizontal asymptote, i.e. that limT,, 
f (t, T) exists for all t. 
(The limit will obviously depend upon t and ~ ( t ) . )  
The object of this exercise is 
to show that the Ho-Lee model is not consistent with such a demand. 
(a) Compute the explicit formula for the forward rate curve f (t, T) for the 
Ho-Lee model (fitted to the initial term structure). 
(b) Now assume that the initial term structure indeed has a horizontal asymp 
tote, i.e. that limT,, 
f*(O, T) exists. Show that this property is not 
respected by the Ho-Lee model, by fixing an arbitrary time t, and showing 
that f (t, T) will be asymptotically linear in T. 
Exercise 22.8 The object of this exercise is to indicate why the CIR model is 
connected to squares of linear diffusions. Let Y be given as the solution to the 
following SDE: 
Define the process Z by Z(t) = m. 
It turns out that Z satisfies a stochastic 
differential equation. Which? 
22.6 Notes 
Basic papers on short rate models are VasiEek (1977), Hull and White (1990), 
Ho and Lee (1986), Cox et al. (1985b), Dothan (1978), and Black et al. (1990). 
For extensions and notes on the afFine term structure theory, see Dufiie and Kan 
(1996). An extensive analysis of the linear quadratic structure of the CIR model 
can be found in Magshoodi (1996). The bond option formula for the VasiEek 
model was first derived by Jamshidian (1989). For examples of two-factor models 
see Brennan and Schwartz (1979, 1982), and Longstaff and Schwartz (1992). 
Rogers (1997) shows how it is possible to generate a wide class of short rate 
models by modeling the state price density directly under P and using resolvents. 
A completely different approach to interest rate theory is given in Platen (1996) 
where the short rate is derived as a consequence of an entropy related principle. 
See also Platen and Rebolledo (1995). For an overview of interest rate theory see 
Bjork (1997). 


## Forward Rate Models (HJM)

FORWARD RATE MODELS 
23.1 The Heath-Jarrow-Morton Framework 
Up to this point we have studied interest models where the short rate r is the only 
explanatory variable. The main advantages with such models are as follows: 
Specifying r as the solution of an SDE allows us to use Markov process 
theory, so we may work within a PDE framework. 
In particular it is often possible to obtain analytical formulas for bond 
prices and derivatives. 
The main drawbacks of short rate models are as follows: 
From an economic point of view it seems unreasonable to assume that the 
entire money market is governed by only one explanatory variable. 
It is hard to obtain a realistic volatility structure for the forward rates 
without introducing a very complicated short rate model. 
As the short rate model becomes more realistic, the inversion of the yield 
curve described above becomes increasingly more difficult. 
These, and other considerations, have led various authors to propose models 
which use more than one state variable. One obvious idea would, for example, 
be to present an a priori model for the short rate as well as for some long 
rate, and one could of course also model one or several intermediary interest 
rates. The method proposed by Heath-Jarrow-Morton (HJM) is at the far end 
of this spectrum-they choose the entire forward rate curve as their (infinite 
dimensional) state variable. 
We now turn to the specification of the HJM framework. We start by 
specifying everything under a given objective measure P. 
Assumption 23.1.1 We assume that, for every fied T > 0, the forward 
mte f(.,T) has a stochastic diflerential which under the objective measure P 
is given by 
where w is a (d-dimensional) P- Wiener process whereas a(., T) and u(., T) are 
adapted processes. 
Note that conceptually eqn (23.1) is one stochastic differential in the t-variable 
for each fixed choice of T. The index T thus only serves as a "mark" or "par& 
C 
meter" in order to indicate which maturity we are looking at. Also note that we 

THE HEATH-JARROW-MORTON FRAMEWORK 
341 
use the observed forward rated curve {f*(O, T); T 2 0) as the initial condition. 
This will automatically give us a perfect fit between observed and theoretical 
bond prices at t = 0, thus relieving us of the task of inverting the yield curve. 
Remark 23.1.1 It is important to observe that the HJM approach to interest 
rates is not a proposal of a specific model, like, for example, the VasiEek model. 
It is instead a framework to be used for analyzing interest rate models. Every 
short rate model can be equivalently formulated in forward rate terms, and for 
every forward rate model, the arbitrage free price of a contingent T-claim X will 
still be given by the pricing formula 
n(0; ,) 
= EQ [exp {- 1' r(.) ds} x] , 
where the short rate as usual is given by r(s) = f (s, 3). 
Suppose now that we have specified a ,  u and { f * (0, T) ; T L 0). Then we have 
specified the entire forward rate structure and thus, by the relation 
TI = exP {- iT 
f (t, s) ds} 7 
(23.3) 
we have in fact specified the entire term structure {p(t, T); T > 0, 0 5 t _< T). 
Since we have d sources of randomness (one for every Wiener process), and an 
infinite number of traded assets (one bond for each maturity T), we run a clear 
risk of having introduced arbitrage possibilities into the bond market. The first 
question we pose is thus very natural: How must the processes a and a be related 
in order that the induced system of bond prices admits no arbitrage possibilities? 
The answer is given by the HJM drift condition below. 
Theorem 23.1 (HJM drift condition) Assume that the family of forward 
rates is given by (23.1) and that the induced bond market is arbitrage free. Then 
there exists a d-dimensional column-vector process 
x(t) = [xl(t), . xd(t)]' 
with the property that for all T 2 0 and for all t 5 T, we have 
T 
a(t, T) = o(t, T) 1 u(t, s)' ds - o(t, T)A(~). 
(23.4) 
In these fonulas ' denotes transpose. 
Proof From Proposition 20.5 we have the bond dynamics 
dp(t, T) 
= PO, T) {r(t) + A(t, T) + $ IlS(t, T)II~) dt + ~ ( t ,  
T)S(t, T) dW(t), 
(23.5) 

FORWARD RATE MODELS 
342 
where 
A(t, T) = - s , ~  
a(t, S) ds, 
S(t,T) = - ~ ~ a ( t , s ) d s .  
The risk premium for the T-bond is thus given by 
A(t,T) + ;lIS(t,~)11~, 
and, applying Result 15.6.1, we conclude the existence of a d-dimensional 
column-vector process X such that 
Taking the T-derivative of this equation gives us eqn (23.4). 
23.2 Martingale Modeling 
We now turn to the question of martingale modeling, and thus assume that the 
forward rates are specified directly under a martingale measure Q as 
df (t, T) = a(t, T) dt + a(t, T) dW(t), 
(23.7) 
f (0, T) = f*(O, T), 
(23.8) 
where W is a (d-dimensional) Q-Wiener process. Since a martingale measure 
automatically provides arbitrage free prices, we no longer have a problem of 
absence of arbitrage, but instead we have another problem. This is so because 
we now have the fillowing two different formulas for bond prices 
where the short rate r and the forward rates f are connected by r(t) = f (t, t). In 
order for these formulas to hold simultaneously, we have to impose some sort of 
consistency relation between a and a in the forward rate dynamics. The result 
is the famous HJM drift condition. 
Proposition 23.2 (HJM drift condition) Under the martingale measure Q, 
the processes a and u must satisfy the following relation, for every t and 
every T 3 t. 
rT 
a(t, T) = g(t, T) 1 a(t, s)' ds. 

MARTINGALE MODELING 
343 
Proof A short and brave argument is to observe that if we start by modeling 
directly under the martingale measure, then we may apply Proposition 23.1 with 
X = 0. A more detailed argument is as follows. 
From Proposition 20.5 we again have the bond price dynamics 
We also know that, under a martingale measure, the local rate of return has to 
equal the short rate r. Thus we have the equation 
which gives us the result. 
The moral of Proposition 23.2 is that when we specify the forward rate dynamics 
(under Q) we may freely specify the volatility structure. The drift parameters 
are then uniquely determined. An "algorithm" for the use of an HJM model can 
be written schematically as follows: 
1. Specify, by your own choice, the volatilities u(t, T). 
2. The drift parameters of the forward rates are now given by 
T 
a(t, T) = ~ ( t ,  
T) 1 u(t, s)' ds. 
(23.10) 
3. Go to the market and observe today's forward rate structure 
4. Integrate in order to get the forward rates as 
5. Compute bond prices using the formula 
6. Use the results above in order to compute prices for derivatives. 
To see at least how part of this machinery works we now study the simplest 
example conceivable, which occurs when the process u is a deterministic constant. 
With a slight abuse of notation let us thus write u(t, T) = u, where u > 0. 
Equation (23.9) gives us the drift process as 

344 
FORWARD RATE MODELS 
so eqn (23.11) becomes 
In particular we see that r is given as 
so the short rate dynamics are 
dr(t) = { f ~ ( ~ , . t )  
+ u2t) dt + u dW(t), 
(23.17) 
which is exactly the HeLee model, fitted to the initial term structure. Observe 
in particular the ease with which we obtained a perfect fit to the initial 
term structure. 
23.3 The Musiela Parameterization 
In many practical applications it is more natural to use time to maturity, rather 
than time of maturity, to parameterize bonds and forward rates. If we denote 
running time by t, time of maturity by T, and time to maturity by x, then we 
have x = T - t, and in terms of x the forward rates are defined as follows. 
Definition 23.3 For all x 2 0 the forward rates r(t, x) are defined by 
the relation 
r(t, x) = f (t, t + x). 
(23.18) 
Suppose now that we have the standard HJM-type model for the forward rates 
under a martingale measure Q 
The question is to find the Q-dynamics for r(t, x), and we have the following 
result, known as the Musiela equation. 
Proposition 23.4 (The Musiela equation) Assume that the forward rate 
dynamics under Q are given by (23.19). Then 
dr(t, x) = {Fr(t, x) + D(t, x)) dt + uo(t, X) dW(t), 
(23.20) 

EXERCISES 
where 
uo(t, x) = u(t, t + x), 
rx 
D(t, x) = uo(t, x) 
uo(t, s)' ds, 
10 
Proof Using a slight variation of the It6 formula we have 
where the differential in the term df (t, t + x) only operates on the first t. We 
thus obtain 
a 
dr(t, 2) = a(t, t + X) dt + u(t, t + x) dW(t) + -r(t, z) dt, 
ax 
and, using the HJM drift condition, we obtain our result. 
The point of the Musiela parameterization is that it highlights eqn (23.20) 
as an infinite dimensional SDE. It has become an indispensible tool of modern 
interest rate theory. 
23.4 Exercises 
Exercise 23.1 Show that for the Hull-White model 
dr = (8 (t) - ar) dt + u dW, 
the corresponding HJM formulation is given by 
df (t, T).= a(t, T) dt + ae-a(T-t) dW 
Exercise 23.2 (Gaussian interest rates) Take as given an HJM model (under 
the risk neutral measure Q) of the form 
d f (t, T) = a(t, T) dt + o(t, T) dW(t), 
where the volatility u(t, T) is a deterministic function of t and T. 
(a) Show that all forward rates, as well as the short rate, are normally 
distributed. 
(b) Show that bond prices are log-normally distributed. 

346 
FORWARD RATE MODELS 
Exercise 23.3 Consider the domestic and a foreign bond market, with bond 
prices being denoted by pd(t, T) and pf (t, T) respectively. Take as given a 
standard HJM model for the domestic forward rates fd(t, T), of the form 
where W is a multidimensional Wiener process under the domestic martingale 
measure Q. The foreign forward rates are denoted by ff(t,T), and their 
dynamics, still under the domestic martingale measure Q, are assumed to be 
given by 
dff(t,T) =af(t,T)dt+af(t,T)dW(t). 
Note that the same vector Wiener process is driving both the domestic and 
the foreign bond market. The exchange rate X (denoted in units of domestic 
currency per unit of foreign currency) has the Q dynamics 
Under a foreign martingale measure, the coefficient processes for the foreign 
forward rates will of course satisfy a standard HJM drift condition, but here 
we have given the dynamics of ff under the domestic martingale measure Q. 
Show that under this measure the foreign forward rates satisfy the modified 
drift condition 
Exercise 23.4 With notation as in the exercise above, we define the yield 
spread g (t, T) by 
~ ( t ,  
T) = ff (t, T) - fd(t, 
Assume that you are given the dynamics for the exchange rate and the domestic 
forward rates as above. You are also given the spread dynamics (again under the 
domestic measure Q) as 
Derive the appropriate drift condition for the coefficient process a, in terms of 
u,, ud and ax (but not involving af ). 
Exercise 23.5 A consol bond is a bond which forever pays a constant con- 
tinuous coupon. We normalize the coupon to unity, so over every interval with 
length dt the consol pays l.dt. No face value is ever paid. The price C(t), at time 
t, of the consol is the value of this infinite stream of income, and it is obviously 
(why?) given by 
C(t) = irn 
p(t, s) ds. 

I Now assume that bond price dynamics under a martingale measure Q are 
1 given by 
dP(t, T) = ~ ( t ,  
T)r(t) dt + ~ ( t ,  
T)v(t, T) 
dW(t), 
where W is a vector valued Q-Wiener process. Use the heuristic arguments given 
in the derivation of the HJM drift condition (see Section 20.2.2) in order to show 
that the consol dynamics are of the form 
dC(t) = (C(t)r(t) - 1) dt + uc (t) dW (t), 
where 
23.5 Notes 
The basic paper for this chapter is Heath et al. (1987). The Musiela paramet- 
erization was first systematically investigated in Musiela (1993), and developed 
further in Brace and Musiela (1994). Consistency problems for HJM models and 
families of forward rate curves were studied in Bjork and Christensen (1999), 
Filipovit: (1999), and FilipoviE (2001). The question of when the short rate in a 
I HJM model is in fact Markovian was first studied in Carverhill (1994) for the 
case of deterministic volatiliy, and for the case of a short rate depending volatility 
structure it was solved in Jeffrey (1995). The more general question when a given 
I HJM model admits a realization in terms of a finite dimensional Markovian diffu- 
1 
sion was, for various special cases, studied in Ritchken and Ssnkarasubramanian 
(1995), Cheyette(l996), Bhar and Chiarella (1997), Inui and Kijima (1998), 
Bjork and Gombani (1999), and Chiarella and Kwon (2001). The necessary and 
I sufficient conditions for the existence of finite dimensional Markovian realisa- 
tions in the general case were first obtained, using methods from differential 
geometry, in Bjork and Svensson (2001). This theory has then been developed 
further in Bjork and Land& (2002), and Filipovid and Teichmann (2001). A 
I 
survey is given in Bjork (2001). In Shirakawa (1991), Bjork (1995), Bjork et al. 
(1997a,b), and Jarrow and Madan (1995) the HJM theory has been extended to 
more general driving noise processes. There is a growing literature on defaultable 
bonds. See Merton (1974), Duffie and Singleton (1994), Leland (1994), Jarrow 
et al. (1997) and Lando (1997). Concerning practical estimation of the yield 
/ curve see Anderson et d. (1996). 

CHANGE OF NUMERAIRE* 
24.1 Introduction 
Consider a given financial market (not necessarily a bond market) with the 
usual locally risk free asset B, and a risk neutral martingale measure Q. As 
noted in Chapter 10 a measure is a martingale measure only relative to some 
chosen numeraire asset, and we recall that the risk neutral martingale measure, 
with the money account B as numeraire, has the property of martingalizing all 
processes of the form S(t)/B(t) where S is the arbitrage free price process of any 
(nondividend paying) traded asset. 
In many concrete situations the computational work needed for the determ- 
ination of arbitrage free prices can be drastically reduced by a clever change 
of numeraire, and the purpose of the present chapter, which to a large extent 
follows and is inspired by Geman et al. (1995), is to analyze such changes. See 
the Notes for the more bibliographic information. 
To get some feeling for where we are heading, let us consider the pricing 
problem for a contingent claim X, in a model with a stochastic short rate r. 
Using the standard risk neutral valuation formula we know that the price at 
t = 0 of X is given by 
The problem with this formula from a computational point of view is that in 
order to compute the expected value we have to get hold of the joint distribution 
(under Q) of the two stochastic variables J: 
r(s) ds and X, and finally we have 
to integrate with respect to that distribution. Thus we have to compute a double 
integral, and in most cases this turns out to be rather hard work. 
Let us now make the (extremely unrealistic) assumption that r and X are 
independent under Q. Then the expectation above splits, and we have the 
formula 
n(o; X) = EQ [,-.far 
r ( s ) d s ]  . EQ [XI, 
which we may write as 
We now note that (24.2) is a much nicer formula than (24.1), since 
We only have to compute the single integral EQ [XI instead of the double 
integral EQ [exp {- % r(s) ds} XI. 

GENERALITIES 
349 
The bond price p(0,T) in formula (24.2) does not have to be com- 
puted theoretically at all. We can observe it (at t = 0) directly on the 
1 
su 
bond market. 
The drawback with the argument above is that, in most concrete cases, r and 
X are not independent under Q, and if X is a contingent claim on an underlying 
bond, this is of course obvious. What may be less obvious is that even if X is 
a claim on an underlying stock which is P-independent of r ,  it will still be the 
case that X and r will be dependent (generically) under Q. The reason is that 
under Q the stock will have r as its local rate of return, thus introducing a 
Q-dependence. 
This is the bad news. The good news is that there exists a general pricing 
formula (see Proposition 24.8), a special case of which reads as 
' Here E~ denotes expectation w.r.t. the so-called forward neutral measure QT, 
which we will discuss below. We will also discuss more general changes 
of numeraire. 
24.2 Generalities 
We now proceed to the formal discussion of numeraire changes, and we start by 
I setting the scene. 
Assumption 24.2.1 We consider an arbitrage free market model with asset 
prices So, S1,. . . , S, where So is assumed to be strictly positive. 
Sometimes, but not always, we will need to assume that all prices are 
Wiener driven. 
Condition 24.2.1 Under P ,  the S-dynamics are of the form 
where the coeficient processes are adapted and W is a multidimensional standard 
P- Wiener process. 
I Remark 24.2.1 We do not necessarily assume the existence of a short rate and 
I a money account. If the model admits a short rate and a money account they 
I will as usual be denoted by r and B, respectively. 
r 
From a mathematical point of view, most of the results concerning changes of 
numeraire are really special cases of the First Fundamental Theorem and the 
associated pricing formulas. Thus the difference between the present chapter 
and Chapter 10 is more one of perspective than one of essence. We now recall 
I some facts from Chapter 10 and start with the Invariance Lemma. 

350 
CHANGE OF NUMERAIRE 
L e m m a  24.1 (Invariance l e m m a )  Let P be any strictly positive It6 process, 
and define the normalized process 2 with numeraire /3, by Z = SIP. Then h 
is S-self-financing if and only if h is 2-self-financing, i.e. with notation as in 
Chapter 10 we have 
d v s ( t ;  h )  = h(t) dS(t) 
(24.4) 
if and only if 
d v Z ( t ;  h )  = h(t) dZ(t). 
Proof Follows immediately from the It6 formula. 
0 
We make two remarks on the Invariance Lemma. 
A process /3 satisfying the assumptions above is sometimes called a 
"deflator process". 
We have assumed that S and p are It6 processes. This is not important, and 
the Invariance Lemma does in fact hold also in a general semimartingale 
setting. 
Observe that at this point we do not assume that the deflator process /3 
is the price process for a traded asset. The Invariance Lemma will hold for 
any positive process p satisfying the assumptions above. 
From Chapter 10 (see summary in Section 10.7) we now recall the First 
Fundamental Theorem and the corresponding pricing formula. 
T h e o r e m  24.2 Under the assumptions above, the following hold: 
The market model is free of arbitrage if and only if there exists a 
martingale measure, Q0 
N P such that the processes 
are (local) martingales under QO. 
In order to avoid arbitrage, a T-claim X must be priced according to the 
formula 
where E0 denotes expectation under QO. 
In most of our applications earlier in the book we have used the money 
account B as the numeraire, but in many applications the choice of another 
asset as the numeraire asset can greatly facilitate computations. A typical 
example when this situation occurs is when dealing with derivatives defined 
in terms of several underlying assets. Assume for example that we are given 
two asset prices S1 and S2, and that the contract X to be priced is of the form 
X = @(S1 (T), S2(T)), where @ is a given linearly homogenous function. Using 

GENERALITIES 
351 
the standard machinery, and denoting the risk neutral martingale measure by 
Q0 we would have to compute the price as 
which essentially amounts to the calculation of a triple integral. If we instead 
use S1 as numeraire, with martingale measure Q1, we have 
where cp(z) = @(l, z) and Zz(t) = Sz(t)/Sl(t). In this formula we note that the 
i 
factor Sl(t) is the price of the traded asset Sl at time t, so this quantity does 
not have to be computed-it can be directly observed on the market. Thus the 
computational work is reduced to computing a single integral. We also note the 
important fact that in the Z economy we have zero short rate. 
Example 24.3 As an example of the reasoning above, assume that, we have two 
stocks, S1 and S2, with price processes of the following form under the objective 
probability measure P: 
dS1 (t) = a1 SI (t) dt + SI (t)ol dW(t), 
(24.8) 
dSz (t) = a z S 2  (t) dt + SZ (~)uz 
dW(t). 
(24.9) 
1 Here al, a 2  E R and ul, 0 2  E R2 are assumed to be deterministic, and W is 
, 
assumed to be a two dimensional standard Wiener process under P. We assume 
absence of arbitrage. 
The T-claim to be priced is an exchange option, which gives the holder the 
I 
right, but not the obligation, to exchange one Sz share for one S1 share at time T. 
Formally this means that the claim is given by Y = max [S2(T) - S1(T), 01, and 
we note that we have a linearly homogeneous contract function. It is thus natural 
to use one of the assets as the numeraire, and we choose S1. From Theorem 24.2, 
and using homogeneity, the price is given by 
with Z2(t) = Sz(t)/Sl(t) and with El denoting expectation under Q1. We are 
thus in fact valuing a European call option on Zz(T), with strike price K = 1 in 
a world with zero short rate. 
We now have to compute the Q1 dynamics of 2 2 ,  but this turns out to be 
very easy. From It8, the P-dynamics of Zz are of the form 
dZ2 (t) = Zz (t) (. . .) dt + 2 2  (t) ( ~ 2  
- ui ) dW(t) 

352 
CHANGE OF NUMERAIRE 
where we do not care about the precise form of the dt-terms. Under Q1 we know 
that Z2 is a martingale, and since the volatility terms do not change under a 
Girsanov transformation we obtain directly the Q1 dynamics as 
dZ2 (t) = 2 2  (t) {a2 - 01 1 dwl (t), 
(24.10) 
where W1 is Q1-Wiener. We can write this as 
where W is a scalar Q1-Wiener process and 
Using the BlackScholes formula with zero short rate, unit strike price and 
volatility a, the price of the exchange option is thus given by the formula 
II(t; X) = Si (t) {Zz(t)N[dil - N[d2l) 
(24.11) 
= Sz(t)N[dlI - Si(t)N[dzI, 
(24.12) 
If, instead of using a two &mensional standard Wiener process, we model the 
stock price dynamics as 
dSl (t) = Sl (t) dt + Si ( t ) ~ i  
dwi (t) , 
dS2 (t) = a 2 5 2  (t) dt + S2 (t)a2 diiTz (t) , 
where w1 and w2 are scalar P-Wiener with local correlation p, and thus a1 and 
0 2  are scalar constants, then it is easy to see that the relevant volatility to use 
in the formula above is given by 
I 
Note that we made no assumption whatsoever about the dynamics of the short 
rate. The result above thus holds for every possible specification of the short 
f 
rate process. 
1 

CHANGING THE NUMERAIRE 
353 
We will give several other concrete examples below, but first we will investig- 
ate how we change from one choice of numeraire to another, i.e. how we determine 
the appropriate Girsanov transformation. This will be done in the next section. 
Remark 24.2.2 Since there sometimes seems to be confusion around what is a 
bona fide choice of numeraire, let us recall some points in the derivation of the 
First Fundamental Theorem: 
In the basic version of the theorem (Theorem 10.9) we assumed that So was 
a risk free traded asset with zero rate of return. It was a crucial ingredient 
in the proof that we were allowed to invest in this risk free asset. 
For the general case we used the traded asset So as the numeraire. In the 
normalized economy this provided us with a traded asset Zo which was 
risk free with zero rate of return. The Invariance Lemma then allowed us 
to use the basic version of Theorem 10.9 to complete the proof. 
The point of these comments is that the Invariance Lemma is true for any 
deflator process P, but when it comes to the existence of martingale meas- 
ures and pricing, we must use a numeraire which is the price process of a 
traded asset without dividends. 
In particular, if we want to use numeraires like 
a nonfinancial index, 
a forward or futures price process, 
the price process of a traded asset with dividends, 
then we must carry out a careful separate analysis, since in these cases 
we do not have access to a standard version of the First Fund* 
mental Theorem. 
24.3 Changing the Numeraire 
Suppose that for a specific numeraire So we have determined the corresponding 
(not necessarily unique) martingale measure QO, and the associated dynamics 
of the asset prices (and possibly also the dynamics of other factors within the 
model). Suppose furthermore that we want to change the numeraire from So to, 
say, Sl. An immediate problem is then to find the appropriate Girsanov trans- 
formation which will take us from Q0 to Q1, where Q1 is the martingale measure 
corresponding to the numeraire Sl. This problem will for example turn up in 
connection with the LIBOR market models treated later in the book. 
This problem is in fact quite easily solved, and to see this, let us use the 
pricing part of Theorem 24.2 for an arbitrary choice of T-claim X. We then have 
and also 
II(0;X) = S1(0)E1 
(24.14) 

354 
CHANGE OF NUMERAIRE 
Denoting by LA(T) the Radon-Nikodym derivative 
we can write (24.14) as 
and we thus have 
for all (sufficiently integrable) T-claims X. We thus deduce that 
I 
so we obtain 
which is our candidate as a Radon-Nikodym derivative. The obvious choice of 
the induced likelihood process is of course given by 
This looks promising, since the process Sl(t)/So(t) is a Qo-martingale (why?), 
and we know that any likelihood process for the transition from Q0 to Q1 has 
to be a Qo-martingale. In more formal terms we have the following proposition. 
Proposition 24.4 Assume that Q0 is a martingale measure for the mmeraire 
So (on FT) and assume that S1 is a positive asset price process such that 
Sl(t)/So(t) is a true Qo-martingale (and not just a local one). Define Q1 on 
FT by the likelihood process 
Then Q1 is a martingale measure for Sl. 
Proof We have to show that for every (sdciently integrable) arbitrage free 
price process 11, the normalized process TI (t) /Sl(t) is a Q1-martingale. Now, if 

FORWARD MEASURES 
355 
I ll is an arbitrage free price process then we know that II/So is a Qu-martingale 
and for s 5 t we have the following calculation, where we use the Abstract 
Bayes' Formula: 
Since we have determined the relevant likelihood process, we can identify the 
Girsanov kernel. 
Proposition 24.5 Assume absence of arbitrage and that Condition 24.2.1 
is in force. Denote the corresponding Q"- Wiener process by W". 1 'hen the 
Qo-dynamics of the likelihood process LA are given by 
L;(t) = LA(t) {a1 (t) - ao(t)) dw"(t). 
(24.19) 
Thus the Girsanov kernel cpA for the transition from Q0 to Q1 is given by the 
volatility difference 
cp;(t) = 0 1  (t) - ao(t). 
(24.20) 
Proof The result follows immediately from applying the It6 formula to 
(24.18). 
I 
i 
24.4 Forward Measures 
In this section we specialize the theory developed in the previous section to the 
case when the new numeraire chosen is a bond maturing at time T. As can be 
expected this choice of numeraire is particularly useful when dealing with interest 
rate derivatives. 
1 
24.4.1 
Using the T-bond as Numeraire 
/ 
Suppose that we are given a specified bond market model with a fixed (money 
account) martingale measure Q. For a fixed time ot maturity T we now choose 
the zero coupon bond maturing at T as our new numeraire. 
Definition 24.6 For a fixed T, the T-forward measure QT is defined as the 
martingale measure for the numeraire process p(t, T). 

356 
CHANGE OF NUMERAIRE 
In interest rate theory we often have our models specified under the risk neutral 
martingale measure Q with the money account B as the numeraire. We then 
have the following explicit description QT. 
Proposition 24.7 If Q denotes the risk neutral martingale measure, then the 
likelihood process 
is given by 
In particular, if the Q-dynamics of the T-bond are Wiener driven, i.e. of the form 
where W is a (possibly multidimensional) Q Wiener process, then the LT 
dynamics are given by 
i.e. the Girsanov kernel for the transition from Q to QT is given by the T-bond 
volatility v(t, T). 
- 
Proof The result follows immediately from Proposition 24.4 with QT = Q1 
and Q0 = Q. 
Observing that P ( T ,  T )  = 1 we have the following useful pricing formula as an 
immediate corollary of Proposition 24.2. 
Proposition 24.8 For any T-claim X we have 
n(t; 
X )  = p(t, T ) E T  [XI 5 1  , 
(24.24) 
where E~ denotes integration w.r.t. QT. 
Note again that the price p(t,T) does not have to be computed. It can be 
observed directly on the market at time t. 
A natural question to ask is when Q and QT coincide. 
Lemma 24.9 The relation Q = QT holds i f  and only if r is deterministic. 
Proof Exercise for the reader. 

FORWARD MEASURES 
1 
24.4.2 An Expectation Hypothesis 
We now make a small digression to discuss the forward rate process f (t, T). The 
economic interpretation of f (t, T) is that this is the risk free rate of return which 
we may have on an investment over the infinitesimal interval [T, T + dT] if the 
contract is made at t. On the other hand, the short rate r(T) is the risk free rate 
of return over the infinitesimal interval [T, T + dT], if the contract is made at 
T. Thus it is natural to view f (t, T) (which can be observed at t) as an estim- 
ate of the future short rate r(T). More explicitly it is sometimes argued that if 
the market expects the short rate at T to be high, then it seems reasonable to 
assume that the forward rate f (t, T) is also high, since otherwise there would be 
1 
profits to be made on the bond market. 
i 
Our task now is to determine whether this reawning is correct in a more pre 
1 
cise sense, and to this end we study the most formalized version of the argument 
I above, known as the "unbiased expectation hypothesis" for forward rates. This 
I 
hypothesis then says that in an efficient market we must have 
\ 
i.e. the present forward rate is an unbiased estimator of the future spot rate. If 
we interpret the expression "an efficient market" as "an arbitrage free market" 
then we may use our general machinery to analyze the problem. 
First we notice that there is no probability measure indicated in (24.25), so 
we have to make a choice. 
Of course there is no reason at all to expect the hypothesis to be true under 
the objective measure P, but it is often claimed that it holds "in a risk neutral 
world". This more refined version of the hypothesis can then be formulated as 
where Q is the usual risk neutral martingale measure. In fact, also this ver- 
sion of the expectation hypothesis is in general incorrect, which is shown by the 
following result. 
Lemma 24.10 Assume that, for all T > 0 we have r(T)/B(T) E L1 
(Q). Then, 
for every jixed T, the process f (t, T) is a QT-martingale for 0 5 t 5 T, and in 
particular we have 
f(t,T) = ET [r(T)IFt]. 
(24.27) 
Proof Using Proposition 24.24 with X = r(T) we have 
II(t; X) = EQ [ r ( ~ ) e -  I: 
'('1 d'l F~] 
= p(t, T ) E ~ [ ~ ( T ) /  
Ft] . 

CHANGE OF NUMERAIRE 
This gives us 
EQ [r (T)~- 1: 
r(s) ds Ft 
ET [r(T) I Ft] = - 
~ ( t ,  
T) 
I I 
1 a 
= -- 
-EQ [,- .I:r(s)ds 3t 
~ ( t ,  
T )  
I I 
= ----- = f(t,T). 
~ ( t ,  
T) 
I3 
We thus see that the expectation hypothesis is false also under Q, but true 
under QT. Note, however, that we have different Q~ for different choices of the 
maturity date T. 
24.5 A General Option Pricing Formula 
The object of this section is to give a fairly general formula for the pricing of 
European call options, and for the rest of the section we basically follow Geman 
et al. (1995). Assume therefore that we are given a financial market with a 
(possibly stochastic) short rate r, and a strictly positive asset price process S(t). 
The option under consideration is a European call on S with date of 
maturity T and strike price K. We are thus considering the T-claim 
X = max [S(T) - K, 01, 
(24.28) 
and, for readability reasons, we confine ourselves to computing the option price 
n(t; X) at time t = 0. 
The main reason for the existence of a large number of explicit option pricing 
formulas is that the contract function for an option is piecewise linear. We can 
capitalize on this fact by using a not so well-known trick with indicator functions. 
Write the option as 
where I is the indicator function, i.e. 
Denoting the risk neutral martingale measure by Q, 
we obtain 

A GENERAL OPTION PRICING FORMULA 
359 
In the first term above, we use the measure Q~ having S as numeraire, and for 
the second term we use the T-forward measure. From Theorem 24.2 and Pro- 
position 24.8 we then obtain the following basic option pricing formula, which is 
a substantial extension of the standard Black-Scholes formula. 
Proposition 24.11 (General option pricing formula) Given the assump- 
tions above, the option price is given by 
Here QT denotes the T-forward measure, whereas QS denotes the martingale 
measure for the numemire process S(t). 
In order to use this formula in a real situation we have to be able to compute 
the probabilities above, and the standard condition which ensures computabil- 
ity turns out to be that volatilities should be deterministic. Hence we have the 
following &sumption. 
Assumption 24.5.1 Assume that the process Z S , ~  
defined by 
has a stochastic differential of the form 
where the volatility process uS,~(t) 
is deterministic. 
The crucial point here is of course the assumption that the row-vector process 
o s , ~  
is deterministic. Note that the volatility process as always is unaffected by 
a change of measure, so we do not have to specify under which measure we check 
the condition. It can be done under P as well as under Q. 
We start the computations by writing the probability in the second term of 
(24.29) as 
Since Z S , ~  
is an asset price, normalized by the price of a T-bond, it is a Q~ 
martingale, so its QT-dynamics are given by 
~ Z S , T  
(t) = ZS,T (~)Qs,T (t) dwT (t). 
(24.33) 
This is basically GBM, driven by a multidimensional Wiener process, and it is 
easy to see that the solution is given by 

F 
! 
360 
CHANGE OF NUMERAIRE 
In the exponent we have a stochastic integral and a deterministic time integral. 
r 
Since the integrand in the stochastic integral is deterministic, an easy extension 
D 
F 
of Lemma 4.15 shows that the stochastic integral has a Gaussian distribution 
i 
f 
with zero mean and variance 
I 
The entire exponent is thus normally distributed, and we can write the 
I 
I 
probability in the second term in (24.29) as 
1 
I 
where 
q L:,T 
t1 ) 
Since the first probability term in (24.29) is a Qs-probability, it is natural to write 
the event under consideration in terms of a quotient with S in the denominator. 
I 
I 
Thus we write 
s P(T TI 
1 
QS(s(T) 2 K) = Q (' 
5 +) = QS(YS,T(T) 5 F) , 
(24.37) 
where YS,T is defined by 
Under QS the process YS,T has zero drift, so its Qs-dynamics are of the form 
dYs,~(t) = Ys,~(t)Ss,~(t) 
dwS (t). 
Since YS,T = z&, an easy application of I~B'S formula gives us asYT(t) = 
-us,~(t). Thus we have 
and again we have a normally distributed exponent. Thus, after some 
simplification, 
Q S ( S ( ~ >  
2 K )  = N[dll, 
where 
1 
We have thus proved the following result. 
1 

r 
THE HULL-WHITE MODEL 
Proposition 24.12 (Geman-El Karoui-Rochet) 
Under 
the 
conditions 
given in Assumption 24.5.1, the price of the call option defined in (24.28) is 
given by the formula 
Here dp and dl are given in (24.36) and (24.38), respectively, whereas C;,,(T) 
is defined by (24.35). 
24.6 The Hull-White Model 
As a concrete application of the option pricing formula of the previous sec- 
i tion, we will now consider the case of interest rate options in the Hull-White 
I model (extended VasiEek). To this end recall that in the Hull-White model the 
Q-dynamics of r are given by 
dr = {%(t) - ar) dt + u dW. 
(24.40) 
From Section 22.3 we recall that we have an affine term structure 
where A and B are deterministic functions, and where B is given by 
The project is to price a European call option with exercise date TI and 
strike price K, on an underlying bond with date of maturity Tz, where TI < Tp. 
In the notation of the general theory above this means that T = TI and that 
S(t) = p(t, Tp). We start by checking Assumption 24.5.1, i.e. if the volatility, (T,, 
I of the process 
~ ( t  
T2) 
Z(t) = - 
(24.43) 
~ ( t ,  
Tl) 
is deterministic. (In terms of the notation in Section 24.5 Z corresponds to ZS,T 
and u, corresponds to 
Inserting (24.41) into (24.43) gives 
Applying the It6 formula to this expression, and using (24.40), we get the 
Q-dynamics 
dZ(t) = Z(t) {- . ) dt + Z(t) . U, (t) dW, 
(24.44) 
where 

362 
CHANGE OF NUMERAIRE 
Thus a, is in fact deterministic, so we may apply Proposition 24.12. We obtain 
the following result, which also holds (why?) for the VasiEek model. 
Proposition 24.13 (Hull-White bond option) In the Hull-White model 
(24.40) the price, at t = 0, of a European call with strike price K ,  and time 
of maturity TI, on a bond maturing at T2 is given by the formula 
where 
We end the discussion of the Hull-White model, by studying the pricing 
problem for a claim of the form 
Using the T-bond as numeraire Proposition 24.8 gives us 
so we must find the distribution of r(T) under QT, and to this end we will use 
Theorem 24.5 (with Q as Q0 and QT as Q1). We thus need the volatility of the 
T-bond, and from (24.41)-(24.42) we obtain bond prices (under Q) as 
where the volatility v(t , T) is given by 
v(t, T) = -aB(t, T). 
Thus, using Theorem 24.5 and the fact that the money account B has zero 
volatility, the Girsanov kernel for the transition from Q to QT is given by 
The QT-dynamics of the short rate are thus given by 
where wT is a QT-Wiener process. 

THE GENERAL GAUSSIAN MODEL 
363 
We observe that, since v(t, T) and O(t) are deterministic, r is a Gaussian 
process, so the distribution of r(T) is completely determined by its mean and 
variance under QT. Solving the linear SDE (24.53) gives us 
, 
We can now compute the conditional QT-variance of r(T), a: (t, T), as 
Note that the QT-mean of r(T), m,(t,T) = E~ [r(T)(Ft], does not have to be 
computed at all. We obtain it directly from Lemma 24.10 as 
which can be observed directly from market data. 
Under QT, the conditional distribution of r(T) is thus the normal distribu- 
tion N[f (t, T), ur(t, T)], and performing the integration in (24.50) we have the 
final result. 
Proposition 24.14 Given the assumptions above, the price of the claim X = 
@(r(T)) is given by 
where o$(t, T)is given by (24.55). 
24.7 The General Gaussian Model 
In this section we extend our earlier results, by computing prices of bond options 
in a general Gaussian forward rate model. We specify the model (under Q) as 
where W is a d-dimensional Q-Wiener process. 
Assumption 24.7.1 We assume that the volatility vector function 
4, 
T) = [m(t, T), . . , ~ d ( t ,  
T)] 
is a deterministic function of the variables t and T. 

364 
CHANGE OF NUMERAIRE 
Using Proposition 20.5 the bond price dynamics under Q are given by 
where the volatility is given by 
We consider a European call option, with expiration date To and exercise 
price K, on an underlying bond with maturity TI (where of course To < TI). In 
order to compute the price of the bond, we use Proposition 24.12, which means 
that we first have to find the volatility U T ~ , T ~  
of the process 
~ ( t ,  
Tl) 
Z(t) = --- 
P(t, To) ' 
An easy calculation shows that in fact 
This is clearly deterministic, so Assumption 24.5.1 is satisfied. We now have the 
following pricing formula. 
Proposition 24.15 (Option prices for Gaussian forward rates) The price, 
at t = 0, of the option 
X = max [p(To, TI) - K, 0] 
is given by 
n(o; x) = p(0, T I ) N [ ~ ~ I  
- K . P(O, T O > N [ ~ ~ I ,  
(24.61) 
where 
dl =
,
1. 
(P(0, Tl)/KP(O, To)) + C$, ,To 
4%' 
and UT,,T, is given by (24.60). 
Proof Follows immediately from Proposition 24.12. 

CAPS AND FLOORS 
24.8 Caps and Floors 
The object of this section is to present one of the most traded of all interest rate 
derivatives-the c a p a n d  to show how it can be priced. 
An interest rate cap is a financial insurance contract which protects you from 
having to pay more than a prespecified rate, the cap rate, even though you have 
a loan at a floating rate of interest. There are also floor contracts which guar- 
I 
antee that the interest paid on a floating rate loan will never be below some 
predetermined floor rate. For simplicity we assume that we are standing at 
time t = 0, and that the cap is to be in force over the interval [0, TI. Technically 
speaking, a cap is the sum of a number of basic contracts, known as caplets, 
which are defined as follows: 
The interval [0, TI is subdivided by the equidistant points 
We use the notation 6 for the length of an elementary interval, i.e. 
6 = Ti - Ti-l. Typically, 6 is a quarter of a year, or half a year. 
The cap is working on some principal amount of money, denoted by K ,  
and the cap rate is denoted by R. 
The floating rate of interest underlying the cap is not the short rate r ,  
but rather some market rate, and we will assume that over the interval 
[Ti-l, Ti] it is the LIBOR spot rate L(T,-1, Ti) (see Section 20.2). 
* 
Caplet i is now defined as the following contingent claim, paid at Ti, 
We now turn to the problem of pricing the caplet, and without loss of gener- 
, ality we may assume that K = 1. We will also use the notation x+ = max[x, 01, 
so the caplet can be written as 
IL 
where L = L(Ti-l,Ti). Denoting p(Ti-~, Ti) by p, and recalling that 
we have 
.
+
.
 
XI 

366 
CHANGE OF NUMERAIRE 
where R* = 1 + 6R. It is, however, easily seen (why?) that a payment of 
(R*/p) ((l/R*) - p)f at time Ti is equivalent to a payment of R* ((l/R*) - p)+ 
at time Ti-l. 
Consequently we see that a caplet is equivalent to R* put options on an 
underlying Ti-bond, where the exercise date of the option is at Ti-l and the 
exercise price is 1/R*. An entire cap contract can thus be viewed as a portfolio 
of put options, and we may use the earlier results of the chapter to compute the 
theoretical price. 
A different approach to the pricing of caplets (and hence of caps) is to view 
the caplet claim in (24.62) as a formal option directly on the LIBOR rate, and 
noting that the LIBOR forward rate L(t; Ti, Ti+l) is a martingale under QT'+l . 
This approach will be investigated in some detail in the chapter on LIBOR 
market models below. 
24.9 Exercises 
Exercise 24.1 Derive a pricing formula for European bond options in the 
HeLee model. 
7 
Exercise 24.2 A Gaussian Interest Rate Model 
Take as given a HJM model (under the risk neutral measure Q) of the form 
d f (t, T) = a(t, T) dt + u1 (T - t)dWl (t) + 0 2  e-a(T-t) dW2(t), 
where a1 and 02 are constants. 
(a) Derive the bond price dynamics. 
(b) Compute the pricing formula for a European call option on an underlying 
bond. 
Exercise 24.3 Prove that a payment of (lip) (A - p)+ at time Ti is equival- 
ent to a payment of (A - p)+ at time Tiwl, where p = p(T,-1, Ti), and A is a 
deterministic constant. 
Exercise 24.4 Prove Lemma 24.9. 
Exercise 24.5 Use the technique above in order to prove the pricing formula 
of Proposition 22.5, for bond options in the HwLee model. 
24.10 Notes 
The first usage of a numeraire different from the risk free asset B was probably 
in Merton (1973), where however the technique is not explicitly discussed. The 
first to explicitly use a change of numeraire change was Margrabe (1978), who 
(referring to a discussion with S. Ross) used an underlying stock as numeraire 
in order to value an exchange option. The numeraire change is also used in 
Harrison and Kreps (1979), Harrison and Pliska (1981) and basically in all later 

NOTES 
367 
works on the existence of martingale measures in order to reduce (as we did 
in Chapter 10) the general case to the basic case of zero short rate. In these 
papers, the numeraire change as such is however not put to systematic use as 
an instrument for facilitating the computation of option prices in complicated 
models. In the context of interest rate theory, changes of numeraire were then 
used and discussed independently by Geman (1989) and (in a Gaussian frame- 
work) Jamshidian (1989), who both used a bond maturing at a fixed time T as 
numeraire. A systematic study of general changes of numeraire has been carried 
out by Geman, El Karoui and h c h e t  in a series of papers, and many of the 
results above can be found in Geman et al. (1995). For further examples of the 
change of numeraire technique, see Benninga et al. (2002). 

In the previous chapters we have concentrated on studying interest rate models 
based on infinitesimal interest rates like the instantaneous short rate and the 
instantaneous forward rates. While these objects are nice to handle from a math- 
ematical point of view, they have two main disadvantages: 
The instantaneous short and forward rates can never be observed in 
real life. 
If you would like to calibrate your model to c a p  or swaption data, then 
this is typically very complicated from a numerical point of view if you use 
one of the "instantaneous" models. 
A further fact from real life, which has been somewhat disturbing from a 
theoretical point of view is the following: 
For a very long time, the market practice has been to value caps, floors, and 
swaptions by using a formal extension of the Black (1976) model. Such an 
extension is typically obtained by an approximation argument where the 
short rate at one point in the argument is assumed to be determinstic, while 
later on in the argument the LIBOR rate is assumed to be stochastic. This 
is of course logically inconsistent. 
Despite this, the market happily continues to use Black-76 for the pricing 
of caps, floors, and swaptions. 
In a situation like this, where market practice seems to be at odds with academic 
I 
work there are two possible attitudes for the theorist: you can join them (the 
market) or you can try to beat them, and since the fixed income market does 
I 
not seem to collapse because of the use of Black-76, the more realistic alternative 
I 
seems to be to join them. 
Thus there has appeared a natural demand for constructing logically consist- 
I 
ent (and arbitrage free!) models having the property that the theoretical prices 
I 
I 
for caps, floors and swaptions produced by the model are of the Black-76 form. 
I 
This project has in fact been carried out very successfully, starting with Miltersen 
I 
et al. (1997), Brace et al, (1997) and Jamshidian (1998). The basic structure of 
the models is as follows: 
In stead of modeling instantaneous interest rates, we model discrete mar- 
ket rates like LIBOR rates in the LIBOR market models, or forward swap 
rates in the swap market models. 
Under a suitable choice of numeraire(s), these market rates can in fact be 
modeled log normally. 

CAPS: DEFINITION AND MARKET PRACTICE 
369 
The market models will thus produce pricing formulas for caps and fioors 
(the LIBOR models), and swaptions (the swap market models) which are 
y 
of the Black-76 type and thus conforming with market practice. 
F 
By construction the market models are thus very easy to calibrate to mar- 
: 
ket data for caps/floors and swaptions respectively. They are then used to 
price more exotic products. For this later pricing part, however, we will 
typically have to resort to some numerical method, like Monte Carlo. 
25.1 Caps: Definition and Market Practice 
In this section we discuss LIBOR caps and the market practice for pricing and 
quoting these intruments. To this end we consider a fixed set of increasing 
maturities To, TI,. . . , TN and we define ai, by 
The number cri is known as the tenor, and in a typical application we could for 
example have all ai equal to a quarter of a year. 
Definition 25.1 W e  let pi(t) denote the zero coupon bond price p(t, T,) and let 
Li(t) 
denote the LIBOR forward rate (see Section 20.2), contracted at t, for the 
period [Ti-1, Ti], 2.e. 
We recall that a cap with cap rate R and resettlement dates To,. . . , TN is 
a contract which at time Ti gives the holder of the cap the amount 
for each i = 1, . . . , N. The cap is thus a portfolio of the individual caplets 
XI,. . . , XN. We note that the forward rate Li(Ti-1) above is in fact the spot rate 
at time 
for the period [Ti-1, Ti], and determined already at time 
The 
amount Xi is thus determined at Ti-1 but not payed out until at time Ti. We 
also note that, formally speaking, the caplet Xi 
is a call option on the underlying 
spot rate. 
The market practice is to use the Black-76 formula for the pricing of caplets. 
Definition 25.2 (Black's Formula for Caplets) The Black-76 formula for 
the caplet 
Xi = ai - ma~[L(Ti-~, 
T,) - R, 01, 
(25.3) 
is given by the expression 

