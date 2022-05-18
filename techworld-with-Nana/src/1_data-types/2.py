

# refactor this code using functions
s = "seconds"
m = "minutes"
calculation_to_minutes = 24 * 60
calculation_to_seconds = 24 * 60 * 60

print(f"50 days are {50 * calculation_to_seconds} {s}")
print(f"50 days are {50 * calculation_to_minutes} {m}")
print(f"35 days are {35 * calculation_to_minutes} {m}")



# functions

# defining the function
def days_to_units():
  print(f"50 days are {50 * calculation_to_seconds} {s}")
  print(f"All good!")

# calling the function in order to execute its code
# "making a function call"
days_to_units()


# function parameters (also called as arguments)

def days_to_units(number_of_days):
  print(f"{number_of_days} days are {number_of_days * calculation_to_seconds} {s}")
  print(f"All good!")

days_to_units(35)
days_to_units(45)
days_to_units(55)



def days_to_units(number_of_days, custom_message):
  print(f"{number_of_days} days are {number_of_days * calculation_to_seconds} {s}")
  print(custom_message)

days_to_units(35, "Awsome")
days_to_units(45, "Awsome")
days_to_units(55, "Awsome")





