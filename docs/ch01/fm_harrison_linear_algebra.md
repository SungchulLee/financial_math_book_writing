# Linear Algebra for Finance

!!! info "Source"
    **Mathematical Economics and Finance** by Michael Harrison and Patrick Waldron, 1998.
    These notes are used for educational purposes.

## Linear Algebra

CHAPTER 1. LINEAR ALGEBRA
3
Chapter 1
LINEAR ALGEBRA
1.1
Introduction
[To be written.]
1.2
Systems of Linear Equations and Matrices
Why are we interested in solving simultaneous equations?
We often have to find a point which satisfies more than one equation simultane-
ously, for example when finding equilibrium price and quantity given supply and
demand functions.
• To be an equilibrium, the point (Q, P) must lie on both the supply and
demand curves.
• Now both supply and demand curves can be plotted on the same diagram
and the point(s) of intersection will be the equilibrium (equilibria):
• solving for equilibrium price and quantity is just one of many examples of
the simultaneous equations problem
• The ISLM model is another example which we will soon consider at length.
• We will usually have many relationships between many economic variables
defining equilibrium.
The first approach to simultaneous equations is the equation counting approach:
Revised: December 2, 1998

4
1.2. SYSTEMS OF LINEAR EQUATIONS AND MATRICES
• a rough rule of thumb is that we need the same number of equations as
unknowns
• this is neither necessary nor sufficient for existence of a unique solution,
e.g.
– fewer equations than unknowns, unique solution:
x2 + y2 = 0 ⇒x = 0, y = 0
– same number of equations and unknowns but no solution (dependent
equations):
x + y
=
1
x + y
=
2
– more equations than unknowns, unique solution:
x
=
y
x + y
=
2
x −2y + 1
=
0
⇒x = 1,
y = 1
Now consider the geometric representation of the simultaneous equation problem,
in both the generic and linear cases:
• two curves in the coordinate plane can intersect in 0, 1 or more points
• two surfaces in 3D coordinate space typically intersect in a curve
• three surfaces in 3D coordinate space can intersect in 0, 1 or more points
• a more precise theory is needed
There are three types of elementary row operations which can be performed on a
system of simultaneous equations without changing the solution(s):
1. Add or subtract a multiple of one equation to or from another equation
2. Multiply a particular equation by a non-zero constant
3. Interchange two equations
Revised: December 2, 1998

CHAPTER 1. LINEAR ALGEBRA
5
Note that each of these operations is reversible (invertible).
Our strategy, roughly equating to Gaussian elimination involves using elementary
row operations to perform the following steps:
1.
(a) Eliminate the first variable from all except the first equation
(b) Eliminate the second variable from all except the first two equations
(c) Eliminate the third variable from all except the first three equations
(d) &c.
2. We end up with only one variable in the last equation, which is easily solved.
3. Then we can substitute this solution in the second last equation and solve
for the second last variable, and so on.
4. Check your solution!!
Now, let us concentrate on simultaneous linear equations:
(2 × 2 EXAMPLE)
x + y
=
2
(1.2.1)
2y −x
=
7
(1.2.2)
• Draw a picture
• Use the Gaussian elimination method instead of the following
• Solve for x in terms of y
x
=
2 −y
x
=
2y −7
• Eliminate x
2 −y = 2y −7
• Find y
3y
=
9
y
=
3
• Find x from either equation:
x
=
2 −y = 2 −3 = −1
x
=
2y −7 = 6 −7 = −1
Revised: December 2, 1998

6
1.2. SYSTEMS OF LINEAR EQUATIONS AND MATRICES
SIMULTANEOUS LINEAR EQUATIONS (3 × 3 EXAMPLE)
• Consider the general 3D picture .. .
• Example:
x + 2y + 3z
=
6
(1.2.3)
4x + 5y + 6z
=
15
(1.2.4)
7x + 8y + 10z
=
25
(1.2.5)
• Solve one equation (1.2.3) for x in terms of y and z:
x = 6 −2y −3z
• Eliminate x from the other two equations:
4 (6 −2y −3z) + 5y + 6z
=
15
7 (6 −2y −3z) + 8y + 10z
=
25
• What remains is a 2 × 2 system:
−3y −6z
=
−9
−6y −11z
=
−17
• Solve each equation for y:
y
=
3 −2z
y
=
17
6 −11
6 z
• Eliminate y:
3 −2z = 17
6 −11
6 z
• Find z:
1
6
=
1
6z
z
=
1
• Hence y = 1 and x = 1.
Revised: December 2, 1998

