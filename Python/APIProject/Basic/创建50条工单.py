# encoding: utf-8

# encoding: utf-8

import requests
import json
import random

url_update = "http://192.168.138.132/ime-container/imeWorkOrder/insertWorkOrder.action"

headers = {'Content-Type': 'application/json'}


def testCreate():
    data = {
    "factoryLineGid": "025ed5d6688d40ca93d13ce29ba50d34",
    "orderType": "62DC90DAFA8C5CB2E055000000000001",
    "orderTypeRef": {
        "name": "类型二"
    },
    "materialRef": {
        "code": "per10",
        "name": "性能测试10",
        "bmMeasurementUnitGidRef": {
            "name": "米"
        },
        "bmMeasurementUnitGid": "858dc0608deb4034833d0abad1f9f31e"
    },
    "code": 'API' + str(random.randint(10000, 99999)),
    "planBeginTime": "2018-05-01 16:40:23",
    "planQty": "10",
    "workCenterRef": {
        "workCenterName": "测试工作中心",
        "workCenterCode": "cs001"
    },
    "imeWorkOrderBoms": [
        {
            "orderQty": 10,
            "factoryStationRef": {
                "stationCode": "x001",
                "gid": "c8249cc7e35f4f59a0e00e991c5322bf",
                "stationName": "x001"
            },
            "reviewGid": "true",
            "materialRef": {
                "code": "per2640",
                "name": "性能测试2640",
                "bmWarehouseGidRef": {}
            },
            "planQty": 1,
            "warehouseRef": {},
            "materialNumber": 1,
            "routeLineRef": {},
            "productNumber": 1,
            "factoryStationGid": "c8249cc7e35f4f59a0e00e991c5322bf",
            "materialGid": "c016d0b6b3694a7fb5d0e4583090eda5"
        },
        {
            "orderQty": 10,
            "factoryStationRef": {
                "stationCode": "x001",
                "gid": "c8249cc7e35f4f59a0e00e991c5322bf",
                "stationName": "x001"
            },
            "reviewGid": "false",
            "materialRef": {
                "code": "per2641",
                "name": "性能测试2641",
                "bmWarehouseGidRef": {}
            },
            "planQty": 1,
            "warehouseRef": {},
            "materialNumber": 1,
            "routeLineRef": {},
            "productNumber": 1,
            "factoryStationGid": "c8249cc7e35f4f59a0e00e991c5322bf",
            "materialGid": "b488495a4f724cf28bf02094156d965f"
        },
        {
            "orderQty": 10,
            "factoryStationRef": {
                "stationCode": "x001",
                "gid": "c8249cc7e35f4f59a0e00e991c5322bf",
                "stationName": "x001"
            },
            "reviewGid": "false",
            "materialRef": {
                "code": "per2642",
                "name": "性能测试2642",
                "bmWarehouseGidRef": {}
            },
            "planQty": 1,
            "warehouseRef": {},
            "materialNumber": 1,
            "routeLineRef": {},
            "productNumber": 1,
            "factoryStationGid": "c8249cc7e35f4f59a0e00e991c5322bf",
            "materialGid": "15c530d0764347b7991eb848ccf8622b"
        },
        {
            "orderQty": 10,
            "factoryStationRef": {
                "stationCode": "x001",
                "gid": "c8249cc7e35f4f59a0e00e991c5322bf",
                "stationName": "x001"
            },
            "reviewGid": "false",
            "materialRef": {
                "code": "per2643",
                "name": "性能测试2643",
                "bmWarehouseGidRef": {}
            },
            "planQty": 1,
            "warehouseRef": {},
            "materialNumber": 1,
            "routeLineRef": {},
            "productNumber": 1,
            "factoryStationGid": "c8249cc7e35f4f59a0e00e991c5322bf",
            "materialGid": "ef83d92c98164fc6af524edf238b0154"
        },
        {
            "orderQty": 10,
            "factoryStationRef": {
                "stationCode": "x001",
                "gid": "c8249cc7e35f4f59a0e00e991c5322bf",
                "stationName": "x001"
            },
            "reviewGid": "true",
            "materialRef": {
                "code": "per2644",
                "name": "性能测试2644",
                "bmWarehouseGidRef": {}
            },
            "planQty": 1,
            "warehouseRef": {},
            "materialNumber": 1,
            "routeLineRef": {},
            "productNumber": 1,
            "factoryStationGid": "c8249cc7e35f4f59a0e00e991c5322bf",
            "materialGid": "dd118c6783484813939c3e073cc2c1de"
        },
        {
            "orderQty": 10,
            "factoryStationRef": {
                "stationCode": "x001",
                "gid": "c8249cc7e35f4f59a0e00e991c5322bf",
                "stationName": "x001"
            },
            "reviewGid": "false",
            "materialRef": {
                "code": "per2645",
                "name": "性能测试2645",
                "bmWarehouseGidRef": {}
            },
            "planQty": 1,
            "warehouseRef": {},
            "materialNumber": 1,
            "routeLineRef": {},
            "productNumber": 1,
            "factoryStationGid": "c8249cc7e35f4f59a0e00e991c5322bf",
            "materialGid": "37b40a21ba06483a8b0c27a04756fc2a"
        },
        {
            "orderQty": 10,
            "factoryStationRef": {
                "stationCode": "x001",
                "gid": "c8249cc7e35f4f59a0e00e991c5322bf",
                "stationName": "x001"
            },
            "reviewGid": "false",
            "materialRef": {
                "code": "per2646",
                "name": "性能测试2646",
                "bmWarehouseGidRef": {}
            },
            "planQty": 1,
            "warehouseRef": {},
            "materialNumber": 1,
            "routeLineRef": {},
            "productNumber": 1,
            "factoryStationGid": "c8249cc7e35f4f59a0e00e991c5322bf",
            "materialGid": "1aebea8aa6e74564bc07b9c60f68bc5b"
        },
        {
            "orderQty": 10,
            "factoryStationRef": {
                "stationCode": "x001",
                "gid": "c8249cc7e35f4f59a0e00e991c5322bf",
                "stationName": "x001"
            },
            "reviewGid": "false",
            "materialRef": {
                "code": "per2647",
                "name": "性能测试2647",
                "bmWarehouseGidRef": {}
            },
            "planQty": 1,
            "warehouseRef": {},
            "materialNumber": 1,
            "routeLineRef": {},
            "productNumber": 1,
            "factoryStationGid": "c8249cc7e35f4f59a0e00e991c5322bf",
            "materialGid": "c27bdf2f7a2b442da2989479f007643d"
        },
        {
            "orderQty": 10,
            "factoryStationRef": {
                "stationCode": "x001",
                "gid": "c8249cc7e35f4f59a0e00e991c5322bf",
                "stationName": "x001"
            },
            "reviewGid": "true",
            "materialRef": {
                "code": "per2648",
                "name": "性能测试2648",
                "bmWarehouseGidRef": {}
            },
            "planQty": 1,
            "warehouseRef": {},
            "materialNumber": 1,
            "routeLineRef": {},
            "productNumber": 1,
            "factoryStationGid": "c8249cc7e35f4f59a0e00e991c5322bf",
            "materialGid": "2b7ddf15f4d84002bc141e911a6aca3e"
        },
        {
            "orderQty": 10,
            "factoryStationRef": {
                "stationCode": "x001",
                "gid": "c8249cc7e35f4f59a0e00e991c5322bf",
                "stationName": "x001"
            },
            "reviewGid": "false",
            "materialRef": {
                "code": "per2649",
                "name": "性能测试2649",
                "bmWarehouseGidRef": {}
            },
            "planQty": 1,
            "warehouseRef": {},
            "materialNumber": 1,
            "routeLineRef": {},
            "productNumber": 1,
            "factoryStationGid": "c8249cc7e35f4f59a0e00e991c5322bf",
            "materialGid": "7c7e60b4a4724eb395c6abf27d8cd650"
        }
    ],
    "surplusOrderFlag": "false",
    "productGid": "c13d04161db14120bc93a3f3d5662f07",
    "factoryLineRef": {
        "lineCode": "cs001",
        "lineName": "离散型产线"
    },
    "factoryLineType": "DISCRETE",
    "smBusiUnitGidRef": {
        "busiUnitName": "测试业务单元"
    },
    "materialGid": "a2ef229d40f64512a8a87c299e941936",
    "smBusiUnitGid": "b4edac62b0d8486da7590008e3a732bd",
    "workOrderCategory": "normal",
    "workCenterGid": "31b0691ed3124a1992059fe8fa728533",
    "planEndTime": "2018-05-14 16:40:45"
}

    resp = requests.post(url=url_update,headers=headers,data=json.dumps(data)).text

    print(resp)



count = 0

# while(count<3):
#     testCreate()
#     count =count+1


for i in range(50):
    testCreate()
