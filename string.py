import datetime

# 字符串格式化方法
# 1. %操作符（旧式字符串格式化）
# name, age = "Alice", 30
# print("1. %操作符: My name is %s and I'm %d years old." % (name, age))

# 2. str.format()方法
pi = 3.14159
print("2. str.format(): Pi is approximately {:.2f}".format(pi))

# 3. f-strings（格式化字符串字面值）
x, y = 10, 20
print(f"3. f-strings: The sum of {x} and {y} is {x + y}")

# 4. 指定宽度和对齐
value = 42
print("4. 宽度和对齐: |{:<5d}|{:>5d}|{:^5d}|".format(value, value, value))   #^5d 是一个格式化说明符，用于指定字符串的对齐方式和宽度。

# 5. 数字格式化
large_number = 1234567890
print(f"5. 数字格式化: {large_number:,}")

# 6. 日期格式化
now = datetime.datetime.now()
print(f"6. 日期格式化: Current date: {now:%Y-%m-%d}")

# 7. 条件表达式in f-strings
x = 5
print(f"7. 条件表达式: x is {'positive' if x > 0 else 'non-positive'}")

# 8. 使用=显示表达式及其值 (Python 3.8+)
y = 10
print(f"8. 显示表达式及值: {y=}")

# 9. 访问对象属性
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Eve", 28)
print("9. 访问对象属性: This is {0.name}, aged {0.age}.".format(p))

# 10. 使用字典
person = {"name": "Bob", "age": 25}
print("10. 使用字典: %(name)s is %(age)d years old." % person)

print("----------------------")

#格式化说明符
# 基本数据
num = 42
num1 = -5
pi = 3.14159
big_num = 1234567890
small_num = 0.00123
neg_num = -42
name = "Alice"
now = datetime.datetime.now()

print("1. 整数格式化:")
print(f"  默认:    {num:d}")
print(f"  填充右对齐: {num:5d}")     #默认是右对齐，相当于{num:>5d}"
print(f"  填充左对齐: {num:<5d}")
print(f"  填充居中:  {num:^5d}")
print(f"  零填充:   {num:05d}")
print(f"  正数带符号:   {num:+d}")
print(f"  负数带符号:    {neg_num:d}")

print("\n2. 浮点数格式化:")
print(f"  默认:    {pi:f}")   # 保留6位小数
print(f"  保留小数: {pi:.2f}")   # 保留2位小数
print(f"  科学计数: {pi:e}")    # 科学计数法表示
print(f"  百分比:   {pi:%}")   # 百分比表示
print(f"  宽度和精度: {pi:8.3f}")    # 宽度为8，保留3位小数，右对齐

print("\n3. 字符串格式化:")
print(f"  默认:    {name:s}")   # 默认左对齐
print(f"  右对齐:   {name:>10s}")
print(f"  左对齐:   {name:10s}")       #相当于{name:<10s}"
print(f"  居中:    {name:^10s}")

print("\n4. 数字的千位分隔:")
print(f"  带逗号:   {big_num:,}")
print(f"  带下划线: {big_num:_}")

print("\n5. 进制转换:")
print(f"  二进制:   {num:b}")  #bin()函数将一个整数转换为二进制字符串，用{bin(num)}将输出结果：0b1010，0b表示二进制
print(f"  八进制:   {num:o}")  #oct()函数将一个整数转换为八进制字符串,用{oct(num)}将输出结果：0o1010，0o表示八进制
print(f"  十六进制(小写): {num:x}")
print(f"  十六进制(大写): {num:X}")

print("\n6. 日期和时间格式化:")
print(f"  年-月-日:     {now:%Y-%m-%d}")
print(f"  时:分:秒:     {now:%H:%M:%S}")
print(f"  完整日期时间:  {now:%Y-%m-%d %H:%M:%S}")
print(f"  本地化格式:    {now:%c}")  #它将输出  星期 月 日 时:分:秒 年，如果想将其改为  月/日/年 时:分:秒 星期，可以使用：{now:%x %X}
print(f"  本地化日期:    {now:%x %X}")
# %x 表示 月/日/年
# %X 表示 时:分:秒

print("\n7. 特殊格式化:")
print(f"  指数格式(小写): {small_num:.2e}")
print(f"  指数格式(大写): {small_num:.2E}")
print(f"  一般格式:      {small_num:g}")    # 它将根据数值大小自动选择使用科学计数法或一般格式
print(f"  前导符号空格:   {num: d} and {neg_num: d}") #前导符号空格指定在正数前面加上一个空格，负数前面加上一个负号

print("\n8. 复杂组合:")
print(f"  对齐+填充+宽度+精度: {pi:*^10.2f}")   # 对齐方式为居中，填充字符为*，宽度为10，精度为2。如果宽度为11，那么输出结果为：***3.14****，后边会优先多出一个*
print(f" 千位分隔+精度: {big_num:*^20,.2f}")


print("\n9. 使用`=`显示变量名和值 (Python 3.8+):")
print(f"  {num=}")
print(f"  {pi=:.2f}")

# 整数格式化：d, 5d, <5d, ^5d, 05d, +d
# 浮点数格式化：f, .2f, e, %, 8.3f
# 字符串格式化：s, >10s, <10s, ^10s
# 数字的千位分隔：,, _
# 进制转换：b, o, x, X
# 日期和时间格式化：%Y-%m-%d, %H:%M:%S, %c
# 特殊格式化：.2e, .2E, g,  d（前导空格）
# 复杂组合：*^10.2f, ,.2f
# 使用=显示变量名和值（Python 3.8+）

# 格式说明符的一般形式是：[[fill]align][sign][#][0][width][grouping_option][.precision][type]
# [[填充]对齐][符号][#][0][宽度][分组选项][.精度][类型]
# [填充]：可选，指定填充字符    如：{:*>10}
# 对齐：可选，<（左对齐），>（右对齐），^（居中对齐）
# 符号：可选，+（正数也显示加号），-（默认，只有负数显示负号），空格（正数前加空格，负数前加负号）如：{: +d}
# #：可选，对于二进制、八进制、十六进制，添加相应的前缀   如：{:b}，{:o}，{:x}，{:X}，bin(), oct(), hex()，b，o，（x，X）分别是将整数转换为二进制、八进制、十六进制的字符串，x与X区别是，x是小写，X是大写
# 0：可选，使用0填充（如果没有指定填充字符）
# 宽度：可选，指定最小字段宽度     如：{:05d}，如果[[fill]align]字段中也有指定宽度，则该宽度会被忽略
# 分组选项：可选，,（使用逗号作为千位分隔符），_（使用下划线作为千位分隔符）
# .精度：可选，对于浮点数，指定小数点后的位数；对于字符串，指定最大字符数
# 类型：指定输出的类型（如d表示十进制整数，f表示浮点数，s表示字符串等）