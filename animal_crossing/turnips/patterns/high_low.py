import itertools
from animal_crossing.turnips.price import prices

def rates_high(num_price_periods):
    return itertools.repeat((0.9, 1.4), num_price_periods)

def rates_low(num_price_periods):
    assert num_price_periods > 1

    rate_range = (0.6, 0.8)
    yield rate_range

    for i in range(num_price_periods - 1):
        rate_range = (rate_range[0] - 0.04 - 0.06, rate_range[1] - 0.04)
        yield rate_range

# high, low, high, low, high
def pattern(base_price):
    high_phase_lengths = [(a,b,c) for a in range(7) for b in range(7) for c in range(7) if a+b+c==7 and b > 0]
    low_phase_lengths = [(2,3), (3,2)]

    for lows in low_phase_lengths:
        for highs in high_phase_lengths:
            highs_price = tuple([prices(base_price, rates_high(x)) for x in highs])
            lows_price = tuple([prices(base_price, rates_low(x)) for x in lows])
            
            week = list(itertools.chain(
               highs_price[0],
               lows_price[0],
               highs_price[1],
               lows_price[1],
               highs_price[2],
            ))

            yield week