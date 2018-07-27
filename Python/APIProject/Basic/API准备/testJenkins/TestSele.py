# encoding: utf-8

import unittest
# from APIProject.Basic.API准备.testJenkins.TestSele_public import *

class TestUnitTest(unittest.TestCase):
    def setUp(self):
        # login()
        print("test setup")

    def testOne(self):
        # createMaterial()
        print("testOne")

    @unittest.skip("skip with no reason")
    def testTwo(self,ignore):
        print("testTwo")

    def tearDown(self):
        # logOut()
        print("test teardown")

if __name__ == '__main__':
    unittest.main()
