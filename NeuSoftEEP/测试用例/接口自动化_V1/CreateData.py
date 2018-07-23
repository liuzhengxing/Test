# _*_coding: utf-8_*_

import requests
import json

from public import params

BaseDir = params.BaseDir
BaseUrl = params.BaseUrl


headers = {
    "Content-Type": "application/json"
}


# 创建用户bc9ebfd4c63d4c66acff0acbb06e43ca
url1 = BaseUrl + "/ime-container/user/add.action"
data1 = {"code": "QU0", "name": "QU0"}
try:
    req1 = requests.post(url1, headers=headers, data=json.dumps(data1)).content.decode()
    userGid = json.loads(req1)["data"]
except KeyError:
    url1 = BaseUrl + "/ime-container/user/query.action?usedPost=true"
    data1 = {"query":{"query":[{"operator":"and","field":"code","type":"eq","value":"QU0","left":"(","right":")"}]},"pager":{"page":1,"pageSize":10}}
    req1 = requests.post(url1, headers=headers, data=json.dumps(data1)).content.decode()
    userGid = json.loads(req1)["data"][0]["gid"]
print("usergid", userGid)


# 创建业务组7f87ddd3fe354e3dbb492ce0613a0201
url2 = BaseUrl + "/ime-container/busiGroup/add.action"
data2 = {
    "mode": "create",
    "active": "false",
    "busiGroupCode": "Q1",
    "busiGroupName": "小米集团",
    "creationDate": "2018-05-01",
    "phone": "18888888888",
    "address": "文化大道",
    "descr": "测试"
}
try:
    req2 = requests.post(url2, headers=headers, data=json.dumps(data2)).content.decode()
    busiGroupGid = json.loads(req2)["data"]
except KeyError:
    url2 = BaseUrl + "/ime-container/busiGroup/query.action?usedPost=true"
    data2 = {"query":{"query":[{"operator":"and","field":"busiGroupCode","type":"eq","value":"Q1","left":"(","right":")"}]},"pager":{"page":1,"pageSize":10}}
    req2 = requests.post(url2, headers=headers, data=json.dumps(data2)).content.decode()
    busiGroupGid = json.loads(req2)["data"][0]["gid"]
print("busiGroupGid", busiGroupGid)

# 添加业务组管理员674e543f1c9b4366b0de744d4cfcb09c
url3 = BaseUrl + "/ime-container/identity/add.action"
data3 = {
    "identity": "BusiGroupMgr",
    "type": "0",
    "groupGid": busiGroupGid,
    "name": "QU0",
    "smObjectGid": userGid,
    "startTime": "2018-05-01"
}
try:
    req3 = requests.post(url3, headers=headers, data=json.dumps(data3)).content.decode()
    # print(req3)
except KeyError:
    pass

# 创建业务单元7f7d0e5b65274995b88e252b209dc010
url4 = BaseUrl + "/ime-container/busiUnit/add.action"
data4 = {
    "descr": "测试",
    "mobile": "16666666666",
    "active": "true",
    "abbreviate": "小米",
    "active1": "true",
    "active2": "true",
    "active3": "true",
    "active4": "true",
    "active5": "true",
    "active6": "true",
    "active7": "true",
    "active8": "true",
    "active9": "true",
    "busiUnitName": "小米科技",
    "busiUnitCode": "Q1",
    "funcGid": [
        "6392A29965804A03E055000000000001",
        "6392A29965814A03E055000000000001",
        "6392A29965824A03E055000000000001",
        "6392A29965834A03E055000000000001",
        "6392A29965844A03E055000000000001",
        "6392A29965854A03E055000000000001",
        "6392A29965864A03E055000000000001",
        "6392A29965874A03E055000000000001",
        "6392A29965884A03E055000000000001"
    ],
    "busiUnitFunRelationList": [
        {"funGid": "6392A29965804A03E055000000000001", "active": "true"},
        {"funGid": "6392A29965814A03E055000000000001", "active": "true"},
        {"funGid": "6392A29965824A03E055000000000001", "active": "true"},
        {"funGid": "6392A29965834A03E055000000000001", "active": "true"},
        {"funGid": "6392A29965844A03E055000000000001", "active": "true"},
        {"funGid": "6392A29965854A03E055000000000001", "active": "true"},
        {"funGid": "6392A29965864A03E055000000000001", "active": "true"},
        {"funGid": "6392A29965874A03E055000000000001", "active": "true"},
        {"funGid": "6392A29965884A03E055000000000001", "active": "true"}
    ],
    "groupGid": busiGroupGid
}
try:
    req4 = requests.post(url4, headers=headers, data=json.dumps(data4)).content.decode()
    busiUnitGid = json.loads(req4)["data"]
except KeyError:
    url4 = BaseUrl + "/ime-container/busiUnit/query.action?usedPost=true"
    data4 = {"query":{"query":[{"operator":"and","field":"busiUnitCode","type":"eq","value":"Q1","left":"(","right":")"}]},"pager":{"page":1,"pageSize":10}}
    req4 = requests.post(url4, headers=headers, data=json.dumps(data4)).content.decode()
    busiUnitGid = json.loads(req4)["data"][0]["gid"]
print("busiUnitGid", busiUnitGid)


# 创建部门74c0eeefed9548d9ad9bb555a6a085d7
url5 = BaseUrl + "/ime-container/department/add.action"
data5 = {
    "smBusiUnitGid": busiUnitGid,
    "smBusiGroupGid": "null",
    "smBusiUnitGidRef": {"busiUnitName": "小米科技"},
    "code": "Q1",
    "name": "手机"
}
try:
    req5 = requests.post(url5, headers=headers, data=json.dumps(data5)).content.decode()
    departmentGid = json.loads(req5)["data"]
except KeyError:
    pass

# 创建工作中心dd9476eba77b4bd18d171af766f78e0e
url6 = BaseUrl + "/ime-container/bmFactoryWorkCenter/add.action"
data6 = {
    "workCenterCode": "Q1",
    "workCenterName": "小米科技",
    "factoryBusiUnitGid": busiUnitGid,
    "busiUnitName": busiUnitGid
}
try:
    req6 = requests.post(url6, headers=headers, data=json.dumps(data6)).content.decode()
    bmFactoryWorkCenterGid = json.loads(req6)["data"]
