#!/usr/bin/python3

#unicode=utf-8

dist = {'Alice':'2341','Beth':'9120','Celi':'3258'}

dist1 = {'abc':456}
dist2 = {'abc':123,98.6:37}

print(dist['Alice'])

print(dist)

dist['Alice']=789

print(dist['Alice'])

# delete dictionary
del dist['Alice']

print(dist)

dist.clear()

print(dist)

del dist

# NameError: name 'dist' is not defined
# print(dist)


# 字典键的特性
#
# 字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
#
# 两个重要的点需要记住：
#
# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
# 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：

# 字典内置函数&方法
#
# Python字典包含了以下内置函数：
# 序号	函数及描述	实例
# 1	len(dict)
# 计算字典元素个数，即键的总数。
#
# >>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# >>> len(dict)
# 3
#
# 2	str(dict)
# 输出字典，以可打印的字符串表示。
#
# >>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# >>> str(dict)
# "{'Name': 'Runoob', 'Class': 'First', 'Age': 7}"
#
# 3	type(variable)
# 返回输入的变量类型，如果变量是字典就返回字典类型。
#
# >>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# >>> type(dict)
# <class 'dict'>


# Python字典包含了以下内置方法：
# 序号	函数及描述
# 1	radiansdict.clear()
# 删除字典内所有元素
# 2	radiansdict.copy()
# 返回一个字典的浅复制
# 3	radiansdict.fromkeys()
# 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
# 4	radiansdict.get(key, default=None)
# 返回指定键的值，如果值不在字典中返回default值
# 5	key in dict
# 如果键在字典dict里返回true，否则返回false
# 6	radiansdict.items()
# 以列表返回可遍历的(键, 值) 元组数组
# 7	radiansdict.keys()
# 以列表返回一个字典所有的键
# 8	radiansdict.setdefault(key, default=None)
# 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
# 9	radiansdict.update(dict2)
# Update ??? 重复的覆盖 没有的插入
# 把字典dict2的键/值对更新到dict里
# 10	radiansdict.values()
# 以列表返回字典中的所有值
# 11	pop(key[,default])
# 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
# 12	popitem()
# 随机返回并删除字典中的一对键和值(一般删除末尾对)。



# 缺少 Set的实例