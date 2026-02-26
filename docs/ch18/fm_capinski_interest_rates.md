# Variable & Stochastic Interest Rates

!!! info "Source"
    **Mathematics for Finance: An Introduction to Financial Engineering** by Marek Capinski and Tomasz Zastawniak, Springer, 2003.
    These notes are used for educational purposes.

## Risk-Free Assets

22
Mathematics for Finance
2.1.1 Simple Interest
Suppose that an amount is paid into a bank account, where it is to earn interest.
The future value of this investment consists of the initial deposit, called the
principal and denoted by P, plus all the interest earned since the money was
deposited in the account.
To begin with, we shall consider the case when interest is attracted only
by the principal, which remains unchanged during the period of investment.
For example, the interest earned may be paid out in cash, credited to another
account attracting no interest, or credited to the original account after some
longer period.
After one year the interest earned will be rP, where r > 0 is the interest
rate. The value of the investment will thus become V (1) = P + rP = (1 + r)P.
After two years the investment will grow to V (2) = (1 + 2r)P. Consider a
fraction of a year. Interest is typically calculated on a daily basis: the interest
earned in one day will be
1
365rP. After n days the interest will be
n
365rP and
the total value of the investment will become V ( n
365) = (1 +
n
365r)P. This
motivates the following rule of simple interest: The value of the investment at
time t, denoted by V (t), is given by
V (t) = (1 + tr)P,
(2.1)
where time t, expressed in years, can be an arbitrary non-negative real number;
see Figure 2.1. In particular, we have the obvious equality V (0) = P. The
number 1+rt is called the growth factor. Here we assume that the interest rate
r is constant. If the principal P is invested at time s, rather than at time 0,
then the value at time t ≥s will be
V (t) = (1 + (t −s)r)P.
(2.2)
Figure 2.1
Principal attracting simple interest at 10% (r = 0.1, P = 1)

2. Risk-Free Assets
23
Throughout this book the unit of time will be one year. We shall transform
any period expressed in other units (days, weeks, months) into a fraction of a
year.
Example 2.1
Consider a deposit of $150 held for 20 days and attracting simple interest at
a rate of 8%. This gives t =
20
365 and r = 0.08. After 20 days the deposit will
grow to V ( 20
365) = (1 + 20
365 × 0.08) × 150 ∼= 150.66.
The return on an investment commencing at time s and terminating at time
t will be denoted by K(s, t). It is given by
K(s, t) = V (t) −V (s)
V (s)
.
(2.3)
In the case of simple interest
K(s, t) = (t −s)r,
which clearly follows from (2.2). In particular, the interest rate is equal to the
return over one year,
K(0, 1) = r.
As a general rule, interest rates will always refer to a period of one year, fa-
cilitating the comparison between different investments, independently of their
actual duration. By contrast, the return reflects both the interest rate and the
length of time the investment is held.
Exercise 2.1
A sum of $9, 000 paid into a bank account for two months (61 days) to
attract simple interest will produce $9, 020 at the and of the term. Find
the interest rate r and the return on this investment.
Exercise 2.2
How much would you pay today to receive $1, 000 at a certain future
date if you require a return of 2%?
Exercise 2.3
How long will it take for a sum of $800 attracting simple interest to
become $830 if the rate is 9%? Compute the return on this investment.

24
Mathematics for Finance
Exercise 2.4
Find the principal to be deposited initially in an account attracting sim-
ple interest at a rate of 8% if $1, 000 is needed after three months (91
days).
The last exercise is concerned with an important general problem: Find the
initial sum whose value at time t is given. In the case of simple interest the
answer is easily found by solving (2.1) for the principal, obtaining
V (0) = V (t)(1 + rt)−1.
(2.4)
This number is called the present or discounted value of V (t) and (1 + rt)−1 is
the discount factor.
Example 2.2
A perpetuity is a sequence of payments of a fixed amount to be made at equal
time intervals and continuing indefinitely into the future. For example, suppose
that payments of an amount C are to be made once a year, the first payment
due a year hence. This can be achieved by depositing
P = C
r
in a bank account to earn simple interest at a constant rate r. Such a deposit
will indeed produce a sequence of interest payments amounting to C = rP
payable every year.
In practice simple interest is used only for short-term investments and for
certain types of loans and deposits. It is not a realistic description of the value
of money in the longer term. In the majority of cases the interest already earned
can be reinvested to attract even more interest, producing a higher return than
that implied by (2.1). This will be analysed in detail in what follows.
2.1.2 Periodic Compounding
Once again, suppose that an amount P is deposited in a bank account, at-
tracting interest at a constant rate r > 0. However, in contrast to the case of
simple interest, we assume that the interest earned will now be added to the
principal periodically, for example, annually, semi-annually, quarterly, monthly,
or perhaps even on a daily basis. Subsequently, interest will be attracted not

2. Risk-Free Assets
25
just by the original deposit, but also by all the interest earned so far. In these
circumstances we shall talk of discrete or periodic compounding.
Example 2.3
In the case of monthly compounding the first interest payment of
r
12P will be
due after one month, increasing the principal to (1 +
r
12)P, all of which will
attract interest in the future. The next interest payment, due after two months,
will thus be
r
12(1 +
r
12)P, and the capital will become (1 +
r
12)2P. After one
year it will become (1 + r
12)12P, after n months it will be (1 + r
12)nP, and after
t years (1 +
r
12)12tP. The last formula admits t equal to a whole number of
months, that is, a multiple of
1
12.
In general, if m interest payments are made per annum, the time between
two consecutive payments measured in years will be
1
m, the first interest pay-
ment being due at time
1
m. Each interest payment will increase the principal
by a factor of 1 + r
m. Given that the interest rate r remains unchanged, after t
years the future value of an initial principal P will become
V (t) =

1 + r
m
tm
P,
(2.5)
because there will be tm interest payments during this period. In this formula
t must be a whole multiple of the period
1
m. The number

1 + r
m
tm is the
growth factor.
The exact value of the investment may sometimes need to be known at time
instants between interest payments. In particular, this may be so if the account
is closed on a day when no interest payment is due. For example, what is the
value after 10 days of a deposit of $100 subject to monthly compounding at
12%? One possible answer is $100, since the first interest payment would be
due only after one whole month. This suggests that (2.5) should be extended
to arbitrary values of t by means of a step function with steps of duration
1
m,
as shown in Figure 2.2. Later on, in Remark 2.6 we shall see that the extension
consistent with the No-Arbitrage Principle should use the right-hand side of
(2.5) for all t ≥0.
Exercise 2.5
How long will it take to double a capital attracting interest at 6% com-
pounded daily?

26
Mathematics for Finance
Figure 2.2
Annual compounding at 10% (m = 1, r = 0.1, P = 1)
Exercise 2.6
What is the interest rate if a deposit subject to annual compounding is
doubled after 10 years?
Exercise 2.7
Find and compare the future value after two years of a deposit of $100
attracting interest at a rate of 10% compounded a) annually and b) semi-
annually.
Proposition 2.1
The future value V (t) increases if any one of the parameters m, t, r or P
increases, the others remaining unchanged.
Proof
It is immediately obvious from (2.5) that V (t) increases if t, r or P increases.
To show that V (t) increases as the compounding frequency m increases, we
need to verify that if m < k, then

1 + r
m
tm
<

1 + r
k
tk
.
The latter clearly reduces to

1 + r
m
m
<

1 + r
k
k
,

2. Risk-Free Assets
27
which can be verified directly using the binomial formula:

1 + r
m
m
= 1 + r + 1 −1
m
2!
r2 + · · · +

1 −1
m

× · · · ×

1 −m−1
m

m!
rm
≤1 + r + 1 −1
k
2!
r2 + · · · +

1 −1
k

× · · · ×

1 −m−1
k

m!
rm
< 1 + r + 1 −1
k
2!
r2 + · · · +

1 −1
k

× · · · ×

1 −k−1
k

k!
rk
=

1 + r
k
k
.
The first inequality holds because each term of the sum on the left-hand side
is no greater than the corresponding term on the right-hand side. The second
inequality is true because the sum on the right-hand side contains m −k ad-
ditional non-zero terms as compared to the sum on the left-hand side. This
completes the proof.
Exercise 2.8
Which will deliver a higher future value after one year, a deposit of
$1, 000 attracting interest at 15% compounded daily, or at 15.5% com-
pounded semi-annually?
Exercise 2.9
What initial investment subject to annual compounding at 12% is needed
to produce $1, 000 after two years?
The last exercise touches upon the problem of finding the present value
of an amount payable at some future time instant in the case when periodic
compounding applies. Here the formula for the present or discounted value of
V (t) is
V (0) = V (t)(1 + r
m)−tm,
the number (1 + r
m)−tm being the discount factor.
Remark 2.1
Fix the terminal value V (t) of an investment. It is an immediate consequence
of Proposition 2.1 that the present value increases if any one of the factors r,
t, m decreases, the other ones remaining unchanged.

28
Mathematics for Finance
Exercise 2.10
Find the present value of $100, 000 to be received after 100 years if
the interest rate is assumed to be 5% throughout the whole period and
a) daily or b) annual compounding applies.
One often requires the value V (t) of an investment at an intermediate time
0 < t < T, given the value V (T) at some fixed future time T. This can be
achieved by computing the present value of V (T), taking it as the principal,
and running the investment forward up to time t. Under periodic compounding
with frequency m and interest rate r, this obviously gives
V (t) =

1 + r
m
−(T −t)m
V (T).
(2.6)
To find the return on a deposit attracting interest compounded periodically
we use the general formula (2.3) and readily arrive at
K(s, t) = V (t) −V (s)
V (s)
= (1 + r
m)(t−s)m −1.
In particular,
K(0, 1
m) = r
m,
which provides a simple way of computing the interest rate given the return.
Exercise 2.11
Find the return over one year under monthly compounding with r =
10%.
Exercise 2.12
Which is greater, the interest rate r or the return K(0, 1) if the com-
pounding frequency m is greater than 1?
Remark 2.2
The return on a deposit subject to periodic compounding is not additive. Take,
for simplicity, m = 1. Then
K(0, 1) = K(1, 2) = r,
K(0, 2) = (1 + r)2 −1 = 2r + r2,
and clearly K(0, 1) + K(1, 2) ̸= K(0, 2).

2. Risk-Free Assets
29
2.1.3 Streams of Payments
An annuity is a sequence of finitely many payments of a fixed amount due
at equal time intervals. Suppose that payments of an amount C are to be
made once a year for n years, the first one due a year hence. Assuming that
annual compounding applies, we shall find the present value of such a stream
of payments. We compute the present values of all payments and add them up
to get
C
1 + r +
C
(1 + r)2 +
C
(1 + r)3 + · · · +
C
(1 + r)n .
It is sometimes convenient to introduce the following seemingly cumbersome
piece of notation:
PA(r, n) =
1
1 + r +
1
(1 + r)2 + · · · +
1
(1 + r)n .
(2.7)
This number is called the present value factor for an annuity. It allows us to
express the present value of an annuity in a concise form:
PA(r, n) × C.
The expression for PA(r, n) can be simplified by using the formula
a + qa + q2a + · · · + qn−1a = a1 −qn
1 −q .
In our case a =
1
1+r and q =
1
1+r, hence
PA(r, n) = 1 −(1 + r)−n
r
.
(2.8)
Remark 2.3
Note that an initial bank deposit of
P = PA(r, n) × C =
C
1 + r +
C
(1 + r)2 + · · · +
C
(1 + r)n
attracting interest at a rate r compounded annually would produce a stream
of n annual payments of C each. A deposit of C(1 + r)−1 would grow to C
after one year, which is just what is needed to cover the first annuity payment.
A deposit of C(1 + r)−2 would become C after two years to cover the second
payment, and so on. Finally, a deposit of C(1 + r)−n would deliver the last
payment of C due after n years.

30
Mathematics for Finance
Example 2.4
Consider a loan of $1, 000 to be paid back in 5 equal instalments due at yearly
intervals. The instalments include both the interest payable each year calculated
at 15% of the current outstanding balance and the repayment of a fraction of
the loan. A loan of this type is called an amortised loan. The amount of each
instalment can be computed as
1, 000
PA(15%, 5)
∼= 298.32.
This is because the loan is equivalent to an annuity from the point of view of
the lender.
Exercise 2.13
What is the amount of interest included in each instalment? How much
of the loan is repaid as part of each instalment? What is the outstanding
balance of the loan after each instalment is paid?
Exercise 2.14
How much can you borrow if the interest rate is 18%, you can afford to
pay $10, 000 at the end of each year, and you want to clear the loan in
10 years?
Exercise 2.15
Suppose that you deposit $1, 200 at the end of each year for 40 years,
subject to annual compounding at a constant rate of 5%. Find the bal-
ance after 40 years.
Exercise 2.16
Suppose that you took a mortgage of $100, 000 on a house to be paid
back in full by 10 equal annual instalments, each consisting of the in-
terest due on the outstanding balance plus a repayment of a part of
the amount borrowed. If you decided to clear the mortgage after eight
years, how much money would you need to pay on top of the 8th instal-
ment, assuming that a constant annual compounding rate of 6% applies
throughout the period of the mortgage?
Recall that a perpetuity is an infinite sequence of payments of a fixed amount
C occurring at the end of each year. The formula for the present value of a

2. Risk-Free Assets
31
perpetuity can be obtained from (2.7) in the limit as n →∞:
lim
n→∞PA(r, n) × C =
C
1 + r +
C
(1 + r)2 +
C
(1 + r)3 + · · · = C
r .
(2.9)
The limit amounts to taking the sum of a geometric series.
Remark 2.4
The present value of a perpetuity is given by the same formula as in Exam-
ple 2.2, even though periodic compounding has been used in place of simple
interest. In both cases the annual payment C is exactly equal to the interest
earned throughout the year, and the amount remaining to earn interest in the
following year is always C
r . Nevertheless, periodic compounding allows us to
view the same sequence of payments in a different way: The present value C
r
of the perpetuity is decomposed into infinitely many parts, as in (2.9), each
responsible for producing one future payment of C.
Remark 2.5
Formula (2.8) for the annuity factor is easier to memorise in the following way,
using the formula for a perpetuity: The sequence of n payments of C = 1 can
be represented as the difference between two perpetuities, one starting now
and the other after n years. (Cutting offthe tail of a perpetuity, we obtain
an annuity.) In doing so we need to compute the present value of the latter
perpetuity. This can be achieved by means of the discount factor (1 + r)−n.
Hence,
PA(r, n) = 1
r −1
r ×
1
(1 + r)n = 1 −(1 + r)−n
r
.
Exercise 2.17
Find a formula for the present value of an infinite stream of payments
of the form C, C(1 + g), C(1 + g)2, . . . , growing at a constant rate g. By
the tail-cutting procedure find a formula for the present value of n such
payments.

32
Mathematics for Finance
2.1.4 Continuous Compounding
Formula (2.5) for the future value at time t of a principal P attracting interest
at a rate r > 0 compounded m times a year can be written as
V (t) =

1 + r
m
 m
r tr
P.
In the limit as m →∞, we obtain
V (t) = etrP,
(2.10)
where
e = lim
x→∞
	
1 + 1
x

x
is the base of natural logarithms. This is known as continuous compounding.
The corresponding growth factor is etr. A typical graph of V (t) is shown in
Figure 2.3.
Figure 2.3
Continuous compounding at 10% (r = 0.1, P = 1)
The derivative of V (t) = etrP is
V ′(t) = retrP = rV (t).
In the case of continuous compounding the rate of the growth is proportional
to the current wealth.
Formula (2.10) is a good approximation of the case of periodic compounding
when the frequency m is large. It is simpler and lends itself more readily to
transformations than the formula for periodic compounding.

2. Risk-Free Assets
33
Exercise 2.18
How long will it take to earn $1 in interest if $1, 000, 000 is deposited at
10% compounded continuously?
Exercise 2.19
In 1626 Peter Minuit, governor of the colony of New Netherland, bought
the island of Manhattan from Indians paying with beads, cloth, and
trinkets worth $24. Find the value of this sum in year 2000 at 5% com-
pounded a) continuously and b) annually.
Proposition 2.2
Continuous compounding produces higher future value than periodic com-
pounding with any frequency m, given the same initial principal P and interest
rate r.
Proof
It suffices to verify that
etr > (1 + r
m)tm =

(1 + r
m)
m
r
rt
.
The inequality holds because the sequence (1+ r
m)
m
r is increasing and converges
to e as m ↗∞.
Exercise 2.20
What will be the difference between the value after one year of $100
deposited at 10% compounded monthly and compounded continuously?
How frequent should the periodic compounding be for the difference to
be less than $0.01?
The present value under continuous compounding is obviously given by
V (0) = V (t)e−tr.
In this case the discount factor is e−tr. Given the terminal value V (T), we
clearly have
V (t) = e−r(T −t)V (T).
(2.11)

34
Mathematics for Finance
Exercise 2.21
Find the present value of $1, 000, 000 to be received after 20 years as-
suming continuous compounding at 6%.
Exercise 2.22
Given that the future value of $950 subject to continuous compounding
will be $1, 000 after half a year, find the interest rate.
The return K(s, t) defined by (2.3) on an investment subject to continuous
compounding fails to be additive, just like in the case of periodic compounding.
It proves convenient to introduce the logarithmic return
k(s, t) = ln V (t)
V (s).
(2.12)
Proposition 2.3
The logarithmic return is additive,
k(s, t) + k(t, u) = k(s, u).
Proof
This is an easy consequence of (2.12):
k(s, t) + k(t, u) = ln V (t)
V (s) + ln V (u)
V (t)
= ln V (t)
V (s)
V (u)
V (t) = ln V (u)
V (s) = k(s, u).
If V (t) is given by (2.10), then k(s, t) = r(t−s), which enables us to recover
the interest rate
r = k(s, t)
t −s .
Exercise 2.23
Suppose that the logarithmic return over 2 months on an investment
subject to continuous compounding is 3%. Find the interest rate.

2. Risk-Free Assets
35
2.1.5 How to Compare Compounding Methods
As we have already noticed, frequent compounding will produce a higher fu-
ture value than less frequent compounding if the interest rates and the initial
principal are the same. We shall consider the general circumstances in which
one compounding method will produce either the same or higher future value
than another method, given the same initial principal.
Example 2.5
Suppose that certificates promising to pay $120 after one year can be purchased
or sold now, or at any time during this year, for $100. This is consistent with a
constant interest rate of 20% under annual compounding. If an investor decided
to sell such a certificate half a year after the purchase, what price would it fetch?
Suppose it is $110, a frequent first guess based on halving the annual profit of
$20. However, this turns out to be too high a price, leading to the following
arbitrage strategy:
• Borrow $1, 000 to buy 10 certificates for $100 each.
• After six months sell the 10 certificates for $110 each and buy 11 new
certificates for $100 each. The balance of these transactions is nil.
• After another six months sell the 11 certificates for $110 each, cashing
$1, 210 in total, and pay $1, 200 to clear the loan with interest. The balance
of $10 would be the arbitrage profit.
A similar argument shows that the certificate price after six months cannot be
too low, say, $109.
The price of a certificate after six months is related to the interest rate
under semi-annual compounding: If this rate is r, then the price is 100

1 + r
2

dollars and vice versa. Arbitrage will disappear if the corresponding growth
factor

1 + r
2
2 over one year is equal to the growth factor 1.2 under annual
compounding,

1 + r
2
2
= 1.2,
which gives r ∼= 0.1909, or 19.09%. If so, then the certificate price after six
months should be 100

1 + 0.1909
2
 ∼= 109.54 dollars.
The idea based on considering the growth factors over a fixed period, typi-
cally one year, can be used to compare any two compounding methods.

36
Mathematics for Finance
Definition 2.1
We say that two compounding methods are equivalent if the corresponding
growth factors over a period of one year are the same. If one of the growth
factors exceeds the other, then the corresponding compounding method is said
to be preferable.
Example 2.6
Semi-annual compounding at 10% is equivalent to annual compounding at
10.25%. Indeed, in the former case the growth factor over a period of one
year is
	
1 + 0.1
2

2
= 1.1025,
which is the same as the growth factor in the latter case. Both are preferable
to monthly compounding at 9%, for which the growth factor over one year is
only
	
1 + 0.09
12

12
∼= 1.0938.
We can freely switch from one compounding method to another equivalent
method by recalculating the interest rate. In the chapters to follow we shall
normally use either annual or continuous compounding.
Exercise 2.24
Find the rate for continuous compounding equivalent to monthly com-
pounding at 12%.
Exercise 2.25
Find the frequency of periodic compounding at 20% to be equivalent to
annual compounding at 21%.
Instead of comparing the growth factors, it is often convenient to compare
the so-called effective rates as defined below.
Definition 2.2
For a given compounding method with interest rate r the effective rate re is
one that gives the same growth factor over a one year period under annual
compounding.

2. Risk-Free Assets
37
In particular, in the case of periodic compounding with frequency m and
rate r the effective rate re satisfies

1 + r
m
m
= 1 + re.
In the case of continuous compounding with rate r
er = 1 + re.
Example 2.7
In the case of semi-annual compounding at 10% the effective rate is 10.25%,
see Example 2.6.
Proposition 2.4
Two compounding methods are equivalent if and only if the corresponding
effective rates re and r′
e are equal, re = r′
e. The compounding method with
effective rate re is preferable to the other method if and only if re > r′
e.
Proof
This is because the growth factors over one year are 1 + re and 1 + r′
e, respec-
tively.
Example 2.8
In Exercise 2.8 we have seen that daily compounding at 15% is preferable to
semi-annual compounding at 15.5%. The corresponding effective rates re and
r′
e can be found from
1 + re =
	
1 + 0.15
365

365
∼= 1.1618,
1 + r′
e =
	
1 + 0.155
2

2
∼= 1.1610.
This means that re is about 16.18% and r′
e about 16.10%.
Remark 2.6
Recall that formula (2.5) for periodic compounding, that is,
V (t) =

1 + r
m
tm
P,

38
Mathematics for Finance
admits only time instants t being whole multiples of the compounding period
1
m. An argument similar to that in Example 2.5 shows that the appropriate no-
arbitrage value of an initial sum P at any time t ≥0 should be

1 + r
m
tm P.
A reasonable extension of (2.5) is therefore to use the right-hand side for all
t ≥0 rather than just for whole multiples of
1
m. From now on we shall always
use this extension.
In terms of the effective rate re the future value can be written as
V (t) = (1 + re)t P.
for all t ≥0. This applies both to continuous compounding and to periodic
compounding extended to arbitrary times as in Remark 2.6. Proposition 2.4
implies that, given the same initial principal, equivalent compounding methods
will produce the same future value for all times t ≥0. Similarly, a compounding
method preferable to another one will produce a higher future value for all t > 0.
Remark 2.7
Simple interest does not fit into the scheme for comparing compounding meth-
ods. In this case the future value V (t) is a linear function of time t, whereas it is
an exponential function if either continuous or periodic compounding applies.
The graphs of such functions have at most two intersection points, so they can
never be equal to one another for all times t ≥0 (except for the trivial case of
zero principal).
Exercise 2.26
What is the present value of an annuity consisting of monthly payments
of an amount C continuing for n years? Express the answer in terms of
the effective rate re.
Exercise 2.27
What is the present value of a perpetuity consisting of bimonthly pay-
ments of an amount C? Express the answer in terms of the effective
rate re.

