# Term Structure Modeling & Bond Portfolio

!!! info "Source"
    **The Mathematics of Financial Modeling and Investment Management** by Sergio M. Focardi and Frank J. Fabozzi, Wiley, 2004.
    These notes are used for educational purposes.

## Term Structure Modeling and Valuation

CHAPTER 20 
Term Structure Modeling and 
Valuation of Bonds and 
Bond Options 
I
n this chapter we introduce the concepts and mathematical technology 
of bond and bond option valuation. We will begin by analyzing the 
behavior of bond prices in a deterministic interest rate environment 
(i.e., assuming that interest rates are known at every future date). We 
will then move on to a full stochastic description of interest rates and of 
the term structure of interest rates and will tackle bond and bond option 
valuation problems in this environment. 
The term structure of interest rates plays a key role in financial decision-
making and investment management. Richard McEnally and James Jordan1 
provide the following list of uses for the term structure of interest rates:
 ■ Analyzing the potential returns for investments with different maturi-
ties.
 ■ Assessing market consensus expectations of future interest rates.
 ■ Pricing bonds and other fixed-income contractual obligations.
 ■ Pricing contingent claims in which the underlying is a fixed-income 
security.
 ■ Arbitraging between bonds with different maturities.
 ■ Forming expectations about the economy (e.g., economic activity and 
inflation). 
1 Richard W. McEnally and James V. Jordan, “The Term Structure of Interest 
Rates,” Chapter 43 in Frank J. Fabozzi (ed.), The Handbook of Fixed Income Secu-
rities: Fifth Edition (Chicago: Irwin Professional Publishing, 1997), pp. 818–822. 
593 

594 
The Mathematics of Financial Modeling and Investment Management 
The estimation of the term structure of interest rates is referred to as 
term structure modeling. We will explain how this is done in this chapter. 
BASIC PRINCIPLES OF VALUATION OF DEBT INSTRUMENTS 
A useful way of understanding the valuation of debt instruments and 
how this relates to interest rates is to use the principle that, in perfect 
markets, all riskless instruments have the same short-term return which 
must coincide with the riskless short-term rate for that period. This con-
dition may be expected to be enforced through arbitrage. The 1-period 
rate of return from, say, an instrument with maturity n and a cash flow 
denoted by (a1, ..., an), consists of the cash payment, a1, plus the capital 
gain, or the difference between the next-period price and the current 
price of the security, expressed as a percentage of initial value. 
Let us denote by nPj the price j periods (j < n) from the present of an 
instrument maturing n periods later; the capital gain for the current 
period is: n–1P1 – P0. Hence the condition that the 1-period return
n
from holding the instrument must be equal to the short-term rate for the 
forthcoming period, denoted by r1, can be written as 
a1 + (
)
n – 1P1 – nP0 
---------------------------------------------- = r1 
(20.1) 
nP0 
Solving for nP0, 
a1 + n – 1P1 
= ---------------------------
(20.2)
nP0 
1 + r1 
The reason why the right-hand side of equation (20.2) must be the 
equilibrium price of the n-period asset is that, as can be verified, if the 
current price, P0, were larger than the right-hand side of equation
n
(20.2), then the 1-period return of the debt instrument, given by equa-
tion (20.1), would be smaller than the return r1 obtainable by investing 
in the 1-period debt instrument. As a result, no one would want to hold 
it, causing its price to drop. Similarly, if nP0 is smaller than the right-
hand side of equation (20.2), this yield for the debt instrument would be 
larger than r1, and everyone would want to hold it. 
Next we observe that n–1P1 must satisfy an equation like equation 
(20.2), or 

595 
Term Structure Modeling and Valuation of Bonds and Bond Options 
a2 + n – 2P2 
= ---------------------------
n – 1P1 
1 + r2 
Substituting this equation into equation (20.2), we get 
a1 
a2 + n – 2P2 
= ------------------- + ---------------------------------------
nP0 
(1 + r1)
(1 + r1)(1 + r2) 
Repeating the same substitution recursively, up to the maturity of the 
debt instrument, we find 
= ------------------- + --------------------------------------- + … + -----------------------------------------------------------------
(20.3)
nP0 
a1 
a2 
an 
(1 + r1)
(1 + r1)(1 + r2)
(1 + r1)(1 + r2)…(1 + r )
n 
In other words, the debt instrument must equal the sum of the present 
value of the payments that the debtor is required to make until maturity. 
Let’s illustrate the principles to this point. Assume that the length of 
a period is one year. Suppose that an investor purchases a 4-year debt 
instrument with the following payments promised by the borrower: 
Year 
Interest Payment 
Principal Repayment 
Cash Flow 
1 
$100
 $0
 $100 
2
 120
 0
 120 
3
 140
 0
 140 
4
 150 
1,000 
1,150 
In terms of our notation: a1 = $100; a2 = $120; a3 = $140; a4  = 
$1,150. Assume that the 1-year rates for the next four years are: r1 = 
0.07; r2 = 0.08; r3 = 0.09; r4 = 0.10. The current value or price of this 
debt instrument today, denoted 4P0, using equation (20.3) is then 
100 
120 
140
P
4
0
 = --------------- + -------------------------------- + -------------------------------------------------
(1.07)
(1.07)(1.08)
(1.07)(1.08)(1.09) 
1,150
+ ------------------------------------------------------------------ = $1,138.43 
(1.07)(1.08)(1.09)(1.10) 

596 
The Mathematics of Financial Modeling and Investment Management 
YIELD-TO-MATURITY MEASURE 
Next we must consider how to construct a measure that will permit us 
to compare the rate of return of debt instruments having different cash 
flows and different maturities. For 1-period debt instruments, the mea-
sure is clear; it is provided by the left-hand side of equation (20.1). But 
that approach cannot be generalized readily to long-term debt instru-
ments. For instance, for an instrument with a cash flow (a1, a2), the 
measure (a1 + a2)/P0 would not be a useful measure of yield. In the first 
place, if we seek a measure that can be used to compare instruments of 
different maturities, it must measure return per unit of time. And sec-
ond, the proposed measure ignores the timing of receipts, thus failing to 
reflect the time value of money. 
The widely accepted solution to this problem is provided by a mea-
sure known as the yield to maturity. It is defined as the interest rate that 
makes the present value of the cash flow equal to the market value 
(price) of the instrument. Thus for the debt instrument in equation 
(20.3), the yield to maturity is the interest rate y that satisfies the fol-
lowing equation: 
= ---------------- + ------------------- + … + -------------------
(20.4)
nP0 
a1 
a2 
an 
(1 + y)
(1 + y)2 
(1 + y)n 
In general, the yield to maturity must be found by trial and error or 
by using an iterative technique like Newton-Raphson. If the debt instru-
ment is a bond, the cash flow (a1... an) can be written as (C, C, ..., C + 
M), where C is the coupon payment and M the maturity value. Equation 
(20.4) can be rewritten as 
C
C 
C
M
+
P = ---------------- + ------------------- + … + -------------------
(20.5) 
(1 + y)
(1 + y)2 
(1 + y)n 
After dividing both sides of equation (20.5) by M, to obtain the 
price per dollar of maturity value, and factoring C, we obtain 
n 
P
C 
1
1 
----- = ----- ∑ ------------------ + ------------------- 
(20.6) 
t
M 
Mt = 1 (1 + y)
(1 + y)n 
Recognizing that the summation on the right-hand side of equation 
(20.6) is the sum of a geometric progression, we can rewrite the equa-
tion as 

597 
Term Structure Modeling and Valuation of Bonds and Bond Options 
P
C 1 – (1 + y) –n 
1 
----- = ----- ------------------------------- + -------------------
(20.7) 
M
M 
y 
(1 + y)n 
The yield to maturity is the solution to equation (20.7) for y, the 
yield of an n-period bond. In equation (20.7) P/M is the so-called par 
value relation, usually expressed as a percentage. If it is equal to one, 
the bond sells “at par”; if it is larger than one, it sells at a “premium”; 
and if it is less than one, it sells at a “discount.” C/M is the coupon rate 
expressed as a ratio. 
So far we have not specified the unit of time for measuring the fre-
quencies with which interest is computed and the coupons are paid. 
Interest rates (and maturity) customarily are quoted per year (e.g., 7% 
per year), and we shall follow this convention; this means that in equa-
tion (20.7) it is implicitly assumed that the coupon rate is C per year 
and paid once a year. In fact, in the United States almost all bonds pay 
interest twice a year. Each coupon payment therefore amounts to C/2, 
which must be discounted twice a year at half the annual yield or y/2. 
As a result, equation (20.7) is changed to 
P
C 1 – (1 + y ⁄ 2) –2n 
1 
----- = -------- ----------------------------------------- + -----------------------------
(20.8) 
M 
2M
y ⁄ 2 
(1 + y ⁄ 2)2n 
To illustrate calculation of the yield to maturity of a bond with semi-
annual coupon payments, consider a 7%, 20-year bond with a maturity 
or par value of $100, and selling for 74.26%, or 74.26 cents per $1 of par 
value. The cash flow for this bond per dollar of par value is: 40 six-month 
payments of $0.035, and $1 received in 40 six-month periods from now. 
The present value at various semiannual interest rates (y/2) is: 
Interest rate (y/2): 
3.5% 
4.0% 
4.5% 
5.0% 
5.5% 
6.0% 
6.5% 
Present value (P/M): 1.0000 0.9010 0.8160 0.7426 0.6791 0.6238 0.5756 
When a 5.0% semiannual interest rate is used, the present value of the 
cash flows is equal to 0.7426 per $1 of par value, which is the price of 
the bond. Hence, 5.0% is the semiannual yield to maturity. 
The annual yield to maturity should, strictly speaking, be found by 
compounding 5.0% for one year. That is, it should be 10.25. But the con-
vention adopted by the bond market is to double y/2, the semiannual 
yield to maturity. Thus, the yield to maturity for the bond above is 10% 
(two times 5.0%). The yield to maturity computed using this convention 
of doubling the semiannual yield is called the bond equivalent yield. 

598 
The Mathematics of Financial Modeling and Investment Management 
Premium Par Yield 
In general, equation (20.7) and equation (20.8) cannot be solved explic-
itly for y (for n > 2); these equations must be solved by trial and error or 
by using an iterative technique—with one important exception. It is 
apparent from equation (20.7) that the par value, P/M, increases as the 
coupon rate, C/M, increases. Now consider a bond whose coupon rate is 
such that the corresponding value of P/M is one—that is, the bond sells 
at par. Then equation (20.7) becomes: 
C 1 – (1 + y) –n 
1
1 = ----- ------------------------------- + -------------------
(20.9) 
M
y 
(1 + y)n 
Equation (20.9) can be solved explicitly for y; the solution is y = C/ 
M. In other words, if a bond sells at par, its yield to maturity is the same 
as its coupon rate; for example, if a 7.75%, 20-year bond sells at par, its 
yield to maturity is 7.75%. This means that, for a bond to be issued at 
par, the coupon rate offered must be the same as the market-required 
yield for that maturity. The coupon rate of an n-period bond selling at 
par may be labeled the n-period par yield. 
It can also be verified from equation (20.9) that if the coupon rate 
on a bond is less than the required yield to maturity, or par yield, the 
bond will sell at a discount; the converse is true for a bond with a cou-
pon above par yield. The explanation for this relation is self-evident: if 
the cash payment per period—namely, the coupon is below the required 
yield per period, the difference must be made up by an increase in price, 
or capital gain, over the life of the bond. This requires that the price of 
the bond be lower than its maturity value. In the United States, bonds 
(other than zero-coupon bonds) customarily are issued with a yield to 
maturity as to insure that the issue sells at close to par. 
Reinvestment of Cash Flow and Yield 
The yield to maturity takes into account the coupon income and any 
capital gain or loss that the investor will realize by holding the bond to 
maturity. The measure has its shortcomings, however. We might think 
that if we acquire for P a bond of maturity n and yield y, then at matu-
rity we can count on obtaining a terminal value equal to P(1 + y)n. This 
inference is not justified. By multiplying both sides of equation (20.5) by 
(1 + y)n, we obtain 
P(1 + y)n = C(1 + y)n–1 + C(1 + y)n–2 + C + M 

599 
Term Structure Modeling and Valuation of Bonds and Bond Options 
For the terminal value to be P(1 + y)n, each of the coupon payments 
must be reinvested until maturity at an interest rate equal to the yield to 
maturity. If the coupon payment is semiannual, then each semiannual 
payment must be reinvested at the yield y. 
Clearly, as the equation indicates, the investor will realize the yield to 
maturity that is calculated at the time of purchase only if (1) all the cou-
pon payments can be reinvested at the yield to maturity, and (2) the bond 
is held to maturity. With respect to the first assumption, the risk that an 
investor faces is that future interest rates at which the coupon can be rein-
vested will be less than the yield to maturity at the time the bond is pur-
chased. This risk is referred to as reinvestment risk. And if the bond is not 
held to maturity, it may have to be sold for less than its purchase price, 
resulting in a return that is less than the yield to maturity. The risk that a 
bond will have to be sold at a loss is referred to as interest rate risk. 
Our focus in this section has been on coupon-bearing bonds. In the 
special case of a bond that produces only one cash flow, the maturity value, 
the yield to maturity does measure the rate at which the initial investment 
rises. We can see this if we substitute zero for the coupon payments in the 
last equation. As explained in Chapter 3, bonds that do not make coupon 
payments are called zero-coupon bonds. The advantage of these bonds is 
that they do not expose the investor to reinvestment risk. Zero-coupon 
bonds play a key role in the valuation process as explained later. 
THE TERM STRUCTURE OF THE INTEREST RATES AND THE 
YIELD CURVE 
The relationship between the yield on bonds of the same credit quality 
but different maturities is generically referred to as the term structure of 
interest rates. The graphical depiction of the term structure of interest 
rates is called the yield curve. 
There are different yield measures that can be used to construct the 
yield curve. As we will see in this chapter, the alternative yield measures 
that can be used are (1) the yield to maturity on a country’s benchmark 
government bonds; (2) the spot rate; (3) the forward rates; and (4) and 
the swap rate. We will explain the last three yield measures later in this 
chapter. Market participants typically construct yield curves from the 
market prices and yields in the government bond market of a country or 
from swap rates. As we will see, the other two rates—spot rates and for-
ward rates—are derived from market information. 
In the United States it is the U.S. Treasury securities market and the 
resulting yield curve is referred to as the Treasury yield curve. Two rea-

600 
The Mathematics of Financial Modeling and Investment Management 
sons account for this tendency. First, Treasury securities are free of 
default risk, and differences in creditworthiness do not affect yield esti-
mates. Second, the Treasury market offers the fewest problems of illi-
quidity or infrequent trading. 
Typically in constructing a yield curve using Treasury yields the on-
the-run Treasury issues are used. These are the most recently auctioned 
Treasury issues. In the United States, the U.S. Department of the Trea-
sury currently issues 3-month and 6-month Treasury bills and 2-year, 5-
year, and 10-year Treasury notes. Treasury bills are zero-coupon instru-
ments and Treasury notes are coupon-paying instruments. Hence, there 
are not many data points from which to construct a Treasury yield 
curve, particularly after two years. At one time, the U.S. Treasury issued 
30-year securities (referred to as Treasury bonds). However, the Trea-
sury stopped this practice. In constructing a Treasury yield curve, mar-
ket participants use the last issued Treasury bond (which has a maturity 
less than 30 years) to estimate the 30-year yield. The 2-year, 5-year, and 
10-year Treasury notes and an estimate of the 30-year Treasury bond is 
used to construct the Treasury yield curve. On September 5, 2003, Leh-
man Brothers reported the following values for these four yields: 
2 year 
1.71% 
5 year 
3.25% 
10 year 
4.35% 
30 year 
5.21% 
To fill in the yield for the 25 missing whole year maturities (3 year, 4 
year, 6 year, 7 year, 8 year, 9 year, 11 year, and so on to the 29-year matu-
rity), the yield for the 25 whole-year maturities are interpolated from the 
yield on the surrounding maturities. The simplest interpolation, and the 
one most commonly used in practice, is simple linear interpolation. 
For example, suppose that we want to fill in the gap for each one 
year of maturity. To determine the amount to add to the on-the-run 
Treasury yield as we go from the lower maturity to the higher maturity, 
the following formula is used: 
(yH  – yL)/N 
where: 
yH = yield at higher maturity 
yL = yield at lower maturity 
N = number of years between two observed maturity points 

601 
Term Structure Modeling and Valuation of Bonds and Bond Options 
The estimated on-the-run yield for all intermediate whole-year maturi-
ties is found by adding to the yield at the lower maturity the amount 
computed from the above formula. 
For example, using the September 5, 2003 yields, the 5-year yield is 
3.25% and the 10-year yield is the 4.35%% are used to obtain the 
interpolated 6-year, 7-year, 8-year, and 9-year yields by first calculating: 
(4.35% – 3.25%)/5 = 0.22% 
Then, 
interpolated 6-year yield = 3.25% + 0.22% = 3.47% 
interpolated 7-year yield = 3.47% + 0.22% = 3.69% 
interpolated 8-year yield = 3.69% + 0.22% = 3.91% 
interpolated 9-year yield = 3.91% + 0.22% = 4.13% 
Thus, when market participants talk about a yield on the Treasury 
yield curve that is not one of the on-the-run maturities—for example, 
the 8-year yield—it is only an approximation. Notice that there is a 
large gap between the maturity points. This may result in misleading 
yields for the interim maturity points when estimated using the linear 
interpolation method. 
Another factor complicates the relationship between maturity and 
Treasury yield in constructing the Treasury yield curve. The yield for 
on-the-run Treasury issues may be distorted by the fact that these secu-
rities can be financed at cheaper rates and as a result can offer a lower 
yield than in the absence of this financing advantage. There are inves-
tors who purchase securities with borrowed funds and use the securities 
purchased as collateral for the loan. This type of collateralized borrow-
ing is called a repurchase agreement. Since dealers, for whatever reason, 
want to obtain use of these securities for their own trading activities, 
they are willing to loan funds to investors at a lower interest rate than is 
otherwise available for borrowing in the market. Consequently, 
impounded into the price of an on-the-run Treasury security is the 
cheaper financing available, resulting in a lower yield for an on-the-run 
than would prevail in the absence of attractive financeability. 
From a practical viewpoint, the key function of the Treasury yield 
curve is to serve as a benchmark for pricing bonds and setting yields in all 
other sectors of the debt market—bank loans, mortgages, corporate debt, 
and international bonds. However, the Treasury yield curve is an unsatis-
factory measure of the relation between required yield and maturity. The 
key reason is that securities with the same maturity may actually carry 
different yields. This phenomenon reflects the role and impact of differ-

602 
The Mathematics of Financial Modeling and Investment Management 
ences in the bonds’ coupon rates. Hence, it is necessary to develop more 
accurate and reliable estimates of the term structure of interest rates. We 
will show how this is done later. Basically, the approach consists of identi-
fying yields that apply to zero-coupon bonds and, therefore, eliminates 
the problem of nonuniqueness in the yield-maturity relationship. 
Limitations of Using the Yield to Value a Bond 
The price of a bond is the present value of its cash flow. However, in our 
illustrations and our discussion of the pricing of a bond above, we assume 
that one interest rate should be used to discount all the bond’s cash flows. 
The appropriate interest rate is the yield on a Treasury security, with the 
same maturity as the bond, plus an appropriate risk premium or spread. 
To illustrate the problem with using the Treasury yield curve to deter-
mine the appropriate yield at which to discount the cash flow of a bond, 
consider the following two hypothetical 5-year Treasury bonds, A and B. 
The difference between these two Treasury bonds is the coupon rate, 
which is 12% for A and 3% for B. The cash flow for these two bonds per 
$100 of par value for the 10 six-month periods to maturity would be: 
Period 
Cash Flow for A 
Cash Flow for B 
1–9
 $6.00
 $1.50
 10 
106.00 
101.50 
Because of the different cash flow patterns, it is not appropriate to 
use the same interest rate to discount all cash flows. Instead, each cash 
flow should be discounted at a unique interest rate that is appropriate 
for the time period in which the cash flow will be received. But what 
should be the interest rate for each period? 
The correct way to think about bonds A and B in order to avoid arbi-
trage opportunities is not as bonds but as packages of cash flows. More 
specifically, they are packages of zero-coupon instruments. Thus, the 
interest earned is the difference between the maturity value and the price 
paid. For example, bond A can be viewed as 10 zero-coupon instru-
ments: one with a maturity value of $6 maturing six months from now; a 
second with a maturity value of $6 maturing one year from now; a third 
with a maturity value of $6 maturing 1.5 years from now, and so on. The 
final zero-coupon instrument matures 10 six-month periods from now 
and has a maturity value of $106. Likewise, bond B can be viewed as 10 
zero-coupon instruments: one with a maturity value of $1.50 maturing 
six months from now; one with a maturity value of $1.50 maturing one 
year from now; one with a maturity value of $1.50 maturing 1.5 years 
from now, and so on. The final zero-coupon instrument matures 10 six-