except KeyError:
    url6 = BaseUrl + "/ime-container/bmFactoryWorkCenter/query.action?usedPost=true"
    data6 = {"query":{"query":[{"operator":"and","field":"workCenterCode","type":"eq","value":"Q1","left":"(","right":")"}]},"pager":{"page":1,"pageSize":10}}
    req6 = requests.post(url6, headers=headers, data=json.dumps(data6)).content.decode()
    bmFactoryWorkCenterGid = json.loads(req6)["data"][0]["gid"]
print('bmFactoryWorkCenterGid', bmFactoryWorkCenterGid)

# 创建重复型产线aad631b9c1dc4d5b8443324500b50dbd
url7 = BaseUrl + "/ime-container/bmFactoryLine/add.action"
data7 = {
    "lineCode": "Q11",
    "lineName": "小米重复",
    "workCenterGid": bmFactoryWorkCenterGid,
    "busiUnitName": "小米科技",
    "lineType": "REPEAT",
    "remarks": "测试"
}
try:
    req7 = requests.post(url7, headers=headers, data=json.dumps(data7)).content.decode()
    bmFactoryLineCF = json.loads(req7)["data"]
except KeyError:
    url7 = BaseUrl + "/ime-container/bmFactoryLine/query.action?usedPost=true"
    data7 = {"query":{"query":[{"operator":"and","field":"lineCode","type":"eq","value":"Q11","left":"(","right":")"}]},"pager":{"page":1,"pageSize":10}}
    req7 = requests.post(url7, headers=headers, data=json.dumps(data7)).content.decode()
    bmFactoryLineCF = json.loads(req7)["data"][0]["gid"]
print("bmFactoryLineCF", bmFactoryLineCF)

# 创建离散型产线3d33bf007bbc4ddea0b1bd6be33d5a22
url8 = BaseUrl + "/ime-container/bmFactoryLine/add.action"
data8 = {
    "lineCode": "Q12",
    "lineName": "小米离散",
    "workCenterGid": bmFactoryWorkCenterGid,
    "busiUnitName": "小米科技",
    "lineType": "DISCRETE",
    "remarks": "测试"
}
try:
    req8 = requests.post(url8, headers=headers, data=json.dumps(data8)).content.decode()
    bmFactoryLineLS = json.loads(req8)["data"]
except KeyError:
    url8 = BaseUrl + "/ime-container/bmFactoryLine/query.action?usedPost=true"
    data8 = {"query":{"query":[{"operator":"and","field":"lineCode","type":"eq","value":"Q12","left":"(","right":")"}]},"pager":{"page":1,"pageSize":10}}
    req8 = requests.post(url8, headers=headers, data=json.dumps(data8)).content.decode()
    bmFactoryLineLS = json.loads(req8)["data"][0]["gid"]
print("bmFactoryLineLS", bmFactoryLineLS)

# 创建重复型产线下的工作单元093a52d1204f496b89f0a3ec44d03451
url9 = BaseUrl + "/ime-container/bmFactoryWorkUnit/add.action"
data9 = {
    "workUnitCode": "Q111",
    "workUnitName": "小米重复单元",
    "factoryLineGid": bmFactoryLineCF,
    "remarks": "测试"
}
try:
    req9 = requests.post(url9, headers=headers, data=json.dumps(data9)).content.decode()
    bmFactoryWorkUnitCF = json.loads(req9)["data"]
except KeyError:
    url9 = BaseUrl + "/ime-container/bmFactoryWorkUnit/query.action?usedPost=true"
    data9 = {"query":{"query":[{"operator":"and","field":"workUnitCode","type":"eq","value":"Q111","left":"(","right":")"}]},"pager":{"page":1,"pageSize":10}}
    req9 = requests.post(url9, headers=headers, data=json.dumps(data9)).content.decode()
    bmFactoryWorkUnitCF = json.loads(req9)["data"][0]["gid"]
print("bmFactoryWorkUnitCF", bmFactoryWorkUnitCF)

# 创建离散型产线下的工作单元8daaaf8d62144fe19e6cef435a7b9b77
url10 = BaseUrl + "/ime-container/bmFactoryWorkUnit/add.action"
data10 = {
    "workUnitCode": "Q121",
    "workUnitName": "小米离散单元",
    "factoryLineGid": bmFactoryLineLS,
    "remarks": "测试"
}
try:
    req10 = requests.post(url10, headers=headers, data=json.dumps(data10)).content.decode()
    bmFactoryWorkUnitLS = json.loads(req10)["data"]
except KeyError:
    url10 = BaseUrl + "/ime-container/bmFactoryWorkUnit/query.action?usedPost=true"
    data10 = {"query":{"query":[{"operator":"and","field":"workUnitCode","type":"eq","value":"Q121","left":"(","right":")"}]},"pager":{"page":1,"pageSize":10}}
    req10 = requests.post(url9, headers=headers, data=json.dumps(data10)).content.decode()
    bmFactoryWorkUnitLS = json.loads(req10)["data"][0]["gid"]
print("bmFactoryWorkUnitLS", bmFactoryWorkUnitLS)

# 创建重复型产线CPU工位0ed34e1027ad4a5fa090b6dd9ff0989d
url11 = BaseUrl + "/ime-container/bmFactoryWorkStation/add.action"
data11 = {
    "stationCode": "Q1111",
    "stationName": "处理器",
    "workUnitGid": bmFactoryWorkUnitCF,
    "workUnitGidRef": {"workUnitName": "小米重复单元"},
    "stationFunction": "produce_store",
    "remarks": "测试"
}
try:
    req11 = requests.post(url11, headers=headers, data=json.dumps(data11)).content.decode()
    bmFactoryWorkStationCPUGid = json.loads(req11)["data"]