2. Risk-Free Assets
39
2.2 Money Market
The money market consists of risk-free (more precisely, default-free) securi-
ties. An example is a bond, which is a financial security promising the holder
a sequence of guaranteed future payments. Risk-free means here that these
payments will be delivered with certainty. (Nevertheless, even in this case risk
cannot be completely avoided, since the market prices of such securities may
fluctuate unpredictably; see Chapters 10 and 11.) There are many kinds of
bonds like treasury bills and notes, treasury, mortgage and debenture bonds,
commercial papers, and others with various particular arrangements concern-
ing the issuing institution, duration, number of payments, embedded rights and
guarantees.
2.2.1 Zero-Coupon Bonds
The simplest case of a bond is a zero-coupon bond, which involves just a single
payment. The issuing institution (for example, a government, a bank or a com-
pany) promises to exchange the bond for a certain amount of money F, called
the face value, on a given day T, called the maturity date. Typically, the life
span of a zero-coupon bond is up to one year, the face value being some round
figure, for example 100. In effect, the person or institution who buys the bond
is lending money to the bond writer.
Given the interest rate, the present value of such a bond can easily be
computed. Suppose that a bond with face value F = 100 dollars is maturing in
one year, and the annual compounding rate r is 12%. Then the present value
of the bond should be
V (0) = F(1 + r)−1 ∼= 89.29
dollars.
In reality, the opposite happens: Bonds are freely traded and their prices
are determined by market forces, whereas the interest rate is implied by the
bond prices,
r =
F
V (0) −1.
(2.13)
This formula gives the implied annual compounding rate. For instance, if a
one-year bond with face value $100 is being traded at $91, then the implied
rate is 9.89%.
For simplicity, we shall consider unit bonds with face value equal to one unit
of the home currency, F = 1.

40
Mathematics for Finance
Typically, a bond can be sold at any time prior to maturity at the market
price. This price at time t is denoted B(t, T). In particular, B(0, T) is the
current, time 0 price of the bond, and B(T, T) = 1 is equal to the face value.
Again, these prices determine the interest rates by applying formulae (2.6)
and (2.11) with V (t) = B(t, T), V (T) = 1. For example, the implied annual
compounding rate satisfies the equation
B(t, T) = (1 + r)−(T −t).
The last formula has to be suitably modified if a different compounding method
is used. Using periodic compounding with frequency m, we need to solve the
equation
B(t, T) =

1 + r
m
−m(T −t)
.
In the case of continuous compounding the equation for the implied rate satisfies
B(t, T) = e−r(T −t).
Of course all these different implied rates are equivalent to one another, since
the bond price does not depend on the compounding method used.
Remark 2.8
In general, the implied interest rate may depend on the trading time t as well as
on the maturity time T. This is an important issue, which will be discussed in
Chapters 10 and 11. For the time being, we adopt the simplifying assumption
that the interest rate remains constant throughout the period up to maturity.
Exercise 2.28
An investor paid $95 for a bond with face value $100 maturing in six
months. When will the bond value reach $99 if the interest rate remains
constant?
Exercise 2.29
Find the interest rates for annual, semi-annual and continuous com-
pounding implied by a unit bond with B(0.5, 1) = 0.9455.
Note that B(0, T) is the discount factor and B(0, T)−1 is the growth factor
for each compounding method. These universal factors are all that is needed
to compute the time value of money, without resorting to the corresponding
interest rates. However, interest rates are useful because they are more intuitive.

2. Risk-Free Assets
41
For an average bank customer the information that a one-year $100 bond can
be purchased for $92.59 may not be as clear as the equivalent statement that
a deposit will earn 8% interest if kept for one year.
2.2.2 Coupon Bonds
Bonds promising a sequence of payments are called coupon bonds. These pay-
ments consist of the face value due at maturity, and coupons paid regularly,
typically annually, semi-annually, or quarterly, the last coupon due at maturity.
The assumption of constant interest rates allows us to compute the price of a
coupon bond by discounting all the future payments.
Example 2.9
Consider a bond with face value F = 100 dollars maturing in five years, T = 5,
with coupons of C = 10 dollars paid annually, the last one at maturity. This
means a stream of payments of 10, 10, 10, 10, 110 dollars at the end of each
consecutive year. Given the continuous compounding rate r, say 12%, we can
find the price of the bond:
V (0) = 10e−r + 10e−2r + 10e−3r + 10e−4r + 110e−5r ∼= 90.27
dollars.
Exercise 2.30
Find the price of a bond with face value $100 and $5 annual coupons
that matures in four years, given that the continuous compounding rate
is a) 8% or b) 5%.
Exercise 2.31
Sketch the graph of the price of the bond in Exercise 2.30 as a function
of the continuous compounding rate r. What is the value of this function
for r = 0 ? What is the limit as r →∞?
Example 2.10
We continue Example 2.9. After one year, once the first coupon is cashed, the
bond becomes a four-year bond worth
V (1) = 10e−r + 10e−2r + 10e−3r + 110e−4r ∼= 91.78


## Forward and Futures Contracts

132
Mathematics for Finance
In general, if the contract is initiated at time t < T, then
F(t, T) = S(t)e(r−rdiv)(T −t).
(6.7)
Exercise 6.5
A US importer of German cars wants to arrange a forward contract to
buy euros in half a year. The interest rates for investments in US dollars
and euros are rUSD = 4% and rEUR = 3%, respectively, the current
exchange rate being 0.9834 euros to a dollar. What is the forward price
of euros expressed in dollars (that is, the forward exchange rate)?
6.1.2 Value of a Forward Contract
Every forward contract has value zero when initiated. As time goes by, the price
of the underlying asset may change. Along with it, the value of the forward
contract will vary and will no longer be zero, in general. In particular, the
value of a long forward contract will be S(T) −F(0, T) at delivery, which may
turn out to be positive, zero or negative. We shall derive formulae to capture
the changes in the value of a forward contract.
Suppose that the forward price F(t, T) for a forward contract initiated at
time t, where 0 < t < T, is higher than F(0, T). This is good news for an
investor with a long forward position initiated at time 0. At time T such an
investor will gain F(t, T) −F(0, T) as compared to an investor entering into a
new long forward contract at time t with the same delivery date T. To find the
value of the original forward position at time t all we have to do is to discount
this gain back to time t. This discounted amount would be received (or paid,
if negative) by the investor with a long position should the forward contract
initiated at time 0 be closed out at time t, that is, prior to delivery T. This
intuitive argument needs to be supported by a rigorous arbitrage proof.
Theorem 6.4
For any t such that 0 ≤t ≤T the time t value of a long forward contract with
forward price F(0, T) is given by
V (t) = [F(t, T) −F(0, T)]e−r(T −t).
(6.8)

6. Forward and Futures Contracts
133
Proof
Suppose that
V (t) < [F(t, T) −F(0, T)]e−r(T −t).
If so, then at time t
• borrow the amount V (t) to enter into a long forward contract with forward
price F(0, T) and delivery time T;
• initiate a short forward position with forward price F(t, T), at no cost.
Next, at time T
• close out the forward contracts collecting (or paying, if negative) the
amounts S(T) −F(0, T) for the long position and −S(T) + F(t, T) for
the short position;
• pay back the loan with interest amounting to V (t)et(T −t) in total.
The final balance F(t, T) −F(0, T) −V (t)et(T −t) > 0 will be your arbitrage
profit.
We leave the case when
V (t) > [F(t, T) −F(0, T)]e−r(T −t)
as an exercise.
Exercise 6.6
Show that V (t) > [F(t, T) −F(0, T)]e−r(T −t) leads to an arbitrage op-
portunity.
Observe that V (0) = 0, which is the initial value of the forward contract,
and V (T) = S(T) −F(0, T) (since F(T, T) = S(T)), which is the terminal
payoff.
For a stock paying no dividends formula (6.8) gives
V (t) = [S(t)er(T −t) −S(0)erT ]e−r(T −t) = S(t) −S(0)ert.
(6.9)
The message is: If the stock price grows at the same rate as a risk-free invest-
ment, then the value of the forward contract will be zero. Growth above the
risk-free rate results in a gain for the holder of a long forward position.
Remark 6.3
Consider a contract with delivery price X rather than F(0, T). The value of
this contract at time t will be given by (6.8) with F(0, T) replaced by X,
VX(t) = [F(t, T) −X]e−r(T −t).

134
Mathematics for Finance
Such a contract may have non-zero value initially. In the case of a stock paying
no dividends
VX(0) = [F(0, T) −X]e−rT = S(0) −Xe−rT .
(6.10)
For a stock paying one dividend between times 0 and T the initial value of the
contract is
VX(0) = S(0) −div0 −Xe−rT ,
div0 being the value of the dividend discounted to time 0. For a stock paying
dividends continuously at a rate rdiv, the initial value of the contract is
VX(0) = S(0)e−rdivT −Xe−rT .
Exercise 6.7
Suppose that the price of a stock is $45 at the beginning of the year, the
risk-free rate is 6%, and a $2 dividend is to be paid after half a year.
For a long forward position with delivery in one year, find its value after
9 months if the stock price at that time turns out to be a) $49, b) $51.
6.2 Futures
One of the two parties to a forward contract will be losing money. There is
always a risk of default by the party suffering a loss. Futures contracts are
designed to eliminate such risk.
We assume for a while that time is discrete with steps of length τ, typically
a day.
Just like a forward contract, a futures contract involves an underlying asset
and a specified time of delivery, a stock with prices S(n) for n = 0, 1, . . . and
time T, say. In addition to the usual stock prices, the market dictates the so-
called futures prices f(n, T) for each step n = 0, 1, . . . such that nτ ≤T. These
prices are unknown at time 0, except for f(0, T), and we shall treat them as
random variables.
As in the case of a forward contract, it costs nothing to initiate a futures
position. The difference lies in the cash flow during the lifetime of the contract.
A long forward contract involves just a single payment S(T) −F(0, T) at de-
livery. A futures contract involves a random cash flow, known as marking to
market. Namely, at each time step n = 1, 2, . . . such that nτ ≤T the holder of
a long futures position will receive the amount
f(n, T) −f(n −1, T)

6. Forward and Futures Contracts
135
if positive, or will have to pay it if negative. The opposite payments apply for
a short futures position. The following two conditions are imposed:
1. The futures price at delivery is f(T, T) = S(T).
2. At each time step n = 0, 1, . . . such that nτ ≤T the value of a futures
position is zero. (At each step n ≥1 this value is computed after marking
to market.)
The second condition means that, in particular, it costs nothing to close, open
or alter a futures position at any time step between 0 and T.
Remark 6.4
To ensure that the obligations involved in a futures position are fulfilled, certain
practical regulations are enforced. Each investor entering into a futures contract
has to pay a deposit, called the initial margin, which is kept by the clearing
house as collateral. In the case of a long futures position the amount f(n, T) −
f(n −1, T) is added to the deposit if positive or subtracted if negative at each
time step n, typically once a day. (The opposite amount is added or subtracted
for a short futures position.) Any excess that builds up above the initial margin
can be withdrawn by the investor. On the other hand, if the deposit drops below
a certain level, called the maintenance margin, the clearing house will issue a
margin call, requesting the investor to make a payment and restore the deposit
to the level of the initial margin. A futures position can be closed at any time,
in which case the deposit will be returned to the investor. In particular, the
futures position will be closed immediately by the clearing house if the investor
fails to respond to a margin call. As a result, the risk of default is eliminated.
Example 6.1
Suppose that the initial margin is set at 10% and the maintenance margin at
5% of the futures price. The table below shows a scenario with futures prices
f(n, T). The columns labelled ‘margin 1’ and ‘margin 2’ show the deposit at the
beginning and at the end of each day, respectively. The ‘payment’ column con-
tains the amounts paid to top up the deposit (negative numbers) or withdrawn

136
Mathematics for Finance
(positive numbers).
n
f(n, T)
cash flow
margin 1
payment
margin 2
0
140
opening:
0
−14
14
1
138
−2
12
0
12
2
130
−8
4
−9
13
3
140
+10
23
+ 9
14
4
150
+10
24
+ 9
15
closing:
15
+15
0
total:
10
On day 0 a futures position is opened and a 10% deposit paid. On day 1 the
futures price drops by $2, which is subtracted from the deposit. On day 2 the
futures price drops further by $8, triggering a margin call because the deposit
falls below 5%. The investor has to pay $9 to restore the deposit to the 10%
level. On day 3 the forward price increases and $9 is withdrawn, leaving a 10%
margin. On day 4 the forward price goes up again, allowing the investor to
withdraw another $9. At the end of the day the investor decides to close the
position, collecting the balance of the deposit. The total of all payments is $10,
the increase in the futures price between day 0 and 4.
Remark 6.5
An important feature of the futures market is liquidity. This is possible due to
standardisation and the presence of a clearing house. Only futures contracts
with particular delivery dates are traded. Moreover, futures contracts on com-
modities such as gold or timber specify standardised delivery arrangements as
well as standardised physical properties of the assets. The clearing house acts
as an intermediary, matching the total of a large number of short and long
futures positions of various sizes. The clearing house also maintains the margin
deposit for each investor to eliminate the risk of default. This is in contrast to
forward contracts negotiated directly between two parties.
6.2.1 Pricing
We shall show that in some circumstances the forward and the futures prices
are the same. Let r be the risk-free rate under continuous compounding.
Theorem 6.5
If the interest rate is constant, then f(0, T) = F(0, T).

6. Forward and Futures Contracts
137
Proof
Suppose for simplicity that marking to market is performed at just two inter-
mediate time instants 0 < t1 < t2 < T. The argument below can readily be
extended to cover more frequent marking to market.
Take a long forward position with forward price F(0, T) and invest the
amount of e−rT F(0, T) risk free. At time T close the risk-free investment, col-
lecting the amount F(0, T), purchase one share for F(0, T) using the forward
contract, and sell the share for the market price S(T). Your final wealth will
be S(T).
Our goal is to replicate this payoffby a suitable strategy using futures
contracts. At time 0
• we open a fraction e−r(T −t1) of a long futures position (at no cost);
• we invest the amount e−rT f(0, T) risk free (this investment will grow to
v0 = f(0, T) at time T).
At time t1
• we receive (or pay) the amount e−r(T −t1)[f(t1, T) −f(0, T)] as a result of
marking to market;
• we invest (or borrow, depending on the sign) e−r(T −t1)[f(t1, T) −f(0, T)]
(this investment will grow to v1 = f(t1, T) −f(0, T) at time T);
• we increase our long futures position to e−r(T −t2) of a contract (at no cost).
At time t2
• we cash (or pay) e−r(T −t2)[f(t2, T) −f(t1, T)] as a result of marking to
market;
• we invest (or borrow, depending on the sign) e−r(T −t2)[f(t2, T) −f(t1, T)]
(this investment will grow to v2 = f(t2, T) −f(t1, T) at time T);
• we increase the long futures position to 1 (at no cost).
At time T
• we close the risk-free investment, collecting the amount v0 + v1 + v2 =
f(t2, T);
• we close the futures position, receiving (or paying) the amount S(T) −
f(t2, T).
The final wealth will be S(T), as before. Therefore, to avoid arbitrage, the
initial investments initiating both strategies have to be the same, that is,
e−rT F(0, T) = e−rT f(0, T),
which proves the claim.
This construction cannot be performed if the interest rate changes unpre-
dictably. However if interest rate changes are known in advance, the argument

138
Mathematics for Finance
can be suitably modified and the equality between the futures and forward
prices remains valid.
In an economy with constant interest rates r we obtain a simple structure
of futures prices,
f(t, T) = S(t)er(T −t)
(6.11)
if the stock pays no dividends. The futures prices are random, but this is caused
entirely by the randomness of the prices of the underlying asset. If the futures
prices depart from the values given by the above formula, it is a reflection of
the market’s view of future interest rate changes.
Exercise 6.8
Suppose the interest rate r is constant. Given S(0), find the price S(1)
of the stock after one day such that the marking to market of futures
with delivery in 3 months is zero on that day.
This exercise shows an important benchmark for the profitability of a fu-
tures position: An investor who wants to take advantage of a predicted increase
in the price of stock above the risk-free rate should enter into a long futures
position. A short futures position will bring a profit should the stock price go
down or increase below the risk-free rate.
6.2.2 Hedging with Futures
The Basis. One relatively simple way to hedge an exposure to stock price
variations is to enter a forward contract. However, a contract of this kind may
not be readily available, not to mention the risk of default. Another possibility is
to hedge using the futures market, which is well-developed, liquid and protected
from the risk of default.
Example 6.2
Let S(0) = 100 dollars and let the risk-free rate be constant at r = 8%. Assume
that marking to market takes place once a month, the time step being τ = 1/12.
Suppose that we wish to sell the stock after 3 months. To hedge the exposure
to stock price variations we enter into one short futures contract on the stock
with delivery in 3 months. The payments resulting from marking to market are
invested (or borrowed), attracting interest at the risk-free rate. The results for
two different stock price scenarios are displayed below. The column labelled

6. Forward and Futures Contracts
139
‘m2m’ represents the payments due to marking to market and the last column
shows the interest accrued up to the delivery date.
Scenario 1
n
S(n)
f(n, 3/12)
m2m
interest
0
100
102.02
1
102
103.37
−1.35
−0.02
2
101
101.67
+1.69
+0.01
3
105
105.00
−3.32
0.00
total:
−2.98
−0.01
In this scenario we sell the stock for $105.00, but marking to market brings
losses, reducing the sum to 105.00 −2.98 −0.01 = 102.01 dollars. Note that if
the marking to market payments were not invested at the risk-free rate, then
the realized sum would be 105.00−2.98 = 102.02 dollars, that is, exactly equal
to the futures price f(0, 3/12).
Scenario 2
n
S(n)
f(n, 3/12)
m2m
interest
0
100
102.02
1
98
99.31
+2.70
+0.04
2
97
97.65
+1.67
+0.01
3
92
92.00
+5.65
0.00
total:
+10.02
+0.05
In this case we sell the stock for $92.00 and benefit from marking to market
along with the interest earned, bringing the final sum to 92.00+10.02+0.05 =
102. 07 dollars. Without the interest the final sum would be 92.00 + 10.02 =
102.02 dollars, once again exactly the futures price f(0, 3/12).
In reality the calculations in Example 6.2 are slightly more complicated
because of the presence of the initial margin, which we have neglected for
simplicity. Some limitations come from the standardisation of futures contracts.
As a result, a difficulty may arise in matching the terms of the contract to our
needs. For example, the exercise dates for futures are typically certain fixed
days in four specified months in a year, for example the third Friday in March,
June, September and December. If we want to close out our investment at the
end of April, we will need to hedge with futures contracts with delivery date
beyond the end of April, for example, in June.

140
Mathematics for Finance
Example 6.3
Suppose we wish to sell stock after 2 months and we hedge using futures with
delivery in 3 months (we work in the same scenarios as in Example 6.2):
Scenario 1
n
S(n)
f(n, 3/12)
m2m
interest
0
100
102.02
1
102
103.37
−1.35
−0.01
2
101
101.67
1.69
0.00
total:
0.34
−0.01
We sell the stock for $101.00, which together with marking to market and
interest will give $101.33.
Scenario 2
n
S(n)
f(n, 3/12)
m2m
interest
0
100
102.02
1
98
99.31
2.70
0.02
2
97
97.65
1.67
0.00
total:
4.37
0.02
In this case we sell the stock for $97.00, and together with marking to market
and interest obtain $101.39.
We almost hit the target, which is the futures price f(0, 2) ∼= 101.34 dollars,
that is, the value of $100 compounded at the risk-free rate.
Remark 6.6
The difference between the spot and futures prices is called the basis (as for
forward contracts):
b(t, T) = S(t) −f(t, T).
(Sometimes the basis is defined as f(t, T) −S(t).) The basis converges to zero
as t →T, since f(T, T) = S(T). In a market with constant interest rates it is
given explicitly by
b(t, T) = S(t)(1 −er(T −t)),
being negative for t < T. If the asset pays dividends at a rate rdiv > r, then
the basis is positive:
b(t, T) = S(t)(1 −e(r−rdiv)(T −t)).

6. Forward and Futures Contracts
141
Going back to the problem of designing a hedge, suppose that we wish to sell
an asset at time t < T. To protect ourselves against a decrease in the asset price,
at time 0 we can short a futures contract with futures price f(0, T). At time t
we shall receive S(t) from selling the asset plus the cash flow f(0, T) −f(t, T)
due to marking to market (for simplicity, we neglect any intermediate cash flow,
assuming that t is the first instance when marking to market takes place), that
is, we obtain
f(0, T) + S(t) −f(t, T) = f(0, T) + b(t, T).
The price f(0, T) is known at time 0, so the risk involved in the hedging position
will be related to the unknown level of the basis. This uncertainty is mainly
concerned with unknown future interest rates.
If the goal of a hedger is to minimise risk, it may be best to use a certain
optimal hedge ratio, that is to enter into N futures contracts, with N not
necessarily equal to the number of shares of the underlying asset held. To see
this compute the risk as measured by the variance of the basis bN(t, T) =
S(t) −Nf(t, T):
Var(bN(t, T)) = σ2
S(t) + N 2σ2
f(t,T ) −2NσS(t)σf(t,T )ρS(t)f(t,T ),
where ρS(t)f(t,T ) is the correlation coefficient between the spot and futures
prices, and σS(t), σf(t,T ) are the standard deviations. The variance is a quadratic
function in N and has a minimum at
N = ρS(t)f(t,T )
σS(t)
σf(t,T )
,
which is the optimal hedge ratio.
Exercise 6.9
Find the optimal hedge ratio if the interest rates are constant.
Futures on Stock Index. A stock exchange index is a weighted average of a
selection of stock prices with weights proportional to the market capitalisation
of stocks. An index of this kind will be approximately proportional to the value
of the market portfolio (see Chapter 5) if the chosen set of stocks is large
enough. For example, the Standard and Poor Index S&P500 is computed using
500 stocks, representing about 80% of trade at the New York Stock Exchange.
For the purposes of futures markets the index can be treated as a security. This
is because the index can be identified with a portfolio, even though in practice
transaction costs would impede trading in this portfolio. The futures prices
f(n, T), expressed in index points, are assumed to satisfy the same conditions
as before. Marking to market is given by the difference f(n, T) −f(n −1, T)

142
Mathematics for Finance
multiplied by a fixed amount ($500 for futures on S&P500). If the number of
stocks included in the index is large, it is possible and convenient to assume
that the index is an asset with dividends paid continuously.
Exercise 6.10
Suppose that the value of a stock exchange index is 13, 500, the futures
price for delivery in 9 months is 14, 100 index points, and the interest
rate is 8%. Find the dividend yield.
Our goal in this section is to study applications of index futures for hedging
based on the Capital Asset Pricing Model introduced in Chapter 5. As we know,
see (5.19), the expected return on a portfolio over a time step of length τ is
given by
µV = rF + (µM −rF )βV ,
where βV is the beta coefficient of the portfolio, µM is the expected return on
the market portfolio and rF is the risk-free return over one time step. By V (n)
we shall denote the value of the portfolio at the nth time step. We assume for
simplicity that the index is equal to the value of the market portfolio, so that
the futures prices are given by
f(n, T) = M(n)(1 + rF )T −n,
M(n) being the value of the market portfolio at the nth time step. (Here we
use discrete time and ordinary returns together with periodic compounding in
the spirit of Portfolio Theory.)
We can form a new portfolio with value V (n) by supplementing the original
portfolio with N short futures contracts on the index with delivery time T.
The initial value V (0) of the new portfolio is the same as the value V (0) of
the original portfolio, since it costs nothing to initiate a futures contract. The
value
V (n) = V (n) −N(f(n, T) −f(n −1, T))
of the new portfolio at the nth step includes the marking to market cash flow.
The return on the new portfolio over the first step is
KV =
V (1) −V (0)
˜V (0)
= V (1) −N(f(1, T) −f(0, T)) −V (0)
V (0)
.
We shall show that the beta coefficient βV of the new portfolio can be modified
arbitrarily by a suitable choice of the futures position N.

