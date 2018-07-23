# -*- coding: utf-8 -*-

import unittest

from 测试用例.接口自动化_V1.设备管理.大修管理.大修单 import overhaulbill_public


class OverhaulBillModify(unittest.TestCase):
    def setUp(self):
        pass

    def test_overhaulbill_modify(self):
        u'''大修单报工保存'''
        obgids = []
        obgid = overhaulbill_public.overhaulbill_create()
        obgids.append(obgid)
        overhaulbill_public.overhaulbill_dispatch(obgids)
        overhaulbill_public.overhaulbill_saveorrecord(obgid, 'save')
        obsreq = overhaulbill_public.overhaulbill_select(obgid)
        if 'status":"20' in obsreq:
            assert 1 == 1
        else:
            assert 1 == 2
