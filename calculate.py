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
    print("C=",c,"D=",d,sep="\n")
    print("C+D=",f"({c}) + ({d}) = {c + d}")
    print("C*D=",f"({c}) * ({d}) = {c * d}")

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
    #random.seed(42)  # 设置随机种子，以确保结果可重复
    print("\n随机数:")
    print(f"random.random() = {random.random()}")  # 0到1之间的随机浮点数
    print(f"random.randint(1, 10) = {random.randint(1, 10)}")  # 1到10之间的随机整数
    print(f"random.choice([1, 2, 3, 4, 5]) = {random.choice([1, 2, 3, 4, 5])}")  # 从列表中随机选择

    # 位运算
    # & ，| ，^ ，~ ，<< ，>>
    print("\n位运算:")
    print(f"5 & 3 = {5 & 3}")  # 按位与
    print(f"5 | 3 = {5 | 3}")  # 按位或
    print(f"5 ^ 3 = {5 ^ 3}")  # 按位异或
    print(f"~5 = {~5}")  # 按位取反
    print(f"5 << 1 = {5 << 1}")  # 左移
    print(f"5 >> 1 = {5 >> 1}")  # 右移

    # 比较运算符
    # == ，>=，<=，!=，<，>
    print("\n比较运算符:")
    a, b = 5, 3
    print(f"a = {a}, b = {b}")
    print(f"a>b = {a>b}")
    print(f"a<b = {a<b}")
    print(f"a>=b = {a>=b}")
    print(f"a<=b = {a<=b}")
    print(f'a!=b = {a!=b}')
    print(f"a==b = {a==b}")

    # math库中高级数学函数
    # math.trunc() ，math.fabs() ，math.factorial() ，math.gcd() ，math.isclose() ，math.isfinite() ，math.isinf() ，math.isnan()
    print("\nmath库中高级数学函数:")
    print(f"math.trunc(3.14) = {math.trunc(3.14)}") # 截断, 3.14的截断值是3
    print(f"math.fabs(-5) = {math.fabs(-5)}") # 绝对值, -5的绝对值是5
    print(f"math.factorial(5) = {math.factorial(5)}") # 阶乘, 5! = 5 * 4 * 3 * 2 * 1 = 120
    print(f"math.gcd(12, 18) = {math.gcd(12, 18)}") # 最大公约数, 12和18的最大公约数是6
    print(f"math.isclose(1.0, 1.000001, rel_tol=1e-6) = {math.isclose(1.0, 1.000001, rel_tol=1e-6)}") # 判断两个浮点数是否接近, 1e-6表示相对误差的容忍度
    print(f"math.isfinite(1.0) = {math.isfinite(1.0)}") # 判断一个浮点数是否有限, 1.0是有限的
    print(f"math.isinf(1.0) = {math.isinf(1.0)}") # 判断一个浮点数是否无穷, 1.0不是无穷的
    print(f"math.isnan(1.0) = {math.isnan(1.0)}") # 判断一个浮点数是否为NaN, 1.0不是NaN




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
    # = ，+= ，-= ，*= ，/= ，%= ，//= ，**=，:=
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
    print(f"a %= 3 = {a}")  #返回的是余数
    a = 5
    a //= 2  # 等价于 a = a // 2
    print(f"a //= 2 = {a}")  #返回的是商的整数部分
    a = 5
    a **= 2  # 等价于 a = a ** 2
    print(f"a **= 2 = {a}")  #返回的是a的2次方
    #海象赋值运算符
    a = 5
    a := 3
    print(f"a := 3 = {a}")


if __name__ == "__main__":
# 确保在直接运行脚本时执行(即不是导入时执行)
#这里的__name__是一个特殊变量，用于表示当前模块的名称。
    demonstrate_number_operations()