6. Forward and Futures Contracts
143
Proposition 6.6
If
N = (βV −a)(1 + rF )V (0)
f(0, T)
,
then βV = a for any given number a.
Proof
We shall compute the beta coefficient from the definition:
βV = Cov(KV , KM)/σ2
M
= Cov(KV , KM)/σ2
M −
1
V (0)Cov(N(f(1, T) −f(0, T)), KM)/σ2
M,
where KM is the return on the market portfolio and KV the return on the
portfolio without futures. Since Cov(f(0, T), KM) = 0 and covariance is linear
with respect to each argument,
Cov(N(f(1, T) −f(0, T)), KM) = NCov(f(1, T), KM).
Inserting the futures price f(1, T) = M(1)(1 + rF )T −1, we have
Cov(f(1, T), KM) = (1 + rF )T −1Cov(M(1), KM).
Again by the linearity of covariance in each argument
Cov(M(1), KM) = M(0)Cov(M(1) −M(0)
M(0)
, KM) = M(0)σ2
M.
Subsequent substitutions give
βV = βV −(1 + rF )T −1NM(0)
V (0)
= βV −N
f(0, T)
V (0)(1 + rF ),
which implies the asserted property.
Corollary 6.7
If a = 0, then µV = rF .
Example 6.4
Suppose that the index drops from M(0) = 890 down to M(1) = 850, that is,
by 4.49% within one time step. Suppose further that the risk-free rate is 1%.

144
Mathematics for Finance
This means that the futures prices on the index (with delivery after 3 steps)
are
f(0, 3) = M(0)(1 + rF )3 = 890 × 1.013 ∼= 916.97,
f(1, 3) = M(1)(1 + rF )3 = 850 × 1.012 ∼= 867.09.
Consider a portfolio with βV = 1.5 and initial value V (0) = 100 dollars. This
portfolio will have negative expected return
µV = rF + (µM −rF )βV
∼= 1% + (−4.49% −1%)1.5 ∼= −7.24%.
To construct a new portfolio with βV = 0 we can supplement the original
portfolio with
N = βV
(1 + rF )V (0)
f(0, 3)
∼= 1.5 × 1.01 × 100
916.97
∼= 0.1652
short forward contracts on the index with delivery after 3 steps.
Suppose that the actual return on the original portfolio during the first
time step happens to be equal to the expected return. This gives V (1) ∼= 92.76
dollars. Marking to market gives a payment of
−N (f(1, 3) −f(0, 3)) ∼= −0.1652 × (867.09 −916.97) ∼= 8.24
dollars due to the holder of N ∼= 0.1652 short forward contracts. This makes
the new portfolio worth
V (1) = V (1) −N (f(1, 3) −f(0, 3)) ∼= 92.76 + 8.24 = 101.00
dollars at time 1, matching the risk-free growth exactly.
Exercise 6.11
Perform the same calculations in the case when the index increases from
890 to 920.
Remark 6.7
The ability to adjust the beta of a portfolio is valuable to investors who may
wish either to reduce or to magnify the systematic risk. For example, suppose
that an investor is able to design a portfolio with superior average performance
to that of the market. By entering into a futures position such that the beta
of the resulting portfolio is zero, the investor will be hedged against adverse
movements of the market. This is crucial in the event of recession, so that the

6. Forward and Futures Contracts
145
superior performance of the portfolio as compared to the market can be turned
into a profit despite a decline in the market. On the other hand, should the
market show some growth, the expected return on the hedged portfolio will be
reduced by comparison because the futures position will result in a loss.
It needs to be emphasized that this type of hedging with futures works only
on average. In particular, setting the beta coefficient to zero will not make the
investment risk-free.
Let us conclude this chapter with a surprising application of index futures.
Example 6.5
In emerging markets short sales are rarely available. This was the case in Poland
in the late 1990’s. However, index futures were traded. Due to the fact that
one of the indices (WIG20) was composed of 20 stocks only, it was possible to
manufacture a short sale of any stock among those 20 by entering into a short
futures position on the index, combined with purchasing a suitable portfolio of
the remaining 19 stocks. With a larger number of stocks comprising the index
the transaction costs would have been too high to make such a construction
practicable.

This page intentionally left blank 

7
Options: General Properties
In Chapters 1 and 4 we have seen simple examples of call and put options
in a one-step discrete-time setting. Here we shall establish some fundamental
properties of options, looking at them from a wider perspective and using con-
tinuous time. Nevertheless, many conclusions will also be valid in discrete time.
Chapter 8 will be devoted to pricing and hedging options.
7.1 Definitions
A European call option is a contract giving the holder the right to buy an asset,
called the underlying, for a price X fixed in advance, known as the exercise price
or strike price, at a specified future time T, called the exercise or expiry time.
A European put option gives the right to sell the underlying asset for the strike
price X at the exercise time T.
An American call or put option gives the right to buy or, respectively, to
sell the underlying asset for the strike price X at any time between now and
a specified future time T, called the expiry time. In other words, an American
option can be exercised at any time up to and including expiry.
The term ‘underlying asset’ has quite general scope. Apart from typical
assets such as stocks, commodities or foreign currency, there are options on
stock indices, interest rates, or even on the snow level at a ski resort. Some
underlying assets may be impossible to buy or sell. The option is then cleared
in cash in a fashion which resembles settling a bet. For example, the holder of
147

148
Mathematics for Finance
a European call option on the Standard and Poor Index (see page 141) with
strike price 800 will gain if the index turns out to be 815 on the exercise date.
The writer of the option will have to pay the holder an amount equal to the
difference 815 −800 = 15 multiplied by a fixed sum of money, say by $100. No
payment will be due if the index turns out to be lower than 800 on the exercise
date.
An option is determined by its payoff, which for a European call is
 S(T) −X
if S(T) > X,
0
otherwise.
This payoffis a random variable, contingent on the price S(T) of the underlying
on the exercise date T. (This explains why options are often referred to as
contingent claims.) It is convenient to use the notation
x+ =
 x
if x > 0,
0
otherwise.
for the positive part of a real number x. Then the payoffof a European call
option can be written as (S(T) −X)+. For a put option the payoffis (X −
S(T))+.
Since the payoffs are non-negative, a premium must be paid to buy an
option. If no premium had to be paid, an investor purchasing an option could
under no circumstances lose money and would in fact make a profit whenever
the payoffturned out to be positive. This would be contrary to the No-Arbitrage
Principle. The premium is the market price of the option.
Establishing bounds and some general properties for option prices is the
primary goal of the present chapter. The next chapter will be devoted to de-
tailed techniques of computing these prices. We assume that options are freely
traded, that is, can readily be bought and sold at the market price. The prices
of calls and puts will be denoted by CE, P E for European options and CA, P A
for American options, respectively. The same constant interest rate r will apply
for lending and borrowing money without risk, and continuous compounding
will be used.
Example 7.1
On 22 March 1997 European calls on Rolls-Royce stock with strike price
220 pence to be exercised on 22 May 1997 traded at 19.5 pence at the London
International Financial Futures Exchange (LIFFE). Suppose that the purchase
of such an option was financed by a loan at 5.23% compounded continuously, so
that 19.5e0.0523× 2
12 ∼= 19.67 pence would have to be paid back on the exercise
date. The investment would bring a profit if the stock price turned out to be
higher than 220 + 19.67 = 239.67 pence on the exercise date.

7. Options: General Properties
149
Exercise 7.1
Find the stock price on the exercise date for a European put option
with strike price $36 and exercise date in three months to produce a
profit of $3 if the option is bought for $4.50, financed by a loan at 12%
compounded continuously.
The gain of an option buyer (writer) is the payoffmodified by the premium
CE or P E paid (received) for the option. At time T the gain of the buyer of a
European call is (S(T)−X)+ −CEerT , where the time value of the premium is
taken into account. For the buyer of a European put the gain is (X −S(T))+ −
P EerT . These gains are illustrated in Figure 7.1. For the writer of an option
the gains are CEerT −(S(T) −X)+ for a call and P EerT −(X −S(T))+ for a
put option. Note that the potential loss for a buyer of a call or put is always
limited to the premium paid. For a writer of an option the loss can be much
higher, even unbounded in the case of a call option.
Figure 7.1
Payoffs (solid lines) and gains (broken lines) for a buyer of Euro-
pean calls and puts
Exercise 7.2
Find the expected gain (or loss) for a holder of a European call option
with strike price $90 to be exercised in 6 months if the stock price on
the exercise date may turn out to be $87, $92 or $97 with probability 1
3
each, given that the option is bought for $8, financed by a loan at 9%
compounded continuously.

150
Mathematics for Finance
7.2 Put-Call Parity
In this section we shall make an important link between the prices of European
call and put options.
Consider a portfolio constructed by and writing and selling one put and
buying one call option, both with the same strike price X and exercise date T.
Adding the payoffs of the long position in calls and the short position in puts,
we obtain the payoffof a long forward contract with forward price X and
delivery time T. Indeed, if S(T) ≥X, then the call will pay S(T) −X and the
put will be worthless. If S(T) < X, then the call will be worth nothing and the
writer of the put will need to pay X −S(T). In either case, the value of the
portfolio will be S(T) −X at expiry, the same as for the long forward position,
see Figure 7.2. As a result, the current value of such a portfolio of options
should be that of the forward contract, which is S(0)−Xe−rT , see Remark 6.3.
This motivates the theorem below. Even though the theorem follows from the
above intuitive argument, we shall give a different proof with a view to possible
generalisations.
Figure 7.2
Long forward payoffconstructed from calls and puts
Theorem 7.1 (Put-Call Parity)
For a stock that pays no dividends the following relation holds between the
prices of European call and put options, both with exercise price X and exercise
time T:
CE −P E = S(0) −Xe−rT .
(7.1)
Proof
Suppose that
CE −P E > S(0) −Xe−rT .
(7.2)
In this case an arbitrage strategy can be constructed as follows: At time 0
• buy one share for S(0);

7. Options: General Properties
151
• buy one put option for P E;
• write and sell one call option for CE;
• invest the sum CE−P E−S(0) (or borrow, if negative) on the money market
at the interest rate r.
The balance of these transactions is 0. Then, at time T
• close out the money market position, collecting (or paying, if negative) the
sum (CE −P E −S(0))erT ;
• sell the share for X either by exercising the put if S(T) ≤X or settling the
short position in calls if S(T) > X.
The balance will be (CE −P E −S(0))erT + X, which is positive by (7.2),
contradicting the No-Arbitrage Principle.
Now suppose that
CE −P E < S(0) −Xe−rT .
(7.3)
Then the following reverse strategy will result in arbitrage: At time 0
• sell short one share for S(0);
• write and sell a put option for P E;
• buy one call option for CE;
• invest the sum S(0)−CE+P E (or borrow, if negative) on the money market
at the interest rate r.
The balance of these transactions is 0. At time T
• close out the money market position, collecting (or paying, if negative) the
sum (S(0) −CE + P E)erT ;
• buy one share for X either by exercising the call if S(T) > X or settling the
short position in puts if S(T) ≤X, and close the short position in stock.
The balance will be (S(0) −CE + P E)erT −X, positive by (7.3), once again
contradicting the No-Arbitrage Principle.
Exercise 7.3
Suppose that a stock paying no dividends is trading at $15.60 a share.
European calls on the stock with strike price $15 and exercise date in
three months are trading at $2.83. The interest rate is r = 6.72%, com-
pounded continuously. What is the price of a European put with the
same strike price and exercise date?
Exercise 7.4
European call and put options with strike price $24 and exercise date
in six months are trading at $5.09 and $7.78. The price of the under-


## Variable Interest Rates

232
Mathematics for Finance
be ln(110, 517.09/100, 000) ∼= 10%. Financial intermediaries may simplify your
task by offering a so-called Forward Rate Agreement and perform the above
construction of the loan on your behalf.
Exercise 10.17
Explain how a deposit of $50, 000 for six months can be arranged to start
in six months and find the rate if y(0, 6) = 6% and y(0, 12) = 7%, where
τ =
1
12.
In general, the initial forward rate f(0, M, N) is an interest rate such that
B(0, N) = B(0, M)e−(N−M)τf(0,M,N),
so
f(0, M, N) = −
1
τ(N −M) ln B(0, N)
B(0, M) = −ln B(0, N) −ln B(0, M)
τ(N −M)
.
Note that this rate is deterministic, since it is worked out using the present bond
prices. It can be conveniently expressed in terms of the initial term structure.
Insert into the above expression the bond prices as determined by the yields,
B(0, N) = e−τNy(0,N) and B(0, M) = e−τMy(0,M), to get
f(0, M, N) = Ny(0, N) −My(0, M)
N −M
.
(10.5)
Exercise 10.18
Suppose that the following spot rates are provided by central London
banks (LIBOR, the London Interbank Offer Rate, is the rate at which
money can be deposited; LIBID, the London Interbank Bid Rate, is the
rate at which money can be borrowed):
Rate
LIBOR
LIBID
1 month
8.41%
8.59%
2 months
8.44%
8.64%
3 months
9.01%
9.23%
6 months
9.35%
9.54%
As a bank manager acting for a customer who wishes to arrange a loan of
$100, 000 in a month’s time for a period of 5 months, what rate could you
offer and how would you construct the loan? Suppose that another insti-
tution offers the possibility of making a deposit for 4 months, starting 2

10. Variable Interest Rates
233
months from now, at a rate of 10.23%. Does this present an arbitrage op-
portunity? All rates stated in this exercise are continuous compounding
rates.
As time passes, the bond prices will change and, consequently, so will the
forward rates. The forward rate over the interval [M, N] determined at time
n < M < N is defined by
B(n, N) = B(n, M)e−(N−M)τf(n,M,N),
that is,
f(n, M, N) = −ln B(n, N) −ln B(n, M)
(N −M)τ
.
The instantaneous forward rates f(n, N) = f(n, N, N + 1) are the forward
rates over a one-step interval. Typically, when τ is one day, the instantaneous
forward rates correspond to overnight deposits or loans. The formula for the
forward rate
f(n, N) = −ln B(n, N + 1) −ln B(n, N)
τ
(10.6)
will enable us to reconstruct the bond prices, given the forward rates at a
particular time n.
Example 10.11
Let τ =
1
12, n = 0, N = 0, 1, 2, 3, and suppose that the bond prices are
B(0, 1) = 0.9901,
B(0, 2) = 0.9828,
B(0, 3) = 0.9726.
Then we have the following implied yields
y(0, 1) ∼= 11.94%,
y(0, 2) ∼= 10.41%,
y(0, 3) ∼= 11.11%,
and forward rates
f(0, 0) ∼= 11.94%,
f(0, 1) ∼= 8.88%,
f(0, 2) ∼= 12.52%.
Observe that, using the formula for the forward rates, we get
exp(−(0.1194 + 0.0888 + 0.1252)/12) ∼= 0.9726 = B(0, 3)
which illustrates the next proposition.

234
Mathematics for Finance
Proposition 10.3
The bond price is given by
B(n, N) = exp{−τ(f(n, n) + f(n, n + 1) + · · · + f(n, N −1))}.
Proof
For this purpose note that
f(n, n) = −ln B(n, n + 1)
τ
,
since B(n, n) = 1, so
B(n, n + 1) = exp{−τf(n, n)}.
Next,
f(n, n + 1) = −ln B(n, n + 2) −ln B(n, n + 1)
τ
and, after inserting the expression for B(n, n + 1),
B(n, n + 2) = exp{−τ(f(n, n) + f(n, n + 1))}.
Repeating this a number of times, we arrive at the required general formula.
We have a simple representation of the forward rates in terms of the yields:
f(n, N) = (N + 1 −n)y(n, N + 1) −(N −n)y(n, N).
(10.7)
In particular,
f(n, n) = y(n, n + 1),
resulting in the intuitive formula
y(n, N) = f(n, n) + f(n, n + 1) + · · · + f(n, N −1)
N −n
.
Example 10.12
We can clearly see from the above formulae that if the term structure is flat,
that is, y(n, N) is independent of N, then f(n, N) = y(n, N). Now consider an
example of f(n, N) increasing with N for a fixed n, and compute the corre-
sponding yields
f(0, 0) = 8.01%,
f(0, 1) = 8.03%,
f(0, 2) = 8.08%,
y(0, 1) = 8.01%,
y(0, 2) = 8.02%,
y(0, 3) = 8.04%.

10. Variable Interest Rates
235
We can see that the yields also increase. (See Exercise 10.20 below for a gener-
alisation of this.)
However, the forward rates do not have to increase with maturity even if
the yields do:
f(0, 0) = 9.20%,
f(0, 1) = 9.80%,
f(0, 2) = 9.56%,
y(0, 1) = 9.20%,
y(0, 2) = 9.50%,
y(0, 3) ∼= 9.52%.
Exercise 10.19
Can a forward rate be negative?
Exercise 10.20
Prove that if f(n, N) increases with N, then the same is true for y(n, N).
10.2.2 Money Market Account
The short rate is defined by r(n) = f(n, n). An alternative expression is r(n) =
y(n, n + 1), so this is a rate valid for one step starting at time n. The short
rates are unknown in advance, except for the current one, r(0). It is important
to distinguish between r(n) and f(0, n). Both rates apply to a single step from
time n to n + 1, but the former is random, whereas the latter is known at the
present moment and determined by the initial term structure.
The money market account denoted by A(n), n ≥1, is defined by
A(n) = exp{τ(r(0) + r(1) + · · · + r(n −1))}
with A(0) = 1, and represents the value at time n of one dollar invested in
an account attracting interest given by the short rate under continuous com-
pounding. For example, if τ =
1
365, then the interest is given by the overnight
rate.
The money market account defined in Chapter 2 was a deterministic
sequence independent of the particular way the initial dollar is invested.
Here A(n) is random and, as will be seen below, in general different from
exp{τny(0, n)}, the latter being deterministic and constructed by using zero-
coupon bonds maturing at time n.
Example 10.13
In the setting introduced in Example 10.11, suppose that the bond prices change

236
Mathematics for Finance
as follows:
B(0, 1) = 0.9901,
B(0, 2) = 0.9828,
B(0, 3) = 0.9726,
B(1, 2) = 0.9947,
B(1, 3) = 0.9848,
B(2, 3) = 0.9905.
The corresponding yields are
y(0, 1) ∼= 11.94%,
y(0, 2) ∼= 10.41%,
y(0, 3) ∼= 11.11%,
y(1, 2) ∼= 6.38%,
y(1, 3) ∼= 9.19%,
y(2, 3) ∼= 11.45%.
The forward rates are
f(0, 0) ∼= 11.94%,
f(0, 1) ∼= 8.88%,
f(0, 2) ∼= 12.52%,
f(1, 1) ∼= 6.38%,
f(1, 2) ∼= 12.00%,
f(2, 2) ∼= 11.45%.
We can read offthe short rates and compute the values of the money market
account
r(0) = f(0, 0) ∼= 11.94%,
r(1) = f(1, 1) ∼= 6.38%,
r(2) = f(2, 2) ∼= 11.45%,
A(0) = 1,
A(1) ∼= 1.0100,
A(2) ∼= 1.0154,
A(3) ∼= 1.0251.
Exercise 10.21
Which bond prices in Example 10.13 can be altered so that the values
of the money market remain unchanged?
Exercise 10.22
Using the data in Example 10.13, compare the logarithmic return on
an investment in the following securities over the period from 0 to 3:
a) zero-coupon bonds maturing at time 3; b) single-period zero-coupon
bonds; c) the money market account.

11
Stochastic Interest Rates
This chapter is devoted to modelling the time evolution of random interest
rates. We adopt an approach similar to the binomial model of stock prices in
Chapter 3. Modelling the evolution of interest rates can be reduced to modelling
the evolution of the bond prices, since the latter determine the former. We begin
with some properties that a model of bond prices should satisfy, emphasising
the differences between bonds and stock.
First, let us recall that the evolution of interest rates or bond prices is
described by functions of two variables, the running time and the maturity
time, whereas stock prices are functions of just one variable, the running time.
Second, there are many ways of describing the term structure: bond prices,
implied yields, forward rates, short rates. Bond prices and yields are clearly
equivalent, being linked by a simple formula. Bond prices and forward rates are
also equivalent. The short rates are different, easier to handle, but the problem
of reconstructing the term structure emerges. This may be non-trivial, since
short rates usually carry less information.
Third, the model needs to match the initial data. For a stock this is just
the current price. In the case of bonds the whole initial term structure is given,
imposing more restrictions on the model, which has to be consistent with all
currently available market information.
Fourth, bonds become non-random at maturity. This is in sharp contrast
with stock prices. The fact that a bond gives a sure dollar at maturity has to
be included in the model.
Finally, the dependence of yields on maturity must be quite special. Bonds
with similar maturities will typically behave in a similar manner. In statistical
237

238
Mathematics for Finance
terms this means that they are strongly positively correlated.
11.1 Binomial Tree Model
The shape of the tree will be similar to that in Section 3.2. However, to facilitate
the necessary level of sophistication of the model, it has to be more complex.
Namely, the probabilities and returns will depend on the position in the tree.
We need suitable notation to distinguish between different positions.
By a state we mean a finite sequence of consecutive up or down movements.
The state depends, first of all, on time or, in other words, on the number of
steps. We shall use sequences of letters u and d of various lengths, the length
corresponding to the time elapsed (the number of steps from the root of the
tree). At time 1 we have just two states s1 = u or d, at time 2 four states
s2 = ud, dd, du, or uu. We shall write s2 = s1u or s1d, meaning that we go
up or, respectively, down at time 2, having been at s1 at time 1. In general,
sn+1 = snu or snd.
The probabilities will be allowed to depend on particular states. We write
p(sn) to denote the probability of going up at time n + 1, having started at
state sn at time n. At the first step the probability of going up will be denoted
by p without an argument. In Figure 11.1 we have p = 0.3, p(u) = 0.1, p(d) =
0.4, p(uu) = 0.4, p(ud) = 0.2, p(du) = 0.5, p(dd) = 0.4.
Figure 11.1
States and probabilities
Let us fix a natural number N as the time horizon. It will be the upper
bound of the maturities of all the bonds considered. The states sN at time N
represent the complete scenarios of bond price movements.

11. Stochastic Interest Rates
239
Next, we shall describe the evolution of bond prices. At time 0 we are given
the initial bond prices for all maturities up to N, that is, a sequence of N
numbers
B(0, 1), B(0, 2), B(0, 3), . . . , B(0, N −1), B(0, N).
At time 1 one of the prices becomes redundant, namely the first bond matures
and only the remaining N −1 bonds are still being traded. We introduce ran-
domness by allowing two possibilities distinguished by the states u and d, so
we have two sequences
B(1, 2; u), B(1, 3, u), . . . , B(1, N −1; u), B(1, N; u),
B(1, 2; d), B(1, 3; d), . . . , B(1, N −1; d), B(1, N; d).
At time 2 we have four states and four sequences of length N −2:
B(2, 3, uu), . . . , B(2, N −1; uu), B(2, N; uu),
B(2, 3; ud), . . . , B(2, N −1; ud), B(2, N; ud),
B(2, 3; du), . . . , B(2, N −1; du), B(2, N; du),
B(2, 3; dd), . . . , B(2, N −1; dd), B(2, N; dd).
We do not require that the ud and du prices coincide, which was the case for
stock prices movements in Section 3.2.
This process continues in the same manner. At each step the length of the
sequence decreases by one and the number of sequences doubles. At time N −1
we have just single numbers, 2N−1 of them,
B(N −1, N; sN−1)
indexed by all possible states sN−1. The tree structure breaks down here be-
cause the last movement is certain: The last bond matures, becoming a sure
dollar at time N, B(N, N; sN) = 1 for all states.
Example 11.1
A particular evolution of bond prices for N = 3, with monthly steps (τ =
1
12)
is given in Figure 11.2. The prices of three bonds with maturities 1, 2, and 3
are shown.
The evolution of bond prices can be described be means of returns. Suppose
we have reached state sn−1 and the bond price B(n −1, N; sn−1) becomes
known. Then we can write
B(n, N; sn−1u) = B(n −1, N; sn−1) exp{k(n, N; sn−1u)},
B(n, N; sn−1d) = B(n −1, N; sn−1) exp{k(n, N; sn−1d)},

