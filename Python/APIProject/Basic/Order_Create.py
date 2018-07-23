# encoding: utf-8

import requests
import json
import random

url_update = "http://192.168.138.191:9080/ime-container/imePlanOrder/insertPlanOrder.action"

headers = {'Content-Type': 'application/json'}


def testCreate():
    data = {
        "code": 'API' + str(random.randint(10000, 99999)),  # 编码--非空
        "workCenterGid": "0aad8f6efdbb404c94296965918d1a9d",  # 工作中心--非空
        "orderType": "ss",  # 订单类型
        "materialGid": "2e178a4731304d8f9b959e685fed0228",  # 物料Gid--非空
        "materialVersion": "1",  # 物料版本（冗余）--非空
        "planBeginTime": "2018-01-04",  # 计划开始时间--非空
        "planEndTime": "2018-01-14",  # 计划完成时间--非空
        "planQty": "50",  # 生产订单数量--非空
        "finishQty": "",  # 已完工数量
        "publishedQty": "",  # 已下发数量
        "qualifiedQty": "",  # 合格数量
        "unqualifiedQty": "",  # 不合格数量
        "wasteQty": "",  # 废品数量
        "orderStatus": "",  # 订单状态
        "planOrderSource": "",  # 生产订单来源
        "planOrderCategory": "normal",  # 订单类别
        "orderSeq": "",  # 订单顺序
        "factoryLineGid": "",  # 产线
        "actualBeginTime": "",  # 实际开始时间
        "actualEndTime": "",  # 实际结束时间
        "measureBeginTime": "",  # 测算开始时间
        "measureEndTime": "",  # 测算结束时间
        "bomStatus": "",  # BOM状态
        "processStatus": "",  # 订单进程
        "canOperation": "",  # 是否可操作
        "surplusOrderFlag": ""  # 是否余量订单
    }

    resp = requests.post(url=url_update,headers=headers,data=json.dumps(data)).text

    print(resp)



count = 0

# while(count<3):
#     testCreate()
#     count =count+1


for i in range(2):
    testCreate()