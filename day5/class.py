#coding=utf-8
#class dog:
#    def name(self):
#        print"Hello, my name is Python"
#a = dog()
#a.name()
#
#"""
#类的方法：self：代表类本身
#__init__初始化函数：
#析构和解构函数
#__del__释放函数
#"""
class person:#类
    def __init__(self,name,age):
        print 'I am being called right now'
        self.Name = name
        self.Age = age
    def sayhi(self):
        print'my name is %s, I am %s years old' %(self.Name, self.Age)
        self.__talk()
    #def __del__(self):
    #    print"glad to meet you",self.Name
    def __talk(self):#以两个下划线开始代表私有属性
        print 'print private var'
p = person('Nolan',26)#实例
p.sayhi()
#del p
##p.talk()#因为维私有函数，故无法在外部调用
##p._person__talk()#此为强制调用
#print "*"*60
#p2 = person('jona',26)
#p2.sayhi()
#"""
#私有函数：
#    def __talk(self):#以两个下划线开始代表私有属性
#p.talk()#因为维私有函数，故无法在外部调用
#p._person__talk()#此为强制调用
#"""
#
print '*'*60
print "This is another example"
print '*'*60
#
#class dog:
#    def name(self):#类的方法
#        print"hello, boss "
#
#D = dog()#将类实例化
#D.name()#引用dog类下面的name方法#相当于dog.name(D)
#
