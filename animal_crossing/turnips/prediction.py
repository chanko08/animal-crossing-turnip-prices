import textwrap
from animal_crossing.turnips.price import PriceRange

class Prediction:
    def __init__(self, base_price, pattern_name, weeks=None):
        self.base_price = base_price
        self.pattern_name = pattern_name
        self.weeks = weeks if weeks is not None else []

    def __bool__(self):
        return len(self.weeks) > 0

    def __str__(self):
        if len(self.weeks) < 1:
            msg = f"""
                Pattern: {self.pattern_name}
                =============================================
                Buy Price: {self.base_price}
                No possible predictions
            """
            msg = textwrap.dedent(msg)
            return msg

        msg = f"Pattern: {self.pattern_name}\n=============================================\nBuy Price: {self.base_price}\n"
        for i,prices in enumerate(self.weeks):
            msg_part = f"""
            ```
            Mon AM: {prices[0]}
                PM: {prices[1]}
            Tue AM: {prices[2]}
                PM: {prices[3]}
            Wed AM: {prices[4]}
                PM: {prices[5]}
            Thu AM: {prices[6]}
                PM: {prices[7]}
            Fri AM: {prices[8]}
                PM: {prices[9]}
            Sat AM: {prices[10]}
                PM: {prices[11]}    
            ```
            """
            msg_part = textwrap.dedent(msg_part)
            msg += msg_part
            msg += "\n"

        return msg
    
    def add(self, week):
        self.weeks.add(week)

    def consolidate(self):
        if len(self.weeks) == 0:
            return Prediction(self.base_price, self.pattern_name, [])

        summarized_price = {}
        for prices in self.weeks:
            for i, price in enumerate(prices):
                if i not in summarized_price:
                    summarized_price[i] = price
                
                min_price_point = min(summarized_price[i].low, price.low)
                max_price_point = max(summarized_price[i].high, price.high)
                summarized_price[i] = PriceRange(min_price_point, max_price_point)
    
        week = [r for _, r in sorted(summarized_price.items(), key=lambda x: x[0])]
        return Prediction(self.base_price, self.pattern_name, [week])

    def replace_ranges_with_data(self, sell_prices):
        tmp_weeks = []
        for w in self.weeks:
            tmp_week = [r for r in w]
            for i, sell_price in sell_prices.items():
                tmp_week[i] = PriceRange(sell_price, sell_price)

            tmp_weeks.append(tmp_week)
        
        return Prediction(self.base_price, self.pattern_name, tmp_weeks)
            

    def with_sell_prices(self, sell_prices):
        def matches_price(week):
            for i, sell_price in sell_prices.items():
                if sell_price is None: continue
                if sell_price not in week[i]:
                    return False
            
            return True

        weeks = [w for w in self.weeks if matches_price(w)]
        return Prediction(self.base_price, self.pattern_name, weeks)
    
    @staticmethod
    def with_pattern(base_price, pattern_name, pattern):
        weeks = list(pattern(base_price))
        #weeks = [ [PriceRange(low, high) for (low, high) in week] for week in weeks ]

        return Prediction(base_price, pattern_name, weeks)


