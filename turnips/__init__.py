from turnips import patterns


def find_pattern_matches(week, buy_price):

    all_matches = {}
    for pattern_type, pattern in patterns.all_patterns.items():
        matches = find_matches(week, pattern, buy_price)
        all_matches[pattern_type] = matches
    return all_matches
    
    
def find_matches(week, pattern, base_price):
    def matches_price(week, price):
        for i, value in week.items():
            if value is None: pass
            if value < price[i][0] or value > price[i][1]:
                return False
        return True

    return [ p for p in pattern(base_price) if matches_price(week, p) ] 