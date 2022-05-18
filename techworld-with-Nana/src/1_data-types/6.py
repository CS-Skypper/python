# what if the user is giving a string? Or a float?


import sys


calculation_to_units = 24
unit = "hours"

user_input = input("Provide the number of days that it will be converted in hours \n")

if user_input.isdigit():
  num_user_input = int(user_input)
else:
  print("Provided a number input as inpput")
  sys.exit(1)


# validate user input using conditional statemets
def days_to_units(num_of_days):
  # returns Boolean (True or False)
  #print(num_of_days > 0)

  # returns the data type of the provided variable
  #condition_check = num_of_days > 0
  #print(type(condition_check))

  if num_of_days > 0:
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {unit}"
  elif num_of_days == 0:
    return "For this calculation provide a number greater than 0"
  else:
    return "Could not convert negative values"


calculated_value = days_to_units(num_user_input)
print(calculated_value)
