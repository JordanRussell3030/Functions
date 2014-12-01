#Jordan Russell
#1/12/14
#Functions Revision Task 4

def input_fahrenheit():
    fahrenheit = float(input("Please input the temperature in Fahrenheit: "))
    return fahrenheit

def convert_value(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius

def output_celsius(celsius):
    print(celsius)

fahrenheit = input_fahrenheit()
celsius = convert_value(fahrenheit)
output_celsius(celsius)
