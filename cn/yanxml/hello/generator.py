#!/usr/bin/python3
#unicode=utf-8
import  sys
# python 自己的递归调用被 可以使用yield
# yield 表示自己调用的 next()


def fibonacci(n):
    a,b,counter=0,1,0
    while True:
        # 结束标记
        if(counter > n):
            return
        yield a
        a,b = b,a+b
        counter+=1

f = fibonacci(10)

# print(f)



while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()