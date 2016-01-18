import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(raw_input())
h = int(raw_input())
t = raw_input()
row = []
for i in xrange(h):
    row.append(raw_input())
    print >> sys.stderr, row

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
print >> sys.stderr, l
print >> sys.stderr, h
print >> sys.stderr, t
waarden = []
result = []
for letter in t:
    answer = ord(letter) - 65  # a =0
    if answer > 25:
        answer -= 32
    waarden.append(answer)
for i in xrange(h):
    result.append("")
for j in xrange(len(waarden)):
    for i in xrange(h):
        if waarden[j] < 0 or waarden[j] > 25:
            waarden[j] = 26
        bgin = waarden[j] * l
        eind = bgin + l
        result[i] += row[i][bgin:eind]
for i in xrange(h):
    print result[i]
