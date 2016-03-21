try:
    name = ['a','b','c']
    name[3]
    info_dic = {}
    info_dic['alex']
except IndexError:
    print "Your list is out of range"
except KeyError:
    print " No valid key"
