#coding=utf-8
import time


#def sayhi():
#    start = time.time()
#    print 'hi'
#    end = time.time()
#    print 'This function costs:', end - start
#
#sayhi()



def time_counter(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print 'This costs:', end - start
    return wrapper

@time_counter #等于 tellyoursalary = time_counter
def tellyoursalary():
    print'Nolan makes 15K per month'
tellyoursalary()

@time_counter
def sayhi():
    print 'hello'
sayhi()
