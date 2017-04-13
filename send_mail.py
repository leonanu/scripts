#!/usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText


SMTP_SERVER = ''
SMTP_PORT = 
SMTP_SSL = True
USERNAME = ''
PASSWORD = ''
SENDTO = 'user1@foo.com','user2@foo.com'


def send_mail(subject, content):
    msg = MIMEText(unicode(content).encode('utf-8'), _subtype='plain',_charset='utf-8')
    msg['Subject'] = unicode(subject)
    msg['From'] = USERNAME
    msg['To']   = ','.join(SENDTO)
    msg["Accept-Charset"] = 'ISO-8859-1,utf-8'

    retry = 3
    while retry > 0:
        try:
            if SMTP_SSL:
                s = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
            else:
                s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            s.login(USERNAME, PASSWORD)
            s.sendmail(USERNAME, SENDTO, msg.as_string())
            s.quit()

            break

        except smtplib.SMTPException,e:
            retry -= 1
            if retry > 0:
                time.sleep(10)
