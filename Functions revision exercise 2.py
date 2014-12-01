#Jordan Russell
#25/11/14
#Functions Revision Exercise 2

def get_odd_number():
    number = int(input("Please input an odd number: "))
    if number % 2 == 0:
        print("That number is not odd. ")
    else:
        return number

def output_stars(number):
    star = "*"
    count = number
    while count in range(0, count):
        count = count - 2
        print("*{,^:}") * count

number = get_odd_number()
output_stars(number)
