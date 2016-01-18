import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = raw_input()

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

print >> sys.stderr, message
answer = ''.join(format(ord(letter), 'b').zfill(7) for letter in message)
line = ""
vorig = ""
teller = 1
waarden = []
nul_een = ["00", "0"]
start = True
result = ""
for nmber in answer:
    if nmber == vorig:
        teller += 1
    else:
        if not start:
            waarden.append(teller)
        start = False
        vorig = nmber
        teller = 1
waarden.append(teller)
karakter = int(answer[0])

for waarde in waarden:
    result += " "
    result += nul_een[karakter]
    result += " "
    for i in xrange(waarde):
        result += "0"
    karakter = 0 if karakter == 1 else 1
print result.strip()