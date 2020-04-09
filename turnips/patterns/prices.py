import math

def prices(base_price, rates):
    for r in rates:
        yield (math.ceil(r[0] * base_price), math.ceil(r[1] * base_price))