# _*_coding: utf-8_*_

import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders


def sendmail(subject, filename):
    fromo = '齐振鋆<qizhy@neusoft.com>'
    to = ['齐振鋆<qizhy@neusoft.com>']
    cc = ['齐振鋆<qizhy@neusoft.com>']
    bcc = ['15388511@qq.com']
    msg = MIMEMultipart('related')
    msg['To'] = ','.join(to)
    msg['CC'] = ','.join(cc)
    msg['Subject'] = subject
    content = MIMEText('''\
        FYI
    ''', 'plain')
    msg.attach(content)
    signature = MIMEText('''\
<html>
    <body>
        </br>
        Best regards,</br>
        -----------------------------------------------------</br>
        齐振鋆</br>
        <small>产品事业二部 测试工程师</small></br>
        <big><b>北京东软慧聚信息技术股份有限公司</b></big></br>
        <small>地址：武汉市洪山区文化大道555号融创智谷A6栋301</br>
        电话：(86)88238233</br>
        手机：13476818175</br>
        邮箱：qizhy@neusoft.com</br>
        网址：<a href="http://www.neusoft.com">http://www.neusoft.com</a></small>
    </body>
</html>
    ''', 'html', 'utf-8')
    msg.attach(signature)

    # 添加附件
    attfile = filename
    basename = os.path.basename(attfile)
    fp = open(attfile, 'rb')
    att = MIMEText(fp.read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=('gbk', '', basename))
    encoders.encode_base64(att)
    msg.attach(att)

    # -----------------------------------------------------------
    s = smtplib.SMTP()
    s.connect('smtp.neusoft.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('qizhy', '81p@4QC2')
    # toaddrs = to + cc + bcc
    toaddrs = to
    s.sendmail(fromo, toaddrs, msg.as_string())
    print('发送成功')
    s.quit()


if __name__ == '__main__':
    # print(os.getcwd())
    sendmail('接口自动化测试报告_2018-01-16 17-34-59', 'D:\\NeuSoftEEP\\report\\接口自动化测试报告_2018-01-16 17-34-59.html')