CHAPTER 1. LINEAR ALGEBRA
7
1.3
Matrix Operations
We motivate the need for matrix algebra by using it as a shorthand for writing
systems of linear equations, such as those considered above.
• The steps taken to solve simultaneous linear equations involve only the co-
efficients so we can use the following shorthand to represent the system of
equations used in our example:
This is called a matrix, i.e.— a rectangular array of numbers.
• We use the concept of the elementary matrix to summarise the elementary
row operations carried out in solving the original equations:
(Go through the whole solution step by step again.)
• Now the rules are
– Working column by column from left to right, change all the below
diagonal elements of the matrix to zeroes
– Working row by row from bottom to top, change the right of diagonal
elements to 0 and the diagonal elements to 1
– Read off the solution from the last column.
• Or we can reorder the steps to give the Gaussian elimination method:
column by column everywhere.
1.4
Matrix Arithmetic
• Two n × m matrices can be added and subtracted element by element.
• There are three notations for the general 3×3 system of simultaneous linear
equations:
1. ‘Scalar’ notation:
a11x1 + a12x2 + a13x3
=
b1
a21x1 + a22x2 + a23x3
=
b2
a31x1 + a32x2 + a33x3
=
b3
Revised: December 2, 1998

8
1.4. MATRIX ARITHMETIC
2. ‘Vector’ notation without factorisation:



a11x1 + a12x2 + a13x3
a21x1 + a22x2 + a23x3
a31x1 + a32x2 + a33x3


=



b1
b2
b3



3. ‘Vector’ notation with factorisation:



a11
a12
a13
a21
a22
a23
a31
a32
a33






x1
x2
x3


=



b1
b2
b3



It follows that:



a11
a12
a13
a21
a22
a23
a31
a32
a33






x1
x2
x3


=



a11x1 + a12x2 + a13x3
a21x1 + a22x2 + a23x3
a31x1 + a32x2 + a33x3



• From this we can deduce the general multiplication rules:
The ijth element of the matrix product AB is the product of the
ith row of A and the jth column of B.
A row and column can only be multiplied if they are the same
‘length.’
In that case, their product is the sum of the products of corre-
sponding elements.
Two matrices can only be multiplied if the number of columns
(i.e. the row lengths) in the first equals the number of rows (i.e.
the column lengths) in the second.
• The scalar product of two vectors in ℜn is the matrix product of one written
as a row vector (1×n matrix) and the other written as a column vector (n×1
matrix).
• This is independent of which is written as a row and which is written as a
column.
So we have C = AB if and only if cij =
P k = 1naikbkj.
Note that multiplication is associative but not commutative.
Other binary matrix operations are addition and subtraction.
Addition is associative and commutative. Subtraction is neither.
Matrices can also be multiplied by scalars.
Both multiplications are distributive over addition.
Revised: December 2, 1998

CHAPTER 1. LINEAR ALGEBRA
9
We now move on to unary operations.
The additive and multiplicative identity matrices are respectively 0 and In ≡

δi
j

.
−A and A−1 are the corresponding inverse. Only non-singular matrices have
multiplicative inverses.
Finally, we can interpret matrices in terms of linear transformations.
• The product of an m × n matrix and an n × p matrix is an m × p matrix.
• The product of an m × n matrix and an n × 1 matrix (vector) is an m × 1
matrix (vector).
• So every m × n matrix, A, defines a function, known as a linear transfor-
mation,
TA : ℜn →ℜm : x 7→Ax,
which maps n−dimensional vectors to m−dimensional vectors.
• In particular, an n×n square matrix defines a linear transformation mapping
n−dimensional vectors to n−dimensional vectors.
• The system of n simultaneous linear equations in n unknowns
Ax = b
has a unique solution ∀b if and only if the corresponding linear transfor-
mation TA is an invertible or bijective function: A is then said to be an
invertible matrix.
A matrix has an inverse if and only the corresponding linear transformation is an
invertible function:
• Suppose Ax = b0 does not have a unique solution. Say it has two distinct
solutions, x1 and x2 (x1 ̸= x2):
Ax1
=
b0
Ax2
=
b0
This is the same thing as saying that the linear transformation TA is not
injective, as it maps both x1 and x2 to the same image.
• Then whenever x is a solution of Ax = b:
A (x + x1 −x2)
=
Ax + Ax1 −Ax2
=
b + b0 −b0
=
b,
so x + x1 −x2 is another, different, solution to Ax = b.
Revised: December 2, 1998

