# -*-coding: utf-8 -*-

import requests

from bs4 import BeautifulSoup
from public import params

domain = params.cddomain
account = params.cduser
password = params.cdpasswd


class Zentao():
    def __init__(self):
        self.loginurl = 'http://' + domain + '/zentao/user-login.html'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/63.0.3239.108  '
                          'Safari/537.36'
        }
        self.data = {
            'account': account,
            'password': password,
            'referer': 'http://' + domain + '/zentao/my/'
        }

    def login(self):
        session = requests.Session()
        session.post(self.loginurl, headers=self.headers, data=self.data)
        return session

    def getcaseinfo(self, caseid):
        session = self.login()
        caseurl = 'http://' + domain + '/zentao/testcase-view-' + str(caseid) + '.html'
        html = session.get(caseurl).content.decode()
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)

        # 用例标题
        title = soup.select('.heading')[0].find_all('strong')[1].get_text()
        # print('############', title)

        # 前置条件登录
        beforestep = soup.select('fieldset')[0].get_text().split(u'前置条件')[1].replace('\n', '').strip()
        # print(beforestep)

        # 用例步骤
        teststeps = []
        steps = soup.select('.step-group')
        # print('############', steps)
        for step in steps:
            url = step.select('.input-group')[0].get_text()
            data = step.select('.text-left')[1].get_text()
            teststep = url, data
            teststeps.append(teststep)
        # print(teststeps)

        # 检查点
        checkpoint = soup.select('.table-borderless')[0].find_all('tr')[-1].select('td')[0].get_text()
        # print('############', checkpoint)
        return caseid, title, beforestep, teststeps, checkpoint


if __name__ == '__main__':
    p = Zentao()
    p.getcaseinfo(2)
