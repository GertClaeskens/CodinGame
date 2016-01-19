import sys
import math

# Save humans, destroy zombies!

chosen = False
# game loop
while True:
    human_x = []
    human_y = []
    x, y = [int(i) for i in raw_input().split()]
    human_count = int(raw_input())
    for i in xrange(human_count):
        regel = raw_input().split()
        human_id = regel[0]
        human_x.append(int(regel[1]))
        human_y.append(int(regel[2]))
        # human_id, human_x, human_y = [int(j) for j in raw_input().split()]
    zombie_count = int(raw_input())
    for i in xrange(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in raw_input().split()]

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    print >> sys.stderr, human_x
    # Your destination coordinates
    choose = []

    if not chosen:
        for i in xrange(human_count):
            choose.append(math.sqrt(abs(x - human_x[i]) ** 2 + abs(y - human_y[i] ** 2)))
        print >> sys.stderr, choose
        min_value = min(choose)
        if len(choose) > 1:
            choose[choose.index(min_value)] = 100000
            min_value = min(choose)
            print >> sys.stderr, choose
        minindex = choose.index(min_value)
        chosen = True
        naarX = human_x[minindex]
        naarY = human_y[minindex]
    print >> sys.stderr, minindex
    print str(naarX) + " " + str(naarY)
    if len(human_x) > 4:
        chosen = False
