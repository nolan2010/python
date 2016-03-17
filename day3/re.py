#!/usr/bin/env python
#coding=utf-8
"""
regular expression  
python的正则表达式
"""
import re

"""
>>> import re
>>> p = re.compile('hello')
>>> str_a = 'hello, my name is Nolan'
>>> p.match(str_a)
<_sre.SRE_Match object at 0x1085f19f0>
>>> m=p.match(str_a) #match仅匹配开头的字符串，常用search()替换
>>> m.group()
'hello'
"""

