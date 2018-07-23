# encoding: utf-8
from unittest import mock
import unittest
class Count():

    def add(self,a,b):
        a = 6
        return a + b


    def devide(self):
        pass

count = Count()
count.add = mock.Mock(return_value=10,side_effect=count.add)
result = count.add(4,5)
print(result)
