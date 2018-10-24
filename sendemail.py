# !/sur/bin/env python
# _*_ coding : utf-8 _*_

"""
发送邮件
"""

import os
import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText
from email import encoders
from email.utils import parseaddr ,formataddr


print(__doc__)

MAIL_ENCODING = "utf-8"

def formatAddr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name,MAIL_ENCODING).encode(), addr))

mail_host = "smtp.163.com"

sender = os.environ['mail_send']
password = os.environ['password']
receivers = os.environ['mail_rece']


content = "邮件..,内容待更新"

def sendMail():
    message = MIMEText(content,'plain','utf-8')
    message['From'] = formatAddr('管理员<%s>'%sender)
    message['To'] = formatAddr('接收<%s>'%receivers)
    subject = "你好"
    message['subject'] = Header(subject,MAIL_ENCODING).encode()

    try:
        s = smtplib.SMTP(mail_host,"25")
        s.login(sender,password)
        s.sendmail(sender,receivers,message.as_string())
        s.quit()

        print("发送成功")

    except smtplib.SMTPException as e:
        print("error: %s"%e)


if __name__ =="__main__":
    sendMail()



