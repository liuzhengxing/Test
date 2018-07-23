# encoding: utf-8
import requests
import json

'''查询物料50条明细'''
url= 'http://192.168.138.132/ime-container/bmMaterielInfo/queryByExcludeCondition.action?usedPost=true&ids=b0d70225e297458bbecaf8e8a4bc7b9d'

data = {
    "query": {
        "query": []
    },
    "pager": {
        "page": 1,
        "pageSize": 50
    }
}

headers = {'Content-Type': 'application/json'}

resp = requests.post(url=url,headers=headers,data=json.dumps(data)).text

s = json.loads(resp)

'''拼接所有的子物料'''
finalData = []

for i in range(0,9):
    data = {
        "bomNumber": "10",
        "denoNumber": "1",
        "pivotal": "false",
        "moleculeNumber": "10",
        "mdMaterialGidRef": {
            "code": s["data"][i]["code"],
            "name": "物流重复1"
        },
        "useNumber": "0.00",
        "substitute": "no",
        "validBeginTime": "2018-05-18 10:47:43",
        "materialGid": s["data"][i]["gid"],
        "dosageScheme": "BOM_NUMBER"
    }
    finalData.append(data)


print(finalData)

'''子物料拼接成BOM'''
BOM = {
    "bmProductDetialList": finalData,
    "endTime": "2099-12-31",
    "virtual": "false",
    "replaceBom": "host_bom",
    "pivotal": "true",
    "startTime": "2018-05-20 10:45:14",
    "mdMaterialGidRef": {
        "code": "01",
        "name": "物流重复产品",
        "bmMeasurementUnitGidRef": {
            "name": "克"
        }
    },
    "version": "10",
    "bomType": "produce_bom",
    "materialGid": "b0d70225e297458bbecaf8e8a4bc7b9d"
}


# for i in range(10):
#     print(s["data"][i]["code"])
#     print(s["data"][i]["gid"])

print(BOM)