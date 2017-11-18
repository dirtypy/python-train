#!/usr/bin/python3
#unicode=utf-8

import  sys
list = [1,2,3,4,]
it = iter(list)
while next(it,None):
    print(next(it,None))

it2 = iter(list)

while True:
    try :
        print(next(it2))
    except StopIteration:
        sys.exit()

# hasnext-in-python-iterators
#  https://stackoverflow.com/questions/1966591/hasnext-in-python-iterators

# python内没有hasNext()方法