10
1.4. MATRIX ARITHMETIC
• So uniqueness of solution is determined by invertibility of the coefficient
matrix A independent of the right hand side vector b.
• If A is not invertible, then there will be multiple solutions for some values
of b and no solutions for other values of b.
So far, we have seen two notations for solving a system of simultaneous linear
equations, both using elementary row operations.
1. We applied the method to scalar equations (in x, y and z).
2. We then applied it to the augmented matrix (A b) which was reduced to the
augmented matrix (I x).
Now we introduce a third notation.
3. Each step above (about six of them depending on how things simplify)
amounted to premultiplying the augmented matrix by an elementary ma-
trix, say
E6E5E4E3E2E1 (A b) = (I x) .
(1.4.1)
Picking out the first 3 columns on each side:
E6E5E4E3E2E1A = I.
(1.4.2)
We define
A−1 ≡E6E5E4E3E2E1.
(1.4.3)
And we can use Gaussian elimination in turn to solve for each of the columns
of the inverse, or to solve for the whole thing at once.
Lots of properties of inverses are listed in MJH’s notes (p.A7?).
The transpose is A⊤, sometimes denoted A′ or At.
A matrix is symmetric if it is its own transpose; skewsymmetric if A⊤= −A.
Note that

A⊤−1 = (A−1)⊤.
Lots of strange things can happen in matrix arithmetic.
We can have AB = 0 even if A ̸= 0 and B ̸= 0.
Definition 1.4.1 orthogonal rows/columns
Definition 1.4.2 idempotent matrix A2 = A
Definition 1.4.3 orthogonal1 matrix A⊤= A−1.
Definition 1.4.4 partitioned matrices
Definition 1.4.5 determinants
Definition 1.4.6 diagonal, triangular and scalar matrices
1This is what ? calls something that it seems more natural to call an orthonormal matrix.
Revised: December 2, 1998

CHAPTER 1. LINEAR ALGEBRA
11
1.5
Vectors and Vector Spaces
Definition 1.5.1 A vector is just an n × 1 matrix.
The Cartesian product of n sets is just the set of ordered n-tuples where the ith
component of each n-tuple is an element of the ith set.
The ordered n-tuple (x1, x2, . . . , xn) is identified with the n × 1 column vector






x1
x2
...
xn





.
Look at pictures of points in ℜ2 and ℜ3 and think about extensions to ℜn.
Another geometric interpretation is to say that a vector is an entity which has both
magnitude and direction, while a scalar is a quantity that has magnitude only.
Definition 1.5.2 A real (or Euclidean) vector space is a set (of vectors) in which
addition and scalar multiplication (i.e. by real numbers) are defined and satisfy
the following axioms:
1. copy axioms from simms 131 notes p.1
There are vector spaces over other fields, such as the complex numbers.
Other examples are function spaces, matrix spaces.
On some vector spaces, we also have the notion of a dot product or scalar product:
u.v ≡u⊤v
The Euclidean norm of u is
√u.u ≡∥u ∥.
A unit vector is defined in the obvious way . . .unit norm.
The distance between two vectors is just ∥u −v ∥.
There are lots of interesting properties of the dot product (MJH’s theorem 2).
We can calculate the angle between two vectors using a geometric proof based on
the cosine rule.
∥v −u ∥2
=
(v −u) . (v −u)
(1.5.1)
=
∥v ∥2 + ∥u ∥2 −2v.u
(1.5.2)
=
∥v ∥2 + ∥u ∥2 −2 ∥v ∥∥u ∥cos θ
(1.5.3)
Two vectors are orthogonal if and only if the angle between them is zero.
Revised: December 2, 1998

12
1.6. LINEAR INDEPENDENCE
A subspace is a subset of a vector space which is closed under addition and scalar
multiplication.
For example, consider row space, column space, solution space, orthogonal com-
plement.
1.6
Linear Independence
Definition 1.6.1 The vectors x1, x2, x3, . . . , xr ∈ℜn are linearly independent if
and only if
r
X
i=1
αixi = 0 ⇒αi = 0∀i.
Otherwise, they are linearly dependent.
Give examples of each, plus the standard basis.
If r > n, then the vectors must be linearly dependent.
If the vectors are orthonormal, then they must be linearly independent.
1.7
Bases and Dimension
A basis for a vector space is a set of vectors which are linearly independent and
which span or generate the entire space.
Consider the standard bases in ℜ2 and ℜn.
Any two non-collinear vectors in ℜ2 form a basis.
A linearly independent spanning set is a basis for the subspace which it generates.
Proof of the next result requires stuff that has not yet been covered.
If a basis has n elements then any set of more than n elements is linearly dependent
and any set of less than n elements doesn’t span.
Or something like that.
Definition 1.7.1 The dimension of a vector space is the (unique) number of vec-
tors in a basis. The dimension of the vector space {0} is zero.
Definition 1.7.2 Orthogonal complement
Decomposition into subspace and its orthogonal complement.
Revised: December 2, 1998