603 
Term Structure Modeling and Valuation of Bonds and Bond Options 
month periods from now and has a maturity value of $101.50. Obvi-
ously, in the case of each coupon bond, the value or price of the bond is 
equal to the total value of its component zero-coupon instruments. 
Valuing a Bond as a Package of Cash Flows 
In general, any bond can be viewed as a package of zero-coupon instru-
ments. That is, each zero-coupon instrument in the package has a maturity 
equal to its coupon payment date or, in the case of the principal, the matu-
rity date. The value of the bond should equal the value of all the compo-
nent zero-coupon instruments. If this does not hold, it is possible for a 
market participant to generate riskless profits by stripping the security and 
creating stripped securities. We will demonstrate this later in this chapter. 
To determine the value of each zero-coupon instrument, it is neces-
sary to know the yield on a zero-coupon Treasury with that same matu-
rity that we referred to as the spot rate earlier. The spot rate curve is the 
graphical depiction of the relationship between the spot rate and its 
maturity. Because there are no zero-coupon Treasury debt issues with a 
maturity greater than one year issued by the U.S. Department of the 
Treasury, it is not possible to construct such a curve solely from obser-
vations of market activity. Rather, it is necessary to derive this curve 
from theoretical considerations as applied to the yields of actual Trea-
sury securities. Such a curve is called a theoretical spot rate curve. 
Obtaining Spot Rates from the Treasury Yield Curve 
We will now explain the process of creating a theoretical spot rate curve 
from the yield curve that is based on the observed yields of Treasury 
securities. The process involves the following: 
1. Select the universe of Treasury securities to be used to construct the 
theoretical spot rates. 
2. Obtain the theoretical spot rates using bootstrapping. 
3. Create a smooth continuous curve. 
We will return to the first and the third tasks later in this chapter. For 
now, we want to show how the theoretical spot rates can be obtained 
from the interpolated yields on Treasury securities (i.e., the Treasury yield 
curve). To simplify the illustration, we will assume that an estimated 
Treasury yield curve is as shown in Exhibit 20.1. The 6-month and 1-year 
Treasury securities are assumed to be zero-coupon Treasury securities. 
The process of extracting the theoretical spot rates from the Trea-
sury yield curve is called bootstrapping. To explain this process, we use 
the data for the price, annualized yield (yield to maturity), and maturity 

604 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 20.1 
Hypothetical Treasury Yields (Interpolated) 
Annual Par Yield to 
Spot Rate 
Period 
Years 
Maturity (BEY) (%)a 
Price 
(BEY) (%)a
 1
 0.5 
3.00 
— 
3.0000
 2
 1.0 
3.30 
— 
3.3000
 3
 1.5 
3.50 
100.00 
3.5053
 4
 2.0 
3.90 
100.00 
3.9164
 5
 2.5 
4.40 
100.00 
4.4376
 6
 3.0 
4.70 
100.00 
4.7520
 7
 3.5 
4.90 
100.00 
4.9622
 8
 4.0 
5.00 
100.00 
5.0650
 9
 4.5 
5.10 
100.00 
5.1701 
10
 5.0 
5.20 
100.00 
5.2772 
11
 5.5 
5.30 
100.00 
5.3864 
12
 6.0 
5.40 
100.00 
5.4976 
13
 6.5 
5.50 
100.00 
5.6108 
14
 7.0 
5.55 
100.00 
5.6643 
15
 7.5 
5.60 
100.00 
5.7193 
16
 8.0 
5.65 
100.00 
5.7755 
17
 8.5 
5.70 
100.00 
5.8331 
18
 9.0 
5.80 
100.00 
5.9584 
19
 9.5 
5.90 
100.00 
6.0863 
20 
10.0 
6.00 
100.00 
6.2169 
a The yield to maturity and the spot rate are annual rates. They are reported as bond-
equivalent yields. To obtain the semiannual yield or rate, one half the annual yield 
or annual rate is used. 
of the 20 hypothetical Treasury securities shown in Exhibit 20.1. The 
basic principle of bootstrapping is that the value of the Treasury secu-
rity should be equal to the value of the package of zero-coupon Trea-
sury securities that duplicates the coupon bond’s cash flow. 
Consider the 6-month and 1-year Treasury securities in Exhibit 
20.1. These securities are assumed to be zero-coupon instruments.
Therefore, their annualized yield of 3% and 3.3% are respectively the 6-
month spot and the rate 1-year spot rate. Given these two spot rates, we 
can compute the spot rate for a theoretical 1.5-year zero-coupon Trea-
sury. The price of a theoretical 1.5-year Treasury should equal the 
present value of three cash flows from an actual 1.5-year coupon Trea-
sury, where the yield used for discounting is the spot rate corresponding 

605 
Term Structure Modeling and Valuation of Bonds and Bond Options 
to the cash flow. Using $100 as par, the cash flow for the 1.5-year cou-
pon Treasury is $1.75 for the first two 6-month periods and $101.75 in 
1.5 years when the bond matures. Letting zt represent one-half the 
annualized spot rate for period t, then the absence of arbitrage requires 
that the present value of the three cash flows when discounted at the 
spot rates equal the market price, $100 in our illustration. That is, 
1.75 
1.75 
101.75 
---------------------- + ---------------------- + ---------------------- = 100 
(1 + z1)1 
(1 + z2)2 
(1 + z3)3 
Since the 6-month spot rate and 1-year spot rate are 3.0% and 
3.3%, respectively, we know that: z1 = 0.015 and z2 = 0.0165. Substi-
tuting these spot rates into the above equation and solving for z3, we 
obtain 1.7527%. Doubling this yield, we obtain the bond-equivalent 
yield of 3.5053%, which is the theoretical 1.5-year spot rate. That rate 
is the spot rate that the market would apply to a 1.5-year zero-coupon 
Treasury security if, in fact, such a security existed. 
Given the theoretical 1.5-year spot rate, we can obtain the theoreti-
cal 2-year spot rate. The cash flows for the 2-year coupon Treasury 
security follows from Exhibit 20.1. Since the annual coupon rate is 
3.9%, the cash flow for the first three periods is $1.95 and the cash flow 
for the fourth period is $101.95. Given the spot rate for the first three 
periods (z1 = 0.015, z2 = 0.0165, and z3 = 0.017527), the 4-period spot 
rate is then found by solving the following equation: 
1.95 
1.95 
1.95 
101.95 
---------------------- + ------------------------- + -------------------------------- + ---------------------- = 100 
(1.015)1 
(1.0165)2 
(1.017527)3 
(1 + z4)4 
The value for z4 is 0.019582 or 1.9582%. Doubling this yield, we obtain 
the theoretical 2-year spot rate bond-equivalent yield of 3.9164%. 
One can follow this approach sequentially to derive the theoretical 
2.5-year spot rate from the calculated values of z1, z2, z3, and z4, and the 
price and coupon of the 2.5-year bond in Exhibit 20.1. Further, one 
could derive theoretical spot rates for the remaining 15 half-yearly rates. 
The spot rates thus obtained are shown in the last column of 
Exhibit 20.1. They represent the term structure of Treasury spot rates 
for maturities up to 10 years. 
In practice, yields for interim maturities are not readily available for 
government bond markets. Hence, to construct a continuous spot rate 
curve requires the use of a methodology described later in this chapter. 

606 
The Mathematics of Financial Modeling and Investment Management 
Using Spot Rates to the Arbitrage-Free Value of a Bond 
Finance theory tells us that the theoretical price of a Treasury security 
should be equal to the present value of the cash flow where each cash 
flow is discounted at the appropriate theoretical spot rate For example, 
if the Treasury spot rates shown in the last column of Exhibit 20.1 are 
used to compute the arbitrage-free value of an 8% 10-year Treasury 
security, the present value of the cash flow would be found to be 
$115.2619. If a 4.8% coupon 10-year Treasury bond is being valued 
based on the Treasury spot rates shown in Exhibit 20.1, the arbitrage-
free value is $90.8428. 
Suppose that the 8% coupon, 10-year Treasury issue is valued using 
the traditional approach based on 6% (i.e., the yield on a 10-year Trea-
sury coupon bond shown in Exhibit 20.1). Discounting all cash flows at 
6% would produce a value for the 8% coupon bond of $114.8775. Con-
sider what would happen if the market priced the security at $114.8775. 
The value based on the Treasury spot rates is $115.2619. Faced with this 
situation, a securities dealer can buy the 8% 10-year issue for $114.8775, 
strip off each coupon payment and the maturity value, and sell each cash 
flow in the market at the spot rates shown in Exhibit 20.1. By doing so, 
the proceeds that will be received by the dealer are $115.2619. This 
results in an arbitrage profit of $0.3844 (= $115.2619 – $114.8775). 
Securities dealers recognizing this arbitrage opportunity will bid up the 
price of the 8% 10-year Treasury issue in order to acquire it and strip it. 
Once the price is up to around $115.2619 (the arbitrage-free value), the 
arbitrage opportunity is eliminated. 
We have just demonstrated how stripping of a Treasury issue will 
force the market value to be close to its arbitrage-free value when the 
market price is less than the arbitrage-free value. When a Treasury issue’s 
market price is greater than the arbitrage-free value, a securities dealer 
can capture the arbitrage value by a process referred to as reconstitution. 
Basically, the securities dealer can purchase a package of stripped Trea-
sury securities traded in the market so as to create a synthetic Treasury 
coupon security that is worth more than the same maturity and the same 
coupon Treasury issue. The sale of the resulting synthetic coupon security 
that is created will force the price down to its arbitrage-free value. 
The Discount Function 
A more convenient way of characterizing the term structure of interest rates 
is by means of the discount function. The discount function specifies the 
present value of a cash flow in the future. It can therefore be interpreted as 
the price of a pure risk-free discount bond of a given maturity with a $1 
face value. The discount function (Dn) is related to spot rates as follows: 

607 
Term Structure Modeling and Valuation of Bonds and Bond Options 
1
D
= ----------------------
n 
(1 + z )n 
n 
The reason for describing the term structure in terms of the discount 
function is that bond prices can be expressed in an easy way in terms of 
it. The price of a bond is simply the sum of the products of the cash flow 
expected from the bond at time t and the discount function for time t. 
That is, for a bond with a maturity n and a cash flow of C for periods 
1,…,n–1 and maturity value of M, the price is 
n – 1 
∑ DtC
D (C
M)
+
+
n 
t – 1 
Forward Rates 
In addition to spot rates and discount functions to describe the term 
structure, there is another important analytical concept that can be used 
to describe the term structure: forward rates. Forward rates can be 
derived from the Treasury yield curve by using arbitrage arguments, just 
as we did for spot rates. 
To illustrate the process of obtaining 6-month forward rates, we will 
use the yield curve and corresponding spot rate curve from Exhibit 20.1. 
For this construction, we will use a very simple arbitrage: If two invest-
ments have the same cash flows and have the same risk, they should have 
the same value. 
Consider an investor who has a 1-year investment horizon and is 
faced with the following two alternatives:
 ■ Alternative 1. Buy a 1-year Treasury security
 ■ Alternative 2. Buy a 6-month Treasury security and, when it matures in 
six months, buy another 6-month Treasury security 
The investor will be indifferent toward the two alternatives if they 
produce the same return over the 1-year investment horizon. The investor 
knows the spot rate on the 6-month Treasury security and the 1-year 
Treasury security. However, he does not know what yield will be available 
on a 6-month Treasury security that will be purchased six months from 
now. That is, he does not know the 6-month forward rate six months 
from now. Given the spot rates for the 6-month Treasury security and the 
1-year Treasury security, the forward rate on a 6-month Treasury security 
is the rate that equalizes the dollar return between the two alternatives. 

608 
The Mathematics of Financial Modeling and Investment Management 
Letting $X denote the face amount of the 6-month Treasury security, z1 is 
one-half the bond-equivalent yield (BEY) of the theoretical 6-month spot 
rate, and z2 represents one-half the BEY of the theoretical 1-year spot 
rate, then the investor will be indifferent toward the two alternatives if 
X(1 + z1)(1 + f) = X(1 + z2)2 
where f is the 6-month forward rate six months from now. Solving, we get 
(1 + z2)2 
f = ---------------------- – 1 
(1 + z1) 
Doubling f gives the BEY for the 6-month forward rate six months 
from now. In our illustration, f is 1.8% and therefore the 6-month for-
ward rate on a BEY basis is 3.6%. 
We can generalize the 1-period forward rates as follows.2 Let fn 
denote the 1-period forward rate contract that will begin at time n. 
Then f0 is simply the current 1-period spot rate. 
Exhibit 20.2 shows all of the 6-month (i.e., 1-period) forward rates 
for the Treasury yield curve and corresponding spot rate curve shown in 
Exhibit 20.1. The forward rates reported in Exhibit 20.2 are the annual-
ized rates on a bond-equivalent basis. The set of these forward rates is 
called the short-term forward-rate curve. 
The relationship between the n-period spot rate, the current 6-
month spot rate, and the 6-month forward rates is as follows: 
zn = [(1 + z1) (1 + f1) (1 + f2) ... (1 + fn–1)]1/n – 1 
The discount function can be expressed in terms of forward rates as 
follows: 
1
D
= --------------------------------------------------------------------------------------------------------------------
n 
[(1 + z1)(1 + f1)(1 + f2)…(1 + 1fn – 1)]1 ⁄ n – 1 
Swap Curve 
Instead of using a government spot rate curve, market participants are 
more often using the swap curve or London Interbank Offered Rate 
(LIBOR) curve for reasons described below. A swap curve is derived 
2 We will generalize the notation later in this chapter when continuous time is used. 

609 
Term Structure Modeling and Valuation of Bonds and Bond Options 
EXHIBIT 20.2 
Short-Term Forward Rates 
Notation 
Forward Rate
 1f0 
3.00
 1f1 
3.60
 1f2 
3.92
 1f3 
5.15
 1f4 
6.54
 1f5 
6.33
 1f6 
6.23
 1f7 
5.79
 1f8 
6.01
 1f9 
6.24 
1f10 
6.48 
1f11 
6.72 
1f12 
6.97 
1f13 
6.36 
1f14 
6.49 
1f15 
6.62 
1f16 
6.76 
1f17 
8.10 
1f18 
8.40 
1f19 
8.72 
from observed swap rates in the interest rate swap market. In a generic 
interest rate swap two parties agree to exchange cash flows based on a 
notional amount where (1) one party pays a fixed rate and receives a 
floating rate and (2) the other party agrees to pay a floating rate and 
receives a fixed rate. The fixed rate is called the swap rate. A swap curve 
can be constructed that is unique to a country where there is a swap 
market for converting fixed cash flows to floating cash flows in that 
country’s currency. 
Typically, the reference rate for the floating rate is 3-month LIBOR. 
Effectively, the swap curve indicates the fixed rate (i.e., swap rate) that a 
party must pay to lock in 3-month LIBOR for a specified future period. 
By locking in 3-month LIBOR it is meant that a party that pays the 
floating rate (i.e., agrees to pay 3-month LIBOR) is locking in a borrow-
ing rate; the party receiving the floating rate is locking in an amount to 
be received. Because 3-month LIBOR is being exchanged, the swap 
curve is also called the LIBOR curve. 

610 
The Mathematics of Financial Modeling and Investment Management 
The convention in the swap market is to quote the reference rate flat 
(i.e., no spread) and quote the fixed-rate side as a spread over a bench-
mark (typically the yield on a government bond) with the same maturity 
as the swap. 
Effectively the swap rate reflects the risk of the counterparty to the 
swap failing to satisfy its obligation. Consequently, the swap curve does 
not reflect rates for a default-free obligation. Instead, the swap curve 
reflects credit risk. Since the counterparty in swaps are typically bank-
related entities, the swap curve reflects the credit risk of the banking sec-
tor—effectively, it is an interbank or AA rated curve. 
Investors and issuers use the swap market for hedging and arbitrage 
purposes, and the swap curve as a benchmark for evaluating performance 
of fixed-income securities and the pricing of fixed-income securities. Since 
the swap curve is effectively the LIBOR curve and investors borrow based 
on LIBOR, the swap curve is more useful to funded investors than a gov-
ernment yield curve. 
The increased application of the swap curve for these activities is 
due to its advantages over using the government bond yield curve as a 
benchmark. Before identifying these advantages, it is important to 
understand that the drawback of the swap curve relative to the govern-
ment bond yield curve could be poorer liquidity. In such instances, the 
swap rates would reflect a liquidity premium. Fortunately, liquidity is 
not an issue in many countries as the swap market has become highly 
liquid, with narrow bid-ask spreads for a wide range of swap maturities. 
In some countries swaps may offer better liquidity than that country’s 
government bond market. The advantages of the swap curve over a gov-
ernment bond yield curve are:3 
1. There is almost no government regulation of the swap market. The 
lack of government regulation makes swap rates across different 
markets more comparable. In some countries, there are some sover-
eign issues that offer various tax benefits to investors and, as a 
result, for global investors it makes comparative analysis of govern-
ment rates across countries difficult because some market yields do 
not reflect their true yield. 
2. The supply of swaps depends only on the number of counterparties 
that are seeking or are willing to enter into a swap transaction at 
any given time. Since there is no underlying government bond, there 
3 See Uri Ron, “A Practical Guide to Swap Curve Construction,” Chapter 6 in Frank 
J. Fabozzi (ed.), Interest Rate, Term Structure, and Valuation Modeling (New York: 
John Wiley & Sons, 2002). 

611 
Term Structure Modeling and Valuation of Bonds and Bond Options 
can be no effect of market technical factors that may result in the 
yield for a government bond issue being less than its true yield.4 
3. Comparisons across countries of government yield curves is difficult 
because of the differences in sovereign credit risk. In contrast, the 
credit risk as reflected in the swaps curve are similar and make com-
parisons across countries more meaningful than government yield 
curves. Sovereign risk is not present in the swap curve because, as 
noted earlier, the swap curve is viewed as an interbank yield curve 
or AA yield curve. 
4. There are more maturity points available to construct a swap curve 
than a government bond yield curve. More specifically, what is 
quoted daily in the swap market are swap rates for 2-, 3-, 4-, 5-, 6-, 
7-, 8-, 9-, 10-, 15-, and 30-year maturities. Thus, in the swap mar-
ket there are 10 market interest rates with a maturity of two years 
and greater. In contrast, in the U.S. Treasury market, for example, 
there are only three market interest rates for on-the-run Treasuries 
with a maturity of two years or greater (2, 5, and 10 years) and one 
of the rates, the 10-year rate, may not be a good benchmark because 
it is often on special in the repo market. Moreover, because the U.S. 
Treasury has ceased the issuance of 30-year bonds, there is no 30-
year yield available. 
In the valuation of fixed-income securities, it is not the Treasury 
yield curve that is used as the basis for determining the appropriate dis-
count rate for computing the present value of cash flows but the Trea-
sury spot rates. The Treasury spot rates are derived from the Treasury 
yield curve using the bootstrapping process. Similarly, it is not the swap 
curve that is used to for discounting cash flows when the swap curve is 
the benchmark but the corresponding spot rates. The spot rates are 
derived from the swap curve in exactly the same way—using the boot-
strapping methodology. The resulting spot rate curve is called the 
LIBOR spot rate curve. Moreover, a forward rate curve can be derived 
from the spot rate curve. The same thing is done in the swap market. 
The forward rate curve that is derived is called the LIBOR forward rate 
curve. 
Consequently, if we understand the mechanics of moving from the 
yield curve to the spot rate curve to the forward rate curve in the Trea-
sury market, there is no reason to repeat an explanation of that process 
here for the swap market; that is, it is the same methodology, just differ-
ent yields are used. 
4 For example, a government bond issue being on “special” in the repurchase agree-
ment market. 

612 
The Mathematics of Financial Modeling and Investment Management 
CLASSICAL ECONOMIC THEORIES ABOUT THE 
DETERMINANTS OF THE SHAPE OF THE TERM STRUCTURE 
As mentioned earlier, the Treasury yield curve shows the relationship 
between the yield to maturity on Treasury securities and maturity. His-
torically, three shapes have been observed: an upward sloping yield 
curve (the most typical and therefore referred to as a “normal” yield 
curve), an downward sloping yield curve (also referred to as an 
“inverted” yield curve), and a flat yield curve. Exhibit 20.3 shows the 
yield curve for four countries on September 5, 2003 and September 12, 
2003: United States, Germany, United Kingdom, and Japan. Notice that 
all four yield curves are upward sloping. 
While we know that the yield curve is not the same as the term struc-
ture of interest rates, what will the shape of the spot rate curve and short-
term forward rate curve look like? If the yield curve is upward sloping, the 
spot rate curve will lie above the yield curve, and the forward rate curve 
EXHIBIT 20.3 
Global Bellwether Yield Curves, September 5, 2003 and 
September 12, 2003 

Term Structure Modeling and Valuation of Bonds and Bond Options 
613 
EXHIBIT 20.3
 (Continued) 
Yields (%) 
2-Yr 
5-Yr 
10-Yr 
30-Yr 
United 
States 
9/5/03 
1.71 
3.25 
4.35 
5.21 
9/12/03 
1.62 
3.15 
4.26 
5.17 
W-o-W Chg (bp) 
–9 
–10 
–9 
–4 
Germany 
9/5/03 
2.60 
3.54 
4.30 
4.98 
9/12/03 
2.44 
3.36 
4.17 
4.90 
W-o-w Chg (bp) 
–16 
–18 
–13 
–8 
United 
Kingdom 
9/5/03 
4.16 
4.46 
4.69 
4.77 
9/12/03 
4.05 
4.36 
4.57 
4.69 
W-o-w Chg (bp) 
–11 
–10 
–12 
–8 
Japan 
9/5/03 
0.19 
0.74 
1.44 
1.79 
9/12/03 
0.20 
0.73 
1.54 
1.98 
W-o-w Chg (bp) 
1 
–1 
10 
19 
Source: Lehman Brothers, “Global Relative Value,” Fixed Income Research, Sep-
tember 8, 2003, p. 13. 
will lie above the spot rate curve. The reverse is true if the yield curve is 
downward sloping. If the yield curve is flat, all three curves are flat. 
Two major economic theories have evolved to account for these 
observed shapes of the yield curve: expectations theories and market 
segmentation theory. We describe these theories below. However, these 
are qualitative theories that tend to explain general features of market 
behavior. The quantitative determination of interest rates is a major 
problem of macroeconomics; it is made particularly challenging by the 
fact that interest rates are influenced by both market forces and by the 
decisions of central banks. In principle, General Equilibrium Theories 
(GET) can determine interest rates endogenously. However, GET remain 
an abstract tool; it is virtually impossible to apply them to practical 
forecasting. In practice, the forecast of interest rates for bond and bond 
option valuation is made using econometric models. Later in this chap-
ter we will take a look at the structure and form of econometric models 
used to forecast interest rates, or represent their stochastic evolution. 
Expectations Theories 
There are several forms of the expectations theory: pure expectations 
theory, liquidity theory, and preferred habitat theory. Expectations theo-
ries share a hypothesis about the behavior of short-term forward rates 

