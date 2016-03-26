#coding=utf-8
number = 23
running = True
while running:
    guess=int(raw_input("Please enter an integer:"))
    if guess == number:
        print ("Congratulation")
        running = False
    elif guess>number:
        print("sorry, It is litter higer than that")
    else:
        print ("Sorry, It is litter lower than that")
#else:
#    print("THe while loop is over")
#print("done")
#----------------------------------------------------
print '*'*60
print "This is another loop script"
print '*'*60
for i in range(1,5):
 print i
else:#该语句块儿可选，在循环结束后执行
 print "The for loop is over"
#----------------------------------------------------
print '*'*60
print "This is another loop script"
print '*'*60
#break语句，终止for和while循环，else块将不执行
while True:
 s=raw_input("Enter something:")
 if s=="quit":
  break
 print"length of the string is:", len(s)
print "Done"
#----------------------------------------------------
print '*'*60
print "This is another loop script"
print '*'*60
#continue语句，跳过当前循环的剩余语句，继续下一轮循环
while True:
 s = raw_input("Enter somthing:")
 if s == 'quit':
    break
 if len(s) < 3:
    continue
 print "Your Input is %s" % s
#-----------------------------------------------------
