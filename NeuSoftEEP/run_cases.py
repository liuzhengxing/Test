# -*- coding: utf-8 -*-

import time

from 测试用例 import test_case
from public import params, HTMLTestRunnerCN

# 测试版本维护
# vid = params.vid
# vname = params.vname
# conn = db.getconn()
# c = conn.cursor()
# c.execute("SELECT COUNT(id) from autotest_versionmodels WHERE vid=%s", vid)
# if c.fetchone()[0] == 0:
#     c.execute("INSERT INTO autotest_versionmodels(vid, vname) VALUES(%s, %s)", (vid, vname))
#     conn.commit()l
# conn.close()

# 执行测试
basedir = params.BaseDir
tu = test_case.creatsuite()
# 取前面时间
now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
title = 'IME接口测试报告' + '_' + now
# 把当前时间加到报告中
filename = basedir + '\\report\\' + title + '_' + now + '.html'
fp = open(filename, 'wb')
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title=title, description=u'用例执行情况：')

# 执行测试用例
runner.run(tu)
time.sleep(3)
# 发送邮件
# send_mail.sendmail(title, filename)
