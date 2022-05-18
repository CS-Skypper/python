import csv

req_file="/home/skypper/Projects/eLearning/python/python_scripting_for_linux_admins/sample.csv"

fo=open(req_file,"r")
content=fo.readlines()

data=csv.reader(fo)

#fo.close()

for lines in content:
  print(lines.strip("\n"))

print(data)


for lines in data:
  print(lines)
fo.close()
