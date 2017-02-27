#!/bin/bash

### CentOS 6
/usr/bin/rsync -avrt --timeout=300 --contimeout=300 --delete --delete-excluded --progress \
rsync://rsync.mirrors.ustc.edu.cn/centos/6/ --exclude-from=/usr/local/bin/exclude_centos6.list /repo/centos/6/

if [ $? -eq 0 ];then
    RES='OK!'
else
    RES='FAILED!'
fi

FIN_TIME=`date +'%Y-%m-%d %H:%M:%S'`

echo "<p>CentOS 6 Repo Sync" > /repo/centos6_status.html
echo "<p>Finish Time: ${FIN_TIME}" >> /repo/centos6_status.html
echo "<p>Finish Status: ${RES}" >> /repo/centos6_status.html


### CentOS 7
/usr/bin/rsync -avrt --timeout=300 --contimeout=300 --delete --delete-excluded --progress \
rsync://rsync.mirrors.ustc.edu.cn/centos/7/ --exclude-from=/usr/local/bin/exclude_centos7.list /repo/centos/7/

if [ $? -eq 0 ];then
    RES='OK!'
else
    RES='FAILED!'
fi

FIN_TIME=`date +'%Y-%m-%d %H:%M:%S'`

echo "<p>CentOS 7 Repo Sync" > /repo/centos7_status.html
echo "<p>Finish Time: ${FIN_TIME}" >> /repo/centos7_status.html
echo "<p>Finish Status: ${RES}" >> /repo/centos7_status.html


### EPEL 6
/usr/bin/rsync -avrt --timeout=300 --contimeout=300 --delete --delete-excluded --progress \
rsync://rsync.mirrors.ustc.edu.cn/epel/6/x86_64/ --exclude-from=/usr/local/bin/exclude_epel6.list /repo/epel/6/x86_64/

if [ $? -eq 0 ];then
    RES='OK!'
else
    RES='FAILED!'
fi

FIN_TIME=`date +'%Y-%m-%d %H:%M:%S'`

echo "<p>EPEL 6 Repo Sync" > /repo/epel6_status.html
echo "<p>Finish Time: ${FIN_TIME}" >> /repo/epel6_status.html
echo "<p>Finish Status: ${RES}" >> /repo/epel6_status.html


### EPEL 7
/usr/bin/rsync -avrt --timeout=300 --contimeout=300 --delete --delete-excluded --progress \
rsync://rsync.mirrors.ustc.edu.cn/epel/7/x86_64/ --exclude-from=/usr/local/bin/exclude_epel7.list /repo/epel/7/x86_64/

if [ $? -eq 0 ];then
    RES='OK!'
else
    RES='FAILED!'
fi

FIN_TIME=`date +'%Y-%m-%d %H:%M:%S'`

echo "<p>EPEL 7 Repo Sync" > /repo/epel7_status.html
echo "<p>Finish Time: ${FIN_TIME}" >> /repo/epel7_status.html
echo "<p>Finish Status: ${RES}" >> /repo/epel7_status.html


/usr/bin/chown -R www:www /repo
