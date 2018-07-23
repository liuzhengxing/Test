import json
import requests

from public import params

BaseUrl = params.BaseUrl
Headers = {
    'Content-Type': 'application/json'
}


def neu_reqeust(**kwargs):
    """
    :param kwargs: 请求数据
    :return:
    """
    resp = None
    method = kwargs.pop('method')
    url = BaseUrl + kwargs.pop('url')
    if method == 'GET':
        resp = requests.get(url).content.decode()
    elif method == 'POST':
        if 'data' in kwargs.keys():
            data = kwargs.pop('data')
            resp = requests.post(url, headers=Headers, data=json.dumps(data)).content.decode()
        else:
            resp = requests.post(url, headers=Headers).content.decode()
    return resp