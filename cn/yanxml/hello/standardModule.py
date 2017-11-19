#!/usr/bin/python3
#unicode=utf-8

#python 标准库

import os

import shutil

import glob

import sys

import  re

import  math


# import  random

# os 操作库
# dir(os)
# help(os)

os.getcwd()
# os.chdir('/server/accesslogs')
os.system('mkdir today')

# 文件操作任务

# shutil.copyfile('data.db','archive.db')
# shutil.move('/build/executables','installer')


# 文件统配符
glob.glob('*.py')

# 命令行参数
print(sys.argv)

# 错误重定向
sys.stderr.write('Warning.')


# 正则匹配库
re.findall(r'\b[a-z]*]','which foot or hand fell fastest')

# 正则替换
re.sub(r'(\b[a-z]+) \1','\1','cat in the hat')

str = 'tea for too'
str.replace('tea','too')

# 数学计算
# math.cos(math.pi/4)

# math.log(1024,2)


# 随机函数
#
# random.choice(['apple','pear','banana'])
#
# random.sample(range(100),10)
#
# random.random()
#
# random.randrange(6)# random integer chosen from range(6)

# 访问 互联网

# 有几个模块用于访问互联网以及处理网络通信协议。其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib:


# 数据压缩

import  zlib

s = b'witch which has which witches wrist watch'
print(len(s))

t= zlib.compress(s)
print(len(t))

zlib.decompress(t)

zlib.crc32(s)

# 有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣。Python 提供了一个度量工具，为这些问题提供了直接答案。


from timeit import  Timer

Timer('t=a;a=b;b=t','a=1;b=2').timeit()

Timer('a,b = b,a', 'a=1; b=2').timeit()


# 测试工具
#doctest模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。
def average(values):
    return sum(values)/len(values)

import  doctest
doctest.testmod(average(100))

# unittest模块不像 doctest模块那么容易使用，不过它可以在一个独立的文件里提供一个更全面的测试集:
#
# import unittest
#
# class TestStatisticalFunctions(unittest.TestCase):
#
#     def test_average(self):
#         self.assertEqual(average([20, 30, 70]), 40.0)
#         self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
#         self.assertRaises(ZeroDivisionError, average, [])
#         self.assertRaises(TypeError, average, 20, 30, 70)
#
# unittest.main() # Calling from the command line invokes all tests

# 时间函数
from datetime import  date
now=date.today()
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

birthday = date(1964,7,31)
age = now-birthday
age.days


# 访问互联网

# 访问 互联网
#
# 有几个模块用于访问互联网以及处理网络通信协议。其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib:
#
# >>> from urllib.request import urlopen
# >>> for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
#     ...     line = line.decode('utf-8')  # Decoding the binary data to text.
# ...     if 'EST' in line or 'EDT' in line:  # look for Eastern Time
#     ...         print(line)
#
# <BR>Nov. 25, 09:43:32 PM EST
#
# >>> import smtplib
# >>> server = smtplib.SMTP('localhost')
# >>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
#                     ... """To: jcaesar@example.org
# ... From: soothsayer@example.org
# ...
# ... Beware the Ides of March.
# ... """)
# >>> server.quit()