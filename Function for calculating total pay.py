#Jordan Russell
#18/11/14
#Function for calculating overtime pay

def calculate_basic_pay(hours, pay):
    basic_pay = hours * pay
    return basic_pay

def calculate_overtime_pay(hours, pay):
    overtime_pay = (hours - 40) * (pay * 1.5)
    total = overtime_pay + (40 * pay)
    return total

def calculate_total_pay(hours, pay):
    if hours <= 40:
        total = calculate_basic_pay(hours, pay)
    else:
        total = calculate_overtime_pay(hours, pay)
    return total

def work_details():
    hours = int(input("Please enter the number of hours you have worked this week: "))
    pay = float(input("Please enter your rate of pay: "))
    return hours, pay
    
def display_total_pay(total):
    print("This week you have earned £{0}.".format(total))

def calculate_pay():
    hours, pay = work_details()
    total = calculate_total_pay(hours, pay)
    display_total_pay(total)
    return total

calculate_pay()
    

    
    
