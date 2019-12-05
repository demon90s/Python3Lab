import os
import sys

for x in range(0, 10) :
    print(x, ' ', end="")
print("")

for x in [1, 2, 3, 4, 5] :
    print(x, ' ', end="")
print("")

x = 0
while x <= 5:
    print(x)
    x += 1

print("---------------test break continue")

# break continue
for x in range(0, 10) :
    if x <= 5 :
        continue
    if x >= 8 :
        break
    print(x)