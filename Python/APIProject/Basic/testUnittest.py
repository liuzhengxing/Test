#encoding = utf-8
import unittest

def commonTest():
    print("commonTest")

class Unit():

    def Test(self):
        print("I love U")

class TestUnitTest(unittest.TestCase):
    def setUp(self):
        commonTest()

    def testOne(self):
        print("testOne")

    def testTwo(self):
        print("testTwo")



