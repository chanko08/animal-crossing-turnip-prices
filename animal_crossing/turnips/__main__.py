import argparse
import animal_crossing.turnips as turnips
import animal_crossing.turnips.price as price

def main():
    argp = argparse.ArgumentParser(prog="turnips")

    argp.add_argument("-buy-price", type=int, required=True, help="The price turnips was bought at on Sunday")
    argp.add_argument("-sell-prices", type=price.from_str, required=True, help="Comma-seperated list of the values observed in the week starting on Monday. Use zero to delimit unknown values between known values.")
    args = argp.parse_args()
    
    predictions = turnips.predict(args.buy_price, args.sell_prices)

    for p in predictions:
        print(p)


if __name__ == "__main__": main()