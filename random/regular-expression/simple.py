import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'
#                   "r" for raw string
# pattern = re.compile(r'\bHa')
# pattern = re.compile(r'\BHa')
# pattern = re.compile(r'^Start') # matches = pattern.finditer(sentence)
# pattern = re.compile(r'end&')   # matches = pattern.finditer(sentence)

# match the phone numbers
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
#                            character set "[]" ; it is literal "." (\.) ; inside the brackets it means "either this or that"
#                            this character set will not match the numbers separated by *
pattern = re.compile(r'\d\d\d[-.]\d\d\d[.-]\d\d\d\d')
# match only the phone numbers starting goruped by 800 or 900
pattern = re.compile(r'[89]00[-.]\d\d\d[.-]\d\d\d\d')
#                       the carat inside a character set it negates the set "wvery thing but the set"
pattern = re.compile(r'[^a-zA-Z]')
pattern = re.compile(r'[^b]at')

pattern = re.compile(r'[89]00[-.]\d\d\d[.-]\d\d\d\d')       # check snippets.txt
pattern = re.compile(r'\d{3}[-.]\d{3}[.-]\d{3,4}')
pattern = re.compile(r'\d{3}[.]\d{3}[.]\d{3,4}')
pattern = re.compile(r'\d{3}.\d{3}.\d{3,4}')

matches = pattern.finditer(text_to_search)
# for match in matches:
#   print(match)

with open('data.txt', 'r', encoding='utf-8') as f:
  contents = f.read()
  matches = pattern.finditer(contents)
  for match in matches:
    print(match)

# print(text_to_search[1:4])

# # raw string
# print(r'tTab')
# print('\tTab')
