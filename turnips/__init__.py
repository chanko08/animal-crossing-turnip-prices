from turnips import patterns


def prediction_to_str(week, prediction, prediction_type, base_price):
    values = []
    for i, r in enumerate(prediction):
        v = f"{r[0]}..{r[1]}"
        values.append(v)
    
    return f"{prediction_type} | {base_price} | " + " | ".join(values)

def find_pattern_matches(week, buy_price):

    base_prices = range(90, 111)
    base_prices = [buy_price]
    
    for pattern_type, pattern in patterns.all_patterns.items():
        matches = find_matches(week, pattern, buy_price)

        if matches:
            for m in matches:
                print(prediction_to_str(week, m, pattern_type, buy_price))
                input()    
    
    
def find_matches(week, pattern, base_price):
    def matches_price(week, price):
        for i, value in week.items():
            if value is None: pass
            if value < price[i][0] or value > price[i][1]:
                return False
        return True

    return [ p for p in pattern(base_price) if matches_price(week, p) ] 