614 
The Mathematics of Financial Modeling and Investment Management 
and also assume that the forward rates in current long-term bonds are 
closely related to the market’s expectations about future short-term 
rates. These three expectations theories differ, however, as to whether 
other factors also affect forward rates, and how. The pure expectations 
theory postulates that no systematic factors other than expected future 
short-term rates affect forward rates; the liquidity theory and the pre-
ferred habitat theory assert that there are other factors. Accordingly, the 
last two forms of the expectations theory are sometimes referred to as 
biased expectations theories. 
Pure Expectations Theory 
According to the pure expectations theory, the forward rates exclusively 
represent the expected future spot rates. Thus the entire term structure at a 
given time reflects the market’s current expectations of the family of future 
short-term rates. Under this view, a rising term structure must indicate 
that the market expects short-term rates to rise throughout the relevant 
future. Similarly, a flat term structure reflects an expectation that future 
short-term rates will be mostly constant, and a falling term structure must 
reflect an expectation that future short rates will decline steadily. 
We can illustrate this theory by considering how the expectation of 
a rising short-term future rate would affect the behavior of various mar-
ket participants so as to result in a rising yield curve. Assume an initially 
flat term structure, and suppose that subsequent economic news leads 
market participants to expect interest rates to rise. 
1. Those market participants interested in long-term bonds would not 
want to buy long-term bonds because they would expect the yield 
structure to rise sooner or later, resulting in a price decline for the 
bonds and a capital loss on the long-term bonds purchased. Instead, 
they would want to invest in short-term debt obligations until the rise 
in yield had occurred, permitting them to reinvest their funds at the 
higher yield. 
2. Speculators expecting rising rates would anticipate a decline in the 
price of long-term bonds and therefore would want to sell any long-
term bonds they own and possibly to “short sell” some they do not 
own. (Should interest rates rise as expected, the price of longer-term 
bonds will fall. Because the speculator sold these bonds short and can 
then purchase them at a lower price to cover the short sale, a profit will 
be earned.) Speculators will reinvest in short-term bonds. 
3. Borrowers wishing to acquire long-term funds would be pulled toward 
borrowing now in the long end of the market by the expectation that 
borrowing at a later time would be more expensive. 

615 
Term Structure Modeling and Valuation of Bonds and Bond Options 
All these responses would tend either to lower the net demand for, 
or to increase the supply of, long-maturity bonds, and all three 
responses would increase demand for short-term bonds. This would 
require a rise in long-term yields in relation to short-term yields; that is, 
these actions by investors, speculators, and borrowers would tilt the 
term structure upward until it is consistent with expectations of higher 
future interest rates. By analogous reasoning, an unexpected event lead-
ing to the expectation of lower future rates will result in the yield curve 
sloping downward. 
Unfortunately, the pure expectations theory suffers from one short-
coming, which, qualitatively, is quite serious. It neglects the risks inher-
ent in investing in bonds. If forward rates were perfect predictors of 
future interest rates, the future prices of bonds would be known with 
certainty. The return over any investment period would be certain and 
independent of the maturity of the instrument initially acquired and of 
the time at which the investor needed to liquidate the instrument. How-
ever, with uncertainty about future interest rates and hence about future 
prices of bonds, these instruments become risky investments in the sense 
that the return over some investment horizon is unknown. 
There are two risks that cause uncertainty about the return over some 
investment horizon: interest rate risk and reinvestment risk. Interest rate 
risk is the uncertainty about the price of the bond at the end of the invest-
ment horizon. For example, an investor who plans to invest for five years 
might consider the following three investment alternatives: (1) invest in a 
5-year bond and hold it for five years; (2) invest in a 12-year bond and sell 
it at the end of five years; and (3) invest in a 30-year bond and sell it at the 
end of five years. The return that will be realized for the second and third 
alternatives is not known because the price of each long-term bond at the 
end of five years is not known. In the case of the 12-year bond, the price 
will depend on the yield on 7-year debt securities five years from now; and 
the price of the 30-year bond will depend on the yield on 25-year bonds 
five years from now. Because forward rates implied in the current term 
structure for a future 12-year bond and a future 25-year bond are not per-
fect predictors of the actual future rates, there is uncertainty about the 
price for both bonds five years from now. Thus there is interest rate risk; 
that is, the risk that the price of the bond will be lower than currently 
expected at the end of the investment horizon. An important feature of 
interest rate risk is that it is greater the longer the maturity of the bond. 
The second risk has to do with the uncertainty about the rate at 
which the proceeds from a bond can be reinvested until the expected 
maturity date. This risk is referred to as reinvestment risk. For example, 
an investor who plans to invest for five years might consider the follow-
ing three alternative investments: (1) invest in a 5-year bond and hold it 

616 
The Mathematics of Financial Modeling and Investment Management 
for five years; (2) invest in a 6-month instrument and when it matures, 
reinvest the proceeds in six-month instruments over the entire 5-year 
investment horizon; and (3) invest in a 2-year bond and when it matures, 
reinvest the proceeds in a 3-year bond. The risk in the second and third 
alternatives is that the return over the 5-year investment horizon is 
unknown because rates at which the proceeds can be reinvested until 
maturity are unknown. 
As noted by John Cox, Jonathan Ingersoll, and Stephen Ross, in 
practice, there are at least five variants of the pure expectations theory 
that have been put forth in the financial literature.5 
1. Globally equal expected-holding-period return theory 
2. Local expectations theory 
3. Unbiased expectations theory 
4. Return-to-maturity expectations theory 
5. Yield-to-maturity theory6 
The globally expected-holding-period return theory asserts that the 
expected return for a given holding period is the same regardless of the 
maturity of the bonds held. So, for example, an investor who has a 
holding period of three years is expected to have the same 5-year return 
whether the investor (1) purchased a 1-year bond today and when it 
matures reinvests the proceeds in a 4-year bond; (2) purchased a 2-year 
bond today and when it matures reinvest the proceeds in a 3-year bond; 
or (3) purchased a 10-year bond and sold it at the end of three years. 
The globally expected-holding-period return theory is the broadest 
interpretation of the pure expectations theory. 
The second variant of the pure expectations theory, the local expec-
tations theory, is more restrictive about the relevant holding period for 
which the returns are expected to be equal. It is restricted to short-term 
holding periods that begin today. An investor with a 6-month holding 
period, for example, would have the same expected return if (1) a 6-
month bond is purchased today; (2) a 3-year bond is purchased today; 
or (3) a 20-year bond is purchased today. 
The unbiased expectations theory asserts that the spot rates that the 
market expects in the future are equal to today’s the forward rates. 
5 John Cox, Jonathan Ingersoll, and Stephen Ross, “A Re-examination of Tradition-
al Hypotheses about the Term Structure of Interest Rates,” Journal of Finance (Sep-
tember 1981), pp. 769–799. 
6 The labels for the last four variants of the pure expectations theory are those given 
by Cox, Ingersoll, and Ross. The first label is given by McEnally and Jordan, “The 
Term Structure of Interest Rates,” p. 829. 

617 
Term Structure Modeling and Valuation of Bonds and Bond Options 
Thus, the forward rates are viewed as the market’s consensus of future 
interest rates. The return-to-maturity theory asserts that the return that 
can be realized if a zero-coupon bond is held to maturity is the same 
return expected by following a strategy of buying shorter term maturity 
bonds and reinvesting them until the maturity of the zero-coupon bond. 
For example, if an investor purchases a 5-year zero-coupon bond, then 
the known return from holding that bond to maturity is the same as the 
expected return from buying a 6-month bond today and reinvesting the 
proceeds when it matures in another six-month bond and then continu-
ing to reinvest in six-month instruments until the end of the fifth year. 
The yield-to-maturity theory asserts the same as in the return-to-matu-
rity theory except that this variant of the pure expectations theory is in 
terms of periodic returns. 
As Cox, Ingersoll, and Ross have demonstrated, these interpreta-
tions are not exact equivalents nor are they consistent with each other, 
in large part because they offer different treatments of the two risks 
associated with realizing a return (i.e., interest rate risk and reinvest-
ment risk). Furthermore, Cox, Ingersoll, and Ross showed that only one 
of the five variants of the pure expectations theory is consistent with 
equilibrium: the local expectations theory. 
Liquidity Theory 
We have explained that the drawback of the pure expectations theory is 
that it does not consider the risks associated with investing in bonds. 
Nonetheless, there is indeed risk in holding a long-term bond for one 
period, and that risk increases with the bond’s maturity because matu-
rity and price volatility are directly related. Given this uncertainty, and 
the reasonable consideration that investors typically do not like uncer-
tainty, some economists and financial analysts have suggested a different 
theory. This theory states that investors will hold longer-term maturities 
if they are offered a long-term rate higher than the average of expected 
future rates by a risk premium that is positively related to the term to 
maturity. Put differently, the forward rates should reflect both interest 
rate expectations and a “liquidity” premium (really a risk premium), 
and the premium should be higher for longer maturities. 
According to this theory, which is called the liquidity theory of the 
term structure, the implied forward rates will not be an unbiased esti-
mate of the market’s expectations of future interest rates because they 
embody a liquidity premium. Thus, an upward-sloping yield curve may 
reflect expectations that future interest rates either (1) will rise, or (2) 
will be flat or even fall, but with a liquidity premium increasing fast 
enough with maturity so as to produce an upward-sloping yield curve. 

618 
The Mathematics of Financial Modeling and Investment Management 
Preferred Habitat Theory 
Another theory, known as the preferred habitat theory, also adopts the 
view that the term structure reflects the expectation of the future path of 
interest rates as well as a risk premium. However, the preferred habitat 
theory rejects the assertion that the risk premium must rise uniformly 
with maturity. Proponents of the preferred habitat theory say that the 
latter conclusion could be accepted if all investors intend to liquidate 
their investment at the shortest possible date while all borrowers are 
anxious to borrow long. This assumption can be rejected since institu-
tions have holding periods dictated by the nature of their liabilities. 
The preferred habitat theory asserts that, to the extent that the 
demand and supply of funds in a given maturity range do not match, 
some lenders and borrowers will be induced to shift to maturities show-
ing the opposite imbalances. However, they will need to be compensated 
by an appropriate risk premium whose magnitude will reflect the extent 
of aversion to either price or reinvestment risk. Thus, this theory pro-
poses that the shape of the yield curve is determined by both expecta-
tions of future interest rates and a risk premium, positive or negative, to 
induce market participants to shift out of their preferred habitat. 
Clearly, according to this theory, yield curves sloping up, down, flat, or 
humped are all possible. 
Market Segmentation Theory 
The market segmentation theory also recognizes that investors have pre-
ferred habitats dictated by the nature of their liabilities. This theory also 
proposes that the major reason for the shape of the yield curve lies in 
asset/liability management constraints (either regulatory or self-imposed) 
and/or creditors (borrowers) restricting their lending (financing) to spe-
cific maturity sectors. However, the market segmentation theory differs 
from the preferred habitat theory in that it assumes that neither investors 
nor borrowers are willing to shift from one maturity sector to another to 
take advantage of opportunities arising from differences between expec-
tations and forward rates. Thus, for the segmentation theory, the shape 
of the yield curve is determined by supply of and demand for securities 
within each maturity sector. 
BOND VALUATION FORMULAS IN CONTINUOUS TIME 
Recall that the price of a coupon-paying bond can be expressed as the 
price of a package of cash flows as follows: 

619 
Term Structure Modeling and Valuation of Bonds and Bond Options 
C
C 
C
M
+
P = ---------------------- + ---------------------- + … + ------------------------
(1 + z1)1 
(1 + z2)2 
(1 + zN)N 
where zi is the spot rate relative to the i-th period. The coefficients 
1
Di = -------------------
(1 + zi)i 
are called the discount function or discount factors. 
In continuous time, as it will be demonstrated in the below, if short-
term interest rates are constant, the bond valuation formula is 
C
C 
C
M
+
P = ---------- + ---------- + … + ---------------
1 × i 
2 × i 
N
i
× 
e
e 
e 
If short-term rates are variable, the formula is: 
–∫
1 ( ) s
d 
–∫
2i s  
( ) s
d 
i s
( ) s
d 
–∫
Ni s
+
P = Ce
 
0 
+ Ce 
0 
+ … + (C
M)e 
0 
To consider bond valuation in continuous time, we will use many 
relationships related to yield and interest rates in a stochastic environ-
ment. We begin by explicitly computing a number of these relationships 
in a deterministic environment (that is, assuming that interest rates are a 
known function of time) then extending these relationships to a stochas-
tic environment. 
In the case of a zero-coupon bond, the financial principles of valua-
tion are those illustrated earlier when we considered very small time 
intervals, in the limit infinitesimal time interval. We denote by T the 
time of maturity of a bond. At a point in time s < T the time to maturity 
is t = T – s. In the infinitesimal interval dt, the bond value P(t) changes 
by an amount dP according to the following equation: 
dP = –iPdt 
where i is the deterministic short-term interest rate. 
If M is the principal to be repaid at maturity, we have the initial condi-
tion M = P(0). The solution of this an ordinary differential equation with 
separable variables whose solution is 

620 
The Mathematics of Financial Modeling and Investment Management 
P = Me–it = Me–i(T–s) 
If the interest rate is a known function of time, the above equation 
becomes 
dP = –i(t)Pdt 
This too is an equation with separable variables whose solution is 
–∫
Ti u
( ) u
d 
P = Me
 
s 
where M is the principal to be repaid. The equivalence pathwise between 
capital appreciation and present value is valid only if interest rates are 
known. 
In the above expression, the interest rate i is the instantaneous rate 
of interest, also called the short-term rate. In continuous time, the short-
term rate is the limit of the interest rate over a short time interval when 
the interval goes to zero. As observations can only be performed at dis-
crete dates, the short-term rate is a function i(t) such that 
t2 i s( ) s
d 
∫t1 
e 
represents the interest earned over the interval (t1,t2). 
We can now examine these valuation formulas in the limiting case 
where the interval between two coupon payments goes to zero. This 
means that coupon payments are replaced by a continuous stream of 
cash flows with rate c(s). As discussed in Chapter 15 on arbitrage pric-
ing, a continuous cash flow rate means that 
t2 
C = ∫c
 
s( ) s
d 
t1 
is the cash received in the interval (t1,t2). To gain a better understanding 
of these valuation relationships, let’s now explicitly compute the present 
value of a continuous cash-flow rate c(s). We will arrive at the formula 
for the present value of a known, deterministic continuous cash flow 
rate c(t) in two different ways. We can thus illustrate in a simple context 
two lines of reasoning that will be widely used later. 

621 
Term Structure Modeling and Valuation of Bonds and Bond Options 
The first line of reasoning is the following. The cash received over the 
infinitesimal interval (t,t + dt) is c(t)dt. Its value at time 0 is therefore 
c(t)dte–it, if the short-term rate is constant, or, more in general, 
–∫
t i s( )  s
d 
c t( )dte 
0 
if the short-term rate is variable. The value at time 0 of the entire cash-
flow stream is the infinite sum of all these elementary elements, that is, it 
is the integral 
t 
( )e –is
P0 = c s
s
d 
∫ 
0 
for the constant short-term rate, and: 
t
s i u
–∫
( ) u
d 
P0 = c s( )e 
0 
s
d 
∫ 
0 
in the general case of variable (but known) short-term interest rates. 
This present value has to be interpreted as the market price at which the 
stream of continuous cash flows would trade if arbitrage is to be 
avoided. 
The second line of reasoning is more formal. Consider the cumu-
lated capital C(t) which is the cumulative cash flow plus the interest 
earned. In the interval (t,t + dt), the capital increments by the cash c(t)dt 
plus the interest i(t)C(t)dt earned on the capital C(t) in the elementary 
period dt. We can therefore write the equation 
dC = i(t)C(t)dt + c(t)dt 
This is a linear differential equation of the type 
dx 
------ = A t
+ ( ) , 0 ≤t < ∞
( )x
a
 
t
dt 
with initial conditions x(0) = ξ. This is a one-dimensional case of the 
general d-dimensional case discussed in Chapter 10. It can be demon-
strated that this equation has an absolutely continuous solution in the 
domain 0 ≤t < ∞; this solution can be written in the following way: 

622 
The Mathematics of Financial Modeling and Investment Management 
t 
x t
( ) x 0
s
( )ds , 0 ≤t < ∞
( ) = Φ t
( ) + ∫Φ–1( )a s
0 
where Φ(t), called the fundamental solution, solves the equation 
dΦ 
( )Φ , 0 ≤t < ∞ 
dt 
------- = A t
In the case we are considering 
x t
( ) , A t
( ) , a t
( ) , ξ = 0
( ) = C t
( ) = i t
( ) = c t
and 
i s( )ds
∫0 
t
Φ t( ) = e 
and therefore 
s
i s
i u
( )ds t 
–∫
( )du
C t
c s
( ) = e ∫0 
t
∫( )e 
0 
ds 
0 
If we consider that 
–∫
t i s( )ds
= C t
P0 
( )e 
0 
is the value at time 0 of the capital C(t), we again find the formula 
t
s i u
–∫
( )du
( )e 
0 
ds
P0 = ∫c s
0 
that we had previously established in a more direct way. 
If the coupon payments are a continuous cash-flow stream, the sen-
sitivity of their present value to changes in interest rates under the 
assumption of constant interest rates are: 

623 
Term Structure Modeling and Valuation of Bonds and Bond Options 

t 
 
( )e –is 
∂P 
∂

 
0 ∫c s
s
d 

 
t 
∂[c s( )e –is 
t 
( )e –is 
------ = ------------------------------------ = ∫--------------------------] s
d = –∫sc s
s
d 
∂i 
∂i 
0 
∂i 
0 
The above formula parallels the discrete-time formula that was estab-
lished in Chapter 4.7 
THE TERM STRUCTURE OF INTEREST RATES IN 
CONTINUOUS TIME 
Our ultimate objective is to establish a stochastic theory of bond pricing 
and of bond option pricing. To do so, we will reformulate term struc-
ture theory in a continuous-time, continuous-state environment. We will 
subsequently develop examples on how processes can be discretized, 
thus going back to a discrete-state, discrete-time environment. The sto-
chastic description of interest rates is challenging from the point of view 
of both mathematics and economic theory. We discussed the economic 
theories of interest rates earlier in this chapter. 
Mathematical difficulties stem from the fact that one should con-
sider not just one interest rate but the entire term structure of interest 
rates that was defined earlier. This is, in principle, a (difficult) problem 
of infinite dimensionality. Though attempts have been made in the aca-
demic literature to describe the stochastic behavior of a curve without 
any restriction, in practice models currently in use make simplifications 
so that the movement of the term structure curve is constrained to that 
of one or a small number of factors. 
The term structure of interest rates is a function U(t,s) of two vari-
ables t,s that represents the yield computed at time t of a zero-coupon 
risk-free bond with maturity s. The yield on a zero-coupon bond is 
called the spot rate. In calculating the spot rate in developed bond mar-
kets, the yields on government bonds are used. Government bonds are 
typically coupon-paying instruments. However, we have seen in this 
chapter how to obtain, from arbitrage arguments, the theoretical spot 
rates from a set of yields of coupon-paying bonds. The term structure of 
interest rates is a mathematical construct as only a finite number of spot 
rates can be observed. A continuous curve needs to be reconstructed 
from these discrete points. 
7 See footnote 7 in Chapter 4, p. 114. Note that in Chapter 4, V is used rather than 
P to denote market price. 

624 
The Mathematics of Financial Modeling and Investment Management 
Spot Rates: Continuous Case 
Assume for the moment that the evolution of short-term interest rates is 
deterministic and it is known. Thus, at any time t the function i(s) that 
describes the short-term rate is known for every moment s ≥t. Recall 
that i(s) is the limit of the interest rate for an interval that tends to zero. 
Earlier in this chapter we established that the value at time t1 of capital 
of a risk-free bond paying B(t2) at time t2 is given by 
i s
2 ( )ds
t
–∫
t
1
(
) = B t2
B t1
(
)e 
The yield over any finite interval (t1,t2) is the constant equivalent 
interest rate 
t2
Rt1 
over the same interval (t1,t2) which is given by the equation 
t
i s
–(t2 – t1)R 2
2 ( )ds
t
B t1
(
)e 
1 = B t2
–∫t
t
1
(
) = B t2
(
)e 
Given a short-term interest rate function i(t), we can therefore 
u
define the term structure function Rt as the number which solves the 
equation 
ui s
–
–(u
t)Ru 
–∫
( )ds
t
t 
e 
= e 
In a deterministic setting, we can write 
u 
u 
1
Rt = ---------------∫i s( )ds
(u
t)
– 
t 
This relationship does not hold in a stochastic environment, as we will 
see shortly. From the above it is clear that 
u is the yield of a risk-free
Rt 
bond over the interval (t,u). The function 
ui s
–∫
( )ds
u
t 
= e
Λt 

