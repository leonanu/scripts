#!/usr/local/python2.7/bin/python
# -*- coding:utf-8 -*-

import re
import time
import urllib
import urllib2
import smtplib
from email.mime.text import MIMEText


def chdbits_check():
    host = 'https://chdbits.co'
    url = host + '/signup.php'

    headers = {'referer':'https://chdbits.co/login.php',
               'host':'chdbits.co',
               'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    retry = 3
    while retry > 0:
        try:
            req = urllib2.Request(url, headers=headers)
            con = urllib2.urlopen(req, timeout=10)
            res = con.read()

            match = re.findall(r'<h2>对不起</h2>', res)
            break

        except Exception as e:
            retry -= 1
            if retry > 0:
                time.sleep(10)

            match = ['Failed',]

    return match


def send_mail():
    username = ''
    authcode = ''
    recipients = ''

    msg = MIMEText('https://chdbits.co 可能已开放注册！')
    msg['Subject'] = 'CHDBits 可能已开放注册！'
    msg['From'] = username
    msg['To']   = recipients

    retry = 3
    while retry > 0:
        try:
            s = smtplib.SMTP_SSL('smtp.qq.com', 465)
            s.login(username, authcode)
            s.sendmail(username, recipients, msg.as_string())
            s.quit()

            break

        except smtplib.SMTPException,e:
            retry -= 1
            if retry > 0:
                time.sleep(10)


def main():
    res = chdbits_check()

    if len(res) == 0:
        send_mail()


if __name__ == '__main__':
    main()
