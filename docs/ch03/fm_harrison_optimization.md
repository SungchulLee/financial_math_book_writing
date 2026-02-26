# Convexity, Optimization & Econometrics

!!! info "Source"
    **Mathematical Economics and Finance** by Michael Harrison and Patrick Waldron, 1998.
    These notes are used for educational purposes.

## Convexity and Optimization

CHAPTER 3. CONVEXITY AND OPTIMISATION
27
Chapter 3
CONVEXITY AND
OPTIMISATION
3.1
Introduction
[To be written.]
3.2
Convexity and Concavity
3.2.1
Definitions
Definition 3.2.1 A subset X of a vector space is a convex set
⇐⇒
∀x, x′ ∈X, λ ∈[0, 1], λx + (1 −λ)x′ ∈X.
Theorem 3.2.1 A sum of convex sets, such as
X + Y ≡{x + y : x ∈X, y ∈Y } ,
is also a convex set.
Proof The proof of this result is left as an exercise.
Q.E.D.
Definition 3.2.2 Let f : X →Y where X is a convex subset of a real vector
space and Y ⊆ℜ. Then
Revised: December 2, 1998

28
3.2. CONVEXITY AND CONCAVITY
1. f is a convex function
⇐⇒
∀x ̸= x′ ∈X, λ ∈(0, 1)
f (λx + (1 −λ)x′) ≤λf(x) + (1 −λ)f(x′).
(3.2.1)
(This just says that a function of several variables is convex if its restriction
to every line segment in its domain is a convex function of one variable in
the familiar sense.)
2. f is a concave function
⇐⇒
∀x ̸= x′ ∈X, λ ∈(0, 1)
f (λx + (1 −λ)x′) ≥λf(x) + (1 −λ)f(x′).
(3.2.2)
3. f is affine
⇐⇒
f is both convex and concave.1
Note that the conditions (3.2.1) and (3.2.2) could also have been required to hold
(equivalently)
∀x, x′ ∈X, λ ∈[0, 1]
since they are satisfied as equalities ∀f when x = x′, when λ = 0 and when
λ = 1.
Note that f is convex ⇐⇒−f is concave.
Definition 3.2.3 Again let f : X →Y where X is a convex subset of a real vector
space and Y ⊆ℜ. Then
1. f is a strictly convex function
⇐⇒
∀x ̸= x′ ∈X, λ ∈(0, 1)
f (λx + (1 −λ)x′) < λf(x) + (1 −λ)f(x′).
1A linear function is an affine function which also satisfies f(0) = 0.
Revised: December 2, 1998

CHAPTER 3. CONVEXITY AND OPTIMISATION
29
2. f is a strictly concave function
⇐⇒
∀x ̸= x′ ∈X, λ ∈(0, 1)
f (λx + (1 −λ)x′) > λf(x) + (1 −λ)f(x′).
Note that there is no longer any flexibility as regards allowing x = x′ or λ = 0 or
λ = 1 in these definitions.
3.2.2
Properties of concave functions
Note the connection between convexity of a function of several variables and con-
vexity of the restrictions of that function to any line in its domain: the former is
convex if and only if all the latter are.
Note that a function on a multidimensional vector space, X, is convex if and only
if the restriction of the function to the line L is convex for every line L in X, and
similarly for concave, strictly convex, and strictly concave functions.
Since every convex function is the mirror image of a concave function, and vice
versa, every result derived for one has an obvious corollary for the other. In gen-
eral, we will consider only concave functions, and leave the derivation of the
corollaries for convex functions as exercises.
Let f : X →ℜand g : X →ℜbe concave functions. Then
1. If a, b > 0, then af + bg is concave.
2. If a < 0, then af is convex.
3. min{f, g} is concave
The proofs of the above properties are left as exercises.
Definition 3.2.4 Consider the real-valued function f: X →Y where Y ⊆ℜ.
1. The upper contour sets of f are the sets {x ∈X : f(x) ≥α} (α ∈ℜ).
2. The level sets or indifference curves of f are the sets {x ∈X : f(x) = α}
(α ∈ℜ).
3. The lower contour sets of f are the sets {x ∈X : f(x) ≤α} (α ∈ℜ).
In Definition 3.2.4, X does not have to be a (real) vector space.
Revised: December 2, 1998

30
3.2. CONVEXITY AND CONCAVITY
Theorem 3.2.2 The upper contour sets {x ∈X : f(x) ≥α} of a concave
function are convex.
Proof This proof is probably in a problem set somewhere.
Q.E.D.
Consider as an aside the two-good consumer problem. Note in particular the im-
plications of Theorem 3.2.2 for the shape of the indifference curves corresponding
to a concave utility function. Concave u is a sufficient but not a necessary condi-
tion for convex upper contour sets.
3.2.3
Convexity and differentiability
In this section, we show that there are a total of three ways of characterising
concave functions, namely the definition above, a theorem in terms of the first
derivative (Theorem 3.2.3) and a theorem in terms of the second derivative or
Hessian (Theorem 3.2.4).
Theorem 3.2.3 [Convexity criterion for differentiable functions.] Let f : X →ℜ
be differentiable, X ⊆ℜn an open, convex set. Then:
f is (strictly) concave
⇐⇒
∀x ̸= x′ ∈X,
f(x) ≤(<)f(x′) + f ′(x′)(x −x′).
(3.2.3)
Theorem 3.2.3 says that a function is concave if and only if the tangent hyperplane
at any point lies completely above the graph of the function, or that a function is
concave if and only if for any two distinct points in the domain, the directional
derivative at one point in the direction of the other exceeds the jump in the value
of the function between the two points. (See Section 2.7 for the definition of a
directional derivative.)
Proof (See ?.)
1. We first prove that the weak version of inequality 3.2.3 is necessary for
concavity, and then that the strict version is necessary for strict concavity.
Choose x, x′ ∈X.
Revised: December 2, 1998

CHAPTER 3. CONVEXITY AND OPTIMISATION
31
(a) Suppose that f is concave.
Then, for λ ∈(0, 1),
f (x′ + λ(x −x′)) ≥f(x′) + λ (f(x) −f(x′)) .
(3.2.4)
Subtract f(x′) from both sides and divide by λ:
f (x′ + λ(x −x′)) −f(x′)
λ
≥f(x) −f(x′).
(3.2.5)
Now consider the limits of both sides of this inequality as λ →0.
The LHS tends to f ′ (x′) (x −x′) by definition of a directional deriva-
tive (see (2.7.2) and (2.7.3) above). The RHS is independent of λ and
does not change. The result now follows easily for concave functions.
However, 3.2.5 remains a weak inequality even if f is a strictly con-
cave function.
(b) Now suppose that f is strictly concave and x ̸= x′.
Since f is also concave, we can apply the result that we have just
proved to x′ and x′′ ≡1
2 (x + x′) to show that
f ′(x′)(x′′ −x′) ≥f(x′′) −f(x′).
(3.2.6)
Using the definition of strict concavity (or the strict version of inequal-
ity (3.2.4)) gives:
f(x′′) −f(x′) > 1
2 (f(x) −f(x′)) .
(3.2.7)
Combining these two inequalities and multiplying across by 2 gives
the desired result.
2. Conversely, suppose that the derivative satisfies inequality (3.2.3). We will
deal with concavity. To prove the theorem for strict concavity, just replace
all the weak inequalities (≥) with strict inequalities (>), as indicated.
Set x′ = λx+(1−λ)x′′. Then, applying the hypothesis of the proof in turn
to x and x′ and to x′′ and x′ yields:
f(x)
≤
f(x′) + f ′(x′)(x −x′)
(3.2.8)
and
f(x′′)
≤
f(x′) + f ′(x′)(x′′ −x′)
(3.2.9)
A convex combination of (3.2.8) and (3.2.9) gives:
λf(x) + (1 −λ)f(x′′)
Revised: December 2, 1998

