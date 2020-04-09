import argparse
import animal_crossing.turnips as turnips

def prediction_to_str(week, prediction, prediction_type, base_price):
    values = []
    for i, r in enumerate(prediction):
        v = f"{r[0]}..{r[1]}"
        values.append(v)
    
    return f"{prediction_type} | {base_price} | " + " | ".join(values)


def prices(s):
    values = [int(v.strip()) for v in s.split(",")]

    week = {}
    for i,v in enumerate(values):
        if v < 1: continue
        week[i] = v
    
    return week


def main():
    argp = argparse.ArgumentParser(prog="turnips")

    argp.add_argument("-buy-price", type=int, required=True, help="The price turnips was bought at on Sunday")
    argp.add_argument("-sell-prices", type=prices, required=True, help="Comma-seperated list of the values observed in the week starting on Monday. Use zero to delimit unknown values between known values.")
    args = argp.parse_args()

    matches = turnips.find_pattern_matches(args.sell_prices, args.buy_price)
    if not any([len(ps) for pattern, ps in matches.items()]):
        print("No matches found for provided parameters")
        return

    print("Pattern type | Sun | Mon AM | Mon PM| Tue AM | Tue PM | Wed AM | Wed PM | Thu AM | Thu PM | Fri AM | Fri PM | Sat AM | Sat PM")
    for pattern, ps in sorted(matches.items(), key=lambda x: x[0]):
        for price in ps:
            print(prediction_to_str(args.sell_prices, price, pattern, args.buy_price))


if __name__ == "__main__": main()