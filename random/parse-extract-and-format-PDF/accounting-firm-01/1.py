import re
import pdfplumber
import pandas as pd


pdf = "buccianti-2018.pdf"

with pdfplumber.open("buccianti-2018.pdf") as pdf:
  page = pdf.pages[1]
  text = page.extract_text()
  print(text)

operation_number = re.compile(r'^\d')

for line in text.split('\n'):
  if operation_number.match(line):
    print(line)
