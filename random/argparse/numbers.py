import argparse

parser = argparse.ArgumentParser()

parser.add_argument('decimal', help='Enter a decimal integer to convert', type=int)
parser.add_argument('-x', '--hex', help='Convert to hex', action='store_true')
parser.add_argument('-o', '--octal', help='Convert to ocal', action='store_true')
parser.add_argument('-b', '--binary', help='Convert to binary', action='store_true')
args = parser.parse_args()

number = args.decimal

if args.hex:
  number = '{:X}'.format(number)
if args.octal:
  number = '{:o}'.format(number)
if args.binary:
  # binary formatted as 8 bits
  number = '{:08b}'.format(number)


print(f'{number}')