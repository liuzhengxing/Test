# encoding: utf-8
import unittest
from Basic.test_unittest1 import *
from Basic.test_unittest2 import *
from Basic.test_unittest3 import *
from HTMLTestRunner import HTMLTestRunner
import datetime


suite = unittest.TestSuite()
tests = [functiontest1("testAdd"), functiontest2("testDivide"), functiontest3("testSubtract")]
suite.addTests(tests)

daytime = str(datetime.datetime.now().date())
hourtime = str(datetime.datetime.now().hour)
minutime = str(datetime.datetime.now().minute)


def runcase():
    with open('D:\\'+ daytime + hourtime + minutime + 'UnittestTextReport.html', 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title="unittest report",
                                description="generated by HTMLTestRunner",
                                verbosity=2)
        runner.run(suite)
        f.close()


runcase()



# filePath = 'D:\\UnittestTextReport.html'
# fp = open(filePath,'wb')
# runner = HTMLTestRunner(stream=fp, description=u'用例执行情况：')
# fp.close()