#!/bin/bash

PRI_KEY="/root/.ssh/code_sync"

SRC_DIR="/data/wwwroot/wx.iloveplanet.cn/"
DST_DIR="/data/wwwroot/wx.iloveplanet.cn/"

DST_SRV="172.21.0.3 172.21.0.7"

for HOST in ${DST_SRV};do
    rsync -avrz --progress --delete-after -e "ssh -i ${PRI_KEY} -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no" ${SRC_DIR} root@${HOST}:${DST_DIR}
    ssh -i ${PRI_KEY} -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no root@${HOST} "chown -R www:www ${SRC_DIR}"
done
