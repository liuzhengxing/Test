# _*_coding: utf-8_*_

import unittest
import json

from 测试用例.接口自动化_V1.生产执行.工单.workorder_public import lcl_data_workorder
from 测试用例.接口自动化_V1.生产执行.工单.workorder_public import workorder_create
from 测试用例.接口自动化_V1.生产执行.工单BOM.wobom_public import wobom_manual

SheetName = 'WorkOrderCreate'


class WorkOrderBomSave(unittest.TestCase):
    """手动关联工单bom接口"""
    def setUp(self):
        self.wogidlist = []
        for i in range(1):
            wodata = lcl_data_workorder(SheetName, 2)
            res = workorder_create(wodata)
            wogid = json.loads(res)['data']
            self.wogidlist.append(wogid)

    def test_manufacture_wobom_manual(self):
        """手动关联工单bom"""
        wogid = self.wogidlist[0]
        try:
            req = wobom_manual(wogid)
            print('手动关联工单bom', req)
            self.assertIn('data', json.loads(req))
        except Exception as e:
            print(e)
            assert 1 == 2


if __name__ == '__main__':
    unittest.main()