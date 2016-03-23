s = raw_input("Input your age:")
if s =="":
    raise Exception("Input must not be empty")
try:
    i=int(s)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unknown exception!"
else:#It is useful for code that must be executed if the try clause does not raise an exception
    print "You are %d" % i,"years old"
finally:#clean up action
    print "Goodbye!"

