#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def index():
    client_ip = request.remote_addr
    return '%s\n' % client_ip


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
