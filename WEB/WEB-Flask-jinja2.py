#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Flask默认支持的模板是jinja2模板。
#Flask通过render_template()函数来实现模板的渲染。
#一定要把模板放到正确的templates目录下，templates和处理文件在同级目录下。
from flask import Flask, request, render_template

app = Flask(__name__)

#GET /：首页，返回Home：
@app.route('/', methods=['GET', 'POST'])
def home():
      return render_template('home.html')

#GET /signin：登录页，显示登录表单：
@app.route('/signin', methods=['GET'])
def signin_form():
      return render_template('form.html')

#POST /signin：处理登录表单，显示登录结果：
@app.route('/signin', methods=['POST'])
def signin():
      username = request.form['username']
      password = request.form['password']
      #需要从request对象读取表单内容：
      if username =='admin' and password == 'password':
            return render_template('signin-ok.html', username=username)
      return render_template('form.html', message='Bad username or password.', username=username)

#Flask自带的Server在端口5000上监听
if __name__ == '__main__':
      #打开调试信息
      #app.debug = True
      #或者 app.run(debug = True)
      app.run()