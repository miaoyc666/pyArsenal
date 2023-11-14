#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
File name    : send_email.py
Author       : miaoyc
Create Date  : 2023/11/14 16:39
Update Date  : 2023/11/14 16:39
Description  : 发送电子邮件
"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import COMMASPACE, formatdate
from email import Encoders


def send_mail(mail_to, mail_from, subject, html, files=[], image_paths=[], server="localhost"):
    assert type(mail_to) == list

    msg = MIMEMultipart()
    msg['From'] = mail_from
    msg['To'] = COMMASPACE.join(mail_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    # 如果 text 是html，则需要设置 _subtype='html'
    # 默认情况下 _subtype='plain'，即纯文本, 开启html模式依旧可以发送文本信息，故此处设置为html类型
    msg.attach(MIMEText(html, _subtype='html', _charset='utf-8'))

    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(f, "rb").read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)

    for index, image in enumerate(image_paths):
        fp = open(image, 'rb')
        images = MIMEImage(fp.read())
        fp.close()
        images.add_header('Content-ID', '<image{0}>'.format(index))
        msg.attach(images)

    smtp = smtplib.SMTP(server)
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.close()
