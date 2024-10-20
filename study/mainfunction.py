# 导入需要的模块
import math
from functools import partial


# 1. 基本函数定义
def greet(name):
    """
    基本函数,带一个必选参数
    """
    print(f"你好, {name}!")


# 2. 带默认参数的函数
def power(x, n=2):
    """
    计算x的n次方,n默认为2
    """
    return x ** n


# 3. 可变参数函数
def sum_numbers(*args):
    """
    计算传入的所有数字的和
    """
    return sum(args)


# 4. 关键字参数函数
def person_info(**kwargs):
    """
    打印人物信息
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# 5. 混合参数函数
def mixed_params(name, *args, age=30, **kwargs):        # 可变参数必须在关键字参数之前,否则会报错  这里的age=30是一个关键字参数，表示默认值为30
    """
    混合使用各种参数类型
    """
    print(f"姓名: {name}")
    print(f"年龄: {age}")
    print("其他信息:")  #args是一个元组，kwargs是一个字典
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# 6. 返回多个值的函数
def circle_calc(radius):
    """
    计算圆的周长和面积
    """
    circumference = 2 * math.pi * radius        # 圆的周长
    area = math.pi * radius ** 2                # 圆的面积
    return circumference, area


# 7. 嵌套函数(闭包)
def outer(x):
    """
    外部函数
    """

    def inner(y):
        """
        内部函数
        """
        return x + y

    return inner


# 8. 装饰器函数
def logging_decorator(func):
    """
    记录函数调用的装饰器
    """

    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        return func(*args, **kwargs)

    # func是被装饰的函数，args和kwargs是传递给被装饰函数的参数。wrapper函数先打印一条日志信息，然后调用func(*args, **kwargs)来执行被装饰的函数，并返回其结果。
    return wrapper
# 当你调用 add 函数时，Python 解释器会先查找是否有装饰器应用在 add 函数上。
# 由于 add 函数被 @logging_decorator 装饰，Python 解释器会先执行 logging_decorator 函数，并将 add 函数作为参数传递给它。
# logging_decorator 函数会返回一个新的函数 wrapper，这个 wrapper 函数包含了原 add 函数的功能，以及额外的日志记录功能。
# Python 解释器会调用 wrapper 函数，而不是直接调用原 add 函数。wrapper 函数会先打印一条日志信息，然后再调用原 add 函数并返回其结果。

@logging_decorator    # 装饰器，装饰器函数执行代码流程：先执行装饰器函数，再执行被装饰的函数
def add(a, b):
    """
    被装饰的加法函数
    """
    return a + b
    # 虽然在wrapper函数的定义中没有直接看到add函数的调用，但实际上add函数是在return func(*args, **kwargs)这一行被调用的。

# 9. lambda函数     作用是定义一个匿名函数，不需要显式地定义函数名，通常用于简单的、一次性的函数
square = lambda x: x ** 2    # 定义一个lambda函数，x是参数，x**2是返回值，参数类型是int，返回值类型是int

# 10. 偏函数   作用是将一个函数的某些参数固定住，返回一个新的函数，调用这个新函数时，只需要传入新的参数即可
cube = partial(power, n=3)    # 定义一个偏函数，power函数的n参数默认值为3


# 主函数
def main():
    print("1. 基本函数调用:")
    greet("张三")

    print("\n2. 默认参数函数:")
    print(f"2的平方: {power(2)}")
    print(f"2的3次方: {power(2, 3)}")

    print("\n3. 可变参数函数:")
    print(f"1+2+3的和: {sum_numbers(1, 2, 3)}")
    print(f"4+5+6+7的和: {sum_numbers(4, 5, 6, 7)}")

    print("\n4. 关键字参数函数:")
    person_info(name="李四", age=25, city="北京")

    print("\n5. 混合参数函数:")
    mixed_params("王五", "学生", "男", age=22, major="计算机科学")

    print("\n6. 返回多个值的函数:")
    circ, area = circle_calc(5)
    print(f"半径为5的圆, 周长: {circ:.2f}, 面积: {area:.2f}")

    print("\n7. 闭包函数:")
    add_5 = outer(5)
    print(f"5 + 3 = {add_5(3)}")

    print("\n8. 装饰器函数:")
    print(f"3 + 4 = {add(3, 4)}")   #这里的add函数是被装饰的函数，add函数的参数是a和b，a和b的类型是int，返回值类型是int

    print("\n9. Lambda函数:")
    print(f"4的平方: {square(6)}") #调用lambda函数

    print("\n10. 偏函数:")
    print(f"2的立方: {cube(2)}")


if __name__ == "__main__":
    main()

