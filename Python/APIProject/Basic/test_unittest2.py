# encoding: utf-8

import unittest
from Basic.test_fuction import *

class functiontest2(unittest.TestCase):

    def setUp(self):
        print("env is prepared")

    def tearDown(self):
        print("env is clean up")


    def testDivide(self):
        result = funcDivide(10,5)
        print("Divide")
        self.assertEqual(2,result)


#case1 = fuctiontest()
#case1.testAdd()
#case1.testDevide()

#放在testsuite中执行，所以这里注释掉
#unittest.main




