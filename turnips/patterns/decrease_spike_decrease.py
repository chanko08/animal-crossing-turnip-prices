import itertools
from turnips.patterns.prices import prices

def rates_decreasing(num_price_periods):
    if num_price_periods <= 0: return
    
    rate_range = (0.4, 0.9)
    yield rate_range

    for i in range(num_price_periods - 1):
        rate_range = (rate_range[0] - 0.03 - 0.02, rate_range[1] - 0.03)
        yield rate_range

def rates_spike():
    yield (0.9, 1.4)
    yield (0.9, 1.4)

    yield (1.4, 2.0)
    yield (1.4, 2.0)
    yield (1.4, 2.0)


# decreasing, spike, decreasing
def pattern(base_price):
    phases = [(a, 7 - a) for a in range(8)]

    for phase in phases:
        
        phase_decreasing1 = prices(base_price, rates_decreasing(phase[0]))
        

        phase_spike = list(prices(base_price, rates_spike()))
        phase_spike[2] = (phase_spike[2][0] - 1, phase_spike[2][1] - 1)
        phase_spike[4] = (phase_spike[4][0] - 1, phase_spike[4][1] - 1)

        phase_decreasing2 = prices(base_price, rates_decreasing(phase[1]))

        week = list(itertools.chain(
            phase_decreasing1,
            phase_spike,
            phase_decreasing2
        ))

        yield week