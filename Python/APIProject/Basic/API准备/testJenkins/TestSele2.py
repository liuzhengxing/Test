# encoding = utf -8

import  unittest
from APIProject.Basic.API准备.testJenkins.TestSele_publicMethod import PublicMethod as PM

class TestSelenium(unittest.TestCase):

    def setUp(self):
        self.T1 = PM()
        self.T1.openBrowser()
        self.T1.login()

    def testOne(self):
        self.T1.getObject('//*[@id="app"]/div/div/div[1]/div[2]/div[1]/div/div[1]/button').click()

    def tearDown(self):
        self.T1.logOut()

    def testTwo(self):
        self.T1.getObject('//*[@id="app"]/div/div/div[1]/div[2]/div[1]/div/div[1]/button').click()