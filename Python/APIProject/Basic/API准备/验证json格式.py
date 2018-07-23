# encoding: utf-8
import json
data = {
        "gid": "",
        "materialGid": "0a2ee0d993ec4686899cb0457e73a356",
        "materialCode": "9800",
        "materialName": "",
        "pivotal": "",
        "replaceBom": "",
        "startTime": "",
        "endTime": "",
        "baseUnit": "",
        "baseQuantity": "5",
        "version": "" ,
        "imepProdBomDetailList": [
            {
                "gid": "",
                "rowNumber": "",
                "imeProdBomInfoGid": "",
                "bomNumber": "",
                "materialGid": "",
                "materialUnit": "",
                "parentGid": "",
                "routeOperationGid":"",
                "routeOperationCode":"",
                "routeOperationName":"",
                "lossRate": "",
                "materialNumber": "",
                "productNumber": "",
                "pivotal": "",
                "virtual": "",
                "substitute": "",
                "optional": "",
                "useNumber": "",
                "dosageScheme": "",
                "factoryStationGid": "",
                "validBeginTime": "",
                "validEndTime": "",
                "version":""
            },
            {
                "gid": "",
                "rowNumber": "",
                "imeProdBomInfoGid": "",
                "bomNumber": "",
                "materialGid": "b65b4d2ffb064e61b02f797d895cb79a",
                "materialUnit": "",
                "parentGid": "",
                "routeOperationGid":"",
                "routeOperationCode":"",
                "routeOperationName":"",
                "lossRate": "",
                "materialNumber": "",
                "productNumber": "",
                "pivotal": "",
                "virtual": "",
                "substitute": "",
                "optional": "",
                "useNumber": "",
                "dosageScheme": "",
                "factoryStationGid": "",
                "validBeginTime": "",
                "validEndTime": "",
                "version":""
            }
        ]
    }

# jsonData = json.dumps(data)
print(data["materialGid"])