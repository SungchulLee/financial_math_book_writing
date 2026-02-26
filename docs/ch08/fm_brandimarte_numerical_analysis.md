# Numerical Analysis for Finance

!!! info "Source"
    **Numerical Methods in Finance and Economics** by Paolo Brandimarte, Wiley, 2nd ed., 2006.
    These notes are used for educational purposes.

## Numerical Integration and Differentiation

Part 11 
Numerical Methods 


Basics of Numerical 
d 
Anal ysis 
The core of the MATLAB system implements a set of functions to cope with 
some classical numerical problems. Although there is no need for a really 
deep knowledge of numerical analysis in order to use MATLAB, a grasp of 
the basics is useful in order to choose among competing methods and to 
understand what may go wrong with them. In fact, numerical computation is 
affected by machine precision and error propagation, in ways that may result 
in quite unreasonable outcomes. Hence, we begin by considering the effect of 
finite precision arithmetic and the issues of numerical instability and problem 
conditioning, which are outlined in section 3.1. This material is essential, 
among other things, in understanding the pitfalls of pricing derivatives by 
solving PDEs. 
Then we describe methods for solving systems of linear equations in section 
3.2; MATLAB provides the user with both direct and iterative methods to 
this purpose, and it is important to understand the characteristics of the 
two classes of methods. Section 3.3 introduces the reader to the problems 
of approximating functions and interpolating data values. Solving non-linear 
equations is the subject of section 3.4. 
Other topics, such as numerical integration and finite difference methods for 
PDEs are dealt with in specific chapters. With respect to standard textbooks 
in numerical analysis, a few types of numerical problems have been omitted, 
most notably the computation of matrix eigenvalues and eigenvectors and 
the solution of ordinary differential equations. Both problems are solved by 
methods available in MATLAB, but since they will not be used in the rest of 
the book, we refer the reader to the references listed at the end of the chapter. 
137 

138 
BASICS OF NUMERICAL ANALYSIS 
3.1 NATURE OF NUMERICAL COMPUTATION 
Real analysis is based on real numbers. Unfortunately, dealing with real 
numbers on a computer is impossible. Each number is represented by a fi- 
nite number of bits, taking the values 0 or 1. Hence, we have to settle for 
binary and finite precision arithmetic. The progress in computing hardware 
has improved the quality of the representation, since more bits may be used 
efficiently without resorting to low-level software tricks. Yet some represen- 
tation error is unavoidable, and its effect may lead to unexpected results. We 
have seen some examples of what may go wrong in section 1.3. In this section 
we try to explain why this may happen. 
3.1.1 
The usual way we represent numbers relies on a decimal base. When writing 
1492, we actually mean 
Number representation, rounding, and truncation 
1 x lo3 + 4 x lo2 + 9 x 10' + 2 x loo. 
Similarly, when we have to represent the fractional part of a number, we use 
negative powers of the base 10: 
0.42 =+ 4 x lo-' + 2 x 
Some numbers, such as 1/3 = 0.3, do not have a finite representation and 
should be thought as limits of an infinite series. However, on a computer we 
must use a binary base, since the hardware is based on a binary logic; for 
instance, 
(21.5)10 + 2* + 22 + 2'+ 2-1 = (10101.1)2. 
How can we convert numbers from a decimal to a binary base? Let us begin 
with an integer number N .  It can be thought of as 
N = ( b k  ' 2 9  + (bk-1 .2"-1) + * * * + (bl -21) + (bo * 20). 
Dividing both sides by 2, we get 
N 
b0 
2 
2 
- = (bk * 2k--1) + (bk-1 
* 2
9
 
+. 
* .  + (bl .2') + -. 
Hence, the rightmost digit in the binary representation, bo, is simply the 
remainder of the integer division of N by 2. We may think of N as 
N = 2 * Q + bo, 
where Q is the result of the integer division by 2. Repeating this step, we 
obtain all the digits of the binary representation. This suggests the algorithm 
whose MATLAB code is illustrated in figure 3.1. The function DecToBinary 

NATURE OF NUMERICAL COMPUTATION 
139 
function b=DecToBinary (n) 
nO = n; 
i=l ; 
while (no > 0) 
nl = floor(n0/2) ; 
b(i) = nO - nl*2; 
nO=nl ; 
i = i+l; 
end 
b=f liplr (b) ; 
Fig. 3.1 MATLAB code to obtain the binary representation of an integer number. 
takes an integer number n and returns a vector b containing the binary digits': 
>> DecToBinary(3) 
1 
1 
>> DecToBinary(8) 
ans = 
ans = 
1 
0 
0 
0 
>> DecToBinary(l3) 
ans = 
1 
1 
0 
1 
Similarly, the fractional part of a number is represented in a binary base as 
k=l 
Some numbers, which can be represented finitely in a decimal base, cannot in 
a binary base; for instance, 
7/10 = (0.7)10 = (0.10110)2. 
Clearly, in such cases the infinite series is truncated, with a corresponding 
error. The binary representation of a fractional number R can be obtained 
by the following algorithm, which is similar to the previous one (int and frac 
denote the integer and the fractional part of a number, respectively): 
1. Set dl = int(2R) and F1 = frac(2R). 
'This is not the best implementation, as the output vector b is resized incrementally. We 
could compute the number of necessary bits and preallocate b. 

140 
BASICS O f  NUMERICAL ANALYSIS 
2. Recursively compute dk = int(2Fk-1) and F k  = frac(2Fk-1) for k = 
2,3,. * .. 
Knowing how to change the base may seem useless, but we will see an ap- 
plication of these procedures in section 4.6, dealing with quasi-Monte Carlo 
simulation. 
In practice, we have to represent both quite large and quite small numbers. 
Hence we resort to a floating-point representation like 
2 = f q  x 2", 
where q is the mantissa and n is the exponent. The exact details of the 
representation depend on the chosen standard and the underlying hardware. 
In any case, since only a finite memory space is available to store the mantissa, 
we will have a roundoff error. 
Rounding off is not the only source of error in numerical computation. An- 
other one is truncation. This occurs, for instance, when we substitute a finite 
sum for an infinite sum. As an example, consider the following expression for 
the exponential function: 
O0 xk 
ex=C-. 
k! 
k=O 
When we truncate a sum like this, a truncation error occurs. 
Example 3.1 One typically troublesome situation is when you subtract two 
nearly equal numbers. To see why, consider the following example2: 
x = 0.3721478693 
y = 0.3720230572 
x - y  
= 0.0001248121. 
If you represent the numbers by five significant digits only (rounding the last 
one), the actual result will be 
2 - $ = 0.37215 - 0.37202 = 0.00013, 
with a relative error of about 4% with respect to the correct result. In fact, 
it is good practice to avoid expressions like 
& G i - l ,  
which could result in remarkable losses in significance for small values of x. 
In such cases, it is easy to rewrite the expression above as 
X 2  
[13, pp. 58-59] 

NATURE OF NUMERICAL COMPUTATION 
141 
Here there is no subtraction involved, but in other cases, there is no easy way 
to avoid the difficulty. 
[I 
3.1.2 
Roundoff errors have been mitigated by the increase in the number of bits 
used to store numbers on modern computers. From a practical perspective, 
numbers are virtually represented exactly. Nevertheless, such errors may ac- 
cumulate within the steps of an algorithm, possibly with disruptive effects, 
as we have seen in example 1.3. Hence, algorithms should be analyzed with 
respect to their numerical stability properties. We typically have alternative 
algorithms for the same problem, and it may happen that some of them are 
subject to instability issues and some are not. A typical case we will con- 
sider in chapter 5 is the choice between explicit and implicit methods to solve 
PDEs by finite differences. Sometimes, but not always, there is a trade-off 
between potential instability and computational efficiency. As an example, 
an advanced optimization library like ILOG CPLEX offers different interior 
point solvers to tackle large-scale linear programming problems3; in case of 
numerical difficulties we may switch to more robust but slower options. 
We see that stability is a property of a specific algorithm to solve a numer- 
ical problem. There is still another issue, which is related to the difficulty of 
solving the problem per se, which is called conditioning. When we consider 
the numerical conditioning of a problem, we are not dealing with specific al- 
gorithms to compute a solution, but with the intrinsic difficulty of a problem. 
Hence, it is important to have a conceptually clear view of how stability and 
conditioning are related. 
From an abstract point of view, a numerical problem may be considered as 
a mapping 
Error propagation, conditioning, and instability 
Y = fb), 
which transforms the input data x into the output y. An algorithm is a compu- 
tationally workable approach to computing that function; different algorithms 
may be used to solve the same numerical problem, possibly with different char- 
acteristics with respect to computational effort and stability properties. When 
using a computer, roundoff errors will be introduced in the representation of 
the input; we should check the effects on the output of a perturbation 6x in 
the input data. Denoting the actual input by Ir: = x + 62, the output should 
be f(lt.), whereas an algorithm will yield some answer, say y*. An algorithm 
is stable if the relative error 
31nterior point methods are dealt with in section 6.4.4. 

142 
BASICS OF NUMERICAL ANALYSIS 
is of the same order of magnitude as the machine preci~ion.~ 
By comparing f (3) with f(x), we analyze a different issue, called the condi- 
tioning of the numerical problem. We should compare the error in the output 
with the error in the input; when the input error is small, the output error 
should be small, too. Ideally, it would be nice to have a bounding relationship 
like 
where 11 
11 is an appropriate 
The number K is called the condition 
number of the problem. Later, we investigate the condition number for the 
problem of solving a system of linear equations, but a simple example will 
illustrate the point. 
Example 3.2 Consider the following non-linear equation: 
p(x) = x8 - 36x7 + 5 4 6 ~ ~  
- 4 5 3 6 ~ ~  
+ 2 2 4 4 9 ~ ~  
- 6 7 2 8 4 ~ ~  
+118124x2 - 109584~ + 40320 = 0. 
This is actually a specific type of non-linear equation, as it is a polynomial 
equation, and it can be solved by special purpose methods, one of which is 
implemented in the function roots6: 
>> pl=[ 1 -36 546 -4536 22449 -67284 118124 -109584 403203; 
>> roots(p1) 
ans = 
8.0000 
7.0000 
6.0000 
5.0000 
4.0000 
3.0000 
2.0000 
1.0000 
Note how the polynomial is represented by a vector containing its coefficients. 
We see a clear pattern in the solution. In particular, we have one root in 
the interval [5.5,6.5]. Now let us change the second coefficient from -36 to 
4T0 get an intuitive idea of what machine precision is about, consider the inequalities 
1 - E < I < 1 + E ,  which are obviously true for any E > 0. With computer arithmetic, 
there is a smallest E such that the inequalities hold; below that value, we cannot tell the 
difference between the two sides of the inequalities. 
5The reader should be familiar with the norm concept for vectors; anyway, it is recalled in 
section 3.2.1. 
6We have already met roots when computing the internal rate of return in example 2.8 on 
page 47. 

NATURE OF NUMERKAL COMPUTATlON 
143 
36.001. This is a small change in the problem data, and one would expect a 
corresponding slight change in the solution: 
>> p2=[ 1 -36.001 546 -4536 22449 -67284 118124 -109584 403201; 
>> roots(p2) 
ans = 
8.2726 
6.4999 + 0.7293i 
6.4999 - 0.7293i 
4.5748 
4.1625 
2.9911 
2.0002 
1.0000 
Some roots do not move that much, but now there is no root in the interval 
[5.5,6.5], and we have a pair of complex conjugate roots, instead. Note again 
that the conditioning issue is linked to the numerical problem itself, not to 
the specific algorithm used to solve it: With r o o t s  we are able to find a 
very good approximation of the solution, but this is significantly changed 
by a slight change in the problem data. Indeed finding the roots of a high- 
degree polynomial is an ill-conditioned problem, and you may imagine the 
potentially dramatic effects of errors in collecting empirical data to define a 
numerical problem. 
0 
Putting the two concepts together, we will find a "good" answer to a specific 
problem when the problem is well-conditioned and the algorithm is stable. 
3.1.3 
Sometimes, we are able to find a solution of a numerical problem directly by 
a relatively straightforward procedure. In other cases, we use iterative algo- 
rithms which generate a sequence of approximations. Given an approximate 
solution x ( ~ ) ,  
some transformation is applied to obtain an improved approx- 
imation x ( ~ + ' ) .  
The minimal requirement of a good algorithm is that the 
sequence generated converges to the correct solution x*. Furthermore, one 
would hope that such convergence is reasonably fast. The speed of conver- 
gence may be quantified by a rate. The rate of convergence is at least linear 
if there are a constant c < 1 and an integer N such that 
Order of convergence and computational complexity 
The rate of convergence is at least quadratic if there are a constant C and 
an integer N such that 
IlXn+l - x* 111 c 
IIXn - x* 
[ I 2 ,  
n L N .  

144 
BASICS OF NUMERICAL ANALYSIS 
In this case we do not require C < 1. This can be generalized to an arbitrary 
order of convergence a: 
IIX,+l--*IIICIIX,--*IIQ, 
n 2 N .  
The larger the rate q, the better; quadratic convergence (q = 2) is preferred 
to linear convergence (q = 1). An iterative method need not always converge. 
Sometimes, convergence depends on the initial estimate x(O) and its distance 
from the solution. 
When we use an iterative algorithm, we may have no precise idea of the 
number of iterations we need to get a satisfactory solution. In other cases, 
some direct method will yield the answer. By direct method we mean a pro- 
cedure which, after a known number of steps, gives the desired solution (if no 
difficulty due to instability arises). For direct methods, it may be possible to 
quantify the number of elementary operations (e.g., additions and multiplica- 
tions) needed to get the answer; this measures the computational complexity 
of the algorithm. The amount of computation will be a function of the size 
of the problem. The number of operations may depend on implementation 
details, and the size of the problem may depend on the type of encoding 
used to represent the problem. In practice, it is not necessary to be overly 
precise in this measure as it is usually enough to have an idea of the rate of 
growth of the computational effort with respect to the increase in problem 
size. Furthermore, the computational burden of running an algorithm may 
depend on the specific problem instance at hand, where by problem instance 
we mean a specific problem with specific numerical data. Sometimes, it is 
possible to analyze the average complexity with respect to the universe of 
problem instances. Usually, it is easier to quantify the worst-case complexity. 
Computational complexity issues are quite important for discrete optimiza- 
tion problems, as they must often solved by potentially time-consuming algo- 
rithms. 
Example 3.3 Consider again the knapsack model for capital budgeting, 
which was introduced in example 1.2. Since there is a finite set of possi- 
ble solutions, in principle one could find the optimal solution by enumerating 
all of them. However, since each project may or may not be financed, there 
may be up to 2N solutions, where N is the number of competing projects and 
is the essential measure of the problem size. This number is actually only an 
upper bound on the number of solutions, since many will be infeasible with 
respect to the budget constraint. Yet we may say that the worst-case com- 
plexity of complete enumeration is in the order of 2N [technically speaking, 
we say that the complexity is O(2N)].7 
0 
Clearly, an exponential growth like this is quite undesirable. Efficient algo- 
rithms are usually characterized by a polynomial growth of the computational 
7A function f(n) is O(g(n)) if limn+oo f(n)/g(n) < 00. 

SOLVING SYSTEMS OF LINEAR EQUATIONS 
145 
effort; their complexity is something like O(NP) for some constant p .  When 
we find a polynomial algorithm for an optimization problem, we say that the 
problem has polynomial complexity. However, if we cannot find a polynomial 
algorithm and only methods with worst-case exponential complexity are avail- 
able, does this mean that the problem has exponential complexity? Actually, 
this need not be the case: Maybe there is a polynomial algorithm, but we are 
not smart enough to come up with it. So, while considering the complexity of 
an algorithm may be relatively easy, doing that for a problem is not trivial in 
general. We wee here the same problem-algorithm duality that we have seen 
with stability and conditioning. 
3.2 SOLVING SYSTEMS OF LINEAR EQUATIONS 
The solution of systems of linear equations is an important problem per se; 
however, it is also instrumental for a variety of other problems. For instance, 
Newton's method for solving systems of non-linear equations calls for the 
repeated solution of linear systems (see section 3.4.2); in chapter 5 we will 
also see how solving linear systems is needed in certain methods to cope with 
PDEs. 
In pencil-and-paper mathematics, when we have to solve a system of linear 
equations like Ax = b, we use matrix inversion to get x = A-'b (provided 
the matrix is non singular). Although MATLAB offers a function, called inv, 
to invert a matrix, it may sound surprising to the newcomer that this is not 
used to solve systems of linear equations. More efficient approaches are used. 
It is not our aim to dwell too deeply on this subject; we limit ourselves to 
the basic concepts needed to understand what MATLAB offers to solve linear 
equations. Methods for solving linear equations can be broadly classified 
as direct or iterative. Direct methods have a clearly defined computational 
complexity, as they yield the result directly within a given number of steps; 
iterative methods build a sequence of solutions whose limit is (under some 
conditions) the desired solution. For iterative methods, the number of steps 
is not known a priori, as it depends on convergence speed. They are useful 
for some large systems characterized by sparse matrices (i.e., matrices with a 
small number of non-zero entries). Both classes are available in MATLAB, and 
there exist definite situations where application of one class is advantageous 
over application of the other. 
We have seen in example 1.3 that solving linear systems may be a difficult 
task with certain matrices. One would expect that when a matrix is close to 
singular, solving the related system may be numerically hard. While this is 
reasonably true, there are other reasons why numerical difficulties may arise. 
In order to see why, we need to analyze problem conditioning, which in this 
case amounts to consider the condition number of the matrix. Before doing 
so, we must introduce preliminary concepts related to the norms of vectors 
and matrices. 

146 
BASICS OF NUMERICAL ANALYSIS 
3.2.1 Vector and matrix norms 
We are all familiar with the concept of vector length in the Euclidean sense. 
The norm is a generalization of that idea, which can be extended to matrices 
and functions, and it is extremely useful in analyzing convergence, stability, 
and conditioning issues in numerical analysis. 
The vector norm is a function mapping vectors x E Rn to real numbers 
11 x 11 such that: 
0 Ilxll>OforanyxfO,and )IxII=Oifandonlyifx=O; 
0 IIcxI)=IclIlxl)foranyc~IW; 
I l x + Y l l I I l x l l + I I Y l l f o ~ a n Y x , Y ~ ~ n ~  
These properties are the intuitive properties a measure of vector length should 
satisfy. The most natural way to define a vector length is through the Eu- 
clidean norm 
However, there are different notions of vector length, which satisfy the condi- 
tions above for a vector norm. The most common ones are: 
0 11 x lloo = maxlliln 1 xi 
1, which is known as L1 norm; 
0 1) x 111 E C:=l I xi 1, which is known as L, norm. 
Generally speaking, one may define a vector L, norm as 
Letting p tend to infinity we get L, norm. 
Example 3.4 Vector and matrix norms are computed in MATLAB by the 
norm function. 
>> v = [2 4 -1 31; 
>> [norm(v,i) norm(v,2) norm(v,inf)] 
ans = 
10.0000 
5.4772 
4.0000 
The function takes two arguments: the vector and an optional parameter 
specifying the type of norm. The default value for the optional parameter is 
2. A call like norm(v,p) corresponds to 
sum(abs(v) .-p)-(l/p). 

SOLVlNG SYSTEMS OF LlNfAR EQUATIONS 
147 
The L, norm is computed when the value of the optional parameter is inf. 
0 
Example 3.5 Quite often we consider the norm of an LLerror.” In numerical 
analysis the error can be the distance between the solution of a problem and 
the current approximation in an iterative algorithm, or an error due to round- 
off or truncation. Most people in Finance and Economics are familiar with 
the idea of least squares. In the simplest setting, given a set of experimental 
data represented by pairs (xi, yi), i = 1, . . . , n, we look for a linear law like 
y = u + b x ,  
which fits the experimental data as best as possible. Since perfect fitting is 
impossible in practice, one defines an LLerrorll 
ei such that for each experimen- 
tal point yi = a + bxi + ei. Typically, the term residual is used rather than 
error, which in any case we would like to keep as low as possible. This can be 
accomplished by minimizing the norm 11 e )I of the residual by solving 
n 
s.t. 
yi = u + bx, + ei 
Vi. 
Taking squares makes sense in order to avoid compensation between positive 
and negative residuals, but we should wonder if there is something wrong in 
using alternative norms such as L1 and solving 
n 
i=l 
or, if we consider the L, norm, solving the min-max problem 
min { max Ieii}. 
The first case makes perfect sense, as it is related to plain average of residu- 
als in absolute value, whereas using Euclidean norm tends to penalize large 
errors a bit more. However, given the non-differentiability of absolute value 
as a function, minimization using the L1 norm requires numerical solution by 
linear programming, whereas the least squares problem has a straightforward 
analytical solution which paves the way to statistical interpretations in the 
case of linear regression. The L, norm makes sense when we are interested in 
controlling the worst-case deviation, rather than minimizing a measure related 
a,b 
i=l, ..., n 
to average residual. 
0 
A less familiar concept is the matrix norm, which can be defined by requir- 
ing the same properties as above. In the case of square matrices, the norm 
function maps RnXn 
to W. The required properties are: 

148 
BASICS OF NUMERICAL ANALYSIS 
0 IIAII>OforanyAfO,and IIAII=OifandonlyifA=O. 
0 ))cA(I =Ic(. IIAII for any c~ R. 
0 11 A + B )I I 11 A 11 + 11 B 11 for any A, B E Rnxn. 
Sometimes, the following additional condition is required: 
IIABII I IIAII . IIBII * 
It may also be important to connect vector and matrix norms. We say that a 
vector and a matrix norm are compatible if the following inequality holds: 
II A x  II SII A II II x II 
for any matrix A and vector b (note that in the left-hand side of the inequality 
we are using the vector norm). 
Typical matrix norms are: 
II A llca = max15i5n c;=, 
I aij I. 
II A 111 = maxl5jln CZl I aij I. 
0 11 A 112 = d m ,  
the spectral nom, where p(.) is the spectral radius 
The first two norms may look a bit weird, but they are easy to compute. In 
the first case, for each matrix row we sum absolute values of the elements in 
each column, and then we take the maximum over the rows. In the second 
case the two roles are swapped. 
Example 3.6 The norm function may be used to compute matrix norms as 
well. A call like 
of a matrix, i.e., p(B) = max{I X I ,  I: XI, is an eigenvalue of B}. 
> > A = [ 2 4 - 1 ; 3 1 5 ;  
- 2 3 - 1 1 ;  
>> [norm(A,inf) norm(A,l) norm(A,2) norm(A,’fro’)l 
ans = 
9.0000 
8,0000 
6.1615 
8.3666 
computes the four matrix norms we have defined, including the spectral and 
Frobenius norms. For the spectral norm, you may check the result by com- 
puting the square root of the eigenvalues of A‘A: 
>> sqrt(eig(A’ * A)) 
ans = 
2.2117 
5.2100 

SOLVING SYSTEMS OF LINEAR EQUATIONS 
149 
6.1615 
and picking up the largest value. 
0 
The Frobenius norm looks like a straightforward generalization of Euclidean 
vector norm, but the other three norms look somewhat unnatural. In fact, 
there is a natural way to introduce a matrix norm, given a vector norm. 
A square matrix may be considered as an operator transforming vectors: it 
rotates a vector and it changes its length, making it longer or shorter. We 
may consider the degree of “amplification” of the vectors as the norm of the 
matrix. Formally, given a vector norm, we may define its subordinate norm 
as 
In this case we also say that the matrix norm is induced by the vector norm. 
It is easy to see that in this case the two norms are compatible. Now it can 
be shown that the vector 1 1 .  Itrn norm induces the matrix 11 . lloo norm and that 
the same holds for the 11 . 111 norms. A surprising fact is that the Euclidean 
vector norm does not induce the Frobenius norm. In fact it is easy to see that 
the Frobenius norm is not a subordinate norm, by considering the identity 
matrix I: From (3.2) we should have IIIII = 1, but IIIIIF = fi, 
for a matrix 
of order n. The matrix norm induced by the Euclidean vector norm is the 
spectral norm, and this explains why it is denoted by 11.112 (see, e.g., [13]). 
A fundamental property of compatible matrix norms is the following. 
THEOREM 3.1 For any matrix norm that is compatible with a vector norm, 
we have 
P(A) 5 I1 All . 
The proof is straightforward. Given a pair of compatible vector and matrix 
norms, consider any eigenvalue X of A and let v be a related eigenvector of 
unit length, IIvII = 1. Then we have 
I 
1 = 1 1  XvII=Il Av I1 i l l  A IIII vII=II A II . 
Since this holds for any eigenvalue of the matrix, the theorem follows. 
3.2.2 
Condition number for a matrix 
Now we are ready to start analyzing the effect of numerical errors on the 
solution of a linear system. Consider the system 
A x = b  
and suppose that we perturb b by adding a term 6b; such a perturbation 
may indeed occur due to rounding off. Then the solution will somehow be 

150 
BASICS OF NUMERKAL ANALYSIS 
perturbed, too. We will have 
A(x + 6x) = b + Sb, 
which implies that 
We would like to assess the error in the solution, 6x, as a function of the input 
error 6b. If we adopt compatible matrix and vector norms, we may write 
II 6x II = II 
II b II = II Ax II L II A II * IIX II ' 
II 5 II A-l II . II 6b II 
Dividing term by term these two inequalities yields 
which is analogous to (3.1). The condition number K(A) 
A 11 . 11 A-' 11 
gives an upper bound on the ratio of the relative error in the solution to the 
relative perturbation. Generally speaking, the higher the condition number, 
the more difficult it is to solve a linear system. 
Example 3.7 The cond function computes the condition number. An op- 
tional parameter may be provided to select a norm; the default value corre- 
sponds to the spectral norm. 
>> cond(hilb(3)) 
ans = 
524.0568 
>> cond(hilb(7)) 
4.7537e+008 
ans = 
>> cond(hilb(l0)) 
ans = 
1.6025e+013 
Checking these numbers it is easy to see why solving a linear system involving 
the Hilbert matrix is a difficult task. 
Intuitively, we expect that a matrix which is close to singular will be difficult 
to deal with. The following theorem, due to Gastinel, somewhat supports this 
view. 
THEOREM 3.2 Let A a non-singular matrix of order n. 
subordinate matrix norm we have 
0 
Then for any 
1 - 
= min { 1' A - 
'1 1 B is a singular matrix 
cond(A) 
I1 A I1 

SOLVING SYSTEMS OF LINEAR EQUATIONS 
151 
The theorem basically states that when condition number is large, the matrix 
can be well approximated by a singular matrix, which may mean trouble 
when we deal with that matrix numerically. However, ill-conditioning is not 
necessarily related to singularity, as the following example clearly shows. 
Example 3.8 Consider the system8 
2 1 - 2 2 - 2 3 -  
...- 2 ,  = -1 
2 2 - 2 3 -  ...- 2, 
= -1 
2 3 -  ...-Ic, 
= -1 
.
.
.
 
Note that the matrix 
A =  
1 -1 
-1 ... -1 
-1 
0 
1 -1 
... -1 
-1 
0 
0 
1 ... -1 
-1 
.
.
 
.
.
 
.
.
 
0 
0 
0 ... 
1 -1 
0 
0 
0 ... 
0 
1 
is not singular, as det(A) = 1. We have 
b = [-1, -1, -1, . . . , -1, l]’, 
and the solution is easy to find by a process called “backsubstitution.” We 
see 2 ,  = 1. Then we may find xn-1 = 2 ,  - 1 = 0. Knowing x,-I, 
we find 
~
~
-
2
,
 
and so on. Using this strategy systematically, we get 
x = [O, 0, 0, . . ., 0, 1]T. 
We may also “verify” this using MATLAB: 
>> N=20; 
>> A = eye (N) ; 
>> f o r  i=l:N, for j=i+l:N, A(i,j) = -1;. end. end 
>> b=-ones(N,l); 
>> b(N,l) = 1; 
>> A\b 
ans = 
0 
‘See chapter 3 of E.A. Volkov, Numerical Methods, MIR Publishers, 1986. 

152 
BASICS OF NUMERICAL ANALYSIS 
0 
0 
0 
0 
0 
0 
0 
0 
0 
0 
0 
0 
0 
0 
0 
0 
0 
0 
1 
Now, assume that we apply a small perturbation to the right-hand side vector 
b, adding E to the last component. Then we should find a different solution. 
The first step of backsubstitution shows a small effect of this small perturba- 
tion: 
2, = 2, + 6x, = 1 + E. 
However, if we go on finding the remaining unknown variables, we see that 
the perturbation gets amplified: 
- 
>> b(N,1) = 1.00001; 
>> A\b 
ans = 
2,6214 
1.3107 
0.6554 
0.3277 
0.1638 
0.0819 
0.0410 
0.0205 
0.0102 
0.0051 
0.0026 
0.0013 
0.0006 
0.0003 
0.0002 
0.0001 
0.0000 

SOLVING SYSTEMS OF LlNEAR EQUATlONS 
153 
0.0000 
0.0000 
1.0000 
Thus, a negligible error in the input may result in a large error in the output. 
Please note that this is due to the structure of the matrix itself, even though it 
is not singular. We are facing a difficulty with the conditioning of the problem 
itself, not with stability. Indeed, we can try to figure out what's happening 
analytically. The error vector dx satisfies the system of equations: 
6x1 - 6x2 - 6x3 - . . . - 6xn = 0 
6x2 - 6 2 3  - ...- 6xn = 0 
6x3 -... -6x, 
= 0 
6xn-1-6xn 
= 0 
6xn = 
E .  
By backsubstitution we see 
In fact, 
>> cond(A, inf) 
ans = 
10485760 
>> 2-18 
ans = 

154 
BASICS OF NUMERICAL ANALYSIS 
262144 
>> 0.00001 * 2-18 
ans = 
2.6214 
3.2.3 
Direct methods for solving linear equations are based on the idea of trans- 
forming the matrix into a suitable form. Example 3.8, among other things, 
shows that if the matrix is in upper triangular form, we may immediately find 
the last unknown x, and then the other ones by backsubstitution. Let us 
make the approach explicit for a system 
Direct methods for solving systems of linear equations 
A x = b  
where A is an upper triangular matrix: 
~11x1 + ~ 1 2 x 2  + * * * + alnxn = bl 
~ 2 2 x 2  + * * * + a2nxn = b2 
. - .  
. - .  
annxn = b,. 
Backsubstitution starts from the last variable xn and proceeds backwards as 
follows: 
Now we should come up with a systematic method to transform a linear 
system of equations into an equivalent triangular form. Gaussian elimination 
is such a procedure. In principle, the idea is rather simple; we must form linear 
combinations of equations in order to eliminate some coefficients from some 
equations. Since combining equations linearly does not change the solution, 
the resulting system is equivalent to the original one. Starting from the system 
in the form 

SOLVING SYSTEMS OF LINEAR EQUATlONS 
155 
we may try to obtain a column of zeros under the coefficient a l l .  This is the 
first step in getting an equivalent triangular system. For each equation (Ek) 
(Ic = 2 , .  . . , n), we must apply the transformation 
which leads to the equivalent system: 
Now we may repeat the procedure to obtain a column of zeros under the 
coefficient a;;’, and so on, until the desired form is obtained, allowing for 
backsubstitution. 
Example 3.9 Consider the following system: 
1
2
1
 
-1 
-3 
0 
It is convenient to represent the operations of Gaussian elimination on an 
augmented matrix: 
-1 
-3 
0 2 
0 - 1 1 2  
From this it is easy to get z3 = 1, 2 2  = -1, and 2 1  = 1. 
0 
We will not quantify exactly the number of operations needed for the overall 
procedure, but it is evident that the algorithm has a quantifiable computa- 
tional complexity, which is of order O(n3) for a system of order n. 
Actually, what we have explained is only the starting point of Gaussian 
elimination, as many things may go wrong with this naive procedure. A first 
point is that we must have all # 0 to carry out the first step of the Gaussian 
elimination; by the same token, we must have a;:) # 0, and so on. Fortunately, 
if the original system is non-singular, this may be accomplished by a suitable 
permutation of variables (columns) or equations (row). 
Example 3.10 Consider the matrix 

156 
BASICS OF NUMERICAL ANALYSIS 
If we try Gaussian elimination to get rid of element a32 = 1, we are in trouble 
since a22 = 0. However, to avoid the difficulty, we may simply swap the 
second and the third equation. Formally, permutations may be represented by 
suitable matrices, called permutation matrices, characterized by the following 
properties: 
0 All elements are either 0 or 1. 
0 For each row, one element is equal to 1. 
0 For each column, one element is equal to 1. 
As an example, consider 
We may check the effect on matrix A: 
1
0
0
 
5
1
4
 
5
1
4
 
There is another reason why Gaussian elimination should include the pos- 
sibility of swapping rows or columns: Some care is needed to minimize the 
effects of finite precision arithmetic. We have seen in example 3.1 that sub- 
traction is a potentially dangerous operation, because of the potential loss of 
significance. Suitable row and column permutations may help in keeping the 
trouble to a minimum; such operations are called pivoting. Scaling the size 
of the coefficients may be used, too. These points are well treated in any 
numerical analysis book, and the details are beyond the scope of this one. 
There are alternative ways to see Gaussian elimination. A compact rep- 
resentation is obtained if we see Gaussian elimination as a way of factoring 
the matrix A into the product of a lower triangular matrix L and an upper 
triangular matrix U. More precisely we have 
PA = LU, 
where P is a permutation matrix which may be necessary or advisable to 
introduce for the above-mentioned reasons. We may try to understand, at 
least intuitively, where the above factorization comes from. The permutation 
matrix P corresponds to the pivoting operations; if pivoting is not required 
for a matrix, then this matrix can be neglected. The upper triangular matrix 
U corresponds to the end result of Gaussian elimination we just described. 
The lower triangular matrix L corresponds to the transformations we must 

SOLVING SYSTEMS OF LINEAR EQUATIONS 
157 
carry out to obtain the equivalent system in upper triangular form. These 
transformations are linear combinations of rows, which can be obtained by 
multiplying the original matrix by suitable elementary matrices; the matrix 
L is linked to the product of these elementary matrices. This factorization is 
called L U-decomposition. 
Example 3.11 LU-decomposition is obtained in MATLAB by calling the 
l u  function with a matrix argument. 
>> A = [I 4 -2 ; -3 9 8; 5 1 - 6 1 ;  
>> [L,U,PI = l u ( A )  
L =  
1.0000 
0 
0 
-0.6000 
1.0000 
0 
0.2000 
0.3958 
1.0000 
U =  
5.0000 
I .  0000 
-6.0000 
0 
9.6000 
4.4000 
0 
0 
-2.5417 
P =  
0 
0 
1 
0 
1 
0 
1 
0 
0 
With such a factorization, solving a system like Ax = b is equivalent to 
solving the two systems 
Ly = Pb 
ux = y 
in cascade. 
>> b = [1;2;31; 
>> x = A\b 
1.0820 
0.1967 
0.4344 
x =  
>> x = U \ ( L \ (P*b)) 
x =  
1.0820 
0.1967 
0.4344 

158 
BASICS OF NUMERICAL ANALYSIS 
7, TryLU.m 
N=2000; 
A=rand(100,100) ; 
t i c  
for i=1:1000 
b=rand(100,1); 
x=A\b; 
end 
toc 
t i c  
[L,U,Pl = lu(A); 
for i=1:1000 
b=rand(100,1); 
x=U\ (L\ (P*b) 1 ; 
end 
t o c  
Fig. 3.2 Script to check the advantage of using LU decomposition. 
LU-decomposition may be advantageous when it is necessary to solve a sys- 
tem repeatedly with different right-hand sides, as it occurs in the solution of 
certain PDEs by finite difference methods. In order to appreciate the point 
immediately, let us try a little experiment by running the MATLAB script in 
figure 3.2. In the example we generate a randomg matrix of order n = 2000 
and then solve 1000 systems with randomly generated right-hand sides. We 
may compare the CPU time with standard Gaussian elimination (cold start) 
and LU decomposition (warm start): 
>> TryLU 
Elapsed time is 0.904283 seconds. 
Elapsed time is 0.096623 seconds. 
Basically, with LU decomposition we obtain the same advantage we would 
have with matrix inversion, without all of its potential numerical difficulties. 
LU-decomposition takes a special form when applied to symmetric positive 
definite matrices; such matrices occur in many optimization problems, and a 
typical example is a covariance matrix. If A is a symmetric positive definite 
matrix, it can be shown that there exists a unique upper triangular matrix 
'The function rand generates a pseudo-random variable in the interval (0,l). It will be 
used extensively for Monte Carlo simulation. 

SOLVlNG SYSTEMS OF LlNEAR EQUATlONS 
159 
U such that A = U'U; this is called Cholesky factorization." 
Cholesky 
factorization may be a suitable alternative to the usual Gaussian elimination 
for special matrices. 
Example 3.12 The Cholesky factorization is computed in MATLAB by the 
chol function. For instance, let us define a matrix and check that it is positive 
definite, by verifying that its eigenvalues are positive: 
> > A = [ 3 1 4 ; 1 5 3 ; 4 3 7 1  
A =  
3 
1 
4 
1 
5 
3 
4 
3 
7 
>> eig(A1 
ans = 
0.3803 
3.5690 
11.0507 
Given a known term b, we may factor A and solve the system. 
>> b=(l : 3) ' ; 
>> U=chol(A) 
U =  
1.7321 
0.5774 
2.3094 
0 
2.1602 
0.7715 
0 
0 
1.0351 
>> U \ (U' \ b) 
ans = 
-1.0000 
-0.0000 
1.0000 
0 
In chapter 4 we will see that the Cholesky factorization is also useful when we 
have to simulate random variables with a multivariate normal distribution. 
3.2.4 
Tridiagonal matrices 
In certain applications, the matrix of a system of linear equations has a very 
specific form. One such case is the tridiagonal matrix, which may occur in 
the solution of option pricing problems by PDEs. A tridiagonal matrix has 
' O h  many texts, a lower triangular matrix L is considered, and the factorization is written 
as A = LL'. It is easy to see that the two definitions are actually equivalent. We will stick 
to this one, since the MATLAB function chol returns an upper triangular matrix. 

160 
BASICS OF NUMERICAL ANALYSIS 
the following form: 
A =  
0 
0 
0 
... 
all 
a12 
0 
0 
0 
a21 
a22 
a23 
0 
0 
0 
a32 
a33 
a34 
0 
0 
... ... 
0 
... ... 
0 
... ... 
... 
... 
an-Z,n-3 
an-2,n-2 
an-2,n-1 
0 
0 
an-1,n-2 
an-2,n-1 
an-1,n 
0 
0 
an,n--l 
ann 
This matrix has a banded form, and it is sparse; i.e., it has few non-zero 
entries. Without loss of generality, assume that ai,j+l # 0. If aj,j+l = 0, it is 
easy to see that the original system may be decomposed into two subsystems, 
since in such a case we have an upper block of lower triangular form. We may 
solve the system by a specially structured direct method. Consider the first 
equation: 
allxl + a1222 = b l .  
We may solve for 52, in terms of XI: 
where c2 = bl/alz and d2 = -a11/a12. By the same token, we may obtain an 
expression of 23 in terms of X I .  In fact, given the second equation 
we may express 23 as a function of 21 and 2 2 .  But since we know xg as a 
function of XI, we may get an expression of the form 
23 = ~3 + d 3 ~ 1 .  
Going on the same way for all equations up to the (n - 1)th one, we obtain 
expressions like X k  = Ck + d k x l ,  for all k = 2 , .  . . , n. Finally, plugging the 
expressions for xn-l and xn into the last equation, we end up with 
an,n-~xn-l + annxn = an,n-~(cn-l + d , - l x l )  + ann(cn + & X I )  = b,, 
which yields XI, and, by substitution, all the other unknowns. The approach 
may be adapted in the case of similar banded matrices. It is also worth noting 
that memory savings may be obtained by storing only the non-zero matrix 
entries. 
3.2.5 
In many situations we must solve a large system of linear equations, charac- 
terized by a sparse matrix. PDEs are a typical source of such systems, but 
Iterative methods for solving systems of linear equations 

SOLVING SYSTEMS OF LINEAR EQUATlONS 
161 
there are others, such as computing the long-term probability distribution of 
some discrete-state, discrete-time stochastic systems (Markov chains). Stor- 
ing a sparse matrix is a waste of memory, since many entries are zero; special 
techniques have been developed to avoid the problem. However, applying a 
direct method such as Gaussian elimination to a sparse matrix may destroy its 
characteristic. So we may try a different approach. One possibility is an iter- 
ative method, generating a sequence of vectors that converges to the solution 
desired. The process may be stopped when a reasonable accuracy has been 
achieved. Note that, unlike direct methods, the number of steps required by 
an iterative algorithm is not known a priori, and its behavior should be char- 
acterized in terms of convergence speed, along the lines illustrated in section 
3.1.3. The first issue to consider is how to characterize the conditions under 
which an iterative method converges; in fact, the method could simply blow 
up due to instability, giving rise to an unbounded sequence. 
Here we illustrate the basic iterative approaches described in any numerical 
analysis text. It is worth emphasizing that MATLAB has efficient capabilities 
to represent sparse matrices and provides the user with a rich set of iterative 
methods, which are much more sophisticated than the ones we describe here. 
Nevertheless, we believe that the background behind relatively simple itera- 
tive methods will be a useful reading, for at least a couple of reasons. On the 
one hand, they have been proposed in the literature on financial engineering to 
solve PDEs (see, e.g., [20, pp. 895-9011 for a comparison of LU-decomposition 
and successive overrelaxation in option pricing). Second, in chapter 5 we inves- 
tigate the numerical stability of finite difference methods for solving PDEs, 
using the same concepts we use here to study the convergence of iterative 
methods. 
Iterative schemes are one possible approach when the fixed point of an 
operator is needed. Consider a generic operator G(.) and assume that you 
want to find a fixed point of G, i.e., a point satisfying the equation 
x = G(x). 
A possible approach is to generate a sequence of approximations of the solu- 
tion, according to the iteration scheme 
(3.3) 
X(k+l) = G(x(k)) 
starting from some initial approximation x(O). This approach, called fixed- 
point iteration, may be used for both linear and non-linear equations, and for 
many other problems as well. Now the question is if and when this scheme 
will converge to a fixed point of G. The general answer lies in the contraction 
mapping concept, which is widely applied in many diverse settings. To keep it 
simple, let us investigate the idea in the case of the familiar system of linear 
equations Ax = b, which can be rewritten as 
x = (A +I)x - b = AX - b. 

162 
BASICS OF NUMERICAL ANALYSIS 
We want to find a fixed point of the operator G(x) = Ax - b, and we could 
consider the iterative approach (3.3). Would such a scheme converge? To be- 
gin with, consider starting from a first guess x(O), and trace the first iteration 
steps: 
x(l) = Ax(o) - b 
~ ( 2 )  
x(3) 
= A3x(0) - A2b - Ab - b 
= Ax(1) - b = A2x(0) - Ab - b 
... 
Intuition suggests that if the elements of the matrix An grow without bound 
as n .--t 00, the iteration scheme will diverge. Indeed, it can be shown that 
convergence will occur only if all the eigenvalues of A have an absolute value 
less than 1 (see below). Since this may well not be the case for an arbitrary 
system of equations, it is better to take a slightly different approach and split 
the matrix A as follows: 
A = D + C ,  
which yields an equivalent system 
DX = -CX + b. 
Then we may apply the iteration scheme 
d ( k )  = -Cx(k) + b  
(3.4) 
Dx(k++') = d(k) 
in order to generate a sequence of approximations x ( ~ ) .  
In some sense, this 
is a generalization of the previous fixed-point approach, but the flexibility 
in choosing D may be exploited to improve convergence. To investigate the 
convergence issue further, we may write, as before, 
X(k+l) = -D-lCx(k) + D-lb 
Letting B = -D-'C = I - D-lA, we may check how the absolute error 
e(k) = x* - x ( ~ )  
evolves, where x* is the correct solution: 
e(k+l) = x*-x('+l) = (Bx*+D-lb)-(Bx(k)+D-lb) = B(x*-x(k)) = Be(k) 
from which it is easy to see that 
lim e(') = lim Bke('). 
k-co 
k-co 
It can be shown that 
lim B~ = o 
k-co 

SOLVING SYSTEMS OF LINEAR EQUATIONS 
163 
if and only if the spectral radius of B is strictly less than 1, i.e., if all of its 
eigenvalues have an absolute value less than 1. This implies that the approach 
will converge if and only if 
P(I - D - ~ A )  < 1. 
To verify this condition, we should compute the eigenvalues of a possibly large 
matrix (actually, only the largest one in absolute value is needed). We may 
avoid this trouble by recalling that 
for any matrix norm compatible with a vector norm. Hence, we may settle 
the convergence question, in the sense of characterizing sufficient but not 
necessary conditions for convergence, by considering easily computable matrix 
norms such as 11 B ( ( 1  or 11 B [loo. 
From a practical point of view, the whole 
approach makes sense only if solving the linear equation (3.4) is easy. By a 
proper choice of D, we obtain the methods described in the following. 
Jacob; method A particularly convenient choice for D is a diagonal matrix: 
which is easily inverted provided that aii # 0; this condition may be obtained 
by proper row/column permutations if A is non-singular. Choosing L, norm, 
we obtain a sufficient condition for convergence: 
j#i 
which actually boils down to diagonal dominance, i.e., 
n 
j=1 
j #i 
To implement the method, we must rewrite the initial equations as 
1 
aii 
, 
i = l ,  ..., 12, 

164 
BASICS OF NUMERICAL ANALYSIS 
function [x, il = Jacobi (A, b ,xO, eps ,MaxIter) 
dA = diag(A); 
C = A - diag(dA); 
Dinv = diag( 1. /dA) ; 
B = - Dinv * C; 
bl = Dinv * b; 
oldx = x0; 
for i=l:MaxIter 
X get elements on the diagonal of A 
x = B * oldx + bl; 
if norm(x-oldx) < eps*norm(oldx) break; end 
oldx = x; 
end 
Fig. 3.3 Implementation of the Jacobi iterative method. 
which leads immediately to the iteration scheme 
The iterations should be stopped when a satisfactory precision has been 
achieved. One possible condition to check is related to relative error. Having 
specified a tolerance parameter E ,  we could stop the algorithm when 
11 X@+l) - X@) I/< E 11 
11 . 
Example 3.13 Jacobi method is easily coded in MATLAB, as illustrated 
in figure 3.3. Input arguments are matrix A and vector b of course, an 
initial approximation XO, convergence parameter E ,  and maximum number of 
iterations. The implementation is based on vector and matrices as preferred 
in MATLAB. Note the twofold use of the diag function; given a matrix, it 
yields the vector of its elements on the diagonal ; given a vector, it builds a 
matrix with the elements of the vector on the diagonal. 
To check jacobi, we may use the script of figure 3.4. Note that the first 
matrix is diagonally dominant; the second one is too, but to a lesser extent; 
the third one is not diagonally dominant. In the script, we compare the 
solution we get from the iterative method with the “correct” one obtained 
by Gaussian elimination; iterations are stopped after at most 10,000 steps. 
Please also note the use of the format string in fprintf (see online help). 
This is the output of the script. 
Case of matrix 

SOLVING SYSTEMS OF LINEAR EQUATIONS 
165 
% ScriptJacobi 
A 1 = [ 3 1 1 0 ;  1 5 - 1 2 ;  1 0 3 1 ; 0 1 1 4 ] ;  
A2 = [2.5 1 1 0 ;  14.1 -1 2; 1 0  2.1 1; 0 1 12.11; 
A3 = [2 1 1 0 ;  1 3.5 -1 2; 1 0 2.1 1; 0 1 1 2.11; 
b = [l 4 -2 11’; 
exactl = Al\b; 
[xl ,ill = Jacobi(Al,b,zeros(4,1) ,le-08,10000); 
fprintf(1, ’Case of matrix\n’); 
disp(A1) ; 
fprintf(1, ’Terminated after %d iterations\n’, 11); 
fprintf(1, ’ Exact 
Jacobi\n’); 
fprintf(1, ’ 2 -10.5g % -10.5g \n’, [exactl’ ; ~1’1); 
exact2 = A2\b; 
[x2, i2] = Jacobi (A2 ,b, 
zeros (4,l) , le-08,10000) ; 
fprintf(1, ’\nCase of matrix\n’); 
disp(A2) ; 
fprintf(1, ’Terminated after %d iterations\n’, i2); 
fprintf(1, ’ Exact 
Jacobi\n’) ; 
fprintf(1, ’ % -10.5g % -10.5g \n’, Cexact2’ ; ~2’1); 
exact3 = A3\b; 
[x3,i3] = Jacobi(A3,b,zeros(4,1) ,le-08,10000) ; 
fprintf(1, ’\nCase of matrix\n’); 
disp(A3) ; 
fprintf(1, ’Terminated after %d iterations\n’, i3); 
fprintf(1, ’ Exact 
Jacobi\n’) ; 
fprintf(1, ’ % -10.5g % -10.5g \n’, Lexact3’ ; ~3’1); 
Fig. 3.4 Script to check jacobi .m. 

166 
BASICS OF NUMERICAL ANALYSIS 
3 
1 
1 
0 
1 
5 
-1 
2 
1 
0 
3 
i 
0 
1 
1 
4 
Terminated a f t e r  41 iterations 
Exact 
Jacobi 
0.55556 
0.55556 
0.32407 
0.32407 
-0.99074 
-0.99074 
0.41667 
0.41667 
Case of matrix 
2.5000 
1.0000 
1.0000 
I. 0000 
4.1000 
-1.0000 
I .  0000 
0 
2.1000 
0 
1.0000 
1.0000 
Terminated a f t e r  207 iterations 
Exact 
Jacobi 
3.1996 
3.1996 
-2.7091 
-2.7091 
-4.2898 
-4.2898 
3.809 
3.809 
Case of matrix 
2.0000 
1.0000 
1 
* 0000 
1.0000 
3.5000 
-1.0000 
1.0000 
0 
2.1000 
0 
1.0000 
1.0000 
0 
2.0000 
1.0000 
2.1000 
0 
2.0000 
1.0000 
2.1000 
Terminated a f t e r  10000 iterations 
Exact 
Jacobi 
-42.808 
1.6603e+027 
47.769 
-1.8057e+027 
38.846 
-1.5345e+027 
-40.769 
1.5812e+027 
We see that convergence is faster in the first case than in the second, and 
that divergence occurs in the third case. This is no surprise, if we check 
the degree of diagonal dominance, but we should note that lack of diagonal 
dominance does not necessarily imply divergence. The reader is urged to 
check the spectral radius of matrix B in the three cases: 
p(B1) = 0.6489, 
p(B2) = 0.9257, 
p(B3) = 1.0059. 
It may also be interesting to check the speed of convergence by plotting the 
norm of relative error with respect to the true solution. To this aim we modify 

SOLVING SYSTEMS OF LINEAR EQUATIONS 
167 
function [x,i] = JacobiBIS(A,b,xO,eps,MaxIter) 
TrueSol = A\b; 
aux = norm(TrueSo1); 
Error = zeros (MaxIter ,1) ; 
dA = diag(A); 
C = A - diag(dA); 
Dinv = diag(1 ./dA) ; 
B = - Dinv * C; 
bl = Dinv * b; 
oldx = x0; 
for i=l:MaxIter 
% get elements on the diagonal of A 
x = B * oldx + bl; 
Error(i) = norm(x-TrueSol)/aux; 
if norm(x-oldx) < eps*norm(oldx) break; end 
oldx = x; 
end 
plot(l:i,Error(l:i)) 
~ 
~ 
fig. 3.5 Modifying Jacobi to plot residual. 
% ScriptJacobiBIS 
A 1 = [ 3 1 1 0 ;  1 5 - 1 2 ; 1 0 3 1 ; 0 1 1 4 1 ;  
A2 = C2.5 1 10; 1 4 . 1  -1 2; 1 0  2.1 1; 0 1 12.11; 
A3 = [2 1 10; 1 3 . 5  -1 2; 1 0  2.1 1; 0 1 12.11; 
b = [l 4 -2 11’; 
hold on 
[xl,il] = JacobiBIS(Al,b,zeros(4,1),le-08,10000); 
pause (3) ; 
[x2,i2] = JacobiBIS(A2,b,zeros(4,1),le-08,10000); 
pause (3) ; 
[x3,i3] = JacobiBIS(A3,b,zeros(4,1), le-08,10000) ; 
pause(3) ; 
axis(C1 100 0 21) 
Fig. 3.6 Script to tun JacobiBIS 
jacobi and the relative script as shown in figures 3.5 and 3.6. The resulting 
plot is displayed in figure 3.7. 
We see how important the spectral radius of matrix B is. In fact, later we 
discuss methods aimed at shifting its eigenvalues to speed up convergence. 
0 

168 
BASICS O f  NUMERICAL ANALYSIS 
Fig. 3.7 Error in Jacobi method. 
Gauss-Seidel method The Gauss-Seidel method is a variant of the Jacobi 
method. The idea is to use the updated values of xik+') immediately, as soon 
as they are computed. The iteration scheme is therefore 
i-1 
n 
b, - C aij x j  
(k+l) - c aijxj 
(k) 
(3-5) 
j=i+l 
$ + I )  
= 
j = 1  
, 
i =  1 ,..., 
72. 
aii 
To analyze convergence of this method, we may note that this corresponds to 
choosing as D the lower triangle of A: 
a11 
0 
0 
*.. 
0 
a22 
0 
D =  [ "i 
a:: 
'I' ] . 
Then it can be shown that diagonal dominance is again a sufficient condition 
for convergence: 
an1 
an2 
an3 
* * *  ann 
Speeding up convergence: successive overrelaxation Consider the iteration 
scheme 
X(k+l) = Bx(k) + d. 

SOLVING SYSTEMS OF LlNEAR EQUATIONS 
169 
Since we move from the current point x ( ~ )  
to the updated point x(lC+l), 
we 
may think of it as the addition of a displacement to the old approximation: 
,(k+l) = ,(k) + 
Even though this method will converge if p(B) < 1, convergence will be slow 
if the spectral radius of B is close to 1 (see example 3.13). We could try to 
speed up convergence by modifying the iteration: 
Intuitively, if dk) is a good direction, we might think of accelerating the 
movement by setting w > 1. We must make sure that a poor choice of w does 
not lead to instability. On the other hand, if the starting iteration is itself 
unstable, we might think that the difficulty stems from moving "too much" 
along the directions d'), which leads to oscillations and instability. In this 
case, we might think of dampening the oscillations with a suitable modification 
of the iteration scheme. To pursue this dampening, we may form a convex 
combination" of the new and the old point as follows: 
j p + U  = w X ( k + l )  + (1 - w)x(w 
= u(Bx(~) 
+ d) + (1 - w ) x ( ~ )  = B,x(~) + wd. 
(3.6) 
This is actually a convex combination if w E (0,l). It is worth noting that 
it looks like common exponential smoothing methods for time series analysis, 
where the aim is just to dampen oscillations in the estimates. The iterative 
scheme is stable if p(B,) < 1. Moreover, by a suitable choice of w ,  the spectral 
radius will be reduced, with a corresponding improvement in convergence 
speed. 
The reasoning above suggests that we may try to pursue modifications of 
the iterative approaches we have just described. For instance, we may try 
the idea on the Gauss-Seidel scheme. We may replace (3.5) by the following 
iteration: 
In order to analyze the effect of this modification, let us rewrite the Gauss- 
Seidel scheme in a compact form, based on the following decomposition of 
A: 
A = L + D + U ,  
"A convex combination of two points x1 and x2 is just a particular linear combination 
with nonnegative weights, such that their sum is 1: Ax1 + (1 - X)xz for X E (0, 
I]. 

170 
BASICS OF NUMERICAL ANALYSIS 
where 
0 
0 
... 
0
0
 
0 
0 
... 
0
0
 
0 
... 
0
0
 
a32 
0 
0 
0 
an-1,n-1 
0 
0 
0 
0 
... 
0 
ann 
a3,n-1 
a3n 
0 
... 
u
=
 I 0  0 
With this notation, the modified Gauss-Seidel scheme may be rewritten in 
matrix form as 
z(k+l) = D-l(b - Lx(k++l) - UX(k)) 
#+l) 
= wz(k+l) + (1 - W)X(k)* 
Eliminating z(~+') and rearranging yields 
(I + wD-'L)x(~+') = [(l- w)I - uD-'U]X(~) + wD-'b, 
which will be stable if 
p ((I + wD-lL)-l[(l - w)I - wD-lU]) < 1. 
This method is called SOR (Successive OverRelaxation) and by proper selec- 
tion of the parameter w, we may reduce the spectral radius of the matrix, 
thus improving convergence. 
Example 3.14 Figure 3.8 shows a possible implementation of successive 
overrelaxation, based on the Gauss-Seidel scheme. We may try to see the 
effect on convergence on the second matrix of example 3.13, which took 207 
steps to converge with the Jacobi method. We do so by plotting the number 
of iterations needed for convergence as a function of different values of w in 
the interval [0,2], which is obtained by running the script of figure 3.9. We 

SOLVING SYSTEMS O f  LINEAR EQUATIONS 
171 
function [x, k] = SORGaussSeidel(A, b,xO, omega, eps,MaxIter) 
oldx = x0; 
x = xo; 
N = length(x0); 
omega1 = l-omega; 
for k=l:MaxIter 
for i=l:N 
z = (b(i) - sum(A(i, (l:i-l))*x(l:(i-l))) 
. . . 
- sum(A(i,(i+l):N)*x((i+l):N))) 
/ A(i,i); 
x(i) = omega*z + omegal*oldx(i); 
end 
if norm(x-oldx) < eps*norm(oldx) break; end 
oldx = x; 
end 
Fig. 3.8 Implementation of SOR modification of Gauss-Seidel method. 
X ScriptSOR 
A2 = r2.5 1 1 0 ;  14.1 -1 2; 1 0  2.1 1; 0 1 12.11; 
b = [l 4 -2 11’; 
omega = 0:0.1:2; 
N = length(omega1; 
NumIterations = zeros(N,l); 
for i=l:N 
[x,k] = SORGaussSeidel(A2,b,zeros(4,1) ,omega(i) ,le-08,1000); 
NumIterations(i) = k; 
end 
plot (omega, NumIterations) 
grid on 
Fig. 3.9 Script to check SOR modification of Gauss-Seidel method. 
get the plot in figure 3.10. This shows the impact of w on speed of conver- 
gence. Actually] when the number of iterations exceeds the limit, we have 
divergence] since by playing with the relaxation parameter a stable case may 
result in instability and vice versa. With w = 1, we have the standard Gauss- 
Seidel approach, which requires 117 iterations; the best result, 49 iterations, 
is obtained with w = 1.4. 
0 
This example shows that finding the right value of the relaxation parameter is 
far from trivial, and in fact it is subject of quite some literature. For specific 
applications, there are strategies to estimate a good value for w. By the way, 

172 
BASICS OF NUMERICAL ANALYSIS 
200 
loo 
- 
- 
n 
“0 
0.5 
1 
1.5 
2 
Fig. 3.10 Number of iterations in modified Gauss-Seidel as a function of the relaxation 
parameter w. 
the careful reader may wonder why in 3.10 we considered values of w in the 
range [0,2]. In fact, it can be proved that this acceleration method cannot 
converge for values of w outside this interval. Finally, looking at equation 
(3.6) we may also guess why the method is actually called under-relaxation 
when w < 1, and overrelaxation when w > 1. 
The conjugate gradient method In MATLAB you will not find either Jacobi or 
Gauss-Seidel functions, as they are just the basic iterative methods to solve 
systems of linear equations. Some functions are related to an apparently 
weird approach to solving such systems, i.e., the solution of an optimization 
problem. In fact, solving the system Ax = b is equivalent to solving the 
optimization problem: 
min 11 Ax - b ( I 2 ,  
X 
where we are using Euclidean norm. Clearly, the objective function cannot 
be negative, and it will be zero for the solution of that system of equation 
(assuming it is unique). We may make the objective function more explicit: 
11 AX - b 
= (AX - b)’(Ax - X) = (x’A’ - b’)(Ax - b) 
= x’A’Ax - 2b’Ax + b’b, 
where the last term is actually irrelevant, as it is constant. We will see in 
chapter 6 that this is a quadratic programming problem (much like risk min- 
imization in mean-variance portfolio optimization), and it can be solved by a 
number of ways. The most general approach, as we will see, is based on the 
gradient of the objective function, which yields a search direction to maximize 
or minimize its value. 

FUNCTION APPROXIMATION AND INTERPOLATION 
173 
In general, there is no advantage in using this approach, but for the case of 
a symmetric positive definite matrix, it can be shown that solving the system 
of equations is equivalent to the following problem: 
1 
2 
min -x’Ax - b’x. 
The conjugate gradient method is based on a peculiar set of search directions, 
such that in theory the method would converge in a number of steps given 
by the order of the matrix. Hence, the method could be classified as a direct 
method. In practice, due to roundoff errors, this property does not hold and 
the method is considered as iterative. With recent improvements, conjugate 
gradient methods have become quite competitive for problems with specific 
structure. Such a structure occurs quite often in the numerical solution of 
PDEs. 
3.3 
FUNCTION APPROXIMATION AND INTERPOLATION 
There are several reasons why we need the ability to approximate a function. 
Sometimes, we know an expression of the function, but it is impossible 
or expensive to evaluate. A typical example is the standard normal 
distribution function 
/x 
e-y2/2 dy. 
1 
N ( 2 )  = - 
-m 
which occurs in the Black-Scholes pricing formula. 
More generally, we may be able to evaluate the function itself, but we 
need something different, like the integral of the function. An approxi- 
mation of the original function may be easier to integrate. 
Finally, there are situations in which the function is known or computed 
only at a discrete set of points (nodes), and we would like to find a 
suitable function which takes the same value (or a close one) at those 
nodes but can be evaluated outside this set. 
In some cases, it is enough to find a local approximation, in the neighborhood 
of a given point 50, in which case a Taylor expansion would suffice: 
f(2) M f(2o) + f’(zo)(z - 20) + $’(zo)(z 
1 
- d2 
+ . . . . 
We have seen such an idea in the duration-convexity approximation used for 
bond portfolio immunization and the delta-gamma approximation used with 
derivatives (see examples 2.10 and 2.24 on pages 59 and 113, respectively). 

174 
BASICS OF NUMERICAL ANALYSIS 
In this section, however, we are interested in an approximation valid over an 
extended range of values of the independent variable. 
Another criterion to classify approximation methods is based on the gen- 
erality of the approach. In the case of the cumulative function for the normal 
distribution, we may look for some ad hoc approximation. In other cases we 
look for more general strategies based on classes of approximating functions. 
A possible choice for the class of approximating functions is represented by the 
class of polynomials of given degree m; let Pm(z; a) denote such a polynomial, 
with coefficients represented by the vector a. One reason behind this choice is 
that polynomials are continuous functions, as well as their derivatives, which 
lend themselves to easy differentiation and integration. One possible metric to 
select the best approximation is the least squares approximation, whereby we 
try to minimize the average square deviation of the approximating function 
from f on a set of selected points zi, 
for which we know the value f(zi). The 
approximation problem can be stated as 
n 
Different objective functions could be used, basically corresponding to differ- 
ent ways of measuring the norm of the vector of the approximation errors. 
Another typical choice is the “min-max” metric, which is based on the )I . lloo 
norm: 
Sometimes, it is very useful to take a slightly more explicit view of function 
approximation. What we usually try to find, given a function f(x), is a 
suitable approximation expressed as a linear combination of a set of basis 
functions. If we consider a set of m basis functions &(x), j = 1,. . . , m, we 
want something like 
m. 
j = 1  
The basis functions may be polynomials, but there are alternatives. Finding 
the approximation means finding the m coefficients cj in the linear combina- 
tion. In function approximation by least squares, we have a set of n nodes 
at which we know the value of the function, and n > m. In this case, we 
have too few degrees of freedom, and we cannot enforce an exact match. In 
other words, we would like to find the approximation by solving a set of linear 
equations like 
m 
CCj4j(ZI) =f(zi), 
i =  l , . . . , n  
j=1 
or, in compact form, 
9 c  = y, 
(3.7) 

FUNCTlON APPROXlMATION AND lNTERPOLATION 
175 
where yi = f ( x i )  and 4ij = 4j(zi). Unfortunately, if n > m the system is 
overdetermined and it cannot be solved. What we can do is finding the least 
squares approximation, which requires the minimization of the sum of squared 
residuals ei, where 
m 
... 
ei = f(xi) - C cj$j(zi), 
i = 1,. . . , n. 
j=1 
Using relatively straightforward calculus, we can show that the least squares 
solution is 
c = (+'+)-1*'y. 
If, however, the number of nodes and the number of basis function is the same, 
m = n, then we may be able to find an exact match of the function values at 
nodes. We find the solution by enforcing the interpolation conditions: 
m 
3=1 
This process is called function interpolation and, within this framework, it 
leads to the solution of a system of linear equations. The following example 
will illustrate the difference between approximation and interpolation. 
Example 3.15 Say that we want to approximate/interpolate an increasing 
concave function, such as log(x). We are given a set of five nodes, which may 
be plotted as follows: 
>> xdata = [I 5 10 30 501; 
>> ydata = log(xdata1; 
>> plot (xdata,ydata, '0') 
>> hold on 
resulting in the plot of figure 3.11 We may try fitting a second-order polyno- 
mial, ax2 + bx + c. Note that this may correspond to selecting basis functions: 
41(z) = 1, 
42(.) = 2, 
43(x) = 2. 
This choice is referred to as the monomial basis, but a different set of poly- 
nomials could be used. Polynomial fitting, in the least squares sense, can be 
accomplished by the MATLAB polyf it function: 
>> p = polyfit(xdata,ydata,2) 
P =  
>> xvet=l:0.1:50; 
>> plot (xvet ,polyval(p,xvet)) 
This snapshot produces the plot in figure 3.12. The 
mial does not really pass through the data point, but 
-0.0022 
0.1802 
0.3544 
approximating polyno- 
this is expected, as the 

176 
BASICS OF NUMERICAL ANALYSIS 
Fig. 3.11 Data points (nodes) for example 3.15. 
I 2  
I 
' 0  
5 
10 
15 
20 
25 
30 
35 
40 
45 
Fig. 3.12 Fitting a second-order polynomial in example 3.15. 
number of nodes is larger than the set of coefficients in the polynomial. The 
trouble may be that, even if the fit is good, the approximating function is not 
monotonically increasing. If the logarithm is actually a utility function, we 
would require an increasing approximation which shows non-satiation. Since 
using a second-order polynomial is not that satisfactory, we could try increas- 
ing the order of the polynomial. We have five data points, and a fourth-order 
polynomial may result in exact polynomial interpolation. Note that the order 
of the polynomial is one less the number of nodes. To remember this, think 

FUNCTlON APPROXIMATION AND lNTERPOLATlON 
177 
6 
I 
0 
5 
10 
15 
20 
25 
30 
35 
40 
45 
50 
-1 ' 
Fig. 3.13 Interpolation in example 3.15. 
that there is one line (polynomial of order one) passing through two points. 
This is also easily accomplished in MATLAB: 
>> p = polyfit(xdata,ydata,4) 
P =  
>> plot (xvet ,polyval(p,xvet)) 
and we get the plot in figure 3.13. Now we do pass through the data points, 
which is nice, but there are spurious oscillations and the approximating func- 
tion is neither concave nor increasing, which is certainly bad for a utility 
function. In finance, we could have similar trouble when we try to define a 
term structure of interest rates fitted on the basis of a limited set of bond 
prices. Hence we see, that polynomial approximation and interpolation is not 
-0.0000 
0.0017 
-0.0529 
0.6705 
-0.6192 
that trivial. 
0 
Function interpolation and approximation is a vast sub-field of numerical anal- 
ysis. In the next sections we will just cover the essentials: an example of ad 
hoc methods is given in section 3.3.1; straightforward polynomial interpola- 
tion is the topic of section 3.3.2; cubic splines are introduced in section 3.3.3; 
section 3.3.4 deals with least squares approximation at a more general level. 
We should also mention that the methods we illustrate here can be extended 
to multivariate cases. 
3.3.1 Ad hoc approximation 
In this section we consider an example of ad hoc approximation by a rational 
function. While polynomials enjoy nice characteristics, sometimes approxi- 

178 
BASICS OF NUMERKAL ANALYSIS 
function z = mynormcdf(x) 
c = [ 0.31938153 , -0.356563782 , 1.781477937 , .. 
gamma = 0.2316419; 
vx = abs(x); 
k = l./(l+gamma.*vx); 
n = exp(-vx.^2./2) ./sqrt(2*pi); 
matk = ones(5,l) * k; 
matexp = (ones(length(x) ,1)*(1:5))’; 
matv = matk.-matexp; 
z = 1 - n.*(c*matv); 
i = find(x < 0); 
z(i) = l-z(i); 
-1.821255978 , 1.330274429 1; 
Fig. 3.14 MATLAB code to approximate the cumulative normal distribution. 
mations involving rational functions fit more nicely. For instance, there are 
various approximation formulas that can be used to evaluate the standard 
normal distribution function N ( x ) .  One is the following12: 
1 - N’(x)(alk + a2k2 + ask3 + a4k4 + ask5) 
1 - N (  -x) 
if x 2 0 
if x < 0, 
N ( x )  = 
where 
y = 0.2316419, 
a1 = 0.31938153 
a2 = -0.356563782, 
a4 = -1.821255978, 
a3 = 1.781477937 
a5 = 1.330274429. 
The MATLAB code for this function is shown in figure 3.14; it is a little 
involved, as we have made sure it can operate on vector arguments (as it should 
be the case with good MATLAB functions). This is not really the formula 
used in the equivalent MATLAB function normcdf, but we may compare the 
two approximations: 
>> normcdf([-1.5 -1 -0.5 0.5 1 1.53) 
ans = 
12This formula is proposed in [9, p. 2481. It is based on approximation 7.1.26 of the error 
function in [I], which in turn refers to (81. If you have some archaeological instinct, you 
may go further back in time. 

FUNCT/ON APPROXlMATlON AND lNTfRPOLATlON 
179 
0.0668 
0.1587 
0.3085 
0.6915 
0.8413 
0.9332 
>> mynormcdf([-l.5 -1 -0.5 0.5 I 1.51) 
ans = 
0.0668 
0.1587 
0.3085 
0.6915 
0.8413 
0.9332 
3.3.2 
Elementary polynomial interpolation 
We consider here elementary interpolation by polynomials of sufficient degree. 
Let us consider aset ofsupport points (xi, y i ) ,  i = 0,1,. . ., n, where yi = f ( x t )  
and 2% # xi for i # j .  It is easy to find a polynomial of degree (at most) n 
such that P,(xi) = yi for any i. We may rely on the Lagrange polynomials 
Li(x), defined as 
n 
xi - xj 
j = O  
i#i 
Note that these are polynomials of degree n and that 
1 i f i = k  
Li(xk) = { 0 otherwise. 
Now an interpolating polynomial can be easily written as 
n 
i=O 
In practice, no one should use this form for computational purposes, and 
some tricks are needed for the sake of computational efficiency, but the idea 
is hopefully clear. 
Example 3.16 We consider here the interpolation of a set of ten data points. 
We may try interpolating them by a polynomial of degree 9: 
>> x=1:10; 
>> y = [8 2.5 -2 0 5 2 4 7 4.5 21; 
>> plot(x,y,’o’) 
>> hold on 
>> x2=1:0.05:10; 
>> p=polyfit(x,y,g); 
Warning: Polynomial is badly conditioned. 
data points or try centering and 
in HELP POLYFIT. 
>> plot (x2,polyval(p,x2)) 
Remove repeated 
scaling as described 
We get some warning from MATLAB, which we disregard for a moment. The 
result is shown in figure 3.15. We may see that the polynomial passes through 
the data set but, unfortunately, we also see that the interpolating polynomial 

180 
BASICS OF NUMERICAL ANALYSIS 
' 7  
12, 
-6- 
' 
I 
1
2
 3 
4 
5 
6 
7 
8 
9 
10 
Fig. 3.15 Interpolating a given data set by a polynomial of degree 9. 
has some undesirable oscillation behavior near the end points of the interval. 
This is not surprising: a polynomial of degree n may have up to n zeros, which 
means it may have up to n - 1 local minima and maxima and oscillations are 
to be expected. 
0 
The oscillation of high-degree interpolating polynomials is a typical diffi- 
culty, and there are a few ways to try overcoming it. One obvious way is to use 
more sophisticated functions, for both approximation and interpolation. But 
actually there is still another basic mistake we are doing in the last example: 
we did a poor choice in selecting nodes. In selecting nodes over an interval 
[a, b], the natural choice is taking evenly spaced ones: 
This choice may have nasty effects in itself. It turns out that a better choice 
is given by Chebyshev nodes: 
a f b  b - a  
xz = - 
+ -cos 
(" - + 0.5r) , 
i = 1,. . .,n. 
2 
2 
n 
An investigation of why this seemingly odd choice is an improvement over 
a naive placement of nodes goes beyond the scope of this book, but we will 
illustrate the effect with a typical example. 
Example 3.17 We consider polynomial interpolation for a well-known func- 
tion, called Runge function: 
1 
1 + 25x2 

FUNCTlON APPROXlMATlON AND /NT€RPOLATlON 
181 
% RungeScript.m 
1 define inline function 
runge = inline(’l./(l+25*x.*2) ’1; 
1 use equispaced nodes 
EquiNodes = -5:5; 
peq = polyf it (EquiNodes, runge (EquiNodes) ,101 ; 
figure 
plot(x,runge(x)); 
hold on 
plot (x ,polyval(plO,x) 1 ; 
% use Chebyshev nodes 
ChebNodes = 5*cos(pi*(ll - (1:11) + 0.5)/11); 
pcheb = polyfit (ChebNodes,runge(ChebNodes) ,101 ; 
figure 
plot(x,runge(x)> ; 
hold on 
plot(x,polyval(pcheb,x)); 
~=-5:0.01:5; 
Fig. 3.16 MATLAB script for example 3.17 
over the interval [ - 5 , 5 ] .  As we mentioned, a seemingly obvious and natu- 
ral choice is to place equally spaced interpolation nodes, for instance xi = 
-5, -4, -3,. . . , 4,5. These are eleven nodes, and we may try interpolating by 
a polynomial of degree ten. 
Straightforward interpolation is accomplished by the MATLAB script in 
figure 3.16. Selecting equally spaced nodes results in the first plot, depicted 
in figure 3.17. We see the usual oscillation near the end points, but in this 
case the behavior looks really pathological. The reader is invited to verify 
that increasing the order of approximation only makes things worse. If we use 
Chebyshev nodes, which is done in the second half of the script, we get the 
result in figure 3.18. While the result is not yet satisfactory, at least it looks 
a bit less pathological. 
0 
Even though choosing Chebyshev nodes helps in the last example, there 
is still something wrong with the quality of the approximation we get by 
interpolating with one high-degree polynomial. Using the right nodes, we 
may try increasing the order of the polynomial, but there is an easier way 
out: using piecewise polynomial functions. A look at figure 3.18 suggests that 
there are regions in which the function is essentially zero, and we should use 
a different approximation there. Using piecewise polynomial interpolation is 
pursued in the next section on splines. 
We close the section here by noting that we have still another issue when 
using simple-minded polynomial interpolation. Consider again the basis func- 

182 
BASICS OF NUMERICAL ANALYSIS 
Fig. 3.1 7 
-0.5 
1 
-5 
0 
5 
nodes. 
Fig. 3.18 Polynomial interpolation for Runge function: Chebyshev nodes. 

FUNCTION APPROXIMATION AND INTERPOLATION 
183 
tion framework. If we want polynomial approximation or interpolation, the 
monomial basis (1, x, . . . , xn-l) is the natural choice when selecting basis 
functions. However, this may lead to a badly conditioned matrix @ in equa- 
tion (3.7), along with a few numerical difficulties. In fact, several alternative 
families of polynomials have been proposed to avoid them. Since we men- 
tioned Chebyshev nodes, we should at least mention in passing Chebyshev 
polynomials, which are recursively defined as follows: 
To(.) 
= 1 
Ti(x) = 
X 
T2(x) = 2x2 - 1 
T3(2) = 4x3-3x 
Tn(x) = 
2ZT,-l(S) - Tj-2(2). 
. . .  
(3.9) 
3.3.3 
Interpolation by cubic splines 
One possible way to avoid oscillating polynomials in function interpolation is 
resorting to low-degree polynomials, interpolating the data points piecewise. 
The simplest idea is to use piecewise linear interpolation. Given the N + 
1 nodes (or knots) (xi, 
yi), we may use N first-degree polynomials Si(z), 
each one valid on the interval (xi, 
xi+l). An obvious requirement is that the 
resulting function is continuous, i.e., Si(xi+l) = Si+l (xi+l). Recalling the 
Lagrange polynomials defined in equation (3.8), we have 
This type of interpolation is called linear spline. Whereas the interpolat- 
ing function is continuous, its derivative is not, which may have undesirable 
consequences. If the data we are interpolating are prices of an asset as a 
function of an underlying factor, non-differentiability prevents the estima- 
tion of sensitivities. If we are approximating a function which must then be 
optimized, as is the case with the value function in dynamic programming, 
non-differentiability is clearly a complication. 
We may enforce the continuity of the derivatives of the spline by increas- 
ing the degree of the polynomials. The most common spline is obtained by 
“joining” N third-degree polynomials Si (x), with coefficients sio, sil, si2, si3, 
which must satisfy the following requirements: 

184 
BASICS OF NUMERICAL ANALYSIS 
Si(xifl) = Si+l (xi+l), 
i = 0,1,. . ., N - 2 
S,’(ZZ+l) 
= s;+l(xz+l), 
i = O , l , .  . ., N - 2 
s;/(xi+1) = s;+l 
(ZZ+l) 
i = 0,1, . . . , N - 2. 
The resulting spline S(x) is called a cubic spline. The condition above re- 
quire continuity for the spline itself and for its first and second derivatives. 
To specify a spline, we must give 4N coefficients. Passage through the sup- 
port points gives N + 1 conditions; the continuity of the spline and the two 
derivatives enforces 3(N - 1) conditions, yielding a total of 4N - 2 conditions. 
Hence, we have two degrees of freedom which may be eliminated by enforcing 
further requirements. Usually, they involve some conditions at, or near, the 
end points xo and X N .  Among the most common conditions, we recall the 
following ones: 
0 S”(x0) = S”(ZN) 
= 0, which leads to natural splines. 
0 S’(x0) 
= f’(z0) and S’(ZN) 
= ~ ’ ( x N ) ,  
which may be used if we have a 
precise idea of the behavior of f (x) near the end points. 
0 The not-a-knot condition, which is obtained by requiring that the third- 
order derivative s”’(~) 
be continuous in x1 and zjv-1. This implies that 
S(x) would be a spline for knots x o , x 2 , 2 3 , .  . . , X N - 2 ,  ZN, but it would 
interpolate through x1 and XN-1 too (hence the name). 
We should note that these conditions are symmetric with respect to the end 
points of the interval; actually we could make different choices for the two end 
points. It is also interesting to note that we have no degree of freedom in linear 
splines; in the case of splines of degree 2, we would have one degree of freedom, 
with a corresponding asymmetry in end points. Despite the appealing name, 
natural splines are usually avoided. Their importance stems from the following 
theorem, which we state without pr00f.l~ 
THEOREM 3.3 Let f“ be continuous in (a, b) and let a = zo < 2 1  < . . . < 
XN = b. If S is the natural cubic spline interpolating f on the knots xi, then 
[[S”(z)]’ 
dx I Jd [f”(x)]’ dx. 
b 
The importance of this theorem can be understood by recalling that the 
curvature of the curve described by the equation y = f (x) is given by 
I f”(5) I . { 1 + f ’ ( x ) 2 } - 3 ’ 2 .  
If f’ is sufficiently small, we see that I f”(x) I approximates the curvature; 
hence, the natural spline is, in some sense, an approximation of minimal 
13See, e.g., [13, pp. 380-3811. 

FUNCTION APPROXIMATION AND INTERPOLATION 
185 
1 
1
2
 3 
4 
5 
6 
7 
8 
9 
10 
fig. 3.19 Interpolating a given data set by a cubic spline. 
curvature over the interval (a, b). When nothing is known about the function, 
the not-a-knot condition is the recommendable choice; in fact, this is the 
default option in MATLAB. 
To find the unknown coefficients, we have to set up a system of linear 
equations; the details are a bit tedious, and since they are implemented in a 
ready-to-use MATLAB function, they are omitted. Yet it is interesting to note 
that for most choices of free conditions, the resulting system has a tridiagonal 
form like that discussed in section 3.2.4; furthermore, it is symmetric and 
diagonally dominant, hence it is particularly easy to solve. 
Splines are so important that an entire MATLAB toolbox is devoted to 
them. In the base MATLAB system, you have two functions that may be 
used for cubic spline interpolation. One is interpl, provided that you call it 
with the parameter 'spline'; the other one is spline. 
Example 3.18 Let us compare the interpolation we obtain for the cases 
we have already discussed in examples 3.16 and 3.17. Running the following 
script, we get the result in figure 3.19: 
x=l: 10; 
y = [8 2.5 -2 0 5 2 4 7 4.5 21; 
plot(x,y, '0') 
hold on 
x2=1:0.05:10; 
y2=interpi(x,y,x2, 'spline') ; 
plot(x,y, 'o',x2,y2); 
We see that spurious oscillations are avoided. The same result is obtained by 
calling spline, which also returns a spline object; this object may be used 
for later evaluations by the function ppval: 

186 
BASKS OF NUMERICAL ANALYSIS 
% RungeSp1ine.m 
% define inline function 
runge = inline ( ’ 1. / (1+25*x. -2) ’1 ; 
1 use 11 equispaced nodes 
EquiNodesll = -5:5; 
ppeqll = spline(EquiNodesl1 ,runge(EquiNodesll)) ; 
subplot (3,1,1) 
plot (x, runge (x) 1 ; 
hold on 
plot(x,ppval(ppeqll,x)); 
axis([-5 5 -0.15 11) 
title(’l1 equispaced points’); 
% use 20 equispaced nodes 
EquiNodes20 = linspace(-5,5,20) ; 
ppeq20 = spline (EquiNodes20 ,runge(EquiNodes20)) ; 
subplot (3,1,2) 
plot (x, runge (x) ; 
hold on 
plot(x,ppval(ppeq20,x)) 
; 
axis([-5 5 -0.15 11) 
title(’20 equispaced points’); 
% use 21 equispaced nodes 
EquiNodes21 = linspace(-5,5,21); 
ppeq21 = spline (EquiNodes21 ,runge(EquiNodes2l)) ; 
subplot(3.1,3) 
plotCx,runge(x)); 
hold on 
plot (x , ppval (ppeq21, x) 1 ; 
axis( 1-5 5 -0.15 11 1 
title(’21 equispaced points’) ; 
~=-5:0.01:5; 
Fig. 3.20 MATLAB script to interpolate Runge function by cubic splines. 
x=l : 10; 
plot(x,y, ’0’) 
y = [8 2.5 -2 0 5 2 4 7 4.5 21; 
hold on 
pp=spline (x, y) ; 
x2=1:0.05:10; 
y2 = ppval(pp,x2); 
plot(X,yJ’oJ,x2,y2); 
We may also check the result with the Runge function. Running the script 
of figure 3.20 we get the plots in figure 3.21. We may notice that using 21 

FUNC TION A P P ROXI MA TI0 N AND IN T f  RP 0 LA TI0 N 
1 8 7 
11 equispaced points 
-5 
0 
20 equispaced points 
5 
-5 
0 
21 equispaced points 
5 
I 
I 
-5 
0 
5 
Fig. 3.21 Interpolating Runge function by a cubic spline. 

188 
BASICS OF NUMERICAL ANALYSIS 
points rather than 11 improves the approximation, whereas an even number 
of points result in a very poor match near the maximum. The approximation 
is still not satisfactory: the reader is urged to try placing nodes in points 
-5, -3,3,5 and distributing 17 nodes on the interval [-2,2]. 
0 
As we have pointed out, in MATLAB the default way to define the two degrees 
of freedom in cubic splines is the not-a-knot condition. But if you provide the 
function spline with an y vector with two more components than the vector 
x ,  the first and last components are used to enforce a value for the spline 
slopes at the extreme points of the interval. 
Cubic splines are only the basic type of spline; many more have been pro- 
posed. A typical application in finance is in estimating term structures of in- 
terest rates given a limited set of market data related to bond prices (see, e.g., 
[3], [4], 
and the references therein). In economics, shape-preserving splines are 
sometimes used, which make sure that the resulting spline has certain quali- 
tative features which are essential from an economical point of view. 
3.3.4 
This section is somewhat more theoretical, and basically aims at providing a 
more general and abstract framework for function approximation. The basic 
concept we use here is a generalization of orthogonality between vectors. We 
should start with a general formulation of the best approximation problem. 
We are given a normed linear space E and a subspace G of E. By “normed” 
we mean that the objects in that space have an associated norm (e.g., the 
vector norms we have discussed in section 3.2.1); by “linear” we mean that 
by taking any linear combination of objects in G or El we get another object 
in that set. 
Given a norm, we may define distances between arbitrary objects in the 
space. The distance between two elements f, g E E is simply given by 11 f -g [I. 
More generally, the distance off E E from the subspace G is defined by 
Theory of function approximation by least squares 
dist(f, G) = inf I( f - g [I . 
gEG 
An interesting specific case occurs when we have an inner-product space, 
whereby norm is based on the inner product defined on the space: 
Ilfll= d< f,f >. 
< X , Y  > = C x i Y i ,  
Typical examples of inner products are 
n 
i=l 
for x,y E R”, and 
(3.10) 

FUNCTlON APPROXlMAT/ON AND lNTERPOLATlON 
189 
for f,g E C(a, b), i.e., the space of continuous functions on the interval (a, b). 
We say that two elements f, g E E are orthogonal (denoted by f l g )  if 
< f,g > = 0. 
We say that a finite or infinite sequence of elements f1, f2, f3,. . . E E is an 
orthogonal system if 
Furthermore, if all elements in the subset have unit norm, we say that the 
system is orthonormal. 
< fi, f j  > = 0 
Vi # j .  
Example 3.19 The following polynomials: 
2
1
 
pz(x) = x  - - 
3 
3
3
 
p3(x) = x - -x 
5 
4
6
 
3 
p4(x) = x - -x2 + - 
7 
35 
form an orthogonal system, on interval [-1,1], if the inner product 
1 
<f,s>=S_lf(x)g(x)dx. 
They are the first polynomials in the family of Legendre polynomials. Simi- 
larly, the Chebyshev polynomials defined in (3.9) form 
with respect to the inner product: 
an orthogonal system 
Actually, there are general strategies to build orthogonal systems, which will 
be outlined in section 4.1.2. 
We should also mention that orthogonal systems of random variables can 
also be built. The idea, said very roughly in financial terms, is to decompose 
risk (a random variable) into the sum of uncorrelated sources of risk, each one 
carrying a piece of information in such a way that redundancy is avoided and 
a simple representation of risk is obtained. 
The fundamental result of approximation in a normed space is that, if the 
space is equipped by an inner product, there is an equivalence between the 
two conditions: 
1. g is a best approximation to f in G. 

190 
BASKS OF NUMERICAL ANALYSIS 
Z 
T 
Fig. 3.22 Orthogonal projection. 
2. The residual is ortliogonal to the subspace: f - g I 
G. 
This is again it generalization of the familiar geometric concept of orthogonal 
projection in Euclidean spaces (see figure 3.22). If we have a vector in the 
(z, y, z )  space, and we want to find the closest vector on the (2, 
y) plane, we do 
an ortliogonal projection. The following example shows how this equivalence 
can he exploited. 
Example 3.20 Consider the space E = C(0,l) of continuous functions over 
interval (0, l), and assume that we want to find an optimal approximation (in 
thc least-squares sense) in the subspace G consisting of polynoniials of degree 
n. We niay build the linear subspace G by using monomials g)(~c) = z’. 
J = 0,1,. . ., n, as the basis. Thus, g(z) = ~ ~ = o u J g J ( x )  
= C ~ = o u J z J .  
We 
want t,o minimize thc deviation 
If f - g is ortliogontil to G, then we must require 
or, in other words, 
11 
x u . ,  < gj(x),g7(x) > = < f1s1(x) >, 
i = 0,. . .,n. 
3 =o 
In ow case, this yields a set of linear equations: 

SOLVING NON-LINEAR EQUATIONS 
191 
These equations are collectively called the normal equations. Unfortunately, 
the matrix of coefficients includes definite integrals evaluating to 
But this is the (dreaded) Hilbert matrix that we already met in example 1.3 
on page 18. 
0 
The example shows that a simple-minded approach may lead to ill-condition- 
ed numerical problems. Proper selection of the basis functions is fundamental 
from the numerical point of view, and this is why families of orthogonal poly- 
nomials are often used. 
We have so far considered the continuous least squares problem, in order to 
motivate the introduction of orthogonal polynomials. Typically, in numerical 
applications, we have to solve a discrete problem in which a set of n data 
points (xi,yi), i = 1,. . .,n, 
is given, where yi = f(xi), and we look for an 
approximation in terms of a linear combination of m basis functions (e.g., 
polynomials). Using the Euclidean norm, as we have already seen, we get the 
ordinary least squares problem: 
In this case the normal equations (or ordinary calculus) yield 
c = (@'@)-l@'y. 
In this case too, solving the normal equations may be easier with a proper 
selection of basis functions. In chapter 10 we will see an application of lin- 
ear regression with polynomials to pricing American options by Monte Carlo 
simulation. 
3.4 
SOLVING NON-LINEAR EQUATIONS 
Solving non-linear equations is a common task in finance; the most elementary 
example is the computation of the internal rate of return (see example 2.8 on 
page 47), which calls for finding the roots of a polynomial. A polynomial 
equation is a particular case of general non-linear equations, and it is a very 
lucky case, in the sense that we are typically able to find all of the roots of 
the equation by specific methods. For instance, if we consider 
x3 + 3x2 - 2x2 + 4 = 0. 
we may use the MATLAB r o o t s  function and get 

192 
BASICS OF NUMERICAL ANALYSIS 
Fig. 3.23 Exairiple of the bisection method. 
>> roots([l 3 -2 41) 
ans = 
-3.8026 
0.4013 + 0.94393. 
0.4013 - 0.9439i 
In general we must settle for one root near some prespecified point. 
as 
or a system of equations in several variables, such as 
You might wish to find a solution of' an equation in a single variable, such 
f(x) = 0 
F(x) = 0. 
MATLAB offers different functionalities to this purpose. We first outline 
the l m i c  features of numerical methods for non-linear equations, limiting the 
treatment to bisection and Newton methods. 
3.4.1 
Bisection method 
The bisection method is the simplest method for solving the scalar equation 
f (x) = 0 
without requiring anything more than the ability to evaluate, or estimate, the 
funct,ion f at, a given point. This is an important feature; since in some cases 
we do not even have an analytical expression for the function f ,  and there- 
fore we are riot able to apply more sophisticated methods such as Newton's 
nietliod, which calls for computation of the derivative of f .  Suppose that we 
know two points a, b (u < b) such that f ( a )  < 0 and f ( b )  > 0. Then, if the 
function is continuous, it is obvious that it must cross the zero axis somewhere 
in the interval [a, b] (see figure 3.23). The same observation holds if the signs 
of the function in a and b are reversed. So [a, b] is an interval encapsulating 
a root of the equation. Then we may try to reduce this interval by checking 
the sign of f in the midpoint of the interval, i.e., 
a + b  
2 
c =  -. 

SOLVING NON-LINEAR EQUATIONS 
193 
If f ( c )  = 0, possibly within some prespecified tolerance, we are done. If 
f ( c )  < 0, we may conclude that a zero must be located somewhere in the 
interval [c, b]; otherwise, the interval to check is [a,c]. Going on this way, we 
build a sequence of smaller and smaller intervals bracketing the zero. Formally, 
you generate a non-decreasing sequence a, and a non-increasing sequence b, 
such that: 
where r is the (unknown) root and c, = (b, + an)/2. It can be shown that 
this method is characterized by a linear convergence rate. 
The method, as usual, will not really find the exact root (in general), but 
only a suitable approximation. Furthermore, we should define some termina- 
tion criteria to stop the algorithm. Possible choices are 
maximum number of iterations 
There is no best criterion and for a robust algorithm we must use all of them. 
Actually, the second one may depend on the chosen units of measure: by 
scaling the equation, this criterion may be met by any point. It is advisable 
to restate the criterion in relative terms. 
Example 3.21 Consider a typical problem in Microeconomics. We want to 
find the price p such that supply S(p) of some item equals demand D(p). What 
we are looking for is a zero of the excess demand function f(p) = D(p) - S(p). 
Asking for I f(p) I< E is a bit arbitrary, as we have said. A better termination 
test could be I D(p) - S(p) I< 6D(p), i.e., demand minus supply is small with 
respect to demand. This is an example of “relative” rather than “absolute” 
condition. 
0 
A possible difficulty of bisection is that you need an interval with a sign 
change to start. Library routines such as fzero may relieve the task, since 
they require a starting interval or one starting value, in which case they are 
supposed to locate a root near there; the search for an interval with a change 
in sign is carried out automatically. The following example shows what may 
go wrong with bisection. 
Example 3.22 Consider the non-linear equation 
1 - = 0. 
2 
Using MATLAB requires the definition of a function handle: 
>> fzero(@(x) l / x ,  3) 

194 
BASICS OF NUMERICAL ANALYSIS 
0 -  
II 
80 
60 
40 
20 
-20 
40 
-60 
4 0  
-lW 
-0 
- 
~ 
- 
- 
- 
- 
- 
- 
0 
0 5  
5 
Fig. 3.24 Bisection cannot be applied to a discontinuous function. 
ans = 
-2.7776e-016 
We get a very small number, virtually zero. But this is not really a root: 
>> l/ans 
ans = 
-3.6003e+015 
In this case we get a “false” zero. Of course it is our fault: we are applying 
bisection to a discontinuous function (see figure 3.24). But what bisection sees 
is a function with a change in sign and a shrinking interval which eventually 
satisfies the first termination criterion, but not the second one. 
In other cases (e.g., x2 = 0) you do not get any root by bisection: 
>> fzero(Q(x1 x-2, 3) 
Exiting fzero: aborting search for an interval containing a 
sign change because NaN or Inf function value encountered 
during search. 
(Function value at -1.8203e+154 is Inf.) 
Check function or try again with a different starting value. 
ans = 
NaN 
The problem here is that we have a root where the graph is tangent to the 
x-axis and the initialization function is clearly not able to find an interval 
with a change in sign. 
0 
Despite all of its weaknesses, the bisection method has the remarkable 
characteristic that it requires nothing more than the ability to evaluate, or 

SOLWNG NON-LINEAR EQUAT/ONS 
195 
estimate] the function f at a given point. To appreciate this, think of a func- 
tion defined as a complicated expected value, or a function defined implicitly 
by an optimization problem: 
f(x) = E, (F(x,w)] 
or 
g(x) = minG(x,y). 
YES 
In both cases, getting more information on f and g (e.g., the value of the 
derivative] if it exists), may be no easy task. Moreover] bisection does not 
require the differentiability of the function. On the other hand, it can only be 
applied to problems in one unknown variable. 
3.4.2 
Newton’s method 
Unlike bisection] Newton’s method exploits more knowledge of the function f ;  
in particular, it requires computing the first-order derivative of the function 
f. The method can be applied to solving a system of non-linear equations] 
but let us first consider Newton’s method for the scalar equation 
f(x) = 0 
and assume that f E C2, i.e., is sufficiently well-behaved in terms of continuity 
and differentiability. Consider a point x(O), which is not a solution of the 
equation since f(x(’)) # 0. We would like to move by a step Ax, such that 
the new point x = do) + Ax solves the equation] i.e., 
f (do) 
+ AX) = 0. 
To obtain the displacement Axl we may consider the Taylor expansion: 
f (x(O) + Ax) z f (x(O)) + f’(J0)) 
AX, 
Solving this equation for Axl we get 
Since the Taylor expansion is truncated, we will not find a root of the equation 
in one step, but we may use the idea to define a sequence of points: 
Geometrically, the method uses the tangent of f in x ( ~ )  
to improve the es- 
timate of the solution, as shown in figure 3.25. Like any method, Newton’s 
method has strengths and weaknesses: 
0 Convergence, unlike bisection] is quadratic] which is good news. 

196 
BASICS OF NUMERICAL ANALYSIS 
Fig. 3.25 Geometrical illustration of Newton’s method. 
0 The lmd news is that convergence is only local: This means that unless 
you start near the root, the method may fail; homotopy continuation 
methods (section 3.4.5) are a possible approach to ease this difficulty. 
0 Many things may go wrong, and stalling may result; in practice, many 
adjustments are needed to get a robust implementation of this meth- 
ods.14 
As an example of application of bisection and Newton‘s method, we consider 
next the computation of implicit volatility. 
Example 3.23 As we have pointed out in section 2 6.5. sometimes Black- 
Scholes formula is used in an apparently weird way to find the value of volatil- 
ity such that the theoretical price predicted by the formula matched the ob- 
served price. This is the zrriplzed volatility. This might be useful in order to 
estimate volatility as perceived by the market participants rather than using 
historical data; indeed. this approach has been advocated for Van calcula- 
tlOIlb. 
This is easily accomplished in MATLAB. consider a call option with strike 
price $54, expiring in five months, on a stock whose current price is $50, 
volatility is 30%. when the risk-free interest rate is 7%. Its price is obtained 
as follows: 
>> c=blsprice(50, 54, 0.07, 5/12, 0.3) 
c =  
2.8466 
’“or 
a full treatment of Newton’s method, including MATLAB code, see [12]. 

SOLVING NON-LINEAR EQUATIONS 
197 
Now let’s go the other way around, and check which volatility would yield this 
price. We may define an anonymous function handle and find a zero using 
f zero: 
>> fzero(Q(x) blsprice(50, 54, 0.07, 5/12, x) - 2.8466, 1) 
ans = 
0.3000 
Alternatively, we could use an M-file to define the function. 
Since in the Black-Scholes formula we have the option price in analytical 
terms, one might wonder if it is better to use Newton’s method rather than 
simpler methods such as bisection. This requires computing the derivative of 
the non-linear function, but this effort could pay off in terms of efficiency. In 
fact, the Financial toolbox includes a function, blsimpv, which computes the 
implied volatility of a European call by Newton’s method. Its performance 
may be compared with that of fzero. 
>> tic, blsimpv(50,54,0.07,5/12,2.8466), toc 
ans = 
0.3000 
Elapsed time is 0.030920 seconds. 
>> tic, fzero(Q(x) blsprice(50, 54, 0.07, 5/12, x)-2.8466,1), toc 
ans = 
Elapsed time is 0.039830 seconds. 
0.3000 
You see that there is a (small) advantage in using Newton’s method. 
I] 
A significant advantage of Newton’s method is that its is immediately gener- 
alized to a vector equation such as 
F(x) = 0, 
where F = [fl f2 . . . fn]’. Given an approximation x(lC) = [xy) 
x r )  . . . xn 
( W ] l  
of the root x* = [x; xa + ‘ .  x:]’, we may write 
.. 
which is simply a system of linear equations in which the matrix coefficients 
form the Jacobian matrix 

198 
BASICS OF NUMERICAL ANALYSIS 
A sequence of solution estimates is built by solving the linear systems 
and setting 
A disadvantage of this approach is that it requires computation of the Jacobian 
matrix at each step. Coding that may be difficult and error-prone. Hence 
numerical approximations of the Jacobian are often used, leading to quasi- 
Newton methods. 
,(k+l) = X(k) + Ax(k). 
3.4.3 
Newton's method and its variants are a possible strategy to solve systems 
of non-linear equations. However, there are alternative approaches based on 
optimization. We have already established the connection between optimiza- 
tion and equation solving by the conjugate gradient method in section 3.2.5. 
When tackling a system of linear equations, like the one we have discussed in 
the previous section, we may consider the following reformulation: 
Optimization-based solution of non-linear equations 
n 
i = l  
The idea is illustrated graphically in figure 3.26. Since the squared norm 
cannot be negative, if we find a minimizer such that the function value is 
zero, then the minimizer is a root of the equation. This is the approach 
taken in the MATLAB f solve function; this function, unlike fzero, aims at 
solving systems of linear equations and is part of the Optimization Toolbox, 
not the MATLAB core. The figure also explains why, in general, finding the 
whole set of roots is a tough issue, corresponding to a non-convex optimization 
problem, possibly featuring several minima. The root we find will depend on 
the starting point. Furthermore, some numerical care is needed as shown in 
the following example. 

SOLVING NON-LINEAR EQUATIONS 
199 
Plot of f(x) 
40 - 
20 - 
1
2
 3 
4 
5 
6 
7 
8 
9 
10 
11 
Plot O f f  2(x) 
2500 3
2000 I 
1500 ! 
iil 
io
500 
0 
1
2
3
4
5
6
7
8
9
1
0
1
1
 
Fig. 3.26 Solving non-linear equations by optimization methods. 

200 
BASICS OF NUMERICAL ANALYSIS 
05 
-0 5 
-4 
-3 
-2 
-1 
0 
1 
2 
3 
4 
Fig. 3.27 Function for example 3.24. 
Example 3.24 To solve the equation 
we may use fsolve as follows. First we define the function (and we plot it, 
obtaining the graph illustrated in figure 3.27): 
>> f = @(XI 
(x."3>.*exp(-x.^2>; 
>> ~~=-4:0.05:4; 
>> plot (vx , f (VX) > 
Then we may easily apply f solve, providing a starting point: 
>> f solve (f ,I> 
Optimization terminated : 
first-order optimality is less than options.TolFun. 
ans = 
0 
>> f solve (f ,2) 
Optimization terminated: 
first-order optimality is less than options.TolFun. 
ans = 
3.4891 
We see that the root we get depends on the starting point, which is expected. 
Unfortunately, the second point is not an actual root of the equation. Looking 
at the graph of the function, we may see that for x + f o o  the function tends 
to zero. This implies that we get a numerical "false" zero when the value of 
the function is smaller than a prescribed tolerance. 
0 

SOLVING NON-LINEAR EQUATlONS 
201 
Example 3.25 To illustrate the advantage of quasi-Newton methods, we 
consider here a classical example in Microeconomics, i.e., the computation of 
a Cournot equilibrium for a duopoly. For the unfamiliar reader, the problem 
is finding the two production outputs for two firms, in such a way that no 
firm would find advantageoys to deviate (unilaterally) from that output. The 
problem each firm faces is that increasing output may increase revenue (the 
firm sells more) but it may also decrease prices (because of larger availability). 
Hence, we should look for production quantities maximizing net profit. 
The two firms have cost functions: 
1 
Cz(q2) 
= pzq,2, 
i = 1,2, 
which display increasing marginal cost. We assume the inverse demand func- 
tion (for the whole market): 
P(q) = q-1/q. 
This function yields the market price, given the joint supply q = q1+ qz. The 
profit for firm i is revenue minus cost: 
7rz(q1,42) = P(q1+ qz)q2 - Cz(qt), 
i = 1,2. 
To find the Cournot equilibrium, we should enforce the optimality condition 
of profit for firm 1, as a function of its output q1, and of profit for firm 2, as 
a function of qz. The stationarity ~ondition'~ 
yields the following set of two 
non-linear equations: 
fZ(4) = (q1 + qz)-'/" - (l/v)(q1 + qz)-l'Q-l q, - c,q, = 0 
i = 1,2. 
We also need the Jacobian matrix, and to improve readability it is better to 
rewrite the function above as 
fz(q) = qe + eqe-lq, - G Q Z ,  
where e = -1/q. Then straightforward calculations yield 
Assume q = 1.6, c1 = 0.6, and cg = 0.8. To solve the problem by Newton's 
method, we need a function computing both the function itself and the Ja- 
cobian. This is accomplished by the code displayed in figure 3.28, which also 
includes a script to call the function. 
"More on this in chapter 6. 

202 
BASICS OF NUMERICAL ANALYSIS 
function [fval,f jac] = cournotJac(q,c,eta) 
e = -l/eta; 
fval = qtot-e + e*qtot-(e-l)*q - c.*q; 
fjac = zeros(2,2); 
fjac(l,l) = 2*e*qtot-(e-l) + e*(e-l)*qtot”(e-2)*q(l) 
- ~(1); 
f jac(l,2) = e*qtot-(e-l) + e* (a-1) *qtot^(e-2) *q(2) ; 
fjac(2,l) = e*qtot-(e-l) + e*(e-l)*qtot-(e-2)*q(I); 
fjac(2,2) = 2*e*qtot-(e-l) + e*(e-1)*qtota(e-2)*q(2) 
- ~(2); 
qtot = sum(q1; 
% CournotJacScript 
c = L0.6; 0.81; 
eta = 1.6; 
qo = E l ;  11; 
options = optimset(’Jacobian’, ’on’, ’DerivativeCheck’, ’on’); 
[q,fval,exitflag,outputl = fsolve(@(q)cournotJac(q,c,eta), q0, options); 
fprintf(1,’ ql = %f\n q2 = %f\n’, q(l), 
q(2)); 
fprintf(1,’ number of iterations = %d\n’, output.iterations); 
Fig. 3.28 Code and script for Cournot duopoly. 
With optimset we tell MATLAB that we are going to provide the Jacobian, 
and we ask to check derivatives against a finite difference approximation. 
Running the script, we get 
>> CournotJacScript 
Maximum discrepancy between derivatives 
Optimization terminated: 
first-order optimality is less than options.TolFun. 
= 3.12648e-009 
ql = 0.839568 
q2 = 0.688796 
number of iterations = 5 
It is interesting to note what happens if we introduce an error in the compu- 
tation of the Jacobian. For instance, if the last line in cournot Jac is changed 
to 
fjac(2’2) = e*qtot-(e-1) + e*(e-1)*qtotA(e-2)*q(2) 
- ~(2); 
we get an error message: 
>> CournotJacScript 
Maximum discrepancy between derivatives 
Warning: Derivatives do not match within tolerance 
= 0.202631 

SOLVING NON-LINEAR EQUATIONS 
203 
function [f Val ,f jac] = cournotNoJac(q, c, eta) 
e = -l/eta; 
qtot = sum(q); 
fval = qtot-e + e*qtot-(e-l)*q - c.*q; 
% CournotNoJacScript 
c = C0.6; 0.81; 
eta = 1.6; 
qo = [l; 11; 
[q, fval, exitflag, output] = fsolve(@(q) cournotNoJac(q,c,eta), SO); 
fprintf(i,’ ql = %f\n q2 = %f\n’, q(I), q(2)); 
fprintf(1,’ number of iterations = %d\n’, output.iterations); 
Fig. 3.29 Code and script for Cournot duopoly using quasi-Newton method. 
Derivative from finite difference calculation: 
-0.8406 
-0.0380 
-0.0380 
-1.0406 
User-supplied derivative, Q(q) cournotJac(q, c,eta) : 
-0.8406 
-0.0380 
-0.0380 
-0.8380 
0.0000 
0.0000 
0.0000 
0.2026 
Difference: 
Strike any key to continue or Ctrl-C to abort 
To avoid this kind of potential trouble, we may rely on numerical approx- 
imations of derivatives. This is easily accomplished by writing a function 
which does not compute the Jacobian, and by calling fsolve with default 
options. This is accomplished by the function and script in figure 3.29, which 
is definitely less prone to errors. Running the script, we get 
>> CournotNoJacScript 
Optimization terminated: 
first-order optimality is less than options.TolFun. 
ql = 0.839568 
q2 = 0.688796 
number of iterations = 3 
We get the same solution, and what looks surprising is that less iterations 
are reported. Intuitively, we would expect less iterations by providing more 
information in the form of the Jacobian. However, we are not really using 

204 
BASICS OF NUMERICAL ANALYSIS 
Newton’s method for non-linear equations, and intuition may fail. In fact, 
the performance of an algorithm depends on many features: f solve is based 
on a choice of three optimization methods and several options may be selected 
influencing the number and speed of iterations. 
0 
3.4.4 
Putting two things together: solving a functional equation by a 
collocation method 
Assume we have to solve a functional equation of the form 
dx, 
f(x)) = 0 
vx E [a, bl, 
where g is given and f is the unknown function. Note that since we want 
to find a function defined over a real interval, this is an infinite-dimensional 
problem. The first step to deal with such a problem numerically is to find 
a suitable way to discretize it. One possibility would be to select a discrete 
subset of n points xi in the interval and solve a system of non-linear equations: 
g(zi, yi) = 0, 
i = 1, . . . , n, 
where the unknown is really yi = f(zi). Then we may use interpolation to 
“complete” the function on the whole interval. 
However there is a more elegant alternative, known as the collocation 
method. The idea is still to fix a set of n points, called collocation nodes, 
and to approximate f by a linear combination of n basis functions: 
n 
i=l 
Then our problem boils down to finding the coefficients ci by solving a system 
of non-linear equations: 
We will meet other functional equations in the form of partial differential 
equations or recursive equations associated to dynamic programming. The 
collocation method is at the heart of the finite element method for solving 
PDEs and of some computational approaches to solve stochastic optimization 
problems by dynamic programming. 
3.4.5 
Homotopy continuation methods 
Since Newton’s method is not globally convergent, a good initial guess may 
be necessary. To overcome this difficulty, and enhance global convergence, we 

SOLVlNG NON-LINEAR EQUAT/ONS 
205 
may embed the problem within a parameterized family of problems. Assume 
that we want to solve the equation f (2; t )  = 0 for a specific value t* of the 
parameter t. If we know that for t = to we have a solution xo, then we may 
generate a sequence of problems corresponding to parameters to, t’, t2, . . ., 
using xi-’ as the initial guess for problem i. More generally, if we know a 
solution of the equation g(z) = 0, in order to solve f(z) = 0 we may define 
and “move” t from 0 to 1. In practice we are “deforming” an easy problem 
into a hard one. This idea may be formalized by a homotopy. Given two 
functions f, g : X - 
Y, 
a homotopy between f and g is a continuous map 
h : [ O , l ] x X - Y  
such that h(0,z) = g(z) and h(1,x) = f(z) Equation (3.11) is the linear 
homotopy. Newton’s homotopy is 
where zo is the solution for t = 0. 
We have a parameterized family of problems, such that a path of solutions 
z(t) results. Strictly speaking, this makes sense if h(t, z) = 0 has one root for 
each t E [0,1]. Assuming this property holds, we must come up with a way 
to follow the path of solutions, leading to the one we are interested in. In 
the following example, based on [13, pp. 140-1411, we give an idea of a path 
following strategy. 
Example 3.26 Assuming differentiability of the involved functions, we may 
differentiate the equation 
h(t, z(t)) = 0 
and get 
dh 
dh 
-(t, 
at 
z(t)) + -(t, 
d X  
z(t)) 
* z’(t) = 0. 
This yields the following differential equation 
where we have eased the notation by using h, and ht to denote partial deriva- 
tives. We could integrate this equation, with initial condition z(O), to get the 
solution ~ ( 1 ) .  
As a numerical example, consider the following problem, where X = Y = 
R2: 
x: - 32; + 3 ] =o. 
~
1
~
2
 
+ 6 
F(x) = 

206 
BASICS OF NUMERICAL ANALYSIS 
Using Newton's homotopy with xo = (1, l), we have 
We may invert h,: 
A = 2x9 + 62:. 
Finally, we get the ordinary differential equations: 
By numerical integration, we get x(1) = (-2.961,1.978). Now we are in a 
neighborhood of the solution of the original equation; to polish the solution, 
we may take a few iterations of Newton's method, which yields the solution 
(-372). 
0 
We have included the example above to illustrate the overall idea, but there 
is a rich set of path following approaches. The same idea can be applied to op- 
timization problems; in fact, we will meet path following again, since it is the 
foundation of advanced optimization methods such as interior point methods 
for linear programming (section 6.4.4). The homotopy continuation method 
is quite sophisticated and powerful; for advanced applications to economics, 
see [7] and [lo]. 
For further reading 
In the literature 
0 The literature on numerical methods is quite extensive. One classical 
reference is [18]. Other references are [2], [13], and [17]. 
An interesting book on numerical methods from an economist's point of 
view is [lo]. 
Splines are dealt with in depth in [5]. They are a widespread tool, both 
in engineering (e.g., in computer-aided design) and in economics. For a 
recent application in financial economics, see [Ill. 
0 A classical source for special function evaluation is [l]. 

REFERENCES 
207 
0 Approximation theory is the subject of [15] and [19]. 
0 If you would like a “cookbook” collection of algorithms, [16] is a well- 
known reference providing many C-language codes implementing nu- 
merical methods (a Fortran version is available, too). 
0 Several numerical analysis books have been written based on MATLAB; 
see, e.g., [6] and [14]. 
On the Web 
0 http : //www . netlib. org is a web site offering many pointers to numer- 
ical analysis material. 
0 http : //www .mathworks. com/support/books lists several MATLAB- 
based books, including basic numerical analysis texts. 
REFERENCES 
1. M. Abramowitz and I.A. Stegun, editors. Handbook of Mathematical 
Functions. Dover Publications, New York, 1972. 
2. K.E. Atkinson. An Introduction to Numerical Analysis (2nd ed.). Wiley, 
Chichester, West Sussex, England, 1989. 
3. L. Barzanti and C. Corradi. A Note on Interest Rate Term Structure Es- 
timation Using Tension Splines. Insurance Mathematics and Economics, 
22~139-143, 1998. 
4. J.F. Carriere. Nonparametric Confidence Intervals of Instantaneous For- 
ward Rates. Insurance Mathematics and Economics, 26:193-202, 2000. 
5. C. de Boor. A Practical Guide to Splines. Springer-Verlag, New York, 
1978. 
6. L.V. Fausett. Applied Numerical Analysis Using MATLAB. Prentice Hall, 
Upper Saddle River, NJ, 1999. 
7. C.B. Garcia and W.I. Zangwill. Pathways to Solutions, Fixed Points, and 
Equilibria. Prentice Hall, Englewood Cliffs, NJ, 1981. 
8. C. Hastings. Approximations for Digital Computers. Princeton University 
Press, Princeton, NJ, 1955. 
9. J.C. Hull. Options, Futures, and Other Derivatives (5th ed.). Prentice 
Hall, Upper Saddle River, NJ, 2003. 

208 
BASKS OF NUMERlCAL ANALYSlS 
10. K.L. Judd. Numerical Methods in Economics. MIT Press, Cambridge, 
MA, 1998. 
11. K.L. Judd, F. Kubler, and K. Schmedders. Computing Equilibria in 
Infinite-Horizon Finance Economies: The Case of One Asset. Journal 
of Economic Dynamics and Control, 24: 1047-1078,2000. 
12. C.T. Kelley. Solving Nonlinear Equations with Newton’s Method. SIAM, 
Philadelphia, PA, 2003. 
13. D. Kincaid and W. Cheney. Numerical Analysis: Mathematics of Scien- 
tific Computing. Brooks/Cole Publishing Company, Pacific Grove, CA, 
1991. 
14. J.H. Mathews and K.D. Fink. Numerical Methods Using MATLAB (3rd 
ed.). Prentice Hall, Upper Saddle River, NJ, 1999. 
15. M. J.D. Powell. Approximation Theory and Methods. Cambridge Univer- 
sity Press, Cambridge, 1981. 
16. W.H. Press, S.A. Teukolsky, W.T. Vetterling, and B.P. Flannery. Nu- 
merical Recipes in C (2nd ed.). Cambridge University Press, Cambridge, 
1992. 
17. H.R. Schwarz. Numerical Analysis: A Comprehensive Introduction. Wi- 
ley, Chichester, West Sussex, England, 1989. 
18. J. Stoer and R. Burlisch. Introduction to Numerical Analysis. Springer- 
Verlag, New York, 1980. 
19. G.A. Watson. Approximation Theory and Numerical Methods. Wiley, 
Chichester, West Sussex, England, 1980. 
20. P. Wilmott. Quantitative Finance (vols. I and II). Wiley, Chichester, 
West Sussex, England, 2000. 

4 
Numerical Integration: 
Deterministic and Monte 
Carlo Methods 
Numerical integration is a standard topic in numerical analysis. We have 
preferred to dedicate a specific chapter to it because of its importance in 
computational finance. Furthermore, we include topics such as Monte Carlo 
integration which are not always covered in standard textbooks on numerical 
analysis. Usually, the term Monte Carlo simulation is used, which is somewhat 
more appealing, but it is important to cast this approach within a numerical 
integration framework in order to pave the way to quasi-Monte Carlo methods. 
Classical approaches to numerical integration based on quadrature formulas 
are deterministic, just as quasi-Monte Carlo methods. Monte Carlo methods 
are based on random sampling, at least conceptually, and so some connection 
with statistics is expected. 
We have seen that option pricing requires computing an expected value 
under a risk-neutral measure, but an expected value is actually an integral. 
The expected value of a function g(.) of a random variable X with probability 
density fx(z) is 
E[S(X)I = J + % ( 4 f X  
-ca 
dx. 
In one-dimensional cases, we may find an analytical solution, like in the Black- 
Scholes case, but this is difficult in general. If the random variable X is a 
scalar, classical deterministic methods work quite well, but when expectation 
is taken with respect to a random vector and we must integrate over a high- 
dimensional space, random sampling may be necessary. Random sampling 
is a natural way to simulate dynamics affected by uncertainty, such as prices 
modeled by stochastic differential equations. Natural applications, apart from 
209 

210 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
option pricing, are portfolio optimization, risk management, and estimation 
of Value at Risk. 
It is worth noting that numerical integration may be implicitly used to 
estimate probabilities. If A is an event which may occur or not depending on 
a random variable X, then 
+m 
P(A) = l , Z A ( Z ) f X ( Z ) d Z ,  
where ZA(Z) is the indicator function for event A (taking the value 1 if A 
occurs when X = Z, 0 otherwise). When A is a rare event, clever strategies 
are needed to get an accurate estimate with a reasonable computational effort. 
Finally, there are situations in which we define a function by an integral. A 
typical case is the expected value of a function depending on a control variable 
(modeling our decisions) and a random variable (modeling what we cannot 
control): 
f m  
H ( z )  = Ex[g(X, 211 = 
g(z, z)fx(.) dx. 
L 
This is quite common in stochastic optimization and dynamic programming, 
whereby we want to find a maximizer (or minimizer) of H(z), and this calls 
for a suitable approximation of H by discretization of the continuous distribu- 
tion. In other words, we want to generate a discrete set of scenarios yielding a 
reasonable approximation of the underlying uncertainty. Numerical methods 
such as Gaussian quadrature are helpful here. Indeed, all numerical integra- 
tion methods require some form of discretization, or sampling, via regular 
grids or other mechanisms. We should also note that we may also be inter- 
ested in the derivative of H ( z ) ,  not only for optimization purposes, but also 
to evaluate sensitivities. A familiar case is computing the Greeks of an option. 
We start the chapter with a very brief overview of classical deterministic 
quadrature in section 4.1. We will just present very basic approaches in order 
to point out the conceptual basis of quadrature functions available in MAT- 
LAB. We will also deal with Gaussian quadrature because of its importance 
in computational dynamic programming. 
Then we introduce Monte Carlo integration in section 4.2. Monte Carlo 
simulation is based on random number generation; actually, we must speak 
of pseudorandom numbers, since nothing is random on a computer. How this 
is accomplished is described in section 4.3. 
If we feed random numbers into a simulation procedure, the output will be a 
sequence of random numbers. Given this output, we use statistical techniques 
to build an estimate of a quantity of interest. We would like to evaluate the 
reliability of this estimate in some way, e.g., by a confidence interval, or the 
other way around, we would like to carry out the simulation experiments in 
such a way that the estimation error is controlled. Section 4.4 deals with the 
issue of setting the number of simulation experiments (replications) properly. 
Intuitively, the more replications we run, the more reliable our estimates will 

DETERMINISTIC QUADRATURE 
21 1 
be. Unfortunately, reaching a suitable precision might require a prohibitive 
number of experiments. Improving the quality of the estimates without in- 
curring huge CPU times calls for proper variance reduction techniques, which 
are the subject of section 4.5. Using pseudorandom numbers on a computer 
and then applying statistical techniques may raise some philosophical issues; 
after all, the sequences of numbers we use are deterministic. It can be argued 
that the success of Monte Carlo simulation simply shows that there are some 
deterministic sequences that work well and that there could be others that 
work even better. Pursuing this idea leads to quasi-Monte Carlo simulation, 
which is dealt with in section 4.6. 
A final consideration is that simulation may be used to evaluate the con- 
sequences of a certain policy, but it cannot generate the policy itself. To this 
end, we should use the optimization methods which will be described in chap- 
ter 6. Unfortunately, most of those techniques require an analytical model 
that may be too complex or not available at all, which is the very reason 
why we resort to simulation so often. Possible ways to couple simulation and 
optimization techniques are described in section 6.6. 
In order to better illustrate the material we will use simple examples from 
elementary integration and pricing of vanilla options. We should bear in mind 
that for those vanilla options analytical formulas are available, and that our 
examples are just illustrative. We will consider practically relevant cases in 
chapter 8. 
4.1 DETER M I N I STI C QUAD RAT U RE 
Consider the problem of approximating the value of a definite integral like 
b 
I[fl = 1 f(x) dx 
over a bounded interval [a, b] for a function f of a single variable. Since the 
integration is a linear operator, it is natural to look for an approximation 
preserving this property. Using a finite number of values of f over a set of 
nodes xj such that 
a = XO < X I  < 
< X N  = b, 
we may define a quadrature formula such as 
A quadrature formula is characterized by the weights wj and by the nodes xj. 
To be precise, a quadrature formula like the one we are describing is called a 
closed formula, since evaluation of the function in the extreme points of the 

212 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
interval is used. Sometimes, open formulas are used when the function is not 
well-behaved near a or b, or when we are integrating on an infinite interval. 
Any quadrature formula is characterized by a truncation error: 
E = Wl - QVI. 
A reasonable requirement is that the error should be zero for sufficiently simple 
functions such as polynomials. We may define the order of a certain quadra- 
ture formula as the maximum degree m such that the truncation error is zero 
for all the polynomials of degree rn or less. In other words, if the original 
function is substituted by an interpolating polynomial, we should not commit 
any error in integrating the polynomial. It is quite common to see expressions 
for the truncation error like 
E = rf'k'(J), 
where y is some constant depending, among other things, on a and b, E is some 
unknown point in the interval (a, b), and k is the order of some derivative. 
Since the derivative of order k is zero for a polynomial of degree not exceeding 
k - 1, there is clear link between k and the order of the quadrature formula. 
If the function f is smooth enough, we may hope that high order translates 
to high accuracy. 
4.1.1 
Classical interpolatory formulas 
One way to derive quadrature formula is to consider equally spaced nodes: 
x j = a + j h ,  
j=O,1,2 ,..., n, 
where h = (b - a)/n; also let fj = f(xj). We have seen in function interpo- 
lation that this choice need not be the best one, but it is a natural starting 
point. Selecting equally spaced nodes yields the set of Newton-Cotes quadra- 
ture formulas. 
Given those n + 1 nodes, we may consider the interpolating polynomial 
P,(x) using Lagrange polynomials of degree n: 
n 
j =O 
Then we may compute the correct weights as follows: 

DETERMINISTIC QUADRATURE 
213 
Fig. 4.1 Example of the trapezoidal quadrature formula. 
Considcr the case of two nodes only, xo = a and 2 1  = b. Here we are just 
interpolating f by a straight line: 
A straightforward calculation yields 
Actually, what we are saying is that we may approximate the area below the 
function using trapezoidal elements, as depicted in figure 4.1, and the formula 
above gives the area of one element. Applying the idea to more subintervals, 
we get the trapezoidal rule: 
Given any quadrature formula for an interval: we may get a composite formula 
by applying the same pattern to small subintervals of a large one. 
A quadrature formula based on n + 1 nodes is by construction exact for 
polynomials of degree 5 n. We may go the other way around, and build a 
formula by requiring a certain order. Consider the case 
1' 
f(x) 
M wof(0) f ~ f ( 0 . 5 )  + Wf(l), 
and say we want a formula that is exact for polynomials of degree 5 2. Having 
fixed the riodcs, we may find the weights by solving the system of linear 

214 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
equations: 
I 
1 = Jd d x = w o + w i + w 2  
1 
- = 
x d x = - w l + w z  
2 
2 
1 
1 
1 
3 
4 
1 
= Jd x2dx = -w1 f w 2 ,  
- 
which yields wo = 116, w1 = 213, w2 = 116. Applying the same idea on the 
interval [a, b], we get Simpson’s rule: 
[f(x) 
dx M - 
6 
It fairly easy to see that, somewhat surprisingly, this formula is actually exact 
for polynomials of degree I 3 .  In fact, we have 
b4 - a4 
[x 
dx=- 
4
.
 
Applying Simpson’s rule we have, by some straightforward algebra: 
b-a 
6 
[ a 3 + 4 ( T ) 3 + b 3 ]  
1 
b4 - a4 
b-a [a3 + - (a3 +3a2b+3ab2 + b3) + b3 = - 
1
4
 
- 
- 
6 
2 
Simpson’s rule may be applied to subintervals of (a, b) in order to get a com- 
posite formula. 
It is important to see the connection between the approach we have just 
pursued and the idea of moment matching in probability. We may discretize 
a continuous probability distribution in such a way that the discrete distri- 
bution matches moments of the continuous distribution, e.g., expected value 
and variance. This idea is used to approximate stochastic processes, such as 
geometric Brownian motion, by binomial and trinomial lattices and it will be 
pursued in chapter 7. Now, what we have seen is that for given nodes we 
may find suitable weights to obtain a quadrature formula with desired order. 
We have also seen that in function interpolation equispaced nodes need not 
be the best choice. Generalizing the idea we should wonder if there is a way 
to find weights and nodes jointly, in order to obtain a quadrature formula of 
maximal order. This idea leads to Gaussian quadrature formulas. 
4.1.2 
Gaussian quadrature 
In Newton-Cotes formulas we fix nodes and try to find suitable weights so 
that the order of the formula is as large as possible. The rationale behind 

DETERMlNlSTK QUADRATURE 
215 
Gaussian quadrature is that if we do not fix nodes a priori, we essentially 
double the degrees of freedom, in such a way that the order can be more or 
less doubled. Furthermore, Gaussian quadrature formulas are developed with 
respect to a non-negative weight function ~ ( x ) .  
We look for a quadrature 
formula like 
which is exact when f is a polynomial. Note that in this section, unlike 
the previous one, it is convenient to consider n nodes xi, i = 1,. . . ,n. The 
weight function w(x) can be used to encapsulate undesired singularities of 
the integrand function. In our setting, ~ ( x )  
will be interpreted as a proba- 
bility density. In fact we will only outline the development of Gauss-Hermite 
quadrature, where w(x) = e-xz, and there is a clear connection with comput- 
ing the expected value of a function of a normal random variable. 
Let Y be a random variable with normal distribution N(p, u'). Then 
In order to use weights and nodes from a Gauss-Hermite formula, we need 
the following change of variable 
Hence 
Now, how should we select the nodes and weights in (4.1) in order to get a 
quadrature formula with maximum order? We should choose as nodes the 
n roots of a polynomial of order n, selected within a family of orthogonal 
polynomials with respect to the inner product (see also section 3.3.4): 
< fI9 > = 
w(x)f(x)g(x) 
dx. 
I" 
It can be shown that a polynomial of degree k within that family has k distinct 
real roots. Furthermore, these roots are interleaved, in the sense that each of 
the k - 1 roots of the polynomial of degree k - 1 lies in an interval defined by 
a pair of consecutive roots of the polynomial of degree k. Using this choice of 
nodes, along with a proper choice of weights, yields a quadrature formula with 
order 2n - 1. To see this, consider a polynomial q E II,, i.e., a polynomial of 
degree n, which is orthogonal to all polynomials in IIn-l: 

216 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
Any polynomial f E IIzn-l can be divided by q, obtaining a quotient p and a 
remainder r: 
f = qP + r, 
where p ,  r E IIn-l. Now let us integrate w f by a quadrature formula on n 
nodes xi, i = 1,. . . , n, which are the zeros of q: 
A family of 
procedure: 
I” 
b 
w(x)p(x)q(x) 
dx + / w(x)r(x) dx 
(division) 
a 
0 + lb 
w(x)r(x) dx 
(q is orthogonal to p )  
n 
wir(xi) 
(quadrature is exact for r E rIn-~) 
i=l 
n C wif(xi) 
orthogonal polynomials pj(x) may be built by the following 
(xi is a zero of q). 
i=l 
where 
j = 0,1,2,. . . 
Here coefficient bo is arbitrary and it can be set to 0. At each step, the 
procedure generates a new polynomial of degree one plus the degree of the 
previous polynomial. In the end, we have a family of orthogonal polynomials, 
one for each degree. Actually there are different choices of normalizations 
yielding different families of polynomials. 
In the Gauss-Hermite case, whereby w(x) = e-zz, applying the proce- 
dure above results in the following recursive procedure yielding a sequence of 
Hermite polynomials Hj: 
Hj+l = 2 ~ H j  
- 2jHj-1. 
It is worth noting that this procedure is not quite numerically viable, as it 
implicitly computes factorials which tend to overflow for large n. This is 

DETERMINISTIC QUADRATURE 
21 7 
why a different normalization can be used, yielding a family of orthonormal 
polynomials': 
I H-1= 0 
1 
Ho = - 
,+14 
In order to select weights, one possibility would be to require exact integration 
for the first n polynomials in the family, including the polynomial of degree 
0. Since po(x) = 1, this means that the (weighted) integrals of pj(x), j = 
1,. . . , n - 1 should be zero, since they are all orthogonal to po(x). These 
conditions yield the following system of linear equations: 
Po (xn) 
It can be shown that a possibly more convenient way of getting weights is by 
using the following recursion: 
< Pn-1,pn-1 > 
wj = 
Pn- 1 ( Z j  ) P i  (Zj 1 ' 
where p;(xj) is the derivative of the polynomial. In the Gauss-Hermite case, 
using the orthonormal set of polynomials, this boils down to: 
where the derivative of polynomial j is 
MATLAB code to implement Gauss-Hermite quadrature is displayed in figure 
4.2. Polynomials are stored in vectors; HPolyl, HPoly2, and HPoly3 play the 
roles of polynomials Hj-1, 
H j ,  and Hj+1 in recursion (4.2), respectively. In 
the f o r  loop, we must pay attention to i, since there is the typical shift in 
index values because of the MATLAB convention (array indexing starts from 
1). On exit from the loop, HPoly3 contains fin and HPolyl contains fin-l. 
In computing roots, we use the standard roots function. This need not be 
'See, e.g., 113, pp. 150-154). 

218 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
function [x,w] = GaussHermite(mu,sigma2,N) 
HPolyl = [ l/pi-0.25 1 ; 
HPoly2 = Csqrt(2) / pi-0.25, 01 ; 
for j=1: 
N-1 
HPoly3 = [sqrt(2/(j+l))*HPoly2 , 01 - LO, 0, sqrt(j/(j+l)*HPolyll; 
HPolyl = HPoly2; 
HPoly2 = HPoly3; 
end 
xl = roots(HPoly3) ; 
wl = zeros(N,l); 
for i=l:N 
wl (i) = l/(N)/ (polyval(HPoly1, xl(i)) 1-2; 
end 
[x, index] = sort (xl*sqrt(2*sigma2)+mu) ; 
w = wl(index)/sqrt(pi); 
fig. 4.2 Code to implement Gauss-Hermite quadrature. 
the best approach, as using the interleaving property one can compute roots 
for each polynomial in the sequence by the Newton’s method, using previous 
roots for initialization.2 The last two lines are used to sort nodes in increasing 
order, and the index vector is used to sort weights accordingly. 
It is interesting to check the weights and nodes we get from this function. 
For instance, let us consider a normal random variable with p = 10 and 
o2 = 20, and let us apply a quadrature formula based on five nodes: 
>> [x,w] = GaussHermite(10,20,5) 
x =  
-2.7768 
3.9375 
10.0000 
16.0625 
22.7768 
0.0113 
0.2221 
0.5333 
0.2221 
0.0113 
w =  
>> sum(w) 
2This is the approach taken in [13]. A MATLAB implementation, which generalizes to mul- 
tidimensional integration, can be found in the Computational Economics Toolbox described 
in [lo]. 

DETERMINISTIC QUADRATURE 
219 
1 GHScript.m 
N = [5, 10, 15, 201; 
mu = 4; 
sigma2 = 4; 
Truevalue = exp(mu+O. 5*sigma2) ; 
for i=l:length(N) 
[x,w] = CaussHermite(mu,sigma2,N(i)); 
ApproxValue = dot (w, exp(x)) ; 
fprintf(l,’N=%2d True=%g Approx=%g PercError=%g \nJ, N(i), ... 
Truevalue, ApproxValue, abs(TrueVa1ue-ApproxValue)/TrueValue); 
end 
Fig. 4.3 Script to check Gauss-Hermite quadrature. 
ans = 
1 * 0000 
Nodes, as expected, are symmetrically centered around the expected value; 
furthermore, the sum of weights is 1, which is only convenient, since this 
should be a discretization of a continuous distribution. As a complete exam- 
ple, we may deal with the case of integrating an exponential function. From 
the properties of the lognormal distribution (see section B.2.1) we know that 
if X N N(p, a’), then 
E[ex] = eP+02/2 
A script to check this is displayed in figure 4.3. Running the script, we may see 
that remarkable precision is obtained with a fairly modest number of nodes: 
>> CHScript 
N= 5 True=403.429 Approx=398.657 PercError=0.0118287 
N=10 True=403.429 Approx=403.429 PercError=5.53771e-007 
N=15 True=403.429 Approx=403.429 PercError=1.90343e-012 
N=20 True=403.429 Approx=403.429 PercError=3.95931e-014 
Actually, the number of nodes needed to obtain a suitable accuracy depends 
on variance. The reader is urged to write a function pricing a vanilla European 
call option using Gauss-Hermite quadrature and to compare the result with 
blspr ice. 
4.1.3 
Extensions and product rules 
The interpolatory rules of section 4.1.1 are extended in many ways, which we 
just outline here. To begin with, nodes should be added dynamically until a 
prespecified accuracy is obtained. This can done according to clever strategies 

220 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
in order to avoid unnecessary function re-evaluations. This leads to recursive 
quadrature formulas and to Romberg integration. Furthermore, the choice of 
the nodes may be improved by adapting it to the function characteristics; more 
nodes are needed where there is more variation, and less are needed where the 
function is more "constant"; this leads to adaptive quadrature formulas. All 
these improvements are exploited in scientific libraries, including MATLAB 
functions. 
Product rules are used when we want to extend quadrature formulas to 
multidimensional integration. Suppose we want to compute an integral on 
the unit hypercube 
r 
where [0, lId = [0,1] x [0,1] x . . . x [0,1], and that we have weights and nodes 
for, say, a Newton-Cotes quadrature formula along each dimension; more 
precisely, for dimension k, k = 1, . . . , d, we have weights wf and nodes xf, 
i = 1, . . . , m k .  A product rule approximates the integral above as 
il=l i z = l  
Zd=l 
A product rule builds nodes taking the Cartesian product of node sets along 
each dimension. It is easy to see that this regular grid is going to be impracti- 
cal for large d, and this motivates Monte Carlo integration based on random 
sampling. 
4.1.4 
Numerical integration in MATLAB 
There are a few MATLAB functions to compute one-dimensional integrals. 
They are based on refinements of basic schemes, such as adaptive extensions 
of Simpson's rule. 
Example 4.1 Consider the integral 
r 2 x  
I = jo e-" sin(l0z) dz. 
Integration by parts yields 
I = - I e - "  [sin( lox) + 10 cos( lox)] I 
x 0.0988. 
0 
101 
Using the quad function, we get 
>> f=@(x) exp(-x).*sin(lO*x) 
f =  
@(x) exp(-x) .*sin(lO*x) 

MONTE CARLO /NT€GRAT/ON 
221 
>> quad(f ,0,2*pi) 
ans = 
0.0987 
Precision may be improved by specifying a tolerance parameter: 
>> quad(f,0,2*pi, IOe-6) 
ans = 
0.0987 
>> quad(f,0,2*pi, 10e-8) 
ans = 
0.0988 
We may also adopt alternative strategies, based on adaptive Lobatto quadra- 
ture: 
>> quadl(f,0,2*pi) 
ans = 
0.0988 
MATLAB also provides us with functions for multidimensional integration. 
In the bidimensional case, dblquad can be used, whereas triplequad is used 
for triple integrals. Actually, the latter is a relatively recent addition and was 
not available in earlier MATLAB versions. You can see that we cannot go 
beyond three dimensions. This is due to the intrinsic difficulty of using regular 
grids when we integrate in several dimensions. The typical way to avoid this 
difficulty is resorting to random sampling. 
4.2 
MONTE CARLO INTEGRATION 
The definite integral of a function is a number, and computing that number is 
a deterministic problem involving no randomness. Nevertheless, we may cast 
the problem within a stochastic framework by interpreting the integral as an 
expected value. Consider an integral on the unit interval [0,1]: 
r l  
I = J, g(x) dx. 
We may think of this integral as the expected value E[g(U)], where U is a uni- 
form random variable on the interval (0, l), i.e., U N (0,l). We may estimate 
the expected value (a number) by a sample mean (a random variable). What 
we have to do is generating a sequence {Ui} of independent random samples 
from the uniform distribution and then evaluate the sample mean: 
-
m
 
1 
fm = - C g ( U , ) .  
r = l  
m 

222 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
The strong law of large numbers implies that, with probability 1, 
lim I, = I. 
Random sampling, which is where “Monte Carlo” comes from, is not really 
possible with a computer, but we can generate a sequence of pseudo-random 
numbers using generators provided by most programming languages and en- 
vironments. 
m-m 
Example 4.2 Consider the trivial case 
1 
I = 
ez dz = e - 1 M 1.7183. 
To generate uniformly distributed random numbers, we may use the MATLAB 
rand function; a call like rand (m, n) yields a m x n matrix of uniform random 
numbers. Please note that the parameters m and n have nothing to do with 
the distribution, which is U ( 0 , l )  anyway. We can see the reliability of our 
estimates as a function of the sample size m: 
>> rand(’state’, 0) 
>> mean(exp(rand(1,lO))) 
ans = 
1.8318 
>> mean(exp(rand(1,lO))) 
ans = 
2.0358 
>> mean(exp(rand(1,lO) 1) 
ans = 
1.3703 
>> mean(exp(rand(1,1000000))) 
ans = 
1.7189 
>> mean(exp(rand(l,1000000))) 
ans = 
1.7178 
>> mean(exp(rand(1,1000000) )) 
ans = 
1.7174 
In order to understand the role of the command rand(’state’ ,O>, we should 
consider how “random” numbers are generated on a computer. For now it is 
enough to say that the command resets the generator so that the experiment 
can be replicated obtaining the same results. We see that the estimate is not 
quite reliable for m = 10, whereas variance of the estimator is much lower 
when m = 1,000,000, and the result is close to the correct number. Needless 
to say, we do not know the exact result in practice, and we should wonder 
how to qualify the reliability of the estimate, and how to improve it. 
0 

MONTE CARL0 INTEGRATION 
223 
For one-dimensional integration, Monte Carlo is hardly competitive with de- 
terministic quadrature, but when computing a multidimensional integral it 
may be the only viable option. In general, if we have an integral like 
(4.3) 
where A c R", we may estimate I by randomly sampling a sequence of points 
xi E A, i = 1,. . . , m, and building the estimator 
i=l 
where vol(A) denotes the volume of the region A. To understand the formula, 
we should think that the ratio (l/m) xzl $(xi) estimates the average value 
of the function, which must be multiplied by the volume of the integration 
region in order to get the integral. 
We will see that in practice we need only to integrate over the unit hyper- 
cube, i.e., 
A = [0,1] x [0,1] x . * * x [0,1], 
hence vol(A) = 1. Considering the unit hypercube looks restrictive. In gen- 
eral, we have a vector random variable 
with joint density function f(z1, . . . , xn), and we use Monte Carlo integration 
to estimate the expected value of an arbitrary function of X: 
MATLAB provides us with many functions to generate random variables, but 
we will see that the primary input is always a stream of uniform random 
numbers U N U(0,l). These generators are actually part of the Statistics 
Toolbox, but the core MATLAB environment also offers a function (randn) 
to sample the standard normal distribution. Using this function, we may use 
Monte Carlo integration to price a vanilla call option. 
Example 4.3 We know that the price of a European style option is the 
expected value, under the risk-neutral measure, of the discounted payoff of 
the option: 
f = e-'TE[f77], 

224 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
X BlsMC1.m 
function Price = BlsMCl (SO, K , r , T , sigma, NRepl) 
nuT = (r - 0.5*sigma-2)*T; 
siT = sigma * sqrt(T) ; 
DiscPayof f = exp( -r*T) *max(O, SO*exp(nuT+siT*randn(NRepl, 1) 
Price = mean(DiscPayoff) ; 
-K) ; 
Fig. 4.4 Code to price a vanilla European call by Monte Carlo simulation. 
where fT is the payoff at the maturity date T and a constant risk-free rate r 
is assumed. The notation E[-] is used to emphasize that expectation is taken 
with respect to the risk-neutral measure. If we assume geometric Brownian 
motion, this means that the drift p for the asset price must be replaced by 
the risk-free rate r (see section 2.6). Depending on the nature of the option at 
hand, we may need to generate the full sample paths, or simply the terminal 
asset price. Path generation will be dealt with in chapter 8, but a vanilla call 
option requires just sampling the payoff max{O,S(T) - K } ,  where S(T) is 
the price of the underlying asset at maturity and K is the strike price. From 
example 2.20 on page 98, we know that we may easily accomplish this by 
generating a standard normal random variable e N N(0,l): 
A MATLAB function to price the call option is displayed in figure 4.4. The 
first five input parameters are self-explanatory and are those required by the 
blsprice function implementing Black-Scholes formula. The last parameter 
NRepl is the number of replications, i.e., samples we want to take. We may 
check the impact of this parameter: 
>> S0=50; 
>> K=60; 
>> r=0.05; 
>> T=1; 
>> sigma=0.2; 
>> randnOstate’, 0) 
>> BlsMCl (SO,K,r 
,T, sigma, 1000) 
ans = 
1.2562 
>> BlsMCI(SO,K,r,T,sigma,1000) 
ans = 
1.8783 
>> BlsMCl (SO, K ,r ,T, sigma, 1000) 
ans = 
1.7864 

GENERATlNG PSEUDORANDOM VARlATES 
225 
>> BlsMC1(SO,K,r,T,sigma,1000000) 
ans = 
1.6295 
>> BlsMCl (SO,K,r ,T, sigma, lOOO000) 
ans = 
1.6164 
>> BlsMC1(SO,K,r,T,sigma,1000000) 
ans = 
1.6141 
As before, we reset first the state of the randn generator, so that the exper- 
iment can be repeated by the reader. With only 1000 samples, we see quite 
some variability in the estimate, which starts looking reasonable when the 
number of samples is increased considerably. Clearly, we cannot yield just 
a point estimate: we should also compute some confidence interval for the 
estimate. Possibly, we should understand how many samples are needed in 
order to attain a given precision. Another point is that too many samples are 
needed; things may be worse with higher volatility, and with complex path- 
dependent options we cannot afford taking a huge number of samples. Hence 
we need clever ways to reduce the variance of the estimator. 
0 
Needless to say, the example above is presented for illustrative purposes, 
as there is no need to resort to Monte Carlo simulation to price a vanilla 
European-style call option. What we need is a numerical approximation of 
the integrals involved in the cumulative distribution function for standard nor- 
mal random variables. Nevertheless, we will see that pricing “easy” options 
by simulation may be useful in variance reduction by control variates. 
4.3 
GENERATING PSEUDORANDOM VARlATES 
The usual way to generate pseudorandom variates, i.e., samples from a given 
probability distribution, starts from the generation of pseudorandom num- 
bers, which are simply variates from the uniform distribution on the inter- 
val (0,l). Then, suitable transformations are applied in order to obtain the 
desired distribution. We discuss briefly the most common transformations: 
the inverse transform method, the acceptancerejection approach, and ad hoc 
strategies such as those used to generate standard normal variates. The MAT- 
LAB Statistics toolbox provides the user with a rich library of random variate 
generators, so that the user need not herself program the procedures we de- 
scribe in the following. Nevertheless, we believe it is important to have at 
least a grasp of what is done, in order to properly apply variance reduction 
procedures to improve the estimates. 

226 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
for 
end 
i=l :N 
seed = mod(a*seed+c, m); 
ZSeq(i) = seed; 
USeq(i) = seedh; 
Fig. 4.5 Code to generate random numbers by a linear congruential generator. 
4.3.1 
Generating pseudorandom numbers 
The standard textbook method to generate U ( 0 , l )  variates, is based on linear 
congruential generators (LCGs). A LCG generates a sequence of non-negative 
integer numbers Zi as follows; given an integer number Zi-1, we generate the 
next number in the sequence by computing 
Zi = (aZi-1 + c) mod m, 
where a (the multiplier), c (the shift), and m (the modulus) are properly 
chosen parameters and mod denotes the remainder of integer division (e.g., 
15 mod 6 = 3). Then, to generate a uniform variate on the unit interval, we 
return the number (&/m). 
Example 4.4 In figure 4.5 we display MATLAB code to implement a LCG. 
Running the code with some choice of the parameters a, c, and m yields 
>> a=5; 
>> c=3; 
>> m=16; 
>> seed=7; 
>> N=20; 
>> [USeq, ZSeq] = LCC(a,c,m,seed,N); 
>> fprintf(l,’%2d %2d 16.4f \nJ, [(l:N)’, ZSeq, USeq]’) 
1 6 0.3750 
2 1 0.0625 
3 8 0.5000 
4 11 0.6875 
5 10 0.6250 
6 5 0.3125 
7 12 0.7500 
8 15 0.9375 
9 14 0.8750 
10 9 0.5625 

GENERATlNG PSEUDORANDOM VARIATES 
227 
11 0 0.0000 
12 3 0.1875 
13 2 0.1250 
14 13 0.8125 
15 4 0.2500 
16 7 0.4375 
17 6 0.3750 
18 1 0.0625 
19 8 0.5000 
20 11 0.6875 
U 
It is clear that there is nothing random in the sequence generated by a LCG. 
To begin with, it must start from an initial number 20; 
this is called the seed 
of the sequence. Starting the sequence from the same seed will always yield 
the same sequence. Indeed, any time you start MATLAB and type rand, you 
get the same number; if you keep typing rand, you see a sequence of numbers 
that look random and uniformly distributed. However, this sequence is always 
the same, since starting MATLAB sets the seed to a precise value. This may 
seem rather dull, and using a command like 
rand(’seed’ ,sum(lOO*clock)), 
which sets the seed of the random generator to a number depending on the 
current clock value, may seem a brilliant idea. In practice this is not a good 
idea at all; on the one hand, it makes debugging difficult; on the other one, 
the variance reduction techniques we describe in the following may call for 
the ability to control the seeds3 
A few remarks are in order. A first observation is that with a LCG we 
actually generate rational numbers rather than real ones; this is not a serious 
problem, provided that m is large enough. But there is another reason to 
choose a large value for m; the generator is periodic. In fact, we may generate 
at most m distinct integer numbers Zi, in the range from 0 to m - 1, and 
whenever we repeat a previously generated number, the sequence repeats itself 
(which is not very random at all). We may see from the previous example 
that we get back to the initial seed 20 = 7 after 16 steps. This is not too bad, 
as 16 is the maximum possible period, for m = 16. We do much worse if we 
select a = 11, c = 5, and m = 16. In this case, starting from 20 = 3, we get 
the following sequence of integer numbers Zi: 
6, 
7, 
2, 
11, 
14, 15, 10, 3 
which has half the maximal period. Since the maximum possible period is 
m, we should make it very large in order to have a large period. The proper 
3Actually, this need is evident when we have a complex simulation with multiple sources of 
uncertainty. 

228 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
choice of a and c ensures that the period is maximized and that the sequence 
looks random. A sequence like 
i 
u. 
1 -  - - 
m’ 
i = O , l , .  . . 
which is obtained if a = c = 1, has a maximum period and is, in some sense, 
uniformly distributed on the interval ( O , l ) ,  but it is far from satisfactory. The 
point is that the samples should also look independent; to be more precise, 
they should be able to trick statistical testing procedures into “believing” that 
they are a sequence of independent samples from the uniform distribution. 
This is why designing a good random number generator is not easy; luckily, 
when you purchase good numerical software, someone has already solved the 
issue for you. 
Example 4.5 Consider the generator Zi = (aZi-1) mod m with a = 216+3 
and m = 231. It is fairly easy to show that for the sequence Ui = Zi/m the 
expression 
takes integer  value^.^ In fact, given Zi (integer) we have 
Ui+2 - 6Ui+1 + 9Ui 
Zi+l = a& mod m = a& - k l m  
for some integer kl. We also have 
z i + ~  = 
= 
aZi+i mod m = a (aZi mod m) mod m = a (a& - k l m )  - kzm 
a2Zi - (akl+ k2)m = a’& mod m 
for some integer kz. This implies 
zi+~ 
- 6zi+l + gzi 
= 
= 
= 
= 232Zi - km, 
(216 + 3)’Zi mod m - 6(216 + 3)Zi mod m + gZi 
[(216 + 3)’Zi - 6(216 + 3)Zi + 9Zi] - k m  
(Z3’ 
+6 216 + 9 - 6 216 - 18+ g)zi - k m  
Therefore 
is integer. This means that points of the form (Ui, Ui+l, Ui+2) lie on a limited 
number of hyperplanes. 
0 
The type of phenomenon illustrated in the example results in a lattice struc- 
ture of LCGs. This concept may also be illustrated by the MATLAB script in 
4The examples below are taken from (14, pp. 22-25]. 

GENERATING PSEUDORANDOM VARIATES 
229 
1 Rip1eyLCG.m 
m = 2048; 
a = 65; 
c = 1; 
seed = 0; 
u = LCG(a,c,m,seed, 2048); 
subplot(2,1,1) 
plot(U(1:m-l), U(2:m), ’ . ’ I ;  
subplot(2,1,2) 
plot(U(1:511), U(2:512), ’. ’1; 
1 
a=1365; 
c=l ; 
u = LCG(a,c,m,seed, 2048); 
figure 
plot(U(i:m-I), 
U(2:m), ’ . ’ I ;  
Fig. 4.6 Script to illustrate the lattice structure of LCGs. 
figure 4.6, which yields the plot displayed in figures 4.7 and 4.8. The top part 
of figure 4.6 shows a fairly good filling of the unit square by points of the form 
(Ui,Ui+l), for the choice a = 65, c = 1, and m = 2048. This may suggest 
that the distribution is uniform and that consecutive samples behave as if 
they were “statistically independent”. However, the second part of the figure 
shows that the first part of the sequence follows some definite pattern. This 
is even worse in the second case, where a = 1365, whose pattern is displayed 
in figure 4.8. We see that selecting parameters for LCGs is not trivial, and 
many commercially used generators in the past were indeed flawed. 
The examples above show that LCGs may have several limitations. Indeed, 
LCGs were state of the art in the past. In fact, they were used in the release 
4 of MATLAB. Now a different approach is taken; we will not enter in any 
detail, but it suffices to say that the new generator is based on a state vector 
with 35 components (see [ll] for more information). By issuing a command 
like rand(state ,O>, 
we tell MATLAB to reset this state vector to the config- 
uration which is loaded when MATLAB is started. Another important point 
is that when generating normal variates, MATLAB uses the randn function; 
this function generates standard normal variates, and it has a separate state 
from the uniform generator. The state mechanism for randn is similar to that 
of rand; the important point to keep in mind is that they are separate, and 
resetting the state for the uniform generator is no use when you are generating 
normal variates (which is a common task when pricing options). 

230 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
"0 
0.2 
0.4 
0.6 
0.8 
1 
" 0 
0.2 
0.4 
0.6 
0.8 
1 
Fig. 4.7 Plots obtained by running the RipleyLCG script. 
4.3.2 
Inverse transform method 
Suppose we are given the distribution function F ( x )  = P{X 5 x } ,  and that 
we want to generate random variates according to F .  If we are able to invert 
F easily, we may apply the following inverse transform method: 
1. We draw a random number U N U(0,l). 
2. We return X = F-'(U). 
It is easy to see that the random variate X generated by this method is 
actually characterized by the distribution function F :  
P{X 5 X} = P{F-'(U) 5 X} = P{U 5 F ( x ) }  = F ( x ) ,  

GENERATING PSEUDORANDOM VARIATES 
231 
“0 
0.2 
0.4 
0.6 
0.8 
1 
Fig. 4.8 Plot obtained by running the RipleyLCG script. 
where we have used the monotonicity of F and the fact that U is uniformly 
distributed. 
Example 4.6 A typical distribution which can be simulated easily by the 
inverse transform method is the exponential distribution. If X - exp(p), 
where l/p is the expected value of X, its distribution function is 
F ( z )  = 1 - e - p x .  
Direct application of the inverse transform yields 
1 
P 
z = -- ln(1 - U ) .  
Since the distributions of U and (1 - U )  are actually the same, it is custom- 
ary to generate exponential variates by drawing a random number U and by 
returning - ln(U)/p. We may check that this is indeed the method used in 
the Statistics toolbox to simulate exponential random variables through the 
exprnd function: 
>> rand(’state’,O) 
>> exprnd(1) 
ans = 
0.0512 
>> rand(’state’,O) 
>> -log(rand) 
0.0512 
ans = 

232 
NUMERICAL INTEGRATION: DETERMlNlSTlC AND MONTE CARL0 METHODS 
Generating exponential random variables is useful when you have to simulate 
a Poisson process, which is a possible model for shocks in asset prices or credit 
rating. 
0 
The inverse transform method is quite simple, and it may also be applied 
when no theoretical distribution model is available and all you have is a set 
of empirical data. You just have to build a sensible distribution function 
based on your data set (see, e.g., [9]); one way to build a distribution function 
in this case is linear interpolation, and inverting a piecewise linear function 
is easily accomplished. However, we may not apply the inverse transform 
method when F is not invertible, as it happens with discrete distributions (in 
this case the distribution function is piecewise constant, with jumps where 
probability mass is concentrated). Nevertheless, we may adapt the method. 
Consider a discrete empirical distribution with a finite support: 
P ( X  = Xj} =pj, 
j = 1,2,. . .,n. 
Then we should generate a uniform random variate U and return X as 
It may be instructive to see how this code may be implemented in a simple 
way (not the most efficient one, however). Suppose we have a distribution 
defined by probabilities 
0.1 0.2 0.4 0.2 0.1 
over values 1,2,3,4,5. First we define cumulative probabilities: 
0.1 0.3 0.7 0.9 1.0, 
then we draw a uniform random number, say U = 0.82. For each cumulative 
probability P we may check if U > P, yielding a vector 
1 1 1 0 0 ,  
where 1 corresponds to “true” and 0 to “false.” To select the right value to 
return, we must sum the ones in this vector (the total is 3 here) and add 
1; in this case we should return the value 4. Using MATLAB, this may be 
accomplished by working on vectors; code is displayed in figure 4.9 (howmany 
is the number of samples we want). For the example we are considering, we 
may check the function by plotting a histogram: 
>> rand(’state’,O) 

GENERATING PSEUDORANDOM VARIATES 
233 
function samples = EmpiricalDrnd(values, probs, howmany) 
% get cumulative probabilities 
cumprobs = cumsum(probs) ; 
N = length(probs1; 
samples = zeros(howmany, 1) ; 
for k=l : howmany 
loc=sum(rand*cumprobs(N) > cumprobs) + 1; 
samples(k)=values(loc) ; 
end 
Fig. 4.9 Sampling from an empirical discrete distribution. 
Fig. 4.10 Histogram produced by calling EhpiricalDrnd. 
>> values=l:5; 
>> probs=[0.1 0.2 0.4 0.2 0.11; 
>> samples=FmpiricalDrnd(values ,probs ,10000) ; 
>> hist (samples, 5) 
The resulting histogram is displayed in figure 4.10. 
For many relevant distributions, the distribution function is invertible, but 
this is not easily accomplished. In such a case, one possibility is to resort to 
the acceptance-rej ection met hod. 
4.3.3 
Acceptance-rejection method 
Suppose we must generate random variates according to a probability density 
f(x), and that the difficulty in inverting the corresponding distribution func- 

234 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
T 
O
A
 
B 
1 
fig. 4.11 Graphical example of the acceptance-rejection method. 
tion makes the inverse transform method unattractive. Assume that we know 
a function t(x) such that 
t(X) 2 f(.) 
vx E 1, 
where I is the support of f. The function t(x) is not a probability density, 
but the related function ~ ( x )  
= t(x)/c is, provided that we select 
c = lt(x) dx. 
If the distribution r(x) is easy to simulate, it can be shown that the follow- 
ing acceptance-rejection method generates a random variate X distributed 
according to the density f: 
1. Generate Y N r. 
2. Generate U N U(0, l), independent of Y .  
3. If U 5 f (Y)/t(Y), 
return X = Y; 
otherwise, repeat the procedure. 
If the support I is bounded, a natural choice for ~ ( x )  
is simply the uniform 
distribution on I ,  and we may choose 
t(x) = maxf(x). 
X E I  
We will not prove the correctness of the method, but an intuitive grasp can be 
gained from figure 4.11. In the figure, the support of f(x) is the unit interval. 
A typical distribution that looks like f is the beta distribution: 

GENERATING PSEUDORANDOM VARIATES 
235 
provided that the parameters satisfy a1,a2 > 1 (the beta distribution does 
not require this condition, but its appearance would be different from figure 
4.11). The beta function is defined as 
1 
B(cr1, a2) = 1 xa1-'(l - z)Q2-1 dz. 
The Y variables are generated according to the uniform distribution and will 
spread evenly over the unit interval. Consider point A; since f ( A )  is close to 
t(A), A is likely to be accepted, as the ratio f(A)/t(A) 
is close to 1. When we 
consider point B, where the value of the density f is small, we see that the 
ratio f(B)/t(B) is small; hence, B is unlikely to be accepted, which is what 
we would expect. It can also be shown that the average number of iterations 
to terminate the procedure with an accepted value is c. 
Example 4.7 Consider the density 
f(.) 
= 30(x2 - 2 2  + 
x E [O, 11. 
The reader is urged to verify that this is indeed a density (actually, it is the 
beta density with 01 = a2 = 3). If we apply the inverse transform method, 
we have to invert a fifth-degree polynomial at each generation, which suggests 
use of the acceptancerejection method. By ordinary calculus we see that 
max f(z) = 30/16 
XE[O,11 
for x* = 0.5. Using the uniform density as the easy density r, we get the 
following algorithm: 
1. Draw two independent and uniformly distributed random variables U1 
and U2. 
2. If U2 5 16(U; - 2U: + V,"), accept X = U1; otherwise, reject and go 
back to step 1. 
The average number of iterations to generate one random variate is 30/16. n 
4.3.4 
The inverse transform and acceptancerejection methods are general purpose, 
but they are not always applicable. In the case of normal variables inverting 
the cumulative distribution function is no easy task, nor may we easily find a 
majorant function for the normal density, since its support is not finite. Actu- 
ally, efficient approximations have been developed for the inverse distribution 
function for normal random variables. In MATLAB, a function call like 
Generating normal variates by the polar approach 
x = norminv(p, mu, sigma) 

236 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
returns the quantile for probability p of a variable with expected value mu 
and standard deviation sigma This can be used to generate samples from the 
standard normal distribution, but it may not be the most efficient way: 
>> t i c ,  Z = norminv(rand(1000000,1));, toc 
Elapsed time is 1.279080 seconds. 
>> t i c ,  Z = randn(1000000,1);, toc 
Elapsedtime is 0.048054 seconds. 
Here, function randn uses a recent ad hoc method for the generation of 
normal variates. We outline here the basics of the classical polar approach, 
which may be outdated but is a nice example of ad hoc method. 
Recall first that if X - N(0, l), then p + uX N N ( p , a 2 ) ;  hence we just 
need a method for generating standard normal variables. One old-fashioned 
possibility, which is still suggested in some textbooks, is to exploit the central 
limit theorem and to generate and sum a suitable number of uniform variates. 
Although this approach would work in the limit, computational efficiency 
would restrict the number of uniform variates that we use. The result is 
that we obtain a variate which could be of sufficient quality in noncritical 
simulations in which we are interested in average values, but is of debatable 
quality when we are interested in critical behavior in the tail of the distribution 
(as is the case in Value at Risk computations). 
An alternative method is the Box-Muller approach. Consider two indepen- 
dent variables X ,  Y N N(0, l), and let (R, 0) be the polar coordinates of the 
point of Cartesian coordinates (XI Y )  in the plane, so that 
d = R2 = X 2  + Y 2  
0 = tan-’ Y / X  
The joint density of X and Y is 
The last expression looks like a product of an exponential density for d and 
a uniform distribution; the term 1 / 2 ~  
may be interpreted as the uniform 
distribution for the angle 6’ E (0,27r). However, we are missing some constant 
term in order to obtain the exponential density. To express the density in 
terms of (d,e), we should properly take the Jacobian of the transformation 
from (2, y) to (d, 0) into a c ~ o u n t . ~  
Some calculations yield 
dd 
dd 
- 
dx dy 
ae 
de 
dx ay 
J =  - 
= 2, 
’See, e.g., [16] for details. 

G€NERAT/NG PSEUDORANDOM VARIATES 
237 
and the correct density in the alternative coordinates is 
1 1  
2 2lr 
f(d, e) = - - c d j 2  
Hence, we may generate R2 as an exponential variable with mean 2 and 
0 as a uniformly distributed angle, and then transform back into Cartesian 
coordinates in order to obtain two independent standard normal variates. The 
Box-Muller algorithm may be implemented as follows: 
1. Generate two independent uniform variates U1, UZ N U(0,l). 
2. Set R2 = -2 log U1 and B = 21rU2. 
3. Set X = Rcose, Y = Rsine. 
In practice, this algorithm may be improved by avoiding the costly evaluation 
of trigonometric functions and integrating the Box-Muller approach with the 
rejection approach. The idea results in the following polar rejection method: 
1. Generate two independent uniform variates U1, Uz - U(0,l). 
2. Set ~1 = 2 ~ 1 -  
1, VZ = 2
~
2
 
- 1, S = Vf + V:. 
3. If S > 1, return to step 1; otherwise, return the independent standard 
normal variates: 
We refer the reader to [15, section 5.31 for a justification of the polar rejection 
method. 
Example 4.8 We have seen that LCGs may exhibit a lattice structure. Since 
the Box-Muller transformation is non-linear, one might wonder if the com- 
position of these two features may yield weird effects. We may check this 
in a somewhat peculiar case (see [14]), using the MATLAB script in figure 
4.12. The script generates 2046 uniform random numbers for a sequence with 
modulus m = 2048; we discard the last pair, because the generator has maxi- 
mum period and reverts back to the seed, which is 0 and causes trouble with 
the logarithm. Vectors U1 and U2 contain odd- and even-numbered random 
numbers in the sequence. The first part of the resulting plot, displayed in 
figure 4.13, shows poor coverage of the plane. The second part shows that 
swapping the pairs of random numbers may have a significant effect, whereas 
with truly random numbers the swap should be irrelevant. Of course, using 
better LCGs, or better random number generators prevents pathological be- 
havior like this. However, it may be sometimes preferable to use the inverse 
transform method. 
0 

238 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
X Ripley2.m 
m = 2048; 
a = 1229; 
c = 1; 
N = m-2; 
seed = 0; 
U = LCG(a,c,m,seed,N); 
U2 = U(2:2:N); 
X=sqrt(-2*1og(Ul)).* cos(2*pi*U2); 
Y=sqrt(-2*log(Ul)).* sin(2*pi*U2); 
figure 
subplot (2,1,1) 
plot(X,Y,'. '1; 
~=sqrt(-2*log(U2)). * cos(2*pi*U1); 
Y=sqrt(-2*log(U2)).* sin(2*pi*U1); 
subplot (2,1,2) 
plot (X ,Y, ' . '1 ; 
U1 = U(l:2:N-l); 
Fig. 4.12 Script to check Box-Muller approach. 
In many financial applications one has to generate variates according to a 
multivariate normal distribution with (vector) expected value p and covari- 
ance matrix C. This task may be accomplished by obtaining the Cholesky 
factor for C ,  i.e., an upper triangular matrix U such that C = UTU (see 
section 3.2.3). Then we may apply the following algorithm: 
1. Generate n independent standard normal variates 21,. . . , 2, N N(0,l). 
2. Return X = p + UTZ, where Z = [Z,, . . . , Z,lT 
Example 4.9 A rough code to simulate multivariate normal variables is 
illustrated in figure 4.14. The code builds a matrix whose columns correspond 
to the different variables, and the rows correspond to the different realizations 
of them. Assume that we have the following parameters: 
>> Sigma = [4 1 -2 ; 1 3 1 ; -2 1 51; 
>> mu = [ 8 ; 6 ; 101; 
>> eig(Sigma) 
1.2855 
4.1433 
6.5712 
ans = 

GENERATING PSEUDORANDOM VARIATES 
239 
4 
-4 
-4 
-3 
-2 
-1 
0 
1 
2 
3 
4 
...................... 
........ 
2 
..... 
2.5 
;,,. 
................. 
....... 
................ 
-.. 
/(@ 
,,./.'"' 
~ 
......... '\ 
.. 
..... 
..... 
..... 
........................ 
-2 
-1 
0 
1 
2 
3 
- 
4 
Fig. 4.13 Effect of swapping random numbers in the Box-Muller transformation. 
Note that we make sure that the matrix C is positive definite, as it should be, 
by checking its eigenvalues. Now we may generate a few samples and verify 
the results. 
>> rand('state',O); 
>> Z = MultiNormrnd(mu,Sigma,10000) ; 
>> mean(Z) 
ans = 
8.0266 
6.0234 
9.9703 
>> COV(Z) 
ans = 
4.0159 
1.0193 -1.9671 
1.0193 
3.0011 
1.0171 
-1.9671 
1.0171 
5.0060 
We leave to the reader the exercise of improving the code, by checking that 
the vector and matrix sizes of the input arguments agree, by checking that 
the matrix Sigma is a positive definite symmetric matrix, and by avoiding the 

240 
NUMERKAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
function Z = MultiNormrnd(mu,sigma,howmany) 
n = length(mu); 
Z = zeros(howmany,n); 
mu = mu(:); 1 make sure it’s a column vector 
U = chol(sigma); 
for i=l:howmany 
end 
Z ( i , : )  
= mu’ + randn(1,n) * U; 
fig. 4.14 Code to simulate multivariate normal variables. 
for loop. Then have a look at the function mvnmd, included in the Statistics 
toolbox, which does just this job. 
0 
4.4 
SETTING THE NUMBER OF REPLICATIONS 
Carrying out a Monte Carlo simulation entails the generation of samples of 
the quantity of interest and then an estimation of the relevant parameters. 
One would expect that the larger the number of samples, or replications, the 
better the quality of the estimates will be. From appendix B we recall that 
given a sequence of independent (and we stress the independence) samples X i ,  
drawn from the same underlying distribution, we may build the sample mean: 
-
r
l
 
1 
X ( n )  = - C X ~ ,  
n i=l 
which is an unbiased estimator of the parameter p = E[Xi], and the sample 
variance: 
l
n
 
S2(n) = - 
C [xi - X(n)] ’ . 
n - 1 ,  
Z=1 
We may try to quantify the quality of our estimator by considering the ex- 
pected value of squared error of estimate: 
2 
n 
E[(X(n) - P ) ~ ]  
= Var[X(n)] = -, 
where 0’ may be estimated by the sample variance. Clearly, increasing the 
number n of replications improves the estimate; but how can we reasonably 
set the value of n? 
Recall that the confidence interval at level (1 - a) may be computed as 
(4.5) 

SETTING THE NUMBER OF REPLICATIONS 
241 
where ~ 1 - ~ / 2  
is the quantile of the standard normal distribution corresponding 
to probability 1 - a. Strictly speaking, this is just an approximation, which 
will be a good one provided that n is large enough, both because X(n) will 
be approximately normal (central limit theorem) and because the quantile 
t n - l , l - a / 2  
from the t distribution with n - 1 degrees of freedom tends to 
Z1-a. 
Suppose you are interested in controlling the absolute error in such a way 
that, with probability (1 - a), 
I X(n) - p I< P, 
where /? is the maximum acceptable tolerance. But the confidence interval 
(4.5) is just built in such a way that 
P{X(n) - H < p L X(n)+ H }  M 1-0, 
where we denote the half-length of the interval by 
H = z 1 - 4 2 m m  
of the confidence interval. This implies that, with probability 1 - a, we have 
X(n) - p I H ,  p - X(n) < H + I X(n) - p 15 H. 
Hence, linking H to P, we should simply run replications until H is less than 
or equal to the tolerance P, and the number n must satisfy 
z 1 - a , 2 d 3 m F  I P. 
(4.6) 
Actually, we are chasing our tail a bit here, since we cannot estimate the 
sample variance S2(n) until the number n has been set. One way out is to 
run a suitable number, say k = 30, of pilot replications, in order to come up 
with an estimate S2(k). Then we may apply (4.6) using S2(k) to determine 
n. After running the n replications, it is advisable to check that equation 
(4.6) holds with the new estimate S2(n). Alternatively, we may simply add 
replications, updating the sample variance, until the criterion is met; however, 
with this approach we do not control the amount of computation we are willing 
to spend. 
If you are interested in controlling the relative error, so that 
holds with probability (1 -a), things are a little more involved. The difficulty 
is that we may run replications until the half-length H satisfies 
H 

242 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
function [Price, CI] = BlsMC2(SO ,K, r , T, sigma, NRepl) 
nuT = (r - O.5*sigmaa2)*T; 
siT = sigma * sqrt(T) ; 
DiscPayoff = exp(-r*T)*max(O, SO*exp(nuT+siT*randn(NRepl,l))-K) ; 
[Price, VarPrice, CI] = normf it (Discpayoff 1 ; 
Fig. 4.15 Revised code to price a vanilla European call by Monte Carlo simulation. 
but in this inequality we are using the known quantity X(n) rather than the 
unknown parameter p. Nevertheless, if the inequality above holds, we may 
write 
where inequality (4.7) follows from the triangle inequality and the last equa- 
tion is obtained by a slight rearrangement. Therefore, we see that if we pro- 
ceed without care, the actual relative error we get is bounded by y/(l - y), 
which is larger than the desired bound y; so, we should choose n such that 
the following criterion is met: 
where 
yl = -2- < y. 
l+Y 
Again, we should run some pilot replications in order to get a first estimate 
of the sample variance S2 (n). 
Confidence intervals in MATLAB may be computed using the normfit 
function. This function is part of the Statistics Toolbox and it assumes that 
we are fitting a normal distribution based on samples from the normal distri- 
bution, which is not exactly what we have in mind; nevertheless, the way it 
computes confidence intervals fits our purpose. By default, normf it returns 
a 95% confidence interval, and different values may be specified, as usual in 
MATLAB, by passing an optional parameter. 
Example 4.10 We may extend the code for pricing a vanilla call in order 
to compute confidence intervals on prices, as shown in figure 4.15. Note that 

SETTlNG THE NUMBER OF REPLICATIONS 
243 
in the last line we must collect three output arguments from normfit; the 
second one is sample variance, which is discarded. We can pIay a bit with 
BlsMC2 in order to get a feeling for how many replications are needed to get 
a fairly accurate estimate: 
>> randn( ’state’, 0 )  
>> S0=50; 
>> K=55; 
>> r=0.05; 
>> T=5/12; 
>> sigma=0.2; 
>> Call = blsprice(SO,K,r,T,sigma) 
Call = 
>> [CallMC, CI] = BlsMC2(SO,K,r,T,sigma,50000) 
CallMC = 
CI = 
1.1718 
1.1953 
1.1704 
1.2201 
>> (CI(2)-CI(l))/CallMC 
ans = 
0.0416 
We may notice that with 50000 samples the estimate is not quite satisfactory; 
however the true value is within the confidence interval, even though close 
to the left end-point. Of course, in a practically relevant case, we could only 
notice that the confidence interval is fairly wide. It may take a very large 
number of replications to get a reliable estimate: 
>> [CallMC, CI] = BlsMC2(S0,K,r,T,sigma,1000000) 
CallMC = 
CI = 
1.1749 
1.1694 
1.1804 
>> (CI(2)-CI(l))/CallMC 
ans = 
0.0094 
From equation (4.5) we see that the rate of improvement of the quality of our 
estimate, i.e., the rate of decrease of the error, is something like O(l/&). In 
practice, this means that the more samples we get the better, but the rate of 
improvement is slower and slower as we keep adding samples. Thus a brute- 
force Monte Carlo simulation may take quite some amount of computation to 
yield an acceptable estimate. One way to overcome this issue is to adopt a 
clever sampling strategy in order to reduce the variance o2 of our samples; 
the other one is to adopt a quasi-Monte Carlo approach. 

244 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
4.5 
VARIANCE REDUCTION TECHNIQUES 
We have seen in section 4.4 that one way to improve the accuracy of an 
estimate is to increase the number of replications n, since Var(x(n)) = 
Var(Xi)/n. However, this brute-force approach may require an excessive com- 
putational effort. An alternative is to work on the numerator of this fraction 
and to reduce the variance of the samples Xi directly. This may be accom- 
plished in different ways, more or less complicated, and more or less rewarding 
as well. 
4.5.1 Antithetic sampling 
A first approach that is easy to apply and does not require deep knowledge of 
what we are simulating is antithetic sampling. In plain Monte Carlo, we gen- 
erate a sequence of independent samples. However, inducing some correlation 
in a clever way may be helpful. Consider the idea of generating a sequence of 
paired replications (Xiz), Xt’), i = 1,. . . , n: 
These samples are “horizontally” independent, in the sense that Xj(E1) and 
Xf2) are independent however we choose j ,  k = 1,2, provided il # i2. Thus 
the pair-averaged samples X(2) = (Xii’ + Xt’)/2 are independent, and we 
may build a confidence interval based on them. However, we do not require 
“vertical” independence, since for a fixed i, Xii) and Xt) may be dependent. 
If we build the sample mean X(n) based on the samples X(i), 
4n 
We see that, in order to reduce the variance of the sample mean, we should 
take negatively correlated replications within each pair. Each sample Xi$ is 
obtained by generating random variates according to one of the methods we 
have described before; but all of these methods exploit a stream of uniformly 
distributed random numbers. Hence, to induce a negative correlation, we may 
use a random number sequence { Uk} for the first replication in each pair, and 
then (1 - U k }  in the second one. Since the input streams are negatively 
correlated, we hope that the output streams will, too. 

VARIANCE REDUCTION TECHNIQUES 
245 
Example 4.11 Let us repeat example 4.2, where we used Monte Carlo in- 
tegration to estimate 
1 
I = 
e" dx = e - 1 M 1.7183. 
With only 100 samples, we do not get a reliable estimate: 
>> randn( ' state ' ,O) 
>> X=exp(rand(100,1)); 
>> [I,dummy,CII = normfit(X1; 
>> I 
I =  
>> (CI (2) -CI(l) )/I 
ans = 
1.7631 
0.1089 
Antithetic sampling is easily accomplished here. We must store random num- 
bers and take their complements to one. In order to have a fair comparison, 
we consider 50 antithetic pairs, which means 100 function samples as before: 
>> randn( 'state' ,O) 
>> Ul=rand(50,1) ; 
>> u2=1-u1; 
>> x=o .5* (exp(Ul)+exp(U2)) ; 
>> [I, dummy ,CI] = normf it (XI ; 
>> I 
I =  
1.7021 
>> (CI (2) -CI (1)) /I 
ans = 
0.0200 
Now the confidence interval is much smaller and, despite the limited number 
of samples, the estimate is fairly reliable. 
0 
The antithetic sampling method looks quite easy to apply and, in the example 
above, it works pretty well. May we always expect a similar pattern? Of course 
not. To begin with, if we integrate the exponential function over [0,1] there is 
a strong positive correlation between U and eu because the function is almost 
linear there. We should not expect impressive results in more complex cases. 
Moreover, the following counterexample shows that the method may actually 
backfire, resulting in an increase in the variance. 
Example 4.12 Consider the function h(x), defined as 
x < o  
0 5 x _< 0.5 
0.5 5 x 5 1 
x > l  
2 - 2 ~ ,  
h(x) = 

246 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
and suppose that we want to take a Monte Carlo approach to estimate 
1' h(x) dx. 
The function we want to integrate is obviously a triangle with both basis and 
height equal to 1; note that, unlike the exponential function of example 4.11, 
this is not a monotone function with respect to x. It is easy to compute the 
integral as the area of a triangle: 
1 
1 
h(x) dx + E[h(U)] = / h(u). 1 du = 1/2. 
0 
Now let 
where U1 and V2 are independent uniform variates, be the usual sample based 
on independent sampling, and let 
h(V) + h(1 - V )  
2 
x* = 
be the pair-averaged sample built by antithetic sampling. We may compare 
the two variances: 
Var(Xr 
V 4 X A )  
The difference between 
Var[h(V)] 
Cov[h(U), h(1- V ) ]  
2 
+ 
- 
- 
2 
the two variances is 
Cov[h(U), h(l - V ) ]  
A = Var(XA) - Var(X1) = 
2 
1 
= - {E[h(U)h(l - V ) ]  - E[h(U)]E[h(l - V ) ] } .  
2 
But in this case, due to the shape of h, we have 
E[h(U)] = E[h(l - V)] = 1/2 
and 
112 
E[h(U)h(l - U ) ]  = 1 2u. (2 - 2(1 - u)) du + 
2(1 - u) . (2 - 2u) du 
1/2 
1 
= 1 4u2 du + Ll2(2 - 2
~
)
~
 
du = 1/3. 
Therefore, Cov[h(U), h(1 - V)] = 1/3 - 1/4 = 1/12 and A = 1/24 > 0, and 
antithetic sampling actually increases variance in this case. 

VARlANCE REDUCTlON TECHNlQUES 
247 
function [Price, CI] = BlsMCAV (SO, K, r ,T, 
sigma, NRepl) 
nuT = (r - 0.5*sigma-2)*T; 
siT = sigma * sqrt (TI ; 
Veps = randn(NRep1,l) ; 
Payoff1 = max( 0 , SO*exp(nuT+siT*Veps) - K); 
Payoff2 = max( 0 , SO*exp(nuT+siT*(-Veps)) - K); 
DiscPayoff = exp(-r*T) * 0.5 * (Payoffl+Payoff2); 
[Price, VarPrice, CI] = normf it (DiscPayoff) ; 
Fig. 4.16 Using antithetic variates to price a vanilla European call by Monte Carlo 
simulation. 
Indeed, there is a trivial explanation. The two antithetic samples have the 
same value h(U) = h(1-U), so that Cov[h(U), h(1-U)] = Cov[h(U), h(U)] = 
Var[h(U)]. In this (pathological) case, the variance of the single sample is 
doubled by applying antithetic sampling. 
0 
What is wrong with example 4.12? The variance of the antithetic pair is 
actually increased due to the non-monotonicity of h(s). In fact, while it is true 
that the random numbers {Ui} and (1 - Vi} are negatively correlated, there 
is no guarantee that the same holds for X!') and Xi in general. To be sure 
that the negative correlation in the input random numbers yields a negative 
correlation in the output samples, we must require a monotonic relationship 
between them. The exponential function is a monotonic function, but the 
triangle function of the second example is not. We should also pay attention 
to how random variates are generated. The inverse transform method is based 
on the distribution function, which is a monotonic function; hence, there is a 
monotonic relationship between the input random numbers and the random 
variates generated. This is not necessarily the case with the acceptance- 
rejection method or the Box-Muller method. Luckily, when we need normal 
variates, we may simply generate a sequence Z,, where Zi N N(0, l), and use 
the sequence -2, for the antithetic samples. This idea is best illustrated by 
applying antithetic sampling to option pricing in the simplest setting. 
We may easily incorporate antithetic sampling in our function BlsMC2 to 
price a European-style call option. MATLAB code is shown in figure 4.16. 
We simply generate a stream of standard normal variates and use the same 
sequence, with a change in sign, in the antithetic run. Each pair of antithetic 
samples is averaged and used as an estimator. Note that the last input pa- 
rameter] NPairs, is the number of antithetic pairs, rather than samples; this 
must be taken into account when checking the variance reduction with respect 
to crude Monte Carlo: 
(2) 
>> randn( 'state',O) 

248 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
>> [Price, CI] = BlsMC2(50,50 ,O. 05,l ,O. 4,200000) 
Price = 
CI = 
9.0843 
9.0154 
9.1532 
>> (cI(2)-CI(l))/Price 
ans = 
0.0152 
>> randn(’ state’ ,O) 
>> [Price, CI] = BlsMCAV(50,50,0.05,1,0.4,100000) 
Price = 
CI = 
9.0553 
8.9987 
9.1118 
>> (CI(2)-CI(l))/Price 
ans = 
0.0125 
We see that some improvement is obtained, but it is not that impressive, 
in this case. Clearly, one run for one example does not allow to draw any 
conclusion, but it is a fact that antithetic sampling is a simple technical trick 
which does not exploit too much knowledge. 
In the case of a vanilla call option, the monotonicity condition required by 
antithetic sampling is met: the higher the sample from the standard normal 
distribution, the higher the terminal price of the underlying, and the higher 
the payoff. With non-monotonic payoffs, this need not be the case. We may 
illustrate this by using a payoff which is similar to the triangle function of 
example 4.12. The butterfly spread6 is a trading strategy involving options 
on the same underlying asset, with the same maturity, but with different strike 
prices. The payoff from this combination is illustrated in figure 4.17. It can 
be obtained by buying one call option with strike price K1, one call option 
with strike price K3 (K1 < K3), and by selling two call options with a strike 
K2 halfway between the other two. Since the butterfly spread is simply a 
combination of European calls, an option with that payoff may be directly 
priced by using Black-Scholes formula. 
Since the payoff is clearly non-monotonic, and we know the “correct” price, 
it is interesting to check whether antithetic sampling works in this case. A 
crude Monte Carlo approach leads to the code in figure 4.18. The function 
MCButterf ly receives the usual input arguments, plus the three strikes. Note 
the use of vectors In1 and In2 to collect the indexes corresponding to repli- 
cations in which the terminal asset price falls in the increasing region of the 
‘See, e.g., [6, chapter 81 for more option trading strategies. 

VARIANCE REDUCTION TECHNIQUES 
249 
Fig. 4.1 7 Payoff froni a butterfly spread. 
function [P, CI] = MCButterfly(SO,r,T,sigma,NRepl,Ki,K2,K3) 
nuT = (r-0.5*sigma-2)*T; 
siT = sigma*sqrt (T) ; 
Veps = randn(NRep1,l) ; 
Stocks = SO*exp(nuT + siT*Veps) ; 
In1 = find((Stocks > K1) & (Stocks < K2)); 
In2 = find((Stocks >= K2) & (Stocks < K3)); 
Payoff = exp(-r*T)*[(Stocks(Inl)-Kl); 
(K3-Stocks(In2)); . . . 
[P, v, CI1 = normfit(Payoff); 
zeros(NRep1 - length(In1) - length(In2) ,111 ; 
payoff (K1 < ST < K 2 )  or in the decreasing region (Kz 5 Sr < K:j); outside 
t,liose regions the payoff is zero. The two vectors are used to avoid for loops. 
The function MCAVButterf ly of figure 4.19 is a modification based on an- 
tithetic sarripling. The vector Veps contains the samples from the standard 
iior1r1al distribution, which are changed in sign to obtain the antithetic stock 
price samples Stocks2. Note that in this case we must preserve the order 
of' the samples so as to pair the corresponding payoffs properly; this is why 
tho code looks A bit inore involved, and it uses find in order to spot samples 
falling in the interval of zero, increasing, or decreasing payoff. 
It is comirion to choose I<2 close to the current stock price So, as this 
st,ratcgy is based on the bet that the stock price will not move too much. Let 
1.1s check the results in such a case. Using blsprice we may get the theoretical 
rcsult. 
>> SO = 60; 
>> K1 = 55; 
>> K2 = 60; 

250 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
function [P, CI] = MCAVButterfly(SO,r,T,sigma,NPairs,Kl,K2,K3) 
nuT = (r-0.5*sigmaa2)*T; 
siT = sigma*sqrt(T) ; 
Veps = randn(NPairs,l) ; 
Stocksl = SO*exp(nuT + siT*Veps) ; 
Stocks2 = SO*exp(nuT - siT*Veps) ; 
Payoff 1 = zeros “Pairs, 1) ; 
Payoff 2 = zeros (NPairs, 1) ; 
In = find((Stocks1 > K1) & (Stocksl < K2)); 
Payoffl(1n) = (Stocksl(1n) - K1); 
In = find((Stocks1 >= K2) & (Stocksl < K3)); 
Payoffl(1n) = (K3 - Stocksl(1n)); 
In = find((Stocks2 > K1) & (Stocks2 < K2)); 
Payoff2(In) = (StocksZ(1n) - Kl); 
In = find((Stocks2 >= K2) & (Stocks2 < K3)); 
Payoff2(In) = (K3 - Stocks2(In)); 
Payoff = 0.5 * exp(-r*T) * (Payoff1 + Payoff2); 
[P, V, CI] = normf it (Payof f) ; 
Fig. 4.19 Using antithetic sampling to price a butterfly spread combination. 
>> K3 = 65; 
>> T = 5/12; 
>> r = 0.1; 
>> sigma = 0.4; 
>> calls = blsprice(S0, CK1, K2, K31, r, T, sigma); 
>> Price = calls(1) - 2*calls(2) + calls(3) 
Price = 
0.6124 
Next, we may compare the two Monte Carlo methods: 
>> randn(’state’ ,O) 
[P, CI] = MCButterfly(SO,r,T,sigma,100000,K1,K2,K3); 
>> P 
P =  
0.6095 
>> (C1(2)-CI(l))/P 
ans = 
0.0256 
>> randn(’state’.O) 
>> [P, CI] = MCAVButterf ly(S0,r ,T, sigma,50000,Kl ,K2,K3) ; 
>> P 
P =  
>> (C1(2)-CI(l))/P 
0.6090 

VARIANCE REDUCTION TECHNIQUES 
251 
ans = 
0.0355 
We may see that variance is actually increased in this case. This does not 
mean that you will always have an increase in variance, as this depends on 
the input data (try changing the strikes to see this). Anyway, since one run 
does not tell us much, a better comparison may be carried out by checking 
the standard error of estimate with respect to the exact result using multiple 
runs: 
Indeed, we see that the standard error of estimate is increased by antithetic 
sampling. 
4.5.2 
Common random numbers 
The common random numbers (CRN) technique is very similar to antithetic 
sampling, but it is applied in a different situation. Suppose that we use Monte 
Carlo simulation to estimate a value depending on a parameter a. In formulas, 
we are trying to estimate something like 
where we have emphasized randomness through the variable w .  We could also 
be interested in evaluating the sensitivity of this value on the parameter a: 
dh(a) 
da 
* 
This would be of interest when dealing with option sensitivities beyond the 
Black-Scholes model. Clearly, we cannot compute the derivative analytically; 
otherwise, we wouldn’t use simulation to evaluate h in the first place. So the 
simplest idea would be using simulation to estimate the value of the finite 
difference, 
h(a + Sa) - h(a) 
ba 
1 

252 
NUMERICAL IN JEGRAJION: DEJERMINISJK AND MONTE CARL0 METHODS 
for a small value of the increment ba. However, what we can really do is to 
generate samples of the difference 
f(a + 6a; 
w )  - f ( a ;  w )  
6a 
and to estimate its expected value. Unfortunately, when the increment 6cu 
is small, it is difficult to tell if the difference we obtain from the simulation 
is due to random noise or to variation in the parameter. A similar problem 
arises when we want to compare two portfolio management policies on a set 
of scenarios; in this case, too, what we need is an estimate of the expected 
value of the difference between two random variables. 
Let us abstract a little and consider the difference of two random variables 
where, in general, E[X1] # E[Xz], since they come from simulating two dif- 
ferent systems, possibly differing only in the value of a single parameter. By 
Monte Carlo simulation we get a sequence of independent samples 
zj = Xl,j - x2,j 
and use statistical techniques to build a confidence interval for E[X1- XZ] . To 
improve our estimate, it would be useful to reduce the variance of the samples 
Var(X1j - Xzj) = Var(X1j) + Var(Xzj) - 2 Cov(Xlj, X2j). 
To achieve this, we may try inducing some positive correlation between X1j 
and Xzj. This can be obtained by using the same stream of random numbers 
in simulating both X I  and XZ. The technique works much like antithetic 
sampling, and the same monotonicity assumption is required to ensure that 
the technique does not backfire. We will see an application of these concepts 
in section 8.5, where we apply Monte Carlo sampling to estimate option price 
sensitivities. 
zj : 
4.5.3 
Control variates 
Antithetic sampling and common random numbers are two almost foolproof 
techniques that, provided the monotonicity assumption is valid, do not require 
much knowledge about the systems we are simulating. Better results might 
be obtained by exploiting some more knowledge. Suppose that we want to 
estimate 6' = E[X], and that there is another random variable Y ,  with a 
known expected value u, which is somehow correlated with X. Such a case 
occurs when we use Monte Carlo simulation to price an option for which an 
analytical formula is not known: 0 is the unknown price of the option, and v 
is the price of a corresponding vanilla option. 

VARlANCE REDUCTKIN TECHNlQUES 
253 
The variable Y is called the control variate. Additional knowledge about 
Y may be exploited by adopting the controlled estimator 
xc = x + c(Y - u), 
where c is a parameter we must choose. Intuitively, when we run a simulation 
and we observe that our estimates are such that 
E[Y] > u, 
we may argue that the estimate E[X] should be increased or reduced accord- 
ingly, depending on the sign of the correlation between X and Y. Indeed, we 
may see that 
E[Xc] = 8 
Var(Xc) = Var(X) + c2Var(Y) + 2c COV(X, Y). 
The first formula says that the controlled estimator is, for any choice of the 
control parameter c, an unbiased estimator of 8. The second formula suggests 
that by a suitable choice of c, we could reduce the variance of the estimator. 
We could even minimize the variance by choosing the optimal value for c: 
COV(X, Y) 
Var(Y) ’ 
c* = - 
where pxy is the correlation between X and Y. Note that the sign of c 
depends on the sign of this correlation. For instance, if Cov(X, Y) > 0, then 
c < 0. This implies that if E[Y] > Y, we should reduce E[X], which does 
make sense, because if our sample values for Y are larger than the average, 
the sample values for X are probably too. 
In practice, the optimal value of c must be estimated, since Cov(X,Y) 
and possibly Var(Y) are not known. This may be accomplished by a set of 
pilot replications. It would be tempting to use these replications both for 
selecting c* and to estimate 8; however, in doing so you induce some bias in 
the estimate of 8, since in this case c* is a random variable depending on X 
itself. So, unless suitable statistical techniques are used, which are beyond 
the scope of this book, the pilot replications should be discarded. 
The control variates approach may be generalized to as many control vari- 
ates as we want, with a possible improvement in the quality of the estimates. 
Of course, this requires more knowledge about the system we are simulating 
and more effort in setting the control parameters. We may illustrate the ap- 
proach using again the vanilla call option. In this case the stock price is a 
natural control variate, as both its expected value and the variance at the 

254 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
function [Price, CI] = BlsMCCV(SO,K,r,T,sigma,NRepl,NPilot) 
nuT = (r - 0.5*sigma-2)*T; 
siT = sigma * sqrt(T) ; 
% compute parameters first 
StockVals = SO*exp(nuT+siT*randn(NPilot ,1)) ; 
OptionVals = exp(-r*T) * max( 0 , StockVals - K); 
MatCov = cov(StockVals, OptionVals); 
Vary = SO-2 * exp(2*r*T) * (exp(T * sigma-2) - 1); 
c = - MatCov(l,2) / Vary; 
ExpY = SO * exp(r*T) ; 
% 
NewStockVals = SO*exp(nuT+siT*randn(NRepl, 1) ; 
NewOptionVals = exp(-r*T) * max( 0 , NewStockVals - K); 
ControlVars = NewOptionVals + c * (NewStockVals - ExpY); 
[Price, VarPrice, CI] = normf it (ControlVars) ; 
Fig. 4.20 Using control variates to price a vanilla European call by Monte Carlo 
simulation. 
expiration of the option are known. To apply the method, we must compute 
an estimation of the covariance between the option value and the underlying 
asset price. The MATLAB code is illustrated in figure 4.20. The BlsMCCV 
function requires as an additional input parameter the number NPilot of pi- 
lot replications we want to run to estimate the covariance. Note that the first 
set of pilot replications is discarded to avoid biasing the estimator. 
>> randn( state ,O) 
>> [P,CI] = BlsMC2(50,52,0.1,5/12,0.4,200000); 
>> P 
P =  
>> (C1(2)-CI(l))/P 
5.2328 
ans = 
0.0149 
>> randn(’state’,O) 
>> [P ,CI] = BlsMCCV(50,52,0.1,5/12 ,O .4,195000,5000) ; 
>> P 
P =  
5.2008 
>> (C1(2)-CI(l))/P 
ans = 
0.0066 
From these runs it would seem that there is some reduction in variance by 
using control variates. We should prepare a script in order to systematically 
check gain in efficiency. This is left as an exercise for the reader. 

VARIANCE REDUCTION TECHNIQUES 
255 
4.5.4 
Variance reduction by conditioning 
Computing expected values by conditioning is a common technique in proba- 
bility theory. When we want to compute (or estimate) E[X], it is sometimes 
useful to condition with respect to another random variable Y, as the following 
formula holds: 
E[X] = E[E[X I Y]]. 
(4.9) 
Variances may be computed by conditioning, too. We recall the conditional 
variance formula [see also equation (B.2) in appendix B] 
Var(X) = E[Var(X I Y)] + Var(E[X I Y]). 
We do not use the conditional variance formula directly in this book. However, 
since all the involved quantities are non-negative, we immediately see that the 
formula implies two consequences: 
1. Var(X) 2 E[Var(X I Y)]. 
2. Var(X) 2 Var(E[X I Y]). 
Using the first inequality to reduce the variance of an estimator leads to 
variance reduction by stratification, which is discussed in the next section. 
The second one leads to variance reduction by Conditioning. 
Using conditioning is useful when our aim is to estimate 8 = E[X] and 
there is another random variable Y such that the value of E[X I Y = y] is 
known. From equation (4.9) we see that E[X I Y] is also an unbiased estimator 
for 8, and the conditional variance formula implies that it may be a better 
one. In practice, to apply variance reduction by conditioning, we simulate Y 
rather than X. Unlike antithetic sampling, variance reduction by conditioning 
requires some careful thinking and is strongly problem dependent. 
As an example of conditioning, we consider the problem of pricing an “as- 
you-like-it” option (also known as chooser option). The option is European- 
style and has maturity Tz. At time TI < TZ you may choose if the option is a 
call or a put; the strike price K is fixed at time t = 0. Clearly, at time TI we 
should compare the values of the two options and choose the more valuable 
one. This can be done by using Black-Scholes formula to evaluate the price of 
call and put options with initial underlying price S(T1) and time to maturity 
Tz -TI. This means that, conditional on S(T1), we may get an exact estimate 
of the expected payoff at time Tz, under the risk-neutral probability. However, 
it is extremely instructive to write a pure Monte Carlo code, in which we only 
use sampling to get estimates. 
In this case, this is not that trivial, as we must take a decision at time 
TI; this is similar to the early exercise decision we must take with American 
options. To get a feeling for the issues involved, let us consider figure 4.21. 
Starting from the initial node, with price So, we generate four samples of 
price S(Tl), and for each of these, we sample three prices S(T2). We have 


## PDEs and Finite Differences

256 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
t = O  
t=q 
t = T 2  
Fig. 4.21 Scenario tree for the as you like it option. 
4 x 3 = 12 scenarios, but they are tree-structured. We need this structure, 
because the decision at time TI (we like the put or the call) must be the 
same for all scenarios departing from each node at time TI. Without this 
structure, our decisions would be based on perfect foresight about the future 
price at time T2. This non-anticipativity concept is fundamental in dynamic 
stochastic optimization and in pricing American options. 
A crude Monte Carlo code to price the option is displayed in figure 4.22. 
Here NRepl 1 is the number of samples (replications) at time TI and NRepl2 
is the number of samples at time Tz, for each node at time TI; hence, the 
overall number of scenarios is the product of NRepll and NRepl2. The vector 
DiscountedPayof f s has size corresponding to the overall number of scenar- 
ios. For each node at T I ,  which is generated as usual with geometric Brownian 
motion, we generate nodes at time T2, and we compare the estimates of ex- 
pected payoff if we take the option as a call and if we take it as a put. Then 
we select one of the two alternatives and we fill a block (of size NRepl2) in 
the vector of discounted payoffs. Then we compute average and confidence 
intervals as usual. Later, we discuss if this is really correct. 
Clearly, we are doing much more work than necessary in the crude Monte 
Carlo code. Conditional on a price S(T1), we know how to estimate expected 
payoff from each of the two choices, as this is given (apart from a discount 
factor) by the Black-Scholes formula. A code exploiting such a knowledge is 
displayed in figure 4.23. The code is actually much simpler: for each node at 
time S(T1) we take the larger value between the price of a call and the price of 
a put with initial price S(T1) and time to maturity T2 - T I ,  and we discount 
this value back from TI to time t = 0. 
A script to compare crude and conditional Monte Carlo is given in figure 
4.24. Running the script, we get 

VARIANCE REDUCTION TECHNIQUES 
257 
function [Price, CI] = AYLIMC(SO,K,r,Tl,T2,sigma,NRepll,NRep12) 
% compute auxiliary quantities outside the loop 
DeltaT = T2-Tl; 
muTl = (r-sigmaA2/2)*Tl; 
muT2 = (r-sigma-2/2)*(T2-T1); 
siTl = sigma*sqrt (T1) ; 
siT2 = sigma*sqrt(T2-T1); 
X vector to contain payoffs 
DiscountedPayoffs = zeros(NRepll*NRepl2, 1); 
% sample at time T1 
Samples1 = randn(NRepl1,l); 
PriceTl = SO*exp(muTl + siTl*Samplesl); 
for k=l:NRepll 
Samples2 = randn(NRepl2,l) ; 
PriceT2 = PriceTl(k)*exp(muT2 + siT2*Samples2); 
Valuecall = exp(-r*DeltaT)*mean(max(PriceT2-K, 0)); 
ValuePut = exp(-r*DeltaT)*mean(max(K-PriceT2, 
0 ) ) ;  
if ValueCall > ValuePut 
, 
DiscountedPayoffs(l+(k-l)*NRepl2:k*NRepl2) 
= ... 
exp(-r*T2)*max(PriceTZ-K, 0 ) ;  
else 
DiscountedPayoffs(l+(k-l)*NRepl2:k*NRepl2) 
= ... 
exp(-r*T2)*max(K-PriceT2, 0 ) ;  
end 
end 
[Price, dummy, CI] = normfit(DiscountedPayoffs); 
~~ 
~ 
~ 
Fig 4 22 Crude Monte Carlo code to price an as-you-like-it option. 
function [Price, CI] = AYLIMCCond(SO,K,r,Tl,T2,sigma,NRepl) 
muTl = (r-sigma^2/2)*Tl; 
siTl = sigma*sqrt(Tl); 
Samples = randn(NRep1,l) ; 
PriceTl = SO*exp(muTl + siTl*Samples) ; 
[calls, puts] = blsprice(PriceTl,K,r,T2-Tl,sigma); 
Values = exp(-r*Tl)*max(calls, puts) : 
[Price, dummy, CI] = normfit(Va1ues) ; 
Fig. 4.23 Using conditioning to price an as-you-like-it option. 

258 
NUMERICAL INTEGRATION: DETERMlNlSTlC AND MONTE CARL0 METHODS 
% AYL1Script.m 
SO = 50; 
K = 50; 
r = 0.05; 
T1 = 2/12; 
T2 = 7/12; 
sigma = 0.4; 
NRepll = 100; 
NRepl2 = 100; 
[Call, Put] = blsprice(SO,KJr,T2,sigma); 
randn(’state’,O); 
[Price, CI] = AYLIMC(SO,K,r ,T1 ,T2, sigma,NRepll,NRepl2) ; 
rand(’state’,O); 
[PriceCond, CICond] = AYLIMCCond(S0,K ,r ,T1 ,T2, sigma,NRepll*NRepl2) ; 
fprintf(l,’Call= %f Put = %f\n’, Call, Put); 
fprintf(1,’MC -> 
Price = If 
CI = (%f, If) \nJ, . . . 
Price, CI(1), CI(2)); 
fprintf (1,’ 
Price = %6.4f%%\n’, . . . 
lOO*(CI(2>-CI(1))/Price); 
fprintf(l,’MC+Cond -> Price = %f 
CI = (%f, If) \nJ, ... 
PriceCond, CICond(l), CICond(2)) ; 
fprintf(1,’ 
Price = %6.4f%%\n’, ... 
100*(CICond(2)-CICond(l))/PriceCond); 
Fig. 4.24 Script to compare pricing methods for an as-you-like-it option. 

VARlANCE REDUCTKJN TECHNlQUES 
259 
>> AYLIScript 
Call = 6.728749 Put = 5.291478 
MC -> 
Price = 8.698173 CI = (8.489842, 8.906504) 
MC+Cond -> Price = 9.298894 CI = (9.218362, 9.379426) 
Ratio = 4.7902% 
Ratio = 1.7321% 
A few things should be noticed: 
1. The value of the as you like it option is larger than the value of the call 
and the put options; deferring the choice has a significant value. 
2. Conditioning seems to reduce variance, using the same number of sce- 
narios in the two cases. 
3. The value obtained by conditional Monte Carlo is larger. 
The last point is quite relevant. Using conditional Monte Carlo, we do not 
only reduce variance; we take truly optimal decisions, whereas in crude Monte 
Carlo we may take the wrong choice at time TI because we are comparing esti- 
mates of the expected payoff. This may happen even if we estimate the payoffs 
with the same samples of price at time Tz (which is essentially variance re- 
duction by common random numbers). Hence, we have a bias. The estimator 
with crude Monte Carlo is biased low, since we are getting less money from 
a suboptimal strategy. And the bias does not disappear by increasing the 
number of replications. We urge the reader to run the script setting both 
NRepll and NRepl2 to 1000, which results in the following output: 
>> AYLIScript 
Call = 6.728749 Put = 5.291478 
MC -> 
Price = 8.930494 CI = (8.909643, 8.951345) 
MC+Cond -> Price = 9.259405 CI = (9.251437, 9.267372) 
Ratio = 0.4670% 
Ratio = 0.1721% 
We see that the bias is still there. This must be taken into account when 
using Monte Carlo methods to price American options (see chapter 10). If we 
use suboptimal exercise strategies, than we get a lower bound on the option 
price. It is also worth noting that this pricing problem is essentially a one- 
dimensional integration problem which may be solved more efficiently by other 
techniques. 
To close this section, we should ask ourselves if the procedure we have 
followed is really correct. We have computed a confidence interval using the 
standard procedure, which assumes that samples are independent, but is this 
actually the case? Consider an intermediate node in our scenario tree, at time 
TI, and its successor nodes at time T2. Are the payoffs we receive in these 
successor nodes independent? Arguably, they are not, since we have used all 
of them to decide which option type we like at time TI. The problem is that 

260 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CAR10 METHODS 
we are mixing two issues. The first one is learning an optimal decision rule by 
sampling; the second one is estimating the payoff we receive with that rule. 
A sound procedure would require two separate sampling phases. Doing so, 
we would be sure that payoffs are independent in the second sampling phase, 
and that the estimate we get is low-biased (since we are probably using a 
sub-optimal decision rule). We will meet such issues again in section 10.4, 
where we consider pricing American options by Monte Carlo sampling. 
4.5.5 
Stratified sampling 
Suppose, as usual, that we are interested in estimating E[X] and that X is 
somehow dependent on the value of another variable random Y ,  which may 
take a finite set of values y j  with known probability. Thus, Y has a discrete 
probability distribution with a known probability mass function: 
P { Y = y j } = p j ,  
j = 1 ,  ..., m. 
Using conditioning, we see that 
m 
E[X] = C E [ X  I Y = yjlpj. 
j=1 
So, we may use simulation to estimate the values E[X I Y = yj], for j = 
1,. . . , m, and use the formula above to put the results together. The condi- 
tional variance formula implies that this may yield a variance reduction with 
respect to crude sampling. The approach may look like variance reduction 
by conditioning. The key difference is that here we select a value for Y and 
then we sample X, conditioned on the event Y = yj; this event is a stratum. 
In variance reduction by conditioning, you actually sample Y ,  not X. The 
following example justifies why such sampling is called stratified. 
Example 4.13 As a simple example of stratification, consider using simu- 
lation to compute 
0 = 1' h(x) dx = E[h(U)]. 
In crude Monte Carlo simulation you would simply draw n uniform random 
numbers Ui N U(0,l) and compute the sample mean 
An improved estimator over crude sampling may be obtained by parti- 
tioning the integration interval (0,l) into m subintervals ((j - l)/m,j/m), 
j = 1,. . . , m. Each event Y = y j  corresponds to a random number falling 

VARIANCE REDUCTION TECHNIQUES 
261 
in the jth subinterval; in this case we have p j  = l/m. For each stratum 
j = 1,. . . , m we may generate nj random numbers uk 
N U(0,l) to estimate 
Then we build the overall estimator: 
m 
B = c 
&pi. 
0 
j=1 
How should we determine the number of samples nj to be allocated to 
each stratum? A uniform allocation in example 4.13 makes sure that we 
sample uniformly over the integration interval (0, l), but this need not be the 
optimal solution. Consider the variance of the estimator 8, and denote by Xj 
the random variable sampled in each stratum. If the strata are independently 
sampled, we have 
To minimize the overall variance, we should allocate more samples to the 
strata where Var(Xj) is larger. So we could run a set of pilot replications 
to estimate Var(Xj) by sample variances Sj” and then obtain the fraction of 
samples to be allocated to each stratum by solving a non-linear programming 
problem: 
p?s? 
min xe 
j=1 
m 
s.t. Cnj = n 
4.5.6 
Importance sampling 
Unlike other variance reduction methods, importance sampling is based on the 
idea of “distorting” the underlying probability measure. It may be particularly 
useful when simulating rare events or sampling from the tails of a distribution. 
Consider the problem of estimating 
8 = E[h(X)] = 1 h(x)f(x) dx, 
where X is a random vector with joint density f(x). If we know another 
density g such that f(x) = 0 whenever g(x) = 0, we may write 
(4.10) 

262 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
where the notation E, is used to stress the fact that the last expected value is 
taken with respect to another measure. The ratio f(x)/g(x) is used to correct 
the change in probability measure, and it is typically called the likelihood 
ratio: when using random sampling, this ratio will be a random ~ a r i a b l e . ~  
That changing the underlying probability measure may be useful should not be 
a surprise for people interested in finance; risk-neutral valuation does just that. 
However, it is not so obvious why this should be helpful in reducing variance. 
Indeed, the method may backfire if g is not chosen with care. Intuitively, we 
may argue that when looking for rare but important events, as is the case in 
estimating Value at Risk, we should distort the probability measure in order 
to sample from the critical region, provided that we compensate for this bias. 
This is exactly what is done in equation (4.10). 
To gain more insight into how density g should be chosen, let us introduce 
the notation 
8 = E”)1 
and assume for simplicity that h(x) 2 0. As we have pointed out above, there 
are two possible ways of estimating 8: 
= /h*(x)g(x) dx = E,[h*(X)], 
where h*(X) = h(x)f(x)/g(x). Note that the condition on the support o f f  
and g is needed in order to avoid any trouble with the case g(x) = 0 in the 
definition of h*; we may think of integrating only on the support. 
The two estimators have the same expectation, but what about the vari- 
ance? Using the well-known properties of the variance, we obtain 
Varf[h(X)] = 1 
h2(x)f(x) 
dx - 8’ 
Var,[h*(X)] = Jh’(x)--f(x) 
f (4 
dx - 8’. 
g(x) 
From the second equation, it is easy to see that the choice 
leads to the ideal condition Varg[h*(X)] = 0. Unfortunately, this is indeed 
“ideal,” as using this density requires knowledge of 8; still, we may at least 
try to use approximations of the ideal density (see the example below). Note 
7Readers with a background in stochastic calculus would probably use the term “Radon- 
Nikodym derivative.” 

VARIANCE REDUCTION TECHNIQUES 
263 
function out=estpi(m) 
z=sqrt(l-rand(1,m) .-2) ; 
out = 4*sum(z)/m; 
Fig. 4.25 Trivial code to estimate T .  
also that the condition h(x) 2 0 is needed in order to ensure that this is a 
density; see, e.g., [17, p. 1221 to see how to deal with a generic function h. 
In general, the difference between the two variances is 
AVar = Varr[h(X)] -Var,[h*(X)] = /h2(x) [l - -1 f (XI f(x)dx. 
d x )  
From this expression we see that, in order to ensure that we do reduce variance, 
we should select a new density g such that 
g(x) > f(x) 
g(x) < f(x) 
when the term h2(x)f(x) is large, 
when the term h2(x)f(x) is small. 
The name “importance sampling” derives from this observation. 
Example 4.14 We may use a trivial integration example to illustrate the 
idea. Let us consider a way to compute T .  We know that8 
?T 
6 =  1’ d-dx= 
4, 
since this is simply the area of a quarter of a unit circle; hence, estimating the 
value of this integral is a possible way to obtain an estimate of T .  A trivial 
code to do this is shown in figure 4.25, where the input parameter m is the 
number of points we want to sample. From the snapshot below we see that 
with 1000 samples, the estimates are not so reliable. 
>> rand(’state’,O) 
>> estpi(1000) 
3.1378 
>> estpi(1000) 
3.1311 
>> estpi(1000) 
a n s  = 
ans = 
ans = 
sThis example is based on [2]. 

264 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
3.0971 
>> estpi(1000) 
3.1529 
ans = 
So, let us try to improve our estimates by using importance sampling. A 
possible idea to approximate the ideal probability distribution is to divide the 
integration interval [0,1] into L equally spaced subintervals of width 1/L. The 
extreme points of the kth subinterval (k = 1,. . . , L) are (k - 1)/L and k/L, 
and the midpoint of this subinterval is s k  = (k - 1)/L + 1/(2L). A rough 
estimate of the integral is obtained by computing 
Then, an approximation of the ideal density g(x), we could use something like 
since f(z) = 1 (uniform distribution). Unfortunately, this need not be a den- 
sity integrating to one over the unit interval. In order to avoid this difficulty 
and to simplify sampling, we may define a probability of sampling from a 
subinterval and use a uniform density 
consider the quantities 
within each subinterval. To this aim, 
k =  1, ..., L. 
Clearly, 
= 1 and q k  2 0, since our function h is non-negative; hence, 
the numbers q k  may be interpreted as probabilities. In our case, they may be 
used as the probabilities of selecting a sample point from the kth subinterval. 
To summarize, and to cast the problem within the general framework, we have 
h(x) = JD 
f(x) = 1 
g(X) = Lqk, 
(k- 1)/L< x < k/L. 
Here, g(x) is a piecewise constant density; the L factor multiplying the q k  in 
g(x) is just needed to obtain the uniform density over an interval of length 
1/L. The resulting code is illustrated in figure 4.26, where m is the number of 
sampled points and L is the number of subintervals. The code is fairly simple, 
and sub-intervals are selected as described in the last part of section 4.3.2, on 
page 233, where we have seen how to sample discrete empirical distributions 
by the function EmpiricalDmd. 
>> rand( ’ state ’ , 0) 

VARlANCE REDUCWON TECHNlQUES 
265 
function z=estpiIS(m,L) 
% define left end-points of sub-intervals 
s= (0: (1/L) : (l-l/L)) + 1/(2*L) ; 
hvals = sqrt(1 - s . ^ 2 ) ;  
% get cumulative probabilities 
cs=cumsum(hvals) ; 
for j=l:m 
% locate sub-interval 
loc=sum(rand*cs(L) > cs) +1; 
x=(loc-l)/L + rand/L; 
p=hvals(loc)/cs(L) ; 
est(j) = sqrt(1 - x.^2)/(p*L); 
sample uniformly within sub-interval 
end 
z = 4*sum(est)/m; 
Fig. 4.26 Importance sampling-based code to estimate 7r. 
>> estpiIS(1000,lO) 
ans = 
3.1491 
>> estpiIS(1000,10) 
ans = 
3.1434 
>> estpiIS(1000,10) 
ans = 
3.1311 
>> estpiIS(1000,100> 
ans = 
3.1403 
>> estpiIS(1000,lOO) 
ans = 
3.1416 
>> estpiIS(1000,100) 
ans = 
3.1411 
We see that the improved code, although not a very sensible way to compute 
x ,  yields a remarkable reduction in variance. 
The approach we have just taken looks suspiciously like stratified sampling. 
Actually, there is a subtle difference. In stratified sampling we define a set 
of strata, which correspond to events of known probability; here we have not 
used strata with known probability, as we have used sampling to estimate the 
probabilities q k .  
0 

266 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
Importance sampling is often used when small probabilities are involved. 
Consider, for instance, a random vector X with joint density f, and suppose 
that we want to estimate 
0 = E[h(X) 1 X E A], 
where {X E A} is a rare event with a small, but unknown probability P{X E 
A}. Such an event could be the occurrence of a loss larger than the Value at 
Risk. The conditional density is 
f (XI 
P{X E A} 
f(xlX E A) = 
for x E A. Defining the indicator function Id(x) as 
1 i f X E A  
Id(x) = { 0 i f X @ A ,  
we may rewrite 0 as 
If we use crude Monte Carlo simulation, many samples will be wasted, as the 
event {X E A} will rarely occur. Now, assume that there is a density g such 
that this event is more likely under the corresponding probability measure. 
Then, we may generate the samples Xi according to g and estimate 
Importance sampling is certainly more difficult to apply than antithetic sam- 
pling or control variates: It requires more knowledge about what we are sim- 
ulating, since we must be able to figure out a suitably distorted probability 
measure. 
As an example, let us consider pricing a deep out-of-the-money vanilla call. 
If SO is the initial price of the underlying, we know that its expected value at 
maturity is, according to geometric Brownian motion under the risk-neutral 
measure, SOerT. If this expected value is small with respect to the strike price 
K ,  it is unlikely that the option will be in-the-money at maturity. If we apply 
crude Monte Carlo, many replications are wasted because the payoff will be 
zero in most of them. We should change the drift in order to increase the 
probability that the payoff is positive. It is easy to find a drift such that the 
expected value of ST is the strike price: 
&ePT = K 

QUASI-MONTE CARL0 SIMULATION 
267 
While under the risk neutral measure we sample ST = SoeZ by generating 
we should sample by generating 
which in turn requires generating standard normal variates E and then using 
Y = l o g -  (E) -- 
u y  -t * f i e .  
Now the tricky part is to compute the likelihood ratio. For the sake of clarity, 
assume that we sample Y from a normal distribution n/(p,<) whereas the 
original distribution is N(Q, <). Then, the ratio of the two probability densities 
is 
1 -ly? 
ze 
6 r t e  2 F L  
= e  - [(Y-a)Z-(Y-P)Z]/Z€Z = e- [ Z ( a - P ) Y - a Z + P 2 ] / 2 5 2  
1 
- ( Y - O P  
Now it is easy to extend BlsMC2 to the function BlsMCIS displayed in figure 
4.27. We may check the efficiency gain of importance sampling by running the 
script CheckBlsMCIS of figure 4.28. For a deep out-of-the-money option, we 
compute price with crude Monte Carlo and with importance sampling, and 
we compare the percentage error with respect to the exact price. We reset 
the random variate generator randn twice in order to use exactly the same 
stream of standard normal variates. Running the script, we get 
>> CheckBlsMCIS 
Average Percentage Error: 
MC 
= 3.060% 
MC+IS = 
1.155% 
We should note that this improvement is not to be expected for at-the-money 
options. 
4.6 
QUASI-MONTE CARLO SIMULATION 
In the preceding sections, we have considered the use of variance reduction 
techniques, which are based on the idea that random sampling is really ran- 
dom. However, the random numbers produced by a LCG or by more sophisti- 
cated algorithms are not random at all. Hence, one could take a philosophical 

268 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
function [Price, CI] = BlsMCIS(SO,K,r .T, 
sigma.NRep1) 
nuT = (r - O.5*sigmaA2)*T; 
siT = sigma * sqrt(T) ; 
ISnuT = log(K/SO) - 0.5*sigmaa2*T; 
Veps = randn(NRep1,l) ; 
VY = ISnuT + siT*Veps; 
ISRatios = exp( (2*(nuT - ISnuT)*VY - nuT-2 + ISnuT-2)/2/siT-2); 
DiscPayoff = exp(-r*T)*max(O, 
(SO*exp(VY)-K)); 
[Price, VarPrice, CI] = normfit(DiscPayoff.*ISRatios); 
Fig. 4.27 Importance sampling-based code to price an out-of-the-money vanilla call. 
% CheckBlsMC1S.m 
SO = 50; 
K = 80; 
r = 0.05; 
sigma = 0 . 4 ;  
T = 5/12; 
NRepl = 100000; 
MCError = zeros (NRepl ,1> ; 
MCISError = zeros (NRepl, 1) ; 
TruePrice = blsprice(SO,K,r ,sigma,T) ; 
randn(’state’ ,O); 
for k=1:100 
MCPrice = BlsMC2 (SO, K,r , sigma, T,NRepl) ; 
MCError = abs(MCPrice - TruePrice)/TruePrice; 
end 
randn(’stata’,O); 
for k=l:100 
MCISPrice = BlsMCIS(S0, K,r , sigma, 
T, NRepl) ; 
MCISError = abs(MC1SPrice - TruePrice)/TruePrice; 
end 
fprintf (1, ’Average Percentage Error:\n’); 
fprintf (1, MC 
= %6.3f%%\n’, 100*mean(MCError)); 
fprintf(1,’ MC+IS = %6.3f%%\n’, lOO*mean(MCISError)); 
~ 
~ 
Fig. 4.28 Script to check effectiveness of importance sampling. 

QUASI-MONTE CARL0 SIMULATION 
269 
view and wonder about the very validity of variance reduction methods, and 
even the Monte Carlo approach itself. Taking a more pragmatic view, and 
considering the fact that Monte Carlo methods have proven their value over 
the years, we should conclude that this shows that there are some determinis- 
tic number sequences that work well in generating samples. So one could try 
to devise alternative deterministic sequences of numbers which are in some 
sense evenly distributed. This idea may be made more precise by defining the 
discrepancy of a sequence of numbers. 
Assume that we want to generate a sequence of N "random" vectors 
X1 
, X2,. . . , X N  in the m-dimensional hypercube I" = [0, 11" c W". Now, 
given a sequence of such vectors, if they are well distributed, the number of 
points included in any subset G of I" 
should be roughly proportional to its 
volume vol(G). Given a vector X = (XI, x2,. . . , xm), consider the rectangular 
subset G, defined as 
which has a volume ~ 1 x 2 . .  
. x,. 
If we denote by SN(G) the function counting 
the number of points in the sequence, which are contained in a subset G C I", 
a possible definition of discrepancy is 
D(x~,...,x~)= 
SUP I S N ( G ~ ) - N X ~ X ~ * . . X ~  
1 .  
X E P  
When computing a multidimensional integral on the unit hypercube, it is 
natural to look for low-discrepancy sequences; an alternative name for a low- 
discrepancy sequence is quasirandom sequence, which is why the term quasi- 
Monte Carlo is used. Actually, the quasirandom term is a bit misleading, 
as there is no randomness at all. Some theoretical results suggest that low- 
discrepancy sequences may perform better than pseudorandom sequences ob- 
tained through a LCG or its variations. The point is that from section 4.4 we 
know that the estimation error with Monte Carlo simulation is something like 
O(l/fi), where N is the number of samples. With certain low-discrepancy 
sequences, it can be shown that the error is something like O(ln N)"/N, where 
m is the dimension of the space in which we are integrating. We refer the 
reader to the comprehensive book [12] for a detailed and rigorous account on 
this subject. Different sequences have been proposed in the literature. In the 
following, we illustrate the basic ideas behind two low-discrepancy sequences, 
Halton and Sobol sequences, and their implementation. Low-discrepancy se- 
quences are sequences in the unit interval (0,l); from what we know about 
the generation of generally distributed random variates, we see that this is 
what we need to simulate according to any distribution we need. 
4.6.1 
Generating Halton low-discrepancy sequences 
Halton low-discrepancy sequences are based on a simple recipe: 

270 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
function h=Halton(n,b) 
nO = n; 
h = 0; 
f = l/b; 
while (no > 0) 
nl = floor(nO/b) ; 
r = nO - nl*b; 
h = h+f*r; 
f = f/b; 
nO=nl ; 
end 
Fig. 4.29 MATLAB code to generate the nth element of a Halton sequence with a 
given base. 
Representing an integer number n in a base b, where b is a prime number: 
Reflecting the digits and adding a radix point to obtain a number within 
the unit interval: 
h = (O.dodldzdsd4.. * ) b .  
More formally, if we represent an integer number n as 
m 
n = x d k b k ,  
k=O 
the nth number in the Halton sequence with base b is 
m 
-(k+l) 
h(n, b) = 
dkb 
k=O 
To be precise, what we get is known as Van der Corput sequence. Halton 
sequences are obtained in multiple dimensions when a Van der Corput gen- 
erator is associated to each dimension, making sure different prime numbers 
are used for each base which is associated to each dimension. For the sake of 
simplicity we will only speak of Halton sequences. 
Using the principles illustrated in section 3.1.1 on the binary representation 
of numbers on a computer, it is easy to generate the nth number in a Halton 
sequence with base b. The code is illustrated in figure 4.29. Let us generate 
the first 10 numbers in the sequence with base 2: 
>> seq = zeros(10,l); 

QUASI-MONTE CARL0 SIMULATION 
271 
function Seq = CetHalton(HowMany, Base) 
Seq = zeros(HowMany,l); 
NumBits = l+ceil(log(HowMany)/log(Base)); 
VetBase = Base.-(-(l:NumBits)); 
WorkVet = zeros (1 ,NumBits) ; 
for i=l:HowMany 
increment last bit and carry over if necessary 
j=1; 
ok = 0; 
while ok == 0 
WorkVet (j) = WorkVet (j )+1; 
if WorkVet(j) < Base 
else 
ok = 1; 
WorkVet(j) = 0; 
j = j+l; 
end 
end 
Seq(i) = dot(WorkVet,VetBase); 
end 
Fig. 4.30 MATLAB code to generate a Halton low-discrepancy sequence with a given 
base. 
>> for i=1:10, seq(i) = Halton(i,2);, end 
>> seq 
seq = 
0.5000 
0.2500 
0.7500 
0.1250 
0.6250 
0.3750 
0.8750 
0.0625 
0.5625 
0.3125 
We see how Halton sequences work; by reflecting and adding more bits, we 
fill the space between 0 and 1 with finer and finer intervals. A code to ob- 
tain a whole sequence is illustrated in figure 4.30; the input parameters are 
HowMany, i.e., how long the sequence should be, and the base Base. Rather 
than generating each number in the sequence one at a time, we generate the 
sequence 1,. . . , n by incrementing the bit representation in base b, which is 
immediately converted into H ( n ,  b). 

272 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
" 
0 
8 
0 
0 
0 
0 
0 
o o  
Q 
0 
O
O
 
0 
_I 
0 
1 
1 
0 
0 
0 
0 1  
0.2 
03 
0 4  
0 5  
0 6  
0 7  
08 
0 9  
1 
Fig. 4.31 Random sample in two dimensions. 
I 
" 
0 4  
O 5 I 0  
O 
o o  O 
O 
0 
0 
n ,  
0 
0.1 
0.2 
0.3 
0 
0 
0 
0 0 
0 I 
0.4 
0 
" 0 
0 0 
0 
0 
0 
0 
0 
0 
0 
0 
0 
0 0 
I 
0 5  
0 6  
0 7  
0 
0 
0 
0 
0 
C 
0 
0 0 
0 
0 
0 
0 ,  
0.9 
Fig. 4.32 Covering the bidimensional unit square with Halton sequences. 

QUASI- MONTE CA RLO SIMULATION 
273 
Fig. 4.33 Bad choice of bases in Halton sequences. 
Example 4.15 It is instructive to compare how a pseudorandom sample 
covers the square (0,l) x (0,l) in two dimensions. Using the MATLAB random 
generator, we get the plot of figure 4.31: 
>> plot(rand(100,l) ,rand(100,1), ’0’) 
>> grid on 
To do the same with Halton sequences we must use different bases, which 
should be prime numbers. Let us try with 2 and 7: 
>> plot (GetHalton(100,2) ,GetHalton (100,7), 
’0’ 
>> grid on 
The result is shown in figure 4.32. The judgment is a bit subjective here, but 
it could be argued that the covering of the Halton sequence is more even. On 
the other hand, using a non-prime number as the base, as in 
>> plot(GetHalton(100,2), CetHalton(100,4), ’0’) 
>> grid on 
may result in quite unsatisfactory patterns, such as the one shown in figure 
4.33. 
0 
Example 4.16 Let us explore the use of Halton low-discrepancy sequences 
in a bidimensional integration context. Suppose that we want to compute 
1-1 
1-1 
eCZy (sin 6na: + cos 87ry) da: dy. 
l o  l o  

274 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
Fig. 4.34 Plot of the integrand function in example 4.16. 

QUASI-MONTE CARL0 SIMULATION 
275 
To begin with, let us set up a function in order to plot the integrand and to use 
the dblquad MATLAB function to get an estimate by traditional quadrature 
formulas. 
>> f=@(x,y) exp(-x.*y) .*(sin(6*pi*x)+cos(8*pi*y)); 
>> dblquad(f ,0,1,0,1) 
ans = 
0.0199 
>> [X,Y] = meshgrid(0:O.Ol:l , 0:O.Ol:l); 
>> z = f(X,Y); 
>> surf(X,Y,Z) 
Please note how the function is defined using the dot operator, in order to 
receive vector or matrix arguments and to compute the vector or matrix of 
the corresponding function values. The resulting surface is illustrated in figure 
4.34. It is easy to see that Monte Carlo estimates with 10,000 sampled points 
are not reliable: 
>> rand(’state’,O); 
>> mean(f (rand(1,lOOOO) ,rand( 1,10000) ) ) 
ans = 
0.0276 
>> mean(f (rand(1,10000),rand(l,10000))) 
ans = 
0.0332 
>> mean(f(rand(l,10000~,rand~l,10000~~~ 
ans = 
0.0098 
So, we may try with Halton sequences, changing the bases and keeping the 
same number of samples: 
>> seq2 = GetHalton(10000,2) ; 
>> seq4 = GetHalton(10000,4); 
>> seq5 = GetHalton(10000,5) ; 
>> seq7 = GetHalton(10000,7) ; 
>> mean(f (seq2,seq5)) 
ans = 
0.0200 
>> mean(f (seq2, seq4) 1 
ans = 
0.0224 
>> mean(f (seq2,seq7)) 
ans = 
0.0199 
>> mean(f (seq5,seq7)) 
ans = 
0.0198 

276 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
We see that, provided that we use prime numbers as the bases, the results are 
much more accurate. It is also instructive to compare the results for a small 
number of samples. 
>> rand(’state’,O> 
>> mean(f (rand(1,lOO) ,rand(l, 100)) 
ans = 
-0.0032 
>> mean(f (rand(1,500) ,rand(1,500))) 
ans = 
0.0197 
>> mean(f (rand(1,lOOO) ,rand(l,1000))) 
ans = 
0.0577 
>> mean(f (rand(1,1500) ,rand(1,1500))) 
ans = 
0.0461 
>> mean(f (rand(1.2000) ,rand(1,2000))) 
ans = 
0.0311 
The potential advantage of low-discrepancy sequences is evident even if the 
optimal choice of bases is an issue. 
0 
Example 4.17 As a more practical exercise, we may try pricing the usual 
vanilla European call using a low-discrepancy sequence. We use here the 
simplest sequence, the Halton sequence. To generate normal variates, we 
may either use the Box-Muller method, which we described in section 4.3.4 
or the inverse transform method. We cannot apply polar rejection, because 
when using low discrepancy sequences we must integrate over a space with a 
well-defined dimensionality. We must know exactly how many quasi-random 
numbers we need, whereas with rejection-based methods we cannot anticipate 

QUASI-MONTE CARL0 SIMULATION 
277 
function Price = BlsHaltonBM(SO,K,r,T,sigma,NPoints,Basel,BaseZ) 
nuT = (r - 0.5*sigma^2)*T; 
siT = sigma * sqrt(T) ; 
% Use Box Muller to generate standard normals 
H1 = GetHalton(ceil(NPoints/2) ,Basel) ; 
H2 = GetHalton(ceil(NPoints/2) ,Base21 ; 
VLog = sqrt (-2*log(H1)) ; 
Norml = VLog .* cos(2*pi*H2); 
Norm2 = VLog .* sin(2*pi*H2); 
Norm = [Norml ; Norm21; 
% 
DiscPayoff = exp(-r*T) * max( 0 , SO*exp(nuT+siT*Norm) - K); 
Price = mean(DiscPayoff1; 
Fig. 4.35 Using Halton sequences and Box-Muller algorithm to price a vanilla Euro- 
pean call. 
that. This is an important remark to keep in mind when pricing complex 
options. 
We recall the Box-Muller algorithm here for convenience. To generate two 
independent standard normal variates, we should first generate two indepen- 
dent random numbers Ul and U2, and then set 
x = d a c o s ( 2 7 r u Z )  
Y = J-2 
In U I  sin(27r~2). 
Rather than generating pseudorandom numbers, we may use two Halton se- 
quences with two prime numbers as bases. This is accomplished by the code 
displayed in figure 4.35. 
An alternative approach is based on the inverse transform method. Given 
the potentially weird effects of the Box-Muller transformation, which we have 
illustrated in figure 4.12 on page 238, one could argue that this is a safer 
approach. The code is given in figure 4.36 
Let us check first the use of Halton sequences with Box-Muller transfor- 
mation first: 
>> blsprice(50,52,0.1,5/12,0.4) 
ans = 
5.1911 
>> BlsHaltonBM (50,52,0.1,5/ 12,O. 4,5000,2,7) 
ans = 
>> BlsHaltonBM(50,52,0.1,5/12,0.4,5000,11,7) 
5.1970 
ans = 
5.2173 

278 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
function Price = BlsHaltonINV(SO,K,r,T,sigma,NPoints,Base) 
nuT = (r - O.5*sigmaA2)*T; 
siT = sigma * sqrt (TI ; 
1 Use inverse transform to generate standard normals 
H = GetHalton(NPoints,Base) ; 
Veps = norminv(H); 
1 
Discpayoff = exp(-r*T) *max(O,SO*exp(nuT+siT*Veps)-K) ; 
Price = mean(DiscPayof f) ; 
Fig. 4.36 Using Halton sequences and inverse transform to price a vanilla European 
call. 
>> BlsHaltonBM(50,52,0.1,5/12 ,O .4,5OOO, 2,4) 
ans = 
6.2485 
The first run shows the potential of low-discrepancy sequences; we get a good 
estimate of the option with a limited number of samples. It is instructive to 
see the variability of a Monte Carlo estimate with 5000 samples: 
>> randn(’state’ ,O) 
>> BlsMC2(50,52,0.1,5/12,0.4,5000) 
ans = 
5.2549 
>> BlsMC2 (50,52,0.1,5/12 
,O. 4,5000) 
ans = 
5.1090 
>> BlsMC2(50,52,0. 1,5/12 ,O .4,5000) 
ans = 
5.2777 
From the second run with Halton sequences, we also see that the quality 
of the estimate may depend on the choice of the bases; the third run shows 
that using a non-prime number as a basis yields a very poor result. 
Using the inverse transform, an interesting pattern emerges: 
>> BlsHaltonINV(50,52,0.1,5/12,0.4,1000,2) 
ans = 
5.1094 
>> BlsHaltonINV(50,52,0.1,5/12,0.4,2000,2) 
ans = 
5.1469 
>> BlsHaltonINV(5O,52,0.1,5/12,0.4,5000,2) 
ans = 
5.1688 

QUASI-MONTE CARL0 SIMULATION 
279 
>> B1sHa1ton1NV(50,52,0.1,5/12,0.4,10000,2) 
ans = 
>> B1sHa1ton1NV(50,52,0.1,5/12,0.4,50000,2) 
5.1789 
ans = 
5.1879 
We see that prices look monotonically increasing with respect to the number 
of samples. This is not really the case, as a detailed plot of the price as a 
function of number of samples would show that there are oscillations, yet there 
is a tendency for the price to increase from below. We can try to find a reason 
for this trend: Using Halton sequence with base 2, we fill the unit interval 
with consecutive runs from a low extreme to a high extreme, according to the 
following scheme: 
0.5 
0.25 0.75 
0.125 0.625 0.375 0.875 
0.0625 0.5625 0.3125 0.8125 0.1875 0.6875 0.4375 0.9375 
0.0313 . . .  
Each subsequence is delimited by the new lowest and the new highest point. 
We see that the current maximum found so far increases according to a regular 
pattern; and high values of these numbers correspond to large prices of the 
underlying asset, which are those contributing to the increase of the option 
price. 
If we use 17 as the basis, we see longer monotonically increasing sequences: 
>> GetHalton(l7,17) 
ans = 
0.0588 
0.1176 
0.1765 
0.2353 
0.2941 
0.3529 
0.4118 
0.4706 
0.5294 
0.5882 
0.6471 
0.7059 
0.7647 
0.8235 
0.8824 
0.9412 
0.0035 

280 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
Hence, it is not surprising that if we use a large prime number as the basis, 
the price we get is, in a sense, “more low-biased”: 
>> BlsHaltonINV(50,52,0.1,5/12,0.4,1000,499) 
ans = 
5.1139 
>> BlsHaltonINV(50,52,0.1,5/12,0.4,2000,499) 
ans = 
5.1141 
>> BlsHaltonINV(50,52 ,O. 1,5/12,0.4,5000,499) 
ans = 
5.1148 
>> BlsHaltonINV(50,52 ,O. 1,5/12,0.4,10000,499) 
ans = 
5.1159 
>> BlsHaltonINV(50,52,0.1,5/12,0.4,50000,499~ 
ans = 
5.1252 
Using a large base, even if it is a prime number, has an even more detri- 
mental effect if we use the Box-Muller transformation: 
>> BlsHaltonBM(50,52,0.1,5/12,0.4,5000,59,83) 
ans = 
5.3232 
>> BlsHaltonBM(50,52,0.1,5/12,0.4,5000,101,103) 
ans = 
6.0244 
To understand why using large bases is a bad idea, we may plot the first 1000 
points in the bidimensional sequence when 109 and 113 are used: 
>> plot (GetHalton(1000,109), GetHalton(1000,113), ’ 0  I) 
yields the plot displayed in figure 4.37. The result should be compared 
against figure 4.32. 
Since pricing certain options is a high-dimensional problem, straightfor- 
ward use of Halton sequences is not feasible, as this would require using large 
bases. As an alternative, Faure sequences have been proposed. The basic 
idea in Faure sequences is using only one base, a prime number which must 
be greater than problem dimensionality; coordinates are generated by suitable 
permutations of Van der Corput sequences. This net effect is using a smaller 
base than the largest one used by Halton sequences. Another alternative is 
represented by Sobol sequences, which are discussed in the next section. In 
Sobol sequences only the base 2 is used, which is good. In order to gener- 
ate multidimensional sequences, the Van der Corput sequence with base 2 is 
permuted by a mechanism linked to polynomials in a binary arithmetic. 

QUASI- MONTE CARL0 SIMULATION 
281 
o.6 t 
Fig. 4.37 Poor coverage of the unit square when large bases are used in Halton se- 
quences. 
4.6.2 
Generating Sobol low-discrepancy sequences 
In this section we would like at least to take a look at a more sophisticated 
alternative than Halton sequences, i.e., Sobol sequences. For the sake of 
clarity, it is better to consider the generation of a one-dimensional sequence 
xn. in the [0,1] interval. A Sobol sequence is generated on the basis of a set 
of “direction numbers” w1, w ~ ,  
. . .; we will see shortly how direction numbers 
are selected, but for now just think of them as numbers which are less than 
1. To get the nth number in the sequence, consider the binary representation 
of the integer n: 
n = (. . .b3b~b1)2. 
The result is obtained by computing the bitwise exclusive or of the direction 
numbers wi for which bi # 0: 
zn = blvl CB bzvz CB . . . . 
(4.11) 
If direction numbers are chosen properly, a low-discrepancy sequence will be 
generated [18]. A direction number may be thought as a binary fraction: 
wi = ( 0 . W ~ ~ W ~ ~ W i ~ .  
. .)2, 
or as 
m i  
2a 
wi = -, 
where mi < 2i is an odd integer. To generate direction numbers, we ex- 
ploit primitive polynomials over the field Z2, i.e., polynomials with binary 

282 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
coefficients: 
Irreducible polynomials are those polynomials which cannot be factored; prim- 
itive polynomials are a subset of the irreducible polynomials and are strongly 
linked to the theory of error-correcting codes, which is beyond the scope of 
the book. Some irreducible polynomials over the field ZZ are listed, e.g., in 
[13, chapter 71, to which the reader is referred for further information. Given 
a primitive polynomial of degree d, the procedure for generating direction 
numbers is based on the recurrence formula 
Some numbers ml, . . . , md are needed to initialize the recursion. They may 
be chosen arbitrarily, provided that each mi is odd and mi < 2a. 
Example 4.18 As an example, let us build the set of direction numbers on 
the basis of the primitive polynomial 
+ + 1. 
The recursive scheme runs as follows: 
which may be initialized with ml = 1, m2 = 3, m3 = 7.9 We may carry 
out the necessary computations step by step in MATLAB, using the bitxor 
function. 
gThe reasons why this may be a good choice are given in 131. 

QUASI-MONTE CARL0 SIMULATION 
283 
function [v, m] = GetDirNumbers(p,mO,n) 
degree = length(p)-1; 
p = p(2:degree); 
m = [ mO , zeros(1,n-degree) 1 ;  
for i= (degree+l):n 
m ( i )  = bitxor(m(i-degree), 2-degree * m(i-degree)) ; 
f o r  j=1: (degree-1) 
end 
m(i) = bitxor(m(i), 2-j * p(j) * m(i-j)); 
end 
v=m. / (2. - (1 :length(m) 1) ; 
Fig. 4.38 MATLAB code to generate direction numbers for Sobol sequences. 
Given the integer numbers mi, we may build the direction numbers vi. To 
implement the generation of direction numbers, we may use a function like 
GetDirNumbers, which is given in figure 4.38. The function requires a primi- 
tive polynomial p, a vector of initial numbers m, and the number n of direction 
numbers we want to generate. On exit we obtain the direction numbers v and 
the integer numbers m. 
>> p = [l 0 1 11; 
>> mO = C1 3 71; 
>> [v,m] =CetDirNumbers(p,mO, 6) 
v =  
0.5000 
0.7500 
0.8750 
0.3125 
0.2188 
0.6719 
m =  
1 
3 
7 
5 
7 
43 
The code is not optimized; for instance, the first and last coefficients of the 
polynomial should be 1 by default, and no check is done on the congruence in 
size of the input vectors. 
After computing the direction numbers, we could generate a Sobol sequence 
according to equation (4.11). However, an improved method was proposed by 
Antonov and Saleev [l], who proved that the discrepancy is not changed by 
using the Gray code representation of n. Gray codes are discussed, e.g., in 
(13, chapter 201; all we need to know is the following: 
1. A Gray code is a function mapping an integer i to a corresponding binary 
representation G(i); the function, for a given integer N ,  is one-to-one 
for o 5 i 5 zN - 1. 
0 
2. A Gray code representation for the integer n is obtained from its binary 
representation by computing 
. * .g3gZg1 = (. . .b3bZb1)2 @ (. . .b4b3b2)2. 

284 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
3. The main feature of such a code is that the codes for consecutive num- 
bers n and n + 1 differ only in one position. 
Example 4.19 Computing a Gray code is easily accomplished in MATLAB. 
For instance, we may define an inline function and compute the Gray codes 
for the numbers i = 0, 1, . . . ,15 as follows: 
>> gray = inline(’bitxor(x,bitshift(x,-l))’); 
>> codes = zeros(l6.4); 
>> f o r  i=1:16, codes(i,:)=bitget(gray(i-11, 
[4 3 2 i l l ; ,  end 
>> codes 
codes = 
0
0
0
 0 
0
0
0
 1 
0
0
 1 
1 
0
0
 1 
0 
0 
1 
1 
0 
0 
1 
1 
1 
0 
1 
0 
1 
0 
1 
0 
0 
1 
1 
0 
0 
1 
1 
0 
1 
1 
1 
1 
1 
1 
1 
1 
0 
1 
0 
1 
0 
1 
0 
1 
1 
1 
0
0
 1 
1 
0
0
 0 
We have used the function bitshif t to shift the binary representation of x one 
position to the right and the function bitget to get specific bits of the binary 
representation of a number. We see that indeed the Gray codes for consecutive 
numbers i and i + 1 differ in one position; that position corresponds to the 
rightmost zero bit in the binary representation of i (adding leading zeros if 
necessary). 
0 
Using the feature of Gray codes, we may streamline generation of a Sobol 
sequence. Given xn, we have 
xn+l = xn @vc, 
where c is the index of the rightmost zero bit 6, in the binary representation 
of n. 
Example 4.20 To implement the mechanism in MATLAB, we need a way 
to find the rightmost zero bit in the binary representation of a number. A 
function like the following one will do (provided that at most eight bits are 
used to represent x): 

QUASI- MONTE CA RLO SIMULATION 
285 
function SobSeq = GetSobol(GenNumbers, x0, HowMany) 
Nbits = 20; 
factor = 2-Nbits; 
BitNumbers = GenNumbers * factor; 
SobSeq = zeros(HowMany + 1, 1) ; 
SobSeq(1) = fix(xO*factor) ; 
for i=l : HowMany 
c = min(find( bitget(i-l,1:16) == 0)); 
SobSeq(i+l) = bitxor(SobSeq(i1 , BitNumbers(c)) ; 
end 
SobSeq = SobSeq / factor; 
Fig. 4.39 MATLAB code to generate a Sobol sequence by the Antonov and Saleev 
approach. 
rightbit = inline(’min(find( bitget(x,l:8) == 0))’) 
Now we may put it all together. First, we generate the direction numbers. 
Then we initialize the sequence in some way, e.g., xo = 0, and apply the code 
of figure 4.39. The code is straightforward; the only point is that in theory we 
should compute the exclusive or on bits of a binary fraction; however, b i t x o r  
works on integer numbers only. This is why we shift everything to the left by 
Nbits position, which is accomplished multiplying by f a c t o r  and dividing on 
exit from the function. Also, we truncate the initial number in order to make 
sure that we are “xoring” integer numbers. 
>> p = [1 0 1 11; 
>> mO = C1 3 71; 
>> [v,m] =GetDirNumbers(p,m0,6) ; 
>> GetSobol(v,O.lO) 
0 
0.5000 
0.2500 
0.7500 
0.1250 
0.6250 
0.3750 
0.8750 
0.6875 
0.1875 
0.9375 
ans = 
Using a different set of generating numbers and a different starting point, we 
generate different sequences. 

286 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
>> p = c1 0 1 1  1 1 1 ;  
>> mO = [I 3 5 9 111; 
>> [v,ml =GetDirNumbers (p,m0,8) ; 
>> GetSobol(v,O. 124,IO) 
ans = 
0.1240 
0.6240 
0.3740 
0.8740 
0.4990 
0 
* 9990 
0.2490 
0.7490 
0.1865 
0.6865 
0.4365 
Note that to generate longer sequences, more generating numbers are needed. 
[I 
For further reading 
In the literature 
For a general introduction to simulation, see [9] or [15], both of which 
have heavily influenced the presentation in this chapter; [14] is another 
classical reference. 
For a more theoretical treatment of Monte Carlo simulation and random 
number generation, see [4]. The random number generators used in 
MATLAB are described in [ 111. 
Low-discrepancy sequences are treated in [12], which is at a quite ad- 
vanced level. 
An excellent and very readable introduction to Monte Carlo and quasi- 
Monte Carlo methods in finance is [5]. See also [7] for a discussion on 
selecting primitive polynomials for Sobol sequences. A table of primitive 
polynomials is also given in [ 131. 
See [8] for an early account on the use of low-discrepancy sequences 
within financial engineering. 
On the Web 
0 For a list of resources on Monte Carlo and quasi-Monte Carlo simulation, 
see http : //www .mcqmc . org. 

REFERENCES 
287 
See also http://www.mat.sbg.ac.at/"schmidw/links.html. 
REFERENCES 
1. I.A. Antonov and V.M. Saleev. An Economic Method of Computing LPT 
Sequences. USSR Computational Mathematics and Mathematical Physics, 
19:252-256, 1979. 
2. I. Beichl and F. Sullivan. The Importance of Importance Sampling. Com- 
puting in Science and Engineering, 1 :71-73, March-April 1999. 
3. P. Bratley and B.L. Fox. Algorithm 659: Implementing Sobol's Quasiran- 
dom Sequence Generator. A CM Transactions on Mathematical Software, 
14:88-100, 1988. 
4. G.S. Fishman. Monte Carlo: Concepts, Algorithms, and Applications. 
Springer-Verlag, Berlin, 1996. 
5. P. Glasserman. Monte Carlo Methods in Financial Engineering. Springer- 
Verlag, New York, NY, 2004. 
6. J.C. Hull. Options, Futures, and Other Derivatives (5th ed.). Prentice 
Hall, Upper Saddle River, NJ, 2003. 
7. P. Jaeckel. Monte Carlo Methods in Finance. Wiley, Chichester, 2002. 
8. C. Joy, P.P. Boyle, and K.S. Tan. Quasi-Monte Carlo Methods in Numer- 
ical Finance. Management Science, 42:926-938, 1996. 
9. A.M. Law and W.D. Kelton. Simulation Modeling and Analysis (3rd ed.). 
McGraw-Hill, New York, 1999. 
10. M.J. Miranda and P.L. Fackler. Applied Computational Economics and 
Finance. MIT Press, Cambridge, MA, 2002. 
11. C. Moler. Random Thoughts. Matlab News 6 
Notes, pages 2-3, Fall 
1995. This paper may be downloaded from The Mathworks' Web site at 
http://www.mathworks.com/company/newsletter/pdf/Cleve.pdf. 
12. H. Niederreiter. 
Random Number Generation and Quasi-Monte Carlo 
Methods. Society for Industrial and Applied Mathematics, Philadelphia, 
PA. 1992. 
13. W.H. Press, S.A. Teukolsky, W.T. Vetterling, and B.P. Flannery. Nu- 
merical Recipes in C (2nd ed.). Cambridge University Press, Cambridge, 
1992. 

288 
NUMERICAL INTEGRATION: DETERMINISTIC AND MONTE CARL0 METHODS 
14. B.D. Ripley. Stochastic Simulation. Wiley, New York, 1987. 
15. S. Ross. Simulation. Academic Press, San Diego, CA, 1997. 
16. S. Ross. Introduction to Probability Models (8th ed.). Academic Press, 
San Diego, CA, 2002. 
17. R.Y. Rubinstein. Simulation and the Monte Carlo Method. Wiley, Chi- 
Chester, 1981. 
18. I.M. Sobol. On the Distribution of Points in a Cube and the Approx- 
USSR Computational Mathematics and 
imate Evaluation of Integrals. 
Mathematical Physics, 7:86-112, 1967. 

Finite Difference 
Methods for Partial 
Differentia[ Equations 
Partial differential equations (PDEs) play a major role in financial engineer- 
ing. Since the seminal work leading to the Black-Scholes equation, which 
we introduced in section 2.6.2, PDEs have become an important tool in op- 
tion valuation. It turns out that PDEs provide a powerful and consistent 
framework for pricing rather complex derivatives. Unfortunately, as analyti- 
cal solutions like the Black and Scholes formula are not available in general, 
one must often resort to numerical methods. 
The numerical solution of PDEs is a common tool in mathematical physics 
and engineering, and quite sophisticated methods have been developed. The 
complexity of the methods also depends on the specific type of PDE at hand. 
As expected, non-linear equations are generally more difficult than linear 
ones, but there is also a subtler dependence on numerical parameters, since 
a change in the value of a coefficient may drastically change the character- 
istics of an equation. In the financial engineering case, it happens that in 
many cases rather simple methods are enough to obtain a reasonably accu- 
rate solution. Indeed, we deal here only with relatively straightforward finite 
difference methods, which are based on the natural idea of approximating par- 
tial derivatives with difference quotients. Even so, the topic is not as trivial 
as one may think, since careless use of finite difference schemes may lead to 
unreasonable results. In fact, while some authors suggest the use of PDEs 
as the single most useful tool in derivatives pricing [9, p. 6151, others suggest 
that they are quite vulnerable to numerical difficulties and, while acknowledg- 
ing the role of finite difference methods, they suggest the use of lattice-based 
methods whenever possible (see, e.g., [2, p. 3651). Actually, this is a bit a 
289 

290 
FlNlTf DlFFERENCE METHODS FOR PARTlAL DlFfERENTlAL EQUATlONS 
matter of taste, and when confident with a method, one is able to squeeze 
the most out of it. Fortunately, when numerical difficulties occur in solving 
a PDE for a financial problem, often the answers we get from the algorithm 
are so blatantly senseless that we may easily spot the trouble; in other cases, 
however, unreliable answers may have nasty effects. In this chapter we also 
introduce concepts related to convergence, consistency, and stability in or- 
der to understand the basic issues connected with the numerical solution of 
PDEs. It should be stressed that PDEs are actually a difficult topic requiring 
advanced mathematical concepts for a rigorous treatment, and as usual we 
will rely mostly on relatively informal arguments and intuition. 
We first classify PDEs in section 5.1. Then in section 5.2 we introduce dif- 
ferent ways to approximate partial derivatives by finite differences, leading to 
different solution schemes which may turn out numerically stable or unstable. 
We devote a particular attention to the heat equation, which is the subject of 
section 5.3, since the Black-Scholes PDE is strongly linked to diffusion pro- 
cesses. We generalize to multiple spatial dimensions in section 5.4, where we 
consider the heat equation in two dimensions; the Alternating Direction Im- 
plicit approach is described. Finally, in section 5.5 we briefly point out a few 
theoretical concepts concerning the convergence of finite difference methods. 
5.1 
INTRODUCTION AND CLASSIFICATION OF PDEs 
We introduced the Black-Scholes PDE in section 2.6.2 to find the theoretical 
price f (S, t) of a derivative security depending on the price S of one underlying 
asset at time t. Using a stochastic differential equation to model the dynamics 
of the underlying asset price and using no arbitrage arguments, we have found 
that f must satisfy the PDE 
af 
1 2 2d2f 
af 
-+--0 
s - + r S - - r f  
=o, 
at 
2 
as2 
as 
where T is the risk-free interest rate and -0 is the asset price volatility. Suitable 
boundary conditions must be added to find a specific solution corresponding 
to the option type we are considering. This equation has various features: 
0 It is second-order. 
0 It is linear. 
0 It is a parabolic equation. 
All these features refer to how PDEs are classified; such a classification is 
relevant in that the choice of a numerical method to cope with a PDE generally 
depends on its characteristics. 
In order to classify PDEs, let us abstract from the financial interpretation 
of the variables involved and refer to an unknown function qi(x, y), depending 

INTRODUCTION AND CLASSIFICATION OF PDEs 
291 
on variables x and y; for simplicity we deal with a function of two independent 
variables only, but the classification scheme may be applied in a more general 
setting. The order of a PDE is the highest order of the derivatives involved. 
For instance, a generic first-order equation has the form 
where a, b, c, dare given functions of the independent variables. This equation 
is first-order since only first-order derivatives are involved. Furthermore, it 
is linear, since the functions a, b, c, and d depend only on the independent 
variables x and y and not on 4 itself. By the same token, the generic form of 
a linear second-order equation is 
a24 
a24 
a24 
a4 
a4 
ax2 
axay 
ay2 
ax 
ay 
a- 
+ b- 
+ c- 
+ d- + e- + f4 + g  = 0, 
where again all the given functions, from a to g, depend only on x and y. An 
example of a first-order non-linear equation is 
2 
(g)2+(g) 
= l .  
An example of a second-order non-linear equation is 
Equation (5.3) is non-linear but in a different way than (5.2). In this equation, 
the coefficient a of the highest-order derivative depends only on the first- 
order derivative. We have a quasilinear equation whenever the highest-order 
derivatives occur linearly, with coefficients depending only on the independent 
variables, the unknown function 4, and its lower-order derivatives. For the 
sake of simplicity, in this introductory book we deal only with linear equations. 
It should be noted that while most of the models you will see in finance 
are linear, non-linear equations may be obtained when relaxing some of the 
assumptions behind the Black-Scholes model; for an example of a non-linear 
equation that arises when introducing transaction costs, see [9, chapter 211. 
It is customary to classify quasilinear second-order equations depending on 
the sign of the expression 6' - 4ac: 
If b2 - 4ac > 0, the equation is hyperbolic. 
If b2 - 4ac = 0, the equation is parabolic. 
If 6' - 4ac < 0, the equation is elliptic. 
It is easy to see that the discriminant term b2 - 4ac is formally similar to 
the analogous term we have in second-degree algebraic equations. Elliptic 

292 
FlNlTE DlFFERENCE METHODS FOR PARTlAL DlFFERENTlAL EQUATlONS 
equations may arise in equilibrium models (where time is not involved). A 
typical example is the Laplace equation 
Here we have a = c = 1 and b = 0, so that b2 - 4ac = -4 < 0. The wave 
equation 
a24 
2a24 
-- p - - 0 ,  
8t2 
8x2 
where t is time, is a typical example of a hyperbolic equation, since the dis- 
criminant term is 4p2 > 0. The prototype parabolic equation is the heat (or 
diffusion) equation: 
_ -  
84 
a24 
- k-, 
at 
8x2 
where t is time and 4 is the temperature of a point with coordinate x on a 
line. In this case, b2 - 4ac = 0. By a change of variables, the equation may 
be cast into a dimensionless form: 
Now consider the Black-Scholes equation; again b = c = 0, so the equation 
is parabolic. This does not happen by chance, since with a transformation 
of coordinates it can be shown that the Black-Scholes equation actually boils 
down to the heat equation. 
An equation like (5.4) must be integrated with suitable conditions in order 
to pinpoint a meaningful solution. For instance, assume that $(x, t )  is the 
“temperature” at point x E [0,1] of a rod of length 1 at time t; the end points 
are kept at a constant temperature UO, and the initial temperature of the rod 
is given over all of its length. Then we must add the initial condition 
and the boundary conditions 
Here the domain is bounded with respect to space and unbounded with re- 
spect to time. In financial problems, the initial condition is usually replaced 
by a terminal condition, as the option payoff is known at expiration; therefore, 
the time domain is bounded, whereas the domain with respect to the price of 
the underlying asset may be (in principle) unbounded. From a computational 
point of view, the domain must be limited in some sensible way. Boundary 
conditions are easy to spot for vanilla European options. With exotic op- 
tions, enforcing boundary conditions may be more complicated, e.g., when 

NUMERICAL SOLUTION BY FlNlTE DIFFERENCE METHODS 
293 
the boundary conditions must themselves be approximated by some numeri- 
cal scheme. In other cases, such as barrier options, the boundary conditions 
may actually result in a simplification of the problem. American options raise 
another issue; for each time before expiration, there is a critical value for the 
price of the underlying asset at which it is optimal to exercise the option (see 
figure 2.22 on page 118); depending on the option type (call or put), it will 
also be optimal to exercise the option for prices above and below the critical 
price.' So with American options we should cope with a free boundary, i.e., 
a boundary within the domain, which separates the exercise and no-exercise 
region. We deal with these issues in chapter 9. 
A noteworthy feature of the heat equation is that any discontinuity in the 
initial conditions is somehow smoothed out, so that the solution for t > 0 is 
differentiable everywhere. On the contrary, in the wave equation, the irreg- 
ularities are propagated along lines called characteristics.2 Another feature 
of parabolic equations is that they are relatively easy to work with from the 
numerical point of view. 
A final remark is that the form of the equation and the boundary conditions 
determine if a given problem involving a PDE is well-posed. A problem is well- 
posed if: 
0 There exists a solution. 
0 The solution is unique (at least within a certain class of functions of 
interest). 
The solution depends in a nice way on the problem data (i.e., a small 
perturbation in the problem data results in a small perturbation of the 
solution). 
We will trust our intuition that the equations we write make sense and will 
assume implicitly that all our problems are well-posed. 
5.2 NUMERICAL SOLUTION BY FINITE DIFFERENCE METHODS 
Finite difference methods to solve PDEs are based on the simple idea of ap- 
proximating each partial derivative by a difference quotient. This transforms 
the functional equation into a set of algebraic equations. As in many nu- 
merical algorithms, the starting point is a finite series approximation. Under 
suitable continuity and differentiability hypotheses, Taylor's theorem states 
'Recall that a vanilla American call should be never exercised unless the stock pays divi- 
dends. 
21n hyperbolic equations, two characteristic lines exist, and this is actually linked to the 
fact that the discriminant b2 - 4ac is positive, a property that is linked to the existence of 
two roots in algebraic second-order equations. 

294 
FINITE DIFFERENCE METHODS FOR PARTIAL DIFFERENTIAL EQUATIONS 
Fig. 5.1 
a derivative. 
Graphical illustration of forward, backward, and central approximations of 
that a function f(x) may be represented as 
If we neglect the terms of order h2 and higher, we get 
(5.6) 
f(. + h) - f(x) + O(h). 
h 
fW = 
This is the forward approximation for the derivative; indeed, the derivative is 
just defined as a limit of the difference quotient above as h -+ 0. There are 
alternative ways to approximate first-order derivatives. By similar reasoning, 
we may write 
from which we obtain the backward approximation, 
In both cases we get a truncation error of order O(h). A better approxima- 
tion can be obtained by subtracting equation (5.7) from equation (5.5) and 
rearranging: 
+ O(h2). 
f(x + h) - f(x - h) 
2h 
fW = 
(5.9) 
This is the centrul or symmetric approximation, and for small h it is a better 
approximation, since the truncation error is O(h2). Why this is the case 
may also be seen from figure 5.1. However, this does not imply that forward 
and backward approximations must be disregarded; they may be useful to 

NUMERICAL SOLUTION BY F/N/T€ DFFERENCE METHODS 
295 
come up with efficient numerical schemes, depending on the type of boundary 
conditions. 
The reasoning may be extended to higher-order derivatives. To cope with 
the Black-Scholes equation, we must approximate second-order derivatives, 
too. This is obtained by adding equations (5.5) and (5.7), which yields 
and rearranging yields 
(5.10) 
In order to apply the ideas above to a PDE involving a function 4(s, 
y), it 
is natural to set up a discrete grid of points of the form (i 62, 
j 6y), where 6s 
and 6y are discretization steps, and to look for the values of 4 on this grid. It 
is customary to use the grid notation: 
42j = 4(i 62, j 6y). 
Depending on the type of equation and on how the derivatives are approx- 
imated, we obtain a set of algebraic equations which may be more or less 
easily solved. A possible difficulty is represented by boundary conditions. If 
the equation is defined over a rectangular domain in the ( 2 ,  y) space, it is easy 
to set up a grid such that the boundary points are on the grid. Other cases 
might not be so easy, and a sensible way to approximate the boundary condi- 
tions must be devised. Nevertheless, we would expect that for 6x, 6y + 0 the 
solution of this set of equations converges (in some sense) to the solution of 
the PDE. Actually, this is not granted at all, as different complications may 
arise. 
5.2.1 
Consider the following example of a first-order linear e q ~ a t i o n : ~  
Bad example of a finite difference scheme 
a4 
84 
- + c - - 0 ,  
at 
ax 
where 4 = $(s, t), c > 0, and the initial condition 
4(2,0) = f(.) 
vs 
is given. It is easy to verify that the solution is of the form 
4(& t) = f(. - 4; 
(5.11) 
3The example is taken from [I, chapter 21. 

296 
F/N/T€ D/Ff€R€NC€ METHODS FOR PARTlAL D/FF€R€NT/AL €QUAT/ONS 
ij+l 
P 
. .  
'J 
i+l j 
Fig. 5.2 Rqmsenting a finite difference scheme by a computational diagram. 
in other words, the solution is simply a translation of f(x) with velocity of 
propagation c. In fact, this type of equation is called the transport equation. 
A real transport equation typically involves a function C ( X )  rather than a 
constant velocity c. We take for granted that the problem is well-posed, 
and we do not check the uniqueness of the solution (see [l, pp. 21-25] for 
a thorough discussion). Now let us ignore what we know about the solution 
and try a finite difference scheme based on forward approximations. Equation 
(5.11) may be approximated by 
which, neglecting the truncation error and using the grid notation x = i6xl 
t = j St, yields 
(5.12) 
4. . 
- 4 . .  
1.3 + 4i+l,j - 4ij 
t,j+i 
= 0, 
6t 
62 
4 i o  = f(ibx) = fi 
with the initial condition 
Vi. 
In practice, in order to solve the problem on a computer, we should restrict 
the domain in some way, enforcing some limits on i and j .  For now, we simply 
awime that we are interested in the solution for t > 0, thus j = 1,2,3,. . .. 
Now; how can we solve equation (5.12) in a systematic way? If we consider 
equation (5.12) for j = 0, we see that values q5i+l,o and qbio are involved, 
and they are known from the initial conditions; the only unknown value is 
which may be obtained as an explicit function of known values. In fact, 
solving for the unknown value, we get 
(5.13) 
where p = 6x/6t. This computational scheme can be represented by the 
computational diagram depicted in figure 5.2, and it is easy to understand 
and implement. Unfortunately, it need not converge to the solution of the 
ecpat,ion. Consider the following initial condition: 
2 < -1, 
(5.14) 

NUMERlCAL SOLUT/ON BY f/N/TE DFFERENCE METHODS 
297 
which implies 
4 i O  = f(i6x) = 1 
vi 2 0. 
Now, using the computational scheme (5.13), for j = 0 we have 
Repeating this argument for any time instant (j = 2 , 3 , .  . .), it is easily seen 
that, however small we take the discretization steps, 
4 i j  = 1, 
i,j 2 0, 
which is certainly not the correct solution. Some readers might wonder if 
this is due to some irregularity in the initial values. In fact, the derivative 
of f(z) is discontinuous at certain points, but it is easy to see that using a 
smoothed version of this function would not change the issue. This example 
also shows that non-differentiable functions may look like acceptable solutions 
of a PDE, which is a bit odd since derivatives are not defined everywhere for 
such functions; a rigorous investigation of this question leads to the concept 
of weak solution of a PDE [l]. 
5.2.2 
The example illustrated in the previous section shows that a numerically rea- 
sonable scheme, with a truncation error that tends to zero as discretization 
steps get smaller and smaller, may fail to converge. From a mathematical 
point of view, there is a non trivial interplay between concepts such as con- 
sistency, stability, and convergence. A full investigation calls for a deep treat- 
ment, and we will just briefly outline the concepts in section 5.5. From a more 
intuitive point of view, the reason for the failure of the previous finite differ- 
ence scheme is that it does not reflect the physical propagation process, where 
the initial condition is translated “to the right” with respect to space. Hence, 
we could try and fix the problem by adopting the computational scheme rep- 
resented in figure 5.3, which is obtained by using a backward difference for 
the partial derivative with respect to x. This yields 
Instability in a finite difference scheme 
4 . . - 4 . .  
+..-+. 
6t 
6X 
= 0, 
(5.15) 
w+1 
$3 + 
v 
% - I d  
and solving for $i,j+l, we get the scheme 
(5.16) 
Note that here 4i,j+1 still depends on the data at the previous time instant 
but “to the left” with respect to space. Let us try this scheme with MATLAB. 

298 
FINITE DIFFERENCE METHODS FOR PARTIAL DIFFERENTIAL EQUATIONS 
P 
i+lj+l 
i j 
i+lj 
Fig. 5.3 Cornputational diagrarn of the niodified scheme for the transport equation. 
% f0transp.m 
function y=f Otransp (x) 
i f  (x < -1) 
y=o ; 
elseif (x <= 0) 
y=x+l ; 
else 
y=l ; 
end 
Fig. 5.4 Finiction to evaluate the initial values for the transport equation. 
Example 5.1 In order to apply the computational scheme (5.16) with ini- 
tial condition (5.14), we have to write a few M-files. In figure 5.4 we show 
code to evaluate the initial value at a given point 2 at t = 0. In figure 5.5 we 
see the MATLAB code for solving the equation. Note that we must truncate 
thc domain between minimum and maximum x values, and with respect to 
time as well. We use a fixed value for the leftmost value in space, assuming 
that for smaller values of x the initial value is constant. Finally, the function 
TransportPlot illustrated in figure 5.6 is used to plot the numerical solu- 
tion at different times: Four time subscripts are passed as an argument and 
the corresponding four plots are obtained. To begin with, we may solve the 
equation on the domain -2 5 x 5 3, 0 5 t 5 2, with discretization steps 
6x = 0.05, 6t = 0.01: 
>> xmin = -2; 
>> xmax = 3; 
>> dx = 0.05; 
>> tmax = 2; 
>> d t  = 0.01; 
>> c = 1; 
>> sol = transport(xmin, dx, xmax. d t ,  tmax. c ,  'fotransp'); 
>> TransportPlot(xmin, dx, xmax, [l 51 101 2011, sol) 
We should note that, since array indexing in MATLAB starts from 1, the 
solution for t = 2 is in column 201 in the array. The solution, plotted in 

NUMERlCAL SOLUTION BY F/N/TE DIFFERENCE METHODS 
299 
% transport .m 
function [solution, N, M] = transport(xmin, dx, xmax, dt, tmax, c, fO) 
N = ceil( (xmax - xmin) / dx) ; 
xmax = xmin + N*dx; 
M = ceil(tmax/dt); 
k2 = dt*c/dx; 
solution = zeros(N+l,M+l); 
vetx = xmin:dx:xmax; 
for i=l:N+l 
end 
f ixedvalue = solution(1,l) ; 
% this is needed because of finite domain 
for j=l:M 
end 
kl = 1 - dt*c/dx; 
solution(i,l) = feval(fO,vetx(i)); 
solution(:, j+l) = kl*solution(: ,j)+k2*[ 
xedvalue ; solution(l:N, 11 ; 
Fig. 5.5 Code implementing the finite difference scheme for the transport equation. 
% TransportP1ot.m 
function TransportPlot (xmin, dx, xmax, times, sol) 
subplot (2,2,1) 
plot (xmin:dx: xmax, sol ( : ,times (1) ) 1 
axis([xmin xmax -0.1 1.11) 
subplot (2,2,2) 
plot(xmin:dx:xmax, sol(:,times(2)) 
axis([xmin xmax -0.1 1.13) 
subplot (2,2,3) 
plot(xmin:dx:xmax, sol(:,times(3)) 
axis([xmin xmax -0.1 1.13) 
subplot (2,2,4) 
plot(xmin:dx:xmax, sol(:,times(4))) 
axis ( Cxmin xmax -0.1 1.11 ) 
Fig. 5.6 Function for plotting the numerical solution of the transport equation. 

300 
FINITE DIFFERENCE METHODS FOR PARTIAL DIFFERENTIAL EQUATIONS 
0.4 
0.2 
0.4 
0.2 trl 
- 2 - 1  
0 
0 
1
2
 3 
- 2 - 1  
0 
1
2
 3 
- 2 - 1  
0 
1
2
 3 
0.4 
0.2 rm 
0 
- 2 - 1  
0 
1
2
 3 
0.4 
0.2 
- 2 - 1  
0 
1
2
 3 
fig. 5.7 Numerical solution of the transport equation for 6x = 0.05, 6t = 0.01; t = 0, 
t = 0.5, t = 1, and t = 2. 
figure 5.7, gets progressively translated as we would expect, but it also looks 
progressively “smoothed.” This could be due to a coarse discretization along 
the x axis. So we may try with Sx = 0.01: 
>> dx = 0.01; 
>> s o l  = transport(xmin, dx, xmax. d t ,  tmax, c ,  ’fotransp’); 
>> TransportPlot(xmin, dx, xmax, [l 51 101 2011, sol) 
The solution is depicted in figure 5.8, and it looks much better. So, why don’t 
we try a finer discretization, say Sx = 0.005? 
>> dx = 0.005; 
>> sol = transport(xmin, dx, xmax, d t ,  tmax, c ,  ’fotransp’); 
>> TransportPlot (xmin, dx, xmax, [l 6 7 81, s o l )  
The solution we see in figure 5.9 is not really satisfactory. Something is 
definitely going wrong. 
0 
As we may see, for certain settings of the discretization steps, the finite 
difference method is subject to numerical instability. By looking at equation 
(5.16), we may see that what we are doing is similar to a convex combination 
(i.e., an average) of two values; indeed, it will be a convex combination, pro- 
vided that c l p  > 0, which is the case as we assumed that c > 0, and c l p  5 1, 
i.e., 
cSt 5 62. 
(5.17) 

NUMERICAL SOLUTION BY FINITE DIFFERENCE METHODS 
301 
0.4 
0.2 
0 4  
02 IL 
0 
- 2 - 1  
0 
1
2
 3 
Fig. 5.8 
t = 0.5, t = 1, and t = 2. 
Numerical solution of the transport equation for 6x = 0.01, d t  = 0.01; t = 0, 
-2 
-1 
0 
1 
2 
~~ 
-2 
-1 
0 
1 
2 
3 
-
2
-
1
 
0 
1
2
 3 
Fig. 5.9 
t = 0, t = 0.05, t = 0.06, and t = 0.07. 
Numerical solution of the transport equation for 6x = 0.005, bt = 0.01; 

302 
FINITE DIFFERENCE METHODS FOR PARTIAL DIFFERENTIAL EQUATIONS 
Fig. 5.10 Pliysid interpretation of the stability coiiditiori (5.17) 
If thib condition is not met, we have a negative coefficient in the linear combi- 
iiation (5.16); hut if the initial data are positive, we would not expect negative 
(pant i t ies . 
It is also possible to give a more physical interpretation of the stability 
condition (5.17) in terms of a domain of influence. Consider figure 5.10. Due 
to the structure of the niiinerical scheme (5.16), the value a7+l,l depends on 
the values 410 and q!1~+1,0. The exact solution of the transport equation is 
such that the initial value at point i6x should influence only the values on 
the characteristic" represented as a dotted line in figure 5.10. The slope of 
the characteristic line is l/c; the slope of the line joining the points (i 6z, 0) 
and ((i + 1)6z,St) is clearly 6t/6x. In the figure this second line has a larger 
slope than the first one and the stability condition (5.17) is violated, since 
6t 
1 
62 
c 
- > -  
Froiii a physical point of view this makes no sense, since in this case the 
numerical sclienie is such that the initial value at point i 62 is influencing the 
value at a point nbo~ue the characteristic line. In other words, the "speed" of 
the numerical scheme, 6x/6t, should not be smaller than the transport speed 
c to ensure stability. 
All of these considerations are nothing more than intuitive arguments. The 
instability problem may be analyzed rigorously in different ways. One ap- 
pronch, known as Von Neumann stability analysis, is related to Fourier analy- 
sis and is illustrated in the next example. Another approach, based on matrix 
theoretic arguments, will be illustrated in section 5.3, where we consider the 
heat equation. It should also he noted that in some cases a financial interpre- 
tation of instability niay be given (see section 9.2.1). 
*The characteristic is also a curve on which singularities in the solution may propagate. 

EXPLICIT AND IMPLICIT METHODS FOR THE HEAT EQUATION 
303 
Example 5.2 Consider again the transport equation, but with different ini- 
tial values: 
(3 
4(x1 0) = f(x) = E cos 
Since we know that the exact solution is $(x, t )  = f(x - ct), we see that the 
solution will be bounded everywhere, just like the initial values. Note also 
that after discretization we have a peculiar set of initial values on the grid: 
Going forward one layer of nodes in time, applying the scheme (5.16) yields 
C 
4 3 
P 
4 2 , l  = (1 - ;) 
E ( - l ) %  + - E ( - 1 ) 2 - 1  
- 1 - - E ( - l ) %  - - E ( - 1 ) 2  
C 
P 
= 
E (-l)i (1 - 2;) . 
By the same token, 
( 3 
$h2,2 = (1 - ;) 
E (-1)i (1 - 2;) + p'(-l)i-l 
1 - 2- 
C 
2 
= 
E ( - l ) i  
(1 - 2
3
 , 
and in general we get 
j 
4ij = E ( - l ) i  
(1 - 2;) 
. 
We see that the if the stability condition (5.17) is violated, i.e., if c/p > 1, we 
have 
/ l - p l > l  
2c 
and the initial data are amplified by a factor that goes to infinity for increasing 
values of j. 
0 
5.3 
EXPLICIT AND IMPLICIT METHODS FOR THE HEAT 
E Q U AT1 0 N 
Let us consider the heat equation in dimensionless form: 
84 - a24 
at 
ax2' 
- -  
- 

304 
NNlTE DlFFERENCE METHODS FOR PARTlAL DlFFERENTlAL EQUATlONS 
x-6x 
X 
x+6x 
x-6x 
X 
x+Fx 
With some work, the Black-Scholes equation can be transformed into this 
form, so it is worthwhile to investigate this equation in some detail. We also 
lime that, the domain of interest is x E (0,l) and t E (0, m); actually, in a 
practical scheme, we will also limit the domain with respect to time, t E (0; 7'). 
We have inibial conditions for t = 0 and boundary conditions at x = 0 and 
x = 1 for any t > 0. We discretize with respect to x with a step 62, such that 
N6:c = 1, and with respect to t with a step dt, such that M d t  = T .  Note 
that this results in a grid with ( N  + 1) x ( M  + 1) points. 
Before proceeding with the treatment of standard methods for the heat 
equation: it may he useful to get an intuitive feeling for the physical sense 
of this equation. To this aim, let us consider figure 5.11. The figure on the 
left shows a temperature profile which is (at least) locally convex at point 2. 
In taliis case, heat should diffuse from the warmer points x - 6x and .2: + 6z 
towards the center, arid temperature in x should rise. In fact, the second-order 
tlerivative with respect to time is positive and the derivative with respect to 
time is positive as well. Ift,lic temperature profile is locally concave, in which 
case t,he second-order derivative is negative, heat should diffuse from the centjer 
to the left and to the right; temperature at point x should decrease, and its 
derivative with respect to time is negative. 
In general, when we have a term like a24/6x2 in a PDE, it is called a 
diflusion term. In cquation (5.11) we have seen that a term D#/Dx may he 
linked to transportation, or convection, phenomena. Indeed, an equation like 
(5.18) 
is called a convection-diflusion equation. 
5.3.1 
A first possibility for coping with this equation is to approximate the derivatiw 
with respect. to time by a forward approximation, and the second derivative 
Solving the heat equation by an explicit method 

EXPLICIT AND IMPLICIT METHODS FOR THE HEAT EQUATION 
305 
ij+l 
9 
i -l j  
i j 
i+lj 
Fig. 5.12 Coinputai ional diagrani of the explicit method for the heat equation. 
by the appioxiniation (5.10). This yields 
4L.J+1 - 4 , 3  - 
- 41+l.J - 248, + L 1 , J  
St 
(62)2 
that we rnay rearrange this equation by solving for the un- 
known value 4, ,) + I : 
4,.J+1 = P4L-1,) + (1 - 2/J)4,, + /)42+1,3’ 
(5.19) 
where p = bt/(6x)’. 
Starting from the initial conditions ( j  = O), we may solve the equation for 
increasing valiics of 3 = 1,. . . , AT. Note that for each 3, i e., for each layer in 
time, we rnust use equation (5.19) to firid out N -  1 values for 1 = 1, . . . , N - 1. 
as the reniaining two are given by the boundary conditions. Since the unknown 
values are giveii by an explicit expression, this approach is called explzczt. It 
can he represented by the computational diagram in figure 5.12. 
Example 5.3 Consider the following initial data: 
0 5 x 5 0.5 
0.5 5 x 5 1, 
{ 
-z), 
$(:c, 0) = f(x) = 
and Imuntlary conclitioiis 
4(0, t )  = qql, t )  = 0 
vt. 
The MATLAB code for solving the heat equation for this initial condition is 
shown in figure 5.13. Note that we store the results in a matrix; we could also 
store only two consecutive layers of points in time, but keeping the whole set 
of resiilts makes plotting the solution easier. Let us solve the equation with 
6X 
>> 
>> 
>> 
>> 
>> 
= 0.1 ant1 bt = 0.001, and plot the result for t = 0, 10St, 506t, 100St. 
dx = 0.1; 
dt = 0.001; 
tmax = dt*100; 
sol=HeatExpl(dx, dt , tmax) ; 
subplot (2,2,1) ; 

306 
FINITE DFFERENCE METHODS FOR PARTIAL DIFFERENTIAL EQUATIONS 
1 
0.8. 
0.6. 
0.4 
% HeatExp1.m 
function sol = HeatExpl(deltax, deltat, tmax) 
N = round(l/deltax); 
M = round(tmax/deltat) ; 
sol = zeros(N+l,M+l) ; 
rho = deltat / (deltaxl-2; 
rho2 = 1-2*rho; 
vetx = 0:deltax:l; 
for i=2: ceil ((N+1) /2) 
sol(i,l) = 2*vetx(i); 
sol(N+2-i,l) = sol(i,l); 
end 
for j=l:M 
for i=2:N 
sol(i,j+l) = rho*sol(i-l,j) + . . . 
rho2*sol(i,j) + rho*sol(i+l,j); 
end 
end 
’ 
Fig. 5.13 MATLAB code for solving the heat equation by the explicit method. 
0.6 o . : r l  
0.2 0.4D
0 
0 
0.2 
0.4 
0.6 
0.8 
1 
Fig. 5.14 Numerical solution of the heat equation with 6x = 0.1 and 6t = 0.001, by 
the explicit method, for t = 0, t = 0.01, t = 0.05, t = 0.1. 

EXPLlClT AND IMPLICIT METHODS FOR THE HEAT EQUATION 
307 
>> plot (0: 
dx: 1, sol ( : ,1)) 
>> axis(E0 1 0  11) 
>> subplot(2,2,2); 
>> plot (0:dx: 1 ,sol( : ,11)) 
>> axis( [O 1 0 11 1 
>> subplot(2,2,3); 
>> plot(O:dx:l,sol(:,51)) 
>> axis(C0 1 0 11) 
>> subplot(2,2,4); 
>> plot(O:dx:l,sol(:,l01)) 
>> axis([0 1 0 11) 
The result, plotted in figure 5.14, looks reasonable, as the heat is progressively 
diffused and lost through the end points. At this point the reader may wish 
to refer back to figure 2.21, which depicts the value of a call option when the 
expiration date is approached. The only difference between figures 5.14 and 
2.21 is that time goes forward for the heat equation, and it goes backward 
for the Black-Scholes equation; in fact, for an option we have a final condi- 
tion rather than an initial one. Apart from this difference, the two solutions 
are qualitatively similar, as the boundary condition is a kinky function which 
is smoothed going forward or backward in time. This is a characteristic of 
parabolic equations, which smooth the irregularities of the boundary condi- 
tions out. On the contrary, these are propagated by hyperbolic equations and, 
as we have seen, by the transport equation. 
However, we note that the discretization with respect to space is a bit 
coarse: we could increase precision by letting 6x = 0.01. We can repeat the 
above set of MATLAB and plot the solution at time instants t = 6t, 26t, 3St, 46t. 
The result is shown in figure 5.15. We see that the solution does not make any 
sense; first, it assumes negative values, which should not be the case for intu- 
itive physical reasons; then it shows an evident instability. The point is that 
here we have chosen discretization steps such that p = 10. In the following 
we show that for stability, the condition 0 < p 5 0.5 is required. 
0 
How can we figure out a way to understand what condition should be 
required on the discretization steps to ensure numerical stability? In the 
case of the transport equation we have used one approach, based on Fourier 
analysis. Here we illustrate a matrix theoretic approach. The explicit method 
of equation (5.19), together with the boundary conditions 
can be represented in matrix terms as 
@j+l = AQj + p g j ,  
j = 0,1,2,. . ., 

308 
FINITE DIFFERENCE METHODS FOR PARTIAL DIFFERENTIAL EQUATIONS 
-100 
-200 IF 
-300 ' 
J 
0 
0.2 
0.4 
0.6 
0.8 
1 
8000, 
I 
Fk. 5.15 Instability in the solution of the heat equation by an explicit method. 
where 
1 - 2 P  
P 
0 
. * .  
0 
0 
p 
1 - 2 p  
... 0 
0 
1 
p 
1 - 2 p  
p 
*
f
a
 0 
0 
.
.
 
.
.
 
0 
0 
*
*
a
 
p 
1 - 2 p  
Note that A E RN-l>N-l is a tridiagonal matrix. Recalling the convergence 
analysis that we carried out in section 3.2.5 for iterative algorithms, it is easy 
to see that the scheme will be stable when 

EXPLICIT AND IMPLICIT METHODS FOR THE HEAT EQUATION 
309 
fig. 5.16 Compiittitioiinl diagram of t~he implicit method for the heat equation. 
But if p > 1/2, then I 1 - 2p I= 2p - 1 and 
and stability carinot be guaranteed. 
To get a more intuitive feeling for this stability condition, we see from figure 
5.12 that the explicit scheme is based on a linear combination of three values 
in the previous time layer. Since the heat equation is a diffusion equation, we 
should take an average of these three values. But an average must be a convex 
combination, with positive weights; indeed, the stability condition makes the 
weight 1 - 2p positive. In a financial framework, similar interpretations can be 
found where weights are interpreted as risk-neutral probabilities, which must 
he positive as well. 
To avoid instability, we may be forced to keep bt very small, since it must 
satisfy the condition bt 5 0.5(Sx)’; if we want accuracy, we must take a small 
62; which is smaller when squared, placing a severe restriction on bt. As this 
may require too much computational effort, an alternative approach may be 
pursued; based on implicit methods. 
5.3.2 
If we use a forward approxirnation for the derivative with respect to time. we 
get an explicit method for the heat equation. We get a completely different 
sclicine if wt: usc a backward approximation: 
Solving the heat equation by a fully implicit method 
4 I J  - 47.J-1 
bt 
In this case we link one known 
values in time layer j :  
value in time layer j - 1 to three unknown 
- / $ f - l , J  + + 2/1)47J 
- p47+1,J = 47,~-1r 
(5.20) 
wliere again p = S t / ( 6 ~ ) ~ :  
see the computational diagram of figure 5.16. Thus, 
the unknown values are givcn implicitly, which is where the “implicit method” 
name coines from; a scheme like this is often referred to as fully zmplicit. We 
have to solve a system of linear equations for each time layer. Since boundary 

31 0 
FINITE DIFFERENCE METHODS FOR PARTIAL DIFFERENTIAL EQUATIONS 
% HeatImp1.m 
function sol = HeatImpl(deltax, deltat, tmax) 
N = round(l/deltax); 
M = round(tmax/deltat) ; 
sol = zeros(N+l,M+l); 
rho = deltat / (deltaxl-2; 
B = diag((l+2*rho) * ones(N-1,l)) - ... 
vetx = 0:deltax:l; 
for i=2:ceil((N+1)/2) 
diag(rho*ones(N-2, l), 1) - diag(rho*ones(N-2,1) ,-1) ; 
sol(i,l) = 2*vetx(i); 
sol(N+2-i, 1) = sol(i, 1) ; 
end 
for j=l:M 
end 
sol(2:N,j+l) = B \ sol(2:N,j); 
Fig. 5.1 7 MATLAB code for the implicit method. 
conditions are given, we have N - 1 equations in N - 1 unknowns. In matrix 
terms, we have to solve a set of systems like 
B@j+l = @ j  + p g j ,  
j = 0, 1,2,. . . , 
(5.21) 
where B E lRN-lzN-l is a tridiagonal matrix, 
B =  
1 f 2 p  
- p  
0 
... 0 
0 
- p  
1 + 2 p  
- p  
. . *  0 
0 
0 
- p  
1 + 2 p  
. * *  
0 
0 
0 
0 
0 
-p 
1 + 2 p  
Example 5.4 The MATLAB code for the implicit method to solve the heat 
equation is illustrated in figure 5.17 (here gj = 0). Note that we are not 
exploiting the fact that the matrix B is tridiagonal, as we simply leave to 
MATLAB the solution of the system of linear equations; the techniques de- 
scribed in section 3.2.4 could and should be used here. Furthermore, a matrix 
factorization like LU would be also useful, since the systems we are solving 
share the same matrix. 
We may verify that the case 6x = 0.1 and 6t = 0.001 does not cause any 
trouble. 
>> dx=O.Ol; 
>> dt=0.001; 
>> tmax=dt*100 ; 

EXPLICIT AND IMPLICIT METHODS FOR THE HEAT EQUATION 
311 
1 ,  
I 
o.2 0 0 u 
0.5 
1 
0.6 
o.8 I 
0.6 
O ' I  
0.2 \...\ 
n " 0 
0.5 
1 
Fig. 5.18 Numerical solution of the heat equation with 6x = 0.1 and 6t = 0.001, by 
the implicit method, for t = 0, t = 0.01, t = 0.05, t = 0.1. 
>> sol=HeatImpl(dx,dt,tmax); 
>> subplot(2,2,1); 
>> plot ( 0 :  dx: 1, s o l (  : ,1) 1 
>> axis(C0 1 0 13) 
>> subplot (2,2,2) ; 
>> plot (0:dx: 1, sol ( : ,111 
>> axis([O 1 0 11) 
>> subplot (2,2,3) ; 
>> plot(O:dx:l,sol(:,51)) 
>> axis(C0 1 0  11) 
>> subplot(2,2,4); 
>> plot(O:dx:l,sol(:,lOl)) 
>> axis(C0 1 0  11) 
The plots in figure 5.18 look less jagged than the plots of figure 5.14), because 
of the smaller discretization step with respect to space. In fact, we may prove 
that the implicit method is unconditionally stable. 
I] 
To prove that the implicit method of equation (5.21) is stable, we may rewrite 
the scheme as 
@j+i = B-l(@j + Pgj), 
from which it is easy to see that stability depends on the spectral radius 
p(B-'). In this case, we may work directly on the spectral radius, rather 
than on a matrix norm. The scheme will be stable if the eigenvalues of B-' 

312 
FINITE DIFFERENCE METHODS FOR PARTIAL DIFFERENTIAL EQUATIONS 
- 
2 
-1 
0 
. ' .  0
0
 
-1 
2 
-1 
... 0
0
 
0 
-1 
2 
... 0
0
 
T =  
.
.
 
.
.
 
-
.
.
 
.
.
 
0 
0 
0 
... -1 
2 
- 
- 
are less than 1 in absolute value; to see that this is indeed the case, we may 
rewrite the matrix as follows: 
B = I + p T ,  
where 
(5.22) 
We will not prove this claim, but we may have a quick informal check with 
MATLAB: 
>> N=6; 
>> T = diag(2*ones(N-l,l)) - diag(ones(N-2,1),1) - ... 
>> s o r t  (eig(T) 1 
0.2679 
1.0000 
2.0000 
3.0000 
3.7321 
diag(ones(N-2,1),-1); 
ans = 
>> s o r t  (4*sin((l :N-l)*pi/(2*N)) . -2) 
ans = 
0.2679 
1.0000 
2.0000 
3.0000 
3.7321 
Now we recall a couple of facts from matrix algebra, which are easily proved: 
0 If X is an eigenvalue of the matrix T, 1 + pX is an eigenvalue of the 
matrix I + pT. 
B-1. 
0 If /3 is an eigenvalue of the matrix B, p-' is an eigenvalue of the matrix 
Putting all together, we may conclude that the eigenvalues of B-' are 
< 1 ,  
k = 1 , 2  ,..., N-1, 
1 
(Yk = 
1 + 4p sin2 (&) 
and the fully implicit scheme is unconditionally stable. 

EXPLICIT AND IMPLICIT METHODS FOR THE HEAT EQUATION 
313 
i-I,j+I 
ij+l 
i+lj+l 
i - l j  
ij 
i + l j  
Fig. 5.19 
tion. 
Conlput,i~t,iurli~l 
diagrilrn of the Crank-Nicolson method for the heat eqiia- 
5.3.3 
Solving the heat equation by the Crank-Nicolson method 
So far. we have seen methods involving three points on one time layer and 
one on il neighboring layer. It is natural to wonder if a better scheme may 
be obtained by considering three points on both layers. One way to do this 
is to consider the point (x,, 
t,+l/z) = (x,, 
t, + 6t/2), which is actually outside 
the grid, and to approxiinate the derivatives at that point using values in the 
six neighboring points 011 the grid. By using Taylor expansions, a5 we did in 
section 5.2, we may see that 
and a central difference approximation for the derivative with respect to time 
in ( x 7 ,  tj+Ip) yields 
Using these two approximations together with the usual ones, we get the 
Craiik-Nicolson scheme: 
-~41-1.3+1+2(1+~)4i,j+l 
-~4i+l.j+1 = ~4i-l,j+2(1-~)4ij+~4i+i,j, (5.23) 
which is represented in figure 5.19. The fundamental feature of this scheme is 
that the error is both O(Sx2) and O(bt2); this implies that less computational 
effort is required to oht,ain a satisfactory degree of accuracy in the numerical 
soliit,ion. 
The Crank-Nicolson scheme may be analyzed in a more general framework. 
Wc may think of using a convex combination of two approximations of the 
second-order derivative in the finite difference scheme: 
+ (1 - W(4i-lj - 24ij + 4i+l,j)I 
(5.24) 
for 0 5 X 5 1. Note that we get the explicit scheme by choosing X = 0, the 
fiilly implicit scheme for X = 1, and the Crank-Nicolson scheme for X = 1/2. 

314 
FINITE DIFFERENCE METHODS FOR PARTIAL DIFFERENTIAL EQUATIONS 
- 
2(1 - P I  
P 
0 
... 0 
0 
P 
2(1 - P) 
P 
0 
p 
2(1-p) 
... 0 
0 
0 
0 
0 
. - .  p 2(1-p) 
0 
... 0 
.
.
 
.
.
 
To see that the Crank-Nicolson scheme is unconditionally stable, we may 
proceed just as with the first implicit scheme. We may rewrite equation (5.23) 
in matrix form: 
where 
C =  
D =  
2(1+P) 
-P 
0 
0 
0 
... 
0 
0 
0 
-P 
... 
-p 
2(1+ P )  
-p 
2(1+P) 
. * *  
0 
0 
Then, using matrix the same matrix T of equation (5.22) again, we may see 
that the eigenvalues of C-lD are 
2 - 4 sin2 (&) 
2 + 4 s i n  2 (m> 
k7r 
(Yk = 
k = 1 , 2 ,  ..., N-1. 
As these eigenvalues are, in absolute value, less than 1, we see that the scheme 
is unconditionally stable. 
5.4 
SOLVING THE BlDlMENSlONAL HEAT EQUATION 
Sometimes, PDEs arising in financial engineering involve two uncertain quan- 
tities. They may be the prices of two assets in a multidimensional option, or 
a price and an interest rate, or a price and a volatility. In these cases we have 
a more complex PDE to deal with. When the dimensionality of the equa- 
tion goes beyond a certain limit, we must necessarily resort to Monte Carlo 
methods, but in two or three dimensions (plus time), finite difference schemes 
can be still applied. To get a feeling for the issues involved, we consider here 
the simplest generalization of the heat equation, i.e., the bidimensional heat 
equation 
(5.25) 
where the unknown function +(t, x, y) is the temperature of a point (z, y) in 
the plane at time t. We may extend the standard grid notation by introducing 

SOLVING THE BlDlMENSlONAL HEAT EQUATION 
315 
discretization steps bx, by, and bt: 
q!(kbt,ibs,jby) 
4fj, 
where time index k is written as a superscript and should not be confused 
with a power. For the sake of simplicity we will assume that we are interested 
in the solution on the unit square 
given initial and boundary conditions. 
Just like in the onedimensional case, we may use central differences for 
the second-order spatial derivatives. If we use the forward difference for the 
derivative with respect to time, we get the finite difference approximation: 
This immediately leads to an explicit scheme: 
where 
bt 
bt 
P -- 
- ( h X ) 2 '  
PY = (62)2 
This method is relatively straightforward to implement, but it suffers from 
instability. It can be shown that a stability condition is: 
1 
PX+P 
-. 
y - 2  
This condition may be interpreted intuitively as usual: it just makes sure that 
we are taking a convex combination of five neighboring values in the previous 
time layer to get the value 41";". 
This implies a rather severe condition on 6t, 
just like the onedimensional case. However, in this case an explicit algorithm 
is more time-consuming and requires more memory. In fact, now we must 
solve the equation by avoiding storage of a tridimensional array, whereas in 
the one-dimensional case we stored all the solution in one matrix. We alternate 
time layers, keeping track of two consecutive ones, and swapping them as time 
goes forward. 
A code to implement this explicit method is shown in figure 5.20. A few 
comments are in order here. 
0 The input arguments are: 
- the three discretization steps (dt, dx, dy) 
- the time Tmax at which we want to stop the solution process 

316 
FlNITE DFFERENCE METHODS FOR PARTIAL DlFFfRfNTlAL EQUATIONS 
function U = Heat2D(dt, dx, dy, Tmax, Tsnap, value, bounds) 
% make sure steps are consistent 
Nx = 
dx = 
Ny = 
dy = 
Nt = 
dt = 
rhox 
rhoy 
round(l/dx) ; 
l/Nx; 
round(l/dy) ; 
1/Ny; 
round(Tmax/dt) ; 
Tmax/Nt ; 
= dt/dx^2; 
= dt/dy^2; 
if 
end 
C1 = 1-2*rhox-2*rhoy; 
Layers = zeros(2, 1+Nx, 1+Ny) ; 
tpast = 1; 
tnow = 2; 
iTsnap = Tsnap/dt; 
[X, Y] = meshgrid(O:dx:l, 0:dy:l); 
% set up initial conditions and plot 
Layers(tpast, (l+round(bounds(l)/dx)):(l+round(bounds(2)/dx)), 
... 
(l+round(bounds(3)/dy)) 
: (l+round(bounds(4)/dy) 
)) = value; 
U = shif tdim(Layers (tpast, : , : 1) ; 
figure ; 
surf (X,Y,U) ; 
title(’t=O’, ’Fontsize’ ’12); 
% Carry out iterations 
for t=l :Nt 
rhox + rhoy > 0.5 
fprintf(1,’Warning: bad selection of steps\n’); 
for i=2:Nx 
for j=2 : Ny 
Layers(tnow,i,j) = Cl*Layers(tpast,i,j) + . . . 
rhox*(Layers(tpast,i+l,j) + Layers(tpast,i-l,j)) + . . . 
rhoy*(Layers(tpast,i,j+l) + Layers(tpast,i,j-1)); 
end 
end 
if find(iTsnap == t) 
% Plot if required 
U = shif tdim(Layers (tnow, : , : 1) ; 
figure ; 
surf (X,Y,U) ; 
title([’t=’, num2str(Tsnap(l)) 
I ,  ’Fontsize’,lZ); 
Tsnap(1) = [I; 
end 
tnow = l+mod(t+l,2); 
tpast = l+mod(t,2); 
% Swap layers 
end 
Fig. 5.20 Code to solve the bidimensional heat equation by an implicit method. 

SOLVING THE BIDIMENSIONAL HEAT EQUATION 
31 7 
dt = 0.0001; 
dx = 0.05; 
dy = 0.05; 
value = 10; 
bounds = E0.7, 0.9, 0.1, 0.91; 
Tmax = 0.1; 
Tsnap = EO.01, 0 . 0 2 ,  0.03, 0.04, 0.05, 0.061; 
U = Heat2D(dt, dx, dy, Tmax, Tsnap, value, bounds); 
Fig. 5.21 Script to test Heat2D. 
- a vector Tsnap of time instants at which we want to display a plot 
- a value value and a four-dimensional vector bounds to store the 
of the solution 
initial conditions, which we assume of the form 
V for 0 < bl 5 x 5 bz < 1 and 0 < b3 5 y 5 b4 < 1 
4(x7 ” = { 0 
otherwise. 
0 In the first few lines we check consistency of discretization steps with the 
boundaries of the domain, changing discretization steps a bit if neces- 
sary. Then we precompute fixed quantities outside the main loop of the 
procedure (issuing a warning message if discretization steps may lead to 
instability). 
0 The solution is stored in two consecutive layers of size (1 + N,) x (1 + 
Ny), which form the tridimensional array Layers. The two layers are 
alternated, as one is indexed by tnow and the other one by tpast; these 
two indexes are incremented modulo two at the end of the main loop 
(so that copying a matrix is not necessary). 
0 Plots are displayed in separate figures (with some heading) at time t = 0 
and when required; to that purpose we must use meshgrid to set up 
matrices of coordinates in the plane, and shiftdim to transform one 
layer in the tridimensional array Layers to the bidimensional array U. 
0 Finally, things are made a bit more complicated by the fact that in 
mathematics we start subscripts from 0, whereas in MATLAB array 
indexing starts from 1. 
Running the script of figure 5.21 we get a set of surfaces, three of which are 
displayed in figure 5.22. 
The explicit method may prove time-consuming because of the restriction 
on the time step, and we would like to have stability guarantees typically 
associated with implicit methods. A fully implicit method is easily obtained 

318 
FINITE DIFFERENCE METHODS FOR PARTIAL DIFFERENTIAL EQUATIONS 
Fig. 5.22 Numerical solution of the bidimensional heat equation by an explicit 
met hod. 

SOLVING THE BlDlMENSlONAL HEAT EQUATION 
319 
by taking a backward approximation of the derivative with respect to time, 
but in the bidimensional case we have a system of linear equations which may 
be time-consuming to solve, since there is no easy structure to exploit. 
Alternative approaches have been proposed, including the Alternating Di- 
rection Implicit (ADI) method. There are several variations on this theme, 
and we will just describe the simplest one, due to Peaceman and Rachford. 
A sound motivation of the scheme would call for a detailed analysis of finite 
difference operators and their truncation errors, which together with a stabil- 
ity analysis would prove convergence. Since this is not trivial, we refer the 
reader to the references listed at the end of the ~ h a p t e r . ~  
The intuitive idea 
is to introduce an intermediate time layer in the solution process, stepping 
from t to t + 6t/2, and to use an approximation scheme which is implicit with 
respect to one of the two space dimensions, and explicit with respect to the 
other one. Then we step from t + 6t/2 to t + 6t, swapping the role of the two 
space dimensions. The net effect is to solve the bidimensional problem as a 
set of one-dimensional ones. 
We can specify the method in detail by using first a difference scheme based 
on points (2, y, t )  and (z, y, t + 6t/2): 
Note that the scheme is implicit in x but explicit in y, since the second-order 
derivative for z is approximated by a central difference on time layer k + 112 
rather than on time layer k. This may look arbitrary, but it introduces a 
truncation error which is comparable to other terms. Equation (5.27) can be 
rewritten as 
which can be rearranged by separating what is known and what is not: 
(5.28) 
We should note that everything is known on the right-hand side, whereas on 
the left-hand side subscript j is fixed; hence we may solve one tridiagonal 
system for each j ,  i.e., for given y. Indeed, we see that a bidimensional 
problem is decomposed into a sequence of one-dimensional problems. By the 
same token, we can step forward to Ic + 1, reversing the roles of i and j. The 
starting point is the finite difference scheme: 
51n particular, we suggest section 7.3 of [7] or chapter 3 of [4]. 

320 
FINITE D/FF€R€NCE METHODS FOR PARTIAL DIFFERENTIAL EQUATIONS 
which is explicit in x and implicit in y and can be rearranged to 
PY k + l  
k + l  
PY k + l  
PI 
k + L  
k+' 
p x  k+' 
--4i,j-1+ 
2 
(1 + PyI4i.j - Z4i,j+l = pi-& 
+ (1 - P X M i j  + 7 4 i + < j .  
(5.30) 
In this case, we solve one tridiagonal system for each value of II: in the time 
layer. 
The idea is implemented in the MATLAB code displayed in figures 5.23 
and 5.24. The remarks we have made for the implementation of the explicit 
method apply here too, with some additional issues: 
We use LU factorization of both matrices involved, since they are con- 
stant with respect to time, resulting in matrices Ll, U1, L2, and U2; 
right-hand sides of systems are stored in vectors Rhsl and Rhs2. 
0 The intermediate layer for time t + 6t/2 is stored in the bidimensional 
array Auxlayer, which is the unknown in the first system, and makes 
up the right-hand side in the second one. 
In checking the code pay attention to the shift from mathematical sub- 
scripts to MATLAB array indexing. 
The code may be easily tested by adapting the script of figure 5.21. 
5.5 
CONVERGENCE, CONSISTENCY, AND STABILITY 
We have developed finite difference schemes, and we have informally noted 
that there is some truncation error that tends to zero as the discretization 
steps tend to zero. We would expect that this ensures the convergence of the 
solution to the difference equations to the solution of the differential equation. 
However, the counterexample of section 5.2.1 shows that the matter is not 
so trivial, since we should consider carefully the interplay of three concepts: 
convergence, stability, and consistency. The point is that the solution of the 
finite difference equations for discretization steps ax,& -+ 
0 could converge 
to a function which is not the solution of the PDE. A rigorous analysis of 
these concepts and their relationships is beyond the scope of the book, but 
we would like to give at least a glimpse into these topics. 
An initial value problem such as the familiar heat equation is defined over 
a space/time domain 
The problem can be cast in a more abstract way as 
v x (0 < t < w). 
where L is a differential operator, f is a known function, and 4 is the unknown 
function we seek to determine. When we set up a discrete grid BA, we also 

CON VERGEN CE, CONSISTENCY, AND STABILITY 
321 
function U = Heat2DADI(dt, dx, dy, Tmax, Tsnap, value, bounds) 
X make sure steps are consistent 
Nx = round(l/dx); 
dx = 1/Nx; 
Ny = round(l/dy); 
dy = 1/Ny; 
Nt = round (Tmax/dt ) ; 
dt = Tmax/Nt; 
rhox = dt/dx^2; 
rhoy = dt/dy^2; 
Layers = zeros(2, 1+Nx, 1+Ny) ; 
Auxlayer = zeros (1+Nx, 1+Ny) ; 
tpast = 1; 
tnow = 2; 
iTsnap = Tsnap/dt; 
[X, Y] = meshgrid(O:dx:l, 0:dy:l); 
% set up initial conditions 
Layers(tpast, (l+round(bounds(l)/dx)):(l+round(bounds(2~/dx~~, . . .  
(l+round(bounds(3)/dy)):(l+round(bounds(4)/dy))) 
= value; 
U = shiftdim(Layers(tpast,:,:)); 
figure ; 
surf(X,Y,U); 
title(’t=O’, ’Fontsize’ ,121 ; 
% Prepare matrices and LU decomposition 
Matrix1 = diag((l+rhox)*ones(Nx-l,l)) 
+ ... 
diag(-rhox/2*ones(Nx-2,1),1) + ... 
diag(-rhox/2*ones(Nx-2,1),-1); 
[Ll, U11 = lu(Matrix1); 
Matrix2 = diag((l+rhoy)*ones(Ny-1,l)) 
+ ... 
diag(-rhoy/2*ones(Ny-2,1),1) + . . .  
diag(-rhoy/2*ones(Ny-2,1) ,-1) ; 
[L2, U21 = lu(Matrix2); 
Rhsl = zeros(Nx-1,l); 
Rhs2 = zeros (Ny-l,l) ; 
Fig. 5.23 Code to solve the bidiniensional heat equation by an AD1 method (continued 
in figure 5.24). 

322 
FINITE DIFFERENCE METHODS FOR PARTIAL DIFFERENTIAL EQUATIONS 
% Carry out iterations 
for t=l : Nt 
% first half step 
for j =1: Ny- 1 
% set up right hand side 
for i=l:Nx-1 
Rhsl(i) = rhoy/2*Layers(tpast,i+l,j) + ... 
(1-rhoy)*Layers(tpast,i+l,j+l) + ... 
rhoy/2*Layers (tpast , i+l , j+2) ; 
end 
% solve 
Auxlayer(2:Nx,j+l) = U1 \ (L1 \ Rhsl); 
end 
% second half step 
for i=l:Nx-1 
% set up right hand side 
for j=l:Ny-1 
Rhs2(j) = rhox/2*Auxlayer(i,j+l) + . . . 
(1-rhox)*Auxlayer(i+l,j+l) + . . . 
rhox/2*Auxlayer(i+2,j+l) ; 
end 
% solve 
Layers(tnow, i+l,2:Ny) = (U2 \ (L2 \ Rhs2) 1 ; 
end 
1 plot if necessary 
if find(iTsnap == t) 
U = shiftdim(Layers(tnow,: ,:I); 
figure ; 
surf (X,Y,U) ; 
title(['t=', num2str(Tsnap(l)) 
1 ,'FontsizeJ,12); 
Tsnap(1) = [I; 
end 
2 swap layers 
tnow = l+mod(t+l,2); 
tpast = l+mod(t,2); 
end 
Fig. 5.24 
from figure 5.23). 
Code to solve the bidimensional heat equation by an AD1 method (continued 

CONVERGENCE, CONSISTENCY, AND STABlLlTY 
323 
discretize the operator L by an operator La. Given a function $ and a point 
(Pilt,) E GA, we may consider the truncation error 
t $ ( P i ~  
tj) = L$(Pi, tj) - LA$(Pi, t j ) .  
If, when the grid is refined and the discretization steps tend to zero, this 
truncation error tends to zero,‘ the numerical scheme is said to be consistent. 
This essentially says that the finite difference representation we are using 
tends to the PDEs we are interested in. 
The stability issue is concerned basically with whether or not the difference 
between the numerical solution and the exact solution remains bounded as 
time progresses. To be more specific, consider the heat equation of section 
5.3. Let q5ij be the solution of the finite difference scheme and +(x,t) the 
correct solution of the PDE. We may investigate 
0 the behavior of 1 & - 4(i 62, j bt) 1 as j + CQ for fixed discretization 
steps bx and bt, 
0 or the behavior of I g5ij - +(z bx, j bt) I as bx,6t -+ 0 for a fixed value of 
j 6t. 
The first issue is related to stability; the second issue is related to convergence. 
To ensure the convergence of the numerical solution to the exact solution, 
the consistency condition is not enough. However, it can be shown (Lax’s 
equivalence theorem; see [5]) that for a well-posed linear initial value problem, 
stability is a necessary and sufficient condition for convergence of a consistent 
numerical scheme. As the following example shows, the numerical scheme of 
section 5.2.1 is not stable, and this is why it fails to converge. 
Example 5.5 For the sake of convenience, let us recall the numerical scheme 
of section 5.2.1 for the transport equation with constant velocity c: 
where p = ax/&. We may apply the same Von Neumann analysis of stability 
that we applied in example 5.2. Leaving the details as an exercise, we may 
see that in this case 
3 
42j = E (-l)i (1 + 2;) 
. 
Since c and p are both positive, we see that +ij goes to infinity as j + DC). 
Hence, the scheme is unconditionally unstable and convergence is not ensured 
even if the discretization steps tend to zero. 
0 
“his 
should be made more precise, as the space and time discretization steps could tend 
to zero in an arbitrary way, or with some relationship between them. 

324 
FINITE DIFFERENCE METHODS FOR PARTIAL DIFFERENTIAL EQUATIONS 
For further reading 
0 Partial differential equations are a large and complicated topic. For an 
introduction including both classical and advanced concepts, see, e.g., 
[ 3 1 . ~  
0 Another book covering PDEs in a relatively general setting is [l], which 
also includes many pieces of MATLAB code. 
0 A classical reference on finite difference methods for PDEs is [6]. See 
also [4] and [8]. 
0 A recent addition to the literature on finite difference schemes is [7]. 
0 Advanced issues, including the important Lax theorem, are covered in 
[51. 
0 To see extensive examples of PDEs in action to tackle financial engi- 
neering problems, see [9] or [lo]. 
REFERENCES 
1. J. Cooper. Introduction to Partial Differential Equations with MATLAB. 
Birkhauser, Berlin, 1998. 
2. D.G. Luenberger. Investment Science. Oxford University Press, New 
York. 1998. 
3. R. McOwen. Partial Differential Equations: Methods and Applications. 
Prentice Hall, Upper Saddle River, NJ, 1996. 
4. K.W. Morton and D.F. Mayers. Numerical Solution of Partial Differential 
Equations (2nd ed.). Cambridge University Press, Cambridge, 2005. 
5. R.D. Richtmyer and K.W. Morton. Difference Methods for Initial Value 
Problems (2nd ed.). Wiley, New York, 1967. Reprinted in 1994 by Krieger, 
New York. 
6. G.D. Smith. Numerical Solution of Partial Differential Equations: Finite 
Diflerence Methods (3rd ed.). Oxford University Press, Oxford, 1985. 
7. J.C. Strickwerda. Finite Difference Schemes and Partial Difference Equa- 
tions. SIAM, Philadelphia, PA, 2004. 
7An erratasheet for this book is available at www.math.neu.edu/~mcowen/mathindex.html. 

REFERENCES 
325 
8. J.W. Thomas. Numerical Partial Differential Equations: Finite Differ- 
ence Methods. Springer-Verlag, New York, 1995. 
9. P. Wilmott. Derivatives: The Theory and Practice of Financial Engineer- 
ing. Wiley, Chichester, West Sussex, England, 1999. 
10. P. Wilmott. Quantitative Finance (vols. I and II). Wiley, Chichester, 
West Sussex, England, 2000. 

This Page Intentionally Left Blank

6 
Convex Optimization 
Optimization methods play an important role in finance. As we have seen 
in chapter 2, optimization models may be used in portfolio management, in 
which case they are used as a decision support tool; sometimes, optimization 
methods are somewhat more instrumental and are used, e.g., to solve model 
calibration problems. Covering in depth all optimization methods that could 
be useful in solving finance-related problems would require a few books (tough 
ones, by the way). The aim of this chapter is much less ambitious. We want 
to provide the reader with a minimal background required to grasp what 
MATLAB offers in the Optimization toolbox; in particular, one should know 
what she’s doing when choosing one among the various methods that are 
available to cope with the same type of problem. 
To simplify things, we consider only basic optimization problems in this 
chapter. In particular, we assume they are convex and deterministic. Basic 
notions on convexity are summarized in supplement S6.1 at the end of this 
chapter. Basically, convexity ensures that a local optimum is a global one, 
and allows to find easy characterizations of optimal solutions, which pave the 
way to solution algorithms. Optimization models and methods in non-convex 
cases are dealt with in chapter 12. When data are uncertain, we should resort 
to stochastic optimization models, which is quite important in the context of 
dynamic decision making over time. There are two basic approaches to cope 
with dynamic decision making under uncertainty: dynamic programming and 
stochastic programming with recourse. Dynamic programming is described 
in chapter 10, where we also describe its role in pricing American options 
by Monte Carlo simulation; stochastic programming with recourse is covered 
in chapter 11. Actually, these two approaches have a lot in common, but 
327 

328 
CONVEX OPTIMIZATION 
apparently the first one is quite common in Economics, whereas the second 
one is more appreciated within the engineering community. We will try to 
explain why in later chapters. 
We first provide a framework to classify optimization models in section 6.1. 
In fact, models may be classified along many directions, including constrained 
and unconstrained problems. Unconstrained optimization is covered in sec- 
tion 6.2. Methods for unconstrained optimization differ in their requirements; 
many are gradient-based, and require the ability of computing or approxi- 
mating function derivatives; other methods are derivative-free, in the sense 
that they are just based on function evaluations.' Constrained optimization 
is dealt with in section 6.3, where we also introduce fundamental theoretical 
concepts like Kuhn-Tucker conditions and duality theory. A specific case of 
constrained optimization is linear programming, which is the topic of section 
6.4; quite often, non-trivial problems may be expressed as linear programming 
models, and the ability to solve really huge optimization problems efficiently 
make linear programming a fundamental tool. We illustrate MATLAB func- 
tions all along the way with small toy examples, and we close with more 
significant examples in section 6.5. 
Finally, we should bear in mind that optimization methods typically assume 
that we are able to capture the desirability of a solution by a function given 
in closed form. But analytical models may be too complex or not available at 
all, and we may be forced to resort to simulation tools for performance evalu- 
ation. The integration of simulation and optimization techniques is described 
in section 6.6. 
6.1 CLASSIFICATION OF OPTIMIZATION PROBLEMS 
There is a huge variety of optimization models that we meet in financial 
applications, which can be tackled by an equally vast array of methods. Hence, 
the starting point of this chapter should be a listing of the basic features by 
which an optimization model may be characterized. 
6.1.1 Finite- vs. infinite-dimensional problems 
In this chapter we are concerned with problems whose abstract form is 
min 
f(x) 
s.t. 
x E s c IWn. 
Derivative-free optimization methods are the core of a recently released MATLAB toolbox, 
called Genetic Algorithm and Direct Search. We outline genetic algorithms in section 12.4. 

CLASSIFICATION OF OPTIMIZATION PROBLEMS 
329 
The objective function f is a scalar function quantifying the suitability of 
a solution x, which is a vector of decision variables and must belong to a 
feasible set S, which is a subset of the set of vectors with n real components. 
Since the solution is expressed by a finite-dimensional vector, we speak of a 
finite-dimensional problem. There is no loss of generality in considering only 
minimization problems, since a maximization problem may be transformed 
into a minimization problem simply by changing the sign in the objective: 
maxf(2) =+ - min[-f(s)]. 
Indeed, all MATLAB functions in the Optimization toolbox assume a mini- 
mization problem. Solving an optimization problem like (6.1) means finding 
a point x* E S such that 
f(x*) 5 f(x) 
vx E s. 
The point x* is said to be a global optimum (the terms optimizer or min- 
imizer are also used to avoid confusion between the optimal point and the 
corresponding value of the objective function). Neither the existence nor the 
uniqueness of a global optimum should be taken for granted. To begin with, 
the problem may be unbounded, which is the case if there is a sequence of 
solutions x ( ~ )  
E S such that 
lim f ( ~ ( ~ ) )  
= -oo. 
Furthermore, the problem may be infeasible, i.e., the feasible set S may be 
empty. Finally, the solution is not unique when condition (6.2) is satisfied 
by a set of alternative optima, which may be a discrete and finite set, or an 
infinite set. If the condition (6.2) holds only in a neighborhood of x*, we 
speak of a local optimum. 
Example 6.1 A typical objective function that gives rise to local optima is 
a polynomial function; recall that the oscillatory behavior of high-order poly- 
nomials is the reason why they are not well-suited to function interpolation 
(see example 3.16 on page 179). We may check this with a simple MATLAB 
snapshot. Consider a polynomial like 
k - m  
f(x) = z4 - 1 0 . 5 ~ ~  
+ 392' - 59.52 + 30 
and use MATLAB to plot it. 
>> g = @(x) polyval( [ 1 -10.5 39 -59.5 301, x ) ;  
>> xvet=1:0.05:4; 
>> plot(xvet,g(xvet)) 
The plot produced is illustrated in figure 6.1, from which it is clear that there 
are two local minimizers. One MATLAB function to solve a minimization 

330 
CONVEX OPTIMIZATION 
1.5 
2 
2.5 
3 
3.5 
-2‘ 
Fig. 6.1 Global and local optima for a polynomial. 
problem is fminunc; the "uric" stands for unconstrained, since we are not 
enforcing any requirement on the decision variable. This function requires an 
argument which is the initial point of the search process. 
>> [x,fval] = fminunc(g, 0) 
Warning: Gradient must be provided for trust-region method; 
using line-search method instead. 
x =  
1.4878 
-1.8757 
fval = 
>> [x,fval] = fminunc(g, 5) 
Warning: Gradient must be provided f o r  trust-region method; 
using line-search method instead. 
x =  
3.6437 
-0.6935 
fval = 
We see that depending on the starting point, we get the global or the local 
minimizer. The MATLAB output has been cut a little, but we see some 
messages concerning trust regions and line search; the meaning of these terms 
is illustrated in the following (this is all this chapter is about, after all). A 
different situation occurs in the following case: 
>> f = O(X) polyval( C I -8 22 -24 11 , X); 
>> xvet=0:0.05:4; 
>> plot (xvet , f (xvet) 1 

CLASSIFICATION OF OPT/M/ZAT/ON PROBLEMS 
331 
Fig. 6.2 Objective function with two global optima. 
The plot is shown in figure 6.2. It may be seen that we have two alternative 
global minima. 
0 
Example 6.2 It is easy to build problems which are, respectively: 
1. Unbounded: 
max 
xy+xi 
s.t. 
5 1  + x2 2 4 
x1,xz 2 0. 
2 .  Infeasible: 
max 
2x1 + 3 x 2  
s.t. 
2 1  + 2 2  L 4 
0 i x1,52 5 1. 
3. Characterized by an infinite set of optima: 
max 
2 1  +xz 
s.t. 
2 1  + 2 2  5 4 
Z l r Z 2  2 0. 
The reader is urged to check this by drawing the feasible set and the level 
curves of the objective function. 
Another important remark is that some problems may have no solution 
because they are posed the wrong way. Consider the innocent-looking example 
min 
z 
s.t. 
z > 2. 

332 
CONVEX OPTIMIZATION 
This problem has no solution, as the feasible set is open, and the apparently 
obvious solution x = 2 is not feasible. In fact, there is not a minimum but only 
an infimum. This is why in any optimization software you only get constraints 
such as 2 or 5, so that the feasible set is a closed region. 
0 
So far we have assumed that the feasible set is a subset of the space on 
n-dimensional vectors with real components. In infinite-dimensional problems 
the solution is represented by an infinite collection of decision variables. This 
is the case when the solution we are seeking is a function of time over a 
continuous interval. Consider, for instance, a continuous-time dynamic system 
represented by the vector differential equation 
X(t) = “(t), U(t)l, 
where x is the vector of state variables and u is the vector of control inputs. 
An optimal control u(t), t E [0, T] for this system may be found by solving 
T 
min 
f[x(t>,u(t)l 
dt + g[x(T)I 
s.t. 
X(t) = h[x(t), 
~ ( t ) ]  Vt E [0, T] 
x(0) = XI) 
U(t) E R 
vt E [O,T], 
where [0, T] is the time horizon we are interested in, xo is the (known) initial 
state of the system, and fl is the set of admissible controls. The objective 
function includes both a trajectory cost, depending on both states and controls, 
and a terminal cost, depending on the terminal state x(T). It is also possible 
to specify some constraints on the terminal state. 
There is a vast literature on optimal control models in finance. They are 
actually formulated within a stochastic setting (returns are random and mod- 
eled by stochastic differential equations as discussed in chapter 2) and solved 
by dynamic programming (see, e.g., [13]). Optimal control methods are an ex- 
cellent tool to analyze relatively simple models and to derive valuable insights 
from a qualitative and theoretical point of view; however, it might be argued 
that, in general, complex and realistic problems are usually best formulated 
and solved as finite-dimensional models. This is an admittedly debatable 
point, as many would disagree, particularly when it comes to stochastic mod- 
els for finance (see, e.g., [12] for an alternative view). Anyway, we do not deal 
with this class of models, essentially to keep the book to a reasonable size. It 
is worth noting that finite-dimensional models may be used to approximate 
infinite-dimensional problems by discretizing the continuous-time model. For 
instance, the infinite-dimensional problem above can be transformed into the 
finite-dimensional problem 
K 
min c 
f ( X k ,  U k )  + g(xK) 
k = l  

CLASSIFICATION OF OPTIMIZATION PROBLEMS 
333 
where the time horizon has been discretized in time intervals of width dt and 
xk = x ( k d t ) .  Note that xk is the state at the end of the kth period [i.e., the 
period between (Ic - 1)dt and k dt], whereas u k  is the control applied during 
the kth period. 
6.1.2 
Unconstrained vs. constrained problems 
If S = R”, we have an unconstrained problem; otherwise, we have a con- 
strained problem. Needless to say, real-life problems are rarely unconstrained; 
yet methods for unconstrained optimization are the foundation for many con- 
strained optimization methods. The set S is usually specified by enforcing 
the following types of constraints on the decision variables. 
Equality constraints: 
hi(X) = 0, 
i E E, 
or in vector form: 
h ( x )  = 0. 
0 Inequality constraints: 
S i ( X )  L 0, 
i E I .  
or in vector form: 
d x )  LO, 
having stipulated that a vector inequality is interpreted componentwise. 
The constraint gi(x) L 0 is said to be active at the point 12 if gi(x) = 0, 
and inactive if gi(12) < 0. A “greater than” constraint such as & ( X )  2 0 
can be rewritten immediately in the form - g k ( X )  5 0. In MATLAB, in- 
equality constraints are assumed in the “less than” form. Non-negativity 
restrictions such as x 2 0, also denoted by x E R+, may be thought of 
as inequality constraints. However, simple bounding constraints of the 
form 1 5 x 5 u are usually dealt with in a special way by optimiza- 
tion algorithms; hence, inequality constraints and bounds are passed 
separately to optimization procedures. 
6.1.3 
Convex vs. non-convex problems 
Depending on the nature of the objective function f and of the feasible set 
S, problem (6.1) may or may not be easy. In particular, when there is only 
one local optimum which is also the global optimum, the problem should be 

334 
CONVEX OPTIMIZATION 
expected to be relatively easy. The key concept here, and in most optimization 
theory as well, is convexity. Some background in convex analysis is given in 
supplement S6.1 at the end of the chapter. 
Problem (6.1) is a convex problem iff is a convex function and S is a convex 
set. Problem (6.1) is a concave problem if f is a concave function and S is 
a convex set. Assuming that the optimization problem has a finite solution, 
the following properties can be proved. 
PROPERTY 6.1 In a convex problem a local optimum is also a global op- 
timum. 
PROPERTY 6.2 In a concave problem the global optimum lies on the bound- 
ary of the feasible region s. 
To get a feeling for the second property, the reader is urged to solve the 
following problem graphically: 
min 
-(x - 2)2 + 3 
1 5 x 5 4. 
s.t. 
Ideally, we would like to come up with a set of necessary and sufficient 
conditions for global optimality. Regrettably, what we have, in general, are 
just either sufficient or necessary conditions for local or global optimality. 
However, when the problem is unconstrained and the function is convex, it is 
easy to find a convenient characterization of a global minimizer. 
THEOREM 6.3 If the function f is convex and differentiable on R”, the 
point x* is a global minimizer off if and only if it satisfies the stationarity 
condition: 
Vf(X*) = 0. 
f(x) 2 f(xo)+vf’(Xo)(X--o) 
vx,xo. 
Proof. Iff is convex and differentiable, then we have 
But if the function is stationary at point x*, 
f (x) 2 f (x*) + v f’(x*)(x - x*) = f (x*) + O’(x - x*) = f (x*) 
vx, 
which simply says that x* is a global optimum. 
0 
The stationarity condition is a first-order condition; for generic functions, 
second-order conditions involving the Hessian matrix are required to guaran- 
tee that a stationary point is actually a (local) minimizer. The stationarity 
condition is easily extended to the case of a convex non-differentiable function. 
THEOREM 6.4 If the function f is convex on R”, the point x* is a global 
minimizer off if and only i f  the subdiflerential off at x* includes the zero 
vector: 
0 E af(X*). 

CLASSIFICATION OF OPTIMIZATION PROBLEMS 
335 
Proof. As discussed in supplement S6.1, a convex function f is subdifferen- 
tiable at any point2; that is, at any point xo there is a set of subgradients, 
which is called the subdifferential. A subgradient at xo is a vector y such that 
It is easy to see that if 0 belongs to the subdifferential at x*, we have f ( x )  2 
f ( x * )  for any x .  It is worth noting that this theorem is a generalization of 
the previous one, as if the function is differentiable in x*, the subdifferential 
includes only the gradient, and this condition boils down to stationarity. 
0 
It should be noted that a set S = { x  E Rn 
1 gz(x) 5 0, i E I} is convex if 
the functions gi are convex. To see this for a single function g(x), assume 
that XI, 
x2 E S. Convexity of g implies that 
Since the intersection of convex sets is a convex set, the result is valid for an 
arbitrary number of convex functions. The equality-constrained case is more 
critical. Since an inequality constraint hi(x) = 0 can be thought of as two 
inequalities , 
hi(x) L 0, 
-hi(x) 5 0, 
we see that it will describe a convex set only if the function hi is both convex 
and concave. This will be the case only if hi is affine, i.e., it is of the form 
6.1.4 
Linear vs. non-linear problems 
A finite-dimensional problem is called a linear programming (LP) problem 
when both the constraints and the objective are expressed by affine functions. 
The general form of a linear programming problem is 
j = 1  
n 
.j = 1 
’Strictly speaking, this is true only for the interior of the domain over which the function 
is convex. 

336 
CONVEX OPTIMIZATION 
which can be written in matrix form as 
min 
c’x 
s.t. 
Ax = b 
D x  5 e. 
Linear programming problems have two important features; they are both 
convex and concave problems. Thus, a local optimum is also a global one, 
and it lies on the boundary of the feasible solution; actually, it turns out that 
the feasible set is a polyhedron and that there is an optimal solution which 
corresponds to one of its vertices. 
Example 6.3 Here is an example of an LP problem: 
min 
s.t. 
2 x 1  + 3 x 2  + 3 x 3  
2 1  + 2 x 2  = 3 
X I +  2 3  L 3 
X l , X 2 , X 3  L 0. 
If either condition is not met, i.e., if the objective function or a constraint is 
expressed by a non-linear function, we have a non-linear programming prob- 
lem. 
Example 6.4 The following are examples of non-linear programming prob- 
lems: 
min 
s.t. 
min 
s.t. 
min 
s.t. 
22; + 32; + 3 5 1 x 3  
2 1  + 2 x 2  = 3 
2 1  + 2 3  L 3 
X l , X 2 ,  x 3  L 0. 

CLASSIFICATION OF OPTIMIZATION PROBLEMS 
337 
The last problem is characterized by a quadratic objective function and by 
linear constraints. This kind of problem is called a quadratic programming 
problem. Quadratic programming problems are the simplest non-linear pro- 
gramming problems, provided that the objective function is convex. If the 
quadratic part of the objective is related to a covariance matrix, as it happens 
for mean-variance portfolio optimization, the objective function is convex, as 
the covariance matrix is positive semidefinite (see theorem 6.11 in supplement 
S6.1.1). 
0 
6.1.5 
Continuous vs. discrete problems 
Linear and quadratic programming problems are rather easy to solve, as they 
are convex problems. In some decision problems, it is necessary to enforce 
integrality constraints on some decision variables: 
X E Z?, 
where Z+ = (0,1,2,. . .} is the set of non-negative integers (models involving 
negative integer variables are quite rare). If the integrality constraint applies 
to all of the decision variables, we have a pure integer program; otherwise, we 
have a mixed-integer program. Such a restriction makes the problem much 
harder, mainly because a discrete feasible region is not convex. While non- 
linear integer programming techniques are known, robust commercial tools 
are available only for mixed-integer linear  program^.^ 
Quite often, an integrality restriction has the form 2 E (0, l}, which is 
used when we have to model all-or-nothing decisions. One such case is the 
knapsack problem we met in example 1.2 on page 15. We will illustrate 
several “modeling tricks” based on logical variables in section 12.1.1. We 
should mention that past versions of the Optimization toolbox were not able 
to cope with discrete optimization problems. At the time of writing, a function 
bintprog is available to solve pure binary problems, i.e., linear programming 
problems in which all the decision variables are restricted to the set (0,l). 
This is a limited functionality which could be improved in future versions to 
cope with general mixed-integer problems. Nevertheless, we should mention 
that large-scale mixed-integer problems are a hard nut to crack and that 
specialized state-of-the-art packages are required. 
6.1.6 
Deterministic vs. stochastic problems 
All the model classes we have considered so far assume, on the one hand, 
that there is no uncertainty in the data and, on the other one, that a sensible 
analytical model can be built. In some cases, building an analytical model 
3However, recently released versions of ILOG CPLEX are able to solve mixed-integer 
quadratic problems. 

338 
CONVEX OPTIMIZATION 
is out of the question, because of both the randomness and the complexity 
involved. As an example, consider a set of rules for portfolio rebalancing; say 
these rules depend on a set of parameters and that you would like to find the 
optimal value of these parameters. It may be the case that a thorough testing 
of the rules may be carried out only by running a set of simulated experiments. 
This means that a simulator acts as a black box mapping a vector of decision 
variables x into an estimate of an objective function f(x) = E[U(x)], possibly 
related to an expected utility. In this case, you have to integrate stochastic 
simulation and optimization methods, as described in section 6.6. 
In other cases, we may be able to build an optimization model, but uncer- 
tainty in the problem data prevents the application of standard optimization 
methods. It is fairly obvious that coping with uncertain data is a significant 
complication, but there is a subtler issue. When uncertainty is involved, we 
should consider how and when the “true” values of the problem data are dis- 
covered: In fact, time and information are likely to play a role, since decision 
making under uncertainty typically involves a dynamic process in which de- 
cisions are ‘Ladjusted” when more and more information is revealed. Dealing 
with this dynamic decision process calls for an appropriate framework which 
is discussed in chapters 10 and 11. 
6.2 
NUMERICAL METHODS FOR UNCONSTRAINED 
OPTIMIZATION 
In principle, an unconstrained problem minxcp f(x) may be solved by look- 
ing for a stationary point. Some care is needed for the non-convex case, 
since second-order information should be checked; furthermore, what we get 
in general is a local optimizer; indeed, almost all the non-linear programming 
libraries commercially available are aimed at local optimization. The station- 
arity condition yields a set of non-linear equations which could be solved to 
spot candidate optima; in fact, there are a few links between unconstrained 
optimization and the numerical solution of non-linear equations. 
In optimization, one avoids direct solution of the non-linear equations. The 
computational approaches are generally based on the generation of a sequence 
of points x(’), converging to a local optimum x*. In order to drive the search 
process in the right direction, one should find, for each point x ( ~ )  
in the 
sequence, a descent direction, i.e., a vector s ( ~ )  
E Rn such that 
for some (u > 0. If we consider the function h((u) = f(x + (us), a descent 
direction is characterized by 
dhl 
= [Vf(x)]’s < 0. 
a = O  

NUMERICAL METHODS FOR UNCONSTRAINED OPTIMIZATION 
339 
It may be convenient to consider true direction vectors, i.e., unit norm vectors 
such that 11 s 1) = 1. A general iteration scheme is, after initialization with a 
starting guess x(O): 
1. Find a descent direction ~ ( ~ 1 .  
2. Find a step length a(k) 
E R+. 
3. Update ~ ( ~ + l )  
= ~
(
~
1
 
+ a ( k ) ~ ( ~ ) .  
The scheme is iterated until some convergence criterion is met. There are 
a variety of choices, which lead to different algorithms, some of which are 
briefly outlined in the following. It should be noted that this approach can 
be extended to deal with constrained optimization problems. An easy case is 
when we have to solve 
min f(x). 
XEW; 
Here it is sufficient to slightly modify the updating rule as follows: 
which should be interpreted componentwise; if some component becomes neg- 
ative, set it at zero. This operation essentially amounts to projecting x ( ~ + ~ )  
onto the feasible set RT (projection can be exploited for more general feasible 
sets, with computational difficulties depending on their nature). 
6.2.1 Steepest descent method 
One seemingly obvious choice for the descent direction is 
which yields the steepest descent or gradient method. The step length Q may 
be chosen by solving the one-dimensional problem 
This one-dimensional problem is easier than the original problem, as it is a 
scalar optimization problem. It can be solved by a variety of line search meth- 
ods. One possibility, which works for convex functions, is using a quadratic 
fit. Assume that we have three points 0 5 a1 < a2 < a3, such that 
h(a1) > h(a2), 
h(ff2) < h(a3). 
An initial set of points satisfying these conditions can be found by some search 
procedure. Now we may fit a quadratic curve passing through the three points; 

340 
CONVEX OPTIMIZATION 
t“ 
X, 
Fig. 6.3 Zig-zagging in the steepest descent procedure 
rninimization of the quadratic curve is easily accomplished, under convexity 
assumption, by setting its derivative to zero. This yields another point, a*. 
Assume that N* > 0 2 .  If h(cu*) 2 h(az), we proceed with the new set of 
points (all 
LYZ, N*); otherwise, we proceed with (QZ, a*, 0 3 ) .  Actually, there 
is a rich set of line search methods, involving, e.g., cubic interpolation and 
other tricks of the trade; some may be selected by setting MATLAB option 
parameters. 
Despite its apparent, appeal, the steepest descent method may suffer from 
poor convergence near the minimizer. In some cases, pathological behavior 
called “zig-zagging” is observed. The zig-zagging phenomenon is illustrated 
in figure G.3.4 Furthermore, roundoff errors may make the straightforward 
steepest descent method rather unreliable. 
6.2.2 
The subgradient method 
It is obvious that the gradient method cannot be applied to a non-differentiable 
function. In supplement 56.1.1 we note that the subgradient is a geiier a 1‘ iza- 
tion of the gradient concept to the case of non-smooth functions. Hence, 
assanling we can compute a subgradient +’) 
for a convex function f at any 
point x(‘), we may wonder if a scheme like 
could work. The answer is not easy, since there is no guarantee that by chang- 
ing the sign of the subgradient we find a descent direction. However, if some 
condition is enforced on the step lengths dk), 
it can be shown that the sub- 
gradient, method converges to the optimal solution. An intuitive justification 
runs as follows. 
4The purpost. of the figure is just to illustrate the phenomenon, as the angles between 
successive segments are not necessarily realistic. To really see zig-zagging, the reader is 
urged to try the optimization toolbox demos. Just type demo, which opens a window 
in which you should select the Optimization toolbox. Then try the “minimization of the 
hanaila. function” demo. 

NUMERICAL METHODS FOR UNCONSTRAINED OPTIMIZATION 
341 
Consider a point xo and let yo be a subgradient of f at XO. Then, by 
definition of a subgradient: 
f(x) L f(x0) + rbb - xo) 
h. 
By applying this inequality to the optimal solution x* and rearranging, we 
obtain 
-rb(x* - xo) L f(x0) - f(x*) 2 0. 
Note that the vector x* - xo is the direction along which we should move 
to reach the optimal solution from XO. The inequality above shows that this 
vector forms an angle less than 90 degrees with -yo. Hence, the subgradient, 
changed in sign, need not be a descent direction, but at least it points to the 
“right” half-space, where the optimal solution lies. 
6.2.3 
The convergence problems in the gradient method are essentially due to the 
fact that the gradient method uses a first-order local approximation of f 
ignoring curvature information. The situation could be improved by using a 
second-order approximation, for a displacement vector 6: 
Newton and the trust region methods 
1 
2 
f(x + 6 )  M f(x) + [V f (x)]’S + -6’H(x)6, 
where H is the Hessian matrix. If H is positive definite, the function is locally 
strictly convex and we may find a minimizer for the quadratic approximation 
by solving the system of linear equations 
H ( x ) ~  
= -Vf(x). 
This method is known as Newton’s method (for optimization) and it has better 
convergence properties as well as higher computational costs. However, we 
are in trouble if the Hessian is not positive definite. 
Another approach is to restrict the step a taken along the direction given 
by the gradient. The rationale is that the first-order approximation is valid 
only in a neighborhood of the current iterate x(’). To find the displacement 
6, we could consider the restricted minimization subproblem: 
s.t. 
11611< h(”. 
Exploiting this idea leads to trust region methods, which are actually used 
in MATLAB for large-scale problems. The trust region is delimited by the 
parameter h(k), which controls the step length and should be adjusted dynam- 
ically. We may compare the predicted improvement in the objective function 

342 
CONVEX OPTIMIZATION 
(according to the approximating function) with the actual improvement. A 
large difference suggests that the approximation is not reliable and that the 
step length should be reduced. Otherwise, the step length can be increased. 
6.2.4 
No-derivatives algorithms: quasi-Newton method and simplex 
search 
One problem with Newton’s method is that the Hessian matrix is required. 
Since providing the software with this information requires a good deal of 
error-prone work, alternative approaches have been developed in order to 
approximate this matrix based on function evaluations only. This leads to 
quasi-Newton methods, which we have already met in the case of non-linear 
equations (see example 3.25 on page 201). The same observation applies to 
providing the gradient of the objective function. As we have seen in chapter 
5, one idea is to approximate the gradient by finite differences like 
N f(2 + hili) - f(2) 
%1,=* - 
hi 
or 
f(2 + hili) - f(2 - hili) 
aft,,/ 
dxi 
x=f = 
2hi 
9 
where l i  is the ith unit vector. By the same token, we may devise suitable 
approximations of the Hessian matrix. 
In some circumstances, you would not be able to compute the gradient any- 
way; one case is when the objective function is not known, but it is implicitly 
computed by a simulation model; another one is when there are discontinuities 
in the objective function. In such cases, it is useful to adopt methods that 
rely only on function evaluations. One such approach is the simplex search 
method developed by Nelder and Mead.5 The rationale behind the method 
is illustrated in figure 6.4 for a minimization problem in R2. A simplex in Rn 
In two dimensions, a simplex is simply a triangle, whereas in three dimen- 
sions it is a tetrahedron. The simplex search method works by building and 
transforming a set of n + 1 points rather than generating a sequence of single 
points; the point with the worst value of the objective is spotted and replaced 
by another point. For instance, consider the three vertices of the triangle in 
figure 6.4 and assume that f(x3) is the worst objective value; then it seems 
reasonable to move away from x3 by reflecting it through the center of the 
is the convex hull of a set of n + 1 affinely independent points XI, . . . , xn+l. 
6 
5This method should not be confused with the celebrated simplex method for linear pro- 
gramming. 
6Affine independence here means that the vectors (x2 - xi), . . . , (xn+l - xi) are linearly 
independent. For TI = 2 this means that the three points do not lie on the same line. For 
n = 3 this means that the four points do not lie on the same plane. 

NUMERICAL METHODS FOR UNCONSTRAINED OPTIMIZATION 
343 
t .
Fig. 6.4 
cediire. 
Rcflcctioii of the worst value Imirit iri the Nelder-Mead simplex search pro- 
face formed by the other points. This is easily accomplished algebraically. 
Assume that x,,+1 is the worst point; then we compute the centroid of the 
best 11 points as 
1 
I' 
c = - E x , ,  
n 
a=1 
and we try a new point of the form 
x, = c + a(c - x,+1). 
The reflection coefficient a > 0 is adjusted depending on the circumstances. If 
x, turns out to be even worse than x,,+l, we may argue that the step was too 
lorig, and the siniplex should be contracted. If x,. turns out to be the new best 
point, we have fouiicl a good direction and the simplex should be expanded. 
Difftwnt tricks have lieen devised in order to improve the convergence of the 
method. 
6.2.5 
Unconstrained optimization in MATLAB 
Consider the unconstrained optimization problem 
niiiif(z1,22) = ( 2 1  - q4 + ( 2 1  - 2 ~ 2 ) ~ .  
Clearly, f ( ~ 1 ,  
x 2 )  2 0 and f ( 2 , l )  = 0; hence (2,l) is a globally optimal 
solution. The gradient off is given by 
It is casy to see that Vf(2,l) = 0. 
uiicoiist,raineci optimization: 
In the Optimization toolbox we have two functions that can be used for 

344 
CONVEX OPTIMIZATION 
fminsearch, which implements a variant of the simplex search method. 
0 fminunc, which actually implements a variety of methods, which are 
selected according to a set of options controlled by the user. 
Both functions require an M-file, a function handle, or an inline function to 
evaluate the objective, and an initial estimate of the solution. An optional 
parameter may be used to set the desired options through the optimset func- 
tion. 
Let us first try the simplex search procedure, giving an initial estimate 
xo = 0: 
>> f = Q(x) (~(1) - 21-4 + (~(1) - 2 * ~(2))-2; 
>> x=fminsearch(f, [O 01) 
2.0000 
1.0000 
x =  
>> f(x) 
ans = 
2.9563e-017 
>> 
Now we may try fminunc: 
>> x=fminunc(f , [O 01 ) 
Warning: Gradient must be provided for trust-region method; 
Optimization terminated: relative infinity-norm of gradient less 
using line-search method instead. 
than options.TolFun. 
1.9897 
0.9948 
x =  
>> f(x) 
ans = 
1.1274e-008 
The result is not exact really. The point is that the function is rather “flat” 
around the minimizer; in fact the objective function is close to zero in the 
solution reported by MATLAB. We could change the tolerance parameters 
in order to improve the solution, but this could make no sense in practice. 
We may also note that MATLAB complains about the lack of gradient in- 
formation, so that it cannot apply a trust region method. This is not much 
trouble, as the gradient may be estimated numerically. However, we could 
ask MATLAB not to use the default “large-scale” algorithm, which is a trust 
region method, but a “medium-scale” algorithm. 
>> options=optimset(’largescale’ , ’off I )  ; 
x=fminunc(f, [O 01, options) 
Optimization terminated: relative infinity-norm of gradient less 
than options.TolFun. 
x =  

N UM ERICA L ME TH ODs FOR UN CONSTRAINED OPTIMIZA TION 
345 
1.9897 
0.9948 
Alternatively, we may provide a function to compute the gradient and tell 
MATLAB to use it within a large-scale algorithm, possibly with a stricter 
tolerance: 
>> f = @(XI 
( ~ ( 1 )  
- 21-4 + ( ~ ( 1 )  
- 2 * ~(2))-2; 
>> gradf = @(x) 
[4*(~(1)-2)-3+2*(~(1)-2*~(2)) , -4*(~(1)-2*~(2))] 
; 
>> options=optimset(’gradobj’,’on’, 
’largescale’,’on’, ’tolfunJ,le-13); 
>> x=fminunc((f, 
gradf), 
[O 01, options) 
Optimization terminated: relative function value changing by less 
than 0PTIONS.TolFun. 
1.9997 
0.9998 
x =  
Computing a gradient analytically is clearly an error-prone activity. To help 
with this task, it is possible to ask MATLAB to compare the gradient we 
provide with a numerical estimate. All we have to do is to reset the options and 
to set the derivativecheck option om7 Here we may try this functionality, 
providing MATLAB with an incorrect expression for the gradient implemented 
in the function gradf I: 
>> options = optimset; 
>> options=optimset(’gradobj’, ’on’, ’largescale’, ’off’, ... 
’derivativecheck’, ’on’) ; 
>> gradfl = @(x) [S*(x(l)-2)’3+2*(~(1)-2*~(2)) , -4*(x(1)-2*x(2))1 ; 
>> x=fminunc({f, gradf 11, [O 01, options) 
Maximum discrepancy between derivatives = 16 
Warning: Derivatives do not match within tolerance 
Derivative from finite difference calculation: 
-32.0000 
0 
User-supplied derivative, 
@(XI 
[6* (~(1) -2) -3+2*(~(1)-2*~(2)) , -4* (~(1) -2*x(2) 11 : 
-48 
0 
Difference: 
-16.0000 
0 
Strike any key to continue or Ctrl-C to abort 
Optimization terminated: 
relative infinity-norm of gradient less than options.TolFun. 
x =  
1.9841 
0.9921 
Indeed, we see that a warning is issued by the system, spotting a likely trouble 
with our analytical gradient. 
7See also the code displayed in figure 3.28 on page 202. 

346 
CONVEX OPTIMIZATION 
6.3 
METHODS FOR CONSTRAINED OPTIMIZATION 
Consider a general constrained optimization problem, such as 
min 
f(x) 
s.t. 
hi(x) = 0 
i E E 
i E I. 
gz(x) 5 0 
In this section we assume that all the involved functions have suitable differen- 
tiability properties. For a constrained problem, stationarity is not a necessary 
condition anymore, since the optimal solution may be a non-stationary point 
on the boundary of the feasible set (this means that there are descent direc- 
tions, but they all lead outside the feasible region). One possible approach to 
cope with this difficulty is trying to transform the problem in such a way that 
stationarity condition may be applied again; this leads to the penalty func- 
tion approach (section 6.3.1). Another idea is to develop optimality conditions 
which include some form of stationarity, plus some additional requirements; 
this leads to the Kuhn-Tucker conditions (section 6.3.2). Kuhn-Tucker con- 
ditions generalize the Lagrange multiplier method for equality-constrained 
problems, and they are linked to a body of optimization theory called duality 
theory (section 6.3.3), which leads both to theoretical insights and to practical 
algorithms. Another important observation is that a constrained problem is 
relatively easy when all the involved function are affine; indeed, linear pro- 
gramming is a very well developed branch of optimization theory (section 
6.4). So it may be interesting to develop algorithms which somehow trans- 
form a non-linear problem to a linear problem. This may be accomplished 
easily if the constraints are linear and the objective function is convex; Kel- 
ley’s cutting planes algorithm (section 6.3.4) is based on this idea, and it is 
the conceptual basis of some methods for stochastic problems. In general, it 
is reasonable to assume that a linearly constrained problem has some specific 
features that may be exploited in a computational algorithm. The active set 
method (section 6.3.5) is one such strategy; it also worth noting that, in the 
earlier versions of the Optimization toolbox, the active set method was the 
basis of the functions for both linear and quadratic programming. 
Due to its introductory nature, this book has been written sacrificing the 
mathematical rigor. This is particularly true for this chapter, as optimization 
theory is a tough subject in which simplistic approaches may lead to disasters. 
Hence, the serious reader is urged not to take what we illustrate in the follow- 
ing as a foolproof set of recipes; it is a good starting point, but the references 
at the end of the chapter should be consulted for a more thorough treatment. 
6.3.1 
Penalty function approach 
Penalty functions are based on the idea of relaxing constraints through the 
addition of a suitable term to the objective function. Consider a problem with 

METHODS FOR CONSTRAINED OPTIMIZATION 
347 
equality constraints: 
min 
f(x) 
s.t. 
hi(x) = 0, 
i E E. 
It is possible to approximate this constrained problem by the unconstrained 
one 
min@(x, u) = f(x) + u 
hT(x). 
~ 
iEE 
This function penalizes both positive and negative values of hi. If u is large 
enough, the optimization algorithm will, in some sense, first drive the solution 
toward the feasible region by minimizing the penalty term; then it will try to 
minimize the objective f. Actually, convergence difficulties will arise if we try 
solving the unconstrained problem with a large value of the penalty coefficient 
u. So it is advisable to solve a sequence of unconstrained problems using the 
optimal solution of each subproblem as the initial solution of the next one: 
1. Choose a sequence {dk)} 
-+ 00. 
2. Find the minimizer x*(dk)) 
of @(x, a). 
3. Stop if hi(x*) is sufficiently small for all i. 
We can see this as an example of a continuation strategy (see section 3.4.5). 
The case of inequality constraints 
min 
f(x) 
s.t. 
gi(x) 5 0 
i E 1. 
can be tackled by a similar approach. In this case, however, we must only 
penalize positive values of the constraint functions gi. Using the notation 
[y]+ = max{y, 0}, we may use a penalty function like 
or 
for increasing values of 0. The first penalty function is differentiable, whereas 
the second one is not, as you may see in figure 6.5a; however, the second 
function may be advantageous from the numerical point of view, as there is 
no need to use too large values of the penalty coefficients. Indeed, one of the 
driving forces behind the development of non-smooth optimization algorithms 
was the use of exact penalty functions. 
In both cases, we are actually using an exterior penalty function. The 
name stems from the fact that the feasible set is approached from outside for 

348 
CONVEX OPTlMlZATlON 
o increasing 
S 
o decrcasine Ill 
(b) 
Fig. 6.5 Exlcrior (a) and interior (b) penalties. 

METHODS FOR CONSTRAINED OPTIMIZATION 
349 
increasing values of CJ, as illustrated in figure 6.5a. If the optimal solution 
is on the boundary of the feasible set (which is usually the case, since some 
inequality constraints are active), a feasible solution is obtained only in the 
limit. In some cases, this is quite natural, as the constraints may be soft or 
“elastic” and express some desirable feature rather than a hard requirement. 
In other cases, we would like to be able to stop the algorithm whenever we want 
and still come up with a strictly feasible solution. To overcome this problem, 
an interior penalty approach can be pursued, by introducing a suitable barrier 
function. One example is 
The barrier function goes to infinity when x tends to the boundary of the 
feasible region from inside. Then an unconstrained problem, 
rninf(x) + aB(x), 
is solved for decreasing values of CJ, until the term aB(x) is small enough. 
As shown in figure 6.5b, in this case we approach the optimal solution on 
the boundary staying within the feasible region; this may be an advantage, 
provided that we have a way to start the iterations with a feasible point. 
From figure 6.5 it should also be clear that both exterior and interior penalty 
functions are numerically feasible ways of approximating the ideal penalty: 
gi(x) I0 
{ ”+, 
gi(x) > 0. 
Pa(.) 
= 
Example 6.5 Consider the problem 
min 
s.t. 
2, y 5 1, 
(x - 1.5)’ + ( y  - 0.5)’ 
whose optimal solution is clearly x* = 1, y* = 0.5. An interior penalty 
function could be 
0 
I7 
(2 - 1.5)’ + ( y  - 0.5)’ + - 
+ - 
1 - 2  
1 - y  
Using MATLAB graphics, we may easily plot the level curves of the penalty 
function for different values of the parameter 0. We need to define a function 
and to use the functions meshgrid, to define the grid of points on which we 
want to evaluate the function, and contour, to plot a set of level curves. 
>> f=@(sigma,x,y) (~-~.5).^2+(y-0.5).^2+sigma./(I-x)+sigma./(l-y); 
>> [x y] = meshgrid(0.01 : 0.01 : 0.99); 
>> subplot (2,2, 
I) 
>> contour(f (O.i,x,y) ,301 

350 
CONVEX OPTIMIZATION 
80 
80 
60 
60 
40 
40 
20 
20 
20 
40 
60 
80 
20 
40 
60 
80 
80 
80 
60 
60 
40 
40 
20 
20 
20 
40 
60 
80 
20 
40 
60 
80 
fig. 6.6 Plots of the level curves for the interior penalty function of example 6.5 for 
u = 0.1, u = 0.01, u = 0.001, u = 0.0001. 

METHODS FOR CONSTRAINED OPTIMIZATION 
351 
>> subplot(2,2,2) 
>> contour(f (O.Ol,x,y) ,301 
>> subplot (2,2,3) 
>> contour(f (O.OOI,x,y) ,301 
>> subplot (2,2 , 4) 
>> contour(f (O.OOOl,x,y) ,301 
The three plots are shown in figure 6.6. We see that the optimal solution of 
the unconstrained problem tends to the optimal solution of the original one 
from the inside. 
0 
The penalty function approach is conceptually very simple, and some con- 
vergence properties can be proved. However, severe numerical difficulties may 
arise, for instance, when u gets very large in the case of an exterior penalty. 
Nevertheless, penalty functions are most useful in providing a starting point 
for other, more sophisticated methods. They may be integrated with the La- 
grangian methods described below, giving rise to the augmented Lagrangian 
methods, and they are one of the ingredients of the increasingly popular inte- 
rior point methods for linear programming. 
6.3.2 
Kuhn-Tucker conditions 
Consider a general constrained problem ( PEI): 
min 
f ( x )  
s.t. 
hi(.) 
= 0, 
i E E 
i E I. 
gi(x) 5 0, 
The stationarity of f plays no role in proving optimality here, but the sta- 
tionarity of a related function does. Consider the Lagrangian function 
The stationarity of C does play a role in the following conditions. 
THEOREM 6.5 (Kuhn-Tucker conditions) Assume that the functions 
f, hi,gi in (PEI) are continuously differentiable, and that x* is feasible and 
satisfies a constraint qualification condition. Then a necessary condition for 
the local optimality of X *  is that there exist numbers A t  (i E E )  and & 2 
0 (i E I )  such that 
iEE 
i E I  
pfgi(x*) = 0 
Vi E I. 

352 
CONVEX OPTIMIZATION 
The first condition is the stationarity of the Lagrangian function; if the 
set of inequality constraints is empty, these conditions boil down to the older 
Lagrange method to deal with equality-constrained problems. The numbers X i  
and pi are called Lagrange multipliers; note that the multipliers for inequality 
constraints are restricted in sign. For reasons that will be clear in the next 
section, the multipliers are also called dual variables (as opposed to the primal 
variables x). The Kuhn-Tucker conditions are, in a sense, rather weak, as they 
are only necessary conditions for local optimality, and they further require 
differentiability properties and some additional qualification condition on the 
constraints (to be clarified in example 6.7). They are, however, necessary and 
sufficient for global optimality in the convex case. 
Example 6.6 As a first example, we may solve the optimization problem we 
have considered in example 2.3, on page 37. It is a non-linear programming 
problem with one equality constraint: 
max 
x~x;-* 
s.t. 
P I X 1  f p z x z  = w. 
We introduce a Lagrange multiplier X and build the Lagrangian function: 
LI 1-LI 
C(Xl,X2rX) = 
+ ( P l X l  +P2XZ - W )  . 
Since there is no inequality, we have just to write first-order optimality con- 
ditions: 
dC - 
dX = p l x l  +pzx2 - w = 0. 
Dividing the first two equations term by term, after a rearrangement, we get 
From the budget equation we may get 2 2 :  
w - P l X l  
x2 = 
7 
P2 
which may be substituted in (6.4): 
( 1  - Q ) P l X l  - a (W - PlXl) = 0, 

ME TH ODs FOR CONSTRAIN ED OPTIMIZATIO N 
353 
We see that consumption of each good is inversely proportional to its price, 
0 
and it depends on the preference parameter a. 
We will not prove the Kuhn-Tucker conditions, as a rigorous proof is be- 
yond the scope of the book; informally, they can be derived by characterizing 
a local optimum as a point such that an improvement in the objective function 
can only be obtained by going outside the feasible region. It is worth noting 
that the stationarity condition says that the gradient of the objective function 
can be expressed as a linear combination of the gradients of the objectives; 
this clarifies a little what we mean by constraint qualification; if the gradients 
of the constraints are not linearly independent at XI, it might be the case 
that we cannot use them as a basis to express Of. 
So it may happen that the 
Kuhn-Tucker conditions are not satisfied by a point that is actually a local 
minimizer. 
Example 6.7 To understand the issue behind the constraint qualification 
condition, consider the problem: 
min 
X I  f x z  
s.t. 
3 
h l ( X )  = 2 2  - XI = 0 
h 2 ( X )  = 2 2  = 0. 
It is easy to see that the feasible set is the single point (O,O), which is the 
(trivial) optimal solution. If we try applying the Kuhn-Tucker conditions, we 
first build the Lagrangian function 
C ( X l , X Z ,  X1, X2) = 2 1  + x 2  + Xl(X2 - x;) + x 2 x z .  
Writing the stationarity yields the system 
- = 2 2  = 0, 
ac 
8 x 2  
which has no solution (the first equation requires that x 1  # 0, which is not 
compatible with the last two equations). This is due to the fact that the 
gradients of the two constraints are parallel at the origin: 

354 
CONVEX OPTIMIZATION 
and they are not a basis able to express the gradient of f 
Different constraint qualification conditions have been proposed in the lit- 
erature. Sufficient conditions to avoid trouble are that the gradients of the 
active constraints are linearly independent, or that the constraints are all lin- 
ear. We will not pursue this issue any further, but we recommend a book like 
[18] as a warning against easy cookbook recipes in optimization. 
The Kuhn-Tucker theorem also includes a second set of conditions, which 
are known as complementary slackness conditions. They may be interpreted 
by noting that if a constraint is inactive at x*, i.e., if gi(x*) < 0, the corre- 
sponding multiplier must be zero; by the same token, if the multiplier p: is 
strictly positive, the corresponding constraints must be active (which roughly 
means that it could be substituted by an equality constraint without chang- 
ing the optimal solution). The complementary slackness conditions could be 
used, in principle, to find a feasible point and a set of multipliers satisfying 
the Kuhn-Tucker conditions. 
Example 6.8 Consider the convex problem 
s.t. 
21 2 0 
5 2  2 3 
21 + 2 2  = 4. 
First write the Lagrangian function: 
A set of numbers satisfying the Kuhn-Tucker conditions can be found by 
solving the following system: 
2x1 - p1+ x = 0 
2x2 - p2 + x = 0 
21 2 0, 
21 + x2 = 4 
1-1121 =o, 
1-11 LO 
PZ(Q - 3) = 0, 
x2 2 3 
1-12 2 0. 
We may proceed with a case-by-case analysis exploiting the complementary 
slackness conditions. If a multiplier is strictly positive, the corresponding 
inequality is active, which helps us in finding the value of a decision variable. 

METHODS FOR CONSTRAINED OPTIMIZATION 
355 
Case 1 (p1 = p~ = 0). In this case, the inequality constraints are dropped 
from the Lagrangian function. From the stationarity conditions we ob- 
tain the system 
2x1 + x = 0 
2x2 + x = 0 
2 1  + 22 - 4 = 0. 
This yields a solution XI = x2 = 2, which violates the second inequality 
constraint. 
Case 2 ( P I ,  p~ # 0). The complementary slackness conditions immediately 
Case 3 (p1 # 0, p2 = 0). We obtain 
yield x1 = O,x2 = 3, violating the equality constraint. 
21 = 0 
x2 = 4 
X = - 2 ~ 2  = -8 
111 = X = -8. 
The Kuhn-Tucker conditions are not satisfied since the value of p1 is 
negative. 
Case 4 (p1 = 0, 
p2 # 0). We obtain 
x2 = 3 
x1 = 1 
x = -2 
p2 = 4, 
which satisfy all the necessary conditions. 
Since this is a convex problem, we have obtained the global optimum. Note 
how non-zero multipliers correspond to the active constraints, whereas the 
inactive constraint 21 2 0 is associated to a multiplier p1 = 0. The same 
result can easily be obtained through MATLAB. The quadprog function deals 
with quadratic programming problems such as 
1 
min 
-x’Hx + f’x 
2 
s.t. 
Ax 5 b 
AeqX = beq 
l < X < U .  
For our example, some entries of the problem are empty. Note also that 
simple bounds are treated apart in practice and that the quadratic term in 

356 
CONVEX OPTIMIZATION 
the objective function must be written in a specific way, as it involves a 1 / 2  
factor and it assumes a symmetric Hessian matrix H. 
>> H = 2*eye(2) ; 
>> Aeq = Cl 11; 
>> beq = 4; 
>> lb = LO; 31; 
>> options=optimset( 'Largescale', 'off '1 ; 
>> [x,fval,exitflag,output,lambda] = quadprog(H,f, [I, [I ,Aeq,beq, . 
Optimization terminated. 
>> x 
>> f = ro 01; 
lb, [I , [I ,options) ; 
X' 
1.0000 
3.0000 
>> 1ambda.eqlin 
ans = 
-2.0000 
>> 1ambda.lower 
ans = 
0 
4.0000 
.. 
The output arguments include the optimal decision variables, the optimal 
value of the objective function, an exit flag containing information about the 
termination of the algorithm, additional output information, and the mul- 
tipliers included in the structure lambda. The multipliers in our case are 
associated to the linear equalities and to the lower bounds on the decision 
variables. 
0. 
Clearly, the approach we have taken in the example is not practical. Some 
alternative way must be found to spot the optimal multipliers. This leads to 
duality theory, which is the topic of next section. Before proceeding, it is also 
useful to get an intuitive grasp of the meaning of the Lagrange multipliers. 
Example 6.9 Consider the parameterized problem 
min 
2; +x; 
s.t. 
2 1  + 22 = b. 
The stationarity conditions on the Lagrangian function, 
C ( ~ i , 2 2 ,  
A) = 2: + 2; + X ( Z ~  + 2 2  - b), 
immediately yield xr = x; = b/2 and A* = -b. Now, ask how slight changes 
in the parameter b will affect the optimal value f* = b2/2: 

METHODS FOR CONSTRAINED OPTIMIZATION 
357 
This suggests that, neglecting the sign, the dual variables are linked to the 
sensitivity of the optimal value with respect to perturbations in the right hand 
side of the constraints. 
0 
The intuition suggested by the example is correct, provided we assume 
that the derivative makes sense. Consider an equality-constrained problem 
and apply a small perturbation to the constraints 
hi(X) = €i, 
i E E. 
Applying the Lagrangian approach to the perturbed problem, we get a new 
solution x * ( E )  and a new multiplier vector A*(€), both depending on E .  The 
Lagrangian function for the perturbed problem is 
C(X, A, E )  = f(x) + C Xi(hi(x) - ~ i ) .  
(6.5) 
iEE 
Equality constraints must be satisfied by the optimal solution of the perturbed 
problem. Hence: 
f *  = f(X*(€)) = C(X*(E), 
A*(€), E). 
(6.6) 
We can evaluate the derivative of the optimal value with respect to each 
component of E ,  
Y 
=O 
where we have used the stationarity condition of C. As to inequality con- 
straints, they are either inactive or active in x*: in the first case, they play 
no role for small enough perturbations; in the second one, they essentially act 
as equality constraints. It may be tempting to conclude that if a constraint is 
associated to a null multiplier, then it can be dropped without changing the 
optimal solution. The counterexample shown in figure 6.7 shows that this is 
not the case. Here we have a convex quadratic objective, to which the two 
concentric level curves are associated; the feasible region is the portion of the 
“bean” S below the constraint g(x) I 0, which is actually an upper bound 
on 52. The optimal solution is the point A, and the constraint g(x) 5 0 is 
inactive at that point; however, if we eliminate the constraint, the optimal 
solution is B (it remains true that A is a locally optimal solution). The issue 
here is that the overall problem is not convex. 
6.3.3 
Duality theory 
In preceding sections we have shown that the stationarity of the Lagrangian 
function plays a crucial role in constrained optimization. Stationarity is linked 

358 
CONVEX OPTIMIZATION 
t x2 
S 
ecreasing 
I 
X. 
Fig. 6.7 Coiinterexaniple showing that a constraint may be relevant even if it has it 
null mi ilt iplier . 
to an optimalitmy condition for either minimization or maximization. It is 
rather intuitive that we should minimize the Lagrangian function with re- 
spect to the primal variables, but what about the dual variables? This is an 
important point if’ we want to devise a numerical way to find optimal values 
for both the primal and dual variables. In this section we show that inter- 
cst,ing results are obtained by maxcimizing a dual function with respect to the 
dual variables: leading to duality theory. 
Consider the inequalitmy-constrained problem 
( P )  
niin 
f(x) 
s.t. 
gz(x) 5 0 
2 E z 
(6.8) 
x E s c W”. 
This problem is called the primal problem. Note that the set S is any subset 
of W”: possibly a discrete one; furthermore, in this section we do not assume 
the differentiability nor the convexity of the objective function. The results 
we get are therefore extremely general. 
Consider the Lagrangian function obtained by dualizing constraints (6.8): 
a x ,  P )  = f(x) + c Pigi.(x). 
i E I  
For a given multiplier vector p, the minimization of the Lagrangian function 
with respect to x E S is called the relaxed problem; the solution of the relaxed 
problem defines a function ui(p), called the dual function: 
Consider the d ~ d  
problem,: 
( D )  
w(p) = minC(x, p). 
XES 
maxw(p) = max 
(6.9) 
PLLO 

METHODS FOR CONSTRAIN ED OPTIMIZATION 
359 
The following theorem holds. 
THEOREM 6.6 (Weak duality theorem) For any p 2 0, the dual func- 
tion is a lower bound for the optimum f (x*) of the primal problem ( P ) ,  i.e., 
W ( P )  i fb*) 
v p  2 0. 
Proof. Let us adopt the notation v(P) to denote the optimal value of the 
objective function for an optimization problem P. Under the hypothesis p 2 
0, it is easy to see that 
(6.10) 
(6.11) 
1 
min 
f(x) 
v(P) 2 
v 
s.t. 
xE s 
dg(x) 5 0 
min 
f(x) + p’g(x) 
( 
2 v ( s . t .  
X € S  
p’g(x) 5 0  
(6.12) 
Inequality (6.10) is justified by the fact that the points satisfying the set of 
constraints gi(x) 5 0, for all i, also satisfy the aggregate constraint p’g(x) 5 0 
if p 2 0, but not vice versa. In other words, the feasible set of the first problem 
is a subset of the feasible set of the second one. Clearly, when we relax the 
feasible set, the optimal value cannot increase. Inequality (6.11) holds since 
the third problem involves the same feasible set as the second problem, but we 
have added a non-positive term to the objective function. Finally, inequality 
(6.12) holds since the fourth problem is a relaxation of the third one (we delete 
a constraint). 
0 
We obtain a very general but weak relationship. Under suitable conditions 
(essentially convexity) , a stronger property holds, known as strong duality: 
v(D) = w(p*) = f(x*) = v(P). 
The convexity assumption does not hold, in particular, for the case of a dis- 
crete set; therefore, in general, duality yields only a lower bound for discrete 
optimization problems. The following theorem is useful in establishing when 
the dual problem yields an optimal solution of the primal problem. 
THEOREM 6.7 If there is a pair (x*,p*), 
where x* E S and p* 2 0, 
satisfying the following conditions: 
1. fb*) + (p*)’g(x*) 
= minxEs{f(x) + (P*)’g(x)l; 
2. (p*)’g(x*) 
= 0; 

360 
CONVEX OPTIMIZATION 
3. g(x*) 5 0; 
then x* is a global optimum for the primal problem (P). 
In other words, the optimal solution x* of the relaxed problem for a multi- 
plier vector p* is a global optimum for the primal problem if the pair (x*, p*) 
is primal feasible, dual feasible, and it satisfies the complementary slackness 
conditions. Note that these are suficient conditions for global optimality. 
Weak duality also holds in the equality-constrained case. Consider the 
optimal solution X* of the primal problem: 
min 
f ( x )  
s.t. 
hi(.) 
= 0, 
i E E 
x E s, 
and the optimal solution % of the relaxed problem: 
min { f ( x )  + X'h(x)} . 
XES 
For any multiplier vector X (not restricted in sign), it is easy to see that 
f(X) + X'h(%) 5 f(x*) + X'h(x*) = f(x*). 
Unfortunately, convexity does not hold easily for equality constraints. In fact, 
it holds only for linear equality constraints such as al,x = bi. Hence, strong 
duality with equality constraints holds only in specific cases; a very important 
one is linear programming (see section 6.4.3). 
Example 6.10 Consider the problem 
min 
x f + x z  
s.t. 
21 + 2 2  2 4 
z1,22 2 0. 
The optimal value is 8, corresponding to the optimal solution (2,2). Since 
this is a convex problem, we can apply strong duality. The dual function is 
w(p) = :;Ip: 
+ 2; + p(-s1 - 2 2  + 4); s.t. 21, 
2 2  2 0) 
= min{z: - pzl; s.t. 21 2 0) + min{zi - pzz; s.t. 22 2 0) + 4p. 
x1 
x2 
Since ,LL 2 0, the optima with respect to XI, 
22 are obtained for 
Hence, 
1 
w(p) = --p2 
2 + 4p. 

METHODS FOR CONSTRAINED OPTIMIZATION 
361 
The maximum of the dual function is reached for p* = 4, and we have w(4) = 
f* =8. 
0 
In example 6.10, we have found an explicit representation of the dual func- 
tion. In general, the maximization of the dual function must be tackled by 
a numerical method. In practice, the following iterative procedure can be 
adopted (assuming the inequality-constrained case): 
1. Assign an initial value p(O) 2 0; set k +- 0. 
2. Solve the relaxed problem with multipliers p('). 
3. Given the solution k(k) of the relaxed problem, compute a search di- 
and update the multipliers (making 
rection s ( ~ )  
and a step length 
sure they stay non-negative): 
p(k+l) = max { 0 ,  p(k) + C y ( k ) S ( k ) }  . 
Then set k t 
k + 1, and go to step 2. 
In order to find a search direction, one would be tempted to compute a gra- 
dient of the dual function. Unfortunately, the dual function need not be 
everywhere differentiable, as we can see from the following example. 
Example 6.11 Consider the discrete optimization problem 
min 
c'x 
s.t. 
a'x 2 b 
(6.13) 
(6.14) 
where c, a, x E Rn, b E R and S is a discrete set. Dualizing constraint (6.13) 
with a multiplier p 2 0, we obtain the dual function: 
x E s = {xl,x2,. . . ,xm}, 
w(p) = , min { (b - a'xj)p + c ' d }  . 
j=l, ..., m 
It is easy to see that the dual function is the lower envelope of a family of 
affine functions, as shown in figure 6.8. We have a non-differentiability point 
when the relaxed problem has multiple optimal solutions. 
0 
Rom example 6.11 we may conclude that there is no differentiability guar- 
antee for the dual function; however, the dual function for this case is concave. 
In fact, we may easily prove that the dual function is always concave. 
THEOREM 6.8 The dual function w(p) is a concaue function. 
Proof. We must show that for any multiplier vectors p1 and pz, 
" [ h l  + (1 - X)P21 2 W P 1 )  + (1 - X).w(P2), 
A E [0,1]. 

362 
CONVEX OPTIMIZATION 
Fig. 6.8 Nori-tliffc.reiitiable dual function. 
Let us denote by XI and X z  the optimal solutions of the relaxed subproblems 
with multipliers pl and pz, respectively. We have 
4 P I )  = f @ l )  + P M X d  I 
f b x )  + P M X X )  
7
4
4
 = f F 2 )  + C L M ~ Z )  I f ( x x )  + CLk(xx), 
where xx is the optimal solution corresponding to the multiplier vector Apl + 
(1 - A)pz. The result is obtained by multiplying the first inequality by A, the 
second one by 1 - A, and summing. 
0 
Siiire maximizing a concave function is equivalent to minimizing a convex 
function, this is a reassuring result. In fact, we may apply a subgradient 
algorithm (see section 6.2.2) provided that we are able to find a subgradient 
of the d1d function for any value of the niultipliers. 
THEOREM 6.9 Let x he an optimal solution of the relaxed problem for a 
multiplier vector ji. Then g(2) is a subgradient of the dual function at fi. 
Proof. To show that g(X) E dw(ji), we must show that, for any p, we have 
W ( P )  I 4fi) + g(X)’(p - fi). 
Here the inequality is reversed with respect to the definition of a subgradient 
for a convex function, since w is concave. We know that x is the optimal 
solution of the relaxed problem for C;: 
‘ u I ( j i )  = f (2) + fi’g(Xz) 
(6.15) 
lxit not for a generic p: 
(6.16) 

ME TH 0 DS FOR CONSTRAINED OPTIMIZATION 
363 
Subtracting equation (6.15) from inequality (6.16), we get 
W(P) - W ( P )  I g’(X)(cL - PI1 
and the result follows. 
0 
Theorem 6.9 allows us to solve the dual problem (6.9) by a subgradient 
algorithm. A remarkable point is that we are able to optimize a function, 
even if it is not known in explicit form, provided we know how to find a 
subgradient; this applies to the dual function, which is implicitly defined by 
an optimization problem, and to the recourse function that we will meet in 
stochastic programming (chapter 11). 
In order to maximize the dual function, a sequence of relaxed problems is 
solved, updating the dual variables as follows: 
where X ( k )  is the solution of the kth relaxed problem. Note that this solution 
need not be feasible for the original (primal) problem. Provided that strong 
duality holds, the method converges to the optimal solution of the original 
problem. When only weak duality applies, we obtain a lower bound on the 
optimal value of the primal problem (which may be valuable in itself), and 
probably a near-feasible solution, from which a feasible near-optimal solution 
may be obtained with some problem-dependent procedure. It should be noted 
that duality theory in itself does not generally yield numerically efficient al- 
gorithms directly. Nevertheless, it may be fruitfully exploited for specially 
structured problems; in fact, we have seen in example 6.10 that dualizing cer- 
tain constraints may decompose an optimization problem into independent 
subproblems; certain model formulations lend themselves to a decomposition 
by dualization of the interaction constraints. Furthermore, duality theory 
is a fundamental theoretical tool paving the way for important algorithmic 
developments. 
6.3.4 Kelley’s cutting plane algorithm 
In the last section, we have been able to maximize the dual function, even 
if it is not known in an explicit form. We have relied on the fact that the 
function was concave and we were able to evaluate the function and to find 
a subgradient at a given point. A similar idea leads to Kelley’s cutting plane 
method for the minimization of a convex function. Assume that we have to 
solve a convex problem minxes f(x), where the objective function f is actually 
not known in analytical form. Suppose that, for a given point xk, we are not 
only able to compute the function value f ( x k )  = a k ,  but also a subgradient 
yk, which does exist if the function is convex on the set S. In other words, 
we are able to find an affine function such that 
f(xk) = a k + y : X k  
(6.17) 

364 
CONVEX OPJlMlZATlON 
Fig. 6.9 Example of Kelley’s cutting plane algorithm. 
f(x) 2 TYk:+-/;x 
V X E  s. 
(6.18) 
Thc availability of such a support hyperplane suggests the possibility of ap- 
proximating f from below, by the upper envelope of support hyperplanes, as 
illustrated in figure 6.9. The Kelley’s cutting plane algorithm exploits this idea 
by building and improving a lower bounding function until some convergence 
criterion is met. 
Step 0. Let x1 E S lie an initial feasible solution; initialize the iteration 
counter k + 0, the upper bound ug = f(x’), the lower bound 10 = -35, 
a i d  thc lower bounding function ,&(x) = -m. 
Step 1. Iricreinent the iteration counter k + k + 1. Find a subgradient of f 
at xk, such that equation (6.17) and condition (6.18) hold. 
Step 2. Updatte the upper bouiid 
ant1 the lower l~oiincling function 
Step 3. Solve the problem 
l k  = minpk:(x), 
XES 
and let x’+l he the optimal solution. 
Step 4. If uk - lk < c, stop: xk+l is a satisfactory approximation of the 
optimal solutioii; othcrwise, go to step 1. 

METHODS FOR CONSTRAINED OPTIMIZATION 
365 
It is worth noting that, if the feasible set S is polyhedral, then all the 
subproblems we solve are LP problems. The Kelley's cutting plane algorithm 
is the conceptual basis of some algorithms for stochastic programming, such 
as the L-shaped decomposition for stochastic programming, which will be 
described in section 11.4. 
6.3.5 
Active set method 
Although duality theory is a powerful tool, both in theory and practice, dual 
algorithms have the general drawback that a feasible solution is generally 
obtained only in the limit. A natural aim of many constrained optimization 
algorithms is to stay within the feasible region. This is particularly easy to 
accomplish if the problem is linearly constrained. Consider the problem 
min 
f(x) 
s.t. 
AX = b, 
where the matrix A E Bm,n, m < n, is assumed of full row rank for simplicity. 
Given a feasible solution 12, how can we characterize descent directions 6 such 
that the new solution 12 + a6 remains feasible for some cr > O? Since both 
solutions must be feasible, 
A ( i + c t 6 ) = b + a A S = b  + A 6 = 0 .  
Technically speaking, the vector 6 must lie in the null space of the matrix A; 
since this is a linear space, there must be a basis for it. Let Z E Bnl("-m) be 
a matrix whose columns are a basis for this space; then we have 
AZ = 0, 
and the direction 15 is a linear combination of the columns of Z: 
6 = Zd. 
The basis consists of (n-m) vectors. To see why, consider that the m equality 
constraints eliminate m degrees of freedom for the n decision variables. Then 
we may move in some space with (n - m) degrees of freedom. The first-order 
Taylor expansion for a perturbed point along the feasible direction is 
f (i + eZd) M f (x) + td'Z'V f (x). 
A descent direction is obtained when d'Z'V f (x) < 0; furthermore, the first- 
order necessary optimality condition is 
z'v f (x*) = 0. 
(6.19) 
The vector Z'V f is called the reduced gradient, and we see that a stationarity 
condition must be required for this reduced gradient. By the way, the condi- 
tion (6.19) implies that the gradient Of is a linear combination of the rows 

366 
CONVEX OPTIMIZATION 
of A. This means that 
which could also be obtained by the Lagrange multipliers approach. 
Provided that we are able to find a suitable matrix Z, an algorithm is 
readily devised, as we must simply spot descent directions and select the step 
length a: in order to reduce the objective function while keeping the iterates 
feasible. One possible choice of Z is obtained by exploiting QR factorization. 
This factorization, which is implemented by the qr function in MATLAB, 
allows us to write 
Vf(x*) = A'X, 
A ' = Q  [ t ] = [ QI 
QZ ] [ t ] = QIR, 
where Q E B"1" is an orthogonal matrix (Le., its columns are orthogonal 
vectors), and R E B"jn-" is upper triangular. The choice Z = Q2 satisfies 
our requirements, since the orthogonality of Q implies that 
A = R'Q: + AZ = R'QiQ2 = 0. 
Different choices of Z and different approaches in selecting the descent direc- 
tion and the step length result in a variety of methods which are described 
in the literature. It should also be mentioned that second-order conditions 
should be checked iff is not convex. 
To cope with a 
problem like 
The approach may be extended to linear inequalities. 
min 
f(x) 
s.t. 
Ax 5 b, 
a possible idea is to restrict the attention to the active constraints, i.e., the 
constraints which are satisfied at equality. In principle, if we knew which 
constraints are active in the optimal solution, we could treat the problem like 
an equality-constrained problem. The active set strategy works on a pool of 
active constraints, trying to identify which constraints must be brought in and 
out of the active set. Roughly speaking, if we see that a relaxed constraint 
would get violated by a move along the feasible direction, it should be added to 
the set. Similarly, an inactive constraints can be dropped. The details of the 
method are not so easy, but it is enough to know the qualitative aspects of its 
working and that it is actually implemented and used in MATLAB functions 
for both quadratic and linear programming (see section 6.5.1 to appreciate 
this point). 
6.4 
LINEAR PROGRAMMING 
A general LP problem can be expressed as 
min 
c'x 

LINEAR PROGRAMMING 
367 
s.t. 
a:x = b;, 
i E E 
a E I ,  
a:x 2 bi, 
where C, ail x E W", 
bi E W. When dealing with solution algorithms for LP 
problems, it is convenient to assume that the problem has a specific form. 
An LP problem is said to be in canonical form if it involves only inequality 
constraints, and all the decision variables are restricted in sign. A canonical 
form for a maximization problem is 
max 
c'x 
s.t. 
Ax 5 b 
x 2 0 ,  
where c,x E Rn, b E W", A E R"?". We denote the ith row (corresponding 
to the ith constraint) of A by a: and the j t h  column (corresponding to the j t h  
variable) by Aj. An LP problem is said to be in standard form if it involves 
only equality constraints: 
min 
c'x 
s.t. 
AX = b 
x L 0, 
with the same notation as in the case of the canonical form. Clearly, we must 
have m < n, so that the system of linear equations is underdetermined and 
there are multiple solutions. 
The reader might think that the canonical and standard forms are some- 
what restrictive; in fact, this is not true, since a generic LP problem can be 
reduced to either form using the following transformations: 
If a variable xj is not restricted in sign, it can be rewritten as xj = 
xj' - xi, where xj',xT 2 0. 
An inequality constraint 
a:x 2 bi 
can be transformed into an equality constraint by introducing a slack 
variable si 2 0: 
a:x - si = bi. 
An equality constraint 
a:x = b, 
can be transformed into two inequality constraints: 
a:x 2 bi, 
-a:x 2 - b i .  
We know from supplement S6.1 that the feasible set of a LP problem is convex 
and polyhedral. Furthermore, the problem is both convex and concave. This 

368 
CONVEX OPTIMIZATION 
implies that an optimal solution (if any exists) may be found on the boundary 
of the feasible set; more specifically, it will be a vertex of the feasible set. 
This is easy to see by expressing the feasible region S as the convex hull of 
its extreme points X k ,  k = 1 , .  . . , I .  Strictly speaking, if S is unbounded, we 
should also consider its extreme rays; however, if we assume that the optimal 
value is finite, there is no loss of generality by discarding the possibility of 
going to infinity along a ray. Denoting by Ck the cost of the extreme point 
X k ,  we may transform the LP problem 
min 
c’x 
s.t. 
x E s 
into the equivalent problem 
I 
k = l  
i=l 
X I ,  2 0. 
This problem has just one constraint, but a possibly huge number of variables; 
nevertheless, it is easy to see that an optimal solution can be found as the 
least cost extreme point. 
If the problem is cast in standard form, the extreme points correspond to 
special solutions of the system of linear equations Ax = b; this is explained 
briefly in section 6.4.1 and is the basis of the simplex algorithm to which 
section 6.4.2 is devoted. Applying the duality principles to LP problems pro- 
duces an interesting theory, outlined in section 6.4.3. The simplex algorithm 
is certainly the best known method for LP problems, but it is not the only 
method that you get in MATLAB. The Optimization toolbox provides the 
user with two options: for medium-scale problems, a version of the active 
set method is also implemented; for large-scale problems, an interior point 
method is available. Some ideas behind interior point methods are described 
in section 6.4.4. It is interesting to note that the simplex algorithm is not, 
in the worst case, a polynomial complexity algorithm, whereas polynomial 
complexity may be proved for interior point methods. In fact, interior point 
methods are faster on many problem instances, but not always. 
6.4.1 
Given an LP problem, one of the three following cases occurs: 
Geometric and algebraic features of linear programming 
1. The feasible set is empty, and the problem has no solution. 
2. The optimal solution is, loosely speaking, “unbounded.” This case may 
occur only if the feasible set is an unbounded polyhedron, and we may 

LINEAR PROGRAMMING 
369 
keep improving the objective value by going to infinity along an extreme 
ray. 
3. The problem has a finite optimal solution, corresponding to an extreme 
point of the feasible set; note that we have an infinite set of optimal 
solutions if the level curves of the objective function are parallel to a 
face of the polyhedron (see example 6.2). 
Since there is a finite number of extreme points in a polyhedron, one way 
to solve an LP problem is to explore the set of extreme points of the feasible 
set without considering the interior points. Furthermore, a local minimizer 
will also be a global one; hence, if we find an extreme point such that no 
adjacent extreme point improves the objective function, then we have found 
the optimal solution. 
To implement this idea, the geometrical intuition must be translated into 
algebraic terms. To this end, it is convenient to work on the standard LP 
form. To avoid unnecessary complications, let us assume that the matrix 
A E It",", m < n, has full row rank. This assumption is not necessary in 
practice, as redundant equations are easily spot and eliminated. It is useful 
to consider a solution of the system Ax = b as a way to express the vector b 
as a linear combination of the columns of A: 
n c 
j = 1  
x ~ A J  
= b. 
This system has infinite solutions, but not all of them are feasible with respect 
to the requirement x 2 0. Furthermore, we would like to work on feasible 
solutions which are extreme points of the feasible set. This is easily accom- 
plished by considering only solutions in which at most m components xj are 
strictly positive, and the remaining n - m variables are zero. Such solutions 
are called basic solutions; the name derives from the fact that the m column 
vectors associated with the m possibly non-null variables are sufficient to ex- 
press the m-dimensional vector b. Any basic solution is associated with a 
basis of R" consisting of m columns of A. The m variables corresponding to 
the columns selected are called basic variables; the others are called non-basic 
variables. A basic solution with non-negative components is called a basic 
feasible solution. 
Example 6.12 Consider the following system of linear equations: 

370 
CONVEX OPTIMIZATION 
A basic solution is 
2 1  = 2, 2 2  = 3, 2 3  = 2 4  = 0, 2 5  = 1, 
which corresponds to the basis formed by the columns A',A2,A5. This 
solution is also feasible. If we take the basis formed by A', A3, A5, we obtain 
the basic solution 
2 1  = 0, 2 2  = 3, 2 3  = -2, 54 = 0, x5 = 5, 
which is not feasible since 2 3  < 0. 
U 
Basic feasible solutions are fundamental because it can be shown that they 
actually correspond to the extreme points of the feasible set. Furthermore, 
given a current extreme point, the adjacent extreme point may be obtained 
by exchanging one basic variable with a non-basic one; this means that we 
may move from a vertex to another one by driving one basic variable out of 
the basis and driving one non-basic variable into the basis. 
6.4.2 
Simplex method 
The simplex method is an iterative algorithm; given a current extreme point 
(or basic feasible solution, or basis), it looks for an adjacent extreme point 
such that the objective function is improved, and it stops when no improving 
adjacent extreme point is found. 
Assume that we have a basic feasible solution x; we will consider later how 
to obtain an initial basic feasible solution. We can partition the vector x into 
two subvectors: the subvector XB E Rm of the basic variables and the sub- 
vector XN € R"-" 
of the non-basic variables. Using a suitable permutation 
of the variable indexes, we may rewrite the system of linear equations 
A x = b  
as 
(6.20) 
where Ag E R"?" is non-singular and AN E R"~"-" . If x is basic feasible, 
where 
b = Ai'b 2 0. 
The objective function value corresponding to x is 
f = [C'B c;v] [ g ] = C'Bb. 
(6.21) 

LINEAR PROGRAMMING 
371 
Now we must find out if it is possible to improve the current solution by 
slightly changing the basis, i.e., by replacing one basic variable with a non- 
basic one. To assess the potential benefit of introducing a non-basic variable 
into the basis, we may eliminate the basic variables in equation (6.21). Using 
equation (6.20), we may express the basic variables as 
XE = AB1(b - ANXN) = b - AB'ANxN; 
(6.22) 
then we rewrite the objective function value 
C'X = CLXB + C ~ X N  
= cL(b - A B ' A N X ~ )  + ch = f^ + N x Ni 
where 
eh = C" - cLAB 1 AN. 
(6.23) 
The quantities cb are called reduced costs, as they measure the marginal 
variation of the objective function with respect to the non-basic variables. If 
ch 2 0, it is not possible to improve the objective function; in this case, 
bringing a non-basic variable into the basis at some positive value cannot 
reduce the overall cost. Therefore, the current basis is optimal if ch 2 0. If, 
on the contrary, there exists a q E N such that i., < 0, it is possible to improve 
the objective function by bringing xq into the basis. A simple strategy is to 
choose q such that 
2, = min 2j. 
3EN 
This selection does not necessarily result in the best performance of the algo- 
rithm; we should consider not only the rate of change in the objective function, 
but also the value attained by the new basic variable. Furthermore, it may 
happen that the entering variable is stuck to zero and does not change the 
value of the objective. In such a case, there is danger of cycling on a set of 
bases; ways to overcome this difficulty are well explained in the literature. 
When xq is brought into the basis, a basic variable must "leave" in order 
to maintain Ax = b. To spot the leaving variable we can reason as follows. 
Given the current basis, we can use it to express both b and the column AQ 
corresponding to the entering variable: 
m 
(6.24) 
i=l 
m 
a=1 
where B(i) is the index of the ith basic variable (i = 1,. . . , rn) and 

372 
CONVEX OPTIMIZATION 
If we multiply equation (6.25) by a number 8 and subtract it from equation 
(6.24), we obtain 
m. 
(6.26) 
i=l 
From equation (6.26) we see that 8 is the value of the entering variable in 
the new solution, and that the value of the current basic is affected in a way 
depending on the sign of di. If di 5 0, x ~ ( i )  
remains non-negative when xg 
increases. But if there is an index i such that di > 0, then we cannot increase 
zq at will, since there is a limit value for which a currently basic variable 
becomes zero. This limit value is attained by the entering variable xq, and 
the first current basic variable which gets zero leaves the basis 
bi 
x q = ,  min -. 
If d 5 0, there is no limit on the increase of zg, and the optimal solution is 
unbounded. 
In order to start the iterations, a starting basis is needed. One possibility 
is to introduce a set of auxiliary artificial variables z in the constraints: 
z = l ,  ..., m di 
di >O 
A x + z = b  
x,z 2 0. 
Assume also that the equations have been rearranged in such a way that b 2 0; 
then a basic feasible solution is trivially z = b. Minimizing the inadmissibility 
form 
4 = m i n x  t i  
by the simplex method itself, we may find a basic feasible solution if 4 = 0; 
otherwise, the original problem is not feasible. 
At this point, one should wonder what is the connection, if any exists, 
between the simplex method for LP problems and the simplex search we have 
hinted at in section 6.2.4. Actually, they are quite different approaches for 
different problems. The name of the simplex method comes from the fact that 
it works on a simplex in the reduced space of the non-basic variables. In this 
space, the origin corresponds to the current basic solution, as the non-basic 
variables are zero; the remaining extreme points of the simplex correspond to 
the adjacent bases. The simplex method checks, in the reduced space, if any 
of these extreme points improves the objective function. 
m 
i=l 
6.4.3 
Duality in linear programming 
We dealt with duality in non-linear programming in section 6.3.3. Duality in 
LP can be developed without considering the more general non-linear case, 

LINEAR PROGRAMMING 
373 
but we prefer to put it in a more general framework. Note that, due to the 
convexity of LP problems, strong duality holds. Let us start with an LP 
problem (PI) in the following canonical form: 
(PI) 
min 
c’x 
s.t. 
Ax 2 b. 
If we dualize the inequality constraints with a vector p E Wl;. of dual variables, 
we get the dual problem 
maxmin {c’x + p‘ (b - Ax)} = max 
(c’ - p’A) x} . 
p l o  x 
p 3  
Since x is unrestricted in sign, the inner minimization problem has a finite 
value if and only if 
C‘ - p‘A = 0; 
otherwise, each component of x is set to fco, depending on the sign of the 
corresponding cost coefficient, and this results in a value -co for the dual 
function. Since we want to maximize the dual function, we may enforce the 
condition above, and the dual problem (01) 
turns out to be 
(01) max 
p’b 
s.t. 
A’p = c 
p 2 0. 
The dual problem is still an LP problem, resulting from exchanging b with c 
and by transposing A. The duality relationship between (PI) and (01) can 
be interpreted the other way round, too: 
max x‘c 
min b’u 
( s.t. 
Ax = b ) u ( 
x 2 0  
Given an LP problem (Pz) in standard form, 
(Pz) 
min 
c‘x 
s.t. 
AX = b 
x 2 0 ,  
we can use the relationship above to find its dual: 
min c’x 
max XI(-c) 
( s . t .  
A x = b )  u ( s.t. 
(A’)’x = b 
x 2 0  
x 2 0  
min -b’p 
s.t. 
-Alp 2 -C 
min b’u 
s.t. 
A’u 2 -C 
max b’p 
s.t. 
A’p 5 c 

374 
CONVEX OPTIMIZATION 
Table 6.1 Duality Relationships 
Primal 
Dual 
min c'x 
a:x = bi 
a:x 2 bi 
xj 2 0 
xj unrestricted 
where we have introduced p = -v; we obtain the dual ( 0 2 )  of problem (P2). 
Note the similarities and the differences between the two dual pairs. The 
dual variables are restricted in sign when the constraints of the primal problem 
are inequalities, and are unrestricted in sign in the other case (this is coherent 
with the Kuhn-Tucker conditions). When the variables are restricted in sign 
in the primal, we have inequality constraints in the dual, whereas in the case 
of unrestricted variables we have equality constraints in the dual. In table 6.1 
we summarize the "recipe" for building the dual of a generic LP. 
Given a primal-dual pair of LP problems, the following cases may occur: 
0 Both problems have a finite optimal solution, in which case the two 
objectives have the same value at the optimum. 
0 Both problems are infeasible. 
0 One problem is unbounded, in which case the other one is infeasible. 
As a final remark, it is important to note that the dual feasibility constraint 
Alp 5 c for the dual of the problem in standard form can be read as the non- 
negativity condition on the reduced costs by equating p' = CIA,'. Recall the 
sufficient conditions (6.7) for global optimality. They correspond to 
0 Primal feasibility 
0 Dual feasibility 
0 Complementary slackness 
In fact, the simplex method works by maintaining primal feasibility and com- 
plementary slackness, and it iterates until dual feasibility is obtained. Switch- 
ing roles between primal and dual problems, it is possible to devise a dual 
simplex method which works toward primal feasibility. This is sometimes ad- 
vantageous over the primal simplex approach. However, there is still a third 
possibility: We can keep a pair of primal and dual feasible solutions and work 

LINEAR PROGRAMMING 
375 
to obtain complementary slackness. This approach leads to primal-dual algo- 
rithms, and it is exploited in the interior point method described in the next 
section. 
6.4.4 
Interior point methods 
The simplex method works only on the extreme points of the feasible set. As 
the name suggests, interior point methods move on a path that lies within 
the feasible set. There are several variants of interior point algorithms; we 
describe just the basics of a rather simple approach, which may be called 
the primal-dual barrier method, as it exploits the correspondence between a 
primal and dual problems, and an interior penalty function. It is convenient 
to start with the LP problem written in canonical form for a maximization 
problem’: 
max 
c’x 
s.t. 
A x  5 b 
x 2 0, 
which may be converted to the standard form by adding slack variables w: 
max 
c’x 
s.t. 
AX + w = b 
XI w 2 0. 
Now suppose that we do not know anything about the simplex method. We 
could try applying what we know from the general theory of constrained 
optimization; one idea would be getting rid of the non-negativity restriction by 
a suitable penalty function and then apply the method of Lagrange multipliers. 
Using an interior penalty function based on a logarithmic barrier, we get the 
problem 
j 
i 
s.t. 
AX + w = b. 
Since this problem has only equality constraints, we may dualize them by 
introducing the vector of Lagrange multipliers y, yielding the Lagrangian 
function 
L(x, w, 
y) = C’X + c 
logzj + 0 c 
logwi + y’(b - A x  - w). 
3 
2 
8The exposition here is based on [19]. 

376 
CONVEX OPTIMIZATION 
The first-order stationarity conditions are then 
Using the notation 
the optimality equations may be rewritten in matrix form: 
A’y - oX-’e = c 
y = czW-le 
A x + w = b .  
The addition of the auxiliary vector 
and a slight rearrangement yield the following set of optimality equations: 
A X + W  = b 
A’y-z 
= C 
XZe = cze 
YWe = cze. 
These equations have a nice interpretation. We have just to recall that the 
starting problem has an LP dual: 
min 
b’y 
s.t. 
A’y 1 c 
Y L 01 
or, adding slack variables z, 
min 
b’y 
s.t. 
A’y - z = c 
Y , Z  2 0. 

CONSTRAINED OPTlMlZATlON IN MATLAB 
377 
Hence, the equations we arrived at are simply the conditions of primal feasi- 
bility, dual feasibility, and (if D = 0) complementary slackness (see theorem 
6.7). For (T > 0, they are a set of non-linear equations: 
where 
which may be tackled by Newton’s method (section 3.4.2). 
In principle, by solving this system of non-linear equations for different 
values of 0 we get a path (xar 
yo, w,, 2,). 
This path is called central path 
and for D + 0, it leads to the optimal solution of the original LP. From a 
computational point of view, it is not convenient to start with a too small (T, 
nor to solve the non-linear equations exactly for each D. One idea is to reduce 
the value of the penalty parameter within the iterations of Newton’s method, 
so that the central path is only a reference path leading to solution through 
the interior of the feasible set. It is worth noting the similarity between this 
path following approach and homotopy continuation methods described in 
section 3.4.5. In both cases we solve a difficult problem by a sequence of 
easier problems which converge to the original one. 
Interior point methods have a polynomial computational complexity which 
is, theoretically, better than the complexity of the simplex method, which is 
exponential in pathological cases.’ It should be stressed that many compu- 
tational tricks are needed to implement both the simplex and interior point 
method in a very efficient way. These are beyond the scope of this book, but 
it should be clear that the two approaches may lead to qualitatively different, 
though cost-equivalent solutions, as illustrated in the next section. 
6.5 
CONSTRAINED OPTIMIZATION IN MATLAB 
In this section, we briefly describe functions from the Optimization toolbox 
which can be used for constrained optimization. In particular we consider the 
functions linprog for linear programming, quadprog for quadratic program- 
ming, and fmincon for generic constrained optimization. The coverage is not 
complete really, but we will provide a couple of examples related to financial 
problems. 
gComputational complexity has been introduced in section 3.1.3. 

378 
CONVEX OPTIMIZATION 
6.5.1 
Linear programming in MATLAB 
The Optimization toolbox includes a function, linprog, which solves LP prob- 
lems of the form 
min 
c’x 
s.t. 
Ax 5 b 
We have seen that alternative algorithms are available for linear programming. 
What happens in MATLAB, then? Consider the following rather trivial LP 
problem: 
It is easy to see that two basic optimal solutions are ( 1 , O )  and (0,l). All 
the solutions between these two extreme points are equivalent and optimal. 
We expect that the simplex algorithm should report one of the two extreme 
points. To use linprog, we have to change the sign of the coefficients in the 
objective function and to pass as null vectors the parameters we do not need: 
>> x=linprog( C-1 -11, Ci 11 I, [I C1 
CO 01) 
Optimization terminated successfully. 
x =  
0.5000 
0.5000 
We see that the reported solution is on the center of the face of equivalent 
solutions, and it is not basic. This happens since the default LP option in 
MATLAB is an interior point algorithm. Actually, linprog implements three 
alternative approaches: 
if the Largescale option is on, then an interior point method is used; 
if the Largescale option is off, then an active set method is used (see 
section 6.3.5), which by the way is the same used by quadprog ; 
when Largescale option is off, we may select the simplex method by 
setting the Simplex option. 
The three methods also differ in terms of using an initial solution or not. To 
get the point, we may play a little bit with the options. 
>> options = optirnset(’LargeScale’,’off’); 

CONSTRAINED OPTIMIZATION IN MATLAB 
379 
>> x=linprog( [-I -11 , [I 11 ,I, [I ,[I , [O 01 , [I ,[I ,options) 
Optimization terminated successfully. 
x =  
0.5000 
0.5000 
>> x=linprog( [-I -11 , [I 11 ,I, [I , [I, CO 01, [ I ,  CO 0.51 ,options) 
Optimization terminated successfully. 
x =  
0.2500 
0.7500 
Note that to set the options, we have to pass (possibly empty) vectors cor- 
responding to upper bounds and initial points. We see that, starting from 
the initial solution, the search moves along the gradient until the constraint 
is reached, which is turned active and the process is stopped. With the active 
set method, the solution depends on the initial point. If we select the simplex 
method, we have a different behavior: 
>> options = optimset(’LargeScale’, ’ o f f ’ ,  ’Simplex’, ’on’); 
>> x=linprog(C-I -11, [I 11 ,I, [I, [ I ,  [O 01, [ I ,  [I ,options) 
Optimization terminated. 
x =  
I 
0 
>> x=linprog( [-1 -11, [1 11,1, [I, [I, [O 01, [I, [O 0.51 ,options) 
Warning: Simplex method uses a built-in starting point; 
> In linprog at 215 
Optimization terminated. 
ignoring user-supplied XO. 
x =  
1 
0 
We see that a basic solution is obtained, and that the initial point is ignored. 
The initial point is ignored by the interior point method as well: 
>> options = optimset(’LargeScale’,’on’); 
>> x=linprog( 1-1 -11, C1 11,1, [I, [ I ,  [O 01, [ I ,  [O 0.51 ,options) 
Warning: Large scale (interior point) method uses 
a built-in starting point; ignoring user-supplied XO. 
> In linprog at 205 
Optimization terminated. 
x =  
0.5000 
0.5000 

380 
CONVEX OPTIMIZATION 
It is important to bear in mind that, unless the simplex method is selected, an 
optimal but non-basic solution may be obtained. This may have consequences 
if linprog is embedded within an algorithm that requires basic optimal so- 
lutions. For instance, in some problems with special structure, the simplex 
method yields an integer solution; this is the case when the feasible set is 
a polyhedron whose extreme points have integer coordinates. Indeed, the 
simplex method must be used when tackling a mixed-integer programming 
problem by a branch and bound strategy (see chapter 12). 
6.5.2 
In chapter 2 we have considered the immunization of a bond portfolio (see 
example 2.12 on page 63). We considered three bonds and we selected a port- 
folio with given value, duration, and convexity. The problem was set up in 
such a way that there was a unique solution (which may require selling a bond 
short). However, when many bonds are available, more than one solution can 
be found. In such a case, it might make sense to look for the “best” solution 
among the feasible ones. Defining “best” is not easy at all. We should prob- 
ably include some explicit characterization of uncertainty in interest rates, 
and this leads to stochastic programming problems described in chapter 11. 
Furthermore, since this is likely to be an asset-liability management problem, 
rather than a simple portfolio management problem, we should also character- 
ize uncertainty in liabilities. However, just to try a MATLAB programming 
exercise, let us consider a simple linear programming model.1° One possible 
idea is maximizing the average yield of the portfolio, given that the portfolio 
must have duration D and convexity C; we also add the requirement that 
short sales are not allowed. This results in the following linear programming 
(LP) model: 
A trivial LP model for bond portfolio management 
N 
i=l 
N 
i=l 
N 
i=l 
N 
l0We should probably say “simplistic” rather than simple. The model is somewhat inspired 
by a model discussed in (141 for a different purpose. 

CONSTRAINED OPTIMIZATION IN MATLAB 
381 
Note that, without the non-negativity constraints on the weights wi, 
we may 
easily end up with an unbounded solution." It is easy to write a MATLAB 
function solving this problem. The code is illustrated in figure 6.10. 
Since all the functions dealing with bonds are able to cope with vector 
arguments, provided that they are of compatible size, we group the bond 
characteristics in vectors." 
Here we assume that we know the clean price 
for each bond, and we use bndyield to compute the corresponding yield and 
bnddury and bndconvy to obtain the sensitivities. Note that, when calling 
linprog, we must change the sign of the coefficients in the objective function, 
because we want to maximize it; the next four arguments contain the coef- 
ficient matrix and the right-hand side of inequality and equality constraints 
(since we have only equality constraints in this model, the first two arguments 
are empty); finally, we have a vector of zeros representing the lower bound 
on the decision variables. First we consider a set of five bonds, and then we 
enlarge the set by adding five more bonds. Running this script, we get the 
following output: 
>> LPbondsl 
Optimization terminated. 
weights1 = 
0.4955 
0.0000 
0.4361 
0.0684 
0.0000 
Optimization terminated. 
weights2 = 
0.0000 
0.0000 
0.3813 
0.0000 
0.0000 
0.0800 
0.0000 
0.5387 
0.0000 
0.0000 
You may notice that in both cases only three bonds are included in the port- 
folio. This might appear a bit odd, since one would assume that considering 
"See (141 for conditions ensuring the finiteness of the solution and for generalizations of 
the model. 
"The reader is referred to section 2.3.4 for a description of MATLAB functions to deal 
with simple bonds. 

382 
CONVEX OPTIMIZATION 
% SCRIPT LPBonds1.m 
% BOND CHARACTERISTICS FOR SET 1 
settle 
= ’19-Mar-2006’; 
maturityl = [’15-Jun-2021’ ; ’02-Oct-2016’ ; ’01-Mar-2031’ ; ... 
Face 1 
= [500 ; 1000 ; 250 ; 100 ; 1003; 
couponRate1 = C0.07 ; 0.066 ; 0.08 ; 0.06 ; 0.051; 
cleanPrice1 = [ 549.42 ; 970.49 ; 264.00 ; 112.53 ; 87.93 I; 
% COMPUTE YIELDS AND SENSITIVITIES 
yields1 = bndyield(cleanPrice1, couponRate1, settle, maturityl, ... 
durationsl = bnddury(yields1, couponRate1, settle, maturityl, ... 
convexitiesl = bndconvy(yields1, couponRate1, settle, maturityl, ... 
% SET UP AND SOLVE LP PROBLEM 
A1 = [durationsl’ 
’01-Mar-2026’ ; ’01-Mar-2011’1 ; 
2, 0, [I , [I , [I , [I, [I , Facell; 
2, 0, [I , [I , [I , [I, [I , Facell; 
2, 0, [I , [I , [I , [I, [I , Facell; 
convexitiesl’ 
ones(l,5)1; 
b = [ 10.3181 ; 157.6346 ; 11; 
weights1 = linprog(-yieldsl, [I, [I ,Al,b,zeros(l,5)) 
% BOND CHARACTERISTICS FOR SET 2 
maturity2 = [maturityl ; . . . 
’15-Jan-2019’ ; ’10-Sep-2010’ ; ’01-Aug-2023’ ; ... 
’ 01-Mar-2016 ’ ; ’01-May-2013’1 ; 
Face2 
= [Facel ; 100 ; 500 ; 200 ; 1000 ; 1003; 
couponRate2 = [couponRatel ; 0.08 ; 
cleanPrice2 = [ cleanPrice1 ; . . . 
% COMPUTE YIELDS AND SENSITIVITIES 
yields2 = bndyield(cleanPrice2, couponRate2, settle, maturity2. ... 
durations2 = bnddury(yields2, couponRate2, settle, maturity2, ... 
convexities2 = bndconvy(yields2, couponRate2, settle, maturity2, ... 
% SET UP AND SOLVE LP PROBLEM 
A2 = [durations2’ 
convexities2’ 
ones(1,lO)l; 
0.07 ; 0.075 ; 0.07 ; 0.061 ; 
108.36 ; 519.36 ; 232.07 ; 1155.26 ; 89.29 1; 
2, 0, [I , [I , [I , [I, [I , Face2); 
2, 0, [I , [I , [I , [I, [I , Face2); 
2, 0, C1 , Cl , [I , [I, [I , Face2); 
weights2 = linprog(-yields2, [I, c1 ,A2,b,zeros(l,lO)) 
Fig. 6.10 Code to set up and solve a linear programming model for bond portfolio 
optimization. 

CONSTRAINED OPTIMIZATION IN MATLAB 
383 
more bonds leaves more space for diversification. Actually, this does not hap- 
pen by chance, but it depends on the structure of the optimal solution of a 
linear programming problem. If we have only M equality constraints in a 
linear program, there is an optimal solution (provided that the problem is 
bounded and feasible) with at most M decision variables which take a non- 
zero value at optimality. Since here M = 3, the optimal portfolio will always 
include just three bonds, even if many more are available, unless there are 
alternative optima (in which case the solution would depend on the algorithm 
we select for linprog; for this problem instance, there are no alternative op- 
tima, and the interior point method returns the same solution we would obtain 
by selecting the simplex method). If we considered only duration constraints, 
we would include just two bonds, whose durations would bracket the target 
duration. 
6.5.3 
In section 2.4.3 we have considered some MATLAB functions to trace the 
set of mean-variance efficient portfolios. To that aim, we must solve a set of 
problems of the form (2.13), which we recall here for convenience: 
Using quadratic programming to trace efFicient portfolio frontier 
min 
w'Xw 
s.t. 
w'f; = 
n 
c w i  = 1 
i=l 
for different values of the target expected return FT. We see that this is 
a quadratic programming problem, which can be solved by quadprog. It 
is a useful exercise to write a function to do that, which will be a (very) 
simplified version of frontcon. The input arguments to this function, which 
we call NaiveMV and whose code is displayed in figure 6.11, are: ERet, the 
vector of expected return for the assets we are considering, ECov, the variance- 
covariance matrix, and NPts the number of efficient points (portfolios) we want 
to find on the frontier. Output arguments are: PRisk, the risk (standard 
deviation of return) for each portfolio we generate, PRoR, the rate of return, 
and PWts, the matrix portfolio weights (one vector for each portfolio). 
To select target returns we have to spot both the maximum return achiev- 
able and the return associated with the minimum variance (minimum risk) 
portfolio. The first target return is obtained by solving 
max 
W'F 
n 

384 
CONVEX OPTIMIZATION 
function [PRisk, PRoR, PWts] = NaiveMV(ERet, ECov, NPts) 
ERet = ERet( : ; 
% makes sure it is a column vector 
NAssets = length(ERet); 
% vector of lower bounds on weights 
VO = zeros(NAssets, 1); 
% row vector of ones 
V1 = ones(1, NAssets); 
% set medium scale option 
options = optimset(’LargeScdle’, ’off’); 
1 Find the maximum expected return 
MaxReturnWeights = linprog(-ERet , [I, [I, V1, 1, VO) ; 
MaxReturn = MaxReturnWeights’ * ERet; 
Find the minimum variance return 
MinVarWeights = quadprog(ECov,VO, [I, [I ,V1,1,VO, [I, [I ,options); 
MinVarReturn = MinVarWeights’ * ERet; 
MinVarStd = sqrt (MinVarWeights’ * ECov * MinVarWeights) ; 
% check if there is only one efficient portfolio 
if MaxReturn > MinVarReturn 
% get number of assets 
RTarget = linspace(MinVarReturn, MaxReturn, NPts) ; 
NumFrontPoints = NPts; 
RTarget = MaxReturn; 
NumFrontPoints = 1; 
end 
% Store first portfolio 
PRoR = zeros(NumFrontPoints, 1) ; 
PRisk = zeros(NumFrontPoints, 1); 
PWts = zeros (NumFrontPoints, NAssets) ; 
PRoR(1) = MinVarReturn; 
PRisk(1) = MinVarStd; 
PWts(1, :) = MinVarWeights(:)’; 
% trace frontier by changing target return 
VConstr = ERet’; 
A = [Vl ; VConstr 1; 
B = [I ; 01; 
for point = 2:NumFrontPoints 
else 
B(2) = RTarget (point) ; 
Weights = quadprog(ECov,VO, [I, [I ,A,B,VO, [I, [I ,options) ; 
PRoR(point) = dot(Weights, ERet); 
PRisk(point) = sqrt (Weights’*ECov*Weights) ; 
PWts(point, :) = Weights(:)’; 
end 
Fig. 6.11 Simple MATLAB code to trace the mean-variance efficient frontier. 

CONSTRAINED OPTIMIZATION IN MATLAB 
385 
Actually, this is a trivial LP problem, whose optimal solution is clearly the 
maximum expected return. Nevertheless, if additional constraints are given 
on asset allocation, we may really have to solve an LP problem. This is why we 
use linprog in the code to get the MaxReturn. The second return is obtained 
by finding the minimum risk portfolio: 
min 
wlCw 
n 
i=l 
wa 2 0 
and by computing its return (we take for granted that the solution of this 
problem is unique). These are the two extreme efficient portfolios. If they 
are equal, there is a unique portfolio maximizing return and minimizing risk: 
an unlikely event in practice, which is taken into account by the function 
(in this case the number NumFrontPoints of efficient points in the frontier is 
1; otherwise it is the input number NPts). To find other efficient portfolios, 
we use the function linspace to specify the vector of NPts target returns 
between the two extremes. Then we solve a sequence of risk minimization 
problems, obtaining the risk/return characteristics and the composition of 
each portfolio. To that aim we must simply change one element, corresponding 
to target return, in the vector B containing the right-hand sides of linear 
equality constraints in the quadratic program. 
We may check that NaiveMV yields the same results as f rontcon for this 
simple problem: 
>> ExpRet = [ 0.15 0.2 0.081; 
>> CovMat = [ 0.2 0.05 -0.01 ; 0.05 0.3 0.015 ; ... 
>> [PRisk, PRoR, PWts] = naiveMV(ExpRet, CovMat, 10); 
>> [PRoR , PRisk] 
-0.01 0.015 0.11; 
ans = 
0.1143 
0.2411 
0.1238 
0.2456 
0.1333 
0.2588 
0.1428 
0.2794 
0.1524 
0.3060 
0.1619 
0.3370 
0.1714 
0.3714 
0.1809 
0.4093 
0.1905 
0.4682 
0.2000 
0.5477 
6.5.4 
Non-linear programming in MATLAB 
The most general function to deal with a non-linear programming problem 
is fmincon. How this function should be called depends on the problem at 

386 
CONVEX OPTIMIZATION 
hand, as constraints are partitioned in linear and non linear constraints as 
follows: 
min 
f(x) 
s.t. 
Ax < b 
AeqX = be, 
g(x) 5 0  
geq(X) = 0 
l < x < u .  
Matrices and both upper and lower bounds are passed as vector arguments, 
whereas the non-linear functions for inequality and equality constraints must 
be written as M-files or anonymous functions. For instance, to solve 
min 
ezl (4s; + 2 4  + 4x122 + 2x2 + 1) 
~
1
~
2
 
- 21 - ~2 5 -1.5 
z1z2 2 10 
s.t. 
we may write two M-files. The first one must return two vectors corresponding 
to non-linear constraints: 
function [c, ceql = confun(x) 
'L non-linear inequality constraints 
c = C1.5 + x(l)*x(2) 
- ~ ( 1 )  - ~(2); 
% non-linear equality constraints 
ceq = [I; 
Here the second vector is empty, since there are no equality constraints. Also 
note the change in sign for the second constraint. Another file is needed for 
the objective function: 
function fval = objfun(x) 
fval = exp(x(1)) 
* ( 4*x(1)'2 
+ 2*x(2)-2 + 4*x(l)*x(2) 
+ 2*x(2) + 1); 
These M-files may also return analytical values for the gradients of the in- 
volved functions. Then we may call fmincon: 
>> xo = [-1,11 ; 
>> options = optimset ( 'Largescale ' , ' off '1 ; 
>> [x, fval] = fmincon(@objfun,xO, 11, [I, [I, [I, [I, [I ,Qconfun,options) 
Optimization terminated: first-order optimality measure less 
-x(l)*x(2) - 101; 
than options.TolFun and maximum constraint violation is less 
than options.TolCon. 
Active inequalities (to within options.TolCon = le-006): 
lower 
upper 
ineqlin 
ineqnonlin 
1 

INTEGRATING SIMULATION AND OPTIMIZATION 
387 
x =  
-9.5474 
1.0474 
f v a l  = 
0.0236 
We should note that fmincon is not always the best choice. For instance, 
model calibration may lead to optimization models of the form 
m 
i=l 
which are best solved as non-linear least squares problems by lsqnonlin. 
6.6 
INTEGRATING SIMULATION AND OPTIMIZATION 
Simulation models are a convenient way to evaluate the performance of com- 
plex and stochastic systems for which analytical models may be very hard 
or even impossible to come up with. However, they are just able to evaluate 
a performance measure given a set of input parameters. In option pricing, 
this may be just what we need, but we could also be interested in finding the 
optimal set of parameters; in other words, in many settings, such as portfo- 
lio optimization, we would like to integrate simulation and optimization (see, 
e.g., [5]). Such an integration may certainly be worthwhile, as it provides us 
with a way to optimize complex and stochastic systems which cannot be dealt 
with by deterministic and even stochastic programming. However, we may 
have to face at least some of the following issues: 
0 The objective function may be non-convex. 
0 Some of the input parameters may be discrete rather than continuous. 
0 The evaluation of the objective function may be affected by noise. 
0 Using gradient-based methods may be difficult, as gradients must be 
estimated. 
Let us start from the last point and assume for simplicity that we want to 
solve an unconstrained optimization whereby the objective function is the 
expected value of some random performance measure depending on a vector 
of parameters x E Rn: 
min f(x) = E,[h(x,w)]. 
For optimization purposes it would be useful to have a way to compute the 
gradient V f (x) at any point. As pointed out in section 4.5.2, a gradient could 
be estimated by finite differences, but this is made difficult by the noise in 

388 
CONVEX OPTIMIZATION 
the estimates. Using common random numbers to reduce variance is the least 
we should do; an alternative is represented by using some form of regression. 
The idea is to use a simulation model to build a sort of empirical metamodel, 
the response surface, which yields an analytical approximation g(x) of the 
unknown objective function f (x) with respect to the input parameters. If we 
want to estimate the gradient at a certain point x, we may consider a linear 
approximation, such as 
n 
g(x) = a + c 
pixi = a + plx. 
i=l 
We may estimate a and p by evaluating f for a set of test values xj and by 
minimizing a function of the regression errors. Let fj be the estimate of f 
corresponding to the point xi ( j  = 1,. . . , m). We have 
fj = a + p’xi + €j, 
where c j  is an error term (or a residual, if you prefer; see section 3.3). Using 
least squares, we may find a and 
E; is minimized. 
Let us define the matrix 
in such a way that 
where xi is the jth setting of the parameter xi. It can be shown that the sum 
of the squared errors is minimized by 
[ ; 
] = (x’x)-’x’i, 
where f is the vector of the m estimates of f. Then we may set V f (k) = p and 
use it within a gradient optimization method. A first-order fit is suitable when 
we are not close to the optimum. When we are approaching the minimizer, a 
quadratic polynomial can be fitted: 
1 
2 
f (x) = (Y + p’x + 4 r X ,  
where I’ is a square matrix, and quadratic programming may be used to 
find the optimal set of parameters for the metamodel, which is successively 
updated until some convergence criterion is met [7]. This results in a method 
resembling the quasi-Newton methods for non-linear programming. 
An obvious disadvantage of an approach based on the response surface 
methodology is that it is likely to be quite expensive in computational terms. 

ELEMENTS OF CONVEX ANALYSIS 
389 
Alternative methods, such as perturbation analysis, have been proposed to 
estimate sensitivities with a single simulation runs. An example of an appli- 
cation to estimate option sensitivities can be found in [4]; we will consider a 
simple case in section 8.5. A treatment of these methods require deep mathe- 
matical knowledge, so we refer, e.g., to [15] for a thorough treatment of these 
topics. We would only like to point out a subtle issue of using gradient-based 
methods for simulation optimization. In principle, we should evaluate 
0 . w  = V L W ,  w)l, 
Eu [V+, w)]. 
but simulation actually yields something like 
That expectation can be commuted with differentiation is not granted at 
all. This issue is well explored in [8]; for a treatment oriented to financial 
engineering, see [9]. 
Given all of the considerations above, it’s no surprise that non-linear pro- 
gramming methods that do not exploit derivatives in any way are of interest 
for simulation optimization. One such method is the simplex search procedure 
we have outlined in section 6.2.4; see [ll] for a recent paper on this 
Although using a simplex search procedure has its merit, it does not over- 
come the possible difficulties due to the non-convexity of the objective func- 
tion or the discrete character of some decision parameters. For such cases the 
integration of simulation with metaheuristics such as tabu search or genetic 
algorithms, which we will describe in section 12.4, is probably the only practi- 
cal solution approach. Indeed, this is the approach taken in some commercial 
stochastic simulation packages. The application of a population-based ap- 
proach like genetic algorithms or their variants has the further advantage of 
making the noisy function evaluations less critical. 
S6.1 ELEMENTS OF CONVEX ANALYSIS 
Convexity is arguably the most important concept in optimization theory. In 
the next two sections we want first to recall the related concepts of convex set 
and convex function, and then to outline a few concepts in polyhedral theory 
which are important for linear and mixed-integer programming. 
S6.1.1 Convexity in optimization 
Convexity is a possible attribute of the feasible set S of an optimization prob- 
lem. 
131t may also be worth noting that MATLAB allows the integration of simplex search and 
other no-derivatives methods with the dynamic systems simulator SIMULINK. 

390 
CONVEX OPTIMIZATION 
Fig. 6.12 Convex and non-convex sets. 
Definition. A set S 2 W'l is a convex set if 
x,y€S*Xx+(l-X)yES 
VXE [0,1]. 
Example 6.13 The concept of convexity can be grasped intuitively by con- 
sidering that the points of the form Ax + (1 - X)y, where 0 5 X 5 1, are 
simply the points 011 the straight line joining x and y. A set S is convex if 
the line joining any pair of points x, y E S is contained in S. Consider the 
three subsets of R2 depicted in Figure 6.12. S1 is convex; but Sz is not. $3 
is 
a discrete set and it is not convex; this fact has important consequences for 
discrete optimization problems. 
0 
The following property is easy to verify. 
PROPERTY 6.10 The intersection of convex sets is a convex set. 
Note that the union of convex sets need not be convex. The convex comhi- 
natzon of p points x1 , x2, . . . , xp E W" is defined as 
1=1 
?=I 
Given a set S c W"; the set of points which are the convex combinations of 
points in S is the convex hull of S (denoted by [S]). If S is a convex set, 
then S = [S]. The convex hull of a generic set S is the smallest convex set 
containing S; it can also be regarded as the intersection of all the convex sets 
containing S. Two non-convex sets and their convex hulls are shown in figure 
6.13. 
Definition. A scalar function f: W" + R, defined over a convex set S 
R", 
is a convex function on S if, for any x and y in S, for any X E [0,1], we have 
f (Ax + (1 - WY) I Xf(4 + (1 - X)f(Y). 
If this condition is met with strict inequality for all x # y, the function is 
strictly convex. 

ELEMENTS OF CONVEX ANALYSIS 
391 
fg. 6 14 Coiivcx aiiti iioii-corivex functions. 
Definition. A fiiiiction .f is c071c11.11e if (-f) is convcx. 
Tlie c:oncept of convex function is illustrated in figure 6.14. The first func- 
t,ioii is convex; wlicrcas t,he second is not. Also, the third function is convex; ii 
convex fiiiiction need not, he differentiable everywhere. The definition can he 
interpreted as follows. Given any two points x and y, consider another point 
which is H convex combination of x and y; then the function value in this 
point is ovcrestiinatecl by the convex conihination of the function values f(x) 
;uitl f(y), siricc tlic linc scgiiicnt joining (x, 
f(x)) arid ( y ,  f(y)) lics abovc 
the griL1)li of the fiinction between x and y. In other words, it fiinctiori is 
(:oiivcx if its epigrapli, i.e., the region above the functioii graph, is a coiivex 
set,. A fiutlicr link hetwcen coIivcx sets and convex functions is that the set 
S = {x E R" I g(x) 5 O} is convex if g is a convex function. Convexity of 
fiilictioris is prc!scrved hy some operations; in particular, a lincar conihination 
Fig. 6.13 NOn-convex sets and their convex hulls.

392 
CONVEX OPTIMIZATION 
of convex functions fi, 
n 
f(x) = CXifi(4, 
i=l 
is a convex function if X i  
There are alternative characterizations of a convex function. For our pur- 
poses the most important is the following. If f is a differentiable function, it 
is convex (over S) if and only if 
0, for any i. 
f(x) L f(x0) + Vf'(XO)(X - xo) 
vx,xo E s. 
(6.27) 
Note that the hyperplane 
z = f(x0) + Vf'(XO)(X - XO) 
is the usual tangent hyperplane, i.e., the first-order Taylor expansion of f at 
XO. For a differentiable function, convexity implies that the first-order approx- 
imation at a certain point xo consistently underestimates the true value of the 
function at all the other points x E S. The concept of a tangent hyperplane 
applies only to differentiable convex functions, but it can be generalized by 
the concept of a support hyperplane. 
Definition. Given a convex function f and a point xo, the hyperplane (in 
R"+l) given by z = f(xo) + T'(X - xo), which meets the epigraph of f in 
(xo, 
f(xo)) and lies below it is called the support hyperplane of f at xo. 
The concept of a support hyperplane is depicted in figure 6.15. A support 
hyperplane at xo is essentially defined by a vector y such that 
f (x) L f (xo) + r'(x - xo) 
vx E s. 
(6.28) 
The vector y in inequality (6.28) plays the same role as the gradient does 
in inequality (6.27). If f is differentiable in XO, the support hyperplane is 
the usual tangent hyperplane and 
= Vf(x0). This is why a vector y such 
that inequality (6.28) holds is called a subgradient of f at XO. If f is non- 
differentiable, the support hyperplane need not be unique and there is a set of 
subgradients. The set of subgradients at a point xo is called the subdifferential 
off at XO, and it is denoted by af (xo). It can be shown that a convex function 
on a set S is subdifferentiable on the interior of S, i.e., we can always find a 
subgradient (on the boundary of the set S some difficulties may occur due, 
e.g., to discontinuities, but we need not be concerned with this technicality in 
the following). 
A further characterization of convex functions can be given for twice- 
differentiable functions. 
THEOREM 6.11 Iff is a twice-differentiable function, defined on a non- 
empty and open convex set S, then f is convex if and only if its Hessian 
matrix is positive semidefinite at any point in S. 

ELEMENTS OF CONVEX ANALYSIS 
393 
Fig. 6.15 Illustratioii of the support hyperplane for convex fuiictions. 
We recall that the Hessian matrix H(x) is the (symmetric) matrix of 
second-order derivatives of f(x): 
d2 f 
H -- 
‘’ - ax, 
ax, 
We also recall that a symmetric (hence square) matrix A(x) is positive seniidef- 
inite on S if 
x’A(x)x 2 0 
‘dx E 5’. 
Thc matrix is positive definite if the inequality above is strict for all x # 0. If 
the Hessian matrix is positive definite, the function is strictly convex; however, 
the converse is not necessarily true. The definiteness of a matrix may be 
investigated by checking the sign of its eigenvalues; the matrix is positive 
scinidefinite if all of its eigenvalues are non-negative, and it is positive definite 
if all of its oigcnvalues are positive. 
S6.1.2 
Convex polyhedra and polytopes 
Consider in R” the hyperplane a:x = b,, where b, E W and a,, x E R” are 
coluniri vectors. l4 A hyperplane divides R” into two half-spaces expressed by 
the linear inequalities aix 5 b, and aix 2 b,. 
Definition. A polyhedron P 
tion of linear inequalities, i.e., 
R” is a set of points satisfying a finite collec- 
P = {X E R” I Ax 2 b}. 
A polyhedron is therefore the intersection of a finite collection of half-spaces. 
’*Unless the contrary is stated, we assume that all vectors are columns. 

394 
CONVEX OPTIMIZATION 
PROPERTY 6.12 A polyhedron is a convex set (it is the intersection of 
convex sets). 
Definition. A polyhedron is bounded if there exists a positive number M 
such that 
P 
{X E JR" I -M 5 ~j 5 M j = 1,. . . , n } .  
A bounded polyhedron is called a polytope. A polytope and an unbounded 
polyhedron are shown in figure 6.16. 
Definition. A point x is an extreme point of a polyhedron P if x E P and it 
is not possible to express x as x = fx' + fx" with x', x" E P and x' # x". 
A polytope P has a finite number of extreme points xl,. . . , d. 
Any point 
x in a polytope P can be expressed as a convex combination of its extreme 
points: 
in other words, a polytope is the convex hull of its extreme points. In the case 
of an unbounded polyhedron, this is not true and we must introduce another 
concept. 
Definition. A vector r E R" is called a ray of the polyhedron 
P = {x E JR" I Ax 2 b} 
if Ar 2 0. 
If xo is a point in a polyhedron P and r is a ray of P, then 
Clearly, only unbounded polyhedra have rays. 
Definition. A ray r of a polyhedron P is called an extreme ray if it cannot 
be expressed as r = irl + ir2 where r1,r2 are rays of P such that rl # Xr2 
for any number X > 0. 
A polyhedron P can be described in terms of its extreme rays and points, 
in the sense that any point x E P can be expressed combining extreme rays 
and points: 
K 
9 
j=1 
k = l  
j = 1  

ELEMENTS OF CONVEX ANALYSlS 
395 
Fig 6.16 Two-tliiiieiisional polytope (a) arid uiibountletl polyhedron (b) . 

396 
CONVEX OPTIMIZATION 
For further reading 
In the literature 
0 A general and introductory book on optimization theory is [18]. 
0 See, e.g., [3] for non-linear programming and I191 for linear program- 
ming. 
0 Interior point methods are dealt with in [20]. 
0 If you are interested in the theory behind convex optimization, you 
should check [lo] or [16]. If you are more interested in the numerical 
aspects of optimization, [6] is for you. 
0 For a text which presents non-linear programming methods is some de- 
tail, with applications to finance, see [l]. 
0 Advanced issues in portfolio management are dealt with in [17]. 
0 For a tutorial survey on the integration of simulation and optimization, 
see [7]. A deep mathematical treatment is given in [15]. 
0 The use of simplex search to drive a simulator is explored in [2] and [ 111. 
On the Web 
A good source for information on the practical application of optimiza- 
tion models and methods to a variety of problems is 
http://e-0PTIMIZATION.COM. 
0 Relevant academic societies in the field are: 
- http : //www . inf orms . org (INFORMS: Institute for Operations Re- 
- http : //www . siam. org (SIAM: Society for Industrial and Applied 
- http: //www. cam. rice. edu/"mathprog (MPS: Mathematical Pro- 
search and the Management Sciences) 
Mathematics) 
gramming Society) 
A good pointer for interior point methods is 
http://www-unix.mcs.anl.gov/otc/InteriorPoint, 
0 Michael Trick's Web page lists several useful links to journals, societies, 
people, etc.; see http: //mat. gsia. cmu. edu. 

REFERENCES 
397 
REFERENCES 
1. M. Bartholomew-Biggs. Nonlinear Optimization woith Financial Appli- 
cations. Kluwer Academic Publishers, New York, 2005. 
2. R.R. Barton and J.S. Ivey, Jr. Nelder-Mead Simplex Modifications for 
Simulation Optimization. Management Science, 42:954-973, 1996. 
3. M.S. Bazaraa, H.D. Sherali, and C.M. Shetty. Nonlinear Programming. 
Theory and Algorithms (2nd ed.). Wiley, Chichester, West Sussex, Eng- 
land, 1993. 
4. M. Broadie and P. Glasserman. Estimating Security Price Derivatives 
Using Simulation. Management Science, 42:269-285, 1996. 
5. A. Consiglio and S.A. Zenios. Designing Portfolios of Financial Products 
via Integrated Simulation and Optimization Models. Operations Research, 
47:195-208, 1999. 
6. R. Fletcher. Practical Methods of Optimization (2nd ed.). Wiley, Chi- 
Chester, West Sussex, England, 1987. 
7. M.C. Fu. Optimization by Simulation: A Review. Annals of Operations 
Research, 53:199-247, 1994. 
8. P. Glasserman. Gradient Estimation via Perturbation Analysis. Kluwer 
Academic, Boston, MA, 1991. 
9. P. Glasserman. Monte Carlo Methods in Financial Engineering. Springer- 
Verlag, New York, NY, 2004. 
10. J.-B. Hiriart-Urruty and Claude Lemarkhal. Convex Analysis and Mini- 
mization Algorithms (vols. 1 and 2). Springer-Verlag, Berlin, 1993. 
11. D.G. Humphrey and J.R. Wilson. A Revised Simplex Search Procedure 
INFORMS 
for Stochastic Simulation Response Surface Optimization. 
Journal on Computing, 12:272-283,2000. 
12. R. Korn. Optimal Portfolios: Stochastic Models for Optimal Investment 
and Risk Management in Continuous Time. World Scientific Publishing, 
Singapore, 1997. 
13. R.C. Merton. Continuous- Time Finance. Blackwell Publishers, Malden, 
MA, 1990. 
14. J. Paroush and E.Z. Prisman. On the Relative Importance of Duration 
Constraints. Management Science, 43: 198-205, 1997. 
15. G.C. Pflug. Optimization of Stochastic Models: The Interface Between 
Simulation and Optimization. Kluwer Academic, Dordrecht, The Nether- 
lands, 1996. 

398 
CONVEX OPTIMIZATION 
16. R.T. Rockafellar. Convex Analysis. Princeton University Press, Prince- 
ton, NJ, 1970. 
17. B. Scherer and D. Martin. Introduction to Modern Portfolio Optimization 
with NuOPT, S-Plus, and PBayes. Springer, New York, 2005. 
18. R.K. Sundaram. A First Course in Optimization Theory. Cambdridge 
University Press, Cambridge, 1996. 
19. R. J. Vanderbei. Linear Programming: Foundations and Extensions. Kluwer 
Academic, Dordrecht, The Netherlands] 1996. 
20. S. J. Wright. Primal-Dual Interior-Point Methods. Society for Industrial 
and Applied Mathematics, Philadelphia, 1997. 