240
Mathematics for Finance
Figure 11.2
Evolution of bond prices in Example 11.1
implicitly defining the logarithmic returns
k(n, N; sn−1u) = ln
B(n, N; sn−1u)
B(n −1, N; sn−1),
k(n, N; sn−1d) = ln
B(n, N; sn−1d)
B(n −1, N; sn−1).
We assume here that k(n, N; sn−1u) ≥k(n, N; sn−1d).
Remark 11.1
Note that there are some places in the tree where the returns are non-random
given the state sn−1 is known. Namely,
k(n, n; sn−1u) = k(n, n; sn−1d) = ln
1
B(n −1, n; sn−1),
since B(n, n; sn) = 1 for all sn.
Example 11.2
From the data in Example 11.1 we extract the prices of bonds with maturity 3,
completing the picture with the final value 1. The tree shown in Figure 11.3
Figure 11.3
Prices of the bond maturing at time 3 in Example 11.2

11. Stochastic Interest Rates
241
describes the random evolution of a single bond purchased at time 0 for 0.9726.
The returns are easy to compute, for instance
k(2, 3; ud) = ln B(2, 3; ud)
B(1, 3; u)
∼= 0.27%.
The results are gathered in Figure 11.4. (Recall that the length of each step is
one month.)
Figure 11.4
Returns on the bond maturing at time 3 in Example 11.2
Exercise 11.1
For the tree of weekly returns shown in Figure 11.5 construct the tree of
bond prices and fill in the missing returns.
Figure 11.5
Returns in Exercise 11.1
The evolution of bond prices is in perfect correspondence with the evolution
of implied yields to maturity. Namely,
y(n, m; sn) =
1
τ(m −n) ln
1
B(n, m; sn)
with the same tree structure as for bond prices. In particular, the final yields are
non-random given that the state sn−1 at the penultimate step is known. Note

242
Mathematics for Finance
that the words ‘up’ and ‘down’ lose their meaning here because the yield goes
down as the bond price goes up. Nevertheless, we keep the original indicators
u and d.
Example 11.3
We continue Example 11.1 and find the yields, bearing in mind that τ =
1
12.
The results are collected in Figure 11.6.
Figure 11.6
Yields in Example 11.3
Exercise 11.2
Take the returns in Exercise 11.1 and find the yield y(0, 3). What is the
general relationship between the returns and yields to maturity? Can
you complete the missing returns without computing the bond prices?
Now consider the instantaneous forward rates. At the initial time 0 there
are N forward rates
f(0, 0), f(0, 1), f(0, 2), . . . , f(0, N −1)
generated by the initial bond prices. Note that the first number is the short
rate r(0) = f(0, 0). For all subsequent steps the current bond prices imply the
forward rates. Formula (10.6) applied to random bond prices allows us to find
the random evolution of forward rates:
f(n, N; sn) = −ln B(n, N + 1; sn) −ln B(n, N; sn)
τ
.
(11.1)
At time 1 we have two possible sequences of N −1 forward rates obtained from
two sequences of bond prices
f(1, 1; u), f(1, 2; u), . . . , f(1, N −1; u),
f(1, 1; d), f(1, 2; d), . . . , f(1, N −1; d).

11. Stochastic Interest Rates
243
At time 2 we have four sequences of N−2 forward rates, and so on. At time N−1
we have 2N−1 single numbers f(N −1, N −1; sN−1).
Example 11.4
Using (11.1), we can evaluate the forward rates for the data in Example 11.1.
For instance,
f(1, 2; u) = −ln B(1, 3; u) −ln B(1, 2; u)
τ
.
Alternatively, we can use the yields found in Example 11.3 along with for-
mula (10.7):
f(1, 2; u) = 2y(1, 3; u) −y(1, 2; u).
The results are gathered in Figure 11.7.
Figure 11.7
Forward rates in Example 11.4
The information contained in forward rates is sufficient to reconstruct the
bond prices, as was shown in Proposition 10.3.
Exercise 11.3
Suppose a tree of forward rates is given as in Figure 11.8. Find the
corresponding bond prices (using one-month steps).
The short rates are just special cases of forward rates,
r(n; sn) = f(n, n; sn)
for n ≥1, with deterministic r(0) = f(0, 0). The short rates are also given by
r(n; sn) = y(n, n + 1; sn), n ≥1, and r(0) = y(0, 1), that is, by the rates of
return on a bond maturing at the next step. This is obvious from the relations
between the forward rates and yields.

244
Mathematics for Finance
Figure 11.8
Forward rates in Exercise 11.3
We are now ready to describe the money market account. It starts with
A(0) = 1. The next value
A(1) = exp(τr(0))
is still deterministic. It becomes random at subsequent steps. At time 2 there
are two values depending on the states at time 1:
A(2; u) = exp(τ(r(0) + r(1; u)) = A(1) exp{τr(1; u)},
A(2; d) = exp(τ(r(0) + r(1; d)) = A(1) exp{τr(1; d)}.
Next, for example,
A(3; ud) = exp(τ(r(0) + r(1; u) + r(2; ud)) = A(2; u) exp{τr(2; ud)}.
In general,
A(n + 1; sn−1u) = A(n; sn−1) exp{τr(n; sn−1u)},
A(n + 1; sn−1d) = A(n; sn−1) exp{τr(n; sn−1d)}.
Exercise 11.4
Find the evolution of the money market account if the forward rates are
the same as in Exercise 11.3.
For bond investments the money market account plays the same role as
the risk-free component of investment strategies on the stock market in ear-
lier chapters. It is used to discount future cash flows when valuing bonds and
derivative securities, as will be shown below.

11. Stochastic Interest Rates
245
11.2 Arbitrage Pricing of Bonds
Suppose that we are given the binomial tree of bond prices B(n, N; sn) for
a bond maturing at the fixed time horizon N. In addition, we are given the
money market process A(n; sn−1). As was mentioned in the introduction to
this chapter, the prices of other bonds cannot be completely arbitrary. We
shall show that the prices B(n, M; sn) for M < N can be replicated by means
of bonds with maturity N and the money market. As a consequence of the
No-Arbitrage Principle, the prices of B(n, M; sn) will have to be equal to the
values of the corresponding replicating strategies.
Example 11.5
Consider the data in Example 11.1. At the first step the short rate is deter-
ministic, being implied by the price B(0, 1). The first two values of the money
market account are A(0) = 1 and A(1) = 1.01. As the underlying instrument
we take the bond maturing at time 3. The prices of this bond at time 0 and 1
are given in Figure 11.9, along with the prices of the bond maturing at time 2.
We can find a portfolio (x, y), with x being the number of bonds of maturity 3
Figure 11.9
Bond prices from Example 11.1
and y the position in the money market, such that the value of this portfolio
matches the time 1 prices of the bond maturing at time 2. To this end we solve
the following system of equations
0.9848x + 1.01y = 0.9948,
0.9808x + 1.01y = 0.9907,
obtaining x = 1 and y ∼= 0.0098. The value of this portfolio at time 0 is
1 × B(0, 3) + 0.0098 × A(0) ∼= 0.9824, which is not equal to B(0, 2). The prices
in Figure 11.9 provide an arbitrage opportunity:
• Sell a bond maturing at time 2 for $0.9828 and buy the portfolio constructed
above for $0.9824.
• Whatever happens at time 1, the value of the portfolio will be sufficient to
buy the bond back, the initial balance $0.0004 being the arbitrage profit.

246
Mathematics for Finance
The model in Example 11.1 turns out to be inconsistent with the No-Arbitrage
Principle and has to be rectified. We can only adjust some of the future prices,
since the present prices of all bonds are dictated by the market. It is easy to
see that by taking B(1, 2; u) = 0.9958 with B(1, 2; d) unchanged, or by letting
B(1, 2; d) = 0.9913 with B(1, 2; u) unchanged, we can eliminate the arbitrage
opportunity. Of course, there are many other ways of repairing the model by a
simultaneous change of both values of B(1, 2). Let us put B(1, 2; d) = 0.9913
and leave B(1, 2; u) unchanged. The rectified tree of bond prices is shown in
Figure 11.10 and the corresponding yields in Figure 11.11.
Figure 11.10
Rectified tree of bond prices in Example 11.5
Figure 11.11
Rectified tree of yields in Example 11.5
Remark 11.2
The process of rectifying bond prices in Example 11.5 bears some resemblance
to the pricing of general derivative securities described in Chapter 8. The role
of the derivative security is played by the bond maturing at time 2. The bond
maturing at time 3 plays the role of the underlying security. The difference
is that the present price of the bond of maturity 2 is fixed and we can only
adjust the future prices in the model to eliminate arbitrage. At this stage we
are concerned only with building consistent models rather than with pricing
securities.

11. Stochastic Interest Rates
247
Exercise 11.5
Evaluate the prices of a bond maturing at time 2 given a tree of prices
of a bond maturing at time 3 and short rates as shown in Figure 11.12,
with τ = 1/12.
Figure 11.12
Bond prices and short rates in Exercise 11.5
We can readily generalize Example 11.5. The underlying bond matures at
time N and we can find the structure of prices of any bond maturing at M < N.
The replication proceeds backwards step-by-step starting from time M, for
which B(M, M; sM) = 1 in each state sM. The first step is easy: for each
state sM−1 we take a portfolio with x = 0 and y = 1/A(M; sM−1), since the
bond becomes risk free one step prior to maturity.
Next, consider time M −2. For any state sM−2 we find x = x(M −1; sM−2),
the number of bonds maturing at N, and y = y(M −1; sM−2), the position in
the money market, by solving the system
xB(M −1, N; sM−2u) + yA(M −1; sM−2) = B(M −1, M; sM−2u),
xB(M −1, N; sM−2d) + yA(M −1; sM−2) = B(M −1, M; sM−2d).
In this way we can find the prices at time M −2 of the bond maturing at
time M,
B(M −2, M; sM−3u) = xB(M −2, N; sM−3u) + yA(M −2; sM−3),
B(M −2, M; sM−3d) = xB(M −2, N; sM−3d) + yA(M −2; sM−3).
We can iterate the replication process moving backwards through the tree.
Remark 11.3
Replication is possible if a no-arbitrage condition analogous to Condition 3.2
is satisfied for the binomial tree. Here the condition u > r > d of Chapter 3 is

248
Mathematics for Finance
replaced by
k(n, N; sn−1u) > τr(n −1; sn−1) > k(n, N; sn−1d).
(11.2)
Any future cash flow can be replicated in a similar fashion. Consider, for
example, a coupon bond with fixed coupons.
Example 11.6
Take a coupon bond maturing at time 2 with face value F = 100, paying
coupons C = 10 at times 1 and 2. We price the future cash flow by using the
zero-coupon bond maturing at time 3 as the underlying security. The coupon
bond price P at a particular time will not include the coupon due (the so-
called ex-coupon price). Assume that the structure of the bond prices is as in
Figure 11.10.
Consider time 1. In state u the short rate is determined by the price
B(1, 2; u) = 0.9947, so we have r(1; u) ∼= 6.38%. Hence P(1; u) ∼= 109.4170.
In state d we use B(1, 2; d) = 0.9913 to find r(1; d) ∼= 10.49% and P(1; d) ∼=
109.0485.
Consider time 0. The cash flow at time 1 which we are to replicate includes
the coupon due, so it is given by P(1; u) + 10 ∼= 119.417 and P(1; d) + 10 ∼=
119.0485. The short rate r(0) ∼= 11.94% determines the money market account
as in Example 11.5, A(1) = 1.01, and we find x ∼= 92.1337, y ∼= 28.3998. Hence
P(0) ∼= 118.009 is the present price of the coupon bond.
An alternative is to use the spot yields: y(0, 1) ∼= 11.94% and y(0, 2) ∼=
10.41% to discount the future payments with the same result: 118.009 ∼= 10 ×
exp(−1
12 × 11.94%) + 110 × exp(−2
12 × 10.41%).
In general,
P(0) = C1 exp{−τy(0, 1)} + C2 exp{−2τy(0, 2)}
+ · · · + (CN + F) exp{−Nτy(0, N)}.
(11.3)
(For simplicity we include all time steps, so Ck = 0 at the time steps k when
no coupon is paid.) At each time k when a coupon is paid, the cash flow is the
sum of the (deterministic) coupon and the (stochastic) price of the remaining
bond:
Ck + P(k; sk) = Ck + Ck+1 exp{−τy(k, k + 1; sk)}
+ · · · + (Cn + F) exp{−τ(n −k)y(k, n; sk)}.
Quite often the coupons depend on other quantities. In this way a coupon
bond may become a derivative security. An important benchmark case is de-
scribed below, where the coupons are computed as fractions of the face value.

11. Stochastic Interest Rates
249
These fractions, defining the coupon rate, are obtained by converting the short
rate to an equivalent discrete compounding rate. In practice, when τ is one day,
the coupon rate will be the overnight LIBOR rate.
Proposition 11.1
A coupon bond maturing at time N with random coupons
Ck(sk−1) = (exp{τr(k −1; sk−1)} −1)F
(11.4)
for 0 < k ≤N is trading at par. (That is, the price P(0) is equal to the face
value F.)
Proof
Fix time N −1 and a state sN−1. In this state the value P(N −1; sN−1)
of the bond is F + CN(sN−1) discounted at the short rate, which gives
P(N −1; sN−1) = F if the coupon is expressed by (11.4). Proceeding back-
wards through the tree and applying the same argument for each state, we
finally arrive at P(0) = F.
Exercise 11.6
Find the coupons of a bond trading at par and maturing at time 2, given
the yields as in Example 11.5, see Figure 11.11.
11.2.1 Risk-Neutral Probabilities
In Chapter 3 we have learnt that the stock price S(n) at time n is equal to the
expectation under the risk-neutral probability of the stock price S(n + 1) at
time n+1 discounted to time n. The situation is similar in the binomial model
of interest rates.
The discount factors are determined by the money market account, or, in
other words, by the short rates. In general, they are random, being of the form
exp{−τr(n; sn)}.
Suppose that state sn has occurred at time n. The short rate determining
the time value of money for the next step is now known with certainty. Consider
a bond maturing at time N with n < N −1. We are given the bond price
B(n, N; sn) and two possible values at the next step, B(n+1, N; snu) and B(n+
1, N; snd). These values represent a random variable, which will be denoted by
B(n + 1, N; sn·). If n = N −1, then the bond matures at the next step N,

250
Mathematics for Finance
when it has just one price independent of the state, namely the face value. We
are looking for a probability p∗such that
B(n, N; sn) = [p∗B(n + 1, N; snu) + (1 −p∗)B(n + 1, N; snd)]
× exp{−τr(n; sn)}.
(11.5)
This equation can be solved for p∗, which in principle depends on n, N and sn.
(As will turn out soon, see Proposition 11.2, p∗is in fact independent of ma-
turity N.) Recalling the definition of logarithmic returns, we have
B(n + 1, N; sn+1) = B(n, N; sn) exp{k(n + 1, N; sn+1)},
which gives
p∗(n, N; sn) =
exp{τr(n; sn)} −exp{k(n + 1, N; snd)}
exp{k(n + 1, N; snu)} −exp{k(n + 1, N; snd)}.
(11.6)
These numbers are called the risk-neutral or martingale probabilities. Condi-
tion (11.2) for the lack of arbitrage can now be written as
0 < p∗(n, N; sn) < 1.
Example 11.7
We shall find the tree of risk-neutral probabilities p∗(n, 3; sn) for n = 0, 1, using
the data in Example 11.5 (the bond prices as shown in Figure 11.10).
First we compute the returns on the money market. The simplest way is
to use the yields (Figure 11.11). With τ =
1
12 we have τr(n; sn) = y(n, n +
1; sn)/12, n = 0, 1, which gives the following values:
τr(1; u) = 0.521%
τr(0) = 0.995%
<
τr(1; d) = 0.874%
Next, we find the returns k(1, 3; s1) and k(2, 3; s2) on bonds. For example, if
s2 = ud, then k(2, 3; ud) = ln( 0.9875
0.9848). The results are collected below:
k(2, 3; uu) = 0.58%
k(1, 3; u) = 1.25%
<
/
k(2, 3; ud) = 0.27%
\
k(2, 3; du) = 1.01%
k(1, 3; d) = 0.84%
<
k(2, 3; dd) = 0.84%

11. Stochastic Interest Rates
251
We can see that the no-arbitrage conditions are satisfied: 0.84% < 0.99% <
1.25%, 0.27% < 0.52% < 0.58% and 0.84% < 0.87% < 1.01%.
Finally, we find the desired probabilities by a direct application of (11.6):
p∗(0) = 0.3813, p∗(1; u) = 0.8159, p∗(1; d) = 0.1811, see Figure 11.13.
Figure 11.13
Risk-neutral probabilities in Example 11.7
A crucial observation about the model is this: Pricing via replication is
equivalent to pricing by means of the risk-neutral probability. This follows from
the No-Arbitrage Principle and applies to any cash flow, even a random one,
where the amounts depend on the states. This opens a way to pricing absolutely
any security by means of the expectation with respect to the probabilities
p∗(n, N; sn). The expectation is computed step-by-step, starting at the last
one and proceeding backwards through the tree.
Example 11.8
Consider a coupon bond maturing at N = 2 with face value F = 100 and
with coupons equal to 5% of the current value of the bond, paid at times 1
and 2. In particular, the coupon at maturity is C2 = 5 in each state. Using the
risk-neutral probabilities from Example 11.7, we can find the bond values at
time 1. In the up state we have the discounted value of 105 due at maturity
using the short rate r(1; u) ∼= 6.26%, which gives 104.4540. In the same way in
the down state we obtain 104.0865. Now we add 5% coupons, so the amounts
due at time 1 become 109.6767 in the up state and 109.2908 in the down state.
Using the risk-neutral probabilities, we find the present value of the bond:
108.3545 ∼= (0.3813 × 109.6767 + 0.6187 × 109.2908)/1.01.
Exercise 11.7
Use the risk-neutral probabilities in Example 11.7 to find the present

252
Mathematics for Finance
value of the following random cash flow: At time 2 we receive $20 in the
state uu, $10 in the states ud and du, and nothing in the state dd. No
payments are due at other times.
Exercise 11.8
Find an arbitrage opportunity for the bond prices in Figure 11.14.
Figure 11.14
Bond prices in Exercise 11.8
Exercise 11.9
Suppose that the risk-neutral probabilities are equal to 1
2 in every state.
Given the following short rates, find the prices of a bond maturing at
time 3 (with a one-month time step, τ =
1
12):
r(2; uu) = 8.3%
r(1; u) = 8.5%
<
/
r(2; ud) = 8.9%
r(0) = 9.5%
\
r(2; du) = 9.1%
r(1; d) = 9.8%
<
r(2; dd) = 9.3%
The next proposition gives an important result, which simplifies the model
significantly.
Proposition 11.2
The lack of arbitrage implies that the risk-neutral probabilities are independent
of maturity.

11. Stochastic Interest Rates
253
Proof
Consider two bonds with maturities M ≤N and fix an n ≤M. For each of the
two bonds we have
B(n, M; sn) = [p∗(n, M; sn)B(n + 1, M; snu) + (1 −p∗(n, M; sn))
×B(n + 1, M; snd)] exp{−τr(n; sn)},
(11.7)
B(n, N; sn) = [p∗(n, N; sn)B(n + 1, N; snu) + (1 −p∗(n, N; sn))
×B(n + 1, N; snd)] exp{−τr(n; sn)}.
(11.8)
Our goal is to show that p∗(n, M; sn) = p∗(n, N; sn) in any state sn.
We can replicate the prices of the bond maturing at time M by means of the
bond with maturity N and the money market account. Hence we find numbers
x, y such that
B(n + 1, M; snu) = xB(n + 1, N; snu) + yA(n + 1; sn),
B(n + 1, M; snd) = xB(n + 1, N; snd) + yA(n + 1; sn).
The No-Arbitrage Principle implies that equalities of this kind must also hold
at time n,
B(n, M; sn−1u) = xB(n, N; sn−1u) + yA(n; sn−1),
B(n, M; sn−1d) = xB(n, N; sn−1d) + yA(n; sn−1).
Inserting the values of the M-bonds into (11.7) and using the formula for the
money market account, after some algebraic transformations we obtain
B(n, N; sn) = [p∗(n, M; sn)B(n + 1, N; snu) + (1 −p∗(n, M; sn))
×B(n + 1, N; snd)] exp{−τr(n; sn)}.
This can be solved for p∗(n, M; sn). It turns out that the solution coincides
with the probability p∗(n, N; sn) implied by (11.8), as claimed.
Exercise 11.10
Spot an arbitrage opportunity if the bond prices are as in Figure 11.15.
11.3 Interest Rate Derivative Securities
The tools introduced above make it possible to price any derivative security
based on interest rates or, equivalently, on bond prices. Within the binomial tree

254
Mathematics for Finance
Figure 11.15
Data for Exercise 11.10
model the cash flow associated with the derivative security can be replicated
using the money market account and a bond with sufficiently long maturity.
The bond does not even have to be the underlying security, since the prices
of various bonds must be consistent. An alternative is to use the risk-neutral
probabilities. The latter approach is often preferable to replication because of
its simplicity. The equivalence of both methods should be clear in view of what
has been said before.
The pricing of complex securities can essentially be reduced to finding the
associated cash flows. Below we present examples of some classical interest rate
contingent claims. We begin with the simplest case of options.
11.3.1 Options
The underlying securities for interest rate options are bonds of various kinds.
Example 11.9
With the bond prices as in Example 11.5 (Figure 11.10), consider a call option
with exercise time 2 and strike price X = 0.99 on a zero-coupon bond maturing
at time 3. Starting with the final payoffs shown in the last column in the table
below, we move back step-by-step, computing the risk-neutral expectations of

11. Stochastic Interest Rates
255
the consecutive values discounted by the appropriate short rates:
n = 0
n = 1
n = 2
0.0005
0.00041
<
/
0
0.00024
\
0.0008
0.00014
<
0
As a result, the price of the option is 0.00024.
Exercise 11.11
Assume the structure of bond prices in Example 11.5 (Figure 11.10).
Consider a coupon bond maturing at time 2 with face value F = 100
and coupons C = 1 payable at each step. Find the price of an American
call option expiring at time 2 with strike price X = 101.30. (Include the
coupon in the bond price at each step.)
Call options on bonds can be used by institutions issuing bonds to include
the possibility of buying the bond back prior to maturity for a prescribed price.
A bond that carries such a provision is called a callable bond. Its price should
be reduced by the price of the attached option.
11.3.2 Swaps
Writing and selling a bond is a method of borrowing money. In the case of a
coupon bond trading at par the principal represents the sum borrowed and the
coupons represent the interest. This interest may be fixed or floating (variable).
The interest is fixed if all coupons are the same. Floating interest can be realised
in many ways. Here we assume that it is determined by the short rates as
in (11.4). The basis for our discussion is laid by Proposition 11.1, according to
which the market value of such a floating-coupon bond must be equal to its face
value, the bond trading at par. For a fixed-coupon bond trading at par the size
of the coupons can easily be found from (11.3). We could say that the resulting
fixed coupon rate is equivalent to the variable short rate over the lifetime of
the bond.

256
Mathematics for Finance
Example 11.10
Consider a fixed-coupon bond and a floating-coupon bond, both with annual
coupons, trading at par and maturing after two years with face value F = 100.
Given that the tree of one- and two-year zero-coupon bond prices is
B(1, 2; u) = 0.9101
B(0, 1) = 0.9123
B(0, 2) = 0.8256
<
B(1, 2; d) = 0.8987
where a time step is taken to be one year, τ = 1, we can evaluate the coupons
of the fixed- and floating-coupon bonds. The size of the floating coupons can
be found from (11.4),
C1 = (B(0, 1)−1 −1)F ∼= 9.6131,
C2(u) = (B(1, 2; u)−1 −1)F ∼= 9.8780,
C2(d) = (B(1, 2; d)−1 −1)F ∼= 11.2718.
The fixed coupons C can be found by solving equation (11.3), which takes the
form
F = CB(0, 1) + (C + F)B(0, 2).
This gives
C ∼= 10.0351.
By buying a fixed-coupon bond and selling a floating-coupon one (or the other
way round, selling a fixed-coupon bond and buying a floating-coupon one) an
investor can create an random cash flow with present value zero, since the two
kinds of bond have the same initial price.
A company who has sold fixed-coupon bonds and is paying fixed interest
may sometimes wish to switch into paying the floating rate instead. This can
be realised by writing a floating-coupon bond and buying a fixed-coupon bond
with the same present value. In practice, a financial intermediary will provide
this service by offering a contract called a swap. Clearly, a swap of this kind
will cost nothing to enter. Here is an example of a practical situation, where
the role of the intermediary is to match the needs of two particular companies.
Example 11.11
Suppose that company A wishes to borrow at a variable rate, whereas B prefers
a fixed rate. Banks offer the following effective rates (that is, rates referring to

11. Stochastic Interest Rates
257
annual compounding):
A
B
fixed
11.40%
13.40%
variable
LIBOR + 2%
LIBOR + 3%
In this case we say that A has comparative advantage over B in the fixed rate,
with B having comparative advantage over A in the variable rate. (Notwith-
standing the fact that the overall credit rating of A is better, as reflected by
the lower interest rates offered.) In these circumstances A should borrow at
the fixed rate, B should borrow at the variable rate, and they can swap their
interest payments.
Consider a principal of $100, 000 borrowed for one year and suppose that
LIBOR is 10% and (just for simplicity) remains the same during the first year
of the loan. If A borrows at the variable rate and B at the fixed rate, then
the total interest paid will be $25, 400 between them. However, if A borrows
at the fixed rate and B at the variable rate, the interest payments will be only
$24, 400 in total. The difference of $1, 000 will be available to share between
the two companies if they arrange to swap the rates. (In practice, this amount
would be reduced by a fee charged by the intermediary arranging the deal.)
If LIBOR changes to 9%, say, in the second year of the loan, so will the total
interest payable, but the difference will remain at $1, 000.
How should this difference be shared between the two companies? To answer
the question, we assume the term structure of interest rates determined by the
prices of one- and two-year zero-coupon bonds in Example 11.10. In particular,
we can identify LIBOR with the effective short rate implied by the bond prices,
B(0, 1)−1 −1 in year one and B(1, 2)−1 −1 in year two. These are the same
rates as those implied by the floating coupons in Example 11.10. The fixed
coupons in the same example imply a rate of 10.04%.
Instead of swapping interest payments with B, company A would achieve
the same result by taking a loan of $100, 000 at the fixed rate of 11.40% offered
by the bank, buying 1, 000 of the fixed-coupon bonds, and writing 1, 000 of the
floating-coupon bonds considered in Example 11.10. As a result, company A
will have borrowed $100, 000 at the rate 11.40%−10.04%+LIBOR = LIBOR+
1.36%. Compared to the variable rate of LIBOR + 2% offered to company A,
this is a gain of 0.64%. On a $100, 000 loan this would mean a gain of $640 in
each year.
By a similar argument, instead of swapping with A, company B could bor-
row $100, 000 at the variable rate LIBOR + 3%, buy 1, 000 floating-coupon
bonds and write 1, 000 fixed-coupon bonds. As a result, B would pay interest
at LIBOR + 3% −LIBOR + 10.04% = 13.04%, a gain of 0.36% as compared to

258
Mathematics for Finance
the fixed rate of 13.40% it was offered. This means a gain of $360 in each year
on an $100, 000 loan.
The result is that the $1, 000 gain should be shared as $640 and $360 be-
tween companies A and B.
Finally, note that the value of the swap may vary with time and state,
departing from the initial value of zero. If a company wishes to enter into a
swap agreement at a later time, it may purchase a swaption, which is a call
option on the value of the swap (with prescribed strike price and expiry time).
11.3.3 Caps and Floors
A cap is a provision attached to a variable-rate bond which specifies the maxi-
mum coupon rate paid in each period over the lifetime of a loan. A caplet is a
similar provision applied to a particular single period. In other words, a caplet
is a European option on the level of interest paid or received. A cap can be
thought of as a series of caplets.
Example 11.12
We take a loan by selling a par floating-coupon bond maturing at time 3. (That
is, a bond which always has the par value, the coupons being implied by the
short rates as in (11.4).) We use the bond prices and rates in Example 11.5,
see Figures 11.10 and 11.11. The cash flow shown below includes the initial
amount received for selling the bond together with the coupons and face value
to be paid:
n = 0
n = 1
n = 2
−0.99990
—
−100.52272
100
<
−0.99990
—
−100.87764
Consider a caplet that applies at time 1 (one month) with strike interest rate of
8% (corresponding to 0.67% for a one-month period). The coupon determined
by the caplet rate is 0.66889 and we modify the cash flow accordingly. At time 0
we find the bond price by discounting its time 1 value, 100.66889 in each state,
that is 100 plus the coupon. This gives the following cash flow:
n = 0
n = 1
n = 2
−0.66889
—
−100.52272
99.67227
<
−0.66889
—
−100.87764

11. Stochastic Interest Rates
259
The price of the bond is reduced by the value of the caplet, that is, by 0.32773.
For a caplet at time 2 with the same strike rate the maximum size of the
coupon is 0.66889, as before. In the up state we pay the original interest,
exercising the caplet in the down state. The value of the bond at time 1 is
not 100, since the final coupons are no longer the same as for the par bond.
The time 1 prices are obtained by discounting the time 2 values. At time 0 we
find the bond price by evaluating the risk-neutral expectation of the discounted
values of the bond at time 1. The resulting cash flow is
n = 0
n = 1
n = 2
−0.99990
—
−100.52272
99.87323
<
−0.99990
—
−100.66889
This fixes the price of this caplet at 0.12677.
Finally, consider a cap for both times 1 and 2 with the same strike rate as
above. The cash flow can be obtained in a similar manner:
n = 0
n = 1
n = 2
−0.66889
—
−100.52272
99.54550
<
−0.66889
—
−100.66889
We can see that the value of the cap, 0.45450, is the sum of the values of the
caplets.
Analogously, a floor is a provision limiting the coupon from below. This
will be of value for a bond holder. It is composed from a series of floorlets, each
referring to a single period.
Exercise 11.12
In the framework of the above example, value a floor expiring at time 2
with strike rate 8%, based on the bond prices in Example 11.5.
11.4 Final Remarks
We conclude this chapter with some informal remarks on possible ways in which
models of the structure of bond prices can be built. This is a complex area and
all we can do here is to make some general comments.
As we have seen, the theory of interest rates is more complicated than the
theory of stock prices. In order to be able to price interest rate derivatives,

260
Mathematics for Finance
we need a model of possible movements of bond prices for each maturity. The
bond prices with different maturities have to be consistent with each other. As
we have seen above, the specification of
a) a model of possible short rates,
b) a model of possible values of a bond with the longest maturity (consistent
with the initial term structure)
determines the structure of possible prices of all bonds maturing earlier. An
alternative approach is to specify
a) a model of possible short rates,
b) the probabilities at each state,
and, taking these probabilities as risk-neutral ones, to compute the prices of all
bonds for all maturities. The latter method is conceptually simpler, especially
if we take the same probability in each state. The flexibility of short rate mod-
elling allows us to obtain sufficiently many models consistent with the initial
term structure.
If so, the simplest choice of probability 1/2 at each state of the binomial
tree appears to be as good as any, and we can focus on constructing short rate
models so that their parameters are consistent with historical data. A general
short-rate model in discrete time can be described as follows. Let tn = nτ.
Then the following relations specify a tree of the rate movements
r(tn+1) −r(tn) = µ(tn, r(tn))τ + σ(tn, r(tn))ξn
where ξn = ±1 with probability 1/2 each, and µ(t, r), σ(t, r) are suitably
chosen functions. In the continuous time limit (in the spirit of Section 3.3.2)
these relations lead to a stochastic differential equation of the form
dr(t) = µ(t, r(t))dt + σ(t, r(t))dw(t).
There are many ways in which the functions µ and σ can be specified, but none
of them is universally accepted. Here are just a few examples: µ(t, r) = b −ar,
σ(t, r) = σ (Vasiˇcek model), µ(t, r) = a(b −r), σ(t, r) = σ√r (Cox–Ingersoll–
Ross model), or µ(t, r) = θ(t)r, σ(t, r) = σr (Black–Derman–Toy model).
Given the short-rates, the next step is to compute the bond prices. These
will depend on the functions µ and σ. Two problems may be encountered:
1. The model is too crude, for example these functions are just constants. Then
we may not be able to adjust them so that the resulting bond prices agree
with the initial term structure.
2. The model is too complicated, for example we take absolutely general func-
tions µ, σ. Fitting the initial term structure imposes some constraints on
the parameters, but many are left free and the result is too general to be of
any practical use.

