print('爸!!!', end='')
print('妈!!!')

import sys;

x = 'XCQ';
sys.stdout.write(x + '\n')

str1 = '123456789'

print(str1)  # 输出字符串
print(str1[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str1[1:-1])  # 输出第二个到倒数第二个的所有字符
print(str1[-2:-1])  # 输出倒数第二个字符
print(str1[3::-1])  # 输出字符串的逆序
print(str1[0])  # 输出字符串第一个字符
print(str1[2:5])  # 输出从第三个开始到第六个的字符（不包含）
print(str1[2:])  # 输出从第三个开始后的所有字符
print(str1[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str1 * 2)  # 输出字符串两次
print(str1 + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

import keyword

print(keyword.kwlist)   # 输出所有关键字

import math

result = math.sqrt(16)
print(result)  # 输出 4.0

from math import sqrt

result = sqrt(16)
print(result)  # 输出 4.0

import OSdemo

current_directory = os.getcwd()
print(current_directory)  # 输出当前工作目录

from datetime import date

today = date.today()
print(today)  # 输出当前日期

a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))


class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))   #意思是A()是A类的实例对象，是True
print(type(A()) == A)
print(isinstance(B(), A))   #意思是B()是A类的实例对象，是False
print(type(B()) == A)

print('------------------------------------')

print(True == 1)
print(1 is True)
del str1
if 'str1' in locals():
    print(str1 == 0)
else:
    print("str1 is not defined")

