#/usr/bin/python3
#uncode=utf-8

# python 数据结构

#list

# 列表
#
# Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，一句话概括即：列表可以修改，而字符串和元组不能。
#
# 以下是 Python 中列表的方法：
# 方法 	描述
# list.append(x) 	把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
# list.extend(L) 	通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
# list.insert(i, x) 	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
# list.remove(x) 	删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
# list.pop([i]) 	从列表的指定位置删除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被删除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
# list.clear() 	移除列表中的所有项，等于del a[:]。
# list.index(x) 	返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
# list.count(x) 	返回 x 在列表中出现的次数。
# list.sort() 	对列表中的元素进行排序。
# list.reverse() 	倒排列表中的元素。
# list.copy() 	返回列表的浅复制，等于a[:]。

a = [66.25,333,333,1,234.5]

print(a.count(333),a.count(66.25),a.count('x'))

#insert 可以指定插入的位置
a.insert(-2,1)

a.append(3332)

print(a)

# 返回第一个的index
a.index(333)

a.remove(333)

# 不会全部删除
print(a)

# 反转队列
a.reverse()

# 队列排序
a.sort()


# 将列表当做堆栈使用

a = [3,4,5]

a.append(6)

a.append(7)

# 弹出 出栈
a.pop()

a.pop()

# 将列表当作队列使用

from collections import  deque


a = deque([1,2,3,4])

a.append(6)

a.append(7)

# 出队列
a.popleft()
a.popleft()


# 列表推导式
vec = [1,2]
[3*x for x in vec if x > 3]

# 不推荐使用



# 元祖
t = 12345, 54321, 'hello!'

t[0]

t
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u
# ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# 二层嵌套

matrix = [
         [1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         ]

[[row[i] for row in matrix] for i in range(4)]


transposed = []

for i in range(4):
    transposed.append(row[i] for row in matrix )


transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)


# del 语句

a = [1,2,3,4,5]
del a[0]

del a[:]

del a
# 集合
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
'orange' in basket
a = set('adadadad')
b = set('ddsaaaada')

a&b
a|b
a^b
a-b
a+b

a = {x for x in 'abracadabra' if x not in 'abc'}

# 字典

tel = {'jack': 4098, 'sape': 4139}
tel['jack'] = 9000
'guido' in tel

{x: x**2 for x in (2, 4, 6)}

#遍历技巧

knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k,v in knights.items():
    print(k,v)

# set
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)

# list
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in basket:
    print(i)