625 
Term Structure Modeling and Valuation of Bonds and Bond Options 
is called the discount function.8 
The term on the right side is the price at time t of a bond of face 
value 1 maturing at u. 
Forward Rates: Continuous Case 
The forward rate f(t,u) is the short-term spot rate at time u contracted 
at time t. To avoid arbitrage, the following relationship must hold: 
logΛu + ∆u – logΛu 
∂logΛu 
t
( , 
t
f t  u  ) = lim – ----------------------------------------------t = – -----------------
∆u →0 
∆u
∂u 
In this deterministic setting, the above relationship yields: f(t,t) = 
i(t). Given the short-rate function i(s), the term structure is completely 
determined and vice versa. 
In a stochastic environment, short-term interest rates form a sto-
chastic process is(ω). This means that for each state of the world there is 
a path of spot interest rates. For each path and for each interval (t,u), 
we can compute the discount function 
ui s
–∫
( ) s
d 
t 
e 
Under a risk-neutral probability measure Q, the price at time t of a 
bond of face value 1 maturing at time u is the expected value of 
ui s
–∫
( ) s
d 
t 
e 
computed at time t: 
ui s
–∫
( ) s
d 
u
Q
Λt = Et
e 
t 
The term structure function can be computed from the discount func-
tion as follows as follows: 
8 Some authors call this function the term structure of interest rates. For example, 
Darrell Duffie, Dynamic Asset Pricing Theory (Princeton, NJ: Princeton University 
Press, Third Edition, 2001) and Steven Shreve, Stochastic Calculus and Finance 
(Springer, forthcoming 2004). 

626 
The Mathematics of Financial Modeling and Investment Management 
ui s
–∫
( ) s
d 
u 
1
1 
 Q
t
Rt = – ---------------log (Λu) = – ---------------log Et e 

t 

–
–
(u
t)
(u
t)
 
As noted above, this formula does not imply 
u 
u 
– 
Q ∫( ) s
d 
(u
t)Rt = Et 
i s
t 
Relationships for Bond and Option Valuation 
We have established the formula 
u
u 
–∫
( ) s
d 
–
–(u
t)Rt = EQ
t e 
t i s
e 
in a rather intuitive way as the expectation under risk-neutral probabil-
ity of discounted final bond values. However, this formula can be 
derived formally as a particular case of the general expression for the 
price of a security that we determined in Chapter 15 on arbitrage pric-
ing in continuous time: 
T
T
T
–r
u
d 
–r
u
d 
u 
St = Et e
Q ∫t 
u
ST + ∫e ∫t 
dDs 
t 
considering that, for zero-coupon bonds, the payoff rate is zero and that 
we assume ST = 1. 
We used risk-neutral probabilities for the following reason. The factor 
ui s( ) s
d 
∫t 
e 
represents capital appreciation pathwise. However, the formula 
ui s
–∫
( ) s
d 
u
t 
= e
Λt 
which gives the price at time t of a bond of face value 1 maturing at u in 
a deterministic environment, does not hold pathwise in a stochastic 

627 
Term Structure Modeling and Valuation of Bonds and Bond Options 
environment. This is because bonds of longer maturities are riskier than 
bonds of shorter maturities. The martingale relationship holds only for 
risk-neutral probabilities. 
We can now go back to the forward rates. The expression 
logΛ u + ∆ u – logΛ u 
∂ logΛ u 
( , 
t
t
f t  u  ) = lim – --------------------------------------------- = – -----------------t -
→ 
∆ 
0 
∆ u
u 
∂ u 
holds in a stochastic environment when the term structure is defined as 
above. 
We have now defined the basic terms and relationships that can be 
used for bond valuation and for bond option valuation and we have 
established a formula that relates the term structure to the short-rate 
process. The next step is to specify the models of the short-term interest 
rate process. The simplest assumption is that the short-term rate follows 
an Itô process of the form 
ˆ
drt = µ( rt, t) dt + σ( rt, t) dBt 
where dBˆ t is a standard Brownian motion under the equivalent martin-
gale measure. 
As explained in Chapter 15 on arbitrage pricing, it is possible to 
develop all calculations under the equivalent martingale measure and to 
revert to the real probabilities only at the end of calculations. This pro-
cedure greatly simplifies computations. Under the equivalent martingale 
measure all price processes St follow Itô processes with the same drift of 
the form 
ˆ
dSt = rtStdt + σ( rt, t) dBt 
Note that the short-term interest rate process is not a price process 
and therefore does not follow the previous equation. Models of the 
short-term rate as the above are called one-factor model because they 
model only one variable. 
The Feynman-Kac Formula 
Computing the term structure implies computing the expectation 
ui s
–∫ ( )  s
d 
u
Q
Λ t = Et
e 
t 