11. Stochastic Interest Rates
261
These problems can be avoided if some middle-of-the-road solution is adopted.
Yet another alternative is to specify the dynamics of the entire curve of for-
ward rates. This determines the time evolution of the term structure, with the
initial term structure playing the role of initial data. This sounds conceptually
simple, but the model (the Heath–Jarrow–Morton model in continuous time
setting) is mathematically complex.
The literature on the subject is vast and expanding. We recommend that
the reader interested in pursuing this topic should look, for example, at
Pliska (1997), and Jarrow (1995) for the discrete time setting, or Bj¨ork (1998)
and Chen (1996) for continuous time models.


## Stochastic Interest Rates

This page intentionally left blank 

Solutions
Chapter 1
1.1 The value of the portfolio at time 0 is
V (0) = xS(0) + yA(0) = 1, 600
dollars. The value of the portfolio at time 1 will be
V (1) = xS(1) + yA(1) =

1, 800
if stock goes up,
1, 700
if stock goes down.
Hence, the return on the portfolio will be
KV = V (1) −V (0)
V (0)
=

0.1250
if stock goes up,
0.0625
if stock goes down,
that is, either 12.5% or 6.25%.
1.2 Given the same bond and stock prices as in Exercise 1.1, the value of a portfolio
(x, y) at time 1 will be
V (1) =

x30 + y100
if stock goes up,
x20 + y100
if stock goes down.
Thus, we obtain a system of equations

x30 + y100 = 1, 160,
x20 + y100 = 1, 040.
The solution is x = 12 and y = 8. A portfolio with 12 shares of stock and
8 bonds will produce the desired value at time 1. The time 0 value of this
portfolio is
V (0) = 12 × 25 + 8 × 90 = 1, 020
dollars.
1.3 An arbitrage opportunity can be realised as follows:
263

264
Mathematics for Finance
• Use dealer A to change 1 dollar into
1
1.5844 ∼= 0.6312 pounds.
• Use dealer B to change 0.6312 pounds into 0.6312
0.6401 ∼= 0.9861 euros.
• Use dealer A to change 0.9861 euros into 0.9861 × 1.0202 ∼= 1.0060 dollars.
The arbitrage gain will be about 0.0060 dollars.
1.4 We want both xS(0) and yA(0) to be equal to a half of the initial wealth. This
gives x80 = 5, 000 and y100 = 5, 000, so x = 62.5 and y = 50. The value of
this portfolio at time 1 will be
V (1) = 62.5S(1) + 50A(1) =

11, 750
if stock goes up,
9, 250
if stock goes down,
and hence the return on this portfolio will be
KV =

0.175
if stock goes up,
−0.075
if stock goes down.
Now we can compute the expected return
E(KV ) = 0.175 × 0.8 −0.075 × 0.2 = 0.125,
which is 12.5%, and the risk
σV =

(0.175 −0.125)2 × 0.8 + (−0.075 −0.125)2 × 0.2 = 0.1,
that is, 10%.
1.5 The following strategy will realise an arbitrage opportunity. At time 0:
• Borrow $34.
• Buy a share of stock for $34.
• Enter into a short forward contract with forward price $38.60 and delivery
date 1.
At time 1:
• Sell the stock for $38.60, closing the short forward position.
• Pay 34 × 1.12 = 38.08 dollars to clear the loan with interest.
The balance of 38.60 −38.08 = 0.52 dollars will be your arbitrage profit.
1.6 Suppose that a sterling bond promising to pay £100 at time 1 is selling for x
pounds at time 0. To find x consider the following strategy. At time 0:
• Borrow 1.6x dollars and change the sum into x pounds.
• Purchase a sterling bond for x pounds.
• Take a short forward position to sell £100 for $1.50 to a pound with
delivery date 1.
Then, at time 1:
• Cash the bond, collecting £100.
• Close the short forward position by selling £100 for $150.
• Repay the cash loan with interest, that is, 1.68x dollars in total.
The balance of all these transactions is 150 −1.68x dollars, which must be
equal to zero or else an arbitrage opportunity would arise. It follows that a
sterling bond promising to pay £100 at time 1 must sell for x =
150
1.68 ∼= 89.29
pounds at time 0.

Solutions
265
1.7 a) The payoffof a call option with strike price $90 will be
C(1) =

30
if stock goes up,
0
if stock goes down.
The replicating investment into x shares and y bonds satisfies the system of
equations

x120 + y110 = 30,
x80 + y110 = 0.
The solution is x = 3
4 and y = −6
11. Hence the price of the option must be
C(0) = 3
4 × 100 −6
11 × 100 ∼= 20.45
dollars.
b) The payoffof a call option with strike price $110 will be
C(1) =

10
if stock goes up,
0
if stock goes down.
The replicating investment into x shares and y bonds satisfies

x120 + y110 = 10,
x80 + y110 = 0.
Solving this system of equations, we find that x = 1
4 and y = −2
11. Hence the
price of the option is
C(0) = 1
4 × 100 −2
11 × 100 ∼= 6.82
dollars.
1.8 a) The replicating investment into x shares and y bonds satisfies the system
of equations

x120 + y105 = 20,
x80 + y105 = 0,
which gives x = 1
2 and y = −8
21. Hence
C(0) = 1
2 × 100 −8
21 × 100 ∼= 11.91
dollars.
b) In this case the replicating investment into x shares and y bonds satisfies

x120 + y115 = 20,
x80 + y115 = 0,
so x = 1
2 and y = −8
23. It follows that
C(0) = 1
2 × 100 −8
23 × 100 ∼= 15.22
dollars.

266
Mathematics for Finance
1.9 We need to find an investment into x shares and y bonds replicating the put
option, that is, such that xS(1) + yA(1) = P(1), no matter whether the stock
price goes up or down. This leads to the system of equations

x120 + y110 = 0,
x80 + y110 = 20.
The solution is x = −1
2 and y =
6
11. To replicate the put option we need to
take a short position of 1
2 a share in stock and to buy
6
11 of a bond. The value
of this investment at time 0 is
xS(0) + yA(0) = −1
2 × 100 + 6
11 × 100 ∼= 4.55
dollars. By a similar argument as in Proposition 1.3, it follows that xS(0) +
yA(0) = P(0), or else an arbitrage opportunity would arise. Therefore, the
price of the put must be P(0) ∼= 4.55 dollars.
1.10 The investor will buy 500
100 = 5 shares and
500
13.6364 ∼= 36.6667 options. Her final
wealth will then be 5×S(1)+36.6667×C(1), that is, 5×120+36.6667×20 ∼=
1, 333.33 dollars if the price of stock goes up to $120, or 5×80+36.6667×0 ∼=
400.00 dollars if it drops to $80.
1.11 a) If p = 0.25, then the standard deviation of the return is about 52% when
no option is purchased and about 26% with the option.
b) If p = 0.5, then the standard deviation of the return is about 60% and 30%,
respectively.
c) For p = 0.75 the standard deviation of the return is about 52% and 26%,
respectively.
1.12 The standard deviation of a random variable taking values a and b with
probabilities p and 1 −p, respectively, is |a −b|

p(1 −p). If no option is in-
volved, then the return on stock will be 60% or −60%, depending on whether
stock goes up or down. In this case |a −b| = |60% −(−60%)| = 120%. If
one option is purchased, then the return on the investment will be 35% or
−25%, and |a −b| = |35% −(−25%)| = 60%. Clearly, the standard deviation
|a −b|

p(1 −p) will be reduced by a half, no matter what p is.
Chapter 2
2.1 The rate r satisfies
	
1 + 61
365 × r

× 9, 000 = 9, 020.
This gives r ∼= 0.0133, that is, about 1.33%. The return on this investment
will be
K(0, 61
365) = 9, 020 −9, 000
9, 000
∼= 0.0022,
that is, about 0.22%.
2.2 Denote the amount to be paid today by P. Then the return will be
1, 000 −P
P
= 0.02.
The solution is P ∼= 980.39 dollars.

Solutions
267
2.3 The time t satisfies
(1 + t × 0.09) × 800 = 830,
which gives t ∼= 0.4167 years, that is, 0.4167 × 365 ∼= 152.08 days. The return
will be
K(0, t) = 830 −800
800
= 0.0375,
that is, 3.75%.
2.4 The principal P to be invested satisfies
	
1 + 91
365 × 0.08

× P = 1, 000,
which gives P ∼= 980.44 dollars.
2.5 The time t when the future value will be double the initial principal satisfies
the equation
	
1 + 0.06
365

365t
= 2.
The solution is t ∼= 11.5534 years. Because no interest will be paid for a fraction
of the last day, this needs to be rounded up to a whole number of days, which
gives 11 years and 202 days. (We disregard leap years and assume for simplicity
that each year has 365 days.)
2.6 The interest rate r satisfies the equation
(1 + r)10 = 2,
which gives r ∼= 0.0718, that is, about 7.18%.
2.7 a) In the case of annual compounding the value after two years will be
V (2) =
	
1 + 0.1
1

2×1
100 = 121.00
dollars.
b) Under semi-annual compounding the value will be
V (2) =
	
1 + 0.1
2

2×2
100 ∼= 121.55
dollars, which is clearly greater than in case a).
2.8 At 15% compounded daily the deposit will grow to
	
1 + 0.15
365

1×365
1, 000 ∼= 1, 161.80
dollars after one year. If interest is compounded semi-annually at 15.5%, the
value after one year will be
	
1 + 0.155
2

1×2
1, 000 ∼= 1, 161.01
dollars, which is less than in the former case.

268
Mathematics for Finance
2.9 The initial principal P satisfies the equation
(1 + 0.12)2 P = 1, 000.
It follows that P ∼= 797.19 dollars.
2.10 a) Under daily compounding the present value is
100, 000
	
1 + 0.05
365

−100×365
∼= 674.03
dollars.
b) If annual compounding applies, then the present value is
100, 000 (1 + 0.05)−100 ∼= 760.45
dollars.
2.11 The return will be
K(0, 1) =
	
1 + 0.1
12

12
−1 ∼= 0.1047,
that is, about 10.47%.
2.12 Using the binomial formula to expand the mth power, we obtain
K(0, 1) = (1 + r
m)m −1
= 1 + r + (1 −1
m)
2!
r2 + · · · + (1 −m−1
m )
m!
rm −1 > r
if m is an integer greater than 1.
2.13 Denote the interest rate by r, the amount borrowed by P and the amount of
each instalment by C,
C =
P
PA(r, 5) =
Pr
1 −(1 + r)−5 ,
see Example 2.4. Let n = 1, 2, 3, 4 or 5. The present value of the outstanding
balance after n −1 instalments are paid is equal to the amount borrowed
reduced by the present value of the first n −1 instalments:
P −
C
1 + r −· · · −
C
(1 + r)n−1 = P (1 + r)6−n −1
(1 + r)5 −1
.
The actual outstanding balance remaining after n−1 instalments are paid can
be found by dividing the above by the discount factor (1 + r)−(n−1), which
gives
P (1 + r)5 −(1 + r)n−1
(1 + r)5 −1
.
(S.1)
The interest included in the nth instalment is, therefore,
P (1 + r)5 −(1 + r)n−1
(1 + r)5 −1
r.
(S.2)

Solutions
269
The capital repaid as part of the nth instalment is the difference between the
outstanding balance of the loan after the (n −1)st and after the nth instal-
ment. By (S.1) this difference is equal to
P (1 + r)n −(1 + r)n−1
(1 + r)5 −1
= P r (1 + r)n−1
(1 + r)5 −1
.
(S.3)
Putting P to be $1, 000 and r to be 15% in (S.1), (S.2) and (S.3), we can
compute the figures collected in the table:
t (years)
interest paid ($)
capital repaid ($)
outstanding balance ($)
0
—
—
1, 000.00
1
150.00
148.32
851.68
2
127.75
170.56
681.12
3
102.17
196.15
484.97
4
72.75
225.57
259.40
5
38.91
259.40
0.00
2.14 The amount you can afford to borrow is
PA(18%, 10) × 10, 000 = 1 −(1 + 0.18)−10
0.18
× 10, 000 ∼= 44, 941
dollars.
2.15 The present value of the balance after 40 years is
PA(5%, 40) × 1, 200 = 1 −(1 + 0.05)−40
0.05
× 1, 200 ∼= 20, 591
dollars. Dividing by the discount factor (1 + 0.05)−40, we find that the actual
balance after 40 years will be
20, 591
(1 + 0.05)−40 ∼= 144, 960
dollars.
2.16 The annual payments will amount to
C =
100, 000
PA(6%, 10)
∼= 13, 586.80
dollars each. The outstanding balance to be paid to clear the mortgage after
8 years (once the 8th annual payment is made) will be
PA(6%, 2) × C ∼= 24, 909.93
dollars.
2.17 Suppose that payments C, C(1+g), C(1+g)2, . . . are made after 1 year, 2 years,
3 years, and so on. If the interest rate is constant and equal to r, then the
present values of these payments are C (1 + r)−1 , C(1 + g) (1 + r)−2 , C(1 +
g)2 (1 + r)−3 , . . . . The present value of the infinite stream of payments is,
therefore,
C
1 + r + C(1 + g)
(1 + r)2 + C(1 + g)2
(1 + r)3
+ . . . =
C
r −g .

270
Mathematics for Finance
The condition g < r must be satisfied or otherwise the series will be divergent.
Using this formula and the tail-cutting procedure, we can find that for a stream
of n payments
C
r −g −C(1 + g)n
r −g
1
(1 + r)n = C
1 −

1+g
1+r
n
r −g
.
2.18 The time t it will take to earn $1 in interest satisfies
e0.1t × 1, 000, 000 ∼= 1, 000, 001.
This gives t ∼= 0.00001 years, that is, 315.36 seconds.
2.19 a) The value in year 2000 of the sum of $24 for which Manhattan was bought
in 1626 would be
24e(2000−1626)×0.05 ∼= 3, 173, 350, 575
dollars, assuming continuous compounding at 5%.
b) The same amount compounded at 5% annually would be worth
24(1 + 0.05)2000−1626 ∼= 2, 018, 408, 628
dollars in year 2000.
2.20 $100 deposited at 10% compounded continuously will become
100e0.1 ∼= 110.52
dollars after one year. The same amount deposited at 10% compounded
monthly will become
100
	
1 + 0.1
12

12
∼= 110.47
dollars. The difference is about $0.05.
If the difference is to be less than $0.01, the compounding frequency m
should satisfy
100
	
1 + 0.1
m

m
> 110.51.
This means that m should be greater than about 55.19.
2.21 The present value is
1, 000, 000e−20×0.06 ∼= 301, 194
dollars.
2.22 The rate r satisfies
950e0.5r = 1, 000.
It follows that
r =
1
0.5 ln 1, 000
950
∼= 0.1026,
that is, about 10.26%.
2.23 The interest rate is
r = 0.03
2/12 = 0.18,
that is, 18%.

Solutions
271
2.24 The rate r satisfies
er =
	
1 + 0.12
12

12
.
The solution is r ∼= 0.1194, about 11.94%.
2.25 The frequency m satisfies
	
1 + 0.2
m

m
= 1 + 0.21.
Whence m = 2.0.
2.26 If monthly compounding at a rate r applies, then

1 +
r
12
12 = 1 + re and the
present value of the annuity is
V (0) =
C
1 +
r
12
+
C

1 +
r
12
2 + · · · +
C

