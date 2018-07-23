# encoding: utf-8
import requests
import json



url= 'http://192.168.138.132/ime-container/bmFactoryWorkStation/add.action'
i = 1



headers = {'Content-Type': 'application/json'}



for i in range(200):
    data = {
        "stationCode": "P" + str(i),
        "stationName": "物流性能工位",
        "workUnitGid": "a41dd562a4d0493891f81d55a14aa200",
        "workUnitGidRef": {
            "workUnitName": "总装工作单元"
        },
        "stationFunction": "only_produce"
    }
    rep = requests.post(url=url, headers=headers, data=json.dumps(data))