32
3.2. CONVEXITY AND CONCAVITY
≤
f(x′) + f ′(x′) (λ ((x −x′)) + (1 −λ) ((x′′ −x′)))
=
f(x′),
(3.2.10)
since
λ ((x −x′)) + (1 −λ) ((x′′ −x′)) = λx + (1 −λ)x′′ −x′ = 0n. (3.2.11)
(3.2.10) is just the definition of concavity as required.
Q.E.D.
Theorem 3.2.4 [Concavity criterion for twice differentiable functions.] Let f :
X →ℜbe twice continuously differentiable (C2), X ⊆ℜn open and convex.
Then:
1. f is concave
⇐⇒
∀x ∈X, the Hessian matrix f ′′(x) is negative semidefinite.
2. f ′′(x) negative definite ∀x ∈X
⇒
f is strictly concave.
The fact that the condition in the second part of this theorem is sufficient but not
necessary for concavity inspires the search for a counter-example, in other words
for a function which is strictly concave but has a second derivative which is only
negative semi-definite and not strictly negative definite. The standard counter-
example is given by f(x) = x2n for any integer n > 1.
Proof We first use Taylor’s theorem to demonstrate the sufficiency of the condi-
tion on the Hessian matrices. Then we use the Fundamental Theorem of Calculus
(Theorem 2.9.1) and a proof by contrapositive to demonstrate the necessity of this
condition in the concave case for n = 1. Then we use this result and the Chain
Rule to demonstrate necessity for n > 1. Finally, we show how these arguments
can be modified to give an alternative proof of sufficiency for functions of one
variable.
1. Suppose first that f ′′(x) is negative semi-definite ∀x ∈X. Recall Taylor’s
Theorem above (Theorem 2.8.1).
It follows that f(x) ≤f(x′) + f ′(x′)(x −x′). Theorem 3.2.3 shows that f
is then concave. A similar proof will work for negative definite Hessian and
strictly concave function.
Revised: December 2, 1998

CHAPTER 3. CONVEXITY AND OPTIMISATION
33
2. To demonstrate necessity, we must consider separately first functions of a
single variable and then functions of several variables.
(a) First consider a function of a single variable. Instead of trying to show
that concavity of f implies a negative semi-definite (i.e. non-positive)
second derivative ∀x ∈X, we will prove the contrapositive. In other
words, we will show that if there is any point x∗∈X where the second
derivative is positive, then f is locally strictly convex around x∗and
so cannot be concave.
So suppose f ′′(x∗) > 0. Then, since f is twice continuously differ-
entiable, f ′′(x) > 0 for all x in some neighbourhood of x∗, say (a, b).
Then f ′ is an increasing function on (a, b). Consider two points in
(a, b), x < x′′ and let x′ = λx + (1 −λ)x′′ ∈X, where λ ∈(0, 1).
Using the fundamental theorem of calculus,
f(x′) −f(x)
=
Z x′
x
f ′(t)dt < f ′(x′)(x′ −x)
and
f(x′′) −f(x′)
=
Z x′′
x′
f ′(t)dt < f ′(x′)(x′′ −x′).
Rearranging each inequality gives:
f(x)
>
f(x′) + f ′(x′)(x −x′)
and
f(x′′)
>
f(x′) + f ′(x′)(x′′ −x′),
which are just the single variable versions of (3.2.8) and (3.2.9). As in
the proof of Theorem 3.2.3, a convex combination of these inequalities
reduces to
f(x′) < λf(x) + (1 −λ)f(x′′),
and hence f is locally strictly convex on (a, b).
(b) Now consider a function of several variables. Suppose that f is con-
cave and fix x ∈X and h ∈ℜn. (We use an x, x+h argument instead
of an x, x′ argument to tie in with the definition of a negative definite
matrix.) Then, at least for sufficiently small λ, g(λ) ≡f(x + λh) also
defines a concave function (of one variable), namely the restriction of
f to the line segment from x in the direction from x to x + h. Thus,
using the result we have just proven for functions of one variable, g
has non-positive second derivative. But we know from p. 25 above
that g′′(0) = h⊤f ′′(x)h, so f ′′(x) is negative semi-definite.
Revised: December 2, 1998

34
3.2. CONVEXITY AND CONCAVITY
3. For functions of one variable, the above arguments can give an alternative
proof of sufficiency which does not require Taylor’s Theorem. In fact, we
have something like the following:
f ′′ (x) < 0 on (a, b)
⇒
f locally strictly concave on (a, b)
f ′′ (x) ≤0 on (a, b)
⇒
f locally concave on (a, b)
f ′′ (x) > 0 on (a, b)
⇒
f locally strictly convex on (a, b)
f ′′ (x) ≥0 on (a, b)
⇒
f locally convex on (a, b)
The same results which we have demonstrated for the interval (a, b) also
hold for the entire domain X (which of course is also just an open interval,
as it is an open convex subset of ℜ).
Q.E.D.
Theorem 3.2.5 A non-decreasing twice differentiable concave transformation of
a twice differentiable concave function (of several variables) is also concave.
Proof The details are left as an exercise.
Q.E.D.
Note finally the implied hierarchy among different classes of functions:
negative definite Hessian ⊂strictly concave ⊂concave = negative semidefinite
Hessian.
As an exercise, draw a Venn diagram to illustrate these relationships (and add
other classes of functions to it later on as they are introduced).
The second order condition above is reminiscent of that for optimisation and sug-
gests that concave or convex functions will prove useful in developing theories of
optimising behaviour. In fact, there is a wider class of useful functions, leading us
to now introduce further definitions.
3.2.4
Variations on the convexity theme
Let X ⊆ℜn be a convex set and f : X →ℜa real-valued function defined on X.
In order (for reasons which shall become clear in due course) to maintain consis-
tency with earlier notation, we adopt the convention when labelling vectors x and
x′ that f(x′) ≤f(x).2
2There may again be some lapses in this version.
Revised: December 2, 1998

CHAPTER 3. CONVEXITY AND OPTIMISATION
35
Definition 3.2.5 Let
C(α) = {x ∈X : f(x) ≥α}.
Then f : X →ℜis quasiconcave
⇐⇒
∀α ∈ℜ, C(α) is a convex set.
Theorem 3.2.6 The following statements are equivalent to the definition of qua-
siconcavity:
1. ∀x ̸= x′ ∈X such that f(x′) ≤f(x) and ∀λ ∈(0, 1),
f (λx + (1 −λ)x′) ≥f(x′).
2. ∀x, x′ ∈X, λ ∈[0, 1], f (λx + (1 −λ)x′) ≥min{f(x), f(x′)}.
3. (If f is differentiable,) ∀x, x′ ∈X such that f(x) −f(x′) ≥0, f ′(x′)(x −
x′) ≥0.
Proof
1. We begin by showing the equivalence between the definition and
condition 1.3
(a) First suppose that the upper contour sets are convex. Let x and x′ ∈X
and let α = min{f(x), f(x′)}. Then x and x′ are in C(α). By the
hypothesis of convexity, for any λ ∈(0, 1), λx + (1 −λ)x′ ∈C(α).
The desired result now follows.
(b) Now suppose that condition 1 holds. To show that C(α) is a convex
set, we just take x and x′ ∈C(α) and investigate whether λx + (1 −
λ)x′ ∈C(α). But, by our previous result,
f (λx + (1 −λ)x′) ≥min{f(x), f(x′)} ≥α
where the final inequality holds because x and x′ are in C(α).
2. It is almost trivial to show the equivalence of conditions 1 and 2.
(a) In the case where f(x) ≥f(x′) or f(x′) = min{f(x), f(x′)}, there
is nothing to prove. Otherwise, we can just reverse the labels x and x′.
The statement is true for x = x′ or λ = 0 or λ = 1 even if f is not
quasiconcave.
3This proof may need to be rearranged to reflect the choice of a different equivalent character-
isation to act as definition.
Revised: December 2, 1998

