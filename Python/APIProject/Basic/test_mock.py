# encoding: utf-8
from unittest import  mock
import  requests


def sendRequest(url):
    res = requests.get(url).status_code
    return res

def mockTest():
    return sendRequest("http://www.ustack.com")