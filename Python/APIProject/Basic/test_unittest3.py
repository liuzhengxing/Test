# encoding: utf-8

import unittest
from Basic.test_fuction import *


class functiontest3(unittest.TestCase):

    def setUp(self):
        print("env is prepared")

    def tearDown(self):
        print("env is clean up")


    def testSubtract(self):
        result = funcSubtract(100,200)
        print("Subtract")
        self.assertEqual(-100,result)

#case1 = fuctiontest()
#case1.testAdd()
#case1.testDevide()

#unittest.main




