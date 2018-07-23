# encoding: utf-8

import requests
import random
import json
import Basic.dataPrepare as d

url_Create = d.dev.url_Create
url_Delete = d.dev.url_Delete
headers = {'Content-Type': 'application/json'}
postfix = str(random.randint(10000,99999))

# 方法：创建不带无工序质检项目
def QualityItemCreate():

    data = {"mode":"modify","code":"item" + postfix,"name":"大飞机"}

    res = requests.post(url=url_Create,data=json.dumps(data),headers = headers).text

    gid = json.loads(res)['data']

    return gid

# 方法：删除无工序质检项目
def QualityDelete():

    gid = QualityItemCreate()

    data = '[' + json.dumps(gid) + ']'

    res = requests.post(url=url_Delete,data=data,headers = headers).text

    print(res)

QualityDelete()