CHAPTER 1. LINEAR ALGEBRA
13
1.8
Rank
Definition 1.8.1
The row space of an m × n matrix A is the vector subspace of ℜn generated by
the m rows of A.
The row rank of a matrix is the dimension of its row space.
The column space of an m × n matrix A is the vector subspace of ℜm generated
by the n columns of A.
The column rank of a matrix is the dimension of its column space.
Theorem 1.8.1 The row space and the column space of any matrix have the same
dimension.
Proof The idea of the proof is that performing elementary row operations on a
matrix does not change either the row rank or the column rank of the matrix.
Using a procedure similar to Gaussian elimination, every matrix can be reduced to
a matrix in reduced row echelon form (a partitioned matrix with an identity matrix
in the top left corner, anything in the top right corner, and zeroes in the bottom left
and bottom right corner).
By inspection, it is clear that the row rank and column rank of such a matrix are
equal to each other and to the dimension of the identity matrix in the top left
corner.
In fact, elementary row operations do not even change the row space of the matrix.
They clearly do change the column space of a matrix, but not the column rank as
we shall now see.
If A and B are row equivalent matrices, then the equations Ax = 0 and Bx = 0
have the same solution space.
If a subset of columns of A are linearly dependent, then the solution space does
contain a vector in which the corresponding entries are nonzero and all other en-
tries are zero.
Similarly, if a subset of columns of A are linearly independent, then the solution
space does not contain a vector in which the corresponding entries are nonzero
and all other entries are zero.
The first result implies that the corresponding columns or B are also linearly de-
pendent.
The second result implies that the corresponding columns of B are also linearly
independent.
It follows that the dimension of the column space is the same for both matrices.
Q.E.D.
Revised: December 2, 1998

14
1.9. EIGENVALUES AND EIGENVECTORS
Definition 1.8.2 rank
Definition 1.8.3 solution space, null space or kernel
Theorem 1.8.2 dimension of row space + dimension of null space = number of
columns
The solution space of the system means the solution space of the homogenous
equation Ax = 0.
The non-homogenous equation Ax = b may or may not have solutions.
System is consistent iff rhs is in column space of A and there is a solution.
Such a solution is called a particular solution.
A general solution is obtained by adding to some particular solution a generic
element of the solution space.
Previously, solving a system of linear equations was something we only did with
non-singular square systems.
Now, we can solve any system by describing the solution space.
1.9
Eigenvalues and Eigenvectors
Definition 1.9.1 eigenvalues and eigenvectors and λ-eigenspaces
Compute eigenvalues using det (A −λI) = 0. So some matrices with real entries
can have complex eigenvalues.
Real symmetric matrix has real eigenvalues. Prove using complex conjugate ar-
gument.
Given an eigenvalue, the corresponding eigenvector is the solution to a singular
matrix equation, so one free parameter (at least).
Often it is useful to specify unit eigenvectors.
Eigenvectors of a real symmetric matrix corresponding to different eigenvalues
are orthogonal (orthonormal if we normalise them).
So we can diagonalize a symmetric matrix in the following sense:
If the columns of P are orthonormal eigenvectors of A, and λ is the matrix with
the corresponding eigenvalues along its leading diagonal, then AP = Pλ so
P−1AP = λ = P⊤AP as P is an orthogonal matrix.
In fact, all we need to be able to diagonalise in this way is for A to have n linearly
independent eigenvectors.
P−1AP and A are said to be similar matrices.
Two similar matrices share lots of properties: determinants and eigenvalues in
particular. Easy to show this.
But eigenvectors are different.
Revised: December 2, 1998

CHAPTER 1. LINEAR ALGEBRA
15
1.10
Quadratic Forms
A quadratic form is
1.11
Symmetric Matrices
Symmetric matrices have a number of special properties
1.12
Definite Matrices
Definition 1.12.1 An n × n square matrix A is said to be
positive definite
⇐⇒
x⊤Ax > 0 ∀x ∈ℜn, x ̸= 0
positive semi-definite
⇐⇒
x⊤Ax ≥0 ∀x ∈ℜn
negative definite
⇐⇒
x⊤Ax < 0 ∀x ∈ℜn, x ̸= 0
negative semi-definite
⇐⇒
x⊤Ax ≤0 ∀x ∈ℜn
Some texts may require that the matrix also be symmetric, but this is not essential
and sometimes looking at the definiteness of non-symmetric matrices is relevant.
If P is an invertible n × n square matrix and A is any n × n square matrix, then
A is positive/negative (semi-)definite if and only if P−1AP is.
In particular, the definiteness of a symmetric matrix can be determined by check-
ing the signs of its eigenvalues.
Other checks involve looking at the signs of the elements on the leading diagonal.
Definite matrices are non-singular and singular matrices can not be definite.
The commonest use of positive definite matrices is as the variance-covariance
matrices of random variables. Since
vij = Cov [˜ri, ˜rj] = Cov [˜rj, ˜ri]
(1.12.1)
and
w⊤Vw
=
N
X
i=1
N
X
j=1
wiwjCov [˜ri, ˜rj]
(1.12.2)
=
Cov