print(5 + 4)  # 加法
print(4.3 - 2)  # 减法
print(3 * 7)  # 乘法
print(2 / 4)  # 除法，得到一个浮点数
print(2 // 4)  # 除法，得到一个整数
print(17 % 3)  # 取余
print(2 ** 5)  # 乘方

print("这是一个很长的字符串，需要分成两行显示"
      "\t这是第二行")

print("""这是一个很长的字符串，
需要分成两行显示""")

word = 'Python'
print(word[0], word[5])  # 输出: P n
print(word[-1], word[-6])  # 输出: n P
# wrong:word[0] = 'm'

# 布尔类型的值和类型
a = True
b = False
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>

# 布尔类型的整数表现
print(int(True))  # 1
print(int(False))  # 0

# 使用 bool() 函数进行转换
print(bool(0))  # False
print(bool(42))  # True
print(bool(''))  # False
print(bool('Python'))  # True
print(bool([]))  # False
print(bool([1, 2, 3]))  # True
# 在 Python 中，所有非零的数字和非空的字符串、列表、元组等数据类型都被视为 True，只有 0、空字符串、空列表、空元组等被视为 False。因此，在进行布尔类型转换时，需要注意数据类型的真假性。


# 布尔逻辑运算
print(True and False)  # False
print(True or False)  # True
print(not True)  # False

# 布尔比较运算
print(5 > 3)  # True
print(2 == 2)  # True
print(7 < 4)  # False

# 布尔值在控制流中的应用
if True:
    print("This will always print")

if not False:
    print("This will also always print")

x = 10
if x:
    print("x is non-zero and thus True in a boolean context")


def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list01 = [1,2,3,4],
    # list01[0]=1, list01[1]=2 ，而 -1 表示最后一个元素 list01[-1]=4 ( 与 list01[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output


# default_input = 'I like runoob'
# user_input = input("请输入一个句子（直接回车将使用默认句子）：")
# if user_input:
#   rw = reverseWords(user_input)
# else:
#     rw = reverseWords(default_input)
#     print(rw)


list0 = [1, 2, 3, 4]
tuple0 = (999, list0)
print(list0, tuple0)
# tuple[0]=111   # 元组中的元素值是不允许修改的，但我们可以对元组中的列表的元素进行修改。
tuple0[1][2] = 33
print(list0, tuple0)
tup2 = ('stop',)
tup3 = (3,)
tup4 = (4)
print(type(tup2), type(tup3), type(tup4))
print(tup2, tup3, tup4)
# 如果tup3不加,的话，会被当作一个数，而不是元组，而括号会被理解为一个运算符。

# 1、与字符串一样，元组的元素不能修改。
# 2、元组也可以被索引和切片，方法一样。
# 3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
# 4、元组也可以使用 + 操作符进行拼接。

# 4的示例
tup1 = ('a', 'b', 'c', 'd')
tup2 = (1, 2, 3, 4)
tup3 = tup1 + tup2
print(tup3)  # 输出：('a', 'b', 'c', 'd', 1, 2, 3, 4)

# Python 中的集合（Set）是一种无序、可变的数据类型，用于存储唯一的元素。
# 集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。
# 在 Python 中，集合使用大括号 {} 表示，元素之间用逗号 , 分隔。
# 另外，也可以使用 set() 函数创建集合。

# 集合的定义

# 创建一个空集合
set1 = set()
print(set1)  # 输出：set()
# 输出为set()是因为在 Python 中，空集合用 set() 表示，而不是 {}。
# 在Python中，空字典用{}表示，空列表用[]表示，空元组用()表示，空字符串用''表示，空集合用set()（不是{}括号）表示
'''
集合中的元素必须是不可变（immutable）的。这意味着集合可以包含的元素类型有限制。
可以包含的元素类型：
数字（整数、浮点数）
字符串
元组（只包含不可变元素的元组）
布尔值
frozenset（不可变集合）
集合中的元素是无序的，无法通过索引访问元素。
'''

# 创建一个包含元素的集合
set2 = {1, 2, 3, 4, 5}
print(set2)  # 输出：{1, 2, 3, 4, 5}

# 创建一个包含重复元素的集合
set3 = {1, 2, 2, 3, 4, 4, 5}
print(set3)  # 输出：{1, 2, 3, 4, 5}

# 使用 set() 函数创建集合
list1 = [1, 2, 3, 4, 5, 5]
set4 = set(list1)
print(set4)  # 输出：{1, 2, 3, 4, 5}

# 集合的基本操作
set5 = {1, 2, 3, 4, 5}
set5.add(6)  # 添加元素
print(set5)  # 输出：{1, 2, 3, 4, 5, 6}
set5.remove(3)  # 删除元素
print(set5)  # 输出：{1, 2, 4, 5, 6}
# 集合的常用方法
set6 = {1, 2, 3, 4, 5}
print(len(set6))  # 输出：5
print(1 in set6)  # 输出：True
print(6 in set6)  # 输出：False
set6.clear()  # 清空集合
print(set6)  # 输出：set()
# 集合的常用方法
set7 = {1, 2, 3, 4, 5}
set8 = {4, 5, 6, 7, 8}
print(set7.union(set8))  # 并集, 输出：{1, 2, 3, 4, 5, 6, 7, 8}，即set7和set8中的所有元素
print(set7.intersection(set8))  # 交集, 输出：{4, 5}，即set7和set8中都存在的元素
print(set7.difference(set8))  # 差集, 输出：{1, 2, 3}，即set7中有，set8中没有的元素
print(set7.symmetric_difference(set8))  # 对称差集, 输出：{1, 2, 3, 6, 7, 8}，即set7和set8中不同时存在的元素
print(set7.issubset(set8))  # 判断 set7 是否是 set8 的子集, 输出：False
print(set7.issuperset(
    set8))  # 判断 set7 是否是 set8 的超集, 输出：False，超集指的是包含关系，如:{1,2,3}是{1,2,3,4,5}的超集，而{1,2,3,4,5}不是{1,2,3}的超集。
print(set7.isdisjoint(set8))  # 判断 set7 和 set8 是否不相交, 输出：False

# 超集的详细介绍
# 在数学中，集合的超集是指包含原集合所有元素的集合。
# 例如，集合A={1,2,3}，集合B={1,2,3,4,5}，集合B是集合A的超集，因为集合B包含了集合A的所有元素。也可以称为集合B是集合A的扩展，集合A是集合B的子集。

set9 = {1, 2, 3, 4, 5}
set10 = {1, 2, 3, 4, 5, 6, 7}
set9.update(set10)  # 将 set10 的元素添加到 set9 中
print(set9)  # 输出：{1, 2, 3, 4, 5 ，6，7}

# 以下是更为简单的方法
a = set('abracadabra')
b = set('alacazam')
# set中一共有12个元素，而不是1个。''围起来的是字符串，字符串是由字符组成的，而字符是由单个字符组成的。每个字符都是一个元素。
print(a)
print(a - b)  # a 和 b 的差集    #输出：{'r', 'd', 'b'}
print(a | b)  # a 和 b 的并集    #输出：{'a', 'c', 'b', 'r', 'd','m', 'z', 'l'}
print(a & b)  # a 和 b 的交集    #输出：{'a', 'c'}
print(a ^ b)  # a 和 b 中不同时存在的元素  #输出：{'r', 'b', 'd'}

# 这里的-，|，&，^都是集合的运算符，等同于上面的difference，union，intersection，symmetric_difference方法。

# 直接添加字符串：整个字符串被视为一个元素。
# 使用 set() 构造函数：字符串被拆分成单个字符。
s1 = {'hello'}
print(s1)  # 输出: {'hello'}
print(len(s1))  # 输出: 1

# 使用集合构造方法，字符串被拆分成单个字符
s2 = set('hello')
print(s2)  # 输出: {'h', 'e', 'l', 'o'}
print(len(s2))  # 输出: 4 (注意 'l' 只出现一次，因为集合中元素是唯一的)

# 集合的遍历
s = {'apple', 'banana', 'orange'}
print(s)
for item in s:
    print(item)
print('---------------------------------')

dict1 = {}
dict1['one'] = "1 - 菜鸟教程"
dict1[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict1)
print(dict1['one'])  # 输出键为 'one' 的值
print(dict1[2])  # 输出键为 2 的值

print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

# 高级输入字典方法
dict1 = {x: x ** 2 for x in (2, 4, 6)}
print(dict1)
dict2 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(type(dict2))  # 输出：<class 'dict'>
print(dict2)
# print(['test']+dict2)   #print函数内输出的内容必需是同种类型，这里['test']是列表类型，dict2是元组类型，两者类型不同，不能相加。


# dict3 = dict(dict2)
# #意思是把dict2转换成字典，dict2类型可以是列表，元组，字典

# 元组（tuple）：使用圆括号 () 来定义，例如 (1, 2, 3)。元组是不可变的，这意味着一旦创建，其元素就不能被更改。
# 字典（dictionary）：使用花括号 {} 来定义，例如 {'a': 1, 'b': 2, 'c': 3}。字典是可变的，但是字典的键（key）必须是不可变的，而值（value）可以是任意类型。
# 集合（set）：使用花括号 {} 来定义，但是与字典不同的是，集合中只包含元素，而没有键值对。例如 {1, 2, 3}。集合是可变的，但是集合中的元素必须是不可变的。
# 列表（list01）：使用方括号 [] 来定义，例如 [1, 2, 3]。列表是可变的，这意味着你可以添加、删除或修改列表中的元素。


# bytes 类型
# bytes 类型是不可变的字节序列，通常用于存储二进制数据。它可以通过两种方式创建：
# 使用 b 前缀来表示字节字符串，例如 b"hello"。
# 使用 bytes() 函数来创建字节对象，例如 bytes("hello", "utf-8")。#默认是utf-8编码，还有其他编码，如gbk，gb2312，ascii等。
# 编码的影响是1.在不同的编码下，一个字符的字节数是不同的。2.不同编码在控制台中显示的是不同的字符。
# 以下是一些示例：
print(ord('a'))
x = b"hello"
for i in range(len(x)):  # 遍历字节串,range函数返回一个可迭代的对象，从0开始，到len(x)结束，不包括len(x)
    print(f"The element is '{chr(x[i])}'")

# -----------------------类型转换----------------------
# bool(x)
print(bool(0))  # False
# int(x [,base])    #其中x可以是数字或者字符串，base表示进制，默认为10进制。base表示x的进制数，用int类型将其转换为10进制的整数。
print(int("123"))  # 字符串转整数：123
print(int("1010", 2))  # 二进制字符串转整数：10
print(int("FF", 16))  # 十六进制字符串转整数：255
print(int(5.7))  # 浮点数转整数：5
# float(x)
print(float("3.14"))  # 字符串转浮点数：3.14
print(float("1e-3"))  # 科学计数法字符串转浮点数：0.001
print(float(5))  # 整数转浮点数：5.0
# complex(real [,imag])
print(complex(1, 2))  # 1+2j
print(complex("1+2j"))  # 字符串转复数：(1+2j) #注意，这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
print(complex(3))  # 只有实部：(3+0j)
# str(x)      函数返回一个对象的 string 格式
print(str(123))  # 整数转字符串：'123'
print(str([1, 2, 3]))  # 列表转字符串：'[1, 2, 3]'
print(str({'a': 1, 'b': 2}))  # 字典转字符串："{'a': 1, 'b': 2}"

print('---------------------------------')
# repr(x)     函数返回一个对象的 string 格式,与str()函数的区别在于，str()函数返回一个用户易读的字符串，而repr()函数返回一个开发者易读的字符串。
# 比如：repr()函数返回的字符串可以直接用于eval()函数，而str()函数返回的字符串不能直接用于eval()函数。
# 简单字符串
s = "Hello, World!"
print(str(s))  # 输出: Hello, World!
print(repr(s))  # 输出: 'Hello, World!'
# 包含特殊字符的字符串
s = "Hello\nWorld"
print(str(s))  # 输出: Hello
#       World
print(repr(s))  # 输出: 'Hello\nWorld'
# 列表
lst = [1, 2, 3]
print(str(lst))  # 输出: [1, 2, 3]
print(repr(lst))  # 输出: [1, 2, 3]
# 元组
tpl = (1, 2, 3)
print(str(tpl))  # 输出: (1, 2, 3)
print(repr(tpl))  # 输出: (1, 2, 3)
# 字典
dct = {'a': 1, 'b': 2}
print(str(dct))  # 输出: {'a': 1, 'b': 2}
print(repr(dct))  # 输出: {'a': 1, 'b': 2}
# 日期时间对象
import datetime

d = datetime.datetime(2023, 1, 1, 12, 0)
print(str(d))  # 输出: 2023-01-01 12:00:00
print(repr(d))  # 输出: datetime.datetime(2023, 1, 1, 12, 0)


# 自定义对象
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"


p = Person("Alice", 30)
print(str(p))  # 输出: Alice, 30 years old
print(repr(p))  # 输出: Person('Alice', 30)

print('-------------------------------------')

# eval(str) 函数用于计算字符串中的有效 Python 表达式，并返回计算结果。
print(eval("1 + 2"))  # 3
print(eval("'Hello' + ' World'"))  # 'Hello World'
print(eval("[1, 2, 3] + [4, 5]"))  # [1, 2, 3, 4, 5]
x = 1
print(eval("x + 1"))  # 2
# 注意，eval()函数的参数必须是一个有效的 Python 表达式，否则会引发 SyntaxError 异常。
namespace = {"x": 3, "y": 2}
print(eval("x + y", namespace))  # 5
# 注意，eval()函数的第二个参数是一个可选的命名空间字典，用于指定变量的作用域。如果不提供命名空间字典，eval()函数将使用全局命名空间。
# tuple(s) 函数用于将序列（如列表、元组、字符串等）转换为元组。
print('-------------------------------------')
print(tuple([1, 2, 3]))  # (1, 2, 3)
print(tuple("abc"))  # ('a', 'b', 'c')
print(tuple({1, 2, 3}))  # (1, 2, 3)
print('-------------------------------------')
# list01(s) 函数用于将序列（如列表、元组、字符串等）转换为列表。
list1 = list((123, 'Google', 'Runoob', 'Taobao'))
print("列表元素 : ", list1)
list2 = list("Hello World")  # 使用list会将字符串拆分成单个字符
print("列表元素 : ", list2)
print('-------------------------------------')
# set(s) 函数用于将序列（如列表、元组、字符串等）转换为集合。
print(set([1, 2, 2, 3]))  # {1, 2, 3}
print(set("hello"))  # {'h', 'e', 'l', 'o'}
print(set((1, 2, 3, 1)))  # {1, 2, 3}
print('-------------------------------------')
# dict(d) 函数用于创建一个字典。
print(dict([('a', 1), ('b', 2)]))  # {'a': 1, 'b': 2}   # 可迭代对象方式来构造字典
print(dict(a=1, b=2))  # {'a': 1, 'b': 2}    # 关键字参数方式来构造字典
print(dict(zip(['a', 'b'], [1, 2])))  # {'a': 1, 'b': 2}    # 映射函数方式来构造字典
print(dict([('x', 5), ('y', -5)], z=8))  # {'x': 5, 'y': -5, 'z': 8}    # 可迭代对象方式来构造字典，同时添加一个新的键值对
print('-------------------------------------')
# bin(x) 函数用于将一个整数转换为对应的二进制字符串。
print(bin(10))  # '0b1010'
print(bin(-5))  # '-0b101'
print('-------------------------------------')
# frozenset(s) 函数用于创建一个不可变的集合。
print(frozenset([1, 2, 2, 3]))  # frozenset({1, 2, 3})
print(frozenset("hello"))  # frozenset({'h', 'e', 'l', 'o'})
# 生成一个新的不可变集合
a = frozenset(range(
    10))  # 生成一个包含 0 到 9 的不可变集合，range 函数用于生成一个整数序列，其可传入参数有：起始值、结束值、步长。如：range(1, 10, 2) 表示生成一个包含 1、3、5、7、9 的不可变集合。默认的起始值为 0，步长为 1。
print(a)  # 输出: frozenset([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# 创建不可变集合
b = frozenset('runoob')
print(b)  # 输出: frozenset(['b', 'r', 'u', 'o', 'n'])
print('-------------------------------------')
# chr(x) 函数用于将一个整数转换为对应的 ASCII 字符。
print(int(0x30))  # 48
print(chr(0x30))  # 0
print(chr(65))  # 'A'
print(chr(97))  # 'a'
print(chr(8364))  # '€'
# 0的ASCII码为48，A的ASCII码为65，a的ASCII码为97
print('-------------------------------------')
# ord(x) 函数用于将一个字符转换为对应的 ASCII 码。
print(ord('A'))  # 65
print(ord('a'))  # 97
print(ord('€'))  # 8364
print('-------------------------------------')
# hex(x) 函数用于将一个整数转换为对应的十六进制字符串。
print(hex(255))  # '0xff'
print(hex(-42))  # '-0x2a'
print(hex(3735928559))  # '0xdeadbeef'
print('-------------------------------------')
# oct(x) 函数用于将一个整数转换为对应的八进制字符串。
print(oct(8))  # '0o10'
print(oct(-56))  # '-0o70'
print(oct(100))  # '0o144'

'''
ssh -T git@github.com
git init
git add .
git config --global http.sslVerify "false"
git config --global --unset http.proxy 
git config --global --unset https.proxy 
git push origin master
'''

# 元组 (Tuple)：使用圆括号 ()
# 例如：(1, 2, 3)
#
# 集合 (Set)：使用花括号 {}
# 例如：{1, 2, 3}
# 注意：空集合要用 set() 创建，因为 {} 表示空字典
#
# 列表 (List)：使用方括号 []
# 例如：[1, 2, 3]
#
# 字典 (Dictionary)：使用花括号 {}，但内部是键值对
# 例如：{"a": 1, "b": 2, "c": 3}