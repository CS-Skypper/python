my_set = {"January", "February", "March", "April", "May", "June"}

def run(iterable):
  for month in my_set:
    print(month)

# adde elements to set
my_set.add("July")

# remove items from the set
my_set.remove("January")

run(my_set)
