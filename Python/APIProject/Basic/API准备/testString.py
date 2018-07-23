#-*- coding: utf-8 -*-
from time import time
def plus_test():
    t = time()
    s = ''
    for i in range(10):
        s += 'test'
    print(s)
    print(time() - t)
def join_test():
    t = time()
    li = []
    for i in range(10):
        li.append('test')
    s = ''.join(li)
    print(li)
    print(time() - t)

plus_test()
join_test()