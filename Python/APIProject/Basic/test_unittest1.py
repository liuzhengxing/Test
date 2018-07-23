# encoding: utf-8

import unittest
from Basic.test_fuction import *

class functiontest1(unittest.TestCase):

    def setUp(self):
        "初始化环境"
        print("env is prepared")

    def tearDown(self):
        print("env is clean up")

    def testAdd(self):
        result = funcAdd(1,2)
        print("Add")
        self.assertEqual(3,result)


#case1 = fuctiontest()
#case1.testAdd()
#case1.testDevide()

#放在testsuite中执行，所以这里注释掉
#unittest.main




