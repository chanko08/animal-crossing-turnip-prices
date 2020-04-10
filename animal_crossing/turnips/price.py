import math

class PriceRange:
    def __init__(self, low, high):
        self.low = low
        self.high = high
    
    def __str__(self):
        if self.low == self.high: return str(self.low)
        return f"{self.low}..{self.high}"
    
    def __contains__(self, value):
        if value <= self.high and value >= self.low:
            return True
        
        return False


def prices(base_price, rates):
    for r in rates:
        yield PriceRange(math.ceil(r[0] * base_price), math.ceil(r[1] * base_price))


def from_str(s):
    values = [int(v.strip()) for v in s.split(",")]

    week = {}
    for i,v in enumerate(values):
        if v < 1: continue
        week[i] = v
    
    return week
