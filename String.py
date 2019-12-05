import os
import sys

some_string = "hello python"

print(some_string[0:5])     # hello (01234)
print(some_string[:5])      # hello (01234)
print(some_string[-6:])     # python 从倒数第6个字符开始
print(some_string[:-7])     # hello

print(some_string.capitalize()) # Hello python 不会改变 some_string
print(some_string.find("python"))   # 6 获取下标

print(some_string.isalnum())    # False

print(len(some_string))     # 12

print(some_string.replace("hello", "hi"))   # hi python 不会改变 some_string

print(some_string.strip())  # 把两头的空格删了

string_list = some_string.split(" ")    # 分割字符串，存入List
print(string_list)

# format
print("{}'s age is {}".format("miemie", 4))