#!/usr/bin/python3
#uncoding=utf-8

#there are some operatio type to be introducted as follow:
#

# 算术运算符 arithmetic operator
# 比较运算符号 compare operator
# 赋值运算符 assignment operator
# 逻辑运算符 logic operator
# 位运算符 bit operator
# 成员运算符 member operator
# 身份运算符 identify operator
# 运算符优先级 priviledge of operator


# arithetic operator

# six operation: + - * / // % **

# compare operator

# six operation: == != >= <= > <

# assignment operator

# eight opration: = += -= *= /= //= %= **=

#logic operator

# three operation: and or not

a=1
b=2
if(a and b):
    print ("abc")

if( a or b):
    print ("Yehhl")

if(not a):
    print("saab")

# bit operator

# six operation : & | ^  ~ << >>

a = 0x00111100
b = 0x00001101

#a&b = 0x00001100
#a|b = 0x00111101
#a^b = 0x00110001 # 异或运算非常有用 同0 为0 同1 为1 不同为1 可以获取两个集合的独有数据
#~a  = 0x11000011

# member operation

# two operation: in / not in

a = 10
b = 20

list = [1,2,3,4,5,10]

if(a in list):
    print("a in list")

if(b not in list):
    print("b not in list")


#identify operation
# two operation : is/ is not

a=b=10
c=10
if( a is b):
    print("a is b")

if( id(a) == id(b)):
    print(" id(a)==id(b)")

if( a is not c):
    print(" a is not c")
else:
    print(" a is c")

if( id(a) != id(c)):
    print(" id(a) != id(c)")

# 注： id() 函数用于获取对象内存地址。
# 注: 常量字符串基本上都是使用的公共的常量池



    # is 与 == 区别：
    #
    # is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
    # >>>a = [1, 2, 3]
    # >>> b = a
    # >>> b is a
    # True
    # >>> b == a
    # True
    # >>> b = a[:]
    # >>> b is a
    # False
    # >>> b == a
    # True


# operation previlidge
# python3 逻辑运算符优先级

# 指数： **
# 正 负号/取反 ＋ － ～
# 乘除取余整除 / // % *
# 加减 + -
# 左右 移动 << >>
# 位运算符 & ^ |
# 比较运算符 > >= < <=
# 等于运算符 == !=
# 赋值运算符 = -= += *= /= //= %=
# 身份运算符 is not is
# 成员运算符 in / not in
# 逻辑运算符 and or

a = 20
b = 15
c = 10
d = 5
e = 0
e= (a+b)*c/d

