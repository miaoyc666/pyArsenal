#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
File name    : send_email.py
Author       : miaoyc
Create Date  : 2023/11/14 16:39
Update Date  : 2023/11/14 16:39
Description  : send email
"""

import os
import smtplib
from email import Encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def send_mail(mail_to, mail_from, subject, html, files=None, image_paths=None, server="localhost"):
    if image_paths is None:
        image_paths = []
    if files is None:
        files = []
    assert type(mail_to) == list

    msg = MIMEMultipart()
    msg['From'] = mail_from
    msg['To'] = COMMASPACE.join(mail_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    # If the text is HTML, it needs to be set_ Subtype='html 
    # By default_ Subtype='plain ', which means plain text. 
    # Even when the HTML mode is turned on, text messages can still be sent, so this is set as an HTML class
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
