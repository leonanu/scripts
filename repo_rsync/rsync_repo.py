#!/usr/local/python2.7/bin/python
# -*- coding:utf-8 -*-

import os
import re
import time
import commands


# The status log file path and name.
STATUS_LOG = '/repo/Status.html'

# Repo Site
REPO_SITE = 'rsync://mirrors.tuna.tsinghua.edu.cn'

### Repo information.
REPO_LIST = [ { 'repo_name':'CentOS6',
                'repo_url':REPO_SITE + '/centos/6/',
                'repo_dir':'/repo/centos/6/',
                'exclude_list':'/usr/local/bin/exclude_centos6.list', },

              { 'repo_name':'CentOS7',
                'repo_url':REPO_SITE + '/centos/7/',
                'repo_dir':'/repo/centos/7/',
                'exclude_list':'/usr/local/bin/exclude_centos7.list', },

              { 'repo_name':'EPEL6',
                'repo_url':REPO_SITE + '/epel/6/x86_64/',
                'repo_dir':'/repo/epel/6/x86_64/',
                'exclude_list':'/usr/local/bin/exclude_epel6.list', },

              { 'repo_name':'EPEL7',
                'repo_url':REPO_SITE + '/epel/7/x86_64/',
                'repo_dir':'/repo/epel/7/x86_64/',
                'exclude_list':'/usr/local/bin/exclude_epel7.list', },

              { 'repo_name':'SaltStack6',
                'repo_url':REPO_SITE + '/saltstack/yum/redhat/6/x86_64/latest/',
                'repo_dir':'/repo/saltstack/yum/redhat/6/x86_64/latest/',
                'exclude_list':'/usr/local/bin/exclude_salt-latest6.list', },

              { 'repo_name':'SaltStack7',
                'repo_url':REPO_SITE + '/saltstack/yum/redhat/7/x86_64/latest/',
                'repo_dir':'/repo/saltstack/yum/redhat/7/x86_64/latest/',
                'exclude_list':'/usr/local/bin/exclude_salt-latest7.list', }, ]


def status_log(repo_name, repo_url, status):
    now_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    if status == 0:
        status = '<strong><font color="green">OK!</font></strong>'
    else:
        status = '<strong><font color="red">FAILED!</font></strong>'

    try:
        fd = open(STATUS_LOG, 'a')

    except Exception as e:
        print e

    title = '<p><strong>' + repo_name + ' Rsync Status</strong>\n'
    dtime = '<br>Last Sync: ' + now_date + '\n'
    status = '<br>Sync Status: ' + status + '\n<p>'

    if re.match(r'^rsync://', repo_url):
        repo_url = re.sub(r'^rsync://', 'http://', repo_url)

    repo_url = '<br>Repo URL: <a href="' + repo_url + '" target="_blank">' + repo_url + '</a>\n'

    fd.write(title)
    fd.write(repo_url)
    fd.write(dtime)
    fd.write(status)

    fd.close()


def sync_repo(repo_info):
    # Max rsync retry times.
    RSYNC_TRY_TIMES = 3

    # The wait time between retry.
    RSYNC_RETRY_WAIT = 10

    repo_name = repo_info['repo_name']
    repo_url = repo_info['repo_url']
    repo_dir = repo_info['repo_dir']
    exclude_list = repo_info['exclude_list']

    sync_cmd = '/usr/bin/rsync -avrt --timeout=300 --contimeout=300\
                --delete --delete-excluded --progress ' +\
                repo_url + ' --exclude-from=' + exclude_list + ' ' + repo_dir

    status = 1
    while RSYNC_TRY_TIMES > 0 and status != 0:
        (status, output) = commands.getstatusoutput(sync_cmd)
        # Debug - output
        #print output
        if status == 0:
            break

        RSYNC_TRY_TIMES -= 1
        time.sleep(RSYNC_RETRY_WAIT) 

    chmod_cmd = '/usr/bin/chown -R www:www ' + repo_dir
    os.system(chmod_cmd)

    status_log(repo_name, repo_url, status)


def main():
    if os.path.isfile(STATUS_LOG):
        os.remove(STATUS_LOG)

    for repo in REPO_LIST:
        sync_repo(repo)


if __name__ == '__main__':
    main()
