from jsonschema import validate
from 测试用例.接口自动化_V2.接口测试.public_method import neu_reqeust as nr

kwargs = {}


class PlanOrder:

    def planorder_create(self, data):
        schema = {
            'type': 'object',
            'properties': {
                'code': {'type': 'string'},
                'workCenterGid': {'type': 'string'},
                'orderType': {'type': 'string'},
                'materialGid': {'type': 'string'},
                'planQty': {'type': 'number'},
                'factoryLineGid': {'type': 'string'}
            },
            'required': [
                'code',
                'factoryLineGid',
                'workCenterGid',
                'orderType',
                'materialGid',
                'planQty',
                'planBeginTime',
                'planEndTime'
            ]
        }
        validate(data, schema)

        kwargs.setdefault('method', 'POST')
        kwargs.setdefault('url', '/ime-container/imePlanOrder/insertPlanOrder.action')
        kwargs.setdefault('data', data)
        req = nr(**kwargs)
        return req