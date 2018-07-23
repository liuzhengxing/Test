# encoding: utf-8

from unittest import mock
import unittest
import requests
import json

url = "http://192.168.138.132/ime-container/bmStepInfo/add"
headers = {'Content-Type': 'application/json'}
para_in = {"processTest":"false","stepCode":"GB0716007","stepName":"API-GB"}
# para_out = {
# 	"data":"af42124126e64075b16806f4f3945baf",
# 	"success":"True"
#                 }
para_out = True

class API():
    def add(self):
        rep = requests.post(headers=headers,url=url,data=json.dumps(para_in)).text
        return json.loads(rep)["success"]

class TestCount(unittest.TestCase):

    def test_add(self):
        api = API()
        api.add = mock.Mock(return_value=13,side_effect=api.add)
        self.assertEqual(para_out,api.add())

if __name__ == '__main__':
    unittest.main()

