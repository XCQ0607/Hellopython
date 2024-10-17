#end参数

# 创建进度条
import time

# #进度条原理：   \r  回到行首，  end=""  不换行，range(101)  0-100,sleep(0.1)每次循环停顿0.1秒
# for i in range(101):
#     print(f"\rProgress: {i}%", end="")
#     time.sleep(0.1)
#
# print('\n')

# 构建复杂的多行字符串
def draw_triangle(n):
    for i in range(1, n + 1):     # 控制行数,包含1，不包含n+1
        print("*" * i, end="")
        print()


draw_triangle(5)
# 输出:
# *
# **
# ***
# ****
# *****

# 在同一行打印多个元素
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num, end=" ")
# 输出: 1 2 3 4 5

#sep参数

# 用于构建文件路径
parts = ["C:", "Users", "Username", "Documents", "file.txt"]
path = print(*parts, sep="\\")  # 输出: C:\Users\Username\Documents\file.txt
#这里的*parts表示将parts列表中的元素作为参数传递给print函数，这里sep虽然是\\但是在print函数中会被自动替换为\,前一个\是转义字符，后一个\是普通字符


# 格式化输出表格
data = [
    ("John", 25, "New York"),
    ("Alice", 30, "London"),
    ("Bob", 35, "Paris")
]

for name, age, city in data:
    print(name, age, city, sep=" | ")

# 输出:
# John | 25 | New York
# Alice | 30 | London
# Bob | 35 | Paris

# -----------------------------------

# 转义字符
# \n：换行
# \t：水平制表符（Tab键）
# \r：回车（回到行首）
# \b：退格（Backspace）
# \f：换页（即将光标移到下一页，控制台上表现为所有内容都被清除，但光标位置不变）
# '：单引号
# "：双引号
# \：反斜杠
# \a：响铃
# \v：垂直制表符
# \ooo：八进制数，o代表0~7的字符
# \xhh：十六进制数，h代表0~9或a~f的字符



# 根据以上文档跟我请详细列举说明这些函数的用法。要有详细的代码示例以展现这些参量最大使用场景与最大功能，整合到一个代码示例中，且在控制台要清晰显示这些函数用法