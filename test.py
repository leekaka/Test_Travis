import os
from common import *
import smtplib


print(sender)

try:
    s = smtplib.SMTP(mail_host,"25")
    s.login(sender,password)
    print("ok")
    s.quit()
except:
    print("error")

