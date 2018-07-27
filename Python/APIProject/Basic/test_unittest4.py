# encoding: utf-8

import unittest
class A():
    def funA(self):
        print("funA")

    def funB(self):
        print("funB")

class TestUnitTest(unittest.TestCase):


    # global a
    # a = A()

    def setUp(self):
        self.a = A()
        self.a.funA()


    def testOne(self):
        self.a.funB()


if __name__ == '__main__':
    unittest.main()
