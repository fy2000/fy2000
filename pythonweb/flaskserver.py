# -*- coding: utf-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from flask import Flask, request, render_template
from utility import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/login/', methods=['POST'])
def login():
    uname = request.form['username']
    pwd = request.form['password']
    userinfo = get_user_info(uname)  # [(username, userpassword)]

    if not userinfo:
        return render_template('index.html', errorinfo='username non-existent!')

    elif uname == userinfo[0][0] and pwd == userinfo[0][1]:
        return render_template('statall.html')

    else:
        return render_template('index.html', errorinfo='password wrong!')


@app.route('/stat/<stattype>/', methods=['GET'])
def stattype(stattype: str):
    # 根据统计的内容执行不同的操作：
    if stattype == 'monthstat':
        monthinfo = get_month_info()
        return render_template('statall.html', showname="按月份统计", infolist=monthinfo)

    if stattype == 'cusstat':
        # cusinfo = get_cus_info()
        return render_template('statall.html', showname="按客户统计", infolist=0)

    if stattype == 'selesstat':
        # cusinfo = get_cus_info()
        return render_template('statall.html', showname="按客户统计", infolist=0)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
