# encoding: utf-8

import  requests


class apiTest():
    def __init__(self):
        self.url = "http://192.168.138.54:9080/ime-container/bmRouteLine/add.action"
        self.headers = {'Content-Type': 'application/json'}
        self.data = '{"bmOperStepList":[],"classify":"common","outputNum":"10","trackOrderMode":"workPublishProduce","produceCycle":"10","name":"route0315001","timeTypeProduceCycle":"minute","code":"20180315001","workMode":["start","end","process"],"rhythm":"10","version":"1.1","type":"main","timeTypeRhythm":"minute","mdRouteOperList":[]}'

    def test(self):
        responseData = requests.post(url=self.url,headers=self.headers,data=self.data).text
        if "data" in responseData and "success" in responseData:
            print("OK")


t = apiTest()
t.test()

