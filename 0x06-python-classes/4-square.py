#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.size = size

    def size(self):
        return self.__size

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if not self.__size:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
