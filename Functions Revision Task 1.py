def input_symbols(amount, symbol):
    amount_of_symbols = int(input("Please enter how many times you would like your symbol to appear: "))
    symbol = str(input("Please enter the symbol you would like to be displayed: "))
    return amount, symbol

def display_symbols(amount, symbol):
    print("{0}".format(symbol * amount_of_symbols))

def output_symbols():
    amount = input_symbols(amount, symbol)
    symbols = input_symbols(amount, symbol)
    display_symbols(amount, symbols)

output_symbols()