N
X
i=1
wi˜ri,
N
X
j=1
wj˜rj


(1.12.3)
=
Var[
N
X
i=1
wi˜ri] ≥0
(1.12.4)
a variance-covariance matrix must be real, symmetric and positive semi-definite.
Revised: December 2, 1998

16
1.12. DEFINITE MATRICES
In Theorem 3.2.4, it will be seen that the definiteness of a matrix is also an essen-
tial idea in the theory of convex functions.
We will also need later the fact that the inverse of a positive (negative) definite
matrix (in particular, of a variance-covariance matrix) is positive (negative) defi-
nite.
Semi-definite matrices which are not definite have a zero eigenvalue and therefore
are singular.
Revised: December 2, 1998


## Vector Calculus

CHAPTER 2. VECTOR CALCULUS
17
Chapter 2
VECTOR CALCULUS
2.1
Introduction
[To be written.]
2.2
Basic Topology
The aim of this section is to provide sufficient introduction to topology to motivate
the definitions of continuity of functions and correspondences in the next section,
but no more.
• A metric space is a non-empty set X equipped with a metric, i.e. a function
d : X × X →[0, ∞) such that
1. d(x, y) = 0 ⇐⇒x = y.
2. d(x, y) = d(y, x) ∀x, y ∈X.
3. The triangular inequality:
d(x, z) + d(z, y) ≥d(x, y) ∀x, y, z ∈X.
• An open ball is a subset of a metric space, X, of the form
Bϵ(x) = {y ∈X : d(y, x) < ϵ}.
• A subset A of a metric space is open
⇐⇒
∀x ∈A, ∃ϵ > 0 such that Bϵ(x) ⊆A.
Revised: December 2, 1998

18
2.3. VECTOR-VALUED FUNCTIONS AND FUNCTIONS OF SEVERAL
VARIABLES
• A is closed ⇐⇒X −A is open. (Note that many sets are neither open nor
closed.)
• A neighbourhood of x ∈X is an open set containing x.
Definition 2.2.1 Let X = ℜn. A ⊆X is compact ⇐⇒A is both closed and
bounded (i.e. ∃x, ϵ such that A ⊆Bϵ(x)).
We need to formally define the interior of a set before stating the separating theo-
rem:
Definition 2.2.2 If Z is a subset of a metric space X, then the interior of Z,
denoted int Z, is defined by
z ∈int Z ⇐⇒Bϵ (z) ⊆Z for some ϵ > 0.
2.3
Vector-valued Functions and Functions of Sev-
eral Variables
Definition 2.3.1 A function (or map) f : X →Y from a domain X to a co-
domain Y is a rule which assigns to each element of X a unique element of Y .
Definition 2.3.2 A correspondence f : X →Y from a domain X to a co-domain
Y is a rule which assigns to each element of X a non-empty subset of Y .
Definition 2.3.3 The range of the function f : X →Y is the set f(X) = {f(x) ∈
Y : x ∈X}.
Definition 2.3.4 The function f : X →Y is injective (one-to-one)
⇐⇒
f(x) = f(x′) ⇒x = x′.
Definition 2.3.5 The function f : X →Y is surjective (onto)
⇐⇒
f(X) = Y
Definition 2.3.6 The function f : X →Y is bijective (or invertible)
⇐⇒
it is both injective and surjective.
Revised: December 2, 1998

CHAPTER 2. VECTOR CALCULUS
19
Note that if f: X →Y and A ⊆X and B ⊆Y , then
f (A) ≡{f (x) : x ∈A} ⊆Y
and
f −1 (B) ≡{x ∈X: f (x) ∈B} ⊆X.
Definition 2.3.7 A vector-valued function is a function whose co-domain is a sub-
set of a vector space, say ℜN. Such a function has N component functions.
Definition 2.3.8 A function of several variables is a function whose domain is a
subset of a vector space.
Definition 2.3.9 The function f: X →Y (X ⊆ℜn, Y ⊆ℜ) approaches the limit
y∗as x →x∗
⇐⇒
∀ϵ > 0, ∃δ > 0 s.t. ∥x −x∗∥< δ =⇒|f(x) −y∗)| < ϵ.
This is usually denoted
lim
x→x∗f(x) = y∗.
Definition 2.3.10 The function f: X →Y (X ⊆ℜn, Y ⊆ℜ) is continuous at x∗
⇐⇒
∀ϵ > 0, ∃δ > 0 s.t. ∥x −x∗∥< δ =⇒|f(x) −f(x∗)| < ϵ.
This definition just says that f is continuous provided that
lim
x→x∗f(x) = f(x∗).
? discusses various alternative but equivalent definitions of continuity.
Definition 2.3.11 The function f : X →Y is continuous
⇐⇒
it is continuous at every point of its domain.
We will say that a vector-valued function is continuous if and only if each of its
component functions is continuous.
The notion of continuity of a function described above is probably familiar from
earlier courses. Its extension to the notion of continuity of a correspondence,
however, while fundamental to consumer theory, general equilibrium theory and
much of microeconomics, is probably not. In particular, we will meet it again in
Theorem 3.5.4. The interested reader is referred to ? for further details.
Revised: December 2, 1998

