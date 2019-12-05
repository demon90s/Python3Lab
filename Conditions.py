import os
import sys

# relation operators: > < >= <= != ==
# logic operators: and or not

age = 3

if age >= 18 :
    print("you are adult")
elif age >= 12 :
    print("you are teenager")
else :
    print("you are child")

if (age >= 1 and age <= 3) :
    print("you are baby")