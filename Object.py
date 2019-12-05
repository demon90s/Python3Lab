import os
import sys

# __ 表示 private
class Animal :
    __name = ""
    __x = 0
    __y = 0

    # constructor
    def __init__(self, name, x, y) :
        self.__name = name
        self.__x = x
        self.__y = y

    # setter and getter
    def setName(self, name) :
        self.__name = name

    def setXY(self, x, y) :
        self.__x = x
        self.__y = y

    def getName(self) :
        return self.__name

    def getX(self) :
        return self.__x
    def getY(self) :
        return self.__y

    def getType(self) :
        return "Animal"

    def ToString(self) :
        return "{}({}, {})".format(self.__name, self.__x, self.__y)

cat = Animal("Kitty", 42, 30)
print(cat.ToString())

# 继承
class Dog(Animal) :
    __owner = ""

    def __init__(self, name, x, y, owner) :
        self.__owner = owner
        super(Dog, self).__init__(name, y, y)

    def setOwner(self, owner) :
        self.__owner = owner

    def getOwner(self) :
        return self.__owner

    def getType(self) :
        return "Dog"

    def ToString(self) :
        return "{}({}, {}) owner({})".format(self.getName(), self.getX(), self.getY(), self.__owner)

dog = Dog("Gouqi", 21, 11, "Diwen")
print(dog.ToString())

# 多态
def test_get_type(animal) :
    print(animal.getType())

test_get_type(cat)  # Animal
test_get_type(dog)  # Dog