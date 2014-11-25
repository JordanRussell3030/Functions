# functions improvement exercise
# times-table tester
import random

def detail():
    print("Times-table tester")
    print()
    test_table = input("Which times-table do you want to be tested on? ")
    test_table = int(test_table)
    return test_table

def times_table(test_table):
    for questions in range(1,6):
        Num1 = test_table
        Num2 = random.randrange(2,13)
        Ans = Num1 * Num2
        UserAnswer = input(str(Num1) + ' x ' + str(Num2) + ' = ? ')
        UserAnswer = int(UserAnswer)
        if UserAnswer == Ans:
            print('Well done, you got the correct answer!')
            print()
        else:
            print('Sorry, you got the answer wrong. The correct answer is',Ans)
            print()

test_table = detail()
times_table(test_table)
