#!/usr/bin/env  python
#coding=utf-8
import pickle

#load data first
account_info = {
'037195535':['Nolan',12000,12000],
'037159939':['Lydia',72000,72000]
}

f = file('account.pkl','wb')
pickle.dump(account_info, f)
account_info['037159939'][0]='Alipay'
pickle.dump(account_info, f)
f.close()

"""
>>> import pickle
>>> f=open('account.pkl')
>>> acc1 = pickle.load(f)
>>> acc2 = pickle.load(f)
python 解释器读取文件
>>> f=open('account.pkl')
>>> 
>>> acc1 = pickle.load(f)
>>> acc2 = pickle.load(f)
>>> acc1
{'037159939': ['Lydia', 72000, 72000], '037195535': ['Nolan', 12000, 12000]}
>>> acc2
{'037159939': ['Alipay', 72000, 72000], '037195535': ['Nolan', 12000, 12000]}
另一种用法
>>> pickle.dumps(acc1)
"(dp0\nS'037159939'\np1\n(lp2\nS'Lydia'\np3\naI72000\naI72000\nasS'037195535'\np4\n(lp5\nS'Nolan'\np6\naI12000\naI12000\nas."
>>> a = pickle.dumps(acc1)
>>> pickle.loads(a)
{'037159939': ['Lydia', 72000, 72000], '037195535': ['Nolan', 12000, 12000]}
>>> 
"""