except KeyError:
    url11 = BaseUrl + "/ime-container/bmFactoryWorkStation/query.action?usedPost=true"
    data11 = {"query":{"query":[{"operator":"and","field":"stationCode","type":"eq","value":"Q1111","left":"(","right":")"}]},"pager":{"page":1,"pageSize":10}}
    req11 = requests.post(url11, headers=headers, data=json.dumps(data11)).content.decode()
    bmFactoryWorkStationCPUGid = json.loads(req11)["data"][0]["gid"]
print("bmFactoryWorkStationCPUGid", bmFactoryWorkStationCPUGid)


# 创建重复型产线主板工位
url12 = BaseUrl + "/ime-container/bmFactoryWorkStation/add.action"
data12 = {
    "stationCode": "Q1112",
    "stationName": "主板",
    "workUnitGid": bmFactoryWorkUnitCF,
    "workUnitGidRef": {"workUnitName": "小米重复单元"},
    "stationFunction": "produce_store",
    "remarks": "测试"
}
try:
    req12 = requests.post(url12, headers=headers, data=json.dumps(data12)).content.decode()
    bmFactoryWorkStationZBGid = json.loads(req12)["data"]
except KeyError:
    url12 = BaseUrl + "/ime-container/bmFactoryWorkStation/query.action?usedPost=true"
    data12 = {"query":{"query":[{"operator":"and","field":"stationCode","type":"eq","value":"Q1112","left":"(","right":")"}]},"pager":{"page":1,"pageSize":10}}
    req12 = requests.post(url12, headers=headers, data=json.dumps(data12)).content.decode()
    bmFactoryWorkStationZBGid = json.loads(req12)["data"][0]["gid"]
print("bmFactoryWorkStationZBGid", bmFactoryWorkStationZBGid)


# 创建重复型产线屏幕工位
url13 = BaseUrl + "/ime-container/bmFactoryWorkStation/add.action"
data13 = {
    "stationCode": "Q1113",
    "stationName": "屏幕",
    "workUnitGid": bmFactoryWorkUnitCF,
    "workUnitGidRef": {"workUnitName": "小米重复单元"},
    "stationFunction": "produce_store",
    "remarks": "测试"
}
try:
    req13 = requests.post(url13, headers=headers, data=json.dumps(data13)).content.decode()
    bmFactoryWorkStationPMGid = json.loads(req13)["data"]
except KeyError:
    url13 = BaseUrl + "/ime-container/bmFactoryWorkStation/query.action?usedPost=true"
    data13 = {"query":{"query":[{"operator":"and","field":"stationCode","type":"eq","value":"Q1113","left":"(","right":")"}]},"pager":{"page":1,"pageSize":10}}
    req13 = requests.post(url13, headers=headers, data=json.dumps(data13)).content.decode()
    bmFactoryWorkStationPMGid = json.loads(req13)["data"][0]["gid"]
print("bmFactoryWorkStationPMGid", bmFactoryWorkStationPMGid)

# 创建离散型型产线工位1
url14 = BaseUrl + "/ime-container/bmFactoryWorkStation/add.action"
data14 = {
    "stationCode": "Q1211",
    "stationName": "离散1",
    "workUnitGid": bmFactoryWorkUnitLS,
    "workUnitGidRef": {"workUnitName": "小米离散单元"},
    "stationFunction": "produce_store",
    "remarks": "测试"
}
try:
    req14 = requests.post(url14, headers=headers, data=json.dumps(data14)).content.decode()
    bmFactoryWorkStationLS1Gid = json.loads(req14)["data"]
except KeyError:
    url14 = BaseUrl + "/ime-container/bmFactoryWorkStation/query.action?usedPost=true"
    data14 = {"query":{"query":[{"operator":"and","field":"stationCode","type":"eq","value":"Q1211","left":"(","right":")"}]},"pager":{"page":1,"pageSize":10}}
    req14 = requests.post(url14, headers=headers, data=json.dumps(data14)).content.decode()
    bmFactoryWorkStationLS1Gid = json.loads(req14)["data"][0]["gid"]
print("bmFactoryWorkStationLS1Gid", bmFactoryWorkStationLS1Gid)


# 创建离散型型产线工位2
url15 = BaseUrl + "/ime-container/bmFactoryWorkStation/add.action"
data15 = {
    "stationCode": "Q1212",
    "stationName": "离散2",
    "workUnitGid": bmFactoryWorkUnitLS,
    "workUnitGidRef": {"workUnitName": "小米离散单元"},
    "stationFunction": "produce_store",
    "remarks": "测试"
}
try:
    req15 = requests.post(url15, headers=headers, data=json.dumps(data15)).content.decode()
    bmFactoryWorkStationLS2Gid = json.loads(req15)["data"]
except KeyError:
    url15 = BaseUrl + "/ime-container/bmFactoryWorkStation/query.action?usedPost=true"
    data15 = {"query":{"query":[{"operator":"and","field":"stationCode","type":"eq","value":"Q1212","left":"(","right":")"}]},"pager":{"page":1,"pageSize":10}}
    req15 = requests.post(url15, headers=headers, data=json.dumps(data15)).content.decode()
    bmFactoryWorkStationLS2Gid = json.loads(req15)["data"][0]["gid"]
print("bmFactoryWorkStationLS2Gid", bmFactoryWorkStationLS2Gid)


# 创建计量单位6d7c10bcb7c54f4e896a60a4a26e731b
url16 = BaseUrl + "/ime-container/bmMeasurementUnit/createOrUpdate.action"
data16 = [{
    "basicUnit": "true",
    "code": "Q1",
    "name": "件",
    "englishName": "jian",
    "type": "pcs",
    "conversionFactor": "1",
    "decimalDigit": "1"
}]
try:
    req16 = requests.post(url16, headers=headers, data=json.dumps(data16)).content.decode()
    bmMeasurementUnitGid = json.loads(req16)["data"]
except KeyError:
    url16 = BaseUrl + "/ime-container/bmMeasurementUnit/query.action?usedPost=true"
    data16 = {"query":{"query":[{"operator":"and","field":"code","type":"eq","value":"Q1","left":"(","right":")"}]},"pager":{"page":1,"pageSize":10}}
    req16 = requests.post(url16, headers=headers, data=json.dumps(data16)).content.decode()
    bmMeasurementUnitGid = json.loads(req16)["data"][0]["gid"]
