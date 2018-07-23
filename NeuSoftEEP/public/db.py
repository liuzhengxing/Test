# _*_ coding=utf-8 _*_

import pymysql

from public import params

domain = params.mysqldomain
user = params.msuser
passwd = params.mspasswd


def getconn():
    conn = pymysql.connect(host=domain, user=user, passwd=passwd, db="autotest", charset="utf8")
    return conn


if __name__ == '__main__':
    getconn()
