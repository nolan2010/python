#!/usr/bin/env python
#coding=utf-8
a = raw_input("请输入\033[31;1m一个字母\033[0m：")
#if  str.isalpha(a):
#    print "大写格式为：", a.upper() 
#else:
#    print "请输入一个字母"
#

while True:
    if str.isalpha(a):
        print "CAPS is " ,a.upper()
        break
    
#*****************
input_char = raw_input('Please enter \033[31;1m a alapha\033[0m:')

output_char = chr(ord(input_char) - (ord('a')-ord('A')))

print output_char
