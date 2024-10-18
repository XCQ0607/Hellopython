import math
import random


def demonstrate_number_operations():
    # 基本算术运算
    print("基本算术运算:")
    a, b = 10, 3
    print(f"a = {a}, b = {b}")
    print(f"{a} + {b} = {a + b}")  # 加法
    print(f"{a} - {b} = {a - b}")  # 减法
    print(f"{a} * {b} = {a * b}")  # 乘法
    print(f"{a} / {b} = {a / b}")  # 除法（返回浮点数）
    print(f"{a} // {b} = {a // b}")  # 整除（向下取整）
    print(f"{a} % {b} = {a % b}")  # 取余
    print(f"{a} ** {b} = {a ** b}")  # 幂运算

    # 复数运算
    c = 3 + 4j
    d = 2 - 1j
    print("\n复数运算:")
    print("C=", c, "D=", d, sep="\n")
    print("C+D=", f"({c}) + ({d}) = {c + d}")
    print("C*D=", f"({c}) * ({d}) = {c * d}")

    # 数据类型转换
    # int() ，float() ，complex()
    print("\n数据类型转换:")
    x = 3.14

    print(f"int({x}) = {int(x)}")  # 浮点数转整数
    print(f"float({a}) = {float(a)}")  # 整数转浮点数
    print(f"complex({a}, {b}) = {complex(a, b)}")  # 创建复数

    # 数学函数
    #  abs() ，ceil() ，floor() ，round() ，sqrt() ，pow()
    print("\n数学函数:")
    print(f"x={x}")
    print(f"abs(-5) = {abs(-5)}")  # 绝对值
    print(f"math.ceil({x}) = {math.ceil(x)}")  # 向上取整
    print(f"math.floor({x}) = {math.floor(x)}")  # 向下取整
    print(f"round({x}, 1) = {round(x, 1)}")  # 四舍五入到指定小数位
    print(f"math.sqrt(16) = {math.sqrt(16)}")  # 平方根
    print(f"math.pow(2, 3) = {math.pow(2, 3)}")  # 幂运算

    # 三角函数
    # sin() ，cos() ，tan()
    angle = math.pi / 4
    print("\n三角函数:")
    print(f"math.sin({angle}) = {math.sin(angle)}")
    print(f"math.cos({angle}) = {math.cos(angle)}")
    print(f"math.tan({angle}) = {math.tan(angle)}")

    # 对数和指数
    # log() ，exp()
    # 注意：math.log()函数默认以e为底，如果你需要以其他底的对数，可以使用math.log(x, base)
    print("\n对数和指数:")
    print(f"math.log(100, 10) = {math.log(100, 10)}")  # 以10为底100的对数
    print(f"math.exp(1) = {math.exp(1)}")  # e的1次方

    # 随机数
    # random.seed(42)  # 设置随机种子，以确保结果可重复
    print("\n随机数:")
    print(f"random.random() = {random.random()}")  # 0到1之间的随机浮点数
    print(f"random.randint(1, 10) = {random.randint(1, 10)}")  # 1到10之间的随机整数
    print(f"random.choice([1, 2, 3, 4, 5]) = {random.choice([1, 2, 3, 4, 5])}")  # 从列表中随机选择

    # 位运算
    # & ，| ，^ ，~ ，<< ，>>
    print("\n位运算:")
    print(f"5 & 3 = {5 & 3}")  # 按位与        # 5的二进制表示为101，3的二进制表示为011，5 & 3的结果为001，即1
    print(f"5 | 3 = {5 | 3}")  # 按位或        # 5的二进制表示为101，3的二进制表示为011，5 | 3的结果为111，即7
    print(f"5 ^ 3 = {5 ^ 3}")  # 按位异或        # 5的二进制表示为101，3的二进制表示为011，5 ^ 3的结果为110，即6
    print(f"~5 = {~5}")  # 按位取反             # 5的二进制表示为101，~5的结果为010，即2
    print(f"5 << 1 = {5 << 1}")  # 左移         # 5的二进制表示为101，左移一位后变为1010，即10
    print(f"5 >> 1 = {5 >> 1}")  # 右移         # 5的二进制表示为101，右移一位后变为10，即2

    # 左移和右移在实际中使用较少, 因为位运算的效率比四则运算要低, 而且位运算的结果也不容易理解
    # 实际运用的场景:
    print(f"5 >> 2 = {5 >> 2}")  # 右移2位, 相当于除以4

    # 比较运算符
    # == ，>=，<=，!=，<，>
    print("\n比较运算符:")
    a, b = 5, 3
    print(f"a = {a}, b = {b}")
    print(f"a>b = {a > b}")
    print(f"a<b = {a < b}")
    print(f"a>=b = {a >= b}")
    print(f"a<=b = {a <= b}")
    print(f'a!=b = {a != b}')
    print(f"a==b = {a == b}")

    # math库中高级数学函数
    # math.trunc() ，math.fabs() ，math.factorial() ，math.gcd() ，math.isclose() ，math.isfinite() ，math.isinf() ，math.isnan()
    print("\nmath库中高级数学函数:")
    print(f"math.trunc(3.14) = {math.trunc(3.14)}")  # 截断, 3.14的截断值是3,与int()函数的作用一样
    print(f"math.fabs(-5) = {math.fabs(-5)}")  # 绝对值, -5的绝对值是5
    print(f"math.factorial(5) = {math.factorial(5)}")  # 阶乘, 5! = 5 * 4 * 3 * 2 * 1 = 120
    print(f"math.gcd(12, 18) = {math.gcd(12, 18)}")  # 最大公约数, 12和18的最大公约数是6
    print(
        f"math.isclose(1.0, 1.000001, rel_tol=1e-6) = {math.isclose(1.0, 1.000001, rel_tol=1e-6)}")  # 判断两个浮点数是否接近, 1e-6表示相对误差的容忍度
    print(f"math.isfinite(1.0) = {math.isfinite(1.0)}")  # 判断一个浮点数是否有限, 1.0是有限的
    print(f"math.isinf(1.0) = {math.isinf(1.0)}")  # 判断一个浮点数是否无穷, 1.0不是无穷的
    print(f"math.isnan(1.0) = {math.isnan(1.0)}")  # 判断一个浮点数是否为NaN, 1.0不是NaN

    # 逻辑运算符
    # and ，or ，not
    print("\n逻辑运算符:")
    print(f"True and False = {True and False}")  # 逻辑与
    print(f"True or False = {True or False}")  # 逻辑或
    print(f"not True = {not True}")  # 逻辑非

    # 数学常量
    # pi ，e，inf，nan
    print("\n数学常量:")
    print(f"math.pi = {math.pi}")  # 圆周率
    print(f"math.e = {math.e}")  # 自然对数的底
    print(f"math.inf = {math.inf}")  # 正无穷大
    print(f"math.nan = {math.nan}")  # 非数字值, 用于表示无效的数学运算结果

    # 赋值运算符
    # = ，+= ，-= ，*= ，/= ，%= ，//= ，**=
    print("\n赋值运算符:")
    a = 5
    print(f"a = {a}")
    a += 3  # 等价于 a = a + 3
    print(f"a += 3 = {a}")
    a = 5
    a -= 2  # 等价于 a = a - 2
    print(f"a -= 2 = {a}")
    a = 5
    a *= 4  # 等价于 a = a * 4
    print(f"a *= 4 = {a}")
    a = 5
    a /= 2  # 等价于 a = a / 2
    print(f"a /= 2 = {a}")
    a = 5
    a %= 3  # 等价于 a = a % 3
    print(f"a %= 3 = {a}")  # 返回的是余数
    a = 5
    a //= 2  # 等价于 a = a // 2
    print(f"a //= 2 = {a}")  # 返回的是商的整数部分
    a = 5
    a **= 2  # 等价于 a = a ** 2
    print(f"a **= 2 = {a}")  # 返回的是a的2次方

    # 海象赋值运算符
    # 海象运算符 := ，可以在表达式内部同时赋值和返回值
    # 不使用海象运算符
    data = [1, 2, 3, 4, 5]
    if len(data) > 2:
        print(f"列表长度为 {len(data)}")
    # 使用海象运算符
    if (n := len(data)) > 2:  # 这里的n是一个局部变量，用于存储len(data)的值
        print(f"列表长度为 {n}")

    # 不使用海象运算符
    # while True:
    #     line = input("输入一行文本 (输入'quit'退出): ")
    #     if line == 'quit':
    #         break
    #     print(f"你输入了: {line}")
    # 使用海象运算符
    # while (line := input("输入一行文本 (输入'quit'退出): ")) != 'quit':
    #     print(f"你输入了: {line}")

    # 不使用海象运算符
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"原始列表: {numbers}")
    squared = [n ** 2 for n in numbers if n % 2 == 0]  # 这里的square是一个局部变量，用于存储n ** 2的值
    # 意思是遍历numbers中的每一个元素，n是一个局部变量，用于存储numbers中的每一个元素的值
    print(f"能被2整除的数的平方: {squared}")
    # 使用海象运算符
    squared = [square for n in numbers if (square := n ** 2) > 10]

    import re
    text = "Python 3.8 introduced the walrus operator"
    # 不使用海象运算符
    match = re.search(r'Python (\d+\.\d+)', text)       #r表示原始字符串，\d表示数字，+表示匹配一次或多次，\.表示匹配小数点，\d表示数字
    if match:
        version = match.group(1)
        print(f"Python version: {version}")
    # 使用海象运算符
    if match := re.search(r'Python (\d+\.\d+)', text):
        print(f"Python version: {match.group(1)}")

    # 成员运算符
    # in ，not in
    print("\n成员运算符:")
    print(f"5 in [1, 2, 3, 4, 5] = {5 in [1, 2, 3, 4, 5]}")  # 成员运算符
    print(f"5 not in [1, 2, 3, 4, 5] = {5 not in [1, 2, 3, 4, 5]}")  # 非成员运算符

    # 身份运算符
    # is，is not
    print('\n身份运算符:')
    # 创建一个原始列表
    a = [1, 2, 3]
    print("原始列表 a:", a)
    # 通过赋值创建 b，b 和 a 引用同一个列表对象
    b = a
    print("\nb=a赋值后:")
    print("a:", a)
    print("b:", b)
    # 使用 'is' 检查 a 和 b 是否是同一个对象
    print("b is a:", b is a)
    # 使用 '==' 检查 a 和 b 的值是否相等
    print("b == a:", b == a)
    # 使用切片操作创建 a 的浅拷贝
    b = a[:]
    print("\nb=a[:]浅拷贝后:")
    print("a:", a)
    print("b:", b)
    # 再次检查 a 和 b 是否是同一个对象
    print("b is a:", b is a)
    # 检查 a 和 b 的值是否仍然相等
    print("b == a:", b == a)
    # 修改 b 中的一个元素
    b[0] = 100
    print("\n修改 b[0] 后:")
    print("a:", a)
    print("b:", b)

    # 创建一个包含可变对象（列表）的列表
    nested_a = [1, [2, 3], 4]
    nested_b = nested_a[:]
    print("\n嵌套列表浅拷贝:")
    print("nested_a:", nested_a)
    print("nested_b:", nested_b)

    # 修改嵌套列表中的元素
    nested_b[1][0] = 200
    print("\n修改嵌套列表中的元素 nested_b[1][0] 后:")
    print("nested_a:", nested_a)
    print("nested_b:", nested_b)

    #修改列表中的元素
    nested_b[0] = 300
    print("\n修改列表中的元素 nested_b[0] 后:")
    print("nested_a:", nested_a)
    print("nested_b:", nested_b)

    #浅拷贝后只会拷贝外层嵌套，内层嵌套依然引用相同列表
    print('----------------------------')
    nested_a0 = [1, [2, 3], 4]
    nested_b0 = nested_a0[:]
    print("初始状态(b=a[:]:")
    print("nested_a0:", nested_a0)
    print("nested_b0:", nested_b0)

    print("\n内层嵌套[1]ID 比较:")
    print("nested_a0[1] 的 ID:", id(nested_a0[1]))
    print("nested_b0[1] 的 ID:", id(nested_b0[1]))

    nested_b0[0] = 200

    print("\n修改后:")
    print("nested_a0:", nested_a0)
    print("nested_b0:", nested_b0)

    print("\n内层嵌套[1]ID 比较:")
    print("nested_a0[1] 的 ID:", id(nested_a0[1]))
    print("nested_b0[1] 的 ID:", id(nested_b0[1]))

