# refactoring the code with while loop so it does not exit the script so the user can provide more inputs


import sys


calculation_to_units = 24
unit = "hours"


# validate user input using conditional statemets
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {unit}"


def validate_and_execute():
  try:
    user_input_number = int(user_input)
    if user_input_number > 0:
      calculated_value = days_to_units(user_input_number)
      print(calculated_value)
    elif user_input_number == 0:
      print("For this calculation provide a number greater than 0")     
    else:
      print("Could not convert negative values")
  except ValueError:
    print("Your input is not valid. Provide an integer")
    sys.exit(1)


# it will run indefinitely
#while True:
# we need to create the user_input var before the while loop
user_input = ""
while user_input != "exit":
  user_input = input("Provide the number of days that it will be converted in hours \n")
  validate_and_execute()
