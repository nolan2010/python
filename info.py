#coding=utf-8
name = raw_input("请输入你的名字：").strip()
age  = int(raw_input("请告诉我你的年龄：").strip())
job  = raw_input("以及你的工作：").strip()
msg = """
你的个人信息如下：
名字：%s
年龄：%s
工作：%s
""" %(name,age,job)
print msg
if name =='nolan':
    print 'Hi, %s, how are you'%name
else:
    print 'Sorry, I do not know you!, haha'
    name = raw_input("Do you want to try another name:")
    if name =='root':
         print 'Hi,boss, it is a joke, you know I know you!'
    elif name =='nolan':
             print "Come on, %s, why don't you type in at firt time!\n How are you!" %name
    else:
         print "Sorry, I really do not know you!"
    
