#25/11/14
#Functions Revision Exercise 1

def output_symbols(integer, character_symbol):
    integer = int(input("Please input an integer: "))
    character_symbol = input("Please input a character: ")
    print("{0}".format(character_symbol) * integer)
    return integer, character_symbol

output_symbols(5, '#')
    