36
3.2. CONVEXITY AND CONCAVITY
(b) The proof of the converse is even more straightforward and is left as
an exercise.
3. Proving that condition 3 is equivalent to quasiconcavity for a differentiable
function (by proving that it is equivalent to conditions 1 and 2) is much the
trickiest part of the proof.
(a) Begin by supposing that f satisfies conditions 1 and 2. Proving that
condition 3 is necessary for quasiconcavity is the easier part of the
proof (and appears as an exercise on one of the problem sets). Pick
any λ ∈(0, 1) and, without loss of generality, x and x′ such that
f(x′) ≤f(x). By quasiconcavity,
f (λx + (1 −λ)x′) ≥f(x′).
(3.2.12)
Consider
f|L(λ) = f (λx + (1 −λ)x′) = f (x′ + λ(x −x′)) .
(3.2.13)
We want to show that the directional derivative
f|′
L(0) = f ′(x′)(x −x′) ≥0.
(3.2.14)
But
f|′
L(0) = lim
λ→0
f (x′ + λ(x −x′)) −f(x′)
λ
.
(3.2.15)
Since the right hand side is non-negative for small positive values of λ
(λ < 1), the derivative must be non-negative as required.
(b) Now the difficult part — to prove that condition 3 is a sufficient con-
dition for quasiconcavity.
Suppose the derivative satisfies the hypothesis of the theorem, but f is
not quasiconcave. In other words, ∃x, x′, λ∗such that
f (λ∗x + (1 −λ∗)x′) < min{f(x), f(x′)},
(3.2.16)
where without loss of generality f(x′) ≤f(x). The hypothesis of the
theorem applied first to x and λ∗x + (1 −λ∗)x′ and then to x′ and
λ∗x + (1 −λ∗)x′ tells us that:
f ′ (λ∗x + (1 −λ∗)x′) (x −(λ∗x + (1 −λ∗)x′)) ≥0 (3.2.17)
f ′ (λ∗x + (1 −λ∗)x′) (x′ −(λ∗x′ + (1 −λ∗)x)) ≥0. (3.2.18)
Revised: December 2, 1998

CHAPTER 3. CONVEXITY AND OPTIMISATION
37
Multiplying the first inequality by (1 −λ∗) and the second by λ∗yields
a pair of inequalities which can only be satisfied simultaneously if:
f ′ (λ∗x + (1 −λ∗)x′) (x′ −x) = 0.
(3.2.19)
In other words, f|′
L(λ∗) = 0; we already know that f|L(λ∗) < f|L(0) ≤
f|L(1). We can apply the same argument to any point where the value
of f|L is less than f|L(0) to show that the corresponding part of the
graph of f|L has zero slope, or is flat. But this is incompatible either
with continuity of f|L or with the existence of a point where f|L(λ∗)
is strictly less than f|L(0). So we have a contradiction as required.
Q.E.D.
In words, part 3 of Theorem 3.2.6 says that whenever a differentiable quasicon-
cave function has a higher value at x than at x′, or the same value at both points,
then the directional derivative of f at x′ in the direction of x is non-negative. It
might help to think about this by considering n = 1 and separating out the cases
x > x′ and x < x′.
Theorem 3.2.7 Let f : X →ℜbe quasiconcave and g : ℜ→ℜbe increasing.
Then g ◦f is a quasiconcave function.
Proof This follows easily from the previous result. The details are left as an
exercise.
Q.E.D.
Note the implications of Theorem 3.2.7 for utility theory. In particular, if pref-
erences can be represented by a quasiconcave utility function, then they can be
represented by a quasiconcave utility function only. This point will be considered
again in a later section of the course.
Definition 3.2.6 f : X →ℜis strictly quasiconcave
⇐⇒
∀x ̸= x′ ∈X such that f(x) ≥f(x′) and ∀λ ∈(0, 1), f (λx + (1 −λ)x′) >
f(x′).
Definition 3.2.7 f is (strictly) quasiconvex
⇐⇒
−f is (strictly) quasiconcave4
4EC3080 ended here for Hilary Term 1998.
Revised: December 2, 1998

38
3.2. CONVEXITY AND CONCAVITY
Definition 3.2.8 f is pseudoconcave
⇐⇒
f is differentiable and quasiconcave and
f(x) −f(x′) > 0
⇒
f ′(x′) (x −x′) > 0.
Note that the last definition modifies slightly the condition in Theorem 3.2.6 which
is equivalent to quasiconcavity for a differentiable function.
Pseudoconcavity will crop up in the second order condition for equality con-
strained optimisation.
We conclude this section by looking at a couple of the functions of several vari-
ables which will crop repeatedly in applications in economics later on.
First, consider the interesting case of the affine function
f: ℜn →ℜ: x 7→M −p⊤x,
where M ∈ℜand p ∈ℜn. This function is both concave and convex, but neither
strictly concave nor strictly convex. Furthermore,
f (λx + (1 −λ) x′)
=
λf(x) + (1 −λ)f(x′)
(3.2.20)
≥
min{f(x), f(x′)}
(3.2.21)
and
(−f) (λx + (1 −λ) x′)
=
λ(−f)(x) + (1 −λ)(−f)(x′)
(3.2.22)
≥
min{(−f)(x), (−f)(x′)},
(3.2.23)
so f is both quasiconcave and quasiconcave, but not strictly so in either case. f
is, however, pseudoconcave (and pseudoconvex) since
f(x) > f(x′)
⇐⇒
p⊤x < p⊤x′
(3.2.24)
⇐⇒
p⊤(x −x′) < 0
(3.2.25)
⇐⇒
−f ′(x′)(x −x′) < 0
(3.2.26)
⇐⇒
f ′(x′)(x −x′) > 0.
(3.2.27)
Finally, here are two graphs of Cobb-Douglas functions:5
5To see them you will have to have copied two .WMF files retaining their uppercase filenames
and put them in the appropriate directory,
C:/TCD/teaching/WWW/MA381/NOTES/!
Revised: December 2, 1998

