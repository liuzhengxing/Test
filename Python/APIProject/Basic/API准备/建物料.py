# encoding: utf-8
import requests
import  json

url= 'http://192.168.138.132/ime-container/bmMaterielInfo/add.action'



headers = {'Content-Type': 'application/json'}

for i in range(3):
    data = {
    "productionBatch": "false",
    "versionNumber": "1.2.2",
    "isVirtual": "false",
    "optionMark": "false",
    "barCodeManagement": "false",
    "replacementPart": "false",
    "resources": "false",
    "bmMeasurementUnitGidRef": {
        "name": "台"
    },
    "outsourcing": "false",
    "sparePart": "false",
    "name": "performance0523",
    "traceBack": "false",
    "code": "WL0523" + str(i),
    "bmMeasurementUnitGid": "7aab8c66af1e43668191437b42e00a60",
    "qualityAssurance": "false",
    "equipment": "false",
    "serialNumManagement": "false",
    "substitute": "false",
    "homemadePiece": "false",
    "productionPath": "false",
    "consumptivePart": "false",
    "purchaseParts": "false"
}
    res = requests.post(url=url,headers=headers,data=json.dumps(data)).text
    print(res)

