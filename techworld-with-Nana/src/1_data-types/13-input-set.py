# refactoring the code with while loop so it does not exit the script so the user can provide more inputs

# refactoring the codeto use a set data type instead of a list
# a set is a list with unique elements

import sys


calculation_to_units = 24
unit = "hours"


# validate user input using conditional statemets
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {unit}"


def validate_and_execute():
  try:
    user_input_number = int(num_of_days_element)

    # we want to do conversion only for positive integer
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


# provide a list of values to the app:
# my_list = [1, 2, 3, 4, 5]


# how to get each element of the list?


# we need to create the user_input var before the while loop
user_input = ""
while user_input != "exit":
  user_input = input("Provide the number of days that it will be converted in hours \n")
  # .split() => we are calling this function on user_input var
  # .split() => converts the string in list data type
  # .split() => we should provide as input integers separated by " " space bar
  # however we can overwrite the default separator
  # also the trailing spaces are included as element of the list so we need to split also on ", " coma and space
  list_of_days = user_input.split(", ")
  print(list_of_days)
  print(type(list_of_days))
  for num_of_days_element in set(list_of_days):
    validate_and_execute()
