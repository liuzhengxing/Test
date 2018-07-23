# encoding: utf-8

class ClassOne():

    def func(self):
        print("func() in one.py")



if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("two.py is being imported into another module")

def func1():
    print("func1")

def func2():
    print("func2")

class ClassTwo():
    print("test import .*")

test = 'json'