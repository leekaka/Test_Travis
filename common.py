# !/usr/bin/env python
# coding = utf-8

"""
存放通用函数和变量
"""

import os
import datetime


MAIL_ENCODING = "utf-8"
mail_host = "smtp.163.com"
CITY = "北京"
sender = os.environ.get("MAIL_SEND")
password = os.environ.get("PASSWORD")
receivers = os.environ.get("MAIL_RECE")

GET_MARRIED = (2017,11,6)


def get_married_days():
    """
    计算天数
    """
    today = datetime.datetime.today()
    anniversary = datetime.datetime(*GET_MARRIED)
    return (today - anniversary).days


if __name__ == "__main__":
    print(get_married_days())




