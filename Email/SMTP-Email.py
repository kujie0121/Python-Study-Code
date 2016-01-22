#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.utils import parseaddr, formataddr

import smtplib

#格式化邮件地址
def _format_addr(s):
    #email.utils.parseaddr()解析字符串中的email地址
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#输入Email地址和口令：
from_addr = input('From: ')
password = input('Password: ')
#输入收件人地址：
to_addr = input('To: ')
#输入SMTP服务器地址：
smtp_server = input('SMTP server: ')

#不带附件直接发送MIMEText正文：
#msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')   #plain表示纯文本邮件，html表示HTML邮件
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')

#带附件形式，创建邮件对象：
# msg = MIMEMultipart()
#发送HTML的同时再附加一个纯文本，如果收件人无法查看HTML格式的邮件，可以自动降级查看纯文本邮件。利用MIMEMultipart组合一个HTML和Plain，要注意指定subtype是alternative：
msg = MIMEMultipart('alternative')
#邮件正文是MIMEText：
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
#在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入到正文中。如果有多个图片，依次编号，然后引用不同的cid:x即可。
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

#添加附件就是加上一个MIMEBase，从本地读取一个图片：
with open('Qiuzhu.jpg', 'rb') as f:
    #设置附件的MIME和文件名，这里是jpg类型：
    mime = MIMEBase('image', 'jpeg', filename='Qiuzhu.jpg')
    #加上必要的头信息：
    mime.add_header('Content-Disposition', 'attachment', filename='Qiuzhu.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    #把附件的内容读进来：
    mime.set_payload(f.read())
    #用Base64编码：
    encoders.encode_base64(mime)
    #添加到MIMEMultipart:
    msg.attach(mime)


msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候....', 'utf-8').encode()



#标准SMTP协议默认端口是25
server = smtplib.SMTP(smtp_server, 25)

#加密SMTP：创建SMTP对象(须知道SMTP端口)后立刻调用starttls()方法，创建安全连接，其它一样。
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# server = smtplib.SMTP(smtp_server, smtp_port)
# server.starttls()

server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()



