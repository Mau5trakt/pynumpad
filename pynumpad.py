#! /usr/bin/python
import argparse
import pyperclip

# Create the parser and add arguments
parser = argparse.ArgumentParser()
parser.add_argument(dest='argument1', help="This is the first argument", type=int)

# Parse and print the results

args = parser.parse_args()
#print(args.argument1)
print(chr(args.argument1))
pyperclip.copy(chr(args.argument1))
