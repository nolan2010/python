#!/usr/bin/env python
#coding=utf-8
a = raw_input("请输入一个字符：")
if str.isalpha(a):
    print "大写格式为：", a.upper() 
else:
    print "请输入一个字母"
