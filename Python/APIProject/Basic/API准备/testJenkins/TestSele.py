# encoding: utf-8

import unittest
from APIProject.Basic.API准备.testJenkins.TestSele_public import *

class TestUnitTest(unittest.TestCase):
    def setUp(self):
        login()

    def testOne(self):
        createMaterial()

    def testTwo(self):
        print("testTwo")