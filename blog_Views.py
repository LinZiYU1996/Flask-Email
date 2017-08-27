#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/24 21:36
# @File    : Views.py
from __future__ import unicode_literals
from  flask import render_template,Blueprint,redirect,url_for,flash,request,current_app
from Main import login_manger
from Forms import Login_Form,Register_Form,PostForm
from Model import  User,Post,Permission
from flask_login import LoginManager,login_user,UserMixin,logout_user,login_required,current_user
from emails import send_email

"""
主页路由
"""



blog = Blueprint('blog', __name__)

@blog.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)

@blog.route('/index',methods=['GET','POST'])
def index():
    from Main import db
    form=PostForm()

    if form.validate_on_submit():
        if current_user.is_authenticated:
            post=Post(body=form.body.data,author=current_user._get_current_object())
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('.index'))
        else:
            flash('请先登录')
            return redirect(url_for('.index'))
    query = Post.query
    page = request.args.get('page', 1, type=int)
    posts=Post.query.order_by(Post.timestamp.desc()).all()      #分页处理
    pagination = query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=6,
        error_out=False)
    posts = pagination.items
    return render_template('index.html',form=form,posts=posts,pagination=pagination)


@blog.route('/user/<name>')
def user(name):
    user=User.query.filter_by(name=name).first()
    page=request.args.get('page',1,type=int)
    pagination=user.posts.order_by(Post.timestamp.desc()).paginate(
       page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False
    )

    posts=pagination.items

    return render_template('user.html',user=user,posts=posts,
                           pagination=pagination)



