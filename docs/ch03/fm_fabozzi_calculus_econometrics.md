# Calculus, Optimization & Financial Econometrics

!!! info "Source"
    **The Mathematics of Financial Modeling and Investment Management** by Sergio M. Focardi and Frank J. Fabozzi, Wiley, 2004.
    These notes are used for educational purposes.

## Principles of Calculus

I 
CHAPTER 4 
Principles of Calculus 
nvented in the seventeenth century independently by the British physi-
cist Isaac Newton and the German philosopher G.W. Leibnitz, (infini-
tesimal) calculus was a major mathematical breakthrough; it was to 
make possible the modern development of the physical sciences. Calcu-
lus introduced two key ideas:
 ■ The concept of instantaneous rate of change.
 ■ A framework and rules for linking together quantities and their instan-
taneous rates of change. 
Suppose that a quantity such as the price of a financial instrument 
varies as a function of time. Given a finite interval, the rate of change of 
that quantity is the ratio between the amount of change and the length 
of the time interval. Graphically, the rate of change is the steepness of 
the straight line that approximates the given curve.1 In general, the rate 
of change will vary as a function of the length of the time interval. 
What happens when the length of the time interval gets smaller and 
smaller? Calculus made the concept of infinitely small quantities precise 
with the notion of limit. If the rate of change can get arbitrarily close to 
a definite number by making the time interval sufficiently small, that 
number is the instantaneous rate of change. The instantaneous rate of 
change is the limit of the rate of change when the length of the interval 
gets infinitely small. This limit is referred to as the derivative of a func-
tion, or simply, derivative. Graphically, the derivative is the steepness of 
the tangent to a curve. 
Starting from this definition and with the help of a number of rules 
for computing a derivative, it was shown that the instantaneous rate of 
1 The rate of change should not be confused with the return on an asset, which is the 
asset’s percentage price change. 
91 

92 
The Mathematics of Financial Modeling and Investment Management 
change of a number of functions—such as polynomials, exponentials, 
logarithms, and many more—can be explicitly computed as a closed for-
mula. For example, the rate of change of a polynomial is another poly-
nomial of a lower degree. 
The process of computing a derivative, referred to as differentiation, 
solves the problem of finding the steepness of the tangent to a curve; the 
process of integration solves the problem of finding the area below a 
given curve. The reasoning is similar. The area below a curve is approx-
imated as the sum of rectangles and is defined as the limit of these sums 
when the rectangles get arbitrarily small. 
A key result of calculus is the discovery that integration and deriva-
tion are inverse operations: Integrating the derivative of a function 
yields the function itself. What was to prove even more important to the 
development of modern science was the possibility of linking together a 
quantity and its various instantaneous rates of change, thus forming dif-
ferential equations, the subject of Chapter 9. 
A solution to a differential equation is any function that satisfies it. 
A differential equation is generally satisfied by an infinite family of func-
tions; however, if a number of initial values of the solutions are 
imposed, the solution can be uniquely identified. This means that if 
physical laws are expressed as differential equations, it is possible to 
exactly forecast the future development of a system. For example, 
knowing the differential equations of the motion of bodies in empty 
space, it is possible to predict the motion of a projectile knowing its ini-
tial position and speed. It is difficult to overestimate the importance of 
this principle. The fact that most laws of physics can be expressed as 
relationships between quantities and their instantaneous rates of change 
prompted the physicist Eugene Wigner’s remark on the “unreasonable 
effectiveness of mathematics in the natural sciences.”2 
Mathematics has, however, been less successful in describing human 
artifacts such as the economy or financial markets. The problem is that 
no simple mathematical law can faithfully represent the evolution of 
observed quantities. A description of economic behavior requires the 
introduction of a certain amount of uncertainty in economic laws. 
Uncertainty can be represented in various ways. It can, for example, 
be represented with concepts such as fuzziness and imprecision or more 
quantitatively as probability. In economics, uncertainty is usually repre-
sented within the framework of probability. Probabilistic laws can be 
cast in two mathematically equivalent ways: 
2 Eugene Wigner, “The Unreasonable Effectiveness of Mathematics in the Natural 
Sciences,” Communications in Pure and Applied Mathematics 13, no. 1 (February 
1960). 

93
Principles of Calculus 
■ The evolution of probability distributions is represented through differ-
ential equations. This is the case within the framework of calculus.
 ■ The evolution of random phenomena is represented through direct 
relationships between stochastic processes. This is the case within the 
framework of stochastic calculus. 
Stochastic calculus has been adopted as the preferred framework in 
finance and economics. We will start with a review of the key concepts 
of calculus and then introduce the concepts of its stochastic evolution. 
SETS AND SET OPERATIONS 
The basic concept in calculus (and in the theory of probability) is that of 
a set. A set is a collection of objects called elements. The notions of both 
element and set should be considered primitive. Following a common 
convention, let’s denote sets with capital Latin or Greek letters: 
A,B,C,Ω… and elements with small Latin or Greek letters: a,b,ω. Let’s 
then consider collections of sets. In this context, a set is regarded as an 
element at a higher level of aggregation. In some instances, it might be 
useful to use different alphabets to distinguish between sets and collec-
tions of sets. 
Piling up sets and sets of sets is not as innocuous as it might seem; it 
is effectively the source of subtle and basic fundamental logical contra-
dictions called antinomies. Mathematics requires that a distinction be 
made between naive set theory, which deals with basic set operations, 
and axiomatic set theory, which deals with the logical structure of set 
theory. In working with calculus, we can stay within the framework of 
naive set theory and thus consider only basic set operations. 
Proper Subsets 
An element a of a set A is said to belong to the set A written as a ∈ A. If 
every element that belongs to a set A also belongs to a set B, we say that 
A is contained in B and write: A ⊂ B. We will distinguish whether A is a 
proper subset of B (i.e., whether there is at least one element that 
belongs to B but not to A) or if the two sets might eventually coincide. 
In the latter case we write A ⊆ B. 
For example, as explained in Chapter 2, in the United States there 
are indexes that are constructed based on the price of a subset of com-
mon stocks from the universe of all common stock in the country. There 
are three types of common stock (equity) indexes: 

94 
The Mathematics of Financial Modeling and Investment Management 
1. Produced by stock exchanges based on all stocks traded on the particu-
lar exchanges (the most well known being the New York Stock 
Exchange Composite Index). 
2. Produced by organizations that subjectively select the stocks included 
in the index (the most popular being the Standard & Poor’s 500). 
3. Produced by organizations where the selection process is based on an 
objective measure such as market capitalization. 
The Russell equity indexes, produced by Frank Russell Company, 
are examples of the third type of index. The Russell 3000 Index includes 
the 3,000 largest U.S. companies based on total market capitalization. It 
represents approximately 98% of the investable U.S. equity market. The 
Russell 1000 Index includes 1,000 of the largest companies in the Rus-
sell 3000 Index while the Russell 2000 Index includes the 2,000 smallest 
companies in the Russell 3000 Index. The Russell Top 200 Index 
includes the 200 largest companies in the Russell 1000 Index and the 
Russell Midcap Index includes the 800 smallest companies in the Rus-
sell 1000 Index. None of the indexes include non-U.S. common stocks. 
Let us introduce the notation: 
A 
= all companies in the United States that have issued common 
stock 
I3000 
= companies included in the Russell 3000 Index 
I1000 
= companies included in the Russell 1000 Index 
I2000 
= companies included in the Russell 2000 Index 
ITop200 = companies included in the Russell Top 200 Index 
IMicap 
= companies included in the Russell Midcap200 Index 
We can then write the following: 
I3000 ⊂ A 
(every company that is contained in the Russell 3000 
Index is contained in the set of all companies in the 
United States that have issued common stock) 
I1000 ⊂ I3000 
(the largest 1,000 companies contained in the Rus-
sell 1000 Index are contained in the Russell 3000 
Index) 
IMicap ⊂ I1000 
(the 800 smallest companies in the Russell Midcap 
Index are contained in the Russell 1000 Index) 
ITop200 ⊂ I1000 ⊂ I3000 ⊂ A 
IMicap ⊂ I1000 ⊂ I3000 ⊂ A 

95 
Principles of Calculus 
Throughout this book we will make use of the convenient logic sym-
bols ∀ and ∃ that mean respectively, “for any element” and “an element 
exists such that.” We will also use the symbol ⇒ that means “implies.” 
For instance, if A is a set of real numbers and a ∈ A, the notation ∀a: a 
< x means “for any number a smaller than x” and ∃a: a < x means 
“there exists a number a smaller than x.” 
Empty Sets 
Given a subset B of a set A, the complement of B with respect to A writ-
ten as BC is formed by all elements of A that do not belong to B. It is 
useful to consider sets that do not contain any elements called empty 
sets. The empty set is usually denoted by ∅. For example, using the Rus-
sell Indexes, the set of non-U.S. companies in the Russell 3000 Index 
whose stock is not traded in the United States is an empty set. 
Union of Sets 
Given two sets A and B, their union is formed by all individuals that 
belong to either A or B. This is written as C = A ∪ B. For example, 
I1000 ∪ I2000 = I3000 
(the union of the companies contained in 
the Russell 1000 Index and the Russell 
2000 Index is the set of all companies 
contained in the Russell 3000 Index) 
IMicap ∪ ITop200 = I1000 
(the union of the companies contained in 
the Russell Midcap Index and the Russell 
Top 200 Index is the set of all companies 
contained in the Russell 1000 Index) 
Intersection of Sets 
Given two sets A and B, their intersection is formed by all elements that 
belong to both A and B. This is written as C = A ∩ B. For example, let 
IS&P = companies included in the S&P 500 Index 
The S&P 500 is a stock market index that includes 500 widely held 
common stocks representing about 77% of the New York Stock Exchange 
market capitalization. (Market capitalization for a company is the product 
of the market value of a share and the number of shares outstanding.) 
Then 

96 
The Mathematics of Financial Modeling and Investment Management 
IS&P ∩ ITop200 = C 
(the stocks contained in the S&P 500 Index 
that are the largest 200 companies in the Rus-
sell Index) 
We can also write: 
I1000 ∩ I2000 = ∅ 
(companies included in both the Russell 2000 
and the Russell 1000 Index is the empty set since 
there are no companies that are in both indexes) 
Elementary Properties of Sets 
Suppose that the set Ω includes all elements that we are presently con-
sidering (i.e., that it is the total set). Three elementary properties of sets 
are given below:
 ■ Property 1. The complement of the empty set is the total set: 
ΩC = ∅, ∅C = Ω
 ■ Property 2. If A,B,C are subsets of Ω, then the distribution properties 
of union and intersection hold: 
A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) 
A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
 ■ Property 3. The complement of the union is the intersection of the 
complements and the complement of the intersection is the union of the 
complements: 
(B ∪ C)C = BC ∩ CC 
(B ∩ C)C = BC ∪ CC 
DISTANCES AND QUANTITIES 
Calculus describes the dynamics of quantitative phenomena. This calls 
for equipping sets with a metric that defines distances between elements. 
Though many results of calculus can be derived in abstract metric 
spaces, standard calculus deals with sets of n-tuples of real numbers. In 

97 
Principles of Calculus 
a quantitative framework, real numbers represent the result of observa-
tions (or measurements) in a simple and natural way. 
n-tuples 
An n-tuple, also called an n-dimensional vector, includes n components: 
(a1, a2, ..., an). The set of all n-tuples of real numbers is denoted by Rn . 
The R stands for real numbers.3 
For example, suppose the monthly rates of return on a portfolio in 
2002 are as shown below along with the actual return for the S&P 500 
(the benchmark index for the portfolio manager):4 
Month 
Portfolio 
S&P 500 
January
 1.10% 
–1.46% 
February
 1.37%
 1.93% 
March
 2.95%
 3.76% 
April
 5.78%
 6.06% 
May
 0.51%
 0.74% 
June
 7.32%
 7.09% 
July
 7.13%
 7.80% 
August
 1.47%
 0.66% 
September
 9.54% 
10.87% 
October
 7.32%
 8.80% 
November
 6.19%
 5.89% 
December 
–4.92% 
–5.88% 
Then the monthly returns rport for the portfolio can be written as a 12-
tuple and has the following 12 components: 
= 1.10% 1.37% 2.95% 5.78% 0.51% 7.32% ,
rport 
,
,
,
,
, 
7.13% 1.47% 9.54% 7.32% 6.19% , –4.92% 
,
,
,
, 
Similarly, the return rS&P on the S&P 500 can be expressed as a 12-
tuple as follows: 
3 Where the components of an n-tuple are only integers, the set of n-tuples is denoted 
by Zn , Z representing zahlen, which is German for integer. 
4 The monthly rate of return on the S&P 500 is computed as follows 
Dividends paid on all + Change in the index 
the stock in the index 
value for the month 
----------------------------------------------------------------------------------------------------------------------------- – 1 
Value of the index at the beginning of the period 

98 
The Mathematics of Financial Modeling and Investment Management 
rS&P = 
,
,
,
,
,
–1.46% 1.93% 3.76% 6.06% 0.74% 7.09% , 
7.80% 0.66% 10.87% 8.80% 5.89% , –5.88%
,
, 
,
, 
One can perform standard operations on n-tuples. For example, 
consider the portfolio returns in the two 12-tuples. The 12-tuple that 
expresses the deviation of the portfolio’s performance from the bench-
mark index is computed by subtracting from each component of the 
return 12-tuple from the corresponding return on the S&P 500. That is, 
–
rport rS&P 
1.10% 1.37% 2.95% 5.78% 0.51% 7.32% , 
= 
,
,
,
,
, 
7.13% 1.47% 9.54% 7.32% 6.19% , –4.92%
,
,
,
, 
–1.46% , 1.93% 3.76% 6.06% 0.74% 7.09% ,
– 
,
,
,
, 
7.80% 0.66% 10.87% 8.80% 5.89% , –5.88%
,
, 
,
, 
= 2.56% , –0.56%, –0.81% , –0.28%, –0.23% 0.23% ,
, 
,
,
–0.67% 0.81% , –1.33%, –1.48% , 0.30% 1.26% 
It is the resulting 12-tuple that is used to compute the tracking error of a 
portfolio—the standard deviation of the variation of the portfolio’s return 
from its benchmark index’s return described in Chapter 19. 
Coming back to the portfolio return, one can compute a logarithmic 
return for each month by adding 1 to each component of the 12-tuple 
and then taking the natural logarithm of each component. One can then 
obtain a geometric average, called the geometric return, by multiplying 
each component of the resulting vector and taking the 12th root. 
Distance 
Consider the real line R1 (i.e., the set of real numbers). Real numbers 
include rational numbers and irrational numbers. A rational number is 
one that can be expressed as a fraction, c/d, where c and d are integers 
and d ≠ 0. An irrational number is one that cannot be expressed as a 
fraction. Three examples of irrational numbers are 
2 ≅ 1.4142136 
Ratio between diameter and circumference 
= π ≅ 3.1415926535897932384626 
Natural logarithm = e ≅ 2.7182818284590452353602874713526 

99 
Principles of Calculus 
On the real line, distance is simply the absolute value of the difference 
between two numbers a
b
– 
which also can be written as 
(a
b)2 
– 
Rn is equipped with a natural metric provided by the Euclidean distance 
between any two points 
[(
d
a1, a2, …, a ), (b1, b2, …, b )] = ∑(ai – bi)2 
n
n 
Given a set of numbers A, we can define the least upper bound of 
the set. This is the smallest number s such that no number contained in 
the set exceeds s. The quantity s is called the supremum and written as s 
= supA. More formally, the supremum is that number, if it exists, that 
satisfies the following properties: 
∀a: a ∈ A, s ≥ a 
∀ε > 0, ∃a: s – a ≤ε  
The supremum need not to belong to the set A. If it does, it is called the 
maximum. 
Similarly, infimum is the greatest lower bound of a set A, defined as 
the greatest number s such that no number contained in the set is less 
than s. If infimum belongs to the set it is called the minimum. 
Density of Points 
A key concept of set theory with a fundamental bearing on calculus is 
that of the density of points. In fact, in financial economics we distin-
guish between discrete and continuous quantities. Discrete quantities 
have the property that admissible values are separated by finite dis-
tances. Continuous quantities are such that one might go from one to 
any of two possible values passing through every possible intermediate 
value. For instance, the passing of time between two dates is considered 
to occupy every possible instant without any gap. 
The fundamental continuum is the set of real numbers. A contin-
uum can be defined as any set that can be placed in a one-to-one rela-
tionship with the set of real numbers. Any continuum is an infinite non-
countable set; a proper subset of a continuum can be a continuum. It 
can be demonstrated that a finite interval is a continuum as it can be 
placed in a one-to-one relationship with the set of all real numbers. 

100 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 4.1 
Bernoulli’s Construction to Enumerate Rational Numbers 
1/1 
1/2 
1/3 
1/4 
2/1 
2/2 
2/3 
2/4 
3/1 
3/2 
3/3 
3/4 
4/1 
4/2 
4/3 
4/4 
The intuition of a continuum can be misleading. To appreciate this, 
consider that the set of all rational numbers (i.e., the set of all fractions 
with integer numerator and denominator) has a dense ordering, i.e., has 
the property that given any two different rational numbers a,b with a < 
b, there are infinite other rational numbers in between. However, ratio-
nal numbers have the cardinality of natural numbers. That is to say 
rational numbers can be put into a one-to-one relationship with natural 
numbers. This can be seen using a clever construction that we owe to 
the seventeenth century Swiss mathematician Jacob Bernoulli. 
Using Bernoulli’s construction, we can represent rational numbers 
as fractions of natural numbers arranged in an infinite two-dimensional 
table in which columns grow with the denominators and rows grow 
with the numerators. A one-to-one relationship with the natural num-
bers can be established following the path: (1,1) (1,2) (2,1) (3,1) (2,2) 
(1,3) (1,4) (2,3) (3,2) (4,1) and so on (see Exhibit 4.1). 
Bernoulli thus demonstrated that there are as many rational num-
bers as there are natural numbers. Though the set of rational numbers 
has a dense ordering, rational numbers do not form a continuum as they 
cannot be put in a one-to-one correspondence with real numbers. 
Given a subset A of Rn, a point a ∈ A is said to be an accumulation 
point if any sphere centered in a contains an infinite number of points 
that belong to A. A set is said to be “closed” if it contains all of its own 
accumulation points and “open” if it does not. 
FUNCTIONS 
The mathematical notion of a function translates the intuitive notion of a 
relationship between two quantities. For example, the price of a security is a 
function of time: to each instant of time corresponds a price of that security. 
Formally, a function f is a mapping of the elements of a set A into 
the elements of a set B. The set A is called the domain of the function. 
The subset R = f(A) ⊆ B of all elements of B that are the mapping of 
some element in A is called the range R of the function f. R might be a 
proper subset of B or coincide with B. 

101 
Principles of Calculus 
The concept of function is general: the sets A and B might be any two 
sets, not necessarily sets of numbers. When the range of a function is real 
numbers, the function is said to be a real function or a real-valued function. 
Two or more elements of A might be mapped into the same element 
of B. Should this situation never occur, that is, if distinct elements of A 
are mapped into distinct elements of B, the function is called an injection. 
If a function is an injection and R = f(A) = B, then f represents a one-to-
one relationship between A and B. In this case the function f is invertible 
and we can define the inverse function g = f –1 such that f(g(a)) = a. 
Suppose that a function f assigns to each element x of set A some ele-
ment y of set B. Suppose further that a function g assigns an element z of 
set C to each element y of set B. Combining functions f and g, an element 
z in set C corresponds to an element x in set A. This process results in a 
new function, function h, and that function takes an element in set A and 
assigns it to set C. The function h is called the composite of functions g 
and f, or simply a composite function, and is denoted by h(x) = g[f(x)]. 
VARIABLES 
In calculus one usually deals with functions of numerical variables. Some 
distinctions are in order. A variable is a symbol that represents any element 
in a given set. For example, if we denote time with a variable t, the letter t 
represents any possible moment of time. Numerical variables are symbols 
that represent numbers. These numbers might, in turn, represent the ele-
ments of another set. They might be thought of as numerical indexes which 
are in a one-to-one relationship with the elements of a set. For example, if 
we represent time over a given interval with a variable t, the letter t repre-
sents any of the numbers in the given interval. Each of these numbers in 
turn represents an instant of time. These distinctions might look pedantic 
but they are important for the following two reasons. 
First, we need to consider numeraire or units of measure. Suppose, 
for instance, that we represent the price P of a security as a function of 
time t: P = f(t). The function f links two sets of numbers that represent 
the physical quantities price and time. If we change the time scale or the 
currency, the numerical function f will change accordingly though the 
abstract function that links time and price will remain unchanged. 
Second, in probability theory we will have to introduce random vari-
ables which are functions from states of the world to real numbers and not 
from real numbers to real numbers. 
One important type of function is a sequence. A sequence is a mapping 
of the set of natural numbers into another set. For example a discrete-time, 
real-valued time series maps discrete instants of time into real numbers. 

102 
The Mathematics of Financial Modeling and Investment Management 
LIMITS 
The notion of limit is fundamental in calculus. It applies to both func-
tions and sequences. Consider an infinite sequence S of real numbers 
S ≡ (a1, a2, ..., ai,...) 
If, given any real number ε > 0, it is always possible to find a natural 
number i(ε ) such that 
i
i ε 
( )  implies
≥
ai – a 
ε 
< 
then we write 
lim a
= a 
n →∞ n 
and say that the sequence S tends to a when n tends to infinity, or that a 
is the limit of the sequence S. 
Two aspects of this definition should be noted. First, ε can be chosen 
arbitrarily small. Second, for every choice of ε the difference, in absolute 
value, between the elements of the sequence S and the limit a is smaller 
than ε for every index i above i(ε ). This translates the notion that the 
sequence S gets arbitrarily close to a as the index i grows. 
We can now define the concept of limit for functions. Suppose that a 
real function y = f(x) is defined over an open interval (a,b), i.e., an inter-
val that excludes its end points. If, given any real number ε > 0, it is 
always possible to find a positive real number r(ε ) such that 
x
c
– 
< r ε 
( )  implies y
d
– 
ε 
< 
then we write 
lim f x
( )  = d 
x → c 
and say that the function f tends to the limit d when x tends to c. 
These basic definitions can be easily modified to cover all possible 
cases of limits: infinite limits, limits from the left or from the right or 
finite limits when the variable tends to infinity. Exhibit 4.2 presents in 
graphical form these cases. Exhibit 4.3 lists the most common defini-
tions, associating the relevant condition to each limit. 

103 
Principles of Calculus 
EXHIBIT 4.2 
Graphical Presentation of Infinite Limits, Limits from the Left or 
Right, and Finite Limits 
Note that the notion of limit can be defined only in a continuum. In 
fact, the limit of a sequence of rational numbers is not necessarily a 
rational number. 
CONTINUITY 
Continuity is a property of functions, a continuous function being a 
function that does not make jumps. Intuitively, a continuous function 
might be considered one that can be represented through an uninter-
rupted line in a Cartesian diagram. Its formal definition relies on limits. 
A function f is said to be continuous at the point c if 
( ) = f c
lim f x
( )  
x →c 

104 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 4.3 
Most Common Definitions Associating the Relevant Condition to 
Each Limit 
The sequence tends to a finite 
limit 
The sequence tends to plus 
infinity 
The sequence tends to minus 
infinity 
Finite limit of a function 
Finite left limit of a function 
Finite right limit of a function 
Finite limit of a function when 
x tends to plus infinity 
Finite limit of a function when 
x tends to minus infinity 
Infinite limit of a function 
Infinite limit of a function 
when x tends to plus infinity 
lim a
= a 
∀ε > 0, ∃i(ε): |a  – a| < ε
n
n
∞ 
→ 
n 
for n > i(ε) 
lim a
= +∞
∀D > 0, ∃i(D): a  > D 
n
∞ 
→ 
n 
for n > i(ε) 
n
lim a
= –∞
∀D < 0, ∃i(D): a  < D
n
n
∞ 
→ 
n 
for n > i(ε) 
lim f x
( )  = d 
∀ε > 0, ∃r(ε): |f(x) – d| < ε 
x → c 
for |x – c| < r(ε) 
lim f x  
( )  = d 
∀ε > 0, ∃r(ε): |f(x) – d| < ε 
– 
x → c 
for |x – c| < r(ε), x < c 
lim f x
( )  = d 
∀ε > 0, ∃r(ε): |f(x) – d| < ε 
+ 
x → c 
for |x – c| < r(ε), x > c 
lim f x
( )  = d 
∀ε > 0, ∃R(ε) > 0: |f(x) – a| < ε 
x → +∞ 
for x > R(ε) 
lim f x
( )  = d 
∀ε > 0, ∃R(ε) > 0: |f(x) – a| < ε 
x → –∞ 
for x < –R(ε) 
lim f x
( )  = ∞
∀D > 0, ∃r(D): |f(x)| > D 
x → c 
for |x – c| < r(D) 
lim f x  
( )  = +∞
∀D > 0, ∃R(D): f(x) > D 
x → +∞ 
for x > r(D) 
This definition does not imply that the function f is defined in an inter-
val; it requires only that c be an accumulation point for the domain of 
the function f. 
A function can be right continuous or left continuous at a given 
point if the value of the function at the point c is equal to its right or left 
limit respectively. A function f that is right or left continuous at the 
point c can make a jump provided that its value coincides with one of 
the two right or left limits. (See Exhibit 4.4.) A function y = f(x) defined 
on an open interval (a,b) is said to be continuous on (a,b) if it is contin-
uous for all x ∈ (a,b). 
A function can be discontinuous at a given point for one of two rea-
sons: (1) either its value does not coincide with any of its limits at that 
point or (2) the limits do not exist. For example, consider a function f 
defined in the interval [0,1] that assumes the value 0 at all rational 
points in that interval, and the value 1 at all other points. Such a func-

105 
Principles of Calculus 
EXHIBIT 4.4 
Graphical Illustration of Right Continuous and Left Continuous 
tion is not continuous at any point of [0,1] as its limit does not exist at 
any point of its domain. 
TOTAL VARIATION 
Consider a function f(x) defined over a closed interval [a,b]. Then con-
sider a partition of the interval [a,b] into n disjoint subintervals defined 
by n + 1 points: a = x0 < x1 < ... < xn–1 < xn = b and form the sum 
n 
T = ∑
(
) – f xi
f
 
xi
( 
– 1) 
i = 1 
The supremum of the sum T over all possible partitions is called the 
total variation of the function f on the interval [a,b]. If the total varia-
tion is finite, the function f is said to have bounded variation or finite 
variation. Note that a function can be of infinite variation even if the 

106 
The Mathematics of Financial Modeling and Investment Management 
function itself remains bounded. For example, the function that assumes 
the value 1 on rational numbers and 0 elsewhere is of infinite variation 
in any interval, though the function itself is finite. 
Continuous functions might also exhibit infinite variation. The follow-
ing function is continuous but with infinite variation in the interval [0,1]: 
0 for x = 0 
 

( ) = 
π 
--
x
f x

xsinfor 0 
≤
< 
1 
 
x
 
DIFFERENTIATION 
Given a function y = f(x) defined on the open interval (a,b), consider its 
increments around a generic point x consequent to an increment h of the 
variable x ∈(a,b) 
∆y = f(x + h) – f(x) 
Consider now the ratio ∆y/h between the increments of the depen-
dent variable y and the independent variable x. Called the difference 
quotient, this quantity measures the average rate of change of y in some 
interval around x. For instance, if y is the price of a security and t is 
time, the difference quotient 
( 
( )
y t  + h) – y t
∆y = -----------------------------------
h 
represents the average price change per unit time over the interval 
[t,t+h]. The ratio ∆y/h is a function of h. We can therefore consider its 
limit when h tends to zero. 
If the limit 
( 
( )
f x  + h) – f x
x
f ′( ) = lim ------------------------------------
h →0 
h 
exists, we say that the function f is differentiable at x and that its deriv-
ative is f ′, also written as
df 
dy
------ or ------
dx 
dx 

107 
Principles of Calculus 
The derivative of a function represents its instantaneous rate of change. 
If the function f is differentiable for all x ∈ (a,b), then we say that f is 
differentiable in the open interval (a,b). 
Introduced by Leibnitz, the notation dy/dx has proved useful; it sug-
gests that the derivative is the ratio between two infinitesimal quantities 
and that calculations can be performed with infinitesimal quantities as 
well as with discrete quantities. When first invented, calculus was 
thought of as the “calculus of infinitesimal quantities” and was there-
fore called “infinitesimal calculus.” Only at the end of the nineteenth 
century was calculus given a sound logical basis with the notion of the 
limit.5 The infinitesimal notation remained, however, as a useful 
mechanical device to perform calculations. The danger in using the 
infinitesimal notation and computing with infinitesimal quantities is 
that limits might not exist. Should this be the case, the notation would 
be meaningless. 
In fact, not all functions are differentiable; that is to say, not all 
functions possess a derivative. A function might be differentiable in 
some domain and not in others or be differentiable in a given domain 
with the exception of a few singular points. A prerequisite for a function 
to be differentiable at a point x is that it is continuous at the point. 
However, continuity is not sufficient to ensure differentiability. This 
can be easily illustrated. Consider the Cartesian plot of a function f. 
Derivatives have a simple geometric interpretation: The value of the 
derivative of f at a point x equals the angular coefficient of the tangent 
of its plot in the same point (see Exhibit 4.5). A continuous function 
does not make jumps, while a differentiable function does not change 
direction by discrete amounts (i.e., it does not have cusps). A function 
can be continuous but not differentiable at some points. For example, 
the function y = x at x = 0 is continuous but not differentiable. How-
ever, there are examples of functions that defy visual intuition; in fact, it 
is possible to demonstrate that there are functions that are continuous 
in a given interval but never differentiable. One such example is the 
path of a Brownian motion which we will discuss in Chapter 8. 
Commonly Used Rules for Computing Derivatives 
There are rules for computing derivatives. These rules are mechanical rules 
that apply provided that all derivatives exist. The proofs are provided in all 
standard calculus books. The basic rules are: 
5 In the 1970s the mathematician Abraham Robinson reintroduced on a sound logi-
cal basis the notion of infinitesimal quantities as the basis of a generalized calculus 
called “nonstandard analysis.” See Abraham Robinson, Non-Standard Analysis 
(Princeton, NJ: Princeton University Press, 1996). 

108 
The Mathematics of Financial Modeling and Investment Management
EXHIBIT 4.5 
Geometric Interpretation of a Derivative 
d c
■ Rule 1: ------( ) = 0 , where c is a real constant. 
dx 
d 
■ Rule 2: ------(bxn ) = nbxn – 1 , where b is a real constant. 
dx 
d 
d
d 
■ Rule 3: ------(af x
( )) = a------f x
( ) , where a and b are
( ) + bg x
( ) + b------g x
dx 
dx
dx 
real constants. 
Rule 3 is called the rule of termwise differentiation and shows that dif-
ferentiation is a linear operation. 
Let’s apply the basic rules to the following function: 
k
y = a + b1x + b2x2 + b3x3 + ... + bkx
where a, b1, b2, b3, ..., bk are the constants. 

------
------
109 
Principles of Calculus 
The first term is just a and as per Rule 1 the derivative is zero. The 
derivative of b1x by Rule 2 is b1. For each term bnxn by Rule 2 the 
derivative is nbnxn–1. Thus, the derivative of 
b2x2
2b2x1
is  
b3x3
3b3x2 
is  
b4x4
4b4x3 
is  
etc. 
Therefore, the derivative of y is 
dy 
2 
n – 1 
------ = b1 + 2b2x 1 + 3b3x + 4b4x 3 + … + nb x
n
dx 
There is a special rule for a composite function. Consider a compos-
ite function: h(x) = f[g(x)]. Provided that h and g are differentiable at 
the point x and that f is derivable at the point s = g(x), then the follow-
ing rule, called the chain rule, applies: 
x
( ))g′( )
h′( ) = f ′(g x
x
( ) = f g x
h x
( ( )) 
df 
 
 
dh 

dg
------ = 

 
 
dx 


 
 
dg dx 
Exhibit 4.6 shows the sum rule, product rule, quotient rule, and 
chain rule for calculating derivatives in both standard and infinitesimal 
notation. In Exhibit 4.6 it is assumed that a,b are real constants (i.e., 
fixed real numbers), that f, g, and h are functions defined in the same 
domain, and that all functions are differentiable at the point x. Exhibit 
4.7 lists (without proof) a number of commonly used derivatives.
Given a function f(x), its derivative f ′(x) represents its instanta-
neous rate of change. The logarithmic derivative 
x
d
f ′( )
------ln P x
( ) = ------------
dx 
f x
( )  
for all x such that P(x) ≠0, represents the instantaneous percentage 
change. In finance, the function p = p(t) represents prices; its logarith-
mic derivative represents the instantaneous returns. 

110 
EXHIBIT 4.6 
Commonly Used Rules of Derivation
Function 
Standard Notation 
Infinitesimal Notation
Termwise dif-
h x
( ) + bg x
x
x
x
( ) = af x
( )
h′( ) = af ′( ) + bg′( )
or 
dh
df
bdg
------ = a------ +
------
ferentiation 
dx 
dx
dx 
Product rule 
h x
( )g x
x
x
( ) + f x
x
------ = ------
+ ------
( ) = f x
( )
h′( ) = f′( )g x
( )g′( )
or 
dh
df-g
fdg
dx
dx 
dx 
Quotient rule 
1
g′( )
or 
dh
1
dg
x
h x
x
( ) = ----------
h′( ) = – ------------------
------ = – ------------------------
( )  
(g x
( )) 2 dx
g x
( )) 2 
dx 
(g x
Chain rule 
h x
( ( ))
h′( ) = f ′(g x
x
------ = ------------
( ) = f g x
x
( ))g′( )
dh
df dg
dx 
dgdx 

------
-------------------
--
-----------
111 
x
Principles of Calculus 
EXHIBIT 4.7 
Commonly Used Derivatives 
f(x) 
xn 
α 
sin x 
cos x 
tan x 
ln x 
ex 
log (f(x)) 
df 
dx 
nxn–1 
α–1
ax
cos x 
–sin x 
1 
2 
cos ( )
x
1 
x 
ex 
f ′( )
x 
f x  
( )  
Domain of P 
R, x ≠0 if n < 0 
x > 0 
R 
R 
π
π 
π
π 
x
– -- + n-- <
< -- + n--
2
2 
2
2 
x > 0 
R 
f(x) ≠0 
Note: Where R denotes real numbers. 
Given a function y = f(x), its increments ∆f = f(x + ∆x) – f(x) can be 
approximated by 
f x
x
( )
∆ 
= f ′( )∆x
The quality of this approximation depends on the function itself. 
HIGHER ORDER DERIVATIVES 
Suppose that a function f(x) is differentiable in an interval D and its 
derivative is given by 
df x
( )
x
f′( ) = -------------
dx 
The derivative might in turn be differentiable. The derivative of a deriv-
ative of a function is called a second-order derivative and is denoted by 

112 
The Mathematics of Financial Modeling and Investment Management 
df x
( ) 
d2f x
d------------- 
( )  
dx  
x
f″( ) = ---------------- = -----------------------
dx
dx2 
Provided that the derivatives exist, this process can be iterated, pro-
ducing derivatives of any order. A derivative of order n is written in the 
following way: 
– 1 x
df n 
( ) 
d------------------------ 
f x
dxn – 1 
( ) x
d n ( )
f n ( ) = ----------------- = ---------------------------------
dx
dxn 
Application to Bond Analysis 
Two concepts used in bond portfolio management, duration and con-
vexity, provide an illustration of derivatives. A bond is a contract that 
provides a predetermined stream of positive cash flows at fixed dates 
assuming that the issuer does not default nor prepay the bond issue 
prior to the stated maturity date. If the interest rate is the same for each 
period, the present value of a risk-free bond has the following expres-
sion: 
C
C 
C
M
+
V = ------------------ + ------------------ + … + ------------------- , i = 1,...,N 
(1 + i)1 
(1 + i)2 
(1 + i)N 
If interest rates are different for each period, the previous formula 
becomes 
C
C 
C
M
+
V = --------------------- + --------------------- + … + ----------------------- , i = 1,...,N 
(1 + i1)1 
(1 + i2)2 
(1 + iN)N 
In Chapter 8, we introduce the concept of continuous compound-
ing. With continuous compounding, if the short-term interest rate is 
constant, the bond valuation formula becomes6 
6 If the short-term rate is variable: 
–∫
1
–∫
2 
–∫
N
i s
( ) s
d 
i s
( ) s
d 
i s  
( ) s
d 
+
V = Ce
 
0 
+ Ce 
0 
+ … + (C
M)e 
0 

113 
Principles of Calculus 
C
C 
C
M
+
V = ------ + ------ + … + ---------------
1i 
2i 
Ni 
e
e 
e 
Application of the First Derivative 
The sensitivity of the bond price V to a change in interest rates is given 
by the first derivative of V with respect to the interest rate i. The first 
derivative of V with respect to the interest rate i is called dollar dura-
tion. We can compute dollar duration in each case using the derivation 
formulas defined thus far. In the discrete-time case we can write 
dV i 
+
( )  
d  
C
C 
C
M  
-------------- = ---------------------- + ------------------ + … + ------------------- 
1
di 
di(1 + i)
(1 + i)2 
(1 + i)N 
d 
C 
d
C
M
+ 
= ---- ------------------ + … + ---- -------------------
di (1 + i)1 
di (1 + i)N 
d 
1 
d 
1
+
= C ---- ------------------ + … + (C
M)---- -------------------
di (1 + i)1 
di (1 + i)N 
We can use the quotient rule 
d 
1
1 
------ ---------
= – ------------f ' ( )
x
dx f x
x
( )  
f2( )  
to compute the derivatives of the generic summand as follows: 
d 
1
1 
1 
---- -----------------
= – ------------------- i(1 + i)i – 1 = –i------------------------
di (1 + i)i 
(1 + i)2i 
(1 + i)i + 1 
Therefore, the derivative of the bond value V with respect to the interest 
rates is 
dV 
–1 
( 
–N 
------- = –(1 + i)–1[C(1 + i)
+ 2C(1 + i)–2 + … + N C  + M)(1 + i)
] 
di 
Using a similar reasoning, we can slightly generalize this formula, 
allowing the interest rates to be different for each period. Call it the 
interest rate for period t. The sequence of values is called the yield 
curve. We will have more to say about the yield curve in Chapter 20. 

-------
--------------
114 
The Mathematics of Financial Modeling and Investment Management 
Now suppose that interest rates are subject to a parallel shift. In other 
words, let’s assume that the interest rate for period t is (it + x). If we 
compute the first derivative with respect to x for x = 0, we obtain 


dV i( )  
d
C
C 
C 

= ------------------------------------ + ------------------------------ + … + ---------------------------------
1
dx 
x = 0 
dx

(1 + i1 + x)
(1 + i2 + x)2 
(1 + iN + x)N 
x = 0 
–3 
(
= –[C(1 + i1)–2 + 2C(1 + i2)
+ … + N C  + M)(1 + iN)– N – 1] 
In this case we cannot factorize any term as interest rates are different in 
each period. Obviously, if interest rates are constant, the yield curve is a 
straight line and a change in the interest rates can be thought of as a 
parallel shift of the yield curve. 
In the continuous-time case, assuming that interest rates are con-
stant, the dollar duration is7 
[ 
–
– 
–Ni
+
dV 
d Ce  1i + Ce 2i + … + (C
M)e 
]
------- = ---------------------------------------------------------------------------------------------
di 
di 
–
– 
( 
–Ni 
= – 1Ce 1i – 2Ce 2i – … – N C  + M)e 
where we make use of the rule 
7 When interest rates are deterministic but time-dependent, the derivative dV/di is 
computed as follows. Assume that interest rates experience a parallel shift i(t) + x and 
compute the derivative with respect to x evaluated at x = 0. To do this, we need to 
compute the following derivative: 
–∫
t
( ) + x] s
d 
i s
d 
( ) s
d 
d –∫
t [i s
( ) s
d 
–∫
t x s
i s
0 
d 
–∫
t
0
0 
0 
d
------e 
= ------ e
e 
= e 
------(e –xt) 
dx 
dx 
dx 
–∫
t i s( ) s
d 
= –te –xte 
0 
–∫
t
–∫
t
d –∫
t [i s( ) + x] s
d 
i s( ) s
d 
i s( ) s
d 
–xt 
0
0 
0 
------e 
= –te 
e 
= –te 
x = 0
dx 
x = 0 
Therefore, we can write the following: 
–∫
1
–∫
2
–∫
N
i s
( ) s
d 
i s
( ) s
d 
i s
( ) s
d 
dV 
= – Ce 
0 
– 2Ce 
0 
– … – N C  + M)e 
0
( 
dx x = 0 
For i = constant we find again the formula established above. 

----------
115 
Principles of Calculus 
d
x
x 
------(
) = e
e 
dx 
Application of the Chain Rule 
The above formulas express dollar duration which is the derivative of 
the price of a bond with respect with the interest rate and which 
approximates price changes due to small parallel interest rate shifts. 
Practitioners, however, are more interested in the percentage change of a 
bond price with respect to small parallel changes in interest rates. The 
percentage change is the price change divided by the bond value: 
dV 1 
di V 
The percentage price change is approximated by duration, which is the 
derivative of a bond’s value with respect to interest rates divided by the 
value itself. Recall from the formulas for derivatives that the latter is the 
logarithmic derivative of a bond’s price with respect to interest rates: 
dV 1 
d(log V)
Duration = ---------- = --------------------
di V 
di 
Based on the above formulas, we can write the following formulas 
for duration: 
Duration for constant interest rates in discrete time: 
dV 1
1 
C 
2C 
N C  + M)
(
---------- = – -------------------- --------------- + ------------------ + … + --------------------------
di V 
V(1 + i) (1 + i)
(1 + i)2 
(1 + i)N 
Duration for variable interest rates in discrete time: 
dV 1
1 
C 
2C 
N C  + M)
(
---------- = – --- --------------------- + --------------------- + … + ------------------------------
dx V 
V (1 + i1)2 
(1 + i2)3 
(1 + iN)N + 1 

----------
---
116 
The Mathematics of Financial Modeling and Investment Management 
Duration for continuously compounding constant interest rate in dis-
crete time:8 
dV 1
1 
– 
( 
–Ni 
---------- = – ---[Ce –i + 2Ce 2i + … + N C  + M)e 
]
di V 
V 
We will now illustrate the chain rule of derivation by introducing 
the concept of effective duration. In Chapter 2, we described the differ-
ent features of bonds. The bond valuation we presented earlier is for an 
option-free bond. But when a bond has an embedded option, such as a 
call option as discussed in Chapter 2, it is more complicated to value. 
Similarly, the sensitivity of the value of a bond to changes in interest 
rates is more complicated to assess when there is an embedded call 
option. Intuitively, we know that the sensitivity of the value of a bond 
with an embedded option would be sensitive to not only how changes in 
interest rates affect the present value of the cash flows as shown above 
for an option-free bond, but also how they would affect the value of the 
embedded option. 
We will use the following notation to assess the sensitivity of a call-
able bond’s value (i.e., a bond with an embedded call option) to a 
change in interest rates. The value of an option-free bond can be decom-
posed as follows: 
= Vcb + Vco
Vofb
where 
= value of an option-free bond
Vofb 
= value of a callable bond
Vcb 
= value of a call option on the bond
Vco 
The above equation says that an option-free bond’s value depends 
on the sum of the value of a callable bond’s value and a call option on 
that option-free bond. The equation can be rewritten as follows: 
Vcb = Vofb – Vco 
8 The duration for continuously compounding variable interest rate in discrete time is 
dV 
di 
- 1 
V 
-
1 
V 
- Ce 
i s( )
0 
1∫
– 
2Ce 
i s( )
0 
2∫
– 
… 
N C  M
+
( 
)e 
i s( )
0 
N∫
– 
+ 
+ 
+
–
= 
s
d 
s
d 
s
d 

-------------- -----------
117 
Principles of Calculus 
That is, the value of a callable bond is found by subtracting the value of 
the call option from the value of the option-free bond. Both components 
on the right side of the valuation equation depend on the interest rate i. 
Using linearity to compute the first derivative of the valuation equation 
with respect to i and dividing both sides of the equation by the callable 
bond’s value gives 
dVcb 1 
dVofb 1 
dVco 1 
-------------------- = -------------- -------- – --------------------
di Vcb 
di Vcb 
di Vcb 
Multiplying the numerator and denominator of the right-hand side 
by the value of the option-free bond and rearranging terms gives 
dVcb 1 
dVofb 1 Vofb dVco 1 Vofb 
-------------------- = -------------- ---------------------- – ----------------------------------
di Vcb 
di Vofb Vcb 
di Vofb Vcb 
The above equation is the sensitivity of a callable bond’s value to 
changes in interest rates. That is, it is the duration of a callable bond, 
which we denote by DurCB.9 The component given by 
dVofb 1 
di Vofb 
is the duration of an option-free bond’s value to changes in interest 
rates, which we denote by Durofb. Thus, we can have 
Vofb dVco 1 Vofb
Durcb = Durofb ----------- – ----------------------------------
Vcb 
di Vofb Vcb 
Now let’s look at the derivative, which is the second term in the 
above equation. The change in the value of an option when the price of 
the underlying changes is called the option’s delta. In the case of an 
option on a bond, as explained above, changes in interest rates change 
the value of a bond. In turn, the change in the value of the bond changes 
the value of the embedded option. Here is where we see a function of a 
function and the need to apply the chain rule. That is, 
9 Actually, it is equal to –Durcb, but because we will be omitting the negative sign for 
the durations on the right-hand side, this will not affect our derivation. 

118 
The Mathematics of Financial Modeling and Investment Management 
i
f Vofb i
V
( ) = [ 
( )]
co 
This tells us that the value of the call option on an option-free bond 
depends on the value of the option-free bond and the value of the 
option-free bond depends on the interest rate. Now let’s apply the chain 
rule. We get 
i
dV
( )  
df dVofb
co 
------------------- = -------------- --------------
di
di 
dVofb 
The first term on the right-hand side of the equation is the change in 
the value of the call option for a change in the value of the option-free 
bond. This is the delta of the call option, ∆co. Thus, 
dV
( )  
dVofb
i
co 
------------------- = –∆
--------------
co
di 
di 
Substituting this equation into the equation for the duration and rear-
ranging terms we get 
Vofb
Durcb = Durofb -----------(1 – ∆
)
co
Vcb 
This equation tells us that the duration of the callable bond depends on 
the following three quantities. The first quantity is the duration of the 
corresponding option-free bond. The second quantity is the ratio of the 
value of the option-free bond to the value of the callable bond. The dif-
ference between the value of an option-free bond and the value of a call-
able bond is equal to the value of the call option. The greater (smaller) 
the value of the call option, the higher (lower) the ratio. Thus, we see 
that the duration of the callable bond will depend on the value of the 
call option. Basically, this ratio indicates the leverage effectively associ-
ated with the position. The third and final quantity is the delta of the 
call option. The duration of the callable bond as given by the above 
equation is called the option-adjusted duration or effective duration. 
Application of the Second Derivative 
We can now compute the second derivative of the bond value with 
respect to interest rates. Assuming cash flows do not depend on interest 

-----------------
-------
119 
Principles of Calculus 
rates, this second derivative is called dollar convexity. Dollar convexity 
divided by the bond’s value is called convexity. In the discrete-time fixed 
interest rate case, the computation of convexity is based on the second 
derivatives of the generic summand: 

 
d2
1 
d d 
1 
 
d 
1 
------- -----------------
= -------- ----------------- = ---- –t------------------------
t
di2 (1 + i)
didi (1 + i)t 
 
di 
(1 + i)t + 1 
 
d 
1 
1 
= –t ---- ------------------------
= t(1 + t)------------------------
di (1 + i)t + 1 
(1 + i)t + 2 
Therefore, dollar convexity assumes the following expression: 
d2 ( )  
d2 
C
C 
C
M
V i  
+ 
----------------- = ------- ------------------ + ------------------ + … + -------------------
1
di2 
di2 (1 + i)
(1 + i)2 
(1 + i)N 
d2
1 
d2
1
+
= C------- ------------------ + … + (C
M)------- -------------------
1 
N
di2 (1 + i) 
di2 (1 + i)
–4 
⋅
= [2C(1 + i)–3 + 2 3C(1 + i)
+ … 
( 
+
+ N N  + 1)(C
M)(1 + i) –(N + 2)] 
Using the same reasoning as before, in the variable interest rate case, 
dollar convexity assumes the following expression: 
d2V i( )  
3 
–4 
= [2C(1 + i1)–3 + 2 ⋅
⋅C(1 + i2)
+ … 
dx2 
x = 0 
( 
+
+ N N  + 1)(C
M)(1 + iN)– N – 2 ] 
This scheme changes slightly in the continuous-time case, where, 
assuming that interest rates are constant, the expression for convexity is10 
10 For variable interest rates this expression becomes 
( ) s
d 
i s  
( ) s
d 
i s
( ) s
d 
i s
dV 
0
0 
0
+
= 12Ce 
–∫
1
+ 22Ce 
–∫
2
+ … + N2(C
M)e 
–∫
N
dx x = 0 

120 
The Mathematics of Financial Modeling and Investment Management 
i 
–Ni
+
d2V
d2[Ce –i + Ce –2 + … + (C
M)e 
]
---------- = ---------------------------------------------------------------------------------------------
di2 
di2 
i 
–Ni
+
= 12 ⋅Ce –i + 22 ⋅Ce –2 + … + N2 ⋅(C
M)e 
where we make use of the rule 
d2 
x
e
---------(
) = ex 
dx2 
We can now write the following formulas for convexity: 
Convexity for constant interest rates in discrete time: 
dV2 1 
1
2C 
( ) 2
( 
+
3 ( )C 
N N  + 1)(C
M)
------------- = ----------------------- --------------- + -------------------- + … + ---------------------------------------------
di2 V
V(1 + i)2 (1 + i)
(1 + i)2 
(1 + i)N 
Convexity for variable interest rates in discrete time: 
d2V 1
1
2C 
( ) 2
( 
+
3 ( )C 
N N  + 1)(C
M)
------------- = --- --------------------- + --------------------- + … + ---------------------------------------------
dx2 V
V (1 + i1)3 
(1 + i2)4 
(1 + iN)N + 2 
Convexity for continuously compounding constant interest rate in dis-
crete time:11 
d2V 1
1 
–
–Ni
+
------------- = ---[Ce –i + 22Ce 2i + … + N2(C
M)e 
]
V
V
di2 
11 The convexity for continuously compounding variable interest rate in discrete time 
is 
( ) s
d 
i s
( ) s
d 
–∫
2i s
( ) s
d 
d2V 1
1 
–∫
1i s
+ 22Ce 
0
0
+
------------- = --- Ce 
0 
+ … + N2(C
M)e 
–∫
N 
V
V 
di2 

121 
Principles of Calculus 
TAYLOR SERIES EXPANSION 
An important relationship used in economics and finance theory to 
approximate how the value of a function, such as a price function, will 
change is the Taylor series expansion. We begin by establishing Taylor’s 
theorem. Consider a continuous function with continuous derivatives 
up to order n in the closed interval [a,b] and differentiable with contin-
uous derivatives in the open interval (a,b) up to order n + 1. It can be 
demonstrated that there exists a point ξ ∈(a,b) such that 
( ) a
f ″( )(b
a)2 
f n ( )(b
a)n 
– 
( ) = f a
a
– 
a
– 
f b
( ) + f ′( )(b
a) + --------------------------------- + … + ------------------------------------ + Rn
2! 
n! 
where the residual Rn can be written in either of the following forms: 
f (n + 1)( )(b
a)n + 1
ξ
– 
Lagrange’s form: R
= ---------------------------------------------------
n 
(n + 1)! 
ξ
–
f (n + 1)( )(b – ξ)n(b
a)
Cauchy’s form: R
= -------------------------------------------------------------
n 
n! 
In general, the point ξ ∈(a,b) is different in the two forms. This 
result can be written in an alternative form as follows. Suppose x and x0 
are in (a,b). Then, using Lagrange’s form of the residual, we can write 
( ) x
x
–
–
f″( )(x
x0)2 
f n ( )(x
x0)n 
( ) = f x0
x
–
f x
(
) + f′( )(x
x0) + ------------------------------------ + … + ----------------------------------------
2! 
n! 
f (n + 1) ξ
–
( )(x
x0)n + 1 
+ ------------------------------------------------------ 
(n + 1)! 
If the function f is infinitely differentiable, i.e., it admits derivatives 
of every order and if 
lim R
= 0 
n →∞ n 
the infinite series obtained is called a Taylor series expansion (or simply 
Taylor series) for f(x). If x0 = 0, the series is called a Maclaurin series. 

122 
The Mathematics of Financial Modeling and Investment Management 
Such series, called power series, generally converge in some interval, 
called interval of convergence, and diverge elsewhere. 
The Taylor series expansion is a powerful analytical tool. To appre-
ciate its importance, consider that a function that can be expanded in a 
power series is represented by a denumerable set of numbers even if it is 
a continuous function. Consider also that the action of any linear oper-
ator on the function f can be represented in terms of its action on pow-
ers of x. 
The Maclaurin expansion of the exponential and of trigonometric 
functions are given by: 
2 
n 
x 
x
x 
x
e = 1 +
+
 
----- + … + ----- + Rn
2! 
n! 
3
5 
(–1)nx 2n + 1 
x
x
sin x = x – ----- + ----- + … + ------------------------------ + Rn
3! 
5! 
(2n + 1)! 
2
4 
x
x 
(–1)nx 2n 
cos x = 1 – ----- + ----- + … + ---------------------- + Rn
2! 
4! 
(2n)! 
Application to Bond Analysis 
Let’s illustrate Taylor and Maclaurin power series by computing a sec-
ond-order approximation of the changes in the present value of a bond 
due to a parallel shift of the yield curve. This information is important 
to portfolio managers and risk managers to control the interest rate risk 
exposure of a position in bonds. In bond portfolio management, the first 
two terms of the Taylor expansion series are used to approximate the 
change in an option-free bond’s value when interest rates change. An 
approximation based on the first two terms of the Taylor series is called 
a second order approximation, because it considers only first and sec-
ond powers of the variable. 
We begin with the bond valuation equation, again assuming a single 
discount rate. We first compute dollar duration and convexity, i.e., the 
first and second derivatives with respect to x evaluated at x = 0, and we 
expand in Maclaurin power series. We obtain 
( ) = V 0
1
V x
( ) – (Dollar duration)x + --(Dollar convexity)x 2 + R3
2 
We can write this expression explicitly as: 

-------
-------------------------------
123 
Principles of Calculus 
C
C 
C
M
+
V x
( ) = ------------------ + ------------------ + … + ------------------- 
(1 + i)1 
(1 + i)2 
(1 + i)N 
(
+
C 
C 
N C  M)
– x ------------------ + ------------------ + … + --------------------------
(1 + i)2 
(1 + i)3 
(1 + i)N + 1 
1
2 
2C 
3 2  
( 
+
⋅
⋅C 
(N N + 1))(C
M)
+ --x ------------------ + ------------------- + … + --------------------------------------------------
2 
(1 + i)3 
(1 + i)4 
(1 + i)N + 2 
1 
3
3 2  
⋅
⋅
⋅C
⋅
⋅C 
4 3 2  
– ----------x --------------------------- + --------------------------- + … 
⋅ 
i ξ)4 
(1 + +
3 2
(1 + +  
i ξ)5 
( 
+
N N + 1)(N + 2)(C
M)
+ -----------------------------------------------------------------
i ξ)N + 3
(1 + +  
Asset managers, however, are primarily interested in percentage price 
change. We can now compute the percentage price change as follows: 
( )
V 0
∆V = V x – ( )  
V
V 0
( )  
(
+
C 
C 
N C  M)
= –x ------------------ + ------------------ + … + --------------------------
(1 + i)2 
(1 + i)3 
(1 + i)N + 1 
1
× -----------------------------------------------------------------------------------
C
C 
C
M
+ 
------------------ + ------------------ + … + -------------------
(1 + i)1 
(1 + i)2 
(1 + i)N 
1
2 
2 ⋅C 
3 2  
( 
+
⋅
⋅C 
N N + 1)(C
M)
+ --x 
------------------ + ------------------- + … + ---------------------------------------------
2 
(1 + i)3 
(1 + i)4 
(1 + i)N + 2 
1
× -----------------------------------------------------------------------------------------
C
C 
C
M
+ 
------------------ + ------------------ + … + -------------------
(1 + i)1 
(1 + i)2 
(1 + i)N 

----------
⋅
⋅
 
---------------------------
-----------------------------------------------------------------
------------------
------------------
-------------------
----------------------------------------------------------------------------------------
-------------------
124 
The Mathematics of Financial Modeling and Investment Management 
The first term in the square brackets on the right-hand side of the equa-
tion is the first approximation and is the approximation based on the 
duration of the bond. The second term in the square brackets on the 
right-hand side is the second derivative, the convexity measure, multi-
plied by one half. The third term is the residual. Its size is responsible 
for the quality of the approximation. 
The residual is proportional to the third power of the interest rate 
shift x. The term in the square bracket of the residual is a rather com-
plex function of C,M,N, and i. A rough approximation of this term is 
N(N + 1)(N + 2). In fact, in the case of zero-coupon bonds, i.e., C = 0, 
the residual can be written as 
1 
3 2
⋅ 
-x 3 
3 2  C 
1 i ξ
+ +
( 
)4 -
… 
N N  1
+
( 
) N 2
+
( 
) C
M
+
( 
) 
1 i ξ
+ +
( 
)N 3
+ 
-
+ 
+
– 
1 
C 
1 i
+
( 
)1 
C 
1 i
+
( 
)2 
… 
C
M
+ 
1 i
+
( 
)N -
+ 
+ 
+ 
-

(
1 
N N  + 1)(N + 2)M 
1
R3 = – ------------x 3 
 ---------------------------------------------------------------------------
× 
i
3
2
(1 + + ξ)N + 3 
 
M 
(1 + i)N 
(1 + i)N 
(
= N N  + 1)(N + 2)------------------------------------
i
(1 + + ξ)N + 3 
which is a third order polynomial in N. 
Therefore, the error of the second order approximation is of the 
order [1/(3 × 2)](xN)3. For instance, if x = 0.01 and N = 20 years, the 
approximation error is of the order 0.001. The following numerical 
example will clarify these derivations. 
In Chapter 2 we discussed the features of bonds. In our illustration 
to demonstrate how to use the Taylor series, we will use an option-free 
bond with a coupon rate of 9% that pays interest semiannually and has 
20 years to maturity. Suppose that the initial yield is 6%. In terms of 

125 
Principles of Calculus 
our bond valuation equation, this means C = $4.5, M = $100, and i = 
0.06. Substituting these values into the bond valuation equation, the
price of the bond is $134.6722. 
Suppose that we want to know the approximate percentage price 
change if the interest rate (i.e., i) increases instantaneously from 6% to 
8%. In the bond market, a change in interest rates is referred to in terms 
of basis points. One basis point is equal to 0.0001 and therefore 1 per-
centage point is 100 basis points. In our illustration we are looking at 
an instantaneous change in interest rates of 200 basis points. We will 
use the two terms of the Taylor expansion series to show the approxi-
mate percentage change in the bond’s value for a 200 basis point 
increase in interest rates. 
We do know what the answer is already. The initial value for this 
bond is $134.6722. If the interest rate is 8%, the value of this bond 
would be $109.8964. This means that the bond’s value declines by 
18.4%. Let’s see how well the Taylor expansion series using only two 
terms approximates this change. 
The first approximation is the estimate using duration. The duration 
for this bond is 10.66 found by using the formula above for duration. 
The convexity measure for this bond is 164.11 The change in interest 
rates, di, is 200 basis points. Expressed in decimal it is 0.02. The first 
term of the Taylor expansion series gives 
–10.66 × (0.02) = –0.2132 = –21.32% 
Notice that this approximation overestimates the actual change in 
value, which is –18.4% and means that the estimated new value for the 
bond is underestimated. 
Now we add the second approximation. The second term of the 
Taylor series gives 
¹₂(164.11) × (0.02)2 = 3.28% 
The approximate percentage change in the bond’s value found by using 
the first term of the Taylor series and the second term of the Taylor series 
is –21.32% + 3.28% = –18.0%. The actual percentage change in value is 
–18.4%. Thus the two terms of the Taylor series do an excellent job of 
approximating the percentage change in value. 
Let’s look at what would happen if the change in interest rates is a 
decline from 6% to 4%. The exact percentage change in value is +25.04% 
(from 134.6722 to 168.3887). Now the change in interest rates di is –0.02. 
Notice that the approximate change in value due to duration is the same 
except for a change in sign. That is, the approximate change based on the 

126 
The Mathematics of Financial Modeling and Investment Management 
first term (duration) is +21.32%. Since the percentage price change is 
underestimated, the new value of the bond is underestimated. The change 
due to the second term of the Taylor series is the same in magnitude and 
sign since when –0.02 is squared, it gives a positive value. Thus, the 
approximate change is 21.32% + 3.28% = 24.6%. Using the terms of the 
Taylor series does a good job of estimating the change in the bond’s value. 
We used a relatively large change in interest rates to see how well the 
two terms of the Taylor series approximate the percentage change in a 
bond’s value. For a small change in interest rates, duration does an effec-
tive job. For example, suppose that the change in interest rates is 10 basis 
points. That is, di is 0.001. For an increase in interest rates from 6% to 
6.1% the actual change in the bond’s value would be –1.06% ($134.6722 
to $133.2472). Using just the first term of the Taylor series, the approxi-
mate change in the bond’s value gives the precise change: 
–10.66 × 0.001 = –1.066% 
For a decrease in interest rates by 10 basis points, the result would be 
1.066%. 
What this illustration shows is that for a small change in a variable, 
a linear approximation does a good job of estimating the change in the 
value of the price function of a bond. A different interpretation, how-
ever, is possible. Note that in general convexity is computed as a num-
ber, which is a function of the term structure of interest rates as follows: 
Dollar convexity = [2C(1 + i1)–3 + 2 3
⋅
⋅C(1 + i2)–4 + … 
⋅( 
+
+ N
N
 
+ 1) ⋅(C
M)(1 + iN)– N – 2 ] 
This expression is a nonlinear function of all the yields. It is sensitive to 
changes of the curvature of the term structure. In this sense it is a mea-
sure of the convexity of the term structure. 
Let’s suppose now that the term structure experiences a change that 
can be represented as a parallel shift plus a change in slope and curva-
ture. In general both duration and convexity will change. The previous 
Maclaurin expansion, which is valid for parallel shifts of the term struc-
ture, will not hold. However, we can still attempt to represent the 
change in a bond’s value as a function of duration and convexity. In par-
ticular, we could represent the changes in a bond’s value as a linear 
function of duration and convexity. This idea is exploited in more gen-
eral terms by assuming that the term structure changes are a linear com-
bination of factors. 

127 
Principles of Calculus 
INTEGRATION 
Differentiation addresses the problem of defining the instantaneous rate 
of change, whereas integration addresses the problem of calculating the 
area of an arbitrary figure. Areas are easily defined for rectangles and 
triangles, and any plane figure that can be decomposed into these 
objects. While formulas for computing the area of polygons have been 
known since antiquity, a general solution of the problem was arrived at 
first in the seventeenth century, with the development of calculus. 
Riemann Integrals 
Let’s begin by defining the integral in the sense of Riemann, so called after 
the German mathematician Bernhard Riemann who introduced it. Con-
sider a bounded function y = f(x) defined in some domain which includes 
the interval [a,b]. Consider the partition of the interval [a,b] into n disjoint 
subintervals a = x0 < x1 < ... < xn–1 < xn = b, and form the sums: 
n 
SU = ∑fM(
)(xi – xi – 1)
n 
xi
i = 1 
xi
( )
∈ 
, 
[xi – 1, xi] and
where fM(
) = supf x
x 
n 
SL = ∑f (
)(xi – xi – 1)
n 
m xi
i = 1 
m xi
( )
∈ 
, 
[xi – 1, xi] .
where f (
) = inf f x
x 
Exhibit 4.8 illustrates this construction. Sn 
L
U , Sn are called, respec-
tively, the upper Riemann sum and lower Riemann sum. Clearly an infi-
U
L
nite number of different sums, Sn , Sn can be formed depending on the 
choice of the partition. Intuitively, each of these sums approximates the 
area below the curve y = f(x), the upper sums from above, the lower 
sums from below. Generally speaking, the more refined the partition the 
more accurate the approximation. 
U
L
Consider the sets of all the possible sums {
 }
 
and {
} for every
Sn 
Sn 
L
possible partition. If the supremum of the set {
} (which in general
Sn 
U
will not be a maximum) and the infimum of the set {
 }
 
(which in gen-
Sn 
eral will not be a minimum) exist, respectively, and if the minimum and 
the supremum coincide, the function f is said to be “Riemann integrable 
in the interval (a,b).” 
If the function f is Riemann integrable in [a,b], then 

128 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 4.8 
Riemann Sums 
( ) x
d = sup SL
{
 }
 
I = ∫ 
b
f
 
x
{
} = inf SU 
n
n 
a 
is called the proper integral of f on [a,b] in the sense of Riemann. 
An alternative definition of the proper integral in the sense of Rie-
mann is often given as follows. Consider the Riemann sums: 
n 
*
(
)(xi – x
Sn = ∑f xi 
x – 1) 
i = 1 
*
where xi is an arbitrary point in the interval [x1,xi–1]. Call ∆xi = (xi – 
xi–1) the length of the i-th interval. The proper integral I between a and 
b in the sense of Riemann can then be defined as the limit (if the limit 
exists) of the sums Sn when the maximum length of the subintervals 
tends to zero: 

129 
Principles of Calculus 
I = 
lim 
S
max∆xi →0 n 
In the above, the limit operation has to be defined as the limit for 
any sequence of sums Sn as for each n there are infinitely many sums. 
Note that the function f need not be continuous to be integrable. It 
might, for instance, make a finite number of jumps. However every 
function that is integrable must be of bounded variation. 
Properties of Riemann Integrals 
Let’s now introduce a number of properties of the integrals (we will 
state these without proof). These properties are simple mechanical rules 
that apply provided that all integrals exist. Suppose that a,b,c are fixed 
real numbers, that f,g,h are functions defined in the same domain, and 
that they are all integrable on the same interval (a,b). The following 
properties apply: 
Properties of Riemann Integrals
a 
Property 1 
f x
( ) x
d = 0
∫ a 
c 
b
c 
( ) x
d = ∫ a f x
b ( ) x
d , a
b
c
Property 2 
f x
( ) x
d + ∫f x
≤
≤
∫ a 
b 
b
b 
Property 3 h x = 
( )  βg x
( ) x
d = α 
f x
( ) x
d 
( )  αf x + 
( ) ⇒ 
h x
( ) x
d + β 
g x
∫ 
∫
∫
a 
a
a 
b 
b
b 
Property 4 
f′( )g x
( )g x
x
( ) x
d = f x
( )
– ∫f x
x
( )g′( ) x
d 
∫ 
a 
a
a 
■ Properties 1 and 2 establish that integrals are additive with respect to 
integration limits.
 ■ Property 3 is the statement of the linearity of the operation of integra-
tion.
 ■ Property 4 is the rule of integration by parts. 
Now consider a composite function: h(x) = f(g(x)). Provided that g is 
integrable on the interval (a,b) and that f is integrable on the interval corre-
sponding to all the points s = g(x), the following rule, known as the chain 
rule of integration, applies: 

130 
The Mathematics of Financial Modeling and Investment Management 
b
b
∫
( ) y
d = ∫
g –1( )f g x
x
f y
( ( ))g′( ) x
d 
–1 a
a
g ( )  
Lebesque-Stieltjes Integrals 
Most applications of calculus require only the integral in the sense of 
Riemann. However, a number of results in probability theory with a 
bearing on economics and finance theory can be properly established 
only in the framework of Lebesgue-Stieltjes integral. Let’s therefore 
extend the definition of integrals by introducing the Lebesgue-Stieltjes 
integral. 
The integral in the sense of Riemann takes as a measure of an inter-
val its length, also called the Jordan measure. The definition of the inte-
gral can be extended in the sense of Lebesgue-Stieltjes by defining the 
integral with respect to a more general Lebesgue-Stieltjes measure. 
Consider a non-decreasing, left-continuous function g(x) defined on a 
domain which includes the interval [xi – xi–1] and form the differences 
= g(xi) – g(xi–1). These quantities are a generalization of the concept 
mLi
of length. They are called Lebesgue measures. Suppose that the interval 
(a,b) is divided into a partition of n disjoint subintervals by the points 
a = x0 < x1 < ... < xn = b and form the Lebesgue-Stieltjes sums 
n 
S
= ∑f xi *
* ∈(xi,
(
)mLi , xi 
xi – 1)
n 
i = 1 
where xi * is any point in i-th subinterval of the partition. 
Consider the set of all possible sums {Sn}. These sums depend on the 
partition and the choice of the midpoint in each subinterval. We define 
the integral of f(x) in the sense of Lebesgue-Stieltjes as the limit, if the 
limit exists, of the Lebesgue-Stieltjes sums {Sn} when the maximum 
length of the intervals in the partition tends to zero. We write, as in the 
case of the Riemann integral: 
b 
( ) g x
I = ∫f
 
x d ( ) = lim Sn 
a 
The integral in the sense of Lebesgue-Stieltjes can be defined for a 
broader class of functions than the integral in the sense of Riemann. If f 
is an integrable function and g is a differentiable function, the two inte-
grals coincide. In the following chapters, all integrals are in the sense of 
Riemann unless explicitly stated to be in the sense of Lebesgue-Stieltjes. 

131 
Principles of Calculus 
INDEFINITE AND IMPROPER INTEGRALS 
In the previous section we defined the integral as a real number associ-
ated with a function on an interval (a,b). If we allow the upper limit b to 
vary, then the integral defines a function: 
x 
( ) = 
f u
( ) u
d 
F x
∫ a 
which is called an indefinite integral. 
Given a function f, there is an indefinite integral for each starting 
point. From the definition of integral, it is immediate to see that any two 
indefinite integrals of the same function differ only by a constant. In 
fact, given a function f, consider the two indefinite integrals: 
x
x 
( )du, Fb x
( )du
F ( ) = 
f u
( ) = ∫bf u
a x
∫ a 
If a < b, we can write 
x 
b
x 
F ( ) = 
f u
( ) u
d + ∫f u
( )
( ) u
d = 
f u
( ) u
d = constant + Fb x
a x
∫a 
∫a
b 
We can now extend the definition of proper integrals by introducing 
improper integrals. Improper integrals are defined as limits of indefinite 
integrals either when the integration limits are infinite or when the inte-
grand diverges to infinity at a given point. Consider the improper integral 
∞ 
f x
( ) x
d 
∫ a 
This integral is defined as the limit 
∞ 
x 
( ) x
d = lim 
f u
f x
( ) u
d 
∫ a
x →∞∫ a 
if the limit exists. Consider now a function f that goes to infinity as x 
approaches the upper integration limit b. We define the improper integral 
b 
f x
( ) x
d 
∫ a 

132 
The Mathematics of Financial Modeling and Investment Management 
as the left limit 
b
x 
( ) x
d = 
lim 
f u
( ) u
d
∫f x
– ∫a
a
x →b 
A similar definition can be established for the lower integration 
limit. Improper integrals exist only if these limits exist. For instance, the 
integral 
1 1 
1
1 
1 
 
-- x
d = lim – -----
= lim ----- – 1= ∞
∫0 x
x →0+ 
x 2 
x →0+
2 
 
0 
x 
does not exist. 
THE FUNDAMENTAL THEOREM OF CALCULUS 
The fundamental theorem of calculus shows that integration is the 
inverse operation of derivation; it states that, given a continuous func-
tion f, any of its indefinite integrals F is a differentiable function and the 
following relationship holds: 
x 
d
f
 
u
( ) u
d 
dF x
( )  ∫ a 
( )
-------------- = -------------------------- = f x
dx 
dx 
If the function f is not continuous, then the fundamental theorem 
still holds, but in any point of discontinuity the derivative has to be 
replaced with the left or right derivative dependent on whether or not 
the function f is left or right continuous at that point. 
Given a continuous function f, any function F such that 
dF x
( )  
( )
-------------- = f x
dx 
is called a primitive or an indefinite integral of the function f. It can be 
demonstrated that any two primitives of a function f differ only by a 
constant. Any primitive of a function f can therefore be represented 
generically as an indefinite integral plus a constant. 

--
------------
133 
Principles of Calculus 
As an immediate consequence of the fundamental theorem of calculus 
we can now state that, given a primitive F of a function f, the definite integral 
b 
f x
( )dx
∫ a 
can be computed as 
b 
( )dx = F b
( )
f x
( ) – F a
∫ a 
All three properties—the linearity of the integration operation, the chain 
rule, and the rule of integration by parts—hold for indefinite integrals: 
h x
( ) + bg x
( )dx = a f x
( )dx
( ) = af x
( ) ⇒ h x
( )dx + b g x
∫ 
∫
∫ 
∫ 
x
( )dx = f x
( ) – ∫f x
x
f ′( )g x
( )g x
( )g ′( )dx
( ) ⇒∫f y d 
( )g ′( )dx
y = g x
( ) y = f x
x
∫ 
The differentiation formulas established in the previous section can now 
be applied to integration. Exhibit 4.9 lists a number of commonly used 
integrals. 
EXHIBIT 4.9 
Commonly Used Integrals 
f(x) 
∫( )dx
Domain
f x
xn 
1 
n + 1 
n ≠–1, R, x ≠0 if n < 0 
------------x 
n + 1 
xα 
1 
α + 1 
x > 0 
------------ x 
α + 1 
sin x 
–cos x
R 
cos x 
sin x
R 
1 
log x
x > 0 
x 
ex 
ex 
R 
f ′( )  
log [f(x)] 
f(x) > 0
x 
f x  
( )  

134 
The Mathematics of Financial Modeling and Investment Management 
INTEGRAL TRANSFORMS 
Integral transforms are operations that take any function f(x) into 
another function F(s) of a different variable s through an improper inte-
gral 
∞ 
( , 
( )dx
( ) = 
G s x  )f x
F s
∫ 
–∞ 
The function G(s,x) is referred to as the kernel of the transform. The 
association is one-to-one so that f can be uniquely recovered from its 
transform F. For example, linear processes can be studied in the time 
domain or in the frequency domain: The two are linked by integral 
transforms. We will see how integral transforms are applied to several 
applications in finance. The two most important types of integral trans-
forms are the Laplace transform and Fourier transform. We discuss both 
in this section. 
Laplace Transform 
Given a real-valued function f, its one-sided Laplace transform is an 
operator that maps f to the function L(s) = L(f(x)) defined by the 
improper integral 
∞ 
( ) = L[f x
( )dx
L s
( )] = 
e –sxf x
∫ 
0 
if it exists. 
The Laplace transform of a real-valued function is thus a real-valued 
function. The one-sided transform is the most common type of Laplace 
transform used in physics and engineering. However in probability theory 
Laplace transforms are applied to density functions. As these functions are 
defined on the entire real axis, the two-sided Laplace transforms are used. 
In probability theory, the two-sided Laplace transform is called the 
moment generating function. The two-sided Laplace transform is defined 
by 
∞ 
( ) = L[f x
( )dx
L s
( )] = 
e –sxf x
∫ 
–∞ 

135 
Principles of Calculus 
if the improper integral exists. 
Laplace transforms “project” a function into a different function 
space, that of their transforms. Laplace transforms exist only for func-
tions that are sufficiently smooth and decay to zero sufficiently rapidly 
when x → ∞. The following conditions ensure the existence of the 
Laplace transform:
 ■ f(x) is piecewise continuous.
 ■ f(x) is of exponential order as x → ∞, that is, there exist positive real 
Keax
constants K, a, and T, such that f x
( ) ≤ 
, for x > T. 
Note that the above conditions are sufficient but not necessary for 
Laplace transforms to exist. It can be demonstrated that, if they exist, 
Laplace transforms are unique in the sense that if two functions have 
the same Laplace transform they coincide pointwise. As a consequence, 
the Laplace transforms are invertible in the sense that the original func-
tion can be fully recovered from its transform. In fact, it is possible to 
define the inverse Laplace transform as the operator L–1(F(s)) such that 
L–1[L(s)] = f(x) 
The inverse Laplace transform can be represented as a Bromwich 
integral, that is, an integral defined on a contour in the complex plane 
that leaves all singularities of the transform to the left: 
γ + i∞ 
1
(
) = --------
esxL s( ) s
d 
f X
∫
2πiγ – i∞ 
The following conditions ensure the existence of an inverse Laplace 
transform: 
lim F s( ) = 0 
s →∞ 
lim sF s( ) is finite 
s →∞ 
We will now list (without proof) some key properties of Laplace 
transforms; both the one-sided and two-sided Laplace transforms have 
similar properties. The Laplace transform is a linear operator in the 
sense that, if f,g are real-valued functions that have Laplace transforms 
and a,b are real-valued constants, then the following property holds: 

136 
The Mathematics of Financial Modeling and Investment Management 
∞ 
[ ( ) + bg x
( ) + bg x
L af x
( )] = 
e –sx(af x
( ))dx
∫ 
–∞ 
∞
∞ 
∫
–sx ( )dx + b
e–sxg x
= a
e
 f x
∫ 
( )dx
–∞ 
–∞ 
( )] + bL[g x
= aL[f x
( )] 
Laplace transforms turn differentiation, integration, and convolu-
tion (defined below) into algebraic operations. For derivatives the fol-
lowing property holds for the two-sided transform: 
L df x
( )  
( )]
-------------
= sL[f x
dx 
and 
L df x
( )  
( )] – f 0
-------------
= sL[f x
( )
dx 
for the one-sided transform. For higher derivatives the following for-
mula holds for the two-sided transform 
( ) x
n 
0
f(n – 1)( )
( )] – sn – 1f 0
L[f n ( )] = s L[f x
( ) – sn – 2f ' ( ) – … – 
0
An analogous property holds for integration for one-sided trans-
forms 
t 
L ∫f x
1 
( )] for the one-sided transform
( )  = --L[f x  
s 
0 
t 
L ∫f x
1 
( )] for the two-sided transform
( )  = --L[f x  
s 
0 
Consider now the convolution. Given two functions f and g, their 
convolution h(x) = f(x) ∗g(x) is defined as the integral 

137 
Principles of Calculus 
∞ 
h x
x
∫( – 
( )dt
( ) = (f ∗g)( ) = 
f x  t  )g t
–∞ 
It can be demonstrated that the following property holds: 
( )] = L[f ∗g] = L[f x
( )]
L[h x
( )]L[g x
As we will see in Chapter 9, when we cover differential equations, 
these properties are useful in solving differential equations, turning the 
latter into algebraic equations. These properties are also used in repre-
senting probability distributions of sums of variables. 
Fourier Transforms 
Fourier transforms are similar in many respects to Laplace transforms. 
Given a function f, its Fourier transform fˆ (ω) = F[f(x)] is defined as the 
integral 
fˆ ω
( )] = 
+∞ 
e –2πiωxf x
(
) = F[f x
∫ –∞ 
( )dx
if the improper integral exists, where i is the imaginary unity. The Fou-
rier transform of a real-valued function is thus a complex-valued func-
tion. For a large class of functions the Fourier transform exists and is 
unique, so that the original function, f, can be recovered from its trans-
form, fˆ . 
The following conditions are sufficient but not necessary for a func-
tion to have a forward and inverse Fourier transform:
∞ 
■ 
f x
( ) dx exists.
∫ –∞ 
■ The function f(x) is piecewise continuous.
 ■ The function f(x) has bounded variation. 
The inverse Fourier transform can be represented as: 
∞ 
f x
(
)] = 
e 2πiωxfˆ ω
( ) = F 
–1[fˆ ω
(
)dω
∫ 
–∞ 

----------------------------------
138 
The Mathematics of Financial Modeling and Investment Management 
Fourier transforms are linear operators. The Fourier transform of 
the convolutions is the product of Fourier transforms; the Fourier trans-
form of derivatives and integrals have similar properties to the Laplace 
transform. 
CALCULUS IN MORE THAN ONE VARIABLE 
The previous concepts of calculus can be extended in a multivariate envi-
ronment, that is, they can be extended to functions of several variables. 
Given a function of n variables, y = f(x1,...,x ), we can define n partial
n
derivatives 
∂f x1,
 ,
 
x )
(
…
n 
∂xi 
i = 1,...,n holding constant n – 1 variables and then using the definition 
for derivatives of univariate functions: 
(
…
f x1 …
,
 ,
 
xn) – f x1,
 ,
,
 ,
 
x )
∂f x1,
 ,
 
xn) 
(
,
 ,
 
xi + h …
(
… xi …
n
---------------------------------- = lim ---------------------------------------------------------------------------------------------------------------
∂xi 
h →0 
h 
Repeating this process we can define partial derivatives of any order. 
Consider, for example, the following function of two variables: 
2 
f x y  ) = e –(x 2 + σxy y )
( , 
+ 
Its partial derivatives up to order 2 are given by the following formulas 
2
∂f 
+ 
------ = –(2x + σy)e –(x 2 + σxy y ) 
∂x 
2
∂f 
+ 
----- = –(2y + σx)e –(x 2 + σxy y ) 
∂y 
2
2
∂2f 
–(x 2 + σxy y ) + (2x + σy)2 e –(x + σxy y 2)
+ 
-------- = – 2e 
+ 
∂x 2 

139 
Principles of Calculus 
2
2
∂2f 
–(x 2 + σxy + y ) + (2y + σx)2 e –(x 2 + σxy + y )
-------- = – 2e 
∂y 2 
2
2
∂2f 
–(x 2 + σxy + y )
------------ = (2x + σy)(2y + σx)e –(x 2 + σxy + y ) – σe 
∂x∂y 
In bond analysis, we can also compute partial derivatives in the case 
where each interest rate is not the same for each time period in the bond 
valuation formula. In that case, derivatives can be computed for each 
time period’s interest rate. When the percentage price sensitivity of a 
bond to a change in the interest rate for a particular time period is com-
puted, the resulting measure is called rate duration or partial duration.12 
The definition of the integral can be obtained in the same way as in 
the one variable case. The integral is defined as the limit of sums of 
multidimensional rectangles. Multidimensional integrals represent the 
ordinary concept of volume in three dimensions and n-dimensional 
hypervolume in more that three dimensions. A more general definition 
of integral that includes both the Riemann and the Riemann-Stieltjes as 
special cases, will be considered in the chapter on probability. 
SUMMARY 
We can now summarize our discussion of calculus as follows:
 ■ The infinitesimally small and infinitely large. Through the concept of 
the limit, calculus has rendered precise the notion of infinitesimally 
small and infinitely large.
 ■ Rules for computing limits. A sequence or a function tends to a finite 
limit if there is a number to which the sequence or the function can get 
arbitrarily close; a sequence or a function tends to infinity if it can 
exceed any given quantity. Starting from these simple concepts, rules 
for computing limits can be established and limits computed.
 ■ Derivatives. A derivative of a function is the limit of its incremental 
ratio when the interval tends to zero. Derivatives represent the rate of 
change of quantities.
 ■ Integrals. Integrals represent the area below a curve; they are the limit 
of sums of rectangles that approximate the area below the curve. More 
12 There is a technical difference between rate duration and partial duration but the 
difference is not important here. 

140 
The Mathematics of Financial Modeling and Investment Management 
in general, integrals can be used to represent cumulated quantities such 
as cumulated gains.
 ■ Integrals and derivatives. The fundamental theorem of calculus proves 
that integrals and derivatives are inverse operations, insofar as the 
derivative of the integral of a function returns the function. 
■ The derivative of the product of a constant and a function is the prod-
uct of the constant and the derivative of the function.
 ■ The integral of the product of a constant and a function is the product 
of the constant and the integral of the function.
 ■ The derivative and the integral of a sum of functions is the sum of 
derivatives or integrals.
 ■ Derivation and integration are linear operations.
 ■ The derivative of a product of functions is the derivative of the first 
function times the second plus the first function times the derivative of 
the second.
 ■ The derivative of a function of function is the product of outer function 
with respect to the inner function times the derivative of the inner func-
tion.
 ■ A derivative of order n of a function is defined as the function that 
results from applying the operation of derivation n times.
 ■ A function that is differentiable to any order at a given point a can be 
represented as a series of the powers of (x – a) times the n-th derivative 
at a times the reciprocal of n!; this expansion is called a Taylor series 
expansion.
 ■ Taylor series truncated to the first or second terms are called first and 
second order approximations, respectively.
 ■ Laplace and Fourier transforms of a function are the integral of that 
function times an exponential. 
■ Laplace and Fourier transforms are useful because they transform dif-
ferentiation and integration into algebraic operations, thereby provid-
ing a method for solving linear differential equations.
 ■ Differentiation and integration can be extended to functions of more 
than one variable.
 ■ A function of n variables has n first derivatives, n-square second deriv-
atives and so on. 


## Optimization

CHAPTER 7 
Optimization 
T
he concept of optimization is intrinsic to finance theory. The seminal 
work of Harry Markowitz demonstrated that financial decision-mak-
ing is essentially a question of an optimal trade-off between risk and 
returns. While Markowitz was developing his theory of investment in 
the 1950s, as we will see in Chapter 16, Georg Dantzig, the father of 
linear programming, was laying down the foundations of the modern 
computerized approach to optimization.1 
Purely mathematical solutions to optimization problems were proposed 
early in the history of calculus. In the eighteenth century, the French mathe-
matician Lagrange introduced a general methodology for finding the 
maxima or minima of a multivariate function subject to constraints; the 
Swiss-born mathematician Euler2 introduced the mathematics of the calculus 
of variations.3 Nevertheless, no matter how important from the concep-
tual point of view, optimization had limited practical applications in 
engineering, business, and financial planning until the recent develop-
ment of high-performance computing. 
In modern terminology, an optimization problem is called a mathe-
matical programming problem. From an analytical perspective, a static 
mathematical program attempts to identify the maxima or minima of a 
function f(x1,...,xn) of n real-valued variables, called the objective func-
tion, in a domain identified by a set of constraints. The latter might take 
the general form of inequalities gi(x1,...,xn) ≥ bi. Linear programming is 
the specialization of mathematical programming to instances where 
1 Dantzig and Markowitz worked together at the Rand Corporation in the 1950s. 
2 Euler was born in Basel, Switzerland, but spent a large part of his long career in 
Russia. 
3 The calculus of variations played a fundamental role in the development of modern 
science. 
201 

202 
The Mathematics of Financial Modeling and Investment Management 
both f and the constraints are linear. Quadratic programming is the spe-
cialization of mathematical programming to instances where f is a qua-
dratic function. The Markowitz mean-variance approach leads to a 
quadratic programming problem. 
A different, and more difficult, problem is the optimization of a 
dynamic process. In this case, the objective function depends on the entire 
realization of a process, which is often not deterministic but stochastic. 
Decisions might be taken at intermediate steps on the basis of information 
revealed up to that point. This is the concept of recourse, that is, revision of 
past decisions. This area of optimization is called stochastic programming. 
From an application perspective, mathematical programming is an 
optimization tool that allows the rationalization of many business or 
technological decisions. The computational tractability of the resulting 
analytical models is a key issue in mathematical programming. The sim-
plex algorithm, developed in 1947 by George Dantzig, was one of the 
first tractable mathematical programming algorithms to be developed 
for linear programming. Its subsequent successful implementation con-
tributed to the acceptance of optimization as a scientific approach to 
decision-making and initiated the field known as operations research. 
Optimization is a highly technical subject, which we will not fully 
develop in this chapter. Instead, our objective is to give the reader a gen-
eral understanding of the technology. We begin with an explanation of 
maxima or minima of a multivariate function subject to constraints. We 
then discuss the basic tools for static optimization: linear programming 
and quadratic programming. After introducing the idea of optimizing a 
process and defining the concepts of the calculus of variations and con-
trol theory, we briefly cover the techniques of stochastic programming.4 
MAXIMA AND MINIMA 
Consider a multivariate function f(x1,...,xn) of n real-valued variables. Sup-
pose that f is twice differentiable. Define the gradient of f, gradf, also written 
∇f, as the vector whose components are the first order partial derivatives of f 
∂f 
∂f  
(
grad[f x1, …, x )] = ∇f = --------, …, --------
n 
∂x1 
∂x  
n 
4 For a good introduction to stochastic programming, see, among others, J.R. Birge 
and F. Louveaux, Introduction to Stochastic Programming (Heidelberg: Springer, 
1997) and Peter Kall and Stein W. Wallace, Stochastic Programming (Chichester, 
West Sussex: Wiley, 1995). 

------------------
Optimization 
203 
Given a multivariate function f(x1,...,x ), consider the matrix
n
formed by the second order partial derivatives. This matrix is called the 
Hessian matrix and its determinant, denoted by H, is called the Hessian 
determinant (see Chapter 5 for definition of matrix and determinants): 
∂2f 
∂2f 
--------
· · ·  ------------------
2 
∂x1∂x
∂x1 
n 
·
· 
· 
H = 
·
· 
· 
∂2f 
· 
·
· 
∂2f 
· · ·  --------
∂x2
∂x1∂xn
n 
A point (a1,...,a ) is called a relative local maxima or a relative local
n
minima of the function f if the relationship 
f a1 + h1, …, x + h ) ≤ f a1, …, a ) ,
(
( 
h ≤ d > 0
n
n 
n 
or, respectively, 
f a1 + h1, …, x + h ) ≥ f a1, …, a ) ,
(
( 
h ≤ d > 0
n
n 
n 
holds for any real positive number d > 0. 
A necessary, but not sufficient, condition for a point (x1,...,x ) to be
n
a relative maximum or minimum is that all first order partial derivatives 
evaluated at that point vanish, that is, that the following relationship 
holds: 
∂f 
∂f  
--------…--------
(
grad[f x1, …, x )] =  
= (0, …, 0)
n 
∂x1 
∂xn 
A point where the gradient vanishes is called a critical point. 
A critical point can be a maximum, a minimum or a saddle point. 
For functions of one variable, the following sufficient conditions hold:
 ■ If the first derivative evaluated at a point a vanishes and the second 
derivative evaluated at a is positive, then the point a is a (relative) min-
imum. 

204 
The Mathematics of Financial Modeling and Investment Management
 ■ If the first derivative evaluated at a point a vanishes and the second 
derivative evaluated at a is negative, then the point a is a (relative) 
maximum.
 ■ If the first derivative evaluated at a point a vanishes and the second 
derivative evaluated at a also vanishes, then the point a is a saddle point. 
In the case of a function f(x,y) of two variables x,y, the following 
conditions hold:
 ■ If ∇f = 0 at a given point a and if the Hessian determinant evaluated at 
a is positive, then the function f has a relative maximum in a if fxx < 0 
or f
< 0 and a relative minimum if fxx > 0 or fyy > 0. Note that if the
yy 
Hessian is positive the two second derivatives fxx and fyy must have the 
same sign.
 ■ If ∇f = 0 at a given point a and if the Hessian determinant evaluated at 
a is negative, then the function f has a saddle point in a.
 ■ If ∇f = 0 at a given point a and if the Hessian determinant evaluated at 
a vanishes, then the point a is degenerate and no conclusion can be 
drawn in this case. 
The above conditions can be expressed in a more compact way if we 
consider the eigenvalues (see Chapter 5) of the Hessian matrix. If both 
eigenvalues are positive at a critical point a, the function has a local 
minimum at a; if both are negative the function has a local maximum; if 
they have opposite signs, the function has a saddle point; and if at least 
one of them is 0, the critical point is degenerate. Recall that the product 
of the eigenvalues is equal to the Hessian determinant. 
This analysis can be carried over in the three-dimensional case. In this 
case there will be three eigenvalues, all of which are positive at a local 
minimum and negative at a local maximum. A critical point of a function 
of three variables is degenerate if at least one of the eigenvalues of the 
Hessian determinant is 0 and has a saddle point if at least one eigenvalue 
is positive, at least one is negative, and none is 0. 
In higher dimensions, the situation is more complex and goes beyond 
the scope of our introduction to optimization. 
LAGRANGE MULTIPLIERS 
Consider a multivariate function f(x1,...,xn) of n real-valued variables. 
In the previous section we saw that, if the n variables are unconstrained, 
a local optimum of f can be found by solving the n equations: 

Optimization 
205 
∂f 
∂f  
∇f = --------, …, -------- = (0, …, 0)
∂x1 
∂x  
n 
Let’s now discuss how to find maxima and minima when the optimi-
zation problem has equality constraints. Suppose that the n variables 
(x1,...,xn) are not independent, but satisfy m < n constraint equations 
g1(x1,...,xn) = 0 
. 
. 
. 
gm(x1,...,xn) = 0 
These equations define, in general, an (n-m)-dimensional surface. 
For instance, in the case of two variables, a constraint g1(x,y) = 0 
defines a line. In the case of three variables, one constraint g1(x,y,z) = 0 
defines a two-dimensional surface while two constraints g1(x,y,z) = 0, 
g2(x,y,z) = 0 define a line in the three-dimensional space, and so on. 
Our objective is to find the maxima or minima of the function f for 
the set of points that also satisfy the constraints. It can be demonstrated 
that, under this restriction, the gradient ∇f of f need not vanish at the 
maxima or minima, but need only be orthogonal to the (n-m)-dimen-
sional surface described by the constraint equations. That is, the follow-
ing relationships must hold 
∇f = λT∇g , for some λ = (λ1, … λ )
, m 
or, in the usual notation 
m
∂f 
∂gj
------- = ∑λj ------- , i = 1,...,n 
∂xi 
j = 1 ∂xi 
The coefficients (λ1,...,λm) are called Lagrange multipliers. 
If we define the function 
m 
(
, m 
(
F x1, …, x , λ1, … λ ) = f x1, …, x ) – ∑λjgj
n
n 
j = 1 

206 
The Mathematics of Financial Modeling and Investment Management 
the above equations together may be written as 
∇F = 0 
or 
∂F 
∂F 
∂F 
∂F 
-------- = … = -------- = -------- = … = ---------- = 0 
∂x1 
∂x
∂λ1 
∂λ
n
m 
In other words, the method of Lagrange multipliers transforms a con-
strained optimization problem into an unconstrained optimization 
problem. The method consists in replacing the original objective func-
tion f to be optimized subject to the constraints g with another objective 
function 
m 
F = f – ∑λjgj 
j = 1 
to be optimized without constraints in the variables (x1,...,xn,λ1,...,λm). 
The Lagrange multipliers are not only a mathematical device. In many 
applications they have a useful physical or economic interpretation. 
NUMERICAL ALGORITHMS 
The method of Lagrange multiplers works with equality constraints, 
that is, when the solution is constrained to stay on the surface defined 
by the constraints. Optimization problems become more difficult if ine-
quality constraints are allowed. This means that the admissible solu-
tions must stay within the boundary defined by the constraints. In this 
case, approximate numerical methods are often needed. Numerical 
algorithms or “solvers” to many standard optimization problems are 
available in many computer packages. 
Linear Programming 
The general form for a linear programming (LP) problem is as follows. 
Minimize a linear objective function 
(f x1, …, x ) = c1x1 + … + c x
n 
n
n 
or, in vector notation, 

Optimization 
207 
f x1, …, x ) = c T x , c = (c1, ..., cn), x = (x1,...,xn)
( 
n 
subject to the constraints 
 
 
≤ 
+ … + ai nx
= bi , i = 1,2,...,m
ai, 1x1 
, 
n 
≥
 
or, in matrix notation 
 
Axb 
≤ 
=
 
≥
 
with additional sign restrictions such as xi ≤0, xi ≥0, or xi unrestricted 
in sign. 
The largest or smallest value of the objective function is called the 
optimal value, and a vector [x1 ... xn] that gives the optimal value con-
stitutes an optimal solution. The variables x1,...,xn are called the deci-
sion variables. The feasible region determined by a collection of linear 
inequalities is the collection of points that satisfy all of the inequalities. 
The optimal solution belongs to the feasible region. 
The above formulation has the general structure of a mathematical 
programming problem as outlined in the introduction to the chapter, 
but is characterized, in addition, by the fact that the objective function 
and the constraints are linear. 
LP problems can be transformed into standard form. An LP is said 
to be in standard form if (1) all constraints are equality constraints and 
(2) all the variables have a nonnegativity sign restriction. An LP prob-
lem in standard form can therefore be written as follows 
min cTx 
subject to constraints 
Ax = b  
 
x ≥0 
 
where A is an m × n matrix and b is an m-vector. 
Every LP can be brought into standard form through the following 
transformations: 

208 
The Mathematics of Financial Modeling and Investment Management 
1. An inequality constraint 
 
 
≤ 
+ … + ai nx
=
ai, 1x1 
, 
nbi 
≥
 
can be converted into an equality constraint through the introduction 
of a slack variable, denoted by S, or an excess variable, denoted by E, 
such that 
+ … + ai nx + S = bi
ai, 1x1 
, 
n 
or 
+ … + ai nx – E = bi
ai, 1x1 
, 
n 
2. A variable with negative sign restriction xi ≤0 can be substituted by 
xi = –xi ′ , xi ′ ≥0 while an unrestricted variable can be substituted by 
xi = xi ′ – xi ″ , xi ′, xi ″ ≥0 . 
There are two major techniques for solving an LP problem: the sim-
plex method and the interior-point method. The simplex method was 
discovered by Dantzig in the 1940s. Although the number of iterations 
may be exponential in the number of unknowns, the simplex method 
proved very useful and was unrivaled until the late 1980s. The exponen-
tial computational complexity of the simplex method led to a search for 
algorithms with better computational complexity features, in particular 
polynomial complexity. Khachiyan’s ellipsoid method—the first polyno-
mial-time algorithm—appeared in the 1970s. Most interior-point meth-
ods also have polynomial complexity. We will briefly describe both the 
simplex and the interior-point methods. 
The Simplex Algorithm 
Linear constraints identify a region called a simplex. The simplex 
method searches for optima on the vertices of the simplex. Recall from 
Chapter 5 on matrix algebra that the system Ax = b admits solutions if 
and only if rank [Ab] = rank A. We can assume without loss of general-
ity that rank A = m, otherwise we drop redundant equations. The feasi-
ble set is the set B of points that satisfy the constraints 
B = {x: Ax = b, x ≥0} 

Optimization 
209 
A feasible basic solution is a solution xˆ ≡( xˆ 1… xˆ ) ∈ B with the following
n 
additional properties. For each solution x consider the set I of indices such 
that the respective variables are strictly positive: I(x) ≡ (i: xi > 0), with x ∈ 
B. A feasible basic solution x is a feasible solution such that the set
I xˆ
{ Ai: i 
( )  
∈ 
} of columns of the matrix A are linearly independent. There-
I xˆ
fore, the components xˆ i , i 
( )  
∈ 
are the unique solutions of the system 
∑ Aixi = bi 
i 
( )  
∈ I xˆ
In fact, it is possible to demonstrate the following two important 
results:
 ■ If an LP has a bounded optimal solution, then there exists an extreme 
point, that is, a minimum or maximum, of the feasible (on one of the 
vertices) region, which is optimal. 
■ Extreme points of the feasible region of an LP correspond to basic fea-
sible solutions of the standard form representation of the problem. 
The first result implies that in order to obtain an optimal solution of 
an LP, we can constrain our search on the set of the extreme points of its 
feasible region. The second result implies that each of these points is 
determined by selecting a set of basic variables, with cardinality equal to 
the number of the constraints of the LP and the additional requirement 
that the (uniquely determined) values of these variables are nonnegative. 
This further implies that the set of extreme points for an LP with m con-
straints and N variables in its standard form representation can have only a 
finite number of extreme points. A naive approach to the problem would be 
to enumerate the entire set of extreme points and select one which minimizes 
the objective function over this set. However, for reasonably sized LP prob-
lems, the set of extreme points, even though finite, can become extremely 
large. Hence a more systematic approach to organize the search is needed. 
The simplex algorithm provides such a systematic approach. 
The algorithm starts with an initial basic feasible solution and tests its 
optimality. If an optimality condition is verified, then the algorithm termi-
nates. Otherwise, the algorithm identifies an adjacent feasible solution 
with a better objective value. The optimality of this new solution is tested 
again and the entire scheme is repeated until an optimal solution is found. 
The algorithm will terminate in a finite number of steps except in special 
pathological cases. In other words, the simplex algorithm starts from 
some initial extreme point and follows a path along the edges of the feasi-
ble region towards an optimal extreme point, such that all the intermedi-

210 
The Mathematics of Financial Modeling and Investment Management 
ate extreme points visited improve the objective function. Many standard 
optimization software packages contain the simplex algorithm. However, 
the simplex method exhibits exponential complexity. This means that the 
number of steps required for finding a solution grows exponentially with 
the number of unknowns. 
Interior-Point Methods 
The exponential complexity of the simplex method was behind the search 
for more computationally efficient methods. The 1980s saw the introduc-
tion of the first fast algorithms that generate iterates lying in the interior 
of the feasible set rather than on the boundary, as simplex methods do. 
The primal-dual class of interior-points algorithms is today considered 
the state-of-the-art technique for the practical solution of LP problems. 
Furthermore, this class of methods are also very amenable to theoretical 
analysis, and has opened up a new area of research within optimization. 
We will limit our brief discussion to this class of interior-point algorithms. 
Let’s begin by formulating the concept of duality. Every problem of 
the type 
maximize c1x1 + ... + cnxn 
subject to 
ai,1x1 + ... + ai,nxn ≥ bi, i = 1,2,...,m 
xj ≥ 0, j = 1,2,...,n 
has a dual problem 
minimize b1y1 + ... + bmym 
subject to 
y1a1,i + ... + ymam,i ≤ ci, i = 1,2,...,n 
yj ≥ 0, j = 1,2,...,m 
The original problem is called the primal problem. The primal-dual gap 
is the difference, if it exists, between the largest primal value and the small-
est dual value. The Strong Duality Theorem states that, if the primal prob-
lem has an optimal solution x* = (x1,...,xn), the dual also has an optimal 
solution y* = (y1,...,ym) and there is no primal-dual gap in the sense that 

Optimization 
211 
∑cixi = ∑bjyj 
i
j 
Interior-point algorithms generate iterates such that the duality gap is 
driven to zero, yielding a limiting point that solves the primal and dual 
linear programs. Commercial software packages that contain primal-
dual interior-point solvers are available. 
Quadratic Programming 
The general quadratic programming (QP) problem is a mathematical 
programming problem where the objective function is quadratic and 
constraints are linear as follows: 
( 
1
minimize f x1, …, x ) = c T x + --x TDx
n 
2 
where c = (c1,...,cn), x = (x1,...,xn) are n-vectors and D is a n×n matrix, 
subject to 
aix ≤ bi, i ∈ I 
aix = bi, i ∈ E 
x ≥ 0 
where b is an m-vector b = (b1,...,bm), A = [ai] is an m×n matrix, and I 
and E specify the nonequality and equality constraints respectively. 
The major classification criteria for these problems come from the 
characteristics of the matrix D as follow:
 ■ If the matrix D is positive semidefinite or positive definite, then the QP 
problem is a convex quadratic problem. For convex quadratic prob-
lems, every local maximum is a global maximum. Algorithms exist for 
solving this problem in polynomial time.5 The Markowitz mean-vari-
ance optimization problem is of this type.
 ■ If the matrix D is negative semidefinite, that is, its eigenvalues are all 
nonpositive, then the QP problem is a concave quadratic problem. All 
solutions lie at some vertex of the feasible regions. There are efficient 
algorithms for solving this problem. 
5 A problem is said to be solvable in polynomial time if the time needed to solve the 
problem scales with the number of variables as a polynomial. 

212 
The Mathematics of Financial Modeling and Investment Management
 ■ If the matrix D is such that the problem is bilinear, that is, the variables 
x can be split into two subvectors such that the problem is linear when 
one of the two subvectors is fixed, then the QP problem is bilinear. 
There are efficient algorithms for solving this problem.
 ■ If the matrix D is indefinite, that is, it has both positive and negative 
eigenvalues, then the QP problem is very difficult to solve. Depending 
on the matrix D, the complexity of the problem might grow exponen-
tially with the number of variables. 
Many modern software optimization packages have solvers for several 
of these problems. 
CALCULUS OF VARIATIONS AND OPTIMAL CONTROL THEORY 
We have thus far discussed the problem of finding the maxima or min-
ima of a function of n real variables. The solution to these problems is 
typically one point in a domain. This formulation is sufficient for prob-
lems such as finding the optimal composition of a portfolio for a single 
period of a finite horizon: An investment is made at the initial time and 
a payoff is received at the end of the period. However, many other 
important optimization problems in finance require finding an optimal 
function or path throughout time and over multiple periods. The mathe-
matical foundation for problems whose solution requires finding an 
optimal function or path of this kind is the calculus of variations. The 
basic setting of the calculus of variations is the following. An infinite set 
of admissible functions y = f(x), x0 ≤x ≤x1 is given. The end points 
might vary from curve to curve. Let’s assume all curves are differentia-
ble in the given interval [x0,x1]. A function of three variables F(x,y,z) is 
given such that the integral 
x1 
J
= ∫F  x y y
(
′ 
, ,  ) x
d 
y 
x0 
is well defined where y′ = dy/dx. The value of J depends on the curve y. The 
basic problem of the calculus of variations is to find the curve y = f(x) that 
minimizes J. This problem could be easily reformulated in many variables. 
One strategy for solving this problem is the following. Any solution 
y = f(x) has the property that, if we slightly displace the curve y, the 
integral assumes higher values. Therefore if we parameterize parallel 
displacements with a variable ε (denoting by {yε} the collection of all 

Optimization 
213 
such displacements from the optimal y such that y
= y ), the deriv-
ε ε = 0
ative of J with respect to ε must vanish for ε = 0. 
If we compute this derivative, we arrive at the following differential 
equation that must be satisfied by the optimal solution y 
( 
′ 
, ,  ) 
d ∂F x y y
∂F x y y
( 
′ 
, ,  )
---------------------------- – ---------------------------------- = 0 
∂y 
dx 
∂y′ 
First established by Leonard Euler in 1744, this differential equation is 
known as the Euler equation or the Euler-Lagrange equation.6 
Though fundamental in the physical sciences, this formulation of 
variational principles, is rarely encountered in finance theory. In finance 
theory, as in engineering, one is primarily interested in controlling the 
evolution of a process. For instance, in investment management, one is 
interested in controlling the composition of a portfolio in order to attain 
some objective. This is the realm of control theory. Let’s now define con-
trol theory in a deterministic setting. The following section will discuss 
stochastic programming—a computational implementation of control 
theory in a stochastic setting. 
Consider a dynamic process which starts at a given initial time t0 and 
ends at a given terminal time t1. Let’s suppose that the state of the system is 
described by only one variable x(t) called the state variable. The state of the 
system is influenced by a set of control variables that we represent as a vec-
tor u(t) = [u1(t),...,u (t)]. The control vector must lie inside a given subset of
n
a Euclidean r-dimensional space, U which is assumed to be closed and time-
invariant. An entire path of the control vector is called a control. A control 
is admissible if it stays in U and satisfies some regularity conditions. 
The dynamics of the state variables are specified through the differ-
ential equation 
dx 
( ) u t
------ = f1[x t
( )  
, 
] 
dt 
where f1 is assumed to be continuously differentiable with respect to 
both arguments. Suppose that the initial state is given but the terminal 
state is unrestricted. 
The problem to be solved is that of maximizing the objective func-
tional: 
6 Lagrange himself attributed the equation to Euler. 

214 
The Mathematics of Financial Modeling and Investment Management 
t1 
, ( ), u t
[ 
x t1
J
= ∫f0[t x  t
( )] t
d + S t1
(
)
 
, 
]
y 
t0 
A functional is a mapping from a set of functions into the set of real 
numbers; it associates a number to each function. The definite integral is 
an example of a functional. 
To solve the above optimal control problem, a useful strategy is to find 
a set of differential equations that must be satisfied by the control. Two 
major approaches for solving this problem are available: Bellman’s 
Dynamic Programming7 and Pontryagin’s Maximum Principle.8 The 
former approach is based on the fact that the value of the state variable at 
time t captures all the necessary information for the decision-making from 
time t and onward: The paths of the control vector and the state variable 
up to time t do not make any difference as long as the state variable at time 
t is the same. Bellmann showed how to derive from this observation a par-
tial differential equation that uniquely determines the control. Pontryagin’s 
Maximum Principle introduces additional auxiliary variables and derives 
differential equations via the calculus of variations that might be simpler to 
solve than those of Bellmann’s dynamic programming. 
STOCHASTIC PROGRAMMING 
The model formulations discussed thus far assume that the data for the 
given problem are known precisely. However, in financial economics, data 
are stochastic and cannot be known with certainty. Stochastic program-
ming can be used to make optimal decisions under uncertainty. The fun-
damental idea behind stochastic programming is the concept of stages 
and recourse. Recourse is the ability to take corrective action at a future 
time, that is, a decision stage, after a random event has taken place. 
To formulate problems of dynamic decision-making under uncer-
tainty as a stochastic program, we must first characterize the uncertainty 
in the model. The most common method is to formulate scenarios and to 
assign to each scenario a probability. A scenario is a complete path of 
data. To illustrate the problem of stochastic programming, let’s consider 
7 R. Bellman, Dynamic Programming (Princeton, NJ: Princeton University Press, 
1957). 
8 For a discussion of Pontryagin’s Maximum Principle see, for instance: E.B. Lee, and 
L. Marcus, Foundations of Optimal Control Theory (New York: John Wiley & 
Sons, 1967). 

Optimization 
215 
a two-stage program that seeks to minimize the cost of the first-period 
decision plus the expected cost of the second-period recourse decision. In 
Chapter 21 we provide an example related to bond portfolio manage-
ment. 
To cast the stochastic programming problem in the framework of LP, 
we need to create a deterministic equivalent of the stochastic problem. 
This is obtained introducing a new set of variables at each stage and tak-
ing expectations. The first-period direct cost is cTx while the recourse 
T
cost at the second stage is di yi where i = 1,...,S represents the different 
states. The first-period constraints are represented as Ax = b. At each 
stage, recourse is subject to some recourse function Tx + Wy = h. This 
constraint can be, for example, self-financing conditions in portfolio 
management. It should be noted that in stochastic programs the first-
period decision is independent of which second-period scenario actually 
occurs. This is called the nonanticipativity property. 
A two-stage problem can be formulated as follows 
S 
T
minimize c T x + ∑ pidi yi 
i = 1 
subject to 
Ax = b 
Tix + Wiyi = hi, i = 1,...,S 
x ≥ 0 
yi ≥ 0 
where S is the number of states and pi is the probability of each state 
such that 
S 
∑ pi = 1 
i = 1 
Notice that the nonanticipativity constraint is met. There is only one 
first-period decision whereas there are S second-period decisions, one 
for each scenario. In this formulation, the stochastic programming 
problem has been reduced to an LP problem. This formulation can be 
extended to any number of intermediate stages. 

216 
The Mathematics of Financial Modeling and Investment Management 
SUMMARY 
 ■ Optimizing means finding the maxima or minima of a function or of a 
functional.
 ■ Optimization is a fundamental principle of financial decision-making 
insofar as financial decisions are an optimal trade-off between risk and 
return.
 ■ The partial derivatives of an unconstrained function vanish at maxima 
and minima.
 ■ The maxima and minima of a function subject to equality constraints 
can be found equating to zero the derivatives of the corresponding 
Lagrangian function, which is the sum of the original function and of a 
linear combination of the constraints.
 ■ If constraints are linear inequalities, the problem can be solved numeri-
cally with the techniques of linear programming, quadratic program-
ming, or nonlinear mathematical programming.
 ■ There are two major solution strategies for a linear programming prob-
lem: the simplex method and the interior points method.
 ■ The simplex method searches for a solution by moving on the vertices 
of the simplex, that is, the area identified by the constraint equations.
 ■ The interior points method allows movement in the interior points of 
the area identified by the constraint equations.
 ■ Quadratic and, more in general, nonlinear optimization problems are 
more difficult to solve and more computationally intensive. 
■ Functionals are functions defined on other functions.
 ■ Calculus of variations deals with the problem of finding those func-
tions that optimize a functional.
 ■ Control theory deals with the problem of optimizing a functional by 
controlling some of the variables while other variables are subject to 
exogenous dynamics.
 ■ Bellmann’s Dynamic Programming and Pontryagin’s Maximum Princi-
ple are the key mathematical tools of control theory.
 ■ Multistage stochastic programming is a set of numerical techniques for 
finding the maxima and minima of a functional defined on a stochastic 
process.
 ■ Multistage stochastic optimization is based on formalizing the rules for 
recourse, that is, how decisions are made at each stage and on describ-
ing possible scenarios. 


## Financial Econometrics: Time Series

CHAPTER 11 
Financial Econometrics: 
Time Series Concepts, 
Representations, and Models 
I
n this chapter and the next we introduce models of discrete-time sto-
chastic processes (that is, time series) and address the general problem 
of estimating a model from a given set of empirical data. Recall from 
Chapter 6 that a stochastic process is a time-dependent random variable. 
Stochastic processes explored thus far, for instance Brownian motion and 
Itô processes, develop in continuous time. This means that time is a real 
variable that can assume any real value. In many applications, however, it 
is convenient to constrain time to assume only discrete values. A time 
series is a discrete-time stochastic process; that is, it is a collection of ran-
dom variables Xi indexed with the integers ...–n,...,–2,–1,0,1,2,...,n,... 
In finance theory, as in the practice of quantitative finance, both 
continuous-time and discrete-time models are used. In many instances, 
continuous-time models allow simpler and more concise expressions as 
well as more general conclusions, though at the expense of conceptual 
complication. For instance, in the limit of continuous time, apparently 
simple processes such as white noise cannot be meaningfully defined. 
The mathematics of asset management tends to prefer discrete-time pro-
cesses while the mathematics of derivatives tends to prefer continuous-
time processes. 
The first issue to address in financial econometrics is the spacing of 
discrete points of time. An obvious choice is regular, constant spacing. 
In this case, the time points are placed at multiples of a single time inter-
val: t = i∆t. For instance, one might consider the closing prices at the 
end of each day. The use of fixed spacing is appropriate in many appli-
283 

284 
The Mathematics of Financial Modeling and Investment Management 
cations. Spacing of time points might also be irregular but deterministic. 
For instance, week-ends introduce irregular spacing in a sequence of 
daily closing prices. These questions can be easily handled within the 
context of discrete time series. 
The diffusion of electronic transactions has made available high-fre-
quency data related to individual transactions. These data are randomly 
spaced as the intervals between two transactions are random variables. If 
one wants to consider randomly spaced time intervals, discrete-time 
models will not suffice; one must use either marked point processes (dis-
cussed briefly in Chapter 13) or continuous-time processes through the 
use of master equations. In this chapter and the next we discuss only 
time series at discrete and fixed intervals of time. Here we introduce con-
cepts, representations, and models of time series. In the next chapter we 
will discuss model selection and estimation. 
CONCEPTS OF TIME SERIES 
A time series is a collection of random variables Xt indexed with a dis-
crete time index t = ...–2,–1,0,1,2,.... The variables Xt are defined over a 
probability space (Ω,P,ℑ), where Ω is the set of states, P is a probability 
measure, and ℑ is the σ-algebra of events, equipped with a discrete fil-
tration {ℑt} that determines the propagation of information (see Chapter 
6). A realization of a time series is a countable sequence of real num-
bers, one for each time point. 
The variables Xt are characterized by finite-dimensional distributions 
(see the section on stochastic processes in Chapter 6) as well as by condi-
tional distributions, Fs(xs/ℑt), s > t. The latter are the distributions of the 
variable x at time s given the σ-algebra {ℑt} at time t. Note that condition-
ing is always conditioning with respect to a σ-algebra though (see Chap-
ter 6) we will not always strictly use this notation and will condition with 
respect to the value of variables, for instance: 
Fs(xs/xt), s > t 
If the series starts from a given point, initial conditions must be fixed. 
Initial conditions might be a set of fixed values or a set of random vari-
ables. If the initial conditions are not fixed values but random variables, 
one has to consider the correlation between the initial values and the ran-
dom shocks of the series. A usual assumption is that the initial conditions 
and the random shocks of the series are statistically independent. 

285 
Financial Econometrics: Time Series Concepts, Representations, and Models 
How do we describe a time series? One way to describe a time series 
is to determine the mathematical form of the conditional distribution. 
This description is called an autopredictive model because the model 
predicts future values of the series from past values. However, we can 
also describe a time series as a function of another time series. This is 
called an explanatory model as one variable is explained by another. 
The simplest example is a regression model where a variable is propor-
tional to another exogenously given variable plus a constant term. Time 
series can also be described as random fluctuations or adjustments 
around a deterministic path. These models are called adjustment mod-
els. Explanatory, autopredictive, and adjustment models can be mixed 
in a single model. The data generation process  (DGP) of a series is a 
mathematical process that computes the future values of the variables 
given all information known at time t. 
An important concept is that of a stationary time series. A series is 
stationary in the “strict sense” if all finite dimensional distributions are 
invariant with respect to a time shift. A series is stationary in a “weaker 
sense” if only the moments up to a given order are invariant with 
respect to a time shift. In this chapter, time series will be considered 
(weakly) stationary if the first two moments are time-independent. Note 
that a stationary series cannot have a starting point but must extend 
over the entire infinite time axis. Note also that a series can be strictly 
stationary (that is, have all distributions time-independent, but the 
moments might not exist). Thus a strictly stationary series is not neces-
sarily weakly stationary. 
A time series can be univariate or multivariate. A multivariate time 
series is a time-dependent random vector. The principles of modeling 
remain the same but the problem of estimation might become very diffi-
cult given the large numbers of parameters to be estimated. 
Models of time series are essential building blocks for financial fore-
casting and, therefore, for financial decision-making. In particular asset 
allocation and portfolio optimization, when performed quantitatively, 
are based on some model of financial prices and returns. This chapter 
lays down the basic financial econometric theory for financial forecasting. 
We will introduce a number of specific models of time series and of multi-
variate time series, presenting the basic facts about the theory of these 
processes. The next chapter will tackle the problem of model estimation 
from empirical data. We will consider primarily models of financial 
assets, though most theoretical considerations apply to macroeconomic 
variables as well. These models include:
 ■ Correlated random walks. The simplest model of multiple financial 
assets is that of correlated random walks. This model is only a rough 

286 
The Mathematics of Financial Modeling and Investment Management 
approximation of equity price processes and presents serious problems 
of estimation in the case of a large number of processes.
 ■ Factor models. Factor models address the problem of estimation in the 
case of a large number of processes. In a factor model there are correla-
tions only among factors and between each factor and each time series. 
Factors might be exogenous or endogenously modeled.
 ■ State-space models. State-space models describe factors as autoregres-
sive processes. They work in stationary and nonstationary environ-
ments. In the latter case, state-space models are equivalent to 
cointegrated models.
 ■ Cointegrated models. In a cointegrated model there are portfolios 
which are described by autocorrelated, stationary processes. All pro-
cesses are linear combinations of common trends that are represented 
by the factors. 
The above models are all linear. However, nonlinearities are at work 
in financial time series. One way to model nonlinearities is to break down 
models into two components, the first being a linear autoregressive model 
of the parameters, the second a regressive or autoregressive model of 
empirical quantities whose parameters are driven by the first. This is the 
case with most of today’s nonlinear models (e.g., ARCH/GARCH mod-
els), Hamilton models, and Markov switching models. 
There is a coherent modeling landscape, from correlated random 
walks and factor models to the modeling of factors, and, finally, the 
modeling of nonlinearities by making the model parameters vary. Before 
describing models in detail, however, let’s present some key empirical 
facts about financial time series. 
STYLIZED FACTS OF FINANCIAL TIME SERIES 
Most sciences are stratified in the sense that theories are organized on 
different levels. The empirical evidence that supports a theory is gener-
ally formulated in a lower level theory. In physics, for instance, quan-
tum mechanics cannot be formulated as a standalone theory but needs 
classical physics to give meaning to measurement. Economics is no 
exception. A basic level of knowledge in economics is represented by the 
so-called stylized facts. Stylized facts are statistical findings of a general 
nature on financial and economic time series; they cannot be considered 
raw data insofar as they are formulated as statistical hypotheses. On the 
other hand, they are not full-fledged theories. 

287 
Financial Econometrics: Time Series Concepts, Representations, and Models 
Amongst the most important stylized facts from the point of view of 
finance theory, we can mention the following:
 ■ Returns of individual stocks exhibit nearly zero autocorrelation at 
every lag.
 ■ Returns of some equity portfolios exhibit significant autocorrelation.
 ■ The volatility of returns exhibits hyperbolic decay with significant 
autocorrelation.
 ■ The distribution of stock returns is not normal for time horizons from 
a few minutes to a few days. The exact shape is difficult to ascertain 
but power law decay cannot be rejected.
 ■ The distribution of stock returns is close to a log-normal after a few 
days.
 ■ There are large stock price drops (that is, market crashes) that seem to 
be outliers with respect to both normal distributions and power law 
distributions.
 ■ Stock return time series exhibit significant cross-correlation. 
These findings are, in a sense, model-dependent. For instance, the 
distribution of returns, a subject that has received a lot of attention, can 
be fitted by different distributions. There is no firm evidence on the 
exact value of the power exponent, with alternative proposals based on 
variable exponents. The autocorrelation is model-dependent while the 
exponential decay of return autocorrelation can be interpreted only as 
absence of linear dependence. 
It is fair to say that these stylized facts set the stage for financial model-
ing but leave ample room for model selection. Financial time series seem to 
be nearly random processes that exhibit significant cross correlations and, 
in some instances, cross autocorrelations. The global structure of auto and 
cross correlations, if it exists at all, must be fairly complex and there is no 
immediate evidence that financial time series admit a simple DGP. 
One more important feature of financial time series is the presence 
of trends. Prima facie trends of economic and financial variables are 
exponential trends. Trends are not quantities that can be independently 
measured. Trends characterize an entire stochastic model. Therefore 
there is no way to arrive at an assessment of trends independent from 
the model. We will see later in this chapter that a number of models 
reject the assumption of exponential trends. Exponential trends are, 
however, a reasonable first approximation. 
Given the finite nature of world resources, exponential trends are 
not sustainable in the long run. However, they might still be a good 
approximation over limited time horizons. An additional insight into 
financial time series comes from the consideration of investors’ behav-

288 
The Mathematics of Financial Modeling and Investment Management 
ior. If investors are risk averse, as required by the theory of investment 
(see Chapter 16) then price processes must exhibit a trade off between 
risk and returns. The combination of this insight with the assumption of 
exponential trends yields market models with possibly diverging expo-
nential trends for prices and market capitalization. 
Again, diverging exponential trends are difficult to justify in the 
long run as they would imply that after a while only one entity would 
dominate the entire market. Some form of reversion to the mean or 
more disruptive phenomena that prevent time series to diverge exponen-
tially must be at work. 
In the following sections we will proceed to describe the theory and 
the estimation procedures of a number of market models that have been 
proposed. After introducing general concepts of the measure of depen-
dence between random variables, we will present the multivariate ran-
dom walk model and will analyze in some detail the correlation 
structure of real markets. We will introduce dimensionality reduction 
techniques and multifactor models. We will then proceed to introduce 
cointegration, autoregressive models, state-space models, ARCH/ 
GARCH models, Markov switching, and other nonlinear models. 
INFINITE MOVING-AVERAGE AND AUTOREGRESSIVE 
REPRESENTATION OF TIME SERIES 
There are several general representations (or models) of time series. This 
section introduces representations based on infinite moving averages or 
infinite autoregressions useful from a theoretical point of view. In the 
practice of econometrics, however, more parsimonious models such as 
the ARMA models (described in the next section) are used. Representa-
tions are different for stationary and nonstationary time series. Let’s 
start with univariate stationary time series. 
Univariate Stationary Series 
The most fundamental model of a univariate stationary time series is the 
infinite moving average of a white noise process. In fact, it can be dem-
onstrated that under mild regularity conditions, any univariate station-
ary causal time series admits the following infinite moving average 
representation: 
∞
∑
xt = 
+ m
hiεt
i
– 
i = 0 

289 
Financial Econometrics: Time Series Concepts, Representations, and Models 
where the hi are coefficients and εt–i is a one-dimensional zero-mean 
white-noise process. This is a causal time series as the present value of 
the series depends only on the present and past values of the noise pro-
cess. A more general infinite moving-average representation would 
involve a summation which extends from –∞to +∞. Because this repre-
sentation would not make sense from an economic point of view, we 
will restrict ourselves only to causal time series. 
A sufficient condition for the above series to be stationary is that the 
coefficients hi are absolutely summable: 
∞ 
∑
2 < ∞
hi 
i = 0 
Also, in general it can be demonstrated that given any stationary pro-
cess xi, if the sequence of coefficients hi is absolutely summable, then the 
process 
∞ 
yi = ∑hixi 
i = 1 
is stationary. 
The Lag Operator L 
Let’s now simplify the notation by introducing the lag operator L. The 
lag operator L is an operator that acts on an infinite series and produces 
another infinite series shifted one place to the left. In other words, the 
lag operator replaces every element of a series with the one delayed by 
one time lag: 
L xt
(
) = xt – 1 
The n-th power of the lag operator shifts a series by n places: 
Ln(
) =
xt
xt
n
– 
Negative powers of the lag operator yield the forward operator F, 
which shifts places to the right. The lag operator can be multiplied by a 
scalar and different powers can be added. In this way, linear functions 
of different powers of the lag operator can be formed as follows: 

290 
The Mathematics of Financial Modeling and Investment Management 
A L
(
) = 
N 
∑aiLi 
i = 1 
Note that if the lag operator is applied to a series that starts from a 
given point, initial conditions must be specified. 
Within the domain of stationary series, infinite power series of the 
lag operator can also be formed. In fact, as remarked above, given a sta-
tionary series, if the coefficients hi are absolutely summable, the series 
∞
∑hiLixt 
i = 1 
is well defined in the sense that it converges and defines another station-
ary series. It therefore makes sense to define the operator: 
∞
∑hiLi
A L
(
) = 
i = 1 
λ
Now consider the operator I – λ L. If
< 1 , this operator can be 
inverted and its inverse is given by the infinite power series, 
∞
∑
–1
λ iLi
( I – λ L ) 
= 
i = 1 
λ
∞
∑
iLi :
as can be seen by multiplying I – λL by the power series 
i = 1 
( I – λ L ) 
∞
∑λ iLi 
L0 = I
= 
i = 1 
On the basis of this relationship, it can be demonstrated that any opera-
tor of the type 
A L
(
) = 
N 
∑aiLi 
i = 1 
can be inverted provided that the solutions of the equation 

291 
Financial Econometrics: Time Series Concepts, Representations, and Models 
N 
∑
i 
aiz = 0 
i = 1 
have absolute values strictly greater than 1. The inverse operator is an 
infinite power series 
A –1 L
(
) =
ψ
∞
∑
iLi 
i = 1 
Given two linear functions of the operator L, it is possible to define 
their product 
M 
∑aiLi
A L
(
) = 
i = 1 
N 
∑biLi
B L
(
) = 
j = 1 
+ 
∑ 
M
N
i = 1 
piLi
(
) = A L
(
) =
P L
(
)B L
pi = 
i 
∑a rbi
r
– 
r = 1 
The convolution product of two infinite series in the lag operator is 
defined in a similar way 
∞
∑aiLi
A L
(
) = 
i = 0 
∞
∑biLi
B L
(
) = 
j = 0 

292 
The Mathematics of Financial Modeling and Investment Management 
∞
∑ckLk
C L
(
)
 B L
(
) = A L
(
)
 
× 
= 
k = 0 
ck = 
k 
∑a sbk
s
– 
s = 0 
We can define the left-inverse (right-inverse) of an infinite series as the oper-
ator A–1(L), such that A–1(L) × A(L) = I. The inverse can always be com-
puted solving an infinite set of recursive equations provided that a0 ≠0. 
However, the inverse series will not necessarily be stationary. A sufficient 
condition for stationarity is that the coefficients of the inverse series are 
absolutely summable. 
In general, it is possible to perform on the symbolic series 
H L
(
) = 
∞
∑hiLi 
i = 1 
the same operations that can be performed on the series 
H z
( ) = 
∞
∑hiz i 
i = 1 
with z complex variable. However operations performed on a series of 
lag operators neither assume nor entail convergence properties. In fact, 
one can think of z simply as a symbol. In particular, the inverse does not 
necessarily exhibit absolutely summable coefficients. 
Stationary Univariate Moving Average 
Using the lag operator L notation, the infinite moving average represen-
tation can be written as follows: 


 
∞
∑


hiLi ε + m 
H L
(
)ε
 + m
xt = 
= 
t 
t
 i = 0 
Consider now the inverse series: 

293 
Financial Econometrics: Time Series Concepts, Representations, and Models 
∞ 
Π L
(
)H L
(
) = ∑λiLi , Π L
(
) = I 
i = 1 
If the coefficients λi are absolutely summable, we can write 
∞ 
= Π L
–
εt 
(
)xt = ∑λiLixt
i
i = 1 
and the series is said to be invertible. 
Multivariate Stationary Series 
The concepts of infinite moving-average representation and of invert-
ibility defined above for univariate series carry over immediately to the 
multivariate case. In fact, it can be demonstrated that under mild regu-
larity conditions, any multivariate stationary causal time series admits 
the following infinite moving-average representation: 
∞ 
+ m
xt = ∑Hiεt
i
– 
i = 0 
where the Hi are n×n matrices, εt is a n-dimensional, zero-mean, white 
noise process with nonsingular variance-covariance matrix Ω, and m is an 
n-vector of constants. The coefficients Hi are called Markov coefficients. 
This moving-average representation is called the Wold representation. 
Wold representation states that any series where only the past influences 
the present can be represented as an infinite moving average of white noise 
terms. Note that, as in the univariate case, the infinite moving-average rep-
resentation can be written in more general terms as a sum which extends 
from –∞to +∞. However a series of this type is not suitable for financial 
modeling as it is not causal (that is, the future influences the present). 
Therefore we consider only moving averages that extend to past terms. 
Suppose that the Markov coefficients are an absolutely summable 
series: 
∞ 
+∞ 
< 
Hi 
i = 0 
∑ 
2
where H 
indicates the largest eigenvalue of the matrix HH′. Under 
this assumption, it can be demonstrated that the series is stationary and 

294 
The Mathematics of Financial Modeling and Investment Management 
that the (time-invariant) first two moments can be computed in the fol-
lowing way: 
∞
∑
cov xt
i = 0 
E[
] = m
xt
with the convention Hi = 0 if i < 0. Note that the assumption that the 
Markov coefficients are an absolutely summable series is essential, oth-
erwise the covariance matrix would not exist. For instance, if the Hi 
were identity matrices, the variances of the series would become infinite. 
As the second moments are all constants, the series is weakly sta-
tionary. We can write the time-independent autocovariance function of 
(
) 
HiΩ 
ΩHi
h
– 
′ 
xt
h
– 
= 
the series, which is a n× n matrix whose entries are a function of the lag 
h, as 
Γ 
Γx h
( ) = 
∞
∑HiΩ 
Ω
′
Hi
h
– 
i = 0 
Under the assumption that the Markov coefficients are an abso-
lutely summable series, we can use the lag-operator L representation 
and write the operator 
H L
(
) = 
∞
∑HiLi 
i = 0 
so that the Wold representation of a series can be written as 
xt = H L
(
)ε + m 
The concept of invertibility carries over to the multivariate case. A 
multivariate stationary time series is said to be invertible if it can be rep-
resented in autoregressive form. Invertibility means that the white noise 
process can be recovered as a function of the series. In order to explain 
the notion of invertible processes, it is useful to introduce the generating 
function of the operator H, defined as the following matrix power 
series: 

295 
Financial Econometrics: Time Series Concepts, Representations, and Models 
∞ 
H z
( ) = ∑Hizi 
i = 0 
It can be demonstrated that, if H0 = I, then H(0) = H0 and the 
power series H(z) is invertible in the sense that it is possible to formally 
derive the inverse series, 
∞ 
Π z
( ) = ∑Πizi 
i = 0 
such that 
( )H z
z
Π z
( ) = (Π × H)( ) = I 
where the product is intended as a convolution product. If the coeffi-
cients Πi are absolutely summable, as the process xt is assumed to be 
stationary, it can be represented in infinite autoregressive form: 
(
)(xt – m) =
Π L
εt 
In this case the process xt is said to be invertible. 
From the above, it is clear that the infinite moving average represen-
tation is a more general linear representation of a stationary time than 
the infinite autoregressive form. A process that admits both representa-
tions is called invertible. 
Nonstationary Series 
Let’s now look at nonstationary series. As there is no very general model 
of nonstationary time series valid for all nonstationary series, we have 
to restrict somehow the family of admissible models. Let’s consider a 
family of linear, moving-average, nonstationary models of the following 
type: 
t 
+ h t
–
xt = ∑Hiεt
i
( )z–1 
i = 0 
where the Hi are left unrestricted and do not necessarily form an abso-
lutely summable series, h(t) is deterministic, and z–1 is a random vector 
called the initial conditions, which is supposed to be uncorrelated with 

296 
The Mathematics of Financial Modeling and Investment Management 
the white noise process. The essential differences of this linear model 
with respect to the Wold representation of stationary series are:
 ■ The presence of a starting point and of initial conditions.
 ■ The absence of restrictions on the coefficients.
 ■ The index t which restricts the number of summands. 
The first two moments of a linear process are not constant. They can be 
computed in a way similar to the infinite moving average case: 
t 
cov(xtxt
h) = ∑HiΩH' 
+ h t
( )h′ 
i
h
( )var z
–
– 
i = 0 
xt
( )E[ ]
E[
] = mt = h t
z
Let’s now see how a linear process can be expressed in autoregres-
sive form. To simplify notation let’s introduce the processes ε˜ t and x˜ t 
t
and the deterministic series h˜ ( ) defined as follows: 
ε˜ t = 
εt if t > 0 
x˜ t = 
xt if t > 0 
h˜ ( ) = 
ht if t > 0 
t
0 if  t < 0 
0 if  t < 0 
0 if  t < 0 
It can be demonstrated that, due to the initial conditions, a linear pro-
cess always satisfies the following autoregressive equation: 
Π L
εt 
(
)h × ( )z–1
(
)xt =
+ Π L
t
A random walk model 
t 
xt = xt – 1 + εt = εt + ∑εt
i
– 
i = 1 
is an example of a linear nonstationary model. 
The above linear model can also represent processes that are nearly 
stationary in the sense that they start from initial conditions but then 
converge to a stationary process. A process that converges to a station-
ary process is called asymptotically stationary. 
We can summarize the previous discussion as follows. Under mild 
regularity conditions, any causal stationary series can be represented as 

297 
Financial Econometrics: Time Series Concepts, Representations, and Models 
an infinite moving average of a white noise process. If the series can also 
be represented in an autoregressive form, then the series is said to be 
invertible. Nonstationary series do not have corresponding general rep-
resentations. Linear models are a broad class of nonstationary models 
and of asymptotically stationary models that provide the theoretical 
base for ARMA and state-space processes that will be discussed in the 
following sections. 
ARMA REPRESENTATIONS 
The infinite moving average or autoregressive representations of the pre-
vious section are useful theoretical tools but they cannot be applied to 
estimate processes. One needs a parsimonious representation with a 
finite number of coefficients. Autoregressive moving average (ARMA) 
models and state-space models provide such representation; though 
apparently conceptually different, they are statistically equivalent. 
Stationary Univariate ARMA Models 
Let’s start with univariate stationary processes. An autoregressive pro-
cess of order p – AR(p) is a process of the form: 
+ a1xt – 1 + … + aPx –
xt 
t
P = εt 
which can be written using the lag operator as 
p
(
)x = (1 + a1L + … + aPL )xt = xt + a1Lx + … + aPL xt
P = εt
A L
t 
p
t 
– 
Not all processes that can be written in autoregressive form are sta-
tionary. In order to study the stationarity of an autoregressive process, 
consider the following polynomial: 
( ) = 1 + a1z + … + a
A z
Pzp 
where z is a complex variable. 
The equation 
A z
p
( ) = 1 + a1z + … + aPz
= 0 
is called the inverse characteristic equation. It can be demonstrated that 
if the roots of this equation, that is, its solutions, are all different from 1 

298 
The Mathematics of Financial Modeling and Investment Management 
in modulus (that is, the roots do not lie on the unit circle), then the 
operator A(L) is invertible and admits the inverse representation: 
+∞ 
+∞ 
xt = A– 1(
)ε = ∑λiε
, with ∑ 
+∞ 
< 
L
t 
t
i
– 
λi 
i
– 
= ∞ 
i
– 
= ∞ 
In addition, if the roots are all strictly greater than 1 in modulus, then 
the representation only involves positive powers of L: 
+∞ 
+∞ 
xt = A– 1(
)ε = ∑λiε
, with ∑ 
+∞ 
< 
L
t 
t
i
– 
λi 
i
– 
= ∞ 
i = 0 
We can therefore say that, if the roots of the inverse characteristic equa-
tion of an autoregressive process are all strictly greater than 1 in modu-
lus (that is, they lie outside the unit circle), then the process is invertible 
as it admits a causal infinite moving average representation. 
In order to avoid possible confusion, note that the solutions of the 
inverse characteristic equation are the reciprocal of the solution of the 
characteristic equation defined as 
A z
p
( ) = z + a1zp – 1 + … + a
= 0
P 
Therefore an autoregressive process is invertible with an infinite moving 
average representation that only involves positive powers of the opera-
tor L if the solutions of the characteristic equation are all strictly 
smaller than 1 in absolute value. This is the condition of invertibility 
often stated in the literature. 
Let’s now consider finite moving-average representations. A process 
is called a moving average process of order q – MA(q) if it admits the 
following representation: 
xt = (1 + b1L + … + bPLq)ε = εt + b1ε
+ … + bPεt
q
–
t
t – 1 
In a way similar to the autoregressive case, if the roots of the equation 
B z
q
( ) = 1 + b1z + … + bqz
= 0 
are all different from 1 in modulus, then the MA(q) process is invertible 
and, therefore, admits the infinite autoregressive representation: 

299 
Financial Econometrics: Time Series Concepts, Representations, and Models 
+∞ 
+∞ 
– 
εt = B 1(
)ε = ∑πiε
, with ∑ 
+∞ 
< 
L
t 
t
i
– 
πi 
i
– 
= ∞ 
i = 0 
In addition, if the roots of B(z) are strictly greater than 1 in modulus, 
then the autoregressive representation only involves past values of the 
process: 
+∞ 
+∞ 
– 
εt = B 1(
)ε = ∑πiε
, with ∑ 
+∞ 
< 
L
t 
t
i
– 
πi 
i = 0 
i = 0 
As in the previous case, if one considers the characteristic equation, 
B z
q + b1zq – 1
( ) = z
+ … + bq = 0 
then the MA(q) process admits a causal autoregressive representation if 
the roots of the characteristic equation are strictly smaller than 1 in 
modulus. 
Let’s now consider, more in general, an ARMA process of order p,q. 
We say that a stationary process admits a minimal ARMA(p,q) repre-
sentation if it can be written as 
xt + a1xt – 1 + apxt
p
–
= b1εt + … + bqεt
q
– 
or equivalently in terms of the lag operator 
(
)x = B L
(
)ε
A L
t 
t 
where εt is a serially uncorrelated white noise with nonzero variance, a
= b0 = 1, ap ≠0, bq ≠0, the polynomials A and B have roots strictly 
greater than 1 in modulus and do not have any root in common. 
Generalizing the reasoning in the pure MA or AR case, it can be 
demonstrated that a generic process, which admits the ARMA(p,q) rep-
resentation A(L)x = B(L)εt is stationary if both polynomials A and B
t 
have roots strictly different from 1. In addition, if all the roots of the 
polynomial A(z) are strictly greater than 1 in modulus, then the 
ARMA(p,q) process can be expressed as a moving average process: 
B L
(
)
xt = ------------ εt
A L
(
)
 
0 

300 
The Mathematics of Financial Modeling and Investment Management 
Conversely, if all the roots of the polynomial B(z) are strictly greater 
than 1, then the ARMA(p,q) process can be expressed as an autoregres-
sive process: 
A L
εt 
(
)
= ------------ xt
B L
(
)
 
Note that in the above discussions every process was centered—that 
is, it had zero constant mean. As we were considering stationary pro-
cesses, this condition is not restrictive as the eventual nonzero mean can 
be subtracted. 
Note also that ARMA stationary processes extend through the 
entire time axis. An ARMA process, which begins from some initial con-
ditions at starting time t = 0, is not stationary even if its roots are 
strictly outside the unit circle. It can be demonstrated, however, that 
such a process is asymptotically stationary. 
Nonstationary Univariate ARMA Models 
So far we have considered only stationary processes. However, ARMA 
equations can also represent nonstationary processes if some of the 
roots of the polynomial A(z) are equal to 1 in modulus. A process 
defined by the equation 
(
)x = B L
(
)ε
A L
t 
t 
is called an Autoregressive Integrated Moving Average (ARIMA) process 
if at least one of the roots of the polynomial A is equal to 1 in modulus. 
Suppose that λ be a root with multiplicity d. In this case the ARMA rep-
resentation can be written as 
L
(
)ε
A′(
)(I – λL)dxt = B L
t 
A L
L
(
) = A′(
)(I – λL)d 
However this formulation is not satisfactory as the process A is not 
invertible if initial conditions are not provided; it is therefore preferable 
to offer a more rigorous definition, which includes initial conditions. 
Therefore, we give the following definition of nonstationary integrated 
ARMA processes. 

301 
Financial Econometrics: Time Series Concepts, Representations, and Models 
A process xt defined for t ≥0 is called an Autoregressive Integrated 
Moving Average process—ARIMA(p,d,q)—if it satisfies a relationship 
of the type 
(
)(I – λL)dxt = B L
A L  
(
)εt 
where:
 ■ The polynomials A(L) and B(L) have roots strictly greater than 1.
 ■ εt is a white noise process defined for t ≥0.
 ■ A set of initial conditions (x–1, ..., x–p–d, εt, ..., ε–q) independent from 
the white noise is given. 
Later in this chapter we discuss the interpretation and further properties 
of the ARIMA condition. 
Stationary Multivariate ARMA Models 
Let’s now move on to consider stationary multivariate processes. A sta-
tionary process which admits an infinite moving-average representation 
of the type 
∞ 
xt = ∑Hiεt
i
– 
i = 0 
where εt–i is an n-dimensional, zero-mean, white-noise process with 
nonsingular variance-covariance matrix Ωis called an autoregressive 
moving average—ARMA(p,q)—model, if it satisfies a difference equa-
tion of the type 
(
)xt = B L
A L
(
)εt 
where A and B are matrix polynomials in the lag operator L of order p 
and q respectively: 
p 
A L 
(
) = ∑AiLi , A0 = I, Ap ≠0 
i = 1 

302 
The Mathematics of Financial Modeling and Investment Management 
p 
B L
(
) = ∑BjLj , B0 = I, Bq ≠0 
j = 1 
If q = 0, the process is purely autoregressive of order p; if q = 0, the pro-
cess is purely a moving average of order q. Rearranging the terms of the 
difference equation, it is clear that an ARMA process is a process where 
the i-th component of the process at time t, xi,t, is a linear function of all 
the components at different lags plus a finite moving average of white 
noise terms. 
It can be demonstrated that the ARMA representation is not unique. 
The nonuniqueness of the ARMA representation is due to different rea-
sons, such as the existence of a common polynomial factor in the 
autoregressive and the moving-average part. It entails that the same pro-
cess can be represented by models with different pairs p,q. For this rea-
son, one would need to determine at least a minimal representation— 
that is, an ARMA(p,q) representation such that any other ARMA(p′,q′) 
representation would have p′ > p, q′ > q. With the exception of the 
univariate case, these problems are very difficult from a mathematical 
point of view and we will not examine them in detail. 
Let’s now explore what restrictions on the polynomials A(L) and 
B(L) ensure that the relative ARMA process is stationary. Generalizing 
the univariate case, the mathematical analysis of stationarity is based on 
the analysis of the polynomial det[A(z)] obtained by formally replacing 
the lag operator L with a complex variable z in the matrix A(L) whose 
entries are finite polynomials in L. 
It can be demonstrated that if the complex roots of the polynomial 
det[A(z)], that is, the solutions of the algebraic equation det[A(z)] = 0, 
which are in general complex numbers, all lie outside the unit circle, 
that is, their modulus is strictly greater than one, then the process that 
satisfies the ARMA conditions, 
(
)xt = B L
A L
(
)εt 
is stationary. The demonstration is based on formally solving the ARMA 
equation, writing (see Chapter 5 on matrix algebra) 
(
)]
(
)ε
xt = A –1(
)B L
adj[A L
L
(
)ε = --------------------------B L
t 
t
det[A L
(
)] 
If the roots of the polynomial det[A(z)] lie outside the unit circle, 
then it can be shown that 

303 
Financial Econometrics: Time Series Concepts, Representations, and Models 
∞
∞ 
adj[A L 
(
)]
(
)ε = ∑HiLiε , with ∑Hi absolutely summable
--------------------------B L
t 
t
det[A L
(
)] 
i = 1 
i = 1 
which demonstrates that the process xt is stationary.1 As in the univari-
ate case, if one would consider the equations in 1/z, the same reasoning 
applies but with roots strictly inside the unit circle. 
A stationary ARMA(p,q) process is an autocorrelated process. Its 
time-independent autocorrelation function satisfies a set of linear differ-
ence equations. Consider an ARMA(p,q) process which satisfies the fol-
lowing equation: 
A0xt + A1xt – 1 + … + APxt
P = B0ε + B1ε
+ … + Bqεt
q
– 
t
t – 1 
– 
where A0 = I. By expanding the expression for the autocovariance func-
tion, it can be demonstrated that the autocovariance function satisfies 
the following set of linear difference equations: 
0 if  h
q
> 
q
h
A0Γh + A1Γh – 1 + … + APΓh
p = 

∑Bj
hΩH′ j 
– 
– 
+ 
j = 0 
where Ωand Hi are, respectively, the covariance matrix and the Markov 
coefficients of the process in its infinite moving-average representation: 
∞ 
xt = ∑Hiε –
t
i
i = 0 
From the above representation, it is clear that if the process is purely MA, 
that is, if p = 0, then the autocovariance function vanishes for lag h > q. 
It is also possible to demonstrate the converse of this theorem. If a 
linear stationary process admits an autocovariance function that satis-
fies the following equations,
A0Γh + A1Γh – 1 + … + APΓh
p = 0 if h > q
– 
1 Christian Gourieroux and Alain Monfort, Time Series and Dynamic Models (Cam-
bridge: Cambridge University Press, 1997). 

304 
The Mathematics of Financial Modeling and Investment Management 
then the process admits an ARMA(p,q) representation. In particular, a sta-
tionary process is a purely finite moving-average process MA(q), if and 
only if its autocovariance functions vanish for h > q, where q is an integer. 
Nonstationary Multivariate ARMA Models 
Let’s now consider nonstationary series. Consider a series defined for t ≥ 
0 that satisfies the following set of difference equations: 
A0xt + A1xt – 1 + … + APxt
P = B0ε + B1ε
+ … + Bqεt
q
– 
t
t – 1 
– 
where, as in the stationary case, εt–i is an n-dimensional zero-mean, 
white noise process with nonsingular variance-covariance matrix Ω, A0 
= I, B0 = I, Ap ≠0, Bq ≠0. Suppose, in addition, that initial conditions 
(x–1,...,x–p,εt,...,ε–q) are given. Under these conditions, we say that the pro-
cess xt, which is well defined, admits an ARMA representation. 
A process xt is said to admit an ARIMA representation if, in addi-
tion to the above, it satisfies the following two conditions: (1) det[B(z)] 
has all its roots strictly outside of the unit circle, and (2) det[A(z)] has 
all its roots outside the unit circle but with at least one root equal to 1. 
In other words, an ARIMA process is an ARMA process that satisfies 
some additional conditions. Later in this chapter we will clarify the 
meaning of integrated processes. 
Markov Coefficients and ARMA Models 
For the theoretical analysis of ARMA processes, it is useful to state 
what conditions on the Markov coefficients ensure that the process 
admits an ARMA representation. Consider a process xt, stationary or 
not, which admits a moving-average representation either as 
∞ 
xt = ∑Hiεt
i
– 
i = 0 
or as a linear model: 
t 
xt = ∑Hiεt
i + h t( )z
– 
i = 0 
The process xi admits an ARMA representation if and only if there 
is an integer q and a set of p matrices Ai, i = 0, ..., p such that the 

305 
Financial Econometrics: Time Series Concepts, Representations, and Models 
Markov coefficients Hi satisfy the following linear difference equation 
starting from q: 
p 
∑ AJHl
j = 0 , l > q
– 
j = 0 
Therefore, any ARMA process admits an infinite moving-average 
representation whose Markov coefficients satisfy a linear difference 
equation starting from a certain point. Conversely, any such linear infi-
nite moving-average representation can be expressed parsimoniously in 
terms of an ARMA process. 
Hankel Matrices and ARMA Models 
For the theoretical analysis of ARMA processes it is also useful to 
restate the above conditions in terms of the Hankel infinite matrices.2 It 
can be demonstrated that a process, stationary or not, which admits 
either the infinite moving average representation 
xt = 
∞
∑Hiε εt
i
– 
i = 0 
or a linear moving average model 
t 
xt = ∑ Hiε εt
i
– + h t( )z 
i = 0 
also admits an ARMA representation if and only if the Hankel matrix 
formed with the sequence of its Markov coefficients has finite rank or, 
equivalently, a finite column rank or row rank. 
STATE-SPACE REPRESENTATION 
There is another representation of time series called state-space models. 
As we will see in this section, state-space models are equivalent to ARMA 
models. While the latter are typical of econometrics, state-space models 
originated in the domain of engineering and system analysis. Consider a 
2 Hankel matrices are explained in Chapter 5. 

306 
The Mathematics of Financial Modeling and Investment Management 
system defined for t ≥ 0 and described by the following set of linear differ-
ence equations: 
= Azt + But
zt + 1
 
= Czt + Dut + Est
xt 
where 
xt = an  n-dimensional vector 
zt = a  k-dimensional vector 
ut = an  m-dimensional vector 
st = a  k-dimensional vector 
A = a  k×k matrix 
B = a  k×m matrix 
C = an  n×k matrix 
D = an  n×m matrix 
E = an  n×k matrix 
In the language of system theory, the variables ut are called the 
inputs of the system, the variables zt are called the state variables of the 
system, and the variables xt are called the observations or outputs of the 
system, and st are deterministic terms that describe the deterministic 
components if they exist. 
The system is formed by two equations. The first equation is a 
purely autoregressive AR(1) process that describes the dynamics of the 
state variables. The second equation is a static regression of the observa-
tions over the state variables, with inputs as innovations. Note that in 
this state-space representation the inputs ut are the same in both equa-
tions. It is possible to reformulate state space models with different, 
independent inputs for the states, and the observables. The two repre-
sentations are equivalent. 
The fact that the first equation is a first order equation is not restric-
tive as any AR(p) system can be transformed into a first-order AR(1) 
system by adding variables. The new variables are defined as the lagged 
values of the old variables. This can be illustrated in the case of a single 
second-order autoregressive equation: 
= α0Xt +
Xt + 1 
α1Xt – 1 + εt + 1 
Define Yt = 
. The previous equation is then equivalent to the first-
Xt – 1 
order system: 

307 
Financial Econometrics: Time Series Concepts, Representations, and Models 
= α0Xt + α1Yt + ε
Xt + 1 
t + 1 
= Xt
Yt + 1 
This transformation can be applied to systems of any order and with 
any number of equations. Recall from Chapter 9 that a similar proce-
dures is applied to systems of differential equations. 
Note that this state-space representation is not restricted to white 
noise inputs. A state-space representation is a mapping of inputs into 
outputs. Given a realization of the inputs ut and an initial state z0, the 
realization of the outputs xt is fixed. The state-space representation can 
be seen as a black-box, characterized by A, B, C, D, and z0 that maps 
any m-dimensional input sequence into an n-dimensional output 
sequence. The mapping S = S(A,B,C,D,z0) of u →x is called a black-box 
representation in system theory. 
State-space representations are not unique. Given a state-space rep-
resentation, there are infinite other state-space representations that 
implement the same mapping u →x. In fact, given any nonsingular 
(invertible) matrix Q, it can be easily verified that 
, 
D Qz0)
S(A B C D z
,
,
,
 ,
0) = S(QAQ –1 , QB CQ –1 , , 
Any two representations that satisfy the above condition are called 
equivalent. 
The minimal size of a system that admits a state-space representa-
tion is the minimum possible size k of the state vector. A representation 
is called minimal if its state vector has size k. 
We can now establish the connection between state-space and infi-
nite moving-average representations and the equivalence of ARMA and 
state-space representations. Consider a n-dimensional process xt, which 
admits an infinite moving-average representation 
∞ 
xt = ∑Hiε –
t
i
i = 0 
where εt is an n-dimensional, zero-mean, white noise process with non-
singular variance-covariance matrix Ωand H0 = I, or a linear moving 
average model 

308 
The Mathematics of Financial Modeling and Investment Management 
t 
xt = ∑Hiε – + h t( )z
t
i
i = 0 
It can be demonstrated that this system admits the state-space repre-
sentation: 
= Azt + Bε
zt + 1 
t
 
xt 
= Czt + Dεt 
if and only if its Hankel matrix is of finite rank. In other words, a time 
series which admits an infinite moving-average representation and has a 
Hankel matrix of finite rank can be generated by a state-space system 
where the inputs are the noise. Conversely, a state-space system with 
white-noise as inputs generates a series that can be represented as an 
infinite moving-average with a Hankel matrix of finite rank. This con-
clusion is valid for both stationary and nonstationary processes. 
Equivalence of State-Space and ARMA Representations 
We have seen in the previous section that a time series which admits an 
infinite moving-average representation can also be represented as an 
ARMA process if and only if its Hankel matrix is of finite rank. There-
fore we can conclude that a time series admits an ARMA representation 
if and only if it admits a state-space representation. ARMA and state-
space representations are equivalent. 
To see the equivalence between ARMA and state-space models, con-
sider a univariate ARMA(p,q) model 
p
q 
xt = ∑ϕtxt
i + ∑ψjεt
j , ψ0 = 1
–
– 
i = 1 
j = 0 
This ARMA model is equivalent to the following state-space model 
xt = Czt 
zt = Azt–1 + εt 
where 
C = [ϕ1 ... ϕp 1 ψ1 ... ψq] 

309
Financial Econometrics: Time Series Concepts, Representations, and Models 
–
xt – 1 
–ϕ1 …
ϕp 1 ψ1 … ψq – 1 ψq
· · ·
1 … 0
0
0
 … 
0 
0 
xt
p
·
·
·
·
·
· 
· 
· 
– 
·
·
·
·
·
· 
· 
· 
·
·
·
·
·
· 
· 
· 
zt = εt 
and A = 
0 … 1
0
0
 … 
0 
0 
0 … 0
0
0
 … 
0 
0
εt – 1 
· 
·
·
·
·
·
· 
· 
· 
·
·
·
·
·
· 
· 
· 
· 
·
·
·
·
·
· 
· 
· 
· 
0 … 0
0
0
 … 
1
0
εt
q
– 
In general, the number of states will be larger than the number of obser-
vations. However, the number of states can be reduced model reduction 
techniques.3 
The connection between ARMA and state-space models has a deep 
meaning that will be elucidated after introducing the concept of cointe-
gration and after generalizing the concept of state-space modeling. As 
we will see, both cointegration and state-space modeling implement a 
fundamental dimensionality reduction which plays a key role in the 
econometrics of financial time series. 
INTEGRATED SERIES AND TRENDS 
This section introduces the fundamental notions of trend stationary 
series, difference stationary series, and integrated series. Consider a one-
dimensional time series. A trend stationary series is a series formed by a 
deterministic trend plus a stationary process. It can be written as 
Xt = f t + ( )
( )  ε t
A trend stationary process can be transformed into a stationary pro-
cess by subtracting the trend. Removing the deterministic trend entails 
that the deterministic trend is known. A trend stationary series is an 
example of an adjustment model. 
Consider now a time series Xt. The operation of differencing a series 
consists of forming a new series Yt = ∆Xt = Xt – Xt–1. The operation of 
differencing can be repeated an arbitrary number of times. For instance, 
differencing twice the series Xt yields the following series: 
3 The idea of applying model reduction techniques to state-space models was advo-
cated by, among others, Masanao Aoki. See M. Aoki and A. Havenner, “State Space 
Modeling of Multiple Time Series,” Econometric Reviews (1991), pp. 10:1–59. 

310 
The Mathematics of Financial Modeling and Investment Management 
Zt = ∆Yt = ∆(∆Xt) = (Xt – 
) – (Xt 
)
Xt – 1 
– 2 – Xt – 3 
= Xt – Xt – 1 – Xt – 2 + Xt – 3 
Differencing can be written in terms of the lag operator as 
∆Xt
d = (1 – L)dXt 
A difference stationary series is a series that is transformed into a 
stationary series by differencing. A difference stationary series can be 
written as 
∆Xt 
+ 
= 
( )
µ
 
ε t
µ
ε t
Xt = 
+
+ ( )
Xt – 1 
where ε(t) is a zero-mean stationary process and µ is a constant. A trend 
stationary series with a linear trend is also difference stationary, if spac-
ings are regular. The opposite is not generally true. A time series is said 
to be integrated of order n if it can be transformed into a stationary 
series by differencing n times. 
Note that the concept of integrated series as defined above entails 
that a series extends on the entire time axis. If a series starts from a set 
of initial conditions, the difference sequence can only be asymptotically 
stationary. 
There are a number of obvious differences between trend stationary 
and difference stationary series. A trend stationary series experiences 
stationary fluctuation, with constant variance, around an arbitrary 
trend. A difference stationary series meanders arbitrarily far from a lin-
ear trend, producing fluctuations of growing variance. The simplest 
example of difference stationary series is the random walk. 
An integrated series is characterized by a stochastic trend. In fact, a 
difference stationary series can be written as 
t – 1 
Xt = µt + ∑ε s
( )
( )  + ε t
s + 0 
*
The difference Xt – Xt between the value of a process at time t and 
the best affine prediction at time t – 1 is called the innovation of the pro-
cess. In the above linear equation, the stationary process ε(t) is the inno-
vation process. A key aspect of integrated processes is that innovations 

311 
Financial Econometrics: Time Series Concepts, Representations, and Models 
ε(t) never decay but keep on accumulating. In a trend stationary pro-
cess, on the other hand, past innovations disappear at every new step. 
These considerations carry over immediately in a multidimensional 
environment. Multidimensional trend stationary series will exhibit multiple 
trends, in principle one for each component. Multidimensional difference-
stationary series will yield a stationary process after differencing. 
Let’s now see how these concepts fit into the ARMA framework, 
starting with univariate ARMA model. Recall that an ARIMA process is 
defined as an ARMA process in which the polynomial B has all roots 
outside the unit circle while the polynomial A has one or more roots 
equal to 1. In the latter case the process can be written as 
L
(
)ε
A′(
)∆dxt = B L
t 
A L
L
(
) = (1 – L)dA′(
)
 
and we say that the process is integrated of order n. If initial conditions 
are supplied, the process can be inverted and the difference sequence is 
asymptotically stationary. 
The notion of integrated processes carries over naturally in the mul-
tivariate case but with a subtle difference. Recall from earlier discussion 
in this chapter that an ARIMA model is an ARMA model: 
(
)xt = B L
A L
(
)εt 
which satisfies two additional conditions: (1) det[B(z)] has all its roots 
strictly outside of the unit circle, and (2) det[A(z)] has all its roots out-
side the unit circle but with at least one root equal to 1. 
Now suppose that, after differencing d times, the multivariate series
∆d xt can be represented as follows:
A′(
)xt = B′(
)ε , 1 with A′(
) = A L
L
L
t 
L
(
)∆d 
z
z
In this case, if (1) B′( ) is of order q and det[B′( )] has all its roots 
z
strictly outside of the unit circle and (2) A′( )
is of order p and 
det [A′( )] has all its roots outside the unit circle, then the process is
z
called ARIMA(p,d,q). Not all ARIMA models can be put in this frame-
work as different components might have a different order of integration. 
Note that in an ARIMA(p,d,q) model each component series of the 
multivariate model is individually integrated. A multivariate series is 
integrated of order d if every component series is integrated of order d. 

312 
The Mathematics of Financial Modeling and Investment Management 
Note also that ARIMA processes are not invertible as infinite mov-
ing averages, but as discussed, they can be inverted in terms of a generic 
linear moving average model with stochastic initial conditions. In addi-
tion, the process in the d-differences is asymptotically stationary. 
In both trend stationary and difference stationary processes, innova-
tions can be serially autocorrelated. In the ARMA representations dis-
cussed in the previous section, innovations are serially uncorrelated white 
noise as all the autocorrelations are assumed to be modeled in the ARMA 
model. If there is residual autocorrelation, the ARMA or ARIMA model 
is somehow misspecified. 
The notion of an integrated process is essentially linear. A process is 
integrated if stationary innovations keep on adding indefinitely. Note 
that innovations could, however, cumulate in ways other than addition, 
producing essentially nonlinear processes. In ARCH and GARCH pro-
cesses for instance, innovations do not simply add to past innovations. 
The behavior of integrated and nonintegrated time series is quite dif-
ferent and the estimation procedures are different as well. It is therefore 
important to ascertain if a series is integrated or not. Often a prelimi-
nary analysis to ascertain integratedness suggests what type of model 
should be used. 
A number of statistical tests to ascertain if a univariate series is inte-
grated are available. Perhaps the most widely used and known are the 
Dickey-Fuller (DF) and the Augmented Dickey-Fuller (ADF) tests. The 
DF test assumes as a null hypothesis that the series is integrated of order 
1 with uncorrelated innovations. Under this assumption, the series can 
be written as a random walk in the following form: 
b
= ρXt +
+ εt
Xt + 1 
ρ = 1 
εt IID 
where IID is an independent and identical sequence (see Chapter 6). 
In a sample generated by a model of this type, the value of ρ esti-
mated on the sample is stochastic. Estimation can be performed with the 
ordinary least square (OLS) method. Dickey and Fuller4 determined the 
theoretical distribution of ρ and computed the critical values of ρ that 
4 See William H. Greene, Econometric Analysis: Fifth Edition (Upper Sadle River, 
NJ: Prentice-Hall, 2003). 

313 
Financial Econometrics: Time Series Concepts, Representations, and Models 
correspond to different confidence intervals. The theoretical distribution 
of ρ is determined computing a functional of the Brownian motion. 
Given a sample of a series, for instance a series of log prices, appli-
cation of the DF test entails computing the autoregressive parameter ρ 
on the given sample and comparing it with the known critical values for 
different confidence intervals. The strict hypothesis of random walk is 
too strong for most econometric applications. The DF test was extended 
to cover the case of correlated residuals that are modeled as a linear 
model. In the latter case, the DF test is called the Augmented Dickey 
Fuller or ADF test. The Phillips and Perron test is the DF test in the gen-
eral case of autocorrelated residuals. 
SUMMARY
 ■ A time series is a discrete-time stochastic process, that is, a denumera-
ble collection of random variables indexed by integer numbers.
 ■ Any stationary time series admits an infinite moving average represen-
tation, that is to say, it can be represented as an infinite sum of white 
noise terms with appropriate coefficients.
 ■ A time series is said to be invertible if it can also be represented as an 
infinite autoregression, that is, an infinite sum of all past terms with 
appropriate coefficients.
 ■ ARMA models are parsimonious representations that involve only a 
finite number of moving average and autoregressive terms.
 ■ An ARMA model is stationary if all the roots of the inverse characteris-
tic equation of the AR or the MA part have roots with modulus strictly 
greater than one.
 ■ A process is said to be integrated of order p if it becomes stationary 
after differencing p times.
 ■ A state-space model is a regression of observable variables over an 
ARMA model of lower dimensionality.
 ■ Every ARMA process admits a state-space representation. 



## Financial Econometrics: Model Selection

I 
CHAPTER 12 
Financial Econometrics: 
Model Selection, Estimation, 
and Testing 
n economics and finance theory models are rarely determined by 
strong theoretical considerations. Often, one or more families of mod-
els compete as plausible explanations of empirical data. Therefore, a 
specific family of models has to be selected and, within a given family, 
parameters have to be estimated. In this chapter we discuss criteria for 
model selection and parameter estimation. 
MODEL SELECTION 
Science works by making hypotheses and testing them. In the physical 
sciences, in particular, hypotheses are mathematical models typically 
tested with a very high level of precision under a variety of experimental 
settings. In the usual process of scientific inquiry, models can be under-
stood as the product of human creativity. How the general concepts of 
science are formed and modified to account for new empirical evidence 
has been the subject of intense study.1 
With the advent of fast computers, an automatic approach to sci-
ence—and to the creative process in general—has been made possible. 
The Nobel laureate Herbert Simon was a strong advocate of the idea 
that the creative discovery process can be automated as an algorithmic 
(that is, step-by-step) search in a space of different possibilities. 
1 See for instance Thomas Kuhn, The Structure of Scientific Revolutions: Third Edi-
tion (Chicago: University of Chicago Press, 1996). 
315 

316 
The Mathematics of Financial Modeling and Investment Management 
Since the pioneering work of Simon, many different search strate-
gies have been proposed by statisticians and researchers in artificial 
intelligence. Most approaches to searching strategies are based on mini-
mizing a “distance” from an objective. In the case of econometrics, the 
objective of searching is to find the best model that describes data. 
Searches are implemented by optimization of some functional. 
The problem with the search approach is that the search space is infi-
nite. Even if the search space can be made finite by applying some sort of 
discretization, its size for real-life problems is enormous. Any practical 
application of the idea of automatic searches requires that the search 
space is constrained. Econometrics, as well as statistics and data mining, 
constrains the search space by searching within given families of models. 
In econometrics, the selection of the model family is typically per-
formed on the basis of theoretical considerations as in the physical sci-
ences. There is no way that an unconstrained search for models might 
yield positive results. Various tools might help to decide what family of 
models to adopt but, ultimately, model selection is a creative decision 
based on theoretical grounds. Once a family of models is selected, there 
are still choices to be made as regards the constraints to apply. 
A typical top-down approach to constraining searches consists of 
starting with a broad family of unrestricted models, for instance, as 
explained later in this chapter, Vector Autoregressive Models (VAR), 
and then proceeding by constraining them, for instance by applying 
error correction constraints as discussed later. A typical bottom-up 
approach starts with a family of highly constrained models suggested by 
theory and then progressively relaxes constraints. 
As there is a large amount of uncertainty in econometrics, model 
selection is never definitive and many different models may coexist as 
competing or synergic explanations of the same empirical facts, leading 
to model uncertainty. One can deal with this by giving weights to vari-
ous models, e.g., predict with the weighted average of the prediction 
from several models. This process can be performed under a classical 
statistical framework or under a Bayesian statistical framework if prior 
probabilities can be assigned to models.2 In this sense, econometrics is 
quite different from the physical sciences where the coexistence of com-
peting theories is a rare event. 
Econometric models generally entail the selection of parameters or 
even the selection of a specific model within a family. This is the realm of 
algorithmic searches, generally in the form of optimization procedures. 
2 A classical reference to Bayesian statistics with emphasis on statistical inference as 
decision theory is: Josè M. Bernardo and Adrian F.M. Smith, Bayesian Theory 
(Chichester, U.K.: John Wiley & Sons., 2000). 

317 
Financial Econometrics: Model Selection, Estimation, and Testing 
For instance, an econometrician might decide, on theoretical grounds, to 
adopt an ARMA family of models. Searches will then help determine 
parameters such as the order of the model and the estimation of the 
model parameter. We will return to the problem of determining the 
model complexity and estimating parameters in the following sections. 
The above considerations apply to parametric models, that is, mod-
els that include parameters to be estimated. There are statistical models 
that appear to be nonparametric. Nonparametric models are typically 
based on the empirical estimation of probability distribution functions. 
Nonparametric models are typically simple models as there is no practi-
cal way to estimate empirically complex models. 
In summary, econometrics follows a general scientific principle of 
formulation and testing of theoretical hypotheses. However, economet-
ric hypotheses are generally formulated as a family of models with 
parameters to be optimized. Econometrics is thus an instance of a gen-
eral process of learning.3 
LEARNING AND MODEL COMPLEXITY 
If one had an infinite amount of empirical data and an infinite amount of 
computational resources, econometric models could in principle be selected 
with arbitrary accuracy. However as empirical data are finite and, gener-
ally, scarce, many different models fit empirical data. The key problem of 
statistical learning is that most families of models can be parameterized so 
that they can fit a finite sample of data with arbitrary accuracy. For 
instance, if an arbitrary number of lags is allowed, an ARMA model can be 
made to fit any sample of data with arbitrary accuracy. A model of this 
type, however, would have very poor forecasting ability. The phenomenon 
of fitting sample data with excessive accuracy is called overfitting. 
In the classical formulation of the physical sciences, overfitting is a 
nonissue as models are determined with theoretical considerations and 
are not adaptively fit to data. The problem of overfitting arises in con-
nection with broad families of models that are able to fit any set of data 
with arbitrary accuracy. Avoiding overfitting is essentially a problem of 
3 Christian Gourieroux and Alain Monfort, Statistics and Econometric Models 
(Cambridge: Cambridge University Press, 1995); D.F. Hendry, “Econometrics: Al-
chemy or Science?” Economica 47 (1980), pp. 387–406, reprinted in D.F. Hendry, 
Econometrics: Alchemy or Science? (Oxford: Blackwell Publishers, 1993, and Ox-
ford University Press, 2000); D.F. Hendry, Dynamic Econometrics (Oxford: Oxford 
University Press, 1995); and Vladimir N. Vapnik, Statistical Learning Theory (New 
York: John Wiley and Sons, 1998). 

318 
The Mathematics of Financial Modeling and Investment Management 
selecting the right model complexity. The complexity of a model is 
sometimes identified with its dimensionality, that is, with the number of 
free parameters of the model. 
The problem of model complexity is intimately connected with the 
concept of algorithmic compressibility introduced in the 1960s indepen-
dently by Andrei Kolmogorov4 and Gregory Chaitin.5 In intuitive terms, 
algorithmic complexity is defined as the minimum length of a program 
able to reproduce a given stream of data. If the minimum length of a 
program able to generate the given sequence is the same as the length of 
the data stream, then there is no algorithmic compressibility and data 
can be considered purely random. If, on the other hand, a short pro-
gram is able to describe a long stream of data, then the level of algorith-
mic compressibility is high and scientific explanation is possible. 
Models can only describe algorithmically compressible data. In a 
nutshell, the problem of learning is to find the right match between the 
algorithmic compressibility of the data and the dimensionality of the 
model. In practice, it is a question of implementing a trade-off between 
the accuracy of the estimate and the size of the sample. 
Various methodologies have been proposed. Some early proposals are 
empirical rules of thumb, based on increasing the model complexity until 
there is no more gain in the forecasting accuracy of the model. These pro-
cedures require partitioning the data in training and test sets, so that 
models can be estimated on the training data and tested on the test data. 
Procedures such as the Box-Jenkins methodology for the determina-
tion of the right ARMA model can be considered ad hoc methods based 
on specific characteristics of the model, for instance, the decay of the 
autocorrelation function in the case of ARMA models. 
More general criteria for model complexity are based on results 
from information theory. The Akaike Information Criteria (AIC) pro-
posed by Akaike6 is a model selection criterion based on the informa-
tion content of the model. The Bayesian Information Criteria (BIC) 
proposed by Schwartz7 is another model selection criterion based on 
information theory in a Bayesian context. 
4 Andrei N. Kolmogorov, “Three Approaches to the Quantitative Definition of In-
formation,” Problems of Information Transmission 1 (1965), pp. 1–7. 
5Gregory J. Chaitin, “On the Length of Programs for Computing Finite Binary Sequenc-
es,” Journal of Association Computational Mathematics 13 (1965), pp. 547–569. 
6 H. Akaike, “Information Theory and an Extension of the Maximum Likelihood 
Principle,” in B.N. Petrov and F. Csake (eds.), Second International Symposium on 
Information Theory (Budapest: Akademiai Kiado, 1973), pp. 267–281. 
7 Gideon Schwarz, “Estimating the Dimension of a Model,” Annals of Statistics 6 
(1978), pp. 461–464. 

319 
Financial Econometrics: Model Selection, Estimation, and Testing 
Recently, the theory of learning has been given a firm theoretical 
basis by Vladimir Vapnik and Alexey Chervonenkis.8 The Vapnik-Cher-
vonenkis (VC) theory of learning is a complex theoretical framework 
for learning that, when applicable, is able to give precise theoretical 
bounds to the learning abilities of models. The VC theory has been 
applied in the context of nonlinear models thus originating the so-called 
Support Vector Machines. Though its theoretical foundation is solid, 
the practical applicability of the VC theory is complex. It has not found 
yet a broad following in the world of econometrics. 
MAXIMUM LIKELIHOOD ESTIMATE 
Once the dimensionality of the model has been chosen, parameters need 
to be estimated. This is the somewhat firmer ground of statistical esti-
mation. An estimator of a parameter is a statistic, that is, a function 
computed on the sample data. For instance, the empirical average 
n 
x = ∑ xi 
i = 1 
of an n-sample is an estimator of the population mean. An estimator is 
called unbiased if its expected value coincides with the theoretical 
parameter. An estimator is called consistent if a sequence of estimators 
computed on a sequence of samples whose size tends to infinity con-
verges to the true theoretical value of the parameter. 
An estimator is a stochastic quantity when computed on a sample. 
Given a model, the distribution of the estimator on samples of a given 
size is determined and can be computed. Different estimators of the 
same parameters will be characterized by different distributions when 
computed on samples of the same size. The variance of the estimator’s 
distribution is an indication of the quality of the approximation offered 
by the estimator. An efficient estimator has the lowest possible variance. 
A lower bound of an estimator variance is given by the Cramer-Rao 
bound. 
The Cramer-Rao bound is a theoretical lower bound to the accuracy 
of estimates. It can be formulated as follows. Suppose that a population 
sample X has a joint density f(x ϑ) that depends on a parameter ϑ and 
that Y = g(X) is an unbiased estimator of ϑ. Y is a random variable that 
depends on the sample. The Cramer-Rao bound prescribes a lower 
8 Vapnik, Statistical Learning Theory. 

320 
The Mathematics of Financial Modeling and Investment Management 
2
bound for the variance σY of Y. In fact, under mild regularity condi-
tions, it can be demonstrated that 
2
1
σY = var Y ≥ ----
In 
2 
 ∂
I
= nE ----- log f(X θ)  

n 

∂θ 
The Cramer-Rao bound can be generalized to the estimates of a k-
vector of parameters θ. In this case, one must consider the Fisher infor-
mation matrix I(θ) (see below) which is defined as the variance-covari-
ance matrix of the vector 
∂ 
----- log f(X θ)
∂θ 
It can be demonstrated that the difference between the variance-covari-
ance matrix of the vector θ and the inverse of the Fisher information 
matrix is a nonnegative definite matrix. 
This does not mean that the entries of the variance-covariance 
matrix of the vector θ are systematically bigger than the elements of the 
inverse of the Fisher information matrix. However, we can determine a 
lower bound for the variance of each parameter θi. In fact, as all the 
diagonal elements a nonnegative definite matrix are nonnegative, the 
following relationship holds: 
2
σθi = var θi ≥{I –1}i i, 
In other words, the lower bound of the variance of the i-th parameter 
θi is the i-th diagonal entry of the inverse of the Fisher information 
matrix. Estimators that attain the Cramer-Rao bound are called efficient 
estimators. In the following section we will show that the maximum like-
lihood (ML) estimators attain the Cramer-Rao lower bound and are 
therefore efficient estimators. 
There are various methodologies for determining estimators. An 
important methodology is based on the maximum likelihood estimation 
(MLE). MLE is a principle of statistical estimation which, given a para-
metric model, prescribes choosing those parameters that maximize the 

321 
Financial Econometrics: Model Selection, Estimation, and Testing 
likelihood of the sample under the model. This idea is highly intuitive: If 
one throws a coin and obtains 75 heads out of 100 trials, one believes 
that the probabilities of head and tail are ³₄ and ¹⁄₄ respectively and not 
that one is experiencing a very unlikely run of heads. 
Suppose that an n-sample x = (x1,...,xn) with a joint density function 
f(x/ϑ) is given. Suppose also that the density depends on a set of parame-
ters ϑ. The likelihood function is any function L(ϑ) proportional to f(x/ϑ): 
L ϑ
( ) ∝f(x ϑ) 
computed on the given sample. The MLE prescribes to choose those 
parameters ϑ that maximize the likelihood. If the sample is formed by 
independent draws from a density, then the likelihood is the product of 
individual likelihoods: 
n 
f(x ⁄ ϑ) = ∏f xi
( 
ϑ) 
i = 1 
n 
( ) ∝∏f xi
L ϑ
( 
ϑ) 
i = 1 
In this case, in order to simplify calculations, one normally com-
putes the log-likelihood defined as the logarithm of the likelihood, so 
that the product is transformed into a sum. As the logarithm is an 
increasing function, maximizing the likelihood or the log likelihood 
gives the same results. 
The MLE is an estimation method which conforms to general scientific 
principles. From a statistical point of view, it has interesting properties. In 
fact, it can be demonstrated that a ML estimator is an efficient estimator 
(that is, an estimator which attains the minimum possible variance). 
In the case of independent samples, the classical theory of ML esti-
mators can be resumed as follows. Let Yi, i = 1,2,...,n be n independent 
variables with probability density functions fi(yi|θ), where θ is a k-vector 
of parameters to be estimated. Let the joint density of n independent 
observations y = (yi) of the variables Yi be 
n 
f(y θ) = ∏fi(yi θ) = L(y θ) 
i = 1 
The log-likelihood function of the sample is 

322 
The Mathematics of Financial Modeling and Investment Management 
n 
log L(y θ) = ∑log fi(yi θ) 
i = 1 
The Fisher score function u is defined as the k-vector of the first deriva-
tives of the log-likelihood: 
u θ
θ
( ) = [uj( )] 
∂
θ
uj( ) = -------log L(y θ) , j = 1,2,...,k 
∂θj 
The ML estimator θˆ of the true parameter θ is obtained equating 
the score to zero: u θˆ
( ) = 0 . It can be demonstrated that the mean of the 
score evaluated at the true parameter value vanishes: E[u(θ)] = 0. The 
variance-covariance matrix of the score is called the Fisher information 
matrix: 
( )] = E[u θ
( )] = I θ
var/cov[u θ
( )u T θ
( )  
Under mild regularity conditions it can be demonstrated that the follow-
ing relationship holds: 
I θ
( )
∂2log L θ
( ) = –E --------------------------
∂θi∂θj 
The matrix of the second derivatives on the right side is called the 
observed information matrix. The classical theory of ML estimators 
states that, in large samples, the distribution of the ML estimator θˆ of θ
, I–1(θ
is approximately normal with parameters [θ
)], that is, the follow-
ing relationship holds: 
θ
θˆ ∼N[θ, I –1( )] 
This relationship tells us that ML estimators are efficient estimators as 
their variance attains the Cramer-Rao bound. The asymptotic joint nor-
mality of the ML estimators can be used to construct a number of tests 
and confidence intervals. 

323 
Financial Econometrics: Model Selection, Estimation, and Testing 
Suppose that one wants to estimate a regressive model Y = aX + b + 
ε from a sample of n pairs (yi, xi). The linear regressive model is charac-
terized by the two parameters a and b, which can be estimated with the 
Ordinary Least Square (OLS) method. The OLS computes the straight 
line that minimizes the sum of the squares of the distances of the sam-
ples from that straight line. 
In a probabilistic setting, the estimates aˆ , bˆ of the two parameters a 
and b depend on the sample. They obey a distribution that depends on 
the distribution of the errors ε. It can be demonstrated that, if the errors 
are normally distributed IID sequences than the OLS estimators aˆ , bˆ are 
unbiased ML estimators. They are therefore efficient estimators. If the 
errors are IID variables with finite variance but are not normally distrib-
uted, then the OLS estimators aˆ , bˆ of the two parameters a and b are 
unbiased estimators but not necessarily ML estimators. 
The OLS estimation procedure is very general. It can be demon-
strated that any linear unconstrained autoregressive model with normal 
innovations can be estimated with OLS estimators and that the ensuing 
estimators are unbiased ML estimators and thus efficient estimators. 
One can also estimate directly the moments of a distribution. In par-
ticular, in a multivariate environment we have to estimate the variance-
covariance matrix Ω. It can be demonstrated that the variance-covari-
ance matrix can be estimated through empirical variances and covari-
ances. Consider two random variables X,Y. 
The empirical covariance between the two variables is defined as 
follows: 
n 
σˆ X Y
1 
= -- ∑(Xi – X)(Yi – Y)
, 
ni = 1 
where the empirical means of the variables are: 
n 
1
X = -- ∑ Xi 
ni = 1 
n 
1
Y = -- ∑ Yi 
ni = 1 
The correlation coefficient is the covariance normalized with the 
product of the respective empirical standard deviations: 

324 
The Mathematics of Financial Modeling and Investment Management 
σˆ X Y
,
ρˆ 
= -------------
X Y
, 
σˆ Xσˆ Y 
Empirical standard deviations are defined as follows: 
n 
σˆ 
= ∑(Xi – X)
2 
X 
i = 1 
n 
σˆ 
= ∑(Yi – Y)
2 
Y 
i = 1 
It can be demonstrated that the empirical covariance matrix is an 
unbiased estimator of the variance-covariance matrix. If innovations are 
jointly normally distributed, it is also an ML estimator. 
LINEAR MODELS OF FINANCIAL TIME SERIES 
Let’s now apply previous general theoretical considerations and those of 
the previous chapter to modeling financial time series. This section 
describes linear models of financial time series using the concepts intro-
duced in the previous sections. Linear financial models are regressive 
and/or autoregressive models where a series is regressed over exogenous 
variables and/or its own past under a number of constraints. 
In the practice of asset and portfolio management, models of prices, 
returns, and rates are used as inputs to asset selection methodologies 
such as semiautomated investment processes, heuristic computational 
procedures, or full-fledged optimization procedures. The following 
chapters on methods for asset management will explain how the compu-
tational models described in this and the following chapter translate 
into asset and portfolio management strategies. We will start with ran-
dom walk models and progressively introduce more complex factor-
based models. 
RANDOM WALK MODELS 
Consider a time series of prices Pt of a financial asset. Assume there are 
no cash payouts. The simple net return of the asset between periods t – 
1 and t is defined as 

325 
Financial Econometrics: Model Selection, Estimation, and Testing 
Pt – Pt – 1 
Pt
Rt = ----------------------- = ----------- – 1 
Pt – 1 
Pt – 1 
From this definition it is clear that the compound return Rt(k) over k 
periods is: 
Pt 
k – 1 Pt
i
k – 1 
– 
Rt( ) = ----------- – 1 = ∏----------------- – 1 = ∏(Rt
i + 1) – 1
k
– 
–
–
Pt
k
i = 0 Pt
i + 1 
i = 0 
Consider now the logarithms of prices and returns: 
pt = log Pt 
(
rt = log 1 + Rt) 
k
[ 
k
rt( ) = log 1 + Rt( )] 
Following standard usage, we denote prices and returns with upper case 
letters and their logarithms with lower case letters. As the logarithms of 
a product is the sum of the logarithms, we can write: 
Pt
(
rt = log 1 + Rt) = log ----------- = pt – pt – 1
Pt – 1 
k
[ 
k
rt( ) = log 1 + Rt( )] = rt + 
+
–
rt – 1 + … 
rt
k + 1 
Note that for real-world price time series, if the time interval is small, 
the numerical value of returns will also be small. Therefore, as a first 
approximation, we can write 
(
rt = log 1 + Rt) ≈Rt 
The simplest model of equity prices consists in assuming that loga-
rithmic returns are an IID sequence. Under this assumption we can 
write: rt = µ + εt, where µ is a constant and εt is a white noise, that is, a 
zero-mean, finite-variance IID sequence. Under this model we can write 

326 
The Mathematics of Financial Modeling and Investment Management 
pt = 
+
+
pt – 1 
µ
εt 
A time series of this form is called an arithmetic random walk. It is a 
generalization of the simple random walk that was introduced in Chap-
ter 6. The arithmetic random walk is the simplest example of an inte-
grated process. 
Let’s go back to simple net returns. From the above definition, it is 
clear that we can write 
µ
ε
1 + Rt = e 
+
t 
If the white noise is normally distributed, then the returns Rt are lognor-
mally distributed. Recall that we found a simple correspondence 
between a geometric Brownian motion with drift and an arithmetic 
Brownian motion with drift. In fact, using Itô’s Lemma, we found that, 
if the process St follows a geometric Brownian motion with drift 
dS 
------ = µdt + σdB 
S 
its logarithm st = log St then follows the arithmetic Brownian motion 
with drift: 
1 
 
ds = 

µ – --σ2dt + σdB 
 
2 
 
In discrete time, there is no equivalent simple formula as we have to 
integrate over a finite time step. If the logarithms of prices follow a discrete-
time arithmetic random walk with normal increments, the prices them-
selves follow a time series with lognormal multiplicative increments 
written as 
+
t
Pt = (1 + Rt)Pt – 1 = e 
µ
ε Pt – 1 
The arithmetic random walk model of log price processes is sug-
gested by theoretical considerations of market efficiency. As we have seen 
in Chapter 3, it was Bachelier who first suggested Brownian motion as a 
model of stock prices. Recall that the Brownian motion is the continu-
ous-time version of the random walk. Fama and Samuelson formally 

327 
Financial Econometrics: Model Selection, Estimation, and Testing 
introduced the notion of efficient markets which makes it reasonable to 
assume that log price processes evolve as random walks. 
The question of the empirical adequacy of the random walk model 
is very important from the practical point of view. Whatever notion or 
tools for financial optimization one adopts, a stock price model is a 
basic ingredient. Therefore substantial efforts have been devoted to 
proving or disproving the random walk hypothesis.9 
There are many statistical tests aimed at testing the random walk 
hypothesis. A typical test takes the random walk as a null hypothesis. 
The number of runs (that is, consecutive sequences of positive or nega-
tive returns) and the linear growth of the variance are parameters used 
in classical random walk tests. More recent tests are based on the work 
of Aldous and Diaconis10 on the distribution of sequences of positive 
and negative returns. 
There is no definite response. Typical tests fail to reject the null 
hypothesis of random walk behavior with a high level of confidence on 
a large percentage of equity price processes. This does not mean that the 
random walk hypothesis is confirmed, but only that it is a reasonable 
first approximation. As we will see in the following sections, other mod-
els have been proposed. 
CORRELATION 
Before moving on to more sophisticated models, let’s consider random 
walk models of portfolios of equities as opposed to single price pro-
cesses. Let’s therefore consider a multivariate random walk model of an 
equity portfolio assuming that each log price process evolves as an 
arithmetic random walk. We will consider a set of n time series pi,t, i = 
1, ..., n that represent log price processes. Suppose that each time series 
is a random walk written as 
+
+
 
εi t
,
,
pi t = pi t  – 1 
µi 
, 
A multivariate random walk can be represented in vector form as fol-
lows: 
9 See John Y. Campbell, Andrew W. Lo, and A. Craig MacKinley, The Econometrics 
of Financial Markets (Princeton, NJ: Princeton University Press, 1997). 
10 David Aldous and Persi Diaconis, “Shuffling Cards and Stopping Times,” Ameri-
can Mathematical Monthly 8 (1986), pp. 333–348. 

328 
The Mathematics of Financial Modeling and Investment Management 
pt = 
+
+
pt – 1 
µ
εt 
The key difference with respect to univariate random walks is that 
one needs to consider cross correlations as the random disturbances εt 
will be characterized by a covariance matrix Ωwhose entries σi,j are the 
covariances between asset i and asset j. Covariance and correlation are 
one way of expressing the notion of functional dependence between ran-
dom variables. Consider two random variables X,Y. 
The covariance between the two variables is defined as 
, 
{[ 
–
(
)][Y
E Y
( 
(
)E Y
= Cov(X Y) = E
X
 E X
–
(
)]} = E XY) – E X
(
)
σX Y
, 
The correlation coefficient is the covariance normalized with the prod-
uct of the respective standard deviations: 
Cov(X Y)
, 
,
ρX Y = Corr(X Y) = ------------------------------------------
, 
(
)Var Y
Var X
(
)
 
σX Y
,
= -------------
σXσY 
The correlation coefficient expresses a measure of linear dependence. 
Suppose that the variables X,Y have finite mean and variance and that 
are linearly dependent so that 
Y = aX + b + ε 
The above relationship is called a linear regression (see Chapter 6). It 
can be demonstrated that the correlation coefficient between X and Y is 
related to the parameter a in the following way: 
σX 
a = ρX Y------
, σY 
The correlation coefficient can assume values between –1 and +1 
inclusive. It can be demonstrated that the variables X,Y are propor-
tional without any noise term if and only if the correlation coefficient is 
+/–1. If the regression has a noise term, then the correlation coefficient 
assumes a value intermediate between –1 and +1. If variables are inde-
pendent, then the correlation coefficient is zero. The converse is not 
true. In fact, it is possible that two variables exhibit nonlinear depen-

329 
Financial Econometrics: Model Selection, Estimation, and Testing 
dence though the correlation coefficient is zero. Uncorrelated variables 
are not necessarily independent. If the variables X,Y have a nonlinear 
dependence relationship, then the correlation coefficient might become 
meaningless.11 
RANDOM MATRICES 
Modeling log prices of equity portfolios as a set of correlated arithmetic 
random walks is only a rough approximation in the sense that this 
model, when estimated, has poor forecasting ability. A key reason is 
that the full variance-covariance matrix is unstable. This fact can be 
ascertained in different ways. A simple test is the computation of the 
variance-covariance matrix over a moving window. If one performs this 
computation on a broad set of equity price processes such as the S&P 
500, the result is a matrix that fluctuates in a nearly random way 
although the average correlation level is high, in the range of 15 to 
17%. Exhibit 12.1 illustrates the amount of fluctuations in a correlation 
matrix estimated over a moving window. The plot represents the aver-
age when the sampling window moves. 
An evaluation of the random nature of the variance-covariance 
matrix was proposed by Laloux, Cizeau, Bouchaud, and Potters12 
using the Random Matrices Theory (RMT). This theory was developed 
in the 1950s in the domain of quantum physics.13 A random matrix is 
the variance covariance matrix of a set of independent random walks. 
As such, its entries are a set of zero-mean independent and identically 
distributed variables. The mean of the random correlation coefficients 
is zero as these coefficients have a symmetrical distribution in the range 
[–1,+1]. 
Interesting results can be demonstrated in the case that both the 
number of sample points M and the number N of time series tend to 
infinity. Suppose that both T and N tend to infinity with a fixed ratio 
Q = M ⁄ N ≥ 1 
11 See Paul Embrechts, Filip Lindskog, and Alexander McNeil, “Modelling Depen -
dence with Copulas and Applications to Risk Management,” Chapter 8 in S. Rachev 
(ed.), Handbook of Heavy Tailed Distributions in Finance (Amsterdam: Elsevier/ 
North Holland, 2003). 
12 L. Laloux, P. Cizeau, J.-P. Bouchaud, and M. Potters, “Noise Dressing of Financial 
Correlation Matrices,” Physics Review Letter 83 (1999), pp. 1467–1470. 
13 M.L. Mehta, Random Matrix Theory (New York: Academic Press, 1995). 

330 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 12.1 
Fluctuations of the Variance-Covariance Matrix 
It can then be demonstrated that the density of eigenvalues of the ran-
dom matrix tends to the following distribution: 
ρ λ
Q 
(λmax – λ)(λmin – λ)
( )  = --------------------------------------------------------------------
λ
2πσ2 
,
⁄
M N
∞
 
→ , Q = M
 
N
 
≥ 1 
1
1
λmax min = σ2 1 + ---- ± 2 ----
, 
Q
Q 
where σ2 is the average eigenvalue of the matrix. Exhibit 12.2 illustrates 
the theoretical function and a sample computed on 500 simulated inde-
pendent random walks. The shape of the distribution of the eigenvalues 
is the signature of randomness. 

331 
Financial Econometrics: Model Selection, Estimation, and Testing 
EXHIBIT 12.2 
Theoretical Distribution of the Eigenvalues in a Random Matrix 
and Distribution of the Eigenvalues in a Sample of 500 Simulated Independent 
Random Walks 
If the variance-covariance matrix entries do not have a zero mean, 
then the spectrum of the eigenvalues is considerably different. Malev-
ergne and Sornette14 demonstrate that if the entries of the variance-
covariance matrix are all equal—with the obvious exception of the ele-
ments on the diagonal—then a very large eigenvalue appears while all 
the others are equal to a single degenerate eigenvalue. The eigenvector 
corresponding to the large eigenvalue has all components proportional 
to 1, that is, its components have equal weights. 
14 Y. Malevergne and D. Sornette, “Collective Origin of the Coexistence of Apparent 
RMT Noise and Factors in Large Sample Correlation Matrices,” Cond-Mat 02/ 
0115, 1, no. 4 (October 2002). 

332 
The Mathematics of Financial Modeling and Investment Management 
If the entries of the variance-covariance matrix are random but with 
nonzero average, it can be demonstrated that a large eigenvalue still 
appears. However, a small number of large eigenvalues also appear 
while the bulk of the distribution resembles that of a random matrix. 
The eigenvector corresponding to the largest eigenvalue includes all 
components with all equal weights proportional to 1. 
If we compute the distribution of the eigenvalues of the variance-
covariance matrix of the S&P 500 over a window of two years, we 
obtain a distribution of eigenvalues which is close to the distribution of 
a random matrix with some exception. In particular, the empirical dis-
tribution of eigenvalues fits well the theoretical distribution with the 
exception of a small number of eigenvalues that have much larger val-
ues. Following the reasoning of Malevergne and Sornette, the existence 
of a large eigenvalue with a corresponding eigenvector of 1s in a large 
variance-covariance matrix arises naturally in cases where correlations 
have a random distribution with a nonzero mean. 
This analysis shows that there is little information in the variance-
covariance matrix of a large portfolio. Only a few eigenvalues carry 
information while the others are simply the result of statistical fluctua-
tions in the sample correlation. Note that it is the entire matrix which is 
responsible for the structure of eigenvalues, not just a few highly corre-
lated assets. This can be clearly seen in the case of a variance-covariance 
matrix whose entries are all equal. Clearly there is no privileged correla-
tion between any couple of assets but a very large eigenvalue nevertheless 
appears. 
MULTIFACTOR MODELS 
The analysis of the previous section demonstrates that modeling an 
equity portfolio as a set of correlated random walks is only a rough 
approximation. Though the random walk test cannot be rejected at the 
level of individual securities and though there are significant empirical 
correlations between securities, the global structure of large portfolios is 
more intricate than a set of correlated random walks. 
Failure in modeling log price processes as correlated random walks 
might happen for several reasons: There might be nonlinearities in the 
DGPs of price processes; dependence between log price processes might 
not be linear. There might be structural changes (which are a discrete 
form of nonlinearity). What is empirically ascertained is that the vari-
ance-covariance matrix of a large set of price processes is not stable and 
that its eigenvalues have a distribution that resembles the distribution of 

333 
Financial Econometrics: Model Selection, Estimation, and Testing 
the eigenvalues of a random matrix with the exception of a few large 
eigenvalues. 
These considerations lead to adopting models where the correlation 
structure is concentrated in a number of factors. A model for asset log 
prices which is compatible with the findings on the correlation matrices 
is the generic multifactor model that we can write as follows: 
x = a + Bf + ε
where x is the n-vector of the process to be modeled, f is a k-vector of 
common factors with k << n, a is an n-vector of constants, B is an n×k 
matrix and ε is an n-vector of random disturbances such that: 
E[ε f] = 0 
E[εε′ f] = Σ 
The key advantage of multifactor models, that we discuss in Chap-
ter 18, is that the number of factors is generally much smaller than the 
number of variables, thus implementing a substantial dimensionality 
reduction. Note that in the above form, a multifactor model is a static 
regression model, not a dynamic econometric model; it describes the 
static regression relationship of the process variables on factors. 
As explained in the previous chapter, state-space models combine a 
multifactor regression model with an autoregressive model for the fac-
tors. This combination of autoregressive models for the factors and of 
multifactor regressive models for the process variables result in impor-
tant families of dynamic models including models of cointegrating rela-
tionships. 
The latter point raises an important issue in modern econometrics. 
In principle, the variables x can be any sort of economic or financial 
quantities. However, multifactor models were developed and are used 
mainly in the context of financial econometrics. In that context, the 
variables x generally represent returns. This is by no means the only 
possible or useful interpretation of factor models. In fact, cointegration 
models are effectively multifactor models whose main variables are log 
prices and whose factors are the common trends. 
There are therefore two different interpretations for and uses of fac-
tor models in financial econometrics. The most widely used factor mod-
els are models of returns such that factorization implements a 
dimensionality reduction. However, more recently factor models—either 
as cointegrated models of returns and prices or, equivalently, as state-

334 
The Mathematics of Financial Modeling and Investment Management 
space models of prices—have been introduced to capture additional eco-
nomic information contained in asset prices, especially equity prices.15 
CAPM 
Let’s begin by discussing multifactor models of returns. There are many 
different ways of writing such models depending on the nature of the 
factors. The first, and most famous, factor model is the Capital Asset 
Pricing Model (CAPM) developed by Sharpe-Lintner-Mossin. In the 
CAPM there is only one factor given by the portfolio of all investable 
assets. Each log price process can be written as follows: 
xi = βi + αif + σ 
In its original formulation, the CAPM was derived as a general equi-
librium theory; the actual asset price process is the fixed point where the 
collective action of all agents trying to maximize their utility does not 
produce any change in the price process, thus the situation of equilibrium. 
CAPM assumes the joint normality of returns and the independence 
of returns from one period to another; the single factor evolves as an 
arithmetic random walk. This version of the CAPM is conceptually 
restrictive and difficult to test given that the market portfolio, which is 
the portfolio of all investable assets, is difficult to define and measure. 
A later version of CAPM called Conditional CAPM or C(CAPM) was 
proposed. Essentially, the Conditional CAPM assumes that there is only 
one factor driving all prices, but does not impose the restriction that such 
a factor is the market portfolio or that it evolves as a random walk. 
15 The literature on dynamic factor models is ample. Here is a selection of widely 
quoted papers: M. Forni, M. Hallin, M. Lippi, and L. Reichlin, “The Generalized 
Dynamic Factor Model: Identification and Estimation,” Review of Economics and 
Statistics 82, no. 4 (2000), pp. 540–554; J.F. Geweke, “The Dynamic Factor Analy-
sis of Economic Time-Series Models” in D.J. Aigner and A.S. Goldberger (eds.) La-
tent Variables in Socioeconomic Models (Amsterdam: North Holland, 1981); J.F. 
Geweke and K.J. Singleton, “Maximum Likelihood ‘Confirmatory’ Factor Analysis 
of Economic Time Series,” International Economic Review 22, no. 1, pp. 37–54; D. 
Quah and T.J. Sargent, “A Dynamic Index Model for Large Cross Sections,” in J.H. 
Stock and M.W. Watson (eds.), Business Cycles, Indicators and Forecasting (Chica-
go, IL: The University of Chicago Press, 1993), pp. 285–309; J.H. Stock and M.W. 
Watson, “Diffusion Indexes,” NBER Working Paper W6702, 1998; J.H. Stock and 
M.W. Watson, “New Indexes of Coincident and Leading Economic Indications,” in
O.J. Blanchard and S. Fischer (eds.), NBER Macroeconomics Annual 1989 (Cam-
bridge, MA: M.I.T. Press, 1989); M.W. Watson and R.F. Engle, “Alternative Algo-
rithms for Estimation of Dynamic MIMIC, Factor, and Time Varying Coefficient 
Regression Models,” Journal of Econometrics 23 (1983), pp. 385–400. 

335 
Financial Econometrics: Model Selection, Estimation, and Testing 
Asset Pricing Theory (APT) Models 
Asset pricing models based on a single factor have been criticized as 
unduly restrictive and truly multifactor models have been proposed. In a 
multifactor model of asset prices, the restriction of absence of arbitrage 
must be imposed. The Arbitrage Pricing Theory (APT) of Roll and Ross 
allows multiple factors and fixes all other price processes on the basis of 
absence of arbitrage (see Chapter 14). 
APT models can be divided into two different categories in function 
of how factors are treated. In the one, factors are portfolios or exoge-
nous variables such as macroeconomic factors; in the other, factors are 
either modeled or not. 
First consider the case of given exogenous factors. In this case, the APT 
model must be estimated as a constrained regressive model. Constraints 
typically forbid the possibility of using simple ordinary least square (OLS) 
estimates. Thus the estimation procedures are generally based on the direct 
application of Maximum Likelihood principles. 
PCA and Factor Models 
If factors are not given, they must be determined with statistical learning 
techniques. Given the variance-covariance matrix, if factors are portfo-
lios, one can determine factors using the technique of Principal Compo-
nents Analysis (PCA). 
Principal Components Analysis (PCA) implements a dimensionality 
reduction of a set of observations. The concept of PCA is the following. 
Consider a set of n time series Xi, for example the 500 series of returns 
of the S&P 500. Consider next a linear combination of these series, that 
is, a portfolio of securities. Each portfolio P is identified by an n-vector 
2
of weights ωP and is characterized by a variance σP . In general, the
2
variance σP will depend on the portfolio’s weights ωP. Lastly consider a 
normalized portfolio which has the largest possible variance. In this 
context, a normalized portfolio is a portfolio such that the squares of 
the weights sum to one. 
If we assume that returns are IID sequences, jointly normally dis-
tributed with variance-covariance matrix Ω, a lengthy direct calculation 
demonstrates that each portfolio’s return will be normally distributed 
with variance 
2
σP = ωP 
TΩωP 
Therefore the normalized portfolio of maximum variance can be deter-
mined in the following way: 

336 
The Mathematics of Financial Modeling and Investment Management 
Maximize ωP 
TΩωP 
subject to the normalization condition 
TωP = 1
ωP 
where the product is a scalar product. It can be demonstrated that the 
solution of this problem is the eigenvector ω1 corresponding to the larg-
est eigenvalue λ1 of the variance-covariance matrix Ω. As Ωis a vari-
ance-covariance matrix, the eigenvalues are all real. 
Consider next the set of all normalized portfolios orthogonal to ω1, 
that is, portfolios completely uncorrelated with ω1. These portfolios are 
identified by the following relationship: 
TωP = ωP
ω1 
Tω1 = 0 
We can repeat the previous reasoning. Among this set, the portfolio of 
maximum variance is given by the eigenvector ω2 corresponding to the 
second largest eigenvalue λ2 of the variance-covariance matrix Ω. If 
there are n distinct eigenvalues, we can repeat this process n times. In 
this way, we determine the n portfolios Pi of maximum variance. The 
weights of these portfolios are the ortho-normal eigenvectors of the 
variance-covariance matrix Ω. Note that each portfolio is a time series 
which is a linear combination of the original time series Xi. The coeffi-
cients are the portfolios’ weights. 
These portfolios of maximum variance are all mutually uncorre-
lated. It can be demonstrated that we can recover all the original return 
time series as linear combinations of these portfolios: 
n 
Xi = ∑αiPi 
i = 1 
Thus far we have succeeded in replacing the original n correlated time 
series Xi with n uncorrelated time series Pi with the additional insight 
that each Xi is a linear combination of the Pi. Suppose now that only p 
of the portfolios Pi have a significant variance, while the remaining n-p 
have very small variances. We can then implement a dimensionality 
reduction by choosing only those portfolios whose variance is signifi-
cantly different from zero. Let’s call these portfolios factors F. 

337 
Financial Econometrics: Model Selection, Estimation, and Testing 
It is clear that we can approximately represent each series Xi as a 
linear combination of the factors plus a small uncorrelated noise. In fact 
we can write 
p
n 
p 
Xi = ∑αiFi + ∑
αiPi = ∑αiFi + ε 
i = 1 
i = p + 1 
i = 1 
where the last term is a noise term. Therefore to implement PCA one 
computes the eigenvalues and the eigenvectors of the variance-covari-
ance matrix and chooses the eigenvalues significantly different from 
zero. The corresponding eigenvectors are the weights of portfolios that 
form the factors. Criteria of choice are somewhat arbitrary. 
Note that PCA works either on the variance-covariance matrix or on 
the correlation matrix. The technique is the same but results are gener-
ally different. PCA applied to the variance-covariance matrix is sensitive 
to the units of measurement, which determine variances and covariances. 
This observation does not apply to returns, which are dimensionless 
quantities. However, if PCA is applied to prices and not to returns, the 
currency in which prices are expressed matters; one obtains different 
results in different currencies. In these cases, it might be preferable to 
work with the correlation matrix. 
We have described PCA in the case of time series, which is the rele-
vant case in econometrics. However PCA is a generalized dimensionality 
reduction technique applicable to any set of multidimensional observa-
tions. It admits a simple geometrical interpretation which can be easily 
visualized in the three-dimensional case. Suppose a cloud of points in the 
three-dimensional Euclidean space is given. PCA finds the planes that cut 
the cloud of points in such a way as to obtain the maximum variance. 
Suppose that there is a strict factor structure, which means that 
returns exactly follow the model 
r = a + Bf + ε
with 
E[ε f] = 0 
E[εε' f] = Σ 
The matrix B can be obtained diagonalizing the variance-covariance 
matrix. In general, the structure of factors will not be strict and one will 
try to find an approximation by choosing only the largest eigenvalues. 

338 
The Mathematics of Financial Modeling and Investment Management 
Factors can also be obtained through another statistical procedure 
called factor analysis. Factor analysis estimates factors using a maxi-
mum likelihood procedure. Suppose that factors are not portfolios but 
exogenous variables, such as macroeconomic variables. In this case, the 
factor structure is given and the estimation problem becomes one of esti-
mating a regression relationship. This problem can be solved through 
maximum likelihood estimates. 
Let’s now summarize the previous discussion on multifactor models. 
From the point of view of econometrics, the key justification of factor 
models is dimensionality reduction. It can be empirically ascertained 
that the empirical variance-covariance matrices computed over reason-
able time windows are unstable and noisy. This might be due to various 
reasons, in particular to the fact that functional dependence between 
variables is more complex than a simple structure of linear correlation. 
The key problem is to extract maximum information from noise. Multi-
factor models attempt to provide a solution to this problem within the 
domain of simple regressive models. There are different families of mul-
tifactor models: regression over given exogenous variables, factor analy-
sis under the assumption of multivariate random walks, state-space 
models. In addition, multifactor models might be applied to both 
returns and prices. 
VECTOR AUTOREGRESSIVE MODELS 
The next step is to model factors. This requires introducing a broad 
family of ARMA models called Vector Autoregressive (VAR) Models. A 
VAR model is a multivariate AR(n) model. In a VAR model the current 
value of each variable is a linear function of the past values of all vari-
ables plus random disturbances. In full generality, a VAR model can be 
written as follows: 
xt = A1xt – 1 + A2xt – 2 + … + Apxt
p + Dst + ε
– 
t 
where xt = (x1, t, …, xn t) is a multivariate stochastic time series in vec-
, 
tor notation, Ai, i = 1,2,...,p, and D are deterministic n×n matrices, 
εt = ε1, t, … ε
is a multivariate white noise with variance-covariance
n t
,
, 
matrix Ω= { 
} and st = s1, t, …, sn t  is a vector of deterministic
σij 
, 
terms. Using the lag-operator L notation, a VAR model can be written 
in the following form: 
xt = (A1L + A2L2 + … + A LN)xt + Dst + ε
n
t 

339 
Financial Econometrics: Model Selection, Estimation, and Testing 
VAR models can be written in equivalent forms that will be useful in 
the next section. In particular, a VAR model can be written in terms of 
the differences ∆xt in the following error-correction form: 
Ln – 1
∆xt = (Φ1L + Φ2L2 + … + Φ
)∆xt + ΠLn – 1 xt + Dst + εt
n – 1 
where the first n – 1 terms are in first differences and the last term is in levels. 
The multivariate random walk model of log prices is the simplest 
VAR model: 
xt = xt + m + εt 
∆xt = m + εt 
Note that in this model log prices are autoregressive while returns (that 
is, the first differences) are simply correlated multivariate white noise 
plus a constant term. 
As we know from our discussion on ARMA models (see Chapter 
11), the stationarity and stability properties of a VAR model depend on 
the roots of the polynomial matrix 
N
A1z + A2z 2 + … + A z
n
In particular, if all the roots of the above polynomial are strictly outside 
the unit circle, then the VAR process is stationary. In this case, the VAR 
process can be inverted and rewritten as an infinite moving average of a 
white-noise process. If all the roots are outside the unit circle with the 
exception of some root which is on the unit circle, then the VAR process 
is integrated. In this case it cannot be inverted as an infinite moving 
average. If some of the roots are inside the unit circle, then the process is 
explosive. If the VAR process starts at some initial point characterized 
by initial values or distributions, then the process cannot be stationary. 
However, if all the roots are outside the unit circle, the process is 
asymptotically stationary. If some root is equal to 1, then the process 
can be differentiated to obtain an asymptotically stationary process. 
COINTEGRATION 
Let’s now look at the problem of representation of multivariate time 
series from a different angle. Recall that a variable is integrated of order 

340 
The Mathematics of Financial Modeling and Investment Management 
n if it can be transformed into a stationary series differencing n times. In 
particular, a univariate time series X is integrated of order 1 if it can be 
represented as follows: 
b
= ρXt +
+ εt
Xt + 1 
ρ = 1 
εt stationary possibly autocorrelated 
The key feature of an integrated time series is that random innova-
tions never decay. Most economic variables are integrated variables. In 
particular, testing for integration in log price processes one finds that 
the null of integration cannot be rejected in most cases. For instance, 
testing the log price processes in the S&P 500 using a standard test such 
as the ADF test, the null of integration cannot be rejected in about 90% 
of time series as shown in Exhibit 12.3. Nor can the null hypothesis of 
integration be rejected for economic time series such as the monetary 
mass (M3) or the Gross Disposable Product. 
Suppose that a set of time series integrated of order 1 is given. 
Though each series is integrated of order 1, for instance they are arith-
metic random walks, there might be linear combinations of the series 
which are stationary. If this happens, the series are said to be cointe-
grated. The financial meaning of cointegration is the following. Indi-
vidual log price processes can be arithmetic random walks but there are 
portfolios, in general long-short portfolios, which are stationary, and 
thus mean reverting around a constant mean. In other words, individ-
ual securities might be totally unpredictable random walks but portfo-
lios might be more predictable. We will come back to the question of 
the empirical findings of cointegration in real-world economic time 
series and price processes. First, we need to define cointegration mathe-
matically. 
EXHIBIT 12.3 
Integratedness of the S&P 500 
Number 
Type 
Period 
of Series 
of Test 
Integratedness Percentage 
From Jan. 1, 
487 series 
Augmented Dickey-
422 series I(1) 87% 
2001 to 
in the 
Fuller test with two 65 series I(0) 
integrated 
Dec. 31, 2003 
S&P 500 
lags, 95% confi-
dence level. 

341 
Financial Econometrics: Model Selection, Estimation, and Testing 
The concept of cointegration, introduced by Granger in 1981,16 can 
be expressed in the following way. Suppose that a set of n time series, 
integrated of order 1, is given. If there is a linear combination of the 
series 
n 
δt = ∑βixi t
, 
i = 1 
which is stationary, then the series xi,t are said to be cointegrated. Any 
linear combination as the one above is called a cointegrating relation-
ship. Given n time series, there can be from none to at most n – 1 coin-
tegrating relationships. 
Though a definition of cointegration of this type is often given in the 
literature, it should be clear that it is strictly applicable only to pro-
cesses that extend in time from –∞ to +∞. Series that start from some ini-
tial instant cannot be stationary but can be, at most, asymptotically 
stationary. To make the definition of cointegration more general, one 
should allow asymptotic stationarity instead of strict stationarity. 
Cointegrating relationships express long-run equilibrium between 
time series. As noted above, in financial terms, cointegrating relation-
ships represent stationary portfolios. Suppose there are n time series xi,t, 
i = 1,...,n and k < n cointegrating relationships. It can be demonstrated 
that there are n – k integrated time series uj,t, j = 1,...,n – k, called com-
mon trends, such that every time series xi,t can expressed as a linear 
combination of the common trends plus a stationary disturbance: 
n
k
– 
xit = ∑γ juj t + ηi t
,
, 
j = 1 
This is clearly a multifactor representation of integrated processes. 
Is there a general representation of cointegrated processes? The 
answer is affirmative. Granger was able to demonstrate the fundamental 
theorem according to which a multivariate integrated process is cointe-
grated if and only if it can be represented in the Error Correction Model 
(ECM) form. The ECM representation is a representation of a multi-
variate process in first differences with corrections in levels as follows: 
16 C.W.J. Granger, “Some Properties of Time Series Data and Their Use in Econo-
metric Model Specification,” Journal of Econometrics 16 (1981), pp. 121–130. 

342 
The Mathematics of Financial Modeling and Investment Management 
n – 1 
∆xt 
= ∑ ALi

∆xt + αβ′xt + ηt
+ 1 

i = 1 
where α is a p×r matrix, β is a a p×r matrix with αβ′ = Π and ηt is a vec-
tor of stationary disturbances. 
Within the basic framework of ECM, different cointegration models 
have been proposed. Two major models need mention:
 ■ The Autoregressive Distributed Lag (ARDL) model which explicitly 
takes into account exogenous variables that are not cointegrated 
among themselves.17
 ■ The Dynamic Cointegration Approach which models the long-run 
cointegration relationships not as a static regression but as a dynamic 
model with a small number of lags. 
Cointegration of log price processes makes sense from an economic 
point of view. Prices must somehow follow a common trend otherwise 
they will, in the long run, diverge indefinitely. This is not a real eco-
nomic justification of cointegration. Even if in the long run all processes 
end up as fluctuations around some common trend, it does not mean 
that they are cointegrated. Many other possible mechanisms might be at 
work, such as discrete adjustment. 
State-Space Modeling and Cointegration 
The notion of state-space modeling is that empirically measurable eco-
nomic variables are a linear regression over a set of hidden variables 
modeled as an autoregressive process. State-space models represent 
dynamical factor models as the states are the hidden factors of the 
model. The state-space representation introduced above can be general-
ized in many different ways, in particular by letting the noise terms be 
different in the state equations and in the regressions. 
As we have seen earlier in this chapter, there is equivalence between 
state-space models and ARMA models. In particular, there is equiva-
lence between cointegrated models represented by ECM models, and 
state-space models. The factors are the common trends. 
17 See M.H. Pesaran and Y. Shin, “An Autoregressive Distributed Lag Modeling Ap-
proach to Cointegration Analysis,” Chapter 11 in S. Strom (ed.), Econometrics and 
Economic Theory in the 20th Century: The Ragnar Fresh Centennial Symposium 
(Cambridge: Cambridge University Press, 1999). 

343 
Financial Econometrics: Model Selection, Estimation, and Testing 
Empirical Evidence of Cointegration in Equity Prices 
It is now time to discuss the empirical evidence that support various 
types of models. The usual tests do not reject the random walk hypothe-
sis for more than 90% of stocks investigated. The average correlation of 
the S&P 500 computed in the 2001–2003 period is roughly 17% as 
shown in Exhibit 12.1. The distribution of the eigenvalues of the correla-
tion matrix has the distribution shown in Exhibit 12.4. The distribution 
of the eigenvalues is quite close to the theoretical shape for large portfo-
lios of a random matrix with the exception of a number of eigenvalues. 
Cointegration is more difficult to ascertain. A number of academic 
studies have found contradicting evidence about mean reversion around 
exponential trends. Poterba and Summers18 found positive evidence of 
mean reversion of stock prices around exponential trends. This early 
EXHIBIT 12.4 
Distribution of the Eigenvalues of the S&P 500 
18 J. Poterba and L. Summers, “Mean Reversion in Stock Prices: Evidence and Impli-
cations,” Journal of Financial Economics 79 (1988), pp. 22–25. 

344 
The Mathematics of Financial Modeling and Investment Management 
evidence has not been confirmed by later studies.19 Kim, Nelson and 
Startz have argued that mean-reversion is a pre-World War II phenome-
non.20 However, more recent papers give new support to the hypothesis 
of mean reversion.21 
Common trends in exchange rates have documented by Baillie and 
Bollerslev22 and by Kasa23 in equity prices. Cross-correlations at differ-
ent lags between equities have been reported in the literature. For 
instance, Campbell, Lo, and MacKinley24 report significant autocorrela-
tions of portfolio returns for selected portfolios, a fact that is attributed 
to the existence of autocross-correlations. An interpretation of the same 
phenomena on the same data set based on cointegration has been pro-
posed by Kanas and Kouretas.25 
Evidence on asset price cointegration and the use of cointegration in 
asset allocation and portfolio management is discussed in a number of 
papers. See, for instance, Lucas,26 Alexander,27 and Alexander and Dim-
itriu.28 In most cases cointegrating relationships are found in small port-
folios. How to select the cointegrated portfolios in large sets of price 
19 See: Eugene F. Fama and Kenneth.R. French, “Permanent and Temporary Com-
ponents of Stock Prices,” Journal of Political Economy 96, no. 2 (1988), pp. 246– 
273 and Campbell, Lo, and MacKinley, The Econometrics of Financial Markets. 
20 M.J. Kim, C.R. Nelson and R. Startz, “Mean Reversion in Stock Prices? A Reapprais-
al of the Empirical Evidence,” Review of Economic Studies 58 (1991), pp. 515–528. 
21 See: Kent Daniel (2001) “Power and Size of Mean Reversion Tests,” Journal of 
Empirical Finance 8, no. 5 (December 2001), pp. 493–535; Steen Nielsen and Jan 
Overgaard Olesen, “Regime-Switching Stock Returns and Mean Reversion,” Work-
ing paper 11–2000, Department of Economics and EPRU, Copenhagen Business 
School; and Ole Risager, “Random Walk or Mean Reversion: the Danish Stock Mar-
ket since World War I,” Working paper 7–98, Department of Economics and EPRU, 
Copenhagen Business School. 
22 R. Baillie and T. Bollerslev, “Common Stochastic Trends in a System of Exchange 
Rates,” Journal of Finance 44 (1989), pp. 167–182. 
23 K. Kasa, “Common Stochastic Trends in International Stock Markets,” Journal of 
Monetary Economics 29 (1992), pp. 95–124. 
24 See Campbell, Lo, and MacKinley, The Econometrics of Financial Markets. 
25 A. Kanas and G.P. Kouretas, “A Cointegration Approach to the Lead-Lag Effect 
Among Size-Sorted Equity Portfolios,” 2001. 
26 A. Lucas, “Strategic and Tactical Asset Allocation and the Effect of Long-Run 
Equilibrium Relations,” Research Memorandum, Vrije Universiteit Amsterdam, 
1997-42 (1997). 
27 C.O. Alexander, “Optimal Hedging Using Cointegration,” Philosophical Trans-
actions of the Royal Society A 357 (1999), pp. 2039–2058. 
28 C.O. Alexander and A. Dimitriu, “The Cointegration Alpha: Enhanced Index 
Tracking and Long-Short Equity Market Neutral Strategies,” Discussion Paper 
2002-08, ISMA Centre Discussion Papers in Finance Series, 2002. 

345 
Financial Econometrics: Model Selection, Estimation, and Testing 
processes is a critical issue. Usual tests for cointegration cannot be 
applied to large portfolios such as the S&P 500 given the computational 
cost: The space of possible cointegrating relationships is simply too 
large to be searched effectively. 
Effective methods to reduce the search space are needed. The dis-
covery of cointegrating relationships is a tremendous advantage from a 
trading point of view. As discussed by Alexander, it allows, for instance, 
to engineer parsimonious portfolios for index tracking and to create 
profitable trading strategies for hedge funds. Possible solutions to this 
problem remain proprietary. The consideration of the equivalence of 
cointegration and state-space modeling might be a step in this direction. 
Effective algorithms for determining state space models are described in 
the engineering and, more recently, in the econometric literature.29 
NONSTATIONARY MODELS OF FINANCIAL TIME SERIES 
Let’s now proceed to explore a number of nonlinear models. The exist-
ence of nonlinearities in financial time series has been documented in 
many works.30 However identifying and estimating a reasonable non-
linear model remains a highly challenging task. The key problem is the 
explosion of the search space, the so called “curse of dimensionality” 
entailed by nonlinear models. 
Models based on neural networks and many other families of uni-
versal function approximators have been explored both in the literature 
and in the practice of financial trading. These models try to estimate a 
nonlinear DGP. We will not deal with these models which are highly 
specialized and often used as proprietary trading models. 
However, a number of relatively simple nonlinear models have dem-
onstrated their ability to capture important nonlinear phenomena. The 
first (and perhaps the best known) of such models, is the ARCH/ 
GARCH family of models. Another class of nonlinear models are the 
Markov switching models, where a Markov chain drives discrete 
changes in the model parameters. Perhaps the best known of these mod-
els is the Hamilton model, though a variety of Markov switching VAR 
models have been proposed. These models are appealing because they 
implement, in a coherent statistical framework, the idea of structural 
change which is reasonable from an economic standpoint. 
29 D. Bauer and M. Wagner, “Estimating Cointegrated Systems Using Subspace Al -
gorithms,” Journal of Econometrics 111 (2002), pp. 47–84. 
30 Campbell, Lo, and MacKinley, The Econometrics of Financial Markets. 

346 
The Mathematics of Financial Modeling and Investment Management 
The ARCH/GARCH Family of Models 
The ARCH models were proposed by Engle31 as a model of inflation. 
The empirical fact behind ARCH models is the clustering of volatility 
observed in many economic and financial series. If instantaneous volatil-
ity is defined as a hidden variable in a price model and estimated as the 
variance of returns over relatively long periods, one finds periods of 
high volatility followed by periods of low volatility and vice versa. 
Note that a new strain of econometric literature deals with instanta-
neous volatility as an observed variable. The observability of volatility 
is made possible by the availability of high frequency data. In this case, 
there is a variety of models for the volatility process, in particular long-
memory fractional models.32 We maintain the classical definition of vol-
atility as a hidden variable. 
Engle proposed a model in the spirit of state-space modeling where 
volatility is modeled by an autoregressive process and then injected mul-
tiplicatively in the price process. More precisely, the simplest ARCH 
model is defined as follows: 
xt 
β
λxt 1
– 
2
+ 
zt 
= 
In the above equation, x is the process variable and the terms z form 
an IID sequence. The ARCH model was extended by Bollerslev,33 who 
proposed the GARCH family of models. In the GARCH models, volatil-
ity is modeled as a more general ARMA process and then treated as 
before: 
xt = σtzt 
p
q 
2
2
σt = β + ∑λixt
i + ∑δiσt
j
–
– 
i = 1 
j = 1 
The key ingredients of ARCH modeling are an ARMA process for vol-
atility and a regressive process where volatility multiplies a white-noise 
31 R.F. Engle, “Autoregressive Conditional Heteroscedasticity with Estimates of the 
Variance of United Kingdom Inflation,” Econometrica 50 (July 1982), pp. 987– 
1007. 
32 T.G. Andersen, T. Bollerslev, F.X. Diebold, and P. Labys, “Modeling and Fore -
casting Realized Volatility,” Econometrica 71, 2003, pp. 529–626. 
33 T. Bollerslev, “Generalized Autoregressive Conditional Heteroscedasticity,” Jour -
nal of Econometrics 31 (1986), pp. 307–327. 

347 
Financial Econometrics: Model Selection, Estimation, and Testing 
process. If the ARMA process for volatility is integrated (that is, it has unit 
roots) then the GARCH process is called Integrated GARCH or IGARCH. 
The ARCH technology is not restricted to univariate processes but 
can be extended to multivariate processes. Multivariate GARCH pro-
cesses model the entire variance-covariance matrix as an autoregressive 
process. 
Multivariate models of the ARCH-GARCH type become rapidly 
unmanageable as the number of parameters to estimate grows with the 
fourth power of the number of assets. Dimensionality reduction is called 
for. Different proposals have been made, in particular factor models for 
the volatility process. 
The random terms z might have arbitrary distributions. In practice, 
normality is often assumed. However, though the conditional distribu-
tion is normal, the unconditional distribution of a GARCH process is 
not normal but exhibits fat tails (see Chapter 13). This feature of 
GARCH processes, in addition to the modeling of volatility clustering, 
has made them attractive as models of returns. Returns at short time 
horizons are, in fact, not normally distributed but exhibit fat tails. 
However, fitting different families of GARCH processes to empirical 
return data has shown that GARCH models cannot fit simultaneously 
the volatility clustering and the fat-tailedness of returns. Distributions 
of the shock z other than normal have been tried, for instance T-Student 
distributions, but no good fit of volatility and returns has been reported 
in the literature. GARCH models can be considered a useful economet-
ric tool, but not a firm theory of price processes. 
Markov Switching Models 
Markov switching models belong to a vast family of models that have 
found applications in many fields other than econometrics, such as 
genomics and speech recognition. The economic idea behind Markov 
switching models is that the economy undergoes discrete switches 
between economic states at random times. To each state corresponds a 
set of model parameters. 
One of the first Markov switching models proposed is the Hamil-
ton34 model. The Hamilton model is based on two states, a state of 
“expansion” and a state of “recession.” Periods of recession are fol-
lowed by periods of expansion and vice versa. The time of transition 
between states is governed by a two-state Markov chain. In each state, 
price processes follow a random walk model. 
34 J.D. Hamilton, “A New Approach to the Economic Analysis of Nonstationary 
Time Series and the Business Cycle,” Econometrica 57 (1989), pp. 357–384. 

348 
The Mathematics of Financial Modeling and Investment Management 
The Hamilton model can be extended to an arbitrary number of 
states and to more general VAR models. In a Markov switching context, 
a VAR model 
(
)L + A2 st
n st
(
)
 ε
xt = [A1 st
(
)L2 + … + A (
)LN]xt + m st + t 
has parameters that depend on a set of hidden states that are governed 
by a discrete-state, discrete-time Markov chain with transition probabil-
ity matrix: 
pi j = Pr(st + 1 = i st = i)
, 
M 
∑pi j = 1 
, 
j = 1 
Estimation of Markov switching VAR models can be done within a 
general maximum likelihood framework. The estimation procedure is 
rather complex as approximate iteration techniques are used. Hamil-
ton35 made use of the Expectation Maximization (EM) algorithm which 
had been proposed earlier in a broader context.36 Other numerical tech-
niques are available and are now implemented in commercial software 
packages. 
Markov switching VAR models have been applied to macroeco-
nomic problems, in particular to the explanation of business cycles. 
Applications to the modeling of large portfolios present significant 
problems of estimation given the large number of data necessary. 
Markov switching models are, in fact, typically estimated over long 
periods of time, say 20 or 30 years. If one wants to construct coherent 
data sets for broad aggregates such as the S&P 500, one rapidly runs 
into problems as many firms, over periods of that length, undergo signif-
icant change such as mergers and acquisitions or stock splits. As one can-
not simply exclude these firms as doing so would introduce biases in the 
estimation process, ad hoc adjustment procedures are needed to handle 
change. Despite these difficulties, however, Markov switching models 
can be considered a promising technique for financial econometrics. 
35 J.D. Hamilton, “Analysis of Time Series Subject to Changes in Regime,” Journal 
of Econometrics 45 (1990), pp. 39–70. 
36 A.P. Dempster, N.M. Laird, and D.B. Rubin, “Maximum Likelihood Estimation 
From Incomplete Data Via the EM Algorithm,” Journal of the Royal Statistical So-
ciety 39 (1977), Series B, 1–38. 

349 
Financial Econometrics: Model Selection, Estimation, and Testing 
SUMMARY 
 ■ Model selection cannot be completely automated because the search 
space is too large.
 ■ Econometrics constrains the search for an optimal model within model 
classes.
 ■ If a family of models can fit data with arbitrary accuracy, then criteria 
for choosing the optimal model complexity are needed.
 ■ Overfitting occurs when a model is too complex and thus fits unpre-
dictable noise.
 ■ Akaike Information Criteria and Bayesian Information Criteria are 
complexity selection criteria based on information theory.
 ■ The Vapnik-Chervonenkis theory of learning has given a rigorous theo-
retical basis to the principles of statistical learning.
 ■ An estimator is a random variable function of the sample data that 
approximates a given parameter of a distribution.
 ■ The Cramer-Rao bound prescribes lower bounds for the variance of 
estimators.
 ■ Maximum Likelihood Estimate (MLE) chooses those parameters that 
maximize likelihood on samples.
 ■ For unconstrained regressions, MLE coincides with Ordinary Least 
Square estimation.
 ■ MLE estimators are efficient estimators, that is, they attain the Cramer-
Rao variance lower bound.
 ■ The simplest asset price model is the random walk.
 ■ A multivariate correlated random walk is a model for the joint price 
process of a set of asset prices.
 ■ A large set of price processes exhibits nearly random variance-covari-
ance matrix of the return process.
 ■ Factor models reduce the dimensionality of the variance-covariance 
matrix of the return process.
 ■ Principal component analysis identifies a generally small number of sta-
ble factors.
 ■ Vector Autoregressive (VAR) models capture the dynamics of time 
series.
 ■ It is impossible to describe large sets of asset price processes with unre-
stricted VAR models because the number of parameters is too high and 
therefore not stable.
 ■ Cointegration captures common stable trends thus implementing a 
dimensionality reduction.
 ■ Cointegrated time series can be represented with a constrained Error 
Correction VAR model.
 ■ State-space models are equivalent to Error Correction models. 

350 
The Mathematics of Financial Modeling and Investment Management
 ■ State-of–the-art nonlinear econometric models use an autoregressive 
process to drive the parameters of another model.
 ■ ARCH/GARCH models use an ARMA model to drive the volatility 
parameter.
 ■ Markov switching models use a Markov chain to drive the parameters 
of an autoregressive model. 


## Fat Tails, Scaling, and Stable Laws

CHAPTER 13 
Fat Tails, Scaling, and 
Stable Laws 
M
ost models of stochastic processes and time series examined thus far 
assume that distributions have finite mean and finite variance. In 
this chapter we describe fat tailed distributions with infinite variance. 
Fat-tailed distributions have been found in many financial economic 
variables ranging from forecasting returns on financial assets to model-
ing recovery distributions in bankruptcies. They have also been found in 
numerous insurance applications such as catastrophic insurance claims 
and in value-at-risk measures employed by risk managers. 
In this chapter, we review the related concepts of fat-tailed, power-
law and Levy-stable distributions, scaling and self-similarity, as well as 
explore the mechanisms that generate these distributions. We discuss the 
key intuition relative to the applicability of fat-tailed or scaling pro-
cesses to finance: In a fat-tailed or scaling world (as opposed to an 
ergodic world), the past does not offer an exhaustive set of possible con-
figurations. Adopting, as an approximation, a scaling description of 
financial phenomena implies the belief that only a small space of possi-
ble configurations has been explored; vast regions remain unexplored. 
We begin with the mathematics of fat-tailed processes, followed by 
a discussion of classical Extreme Value Theory for independent and 
identically distributed sequences. We then explore the consequences of 
eliminating the assumption of independence and discuss different con-
cepts of scaling and self similarity. Finally, we present evidence of fat 
tails in financial phenomena and discuss applications of Extreme Value 
Theory. 
351 

352 
The Mathematics of Financial Modeling and Investment Management 
SCALING, STABLE LAWS, AND FAT TAILS 
Let’s begin with a review of the different but related concepts and prop-
erties of fat tails, power laws, and stable laws. These concepts appear 
frequently in the financial and economic literature, applied to both ran-
dom variables and stochastic processes. 
Fat Tails 
Consider a random variable X. By definition, X is a real-valued function 
from the set Ωof the possible outcomes to the set R of real numbers, 
such that the set (X ≤x) is an event. Recall from Chapter 6 that if P(X ≤ 
x) is the probability of the event (X ≤x), the function F(x) = P(X ≤x) is a 
well-defined function for every real number x. The function F(x) is called 
the cumulative distribution function, or simply the distribution function, 
of the random variable X. Note that X denotes a function Ω →R, x is a 
real variable, and F(x) is an ordinary real-valued function that assumes 
values in the interval [0,1]. If the function F(x) admits a derivative 
dF x
( )
f x
( ) = --------------
dx 
The function f(x) is called the probability density of the random vari-
able X. The function F x
( ) is the tail of the distribution F(x).
( ) = 1 – F x
The function F x
( ) is called the survival function. 
Fat tails are somewhat arbitrarily defined. Intuitively, a fat-tailed distri-
bution is a distribution that has more weight in the tails than some refer-
ence distribution. The exponential decay of the tail is generally assumed as 
the borderline separating fat-tailed from light-tailed distributions. In the lit-
erature, distributions with a power-law decay of the tails are referred to as 
heavy-tailed distributions. It is sometimes assumed that the reference distri-
bution is Gaussian (i.e., normal), but this is unsatisfactory; it implies, for 
instance, that exponential distributions are fat-tailed because Gaussian tails 
decay as the square of an exponential and thus faster than an exponential. 
These characterizations of fat-tailedness (or heavy-tailedness) are not 
convenient from a mathematical and statistical point of view. It would be 
preferable to define fat-tailedness in terms of a function of some essential 
property that can be associated to it. Several proposals have been 
advanced. Widely used definitions focus on the moments of the distribu-
tion. Definitions of fat-tailedness based on a single moment focus either on 
the second moment, the variance, or the kurtosis, defined as the fourth 
moment divided by the square of the variance. In fact, a distribution is 
often considered fat-tailed if its variance is infinite or if it is leptokurtic 

353 
Fat Tails, Scaling, and Stable Laws 
(i.e., its kurtosis is greater than 3). However, as remarked by Bryson1 defi-
nitions of this type are too crude and should be replaced by more complete 
descriptions of tail behavior. 
Others consider a distribution fat-tailed if all its exponential moments 
[
are infinite, E esX ] = ∞ for every s ≥ 0. This condition implies that the 
moment-generating function does not exist. Some suggest weakening this 
condition, defining fat-tailed distributions as those distributions that do 
not have a finite exponential moment of first order. Exponential moments 
are particularly important in finance and economics when the logarithm of 
variables, for instance logprices, are the primary quantity to be modeled.2 
Fat-tailedness has a consequence of practical importance: the proba-
bility of extremal events (i.e., the probability that the random variable 
assumes large values) is much higher than in the case of normal distribu-
tions. A fat-tailed distribution assigns higher probabilities to extremal 
events than would a normal distribution. For instance, a six-sigma event 
(i.e., a realized value of a random variable whose difference from the 
mean is six times the size of the standard deviation) has a near zero 
probability in a Gaussian distribution but might have a nonnegligible 
probability in fat-tailed distributions. 
The notion of fat-tailedness can be made quantitative as different 
distributions have different degrees of fat-tailedness. The degree of fat-
tailedness dictates the weight of the tails and thus the probability of 
extremal events. Extreme Value Theory attempts to estimate the entire 
tail region, and therefore the degree of fat-tailedness, from a finite sam-
ple. A number of indicators for evaluating the size of extremal events 
have been proposed; among these are the extremal claim index pro-
posed in Embrechts, Kluppelberg, and Mikosch,3 which plays an impor-
tant role in risk management. 
The Class L of Fat-Tailed Distributions 
Many important classes of fat-tailed distributions have been defined; 
each is characterized by special statistical properties that are important 
in given application domains. We will introduce a number of such 
classes in order of inclusion, starting from the class with the broadest 
membership: the class L, which is defined as follows. Suppose that F is a 
1 M.C. Bryson, “Heavy-Tailed Distributions,” in N.L. Kotz and S. Read (eds.), En -
cyclopedia of Statistical Sciences, Vol. 3 (New York: John Wiley & Sons, 1982), pp. 
598–601. 
2 See G. Bamberg and D. Dorfleitner, “Fat Tails and Traditional Capital Market The -
ory,” Working Paper, University of Augsburg, August 2001. 
3 P. Embrechts, C. Kluppelberg, and T. Mikosch, Modelling Extremal Events for In -
surance and Finance (Berlin: Springer, 1999). 

354 
The Mathematics of Financial Modeling and Investment Management 
distribution function defined in the domain (0,∞ ) with F < 1 in the entire 
domain (i.e., F is the distribution function of a positive random variable 
with a tail that never decays to zero). It is said that F ∈ L if, for any y > 
0, the following property holds: 
F x  – y)
(
lim -------------------- = 1 , ∀ y > 0 
x 
∞ 
→ 
F x
( )  
We can rewrite the above property in an equivalent (and perhaps more 
intuitive from the probabilistic point of view) way. Under the same assump-
tions as above, it is said that, given a positive random variable X, its distri-
bution function F ∈ L if the following property holds for any y > 0: 
F x  + y)
(
lim P X  > x + y
( 
X > x) = lim -------------------- = 1 , ∀ y > 0 
x 
∞ 
→ 
x 
∞ 
→ 
F x
( )  
Intuitively, this second property means that if it is known that a random 
variable exceeds a given value, then it will exceed any bigger value. 
Some authors define a distribution as being heavy-tailed if it satisfies 
this property. 4 
It can be demonstrated that if a distribution F(x) ∈ L, then it has the 
following properties:
 ■ Infinite exponential moments of every order: E[esX] = ∞ for every s ≥ 0
 ■ lim F x
( )  
e λ x = ∞ , ∀λ > 0 
x 
∞ 
→ 
As distributions in class L have infinite exponential moments of every 
order, they satisfy one of the previous definitions of fat-tailedness. How-
ever they might have finite or infinite mean and variance. 
The class L is in fact quite broad. It includes, in particular, the two 
classes of subexponential distributions and distributions with regularly 
varying tails that are discussed in the following sections. 
Subexponential Distributions 
A class of fat-tailed distributions, widely used in insurance and telecom-
munications, is the class S of subexponential distributions. Introduced 
4 See, for example, K. Sigman, “A Primer on Heavy-Tailed Distributions,” Queueing 
Systems, 1999. 

355 
Fat Tails, Scaling, and Stable Laws 
by Chistyakov in 1964, subexponential distributions can be character-
ized by two equivalent properties: (1) the convolution closure property 
of the tails and (2) the property of the sums.5 
The convolution closure property of the tails prescribes that the 
shape of the tail is preserved after the summation of identical and inde-
pendent copies of a variable. This property asserts that, for x → ∞, the 
tail of a sum of independent and identical variables has the same shape 
as the tail of the variable itself. As the distribution of a sum of n inde-
pendent variables is the n-convolution of their distributions, the convo-
lution closure property can be written as 
F
n* ( )
x
lim ---------------- = n 
x 
∞ 
→ 
( )
F x
Note that Gaussian distributions do not have this property although 
the sum of independent Gaussian distributions is again a Gaussian distri-
bution. Subexponential distributions can be characterized by another 
important (and perhaps more intuitive) property, which is equivalent to 
the convolution closure property: In a sum of n variables, the largest value 
will be of the same order of magnitude as the sum itself. For any n, define 
n 
x
S ( )  = ∑ Xi
n 
i = 1 
as a sum of independent and identical copies of a variable X and call Mn 
their maxima. In the limit of large x, the probability that the tail of the 
sum exceeds x equals the probability that the largest summand exceeds x: 
(
P S > x)
n
lim -------------------------- = 1 
x 
∞ 
→ P M > x)
( 
n 
The class S of subexponential distributions is a proper subset of the 
class L. Every subexponential distribution belongs to the class L while it 
can be demonstrated (but this is not trivial) that there are distributions 
5 See, for example, C. M. Goldie and C. Kluppelberg, “Subexponential Distribu-
tions,” in R.J. Adler, R.E. Feldman, and M.S. Taqqu (eds.), A Practical Guide to 
Heavy Tails: Statistical Techniques and Applications (Boston: Birkhauser, 1998), pp. 
435–459 and Embrechts, Kluppelberg, and Mikosch, Modelling Extremal Events for 
Insurance and Finance. 

356 
The Mathematics of Financial Modeling and Investment Management 
that belong to the class L but not to the class S. Distributions that have 
both properties are called subexponential as it can be demonstrated 
that, as all distributions in L, they satisfy the property: 
lim F x
( )e λx = ∞ , 
λ
∀ > 0 
x 
∞ 
→ 
Note, however, that the class of distributions that satisfies the latter 
property is broader than the class of subexponential distributions; this 
is because the former includes, for instance, the class L.6 
Subexponential distributions do not have finite exponential 
moments of any order, that is, E esX] = ∞ for every s ≥ 0. They may or
[ 
may not have a finite mean and/or a finite variance. Consider, in fact, 
that the class of subexponential distributions includes both Pareto and 
Weibull distributions. The former have infinite variance but might have 
finite or infinite mean depending on the index; the latter have finite 
moments of every order (see below). 
The key indicators of subexponentiality are (1) the equivalence in 
the distribution of the tail between a variable and a sum of independent 
copies of the same variable and (2) the fact that a sum is dominated by 
its largest term. The importance of the largest terms in a sum can be 
made more quantitative using measures such as the large claims index 
introduced in Embrechts, Kluppelberg, and Mikosch that quantifies the 
ratio between the largest p terms in a sum and the entire sum. 
The class of subexponential distributions is quite large. It includes 
not only Pareto and stable distributions but also log-gamma, lognormal, 
Benkander, Burr, and Weibull distributions. Pareto distributions and sta-
ble distributions are a particularly important subclass of subexponential 
distributions; these will be described in some detail below. 
Power-Law Distributions 
Power-law distributions are a particularly important subset of subexpo-
nential distributions. Their tails follow approximately an inverse power 
law, decaying as x –α. The exponent α is called the tail index of the distri-
bution. To express formally the notion of approximate power-law decay, 
we need to introduce the class ℜ(α), equivalently written as ℜα of regu-
larly varying functions. 
A positive function f is said to be regularly varying with index α or f 
∈ℜ(α) if the following condition holds: 
6 See Sigman, “A Primer on Heavy-Tailed Distributions.” 

357 
Fat Tails, Scaling, and Stable Laws 
f tx
(
)
 
α
lim ------------ = t
x
∞ 
→ f x
( )  
A function f ∈ℜ(0) is called slowly varying. It can be demonstrated that 
a regularly varying function f(x) of index α admits the representation 
f(x) = xαl(x) where l(x) is a slowly varying function. 
A distribution F is said to have a regularly varying tail if the follow-
ing property holds: 
F = x –αl x
( )  
where l is a slowly varying function. An example of a distribution with 
a regularly varying tail is Pareto’s law. The latter can be written in vari-
ous ways, including the following:
F x
( 
c
( )  = P X > x) = -------------- for x ≥0 
α 
c
x
+ 
Power-law distributions are thus distributions with regularly vary-
ing tails. It can be demonstrated that they satisfy the convolution clo-
sure property of the tail. The distribution of the sum of n independent 
variables of tail index α is a power-law distribution of the same index α. 
Note that this property holds in the limit for x → ∞. Distributions with 
regularly varying tails are therefore a proper subset of subexponential 
distributions. 
Being subexponential, power laws have all the general properties of 
fat-tailed distributions and some additional ones. One particularly 
important property of distributions with regularly varying tails, valid 
for every tail index, is the rank-size order property. Suppose that sam-
ples from a power law of tail index α are ordered by size, and call S the
r
size of the rth sample. One then finds that the law 
1 
– ---
S
= ar α 
r 
is approximately verified. The well-known Zipf’s law is an example of 
this rank-size ordering. Zipf’s law states that the size of an observation 
is inversely proportional to its rank. For example, the frequency of 
words in an English text is inversely proportional to their rank. The 
same is approximately valid for the size of U.S. cities. 

358 
The Mathematics of Financial Modeling and Investment Management 
Many properties of power-law distributions are distinctly different in 
the three following ranges of α: 0 < α ≤1, 1 < α ≤2, α > 2. The threshold 
α = 2 for the tail index is important as it marks the separation between 
the applicability of the standard Central Limit Theorem; the threshold α 
= 1 is important as it separates variables with a finite mean from those 
with infinite mean. Let’s take a closer look at the Law of Large Numbers 
and the Central Limit Theorem. 
The Law of Large Numbers and the Central Limit Theorem 
There are four basic versions of the Law of the Large Numbers (LLN), 
two Weak Laws of Large Numbers (WLLN), and two Strong Laws of 
Large Numbers (SLLN). 
The two versions of the WLLN are formulated as follows. 
1. Suppose that the variables Xi are IID with finite mean E[Xi] = E[X] = µ. 
Under this condition it can be demonstrated that the empirical average 
tends to the mean in probability: 
n 
∑Xi 
i = 1 
P 
[
]
 = µ
Xn = ---------------
→ 
E X
n
n
∞ 
→ 
2. If the variables are only independently distributed (ID) but have finite 
means and variances (µi,σi), then the following relationship holds: 
n 
n
n 
∑Xi 
∑Xi 
∑µi 
i = 1 
P
i = 1 
i = 1
Xn = ---------------
→ 
--------------- = --------------
n
n
∞ 
→ 
n 
n 
In other words, the empirical average of a sequence of finite-mean finite-
variance variables tends to the average of the means. 
The two versions of the SLLN are formulated as follows. 
1. The empirical average of a sequence of IID variables Xi tends almost 
surely to a constant a if and only if the expected value of the variables 
is finite. In addition, the constant a is equal to µ. Therefore, if and only 
if E Xi
[
]
 = E X
[
]
 = µ
 ∞
 
< 
the following relationship holds: 

---------------
---------------
---------------
--------------
359 
Fat Tails, Scaling, and Stable Laws 
n 
∑ Xi 
i = 1 
A.S. 
[
]
 = µ
Xn = ---------------
→ 
E X
n 
∞ 
→ 
n 
where convergence is in the sense of almost sure convergence. 
2. If the variables  Xi are only independently distributed (ID) but have 
finite means and variances (µ i,σ i) and 
n 
1
2
lim ----- ∑σ i 
∞ 
< 
n 
∞ 
→ 
2 
n i = 1 
then the following relationship holds: 
n 
n 
n 
Xi
∑ 
Xi
∑ 
µ i
∑ 
Xn 
i = 1 
n 
-
= 
n 
∞ 
→ 
A.S. 
→ 
i 
1
= 
n 
- = i 
1
= 
n 
Suppose the variables are IID. If the scaling factor n is replaced with 
n , then the limit relation no longer holds as the normalized sum 
n 
∑ Xi 
i = 1 
n 
diverges. However, if the variables have finite second-order moments, 
the classical version of the Central Limit Theorem (CLT) can be demon-
strated. In fact, under the assumption that both first- and second-order 
moments are finite, it can be shown that 
S – nµ D 
n 
----------------------
Φ 
→ 
σ n 
n 
S
= ∑ Xi
n 
i = 1 

---
---
360 
The Mathematics of Financial Modeling and Investment Management 
where µ, σ are respectively the expected value and standard deviation of X, 
and Φ the standard normal distribution. 
If the tail index α > 1, variables have finite expected value and the 
SLNN holds. If the tail index α > 2, variables have finite variance and 
the CLT in the previous form holds. If the tail index α ≤ 2, then vari-
ables have infinite variance: The CLT in the previous form does not 
hold. In fact, variables with α ≤2 belong to the domain of attraction of 
a stable law of index α. This means that a sequence of properly normal-
ized and centered sums tends to a stable distribution with infinite vari-
ance. In this case, the CLT takes the form 
S – nµ D 
n 
---------------------- →Gα , if 1 < α ≤2
1 
α 
n 
D
Sn 
------ →Gα , if 0 < α ≤1
1 
α 
n 
where G are stable distributions as defined below. Note that the case α = 
2 is somewhat special: variables with this tail index have infinite vari-
ance but fall nevertheless in the domain of attraction of a normal vari-
able, that is, G2. Below the threshold 1, distributions have neither finite 
variance nor finite mean. There is a sharp change in the normalization 
behavior at this tail-index threshold. 
Stable Distributions 
Stable distributions are not, in their generality, a subset of fat-tailed dis-
tributions as they include the normal distribution. There are different, 
equivalent ways to define stable distributions. Let’s begin with a key 
property: the equality in distribution between a random variable and 
the (normalized) independent sum of any number of identical replicas of 
the same variable. This is a different property than the closure property 
of the tail insofar as (1) it involves not only the tail but the entire distri-
bution and (2) equality in distribution means that distributions have the 
same functional form but, possibly, with different parameters. Normal 
distributions have this property: The sum of two or more normally dis-
tributed variables is again a normally distributed variable. But this 
property holds for a more general class of distributions called stable dis-

361 
Fat Tails, Scaling, and Stable Laws 
tributions or Levy-stable distributions. Normal distributions are thus a 
special type of stable distributions. 
The above can be formalized as follows: Stable distributions can be 
defined as those distributions for which the following identity in distri-
bution holds for any number n ≥ 2: 
n 
= C X
D
+
n
n 
i = 1 
∑ Xi 
D 
where Xi are identical independent copies of X and the Cn, Dn are con-
stants. Alternatively, the same property can be expressed stating that 
stable distributions are distributions for which the following identity in 
distribution holds: 
D 
AX1 + BX2 = CX + D 
Stable distributions are also characterized by another property that 
might be used in defining them: a stable distribution has a domain of 
attraction (i.e., it is the limit in distribution of a normalized and cen-
tered sum of identical and independent variables). Stable distributions 
coincide with all variables that have a domain of attraction. 
Except in the special cases of Gaussian (α = 2), symmetric Cauchy 
(α = 1, β = 0) and stable inverse Gaussian (α = ¹⁄₂, β = 0) distributions, 
stable distributions cannot be written as simple formulas; formulas have 
been discovered but are not simple. However, stable distributions can be 
characterized in a simple way through their characteristic function, the 
Fourier transform of the distribution function. In fact, this function can 
be written as 
α
ΦX t
–
( )  = exp{iγt
c
 
t
 [1 – iβsign t
(
( )z t α 
, )]} 
where t ∈ R, γ ∈ R, c > 0, α ∈ (0,2), β ∈ [–1,1], and
( 
πα
z t α 
, ) = tan------ if α ≠ 1
2 
(
z t α 
, ) = –2log t if α = 1 
It can be shown that only distributions with this characteristic function 
are stable distributions (i.e., they are the only distributions closed under 

362 
The Mathematics of Financial Modeling and Investment Management 
summation). A stable law is characterized by four parameters: α, β, c, and 
γ. Normal distributions correspond to the parameters: α = 2, β = 0, γ = 0. 
Even if stable distributions cannot be written as simple formulas, 
the asymptotic shape of their tails can be written in a simple way. In 
fact, with the exception of Gaussian distributions, the tails of stable 
laws obey an inverse power law with exponent α (between 0 and 2). 
Normal distributions are stable but are an exception as their tails decay 
exponentially. 
For stable distributions, the CLT holds in the same form as for 
inverse power-law distributions. In addition, the functions in the 
domain of attraction of a stable law of index α < 2 are characterized by 
the same tail index. This means that a distribution G belongs to the 
domain of attraction of a stable law of parameter α < 2 if and only if its 
tail decays as α. In particular, Pareto’s law belongs to the domain of 
attraction of stable laws of the same tail index. 
EXTREME VALUE THEORY FOR IID PROCESSES 
In this section we introduce a number of important probabilistic con-
cepts that form the conceptual basis of Extreme Value Theory (EVT). 
The objective of EVT is to estimate the entire tail of a distribution from 
a finite sample by fitting to an appropriate distribution those values of 
the sample that fall in the tail. Two concepts play a crucial role in EVT: 
(1) the behavior of the upper order statistics (i.e., the largest k values in 
a sample) and, in particular, of the sample maxima; and (2) the behavior 
of the points where samples exceed a given threshold. We will explore 
the limit distributions of maxima and the distribution of the points of 
exceedances of a high threshold. Based on these concepts a number of 
estimators of the tail index in sequences of independent and identically 
distributed (IID) variables are presented. 
Maxima 
In the previous sections we explored the behavior of sums. The key result 
of the theory of sums is that the behavior of sums simplifies in the limit of 
properly scaled and centered infinite sums regardless of the shape of indi-
vidual summands. If sums converge, their limit distributions can only be 
stable distributions. In addition, the normalized sums of finite-mean, 
finite-variance variables always converge to a normal variable. 
A parallel theory can be developed for maxima, informally defined 
as the largest value in a sample. The limit distribution of maxima, if it 
exists, belongs to one of three possible distributions: Frechet, Weibull, 

363 
Fat Tails, Scaling, and Stable Laws 
or Gumbel. This result forms the basis of classical EVT. Each limit dis-
tribution of maxima has its own Maximum Domain of Attraction. In 
addition, limit laws are max-stable (i.e., they are closed with respect to 
maxima). However, the behavior of maxima is less robust than the 
behavior of sums. Maxima do not converge to limit distributions for 
important classes of distributions, such as Poisson or geometric distri-
butions. 
Consider a sequence of independent variables Xi with common, 
nondegenerate distribution F and the maxima of samples extracted from 
this sequence: 
M1 = X1, Mn = max(X1,...,Xn) 
The maxima Mn form a new sequence of random variables which are 
not, however, independent. 
As the variables of the sequence Xi are assumed to be independent, 
the distribution Fn of the maxima Mn can be immediately written down: 
F x
( 
x
( )
= P X1 ≤x ∨… ∨X ≤x) = Fn( )
n
n 
where ∨is the logical symbol for and. 
If the distribution F, which is a non-decreasing function, reaches 1 
at a finite point xF—that is, if xF = sup{x: F(x) < 1} < ∞, then 
lim P(M < x) = lim F ( ) = 0 , for x < xF
x
n →∞ 
n
n →∞ n 
If xF is finite, 
P M < x) = F ( ) = 1 , for x > xF
( 
x
n
n 
The point xF is called the right endpoint of the distribution F. 
Exhibit 13.1 illustrates the behavior of maxima in the case of a nor-
mal distribution. Given a normal distribution with mean zero and vari-
ance one, 100,000 samples of 20 elements each are selected. For each 
sample, the maximum is chosen. The distribution of the maxima and the 
empirical distribution of independent draws from the same normal are 
illustrated in the exhibit. 
A deeper understanding of the behavior of maxima can be obtained 
considering sequences of normalized and centered maxima. Consider 
the following sequence: c–1(M – d ) where cn > 0, dn ∈R are con-
n 
n
n 
stants. 

364 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 13.1 
The Distribution of the Maxima of a Normal Variable 
A fundamental result on the behavior of maxima is the Fisher-Tip-
pett theorem which can be stated as follows. Consider a sequence of IID 
variables Xi and the relative sequence of maxima Mn. If there exist two 
sequences of constants cn > 0, dn ∈R and a nondegenerate distribution 
function H such that 
–1 
D 
c
(M – d ) →H
n 
n
n 
then H is one of the following distributions: 
0 
x ≤0 
Frechet: Φα x
( ) =  
α > 0 
exp(–x –α) 
x > 0 
–α 
Weibull: Ψα x
exp[–(–x)
] 
x < 0
( ) =  
α > 0 
1 
x ≥0 

365 
Fat Tails, Scaling, and Stable Laws 
x
x
Gumbel: Λ( )  = exp{ –e –x } 
∈ 
, 
R 
The limit distribution H is unique, in the sense that different sequences 
of normalizing constants determine the same distribution. 
The three above distributions—Frechet, Weibull, and Gumbel—are 
called standard extreme value distributions. They are continuous func-
tions for every real x. Random variables distributed according to one of 
the extreme value distributions are called extremal random variables. 
As an example, consider a standard exponential variable X. As F(x) = 
–x
P(X ≤ x) = 1 – e , x ≥ 0 the distribution of the maxima is P(Mn ≤ x) = Fn(x) 
–x)n
= (1 – e 
, x ≥ 0. If we choose dn = ln n, we can write: P(Mn – dn ≤ x) = 
–x)n 
–x)n
P(Mn ≤ ln n + x) = (1 – n–1e 
, x ≥ 0. For any given x, (1 – n–1e 
→ 
exp(–e –x), which shows that the maxima of standard exponential vari-
ables centered with dn = ln n tend to a Gumbel distribution. Exhibit 
13.2 illustrates the three distributions: Frechet, Gumbel, and Weibull. 
We can now ask if there are conditions on the distribution F that 
ensure the existence of centering and scaling constants and the conver-
gence to an extreme value distribution. To this end, let’s first introduce 
EXHIBIT 13.2 
The Distribution of Frechet, Gumbel, and Weibull 

366 
The Mathematics of Financial Modeling and Investment Management 
the concept of the Maximum Domain of Attraction (MDA) of an 
extreme value distribution H or MDA(H). 
A random variable X is said to belong to the MDA(H) of the extreme 
value distribution H if there exist constants cn > 0, dn ∈R such that 
–1 
D 
c
(M – d ) →H
n 
n
n 
Two distribution functions F,G are said to be tail equivalent if they 
have the same right endpoints and the following condition holds: 
F x
( )
lim ------------ = c , 0 < c < ∞ 
x →∞ ( )
G x
Tail equivalence is an important concept for characterizing MDAs. In 
fact, it can be demonstrated that every MDA(H) is closed with respect 
to tail equivalence (i.e., if two distribution functions F and G are tail 
equivalent F ∈MDA(H) if and only if G ∈MDA(H)). Tail equivalence 
allows for a powerful characterization of the three MDAs. 
Let’s first define the quantile function. Given a distribution function 
F, the quantile function of F, written F←(x), is defined as follows: 
F←(x) = inf[s ∈R: F(s) ≥x], 0 < x < 1 
The MDA of the Frechet Distribution 
The Frechet distribution is written as Φα x
( ) = exp(–x –α) . Let’s start by 
observing that the tail of the Frechet distribution decays as an inverse power 
( ) = 1 – exp(–x –α) ≈x 
for x → ∞.
law. In fact, we can write 1 – Φα x
–α 
It can be demonstrated that a distribution function F belongs to the 
MDA of a Frechet distribution Φα x
( ) , α > 0 if and only if there is a 
( ) = x –αL x
slowly varying function L such that F x
( ) . In this case, the 
constants assume the values 
c
= (1 ⁄ F←)( ) , dn = 0
n
n 
We can rewrite this condition more compactly as follows: 
F
F ∈MDA(Φα)
∈ 
⇔ 
R–α 
From the above definitions it can be demonstrated that the follow-
ing five distributions belong to the MDA of the Frechet distribution: (1) 
Pareto; (2) Cauchy; (3) Burr; (4) Stable laws with exponent α < 2; or (5) 
log-gamma distribution. 

367 
Fat Tails, Scaling, and Stable Laws 
The MDA of the Weibull Distribution 
The Weibull distribution is written as follows: 
Ψα = exp[–(–x –α)] 
The Weibull and the Frechet distributions are closely related to each 
other. In fact, it is clear from the definition that the following relation-
ship holds: 
Ψα x
( ) = Φα(–x –1) , x > 0 
One can therefore expect that the MDA of the two distributions are 
closely related. In fact, it can be demonstrated that a distribution func-
tion F belongs to the MDA of a Weibull distribution α > 0 if and only if 
xF < ∞ 
and 
( 
–α
F xF – x –1) = x L x
( )  
where L is a slowly varying function. 
If 
F ∈MDA(Ψα) 
then 
–1 
D 
c
(M – xF) →Ψα
n
n 
The MDA of the Weibull distribution includes important distribu-
tions such as the distribution uniform in (0,1), power laws truncated to 
the right, and Beta distributions. 
The MDA of the Gumbel Distribution 
The Gumbel distribution is written as Λ(x) = exp[–exp(–x)]. Observe 
that the Gumbel distribution has exponential tails. This fact can be eas-
ily ascertained through Taylor expansion. There is no simple character-
ization of the MDA of the Gumbel Distribution. 

368 
The Mathematics of Financial Modeling and Investment Management 
The MDA of a Gumbel distribution encompasses a large class of dis-
tributions that includes the exponential distribution, the normal distribu-
tion, and the lognormal distribution. Though the Gumbel distribution 
has exponential tails, its MDA includes subexponential distributions 
such as the Berktander distribution, as explained in Goldie and Resnick.7 
Max-Stable Distributions 
Stable distributions remain unchanged after summation; max-stable dis-
tributions remain unchanged after taking maxima. A non-degenerate 
random variable X and the relative distribution is called max-stable if 
there are constants cn > 0, dn ∈ R such that the following conditions are 
satisfied 
D 
max(X1, …, X ) = c X
d
+
n
n
n 
where X, X1, ..., Xn are IID variables. 
It can be demonstrated that the class of max-stable distributions 
coincides with the class of possible limit laws for normalized and cen-
tered maxima. In view of the previous discussions, the max-stable laws 
are the three possible limit laws: Frechet, Weibull, and Gumbel. 
Generalized Extreme Value Distributions 
The three extreme value distributions, Frechet, Weibull, and Gumbel, 
can be represented as a one-parameter family of distributions through 
the Standard Generalized Extreme Value Distribution (GEV) of Jenkin-
son and Von Mises. Define the distribution function Hξ as follows: 
–1 ⁄ ξ]
exp[–(1 + ξx) 
for ξ ≠ 0
Hξ =  
exp(–exp(–x))
 for ξ = 0 
where 1 + ξx > 0. One can see from the definition that ξ = α–1 > 0 corre-
sponds to the Frechet distribution, ξ = 0 corresponds to the Gumbel dis-
tribution, and ξ = –α–1 < 0 corresponds to the Weibull distribution. We 
can now introduce the related location-scale dependent family Hξ;µ,ψ by 
replacing the argument x with (x – µ)/ψ. 
7 C.M. Goldie and S. Resnick, “Distributions that are Both Subexponential and in 
the Domain of Attraction of an Extreme-Value Distribution,” Advanced Applied 
Probability, 20 (1988), pp. 706–718. 

369 
Fat Tails, Scaling, and Stable Laws 
Order Statistics 
The behavior of order statistics is a useful tool for characterizing fat-
tailed distributions. For instance, the famous Zipf’s law is an example of 
the behavior of order statistics. Consider a sample X1, ..., Xn made of n 
independent draws from the same distribution F. Let’s arrange the sam-
ple in decreasing order: 
X
≤… ≤X1, n
n n
, 
The random variable Xk,n is called the kth upper order statistic. It can 
be demonstrated that the distribution of the kth upper order statistic is 
k – 1 
– 
Fk n = P Xk n < x) = ∑F
r( )Fn
r( )
(
, 
x
x
, 
r = 0 
In addition, if F is continuous, it has a density with respect to F such 
that 
x 
Fk n = ∫fk n( ) F z
z d ( )
,
, 
–∞ 
where 
n! 
k – 1 
– 
fk n = -------------------------------------- F
( )Fn
k( )
x
x
, 
–
(k – 1)!(n
k)! 
The differences between two consecutive variables in a sample Xk,n 
– Xk+1,n are random variables called spacings. In the case of variables 
with finite right endpoint xF the zero-th spacing is defined as: X0,n – 
X1,n = xF – X1,n. The distribution of spacings depends on the distribu-
tion F. For instance, it can be demonstrated that the spacings of an 
exponential random variable are independent, exponential random vari-
ables with mean 1/n for a n-sample. Spacings are a key concept for the 
definition of the Hill estimator, as explained later in this section. 
Another key concept, which is related to spacings, is that of quantile 
transformation. Let X1, ..., Xn be IID variables with distribution func-
tion F and let U1, ..., Un be IID variables uniformly distributed on the 
interval (0,1). Recall that, given a distribution function F, the quantile 
function of F, written F←(x), is defined as follows: 

--
370 
The Mathematics of Financial Modeling and Investment Management 
F←( ) = inf{s ∈R: F s
x 
( ) ≥x} , 0 < x < 1 
It can be demonstrated that the following results hold:
D 
■  F←(U1) = X1 
D 
■ (X1, n, …, X
) = [F←(U1, n), …, F←(U
)]
n n  
n n
, 
, 
■ The random variable F(X1) has a uniform distribution on (0,1) if and 
only if F is a continuous function. 
To appreciate the importance of the quantile transformation, let’s 
introduce first the notion of empirical distribution function and second 
the Glivenko-Cantelli theorem. The empirical distribution function Fn 
of a sample X1, ..., Xn is defined as follows: 
n 
1 
x
(
F ( ) = -- ∑I Xi ≤x)
n 
ni = 1 
where I is the indicator function. In other words, for each x, the empiri-
cal distribution function counts the number of samples that are less than 
or equal to x. 
The Glivenko-Cantelli theorem provides the theoretical underpin-
ning of nonparametric statistics. It states that, if the samples X1, ..., Xn 
are independent draws from the distribution F, the empirical distribu-
tion function Fn tends to F for large n in the sense that 
a.s. 
∆n = sup 
x
( )
F ( ) – F x →0 , for n → ∞
n 
x ∈R 
The quantile transformation tells us that in cases where F is a Pareto 
distribution, if we approximate n random draws from a uniformly dis-
tributed variable as the sequence 1,2,…,n, then the corresponding val-
ues of the sample X1, ..., Xn will be 
1 1 
1 
--,
, …, --
1 2 
n 
which is a statement of the Zipf’s law. 
From the quantile transformation, the limit law of the ratio between 
two successive order statistics can also be inferred. Suppose that an (infinite) 

371 
Fat Tails, Scaling, and Stable Laws 
population is distributed according to a distribution F ∈ℜα  
( )  with regu-
larly varying tails. Suppose that n samples are randomly and independently 
drawn from this distribution and ordered in function of size: Xn,n ≥ Xn–1,n ≥ 
... ≥ X1,n. It can be demonstrated that the following property holds: 
Xk n
k
, 
--
------------------ = 1 
→
, 
0 
n
Xk + 1, n 
Point Process of Exceedances or Peaks over Threshold 
We have now reviewed the behavior of sums, maxima, and upper order 
statistics of continuous random variables. Yet another approach to EVT 
is based on point processes; herein we will use point processes only to 
define the point process of exceedances. 
Point processes can be defined in many different ways. To illustrate 
the mathematics of point processes, let’s first introduce the homoge-
neous Poisson process. A homogeneous Poisson process is defined as a 
process N(t) that starts at zero, i.e., N(0) = 0, and has independent sta-
tionary increments. In addition, the random variable N(t) is distributed 
as a Poisson variable with parameter λ t. N(t) is therefore a time-depen-
dent discrete variable that can assume nonnegative integer values. 
Exhibit 13.3 illustrates the distribution of a Poisson variable. 
A homogeneous Poisson process can also be defined as a random 
sequence of points on the real line. Consider all discrete sequences of 
points on the real line separated by random intervals. Intervals are inde-
pendent random variables with exponential distribution. This is the 
usual definition of a Poisson process. Call N(t) the number of points 
that fall in the interval [0,t]. It can be demonstrated that N(t) is a homo-
geneous Poisson process according to the previous definition. 
This latter definition can be generalized to define point processes. Intu-
itively, a generic point process is a random collection of discrete points in 
some space. From a mathematical point of view, it is convenient to 
describe a point process through the distribution of the number of points 
that fall in an arbitrary set.8 In the case of homogeneous Poisson pro-
cesses, we consider the number of points that fall in a given interval; for a 
generic point process, it is convenient to consider a wider class of sets. 
Consider a subspace E of a finite dimensional Euclidean space of 
dimension n. Consider also the σ -algebra B of the Borel sets generated 
by open sets in E. The space E is called the state space. For each point x 
in E and for each set A ∈ B, define the Dirac measure ε x as 
8 D.R. Cox and V. Isham, Point Processes (London: Chapman and Hall, 1980). 

372 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 13.3 
Distribution of a Poisson Variable 
1 if  x ∈A
ε
= 
x 
0 if  x ∉A 
For any given sequence xi, i ≥1 of points in E, define the following set 
function: 
∞ 
m A
A
(
) = ∑εxi(
) = card{i:Xi ∈A} , A ∈B 
i = 1 
It can be verified that m(A) is a measure B, called a counting measure. If 
a counting measure is finite on each compact set, then it is called a point 
measure. In other words, any given countable sequence in E generates a 
counting measure on B. 
A point process is obtained associating to each family of sets Ai ∈B 
the joint probability distributions: 

373 
Fat Tails, Scaling, and Stable Laws 
Pr{m Ai
,
,
 ,
 
k; k = 1 2
(
) = ni; i = 1 2  …
,
, …} 
To make this definition mathematically rigorous, a point process 
can be defined as a measurable map from some probability space to the 
set of all point measures equipped with an appropriate σ-algebra. 
Besides the mathematical details, it should be clear that point processes 
are defined by the probability distribution of the number of points that 
fall in each set A of some σ-algebra. The key ingredients of point pro-
cesses are (1) counting measures that associate to each set A the number 
of points of each discrete sequence that falls in A with the additivity 
restrictions of measures and (2) probability distributions defined over 
the space of counting measures. 
Equipped with the general concept of point processes, we can now 
define the point process of exceedances. Consider a threshold formed by 
any real number u and a sequence of random variables Xi, i = 1, 2, .... The 
point process of exceedances with state space E = (0,1) counts the number 
of instances where the random variables Xi exceed the threshold u: 
∞ 
n A
⁄ 
A
≤
 and Xi > u}
N (
) = ∑εi n(
) = card{i
n
i = 1 
Note that in this case the state space specifies the size of the sample. 
Estimation 
In the previous sections we presented some key topics related to the prob-
ability structure of the tails of distributions, be they light- or fat-tailed. 
Let’s now turn to the problem of estimation which is the key practical 
task. The problem of estimation for EVT is essentially the problem of esti-
mating the tail of a distribution from a finite sample. The key statistical 
idea of EVT from the point of view of estimation is to use only those sam-
ple data that belong to the tail and not the entire sample. This notion has 
to be made precise by finding criteria that allow one to separate the tail 
from the bulk of the distribution. Therefore, the estimation problem of 
EVT distribution can be broken down into three separate subproblems:
 ■ Identify the beginning of the tail.
 ■ Identify the shape of the tail, in particular discriminate if it is a power-
law tail.
 ■ Estimate the tail parameters, in particular the tail index in the case of a 
power-law tail. 

374 
The Mathematics of Financial Modeling and Investment Management 
It turns out that these three problems cannot be easily separated. In 
fact, there is no reliable constructive theory for solving all these problems 
automatically. In particular, the choice of the statistical model (i.e., the 
distribution that best describes data) is a classical problem of formulating 
and validating a scientific hypothesis in a probabilistic context. However, 
there are many tools and tests to help the modeler in this endeavor. 
The first fundamental tool is the graphical representation of data, in 
particular the quantile plot or QQ-plot defined as the following set: 
–
 
←n
k + 1
 
Xk n, F
---------------------: k = 1 2
,
, …, n 

, 
 n + 1 
 
The quantile transformation and the Glivenko-Cantelli theorem 
allow concluding that this plot must be approximately linear. Should F 
be a Pareto distribution, the linearity of the QQ-plot is another state-
ment of Zipf’s law. The quantile plot allows a quick verification of a sta-
tistical hypotheses by checking the approximate linearity of the plot. It 
also allows the modeler to form a preliminary opinion on where the tail 
begins and whether the model fails at the far end of the tail. 
Though invaluable as an exploratory tool, graphics rely on human 
judgment and intuition. Rigorous tests are needed. A starting point is 
parameter estimation for the Generalized Extreme Value (GEV) Distri-
bution that we write as 
–1 ⁄ ξ
 
x – µ
 
x – µ
Hξ µ ψ( ) = exp–1 + ξ------------
, 1 + ξ------------ > 0
; , 
x

ψ 
 
ψ 
with the convention that the case ξ = 0 corresponds to the Gumbel dis-
tribution: 
x – µ
 
– ------------
 
ψ  
x
H0;µ ψ( ) = exp–e 
, x ∈R 
, 

 

 
We saw above that these distributions are the limit distributions, if 
they exist, of the normalized maxima of IID sequences. Suppose that the 
data to be estimated are independent draws from some EGV. This is a 
rather strong assumption that we will progressively relax. This assump-
tion might be justified in domains where long series of data are available 

375 
Fat Tails, Scaling, and Stable Laws 
so that the sample data are the maxima of blocks of consecutive data. 
Though this assumption is probably too strong in the domain of finance, 
it is useful to elaborate its consequences. 
Standard methodologies exist for parameter estimation in this case. 
In particular, the usual maximum likelihood (ML) methodology can be 
used for fitting the best GEV to data. Note that if the above distribu-
tions fit maxima we have to divide data into blocks and consider the 
maxima of each block. To apply ML, we have to compute the likelihood 
function on the data and choose the parameters that maximize it. This 
can be done with numerical integration methods. 
An estimation method alternative to ML is the method of moments 
which consists in equating empirical moments with theoretical moments. 
An ample literature on various versions of the method of moments exists.9 
Let’s now release the assumption that the sequence of empirical data 
are independent draws from an exact GEV and replace this with the 
weaker assumption that empirical data are independent draws from F ∈ 
MDA(Hξ). If we assume that the limit distribution is a Frechet distribu-
tion, then data must be independent draws from some distribution F 
whose tail has the form: 
F = x –αL x
( )  
where L is a slowly varying function as described earlier in this chapter. 
For this reason, estimation under this weaker assumption is semipara-
metric in nature. We will now introduce a number of estimators of the 
shape parameter ξ. 
The Pickand Estimator 
P
( )
The Pickand estimator ξˆ 
k n  for an n-sample of independent draws from
,
a distribution F ∈MDA(Hξ) is defined as 
ξˆ ( )  
1 
Xk n – X2k n
P
,
,
= --------ln -----------------------------------
k n
, 
,
, 
ln 2 X2k n – X4k n
where the Xk,n are upper order statistics. 
9 For a discussion of the different methods, see R. L. Smith, “Extreme Value Theo-
ry,” in W. Ledermann (ed.), Handbook of Applicable Mathematics, Supplement, 
(Chichester, U.K.: John Wiley & Sons, 1990), pp. 437–472. For a discussion of the 
method of probability-weighted moments, see J.R.M. Hosking, J.R. Wallis, and E.F. 
Wood, “Estimation of the Generalized Extreme-Value Distribution by the Method 
of Probability-Weighted Moments,” Technometrics 27 (1985), pp. 251–261. 

376 
The Mathematics of Financial Modeling and Investment Management 
It can be demonstrated that the Pickand estimator has the following 
properties:
 ■ Weak consistency: 
ξˆ ( )  P
k
P
ξ
→ , n → ∞, k → ∞, -- → 0
k n
, 
n 
■ Strong consistency: 
a.s. 
ξˆ ( )  
k
k
P
ξ
→ , n → ∞, ------------------
∞
→ 
, -- → 0
k n
, 
ln ( ln n) 
n 
■ Asymptotic normality under technical conditions. 
The Pickand estimator is an estimator of the parameter ξ that does not 
require any assumption on the type of limit distribution. Let’s now examine 
the Hill estimator, which requires the prior knowledge that sample data are 
independent draws from a Frechet distribution. Later in this chapter we 
will see that the assumption of independence can be weakened. 
The Hill Estimator 
Suppose that X1, ..., Xn are independent draws from a distribution F ∈ 
MDA(Φα), α > 0 so that F = x –αL x
( )  where L is a slowly varying func-
tion. The Hill estimator can be obtained as a MLE based on the k upper 
order statistics. The Hill estimator takes the following form: 
α H
ˆ (
)
  1 
k 
H
ˆ (
)
 = αk n =  -- ∑ ln Xj n
ln
– 
Xk n

 
–1 
, 
,
, 
 kj = 1 
The Hill estimator has the same weak and strong consistency prop-
erty as well as asymptotic normality as the Pickand estimator. The Hill 
estimator is by far the most popular estimator of the tail index. It has 
the advantage of being robust to some dependency in the data but can 
perform very poorly in case of deviations from strict Pareto behavior. In 
addition, it is subject to a bias-variance trade-off in the following sense: 
The variance of the Hill estimator depends on the ratio k/n: it decreases 
for increasing k. However, using a large fraction of the data will intro-
duce bias in the estimator. 
As stated above, a critical tenet of EVT is the idea of fitting the tail 
rather than the entire distribution. A number of articles on the automatic 

377 
Fat Tails, Scaling, and Stable Laws 
determination of the optimal subset of samples to be included in the tail 
have appeared. One approach to the automatic determination of the tail 
sample using the variance-bias trade-off was proposed by Drees and Kauf-
mann,10 while Dacorogna, Muller, Pictet, and de Vries11 and Danielsson 
and de Vries12 proposed methods based on a bootstrap approach. 
The moment ratio estimator is a generalization of the Hill estimator. 
Consider the following estimator of the second order moments of the k 
upper order statistic: 
2 
1
k 
ˆ 
= --∑ln Xj n
ln
– 
Xk 

Mk n
kj = 1 
, 
+ 1, n
, 
 
The moment ratio estimator is defined as follows: 
ˆ 
 
m
ˆ (
)
 
,
1Mk n
= -- ------------
, 

αk n
2
 ˆ (
)
H
αk n  
, 
Niklas Wagner and Terry Marsh13 did extensive simulation analysis 
of various estimators. Their finding is that the moment ratio estimator 
outperforms the Hill estimator in sequences with a dependence structure 
(this is discussed further in the next section). 
The Hill estimator was extended by Dekkers, Einmal, and de Haan14 
to cover the entire range of shape parameters ξ. A number of other esti-
mators have been proposed. In particular, under the assumption that 
financial data follow a stable process, estimation procedures based on 
regression analysis has been suggested. In fact, the assumption of stable 
10 H. Drees and E. Kaufmann, “Selecting the Optimal Sample Fraction in Univariate 
Extreme Value Estimation,” Stochastic Processes and their Application 75 (2000), 
pp. 254–274. 
11 M.M. Dacorogna, U.A. Muller, O.V. Pictet, and C.G. de Vries, “The Distribution 
of Extremal Foreign Exchange Rate Returns in Extremely Large Data Sets,” Olsen 
& Associates preprint, Zurich, 1995. 
12 J. Danielsson and C.G. de Vries, “Tail Index and Quantile Estimation with Very 
High Frequency Data,” Journal of Empirical Finance 4 (1977), pp. 241–257. 
13 N. Wagner and T. Marsh, “On Adaptive Tail Index Estimation for Financial Re-
turn Models,” Research Program in Finance, Working Paper RPF-295, Hans School 
of Management, University of California, Berkeley, November 2000. 
14 See A.L.M. Dekkers and L. de Haan, “On the Estimation of the Extreme-Value 
Index and Large Quantile Estimation,” Annals of Statistics 17 (1989), pp. 1795– 
1832. 

378 
The Mathematics of Financial Modeling and Investment Management 
behavior, or at least of exact Pareto tail, naturally leads to fitting a linear 
model in a logarithmic scale. There is an ample literature on this topic 
with a number of useful discussions, though empirical studies based on 
Monte Carlo simulations are still limited.15 
The estimation methods reviewed above are based on the behavior 
of maxima and upper order statistics; another methodology uses the 
points of exceedances of high thresholds. Estimation methodologies 
based on the points of exceedances require an appropriate model for the 
point process of exceedances that was defined in general terms previ-
ously in this chapter. 
ELIMINATING THE ASSUMPTION OF IID SEQUENCES 
In the previous sections we reviewed a number of mathematical tools 
that are used to describe fat-tailed processes under the key assumption 
of IID sequences. In this section we discuss the implications of eliminat-
ing this assumption. However, in finance theory the assumption of sta-
tionary sequences of independent variables is only a first approximation; 
it has been challenged in several instances. Consider individual price 
time series. The autocorrelation function of returns decays exponen-
tially and goes to near zero at very short-time horizons while the auto-
correlation function of volatility decays only hyperbolically and remains 
different from zero for long periods. In addition, if we consider portfo-
lios made of many securities, price processes exhibit patterns of cross 
correlations at different time-lags and, possibly, cointegrating relation-
ships. These findings offer additional reasons to consider the assump-
tion of serial independence as only a first approximation. 
If we now consider the question of stationarity, empirical findings 
are more delicate. The non-stationarity that can be removed by differ-
encing is easy to handle and does not present a problem. The critical 
issue is whether financial time series can be modeled with a single Data 
Generation Process (DGP) that remains the same for the entire period 
under consideration or if the model must be modified. Consider, for 
instance, the question of structural breaks. At a basic level, structural 
breaks entail nonstationarity as the model parameters change with time 
and thus the finite-dimension distributions change with time. However, 
at a higher level one might try to model structural changes, for instance 
15 Francis X. Diebold, Til Schuermann, and John D. Stroughair, “Pitfalls and Oppor-
tunities in the Use of Extreme Value Theory in Risk Management,” The Journal of 
Risk Finance (Winter 2000), pp. 30–36. 

379 
Fat Tails, Scaling, and Stable Laws 
through state-space models or Markov switching models. In this way, 
stationarity is recovered but at the price of a more complex, serially 
autocorrelated model. 
EVT for multivariate models with complex patterns of serial corre-
lations loses its generality and becomes model-dependent. One has to 
evaluate each model in terms of its behavior as regards extremes. In this 
section we will explore a number of models that have been proposed for 
modeling financial time series: ARCH and GARCH models and, more in 
general, state-space models. First, however, a number of methodological 
considerations are in order. 
In the context of IID sequences, EVT tries to answer the question of 
how to estimate a distribution with heavy tails given only a limited 
amount of data. The model is the simplest (i.e., a sequence of IID vari-
ables) and the question is how to extrapolate from finite samples to the 
entire tail. In the context of IID distributions, conditional and uncondi-
tional distributions coincide. However, if we release the IID assumption, 
we have to specify the model and to estimate the entire model—not just 
the tail of one variable. Conditional and unconditional distributions no 
longer coincide. For instance, there are families of models that are con-
ditionally normal and unconditionally fat-tailed. 
Here difficulties begin as model estimation might be complex. In 
addition, estimation of some specific tail might not be the primary con-
cern in model estimation. In the context of variables with a dependence 
structure, EVT can be thought of as a methodology to estimate the tails 
of the unconditional distribution, leaving aside the question of full 
model estimation. 
An important methodological question is whether fat-tailedness is 
generated by the transformation of a sequence of zero-mean, finite vari-
ance IID variables (i.e., white noise) or whether innovations themselves 
have fat tails (i.e., so-called colored noise). For instance, as we will see, 
GARCH models entail fat-tailed return distributions as the result of the 
transformation of white noise. On the other hand, one might want to 
estimate an Autoregressive Moving Average (ARMA) model under the 
assumption of innovations with infinite variance. 
Understanding how power laws and, more in general, fat tails are 
generated from normal variables has been a primary concern of econo-
metrics and econophysics. Given the universality of power laws in eco-
nomics, it is clearly important to understand how they are generated. 
These questions go well beyond the statistical analysis of heavy-tailed 
processes and involve questions of economic theories. Essentially, one 
wants to understand how the decisions of a large number of economic 
agents do not average out but produce cascading and amplification phe-
nomena. 

380 
The Mathematics of Financial Modeling and Investment Management 
The Law of Large Numbers tells that if individual processes are 
independent and have finite variance, then phenomena average out in 
aggregate and tend to an average limit. However, if individual processes 
have fat tails, phenomena do not average out even in the infinite limit. 
The weight of individual tails prevails and drives the aggregate process. 
Philip W. Anderson, the corecipient of the 1997 Nobel Prize in Physics, 
remarked: 
Much of the real world is controlled as much by the 
“tails” of distributions as by means or averages: by the 
exceptional, not the mean; by the catastrophe, not the 
steady drip; by the very rich, not the “middle class.” We 
need to free ourselves from “average” thinking.16 
When and if fat-tailed drivers exist, they control the ensemble to 
which they belong. But what generates these powerful drivers? Models 
that generate fat tails from standard normal innovations attempt to 
answer this question. Different types of models have been proposed. 
One such category of models is purely geometric and exploits mathe-
matical theories such as percolation and random graph. Others exploit 
phenomena of dynamic nonlinear self-reinforcing cascades of events. 
Percolation models are based on the well known mathematical fact 
that in regular spatial structures of nodes connected by links, a uniform 
density of links produces connected subsets of nodes whose size is dis-
tributed according to power laws. Percolation models are time-transver-
sal models: They model aggregation at any given time. They might be 
used to explain how fat-tailed IID sequences are generated. 
Dynamic financial econometric models exploit cascading phenom-
ena due to nonlinearities, in particular multiplicative noise. In a deter-
ministic setting, it is well known that nonlinear chaotic models generate 
sequences that, when analyzed statistically, exhibit fat-tailed distribu-
tions. The same happens when noise is subject to nonlinear transforma-
tion. In the next sections, we explore simple ARMA models, ARCH-
GARCH models, subordinated models, and state-space models, all 
examples of dynamic financial econometric models. 
Before doing this, however, let’s go back to the question of estima-
tion. As observed above, if variables are not IID but can be considered 
generated by a DGP, the question of estimation is no longer the estima-
tion of a variable but that of estimating a model or a theory. The estima-
16 Philip W. Anderson, “Some Thoughts About Distribution in Economics,” in W. 
B. Arthur, S. N. Durlaf, and D.A. Lane (eds.), The Economy as an Evolving Complex 
System II (Reading, MA: Addison-Wesley, 1997). 

381 
Fat Tails, Scaling, and Stable Laws 
tion of the eventual tail index is part of a larger effort. However, 
empirical data are a sequence of samples characterized by an uncondi-
tional distribution. One might want to understand if estimation proce-
dures used for IID sequences can be applied in this more general setting. 
For instance, one might want to understand if tail-index estimators such 
as the Hill estimator can be used in the case of serially correlated 
sequences generated by a generic DGP. 
From a practical standpoint, this question is quite important as one 
wants to estimate the tails even if one does not know exactly what 
model generated the sequence. Clearly, there is no general answer to this 
problem. However, the behavior of a number of estimators under differ-
ent DGPs has been explored through simulation as explained in the fol-
lowing section. 
Heavy-Tailed ARMA Processes 
Let’s first consider the infinite moving average representation of a 
univariate stationary series: 
xt = 
∞
∑ hiε t
i + m
– 
i = 0 
under the assumption that innovations are IID α -stable laws of tail 
index α . By the properties of stable distributions it can be demonstrated 
that the finite-dimensional distributions of the process x are α -stable. 
However, restrictions on the coefficients need to be imposed. It can be 
demonstrated that a sufficient condition to ensure that the process x 
exists and is stationary is the following: 
∞
∑ hi 
α 
∞ 
< 
i = 0 
As we have seen in the previous section, a general univariate 
ARMA(p,q) model is written as follows: 
Xt = 
p 
∑ α iXt
i
– + 
q 
∑ α jZt
j
– 
i = 1 
j = 1 
where the Z are IID variables. 
Using the Lag Operator—L—notation, Li represents the variable at 
i lags, the ARMA(p,q) model is written as follows: 

382 
The Mathematics of Financial Modeling and Investment Management 
= 
j
Xt 
p 
∑ LiXt + 
q 
∑ L Zt 
i = 1 
j = 1 
The theory of ARMA processes developed in Chapters 11 and 12 
can be carried over at least partially to cover the case of fat-tailed inno-
vations. In particular, an ARMA(p,q) process with IID α -stable innova-
tions admits a stationary, infinite moving average representation under 
the same conditions as in the classical finite-variance case. The coeffi-
cients of the moving average satisfy the condition 
∞
∑ hi 
α 
∞ 
< 
i = 0 
In the case of fat-tailed innovations, covariances, and autocovariances 
looses their meaning. It can also be demonstrated, however, that the 
empirical autocorrelation function is meaningful and is asymptotically 
normal. It can be demonstrated that maximum likelihood estimates can be 
extended to the infinite variance case, though through a number of ad hoc 
processes. 
ARCH/GARCH Processes 
As we saw in Chapter 12, The simplest ARCH model can be written as 
follows. Suppose that X is the random variable to be modeled, Z is a 
sequence of independent standard normal variables, and σ is a hidden 
variable. The ARCH(1) model is written as 
Xt = σ tZt 
σ 2
2 
= β
δ
 
Xt
t 
+
– 1 
This basic model was extended by Bollerslev17 who proposed the 
GARCH(p,q) model written as 
Xt = σ tZt 
17 Tim Bollerslev, “Generalized Autoregressive Conditional Heteroscedasticity,” 
Journal of Econometrics 31 (1989), pp. 307–327. 

383 
Fat Tails, Scaling, and Stable Laws 
p
q 
2 
2
2
σt = β + ∑γ iσt
i + ∑δiXt
i
–
– 
i = 1 
i = 1 
The IID variables Z can be standard normal variables or other symmet-
rical, eventually fat-tailed, variables. 
Let’s first observe that model parameters must be constrained in 
order to guarantee the stationarity of the model. Stationarity conditions 
depend on each model. No general simple expression for the stationarity 
conditions is available. 
Due to the multiplicative nature of noise, GARCH models are able 
to generate fat-tailed distributions even if innovations have finite vari-
ance. This fact was established by Kesten18 in 1973. The tail index can 
be theoretically computed at least in the case GARCH(1,1). Suppose a 
GARCH(1,1) stationary process with Gaussian innovation is given. It 
can be demonstrated that 
( 
c
P X  > x) ≈ --x –2κ 
2 
where κ is the solution of an integral equation. In the generic p, q case, 
the return process is still fat-tailed but no practical way to compute the 
index from model parameter is known. 
Subordinated Processes 
Subordinated processes allow the time scale to vary. Subordinated mod-
els are, in a sense, the counterpart of stochastic volatility models insofar 
as they model the change in volatility by contracting and expanding the 
time scale. The first model was proposed in 1973 by Clark.19 Subordi-
nated models have been extensively studied by Ghysels, Gourieroux, 
and Josiak.20 
Subordinated models can be applied quite naturally in the context 
of trading. Individual trades are randomly spaced. In modern electronic 
exchanges, the time and size of trades are individually recorded thus 
allowing for accurate estimates of the distributional properties of inter-
trades intervals. Consideration of random spacings between trades natu-
18 H. Kesten, “Random Difference Equations and Renewal Theory for Products of 
Random Matrices” Acta Mathematica 131 (1973), pp. 207–248. 
19 P.K. Clark, “A Subordinated Stochastic Process Model with Finite Variance for 
Speculative Prices,” Econometrica 41 (January 1973), pp. 735–755. 
20 E. Ghysels, C. Gourieroux, and J. Josiak, “Market Time and Asset Price Move-
ment Theory and Estimation,” Working Paper 95-32 Cyrano, Montreal, 1995. 

384 
The Mathematics of Financial Modeling and Investment Management 
rally leads to the consideration of subordinated models. Subordinated 
models generate unconditional fat-tailed distributions. 
Markov Switching Models 
The GARCH family of models is not the only family of serially corre-
lated models able to produce fat tails starting from normally distributed 
innovations. State-space models and Markov-switching models present 
the same feature. The basic ideas of state-space models and Markov 
switching models is to split the model into two parts: (1) a regressive 
model that regresses the model variable over a hidden variable and (2) 
an autoregressive model that describes the hidden variables. 
In its simplest linear form, a state-space model is written as follows: 
Xt = αZt + εt 
Zt =
+ δt
βZt – 1 
where εt, δt are normally distributed independent white noises. State-
space models can also be written in a multiplicative form: 
Xt =
+ εt
αZt – 1 
αt = βαt – 1 + δt 
If the second equation is a Markov chain, the model is called a 
Markov-switching model. A well-known example of Markov-switching 
models is the Hamilton model in which a two-state Markov chain drives 
the switch between two different regressions. 
Purely linear state-space models exhibit fat tails only if innovations 
are fat-tailed. However, multiplicative state-space models and Markov-
switching models can exhibit fat tails even if innovations are normally 
distributed. There is a growing literature on Markov-switching and mul-
tiplicative state-space models and a relatively large number of different 
models, univariate as well as multivariate, have been proposed. Stochas-
tic volatility models are the continuous-time version of multiplicative 
state-space models. 
Estimation 
Let’s now go back to the question of model estimation in a non-IID frame-
work. Suppose that we want to estimate the tail index of the unconditional 
distribution of a set of empirical observations in the general setting of non-

385 
Fat Tails, Scaling, and Stable Laws 
IID variables. Note that if variables are fat-tailed, we cannot say that they 
are serially autocorrelated as moments of second order generally do not 
exist. Therefore we have to make some hypothesis on the DGP. 
There is no general theory of estimation under arbitrary DGP. Both 
theoretical and simulation work are limited to specific DGPs. ARMA 
models have been extensively studied. EVT holds for ARMA models 
under general non-clustering conditions.21 
Often only simulation results are available. A fairly ample set of 
results are available for GARCH(1,1) models. For these models Resnick 
and Starica22 showed that the Hill estimator is a consistent estimator of 
the tail index. Wagner and Marsh compared the performance of the Hill 
estimator and of the moment ratio estimator for three model classes: IID 
α-stable returns, IID symmetric student, and GARCH(1,1) with student-
t innovation. They found that, in an adoptive framework, the moment 
ratio estimator generally yields results superior to the Hill estimator. 
Scaling and Self-Similarity 
The concept of scaling is now quite frequently evoked in economics and 
finance. Let’s begin by making a distinction between scaling and self-
similarity and some of the properties associated with inverse power laws 
within or outside the Levy-stable scaling regime. These concepts have 
different, and not equivalent, definitions. 
The concepts of scaling and self-similarity apply to distributions, 
processes or structures. Self-similarity was introduced as a property that 
applies to geometrical self-similar objects (i.e., fractal structures). In this 
context, self-similarity means that a structure can be put into a one-to-
one correspondence with a part of itself. Note that no finite structure 
can have this property; self-similarity is the mark of infinite structures. 
Self-similarity entails scaling: If a fractal structure is expanded by a 
given factor, its measure expands by a power of the same factor.23 The 
notion of scaling is often expressed as absence of scale, meaning that a 
scaling object looks the same at any scale, large or small: It is impossible 
to ascertain the size of a portion of a scaling object by looking at its 
shape. The classical illustration is a Norwegian coastline with its fjords 
and fjords within fjords that look the same regardless of the scale. 
21 See Embrechts, Kluppelberg, and Mikosch, Modelling Extremal Events for Insur -
ance and Finance. 
22 S. Resnick and C. Starica, “Tail Index Estimation for Dependent Data,” Annals of 
Applied Probability 8 (1998), pp. 1156–1183. 
23 For an introduction to fractals, see J. Falconer, Fractal Geometry (Chichester, 
U.K.: John Wiley & Sons, 1990). 

386 
The Mathematics of Financial Modeling and Investment Management 
However, scaling can be defined without making reference to frac-
tals. In its simplest form, the notion of scaling entails a variable x and 
an observable A which is a function of A = A(x). If the observable obeys 
a scaling relationship, there is a constant factor between x and A in the 
sense that A(λx) = λsA(x), where s is the scaling exponent that does not 
depend on x. The only function A(x) that satisfies this relationship is a 
power law. In the three-dimensional Euclidean space, volume scales as 
the third power of linear length and surface as the second power, while 
fractals scale according to their fractal dimension. 
The same ideas can be applied in a random context, but require 
careful reasoning. A power-law distribution has a scaling property as 
multiplying the variable by a factor multiplies probabilities by a con-
stant factor, regardless of the level of the variable. This means that the 
ratio between the probability of the events X > x and X > ax depends 
only on a power of a, not on x. As an inverse power law is not defined 
at zero, scaling in this sense is a property of the tails. The probabilistic 
interpretation of this property is the following: the probability that an 
observation exceeds ax conditional on the knowledge that the observa-
tion exceeds x does not depend on x but only on a. 
There are, however, other meanings attached to scaling and these 
might be a source of confusion. In the context of physical phenomena, 
scaling is often intended as identity of distribution after aggregation. The 
same idea is also behind the theory of groups of renormalization and the 
notion of self-similarity applied to structures such as coastlines. In the lat-
ter case, the intuitive meaning of self-similarity is that if one aggregates 
portions of the coastline, approximating their shape with a straight line, 
and then rescales; the resulting picture is qualitatively similar to the origi-
nal. The same idea applies to percolation structures: By aggregating 
“sites” (i.e., points in a percolation lattice) into supersites and carefully 
redefining links, one obtains the same distribution of connected clusters. 
Applying the idea of aggregation in a random context, self-similar-
ity seems to mean that, after rescaling, the distribution of the sum of 
independent copies of a random variable maintains the same shape of 
the distribution of the variable itself. Note that this property holds only 
for the tails of subexponential distributions—and it holds strictly only 
for stable laws that have tails in the (0,2) range but whose shape is not a 
power law except, approximately, in the tails. It also holds for Gaussian 
distributions that do not have power-law tails. 
Scaling acquires yet another meaning when applied to stochastic pro-
cesses that are functions of time. The most common among the different 
meanings is the following: A stochastic process is said to have a scaling 
property if there is no natural scale for looking at its paths and distribu-
tions. Intuitively, this means that it is not possible to gauge the scale of a 

387 
Fat Tails, Scaling, and Stable Laws 
sample by looking at its distribution; there is absence of scale. An exam-
ple from finance comes from price patterns. If a price pattern is generated 
by a process with the scaling property, the plots of average daily and 
monthly prices will appear to be perfectly similar in distribution; looking 
at the plot, it’s impossible to tell if it refers to daily or monthly prices. 
Self-similarity is another way of expressing the same concept. A 
process is self-similar if a portion of the process is similar to the entire 
process. As we are considering a random environment, self-similarity 
applies to distributions, not to the actual realization of a process. Let’s 
now make these concepts more precise. 
A stochastic process X(t) is said to be self-similar (ss) of index H (H-
ss) if all its finite-dimensional distributions obey the scaling relationship: 
D 
…
…
k
(Xkt1, Xkt2,
 
,
 
Xkt ) = k –H(Xt1, Xt2,
 ,
 
Xt )
> 
∀ 
0 
m
m 
H
t2 …
0 <
 <
 
1 , t1,
,
 ,
 
t
> 0
m 
The above expression means that the scaling of time by the factor k 
scales the variables X by the factor kH. It gives precise meaning to the 
notion of self-similarity applied to stochastic processes. 
There is a wide variety of self-similar processes that cannot be charac-
terized in a simple way as scaling laws: The scaling property of stochastic 
processes might depend upon the shape of distributions as well as the 
shape of correlations. Let’s restrict our attention to processes that are self-
similar with stationary increments (sssi) and with index H (H-sssi). These 
processes can be either Gaussian or non-Gaussian. Note that a Gaussian 
process is a process whose finite-dimensional distributions are all Gaussian. 
Gaussian H-sssi processes might have independent increments or 
exhibit long-range correlations. The only Gaussian H-sssi process with 
independent increment is the Brownian motion, but there are an infinite 
number of fractional Brownian motions, which are Gaussian H-sssi pro-
cesses with long-range correlations. Thus there are an infinite variety of 
Gaussian self-similar processes. Among the many non-Gaussian H-sssi 
processes with independent increments are the stable Levy processes, 
which are random walks whose increments follow a stable distribution.24 
There is another definition of self-similarity for stochastic processes 
which makes use of the concept of aggregation; it is closer, at least in 
spirit, to the theory of renormalization groups. Consider a stationary 
24 See G. Samorodnitsky and M.S. Taqqu, Stable Non-Gaussian Random Processes 
(New York: Chapman & Hall, 1994). 

388 
The Mathematics of Financial Modeling and Investment Management 
infinite sequence of independent and identically distributed variables Xi, 
i ≥1. Create consecutive nonoverlapping blocks of m variables and 
define the corresponding aggregated sequence of level m averaging over 
each block as follows: 
km 
Xk
m
(
)
 
1 
= ----
∑ 
Xi 
mi = (k – 1)m +1
A sequence is called exactly self-similar if, for any integer m the fol-
lowing relationship holds: 
D 
(
)
X = m 1 – HX m
A stationary sequence is called asymptotically self-similar if the above 
relationship holds only for m →∞. 
When we apply the notion of scaling to stochastic processes—the 
natural setting for economics and finance—we have to abandon the sim-
ple characterization of scaling as inverse power laws. Though the scal-
ing property is in itself characterized through simple power laws, the 
scaling processes are complex and rich mathematical structures entail-
ing a variety of distributions and correlation functions. In particular, the 
long-range correlation structure of the process plays a role as important 
as the distribution of its variables. 
EVIDENCE OF FAT TAILS IN FINANCIAL VARIABLES 
To appreciate the applicability of scaling laws, let’s first look at the range of 
variation of the economic and financial variables with which they are gen-
erally associated. Variables such as income, personal wealth, corporate size, 
and market capitalization span many orders of magnitude. Large insurance 
claims cover at least three orders of magnitude, with the largest claims 
reaching billions of dollars.25 Bankruptcies cover a similarly broad range of 
orders of magnitude.26 Daily stock returns span some two orders of magni-
tude. However, economic variables such as interest rates or GNP rates span 
a smaller set of values. Obviously the range of variables is not in itself a 
25 See Embrechts, Kluppelberg, and Mikosch, Modelling Extremal Events for Insur-
ance and Finance. 
26 For empirical evidence on the Japanese experience, see H. Aoyama, Y. Nagahara, 
M. P. Okazaki, W. Souma, H. Takayasu, and M. Takayasu, “Pareto’s Law for In-
come of Individuals and Debt of Bankrupt Companies,” Cond-Mat 0006038, 2000. 

389 
Fat Tails, Scaling, and Stable Laws 
sign of scaling or inverse power laws, but these variables cover a broad 
enough range of values to make the scaling approximation meaningful. 
The first example of scaling laws in economics is due to the econo-
mist Pareto in the nineteenth century. Pareto observed that, above some 
threshold, the proportion of individuals with an income in excess of x is 
inversely proportional to x. Generalizing, a distribution of the type
F x
( 
1
( ) = P X  > x) = ----- for x ≥1 
α 
x 
is called a Pareto law. 
The presence of scaling laws has also been researched in price 
behavior. In 1963 Mandelbrot27 observed self-similarity in economic 
time series when he discovered that cotton price time series had approx-
imately the same shape at different time scales. Based on this empirical 
discovery, Mandelbrot later proposed stable laws and fractional Brown-
ian motions as a model for price behavior. 
Since Mandelbrot’s observations, researchers have been trying to 
prove or disprove the existence of inverse power laws in the area of 
asset returns. The jury is still out. A first remark is that scaling laws of 
returns apply only to short-term (from one minute to a few days) 
returns. Beyond this time horizon, returns exhibit complex behavior 
that depends on the length and positioning of the observation periods. 
One of the first systematic studies of the distribution of high-fre-
quency data was conducted by Zurich-based Olsen & Associates on 
exchange rates.28 Olsen researchers found that many exchange rates fol-
low scaling laws with exponents < 2. More recently, several as yet 
unpublished studies have look at fat-tailed returns in less traded curren-
cies: Payaslioglu29 used tail index estimation for the Turkish lira and 
Chobanov, Mateev, Mittnik and Rachev30 looked at the Bulgarian lev. 
27 Benoit Mandelbrot, “The Variation of Certain Speculative Prices,” Journal of 
Business 36 (1963), pp. 394–419. 
28 U.A. Muller, M.M. Dacorogna, and O.V. Pictet, “Heavy Tails in High Frequency 
Financial Data,” in R. Adler, R. Feldman, and M.S. Taqqu (eds.) A Practical Guide 
to Heavy Tails: Statistical Techniques for Analysing Heavy-Tailed Distributions 
(Boston: Birkhauser, 1997). 
29 Cem Payaslioglu, “Tail Behavior of Return Distributions of Exchange Rates under 
Different Regimes: A Case Study for Turkey.” 
30 G. Chobanov, P. Mateev, S. Mittnik, and S. Rachev, “Modeling the Distribution 
of Highly Volatile Exchange-rate Time Series” in P.M. Robinson and M. Rosenblatt 
(eds.), Athens Conference on Applied Probability and Time Series, Volume II: Time 
Series Analysis (New York: Springer, 1996). 

390 
The Mathematics of Financial Modeling and Investment Management 
In the area of stock price returns at short time horizons, initial find-
ings by Mantegna and Stanley31 seemed to indicate truncated inverse 
power laws with exponents in the range 1.4–1.6, well within the scaling 
regime. More recent findings by Plerou et al32 point to an exponent 3 
without truncation, well outside the Levy stable regime. Johanson and 
Sornette33 suggest that market crashes are not the fat tails of return dis-
tributions, but outliers. Still other studies, for instance Laherre and Sor-
nette,34 found that returns are better described by a function rather than 
by a single exponent, thus creating multifractal distributions. 
Applying the notion of stable laws to stock price returns raises addi-
tional questions. The infinite variance property of stable laws is some-
what in contrast with empirical findings about stock returns, most of 
which seem to indicate finite variance, though higher order moments 
might become infinite. This is in agreement with the use of volatility as a 
key parameter in financial risk management. Stable laws, on the other 
hand, would require abandoning the notion of volatility. It seems fair to 
conclude that stable laws are not a good approximation to stock 
returns, though inverse power laws with exponent >2 might still hold. 
As noted above, the fundamental practical importance of the pres-
ence of stable laws in economic and financial phenomena is that they 
would render risk management and financial decision-making difficult: 
If variables are governed by stable laws, there is no possibility of diver-
sifying risk. Modeling with fat-tailed distributions has the status of a 
theoretical hypothesis as it implies extrapolating that the future will 
bring unbounded innovation. In the insurance industry, for example, the 
assumption of scaling is appropriate in domains such as catastrophe 
insurance, where there is no natural bound to the size of catastrophes 
and where experience has shown that very large catastrophic events do 
indeed occur. 
31 R. N. Mantegna and H.E. Stanley, “Scaling Behavior in the Dynamics of an Eco-
nomic Index,” Nature 46 (1995), p. 376. 
32 V. Plerou, P. Gopikrishnan, L.A.N. Amaral, M. Meyer, and H.E. Stanley, “Scaling 
of the Distribution of Price Fluctuations of Individual Companies,” Physical Review 
E 60, no. 6, Part A (December 1999), pp. 6519–6529 
33 A. Johansen and D. Sornette, “Stock Market Crashes Are Outliers,” European 
Physical Journal B 9, no. 1 (February 1998), pp. 141–143. 
34 J. Laherre and D. Sornette, “Stretched Exponential Distributions in Nature and 
Economy: ‘Fat Tails’ with Characteristic Scales,” European Physical Journal B 2 
(1998), p. 525. 

391 
Fat Tails, Scaling, and Stable Laws 
ON THE APPLICABILITY OF EXTREME VALUE 
THEORY IN FINANCE 
In financial applications, EVT for fat-tailed processes has been applied to 
questions of risk management and portfolio optimization, especially port-
folios with exposure to credit risk. 
We can illustrate the importance of fat-tailed processes in credit risk 
management using an example prepared by Srichander Ramaswamy35 
Exhibit 13.4 shows the credit risk of a 23-corporate bond portfolio 
under different modeling assumptions. Risk values in the first column 
are computed considering default losses under the assumption that joint 
asset return distribution is normal. Values in the second column are 
computed under the same distributional assumptions but consider not 
only default losses but also the losses incurred due to rating migration. 
The values in the third column are computed under the assumption that 
the joint distribution of asset returns is a multivariate t with 8 degrees 
of freedom. 
The risk measures considered are Unexpected Loss (UL) measured 
by the standard deviation in the second row, credit risk Value-at-Risk 
(CrVaR) in the third row, and Expected Shortfall Risk (ESR) in the 
fourth row. (We will discuss these measures in Chapter 22, where we 
cover risk management.) The Expected Loss tabulated in the first row is 
a measure of credit cost and not of risk. 
As explained in Chapter 22, under the assumption of multivariate 
normality, the three risk measures UL, VaR, and ES are equivalent; how-
ever, if we drop this assumption, the three risk measures are no longer 
equivalent. Observe, in particular, that moving from a multivariate nor-
EXHIBIT 13.4 
Portfolio Credit Risk Measures Under Different Modeling 
Assumptions 
Default Mode 
Migration Mode Migration Mode 
and Multivariate and Multivariate and Multivariate 
Description 
Normal 
Normal 
t-Distributed 
Expected loss
 13.9 bp
 34.1 bp
 34.0 bp 
Unexpected loss
 65.9 bp
 88.9 bp 
105.1 bp 
CrVaR at 90% confidence
 0.0 bp 
102.9 bp
 96.6 bp 
ESR at 90% confidence 
139.0 bp 
240.3 bp 
256.2 bp 
35 This illustration is adapted from his book, Managing Credit Risk in Corporate 
Bond Portfolios: A Practitioner’s Guide (Hoboken, NJ: John Wiley & Sons, 2004). 

392 
The Mathematics of Financial Modeling and Investment Management 
mal to a multivariate t CrVaR drops from 102.9 basis points to 96.6 basis 
points but ES grows from 240.3 basis points to 256.2 basis points. This 
happens because the t-distribution is more fat-tailed than the normal dis-
tribution. As a consequence, VaR underestimates the risk of large losses. 
Though there are still questions as to whether asset prices have a 
finite variance, there is little doubt that financial time series are not 
Gaussian. Large events happen at a rate incompatible with Gaussian 
behavior. This problem must be addressed from the point of view of 
both risk management and financial optimization. 
Many issues regarding risk management have been discussed in the 
literature. A number of key issues are summarized by Mulvey who 
points out the need to correctly address problems stemming from conta-
gion phenomena and from the possibility of joint actions such as those 
occurring in market crashes.36 A better understanding of the dynamics 
of these events could lead to effective measures to protect market partic-
ipants from unnecessary risk. 
SUMMARY
 ■ Fat-tailed laws have been found in many economic variables
 ■ Fully approximating a finite economic system with fat-tailed laws 
depends on an accurate statistical analysis of the phenomena, but also 
on a number of the theoretical implications of subexponentiality and 
scaling.
 ■ Modeling financial variables with stable laws implies the assumption of 
infinite variance, which seems to contradict empirical observations.
 ■ Scaling laws might still be an appropriate modeling paradigm given the 
complex interaction of distributional shape and correlations in price 
processes.
 ■ Scaling laws might help in understanding not only the sheer size of eco-
nomic fluctuations but also the complexity of economic cycles. 
36 John M. Mulvey, “Risk Management Systems for Long-term Investors: Address-
ing/Managing Extreme Events,” Working Paper, May 2001, Operations Research 
and Financial Engineering Department, Bendheim Center for Finance, Princeton 
University. 


## Portfolio Selection & CAPM

CHAPTER 16 
Portfolio Selection Using 
Mean-Variance Analysis 
A
s explained in Chapter 3, a major step in the direction of the quanti-
tative management of portfolios was made in the 1950s by Harry 
Markowitz in his paper “Portfolio Selection” published in 1952 in the 
Journal of Finance.1 The ideas introduced in this article have come to 
form the foundations of what is now popularly referred to as mean-vari-
ance analysis (M-V analysis) for reasons explained in this chapter, and 
Modern Portfolio Theory (MPT). Initially, M-V analysis generated rela-
tively little interest, but with time, the financial community adopted the 
thesis, and now 50 years later, financial models based on those very 
same principles are constantly being reinvented to incorporate new find-
ings that result from that seminal work. 
Though widely applicable, M-V analysis has had the most influence 
in the practice of portfolio management. In its simplest form, M-V anal-
ysis provides a framework to construct and select portfolios based on 
the expected performance of the investments and the risk appetite of the 
investor. M-V analysis also introduced a whole new terminology, which 
now has become the norm in the area of investment management. 
It may be useful to mention here that the theory of portfolio selec-
tion is a normative theory. A normative theory is one that describes a 
standard or norm of behavior that investors should pursue in construct-
ing a portfolio, in contrast to a theory that is actually followed. Asset 
1 Harry M. Markowitz, “Portfolio Selection,” Journal of Finance (March 1952), pp. 
77–91. In 1959 Markowitz expanded his ideas in book form: Harry M. Markowitz, 
Portfolio Selection: Efficient Diversification of Investments (New York: John Wiley, 
1959). 
471 

472 
The Mathematics of Financial Modeling and Investment Management 
pricing theory such as the capital asset pricing model, which we discuss 
in the next chapter, goes on to formalize the relationship that should 
exist between asset returns and risk if investors constructed and selected 
portfolios according to mean-variance analysis. In contrast to a norma-
tive theory, asset pricing theory is a positive theory—a theory that 
hypothesizes how investors behave rather than how investors should 
behave. Based on that hypothesized behavior of investors, we derive an 
asset pricing model that provides the expected return is derived. 
Our objective in this chapter is to explain the principles of mean-vari-
ance analysis and present a formal mathematical treatment for determin-
ing “efficient portfolios.” The extensions of Markowitz’s formulation 
includes the case where a risk-free asset is available in the capital mar-
ket. This leads to efficient portfolio’s that dominate efficient portfolios 
that can be constructed in a capital market in which there is no risk-free 
asset. We then provide an application of how M-V analysis is used in 
portfolio selection. While there have been many applications of M-V 
analysis in the areas of finance and insurance, we present an application 
to the asset allocation problem. This decision involves deciding how to 
allocate funds across major asset classes. 
DIVERSIFICATION AS A CENTRAL THEME IN FINANCE 
Conventional wisdom has always dictated “not putting all your eggs in 
one basket.” In more technical terms, this old adage is addressing the 
benefits of diversification. Markowitz quantified the concept of diversifi-
cation, or “undiversification” through the statistical notion of covari-
ance, or correlation. In essence, the old adage is saying that putting all 
your money in investments that may all perform poorly at the same 
time—that is, whose returns are highly correlated—is not a very prudent 
investment strategy—no matter how small the chance is that any one 
single investment will perform poorly. This is because if any one single 
investment performs poorly, it is very likely, due to its high correlation 
with the other investments, that the other investments are also going to 
perform poorly, leading to the poor performance of the portfolio. 
The concept of diversification is so intuitive and so strong that it has 
been continuously applied to different areas within finance. Indeed, a 
vast number of the innovations surrounding finance have either been an 
application of the concept of diversification, or the introduction of new 
methods of obtaining improved estimates of the variances and covari-
ances, thereby, allowing for a more precise measure of diversification, 
and consequently, for a more precise measure of risk. 

473 
Portfolio Selection Using Mean-Variance Analysis 
Markowitz considered an investor who, at time t, decides what 
portfolio of investments to choose; the time horizon of the investor is 
∆t. The investor makes decisions on the gains and losses he or she will 
make at time t + ∆t, without considering eventual gains and losses either 
during or after the period ∆t. At time t + ∆t, the investor will reconsider 
the situation and decide anew; this last condition is called myopic. 
Nonmyopic investment strategies must be adopted when it is necessary 
to make trade-offs at future dates between consumption and investment or 
when significant trading costs related to specific subsets of investments are 
incurred. We will handle these issues later in this chapter and when we dis-
cuss bond portfolio management in Chapter 21 where we apply the multi-
stage optimization technology discussed in Chapter 7.2 
Markowitz reasoned that investors should decide on the basis of a 
trade-off between risk and return. He made the assumption that returns 
are normally distributed and that risk is measured by the variance of the 
return distribution. In the 1950s when asset pricing theories were not 
yet developed, the assumption of joint normality of returns was a rea-
sonable statistical assumption. It was based on the fact that asset 
returns are influenced by many different independent facts. Recall from 
Chapter 6 on probability theory that the sum of many small random 
disturbances tends to a normal distribution. 
Markowitz argued that for any given level of expected returns 
investors should choose the portfolios with minimum variance from 
amongst the set of all possible portfolios that can be constructed. The 
set of all possible portfolios that can be constructed is called the feasible 
set. In this simple one-period model, variance of returns is a measure of 
uncertainty and thus of risk. Minimum variance portfolios are called 
mean-variance-efficient portfolios. The set of all mean-variance efficient 
portfolios is called the efficient frontier. 
Exhibit 16.1 presents the MPT investment process (mean-variance 
optimization or the theory of portfolio selection). Notice in the exhibit 
that the result of the analysis is the selection of the optimal portfolio. 
We describe what is meant by an optimal portfolio later in this chapter. 
Though its implementation can get quite complicated, the theory is 
relatively straightforward. Here we want to give an intuitive and practi-
cal view of MPT. The theory dictates that given estimates of the returns, 
volatilities, and correlations of a set of investments, and constraints on 
investment choices (for example, maximum exposures and turnover 
2 There are applications of multistage optimization in equity portfolio management 
though these are not as common in the bond portfolio management area. See, for ex-
ample, John M. Mulvey and Hercules Vladimirou, “Stochastic Network Optimization 
Models for Investment Planning,” Management Science 38, no. 11, pp. 1642–1664. 

474 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 16.1 
The MPT Investment Process 
Source: Exhibit 2 in Frank J. Fabozzi, Francis Gupta, and Harry M. Markowitz, 
“The Legacy of Modern Portfolio Theory,” Journal of Investing (Fall 2002), p. 8. 
constraints) it is possible to perform an optimization that results in the 
risk-return or mean-variance efficient frontier.3 This frontier is efficient 
because underlying every point on this frontier is a portfolio that results 
in the greatest possible return for that level of risk, or results in the 
smallest possible risk for that level of return. The portfolios that lie on 
the frontier make up the set of efficient portfolios. 
When the efficient frontier is constructed using the M-V formula-
tion developed by Markowitz, they are referred to as Markowitz effi-
cient portfolios and the set or frontier of these portfolios is called the 
Markowitz efficient frontier. Exhibit 16.2 provides a graphical depiction 
of the Markowitz efficient frontier based on the feasible portfolios that 
can be constructed. The Markowitz efficient frontier is the upper por-
tion of the curve from II to III. 
MARKOWITZ’S MEAN-VARIANCE ANALYSIS 
Let’s now place the above in a formal mathematical context developing 
the analysis of mean-variance optimization. Suppose first that an inves-
tor has to choose a portfolio formed of N risky assets. The investor’s 
choice is embodied in an N-vector w = {wi} of weights where each 
weight i represents the percentage of the i-th asset held in the portfolio. 
Suppose assets’ returns are jointly normally distributed with an N-vec-
3 In practice this optimization is performed using an off-the-shelf asset allocation 
package. 

475 
Portfolio Selection Using Mean-Variance Analysis 
EXHIBIT 16.2 
Feasible and Markowitz Efficient Portfoliosa 
a The picture is for illustrative purposes only. The actual shape of the feasible region 
depends on the returns and risks of the assets chosen and the correlation among 
them. 
tor of expected returns µ = {µi} and an N×N variance-covariance matrix 
Σ = {σij}. Under these assumptions, the return of a portfolio a with 
weights wa = {wi}a is a random variable, which is the sum of normally 
distributed random variables. Therefore, it is a normally distributed 
random variable with the following mean and variance: 
µa = wa ′µ
σ2 = w ′Σw
a 
a
a 
For instance, if there are only two assets with weights wa ′ = {wa1wa2}, 
then the portfolios expected return is 
µa = wa1µ1 + wa2µ2 

476 
The Mathematics of Financial Modeling and Investment Management 
and its variance is 
σ2 
wa1 wa2 
σ11 σ12 w1
= 
a 
σ21 σ22 w2 
= {wa1σ11 + wa1σ21 wa2σ12 + wa2σ22} w1 
w2 
= 
2 σ11 + wa2
wa1
2 σ22 + 2wa1wa2σ12 
2
2 
= w2 σ1 + w2 σ2 + 2wa1wa2σ12
a1 
a2 
By choosing the portfolio’s weights, an investor chooses among the 
available mean-variance pairs. Following Markowitz, the investor’s 
problem is a constrained minimization problem in the sense that the 
investor must seek 
min σ2
(
)
 
= min(w ′Σw )
a 
a
a 
subject to the constraints 
µa = wa ′µ
w ′ι = 1, ι′ = [1 1
,
, …, 1]
a 
This is a constrained optimization problem which can be solved 
with the method of Lagrange multipliers. Recall from Chapter 7 that 
this method transforms a constrained optimization problem into an 
unconstrained optimization problem by forming the Lagrangian, that is, 
the sum of the function to be optimized and a linear combination of the 
constraints. In this case, the Lagrangian is 
L = w ′Σw + δ1(µa – wa ′µ) + δ2(1 – w ′ι)
a
a 
a 
The original optimization problem becomes the problem of uncon-
strained maximization of the Lagrangian. To solve this problem, it is 
sufficient to set to zero the partial derivatives of the Lagrangian. Solving 
yields 
w
= g
hµa
+
a 
where g and h are two vectors which are functions of µ and Σ. 

477 
Portfolio Selection Using Mean-Variance Analysis 
Consider the mean-variance plane, that is, a two-dimensional Carte-
sian plane whose coordinates are mean and variance. In this plane, each 
portfolio is represented by a point. Consider now the set of all efficient 
portfolios with all possible efficient mean-variance pairs. This set is 
what we referred to earlier as the efficient frontier. Later in this chapter 
we show actual efficient frontiers. 
CAPITAL MARKET LINE 
As demonstrated by William Sharpe,4 James Tobin,5 and John Lintner 6 
the efficient set of portfolios available to investors who employ M-V anal-
ysis in the absence of a risk-free asset is inferior to that available when 
there is a risk-free asset.7 We present this formulation in this section.8 
Assume a risk-free asset with a risk-free return denoted by Rf. The 
investor has to choose a combination of the N risky assets plus the risk-
free asset. The weights wR = {wi}R do not have to sum to 1 as the remain-
ing part (1 – wR′ι ) can be invested in the risk-free asset. Note that this 
portion of investment can be positive or negative if we allow risk-free 
borrowing and lending. The portfolio’s expected return and variance are: 
µa = wR ′µ + (1 – wR ′ι)Rf 
σ2 = wR ′ΣwR
a 
The portfolio variance is the same expression as before because the 
risk-free asset has zero variance and zero covariances with the risky assets. 
4 William F. Sharpe, “Capital Asset Prices: A Theory of Market Equilibrium Under 
Conditions of Risk,” Journal of Finance (September 1964), pp. 425–442. 
5 James Tobin, “Liquidity Preference as a Behavior Towards Risk,” Review of Eco-
nomic Studies (February 1958), pp. 65–86. 
6 John Lintner, “The Valuation of Risk Assets and the Selection of Risky Investments 
in Stock Portfolios and Capital Budgets,” Review of Economics and Statistics (Feb-
ruary 1965), pp. 13–37. 
7 The portfolio selection model was further extended by Fischer Black in the case of 
a restriction on short selling. See “Capital Market Equilibrium with Restricted Bor-
rowings,” Journal of Business (July 1972), pp. 444–455. 
8 For a comprehensive discussion of these models and computational issues, see Har-
ry M. Markowitz (with a chapter and program by Peter Todd), Mean-Variance Anal-
ysis in Portfolio Choice and Capital Markets (New Hope, PA: Frank J. Fabozzi 
Associates, 2000, originally published in 1987). 

478 
The Mathematics of Financial Modeling and Investment Management 
The investor’s problem is again a constrained optimization problem 
that can be stated as 
min σ 2
(
)
 
= min( wR ′ ΣwR)
a 
subject to the constraints 
µ a = wR ′ µ + ( 1 – wR ′ ι) Rf 
This problem can be solved again with the method of Lagrange multipli-
ers. The Lagrangian is 
L = wR ′ ΣwR + d[µ a – wR ′ µ – ( 1 – wR ′ ι) Rf] 
Equating to zero the derivatives of the Lagrangian with respect to 
the weights and to the Lagrange multiplier d, we obtained the solution 
of the constrained minimization problem. The solution of this problem 
has an interesting feature that leads to the CAPM as we will see in the 
next chapter. In fact, developing the lengthy computations, the optimal 
portfolio weights can be written as 
wR = CΣ–1(µ – Rfι) 
µ a – Rf
C = --------------------------------------------------------
(µ – Rfι)′ Σ–1(µ – Rfι) 
The above formula shows that the weights of the risky assets of any 
minimum-variance portfolio are proportional to the same vector. The 
proportionality constant is C. Therefore, with a risk-free asset, all mini-
mum variance portfolios are a combination of the risk-free asset and of a 
given risky portfolio. This risky portfolio is called the tangency portfolio. 
With the exception of the tangency portfolio, the minimum variance 
portfolios that are a combination of the tangency portfolio and the risk-
free asset are superior to the portfolio on the Markowitz efficient frontier 
that has the same level of risk. 
Deriving the Capital Market Line 
To derive the Capital Market Line (CML), we begin with the efficient fron-
tier. In the absence of a risk-free asset, Markowitz efficient portfolios can 
be constructed as a constrained minimum problem based on expected 

479 
Portfolio Selection Using Mean-Variance Analysis 
return and variance, with the optimal portfolio being the one portfolio 
selected based on the investor’s preference (which later we will see is quan-
tified by the investor’s utility function). The efficient frontier changes, how-
ever, once a risk-free asset is introduced and assuming that investors can 
borrow and lend at the risk-free rate. This is illustrated in Exhibit 16.3. 
Every combination of the risk-free asset and the efficient portfolio 
M, which we referred to as the tangency portfolio in the previous sec-
tion, is shown on the line drawn from the vertical axis at the risk-free 
rate tangent to the Markowitz efficient frontier. All the portfolios on the 
line are feasible for the investor to construct. Portfolios to the left of 
portfolio M represent combinations of risky assets and the risk-free 
asset. Portfolios to the right of portfolio M include purchases of risky 
assets made with funds borrowed at the risk-free rate. Such a portfolio 
is called a leveraged portfolio because it involves the use of borrowed 
funds. The line from the risk-free rate that is tangent to the efficient 
frontier of risky assets is called the capital market line (CML). 
Let’s compare a portfolio on the CML to a portfolio on the 
Markowitz efficient frontier with the same risk in Exhibit 16.3. For 
EXHIBIT 16.3 
Capital Market Line and the Markowitz Efficient Frontier 

480 
The Mathematics of Financial Modeling and Investment Management 
example, compare portfolio PA, which is on the Markowitz efficient 
frontier, with portfolio PB, which is on the CML and therefore some 
combination of the risk-free asset and the efficient portfolio M. Notice 
that for the same risk the expected return is greater for PB than for PA. 
By Assumption 2, a risk-averse investor will prefer PB to PA. That is, PB 
will dominate PA. In fact, this is true for all but one portfolio on the 
CML, portfolio M, which is on the Markowitz efficient frontier. With 
the introduction of the risk-free asset, we can now say that an investor 
will select a portfolio on the CML that represents a combination of bor-
rowing or lending at the risk-free rate and the efficient portfolio M. 
We can derive a formula for the CML algebraically. Based on the 
assumption of homogeneous expectations regarding the inputs in the 
portfolio construction process, all investors can create an efficient port-
folio consisting of wf placed in the risk-free asset and wM in the tan-
gency portfolio, portfolio M, where w represents the corresponding 
percentage (weight) of the portfolio allocated to each asset. 
Thus, wf + wM = 1 or wf = 1 – wm. The expected return is equal to 
the weighted average of the expected returns of the two assets. There-
fore, the expected portfolio return, E(Rp), is equal to 
E(Rp) = wf Rf + wM E(RM) 
Since we know that wf = 1 – wM, we can rewrite E(Rp) as follows: 
E(Rp) = (1 − wM) Rf + wM E(RM) 
This can be simplified as follows: 
E(Rp) = Rf + wM [E(RM) − Rf] 
Earlier in this chapter we derived the variance of a portfolio con-
taining only two assets. The variance of the portfolio consisting of the 
risk-free asset and portfolio M is 
2
2
var(Rp) = wf var(Rf) + wM var(RM) + 2wf wM cov(Rf , RM) 
We know that the variance of the risk-free asset, var(Rf), is equal to 
zero. This is because there is no possible variation in the return since the 
future return is known. The covariance between the risk-free asset and 
portfolio M, cov(Rf,RM), is zero. This is because the risk-free asset has 
no variability and therefore does not move at all with the return on 
portfolio M which is a risky portfolio. Substituting these two values into 
the formula for the portfolio’s variance, we get 

481 
Portfolio Selection Using Mean-Variance Analysis 
2
var(Rp) = wM var(RM) 
In other words, the variance of the portfolio is represented by the 
weighted variance of portfolio M. We can solve for the weight of portfo-
lio M by substituting standard deviations for variances. Since the stan-
dard deviation is the square root of the variance, we can write 
SD(Rp) = wMSD(RM) 
and therefore 
SD(Rp ) 
wM = ---------------------
SD(RM ) 
If we substitute the above result and rearrange terms we get the CML: 
E RM ) – Rf
(
(
E Rp ) = Rf + ----------------------------- SD(Rp )
SD(RM ) 
What is Portfolio M? 
Now we know that portfolio M is pivotal to the CML; we now need to 
know what portfolio M is. That is, how does an investor construct port-
folio M? Eugene Fama demonstrated that portfolio M must consist of 
all assets available to investors, and each asset must be held in propor-
tion to its market value relative to the total market value of all assets.9 
That is, tangency portfolio M is the “market portfolio.” So, rather than 
referring to the market portfolio, we can simply refer to the “market.” 
Recall that using Lagrange multipliers we formally demonstrated in 
a previous section that in the presence of risk-free lending and borrow-
ing the optimal portfolio held by investors is made up of the risk-free 
asset and of one special portfolio called the tangency portfolio. This 
important property is called separation. We can now complete the previ-
ous demonstration: if risk-free lending and borrowing is allowed the 
market is M-V efficient and each investor holds the risk-free asset plus a 
portfolio proportional to the market. 
9 Eugene F. Fama, “Efficient Capital Markets: A Review of Theory and Empirical 
Work,” Journal of Finance (May 1970), pp. 383–417. 

482 
The Mathematics of Financial Modeling and Investment Management 
Risk Premium in the CML 
With homogeneous expectations, SD(RM) and SD(Rp) are the market’s 
consensus for the expected return distributions for portfolio M and 
portfolio p. The risk premium for the CML is 
E RM) – Rf
( 
----------------------------- SD(Rp)
SD(RM) 
Let’s examine the economic meaning of the risk premium. 
The numerator of the first term is the expected return from investing 
in the market beyond the risk-free return. It is a measure of the reward 
for holding the risky market portfolio rather than the risk-free asset. The 
denominator is the market risk of the market portfolio. Thus, the first 
term measures the reward per unit of market risk. Since the CML repre-
sents the return offered to compensate for a perceived level of risk, each 
point on the CML is a balanced market condition, or equilibrium. The 
slope of the CML (i.e., the first term) determines the additional return 
needed to compensate for a unit change in risk. That is why the slope of 
the CML is also referred to as the equilibrium market price of risk. 
The CML says that the expected return on a portfolio is equal to the 
risk-free rate plus a risk premium equal to the market price of risk (as mea-
sured by the reward per unit of market risk) times the quantity of risk for the 
portfolio (as measured by the standard deviation of the portfolio). That is, 
ERp = Rf + market price of risk × quantity of risk 
THE CML AND THE OPTIMAL PORTFOLIO 
Given that the new efficient frontier is the CML, how does one select the 
optimal portfolio? That is, how does one determine the optimal combi-
nation of the market portfolio and the risk-free asset in which to invest? 
This depends on the preferences of the investors. To understand this, we 
must introduce the notion of utility functions and indifference curves. 
Utility Functions and Indifference Curves 
In life there are many situations where entities (i.e., individuals and 
firms) face two or more choices. The economic “theory of choice” uses 
the concept of a utility function to describe the way entities make deci-
sions when faced with a set of choices. A utility function assigns a 
(numeric) value to all possible choices faced by the entity. The utility 

483 
Portfolio Selection Using Mean-Variance Analysis 
index has the property that pair a is preferred to pair b if and only if the 
utility of a is higher than that of b. The higher the value of a particular 
choice, the greater the utility derived from that choice. The choice that 
is selected is the one that results in the maximum utility given a set of 
constraints faced by the entity. 
The assumption that an investor’s decision-making process can be 
represented as optimization of a utility function goes back to Pareto (see 
Chapter 3). Utility functions can represent a broad set of preference 
ordering. The precise conditions under which a preference ordering can 
be expressed through a utility function have been widely explored in the 
literature.10 
In portfolio theory too, entities are faced with a set of choices. Dif-
ferent portfolios have different levels of expected return and risk. Also, 
the higher the level of expected return, the larger the risk. Entities are 
faced with the decision of choosing a portfolio from the set of all possi-
ble risk/return combinations. Whereas they like return, they dislike risk. 
Therefore, entities obtain different levels of utility from different risk/ 
return combinations. The utility obtained from any possible risk/return 
combination is expressed by the utility function. Put simply, the utility 
function expresses the preferences of entities over perceived risk and 
expected return combinations. 
A utility function can be expressed in graphical form by a set of 
indifference curves. Exhibit 16.4 shows indifference curves labeled u1, 
u2, and u3. By convention, the horizontal axis measures risk and the 
vertical axis measures expected return. Each curve represents a set of 
portfolios with different combinations of risk and return. All the points 
on a given indifference curve indicate combinations of risk and expected 
return that will give the same level of utility to a given investor. For 
example, on utility curve u1 there are two points u and u′, with u having 
a higher expected return than u′, but also having a higher risk. 
Because the two points lie on the same indifference curve, the inves-
tor has an equal preference for (or is indifferent between) the two 
points, or, for that matter, any point on the curve. The (positive) slope 
of an indifference curve reflects the fact that, to obtain the same level of 
utility, the investor requires a higher expected return in order to accept 
higher risk. For the three indifference curves shown in Exhibit 16.4, the 
utility the investor receives is greater the further the indifference curve is 
from the horizontal axis because that curve represents a higher level of 
return at every level of risk. Thus, for the three indifference curves 
shown in the exhibit, u3 has the highest utility and u1 the lowest. 
10 See, for example, Akira Takayama, Mathematical Economics (Cambridge, U.K.: 
Cambridge University Press, 1985). 

484 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 16.4 
Indifference Curves 
Selection of the Optimal Portfolio 
A reasonable assumption is that investors are risk averse. A risk-averse 
investor is an investor who, when faced with choosing between two 
investments with the same expected return but two different risks, pre-
fers the one with the lower risk. 
In selecting portfolios, an investor seeks to maximize the expected 
portfolio return given his tolerance for risk. Given a choice from the set 
of efficient portfolios, the optimal portfolio is the one that is preferred 
by the investor. In terms of utility functions, the optimal portfolio is the 
efficient portfolio which has the maximum utility. 
The particular efficient portfolio on the CML that the investor will 
select will depend on the investor’s risk preference. This can be seen in 
Exhibit 16.5, which is the same as Exhibit 16.2 but has the investor’s 
indifference curves included. The investor will select the portfolio on the 
CML that is tangent to the highest indifference curve, u3 in the exhibit. 
Notice that without the risk-free asset, an investor could only get to 
u2, which is the indifference curve that is tangent to the Markowitz effi-
cient frontier. Thus, the opportunity to borrow or lend at the risk-free 
rate results in a capital market where risk-averse investors will prefer to 

485 
Portfolio Selection Using Mean-Variance Analysis 
EXHIBIT 16.5 
Optimal Portfolio and the Capital Market Line 
hold portfolios consisting of combinations of the risk-free asset and the 
tangency portfolio M on the Markowitz efficient frontier. 
EXTENSION OF THE MARKOWITZ MEAN-VARIANCE MODEL TO 
INEQUALITY CONSTRAINTS 
The earlier optimization model introduced by Markowitz is useful from 
a theoretical point of view, but it is insufficient from the point of view of 
a portfolio manager who wants to optimize a real portfolio. In fact, the 
above model has a number of serious shortcomings. In the next chapter 
we will introduce the notion of systematic risk and nonsystematic risk. 
A limitation of the Markowitz model presented above is that it only 
minimizes systematic risk given a target expected return, but it does not 
set any objectives for systematic risk. The latter can be set by constrain-
ing the portfolio exposure to selected risk factors. We will discuss these 
risk factors in the next chapter. 

486 
The Mathematics of Financial Modeling and Investment Management 
Suppose asset returns are determined by a multifactor model (as 
described in Chapter 18) so that the expected return of the i-th security 
is a linear combination of p factors. We can then write 
p 
µi = αi + ∑βijfj , j = 1,2,..., p 
j = 1 
where µi are expected returns and fj are the expectations of factors. 
Exposure to the j-th factor can be controlled by constraining the 
beta βaj of portfolio a relative to that factor: 
N 
∑ waiβij = βaj 
i = 1 
where wai are the weights of portfolio a. 
A portfolio manager might want to maximize a portfolio’s return 
given a target level of risk. This problem would lead to maximizing a 
linear function subject to quadratic constraints of the form 
w ′Σw
= w
a
a 
a 
In practice, however, a portfolio manager prefers to minimize a 
function of the type: 
w ′Σw – λwa ′µ
a
a 
where µ is the vector of securities’ expected returns and λ is a risk-aver-
sion parameter. A function of this type implements a compromise 
between risk and returns. 
Finally, a portfolio manager needs to impose lower thresholds on 
portfolio weights to avoid portfolios being made up of a large number 
of small holdings. This implies the constraints wai ≥ bi. In practice, 
therefore, mean-variance portfolio selection leads to a quadratic optimi-
zation problem of the following type: 
Minimize 
w ′Σw – λwa ′µ
a
a 
subject to 

487 
Portfolio Selection Using Mean-Variance Analysis 
Aw
= c
a 
and 
wai ≥ bi 
where the equation Aw
= c constrains sector exposure. This is a qua-
a 
dratic programming problem of the type described in Chapter 7. 
In addition to the above, managers might want to impose turnover 
or tradability constraints in the sense that assets can only be traded in 
given lots. As observed in Chapter 7, these constraints result in a mixed-
integer programming problem, which is generally more difficult to solve 
than quadratic programming problems. 
The technology of optimization is presently available on desktop 
computers. Mathematical software such as Matlab routinely solves qua-
dratic portfolio optimization problems of the type described above. 
However special care is still needed in applying optimization technol-
ogy. In fact, optimization is sensitive to expected return forecasts that 
are themselves typically unreliable.11 
A SECOND LOOK AT PORTFOLIO CHOICE 
The mean-variance framework suggested by Markowitz is based on util-
ity functions defined on expected returns and variance. We now have to 
generalize the optimization framework proposed by Markowitz in a 
fully probabilistic setting. This generalization allows the consideration 
of nonnormal distributions and paves the way for multiperiod portfolio 
choice. The three key ingredients in a portfolio optimization methodol-
ogy are (1) a return forecast, (2) a utility function, and (3) an optimizer. 
The Return Forecast 
The return forecast has to be intended as a probabilistic forecast. This 
means that models supply a joint pdf of all the assets that might contrib-
ute to forming the optimal portfolio. A return forecast implies a process 
dynamics. 
The first, and simplest, dynamics is the assumption that returns are 
independent and identical normal (IIN) variables and, therefore, price 
11 See, for example, Peter Muller, “Empirical Tests of Biases in Equity Portfolio Op-
timization,” in Stavros Zenios (ed.), Financial Optimization (Cambridge, MA, Cam-
bridge University Press, 1993). 

488 
The Mathematics of Financial Modeling and Investment Management 
processes are random walks. This assumption entails that the expected 
returns of each asset are known constants. Later in this chapter we will 
consider autoregressive linear models and nonlinear models that follow 
a more complex dynamics than the assumption of IID variables. 
The Utility Function 
In the mean-variance framework, utility functions are defined on 
expected returns and variances. The probability structure of returns is 
summarized by returns and variances. Utility functions express the 
trade-off between risk and return preferred by the investor or by the 
asset manager. By choosing a utility function, an investor decides how 
much return he or she wants to be compensated for taking more risk. 
The choice of utility functions is dictated by (1) a question of mathemat-
ical and computational tractability and (2) the risk-return preferences of 
the investor. 
In the one-period framework of Markowitz, utility is a function of 
two variables: mean and variance. In this way, the problem of portfolio 
choice becomes a problem of finding the return-variance pair with the 
maximum utility: 
arg maxU( w ⁄ µ, Σ) 
where “arg” is shorthand to denote “argument” and with the con-
straints 
µ a = wa ′ µ
w′ι = 1 , ι′ = [ 1 1
,
, …, 1] 
This is a problem of constrained maximum. Additional constraints 
might be imposed, for instance, that weights are all positive and/or that 
weights are within given intervals. The first condition precludes short 
selling; the second condition ensures that no asset has a weight either 
too big or too small. 
In a more general probabilistic setting, utility functions are defined on 
the variables of interest, be they returns or consumption. The investor’s risk 
preference is represented by the shape of the utility function. A linear func-
tion corresponds to risk neutrality. A concave function, that is, a function 
with negative second derivative, expresses risk aversion in so far as utility 
grows less rapidly than the variable. 
A formal measure of absolute risk aversion is defined as

489 
Portfolio Selection Using Mean-Variance Analysis 
x
x
x
rA( ) = –U″( ) ⁄ U′( )  
This measure expresses the intuitive fact that the more the utility func-
tion is curved, the more the investor is risk-averse. Listed below are 
some examples of utility functions:
 ■ Linear utility function: 
U x
+ 
x
x
( ) = a
bx
 
, U′( ) = b , U″( ) = 0 
The linear function is not concave; it represents a risk-neutral investor.
 ■ Power utility function: 
1 – a 
x 
– 1
U x
x
x
( ) = --------------------- , U′( ) = x –a , U″( ) = –ax – a – 1 < 0 
1 – a 
The power utility function is concave; it represents a risk-averse investor.
 ■ Logarithmic utility function: 
( ) = ln ( ) , U′( ) = 1 ⁄ x , U″( ) = –1 ⁄ x 2 < 0
U x
x
x
x
The logarithmic utility function is concave; it represents a risk-averse 
investor.
 ■ Quadratic utility function: 
( ) = a
bx
 
– --x 2 , U′( ) = b
cx
 
, U″( ) = –c < 0
U x
+ 
c
x
– 
x
2 
The quadratic utility function is concave; it represents a risk-averse 
investor. 
In a probabilistic setting, the utility function is a monotone function 
of a random variable and is, therefore, a random variable itself. To opti-
mize, one single utility number must be defined for each portfolio 
choice. Utility is therefore defined as the expected value of stochastic 
utility: 

490 
The Mathematics of Financial Modeling and Investment Management 
+∞ 
[ ( )] = 
( )U x
U = E U x
∫p x
( )dx
–∞ 
From this definition, it is clear why concavity represents risk aver-
sion. To see this point, it is useful to imagine a discrete world where 
only a discrete set of states is possible. In a discrete setting, utility is 
defined as a discrete, finite or infinite sum: 
U = E U x
(
)U x
[ ( )] = ∑p x
(
)
i
i
To each state corresponds a discrete finite probability. A risk-neutral 
investor does not require any compensation for risk-taking: the investor is 
indifferent to choices where the increment in the variable is inversely pro-
portional to the decrease in probability. For instance, a risk-neutral investor 
will be indifferent to choices where the halving of probability is compen-
sated with the doubling of consumption. However, a risk-averse investor 
will require more than a simple proportionality: a halving of probability 
must be compensated with more than a doubling of consumption. 
Optimizers 
An optimizer is a software program that searches the maximum of a 
(multivariate) function. If we know both the analytical expression of the 
function to be optimized and the constraints to be applied, the method 
of Lagrange multiplier yields closed-form solutions. However, if no ana-
lytical expression is available or if the function is too complex, numeri-
cal optimization techniques must be used. Numerical optimizers work 
by searching a space of likely maxima or minima. 
Mathematical optimization is a well-established technology and, 
outside of finance, is also used in many areas of science and technology. 
Different optimization technologies are employed, depending on the 
functions to be optimized and the constraints to be imposed. Statistical 
optimization technologies such as simulated annealing and genetic algo-
rithms have been employed to allow the optimization of generic func-
tions with multiple local minima and/or maxima. Chapter 7 provides a 
brief introduction to optimization technology. 
A Global Probabilistic Framework for Portfolio Selection 
We are now ready to state the global principles of portfolio selection. 
Portfolio selection works by finding those portfolio weights that maxi-
mize expected portfolio utility. Formally, we will have a joint probabil-

491 
Portfolio Selection Using Mean-Variance Analysis 
ity distribution of returns p(x) defined over the vector of returns r. For 
each vector of portfolio weights wa the portfolio return will be w ′r. The
a 
portfolio’s utility will be a stochastic variable U with a pdf that can be 
computed from the joint pdf of returns. For instance, if returns are 
jointly normal, the portfolio pdf will be normal. The portfolio selection 
problem is to maximize the expected value of this stochastic utility in 
function of portfolio weights: 
[
arg maxE U(r w )]
, 
a 
Portfolio optimization is a relatively mature technology, though its 
formal implementation is not yet widespread in the industry. The prob-
lem is one of sensitivity to forecasts. Practitioners who have imple-
mented the optimization technology typically report a great sensitivity 
of the optimization to forecast errors. Because the optimizer looks for 
the best opportunities within the pdf that has been fed to it, any mistake 
in the estimation of the pdf is magnified by the optimizer. This has led 
some in the industry to refer to optimization as “error maximization.”12 
RELAXING THE ASSUMPTION OF NORMALITY 
We can relax the assumption that returns are jointly normally distrib-
uted. It is a well known fact that returns are not normally distributed at 
short-time horizons of the order of days. As we saw in Chapter 13, fat-
tailed distributions were proposed to represent returns at such short 
time horizons. At the longer time horizons typical of portfolio manage-
ment, the assumption of normality is more plausible empirically speak-
ing. However, deviations from normality exist, either because of rare 
large price movements or because of the importance of moments of 
order higher than variance. 
The general utility maximization framework discussed above is very 
general and can be applied, in principle, to arbitrary distribution func-
tions provided that the maxima exist. Henrik Dahl, Alexander Meeraus, 
and Stavros Zenios13 argue that most financial engineering problems 
can be cast into an optimization framework. However practical statisti-
cal and computational problems arise when there is the need to estimate 
moments of high order in a multivariate environment. Extreme Value 
12 Muller, “Empirical Tests of Biases in Equity Portfolio Optimization.” 
13 Henrik Dahl, Alexander Meeraus, and Stavros Zenios, “Some Financial Optimi -
zation Models: I and II,” in Financial Optimization. 

492 
The Mathematics of Financial Modeling and Investment Management 
Theory (EVT) might help to determine the tails of some distributions. In 
this way, as we have seen in Chapter 13, it becomes possible to manage 
the risk associated with large movements. As observed by Jobst and 
Zenios14 the tails of the return distribution significantly affect portfolio 
performance. 
A new framework for portfolio selection with arbitrary distribu-
tions was proposed by Malevergne and Sornette.15 Their framework is 
based on transforming arbitrary variables into normal variables. The 
distribution of the transformed variables is then determined via the 
principle of entropy maximization.16 They showed that the new trans-
formed variables conserve the structure of correlation of the original 
variables as measured by copula functions. In this way they recovered 
the multivariate distribution of the original variables. 
MULTIPERIOD STOCHASTIC OPTIMIZATION 
The factor market models explored thus far are static linear regressions 
with an underlying dynamic that is either exogenously given or consists 
of the assumption of IID returns; these optimization models are myopic 
one-period optimization models. From the point of view of investor 
behavior, one-period models are based on the assumption that wealth is 
consumed at the end of the period. 
An investor must solve the problem of optimal portfolio selection. 
This means that at every trading moment the investor has to revise the 
selected portfolio and to decide what fraction of wealth is consumed 
and what fraction is reinvested. Suppose that an investor is character-
ized by a time-separable utility function defined over the consumption 
process. A time-separable utility function is such that the total utility is 
the sum of utility in different periods, each discounted by an appropri-
ate time-discount factor. It is implicitly assumed that the utility derived 
by the consumption of one unit at some future date is less than the util-
ity derived from the same consumption at the present date. 
Call Ct consumption at time t. The investor’s consumption of period t 
is a fraction of his or her wealth at the beginning of period t. The remaining 
14 Norbert J. Jobst and Stavros A. Zenios, “The Tail That Wags the Dog: Integrating 
Credit Risk in Asset Portfolios,” The Journal of Risk Finance (Fall 2001), pp. 31–44. 
15 Y. Malevergne and D. Sornette, “Higher-Moment Portfolio Theory with Multi-
variate Weibull Distributions,” unpublished paper. 
16 The Principle of Entropy Maximization chooses the distribution that has the max-
imum entropy among those compatible with a set of constraints. In general, con-
straints are given by the values of empirically determined moments. 

493 
Portfolio Selection Using Mean-Variance Analysis 
wealth is invested at a rate Rt. An infinite stream of consumption is possible 
if the return rate is positive. We will write utility in the following form: 
∞ 
C
(
Ut(
) = ∑diU Ct
i)
+ 
i = 0 
where C is a shorthand for a realization of the consumption process and 
d < 1 is the time discount factor of utility. In the following formulation 
we will consider an infinite horizon, i.e., consumption extends over an 
infinite stream at all future dates. It is also possible to consider only a 
finite number of steps ahead; in this case, one needs to write a utility 
function for final wealth in order to establish a trade-off between con-
sumption and final wealth. As in the previous single-period case, utility is 
a random variable as consumption is a stochastic process. We will there-
fore define utility as the expected value of stochastic utility as follows: 
∞ 
Ut = Et ∑diU Ct
i)
( 
+ 
i = 0 
The process dynamics are given by the following equation: 
= (1 + Rt)[Wt – Ct]
Wt + 1 
where Rt is the portfolio stochastic return. The investor’s portfolio 
selection consists of maximizing his expected utility given a return rate 
process for the portfolio and an initial endowment. The solution of this 
problem can be obtained through the methods of stochastic multistage 
optimization. The solution of the infinite horizon problem implies that 
first-order conditions, called Euler conditions, are satisfied for each 
asset. Euler conditions are the following: 
U′(
) = dEt[(1 + 
,
)U′(Ct + 1)]
Ct
Ri t  + 1 
where Ri,t is the period t return of the i-th asset. The left hand side of 
the equation is the utility the investor derives from consuming one unit 
less at time t while the right hand side is the additional expected utility 
that derives from consuming at time t + 1 the unit saved at time t and 
invested at rate Rt. Optimality implies that the two coincide. 
Ct
If we take the unconditional expectation and divide by U′(
) we 
can write the above equations in the following form: 

494 
The Mathematics of Financial Modeling and Investment Management 
1 = E[(1 + 
, )Mt ]
Ri t
where 
U′(Ct + 1) 
= d------------------------
Mt + 1 
U′(
)
Ct
is a random variable known as the stochastic discount factor. 
APPLICATION TO THE ASSET ALLOCATION DECISION17 
One of the most direct and widely used applications of MPT is asset 
allocation. Because the asset allocation decision is so important, almost 
all financial advisors determine an optimal portfolio for their clients— 
be they institutional or individual—by performing an asset allocation 
analysis using a set of asset classes.18 They begin by selecting a set of 
asset classes (e.g., domestic large cap and small cap stocks, long-term 
bonds, international stocks, etc.). To obtain estimates of the returns and 
volatilities and correlations they generally start with the historical per-
formance of the indexes representing these asset classes.19 Exhibit 16.6 
shows the major asset classes and an index commonly used to represent 
the performance characteristics of that asset class (i.e., mean and stan-
dard deviation of return). These estimates are used as inputs in the 
mean-variance optimization which results in an efficient frontier. Then 
using some criteria (for instance, using Monte Carlo simulations to 
compute the wealth distributions of the candidate portfolios), they pick 
an optimal portfolio allocation. Finally, this portfolio is implemented 
using either index or actively managed funds. 
17 This illustration draws from Frank J. Fabozzi, Francis Gupta, and Harry M. 
Markowitz, “Applying Mean-Variance,” Chapter 3 in Frank J. Fabozzi and Harry 
M. Markowitz (eds.), The Theory and Practice of Investment Management (Hobo-
ken, NJ: John Wiley & Sons, 2002). 
18 The following two studies conclude that asset allocation is a major determinant of 
portfolio performance: Gary L. Brinson, Randolph Hood, and Gilbert Beebower, 
“Determinants of Portfolio Performance,” Financial Analysts Journal (July/August 
1986), pp. 39–44 and Gary L. Brinson, Randolph Hood, and Gilbert Beebower, 
“Determinants of Portfolio Performance II: An Update,” Financial Analysts Journal 
(May/June 1991), pp. 40–48. 
19 Not all institutional asset managers use this method to obtain estimates of expect-
ed returns. 

Portfolio Selection Using Mean-Variance Analysis 
495 
EXHIBIT 16.6 
Asset Classes and Commonly Used Indexes 
Index 
Asset Class 
Inception Date 
U.S. 30 day T-bill 
U.S. Cash 
1/26 
Lehman Brothers aggregate bond 
U.S. Bonds 
1/76 
S&P 500 
U.S. Large Cap Equity 
1/26 
Russell 2000 
U.S. Small Cap Equity 
1/79 
MSCI EAFE 
Europe/Japan Equity 
1/70 
MSCI EM Free 
Emerging Markets Equity 
1/88 
Source: Exhibit 3.6 in Frank J. Fabozzi, Francis Gupta, and Harry M. Markow-
itz, “Applying Mean-Variance,” Chapter 3 in Frank J. Fabozzi and Harry M. 
Markowitz (eds.), The Theory and Practice of Investment Management (Hobo-
ken, NJ: John Wiley & Sons, 2002), p. 49. 
Once the funds are allocated to portfolio managers who specialize 
in the asset class, each portfolio manager selects the specific securities to 
be included in the portfolio. The portfolio can be actively managed or 
indexed. In fact, M-V analysis can be employed to construct the specific 
securities from within an asset class. 
The Inputs 
There are a number of approaches that can be used to obtain estimates 
of the inputs that are used in a mean-variance optimization, and all 
approaches have their pros and cons. Since the use of historical returns 
is the approach that is most commonly used, it may be useful to present 
a discussion on this method. 
As explained in Chapters 11 and 12, in the language of economet-
rics the above means that historical returns (i.e., the empirical average 
of past returns), are an estimate of the expected values of returns. This 
entails a model of returns, in particular a stationary model of returns. 
The assumption that returns are independent and identically distributed 
(IID) sequences20 is the simplest model where historical returns are an 
estimate of expected returns. 
Exhibit 16.7 uses monthly returns over different and varying time peri-
ods to present the annualized historical returns for four market indexes. 
One drawback of using the historical performance to obtain esti-
mates is clearly evident from this exhibit. Historical returns are not sta-
ble, the future does not repeat the past. This is one of the reasons 
20 See Chapter 6 for the definition of an IID sequence. 

496 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 16.7 
Annualized Returns Using Historical Performance Depend on the 
Time Period 
Period 
Lehman Aggregate 
S&P 500 
MSCI EAFE 
MSCI EM Free 
Five year
 1990–1995 
9.2% 
15.9% 
10.5% 
16.3%
 1996–2000 
6.3 
18.3 
8.2 
0.1 
Ten year
 1990–2000 
7.7 
17.1 
9.3 
8.2 
Note: Based on monthly returns of Ibbotson Associates. 
Source: Exhibit 3.3 in Frank J. Fabozzi, Francis Gupta, and Harry M. Markow -
itz, “Applying Mean-Variance,” Chapter 3 in Frank J. Fabozzi and Harry M. 
Markowitz (eds.), The Theory and Practice of Investment Management (Hobo -
ken, NJ: John Wiley & Sons, 2002), p. 46. 
econometricians have pushed to study dynamic return models, for 
instance Markov switching Hamilton models, that might capture fluctu-
ations such as those that appear in the exhibit.21 Note that, even using 
more complex models, fluctuations of the estimates will still exist. They 
are an ineliminable consequence of the global uncertainty in financial 
markets. The point is that the fluctuation of the estimates should not be 
too large to invalidate the model that is assumed. 
Based on historical performance, a portfolio manager looking for 
estimates of the expected returns for these four asset classes to use as 
inputs for obtaining the set of efficient portfolios at the end of 1995 might 
have used the estimates from the five-year period, 1990–1995. Then 
according to the portfolio manager’s expectations, over the next five 
years, only the U.S. equity market (as represented by the S&P 500) out-
performed, while U.S. bonds, Europe and Japan and Emerging Markets 
all underperformed. In particular, the performance of Emerging Markets 
was dramatically different from its expected performance (actual perfor-
mance of 0.1% versus an expected performance of 16.3%). This finding 
is disturbing, because if portfolio managers cannot have faith in the 
inputs that are used to solve for the efficient portfolios, then it is not pos-
sible for them to have much faith in the outputs (i.e., the makeup and 
expected performance of the efficient and optimal portfolios). 
Portfolio managers who were performing the exercise at the begin-
ning of 2001 faced a similar dilemma. Should they use the historical 
returns for the 1996–2000 period? That would generally imply that the 
21 For a discussion of these techniques, see Chapter 18. 

497 
Portfolio Selection Using Mean-Variance Analysis 
optimal allocation has a large holding of U.S. equity (since that was the 
asset class that performed well), and an underweighting to U.S. bonds 
and emerging markets equity. But then what if the actual performance 
over the next five years is more like the 1990–1995 period? In that case 
the optimal portfolio is not going to perform as well as a portfolio that 
had a good exposure to bonds and emerging markets equity. (Note that 
emerging markets equity outperformed U.S. equity under that scenario.) 
Or, should the portfolio managers use the estimates computed by using 
10 years of monthly performance? 
This is also true when trying to obtain estimates for the variances 
and correlations. Exhibit 16.8 presents the standard deviations for the 
same indexes over the same time periods. Though the risk estimates for 
the Lehman Aggregate and EAFE indexes are quite stable, the estimates 
for the S&P 500 and EM Free are significantly different over different 
time periods. However, the volatility of the indexes does shed some light 
on the problem of estimating expected returns as presented in Exhibit 
16.8. MSCI EM Free, the index with the largest volatility, also has the 
largest difference in the estimate of the expected return. Intuitively, this 
makes sense—the greater the volatility of an asset, the harder it is to 
predict its future performance. 
Exhibit 16.9 shows the five-year rolling correlation between the 
S&P 500 and MSCI EAFE. In January 1996, the correlation between the 
returns of the S&P 500 and EAFE was about 0.45 over the prior five 
years (1991–1995). Consequently, a portfolio manager would have 
expected the correlation over the next five years to be around that esti-
mate. However, for the five-year period ending December 2000, the cor-
EXHIBIT 16.8 
Annualized Standard Deviations Using Historical Performance 
Depend on the Time Period 
Period 
Lehman Aggregate 
S&P 500 
MSCI EAFE 
MSCI EME Free 
Five year
 1990–1995 
4.0% 
10.1% 
15.5% 
18.0%
 1996–2000 
4.8 
17.7 
15.6 
27.4 
Ten year
 1990–2000 
3.7 
13.4 
15.0 
22.3 
Note: Source of monthly returns is Ibbotson Associates. 
Source: Exhibit 3.4 in Frank J. Fabozzi, Francis Gupta, and Harry M. Markow -
itz, “Applying Mean-Variance,” Chapter 3 in Frank J. Fabozzi and Harry M. 
Markowitz (eds.), The Theory and Practice of Investment Management (Hobo -
ken, NJ: John Wiley & Sons, 2002), p. 47. 

498 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 16.9 
Correlation Between Returns of the S&P 500 and MSCI EAFE 
Indexes 
Source: Exhibit 3.5 in Frank J. Fabozzi, Francis Gupta, and Harry M. Markow-
itz, “Applying Mean-Variance,” Chapter 3 in Frank J. Fabozzi and Harry M. 
Markowitz (eds.), The Theory and Practice of Investment Management (Hobo-
ken, NJ: John Wiley & Sons, 2002), p. 48. 
relation between the assets slowly increased to 0.73. Historically, this 
was an all-time high. In January 2001, should the portfolio manager 
assume a correlation 0.45 or 0.73 between the S&P 500 and EAFE over 
the next five years? Or does 0.59, the correlation over the entire ten-
year period (1991–2000) sound more reasonable? 
In reality, if portfolio managers believe that the inputs based on the 
historical performance of an asset class are not a good reflection of the 
future expected performance of that asset class, they may objectively or 
subjectively alter the inputs. Different portfolio managers may have dif-
ferent beliefs, in which case the alterations will be different.22 The 
important thing here is that all alterations have theoretical justifica-
tions, which, in turn, ultimately leads to an optimal portfolio that 
closely aligns to the future expectations of the portfolio manager. 
22 It is quite common that the optimal strategic bond/equity mix within a portfolio 
differs significantly across portfolio managers. 

499 
Portfolio Selection Using Mean-Variance Analysis 
There are some purely objective arguments as to why we can place 
more faith in the estimates obtained from historical data for some assets 
over others. Exhibit 16.6 shows the inception dates for commonly used 
asset class indexes. Since there are varying lengths of histories available 
for different asset classes (for instance, U.S. and European markets not 
only have longer histories, but their data are also more accurate), inputs 
of some asset classes can generally be estimated more precisely than the 
estimates of others.23 
When solving for the efficient portfolios, the differences in precision 
of the estimates should be explicitly incorporated into the analysis. But 
MPT assumes that all estimates are as precise or imprecise, and there-
fore, treats all asset classes equally. Most commonly, practitioners of 
mean-variance optimization incorporate their beliefs on the precision of 
the estimates by imposing constraints on the maximum exposure of 
some asset classes in a portfolio. The asset classes on whom these con-
straints are imposed are generally those whose expected performances 
are either harder to estimate, or those whose performances are esti-
mated less precisely.24 
The extent to which we can use personal judgment to subjectively 
alter estimates obtained from historical data depends on our under-
standing what factors influence the returns on assets, and what is their 
impact. The political environment within and across countries, mone-
tary and fiscal policies, consumer confidence, and the business cycles of 
sectors and regions are some of the key factors that can assist in forming 
future expectations of the performance of asset classes. 
To summarize, it would be fair to say that using historical returns to 
estimate parameters that can be used as inputs to obtain the set of effi-
cient portfolios depends on whether the underlying economies giving 
rise to the observed outcomes of returns are strong and stable. Strength 
and stability of economies comes from political stability and consistency 
in economic policies. It is only after an economy has a lengthy and 
proven record of a healthy and consistent performance under varying 
(political and economic) forces that impact free markets, can historical 
performance of its markets be seen as a fair indicator of their future per-
formance. 
23 Statistically, the precision of an estimate is proportional to the amount of informa-
tion that is used to estimate it. That is, the more the data used to obtain an estimate, 
the greater the precision of the estimate. 
24 An alternate method for incorporating beliefs into M-V analysis is presented in 
Fisher Black and Robert Litterman, “Asset Allocation: Combining Investor Views 
With Market Equilibrium,” Journal of Fixed Income 1(1991), pp. 7–18. 

500 
The Mathematics of Financial Modeling and Investment Management 
Portfolio Selection: An Example 
Using an explicit example we now illustrate how asset managers and 
financial advisors use M-V analysis to build optimal portfolios for their 
clients and shed some light into the selection of an optimal portfolio. In 
this example we will construct an efficient frontier made up of U.S. 
bonds and U.S. and international equity. Exhibit 16.10 presents the for-
ward-looking assumptions for the four asset classes. 
These inputs are an example of estimates that are not totally based 
on historical performance of these asset classes. The expected return 
estimates are created using a risk premium approach (i.e., obtaining the 
historical risk premiums attached to bonds, large-cap, mid-cap, small-
cap, and international equity) and then have been subjectively altered to 
include the asset manager’s expectations regarding the future long-run 
(5 to 10 years) performance of these asset classes. The risk and correla-
tion figures are mainly historical. 
The next step is to use a software package to perform the optimization 
that results in the efficient frontier. For purposes of exposition, Exhibit 
16.11 presents the efficient frontier using only two of the four asset classes
from Exhibit 16.10—U.S. bonds and large cap equity. We highlight two 
efficient portfolios on the frontier: A and B corresponding to standard 
deviations of 9% and 12%, respectively. Portfolio B has the higher risk, 
but it also has the higher expected return. We suppose that one of these 
two portfolios is the optimal portfolio for a hypothetical client. 
Exhibit 16.12 presents the compositions of portfolios A and B, and 
some important characteristics that may assist in the selection of the 
optimal portfolio for the client. As one would expect, the more conser-
EXHIBIT 16.10 
Forward Looking Inputs (Expected Returns, Standard Deviations, 
and Correlations) 
Expected 
Std. Dev. 
Asset Class Return 
1 
2 
3 
4
Return 
of Return 
Correlations 
6.4%
 4.7% U.S. bonds 
1 1.00 
10.8 
14.9 
U.S. large cap equity 
2 0.32 1.00 
11.9 
19.6 
U.S. small cap equity 
3 0.06 0.76 1.00 
11.5 
17.2 
EAFE international equity 
4 0.17 0.44 0.38 1.00 
Source: Exhibit 3.7 in Frank J. Fabozzi, Francis Gupta, and Harry M. Markow-
itz, “Applying Mean-Variance,” Chapter 3 in Frank J. Fabozzi and Harry M. 
Markowitz (eds.), The Theory and Practice of Investment Management (Hobo-
ken, NJ: John Wiley & Sons, 2002), p. 51. 

501 
Portfolio Selection Using Mean-Variance Analysis 
EXHIBIT 16.11 
The Efficient Frontier Using Only U.S. Bonds and U.S. Large Cap 
Equity from Exhibit A 
Source: Exhibit 3.8 in Frank J. Fabozzi, Francis Gupta, and Harry M. Markow-
itz, “Applying Mean-Variance,” Chapter 3 in Frank J. Fabozzi and Harry M. 
Markowitz (eds.), The Theory and Practice of Investment Management (Hobo-
ken, NJ: John Wiley & Sons, 2002), p. 51. 
vative portfolio (A), allocates more to the conservative asset class, 
bonds. Portfolio A allocated a little more than 45% of the portfolio to 
bonds, while portfolio B only allocates 22% to that asset class. This 
results in significantly higher standard deviation for Portfolio B (12% 
versus 9%). In exchange for the 3% (or 300 basis points) of higher risk, 
portfolio B results in 104 basis points of higher expected return (9.83% 
versus 8.79%). This is the risk/return trade-off that the client faces. 
Does the increase in the expected return compensate the client for the 
increased risk? 
As mentioned earlier, another approach to selecting between the two 
efficient portfolios is to translate the differences in risk in terms of differ-
ences in the wealth distribution over time. The higher the risk, the wider 
the spread of the distribution. A wider spread implies a greater upside 
and a greater downside. Exhibit 16.12 also presents the 95th percentile, 
expected, and 5th percentiles for $100 invested in portfolios A and B over 

502 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 16.12 
Monte Carlo Wealth Distributions to the Risk/Return Trade-Off of 
Portfolios A and B: Growth of $100 
Characteristic 
Portfolio A 
Portfolio B 
U.S. bonds 
45.8% 
22.0% 
U.S. large cap equity 
54.2 
78.0 
Expected return
 8.79%
 9.83% 
Standard deviation
 9.00%
 12.00% 
Return per unit of risk 
98 bps 
82 bps 
1 
5 
10 
1 
5 
10 
Growth of $100 
Year 
Years 
Years 
Year 
Years 
Years 
95th percentile (upside) 
$124 
$203 
$345 
$131 
$232 
$424 
Average (expected)
 109
 152
 232
 110
 160
 255 
5th percentile (downside)
 95
 111
 146
 91
 104
 137 
Note: Assumes annual rebalancing. 
Source: Exhibit 3.9 in Frank J. Fabozzi, Francis Gupta, and Harry M. Markow -
itz, “Applying Mean-Variance,” Chapter 3 in Frank J. Fabozzi and Harry M. 
Markowitz (eds.), The Theory and Practice of Investment Management (Hobo -
ken, NJ: John Wiley & Sons, 2002), p. 52. 
1, 5, and 10 years, respectively.25 Over a one-year period, there is a 1 in 
20 chance that the $100 invested in portfolio A will grow to $124, but 
there is also a 1 in 20 chance that the portfolio will lose $5 (i.e., it will it 
shrink to $95). In comparison, for portfolio B there is a 1 in 20 chance 
that $100 will grow to $130 (the upside is $6 more than if invested in 
portfolio A). But there is also a 1 in 20 chance that the portfolio will 
shrink to $91 (the downside is $4 more than if invested in portfolio A). If 
the investment horizon is one year, is this investor willing to accept a 1 in 
20 chance of losing $9 instead of $4 for a 1 in 20 chance of gaining $31 
instead of $24?26 The answer depends on the investor’s risk aversion. 
As the investment horizon becomes longer, the chances that a port-
folio will lose its principal keep declining. Over 10 years, there is a 1 in 
25 The 95th percentile captures the upside associated with a 1 in 20 chance, while the 
5th percentile represents the downside associated with a 1 in 20 chance. 
26 It may be useful to mention here that more recently researchers in behavioral fi-
nance have found some evidence to suggest that investors view the upside and down-
side differently. In particular, they equate each downside dollar to more than one 
upside dollar. For a good review of the behavioral finance literature, see Hersh Shefrin 
(ed.), Behavioral Finance (Northampton, MA: Edward Elgar Publishing, Ltd., 2001). 

503 
Portfolio Selection Using Mean-Variance Analysis 
20 chance that portfolio A will grow to $345, but there is also a 1 in 20 
chance that the portfolio will only grow to $146 (the chances that the 
portfolio results in a balance less than $100 are much smaller). In com-
parison, over 10 years, there is a 1 in 20 chance that portfolio B will 
grow to $424 (the upside is $79 more than if invested in portfolio A)! 
And there is a 1 in 20 chance that the portfolio will only grow to 
$137—that is only $7 less than if invested in portfolio A! Also portfolio 
B’s average (expected) balance over 10 years is $23 more than portfolio 
A’s ($255 versus $232). Somehow, compounding makes the more risky 
portfolio seem more attractive over the longer run. In other words, a 
portfolio that may not be acceptable to the investor over a short run 
may be acceptable over a longer investment horizon. In summary, it is 
sufficient to say that the optimal portfolio depends not only on risk 
aversion, but also on the investment horizon. 
Inclusion of More Asset Classes 
Exhibit 16.13 compares the efficient frontier using two asset classes, 
namely, U.S. bonds and large cap equity with one obtained from using 
EXHIBIT 16.13 
Expanding the Efficient Frontier Using All Asset Classes 
Source: Exhibit 3.10 in Frank J. Fabozzi, Francis Gupta, and Harry M. Markowitz, 
“Applying Mean-Variance,” Chapter 3 in Frank J. Fabozzi and Harry M. Markow-
itz (eds.), The Theory and Practice of Investment Management (Hoboken, NJ: John 
Wiley & Sons, 2002), p. 54. 

504 
The Mathematics of Financial Modeling and Investment Management 
all four asset classes in the optimization. The inclusion of U.S. small cap 
and EAFE international equity into the mix makes the opportunity set 
bigger (i.e., the frontier covers a larger risk/return spectrum). It also 
moves the efficient frontier outwards (i.e., the frontier results in a larger 
expected return at any given level of risk, or conversely, results in a 
lower risk for any given level of expected return). The frontier also 
highlights portfolios A′ and B′—the portfolios with the same standard 
deviation as portfolios A and B, respectively. 
Exhibit 16.14 shows the composition of the underlying portfolios 
that make up the frontier. Interestingly, U.S. small cap and EAFE inter-
national equity—the more aggressive asset classes—are included in all 
the portfolios. Even, the least risky portfolio has a small allocation to 
these two asset classes. On the other hand, U.S. large cap equity—an 
asset class that is thought of as the backbone of a domestic portfolio— 
gets excluded from the more aggressive portfolios. 
Exhibit 16.15 compares the composition of portfolios A and B to A′ 
and B′, respectively. Both the new portfolios, A′ and B′, find U.S. small 
EXHIBIT 16.14 
Composition of the Efficient Frontier 
Source: Exhibit 3.11 in Frank J. Fabozzi, Francis Gupta, and Harry M. Markow-
itz, “Applying Mean-Variance,” Chapter 3 in Frank J. Fabozzi and Harry M. 
Markowitz (eds.), The Theory and Practice of Investment Management (Hobo-
ken, NJ: John Wiley & Sons, 2002), p. 55. 

505 
Portfolio Selection Using Mean-Variance Analysis 
EXHIBIT 16.15 
Composition of Equally Risky Efficient Portfolios in the Expanded 
Frontier 
Standard Deviation 
Standard Deviation 
= 9.0% 
= 12.0% 
Asset Class 
A 
A′ 
B 
B′ 
U.S. bonds 
34.3% 
40.4% 
22.0% 
15.1% 
U.S. large cap equity 
18.7 
15.8 
78.0 
27.8 
U.S. small cap equity 
— 
16.1 
— 
18.6 
EAFE international equity 
— 
27.7 
— 
38.5 
Expected return 
8.79% 
9.39% 
9.83% 
10.61% 
Standard deviation 
9.00% 
9.00% 
12.00% 
12.00% 
Return per unit of risk 
98 bps 
104 bps 
82 bps 
88 bps 
Source: Exhibit 3.12 in Frank J. Fabozzi, Francis Gupta, and Harry M. Markow-
itz, “Applying Mean-Variance,” Chapter 3 in Frank J. Fabozzi and Harry M. 
Markowitz (eds.), The Theory and Practice of Investment Management (Hobo-
ken, NJ: John Wiley & Sons, 2002), p. 55. 
cap and EAFE international equity very attractive and replace a signifi-
cant proportion of U.S. large cap equity with those asset classes. In 
portfolio B′ the more aggressive mix, the allocation to U.S. bonds also 
declines (15.1% versus 22%). 
Inclusion of U.S. small cap and EAFE international equity results in 
the sizable increases in the expected return and return per unit of risk. 
In particular, the conservative portfolio A′ has an expected return of 
9.39% (60 basis points over portfolio A) and the aggressive portfolio B′ 
has an expected return of 10.61% (78 basis points over portfolio B). 
Note also that there is an increase in the returns per unit of risk. 
The huge allocations to U.S. small cap and EAFE international 
equity in portfolios A′ and B′ may be uncomfortable for some investors. 
U.S. small cap equity is the most risky asset class and EAFE interna-
tional equity is the second most aggressive asset class. The conservative 
portfolio allocates more than 40% of the portfolio to these two asset 
classes, while the aggressive allocates more than 50%. As discussed in 
the section on using inputs based on historical returns, these two would 
also be the asset classes whose expected returns would be harder to esti-
mate. Consequently, investors may not want to allocate more than a cer-
tain amount to these two asset classes. 
On a separate note, investors in the U.S. may also want to limit 
their exposure to EAFE international equity. This may be simply 
because of psychological reasons. Familiarity leads them to believe that 

506 
The Mathematics of Financial Modeling and Investment Management 
domestic asset classes are “less” risky.27 Exhibit 16.16 presents the com-
position of the efficient frontier when the maximum allocation to EAFE 
is constrained at 10% of the portfolio. As a result of this constraint, all 
the portfolios now receive an allocation of U.S. large cap equity. 
Exhibit 16.17 compares the composition portfolios A′ and B′ to port-
folios A″ and B″ the respective equally risky portfolios that lie on the con-
strained efficient frontier. In the conservative portfolio A″, the combined 
allocation to U.S. small cap and EAFE international equity has declined to 
30% (from 43.8%) and in B″ it has fallen to 34.8% (from 57.1%). Also 
now the bond allocation increases for both the portfolios. 
The decline in the expected return can be used to quantify the cost 
of this constraint. The conservative portfolio’s expected return fell from 
9.39% to 9.20%—a decline of 19 basis points. This cost may be well 
EXHIBIT 16.16 
Composition of the Constrained Efficient Frontier 
Maximum Allocation to EAFE International Equity = 10% 
Source: Exhibit 3.13 in Frank J. Fabozzi, Francis Gupta, and Harry M. Markow-
itz, “Applying Mean-Variance,” Chapter 3 in Frank J. Fabozzi and Harry M. 
Markowitz (eds.), The Theory and Practice of Investment Management (Hobo-
ken, NJ: John Wiley & Sons, 2002), p. 57. 
27 Similarly, investors in Europe may believe that EAFE equity is “less” risky than 
U.S. equity and may want to limit their exposure to U.S. asset classes.

507 
Portfolio Selection Using Mean-Variance Analysis 
EXHIBIT 16.17 
The Benefits and Costs of Constraining an Efficient Frontier 
Maximum Allocation to 
EAFE International 
Unconstrained 
Equity = 10.0% 
Asset Class 
A′ 
B′ 
A′′ 
B′′ 
U.S. bonds 
40.4% 
15.1% 
43.1% 
20.1% 
U.S. large cap equity 
15.8 
27.8 
26.9 
45.1 
U.S. small cap equity 
16.1 
18.6 
20.0 
24.8 
EAFE international equity 
27.7 
38.5 
10.0 
10.0 
Expected return
 9.39%
 10.61%
 9.20%
 10.26% 
Standard deviation
 9.00%
 12.00%
 9.00%
 12.00% 
Cost of constraint 
— 
— 
19 bps 
35 bps 
Note: Assumes annual rebalancing. 
Source: Exhibit 3.14 in Frank J. Fabozzi, Francis Gupta, and Harry M. Markow -
itz, “Applying Mean-Variance,” Chapter 3 in Frank J. Fabozzi and Harry M. 
Markowitz (eds.), The Theory and Practice of Investment Management (Hobo -
ken, NJ: John Wiley & Sons, 2002), p. 57. 
worth it for an investor whose optimal appetite for risk is 9%. The 
more aggressive portfolio pays more for the constraint (10.61% – 
10.26% = 35 basis points).28 
EXTENSIONS OF THE BASIC ASSET ALLOCATION MODEL 
In mean-variance analysis, the variance (standard deviation) of returns 
is the proxy measure for portfolio risk. As a supplement, the probability 
of not achieving a portfolio expected return can be calculated. This type 
of analysis, referred to as risk-of-loss analysis, would be useful in deter-
mining the most appropriate mix from the set of optimal portfolio allo-
cations.29 In the context of setting investment strategy for a pension 
fund that has a long-term normal asset allocation policy established, the 
28 For a discussion on the benefits and costs of constraints, see Francis Gupta and 
David Eichhorn, “Mean-Variance Optimization for Practitioners of Asset Alloca-
tion,” in Frank J. Fabozzi (ed.), Handbook of Portfolio Management (New York: 
John Wiley & Sons, 1998), pp. 57–74. 
29 Risk of loss analysis as well as the multiple scenario analysis and short-term/long-
term analysis described next, were developed by Gifford Fong Associates in the early 
1980s. See Chapter 4 and Appendix B in H. Gifford Fong and Frank J. Fabozzi, 
Fixed Income Portfolio Management (Homewood, IL: Dow-Jones-Irwin, 1985). 

508 
The Mathematics of Financial Modeling and Investment Management 
value of the probability of loss for the desired return benchmark over 
the long-term horizon can be used as the maximum value for the short 
term. For example, if the long-term policy has a 15% probability of loss 
for 0% return, the mix may be changed over the short run, as long as 
the probability of loss of the new mix has a maximum of 15%. There-
fore, by taking advantage of short-term expectations to maximize 
return, the integrity of the long-term policy is retained. A floor or base 
probability of loss is therefore established that can provide boundaries 
within which strategic return/risk decisions may be made. As long as the 
alteration of the asset allocation mix does not violate the probability of 
loss, increased return through strategies such as tactical asset allocation 
can be pursued. 
Mean-variance analysis has been extended to multiple possible sce-
narios. Each assumed scenario is believed to be an assessment of the 
asset performance in the long run, over the investment horizon. A prob-
ability can be assigned to each scenario so that an efficient set can be 
constructed for the composite scenario. It is often the case, however, 
that an investor expects a very different set of input values in mean-vari-
ance analysis that are applicable in the short run, say, the next 12 
months. For example, the long-term expected return on equities may be 
estimated at 15% but over the next year the expected return on equities 
may be only 5%. The investment objectives are still stated in terms of 
the portfolio performance over the entire investment horizon. However, 
the return characteristics of each asset class are described by one set of 
values over a short period and another set of values over the balance of 
the investment horizon. A mean-variance analysis can be formulated 
that simultaneously optimizes over the two periods.30 
Finally, mean-variance analysis has been extended to explicitly 
incorporate the liabilities of pension funds.31 This extension requires 
not only the return distribution of asset classes that must be considered 
in an optimization model, but also the liabilities. 
30 See Harry M. Markowitz and André F. Perold, “Portfolio Analysis with Factors 
and Scenarios,” Journal of Finance (September 1981), pp. 871–877. 
31 See Martin L. Leibowitz, Stanley Kogelman, and Lawrence N. Bader, “Asset Per-
formance and Surplus Control—A Dual-Shortfall Approach,” in Robert D. Arnott 
and Frank J. Fabozzi (eds.), Active Asset Allocation (Chicago: Probus Publishing, 
1992). The mean-variance model they present strikes a balance between asset perfor-
mance and the maintenance of acceptable levels of its downside risk, and surplus per-
formance and the maintenance of acceptable levels of its downside risk. 

509 
Portfolio Selection Using Mean-Variance Analysis 
SUMMARY 
 ■ The principles of financial optimization were established by Markowitz 
in 1952.
 ■ The key idea of Markowitz is that financial decision-making should be 
based on an optimal trade-off between risk and returns. 
■ Markowitz’s seminal work proposed optimizing a trade-off between 
variance and the expected returns of a portfolio under the assumption 
of joint normality of returns.
 ■ The key principle behind mean-variance optimization is diversification.
 ■ Markowitz’s work had a lasting influence on the investment manage-
ment community; investment management principles are still deeply 
influenced by these ideas.
 ■ Portfolios that achieve the minimum variance for a given expected 
return are called minimum-variance portfolios.
 ■ Minimum-variance portfolios are called mean-variance efficient portfo-
lios; the set of mean-variance efficient portfolios form the efficient fron-
tier.
 ■ The theoretical problem of finding mean-variance efficient portfolios 
leads to an optimization problem solvable in closed form with the tech-
nique of Lagrange multipliers.
 ■ Sharpe, Tobin, and Lintner extended the portfolio selection model in 
the presence of a risk-free asset; the mean-variance portfolios are those 
that are a combination of the tangency portfolio and the risk-free asset.
 ■ In the presence of a risk-free asset the efficient frontier becomes the 
Capital Market Line which is the straight line tangent to the Market 
Portfolio.
 ■ If realistic constraints are added, namely sector exposure and tradabil-
ity constraints, the problem becomes one of quadratic programming or 
a mixed-integer programming to be solved with numerical techniques.
 ■ Markowitz’s mean-variance formulation can be used for portfolio 
selection as well as asset allocation.
 ■ Risk-of-loss-analysis is an extension of the basic model. It considers the 
risk of not achieving a portfolio’s expected return.
 ■ The basic mean-variance analysis can also be extended to cover the lia-
bilities of pension funds.
 ■ The theory of Markowitz can be extended in a one-period setting as 
maximization of expected utility.
 ■ In a multiperiod setting agents maximize utility defined on consump-
tion.
 ■ In a multiperiod setting agents determine at each step the optimal 
trade-off between investment and consumption. 


CHAPTER 17 
Capital Asset 
Pricing Model 
T
he mean-variance approach to portfolio selection and its generaliza-
tions require a model for variance and expected returns to feed to the 
optimizer. Asset price and/or return models belong to three different 
families:
 ■ General Equilibrium Theories. These determine price processes as the 
equilibrium between demand and supply of markets populated by eco-
nomic agents whose behavior is known. General equilibrium theories 
are therefore truly economic theories based on specific assumptions on 
the behavior of agents. The following models are general equilibrium 
models: CAPM, Conditional CAPM, multifactor CAPM, and Con-
sumption CAPM.
 ■ Arbitrage Pricing Models. Arbitrage pricing is relative pricing inso-
far as the prices and therefore the returns of a set of assets depend 
on another set of processes. Arbitrage pricing was discussed in 
Chapters 14 and 15.
 ■ Econometric Models. These are statistical models of prices or returns. 
They model prices or returns as endogenous phenomena and/or 
establish links between prices and returns and exogenous variables. 
The justification of econometric models is empirical, that is, they are 
valid insofar as they fit empirical data. They are not derived from eco-
nomic theory although economic theory might suggest econometric 
models. For example, Markov switching models are rooted in the the-
ory of economic cycles. 
511 

512 
The Mathematics of Financial Modeling and Investment Management 
The subject of this chapter is the Capital Asset Pricing Model 
(CAPM) formulated by William Sharpe, John Lintner, and Jan Mossin.1 
As explained in the previous chapter, portfolio selection based on mean-
variance analysis is a normative theory that describes the investment 
behavior of market agents in constructing a portfolio. Given this invest-
ment behavior, the capital asset pricing model formalizes the relation-
ship that should exist between asset returns and risk. 
CAPM ASSUMPTIONS 
The CAPM is an equilibrium asset pricing model derived from a set of 
assumptions. Here we demonstrate how the CAPM is derived. 
The CAPM is an abstraction of the real world capital markets and, 
as such, is based upon some assumptions. These assumptions simplify 
matters a great deal, and some of them may even seem unrealistic. How-
ever, these assumptions make the CAPM more tractable from a mathe-
matical standpoint. The CAPM assumptions are as follows:
 ■ Assumption 1. Investors make investment decisions based on the 
expected return and variance of returns.
 ■ Assumption 2. Investors are rational and risk averse.
 ■ Assumption 3. Investors subscribe to the Markowitz method of 
portfolio diversification.
 ■ Assumption 4. Investors all invest for the same period of time.
 ■ Assumption 5. Investors have the same expectations about the 
expected return and variance of all assets.
 ■ Assumption 6. There is a risk-free asset and investors can borrow 
and lend any amount at the risk-free rate.
 ■ Assumption 7. Capital markets are completely competitive and fric-
tionless. 
The first five assumptions deal with the way investors make deci-
sions. The last two assumptions relate to characteristics of the capital 
market. Some of these assumptions require further explanation. As 
explained in Chapter 16, in mean-variance analysis, it is assumed that 
1 William F. Sharpe, “Capital Asset Prices,” Journal of Finance (September 1964), 
pp. 425–442. Others who reached a similar conclusion regarding the pricing of risk 
assets include: John Lintner, “The Valuation of Risk Assets and the Selection of 
Risky Investments in Stock Portfolio and Capital Budgets,” Review of Economics 
and Statistics (February 1965), pp. 13–37 and Jan Mossin, “Equilibrium in a Capital 
Asset Market,” Econometrica (October 1966), pp. 768–783. 

513 
Capital Asset Pricing Model 
investors make investment decisions based on two parameters, the 
expected return and the variance of returns. Assumption 1 indicates that 
in the CAPM the same two parameters are used by investors. Assump-
tion 2 indicates that in order to accept greater risk, investors must be 
compensated by the opportunity of realizing a higher return. 
The CAPM assumes (Assumption 3) that the risk-averse investor 
will ascribe to Markowitz’s methodology of reducing portfolio risk by 
combining assets with counterbalancing covariances or correlations. By 
Assumption 4, all investors are assumed to make investment decisions 
over some single-period investment horizon. How long that period is 
(i.e., six months, one year, two years, etc.) is not specified. In reality, the 
investment decision process is more complex than that, with many 
investors having more than one investment horizon. Nonetheless, the 
assumption of a one-period investment horizon is necessary to simplify 
the mathematics of the theory. 
To obtain the Markowitz efficient frontier which we will be used in 
developing the CAPM, it will be assumed that investors have the same 
expectations with respect to the inputs that are used to derive the efficient 
portfolios: asset returns, variances, and covariances. This is Assumption 5 
and is referred to as the “homogeneous expectations assumption.” 
It is assumed that there is a risk-free asset. An investor in this asset 
earns a risk-free rate. Moreover,  it is assumed that investors cannot 
only earn a risk-free rate, but if they want to borrow, they can do so at 
the risk-free rate (Assumption 6). 
Finally, it is assumed that the capital market is perfectly competitive 
(Assumption 7). In general, this means the number of buyers and sellers 
is sufficiently large, and all investors are small enough relative to the 
market so that no individual investor can influence an asset’s price. Con-
sequently, all investors are price takers, and the market price is deter-
mined where there is equality of supply and demand. In addition, 
according to Assumption 7, there are no transaction costs or impedi-
ments that interfere with the supply of and demand for an asset. 
SYSTEMATIC AND NONSYSTEMATIC RISK 
A risk-averse investor who makes decisions based on expected return and 
variance should construct an efficient portfolio using a combination of the 
market portfolio and the risk-free rate. The combinations are identified by 
the CML. Based on this result, Sharpe derived an asset pricing model that 
shows how a risky asset should be priced. In the process of doing so, we 
can fine-tune our thinking about the risk associated with an asset. Specifi-

514 
The Mathematics of Financial Modeling and Investment Management 
cally, we can show that the appropriate risk that investors should be com-
pensated for accepting is not the variance of an asset’s return but some 
other quantity. In order to do this, let’s take a closer look at risk. 
We can do this by looking at the variance of the portfolio. 
The proof is as follows. The variance of a portfolio consisting of N 
assets is equal to 
N
N 
var(Rp) = ∑∑ wiwjcov(Ri, Rj) 
i = 1 j = 1 
If we substitute M (market portfolio) for p and denote by wiM and wjM, 
the proportion invested in asset i and j in the market portfolio, then the 
above equation can be rewritten as 
N
N 
var(RM) = ∑∑ wiMwjMcov(Ri, Rj) 
i = 1 j = 1 
It can be demonstrated that the above equation can be expressed as follows: 
var(RM) 
N
N 
= w1M ∑ wjMcov(R1, Rj) + w2M ∑ wjMcov(R2, R )
j 
j = 1 
j = 1 
N 
+ … + wNM ∑ wNMcov(RN, Rj) 
j = 1 
The covariance of asset i with the market portfolio, cov(Ri, RM), is 
expressed as follows: 
N 
cov(Ri, RM) = ∑ wjMcov(Rj, Rj) 
j = 1 
Substituting the right-hand side of the left-hand side of the equation 
into the prior equation, gives 
var(RM) 
= w1M cov(R1, RM) + w2M cov(R2, RM) + . . . + wNM cov(RN, RM) 

515 
Capital Asset Pricing Model 
Notice that the portfolio variance does not depend on the variance of 
the assets comprising the market portfolio but on their covariance with 
the market portfolio. Sharpe defines the degree to which an asset cova-
ries with the market portfolio as the asset’s systematic risk. More specif-
ically, he defined systematic risk as the portion of an asset’s variability 
that can be attributed to a common factor. Systematic risk is the mini-
mum level of risk that can be obtained for a portfolio by means of diver-
sification across a large number of randomly chosen assets. 
As such, systematic risk is that which results from general market 
and economic conditions that cannot be diversified away. Sharpe 
defined the portion of an asset’s variability that can be diversified away 
as nonsystematic risk. It is also sometimes called unsystematic risk, 
diversifiable risk, unique risk, residual risk, and company-specific risk. 
This is the risk that is unique to an asset. 
Consequently, total risk (as measured by the variance) can be parti-
tioned into systematic risk as measured by the covariance of asset i’s 
return with the market portfolio’s return and nonsystematic risk. The 
relevant risk is the systematic risk. We will see how to measure the sys-
tematic risk later. How diversification reduces nonsystematic risk for 
portfolios is illustrated in Exhibit 17.1. The vertical axis shows the vari-
ance of the portfolio return. The variance of the portfolio return repre-
sents the total risk for the portfolio (systematic plus nonsystematic). 
EXHIBIT 17.1 
Systematic and Unsystematic Portfolio Risk 

516 
The Mathematics of Financial Modeling and Investment Management 
The horizontal axis shows the number of holdings of different assets 
(e.g., the number of common stock held of different issuers). 
As can be seen, as the number of asset holdings increases, the level 
of nonsystematic risk is almost completely eliminated (i.e., diversified 
away). Studies of different asset classes support this. For example, for 
common stock, several studies suggest that a portfolio size of about 20 
randomly selected companies will completely eliminate nonsystematic 
risk leaving only systematic risk.2 
SECURITY MARKET LINE 
The CML represents an equilibrium condition in which the expected 
return on a portfolio of assets is a linear function of the expected return 
on the market portfolio. Individual assets do not fall on the CML. 
Instead, it can be demonstrated that the following relationship holds for 
individual assets:3 
E Ri
(
) – Rf
E Ri
(
) = Rf + -------------------------- cov(Ri, RM ) 
var(RM ) 
The above equation is called the security market line (SML). 
In equilibrium, the expected return of individual securities will lie 
on the SML and not on the CML. This is true because of the high degree 
of nonsystematic risk that remains in individual assets that can be diver-
sified out of portfolios. In equilibrium, only efficient portfolios will lie 
on both the CML and the SML. 
The SML also can be expressed as 
cov(Ri, RM )
(
) = Rf + [E Ri
E Ri
(
) – Rf]-------------------------------
var(RM ) 
The ratio cov(Ri, RM ) ⁄ var(RM) can be estimated empirically using 
return data for the market portfolio and the return on the asset. The 
2 The first empirical study of this type was by Wayne H. Wagner and Sheila Lau, 
“The Effect of Diversification on Risks,” Financial Analysts Journal (November–De- 
cember 1971), p. 50. 
3 For the proof, see William F. Sharpe, Portfolio Theory and Capital Markets (New 
York, NY: McGraw Hill, 1970), pp. 86–91. 

517 
Capital Asset Pricing Model 
empirical analogue for the above equation is the following linear regres-
sion, called the characteristic line: 
rit − rft = αi + βi [rMt − rft] + eit 
where eit is the error term. 
The beta term βi in the above regression is the estimate of the ratio 
in the SML equation that is 
cov(Ri, RM)
βi = -------------------------------
var(RM) 
Substituting βi into the SML equation gives the beta-version of the 
SML: 
E(Ri) = Rf + βi [E(RM) − Rf] 
This is the CAPM. It states that, given the assumptions of the 
CAPM, the expected return on an individual asset is a positive linear 
function of its index of systematic risk as measured by beta. The higher 
the beta is, the higher the expected return. 
An investor pursuing an active strategy will search for underpriced 
securities to purchase and overpriced securities to avoid (sell if held in 
the current portfolio, or sold short if permitted). If an investor believes 
that the CAPM is the correct asset pricing model, then the SML can be 
used to identify mispriced securities. A security where the market prices 
it such that the expected return is less than the expected return as pre-
dicted by the SML is an undervalued security. In contrast, an overvalued 
security is one where the market prices the security such that its 
expected return is greater than that predicted by the SML. 
In equilibrium, the expected return of individual securities will lie 
on the SML and not on the CML. This is true because of the high degree 
of unsystematic risk that remains in individual securities that can be 
diversified out of portfolios of securities. It follows that the only risk 
investors will pay a premium to avoid is market risk. Hence, two assets 
with the same amount of systematic risk will have the same expected 
return. In equilibrium, only efficient portfolios will lie on both the CML 
and the SML. This underscores the fact that the systematic risk measure, 
beta, is most correctly considered as an index of the contribution of an 
individual security to the systematic risk of a well-diversified portfolio 
of securities. 

518 
The Mathematics of Financial Modeling and Investment Management 
Estimating the Characteristic Line 
The characteristic line is estimated using regression analysis. In fact, all 
the data required are the same except for the risk-free rate each period. 
The coefficient of determination, denoted by R-squared, indicates the 
strength of the relationship. Specifically, it measures the percentage of 
the variation in the return on a stock explained by the return by the 
market portfolio (proxied by the S&P 500 in our illustration). The value 
ranges from 0 to 1. The higher the R-squared, the greater the propor-
tion of systematic risk relative to total risk. For individual stocks, the R-
squared is typically in the 0.3 area. That is, for individual stocks system-
atic risk is small relative to nonsystematic risk. For well-diversified port-
folio, the R-squared is typically greater than 0.9. 
TESTING THE CAPM 
Testing the CAPM has been a major endeavor of financial econometrics. 
The number of articles found under the general heading “tests of the 
CAPM” is impressive. One bibliographic compilation lists almost 1,000 
papers on the topic. Consequently, only the basic results are given here. 
In general, a methodology referred to as “two-pass regression” is 
used to test the CAPM. The first pass involves the estimation of beta for 
each security by means of a time series regression described by charac-
teristic line. The betas from the first-pass regression are then used to 
form portfolios of securities ranked by portfolio beta. The portfolio 
returns, the return on the risk-free asset, and the portfolio betas are then 
used to estimate the second-pass, cross-sectional regression: 
R  – RF = bo + b1βp + e
p
p 
where the parameters to be estimated are bo and b1, and ep is the error 
term for the regression. The return data are frequently aggregated into 
five-year periods for this regression. 
Deriving the Empirical Analogue of the CML 
The above equation is the empirical analogue of a beta version of the 
CML. To see this, subtract RF from both sides of the CML equation 
(
[E RM) – Rf]
E Ri
[
] = Rf + ----------------------------------cov(RiR ) 
var(RM) 
m 
which can then can be rewritten as 

519 
Capital Asset Pricing Model 
(
[E RM ) – Rf ]
E Ri
[
] – Rf = ----------------------------------cov(RiR ) 
var(RM ) 
m 
The above is the CML in “risk-premium form” because the value on 
the left-hand side of the equation is the portfolio’s expected return over 
the risk-free rate. By adding an error term and a constant term, bo, the 
above equation becomes 
E(Rp) – RF = bo + βp [E(RM) – RF] + ep 
The actual process of testing the CAPM using the two-pass regression 
methodology involves the consideration of some econometric problems 
(e.g., measurement error, correlated error terms, and beta instability).4 
Empricial Implications 
Assuming that the capital market can be described as one in which there 
is no opportunity for investors to use information from previous periods 
to earn abnormal returns, several testable hypotheses for the empirical 
analogue of the CML implied by the CAPM can be listed: 
1. The relationship between beta and return should be linear. 
2. The intercept term, bo, should not differ significantly from zero. 
3. The coefficient for beta, b1, should equal the risk premium (RM – RF). 
4. Beta should be the only factor that is priced by the market. That is, 
other factors such as the variance or standard deviation of the returns, 
and variables that we will discuss in later chapters such as the price/ 
earnings ratio, ratio, dividend yield, and firm size should not add any 
significant explanatory power to the equation. 
5. Over long periods of time, the rate of return on the market portfolio 
should be greater than the return on the risk-free asset. This is because 
the market portfolio has more risk than the risk-free asset. Hence, risk-
averse investors would price it so as to generate a greater return. 
4 The interested reader should consult Merton H. Miller and Myron S. Scholes, 
“Rates of Return in Relation to Risk,” Chapter 2 in Michael C. Jensen (ed.), Studies 
in the Theory of Capital Markets (New York: Praeger, 1972), pp. 79–121; Eugene 
F. Fama, Foundations of Finance (New York: Basic Books, 1976); Richard Roll, 
“Performance Evaluation and Benchmark Errors II,” Journal of Portfolio Manage-
ment (Winter 1981), pp. 17–22; and Richard Roll, “A Critique of the Asset Pricing 
Theory’s Tests,” Journal of Financial Economics (March 1977), pp. 129–176 for a 
discussion of these issues. 

520 
The Mathematics of Financial Modeling and Investment Management 
General Findings of Empirical Tests of the CAPM 
The general results of the empirical tests of the CAPM are as follows: 
1. The relationship between beta and return appears to be linear, hence 
the functional form of the CAPM seems to be correct. 
2. The estimated intercept term,  bo, is significantly different from zero 
and consequently different from what is hypothesized for this value. 
3. The estimated coefficient for beta, b1, is less than RM – RF. The combi-
nation of results 2 and 3 suggests that low beta stocks have higher 
returns than the CAPM predicts and high beta stocks have lower 
returns than CAPM predicts. 
4. Beta is not the only factor priced by the market. Several studies have 
discovered other factors that explain stock returns. These include a 
price/earnings factor,5 a dividend factor,6 a firm size factor,7 and both a 
firm size factor and a book/market factor.8 
5. Over long periods of time (usually 20–30 years), the return on the mar-
ket portfolio is greater than the risk-free rate. 
A Critique of Tests of the CAPM 
One of the most controversial papers written on the CAPM is Richard 
Roll’s “A Critique of the Asset Pricing Theory’s Tests.”9 We will discuss 
the major points of Roll’s argument here. Following Roll’s argument, 
the CAPM is a general equilibrium model based upon the existence of a 
market portfolio that is defined as the value-weighted portfolio of all 
investment assets. Furthermore, the market portfolio is defined to be ex 
ante mean-variance efficient. This means that the market portfolio lies 
on the ex ante Markowitz efficient frontier for all investors. 
Roll demonstrates that the only true test of the CAPM is whether the 
market portfolio is in fact ex ante mean-variance efficient. However, the 
5 See Sanjoy Basu, “Investment Performance of Common Stocks in Relation to Their 
Price-Earnings Ratios,” Journal of Finance (June 1977), pp. 663–682 and “The Re-
lationship Between Earnings’ Yield, Market Value and Return for NYSE Common 
Stocks,” Journal of Financial Economics (June 1983), pp. 129–156. 
6 Robert Litzenberger and Krishna Ramaswamy, “The Effect of Personal Taxes and 
Dividends on Capital Asset Prices,” Journal of Financial Economics (June 1979), pp. 
163–195. 
7 Rolf Banz, “The Relationship Between Return and Market Value of Common 
Stocks,” Journal of Financial Economics (March 1981). pp. 3–18. 
8 Eugene Fama and Kenneth French, “The Cross-Section of Expected Returns,” Jour-
nal of Finance (June 1992), pp. 427–465. 
9 Richard Roll, “A Critique of the Asset Pricing Theory’s Tests.” 

521 
Capital Asset Pricing Model 
true market portfolio is, in fact, ex ante since it includes all investment 
assets (e.g., stocks, bonds, real estate, art objects, and human capital). 
The consequences of this “nonobservability” of the true market 
portfolio are: 
1. Tests of the CAPM are extremely sensitive to which market proxy is 
used, even though returns on most market proxies (e.g., the S&P 500 
and the NYSE index) are highly correlated. 
2. A researcher cannot unambiguously discern whether the CAPM failed 
a test because the true market portfolio was ex ante mean-variance 
inefficient, or because the market proxy was inefficient. Alternatively, 
the researcher cannot unambiguously discern whether a test supported 
the CAPM because the true market portfolio was ex ante mean-vari-
ance efficient or because the market proxy was efficient. 
3. The effectiveness of variables such as dividend yield in explaining risk-
adjusted asset returns is evidence that the market proxies used to test 
the CAPM are not ex ante mean-variance efficient. 
Hence, Roll submits that the CAPM is not testable until the exact 
composition of the true market portfolio is known, and the only valid 
test of the CAPM is to observe whether the ex ante true market portfo-
lio is mean-variance efficient. As a result of his findings, Roll states that 
he does not believe there ever will be an unambiguous test of the 
CAPM. He does not say that the CAPM is invalid. Rather, Roll says that 
there is likely to be no unambiguous way to test the CAPM and its 
implications due to the nonobservability of the true market portfolio 
and its characteristics. 
Does this mean that the CAPM is useless to the financial practitio-
ner? The answer is no, it does not. What it means is that the implica-
tions of the CAPM should be viewed with caution. 
Merton and Black Modifications of the CAPM 
Several researchers have modified the CAPM. Here we will briefly 
describe two modifications. 
Suppose that there is no risk-free rate and that investors cannot bor-
row and lend at the risk-free rate (Assumption 6). How does that affect 
the CAPM? Fischer Black examined how the original CAPM would 
change if there is no risk-free asset in which the investor can borrow 
and lend.10 He demonstrated that neither the existence of a risk-free 
asset nor the requirement that investors can borrow and lend at the risk-
10 Fischer Black, “Capital Market Equilibrium with Restricted Borrowing,” Journal 
of Business (July 1972), pp. 444–455. 

522 
The Mathematics of Financial Modeling and Investment Management 
free rate is necessary for the theory to hold. Black’s argument was as fol-
lows. The beta of a risk-free asset is zero. Suppose that a portfolio can 
be created such that it is uncorrelated with the market. That portfolio 
would then have a beta of zero, and Black labeled that portfolio a 
“zero-beta portfolio.” He set forth the conditions for constructing a 
zero-beta portfolio and then showed how the CAPM can be modified 
accordingly. Specifically, the return on the zero-beta portfolio is substi-
tuted for the risk-free rate. 
Now let’s look at the assumption that the only relevant risk is the 
variance of asset returns (Assumption 1). That is, it is assumed that the 
only risk factor that an investor is concerned with is the uncertainty 
about the future price of a security. Investors, however, usually are con-
cerned with other risks that will affect their ability to consume goods 
and services in the future. Three examples would be the risks associated 
with future labor income, the future relative prices of consumer goods, 
and future investment opportunities. Consequently, using the variance 
of expected returns as the sole measure of risk would be inappropriate 
in the presence of these other risk factors. Recognizing these other risks 
that investors face, Robert Merton modified the CAPM based on con-
sumers deriving their optimal lifetime consumption when they face such 
non-market risk factors.11 
CAPM and Random Matrices 
Let’s take a look at CAPM from a different angle. Under the assumption 
of IID returns, the CAPM is the statement that the entire market is 
driven by only one factor represented by the market portfolio. Plerou et 
al12 analyzed the distribution and stability of the eigenvalues of the vari-
ance-covariance matrix of large portfolios. Their conclusion can be 
summarized as follows:
 ■ The majority of the eigenvalues fall within the bounds of Random 
Matrix Theory (RMT). This means that the majority of eigenvalues do 
not carry genuine correlation information. This confirms results 
already described in the literature.13
 ■ A number of eigenvalues are definitely outside the RMT bounds. The 
eigenvector corresponding to the largest eigenvalue includes all assets, 
11 Robert C. Merton, “An Intertemporal Capital Asset Pricing Model,” Econometri-
ca (September 1973), pp. 867–888. 
12 Vasiliki Plerou, Parameswaran Gopikrishnan, Bernd Rosenow, Luis A. Nunes 
Amaral, Thomas Guhr, and H. Eugene Stanley, “Random matrix approach to cross 
correlations in financial data,” Physical Review 65 (June 2002). 
13 Random matrices are covered in Chapter 12. 

523 
Capital Asset Pricing Model 
though not necessarily in equal proportion. This eigenvector approxi-
mately corresponds to the entire market. The other largest eigenval-
ues correspond to eigenvectors that identify market sectors. The 
eigenvectors corresponding to the largest eigenvalues exhibit some 
degree of stability in time, the most stable being those corresponding 
to the largest eigenvalues. Stability is measured by computing eigen-
values and eigenvectors on a moving window and counting the per-
centage of assets forming each eigenvector that remain unchanged. 
Based on a remarkably large data set, work by Plerou et al. identi-
fies a number of different meaningful eigenvectors. The multiplicity of 
eigenvectors corresponding to large eigenvalues suggests a structure of 
multiple factors as portfolios. Note that the largest eigenvector is not 
the market portfolio. In fact, the market portfolio includes all investable 
assets. Therefore, it includes assets that are not in the largest eigenvec-
tor. This fact leaves open the door to a possible coexistence of CAPM 
and multifactor models. In order to explore this point, we need first to 
discuss the Conditional CAPM, Asset Pricing Theory, and multifactor 
models. We discuss the Conditional CAPM in this chapter and the last 
two models in the next chapter. 
THE CONDITIONAL CAPM 
As we have seen, the CAPM is embodied in a static linear regression of 
asset returns over the market portfolio whose explanatory power has 
been questioned by, among others, Fama and French.14 Ravi Jagan-
nathan and Zheniu Wang15 suggested a solution: They made the CAPM 
regression coefficients conditional on some global information set, 
thereby generalizing the model. Called the Conditional CAPM or 
C(CAPM), this model represents each expected return rit given the 
information set at time t by the conditional linear regression: 
E[rt ⁄
] = α + βE[ft ⁄
]
It – 1 
It – 1 
cov(ritfst ⁄
)
It – 1 
= ----------------------------------------
βis 
var(fst ⁄
)
It – 1 
14  Fama and French, “The Cross-Section of Expected Stock Returns.” 
15 Ravi Jagannathan and Zhenyu Wang, “The Conditional CAPM and the Cross-
Section of Expected Returns,” Journal of Finance 51, no. 1, pp. 3–53. 

524 
The Mathematics of Financial Modeling and Investment Management 
A difficulty with C(CAPM) is to identify the conditioning relation-
ships as well as the market portfolio. Jagannathan and Wang show that 
the unconditional returns generated by a C(CAPM) can be thought of as 
being generated by a two-factor model where one factor is the uncondi-
tional beta and the other represents the fluctuations of beta. This con-
clusion can be generalized. A C(CAPM) model is equivalent to a 
nonlinear factor model.16 
Jagannathan and Wang show that the C(CAPM) is able to represent 
the cross section of stock returns with a greater accuracy than the con-
ventional unconditional CAPM. They also show that the empirical accu-
racy of the unconditional CAPM is greatly improved by adding human 
capital to the market portfolio. Human capital is not a tradable asset, at 
least not in the same sense as financial assets. 
BETA, BETA EVERYWHERE 
In the development of both modern portfolio theory and CAPM, the 
Greek letter beta appears. Certainly to the mathematically trained, this 
presents no problem. However, it caused confusion in the investment 
management community. The use of the term “beta” in the two theories 
was as follows. First, because of the difficulty of working with the cova-
riance matrix at the time, Markowitz suggested using as a proxy mea-
sure of the full covariance matrix a covariance of a security’s return 
with some index.17 Sharpe picked up on this suggestion and proposed 
the following model for doing so which he referred to as the market 
model:18 
rit = αi + βi rmt + uit 
Note that the index need not be a market portfolio—hence the use of m 
rather than M in the above equation. When Sharpe estimated the market 
model, he used a stock market index. 
Then beta appeared in the CAPM where it is estimated from the 
characteristic line which we discussed earlier. The market model and the 
characteristic line look almost identical. The difference is simply that 
16 For more on this subject see, for instance, Adrian Pagan, “The Econometrics of 
Financial Markets,” Journal of Empirical Finance 3 (1996), pp. 15–102. 
17 Harry M. Markowitz, Portfolio Selection: Second Edition (Cambridge, MA: Basil 
Blackwell Ltd., 1991), p. 100. 
18 William F. Sharpe, “A Simplified Model for Portfolio Analysis,” Management Sci-
ence (January 1963), pp. 277–293. 

525 
Capital Asset Pricing Model 
the characteristic line measures the return relative to the risk-free rate in 
each period. In the case of the characteristic line, a proxy for the market 
portfolio is used. This is in contrast to the market model where the 
index need not be the market portfolio. 
This distinction between the beta in the market model and the beta 
in the characteristic line is important. As we will see in the next section, 
critics of portfolio selection and the CAPM have incorrectly made state-
ments about the drawbacks of these theories because they fail to under-
stand the distinction between these two betas. Adding to the confusion 
was that Sharpe introduced both of these beta concepts around the same 
time (1963 and 1964). 
THE ROLE OF THE CAPM IN INVESTMENT MANAGEMENT 
APPLICATIONS 
In 1980, a highly regarded magazine published an article with the title 
“Is Beta Dead?”19 In response to this article, in its Winter 1981 issue 
The Journal of Portfolio Management published a series of articles. The 
article by Barr Rosenberg in particular provides an excellent discussion 
of the CAPM and its role.20 
The key to the CAPM’s contribution to investment management the-
ory is clearly stated by Rosenberg: 
The CAPM is theory, but, paradoxically, the role of the 
CAPM as “theory” leading to application has been less 
important than its role in mobilizing attention and defin-
ing constructs. We should keep in mind that the CAPM is 
not “true,” since many of its assumptions are not exactly 
satisfied in the real world. Indeed, the CAPM rules out 
active management and investment research, and thus 
abolishes most applications at the stroke of a pen, by vir-
tue of the unrealistic assumptions that it makes. (p. 5) 
That is, even though the CAPM is not true it does not mean that the 
constructs introduced by the theory are not important. Constructs intro-
duced in the development of the theory include the notion of a market 
portfolio, systematic risk, diversifiable risk, and beta. As Rosenberg 
19 Anise Wallace, “Is Beta Dead?” Institutional Investor (July 1980), pp. 23–30. 
20 Barr Rosenberg, “The Capital Asset Pricing Model and the Market Model,” The 
Journal of Portfolio Management (Winter 1981), pp. 5–16. 

526 
The Mathematics of Financial Modeling and Investment Management 
notes: “These ideas play an important role in the methods of ‘modern 
portfolio theory.’” 
In the next chapter we will discuss another asset pricing model that 
introduces risk factors other than market risk. Earlier in this chapter we 
also discussed other models that consider nonmarket risk factors. How-
ever, these do not invalidate the important constructs developed by the 
CAPM. Rosenberg concludes his article with the following statement: 
The question of rewards for factors other than equity mar-
ket risk has been the subject of active study and contro-
versy for a decade—and no doubt will continue to be so in 
the decades to come. Nevertheless, no one has refuted the 
existence of equilibrium reward for equity market risk; 
indeed, it has rarely been questioned, although the magni-
tude has been in doubt. The concept of reward to equity 
market risk (or beta) is a theoretical insight, that, in my 
view, is likely to endure. (p. 16). 
Fast forward a little more than two decades since the publication of the 
Rosenberg article and his conclusions still hold.21 
Moreover, Markowitz has explained that the major reason for the 
debate is the confusion between the beta that is associated with the mar-
ket model (estimated to avoid having to compute all covariances for 
assets in a portfolio) and the beta in the CAPM, a point we emphasized 
in the previous section.22 
SUMMARY
 ■ The Capital Asset Pricing Model (CAPM) is a general equilibrium the-
ory based on the assumption that investors are rational and subscribe 
to the Markowitz mean-variance framework.
 ■ A key finding of the CAPM is that, in a situation of equilibrium 
between demand and supply, if agents optimize in the sense of mean-
21 These sentiments were echoed in a presentation by Peter Bernstein in a keynote ad-
dress on the occasion of the fifth anniversary of the establishment of the Internation-
al Center for Financial Management & Engineering (FAME) in Geneva on February 
7, 2002. (See “How Modern is Modern Portfolio Theory?” Economics and Portfolio 
Strategy, Peter L. Bernstein, Inc., March 15, 2002.) 
22 Harry M. Markowitz, “The ‘Two Beta’ Trap,” The Journal of Portfolio Manage-
ment (Fall 1984), pp. 12–20. 

527 
Capital Asset Pricing Model 
variance optimization, then the total investable portfolio, called the 
market portfolio, is mean-variance efficient.
 ■ From the mean-variance efficiency of the market portfolio, Sharpe, 
Lintner, Treynor, and Mossin were able to derive the fundamental lin-
ear relationship between the expected value of each security and that of 
the market portfolio.
 ■ In the CAPM, risk is decomposed into diversifiable risk and systematic 
or market risk; it is only systematic risk for which an investor should 
be compensated.
 ■ CAPM has been extensively tested using regression-based procedures.
 ■ The fundamental linearity of risk-return relationship seems to be con-
firmed; however, it seems likely that more than one factor is needed to 
explain returns.
 ■ The empirical testability of CAPM has been questioned given that the 
market portfolio cannot be empirically identified.
 ■ CAPM has had a lasting influence on finance theory and on the prac-
tice of asset management. 



## Multifactor Models and Equity Portfolio

I 
CHAPTER 18 
Multifactor Models and 
Common Trends for 
Common Stocks 
n this chapter we discuss how multifactor models are used in the man-
agement of equity portfolios; in Chapter 20 we will discuss how they 
are applied to bond portfolio management. Multifactor models are a 
broad family of econometric models. Essentially, a multivariate process 
admits a multifactor representation if it can be approximately (or 
exactly) expressed as a function of another multivariate process of a 
smaller dimensionality. The general multifactor formulation of a model 
has to be clearly distinguished from the economic theory that might be 
behind it. In fact, multifactor models might be the expression of an eco-
nomic theory as well as the result of an explicit econometric dimension-
ality reduction process. 
For example, the Capital Asset Pricing Model (CAPM) is a general 
equilibrium theory which is embodied in a single-factor linear model. In 
this case, the factorization is the expression of a theoretical formulation. 
The same considerations apply to the Arbitrage Pricing Theory (APT): a 
multifactor model embodies a pricing theory based on the absence of 
arbitrage. However, given a multivariate process, econometric factor 
analysis techniques yield a dimensionality reduction which is also 
embodied in a multifactor model. In the latter case the process is purely 
statistic, not supported by theory. In this sense, the statement, often 
found in the literature, that CAPM and APT are factor models might be 
slightly misleading. It should be clear that both are economic theories, 
general equilibrium and arbitrage pricing respectively, which happen to 
be expressed as multifactor models. 
529 

530 
The Mathematics of Financial Modeling and Investment Management 
It is likely that in the long run all price processes follow one single 
common trend with the exception of disruptive events such as bankrupt-
cies or mergers and acquisitions. This trend-following behavior, how-
ever, might exhibit a complex dynamical structure. Within the time 
horizons that are empirically available, multiple trends, mean reversion, 
and structural breaks are at work. We will first analyze classical multi-
factor models of returns and how they are constructed and used in 
investment management. Subsequently, we will discuss dynamic factor 
models. 
MULTIFACTOR MODELS 
Let’s introduce multifactor models of returns. The general form of a lin-
ear multifactor market model of returns can be written in one of the fol-
lowing ways: 
[ ] = α
β' E f
E r
+ 
[ ]  
[ 
ft] =
+ βift
E rit 
αi 
p 
rit = αi + ∑βisfst + εt 
s = 1 
where: 
rit = the return of the i-th security at time t 
ai 
= constants specific for the i-th security 
βis = the sensitivity of the i-th security to the s-th factor 
ft 
= the s-th factor at time t and εt is a noise process 
In this linear regression model, assuming that factors are orthogonal 
(that is, uncorrelated), the sensitivities βis, referred to as betas, can be 
written as: 
cov(ritfst) 
= -------------------------
βis 
var fst
(
)
 
As both returns and factors are assumed to be stationary stochastic 
processes, unconditional means and covariances are time-independent 

531 
Multifactor Models and Common Trends for Common Stocks 
constants. The first formulation expresses a linear relationship between 
the unconditional means of the returns and of the factors. The second 
formulation is the linear regression function which expresses a linear 
relationship between the mean of returns at time t conditional on the 
realization of the factors at the same time; the third is the standard for-
mulation of the linear regression of returns on factors. 
Obviously returns and factors are all defined on the same probabil-
ity space and have a joint pdf.1 Recall from Chapter 6 on probability 
theory that joint multivariate normal distributions factorize in a linear 
regression. In the case of joint normality, returns, factors and noise all 
have normal joint distributions. However other distributions, for 
instance the Student-t, factorize in a linear regression while distribu-
tions such as lognormal and Pareto distributions do not factorize in a 
linear regression. 
Factors range from innovations to exogenous variables, such as 
macroeconomic variables, to abstract factors formed as linear combina-
tions of the processes. The multifactor model is a regression between 
variables at the same time and does not specify a dynamics for these 
variables. In other words, a multifactor model is not, per se, a predictive 
model. To perform forecasts and parameter estimates, a process dynam-
ics of factors must be specified. The simplest dynamic assumption is that 
factors are independent and identically distributed (IID) variables. In 
this case, the noise is a white noise. Other specifications of factors 
dynamics have been proposed; these will be discussed later. 
Factor market models can be generalized to include linear condi-
tional factor models where factors and returns are conditional on some 
information set I known at time t – 1. The information set will contain 
the history of returns and factors up to time t – 1 and, possibly, other 
variables. Linear conditional factor models are written as follows: 
E[rt 
] = α
βE[ft
+ 
]
It – 1 
It – 1 
where the constants are now time-dependent and conditional on the 
information set: 
cov(ritfst 
)
It – 1 
= --------------------------------------
βis 
var(fst 
)
It – 1 
1 For a discussion of what families of joint pdfs admit a linear regression function, 
see, amongst other, A. Spanos, Statistical Foundations of Econometric Modeling 
(Cambridge, U.K.: Cambridge University Press, 1986). 

532 
The Mathematics of Financial Modeling and Investment Management 
Determination of Factors 
Let’s now see how factors can be determined. Exogenous factors are 
determined through considerations of macroeconomic theory and fun-
damentals of each firm. Abstract factors are determined through a pro-
cess of statistical analysis. We begin by describing the determination of 
exogenous factors and then of abstract factors. 
Exogenous Factors2 
There are several commercially available fundamental multifactor risk 
models. Investment management companies often develop their own 
proprietary models. Brokerage firms have developed models that they 
make available to institutional clients. In this section, we will focus on a 
commercially available model from Barra. The basic relationship to be 
estimated in a multifactor risk model is 
Ri − Rf = βi,F1 RF1 + βi,F2 RF2 + … + βi,FH RFH + ei 
where: 
Ri 
= rate of return on stock i 
Rf 
= risk-free rate of return 
βi,Fj = sensitivity of stock i to risk factor j 
RFj = rate of return on risk factor j 
ei 
= nonfactor (specific) return on security i 
The above function is referred to as a return generating function. 
Fundamental factor models use company and industry attributes 
and market data as “descriptors.” Examples are price/earnings ratios, 
book/price ratios, estimated earnings growth, and trading activity. The 
estimation of a fundamental factor model begins with an analysis of his-
torical stock returns and descriptors about a company. In the Barra 
model, for example, the process of identifying the risk factors begins 
with monthly returns for 1,900 companies that the descriptors must 
explain. Descriptors are not the “risk factors” but instead they are the 
candidates for risk factors. The descriptors are selected in terms of their 
ability to explain stock returns. That is, all of the descriptors are poten-
tial risk factors but only those that appear to be important in explaining 
stock returns are used in constructing risk factors. 
2 The discussion in this section draws from Frank J. Fabozzi, Frank J. Jones, and Ra-
man Vardharaj, “Multi-Factor Equity Risk Models,” Chapter 13 in Frank J. Fabozzi 
and Harry M. Markowitz (eds.), The Theory and Practice of Investment Manage-
ment (Hoboken, NJ: John Wiley & Sons, 2002). 

533 
Multifactor Models and Common Trends for Common Stocks 
Once the descriptors that are statistically significant in explaining 
stock returns are identified, they are grouped into “risk indices” to cap-
ture related company attributes. For example, descriptors such as market 
leverage, book leverage, debt-to-equity ratio, and company’s debt rating 
are combined to obtain a risk index referred to as “leverage.” Thus, a risk 
index is a combination of descriptors that captures a particular attribute 
of a company. The Barra fundamental multifactor risk model, the “E3 
model” being the latest version, has 13 risk indices and 55 industry 
groups. Exhibit 18.1 lists the 13 risk indices in the Barra model.3 
Also shown in the exhibit are the descriptors used to construct each 
risk index. The 55 industry classifications are further classified into sec-
tors. For example, the following three industries comprise the energy 
sector: energy reserves and production, oil refining, and oil services. The 
consumer noncyclicals sector consists of the following five industries: 
food and beverages, alcohol, tobacco, home products, and grocery 
stores. The 13 sectors in the Barra model are basic materials, energy, 
consumer noncyclicals, consumer cyclicals, consumer services, industri-
als, utility, transport, health care, technology, telecommunications, com-
mercial services, and financial. 
Given the risk factors, information about the exposure of every 
stock to each risk factor (βi,Fj) is estimated using statistical analysis. For 
a given time period, the rate of return for each risk factor (RFj) also can 
be estimated using statistical analysis. The prediction for the expected 
return can be obtained from the above equation for any stock. The non-
factor return (ei) is found by subtracting the actual return for the period 
for a stock from the return as predicted by the risk factors. 
Moving from individual stocks to portfolios, the predicted return for 
a portfolio can be computed. The exposure to a given risk factor of a 
portfolio is simply the weighted average of the exposure of each stock in 
the portfolio to that risk factor. For example, suppose a portfolio has 42 
stocks. Suppose further that stocks 1 through 40 are equally weighted in 
the portfolio at 2.2%, stock 41 is 5% of the portfolio, and stock 42 is 
7% of the portfolio. Then the exposure of the portfolio to risk factor j is 
0.022 β1,Fj + 0.022 β2,Fj + … + 0.022 β40,Fj + 0.050 β41,Fj + 0.007 β42,Fj 
The nonfactor error term is measured in the same way as in the case of 
an individual stock. However, in a well diversified portfolio, the nonfactor 
error term will be considerably less for the portfolio than for the individ-
3 For a more detailed description of each descriptor, see Appendix A in Barra, Risk 
Model Handbook United States Equity: Version 3 (Berkeley, CA: Barra, 1998). A 
listing of the 55 industry groups is provided in Exhibit 13.9. 

534 
The Mathematics of Financial Modeling and Investment Management 
ual stocks in the portfolio. The same analysis can be applied to a stock 
market index because an index is nothing more than a portfolio of stocks. 
Abstract Factors 
Suppose now that factors are abstract static factors under the assump-
tion that returns are normally distributed IID variables. Under this 
assumption, two basic techniques can be used: factor analysis and prin-
cipal components analysis. We’ll begin with factor analysis. 
Suppose that there is a strict factor structure with a known number 
of undetermined factors of the form: 
r = α + Bf + ε
N 
fi = ∑α r
s s 
s = 1 
where factors are linear combinations of returns. A strict factor struc-
ture means that factors explain all the covariance between the process 
components. Under this assumption, factors are processes with a vari-
ance-covariance matrix ΩF while the innovations ε are assumed to be 
uncorrelated and have a diagonal variance-covariance matrix D. Under 
these assumptions, the variance-covariance matrix Ω of the multivariate 
process r of returns can be written as the sum of two contributions: 
Ω= BΩFB′ + D 
This representation is not unique as factors are not uniquely deter-
mined. In fact, given any set of factors, one obtains another set of fac-
tors by multiplying the former by an orthonormal matrix G GG′ = I .
, 
This indeterminacy allows one to choose orthogonal factors with unit 
variance so that their variance-covariance matrix is a unitary matrix 
and the return process variance-covariance matrix can be written as: 
Ω= BB′ + D 
This relationship is a constraint on the return variance-covariance 
matrix. The latter can be estimated with MLE techniques. The resulting 
computations are numerically complex. However, many software pack-
ages efficiently perform factor analysis. After estimating the matrix of 
factor sensitivities, the factors themselves can be estimated with MLE 

535 
Multifactor Models and Common Trends for Common Stocks 
EXHIBIT 18.1 
Barra E3 Model Risk Definitions 
Descriptors in Risk Index 
Risk Index 
Beta times sigma 
Volatility 
Daily standard deviation 
High-low price 
Log of stock price 
Cumulative range 
Volume beta 
Serial dependence 
Option-implied standard deviation 
Relative strength 
Momentum 
Historical alpha 
Log of market capitalization 
Size 
Cube of log of market capitalization 
Size nonlinearity 
Share turnover rate (annual) 
Trading activity 
Share turnover rate (quarterly) 
Share turnover rate (monthly) 
Share turnover rate (five years) 
Indicator for forward split 
Volume to variance 
Payout ratio over five years 
Growth 
Variability in capital structure 
Growth rate in total assets 
Earnings growth rate over the last five years 
Analyst-predicted earnings growth 
Recent earnings change 
Analyst-predicted earnings-to-price 
Earnings yield 
Trailing annual earnings-to-price 
Historical earnings-to-price 
Book-to-price ratio 
Value 
Variability in earnings 
Earnings variability 
Variability in cash flows 
Extraordinary items in earnings 
Standard deviation of analyst-predicted earnings-to-price 
Market leverage 
Leverage 
Book leverage 
Debt to total assets 
Senior debt rating 
Exposure to foreign currencies 
Currency sensitivity 
Predicted dividend yield 
Dividend yield 
Indicator for firms outside US-E3 estimation universe 
Nonestimation 
Universe indicator 
Source: Adapted from Table 8-1 in Barra, Risk Model Handbook United States 
Equity: Version 3 (Berkeley, CA: Barra, 1998), pp. 71–73. Adapted with permis-
sion. 

536 
The Mathematics of Financial Modeling and Investment Management 
techniques. In general one finds the entire set of N returns as one factor 
plus a number of additional factors as we have seen in Chapter 12. 
Another statistical technique for determining factors is principal 
components analysis (PCA). As explained in Chapter 12, PCA is imple-
mented by computing the eigenvalues of the estimated variance-covari-
ance matrix. As shown in the study by Plerou et al., the distribution of 
eigenvalues typically follows that of a random matrix with the excep-
tion of a number of outliers. These outliers are the eigenvalues and the 
corresponding eigenvectors that form the factors. 
PCA (as well as factor analysis) is a powerful statistical technique with 
a deep economic interpretation. To see this point, let’s analyze the largest 
eigenvalues and the corresponding eigenvectors. The largest eigenvalue cor-
responds to an eigenvector whose components are all approximately equal 
to 1/N. Therefore, the largest eigenvalue corresponds to the entire market. 
The other large eigenvalues correspond to eigenvectors that have only a 
subset of components different from zero. The important finding is that 
these eigenvectors correspond to specific market sectors. In fact, the assets 
corresponding to the nonzero components of the largest eigenvectors corre-
spond with good approximation to the Standard & Poor’s market sector 
classification. Exhibit 18.2 shows the results obtained by performing PCA 
on the correlation matrix of the S&P 500 stocks in the period January 2, 
2001–September 19, 2003. The ten largest eigenvalues correspond with 
good approximation to ten sectors of the Standard & Poor’s classification.4 
That the ten largest eigenvalues correspond to ten sectors of the 
Standard and Poor’s classification is a powerful and somewhat surpris-
ing result in empirical financial econometrics. Performing PCA on a 
large aggregate of stock prices, we find that the information-carrying 
eigenvalues identify stable subsets of the market that correspond to 
meaningful sectors. It is an important theoretical-empirical finding that 
lends support to the use of factor analysis in financial econometrics. 
The eigenvector corresponding to the largest eigenvalue identifies 
the entire market. Note that this eigenvector is a totally different con-
cept than the “market portfolio” of the CAPM. In fact, the market port-
folio of the CAPM, which is obtained as a General Equilibrium Theory 
and not as a factor model, includes all investable assets and not only 
stocks. Performing PCA on a large aggregate of stock prices one obtains 
a multiplicity of factors. In principle, on a very large sample, the two 
methods—factor analysis and PCA—yield the same result. On a finite 
sample, however, results might differ significantly. Note that both factor 
analysis and PCA tend to solve the problems of the sample limitations. 
4 The details of the methodology to arrive at these results can be found in Plerou, et 
al., “Random Matrix Approach to Cross Correlations in Financial Data.” 

537 
Multifactor Models and Common Trends for Common Stocks 
EXHIBIT 18.2 
PCA Performed on Correlations Matrix of S&P 500 Stocks, 
January 2, 2001–September 19, 2003 
DYNAMIC MARKET MODELS OF RETURNS 
Now let’s consider stationary return processes with a dynamics more 
complex than that of an IID sequence of variables. A reasonable gener-
alization of factor market models are state-space models of the form 
that was described in Chapter 12: 
rt = α + Azt + Bεt 
zt + 1 = Czt + Dεt 
Note that z is non-observable. Therefore, the noise term can be 
placed either at t or t – 1. The first equation is the usual regression of a 
factor market model while the second equation is a one-lag stationary 
Vector Auto Regressive—denoted by VAR(1)—model that describes the 
autoregressive dynamics of the factors. Note that we assume that the 
above equations describe the dynamics of returns; the following section 
discusses how similar equations might describe prices. 

538 
The Mathematics of Financial Modeling and Investment Management 
Dynamic market models of this type can be used to create meaning-
ful scenarios for multistage stochastic optimization. The VAR part of 
the model might describe the evolution of macroeconomic variables. If 
the objective is to apply multistage optimization and stay within the 
domain of linear models of returns, state-space models are the models of 
choice. As we have seen in Chapter 11, any stationary or asymptotically 
stationary linear model can be represented in this form. 
Estimation of State-Space Models 
Methods for the estimation of state-space models were originally devel-
oped for engineering applications. State-space systems can be estimated 
using MLE methods.5 In 1990 Masanao Aoki6 introduced a methodol-
ogy called the subspace algorithm to estimate state-space models; Diet-
mar Bauer and Martin Wagner7 subsequently showed how to apply 
subspace algorithms to cointegrated systems. 
It was R. E. Kalman8 who, in 1960, introduced a recursive methodol-
ogy for making forecasts based on state-space models. Known as the Kal-
man filter, the methodology proved very successful in engineering before 
being applied more recently in economics and finance. Given a state-space 
model, a Kalman filter computes recursively the best estimate of state: 
zˆ
= E zt
[ 
r0, …, rt]
t t  
Kalman filters are now implemented in many software packages. 
DYNAMIC MODELS FOR PRICES 
The models discussed above are single factor or multifactor linear mod-
els of returns; the risk-return trade-off entailed by these models leads to 
price processes that diverge exponentially. To see this point, consider 
that, given log prices, returns are approximately differences of log-
prices. Therefore, log-prices are obtained by adding returns (i.e., they 
are a random-walk) and the real prices are then obtained taking the 
5 See, for instance, Helmut Luetkepohl, Introduction to Multiple Time Series Analy -
sis (New York: Springer, 1991). 
6 Masanao Aoki, State Space Modelling of Time Series (New York: Springer, 1990). 
7 D. Bauer and M. Wagner, “Estimating Cointegrated Systems Using Subspace Algo -
rithms,” Journal of Econometrics 11 (2002), pp. 47–84. 
8 R.E. Kalman, “A New Approach to Linear Filtering and Prediction Problems,” 
Transactions of the ASME-Journal of Basic Engineering (March 1960), pp. 35–45. 

539 
Multifactor Models and Common Trends for Common Stocks 
exponentials. If returns are jointly normally distributed, then log prices 
are jointly normally distributed while the real prices are lognormally 
distributed. Suppose that a variable X is normally distributed with 
expected value and variance µ, σ2. The variable ex is lognornomally dis-
tributed with the following expected value and variance: 
1 
µ + -- σ2 
2 
e 
, σ2(e σ2 
– 1) 
If returns are Independent and Identical Normal (IIN) variables, lin-
ear factor models imply that prices with different factor sensitivities will 
have different average returns, an expression of the risk-return trade-off 
required by investors. In addition, the variance of log prices will grow 
linearly with time at different rates for each process. The means that dif-
ferent price processes will therefore evolve exponentially at different 
rates and diverge exponentially. Under the assumption that factors 
behave as a stationary Vector Auto Regressive (VAR) Model as in the 
state space-models, the dependence is more complex but there is still an 
exponential divergence of prices. 
An exponential divergence of prices is not sustainable in the long 
run. Clearly corrective phenomena are at work in financial markets, 
though exactly how corrections are made is the subject of different 
hypotheses. It has been hypothesized that stock price processes are sub-
ject to discrete regime-changes; this assumption, widely studied in the 
literature, leads to nonlinear models. It has also been hypothesized that 
disruptive phenomena are at work, so that the price of a firm’s stock 
might grow rapidly but then the firm is subject to phenomena such as 
bankruptcy, merger, acquisition or corporate restructuring; this links 
financial theory to macroeconomics and is beyond the scope of this 
book. A third hypothesis is that correction phenomena—and perhaps 
discrete changes—are always at work in markets; these phenomena can 
be modeled within the domain of linear models with the techniques of 
cointegration. The fact that portfolio separation in a fixed and closed 
economy implies collinearity lends additional theoretical support to the 
cointegration of asset prices. Bossaert showed how cointegration natu-
rally arises if one slightly relaxes the assumption of separation.9 
Cointegration (see Chapter 12 can be modeled in two different but 
equivalent ways, using either state-space models or Error Correction 
Models (ECMs). ECMs are VAR models with restrictions. Consider that 
it is always possible to write a VAR model in ECM form: 
9 Peter Bossaerts, “Common Nonstationary Components of Asset Prices,” Journal of 
Economic Dynamics and Control 12 (1988), pp. 347–364. 

540 
The Mathematics of Financial Modeling and Investment Management 
∆xt = (Φ1L + Φ2L2 + … + Φ
Ln – 1)∆xt + Πxt + m + εt
n – 1 
The error correction restrictions apply to the matrix Π. An ECM is a 
VAR model with Π = αβ′ where α, β are n×r matrices. The term in level 
provides the error correction. The Granger Representation Theorem 
demonstrated by Granger in 198710 states that if a process is cointe-
grated with r cointegrating relationships then the above ECM holds. 
James Stock and Mark Watson11 first observed in 1988 that a coin-
tegrated model with r cointegrating relationships admits n–r common 
trends. The implication is that all time series can be written in the form 
xt = a
Azt + ηt
+ 
where the zt are the common stochastic trends, which are I(1) integrated 
processes, and the ηt are stationary processes. 
Models for cointegration can be extended in various ways. In the 
context of cointegration, Hashem Pesaran and Yongcheol Shin12 intro-
duced the Autoregressive Distributed Lag (ARDL) models. An ARDL 
model contains exogenous variables that are not cointegrated among 
themselves. It has the following form: 
xt = α0 + α1t + (Φ1L + Φ2L2 + … + ΦpLp )xt + βzt 
+
+ (β1L + β2L2 + …
βqLq )∆zt + ut 
+
0 = (P1L
P2L2 + … + P Ls)∆zt + εt
s
where the z are I(1) noncointegrated variables and the y exhibit r cointe-
grating relationships. Pesaran and Shin demonstrated that the classical 
approach to ARDL systems that are valid for stationary processes can 
be extended to integrated processes. 
Cointegration models can also be extended in the sense of dynamic 
cointegration (or polynomial cointegration). Cointegrating relationships 
are static relationships between variables taken at the same time; 
10 R.F. Engle and C.W.J. Granger, “Cointegration and Error Correction: Represen-
tations, Estimation and Testing,” Econometrica 55 (1987), pp. 252–276. 
11 James Stock and Mark Watson, “Testing for Common Trends,” Journal of the 
American Statistical Association 83 (December 1988), pp. 1097–1107. 
12 Hashem M. Pesaran and Yongcheol Shin, “An Autoregressive Distributed Lag 
Modelling Approach to Cointegration Analysis,” Chapter 11 in S. Strom (ed.), 
Econometrics and Economic Theory in the 20th Century (Cambridge, U.K.: Cam-
bridge University Press, 1999). 

541 
Multifactor Models and Common Trends for Common Stocks 
dynamic cointegration introduces a small number of lags in the cointe-
grating relationship. In other words, cointegration reduces the order of 
integration by applying linear regressions between variables; dynamic 
cointegration reduces the order of integration by applying autoregres-
sive modeling. A VAR model with n lags 
xt =
+ … + Anxt
n + εt
A1xt – 1 + A2xt – 2 
– 
exhibits dynamic cointegration if there exists a stationary autoregressive 
combination of the variables of the type 
α′xt + β′∆xt 
Cointegration and dynamic cointegration can coexist in the same 
model in the sense that variables can be cointegrated and dynamically 
cointegrated. Note that, if the log price process is integrated of order 1, 
then the return process is stationary so that factor models for returns and 
cointegrated models for prices can coexist. In addition, linear combina-
tions of prices and returns can also be stationary. 
Cointegration is equivalent to the existence of common stochastic 
trends. This property is also expressed by the equivalence between an 
ECM and a state-space model. Recall that a state-space model is written 
as 
xt = a
Azt + Bµt
+ 
zt + 1 = Czt + Dεt 
where state-space variables are either stationary or integrated variables. 
Although a cointegrated price system of price processes can always be 
expressed as a state-space model, the variables in the state-space repre-
sentation might include lagged prices. This fact was shown in Chapter 
12 when addressing the question of the equivalence between ARMA 
models and state-space models. In general, prices might be expressed in 
the following factor form: 
p
q 
pt = st + ∑ Aipt
i + ∑ Bjft
j + ut
–
– 
i = 1 
j = 0 

542 
The Mathematics of Financial Modeling and Investment Management 
s 
ft = ∑ Ckft
k + ηt
– 
k = 1 
where the price processes pt have an autoregressive distributed-lag 
dynamics, the factors ft follow a VAR or VARMA model, the terms ut 
are idiosyncratic (i.e., they are mutually uncorrelated), and st are deter-
ministic terms. The terms ut and ηt might be white noise or might be 
autocorrelated (i.e., they are a stationary process that obeys ARMA 
equations). 
Factor models can be cast in the state-space representation. Con-
sider, for example, the following model: 
pt = Bft + ut 
s 
ft = ∑ Ckft
k + ηt
– 
k = 1 
and 
q 
ut = ∑ Hkut
k + εt
– 
k = 1 
An equivalent state-space model can be obtained by defining the follow-
ing state vector: 
zt ′ = [ft…ft
put…ut
q]
–
– 
and the following transition matrix: 
C . 0  
0
C1 … Cs – 1 
s
ηt
I 
0 
0 . 
.
.
. 
0
.
.
.
.
.
. .  
..
0
.
0 … 
I 
0 . 0  
0
zt = 
.
.
.
. . .
.
. 
. zt – 1 + 
0 
0 . H1 … Hq – 1 Hq 
εt 
0 
. I 
0
0 
..
.
.
.
.
.
.
.
. 
.
.
. 
0
0 
0 . 0 … 
I 
0 

543 
Multifactor Models and Common Trends for Common Stocks 
The static-factor model and the common-trend cointegrated model are 
special cases of the above general dynamic factor model. The ARDL 
model is a dynamic factor model with additional restrictions. 
A conceptual parallel can be made between state-space models and fac-
tor models. Recall that factor models essentially address the problem of a 
nearly random cross-correlation matrix. The correlation coefficients of a 
large correlation matrix are essentially random. To recover a meaningful 
correlation structure, every process is represented as a linear regression on 
a set of factors and only correlations between factors are considered. 
Were we to attempt an estimate of a global VAR model of a large 
portfolio of equity prices or return processes, we would run into the same 
problem of finding meaningless random autocross correlation coefficients. 
This is because the matrices that represent all the correlations at different 
time lags are nearly random. State-space models extract the useful auto-
correlation information from a large set of auto-cross-correlation data. 
Estimation and Testing of Cointegrated Systems 
The estimation and testing of cointegrated systems is a complex issue on 
which there is vast literature. The two major methods for estimation of 
cointegrated systems are due to Engle and Granger13 and Johansen.14 The 
Engle-Granger method is based on writing down explicitly the long-run 
regression equation and subsequently estimating the short term correc-
tions. The Johansen methodology applies directly MLE methods. Stock 
and Watson15 proposed PCA to determine the common trends.16 
When dealing with large sets of asset prices, in particular equity 
prices, the techniques of Engle-Granger and Johansen are not applica-
ble. The PCA-based approach of Stock and Watson, on the other hand, 
can be applied to hundreds of price processes. The Stock and Watson 
methodology is based on the observation that if there are r cointegra-
tion relationships the resulting n-r common trends are integrated I(1) 
while the r cointegrating portfolios are stationary I(0). Consequently, it 
is reasonable to assume that the integrated portfolios have maximum 
variance. Therefore, performing PCA on the variance-covariance matrix 
of the price process should lead to identification of the number and the 
13 Engle and Granger, “Cointegration and Error Correction: Representations, Esti -
mation and Testing.” 
14 S. Johansen, Likelihood-based Inference in Cointegrated Vector Autoregressive 
Models (Oxford: Oxford University Press, 1995). 
15 Stock and Watson, “Testing for Common Trends.” 
16 The interested reader should consult the original works quoted or, G.S. Maddala 
and In-Moo Kim, Unit Roots, Cointegration, and Structural Changes (Cambridge, 
U.K.: Cambridge University Press, 1988). 

544 
The Mathematics of Financial Modeling and Investment Management 
weights of cointegrating vectors. The PCA-based approach can also be 
applied in the frequency domain. The analysis in the frequency domain 
is an alternative way of analyzing time series. It is based on constructing 
a transform of the time series which is the discrete equivalent of a Fou-
rier transform discussed in Chapter 4.17 
An alternative estimation methodology which is suitable for large 
sets is the subspace-space algorithm introduced by Aoki (ref. cited) in 
the context of stationary systems and extended by Bauer and Wagner 
(ref. cited) to integrated systems and to polynomial cointegration.18 
Cointegration and Financial Time Series 
Cointegration is an important technique for portfolio management: It 
allows an investor to detect mispricings and thus sources of profit. In 
fact, if a set of price processes exhibit cointegration, relative returns are 
autocorrelated and therefore predictable. In other words, as we will see 
in Chapter 19, although individual price processes might be unpredict-
able random walks, there are portfolios which exhibit a stationary, 
mean-reverting behavior. For this reason cointegration has attracted the 
attention of both academics and practitioners, especially in the areas of 
index tracking and hedge fund management. 
However, cointegration technology was initially developed in the 
area of macroeconomics where only a small number of variables, gener-
ally less than 10, are used. Extending the concepts of cointegration to a 
large number of equity prices or return processes is difficult both from 
the numerical and theoretical standpoints. Assume, for example, that 
one is working on a large set of equity log-price processes such as those 
in the S&P 500. Standard cointegration estimation and testing methods 
such as the Johansen procedures do not work for sets of processes of 
this size. 
Consider also that in finite samples of sets of processes such as those 
found in the S&P 500, spurious cointegrating relationships will be 
detected. This happens because in a large set of independent processes a 
cointegration test run on a relatively small sample of points will ran-
domly test positive for many cointegrating relationship. For example, 
one finds a significant number, in the range of a few percentage points, 
of cointegrated pairs of processes in computer-generated independent 
arithmetic random walks. 
17 P.C.B. Phillips and S. Ouliaris, “Testing for Cointegration Using Principal Com -
ponents Methods,” Journal of Economic Dynamics and Control 12 (1988), pp. 205– 
230. 
18 The subspace algorithm is quite complex and technical. The interested reader 
should consult the papers by Bauer and Wagner. 

545 
Multifactor Models and Common Trends for Common Stocks 
When testing for cointegration on a large set, one has therefore to take 
an ensemble view. In analyzing macroeconomic series, the question is 
whether they are cointegrated or not; in analyzing a large number of finan-
cial time series, the problem is not if there are cointegrating relationships 
but if the number of cointegrating relationships found in the sample is high 
enough to warrant the belief that the system has a cointegration structure. 
Another important issue—strictly related to the above—is the struc-
ture of cointegration. Cointegration can be found within highly cointe-
grated market segments (i.e., subsets of processes) that exhibit a high 
number of cointegrating relationships. Alternatively, cointegration can be 
found between market segments—perhaps on a different time scale. This 
cointegration structure will be reflected in the structure of common trends. 
These issues are presently inadequately addressed in the literature, 
although much proprietary empirical and analytical work has been done 
by some asset management firms. Studies of cointegration in financial 
processes has been performed at the level of indexes or broad aggre-
gates. Evidence of cointegration have been found between stock indexes 
in different countries and between different indexes in the same country. 
One of the most quoted studies on cointegration in equity prices is the 
1992 study by Kenneth Kasa.19 who found evidence of cointegration 
between stock indexes in five different countries. Using models with 
from 1 to 14 lags, Kasa found that the number of lags plays an impor-
tant role: Cointegration is revealed more clearly with many lags. In a 
critical review of this and other studies on cointegration on various 
assets, Godbout and van Norden20 concluded that the size of the sample 
might be responsible for significant distortions. 
Carol Alexander21 and coworkers at the ISMA Center in Reading, 
United Kingdom, found cointegration within small-size high-capitaliza-
tion liquid indexes such as the Dow Jones Industrial Average (DJIA). 
Their empirical findings corroborate the intuition that equity prices are 
in some way mean-reverting around one or more common stochastic 
trends. Alexander has developed trading strategies used for both index 
tracking and long-short equity portfolios based on replicating the first 
common factor of the market. 
19 Kenneth Kasa, “Common Stochastic Trends in International Stock Markets,” 
Journal of Monetary Economics 29 (1992), pp. 95–124. 
20 Marie-Josee Gobbout and Simon van Norden, “Reconsidering Cointegration in 
International Finance: Three Case Studies of Size Distortion in Finite Samples,” 
Working Paper 97-1, Bank of Canada, 1997. 
21 Carol Alexander and Anca Dimitriu, “The Cointegration Alpha: Enhanced Index 
Tracking and Long - Short Equity Market Neutral Strategies,” Working Paper, April 
2002. 

546 
The Mathematics of Financial Modeling and Investment Management 
Special cointegration models have been described in the literature. 
In particular, the well-documented lead-lag effect described by Andrew 
Lo and Craig MacKinlay22 leads to a cointegration model. The lead-lag 
effect is the strong correlation which exists between the returns at time t 
of portfolios of small firms, the laggards, and the return at time t – 1 of 
portfolios of large firms, the leaders. This effect can be tested either as 
direct correlation between returns or as autocorrelation of portfolios 
that include firms of different sizes. 
In the original formulation of Lo and MacKinlay, the model is sim-
ple as there is only one exogenous factor. Consider the returns of the 
two portfolios of large firms and small firms; the Lo and MacKinlay 
model is written as follows, with the return of small firms a regression 
on the lagged factor: 
rLt = µL + β1Lft + εLt 
rSt = µS + β1Sft +
+ εSt
β2Sft – 1 
Angelos Kanas and Georgios Kouretas23 have cast the lead-lag effect 
of size-sorted portfolios into a cointegration framework using state-space 
modeling in the form of ARDL models for prices. Summing up returns to 
get prices and solving, they arrive at the following ARDL equation: 
pSt = a
bt
 
+ βpLt – 1 + et
+ 
where e is an autocorrelated process that includes the single common 
factor. 
In summary, cointegration and/or state-space modeling are powerful 
modeling techniques whose applicability to real price processes has been 
empirically tested. However, the practical implementation of state-space 
models of large portfolios presents significant challenges given that 
cointegration is largely unstable. 
NONLINEAR DYNAMIC MODELS FOR PRICES AND RETURNS 
While the models for portfolio management discussed above are linear 
models, the linearity of equity price processes has been challenged by 
22 Andrew Lo and Craig MacKinlay, “When Are Contrarian Profits Due to Stock 
Market Overreaction?” Review of Financial Studies 3 (1990), pp. 175–206. 
23 Angelos Kanas and Georgios Kouretas, “A Cointegration Approach to the Lead-
Lag Effect Among Size-Sorted Equity Portfolios,” Working Paper, 2001 

547 
Multifactor Models and Common Trends for Common Stocks 
studies that appear to demonstrate that equity price processes are not 
linear in the sense that their DGP is a nonlinear function. Volatility clus-
tering and structural breaks are the most widely cited nonlinear effects. 
This lead to the development of nonlinear models for portfolio manage-
ment; nonlinear dynamics and universal approximation schemes for 
DGPs such as neural networks have been widely described. However, 
tests for low-dimensional nonlinear dynamics have not given consis-
tently positive results. Despite a period of intense experimentation dur-
ing the 1990s, the techniques of nonlinear dynamics have not been 
successful in describing price processes. 
Nevertheless, approximation schemes remain a subject of study and 
experimentation. Vector support machines based on the Vapnik-Cher-
vonenkis theory of learning (see Chapter 12) are one of the latest addi-
tions to a long series of adaptive methods. By their nature, adaptive 
methods produce nonlinear DGPs that change continuously. While gen-
eral conclusions are difficult, many experiments have confirmed that 
nonlinear approximation schemes have some predictive power—some 
trading strategies based on them have been profitable. However, most 
efforts are now confined to proprietary trading systems. 
Two classes of nonlinear methods that have received a lot of atten-
tion, at both the theoretical and practical levels, are (1) ARCH-GARCH 
methods and (2) Markov switching and multiplicative state-space meth-
ods. Both are based on splitting the model into two parts: one part is a 
linear regressive or autoregressive model, the other an autoregressive 
model that drives the first. 
The ARCH model (described in Chapter 12) was initially proposed 
to model the clustering of volatility. Its generalization, the GARCH fam-
ily of models, applies to processes such as financial time series that 
exhibit volatility clustering. The GARCH(m,q) model represents the 
observed process, for example equity returns, as a sequence of IID vari-
ables multiplied by a coefficient which obeys an ARMA(m,q) model as 
follows: 
rt = σtεt 
m
q 
2
2
σt = ∑αiσt
i + ∑βirt
j
–
– 
i = 1 
j = 1 
The GARCH(m,q) model can be further generalized to multivariate 
processes by modeling not only the process’s volatility but the entire 
variance-covariance matrix. In this form the model is known as multi-

548 
The Mathematics of Financial Modeling and Investment Management 
variate GARCH. Because multivariate GARCH becomes rapidly 
unmanageable with the number of assets, simplified forms have been 
proposed. 
GARCH models are not necessarily stationary insofar as their sta-
tionarity depends on the coefficients of the ARMA process. If the 
ARMA process is not stationary, then the process is called IGARCH. 
While ARCH and GARCH models model volatility, asset pricing 
models require that returns depend on volatility as higher volatility 
commands a higher return. To capture the dependence of returns on vol-
atility, Engle, Lilien, and Robins24 suggested adding an expected return 
term to the GARCH equations. Equations then become 
rt = µt + σtεt 
2 
µt = γ 0 + γ 1σt 
m
q 
2
2
σt = ∑αiσt
i + ∑βirt
j
–
– 
i = 1 
j = 1 
This model is called M-ARCH or ARCH in mean. Recall that M-ARCH 
is also a way to represent the conditional CAPM. 
While ARCH and GARCH models are based on empirical findings 
of volatility clustering, Markov-switching models are based on a gener-
alization of the idea that a model’s parameters cannot be considered sta-
ble for long periods of time. If our objective is to retain linear models as 
the basic DGP, then we have to accept that parameters will change in 
time. Markov switching models use a Markov chain to drive the param-
eters of a basic linear model. The Hamilton model, for example, uses a 
Markov chain to drive the parameters of a random walk. In a more gen-
eral Markov-switching VAR, a Markov chain drives the parameters of a 
VAR model. Continuous-state autoregressive models might replace 
Markov chains, thus originating multiplicative state-space models. 
ARCH and GARCH models follow this modeling strategy. 
If the objective is to model a large collection of price processes, for 
example the price processes in some broad index, then dimensionality 
reduction techniques must be applied. Envisage an outer driver, be it a 
Markov chain or an autoregressive model, that drives the parameters of 
24 R. Engle, D. Lilien, and R. Robins, “Estimating Time-Varying Risk Premia in the 
Term Structure: the ARCH-M Model,” Econometrica 55 (1987), pp. 391–407. 

549 
Multifactor Models and Common Trends for Common Stocks 
a state-space model. One thereby creates a dynamic model of the factors 
that drive a regressive model. As of this writing, however, the statistical 
properties of these models have not been thoroughly investigated. 
SUMMARY
 ■ Multifactor models are linear regressions over a number of variables 
called factors.
 ■ Factors can be exogenous variables or abstract variables formed by 
portfolios.
 ■ The Arbitrage Pricing Theory (APT) asserts that each asset’s return is 
equal to the risk-free rate plus a linear combination of factors.
 ■ The APT can be tested with maximum likelihood methods.
 ■ Exogenous factors can be determined with fundamental analysis.
 ■ Abstract factors can be determined with factor analysis or principal 
component analysis.
 ■ Principal component analysis identifies the largest eigenvalues of the 
variance-covariance matrix or the correlation matrix.
 ■ The largest eigenvalues correspond to eigenvectors that identify the 
entire market and sectors that correspond to industry classification.
 ■ Multifactor models allow the decomposition of risk into systematic 
risk and residual risk.
 ■ The most general formulation of the portfolio selection problem is util-
ity maximization in a multiperiod setting.
 ■ In a multiperiod setting, agents make a decision between consumption 
and investment at each date; the Consumption CAPM is obtained by 
aggregating all agents in a single representative agent and imposing 
consumption optimality conditions.
 ■ Factor models can be extended in a dynamic environment as state-
space models.
 ■ Error correction models and state-space models are equivalent.
 ■ Through cointegration and state space-models it is possible to repre-
sent large portfolios through dynamic factor models. 
■ There is empirical evidence of cointegration in stock prices.
 ■ Nonlinear models of stock prices have been proposed, ARCH/GARCH 
and Markov switching models being two examples. 


I 
CHAPTER 19 
Equity Portfolio Management 
n this chapter we review strategies for equity portfolios, taking a close 
look at active and passive management, the decision as to whether or not 
to pursue an active or passive management, style investing, and the differ-
ent types of active strategies that can be employed. We stress the role of 
multifactor risk models in the portfolio construction process. We begin the 
chapter with a discussion of the equity portfolio management process. 
INTEGRATING THE EQUITY PORTFOLIO MANAGEMENT PROCESS 
In Chapter 1, the investment management process was described as a 
series of five distinct steps. In practice, portfolio management requires 
an integrated approach. There must be recognition that superior invest-
ment performance results when valuable ideas are implemented in a 
cost-efficient manner. The process of investing—as opposed to the pro-
cess of investment—includes innovative stock selection and portfolio 
strategies as well as efficient cost structures for the implementation of 
any portfolio strategy.1 The integrated approach to managing equity 
portfolios recognizes that the value added by the manager is the result 
of information value less the implementation cost of trading. This dif-
ference in value is referred to as “captured value,” a term coined by 
Wayne Wagner and Mark Edwards.2 
1 Wayne H. Wagner and Mark Edwards, “Implementing Investment Strategies: The 
Art and Science of Investing,” Chapter 11 in Frank J. Fabozzi (ed.), Active Equity 
Portfolio Management (New Hope, PA: Frank J. Fabozzi Associates, 1998). 
2 Wagner and Edwards, “Implementing Investment Strategies: The Art and Science 
of Investing.” 
551 

552 
The Mathematics of Financial Modeling and Investment Management 
This view that an investing process requires an integrated approach 
to portfolio management is reinforced by Barra, a vendor of analytical 
systems used by portfolio managers. Barra emphasizes that superior 
investment performance is the product of careful attention paid by 
equity managers to the following four elements:
 ■ Forming reasonable return expectations
 ■ Controlling portfolio risk to demonstrate investment prudence
 ■ Controlling trading costs
 ■ Monitoring total investment performance 
Accordingly, the investing process that includes these four elements 
are all equally important in realizing superior investment performance. 
In Chapter 4, several quantitative models for general expected returns 
were described. As for the second element, we will discuss the process of 
controlling risk in this chapter and in more detail in Chapter 23. Trad-
ing costs were explained in Chapter 2. 
ACTIVE VERSUS PASSIVE PORTFOLIO MANAGEMENT 
In practice there are investors who pursue different degrees of active 
management and different degrees of passive management. It would be 
helpful to have some way of quantifying the degree of active or passive 
management. John Loftus of Pacific Investment Management Company 
(PIMCO) has suggested that one way of classifying the various types of 
equity strategies is in terms of two measures—alpha and tracking error.3 
These measures begin with the calculation of the active return for a 
period. The active return is the difference between the actual portfolio 
return for a given period (say, a month) and the benchmark index return 
for the same period. Alpha is defined as the average active return over 
some time period. So, if there are 12 monthly active returns observed, 
then the average of the 12 monthly active returns is the alpha. Tracking 
error is the standard deviation of the active return. In the next section, 
we discuss tracking error in more detail. Tracking error occurs because 
the risk profile of a portfolio differs from that of the risk profile of the 
benchmark index. 
Based on these measures, Loftus proposes the classification scheme 
shown in Exhibit 19.1. While there may be disagreements as to the values 
3 John S. Loftus, “Enhanced Equity Indexing,” Chapter 4 in Frank J. Fabozzi (ed.), 
Perspectives on Equity Indexing (New Hope, PA: Frank J. Fabozzi Associates, 
2000). 

Equity Portfolio Management 
553 
EXHIBIT 19.1 
Measures of Management Categories 
Indexing 
Active Management 
Enhanced Indexing 
Expected alpha 
0% 
2.0% or higher 
0.5% to 2.0% 
Tracking error 
0% to 0.2% 
4.0% or higher 
0.5% to 2.0% 
Source: Exhibit 2 in John S. Loftus, “Enhanced Equity Indexing,” Chapter 4 in 
Frank J. Fabozzi (ed.), Perspectives on Equity Indexing (New Hope, PA: Frank J. 
Fabozzi Associates, 2000), p. 84. 
proposed by Loftus, the exhibit does provide some guidance. In an 
indexing strategy, the portfolio manager seeks to construct a portfolio 
that matches the risk profile of the benchmark index, the expected alpha 
is zero and, except for transaction costs and other technical issues dis-
cussed later when we cover the topic of indexing, the tracking error 
should be, in theory, zero. Due to these other issues, tracking error will 
be a small positive value. At the other extreme, a manager who pursues 
an active strategy by constructing a portfolio that significantly differs 
from the risk profile of the benchmark portfolio has an expected alpha 
of more than 2% and a large tracking error—a tracking error of 4% or 
higher. 
Using tracking error as our guide and the fact that a manager can 
construct a portfolio whose risk profile can differ to any degree from the 
risk profile of the benchmark index, we have a conceptual framework 
for understanding common stock portfolio management strategies. For 
example, there are managers that will construct a portfolio with a risk 
profile close to that of the benchmark index but intentionally not identi-
cal to it. Such a strategy is called enhanced indexing. This strategy will 
result in the construction of a portfolio that has greater tracking error 
relative to an indexing strategy. In the classification scheme proposed by 
Loftus, for an enhanced indexer the expected alpha does not exceed 2% 
and the tracking error is 0.5% to 2%. 
TRACKING ERROR 
When a portfolio manager’s benchmark is a market index, risk is mea-
sured by the standard deviation of the return of the portfolio relative to 
the return of the benchmark. This risk measure is called tracking error 
and is computed as follows:
 ■ Step 1. Compute the total return for a portfolio for each period.
 ■ Step 2. Obtain the total return for the benchmark for each period. 

554 
The Mathematics of Financial Modeling and Investment Management
 ■ Step 3. Obtain the difference between the values found in Step 1 and 
Step 2. The difference is referred to as the active return.
 ■ Step 4. Compute the standard deviation of the active returns. The 
resulting value is the tracking error. 
The tracking error measurement is in terms of the observation 
period. So, if monthly returns are used, the tracking error is a monthly 
tracking error. Typically, tracking error is computed using either weekly 
or monthly data. Tracking error is annualized as follows: 
Annual tracking error = Monthly tracking error × 
f 
where f is 12 for monthly observations or 52 for weekly observations. 
A portfolio created to match the benchmark index (i.e., an index 
fund) that regularly has zero active returns (that is, always matches its 
benchmark’s actual return) would have a tracking error of zero. But a 
portfolio that is actively managed that takes positions substantially dif-
ferent from the benchmark would likely have large active returns, both 
positive and negative, and thus would have an annual tracking error of, 
say, 5% to 10%. A hybrid portfolio (e.g., enhanced index fund) that 
combines an index portfolio with an active portfolio would typically 
have a tracking error below 2%. 
An enhanced index portfolio’s is simply a combination of an 
indexed portfolio and an active portfolio. That is, the tracking error of 
the enhanced index portfolio is simply the tracking error of the active 
portion times its weight in the overall portfolio. For example, if the 
active portion constitutes 10% of the enhanced index fund (the other 
90% being indexed), and the tracking error of the active portion is 5%, 
then the tracking error of the enhanced index fund is 0.5% (= 10% × 
5%). To see this, let r = return, w = weight, σ2 (.) = variance, and ρ(.,.) = 
correlation. Using the following notation for subscripts, b = benchmark, 
I = indexed portfolio, a = active portfolio, p = enhanced index portfolio 
(a combination of the indexed portfolio and the active portfolio), then 
r = wi ri + wara
p 
since wi + wa = 1, 
rp – rb = wi (ri – rb) + wa (ra – rb) 
So, the tracking error variance of the enhanced index portfolio equals 

555 
Equity Portfolio Management 
σ2(rp – rb) = σ2{wi(ri – rb)} + σ2{w (r – rb)}
a
a 
+ 2wiw ρ(ri – rb, r – rb)σ(ri – rb)σ(r – rb)
a
a 
a 
But, the variance and the standard deviation of the indexed portfo-
lio relative to the benchmark would be zero. So, the first and the last 
terms in the above equation vanish, leaving. 
σ2(rp – rb) = σ2{wa (ra – rb)} 
Taking the square root on both sides, we have 
σ(rp – rb) = σ(wa(ra – rb)) 
Since, σ(wa(ra – rb)) is the tracking error of the active portion, the track-
ing error of the enhanced index portfolio is the product of weight of the 
active portfolio and the tracking error of the active portfolio. 
Backward-Looking versus Forward-Looking Tracking Error 
We have just described how to calculate tracking error based on the 
actual active returns observed for a portfolio. Calculations computed 
for a portfolio based on a portfolio’s actual active returns reflect the 
portfolio manager’s decisions during the observation period with 
respect to the factors that affect tracking error. We call tracking error 
calculated from observed active returns for a portfolio backward-looking 
tracking error, ex post tracking error, or actual tracking error. 
A problem with using backward-looking tracking error in portfolio 
management is that it does not reflect the effect of current decisions by 
the portfolio manager on the future active returns and hence the future 
tracking error that may be realized. If, for example, the manager signifi-
cantly changes the portfolio’s exposure to risk factors during the obser-
vation period, then the backward-looking tracking error, which is 
calculated using data from prior periods would not accurately reflect the 
current portfolio risks going forward. That is, the backward-looking 
tracking error will have little predictive value and can be misleading 
regarding portfolio risks going forward. 
The portfolio manager needs a forward-looking estimate of tracking 
error to reflect the portfolio risk going forward. The way this is done in 
practice is by constructing a multifactor risk model using as the market 
index the portfolio manager’s benchmark. Given a manager’s current 
portfolio holdings, the portfolio’s current exposure to the various risk 
factors can be calculated and compared to the benchmark’s exposures to 

556 
The Mathematics of Financial Modeling and Investment Management 
the factors. Using the differential factor exposures and the risks of the 
factors, a forward-looking tracking error for the portfolio can be com-
puted. This tracking error is also referred to as predicted tracking error 
and ex ante tracking error. Given a forward-looking tracking error, a 
range for the future possible portfolio active return can be calculated 
assuming that the active returns are normally distributed. 
It should be noted that there is no guarantee that the forward-look-
ing tracking error at the start of, say, a year would exactly match the 
backward-looking tracking error calculated at the end of the year. There 
are two reasons for this. The first is that as the year progresses and 
changes are made to the composition of the portfolio, the forward-look-
ing tracking error estimate would change to reflect the new exposure to 
risk factors. The second is that the accuracy of the forward-looking 
tracking error at the beginning of the year depends on the extent of the 
stability in the variances and correlations used in the statistical model to 
estimate forward-looking tracking error. These problems notwithstand-
ing, the average of forward looking tracking error estimates obtained at 
different times during the year will be reasonably close to the backward-
looking tracking error estimate obtained at the end of the year. 
The forward-looking tracking error is a useful in risk control and 
portfolio construction. The manager can immediately see the likely 
effect on tracking error of any intended change in the portfolio. Thus, 
scenario analysis can be performed by a portfolio manager to assess 
proposed portfolio strategies and eliminate those that would result in 
tracking error beyond a specified tolerance for risk. We will illustrate 
the use of multifactor risk models and tracking error later in this chap-
ter and in bond portfolio management in Chapter 21. 
The Impact of Portfolio Size, Benchmark Volatility, and Portfolio 
Beta on Tracking Error4 
There are have been several empirical studies that have investigated the 
relationship between a portfolio’s variance and number of stocks. These 
studies have found that between 15–20 names are needed to eliminate 
most of the unsystematic risk in a portfolio. These studies focus on the 
standard deviation of returns of a portfolio relative to a benchmark, not 
on tracking error. 
Tracking error decreases as the portfolio progressively includes 
more of the stocks that are in the benchmark index. This effect is illus-
trated in Exhibit 19.2 which shows the effect of portfolio size for a large 
4 This discussion draws from Raman Vardharaj, Frank J. Fabozzi, and Frank J. 
Jones, “Determinants of Tracking Errors for Equity Portfolios,” unpublished manu-
script, October 2003. 

557 
Equity Portfolio Management 
EXHIBIT 19.2 
Tracking Error versus the Number of Benchmark Stocks in the 
Portfolio 
Source: Exhibit 7.2 in Raman Vardharaj, Frank J. Jones, and Frank J. Fabozzi, 
“Tracking Error and Common Stock Portfolio Management,” Chapter 7 in Frank 
J. Fabozzi and Harry M. Markowitz (eds.), The Theory and Practice of Invest-
ment Management (New York: John Wiley & Sons, Inc., 2002), p. 171. 

558 
The Mathematics of Financial Modeling and Investment Management 
capitalization portfolio benchmarked to the S&P 500, a mid-cap portfo-
lio benchmarked to the S&P 400, and a small cap portfolio bench-
marked to the S&P 600.5 Notice that an optimally chosen portfolio of 
just 50 stocks can track the S&P 500 within 2.3%. For mid cap and 
small cap stocks, the corresponding tracking errors are 3.5% and 4.3%, 
respectively. In contrast, tracking error increases as the portfolio pro-
gressively includes more stocks that are not in the benchmark. This 
effect is illustrated in Exhibit 19.3. In this case, the benchmark index is 
the S&P 100 and the portfolio progressively includes more and more 
stocks from the S&P 500 that are not in S&P 100. The result is that the 
tracking error with respect to the S&P 100 rises. 
The impact of benchmark volatility is as follows. Managed portfo-
lios generally hold only a fraction of the assets in their benchmark. 
Given this, a highly volatile benchmark index (as measured in terms of 
standard deviation) would be harder to track closely than a generally 
less volatile benchmark index. 
This can be seen by using the market model: 
rp = βrm + e 
EXHIBIT 19.3 
Tracking Error versus the Number of Nonbenchmark Stocks in the 
Portfolio 
Source: Exhibit 7.3 in Raman Vardharaj, Frank J. Jones, and Frank J. Fabozzi, 
“Tracking Error and Common Stock Portfolio Management,” Chapter 7 in Frank 
J. Fabozzi and Harry M. Markowitz (eds.), The Theory and Practice of Invest-
ment Management (New York: John Wiley & Sons, Inc., 2002), p. 171. 
5 The tracking errors for the various portfolios were obtained from Barra Aegis soft-
ware. These are forward-looking tracking errors rather than backward-looking track-
ing errors. Also, the portfolios were optimally constructed to minimize tracking error. 

559 
Equity Portfolio Management 
where 
r
= return of the portfolio in excess of the constant risk-free rate
p 
rm = return of the market index in excess of the constant risk-free rate 
e 
= residual error term 
β 
= beta of the portfolio 
Subtracting market excess return (i.e., rm) from both sides, we get 
ra = rp – rm = (β – 1)rm + e 
where ra is the active return. Therefore, 
σ2(rp – rm) = (β – 1)2σ2(rm) + σ2(e) 
There would be no correlation between rm and the error term due to 
the regression. The left hand side of the above equation is the portfolio 
tracking error variance. So, we have 
σ(rp – rm) = (β – 1)σ(rm) 
As can be seen from the above equation, holding other things equal, 
tracking error increases with market volatility. 
To quantify the relationship between portfolio beta and tracking 
error, look again at the formula for the tracking error from the market 
model given above. Let w = weight of the portfolio invested in the 
benchmark index; (1 – w) = weight of the portfolio invested in cash; rp = 
portfolio return in excess of the risk-free return on cash, and; rb  = 
benchmark index return in excess of the risk-free return on cash. 
Because the excess return on cash is zero, we know that 
r  = wrb + (1 – w) 0 = wrb
p
If β is the portfolio beta versus the benchmark index, then letting 
σ(.,.) denote the covariance, 
β = σ(rp,rb)/σ2(rb) = wσ2(rb)/σ2(rb) = w 
Next we know that, rp – rb = (w – 1)rb = (β – 1)rb 
σ2(rp – rb) = (w – 1)2σ2(rb) = (β – 1)2σ2(rb) 

560 
The Mathematics of Financial Modeling and Investment Management 
Taking square root on both sides and denoting |.| as absolute value, we 
see the following relationship between tracking error and portfolio beta: 
σ(rp – rb) = w – 1 σ(
) = β – 1 σ(
)
rb
rb
Portfolio tracking error with respect to the benchmark index 
increases when both the beta falls below 1 and when the beta rises 
above 1. The same is true of the weight of the portfolio in the bench-
mark index. So, as portfolio increases the proportion of cash held, even 
though its absolute risk falls, its tracking error (i.e., relative risk) rises. 
In the above example, we make the simplistic assumption that the 
manager only chooses between holding the market portfolio and cash 
when making changes to its beta. In the more general case, where the man-
ager can hold any number of stocks in any proportion, its beta can differ 
from 1 due to other reasons. But, even in this general case, the tracking 
error increases when the portfolio beta deviates from the market beta. 
EQUITY STYLE MANAGEMENT 
Before we discuss the various types of active and passive strategies, let’s 
discuss an important topic regarding what has come to be known as 
equity investment styles. Several academic studies found that there were 
categories of stocks that had similar characteristics and performance 
patterns. Moreover, the returns of these stock categories performed dif-
ferently than other categories of stocks. That is, the returns of stocks 
within a category were highly correlated and the returns between cate-
gories of stocks were relatively uncorrelated. As a result of these studies, 
practitioners began to view these categories of stocks with similar per-
formance as a “style” of investing. Using size as a basis for categorizing 
style, some managers became “large cap” investors while others “small 
cap” investors. (“Cap” means market capitalization.) Moreover, there 
was a commonly held belief that a manager could shift “styles” to 
enhance performance return. 
Today, the notion of an equity investment style is widely accepted in 
the investment community. Next we look at the popular equity style 
types and the difficulties of classifying stocks according to style. 
Types of Equity Styles 
Stocks can be classified by style in many ways. The most common is in 
terms of one or more measures of “growth” and “value.” Within a 
growth and value style there is often a substyle based on some measure 

561 
Equity Portfolio Management 
of size. The motivation for the value/growth style categories can be 
explained in terms of the most common measure for classifying stocks 
as growth or value—the price-to-book value per share (P/B) ratio. Earn-
ings growth will increase the book value per share. Assuming no change 
in the P/B ratio, a stock’s price will increase if earnings grow—as higher 
book value times a constant P/B ratio leads to higher stock price. A 
manager who is growth oriented is concerned with earnings growth and 
seeks those stocks from a universe of stocks that have higher relative 
earnings growth. The growth manager’s risks are that growth in earn-
ings will not materialize and/or that the P/B ratio will decline. 
For a value manager, concern is with the price component rather 
than with the future earnings growth. Stocks would be classified as 
value stocks within a universe of stocks if they are viewed as cheap in 
terms of their P/B ratio. By cheap it is meant that the P/B ratio is low rel-
ative to the universe of stocks. The expectation of the manager who fol-
lows a value style is that the P/B ratio will return to some normal level 
and thus even with book value per share constant, the price will rise. 
The risk is that the P/B ratio will not increase. 
Within the value and growth categories there are substyles. With the 
notion of style investing came stock market indexes that could be used 
to represent different styles. There are three major services that provide 
popular style indexes based on capitalization. Standard & Poor’s 
together with Barra publishes cap-based growth and value indexes 
based on three S&P indexes: the S&P 500 Index (also called the S&P 
Composite Index), the Mid Cap 400 Index, and the Small Cap 600 
indexes. Based on its Russell 1000, Russell 3000, and Russell Top 200, 
Frank Russell publishes three large cap style indexes. It also produces a 
mid-cap index and a small cap based on both the Russell 2000 and Rus-
sell 2500 indexes. A large, mid-, and small cap set of indexes is also pro-
duced by Wilshire Associates. 
From the statistical point of view identifying styles means classify-
ing stocks. Classification is a broad topic in statistics. Classification 
used for style analysis is typically unsupervised insofar as no given 
example is needed. The simplest unsupervised technique is linear dis-
criminant analysis. If stocks are characterized by a number of attributes, 
linear discriminant analysis tries to find a hyperplane that discriminates 
between two groups. Consider, for instance “value” and “growth.” 
Each stock is characterized by a pair of value and growth numbers. 
Therefore, all stocks can be visualized as a set of points in the value-
growth plane. Discriminant analysis tries to find the straight line that 
cuts that set in two subsets in some optimal way. Criteria for optimal 
cutting are needed. Nonlinear discriminant analysis might use nonlinear 
functions as discriminant. 

562 
The Mathematics of Financial Modeling and Investment Management 
Discriminant analysis divides a set into two parts. However, one might 
want to classify stocks in several groups. In this case, the problem is one of 
clustering. Clustering means forming groups so that objects in each group 
are similar while objects in different groups are dissimilar. For instance, 
classification in several different styles is an example of clustering. To per-
form clustering one needs a distance function that gives the distance 
between any two objects. Clustering will find groups, i.e., clusters, that 
have the minimum possible distance. A popular way of classifying stocks is 
through hierarchical clustering based on correlation distance.6 
Style Classification Systems 
Now that we have a general idea of the two main style categories, growth 
and value, and the further refinement by size, let’s see how a portfolio man-
ager goes about classifying stocks that fall into the categories. We call the 
methodology for classifying stocks into style categories as a style classifica-
tion system. Vendors of style indices have provided direction for developing a 
style classification system. However, managers will develop their own system. 
Developing such a system is not a simple task. To see why, let’s take 
a simple style classification system where we just categorize stocks into 
value and growth using one measure, the price-to-book value ratio. The 
lower the P/B ratio the more the stock looks like a value stock. The style 
classification system would then be as follows:
 ■ Step 1. Select a universe of stocks.
 ■ Step 2. Calculate the total market capitalization of all the stocks in the 
universe.
 ■ Step 3. Calculate the P/B ratio for each stock in the universe.
 ■ Step 4. Sort the stocks from the lowest P/B ratio to the highest P/B 
ratio.
 ■ Step 5. Calculate the accumulated market capitalization starting from 
the lowest P/B ratio stock to the highest P/B ratio stock.
 ■ Step 6. Select the lowest P/B stocks up to the point where one-half the 
total market capitalization computed in Step 2 is found.
 ■ Step 7. Classify the stocks found in Step 6 as value stocks.
 ■ Step 8. Classify the remaining stocks from the universe as growth 
stocks. 
While this style classification system is simple, it has both theoreti-
cal and practical problems. First, from a theoretical point of view, in 
6 Clustering is broad topic. An excellent reference is Richard O. Duda, Peter E. 
Heart, and David G. Stork, Pattern Classification (New York: John Wiley & Sons, 
2001). 

563 
Equity Portfolio Management 
terms of the P/B ratio there is very little distinguishing the last stock on 
the list that is classified as value and the first stock on the list classified 
as growth. From a practical point of view, the transaction costs are 
higher for implementing a style using this classification system. The rea-
son is that the classification is at a given point in time based on the pre-
vailing P/B ratio and market capitalizations. At a future date, P/B ratios 
and market capitalizations will change, resulting in a different classifica-
tion of some of the stocks. This is often the case for those stocks on the 
border between value and growth that could jump over to the other cat-
egory. This is sometimes called “style jitter.” As a result, the manager 
will have to rebalance the portfolio to sell off stocks that are not within 
the style classification sought. 
There are two refinements that have been made to style classifica-
tion systems in an attempt to overcome these two problems. First, more 
than one categorization variable has been used in a style classification 
system. Categorization variables that have been used based on historical 
and/or expectational data include dividend/price ratio (i.e., dividend 
yield), cash flow/price ratio (i.e., cash flow yield), return on equity, and 
earnings variability, and earnings growth. As an example of this refine-
ment, consider the style classification system developed by one firm, 
Frank Russell, for the Frank Russell style indices. The universe of stocks 
included (either 1,000 for the Russell 1000 index or 2,000 for the Rus-
sell 2000 index) were classified as part of their value index or growth 
index using two categorization variables. The two variables are the B/P 
ratio and a long-term growth forecast of earnings.7 
The second refinement has been to develop better procedures for mak-
ing the cut between growth and value. This involves not classifying every 
stock into one category or the other. Instead, stocks may be classified into 
three groups: “pure value,” “pure growth,” and “middle-of-the-road” 
stocks. The three groups would be such that they each had one third of the 
total market capitalization. The two extreme groups, pure value and pure 
growth, are not likely to face any significant style jitter. The middle-of-the 
road stocks are assigned a probability of being value or growth. 
Thus far our focus has been on style classification in terms of value 
and growth. As we noted earlier, substyle classifications are possible in 
terms of size. Within a value and growth classification, there can be a 
model determining large value and small value stocks, and large growth 
and small growth stocks. The variable most used for classification of 
size is a company’s market capitalization. To determine large and small, 
the total market capitalization of all the stocks in the universe consid-
7 “Russell Equity Indices: Index Construction and Methodology,” Frank Russell 
Company, July 8, 1994 and September 6, 1995. 

564 
The Mathematics of Financial Modeling and Investment Management 
ered is first calculated. The cutoff between large and small is the stock 
that will give an equal market capitalization. Even here though, one 
might worry about “size jitter.” 
PASSIVE STRATEGIES 
There are two types of passive strategies: a buy-and-hold strategy and 
an indexing strategy. In a buy-and-hold strategy, a portfolio of stocks 
based on some criterion is purchased and held to the end of some invest-
ment horizon. There is no active buying and selling of stocks once the 
portfolio is created. While referred to as a passive strategy, there are ele-
ments of active management. Specifically, the investor who pursues this 
strategy must determine which stock issues to buy. 
An indexing strategy is the more commonly followed passive strat-
egy. With this strategy, the manager does not attempt to identify under-
valued or overvalued stock issues based on fundamental security 
analysis. Nor does the manager attempt to forecast general movements 
in the stock market and then structure the portfolio so as to take advan-
tage of those movements. Instead, an indexing strategy involves design-
ing a portfolio to track the total return performance of a benchmark 
index. Next we explain how that is done. 
Constructing an Indexed Portfolio 
In constructing a portfolio to replicate the performance of the bench-
mark index, sometimes referred to as the indexed portfolio or the track-
ing portfolio, there are several approaches that can be used. One 
approach is to purchase all stock issues included in the benchmark 
index in proportion to their weightings. A second approach, referred to 
as the capitalization approach, is one in which the manager purchases a 
number of the largest capitalized names in the benchmark index and 
equally distributes the residual stock weighting across the other issues in 
the benchmark index. For example, if the top 150 highest-capitalization 
stock issues are selected for the replicating portfolio and these issues 
account for 70% of the total capitalization of the benchmark index, the 
remaining 30% is evenly proportioned among the other stock issues. 
Another approach is to construct an indexed portfolio with fewer 
stock issues than the benchmark index. Two methods used to implement 
this approach are the cellular (or stratified sampling) method and the 
multifactor risk model method. 
In the cellular method, the manager begins by defining risk factors 
by which the stocks that make up a benchmark index can be catego-

565 
Equity Portfolio Management 
rized. A typical risk factor is the industry in which a company operates. 
Other factors might include risk characteristics such as beta or capitali-
zation. The use of two characteristics would add a second dimension to 
the stratification. In the case of the industry categorization, each com-
pany in the benchmark index is assigned to an industry. This means that 
the companies in the benchmark have been stratified by industry. The 
objective of this method is then to reduce residual risk by diversifying 
across all industries in the same proportion as the benchmark index. 
Stock issues within each cell or stratum, or in this case industry, can 
then be selected randomly or by some other criterion such as capitaliza-
tion ranking. 
The second method is using a multifactor risk model to construct a 
portfolio that matches the risk profile of the benchmark index. By doing 
so, a predicted tracking error close to zero can be obtained. In the case 
of smaller portfolios, this approach is ideal since the manager can assess 
the tradeoff of including more stock issues versus the higher transaction 
costs for constructing the indexed portfolio. This can be measured in 
terms of the effect on predicted tracking error. 
Index Tracking and Cointegration 
As seen earlier in this chapter, using tools such as multifactor models, 
index trackers try to replicate the returns of the index. This methodology 
has the advantage of being in line with classical methods of portfolio 
management. In fact, it can be easily cast in the mean-variance frame-
work. However, it has the disadvantage that errors grow in time. In fact, 
tracking error is assumed to grow with the square root of time. However, 
if the tracking portfolio is cointegrated with the index, errors are station-
ary. In this case, a time dependent tracking error is suboptimal. 
The techniques of cointegration are clearly important for index 
tracking. Its use in index tracking was pioneered by Carol Alexander at 
the ISMA Centre in Reading, United Kingdom. In fact, because cointe-
gration allows a manager to specify a stationary tracking error and, 
therefore, an optimal global index tracking methodology, the techniques 
of cointegration can be applied to any portfolio that is strongly cointe-
grated with an index. 
The key challenge of cointegration methods is to find the right coin-
tegrating portfolio. This is a difficult task when working with large port-
folios. As mentioned above, standard cointegration tests do not work for 
large portfolios. One possible solution is the use economic consider-
ations that might suggest the choice of particular market segments which 
can be tested for cointegration in aggregate. A more abstract approach is 
to use state-space models to find meaningful common factors. 

566 
The Mathematics of Financial Modeling and Investment Management 
ACTIVE INVESTING 
In contrast with passive investing, active investing makes sense when a 
moderate to low degree of capital market efficiency is present in the 
financial markets (or areas thereof). This happens when the active inves-
tor has (1) better information than most other investors (namely, the 
“consensus” investors); and/or (2) the investor has a more productive 
way of looking at a given information set to generate active rewards. 
In general, active strategies can be classified as either a top-down 
approach or a bottom-up approach. We discuss each approach below. 
Top-Down Approaches to Active Investing 
Before delving into the “top-down” active approach to investing, we must 
first reflect on the different connotations of top-down investing. In princi-
ple, one can distinguish between three types of top-down investing—one of 
which is passive, while two are active. We’ll first explain the top-down pas-
sive connotation. Specifically, we know that modern portfolio theory 
emphasizes that investors should hold efficient portfolios. As we explained 
in Chapter 16, an efficient portfolio is one that maximizes expected return 
for any given level of expected risk. The MPT framework can in turn be 
viewed as a top-down passive approach to investing because an investor is 
only concerned with portfolio choices—albeit efficient ones at that—rather 
than stock selection choices by company, industry, and even market sector. 
Indeed, the top-down maximization of expected portfolio return for a 
given risk level occurs without any direct interest by the investor in the 
specific names of companies that comprise the efficient portfolio—other 
than to say that an individual company, industry, or sector has the poten-
tial to enhance portfolio return and reduce risk through efficient diversifi-
cation. Since an efficient portfolio—such as the market portfolio—is a 
passively constructed portfolio, one must therefore be careful to distin-
guish between top-down passive investing and top-down active investing. 
Given the amount of the portfolio’s funds to be allocated to the 
equity market, the manager must then decide how much to allocate 
among the sectors and industries of the equity market. In making the 
active asset allocation decision, a manager who follows a macroeco-
nomic approach to top-down investing often relies on an analysis of the 
equity market to identify those sectors and industries that will benefit the 
most on a relative basis from the anticipated economic forecast. Once 
the amount to be allocated to each sector and industry is made, the man-
ager then looks for the individual stocks to include in the portfolio. The 
top-down approach looks at changes in several macroeconomic factors 
to assess the expected active return on securities and portfolios. As noted 

567 
Equity Portfolio Management 
before, prominent economic variables include changes in commodity 
prices, interest rates, inflation, and economic productivity. 
Additionally, the macroeconomic outlook approach to top-down 
investing can be both quantitative and qualitative in nature. From the 
former perspective, equity managers employ factor models in their top-
down attempt at generating abnormal returns (i.e., positive alpha). The 
power of top-down factor models is that given the macroeconomic risk 
measures and factor sensitivities, a portfolio’s risk exposure profile can be 
quantified and controlled. In this way, it is possible to see why a portfolio 
is likely to generate abnormally high or low returns in the marketplace. 
Bottom-Up Approaches to Active Investing 
The “bottom-up” approach to active investing makes sense when 
numerous pricing inefficiencies exist in the capital markets (or compo-
nents thereof). An investor who follows a bottom-up approach to 
investing focuses either on (1) technical aspects of the market or (2) the 
economic and financial analysis of individual companies, giving rela-
tively less weight to the significance of economic and market cycles. 
The investor who pursues a bottom-up strategy based on certain 
technical aspects of the market is said to be basing stock selection on 
technical analysis. The primary research tool used for investing based 
on economic and financial analysis of companies is called security anal-
ysis and falls into two categories, traditional fundamental analysis and 
quantitative fundamental analysis. 
Traditional fundamental analysis often begins with the financial state-
ments of a company in order to investigate its revenue, earnings, and cash 
flow prospects, as well as its overall corporate debt burden.8 Growth in 
revenue, earnings, and cash flow on the income statement side and the rel-
ative magnitude of corporate leverage from current and anticipated bal-
ance sheets are frequently used by fundamental equity analysts in forming 
an opinion of the investment merits of a particular company’s stock. 
Specifically, the fundamental analyst attempts to determine the fair 
market value (or the “intrinsic value”) of the stock, using, for example, 
a price-to-earnings or price-to-book value multiplier. The estimated 
“fair value” of the firm is then compared to the actual market price to 
see if the stock is correctly priced in the capital market. “Cheap stocks,” 
or potential buy opportunities, have a current market price below the 
8 Benjamin Graham and David Dodd developed the classical approach to equity se-
curities analysis. Their approach is explained in Security Analysis (New York: 
McGraw-Hill, 1934). Notable investors who have successfully employed the tradi-
tional approach to equity security analysis include Warren Buffet of Berkshire Hath-
away, Inc. and Peter Lynch of Fidelity Management & Research Co. 

568 
The Mathematics of Financial Modeling and Investment Management 
estimated intrinsic value, while “expensive” or overvalued stocks have a 
market price that exceeds the calculated present worth of the stock. 
Quantitative fundamental analysis seeks to assess the value of secu-
rities using a statistical model derived from historical information about 
security returns. The most commonly used model is the fundamental 
multifactor risk model that we will explain later in this chapter. In addi-
tion to identifying the expected return for a security, a fundamental fac-
tor model can be used to construct a portfolio or rebalance a portfolio 
as demonstrated later in this chapter. 
Bruce Jacobs and Kenneth Levy refer to strategies that employ quan-
titative methods to select stocks and to construct portfolios that have the 
same risk profile as a benchmark index but provide the opportunity to 
enhance returns relative to that benchmark index at appropriate incre-
mental level as an “engineered approach” to portfolio management. 
Fundamental Law of Active Management 
The information ratio is the ratio of alpha to the tracking error. It is a 
reward (as measured by alpha) to risk (as measured by tracking error) 
ratio. The higher the information ratio, the better the performance of 
the manager. Two portfolio managers, Richard Grinold and Ronald 
Kahn, have developed a framework—which they refer to as the “funda-
mental law of active management”—for explaining how the informa-
tion ratio changes as a function of:9 
1. The depth of an active manager’s skill 
2. The breadth or number of independent insights or investment opportu-
nities. 
In formal terms, the information ratio can be expressed as 
IR = IC × BR 0.5 
where: 
IR = the information ratio 
IC = the information coefficient 
BR = the number of independent insights or opportunities available 
to the active manager 
In the above expression, the information ratio (IR) is the reward-to-
risk ratio for an active portfolio manager. In turn, the information coef-
9 For a practical discussion of this active management “law,” see Ronald N. Kahn, 
“The Fundamental Law of Active Management,” BARRA Newsletter (Winter 1997). 

569 
Equity Portfolio Management 
ficient (IC) is a measure of the depth of an active manager’s skill. On a 
more formal basis, IC measures the “correlation” between actual 
returns and those predicted by the portfolio manager. According to the 
fundamental law of active management, the information ratio also 
depends on breadth (BR), which reflects the number of creative insights 
or active investment opportunities available to the investment manager. 
There are several interesting implications of the fundamental law of 
active management. First, we see that the information ratio goes up when 
manager skill level rises for a given number of independent insights or 
active opportunities. This fact should be obvious, as a more skillful man-
ager should produce higher risk-adjusted returns, compared with a less 
skilled manager whose performance is evaluated over the same set of 
investment opportunities (possibly securities). Second, a prolific manager 
with a large number of independent insights for a given skill level can, in 
principle, produce a higher information ratio than a manager with the 
same skill but a limited number of investment opportunities. 
Equally important, the fundamental law of active management sug-
gests that a manager with a high skill level, but a limited set of opportu-
nities, may end up producing the same information ratio as a manager 
having a relatively lower level of skill but more active opportunities. 
According to Ronald Kahn,10 a market timer with an uncanny ability to 
predict the market may end up earning the same information ratio on 
the average as a somewhat less skillful stock picker. This might happen 
because the stock picker has numerous potentially mispriced securities 
to evaluate, while the otherwise successful market timer may be con-
strained by the number of realistic market forecasts per year (due, per-
haps, to quarterly forecasting or macroeconomic data limitations). 
Thus, the ability to profitably evaluate an investment opportunity (skill) 
and the number of independent insights (breadth) is key to successful 
active management. 
With an understanding of the fundamental law of active manage-
ment, we can now look at the risk of failing to produce a given level of 
active portfolio return. In this context, Bruce Jacobs and Kenneth Levy 
suggest that even traditional equity managers face a portfolio manage-
ment dilemma involving a trade-off between the depth, or “goodness,” 
of their equity management insights and the breadth or scope of their 
equity management ideas.11 According to Jacobs and Levy, the breadth 
of active research conducted by equity managers is constrained in prac-
tical terms by the number of investment ideas (or securities) that can be 
10 See Kahn, “The Fundamental Law of Active Management.” 
11 Jacobs and Levy, “Investment Management: An Architecture for the Equity Mar -
ket.” 

570 
The Mathematics of Financial Modeling and Investment Management 
implemented (researched) in a timely and cost-efficient manner. This 
trade-off is shown in Exhibit 19.4. 
The exhibit displays the relationship between the depth of equity man-
ager insights (vertical axis) and the breadth of those insights (horizontal 
axis). The depth of equity manager insights is measured in formal terms by 
the information coefficient (IC, on the vertical axis), while the breadth 
(BR) of manager insights can be measured by the potential number of 
investment ideas or the number of securities in the manager’s acceptable 
universe. When the breadth of equity manager insights is low—as in the 
case of traditional equity management, according to Jacobs and Levy— 
then the depth, or “goodness” of each insight needs to be high in order to 
produce a constant level of active reward-to-active risk (information ratio, 
IR). Exhibit 19.4 shows that this low breadth/high depth combination 
produces the same level of active reward that would be associated with a 
pair-wise high number of investable ideas (or securities) and a relatively 
low level of equity manager “goodness” or depth per insight. 
In a risk management context, one can say that the probability of fail-
ure to achieve a given level of active reward is quite high when the breadth 
of investment ideas or securities to be analyzed is very low. If the market is 
price efficient, that scenario is likely in the traditional fundamental analysis 
approach to active equity management discussed earlier. On the other 
hand, the risk of not achieving a given level of active reward is low when 
EXHIBIT 19.4 
Combination of Breadth (Number) of Insights and Depth, or 
“Goodness,” of Insights Needed to Produce a Given Investment Return/Risk Ratio 
Source: See Bruce I. Jacobs and Kenneth N. Levy, “Investment Management: An 
Architecture for the Equity Market,” Chapter 1 in Frank J. Fabozzi (ed.), Active 
Equity Portfolio Management (New Hope, PA: Frank J. Fabozzi Associates, 
1998), p. 6. 

571 
Equity Portfolio Management 
the breadth of implementable manager ideas is high. This can happen in a 
world where active managers employ an engineered approach to active 
portfolio management. However, if the capital market is largely price effi-
cient, then the probability of failing to produce any level of active reward is 
high (near one). With market efficiency, investable ideas are transparent, 
and their active implications are already fully impounded in security prices. 
Strategies Based on Technical Analysis 
Given the preceding developments, we would be remiss for not shedding 
some insight on active strategies based on technical analysis. In this con-
text, various common stock strategies that involve only historical price 
movement, trading volume, and other technical indicators have been sug-
gested since the beginning of stock trading. Many of these strategies 
involve investigating patterns based on historical trading data (past price 
data and trading volume) to forecast the future movement of individual 
stocks or the market as a whole. Based on observed patterns, mechanical 
trading rules indicating when a stock should be bought, sold, or sold 
short are developed. Thus, no consideration is given to any factor other 
than the specified technical indicators. This approach to active manage-
ment is called technical analysis. Because some of these strategies involve 
the analysis of charts that plot price and/or volume movements, investors 
who follow a technical analysis approach are sometimes called chartists. 
The overlying principle of these strategies is to detect changes in the sup-
ply of and demand for a stock and capitalize on the expected changes. 
Simple Filter Rules 
The simplest type of technical strategy is to buy and sell on the basis of a 
predetermined movement in the price of a stock; the rule is basically if the 
stock increases by a certain percentage, the stock is purchased and held 
until the price declines by a certain percentage, at which time the stock is 
sold. The percentage by which the price must change is called the “filter.” 
Each investor pursuing this technical strategy decides his or her own filter. 
Moving Averages 
Some technical analysts make decisions to buy or sell a stock based on the 
movement of a stock over an extended period of time (for example, 200 
days). An average of the price over the time period is computed, and a 
rule is specified that if the price is greater than some percentage of the 
average, the stock should be purchased; if the price is less than some per-
centage of the average, the stock should be sold. The simplest way to cal-
culate the average is to calculate a simple moving average. Assuming that 
the time period selected by the technical analyst is 200 days, then the 

572 
The Mathematics of Financial Modeling and Investment Management 
average price over the 200 days is determined. A more complex moving 
average can be calculated by giving greater weight to more recent prices. 
Advance/Decline Line 
On each trading day, some stocks will increase in price or “advance” 
from the closing price on the previous trading day, while other stocks 
will decrease in price or decline from the closing price on the previous 
trading day. It has been suggested by some market observers that the 
cumulative number of advances over a certain number of days minus the 
cumulative number of declines over the same number of days can be 
used as an indicator of short-term movements in the stock market. 
Relative Strength 
The relative strength of a stock is measured by the ratio of the stock 
price to some price index. The ratio indicates the relative movement of 
the stock to the index. The price index can be the index of the price of 
stocks in a given industry or a broad-based index of all stocks. If the 
ratio rises, it is presumed that the stock is in an uptrend relative to the 
index; if the ratio falls, it is presumed that the stock is in a downtrend 
relative to the index. Similarly, a relative strength measure can be calcu-
lated for an industry group relative to a broad-based index. Relative 
strength is also referred to as price momentum or price persistence. 
Short Interest Ratio 
Some technical analysts believe that the ratio of the number of shares sold 
short relative to the average daily trading volume is a technical signal that 
is valuable in forecasting the market. This ratio is called the short interest 
ratio. However, the economic link between this ratio and stock price move-
ments can be interpreted in two ways. On one hand, some market observ-
ers believe that if this ratio is high, this is a signal that the market will 
advance. The argument is that short sellers will have to eventually cover 
their short position by buying the stocks they have shorted and, as a result, 
market prices will increase. On the other hand, there are some market 
observers who believe this a bearish signal being sent by market partici-
pants who have shorted stocks in anticipation of a declining market. 
Market Overreaction 
To benefit from favorable news or to reduce the adverse effect of unfa-
vorable news, investors must react quickly to new information.12 
12 Werner DeBondt and Richard Thaler, “Does the Market Overreact?” Journal of Finance 
(July 1985), pp. 793–805. 

573 
Equity Portfolio Management 
According to cognitive psychologists, people tend to overreact to 
extreme events. People tend to react more strongly to recent informa-
tion and they tend to heavily discount older information. 
The question is, do investors follow the same pattern? That is, do 
investors overreact to extreme events? The overreaction hypothesis sug-
gests that when investors react to unanticipated news that will benefit a 
company’s stock, the price rise will be greater than it should be given 
that information, resulting in a subsequent decline in the price of the 
stock. In contrast, the overreaction to unanticipated news that is 
expected to adversely affect the economic well-being of a company will 
force the price down too much, followed by a subsequent correction 
that will increase the price. 
If, in fact, the market does overreact, investors may be able to 
exploit this to realize positive abnormal returns if they can (1) identify 
an extreme event, and (2) determine when the effect of the overreaction 
has been impounded in the market price and is ready to reverse. Inves-
tors who are capable of doing this will pursue the following strategies. 
When positive news is identified, investors will buy the stock and sell it 
before the correction to the overreaction. In the case of negative news, 
investors will short the stock and then buy it back to cover the short 
position before the correction to the overreaction. 
Nonlinear Dynamic Models and Chaos 
Technical analysis has taken a more scientific twist with the development 
of nonlinear dynamics and chaos theory. Patterns generated by nonlinear 
dynamic models can be very complex and appear nearly random. A num-
ber of studies have tried to ascertain whether the apparent randomness 
of price processes could be generated by deterministic nonlinear pro-
cesses. A chaotic process rapidly becomes unpredictable. There are, how-
ever, chaotic processes that are relatively simple and that maintain a 
certain level of predictability. Models of weather, for instance, are cha-
otic but still allow to make reasonable weather forecast. 
A number of chaos scientists hoped to discover that economic laws 
could be expressed as simple chaotic processes. In particular, it was 
hoped to discover that price processes could be described as simple cha-
otic laws with some level of predictability. Should this be the case, chaos 
theory offers a reasonable toolbox to recover the chaotic model from 
past data. In fact, if the chaotic dynamic is simple, a fundamental theo-
rem of chaos theory, the theorem of Takens, offers a way to fully recon-
struct chaotic dynamics from a sufficient number of past data. In 
addition, functional approximation schemes such as neural networks 
could be used to approximate the chaotic dynamics. 

574 
The Mathematics of Financial Modeling and Investment Management 
The key point is that Takens theorem and all approximation 
schemes work only if the dynamic is simple.13 A number of tests have 
been devised to check if economic and financial quantities can be effec-
tively be represented as a simple chaotic laws. Among the tests, in par-
ticular the BDS test (see Chapter 9) is popular amongst economists. The 
results of tests are generally negative. There is no compelling evidence 
that reasonably simple chaotic dynamics can explain financial processes. 
Despite these negative theoretical results, technical rules based on 
neural networks or directly on the Takens theorem have been proposed 
and continue to be proposed. 
These rules have shown some result. This is not necessarily in con-
trast with the negative theoretical finding. One might find some profit-
ability in trading rules even if the dynamics is theoretically not simple. 
Technical Analysis and Statistical Nonlinear Pattern Recognition 
Technical analysis can also be cast in terms of statistical pattern recogni-
tion. A number of models that fundamentally differ from a random 
walk or a martingale model have been proposed. Pair trading and coin-
tegration-based strategies are perhaps the best known examples of sta-
tistical models that exploit statistical patterns. 
The empirical literature offers contradicting evidence. There is 
agreement that asset price processes offer some level of forecastability.14 
There are also theoretical reasons to believe that price processes in a 
finite economy must exhibit cointegration15 and therefore recognizable 
patterns. ARCH and GARCH behavior is another source of nonlinear 
statistical patterns. What is not clear, however, is the profitability that 
can be associated to these statistical findings once the trading costs are 
taken into account. 
13 Simple dynamics means that there is a low-dimensionality attractor. Chaos theory 
is a complex subject. The interested reader should consult Robert C. Hilborn, Chaos 
and Nonlinear Dynamics (New York: Oxford University Press, 2000). 
14 See W. Brock, J. Lakonishok, and B. LeBaron, “Simple Technical Trading Rules 
and the Stochastic Properties of Stock Returns,” Working paper 90–22, Wisconsin 
Madison Social Systems; and John Campbell, Andrew Lo, and Craig MacKinlay, 
The Econometrics of Financial Markets (Princeton, NJ: Princeton University Press, 
1997). 
15 See Marlene Cerchi and Arthur Havenner, “Cointegration and Stock Prices: The 
Random Walk on Wall Street Revisited,” Journal of Economic Dynamics and Con-
trol 12 (1988), pp. 333–346; Peter Bossaerts, “Common Nonstationary Compo-
nents of Asset Prices,” Journal of Economic Dynamics and Control 12 (1988), pp. 
347–364; and, Barr Rosenberg and J.A. Ohlson, “The Stationary Distribution of Re-
turns and Portfolio Separation in Capital Markets: A Fundamental Contradiction,” 
Journal of Financial and Quantitative Analysis 11 (1976), pp. 393–401. 

575 
Equity Portfolio Management 
Market-Neutral Strategies and Statistical Arbitrage 
Market-neutral strategies are portfolio management strategies aimed at 
obtaining a positive return regardless of market conditions; a typical 
way to achieve this result is long-short equity portfolio management. In 
general, a market-neutral strategy will specify four elements:
 ■ Market neutrality is normally defined as lack of correlation with some 
broad index such as the S&P 500.
 ■ The return objective varies in function of market conditions. In a bear 
market, a market-neutral strategy might be happy with a modest 5% 
return while double-digit return rates might be required in normal con-
ditions.
 ■ In general, return volatility bounds are set low, significantly lower than 
the market volatility. Often this requirement is imposed by central 
banks.
 ■ A maximum draw-down. 
The above requirements might seem contrary to finance theory as 
they appear to violate the risk-return trade-offs of efficient markets. 
They might also seem contrary to common sense as conservative pre-
scriptions for volatility and draw-dawns are coupled with aggressive 
return objectives. The only possible response to these criticisms is that 
market neutral-strategies represent only a small fraction of the market— 
those pockets of inefficiency inevitable in (and perhaps instrumental to) 
a large efficient market. 
Let’s now describe statistical arbitrage, a method used to obtain 
market neutral strategies. Statistical arbitrage exploits the existence of 
small probabilistic profit opportunities that become nearly deterministic 
on a large scale. It was made possible by the diffusion of electronic 
transactions that have greatly reduced transaction costs. Obviously 
transaction costs and bid-ask spreads might reduce profit opportunities 
to nearly zero or even cause losses. 
To understand the working of statistical arbitrage, recall that in the 
limit of a large economy and under the assumption that it is possible to 
completely diversify portfolios, the APT conditions are valid. Recall 
also that the APT conditions are represented by zero intercept. The 
same condition is valid in the case of single-factor CAPM. As a conse-
quence, if a large number of non-zero intercepts exist, then large profits 
can be made with zero initial investment and little risk. 
To demonstrate the above, we start with a single-factor market 
model with nonzero intercepts: 

576 
The Mathematics of Financial Modeling and Investment Management 
ri = αi + βirM + ε 
where the noise term exhibits only local correlation and tends to zero 
over large portfolios. Market return is stochastic and therefore uncer-
tain. Suppose, however, that there are many returns with similar betas 
but with different alphas. The no-arbitrage condition forbids this situa-
tion for an infinite economy but leaves open the possibility that a finite 
number of such situations exist. 
For each beta, or more likely for each beta band as betas will not be 
strictly equal, invest in a long portfolio with the positive alphas and a 
short portfolio with the negative alphas. Repeat the operation for each 
band of beta. The resulting portfolio will implement a simple statistical 
arbitrage strategy. It will be nearly market-neutral, with profit depending 
only on the spreads between alphas and not on the direction of the market. 
There are several caveats. First, the appropriate distribution of betas 
and alphas must exist. This is an empirical question that cannot be solved 
a priori. Second, there are residual risks, as the noise term will be reduced 
but not completely eliminated and betas will not be strictly equal. Third, 
the factor model might be misspecified and therefore unstable. 
Contrarian strategies where managers go short on overpriced stocks 
and long on underpriced stocks are also possible. Long-short strategies 
of this type started in the 1980s with so-called pair trading reportedly 
initiated by a trading group working at Morgan Stanley. Under the 
direction of Nunzio Tartaglia, this group’s strategy consisted in forming 
pairs of stocks that had a small distance measured by the relative vari-
ance. Setting appropriate thresholds, underpriced stocks are bought and 
overpriced stocks sold. 
The ideas underlying contrarian strategies are ultimately formalized 
by the concepts of cointegration and error correction. When applied to 
price, processes error correction represents changes in returns when prices 
diverge from some common trend. Many efforts at building true statisti-
cal arbitrage techniques therefore make use of cointegration techniques. 
In terms of cointegration, one implements statistical arbitrage by search-
ing for cointegrating relationships. Each cointegrating relationship repre-
sents a stationary, mean-reverting portfolio. Being autocorrelated, these 
portfolios are more predictable than other portfolios or individual stocks. 
As most implementations are proprietary, the different approaches 
are only partially described. The key problem is to find true cointegrated 
portfolios. In practice, there are several approaches; these include:
 ■ Searching for cointegrated pairs of stocks. This can be performed with 
standard cointegration tests and techniques. However results are very 

577 
Equity Portfolio Management 
noisy as a large fraction of the cointegrated pairs will be spurious. In 
practice, the number of cointegrated pairs has to be reduced.
 ■ Searching for cointegrated indexes. This is performed testing cointegra-
tion on existing, commercially available indexes. These indices typi-
cally reflect economic sectors or geographies. After determining that 
cointegration among the indexes exists, one has to select stocks within 
the index to reduce transaction costs.
 ■ Searching for common trends. This is a recent development in statisti-
cal arbitrage. It is based on approximate robust techniques for finding 
factors using state space models. Factors, in this sense, are linear com-
binations of price processes not of returns. 
In summary, statistical arbitrage is a new methodology for managing 
long-short equity portfolios based on finding stable trends that signal 
profit opportunities. Trends might be determined with classical factor 
models of returns. More recently, cointegration techniques are being used. 
APPLICATION OF MULTIFACTOR RISK MODELS 
In the previous chapter, we explained how factors are determined. In 
this section we will see how multifactor risk models are used. In our 
illustration with use the Barra model described in the previous chapter. 
Risk Decomposition 
The real usefulness of a linear multifactor model lies in the ease with 
which the risk of a portfolio with several assets can be estimated. Con-
sider a portfolio with 100 assets. Risk is commonly defined as the vari-
ance of the portfolio’s returns. So, in this case, we need to find the 
variance-covariance matrix of the 100 assets. That would require us to 
estimate 100 variances (one for each of the 100 assets) and 4,950 covari-
ances among the 100 assets. That is, in all we need to estimate 5,050 val-
ues, a very difficult undertaking. Suppose, instead, that we use a 3 factor 
model to estimate risk. Then, we need to estimate (1) the three factor 
loadings for each of the 100 assets (i.e., 300 values); (2) the six values of 
the factor variance-covariance matrix; and (3) the 100 residual variances 
(one for each asset). That is, in all, we need to estimate only 406 values. 
This represents a nearly 90% reduction from having to estimate 5,050 
values, a huge improvement. Thus, with well-chosen factors, we can sub-
stantially reduce the work involved in estimating a portfolio’s risk. Note 
that the ease of estimation of correlation parameters is another facet of 
the fact that factor models capture the stable correlation information. 

578 
The Mathematics of Financial Modeling and Investment Management 
Multifactor risk models allow a manager and a client to decompose 
risk in order to assess the potential performance of a portfolio to the 
risk factors and to assess the potential performance of a portfolio rela-
tive to a benchmark. This is the portfolio construction and risk control 
application of the model. Also, the actual performance of a portfolio 
relative to a benchmark can be assessed. This is the performance attri-
bution analysis application of the model. 
Barra suggests that there are various ways that a portfolio’s total risk 
can be decomposed when employing a multifactor risk model.16 Each 
decomposition approach can be useful to managers depending on the 
equity portfolio management that they pursue. The four approaches are 
(1) total risk decomposition; (2) systematic-residual risk decomposition;
(3) active risk decomposition; and (4) active systematic-active residual
risk decomposition. We describe each below and explain how managers 
pursuing different management strategies (i.e., active versus passive) will 
find the decomposition helpful in portfolio construction and evaluation. 
In all of these approaches to risk decomposition, the total return is first 
divided into the risk-free return and the total excess return. The total excess 
return is the difference between the actual return realized by the portfolio 
and the risk-free return. The risk associated with the total excess return, 
called total excess risk, is what is further partitioned in the four approaches. 
Total Risk Decomposition 
There are managers who seek to minimize total risk. For example, a 
manager pursuing a long-short or market neutral strategy, as discussed 
later in this chapter, seek to construct a portfolio that minimizes total 
risk. For such managers, total risk decomposition which breaks down 
the total excess risk into two components—common factor risks (e.g., 
capitalization and industry exposures) and specific risk—is useful. This 
decomposition is shown in Exhibit 19.5. There is no provision for mar-
ket risk, only risk attributed to the common factor risks and company-
specific influences (i.e., risk unique to a particular company and there-
fore uncorrelated with the specific risk of other companies). Thus, the 
market portfolio is not a risk factor considered in this decomposition. 
Systematic-Residual Risk Decomposition 
There are managers who seek to time the market or who intentionally 
make bets to create a different exposure than that of a market portfolio. 
Such managers would find it useful to decompose total excess risk into 
systematic risk and residual risk as shown in Exhibit 19.6. Unlike in the 
16 See Chapter 4 in Barra, Risk Model Handbook United States Equity: Version 3. 
The discussion to follow in this section follows that in the Barra publication. 

579 
Equity Portfolio Management 
EXHIBIT 19.5 
Total Risk Decomposition 
Source: Figure 4.2 in Barra, Risk Model Handbook United States Equity: Version 
3 (Berkeley, CA: Barra, 1998), p. 34. Reprinted with permission. 
total risk decomposition approach just described, this view brings mar-
ket risk into the analysis. 
Residual risk in the systematic-residual risk decomposition is 
defined in a different way than residual risk is in the total risk decompo-
sition. In the systematic-residual risk decomposition, residual risk is risk 
that is uncorrelated with the market portfolio. In turn, residual risk is 
partitioned into specific risk and common factor risk. Notice that the 
partitioning of risk described here is different from that in the APT 
model described earlier in this chapter. In that section, all risk factors 
that could not be diversified away were referred to as “systematic 
risks.” In our discussion here, risk factors that cannot be diversified 
away are classified as market risk and common factor risk. Residual risk 
can be diversified to a negligible level. 
Active Risk Decomposition 
The active risk decomposition approach is useful for assessing a portfolio’s 
risk exposure and actual performance relative to a benchmark index is 
explained. that purpose. In this type of decomposition, shown in Exhibit 
19.7, the total excess return is divided into benchmark risk and active risk. 

580 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 19.6 
Systematic-Residual Risk Decomposition 
Source: Figure 4.3 in Barra, Risk Model Handbook United States Equity: Version
3 (Berkeley, CA: Barra, 1998), p. 34. Reprinted with permission. 
Benchmark risk is defined as the risk associated with the benchmark 
portfolio. Active risk or tracking error is the risk that results from the man-
ager’s attempt to generate a return that will outperform the benchmark. The 
active risk is further partitioned into common factor risk and specific risk. 
Active Systematic-Active Residual Risk Decomposition 
There are managers who overlay a market-timing strategy on their stock 
selection. That is, they not only try to select stocks they believe will out-
perform but also try to time the purchase of the acquisition. For a man-
ager who pursues such a strategy, it will be important in evaluating 
performance to separate market risk from common factor risks. In the 
active risk decomposition approach just discussed, there is no market 
risk identified as one of the risk factors. Since market risk (i.e., system-
atic risk) is an element of active risk, its inclusion as a source of risk is 
preferred by managers. When market risk is included, we have the 
active systematic-active residual risk decomposition approach shown in 
Exhibit 19.8. Total excess risk is again divided into benchmark risk and 
active risk. However, active risk is further divided into active systematic 
risk (i.e., active market risk) and active residual risk. Then active resid-
ual risk is divided into common factor risks and specific risk. 

581 
Equity Portfolio Management 
EXHIBIT 19.7 
Active Risk Decomposition 
Source: Figure 4.4 in Barra, Risk Model Handbook United States Equity: Version 3 
(Berkeley, CA: Barra, 1998), p. 34. Reprinted with permission. 
EXHIBIT 19.8 
Active Systematic-Active Residual Risk Decomposition 
Source: Figure 4.5 in Barra, Risk Model Handbook United States Equity: Version 3 
(Berkeley, CA: Barra, 1998), p. 37. Reprinted with permission. 

582 
The Mathematics of Financial Modeling and Investment Management 
Summary of Risk Decomposition 
The four approaches to risk decomposition are just different ways of 
slicing up risk to help a manager in constructing and controlling the risk 
of a portfolio and for a client to understand how the manager per-
formed. Exhibit 19.9 provides an overview of the four approaches to 
carving up risk into specific/common risks, systematic/residual risks, 
and benchmark/active risks. 
Portfolio Construction and Risk Control 
The power of a multifactor risk model is that given the risk factors and 
the risk factor sensitivities, a portfolio’s risk exposure profile can be 
quantified and controlled. The three examples below show how this can 
be done so that the a manager can avoid making unintended bets. In the 
examples, we use the Barra E3 factor model.17 
EXHIBIT 19.9 
Risk Decomposition Overview 
Source: Figure 4.6 in Barra, Risk Model Handbook United States Equity: Version 
3 (Berkeley, CA: Barra, 1998), p. 38. Reprinted with permission. 
17 The illustrations are taken from Frank J. Fabozzi, Frank J. Jones, and Raman 
Vardharaj, “Multi-Factor Risk Models,” Chapter 13 in Frank J. Fabozzi and Harry 
M. Markowitz (eds.), The Theory and Practice of Investment Management (Hobo-
ken, NJ: John Wiley & Sons, 2002). 

583 
Equity Portfolio Management 
Assessing the Exposure of a Portfolio 
A fundamental multifactor risk model can be used to assess whether the 
current portfolio is consistent with a manager’s strengths. Exhibit 19.10 
is a list of the top 15 holdings of Portfolio ABC as of September 30, 
2000. Exhibit 19.11 is a risk-return report for the same portfolio. The 
portfolio had a total market value of over $3.7 billion, 202 holdings, 
and a predicted beta of 1.20. The risk report also shows that the portfo-
lio had an active risk of 9.83%. This is its tracking error with respect to 
the benchmark, the S&P 500. Notice that over 80% of the active risk 
variance (which is 96.67) comes from the common factor risk variance 
(which is 81.34), and only a small proportion comes from the stock-spe-
cific risk variance (which is 15.33). Clearly, the manager of this portfo-
lio has placed fairly large factor bets. 
Exhibit 19.12a assesses the factor risk exposures of Portfolio ABC rel-
ative to those of the S&P 500, its benchmark. The first column shows the 
exposures of the portfolio, and the second column shows the exposures 
for the benchmark. The last column shows the active exposure, which is 
EXHIBIT 19.10 
Portfolio ABC’s Holdings (Only the Top 15 Holdings Shown) 
Portfolio: 
ABC Fund 
Benchmark: 
S&P 500 
Model Date: 
2000-10-02 
Report Date: 
2000-10-15 
Price Date: 
2000-09-29 
Model: 
U.S. Equity 3 
Price Weight 
Main Industry
Name 
Shares 
($) 
(%) 
Beta 
Name 
Sector 
General Elec. Co. 
2,751,200
 57.81 4.28 0.89 Financial Services 
Financial 
Citigroup, Inc. 
2,554,666
 54.06 3.72 0.98 Banks 
Financial 
Cisco Sys., Inc. 
2,164,000
 55.25 3.22 1.45 Computer Hardware 
Technology 
EMC Corp., Mass. 
1,053,600
 99.50 2.82 1.19 Computer Hardware 
Technology 
Intel Corp. 
2,285,600
 41.56 2.56 1.65 Semiconductors 
Technology 
Nortel Networks Corp. N 1,548,600
 60.38 2.52 1.40 Electronic Equipment 
Technology 
Corning, Inc.
   293,200 297.50 2.35 1.31 Electronic Equipment 
Technology 
International Business
   739,000 112.50 2.24 1.05 Computer Software 
Technology 
Oracle Corp.
 955,600
 78.75 2.03 1.40 Computer Software 
Technology 
Sun Microsystems, Inc.
   624,700 116.75 1.96 1.30 Computer Hardware 
Technology 
Lehman Bros. Hldgs. Inc.    394,700 148.63 1.58 1.51 Sec. & Asset Management Financial 
Morgan Stanley Dean Wi.
 615,400
 91.44 1.52 1.29 Sec. & Asset Management Financial 
Walt Disney Co. 
1,276,700
 38.25 1.32 0.85 Entertainment 
Cnsmr. Services 
Coca-Cola Co.
 873,900
 55.13 1.30 0.68 Food & Beverage 
Cnsmr. (non-cyc.) 
Microsoft Corp.
 762,245
 60.31 1.24 1.35 Computer Software 
Technology 
Source: Exhibit 13.7 in Frank J. Fabozzi, Frank J. Jones, and Raman Vardharaj, 
“Multi-Factor Risk Models,” Chapter 13 in Frank J. Fabozzi and Harry M. 
Markowitz (eds.), The Theory and Practice of Investment Management (Hobo-
ken, NJ: John Wiley & Sons, 2002). 

584 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 19.11 
Portfolio ABC’s Risk-Return Decomposition 
Number of Assets 
202 
Total Shares 
62,648,570 
Average Share Price 
$59.27 
Portfolio Beta 
1.20 
Portfolio Value 
$3,713,372,229.96 
Risk Decomposition 
Variance 
Standard Deviation (%) 
Active Specific Risk
 15.33
 3.92 
Active Common Factor
 Risk Indices
 44.25
 6.65
 Industries
 17.82
 4.22
 Covariance 
19.27
     Total Active Common Factor Riska
 81.34
 9.02 
Total Activeb
 96.67
 9.83 
Benchmark 
247.65 
15.74 
Total Risk 
441.63 
21.02 
a Equal to Risk Indices + Industries + Covariances 
b Equal to Active Specific Risk + Total Active Common Factor Risk 
Source: Exhibit 13.8 in Frank J. Fabozzi, Frank J. Jones, and Raman Vardharaj, 
“Multi-Factor Risk Models,” Chapter 13 in Frank J. Fabozzi and Harry M. 
Markowitz (eds.), The Theory and Practice of Investment Management (Hobo-
ken, NJ: John Wiley & Sons, 2002). 
the difference between the portfolio exposure and the benchmark expo-
sure. The exposures to the risk index factors are measured in units of stan-
dard deviation, while the exposures to the industry factors are measured 
in percentages. The portfolio has a high active exposure to the momentum 
risk index factor. That is, the stocks held in the portfolio have significant 
momentum. The portfolio’s stocks were smaller than the benchmark aver-
age in terms of market cap. The industry factor exposures reveal that the 
portfolio had an exceptionally high active exposure to the semiconductor 
industry and electronic equipment industry. Exhibit 19.12b combines the 
industry exposures to obtain sector exposures. It shows that Portfolio 
ABC had a very high active exposure to the Technology sector. Such large 
bets can expose the portfolio to large swings in returns. 
An important use of such risk reports is the identification of portfo-
lio bets, both explicit and implicit. If, for example, the manager of Port-
folio ABC did not want to place such a large Technology sector bet or 
momentum risk index bet, then she (or he) can rebalance the portfolio 
to minimize any such bets. 

585 
Equity Portfolio Management 
EXHIBIT 19.12 
Analysis of Portfolio ABC’s Exposures 
a. Analysis of Risk Exposures to S&P 500
Factor Exposures 
Risk Index Exposures (Std. Dev.) 
Mgd. 
Bmk. 
Act. 
Mgd. 
Bmk. 
Act. 
Volatility
 0.220 
−0.171
 0.391 
Value 
−0.169 
−0.034 
−0.136 
Momentum
 0.665 
−0.163
 0.828 
Earnings variation
 0.058 
−0.146
 0.204 
Size 
−0.086
 0.399 
−0.485 
Leverage
 0.178 
−0.149
 0.327 
Size nonlinearity
 0.031
 0.097 
−0.067 
Currency sensitivity
 0.028 
−0.049
 0.077 
Trading Activity
 0.552 
−0.083
 0.635 
Yield 
−0.279
 0.059 
−0.338 
Growth
 0.227 
−0.167
 0.395 
Non-EST universe
 0.032
 0.000
 0.032 
Earnings yield 
−0.051
 0.081 
−0.132 
Industry Weights (Percent) 
Mining and Metals 
Gold 
Forestry and Paper 
Chemicals 
Energy Reserves 
Oil Refining 
Oil Services 
Food & Beverages 
Alcohol 
Tobacco 
Home Products 
Grocery Stores 
Consumer Durables 
Motor Vehicles and Parts 
Apparel and Textiles 
Clothing Stores 
Specialty Retail 
Department Stores 
Constructn. and Real Prop. 
Publishing 
Media 
Hotels 
Restaurants 
Entertainment 
Leisure 
Environmental Services 
Heavy Electrical Eqp. 
Mgd. Bmk. 
Act. 
Mgd. 
Bmk. 
Act. 
0.013 
0.000 
0.198 
0.439 
2.212 
0.582 
2.996 
2.475 
0.000 
0.000 
0.000 
0.000 
0.165 
0.000 
0.000 
0.177 
0.445 
0.000 
0.569 
0.014 
1.460 
0.090 
0.146 
1.179 
0.000 
0.000 
1.438 
0.375 
0.119 
0.647 
2.386 
4.589 
0.808 
0.592
3.073 
0.467 
0.403 
1.821 
0.407 
0.125
0.714 
0.191 
0.308 
2.127 
2.346 
0.204
0.508 
2.077 
0.112 
0.465 
1.277 
0.247 
0.117 
1.922 
−0.362 
−0.119 
−0.449 
−1.947 
−2.377 
−0.226 
2.404 
−0.597 
−0.467 
−0.403 
−1.821 
−0.407 
0.039 
−0.714 
−0.191 
−0.131 
−1.681 
−2.346 
0.364 
−0.494 
−0.617 
−0.022 
−0.319 
−0.098 
−0.247 
−0.117 
−0.483 
Heavy Machinery 
Industrial Parts 
Electric Utility 
Gas Utilities 
Railroads 
Airlines 
Truck/Sea/Air Freight 
Medical Services 
Medical Products 
Drugs 
Electronic Equipment 
Semiconductors 
Computer Hardware 
Computer Software 
Defense and Aerospace 
Telephone 
Wireless Telecom. 
Information Services 
Industrial Services 
Life/Health Insurance 
Property/Casualty Ins. 
Banks 
Thrifts 
Securities and Asst. Mgmt. 
Financial Services 
Internet 
Equity REIT 
0.000 
0.062 −0.062 
0.234 
1.086 −0.852 
1.852 
1.967 −0.115 
0.370 
0.272
 0.098 
0.000 
0.211 −0.211 
0.143 
0.194 −0.051 
0.000 
0.130 −0.130 
1.294 
0.354
 0.940 
0.469 
2.840 −2.370 
6.547 
8.039 −1.492 
11.052 5.192
 5.860 
17.622 6.058 11.564 
12.057 9.417
 2.640 
9.374 
6.766
 2.608 
0.014 
0.923 −0.909 
0.907 
4.635 −3.728 
0.000 
1.277 −1.277 
0.372 
1.970 −1.598 
0.000 
0.511 −0.511 
0.062 
1.105 −1.044 
1.069 
2.187 −1.118 
5.633 
6.262 −0.630 
1.804 
0.237
 1.567 
6.132 
2.243
 3.888 
5.050 
5.907 −0.857 
3.348 
1.729
 1.618 
0.000 
0.000
 0.000 
Note: Mgd. = Managed; Bmk. = S&P 500 (the benchmark); Act. = Active = Managed 
− Benchmark 

586 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 19.12 (Continued) 
b. Analysis of Sector Exposures Relative to S&P 500
Sector Weights (Percent) 
Mgd. 
Bmk. 
Act. 
Mgd. 
Bmk. 
Act. 
Basic Materials 
0.65 
3.53 
−2.88 
Utility
 2.22
 2.24 
−0.02
 Mining 
0.01 
0.38 
−0.36
 Electric Utility
 1.85
 1.97 
−0.12
 Gold 
0.00 
0.12 
−0.12
 Gas Utility
 0.37
 0.27
 0.10
 Forest 
0.20 
0.65 
−0.45 
Transport
 0.14
 0.54 
−0.39
 Chemical 
0.44 
2.39 
−1.95
 Railroad
 0.00
 0.21 
−0.21 
Energy 
5.79 
5.99 
−0.20
 Airlines
 0.14
 0.19 
−0.05
 Energy Reserves 
2.21 
4.59 
−2.38
     Truck Freight
 0.00
 0.13 
−0.13
 Oil Refining 
0.58 
0.81 
−0.23
 Health Care
 8.31 
11.23 
−2.92
 Oil Services 
3.00 
0.59
 2.40
 Medical Provider
 1.29
 0.35
 0.94 
Cnsmr (non-cyc.) 
2.48 
6.17 
−3.70
 Medical Products
 0.47
 2.84 
−2.37
 Food/Beverage 
2.48 
3.07 
−0.60
 Drugs
 6.55
 8.04 
−1.49
 Alcohol 
0.00 
0.47 
−0.47 
Technology 
53.47 
30.09 
23.38
     Tobacco 
0.00 
0.40 
−0.40
 Electronic Equipment 
11.05
 5.19
 5.86
 Home Prod. 
0.00 
1.82 
−1.82
 Semiconductors 
17.62
 6.06 
11.56
 Grocery 
0.00 
0.41 
−0.41
 Computer Hardware 
12.06
 9.42
 2.64 
Cnsmr. (cyclical) 
1.36 
6.01 
−4.66
 Computer Software
 9.37
 6.77
 2.61
 Cons. Durables 
0.17 
0.13
 0.04
 Defense and Aerospace
 0.01
 0.92 
−0.91
     Motor Vehicles 
0.00 
0.71 
−0.71
 Internet
 3.35
 1.73
 1.62
 Apparel 
0.00 
0.19 
−0.19 
Telecommunications
 0.91
 5.91 
−5.00
 Clothing 
0.18 
0.31 
−0.13
     Telephone
 0.91
 4.63 
−3.73
 Specialty Retail 
0.45 
2.13 
−1.68
     Wireless
 0.00
 1.28 
−1.28
 Dept. Store 
0.00 
2.35 
−2.35 
Commercial Services
 0.37
 2.48 
−2.11
 Construction 
0.57 
0.20
 0.36
 Information Services
 0.37
 1.97 
−1.60 
Cnsmr Services 
2.89 
4.69 
−1.80
 Industrial Services
 0.00
 0.51 
−0.51
 Publishing 
0.01 
0.51 
−0.49 
Financial 
19.75 
17.94
 1.81
 Media 
1.46 
2.08 
−0.62
 Life Insurance
 0.06
 1.11 
−1.04
 Hotels 
0.09 
0.11 
−0.02
 Property Insurance
 1.07
 2.19 
−1.12
 Restaurants 
0.15 
0.47 
−0.32
 Banks
 5.63
 6.26 
−0.63
 Entertainment 
1.18 
1.28 
−0.10
 Thrifts
 1.80
 0.24
 1.57
 Leisure 
0.00 
0.25 
−0.25
 Securities/Asst. Mgmt.
 6.13
 2.24
 3.89 
Industrials 
1.67 
3.19 
−1.51
 Financial Services
 5.05
 5.91 
−0.86
     Env. Services 
0.00 
0.12 
−0.12
 Equity REIT
 0.00
 0.00
 0.00
 Heavy Electrical 
1.44 
1.92 
−0.48
 Heavy Mach. 
0.00 
0.06 
−0.06
 Industrial Parts 
0.23 
1.09 
−0.85 
Note: Mgd = Managed; Bmk = Benchmark; Act = Active = Managed − Benchmark 
Source: Exhibit 13.9 in Frank J. Fabozzi, Frank J. Jones, and Raman Vardharaj, 
“Multi-Factor Risk Models,” Chapter 13 in Frank J. Fabozzi and Harry M. 
Markowitz (eds.), The Theory and Practice of Investment Management (Hobo-
ken, NJ: John Wiley & Sons, 2002). 

587 
Equity Portfolio Management 
Risk Control Against a Stock Market Index 
The objective in equity indexing is to match the performance of some 
specified stock market index with little tracking error. To do this, the 
risk profile of the indexed portfolio must match the risk profile of the 
designated stock market index. Put in other terms, the factor risk expo-
sure of the indexed portfolio must match as closely as possible the expo-
sure of the designated stock market index to the same factors. Any 
differences in the factor risk exposures result in tracking error. Identifi-
cation of any differences allows the indexer to rebalance the portfolio to 
reduce tracking error. 
To illustrate this, suppose that an index manager has constructed a 
portfolio of 50 stocks to match the S&P 500. Exhibit 19.13 shows out-
put of the exposure to the Barra risk indices and industry groups of the 
50-stock portfolio and the S&P 500. The last column in the exhibit 
shows the difference in the exposure. The differences are very small 
except for the exposures to the size factor and one industry (equity 
REIT). That is, the 50-stock portfolio has more exposure to the size risk 
index and equity REIT industry. 
The illustration in Exhibit 19.13 uses price data as of December 31, 
2001. It demonstrates how a multifactor risk model can be combined 
with an optimization model to construct an indexed portfolio when a 
given number of holdings is sought. Specifically, the portfolio analyzed 
in Exhibit 19.13 is the result of an application in which the manager 
wants a portfolio constructed that matches the S&P 500 with only 50 
stocks and that minimizes tracking error. Not only is the 50-stock port-
folio constructed, but the optimization model combined with the factor 
model indicates that the tracking error is only 2.19%. Since this is the 
optimal 50-stock portfolio to replicate the S&P 500 that minimizes 
tracking error risk, this tells the index manager that if he or she seeks a 
lower tracking error, more stocks must be held. Note, however, that the 
optimal portfolio changes as time passes and prices move. 
Tilting a Portfolio 
Now let’s look at how an active manager can construct a portfolio to 
make intentional bets. Suppose that a portfolio manager seeks to con-
struct a portfolio that generates superior returns relative to the S&P 500 
by tilting it toward low P/E stocks. At the same time, the manager does 
not want to increase tracking error significantly. An obvious approach 
may seem to be to identify all the stocks in the universe that have a 
lower than average P/E. The problem with this approach is that it intro-
duces unintentional bets with respect to the other risk indices. 

588 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 19.13 
Factor Exposures of a 50-Stock Portfolio that 
Optimally Matches the S&P 500 
Risk Index Exposures (Std. Dev.) 
Mgd. 
Bmk. 
Act. 
Mgd. 
Bmk. 
Act. 
Volatility 
−0.141 
−0.084 
−0.057 
Value 
−0.072 
−0.070 
−0.003 
Momentum 
−0.057 
−0.064
 0.007 
Earnings variation 
−0.058 
−0.088
 0.029 
Size
 0.588
 0.370
 0.217 
Leverage 
−0.206 
−0.106 
−0.100 
Size nonlinearity
 0.118
 0.106
 0.013 
Currency sensitivity 
−0.001 
−0.012
 0.012 
Trading activity 
−0.101 
−0.005 
−0.097 
Yield
 0.114
 0.034
 0.080 
Growth 
−0.008 
−0.045
 0.037 
Non-EST universe
 0.000
 0.000
 0.000 
Earnings yield
 0.103
 0.034
 0.069 
Industry Weights (Percent) 
Mining and Metals 
Gold 
Forestry and Paper 
Chemicals 
Energy Reserves 
Oil Refining 
Oil Services 
Food and Beverages 
Alcohol 
Tobacco 
Home Products 
Grocery Stores 
Consumer Durables 
Motor Vehicles & Parts 
Apparel and Textiles 
Clothing Stores 
Specialty Retail 
Department Stores 
Constructn. and Real Prop. 
Publishing 
Media 
Hotels 
Restaurants 
Entertainment 
Leisure 
Environmental Services 
Heavy Electrical Eqp. 
Mgd. Bmk. 
Act. 
Mgd. 
Bmk. 
Act. 
0.000 
0.000 
1.818 
2.360 
5.068 
1.985 
1.164 
2.518 
0.193 
1.372 
0.899 
0.000 
0.000 
0.000 
0.000 
0.149 
1.965 
4.684 
0.542 
2.492 
1.822 
1.244 
0.371 
2.540 
0.000 
0.000 
1.966 
0.606 
0.161 
0.871
2.046
4.297
1.417
0.620
3.780 
0.515 
0.732
2.435 
0.511 
0.166 
0.621 
0.373 
0.341 
2.721 
3.606
0.288
0.778
1.498
0.209
0.542 
1.630
0.409 
0.220 
1.949
−0.606 
−0.161 
0.947 
0.314 
0.771 
0.568 
0.544 
−1.261 
−0.322 
0.641 
−1.536 
−0.511 
−0.166 
−0.621 
−0.373 
−0.191 
−0.756 
1.078 
0.254 
1.713 
0.323 
1.035 
−0.171 
0.910 
−0.409 
−0.220 
0.017 
Heavy Machinery 
Industrial Parts 
Electric Utility 
Gas Utilities 
Railroads 
Airlines 
Truck/Sea/Air Freight 
Medical Services 
Medical Products 
Drugs 
Electronic Equipment 
Semiconductors 
Computer Hardware 
Computer Software 
Defense and Aerospace 
Telephone 
Wireless Telecom. 
Information Services 
Industrial Services 
Life/Health Insurance 
Property/Casualty Ins. 
Banks 
Thrifts 
Securities and Asst. Mgmt. 
Financial Services 
Internet 
Equity REIT 
0.000
 0.141 −0.141 
1.124
 1.469 −0.345 
0.000
 1.956 −1.956 
0.000
 0.456 −0.456 
0.000
 0.373 −0.373 
0.000
 0.206 −0.206 
0.061
 0.162 −0.102 
1.280
 0.789
 0.491 
3.540
 3.599 −0.059 
9.861 10.000 −0.140 
0.581
 1.985 −1.404 
4.981
 4.509
 0.472 
4.635
 4.129
 0.506 
6.893
 6.256
 0.637 
1.634
 1.336
 0.297 
3.859
 3.680
 0.180 
1.976
 1.565
 0.411 
0.802
 2.698 −1.896 
0.806
 0.670
 0.136 
0.403
 0.938 −0.535 
2.134
 2.541 −0.407 
8.369
 7.580
 0.788 
0.000
 0.362 −0.362 
2.595
 2.017
 0.577 
6.380
 6.321
 0.059 
0.736
 0.725
 0.011 
2.199
 0.193
 2.006 
Note: Mgd = Managed; Bmk = S&P 500 (the benchmark); Act = Active = Managed 
− Benchmark 
Source: Exhibit 13.10 in Frank J. Fabozzi, Frank J. Jones, and Raman Vardharaj, 
“Multi-Factor Risk Models,” Chapter 13 in Frank J. Fabozzi and Harry M. 
Markowitz (eds.), The Theory and Practice of Investment Management (Hoboken, 
NJ: John Wiley & Sons, 2002). 

589 
Equity Portfolio Management 
Instead, an optimization method combined with a multifactor risk 
model can be used to construct the desired portfolio. The necessary 
inputs to this process are the tilt exposure sought and the benchmark 
stock market index. Additional constraints can be placed, for example, 
on the number of stocks to be included in the portfolio. The Barra opti-
mization model can also handle additional specifications such as fore-
casts of expected returns or alphas on the individual stocks. 
In our illustration, the tilt exposure sought is towards low P/E 
stocks, that is, towards high earnings yield stocks (since earnings yield is 
the inverse of P/E). The benchmark is the S&P 500. We seek a portfolio 
that has an average earnings yield that is at least 0.5 standard deviations 
more than that of the earnings yield of the benchmark. We do not place 
any limit on the number of stocks to be included in the portfolio. We 
also do not want the active exposure to any other risk index factor 
(other than earnings yield) to be more than 0.1 standard deviations in 
magnitude. This way we avoid placing unintended bets. While we do 
not report the holdings of the optimal portfolio here, Exhibit 19.14 pro-
vides an analysis of that portfolio by comparing the risk exposure of the 
50-stock optimal portfolio to that of the S&P 500. 
SUMMARY
 ■ The investing process involves forming reasonable return expecta-
tions, controlling portfolio risk to demonstrate investment prudence, 
controlling trading costs, and monitoring total investment perfor-
mance.
 ■ The different degrees of active management and different degrees of 
passive management can be measured in terms of tracking error. 
■ The active return is the difference between the actual portfolio return 
for a given period and the benchmark index return for the same 
period.
 ■ Alpha is defined as the average active return over some time period. 
■ The information ratio is the ratio of alpha to the tracking error. 
■ Tracking error is the standard deviation of the active return and 
occurs because the risk profile of a portfolio differs from that of the 
risk profile of the benchmark index.
 ■ Backward-looking tracking error measures the tracking error based 
on active returns; forward-looking tracking error measures the poten-
tial tracking error of a portfolio.
 ■ Portfolio size, benchmark volatility, and portfolio beta have an 
impact on tracking error. 

590 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 19.14 
Factor Exposures of a Portfolio Tilted Towards Earnings Yield 
Risk Index Exposures (Std. Dev.) 
Mgd. 
Bmk. 
Act. 
Mgd. 
Bmk. 
Act. 
Volatility 
−0.126 
−0.084 
−0.042 
Value
 0.030 
−0.070
 0.100 
Momentum
 0.013 
−0.064
 0.077 
Earnings variation 
−0.028 
−0.088
 0.060 
Size
 0.270
 0.370 
−0.100 
Leverage 
−0.006 
−0.106
 0.100 
Size nonlinearity
 0.067
 0.106 
−0.038 
Currency sensitivity 
−0.105 
−0.012 
−0.093 
Trading activity
 0.095 
−0.005
 0.100 
Yield
 0.134
 0.034
 0.100 
Growth 
−0.023 
−0.045
 0.022 
Non-EST universe
 0.000
 0.000
 0.000 
Earnings Yield
 0.534
 0.034
 0.500 
Industry Weights (Percent) 
Mining and Metals 
Gold 
Forestry and Paper 
Chemicals 
Energy Reserves 
Oil Refining 
Oil Services 
Food and Beverages 
Alcohol 
Tobacco 
Home Products 
Grocery Stores 
Consumer Durables 
Motor Vehicles and Parts 
Apparel and Textiles 
Clothing Stores 
Specialty Retail 
Department Stores 
Constructn. and Real Prop. 
Publishing 
Media 
Hotels 
Restaurants 
Entertainment 
Leisure 
Environmental Services 
Heavy Electrical Eqp. 
Mgd. Bmk. 
Act. 
Mgd. 
Bmk. 
Act. 
0.022 
0.000 
0.000 
1.717 
4.490 
3.770 
0.977 
0.823 
0.365 
3.197 
0.648 
0.636 
0.000 
0.454 
0.141 
0.374 
0.025 
3.375 
9.813 
0.326 
0.358 
0.067 
0.000 
0.675 
0.000 
0.000 
1.303 
0.606 
0.161 
0.871 
2.046 
4.297
1.417
0.620
3.780 
0.515 
0.732
2.435 
0.511
0.166 
0.621 
0.373 
0.341
2.721 
3.606 
0.288
0.778 
1.498 
0.209 
0.542 
1.630 
0.409 
0.220 
1.949 
−0.585 
−0.161 
−0.871 
−0.329 
0.193 
2.353 
0.357 
−2.956 
−0.151 
2.465 
−1.787 
0.125 
−0.166 
−0.167 
−0.232 
0.033 
−2.696 
−0.231 
9.526 
−0.452 
−1.140 
−0.141 
−0.542 
−0.955 
−0.409 
−0.220 
−0.647 
Heavy Machinery 
Industrial Parts 
Electric Utility 
Gas Utilities 
Railroads 
Airlines 
Truck/Sea/Air Freight 
Medical Services 
Medical Products 
Drugs 
Electronic Equipment 
Semiconductors 
Computer Hardware 
Computer Software 
Defense and Aerospace 
Telephone 
Wireless Telecom. 
Information Services 
Industrial Services 
Life/health Insurance 
Property/Casualty Ins. 
Banks 
Thrifts 
Securities and Asst. Mgmt. 
Financial Services 
Internet 
Equity REIT 
0.000
 0.141 −0.141 
1.366
 1.469 −0.103 
4.221
 1.956
 2.265 
0.204
 0.456 −0.252 
0.185
 0.373 −0.189 
0.000
 0.206 −0.206 
0.000
 0.162 −0.162 
0.000
 0.789 −0.789 
1.522
 3.599 −2.077 
7.301 10.000 −2.699 
0.525
 1.985 −1.460 
3.227
 4.509 −1.282 
2.904
 4.129 −1.224 
7.304
 6.256
 1.048 
1.836
 1.336
 0.499 
6.290
 3.680
 2.610 
2.144
 1.565
 0.580 
0.921
 2.698 −1.777 
0.230
 0.670 −0.440 
1.987
 0.938
 1.048 
4.844
 2.541
 2.304 
8.724
 7.580
 1.144 
0.775
 0.362
 0.413 
3.988
 2.017
 1.971 
5.510
 6.321 −0.811 
0.434
 0.725 −0.291 
0.000
 0.193 −0.193 
Note: Mgd = Managed; Bmk = S&P 500 (the benchmark); Act = Active = Managed 
− Benchmark 
Source: Exhibit 13.11 in Frank J. Fabozzi, Frank J. Jones, and Raman Vardharaj, 
“Multi-Factor Risk Models,” Chapter 13 in Frank J. Fabozzi and Harry M. 
Markowitz (eds.), The Theory and Practice of Investment Management (Hobo-
ken, NJ: John Wiley & Sons, 2002). 

591
Equity Portfolio Management 
■ Practitioners view categories of stocks with similar historical perfor-
mance as a “style” of investing with the two main style categories 
being growth and value. 
■ There are methodologies for classifying stocks into style categories. 
■ There are two types of passive strategies: a buy-and-hold strategy and 
an indexing strategy with the latter being the more common strategy 
pursued by institutional investors.
 ■ In constructing the tracking or indexed portfolio a manager can use the 
capitalization approach which involves either purchasing all stock 
issues included in the benchmark index in proportion to their weight-
ings or purchasing a number of the largest capitalized names in the 
benchmark index and equally distributes the residual stock weighting 
across the other issues in the benchmark index.
 ■ Two approaches to construct an indexed portfolio with fewer stock 
issues than the benchmark index are the cellular (or stratified sampling) 
method and the multifactor risk model method.
 ■ The “fundamental law of active management” explains how the infor-
mation ratio changes as a function of the depth of an active manager’s 
skill and the breadth or number of independent insights or investment 
opportunities.
 ■ Technical analysis strategies are active management strategies whose 
overlying principle is to detect changes in the supply of and demand for 
a stock and capitalize on the expected changes.
 ■ Technical analysis has taken a more scientific twist with the develop-
ment of nonlinear dynamics and chaos theory.
 ■ Market-neutral strategies seek a positive return regardless of market 
conditions. A typical way to achieve this result is by constructing an 
appropriate portfolio consisting of long and short equity positions.
 ■ Statistical arbitrage is a new methodology for managing long-short 
equity portfolios based on finding stable trends that signal profit 
opportunities.
 ■ Multifactor risk models permit the decomposition of risk in order to 
assess the potential performance of a portfolio to the risk factors, the 
potential performance of a portfolio relative to a benchmark, and the 
actual performance of a portfolio relative to a benchmark
 ■ In risk decomposition, the total return is first divided into the risk-free 
return and the total excess return (the difference between the actual 
return realized by the portfolio and the risk-free return); the total 
excess risk is further partitioned into specific/common risks, system-
atic/residual risks, and benchmark/active risks. 


