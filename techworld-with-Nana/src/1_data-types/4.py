calculation_to_units = 24
unit = "hours"


def days_to_units(num_of_days):
  return f"{num_of_days} days are {num_of_days * calculation_to_units} {unit}"


user_input = input("Provide the number of days that it will be converted in hours \n")
num_user_input = int(user_input)


calculated_value = days_to_units(num_user_input)

print(calculated_value)