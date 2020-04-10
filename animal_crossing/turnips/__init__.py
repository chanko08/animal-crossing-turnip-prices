from animal_crossing.turnips import patterns

from animal_crossing.turnips.prediction import Prediction
from animal_crossing.turnips.price import PriceRange

def predict(buy_price, sell_prices, show_empty_patterns=False):
    predictions = []
    for pattern_name, pattern in patterns.ALL_PATTERNS.items():
        p = Prediction.with_pattern(buy_price, pattern_name.value, pattern).with_sell_prices(sell_prices).consolidate().replace_ranges_with_data(sell_prices)
        if show_empty_patterns or p:
            predictions.append(p)
    return predictions