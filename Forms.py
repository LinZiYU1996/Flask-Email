#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/23 18:09
# @File    : Forms.py

from __future__ import unicode_literals
from wtforms import StringField,SubmitField,PasswordField,TextAreaField,FileField
from wtforms.validators import  Required,Length
from flask_wtf import FlaskForm
from flask_pagedown.fields import  PageDownField



#登录表单
class Login_Form(FlaskForm):
    email=StringField('email',validators=[Required()])
    pwd=PasswordField('pwd',validators=[Required()])
    submit=SubmitField('Login in')


#注册表单
class Register_Form(FlaskForm):
    Email=StringField('email',validators=[Required()])


    name=StringField('name',validators=[Required()])
    pwd=PasswordField('pwd',validators=[Required()
                                        ,Length(3,10)])
    submit=SubmitField('register')

class PostForm(FlaskForm):
    body=PageDownField('What is you mind',validators=[Required()])
    submit=SubmitField('Submit')
