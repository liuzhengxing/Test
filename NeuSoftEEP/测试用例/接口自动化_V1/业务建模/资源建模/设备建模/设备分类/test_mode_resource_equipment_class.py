# _*_coding:utf-8_*_

import unittest
import requests
import json

from public import params
from 测试用例.接口自动化_V1.业务建模.资源建模.设备建模.设备分类 import equipmentclass_public

domain = params.testdomain
port = params.testport
headers = {
        'Content-Tpye': 'application/json;charset=utf-8'
    }


class EquipmentClass(unittest.TestCase):
    def setUp(self):
        pass

    def test_equipmentclass_create(self):
        u'''创建设备分类'''
        eccreq = equipmentclass_public.equipmentclass_create()
        if 'data":"' in eccreq and 'success":true' in eccreq:
            assert 1 == 1
        else:
            assert 1 == 2
