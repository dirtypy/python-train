#!/usr/bin/python
#unicode=utf-8

# import  cn.yanxml.hello.package.hello as hello
# hello.helloMethod()


from  cn.yanxml.hello.package.hello import helloMethod

helloMethod()



# _name__属性
#
# 一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
#
# #!/usr/bin/python3
# # Filename: using_name.py
#
# if __name__ == '__main__':
#     print('程序自身在运行')
# else:
#     print('我来自另一模块')
#
# 运行输出如下：
#
# $ python using_name.py
# 程序自身在运行
#
# $ python
# >>> import using_name
# 我来自另一模块
# >>>
#
# 说明： 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
# dir() 函数
#
# 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
# </p>
# <pre>
# >>> import fibo, sys
# >>> dir(fibo)
# ['__name__', 'fib', 'fib2']
# >>> dir(sys)
# ['__displayhook__', '__doc__', '__excepthook__', '__loader__', '__name__',
#  '__package__', '__stderr__', '__stdin__', '__stdout__',
#  '_clear_type_cache', '_current_frames', '_debugmallocstats', '_getframe',
#  '_home', '_mercurial', '_xoptions', 'abiflags', 'api_version', 'argv',
#  'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder',
#  'call_tracing', 'callstats', 'copyright', 'displayhook',
#  'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix',
#  'executable', 'exit', 'flags', 'float_info', 'float_repr_style',
#  'getcheckinterval', 'getdefaultencoding', 'getdlopenflags',
#  'getfilesystemencoding', 'getobjects', 'getprofile', 'getrecursionlimit',
#  'getrefcount', 'getsizeof', 'getswitchinterval', 'gettotalrefcount',
#  'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
#  'intern', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path',
#  'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1',
#  'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit',
#  'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout',
#  'thread_info', 'version', 'version_info', 'warnoptions']
#
# 如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称:
#
# >>> a = [1, 2, 3, 4, 5]
# >>> import fibo
# >>> fib = fibo.fib
# >>> dir() # 得到一个当前模块中定义的属性列表
# ['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
# >>> a = 5 # 建立一个新的变量 'a'
# >>> dir()
# ['__builtins__', '__doc__', '__name__', 'a', 'sys']
# >>>
# >>> del a # 删除变量名a
# >>>
# >>> dir()
# ['__builtins__', '__doc__', '__name__', 'sys']
# >>>
#
# 标准模块
#
# Python 本身带着一些标准的模块库，在 Python 库参考文档中将会介绍到（就是后面的"库参考文档"）。
#
# 有些模块直接被构建在解析器里，这些虽然不是一些语言内置的功能，但是他却能很高效的使用，甚至是系统级调用也没问题。
#
# 这些组件会根据不同的操作系统进行不同形式的配置，比如 winreg 这个模块就只会提供给 Windows 系统。
#
# 应该注意到这有一个特别的模块 sys ，它内置在每一个 Python 解析器中。变量 sys.ps1 和 sys.ps2 定义了主提示符和副提示符所对应的字符串:
#
# >>> import sys
# >>> sys.ps1
# '>>> '
# >>> sys.ps2
# '... '
# >>> sys.ps1 = 'C> '
# C> print('Yuck!')
# Yuck!
# C>
#
# 包
#
# 包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
#
# 比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B 。
#
# 就好像使用模块的时候，你不用担心不同模块之间的全局变量相互影响一样，采用点模块名称这种形式也不用担心不同库之间的模块重名的情况。
#
# 这样不同的作者都可以提供 NumPy 模块，或者是 Python 图形库。
#
# 不妨假设你想设计一套统一处理声音文件和数据的模块（或者称之为一个"包"）。
#
# 现存很多种不同的音频文件格式（基本上都是通过后缀名区分的，例如： .wav，:file:.aiff，:file:.au，），所以你需要有一组不断增加的模块，用来在不同的格式之间转换。
#
# 并且针对这些音频数据，还有很多不同的操作（比如混音，添加回声，增加均衡器功能，创建人造立体声效果），所你还需要一组怎么也写不完的模块来处理这些操作。
#
# 这里给出了一种可能的包结构（在分层的文件系统中）:
#
# sound/                          顶层包
# __init__.py               初始化 sound 包
# formats/                  文件格式转换子包
# __init__.py
# wavread.py
# wavwrite.py
# aiffread.py
# aiffwrite.py
# auread.py
# auwrite.py
# ...
# effects/                  声音效果子包
# __init__.py
# echo.py
# surround.py
# reverse.py
# ...
# filters/                  filters 子包
# __init__.py
# equalizer.py
# vocoder.py
# karaoke.py
# ...
#
# 在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录。
#
# 目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。
#
# 最简单的情况，放一个空的 :file:__init__.py就可以了。当然这个文件中也可以包含一些初始化代码或者为（将在后面介绍的） __all__变量赋值。
#
# 用户可以每次只导入一个包里面的特定模块，比如:
#
# import sound.effects.echo
#
# 这将会导入子模块:sound.effects.echo。 他必须使用全名去访问:
#
# sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
#
# 还有一种导入子模块的方法是:
#
# from sound.effects import echo
#
# 这同样会导入子模块: echo，并且他不需要那些冗长的前缀，所以他可以这样使用:
#
# echo.echofilter(input, output, delay=0.7, atten=4)
#
# 还有一种变化就是直接导入一个函数或者变量:
#
# from sound.effects.echo import echofilter
#
# 同样的，这种方法会导入子模块: echo，并且可以直接使用他的 echofilter() 函数:
#
# echofilter(input, output, delay=0.7, atten=4)
#
# 注意当使用from package import item这种形式的时候，对应的item既可以是包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量。
#
# import语法会首先把item当作一个包定义的名称，如果没找到，再试图按照一个模块去导入。如果还没找到，恭喜，一个:exc:ImportError 异常被抛出了。
#
# 反之，如果使用形如import item.subitem.subsubitem这种导入形式，除了最后一项，都必须是包，而最后一项则可以是模块或者是包，但是不可以是类，函数或者变量的名字。
# 从一个包中导入*
#
# 设想一下，如果我们使用 from sound.effects import *会发生什么？
#
# Python 会进入文件系统，找到这个包里面所有的子模块，一个一个的把它们都导入进来。
#
# 但是很不幸，这个方法在 Windows平台上工作的就不是非常好，因为Windows是一个大小写不区分的系统。
#
# 在这类平台上，没有人敢担保一个叫做 ECHO.py 的文件导入为模块 echo 还是 Echo 甚至 ECHO。
#
# （例如，Windows 95就很讨厌的把每一个文件的首字母大写显示）而且 DOS 的 8+3 命名规则对长模块名称的处理会把问题搞得更纠结。
#
# 为了解决这个问题，只能烦劳包作者提供一个精确的包的索引了。
#
# 导入语句遵循如下规则：如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。
#
# 作为包的作者，可别忘了在更新包之后保证 __all__ 也更新了啊。你说我就不这么做，我就不使用导入*这种用法，好吧，没问题，谁让你是老板呢。这里有一个例子，在:file:sounds/effects/__init__.py中包含如下代码:
#
# __all__ = ["echo", "surround", "reverse"]
#
# 这表示当你使用from sound.effects import *这种用法时，你只会导入包里面这三个子模块。
#
# 如果 __all__ 真的没有定义，那么使用from sound.effects import *这种语法的时候，就不会导入包 sound.effects 里的任何子模块。他只是把包sound.effects和它里面定义的所有内容导入进来（可能运行__init__.py里定义的初始化代码）。
#
# 这会把 __init__.py 里面定义的所有名字导入进来。并且他不会破坏掉我们在这句话之前导入的所有明确指定的模块。看下这部分代码:
#
# import sound.effects.echo
# import sound.effects.surround
# from sound.effects import *
#
# 这个例子中，在执行from...import前，包sound.effects中的echo和surround模块都被导入到当前的命名空间中了。（当然如果定义了__all__就更没问题了）
#
# 通常我们并不主张使用*这种方法来导入模块，因为这种方法经常会导致代码的可读性降低。不过这样倒的确是可以省去不少敲键的功夫，而且一些模块都设计成了只能通过特定的方法导入。
#
# 记住，使用from Package import specific_submodule这种方法永远不会有错。事实上，这也是推荐的方法。除非是你要导入的子模块有可能和其他包的子模块重名。
#
# 如果在结构中包是一个子包（比如这个例子中对于包sound来说），而你又想导入兄弟包（同级别的包）你就得使用导入绝对的路径来导入。比如，如果模块sound.filters.vocoder 要使用包sound.effects中的模块echo，你就要写成 from sound.effects import echo。
#
# from . import echo
# from .. import formats
# from ..filters import equalizer
#
# 无论是隐式的还是显式的相对导入都是从当前模块开始的。主模块的名字永远是"__main__"，一个Python应用程序的主模块，应当总是使用绝对路径引用。
#
# 包还提供一个额外的属性__path__。这是一个目录列表，里面每一个包含的目录都有为这个包服务的__init__.py，你得在其他__init__.py被执行前定义哦。可以修改这个变量，用来影响包含在包里面的模块和子包。
#
# 这个功能并不常用，一般用来扩展包里面的模块。