#LOC counter
import sys
import csv
#ensures correct argument was given
if len(sys.argv)>2:
    sys.exit("too many arguments")
elif len(sys.argv)<2:
    sys.exit("too few arguments")
elif sys.argv[1].split(sep=".")[1]!="py":
    sys.exit("wrong file format")

try:
    with open(sys.argv[1]) as file:
        lines=file.readlines()
except FileNotFoundError:
    sys.exit("file doesn't exist")

#counts lines
num=0
for line in lines:
    if line.strip().startswith("#"):
        num=num+0
    elif line.strip()==(""):
        num=num+0
    else:
        num=num+1

print(num)
