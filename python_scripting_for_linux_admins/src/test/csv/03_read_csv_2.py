import csv

req_file="/home/skypper/Projects/eLearning/python/python_scripting_for_linux_admins/sample.csv"

file_object=open(req_file,"r")
file_rows=csv.reader(file_object,delimiter=";")

for lines in file_rows:
  print(lines)
file_object.close()