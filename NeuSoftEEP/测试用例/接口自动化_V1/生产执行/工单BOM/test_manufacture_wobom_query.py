# _*_coding: utf-8_*_

import unittest
import json

from 测试用例.接口自动化_V1.生产执行.工单.workorder_public import lcl_data_workorder
from 测试用例.接口自动化_V1.生产执行.工单.workorder_public import workorder_create
from 测试用例.接口自动化_V1.生产执行.工单BOM.wobom_public import wobom_manual
from 测试用例.接口自动化_V1.生产执行.工单BOM.wobom_public import wobom_query

SheetName = 'WorkOrderCreate'


class WorkOrderBomQuery(unittest.TestCase):
    """工单bom查询接口"""
    def setUp(self):
        self.wogidlist = []
        for i in range(1):
            wodata = lcl_data_workorder(SheetName, 2)
            res = workorder_create(wodata)
            wogid = json.loads(res)['data']
            self.wogidlist.append(wogid)

    def test_manufacture_wobom_manual(self):
        """查询工单bom"""
        wogid = self.wogidlist[0]
        print(wogid)
        try:
            wobom_manual(wogid)
            req = wobom_query(wogid)
            print('查询工单bom', req)
            assert len(json.loads(req)['data']) == 1, '查询到的数量错误'
        except Exception as e:
            print(e)
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()
