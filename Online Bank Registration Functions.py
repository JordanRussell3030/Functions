#25/11/14
#Online Bank Registration Program
#Partner: Hugo

def user_information():
    print("Please enter your details below: ")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    gender = input("Gender: ")
    address = input("Address: ")
    town = input("Town: ")
    postcode = input("Postcode: ")
    return first_name, last_name, gender, address, town, postcode

def process_details(first_name, last_name, gender, address, town, postcode):
    if gender == "Male" or gender == "male" or gender == "M" or gender == "m":
        title = "Mr"
        return title
    elif gender == "Female" or gender == "female" or gender == "F" or gender == "f":
        married = input("Are you married? ")
        if married == "Yes":
            title = "Mrs"
            return title
        elif married == "No":
            title = "Ms"
            return title

def return_message(title, first_name, last_name):
    print("Thank you {0} {1} {2} for registering with our Online Bank. Registration is now complete.".format(title, first_name, last_name))

first_name, last_name, gender, address, town, postcode = user_information()
title = process_details(first_name, last_name, gender, address, town, postcode)
return_message(title, first_name, last_name)

    
