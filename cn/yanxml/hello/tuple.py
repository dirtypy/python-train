#!/usr/bin/python3
#unicode=utf-8

# basic tuple

tup1 = ('Google','Runoob',1997,2000)
tup2 = (1,2,3,4,5)

# 竟然不写括号也能够识别
tup3 = "a","b","c","d"

print(tup1)
print(tup2)
print(tup3)

tup4=();


tup5 = (20);
# 不加逗号，类型为整型
print(type(tup5))

tup6 = (20,)
type(tup6)
# 加上逗号，类型为元组
print(type(tup6))


# visit the tuple
print(tup1[0])
print(tup2[1:4])

# Update tuple

# The tuple can not be update.
# TypeError: 'tuple' object does not support item assignment
# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tupUnion = tup1+tup2

print(tupUnion)
# 注意 元组 只能整体的删除 但是不能够单个删除元素
# TypeError: 'tuple' object doesn't support item deletion
# del tup1[0]

del tup1
print(tup1)

# 元组运算符
#
# 与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。
# Python 表达式	结果 	描述
# len((1, 2, 3))	3	计算元素个数
# (1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	连接
# ('Hi!',) * 4 	('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制
# 3 in (1, 2, 3)	True	元素是否存在
# for x in (1, 2, 3): print x,	1 2 3	迭代

# 元组索引，截取
#
# 因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素，如下所示：
#
# 元组：
#
# L = ('Google', 'Taobao', 'Runoob')
#
# Python 表达式	结果 	描述
# L[2]	'Runoob!'	读取第三个元素
# L[-2]	'Taobao'	反向读取；读取倒数第二个元素
# L[1:]	('Taobao', 'Runoob!')	截取元素，从第二个开始后的所有元素。


# 元组内置函数

# 方法 没有list那么多

# Python元组包含了以下内置函数
# 序号	方法及描述	实例
# 1	len(tuple)
# 计算元组元素个数。
#
# >>> tuple1 = ('Google', 'Runoob', 'Taobao')
# >>> len(tuple1)
# 3
# >>>
#
# 2	max(tuple)
# 返回元组中元素最大值。
#
# >>> tuple2 = ('5', '4', '8')
# >>> max(tuple2)
# '8'
# >>>
#
# 3	min(tuple)
# 返回元组中元素最小值。
#
# >>> tuple2 = ('5', '4', '8')
# >>> min(tuple2)
# '4'
# >>>
#
# 4	tuple(seq)
# 将列表转换为元组。
#
# >>> list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
# >>> tuple1=tuple(list1)
# >>> tuple1
# ('Google', 'Taobao', 'Runoob', 'Baidu')

