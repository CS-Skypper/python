import sys


# validate user input using conditional statemets
def days_to_units(num_of_days, conversion_unit):
  if conversion_unit == "hours":
    return f"{num_of_days} days are {num_of_days * 24} hours"
  elif conversion_unit == "minutes":
    return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
  else:
    return "curently unsupported unit"

def validate_and_execute():
  try:
    user_input_number = int(days_and_unit_dict["days"])

    # we want to do conversion only for positive integer
    if user_input_number > 0:
      calculated_value = days_to_units(user_input_number, days_and_unit_dict["unit"])
      print(calculated_value)
    elif user_input_number == 0:
      print("For this calculation provide a number greater than 0")     
    else:
      print("Could not convert negative values")
  except ValueError:
    print("Your input is not valid. Provide an integer")
    sys.exit(1)


user_input = ""
while user_input != "exit":
  user_input = input("Provide the number of days and coversion unit; ex: 56:hours \n")
  days_and_unit = user_input.split(":")
  print(days_and_unit)
  days_and_unit_dict = {"days":days_and_unit[0], "unit":days_and_unit[1]}
  print(days_and_unit_dict)
  validate_and_execute()