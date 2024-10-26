# 全局变量
x = 0
y = 'global'


def outer_function():
    x = 1  # 外层函数的局部变量
    y = 'outer'  # 外层函数的局部变量

    print(f"在outer_function中 - x: {x}, y: {y}")

    def middle_function():
        # 使用nonlocal关键字访问外层函数的变量
        nonlocal x
        x = 2  # 修改外层函数的x
        y = 'middle'  # 中层函数的局部变量

        print(f"在middle_function中 - x: {x}, y: {y}")

        def inner_function():
            # 使用global关键字访问全局变量
            global x
            x = 3  # 修改全局变量x
            nonlocal y  # 访问中层函数的y
            y = 'inner'  # 修改中层函数的y
            z = 'local to inner'  # 内层函数的局部变量

            print(f"在inner_function中 - x: {x}, y: {y}, z: {z}")

        inner_function()
        print(f"inner_function之后 - x: {x}, y: {y}")

    middle_function()
    print(f"middle_function之后 - x: {x}, y: {y}")


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

    print("\nouter_function之后:")
    print(f"x: {x}, y: {y}")

    print("\n演示类和实例变量:")
    obj = ExampleClass()
    obj.method()

    print("\n演示内置命名空间:")
    demonstrate_builtins()

    print("\n从不同作用域访问变量:")
    z = '全局z'


    def scope_test():
        z = '局部z'
        print(f"局部z: {z}")
        print(f"全局y: {y}")  # 访问全局y
        print(f"内置函数id: {id(z)}")  # 使用内置函数


    scope_test()
    print(f"全局z: {z}")