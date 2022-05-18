
# import the module
import argparse

# create an instance of the argparse class
parser = argparse.ArgumentParser()


parser.add_argument('name', help='Enter a name to work with', type=str)
# adding the "-" before an argument it means that it is optional
parser.add_argument('-u', '--upper', help='Convert to upper case', action='store_true')
parser.add_argument('-l', '--lower', help='Convert to lower case', action='store_true')
parser.add_argument('-t', '--title', help='Convert to title case', action='store_true')

# the list of the arguments that we passed through
# through the "parser" instance it is used the method "parse_args()"
args = parser.parse_args()

# we can access the arguments by their name and not by the index of the list
name = args.name

if args.upper:
  name = name.upper()
if args.lower:
  name = name.lower()
if args.title:
  name = name.title()


print(f'Hello {name}')