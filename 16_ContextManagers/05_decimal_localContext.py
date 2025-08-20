from decimal import Decimal, localcontext

with localcontext() as ctx:
    ctx.prec = 4
    print(Decimal(1) / Decimal(3))  # prints 0.3333
# outside the with, precision resets to default
