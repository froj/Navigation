from haversine import *
from math import *
import sys

old = ()
new = ()
count = 0

f = open(sys.argv[1], 'r')

for line in f:
    old = new
    new = parse_coordinate(line)
    if count > 0:
        print(line.rstrip() + "\t" + str(distance(old[0], old[1], new[0], new[1])) + " nm")
#        print(line + "\t" + str(haversine(*old, *new)*60))
    else:
        print(line.rstrip())

    count += 1

