#coding=UTF-8

#!/usr/bin/python3

counter = 100   #整型
miles = 1000.0  #浮点数类型
name = "runoob" #字符串类型

print (counter)
print (miles)
print (name)

# more data assignment
a = b = c = 1
a, b, c = 1,2,"runoob"

# six standard data type
# Number(数字) String (字符串) List(列表) Tuple(元祖) Sets(集合) Dictionary(字典)

# Number (数字)
# int float bool complex
a,b,c,d = 20,5.5,True,4+3j
print (type(a),type(b),type(c),type(d))


a=1111
isinstance(a,int)

# class A:
#     pass
# class B(A):
#     pass

# isinstance(A(),A)
# type(A()== A)
# isinstance(B(),A)
# type(B()==A)

var1 = 1
var2 = 10
# del method to delete some object reference
# del var1[,var2[var3[...,varN]]]
# del var1
del var1 , var2

# basic arithmetic
# 5+4 加法 整数 9
# 4.3-2 减法 浮点数 2.3
# 3*7 乘法 整数 21
# 2/4 整除 浮点数 0.5
# 2//4 整除 0
# 17 % 3 取余 2
# 2**5 乘方 32

# int	float	complex
# 10	0.0	3.14j
# 100	15.20	45.j
# -786	-21.9	9.322e-36j
# 080	32.3+e18	.876j
# -0490	-90.	-.6545+0J
# -0x260	-32.54e100	3e+26J
# 0x69	70.2-E12	4.53e-7j


#Basic Type : String (字符串)
# 变量[头下标:尾下标]

#!/usr/bin/python3

str="csdn.yanxml.cn"
print (str)# 输出字符串
print (str[0:-1])# 输出第一个到倒数第二个的所有字符
print (str[0])# 输出字符串第一个字符
print (str[2:5])# 输出从第三个开始到第五个的字符
print (str[2:])# 输出从第三个开始的后的所有字符
print (str * 2) # 输出字符串两次
print (str + "TEST") # 连接字符串
print("csdn.\nyanxml.cn")
print(r"csdn.\nyanxml.cn")
print(R"csdn.\nyanxml.cn")

word='Python'
print (word[0],word[5])
print (word[-1],word[-6])

# 与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。
#
# 注意：
#
# 1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
# 2、字符串可以用+运算符连接在一起，用*运算符重复。
# 3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
# 4、Python中的字符串不能改变。


#Basic Data Type : List(列表)

# 变量[头下标:尾下标]
list = ['abcd',786,2.23,'yanxml',70.2]
tinylist=[123,'yanxml']
print ("LIST DATA PRINT:========================")
print (list)# 输出完整列表
print (list[0]) # 输出列表第一个元素
print (list[1:3])# 从第二个开始输出到第三个元素
print (list[2:])# 输出从第三个元素开始的所有元素
print (tinylist * 2)# 输出两次列表
print (list + tinylist)# 连接列表

a=[1,2,3,4,5,6]
a[0]=9
a[2:5]=[13,14,16]
print (a)

a[2:5]=[]
print (a)

#append() pop()
# 注意：
#
# 1、List写在方括号之间，元素用逗号隔开。
# 2、和字符串一样，list可以被索引和切片。
# 3、List可以使用+操作符进行拼接。
# 4、List中的元素是可以改变的。

#Basic Data Type:Tuple(元组)

#!/usr/bin/python3
tuple=(1,2,3,4,5,6)
print ("TUPLE DATA PRINT:========================")
print (tuple[0])
print (tuple[1:5])
# tuple[0]=1# 修改元组元素的操作是非法的
# TypeError: 'tuple' object does not support item assignment
# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
tuple1=()# 空元组
tuple2=(20,)# 一个元素，需要在元素后添加逗号

# string、list和tuple都属于sequence（序列）。
#
# 注意：
#
# 1、与字符串一样，元组的元素不能修改。
# 2、元组也可以被索引和切片，方法一样。
# 3、注意构造包含0或1个元素的元组的特殊语法规则。
# 4、元组也可以使用+操作符进行拼接。

#Basic Data Type:Set(集合)
#parame = {value01,value02,...} 或者 set(value)

# 集合（set）是一个无序不重复元素的序列。
#!/usr/bin/python3

print ("Set DATA PRINT:========================")

student = {'Tom','Jim','Mary','Tom','Jack','Rose'}
print (student) # 输出集合，重复的元素被自动去掉
#成员测试

if('Rose' in student):
    print ('Rose 在集合中')
else:
    print ('Rose 不在集合中')

# set 可以进行集合运算
a=set('abracadabra')
b=set('alacazam')

print (a)
print (b)

print (a - b) #差集
print (a | b) #并集
print (a & b) #交集
print (a ^ b) #a b 不同时存在的元素 (与或 / 异或)


#Basic Data Type:Dictionary(字典类)

# 字典（dictionary）是Python中另一个非常有用的内置数据类型。

# 列表是有序的对象结合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#
# 字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。
#
# 键(key)必须使用不可变类型。
#
# 在同一个字典中，键(key)必须是唯一的。

#!/usr/bin/python3
dist={}
dist['one'] = "1-教程"
dist[2] = "2-工具"

tinydist = {'name':'yanxml' ,'code':1,'site':'www.yanxml.cn'}
print (dist['one'])# 输出键为 'one' 的值
print (dist[2])  # 输出键为 2 的值
print (tinydist)# 输出完整的字典
print (tinydist.keys())# 输出所有键
print (tinydist.values())# 输出所有值

dist([('yanxml',1),('Google',2),('Tamboo',3)])

x=2
{x: x**2 for x in (2,4,6)}

dist(yanxml=1,google=2,taobao=3)


# 另外，字典类型也有一些内置的函数，例如clear()、keys()、values()等。
#
# 注意：
#
# 1、字典是一种映射类型，它的元素是键值对。
# 2、字典的关键字必须为不可变类型，且不能重复。
# 3、创建空字典使用 { }。


# Python数据类型转换
#
# 有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
#
# 以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
# 函数	描述
#
# int(x [,base]) 将x转换为一个整数
# float(x) 将x转换到一个浮点数
# complex(real [,imag]) 创建一个复数
# str(x) 将对象 x 转换为字符串
# repr(x) 将对象 x 转换为表达式字符串
# eval(str) 用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s) 将序列 s 转换为一个元组
# list(s) 将序列 s 转换为一个列表
# set(s) 转换为可变集合
# dict(d) 创建一个字典。d 必须是一个序列 (key,value)元组。
# frozenset(s) 转换为不可变集合
# chr(x) 将一个整数转换为一个字符
# unichr(x) 将一个整数转换为Unicode字符
# ord(x) 将一个字符转换为它的整数值
# hex(x) 将一个整数转换为一个十六进制字符串
# oct(x) 将一个整数转换为一个八进制字符串