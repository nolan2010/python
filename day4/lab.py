#!/usr/bin/env python
#coding=utf-8
a = raw_input("请输入\033[31;1m一个\033[0m字符或数字:")
b = ord(a)
c = hex(b)
print "16进制值为:", c 