print("bmMeasurementUnitGid", bmMeasurementUnitGid)


# 创建物料分类949c8a2d109043b98c2ebfc84c6d6034
url17 = BaseUrl + "/ime-container/bmMaterielType/add.action"
data17 = {"code": "Q1", "name": "手机"}
try:
    req17 = requests.post(url17, headers=headers, data=json.dumps(data17)).content.decode()
    bmMaterielTypeGid = json.loads(req17)["data"]
except Exception as e:
    url17 = BaseUrl + "/ime-container/bmMaterielType/getMaterielTypeTree.action"
    req17 = requests.post(url17, headers=headers).content.decode()
    gids = json.loads(req17)["data"][0]["childs"]
    for gid in gids:
        if gid["code"] == "Q1":
            bmMaterielTypeGid = gid["id"]
print("bmMaterielTypeGid", bmMaterielTypeGid)

# 创建仓库71c77cb81dc049859c2396477aabc0c8
url18 = BaseUrl + "/ime-container/bmWarehouse/add.action"
data18 = {
    "smBusiUnitGid": busiUnitGid,
    "busiUnitName": "小米科技",
    "code": "Q1",
    "name": "小米仓",
    "warehouseType": "materialWarehouse",
    "workCenterGid": bmFactoryWorkCenterGid,
    "workCenterGidRef": {"workCenterName": "小米科技"}
}
try:
    req18 = requests.post(url18, headers=headers, data=json.dumps(data18)).content.decode()
    bmWarehouseGid = json.loads(req18)["data"]
except KeyError:
    url18 = BaseUrl + "/ime-container/bmWarehouse/getWarehouseTree.action?filter=sm_busi_unit_gid eq '" + busiUnitGid + "'"
    req18 = requests.post(url18, headers=headers).content.decode()
    bmWarehouseGid = json.loads(req18)["data"][0]["childs"][0]["id"]
print("bmWarehouseGid", bmWarehouseGid)

# 创建物料cpu
url19 = BaseUrl + "/ime-container/bmMaterielInfo/add.action"
data19 = {
    "productionBatch": "false",
    "versionNumber": "2",
    "isVirtual": "false",
    "optionMark": "false",
    "packNumber": "12",
    "barCodeManagement": "false",
    "replacementPart": "false",
    "resources": "false",
    "materielTypeGid": bmMaterielTypeGid,
    "bmMeasurementUnitGidRef": {"name": "件"},
    "outsourcing": "false",
    "materialWay": "process_of_acquisition",
    "bmWarehouseGidRef": {"name": "小米仓"},
    "model": "晓龙",
    "bmWarehouseGid": bmWarehouseGid,
    "sparePart": "false",
    "name": "处理器",
    "traceBack": "true",
    "code": "Q11",
    "figureNumber": "1",
    "bmMeasurementUnitGid": bmMeasurementUnitGid,
    "qualityAssurance": "true",
    "equipment": "false",
    "inspectionType": "1",
    "materielTypeGidRef": {"name": "手机"},
    "alias": "835",
    "serialNumManagement": "false",
    "packWay": "D",
    "inspectionMode": "fullInspection",
    "substitute": "false",
    "homemadePiece": "true",
    "spec": "F5JN3",
    "productionPath": "false",
    "consumptivePart": "false",
    "purchaseParts": "false"
}
try:
    req19 = requests.post(url19, headers=headers, data=json.dumps(data19)).content.decode()
    if json.loads(req19)["code"] == 105000:
        url19 = BaseUrl + "/ime-container/bmMaterielInfo/query.action?usedPost=true"
        data19 = {"query": {
            "query": [{"operator": "and", "field": "code", "type": "eq", "value": "Q11", "left": "(", "right": ")"}]},
                  "pager": {"page": 1, "pageSize": 10}}
        req19 = requests.post(url19, headers=headers, data=json.dumps(data19)).content.decode()
        MaterielCPUGid = json.loads(req19)["data"][0]["gid"]
    else:
        MaterielCPUGid = json.loads(req19)["data"]
    print("MaterielCPUGid", MaterielCPUGid)
except KeyError:
    pass


# 创建物料电池
url20 = BaseUrl + "/ime-container/bmMaterielInfo/add.action"
data20 = {
    "productionBatch": "false",
    "versionNumber": "2",
    "isVirtual": "false",
    "optionMark": "false",
    "packNumber": "12",
    "barCodeManagement": "false",
    "replacementPart": "false",
    "resources": "false",
    "materielTypeGid": bmMaterielTypeGid,
    "bmMeasurementUnitGidRef": {"name": "件"},
    "outsourcing": "false",
    "materialWay": "process_of_acquisition",
    "bmWarehouseGidRef": {"name": "小米仓"},
    "model": "typ",
    "bmWarehouseGid": bmWarehouseGid,
    "sparePart": "false",
    "name": "电池",
    "traceBack": "true",
    "code": "Q12",
    "figureNumber": "1",
    "bmMeasurementUnitGid": bmMeasurementUnitGid,
    "qualityAssurance": "true",
    "equipment": "false",
    "inspectionType": "1",
    "materielTypeGidRef": {"name": "手机"},
    "alias": "3350mA",
    "serialNumManagement": "false",
    "packWay": "D",
    "inspectionMode": "fullInspection",
    "substitute": "false",
    "homemadePiece": "true",
    "spec": "F5JN3",
    "productionPath": "false",
    "consumptivePart": "false",
    "purchaseParts": "false"
}
try:
    req20 = requests.post(url20, headers=headers, data=json.dumps(data20)).content.decode()
    print(url20, '----', data20)
    if json.loads(req20)["code"] == 105000:
        url20 = BaseUrl + "/ime-container/bmMaterielInfo/query.action?usedPost=true"
        data20 = {"query": {
            "query": [{"operator": "and", "field": "code", "type": "eq", "value": "Q12", "left": "(", "right": ")"}]},
                  "pager": {"page": 1, "pageSize": 10}}
        req20 = requests.post(url20, headers=headers, data=json.dumps(data20)).content.decode()
        MaterielDCGid = json.loads(req20)["data"][0]["gid"]
    else:
        MaterielDCGid = json.loads(req20)["data"]
    print("MaterielDCGid", MaterielDCGid)