CHAPTER 3. CONVEXITY AND OPTIMISATION
39
Graph of z = x0.5y0.5
Graph of z = x−0.5y1.5
3.3
Unconstrained Optimisation
Definition 3.3.1 Let X ⊆ℜn, f : X →ℜ.
Then f has a (strict) global maximum at x∗⇐⇒∀x ∈X, x ̸= x∗, f(x) ≤(<
)f(x∗).
Also f has a (strict) local maximum at x∗
⇐⇒
∃ϵ > 0 such that ∀x ∈
Bϵ(x∗), x ̸= x∗, f(x) ≤(<)f(x∗).
Similarly for minima.
Theorem 3.3.1 A continuous real-valued function on a compact subset of ℜn at-
tains a global maximum and a global minimum.
Proof Not given here. See ?.
Q.E.D.
While this is a neat result for functions on compact domains, results in calculus
are generally for functions on open domains, since the limit of the first difference
Revised: December 2, 1998

40
3.3. UNCONSTRAINED OPTIMISATION
of the function at x, say, makes no sense if the function and the first difference are
not defined in some open neighbourhood of x (some Bϵ(x)).
The remainder of this section and the next two sections are each centred around
three related theorems:
1. a theorem giving necessary or first order conditions which must be satis-
fied by the solution to an optimisation problem (Theorems 3.3.2, 3.4.1 and
3.5.1);
2. a theorem giving sufficient or second order conditions under which a solu-
tion to the first order conditions satisfies the original optimisation problem
(Theorems 3.3.3, 3.4.2 and 3.5.2); and
3. a theorem giving conditions under which a known solution to an optimisa-
tion problem is the unique solution (Theorems 3.3.4, 3.4.3 and 3.5.3).
The results are generally presented for maximisation problems. However, any
minimisation problem is easily turned into a maximisation problem by reversing
the sign of the function to be minimised and maximising the function thus ob-
tained.
Throughout the present section, we deal with the unconstrained optimisation prob-
lem
max
x∈X f (x)
(3.3.1)
where X ⊆ℜn and f : X →ℜis a real-valued function of several variables,
called the objective function of Problem (3.3.1.)
(It is conventional to use the letter λ both to parameterise convex combinations
and as a Lagrange multiplier. To avoid confusion, in this section we switch to the
letter α for the former usage.)
Theorem 3.3.2 Necessary (first order) condition for unconstrained maxima and
minima.
Let X be open and f differentiable with a local maximum or minimum at x∗∈X.
Then f ′(x∗) = 0, or f has a stationary point at x∗.
Proof Without loss of generality, assume that the function has a local maximum
at x∗. Then ∃ϵ > 0 such that, whenever ∥h∥< ϵ,
f(x∗+ h) −f(x∗) ≤0.
It follows that, for 0 < h < ϵ,
f(x∗+ hei) −f(x∗)
h
≤0,
Revised: December 2, 1998

CHAPTER 3. CONVEXITY AND OPTIMISATION
41
(where ei denotes the ith standard basis vector) and hence that
∂f
∂xi
(x∗) = lim
h→0
f(x∗+ hei) −f(x∗)
h
≤0.
(3.3.2)
Similarly, for 0 > h > −ϵ,
f(x∗+ hei) −f(x∗)
h
≥0,
and hence
∂f
∂xi
(x∗) = lim
h→0
f(x∗+ hei) −f(x∗)
h
≥0.
(3.3.3)
Combining (3.3.2) and (3.3.3) yields the desired result.
Q.E.D.
The first order conditions are only useful for identifying optima in the interior
of the domain of the objective function: Theorem 3.3.2 applies only to functions
whose domain X is open. Other methods must be used to check for possible cor-
ner solutions or boundary solutions to optimisation problems where the objective
function is defined on a domain that is not open.
Theorem 3.3.3 Sufficient (second order) condition for unconstrained maxima and
minima.
Let X ⊆ℜn be open and let f : X →ℜbe a twice continuously differentiable
function with f ′(x∗) = 0 and f ′′(x∗) negative definite.
Then f has a strict local maximum at x∗.
Similarly for positive definite Hessians and local minima.
Proof Consider the second order Taylor expansion used previously in the proof
of Theorem 3.2.4: for any x ∈X, ∃s ∈(0, 1) such that
f(x) = f(x∗) + f ′(x∗)(x −x∗) + 1
2(x −x∗)⊤f ′′(x∗+ s(x −x∗))(x −x∗).
or, since the first derivative vanishes at x∗,
f(x) = f(x∗) + 1
2(x −x∗)⊤f ′′(x∗+ s(x −x∗))(x −x∗).
Since f ′′ is continuous, f ′′(x∗+ s(x −x∗)) will also be negative definite for x
in some open neighbourhood of x∗. Hence, for x in this neighbourhood, f(x) <
f(x∗) and f has a strict local maximum at x∗.
Revised: December 2, 1998

42
3.3. UNCONSTRAINED OPTIMISATION
Q.E.D.
The weak form of this result does not hold. In other words, semi-definiteness
of the Hessian matrix at x∗is not sufficient to guarantee that f has any sort of
maximum at x∗. For example, if f(x) = x3, then the Hessian is negative semi-
definite at x = 0 but the function does not have a local maximum there (rather, it
has a point of inflexion).
Theorem 3.3.4 Uniqueness conditions for unconstrained maximisation.
If
1. x∗solves Problem (3.3.1) and
2. f is strictly quasiconcave (presupposing that X is a convex set),
then x∗is the unique (global) maximum.
Proof Suppose not, in other words that ∃x ̸= x∗such that f (x) = f (x∗).
Then, for any α ∈(0, 1),
f (αx + (1 −α) x∗) > min {f (x) , f (x∗)} = f (x∗) ,
so f does not have a maximum at either x or x∗.
This is a contradiction, so the maximum must be unique.
Q.E.D.
Theorem 3.3.5 Tempting, but not quite true, corollaries of Theorem 3.3.3 are:
• Every stationary point of a twice continuously differentiable strictly con-
cave function is a strict global maximum (and so there can be at most one
stationary point).
• Every stationary point of a twice continuously differentiable strictly convex
function is a strict global minimum.
Proof If the Hessian matrix is positive/negative definite everywhere, then the ar-
gument in the proof of Theorem 3.3.3 can be applied for x ∈X and not just for
x ∈Bϵ (x∗). If there are points at which the Hessian is merely semi-definite, then
the proof breaks down.
Q.E.D.
Note that many strictly concave and strictly convex functions will have no station-
ary points, for example
f: ℜ→ℜ: x 7→ex.
Revised: December 2, 1998

CHAPTER 3. CONVEXITY AND OPTIMISATION
43
3.4
Equality Constrained Optimisation:
The Lagrange Multiplier Theorems
Throughout this section, we deal with the equality constrained optimisation prob-
lem
maxx∈X f (x)
s.t.
g (x) = 0m
(3.4.1)
where X ⊆ℜn, f : X →ℜis a real-valued function of several variables, called
the objective function of Problem (3.4.1) and g : X →ℜm is a vector-valued
function of several variables, called the constraint function of Problem (3.4.1); or,
equivalently, gj: X →ℜare real-valued functions for j = 1, . . . , m. In other
words, there are m scalar constraints represented by a single vector constraint:




g1 (x)
...
gm (x)



=




0
...
0



