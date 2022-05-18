# refactoring the code that we do vlaidations only in once function
# it is not recommended to nest if statemets but some times it is necessary
# (this time it isn't. check 7.py)


import sys


calculation_to_units = 24
unit = "hours"

user_input = input("Provide the number of days that it will be converted in hours \n")


# validate user input using conditional statemets
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {unit}"


def validate_and_execute():
  if user_input.isdigit():
    user_input_number = int(user_input)
    if user_input_number > 0:
      calculated_value = days_to_units(user_input_number)
      print(calculated_value)
    elif user_input_number == 0:
      print("For this calculation provide a number greater than 0")
  else:
    print("Could not convert negative values")
    sys.exit(1)


validate_and_execute()