20
2.4. PARTIAL AND TOTAL DERIVATIVES
Definition 2.3.12
1. The correspondence f: X →Y (X ⊆ℜn, Y ⊆ℜ) is
upper hemi-continuous (u.h.c.) at x∗
⇐⇒
for every open set N containing the set f(x∗), ∃δ > 0 s.t. ∥x −x∗∥<
δ =⇒f(x) ⊆N.
(Upper hemi-continuity basically means that the graph of the correspon-
dence is a closed and connected set.)
2. The correspondence f: X →Y (X ⊆ℜn, Y ⊆ℜ) is lower hemi-continuous
(l.h.c.) at x∗
⇐⇒
for every open set N intersecting the set f(x∗), ∃δ > 0 s.t. ∥x −x∗∥<
δ =⇒f(x) intersects N.
3. The correspondence f: X →Y (X ⊆ℜn, Y ⊆ℜ) is continuous (at x∗)
⇐⇒
it is both upper hemi-continuous and lower hemi-continuous (at x∗)
(There are a couple of pictures from ? to illustrate these definitions.)
2.4
Partial and Total Derivatives
Definition 2.4.1 The (total) derivative or Jacobean of a real-valued function of N
variables is the N-dimensional row vector of its partial derivatives. The Jacobean
of a vector-valued function with values in ℜM is an M × N matrix of partial
derivatives whose jth row is the Jacobean of the jth component function.
Definition 2.4.2 The gradient of a real-valued function is the transpose of its Ja-
cobean.
Definition 2.4.3 A function is said to be differentiable at x if all its partial deriva-
tives exist at x.
Definition 2.4.4 The function f : X →Y is differentiable
⇐⇒
it is differentiable at every point of its domain
Definition 2.4.5 The Hessian matrix of a real-valued function is the (usually sym-
metric) square matrix of its second order partial derivatives.
Revised: December 2, 1998

CHAPTER 2. VECTOR CALCULUS
21
Note that if f: ℜn →ℜ, then, strictly speaking, the second derivative (Hessian) of
f is the derivative of the vector-valued function
(f ′)⊤: ℜn →ℜn: x 7→(f ′ (x))⊤.
Students always need to be warned about the differences in notation between the
case of n = 1 and the case of n > 1. Statements and shorthands that make sense
in univariate calculus must be modified for multivariate calculus.
2.5
The Chain Rule and Product Rule
Theorem 2.5.1 (The Chain Rule) Let g: ℜn →ℜm and f: ℜm →ℜp be contin-
uously differentiable functions and let h: ℜn →ℜp be defined by
h (x) ≡f (g (x)) .
Then
h′ (x)
| {z }
p×n
= f ′ (g (x))
|
{z
}
p×m
g′ (x)
| {z }
m×n
.
Proof This is easily shown using the Chain Rule for partial derivatives.
Q.E.D.
One of the most common applications of the Chain Rule is the following:
Let g: ℜn →ℜm and f: ℜm+n →ℜp be continuously differentiable functions, let
x ∈ℜn, and define h: ℜn →ℜp by:
h (x) ≡f (g (x) , x) .
The univariate Chain Rule can then be used to calculate ∂hi
∂xj (x) in terms of partial
derivatives of f and g for i = 1, . . . , p and j = 1, . . . , n:
∂hi
∂xj
(x) =
m
X
k=1
∂f i
∂xk
(g (x) , x) ∂gk
∂xj
(x) +
m+n
X
k=m+1
∂f i
∂xk
(g (x) , x) ∂xk
∂xj
(x) . (2.5.1)
Note that
∂xk
∂xj
(x) = δk
j ≡
 1
if k = j
0
otherwise ,
which is known as the Kronecker Delta. Thus all but one of the terms in the second
summation in (2.5.1) vanishes, giving:
∂hi
∂xj
(x) =
m
X
k=1
∂f i
∂xk
(g (x) , x) ∂gk
∂xj
(x) + ∂f i
∂xj
(g (x) , x) .
Revised: December 2, 1998

22
2.5. THE CHAIN RULE AND PRODUCT RULE
Stacking these scalar equations in matrix form and factoring yields:




