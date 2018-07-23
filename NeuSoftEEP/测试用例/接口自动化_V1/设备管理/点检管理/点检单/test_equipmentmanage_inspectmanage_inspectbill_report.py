# _*_coding: utf-8 _*_

import unittest

from public import params
from 测试用例.接口自动化_V1.设备管理.点检管理.点检单 import inspectbill_public

domain = params.testdomain
port = params.testport
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


class InspectBillReport(unittest.TestCase):
    u'''点检单报工'''
    def setUp(self):
        pass

    def test_inspectbill_report(self):
        u'''单个点检单报工'''


    def test_inspectbill_report_created(self):
        u'''已创建的点检单报工'''
        pass


    def test_inspectbill_report_reported(self):
        u'''已报工的点检单报工'''
        # 获取保养单gid
        pass
    

if __name__ == '__main__':
    unittest.main()
