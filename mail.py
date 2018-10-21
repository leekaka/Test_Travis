# coding:utf-8
"""
just mail

"""

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

print __doc__


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
# 发送人地址


from_addr = 'lika27@163.com'
# 邮箱密码
password = 'garrulous0422'
# 收件人地址
to_addr = 'dilik520@126.com'

smtp_server = 'smtp.163.com'

msg = MIMEText('<html><body><h1>hello word</h1><p>异常网页<a href= "http://www.baidu.com">百度</a><p></body></html>', 'html', 'utf-8')
msg['from'] = _format_addr('Python绿色通道<%s>' % from_addr)
msg['to'] = _format_addr('Python绿色通道管理员<%s>' % to_addr)
msg['subject'] = Header('Python绿色通道爬虫运行状态', 'utf-8').encode()


# 发送邮件
server = smtplib.SMTP(smtp_server, 25)     # 负责发送邮件
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
