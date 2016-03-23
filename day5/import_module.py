#every py file can be treats as a moudle, moudles can be imported by each other 
from a import add_func#or use import a

print "Import add_func from module a"
print "Result of 1 plus 2 is:"
print add_func(1,2)# if using 'Import a', then here should be "a.add_func"