.
We will introduce and motivate the Lagrange multiplier method which applies to
such constrained optimisation problems with equality constraints. We will assume
where appropriate that the objective function f and the m constraint functions
g1, . . . , gm are all once or twice continuously differentiable.
The entire discussion here is again presented in terms of maximisation, but can
equally be presented in terms of minimisation by reversing the sign of the objec-
tive function. Similarly, note that the signs of the constraint function(s) can be
reversed without altering the underlying problem. We will see, however, that this
also reverses the signs of the corresponding Lagrange multipliers. The signifi-
cance of this effect will be seen from the formal results, which are presented here
in terms of the usual three theorems.
Before moving on to those formal results, we briefly review the methodology for
solving constrained optimisation problems which should be familiar from intro-
ductory and intermediate economic analysis courses.
If x∗is a solution to Problem (3.4.1), then there exist Lagrange multipliers,6 λ ≡
(λ1, . . . , λm), such that
f ′ (x∗) + λ⊤g′ (x∗) = 0n.
Thus, to find the constrained optimum, we proceed as if optimising the Lagrangean:
L (x, λ) ≡f (x∗) + λ⊤g (x∗) .
Note that
6As usual, a row of numbers separated by commas is used as shorthand for a column vector.
Revised: December 2, 1998

44
3.4. EQUALITY CONSTRAINED OPTIMISATION:
THE LAGRANGE MULTIPLIER THEOREMS
1. L = f whenever g = 0 and
2. g = 0 where L is optimised.
Roughly speaking, this is why the constrained optimum of f corresponds to the
optimum of L.
The Lagrange multiplier method involves the following four steps:
1. introduce the m Lagrange multipliers, λ ≡(λ1, . . . , λm).
2. Define the Lagrangean L: X × ℜm →ℜ, where
X × ℜm ≡{(x, λ) : x ∈X, λ ∈ℜm} ,
by
L (x, λ) ≡f (x) + λ ⊤g (x) .
3. Find the stationary points of the Lagrangean, i.e. set L′ (x, λ) = 0. Since
the Lagrangean is a function of n + m variables, this gives n + m first order
conditions. The first n are
f ′ (x) + λ⊤g′ (x) = 0
or
∂f
∂xi
(x) +
m
X
j=1
λj
∂gj
∂xi
(x) = 0
i = 1, . . . , n.
The last m are just the original constraints,
g (x) = 0
or
gj (x) = 0
j = 1, . . . , m.
4. Finally, the second order conditions must be checked.
As an example, consider maximisation of a utility function representing Cobb-
Douglas preferences subject to a budget constraint.
The first n first order or Lagrangean conditions say that the total derivative (or
gradient) of f at x is a linear combination of the total derivatives (or gradients) of
the constraint functions at x.
Consider a picture with n = 2 and m = 1.
Since the directional derivative along a tangent to a level set or indifference curve
is zero at the point of tangency, x, (the function is at a maximum or minimum
Revised: December 2, 1998

CHAPTER 3. CONVEXITY AND OPTIMISATION
45
along the tangent) or f ′ (x) (x′ −x) = 0, the gradient vector, f ′ (x)⊤, must be
perpendicular to the direction of the tangent, x′ −x.
At the optimum, the level sets of f and g have a common tangent, so f ′ (x) and
g′ (x) are collinear, or f ′ (x) = −λg′ (x). It can also be seen with a little thought
that for the solution to be a local constrained maximum, λ must be positive if g is
quasiconcave and negative if g is quasiconvex (in either case, the constraint curve
is the boundary of a convex set).
We now consider the equality constrained optimisation problem in more depth.
Theorem 3.4.1 First order (necessary) conditions for optimisation with equality
constraints.
Consider problem (3.4.1) or the corresponding minimisation problem.
If
1. x∗solves this problem (which implies that g (x∗) = 0),
2. f and g are continuously differentiable, and
3. the m × n matrix
g′ (x∗) =




∂g1
∂x1 (x∗)
. . .
∂g1
∂xn (x∗)
...
...
...
∂gm
∂x1 (x∗)
. . .
∂gm
∂xn (x∗)




is of rank m (i.e. there are no redundant constraints, both in the sense that
there are fewer constraints than variables and in the sense that the con-
straints which are present are ‘independent’),
then ∃λ∗∈ℜm such that f ′ (x∗) + λ∗⊤g′ (x∗) = 0 (i.e. in ℜn, f ′ (x∗) is in the
m−dimensional subspace generated by the m vectors g1′ (x∗) , . . . , gm′ (x∗)).
Proof The idea is to solve g (x∗) = 0 for m variables as a function of the other
n −m and to substitute the solution into the objective function to give an uncon-
strained problem with n −m variables.
For this proof, we need Theorem 2.6.1 on p. 2.6.1 above, the Implicit Function
Theorem. Using this theorem, we must find the m weights λ1, . . . , λm to prove
that f ′ (x∗) is a linear combination of g1′ (x∗) , . . . , gm′ (x∗).
Without loss of generality, we assume that the first m columns of g′ (x∗) are lin-
early independent (if not, then we merely relabel the variables accordingly).
Now we can partition the vector x∗as (y∗, z∗) and, using the notation of the
Implicit Function Theorem, find a neighbourhood Z of z∗and a function h defined
on Z such that
g (h (z) , z) = 0
∀z ∈Z
Revised: December 2, 1998

46
3.4. EQUALITY CONSTRAINED OPTIMISATION:
THE LAGRANGE MULTIPLIER THEOREMS
and also
h′ (z∗) = −(Dyg)−1 Dzg.
Now define a new objective function F: Z →ℜby
F (z) ≡f (h (z) , z) .
Since x∗solves the constrained problem maxx∈X f (x) subject to g (x) = 0, it
follows that z∗solves the unconstrained problem maxz∈Z F (z). (This is easily
shown using a proof by contradiction argument.)
Hence, z∗satisfies the first order conditions for unconstrained maximisation of F,
namely
F ′ (z∗) = 0.
Applying the Chain Rule in exactly the same way as in the proof of the Implicit
Function Theorem yields an equation which can be written in shorthand as:
Dyfh′ (z) + Dzf
=
0.
Substituting for h′ (z) gives:
Dyf (Dyg)−1 Dzg = Dzf.
We can also partition f ′ (x) as

Dyf (Dyg)−1 Dyg
Dzf

Substituting for the second sub-matrix yields:
f ′ (x)
=

Dyf (Dyg)−1 Dyg
Dyf (Dyg)−1 Dzg

=
Dyf (Dyg)−1 
Dyg
Dzg

=
−λ ⊤g′ (x)
where we define
λ ≡−Dyf (Dyg)−1 .
Q.E.D.
Theorem 3.4.2 Second order (sufficient or concavity) conditions for maximisa-
tion with equality constraints.
If
1. f and g are differentiable,
Revised: December 2, 1998

CHAPTER 3. CONVEXITY AND OPTIMISATION
47
2. f ′ (x∗) + λ∗⊤g′ (x∗) = 0 (i.e. the first order conditions are satisfied at x∗),
3. λ∗
j ≥0 for j = 1, . . . , m,
4. f is pseudoconcave, and
5. gj is quasiconcave for j = 1, . . . , m,
then x∗solves the constrained maximisation problem.
It should be clear that non-positive Lagrange multipliers and quasiconvex con-
straint functions can take the place of non-negative Lagrange multipliers and qua-
siconcave Lagrange multipliers to give an alternative set of second order condi-
tions.
Proof Suppose that the second order conditions are satisfied, but that x∗is not a
constrained maximum. We will derive a contradiction.
Since x∗is not a maximum, ∃x ̸= x∗such that g (x) = 0 but f (x) > f (x∗).
By pseudoconcavity, f (x) −f (x∗) > 0 implies that f ′ (x∗) (x −x∗) > 0.
Since the constraints are satisfied at both x and x∗, we have g (x∗) = g (x) = 0.
By quasiconcavity of the constraint functions (see Theorem 3.2.6), gj (x)−gj (x∗) =
0 implies that gj′ (x∗) (x −x∗) ≥0.
By assumption, all the Lagrange multipliers are non-negative, so
f ′ (x∗) (x −x∗) + λ∗⊤g′ (x∗) (x −x∗) > 0.
Rearranging yields:
h
f ′ (x∗) + λ∗⊤g′ (x∗)
i
(x −x∗) > 0.
But the first order condition guarantees that the LHS of this inequality is zero (not
positive), which is the required contradiction.
Q.E.D.
Theorem 3.4.3 Uniqueness condition for equality constrained maximisation.
If
1. x∗is a solution,
2. f is strictly quasiconcave, and
3. gj is an affine function (i.e. both convex and concave) for j = 1, . . . , m,
then x∗is the unique (global) maximum.
Revised: December 2, 1998

