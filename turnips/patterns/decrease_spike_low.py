import itertools
from turnips.patterns.prices import prices

def rates_decreasing(num_price_periods):
    assert num_price_periods > 0

    rate_range = (0.85, 0.9)
    yield rate_range

    for i in range(num_price_periods - 1):
        rate_range = (rate_range[0] - 0.03 - 0.02, rate_range[1] - 0.03)
        yield rate_range

def rates_spike():
    return iter([
        (0.9, 1.4),
        (1.4, 2.0),
        (2.0, 6.0),
        (1.4, 2.0),
        (0.9, 1.4)
    ])


def rates_low(num_price_periods):
    return itertools.repeat((0.4, 0.9), num_price_periods)

# decreasing, high spike, random low
def pattern(base_price):
    phase_lengths = [(a, 7 - a) for a in range(1, 7)]

    for phases in phase_lengths:
        phase_decreasing = prices(base_price, rates_decreasing(phases[0]))
        phase_spike = prices(base_price, rates_spike())
        phase_low = prices(base_price, rates_low(phases[1]))

        week = list(itertools.chain(
            phase_decreasing,
            phase_spike,
            phase_low
        ))

        yield week