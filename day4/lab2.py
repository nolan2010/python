#!/usr/bin/env python
#coding=utf-8
a = raw_input("请输入\033[31;1m一个字母\033[0m：")
if  str.isalpha(a):
    print "大写格式为：", a.upper() 
else:
    print "请输入一个字母"