except KeyError:
    pass


# 创建物料摄像头
url21 = BaseUrl + "/ime-container/bmMaterielInfo/add.action"
data21 = {
    "productionBatch": "false",
    "versionNumber": "2",
    "isVirtual": "false",
    "optionMark": "false",
    "packNumber": "12",
    "barCodeManagement": "false",
    "replacementPart": "false",
    "resources": "false",
    "materielTypeGid": bmMaterielTypeGid,
    "bmMeasurementUnitGidRef": {"name": "件"},
    "outsourcing": "false",
    "materialWay": "process_of_acquisition",
    "bmWarehouseGidRef": {"name": "小米仓"},
    "model": "后置",
    "bmWarehouseGid": bmWarehouseGid,
    "sparePart": "false",
    "name": "摄像头",
    "traceBack": "true",
    "code": "Q13",
    "figureNumber": "1",
    "bmMeasurementUnitGid": bmMeasurementUnitGid,
    "qualityAssurance": "true",
    "equipment": "false",
    "inspectionType": "1",
    "materielTypeGidRef": {"name": "手机"},
    "alias": "321",
    "serialNumManagement": "false",
    "packWay": "D",
    "inspectionMode": "fullInspection",
    "substitute": "false",
    "homemadePiece": "true",
    "spec": "BGS723",
    "productionPath": "false",
    "consumptivePart": "false",
    "purchaseParts": "false"
}
try:
    req21 = requests.post(url21, headers=headers, data=json.dumps(data21)).content.decode()
    print(url21, '----', data21)
    if json.loads(req21)["code"] == 105000:
        url21 = BaseUrl + "/ime-container/bmMaterielInfo/query.action?usedPost=true"
        data21 = {"query": {
            "query": [{"operator": "and", "field": "code", "type": "eq", "value": "Q13", "left": "(", "right": ")"}]},
                  "pager": {"page": 1, "pageSize": 10}}
        req21 = requests.post(url21, headers=headers, data=json.dumps(data21)).content.decode()
        MaterielSXTGid = json.loads(req21)["data"][0]["gid"]
    else:
        MaterielSXTGid = json.loads(req21)["data"]
    print("MaterielSXTGid", MaterielSXTGid)
except KeyError:
    pass

# 创建物料手机
url22 = BaseUrl + "/ime-container/bmMaterielInfo/add.action"
data22 = {
    "productionBatch": "false",
    "versionNumber": "2",
    "isVirtual": "false",
    "optionMark": "false",
    "packNumber": "12",
    "barCodeManagement": "false",
    "replacementPart": "false",
    "resources": "false",
    "materielTypeGid": bmMaterielTypeGid,
    "bmMeasurementUnitGidRef": {"name": "件"},
    "outsourcing": "false",
    "materialWay": "process_of_acquisition",
    "bmWarehouseGidRef": {"name": "小米仓"},
    "model": "小米6",
    "bmWarehouseGid": bmWarehouseGid,
    "sparePart": "false",
    "name": "手机",
    "traceBack": "true",
    "code": "Q01",
    "figureNumber": "1",
    "bmMeasurementUnitGid": bmMeasurementUnitGid,
    "qualityAssurance": "true",
    "equipment": "false",
    "inspectionType": "1",
    "materielTypeGidRef": {"name": "手机"},
    "alias": "至尊",
    "serialNumManagement": "false",
    "packWay": "D",
    "inspectionMode": "fullInspection",
    "substitute": "false",
    "homemadePiece": "true",
    "spec": "陶瓷",
    "productionPath": "false",
    "consumptivePart": "false",
    "purchaseParts": "false"
}
try:
    req22 = requests.post(url22, headers=headers, data=json.dumps(data22)).content.decode()
    print(url22, '----', data22)
    if json.loads(req22)["code"] == 105000:
        url22 = BaseUrl + "/ime-container/bmMaterielInfo/query.action?usedPost=true"
        data22 = {"query": {
            "query": [{"operator": "and", "field": "code", "type": "eq", "value": "Q13", "left": "(", "right": ")"}]},
                  "pager": {"page": 1, "pageSize": 10}}
        req22 = requests.post(url22, headers=headers, data=json.dumps(data22)).content.decode()
        MaterielSJGid = json.loads(req22)["data"][0]["gid"]
    else:
        MaterielSJGid = json.loads(req22)["data"]
    print("MaterielSJGid", MaterielSJGid)
except KeyError:
    pass

# 创建物料零件
url23 = BaseUrl + "/ime-container/bmMaterielInfo/add.action"
data23 = {
    "productionBatch": "false",
    "versionNumber": "2",
    "isVirtual": "false",
    "optionMark": "false",
    "packNumber": "12",
    "barCodeManagement": "false",
    "replacementPart": "false",
    "resources": "false",
    "materielTypeGid": bmMaterielTypeGid,
    "bmMeasurementUnitGidRef": {"name": "件"},
    "outsourcing": "false",
    "materialWay": "process_of_acquisition",
    "bmWarehouseGidRef": {"name": "小米仓"},
    "model": "零件",
    "bmWarehouseGid": bmWarehouseGid,
    "sparePart": "false",
    "name": "零件",
    "traceBack": "true",
    "code": "Q02",
    "figureNumber": "1",
    "bmMeasurementUnitGid": bmMeasurementUnitGid,
    "qualityAssurance": "true",
    "equipment": "false",
    "inspectionType": "1",
    "materielTypeGidRef": {"name": "手机"},
    "alias": "零件",
    "serialNumManagement": "false",
    "packWay": "D",
    "inspectionMode": "fullInspection",
    "substitute": "false",
    "homemadePiece": "true",
    "spec": "零件",
    "productionPath": "false",
    "consumptivePart": "false",
    "purchaseParts": "false"
}
try:
    req23 = requests.post(url23, headers=headers, data=json.dumps(data23)).content.decode()
    print(url23, '----', data23)
    if json.loads(req23)["code"] == 105000:
        url23 = BaseUrl + "/ime-container/bmMaterielInfo/query.action?usedPost=true"
        data23 = {"query": {
            "query": [{"operator": "and", "field": "code", "type": "eq", "value": "Q13", "left": "(", "right": ")"}]},
                  "pager": {"page": 1, "pageSize": 10}}
        req23 = requests.post(url23, headers=headers, data=json.dumps(data23)).content.decode()
        MaterielLJGid = json.loads(req23)["data"][0]["gid"]
    else:
        MaterielLJGid = json.loads(req23)["data"]
    print("MaterielLJGid", MaterielLJGid)
