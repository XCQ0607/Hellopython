# 全局变量
x = 0
y = 'global'


def outer_function():
    print("\n----------------运行outer_function:----------------")
    x = 1  # 外层函数的局部变量
    y = 'outer'  # 外层函数的局部变量
    print(f"外层函数的局部变量x: {x}, y: {y}")

    print(f"在outer_function中 - x: {x}, y: {y}")

    def middle_function():  # 中层函数，运行outer_function时，会运行该函数(该函数是一个闭包)
        # 使用nonlocal关键字访问外层函数的变量
        y = 'middle'  # 中层函数的局部变量
        nonlocal x  # 访问外层函数的x
        print(f"外层x:{x}")
        x = 2  # 修改外层函数的x
        print(f"中层函数的局部变量y: {y}")
        print(f"修改后")

        print(f"在middle_function中 - x: {x}, y: {y}")

        def inner_function():       # 内层函数，运行middle_function时，会运行该函数
            # 使用global关键字访问全局变量
            z = 'local to inner'  # 内层函数的局部变量
            global x      # 访问全局变量x
            print(f"全局x:{x}")
            x = 3  # 修改全局变量x
            nonlocal y  # 访问中层函数的y
            print(f"中层y:{y}")
            print(f"内层函数的局部变量z: {z}")
            print(f"修改后")
            y = 'inner'  # 修改中层函数的y
            print(f"在inner_function中 - x: {x}, y: {y}, z: {z}")
            print("\n----------------inner_function结束----------------")

        print("\n----------------运行inner_function:----------------")
        inner_function()
        print(f"inner_function之后 - x: {x}, y: {y}")
        print("\n----------------middle_function结束----------------")

    print("\n----------------运行middle_function:----------------")
    middle_function()
    print(f"middle_function之后 - x: {x}, y: {y}")
    print("\n----------------outer_function结束----------------")
    print(f"outer_function之后 - x: {x}, y: {y}")


class ExampleClass:
    class_var = '我是类变量'

    def __init__(self):
        self.instance_var = '我是实例变量'

    def method(self):
        method_var = '我是方法变量'
        print(f"在方法中 - class_var: {self.class_var}")
        print(f"在方法中 - instance_var: {self.instance_var}")
        print(f"在方法中 - method_var: {method_var}")

        # 访问全局变量
        global y
        print(f"在方法中 - 全局变量y: {y}")


def demonstrate_builtins():
    print(f"内置函数示例 - len('hello'): {len('hello')}")
    print(f"内置常量示例 - True: {True}")


# 主程序
if __name__ == "__main__":
    print("初始全局值:")
    print(f"x: {x}, y: {y}")

    outer_function()


    print("\n演示类和实例变量:")
    obj = ExampleClass()
    obj.method()

    print("\n演示内置命名空间:")
    demonstrate_builtins()

    print("\n从不同作用域访问变量:")
    z = '全局z'


    def scope_test():    # 局部作用域
        z = '局部z'
        print(f"局部z: {z}")
        print(f"全局y: {y}")  # 访问全局y
        print(f"内置函数id: {id(z)}")  # 使用内置函数


    scope_test()
    print(f"全局z: {z}")

'''
总结
nonlocal:用于在函数或其他作用域中访问外层(非全局)变量。
global:用于在函数中访问全局变量。
若没有使用 global 或 nonlocal 关键字对局部变量进行声明，在局部作用域中，可以访问全局命名空间中的变量，不可对其进行赋值。

'''