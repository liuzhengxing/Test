# encoding: utf-8
# encoding: utf-8

# encoding: utf-8

import requests
import json


head = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/65.0.3325.162 Safari/537.36'

}
url = 'http://pms.neusofthuiju.com:8169/pms/login'

# time1 = time.time()
# print('time1:', time1)
ses = requests.session()
ses.get(url, headers=head)

url2 = 'http://pms.neusofthuiju.com:8169/pms/randomcode.jpg'
req = ses.get(url2, headers=head)
# time2 = time.time()
# print('time2:', time2)
print(req)
with open('d:\\test.jpg', "wb") as f:
    for chunk in req:  # 读取每个图片链接的二进制数据
        f.write(chunk)  # 写入

url3 = 'http://pms.neusofthuiju.com:8169/pms/login'
ra = input('What is your name?')
data = 'username=10001704&password=Workhard1&random=' + ra
req = ses.post(url3, headers=head, data=data).content.decode()
# print(req)


url4 = 'http://pms.neusofthuiju.com:8169/pms/pmsDrJobRptPj/insert'
data2 = {"subBizCode":"900001715991","subopportunityName":"产品四部数字化企业运营平台","drDate":"2018-03-12","startHour":"09:00","endHour":"18:00","milestoneId":"90000171599101","content":"质量管理用例编写","workMode":"N","opportunityProjectChose":"P","reportedBy":"10001704","reportedName":"刘正兴","reportedByType":"0"}
head2 = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/65.0.3325.162 Safari/537.36'}
resb = ses.post(url4,headers=head2,data=json.dumps(data2)).content.decode()
print(resb)