# _*_coding: utf-8 _*_

import time
import requests
from unittest import TestCase
from public import db as db, params
from public.zentao import Zentao

vid = params.vid
t = params.t


class RunCase(TestCase):
    def runcase(self, caseid):
        headers = {
            'Content-Tpye': 'application/json'
        }
        conn = db.getconn()
        cursor = conn.cursor()
        runtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        case = Zentao()
        caseinfo = case.getcaseinfo(caseid)
        # print(caseinfo)

        # 标题
        casetitle = caseinfo[1]
        # print('casetitle', casetitle)

        # 前置
        beforestep = caseinfo[2]
        # print('beforestep:', beforestep)

        # 步骤
        casesteps = caseinfo[3]

        req = None
        # 判断是否需要登录
        if beforestep is not '':
            print('-------------有登录')
            loginstep = casesteps[0]
            # print('loginstep', loginstep)
            session = requests.Session()
            loginheads = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            session.post(loginstep[0], headers=loginheads, data=loginstep[1]).content.decode()

            for casestep in casesteps[1:]:
                # 判断请求方式
                if casestep[1] == 'NULL':
                    req = session.get(url=casestep[0], headers=headers).content.decode()
                else:
                    # data = json.dumps(casestep[1])
                    # print(data)
                    req = session.post(url=casestep[0], headers=headers, data=casestep[1].encode('utf-8'))\
                        .content.decode()
        else:
            for casestep in casesteps:
                # 判断请求方式
                if casestep[1] == 'NULL':
                    req = requests.get(url=casestep[0], headers=headers).content.decode()
                else:
                    req = requests.post(url=casestep[0], headers=headers, data=casestep[1]).content.decode()

        # print(req)

        if caseinfo[4] in str(req).replace('\n', ''):
            testres = 'Pass'
        else:
            testres = 'Fail'
        value = (caseid, casetitle, testres, runtime, vid, t)
        cursor.execute("INSERT INTO autotest_casemodels(caseid, title, result, testdate, vid, t) "
                            "VALUES(%s, %s, %s, %s, %s, %s)", value)
        conn.commit()
        conn.close()
        TestCase.assertIn(self, member=caseinfo[4], container=str(req).replace('\n', ''))


if __name__ == '__main__':
    # t1 = RunCase()
    # t1.test_send(1)
    t2 = RunCase()
    t2.runcase(1)