1 +
r
12
12n
=
C
(1 + re)1/12 +
C
(1 + re)2/12 + · · · +
C
(1 + re)n
= C 1 −(1 + re)−n
(1 + re)1/12 −1
.
2.27 If bimonthly compounding at a rate r applies, then

1 + r
6
6 = 1 + re and the
present value of the perpetuity is
V (0) =
C
1 + r
6
+
C

1 + r
6
2 +
C

1 + r
6
3 + · · ·
=
C
(1 + re)1/6 +
C
(1 + re)2/6 +
C
(1 + re)3/6 + · · ·
= C
1
(1 + re)1/6 −1
.
2.28 We solve the equation
100 = 95 (1 + r)
1
2
for r to find the implied effective rate to be about 10.80%. If this rate remains
constant, then the bond price will reach $99 at a time t such that
100 = 99 (1 + r)( 1
2 −t) .
The solution is t ∼= 0.402 years, that is, about 0.402 × 365 ∼= 146.73 days. The
bond price will reach $99 on day 147.
2.29 The interest rate for annual compounding implied by the bond can be found
by solving the equation
(1 + r)−(1−0.5) = 0.9455
for r. The solution is about 11.86%. By solving the equation

1 + r
2
−2(1−0.5)
= 0.9455,
we obtain the semi-annual rate of about 11.53%, and solving
e−r(1−0.5) = 0.9455,
we find the continuous rate to be about 11.21%.

272
Mathematics for Finance
2.30 a) If the continuous compounding rate is 8%, then the price of the bond will
be
5e−0.08 + 5e−2×0.08 + 5e−3×0.08 + 105e−4×0.08 ∼= 89.06
dollars.
b) If the rate is 5%, then the price of the bond will be
5e−0.05 + 5e−2×0.05 + 5e−3×0.05 + 105e−4×0.05 ∼= 99.55
dollars.
2.31 The price of the bond as a function of the continuous compounding rate r can
be expressed as 5e−r + 5e−2r + 5e−3r + 105e−4r. The graph of this function is
shown in Figure S.1. When r ↘0, the price approaches 5 + 5 + 5 + 105 = 120
dollars. In the limit as r ↗∞the price tends to zero.
Figure S.1
Bond price versus interest rate in Exercise 2.31
2.32 The time t price of the coupon bond in Examples 2.9 and 2.10 is
10er(t−1) + 10er(t−2) + 10er(t−3) + 10er(t−4) + 110er(t−5)
if
0 ≤t < 1,
10er(t−2) + 10er(t−3) + 10er(t−4) + 110er(t−5)
if
1 ≤t < 2,
10er(t−3) + 10er(t−4) + 110er(t−5)
if
2 ≤t < 3,
10er(t−4) + 110er(t−5)
if
3 ≤t < 4,
110er(t−5)
if
4 ≤t < 5.
The graph is shown in Figure S.2.
2.33 In Figure S.2 we can see that the bond price will reach $95 for the first time dur-
ing year one, when the bond price is given by 10er(t−1)+10er(t−2)+10er(t−3)+
10er(t−4) + 110er(t−5). Putting r = 0.12, we can find the desired time t when
the price will reach $95 by solving the equation
10er(t−1) + 10er(t−2) + 10er(t−3) + 10er(t−4) + 110er(t−5) = 95.
This gives t ∼= 0.4257 years or 155.4 days.
2.34 Since the bond is trading at par, its initial price is the same as the face value
F = 100. The implied continuous compounding rate r can be found by solving
the equation
8e−r + 8e−2r + 108e−3r = 100.
This gives r ∼= 0.0770 or 7.70%.

Solutions
273
Figure S.2
Coupon bond price versus time in Exercise 2.32
2.35 By solving the equation
(1 + r)−1 = 0.89
we find that r ∼= 0.1236, that is, the effective rate implied by the bond is about
12.36%. The price of the bond after 75 days will be
B(75/365, 1) = B(0, 1) (1 + r)
75
365 = 0.89 (1 + 0.1236)
75
365 ∼= 0.9115
and the return will be
K(0, 75/365) = B(75/365, 1) −B(0, 1)
B(0, 1)
∼= 0.9115 −0.89
0.89
∼= 0.0242,
about 2.42%.
2.36 The initial price of a six-month unit bond is e−0.5r, where r denotes the implied
continuous rate. If the bond is to produce a 7% return over six months, then
1 −e−0.5r
e−0.5r
= 0.07,
which gives r ∼= 0.1353, or 13.53%.
2.37 The continuous rate implied by the bond satisfies
e−r = 0.92.
The solution is r ∼= 0.0834. At time t the bond will be worth 0.92ert. It will
produce a 5% return at a time t such that
0.92ert −0.92
0.92
= 0.05,
which gives t ∼= 0.5851 years or 213.6 days.
2.38 At time 0 we buy 1/B(0, 1) = er bonds, at time 1 we increase our holdings to
er/B(1, 2) = e2r bonds, and generally at time n we purchase e(n+1)r one-year
bonds.

274
Mathematics for Finance
2.39 Because the bond is trading at par and the interest rates remain constant,
the price of the bond at the beginning of each year will be $100. The sum of
$1, 000 will buy 10 bonds at the beginning of year one. At the end of the year
the coupons will pay 10 × 8 = 80 dollars, enough to buy 0.8 bonds at $100
each. As a result, the investor will be holding 10 + 0.8 = 10.8 bonds in year
two. At the end of that year the coupons will pay 10.8 × 8 = 86.4 dollars and
0.864 additional bonds will be purchased at $100 each. The number of bonds
held in year three will be 10.8 + 0.864 = 11.664, and so on.
In general, the number of bonds held in year n will be
10
	
1 +
8
100

n−1
,
which gives 10.0000, 10.8000, 11.6640, 12.5971, 13.6049 bonds held in years
one to five.
Chapter 3
3.1 The tree representing the scenarios and price movements in Example 3.1 is
shown in Figure S.3.
Figure S.3
Tree of price movements in Example 3.1
3.2 The tree representing the scenarios and price movements is shown in Fig-
ure S.4. There are altogether eight scenarios represented by the paths through
the tree leading from the ‘root’ on the left towards the rightmost branch tips.
3.3 We can use (3.1) to find
Scenario
S(0)
S(1)
S(2)
S(3)
ω1
45.00
49.50
51.98
46.78
ω2
45.00
47.25
51.98
57.17
ω3
45.00
47.25
42.53
46.78
The tree is shown in Figure S.5.
3.4 When dividends are payable, formula (3.1) becomes
S(n) = S(n −1)(1 + K(n)) −div(n),
which gives
Scenario
S(0)
S(1)
S(2)
S(3)
ω1
45.00
48.50
49.93
43.93
ω2
45.00
46.25
49.88
53.86
ω3
45.00
46.25
40.63
43.69

Solutions
275
Figure S.4
Tree of price movements in Exercise 3.2
Figure S.5
Tree of price movements in Exercise 3.3
3.5 The return over two time steps as compared to the sum of one-step returns
can take the following values:
Scenario
K(0, 2)
K(1) + K(2)
ω1
15.50%
15.00%
ω2
15.50%
15.00%
ω3
−5.50%
−5.00%
Over three time steps we have
Scenario
K(0, 3)
K(1) + K(2) + K(3)
ω1
3.95%
5.00%
ω2
27.05%
25.00%
ω3
3.95%
5.00%
The sum of one-step returns tends to be larger then the return over the total
interval if the sign of one-step returns alternates.
3.6 First find K(0, 2) and then the one-step returns K(1) = K(2) = K from the

276
Mathematics for Finance
relation 1 + K(0, 2) = (1 + K)2 (assuming that 1 + K > 0):
Scenario
K(0, 2)
K(1) = K(2)
ω1
17.14%
8.23%
ω2
−8.57%
−4.38%
ω3
−20.00%
−10.56%
3.7 The formula
1 + K(0, 2) = (1 + K(1)) (1 + K(2))
can be used to find K(2). For example, the following scenarios and values of
K(2) are consistent with the conditions of Exercise 3.7:
Scenario
K(0, 2)
K(1)
K(2)
ω1
21.00%
10.00%
10.00%
ω2
10.00%
10.00%
0.00%
ω3
−1.00%
−10.00%
10.00%
This is not the only possible solution. Another one can be obtained from the
above by changing scenario ω2 to
Scenario
K(0, 2)
K(1)
K(2)
ω2
10.00%
−10.00%
22.22%
with the other two scenarios unaltered.
3.8 For the three scenarios in Example 3.2 we find
Scenario
k(1)
k(2)
k(0, 2)
ω1
5.31%
3.39%
8.70%
ω2
5.31%
−10.92%
−5.61%
ω3
−5.61%
1.90%
−3.70%
In all three cases k(0, 2) = k(1) + k(2).
3.9 Let K denote the return in the third scenario. If the expected return is equal
to 6%, then
1
2 × (−5%) + 1
4 × 6% + 1
4 × K = 6%.
Solving for K, we find that the return in the third scenario must be 28%.
3.10 First, compute the returns K(1), K(2) and K(0, 2) in each scenario:
Scenario
K(1)
K(2)
K(0, 2)
ω1
10.00%
9.09%
20.00%
ω2
5.00%
−4.76%
0.00%
ω3
−10.00%
11.11%
0.00%
It follows that
E(K(1)) ∼= 0.25 × 10.00% + 0.25 × 5.00% −0.5 × 10.00% ∼= −1.25%,
E(K(2)) ∼= 0.25 × 9.09% −0.25 × 4.76% + 0.5 × 11.11% ∼=
6.64%,
E(K(0, 2)) ∼= 0.25 × 20.00% + 0.25 × 0.00% + 0.5 × 0.00% ∼=
5.00%.
Clearly,
(1 + E(K(1)))(1 + E(K(2))) ∼= 1.0530 ̸= 1.0500 ∼= 1 + E(K(0, 2)).

Solutions
277
3.11 Since the quarterly returns K(1), K(2), K(3), K(4) are independent and iden-
tically distributed,
E(K(1)) = E(K(2)) = E(K(3)) = E(K(4))
and
1 + E(K(0, 3)) = (1 + E(K(1))3,
1 + E(K(0, 4)) = (1 + E(K(1))4.
Thus, if E(K(0, 3)) = 12%, then the expected quarterly return E(K(1)) ∼=
3.85% and the expected annual return E(K(0, 4)) ∼= 16.31%.
3.12 By Condition 3.1 the random variables
S(1)
S(0) = 1 + K(1),
S(2)
S(1) = 1 + K(2),
S(3)
S(2) = 1 + K(3)
(S.4)
are independent, each taking two values 1 + d and 1 + u with probabilities p
and 1 −p, respectively.
The price S(2), which is the product of S(0) and the first two of these
random variables, takes up to four values corresponding to the four price
movement scenarios, that is, paths through the two-step tree of stock prices
shown in Figure 3.3 (in which S(0) = 1 for simplicity). Among these four
values of S(2) there are in fact only three different ones,
S(2) =



S(0)(1 + u)2
with probability p2,
S(0)(1 + u)(1 + d)
with probability 2p(1 −p),
S(0)(1 + d)2
with probability (1 −p)2.
The price S(3), which is the product of S(0) and the three independent
random variables in (S.4), takes up to eight values corresponding to the eight
price movement scenarios, that is, paths through the three-step tree of stock
prices in Figure 3.4 (with S(0) = 1 for simplicity). Among these eight values
of S(3) there are only four different ones,
S(3) =







S(0)(1 + u)3
with probability p3,
S(0)(1 + u)2(1 + d)
with probability 3p2(1 −p),
S(0)(1 + u)(1 + d)2
with probability 3p(1 −p)2,
S(0)(1 + d)3
with probability (1 −p)3.
3.13 The top values of S(1) and S(2) can be used to find u:
u = 92 −87
87
∼= 0.0575.
Next, u and the top value of S(1) give the value of S(0):
S(0) ∼=
87
1 + 0.0575
∼= 82.27
dollars. Finally, d is determined by S(0) and the bottom value of S(1):
d ∼= 76 −82.27
82.27
∼= −0.0762.

278
Mathematics for Finance
3.14 Given the continuous risk-free rate of 14% and the time step τ = 1/12, we
find the one-step return
r = e0.14/12 −1 ∼= 0.0117.
By Condition 3.2, u > r ∼= 0.0117. This means that the middle value S(0)(1 +
u)(1 + d) of S(2) must be no less than about 22(1 + 0.0117)(1 −0.01) ∼= 22.04
dollars.
3.15 Consider the system of equations
S(0)(1 + u)2 = 32,
S(0)(1 + u)(1 + d) = 28,
S(0)(1 + d)2 = x.
It follows that
32
28 = 1 + u
1 + d = 28
x
and x = 282/32 = 24.50 dollars. However, the tree cannot be reconstructed
uniquely. For any value S(0) > 0 one can find u and d consistent with the
data.
3.16 The values of u and d can be found by solving the equations
S(0)(1 + u)2 = 121,
S(0)(1 + d)2 = 100,
and selecting those solutions that satisfy 1+u > 0 and 1+d > 0. If S(0) = 100,
then u = 0.1 and d = 0. If S(0) = 104, then u ∼= 0.0786 and d ∼= −0.0194.
3.17 We only need to consider the values of d between −1 and r, that is, −1 < d <
1/10. As d increases between these two bounds, p∗decreases from 11/13 to 0.
The dependence of p∗on d is shown in Figure S.6.
Figure S.6
The risk-neural probability p∗as a function of d
3.18 By (3.4) the condition d < r < u is equivalent to d < p∗u+(1−p∗)d < u. This,
in turn, can be written as 0 < p∗(u −d) < u −d or, equivalently, 0 < p∗< 1.
3.19 By Proposition 3.5
E∗(S(3)|S(2) = 110) = 110(1 + r) = 110(1 + 0.2) = 132
dollars.

Solutions
279
3.20 By Condition 3.3 the random variables S(1)/S(0) = 1+K(1) and S(2)/S(1) =
1 + K(2) are independent, each taking three values 1 + d, 1 + n and 1 + u with
probabilities p, q and 1 −p −q, respectively. Therefore S(2), which is the
product of these two random variables and the number S(0), takes up to nine
values. Among these nine values there are only six different ones,
S(2) =













S(0)(1 + u)2
with probability p2,
S(0)(1 + n)2
with probability q2,
S(0)(1 + d)2
with probability (1 −p −q)2,
S(0)(1 + u)(1 + n)
with probability 2pq,
S(0)(1 + u)(1 + d)
with probability 2p(1 −p −q),
S(0)(1 + n)(1 + d)
with probability 2q(1 −p −q).
3.21 Let p∗, q∗, 1−p∗−q∗be the probabilities of upward, middle and downward price
movements, respectively. Condition (3.6) implies that 0.2p∗−0.1(1−p∗−q∗) =
0, that is, q∗= 1−3p∗and 1−p∗−q∗= 2p∗. Observe that p∗, 1−3p∗, 2p∗∈[0, 1]
if and only if p∗∈[0, 1/3]. It follows that p∗, q∗, 1 −p∗−q∗are risk-neutral
probabilities if and only if q∗= 1 −3p∗and p∗∈[0, 1/3].
3.22 Solving the system of equations
ln(1 + u) = mτ + σ√τ,
ln(1 + d) = mτ −σ√τ,
we find σ ∼= 0.052 and m ∼= 0.059.
3.23 Since p = 1/2 and ξ(n)2 = τ,
E(ξ(n)) = 1
2
√τ −1
2
√τ = 0,
Var(ξ(n)) = E(ξ(n)2) −E(ξ(n))2 = 1
2τ + 1
2τ = τ,
E(k(n)) = mτ + σE(ξ(n)) = mτ,
Var(k(n)) = σ2Var(ξ(n)) = σ2τ.
3.24 By (3.2)
S(1) = S(0)ek(1) = S(0)emτ+σξ(1),
S(2) = S(0)ek(1)+k(2) = S(0)e2mτ+σ(ξ(1)+ξ(2)).
3.25 Let t = n
N . Because the ξN(i) are independent, E(ξN(i)) = 0 and Var(ξN(i)) =
1
N for each i = 1, 2, . . . , it follows that
E(wN(t)) = E(ξN(1) + · · · + ξN(n))
= E(ξN(1)) + · · · + E(ξN(n)) = 0,
Var(wN(t)) = Var(ξN(1) + · · · + ξN(n))
= Var(ξN(1)) + · · · + Var(ξN(1)) = n
N = t.

280
Mathematics for Finance
Chapter 4
4.1 We can use the formulae in the proof of Proposition 4.1 to find
y(1) = 200 −35.24 × 60 −24.18 × 20
100
∼= −23.98,
V (1) ∼= 35.24 × 65 + 24.18 × 15 −23.98 × 110 ∼= 15.50,
y(2) = 15.50 + 40.50 × 65 −10.13 × 15
110
∼= 22.69,
V (2) ∼= −40.50 × 75 + 10.13 × 25 + 22.69 × 121 ∼= −38.60.
4.2 For a one-step strategy admissibility reduces to a couple of inequalities, V (0) ≥
0 and V (1) ≥0. The first inequality can be written as
10x + 10y ≥0.
The second inequality means that both values of the random variable V (1)
should be non-negative, which gives two more inequalities to be satisfied by x
and y,
13x + 11y ≥0,
9x + 11y ≥0.
The set of portfolios (x, y) satisfying all these inequalities is shown in Fig-
ure S.7.
Figure S.7
Admissible portfolios in Exercise 4.2
4.3 Suppose that there is a self-financing predictable strategy with initial value
V (0) = 0 and final value 0 ̸= V (2) ≥0, such that V (1) < 0 with positive
probability. The last inequality means that this strategy is not admissible, but
we shall construct an admissible one that violates the No-Arbitrage Principle.
Here is how to proceed to achieve arbitrage:
• Do not invest at all at time 0.
• At time 1 check whether the value V (1) of the non-admissible strategy is
negative or not. If V (1) ≥0, then refrain from investing at all once again.
However, if V (1) < 0, then take the same position in stock as in the non-
admissible strategy and a risk-free position that is lower by −V (1) than
that in the non-admissible strategy.

Solutions
281
This defines a predictable self-financing strategy. Its time 0 and time 1 value
is 0. The value at time 2 will be

0
if V (1) ≥0,
V (2) −V (1) > 0
if V (1) < 0.
This is, therefore, an admissible strategy realising an arbitrage opportunity.
4.4 If you happen to know that an increase in stock price will be followed by a fall
at the next step, then adopt this strategy:
• At time 0 do not invest in either asset.
• At time 1 check whether the stock has gone up or down. If down, then
again do not invest in either asset. But if stock has gone up, then sell
short one share for S(0)u, investing the proceeds risk-free.
Clearly, the time 0 and time 1 value of this strategy is V (0) = V (1) = 0. If
stock goes down at the first step, then the value at time 2 will be V (2) = 0.
But if stock goes up at the first step, then it will go down at the second step
and V (2) = S(0)u(r −d) will be positive, as required, since u > r > d. (The
notation is as in Section 3.2.)
Clearly, this is not a predictable strategy, which means that no arbitrage
has been achieved.
4.5 a) If there are no short-selling restrictions, then the following strategy will
realise an arbitrage opportunity:
• At time 0 do not invest at all.
• At time 1 check the price S(1). If S(1) = 120 dollars, then once again do
not invest at all. But if S(1) = 90 dollars, then sell short one share of the
risky asset and invest the proceeds risk-free.
The time 0 and time 1 value of this admissible strategy is 0. The value at
time 2 will be

0
in scenarios ω1 and ω2,
3
in scenario ω3,
which means that arbitrage can be achieved.
b) In a) above arbitrage has been achieved by utilising the behaviour of stock
prices at the second step in scenario ω2: The return on the risky asset is
lower than the risk-free return. Thus, shorting the risky asset and investing
the proceeds risk-free creates arbitrage. However, when short selling of risky
assets is disallowed, then this arbitrage opportunity will be beyond the reach
of investors.
4.6 The arbitrage strategy described in Solution 4.5 involves buying a fraction of
a bond. If S(1) = 90 dollars, then one share of stock should be shorted and
9
11 of a bond purchased at time 1. To obtain an arbitrage strategy involving
an integer number of units of each asset, multiply these quantities by 11, that
is, short sell 11 shares of stock and buy 9 bonds.
4.7 Suppose that transaction costs of 5% apply whenever stock is bought or sold.
An investor who tried to follow the strategy in Solution 4.5, short selling one
share of stock at time 1 if S(1) = 90 dollars, would have to pay transaction
costs of 90 × 5% = 4.50 dollars. If the remaining amount of 90 −4.50 = 85.50
dollars were invested risk-free, it would be worth 85.5 × 121
110 = 94.05 dollars
at time 2. But closing the short position in stock would cost $96, making the
final wealth negative. As a result, there is no arbitrage strategy.

282
Mathematics for Finance
4.8 The put option gives the right (but no obligation) to sell one share of stock
for the strike price X = 110 dollars at time 2. We consider an extended model
with three assets, the stock, the money market, and the option. The unit prices
of these assets are S(n), A(n), P E(n), where P E(n) is the market price of the
put option at time n = 0, 1, 2. The time 2 price of the put option is
P E(2) = max{X −S(2), 0}.
According to the Fundamental Theorem of Asset Pricing, the discounted stock
and option prices S(n) = S(n)/A(n) and P E(n) = P E(n)/A(n) should form a
martingale under some probability measure P∗, or else an arbitrage opportu-
nity would arise. From Example 4.5 we know that there is only one probability
P∗turning S(n) into a martingale. Because of this, P E(n) must be a martin-
gale under the same probability P∗. It follows that
P E(1) = A(1)
A(2)E∗(P E(2)|S(1))
and
P E(0) = A(0)
A(1)E∗(P E(1)).
Using the values of P∗for each scenario found in Example 4.5, we can compute
P E(1) and P E(0). For example
P E(1, ω3) = P E(1, ω4) = A(1)
A(2)
P∗(ω3)P E(2, ω3) + P∗(ω4)P E(2, ω4)
P∗(ω3) + P∗(ω4)
= 110
121
1
25 × 20 +
1
100 × 30
1
25 +
1
100
∼= 20.00
dollars. In this manner, we obtain
Scenario
P E(0)
P E(1)
P E(2)
ω1
1.96
1.21
0.00
ω2
1.96
1.21
4.00
ω3
1.96
20.00
20.00
ω4
1.96
20.00
30.00
Chapter 5
5.1 In the first investment project
E(K1) = 0.12 × 0.25 + 0.12 × 0.75 = 0.12,
Var(K1) = (0.12 −0.12)2 × 0.25 + (0.12 −0.12)2 × 0.75 = 0.
In the second project
E(K2) = 0.11 × 0.25 + 0.13 × 0.75 = 0.125,
Var(K2) = (0.11 −0.125)2 × 0.25 + (0.13 −0.125)2 × 0.75 = 0.000075.
Finally, in the third project
E(K3) = 0.02 × 0.25 + 0.22 × 0.75 = 0.17,
Var(K3) = (0.02 −0.17)2 × 0.25 + (0.22 −0.17)2 × 0.75 = 0.0075.
The first project is the least risky one, in fact, it is risk-free. The third project
involves the highest risk.

Solutions
283
5.2 First we put K2(ω2) = x and compute
Var(K1) = 0.001875,
Var(K2) = 0.187 5x2 + 0.015x + 0.0003.
The two securities will have the same risk if Var(K1) = Var(K2). This gives
the following equation
0.0003 + 0.187 5x2 + 0.015x = 0.001875
with two solutions x = −0.14 or 0.06. This means that K2(ω2) = −14% or
6%.
5.3 First we use the formula eki = 1 + Ki for i = 1, 2 to compute the logarithmic
returns and then work out the variance of each return:
Scenario
Probability
K1
K2
k1
k2
ω1
0.5
10.53%
7.23%
10.01%
6.98%
ω2
0.5
13.89%
10.55%
13.01%
10.03%
Variance
0.000282
0.000276
0.000224
0.000232
We find that Var(K1) > Var(K2), whereas Var(k1) < Var(k2).
This is an interesting observation because it shows that greater risk as
measured by Var(K) does not necessarily mean greater risk in the sense of
Var(k). Nevertheless, when the rates of return are of the order of 10% or lower,
the differences between these two measures of risk are tiny and can simply
be ignored in financial practice. This is because the errors due to inaccurate
estimation of the parameters (the probabilities and values of return rates in
different scenarios) are typically greater than these differences.
5.4 Let x1 and x2 be the number of shares of type 1 and 2 in the portfolio. Then
V (1) = x1S1(1) + x2S2(1) = V (0)
	
