# user input
user_input = input("Provide the number of days that it will be converted in minutes \n")

def days_to_units(number_of_days):
  number_of_days = user_input
  s = "seconds"
  m = "minutes"
  calculation_to_minutes = 24 * 60
  calculation_to_seconds = 24 * 60 * 60
  
  # hmmm...
  return f"{number_of_days} days are {type({number_of_days})} * {calculation_to_seconds} {s}"
  print(f"{number_of_days} days are {number_of_days} * {calculation_to_seconds} {s}")

  # works
  total = int(number_of_days) * int(calculation_to_seconds)
  print(f"{number_of_days} days are {total} {s}")

#var = days_to_units()
print(days_to_units(user_input))


# user_input = input("Provide the number of days that it will be converted in minutes \n")

# def days_to_units(number_of_days):
#   number_of_days = user_input
#   s = "seconds"
#   m = "minutes"
#   calculation_to_minutes = 24 * 60
#   calculation_to_seconds = 24 * 60 * 60

#   return f"{number_of_days} days are {number_of_days * calculation_to_seconds} {s}"

# var = days_to_units(user_input)

# print(var)








# 