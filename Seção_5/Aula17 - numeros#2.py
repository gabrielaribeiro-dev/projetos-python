from decimal import Decimal, getcontext
print(Decimal(1) / Decimal(7))
getcontext().prec = 4
print(Decimal(1) / Decimal(7))
result = Decimal.max(Decimal(1), Decimal(7))
print(result)
1.1 + 2.2
print(Decimal(1.1) + Decimal(2.2))