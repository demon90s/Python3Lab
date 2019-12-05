import random
import os
import sys

name_list = ['diwen', 'miemie', 'meili']

print("first name: ", name_list[0]) # diwen

name_list[0] = 'liudiwen'
print("first name: ", name_list[0]) # liudiwen

print(name_list)
print(len(name_list))   # 3
print(max(name_list))   # miemie
print(min(name_list))   # liudiwen

more_list = [name_list, "bbb", "aaa"]
print(more_list)

# List operator
name_list.append("goudan")
print(name_list)

name_list.insert(1, "ergou")
print(name_list)

name_list.remove("ergou")
print(name_list)

name_list.sort()
print(name_list)

name_list.reverse()
print(name_list)

del name_list[3] # erase 4th element
print(name_list)