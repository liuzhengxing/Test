# encoding: utf-8
import xlrd
import requests
import json


#定义excel文件地址
fname = 'C:\\Users\\admin\\Desktop\\material.xlsx'
bk = xlrd.open_workbook(fname,"rb")
sh = bk.sheet_by_name("material")

#sheet页的行数和列数
nrows = sh.nrows
nclos = sh.ncols


#循环读取每一行的数据并写入到list中
row_list = []
for i in range(1,nrows):
    row_data = sh.row_values(i)
    row_list.append(row_data)

# print(row_list)

#把list中的数据拼接成json串
listLength = len(row_list)
finalData = []
for i in range(0,listLength):
    data = {
        "bomNumber": "10",
        "denoNumber": "1",
        "pivotal": "false",
        "moleculeNumber": "10",
        "mdMaterialGidRef": {
            "code": row_list[i][0],
            "name": "物流重复1"
        },
        "useNumber": "0.00",
        "substitute": "no",
        "validBeginTime": "2018-05-18 10:47:43",
        "materialGid": row_list[i][1],
        "dosageScheme": "BOM_NUMBER"
    }
    finalData.append(data)



# print(finalData)

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

# print(BOM)
url_update = "http://192.168.138.132/ime-container/bmProductInfo/add.action"

headers = {'Content-Type': 'application/json'}

resp = requests.post(url=url_update,headers=headers,data=json.dumps(BOM)).text