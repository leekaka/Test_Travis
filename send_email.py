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

from common import *
from get_weather_info import *

print(__doc__)

def formatAddr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name,MAIL_ENCODING).encode(), addr))



content = get_content()
content = "lika,shishi"

def sendMail():
    message = MIMEText(content,'plain','utf-8')
    message['From'] = formatAddr('老公<%s>'%sender)
    message['To'] = formatAddr('亲爱的<%s>'%receivers)
    subject = "每日请安"
    message['subject'] = Header(subject,MAIL_ENCODING).encode()
    print(content)

    try:
        s = smtplib.SMTP_SSL(mail_host)
        s.login(sender,password)
        s.sendmail(sender,[receivers],message.as_string())
        s.quit()

        print("发送成功")

    except smtplib.SMTPException as e:
        print("error: %s"%e)



if __name__ =="__main__":
    sendMail()



