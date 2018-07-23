# encoding: utf-8

# encoding: utf-8

import requests
import json
import random

url_update = "http://192.168.138.131/ime-container/bmQcStandardIndex/add.action"

headers = {'Content-Type': 'application/json'}


for i in range(700):
    data =  {
    "bmQcStandardGid": "3dbc5e2866474c6ca753d1715dd803d5",
    "bmQcStandardGidRef": {
        "name": "ISO9001"
    },
    "code": "Code0702" +str(i),
    "type": "ration",
    "lowerLimit": "1",
    "upperLimit": "100",
    "importance": "important",
    "name": "质检项" +str(i)
    }
    resp = requests.post(url=url_update,headers=headers,data=json.dumps(data))
    # print(resp)

print("OK")