∂h1
∂x1 (x)
. . .
∂h1
∂xn (x)
...
...
...
∂hp
∂x1 (x)
. . .
∂hp
∂xn (x)



=




∂f1
∂x1 (g (x) , x)
. . .
∂f1
∂xm (g (x) , x)
...
...
...
∂fp
∂x1 (g (x) , x)
. . .
∂fp
∂xm (g (x) , x)








∂g1
∂x1 (x)
. . .
∂g1
∂xn (x)
...
...
...
∂gm
∂x1 (x)
. . .
∂gm
∂xn (x)




+





∂f1
∂xm+1 (g (x) , x)
. . .
∂f1
∂xm+n (g (x) , x)
...
...
...
∂fp
∂xm+1 (g (x) , x)
. . .
∂fp
∂xm+n (g (x) , x)




.
(2.5.2)
Now, by partitioning the total derivative of f as
f ′ (·)
| {z }
p×(m+n)
=

Dgf (·)
|
{z
}
p×m
Dxf (·)
|
{z
}
p×n

,
(2.5.3)
we can use (2.5.2) to write out the total derivative h′ (x) as a product of partitioned
matrices:
h′ (x) = Dgf (g (x) , x) g′ (x) + Dxf (g (x) , x) .
(2.5.4)
Theorem 2.5.2 (Product Rule for Vector Calculus) The multivariate Product Rule
comes in two versions:
1. Let f, g: ℜm →ℜn and define h: ℜm →ℜby
h (x)
| {z }
1×1
≡(f (x))⊤
|
{z
}
1×n
g (x)
| {z }
n×1
.
Then
h′ (x)
| {z }
1×m
= (g (x))⊤
|
{z
}
1×n
f ′ (x)
| {z }
n×m
+ (f (x))⊤
|
{z
}
1×n
g′ (x)
| {z }
n×m
.
2. Let f: ℜm →ℜand g: ℜm →ℜn and define h: ℜm →ℜn by
h (x)
| {z }
n×1
≡f (x)
| {z }
1×1
g (x)
| {z }
n×1
.
Then
h′ (x)
| {z }
n×m
= g (x)
| {z }
n×1
f ′ (x)
| {z }
1×m
+ f (x)
| {z }
1×1
g′ (x)
| {z }
n×m
.
Proof This is easily shown using the Product Rule from univariate calculus to
calculate the relevant partial derivatives and then stacking the results in matrix
form.
Q.E.D.
Revised: December 2, 1998

CHAPTER 2. VECTOR CALCULUS
23
2.6
The Implicit Function Theorem
Theorem 2.6.1 (Implicit Function Theorem) Let g: ℜn →ℜm, where m < n.
Consider the system of m scalar equations in n variables, g (x∗) = 0m.
Partition the n-dimensional vector x as (y, z) where y = (x1, x2, . . . , xm) is m-
dimensional and z = (xm+1, xm+2, . . . , xn) is (n −m)-dimensional. Similarly,
partition the total derivative of g at x∗as
g′ (x∗)
=
[Dyg
Dzg]
(m × n)
(m × m)
(m × (n −m))
(2.6.1)
We aim to solve these equations for the first m variables, y, which will then be
written as functions, h (z) of the last n −m variables, z.
Suppose g is continuously differentiable in a neighbourhood of x∗, and that the
m × m matrix:
Dyg ≡




∂g1
∂x1 (x∗)
. . .
∂g1
∂xm (x∗)
...
...
...
∂gm
∂x1 (x∗)
. . .
∂gm
∂xm (x∗)




formed by the first m columns of the total derivative of g at x∗is non-singular.
Then ∃neighbourhoods Y of y∗and Z of z∗, and a continuously differentiable
function h: Z →Y such that
1. y∗= h (z∗),
2. g (h (z) , z) = 0
∀z ∈Z, and
3. h′ (z∗) = −(Dyg)−1 Dzg.
Proof The full proof of this theorem, like that of Brouwer’s Fixed Point Theorem
later, is beyond the scope of this course. However, part 3 follows easily from
material in Section 2.5. The aim is to derive an expression for the total derivative
h′ (z∗) in terms of the partial derivatives of g, using the Chain Rule.
We know from part 2 that
f (z) ≡g (h (z) , z) = 0m
∀z ∈Z.
Thus
f ′ (z) ≡0m×(n−m)
∀z ∈Z,
in particular at z∗. But we know from (2.5.4) that
f ′ (z) = Dygh′ (z) + Dzg.
Revised: December 2, 1998

