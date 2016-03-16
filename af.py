#!/usr/bin/env python
#coding=utf-8
#lambda语句用来创建匿名函数
"""
lambda主体是一个表达式，函数体比def简单，拥有自己的名字空间，仅能在lambda表达式中封装有限的逻辑，不能访问参数列表之外或全局名字空间里的参数。
"""
#sum = lambda arg1, arg2: arg1 + arg2;

#print "相加后的值为：", sum(10,20)
#print "相加后的值为：", sum(20,20)




#retun语句[表达式]退出函数

#def sum(arg1, arg2):
#    total = arg1 + arg2
#    print "函数内：", total
#    return total
#
#total = sum(10,20)
#print "函数外：", total


##全局变量和局部变量
#total = 0 #这是一个全局变量
##函数说明
#def sum(arg1, arg2):
#    #返回2个参数的和
#    total = arg1 + arg2
#    print "函数内是局部变量：", total
#    return total
##调用sum函数
#sum(10,20)
#print "函数外是全局变量：", total
#
