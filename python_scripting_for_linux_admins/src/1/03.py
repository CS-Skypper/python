#!/usr/bin/env python3

import os, argparse

parser = argparse.ArgumentParser()
parser.add_argument( '--dir', '-d', help='Enter directory name', default='/etc/')
args = parser.parse_args()
dir_path = args.dir

for file in os.listdir(dir_path):
  if os.path.isfile(dir_path + file):
    print(file)
