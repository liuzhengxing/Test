# _*_coding: utf-8_*_

import json
import unittest

from 测试用例.接口自动化_V1.生产执行.工单.workorder_public import workorder_create
from 测试用例.接口自动化_V1.生产执行.工单.workorder_public import lcl_data_workorder

SheetName = 'WorkOrderCreate'


class WorkOrderCreate(unittest.TestCase):
    u"""工单创建接口"""
    def setUp(self):
        pass

    def test_workorder_create_true(self):
        """必填项正常验证"""
        # noinspection PyBroadException
        try:
            data = lcl_data_workorder(SheetName, 2)
            # print(data)
            req = workorder_create(data)
            if req == '':
                assert 1 == 2
            else:
                assert 1 == 1
        except Exception as e:
            print('接口执行错误', e)
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
