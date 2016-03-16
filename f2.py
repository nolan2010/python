#!/usr/bin/env python
#coding=utf-8
#必备参数--必须以正确的顺序传入函数，调用时的数量必须和声明一样
#命名参数--调用方以参数的命名(str = 'Nolan')方式传入函数，可以跳过不传的参数or乱序传入
#缺省参数--函数的默认值，定义时def fname (arg1,arg2=default) 
#不定长参数--增加一个函数来处理比当初声明时更多的参数,定义时在变量前添加*号
#不定长参数的的例子
def printinfo( arg1, *vartuple):
    "打印任何传入的参数"
    print arg1
    for var in vartuple:
        print var
    return    
printinfo(10)
printinfo(10,20,30)