48
3.4. EQUALITY CONSTRAINED OPTIMISATION:
THE LAGRANGE MULTIPLIER THEOREMS
Proof The uniqueness result is also proved by contradiction. Note that it does not
require any differentiability assumption.
• We first show that the feasible set is convex.
Suppose x ̸= x∗are two distinct solutions.
Consider the convex combination of these two solutions xα ≡αx+(1 −α) x∗.
Since each gj is affine and gj (x∗) = gj (x) = 0, we have
gj (xα) = αgj (x) + (1 −α) gj (x∗) = 0.
In other words, xα also satisfies the constraints.
• To complete the proof, we find the required contradiction:
Since f is strictly quasiconcave and f (x∗) = f (x), it must be the case that
f (xα) > f (x∗).
Q.E.D.
The construction of the obvious corollaries for minimisation problems is left as
an exercise.
We conclude this section with
Theorem 3.4.4 (Envelope Theorem.) Consider the modified constrained optimi-
sation problem:
max
x
f (x, α)
subject to
g (x, α) = 0,
(3.4.2)
where x ∈ℜn, α∈ℜq, f: ℜn+q →ℜand g: ℜn+q →ℜm (i.e. as usual f is
the real-valued objective function and g is a vector of m real-valued constraint
functions, but either or both can depend on exogenous or control variables α as
well as on the endogenous or choice variables x).
Suppose that the standard conditions for application of the Lagrange multiplier
theorems are satisfied.
Let x∗(α) denote the optimal choice of x for given α (x∗: ℜq →ℜn is called the
optimal response function) and let M (α) denote the maximum value attainable
by f for given α (M: ℜq →ℜis called the envelope function).
Then the partial derivative of M with respect to αi is just the partial derivative
of the relevant Lagrangean, f + λ⊤g, with respect to αi, evaluated at the optimal
value of x. The dependence of the vector of Lagrange multipliers, λ, on the vector
α should be ignored in calculating the last-mentioned partial derivative.
Proof The Envelope Theorem can be proved in the following steps:
Revised: December 2, 1998

CHAPTER 3. CONVEXITY AND OPTIMISATION
49
1. Write down the identity relating the functions M, f and x∗:
M (α) ≡f (x∗(α) , α)
2. Use (2.5.4) to derive an expression for the partial derivatives ∂M
∂αi of M in
terms of the partial derivatives of f and x∗:
M ′ (α) = Dxf (x∗(α) , α) x∗′ (α) + Dαf (x∗(α) , α) .
3. The first order (necessary) conditions for constrained optimisation say that
Dxf (x∗(α) , α) = −λ⊤Dxg (x∗(α) , α)
and allow us to eliminate the ∂f
∂xi terms from this expression.
4. Apply (2.5.4) again to the identity g (x∗, α) = 0m to obtain
Dxg (x∗(α) , α) x∗′ (α) + Dαg (x∗(α) , α) = 0m×q.
Finally, use this result to eliminate the ∂g
∂xi terms from your new expression
for ∂M
∂αi .
Combining all these results gives:
M ′ (α) = Dαf (x∗(α) , α) + λ⊤Dαg (x∗(α) , α) ,
which is the required result.
Q.E.D.
In applications in economics, the most frequently encountered applications will
make sufficient assumptions to guarantee that
1. x∗satisfies the first order conditions with each λi ≥0;
2. the Hessian f ′′ (x∗) is a negative definite (n × n) matrix; and
3. g is a linear function,
so that x∗is the unique optimal solution to the equality constrained optimisation
problem.
Revised: December 2, 1998

50
3.5. INEQUALITY CONSTRAINED OPTIMISATION:
THE KUHN-TUCKER THEOREMS
3.5
Inequality Constrained Optimisation:
The Kuhn-Tucker Theorems
Throughout this section, we deal with the inequality constrained optimisation
problem
maxx∈X f (x)
s.t.
gi (x) ≥0,
i = 1, 2, . . . , m
(3.5.1)
where once again X ⊆ℜn, f : X →ℜis a real-valued function of several
variables, called the objective function of Problem (3.5.1) and g : X →ℜm
is a vector-valued function of several variables, called the constraint function of
Problem (3.5.1).
Before presenting the usual theorems formally, we need some graphical motiva-
tion concerning the interpretation of Lagrange multipliers.
Suppose that the constraint functions are given by
g (x, α) = α −h (x) .
(3.5.2)
The Lagrangean is
L (x, λ) = f (x) + λ⊤(α −h (x)) .
(3.5.3)
Thus, using the Envelope Theorem, it is easily seen that the rate of change of the
envelope function M (α) with respect to the ‘level’ of the ith underlying con-
straint function hi is:
∂M
∂αi
= ∂L
∂αi
= λi.
(3.5.4)
Thus
• when λi = 0, the envelope function is at its maximum, or the objective
function at its unconstrained maximum, and the constraint is not binding.
• when λi < 0, the envelope function is decreasing
• when λi > 0, the envelope function is increasing
Now consider how the nature of the inequality constraint change as αi increases
(as illustrated, assuming f quasiconcave as usual and hi quasiconvex or gi quasi-
concave, so that the relationship between αi and λi is negative)
hi (x) ≤αi
(3.5.5)
Revised: December 2, 1998

CHAPTER 3. CONVEXITY AND OPTIMISATION
51
Derivative of
Lagrange
Constraint
Type of constraint
objective fn.
Multiplier
fn.
Binding/active
f ′ ≤0
λ ≥0
g = 0
Non-binding/inactive
f ′ = 0
λ = 0
g > 0
Table 3.1: Sign conditions for inequality constrained optimisation
(or gi (x, α) ≥0). For values of αi such that λi > 0, this constraint is strictly
binding. For values of αi such that λi = 0, this constraint is just binding. For
values of αi such that λi < 0, this constraint is non-binding.
Note that in this setup,
∂2M
∂α2
i
= ∂λi
∂αi
< 0,
(3.5.6)
so that the envelope function is strictly concave (up to the unconstrained optimum,
and constant beyond it).
Thus we will find that part of the necessity conditions below is that the Lagrange
multipliers be non-negative.
(For equality constrained optimisation, the signs
were important only when dealing with second order conditions).
Consider also at this stage the first order conditions for maximisation of a function
of one variable subject to a non-negativity constraint:
max
x
f(x) s.t. x ≥0.
They can be expressed as:
f ′(x∗)
≤
0
(3.5.7)
f ′(x∗)
=
0
if x > 0
(3.5.8)
The various sign conditions which we have looked at are summarised in Table 3.1.
Theorem 3.5.1 Necessary (first order) conditions for optimisation with inequal-
ity constraints.
If
1. x∗solves Problem (3.5.1), with
gi (x∗) = 0, i = 1, 2, . . . , b
and
gi (x∗) > 0, i = b + 1, . . . , m
(in other words, the first b constraints are binding (active) at x∗and the
last n −b are non-binding (inactive) at x∗, renumbering the constraints if
necessary to achieve this),
Revised: December 2, 1998

