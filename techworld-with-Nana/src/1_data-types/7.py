# refactoring the code incapsulating the logic inside functions


import sys


calculation_to_units = 24
unit = "hours"

user_input = input("Provide the number of days that it will be converted in hours \n")


def validate_and_execute():
  if user_input.isdigit():
    user_input_number = int(user_input)
    calculated_value = days_to_units(user_input_number)
    print(calculated_value)
  else:
    print("Could not convert negative values")
    sys.exit(1)

# validate user input using conditional statemets
def days_to_units(num_of_days):
  if num_of_days > 0:
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {unit}"
  elif num_of_days == 0:
    return "For this calculation provide a number greater than 0"


validate_and_execute()


# we are doing validations in two places