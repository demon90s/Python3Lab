import sys
import os

test_file = open("test.txt", "wb")
print(test_file)
print(test_file.mode)
print(test_file.name)

test_file.write(bytes("hello python, test file...", "UTF-8"))

test_file.close()

# read
test_file = open("test.txt", "r+")

text = test_file.read()
print(text)

# 删除文件
os.remove("test.txt")