import os
from common import *
import smtplib


print(sender)

try:
    s = smtplib.SMTP_SSL(mail_host)
    s.login(sender,password)
    print("ok")
    s.quit()
except:
    print("error")

