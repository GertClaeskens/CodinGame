import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())  # Number of elements which make up the association table.
q = int(raw_input())  # Number Q of file names to be analyzed.
ext = []
mt = []
for i in xrange(n):
    # ext: file extension
    # mt: MIME type.
    regel = raw_input().split()
    ext.append(regel[0].lower())
    mt.append(regel[1])

fname = []
for i in xrange(q):
    fname.append(raw_input().lower())  # One file name per line.
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
teller = 0
# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
for fn in fname:

    k = fn.rfind(".")
    extens = fn[k + 1:]
    if k >= 0 and extens in ext:
        i = ext.index(extens)
        print mt[i]
    else:
        print "UNKNOWN"
