#!/usr/bin/python3
#unicoding=utf-8

# 语法
#
# Python 定义函数使用 def 关键字，一般格式如下：
#
# def 函数名（参数列表）:
# 函数体

def hello():
    print("Hello:")

hello()

print(type(2))
def area(height,width):
    area = 0
    # if type(height) =='int'and type(width)=='int' and height > 0 and width > 0:
    if height > 0 and width > 0:
        area = height*width
    return area

# 这样的判断语法有问题
print(area(2,3))
# print(area("2",3))

# Python判断变量的数据类型的两种方法
# https://www.cnblogs.com/jessicaxu/p/7727264.html

a=2
if(type(a)==type(1)):
    print("a Type:",type(1))

b="str"
if(isinstance(b,str)):
    print("b Type:","str")


# param

paramInt = 1
paramList = [1,2,3]

def func1(number):
    return number

def func2(mylist):
    mylist.append([1,2,3])
    return mylist


print(paramList)
print(func2(paramList))

# 值传递会改变引用的类型
print(paramList)

# Number & String 为不可变参数类型
# Set Tuple List Dictionary 为可变参数类型


# 参数
# 必需参数
# 关键字参数
# 默认参数
# 不定长参数

# 必需参数

def printme(str):
    return str

printme("123")

# 关键字参数

def printInfo(age,name):
    pass

printInfo(age=18,name="Sean")

# 默认参数

def printInfo2(age,name="sean"):
    pass

printInfo2(19)

def printInfo3(age,*vartuple):
    pass

printInfo3(10)
printInfo3(10,10,20,20)

# 匿名函数

sum = lambda  arg1,agr2: arg1+agr2

print("Sum",sum(1,2))


# Effictive Scope


# L （Local） 局部作用域
# E （Enclosing） 闭包函数外的函数中
# G （Global） 全局作用域
# B （Built-in） 内建作用域
# 以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。


# x = int(2.9)  # 内建作用域
#
# g_count = 0  # 全局作用域
# def outer():
#     o_count = 1  # 闭包函数外的函数中
#     def inner():
#         i_count = 2  # 局部作用域


# global 和 nonlocal关键字
#
# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
#
#
# #!/usr/bin/python3
#
# num = 1
# def fun1():
#     global num  # 需要使用 global 关键字声明
#     print(num)
#     num = 123
#     print(num)
# fun1()
# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了，如下实例：
#
#
# #!/usr/bin/python3
#
# def outer():
#     num = 10
#     def inner():
#         nonlocal num   # nonlocal关键字声明
#         num = 100
#         print(num)
#     inner()
#     print(num)
# outer()


# python 函数的作用域是在是有点奇葩
#!/usr/bin/python3

num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)
fun1()


def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()