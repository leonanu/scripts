#!/bin/bash

PIP_BIN=/usr/local/python2.7/bin/pip

if [ ! -x ${PIP_BIN} ];then
    echo "${PIP_BIN}: Not exist or not executable!"
    exit 1
fi

pkgs=$(${PIP_BIN} list --format=legacy | cut -d ' ' -f 1)

for pkg in ${pkgs};
do
    ${PIP_BIN} install -U ${pkg}
done
