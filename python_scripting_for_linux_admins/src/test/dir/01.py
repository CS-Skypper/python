import os

dir_path = "/etc/"

for dir in os.listdir(dir_path):
  if os.path.isfile(dir_path + dir):
    print(dir)



# python -c "print(8*3)"
