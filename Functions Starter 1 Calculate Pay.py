#Jordan Russell
#14/11/14
#Functions Starter 1 - Calculate pay

hours_worked = int(input("Please input how many hours you have worked this week: "))
hourly_wages = float(input("Please input your hourly wages: "))
if hours_worked > 40:
    extra_hours = hours_worked - 40
    basic_pay = round(hourly_wages * 40, 3)
    extra_pay = round(extra_hours * hourly_wages, 3)
    total_pay = round(basic_pay + extra_pay, 3)
    print("This week you earned £{0}, and your extra pay is £{1}. Your total pay is £{2}.".format(basic_pay, extra_pay, total_pay))
elif hours_worked <= 40:
    total_pay = round(hours_worked * hourly_wages, 3)
    print("This week you earned £{0}.".format(total_pay))
    
