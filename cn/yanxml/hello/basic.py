#coding=UTF-8
from __future__ import print_function
import sys
from sys import  argv,path

##coding=GBK

#Keywords
import keyword
print (keyword.kwlist)

# ocalhost:python-train Sean$ python3
# Python 3.6.2 (default, Jul 17 2017, 16:44:47)
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import keyword
# >>> keyword.kwlist
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


#Annonation style

#!/usr/bin/python3

# 第一个注释
print("hello,python3!") # 第二个注释


#  Line & indent 行与缩进
if True:
    print ("True")
else:
    print ("False")
# ERROR
# print ("123")
#File "/Users/Sean/Documents/Gitrep/python-train/cn/yanxml/hello/basic.py", line 29
#print ("123")
#^
#IndentationError: unindent does not match any outer indentation level


# Code in more than one line 多行语句
a="Hello,"
b="my "
c="friend ."
total = a + \
        b + \
        c
print (total)


total = ['hello','my',
         'frined']

# Data Type 数据类型
# Number: 1 / Long: 111111111111111 / Float: 1.2f 3E-2 /Complex: 1 + 2j 1.1+2.2j

#charater string
# Escape code '\'
# Not escape r"\n" R"\n"
# Unicode u "this is an unicode string."
word = '字符串'
sentence = "这是一个句子"
paragraph="""
这是一个段落,
可以由多行组成。
"""

# Blank Line

#Wait the input by the user
#!/usr/bin/python3
#input("\n\n按下Enter键退出程序.")


#More code in one line.
#!/usr/bin/python3

import  sys; x='runoob';sys.stdout.write(x + "\n");


#More code consist one code group

# if expression:
#     suite
# else expression:
#     suite
# else:
#     suite

#!/usr/bin/python3

x="a"
y="b"
#换行输出
print (x)
print (y)

print ("---------")

#python2 & python3
# File "try.py", line 3 print(x, end = " ") ^ SyntaxError: invalid syntax 用的版本为python2.5
# 可以用__future__模块
# from __future__ import print_function
# 这样就可以在2.X中使用3.X中的print函数了
# print默认输出语句后换行，此处被修改为" "
# 和print x, ''是不一样的

#不换行输出
print (x,y,)
print(x, end="")
print(y, end="")
print(y, end="")

print()

# import somemodule
# from somemodule import somefunction
# from somemodule import firstfunc , secondfunc , thirdfunc
# from somemodule import *

#import sys
print ("---Python import code.----")
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ("\n python路径为: ",sys.path)

#
print ("========python from import========")
print ('path:',path) # 因为已经导入sys 所以不需要再导入sys.path

# Parameter in command line
# $ python -h
# usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
# Options and arguments (and corresponding environment variables):
# -c cmd : program passed in as string (terminates option list)
# -d     : debug output from parser (also PYTHONDEBUG=x)
# -E     : ignore environment variables (such as PYTHONPATH)
# -h     : print this help message and exit
#
# [ etc. ]