if __name__ == "__main__":
    # 确保在直接运行脚本时执行(即不是导入时执行)
    # 这里的__name__是一个特殊变量，用于表示当前模块的名称。
    demonstrate_number_operations()

    # 在Python中，切片操作[:]是一种非常强大和灵活的方式来访问序列（如列表、字符串、元组）的部分元素。它的基本语法是[start:stop:step]，其中每个参数都是可选的。让我详细解释一下：
    # 基本语法：sequence[start:stop:step]
    # 1.基本用法：
    # my_list = [0, 1, 2, 3, 4, 5]
    # print(my_list[2:4])  # 输出: [2, 3]
    # 2.省略参数：
    # my_list[:]创建整个列表的浅拷贝
    # my_list[:4]从开始到索引4（不包括）
    # my_list[2:]从索引2到结束
    # 3.使用负索引：
    # print(my_list[-3:])  # 输出: [3, 4, 5]
    # print(my_list[:-2])  # 输出: [0, 1, 2, 3]
    # 4.使用步长：
    # print(my_list[::2])  # 输出: [0, 2, 4]
    # print(my_list[::-1])  # 输出: [5, 4, 3, 2, 1, 0] (反转列表)
    # 5.在字符串中使用：
    # text = "Hello, World!"
    # print(text[7:])  # 输出: "World!"
    # print(text[::-1])  # 输出: "!dlroW ,olleH" (反转字符串)
    # 6.用于创建浅拷贝：
    # original = [1, 2, 3]
    # copy = original[:]
    # 7.修改列表：
    # my_list = [0, 1, 2, 3, 4, 5]
    # my_list[1:4] = [10, 20, 30]
    # print(my_list)  # 输出: [0, 10, 20, 30, 4, 5]
    # 8.删除元素：
    # my_list = [0, 1, 2, 3, 4, 5]
    # del my_list[2:4]
    # print(my_list)  # 输出: [0, 1, 4, 5]