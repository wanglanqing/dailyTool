# -*- coding: utf-8 -*-
from flask import Flask,render_template
from flask import request
from flask import current_app
from flask import Blueprint
from flask_paginate import Pagination ,get_page_parameter

mod = Blueprint('users',__name__)

@mod.route('/')
def index():
    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get(get_page_parameter(),type=int, default=1)
    # users = User.find(...)
    pagination = Pagination(page=page, total=3,search=search,record_name='wlq')

    return render_template('users/index.html',pagination=pagination)

#初始化
app = Flask(__name__)


#路由和视图函数，有映射关系，
@app.route('/<any(a,b):page_name>/')
def hello_world(page_name):
    user_agent = request.data
    # # a = request.headers.im_func
    # app_ctx = app.app_context()
    # app_ctx.push()
    return '<p> your browser is what {} </p>'.format(user_agent)
        # .format(user_agent, current_app.name)

@app.route('/user1/<int(3):pagess_name>/')
def user1(pagess_name):
    return render_template('user.html',name=pagess_name)
    # return 'hi user1'

@app.route('/class/<float(2):gogo>/')
def class_go(gogo):
    return '<p>zadine</p>'

@app.errorhandler(404)
def e404(e):
    return '<h1>sorry, {}</h1>'.format(e)


if __name__ == '__main__':
    app.run(debug=True)
    app_ctx = app.app_context()
    app_ctx.push()
    print current_app.name
    app_ctx.pop()
    print app.url_map