24
2.7. DIRECTIONAL DERIVATIVES
Hence
Dygh′ (z) + Dzg = 0m×(n−m)
and, since the statement of the theorem requires that Dyg is invertible,
h′ (z∗) = −(Dyg)−1 Dzg,
as required.
Q.E.D.
To conclude this section, consider the following two examples:
1. the equation g (x, y) ≡x2 + y2 −1 = 0.
Note that g′ (x, y) = (2x 2y).
We have h(y) = √1 −y2 or h(y) = −√1 −y2, each of which describes a
single-valued, differentiable function on (−1, 1). At (x, y) = (0, 1), ∂g
∂x =
0 and h(y) is undefined (for y > 1) or multi-valued (for y < 1) in any
neighbourhood of y = 1.
2. the system of linear equations g (x) ≡Bx = 0, where B is an m × n
matrix.
We have g′ (x) = B
∀x so the implicit function theorem applies provided
the equations are linearly independent.
2.7
Directional Derivatives
Definition 2.7.1 Let X be a vector space and x ̸= x′ ∈X. Then
1. for λ ∈ℜand particularly for λ ∈[0, 1], λx+(1 −λ) x′ is called a convex
combination of x and x′.
2. L = {λx + (1 −λ) x′ : λ ∈ℜ} is the line from x′, where λ = 0, to x,
where λ = 1, in X.
3. The restriction of the function f: X →ℜto the line L is the function
f|L: ℜ→ℜ: λ 7→f (λx + (1 −λ) x′) .
4. If f is a differentiable function, then the directional derivative of f at x′ in
the direction from x′ to x is f|′
L (0).
Revised: December 2, 1998

CHAPTER 2. VECTOR CALCULUS
25
• We will endeavour, wherever possible, to stick to the convention that x′
denotes the point at which the derivative is to be evaluated and x denotes
the point in the direction of which it is measured.1
• Note that, by the Chain Rule,
f|′
L (λ) = f ′ (λx + (1 −λ) x′) (x −x′)
(2.7.1)
and hence the directional derivative
f|′
L (0) = f ′ (x′) (x −x′) .
(2.7.2)
• The ith partial derivative of f at x is the directional derivative of f at x in
the direction from x to x + ei, where ei is the ith standard basis vector. In
other words, partial derivatives are a special case of directional derivatives
or directional derivatives a generalisation of partial derivatives.
• As an exercise, consider the interpretation of the directional derivatives at a
point in terms of the rescaling of the parameterisation of the line L.
• Note also that, returning to first principles,
f|′
L (0) = lim
λ→0
f (x′ + λ (x −x′)) −f (x′)
λ
.
(2.7.3)
• Sometimes it is neater to write x −x′ ≡h. Using the Chain Rule, it is
easily shown that the second derivative of f|L is
f|′′
L(λ) = h⊤f ′′(x′ + λh)h
and
f|′′
L(0) = h⊤f ′′(x′)h.
2.8
Taylor’s Theorem: Deterministic Version
This should be fleshed out following ?.
Readers are presumed to be familiar with single variable versions of Taylor’s The-
orem. In particular recall both the second order exact and infinite versions.
An interesting example is to approximate the discount factor using powers of the
interest rate:
1
1 + i = 1 −i + i2 −i3 + i4 + . . .
(2.8.1)
1There may be some lapses in this version.
Revised: December 2, 1998

26
2.9. THE FUNDAMENTAL THEOREM OF CALCULUS
We will also use two multivariate versions of Taylor’s theorem which can be ob-
tained by applying the univariate versions to the restriction to a line of a function
of n variables.
Theorem 2.8.1 (Taylor’s Theorem) Let f : X →ℜbe twice differentiable,
X ⊆ℜn. Then for any x, x′ ∈X, ∃λ ∈(0, 1) such that
f(x) = f(x′) + f ′(x′)(x −x′) + 1
2(x −x′)⊤f ′′(x′ + λ(x −x′))(x −x′). (2.8.2)
Proof Let L be the line from x′ to x.
Then the univariate version tells us that there exists λ ∈(0, 1)2 such that
f|L(1) = f|L(0) + f|′
L(0) + 1
2f|′′
L(λ).
(2.8.3)
Making the appropriate substitutions gives the multivariate version in the theorem.
Q.E.D.
The (infinite) Taylor series expansion does not necessarily converge at all, or to
f(x). Functions for which it does are called analytic. ? is an example of a function
which is not analytic.
2.9
The Fundamental Theorem of Calculus
This theorem sets out the precise rules for cancelling integration and differentia-
tion operations.
Theorem 2.9.1 (Fundamental Theorem of Calculus) The integration and dif-
ferentiation operators are inverses in the following senses:
1.
d
db
Z b
a f(x)dx = f(b)
2.
Z b
a f ′(x)dx = f(b) −f(a)
This can be illustrated graphically using a picture illustrating the use of integration
to compute the area under a curve.
2Should this not be the closed interval?
Revised: December 2, 1998

