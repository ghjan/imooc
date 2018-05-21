# _*_ coding: utf-8 _*_
__author__ = 'david'
__date__ = '2018/5/21 21:37'

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)