628 
The Mathematics of Financial Modeling and Investment Management 
We will now describe a mathematical technique for computing this 
expectation using the Feynman-Kac formula. 
To understand the reasoning behind the Feynman-Kac formula, 
recall that there are two basic ways to represent stochastic processes. 
The first, which was presented in Chapter 8, is a direct representation of 
uncertainty pathwise through Itô processes. Itô processes can be 
thought of as modifications of Brownian motions. One begins by defin-
ing Brownian motions and then defines a broad class of stochastic pro-
cesses, the Itô processes, as Itô integrals obtained from the Brownian 
motion. Discretizing an Itô process, one obtains equations that describe 
individual paths. 
An equivalent way to represent stochastic Itô processes is through 
transition probabilities. Given a process Xt that starts at X0, the transi-
tion probabilities are the conditional probability densities p(X /X0).
t
Given that the process is a Markov process, these densities also describe 
the transition between the value of the process at time s to time t: 
p(X Xs) that we write p(x,t,y,s). The Markov nature of the process
t
means that, given any function h(y), the expectation E [h(X Xs)] is the
s
t
same as if the process started anew at the value Xs. 
It can be demonstrated that the transition density p(x,t,y,s) obeys 
the following partial differential equation (PDE) which is called the for-
ward Kolmogorov equation or the Fokker-Planck equation: 
2
∂
( 
1∂2[σ (x t)p x t y s)] ∂µ(x t)p x t y s)]
, 
( , ,  ,  
[ 
, 
( , ,  ,
----p x t y s) = -- ---------------------------------------------------------- – -----------------------------------------------------
∂x 
, ,  ,  
∂t 
2 
∂x 2 
with boundary conditions p(x,t,y,s) = δ (y) where δ (y) is Dirac’s delta
s
s
function.9 The numerical solution of this equation, after discretization, 
gives the required probability density. 
For example, consider the Brownian motion whose stochastic differ-
ential equation is 
= dBt , µ = 0, σ = 1
dXt 
The associated Fokker-Planck equation is the diffusion equation in one 
dimension: 
9 Strictly speaking Dirac’s delta function is not a function but a distribution. In a 
loose sense, it is a function that assumes value zero in all points except one where it 
becomes infinite. It is defined only through its integral which is finite. 

629 
Term Structure Modeling and Valuation of Bonds and Bond Options 
∂p 
1
2∂2 p
------ = --σ --------
∂t 
2 
∂x 2 
As a second example, consider the geometric Brownian motion whose 
stochastic differential equation is 
= µX dt + σXtdB , µ(Xt, t) = µX , σ(Xt, t) = σXt
dXt
t
t 
t 
The associated Fokker-Planck equation is 
2
∂p 
1
2∂2(x p) 
∂(xp)
------ = --σ -------------------- – µ--------------
∂x
∂t 
2 
∂x 2 
The Fokker-Planck equation is a forward equation insofar it gives 
the probability density at a future time t starting at the present time s. 
Another important PDE associated with Itô diffusions is the following 
backward Kolmogorov equation: 
∂2 p x t y s)
∂p x t y s)
( , ,  ,  
( , ,  ,
∂ ( , ,  ,  
1 
,
,
–----p x t y s) = --σ2(x t)--------------------------------- – µ(x t)------------------------------
∂t 
2 
∂x 2 
∂x 
The Kolmogorov backward equation gives the probability density that 
we were at x,t given that we are now at y,s. Note that there is a fundamen-
tal difference between the backward and the forward Kolmogorov equa-
tions because the Itô processes are not reversible. In other words, the 
probability density that we were at x,t given that we are now at y,s is not 
the same as if we start the process at y,s and we look at density at x,t. 
Thus far we have established an equivalence between stochastic dif-
ferential equations and associated partial differential equations in the 
sense that they describe the same process. We have now to make an 
additional step by establishing a connection between the expectations of 
an Itô process and an associated PDE. The connection is provided by the 
Feynman-Kac formula which is obtained from a generalization of the 
backward Kolmogorov equation. 
Consider the following PDE: 
∂F x t) 
1 
∂2F x t)
∂F x t)
( , 
( ,
( ,
–------------------- = --σ2(x t)---------------------- + µ(x t)-------------------
,
, 
∂x
∂t 
2 
∂x 2 

630 
The Mathematics of Financial Modeling and Investment Management 
with boundary conditions F(x,T) = Ψ(x). Consider now the stochastic 
differential equation 
dX
= µ(X , t)dt + σ(X , t)dB , s ∈ [t,T], Xt = x
s
s 
s
s 
There is a fundamental relationship between the two equations given by 
the Feynman-Kac formula, which states that 
( ,
F x t) = 
[Ψ(X ) 
= x]
Et 
T Xt 
The meaning of this relationship can be summarized as follows. A 
PDE with the related boundary conditions F(x,T) = Ψ(x) is given. The 
solution of this PDE is a function of two variables F(x,t), which assumes 
the value Ψ(x) for t = T. A stochastic differential equation (SDE) is asso-
ciated to this equation. The two coefficients of the PDE are the drift and 
the volatility of the SDE. The solution of the SDE starts at (x,t). For 
each starting point (x,t), consider the expectation E [Ψ(XT)]. This
t
expectation coincides with F(x,t). 
One might wonder how it happened that a conditional expectation— 
which is a random variable—has become the perfectly deterministic solu-
tion of a PDE. The answer is that F(x,t) associates the expectation of a 
given function Ψ(XT) to each starting point (x,t). This relationship is 
indeed deterministic while the starting point depends on the evolution 
of the stochastic process which solves the SDE. It is thus easy to see why 
the above is a consequence of the backward Kolmogorov equation 
which associates to each starting point (x,t) the conditional probability 
density of X .
T
We can now make the final step and state the Feynman-Kac equa-
tion in a more general form. In fact, it can be demonstrated that, given 
the following PDE: 
( , 
( ,
( ,
∂F x t) 
1 
∂2F x t) 
,
∂F x t) 
( , 
( ,
------------------- + --σ2(x t)---------------------- + µ(x t)------------------- – f x t)F x t) = 0
, 
∂x
∂t 
2 
∂x 2 
with boundary conditions F(x,T) = Ψ(x) and given the stochastic equa-
tion 
dX
= µ(X , t)dt + σ(X , t)dB , s ∈ [t,T], Xt = x
s
s 
s
s 
the following relationship holds: 

631 
Term Structure Modeling and Valuation of Bonds and Bond Options 
(
–∫
Tf XT, s)ds
( ,
F x t) = Et e 
t 
Ψ(XT)
= x
Xt 
We can now go back to the original problem of computing the term 
structure from the stochastic differential equation of the short-rate pro-
cess. Recall that the term structure is given by the following conditional 
expectation: 
ui s( )ds
u = EQ
t e ∫t
Λt 
If we apply the Feynman-Kac formula, we see that the term struc-
ture is a function 
u = F it, t)
(
Λt 
of time t and of the short-rate it which solves the following PDE: 
( , 
( ,
( ,
∂F x t) 
1 
∂2F x t)
∂F x t) 
( ,
,
,
------------------- + --σ2(x t)---------------------- + µ(x t)------------------- – xF x t) = 0 
∂x
∂t 
2 
∂x 2 
with boundary conditions F(x,T) = 1. 
Note explicitly that the solution of this equation does not determine 
the dynamics of interest rates. In other words, given the short-term rate 
it at time t the function 
u = F it, t)
(
Λt 
does not tell us what interest rate will be found at time s > t. It does tell, 
however, the price at time s of a bond with face value 1 at maturity T for 
every interest rate i . If the coefficients σ = σ(x), µ = µ(x) do not depend
s
on time explicitly, then one single function gives the entire term structure. 
Note also that the above is true in general for any asset which does 
not exhibit any intermediate payoff. Recall, in fact, the pricing formula: 
St 
Et 
Q e 
ru 
– 
u
d 
t 
T∫ 
ST 
e 
ru 
– 
u
d 
t 
s∫ 
t 
T 
∫ 
dDs
+
= 

632 
The Mathematics of Financial Modeling and Investment Management 
If intermediate payoffs are zero the previous formula becomes 
T–r
u
d 
u
Q ∫t
St = Et
e 
ST 
Given the final price ST, there is a pricing function in the sense that 
T–r
u
d 
u
Q ∫t
St = F it, t) = Et
e 
ST
( 
The pricing function satisfies a Feynman-Kac formula and is the solu-
tion of a PDE. It tells us that the price St is a function of time t and of 
the interest rate at time t. 
Multifactor Term Structure Model 
The above discussion presented the derivation of the term structure 
from the interest rate process. We say that, under this assumption, the 
term structure model is a one-factor model because it depends on one 
single process. Empirical analysis has shown that one factor is insuffi-
cient. Principal component analysis of the term structure of the U.S. 
Treasury market, as well as other country government bond markets, 
has shown that three factors are sufficient to explain 98% of the term 
structure fluctuations. The three factors are the level, slope, and curva-
ture of the yield curve. Typically 90% of the term structure is explained 
by changes in the level of interest rates. Around 8% is explained by 
changes in the slope, or steepness, of the spot rate curve. Exhibit 20.4 
provides a summary of these studies.10 
Multifactor models of the term-structure have been proposed. Note 
that multifactor models described in the literature and currently used by 
practitioners might use variables such as the long-term interest rate and 
the short-term interest rate. This might give the impression that the 
short-term interest rate is not sufficient to determine the term structure. 
This is not true. The short-term rate is indeed sufficient to completely 
determine the term structure. Conversely, given the term structure, 
10 In addition to the references in Exhibit 20.4, there is the study from which the ex-
hibit is reproduced: Lionel Martellini, Philippe Priaulet, and Stéphane Priaulet, “An 
Empirical Analysis of the Domestic and Euro Yield Curve Dynamics,” Chapter 24 in 
Frank J. Fabozzi and Moorad Choudhry (eds.), The Handbook of European Fixed 
Income Markets (Hoboken, NJ: John Wiley & Sons, 2004). 

EXHIBIT 20.4 
Summary of Some Popular Studies of Yield Curve Dynamics 
Authors
 
Country (Period) 
Kind of Rates 
Range 
Factors 
% of Explanation
633 
Robert Litterman and José Scheinkman, “Common Factors Affecting Bond Returns,”
Journal of Fixed Income (June 1991), pp. 54–61.
C. Kanony and M. Mokrane, “Reconstitution de la courbe des taux, analyse des fac-
teurs d’évolution et couverture factorielle,” Cahiers de la Caisse Autonome de Refi-
nancement 1 (June 1992).
R.L. D’Ecclesia and S.A. Zenios, “Risk Factor Analysis and Portfolio Immunization in
the Italian Bond Market,” Journal of Fixed Income 4, no. 2 (September 1994), pp. 51–
58.
J. Kärki and C. Reyes, “Model Relationship,” Risk 7, no. 12 (December 1994), pp. 32–35.
J.R. Barber and M.L. Copper, “Immunization Using Principal Component Analysis,” 
Journal of Portfolio Management (Fall 1996), pp. 99–105.
A. Bühler and H. Zimmerman, “A Statistical Analysis of the Term Structure of Interest 
Rates in Switzerland and Germany,” Journal of Fixed Income 6, no. 3 (December
1996), pp. 55–67.
Golub, B. W., and L. M. Tilman, “Measuring Yield Curve Risk Using Principal Compo-
nents Analysis, Value at Risk, and Key Rate Durations,” Journal of Portfolio Man-
agement (Summer 1997), pp. 72–84.
I. Lekkos, “A Critique of Factor Analysis of Interest Rates,” Journal of Derivatives (Fall 
2000), pp. 72–83.
L. Martellini and P. Priaulet, Fixed-Income Securities: Dynamic Methods for Interest
Rate Risk Pricing and Hedging (New York: John Wiley & Sons, 2000). 
U.S. (1984–88)
 
Spot Zero-
6M–18Y 
3 
88.04/8.38/1.97
Coupon (ZC) 
France (1989–90) 
Spot ZC 
1Y–25Y 
2 
93.7/6.1 
Italy (1988–92) 
Spot ZC 
6M–7Y 
3 
93.91/5.49/0.42 
Germ./Switz./U.S.
Spot ZC 
3M–10Y 
3 
Total: 97/98/98 
(1990–94)
U.S. (1985–91) 
Spot ZC 
1M–20Y 
3 
80.93/11.85/4.36 
Germany (1988–96) 
Spot ZC 
1M–10Y 
3 
71/18/4 
Switzerland (1988–96) 
75/16/3 
RiskMetrics
Spot ZC 
3M–30Y 
3 
92.8/4.8/1.27
09/30/96)
U.S. (1984–95) 
1–Year 
1Y–9Y 
5 
56.5/17.4/9.86/8.12/4.3
Germany (1987–95) 
Forward 
50.6/17.3/13.5/8.8/5.8
U.K. (1987–95)
 
Japan (1987–95)
 
France (1995–98) 
Spot ZC
 
63.5/6.3/7.5/8.1/5.3
42.8/25.5/17.1/6/4.9
1M–10Y 
3 
66.64/20.52/6.96 
Note: M stands for month and Y for year. For example, “88.04/8.38/1.97” means that the first factor explains 88.04% of the yield curve
variations, the second 8.38%, and the third 1.97%. Sometimes, we also provide the total amount by adding up these terms.
Source: Exhibit A1 in Lionel Martellini, Philippe Priaulet, and Stéphane Priaulet, “An Empirical Analysis of the Domestic and Euro
Yield Curve Dynamics,” Chapter 24 in Frank J. Fabozzi and Moorad Choudhry (eds.), The Handbook of European Fixed Income
Markets (Hoboken, NJ: John Wiley & Sons, 2004). 

634 
The Mathematics of Financial Modeling and Investment Management 
short-term interest rates are determined. Multiple factors model the 
term structure as well as the short-term rate. 
In fact, a multifactor term-structure model is a model of the form: it 
= F(Xt,t) where it is the short-rate process and Xt is an N-dimensional 
Itô process that obeys the following SDE: 
ˆ
dX
= µ(X , t)dt + σ(X , t)dB
s
s 
s
s 
ˆ
where Xs is an N-vector, i is a 1-vector, dB  is an N-dimensional
s 
Brownian motion under an equivalent martingale measure, µ(Xs,t) is an 
N-vector and σ(Xs,t)s is a N×N matrix. The Feynman-Kac formula can 
be extended in a multidimensional environment in the sense that the fol-
lowing relationships hold: 
–∫
Tf XT, s) s
d
( 
( , 
Q
t
F x  t) = Et e 
Ψ(XT) 
and 
( , 
( ,
( ,
∂F x  t) 
1 
∂2F x  t)
∂F x  t) 
( ,
,
, 
,
------------------- + --tr σ(x t)σT(x t)---------------------- + µ(x t)------------------- – xF x t) = 0 
∂x
∂t 
2 
∂x 2 
Arbitrage-Free Models versus Equilibrium Models 
Stochastic differential equations are typically used to model interest 
rates. There are two approaches used to implement the same SDE into a 
term structure model: equilibrium and no arbitrage. While these two 
approaches begin with a given SDE, they differ as to how each approach 
applies the SDE to bonds and contingent claims. Equilibrium models 
begin with an SDE model and develop pricing mechanisms for bonds 
under an equilibrium framework. Arbitrage models, also referred to as 
no-arbitrage models, start with the same or similar SDE models as the 
equilibrium models. However, no-arbitrage models utilize observed 
market prices to generate an interest rate lattice. The lattice represents 
the short rate in such a way as to ensure there is a no arbitrage relation-
ship between the observed market price and the model-derived value. 
Practitioners prefer arbitrage-free models to value options on bonds 
because such models ensure that the prices observed for the underlying 
bonds are exact. As a result, bonds and options on those bonds will be 
valued in a consistent framework. Equilibrium models, in contrast, will 

635 
Term Structure Modeling and Valuation of Bonds and Bond Options 
not price bonds exactly so they do not provide a consistent framework 
for valuing options on bonds and the underlying bonds. 
Examples of One-Factor Term Structure Models 
A number of one-factor and multifactor term structure models have 
been proposed in the literature. We will discuss some of the more popu-
lar one-factor models here:
 ■ The Ho-Lee model
 ■ The Vasicek model
 ■ The Hull-White model
 ■ The Cox-Ingersoll-Ross model
 ■ The Kalotay-Williams-Fabozzi model 
■ Black-Karasinski model 
■ The Black-Derman-Toy model 
Our coverage is not intended to be exhaustive.11 
Most of these models are based on a short-term process which satis-
fies an SDE of the following type: 
ˆ
,
di = µ(i t)dt + σiαdB
The various models differ for the choice of the drift µ(i,t) and of the 
exponent α. 
The Ho-Lee Model 
The first arbitrage-free model was introduced by Thomas Ho and Sang-
Bin Lee in 1986.12 In the Ho-Lee model α = 0, µ(i,t) = µ = constant. 
di = µdt + σdBˆ 
This model is quite simple. It has the disadvantage that interest rates 
might drift and become negative, which is inconsistent with what is 
observed in financial markets. In addition, having only two free param-
eters, it cannot be easily fitted to the initial observed term structure. 
11 For a more detailed discussion of these models, see Gerald W. Buetow, Jr., Frank 
J. Fabozzi, and James Sochacki, “A Review of No Arbitrage Interest Rate Models,”
Chapter 3 in Fabozzi, Interest Rate, Term Structure, and Valuation Modeling. 
12 Thomas Ho and Sang Bin Lee, “Term Structure Movements and Pricing Interest 
Rate Contingent Claims,” Journal of Finance (1986), pp. 1011–1029. 

636 
The Mathematics of Financial Modeling and Investment Management 
The Vasicek Model 
In 1977, Oldrich Vasicek proposed the Ornstein-Uhlenbeck process as a 
model of interest rates to produce a one-factor equilibrium model.13 In 
the Vasicek model α = 0, 
(L
i)
– 
,
µ(i t) = ---------------
T 
L
i
ˆ
– 
di = -----------dt + σdB
T 
where L and T are constants. 
The Vasicek model is a mean-reverting process as interest rates are 
pulled back to the value L. Interest rates exhibit mean reversion proper-
ties, a fact that the Vasicek models correctly address. However, having 
only three free parameters, the Vasicek model is difficult to fit to the ini-
tial term structure. 
The Hull-White Model 
In 1990 Hull and White proposed a mean-reverting model that generalizes 
the Vasicek model.14 The Hull-White model is given by the choice α = 0, 
(L t( ) – i)
,
µ(i t) = -----------------------
T t( )  
with time-variable volatility 
L t( ) – i 
( )dB
di = ------------------dt + σ t
ˆ 
T t( )  
The Hull-White model has enough parameters to be fitted to any 
initial term structure. 
13 Oldrich Vasicek, “An Equilibrium Characterization of the Term Structure,” Jour-
nal of Financial Economics (1977), pp. 177–188. 
14 J. Hull and A. White, “Pricing Interest Rate Derivative Securities,” Review of Fi-
nancial Studies 3 (1990), pp. 573–592, and, “One Factor Interest Rate Models and 
the Valuation of Interest Rate Derivative Securities,” Journal of Financial and Quan-
titative Analysis (1993), pp. 235–254. 

637 
Term Structure Modeling and Valuation of Bonds and Bond Options 
The Cox-Ingersoll-Ross Model 
In 1985 John Cox, Jonathan Ingersoll, and Stephen Ross (CIR)15 pro-
posed an equilibrium model with 
1
α = --
2 
(L
i)
– 
,
µ(i t) = ---------------
T 
L
i
– 
di = -----------dt + σ idBˆ 
T 
where L and T are constants. The CIR model is mean reverting but has 
only three free parameters to fit the initial term structure. It can be 
shown that in this model interest rates always remain non-negative. 
Kalotay, Williams, and Fabozzi 
In 1993 Andrew Kalotay, George Williams, and Frank Fabozzi (KWF)16 
proposed a model with α = 1, µ = θ(t)i described by the following SDE: 
di = θ t( )idt + σidBt 
For θ = constant the model becomes a geometric random walk. As the 
model is lognormal, interest rates never become negative. 
Black-Karasinski 
In 1991 Fisher Black and Piotr Karasinski17 proposed a model with α = 
1 described by the following SDE: 
d ln i = [θ(t) – φ(t)ln i]dt + σ(t)dBt 
15 John Cox, Jonathan Ingersoll, and Stephen. Ross, “A Theory of the Term Struc-
ture of Interest Rates,” Econometrica (1985), pp. 385–408. 
16 Andrew J. Kalotay, George Williams, and Frank J. Fabozzi, “A Model for the Val-
uation of Bonds and Embedded Options,” Financial Analyst Journal (May–June 
1993), pp. 35–46. 
17 Fischer Black and Piotr Karasinski, “Bond and Option Pricing when Short Rates 
are Lognormal,” Financial Analysts Journal (July–August 1991), pp. 2–59. 

638 
The Mathematics of Financial Modeling and Investment Management 
If φ(t) = 0 then the Black-Karasinki model becomes the KWF model. 
The Black-Karasinki model is lognormal and therefore interest rates 
cannot be negative. The error correction term also prevents rates from 
diverging. 
The Black-Derman-Toy Model 
In 1990 Fischer Black, Emanuel Derman, and William Toy18 proposed a 
lognormal arbitrage-free model with α = 1, µ(i,t) = c(t)i: 
di = c t
( )idB
( )idt + σ t
ˆ 
Two-Factor Models 
A number of two factor models have also been proposed. Brennan and 
Schwarz, for example, proposed in 1979 a model based on a short rate i 
and a long rate y.19 This model is written as a set of two equations, 
, ,  
, ,
di = µ1(i τ y)dt + σ1(i τ y)dBˆ 
, ,  
, ,
dy = µ2(i τ y)ydt + σ2(i τ y)ydBˆ * 
where the two Brownian motions are correlated. 
PRICING OF INTEREST-RATE DERIVATIVES 
The models of the term structure described thus far are based on deriv-
ing the arbitrage-free prices of zero-coupon bonds from the short-term 
rate process. In a nutshell, the methodology involves the following 
steps:
 ■ Step 1. Assume that the short rate process it is a function of an N-
dimensional Itô process Xt (the factors): 
(
it = F Xt, t) 
18 Fischer Black, Emanuel Derman, and William Toy, “A One Factor Model of In-
terest Rates and Its Application to the Treasury Bond Options,” Financial Analyst 
Journal (January–February 1990), pp. 33–39. 
19 Michael J. Brennan. and Eduardo S. Schwartz, “A Continuous Time Approach to 
the Pricing of Bonds,” Journal of Banking and Finance 3 (1979), pp. 133–155. 

639 
Term Structure Modeling and Valuation of Bonds and Bond Options 
ˆ
dX
= µ(X , t)dt + σ(X , t)dB
s
s 
s
s 
where dBˆ s is a standard Brownian motion under an equivalent mar-
tingale measure Q. In the single factor case, the short rate process it 
follows an Itô process
ˆ
di
= µ(i , t)dt + σ(i , t)dB
s
s 
s
s 
■ Step 2. Compute the arbitrage-free price of a zero-coupon bond using 
the theory of arbitrage-free pricing under an equivalent martingale 
measure according to which the price 
u at time t of a zero-coupon
Λt 
bond with face-value 1 maturing at time u is 
ui s( )  s
d 
u = EQ
t e ∫t
Λt 
■ Step 3. Use the Feynman-Kac formula to show that Λu
t = F it, t) ,
( 
which solves the following PDE: 
( , 
( ,
( ,
∂F x  t) 
1 
∂2F x  t)
∂F x  t) 
( ,
,
,
------------------- + --σ2(x t)---------------------- + µ(x t)------------------- – xF x t) = 0 
∂x
∂t 
2 
∂x 2 
with boundary conditions F(x,T) = 1. 
The above methodology can be immediately extended to cover the 
pricing of a class of interest-rate derivatives whose payoff can be 
expressed as a function of short-term interest rates or, alternatively, as a 
function of bond prices. Consider, first, the case of a derivative security 
whose payoff is given by two functions h(it,t) and g(iτ,τ), which specify, 
respectively, the continuous payoff rate and the final payoff at a speci-
fied date τ ≤T. This specification covers a rather broad class of deriva-
tive securities and bond optionality, including European options on 
zero-coupon bonds, swaps, caps and floors. 
The general arbitrage pricing theory (see Chapter 15) can be imme-
diately applied. The price at time t of a derivative security defined as 
above is the following extension of the bond pricing formula: 
τ 
u ( )  s
d 
i s
i s
( )  s
d
Q 
∫t 
(
∫t 
τ
(
(
F it, t) = Et ∫e 
h is, s) s
d + e 
g iτ, τ) 
t 

640 
The Mathematics of Financial Modeling and Investment Management 
Note that the first term under the expectation sign is the expectation 
under risk-neutral probabilities of the formula for the present value of a 
continuous cash-flow stream that we established earlier in this chapter: 
t
s i u
–∫
( )  u
d 
V0 = c s( )e 
0 
s
d
∫ 
0 
where c(s) = h(is,s) and the initial time is 0. 
The Feynman-Kac formula can be extended to this case. In fact it 
can be demonstrated that the function F obeys the following PDE: 
( , 
( ,
( ,
∂F x  t) 
1 
∂2F x  t) 
,
∂F x  t) 
( , 
( ,
,
------------------- + --σ2(x t)---------------------- + µ(x t)------------------- – xF x t) + h x  t) = 0 
∂x
∂t 
2 
∂x 2 
with boundary conditions F(x,τ) = g(x,τ). If h(x,t) = 0, g(x,τ) ≡1, we find 
the bond valuation formula of the previous section. 
THE HEATH-JARROW-MORTON MODEL OF THE 
TERM STRUCTURE 
In the previous sections we derived the term structure from a short-term 
rate process which might depend, in turn, on a number of factors. How-
ever, this is not the only possible choice. In 1992, David Heath, Robert 
Jarrow, and Andrew Morton introduced a methodology that recovers 
the term structure (i.e., bond prices) from the forward rates.20 The key 
issue with this methodology is to ensure the absence of arbitrage. 
Recall that the forward rate f(t,u) is the short-term spot rate at time 
u contracted at time t. In a deterministic environment (that is, assuming 
that the forward rates are known) to avoid arbitrage, the following rela-
tionships must hold: 
u
∂(logΛt )
( ,
f t  u) = – ----------------------
∂u 
20 David Heath, Robert A. Jarrow, and Andrew J. Morton, “Bond Pricing and the 
Term Structure of Interest Rates: A New Methodology for Contingent Claim Valu-
ation,” Econometrica (1992), pp. 77–105. 

641 
Term Structure Modeling and Valuation of Bonds and Bond Options 
f(t,t) = it 
Integrating the first relationship we obtain 
u ( ,
–∫f t s  )ds
u
t 
= e
Λt 
Now suppose that in the interval u ∈(0,T] the forward rate obeys 
the following SDE: 
df = α(t,u)dt + σ(t,u)dBt 
Equivalently, this means that for each u ∈(0,T] the following rela-
tionship holds: 
t
t 
( , 
,
, 
ˆ
f t u  ) = f(0, u) + α(s u)ds + ∫σ(s u)dBs
∫ 
0
0 
Stochastic differentiation yields 
u
u 
( , 
( , 
f( ,
d –∫f t s
 
)ds
= f t t  )dt + ∫d t s  
)ds
t
t 
u 
= i t
,
, 
ˆ t
( )dt – ∫[α(t s)dt + σ(t s)dB ]ds
t 
( )dt – α*(t u)dt + σ*(t u)dB
= i t
, 
ˆ
, 
t 
where 
u 
,
,
α*(t u) = α(t s)ds
∫ 
t 
u 
,
,
σ*(t u) = σ(t s)ds
∫ 
t 
Using Itô’s lemma, it can be demonstrated that the term structure 
process obeys the following SDE: 

642 
The Mathematics of Financial Modeling and Investment Management 

u
u ˆ
( )  α*(t u) + --[σ*(t u)]2 dt – σ*(t u)Λ dBt
dΛt = Λu
t 
 i t – 
, 
1 
,
,
 
2 
 
t 
This process determines the bond price process in function of a for-
ward rate process. However, to avoid arbitrage, the forward rate pro-
cess must be constrained. In particular, Heath, Jarrow, and Morton 
(HJM) demonstrated the following theorems. 
Suppose that the forward rate obeys the following SDE under the 
probability measure P: 
t
t 
( , 
,
, 
ˆ
f t u) = f(0, u) + α(s u)ds + ∫σ(s u)dBs
∫ 
0
0 
Then P is an equivalent martingale measure if and only if the coeffi-
cients α(t,u), σ(t,u) obey the following relationship: 
1 
,
,
α*(t u) = --[σ*(t u)]2 
2 
that is, 
u 

2 
1
u 
,
,
α(t s)ds = --∫σ(t s)ds
∫ 
2
 
t
t 
where 0 ≤t ≤u ≤T. 
If P is not an equivalent martingale measure, then there is no arbi-
trage if and only if there is an adapted process θ(τ) satisfying the follow-
ing relationship: 
1
α*(t u) = --[σ*(t u)]2 + σ*(t u)θ τ
, 
, 
,
( ) , 0 ≤t ≤u ≤T 
2 
or, equivalently, differentiating both sides with respect to u: 
, 
,
, 
,
( ) , 0 ≤t ≤u ≤T
α(t u) = σ(t u)σ*(t u) + σ(t u)θ t
Implementing the HJM methodology takes advantage of the available 
degrees of freedom. The initial forward rate curve f(0,u) can be deter-
mined by observing the initial curve 

643 
Term Structure Modeling and Valuation of Bonds and Bond Options 
∂(log ΛT )
0
f(0, T) = – -----------------------
∂u 
As only a finite number of bond prices can be observed, it is necessary to 
use techniques to convert a number of finite observations into a smooth 
curve. One cannot simply fit a high-degree polynomial to the available 
observations as this would introduce a lot of noise. On the other hand, fit-
ting a low-degree polynomial would create a curve that does not corre-
spond to the true term structure. Splines is an approach that is often used to 
create a smooth initial forward curve. This technique involves fitting pieces 
of curves in such a way that the transition between the pieces is smooth. 
Suppose that the initial forward rate curve has been fitted to empiri-
cal data. Suppose that two deterministic functions σ*(t,u), θ(t) have 
been chosen. Let’s define 
α(t u) = σ(t u)σ*(t u) + σ(t u)θ t
, 
,
, 
,
( )  
With these definitions, the forward rate process is determined by the fol-
lowing equation in the risk neutral probabilities: 
ˆ
,
,
df = σ(t u)σ*(t u)dt + σ(t u)dB
, 
t 
Solving this equation yields the forward rate process and the short-term 
process. The bond pricing equation then becomes 
u
dΛt = i t
t 
, 
u
ˆ
( )Λudt – σ*(t u)Λt dBt 
In this equation only the volatility σ*(t,u) appears. This shows that, 
in order to implement the HJM model, only the initial term structure 
and the volatilities are needed. 
THE BRACE-GATAREK-MUSIELA MODEL 
The Brace-Gatarek-Musiela (BGM) model is a particular implementa-
tion of the HJM model which corresponds to a specific choice of the 
volatility.21 The BGM model is based on defining a forward LIBOR 
21 Alan Brace, Dariusz Gatarek, and Marek Musiela, “The Market Model of Interest 
Rate Dynamics,” Mathematical Finance 7, no. 2 (April 1997), pp 127–155. 

644 
The Mathematics of Financial Modeling and Investment Management 
interest rate which is a simple forward interest rate defined over a dis-
crete time period. The BGM model, and the HJM from which it derives, 
form a wide class of models which has been extensively explored in the 
literature. Here we will only give a brief account of the BGM model. 
First define L(t,0) as the rate of simple interest over a discrete period 
δ so that an amount of D(t,δ ) dollars invested at time t in a bond with 
maturity (t + δ ) become 1 dollar at maturity: 
(
(
D t  δ
, )[ 1 + δ L t, 0)] = 1 
Then define the forward LIBOR as follows: 
D t, τ
δ) 
(
( 
+ 
--------------------------[ 1 + δ L t  τ
, )] = 1 
D t  τ
, )
( 
It is possible to demonstrate that 
+
∫ 
(
τ
τ
δ) f t  u) u
d
( , 
( 
δ 
L t  τ
, ) = ------------------------------------------
e 
– 1 
where f is the continuously compounding forward rate. 
Define now σ *(t,τ ) recursively as follows: 
(
δ L t  τ
, )γ( t τ
, )
+
σ *( t, τ
δ) = σ *( t τ
, ) + -----------------------------------
1 + δ L t  τ
, )
( 
( 
1 
( 
+
L t  τ
, )γ( t τ
, ) = --[ 1 + δ L t  τ
, )][σ *( t, τ
δ) – σ *( t τ
, )]
δ 
DISCRETIZATION OF ITÔ PROCESSES 
Itô processes are stochastic differential equations that admit a forward 
discretization scheme similar to that of ordinary differential equations. 
Consider an Itô process that obeys the following SDE: 
dXt = µ( Xt, t) dt + σ( Xt, t) dBt 

645 
Term Structure Modeling and Valuation of Bonds and Bond Options 
A natural, and simple, discretization scheme is given by the Euler 
approximation. The Euler approximation replaces the differentials with 
finite differences. If we divide the unit interval in n subintervals, the 
Euler approximation replaces the SDE with the following recursive 
scheme: 
 
k 1 
 
k 1
– Xk = µXk, -- -- + σXk, -- ------ εk + 1
Xk + 1 
 
n n 
 
n n 
where εk + 1 are independent random draws from a standard normal, 
N(0,1). A computer implementation of this scheme would start from 
some initial value and compute the solution recursively using a random 
number generator to generate the 
. Repeating the process many
εk + 1 
times over, one obtains many paths and many final points from which 
quantities such as averages can be easily computed. More complex 
schemes can be used in order to obtain a smaller approximation error. 
As an illustration of the above, Exhibit 20.5 presents random paths 
generated using the Euler approximation to approximate several one-
factor interest rate models described earlier in this chapter. 
EXHIBIT 20.5 
Ten Paths Generated from Different One-Factor Interest Rate 
Models 
Ho-Lee model: 
Vasicek model: 
µ = 0.005, σ = 0.1 
L = 1, T = 200, σ = 0.1 

646 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 20.5
 (Continued) 
Hull-White model: 
L(t) = 1 + 0.002t, T(t) = cost. = 200, 
CIR model: 
σ = 0.01 
L = 1, T = 200, σ = 0.005 
Black-Karasinski model: 
Kalotay-Williams-Fabozzi model: 
ϑ(t) = 0.005exp(–0.005t), 
ϑ(t) = 0.005exp(–0.005t), σ = 0.01 
φ(t) = 0.001, σ = 0.01 
SUMMARY
 ■ There are different types of interest rates.
 ■ The term structure of interest rates is a curve that associates to each 
future date the yield of an hypothetical risk-free zero-coupon bond 
maturing exactly at that date.
 ■ The term structure of interest rates can be recovered from empirical 
data using the no-arbitrage principle and curve smoothing techniques.
 ■ The term structure of interest rates is not fixed but might change with 
time. 

647
Term Structure Modeling and Valuation of Bonds and Bond Options 
■ A number of classical economic theories explain the shape of the term 
structure.
 ■ Mathematically, the term structure can be derived by a model of short-
term interest rates.
 ■ Multifactor models of the term structure are based on multifactor mod-
els of the short-term interest rates.
 ■ A number of models for the short term rate as (multivariate) Itô pro-
cesses have been proposed.
 ■ The term structure of the interest rates can also be modelled starting 
from a model of the forward rates.
 ■ Features of term structure models include absence of arbitrage, mean 
reversion, ability to fit empirical term structure. 



## Bond Portfolio Management

I 
CHAPTER 21 
Bond Portfolio Management 
n this chapter, we look at the more popular strategies for managing a bond 
portfolio. A portfolio manager will select a portfolio strategy that is con-
sistent with the objectives and policy guidelines of the client or institution. 
As explained in Chapter 1, a portfolio manager’s benchmark can be either a 
bond market index or liabilities. In this chapter, we provide an overview of 
strategies for managing a bond portfolio versus both benchmarks. 
MANAGEMENT VERSUS A BOND MARKET INDEX 
There are several bond market indexes that represent different sectors of 
the bond market. The wide range of bond market indexes available can 
be classified as broad-based bond market indexes and specialized bond 
market indexes. The three broad-based bond market indexes most com-
monly used by institutional investors are the Lehman Brothers U.S. 
Aggregate Index, the Salomon Smith Barney Broad Investment-Grade 
Bond Index, and the Merrill Lynch Domestic Market Index. There are 
more than 5,500 issues in each index. One study has found that the cor-
relation of annual returns between the three broad-based bond market 
indexes were around 98%.1 The three broad-based bond market indexes 
are computed daily and are market value weighted. This means that for 
each issue, the ratio of the market value of an issue relative to the mar-
ket value of all issues in the index is used as the weight of the issue in all 
1 Frank K. Reilly and David J. Wright, “Bond Market Indexes,” Chapter 7 in Frank 
J. Fabozzi (ed.), The Handbook of Fixed Income Securities: Sixth Edition (New 
York: McGraw-Hill, 2000). 
649 

650 
The Mathematics of Financial Modeling and Investment Management 
calculations.2 The specialized bond market indexes focus on one sector 
of the bond market or a subsector of the bond market. 
There are risk factors associated with a bond market index which 
we discuss later in this chapter. The proper way to categorize bond port-
folio strategies is in terms of the degree to which a manager constructs a 
portfolio with a risk profile that differs from the risk profile of the bond 
market index that is the manager’s benchmark. The following general 
categorization of bond portfolio management strategies has been pro-
posed by Kenneth Volpert of the Vanguard Group:3
 ■ Pure bond index matching
 ■ Enhanced indexing/matching risk factors
 ■ Enhanced indexing/minor risk factor mismatches
 ■ Active management/larger risk factor mismatches
 ■ Active management/full-blown active 
In terms of risk and return, a pure bond index matching strategy 
involves the least risk of underperforming a bond market index. 
An enhanced indexing strategy can be pursued so as to construct a 
portfolio to match the primary risk factors associated with a bond mar-
ket index without acquiring each issue in the index. While in the spec-
trum of strategies defined by Volpert this strategy is called an “enhanced 
strategy,” some investors refer to this as simply an indexing strategy. 
Two commonly used techniques to construct a portfolio to replicate an 
index are cell matching (stratified sampling) and tracking error minimi-
zation using a multifactor risk model. Both techniques assume that the 
performance of an individual bond depends on a number of systematic 
factors that affect the performance of all bonds and on an unsystematic 
factor unique to the individual issue or issuers. With the cell matching 
approach the index is divided into cells representing the risk factors. 
The objective is then to select from all of the issues in the index one or 
more issues in each cell that can be used to represent that entire cell. 
This approach is inferior to the second approach, minimizing tracking 
error using a multifactor risk model discussed later.4 
Another form of enhanced strategy is one in which the portfolio is 
constructed so as to have minor deviations from the risk factors that affect 
the performance of the index. For example, there might be a slight over-
2 The securities in the SSB BIG index are all trader priced. For the two other indexes, 
the securities are either trader priced or model priced. 
3 Kenneth E. Volpert, “Managing Indexed and Enhanced Indexed Bond Portfolios,” 
Chapter 3 in Frank J. Fabozzi (ed.), Fixed Income Readings for the Chartered Financial 
Analyst Program: First Edition (New Hope, PA: Frank J. Fabozzi Associates, 2000). 

651 
Bond Portfolio Management 
weighting of issues or sectors where the manager believes there is relative 
value. A feature of this strategy is that the duration of the constructed 
portfolio is matched to the duration of the benchmark index. That is, 
there is no duration bet for this strategy, just as with the pure index match 
strategy and the enhanced index with matching risk strategy. 
Active bond strategies are those that attempt to outperform the 
bond market index by intentionally constructing a portfolio that will 
have a greater index mismatch than in the case of enhanced indexing. 
Volpert classifies two types of active strategies. In the more conservative 
of the two active strategies, the manager constructs the portfolio so that 
it has larger mismatches relative to the benchmark index in terms of risk 
factors. This includes minor mismatches of duration. Typically, there 
will be a limitation as to the degree of duration mismatch that a client 
will permit. In full-blown active management, the manager is permitted 
to make a significant duration bet without any constraint. 
Tracking Error and Bond Portfolio Strategies 
In Chapter 18, we explained forward-looking (ex ante) tracking error. 
Tracking error, or active risk, is the standard deviation of a portfolio’s 
return relative to the return of the benchmark index.5 Forward-looking 
tracking error is an estimate of how a portfolio will perform relative to 
a benchmark index in the future. Forward-looking tracking error is used 
in risk control and portfolio construction. The higher the forward-look-
ing tracking error, the more the manager is pursuing a strategy in which 
the portfolio has a different risk profile than the benchmark index and 
there is, therefore, greater active management. 
We can think of the spectrum of bond portfolio strategies relative to 
a bond market index in terms of forward-looking tracking error. In con-
structing a portfolio, a manager can estimate forward-looking tracking 
error. When a portfolio is constructed to have a forward-looking track-
ing error equal or close to zero, the manager has effectively designed the 
portfolio to replicate the performance of the benchmark. If the forward-
looking tracking error is maintained for the entire investment period, 
the portfolio’s return should be close to zero. Such a strategy—one with 
4 For a discussion and illustration of both approaches to bond indexing, see Lev 
Dynkin, Jay Hyman, and Vadim Konstantinovsky, “Bond Portfolio Analysis Rela-
tive to a Benchmark,” Chapter 23 in Frank J. Fabozzi and Harry M. Markowitz 
(eds.), The Theory and Practice of Investment Management (Hoboken, NJ: John 
Wiley & Sons, 2002). 
5 There are two types of tracking error—backward-looking tracking error and for-
ward-looking tracking error. Backward-looking tracking error is calculated based on 
the actual performance of a portfolio relative to a benchmark index. 

652 
The Mathematics of Financial Modeling and Investment Management 
a forward-looking tracking error of zero or “very small”—indicates that 
the manager is pursing a passive strategy relative to the benchmark 
index. When the forward-looking tracking error is “large” the manager 
is pursuing an active strategy. 
Risk Factors and Portfolio Management Strategies 
Since forward-looking tracking error indicates the degree of active portfo-
lio management being pursued by a manager, it is necessary to understand 
what factors (referred to as “risk factors”) affect the performance of a man-
ager’s benchmark index. The risk factors affecting one of the most popular 
broad-based bond market indexes, the Lehman Brothers U.S. Aggregate 
Index, have been investigated by Dynkin, Hyman, and Wu.6 A summary of 
the risk factors is provided in Exhibit 21.1. They first classify the risk fac-
tors into two types: systematic risk factors and nonsystematic risk factors. 
Systematic risk factors are the common factors that affect all securities in a 
certain category in the benchmark bond market index. Nonsystematic fac-
tor risk is the risk that is not attributable to the systematic risk factors. 
EXHIBIT 21.1 
Summary of Risk Factors for a Benchmark 
Systematic 
Nonsystematic 
Risk Factors 
Risk Factors 
Term Structure 
Nonterm Structure 
Issuer 
Issue 
Risk Factors 
Risk Factors 
Specific 
Specific 
Sector Risk 
Quality Risk 
Optionality Risk 
Coupon Risk 
MBS Sector Risk 
MBS Volatility Risk 
MBS Prepayment Risk 
6 Lev Dynkin, Jay Hyman, and Wei Wu, “Multi-Factor Risk Factors and Their Ap-
plications,” in Frank J. Fabozzi (ed.) Professional Perspectives on Fixed Income 
Portfolio Management: Volume 2 (Hoboken, NJ: John Wiley & Sons, 2001). 

653 
Bond Portfolio Management 
Systematic risk factors, in turn, are divided into two categories: 
term structure risk factors and nonterm structure risk factors. Term 
structure risk factors are risks associated with changes in the shape of 
the term structure (level and shape changes). Nonterm structure risk 
factors include the following:
 ■ Sector risk
 ■ Quality risk
 ■ Optionality risk
 ■ Coupon risk
 ■ MBS sector risk
 ■ MBS volatility risk
 ■ MBS prepayment risk 
Sector risk is the risk associated with exposure to the sectors of the 
benchmark index. For example, consider the Lehman Brothers U.S. Aggre-
gate Index. At the macro level, these sectors include Treasury, agencies, credit 
(i.e., corporates), residential mortgages, commercial mortgages, and asset-
backed securities (ABS). Each of these sectors is divided further. For example, 
the credit sector is divided into financial institutions, industrials, transporta-
tions, and utilities. In turn, each of these subsectors is further divided. For 
the residential mortgage market (which includes agency passthrough securi-
ties), there are a good number of subsectors based on the entity issuing the 
security, the coupon rate, the maturity, and the mortgage design. 
Quality risk is the risk associated with exposure to the credit rating 
of the securities in the benchmark index. The breakdown for the Leh-
man Brothers U.S. Aggregate Index which includes only investment-
grade credits is Aaa+, Aaa, Aa, A, Baa, and mortgage-backed securities 
(MBS). MBS includes credit exposure to the agency passthrough sector. 
Optionality risk is the risk associated with an adverse impact on the 
embedded options of the securities in the benchmark index. This 
includes embedded options in callable and putable corporate bonds, 
MBS, and ABS. Coupon risk is the exposure of the securities in the 
benchmark index to different coupon rates. 
The last three risks are associated with the investing in residential 
mortgage passthrough securities. The first is MBS sector risk which is 
the exposure to the sectors of the MBS market. The value of an MBS 
depends on the expected interest rate volatility and prepayments. MBS 
volatility risk is the exposure of a benchmark index to changes in 
expected interest rate volatility. MBS prepayment risk is the exposure of 
a benchmark index to changes in prepayments. 
Nonsystematic factor risks are classified as risks associated with a 
particular issuer, issuer-specific risk, and those associated with a partic-
ular issue, issue-specific risk. 

654 
The Mathematics of Financial Modeling and Investment Management 
Determinants of Tracking Error 
Using statistical techniques,7 given the risk factors associated with a 
benchmark index, forward-looking tracking error can be estimated for a 
portfolio based on historical return data. The tracking error occurs 
because the portfolio constructed deviates from the exposures for the 
benchmark index. The tracking error for a portfolio relative to a bench-
mark index can be decomposed as follows: 
I. Tracking error due to systematic risk factors:
 A. Tracking error due to term structure risk factor
 B. Tracking error due to nonterm structure risk factors
 1. Tracking error due to sector
 2. Tracking error due to quality
 3. Tracking error due to optionality
 4. Tracking error due to coupon
 5. Tracking error due to MBS sector
 6. Tracking error due to MBS volatility
 7. Tracking error due to MBS prepayment 
II. Tracking error due to nonsystematic risk factors
 A. Tracking error due to issuer-specific risk
 B. Tracking error due to issue-specific risk 
A manager provided with information about (forwarding-looking) 
tracking error for the current portfolio can quickly assess if (1) the risk 
exposure for the portfolio is one that is acceptable and (2) if the partic-
ular exposures are the ones being sought. 
Illustration of the Multifactor Risk Model 
We will now illustrate how a multifactor risk model is used to quantify 
the risk profile of a portfolio relative to a benchmark and then explain 
how optimization can be used to construct a portfolio. We will use the 
Lehman Brothers multifactor model in the illustration. The bond market 
index used as benchmark is the Lehman Brothers U.S. Aggregate Index.8 
7 Lev Dynkin of Lehman Brothers has described the statistical technique to the authors 
as follows. The risk model uses decomposition of individual bond returns into carry, 
yield curve, and spread components. The spread component is regressed on a certain 
set of systematic (or common to all bonds in a peer group) risk factors using a prespec-
ified set of sensitivities. Residuals of this regression are used to estimate security-specific 
risk. Factor realizations collected over many months form the covariance matrix of sys-
tematic risk factors. The current mismatch in risk sensitivities between the portfolio 
and the benchmark is multiplied by this matrix to get the systematic tracking error. 
8 The illustration in this section draws from Dynkin, Hyman, and Wu, “Multi-Factor 
Risk Factors and Their Applications.” 

655 
Bond Portfolio Management 
Exhibit 21.2 shows the sample portfolio used in the illustration. The 
portfolio includes 57 bonds. The analysis was performed on September 
30, 1998. Summary information for the portfolio and the corresponding 
information for the Lehman Brothers U.S. Aggregate Index are shown in 
Exhibit 21.3. From the exhibit, it can be seen that the 57-bond portfolio 
has greater interest rate risk as measured by duration—4.82 for the 
portfolio versus 4.29 for the benchmark. 
EXHIBIT 21.2 
Portfolio Report: Composition of Sample Portfolio, 9/30/98 
# 
Issuer Name 
Coup 
Maturity 
Moody 
S&P 
Sect 
Par Val 
%
 1 BAKER HUGHES 
8.000 
05/15/04 
A2 
A 
IND
 5,000 0.87
 2 BOEING CO 
6.350 
06/15/03 
Aa3 
AA 
IND 
10,000 1.58
 3 COCA-COLA ENTERPRISES I 
6.950 
11/15/26 
A3 
A+ 
IND 
50,000 8.06
 4 ELI LILLY CO 
6.770 
01/01/36 
Aa3 
AA 
IND
 5,000 0.83
 5 ENRON CORP 
6.625 
11/15/05 
Baa2 
BBB+ 
UTL
 5,000 0.80
 6 FEDERAL NATL MTG ASSN 
5.625 
03/15/01 
Aaa+ 
AAA+ 
USA 
10,000 1.53
 7 FEDERAL NATL MTG ASSN-G 
7.400 
07/01/04 
Aaa+ 
AAA+ 
USA
 8,000 1.37
 8 FHLM Gold 7-Years Balloon 
6.000 
04/01/26 
Aaa+ 
AAA+ 
FHg 
20,000 3.03
 9 FHLM Gold Guar Single F. 
6.500 
08/01/08 
Aaa+ 
AAA+ 
FHd 
23,000 3.52 
10 FHLM Gold Guar Single F. 
7.000 
01/01/28 
Aaa+ 
AAA+ 
FHb 
32,000 4.93 
11 FHLM Gold Guar Single F. 
6.500 
02/01/28 
Aaa+ 
AAA+ 
FHb 
19,000 2.90 
12 FIRST BANK SYSTEM 
6.875 
09/15/07 
A2 
A− 
FIN
 4,000 0.65 
13 FLEET MORTGAGE GROUP 
6.500 
09/15/99 
A2 
A+ 
FIN
 4,000 0.60 
14 FNMA Conventional Long T. 
8.000 
05/01/21 
Aaa+ 
AAA+ 
FNa 
33,000 5.14 
15 FNMA MTN 
6.420 
02/12/08 
Aaa+ 
AAA+ 
USA
 8,000 1.23 
16 FORD MOTOR CREDIT 
7.500 
01/15/03 
A1 
A 
FIN
 4,000 0.65 
17 FORT JAMES CORP 
6.875 
09/15/07 
Baa2 
BBB− 
IND
 4,000 0.63 
18 GNMA I Single Family 
9.500 
10/01/19 
Aaa+ 
AAA+ 
GNa 
13,000 2.11 
19 GNMA I Single Family 
7.500 
07/01/22 
Aaa+ 
AAA+ 
GNa 
30,000 4.66 
20 GNMA I Single Family 
6.500 
02/01/28 
Aaa+ 
AAA+ 
GNa
 5,000 0.76 
21 GTE CORP 
9.375 
12/01/00 
Baa1 
A 
TEL 
50,000 8.32 
22 INT-AMERICAN DEV BANK-G 
6.375 
10/22/07 
Aaa 
AAA 
SUP
 6,000 1.00 
23 INTL BUSINESS MACHINES 
6.375 
06/15/00 
A1 
A+ 
IND 
10,000 1.55 
24 LEHMAN BROTHERS INC 
7.125 
07/15/02 
Baa1 
A 
FIN
 4,000 0.59 
25 LOCKHEED MARTIN 
6.550 
05/15/99 
A3 
BBB+ 
IND 
10,000 1.53 
26 MANITOBA PROV CANADA 
8.875 
09/15/21 
A1 
AA− 
CAN
 4,000 0.79 
27 MCDONALDS CORP 
5.950 
01/15/08 
Aa2 
AA 
IND
 4,000 0.63 
28 MERRILL LYNCH & CO.-GLO 
6.000 
02/12/03 
Aa3 
AA− 
FIN
 5,000 0.76 
29 NATIONSBANK CORP 
5.750 
03/15/01 
Aa2 
A+ 
FIN
 3,000 0.45 
30 NEW YORK TELEPHONE 
9.375 
07/15/31 
A2 
A+ 
TEL
 5,000 0.86 
31 NIKE INC 
6.375 
12/01/03 
A1 
A+ 
IND
 3,000 0.48 
32 NORFOLK SOUTHERN CORP 
7.800 
05/15/27 
Baa1 
BBB+ 
IND
 4,000 0.71 
33 NORWEST FINANCIAL INC. 
6.125 
08/01/03 
Aa3 
AA− 
FIN
 4,000 0.62 
34 ONT PROV CANADA-GLOBA 
7.375 
01/27/03 
Aa3 
AA− 
CAN
 4,000 0.65 

656 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 21.2 
(Continued) 
# 
Issuer Name 
Coup 
Maturity 
Moody 
S&P 
Sect 
Par Val 
% 
35 PUB SVC ELECTRIC + GAS 
6.125 
08/01/02 
A3 
A− 
ELU
 3,000 0.47 
36 RAYTHEON CO 
7.200 
08/15/27 
Baa1 
BBB 
IND
 8,000 1.31 
37 RESOLUTION FUNDING CORP 
8.125 
10/15/19 
Aaa+ 
AAA+ 
USA 
17,000 3.51 
38 TIME WARNER ENT 
8.375 
03/15/23 
Baa2 
BBB− 
IND
 5,000 0.90 
39 ULTRAMAR DIAMOND SHAM 
7.200 
10/15/17 
Baa2 
BBB 
IND
 4,000 0.63 
40 US TREASURY BONDS 
10.375 
11/15/12 
Aaa+ 
AAA+ 
UST 
10,000 2.17 
41 US TREASURY BONDS 
10.625 
08/15/15 
Aaa+ 
AAA+ 
UST 
14,000 3.43 
42 US TREASURY BONDS 
6.250 
08/15/23 
Aaa+ 
AAA+ 
UST 
30,000 5.14 
43 US TREASURY NOTES 
8.875 
02/15/99 
Aaa+ 
AAA+ 
UST
 9,000 1.38 
44 US TREASURY NOTES 
6.375 
07/15/99 
Aaa+ 
AAA+ 
UST
 4,000 0.61 
45 US TREASURY NOTES 
7.125 
09/30/99 
Aaa+ 
AAA+ 
UST 
17,000 2.59 
46 US TREASURY NOTES 
5.875 
11/15/99 
Aaa+ 
AAA+ 
UST 
17,000 2.62 
47 US TREASURY NOTES 
6.875 
03/31/00 
Aaa+ 
AAA+ 
UST
 8,000 1.23 
48 US TREASURY NOTES 
6.000 
08/15/00 
Aaa+ 
AAA+ 
UST 
11,000 1.70 
49 US TREASURY NOTES 
8.000 
05/15/01 
Aaa+ 
AAA+ 
UST
 9,000 1.50 
50 US TREASURY NOTES 
7.500 
11/15/01 
Aaa+ 
AAA+ 
UST 
10,000 1.67 
51 US TREASURY NOTES 
6.625 
03/31/02 
Aaa+ 
AAA+ 
UST
 6,000 0.96 
52 US TREASURY NOTES 
6.250 
08/31/02 
Aaa+ 
AAA+ 
UST 
10,000 1.60 
53 US TREASURY NOTES 
5.750 
08/15/03 
Aaa+ 
AAA+ 
UST
 1,000 0.16 
54 US TREASURY NOTES 
6.500 
05/15/05 
Aaa+ 
AAA+ 
UST
 1,000 0.17 
55 US TREASURY NOTES 
6.125 
08/15/07 
Aaa+ 
AAA+ 
UST
 1,000 0.17 
56 WELLS FARGO + CO 
6.875 
04/01/06 
A2 
A− 
FIN
 5,000 0.80 
57 WESTPAC BANKING CORP 
7.875 
10/15/02 
A1 
A+ 
FOC
 3,000 0.49 
Source: Exhibit 9 in Lev Dynkin, Jay Hyman, and Wei Wu, “Multi-Factor Risk 
Models and Their Applications,” in Frank J. Fabozzi (ed.) Professional Perspec-
tives on Fixed Income Portfolio Management: Volume 2 (New Hope, PA: Frank J. 
Fabozzi Associates, 2001). 
Systematic Risk Exposure 
The estimated total tracking error is 52 basis points per year. Exhibit 21.3 
provides a summary of the tracking error breakdown for the 57-bond port-
folio. As described earlier, the systematic risk factors are broken into two 
parts: term structure factors and nonterm structure factors. From the first 
column of Exhibit 21.3 it can be seen that the three major systematic risk 
exposures are (1) term structure factors (i.e., exposure to changes in the 
term structure); (2) sector factors (i.e., changes in credit spreads of sectors); 
and (3) quality factors (i.e., changes in credit spreads by quality rating). 
The subcomponents of the tracking error breakdown reported in 
Exhibit 21.3 are shown in two different ways, labeled “Isolated” and 
“Cumulative.” In the “Isolated” column, the tracking error due to the 
effect of each subcomponent is considered in isolation. What is not con-

657 
Bond Portfolio Management 
sidered in the “Isolated” calculations are the correlations between the 
risk factors. For example, the 14.7 basis points for the tracking error for 
quality considers only the mismatch between the portfolio exposure and 
benchmark exposure due to quality and taking into consideration the 
correlations only of quality exposure for the different quality ratings. 
The tracking error for the portfolio is 52 basis points and the tracking 
error for the systematic and nonsystematic risk is 45 basis points and 
26.1 basis points, respectively. Because the tracking errors represent 
EXHIBIT 21.3 
Tracking Error Breakdown for Sample Portfolio 
Sample Portfolio versus Aggregate Index, 9/30/98 
Tracking Error (bp/year) 
Isolated 
Cumulative 
Change in 
Cumulative 
Tracking error term structure 
36.3 
36.3 
36.3 
Nonterm structure 
39.5 
Tracking error sector 
32.0 
38.3
 2.0 
Tracking error quality 
14.7 
44.1
 5.8 
Tracking error optionality
 1.6 
44.0 
−0.1 
Tracking error coupon
 3.2 
45.5
 1.5 
Tracking error MBS sector
 4.9 
43.8 
−1.7 
Tracking error MBS volatility
 7.2 
44.5
 0.7 
Tracking error MBS prepayment
 2.5 
45.0
 0.4 
Total systematic tracking error 
45.0 
Nonsystematic tracking error 
Issuer-specific 
25.9 
Issue-specific 
26.4 
Total 
26.1 
Total tracking error 
52 
Systematic 
Nonsystematic 
Total 
Benchmark return standard deviation 
417
 4 
417 
Portfolio return standard deviation 
440 
27 
440 
Source: Exhibit 2 in Lev Dynkin, Jay Hyman, and Wei Wu, “Multi-Factor Risk 
Models and Their Applications,” in Frank J. Fabozzi (ed.) Professional Perspec-
tives on Fixed Income Portfolio Management: Volume 2 (New Hope, PA: Frank 
J. Fabozzi Associates, 2001).

658 
The Mathematics of Financial Modeling and Investment Management 
variances, it not the sum of these two risks that sum to the portfolio’s 
tracking error, but rather the squares of these two tracking errors that 
will equal the square of the portfolio’s tracking error. Or equivalently, 
the square root of the square of the two tracking errors will equal the 
portfolio’s tracking error (i.e., [(45.0)2 + (26.1)2]0.5 = 52.0). Adding of 
variances assumes that there is zero correlation between the risk factors 
(i.e., the risk factors are statistically independent). 
The alternative calculation for subdividing the tracking error is shown 
in the last two columns of Exhibit 21.3, the “Cumulative” calculation. In 
the second column the cumulative tracking error is computed by introduc-
ing one group of risk factors at a time and computing the resulting change 
in the tracking error. The analysis begins with the 36.3 basis point tracking 
error due to the term structure risk. The value shown in the next row of 
38.3 basis points is calculated by holding the risk factors constant except
for term structure risk and sector risk. The change in the cumulative track-
ing error from 36.3 to 38.3 basis points is shown in the last column for the 
row corresponding to sector risk. The 2 basis point change is interpreted 
as follows: given the exposure to yield curve risk, sector risk adds 2 basis 
points to tracking error. By continuing to add the subcomponents of the 
risk factors, the cumulative tracking error is determined. Because of the 
way in which the calculations are performed, the cumulative tracking 
error shown for all the systematic risk factors in the next-to-the last col-
umn is 45 basis points, the same as in the “isolated” calculation. 
Exhibit 21.4 can be used to understand the difference between the 
“isolated” and “cumulative” calculations. For purposes of the illustra-
tion, the exhibit shows a covariance matrix for just the following three 
groups of risk factors: yield curve (Y), sector spreads (S), and quality 
spreads (Q). How the covariance matrix is used to calculate the subcom-
ponents of the tracking error in the “isolated” case is shown in panel a. 
The diagonal of the covariance matrix shows the elements of the matrix 
that are used in the calculation for that subcomponent. The off-diagonal 
terms of the matrix deal with the correlations among different sets of risk 
factors. They are not used in calculating the tracking error and therefore 
do not contribute to any of the partial tracking errors. The elements of 
the covariance matrix used in the calculation of the “cumulative” track-
ing error at each stage of the calculation are shown in Panel b of Exhibit 
21.4. The incremental tracking error due to sector risk takes into consid-
eration not only the S × S variance but also the cross terms S × Y and Y × 
S which represent the correlation between yield curve risk and sector risk. 
Note that the incremental tracking error need not be positive. When the 
correlation is negative, the increment will be negative. This can be seen in 
the last column of Exhibit 21.3 which shows that the incremental risk 
due to the MBS sector risk is –1.7 basis points. 

659 
Bond Portfolio Management 
EXHIBIT 21.4 
Illustration of “Isolated” and “Cumulative” Calculations of 
Tracking Error Subcomponentsa 
a. Isolated Calculation of Tracking Error Components
Y × Y 
Y × S 
Y × Q 
S × Y 
S × S 
S × Q 
Q × Y 
Q × S 
Q × Q 
b. Cumulative Calculation of Tracking Error Components
Y × Y 
Y × S 
Y × Q 
S × Y 
S × S 
S × Q 
Q × Y 
Q × S 
Q × Q 
a Y – Yield curve risk factors; S – Sector spread risk factors; Q – Credit Quality 
spread risk factors. 
Source: Exhibit 12 in Lev Dynkin, Jay Hyman, and Wei Wu, “Multi-Factor Risk 
Models and Their Applications,” in Frank J. Fabozzi (ed.), Professional Perspec-
tives on Fixed Income Portfolio Management: Volume 2 (New Hope, PA: Frank 
J. Fabozzi Associates, 2001).
The “isolated” calculation helps a portfolio manager identify the 
relative magnitude of each subcomponent of the tracking error. The 
advantage of the “cumulative” calculation is that it takes into consider-
ation the correlations among the subcomponents of the risk factors and 
the sum of the tracking error components is equal to the total tracking 
error. The drawback of the “cumulative” calculation is that it is depen-
dent upon the order in which the risk factors are introduced. 
Another portfolio risk measure provided in Exhibit 21.3 is the vola-
tility of returns. That is, the standard deviation of the return for each 
systematic risk factor and the standard deviation for the portfolio return 
can be computed. Similarly, the standard deviation of the benchmark 
return can be calculated. Note the difference between tracking error and 
standard deviation of returns. The former is computed by using the his-
torical differences in return between the portfolio and the benchmark. 
The latter only considers the historical returns. As was computed for 
tracking error, there are systematic return and nonsystematic return 
components. The last panel in Exhibit 21.3 reports the total standard 
deviation for the portfolio and the benchmark and the composition of 
each in terms of systematic and nonsystematic risk factors. Notice that 
the portfolio’s standard deviation (430 basis points) is greater than that 
of the benchmark (417 basis points). 

660 
The Mathematics of Financial Modeling and Investment Management 
Nonsystematic Risk Exposure 
Now let’s look at nonsystematic risk. The nonsystematic tracking error is 
divided into those that are issuer specific and those that are issue specific. 
As indicated in Exhibit 21.3, the tracking error associated with the 57-
bond portfolio is 52 basis points per annum and there is 26 basis points 
per annum of nonsystematic risk. The latter risk arises from the concen-
tration of the portfolio in individual securities or issuers. The last column 
of Exhibit 21.2 shows this risk. The column reports the percentage of the 
portfolio’s market value invested in each issue. Because there are only 57 
issues in the portfolio, the portfolio is relatively small in terms of issues. 
Consequently, each issue makes up a nontrivial fraction of the portfolio. 
Specifically, look at the exposure to two corporate issuers, GTE Corp. 
and Coca-Cola. Each is more than 8% of the portfolio. If there is a 
downgrade of either firm, this would cause large losses in the 57-bond 
portfolio, but it would not have a significant effect on the benchmark 
which includes 6,932 issues. Consequently, a large exposure in a portfo-
lio to a specific corporate issuer represents a material mismatch between 
the exposure of the portfolio and a benchmark that must be taken into 
account in assessing a portfolio’s risk relative to a benchmark. 
Optimization Application 
The multifactor risk model can be used by the portfolio manager in 
combination with optimization in constructing and rebalancing a port-
folio to reduce tracking error. A portfolio manager using optimization, 
for example, can determine the single largest transaction that can be 
used to reduce tracking error. Or, a portfolio manager can determine 
using optimization a series of transactions (i.e., bond swaps) that would 
be necessary to alter the target tracking error at minimum cost.9 
Suppose that the portfolio manager’s objective is to minimize track-
ing error. From the universe of bonds selected by the portfolio manager, 
9 According to Lev Dynkin of Lehman Brothers, the optimization procedure is as fol-
lows. Instead of finding a complete portfolio that optimizes tracking error in the 
model, a step-by-step optimization algorithm is chosen based on marginal contribu-
tions of each security already in a portfolio or any buy-candidate to the portfolio risk 
versus the benchmark. Current portfolio holdings are then sorted in a descending or-
der of their marginal contribution to tracking error, offering the manager an oppor-
tunity to pick a sell candidate with the most impact on tracking error, but not forcing 
the portfolio manager into any one choice. Once the sell candidate is selected, it is 
paired with any eligible buy candidate to find the highest possible tracking error im-
provement. Buy candidates are ranked on the tracking error that would result from 
having picked each specific security. This step-by-step optimization mechanism al-
lows the portfolio manager to intervene with every transaction. 

661 
Bond Portfolio Management 
an optimizer can be employed to rank bond purchases in terms of the 
marginal decline in tracking error per unit of each bond purchased. A 
portfolio manager would then determine the bond issues that would be 
purchased and the optimizer would then identify potential market-
value-neutral swaps of these bond issues against various bonds issues 
currently held in the portfolio; the optimizer would indicate the optimal 
transaction size for each pair of bond issues that are being swapped 
ranked by the potential reduction in tracking error. 
Dynkin, Hyman, and Wu illustrate how this optimization process can 
be used to minimize the tracking error for the 57-bond portfolio. The 
illustration is provided in Exhibit 21.5. Look at the first trade used in the 
exhibit which indicates that the majority of the large position in the 
Coca-Cola 30-year bond can be swapped for a Treasury note. If the pro-
posed trade (i.e., bond swap) is executed, this would result in (1) a change 
in the systematic exposures to term structure, sector, and quality and (2) a 
reduction in nonsystematic risk by cutting one of the largest issuer expo-
sures. From this one bond swap alone that the optimizer identifies, track-
ing error is reduced from 52 basis points to 29 basis points. Notice that as 
the risk profile of the initial sample portfolio approaches that of the 
benchmark (Lehman Brothers U.S. Aggregate Index), the opportunity for 
major reductions in the tracking error declines. 
If all five transactions shown in Exhibit 21.5 are executed, there is 
the potential to reduce the tracking error to 16 basis points. The result-
ing portfolio after these transactions is effectively a passive portfolio. 
Exhibit 21.6 provides a summary of the tracking error for the portfolio 
if all five transactions are executed. The systematic and nonsystematic 
tracking error is 10 and 13 basis points, respectively. 
LIABILITY-FUNDING STRATEGIES 
Liability-funding strategies are strategies whose objective is to match a 
given set of liabilities due at future times. These strategies provide the cash 
flows needed at given dates at a minimum cost and with zero or minimal 
interest rate risk. However, depending on the universe of bonds that are 
permitted to be included in the portfolio, there may be credit risk and/or 
call risk. Liability-funding strategies are used by (1) sponsors of defined 
benefit pension plans (i.e., there is a contractual liability to make payments 
to beneficiaries); (2) insurance companies for single premium deferred 
annuities (i.e., a policy in which the issuer agrees for a single premium to 
make payments to policyholders over time), guaranteed investment con-
tracts (i.e., a policy in which the issuer agrees for a single premium to 

662 
The Mathematics of Financial Modeling and Investment Management 
EXHIBIT 21.5 
Sequence of Transactions Selected by Optimizer Showing 
Progressively Smaller Tracking Error, $000s 
Initial Tracking Error: 52.0 bp 
Transaction # 1 
Sold: 
31,000 of COCA-COLA ENTERPRISES 
6.950 2026/11/15 
Bought: 
30,000 of U.S. TREASURY NOTES 
8.000 2001/05/15 
Cash Leftover: 
−17.10 
New Tracking Error: 
29.4 bp 
Cost of This Transaction: 
152.500 
Cumulative Cost: 
152.500 
Transaction # 2 
Sold: 
10,000 of LOCKHEED MARTIN 
6.550 1999/05/15 
Bought: 
9,000 of U.S. TREASURY NOTES 
6.125 2007/08/15 
Cash Leftover: 
132.84 
New Tracking Error: 
25.5 bp 
Cost of This Transaction: 
47.500 
Cumulative Cost: 
200.000 
Transaction # 3 
Sold: 
4,000 of NORFOLK SOUTHERN CORP 7.800 2027/05/15 
Bought: 
3,000 of U.S. TREASURY BONDS 
10.625 2015/08/15 
Cash Leftover: 
−8.12 
New Tracking Error: 
23.1 bp 
Cost of This Transaction: 
17.500 
Cumulative Cost: 
217.500 
Transaction # 4 
Sold: 
33,000 of GTE CORP 
9.375 2000/12/01 
Bought: 
34,000 of U.S. TREASURY NOTES 
6.625 2002/03/31 
Cash Leftover:
 412.18 
New Tracking Error: 
19.8 bp 
Cost of This Transaction: 
167.500 
Cumulative Cost: 
385.000 
Transaction # 5 
Sold: 
7,000 of COCA-COLA ENTERPRISES 
6.950 2026/11/15 
Bought: 
8,000 of U.S. TREASURY NOTES 
6.000 2000/08/15 
Cash Leftover: 
−304.17 
New Tracking Error: 
16.4 bp 
Cost of This Transaction: 
37.500 
Cumulative Cost: 
422.500 
Source: Exhibit 15 in Lev Dynkin, Jay Hyman, and Wei Wu, “Multi-Factor Risk 
Models and Their Applications,” in Frank J. Fabozzi (ed.) Professional Perspec-
tives on Fixed Income Portfolio Management: Volume 2 (New Hope, PA: Frank 
J. Fabozzi Associates, 2001).

663 
Bond Portfolio Management 
EXHIBIT 21.6 
Tracking Error Summary 
Passive Portfolio versus Aggregate Index, 9/30/98 
Tracking Error (bp/year) 
Isolated 
Cumulative 
Change 
Tracking error term structure 
7.0
 7.0 
7.0 
Nonterm structure 
9.6 
Tracking error sector 
7.4 
10.5 
3.5 
Tracking error quality 
2.1 
11.2 
0.7 
Tracking error optionality 
1.6 
11.5 
0.3 
Tracking error coupon 
2.0 
12.3 
0.8 
Tracking error MBS sector 
4.9 
10.2 
−2.1 
Tracking error MBS volatility 
7.2 
11.1 
0.9 
Tracking error MBS prepayment 
2.5 
10.3 
−0.8 
Total systematic tracking error 
10.3 
Nonsystematic tracking error 
Issuer-specific 
12.4 
Issue-specific 
3.0 
Total 
12.7 
Total tracking error return 
16 
Systematic 
Nonsystematic 
Total 
Benchmark sigma 
417
 4 
417 
Portfolio sigma 
413 
13 
413 
Source: Exhibit 16 in Lev Dynkin, Jay Hyman, and Wei Wu, “Multi-Factor Risk 
Models and Their Applications,” in Frank J. Fabozzi (ed.) Professional Perspec-
tives on Fixed Income Portfolio Management: Volume 2 (New Hope, PA: Frank 
J. Fabozzi Associates, 2001).
make a single payment to a policyholder at a specified date with a guaran-
teed interest rate); and (3) municipal governments for prerefunding munic-
ipal bond issues (i.e., creating a portfolio that replicates the payments that 
must be made for an outstanding municipal government bond issue), and, 
for states, payments that must be made to lottery winners who have 
agreed to accept payments over time rather than a lump sum. 
There are two types of solutions to the problem of liability funding 
currently used by practitioners: (1) numerical/analytical solutions based 
on the concept of duration and convexity and (2) numerical solutions 

664 
The Mathematics of Financial Modeling and Investment Management 
based on optimization methodologies. Ultimately, all methodologies can 
be cast in the framework of optimization, but duration and convexity play 
an important role from the practical as well as conceptual point of view. 
We will begin by discussing the cash-flow matching approach in a deter-
ministic context and then successively discuss strategies based on duration 
and convexity and lastly a full stochastic programming approach. 
Cash Flow Matching 
Cash flow matching (CFM), also referred to as a dedicated portfolio strat-
egy, in a deterministic environment is the problem of matching a predeter-
mined set of liabilities with an investment portfolio that produces a 
deterministic stream of cash flows.10 In this context, fluctuations of inter-
est rates, credit risk, and other sources of uncertainty are ignored. There 
are, however, conditions where financial decisions have to be made. 
Among them we will consider:
 ■ Reinvestment of excess cash
 ■ Borrowing against future cash flows to match liabilities
 ■ Trading constraints such as odd lots 
To formulate the model, consider a set of m dates {t0,t1,...,tm} and a 
universe U of investable assets U = {1,2,...,n}. Call {Ki,0,...,Ki,m} the 
stream of cash flows related to the i-th asset. We will consider only 
bonds but most considerations that will be developed apply to broader 
classes of assets with positive and negative cash flows. In the case of a 
bond with unit price Pi per unit par value 1, with coupon ci,t, and with 
maturity k, the cash flows are 
{–Pi,ci,1,...,ci,k–1,ci,k + 1,0,...,0} 
Let’s call Lt the liability at time t. Liabilities must be met with a 
portfolio 
∑αiPi 
i ∈ U 
where αi is the amount of bond i in the portfolio. The CFM problem can 
be written, in its simplest form, in the following way: 
10 For an illustration of cash flow matching applied to pension fund liabilities, see 
Frank J. Fabozzi and Peter F. Christensen, “Dedicated Bond Portfolios,” Chapter 45 
in Frank J. Fabozzi (ed.), The Handbook of Fixed Income Securities (New York, NY: 
McGraw Hill, 2000). 

665 
Bond Portfolio Management 
Minimize ∑αiPi , subject to the constraints 
i ∈ U 
∑αiKi t ≥ Lt
, 
i ∈ U 
αi ≥ 0 
The last constraint specifies that short selling is not permitted. 
The above formulation of the CFM as an optimization problem is too 
crude as it takes into account only the fact that it is practically impossible 
to create exactly the required cash flows. In fact, in this formulation at 
each date there will be an excess of cash not used to satisfy the liability 
due at that date. If borrowing and reinvesting are allowed, as is normally 
the case, excess cash can be reinvested and used at the next date while 
small cash shortcomings can be covered with borrowing. 
Suppose, therefore, that it is possible to borrow in each period an 
amount bt at the rate βt and reinvest an amount rt at the rate ρt. Suppose 
that these rates are the same for all periods. At each period we will require 
that the positive cash flow exactly matches liabilities. Therefore coupon 
payments of that period plus the amount reinvested in the previous period 
augmented by the interest earned on this amount plus the reinvestment of 
that period will be equal to the liabilities of the same period, plus the repay-
ment of borrowing in the previous period plus the eventual new borrowing 
of the period. The optimization problem can be formulated as follows: 
Minimize ∑αiPi , subject to the constraints 
i ∈ U 
∑αiKi t + (1 + ρt)rt – 1 + bt = Lt + (1 + βt)bt – 1 + rt
, 
i ∈ U 
bm = 0 
αi ≥ 0; i ∈ U 
The CFM problem formulated in this way is a linear programming (LP) 
problem.11 Problems of this type can be routinely solved on desk-top 
computers using standard off-the-shelf software. 
11 The mathematical programming techniques described in this chapter are discussed 
in Chapter 7. 

666 
The Mathematics of Financial Modeling and Investment Management 
The next step is to consider trading constraints, such as the need to 
purchase “even” lots of assets. Under these constraints, assets can be 
purchased only in multiples of some minimal quantity, the even lots. For 
a large organization, purchasing smaller amounts, “odd” lots, might be 
suboptimal and might result in substantial costs and illiquidity. 
The optimization problem that results from the purchase of assets in 
multiples of a minimal quantity is much more difficult. It is no longer a rel-
atively simple LP problem but it becomes a much harder mixed-integer pro-
gramming (MIP) problem. A MIP problem is conceptually more difficult 
and computationally much more expensive to solve than an LP problem. 
The next step involves allowing for transaction costs. The objective 
of including transaction costs is to avoid portfolios made up of many 
assets held in small quantities. Including transaction costs, which must 
be divided between fixed and variable costs, will again result in a MIP 
problem which will, in general, be quite difficult to solve. 
In the formulation of the CFM problem discussed thus far, it was 
implicitly assumed that the dates of positive cash flows and liabilities are 
the same. This might not be the case. There might be small misalignment 
due to the practical availability of funds or positive cash flows might be 
missing when liabilities are due. To cope with these problems, one could 
simply generate a bigger model with more dates so that all the dates cor-
responding to inflows and outflows are properly considered. In a number 
of cases, this will be the only possible solution. A simpler solution, when 
feasible, consists in adjusting the dates so that they match, considering the 
positive interest earnings or negative costs incurred to match dates. 
In the above formulation of the CFM problem, the initial investment 
cost is the only variable to optimize: The eventual residual cash at the end of 
the last period is considered lost. However, it is possible to design a different 
model under the following scenario. One might try to maximize the final 
cash position, subject to the constraint of meeting all the liabilities and 
within the constraint of an investment budget. In other words, one starts 
with an investment budget which should be at least sufficient to cover all the 
liabilities. The optimization problem is to maximize the final cash position. 
We have just described the CFM problem in a deterministic setting. 
This is more than an academic exercise as many practical dedication 
problems can be approximately cast into this framework. Generally 
speaking, however, a dedication problem would require a stochastic for-
mulation, which in turn requires multistage stochastic optimization. 
Dahl, Meeraus, and Zenios12 discuss the stochastic case. Later in this 
12 H. Dahl, A. Meeraus, and S.A. Zenios, “Some Financial Optimization Models,” 
in S.A. Zenios (ed.), Financial Optimization (Cambridge: Cambridge University 
Press, 1993). 

667 
Bond Portfolio Management 
chapter we discuss dedication in a multistage stochastic formulation, as 
well as other bond portfolio optimization problems. Let’s now discuss 
portfolio immunization, which is the numerical/analytical solution of a 
special dedication problem under a stochastic framework. 
Portfolio Immunization 
The actuary generally credited with pioneering the immunization strat-
egy is Reddington, who defined immunization in 1952 as “the invest-
ment of the assets in such a way that the existing business is immune to 
a general change in the rate of interest.”13 The mathematical formula-
tion of the immunization problem was proposed by Fisher and Weil in 
1971.14 The framework is the following in the single liability case 
(which we refer to as single period immunization): Given a predeter-
mined liability at a fixed time horizon, create a portfolio able to satisfy 
the given liability even if interest rates change. 
The problem would be simple to solve if investors were happy to 
invest in U.S. Treasury zero-coupon bonds (i.e., U.S. Treasury strips) 
maturing at exactly the given date of the liability. However, investors seek 
to earn a return greater than the risk-free rate. For example, the typical 
product where a portfolio immunization strategy is used is a GIC offered 
by an insurance company. This product is typically offered to a pension 
plan. The insurer receives a single premium from the pension sponsor and 
in turn guarantees an interest rate that will be earned such that the pay-
ment to the policyholder at a specified date is equal to the premium plus 
the guaranteed interest. The interest rate offered on the policy is greater 
than that on existing risk-free securities, otherwise a potential policy 
buyer can do the immunization without the need for the insurance com-
pany’s service. The objective of the insurance company is to earn a higher 
rate than that offered on the policy (i.e., the guaranteed interest rate).15 
The solution of the problem is based on the fact that a rise in interest 
rates produces a drop in bond prices but an increase in the reinvestment 
income on newly invested sums while a fall of interest rates increases bond 
prices but decreases the reinvestment income on newly invested sums. One 
13 F.M. Reddington, “Review of the Principle of Life-Office Valuations,” Journal of 
the Institute of Actuaries 78 (1952), pp. 286–340. 
14 L. Fisher and R.L. Weil, “Coping with the Risk of Interest-Rate Fluctuations: Re-
turns to Bondholders from Naive and Optimal Strategies,” Journal of Business (Oc-
tober 1971), pp. 408–431. 
15 For a discussion of the implementation issues associated with immunization, see 
Frank J. Fabozzi and Peter F. Christensen, “Bond Immunization: An Asset/Liability 
Optimization Strategy,” Chapter 44 in The Handbook of Fixed Income Securities: 
Sixth Edition. 

---------------
---------
668 
The Mathematics of Financial Modeling and Investment Management 
can therefore choose an investment strategy such that the change in a port-
folio’s value is offset by changes in the returns earned by the reinvestment 
of the cash obtained through coupon payments or the repayment of the 
principal of bonds maturing prior to the liability date. 
The principle applies in the case of multiple liabilities. To see how 
multiple-period immunization works, let’s first demonstrate that—given 
a stream of cash flows at fixed dates—there is one instant at which the 
value of the stream is insensitive to small parallel shifts in interest rates. 
Consider a case where a sum V0 is initially invested in a portfolio of 
risk-free bonds (i.e., bonds with no default risk) that produces a stream 
of N deterministic cash flows Ki at fixed dates ti. At each time ti the sum 
Ki is reinvested at the risk-free rate. Suppose that there is only one rate r 
common to all periods. The following relationship holds: 
V0 = 
N 
∑Kie 
–rti 
i = 1 
where we have used the formula for the present value in continuous time. 
As each intermediate payment is reinvested, the value of the portfo-
lio at any instant t is given by the following expression: 
Vt = 
N 
∑Kie 
(
–r t  – ti)
rt
= e V0 
i = 1 
Our objective is to determine a time t such that the value Vt at time 
t of the portfolio is insensitive to parallel shifts in the interest rates. The 
quantity Vt is a function of the interest rate r. The derivative of Vt with 
respect to r must be zero so that Vt is insensitive to interest rate changes. 
Let’s compute the derivative: 
N 
∑
dVt
(
(
r t  
Ki t
ti 
– 
– ti)
)e 
= 
dr 
i = 1 
N 
∑Kitie 
–rti 
i = 1
= tVt – Vt -----------------------------
V0 
Kie 
–rti
N 
∑
V t  
 
 
= 
– 
ti 
i = 1 
 
 V0 
 
 

---------
669 
Bond Portfolio Management 
From this expression it is clear that the derivative 
dVt 
dr 
is zero at a time horizon equal to the portfolio duration. In fact, the 
quantity 
N 
Kie 
–rti
∑ ti--------------- 
 V0 
i = 1 
is the portfolio’s duration expressed in continuous time. 
Therefore, if the term structure of interest rates is flat, we can match 
a given liability with a portfolio whose duration is equal to the time of 
the liability and whose present value is equal to the present value of the 
liability. This portfolio will be insensitive to small parallel shifts of the 
term structure of interest rates. 
We can now extend and generalize this reasoning. Consider a 
stream of liabilities Lt. Our objective is to match this stream of liabili-
ties with a stream of cash flows from some initial investment insensitive 
to changes in interest rates. First we want to prove that the present 
value of liabilities and of cash flows must match. Consider the frame-
work of CMF with reinvestment but no borrowing: 
∑αiKi t + (1 + ρt)rt – 1 = Lt + rt
, 
i ∈ U 
∑αiKi t – Lt ≥ 0 
, 
i ∈ U 
ai ≥ 0; i ∈ U 
We can recursively write the following relationships: 
∑αiKi, 1 – Lt = r1 
i ∈ U 
∑αiKi, 2 + (1 + ρ2) ∑ αiKi, 1 = (1 + ρ2)L1 + L2 + r2 
i ∈ U
i ∈ U 

670 
The Mathematics of Financial Modeling and Investment Management 
… 
n
m 
m 
∑αiKi, 1 ∏(1 + ρt) + …
αiKi m
= L1 ∏(1 + ρ ) + … + L
+ 
, 
t
m 
i = 1 
t = 2 
t = 2 
ai ≥0; i ∈U 
If we divide both sides of the last equation by 
∏ 
m 
(1 + ρt) 
t = 2 
we see that the present value of the portfolio’s stream of cash flows must 
be equal to the present value of the stream of liabilities. We can rewrite 
the above expression in continuous-time notation as 
n 
–r t
+ 
m m
∑[αiKi, 1 + …
αiKi me 
–rmtm] = L1 + … + L e 
, 
m
i = 1 
As in the case of CFM, if cash flows and liabilities do not occur at the 
same dates, we can construct an enlarged model with more dates. At 
these dates, cash flows or liabilities can be zero. 
To see under what conditions this expression is insensitive to small 
parallel shifts of the term structure, we perturb the term structure by a 
small shift r and compute the derivative with respect to r for r = 0. In 
this way, all rates are written as rt + r. If we compute the derivatives we 
obtain the following equation: 
n 
m
m]
+
d ∑[αiKi, 1 + …
αiKi me 
–(r
+ r)t
[ 
–(r
+ r)tm]
, 
d L1 + … + L e 
m 
i = 1 
m
------------------------------------------------------------------------------------------------ = -------------------------------------------------------------------
dr 
dr 
n 
–(r
+ r)t
+ 
m
m 
m 
– ∑[αiKi, 1 + …
αiKi mt e 
–(r
+ r)t ] = –[L1 + … + L t e 
m]
, 
m
m m 
i = 1 
which tells us that the first-order conditions for portfolio immunization 
are that the duration of the cash flows must be equal to the duration of 

671 
Bond Portfolio Management 
the liabilities. This duration is intended in the sense of effective duration 
which allows for a shift in the term structure. This condition does not 
determine univocally the portfolio. 
To determine the portfolio, we can proceed in two ways. The first is 
through optimization. Optimization calls for maximizing some function 
subject to constraints. In the CFM problem there are two constraints: 
(1) The initial present value of cash flows must match the initial present
value of liabilities, and (2) the duration of cash flows must match the 
duration of liabilities. A typical objective function is the portfolio’s 
return at the final date. It can be demonstrated that this problem can be 
approximated by an LP problem. 
Optimization might not be ideal as the resulting portfolio might be 
particularly exposed to the risk of nonparallel shifts of the term struc-
ture. In fact, it can be demonstrated that the result of the yield maximi-
zation under immunization constraints tends to produce a barbell type 
of portfolio. A barbell portfolio is one in which the portfolio is concen-
trated at short-term and long-term maturity securities. A portfolio of 
this type is particularly exposed to yield curve risk, i.e., to the risk that 
the term structure changes its shape, as described in Chapter 20. 
One way to control yield curve risk is to impose second-order con-
vexity conditions. In fact, reasoning as above and taking the second 
derivative of both sides, it can be demonstrated that, in order to protect 
the portfolio from yield curve risk, the convexity of the cash flow stream 
and the convexity of the liability stream must be equal. (Recall from 
Chapter 4 that mathematically convexity is the derivative of duration.) 
This approach can be generalized16 by assuming that changes of interest 
rates can be approximated as a linear function of a number of risk fac-
tors. Under this assumption we can write 
k 
∆rt = ∑βj t∆
εt
+ 
, 
fj 
j = 1 
where the fj are the factors and εt is an error term that is assumed to be 
normally distributed with zero mean and unitary variance. Factors here 
are a simple discrete-time instance of the factors we met in the description 
of the term structure in continuous time in Chapter 19. There we assumed 
that interest rates were an Itô process function of a number of other Itô 
processes. Here we assume that changes in interest rates, which are a dis-
crete-time process, are a linear function of other discrete-time processes 
called “factors.” Each path is a vector of real numbers, one for each date. 
16 See Stavros Zenios, Practical Financial Optimization, unpublished manuscript. 

672 
The Mathematics of Financial Modeling and Investment Management 
Ignoring the error term, changes in the present value of the stream of cash 
flows are therefore given by the following expression: 
n 
+ 
m m
∆V = – ∑[αiKi, 1 + …
αiKi mt e 
–r t ∆r ]
, 
m
m 
i = 1 
n
k 
= – ∑αiKi, 1 + …
αiKi mt e 
–rmtm ∑βj tm ∆fj
+ 
, 
m
, 
i = 1 
j = 1 
The derivative of the present value with respect to one of the factors 
is therefore given by 
n 
∂V 
+ 
e 
m m 
,
, 
------- = – ∑αiKi, 1 + …
αiKi mtmβj tm 
–r t
∂fj 
i = 1 
The factor duration with respect to the j-th factor is defined as the rela-
tive value sensitivity to that factor: 
1 ∂V 
= --- -------
kj 
V ∂fj 
The second derivative represents convexity relative to a factor: 
1 ∂2V 
= --- ---------
Qj 
V ∂f2 
j 
First- and second-order immunization conditions become the equality of 
factor duration and convexity relative to cash flows and liabilities. 
Scenario Optimization 
The above strategies are based on perturbing the term structure of inter-
est rates with a linear function of one or more factors. We allow sto-
chastic behavior as rates can vary (albeit in a controlled way through 
factors) and impose immunization constraints. We can obtain a more 
general formulation of a stochastic problem in terms of scenarios.17 Let 
the variables be stochastic but assume distributions are discrete. Scenar-
17 Ron Dembo, “Scenario Immunization,” in Financial Optimization. 

673 
Bond Portfolio Management 
ios are joint paths of all the relevant variables. A probability number is 
attached to each scenario. A path of interest rates is a scenario. If we 
consider corporate bonds, a scenario will be formed, for example, by a 
joint path of interest rates and credit ratings. How scenarios are gener-
ated will be discussed later in this chapter. 
Suppose that scenarios are given. Using an LP program, one can find 
the optimal portfolio that (1) matches all the liabilities in each scenario 
and (2) minimizes initial costs or maximizes final cash positions subject 
to budget constraints. The CFM problem can be reformulated as follows: 
Minimize ∑αiPi , subject to the constraints 
i ∈ U 
s 
s
s 
s
s 
s
s
s
∑αiKi t + (1 + ρt )rt – 1 + bt = Lt + (1 + βt )bt – 1 + rt
, 
i ∈ U 
bs = 0
m 
ai ≥ 0; i ∈ U 
In this formulation, all terms are stochastic and scenario dependent 
except the portfolio’s weights. Each scenario imposes a constraint. 
Scenario optimization can also be used in a more general context. 
One can describe a general objective, for instance expected return or a 
utility function, which is scenario-dependent. Scenario-dependent con-
straints can be added. The optimization program maximizes or mini-
mizes the objective function subject to the constraints. 
Stochastic Programming 
Strategies discussed thus far are static (or myopic) in the sense that deci-
sions are made initially and never changed. As explained in Chapter 7, 
stochastic programming (or multistage stochastic optimization) is a 
more general, flexible framework in which decisions are made at multi-
ple stages, under uncertainty, and on the basis of past decisions and 
information then available. Both immunization and CFM discussed 
above can be recast in the framework of stochastic programming. 
Indeed, multistage optimization is a general framework that allows one 
to formulate most problems in portfolio management, not only for 
bonds but also for other asset classes including stocks and derivatives. 
Stochastic programming is a computerized numerical methodology to 
solve variational problems. A variational principle is a law expressed as the 

674 
The Mathematics of Financial Modeling and Investment Management 
maximization of a functional, with a functional being a real-valued func-
tion defined over other functions. Most classical physics can be expressed 
equivalently through differential equations or variational principles. 
Variational methodologies also have important applications in engi-
neering, where they are used to select a path that maximizes or mini-
mizes a functional given some exogenous dynamics. For example, one 
might want to find the optimal path that an airplane must follow in 
order to minimize fuel consumption or flying time. The given dynamics 
are the laws of motion and eventually specific laws that describe the 
atmosphere and the behavior of the airplane. 
Economics and finance theory have inherited this general scheme. 
General equilibrium theories can be expressed as variational principles. 
However, financial applications generally assume that some dynamics 
are given. In the case of bond portfolios, for example, the dynamics of 
interest rates are assumed to be exogenously given. The problem is to 
find the optimal trading strategy that satisfies some specific objective. In 
the case of immunization an objective might be to match liabilities at 
the minimum cost with zero exposure to interest rates fluctuations. The 
solution is a path of the portfolio’s weights. In continuous time, it 
would be a continuous trading strategy. 
Such problems are rarely solvable analytically; numerical techniques, 
and in particular multistage stochastic optimization, are typically 
required. The key advantage of stochastic programming is its ability to 
optimize on the entire path followed by exogenously given quantities. In 
applications such as bond portfolio optimization, this is an advantage 
over myopic strategies which optimize looking ahead only one period. 
However, because stochastic programming works by creating a set of sce-
narios and choosing the scenario that optimizes a given objective, it 
involves huge computational costs. Only recently have advances in IT 
technology made it feasible to create the large number of scenarios 
required for stochastic optimization. Hence there is a renewed interest in 
these techniques both at academia and inside financial firms.18 
Scenario Generation 
The generation of scenarios (i.e., joint paths of the stochastic variables) is 
key to stochastic programming. Until recently, it was imperative to create 
a parsimonious system of scenarios. Complex problems could be solved 
only on supercomputers or massively parallel computers at costs prohibi-
tive for most organizations. While parsimony is still a requirement, sys-
18 A presentation of stochastic programming in finance can be found in Zenios, Prac-
tical Financial Optimization, forthcoming. 

675 
Bond Portfolio Management 
tems made of thousands of scenarios can now be solved on desk-top 
machines. Two well-known scenario systems in practical use are SPAN, a 
16-scenario system developed by the Chicago Mercantile Exchange and 
New York 7, a 7-scenario system use by New York insurance regulators 
(National Association of Insurance Commissioner scenarios). 
As a general requirement, scenarios must be both “complete” and 
“coherent.” Completeness means that scenarios must capture the business-
as-usual situations as well the extremes. Coherence means that scenarios 
must respect the conditions typical of many financial variables. For 
instance, some financial variables are perfectly anti-correlated, a condition 
that must be respected by scenarios. Financial and economic scenarios 
must also be free from anticipation of information. A natural way to make 
nonanticipative scenarios is the use of information structures as described 
in Chapter 5. Information structures require that scenarios are indistin-
guishable up to a given date and then part in a treelike structure. 
Consider the generation of interest rates scenarios. This is a prob-
lem that can be solved starting from a model of the term structure of 
interest rates. Continuous-time models of interest rates were introduced 
in Chapter 15. To create scenarios, these models need to be discretized 
as discussed in Chapter 15. Recall that there are different ways of dis-
cretizing a continuous-time model. For example, a Brownian motion 
can be simulated as a random walk whose increments are random draws 
from a normal distribution. Alternatively, one can adopt a binomial 
approximation to the Brownian motion. The first procedure creates a 
random sampling from a continuous distribution while the second pro-
duces a discrete-time, discrete-state model. 
If we consider only risk-free bonds, the information contained in the 
interest rate processes is sufficient to create scenarios. A large number of 
scenarios can be created either by sampling or with discrete models. If, 
in contrast, we want to consider bonds with default risk, then we need 
to generate scenarios according to a specified model of credit risk (see 
Chapter 22). For example, if we use a rating process, we need to simu-
late a rating process for each bond taking into consideration correla-
tions. It is clear that we immediately run into computational difficulties, 
because the number of scenarios explodes even for a modest number of 
bonds. Drastic simplifications need to be made to make problems tracta-
ble. Simplifications are problem-dependent. 
Multistage Stochastic Programming 
After creating scenarios one can effectively optimize, taking into account 
that after initial decisions there will be recourses (i.e., new decisions even-

676 
The Mathematics of Financial Modeling and Investment Management 
tually on a smaller set of variables) at each subsequent stage. Here we 
provide a brief description of multistage stochastic optimization.19 
The key idea of stochastic programming is that at every stage a deci-
sion is made based on conditional probabilities. Scenarios form an informa-
tion structure so that, at each stage, scenarios are partitioned. Conditional 
probabilities are evaluated on scenarios that belong to each partition. For 
this reason, stochastic optimization is a process that runs backwards. Opti-
mization starts from the last period, where variables are certain, and then 
conditional probabilities are evaluated on each partition. 
To apply optimization procedures, an equivalent deterministic prob-
lem needs to be formulated. The deterministic equivalent depends on the 
problem’s objective. Taking expectations naturally leads to deterministic 
equivalents. A deterministic equivalent of a stochastic optimization 
problem might involve maximizing or minimizing the conditional 
expectation of some quantity at each stage. 
We will illustrate stochastic optimization in the case of CFM as a 
two-stage stochastic optimization problem. The first decision is made 
under conditions of uncertainty, while the second decision at step 1 is 
made with certain final values. This problem could be equivalently for-
mulated in a m-period setting, admitting perfect foresight after the first 
period. This two-stage setting can then be extended to a true multistage 
setting. At the first stage there will be a new set of variables. In this case, 
the new variables will be the portfolio’s weights at stage 1. Call S the set 
of scenarios. Scenarios are generated from an interest rate model. A 
probability ps, s ∈ S is associated with each scenario s. The quantity to 
optimize will be the expected value of final cash. The two-stage stochas-
tic optimization problem can be formulated as follows: 
Maximize ∑ psh , subject to the constraints
s 
s ∈ S 
∑αiKi, 0 + b0 + B = r0 
i ∈ U 
s 
s
s 
s
s 
s
s
s
∑αiKi t + (1 + ρt )rt – 1 + bt = Lt + (1 + βt )bt – 1 + rt
, 
i ∈ U 
s
s
∑αiPi = ∑γ iPi 
i ∈ U
i ∈ U 
19 For a full account of stochastic programming in finance, Zenios, Practical Finan-
cial Optimization. 

677 
Bond Portfolio Management 
bs = 0
m 
s 
r
= hs 
m 
αi, γi ≥ 0; i ∈ U 
The first condition is the initial budget constraint, which tells us 
that the initial investment (which has a negative sign) plus the initial 
borrowing plus the initial budget B is equal to the first surplus. The sec-
ond condition is the liability-matching condition. The third condition is 
the self-financing condition. Note that as interest rates are known in 
each scenario, bond prices are also known in each scenario. The fifth 
and sixth conditions are the statements that there is no borrowing at the 
final stage and that the objective is the final cash. The seventh condition 
is the constraint that weights are nonnegative at each stage 
This formulation illustrates all the basic ingredients. The problem is 
formulated as a deterministic equivalent problem, setting as its objective 
the maximization of final expected cash. The final stage is certain and 
the process is backward. With this objective, the stochastic optimization 
problem is recast as an LP problem. 
This formulation can be extended to an arbitrary number of stages. 
Formulating in full generality a multistage stochastic optimization prob-
lem is beyond the scope of this book. In fact, there are many technical 
points that need a careful handling.20 
SUMMARY 
■ Bond market indexes can be classified as broad-based bond market 
indexes and specialized bond market indexes.
 ■ Bond management strategies range from pure bond index matching to 
active management.
 ■ Pure bond index matching strategy involves the least risk of underper-
forming a bond market index.
 ■ Enhanced indexing strategies involve constructing portfolios to match 
the primary risk factors associated with a bond market index without 
acquiring each issue in the index. 
20 See, for example, Peter Kall and Stein W. Wallace, Stochastic Programming 
(Chichester, U.K.: John Wiley & Sons, 1994). 

678 
The Mathematics of Financial Modeling and Investment Management
 ■ Active bond strategies attempt to outperform the bond market index 
by intentionally constructing a portfolio that will have a greater index 
mismatch than in the case of enhanced indexing.
 ■ Tracking error, or active risk, is the standard deviation of a portfolio’s 
return relative to the return of the benchmark index.
 ■ Systematic risk factors are the common factors that affect all securities 
in a certain category in the benchmark bond market index.
 ■ Nonsystematic factor risk is the risk that is not attributable to the sys-
tematic risk factors.
 ■ Systematic risk factors are divided into term structure risk factors and 
nonterm structure risk factors.
 ■ Given the risk factors associated with a benchmark index, forward-
looking tracking error can be estimated.
 ■ A multifactor risk model can be used by the portfolio manager in com-
bination with optimization in constructing and rebalancing a portfolio 
to reduce tracking error.
 ■ Optimization is generally done step-by-step based on marginal contri-
butions of each security.
 ■ Liability-funding strategies are strategies whose objective is to match a 
given set of liabilities due at future times.
 ■ Cash flow matching in a deterministic environment is the problem of 
matching a predetermined set of liabilities with an investment portfolio 
that produces a deterministic stream of cash flows.
 ■ Cash flow matching problems can be solved with linear programming 
or mixed-integer programming algorithms.
 ■ The objective of an immunization strategy is to construct a portfolio 
that is insensitive to small parallel shifts of interest rates.
 ■ A given stream of liabilities can be matched with a portfolio whose 
duration is equal to the duration of the liabilities and whose present 
value is equal to the present value of the liabilities.
 ■ Matching duration and present value makes portfolios insensitive only 
to small parallel shifts of interest rates; in order to minimize the effects 
of nonparallel shifts, optimization procedures are needed.
 ■ Scenario optimization optimizes on a number of representative scenar-
ios.
 ■ Multistage stochastic optimization deals with the problem of optimiza-
tion when there is recourse, that is, when decisions are made at each 
stage.
 ■ Taking expectations at each stage, stochastic optimization becomes a 
problem of deterministic optimization. 