52
3.5. INEQUALITY CONSTRAINED OPTIMISATION:
THE KUHN-TUCKER THEOREMS
2. f and g are continuously differentiable, and
3. the b × n submatrix of g′ (x∗),





∂g1
∂x1 (x∗)
. . .
∂g1
∂xn (x∗)
...
...
...
∂gb
∂x1 (x∗)
. . .
∂gb
∂xn (x∗)




,
is of full rank b (i.e. there are no redundant binding constraints, both in
the sense that there are fewer binding constraints than variables and in the
sense that the constraints which are binding are ‘independent’),
then ∃λ ∈ℜm such that f ′ (x∗) + λ⊤g′ (x∗) = 0, with λi ≥0 for i = 1, 2, . . . , m
and gi(x∗) = 0 if λi > 0.
Proof The proof is similar to that of Theorem 3.4.1 for the equality constrained
case. It can be broken into seven steps.
1. Suppose x∗solves Problem (3.5.1).
We begin by restricting attention to a neighbourhood Bϵ (x∗) throughout
which the non-binding constraints remain non-binding, i.e.
gi (x) > 0 ∀x ∈Bϵ (x∗) , i = b + 1, . . ., m.
(3.5.9)
Such a neighbourhood exists since the constraint functions are continuous.
Since x∗solves Problem (3.5.1) by assumption, it also solves the following
problem:
maxx∈Bϵ(x∗) f (x)
s.t.
gi (x) ≥0,
i = 1, 2, . . . , b.
(3.5.10)
In other words, since the non-binding constraints are non-binding ∀x ∈
Bϵ (x∗) by construction, we can ignore them if we confine our search for
a maximum to this neighbourhood. We will return to the non-binding con-
straints in the very last step of this proof, but until then g will be taken to
refer to the vector of b binding constraint functions only and λ to the vector
of b Kuhn-Tucker multipliers corresponding to these binding constraints.
2. We now introduce slack variables s ≡(s1, . . ., sb), one corresponding to
each binding constraint, and consider the following equality constrained
maximisation problem:
maxx∈Bϵ(x∗),s∈ℜb
+ f (x)
Revised: December 2, 1998

CHAPTER 3. CONVEXITY AND OPTIMISATION
53
s.t.
G (x, s) = 0b
(3.5.11)
where Gi (x, s) ≡gi (x) −si, i = 1, 2, . . . , b.
Since x∗solves Problem (3.5.10) and all b constraints in that problem are
binding at x∗, it can be seen that (x∗, 0b) solves this new problem. For
consistency of notation, we define s∗≡0b.
3. We proceed with Problem (3.5.11) as in the Lagrange case. In other words,
we use the Implicit Function Theorem to solve the system of b equations in
n + b unknowns,
G (x, s) = 0b,
(3.5.12)
for the first b variables in terms of the last n. To do this, we partition the
vector of choice and slack variables three ways:
(x, s) ≡(y, z, s)
(3.5.13)
where y ∈ℜb and z ∈ℜn−b, and correspondingly partition the matrix of
partial derivatives evaluated at the optimum:
G′ (y∗, z∗, s∗)
=
G′ (x∗, s∗)
(3.5.14)
=

DyG
Dz,sG

(3.5.15)
=

DyG
DzG
DsG

(3.5.16)
=

Dyg
Dzg
−Ib

.
(3.5.17)
The rank condition allows us to apply the Implicit Function Theorem and
to find a function h : ℜn −→ℜb such that y = h (z, s) is a solution to
G (y, z, s) = 0 with
h′ (z∗, s∗) = −(Dyg)−1 Dz,sG.
(3.5.18)
(3.5.18) can in turn be partitioned to yield
Dzh = −(Dyg)−1 DzG = −(Dyg)−1 Dzg
(3.5.19)
and
Dsh = −(Dyg)−1 DsG = (Dyg)−1 Ib = (Dyg)−1 .
(3.5.20)
4. This solution can be substituted into the original objective function f to
create a new objective function F defined by
F (z, s) ≡f (h (z, s) , z)
(3.5.21)
Revised: December 2, 1998

54
3.5. INEQUALITY CONSTRAINED OPTIMISATION:
THE KUHN-TUCKER THEOREMS
and another new maximisation problem where there are only (implicit) non-
negativity constraints:
maxz∈Bϵ(z∗),s∈ℜb
+ F (z, s)
(3.5.22)
It should be clear that z∗, 0b solves Problem (3.5.22). The first order con-
ditions for Problem (3.5.22) are just that the partial derivatives of F with
respect to the remaining n −b choice variables equal zero (according to
the first order conditions for unconstrained optimisation), while the partial
derivatives of F with respect to the b slack variables must be less than or
equal to zero.
5. The Kuhn-Tucker multipliers can now be found exactly as in the Lagrange
case. We know that
DzF = DyfDzh + DzfIn−b
=
0n−b.
Substituting for Dzh from (3.5.19) gives:
Dyf (Dyg)−1 Dzg = Dzf.
We can also partition f ′ (x) as

Dyf (Dyg)−1 Dyg
Dzf

Substituting for the second sub-matrix yields:
f ′ (x)
=

Dyf (Dyg)−1 Dyg
Dyf (Dyg)−1 Dzg

=
Dyf (Dyg)−1 
Dyg
Dzg

≡
−λ ⊤g′ (x)
where we define the Kuhn-Tucker multipliers corresponding to the binding
constraints, λ , by
λ ≡−Dyf (Dyg)−1 .
(3.5.23)
6. Next, we calculate the partial derivatives of F with respect to the slack
variables and show that they can be less than or equal to zero if and only
if the Kuhn-Tucker multipliers corresponding to the binding constraints are
greater than or equal to zero. This can be seen by differentiating both sides
of (3.5.21) with respect to s to obtain:
DsF
=
DyfDsh + Dzf0(n−b)×b
(3.5.24)
=
Dyf (Dyg)−1
(3.5.25)
=
−λ ,
(3.5.26)
where we have used (3.5.20) and (3.5.23).
Revised: December 2, 1998

CHAPTER 3. CONVEXITY AND OPTIMISATION
55
7. Finally just set the Kuhn-Tucker multipliers corresponding to the non-binding
constraints equal to zero.
Q.E.D.
Theorem 3.5.2 Second order (sufficient or concavity) conditions for optimisation
with inequality constraints.
If
1. f and g are differentiable,
2. ∃λ ∈ℜm such that f ′ (x∗)+λ⊤g′ (x∗) = 0, with λi ≥0 for i = 1, 2, . . . , m
and gi(x∗) = 0 if λi > 0 (i.e. the first order conditions are satisfied at x∗),
3. f is pseudoconcave, and
4. gi (x∗) = 0, i = 1, 2, . . . , b; gi (x∗) > 0, i = b + 1, . . . , m and gj is qua-
siconcave for j = 1, . . . , b (i.e. the binding constraint functions are quasi-
concave),
then x∗solves the constrained maximisation problem.
Proof The proof just requires the first order conditions to be reduced to
f ′ (x∗) +
b
X
i=1
λigi′ (x∗) = 0
(3.5.27)
from where it is virtually identical to that for the Lagrange case, and so it is left as
an exercise.
Q.E.D.
Theorem 3.5.3 Uniqueness condition for inequality constrained optimisation.
If
1. x∗is a solution,
2. f is strictly quasiconcave, and
3. gj is a quasiconcave function for j = 1, . . . , m,
then x∗is the unique (global) optimal solution.
Revised: December 2, 1998

