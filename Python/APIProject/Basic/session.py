# encoding: utf-8
import requests

'''.........................................................................'''

zentao_url = 'http://192.168.138.99:81/zentao/user-login-L3plbnRhby9teS5odG1s.html'

data = "account=liuzhengxing&password=bdb2488f5e41acb566b6584b1fa212ce&referer=%2Fzentao%2Fmy.html"


head = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/65.0.3325.162 Safari/537.36'

}

ses = requests.session()

ses.post(url = zentao_url,data=data,headers = head)

'''......................................................................'''
zentao_url2 = 'http://192.168.138.99:81/zentao/bug-browse.html'


rep = ses.get(url = zentao_url2 ,headers = head).text
print(rep)