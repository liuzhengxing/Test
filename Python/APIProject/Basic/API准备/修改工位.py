# encoding: utf-8
import requests
import json

url= 'http://192.168.138.132/ime-container/bmFactoryWorkStation/query.action?usedPost=true'

headers = {'Content-Type': 'application/json'}

data = {
    "query": {
        "query": [
            {
                "operator": "and",
                "field": "stationName",
                "type": "eq",
                "value": "物流性能工位",
                "left": "(",
                "right": ")"
            }
        ]
    },
    "pager": {
        "page": 1,
        "pageSize": 200
    }
}

rep = requests.post(url=url, headers=headers, data=json.dumps(data)).json()

# s = json.loads(rep)
url_update = 'http://192.168.138.132/ime-container/bmFactoryWorkStation/modify.action'

# print(type(rep))
# print(rep)
# print(type(s))

for j in range(0,200):
    data_update = {
        "stationCode": rep['data'][j]['stationCode'],
        "gid": rep['data'][j]['gid'],
        "workUnitGidRef": {
            "workUnitName": "总装工作单元",
            "gid": "a41dd562a4d0493891f81d55a14aa200"
        },
        "stationFunction": "only_store",
        "stationName": "物流性能工位",
        "serialNum": 1
    }
    requests.post(url=url_update, headers=headers, data=json.dumps(data_update))