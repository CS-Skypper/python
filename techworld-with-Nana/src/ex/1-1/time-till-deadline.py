"""
Exercise Goal
a) Accept user input of goal and deadline
b) Print back:
  How much time till deadline?
    deadline = date
  
  In order to work with dates import datetime module
"""

import datetime

user_input = input("enter your goal with a deadline separated by colon \n")
input_list =  user_input.split(" : ")

goal = input_list[0]
deadline = input_list[1]
# print(input_list)

# first `datetime` is the module; second `datetime` is a definition (better say a class) in that module
# for date format check module doc
# print(datetime.datetime.strptime(deadline, "%d.%m.%Y"))
# print(type(datetime.datetime.strptime(deadline, "%d.%m.%Y")))

# define date format: day.mont.year """having a clearer understanding of python : 02.03.2022"""
deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")

# calculate how many days from now till deadline
today = datetime.datetime.today()
time_till = deadline_date - today
#print(time_till)

# present the user with a messagge
print(f"Time remaining for your goal: {goal} is {time_till.days} days")
print(f".. or {int(time_till.total_seconds() / 60 / 60)} hours in case you wandered")

