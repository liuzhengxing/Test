# encoding: utf-8

import requests
import json

urlCreate = "http://192.168.138.54:9080/ime-container/bmRouteLine/add.action"
urlDelete = 'http://192.168.138.54:9080/ime-container/bmRouteLine/delete'
headers = {'Content-Type': 'application/json'}
dataCreate = '{"bmOperStepList":[],"classify":"common","outputNum":"10","trackOrderMode":"workPublishProduce","produceCycle":"10","name":"route0315001","timeTypeProduceCycle":"minute","code":"20180315001","workMode":["start","end","process"],"rhythm":"10","version":"1.1","type":"main","timeTypeRhythm":"minute","mdRouteOperList":[]}'
dataDelete = '["672456427b934e0093951e51635576f8"]'

class apiTest():
    # create route, and get the gid from response
    def create(self):
        response = requests.post(url=urlCreate,headers=headers,data=dataCreate).text
        responseData = json.loads(response)
        gid = responseData['data']
        if "data" in responseData and "success" in responseData:
            print("OK, add success")
        else:print("add failed")
        return gid

    # change the gid to json, and delete the route
    def delete(self,gid):
        gidJson = json.dumps(gid)
        response = requests.post(url=urlDelete,headers=headers,data='['+gidJson+']').text
        if "success" in response:
            print("OK, delete success")
        else:print("delete failed")


t = apiTest()
gid = t.create()
#t.delete(gid)

