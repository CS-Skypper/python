#!/usr/bin/env python3

import os, sys

try:
  dir_path = sys.argv[1]
except:
  dir_path = '/etc/'

for file in os.listdir(dir_path):
  if os.path.isfile(dir_path+file):
    print(file)
