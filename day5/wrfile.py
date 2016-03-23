#!/usr/bin/env python
spath = "/Users/Nolan/python/nday5/d.py" 
f=open(spath,"w")#open or create a file for writing
f.write("the block ip is \n")
f.writelines("First line 2")

f.close()
f=open(spath,"r")#opens file for reading

for line in f :
    print line
