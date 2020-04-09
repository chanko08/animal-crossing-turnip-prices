from turnips.patterns import decrease
from turnips.patterns import decrease_spike_decrease
from turnips.patterns import decrease_spike_low
from turnips.patterns import high_low


all_patterns = {
    "high, decrease, high, decrease, high": high_low.pattern,
    "decrease, spike, low": decrease_spike_low.pattern,
    "decrease": decrease.pattern,
    "decrease, spike, decrease": decrease_spike_decrease.pattern,
}

def consolidate_predictions(predictions):
    pattern = {}

    for prices in predictions:
        for i, price in enumerate(prices):
            if i not in pattern:
                pattern[i] = price
            
            min_price_point = min(pattern[i][0], price[0])
            max_price_point = max(pattern[i][1], price[1])
            pattern[i] = (min_price_point, max_price_point)
    
    return [r for _, r in sorted(pattern.items(), key=lambda x: x[0])]

def replace_predictions_with_data(sell_prices, prediction):
    p = []
    for i, r in enumerate(prediction):
        if i in sell_prices:
            p.append((sell_prices[i], sell_prices[i]))
            continue
        p.append(r)
    
    return p

def prediction_rates_to_str(prediction):
    return [rate_to_str(r) for r in prediction]

def rate_to_str(r):
    if r[0] == r[1]: return str(r[0])
    return f"{r[0]}..{r[1]}"