w1 S1(1)
S1(0) + w2 S2(1)
S2(0)

= 100
	
0.25 × 48
45 + 0.75 × 32
33

= 99.394.
5.5 The return on the portfolio is KV = w1K1 + w2K2. This gives
KV = 0.30 × 12% −0.7 × 4% = 0.8%
in scenario ω1,
KV = 0.30 × 10% + 0.7 × 7% = 7.9%
in scenario ω2.
5.6 The initial and final values of the portfolio are
V (0) = x1S1(0) + x2S2(0),
V (1) = x1S1(0)ek1 + x2S2(0)ek2
= V (0)

w1ek1 + w2ek2
.
As a result, the return on the portfolio is
ekV = V (1)
V (0) = w1ek1 + w2ek2.

284
Mathematics for Finance
5.7 First we find E(K1) = 7% and E(K2) = 23%. If the expected return on the
portfolio is to be E(KV ) = 20%, then by (5.4) and (5.1) the weights must
satisfy the system of equations
7w1 + 23w2 = 20,
w1 + w2 = 1.
The solution is w1 = 18.75% and w2 = 81.25%.
5.8 First, we find compute µ1 = 4% and µ2 = 16% from the data in Example 5.6.
Next, (5.7) and (5.1) give the system of equations
4w1 + 14w2 = 46,
w1 + w2 = 1,
for the weights w1 and w2. The solution is w1 = −3.2 and w2 = 4.2. Finally,
we use (5.7) with the values σ2
1 ∼= 0.0184, σ2
2 ∼= 0.0024 and ρ12 ∼= −0.96309
computed in Example 5.6 to find the risk of the portfolio:
σ2
V ∼= (−3.2)2 × 0.0184 + (4.2)2 × 0.0024
+2 × (−3.2) × 4.2 × (−0.96309) ×
√
0.0184 ×
√
0.0024
∼= 0.40278.
5.9 The returns on risky securities are non-constant random variables, that is,
K1(ω1) ̸= K1(ω2) and K2(ω1) ̸= K2(ω2). Because of this, the system of equa-
tions
K1(ω1) = aK2(ω1) + b,
K1(ω2) = aK2(ω2) + b,
must have a solution a ̸= 0 and b. It follows that K1 = aK2 + b.
Now, use the properties of covariance and variance to compute
Cov(K1, K2) = Cov(aK2 + b, K2) = aCov(K2, K2) = aVar(K2) = aσ2
2,
σ2
1 = Var(K1) = Var(aK2 + b) = a2Var(K2) = a2σ2
2.
It follows that σ1 = |a| σ2 and
ρ12 = Cov(K1, K2)
σ1σ2
= aσ2
2
|a| σ2
2
= ±1.
5.10 Using the values σ2
1 ∼= 0.0184, σ2
2 ∼= 0.0024 and ρ12 ∼= −0.96309 computed in
Example 5.6, we find s0 from (5.13):
s0 =
σ2
1 −ρ12σ1σ2
σ2
1 + σ2
2 −2ρ12σ1σ2
∼= 0.73809.
This means that the weights in the portfolio with minimum risk are w1 =
0.73809 and w2 = 0.26191 and it involves no short selling.
5.11 µV = 0.06, σV ∼= 1.013.
5.12 The weights of the three securities in the minimum variance portfolio are w ∼=
 0.314
0.148
0.538 
, the expected return on the portfolio is µV ∼= 0.173
and the standard deviation is σV ∼= 0.151.

Solutions
285
5.13 The weights in the portfolio with the minimum variance among all attainable
portfolios with expected return µV = 20% are w ∼=
 0.672
−0.246
0.574 
.
The standard deviation of this portfolio is σV ∼= 0.192.
5.14 The weights and standard deviations of portfolios along the minimum variance
line, parametrised by the expected return µV , are
w ∼=
 −2.027 + 13.492µV
2.728 −14.870µV
0.298 + 1.376µV

,
σV =

0.625 −6.946µV + 20.018µ2
V .
This minimum variance line is presented in Figure S.8, along with the set of
attainable portfolios with short selling (light shading) and without (darker
shading).
Figure S.8 Minimum variance line and attainable portfilios on the w2, w3 and
σ, µ planes
5.15 Let m be the one-row matrix formed by the expected returns of the three
securities. By multiplying the γwC = m −µu equality by C−1uT and, re-
spectively, C−1mT , we get
µV (m −µu)C−1uT = (m −µu)C−1mT ,
since wuT = 1 and wmT = µV . This can be solved for µ to get
µ = mC−1(mT −µV uT )
uC−1 (mT −µV uT )
∼= 0.142.
Then, γ can be computed as follows:
γ = (m −µu)C−1uT ∼= 1.367.
5.16 The market portfolio weights are w ∼=
 0.438
0.012
0.550 
. The expected
return on this portfolio is µM ∼= 0.183 and the standard deviation is σM ∼=
0.156.
5.17 βV ∼= 0.857, αV ∼= −0.102.

286
Mathematics for Finance
5.18 The expected return on the portfolio can be expressed as KV = w1K1 + · · · +
wnKn in terms of the expected returns on the individual securities. Because
covariance is linear in each of its arguments,
βV = Cov(KV , KM)
σ2
M
= w1 Cov(K1, KM)
σ2
M
+ · · · + wn Cov(Kn, KM)
σ2
M
= w1β1 + · · · + wnβn.
5.19 The equation of the characteristic line is y = βV x + αV , where βV is the
beta factor of that security and αV = µV −βV µM. In the CAPM the equation
µV = rF +(µM −rF )βV of the security market line holds. Substitution into the
formula for αV gives αV = rF −rF βV , so the equation of the characteristic line
becomes y = βV (x −rF ) + rF . Clearly, the characteristic line of any security
will pass through the point with coordinates rF , rF .
Chapter 6
6.1 Yes, there is an arbitrage opportunity. We enter into a long forward contract
and sell short one share, investing 70% of the proceeds at 8% and paying the
remaining 30% as a security deposit to attract interest at 4%. At the time of
delivery the cash investments plus interest will be worth about $18.20, out of
which $18 will need to be paid for one share to close out the short position in
stock. This leaves a $0.20 arbitrage profit.
The rates d for the security deposit such that there is no arbitrage oppor-
tunity satisfy 30% × 17 × ed + 70% × 17 × e8% ≤18. The highest such rate is
d ∼= 0.1740%.
6.2 We take 1 January 2000 to be time 0. By (6.2)
F(0, 3/4) = S(0)e0.06× 3
4 ,
F(1/4, 3/4) = 0.9S(0)e0.06× 2
4 .
It follows that the forward price drops by
F(0, 3/4) −F(1/4, 3/4)
F(0, 3/4)
= e
3
4 ×6% −0.9e
1
2 ×6%
e
3
4 ×6%
∼= 11.34%.
6.3 The present value of the dividends is
div0 = 1e−6
12 ×12% + 2e−9
12 ×12% ∼= 2.77
dollars. The right-hand side of (6.4) is equal to
[S(0) −div0]erT ∼= (120 −2.77)e
10
12 ×12% ∼= 129.56
dollars, which is less than the quoted forward price of $131. As a result, there
will be an arbitrage opportunity, which can be realised as follows:
• on 1 January 2000 enter into a short forward position and borrow $120 to
buy stock;
• on 1 July 2000 collect the first dividend of $1 and invest risk-free;
• on 1 October 2000 collect the second dividend of $2 and invest risk-free;
• on 1 November 2000 close out all positions.

Solutions
287
You will be left with an arbitrage profit of
131 −120e
10
12 ×12% + 1e
4
12 ×12% + 2e
1
12 ×12% ∼= 1.44
dollars.
6.4 No arbitrage profit can be realised in these circumstances. Though the theoret-
ical no-arbitrage forward price is about $87.83, the first strategy in the proof
of Proposition 6.2 brings a loss of 89 −83e10% + 2e0.5×7% ∼= −0.66 dollars and
the second one results in a loss of −89 + 83e7% −2e0.5×10% ∼= −2.08 dollars.
6.5 The euro plays the role of the underlying asset with dividend yield 3%. Hence
the forward price (the exchange rate) is
F(0, 1/2) = 0.9834e0.5(4%−3%) ∼= 0.9883
euros to a dollar.
6.6 At time t
• borrow and pay (or receive and invest, if negative) the amount V (t) to
acquire a short forward contract with forward price F(0, T) and delivery
date T,
• initiate a new long forward contact with forward price F(t, T) at no cost.
Then at time T
• close out both forward contracts receiving (or paying, if negative) the
amounts S(T) −F(0, T) and S(T) −F(t, T), respectively;
• collect V (t)er(T −t) from the risk-free investment, with interest.
The final balance V (t)er(T −t) −[F(t, T) −F(0, T)] > 0 will be your arbitrage
profit.
6.7 By (6.3) the initial forward price is F(0, 1) ∼= 45.72 dollars. This takes into
account the dividend paid at time 1/2.
a) If S(9/12) = 49 dollars, then F(9/12, 1) ∼= 49.74 dollars by (6.2). It
follows by (6.8) that V (9/12) ∼= 3.96 dollars.
b) If S(9/12) = 51 dollars, then F(9/12) ∼= 51.77 dollars and V (9/12) ∼=
5.96 dollars.
6.8 Let t = 1/365, T = 1/4. We apply the formula (6.11) to get
f(t, T) −f(0, T) = S(t)er(T −t) + S(0)erT = 0
if S(t) = S(0)ert, that is, if the stock grows at the risk-free rate.
6.9 Since f(t, T) = S(t)er(T −t), the random variables S(t) and f(t, T) are perfectly
correlated with ρS(t)f(t,T ) = 1 and σf(t,T ) = er(T −t)σS(t). It follows that N =
e−r(T −t).
6.10 Observe that Theorem 6.5 on the equality of futures and forward prices applies
also in the case of an asset with dividends paid continuously. We can, therefore,
use (6.6) to obtain
rdiv = 8% −
1
0.75 ln 14, 100
13, 500
∼= 2.20%.

288
Mathematics for Finance
6.11 The return on the index will be 3.37%. For rF = 1% this gives the futures prices
f(0, 3) ∼= 916.97 and f(1, 3) ∼= 938.49. If the beta coefficient for a portfolio is
βV = 1.5, then the expected return on this portfolio will be µV ∼= 4.56%.
To construct a portfolio with β V = 0 and initial value V (0) = 100 dollars,
supplement the original portfolio with N ∼= 0.1652 short futures contracts
(observe that N is the same as in Example 6.4).
If the actual return on the original portfolio during the first time step
happens to be equal to the expected return, then its value after one step will
be V (1) ∼= 104.56 dollars. Marking to market requires the holder of N ∼= 0.1652
short forward contracts to pay $3.56. As a result, after one step the value of
the portfolio with forward contracts will be V (1) ∼= 104.56 −3.56 = 101.00
dollars, once again matching the risk-free growth.
Chapter 7
7.1 The investment will bring a profit of
(36 −S(T))+ −4.50e0.12× 3
12 = 3,
where S(T) is the stock price on the exercise date. This gives S(T) ∼= 28.36
dollars.
7.2 E((S(T) −90)+ −8e0.09× 6
12 ) ∼= −5.37 dollars.
7.3 By put-call parity 2.83−P E = 15.60−15.00e−3
12 ×0.0672, so P E ∼= 1. 98 dollars.
7.4 Put-call parity is violated, 5.09 −7.78 > 20.37 −24e−0.0748× 6
12 . Arbitrage can
be realised as in the first part of the proof of Theorem 7.1:
• Buy a share for $20.37;
• Buy a put option for $7.78;
• Write and sell a call option for $5.09;
• Borrow $23.06 at the interest rate of 7.48%.
The balance of these transactions is zero. After six months
• Sell one share for $24 by exercising the put option or settling the short
position in calls, depending on whether the share price turns out to be
below or above the strike price;
• Repay the loan with interest, amounting to 23.06e
1
2 ×0.0748 ∼= 23.94 dollars
in total.
The balance of 24 −23.96 = 0.06 dollars will be your arbitrage profit.
7.5 If CE −P E > S(0) −div0 −Xe−rT , then at time 0 buy a share and a put
option, write and sell a call option, and invest (or borrow, if negative) the
balance on the money market at the interest rate r. As soon as you receive
the dividend, invest it at the rate r. At the exercise time T close the money
market investment and sell the share for X, either by exercising the put if
S(T) < X, or by settling the call if S(T) ≥X. The final balance (CE −P E −
S(0) + div0)erT + X > 0 will be your arbitrage profit.
On the other hand, if CE −P E < S(0) −div0 −Xe−rT , then at time 0 sell
short a share, write and sell a put, and buy a call option, investing the balance
on the money market. When a dividend becomes due on the shorted share,
borrow the amount and pay it to the owner of the stock. At time T close the
money market position, buy a share for X by exercising the call if S(T) > X
or settling the put if S(T) ≤X, and close the short position in stock. Your
arbitrage profit will be (−CE + P E + S(0) −div0)erT −X > 0.

Solutions
289
7.6 If CE −P E < S(0)e−rdivT −Xe−rT , then at time 0 sell short e−rdivT of a
share, write and sell a put, and buy a call option, investing the balance at
the rate r. Between time 0 and T pay dividends to the stock owner, raising
cash by shorting the stock. This will lead to one shorted share held at time T.
If the put option is exercised at time T, you will have to buy a share for X.
Use this share to close the short position in stock. You will be left with a call
option and a positive amount (−CE + P E + S(0)e−rdivT −Xe−rT )erT > 0. If
the put option is not exercised at all, then you can use the call to buy a share
for X at time T, closing the short position in stock. You will also be left with
a positive final balance (−CE + P E + S(0)e−rdivT −Xe−rT )erT > 0.
On the other hand, if CE −P E > S(0)e−rdivT −Xe−rT , then the opposite
strategy will also lead to arbitrage.
7.7 The strike price is equal to the forward price (more precisely, the exchange
rate) of 0.9883 euros to a dollar computed in Solution 6.5.
7.8 If S(0) −Xe−rT < CA −P A, then write and sell a call, buy a put, and buy
a share, investing (or borrowing, if negative) the balance at the rate r. Now
the same argument as in the first part of the proof of Theorem 7.2 applies,
except that the arbitrage profit may also include the dividend if the call is
exercised after the dividend becomes due. (Nevertheless, the dividend cannot
be included in this inequality because the option may be exercised and the
share sold before the dividend is due.)
If CA −P A < S(0) −div0 −X, then at time 0 sell short a share, write and
sell a put, and buy a call option, investing the balance at the rate r. If the put
is exercised at time t < T, you will have to buy a share for X, borrowing the
amount at the rate r. As the dividend becomes due, borrow the amount at the
rate r and pay it to the owner of the share. At time T return the share to the
owner, closing the short sale. You will be left with the call option and a positive
amount (S(0) + P A−CA −div0)erT −Xer(T −t) > XerT −Xer(T −t) ≥0. (If
the put is exercised before the dividend becomes due, you can increase your
arbitrage profit by closing out the short position in stock immediately, in which
case you would not have to pay the dividend.) If the put is not exercised before
expiry T, then the second part of Solution 7.5 applies.
7.9 If S(0) −Xe−rT < CA −P A, then use the same strategy as in the first part
of the proof of Theorem 7.2. The resulting arbitrage profit will in fact be
increased by the dividends accumulated up to the time when the call option
is exercised.
If CA −P A < S(0)e−rdivT −X, then at time 0 sell short e−rdivT of a
share, write and sell a put, and buy a call option, investing the balance at the
rate r. Between time 0 and T pay dividends to the stock owner, raising cash
by shorting the stock. This will lead to one shorted share held at time T. If
the put option is exercised at time t ≤T, you will have to buy a share for X,
borrowing this amount at the rate r. At time T use this share to close the short
position in stock. You will be left with a call option and a positive amount
(−CA + P A + S(0)e−rdivT )erT −Xer(T −t) ≥(−CA + P A + S(0)e−rdivT −
X)erT > 0 plus any dividends accumulated since the share was bought at
time t. If the put option is not exercised at all, then you can use the call to
buy a share for X at time T, closing the short position in stock. You will also
be left with a positive final balance (−CA + P A + S(0)e−rdivT )erT −X >
(−CA + P A + S(0)e−rdivT −X)erT > 0.
7.10 If CE > CA, then write and sell a European call and purchase an American
call. The difference CE −CA will be your arbitrage income. To keep it, do not

290
Mathematics for Finance
exercise the American option until expiry, when either both options will turn
out worthless, or the loss from settling the European call will be recovered by
exercising the American call. The argument for put options is similar.
7.11 Suppose that CE ≥S(0) −div0. In this case write and sell a call option and
buy stock, investing the balance on the money market. As soon as you receive
the dividends, also invest them on the money market. On the exercise date
you can sell the stock for at least min(S(T), X), settling the call option. Your
final wealth will be positive, (CE −S(0) + div0)erT + min(S(T), X) > 0. This
proves that CE < S(0) −div0.
The remaining bounds follow by the put-call parity relation (7.5) for
dividend-paying stock: S(0) −div0 −Xe−rT ≤CE, since P E ≥0; −S(0) +
div0 + Xe−rT ≤P E, since CE ≥0; and P E < Xe−rT , since CE < S(0) −div0.
7.12 For dividend-paying stock the regions determined by the bounds on call and
put prices in Proposition 7.3 are shown as shaded areas in Figure S.9.
Figure S.9 Bounds on European call and put prices for dividend-paying stock
7.13 If CA ≥S(0), then buy a share, write and sell an American call and invest
the balance CA −S(0) without risk. If the option is exercised before or at
expiry, then settle your obligation by selling the share for X. If the option
is not exercised at all, you will end up with the share worth S(T) at expiry.
In either case the final cash value of this strategy will be positive. The final
balance will in fact also include the dividend collected, unless the option is
exercised before the dividend becomes due.
7.14 Suppose that X′ < X′′, but CE(X′) ≤CE(X′′). We can write and sell a
call with strike price X′′ and buy a call with strike price X′, investing the
difference CE(X′′) −CE(X′) without risk. If the option with strike price X′′
is exercised at expiry, we will need to pay (S(T) −X′′)+. This amount can
be raised by exercising the option with strike price X′ and cashing the payoff
(S(T) −X′)+. Because X′ < X′′ and (S(T) −X′)+ ≥(S(T) −X′′)+ with
strict inequality whenever X′ < S(t), it follows that an arbitrage profit will
be realised.
The inequality for puts follows by a similar arbitrage argument.
7.15 Consider four cases:
1) If S(T) ≤X′ < X < X′′, then (7.9) reduces to 0 ≤0.
2) If X′ < S(T) ≤X < X′′, then (7.9) becomes 0 ≤α (S(T) −X′),
obviously satisfied for X′ < S(T).
3) If X′ < X < S(T) ≤X′′, then (7.9) can be written as S(T) −X ≤
α (S(T) −X′). This holds because X = αX′ + (1 −α)X′′ and S(T) ≤
X′′.

Solutions
291
4) Finally, if X′ < X < X′′ < S(T), then (7.9) becomes an equality,
S(T) −X = α (S(T) −X′) + (1 −α) (S(T) −X′′) because X = αX′ +
(1 −α)X′′.
7.16 Suppose that P E(S′) ≤P E(S′′) for some S′ < S′′, where S′ = x′S(0) and
S′′ = x′′S(0). Write and sell a put option on a portfolio with x′′ shares and
buy a put option on a portfolio with x′ shares, investing the balance P E(S′′)−
P E(S′) without risk. If the written option is exercised at time T, then the
liability can be met by exercising the other option. Since x′ < x′′, the payoffs
satisfy (X −x′S(T))+ ≥(X −x′′S(T))+ with strict inequality whenever X ≥
x′S(T). It follows that this is an arbitrage strategy.
7.17 Suppose that X′ < X′′, but CA(X′) ≤CA(X′′). We can write and sell the
call with strike price X′′ and purchase the call with strike price X′, investing
the balance CA(X′′) −CA(X′) without risk. If the written option is exercised
at time t ≤T, we will have to pay (S(t) −X′′)+. This liability can be met
by exercising the other option immediately, receiving the payoff(S(t) −X′)+.
Since (S(t) −X′′)+ ≤(S(t) −X′)+ with strict inequality whenever X′ < S(t),
this strategy leads to arbitrage.
The inequality for put options can be proved in a similar manner.
7.18 We shall prove Proposition 7.19 for American put options. The argument for
European puts is similar. By Proposition 7.15 P A(S) is a decreasing function
of S. When S ≥X, the intrinsic value of a put option is zero, and so the time
value, being equal to P A(S), is also a decreasing function of S. On the other
hand, P A(S′) −P A(S′′) ≤S′′ −S′ for any S′ < S′′ by Proposition 7.16. This
implies that P A(S′) −(X −S′)+ ≤P A(S′′) −(X −S′′)+ if S′ < S′′ ≤X, so
the time value is an increasing function of S for S ≤X. As a result, the time
value has a maximum at S = X.
Chapter 8
8.1 Let us compute the derivative of the price CE(0) of a call option with respect
to u. The formula for the price, assuming that Sd < X < Su, is
CE(0) =
1
1 + r
r −d
u −d[S(0)(1 + u) −X].
The derivative with respect to u is equal to
(r −d)[X −S(0)(1 + d)]
(1 + r)(u −d)2
= (r −d)[X −Sd]
(1 + r)(u −d)2 .
This is positive in our situation, since r > d and X > Sd, so CE(0) increases
as u increases.
The derivative of CE(0) with respect to d is equal to
−(u −r)[S(0)(1 + u) −X]
(1 + r)(u −d)2
= −(u −r)[Su −X]
(1 + r)(u −d)2 ,
which is negative, since r < u and X < Su. The option price decreases as d
increases.

292
Mathematics for Finance
8.2 If r = 0 and S(0) = X = 1, then CE(0) = −ud
u−d. For u = 0.05 and d = −0.05
we have u −d = 0.1 and CE(0) = 0.025 dollars. However, if u = 0.01 and
d = −0.19, then u −d = 0.2. The variance of the return on stock is equal to
(u −d)2p(1 −p) and is higher in the latter case, but the option price is lower:
CE(0) = 0.0095 dollars.
8.3 To replicate a call option the writer needs to buy stock initially and sell it
when the option is exercised. The following system of equations needs to be
solved to find the replicating portfolio:

