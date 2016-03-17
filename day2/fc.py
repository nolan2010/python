#!/usr/bin/env python
#coding=utf-8
#必备参数--必须以正确的顺序传入函数，调用时的数量必须和声明一样
#命名参数--以参数的命名(str = 'Nolan')方式传入函数，可以跳过不传的参数or乱序传入
#缺省参数--函数的默认值，定义时def fname (arg1,arg2=default) 
#不定长参数--增加一个函数来处理比当初声明时更多的参数,定义时在变量前添加*号
"""
命名参数的例子
"""
#def printinfo(name,age):
#    "打印任何传入的参数"
#    print "Name:", name
#    print "Age", age
#    return
#printinfo (age = 26, name= "Nolan")
#

"""
缺省参数的例子
"""
#def printinfo(name, age = 26):
#    "打印任何传入的字符串"
#    print "Name:", name
#    print "Age", age
#    return
#printinfo (age = 26, name= "Jona")
#printinfo (name = "Nolan")
#    

"""
不定长参数的的例子
"""
#def printinfo( arg1, *vartuple):
#    "打印任何传入的参数"
#    print "输出："
#    print arg1
#    for var in vartuple:
#        print var
#    return    
#printinfo(10)
#printinfo(10,20,30)
#

