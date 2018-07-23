# encoding: utf-8
import datetime
import time

#取当前时间，并且查看时间类型
# now = datetime.datetime.now()
# print(type(now.hour))



def func():

    print("test crontab")


def runtime(h,m):

    now = datetime.datetime.now()
    if str(now.hour) == h and str(now.minute)==m:
        func()

runtime("16","51")