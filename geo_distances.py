from haversine import *
from math import *
import sys

old = ()
new = ()
count = 0
total = 0

f = open(sys.argv[1], 'r')

for line in f:
    old = new
    new = parse_coordinate(line)
    if count > 0:
        dist = distance(old[0], old[1], new[0], new[1])
        total += dist
        print(line.rstrip() + "\t" + str(dist) + " nm")
    else:
        print(line.rstrip())

    count += 1

print("")
print("Total:\t" + str(total) + " nm")
