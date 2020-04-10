from animal_crossing.turnips.price import prices

def rates_decreasing():
    rate_range = (0.9 - 0.05 ,0.9)
    yield rate_range

    for i in range(11):
        rate_range = (rate_range[0] - 0.03 - 0.02, rate_range[1] - 0.03)
        yield rate_range

# decreasing only
def pattern(base_price):
    yield list(prices(base_price, rates_decreasing()))