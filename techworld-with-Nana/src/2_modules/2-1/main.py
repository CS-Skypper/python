#import helper # to import all the module with all his functions
# helper.validate_and_execute(days_and_unit_dict)

# import helper as h ; h.validate_and_execute ;  h.user_input_message

from helper import validate_and_execute, user_input_message

user_input = ""
while user_input != "exit":
  user_input = input(user_input_message)
  days_and_unit = user_input.split(":")
  print(days_and_unit)
  days_and_unit_dict = {"days":days_and_unit[0], "unit":days_and_unit[1]}
  print(days_and_unit_dict)
  validate_and_execute(days_and_unit_dict)