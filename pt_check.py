#!/usr/local/python2.7/bin/python
# -*- coding:utf-8 -*-

import re
import time
import urllib
import urllib2
import smtplib
from email.mime.text import MIMEText


PT_SITES = {'CHDBits':'chdbits.co',
            'HDSky':'hdsky.me',
           }


def req_make(pt_sites):
    for site in pt_sites:
        host = pt_sites[site]
        url = 'https://' + host + '/signup.php'

        headers = {'referer':'https://' + host + '/login.php',
                   'host':host,
                   'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

        reg_check(site, url, headers)


def reg_check(site, url, headers):
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
                time.sleep(1)

            match = ['Error!',]

    if len(match) == 0:
        send_mail(site, url)


def send_mail(site, url):
    username = ''
    authcode = ''
    recipients = ['',]

    subject = site.encode('utf-8')  + u' 可能已开放注册！'
    content = url.encode('utf-8')

    msg = MIMEText(unicode(content).encode('utf-8'), _subtype='plain',_charset='utf-8')
    msg['Subject'] = unicode(subject)
    msg['From'] = username
    msg['To']   = ','.join(recipients)
    msg["Accept-Charset"] = 'ISO-8859-1,utf-8'

    retry = 3
    while retry > 0:
        try:
            s = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
            s.login(username, authcode)
            s.sendmail(username, recipients, msg.as_string())
            s.quit()

            break

        except smtplib.SMTPException,e:
            retry -= 1
            if retry > 0:
                time.sleep(10)


def main():
    req_make(PT_SITES)


if __name__ == '__main__':
    main()
