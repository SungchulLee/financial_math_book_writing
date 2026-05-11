# Bond Price Quote

## Background

# ======================================================================

Bond Price Quote

Educational script demonstrating bond price quote concepts.

---

## Code

```python
"""
# ======================================================================

Bond Price Quote

Educational script demonstrating bond price quote concepts.
"""

import numpy as np


if __name__ == "__main__":
    coupon = 0.01
    face_value = 100

    price = 99 + (21+3/4) / 32
    print(price)

    #                       price           continuous compounding discrete compounding
    # yield_rate = 0.0106 # 99.6796875      99.69491779393837      99.70856275264174
    yield_rate = 0.0107   # 99.6796875      99.64618584276408      99.6600821321915
    # yield_rate = 0.0108 # 99.6796875      99.59747805070536      99.61162782828589

    value_discrete_compounding = 0
    value_continuous_compounding = 0
    for i in range(1,11):
        period = 0.5 * i
        value_discrete_compounding += face_value*(coupon/2)/(1+yield_rate/2)**i
        value_continuous_compounding += face_value*(coupon/2)*np.exp(-yield_rate*period)
    value_discrete_compounding += face_value/(1+yield_rate/2)**i
    value_continuous_compounding += face_value*np.exp(-yield_rate*period)
    print(value_discrete_compounding)
    print(value_continuous_compounding)
```


## Exercises

**Exercise 1.**
A bond with face value $\$1{,}000$, coupon rate 5% (semiannual), and 10 years to maturity is quoted at 95.50. Compute the clean price in dollars.

??? success "Solution to Exercise 1"
    Clean price $= 95.50\% \times \$1{,}000 = \$955.00$. The bond trades at a discount (below par) because the market yield exceeds the coupon rate.

---

**Exercise 2.**
If the last coupon was paid 45 days ago and the coupon period is 182 days, compute the accrued interest and the dirty (invoice) price.

??? success "Solution to Exercise 2"
    Accrued interest $= \frac{45}{182} \times \frac{5\%}{2} \times \$1{,}000 = 0.2473 \times \$25 = \$6.18$. Dirty price $= \$955.00 + \$6.18 = \$961.18$.

---

**Exercise 3.**
Explain the difference between clean price, dirty price, and yield to maturity. Which is used for trading? For settlement?

??? success "Solution to Exercise 3"
    Clean price: excludes accrued interest, used for quoting and comparison across bonds. Dirty price: includes accrued interest, the actual amount paid at settlement. YTM: the internal rate of return solving $\text{dirty price} = \sum \frac{c_i}{(1+y/2)^i}$, a summary measure of return assuming reinvestment at $y$.

---

**Exercise 4.**
A zero-coupon bond maturing in 5 years is quoted at 78.35. Compute the continuously compounded yield.

??? success "Solution to Exercise 4"
    $P = e^{-yT}$, so $y = -\ln(P)/T = -\ln(0.7835)/5 = 0.2440/5 = 0.0488 = 4.88\%$.