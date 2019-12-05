import os
import sys

# can not change tuple after it created

num_tuple = (1, 3, 5, 2, 4, 6)
print(num_tuple)

# convert to list
new_num_list = list(num_tuple)
new_num_list.remove(3)
print(new_num_list)

# convert list to tuple
new_num_tuple = tuple(new_num_list)
print(new_num_tuple)

# operators
print(len(num_tuple))   # 6
print(min(num_tuple))   # 1
print(max(num_tuple))   # 6