# encoding: utf-8
import json
data = {
    "bmProductDetialList": [
        {
            "bomNumber": "10",
            "denoNumber": "1",
            "validEndTime": "2018-05-31 09:50:05",
            "pivotal": "true",
            "moleculeNumber": "10",
            "mdMaterialGidRef": {
                "code": "Q13",
                "name": "屏幕",
                "spec": "屏幕",
                "model": "夏普",
                "bmMeasurementUnitGidRef": {
                    "name": "件"
                }
            },
            "useNumber": "0.00",
            "validBeginTime": "2018-05-04 09:50:05",
            "materialGid": "fec61ca513b44a9c8653a5f66ab50dcc",
            "dosageScheme": "BOM_NUMBER"
        },
        {
            "bomNumber": "10",
            "denoNumber": "1",
            "validEndTime": "2018-05-31 09:50:05",
            "pivotal": "true",
            "moleculeNumber": "10",
            "mdMaterialGidRef": {
                "code": "Q12",
                "name": "主板",
                "spec": "主板",
                "model": "黑板",
                "bmMeasurementUnitGidRef": {
                    "name": "件"
                }
            },
            "useNumber": "0.00",
            "substitute": "no",
            "validBeginTime": "2018-05-04 09:50:05",
            "materialGid": "2b6054e19b47481caddc880279f3c08f",
            "dosageScheme": "BOM_NUMBER"
        }
    ],
    "endTime": "2099-12-31",
    "replaceBom": "host_bom",
    "pivotal": "true",
    "startTime": "2018-05-04 09:49:50",
    "mdMaterialGidRef": {
        "code": "2e178a4731304d8f9b959e685fed0228",
        "name": "手机重复",
        "bmMeasurementUnitGidRef": {
            "name": "台"
        },
        "spec": "至尊陶瓷",
        "model": "MI6",
        "figureNumber": "1"
    },
    "version": "121",
    "bomType": "produce_bom",
    "materialGid": "2e178a4731304d8f9b959e685fed0228"
}


arr1 = []
for i in range(1,10):

    data1 = {
            "bomNumber": "10",
            "denoNumber": "1",
            "validEndTime": "2018-05-31 09:50:05",
            "pivotal": "true",
            "moleculeNumber": "10",
            "mdMaterialGidRef": {
                "code": "pre" + str(i),
                "name": "屏幕",
                "spec": "屏幕",
                "model": "夏普",
                "bmMeasurementUnitGidRef": {
                    "name": "件"
                }
            },
            "useNumber": "0.00",
            "validBeginTime": "2018-05-04 09:50:05",
            "materialGid": "fec61ca513b44a9c8653a5f66ab50dcc",
            "dosageScheme": "BOM_NUMBER"
        }

    arr1.append(data1)

print(arr1)


arr2 = ''
arr3 = []
for i in range(1,10):

    data2 = 'pre' + str(i)
    arr2 += data2
    arr3.append(data2)
print(arr2)
print(arr3)









