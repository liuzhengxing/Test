import unittest

from unittest.mock import Mock
from 测试用例.接口自动化_V2.接口管理.订单 import PlanOrder
kwargs = {}


class TestPlanOrder(unittest.TestCase):
    """订单测试类"""

    def setUp(self):
        self.po = PlanOrder()

    def test_planorder_create1(self):
        """订单创建接口测试：输入正确的必填项生成订单"""
        mock_status = False
        mock_data = {
            "code": "$code",
            "workCenterGid": "$workCenterGid",
            "orderType": "62DC90DAFA845CB2E055000000000001",
            "materialGid": "$materialGid",
            "materialVersion": "1",
            "planBeginTime": "2018-05-04",
            "planEndTime": "2018-05-14",
            "planQty": "10",
            "finishQty": "",
            "publishedQty": "",
            "qualifiedQty": "",
            "unqualifiedQty": "",
            "wasteQty": "",
            "orderStatus": "",
            "planOrderSource": "",
            "planOrderCategory": "normal",
            "factoryLineGid": "$factoryLineGid",
            "actualBeginTime": "",
            "actualEndTime": "",
            "measureBeginTime": "",
            "measureEndTime": "",
            "bomStatus": "",
            "processStatus": "",
            "canOperation": "",
            "surplusOrderFlag": ""
        }

        mock_resp = {
            'data': 'DDIENFB321GFDSK90AGV2DF90GA9F',
            'success': 'True'
        }
        if mock_status:
            self.po.planorder_create = Mock(return_value=mock_resp)
        else:
            self.po.planorder_create = Mock(return_value=mock_resp, side_effect=self.po.planorder_create)
        self.assertEqual(self.po.planorder_create(mock_data), mock_resp)


if __name__ == '__main__':
    unittest.main()