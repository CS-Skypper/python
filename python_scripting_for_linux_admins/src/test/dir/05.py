#!/usr/bin/python

import os

# get the dir from the user
print("The current working dir is: ",os.getcwd())
req_path=input("Enter the path to change working directory: ")
try:
  os.chdir(req_path)
  print("The current working directory is: ",os.getcwd())
except FileNotFoundError:
  print("Please verify the given path")
except NotADirectoryError:
  print("Given path is a file path")
except PermissionError:
  print("Error: This command has to be run with superuser privileges (under the root user on most systems).")