except KeyError:
    pass

# 创建CPU工序3b0e4afd5cf1406b9e52e8f61cfe9b42
url24 = BaseUrl + "/ime-container/bmOperationInfo/add"
data24 = {
    "reportRowNum": "10",
    "bmWorkLineGidRef": {"lineName": "小米重复"},
    "processTest": "true",
    "bmWorkUnitGid": bmFactoryWorkUnitCF,
    "bmWorkCenterGidRef": {"workCenterName": "小米科技"},
    "businessMode": ["start", "end", "process"],
    "worksheetGenarationMode": "workPublishProduce",
    "bmWorkStationGidRef": {"stationName": "CPU"},
    "bmWorkStationGid": bmFactoryWorkStationCPUGid,
    "name": "CPU",
    "code": "Q11",
    "rhythmType": "hour",
    "bmWorkCenterGid": bmFactoryWorkCenterGid,
    "bmWorkUnitGidRef": {"workUnitName": "小米重复单元"},
    "bmWorkLineGid": bmFactoryLineCF,
    "matEndPoint": "false",
    "rhythm": "1",
    "processingMode": "unlimited",
    "type": "turning"
}
try:
    req24 = requests.post(url24, headers=headers, data=json.dumps(data24)).content.decode()
    bmOperationInfoCPUGid = json.loads(req24)["data"]
except KeyError:
    url24 = BaseUrl + "/ime-container/bmOperationInfo/query.action?usedPost=true"
    data24 = {"query":{"query":[{"operator":"and","field":"code","type":"eq","value":"Q11","left":"(","right":")"}]},"pager":{"page":1,"pageSize":10}}
    req24 = requests.post(url24, headers=headers, data=json.dumps(data24)).content.decode()
    bmOperationInfoCPUGid = json.loads(req24)["data"][0]["gid"]
print("bmOperationInfoCPUGid", bmOperationInfoCPUGid)

# 创建主板工序
url25 = BaseUrl + "/ime-container/bmOperationInfo/add"
data25 = {
    "reportRowNum": "10",
    "bmWorkLineGidRef": {"lineName": "小米重复"},
    "processTest": "true",
    "bmWorkUnitGid": bmFactoryWorkUnitCF,
    "bmWorkCenterGidRef": {"workCenterName": "小米科技"},
    "businessMode": ["start", "end", "process"],
    "worksheetGenarationMode": "workPublishProduce",
    "bmWorkStationGidRef": {"stationName": "主板"},
    "bmWorkStationGid": bmFactoryWorkStationZBGid,
    "name": "主板",
    "code": "Q12",
    "rhythmType": "hour",
    "bmWorkCenterGid": bmFactoryWorkCenterGid,
    "bmWorkUnitGidRef": {"workUnitName": "小米重复单元"},
    "bmWorkLineGid": bmFactoryLineCF,
    "matEndPoint": "false",
    "rhythm": "1",
    "processingMode": "unlimited",
    "type": "turning"
}
try:
    req25 = requests.post(url25, headers=headers, data=json.dumps(data25)).content.decode()
    bmOperationInfoZBGid = json.loads(req25)["data"]
except KeyError:
    url25 = BaseUrl + "/ime-container/bmOperationInfo/query.action?usedPost=true"
    data25 = {"query":{"query":[{"operator":"and","field":"code","type":"eq","value":"Q12","left":"(","right":")"}]},"pager":{"page":1,"pageSize":10}}
    req25 = requests.post(url25, headers=headers, data=json.dumps(data25)).content.decode()
    bmOperationInfoZBGid = json.loads(req25)["data"][0]["gid"]
print("bmOperationInfoZBGid", bmOperationInfoZBGid)

# 创建屏幕工序
url26 = BaseUrl + "/ime-container/bmOperationInfo/add"
data26 = {
    "reportRowNum": "10",
    "bmWorkLineGidRef": {"lineName": "小米重复"},
    "processTest": "true",
    "bmWorkUnitGid": bmFactoryWorkUnitCF,
    "bmWorkCenterGidRef": {"workCenterName": "小米科技"},
    "businessMode": ["start", "end", "process"],
    "worksheetGenarationMode": "workPublishProduce",
    "bmWorkStationGidRef": {"stationName": "屏幕"},
    "bmWorkStationGid": bmFactoryWorkStationPMGid,
    "name": "屏幕",
    "code": "Q13",
    "rhythmType": "hour",
    "bmWorkCenterGid": bmFactoryWorkCenterGid,
    "bmWorkUnitGidRef": {"workUnitName": "小米重复单元"},
    "bmWorkLineGid": bmFactoryLineCF,
    "matEndPoint": "false",
    "rhythm": "1",
    "processingMode": "unlimited",
    "type": "turning"
}
try:
    req26 = requests.post(url26, headers=headers, data=json.dumps(data26)).content.decode()
    bmOperationInfoPMGid = json.loads(req26)["data"]
except KeyError:
    url26 = BaseUrl + "/ime-container/bmOperationInfo/query.action?usedPost=true"
    data26 = {"query":{"query":[{"operator":"and","field":"code","type":"eq","value":"Q13","left":"(","right":")"}]},"pager":{"page":1,"pageSize":10}}
    req26 = requests.post(url26, headers=headers, data=json.dumps(data26)).content.decode()
    bmOperationInfoPMGid = json.loads(req26)["data"][0]["gid"]
