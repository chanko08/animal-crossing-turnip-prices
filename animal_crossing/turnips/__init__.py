from animal_crossing.turnips import patterns

from animal_crossing.turnips.prediction import Prediction
from animal_crossing.turnips.price import PriceRange

def predict(buy_price, sell_prices):
    predictions = []
    for pattern_name, pattern in patterns.ALL_PATTERNS.items():
        p = Prediction.with_pattern(buy_price, pattern_name.value, pattern).with_sell_prices(sell_prices).consolidate().replace_ranges_with_data(sell_prices)
        predictions.append(p)
    return predictions