56
3.5. INEQUALITY CONSTRAINED OPTIMISATION:
THE KUHN-TUCKER THEOREMS
Proof The proof is again similar to that for the Lagrange case and is left as an ex-
ercise. The point to note this time is that the feasible set with equality constraints
was convex if the constraint functions were affine, whereas the feasible set with
inequality constraints is convex if the constraint functions are quasiconcave. This
is because the feasible set (where all the inequality constraints are satisfied simul-
taneously) is the intersection of m upper contour sets of quasiconcave functions,
or the intersection of m convex sets.
Q.E.D.
The last important result on optimisation, the Theorem of the Maximum, is closely
related to the Envelope Theorem. Before proceeding to the statement of the theo-
rem, the reader may want to review Definition 2.3.12.
Theorem 3.5.4 (Theorem of the maximum) Consider the modified inequality con-
strained optimisation problem:
max
x
f (x, α)
subject to
gi (x, α) ≥0, i = 1, . . . , m
(3.5.28)
where x ∈ℜn, α∈ℜq, f: ℜn+q →ℜand g: ℜn+q →ℜm.
Let x∗(α) denote the optimal choice of x for given α (x∗: ℜq →ℜn) and let
M (α) denote the maximum value attainable by f for given α (M: ℜq →ℜ).
If
1. f is continuous;
2. the range of f is closed and bounded; and
3. the constraint set is a non-empty, compact-valued, continuous correspon-
dence of α,
then
1. M is a continuous (single-valued) function; and
2. x∗is an upper hemi-continuous correspondence, and hence is continuous if
it is a continuous (single-valued) function.
Proof The proof of this theorem is omitted, along with some of the more technical
material on continuity of (multi-valued) correspondences.
Q.E.D.
Theorem 3.5.4 will be used in consumer theory to prove such critical results as
the continuity of demand functions derived from the maximisation of continuous
utility functions.
The following are two frequently encountered examples illustrating the use of the
Kuhn-Tucker theorems in economics.7
7The calculations should be left as exercises.
Revised: December 2, 1998

CHAPTER 3. CONVEXITY AND OPTIMISATION
57
1. The canonical quadratic programming problem.
Find the vector x ∈ℜn which maximises the value of the quadratic form
x⊤Ax subject to the m linear inequality constraints gi⊤x ≥αi, where
A ∈ℜn×n is negative definite and gi ∈ℜn for i = 1, . . . , m.
The objective function can always be rewritten as a quadratic form in a
symmetric (negative definite) matrixl, since as x⊤Ax is a scalar,
x⊤Ax
=

x⊤Ax
⊤
(3.5.29)
=
x⊤A⊤x
(3.5.30)
=
1
2

x⊤Ax + x⊤A⊤x

(3.5.31)
=
x⊤
1
2

A + A⊤
x
(3.5.32)
and 1
2

A + A⊤
is always symmetric.
Let G be the m × n matrix whose ith row is gi. G must have full rank if
we are to apply the Kuhn-Tucker conditions.
The Lagrangean is:
x⊤Ax + λ⊤(Gx −α) .
(3.5.33)
The first order conditions are:
2x⊤A + λ⊤G = 0n
(3.5.34)
or, transposing and multiplying across by 1
2A−1:
x = −1
2A−1G⊤λ.
(3.5.35)
If the constraints are binding, then we will have:
α = −1
2GA−1G⊤λ.
(3.5.36)
Now we need the fact that G (and hence GA−1G⊤) has full rank to solve
for the Lagrange multipliers λ:
λ = −2

GA−1G⊤−1 α.
(3.5.37)
Now the sign conditions tell us that each component of λ must be non-
negative. An easy fix is to let the Kuhn-Tucker multipliers be defined by:
λ∗≡max

0m, −2

GA−1G⊤−1 α

,
(3.5.38)
Revised: December 2, 1998

58
3.6. DUALITY
where the max operator denotes component-by-component maximisation.
The effect of this is to knock out the non-binding constraints (those with
negative Lagrange multipliers) from the original problem and the subse-
quent analysis.
We can now find the optimal x by substituting for λ in (3.5.35) the value of
λ∗from (3.5.38).
In the case in which all the constraints are binding, the solution is:
x = A−1G⊤
GA−1G⊤−1 α
(3.5.39)
and the envelope function is given by:
x⊤Ax
=
α⊤
GA−1G⊤−1 GA−1AA−1G⊤
GA−1G⊤−1 α
=
α⊤
GA−1G⊤−1 α
=
−1
2α⊤λ.
(3.5.40)
The applications of this problem will include ordinary least squares and
generalised least squares regression and the mean-variance portfolio choice
problem in finance.
2. Maximising a Cobb-Douglas utility function subject to a budget constraint
and non-negativity constraints.
The applications of this problem will include choice under certainty, choice
under uncertainty with log utility where the parameters are reinterpreted as
probabilities, the extension to Stone-Geary preferences, and intertemporal
choice with log utility, where the parameters are reinterpreted as time dis-
count factors.
Further exercises consider the duals of each of the forgoing problems, and it is to
the question of duality that we will turn in the next section.
3.6
Duality
Let X ⊆ℜn and let f, g : X 7→ℜbe, respectively, pseudoconcave and pseudo-
convex functions. Consider the envelope functions defined by the dual families of
problems:
M (α) ≡max
x
f (x) s.t. g (x) ≤α
(3.6.1)
Revised: December 2, 1998

CHAPTER 3. CONVEXITY AND OPTIMISATION
59
and
N (β) ≡min
x g (x) s.t. f (x) ≥β.
(3.6.2)
Suppose that these problems have solutions, say x∗(α) and x† (β) respectively,
and that the constraints bind at these points.
The first order conditions for the two problems are respectively:
f ′ (x) −λg′ (x) = 0
(3.6.3)
and
g′ (x) + µf ′ (x) = 0,
(3.6.4)
where λ and µ are the relevant Lagrange multipliers.
Thus if x and λ∗̸= 0 solve (3.6.3), then x and µ∗≡−1/λ solve (3.6.4). However,
for the x which solves the original problem (3.6.1) to also solve (3.6.2), it must
also satisfy the constraint, or f (x) = β. But we know that f (x) = M (α) . This
allows us to conclude that:
x∗(α) = x† (M (α)) .
(3.6.5)
Similarly,
x† (β) = x∗(N (β)) .
(3.6.6)
Combining these equations leads to the conclusion that
α = N (M (α))
(3.6.7)
and
β = M (N (β)) .
(3.6.8)
In other words, the envelope functions for the two dual problems are inverse func-
tions (over any range where the Lagrange multipliers are non-zero, i.e. where the
constraints are binding). Thus, either α or β or indeed λ or µ can be used to
parameterise either family of problems.
We will see many examples of these principles in the applications in the next part
of the book. In particular, duality will be covered further in the context of its
applications to consumer theory in Section 4.6.
Revised: December 2, 1998

