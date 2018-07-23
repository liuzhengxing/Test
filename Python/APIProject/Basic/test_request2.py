# encoding: utf-8
# encoding: utf-8

import  requests

url = "http://192.168.138.54:9080/ime-container/bmRouteLine/add.action"
headers = {'Content-Type': 'application/json'}
data = '{"bmOperStepList":[],"classify":"common","outputNum":"10","trackOrderMode":"workPublishProduce","produceCycle":"10","name":"route0315001","timeTypeProduceCycle":"minute","code":"20180315001","workMode":["start","end","process"],"rhythm":"10","version":"1.1","type":"main","timeTypeRhythm":"minute","mdRouteOperList":[]}'

def runCase():
    responseData = requests.post(url=url, data=data, headers=headers).text

    if "data" in responseData and "success" in responseData:
        print("OK")

    print(responseData)


runCase()