print("bmOperationInfoPMGid", bmOperationInfoPMGid)

# 创建离散1工序
url27 = BaseUrl + "/ime-container/bmOperationInfo/add"
data27 = {
    "reportRowNum": "10",
    "bmWorkLineGidRef": {"lineName": "小米离散"},
    "processTest": "true",
    "bmWorkUnitGid": bmFactoryWorkUnitLS,
    "bmWorkCenterGidRef": {"workCenterName": "小米科技"},
    "businessMode": ["start", "end", "process"],
    "worksheetGenarationMode": "workPublishProduce",
    "bmWorkStationGidRef": {"stationName": "离散1"},
    "bmWorkStationGid": bmFactoryWorkStationLS1Gid,
    "name": "离散1",
    "code": "Q21",
    "rhythmType": "hour",
    "bmWorkCenterGid": bmFactoryWorkCenterGid,
    "bmWorkUnitGidRef": {"workUnitName": "小米离散单元"},
    "bmWorkLineGid": bmFactoryLineLS,
    "matEndPoint": "false",
    "rhythm": "1",
    "processingMode": "unlimited",
    "type": "turning"
}
try:
    req27 = requests.post(url27, headers=headers, data=json.dumps(data27)).content.decode()
    bmOperationInfoLS1Gid = json.loads(req27)["data"]
except KeyError:
    url27 = BaseUrl + "/ime-container/bmOperationInfo/query.action?usedPost=true"
    data27 = {"query":{"query":[{"operator":"and","field":"code","type":"eq","value":"Q21","left":"(","right":")"}]},"pager":{"page":1,"pageSize":10}}
    req27 = requests.post(url27, headers=headers, data=json.dumps(data27)).content.decode()
    bmOperationInfoLS1Gid = json.loads(req27)["data"][0]["gid"]
print("bmOperationInfoLS1Gid", bmOperationInfoLS1Gid)

# 创建离散2工序
url28 = BaseUrl + "/ime-container/bmOperationInfo/add"
data28 = {
    "reportRowNum": "10",
    "bmWorkLineGidRef": {"lineName": "小米离散"},
    "processTest": "true",
    "bmWorkUnitGid": bmFactoryWorkUnitLS,
    "bmWorkCenterGidRef": {"workCenterName": "小米科技"},
    "businessMode": ["start", "end", "process"],
    "worksheetGenarationMode": "workPublishProduce",
    "bmWorkStationGidRef": {"stationName": "离散2"},
    "bmWorkStationGid": bmFactoryWorkStationLS2Gid,
    "name": "离散2",
    "code": "Q22",
    "rhythmType": "hour",
    "bmWorkCenterGid": bmFactoryWorkCenterGid,
    "bmWorkUnitGidRef": {"workUnitName": "小米离散单元"},
    "bmWorkLineGid": bmFactoryLineLS,
    "matEndPoint": "false",
    "rhythm": "1",
    "processingMode": "unlimited",
    "type": "turning"
}
try:
    req28 = requests.post(url28, headers=headers, data=json.dumps(data28)).content.decode()
    bmOperationInfoLS2Gid = json.loads(req28)["data"]
except KeyError:
    url28 = BaseUrl + "/ime-container/bmOperationInfo/query.action?usedPost=true"
    data28 = {"query":{"query":[{"operator":"and","field":"code","type":"eq","value":"Q22","left":"(","right":")"}]},"pager":{"page":1,"pageSize":10}}
    req28 = requests.post(url28, headers=headers, data=json.dumps(data28)).content.decode()
    bmOperationInfoLS2Gid = json.loads(req28)["data"][0]["gid"]
print("bmOperationInfoLS2Gid", bmOperationInfoLS2Gid)

# 创建重复工艺
url29 = BaseUrl + "/ime-container/bmRouteLine/add.action"
data29 = {
    "classify": "common",
    "outputNum": "1",
    "trackOrderMode": "workPublishProduce",
    "produceCycle": "1",
    "endTime": "2099-12-31",
    "name": "手机",
    "timeTypeProduceCycle": "hour",
    "code": "Q01",
    "mainMaterielGidRef": {"code": "Q01"},
    "startTime": "2018-05-01",
    "mainMaterieGid": MaterielSJGid,
    "workMode": ["start", "end", "process"],
    "rhythm": "1",
    "version": "1",
    "type": "main",
    "timeTypeRhythm": "hour",
    "mdRouteOperList": [
        {
            "reportRowNum": "10",
            "bmWorkLineGidRef": {"lineName": "小米重复"},
            "processTest": "true",
            "bmWorkUnitGid": bmFactoryWorkUnitCF,
            "bmWorkCenterGidRef": {"workCenterName": "小米科技"},
            "businessMode": "[\"start\",\"end\",\"process\"]",
            "bmOperStepList": [],
            "worksheetGenarationMode": "workPublishProduce",
            "mdDefOperationGid": bmOperationInfoCPUGid,
            "bmWorkStationGidRef":{"stationName": "CPU"},
            "bmWorkStationGid": bmFactoryWorkStationCPUGid,
            "bmOperationGidRef": {"code": "Q11", "name": "CPU", "type": "turning"},
            "rhythmType": "hour",
            "bmWorkCenterGid": bmFactoryWorkCenterGid,
            "bmWorkUnitGidRef": {"workUnitName": "小米重复单元"},
            "bmWorkLineGid": bmFactoryLineCF,
            "eventPayload": {},
            "matEndPoint": "false",
            "rhythm": 1,
            "processingMode": "unlimited"
        },
        {
            "reportRowNum": "20",
            "bmWorkLineGidRef": {"lineName": "小米重复"},
            "processTest": "false",
            "bmWorkUnitGid": bmFactoryWorkUnitCF,
            "bmWorkCenterGidRef": {"workCenterName": "小米科技"},
            "businessMode": "[\"start\",\"end\",\"process\"]",
            "bmOperStepList": [],
            "worksheetGenarationMode": "workPublishProduce",
            "mdDefOperationGid": bmOperationInfoZBGid,
            "bmWorkStationGidRef": {"stationName": "主板"},
            "bmWorkStationGid": bmFactoryWorkStationZBGid,
            "bmOperationGidRef": {"code": "Q12", "name": "主板", "type": "turning"},
            "rhythmType": "hour",
            "bmWorkCenterGid": bmFactoryWorkCenterGid,
            "bmWorkUnitGidRef": {"workUnitName": "小米重复单元"},
            "bmWorkLineGid": bmFactoryLineCF,
            "eventPayload": {},
            "matEndPoint": "false",
            "rhythm": 1,
            "processingMode": "unlimited"
        },
        {
            "reportRowNum": "30",
            "bmWorkLineGidRef": {"lineName": "小米重复"},
            "processTest": "false",
            "bmWorkUnitGid": bmFactoryWorkUnitCF,
            "bmWorkCenterGidRef": {"workCenterName": "小米科技"},
            "businessMode": "[\"start\",\"end\",\"process\"]",
            "bmOperStepList": [],
            "worksheetGenarationMode": "workPublishProduce",
            "mdDefOperationGid": bmOperationInfoPMGid,
            "bmWorkStationGidRef":{"stationName": "屏幕"},
            "bmWorkStationGid": bmFactoryWorkStationPMGid,
            "bmOperationGidRef": {"code": "Q13", "name": "屏幕", "type": "turning"},
            "rhythmType": "hour",
            "bmWorkCenterGid": bmFactoryWorkCenterGid,
            "bmWorkUnitGidRef": {"workUnitName": "小米重复单元"},
            "bmWorkLineGid": bmFactoryLineCF,
            "eventPayload": {},
            "matEndPoint": "false",
            "rhythm": 1,
            "processingMode": "unlimited"
        }
    ]
}
try:
    req29 = requests.post(url29, headers=headers, data=json.dumps(data29)).content.decode()
    bmRouteLineCFGid = json.loads(req29)["data"]