110(1 −c)x + 1.05y = 10,
90(1 −c)x + 1.05y = 0.
For c = 2% we obtain x ∼= 0.5102 and y ∼= −42.8471, so the initial value of
the replicating portfolio will be 100x + y ∼= 8.1633 dollars. If c = 0, then the
replicating portfolio will be worth 7.1429 dollars. Note that the money market
position y is the same for each c.
8.4 The borrowing rate should be used to replicate a call, since the money market
position will be negative. This gives x(1) ∼= 0.6667 and y(1) ∼= −40.1786, so the
replicating portfolio value is 9.8214 dollars. For a put we obtain x(1) ∼= −0.3333
and y(1) ∼= 27.7778 using the rate for deposits, so the replicating portfolio will
be worth 2.7778 dollars initially.
The results are consistent with the put and call prices obtained from (8.3)
with the appropriate risk-neutral probability (computed using the correspond-
ing interest rate), p∗∼= 0.7333 for a call and p∗∼= 0.6 for a put.
8.5 The option price at time 0 is 22.92 dollars. In addition to this amount, the
option writer should borrow 74.05 dollars and buy 0.8081 of a share. At time 1,
if S(1) = 144, then the amount of stock held should be increased to 1 share,
the purchase being financed by borrowing a further 27.64 dollars, increasing
the total amount of money owed to 109.09 dollars. If, on the other hand,
S(1) = 108 dollars at time 1, then some stock should be sold to reduce the
number of shares held to 0.2963, and 55.27 dollars should be repaid, reducing
the amount owed to 26.18 dollars. (In either case the amount owed at time 1
includes interest of 7.40 dollars on the amount borrowed at time 0.)
8.6 At time 1 the stock prices Su = 144 and Sd = 108 dollars (the so-called cum-
dividend prices) drop by the amount of the dividend to 129 and 93 dollars
(the so-called ex-dividend prices). These prices generate the prices at time 2,
hence Suu = 154.80, Sud = 116.10, Sdu = 111.60 and Sdd = 83.70 dollars. The
option will be exercised with payoff34.80 dollars if the stock goes up twice.
In the remaining scenarios the payoffwill be zero. The option value at time 1
will be 21.09 dollars in the up state and zero dollars in the down state. The
replicating portfolio constructed at time 1 and based on ex-dividend prices
consists of 0.8992 shares and a loan of 94.91 dollars in the up state, and no
shares and no money market position in the down state. The option price
at time 0 is 12.78 dollars. Replication (based on the cum-dividend prices at
time 1, since the dividend is available to the owner of the stock purchased at
time 0) involves buying 0.5859 shares and borrowing 57.52 dollars.
8.7 From the Cox–Ross–Rubinstein formula CE(0) ∼= 5.93 dollars, P E(0) ∼= 7.76
dollars.
8.8 The least integer m such that S(0)(1 + u)m(1 + d)N−m > X is m = 35.
From the Cox–Ross–Rubinstein formula we obtain CE(0) ∼= 3.4661 dollars
and x(1) = [1 −Φ(m −1, N, q)] ∼= 0.85196 shares.

Solutions
293
8.9 The delta of a European call becomes equal to 1 at the first step n such that
the option will be in the money independently of whether the stock goes up
or down at the next step, that is, S(0)(1 + u)n(1 + d) > X (in this case
S(0)(1 + u)n+1 > X as well). This gives
n > ln X −ln S(0) −ln(1 + d)
ln(1 + u)
.
8.10 The stock values are
n
0
1
2
3
79.86
72.60
<
66.00
<
68.97
S(n)
60.00
<
62.70
<
57.00
<
59.57
54.15
<
51.44
The American put prices are
n
0
1
2
3
0.00
0.00
<
0.50
<
0.00
P A(n)
2.52
<
1.10
<
5.00
<
2.43
7.85
<
10.56
The option will be exercised early in the d node at time 1 or in the dd node
at time 2 (bold figures).
8.11 The values of the European and American calls are the same,
n
0
1
2
52.80
34.91
<
CE(n) = CA(n)
22.92
<
9.60
5.82
<
0.00
At time 2 both options have, of course, the same payoff. At time 1 the American
call will not be exercised in the up state, as this would bring only 24 dollars,
which less than the value of holding the option until expiry. In the down state
the American call will be out of the money and will not be exercised either.
Similarly, it will not be exercised at time 0. As a result, the American call is
equivalent to its European counterpart.
8.12 The ex-dividend stock prices are
n
0
1
2
12.32
11.20
<
/
10.64
S(n)
12.00
ex-div
\
10.34
9.40
<
8.93

294
Mathematics for Finance
The corresponding European and American put prices will be
n
0
1
2
1.68
1.68
2.53
2.80
<
/
3.36
3.36
P E(n)
P A(n)
3.42
3.69
\
3.66
3.66
4.33
4.60
<
5.07
5.07
At time 1 the payoffof the American put option in both the up and down
states will be higher than the value of holding the option to expiry, so the
option should be exercised in these states (indicated by bold figures).
8.13 Take b such that S(0)eσb+ru−1
2 σ2u = a and put V (t) = W(t)+

m −r + 1
2σ2 t
σ
for any t ≥0, which is a Wiener process under P∗. In particular, V (u) is nor-
mally distributed under P∗with mean 0 and variance u. The right-hand side
of (8.8) is therefore equal to
E∗

e−ruS(u)1S(u)<a

= S(0)E∗

eσV (u)−1
2 σ2u1V (u)<b

= S(0)
$ b
−∞
eσx−1
2 σ2u
1
√
2πt
e−x2
2u dx
= S(0)
$ b
−∞
1
√
2πt
e−(x−σu)2
2u
dx.
Now observe that, since V (t) is a Wiener process under P∗, the random vari-
ables V (u) and V (t) −V (u) are independent and normally distributed with
mean 0 and variance u and t −u, respectively. As a result, their joint density
is
1
2πte
−
y2
2(t−u) −x2
2u . This enables us to compute the left-hand side of (8.8),
E∗

e−rtS(t)1S(u)<a

= S(0)E∗

eσV (t)−1
2 σ2u1V (u)<b

= S(0)E∗

eσ(V (t)−V (u))+σV (u)−1
2 σ2u1V (u)<b

= S(0)
$ b
−∞
	$ ∞
−∞
eσy+σx−1
2 σ2t 1
2πte
−
y2
2(t−u) −x2
2u dy

dx
= S(0)
$ b
−∞
	$ ∞
−∞
1
2πte
−(y−σ(t−u))2
2(t−u)
−(x−σu)2
2u
dy

dx
= S(0)
$ b
−∞
1
√
2πt
e−(x−σu)2
2u
dx
We can now see that the two sides of (8.8) are equal to one another.

Solutions
295
8.14 Consider the distribution function
F(x) = P∗{W(t) < x} = P∗

V (t) < x +
	
m −r + 1
2σ2

 t
σ
(
=
$ x+(m−r+ 1
2 σ2) t
σ
−∞
1
√
2π
e−y2
2 dy,
where V (t) = W(t) +

m −r + 1
2σ2 t
σ is normally distributed under P∗. As
a result, the density of W(t) under P∗is
dF(x)
dx
=
1
√
2π
e−1
2(x+(m−r+ 1
2 σ2) t
σ )
2
.
8.15 By put-call parity, for t = 0
P E(0) = CE(0) −S(0) + Xe−rT
= S(0)(N(d1) −1) −Xe−rT (N(d2) −1)
= −S(0)N(−d1) + Xe−rT N(−d2).
Now, by substituting t for 0 and T −t for T, we obtain the Black–Scholes
formula for P E(t).
Chapter 9
9.1 By put-call parity (7.1)
d
dS P E(S) = d
dS CE(S) −1 = N(d1) −1 = −(1 −N(d1)) = −N(−d1),
where d1 is given by (8.9). The delta of a put option is negative, consistently
with the fact that the value of a put option decreases as the price of the
underlying asset increases.
9.2 We maximise 581.96 × S −30, 779.62 −1, 000 × CE(S,
1
365), where S stands for
the stock price after one day, and CE(S, t) is the price of a call at time t, one
day in our case, with 89 days to maturity, and where σ = 30% and r = 8%,
as before. Equating the derivative with respect to S to zero, we infer that the
delta of the option after one day should be the same as the delta on day zero,
d
dS CE(S,
1
365) = 0.58196. This gives the following condition for the stock price
(after inverting the normal distribution function):
ln S
60 + (r + 1
2σ2) ×
89
365
σ

89
365
= ln 60
60 + (r + 1
2σ2) ×
90
365
σ

90
365
.
The result is S ∼= 60.0104 dollars.
9.3 The premium for a single put is 0.031648 dollars (from the Black–Scholes
formula), so the bank will receive 1, 582.40 dollars by writing and selling 50, 000
puts. The delta of a single put is −0.355300, so the delta-hedging portfolio
requires shorting 17, 765.00 shares, which will raise 32, 332.29 dollars. This
gives a total of 33, 914.69 dollars received to be invested at 5%. The value of
the delta neutral portfolio consisting of the shored stock, invested cash and
sold options will be −32, 332.29 + 33, 914.69 −1, 582.40 = 0.00 dollars.

296
Mathematics for Finance
One day later the shorted shares will be worth 17, 765 × 1.81 = 32, 154.64
dollars, whereas the cash investment will grow to 33, 914.69e0.05/365 ∼= 33, 919.34
dollars. The put price will increase to 0.035182 dollars, so the price of 50, 000
puts will be 1, 759.11 dollars. The value of the delta neutral portfolio will be
−32, 154.64 + 33, 919.34 −1, 759.11 ∼= 5.59 dollars.
9.4 The price of a single put after one day will now be 0.038885 dollars, the 50, 000
options sold will therefore be worth 1944.26 dollars, the stock and cash deposit
positions remaining as in Solution 9.3. The delta neutral portfolio will bring
a loss of 179.56 dollars.
9.5 If the stock price does not change, S(t) = S(0) = S, then the value of the
portfolio after time t will be given by
V (t) = SN(d1) −Xerte−rT N(d2) −CE(S, t),
where CE(S, t) is given by the Black–Scholes formula and d1, d2 by (8.9). Then
d
dtV (t)
!!!!
t=0
= −rXe−rT N(d2) −d
dtCE(S, t)
!!!!
t=0
= −rXe−rT N(d2) −thetaCE
=
σS
2
√
2πT
e−d2
1/2,
which is positive.
9.6 Using put-call parity and the Greek parameters for a call, we can find those
for a put:
deltaP E = N(d1) −1 = deltaCE −1 = −N(−d1),
gammaP E = gammaCE,
thetaP E = −
Sσ
2
√
2πT
e−
d2
1
2 + rXe−rT N(−d2),
vegaP E = vegaCE,
rhoP E = −TXe−rT N(−d2).
(The Greek parameters are computed at time t = 0.) These equalities can also
be verified directly by differentiating the Black–Scholes formula for the put
price.
9.7 The rho of the original option is 7.5878, the delta of the additional option is
0.4104 and the rho is 7.1844. The delta-rho neutral portfolio requires buying
approximately 148.48 shares of stock and 1, 056.14 additional options, while
borrowing $7, 693.22. The position after one day is presented in the following
table, in which we also recall the results of the delta hedge:
delta-rho
delta
S(
1
365)
r = 8%
r = 9%
r = 15%
r = 9%
58.00
−7.30
−9.65
−26.14
−133.72
58.50
−2.71
−4.63
−17.95
−97.22
59.00
0.18
−1.23
−10.93
−72.19
59.50
1.59
0.77
−4.85
−58.50
60.00
1.76
1.60
0.52
−55.96
60.50
0.92
1.50
5.45
−64.38
61.00
−0.68
0.72
10.16
−83.51
61.50
−2.78
−0.47
14.90
−113.07
62.00
−5.13
−1.84
19.91
−152.78

Solutions
297
9.8 With 95% probability the logarithmic return on the exchange rate satisfies
k > m + xσ ∼= −23.68%, where x ∼= −1.645, so that N(x) ∼= 5%. The 1, 000
dollars converted into euros, invested without risk at the rate rEUR, and con-
verted back into dollars after one year, will give 1, 000erEURek dollars. With
probability 95% this amount will satisfy
1, 000erEURek > 1, 000erEURem+xσ ∼= 821.40 dollars.
On the other hand, 1, 000 dollars invested at the rate rUSD would have grown
to 1, 000erUSD ∼= 1, 051.27 dollars. As a result,
VaR = 1, 000erUSD −1, 000erEURem+xσ ∼= 229.88 dollars.
9.9 A single call costs $21.634. We purchase approximately 46.22 options. With
probability 5% the stock price will be less than $49.74. We shall still be able
to exercise the options, cashing $450.18 in the borderline case. The alternative
risk-free investment of $1, 000 at 8% would grow to $1, 040.81. Hence VaR ∼=
590.63 dollars. If the stock grows at the expected rate, reaching $63.71, then
we shall obtain $1, 095.88 when the options are exercised. With 5% probability
the stock price will be above $81.6 and then our options will be worth at least
$1, 922.75.
9.10 The cost of a single bull spread is $0.8585, with expected return 29.6523%,
standard deviation 99.169%, and VaR equal to $15, 000 (at 74.03% confidence
level). If 92.95% of the capital is invested without risk and the remainder in
the bull spread, then the expected return will the same as on stock, with risk
of 6.9957% and VaR equal to $650.
9.11 A put with strike price $56 costs $0.426. A put with strike price $58 costs
$0.9282. The expected return on the bear spread is 111.4635%, the risk reach-
ing 177.2334%. The worst case scenario (among those admitted by the an-
alyst) is when the stock price drops to $58.59. In this scenario, which will
happen with conditional probability 0.3901, the investor will lose everything,
so VaR = 15, 000 dollars at 60.99% confidence level.
Chapter 10
10.1 The yields are y(0) ∼= 14.08% and y(3) ∼= 13.63%. Thus B(0, 3) = e−3τy(0) ∼=
0.9654 dollars. Arbitrage can be achieved as follows:
• At time 0 buy a 6-month bond for B(0, 6) = 0.9320 dollars, raising the
money by issuing 0.9654 of a 3-month bond, which sells at B(0, 3) ∼= 0.9654
dollars.
• At time 3 (after 3 months) issue 0.9989 of a 3-month bond, which sells
at B(3, 6) = 0.9665 dollars, and use the proceeds of $0.9654 to settle the
fraction of a 3-month bond issued at time 0.
• At time 6 (after half a year) the 6-month bond bought at time 0 will pay $1,
out of which $0.9989 will settle the fraction of a 3-month bond issued at
time 3.
The balance of $0.0011 will be the arbitrage profit.
10.2 The implied rates are y(0) ∼= 12.38% and y(6) ∼= 13.06%. Investing $100,
we can buy 106.38 bonds now and 113.56 after six months. The logarithmic
return over one year is ln(113.56/100) ∼= 12.72%, the arithmetic mean of the
semi-annual returns.

298
Mathematics for Finance
10.3 To achieve a return of 14%, we would have to sell the bond for 0.8700e14% ∼=
1.0007 dollars, which is impossible. (A zero-coupon bond can never fetch a
price higher than its face value.)
In general, we have to solve the equation B(0, 12)ek = e−τy(6) to find
y(6), where k is the prescribed logarithmic return. The left-hand side must be
smaller than 1.
10.4 During the first six months the rate is y(n) ∼= 8.34%, for n = 0, . . . , 179,
and during the rest of the year y(n) ∼= 10.34%, for n = 180, . . . , 360. The
bond should be sold for 0.92e4.88% ∼= 0.9660 dollars or more. This cannot
be achieved during the first six months, since the highest price before the
rate changes is B(179, 360) ∼= 0.9589 dollars. On the day of the rate change
B(180, 360) ∼= 0.9496 dollars, and we have to wait until day n = 240, on which
the bond price will exceed the required $0.9660 for the first time.
10.5 The rate can be found by using a spreadsheet with goal seek facility to solve
the equation
10.896 ×

10 + 10e−y(1) + 10e−2y(1) + 110e−3y(1)
= 1, 000ek.
This gives y(1) ∼= 12.00% for k = 12% in case a), y(1) ∼= 12.81% for k = 10%
in case b) and y(1) ∼= 11.19% for k = 14% in case c).
10.6 The numbers were found using an Excel spreadsheet with accuracy higher
than the displayed 2 decimal points.
10.7 Scenario 1: $1, 427.10; Scenario 2: $1, 439.69.
10.8 Formula (10.2) can be applied directly to find D ∼= 1.6846.
10.9 The duration is equal to 4 if the face value is $73.97. The smallest possible
duration, which corresponds to face value F = $0, is about 2.80 years. For
very high face values F the duration is close to 5, approaching this number as
F goes to infinity.
When F = 100, the coupon value C ∼= 13.52 gives duration of 4 years. If
the coupon value is zero, then the duration is 5 years. For very high coupon
values C tending to infinity the duration approaches about 2.80 years.
10.10 Since the second derivative of P(y) is positive,
d2
dy2 P(y) = (τn1)2C1e−τn1y + (τn2)2C2e−τn2y + · · · + (τnN)2(CN + F)e−τnN y
> 0,
P is a convex function of y.
10.11 Solving the system 6 = 2wA + 3.4wB, wA + wB = 1, we find wA ∼= −1.8571
and wB ∼= 2.8571. As a result, we invest $14, 285.71 to buy 14, 005.60 bonds B,
raising the shortfall of $9, 285.71 by issuing 9, 475.22 bonds A.
10.12 The yield on the coupon bond A is about 13.37%, so the price of the zero-
coupon bond B is $87.48. The coupon bond has duration 3.29 and we find
the weights to be wA ∼= 0.4366 and wB ∼= 0.5634. This means that we invest
$436.59 to buy 4.2802 bonds A and $563.41 to buy 6.4403 bonds B.
10.13 Directly from the definition (10.2) of duration we compute the duration Dt at

Solutions
299
time t (note that the bond price grows by a factor of eyt),
Dt =
1
eytP(y)

(τn1 −t)C1e−y(τn1−t) + · · · + (τnN −t)(CN + F)e−y(τnN −t)
=
1
P(y)

(τn1 −t)C1e−τn1y + · · · + (τnN −t)(CN + F)e−τnN y
= D0 −t,
since the weights C1e−τn1y/P(y), C2e−τn2y/P(y), . . . , (CN + F)e−τnN y/P(y)
add up to one.
10.14 Denote the annual payments by C1, C2 and the face value by F, so that
P(y) = C1e−y + (C2 + F)e−2y,
D(y) = C1e−y + 2(C2 + F)e−2y
P(y)
.
Compute the derivative of D(y) to see that it is negative:
d
dy D(y) = −C1(C2 + F)e−3y
P(y)2
< 0.
10.15 We first find the prices and durations of the bonds: PA(y) ∼= 120.72, PB(y) ∼=
434.95, DA(y) ∼= 1.8471, DB(y) ∼= 1.9894. The weights wA ∼= −7.46%, wB ∼=
107.46% give duration 2, which means that we have to buy 49.41 bonds B and
issue 12.35 bonds A. After one year we shall receive $247.05 from the coupons
of B and will have to pay the same amount for the coupons of A. Our final
amount will be $23, 470.22, exactly equal to the future value of $20, 000 at 8%,
independently of any rate changes.
10.16 If the term structure is to be flat, then the yield y(0, 6) = 8.16% applies to
any other maturity, which gives B(0, 3) = 0.9798 dollars and B(0, 9) = 0.9406
dollars.
10.17 Issue and sell 500 bonds maturing in 6 months with $100 face value, obtaining
$48, 522.28. Use this sum to buy 520.4054 one-year bonds. After 6 months
settle the bonds issued by paying $50, 000. After one year cash the face value
of the bonds purchased. The resulting rate is 8%.
10.18 You need to deposit 100, 000e−8.41%/12 ∼= 99, 301.62 dollars for one month,
which will grow to the desired level of $100, 000, and borrow the same amount
for 6 months at 9.54%. Your customer will receive $100, 000 after 1 month
and will have to pay 99, 301.62e9.54%/2 ∼= 104, 153.09 dollars after 6 months,
which implies a forward rate of 9.77%. (The rate can be obtained directly from
(10.5).)
The rate for a 4-month loan starting in 2 months is
f(0, 2, 6) = 6 × 9.35% −2 × 8.64%
4
∼= 10.09%,
so a deposit at 10.23% would give an arbitrage opportunity.
10.19 To see that the forward rates f(n, N) may be negative, let us analyse the case
with n = 0 for simplicity. Then
f(0, N) = (N + 1)y(0, N + 1) −Ny(0, N)

300
Mathematics for Finance
and f(0, N) < 0 requires that (N + 1)y(0, N + 1) < Ny(0, N). The border
case is when y(0, N + 1) =
N
N+1y(0, N), which enables us to find a numerical
example. For instance, for N = 8 and y(0, 8) = 9% a negative value f(0, 8)
will be obtained if y(0, 9) < 8
9 × 9% = 8%.
10.20 Suppose that f(n, N) increases with N. We want to show that the same is
true for
y(n, N) = f(n, n) + f(n, n + 1) + · · · + f(n, N −1)
N −n
.
This follows from the fact that if a sequence an increases, then so does the
sequence of averages Sn = a1+···+an
n
. To see this multiply the target inequality
Sn+1 > Sn by n(n + 1) to get (after cancellations) nan+1 > a1 + · · · + an. The
latter is true, since an+1 > ai for all i = 1, . . . , n.
10.21 The values of B(0, 2), B(0, 3), B(1, 3) have no effect on the values of the money
market account.
10.22 a) For an investment of $100 in zero-coupon bonds, divide the initial cash
by the price of the bond B(0, 3) to get the number of bonds held, 102.82,
which gives final wealth of $102.82. The logarithmic return is 2.78%. b) For an
investment of $100 in single-period zero-coupon bonds, compute the number
of bonds maturing at time 1 as 100/B(0, 1) ∼= 100.99. Then, at time 1 find the
number of bonds maturing at time 2 in a similar way, 100.99/B(1, 2) ∼= 101.54.
Finally, we arrive at 101.54/B(2, 3) ∼= 102.51 bonds, each giving a dollar at
time 3. The logarithmic return is 2.48%. c) An investment of $100 in the money
market account, for which we receive 100A(3) ∼= 102.51 at time 3, produces
the same logarithmic return of 2.48% as in b).
Chapter 11
11.1 We begin from the right, that is, from the face values of the bonds, first
computing the values of B(2, 3) in all states. These numbers together with
the known returns give B(1, 3; u) and B(1, 3; d). These, in turn, determine the
missing returns k(2, 3; ud) = 0.20% and k(2, 3; dd) = 0.16%. The same is done
for the first step, resulting in k(1, 3; d) = 0.23%. The bond prices are given in
Figure S.10.
Figure S.10
Bond prices in Solution 11.1
11.2 Because of the additivity of the logarithmic returns, k(1, 3; u) + k(2, 3; uu) +
k(3, 3; uuu) = 0.64% gives the return in the period of three weeks. To obtain
the yield we have to rescale it to the whole year by multiplying by 52/3, hence
y(0, 3) = 11.09%. Note that we must have k(1, 3; u)+k(2, 3; ud)+k(3, 3; udu) =

Solutions
301
0.64% which allows us to find k(2, 3; ud) = 0.20%. The other missing returns
can be computed in a similar manner, first k(1, 3; d), then k(2, 3; dd).
11.3 The bond prices are given in Figure S.11.
Figure S.11
Bond prices in Solution 11.3
11.4 The money market account is given in Figure S.12. Note that the values for
the ‘up’ movements are lower than for the ‘down’ movements. This is related
to the fact that the yield decreases as the bond price increases, and our trees
are based on bond price movements.
Figure S.12
Money market account in Solution 11.4
11.5 The prices B(1, 2; u) = 0.9980 and B(1, 2; d) = 0.9975 are found by discounting
the face value 1 to be received at time 2, using the short rates r(1; u) and
r(1; d). The price B(0, 2) = 0.9944 can be found by the replication procedure.
11.6 At time 2 the coupons are 0.5227 or 0.8776, depending on whether we are in
the up or down state at time 1. At time 1 the coupon is 0.9999.
11.7 At time 1 we find 18.0647 = (0.8159 × 20 + 0.1841 × 10)/1.0052 in the up
state and 1.7951 = (0.1811 × 10 + 0.8189 × 0)/1.0088 in the down state. Next,
applying the same formula again, we obtain 7.9188 = (0.3813 × 18.3928 +
0.6187 × 1.7951)/1.01.
11.8 There is an arbitrage opportunity at time 1 in the up state. The price
B(1, 2; u) = 0.9924 implies that the growth factor in the money market is
1.00766, whereas the prices of the bond maturing at time 3 imply growth fac-
tors 1.01159 and 1.00783. To realise arbitrage, bonds with maturity 3 should
be bought, the purchase financed by a loan in the money market.

