# encoding: utf-8
from unittest import mock

headers = {'Content-Type': 'application/json'}
para_in = {"processTest":"false","stepCode":"GB0713001","stepName":"API-GB"}
para_out = {
	"data":"af42124126e64075b16806f4f3945baf",
	"success":"true"
                }

class API():
    def add(self):
        return 1+1


api = API()
api.add = mock.Mock(return_value=para_out,side_effect=api.add)

result = api.add()
    # requests.post(url="http://192.168.138.132/ime-container/bmStepInfo/add",headers=headers,data=data).text()

print(result)