except KeyError:
    url29 = BaseUrl + "/ime-container/bmRouteLine/query.action?usedPost=true"
    data29 = {"query":{"query":[{"operator":"and","field":"code","type":"eq","value":"Q01","left":"(","right":")"}]},"pager":{"page":1,"pageSize":10}}
    req29 = requests.post(url29, headers=headers, data=json.dumps(data29)).content.decode()
    bmRouteLineCFGid = json.loads(req29)["data"][0]["gid"]
print("bmRouteLineCFGid", bmRouteLineCFGid)

# 创建离散工艺
url30 = BaseUrl + "/ime-container/bmRouteLine/add.action"
data30 = {
    "classify": "common",
    "outputNum": "1",
    "trackOrderMode": "workPublishProduce",
    "produceCycle": "1",
    "endTime": "2099-12-31",
    "name": "零件",
    "timeTypeProduceCycle": "hour",
    "code": "Q02",
    "mainMaterielGidRef": {"code": "Q02"},
    "startTime": "2018-05-01",
    "mainMaterieGid": MaterielLJGid,
    "workMode": ["start", "end", "process"],
    "rhythm": "1",
    "version": "1",
    "type": "main",
    "timeTypeRhythm": "hour",
    "mdRouteOperList": [
        {
            "reportRowNum": "10",
            "bmWorkLineGidRef": {"lineName": "小米离散"},
            "processTest": "true",
            "bmWorkUnitGid": bmFactoryWorkUnitLS,
            "bmWorkCenterGidRef": {"workCenterName": "小米科技"},
            "businessMode": "[\"start\",\"end\",\"process\"]",
            "bmOperStepList": [],
            "worksheetGenarationMode": "workPublishProduce",
            "mdDefOperationGid": bmOperationInfoLS1Gid,
            "bmWorkStationGidRef":{"stationName": "离散1"},
            "bmWorkStationGid": bmFactoryWorkStationLS1Gid,
            "bmOperationGidRef": {"code": "Q21", "name": "离散1", "type": "turning"},
            "rhythmType": "hour",
            "bmWorkCenterGid": bmFactoryWorkCenterGid,
            "bmWorkUnitGidRef": {"workUnitName": "小米离散单元"},
            "bmWorkLineGid": bmFactoryLineLS,
            "eventPayload": {},
            "matEndPoint": "false",
            "rhythm": 1,
            "processingMode": "unlimited"
        },
        {
            "reportRowNum": "20",
            "bmWorkLineGidRef": {"lineName": "小米离散"},
            "processTest": "false",
            "bmWorkUnitGid": bmFactoryWorkUnitLS,
            "bmWorkCenterGidRef": {"workCenterName": "小米科技"},
            "businessMode": "[\"start\",\"end\",\"process\"]",
            "bmOperStepList": [],
            "worksheetGenarationMode": "workPublishProduce",
            "mdDefOperationGid": bmOperationInfoLS2Gid,
            "bmWorkStationGidRef": {"stationName": "离散2"},
            "bmWorkStationGid": bmFactoryWorkStationZBGid,
            "bmOperationGidRef": {"code": "Q22", "name": "离散2", "type": "turning"},
            "rhythmType": "hour",
            "bmWorkCenterGid": bmFactoryWorkCenterGid,
            "bmWorkUnitGidRef": {"workUnitName": "小米离散单元"},
            "bmWorkLineGid": bmFactoryLineCF,
            "eventPayload": {},
            "matEndPoint": "false",
            "rhythm": 1,
            "processingMode": "unlimited"
        }

    ]
}
try:
    req30 = requests.post(url30, headers=headers, data=json.dumps(data30)).content.decode()
    bmRouteLineLSGid = json.loads(req30)["data"]
except KeyError:
    url30 = BaseUrl + "/ime-container/bmRouteLine/query.action?usedPost=true"
    data30 = {"query":{"query":[{"operator":"and","field":"code","type":"eq","value":"Q02","left":"(","right":")"}]},"pager":{"page":1,"pageSize":10}}
    req30 = requests.post(url30, headers=headers, data=json.dumps(data30)).content.decode()
    bmRouteLineLSGid = json.loads(req30)["data"][0]["gid"]
print("bmRouteLineLSGid", bmRouteLineLSGid)
